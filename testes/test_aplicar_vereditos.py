"""Testes do aplicar_vereditos.py."""

from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from auxiliar import fato, gravar, montar_dados
import aplicar_vereditos as av
import comum


def rodar(*args) -> tuple[int, str]:
    with contextlib.redirect_stdout(io.StringIO()) as saida, contextlib.redirect_stderr(io.StringIO()):
        codigo = av.main([str(a) for a in args])
    return codigo, saida.getvalue()


class TestAplicar(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.dados = montar_dados(Path(self.tmp.name))
        candidatos = [fato(id=f"microbiologia-{i:04d}", gancho=f"Gancho {i}", verificado_em=None, nota_surpresa=4)
                      for i in range(1, 6)]
        self.lote = gravar(self.dados / "lotes" / "l1.jsonl", candidatos)

    def tearDown(self):
        self.tmp.cleanup()

    def vereditos(self, rodadas):
        (self.dados / "lotes" / "l1.vereditos.json").write_text(
            json.dumps({"lote": "l1", "rodadas": rodadas}), encoding="utf-8")

    def checagem(self, falhou):
        (self.dados / "lotes" / "l1.checagem.json").write_text(
            json.dumps({"fatos": [{"id": i, "status": "falhou"} for i in falhou]}), encoding="utf-8")

    def test_fluxo_completo(self):
        self.checagem(["microbiologia-0005"])
        self.vereditos({
            "1": [{"id": "microbiologia-0001", "veredito": "aprovado", "nota_surpresa": 5},
                  {"id": "microbiologia-0002", "veredito": "ajustar", "nota_surpresa": 4},
                  {"id": "microbiologia-0003", "veredito": "reprovado", "motivo": "mito: é lenda", "nota_surpresa": 3},
                  {"id": "microbiologia-0004", "veredito": "aprovado", "nota_surpresa": 2}],
            "2": [{"id": "microbiologia-0002", "veredito": "aprovado", "nota_surpresa": 3}],
        })
        codigo, saida = rodar(self.lote, "--dados", self.dados, "--data", "2026-11-17")
        self.assertEqual(codigo, 0, saida)
        aprovados = comum.carregar_fatos(self.dados / "fatos" / "biologia.jsonl")
        descartados = {f["id"]: f["motivo_descarte"] for f in comum.carregar_fatos(self.dados / "descartados" / "biologia.jsonl")}
        self.assertEqual([f["id"] for f in aprovados], ["microbiologia-0001", "microbiologia-0002"])
        self.assertEqual(aprovados[0]["nota_surpresa"], 5)
        self.assertEqual(aprovados[0]["verificado_em"], "2026-11-17")
        self.assertEqual(descartados, {"microbiologia-0003": "mito", "microbiologia-0004": "pouco_interessante",
                                       "microbiologia-0005": "citacao_nao_encontrada"})
        # rodar de novo não duplica
        codigo, saida = rodar(self.lote, "--dados", self.dados, "--data", "2026-11-17")
        self.assertIn("Pulados", saida)
        self.assertEqual(len(comum.carregar_fatos(self.dados / "fatos" / "biologia.jsonl")), 2)

    def test_pendencia_interrompe(self):
        self.vereditos({"1": [{"id": "microbiologia-0001", "veredito": "ajustar"}]})
        codigo, saida = rodar(self.lote, "--dados", self.dados)
        self.assertEqual(codigo, 1)
        self.assertIn("Pendências", saida)
        self.assertFalse((self.dados / "fatos" / "biologia.jsonl").exists())

    def test_descartar_pendentes_e_simular(self):
        self.vereditos({"1": [{"id": "microbiologia-0001", "veredito": "ajustar"}]})
        codigo, saida = rodar(self.lote, "--dados", self.dados, "--descartar-pendentes", "--simular")
        self.assertEqual(codigo, 0)
        self.assertIn("5 descartado", saida)
        self.assertFalse((self.dados / "descartados" / "biologia.jsonl").exists())

    def test_motivo_desconhecido(self):
        self.assertEqual(av.rotulo_motivo("sei lá: algo"), "reprovado_verificador")
        self.assertEqual(av.rotulo_motivo("numero_divergente: 28 °C"), "numero_divergente")


if __name__ == "__main__":
    unittest.main()
