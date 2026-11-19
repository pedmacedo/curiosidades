"""Rodada 2 de Doenças infecciosas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-doencas_infecciosas-01.py"))
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


# 0005: "dez vezes" é taxa; sem aspas de citação em "obsessão cara"
substituir(5, "gancho", "que afastasse o médico com uma \"obsessão cara\" por mosquitos.",
    "que afastasse o médico por sua obsessão cara com mosquitos.")
substituir(5, "explicacao", "e, em 1906, morreram dez vezes mais que os brancos.",
    "e, em 1906, morriam a uma taxa dez vezes maior que a dos brancos.")

# 0007: a doença foi declarada erradicada (o vírus não está extinto)
substituir(7, "gancho", "era a peste bovina, extinta em 2011.", "era a peste bovina, declarada erradicada em 2011.")

# 0008: deixar clara a era das datas antigas
substituir(8, "explicacao", "apontavam para os séculos XI e XII, com margem que chegava ao século V.",
    "apontavam para os séculos XI e XII d.C., com margem que chegava ao século V d.C.")

# 0011: "a partir de 1909"; mentor; "em detalhe"; o Nobel segundo a análise dos arquivos
substituir(11, "gancho", "Em 1909, descreveu parasita, inseto transmissor, hospedeiros e sintomas",
    "A partir de 1909, descreveu parasita, inseto vetor, hospedeiros e sintomas")
substituir(11, "explicacao", "em homenagem ao amigo.", "em homenagem ao seu mentor, Oswaldo Cruz.")
substituir(11, "explicacao", "Descrever de uma vez uma doença desconhecida,", "Ter descrito em detalhe uma doença desconhecida,")
substituir(11, "explicacao",
    "Uma explicação possível é a forte oposição que enfrentou no Brasil, onde houve quem chegasse a duvidar da "
    "existência da doença.",
    "Muitos atribuem isso à oposição que ele sofreu no Brasil, onde houve quem duvidasse da existência da doença. "
    "A análise dos arquivos do Nobel, porém, aponta outros motivos: a cada vez ele teve um único indicador, "
    "brasileiro, e o comitê se ligava quase só a cientistas da Europa e dos EUA.")
acrescentar_trecho(11, 0,
    "He was nominated for the Nobel Prize each time by only a single Brazilian nominator. [...] "
    "Analysis of the database of the Nobel Prize archives, with the revelation of the names of nominators, nominees, and prizewinners from 1901 to 1951 [...] "
    "The connections of the members of the Nobel Committee with the international scientific community, almost exclusively centered in European and North American scientists, also influenced their choices. "
    "The nonrecognition of Carlos Chagas' discoveries by the Nobel Committee appears to be more correctly explained by these factors than by the negative impact of the local opposition. [...] "
    "After the death of his mentor in 1917, Chagas accepted Cruz's directorship of the institute")

# 0012: o estudo de 2015 (baby boom) e confiança consenso_parcial
trocar(12, confianca="consenso_parcial")
substituir(12, "explicacao",
    "A epidemia americana de 1952, a pior da história do país, teve 57.628 casos e 3.145 mortes, e ajudou a "
    "voltar a atenção do público para a necessidade de uma vacina.",
    "Mas a explicação tem limites: um estudo de 2015, com dados dos EUA de meados do século XX, concluiu que o "
    "avanço da pólio nessas décadas se explica melhor pelo baby boom, que multiplicou as crianças suscetíveis, "
    "do que pela higiene. Os autores admitem, porém, que a higiene pode ter pesado no surgimento das epidemias, "
    "por volta de 1900.")
CANDIDATOS[11]["fontes"].append({
    "url": "https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002172",
    "titulo": "Unraveling the Transmission Ecology of Polio (Martinez-Bakker, King e Rohani, PLoS Biology, 2015)",
    "idioma": "en",
    "trecho": (
        "We analyzed an extensive epidemiological dataset, spanning the 1930s to the 1950s and spatially replicated across each state in the United States, to glean insight into the drivers of polio’s historical expansion [...] "
        "contrary to the prevailing “disease of development” hypothesis, our analyses demonstrate that polio’s historical expansion was straightforwardly explained by demographic trends rather than improvements in sanitation and hygiene [...] "
        "Our analyses show that the historical expansion of polio is straightforwardly explained by the demographic “baby boom” during the postwar period rather than improvements in hygiene. [...] "
        "Our results suggest the marked increase in polio incidence from the 1930s to the 1950s was a straightforward consequence of increased birth rates [...] "
        "changes in hygiene and sanitation could have contributed to the initial emergence of polio, which occurred from the late 1800s to the early 20th century."
    ),
})

# 0014: guia (não motorista), colega de enfermagem, medo da injeção
substituir(14, "explicacao", "guiou um carro que levava duas crianças com varíola",
    "foi como guia no carro que levava duas crianças com varíola")
substituir(14, "explicacao", "até que uma colega o denunciou.", "até que um colega da enfermagem o denunciou.")
substituir(14, "explicacao", "contou que fugiu dela porque a agulhada parecia doer.",
    "contou que não se vacinou por medo, porque a injeção parecia doer.")

# 0015: só parte dos tatus; origem europeia como suspeita
substituir(15, "gancho", "Tatus do sul dos EUA carregam a bactéria da hanseníase e podem passá-la a pessoas.",
    "Parte dos tatus do sul dos EUA carrega a bactéria da hanseníase e pode passá-la a pessoas.")
substituir(15, "gancho", "provavelmente dos primeiros europeus nas Américas.",
    "e a suspeita recai sobre os primeiros europeus nas Américas.")

# 0016: a falta de prova vale para as vítimas da repressão em geral, não para os deportados
substituir(16, "explicacao",
    "A repressão deixou 945 presos na Ilha das Cobras, 30 mortos, 110 feridos e 461 deportados para o Acre, "
    "muitos deles sem prova de que tivessem participado.",
    "A repressão deixou 945 presos na Ilha das Cobras, 30 mortos, 110 feridos e 461 deportados para o Acre, e "
    "atingiu sobretudo os mais pobres, cuja participação nem sempre foi comprovada.")

# ganchos que passaram de 220 caracteres depois das correções
trocar(7, gancho="A segunda doença erradicada pela humanidade não era de gente: a peste bovina, declarada erradicada em 2011. "
    "Nos anos 1890, matou até 90% do gado do leste e do sul da África, e a fome pode ter levado um terço da Etiópia.")
substituir(15, "gancho", "Pela genética, eles a pegaram", "Pelo DNA, eles a pegaram")
acrescentar_trecho(12, 1, "Martinez-Bakker M, King AA, Rohani P (2015) Unraveling the Transmission Ecology of Polio.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(12, "gancho", "As grandes epidemias de paralisia infantil surgiram", "As epidemias de paralisia infantil surgiram")
