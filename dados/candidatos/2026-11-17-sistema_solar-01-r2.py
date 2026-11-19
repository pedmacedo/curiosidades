"""Rodada 2 de Sistema Solar: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-17-sistema_solar-01.py"))
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


def acrescentar_trecho(n, i_fonte, extra):
    CANDIDATOS[n - 1]["fontes"][i_fonte]["trecho"] += " [...] " + extra


# 0001: idade debatida
trocar(1, gancho="Os anéis de Saturno podem ser mais novos que os dinossauros, e estão chovendo sobre o planeta: talvez sumam em menos de 100 milhões de anos.")
substituir(1, "explicacao", "eles ainda são claros demais para serem velhos.",
    "eles ainda são claros demais para serem velhos. A idade, porém, ainda é debatida: há pesquisadores que "
    "argumentam que o anel B tem massa suficiente para diluir a poeira que cai nele sem escurecer, o que "
    "permitiria anéis bem mais antigos.")
acrescentar_trecho(1, 0, "However, new research indicates that the B Ring may be massive enough to have diluted infalling material and thus avoided substantial darkening over the age of the Solar System.")

# 0002: o contraste é com a radioatividade; sem os "horários dos eclipses"
substituir(2, "explicacao", "A energia não vem de um interior quente desde a formação, como na Terra, mas do atrito:",
    "A principal fonte de calor não é o decaimento de elementos radioativos, como na Terra, mas o atrito:")
substituir(2, "explicacao", "os horários de seus eclipses atrás de Júpiter foram usados na primeira medição da velocidade da luz.",
    "foi observando Io que se fez a primeira medição da velocidade da luz.")
acrescentar_trecho(2, 0, "Unlike Earth and the Moon, Io's main source of internal heat comes from tidal dissipation rather than radioactive isotope decay")

# 0003: "um dos mais refletores"; oceano global
substituir(3, "explicacao", "o corpo mais refletor do Sistema Solar", "um dos corpos mais refletores do Sistema Solar")
substituir(3, "explicacao", "com cerca de 10 km de espessura.",
    "com cerca de 10 km de espessura. Medições posteriores de uma leve oscilação da lua na órbita indicaram "
    "que a crosta de gelo está solta do núcleo rochoso, ou seja, que o oceano é global.")
acrescentar_trecho(3, 0, "suggests that the entire icy crust is detached from the rocky core and therefore that a global ocean is present beneath the surface")
substituir(3, "fontes", None, None) if False else None
CANDIDATOS[2]["fontes"][0]["trecho"] = CANDIDATOS[2]["fontes"][0]["trecho"].replace(
    "the most reflective body in the Solar System [...] ", "one of the most reflective bodies of the Solar System [...] ")

# 0004: sem os 23 graus; hipótese do impacto
substituir(4, "gancho", "passa 42 anos seguidos sob o Sol", "passa cerca de 42 anos seguidos sob o Sol")
substituir(4, "explicacao", "O eixo de rotação da Terra é inclinado cerca de 23 graus, e é isso que produz as estações.",
    "O eixo de rotação da Terra é levemente inclinado, e é isso que produz as estações.")
substituir(4, "explicacao", "O planeta gira como uma bola rolando pela órbita.",
    "O planeta gira como uma bola rolando pela órbita. Uma das hipóteses para esse tombo é uma colisão, no "
    "passado, com um corpo do tamanho da Terra.")
acrescentar_trecho(4, 0, "the Earth-sized impactor theorised to be behind Uranus's axial tilt")

# 0006: "por volta de 1900"; estudo de 2024; contraponto
substituir(6, "explicacao", "Há cerca de um século, seu comprimento chegava a 40.000 km",
    "Por volta de 1900, seu comprimento chegava a 40.000 km")
substituir(6, "explicacao",
    "Uma mancha foi vista em Júpiter no século XVII, mas pode ter sido outra tempestade, e é possível que a "
    "atual tenha sido avistada pela primeira vez só em 1830.",
    "Uma mancha foi vista em Júpiter entre 1665 e 1713, e um estudo de 2024 sugere que era outra tempestade, "
    "que sumiu; a atual talvez tenha sido avistada pela primeira vez só em 1830.")
substituir(6, "explicacao", "nem se a redução faz parte de uma flutuação periódica.",
    "nem se a redução faz parte de uma flutuação periódica. E nem todos acham que ela esteja morrendo: para "
    "alguns astrônomos, o tamanho visível reflete a cobertura de nuvens, e não o vórtice por baixo.")
acrescentar_trecho(6, 0, "A 2024 study of historical observations suggests that the \"permanent spot\" observed from 1665 to 1713 may not be the same as the modern Great Red Spot observed since 1831. [...] "
    "other astronomers believe the apparent size of the spot reflects its cloud coverage and not the size of the underlying vortex")

# 0009: metano e etano
substituir(9, "gancho", "Só que de metano, a −179 °C", "Só que de metano e etano, a −179 °C")
substituir(9, "explicacao", "O clima tem vento e chuva, que esculpem dunas, rios, lagos e mares.",
    "O clima tem vento e chuva, que esculpem dunas, rios, lagos e mares, provavelmente de metano e etano líquidos.")
CANDIDATOS[8]["fontes"][0]["trecho"] = CANDIDATOS[8]["fontes"][0]["trecho"].replace(
    "such as dunes, rivers, lakes, seas [...] ", "such as dunes, rivers, lakes, seas (probably of liquid methane and ethane), and deltas [...] ")

# 0010: menos de uma hora de busca
substituir(10, "gancho", "e o planeta foi achado no mesmo dia em que o astrônomo apontou o telescópio.",
    "e o astrônomo que apontou o telescópio para lá o achou em menos de uma hora.")
substituir(10, "explicacao", "seguiu os cálculos e encontrou o planeta.",
    "seguiu os cálculos e encontrou o planeta. Levou menos de uma hora de busca, e Netuno estava a menos de 1 "
    "grau da posição prevista.")
acrescentar_trecho(10, 0, "Neptune was discovered just after midnight, after less than an hour of searching and less than 1 degree from the position Le Verrier had predicted, a remarkable match.")

# 0011: mecanismo pela NASA (Curiosity)
substituir(11, "explicacao",
    "A atmosfera é fina e quase não tem oxigênio e nitrogênio, então esse tipo de espalhamento, chamado de "
    "Rayleigh, não domina. O ar marciano está cheio de poeira vermelha levantada por ventos fortes, e é ela que "
    "define a cor do céu, por outro processo, o espalhamento de Mie. O resultado é um pôr do sol com tons de azul.",
    "A atmosfera marciana é muito rarefeita, então o espalhamento pelas moléculas do ar, chamado de Rayleigh, "
    "pesa pouco. Quem manda é a poeira fina levantada pelos ventos. Segundo a NASA, os grãos dessa poeira "
    "deixam a luz azul atravessar o ar com mais eficiência que as cores de onda mais longa, e por isso o azul "
    "fica concentrado na região do céu em volta do Sol, enquanto o amarelo e o vermelho se espalham pelo "
    "resto. O efeito fica mais forte no fim da tarde, quando a luz percorre um caminho mais longo pela "
    "atmosfera.")
CANDIDATOS[10]["fontes"].insert(0, {
    "url": "https://science.nasa.gov/photojournal/sunset-in-mars-gale-crater", "titulo": "Sunset in Mars' Gale Crater",
    "idioma": "en",
    "trecho": "Dust in the Martian atmosphere has fine particles that permit blue light to penetrate the atmosphere more efficiently than longer-wavelength colors. "
              "That causes the blue colors in the mixed light coming from the sun to stay closer to sun's part of the sky, compared to the wider scattering of yellow and red colors. "
              "The effect is most pronounced near sunset, when light from the sun passes through a longer path in the atmosphere"})
_t = CANDIDATOS[10]["fontes"][1]["trecho"]
CANDIDATOS[10]["fontes"][1]["trecho"] = _t[: _t.index(" [...] Mars has a thin atmosphere")] + " [...] " + _t[_t.index("One study also reported"):]
