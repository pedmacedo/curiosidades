"""Testes do montar_lote.py: numeração de ids e gravação do lote (offline)."""

from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from auxiliar import FATO, fato, gravar, montar_dados
import checar_citacoes as cc
import montar_lote as ml

MODULO = '''
LOTE = "2026-11-18-microbiologia-02"
AREA = "biologia"
TEMA = "microbiologia"
CANDIDATOS = [
    {"tipos_espanto": ["contraintuitivo"], "gancho": "Gancho A", "explicacao": "palavra " * 100,
     "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
     "fontes": [{"url": "https://exemplo.org/a", "titulo": "A", "idioma": "en", "trecho": "The deep biosphere is the part of the biosphere"}]},
    {"tipos_espanto": ["contraintuitivo"], "gancho": "Gancho B", "explicacao": "curta",
     "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
     "fontes": [{"url": "https://exemplo.org/a", "titulo": "A", "idioma": "en", "trecho": "nothing like this exists in the page"}]},
]
'''


class TestMontarLote(unittest.TestCase):
    def test_numera_a_partir_dos_ids_existentes_e_grava(self):
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            dados = montar_dados(Path(tmp))
            gravar(dados / "fatos" / "biologia.jsonl", [fato(id="microbiologia-0007")])
            gravar(dados / "descartados" / "biologia.jsonl", [fato(id="microbiologia-0012", gancho="x", motivo_descarte="mito")])
            # texto da fonte já no cache
            b = cc.Baixador(dados / "cache_fontes")
            caminho = b.caminho_cache("https://exemplo.org/a", "pagina")
            caminho.parent.mkdir(parents=True, exist_ok=True)
            caminho.write_text(FATO["fontes"][0]["trecho"], encoding="utf-8")
            cand = Path(tmp) / "cand.py"
            cand.write_text(MODULO, encoding="utf-8")

            with contextlib.redirect_stdout(io.StringIO()) as saida:
                codigo = ml.main([str(cand), "--dados", str(dados), "--data", "2026-11-18"])
            self.assertEqual(codigo, 0)
            texto = saida.getvalue()
            self.assertIn("microbiologia-0013: ok", texto)
            self.assertIn("microbiologia-0014: falhou", texto)
            self.assertIn("explicação com 1 palavras", texto)

            lote = dados / "lotes" / "2026-11-18-microbiologia-02.jsonl"
            fatos = [json.loads(l) for l in lote.read_text(encoding="utf-8").splitlines()]
            self.assertEqual([f["id"] for f in fatos], ["microbiologia-0013", "microbiologia-0014"])
            self.assertEqual(fatos[0]["lote"], "2026-11-18-microbiologia-02")
            self.assertEqual(fatos[0]["fontes"][0]["acessado_em"], "2026-11-18")

            # regravar o mesmo lote mantém os ids dele
            with contextlib.redirect_stdout(io.StringIO()):
                ml.main([str(cand), "--dados", str(dados)])
            fatos = [json.loads(l) for l in lote.read_text(encoding="utf-8").splitlines()]
            self.assertEqual(fatos[0]["id"], "microbiologia-0013")


if __name__ == "__main__":
    unittest.main()
