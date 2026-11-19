"""Rodada 2 de Fermentação: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-fermentacao-01.py"))
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

# 0007: sem o "limite de seis ácaros" (não oficial e com unidade divergente)
substituir(7, "gancho", "por ter ácaros acima do limite permitido", "por ter ácaros demais")
substituir(7, "explicacao",
    "alegando que o queijo passava do limite de seis ácaros por polegada cúbica e que os ácaros poderiam causar reação alérgica se consumidos em grande quantidade",
    "alegando que o queijo tinha ácaros demais e que eles poderiam causar reação alérgica se consumidos em grande quantidade")
substituir(7, "explicacao", "e suspendeu as importações", "e travou novas importações")

# 0011: 1.000 mg/L é a glicose
substituir(11, "explicacao", "acima disso, a produção de etanol aumentava até cerca de 1.000 mg por litro.",
    "acima disso, a velocidade de produção de etanol crescia junto com a glicose, até a glicose chegar a cerca de 1.000 mg por litro.")

# 0012: o menor genoma é sugerido
substituir(12, "explicacao", "é considerado o menor entre os lactobacilos.", "há indícios de que seja o menor entre os lactobacilos.")

# 0014: os esporos diminuíram; o risco não é imediato
substituir(14, "gancho", "quase não faz mais esporos", "produz cada vez menos esporos")
substituir(14, "gancho", "e a indústria tem dificuldade de obter o suficiente.", "e a indústria já tem dificuldade de obtê-los.")
substituir(14, "explicacao", "e ela perdeu a capacidade de produzir esporos assexuados, justamente o que se usa para inocular o leite.",
    "e a capacidade dela de produzir esporos assexuados, justamente o que se usa para inocular o leite, caiu muito.")
substituir(14, "explicacao", "e que a indústria tem dificuldade de conseguir esporos suficientes.",
    "e que a indústria tem dificuldade de conseguir esporos suficientes. O desaparecimento, porém, provavelmente não é para breve.")
acrescentar_trecho(14, 0, "Camembert as we know it today may disappear eventually, though probably not any time soon, per CNN.")
