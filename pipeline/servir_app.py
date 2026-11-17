"""Abre o app no navegador do computador, servindo a pasta app/ em http://localhost:8765.

Uso (de qualquer pasta):
    python pipeline/servir_app.py
    python pipeline/servir_app.py --porta 9000 --sem-navegador

Se a porta estiver ocupada por outro programa, usa a próxima livre. Se quem está nela já
é este app, só abre o navegador.

Ou dê dois cliques em abrir_app.bat, na raiz do projeto.
O app não funciona abrindo o index.html direto (file://): o navegador bloqueia os módulos
JavaScript e o carregamento dos dados fora de um servidor.
Para parar o servidor, feche a janela ou aperte Ctrl+C.
"""

from __future__ import annotations

import argparse
import functools
import http.server
import socket
import sys
import threading
import urllib.request
import webbrowser

import comum

PASTA_APP = comum.RAIZ / "app"
PORTA_PADRAO = 8765
TENTATIVAS = 20


class Servidor(http.server.ThreadingHTTPServer):
    """Servidor que recusa a porta se ela já estiver em uso.

    No Windows, o SO_REUSEADDR padrão deixa dois servidores ocuparem a mesma porta, e as
    requisições caem em qualquer um deles. Aqui a porta fica exclusiva.
    """
    allow_reuse_address = False
    allow_reuse_port = False

    def server_bind(self):
        if hasattr(socket, "SO_EXCLUSIVEADDRUSE"):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        super().server_bind()


class Arquivos(http.server.SimpleHTTPRequestHandler):
    """Serve app/ com os tipos certos. No Windows, o registro às vezes diz que .js é
    text/plain, e aí o navegador recusa os módulos e o app fica em "Carregando…"."""
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".js": "text/javascript",
        ".json": "application/json",
        ".svg": "image/svg+xml",
        ".png": "image/png",
    }

    def guess_type(self, path):
        for ext, tipo in self.extensions_map.items():
            if ext and str(path).lower().endswith(ext):
                return tipo
        return super().guess_type(path)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


def porta_em_uso(porta: int) -> bool:
    """True se algum programa já atende na porta, por IPv4 ou IPv6.

    Só tentar ocupar a porta não basta: um servidor em "::" (IPv6, como o
    `python -m http.server`) e o nosso em 127.0.0.1 convivem na mesma porta, e o
    navegador, ao abrir "localhost", pode cair no outro (foi o que gerou um 404).
    """
    for familia, endereco in ((socket.AF_INET, "127.0.0.1"), (socket.AF_INET6, "::1")):
        try:
            with socket.socket(familia, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((endereco, porta)) == 0:
                    return True
        except OSError:
            continue  # sem IPv6 na máquina, por exemplo
    return False


def e_este_app(porta: int) -> bool:
    """True se quem atende na porta já é este app (aberto antes, em outra janela)."""
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{porta}/data/versao.js", timeout=1) as r:
            return b"VERSAO_DADOS" in r.read(2000)
    except (OSError, ValueError):
        return False


def main(argv: list[str] | None = None) -> int:
    comum.configurar_saida()
    p = argparse.ArgumentParser(description="Serve a pasta app/ e abre o navegador.")
    p.add_argument("--porta", type=int, default=PORTA_PADRAO,
                   help=f"porta preferida (padrão {PORTA_PADRAO}); se estiver ocupada, usa a próxima livre")
    p.add_argument("--sem-navegador", action="store_true", help="não abre o navegador")
    args = p.parse_args(argv)

    if not (PASTA_APP / "data" / "fatos.json").exists():
        print("Faltam os dados do app. Rode antes: python pipeline/construir_dados_app.py", file=sys.stderr)
        return 1

    handler = functools.partial(Arquivos, directory=str(PASTA_APP))
    servidor = None
    for porta in range(args.porta, args.porta + TENTATIVAS):
        if porta_em_uso(porta):
            if e_este_app(porta):
                url = f"http://localhost:{porta}/"
                print(f"O app já está aberto em {url} (em outra janela). Abrindo o navegador.")
                if not args.sem_navegador:
                    webbrowser.open(url)
                return 0
            print(f"A porta {porta} está ocupada por outro programa; tentando a próxima.")
            continue
        try:
            servidor = Servidor(("127.0.0.1", porta), handler)
            break
        except OSError:
            print(f"A porta {porta} está ocupada; tentando a próxima.")
    if servidor is None:
        print(f"Nenhuma porta livre entre {args.porta} e {args.porta + TENTATIVAS - 1}.", file=sys.stderr)
        return 1

    url = f"http://localhost:{porta}/"
    if porta != args.porta:
        print(f"Aviso: usando a porta {porta}. Os perfis ficam guardados por endereço, então o que")
        print(f"for salvo aqui não aparece em http://localhost:{args.porta}/ e vice-versa.")
    print(f"App em {url}  (pasta {PASTA_APP})")
    print("Deixe esta janela aberta enquanto usa o app. Para parar: Ctrl+C.")
    if not args.sem_navegador:
        threading.Timer(0.5, webbrowser.open, args=(url,)).start()
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor parado.")
    finally:
        servidor.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
