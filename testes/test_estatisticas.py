"""Testes do estatisticas.py."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from auxiliar import fato, gravar, montar_dados
import estatisticas as est


class TestEstatisticas(unittest.TestCase):
    def test_resumo_e_cobertura(self):
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            dados = montar_dados(Path(tmp))
            gravar(dados / "fatos" / "biologia.jsonl",
                   [fato(id="microbiologia-0001", nota_surpresa=4), fato(id="microbiologia-0002", gancho="Outro", nota_surpresa=5)])
            gravar(dados / "descartados" / "biologia.jsonl",
                   [fato(id="microbiologia-0003", gancho="X", motivo_descarte="mito"),
                    fato(id="microbiologia-0004", gancho="Y", motivo_descarte="pouco_interessante")])
            (dados / "lotes" / "2026-11-17-biologia-01.vereditos.json").write_text(json.dumps({"rodadas": {"1": [
                {"id": "a", "veredito": "aprovado"}, {"id": "b", "veredito": "ajustar"}, {"id": "c", "veredito": "reprovado"}]}}),
                encoding="utf-8")
            [l] = est.resumo_lotes(dados)
            self.assertEqual((l["candidatos"], l["aprovados"], l["descartados"]), (4, 2, 2))
            self.assertAlmostEqual(l["taxa_descarte"], 0.5)
            self.assertAlmostEqual(l["nota_media"], 4.5)
            self.assertEqual(l["rodada1"]["ajustar"], 1)
            self.assertEqual(l["motivos"]["mito"], 1)
            _, cobertos, total = est.cobertura(dados)
            self.assertEqual((cobertos, total), (1, 3))


if __name__ == "__main__":
    unittest.main()
