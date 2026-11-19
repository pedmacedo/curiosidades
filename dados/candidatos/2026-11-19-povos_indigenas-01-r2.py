"""Rodada 2 de Povos indígenas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-povos_indigenas-01.py"))
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


# 0001: o número de falantes diverge entre fontes; não citar
substituir(1, "explicacao", "falada por cerca de 600 pessoas às margens do rio Nhamundá",
    "falada pelo povo de mesmo nome às margens do rio Nhamundá")

# 0002: regra tradicional, "costumam", e frase mais respeitosa sobre contar as línguas
trocar(2, gancho="Entre os Tukano, a regra tradicional proíbe o homem de se casar com uma mulher que fale a mesma língua "
    "que ele. Por isso, numa mesma casa costumam conviver várias línguas, e as crianças crescem multilíngues.")
substituir(2, "explicacao",
    "É tão natural que muitos nem sabem dizer de pronto quantas línguas falam: precisam ser estimulados a listá-las.",
    "Falar várias línguas é tão corriqueiro que nem chama atenção: muitas vezes a pessoa só chega ao número exato "
    "quando alguém pede que as liste uma a uma.")

# 0008: contagem de uma ONG; FUNAI tem números próprios; "estima"; tipo contraintuitivo
trocar(8, tipos_espanto=["mito_desmentido", "contraintuitivo"],
    gancho="Pela contagem de uma ONG em 2025, o Brasil abriga 124 dos 196 povos isolados do planeta. E eles não são "
           "\"tribos perdidas\": em geral sabem do mundo lá fora e evitam o contato.")
substituir(8, "explicacao", "e achou evidências sólidas de 196 povos isolados em dez países, 124 deles no Brasil.",
    "e diz ter achado evidências de 196 povos isolados em dez países, 124 deles no Brasil. A FUNAI tem contagens "
    "próprias: em 2007, registrava 67 povos isolados no país.")
substituir(8, "explicacao", "O mesmo relatório prevê que quase metade", "O mesmo relatório estima que quase metade")
acrescentar_trecho(8, 0, "In 2007, FUNAI reported the presence of 67 uncontacted Indigenous peoples in Brazil, up from 40 in 2005.")

# 0009: em 2015 voltou o primeiro lote (Penn State); cinco instituições aceitaram devolver
trocar(9, gancho="Em 1967, cientistas americanos colheram sangue de Yanomami no Brasil. A tradição deles proíbe guardar "
    "partes do corpo de quem morreu, e só em 2015 as primeiras 2.693 amostras voltaram para ser enterradas.")
substituir(9, "explicacao",
    "a Universidade Estadual da Pensilvânia devolveu 2.693 amostras de sangue processado e DNA purificado.",
    "a Universidade Estadual da Pensilvânia devolveu todas as que guardava: 2.693 amostras de sangue processado e "
    "DNA purificado. Foi o primeiro lote, porque ao todo cinco instituições americanas aceitaram devolver o material.")
acrescentar_trecho(9, 0, "Todas as amostras que estavam em posse da Universidade da Pennsylvania foram devolvidas. [...] "
    "cinco instituições norte-americanas concordaram em devolver as amostras de sangue que possuíam e começaram negociações com autoridades brasileiras.")

# 0010: sem o número de línguas oficiais de São Gabriel
substituir(10, "explicacao",
    "virou língua oficial, ao lado do português, em São Gabriel da Cachoeira, no Amazonas, que hoje tem quatro línguas oficiais.",
    "virou língua cooficial, ao lado do português, em São Gabriel da Cachoeira, no Amazonas.")
substituir_trecho(10, 0, "Now Nheengatu is one of the four official languages of the municipality. [...] ", "[...] ")

# 0011: atribuir o "único do Nordeste" ao ISA; sertão; fora de Águas Belas; tipo historia_humana
trocar(11, tipos_espanto=["contraintuitivo", "historia_humana"],
    gancho="Segundo o Instituto Socioambiental, os Fulni-ô, de Pernambuco, são o único povo do Nordeste que manteve "
           "viva a própria língua, o iatê. Todo ano passam semanas no Ouricuri, um ritual sobre o qual não falam.")
substituir(11, "explicacao", "no agreste pernambucano", "no sertão pernambucano")
substituir(11, "explicacao", "Quem trabalha na cidade pede licença para ir.", "Quem trabalha fora de Águas Belas pede licença para ir.")
acrescentar_trecho(11, 0, "Os Fulni-ô atualmente habitam o município de Águas Belas, situado na zona fisiográfica do Sertão, a 273 quilômetros da capital do estado de Pernambuco.")

# 0012: sem reproduzir a visão jesuíta como fato; "registrou"; divindade secundária
substituir(12, "gancho", "protestou:", "registrou:")
substituir(12, "explicacao",
    "os jesuítas procuravam entre os indígenas algo parecido com a religião europeia e não acharam.",
    "os jesuítas esperavam encontrar entre os indígenas formas religiosas parecidas com as europeias e, "
    "decepcionados, diziam que eles não adoravam deus algum.")
substituir(12, "explicacao", "Como não havia palavra melhor, a solução foi",
    "Como, para ele, não havia palavra mais conveniente, a solução foi")
substituir(12, "explicacao", "Nem todos concordavam.", "Os cronistas da época divergiam.")
substituir(12, "explicacao", "O certo é que o uso de Tupã",
    "Na teogonia mbyá-guarani, Tupã ocupa o quinto lugar: é uma divindade, mas não o deus supremo. "
    "O certo é que o uso de Tupã")
acrescentar_trecho(12, 0, "daí a decepção com que afirmavam: \"os índios não conhecem ou adoram nenhum deus.\" [...] "
    "O fato de Tupã ocupar o quinto lugar na teogonia mbyá-guarani e posições ainda mais secundárias na de outros grupos guaranis [...] "
    "Sabe-se que Tupã não é o deus supremo, mas uma deidade secundária")

# 0013: outros fatores do aumento e o mecanismo das grandes cidades
substituir(13, "explicacao",
    "e o IBGE atribui o aumento sobretudo à maior disposição das pessoas de se identificar com suas origens.",
    "e o IBGE atribui o aumento, em boa parte, à maior disposição das pessoas de se identificar com suas origens, "
    "além de migrações recentes (como a de indígenas venezuelanos) e de melhorias na coleta dos dados.")
substituir(13, "explicacao", "não o tamanho da população.",
    "não o tamanho da população. O IBGE aponta as migrações e a urbanização entre os fatores por trás desses "
    "números, e algumas cidades viraram polos de atração da população indígena.")
acrescentar_trecho(13, 0, "como os movimentos migratórios, o processo de urbanização, os processos de autoafirmação e reemergência étnica [...] "
    "outros fatores que contribuem para um aumento no número de etnias, como processos de desagregação de subgrupos que passaram a se identificar como etnias distintas, migrações recentes, como a de indígenas venezuelanos e consolidadas, e melhorias na captação e validação dos dados realizadas pelo IBGE durante o Censo 2022. [...] "
    "Campinas, Foz do Iguaçu e cidades do Mato Grosso do Sul passaram a ser polos de atração da população indígena.")
