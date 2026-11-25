"""Rodada 2 de Europa medieval: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-europa_medieval-01.py"))
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


# 0001 e 0002: reprovados (ficam como estão; o orquestrador descarta)

# 0003: sem o "68 anos" (erro de digitalização da fonte); "entre outras"; tipo contraintuitivo
substituir(3, "explicacao",
    "Quem tivesse corpo capaz, menos de 68 anos e nada de que viver era obrigado a servir a quem o chamasse, sob pena de prisão.",
    "Quem tivesse corpo capaz e nada de que viver era obrigado a servir a quem o chamasse, sob pena de prisão.")
substituir_trecho(3, 0, "That every person, able in body and under the age of 68 years, not having enough to live upon,",
    "That every person, able in body [...] not having enough to live upon,")
substituir(3, "explicacao", "O estatuto foi uma das causas da Revolta dos Camponeses de 1381.",
    "O estatuto foi uma das causas, entre outras, da Revolta dos Camponeses de 1381.")
trocar(3, tipos_espanto=["historia_humana", "contraintuitivo"], nota_surpresa=3)

# 0004: uma erupção em 539–540; a peste acompanhou, não foi consequência do clima
substituir(4, "explicacao", "Novas erupções, em 539 e 540, esfriaram o verão europeu em até 2,7 °C.",
    "Uma nova erupção, em 539–540, esfriou o verão europeu em até 2,7 °C.")
substituir(4, "explicacao",
    "Vieram quebras de safra, fome e a Peste de Justiniano, com milhões de mortes, e começou um período frio que durou de 536 a 660.",
    "As erupções provocaram quebras de safra, e a época também teve fome, a Peste de Justiniano e milhões de mortes; "
    "começou ali um período frio que durou de 536 a 660.")

# 0005: técnicas de Guédelon ajudaram (não fizeram) a reconstrução da Notre-Dame
substituir(5, "gancho",
    "O que se reaprendeu nessa obra foi usado para reconstruir a Notre-Dame de Paris após o incêndio de 2019.",
    "Técnicas reaprendidas nessa obra ajudaram na reconstrução da Notre-Dame de Paris após o incêndio de 2019.")
substituir(5, "explicacao", "Em 2014, o canteiro recebia",
    "Técnicas redesenvolvidas em Guédelon foram aproveitadas na reconstrução da Notre-Dame de Paris, depois do "
    "incêndio de 2019. Em 2014, o canteiro recebia")

# 0008: Frederico II duvidou; sem "só no fim do século XIX"
substituir(8, "gancho", "para examinar e concluiu que era lenda.",
    "para examinar e não viu nelas nada parecido com uma ave.")
substituir(8, "explicacao",
    "Só no fim do século XIX se mostrou que eles migram para se reproduzir na Groenlândia ou no norte da Escandinávia.",
    "Hoje se sabe que esses gansos migram para se reproduzir no extremo norte, como na Groenlândia e no norte da Escandinávia.")

# 0009: Banco da Inglaterra já existia em 1697; "a maior parte do prédio"
substituir(9, "explicacao",
    "Em 1697, ajudaram a formar o Banco da Inglaterra, que trocou ações por varetas da dívida da Coroa.",
    "Em 1697, o recém-criado Banco da Inglaterra emitiu ações em troca de varetas da dívida da Coroa.")
substituir(9, "gancho", "destruiu quase todo o prédio", "destruiu a maior parte do prédio")

# 0012: sem o 64; a medida robusta é morte média entre 50 e 60 para quem passava dos 20 e poucos
trocar(12, nota_surpresa=3,
    gancho="Expectativa de vida de uns 30 anos na Idade Média não significa que adultos morriam aos 30: as mortes de "
           "bebês puxavam a média para baixo, e quem passava dos 20 e poucos anos chegava, em média, à casa dos 50.")
substituir(12, "explicacao",
    "No caso medieval, a conta para quem já era adulto era bem maior, como mostra o exemplo do homem inglês de 21 anos.",
    "Na Inglaterra, estimativas para os séculos XIII a XIX indicam que quem passava dos 20 e poucos anos morria, em "
    "média, entre os 50 e os 60 anos.")
acrescentar_trecho(12, 1,
    "In England in the 13th–19th centuries with life expectancy at birth rising from perhaps 25 years to over 40, "
    "expectation of life at age 30 has been estimated at 20–30 years, giving an average age at death of about 50–60 "
    "for those (a minority at the start of the period but two-thirds at its end) surviving beyond their twenties.")

# 0013: "não têm prova medieval"; donzela surge no fim do século XVIII; nova fonte
trocar(13, nota_surpresa=3,
    gancho="Dois símbolos da \"Idade Média cruel\" não têm prova medieval: a donzela de ferro surge só no fim do século "
           "XVIII, e muitos cintos de castidade de museus são tidos como falsificações do século XIX.")
substituir(13, "explicacao", "com uma suposta execução de um falsificador de moedas em 1515.",
    "com uma suposta execução de um falsificador de moedas em 1515 (Siebenkees morreu em 1796).")
CANDIDATOS[12]["fontes"].append(wiki("List_of_common_misconceptions_about_history",
    "There is no evidence that iron maidens were used for torture, or even yet invented, in the Middle Ages. "
    "Instead they were pieced together in the 18th century from several artifacts found in museums, arsenals and the "
    "like to create spectacular objects intended for commercial exhibition.",
    nome="List of common misconceptions about history"))

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(8, "explicacao", "nasciam em madeira de pinheiro à deriva", "nasciam em madeira de abeto à deriva")
substituir(12, "gancho", "e quem passava dos 20 e poucos anos chegava, em média, à casa dos 50.", "e quem chegava aos 30 morria, em média, entre os 50 e os 60.")
substituir(12, "explicacao", "quem passava dos 20 e poucos anos morria", "quem chegava aos 30 anos morria")
