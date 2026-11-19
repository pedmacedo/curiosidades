"""Rodada 2 de Especiarias: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-especiarias-01.py"))
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


# 0002: castóreo vem das bolsas de castor (não são glândulas verdadeiras); sem comparar 1,2 milhão de kg com 12 mil t
substituir(2, "explicacao",
    "Já o castóreo, secreção de glândulas do castor, chegou a ser usado em substitutos de baunilha, mas hoje a "
    "indústria consome só uns 100 kg por ano, contra mais de 1,2 milhão de kg de vanilina.",
    "Já o castóreo, secreção das bolsas que o castor tem perto da base da cauda, chegou a ser usado em "
    "substitutos de baunilha, mas hoje a indústria consome só uns 100 kg dele por ano, uma gota perto das "
    "milhares de toneladas de vanilina.")
acrescentar_trecho(2, 2,
    "Castoreum  is a yellowish exudate from the castor sacs of mature beavers used in combination with urine to scent mark their territory. "
    "Both beaver sexes have a pair of castor sacs and a pair of anal glands, located in two cavities under the skin between the pelvis and the base of the tail. "
    "The castor sacs are not true glands (endocrine or exocrine) on a cellular level")

# 0003: "açafrão" também nomeia a cúrcuma
substituir(3, "gancho", "A planta do açafrão não é encontrada", "O açafrão verdadeiro não é encontrado")
substituir(3, "explicacao",
    "uma planta desconhecida em estado "
    "selvagem. ",
    "uma planta desconhecida em estado "
    "selvagem. Não deve ser confundido com a cúrcuma, também chamada de açafrão-da-terra, que é outra planta "
    "e ganhou o nome por tingir a comida de amarelo, como o açafrão. ")
CANDIDATOS[2]["fontes"].append(wiki("Cúrcuma",
    "Não deve ser confundido com a especiaria extraída das flores de Crocus sativus, comummente conhecida como açafrão. [...] "
    "açafrão-da-índia (também grafada açafrão-das-índias) açafrão-da-terra e turmérico. [...] "
    "provêm, por um lado, das propriedades da raiz desta planta que, tal como o açafrão comum (Crocus sativus), tinge a comida de tons amarelados.",
    nome="Cúrcuma", idioma="pt"))

# 0004: Nuremberg primeiro; a Guerra do Açafrão como relato tradicional
trocar(4, confianca="consenso_parcial",
    gancho="Na Idade Média, Nuremberg chegou a executar quem vendia açafrão adulterado. E, segundo relatos tradicionais, "
           "o roubo de uma carga do tempero por nobres desencadeou uma \"Guerra do Açafrão\" de 14 semanas.")
substituir(4, "explicacao",
    "o episódio desencadeou a chamada Guerra do "
    "Açafrão, que durou 14 semanas.",
    "o episódio teria desencadeado a chamada Guerra do "
    "Açafrão, que, segundo os relatos, durou 14 semanas.")

# 0007: "primeira menção" restrita ao mundo mediterrâneo
substituir(7, "explicacao",
    "A primeira "
    "menção de que a especiaria crescia na região da Índia",
    "Nos textos que circulavam no mundo mediterrâneo, a primeira "
    "menção de que a especiaria crescia na região da Índia")

# 0008: ingestão diária tolerável, não "limite recomendado"
substituir(8, "gancho", "pode passar do limite diário recomendado para uma pessoa pequena",
    "pode passar da ingestão diária tolerável para uma pessoa de pouco peso")

# 0010: o "até 90%" como relato; a data de 2012 com cautela
trocar(10, confianca="consenso_parcial",
    gancho="O remédio contra a gripe Tamiflu nasceu de uma molécula tirada do anis-estrelado. Segundo relatos muito "
           "citados, a fabricante chegou a usar até 90% da safra mundial do tempero.")
substituir(10, "explicacao",
    "e a Roche chegou a consumir até 90% da safra anual de anis-estrelado do mundo para "
    "fazer o medicamento.",
    "e, segundo relatos muito citados, a Roche chegou a consumir até 90% da safra anual de anis-estrelado do "
    "mundo para fazer o medicamento.")
substituir(10, "explicacao",
    "Em 2012, a Roche trocou o tempero por E. coli geneticamente "
    "modificada.",
    "Por volta de 2012, a Roche teria deixado o tempero de lado e passado a usar E. coli geneticamente "
    "modificada.")

# 0014: a água fria importa porque o calor desativa a enzima; o vinagre só reduz a atividade
substituir(14, "gancho", "Por isso a mostarda forte é feita com água fria, e não quente.",
    "Como o calor desativa a enzima, a mostarda forte é feita com água fria, e não quente.")
substituir(14, "explicacao",
    "Líquidos quentes e ácidos fortes, como o vinagre, desnaturam a "
    "enzima e deixam o condimento mais suave.",
    "Líquidos quentes desnaturam a enzima, e ácidos como o vinagre reduzem sua atividade, o que deixa o "
    "condimento mais suave.")
acrescentar_trecho(14, 1,
    "The traditional addition of vinegar reduces the pH, causing a mild reduction in myrosinase activity, "
    "thereby moderating the rate of production of the pungent isothiocyanate compounds.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(8, "explicacao", "Pelas contas do instituto alemão de avaliação de riscos, uma colher de chá de cássia em pó tem",
    "Partindo dos teores medidos pelo instituto alemão de avaliação de riscos, uma colher de chá de cássia em pó teria")
