"""Rodada 2 de Esportes tradicionais: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-esportes_tradicionais-01.py"))
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


# notas dos aprovados sem mudança de texto
trocar(4, nota_surpresa=5)
trocar(9, nota_surpresa=3)

# 0001: a fonte diz que só algumas partidas eram grandes acontecimentos
substituir(1, "explicacao",
    "As partidas tradicionais eram grandes acontecimentos, que podiam durar vários dias.",
    "Algumas partidas tradicionais eram grandes acontecimentos, que podiam durar vários dias.")

# 0003: três formas de ulama; só a de quadril usa a bola de 3 a 4 kg; quem marca ponto é o adversário
substituir(3, "gancho",
    "uma bola maciça de borracha de 3 a 4 kg só pode ser rebatida com o quadril.",
    "na versão mais tradicional, uma bola de borracha de 3 a 4 kg só pode ser rebatida com o quadril.")
substituir(3, "explicacao",
    "Na versão de quadril, cada time tem",
    "Das três formas atuais (de quadril, de antebraço e com taco), a mais tradicional é a de quadril: cada time tem")
substituir(3, "explicacao",
    "perde ponto o time que a deixa sair, que a toca com outra parte do corpo ou até que se esquece de anunciar o placar",
    "o adversário marca ponto quando um time deixa a bola sair, a toca com outra parte do corpo ou até quando se esquece de anunciar o próprio placar")
acrescentar_trecho(3, 0,
    "The modern-day game has three main forms: "
    "Ulama de cadera or hip ulama. [...] "
    "Ulama de antebrazo or forearm ulama. [...] "
    "Ulama de mazo or Ulamad de palo, in which a heavy (6–7 kg or 13–15 lb) two-handed wooden paddle strikes a 500g (1 lb) ball")

# 0005: era a regra anunciada antes do evento
substituir(5, "gancho",
    "O regulamento previa o mesmo prêmio para os quatro melhores de cada prova.",
    "As regras anunciadas antes do evento previam o mesmo prêmio para os quatro melhores de cada prova.")
substituir(5, "explicacao",
    "mas, em vez de medalhas de valores diferentes para os três primeiros, os quatro melhores receberiam o mesmo prêmio.",
    "mas, segundo o que a organização anunciou dias antes da abertura, em vez de medalhas de valores diferentes para os três primeiros, os quatro melhores receberiam o mesmo prêmio.")
trocar(5, nota_surpresa=3)

# 0006: o par de toras krahô é feito quando a disputa começa fora da aldeia
substituir(6, "explicacao",
    "é feito com cuidado a cada disputa",
    "é feito com cuidado sempre que a disputa começa fora da aldeia")

# 0011: em 1960 a Malásia ainda era a Malaia
substituir(11, "explicacao",
    "quando dirigentes da Malásia, de Singapura, da Tailândia e de Mianmar padronizaram as regras",
    "quando dirigentes da Malaia (atual Malásia), de Singapura, da Tailândia e de Mianmar padronizaram as regras")

# 0014: 500 g só para júnior e média; o recorde de 66 m é o mais citado, há relatos maiores
substituir(14, "explicacao",
    "Hoje há regras: o haggis esportivo padrão pesa 500 gramas",
    "Hoje há regras: nas categorias júnior e média, o haggis esportivo pesa 500 gramas")
substituir(14, "explicacao",
    "O recorde mundial, de 66 metros, foi registrado em 2011",
    "O recorde mais citado, de 66 metros, foi registrado em 2011, embora haja relatos de arremessos mais longos")
acrescentar_trecho(14, 0,
    "However, the Australian cricket player Tom Moody was purported to have thrown a haggis in 1989 over 230 feet (70 metres). [...] "
    "An allowance of ±30 grams is given and this weight is used in both junior and middle weight events.")

# 0015: frase vaga sobre a indústria do tejo
substituir(15, "explicacao", "No país, só o futebol move uma indústria maior. ", "")
substituir_trecho(15, 0, "Only soccer has a larger and more supported industry in Colombia. [...] ", "")

# 0016: sumô no Brasil desde 1914 (não o feminino); a prefeita ficou ao lado do ringue
substituir(16, "gancho",
    "Já o Brasil, com torneios desde 1914, é um centro do sumô feminino.",
    "Já o Brasil, onde há sumô desde 1914, é um centro do sumô feminino.")
substituir(16, "explicacao",
    "a prefeita de Takarazuka teve de discursar ao lado do ringue, e não dentro dele",
    "a prefeita de Takarazuka teve de ficar ao lado do ringue, e não dentro dele, numa exibição")

# ganchos de 0003 e 0005 encurtados para caber em 220 caracteres, mantendo as correções
trocar(3, gancho="No México ainda se joga o ulama, herdeiro do jogo de bola asteca. Na versão mais tradicional, a bola de "
    "borracha, de 3 a 4 kg, só pode ser rebatida com o quadril. É tido como um dos esportes mais antigos em atividade.")
trocar(5, gancho="Os primeiros Jogos Mundiais dos Povos Indígenas (Palmas, 2015) tinham o lema \"o importante não é ganhar, "
    "e sim celebrar\". As regras anunciadas antes do evento davam o mesmo prêmio aos quatro melhores de cada prova.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(3, 'gancho',
    'Na versão mais tradicional, a bola',
    'Na versão mais difundida, a bola')
substituir(3, 'explicacao',
    'a mais tradicional é a de quadril',
    'a mais difundida é a de quadril')
substituir(15, 'gancho',
    'esporte tradicional muito popular na Colômbia',
    'esporte tradicional popular na Colômbia')
substituir(15, 'explicacao',
    'colocados na borda do alvo',
    'colocados na borda do aro de metal que serve de alvo, no meio da argila')
