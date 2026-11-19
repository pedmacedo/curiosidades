"""Rodada 2 de Sistema imunológico: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-sistema_imunologico-01.py"))
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


# 0002: no navio houve só a primeira reação; a descoberta decisiva foi no laboratório
substituir(2, "gancho", "A anafilaxia foi descoberta num navio do príncipe de Mônaco.",
    "A descoberta da anafilaxia começou num navio do príncipe de Mônaco.")

# 0003: Boston não "adotou"; a inoculação foi testada apesar da oposição
substituir(3, "gancho", "Em 1721, Boston adotou a inoculação contra a varíola graças a Onésimo",
    "Em 1721, a inoculação contra a varíola foi testada em Boston graças a Onésimo")

# 0005 (opcional do verificador): "podem sair" em vez de "saem"
substituir(5, "explicacao", "do próprio corpo saem do timo e entram na circulação",
    "do próprio corpo podem sair do timo e entrar na circulação")

# 0007: o papel da enzima AID, em vez de "mecanismo desconhecido"
substituir(7, "explicacao", "O mecanismo exato da hipermutação ainda não é conhecido.",
    "As mutações dependem de uma enzima chamada AID, embora detalhes do mecanismo ainda sejam estudados.")
acrescentar_trecho(7, 1, "Somatic hypermutation, a process in which the activation-induced cytidine deaminase (AID) enzyme randomly mutates the variable regions of the antibody and alters their affinity for the antigen, occurs in the dark zone.")

# 0011: Braille (o próprio artigo dele diz "likely due to sympathetic ophthalmia"); Thurber e a flecha
substituir(11, "explicacao",
    "A biografia dele costuma atribuir a cegueira a uma "
    "infecção que passou para os dois olhos, mas há quem a atribua à oftalmia simpática.",
    "O ferimento infeccionou gravemente e, aos cinco anos, ele já não "
    "enxergava com nenhum dos olhos; a perda do olho que não se ferira é atribuída, provavelmente, à oftalmia simpática.")
substituir(11, "explicacao", "que perdeu um olho aos seis anos", "que perdeu um olho na infância, atingido por uma flecha")
acrescentar_trecho(11, 1,
    "In agony, the young boy suffered for weeks as the wound became severely infected. "
    "He eventually lost sight in the other eye, likely due to sympathetic ophthalmia. "
    "Braille survived the torment of the infection, but by the age of five he was completely blind in both eyes.")
acrescentar_trecho(11, 2,
    "James turned around just as William shot, and the arrow hit James in his left eye. [...] "
    "Thurber had lost an eye in childhood")

# 0012: troca o exemplo da dengue pelo do reforço bivalente contra a Ômicron
substituir(12, "explicacao",
    "e pesa no desenho de vacinas: na dengue, depois de formada a resposta a um dos quatro sorotipos, "
    "é improvável que vacinar contra outro funcione, por isso a primeira dose precisa cobrir os quatro de "
    "forma equilibrada.",
    "e pesa no desenho de vacinas: o rendimento menor que o esperado do reforço bivalente contra a variante "
    "Ômicron, em quem já tinha tomado as vacinas originais de covid, foi atribuído a esse imprinting.")
substituir_trecho(12, 0,
    "In dengue fever, for example, once a response against one serotype has been established, it is unlikely that vaccination against a second will be effective. "
    "This implies that balanced responses against all four virus serotypes must be established with the first vaccine dose. [...] ",
    "")
acrescentar_trecho(12, 0,
    "The relative ineffectiveness of the bivalent booster against the SARS-CoV-2 Omicron variant in patients who had previously received COVID-19 vaccines has been attributed to immunological imprinting.")

# 0013: o vírus antigo no gancho; fosfocolina como proposta; Treg como resultado de um estudo
trocar(13, gancho="Para o sistema imune da mãe, o feto lembra um transplante, pois carrega genes do pai. Para não ser "
                  "rejeitada, a placenta usa vários truques, e um deles parece vir de um vírus antigo incorporado ao nosso DNA.")
substituir(13, "explicacao",
    "Ela "
    "secreta neurocinina B com moléculas de fosfocolina, o mesmo recurso que nematódeos parasitas usam para "
    "escapar das defesas do hospedeiro.",
    "Ela secreta neurocinina B ligada a fosfocolina, e há a proposta de que isso ajude a disfarçá-la, por "
    "analogia com o recurso que vermes nematódeos parasitas usam para escapar das defesas do hospedeiro.")
substituir(13, "explicacao", "mulheres com perdas gestacionais repetidas têm menos delas",
    "um estudo encontrou menos delas em mulheres com perdas gestacionais repetidas")
acrescentar_trecho(13, 0,
    "It is believed that the ancestors of modern viviparous mammals evolved after an infection by this virus, enabling the fetus to better resist the immune system of the mother.")

# 0014: tira o "1 em 1.000" (número divergente); frase sem número sustentada por CCR5 e pelo artigo de Brown
substituir(14, "explicacao",
    "Cerca de 1 em cada 1.000 pessoas de "
    "ascendência europeia herda essa mutação, que é mais rara em outras populações.",
    "A variante tem frequências mais altas no norte da Europa e é mais rara em outras populações.")
substituir_trecho(14, 0,
    "Roughly one in 1,000 people of European ancestry have this inherited mutation, but it is rarer in other populations.",
    "[...] but it is rarer in other populations. [...]")
CANDIDATOS[13]["fontes"].append(wiki("CCR5",
    "CCR5-Δ32 is a genetic variant characterized by a 32-base-pair deletion in the CCR5 gene, resulting in a nonfunctional receptor that prevents HIV-1 from entering immune cells. [...] "
    "with higher frequencies in Northern Europe",
    nome="CCR5"))
trocar(14, nota_surpresa=3)
