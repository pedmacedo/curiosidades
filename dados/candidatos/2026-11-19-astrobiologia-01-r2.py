"""Rodada 2 de Astrobiologia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-astrobiologia-01.py"))
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


# 0006: incluir a crítica da mesma fonte (Fermi não publicou; Sagan e a frase apócrifa; leitura de Gray)
trocar(6, tipos_espanto=["historia_humana", "origem_inesperada", "contraintuitivo"])
substituir(6, "explicacao",
    "Versões da mesma dúvida já existiam em textos de Fontenelle, de 1686, de Júlio Verne, de 1865, e do "
    "pioneiro russo dos foguetes Konstantin Tsiolkovsky, de 1933.",
    "Versões da dúvida já apareciam em Fontenelle, Júlio Verne e Tsiolkovsky. Fermi nunca publicou nada sobre o "
    "tema, e Carl Sagan chegou a sugerir que a frase seria apócrifa. Para o pesquisador Robert Gray, a leitura "
    "tradicional distorce a pergunta: Fermi estaria duvidando da viabilidade da viagem interestelar, e não da "
    "existência de extraterrestres avançados.")
acrescentar_trecho(6, 0,
    "Fermi did not publish anything regarding the paradox, with Sagan once suggesting the quote to be apocryphal. [...] "
    "According to Gray, the current understanding of the paradox misinterprets Fermi's question and subsequent discussion, "
    "which was challenging the feasibility of interstellar travel rather than the existence of advanced extraterrestrial life. [...] "
    "Scientists like Robert Gray have criticized its attribution to Fermi")

# 0010: o artigo "sugere"; "mostraram" é forte demais
substituir(10, "gancho", "grãos de gelo de Encélado mostraram que", "grãos de gelo de Encélado indicaram que")

# 0011: "sem vida nenhuma" podia soar como "Europa não tem vida"
substituir(11, "gancho", "por dia, sem vida nenhuma:", "por dia, sem precisar de seres vivos:")

# 0012: a previsão era de queda, não de sumiço; opinião de McKay no passado
trocar(12, nota_surpresa=3,
    gancho="Em 2005, previu-se que, se houvesse vida em Titã consumindo hidrogênio, o gás rarearia perto da superfície. "
           "Em 2010, dados sugeriram isso. É só hipótese: o autor da previsão achou outras causas mais prováveis.")
substituir(12, "explicacao",
    "McKay concordou que vida é uma explicação possível, mas alertou que outras são mais prováveis",
    "McKay concordou que vida era uma explicação possível, mas alertou que outras eram mais prováveis")
