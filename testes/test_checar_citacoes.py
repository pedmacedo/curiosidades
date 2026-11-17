"""Testes do checar_citacoes.py: trecho presente, ausente e aproximado, números e download."""

from __future__ import annotations

import contextlib
import http.server
import io
import json
import tempfile
import threading
import unittest
from pathlib import Path

import auxiliar  # noqa: F401  (ajusta o sys.path)
import checar_citacoes as cc

FONTE = (
    "The deep biosphere is the part of the biosphere that resides below the first few meters "
    "of the surface.[3] It extends down at least 5 kilometers below the continental surface and "
    "10.5 kilometers below the sea surface, with temperatures that may reach beyond 120 °C. "
    "Some microbes there may divide only once every several hundred years, a pace that is “extra-"
    "ordinarily” slow compared with surface life. An estimated 70% of the bacteria and archaea "
    "on Earth live in the subsurface, perhaps 2 to 6 × 10^29 cells."
)


class TestNormalizacao(unittest.TestCase):
    def test_aspas_tracos_espacos_e_caixa(self):
        self.assertEqual(cc.normalizar("“Olá”  —  ‘MUNDO’ !"), "\"olá\" - 'mundo'!")

    def test_hifenizacao_de_quebra_de_linha(self):
        self.assertEqual(cc.normalizar("extra-\n ordinariamente"), cc.normalizar("extraordinariamente"))

    def test_notas_de_rodape_removidas(self):
        self.assertEqual(cc.normalizar("surface.[3] It"), "surface. it")
        self.assertEqual(cc.normalizar("fato[citation needed] aqui"), "fato aqui")

    def test_espaco_antes_de_pontuacao(self):
        self.assertEqual(cc.normalizar("Foo , bar ( baz ) ."), "foo, bar (baz).")

    def test_fragmentos_com_elisao(self):
        self.assertEqual(cc.fragmentos("Primeira parte [...] segunda … terceira"),
                         ["primeira parte", "segunda", "terceira"])


class TestConferirTrecho(unittest.TestCase):
    def test_presente_exato(self):
        r = cc.conferir_trecho("It extends down at least 5 kilometers below the continental surface", FONTE)
        self.assertEqual(r.status, "ok")

    def test_presente_com_diferencas_de_tipografia(self):
        # aspas retas, "extraordinarily" sem hifenização, caixa diferente e sem a nota [3]
        r = cc.conferir_trecho('a pace that is "extraordinarily" SLOW compared with surface life', FONTE)
        self.assertEqual(r.status, "ok")
        r = cc.conferir_trecho("first few meters of the surface. It extends down", FONTE)
        self.assertEqual(r.status, "ok")

    def test_presente_com_elisao_na_ordem(self):
        r = cc.conferir_trecho("The deep biosphere is the part [...] 10.5 kilometers below the sea surface", FONTE)
        self.assertEqual(r.status, "ok")
        self.assertEqual(r.nota, "com elisões")

    def test_elisao_fora_de_ordem_vale_com_nota(self):
        r = cc.conferir_trecho("10.5 kilometers below the sea surface ... The deep biosphere is the part", FONTE)
        self.assertEqual(r.status, "ok")
        self.assertIn("fora da ordem", r.nota)

    def test_elisao_com_pedaco_inexistente_falha(self):
        r = cc.conferir_trecho("The deep biosphere is the part ... microbes glow in the dark", FONTE)
        self.assertEqual(r.status, "ausente")

    def test_ausente(self):
        r = cc.conferir_trecho("Deep microbes are known to glow in the dark when exposed to magma.", FONTE)
        self.assertEqual(r.status, "ausente")

    def test_curto_nao_aceita_aproximacao(self):
        r = cc.conferir_trecho("at least 6 kilometers", FONTE)
        self.assertEqual(r.status, "ausente")

    def test_aproximado_com_pequenas_diferencas(self):
        # duas palavras trocadas num trecho longo → aproximado (≥ 0,9)
        trecho = ("It extends down at least 5 kilometres below the continental surface and "
                  "10.5 kilometres below the sea surface, with temperatures that may reach beyond 120 °C.")
        r = cc.conferir_trecho(trecho, FONTE)
        self.assertEqual(r.status, "aproximado")
        self.assertGreaterEqual(r.similaridade, 0.9)
        self.assertIn("kilometers below the continental surface", r.trecho_na_fonte)

    def test_parecido_demais_mas_abaixo_do_limiar_falha(self):
        trecho = ("It reaches at most 2 miles under the continental crust and also "
                  "ten miles under the oceans, where heat can pass far beyond boiling.")
        r = cc.conferir_trecho(trecho, FONTE)
        self.assertEqual(r.status, "ausente")

    def test_trecho_com_numero_alterado_nao_e_exato(self):
        r = cc.conferir_trecho("An estimated 80% of the bacteria and archaea on Earth live in the subsurface", FONTE)
        self.assertNotEqual(r.status, "ok")


