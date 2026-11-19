"""Rodada 2 de Pintura: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-pintura-01.py"))
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


# 0008: o método dos fractais é contestado
substituir(8, "gancho", "A análise desses padrões já é usada para separar Pollocks verdadeiros de falsificações.",
    "A análise desses padrões já foi usada para flagrar Pollocks falsos, mas o método é contestado.")
substituir(8, "explicacao", "\"Eu sou a natureza\". A ideia ", "\"Eu sou a natureza\". A ideia ")
substituir(8, "explicacao",
    "Um estudo de 2015, que combinou essa e outras técnicas, acertou 93% das vezes ao separar Pollocks "
    "verdadeiros de falsos.",
    "Um estudo de 2015, que combinou essa e outras técnicas, acertou 93% das vezes ao separar Pollocks "
    "verdadeiros de falsos. Mas o método tem críticos. Em 2006, a física Katherine Jones-Smith e colegas "
    "argumentaram na revista Nature que a análise era falha: um desenho tosco de estrelas feito por ela "
    "passou no teste como se fosse um Pollock. Depois, aplicaram a análise a pinturas de respingo "
    "encomendadas a artistas locais e a três Pollocks indiscutíveis: as duas imitações deram resultado "
    "fractal, e só um dos três Pollocks verdadeiros.")
CANDIDATOS[7]["fontes"].append({
    "url": "https://www.sciencenews.org/article/never-mind-pollock-fractals",
    "titulo": "Never mind the Pollock fractals",
    "idioma": "en",
    "trecho": "In a brief response published in Nature in 2006, Jones-Smith and her colleagues argued that the analysis was flawed. "
        "The centerpiece of the claim was a crude drawing of stars made by Jones-Smith. "
        "According to fractal analysis, Jones-Smith’s childish drawing was an authentic Pollock painting. [...] "
        "In the new research, Jones-Smith and colleagues commissioned local painters to create drip paintings in the size and style of Pollock. "
        "The researchers applied fractal analyses to two such paintings, and three undisputed Pollock paintings. "
        "Both of the two commissioned drip paintings turned out to be fractal, and thus, appeared to be authentic Pollocks. "
        "Meanwhile, only one of three undisputed Pollocks was fractal.",
})

# 0009: não há prova de que Vermeer e Leeuwenhoek se conhecessem
trocar(9, gancho="Vermeer teria usado uma câmara escura para pintar? A ideia divide estudiosos. Leeuwenhoek, pioneiro das lentes, administrou os bens da família após sua morte, mas o inventário não lista nenhuma lente.")
substituir(9, "explicacao",
    "Ele era próximo de Antonie van Leeuwenhoek, pioneiro na fabricação de lentes, que foi o inventariante de "
    "seus bens, e o inventário detalhado feito após sua morte não lista nenhuma câmara escura, lente ou "
    "aparelho parecido.",
    "Curiosamente, depois de sua morte os bens da família ficaram a cargo de Antonie van Leeuwenhoek, "
    "pioneiro na fabricação de lentes, mas o inventário detalhado feito após a morte do pintor não lista "
    "nenhuma câmara escura, lente ou aparelho parecido.")
