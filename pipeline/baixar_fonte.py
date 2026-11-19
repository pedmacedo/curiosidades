"""Baixa fontes para dados/cache_fontes antes de escrever candidatos.

Uso: python pipeline/baixar_fonte.py "<url1>" "<url2>" ...
"""
import sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "pipeline"))
import comum; comum.configurar_saida()
from checar_citacoes import Baixador
b = Baixador(RAIZ / "dados" / "cache_fontes")
for url in sys.argv[1:]:
    for v in b.variantes(url):
        try:
            t, p = b.texto(url, v)
            print("OK", len(t), p.name)
        except Exception as e:
            print("FALHA", url, v, e)
