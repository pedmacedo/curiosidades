"""Rodada 2 de História do português: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-historia_portugues-01.py"))
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


# 0001: não era "quase toda a Península"
substituir(1, "gancho", "Era a língua da poesia lírica em quase toda a Península Ibérica.", "Era a língua da moda para a poesia lírica até em Castela.")
substituir(1, "explicacao", "quem compunha poesia lírica nas terras que hoje são Espanha e Portugal o fazia, quase sem exceção, em galego-português",
    "nas cortes de Portugal, da Galiza, de Leão e de Castela, a poesia lírica era composta sobretudo em galego-português")

# 0011: a administração colonial francesa impôs o alfabeto; o chữ Nôm seguia dominante entre os católicos
substituir(11, "gancho", "e baseado sobretudo na ortografia portuguesa. Os franceses o aceitaram a contragosto.",
    "e baseado sobretudo na ortografia portuguesa, não na francesa.")
substituir(11, "explicacao", "Os franceses o aceitaram a contragosto, por ser baseado na ortografia portuguesa, e não na francesa.",
    "Curiosamente, a potência colonial acabou difundindo uma escrita baseada na ortografia portuguesa, e não na francesa.")
substituir(11, "explicacao", "Por 200 anos, esse alfabeto ficou restrito à comunidade católica.",
    "Por 200 anos, esse alfabeto só foi usado na comunidade católica, e mesmo ali perdia para a escrita tradicional de caracteres (chữ Nôm).")
acrescentar_trecho(11, 0, "works written in the Vietnamese alphabet saw limited use, while Catholic texts in chữ Nôm were significantly more widespread. "
    "Chữ Nôm thus remained the principal writing system used by Vietnamese Catholics during this period. [...] "
    "In 1910, the French colonial administration enforced chữ Quốc ngữ.")

# 0013: a contagem das peças varia
substituir(13, "gancho", "Das pelo menos 44 peças dele, só 14 são em português;", "Das cerca de 44 peças dele, só um terço é inteiramente em português;")
substituir(13, "explicacao", "Das pelo menos 44 peças que escreveu, 10 são em espanhol, 14 em português e as restantes misturam os dois idiomas.",
    "Numa contagem clássica, das pelo menos 44 peças que escreveu, 10 são em espanhol, 14 em português e as restantes "
    "misturam os dois idiomas; outras contagens variam um pouco.")

# 0014: antes de 1911 não havia grafia oficial para coincidir
substituir(14, "gancho", "e as duas grafias nunca mais coincidiram totalmente.", "e até hoje as grafias oficiais dos dois países não coincidem por completo.")

# 0015: não minimizar as violências do documento
substituir(15, "explicacao", "A lista vai de terras cujos frutos nunca recebeu até humilhações domésticas: segundo o texto,",
    "A lista mistura terras cujos frutos nunca recebeu e violências sérias, como um criado levado à força pelos montes, "
    "com humilhações domésticas que o texto chama de \"desonras\": segundo ele,")

# ganchos encurtados para caber em 220 caracteres
substituir(13, "gancho", "só um terço é inteiramente em português; as demais são em espanhol ou misturam as duas línguas.",
    "só um terço é todo em português; as demais são em espanhol ou misturam as duas.")
substituir(14, "gancho", ", que não a adotou, e até hoje as grafias oficiais dos dois países não coincidem por completo.",
    ", que não a adotou. Até hoje as grafias dos dois países não coincidem por completo.")
