"""Utilidades comuns aos testes: caminho do pipeline e fixtures mínimas."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "pipeline"))

TAXONOMIA = {
    "areas": [
        {"id": "biologia", "nome": "Biologia", "temas": [
            {"id": "microbiologia", "nome": "Microbiologia", "descricao": "Vida microscópica",
             "vizinhos": ["geologia_profunda", "astrobiologia"]},
        ]},
        {"id": "terra", "nome": "Terra", "temas": [
            {"id": "geologia_profunda", "nome": "Geologia profunda", "descricao": "Crosta e manto",
             "vizinhos": ["microbiologia", "astrobiologia"]},
        ]},
        {"id": "espaco", "nome": "Espaço", "temas": [
            {"id": "astrobiologia", "nome": "Astrobiologia", "descricao": "Vida fora da Terra",
             "vizinhos": ["microbiologia", "geologia_profunda"]},
        ]},
    ]
}

EXPLICACAO = " ".join(["palavra"] * 100)

FATO = {
    "id": "microbiologia-0001",
    "area": "biologia",
    "tema": "microbiologia",
    "temas_secundarios": ["geologia_profunda"],
    "tipos_espanto": ["escala_absurda", "contraintuitivo"],
    "gancho": "Há microrganismos vivendo em rochas a quilômetros de profundidade, com metabolismo lentíssimo.",
    "explicacao": EXPLICACAO,
    "nivel": 1,
    "nota_surpresa": 4,
    "confianca": "alta",
    "fontes": [{"url": "https://en.wikipedia.org/wiki/Deep_biosphere", "titulo": "Deep biosphere",
                "idioma": "en", "trecho": "The deep biosphere is the part of the biosphere that resides below the first few meters of the surface.",
                "acessado_em": "2026-11-17"}],
    "lote": "2026-11-17-biologia-01",
    "verificado_em": "2026-11-17",
}


def fato(**mudancas) -> dict:
    f = copy.deepcopy(FATO)
    for chave, valor in mudancas.items():
        if valor is None:
            f.pop(chave, None)
        else:
            f[chave] = valor
    return f


def montar_dados(base: Path, taxonomia: dict | None = TAXONOMIA) -> Path:
    """Cria uma pasta dados/ mínima dentro de `base` e devolve o caminho."""
    dados = base / "dados"
    for sub in ("fatos", "descartados", "lotes", "revisao", "cache_fontes"):
        (dados / sub).mkdir(parents=True, exist_ok=True)
    tipos = json.loads((RAIZ / "dados" / "tipos_espanto.json").read_text(encoding="utf-8"))
    (dados / "tipos_espanto.json").write_text(json.dumps(tipos, ensure_ascii=False), encoding="utf-8")
    if taxonomia is not None:
        (dados / "taxonomia.json").write_text(json.dumps(taxonomia, ensure_ascii=False), encoding="utf-8")
    return dados


def gravar(caminho: Path, fatos: list[dict]) -> Path:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in fatos), encoding="utf-8")
    return caminho
