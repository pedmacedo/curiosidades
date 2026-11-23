"""Rodada 2 de História da medicina: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-historia_medicina-01.py"))
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


# 0006: o erro de tradução não foi a única causa; cronologia da raspagem
substituir(6, "gancho", "Tudo começou num erro de tradução:", "Na origem, houve um erro de tradução:")
substituir(6, "explicacao", "O melhor vinha de uma montanha em Darabgerd, na Pérsia, e era raro e caro.",
    "O melhor vinha de uma montanha em Darabgerd, na Pérsia, e era raro e caro; por volta do século XII, o betume "
    "importado ficou escasso na Europa.")
substituir(6, "explicacao", "Daí em diante, passou-se a raspar", "A partir do século XII, passou-se a raspar")

# 0011: a cesariana na África; em 1865 só veio a alegação; o nome confirmado depois
trocar(11, gancho="James Barry, cirurgião do exército britânico, fez uma das primeiras cesarianas registradas na África com "
    "mãe e bebê vivos. Só após a morte dele, em 1865, soube-se que Barry fora criado como menina.")
substituir(11, "explicacao", "Não houve exame oficial, e a história chegou à imprensa.",
    "Nenhum médico examinou o corpo para confirmar, e a história chegou à imprensa. O nome de nascimento, Margaret "
    "Anne Bulkley, só foi confirmado por pesquisadores muito depois.")
substituir(11, "explicacao", "com a ajuda de amigos liberais da família", "com a ajuda de amigos liberais do falecido tio pintor")
acrescentar_trecho(11, 0, "Barry, who lived his entire adult life as a man, was named Margaret Anne at birth and was known as "
    "female in childhood. [...] Barry performed the first recorded caesarean section by a European in Africa in which both "
    "the mother and child survived the surgery. [...] Barry, his mother, and her late brother's influential, liberal-minded "
    "friends [...] However, no professional examination was carried out which could have confirmed these points beyond doubt. "
    "[...] this crucial piece of evidence was the one which enabled researchers to confirm Barry's past identity.")

# 0012: Moniz não operava
substituir(12, "explicacao", "passou a cortar essas ligações, a leucotomia, que ficaria conhecida como lobotomia.",
    "propôs cortar essas ligações: era a leucotomia, que ficaria conhecida como lobotomia. Moniz nunca operou com as "
    "próprias mãos, porque não tinha formação em neurocirurgia e sofria de gota. Quem fazia as cirurgias era o "
    "neurocirurgião Pedro Almeida Lima.")
acrescentar_trecho(12, 0, "He enlisted his long-time staff member and neurosurgeon Pedro Almeida Lima to test the procedure [...] "
    "Moniz never performed a surgery himself, partially because of his lack of neurosurgical training but also because he "
    "had limited use of his hands as a complication of gout.")

# 0013: a ordem e o sexo da primeira vítima são incertos
substituir(13, "explicacao", "Pouco mais de dois meses depois, mataram uma inquilina com febre e também a venderam.",
    "Pouco mais de dois meses depois, mataram um hóspede que estava com febre e também venderam o corpo.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(12, "explicacao", "Quem fazia as cirurgias era o neurocirurgião Pedro Almeida Lima.",
    "Sob as instruções dele, quem operava era sobretudo o neurocirurgião Pedro Almeida Lima.")
acrescentar_trecho(12, 0, "Instructed by Moniz, Lima performed ten of the first twenty surgeries")
