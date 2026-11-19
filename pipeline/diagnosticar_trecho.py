"""Mostra qual pedaço de um trecho citado não aparece na fonte (ajuda a corrigir o passo 2 do lote).

Uso:
    python pipeline/diagnosticar_trecho.py dados/lotes/<lote>.jsonl [id ...]

Para cada fonte que falhou, testa cada pedaço (separado por "[...]") contra o texto do cache
e, para os que faltam, mostra o trecho mais parecido da página.
"""

from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path

import comum
from checar_citacoes import Baixador, conferir_trecho, fragmentos, normalizar

RAIZ = Path(__file__).resolve().parent.parent


def divergencia(frag: str, texto: str) -> tuple[str, str]:
    """Maior prefixo do pedaço que existe na fonte; devolve (onde diverge no pedaço, na fonte)."""
    lo, hi = 0, len(frag)
    while lo < hi:  # busca binária pelo maior prefixo presente
        meio = (lo + hi + 1) // 2
        if frag[:meio] in texto:
            lo = meio
        else:
            hi = meio - 1
    if lo == 0:
        sm = difflib.SequenceMatcher(None, texto, frag, autojunk=False)
        b = max(sm.get_matching_blocks(), key=lambda x: x.size)
        return frag[:80], texto[max(0, b.a - b.b): max(0, b.a - b.b) + 80]
    i = texto.find(frag[:lo])
    return frag[max(0, lo - 40): lo + 60], texto[i + max(0, lo - 40): i + lo + 60]


def main(argv: list[str] | None = None) -> int:
    comum.configurar_saida()
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("lote", type=Path)
    p.add_argument("ids", nargs="*")
    p.add_argument("--cache", type=Path, default=RAIZ / "dados" / "cache_fontes")
    args = p.parse_args(argv)
    baixador = Baixador(args.cache, offline=True)
    for fato in comum.carregar_fatos(args.lote):
        if args.ids and fato["id"] not in args.ids:
            continue
        for fonte in fato.get("fontes", []):
            textos = []
            for variante in baixador.variantes(fonte["url"]):
                try:
                    textos.append(baixador.texto(fonte["url"], variante)[0])
                except Exception:
                    pass
            if not textos:
                print(f"{fato['id']}: sem cache para {fonte['url']}")
                continue
            if any(conferir_trecho(fonte["trecho"], t).status in ("ok", "aproximado") for t in textos):
                continue
            norm = normalizar(textos[0])
            print(f"\n{fato['id']} · {fonte['url']}")
            for frag in fragmentos(fonte["trecho"]):
                if frag in norm:
                    continue
                no_trecho, na_fonte = divergencia(frag, norm)
                print(f"  diverge no trecho: …{no_trecho}…")
                print(f"           na fonte: …{na_fonte}…")
    return 0


if __name__ == "__main__":
    sys.exit(main())
