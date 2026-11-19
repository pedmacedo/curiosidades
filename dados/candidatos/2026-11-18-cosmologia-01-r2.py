"""Rodada 2 de Cosmologia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-cosmologia-01.py"))
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


# 0003: McKellar não foi o primeiro a achar moléculas interestelares (CH, 1937)
substituir(3, "explicacao",
    "Em 1940, foi o primeiro a identificar moléculas no meio interestelar, entre elas o radical cianogênio (CN).",
    "Em 1940, identificou o radical cianogênio (CN) no meio interestelar, uma das primeiras moléculas encontradas no espaço.")

# 0005: Alpher como autor principal; a chave do trocadilho "Delter"
substituir(5, "gancho", "O aluno que fez o trabalho não achou graça.",
    "O doutorando que era o autor principal não achou graça.")
substituir(5, "explicacao", "a mudar de nome para Delter.",
    "a mudar de nome para Delter, trocadilho com delta, a quarta letra grega.")
CANDIDATOS[4]["fontes"].append(wiki("Delta_(letter)",
    "is the fourth letter of the Greek alphabet.", nome="Delta (letter)"))

# 0008: o outro lado da tensão (gigantes vermelhas, 69,8)
substituir(8, "explicacao",
    "medidas de cefeidas do Hubble. ",
    "medidas de cefeidas do Hubble. Mas nem todo método local dá 73: em 2019, uma medida baseada em estrelas "
    "gigantes vermelhas, com dados do telescópio Hubble, chegou a um valor intermediário, de 69,8. ")
acrescentar_trecho(8, 0,
    "Also in July 2019, astronomers reported another new method, using data from the Hubble Space Telescope and based on distances to red giant stars calculated using the tip of the red-giant branch (TRGB) distance indicator. "
    "Their measurement of the Hubble constant is 69.8+1.9−1.9 (km/s)/Mpc.")

# 0009: não afirmar que o erro é da teoria
substituir(9, "gancho", "Mas erra no lítio:", "Mas não fecha no lítio:")
substituir(9, "explicacao",
    "A discrepância ganhou nome próprio: problema do lítio cosmológico.",
    "As soluções propostas se dividem em três grupos: o lítio primordial estaria sendo medido errado, inclusive "
    "por causa do que acontece nas estrelas; os cálculos de física nuclear do Big Bang teriam falhas; ou seria "
    "preciso física além do modelo padrão. A discrepância ganhou nome próprio: problema do lítio cosmológico.")
acrescentar_trecho(9, 0,
    "Possible solutions fall into three broad classes. [...] "
    "Considering the possibility that BBN predictions are sound, the measured value of the primordial lithium abundance should be in error [...] "
    "Furthermore, more observations on lithium depletion remain important since present lithium levels might not reflect the initial abundance in the star. [...] "
    "When one considers the possibility that the measured primordial lithium abundance is correct and based on the Standard Model of particle physics and the standard cosmology, the lithium problem implies errors in the BBN light element predictions. [...] "
    "Under the assumptions of all correct calculation, solutions beyond the existing Standard Model or standard cosmology might be needed.")

# 0014: 1884 é a data das palestras; o livro com os apêndices é posterior; conclusão de Poincaré
substituir(14, "gancho",
    "Mas Lord Kelvin já falava em \"corpos escuros\" em 1884, e Poincaré usou a expressão \"matéria escura\" em 1906.",
    "Mas, décadas antes, Lord Kelvin já especulava que muitas estrelas seriam \"corpos escuros\", e Poincaré usou a expressão \"matéria escura\" em 1906.")
substituir(14, "explicacao", "Em palestras de 1884 em Baltimore, Lord Kelvin estimou",
    "Nos apêndices de um livro baseado em palestras que deu em Baltimore em 1884, Lord Kelvin estimou")
substituir(14, "explicacao", "termo francês matière obscure ao discutir esse trabalho.",
    "termo francês matière obscure ao discutir esse trabalho e concluiu que haveria menos matéria escura do que "
    "visível, o que depois se mostrou falso.")
acrescentar_trecho(14, 0,
    "He concluded that the amount of dark matter would need to be less than that of visible matter, which was later found to be false.")

# 0015: 2025 não foi a primeira pista, e sim um censo
substituir(15, "gancho",
    "Em 2025, astrônomos a acharam usando flashes de rádio como lanterna: ela está espalhada como névoa entre as galáxias.",
    "Usando flashes de rádio como lanterna, um censo de 2025 mostrou que ela está espalhada como névoa entre as galáxias.")
substituir(15, "explicacao", "A solução veio das rajadas rápidas de rádio,",
    "Outras técnicas, como medidas em raios X do gás que liga as galáxias, já davam pistas de onde ela estaria. "
    "O censo de 2025 veio das rajadas rápidas de rádio,")
acrescentar_trecho(15, 0, "other techniques had only hinted at its existence.")
acrescentar_trecho(15, 1,
    "In 2020 astrophysicists reported the first direct X-ray emissions measurement of baryonic matter of cosmic web filaments. "
    "Both results are consistent with WHIM accounting for the missing baryons.")
