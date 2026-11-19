"""Rodada 2 de Egito antigo: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-egito_antigo-01.py"))
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


# 0003: artistas da Europa Ocidental; pré-rafaelitas como uma das cores favoritas (os dois já estão no trecho)
substituir(3, "explicacao",
    "A cor fez sucesso de meados do século XVIII ao XIX, sobretudo entre os pré-rafaelitas.",
    "A cor fez sucesso de meados do século XVIII ao XIX entre artistas da Europa Ocidental e foi uma das "
    "favoritas dos pré-rafaelitas.")

# 0004: "muitos" em vez de todos; Saqqara como estimativa (trecho já cobre "temple grounds" e "is estimated")
substituir(4, "explicacao",
    "Os bichos eram criados nos próprios templos e vendidos já mumificados a peregrinos e moradores.",
    "Muitos bichos eram criados nos terrenos dos templos e vendidos já mumificados a peregrinos e moradores.")
substituir(4, "explicacao", "sugerem que eles eram criados só para isso", "sugerem que muitos eram criados só para isso")
substituir(4, "explicacao", "Saqqara guarda quase 500 mil delas e teria produzido",
    "Estima-se que Saqqara guarde quase 500 mil delas e tenha produzido")

# 0010: "quase sem magia" (exceções nos casos 8 e 9, já no trecho); a razão de ser manual de guerra
substituir(10, "gancho", "descreve 48 casos de ferimentos sem recorrer à magia",
    "descreve 48 casos de ferimentos quase sem recorrer à magia")
substituir(10, "explicacao", "Por isso se pensa que era um manual para feridas de guerra.",
    "Pelo caráter prático e pelos tipos de trauma descritos, acredita-se que fosse um manual para feridas de guerra.")

# 0012: "última inscrição conhecida"; fechamento dos templos ordenado por Teodósio
substituir(12, "gancho", "A última inscrição em hieróglifos é de 394 d.C.",
    "A última inscrição conhecida em hieróglifos é de 394 d.C.")
substituir(12, "explicacao",
    "Em 391, o imperador romano Teodósio I fechou os templos não cristãos, e o uso monumental da escrita acabou;",
    "Em 391, o imperador romano Teodósio I ordenou o fechamento dos templos não cristãos, e o uso monumental "
    "da escrita cessou depois disso;")

# 0013: a língua dos escribas era "provavelmente" um proto-cananeu (trecho já tem "probably spoke")
substituir(13, "explicacao", "vem cheio de marcas da língua materna deles, um ancestral das línguas",
    "vem cheio de marcas da língua materna deles, provavelmente um ancestral das línguas")
