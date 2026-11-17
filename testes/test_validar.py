"""Testes do validar.py: taxonomia, esquema dos fatos, ids e duplicatas."""

from __future__ import annotations

import contextlib
import copy
import io
import tempfile
import unittest
from pathlib import Path

import auxiliar
from auxiliar import fato, gravar, montar_dados
import validar


def rodar(*args) -> tuple[int, str]:
    with contextlib.redirect_stdout(io.StringIO()) as saida:
        codigo = validar.main([str(a) for a in args])
    return codigo, saida.getvalue()


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.dados = montar_dados(Path(self.tmp.name))

    def tearDown(self):
        self.tmp.cleanup()

    def aprovados(self, *fatos, area="biologia"):
        return gravar(self.dados / "fatos" / f"{area}.jsonl", list(fatos))

    def erros_de(self, f, modo="aprovado"):
        rel = validar.Relatorio()
        ctx = {"indice": validar.comum.indice_temas(auxiliar.TAXONOMIA),
               "tipos": set(validar.comum.TIPOS_ESPANTO_PADRAO)}
        validar.validar_fato(f, "x", modo, ctx, rel)
        return rel.erros, rel.avisos


class TestFatos(Base):
    def test_fato_valido_passa(self):
        self.aprovados(fato())
        codigo, saida = rodar("--dados", self.dados)
        self.assertEqual(codigo, 0, saida)
        self.assertIn("Resultado: OK", saida)

    def test_sem_fatos_passa(self):
        self.assertEqual(rodar("--dados", self.dados)[0], 0)

    def test_limites(self):
        casos = {
            "gancho": fato(gancho="x" * 221),
            "explicação curta": fato(explicacao="curta demais"),
            "nivel": fato(nivel=4),
            "nota baixa em aprovado": fato(nota_surpresa=2),
            "nota fora": fato(nota_surpresa=6),
            "tipos demais": fato(tipos_espanto=["escala_absurda", "contraintuitivo", "engenhosidade", "mito_desmentido"]),
            "tipo desconhecido": fato(tipos_espanto=["fofo"]),
            "confianca": fato(confianca="certeza"),
            "hipotese sem mistério": fato(confianca="hipotese"),
            "sem fontes": fato(fontes=[]),
            "id fora do formato": fato(id="micro-1"),
            "tema inexistente": fato(tema="dinossauros", id="dinossauros-0001"),
            "tema de outra área": fato(area="terra"),
            "secundário inexistente": fato(temas_secundarios=["xyz"]),
            "secundário = principal": fato(temas_secundarios=["microbiologia"]),
            "sem verificado_em": fato(verificado_em=None),
            "motivo em aprovado": fato(motivo_descarte="mito"),
            "nivel booleano": fato(nivel=True),
        }
        for nome, f in casos.items():
            with self.subTest(nome):
                erros, _ = self.erros_de(f)
                self.assertTrue(erros, f"esperava erro em: {nome}")

    def test_fonte_invalida(self):
        f = fato()
        f["fontes"][0].update(url="ftp:/x", idioma="inglês", acessado_em="17/11/2026", trecho="")
        erros, _ = self.erros_de(f)
        texto = " ".join(erros)
        for pedaço in ("url inválida", "'idioma' inválido", "falta 'trecho'", "acessado_em"):
            self.assertIn(pedaço, texto)

    def test_aprofundar(self):
        ok = fato(aprofundar=[{"tipo": "livro", "titulo": "Um livro"},
                              {"tipo": "video", "titulo": "Vídeo", "url": "https://exemplo.org/v"}])
        self.assertEqual(self.erros_de(ok)[0], [])
        ruim = fato(aprofundar=[{"tipo": "tiktok", "titulo": "x", "url": "https://x.org"},
                                {"tipo": "video", "titulo": "sem url"}])
        self.assertEqual(len(self.erros_de(ruim)[0]), 2)

    def test_hipotese_valida(self):
        f = fato(confianca="hipotese", tipos_espanto=["misterio_aberto"],
                 gancho="Talvez a vida tenha começado nas fontes hidrotermais do fundo do mar.")
        erros, avisos = self.erros_de(f)
        self.assertEqual(erros, [])
        self.assertEqual(avisos, [])

    def test_candidato_e_mais_tolerante(self):
        f = fato(nota_surpresa=2, verificado_em=None, explicacao="curta")
        erros, avisos = self.erros_de(f, modo="candidato")
        self.assertEqual(erros, [])
        self.assertTrue(any("palavras" in a for a in avisos))

    def test_descartado_precisa_de_motivo(self):
        gravar(self.dados / "descartados" / "biologia.jsonl", [fato(nota_surpresa=1)])
        codigo, saida = rodar("--dados", self.dados)
        self.assertEqual(codigo, 1)
        self.assertIn("motivo_descarte", saida)
        gravar(self.dados / "descartados" / "biologia.jsonl", [fato(nota_surpresa=1, motivo_descarte="pouco_interessante")])
        self.assertEqual(rodar("--dados", self.dados)[0], 0)

    def test_area_do_arquivo(self):
        self.aprovados(fato(), area="terra")
        codigo, saida = rodar("--dados", self.dados)
        self.assertEqual(codigo, 1)
        self.assertIn("gravado em terra.jsonl", saida)

    def test_json_invalido(self):
        arq = self.dados / "fatos" / "biologia.jsonl"
        arq.write_text('{"id": "x"\n', encoding="utf-8")
        codigo, saida = rodar("--dados", self.dados)
        self.assertEqual(codigo, 1)
        self.assertIn("JSON inválido", saida)


