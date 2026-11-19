"""Rodada 2 de Grandes obras: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-grandes_obras-01.py"))
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


# 0003: "quase 1 metro"; amortecedores sem atribuí-los às torres nem ao vento
substituir(3, "gancho", "o vão central teve de ficar 1 metro mais longo do que o projetado",
    "o vão central teve de ficar quase 1 metro mais longo do que o projetado")
substituir(3, "explicacao", "de modo que o vão central precisou crescer 1 metro",
    "de modo que o vão central precisou crescer quase 1 metro")
substituir(3, "explicacao",
    "Para enfrentar o vento, as torres têm amortecedores ajustados para operar na frequência de ressonância da ponte.",
    "A ponte também tem amortecedores de massa ajustados para operar na frequência de ressonância da própria "
    "estrutura, o que reduz as vibrações.")

# 0004: o erro é a ressonância forçada clássica
substituir(4, "gancho", "aparece em livros de física como exemplo de ressonância. A explicação está errada:",
    "aparece em livros de física como exemplo de ressonância forçada. Essa explicação está errada:")

# 0006: na hora do desastre o lago estava sendo baixado, não enchido
substituir(6, "explicacao",
    "Em 9 de outubro de 1963, durante o enchimento do lago, a encosta desabou no reservatório.",
    "Em 9 de outubro de 1963, cerca de duas semanas depois de a operadora decidir baixar aos poucos o nível do "
    "lago, a encosta desabou no reservatório.")
acrescentar_trecho(6, 0, "On 26 September 1963, ENEL decided to slowly empty the basin to 240 m (790 ft).")

# 0008: a inversão de 1900 foi a definitiva; 51 km é o sistema ampliado
substituir(8, "gancho", "Em 1900, Chicago fez seu rio correr ao contrário:",
    "Em 1900, Chicago fez seu rio correr ao contrário de vez:")
substituir(8, "explicacao", "O plano foi cortar essa divisa com um canal de 51 km.",
    "O plano foi cortar essa divisa com um canal, que depois foi ampliado e hoje forma um sistema de 51 km.")
acrescentar_trecho(8, 0, "the flow of the river had already been reversed in 1871 when the Illinois and Michigan Canal was deepened enough to reverse the river's flow for one season. [...] "
    "Further construction from 1903 to 1907 extended the canal to Joliet")

# 0011: Emily fez boa parte do trabalho; Washington seguiu como engenheiro-chefe
substituir(11, "gancho", "Quem tocou a construção por uma década foi a nora, Emily Roebling.",
    "Por uma década, a nora, Emily, fez boa parte do trabalho de engenheiro-chefe.")

# 0014: comprimento pelo dado de 33.113 m em 427 poços; o "ainda" fica como registro da fonte
trocar(14, gancho="No Irã, o qanat de Gonabad, rede de túneis de água de cerca de 2.700 anos, consta como fonte de água "
    "para quase 40 mil pessoas. A água corre por mais de 33 km de galerias subterrâneas, só pela gravidade.")
substituir(14, "explicacao", "tem 45 km, e seu poço principal passa de 360 metros de profundidade",
    "soma mais de 33 km de galerias e 427 poços")
substituir_trecho(14, 0,
    "Its main well depth is more than 360 meters (1,180 ft) and its length is 45 kilometers (28 mi). [...] ", "[...] ")
substituir_trecho(14, 0,
    "is one of the oldest and largest qanats in the world built between 700 BCE to 500 BCE. [...] ",
    "is one of the oldest and largest qanats in the world built between 700 BCE to 500 BCE. [...] "
    "This property contains 427 water wells with total length of 33,113 m (20.575 miles). [...] ")
