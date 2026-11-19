"""Rodada 2 de Probabilidade e estatística: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-probabilidade-01.py"))
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


# 0002: os 270 e 276 são tanques Panther; final reescrito numa frase própria sobre o legado do método
trocar(2, gancho="Na Segunda Guerra, os Aliados estimaram quantos tanques Panther a Alemanha fabricava olhando os números "
    "de série de peças capturadas. Para fevereiro de 1944, calcularam 270; os registros alemães diziam 276.")
substituir(2, "explicacao",
    "isso virou uma estimativa de produção mensal: 270 tanques em fevereiro de 1944, bem mais do que se suspeitava.",
    "isso virou uma estimativa de 270 Panthers produzidos em fevereiro de 1944, bem mais do que se suspeitava.")
substituir(2, "explicacao",
    "A abordagem estatística foi muito mais precisa que a espionagem tradicional, que tendia "
    "a superestimar a produção nazista, e deu nome a esse tipo de análise: o \"problema dos tanques "
    "alemães\". O mesmo truque funcionou com outros equipamentos, com mais sucesso no caso do foguete V-2, "
    "e muito depois serviu para estimar quantos computadores Commodore 64 foram fabricados.",
    "Deixando para trás os palpites dos espiões, que costumavam inflar a produção nazista, o método ganhou o "
    "apelido de \"problema dos tanques alemães\" e foi reaproveitado em outros armamentos, com o melhor "
    "resultado no foguete V-2, e até para calcular quantos Commodore 64 foram fabricados.")
acrescentar_trecho(2, 0, "as was the case in estimation of Panther tank production just prior to D-Day.")

# 0004: gancho corrigido e explicação reescrita com estrutura própria (problema, solução, sigilo, Fisher)
trocar(4, nota_surpresa=3,
    gancho="O \"teste t de Student\", da estatística, deve o nome a um pseudônimo: o criador era um cervejeiro da "
           "Guinness, que proibia seus pesquisadores de assinar artigos com o nome verdadeiro.",
    explicacao=(
        "Na cervejaria Arthur Guinness & Son, em Dublin, o trabalho de William Sealy Gosset era tirar conclusões "
        "de pouca informação: descobrir, por exemplo, quais variedades de cevada rendiam mais a partir de "
        "experimentos com amostras pequenas, sabendo que analisá-los era difícil. Karl Pearson e os biometristas lidavam com centenas de observações e não viam pressa em criar "
        "técnicas para poucos dados. A Guinness chegou a mandar Gosset passar dois períodos letivos no "
        "laboratório de Pearson, em 1906 e 1907, mas a solução veio do próprio cervejeiro: a distribuição hoje "
        "chamada t de Student, que no começo ele designava pela letra z, e um trabalho pioneiro no planejamento "
        "de experimentos com amostras pequenas. Restava o problema da assinatura. A empresa tinha se assustado "
        "quando um de seus pesquisadores publicou informações que poderiam servir à concorrência, e passou a "
        "exigir que nenhum artigo da casa falasse em cerveja, citasse a Guinness ou revelasse quem o escreveu. "
        "Gosset virou \"Student\", talvez por causa de um caderno que manteve naqueles anos, \"The Student's "
        "Science Notebook\", e assim assinou a maior parte dos seus 21 artigos. Pearson ajudou com a matemática, "
        "mas deu pouco valor ao resultado. Quem percebeu o alcance dele foi Ronald Fisher, com quem Gosset trocou "
        "mais de 150 cartas; numa de 1924, mandou as tabelas avisando que Fisher era, provavelmente, o único que "
        "as usaria. Gosset passou 38 anos na Guinness e morreu em 1937, um mês depois de virar "
        "cervejeiro-chefe de toda a empresa."
    ))
acrescentar_trecho(4, 0, "He had conducted experiments with only small sample sizes and was aware that analysis was difficult [...] "
    "Pearson helped Gosset with the mathematics of his papers, including the 1908 papers, but had little appreciation of their importance.")

# 0005: "três das quatro escolhidas"; o critério de 5%; sem a frase sobre mais tentativas
substituir(5, "explicacao",
    "Acertar três ou mais por sorte é bem mais fácil: cerca de 24,3%. Por isso, Fisher só aceitaria descartar a "
    "hipótese do chute se ela acertasse as oito, e mesmo assim sem medir o tamanho da habilidade. Depois, ele "
    "discutiu as vantagens de fazer mais tentativas e repetir os testes. ",
    "Já acertar pelo menos três das quatro xícaras escolhidas por pura sorte acontece em cerca de 24,3% das "
    "vezes. Pelo critério usual, de chance abaixo de 5%, só o acerto total era improvável o bastante: um "
    "resultado assim derrubaria a hipótese do chute, mas não diria o quanto ela era boa nisso. ")
acrescentar_trecho(5, 0, "The critical region for rejection of the null of no ability to distinguish was the single case of 4 successes of 4 possible, based on the conventional probability criterion < 5%.")

# 0006: apostadores, não trapaceiros; só contraintuitivo
substituir(6, "explicacao", "E mágicos e trapaceiros treinados conseguem", "E mágicos e apostadores com prática conseguem")
trocar(6, tipos_espanto=["contraintuitivo"])

# 0008: os 34% valem para a grade em três dimensões
trocar(8, gancho="Quem anda ao acaso pelas esquinas de uma cidade infinita quase certamente volta ao ponto de partida um "
    "dia. Já um pássaro que voe ao acaso por uma grade 3D infinita tem só cerca de 34% de chance de voltar.")
substituir(8, "explicacao", "Com três dimensões, porém, a chance de retorno cai para cerca de 34%",
    "Numa grade equivalente em três dimensões, porém, a chance de retorno cai para cerca de 34%")

# 0009: efeito das redes; antes do quê
trocar(9, gancho="Em geral, seus amigos têm mais amigos do que você, por um efeito matemático das redes. Pesquisadores "
    "usaram esse viés para perceber um surto de gripe em Harvard quase duas semanas antes do que no resto do campus.")

# 0010 (aprovado, ajuste opcional): "tendiam a dar"
substituir(10, "explicacao", "reservavam o tratamento melhor, o A, para os casos difíceis, de pedras grandes,",
    "tendiam a dar o tratamento melhor, o A, aos casos difíceis, de pedras grandes,")

# 0013: sem "num assoalho" no gancho; a condição exata dos cruzamentos
substituir(13, "gancho", "disse ter jogado uma agulha 3.408 vezes num assoalho e, contando",
    "disse ter jogado uma agulha 3.408 vezes e, contando")
substituir(13, "explicacao", "e os cruzamentos baterem exatamente com o esperado;",
    "e o número de cruzamentos for exatamente 113/213 do número de lançamentos;")
acrescentar_trecho(13, 0, "or equivalently, x=113n213.")

# 0014: a RAND criou o livro (a Free Press publicou); "repetidamente"
substituir(14, "gancho", "a RAND publicou um livro", "a RAND lançou um livro")
substituir(14, "explicacao", "tendem a abrir sempre as mesmas páginas", "tendem a abrir as mesmas páginas repetidamente")

# 0015: uma espécie, com nome; o uso famoso do problema é estimar pi
substituir(15, "gancho", "Formigas exploradoras medem", "Batedoras de uma formiga europeia medem")
substituir(15, "explicacao", "A espécie é uma formiga europeia de cerca de 3 mm",
    "A espécie é a Temnothorax albipennis (chamada de Leptothorax albipennis no texto que descreve o estudo), "
    "uma formiga europeia de cerca de 3 mm")
substituir(15, "explicacao", "o que interessa não é calcular pi, como Buffon fez, mas",
    "o que interessa não é estimar pi, como no uso mais famoso do problema, mas")
substituir_trecho(15, 1, "a small ant approximately 3mm long", "Leptothorax albipennis [...] a small ant approximately 3mm long")
CANDIDATOS[15 - 1]["fontes"].append(wiki("Buffon%27s_needle_problem",
    "This can be used to design a Monte Carlo method for approximating the number π, although that was not the original motivation for de Buffon's question. [...] "
    "Scientists found that Temnothorax albipennis (rock ants) use the Buffon needle algorithm to estimate the size of potential nests.",
    nome="Buffon's needle problem"))

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(2, "explicacao", "Deixando para trás os palpites dos espiões, que costumavam inflar a produção nazista, o método ganhou",
    "Bem mais preciso que a inteligência tradicional, que costumava superestimar a produção nazista, o método ganhou")
