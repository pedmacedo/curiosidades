"""Aplica os vereditos do verificador a um lote (passo 6 do pipeline).

Uso:
    python pipeline/aplicar_vereditos.py dados/lotes/<lote>.jsonl
    python pipeline/aplicar_vereditos.py dados/lotes/<lote>.jsonl --simular

Lê <lote>.vereditos.json (rodadas do verificador) e <lote>.checagem.json (checar_citacoes).
Para cada fato vale o veredito da rodada mais recente em que ele aparece:
- aprovado (com nota ≥ 3) → dados/fatos/<area>.jsonl, com nota_surpresa do verificador e verificado_em;
- aprovado com nota < 3 → descartado (pouco_interessante);
- reprovado → dados/descartados/<area>.jsonl, com motivo_descarte (rótulo do início do motivo);
- sem fonte confirmada na checagem e sem veredito → descartado (citacao_nao_encontrada).
Fatos com "ajustar" na última rodada ou sem veredito interrompem a aplicação (código 1),
a menos que se use --descartar-pendentes. Ids já gravados em fatos/ ou descartados/ são pulados.

Formato de <lote>.vereditos.json:
    {"lote": "...", "rodadas": {"1": [{"id", "veredito", "nota_surpresa", "motivo", ...}], "2": [...]}}
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import comum


def ultimo_veredito(vereditos: dict) -> dict[str, dict]:
    finais: dict[str, dict] = {}
    for rodada in sorted(vereditos.get("rodadas", {}), key=int):
        for v in vereditos["rodadas"][rodada]:
            finais[v["id"]] = {**v, "rodada": int(rodada)}
    return finais


def rotulo_motivo(motivo: str) -> str:
    rotulo = (motivo or "").split(":")[0].strip()
    return rotulo if rotulo in comum.MOTIVOS_DESCARTE else "reprovado_verificador"


def decidir(fatos: list[dict], finais: dict[str, dict], checagem: dict[str, dict],
            descartar_pendentes: bool) -> tuple[list[dict], list[dict], list[str]]:
    aprovados, descartados, pendencias = [], [], []
    for fato in fatos:
        fid = fato["id"]
        v = finais.get(fid)
        if v is None:
            if checagem.get(fid, {}).get("status") == "falhou":
                descartados.append({**fato, "motivo_descarte": "citacao_nao_encontrada"})
            elif descartar_pendentes:
                descartados.append({**fato, "motivo_descarte": "reprovado_verificador: sem veredito"})
            else:
                pendencias.append(f"{fid}: sem veredito")
            continue
        if v["veredito"] == "aprovado":
            nota = v.get("nota_surpresa", fato.get("nota_surpresa"))
            novo = {**fato, "nota_surpresa": nota}
            if nota < 3:
                descartados.append({**novo, "motivo_descarte": "pouco_interessante"})
            else:
                aprovados.append(novo)
        elif v["veredito"] == "reprovado":
            descartados.append({**fato, "nota_surpresa": v.get("nota_surpresa", fato.get("nota_surpresa")),
                                "motivo_descarte": rotulo_motivo(v.get("motivo", ""))})
        elif descartar_pendentes:
            descartados.append({**fato, "motivo_descarte": "reprovado_verificador: ajuste não concluído"})
        else:
            pendencias.append(f"{fid}: último veredito é '{v['veredito']}' (rodada {v['rodada']})")
    return aprovados, descartados, pendencias


def ids_gravados(pasta: Path) -> set[str]:
    ids: set[str] = set()
    for arq in pasta.glob("*.jsonl"):
        ids |= {f.get("id") for f in comum.carregar_fatos(arq)}
    return ids


def acrescentar(pasta: Path, fatos: list[dict], ja_existem: set[str]) -> tuple[int, list[str]]:
    gravados, pulados = 0, []
    por_area: dict[str, list[dict]] = {}
    for f in fatos:
        if f["id"] in ja_existem:
            pulados.append(f["id"])
        else:
            por_area.setdefault(f["area"], []).append(f)
    for area, lista in por_area.items():
        destino = pasta / f"{area}.jsonl"
        existentes = comum.carregar_fatos(destino) if destino.exists() else []
        comum.escrever_jsonl(destino, existentes + lista)
        gravados += len(lista)
    return gravados, pulados


def main(argv: list[str] | None = None) -> int:
    comum.configurar_saida()
    p = argparse.ArgumentParser(description="Aplica os vereditos do verificador a um lote.")
    p.add_argument("lote", type=Path, help="dados/lotes/<lote>.jsonl")
    p.add_argument("--vereditos", type=Path, help="padrão: <lote>.vereditos.json")
    p.add_argument("--checagem", type=Path, help="padrão: <lote>.checagem.json")
    p.add_argument("--dados", type=Path, default=comum.DADOS_PADRAO)
    p.add_argument("--data", default=comum.hoje(), help="data de verificação (AAAA-MM-DD)")
    p.add_argument("--descartar-pendentes", action="store_true",
                   help="descarta fatos sem veredito final em vez de interromper")
    p.add_argument("--simular", action="store_true", help="só mostra o que faria")
    args = p.parse_args(argv)

    if not args.lote.exists():
        print(f"Lote não encontrado: {args.lote}", file=sys.stderr)
        return 2
    base = args.lote.with_suffix("")
    caminho_v = args.vereditos or base.with_name(base.name + ".vereditos.json")
    caminho_c = args.checagem or base.with_name(base.name + ".checagem.json")
    if not caminho_v.exists():
        print(f"Arquivo de vereditos não encontrado: {caminho_v}", file=sys.stderr)
        return 2
    finais = ultimo_veredito(comum.carregar_json(caminho_v))
    checagem = {}
    if caminho_c.exists():
        checagem = {f["id"]: f for f in comum.carregar_json(caminho_c).get("fatos", [])}

    fatos = comum.carregar_fatos(args.lote)
    aprovados, descartados, pendencias = decidir(fatos, finais, checagem, args.descartar_pendentes)
    for f in aprovados:
        f["verificado_em"] = args.data

    if pendencias:
        print("Pendências (resolva ou use --descartar-pendentes):")
        for linha in pendencias:
            print(f"  {linha}")
        return 1

    print(f"{len(fatos)} candidato(s): {len(aprovados)} aprovado(s), {len(descartados)} descartado(s)")
    for f in descartados:
        print(f"  descartado  {f['id']}: {f['motivo_descarte']}")
    if args.simular:
        print("(simulação: nada foi gravado)")
        return 0

    ja = ids_gravados(args.dados / "fatos") | ids_gravados(args.dados / "descartados")
    n_ap, pul_ap = acrescentar(args.dados / "fatos", aprovados, ja)
    n_de, pul_de = acrescentar(args.dados / "descartados", descartados, ja)
    print(f"Gravados: {n_ap} em fatos/, {n_de} em descartados/")
    if pul_ap or pul_de:
        print(f"Pulados (já gravados antes): {', '.join(pul_ap + pul_de)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
