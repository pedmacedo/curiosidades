"""Rodada 2 de Américas pré-colombianas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-23-americas_pre_colombianas-01.py"))
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


# 0002: espaçamento dos postos e extensão da rede são estimativas disputadas
trocar(2, nota_surpresa=3)
substituir(2, "gancho", "com postos a cada 2,5 km", "com postos a poucos quilômetros uns dos outros")
substituir(2, "explicacao", "a uns 2,5 km uns dos outros,",
    "a cerca de 2,5 km uns dos outros, segundo vários cronistas (outros relatos e estudos modernos falam em "
    "distâncias maiores),")
substituir(2, "explicacao", "somava cerca de 40.000 km",
    "somava dezenas de milhares de quilômetros (uma estimativa comum fala em 40.000 km)")
acrescentar_trecho(2, 1,
    "The exact extent of the road network is not known: travelers and scholars proposed various lengths, spanning from 23,000 kilometres (14,000 mi) to 40,000 kilometres (25,000 mi) to 60,000 kilometres (37,000 mi).")
acrescentar_trecho(2, 0, "other chroniclers report distances of half a league or 2.5 kilometres (1.6 mi).")

# 0004: a comparação com Londres depende das estimativas altas; a construção no topo
substituir(4, "explicacao", "era coroado por uma grande construção de madeira de mais 15 m.",
    "era coroado por uma grande construção com mais 15 m de altura.")
substituir(4, "explicacao", "quando Filadélfia passou dos 40.000.",
    "quando Filadélfia passou dos 40.000. A comparação com a Londres do século XII, que a própria literatura faz "
    "com um \"talvez\", só se sustenta pelas estimativas mais altas; pelas mais baixas, Cahokia seria menor.")

# 0005: houve sacrifícios rituais com mutilação; arte visual "quase" nenhuma
substituir(5, "gancho", "nem muralhas, nem armas, nem corpos mutilados.", "nem muralhas, nem armas.")
substituir(5, "explicacao", "e dela não sobrou nenhuma arte visual", "e dela quase não sobrou arte visual")
substituir(5, "explicacao", "os povoados não tinham defesas.",
    "os povoados não tinham defesas. Isso não quer dizer ausência de violência: há indícios de sacrifícios "
    "humanos rituais na região.")
acrescentar_trecho(5, 0,
    "There, remains of human sacrifices (two children and a newborn) have been found. [...] "
    "One such skeleton represents the earliest known evidence of human sacrifice in the Andean region, dating to around 3000 BC.")

# 0006: os números dos Andes e da Guerra Civil não foram medidos do mesmo jeito
substituir(6, "explicacao", "sem ela, assumiram que o paciente morreu na cirurgia ou poucos dias depois.",
    "sem ela, assumiram que o paciente morreu na cirurgia ou poucos dias depois. Por isso, os números dos Andes e "
    "os da Guerra Civil não foram medidos do mesmo jeito, e a comparação, feita pelos próprios autores, é "
    "aproximada.")

# 0008: o superlativo foi contestado por um estudo de 2025 (corpos defumados na Ásia)
trocar(8, gancho="Entre as múmias feitas de propósito mais antigas do mundo estão as do povo chinchorro, no deserto do "
    "Atacama, no Chile, desde cerca de 5050 a.C. E não só da elite: crianças também.")
substituir(8, "explicacao", "o exemplo mais antigo é uma criança enterrada no vale de Camarones.",
    "o exemplo mais antigo é uma criança enterrada no vale de Camarones. Por décadas, foram tidas como as múmias "
    "artificiais mais antigas do mundo. Em 2025, um estudo na PNAS, de arqueólogos da Universidade Nacional da "
    "Austrália, propôs que corpos secos lentamente na fumaça de fogueiras no sul da China e no Sudeste Asiático, "
    "entre 12 mil e 4 mil anos atrás, seriam ainda mais antigos.")
substituir(8, "explicacao", " Em 2021, os sítios chinchorro viraram Patrimônio Mundial da UNESCO.", "")
CANDIDATOS[7]["fontes"].append(
    {"url": "https://revistapesquisa.fapesp.br/en/worlds-oldest-mummies-found-in-asia/",
     "titulo": "World’s oldest mummies found in Asia (Revista Pesquisa FAPESP, 2025)",
     "idioma": "en",
     "trecho": (
         "World’s oldest mummies found in Asia [...] "
         "HUNG, H.-C. et al. PNAS. 2025 [...] "
         "After examining the remains of 54 human bodies, archaeologists from the Australian National University identified human mummies in Southeast Asia [...] "
         "Between 12,000 and 4,000 years ago, hunter-gatherers in southern China, Southeast Asia, and nearby islands—including Borneo and Java—bound their dead in squatting positions and slowly dried them over smoldering, low-temperature fires for several months before burial. "
         "Lengthy exposure to smoke mummified the skin of the corpses"
     )})

# 0011: sem mistério aberto; datas e "perdeu-se no México"; a receita de 1993 reconstitui o processo
trocar(11, tipos_espanto=["engenhosidade", "conexao_inesperada"])
substituir(11, "explicacao", "A composição só foi descoberta nos anos 1950, por difração em pó.",
    "A composição foi desvendada no século XX, com análises de difração.")
substituir(11, "explicacao", "mas a técnica se perdeu.", "mas depois a técnica se perdeu no México.")
substituir(11, "explicacao",
    "Uma receita para reproduzi-lo só foi publicada em 1993, pelo historiador e químico mexicano Constantino "
    "Reyes-Valerio, que juntou a leitura de crônicas antigas com análises microscópicas e espectroscopia das "
    "pinturas.",
    "Em 1993, o historiador e químico mexicano Constantino Reyes-Valerio publicou uma receita que reconstitui o "
    "processo antigo, juntando a leitura de crônicas antigas com análises microscópicas e espectroscopia das "
    "pinturas.")

# 0014: Humboldt popularizou o termo (Clavijero já o usava)
substituir(14, "gancho", "O uso moderno do termo vem de Humboldt, em 1810.", "O termo foi popularizado por Humboldt, em 1810.")
substituir(14, "explicacao", "quem, em 1810, deu origem ao uso moderno de \"asteca\" como nome coletivo",
    "quem, em 1810, popularizou \"asteca\" como nome coletivo")

# 0015: as sete colheitas são estimativa; o título da ONU por extenso
substituir(15, "gancho", "davam até sete colheitas por ano", "podiam dar até sete colheitas por ano")
substituir(15, "explicacao", "a produtividade era altíssima: até sete colheitas por ano",
    "a produtividade era altíssima: segundo algumas estimativas, até sete colheitas por ano")
substituir(15, "explicacao", "receberam da ONU em 2018 o título de patrimônio agrícola mundial",
    "foram reconhecidas pela ONU, em 2018, como Sistema Importante do Patrimônio Agrícola Mundial")
substituir(2, "gancho", "Sem usar a roda, o Império Inca", "Sem roda, o Império Inca")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(2, "explicacao", "outros relatos e estudos modernos falam em distâncias maiores", "outros relatos e estudos modernos falam em distâncias diferentes")
substituir(4, "explicacao", "morava ali umas mil pessoas", "moravam ali umas mil pessoas")
substituir(4, "explicacao", "era coroado por uma grande construção com mais 15 m de altura", "era coroado por uma grande construção que acrescentava outros 15 m de altura")
substituir(5, "explicacao", "Isso contraria a teoria de que os primeiros Estados", "A ausência de guerra contraria a teoria de que os primeiros Estados")
substituir(8, "explicacao", "entre 12 mil e 4 mil anos atrás, seriam ainda mais antigos.", "entre 12 mil e 4 mil anos atrás, teriam exemplares ainda mais antigos.")
substituir(11, "explicacao", "Aparece por volta do ano 800 e foi usado em murais, cerâmicas, esculturas e códices.", "Foi usado em murais, cerâmicas, esculturas e códices.")
