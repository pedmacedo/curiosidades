"""Acrescenta vereditos do verificador ao <lote>.vereditos.json, assim que eles chegam.

Uso:
    python pipeline/gravar_vereditos.py dados/lotes/<lote>.jsonl --rodada 1 < vereditos.json

A entrada é um array JSON (a resposta do verificador). Um veredito com o mesmo id na mesma
rodada substitui o anterior. Grava logo, para nada se perder se a sessão acabar no meio.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import comum


def main(argv: list[str] | None = None) -> int:
    comum.configurar_saida()
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("lote", type=Path)
    p.add_argument("--rodada", required=True, type=int)
    args = p.parse_args(argv)
    novos = json.loads(sys.stdin.buffer.read().decode("utf-8"))
    ids_lote = {f["id"] for f in comum.carregar_fatos(args.lote)}
    desconhecidos = [v.get("id") for v in novos if v.get("id") not in ids_lote]
    if desconhecidos:
        print(f"ERRO: ids fora do lote: {desconhecidos}")
        return 1
    validos = {"aprovado", "reprovado", "ajustar"}
    if any(v.get("veredito") not in validos for v in novos):
        print("ERRO: veredito inválido")
        return 1
    nome = args.lote.name[: -len(".jsonl")]
    arq = args.lote.with_name(f"{nome}.vereditos.json")
    dados = comum.carregar_json(arq) if arq.exists() else {"lote": nome, "rodadas": {}}
    rodada = dados["rodadas"].setdefault(str(args.rodada), [])
    por_id = {v["id"]: v for v in rodada}
    for v in novos:
        por_id[v["id"]] = {k: v[k] for k in ("id", "veredito", "nota_surpresa", "motivo", "correcao", "ajuste_pontual") if v.get(k) not in (None, "")}
    dados["rodadas"][str(args.rodada)] = sorted(por_id.values(), key=lambda v: v["id"])
    # grava num temporário e só então substitui: uma falha no meio não apaga o que já havia
    tmp = arq.with_name(arq.name + ".tmp")
    tmp.write_text(json.dumps(dados, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    tmp.replace(arq)
    from collections import Counter
    c = Counter(v["veredito"] for v in dados["rodadas"][str(args.rodada)])
    print(f"{arq.name}: rodada {args.rodada} com {sum(c.values())} veredito(s) {dict(c)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
