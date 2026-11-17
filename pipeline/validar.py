"""Valida taxonomia, tipos de espanto e fichas de fatos (esquema, limites, ids, duplicatas).

Uso:
    python pipeline/validar.py                         # taxonomia + dados/fatos + dados/descartados
    python pipeline/validar.py dados/lotes/<lote>.jsonl  # candidatos de um lote (comparados aos aprovados)
    python pipeline/validar.py --estrito               # avisos também reprovam

O modo de cada arquivo é deduzido pela pasta: fatos/ → aprovado, descartados/ → descartado,
qualquer outra → candidato. Sai com código 1 se houver erro.
"""

from __future__ import annotations

import argparse
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

import comum

RE_SNAKE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")
RE_IDIOMA = re.compile(r"^[a-z]{2,3}(?:-[A-Za-z]{2,4})?$")
RE_URL = re.compile(r"^https?://[^\s/$.?#][^\s]*$", re.IGNORECASE)
RE_CLICKBAIT = re.compile(
    r"você não vai acreditar|voce nao vai acreditar|inacreditável|chocante|"
    r"ninguém te contou|o que acontece (a seguir|depois)|vai te surpreender",
    re.IGNORECASE,
)
RE_HIPOTESE = re.compile(
    r"\b(talvez|pode|podem|poderia|poderiam|hipótese|possivelmente|provavelmente|sugere|sugerem|"
    r"suspeita|ainda não|não se sabe|ninguém sabe|debate|propõe|propõem|teoria)\b",
    re.IGNORECASE,
)

GANCHO_MAX = 220
EXPLICACAO_MIN, EXPLICACAO_MAX = 80, 250
TRECHO_LONGO = 400   # por pedaço: trechos longos demais copiam a fonte além do necessário
TRECHO_TOTAL = 1500  # soma dos pedaços de uma fonte
RE_ELISAO = re.compile(r"\[\s*(?:\.\.\.|…)\s*\]|\(\s*(?:\.\.\.|…)\s*\)|…|\.\.\.")
LIMIAR_DUPLICATA = 0.80

CAMPOS_CONHECIDOS = {
    "id", "area", "tema", "temas_secundarios", "tipos_espanto", "gancho", "explicacao",
    "nivel", "nota_surpresa", "confianca", "fontes", "aprofundar", "lote", "verificado_em",
    "motivo_descarte", "revisao_humana",
}


class Relatorio:
    def __init__(self) -> None:
        self.erros: list[str] = []
        self.avisos: list[str] = []

    def erro(self, onde: str, msg: str) -> None:
        self.erros.append(f"{onde}: {msg}")

    def aviso(self, onde: str, msg: str) -> None:
        self.avisos.append(f"{onde}: {msg}")


# --------------------------------------------------------------------------- taxonomia

def validar_tipos(dados: Path, rel: Relatorio) -> None:
    caminho = dados / "tipos_espanto.json"
    if not caminho.exists():
        rel.aviso("tipos_espanto.json", "arquivo ausente; usando a lista fixa do CLAUDE.md")
        return
    try:
        conteudo = comum.carregar_json(caminho)
    except ValueError as e:
        rel.erro("tipos_espanto.json", f"JSON inválido: {e}")
        return
    tipos = conteudo.get("tipos") if isinstance(conteudo, dict) else None
    if not isinstance(tipos, list) or not tipos:
        rel.erro("tipos_espanto.json", "esperado {\"tipos\": [...]} não vazio")
        return
    vistos = set()
    for i, t in enumerate(tipos):
        onde = f"tipos_espanto.json[{i}]"
        if not isinstance(t, dict) or not isinstance(t.get("id"), str):
            rel.erro(onde, "cada tipo precisa de um 'id'")
            continue
        if t["id"] in vistos:
            rel.erro(onde, f"id repetido '{t['id']}'")
        vistos.add(t["id"])
        if not t.get("nome"):
            rel.erro(onde, "falta 'nome'")
    faltando = set(comum.TIPOS_ESPANTO_PADRAO) - vistos
    extras = vistos - set(comum.TIPOS_ESPANTO_PADRAO)
    if faltando:
        rel.aviso("tipos_espanto.json", f"tipos do CLAUDE.md ausentes: {sorted(faltando)}")
    if extras:
        rel.aviso("tipos_espanto.json", f"tipos fora do CLAUDE.md: {sorted(extras)}")


