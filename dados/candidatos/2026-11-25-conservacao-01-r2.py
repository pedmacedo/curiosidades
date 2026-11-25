"""Rodada 2 de Conservação de alimentos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-conservacao-01.py"))
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


# 0001: Appert levou a técnica à escala industrial, não a criou
trocar(1, nota_surpresa=3)
trocar(1, gancho="O francês que levou à indústria a conserva em vidro fervido recebeu 12 mil francos do governo para "
    "revelar o método, meio século antes de Pasteur explicar por que funcionava. Morreu pobre, em cova de indigente.")
substituir(1, "explicacao", "fechava com rolha e cera e "
    "fervia tudo em água.",
    "fechava com rolha e cera e fervia tudo em água. Donas de casa talvez já fizessem algo parecido, mas ele "
    "foi o primeiro a fazer isso em escala industrial.")
acrescentar_trecho(1, 0, "It is believed that this technique was already being used by homemakers, but Appert was the first to do this on an industrial scale.")

# 0002: a instrução era das primeiras latas; sem causalidade inventada
trocar(2, nota_surpresa=3)
substituir(2, "gancho", "Até lá, as latas traziam a instrução de abrir a tampa com martelo e talhadeira.",
    "As primeiras latas traziam a instrução de abrir a tampa com martelo e talhadeira.")
substituir(2, "explicacao", "As latas também foram ficando mais finas com o tempo, o que facilitou a invenção.",
    "As latas foram ficando mais finas com o tempo, mas nem assim surgiu logo um abridor de uso geral.")

# 0003: as críticas vieram depois
substituir(3, "explicacao", "Ela sempre teve críticos:", "Depois vieram as críticas:")

# 0005: há uma fonte (o museu do Smithsonian) que afirma que ele voou
trocar(5, confianca="consenso_parcial")
substituir(5, "explicacao", "os outros dois morreram sem "
    "comentar.",
    "os outros dois morreram sem comentar. Já um artigo do Museu Nacional do Ar e do Espaço, do Smithsonian, "
    "afirma que ele foi servido na Apollo 7.")
CANDIDATOS[4]["fontes"].append({
    "url": "https://airandspace.si.edu/stories/editorial/we-all-scream-even-space-ice-cream",
    "titulo": "We All Scream - Even in Space - for Ice Cream (National Air and Space Museum)",
    "idioma": "en",
    "trecho": "The gift-shop staple, “Astronaut Ice Cream,” was the first type of ice cream to make it into space during the Apollo 7 mission in 1968, and it was the only time it was “served” in space."})

# 0007: sem o "4 MeV", "permitem" em vez de "irradiam", sem "qualquer dose"
trocar(7, nota_surpresa=3,
    gancho="Já em 1906, uma patente britânica propunha conservar comida com radiação, dez anos após a descoberta da "
           "radioatividade. Hoje mais de 60 países permitem a técnica, e no Brasil qualquer alimento pode ser irradiado.")
substituir(7, "explicacao",
    "a energia usada é limitada, nos EUA a 4 MeV nos feixes de elétrons e de raios X, baixa demais para alterar o núcleo dos átomos do alimento",
    "a energia das fontes usadas é limitada por lei, baixa demais para alterar o núcleo dos átomos do alimento")
substituir(7, "explicacao", "no Brasil, qualquer alimento, em qualquer dose.", "no Brasil, qualquer alimento pode ser tratado.")
substituir(7, "explicacao", "em geral já embalada", "muitas vezes já embalada")

# 0008: o mérito era dispensar a fervura
substituir(8, "explicacao",
    "O que Pasteur trouxe foi a explicação: os culpados eram micro-organismos, e não bastava ferver tudo para "
    "afastá-los.",
    "O que Pasteur trouxe foi a explicação: os culpados eram micro-organismos, e para eliminá-los não era "
    "preciso ferver o vinho; um aquecimento curto e moderado bastava.")

# 0009: parágrafo dos cristais reescrito com palavras próprias
substituir(9, "explicacao",
    "Quando a comida congela devagar, perto do ponto de congelamento, cristais se formam dentro das "
    "células; no degelo, o líquido vaza dos tecidos danificados, e a comida fica mole ou seca. No "
    "congelamento rápido, em temperatura bem mais baixa, os cristais têm menos tempo para crescer e "
    "estragam menos.",
    "Congelar devagar dá tempo para a água formar cristais de gelo grandes, que rasgam os tecidos; no "
    "degelo, o suco das células escorre e a comida fica mole ou ressecada. Num frio intenso, o congelamento "
    "é tão rápido que só se formam cristais pequenos, e o estrago é bem menor.")

# 0013: os 27 dias atribuídos à Time
substituir(13, "gancho", "Sem eletricidade, berinjelas passaram a durar 27 dias, em vez de três.",
    "Sem eletricidade, berinjelas duravam 27 dias em vez de três, segundo a revista Time.")
substituir(13, "explicacao", "Segundo a revista Time, os "
    "tomates e pimentões passaram a durar até três semanas.",
    "Segundo a revista Time, que listou a invenção entre as melhores de 2001, as berinjelas duravam 27 dias "
    "em vez de três, e os tomates e pimentões, até três semanas.")
substituir_trecho(13, 1, "In rural northern Nigeria, there are no refrigerators.",
    "Best Inventions of 2001 [...] In rural northern Nigeria, there are no refrigerators.")

# 0014: sem a data de 400 a.C.; muros de 10 m, às vezes 15 m
substituir(14, "gancho", "Desde pelo menos 400 a.C., os persas já faziam e guardavam gelo no deserto, sem eletricidade.",
    "Há séculos, os persas faziam e guardavam gelo no deserto, sem eletricidade.")
substituir(14, "explicacao", "registros "
    "indicam construções desde 400 a.C., e muitas seguem de pé.",
    "muitas, erguidas há séculos, seguem de pé.")
substituir(14, "explicacao", "muros de até 10 m, no sentido "
    "leste-oeste,",
    "muros de 10 m, às vezes 15 m, no sentido leste-oeste,")
substituir_trecho(14, 0, "often as high as 10 m (33 ft) [...] ",
    "often as high as 10 m (33 ft) and sometimes as high as 15 m (49 ft) [...] ")

# notas dos fatos aprovados sem mudança, conforme os vereditos
trocar(4, nota_surpresa=3)
trocar(6, nota_surpresa=4)
trocar(11, nota_surpresa=3)
