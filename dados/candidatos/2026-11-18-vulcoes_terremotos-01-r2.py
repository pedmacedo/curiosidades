"""Rodada 2 de Vulcões e terremotos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-vulcoes_terremotos-01.py"))
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


def acrescentar_trecho(n, i_fonte, extra):
    CANDIDATOS[n - 1]["fontes"][i_fonte]["trecho"] += " [...] " + extra


# 0002: ela começou o livro ali
substituir(2, "gancho", "onde ela escreveu Frankenstein.", "onde ela começou Frankenstein.")

# 0007: a região de Wellington; o evento de 1999 sem redundância
substituir(7, "gancho", "sob a capital da Nova Zelândia,", "sob a região de Wellington, capital da Nova Zelândia,")
substituir(7, "explicacao",
    "escorregou 2 centímetros para sudoeste ao longo de umas semanas, numa área de 50 por 300 quilômetros, em cerca de 35 dias, sem nenhum sinal sísmico de tremor comum.",
    "escorregou 2 centímetros para sudoeste numa área de 50 por 300 quilômetros, num evento de cerca de 35 dias, "
    "sem nenhum sinal sísmico significativo.")
acrescentar_trecho(7, 0, "yet no significant seismic signal was detected.")

# 0008: magnitude nas duas versões; mortos e feridos; a previsão vista como sorte
trocar(8, gancho="Em 1975, a China esvaziou boa parte de Haicheng horas antes de um terremoto de magnitude 7,3: é tida "
    "como a única evacuação bem-sucedida antes de um tremor. Em 1976, sem esses sinais, Tangshan perdeu mais de 240 mil.")
substituir(8, "explicacao", "com magnitude 7,5.", "com magnitude 7,3 (algumas fontes falam em 7,5).")
substituir(8, "explicacao",
    "Estima-se que a evacuação tenha evitado até 150 mil mortes, embora muitos tenham morrido nos dias seguintes por incêndios e frio.",
    "Houve menos de 2.500 mortes, muitas delas nos dias seguintes, por incêndios e frio; sem a evacuação, "
    "estima-se que mortos e feridos pudessem passar de 150 mil.")
substituir(8, "explicacao",
    "matou mais de 240 mil pessoas. Até hoje, prever terremotos com precisão continua fora de alcance.",
    "matou mais de 240 mil pessoas. Por isso, a \"previsão\" de Haicheng foi depois examinada a fundo e "
    "considerada um golpe de sorte: os abalos precursores que guiaram a decisão não aparecem de forma regular e "
    "confiável antes dos terremotos.")
acrescentar_trecho(8, 0, "It measured 7.3 on the surface-wave magnitude scale, making it the largest earthquake in northeastern China since records began.")
acrescentar_trecho(8, 0, "Due to these foreshocks, some of the final evacuation orders were given only hours before the destructive earthquake preventing further loss of life. "
    "This \"prediction\" was later put under heavy scrutiny and was deemed as a fluke. "
    "This prediction and evacuation limited the number of deaths to under 2,500 and total injuries to 27,500 people. "
    "The estimated number of injured and deceased individuals without the implementation of the evacuation may have been more than 150,000")
acrescentar_trecho(8, 0, "the foreshocks that played a huge role in leading to prediction of this earthquake are not a regular, reliable occurrence before all earthquakes")
acrescentar_trecho(8, 0, "Much of the city was evacuated before the earthquake")

# 0010: "3 ou mais"; o dado de 2015 era até agosto
substituir(10, "gancho", "uns dois terremotos de magnitude 3 por ano", "uns dois terremotos de magnitude 3 ou mais por ano")
substituir(10, "explicacao", "Em 2015, chegou a mais de seis vezes o número da Califórnia.",
    "Em meados de agosto de 2015, o total do ano já superava o de 2014 inteiro e passava de seis vezes o da Califórnia.")
acrescentar_trecho(10, 0, "Late on August 16, the number of earthquakes in Oklahoma with moment magnitudes of ≥3.0 for the year of 2015")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(7, "explicacao", "Os terremotos lentos aparecem sobretudo em zonas de subducção",
    "Os terremotos lentos são mais bem documentados em certas zonas de subducção")
substituir(8, "explicacao", "foi depois examinada a fundo e considerada um golpe de sorte",
    "foi depois examinada a fundo e é vista por muitos como provável golpe de sorte")
