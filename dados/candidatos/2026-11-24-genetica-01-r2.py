"""Rodada 2 de Genética: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-genetica-01.py"))
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


# 0001: o crédito de Tschermak não é mais aceito; Hartl e Fairbanks rejeitam a análise de Fisher
substituir(1, "explicacao",
    "Em 1900, Hugo de Vries, Carl Correns e Erich von Tschermak, cada um num país, confirmaram por conta própria vários "
    "resultados dele e publicaram a redescoberta num intervalo de dois meses.",
    "Em 1900, Hugo de Vries e Carl Correns chegaram por conta própria a resultados parecidos e, junto com Erich von "
    "Tschermak (cujo crédito pela redescoberta hoje não é mais aceito), publicaram a redescoberta num intervalo de "
    "dois meses.")
substituir(1, "explicacao",
    "Várias explicações já foram propostas, entre elas o viés de confirmação, e o caso segue em discussão.",
    "Várias explicações já foram propostas, entre elas o viés de confirmação. Já os geneticistas Daniel Hartl e "
    "Daniel Fairbanks rejeitam a análise de Fisher: para eles, Fisher interpretou mal os experimentos, e um livro de "
    "2008 escrito por eles com outros autores concluiu que não há motivo para dizer que Mendel inventou os dados.")
substituir_trecho(1, 0,
    "Erich von Tschermak, Hugo de Vries and Carl Correns independently verified several of Mendel's experimental findings in 1900 [...] ",
    "independent duplication of his work by Hugo de Vries and Carl Correns and the rediscovery of Mendel's writings and laws. [...] "
    "Though Erich von Tschermak was originally also credited with rediscovery, this is no longer accepted because he did not understand Mendel's laws. [...] ")
acrescentar_trecho(1, 0,
    "Daniel L. Hartl and Daniel J. Fairbanks reject Fisher's statistical argument outright, suggesting that Fisher incorrectly interpreted Mendel's experiments. [...] "
    "In 2008 Hartl and Fairbanks (with Allan Franklin and AWF Edwards) wrote a comprehensive book in which they concluded that there were no reasons to assert Mendel fabricated his results")

# 0002 (aprovado): troca opcional
substituir(2, "explicacao", "dono do laboratório", "chefe do laboratório")

# 0003: o recorde de 160 bilhões é da Tmesipteris oblanceolata (2024)
substituir(3, "explicacao",
    "Depois disso, mediu-se uma samambaia, Tmesipteris truncata, com cerca de 160 bilhões.",
    "Em 2024, uma pequena samambaia da Nova Caledônia, Tmesipteris oblanceolata, tomou o recorde, com cerca de 160 "
    "bilhões.")
substituir_trecho(3, 1,
    " Since then, other organisms have been assayed and reported to have larger genomes;  The fork fern, Tmesipteris truncata has 160.45 billion base pairs per cell.",
    "")
CANDIDATOS[2]["fontes"].append(
    {"url": "https://www.sciencenews.org/article/largest-genome-tiny-fern",
     "titulo": "The largest known genome belongs to a tiny fern (Science News, 2024)",
     "idioma": "en",
     "trecho": (
        "By Jake Buehler May 31, 2024 [...] "
        "Tmesipteris oblanceolata (the small green plants), one of six fork fern species from New Caledonia assessed in a new study, has a record-breaking genome that contains 160 billion bases. [...] "
        "And it’s about 7 percent larger than the genome of the previous record holder, a Japanese flower dubbed Paris japonica. [...] "
        "One species — T. oblanceolata — has the largest genome of any organism yet measured. "
        "The fern mainly grows on larger forest plants and is up to only 15 centimeters long. "
        "But its genome has a length of 160 billion nucleobases"
     )})

# 0004: faixa de 3% a 8%; a interferência no HIV foi vista em experimentos
substituir(4, "gancho", "Entre 5% e 8% do DNA humano é feito de restos de vírus",
    "Algo entre 3% e 8% do DNA humano é feito de restos de vírus")
substituir(4, "explicacao",
    "e uma proteína da HERV-K se mistura à do HIV e atrapalha a montagem da cápsula desse vírus",
    "e, em experimentos, uma proteína da HERV-K se mistura à proteína equivalente do HIV e atrapalha a montagem da "
    "cápsula desse vírus")

# 0008: "burglaries" são invasões; a estimativa vale para as buscas, não para qualquer pessoa
substituir(8, "explicacao", "e pelo menos 120 roubos", "e pelo menos 120 invasões de casas")
substituir(8, "explicacao", "uma busca desse tipo, para qualquer pessoa de ascendência europeia, acharia",
    "uma busca desse tipo, para uma pessoa de ascendência europeia, acharia")

# 0009: "algumas" populações; variantes associadas, não causais comprovadas
substituir(9, "explicacao", "Em populações do leste da África, a persistência foi",
    "Em algumas populações do leste da África, a persistência foi")
substituir(9, "explicacao", "As variantes responsáveis não ficam no gene da lactase",
    "As variantes associadas a ela não ficam no gene da lactase")

# 0011: a linhagem CHM13 tem as duas cópias idênticas de cada cromossomo
substituir(11, "explicacao",
    "Também usou uma linhagem de células com só uma cópia de cada cromossomo, quando a maioria das células humanas tem duas.",
    "Também usou uma linhagem de células em que as duas cópias de cada cromossomo são idênticas, o que evita misturar "
    "as duas versões diferentes que a maioria das células humanas carrega.")
substituir_trecho(11, 0,
    "Researchers generated the complete genome sequence using a human cell line with only one copy of each chromosome, unlike most human cells, which carry two copies of each chromosome. [...] ",
    "[...] ")
acrescentar_trecho(11, 1, "a hydatidiform mole-derived cell line in which both copies of each chromosome are identical")

# 0014: cronologia — o teste do intestino veio antes dos corpos de 2007
substituir(14, "explicacao",
    "Os dois últimos corpos apareceram em 2007, e testes repetidos mostraram que nenhuma das quatro filhas sobreviveu. "
    "Restava um trecho de intestino de Anderson, retirado numa cirurgia em 1979 e guardado num hospital da Virgínia. O "
    "DNA dele não batia com o dos Romanov, mas batia com o de Karl Maucher, neto de uma irmã de Franziska "
    "Schanzkowska.",
    "Um trecho de intestino de Anderson, retirado numa cirurgia em 1979 e guardado num hospital da Virgínia, foi "
    "comparado com esse DNA: não batia com o dos Romanov, mas batia com o de Karl Maucher, neto de uma irmã de "
    "Franziska Schanzkowska. Mais tarde, em 2007, apareceram os dois últimos corpos, e testes repetidos mostraram que "
    "nenhuma das quatro filhas sobreviveu.")
