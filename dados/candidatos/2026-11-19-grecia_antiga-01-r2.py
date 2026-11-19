"""Rodada 2 de Grécia antiga: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-grecia_antiga-01.py"))
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


# 0002: "talvez"
substituir(2, "explicacao", "Às vezes bastava alguém parecer proeminente demais.", "Talvez, às vezes, bastasse alguém parecer proeminente demais.")

# 0003: os navios venceram; Salamina foi a virada; morte por volta de 459
substituir(3, "gancho", "em navios e venceu os persas em Salamina.", "em navios, que venceram os persas em Salamina.")
substituir(3, "explicacao", "onde a vitória grega decidiu a guerra.", "onde a vitória grega foi a virada da guerra.")
substituir(3, "explicacao", "Morreu ali em 459 a.C.", "Morreu ali por volta de 459 a.C.")

# 0008: a maior parte do texto ainda era visível em 1906
substituir(8, "gancho", "Séculos depois, o texto apagado foi recuperado com", "Séculos depois, o que ainda estava ilegível foi revelado com")
substituir(8, "explicacao", "confirmou que sob as orações havia obras dele tidas como perdidas e fotografou as páginas.",
    "confirmou que sob as orações havia obras dele tidas como perdidas, fotografou as páginas e publicou a maior parte do texto, que ainda era visível.")
acrescentar_trecho(8, 0, "Most of the original text was still visible, and Heiberg published it in 1915")

# 0009: espetos como dinheiro ainda são debatidos
trocar(9, confianca="consenso_parcial")
substituir(9, "gancho", "os gregos usavam como dinheiro espetos", "os gregos teriam usado como dinheiro espetos")
substituir(9, "explicacao", "A arqueologia apoia a ideia.", "Achados arqueológicos são compatíveis com essa ideia, ainda debatida.")
substituir(9, "explicacao", "o mais provável é que funcionassem como dinheiro simbólico", "provavelmente funcionavam como dinheiro simbólico")

# 0013: sete hilotas por soldado em Plateia
substituir(13, "explicacao", "sete hilotas para cada espartano em 479 a.C.",
    "sete hilotas para cada um dos 5 mil soldados espartanos na batalha de Plateia, em 479 a.C.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(8, "explicacao", "fotografou as páginas e publicou a maior parte do texto", "fotografou as páginas e, em 1915, publicou a maior parte do texto")
