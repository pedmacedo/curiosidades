"""Rodada 2 de Revoluções políticas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-revolucoes_politicas-01.py"))
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


# 0002: as últimas palavras de Adams são contestadas
substituir(2, "gancho", "Últimas palavras de Adams: \"Jefferson sobrevive\".", "Adams teria dito no fim: \"Jefferson sobrevive\".")
substituir(2, "explicacao", "Entre suas últimas palavras, lembrou o amigo e rival: \"Thomas Jefferson sobrevive\".",
    "Segundo relatos, entre suas últimas palavras estava o nome do amigo e rival, numa frase registrada como \"Thomas Jefferson sobrevive\".")

# 0004: a meia folga do quíntidi dava mais descanso no total
trocar(4, gancho="No calendário da Revolução Francesa, a semana tinha dez dias, e cada dia ganhou nome de planta, bicho, mineral "
    "ou ferramenta. Os trabalhadores reclamaram da folga a cada dez dias, embora descansassem mais no ano.")
substituir(4, "explicacao", "e não a cada sete,",
    "e não a cada sete, embora ganhassem também meia folga no quíntidi, o quinto dia, o que somava 54 dias livres por ano, "
    "contra os 52 ou 53 domingos de antes;")
acrescentar_trecho(4, 0, "although they also got a half-day off on the fifth day (thus 36 full days and 36 half days in a year, for a total of 54 free days, compared to the usual 52 or 53 Sundays)")

# 0010: o número de desertores é incerto
substituir(10, "gancho", "Centenas mudaram de lado, e o novo país lhes deu cidadania.", "Parte deles mudou de lado, e o novo país deu cidadania aos poloneses.")
substituir(10, "explicacao", "e uns 500 acabaram passando para o lado dos rebeldes.",
    "e uma parte deles acabou passando para o lado dos rebeldes (quantos, os historiadores divergem).")

# 0011: Trótski fala dos revolucionários
substituir(11, "explicacao", "Trótski escreveu depois que ninguém imaginava", "Trótski escreveu depois que os revolucionários não imaginavam")

# 0013: o acidente precipitou o levante; o fim do império foi a abdicação
substituir(13, "gancho", "começou por acidente", "foi precipitada por um acidente")
substituir(13, "explicacao", "Terminavam ali mais de 2.000 anos de governo imperial.",
    "Em 12 de fevereiro de 1912, o trono Qing abdicou em nome do imperador Puyi, encerrando mais de 2.000 anos de governo imperial.")
acrescentar_trecho(13, 0, "On 12 February 1912, Empress Dowager Longyu, on behalf of Puyi, the Xuantong Emperor, announced the abdication of the Qing throne, marking the end of the dynasty.")

# 0014: só os primeiros cravos vieram do restaurante
substituir(14, "gancho", "E os cravos eram de um restaurante", "E os primeiros cravos vieram de um restaurante")
