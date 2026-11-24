"""Rodada 2 de Gravidez humana: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-gravidez-01.py"))
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


# 0001: a rã era um teste comum, não o único; não antecipar o fato do coelho (0003)
substituir(1, "gancho", "o teste de gravidez foi uma rã africana", "um teste de gravidez comum foi uma rã africana")
substituir(1, "explicacao",
    "Os testes anteriores usavam camundongos ou coelhos, que precisavam ser mortos para o exame; a rã podia ser reaproveitada.",
    "Ao contrário dos testes com coelhos e camundongos, a rã podia ser reaproveitada.")

# 0004: a duração do segredo sem o número de 150 anos
substituir(4, "gancho", "Por cerca de 150 anos, uma família", "Por mais de um século, uma família")

# 0005: sem o custo de 15 dólares (faltava a unidade)
substituir(5, "explicacao",
    "Em 1903, cuidar de um bebê custava em média 15 dólares, e Couney não cobrava dos pais:",
    "O tratamento era caro, mas Couney não cobrava dos pais:")

# 0009: a sincitina-2 não está em todos os primatas (falta nos prossímios)
substituir(9, "explicacao",
    "presente em todos os primatas e com idade estimada em 45 milhões de anos",
    "presente tanto nos macacos do Velho quanto nos do Novo Mundo (mas ausente nos prossímios) e com idade "
    "estimada em 45 milhões de anos")
substituir_trecho(9, 1,
    "and entered the primate genome before Syncytin-1. [...] ",
    "and entered the primate genome before Syncytin-1. "
    "Specifically, this protein entered the genome before the split between New World and Old-World Monkeys. "
    "However, this protein is absent in prosimians. [...] ")

# 0010: as duas hipóteses respondem à mesma pergunta (por que o bebê nasce imaturo)
trocar(10, gancho="A explicação clássica para o bebê humano nascer tão imaturo é o quadril estreito de quem anda em pé. "
    "Uma hipótese rival diz que o parto chega quando a mãe atinge o limite de energia que consegue gastar.")

# 0011: o "ajuste fino" é possibilidade, não posição firme
substituir(11, "gancho", "Os cientistas veem nisso um ajuste fino, como na puberdade.",
    "Para os cientistas, isso pode ser um ajuste fino, como na puberdade.")

# 0014: quase eliminada nos países ricos, não no mundo
substituir(14, "gancho", "quase eliminou uma doença que matava milhares de bebês.",
    "quase eliminou dos países ricos uma doença que matava milhares de bebês.")
substituir(14, "gancho", "que uma mãe Rh negativo", "que a mãe Rh negativo")  # para caber em 220 caracteres
