"""Rodada 2 de História da música: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-historia_musica-01.py"))
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


# 0002: a sílaba do hino era "ut"; a redução do treino veio com a pauta e as sílabas
trocar(2, gancho="Ré, mi, fá, sol e lá (e o antigo \"ut\", hoje dó) saíram de um hino a São João. Com elas e com a pauta, o monge "
    "Guido d'Arezzo, no século XI, encurtou o treino de um cantor de 10 anos para um ou dois.")

# 0003: sem causalidade inventada, sem citar a fonte no texto, sem frase traduzida
substituir(3, "explicacao", "Daí nasceu a lenda de que a Igreja o teria banido, chegando a excomungar cantores.",
    "Circula a lenda de que a Igreja o teria banido, chegando a excomungar cantores.")
substituir(3, "explicacao", "Segundo o artigo da Wikipedia sobre o intervalo, essas histórias de punição são provavelmente fantasiosas.",
    "Mas essas histórias de punição são, ao que tudo indica, fantasiosas.")
substituir(3, "explicacao", "Mas não há citações conhecidas do termo na Idade Média, como se costuma afirmar.",
    "Ao contrário do que se repete, ninguém encontrou o termo em textos medievais.")

# 0004: concordância
substituir(4, "explicacao", "desses pastiches, atribuídas também", "desses pastiches, atribuídos também")

# 0007: o encontro por acaso de 1879
substituir(7, "explicacao",
    "Os dois só se viram de longe: em Florença, ele via o cortejo dela passar todas as manhãs, e uma vez se avistaram na ópera, encontro talvez arranjado por ela.",
    "Quase nunca se viram: em Florença, ele via o cortejo dela passar todas as manhãs, e uma vez se avistaram de longe na "
    "ópera, encontro talvez arranjado por ela. Em 1879, na propriedade dela, os dois se cruzaram por acaso num bosque: ele "
    "tirou o chapéu, ninguém disse nada, e à noite ele escreveu pedindo desculpas pela quebra do combinado.")
acrescentar_trecho(7, 0, "The two did meet on one occasion, purely by chance, in August 1879, while Tchaikovsky was staying at the von Meck estate at Simaki.")

# 0008: o chumbo estava por toda parte; "provavelmente"
substituir(8, "explicacao", "Na época, o chumbo vinha em quantidades bem maiores de outras fontes, como remédios e utensílios de cozinha.",
    "Na época, o chumbo estava por toda parte, de remédios a utensílios de cozinha e até à tinta que marcava as tigelas, "
    "e o pouco que viesse do vidro provavelmente era irrelevante perto disso.")

# 0009: a gravação de 1904 é posterior ao decreto de 1903
trocar(9, gancho="A voz de um castrato não é só lenda: Alessandro Moreschi, do coro da Capela Sistina, gravou discos em 1902 e "
    "1904. Foi o único castrato a gravar solos, bem quando um papa mandou trocar essas vozes por meninos.")

# 0011: o banquete de Hitler é relato não comprovado
substituir(11, "explicacao",
    "O concerto aconteceu em 9 de agosto de 1942, data que Hitler tinha escolhido para celebrar a queda da cidade com um banquete no Hotel Astoria.",
    "O concerto aconteceu em 9 de agosto de 1942. Segundo relatos, era a data que Hitler teria escolhido para celebrar a "
    "queda da cidade com um banquete no Hotel Astoria.")
acrescentar_trecho(8, 0, "would likely have been dwarfed by lead from other sources, such as the lead-content paint used to mark visual identification of the bowls to the players")
