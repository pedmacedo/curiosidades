"""Rodada 2 de Remédios e venenos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-farmacos-01.py"))
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


# 0003: sem "primeira"; os sucessores famosos derivam do GLP-1 humano, não do lagarto
trocar(3, nota_surpresa=4, gancho="Os remédios contra diabetes e obesidade que imitam o hormônio GLP-1 devem muito a um lagarto venenoso, "
    "o monstro-de-gila: a exenatida, aprovada em 2005, é a versão sintética de uma molécula do veneno dele.")
substituir(3, "explicacao",
    "levou outras empresas a investir nessa classe, hoje usada contra diabetes tipo 2 e obesidade.",
    "levou outras empresas a investir nessa classe, hoje usada contra diabetes tipo 2 e obesidade. Os sucessores "
    "mais famosos, porém, não vêm do lagarto: a liraglutida, por exemplo, foi derivada do próprio GLP-1 humano.")
CANDIDATOS[2]["fontes"].append(wiki("Liraglutide",
    "Liraglutide is an acylated glucagon-like peptide-1 (GLP-1) receptor agonist, derived from human GLP-1-(7-37), a less common form of endogenous GLP-1.",
    nome="Liraglutide"))

# 0005: alerta de 1802 sem "tantas"; a Allergan comprou a empresa depois da aprovação
substituir(5, "explicacao",
    "No sul da Alemanha, as intoxicações por salsicha eram tantas que, em 1802, as autoridades de Württemberg alertaram",
    "No sul da Alemanha, depois de vários casos fatais de intoxicação, as autoridades de Württemberg alertaram, em 1802,")
substituir(5, "explicacao",
    "Em 1989, a empresa dele, já comprada pela Allergan, foi aprovada nos EUA, e a Allergan passou a usar a marca Botox.",
    "Em 1989, o Oculinum foi aprovado nos EUA para estrabismo e piscar involuntário; a empresa de Scott logo foi "
    "comprada pela Allergan, que passou a usar a marca Botox.")

# 0006: inventados são o nome e a figura; hidropisia é acúmulo de líquido
trocar(6, nota_surpresa=3)
substituir(6, "gancho", "nunca existiu: ela foi criada em 1928 para a propaganda de um laboratório.",
    "é invenção: nome e figura surgiram em 1928 na propaganda de um laboratório.")
substituir(6, "explicacao", "contra a hidropisia, o inchaço causado pela insuficiência cardíaca,",
    "contra a hidropisia, o acúmulo de líquido no corpo, muitas vezes ligado à insuficiência cardíaca,")
acrescentar_trecho(6, 0, "dropsy (swelling from congestive heart failure)")

# 0007: a origem do nome Aspirin, nos termos da fonte
substituir(7, "explicacao",
    "O princípio ativo, o ácido salicílico, foi extraído em 1839 de outra planta, a ulmária, chamada em alemão de Spirsäure, e esse nome serviu de base para batizar a Aspirin.",
    "O princípio ativo, o ácido salicílico, foi extraído em 1839 de outra planta, a ulmária, então classificada no "
    "gênero Spiraea (hoje Filipendula). O nome Aspirin junta o \"a\" de acetil, o \"spir\" do termo alemão "
    "Spirsäure, ligado a esse gênero, e o sufixo \"-in\", comum nos remédios da época.")
acrescentar_trecho(7, 0,
    "The name is ultimately a blend of the prefix a(cetyl) + spir, from Spirsäure, German for meadowsweet, the plant genus from which the aspirin precursor salicylic acid was first isolated (originally Spiraea, now Filipendula) + -in, the common suffix for drugs near the end of the 19th century.")

# 0010: "o primeiro" amortecido
substituir(10, "gancho", "O primeiro remédio eficaz contra uma doença mental surgiu numa despensa:",
    "O remédio tido como o primeiro eficaz contra uma doença mental surgiu numa despensa:")

# 0011: o comunicado é do Nobel de Medicina, não da Fundação Nobel
substituir(11, "explicacao", "Segundo a Fundação Nobel, ele se recusou a tomá-la",
    "Segundo o comunicado oficial do Nobel de Medicina de 1998, ele se recusou a tomá-la")

# 0014: "sugeriram", como na fonte
substituir(14, "explicacao",
    "que alivia a dor tão bem quanto ela, e que o problema no sangue vinha de outro derivado.",
    "que alivia a dor tão bem quanto ela, e sugeriram que o problema no sangue vinha sobretudo de outro derivado.")
