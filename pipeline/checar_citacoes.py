"""Confere, por código, se o `trecho` de cada fonte está mesmo no texto da fonte.

Uso:
    python pipeline/checar_citacoes.py dados/lotes/<lote>.jsonl
    python pipeline/checar_citacoes.py dados/lotes/<lote>.jsonl --offline   # só usa o cache
    python pipeline/checar_citacoes.py --baixar URL [URL ...]              # só guarda no cache

Para cada fato, informa: ok | aproximado | falhou (motivo), e os números do gancho/explicação
que não aparecem em nenhum trecho confirmado (aviso_numero; não reprova sozinho).
Grava um relatório JSON ao lado do lote (<lote>.checagem.json), com o caminho de cada texto
baixado em dados/cache_fontes/, para o subagente verificador ler.

Códigos de saída: 0 = todos os fatos têm fonte confirmada; 1 = algum fato falhou; 2 = erro de uso.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import sys
import time
import unicodedata
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import quote, unquote, urlparse

import comum

LIMIAR_APROXIMADO = 0.90
MIN_APROXIMADO = 80          # trechos normalizados menores que isso só valem se exatos
TAMANHO_MAXIMO = 15 * 1024 * 1024
VERSAO = "0.1"


# =========================================================================== normalização

_ASPAS = {c: "'" for c in "‘’‚‛′`´"} | {c: '"' for c in "“”„‟″«»"}
_TRACOS = {c: "-" for c in "‐‑‒–—―−"}
_TABELA = str.maketrans(_ASPAS | _TRACOS)
_RE_NOTA = re.compile(
    r"\[(?:\d+|[a-z]|nota \d+|n\. \d+|citation needed|clarification needed|"
    r"carece de fontes\??|verification needed|when\?|which\?|who\?|according to whom\?)\]",
    re.IGNORECASE,
)
_RE_HIFENIZACAO = re.compile(r"(\w)-[ \t]*\r?\n[ \t]*(\w)")
_RE_HIFEN = re.compile(r"(?<=\w)-(?=\w)")
_RE_ESPACO_ANTES = re.compile(r"\s+([,.;:!?)\]}%])")
_RE_ESPACO_DEPOIS = re.compile(r"([(\[{])\s+")
_RE_ELISAO = re.compile(r"\s*(?:\[\s*\.\.\.\s*\]|\(\s*\.\.\.\s*\)|\.\.\.)\s*")


def normalizar(texto: str) -> str:
    """Normaliza para comparação: unicode, aspas, traços, hifenização, notas, caixa e espaços."""
    t = unicodedata.normalize("NFKC", texto)  # também troca nbsp/espaço fino e '…' por '...'
    t = t.replace("­", "").replace("​", "")
    t = t.translate(_TABELA)
    t = _RE_HIFENIZACAO.sub(r"\1\2", t)       # palavra hifeni-\nzada → palavrahifenizada
    t = _RE_HIFEN.sub("", t)                   # bem-vindo → bemvindo (dos dois lados, então tudo bem)
    t = _RE_NOTA.sub("", t)
    t = t.casefold()
    t = " ".join(t.split())
    t = _RE_ESPACO_ANTES.sub(r"\1", t)
    t = _RE_ESPACO_DEPOIS.sub(r"\1", t)
    return t


def fragmentos(trecho: str) -> list[str]:
    """Divide o trecho nas elisões ('...', '[...]', '(...)') e normaliza cada pedaço."""
    t = unicodedata.normalize("NFKC", trecho)
    partes = [normalizar(p) for p in _RE_ELISAO.split(t)]
    return [p for p in partes if p]


# =========================================================================== conferência

@dataclass
class Conferencia:
    status: str                 # ok | aproximado | ausente
    similaridade: float = 1.0
    trecho_na_fonte: str = ""
    nota: str = ""


def _aproximar(frag: str, texto_norm: str) -> tuple[float, str]:
    """Melhor similaridade (difflib) entre `frag` e alguma janela do texto, usando âncoras de 3 palavras."""
    palavras = frag.split()
    if len(palavras) < 3:
        return 0.0, ""
    tam = len(frag)
    inicios: set[int] = set()
    for k in range(len(palavras) - 2):
        ancora = " ".join(palavras[k:k + 3])
        desloc = frag.find(ancora)
        pos, achados = 0, 0
        while achados < 20:
            i = texto_norm.find(ancora, pos)
            if i < 0:
                break
            inicios.add(max(0, i - desloc) // 10 * 10)
            pos, achados = i + 1, achados + 1
        if len(inicios) > 300:
            break
    melhor, recorte_melhor = 0.0, ""
    folga = max(20, tam // 5)
    for ini in inicios:
        a = max(0, ini - folga)
        janela = texto_norm[a:ini + tam + folga]
        blocos = [b for b in SequenceMatcher(None, frag, janela, autojunk=False).get_matching_blocks()
                  if b.size >= 3]
        if not blocos:
            continue
        recorte = janela[blocos[0].b:blocos[-1].b + blocos[-1].size]
        r = SequenceMatcher(None, frag, recorte, autojunk=False).ratio()
        if r > melhor:
            melhor, recorte_melhor = r, recorte
    return melhor, recorte_melhor


def conferir_trecho(trecho: str, texto: str, limiar: float = LIMIAR_APROXIMADO,
                    min_aproximado: int = MIN_APROXIMADO) -> Conferencia:
    frags = fragmentos(trecho)
    if not frags:
        return Conferencia("ausente", 0.0, nota="trecho vazio")
    texto_norm = normalizar(texto)

    # 1) exato, com os fragmentos na ordem
    pos, exato = 0, True
    for f in frags:
        i = texto_norm.find(f, pos)
        if i < 0:
            exato = False
            break
        pos = i + len(f)
    if exato:
        nota = "com elisões" if len(frags) > 1 else ""
        return Conferencia("ok", 1.0, nota=nota)
    if all(f in texto_norm for f in frags):
        # todos os pedaços estão literalmente na fonte, só que citados em outra ordem
        return Conferencia("ok", 1.0, nota="com elisões fora da ordem da fonte")

    # 2) aproximado, fragmento a fragmento (só para fragmentos longos)
    pior, recortes = 1.0, []
    for f in frags:
        if f in texto_norm:
            recortes.append(f)
            continue
        if len(f) < min_aproximado:
            return Conferencia("ausente", 0.0, nota=f"trecho curto não encontrado: “{f[:60]}”")
        r, recorte = _aproximar(f, texto_norm)
        if r < limiar:
            return Conferencia("ausente", round(r, 3), trecho_na_fonte=recorte,
                               nota=f"melhor similaridade {r:.2f} < {limiar}")
        pior = min(pior, r)
        recortes.append(recorte)
    return Conferencia("aproximado", round(pior, 3), trecho_na_fonte=" [...] ".join(recortes))


# =========================================================================== números

_RE_NUMERO = re.compile(r"(?<![A-Za-zÀ-ÿ\d])\d(?:[\d.,   ]*\d)?")
_RE_MULT = re.compile(
    r"\s*(mil|milh(?:ão|ões|ao|oes)|bilh(?:ão|ões|ao|oes)|trilh(?:ão|ões|ao|oes)|"
    r"thousand|million|billion|trillion|mi|bi|tri|bn)\b",
    re.IGNORECASE,
)
_MULT = {"mil": 1e3, "thousand": 1e3, "million": 1e6, "mi": 1e6,
         "billion": 1e9, "bi": 1e9, "bn": 1e9, "trillion": 1e12, "tri": 1e12}


def _mult(palavra: str) -> float:
    p = palavra.lower()
    if p.startswith("milh"):
        return 1e6
    if p.startswith("bilh"):
        return 1e9
    if p.startswith("trilh"):
        return 1e12
    return _MULT.get(p, 1.0)


def _interpretar(token: str, milhar: str, decimal: str) -> float | None:
    s = re.sub(r"[   ]", "", token)
    if milhar in s and decimal in s:
        if s.rfind(decimal) < s.rfind(milhar):
            return None
        s = s.replace(milhar, "").replace(decimal, ".")
    elif milhar in s:
        grupos = s.split(milhar)
        if all(len(g) == 3 for g in grupos[1:]):
            s = "".join(grupos)            # 1.500 (pt) / 1,500 (en)
        elif len(grupos) == 2:
            s = s.replace(milhar, ".")     # escrito com o separador "errado": trata como decimal
        else:
            return None
    elif decimal in s:
        if s.count(decimal) > 1:
            return None
        s = s.replace(decimal, ".")
    try:
        return float(s)
    except ValueError:
        return None


def extrair_numeros(texto: str, convencoes: tuple[str, ...] = ("pt",)) -> list[tuple[str, set[float]]]:
    """Devolve (token, valores possíveis). Considera multiplicadores ('3 milhões', '3 million')."""
    texto = unicodedata.normalize("NFKC", texto)
    saida = []
    for m in _RE_NUMERO.finditer(texto):
        token = m.group(0)
        valores: set[float] = set()
        for conv in convencoes:
            v = _interpretar(token, ".", ",") if conv == "pt" else _interpretar(token, ",", ".")
            if v is not None:
                valores.add(v)
        mm = _RE_MULT.match(texto, m.end())
        if mm:
            fator = _mult(mm.group(1))
            valores |= {v * fator for v in valores}
        if valores:
            saida.append((token, valores))
    return saida


def numeros_sem_suporte(textos_fato: list[str], trechos: list[str]) -> list[str]:
    """Tokens numéricos do fato cujo valor não aparece em nenhum trecho (aceita pt e en nas fontes)."""
    suportados: set[float] = set()
    for t in trechos:
        for _, valores in extrair_numeros(t, ("pt", "en")):
            suportados |= {round(v, 6) for v in valores}
    faltando: list[str] = []
    for texto in textos_fato:
        for token, valores in extrair_numeros(texto, ("pt",)):
            if not {round(v, 6) for v in valores} & suportados and token not in faltando:
                faltando.append(token)
    return faltando


# =========================================================================== download e cache

class FalhaFonte(Exception):
    """A fonte não pôde ser obtida (bloqueio, paywall, 404, formato sem suporte...)."""


_RE_WIKI = re.compile(r"^(?P<lang>[a-z\-]+)(?:\.m)?\.wikipedia\.org$", re.IGNORECASE)
_BLOCOS = ["p", "div", "section", "article", "li", "ul", "ol", "dd", "dt", "dl", "table", "tr",
           "td", "th", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "pre", "figcaption",
           "header", "footer", "main", "aside", "br", "hr", "caption"]
_SINAIS_BLOQUEIO = ("just a moment", "captcha", "access denied", "are you a robot",
                    "enable javascript", "subscribe to continue", "assine para continuar")


def info_wikipedia(url: str) -> tuple[str, str] | None:
    """Se for artigo da Wikipedia, devolve (idioma, título)."""
    u = urlparse(url)
    m = _RE_WIKI.match(u.netloc)
    if not m:
        return None
    if u.path.startswith("/wiki/"):
        titulo = unquote(u.path[len("/wiki/"):])
    else:
        q = dict(p.split("=", 1) for p in u.query.split("&") if "=" in p)
        if "title" not in q:
            return None
        titulo = unquote(q["title"])
    return m.group("lang").lower(), titulo.replace("_", " ")


def url_api_wikipedia(lang: str, titulo: str) -> str:
    return (f"https://{lang}.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1"
            f"&format=json&formatversion=2&redirects=1&titles={quote(titulo)}")


def url_render_wikipedia(lang: str, titulo: str) -> str:
    return f"https://{lang}.wikipedia.org/w/index.php?title={quote(titulo.replace(' ', '_'))}&action=render"


def html_para_texto(conteudo: bytes | str) -> str:
    from bs4 import BeautifulSoup

    sopa = BeautifulSoup(conteudo, "html.parser")
    for tag in sopa(["script", "style", "noscript", "template", "svg"]):
        tag.decompose()
    for tag in sopa.find_all(_BLOCOS):
        tag.insert_before("\n")
        tag.insert_after("\n")
    texto = sopa.get_text()
    linhas = (" ".join(l.split()) for l in texto.splitlines())
    return "\n".join(l for l in linhas if l)


def pdf_para_texto(conteudo: bytes) -> str:
    try:
        from pypdf import PdfReader
    except ImportError as e:
        raise FalhaFonte("pdf_sem_suporte (instale pypdf para ler PDFs)") from e
    try:
        leitor = PdfReader(io.BytesIO(conteudo))
        return "\n".join((p.extract_text() or "") for p in leitor.pages)
    except Exception as e:  # PDFs quebrados geram exceções variadas
        raise FalhaFonte(f"pdf_ilegivel ({e.__class__.__name__})") from e


def _slug(url: str) -> str:
    u = urlparse(url)
    base = (u.netloc + u.path + ("_" + u.query if u.query else "")).strip("/")
    base = re.sub(r"[^A-Za-z0-9]+", "_", unquote(base)).strip("_")
    return base[:80] or "fonte"


class Baixador:
    """Baixa fontes com cache em disco. Wikipedia tem duas variantes: 'extrato' (API) e 'html'."""

    def __init__(self, pasta_cache: Path, offline: bool = False, renovar: bool = False,
                 timeout: float = 20.0, pausa: float = 0.5, tentativas_429: int = 3) -> None:
        self.pasta = pasta_cache
        self.offline = offline
        self.renovar = renovar
        self.timeout = timeout
        self.pausa = pausa
        self.tentativas_429 = tentativas_429
        self._sessao = None
        self._ultimo = 0.0

    # ----- cache
    def caminho_cache(self, url: str, variante: str) -> Path:
        h = hashlib.sha256(url.encode("utf-8")).hexdigest()[:10]
        return self.pasta / f"{_slug(url)}__{h}__{variante}.txt"

    def variantes(self, url: str) -> list[str]:
        return ["extrato", "html"] if info_wikipedia(url) else ["pagina"]

    def texto(self, url: str, variante: str) -> tuple[str, Path]:
        caminho = self.caminho_cache(url, variante)
        if caminho.exists() and not self.renovar:
            return caminho.read_text(encoding="utf-8"), caminho
        if self.offline:
            raise FalhaFonte("sem_cache (modo offline)")
        texto, meta = self._baixar(url, variante)
        self.pasta.mkdir(parents=True, exist_ok=True)
        caminho.write_text(texto, encoding="utf-8")
        meta |= {"url": url, "variante": variante, "baixado_em": comum.hoje()}
        caminho.with_suffix(".json").write_text(json.dumps(meta, ensure_ascii=False, indent=1),
                                                encoding="utf-8")
        return texto, caminho

    # ----- rede
    def _get(self, url: str):
        import requests

        if self._sessao is None:
            ua = f"CuriosidadesSobMedida/{VERSAO} (app pessoal; verificacao de citacoes)"
            contato = os.environ.get("CURIOSIDADES_CONTATO")
            if contato:
                ua += f" contato: {contato}"
            self._sessao = requests.Session()
            self._sessao.headers.update({"User-Agent": ua, "Accept-Language": "pt-BR,pt,en;q=0.8"})
        for tentativa in range(self.tentativas_429 + 1):
            espera = self.pausa - (time.monotonic() - self._ultimo)
            if espera > 0:
                time.sleep(espera)
            try:
                r = self._sessao.get(url, timeout=self.timeout, stream=True, allow_redirects=True)
                conteudo = r.raw.read(TAMANHO_MAXIMO + 1, decode_content=True)
            except requests.RequestException as e:
                raise FalhaFonte(f"erro_de_rede ({e.__class__.__name__})") from e
            finally:
                self._ultimo = time.monotonic()
            if r.status_code != 429 or tentativa == self.tentativas_429:
                break
            # muitas requisições: espera (o que o servidor pedir, até 30 s) e tenta de novo
            try:
                pedido = float(r.headers.get("Retry-After", ""))
            except ValueError:
                pedido = 0.0
            time.sleep(min(30.0, max(pedido, 2.0 * 2 ** tentativa)))
        if len(conteudo) > TAMANHO_MAXIMO:
            raise FalhaFonte("arquivo_grande_demais")
        if r.status_code in (401, 402, 403, 451):
            raise FalhaFonte(f"bloqueado_ou_paywall (HTTP {r.status_code})")
        if r.status_code == 429:
            raise FalhaFonte("muitas_requisicoes (HTTP 429)")
        if r.status_code >= 400:
            raise FalhaFonte(f"http_{r.status_code}")
        return r, conteudo

    def _baixar(self, url: str, variante: str) -> tuple[str, dict]:
        wiki = info_wikipedia(url)
        if wiki and variante == "extrato":
            r, conteudo = self._get(url_api_wikipedia(*wiki))
            try:
                paginas = json.loads(conteudo)["query"]["pages"]
            except (ValueError, KeyError) as e:
                raise FalhaFonte("resposta_inesperada_da_api_wikipedia") from e
            if not paginas or paginas[0].get("missing") or "extract" not in paginas[0]:
                raise FalhaFonte("pagina_inexistente_na_wikipedia")
            return paginas[0]["extract"], {"titulo_resolvido": paginas[0].get("title"),
                                           "status_http": r.status_code}
        if wiki and variante == "html":
            r, conteudo = self._get(url_render_wikipedia(*wiki))
            return html_para_texto(conteudo), {"status_http": r.status_code}

        r, conteudo = self._get(url)
        tipo = r.headers.get("Content-Type", "").split(";")[0].strip().lower()
        meta = {"status_http": r.status_code, "content_type": tipo, "url_final": r.url}
        if tipo == "application/pdf" or conteudo[:5] == b"%PDF-":
            return pdf_para_texto(conteudo), meta
        if tipo in ("text/html", "application/xhtml+xml", "") or b"<html" in conteudo[:2000].lower():
            return html_para_texto(conteudo), meta
        if tipo.startswith("text/") or tipo in ("application/json", "application/xml"):
            return conteudo.decode(r.encoding or "utf-8", errors="replace"), meta
        raise FalhaFonte(f"formato_sem_suporte ({tipo})")


# =========================================================================== checagem de um fato

def _parece_bloqueio(texto: str) -> bool:
    inicio = texto[:3000].casefold()
    return len(texto) < 5000 and any(s in inicio for s in _SINAIS_BLOQUEIO)


def checar_fonte(fonte: dict, baixador: Baixador, limiar: float, min_aprox: int) -> dict:
    url = fonte.get("url", "")
    res: dict = {"url": url, "status": "falhou"}
    trecho = fonte.get("trecho") or ""
    if not trecho.strip():
        res["motivo"] = "trecho_vazio"
        return res
    melhor: Conferencia | None = None
    caches: list[str] = []
    falhas: list[str] = []
    for variante in baixador.variantes(url):
        try:
            texto, caminho = baixador.texto(url, variante)
        except FalhaFonte as e:
            falhas.append(f"{variante}: {e}" if len(baixador.variantes(url)) > 1 else str(e))
            continue  # na Wikipedia, se uma variante falha, a outra ainda pode servir
        caches.append(str(caminho))
        conf = conferir_trecho(trecho, texto, limiar, min_aprox)
        if melhor is None or conf.similaridade > melhor.similaridade or conf.status == "ok":
            melhor = conf
        if conf.status == "ok":
            break
        if _parece_bloqueio(texto):
            res["suspeita"] = "a página parece bloqueio/captcha/paywall"
    if not caches:
        res["motivo"] = "; ".join(falhas)
        return res
    res["cache"] = caches
    if melhor is None:
        res["motivo"] = "sem_texto"
    elif melhor.status == "ausente":
        res["motivo"] = "trecho_nao_encontrado" + (f" ({melhor.nota})" if melhor.nota else "")
        if melhor.trecho_na_fonte:
            res["mais_parecido_na_fonte"] = melhor.trecho_na_fonte
    else:
        res["status"] = melhor.status
        res["similaridade"] = melhor.similaridade
        if melhor.nota:
            res["nota"] = melhor.nota
        if melhor.status == "aproximado":
            res["trecho_na_fonte"] = melhor.trecho_na_fonte
    return res


def checar_fato(fato: dict, baixador: Baixador, limiar: float = LIMIAR_APROXIMADO,
                min_aprox: int = MIN_APROXIMADO) -> dict:
    fontes = fato.get("fontes") or []
    resultados = [checar_fonte(f, baixador, limiar, min_aprox) for f in fontes if isinstance(f, dict)]
    status_fontes = {r["status"] for r in resultados}
    status = "ok" if "ok" in status_fontes else "aproximado" if "aproximado" in status_fontes else "falhou"

    confirmados = [f.get("trecho", "") for f, r in zip(fontes, resultados) if r["status"] != "falhou"]
    trechos = confirmados or [f.get("trecho", "") for f in fontes if isinstance(f, dict)]
    avisos = numeros_sem_suporte([fato.get("gancho", ""), fato.get("explicacao", "")], trechos)
    return {"id": fato.get("id"), "status": status, "aviso_numero": avisos, "fontes": resultados}


# =========================================================================== CLI

def _imprimir(res: dict) -> None:
    rotulo = {"ok": "ok", "aproximado": "aproximado", "falhou": "FALHOU"}[res["status"]]
    n_ok = sum(1 for f in res["fontes"] if f["status"] != "falhou")
    print(f"[{rotulo:<10}] {res['id']}  ({n_ok}/{len(res['fontes'])} fontes confirmadas)")
    for f in res["fontes"]:
        if f["status"] == "falhou":
            print(f"      ✗ {f['url']}\n        → {f.get('motivo')}")
        elif f["status"] == "aproximado":
            print(f"      ≈ {f['url']}  (similaridade {f['similaridade']:.2f})")
    if res["aviso_numero"]:
        print(f"      aviso_numero: {', '.join(res['aviso_numero'])}")


def main(argv: list[str] | None = None) -> int:
    comum.configurar_saida()
    p = argparse.ArgumentParser(description="Confere os trechos citados contra o texto das fontes.")
    p.add_argument("arquivo", nargs="?", type=Path, help="lote .jsonl com os candidatos")
    p.add_argument("--baixar", nargs="+", metavar="URL", help="só baixa as URLs para o cache")
    p.add_argument("--cache", type=Path, default=comum.DADOS_PADRAO / "cache_fontes")
    p.add_argument("--relatorio", type=Path, help="caminho do relatório JSON (padrão: <lote>.checagem.json)")
    p.add_argument("--offline", action="store_true", help="não acessa a rede; usa só o cache")
    p.add_argument("--renovar", action="store_true", help="ignora o cache e baixa de novo")
    p.add_argument("--timeout", type=float, default=20.0)
    p.add_argument("--pausa", type=float, default=0.5, help="segundos entre requisições")
    p.add_argument("--limiar", type=float, default=LIMIAR_APROXIMADO)
    p.add_argument("--min-aproximado", type=int, default=MIN_APROXIMADO)
    args = p.parse_args(argv)

    baixador = Baixador(args.cache, offline=args.offline, renovar=args.renovar,
                        timeout=args.timeout, pausa=args.pausa)

    if args.baixar:
        erro = False
        for url in args.baixar:
            for variante in baixador.variantes(url):
                try:
                    texto, caminho = baixador.texto(url, variante)
                    print(f"ok  {url} [{variante}] → {caminho}  ({len(texto)} caracteres)")
                except FalhaFonte as e:
                    print(f"FALHOU  {url} [{variante}] → {e}")
                    erro = True
        return 1 if erro else 0

    if not args.arquivo:
        p.error("informe o arquivo do lote ou use --baixar")
    if not args.arquivo.exists():
        print(f"Arquivo não encontrado: {args.arquivo}", file=sys.stderr)
        return 2

    linhas = comum.ler_jsonl(args.arquivo)
    invalidas = [(n, e) for n, o, e in linhas if e]
    for n, e in invalidas:
        print(f"Linha {n}: {e}", file=sys.stderr)
    if invalidas:
        return 2

    resultados = []
    for _, fato, _ in linhas:
        res = checar_fato(fato, baixador, args.limiar, args.min_aproximado)
        _imprimir(res)
        resultados.append(res)

    contagem = {s: sum(1 for r in resultados if r["status"] == s) for s in ("ok", "aproximado", "falhou")}
    com_aviso = sum(1 for r in resultados if r["aviso_numero"])
    relatorio = args.relatorio or args.arquivo.with_name(args.arquivo.stem + ".checagem.json")
    relatorio.write_text(json.dumps({
        "arquivo": str(args.arquivo), "gerado_em": comum.hoje(), "limiar": args.limiar,
        "resumo": contagem | {"com_aviso_numero": com_aviso}, "fatos": resultados,
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"\nResumo: {contagem['ok']} ok · {contagem['aproximado']} aproximado · "
          f"{contagem['falhou']} falhou · {com_aviso} com aviso de número")
    print(f"Relatório: {relatorio}")
    return 1 if contagem["falhou"] else 0


if __name__ == "__main__":
    sys.exit(main())
