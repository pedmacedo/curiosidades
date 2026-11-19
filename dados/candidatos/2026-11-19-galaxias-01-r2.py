"""Rodada 2 de Galáxias: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-galaxias-01.py"))
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


KIAA_M31 = "https://kiaa.pku.edu.cn/info/1031/11252.htm"

# 0001: a distância atual de Andrômeda não é exatamente 2 milhões de anos-luz
substituir(1, "explicacao", "Medições melhores põem Andrômeda hoje a 2 milhões de anos-luz.",
    "Medições melhores põem Andrômeda hoje a mais de 2 milhões de anos-luz.")

# 0002: a duplicação de 1952 veio das observações com o telescópio de 200 polegadas
substituir(2, "explicacao",
    "Na reunião da União Astronômica Internacional de 1952, em Roma, ele anunciou que Andrômeda "
    "estava mais longe do que se pensava, o que, na prática, dobrava o tamanho do universo conhecido.",
    "Anos depois, já com o novo telescópio de 200 polegadas, ele procurou em Andrômeda estrelas variáveis "
    "que deveriam aparecer se ela estivesse à distância aceita, de 750 mil anos-luz, e não as encontrou. "
    "Concluiu que a galáxia estava mais longe e anunciou isso em 1952, na reunião da União Astronômica "
    "Internacional em Roma: na prática, o tamanho do universo conhecido dobrava.")
acrescentar_trecho(2, 0, "when he looked for cluster-type variables in the Andromeda galaxy. "
    "At the accepted distance of 750,000 light-years, these stars should have appeared in photographs taken with the 200-inch telescope; when they did not")

# 0003: não é mito desmentido, é debate aberto; o estudo de 2026 voltou a ~90% de fusão
trocar(3,
    tipos_espanto=["misterio_aberto", "contraintuitivo"],
    nota_surpresa=3,
    gancho="A famosa colisão entre a Via Láctea e Andrômeda virou dúvida: um estudo de 2025 deu quase 50% de chance "
           "de não haver fusão em 10 bilhões de anos; outro, de 2026, voltou a cerca de 90% de chance de fusão.",
    explicacao=(
        "Andrômeda vem na nossa direção a cerca de 110 km/s, o que se sabe pelo desvio para o azul da sua luz. "
        "O difícil é medir o movimento lateral dela no céu, e é dele que depende se haverá um choque ou só uma "
        "passagem ao largo. A equipe de Till Sawala usou dados dos telescópios espaciais Gaia e Hubble e rodou "
        "100 mil simulações. A M33, do Triângulo, aumentava a chance de fusão, enquanto a Grande Nuvem de "
        "Magalhães, cuja órbita é perpendicular à rota entre a Via Láctea e Andrômeda, a reduzia. Com as "
        "incertezas de posições, movimentos e massas, cerca de metade dos cenários não terminava em fusão nos "
        "próximos 10 bilhões de anos. Para os autores, o destino da nossa galáxia \"ainda está completamente em "
        "aberto\". Depois, uma equipe da Universidade de Pequim liderada pelo doutorando Hao Wu mediu de novo o "
        "movimento lateral de Andrômeda com estrelas supergigantes e resolveu discrepâncias entre as medições do "
        "Gaia. O resultado, publicado em 2026: cerca de 90% de chance de fusão em 10 bilhões de anos, com tempo "
        "médio de uns 6,5 bilhões. Mesmo assim, esses autores dizem que a questão continua inconclusiva, porque "
        "pequenas mudanças no movimento medido alteram bastante o desfecho. E, se a fusão acontecer, é improvável "
        "que duas estrelas colidam: a distância entre elas é imensa."
    ),
)
CANDIDATOS[2]["fontes"].append(
    {"url": KIAA_M31, "titulo": "The Fate of the Milky Way–Andromeda System: To Merge or Not? (KIAA, Universidade de Pequim)", "idioma": "en",
     "trecho": (
         "Using improved dynamical measurements, PhD student Hao Wu and Professor Huawei Zhang in the Department of Astronomy at Peking University led a team of astronomers to determine that the probability of a merger between the Milky Way and Andromeda is 90% within the next 10 billion years. [...] "
         "Although previous evidence was contradictory, the team resolved these discrepancies using improved stellar samples, showing that a merger is likely in about 6.5 billion years. [...] "
         "Using the Gaia results, Sawala et al. (2025) in Nature Astronomy suggested that the probability of a Milky Way–M31 merger within the next 10 billion years might be only about 50%. [...] "
         "Wu, Zhang, and their collaborators constructed high-quality samples of supergiant stars in Andromeda and the nearby Triangulum Galaxy (M33) [...] "
         "the probability of a MW–M31 merger within the next 10 Gyr is approximately 90% (see Figure 4), with a median merger time of about 6.5 Gyr. [...] "
         "More importantly, the study shows that even small changes in M31's proper motion can significantly alter the future orbital evolution of the Milky Way–M31 system. [...] "
         "although the current results support the picture in which the Milky Way and M31 will ultimately merge, the question remains inconclusive. [...] "
         "The Astrophysical Journal Letters (Wu et al. 2026, ApJL, 1001, L19)"
     )})

# 0005: o verde é falsa cor do Hubble; a proposta do jato complementa a do quasar
substituir(5, "gancho", "achou uma mancha verde estranha no céu", "achou uma mancha estranha no céu, ao lado de uma galáxia")
substituir(5, "explicacao", "Há outras explicações em estudo, como a de um jato de partículas do buraco negro central.",
    "Outra proposta, de 2010, é que parte da luz venha também da interação de um jato de partículas do "
    "buraco negro central com o gás em volta da galáxia.")
acrescentar_trecho(5, 0, "On 17 June 2010, a group of researchers at the European VLBI Network (EVN) and the UK's Multi-Element Radio Linked Interferometer Network (MERLIN), proposed another related explanation.")

# 0008: a mais rápida de sequência principal
substituir(8, "explicacao", "Em novembro de 2019, ela era a estrela mais rápida já detectada",
    "Em novembro de 2019, ela era a estrela de sequência principal (a fase de vida em que está o Sol) mais "
    "rápida já detectada")
acrescentar_trecho(8, 1, "S5-HVS1 is an A-type main-sequence star notable as the fastest one detected as of November 2019")

# 0010: sem misterio_aberto; a região é menos massiva e Shapley responde por boa parte do movimento
trocar(10, tipos_espanto=["escala_absurda", "conexao_inesperada"], nota_surpresa=3)
substituir(10, "explicacao",
    "A história não para aí: o próprio Grande Atrator parece se mover rumo a uma concentração maior e mais "
    "distante, a de Shapley.",
    "A história não para aí: estudos posteriores mostraram que a região é menos massiva do que se pensava e "
    "que boa parte do nosso movimento vem de uma concentração maior e mais distante, a de Shapley, rumo à "
    "qual o próprio Grande Atrator parece se mover.")
acrescentar_trecho(10, 0, "Its results indicated that the Norma region was  much less massive than some early estimates and that a substantial part of the Local Group's motion is produced by more distant structures, especially the Shapley Supercluster.")

# 0014: atualizar com as simulações de 2022 (origem em Sagitário A*)
trocar(14, confianca="consenso_parcial",
    gancho="Em 2010, dados públicos de um telescópio de raios gama revelaram duas bolhas gigantes saindo do centro "
           "da Via Láctea, de 25 mil anos-luz cada. A principal suspeita é o buraco negro central, mas a origem ainda é debatida.")
substituir(14, "explicacao",
    "Outra é um surto de formação de estrelas, já que em outras galáxias esses surtos produzem enormes fluxos de gás.",
    "Outra é um surto de formação de estrelas, já que em outras galáxias esses surtos produzem enormes fluxos de gás. "
    "Desde então, simulações de computador, como as de 2022, reforçaram a hipótese de que as bolhas foram "
    "infladas por uma fase ativa do buraco negro central, Sagitário A*, embora o tema ainda seja estudado.")
acrescentar_trecho(14, 1, "By 2022, detailed computer simulations further confirmed that the bubbles were caused by the Sagittarius A* black hole.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(3, "explicacao", "liderada pelo doutorando Hao Wu", "liderada pelo doutorando Hao Wu e pelo professor Huawei Zhang")
