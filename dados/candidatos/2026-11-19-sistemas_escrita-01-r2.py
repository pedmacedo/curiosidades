"""Rodada 2 de Sistemas de escrita: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-sistemas_escrita-01.py"))
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)

LOTE, AREA, TEMA = _base.LOTE, _base.AREA, _base.TEMA
wiki = _base.wiki
CANDIDATOS = _base.CANDIDATOS


def trocar(n, **campos):
    CANDIDATOS[n - 1].update(campos)


def substituir(n, campo, velho, novo):
    texto = CANDIDATOS[n - 1][campo]
    assert velho in texto, (n, velho)
    CANDIDATOS[n - 1][campo] = texto.replace(velho, novo)


def substituir_trecho(n, i_fonte, velho, novo):
    fonte = CANDIDATOS[n - 1]["fontes"][i_fonte]
    assert velho in fonte["trecho"], (n, velho)
    fonte["trecho"] = fonte["trecho"].replace(velho, novo)


def acrescentar_trecho(n, i_fonte, extra):
    CANDIDATOS[n - 1]["fontes"][i_fonte]["trecho"] += " [...] " + extra


# 0004: algarismos árabes orientais; o thaana chegou a ser deixado de lado
substituir(4, "gancho", "as nove primeiras letras vêm dos algarismos arábicos, e as nove seguintes, de algarismos indianos usados nas ilhas.",
    "as nove primeiras letras vêm dos algarismos do mundo árabe (١ ٢ ٣...), e as nove seguintes, de algarismos indianos locais.")
substituir(4, "explicacao", "saíram dos numerais arábicos;", "saíram dos numerais arábicos orientais, os usados no mundo árabe;")
substituir(4, "explicacao", "De fato, no início o thaana servia", "No início, o thaana servia")
substituir(4, "explicacao", "No século XX, quase foi trocado:", "No século XX, chegou a ser deixado de lado na administração:")

# 0006: na escrita latina; sem atribuir intenção
trocar(6, gancho="Os romanos chegaram a separar palavras com pontos, mas passaram a seguir os gregos, que escreviam tudo emendado. "
    "No latim, os espaços só surgiram em Bíblias irlandesas e anglo-saxãs dos séculos VII e VIII.")
substituir(6, "explicacao", "é aceito em geral que os espaços apareceram primeiro em Bíblias", "é aceito em geral que, na escrita latina, os espaços apareceram primeiro em Bíblias")

# 0008: grafia brasileira; sem repetir o bet do 0007
substituir(8, "explicacao", "virou ómicron", "virou ômicron")
substituir(8, "explicacao", "ʔalp, \"boi\", nomeava a oclusiva glotal, e bet, \"casa\", o som de b.", "ʔalp, \"boi\", nomeava a oclusiva glotal.")

# 0011: a ordem certa do exemplo
substituir(11, "explicacao", "e \"jam\" aparecia entre \"iambic\" e \"jangle\"", "e \"iambic\" aparecia entre \"jam\" e \"jangle\"")

# 0013: "em sua maioria contábeis"; destacar a duração
trocar(13, gancho="A escrita cuneiforme, cujos primeiros registros eram em sua maioria contábeis, durou mais de três mil anos: a "
    "última tabuinha de data firme, um texto astronômico de Uruk, é de 79 ou 80 d.C., já na era romana.")

# 0015: sem descendência inventada; abjad aumentado; tipos
trocar(15, tipos_espanto=["origem_inesperada", "conexao_inesperada"])
substituir(15, "explicacao", "A primeira passou ao fenício, ao hebraico antigo, ao aramaico, ao siríaco, ao grego e ao latino; a segunda sobrevive na escrita ge'ez, da qual foi adaptada a do amárico.",
    "A primeira é a mesma usada depois pelos alfabetos fenício, hebraico antigo, aramaico, siríaco, grego e latino; a segunda aparece na escrita ge'ez, da qual foi adaptada a do amárico.")
substituir(15, "explicacao", "Como outras escritas semíticas, só anotava consoantes",
    "Como outras escritas semíticas, anotava basicamente as consoantes (com a exceção curiosa das vogais depois da oclusiva glotal)")
