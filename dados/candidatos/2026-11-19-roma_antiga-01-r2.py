"""Rodada 2 de Roma antiga: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-roma_antiga-01.py"))
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


# 0007: o nome já existia em 1616 e se firmou no século XIX
substituir(7, "gancho", "ganhou o nome no século XIX por uma teoria sobre onde Roma perdeu três legiões",
    "foi batizada assim por causa de uma teoria sobre onde Roma perdeu três legiões")
substituir(7, "explicacao", "No século XIX, uma teoria venceu o debate, e uma serra chamada Osning, perto de Bielefeld, foi rebatizada de Floresta de Teutoburgo.",
    "Uma teoria venceu o debate, e uma serra chamada Osning, perto de Bielefeld, acabou rebatizada de Floresta de Teutoburgo, nome que se firmou no século XIX.")

# 0009: objeções, não "todas têm problemas"; a leitura ligada a moedas
trocar(9, tipos_espanto=["misterio_aberto", "contraintuitivo"])
substituir(9, "explicacao", "Todas têm problemas.", "Várias delas esbarram em objeções.")
substituir(9, "explicacao", "brinquedo, objeto de adivinhação", "brinquedo, cabeça de arma, objeto de adivinhação")
substituir(9, "explicacao", "Algumas apareceram em tesouros de moedas, sinal de que os donos as consideravam valiosas.",
    "Algumas apareceram em tesouros de moedas, o que sugere que os donos as consideravam valiosas, ou que o uso delas tinha a ver com moedas.")

# 0011: os jarros só sugerem a vindima passada
substituir(11, "explicacao", "grandes jarros cheios de vinho, sinal de que a uva já tinha sido colhida",
    "grandes jarros cheios de vinho, o que sugere que a vindima já tinha passado")

# 0012: a maioria das inscrições; a prática era geral; o motivo do dono é hipótese
substituir(12, "explicacao", "e o nome e o título dele foram apagados das inscrições", "e o nome e o título dele foram apagados da maioria das inscrições")
substituir(12, "explicacao",
    "Fontes antigas registram que essas imagens eram besuntadas de lama, vísceras, tinta e até excremento, e o tondo é uma das raras obras sobreviventes que mostram uma desfiguração desse tipo.",
    "Fontes antigas registram que imagens de condenados podiam ser besuntadas de lama, vísceras, tinta e até excremento, e o "
    "tondo é uma das raras obras sobreviventes que mostram a desfiguração física de um condenado.")
substituir(12, "explicacao", "Para o dono, raspar o rosto era um jeito", "Para o dono, raspar o rosto seria um jeito")
