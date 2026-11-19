"""Rodada 2 de Calendários e feriados: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-calendarios-01.py"))
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


# 0008: a decisão de outubro de 2026
substituir(8, "explicacao",
    "Em 2022, a Conferência Geral de Pesos e Medidas decidiu ampliar, até 2035, a diferença tolerada entre o tempo atômico e o da rotação, de modo a garantir ao UTC pelo menos um século sem saltos.",
    "Em 2022, a Conferência Geral de Pesos e Medidas decidiu ampliar a diferença tolerada entre o tempo atômico e o da "
    "rotação. Em outubro de 2026, fixou o novo limite em uma hora, a partir de 20 de maio de 2027, o que na prática "
    "aposenta o segundo intercalar por vários séculos.")
acrescentar_trecho(8, 0, "On 15 October 2026, the General Conference on Weights and Measures (CGPM) voted to increase the maximum permitted "
    "difference between UT1 and UTC (DUT1) from 0.9 seconds to 3600 seconds (one hour), effective 20 May 2027, permitting "
    "the opportunity to defer leap second decisions for several centuries.")

# 0009: horário padrão do país, não "internacional"
substituir(9, "explicacao", "ao amanhecer, às 6h no horário internacional, e o da noite ao anoitecer, às seis da tarde",
    "ao amanhecer, às 6h no horário padrão do país (o mesmo relógio de 24 horas que usamos), e o da noite ao anoitecer, às 18h")
substituir(9, "explicacao", "do horário oficial", "do horário padrão")

# 0011: o ano inicial é de Scaliger; a contagem de dias veio com Herschel
substituir(11, "gancho", "A data foi escolhida em 1583 por ser o último ano em que três ciclos do calendário começaram juntos.",
    "O ano foi escolhido em 1583 por ser o último em que três ciclos do calendário começaram juntos.")
substituir(11, "explicacao", "Na contagem dos astrônomos, o dia 0 começa",
    "A contagem de dias em si veio depois: foi o astrônomo John Herschel quem a adaptou para a astronomia, em 1849. "
    "Na contagem dos astrônomos, o dia 0 começa")
acrescentar_trecho(11, 0, "John F. W. Herschel then developed them for astronomical use in his 1849 Outlines of Astronomy")

# 0014: "uma das duas mais importantes"
substituir(14, "explicacao", "A mais usada no dia a dia: se a lua nova calculada cair", "Uma das duas mais importantes: se a lua nova calculada cair")

# 0015: municípios e estados; limite dos feriados religiosos municipais
substituir(15, "explicacao",
    "Elas só viram feriado de fato quando um município as inclui entre os seus dias de guarda, que a lei limita a quatro, contando a Sexta-feira da Paixão.",
    "Elas podem virar feriado por lei municipal, e há estados que também tentam, como o Rio de Janeiro com a terça de "
    "Carnaval, decisão contestada no STF. Já os feriados religiosos municipais são limitados por lei a quatro, contando a Sexta-feira da Paixão.")
acrescentar_trecho(15, 0, "Esse é caso dos feriados de terça-feira de carnaval, de São Jorge e da Consciência Negra, no Rio de Janeiro")
