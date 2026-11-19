"""Rodada 2 de Olimpíadas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-olimpiadas-01.py"))
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

# 0003: um dedo do pé, não o pé
substituir(3, "gancho", "com o pé deslocado", "com um dedo do pé deslocado")

# 0005: quadriga; "alguns" historiadores
substituir(5, "gancho", "sem conduzir a biga", "sem conduzir a quadriga")
substituir(5, "explicacao", "Historiadores de hoje desconfiam de um motivo mais prático", "Alguns historiadores de hoje desconfiam de um motivo mais prático")

# 0006: sem o "um ano"; venceu o que disputou
substituir(6, "gancho", "subornou os organizadores para adiar a Olimpíada em um ano e poder competir. Ganhou tudo, até uma corrida",
    "subornou os organizadores para adiar a Olimpíada e poder competir. Venceu todas as provas que disputou, até uma corrida")

# 0007: havia tochas em festivais de Atenas; não nos Jogos de Olímpia
substituir(7, "gancho", "mas não tem precedente antigo:", "mas não existia nos Jogos antigos:")

# 0009: a data do capacete é discutida
substituir(9, "explicacao", "um capacete coríntio do século VIII a.C., achado em Olímpia", "um capacete coríntio da Grécia antiga, achado em Olímpia")

# 0011: a pesquisa de Welch e o obituário de 2018 são momentos diferentes
substituir(11, "explicacao",
    "A façanha só veio à tona depois que Paula Welch, professora da Universidade da Flórida, pesquisou a vida dela, e o jornal The New York Times publicou seu obituário, atrasado, em 2018.",
    "A façanha só veio à tona décadas depois, quando Paula Welch, professora da Universidade da Flórida, pesquisou a vida dela; em 2018, o jornal The New York Times publicou seu obituário, atrasado.")

# 0014: Norman foi prata
substituir(14, "gancho", "Na foto do protesto de 1968, o terceiro homem no pódio, o australiano Peter Norman, usava um broche de apoio.",
    "Na foto do protesto de 1968, o australiano Peter Norman, prata na prova, usava um broche de apoio.")

# 0015: persistência, não engenhosidade
trocar(15, tipos_espanto=["historia_humana"])
