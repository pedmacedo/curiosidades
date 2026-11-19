"""Rodada 2 de Geometria e topologia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-geometria_topologia-01.py"))
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


# 0005: sem citar a fonte no texto; parte da prova de Rao conferida por Hales
substituir(5, "explicacao",
    "Em 2017, Michaël Rao anunciou uma prova de que não existem outros, ainda sujeita à revisão por pares, segundo a Wikipedia.",
    "Em 2017, Michaël Rao anunciou uma prova, feita com auxílio de computador, de que não existem outros; parte dela foi "
    "conferida de forma independente, mas a revisão por pares completa ainda não havia sido concluída.")
acrescentar_trecho(5, 1, "As of 11 July 2017, the first half of Rao's proof had been independently verified (computer code available) by Thomas Hales [...] "
    "In July 2017 Michaël Rao completed a computer-assisted proof showing that there are no other types of convex pentagons that can tile the plane.")

# 0006: o chapéu precisa do espelho; a prova veio em 2023
substituir(6, "gancho", "Foi a solução da versão mais exigente do \"problema do einstein\".",
    "A prova veio em 2023 e resolveu o \"problema do einstein\".")

# 0007: "compatíveis com"; a frase de 2011 sem "ganhou peso"
substituir(7, "gancho", "têm propriedades dos padrões que nunca se repetem", "têm propriedades compatíveis com os padrões que nunca se repetem")
substituir(7, "explicacao",
    "O tema ganhou peso em 2011, quando o Nobel de Química premiou a descoberta dos quasicristais, e os ladrilhamentos de Penrose foram lembrados por ajudarem a entendê-la.",
    "Em 2011, o Nobel de Química premiou a descoberta dos quasicristais, e os ladrilhamentos de Penrose foram lembrados por terem ajudado a entendê-la.")

# 0009: "em 5 dimensões"; o pico depende do raio
substituir(9, "gancho", "na 5ª dimensão", "em 5 dimensões")
substituir(9, "explicacao",
    "chega ao máximo na 5 e depois diminui; com n indo ao infinito, ele tende a zero.",
    "chega ao máximo na 5 e depois diminui. A dimensão do pico muda conforme o raio escolhido, mas, para qualquer raio "
    "fixo, com n indo ao infinito, o volume tende a zero.")
acrescentar_trecho(9, 0, "for any fixed value of R the volume tends to a limiting value of 0 as n goes to infinity. Which value of n maximizes Vn(R) depends upon the value of R")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(15, "explicacao", "segura a forma tempo suficiente para ser comida sem sujeira", "a ponta não desaba antes da próxima mordida")