def validar_taxonomia(taxonomia: dict, rel: Relatorio) -> None:
    onde = "taxonomia.json"
    areas = taxonomia.get("areas") if isinstance(taxonomia, dict) else None
    if not isinstance(areas, list) or not areas:
        rel.erro(onde, "esperado {\"areas\": [...]} não vazio")
        return

    ids_area: set[str] = set()
    area_do_tema: dict[str, str] = {}
    for a, area in enumerate(areas):
        oa = f"{onde} areas[{a}]"
        if not isinstance(area, dict):
            rel.erro(oa, "área não é objeto")
            continue
        aid = area.get("id")
        if not isinstance(aid, str) or not RE_SNAKE.match(aid):
            rel.erro(oa, f"id de área inválido: {aid!r} (use snake_case sem acentos)")
        elif aid in ids_area:
            rel.erro(oa, f"id de área repetido '{aid}'")
        else:
            ids_area.add(aid)
        if not area.get("nome"):
            rel.erro(oa, "falta 'nome'")
        temas = area.get("temas")
        if not isinstance(temas, list) or not temas:
            rel.erro(oa, "área sem temas")
            continue
        for t, tema in enumerate(temas):
            ot = f"{oa} temas[{t}]"
            if not isinstance(tema, dict):
                rel.erro(ot, "tema não é objeto")
                continue
            tid = tema.get("id")
            if not isinstance(tid, str) or not RE_SNAKE.match(tid):
                rel.erro(ot, f"id de tema inválido: {tid!r} (use snake_case sem acentos)")
                continue
            if tid in area_do_tema:
                rel.erro(ot, f"id de tema repetido no projeto: '{tid}'")
            area_do_tema[tid] = aid
            for campo in ("nome", "descricao"):
                if not tema.get(campo):
                    rel.erro(ot, f"falta '{campo}'")

    # vizinhos (segunda passada, quando todos os temas já são conhecidos)
    for area in areas:
        if not isinstance(area, dict):
            continue
        for tema in area.get("temas") or []:
            if not isinstance(tema, dict) or not isinstance(tema.get("id"), str):
                continue
            ot = f"{onde} tema '{tema['id']}'"
            viz = tema.get("vizinhos")
            if not isinstance(viz, list):
                rel.erro(ot, "falta a lista 'vizinhos'")
                continue
            if not 2 <= len(viz) <= 5:
                rel.erro(ot, f"precisa de 2 a 5 vizinhos (tem {len(viz)})")
            if len(set(viz)) != len(viz):
                rel.erro(ot, "vizinho repetido")
            for v in viz:
                if v == tema["id"]:
                    rel.erro(ot, "o tema não pode ser vizinho de si mesmo")
                elif v not in area_do_tema:
                    rel.erro(ot, f"vizinho inexistente '{v}'")
                elif area_do_tema[v] == area.get("id"):
                    rel.erro(ot, f"vizinho '{v}' é da mesma área (vizinhos devem ser de outras áreas)")


# --------------------------------------------------------------------------- fatos

def modo_do_arquivo(caminho: Path) -> str:
    pasta = caminho.resolve().parent.name
    if pasta == "fatos":
        return "aprovado"
    if pasta == "descartados":
        return "descartado"
    return "candidato"


def _str_nao_vazia(v: object) -> bool:
    return isinstance(v, str) and v.strip() != ""


def _int(v: object) -> bool:
    return isinstance(v, int) and not isinstance(v, bool)


