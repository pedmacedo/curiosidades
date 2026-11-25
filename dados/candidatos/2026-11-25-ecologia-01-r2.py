"""Rodada 2 de Ecologia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-ecologia-01.py"))
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


# notas revistas pelo verificador
trocar(2, nota_surpresa=3)
trocar(5, nota_surpresa=5)
trocar(6, nota_surpresa=5)
trocar(11, nota_surpresa=3)

# 0001: a análise de 21 anos trata dos álamos da região norte; o estado anterior não voltou na região norte
substituir(1, "explicacao",
    "Uma análise de 21 anos de dados concluiu que a mudança de comportamento dos elks provocada pelos lobos pode "
    "ser deixada de lado para entender a cascata local.",
    "Uma análise de 21 anos de dados sobre lobos, elks e álamos na região norte do parque concluiu que, ao menos "
    "para os álamos, a mudança de comportamento dos elks provocada pelo medo dos lobos pode ser deixada de lado "
    "para entender a cascata local.")
substituir(1, "explicacao", "E o parque não voltou ao estado anterior:",
    "E boa parte da região norte do parque não voltou ao estado anterior:")
acrescentar_trecho(1, 0, "the ecosystem as a whole has not completely reverted to its state before the")

# 0009: a mixomatose ajudou a levar os predadores à beira da extinção; origem da cepa (tapiti)
substituir(9, "explicacao",
    "O efeito subiu a cadeia alimentar: predadores especializados em coelhos, como o lince-ibérico e a "
    "águia-imperial-ibérica, ficaram à beira da extinção.",
    "O efeito subiu a cadeia alimentar: a queda dos coelhos ajudou a levar predadores especializados neles, como "
    "o lince-ibérico e a águia-imperial-ibérica, à beira da extinção.")
substituir(9, "explicacao", "o vírus foi solto em 1950 como controle biológico,",
    "uma cepa do vírus vinda do tapiti, um coelho silvestre sul-americano, foi solta em 1950 como controle biológico,")

# 0010: culpa dividida com eutrofização e pesca; declínio começou antes da perca; ~200 espécies
trocar(10, confianca="consenso_parcial",
    gancho="A perca-do-nilo, solta no lago Vitória nos anos 1950, levou boa parte da culpa pelo sumiço de cerca de "
           "200 espécies de peixes nativos, culpa hoje dividida com a poluição por nutrientes. E ela trouxe outro "
           "efeito: mais procura por lenha.")
substituir(10, "explicacao", "várias centenas de espécies nativas.",
    "várias centenas de espécies nativas; só de ciclídeos endêmicos, cerca de 200 se extinguiram. Estudos mais "
    "recentes, porém, dividem a culpa: a eutrofização do lago, "
    "o excesso de nutrientes causado por atividades humanas, e a pesca também pesam, e dentes de peixes "
    "preservados nos sedimentos do fundo indicam que o declínio dos ciclídeos começou bem antes da chegada da "
    "perca. O peso de cada causa ainda é debatido.")
# para caber em 250 palavras, enxuga a parte da exportação e do novo equilíbrio
substituir(10, "explicacao",
    " Ao mesmo tempo, o peixe virou negócio de exportação: em 2003, as vendas para a União Europeia chegaram a "
    "169 milhões de euros.", "")
CANDIDATOS[9]["fontes"].append({
    "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10950456/fullTextXML",
    "titulo": "Testing alternative hypotheses for the decline of cichlid fish in Lake Victoria using fish tooth time series from sediment cores (Biology Letters, 2024)",
    "idioma": "en",
    "trecho": "Suggested causal factors include anthropogenic eutrophication, fishing, and introduced non-native species but their relative importance remains unresolved [...] "
              "we reconstruct two time series, covering the last approximately 200 years, of fish assemblage using fish teeth preserved in lake sediments. [...] "
              "Our data show significant decreases in haplochromine and oreochromine cichlid fish abundances that began long before the arrival of Nile perch. [...] "
              "culminating in the extinction of approximately 200 endemic cichlid species."})

# 0011: "em cerca de um ano", "em geral"; sem o "sempre"
trocar(11, gancho="Para testar uma teoria sobre ilhas, dois ecólogos fumigaram ilhotas de mangue na Flórida até "
                  "eliminar seus artrópodes. Em cerca de um ano, a maioria voltou ao número de espécies de antes, e as "
                  "ilhas perto do continente se recuperaram mais rápido.")
substituir(11, "explicacao", "Em um ano, as ilhas tinham voltado aos níveis anteriores",
    "Em cerca de um ano, as ilhas tinham, em geral, voltado aos níveis anteriores")
substituir(11, "explicacao", "uma reserva grande sempre protege mais espécies que várias pequenas",
    "uma reserva grande abrigaria mais espécies que várias pequenas")

# 0012: sem mito_desmentido; "há estudos que não acharam"
trocar(12, tipos_espanto=["contraintuitivo"])
substituir(12, "gancho", "e não se demonstrou que reduzam os parasitas do hospedeiro.",
    "e há estudos em que não reduziram os parasitas do hospedeiro.")
substituir(12, "explicacao",
    "e não se demonstrou relação estatisticamente significativa entre a presença das aves e uma carga menor de parasitas",
    "e há estudos que não acharam relação estatisticamente significativa entre a presença das aves e uma carga "
    "menor de parasitas")

# 0013: a gralha-preta é a principal predadora na região estudada por Soler
substituir(13, "explicacao", "e que a gralha-preta, a principal predadora de ninhos de pega, é a menos sensível a ela.",
    "e que a gralha-preta, principal predadora de ninhos de pega na região estudada por Soler, é a menos sensível a ela.")

# 0015: sem as "danças"; feminização é frequente, não universal
substituir(15, "gancho",
    "Se o caranguejo é macho, o corpo dele ganha formato de fêmea, e ele chega a fazer as danças de acasalamento das fêmeas.",
    "Se o caranguejo é macho, o corpo dele costuma ganhar formato de fêmea, e ele passa a agir como uma.")
substituir(15, "explicacao", "o abdômen alarga e achata como o de uma fêmea",
    "o abdômen costuma alargar e achatar como o de uma fêmea")

# 0016: o mecanismo é suposto; as espécies sumiram da ilha
substituir(16, "gancho", "Sem quem as comesse, as aranhas se multiplicaram:", "Sem as aves, as aranhas se multiplicaram:")
substituir(16, "explicacao", "doze espécies desapareceram", "doze espécies de aves nativas sumiram da ilha")

# limites de gancho (≤ 220) e nota do 0014 conforme o veredito
trocar(10, gancho="A perca-do-nilo, solta no lago Vitória nos anos 1950, levou boa parte da culpa pelo sumiço de cerca "
                  "de 200 espécies de peixes nativos, culpa hoje dividida com a poluição por nutrientes. E fez crescer "
                  "a procura por lenha.")
trocar(11, gancho="Dois ecólogos fumigaram ilhotas de mangue na Flórida até eliminar seus artrópodes. Em cerca de um "
                  "ano, a maioria voltou ao número de espécies de antes, e as ilhas perto do continente se recuperaram "
                  "mais rápido.")
trocar(14, nota_surpresa=4)
