"""Rodada 2 de Consciência: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-consciencia-01.py"))
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

import re

# 0001: sem assumir que o sinal "prepara" o gesto
substituir(1, "gancho", "a atividade cerebral que prepara um gesto simples começou centenas de milissegundos antes",
    "um sinal cerebral ligado a um gesto simples surgiu centenas de milissegundos antes")

# 0002: presença e localização, não identificação
substituir(2, "explicacao", "eles conseguiam indicar objetos em qualquer parte do campo visual com qualquer uma das mãos ou falando",
    "eles conseguiam dizer se havia um objeto e onde ele estava, em qualquer parte do campo visual, respondendo com qualquer uma das mãos ou falando")

# 0004: "mais debatidas"
substituir(4, "gancho", "uma das mais citadas sobre a consciência", "uma das mais debatidas sobre a consciência")

# 0008: "não parece decorrer diretamente"
substituir(8, "explicacao", "e não se explica por perda de sensação: o dano estaria nos processos",
    "e não parece decorrer diretamente da perda de sensação: o dano estaria nos processos")

# 0009: sem o par 45%/55% (leitura errada da fonte)
substituir(9, "explicacao", " Numa análise de cem pacientes, 45% negavam a própria existência; os demais tinham delírios de imortalidade.", "")
_f = CANDIDATOS[8]["fontes"][0]
_f["trecho"] = re.sub(r"\s*(\[\.\.\.\]\s*)?Statistical analysis of a hundred-patient cohort[^.]*\.[^.]*immortality\.", "", _f["trecho"])

# 0010: gancho sem a impressão contestada de Galton; pesquisa moderna desde 2005
trocar(10, gancho="Imagine uma maçã vermelha. Algumas pessoas não veem nada: não conseguem formar imagens na mente, e muita gente "
    "se espanta ao descobrir que isso não é universal. A condição só ganhou nome, afantasia, em 2015.")
substituir(10, "explicacao", "Tudo começou em 2005", "A pesquisa moderna começou em 2005")
substituir(10, "explicacao",
    " Galton se espantou porque a maioria dos cientistas que consultou primeiro garantia não conhecer imagens mentais e o tomava por fantasioso; ele os comparou a um daltônico que nunca percebeu o próprio defeito.", "")

# 0012: a virada não foi em 2023
substituir(12, "gancho", "Em 2023, o autor disse não aceitar mais o próprio argumento.", "Anos depois, o próprio autor abandonou o argumento.")
substituir(12, "explicacao", "Jackson passou a se declarar fisicalista e, em 2023, afirmou que não aceita mais o argumento.",
    "Jackson acabou se declarando fisicalista e, numa entrevista de 2023, disse que não aceita mais o argumento.")

# 0013: "uns 20 km"
substituir(13, "gancho", "dirigiu 20 km de madrugada", "dirigiu uns 20 km de madrugada")

# 0015: a questão segue debatida
trocar(15, confianca="consenso_parcial")
substituir(15, "gancho", "Jovens operados entre 2007 e 2010 deram a resposta: não de imediato.", "Jovens operados entre 2007 e 2010 sugerem que não, ao menos de imediato.")
substituir(15, "explicacao", "Ou seja, não havia transferência inata do tato para a visão.", "Os pesquisadores concluíram que a resposta a Molyneux é, em resumo, não.")
substituir(15, "explicacao", "A ponte entre os sentidos, ao que parece, é aprendida.",
    "A ponte entre os sentidos, ao que parece, se aprende rápido, embora haja quem conteste a interpretação do estudo.")
_f["trecho"] = _f["trecho"].replace("Statistical analysis of a hundred-patient cohort indicated that denial of self-existence is present in 45% of the cases of Cotard's syndrome; the other 55% of the patients presented with delusions of immortality. ", "")