def validar_fato(fato: dict, onde: str, modo: str, ctx: dict, rel: Relatorio) -> None:
    indice = ctx["indice"]
    tipos_validos = ctx["tipos"]
    estrito_esquema = modo == "aprovado"

    for campo in sorted(set(fato) - CAMPOS_CONHECIDOS):
        rel.aviso(onde, f"campo desconhecido '{campo}'")

    # id, área e tema
    fid, area, tema = fato.get("id"), fato.get("area"), fato.get("tema")
    if not _str_nao_vazia(tema):
        rel.erro(onde, "falta 'tema'")
    if not _str_nao_vazia(area):
        rel.erro(onde, "falta 'area'")
    if not _str_nao_vazia(fid):
        rel.erro(onde, "falta 'id'")
    elif _str_nao_vazia(tema) and not re.fullmatch(re.escape(tema) + r"-\d{4}", fid):
        rel.erro(onde, f"id '{fid}' deve ter o formato '{tema}-NNNN'")

    if indice:
        if _str_nao_vazia(tema):
            if tema not in indice:
                rel.erro(onde, f"tema '{tema}' não existe na taxonomia")
            elif indice[tema]["area"] != area:
                rel.erro(onde, f"tema '{tema}' pertence à área '{indice[tema]['area']}', não a '{area}'")
    arq_area = ctx.get("area_do_arquivo")
    if arq_area and _str_nao_vazia(area) and area != arq_area:
        rel.erro(onde, f"fato da área '{area}' gravado em {arq_area}.jsonl")

    # temas secundários
    sec = fato.get("temas_secundarios", [])
    if not isinstance(sec, list) or not all(isinstance(s, str) for s in sec):
        rel.erro(onde, "'temas_secundarios' deve ser lista de ids")
    else:
        if len(set(sec)) != len(sec):
            rel.erro(onde, "tema secundário repetido")
        if tema in sec:
            rel.erro(onde, "o tema principal não pode estar em 'temas_secundarios'")
        if len(sec) > 3:
            rel.aviso(onde, f"{len(sec)} temas secundários (o normal é até 3)")
        if indice:
            for s in sec:
                if s not in indice:
                    rel.erro(onde, f"tema secundário inexistente '{s}'")

    # tipos de espanto
    tipos = fato.get("tipos_espanto")
    if not isinstance(tipos, list) or not 1 <= len(tipos) <= 3:
        rel.erro(onde, "'tipos_espanto' deve ter de 1 a 3 itens")
    else:
        if len(set(tipos)) != len(tipos):
            rel.erro(onde, "tipo de espanto repetido")
        for t in tipos:
            if t not in tipos_validos:
                rel.erro(onde, f"tipo de espanto desconhecido '{t}'")

    # textos
    gancho = fato.get("gancho")
    if not _str_nao_vazia(gancho):
        rel.erro(onde, "falta 'gancho'")
    else:
        if len(gancho) > GANCHO_MAX:
            rel.erro(onde, f"gancho com {len(gancho)} caracteres (máximo {GANCHO_MAX})")
        if RE_CLICKBAIT.search(gancho):
            rel.aviso(onde, "gancho com cara de clickbait")
    expl = fato.get("explicacao")
    if not _str_nao_vazia(expl):
        rel.erro(onde, "falta 'explicacao'")
    else:
        palavras = len(expl.split())
        if not EXPLICACAO_MIN <= palavras <= EXPLICACAO_MAX:
            msg = f"explicação com {palavras} palavras (esperado {EXPLICACAO_MIN}–{EXPLICACAO_MAX})"
            (rel.erro if estrito_esquema else rel.aviso)(onde, msg)

    # números
    nivel = fato.get("nivel")
    if not _int(nivel) or not 1 <= nivel <= 3:
        rel.erro(onde, "'nivel' deve ser 1, 2 ou 3")
    nota = fato.get("nota_surpresa")
    if not _int(nota) or not 1 <= nota <= 5:
        rel.erro(onde, "'nota_surpresa' deve ser inteiro de 1 a 5")
    elif modo == "aprovado" and nota < 3:
        rel.erro(onde, f"fato aprovado com nota_surpresa {nota} (mínimo 3)")

    # confiança
    conf = fato.get("confianca")
    if conf not in comum.CONFIANCAS:
        rel.erro(onde, f"'confianca' deve ser um de {comum.CONFIANCAS}")
    elif conf == "hipotese":
        if not isinstance(tipos, list) or "misterio_aberto" not in tipos:
            rel.erro(onde, "confianca 'hipotese' exige o tipo 'misterio_aberto'")
        if _str_nao_vazia(gancho) and not RE_HIPOTESE.search(gancho):
            rel.aviso(onde, "confianca 'hipotese', mas o gancho não deixa claro que é hipótese")

    # fontes
    fontes = fato.get("fontes")
    if not isinstance(fontes, list) or not fontes:
        rel.erro(onde, "precisa de pelo menos uma fonte")
    else:
        urls = set()
        for i, fonte in enumerate(fontes):
            of = f"{onde} fontes[{i}]"
            if not isinstance(fonte, dict):
                rel.erro(of, "fonte não é objeto")
                continue
            url = fonte.get("url")
            if not isinstance(url, str) or not RE_URL.match(url):
                rel.erro(of, f"url inválida: {url!r}")
            elif url in urls:
                rel.aviso(of, "url repetida no mesmo fato")
            else:
                urls.add(url)
            if not _str_nao_vazia(fonte.get("titulo")):
                rel.erro(of, "falta 'titulo'")
            idioma = fonte.get("idioma")
            if not isinstance(idioma, str) or not RE_IDIOMA.match(idioma):
                rel.erro(of, f"'idioma' inválido: {idioma!r} (ex.: 'pt', 'en')")
            trecho = fonte.get("trecho")
            if not _str_nao_vazia(trecho):
                rel.erro(of, "falta 'trecho'")
            else:
                if len(trecho) < 20:
                    rel.aviso(of, "trecho muito curto para sustentar algo")
                # com elisões ([...]) o trecho junta vários pedaços; o limite vale para cada pedaço
                pedacos = [p for p in RE_ELISAO.split(trecho) if p.strip()]
                maior = max((len(p) for p in pedacos), default=0)
                if maior > TRECHO_LONGO:
                    rel.aviso(of, f"pedaço de trecho com {maior} caracteres; copie só o necessário")
                if len(trecho) > TRECHO_TOTAL:
                    rel.aviso(of, f"trecho com {len(trecho)} caracteres no total; copie só o necessário")
            if not comum.data_valida(fonte.get("acessado_em")):
                rel.erro(of, "'acessado_em' deve ser data AAAA-MM-DD")

    # aprofundar (opcional)
    apro = fato.get("aprofundar", [])
    if not isinstance(apro, list):
        rel.erro(onde, "'aprofundar' deve ser lista")
    else:
        for i, item in enumerate(apro):
            oa = f"{onde} aprofundar[{i}]"
            if not isinstance(item, dict):
                rel.erro(oa, "item não é objeto")
                continue
            if item.get("tipo") not in comum.TIPOS_APROFUNDAR:
                rel.erro(oa, f"'tipo' deve ser um de {comum.TIPOS_APROFUNDAR}")
            if not _str_nao_vazia(item.get("titulo")):
                rel.erro(oa, "falta 'titulo'")
            url = item.get("url")
            if url is None and item.get("tipo") == "livro":
                pass
            elif not isinstance(url, str) or not RE_URL.match(url):
                rel.erro(oa, f"url inválida: {url!r}")

    # metadados de processo
    if not _str_nao_vazia(fato.get("lote")):
        rel.erro(onde, "falta 'lote'")
    ver = fato.get("verificado_em")
    if modo == "aprovado" and not comum.data_valida(ver):
        rel.erro(onde, "'verificado_em' deve ser data AAAA-MM-DD")
    elif ver is not None and not comum.data_valida(ver):
        rel.erro(onde, "'verificado_em' deve ser data AAAA-MM-DD")

    motivo = fato.get("motivo_descarte")
    if modo == "descartado":
        if not _str_nao_vazia(motivo):
            rel.erro(onde, "descartado sem 'motivo_descarte'")
        elif motivo.split(":")[0].strip() not in comum.MOTIVOS_DESCARTE:
            rel.aviso(onde, f"motivo de descarte fora da lista padrão: '{motivo}'")
    elif motivo is not None:
        rel.erro(onde, "'motivo_descarte' só pode existir em dados/descartados/")


