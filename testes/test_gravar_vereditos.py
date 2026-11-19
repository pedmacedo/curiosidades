import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pipeline"))

import gravar_vereditos  # noqa: E402


def entrada(obj):
    """Simula a entrada padrão com bytes UTF-8 (como chega de um heredoc no Windows)."""
    bruto = io.BytesIO(json.dumps(obj, ensure_ascii=False).encode("utf-8"))
    return mock.patch.object(sys, "stdin", io.TextIOWrapper(bruto, encoding="utf-8"))


class TestGravarVereditos(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.lote = Path(self.tmp.name) / "2026-11-18-x-01.jsonl"
        self.lote.write_text('{"id": "x-0001"}\n{"id": "x-0002"}\n', encoding="utf-8")
        self.arq = Path(self.tmp.name) / "2026-11-18-x-01.vereditos.json"

    def tearDown(self):
        self.tmp.cleanup()

    def test_acumula_e_substitui_por_id(self):
        with entrada([{"id": "x-0001", "veredito": "ajustar", "motivo": "números", "nota_surpresa": 4}]):
            self.assertEqual(gravar_vereditos.main([str(self.lote), "--rodada", "1"]), 0)
        with entrada([{"id": "x-0002", "veredito": "aprovado", "motivo": "ok — confere", "nota_surpresa": 3},
                      {"id": "x-0001", "veredito": "reprovado", "motivo": "mito", "nota_surpresa": 2}]):
            self.assertEqual(gravar_vereditos.main([str(self.lote), "--rodada", "1"]), 0)
        dados = json.loads(self.arq.read_text(encoding="utf-8"))
        r1 = {v["id"]: v for v in dados["rodadas"]["1"]}
        self.assertEqual(r1["x-0001"]["veredito"], "reprovado")
        self.assertEqual(r1["x-0002"]["motivo"], "ok — confere")

    def test_id_desconhecido_nao_grava(self):
        with entrada([{"id": "y-0001", "veredito": "aprovado"}]):
            self.assertEqual(gravar_vereditos.main([str(self.lote), "--rodada", "1"]), 1)
        self.assertFalse(self.arq.exists())


if __name__ == "__main__":
    unittest.main()
