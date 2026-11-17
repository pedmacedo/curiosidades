"""Testes do construir_dados_app.py: campos enxutos, versão estável e recusa com dados inválidos."""

from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from auxiliar import fato, gravar, montar_dados
import construir_dados_app as cda


def rodar(*args) -> int:
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        return cda.main([str(a) for a in args])


class TestConstruir(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.dados = montar_dados(Path(self.tmp.name))
        self.saida = Path(self.tmp.name) / "app_data"
        gravar(self.dados / "fatos" / "biologia.jsonl", [fato()])

    def tearDown(self):
        self.tmp.cleanup()

    def test_gera_arquivos_com_campos_do_app(self):
        self.assertEqual(rodar("--dados", self.dados, "--saida", self.saida), 0)
        fatos = json.loads((self.saida / "fatos.json").read_text(encoding="utf-8"))["fatos"]
        self.assertEqual(len(fatos), 1)
        f = fatos[0]
        self.assertEqual(f["id"], "microbiologia-0001")
        self.assertNotIn("lote", f)
        self.assertNotIn("trecho", f["fontes"][0])
        self.assertEqual(f["fontes"][0]["titulo"], "Deep biosphere")
        tax = json.loads((self.saida / "taxonomia.json").read_text(encoding="utf-8"))
        self.assertNotIn("descricao", tax["areas"][0]["temas"][0])
        self.assertIn("vizinhos", tax["areas"][0]["temas"][0])
        tipos = json.loads((self.saida / "tipos_espanto.json").read_text(encoding="utf-8"))
        self.assertTrue(all("nome" in t for t in tipos["tipos"]))
        self.assertIn("self.VERSAO_DADOS", (self.saida / "versao.js").read_text(encoding="utf-8"))

    def test_versao_muda_so_quando_os_dados_mudam(self):
        v1 = cda.construir(self.dados)["versao.js"]
        self.assertEqual(v1, cda.construir(self.dados)["versao.js"])
        gravar(self.dados / "fatos" / "biologia.jsonl", [fato(gancho="Outro gancho bem diferente do primeiro.")])
        self.assertNotEqual(v1, cda.construir(self.dados)["versao.js"])

    def test_versao_do_app_acompanha_o_codigo(self):
        app = Path(self.tmp.name) / "app"
        app.mkdir()
        (app / "app.js").write_text("// v1", encoding="utf-8")
        v1 = cda.construir(self.dados, app)["versao.js"]
        self.assertIn("self.VERSAO_APP", v1)
        (app / "app.js").write_text("// v2", encoding="utf-8")
        self.assertNotEqual(v1, cda.construir(self.dados, app)["versao.js"])

    def test_recusa_dados_invalidos(self):
        gravar(self.dados / "fatos" / "biologia.jsonl", [fato(nota_surpresa=9)])
        self.assertEqual(rodar("--dados", self.dados, "--saida", self.saida), 1)
        self.assertFalse((self.saida / "fatos.json").exists())


if __name__ == "__main__":
    unittest.main()
