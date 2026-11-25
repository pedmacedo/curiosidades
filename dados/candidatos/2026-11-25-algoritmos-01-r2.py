"""Rodada 2 de Algoritmos e computação: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-algoritmos-01.py"))
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


# 0001: o RSA é "muito usado" no comércio eletrônico, não "a" criptografia dele
substituir(1, "gancho", "Hoje ele é um dos passos do RSA, a criptografia do comércio eletrônico.",
    "Hoje é um dos passos do RSA, criptografia muito usada no comércio eletrônico.")

# 0002: Turing provou problemas aparentados; a formulação da parada é dos anos 1950; nota 3
trocar(2, nota_surpresa=3,
    gancho="O problema da parada, segundo o qual nenhum algoritmo prevê se qualquer programa termina, costuma ser "
           "creditado a Turing. Mas ele nunca escreveu \"halt\" (parar): essa formulação só surgiu nos anos 1950.")
substituir(2, "explicacao",
    "Alan Turing mostrou que não existe um algoritmo geral que acerte a resposta para todos os pares de programa e "
    "entrada. A prova dele saiu em janeiro de 1937, meses depois de Alonzo Church publicar, em abril de 1936, outra "
    "prova de indecidibilidade.",
    "Não existe algoritmo geral que acerte a resposta para todos os pares de programa e entrada. O resultado costuma "
    "ser creditado ao artigo de Turing publicado em janeiro de 1937, meses depois de Alonzo Church publicar, em abril "
    "de 1936, outra prova de indecidibilidade. Mas, nesse artigo, Turing provou indecidíveis problemas aparentados, "
    "como o de saber se uma máquina chega a imprimir certo símbolo; o problema da parada, nessa forma, só surgiu nos "
    "anos 1950.")
substituir(2, "explicacao", "atribuem ao artigo de Turing a definição do \"problema da parada\"",
    "atribuem ao artigo de Turing a definição e a prova do \"problema da parada\"")
acrescentar_trecho(2, 0, "Since then, many other undecidable problems have been described, including the halting problem which emerged in the 1950s. [...] "
    "the printing problem considered in Turing's 1936 paper (\"does a Turing machine starting from a blank tape ever print a given symbol?\")")

# 0003: Cohen creditou o nome a Adleman; "primeiro artigo acadêmico"; sem causalidade
substituir(3, "gancho", "O termo \"vírus de computador\" veio do mentor dele.",
    "Ele creditou o nome \"vírus\" ao seu mentor.")
substituir(3, "explicacao", "o primeiro a chamar explicitamente de \"vírus\"",
    "o primeiro artigo acadêmico a chamar explicitamente de \"vírus\"")
substituir(3, "explicacao", "Por isso, os antivírus trabalham com aproximações.",
    "Na prática, os antivírus trabalham com aproximações.")

# 0008: "sem fama" era juízo sem apoio
substituir(8, "explicacao", "Entre 1805 e 1965, outras versões chegaram a ser publicadas, sem fama.",
    "Entre 1805 e 1965, outros autores chegaram a publicar versões do método, sem perceber todo o seu alcance.")
acrescentar_trecho(8, 0, "though like Gauss they did not do the analysis to discover that this led to")

# 0009: o mistério foi resolvido (historia_humana); gancho com a divisão por 2; nota 3
trocar(9, nota_surpresa=3, tipos_espanto=["engenhosidade", "historia_humana"],
    gancho="O jogo Quake III calculava 1/√x lendo os bits de um número com vírgula como se fosse inteiro, dividindo "
           "por 2 e subtraindo de uma constante mágica, 0x5F3759DF. Por anos, ninguém soube quem inventou aquilo.")
acrescentar_trecho(9, 0, "taking a square root by dividing by two (which is just a right-shift)")

# 0012: "empírica"; a rebeldia vinha da escola; o pedido de excomunhão sem afirmar que foi atendido; IEEE Spectrum
substituir(12, "gancho", "tiveram a primeira aplicação prática num poema",
    "tiveram a primeira aplicação empírica num poema")
substituir(12, "explicacao", "Markov tinha fama de rebelde.",
    "Desde a escola, alguns professores o viam como rebelde.")
substituir(12, "explicacao",
    "Ateu, em 1912 respondeu à excomunhão de Liev Tolstói pedindo a própria excomunhão à Igreja Ortodoxa Russa, que atendeu ao pedido.",
    "Ateu, em 1912 pediu à Igreja Ortodoxa Russa a própria excomunhão, numa referência à de Liev Tolstói.")
substituir_trecho(12, 0, " [...] Markov was an atheist. In 1912, he responded to Leo Tolstoy's excommunication from the Russian Orthodox Church by requesting his own excommunication. "
    "The Church complied with his request.",
    " [...] Markov was an atheist. In 1912, he responded to Leo Tolstoy's excommunication from the Russian Orthodox Church by requesting his own excommunication.")
acrescentar_trecho(12, 0, "He attended the St. Petersburg Grammar School, where some teachers saw him as a rebellious student.")
CANDIDATOS[11]["fontes"].append({
    "url": "https://spectrum.ieee.org/andrey-markov-and-claude-shannon-built-the-first-language-generation-models",
    "titulo": "Andrey Markov & Claude Shannon Counted Letters to Build the First Language-Generation Models (IEEE Spectrum)",
    "idioma": "en",
    "trecho": "wrote out the first 20,000 letters of the book in one long string of letters",
})

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
# 0012: a fonte fala só da escola, e diz "responded to"
substituir(12, "explicacao",
    "Desde a escola, alguns professores o viam como rebelde.",
    "Na escola, alguns professores já o viam como rebelde.")
substituir(12, "explicacao",
    "numa referência à de Liev Tolstói.",
    "em resposta à excomunhão de Liev Tolstói.")
