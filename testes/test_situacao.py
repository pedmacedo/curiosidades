import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pipeline"))

import situacao  # noqa: E402


class TestSituacao(unittest.TestCase):
    def test_fila_em_rodizio(self):
        tax = {"areas": [
            {"id": "a", "temas": [{"id": "a1"}, {"id": "a2"}, {"id": "a3"}]},
            {"id": "b", "temas": [{"id": "b1"}]},
        ]}
        self.assertEqual(situacao.fila_de_temas(tax),
                         [("a", "a1"), ("b", "b1"), ("a", "a2"), ("a", "a3")])

    def test_nomes_de_lote(self):
        self.assertEqual(situacao.nome_base_lote(Path("2026-11-17-amazonia-01-r2.py")), "2026-11-17-amazonia-01")
        self.assertEqual(situacao.tema_do_lote("2026-11-17-palavras_viajantes-01"), "palavras_viajantes")

    def test_etapas(self):
        with tempfile.TemporaryDirectory() as tmp:
            dados = Path(tmp)
            (dados / "candidatos").mkdir()
            (dados / "lotes").mkdir()
            lote = "2026-11-18-anatomia-01"
            (dados / "candidatos" / f"{lote}.py").write_text("", encoding="utf-8")
            self.assertEqual(situacao.etapa_do_lote(dados, lote, set())[0], "candidatos escritos")
            (dados / "lotes" / f"{lote}.jsonl").write_text("", encoding="utf-8")
            self.assertEqual(situacao.etapa_do_lote(dados, lote, set())[0], "montado")
            (dados / "lotes" / f"{lote}.checagem.json").write_text("{}", encoding="utf-8")
            self.assertEqual(situacao.etapa_do_lote(dados, lote, set())[0], "citações checadas")
            (dados / "lotes" / f"{lote}.vereditos.json").write_text(
                '{"rodadas": {"1": [{"id": "x", "veredito": "ajustar"}]}}', encoding="utf-8")
            self.assertIn("para ajustar", situacao.etapa_do_lote(dados, lote, set())[0])
            self.assertEqual(situacao.etapa_do_lote(dados, lote, {lote})[0], "aplicado")


if __name__ == "__main__":
    unittest.main()