def _palavras(texto: str) -> set[str]:
    return {p for p in re.findall(r"\w+", texto.casefold()) if len(p) >= 4}


def checar_duplicatas(fatos: list[tuple[str, dict]], rel: Relatorio) -> None:
    """Compara ganchos entre si. Igual (normalizado) → erro; muito parecido → aviso."""
    itens = []
    for onde, f in fatos:
        g = f.get("gancho")
        if isinstance(g, str) and g.strip():
            norm = " ".join(re.findall(r"\w+", g.casefold()))
            itens.append((onde, f.get("id"), norm, _palavras(g)))
    for i in range(len(itens)):
        onde_a, id_a, norm_a, pal_a = itens[i]
        for j in range(i + 1, len(itens)):
            onde_b, id_b, norm_b, pal_b = itens[j]
            if norm_a == norm_b:
                rel.erro(onde_b, f"gancho idêntico ao de {id_a}")
                continue
            uniao = pal_a | pal_b
            if not uniao or len(pal_a & pal_b) / len(uniao) < 0.4:
                continue  # pré-filtro barato
            r = SequenceMatcher(None, norm_a, norm_b).ratio()
            if r >= LIMIAR_DUPLICATA:
                rel.aviso(onde_b, f"gancho muito parecido com o de {id_a} (similaridade {r:.2f})")


