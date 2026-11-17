"""Funções e constantes compartilhadas pelos scripts do pipeline."""

from __future__ import annotations

import datetime as _dt
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS_PADRAO = RAIZ / "dados"

# Lista fixa (§4.2). O arquivo dados/tipos_espanto.json tem prioridade, se existir.
TIPOS_ESPANTO_PADRAO = [
    "escala_absurda",
    "contraintuitivo",
    "origem_inesperada",
    "conexao_inesperada",
    "mito_desmentido",
    "misterio_aberto",
    "engenhosidade",
    "historia_humana",
]

MOTIVOS_DESCARTE = [
    "citacao_nao_encontrada",
    "mito",
    "fonte_fraca",
    "pouco_interessante",
    "numero_divergente",
    "duplicado",
    "exagero",
    "reprovado_verificador",
    "revisao_humana",
]

CONFIANCAS = ["alta", "consenso_parcial", "hipotese"]
TIPOS_APROFUNDAR = ["video", "artigo", "livro", "podcast"]


def configurar_saida() -> None:
    """Garante saída UTF-8 no console (o padrão do Windows quebra com acentos e símbolos)."""
    for fluxo in (sys.stdout, sys.stderr):
        try:
            fluxo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def hoje() -> str:
    return _dt.date.today().isoformat()


def data_valida(texto: object) -> bool:
    if not isinstance(texto, str):
        return False
    try:
        _dt.date.fromisoformat(texto)
    except ValueError:
        return False
    return len(texto) == 10


def ler_jsonl(caminho: Path) -> list[tuple[int, dict | None, str | None]]:
    """Lê um .jsonl. Devolve (nº da linha, objeto ou None, erro ou None). Linhas vazias são ignoradas."""
    saida = []
    with open(caminho, encoding="utf-8") as f:
        for n, linha in enumerate(f, start=1):
            linha = linha.strip()
            if not linha:
                continue
            try:
                obj = json.loads(linha)
            except json.JSONDecodeError as e:
                saida.append((n, None, f"JSON inválido: {e}"))
                continue
            if not isinstance(obj, dict):
                saida.append((n, None, "a linha não é um objeto JSON"))
                continue
            saida.append((n, obj, None))
    return saida


def carregar_fatos(caminho: Path) -> list[dict]:
    """Lê um .jsonl ignorando linhas inválidas (use validar.py para achá-las)."""
    return [obj for _, obj, erro in ler_jsonl(caminho) if obj is not None]


def escrever_jsonl(caminho: Path, objetos: list[dict]) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with open(caminho, "w", encoding="utf-8", newline="\n") as f:
        for obj in objetos:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def carregar_json(caminho: Path):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def carregar_taxonomia(dados: Path) -> dict | None:
    caminho = dados / "taxonomia.json"
    if not caminho.exists():
        return None
    return carregar_json(caminho)


def carregar_tipos_espanto(dados: Path) -> list[str]:
    caminho = dados / "tipos_espanto.json"
    if not caminho.exists():
        return list(TIPOS_ESPANTO_PADRAO)
    conteudo = carregar_json(caminho)
    return [t["id"] for t in conteudo.get("tipos", []) if isinstance(t, dict) and "id" in t]


def indice_temas(taxonomia: dict | None) -> dict[str, dict]:
    """Mapeia id do tema → {"area": id_area, **tema}."""
    indice: dict[str, dict] = {}
    if not taxonomia:
        return indice
    for area in taxonomia.get("areas", []):
        for tema in area.get("temas", []):
            if isinstance(tema, dict) and "id" in tema:
                indice[tema["id"]] = {"area": area.get("id"), **tema}
    return indice


def todos_aprovados(dados: Path) -> list[dict]:
    fatos = []
    for arq in sorted((dados / "fatos").glob("*.jsonl")):
        fatos.extend(carregar_fatos(arq))
    return fatos
