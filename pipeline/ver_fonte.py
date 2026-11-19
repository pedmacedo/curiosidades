"""Mostra o contexto em volta de palavras numa fonte do cache (para achar e copiar trechos literais).

Uso:
    python pipeline/ver_fonte.py <parte do nome do arquivo de cache> <palavra> [palavra ...] [--largura 300] [--max 4]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import comum

CACHE = Path(__file__).resolve().parent.parent / "dados" / "cache_fontes"


def main(argv: list[str] | None = None) -> int:
    comum.configurar_saida()
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("arquivo")
    p.add_argument("palavras", nargs="+")
    p.add_argument("--largura", type=int, default=300)
    p.add_argument("--max", type=int, default=4)
    args = p.parse_args(argv)
    candidatos = sorted(CACHE.glob(f"*{args.arquivo}*.txt"), key=lambda c: ("html" in c.name, c.name))
    if not candidatos:
        print("nenhum arquivo de cache com esse nome")
        return 1
    arq = candidatos[0]
    texto = arq.read_text(encoding="utf-8")
    print(f"# {arq.name} ({len(texto)} caracteres)")
    baixo = texto.lower()
    for palavra in args.palavras:
        pos, n = 0, 0
        while n < args.max:
            i = baixo.find(palavra.lower(), pos)
            if i < 0:
                break
            ini = max(0, i - args.largura // 2)
            print(f"\n[{palavra}] …{texto[ini: i + args.largura // 2]}…".replace("\n", " "))
            pos, n = i + args.largura // 2, n + 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
