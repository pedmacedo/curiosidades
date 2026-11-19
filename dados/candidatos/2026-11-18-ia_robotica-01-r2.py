"""Rodada 2 de Robôs e inteligência artificial: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-ia_robotica-01.py"))
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


# 0001: o que o livro critica, nos termos da fonte
substituir(1, "explicacao", "e virou um crítico do uso deles em decisões humanas.",
    "e criticou a visão que trata computadores como se fossem gente.")
acrescentar_trecho(1, 0, "the anthropomorphic views of computers are just a reduction of human beings")

# 0002: exibições entre 1770 e 1854, não 84 anos de turnê; "enfrentou"; descrições corretas existiram
trocar(2, nota_surpresa=3,
    gancho="Entre 1770 e 1854, um autômato vestido de turco fez exibições de xadrez pela Europa e pelos EUA e enfrentou "
           "até Napoleão e Benjamin Franklin. Dentro da caixa, escondido, havia um mestre de xadrez humano.")
substituir(2, "explicacao", "Ele ganhou a maioria das partidas, inclusive contra estadistas como Napoleão Bonaparte e Benjamin Franklin.",
    "Ele ganhou a maioria das partidas e enfrentou estadistas como Napoleão Bonaparte e Benjamin Franklin.")
substituir(2, "explicacao", "Muita gente desconfiava de fraude, mas ninguém descreveu o mecanismo corretamente enquanto a máquina existia.",
    "Muita gente desconfiava de fraude e surgiram muitos palpites, a maioria errada. Em 1827, em Baltimore, o calor "
    "fez o operador escondido passar mal, e uma revista francesa publicou em 1834 uma descrição considerada "
    "acertada, mas o segredo nunca foi confirmado publicamente enquanto a máquina existia.")
acrescentar_trecho(2, 0, "Of the many contemporary books and articles written about the mechanism of the Turk, most were inaccurate and drew incorrect inferences. "
    "An exception was \"Automate joueur d'échecs\", published in the popular magazine Le Magasin pittoresque in 1834 [...] "
    "The hoax was exposed in 1827 during a match in Baltimore when the unusually high temperature rendered the operator, William Schlumberger, faint.")

# 0003: a observação de 1988, com damas; as críticas
trocar(3, gancho="Em 1988, Hans Moravec notou: é mais fácil um computador ter desempenho de adulto em testes de inteligência "
    "ou no jogo de damas do que ter a percepção e os movimentos de um bebê de um ano.")
substituir(3, "explicacao",
    "Isso ajuda a entender por que robôs que dobram roupa ou sobem escadas com destreza demoraram tanto, enquanto computadores vencem campeões de xadrez há décadas.",
    "A ideia tem críticos: o pioneiro da IA Allen Newell a chamou de \"mito\", e o pesquisador Arvind Narayanan diz que "
    "ela revela mais sobre o que a comunidade de IA acha que vale a pena estudar do que sobre o que será fácil ou "
    "difícil para as máquinas.")
acrescentar_trecho(3, 0, "AI pioneer Allen Newell criticized the idea as a \"myth\". "
    "Arvind Narayanan describes Moravec's paradox as \"a statement about what the AI community finds it worthwhile to work on\" instead of \"pr")

# 0005: o otimismo de "um verão"
trocar(5, nota_surpresa=3,
    gancho="O termo \"inteligência artificial\" nasceu numa proposta de 1955: dez cientistas, dois meses, e a aposta de "
           "que um verão bastaria para um avanço real em fazer máquinas usarem linguagem e se aperfeiçoarem.")

# 0006: 1958 x 1959; a previsão era da Marinha; financiamento; uma das versões
trocar(6, gancho="Em 1958, o New York Times chamou o perceptron, uma máquina que aprendia, de \"embrião\" de um computador "
    "que, segundo a Marinha, andaria, falaria e teria consciência. A versão física, de 1959, tinha só 400 fotocélulas.")
substituir(6, "explicacao", "com dinheiro da Marinha americana", "com dinheiro, entre outros, do Escritório de Pesquisa Naval dos EUA")
substituir(6, "explicacao", "Tinha três camadas:", "Uma das versões tinha três camadas:")
acrescentar_trecho(6, 0, "and the Rome Air Development Center [...] One version was implemented as follows")

# 0007: sem "quentes"; a batuta; o objetivo de Engelberger
substituir(7, "gancho", "pegando peças fundidas quentes", "pegando peças fundidas")
substituir(7, "explicacao", "regeu a orquestra com a batuta e agitou um acordeão", "agitou a batuta do maestro e sacudiu um acordeão")
substituir(7, "explicacao", "O objetivo era criar trabalhadores mecânicos",
    "O objetivo do sócio de Devol, Joseph Engelberger, era criar trabalhadores mecânicos")
substituir_trecho(7, 0, "ultimate goal was to create", "Engelberger's ultimate goal was to create")
acrescentar_trecho(7, 0, "Devol, together with Joseph Engelberger, his business associate, started the world's first robot manufacturing company, Unimation.")

# 0008: os gestos involuntários eram do dono; a pergunta era sobre a data
substituir(8, "gancho", "mas só lia sem querer as reações do dono", "mas só lia gestos involuntários do dono")
substituir(8, "explicacao", "que dia será a sexta seguinte?", "em que dia do mês cairá a sexta seguinte?")

# 0009: o A* nos videogames, com fonte; sem a transformada de Hough
substituir(9, "gancho", "para achar caminhos em mapas e videogames", "para achar caminhos em videogames")
substituir(9, "explicacao",
    "Entre os resultados mais importantes do projeto estão o algoritmo de busca A*, a transformada de Hough, usada para achar retas em imagens, e o método do grafo de visibilidade.",
    "Entre os resultados mais importantes do projeto estão o algoritmo de busca A*, criado para planejar os trajetos "
    "do robô, e o método do grafo de visibilidade.")
CANDIDATOS[8]["fontes"].append(wiki("A*_search_algorithm",
    "A* is often used for the common pathfinding problem in applications such as video games, but was originally designed as a general graph traversal algorithm. [...] "
    "A* was created as part of the Shakey project, which had the aim of building a mobile robot that could plan its own actions. "
    "Nils Nilsson originally proposed using the Graph Traverser algorithm for Shakey's path planning.",
    nome="A* search algorithm"))

# 0010: a anedota não tem data
trocar(10, nota_surpresa=3)
substituir(10, "gancho", "um tradutor automático dos anos 1950", "um tradutor automático da Guerra Fria")
acrescentar_trecho(10, 0, "During the Cold War, the US government was particularly interested in the automatic, instant translation of Russian documents")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(5, "gancho", "para um avanço real em fazer máquinas usarem linguagem e se aperfeiçoarem.",
    "para um avanço real em algum problema, como fazer máquinas usarem linguagem.")
substituir(6, "gancho", "A versão física, de 1959, tinha só 400 fotocélulas.", "Uma versão física, de 1959, tinha só 400 fotocélulas.")