class TestIdsEDuplicatas(Base):
    def test_id_repetido(self):
        outro = fato(gancho="Um gancho completamente diferente sobre arqueias que comem ferro no subsolo.")
        self.aprovados(fato(), outro)
        codigo, saida = rodar("--dados", self.dados)
        self.assertEqual(codigo, 1)
        self.assertIn("repetido", saida)

    def test_gancho_identico_e_parecido(self):
        igual = fato(id="microbiologia-0002", gancho=fato()["gancho"].upper())
        self.aprovados(fato(), igual)
        codigo, saida = rodar("--dados", self.dados)
        self.assertEqual(codigo, 1)
        self.assertIn("gancho idêntico", saida)

        parecido = fato(id="microbiologia-0002",
                        gancho="Há microrganismos vivendo em rochas a vários quilômetros de profundidade, com metabolismo lentíssimo.")
        self.aprovados(fato(), parecido)
        codigo, saida = rodar("--dados", self.dados)
        self.assertEqual(codigo, 0)
        self.assertIn("muito parecido", saida)
        self.assertEqual(rodar("--dados", self.dados, "--estrito")[0], 1)

    def test_lote_comparado_com_aprovados(self):
        self.aprovados(fato())
        lote = gravar(self.dados / "lotes" / "l1.jsonl",
                      [fato(nota_surpresa=2, verificado_em=None)])  # mesmo id e mesmo gancho
        codigo, saida = rodar(lote, "--dados", self.dados)
        self.assertEqual(codigo, 1)
        self.assertIn("repetido", saida)
        self.assertIn("gancho idêntico", saida)


class TestTaxonomia(Base):
    def validar_tax(self, tax):
        rel = validar.Relatorio()
        validar.validar_taxonomia(tax, rel)
        return rel.erros

    def test_taxonomia_valida(self):
        self.assertEqual(self.validar_tax(auxiliar.TAXONOMIA), [])

    def test_problemas_de_taxonomia(self):
        tax = copy.deepcopy(auxiliar.TAXONOMIA)
        temas = tax["areas"][0]["temas"]
        temas.append({"id": "Micro-Bio", "nome": "x", "descricao": "x", "vizinhos": []})
        temas.append({"id": "virus", "nome": "Vírus", "descricao": "x",
                      "vizinhos": ["microbiologia", "inexistente", "virus"]})
        temas.append({"id": "geologia_profunda", "nome": "Dup", "descricao": "x",
                      "vizinhos": ["astrobiologia", "virus"]})
        texto = " | ".join(self.validar_tax(tax))
        self.assertIn("id de tema inválido", texto)
        self.assertIn("mesma área", texto)
        self.assertIn("inexistente", texto)
        self.assertIn("si mesmo", texto)
        self.assertIn("repetido no projeto", texto)

    def test_poucos_vizinhos(self):
        tax = copy.deepcopy(auxiliar.TAXONOMIA)
        tax["areas"][0]["temas"][0]["vizinhos"] = ["astrobiologia"]
        self.assertTrue(any("2 a 5" in e for e in self.validar_tax(tax)))

    def test_sem_taxonomia_avisa_e_segue(self):
        dados = montar_dados(Path(self.tmp.name) / "outro", taxonomia=None)
        gravar(dados / "fatos" / "biologia.jsonl", [fato()])
        codigo, saida = rodar("--dados", dados)
        self.assertEqual(codigo, 0)
        self.assertIn("checagens de área/tema puladas", saida)


if __name__ == "__main__":
    unittest.main()
