"""Rodada 2 de Jogos de tabuleiro: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-jogos_tabuleiro-01.py"))
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


# 0001: a falta de regras se refere à redescoberta moderna, não a "milênios"
substituir(1, "explicacao", "Por milênios, ninguém soube como jogar.",
    "Quando os tabuleiros foram redescobertos, ninguém sabia como jogar.")
substituir(1, "explicacao", "nas estátuas de touros alados do palácio de Sargão II",
    "nas estátuas de touros alados com cabeça humana do palácio de Sargão II")

# 0004: a fonte só diz que o MI9 procurou a EMI; "vinil" é anacrônico
substituir(4, "explicacao", "O MI9 também escondeu mapas em discos de vinil.",
    "O MI9 também procurou a gravadora EMI para esconder mapas laminados dentro de discos de gramofone.")

# 0005: "pontos de vida" como equivalente, sem anacronismo
trocar(5, gancho="Um jogo de guerra prussiano de 1824 já tinha o equivalente aos \"pontos de vida\" dos games: as tropas "
    "sofriam perdas parciais sem sair do mapa. Era o Kriegsspiel, e o rei mandou dar um a cada regimento.")

# 0006: a restrição à promoção não foi reação à regra nova
substituir(6, "explicacao",
    "Houve reação: em certas épocas, proibia-se promover um peão a dama enquanto a original estivesse no "
    "tabuleiro, para não dar ao rei mais de uma rainha.",
    "As regras novas enfrentaram resistência. E, em várias épocas, chegou-se a restringir a promoção de um peão "
    "a dama enquanto a original estivesse no tabuleiro, para não dar ao rei mais de uma rainha.")

# 0008: "tido como o maior"; Schaeffer tirou o Chinook das competições em 1995
substituir(8, "gancho", "O maior campeão da história, Marion Tinsley,", "Tido como o maior de todos, Marion Tinsley,")
substituir(8, "explicacao", "Schaeffer então parou de competir e foi tentar resolver o jogo.",
    "Em 1995, depois de defender o título contra outro humano, Schaeffer tirou o Chinook das competições e foi "
    "tentar resolver o jogo.")
acrescentar_trecho(8, 1, "In 1995, Chinook defended its man-machine title against Don Lafferty in a 32-game match.")

# 0012: efeito sobre Kasparov é versão de Campbell; relatos divergem sobre a partida; "criatividade" = suspeita de intervenção
substituir(12, "gancho", "um lance estranho do Deep Blue fez Kasparov ver nele",
    "um lance estranho do Deep Blue teria feito Kasparov ver nele")
substituir(12, "explicacao", "Quinze anos depois, a história veio a público no livro",
    "Quinze anos depois, a história ganhou fama com o livro")
substituir(12, "explicacao",
    "No fim, o Deep Blue venceu o match, e Kasparov, que já tinha se gabado de que nunca perderia para uma "
    "máquina, passou a dizer que às vezes via nela uma criatividade incomum.",
    "No fim, o Deep Blue venceu o match. Kasparov, que já tinha se gabado de que nunca perderia para uma "
    "máquina, disse que às vezes via nos lances dela uma criatividade incomum, que atribuía a intervenção "
    "humana; a IBM negou. A versão não é unânime: há relatos que situam o lance perturbador na segunda "
    "partida, e não na primeira.")
acrescentar_trecho(12, 0, "suggesting that during the second game, human chess players had intervened on behalf of the machine. "
    "IBM denied this, saying the only human intervention occurred between games.")
acrescentar_trecho(12, 2, "Either at the end of the first game or the beginning of the second, depending on who's telling the story, "
    "the computer made a sacrifice that seemed to hint at its long-term strategy.")

# 0014: sem a coautoria/aposta (verbete fraco); "de forma consistente"
substituir(14, "explicacao",
    "A máquina, MENACE, foi construída com o colega Roger Chambers, depois de uma aposta com alguém que dizia "
    "que ela era impossível.",
    "A máquina se chamava MENACE.")
substituir(14, "explicacao",
    "depois de vinte partidas os dois passaram a empatar sempre, que é o resultado de duas estratégias perfeitas.",
    "depois de vinte partidas os dois passaram a empatar de forma consistente, que é o que acontece quando os "
    "dois lados jogam a estratégia perfeita.")
substituir_trecho(14, 0, "MENACE was constructed as the result of a bet with a computer science colleague who postulated that such a machine was impossible. [...] ", "")

# 0015: a Sotheby's só atribui a peça à oficina de Lewis; carbono-14 mais tardio; nota 3
trocar(15, nota_surpresa=3,
    gancho="Em 1964, um antiquário de Edimburgo pagou 5 libras por uma peça de xadrez de marfim de morsa e a guardou "
           "numa gaveta. Em 2019, a Sotheby's a atribuiu à oficina das famosas peças de Lewis e a vendeu por £735.000.")
substituir(15, "explicacao", "Era uma das torres que faltavam, em forma de guarda armado.",
    "Para a casa de leilões, era provavelmente uma das torres que faltavam, em forma de guarda armado, embora a "
    "própria Sotheby's admita que o tema segue em debate e a datação por carbono-14 da peça tenha dado uma data "
    "mais tardia que a do conjunto.")
acrescentar_trecho(15, 1, "ATTRIBUTED TO THE LEWIS CHESSMEN WORKSHOP, PROBABLY NORWEGIAN, TRONDHEIM, 13TH CENTURY | A WARDER [...] "
    "It is a logical deduction that the present warder could be one of the lost pieces from the Lewis group. "
    "However, it should be recognised that in the absence of a recorded find site for the Lewis hoard and for the present warder, "
    "there is and will continue to be healthy scholarly debate on this subject. [...] "
    "The radiocarbon dating for the present warder below indicates a date later than is generally accepted on stylistic grounds for the Lewis")
# 0012 e 0015: gancho de 0012 dentro de 220 caracteres; trecho com "C14" para o número de carbono-14
substituir(12, "gancho", "jogou um lance válido sorteado ao acaso.", "jogou um lance válido ao acaso.")
acrescentar_trecho(15, 1, "There is no comparative Radiocarbon dating analysis (C14) for any of the Lewis chessmen in the British Museum or National Museum of Scotland.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(8, "gancho", "Marion Tinsley, perdeu", "Marion Tinsley perdeu")
