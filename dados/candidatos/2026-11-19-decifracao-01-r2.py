"""Rodada 2 de Escritas decifradas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-decifracao-01.py"))
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


# 0002: sem "epopeias"; crédito a Kober e a Chadwick
substituir(2, "explicacao", "Quem esperava epopeias se decepcionou: os textos são registros de palácios, com lã, ovelhas e grãos.",
    "Os textos não são poemas: são registros de palácios, com lã, ovelhas e grãos.")
substituir(2, "explicacao", "A virada foi um palpite:",
    "Partindo das tabelas de sinais de Alice Kober, a virada veio de um palpite:")
substituir(2, "explicacao", "pela rádio BBC em 1º de julho de 1952.",
    "pela rádio BBC em 1º de julho de 1952. Quem ouviu foi John Chadwick, filólogo de Cambridge, que passou a "
    "trabalhar com ele.")
substituir(2, "explicacao", "Formado em arquitetura, desenhava escolas para o governo e estudava o Linear B nas horas vagas. ",
    "Formado em arquitetura, desenhava escolas para o governo. ")
acrescentar_trecho(2, 0, "which was heard by John Chadwick, a classicist at the University of Cambridge [...] "
    "The two men began to collaborate on further research into deciphering Linear B.")
acrescentar_trecho(2, 1, "His initial decipherment was achieved using Kober's classification tables, to which he applied his own theories.")

# 0004: Rawlinson concluiu uma decifração iniciada por outros
substituir(4, "explicacao", "Rawlinson decifrou o persa antigo, e ele e Hincks",
    "Rawlinson concluiu a decifração do persa antigo, iniciada décadas antes por outros, e ele e Hincks")

# 0005: parente distante
substituir(5, "gancho", "era uma língua parente do português.", "era uma parente distante do português.")

# 0006: Landa era frade quando queimou os códices; só depois virou bispo
substituir(6, "gancho", "veio do bispo que mandou destruir os livros deles", "veio do frade que mandou destruir os livros deles")
substituir(6, "gancho", "o \"alfabeto\" anotado pelo bispo", "o \"alfabeto\" anotado pelo frade")
substituir(6, "explicacao", "o bispo espanhol Diego de Landa",
    "o frade franciscano espanhol Diego de Landa, que mais tarde seria bispo de Iucatã,")
substituir(6, "explicacao", "como o bispo pronunciava a letra", "como Landa pronunciava a letra")
CANDIDATOS[5]["fontes"].append(wiki("Diego_de_Landa",
    "he became a Franciscan friar in 1541, and was sent as one of the first Franciscans to the Yucatán, arriving in 1549. [...] "
    "Landa was sent back to Spain by Bishop Toral, to stand trial for conducting an illegal Inquisition. [...] "
    "In 1569, the committee absolved Landa of his crimes. "
    "Bishop Toral died in Mexico in 1571, allowing King Philip II of Spain to appoint Landa as the second bishop of Yucatán.",
    nome="Diego de Landa"))

# 0009: soletrar, não pronunciar; entende-se só uma pequena parte; nota 3
trocar(9, nota_surpresa=3)
substituir(9, "gancho", "dá para pronunciar os textos", "dá para soletrar os textos")
substituir(9, "explicacao", "Com isso, os textos podem ser transcritos, mas não traduzidos: faltam textos bilíngues.",
    "Com isso, os textos podem ser transcritos, mas só se entende uma pequena parte deles, como nomes e algumas "
    "palavras: faltam textos bilíngues.")

# 0010: madeira não nativa e reaproveitada; outras datas desde o fim do séc. XVII
trocar(10, nota_surpresa=4, gancho="Uma tabuinha da Ilha de Páscoa com rongorongo, escrita que ninguém sabe ler, é de madeira cortada "
    "entre 1493 e 1509, antes dos europeus. Mas a árvore não é da ilha, e a data virou um enigma.")
substituir(10, "explicacao",
    "Três eram do século XIX, mas a árvore da tabuinha D teria sido derrubada entre 1493 e 1509, data que os "
    "próprios autores não esperavam. A ressalva é que se datou a madeira, não a escrita, que pode ser mais recente.",
    "As outras três deram datas bem posteriores, do fim do século XVII em diante, mas a árvore da tabuinha D teria "
    "sido derrubada entre 1493 e 1509, data que os próprios autores não esperavam. Há duas ressalvas: datou-se a "
    "madeira, não a escrita, que pode ser mais recente; e essa madeira, de uma espécie que não é nativa da ilha, "
    "foi reaproveitada, o que, segundo os próprios autores, limita o valor da data.")
substituir(10, "explicacao", "Se o texto for tão antigo, o rongorongo seria",
    "Se o texto for tão antigo e o rongorongo for de fato escrita, seria")
acrescentar_trecho(10, 1, "Given that the tablets A (Tahua) and D (Échancrée) are crafted from wood derived from non-native tree species, "
    "it is evident that they were fashioned from repurposed wood, thus limiting their utility in dating the tablet's production and the carvings adorning them [...] "
    "Three ranges of the four expand the range of tablets A and B, reaching back to the late seventeenth c. AD.")

# 0013: florescimento; "a maior parte"; Pedra de Roseta como avaliação dos pesquisadores
substituir(13, "explicacao", "Esses conjuntos de cordões circularam pelos Andes entre cerca de 1100 e 1532 e serviram",
    "Esses conjuntos de cordões floresceram nos Andes entre cerca de 1100 e 1532 e serviram")
substituir(13, "explicacao", "Quase tudo o que os pesquisadores conseguiram ler até hoje são números, em sistema decimal.",
    "A maior parte da informação dos quipus estudados até hoje é numérica, em sistema decimal.")
substituir(13, "explicacao", "a ligação mais próxima de uma Pedra de Roseta que se conhece",
    "que os pesquisadores consideram a ligação mais próxima de uma Pedra de Roseta já encontrada")

# 0014: Bankes presumiu e cortou a ajuda
substituir(14, "gancho", "Usou essa leitura sem dizer como chegou a ela, e o inglês nunca o perdoou.",
    "Adotou a leitura sem explicar como, e o inglês, furioso, cortou a ajuda.")
substituir(14, "explicacao", "Bankes concluiu, furioso, que a sugestão dele fora usada sem crédito",
    "Bankes presumiu, furioso, que a sugestão dele fora usada sem crédito")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(2, "explicacao", "Quem ouviu foi John Chadwick, filólogo de Cambridge, que passou a trabalhar com ele.",
    "Entre os ouvintes estava John Chadwick, filólogo de Cambridge, que passou a trabalhar com ele.")
substituir(5, "gancho", "comer: era uma parente distante do português.", "comer: a língua era parente distante do português.")
