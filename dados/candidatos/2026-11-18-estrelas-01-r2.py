"""Rodada 2 de Estrelas e o Sol: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-estrelas-01.py"))
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


# 0002: quem demora é a energia, não o mesmo fóton
trocar(2, nota_surpresa=3)
substituir(2, "gancho", "mas pode ter levado de 10 mil a 170 mil anos só para sair do núcleo até a superfície",
    "mas a energia dela pode ter levado de 10 mil a 170 mil anos só para ir do núcleo até a superfície")
substituir(2, "explicacao", "Cada fóton é emitido de novo numa direção aleatória",
    "A energia é reemitida como um novo fóton, numa direção aleatória")
substituir(2, "explicacao", "Ou seja, a luz que bate em você agora passou milênios presa dentro do Sol.",
    "Ou seja, a energia da luz que bate em você agora passou milênios abrindo caminho dentro do Sol, de fóton em fóton.")

# 0004: sem "mistério"; sem a data ambígua e sem "depois de alguns anos"
trocar(4, tipos_espanto=["historia_humana"])
substituir(4, "explicacao", "Em 28 de novembro de 1967, ela notou", "Em 1967, ela notou")
substituir(4, "explicacao", "e depois de alguns anos foi identificada", "e depois foi identificada")

# 0006: helios, a palavra; Hillebrand; a terminação -ium
trocar(6, gancho="O hélio foi descoberto no Sol, numa linha amarela da luz de um eclipse em 1868, 27 anos antes de ser "
    "isolado e identificado na Terra. Por isso o nome vem de helios, \"Sol\" em grego.")
substituir(6, "explicacao", "A terminação -io costuma ser reservada a metais",
    "A terminação -ium, do nome original em inglês, costuma ser reservada a metais")
substituir(6, "explicacao", "encontraram o gás saindo de um minério de urânio.",
    "encontraram o gás saindo de um minério de urânio. Pouco antes, o geoquímico americano William Hillebrand "
    "já tinha isolado o gás de outro minério de urânio, mas atribuiu as linhas que viu ao nitrogênio.")
acrescentar_trecho(6, 0, "Lockyer named the element helium, from the Greek word for the Sun, ἥλιος (helios).")
acrescentar_trecho(6, 0, "Helium was also isolated by American geochemist William Francis Hillebrand prior to Ramsay's discovery, "
    "when he noticed unusual spectral lines while testing a sample of the mineral uraninite. "
    "Hillebrand, however, attributed the lines to nitrogen.")

# 0007: "principal fonte" ainda em debate
substituir(7, "explicacao",
    "O resultado reforçou que colisões assim, e não só explosões de supernova como se supunha, são a principal fonte dos elementos mais pesados que o ferro, como o ouro e a platina.",
    "O resultado confirmou que colisões assim fabricam elementos mais pesados que o ferro, como ouro e platina, um "
    "papel antes atribuído às explosões de supernova. Se elas são a principal fonte desses elementos ainda está em "
    "debate, e um único evento não basta para medir quanto cada fonte produz.")
acrescentar_trecho(7, 0, "GW170817 therefore confirmed neutron star mergers to be viable sites for the r-process [...] "
    "However, GW170817 alone is insufficient for ascertaining the yields of the production of heavy elements.")

# 0008: resolvido, não mistério; entre um terço e metade; parte do Nobel; sem a frase do MSW
trocar(8, tipos_espanto=["contraintuitivo", "historia_humana"])
substituir(8, "gancho", "Por quase 40 anos, os detectores acharam só cerca de um terço dos neutrinos que o Sol deveria emitir.",
    "Por mais de 30 anos, os detectores acharam só entre um terço e metade dos neutrinos que o Sol deveria emitir.")
substituir(8, "explicacao", "Outros experimentos confirmaram a falta: só cerca de um terço do esperado.",
    "Outros experimentos confirmaram a falta: conforme o detector, chegava entre um terço e metade do esperado.")
substituir(8, "explicacao", "Davis e Masatoshi Koshiba dividiram o Nobel de 2002",
    "Davis e Masatoshi Koshiba receberam parte do Nobel de Física de 2002")
substituir(8, "explicacao",
    " Curiosamente, até o comitê do Nobel errou num detalhe: nos neutrinos de alta energia vistos por um dos experimentos, a mudança vem de um efeito ligado à matéria do Sol, chamado Mikheyev–Smirnov–Wolfenstein.",
    "")
acrescentar_trecho(8, 0, "In various experiments, the number deficit was between one half and two thirds.")

# 0009: poeira como explicação mais aceita; companheira ainda não confirmada
trocar(9, nota_surpresa=3,
    gancho="Em 2019, Betelgeuse, o ombro de Órion, perdeu dois terços do brilho, e muitos acharam que ia explodir. "
           "Tudo indica que era poeira soprada pela própria estrela. Em 2025, acharam uma provável companheira dela.")
substituir(9, "explicacao", "Estudos com o telescópio espacial Hubble indicaram a causa:",
    "Estudos com o telescópio espacial Hubble apontaram a explicação mais aceita (um estudo em ondas "
    "submilimétricas atribuiu o escurecimento a grandes manchas na superfície):")
substituir(9, "explicacao", "foram anunciadas observações de uma provável estrela companheira",
    "foi anunciada uma possível detecção direta, ainda não confirmada, de uma provável estrela companheira")
acrescentar_trecho(9, 0, "A study that uses observations at submillimetre wavelengths rules out significant contributions from dust absorption. "
    "Instead, large starspots appear to be the cause for the dimming. [...] "
    "A possible direct detection with the Gemini North Observatory (instrument ‘Alopeke) was announced in July 2025 [...] "
    "At only 1.5 σ significance, this is not a confirmed detection")

# 0010: kelvin; explicação reescrita com mais liberdade
trocar(10,
    gancho="A superfície do Sol tem uns 6.000 kelvin, mas a coroa, a camada externa e rarefeita acima dela, passa de 1 "
           "milhão de kelvin. Como algo fica mais quente longe da fonte de calor ainda é discutido.",
    explicacao=(
        "Se o calor da coroa viesse só da superfície, ela teria de ser mais fria que a fotosfera, que está a uns "
        "6.000 kelvin. Em vez disso, a coroa chega a 1 a 2 milhões de kelvin, o que mostra que alguma outra coisa a "
        "aquece. A suspeita recai sobre a agitação da zona de convecção, a camada turbulenta que fica logo abaixo da "
        "superfície, e há duas ideias principais sobre como essa energia sobe. Pela primeira, a turbulência gera "
        "ondas, sonoras, gravitacionais ou magnéticas, que viajam para cima e se desfazem em calor lá no alto. Pela "
        "segunda, o vaivém da superfície vai torcendo e acumulando energia nos campos magnéticos, que de tempos em "
        "tempos se rompem e se religam. Isso libera a energia tanto em grandes erupções solares quanto numa "
        "infinidade de estouros pequenos, as nanoexplosões. A ideia das ondas tem um problema: quase todas se perdem "
        "ou se desviam antes de chegar à coroa, e as únicas que chegam, as ondas de Alfvén, têm dificuldade de "
        "deixar sua energia lá. Por isso ainda não se sabe se elas aquecem de forma eficiente."
    ))

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(6, "explicacao", "Pouco antes, o geoquímico americano William Hillebrand", "Antes disso, o geoquímico americano William Hillebrand")
substituir(8, "gancho", "e isso rendeu dois prêmios Nobel.", "e a história rendeu dois prêmios Nobel.")
substituir(8, "explicacao", "O Sol produz energia fundindo hidrogênio, e cada reação solta neutrinos",
    "O Sol produz energia fundindo hidrogênio, e essa fusão solta neutrinos")
substituir(9, "gancho", "Tudo indica que era poeira soprada pela própria estrela.", "A explicação mais aceita é poeira soprada pela própria estrela.")
substituir(9, "gancho", "Em 2025, acharam uma provável companheira dela.", "Em 2025, surgiu indício de uma companheira.")
