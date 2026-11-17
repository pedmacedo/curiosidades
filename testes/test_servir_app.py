"""Testes do servir_app.py: detecção de porta ocupada por IPv4 e por IPv6 e tipos MIME."""

from __future__ import annotations

import socket
import unittest

import auxiliar  # noqa: F401  (põe pipeline/ no caminho)
import servir_app as sa


def ouvir(familia: int, endereco: str) -> socket.socket:
    s = socket.socket(familia, socket.SOCK_STREAM)
    s.bind((endereco, 0))
    s.listen(1)
    return s


class TestPorta(unittest.TestCase):
    def test_porta_ocupada_em_ipv4(self):
        with ouvir(socket.AF_INET, "127.0.0.1") as s:
            self.assertTrue(sa.porta_em_uso(s.getsockname()[1]))

    def test_porta_ocupada_so_em_ipv6(self):
        # o caso do 404: outro servidor só no IPv6, e o nosso no IPv4
        try:
            s = ouvir(socket.AF_INET6, "::1")
        except OSError:
            self.skipTest("máquina sem IPv6")
        with s:
            self.assertTrue(sa.porta_em_uso(s.getsockname()[1]))

    def test_porta_livre(self):
        with ouvir(socket.AF_INET, "127.0.0.1") as s:
            porta = s.getsockname()[1]
        self.assertFalse(sa.porta_em_uso(porta))
        self.assertFalse(sa.e_este_app(porta))

    def test_tipos_mime(self):
        h = sa.Arquivos.__new__(sa.Arquivos)
        self.assertEqual(h.guess_type("app/app.js"), "text/javascript")
        self.assertEqual(h.guess_type("data/fatos.json"), "application/json")


if __name__ == "__main__":
    unittest.main()
