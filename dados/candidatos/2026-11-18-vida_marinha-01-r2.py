"""Rodada 2 de Vida marinha: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-vida_marinha-01.py"))
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


# 0001: a "troca" é a interpretação de um estudo de 2017, contestada por outro, de 2019
trocar(1, confianca="consenso_parcial")
substituir(1, "explicacao",
    "Há um custo. Os inúmeros pontos de edição ficam conservados no genoma desses animais, com a mutação "
    "freada nesses locais. Assim, a flexibilidade maior na leitura dos genes teria saído ao preço de uma "
    "evolução mais lenta do próprio genoma.",
    "Pode haver um custo, segundo o estudo de 2017 que mapeou esses pontos: eles ficam conservados no genoma "
    "desses animais, com a mutação freada nesses locais, e a flexibilidade maior na leitura dos genes teria "
    "saído ao preço de uma evolução mais lenta do próprio genoma. Outros pesquisadores duvidam que a maior "
    "parte dessa edição seja vantajosa: um estudo de 2019 argumenta que, em geral, as edições que mudam "
    "proteínas nesses animais não são adaptativas, e lembra que, fora um canal de potássio de polvo ligado ao "
    "frio, não se conhece benefício dessa edição generalizada.")
CANDIDATOS[0]["fontes"].append({
    "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6881472/fullTextXML",
    "titulo": "The preponderance of nonsynonymous A-to-I RNA editing in coleoids is nonadaptive (Nature Communications, 2019, via Europe PMC)",
    "idioma": "en",
    "trecho": (
        "Although this phenomenon is thought to indicate widespread adaptive editing, its potential advantage is unknown. "
        "Here we propose an alternative, nonadaptive explanation. [...] "
        "Our evidence for this explanation suggests that the prevalent nonsynonymous editing in coleoids is generally nonadaptive, "
        "as in species with much lower editing activities. [...] "
        "Nonetheless, with the exception of recoding of an octopus potassium channel that is associated with cold adaptation [...] "
        "no benefit of the widespread editing is known in coleoids. [...] "
        "Liscovitch-Brauer N, et al.  Trade-off between transcriptome plasticity and genome evolution in cephalopods. Cell. 2017;169:191–202. [...] "
        "Accepted 2019 Oct 31; Collection date 2019."
    ),
})

# 0002: os machos vivem no tubo da fêmea; O. priapus é exceção
substituir(2, "gancho", "Os machos, microscópicos, vivem dentro das fêmeas.",
    "Os machos, em geral microscópicos, vivem no tubo da fêmea.")
substituir(2, "explicacao",
    "A diferença entre os sexos é extrema: as fêmeas são mais de 20 mil vezes maiores que os "
    "machos, que são microscópicos, vivem numa parte do tronco delas e produzem esperma com as próprias "
    "reservas de vitelo.",
    "A diferença entre os sexos costuma ser extrema: as fêmeas são mais de 20 mil vezes maiores que os "
    "machos, que são microscópicos. De 50 a 100 deles vivem no tubo que envolve uma única fêmea, nunca passam "
    "do estágio de larva e produzem esperma com as próprias reservas de vitelo. Uma exceção é Osedax priapus, "
    "cujos machos vivem livres e são bem maiores, com cerca de um terço do volume da fêmea.")
acrescentar_trecho(2, 0,
    "Between 50 and 100 microscopic dwarf males live inside the tube surrounding a single female and never develop past the larval stage; "
    "they produce sperm from yolk reserves. [...] "
    "Interestingly, Osedax priapus lack the frequently observed male dwarfism. Males live freely and compete for space and food with females. "
    "Being larger, they produce and carry more sperm. However, sexual size dimorphism is still observed in O. priapus: most males are one-third the volume of females.")

# 0003: a mudança imune teria vindo primeiro (hipótese de Boehm); frase dele inteira no trecho
substituir(3, "gancho",
    "Para essa união não ser rejeitada como um transplante, várias espécies perderam peças do sistema imune.",
    "Isso só não vira rejeição de transplante porque várias dessas espécies perderam peças do sistema imune.")
substituir(3, "explicacao",
    "Os peixes compensariam com defesas inatas reforçadas, cujos detalhes ainda não foram descobertos.",
    "Os peixes compensariam com defesas inatas reforçadas, cujos detalhes ainda não foram descobertos. "
    "Boehm propõe ainda que forças evolutivas desconhecidas mudaram primeiro o sistema imune, e só depois "
    "essas mudanças foram aproveitadas para a fusão.")
substituir_trecho(3, 0,
    "would result in fatal immunodeficiency [...] "
    "Director at the MPI of Immunobiology and Epigenetics and lead scientist of the project.",
    "For humans, the combined loss of important immune facilities observed in anglerfishes would result in fatal immunodeficiency”, "
    "says Thomas Boehm, Director at the MPI of Immunobiology and Epigenetics and lead scientist of the project.")
acrescentar_trecho(3, 0,
    "We assume that as yet unknown evolutionary forces first drive changes in the immune system, "
    "which are then exploited for the evolution of sexual parasitism”, says Thomas Boehm.")

# 0008: Yoichi Yusa é homem
substituir(8, "explicacao", "as pesquisadoras suspeitam", "os pesquisadores suspeitam")
substituir(8, "explicacao", "e as autoras sugerem", "e os autores sugerem")

# 0012: 2004 e 2012 são lulas diferentes; a isca de 2012 também era uma lula; 1ª frase reescrita
substituir(12, "gancho", "Depois, uma luz imitando uma água-viva a atraiu para a câmera.",
    "Em 2012, uma luz imitando uma água-viva atraiu outra para ser filmada.")
substituir(12, "explicacao",
    "Na virada do século XXI, a lula-gigante ainda era um dos poucos grandes animais vivos nunca "
    "fotografados com vida, nem na natureza nem em cativeiro.",
    "Até o começo deste século, ninguém tinha conseguido fotografar uma lula-gigante viva, nem no mar nem num "
    "aquário: ela era um dos raros animais de grande porte ainda sem esse registro.")
substituir(12, "explicacao",
    "Para atraí-la, usou uma luz que imitava uma água-viva Atolla em pânico",
    "Para atraí-la, usou uma lula como isca e uma luz que imitava uma água-viva Atolla em pânico")
acrescentar_trecho(12, 0, "and by using a Thysanoteuthis rhombus (diamond squid) as bait.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(3, "explicacao", "Segundo o líder do estudo, essa combinação", "Segundo o líder do estudo, o imunologista Thomas Boehm, essa combinação")
substituir(3, "explicacao", "Instituto Max Planck de Imunobiologia, na Alemanha", "Instituto Max Planck de Imunobiologia e Epigenética, na Alemanha")
