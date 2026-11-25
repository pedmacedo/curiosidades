"""Rodada 2 de Padrões e fractais: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-padroes_fractais-01.py"))
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


# 0001: não cravar qual país deu cada número
substituir(1, "gancho",
    "Portugal dizia que sua fronteira com a Espanha tinha 987 km; a Espanha, 1.214 km.",
    "Para a mesma fronteira entre Portugal e Espanha, um país dava 987 km; o outro, 1.214 km.")

# 0004: um estudo, e a rede de Turing modulada por gradientes
substituir(4, "gancho", "Em 2014, a ideia explicou a formação dos dedos.",
    "Em 2014, um estudo a ligou à formação dos dedos.")
substituir(4, "explicacao", "ligadas por uma terceira, a Sox9.",
    "ligadas por uma terceira, a Sox9. Pelo título do artigo, essa rede de Turing não age sozinha: é ajustada "
    "por gradientes de outras moléculas ao longo do membro.")
acrescentar_trecho(4, 0, "Digit patterning is controlled by a Bmp-Sox9-Wnt Turing network modulated by morphogen gradients. Science, 2014.")

# 0006: a média de 1,310 é das 65 conchas do gênero Nautilus; proporção do retângulo que envolve a espiral
substituir(6, "gancho", "Mas medidas de 80 conchas de um museu deram em média 1,31.",
    "Mas, de 80 conchas medidas num museu, as do gênero Nautilus deram média de 1,31.")
substituir(6, "explicacao",
    "mediu 80 conchas de náutilo da coleção Smithsonian, identificadas por especialistas, e encontrou média de "
    "1,310: nem a áurea nem exatamente 4 para 3.",
    "mediu 80 conchas de náutilo da coleção Smithsonian, identificadas por especialistas, comparando os lados "
    "do retângulo que envolve a espiral. As 65 do gênero Nautilus deram média de 1,310: nem a áurea nem "
    "exatamente 4 para 3.")
substituir(6, "explicacao", "Uma espécie, o náutilo-crostoso, destoou, com média de 1,356.",
    "O náutilo-crostoso, hoje classificado num gênero à parte, destoou, com média de 1,356.")
acrescentar_trecho(6, 0,
    "All five species of Nautilus, if taken as a whole (65 shells), with ratios added individually, not as aggregates, had the same range and also a mean of 1.310 (Table 1). [...] "
    "her shell’s spiral is inscribed in the √φ rectangle with only three sides at a tangent. "
    "Four tangents are necessary to establish the correct aspect ratio. [...] "
    "there are differences between Nautilus scrobiculatus and other Nautilus species significant enough for it to be renamed as a sister taxon of Nautilus with its own genus, Allonautilus [...] "
    "The rectangle in Fig. 9 is in a ratio of 1:1.618 while in Fig. 10 it is 1:1.356.")

# 0007: ciclo de vida típico, não regra; a revisão de 2025 é de dois defensores da auto-organização
substituir(7, "explicacao", "Cada um vive de 30 a 60 anos.",
    "Estudos estimam um ciclo de vida típico de 30 a 60 anos, mas alguns somem em menos de uma década.")
substituir(7, "explicacao",
    "Uma revisão de 2025 concluiu que só a auto-organização é compatível com todas as observações",
    "Uma revisão de 2025, assinada por dois defensores dessa ideia, concluiu que só a auto-organização é "
    "compatível com todas as observações")
acrescentar_trecho(7, 0,
    "In some cases, fairy circles have disappeared within a span of 10 years or less, while other fairy circles may have lasted for centuries. [...] "
    "Later in 2013, Michael Cramer and Nichole Barger suggested that the circles were the consequence of vegetation patterns that arose naturally from competition between grasses. [...] "
    "According to Walter Tschinkel, this theory accounts for all the characteristics of fairy circles")

# 0009: "costumam surgir"; sem a frase sobre Hertz
substituir(9, "explicacao",
    "Os padrões têm propriedades fractais e surgem sempre que uma descarga elétrica atravessa um material "
    "isolante, seja sólido, líquido ou gás.",
    "Os padrões têm propriedades fractais e costumam surgir quando uma descarga elétrica rompe um material "
    "isolante, seja sólido, líquido ou gás.")
substituir(9, "explicacao",
    "Mais tarde, Heinrich Hertz usou essas figuras no trabalho que comprovou as ondas eletromagnéticas de "
    "Maxwell. ", "")
substituir_trecho(9, 0,
    "Heinrich Rudolf Hertz employed Lichtenberg dust figures in his seminal work proving Maxwell's electromagnetic wave theories. [...] ",
    "")

# 0010: proporções parecidas, não iguais
substituir(10, "gancho", "Amido de milho secando faz colunas iguais, em miniatura.",
    "Amido de milho secando faz colunas parecidas, em miniatura.")
substituir(10, "explicacao",
    "Como todas as colunas desse tipo obedecem à mesma proporção entre largura, velocidade e difusão do calor",
    "Como todas as colunas desse tipo seguem uma proporção parecida entre largura, velocidade e difusão do calor")
acrescentar_trecho(10, 0, "For basalt, Pe≈0.35. For cornstarch, Pe≈0.1.")

# 0012: escala do Dictyostelium; "não conseguia explicar o fenômeno"
substituir(12, "explicacao",
    "Espirais muito parecidas aparecem em colônias de uma ameba do solo, o Dictyostelium, numa escala de dias "
    "a anos, e não de minutos.",
    "Espirais muito parecidas aparecem em colônias de uma ameba do solo, o Dictyostelium, só que formadas por "
    "células inteiras, e não por moléculas.")
substituir(12, "gancho", "porque ele não sabia explicar", "porque ele não conseguia explicar o fenômeno")
substituir_trecho(12, 0,
    "In the case of the soil amoeba, the size of the elements is typical of single-celled organisms and the times involved are on the order of days to years. [...] ",
    "In the case of the soil amoeba, the size of the elements is typical of single-celled organisms [...] ")

# 0014 (aprovado): troca opcional
substituir(14, "gancho", "lados de 14.500 km", "lados de cerca de 14.500 km")