class TestNumeros(unittest.TestCase):
    def valores(self, texto, conv=("pt",)):
        return [(t, sorted(v)) for t, v in cc.extrair_numeros(texto, conv)]

    def test_formatos_pt(self):
        self.assertEqual(self.valores("1.500 fatos e 1,5 metro em 1905"),
                         [("1.500", [1500.0]), ("1,5", [1.5]), ("1905", [1905.0])])

    def test_formatos_ambiguos_na_fonte(self):
        self.assertEqual(self.valores("1,500 cells", ("pt", "en")), [("1,500", [1.5, 1500.0])])

    def test_multiplicador(self):
        self.assertIn(3e6, dict(cc.extrair_numeros("3 milhões de anos"))["3"])
        self.assertIn(3e6, dict(cc.extrair_numeros("3 million years", ("en",)))["3"])

    def test_ignora_numero_colado_em_letra(self):
        self.assertEqual(self.valores("o CO2 e o H2O"), [])

    def test_sem_suporte(self):
        trechos = ["It extends down at least 5 kilometers and 10.5 kilometers below the sea, 70% of cells"]
        textos = ["Chega a 5 km sob os continentes e 10,5 km sob o mar.", "Cerca de 70% e 37 graus."]
        self.assertEqual(cc.numeros_sem_suporte(textos, trechos), ["37"])

    def test_milhar_entre_idiomas(self):
        self.assertEqual(cc.numeros_sem_suporte(["São 1.500 espécies"], ["about 1,500 species"]), [])
        self.assertEqual(cc.numeros_sem_suporte(["São 3 milhões"], ["about 3,000,000 people"]), [])


class TestWikipedia(unittest.TestCase):
    def test_reconhece_url(self):
        self.assertEqual(cc.info_wikipedia("https://en.wikipedia.org/wiki/Deep_biosphere"),
                         ("en", "Deep biosphere"))
        self.assertEqual(cc.info_wikipedia("https://pt.m.wikipedia.org/wiki/Biosfera_profunda#Hist%C3%B3ria"),
                         ("pt", "Biosfera profunda"))
        self.assertEqual(cc.info_wikipedia("https://pt.wikipedia.org/wiki/S%C3%A3o_Paulo"), ("pt", "São Paulo"))
        self.assertIsNone(cc.info_wikipedia("https://www.nasa.gov/x"))

    def test_url_da_api(self):
        url = cc.url_api_wikipedia("pt", "São Paulo")
        self.assertIn("pt.wikipedia.org/w/api.php", url)
        self.assertIn("explaintext=1", url)
        self.assertIn("S%C3%A3o%20Paulo", url)


class TestHtml(unittest.TestCase):
    def test_extrai_texto_sem_script_e_com_quebras_de_bloco(self):
        html = b"""<html><head><style>p{}</style><script>var x = 'lixo';</script></head>
        <body><h1>Titulo</h1><p>Primeiro <b>par</b>agrafo, com <a href='#'>link</a>.</p><p>Segundo.</p></body></html>"""
        texto = cc.html_para_texto(html)
        self.assertNotIn("lixo", texto)
        self.assertIn("Primeiro paragrafo, com link.", texto)
        self.assertEqual(cc.normalizar(texto), "titulo primeiro paragrafo, com link. segundo.")


# ------------------------------------------------------------------ servidor local para o download

class _Manipulador(http.server.BaseHTTPRequestHandler):
    PAGINAS = {
        "/artigo.html": (200, "text/html; charset=utf-8",
                         f"<html><body><article><p>{FONTE}</p></article></body></html>".encode("utf-8")),
        "/texto.txt": (200, "text/plain; charset=utf-8", "Linha única com ação.".encode("utf-8")),
        "/proibido": (403, "text/html", b"<html>Access denied</html>"),
        "/binario": (200, "application/octet-stream", b"\x00\x01"),
    }

    contagem_429 = 0

    def _responder_429(self):
        """Responde 429 só na primeira vez que /limitado é pedido."""
        type(self).contagem_429 += 1
        if type(self).contagem_429 == 1:
            self.send_response(429)
            self.send_header("Retry-After", "0")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return True
        return False

    def do_GET(self):
        if self.path == "/limitado" and self._responder_429():
            return
        if self.path == "/limitado":
            self.path = "/texto.txt"
        status, tipo, corpo = self.PAGINAS.get(self.path, (404, "text/plain", b"nao achei"))
        self.send_response(status)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def log_message(self, *args):
        pass


