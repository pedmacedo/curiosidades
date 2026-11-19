"""Rodada 2 de Leis e julgamentos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-leis_julgamentos-01.py"))
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


# 0001: o porco também mutilou a criança
substituir(1, "gancho", "um porco que matou uma criança sofreu as mesmas mutilações", "um porco que matou e mutilou uma criança sofreu as mesmas mutilações")
substituir(1, "gancho", "E ratos acusados por um tribunal da Igreja ganharam defensor.", "E ratos processados pela Igreja ganharam defensor.")

# 0002: quem anulou foi Teodoro II
substituir(2, "explicacao", "Em dezembro, o papa seguinte anulou o sínodo", "Em dezembro, o papa Teodoro II anulou o sínodo")
trocar(2, tipos_espanto=["historia_humana", "contraintuitivo"])

# 0006: sem escala_absurda
trocar(6, tipos_espanto=["historia_humana"])

# 0007: no romance, o próprio Parker é o sorteado
trocar(7, gancho="Num romance de 1838, Edgar Allan Poe fez náufragos famintos sortearem qual deles viraria comida, e o sorteado "
    "se chamava Richard Parker. Em 1884, náufragos reais mataram e comeram um grumete: Richard Parker.")
substituir(7, "explicacao", "A coincidência com o romance de Poe",
    "No livro, é o próprio Parker quem sugere o sorteio, e ele acaba sorteado. A coincidência com o romance de Poe")
acrescentar_trecho(7, 1, "Parker suggests that one of them should be killed as food for the others. They draw straws and Parker is sacrificed.")

# 0012: o espanto é a ponte com a IA
trocar(12, gancho="Em 2011, macacos fizeram selfies com a câmera de um fotógrafo. A briga sobre o dono das fotos chegou à Justiça "
    "dos EUA e hoje é citada pelo governo americano ao exigir autor humano em obras feitas com IA.",
    tipos_espanto=["conexao_inesperada", "historia_humana"])

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(7, "explicacao", "No livro, é o próprio Parker quem sugere o sorteio, e ele acaba sorteado.",
    "No livro, é o próprio Parker quem propõe que um deles sirva de comida aos outros, e ele acaba sorteado.")
