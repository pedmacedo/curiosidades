"""Rodada 2 de Biomas brasileiros: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-biomas_brasileiros-01.py"))
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


# 0001: o revés de 2025 (circovírus nas ararinhas soltas), com fonte do ICMBio
trocar(1, gancho="Nos anos 1990, a última ararinha-azul conhecida na natureza era um macho em par com uma fêmea de outra "
    "espécie, uma maracanã. Ele sumiu em 2000. Em 2022, aves de cativeiro voltaram à Caatinga, num retorno ainda frágil.")
substituir(1, "explicacao",
    "Depois de anos de criação, e de aves trazidas da Alemanha para o Brasil em 2020, grupos de ararinhas foram soltos",
    "Com aves trazidas da Alemanha em 2020, grupos de ararinhas foram soltos")
substituir(1, "explicacao",
    "de um casal formado depois da soltura.",
    "de um casal formado depois da soltura. Em 2025, porém, veio um revés: 11 ararinhas que viviam soltas foram "
    "recapturadas no início de novembro por suspeita de circovírus, causador de uma doença de araras e papagaios "
    "que não tem cura e mata a ave na maior parte dos casos, e todas testaram positivo.")
CANDIDATOS[0]["fontes"].append({
    "url": "https://agenciagov.ebc.com.br/noticias/202511/ararinhas-azuis-que-estavam-em-vida-livre-testam-positivo-para-circovirus",
    "titulo": "Ararinhas-azuis que estavam em vida livre testam positivo para circovírus (Agência Gov / ICMBio, 26/11/2025)",
    "idioma": "pt",
    "trecho": (
        "26/11/2025 [...] "
        "O Instituto Chico Mendes de Conservação da Biodiversidade (ICMBio/MMA) divulgou os resultados dos exames realizados nas 11 ararinhas-azuis (Cyanopsitta spixii) que foram recapturadas no início de novembro por suspeita de infecção por circovírus. "
        "Todas testaram positivo. "
        "Oriundo da Austrália, o circovírus dos psitacídeos é o principal causador da doença do bico e das penas em psitacídeos (grupo de aves que inclui araras, papagaios e periquitos). "
        "A enfermidade não tem cura e mata a ave na maior parte dos casos. [...] "
        "As aves haviam sido repatriadas da Europa e mantidas no Criadouro para Fins Conservacionistas do Programa de Reintrodução da Ararinha-Azul, em Curaçá (BA), sendo posteriormente soltas na região em 2022."
    ),
})

# 0003: os 430 mil eram crença, não estimativa; a cobra dá o bote, mas não solta a presa
substituir(3, "gancho", "Já se estimou que a Ilha da Queimada Grande (SP) tivesse 430 mil jararacas-ilhoas",
    "Dizia-se que a Ilha da Queimada Grande (SP) tinha 430 mil jararacas-ilhoas")
substituir(3, "explicacao", "a mesma cifra da antiga estimativa de cobras", "a mesma cifra do antigo número de cobras")
substituir(3, "explicacao",
    "Em vez de dar o bote, soltar a presa e segui-la pelo cheiro, como outras víboras, ela a mantém presa na boca",
    "Outras víboras dão o bote, soltam a presa e a seguem pelo cheiro; ela, depois do bote, não solta a presa da boca")

# 0004: "boa parte" vegetal, com a ressalva das exceções
substituir(4, "gancho", "e a maior parte do que come é vegetal", "e boa parte do que come é vegetal")
substituir(4, "explicacao", "mas a maior parte da dieta é vegetal",
    "mas boa parte da dieta, muitas vezes mais da metade, é vegetal")
substituir(4, "explicacao", "O preferido é a lobeira, cujo fruto",
    "O preferido é a lobeira, que, com exceções, responde por 40% a 90% da dieta. O fruto")
acrescentar_trecho(4, 1, "its fruit accounts for more than 50% of maned wolves' diet")

# 0005: sem generalizações
substituir(5, "explicacao", "climas secos demais para outros tatus", "climas secos demais para alguns outros tatus")
substituir(5, "explicacao", "Só pumas e onças adultos têm força para ser uma ameaça natural.",
    "Entre os mamíferos, só pumas e onças adultos têm força para ser uma ameaça natural.")
substituir(5, "explicacao", "ele dispensa cavar buracos para se proteger, ao contrário da maioria dos parentes",
    "ele não cava buracos para se defender, ao contrário da maioria dos parentes")

# 0008: a fatia do tucano na dispersão varia entre as fontes
substituir(8, "explicacao", "e o tucano sozinho respondia por quase 85% da dispersão",
    "e o tucano sozinho respondia por mais de 80% da dispersão das sementes")

# 0009: o crescimento da população selvagem com os números do próprio artigo
substituir(9, "explicacao",
    "Com um esforço intenso de conservação, a população mundial da espécie cresceu cerca de trinta vezes nas duas primeiras décadas do século XXI.",
    "Com um esforço intenso de conservação, a população selvagem, estimada em cerca de 170 aves em 2000, chegou a 1.694 em 2018.")
acrescentar_trecho(9, 0, "The wild population was surveyed as some 170 individuals in 2000. [...] grew further to 1,694 in the 2018 count.")

# 0010: espécies sensíveis ao fogo, não matas inteiras; sem "depressa"
substituir(10, "explicacao",
    "matas de galeria e brejos de palmeiras podem não se recuperar de um incêndio grande",
    "nas matas de galeria e nos brejos de palmeiras, espécies sensíveis ao fogo podem não se recuperar de um incêndio grande")
substituir(10, "explicacao", "já tinham notado que ele rebrota e floresce depressa após queimar",
    "já tinham notado que ele rebrota e floresce depois de queimar")

# 0012: a falta de chuva foi no próprio ano de 2020
substituir(12, "explicacao",
    "Em 2020, depois de um ano com chuvas 40% abaixo do normal na região, foram 39.030 km².",
    "Em 2020, ano em que as chuvas na região ficaram 40% abaixo do normal, foram 39.030 km².")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
# 0001: as 11 recapturadas eram todas as que viviam soltas; o "retorno ainda frágil" enganava.
trocar(1, gancho="Em 1990, a última ararinha-azul conhecida na natureza era um macho em par com uma fêmea de outra espécie, uma maracanã. Sumiu em 2000. Em 2022, aves de cativeiro voltaram à Caatinga; em 2025, um vírus as tirou de lá.")
substituir(1, "explicacao", "11 ararinhas que viviam soltas foram recapturadas", "as 11 ararinhas que ainda viviam soltas foram recapturadas")
acrescentar_trecho(1, 0, "In November 2025, the Brazilian government and the public environmental preservation agency ICMBio announced that the eleven parrots still surviving in the wild were infected with a circovirus")
