"""Rodada 2 de Domesticação: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-domesticacao-01.py"))
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


# 0002: Mesoamérica
substituir(2, "explicacao", "uma gramínea selvagem do México, o teosinto do rio Balsas",
    "uma gramínea selvagem da Mesoamérica, o teosinto do rio Balsas")
substituir(2, "explicacao", "pelos agricultores americanos", "pelos agricultores indígenas da Mesoamérica")

# 0003: sem "só dominam porque"; tipos; a TR4
trocar(3, tipos_espanto=["contraintuitivo", "historia_humana"])
substituir(3, "gancho", "Elas só dominam o mercado porque a banana anterior, a Gros Michel, foi arrasada por um fungo.",
    "Elas tomaram o mercado depois que a banana anterior, a Gros Michel, foi arrasada por um fungo.")
substituir(3, "explicacao", "banana mais comum do mundo muito vulnerável.",
    "banana mais comum do mundo muito vulnerável. Em 2019, uma nova variante do fungo, a TR4, contra a qual "
    "não há fungicida eficaz, foi encontrada em fazendas do Caribe, e a Cavendish pode ter o mesmo destino da "
    "Gros Michel.")
acrescentar_trecho(3, 0, "in mid-2019, Panama disease Tropical Race 4 (TR4), was discovered on banana farms in the coastal Caribbean region. "
    "With no fungicide effective against TR4, the Cavendish may meet the same fate as the Gros Michel.")

# 0005: orelhas caídas numa filhote só
substituir(5, "gancho", "Em dez gerações, surgiram filhotes de orelha caída e manchas brancas no pelo, como cães, sem que ninguém escolhesse isso.",
    "Em dez gerações, surgiram filhotes com manchas brancas no pelo e até uma de orelhas caídas, como cães, sem que ninguém escolhesse isso.")

# 0006: o amargo é que é recessivo; a domesticação precoce vem de crescer de semente
substituir(6, "explicacao",
    "o amargor depende de um único gene, e a versão doce é recessiva, o que torna a característica fácil de selecionar",
    "o amargor depende de um único gene e é recessivo, duas coisas que facilitam a seleção")
substituir(6, "explicacao", "Por isso a amêndoa foi uma das primeiras árvores frutíferas domesticadas.",
    "A amêndoa também foi uma das primeiras árvores frutíferas domesticadas, em parte porque pode ser plantada "
    "direto da semente, talvez antes mesmo de existir a enxertia.")
substituir_trecho(6, 0, "Almonds were one of the earliest domesticated fruit trees [...]",
    "Almonds were one of the earliest domesticated fruit trees owing to their ability to be grown from seed, allowing their cultivation to have perhaps predated the advent of grafting. [...]")

# 0008: "provavelmente"; "pouca evidência"
trocar(8, gancho="A cenoura laranja provavelmente só virou variedade estável com os holandeses, no século XVIII, mas a ideia de que homenageava a Casa de Orange tem pouca evidência. As antigas eram roxas ou amarelas.")
substituir(8, "explicacao", "só virou uma variedade estável quando", "provavelmente só virou uma variedade estável quando")

# 0009: a domesticação dos cavalos Botai também é contestada
substituir(9, "gancho", "Mas o DNA de cavalos domésticos de 5 mil anos mostrou que ele pode descender deles, como o mustangue.",
    "Mas o DNA de cavalos de 5 mil anos, tidos como domésticos, sugeriu que ele pode descender deles, como o mustangue.")
substituir(9, "explicacao", "de 5 mil anos atrás, que já eram domesticados", "de 5 mil anos atrás, tidos como alguns dos primeiros cavalos domesticados")
substituir(9, "explicacao", "A classificação do animal ainda é debatida.",
    "E há pesquisadores que contestam até que os cavalos Botai tenham sido domesticados, enquanto outros "
    "rejeitam essa crítica. A classificação do animal ainda é debatida.")
acrescentar_trecho(9, 0, "In 2021, William Taylor and Christina Barron-Ortiz disputed the evidence for domestication of Przewalski's horse. "
    "Their case was rejected by Alan Outram and colleagues")

# 0010: a dependência vem da seleção, não da falta de voo
trocar(10, tipos_espanto=["contraintuitivo"])
substituir(10, "explicacao", "O resultado é que ela depende inteiramente dos humanos para se reproduzir.",
    "E os milênios de seleção a deixaram inteiramente dependente dos humanos para se reproduzir.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(2, "explicacao", "com centenas de grãos macios e expostos numa espiga que não se desmancha",
    "com muitos grãos expostos numa espiga que não se desmancha")
substituir(8, "gancho", "As antigas eram roxas ou amarelas.", "As antigas costumavam ser roxas ou amarelas.")
