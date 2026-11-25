"""Rodada 2 de Nomes de lugares: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-nomes_lugares-01.py"))
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


# 0001, 0009, 0011, 0013, 0014: aprovados sem mudança (nota 4 mantida)
# 0004: reprovado, fica como está
# 0007: aprovado, nota ajustada para 3 (já era 3)
trocar(7, nota_surpresa=3)

# 0002: a leitura de Magalhães é relato; sem causalidade inventada
substituir(2, "gancho", "que estava na moda e era uma das leituras favoritas de Fernão de Magalhães.",
    "que estava na moda e, segundo se conta, estava entre as leituras de Fernão de Magalhães.")
substituir(2, "explicacao", "O livro estava muito em voga e era uma das leituras favoritas de Magalhães.",
    "O livro estava muito em voga, e conta-se que Magalhães o lia.")
substituir(2, "explicacao", "mas essa etimologia é questionável, já que o relato de Pigafetta não explica de onde veio a palavra.",
    "mas essa etimologia é questionável, e o relato de Pigafetta não explica de onde veio a palavra.")

# 0003: o mito desmentido passa a ser o "cá nada"; detalhe das línguas iroquesas
trocar(3, nota_surpresa=3,
    gancho="Canadá não vem do português \"cá nada\", como diz uma lenda antiga: vem de kanata, \"aldeia\" numa língua "
           "iroquesa hoje extinta. E Jacques Cartier, que adotou o nome, sabia o que a palavra queria dizer.")
substituir(3, "explicacao", "Houve também teorias de uma origem espanhola ou portuguesa, mas nunca se achou prova",
    "A teoria rival mais conhecida diz que exploradores ibéricos, sem achar ouro nem prata, teriam escrito \"cá nada\" "
    "(ou \"acá nada\", em espanhol) nos mapas. Mas nunca se achou prova")
substituir(3, "explicacao",
    "mas era próxima de línguas como o mohawk, o onondaga e o sêneca, que têm palavras parecidas para \"cidade\"",
    "mas era próxima de outras línguas iroquesas, como o oneida e o mohawk; em mohawk, onondaga e sêneca há palavras "
    "parecidas para \"cidade\"")
acrescentar_trecho(3, 0,
    "While the Saint-Lawrence Iroquoian origin for the name Canada is now widely accepted, other theories have been put forth in the past. [...] "
    "The most common alternative theory suggested that the name originated when Portuguese or Spanish explorers, having explored the northern part of the continent and unable to find gold and silver, "
    "wrote cá nada ('nothing here' in Portuguese), acá nada, aqui nada or el cabo de nada ('Cape Nothing' in Spanish) on that part of their maps. [...] "
    "In most versions of the Iberian origin theory, the Spanish or Portuguese passed their name on to the Iroquois, who rapidly adopted it in place of their own prior word for a village")

# 0005: as fontes divergem sobre quem matou Aleixo Garcia
substituir(5, "explicacao", "Garcia foi morto pelos guaranis no fim de 1525, mas a prata chegou ao litoral",
    "Garcia foi morto no fim de 1525 (os relatos divergem sobre quem o matou), mas a prata chegou ao litoral")
acrescentar_trecho(5, 0, "He was killed by the Payaguás, returning to Santa Catarina (Brazil)")

# 0006: sem superlativo
substituir(6, "explicacao", "O exemplo mais famoso, porém, é exagerado.", "Um dos exemplos mais citados, porém, é exagerado.")

# 0008: a tradução parece invenção de um editor; datas coerentes; confissão de Daly
trocar(8, nota_surpresa=3)
substituir(8, "gancho", "Segundo especialistas, essa tradução é farsa.",
    "Mas essa tradução parece ter sido inventada por um editor de jornal.")
substituir(8, "explicacao", "Desde 1912, porém, ele também é conhecido",
    "Desde o começo do século XX, porém, ele também é conhecido")
substituir(8, "explicacao", "por volta de 1910.",
    "por volta de 1910. Consta que o próprio Daly confessou várias vezes ter inventado a tradução.")
acrescentar_trecho(8, 0, "Reportedly, Daly had confessed to fabricating the name on multiple occasions.")

# 0010: 1545 é o uso mais antigo conhecido; sem "explorado décadas depois"
substituir(10, "explicacao", "A forma encurtada \"Australia\" aparece em latim pela primeira vez em 1545 e se referia",
    "O uso mais antigo conhecido da forma encurtada \"Australia\", em latim, é de 1545, e ela se referia")
substituir(10, "explicacao", "O do polo Sul, que só seria explorado décadas depois, ficou sem nome",
    "O do polo Sul ficou sem nome")

# 0012: "se opôs"; Sagarmatha é nome oficial de hoje
trocar(12, nota_surpresa=3)
substituir(12, "gancho", "um agrimensor que recusou a honra", "um agrimensor que se opôs à homenagem")
substituir(12, "explicacao", "Os nomes locais existem: em nepalês, a montanha é Sagarmatha",
    "Hoje a montanha tem nomes locais oficiais: em nepalês, Sagarmatha")

# 0015: autor da imagem boliviana; frase mais clara sobre Ipanema
substituir(15, "explicacao",
    "Segundo a história do lugar, a imagem foi feita em 1582 por um neto do governante inca Manco Kapac, depois de "
    "muitas tentativas fracassadas, inspirado pelas imagens da Virgem que viu em igrejas de La Paz.",
    "Segundo a tradição, a imagem foi esculpida por volta de 1582 por um artista indígena descendente da nobreza "
    "inca, depois de muitas tentativas fracassadas, inspirado pelas imagens da Virgem que viu em igrejas de La Paz.")
substituir(15, "explicacao", "o bairro homenageia o barão e a terra natal dele, não a praia",
    "o nome não nasceu da praia, mas do título do barão e da terra natal dele")

# 0016: o extinto era o tupi antigo, não "a língua"
substituir(16, "gancho", "quando ninguém mais falava a língua, e alguns saíram errados",
    "quando o tupi antigo já estava extinto havia séculos, e alguns saíram errados")
substituir(16, "explicacao", "Alguns ficaram corretos, como Paratinga", "Na análise de Navarro, alguns ficaram corretos, como Paratinga")

# 0002: gancho dentro de 220 caracteres
substituir(2, "gancho", "Patagón, criatura selvagem de um romance", "Patagón, criatura de um romance")

# 0016: nota conforme o veredito
trocar(16, nota_surpresa=4)

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(3, 'gancho',
    'como diz uma lenda antiga',
    'como diz uma velha teoria')
substituir(3, 'explicacao',
    'e por volta de 1545 livros e mapas europeus',
    'e em 1545 livros e mapas europeus')
substituir(8, 'explicacao',
    'Consta que o próprio Daly confessou várias vezes ter inventado a tradução.',
    'Consta que o próprio Daly confessou várias vezes a invenção.')
substituir(16, 'explicacao',
    'por obra de gente conhecida, e não do uso espontâneo',
    'por obra de autores identificados, e não do uso espontâneo')
