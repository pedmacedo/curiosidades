"""Monta um lote de candidatos a partir de um arquivo Python e confere os trechos no cache.

Uso:
    python pipeline/montar_lote.py candidatos.py            # grava dados/lotes/<LOTE>.jsonl
    python pipeline/montar_lote.py candidatos.py --online   # baixa fontes que faltarem no cache

O arquivo de candidatos é um módulo Python que define:
    LOTE = "AAAA-MM-DD-<tema>-NN"
    AREA = "<id da área>"
    TEMA = "<id do tema>"
    CANDIDATOS = [ {temas_secundarios, tipos_espanto, gancho, explicacao, nivel,
                    nota_surpresa, confianca, fontes: [{url, titulo, idioma, trecho}], aprofundar?}, ... ]
Python facilita escrever textos longos em português e reaproveitar trechos entre rodadas
(um módulo de rodada 2 pode importar o da rodada 1 e trocar só o que mudou).

Os ids são <TEMA>-NNNN, numerados na ordem da lista, a partir do maior id já usado para o tema
em dados/fatos, dados/descartados e em outros lotes (regravar o mesmo lote mantém os ids dele).
Para cada candidato, mostra o status da checagem de citações, o número de palavras e os avisos.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

import checar_citacoes as cc
import comum


def carregar_modulo(caminho: Path):
    spec = importlib.util.spec_from_file_location("candidatos", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    for nome in ("LOTE", "AREA", "TEMA", "CANDIDATOS"):
        if not hasattr(modulo, nome):
            raise SystemExit(f"{caminho} não define {nome}")
    return modulo


def maior_id_usado(dados: Path, tema: str, ignorar_lote: str) -> int:
    padrao = re.compile(re.escape(tema) + r"-(\d{4})$")
    maior = 0
    arquivos = list((dados / "fatos").glob("*.jsonl")) + list((dados / "descartados").glob("*.jsonl"))
    arquivos += [a for a in (dados / "lotes").glob("*.jsonl") if a.stem != ignorar_lote]
    for arq in arquivos:
        for fato in comum.carregar_fatos(arq):
            if fato.get("lote") == ignorar_lote:
                continue
            m = padrao.match(str(fato.get("id", "")))
            if m:
                maior = max(maior, int(m.group(1)))
    return maior


def main(argv: list[str] | None = None) -> int:
    comum.configurar_saida()
    p = argparse.ArgumentParser(description="Monta um lote de candidatos e confere os trechos.")
    p.add_argument("candidatos", type=Path, help="arquivo .py com LOTE, AREA, TEMA e CANDIDATOS")
    p.add_argument("--dados", type=Path, default=comum.DADOS_PADRAO)
    p.add_argument("--online", action="store_true", help="baixa as fontes que não estão no cache")
    p.add_argument("--data", default=comum.hoje(), help="acessado_em padrão das fontes")
    args = p.parse_args(argv)

    mod = carregar_modulo(args.candidatos)
    inicio = maior_id_usado(args.dados, mod.TEMA, mod.LOTE)
    baixador = cc.Baixador(args.dados / "cache_fontes", offline=not args.online)

    saida, problemas = [], 0
    for i, c in enumerate(mod.CANDIDATOS, start=inicio + 1):
        fato = {"id": f"{mod.TEMA}-{i:04d}", "area": mod.AREA, "tema": mod.TEMA, **c}
        fato.setdefault("temas_secundarios", [])
        for fonte in fato["fontes"]:
            fonte.setdefault("acessado_em", args.data)
        fato["lote"] = mod.LOTE
        res = cc.checar_fato(fato, baixador)
        palavras = len(fato["explicacao"].split())
        alertas = []
        if len(fato["gancho"]) > 220:
            alertas.append(f"gancho com {len(fato['gancho'])} caracteres")
        if not 80 <= palavras <= 250:
            alertas.append(f"explicação com {palavras} palavras")
        if res["aviso_numero"]:
            alertas.append(f"números sem trecho: {', '.join(res['aviso_numero'])}")
        for f in res["fontes"]:
            if f["status"] == "falhou":
                alertas.append(f"fonte falhou: {f['url']} ({f.get('motivo')})")
        if res["status"] == "falhou" or alertas:
            problemas += 1
        print(f"{fato['id']}: {res['status']:<10} {palavras:>3} palavras" + (f"  ⚠ {'; '.join(alertas)}" if alertas else ""))
        saida.append(fato)

    destino = args.dados / "lotes" / f"{mod.LOTE}.jsonl"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in saida), encoding="utf-8")
    print(f"\n{len(saida)} candidato(s) → {destino}" + (f" · {problemas} com pendências" if problemas else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
