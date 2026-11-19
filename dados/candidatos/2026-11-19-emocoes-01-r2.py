"""Rodada 2 de Emoções: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-emocoes-01.py"))
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


# 0002: sem "planícies estrangeiras"; a proibição das canções vem de relatos
substituir(2, "explicacao", "que, lutando nas planícies estrangeiras, definhavam de saudade das montanhas",
    "que, servindo longe de casa, definhavam de saudade das paisagens da terra natal")
substituir(2, "gancho", "Certas canções da terra natal eram proibidas a eles.", "Certas canções da terra natal teriam sido proibidas a eles.")
substituir(2, "explicacao", "As canções suíças chamadas Ranz des vaches, ou Kuhreihen, eram proibidas aos mercenários",
    "Segundo relatos da época, as canções suíças chamadas Ranz des vaches, ou Kuhreihen, eram proibidas aos mercenários")

# 0007: sem replicação independente; a leitura como ansiedade é debatida
trocar(7, confianca="consenso_parcial")

# 0008: concordância
substituir(8, "gancho", "já a retratavam como ameaça", "já o retratavam como ameaça")

# 0009: a falta de emoção sozinha não basta para o delírio
substituir(9, "explicacao", "A pessoa reconhece o rosto, sente que algo não está certo e conclui que é um impostor.",
    "A pessoa reconhece o rosto, sente que algo não está certo e conclui que é um impostor. Só a falta da reação "
    "emocional, porém, não basta: o mesmo padrão já foi visto em pessoas sem delírio, e por isso se propõe um segundo "
    "fator, uma falha no raciocínio que transforma a estranheza em crença.")
acrescentar_trecho(9, 0, "Most likely, more than a mere impairment of the automatic emotional arousal response is necessary to form the Capgras delusion, as the same pattern has been reported in patients showing no signs of delusions.")
