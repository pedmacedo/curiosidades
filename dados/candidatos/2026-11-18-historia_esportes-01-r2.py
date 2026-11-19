"""Rodada 2 de História dos esportes: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-historia_esportes-01.py"))
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


# 0004: aluno de Naismith; badminton; homens de meia-idade; o nome volleyball
trocar(4, gancho="O vôlei nasceu em 1895 com o nome de \"mintonette\", inventado por um ex-aluno do criador do basquete para homens de negócios de meia-idade que achavam o basquete puxado demais.")
substituir(4, "explicacao",
    "O basquete tinha sido inventado em 1891, também numa ACM de Massachusetts, em Springfield, cidade vizinha.",
    "Morgan tinha sido aluno de James Naismith, que inventara o basquete em 1891 em Springfield, também em "
    "Massachusetts. O nome \"mintonette\" vinha do badminton, de onde Morgan tirou a ideia, e o público eram "
    "os frequentadores da ACM, na maioria homens de negócios de meia-idade.")
substituir(4, "explicacao",
    "Mais tarde ganhou o nome de volleyball, de \"volley\", rebater a bola antes que ela toque o chão.",
    "Na primeira exibição, em 1896, um observador, Alfred Halstead, reparou que a bola era rebatida de um "
    "lado para o outro no ar, e o jogo logo passou a se chamar volleyball.")
acrescentar_trecho(4, 0, "Because he originally derived the game from badminton, he initially named the sport mintonette. "
    "He was a one-time student of basketball inventor James Naismith and invented the game for his clients at the YMCA, most of whom were middle-aged businessmen for whom the physical demands of basketball were too great. [...] "
    "After an observer, Alfred Halstead, noticed the volleying nature of the game at its first exhibition match in 1896, played at the International YMCA Training School (now called Springfield College), the game quickly became known as volleyball")

# 0008: a objeção ao relógio também é discutida; a teoria das apostas
trocar(8, tipos_espanto=["misterio_aberto", "conexao_inesperada"],
    gancho="Ninguém sabe ao certo por que o tênis conta 15, 30, 40. A teoria de um relógio usado como placar é a mais famosa, mas outra ganha força: as apostas medievais, feitas com moedas num sistema de base 60.")
substituir(8, "explicacao",
    "As primeiras teorias publicadas sobre a origem do 15 são de 1555 e 1579, "
    "mas a origem continua obscura.",
    "A origem continua obscura.")
substituir(8, "explicacao",
    "O problema é a cronologia: as primeiras referências são do século XV, quando os relógios mostravam só as "
    "horas. Os ponteiros de minutos só se tornaram comuns por volta de 1690, com o pêndulo mais preciso.",
    "Contra ela, costuma-se dizer que os ponteiros de minutos só se tornaram comuns por volta de 1690, com o "
    "pêndulo mais preciso. Mas essa objeção também é discutida: o relógio da Catedral de Wells, na Inglaterra, "
    "de 1386, já tinha um mostrador de 60 minutos e tocava a cada quarto de hora. Outra hipótese liga a "
    "contagem às apostas: na Idade Média, jogadores e espectadores apostavam no tênis, e o sistema monetário "
    "carolíngio, usado na Europa do século VIII ao XVIII, era de base 60, o que explicaria os quatro saltos de "
    "15 até 60.")
acrescentar_trecho(8, 0, "However, the clock at the Wells Cathedral in England, which dates from 1386, had an inner dial with 60 minutes and a minute indicator and chimed every quarter hour. [...] "
    "More plausibly, the use of base 60 for counting, accounting and games has been used in many societies for thousands of years, including the use of Sexagesimal for counting in the very earliest civilisations, and the Carolingian monetary system used widely in Europe between the 8th and 18th centuries. "
    "In medieval times, players and spectators regularly wagered on tennis, so alignment with the then prevailing money system is a likely cause of the game scoring system using 4 x 15 to achieve 60.")

# 0009: peso incerto; o látex e a trepadeira; 1528
trocar(9, tipos_espanto=["engenhosidade", "conexao_inesperada"],
    gancho="Há 3.600 anos ou mais, povos da Mesoamérica faziam bolas de borracha maciça misturando látex com seiva de uma trepadeira. Quando as viram quicar, em 1528, os europeus ficaram maravilhados.")
substituir(9, "explicacao", "A bola era de borracha natural maciça e podia pesar até 4,1 quilos.",
    "A bola era de borracha natural maciça. O peso exato das bolas de jogo é incerto, mas os pesquisadores "
    "estimam algo entre 1,4 e 2,7 quilos. A maioria era feita com o látex da árvore Castilla elastica: "
    "misturado à seiva da trepadeira Ipomoea alba, o látex escorregadio virava uma borracha resistente e "
    "elástica.")
substituir(9, "explicacao", "Depois da conquista, Hernán Cortés mandou um grupo de jogadores",
    "Em 1528, logo depois da conquista, Hernán Cortés mandou um grupo de jogadores")
substituir(9, "explicacao", "e os europeus ficaram impressionados com as bolas de borracha que quicavam.",
    "e, além do fascínio pelos visitantes, os europeus se maravilharam com as bolas de borracha que quicavam.")
substituir_trecho(9, 0, "The ball was made of solid natural rubber and weighed as much as 9 pounds (4.1 kg) [...] ",
    "The ball was made of solid natural rubber [...] ")
substituir_trecho(9, 0, "Cortés sent a troupe", "In 1528, soon after the Spanish conquest, Cortés sent a troupe")
acrescentar_trecho(9, 0, "The sizes or weights of the balls actually used in the ballgame are not known with any certainty. [...] "
    "Most balls were made from latex sap of the lowland Castilla elastica tree. "
    "Someone discovered that by mixing latex with sap from the vine of white tropical morning glory (Ipomoea alba), they could turn the slippery polymers in raw latex into a resilient rubber. "
    "The size varied between 10 and 12 in (25 and 30 cm) (measured in hand spans) and weighed 3 to 6 lb (1.4 to 2.7 kg).")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(8, "explicacao", "O 45 teria virado 40 para caber a regra do empate, o deuce, com saltos de 10.",
    "O 45 teria virado 40 para caber a regra do empate, o deuce.")
substituir(9, "gancho", "Quando as viram quicar, em 1528,", "Quando as viram quicar na Espanha, em 1528,")
substituir(9, "explicacao", "Na versão mais comum, os jogadores batiam", "Pela interpretação mais aceita, os jogadores batiam")
