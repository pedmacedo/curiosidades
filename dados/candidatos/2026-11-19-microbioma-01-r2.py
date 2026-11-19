"""Rodada 2 de Microbioma humano: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-microbioma-01.py"))
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


# 0005: o recorde vale para a data do estudo
substituir(5, "gancho", "o microbioma mais diverso já registrado num grupo humano", "o microbioma mais diverso registrado até então num grupo humano")
substituir(5, "explicacao", "a maior diversidade de bactérias e de funções genéticas já descrita em um grupo humano",
    "a maior diversidade de bactérias e de funções genéticas descrita até então em um grupo humano")

# 0006: quase todos raros; "difícil" prever
substituir(6, "gancho", "e a maioria só aparecia em uma pessoa.", "e quase todos eram raros, achados em poucas pessoas.")
substituir(6, "explicacao", "mas não quais bactérias uma pessoa específica teria.", "mas era difícil prever quais bactérias uma pessoa específica teria.")

# 0008: é a derrubada de uma afirmação muito divulgada
trocar(8, tipos_espanto=["contraintuitivo", "mito_desmentido"])

# 0009: bactérias de algas vermelhas; um doador aparentado da Zobellia
substituir(9, "gancho", "Os genes para isso vieram de uma bactéria marinha que vive nessas algas",
    "Os genes para isso vieram de bactérias marinhas que vivem em algas vermelhas")
substituir(9, "explicacao", "Os genes parecem ter passado de uma bactéria para a outra por transferência horizontal:",
    "Os genes parecem ter passado de uma bactéria marinha aparentada da Zobellia para a intestinal, por transferência horizontal:")
