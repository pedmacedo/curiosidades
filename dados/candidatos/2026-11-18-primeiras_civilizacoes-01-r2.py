"""Rodada 2 de Primeiras civilizações: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-primeiras_civilizacoes-01.py"))
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

# 0005: o "museu" é interpretação de Woolley
trocar(5, confianca="consenso_parcial")
substituir(5, "gancho", "Sua filha montou o museu público mais antigo que se conhece, com etiquetas de barro em três línguas.",
    "A coleção de antiguidades da filha dele é tida como o museu mais antigo que se conhece.")
substituir(5, "explicacao", "Concluiu que eram peças de museu porque vinham com \"etiquetas\": cilindros de barro escritos em três línguas, uma delas o sumério.",
    "Concluiu que eram peças de museu por causa de cilindros de barro inscritos, que ele interpretou como \"etiquetas de museu\". "
    "É uma leitura dele: não se sabe ao certo como a coleção era usada.")

# 0006: os três quartos são da cultura de Uruk, e as tigelas, do 4º milênio
trocar(6, gancho="Uruk, provavelmente a maior cidade do mundo por volta de 3100 a.C., deu nome a uma cultura cujo objeto mais típico "
    "é uma tigela tosca, feita em massa e descartada aos montes: uns três quartos de toda a sua cerâmica.")
substituir(6, "explicacao", "Mas o que os arqueólogos mais acham ali é bem mais humilde: as tigelas de borda chanfrada.",
    "Mas o que os arqueólogos mais acham nos sítios da cultura de Uruk, sobretudo do 4º milênio a.C., é bem mais humilde: as tigelas de borda chanfrada.")

# 0007: "muito procurados"; Innaya "envolvido" no processo
substituir(7, "gancho", "fazia tecidos de luxo em Assur", "fazia tecidos muito procurados em Assur")
substituir(7, "explicacao", "Também tratou com as autoridades de um processo contra Innaya por vendas suspeitas de lápis-lazúli.",
    "Também tratou com as autoridades de um processo em que Innaya estava envolvido, sobre vendas suspeitas de lápis-lazúli.")

# 0014: "da época"; sem mito_desmentido
trocar(14, tipos_espanto=["misterio_aberto"])
substituir(14, "gancho", "e nenhum texto babilônico os menciona", "e nenhum texto babilônico da época os menciona")

# 0016: "provável única rainha"; o porquê do dilúvio na lista
substituir(16, "gancho", "e a única rainha citada nela aparece como \"a taberneira\"", "e a provável única rainha citada nela aparece como \"a taberneira\"")
acrescentar_trecho(16, 0, "By inserting a section of primordial kings who ruled before a flood, which is only known from some Old Babylonian versions, the importance of Kish could be downplayed.")
substituir(16, "explicacao", "Mashda, por exemplo, teria reinado 840 anos.",
    "Mashda, por exemplo, teria reinado 840 anos. A seção dos reis anteriores ao dilúvio só aparece em algumas versões do "
    "período babilônico antigo e talvez tenha sido inserida para diminuir a importância de Kish.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(5, "explicacao", "É uma leitura dele: não se sabe ao certo como a coleção era usada.",
    "Toda essa reconstrução, inclusive o uso didático da coleção, se apoia na leitura de Woolley.")
