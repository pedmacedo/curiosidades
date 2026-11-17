"""Sorteia fatos aprovados para revisão humana (§5.4) e apura revisões já marcadas.

Uso:
    python pipeline/sortear_amostra.py --n 30                  # sorteia 30 ainda não revisados
    python pipeline/sortear_amostra.py --todos --lotes L1,L2   # todos os fatos de certos lotes (piloto)
    python pipeline/sortear_amostra.py --apurar dados/revisao/<arquivo>.md
    python pipeline/sortear_amostra.py --apurar dados/revisao/<arquivo>.md --descartar

O arquivo gerado fica em dados/revisao/<nome>.md, com caixas [ ] ok [ ] errado [ ] chato.
Marque com um x. Fatos já sorteados em revisões anteriores não são sorteados de novo.
"""

from __future__ import annotations

import argparse
import random
import re
import sys
from pathlib import Path

import comum

RE_ID = re.compile(r"<!--\s*id:\s*(\S+)\s*-->")
RE_CAIXA = re.compile(r"\[([ xX])\]\s*(ok|errado|chato)\b", re.IGNORECASE)
RE_COMENTARIO = re.compile(r"\*\*Comentário:\*\*[ \t]*(.*)")


def ids_ja_revisados(pasta_revisao: Path) -> set[str]:
    ids: set[str] = set()
    for md in pasta_revisao.glob("*.md"):
        ids |= set(RE_ID.findall(md.read_text(encoding="utf-8")))
    return ids


def sortear(fatos: list[dict], n: int | None, semente: int | None) -> list[dict]:
    rng = random.Random(semente)
    if n is None or n >= len(fatos):
        escolhidos = list(fatos)
        rng.shuffle(escolhidos)
        return escolhidos
    return rng.sample(fatos, n)


def _citar(texto: str) -> str:
    return "\n".join("> " + linha for linha in texto.splitlines() or [""])


def gerar_markdown(fatos: list[dict], nome: str, semente: int | None) -> str:
    partes = [
        f"# Revisão por amostragem: {nome}",
        "",
        f"Gerado em {comum.hoje()} · {len(fatos)} fato(s) · semente {semente}",
        "",
        "Para cada fato, marque **uma** caixa trocando `[ ]` por `[x]`:",
        "",
        "- **ok**: correto e interessante",
        "- **errado**: alguma afirmação não confere, exagera ou a fonte não sustenta",
        "- **chato**: correto, mas trivia de almanaque, já conhecido ou sem graça",
        "",
        "Comentários livres na linha *Comentário* ajudam a ajustar o processo.",
        "Com 0–1 problema (errado + chato) o bloco segue; com 2 ou mais, pausamos para diagnosticar.",
        "",
    ]
    for i, f in enumerate(fatos, start=1):
        partes += [
            "---",
            "",
            f"## {i}. {f.get('id')}",
            f"<!-- id: {f.get('id')} -->",
            "",
            f"*{f.get('area')} › {f.get('tema')}* · tipos: {', '.join(f.get('tipos_espanto', []))} · "
            f"nível {f.get('nivel')} · surpresa {f.get('nota_surpresa')} · confiança {f.get('confianca')}",
            "",
            f"**{f.get('gancho', '')}**",
            "",
            f.get("explicacao", ""),
            "",
            "**Fontes:**",
            "",
        ]
        for fonte in f.get("fontes", []):
            partes += [f"- [{fonte.get('titulo')}]({fonte.get('url')}) ({fonte.get('idioma')})",
                       "", _citar(fonte.get("trecho", "")), ""]
        if f.get("aprofundar"):
            partes += ["**Aprofundar:**", ""]
            partes += [f"- {a.get('tipo')}: [{a.get('titulo')}]({a.get('url', '')})"
                       for a in f["aprofundar"]]
            partes.append("")
        partes += ["**Avaliação:** [ ] ok   [ ] errado   [ ] chato", "", "**Comentário:** ", ""]
    return "\n".join(partes)


def apurar(caminho: Path) -> dict:
    """Lê um .md de revisão marcado e conta ok/errado/chato/pendente/ambíguo por fato."""
    texto = caminho.read_text(encoding="utf-8")
    blocos = RE_ID.split(texto)
    # split com grupo: [antes, id1, depois1, id2, depois2, ...]
    resultado = {"ok": [], "errado": [], "chato": [], "pendente": [], "ambiguo": []}
    for i in range(1, len(blocos), 2):
        fid, corpo = blocos[i], blocos[i + 1]
        marcados = {m.group(2).lower() for m in RE_CAIXA.finditer(corpo) if m.group(1) in "xX"}
        if not marcados:
            resultado["pendente"].append(fid)
        elif len(marcados) > 1:
            resultado["ambiguo"].append(fid)
        else:
            resultado[marcados.pop()].append(fid)
    return resultado


def comentarios(caminho: Path) -> dict[str, str]:
    """Comentário livre de cada fato (linha **Comentário:**), quando preenchido."""
    blocos = RE_ID.split(caminho.read_text(encoding="utf-8"))
    saida = {}
    for i in range(1, len(blocos), 2):
        m = RE_COMENTARIO.search(blocos[i + 1])
        if m and m.group(1).strip():
            saida[blocos[i]] = m.group(1).strip()
    return saida


# chato → pouco_interessante; errado → revisao_humana (o comentário diz o porquê)
MOTIVO_POR_AVALIACAO = {"chato": "pouco_interessante", "errado": "revisao_humana"}


