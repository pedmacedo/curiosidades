"""Rodada 2 de Teoria dos jogos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-teoria_jogos-01.py"))
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


# 0001: Hamilton escreveu o artigo com Axelrod, não os torneios
substituir(1, "explicacao",
    "O trabalho, feito também com o biólogo W. D. Hamilton, virou referência para explicar a cooperação entre seres vivos, de bactérias a primatas.",
    "Num artigo escrito com o biólogo W. D. Hamilton, Axelrod levou essas ideias para a cooperação entre seres vivos, de bactérias a primatas, e o trabalho virou referência.")

# 0004: a frase de von Neumann é relato da biografia de Nasar
trocar(4, gancho="John Nash ganhou o Nobel de Economia de 1994 por ideias de uma tese de doutorado de 28 páginas. "
    "Segundo sua biógrafa, ao mostrar o resultado a von Neumann, ouviu: \"Isso é trivial. É só um teorema do ponto fixo.\"")
substituir(4, "explicacao",
    "Em 1949, ao ouvir a ideia, von Neumann a despachou com a frase famosa.",
    "Segundo a biografia escrita por Sylvia Nasar (Uma Mente Brilhante), foi em 1949, ao ouvir a ideia, que von Neumann a despachou com essa frase.")
substituir_trecho(4, 1,
    "\"That's trivial, you know. That's just a fixed-point theorem.\"",
    "\"That's trivial, you know. That's just a fixed-point theorem.\" (See Nasar, 1998, p. 94.)")

# 0005: tréguas também combinadas; "às vezes"; sem "qualquer morte"
trocar(5, gancho="Nas trincheiras da Primeira Guerra, inimigos paravam de atirar, às vezes sem combinar nada, ou disparavam "
    "de um jeito ritual, sem intenção de matar. Alguns generais chegavam a analisar as baixas para flagrar isso.")
substituir(5, "explicacao", "e o sistema, frágil, se desfazia com qualquer morte",
    "e o sistema, frágil, se desfazia facilmente quando havia mortes")

# 0007: uma revista; leitura de Hamilton sem lugar; artigo "pioneiro"
substituir(7, "explicacao", "escreveu em revistas científicas contra a percepção extrassensorial",
    "escreveu na revista Science contra a percepção extrassensorial")
substituir(7, "explicacao", "Lá, tinha lido os trabalhos de W. D. Hamilton sobre seleção de parentesco e, sem treino",
    "Depois de ler os trabalhos de W. D. Hamilton sobre seleção de parentesco, e sem treino")
substituir(7, "explicacao", "assinou com John Maynard Smith o artigo que levou a teoria dos jogos para a biologia",
    "assinou com John Maynard Smith um artigo pioneiro na aplicação da teoria dos jogos à biologia evolutiva")

# 0011: comparação dos anos 1990; só a China privatizou; "muitas vezes surpreendentemente"
trocar(11, gancho="Nos anos 1990, satélites mostraram pastos nômades da Mongólia mais conservados que os vizinhos da China e "
    "da Rússia, onde houve coletivização (e, na China, privatização). Elinor Ostrom ajudou a entender por quê.")
substituir(11, "explicacao", "concluiu que eles costumam ser bem administrados pelos próprios usuários",
    "concluiu que eles muitas vezes são surpreendentemente bem administrados pelos próprios usuários")

# 0013: sem os números de 16/22 e 15/22; gancho sem "a mesma"
substituir(13, "gancho", "A resposta mais comum foi a mesma: meio-dia, na estação Grand Central.",
    "A resposta mais comum: meio-dia, na estação Grand Central.")
substituir(13, "explicacao",
    "Schelling testou outros casos: com dois jogadores escolhendo \"cara\" ou \"coroa\" e ganhando se coincidissem, 16 de 22 de um grupo e 15 de 22 do outro escolheram cara.",
    "Schelling testou outros casos: quando dois jogadores ganhavam se dissessem a mesma coisa entre \"cara\" e \"coroa\", a maioria escolheu cara.")
substituir_trecho(13, 0,
    "For the two players, A and B, in head-tail game. 16 out of 22 A and 15 out of 22 B chose \"heads\". ",
    "")

# 0015: o vencedor foi 21,6 (fonte nova); sem a "média 33"; só contraintuitivo
trocar(15, tipos_espanto=["contraintuitivo"])
substituir(15, "gancho", "a média dos palpites foi 33.", "o número vencedor foi 21,6.")
substituir(15, "explicacao", "quem dá um passo além aposta 22.",
    "quem dá um passo além aposta 22. O número vencedor do Politiken, em 2005, ficou perto desse segundo degrau: "
    "21,6, com o prêmio dividido entre cinco pessoas.")
substituir_trecho(15, 0,
    "When performed among ordinary people it is usually found that the winner's guess is much higher than 0: the average value was found to be 33 in a large online competition organized by the Danish newspaper Politiken. ",
    "When performed among ordinary people it is usually found that the winner's guess is much higher than 0: [...] in a large online competition organized by the Danish newspaper Politiken. ")
CANDIDATOS[14]["fontes"].append({
    "url": "https://aperiodical.com/2015/08/new-york-times-puzzle-is-pure-game-theory/",
    "titulo": "New York Times puzzle is pure game theory",
    "idioma": "en",
    "trecho": "Past versions of this type of competition include one run by Danish magazine Politiken in 2005, using similar rules, "
              "in which 19,196 entrants turned out a winning value of 21.6 (the prize was shared by five people).",
})

# 0016: "menos chance de dividir", não "tendia a roubar"; "variante" do dilema
substituir(16, "gancho", "quem tocava fisicamente o rival tendia a roubar, e quem puxava o riso tendia a dividir.",
    "quem tocava fisicamente o rival tinha menos chance de dividir, e quem puxava o riso, mais.")
substituir(16, "explicacao",
    "notaram que tomar a iniciativa do contato físico, ou ser tocado, se associava a roubar, e que puxar o riso se associava a dividir.",
    "notaram que tomar a iniciativa do contato físico, ou ser tocado, se associava a uma chance menor de dividir, e que puxar o riso se associava a uma chance maior.")
substituir(16, "explicacao", "a final é um dilema do prisioneiro com dinheiro de verdade",
    "a final é uma variante do dilema do prisioneiro com dinheiro de verdade")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(13, "explicacao", "Schelling testou outros casos: quando dois jogadores ganhavam se dissessem a mesma coisa entre \"cara\" e \"coroa\", a maioria escolheu cara. Ao ordenar", "Schelling testou outros casos: ao ordenar")
