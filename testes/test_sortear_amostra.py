"""Testes do sortear_amostra.py: sorteio determinístico, exclusão de revisados e apuração."""

from __future__ import annotations

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from auxiliar import fato, gravar, montar_dados
import sortear_amostra as sa


def rodar(*args) -> tuple[int, str]:
    with contextlib.redirect_stdout(io.StringIO()) as saida, contextlib.redirect_stderr(io.StringIO()):
        codigo = sa.main([str(a) for a in args])
    return codigo, saida.getvalue()


class TestSorteio(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.dados = montar_dados(Path(self.tmp.name))
        fatos = [fato(id=f"microbiologia-{i:04d}", gancho=f"Gancho número {i}",
                      lote="lote-a" if i <= 5 else "lote-b") for i in range(1, 11)]
        gravar(self.dados / "fatos" / "biologia.jsonl", fatos)

    def tearDown(self):
        self.tmp.cleanup()

    def ids(self, nome):
        return sa.RE_ID.findall((self.dados / "revisao" / f"{nome}.md").read_text(encoding="utf-8"))

    def test_semente_reprodutivel(self):
        rodar("--n", 4, "--semente", 7, "--nome", "a", "--dados", self.dados, "--incluir-revisados")
        rodar("--n", 4, "--semente", 7, "--nome", "b", "--dados", self.dados, "--incluir-revisados")
        self.assertEqual(self.ids("a"), self.ids("b"))
        self.assertEqual(len(self.ids("a")), 4)

    def test_nao_repete_revisados(self):
        rodar("--n", 6, "--semente", 1, "--nome", "r1", "--dados", self.dados)
        codigo, saida = rodar("--n", 6, "--semente", 1, "--nome", "r2", "--dados", self.dados)
        self.assertEqual(codigo, 0)
        self.assertIn("só há 4", saida)
        self.assertFalse(set(self.ids("r1")) & set(self.ids("r2")))
        self.assertEqual(rodar("--n", 1, "--nome", "r3", "--dados", self.dados)[0], 1)  # nada elegível

    def test_todos_de_um_lote(self):
        rodar("--todos", "--lotes", "lote-a", "--nome", "piloto", "--dados", self.dados)
        self.assertEqual(sorted(self.ids("piloto")), [f"microbiologia-{i:04d}" for i in range(1, 6)])

    def test_markdown_tem_conteudo_e_caixas(self):
        rodar("--n", 2, "--semente", 3, "--nome", "m", "--dados", self.dados)
        md = (self.dados / "revisao" / "m.md").read_text(encoding="utf-8")
        self.assertEqual(md.count("[ ] ok   [ ] errado   [ ] chato"), 2)
        self.assertIn("> The deep biosphere", md)
        self.assertIn("Gancho número", md)


class TestApuracao(unittest.TestCase):
    MD = """
<!-- id: a-0001 -->
**Avaliação:** [x] ok   [ ] errado   [ ] chato
<!-- id: a-0002 -->
**Avaliação:** [ ] ok   [X] errado   [ ] chato
<!-- id: a-0003 -->
**Avaliação:** [ ] ok   [ ] errado   [ ] chato
<!-- id: a-0004 -->
**Avaliação:** [x] ok   [ ] errado   [x] chato
"""

    def test_apurar(self):
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            arq = Path(tmp) / "r.md"
            arq.write_text(self.MD, encoding="utf-8")
            r = sa.apurar(arq)
            self.assertEqual(r["ok"], ["a-0001"])
            self.assertEqual(r["errado"], ["a-0002"])
            self.assertEqual(r["pendente"], ["a-0003"])
            self.assertEqual(r["ambiguo"], ["a-0004"])
            codigo, saida = rodar("--apurar", arq)
            self.assertEqual(codigo, 0)
            self.assertIn("incompleta", saida)

    def test_veredito_pausar(self):
        md = "".join(f"<!-- id: b-{i} -->\n[ ] ok [x] {'chato' if i % 2 else 'errado'}\n" for i in range(3))
        md += "<!-- id: b-9 -->\n[x] ok [ ] errado\n"
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            arq = Path(tmp) / "r.md"
            arq.write_text(md, encoding="utf-8")
            self.assertIn("PAUSAR", rodar("--apurar", arq)[1])

    def test_descartar_marcados(self):
        import json
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            dados = montar_dados(Path(tmp))
            gravar(dados / "fatos" / "biologia.jsonl",
                   [fato(id="microbiologia-0001", gancho="G1"), fato(id="microbiologia-0002", gancho="G2")])
            arq = dados / "revisao" / "r.md"
            arq.parent.mkdir(parents=True, exist_ok=True)
            arq.write_text("<!-- id: microbiologia-0001 -->\n[x] ok [ ] errado [ ] chato\n**Comentário:** \n"
                           "<!-- id: microbiologia-0002 -->\n[ ] ok [ ] errado [x] chato\n"
                           "**Comentário:** nunca ouvi falar\n", encoding="utf-8")
            codigo, saida = rodar("--apurar", arq, "--dados", dados, "--descartar")
            self.assertEqual(codigo, 0)
            self.assertIn("microbiologia-0002: chato", saida)
            ficaram = (dados / "fatos" / "biologia.jsonl").read_text(encoding="utf-8").splitlines()
            self.assertEqual([json.loads(l)["id"] for l in ficaram], ["microbiologia-0001"])
            desc = [json.loads(l) for l in (dados / "descartados" / "biologia.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(desc[0]["motivo_descarte"], "pouco_interessante")
            self.assertEqual(desc[0]["revisao_humana"]["comentario"], "nunca ouvi falar")
            # rodar de novo não duplica
            self.assertIn("já descartado", rodar("--apurar", arq, "--dados", dados, "--descartar")[1])
            self.assertEqual(len((dados / "descartados" / "biologia.jsonl").read_text(encoding="utf-8").splitlines()), 1)


if __name__ == "__main__":
    unittest.main()