def descartar_reprovados(caminho: Path, dados: Path) -> list[str]:
    """Move de fatos/ para descartados/ os fatos marcados como errado ou chato.

    Grava em cada um o motivo e o registro da revisão (arquivo, avaliação, comentário, data).
    Devolve as linhas de relatório. Fatos que já não estão em fatos/ são ignorados.
    """
    r = apurar(caminho)
    notas = comentarios(caminho)
    alvo = {fid: aval for aval in MOTIVO_POR_AVALIACAO for fid in r[aval]}
    relatorio = []
    if not alvo:
        return relatorio
    for arq in sorted((dados / "fatos").glob("*.jsonl")):
        fatos = comum.carregar_fatos(arq)
        ficam, saem = [], []
        for f in fatos:
            (saem if f.get("id") in alvo else ficam).append(f)
        if not saem:
            continue
        destino = dados / "descartados" / arq.name
        descartados = comum.carregar_fatos(destino) if destino.exists() else []
        for f in saem:
            aval = alvo.pop(f["id"])
            f["motivo_descarte"] = MOTIVO_POR_AVALIACAO[aval]
            f["revisao_humana"] = {"arquivo": caminho.name, "avaliacao": aval,
                                   "comentario": notas.get(f["id"], ""), "em": comum.hoje()}
            descartados.append(f)
            relatorio.append(f"  {f['id']}: {aval} → descartados/{arq.name} ({f['motivo_descarte']})")
        comum.escrever_jsonl(destino, descartados)
        comum.escrever_jsonl(arq, ficam)
    for fid in alvo:
        relatorio.append(f"  {fid}: não está em fatos/ (já descartado?)")
    return relatorio


def _nome_livre(pasta: Path, base: str) -> str:
    nome, k = base, 2
    while (pasta / f"{nome}.md").exists():
        nome, k = f"{base}-{k}", k + 1
    return nome


def main(argv: list[str] | None = None) -> int:
    comum.configurar_saida()
    p = argparse.ArgumentParser(description="Sorteia fatos aprovados para revisão humana.")
    p.add_argument("--n", type=int, default=30, help="tamanho da amostra (padrão 30)")
    p.add_argument("--todos", action="store_true", help="inclui todos os fatos elegíveis")
    p.add_argument("--lotes", help="só fatos destes lotes (separados por vírgula)")
    p.add_argument("--semente", type=int, help="semente do sorteio (padrão: aleatória)")
    p.add_argument("--nome", help="nome do arquivo de saída (sem .md)")
    p.add_argument("--incluir-revisados", action="store_true",
                   help="permite sortear fatos que já estiveram em revisões anteriores")
    p.add_argument("--dados", type=Path, default=comum.DADOS_PADRAO)
    p.add_argument("--apurar", type=Path, metavar="ARQUIVO_MD", help="apura uma revisão marcada")
    p.add_argument("--descartar", action="store_true",
                   help="com --apurar: move os fatos marcados errado/chato para descartados/")
    args = p.parse_args(argv)
    if args.descartar and not args.apurar:
        p.error("--descartar só funciona junto com --apurar")

    if args.apurar:
        if not args.apurar.exists():
            print(f"Arquivo não encontrado: {args.apurar}", file=sys.stderr)
            return 2
        r = apurar(args.apurar)
        total = sum(len(v) for v in r.values())
        problemas = len(r["errado"]) + len(r["chato"])
        print(f"{args.apurar.name}: {total} fato(s)")
        for chave in ("ok", "errado", "chato", "pendente", "ambiguo"):
            ids = r[chave]
            print(f"  {chave:<9} {len(ids):>3}" + (f"  {', '.join(ids)}" if ids and chave != "ok" else ""))
        if r["pendente"] or r["ambiguo"]:
            print("Veredito: revisão incompleta (há fatos sem marcação ou com mais de uma caixa).")
        elif problemas <= 1:
            print(f"Veredito: {problemas} problema(s) → o bloco segue.")
        else:
            print(f"Veredito: {problemas} problemas → PAUSAR e diagnosticar qual etapa falhou.")
        if args.descartar:
            linhas = descartar_reprovados(args.apurar, args.dados)
            print("Descarte dos marcados como errado/chato:" if linhas else "Nada a descartar.")
            for linha in linhas:
                print(linha)
        return 0

    pasta_revisao = args.dados / "revisao"
    fatos = comum.todos_aprovados(args.dados)
    if args.lotes:
        lotes = {l.strip() for l in args.lotes.split(",") if l.strip()}
        fatos = [f for f in fatos if f.get("lote") in lotes]
    if not args.incluir_revisados:
        revisados = ids_ja_revisados(pasta_revisao)
        fatos = [f for f in fatos if f.get("id") not in revisados]
    if not fatos:
        print("Nenhum fato elegível para sorteio.", file=sys.stderr)
        return 1

    semente = args.semente if args.semente is not None else random.SystemRandom().randrange(10**6)
    n = None if args.todos else args.n
    if n is not None and n > len(fatos):
        print(f"Aviso: só há {len(fatos)} fato(s) elegível(is); todos entram na amostra.")
    escolhidos = sortear(fatos, n, semente)

    pasta_revisao.mkdir(parents=True, exist_ok=True)
    nome = args.nome or _nome_livre(pasta_revisao, f"amostra-{comum.hoje()}")
    destino = pasta_revisao / f"{nome}.md"
    if destino.exists():
        print(f"Já existe: {destino}. Escolha outro --nome.", file=sys.stderr)
        return 2
    destino.write_text(gerar_markdown(escolhidos, nome, semente), encoding="utf-8")
    print(f"{len(escolhidos)} fato(s) sorteado(s) → {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
