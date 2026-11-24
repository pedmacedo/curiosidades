"""Rodada 2 de Partículas e física nuclear: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-23-fisica_particulas-01.py"))
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


# 0002: o telegrama de Pauli aparentemente não chegou (Arquivo do CERN)
substituir(2, "explicacao", "e agradeceu por telegrama, com a frase sobre saber esperar.",
    "e redigiu um telegrama de agradecimento com a frase sobre saber esperar; segundo o Arquivo do CERN, essa "
    "resposta aparentemente nunca chegou aos destinatários e sobreviveu só num rascunho.")
CANDIDATOS[1]["fontes"].append({
    "url": "https://archives.web.cern.ch/?p=610",
    "titulo": "…57 years ago – CERN Archives",
    "idioma": "en",
    "trecho": "Apparently Pauli's reply to the telegram did not arrive, so it survives only in the form of the draft sent by a secretary",
})

# 0005: sem o ano de 1923 e sem "tomaram por prótons"
substituir(5, "explicacao",
    "Rastros parecidos já tinham sido observados por Dmitri Skobeltsyn desde 1923, sem explicação na época, e o casal "
    "Joliot-Curie tinha indícios de pósitrons em fotos antigas, mas os havia tomado por prótons.",
    "Rastros parecidos já tinham aparecido em fotos de outros físicos, como o soviético Dmitri Skobeltsyn e o casal "
    "Joliot-Curie, mas ninguém soube explicá-los na época.")
substituir_trecho(5, 0, "no one at the time had an explanation for these anomalous tracks. [...] ",
    "Similar photographic evidence had been seen by Irene and Frederic Joliot-Curie and others but no one at the time had an explanation for these anomalous tracks. [...] ")
substituir_trecho(5, 0, " [...] Frédéric and Irène Joliot-Curie in Paris had evidence of positrons in old photographs when Anderson's results came out, but they had dismissed them as protons.", "")

# 0007: o ~9% do condensado de quarks e os ~91% da força forte
substituir(7, "explicacao", "partículas sem massa de repouso que prendem os quarks uns aos outros.",
    "partículas sem massa de repouso que prendem os quarks uns aos outros. Cálculos mais completos da "
    "cromodinâmica quântica, que contam também os quarks virtuais que surgem e somem dentro do próton, atribuem "
    "às massas dos quarks algo perto de 9% do total; mesmo assim, uns 91% vêm da força forte, e não do Higgs.")
acrescentar_trecho(7, 1, "About 91% of the proton mass is due to the quark and gluon fields and the QCD conformal anomaly rather than the Higgs interaction.")
acrescentar_trecho(7, 0, "the quark condensate (~9%, comprising the up and down quarks and a sea of virtual strange quarks)")

# 0008: o livro antigo é a Bíblia, com a Torre de Babel
substituir(8, "explicacao", "A segunda: haveria uma ligação com um livro muito mais antigo.",
    "A segunda: uma ligação com um livro bem mais antigo, a Bíblia. Lederman compara o campo de Higgs, que desfez "
    "a simetria do universo primordial e deu origem à variedade de partículas e forças, à Torre de Babel, onde uma "
    "língua única se fragmenta em muitas.")
acrescentar_trecho(8, 0, "his tongue-in-cheek title draws an analogy between the impact of the Higgs field on the fundamental symmetries at the Big Bang, "
    "and the apparent chaos of structures, particles, forces and interactions that resulted and shaped our present universe, "
    "with the biblical story of Babel in which the primordial single language of early Genesis was fragmented into many disparate languages and cultures")

# 0009: sem "só foi premiada em 1978"
substituir(9, "explicacao", "Wu foi mencionada no discurso deles, mas só foi premiada pela descoberta em 1978, com o primeiro Prêmio Wolf.",
    "Wu foi mencionada no discurso deles e, anos depois, em 1978, recebeu o primeiro Prêmio Wolf de Física.")

# 0012: os 1.500 anos em 2050 valem para o cenário de emissões mais altas
substituir(12, "explicacao",
    "Uma análise posterior, com cenários ainda mais altos, previu resultados ambíguos para amostras de quase 1.500 anos já em 2050.",
    "Uma análise posterior foi além: no cenário de emissões mais altas, a datação daria resultados ambíguos para amostras de quase 1.500 anos já em 2050.")
substituir_trecho(12, 2, "In this scenario, radiocarbon dating",
    "The “age” of the atmosphere in the highest emission scenario is up to 2,500 years in the year 2100 [...] In this scenario, radiocarbon dating")

# 0013: a reação de Hawass por inteiro; o corredor publicado em 2023
substituir(13, "explicacao", "e o egiptólogo Zahi Hawass reagiu dizendo que o estudo não oferecia nada à egiptologia.",
    "e o egiptólogo Zahi Hawass reagiu dizendo que o estudo não oferecia nada à egiptologia, embora depois tenha "
    "chamado de grande descoberta outro achado da mesma equipe.")
substituir(13, "explicacao", "Em 2023, a técnica revelou um corredor atrás da entrada original.",
    "Em 2023, a equipe publicou outro achado feito com múons: um corredor atrás da entrada original, depois "
    "inspecionado com uma câmera endoscópica.")
acrescentar_trecho(13, 0, "Later, once the North Face Corridor was inspected with an Endoscope, Hawass conversely commented that ScanPyramids's work had provided a \"major discovery\"")

# 0014: número de neutrinos da SN 1987A diverge entre fontes
substituir(14, "explicacao", "registrar dez neutrinos da supernova SN 1987A",
    "registrar cerca de uma dezena de neutrinos da supernova SN 1987A")

# 0016: Maria Gabriela levou a peça à Vigilância Sanitária
substituir(16, "gancho", "ela mesma levou o material a um hospital.", "levou a peça à Vigilância Sanitária.")
substituir(16, "explicacao", "Em 28 de setembro, recuperou o material e o levou a um hospital;",
    "Em 28 de setembro, recuperou a peça, que tinha sido revendida a outro ferro-velho, e a levou numa sacola "
    "plástica até a Vigilância Sanitária;")
acrescentar_trecho(16, 0, "On September 25, 1987, Devair Ferreira sold the scrap metal to a third scrapyard.")
CANDIDATOS[15]["fontes"].append({
    "url": "https://www.gov.br/ipen/pt-br/assuntos/clipping-de-noticias/quem-e-o-fisico-que-identificou-o-acidente-com-cesio-137-em-goiania",
    "titulo": "Quem é o físico que identificou o acidente com césio-137 em Goiânia",
    "idioma": "pt",
    "trecho": "A suspeita de que o pó era o culpado surgiu com Maria Gabriela, esposa de Devair, que em 28 de setembro levou a cápsula em uma sacola de plástico até a Vigilância Sanitária. "
              "O acidente foi oficialmente identificado no dia seguinte, 29 de setembro, pelo físico Walter Mendes, que confirmou os altos níveis de radiação",
})

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
# 0002: a autoria do nome "neutrino" é disputada (Wikipedia: Amaldi; Arquivo do CERN: Fermi).
substituir(2, "explicacao", "foi inventada de brincadeira por Edoardo Amaldi numa conversa com Enrico Fermi, em Roma, e Fermi a usou em congressos.", "nasceu no grupo de Enrico Fermi em Roma (segundo alguns relatos, de uma brincadeira do colega Edoardo Amaldi), e foi Fermi quem a levou a congressos.")
