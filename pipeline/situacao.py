"""Situação da produção (Fase 4): o que está pela metade, o que vem a seguir e se é hora de revisão.

Feito para retomar o trabalho de onde parou, em qualquer sessão:

    python pipeline/situacao.py            # lotes em andamento, próximos temas, amostragem
    python pipeline/situacao.py --fila 20  # mostra mais temas da fila

A etapa de cada lote é deduzida só pelos arquivos que existem:
  candidatos/<lote>.py → lotes/<lote>.jsonl → <lote>.checagem.json → <lote>.vereditos.json
  → fatos aplicados (algum fato do lote em fatos/ ou descartados/).

A fila de temas é um rodízio pelas áreas, na ordem da taxonomia (1º tema de cada área, depois o
2º de cada área...), para o acervo crescer equilibrado e o questionário cobrir todas as áreas cedo.
Tema "feito" = tem algum lote aplicado.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import comum

RAIZ = Path(__file__).resolve().parent.parent


def fila_de_temas(taxonomia: dict) -> list[tuple[str, str]]:
    areas = taxonomia["areas"]
    fila = []
    for i in range(max(len(a["temas"]) for a in areas)):
        for a in areas:
            if i < len(a["temas"]):
                fila.append((a["id"], a["temas"][i]["id"]))
    return fila


def nome_base_lote(arquivo: Path) -> str:
    """'2026-11-17-amazonia-01-r2.py' → '2026-11-17-amazonia-01'."""
    return re.sub(r"-r\d+$", "", arquivo.stem)


def tema_do_lote(lote: str) -> str:
    """'2026-11-17-palavras_viajantes-01' → 'palavras_viajantes'."""
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", re.sub(r"-\d+$", "", lote))


def etapa_do_lote(dados: Path, lote: str, aplicados: set[str]) -> tuple[str, str]:
    """(etapa concluída, próximo passo)."""
    if lote in aplicados:
        return "aplicado", "—"
    lotes = dados / "lotes"
    cand = sorted((dados / "candidatos").glob(f"{lote}*.py"))
    if (lotes / f"{lote}.vereditos.json").exists():
        rodadas = comum.carregar_json(lotes / f"{lote}.vereditos.json").get("rodadas", {})
        ultima = max(rodadas, key=int) if rodadas else "0"
        pendentes = [v["id"] for v in rodadas.get(ultima, []) if v["veredito"] == "ajustar"]
        if pendentes and ultima == "1":
            if (dados / "candidatos" / f"{lote}-r2.py").exists():
                return (f"verificado (rodada 1; {len(pendentes)} para ajustar; r2 já escrito)",
                        f"montar e checar candidatos/{lote}-r2.py (se ainda não foi) e mandar "
                        f"{len(pendentes)} fato(s) à 2ª rodada do verificador")
            return (f"verificado (rodada 1; {len(pendentes)} para ajustar)",
                    f"escrever candidatos/{lote}-r2.py, montar, checar e rodar a 2ª rodada")
        return (f"verificado (rodada {ultima})",
                f"python pipeline/aplicar_vereditos.py dados/lotes/{lote}.jsonl")
    if (lotes / f"{lote}.checagem.json").exists():
        return "citações checadas", "mandar ao verificador e gravar <lote>.vereditos.json"
    if (lotes / f"{lote}.jsonl").exists():
        return "montado", f"python pipeline/checar_citacoes.py dados/lotes/{lote}.jsonl"
    if cand:
        return "candidatos escritos", f"python pipeline/montar_lote.py dados/candidatos/{cand[-1].name}"
    return "?", "?"


def lotes_revisados(dados: Path, por_id: dict[str, dict]) -> set[str]:
    """Lotes que já tiveram algum fato numa amostra de revisão humana."""
    revisados = set()
    for md in (dados / "revisao").glob("*.md"):
        for fid in re.findall(r"<!-- id: ([\w-]+) -->", md.read_text(encoding="utf-8")):
            if fid in por_id and por_id[fid].get("lote"):
                revisados.add(por_id[fid]["lote"])
    return revisados


def main(argv: list[str] | None = None) -> int:
    comum.configurar_saida()
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--dados", type=Path, default=RAIZ / "dados")
    p.add_argument("--fila", type=int, default=8, help="quantos temas da fila mostrar")
    args = p.parse_args(argv)
    dados = args.dados

    taxonomia = comum.carregar_taxonomia(dados)
    aprovados = comum.todos_aprovados(dados)
    descartados = [f for arq in sorted((dados / "descartados").glob("*.jsonl")) for f in comum.carregar_fatos(arq)]
    aplicados = {f["lote"] for f in aprovados + descartados if f.get("lote")}
    temas_feitos = {f["tema"] for f in aprovados + descartados}

    # lotes em andamento: têm candidatos ou arquivos em lotes/, mas nenhum fato aplicado
    nomes = {nome_base_lote(a) for a in (dados / "candidatos").glob("*.py")}
    nomes |= {a.name.split(".")[0] for a in (dados / "lotes").glob("*.jsonl")}
    em_andamento = sorted(n for n in nomes if n not in aplicados)

    fila = fila_de_temas(taxonomia)
    temas_andamento = {tema_do_lote(n) for n in em_andamento}
    pendentes = [(a, t) for a, t in fila if t not in temas_feitos and t not in temas_andamento]

    print(f"Temas feitos: {len(temas_feitos)} de {len(fila)}  ·  fatos aprovados: {len(aprovados)}"
          f"  ·  descartados: {len(descartados)}")

    print("\nLotes em andamento:" if em_andamento else "\nLotes em andamento: nenhum")
    for lote in em_andamento:
        etapa, proximo = etapa_do_lote(dados, lote, aplicados)
        print(f"  {lote}: {etapa}\n    próximo passo: {proximo}")

    por_id = {f["id"]: f for f in aprovados}
    revisados = lotes_revisados(dados, por_id)
    sem_revisao = [f for f in aprovados if f.get("lote") not in revisados]
    # A amostragem periódica foi dispensada pelo Pedro em 2026-11-18 (CLAUDE.md §5.4): só informa.
    print(f"\nAprovados de lotes sem amostra de revisão humana: {len(sem_revisao)} (amostragem dispensada)")

    print(f"\nPróximos temas da fila ({len(pendentes)} pendentes):")
    nomes_temas = comum.indice_temas(taxonomia)
    for area, tema in pendentes[: args.fila]:
        print(f"  {area:16} {tema:28} {nomes_temas[tema].get('nome', '')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
