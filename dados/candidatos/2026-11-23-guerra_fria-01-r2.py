"""Rodada 2 de Guerra Fria: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-23-guerra_fria-01.py"))
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


# 0002: a intenção do capitão vem de depoimentos; "podia ter começado"
trocar(2, gancho="Em 1962, navios dos EUA soltaram cargas de sinalização perto de um submarino soviético com torpedo "
    "nuclear. Segundo tripulantes, o capitão achou que a guerra podia ter começado e quis disparar. Um oficial se opôs.")

# 0007: Wallace era diretor do Office of Technical Service; o relato de Marchetti é anterior a 2001
substituir(7, "gancho", "Um ex-dirigente da agência contestou", "Um ex-diretor técnico da CIA contestou")
substituir(7, "explicacao", "O caso veio a público em 2001, com a liberação de documentos da CIA.",
    "Os documentos da CIA sobre o projeto só foram liberados em 2001.")

# 0008: quem sabia era a KGB; os EUA bancaram a maior parte
substituir(8, "gancho", "Os soviéticos sabiam de tudo desde o início, por um espião, e deixaram.",
    "A KGB sabia de tudo desde o início, por um espião, e deixou.")
substituir(8, "explicacao", "Os americanos financiaram e cavaram o túnel",
    "Os americanos bancaram a maior parte e cavaram o túnel")

# 0010: tirar a interpretação editorial sobre as duas versões
trocar(10, nota_surpresa=3)
substituir(10, "explicacao", "As duas versões não chegam a se contradizer: a Força Aérea fala de mísseis que nunca foram "
    "de fato disparados; Blair, de qual era o código. ", "")
substituir_trecho(10, 0, " The Air Force's statement (that 00000000 was never used to enable an ICBM, i.e. the weapons "
    "were not actually launched) does not contradict Blair's statement (that 00000000 was the code for doing so).", "")

# 0015: o Alvin achou a bomba em março; os 80 dias vão até o içamento
substituir(15, "explicacao", "Depois de 80 dias, o submersível Alvin encontrou a bomba.",
    "O submersível Alvin localizou a bomba em março, e ela foi içada intacta depois de 80 dias de busca.")
