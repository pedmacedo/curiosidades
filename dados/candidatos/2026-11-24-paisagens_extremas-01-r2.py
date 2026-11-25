"""Rodada 2 de Paisagens extremas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-paisagens_extremas-01.py"))
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


# 0001: sai a alegação "sem chuva de 1570 a 1971"; acrescenta o limite dos testes
substituir(1, "explicacao",
    "Há indícios de que talvez não tenha caído chuva significativa entre 1570 e 1971. ", "")
substituir_trecho(1, 0,
    "Evidence suggests that the Atacama may not have had any significant rainfall from 1570 to 1971. [...] ", "")
substituir(1, "explicacao",
    "No solo da região de Yungay, eles não detectaram sinal algum.",
    "No solo da região de Yungay, eles não detectaram sinal algum, o que mostra mais os limites dos testes do "
    "que um solo totalmente estéril.")

# 0002: o recorde vale para a época da medição; hoje o povoado está quase abandonado
trocar(2, nota_surpresa=3,
    gancho="Dallol, na Etiópia, tem o recorde de maior temperatura média anual de um lugar habitado: cerca de 35 °C, "
           "medida entre 1960 e 1966. Hoje o povoado está quase abandonado, mas caravanas de camelos ainda vão lá buscar sal.")
substituir(2, "explicacao", "o recorde para um lugar habitado.",
    "o recorde para um lugar habitado na época da medição.")

# 0003: "apontada como" o corpo d'água mais salgado
substituir(3, "explicacao", "a lagoa Gaet'ale, com 43% de sal, é o corpo d'água mais salgado da Terra;",
    "a lagoa Gaet'ale, com 43% de sal, é apontada como o corpo d'água mais salgado da Terra;")

# 0004: "podem" e "no verão"; "entre os desertos mais frios e secos"; sem o "primeiro lugar"
# (a fonte do phys.org sugerida deu HTTP 403; a frase nova usa só o que a Wikipedia sustenta)
substituir(4, "gancho", "fazem a neve evaporar em poucas horas.",
    "podem fazer a neve evaporar em poucas horas no verão.")
substituir(4, "explicacao", "formam o deserto mais frio e seco do mundo.",
    "estão entre os desertos mais frios e secos do mundo.")
substituir(4, "explicacao",
    "Não acharam organismos vivos, o que fez do vale o primeiro lugar visitado por humanos sem vida microbiana "
    "ativa detectada.",
    "Não encontraram organismos vivos no permafrost.")
substituir_trecho(4, 0,
    "They found no living organisms in the permafrost, making University Valley the first location on the planet visited by humans with no detected active microbial life.",
    "They found no living organisms in the permafrost")

# 0005: o Lut divide o posto com o deserto de Sonora (NASA Earth Observatory); "em 2020 ainda não havia"
trocar(5, nota_surpresa=3,
    gancho="Satélites da NASA mediram no deserto de Lut, no Irã, até 80,8 °C na superfície, um dos chãos mais quentes "
           "da Terra. O ar sobre ele, porém, pode estar 30 °C mais frio, e por isso esses números não valem como recorde.")
substituir(5, "explicacao",
    "Em 2019, um estudo com dados mais novos do mesmo sensor relatou 80,83 °C na superfície.",
    "Em 2019, um estudo com dados mais novos do mesmo sensor relatou 80,83 °C na superfície; outra análise do "
    "MODIS achou os mesmos 80,8 °C também no deserto de Sonora, no México.")
substituir(5, "explicacao", "até 2020 não havia estações meteorológicas permanentes ali",
    "em 2020 ainda não havia estações meteorológicas permanentes ali")
CANDIDATOS[4]["fontes"].append({
    "url": "https://science.nasa.gov/earth/earth-observatory/irans-lut-desert-153634",
    "titulo": "Iran's Lut Desert (NASA Earth Observatory)", "idioma": "en",
    "trecho": "The analysis measured land surface temperatures from 2002 to 2019 around the world and found that "
              "MODIS recorded the hottest temperatures of 80.8°C (177.4°F) in both the Sonoran and Lut deserts.",
})

# 0006: a declaração da OMM é anterior ao estudo; data da edição do BAMS
substituir(6, "explicacao",
    "A OMM mantém o recorde e diz que só abrirá investigação se surgirem novos materiais.",
    "Por enquanto, a OMM mantém o recorde oficial.")
substituir(6, "explicacao",
    "um estudo publicado em 2026 no Bulletin of the American Meteorological Society",
    "um estudo publicado no Bulletin of the American Meteorological Society (edição de janeiro de 2026)")

# 0008: saem as frases do Sentinel-1A e do Landsat-5
substituir(8, "explicacao",
    "Como ele reflete a maior parte da luz do sol que recebe, também serve para ajustar sensores ópticos: o "
    "instrumento do Landsat-5 foi calibrado em voo usando o salar como alvo estável. Em 2014, poucas semanas "
    "depois do lançamento, o satélite europeu Sentinel-1A sobrevoou o salar para calibrar medições de relevo "
    "feitas por radar.",
    "Como ele reflete a maior parte da luz do sol que recebe, também serve de alvo estável para ajustar "
    "sensores ópticos.")
substituir_trecho(8, 0,
    " [...] the Landsat-5 satellite's Thematic Mapper (TM) was calibrated “in-flight” by using the salar as a radiometrically stable target [...] "
    "In April 2014, the European Space Agency’s (ESA) Sentinel‑1A satellite surveyed the salar a few weeks after its launch as part of the Copernicus programme. "
    "The mission focused on calibrating radar-based measurements of surface topography.",
    "")

# 0009: "povoado permanente de grande porte mais alto do mundo"
substituir(9, "gancho", "o maior povoado permanente mais alto do mundo, a até 5.100 m",
    "o povoado permanente de grande porte mais alto do mundo, a até 5.100 m")

# 0011: gancho com o ácido sulfúrico e sem sugerir 30 anos de escavação
trocar(11, gancho="Nos anos 1950, exploradores ouviram vento rugindo sob o entulho de uma caverna no Novo México. "
                  "Em 1986, uma escavação revelou a Lechuguilla: 244,8 km de galerias dissolvidas de baixo para cima "
                  "por ácido sulfúrico.")

# 0013: gancho com o fogo minguando; dado da Capterio no fim
trocar(13, gancho="A 'Porta do Inferno', cratera de gás em chamas no Turcomenistão, tem origem mal documentada e está "
                  "minguando: em 2025, o governo disse que o fogo caiu a um terço, enquanto poços em volta passaram a "
                  "captar metano.")
substituir(13, "explicacao", "e poços foram perfurados em volta para captar metano.",
    "e poços foram perfurados em volta para captar metano. Segundo a Capterio, empresa que monitora a queima de "
    "gás, a intensidade do calor caiu mais de 75% em três anos.")
acrescentar_trecho(13, 0,
    "The intensity of heat from the flames has diminished by more than 75 percent over the last three years, "
    "according to an analysis by Capterio, a company that monitors natural gas flares.")

# 0015: a idade de 5,5 milhões de anos como estimativa
substituir(15, "gancho", "Selada há cerca de 5,5 milhões de anos, tem uma cadeia alimentar",
    "Isolada há talvez 5,5 milhões de anos, tem uma cadeia alimentar")
substituir(15, "explicacao", "A caverna está isolada da superfície há cerca de 5,5 milhões de anos, e a vida ali",
    "Estima-se que a caverna esteja isolada da superfície há cerca de 5,5 milhões de anos, e a vida ali")

# ganchos encurtados para caber em 220 caracteres
trocar(4, gancho="Nos Vales Secos de McMurdo, na Antártida, ventos que descem das montanhas podem fazer a neve evaporar "
                 "em horas no verão. Em 2013, num desses vales, cientistas não acharam organismos vivos no solo congelado.")
substituir(9, "gancho", "no Peru, o povoado permanente de grande porte mais alto do mundo, a até 5.100 m, muitos mineiros",
    "no Peru, povoado permanente de grande porte mais alto do mundo, a até 5.100 m, mineiros")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(4, "gancho", "cientistas não acharam organismos vivos no solo congelado.", "cientistas não detectaram vida microbiana ativa no solo congelado.")
substituir(4, "explicacao", "Não encontraram organismos vivos no permafrost.", "Não detectaram vida microbiana ativa no permafrost.")
substituir(5, "gancho", "O ar sobre ele, porém, pode estar 30 °C mais frio", "O ar sobre ele, porém, pode estar bem mais frio")
trocar(9, gancho="Em La Rinconada (Peru), povoado permanente de grande porte mais alto do mundo, a até 5.100 m, muitos mineiros de ouro trabalham 30 dias sem salário. Num dia, trabalham para si e levam o minério que aguentam nos ombros.")
