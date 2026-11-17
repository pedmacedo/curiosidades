"""Estatísticas do acervo: descarte por lote, motivos, rodadas do verificador e cobertura por tema.

Uso:
    python pipeline/estatisticas.py              # resumo legível
    python pipeline/estatisticas.py --markdown   # tabelas prontas para colar no PROGRESSO.md
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

import comum


def carregar_pasta(pasta: Path) -> list[dict]:
    fatos: list[dict] = []
    for arq in sorted(pasta.glob("*.jsonl")):
        fatos.extend(comum.carregar_fatos(arq))
    return fatos


def resumo_lotes(dados: Path) -> list[dict]:
    aprovados = carregar_pasta(dados / "fatos")
    descartados = carregar_pasta(dados / "descartados")
    linhas = []
    nomes = {f.get("lote") for f in aprovados + descartados} | {
        p.name[: -len(".vereditos.json")] for p in (dados / "lotes").glob("*.vereditos.json")}
    for lote in sorted(n for n in nomes if n):
        ap = [f for f in aprovados if f.get("lote") == lote]
        de = [f for f in descartados if f.get("lote") == lote]
        arq_v = dados / "lotes" / f"{lote}.vereditos.json"
        rodada1: Counter = Counter()
        ajustes = 0
        if arq_v.exists():
            rodadas = comum.carregar_json(arq_v).get("rodadas", {})
            rodada1 = Counter(v["veredito"] for v in rodadas.get("1", []))
            ajustes = sum(1 for r in rodadas.values() for v in r if v["veredito"] == "ajustar")
        total = len(ap) + len(de)
        tema = (ap or de)[0]["tema"] if (ap or de) else lote
        linhas.append({
            "lote": lote, "tema": tema, "candidatos": total, "aprovados": len(ap), "descartados": len(de),
            "taxa_descarte": (len(de) / total) if total else 0.0,
            "motivos": Counter(f.get("motivo_descarte", "?").split(":")[0] for f in de),
            "rodada1": rodada1, "pedidos_de_ajuste": ajustes,
            "nota_media": (sum(f["nota_surpresa"] for f in ap) / len(ap)) if ap else 0.0,
        })
    return linhas


def cobertura(dados: Path) -> tuple[Counter, int, int]:
    taxonomia = comum.carregar_taxonomia(dados)
    temas = comum.indice_temas(taxonomia)
    por_tema = Counter(f["tema"] for f in carregar_pasta(dados / "fatos"))
    cobertos = sum(1 for t in temas if por_tema[t] > 0)
    return por_tema, cobertos, len(temas)


def _pct(x: float) -> str:
    return f"{100 * x:.0f}%"


def main(argv: list[str] | None = None) -> int:
    comum.configurar_saida()
    p = argparse.ArgumentParser(description="Estatísticas do acervo de fatos.")
    p.add_argument("--dados", type=Path, default=comum.DADOS_PADRAO)
    p.add_argument("--markdown", action="store_true", help="saída em tabelas Markdown")
    args = p.parse_args(argv)

    lotes = resumo_lotes(args.dados)
    por_tema, cobertos, total_temas = cobertura(args.dados)
    n_ap = sum(l["aprovados"] for l in lotes)
    n_de = sum(l["descartados"] for l in lotes)

    if args.markdown:
        print("| Lote | Tema | Candidatos | Aprovados | Descartados | Descarte | Rodada 1 (apr/ajus/repr) | Motivos | Nota média |")
        print("|---|---|---|---|---|---|---|---|---|")
        for l in lotes:
            r1 = l["rodada1"]
            motivos = ", ".join(f"{m} {n}" for m, n in l["motivos"].most_common()) or "—"
            print(f"| {l['lote']} | {l['tema']} | {l['candidatos']} | {l['aprovados']} | {l['descartados']} | "
                  f"{_pct(l['taxa_descarte'])} | {r1['aprovado']}/{r1['ajustar']}/{r1['reprovado']} | {motivos} | "
                  f"{l['nota_media']:.1f} |")
        total = n_ap + n_de
        print(f"| **Total** | | {total} | {n_ap} | {n_de} | {_pct(n_de / total) if total else '—'} | | | |")
        print(f"\nCobertura: {cobertos} de {total_temas} temas com pelo menos um fato aprovado.")
        return 0

    print(f"Aprovados: {n_ap} · Descartados: {n_de} · Temas cobertos: {cobertos}/{total_temas}\n")
    for l in lotes:
        r1 = l["rodada1"]
        print(f"{l['lote']}  ({l['tema']})")
        print(f"  {l['candidatos']} candidatos → {l['aprovados']} aprovados, {l['descartados']} descartados "
              f"({_pct(l['taxa_descarte'])} de descarte), nota média {l['nota_media']:.1f}")
        print(f"  1ª rodada do verificador: {r1['aprovado']} aprovados, {r1['ajustar']} ajustar, "
              f"{r1['reprovado']} reprovados")
        if l["motivos"]:
            print("  motivos: " + ", ".join(f"{m} ({n})" for m, n in l["motivos"].most_common()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
