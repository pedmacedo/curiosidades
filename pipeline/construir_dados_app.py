"""Gera os arquivos de dados do app (app/data/) a partir de dados/ (§6.3).

Uso:
    python pipeline/construir_dados_app.py            # valida e gera app/data/
    python pipeline/construir_dados_app.py --sem-validar

Saídas:
    app/data/fatos.json         só os campos que o app usa
    app/data/taxonomia.json     áreas → temas, com vizinhos
    app/data/tipos_espanto.json
    app/data/versao.js          versões dos dados e do código do app (hashes), lidas pelo
                                service worker para dar nome ao cache

Rode de novo também depois de mudar o código do app: a versão do app muda e o celular
baixa a versão nova na próxima abertura.

Nunca edite app/data/ à mão: rode este script de novo.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import comum
import validar

APP_DATA_PADRAO = comum.RAIZ / "app" / "data"

CAMPOS_FATO = ["id", "area", "tema", "temas_secundarios", "tipos_espanto", "gancho", "explicacao",
               "nivel", "nota_surpresa", "confianca"]


def fato_para_app(f: dict) -> dict:
    saida = {c: f[c] for c in CAMPOS_FATO if c in f}
    saida.setdefault("temas_secundarios", [])
    saida["fontes"] = [{"url": x["url"], "titulo": x.get("titulo", x["url"])} for x in f.get("fontes", [])]
    if f.get("aprofundar"):
        saida["aprofundar"] = [{"tipo": a["tipo"], "titulo": a["titulo"], "url": a["url"]} for a in f["aprofundar"]]
    return saida


def taxonomia_para_app(tax: dict) -> dict:
    return {"areas": [
        {"id": a["id"], "nome": a["nome"], "temas": [
            {"id": t["id"], "nome": t["nome"], "vizinhos": t.get("vizinhos", [])} for t in a["temas"]]}
        for a in tax["areas"]]}


def _json(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"), sort_keys=False)


ARQUIVOS_APP = ["index.html", "estilo.css", "app.js", "recomendador.js", "armazenamento.js", "fundos.js",
                "sw.js", "manifest.json", "icones/icone.svg", "icones/icone-192.png", "icones/icone-512.png",
                "icones/icone-180.png", "icones/icone-maskable-512.png"]


def versao_app(pasta_app: Path) -> str:
    """Hash do código do app: muda quando qualquer arquivo do app muda (o SW renova o cache)."""
    h = hashlib.sha256()
    for nome in ARQUIVOS_APP:
        caminho = pasta_app / nome
        if caminho.exists():
            h.update(nome.encode())
            h.update(caminho.read_bytes())
    return h.hexdigest()[:12]


def construir(dados: Path, pasta_app: Path | None = None) -> dict[str, str]:
    """Devolve {nome_do_arquivo: conteúdo} sem gravar nada."""
    fatos = sorted(comum.todos_aprovados(dados), key=lambda f: f["id"])
    tax = comum.carregar_taxonomia(dados)
    if tax is None:
        raise ValueError("dados/taxonomia.json não existe")
    tipos = comum.carregar_json(dados / "tipos_espanto.json")
    tipos = {"tipos": [{"id": t["id"], "nome": t["nome"]} for t in tipos["tipos"]]}
    arquivos = {
        "fatos.json": _json({"fatos": [fato_para_app(f) for f in fatos]}),
        "taxonomia.json": _json(taxonomia_para_app(tax)),
        "tipos_espanto.json": _json(tipos),
    }
    h = hashlib.sha256()
    for nome in sorted(arquivos):
        h.update(nome.encode())
        h.update(arquivos[nome].encode("utf-8"))
    versao = h.hexdigest()[:12]
    arquivos["versao.js"] = (
        "// Gerado por pipeline/construir_dados_app.py. Não edite à mão.\n"
        f'self.VERSAO_DADOS = "{versao}";\n'
        + (f'self.VERSAO_APP = "{versao_app(pasta_app)}";\n' if pasta_app else "")
        +
        f"self.TOTAL_FATOS = {len(fatos)};\n"
    )
    return arquivos


def main(argv: list[str] | None = None) -> int:
    comum.configurar_saida()
    p = argparse.ArgumentParser(description="Gera app/data/*.json a partir de dados/.")
    p.add_argument("--dados", type=Path, default=comum.DADOS_PADRAO)
    p.add_argument("--saida", type=Path, default=APP_DATA_PADRAO)
    p.add_argument("--sem-validar", action="store_true", help="pula o validar.py (não recomendado)")
    args = p.parse_args(argv)

    if not args.sem_validar:
        codigo = validar.main(["--dados", str(args.dados), "--silencioso"])
        if codigo != 0:
            print("validar.py encontrou erros; nada foi gerado.", file=sys.stderr)
            return 1

    try:
        arquivos = construir(args.dados, args.saida.parent)
    except (OSError, KeyError, ValueError) as e:
        print(f"Erro ao ler dados/: {e}", file=sys.stderr)
        return 1

    args.saida.mkdir(parents=True, exist_ok=True)
    for nome, conteudo in arquivos.items():
        (args.saida / nome).write_text(conteudo, encoding="utf-8", newline="\n")
    n = json.loads(arquivos["fatos.json"])["fatos"]
    temas = len({f["tema"] for f in n})
    print(f"{len(n)} fato(s) de {temas} tema(s) → {args.saida}")
    print(arquivos["versao.js"].splitlines()[1])
    return 0


if __name__ == "__main__":
    sys.exit(main())
