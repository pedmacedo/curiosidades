"""Rodada 2 de Rios, lagos e gelo: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-agua_doce_gelo-01.py"))
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


# 0002: o lago "foi" o quarto maior; os 10% são de 2007; a bacia leste secou pela primeira vez na história moderna
trocar(2, gancho="O mar de Aral, que já foi o quarto maior lago do mundo, encolheu a 10% do tamanho depois que a URSS desviou "
    "seus rios para o algodão. Técnicos previam isso em 1964. E cronistas dizem que ele já sumira em 1417.")
substituir(2, "explicacao", "é um lago salgado sem saída para o mar", "era um lago salgado sem saída para o mar")
substituir(2, "explicacao", "e em 2014 a bacia leste secou de vez.",
    "e em 2014 a bacia leste secou por completo, pela primeira vez na história moderna.")

# 0004: o sal "provavelmente" mantém a salmoura líquida; o papel do sulfato e do ferro, com o "may" da fonte
substituir(4, "explicacao",
    "e a salmoura que sobra ficou de duas a três vezes mais salgada que o oceano, por isso não congela.",
    "e a salmoura que sobra ficou de duas a três vezes mais salgada que o oceano; o sal provavelmente ajuda a "
    "mantê-la líquida mesmo abaixo de zero.")
substituir(4, "explicacao",
    "Uma explicação é que eles respiram sulfato usando o ferro, um processo nunca antes visto na natureza.",
    "Uma explicação possível é que eles usem o sulfato para \"respirar\" ferro em vez de oxigênio, um processo nunca "
    "antes visto na natureza.")

# 0006: sem a contradição; o ponto é a ausência do viés de quem acha
substituir(6, "explicacao",
    "mas lá, onde quase tudo o que cai pode ser recuperado, eles são só 0,4% dos achados.",
    "mas na Antártida, onde a busca é sistemática e não depende de alguém estranhar uma pedra, eles são só 0,4% "
    "dos achados.")

# 0008: calibração "até 52.800 anos atrás"; sem a frase sobre varvas só em água doce
trocar(8, gancho="As camadas do fundo de um lago japonês ajudam a acertar o relógio do carbono-14. Cada ano deixou ali uma "
    "lâmina de sedimento, e essa sequência permitiu calibrá-lo até 52.800 anos atrás.")
substituir(8, "explicacao",
    " Elas só se formam em água doce ou salobra, porque no mar o sal faz a argila se juntar em grãos grossos o ano inteiro.",
    "")
substituir(8, "explicacao", "estenderam a calibração para 52.800 anos.", "estenderam a calibração até 52.800 anos atrás.")
substituir_trecho(8, 1,
    "Varves form only in fresh or brackish water, because the high levels of salt in normal sea water coagulate the clay into coarse grains. [...] ",
    "[...] ")

# 0010: o Grímsvötn solta enchentes com frequência; em 1996 a erupção ergueu a barragem de gelo
substituir(10, "explicacao",
    "O lago Grímsvötn, sob o Vatnajökull, ficou selado até 1996, quando a erupção de Gjálp derreteu gelo demais e ergueu a barragem.",
    "O lago Grímsvötn, sob o Vatnajökull, solta enchentes com frequência; em 1996, a erupção de Gjálp derreteu tanto "
    "gelo que chegou a erguer a barragem de gelo do lago.")
acrescentar_trecho(10, 0, "The Grímsvötn volcano frequently causes large jökulhlaups from Vatnajökull.")

# 0011: sem causalidade entre o sangue extra e os 70 minutos
substituir(11, "explicacao",
    "e tem dois litros de sangue a mais que outras focas do seu tamanho, o que lhe permite ficar até 70 minutos debaixo d'água quando foge de perigo.",
    "e tem dois litros de sangue a mais que outras focas do seu tamanho; assustada ou fugindo de perigo, aguenta até "
    "70 minutos debaixo d'água.")

# 0013: "mais de 5 m", como na fonte
trocar(13, gancho="Nos Andes secos, a neve forma campos de lâminas que podem passar de 5 m de altura, os penitentes. Darwin "
    "teve de passar espremido entre elas em 1835. O segredo: sublimar gasta 8,5 vezes mais energia que derreter.")

# 0015: sai a explicação do sol (contradita pelo estudo de 2020); entra a hipótese do pedestal, com fonte nova
substituir(15, "explicacao",
    "Uma explicação proposta, a partir de bolas que migravam para o sul no Alasca: o musgo escuro absorve sol do lado "
    "iluminado e faz sombra do outro, o gelo derrete só do lado ensolarado, forma-se uma pequena depressão e a bola "
    "rola para dentro dela, e assim por diante.",
    "Uma hipótese para o movimento de cada bola: ela faz sombra no gelo embaixo dela, que derrete mais devagar; o "
    "gelo em volta baixa, a bola fica empoleirada num pedestal de gelo e acaba caindo dele para uma nova posição. "
    "Mas para que lado ela cai, e por que a colônia inteira se move junta, na mesma direção e velocidade, continua "
    "sem explicação: num estudo que acompanhou uma colônia, o rumo não seguiu a luz do sol, a inclinação da geleira nem o vento.")
substituir_trecho(15, 0,
    "Gilbert and Bartholomaus's evidence shows a southern migration in Alaska which suggests a mechanism: the dark "
    "coloured moss absorbs sun energy on the south side, and casts a shadow on the north side. "
    "This causes the ice to melt only on the sunny side, creating a small depression, the moss then rolls into the "
    "depression and the process continues [...] ",
    "")
CANDIDATOS[15 - 1]["fontes"].append({
    "url": "https://news.climate.columbia.edu/2020/06/12/moss-balls-travel-herds-glaciers",
    "titulo": "Balls of Moss Travel in Herds Atop Some Glaciers and We Don't Know Why",
    "idioma": "en",
    "trecho": (
        "Moss balls shield and insulate the ice underneath them from sunlight, reducing the rate of melt in these localized spots. "
        "As the rest of the ice melts around them, the moss ball is left elevated on a pedestal of ice. "
        "Scientists previously observed them teetering on the edges of their pedestals, and hypothesized that eventually, the moss balls would fall from their pedestals and roll into a new position to start the process over again. "
        "However, the exact reason the moss ball falls the direction it does remains an enigma. [...] "
        "for reasons still unknown, the entire colony of moss balls moves in unison—in the same directions and at the same speeds—in a coordinated, herd-like fashion. [...] "
        "their movement does not follow the overwhelming direction of sunlight, the downward slope of the glacier, or the direction of the prevailing winds. [...] "
        "In the end, the explanation for why these glacier mice move synchronously remains a mystery."
    ),
})

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
# 0010: o pico de 500.000 m³/s da Wikipedia está inflado ~10x (literatura: 40 a 53 mil m³/s); o número sai do texto.
substituir(10, "explicacao", "A enchente durou vários dias, com pico de 500.000 m³ por segundo, a maior já registrada ali.", "A enchente durou vários dias e foi a maior já registrada ali.")
