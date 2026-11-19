"""Rodada 2 de Brasil Império: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-brasil_imperio-01.py"))
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


# 0001: Pedro ficou sitiado no Porto; quem tomou Lisboa foi uma expedição enviada ao sul
substituir(1, "explicacao", "montou um pequeno exército e marchou até Lisboa, que se rendeu.",
    "montou um pequeno exército, entrou no Porto e lá ficou sitiado por mais de um ano, até que parte das "
    "tropas, enviada por mar ao sul, marchou até Lisboa, que se rendeu.")
acrescentar_trecho(1, 1, "entering the city of Porto unopposed on 9 July. "
    "His brother's troops moved to encircle the city, beginning a siege that lasted for more than a year. [...] "
    "His cause was nearly lost until he took the risky step of dividing his forces and sending a portion to launch an amphibious attack on southern Portugal. "
    "The Algarve region fell to the expedition, which then marched north straight for Lisbon, which capitulated on 24 July.")

# 0002: sem "desde 1822"
substituir(2, "explicacao",
    "Desde 1822, o hino usado no país era o que o próprio Pedro I compusera",
    "Até então, o hino usado no país era o que o próprio Pedro I compusera")

# 0003: o aborto foi em 2 de dezembro, dias antes da morte
substituir(3, "explicacao",
    "morreu no Rio em 11 de dezembro de 1826, na 12ª semana de gravidez, depois de convulsões, febre alta e delírios.",
    "morreu no Rio em 11 de dezembro de 1826, com convulsões, febre alta e delírios, dias depois de perder o "
    "bebê: estava na 12ª semana de gravidez quando adoeceu.")
acrescentar_trecho(3, 0, "medical records indicated the Empress miscarried a male fetus of about three-months-old of gestation on 2 December, days before her death.")

# 0006: Kossoy não pesquisou "mais de 150 anos" depois
substituir(6, "explicacao",
    "Mais de 150 anos mais tarde, o pesquisador Boris Kossoy examinou seus manuscritos",
    "Bem mais tarde, o pesquisador Boris Kossoy examinou seus manuscritos")
substituir_trecho(6, 0, "Mais de 150 anos depois, o exame detalhado", "o exame detalhado")
trocar(6, nota_surpresa=4)

# 0008: corta os 100 mil de 1910; o nome do abadá no Carnaval veio pela capoeira
trocar(8, gancho="Em 1835, no Ramadã, muçulmanos africanos escravizados e libertos se rebelaram em Salvador. "
    "Muitos escreviam em árabe, e a bata branca que vestiram, o abadá, é a palavra que hoje batiza a camisa do Carnaval.")
substituir(8, "explicacao",
    "Leis mais duras vieram em seguida, mas ainda em 1910 haveria cerca de 100 mil muçulmanos africanos no Brasil.",
    "Leis mais duras vieram em seguida, junto com esforços para forçar conversões ao catolicismo e apagar a "
    "memória do islã.")
substituir(8, "explicacao",
    "e, desde o Carnaval de 1993, a fantasia dos blocos de Carnaval.",
    "e, desde o Carnaval de 1993, quando um designer a escolheu em homenagem a um mestre capoeirista, a "
    "fantasia dos blocos.")
substituir_trecho(8, 0,
    "However, the African Muslim community was not erased overnight, and as late as 1910 it is estimated there were still some 100,000 African Muslims living in Brazil.",
    "In subsequent years intensive efforts were made to force conversions to Catholicism and erase the popular memory and affection towards Islam.")

# 0009: a fonte não diz que aprendeu a ler a bordo; gancho mais preciso
trocar(9, gancho="Em 1881, os jangadeiros de Fortaleza fizeram greve: recusaram-se a levar escravizados até os navios "
    "que os levariam para ser vendidos no Sul. Em 1884, o Ceará aboliu a escravidão, quatro anos antes do resto do Brasil.")
substituir(9, "explicacao",
    " e aprendeu a ler e escrever a bordo de um veleiro.",
    ", aprendeu a ler e escrever e trabalhou até os 20 anos no veleiro do comandante.")

# 0012: cemitério e igrejas não foram os primeiros; número incerto
substituir(12, "gancho", "Fundaram a cidade de Americana, em São Paulo.", "Deram origem à cidade de Americana, em São Paulo.")
substituir(12, "explicacao",
    "e criaram o Cemitério do Campo, o primeiro cemitério não católico e não indígena do Brasil.",
    "e criaram o próprio cemitério, o Cemitério do Campo, em Santa Bárbara d'Oeste.")
substituir(12, "explicacao",
    "lampiões de querosene e as primeiras igrejas batista, presbiteriana e metodista.",
    "lampiões de querosene, além de igrejas batista, presbiteriana e metodista.")
substituir(12, "explicacao",
    "Estima-se que até 20 mil confederados tenham imigrado.",
    "O número exato é desconhecido; as estimativas chegam a 20 mil imigrantes.")
substituir_trecho(12, 0,
    "so they created their own cemetery, the first non-Catholic, non-indigenous cemetery in Brazil.",
    "so they created their own cemetery")
acrescentar_trecho(12, 0, "The center of Confederado culture is the Campo Cemetery in Santa Bárbara d'Oeste [...] "
    "It is not known how many Confederado immigrants came to Brazil, but unprecedented research in the records of the port of Rio de Janeiro, by Betty Antunes de Oliveira, shows that around 20,000 U.S. citizens entered Brazil between 1865 and 1885.")

# 0007: melhoria opcional do verificador
substituir(7, "explicacao", "Cerca de 300 mil pessoas acompanharam o cortejo sob chuva e frio.",
    "Cerca de 300 mil pessoas se aglomeraram ao longo do trajeto, sob chuva e frio.")
