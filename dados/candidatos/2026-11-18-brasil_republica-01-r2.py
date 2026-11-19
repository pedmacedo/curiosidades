"""Rodada 2 de Brasil República: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-brasil_republica-01.py"))
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

# 0002: a quarta expedição chegou a mais de 8.000 soldados
substituir(2, "explicacao",
    "Assim, a quarta expedição, de 3.000 homens com metralhadoras e canhões pesados, encontrou um inimigo com alguns dos fuzis de repetição mais avançados da época.",
    "Assim, a quarta expedição, que levou metralhadoras e canhões pesados e chegou a reunir mais de 8.000 soldados, encontrou um inimigo com alguns dos fuzis de repetição mais avançados da época.")
acrescentar_trecho(2, 0, "A month later a second campaign began with over 8,000 soldiers who encircled and laid siege to Canudos.")

# 0003: as prisões vieram com as revoltas de dezembro; João Cândido sobreviveu
substituir(3, "explicacao", "A vitória durou pouco: logo depois, centenas foram presos na ilha das Cobras.",
    "A vitória durou pouco: semanas depois, aproveitando novas revoltas em dezembro, o governo prendeu centenas deles na ilha das Cobras.")
substituir(3, "explicacao", "na manhã seguinte, só dois estavam vivos.", "na manhã seguinte, só dois estavam vivos, e João Cândido era um deles.")
acrescentar_trecho(3, 0, "On 9 December, crewmen onboard Rio Grande do Sul [...] used this opportunity to round up the remaining amnestied sailors and put them in prison. [...] "
    "There, João Cândido and seventeen others were transferred to an isolation cell; by the next morning, only two were left alive. [...] "
    "It took eighteen months before he and nine other sailors faced trial")

# 0008: a expressão já circulava; a FEB a tornou famosa
substituir(8, "gancho", "\"A cobra vai fumar\" nasceu de uma piada da Segunda Guerra:", "\"A cobra vai fumar\" ganhou fama com uma piada da Segunda Guerra:")
substituir(8, "explicacao", "\"A cobra vai fumar\" passou a significar algo que nunca aconteceria.",
    "Antes de a FEB entrar em combate, \"a cobra vai fumar\" era usada para falar de algo que nunca aconteceria, como \"quando as galinhas criarem dentes\".")