class TestDownloadECache(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.servidor = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _Manipulador)
        cls.base = f"http://127.0.0.1:{cls.servidor.server_address[1]}"
        threading.Thread(target=cls.servidor.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.servidor.shutdown()
        cls.servidor.server_close()

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.cache = Path(self.tmp.name) / "cache"
        self.baixador = cc.Baixador(self.cache, pausa=0)

    def tearDown(self):
        self.tmp.cleanup()

    def _fato(self, *fontes):
        return {"id": "t-0001", "gancho": "Vai a 5 km de profundidade.", "explicacao": "Cerca de 70%, e 99 outros.",
                "fontes": [{"url": u, "trecho": t} for u, t in fontes]}

    def test_fonte_ok_e_cache_gravado(self):
        res = cc.checar_fato(self._fato((f"{self.base}/artigo.html",
                                         "It extends down at least 5 kilometers below the continental surface")),
                             self.baixador)
        self.assertEqual(res["status"], "ok")
        self.assertEqual(res["aviso_numero"], ["70", "99"])  # 70 não está no trecho citado
        caminho = Path(res["fontes"][0]["cache"][0])
        self.assertTrue(caminho.exists())
        self.assertTrue(caminho.with_suffix(".json").exists())

        # offline, usando só o cache
        offline = cc.Baixador(self.cache, offline=True)
        res2 = cc.checar_fato(self._fato((f"{self.base}/artigo.html", "An estimated 70% of the bacteria")), offline)
        self.assertEqual(res2["status"], "ok")

    def test_offline_sem_cache_falha(self):
        offline = cc.Baixador(self.cache, offline=True)
        res = cc.checar_fato(self._fato((f"{self.base}/artigo.html", "The deep biosphere")), offline)
        self.assertEqual(res["status"], "falhou")
        self.assertIn("sem_cache", res["fontes"][0]["motivo"])

    def test_bloqueio_404_e_formato(self):
        res = cc.checar_fato(self._fato(
            (f"{self.base}/proibido", "qualquer coisa aqui"),
            (f"{self.base}/naoexiste", "qualquer coisa aqui"),
            (f"{self.base}/binario", "qualquer coisa aqui"),
        ), self.baixador)
        motivos = [f["motivo"] for f in res["fontes"]]
        self.assertEqual(res["status"], "falhou")
        self.assertIn("bloqueado_ou_paywall", motivos[0])
        self.assertEqual(motivos[1], "http_404")
        self.assertIn("formato_sem_suporte", motivos[2])

    def test_uma_fonte_boa_basta(self):
        res = cc.checar_fato(self._fato(
            (f"{self.base}/proibido", "qualquer coisa aqui"),
            (f"{self.base}/texto.txt", "linha única com ação"),
        ), self.baixador)
        self.assertEqual(res["status"], "ok")
        self.assertEqual([f["status"] for f in res["fontes"]], ["falhou", "ok"])

    def test_429_tenta_de_novo(self):
        _Manipulador.contagem_429 = 0
        rapido = cc.Baixador(self.cache, pausa=0)
        res = cc.checar_fato(self._fato((f"{self.base}/limitado", "linha única com ação")), rapido)
        self.assertEqual(res["status"], "ok")
        self.assertEqual(_Manipulador.contagem_429, 2)

    def test_429_persistente_falha(self):
        _Manipulador.contagem_429 = 0
        sem_retentar = cc.Baixador(self.cache, pausa=0, tentativas_429=0)
        res = cc.checar_fato(self._fato((f"{self.base}/limitado", "linha única com ação")), sem_retentar)
        self.assertEqual(res["status"], "falhou")
        self.assertIn("429", res["fontes"][0]["motivo"])

    def test_cli_relatorio_e_codigo_de_saida(self):
        lote = Path(self.tmp.name) / "lote.jsonl"
        fatos = [self._fato((f"{self.base}/artigo.html", "The deep biosphere is the part of the biosphere")),
                 self._fato((f"{self.base}/artigo.html", "Microbes on the surface glow in the dark at night"))]
        fatos[1]["id"] = "t-0002"
        lote.write_text("\n".join(json.dumps(f) for f in fatos), encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()) as saida:
            codigo = cc.main([str(lote), "--cache", str(self.cache), "--pausa", "0"])
        self.assertEqual(codigo, 1)  # um fato falhou
        self.assertIn("1 ok", saida.getvalue())
        rel = json.loads((Path(self.tmp.name) / "lote.checagem.json").read_text(encoding="utf-8"))
        self.assertEqual([f["status"] for f in rel["fatos"]], ["ok", "falhou"])
        self.assertEqual(rel["resumo"]["falhou"], 1)


if __name__ == "__main__":
    unittest.main()