def validar_arquivos(arquivos: list[Path], dados: Path, rel: Relatorio,
                     comparar_com: list[Path] | None = None) -> int:
    """Valida os arquivos de fatos. `comparar_com` entra só na checagem de ids e duplicatas."""
    taxonomia = comum.carregar_taxonomia(dados)
    ctx_base = {
        "indice": comum.indice_temas(taxonomia),
        "tipos": set(comum.carregar_tipos_espanto(dados)),
    }
    ids: dict[str, str] = {}
    para_duplicata: list[tuple[str, dict]] = []
    total = 0

    def registrar_id(fato: dict, onde: str) -> None:
        fid = fato.get("id")
        if isinstance(fid, str):
            if fid in ids:
                rel.erro(onde, f"id '{fid}' repetido (já usado em {ids[fid]})")
            else:
                ids[fid] = onde

    # referências (ex.: aprovados, quando se valida um lote)
    for arq in comparar_com or []:
        for n, fato, erro in comum.ler_jsonl(arq):
            if fato is not None:
                onde = f"{arq.name}:{n}"
                registrar_id(fato, onde)
                if modo_do_arquivo(arq) == "aprovado":
                    para_duplicata.append((onde, fato))

    for arq in arquivos:
        modo = modo_do_arquivo(arq)
        ctx = dict(ctx_base)
        if modo in ("aprovado", "descartado"):
            ctx["area_do_arquivo"] = arq.stem
        for n, fato, erro in comum.ler_jsonl(arq):
            onde = f"{arq.name}:{n}"
            if erro:
                rel.erro(onde, erro)
                continue
            total += 1
            if fato.get("id"):
                onde = f"{arq.name}:{n} ({fato['id']})"
            validar_fato(fato, onde, modo, ctx, rel)
            registrar_id(fato, onde)
            if modo != "descartado":
                para_duplicata.append((onde, fato))

    checar_duplicatas(para_duplicata, rel)
    return total


def main(argv: list[str] | None = None) -> int:
    comum.configurar_saida()
    p = argparse.ArgumentParser(description="Valida taxonomia e fichas de fatos.")
    p.add_argument("arquivos", nargs="*", type=Path,
                   help="arquivos .jsonl a validar (padrão: dados/fatos e dados/descartados)")
    p.add_argument("--dados", type=Path, default=comum.DADOS_PADRAO, help="pasta de dados")
    p.add_argument("--estrito", action="store_true", help="avisos também reprovam")
    p.add_argument("--silencioso", action="store_true", help="não lista os avisos")
    args = p.parse_args(argv)

    dados: Path = args.dados
    rel = Relatorio()

    validar_tipos(dados, rel)
    try:
        taxonomia = comum.carregar_taxonomia(dados)
    except ValueError as e:
        rel.erro("taxonomia.json", f"JSON inválido: {e}")
        taxonomia = None
    if taxonomia is None:
        rel.aviso("taxonomia.json", "ausente; checagens de área/tema puladas")
    else:
        validar_taxonomia(taxonomia, rel)

    aprovados = sorted((dados / "fatos").glob("*.jsonl"))
    descartados = sorted((dados / "descartados").glob("*.jsonl"))
    if args.arquivos:
        for a in args.arquivos:
            if not a.exists():
                print(f"Arquivo não encontrado: {a}", file=sys.stderr)
                return 2
        alvos = [a.resolve() for a in args.arquivos]
        referencias = [r for r in aprovados + descartados if r.resolve() not in alvos]
        total = validar_arquivos(list(args.arquivos), dados, rel, comparar_com=referencias)
    else:
        total = validar_arquivos(aprovados + descartados, dados, rel)

    if not args.silencioso:
        for a in rel.avisos:
            print(f"AVISO  {a}")
    for e in rel.erros:
        print(f"ERRO   {e}")
    print(f"\n{total} fato(s) conferido(s) · {len(rel.erros)} erro(s) · {len(rel.avisos)} aviso(s)")

    if rel.erros or (args.estrito and rel.avisos):
        print("Resultado: REPROVADO")
        return 1
    print("Resultado: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
