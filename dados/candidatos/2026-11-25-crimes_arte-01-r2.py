"""Rodada 2 de Crimes e mistérios da arte: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-crimes_arte-01.py"))
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


# 0004: o branco de titânio ainda não era vendido em 1914; "vendido", não "revendido"
trocar(4, gancho="O falsário Wolfgang Beltracchi passou anos vendendo \"obras perdidas\" de pintores modernos. Caiu quando, "
                 "uma única vez, usou tinta pronta: o tubo tinha branco de titânio, pigmento ainda não vendido em 1914.")
substituir(4, "explicacao", "Campendonk e revendido por 2,88 milhões de euros", "Campendonk e vendido por 2,88 milhões de euros")

# 0009: o indício é a forma em cristais arredondados; análises iniciadas em 1972
substituir(9, "explicacao",
    "Em 1972, análises acharam nas linhas amareladas da tinta anatásio, uma forma de dióxido de titânio fabricada para pigmentos claros só a partir dos anos 1920.",
    "Em análises iniciadas em 1972, a equipe do químico forense Walter McCrone achou nas linhas amareladas da tinta "
    "anatásio (dióxido de titânio) em cristais arredondados, exatamente a forma fabricada para pigmentos claros só a "
    "partir dos anos 1920.")

# 0010: episódio atribuído aos primeiros biógrafos; segunda fonte; tema secundário sem "pintura"
trocar(10,
    temas_secundarios=["roma_antiga", "economia_curiosa"],
    gancho="Segundo biógrafos da época, o jovem Michelangelo envelheceu de propósito um Cupido que esculpiu, para vendê-lo "
           "como antiguidade. O cardeal que o comprou descobriu a farsa, mas a obra lhe abriu as portas de Roma.")
substituir(10, "explicacao",
    "Michelangelo tinha cerca de 20 anos quando começou a obra, em 1495, em Florença.",
    "Michelangelo tinha cerca de 20 anos quando começou a obra, em 1495, em Florença. O episódio chegou até nós pelos "
    "primeiros biógrafos, Ascanio Condivi, que escreveu com a colaboração do próprio Michelangelo, e Paolo Giovio. As "
    "versões variam sobre quem teve a ideia, e Vasari não o menciona nas Vidas.")
CANDIDATOS[9]["fontes"].append({
    "url": "https://www.theartnewspaper.com/2015/06/26/lost-art-michelangelos-sleeping-eros",
    "titulo": "Lost art: Michelangelo's Sleeping Eros",
    "idioma": "en",
    "trecho": "Michelangelo, it seems, set out to create a sculpture that could be passed off as an ancient original. "
              "His early biographer, Paolo Giovio (1483-1552), wrote: [...] "
              "Michelangelo attained the highest fame in sculpture when he made an Eros out of marble and, after having kept it buried in the earth for a time and then bringing it to light again, so that owing to the stains and marks that it had acquired, as well as other minor imperfections which had intentionally been inflicted upon it, the Eros simulated a work of antiquity. "
              "Then he sold it for a great price through a middleman to Cardinal Riario. [...] "
              "He became Michelangelo’s first patron in Rome [...] "
              "Giorgio Vasari, does not mention the story of Michelangelo’s Sleeping Eros in his canonical Lives of the Artists [...] "
              "Another contemporary biographer, Ascanio Condivi (1525-74), does tells the story, but with the twist that Sleeping Eros had already been sculpted by Michelangelo in Florence, but an offer from a slippery art dealer promised to set Michelangelo up in Rome, if he could sell the statue as an ancient Roman original. "
              "Condivi’s biography is an “authorised” account, however: Michelangelo cooperated with Condivi in exchange for control over what was included",
})

# 0011: data e local tradicionais, em debate
substituir(11, "explicacao",
    "O quadro, de 1609, tem cerca de 2,7 metros de altura e foi pintado na Sicília, um ano antes da morte do artista.",
    "O quadro, tradicionalmente datado de 1609, tem cerca de 2,7 metros de altura; por muito tempo se acreditou que "
    "foi pintado na Sicília, um ano antes da morte do artista.")

# 0012: tradução de "After Leonardo"; quem nega a autoria; o orbe
substituir(12, "explicacao", "com o título \"Segundo Leonardo da Vinci\"", "com o título \"A partir de Leonardo da Vinci\"")
substituir(12, "explicacao", "alguns especialistas, porém, acham que ele fez só partes dela.",
    "alguns especialistas, porém, acham que ele fez só partes dela, e outros negam a autoria.")
substituir(12, "explicacao",
    "mas a do quadro não distorce nada. Para o biógrafo Walter Isaacson, foi uma escolha consciente de Leonardo.",
    "mas no quadro o tecido atrás dela aparece quase sem distorção. Para o biógrafo Walter Isaacson, foi uma escolha "
    "consciente de Leonardo; para o historiador Charles Hope, que nega a autoria, é um indício contra ela.")
acrescentar_trecho(12, 0,
    "The British art historian Charles Hope dismissed the attribution to Leonardo entirely in a January 2020 analysis of the painting's quality and provenance. "
    "He doubted that Leonardo would have painted a work where the eyes were not level and the drapery undistorted by a crystal orb.")

# 0015: a biga do Museu Britânico não é atribuída como falsificação dos Riccardi
substituir(15, "explicacao",
    " Antes, a família já tinha vendido ao Museu Britânico uma biga de bronze supostamente achada perto de Orvieto.", "")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
# 0010: deixar claro que é Michelangelo, não Vasari, quem estudou o cupido
substituir(10, "explicacao",
    "Ele havia estudado uma escultura de cupido adormecido nos jardins dos Médici.",
    "Michelangelo havia estudado uma escultura de cupido adormecido nos jardins dos Médici.")
