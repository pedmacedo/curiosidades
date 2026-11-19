"""Rodada 2 de Revolução industrial: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-revolucao_industrial-01.py"))
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

# 0011: "de memória" é contestado
trocar(11, confianca="consenso_parcial")
substituir(11, "gancho", "partiu para os EUA e lá reconstruiu as máquinas de memória.",
    "foi para os EUA, onde as reconstruiu com o que guardou na cabeça.")
substituir(11, "explicacao", "e reconstruiu de memória as máquinas movidas a água.",
    "e reconstruiu as máquinas movidas a água com base no que tinha memorizado. Historiadores discutem o quanto foi "
    "memória pura, já que ele contou com ajuda e com a máquina comprada por Brown.")
CANDIDATOS[10]["fontes"].append({
    "url": "https://navigator.rihs.org/rhode-island-a-bibliography-of-its-history/the-making-of-a-hero-samuel-slater-and-the-arkwright-frames/",
    "titulo": "The Making of a Hero: Samuel Slater and the Arkwright Frames (Rhode Island Historical Society)",
    "idioma": "en",
    "trecho": "Disputes the idea that Slater worked \"strictly from memory\" and without significant assistance"})

# 0012: os navios não eram do governo; português
substituir(12, "explicacao", "O governo americano mandou navios com comida para Lancashire", "Dos Estados Unidos chegaram navios com comida para Lancashire")
substituir(12, "explicacao", "passaram de os mais prósperos aos mais pobres", "passaram de mais bem pagos a mais pobres")

# 0013: "podia destruir"; a lei de 1908
substituir(13, "gancho", "destruía a mandíbula de quem os fabricava", "podia destruir a mandíbula de quem os fabricava")
substituir(13, "explicacao",
    "O fósforo branco só foi proibido de vez nos fósforos britânicos depois de 31 de dezembro de 1910, seguindo a Convenção de Berna, de 1906.",
    "O fósforo branco só foi banido dos fósforos britânicos por uma lei de 1908, que aplicava a Convenção de Berna, de 1906.")
acrescentar_trecho(13, 1, "In Great Britain, a ban on white phosphorus matches was introduced by the White Phosphorus Matches Prohibition Act 1908")
