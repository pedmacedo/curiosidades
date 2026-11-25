"""Rodada 2 de Pigmentos e cores da arte: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-pigmentos-01.py"))
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


# notas dos aprovados sem mudança
trocar(2, nota_surpresa=5)
trocar(7, nota_surpresa=3)
trocar(10, nota_surpresa=3)
trocar(12, nota_surpresa=3)
trocar(15, nota_surpresa=3)

# 0001: 1814 foi um passo decisivo, não o começo
substituir(1, "explicacao",
    "A virada começou com um acaso: em 1814, um composto azul muito parecido surgiu sozinho num forno de cal da fábrica de vidros e espelhos Saint-Gobain.",
    "Um passo decisivo veio de um acaso: em 1814, um composto azul muito parecido surgiu sozinho num forno de cal da fábrica de vidros e espelhos Saint-Gobain.")

# 0003: deu nome ao ácido prússico (não ao cianeto); "boa parte" do césio já tinha migrado
substituir(3, "gancho", "O pigmento deu nome ao cianeto e hoje é antídoto contra césio radioativo.",
    "Deu nome a um veneno, o ácido prússico, e hoje é antídoto contra césio radioativo.")
substituir(3, "explicacao", "embora parte do material já tivesse passado do sangue para os músculos",
    "embora boa parte do material já tivesse passado do sangue para os músculos")

# 0004: o slogan "primeiro azul novo em dois séculos" é exagerado (azul de manganês de 1907)
trocar(4, nota_surpresa=3,
    gancho="Em 2009, um químico que buscava um material para eletrônicos tirou do forno um azul vivo. A universidade anunciou o YInMn, de ítrio, índio e manganês, como o primeiro azul novo em dois séculos, com exagero.")
substituir(4, "explicacao", "não teria notado o potencial comercial.",
    "não teria notado o potencial comercial. O slogan da universidade, \"primeiro azul novo em dois séculos\", é "
    "generoso: o azul de manganês, por exemplo, foi desenvolvido em 1907 e acabou abandonado pela indústria por "
    "questões de segurança.")
acrescentar_trecho(4, 1, "Synthetic alternatives, such as barium manganate sulfate (or Manganese Blue, developed in 1907 and patented in 1935), have been phased out industrially due to safety and regulatory concerns")

# 0006: Monghyr fica no nordeste de Bihar; ácido hipúrico em parte das amostras
substituir(6, "explicacao", "investigou a produção em Monghyr, no nordeste da Índia",
    "investigou a produção em Monghyr, no nordeste do estado de Bihar, na Índia")
substituir(6, "explicacao", "confirmaram a origem animal: acharam ácido hipúrico, um marcador de urina",
    "confirmaram a origem animal: em parte das amostras, acharam ácido hipúrico, um marcador de urina")

# 0008: a perda de dimensão é aparente; a frustração geométrica foi descartada em 2020
substituir(8, "gancho", "as ondas magnéticas dentro do pigmento \"perderam\" uma dimensão",
    "as ondas magnéticas dentro do pigmento pareceram \"perder\" uma dimensão")
substituir(8, "explicacao", "A causa é o deslocamento entre as camadas de cobre, a chamada frustração geométrica.",
    "Na época, a explicação proposta foi a \"frustração geométrica\" entre camadas de cobre deslocadas; em 2020, "
    "porém, um estudo com nêutrons descartou essa frustração e atribuiu o comportamento em duas dimensões à "
    "existência de três tipos diferentes de camadas de cobre no cristal.")
CANDIDATOS[7]["fontes"].append({
    "url": "https://actu.epfl.ch/news/understanding-quantum-critical-magnetism-in-han-pu",
    "titulo": "Understanding quantum critical magnetism in Han purple (EPFL)", "idioma": "en",
    "trecho": "12.05.20 [...] "
        "Experiments on the ancient pigment Han purple, whose chemical composition is BaCuSi2O6, had revealed puzzling phenomena at the quantum phase transition caused by an applied magnetic field, which suggested that the three-dimensional crystal behaves as if it is only two-dimensional. "
        "Now an international collaboration, led by scientists at EPFL, the Paul Scherrer Institute (PSI) and the University of Toulouse, has shown that this phenomenon is caused by the fact that the crystal structure consists of three magnetically inequivalent Cu bilayers with an exotic ABABAC stacking. [...] "
        "Multiple mechanisms proposed to explain this phenomenon assumed geometrical frustration of the interactions between the bilayers [...] "
        "Researchers at EPFL, PSI and the University of Toulouse have performed high-resolution neutron spectroscopy measurements [...] "
        "Their data revealed effectively ferromagnetic intra-bilayer interactions, in full agreement with the ab initio study, and demonstrated that the crystal structure contains three magnetically inequivalent bilayer types [...] "
        "This had provided the appearance of dimensional reduction [...] "
        "Multiple Magnetic Bilayers and Unconventional Criticality without Frustration in BaCuSi2O6",
    "acessado_em": "2026-11-25"})

substituir(8, "gancho", "dos Guerreiros de Terracota da China virou assunto de física", "dos Guerreiros de Terracota virou tema de física")
trocar(8, nota_surpresa=4)

# 0014: o édito de 1609 é relato tradicional, pouco documentado
trocar(14, confianca="consenso_parcial",
    gancho="Em 1609, um édito de Henrique IV teria previsto a morte para quem usasse índigo na França, para proteger o pastel-dos-tintureiros. Mas as duas plantas tingem com a mesma substância.")
substituir(14, "explicacao", "a proibição foi repetida em 1594 e em 1603.",
    "a proibição foi repetida em 1594 e em 1603. Na França, segundo um relato tradicional, um édito de Henrique IV "
    "de 1609 previa a pena de morte para quem usasse \"a falsa e perniciosa droga indiana\"; o texto do édito, "
    "porém, é pouco documentado.")

# 0016: a origem última é persa; sem "o mais nobre"; século XIV e início do XV
trocar(16, nota_surpresa=3)
substituir(16, "gancho", "O carmesim, vermelho mais nobre da Idade Média,", "O carmesim, vermelho de luxo da Europa medieval,")
substituir(16, "gancho", "chegou pelo árabe, e a raiz sânscrita quer dizer \"feito por verme\".",
    "chegou pelo árabe e vem de uma antiga palavra persa ligada a \"verme\".")
substituir(16, "explicacao", "Nos séculos XIV e XV, o escarlate", "No século XIV e no início do XV, o escarlate")
substituir(16, "explicacao", "o sânscrito \"kṛmija\", \"feito por verme\", passou ao persa e ao árabe como \"qermez\".",
    "a palavra vem do persa, de uma raiz indo-iraniana ligada a \"verme\", parente do sânscrito \"kṛmija\", "
    "\"feito por verme\", e passou ao árabe como \"qermez\".")
acrescentar_trecho(16, 1, "The ultimate source from Classical Persian کرمست (kirmist), from Middle Persian; Proto-Indo-Iranian *kŕ̥miš. Cognate with Sanskrit कृमिज (kṛmija).")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
# 0008: a redução dimensional foi só aparente
substituir(8, "explicacao",
    'No ponto crítico quântico, a onda magnética deixou de se propagar na vertical e ficou presa a duas dimensões, como as ondulações na superfície de um lago.',
    'No ponto crítico quântico, a onda magnética pareceu deixar de se propagar na vertical, como se estivesse presa a duas dimensões, feito as ondulações na superfície de um lago.')
substituir(8, "explicacao",
    'atribuiu o comportamento em duas dimensões à existência',
    'atribuiu essa aparência de duas dimensões à existência')
substituir(8, "explicacao",
    'Até então, essa "redução dimensional", que teóricos usam para tentar explicar fenômenos como a supercondutividade de alta temperatura, nunca tinha sido observada em experimento.',
    'Em 2006, o resultado chamou atenção porque teóricos usam a ideia de "redução dimensional" para tentar explicar fenômenos como a supercondutividade de alta temperatura, e parecia ser a primeira vez que ela aparecia num experimento.')
# 0008: encurtar para caber em 250 palavras
substituir(8, "explicacao",
    'Em 2006, o resultado chamou atenção porque',
    'O resultado chamou atenção porque')
