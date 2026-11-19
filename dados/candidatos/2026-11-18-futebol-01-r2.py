"""Rodada 2 de Futebol: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-futebol-01.py"))
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


# 0008: caixa de sapatos como versão mais contada; "nunca mais foi achada"; dúvida sobre o derretimento
trocar(8, gancho="Segundo a versão mais contada, a Jules Rimet passou a Segunda Guerra numa caixa de sapatos sob a cama "
    "de um dirigente. Em 1966, roubada, foi achada por um cão. Em 1983, sumiu no Rio e nunca mais foi achada.")
substituir(8, "explicacao",
    "tirou-a às escondidas de um banco em Roma e a escondeu numa caixa de sapatos sob a cama",
    "tirou-a às escondidas de um banco em Roma e, segundo o relato mais difundido, a escondeu numa caixa de "
    "sapatos sob a cama")
substituir(8, "explicacao", "muitos acreditam que foi derretida.",
    "muitos acreditam que foi derretida, embora haja quem duvide, já que ela teria pouco ouro para virar "
    "barras, e ache que ainda pode existir.")
acrescentar_trecho(8, 0, "However, some believe the trophy was not melted down (as it did not actually contain enough gold "
    "to produce gold bars if melted down) and was instead sold onto the black market and may still exist.")

# 0009: o gol foi do Brasil, num jogo que terminou empatado
substituir(9, "explicacao", "garantiu o empate do Brasil.", "foi o gol do Brasil num jogo que terminou empatado.")

# 0010: sem aspas atribuídas ao engenheiro da NASA
substituir(10, "gancho", "ela \"dançava\" no ar justamente na velocidade típica das cobranças de falta",
    "ela oscilava de forma errática justamente na velocidade típica das cobranças de falta")

# 0011: a taxa de defesas no centro vem de só 18 cobranças
substituir(11, "explicacao", "Na amostra, ficar parado rendeu defesas em 33,3% das cobranças,",
    "Na amostra, ficar parado rendeu defesas em 33,3% das cobranças (6 de apenas 18 casos),")
acrescentar_trecho(11, 0, "Total 141 18 127 286 [...] "
    "to the payoff of “stay in the center” (6 stopped kicks vs. 12 scored goals)")

# 0014: a regra dos seis segundos virou oito em 2025
substituir(14, "explicacao", "e desde 1997 não pode segurá-la por mais de seis segundos.",
    "e de 1997 a 2025 não podia segurá-la por mais de seis segundos (hoje o limite é de oito).")
acrescentar_trecho(14, 0, "2025: the keeper may not handle the ball for more than eight seconds.")
