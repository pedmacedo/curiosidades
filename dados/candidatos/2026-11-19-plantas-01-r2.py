"""Rodada 2 de Plantas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-plantas-01.py"))
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


# 0002: "Outra é o erro" ficava solta; explicitar as duas limitações
substituir(2, "explicacao",
    "Ela também é relativamente lenta: cada molécula fixa algo como 3 a 10 moléculas de CO2 por segundo. Outra é o erro.",
    "Ela tem duas limitações. Uma é a lentidão: cada molécula fixa algo como 3 a 10 moléculas de CO2 por segundo. A outra é o erro.")

# 0007: o coautor é Jorge Arias (o trecho da Wikipedia escreve "Arius" e fica literal)
substituir(7, "explicacao",
    "O processo foi descrito em detalhe pelo botânico Ghillean Prance e por Jorge Arius.",
    "O processo foi descrito em detalhe pelos pesquisadores Ghillean Prance e Jorge Arias.")

# 0011: quem cresceu foram plantas regeneradas do tecido dos frutos, não a planta original
trocar(11, gancho=(
    "Tecido de frutos congelados havia cerca de 32 mil anos na Sibéria deu origem, em laboratório, a plantas "
    "que cresceram e floresceram. O material veio de despensas de esquilos soterradas no permafrost."))

# 0012: estudo recente achou variação genética baixíssima (três linhagens), não ausência de variação
substituir(12, "gancho", "geneticamente indistinguíveis", "quase idênticos geneticamente")
substituir(12, "explicacao",
    "e os testes genéticos não distinguem um exemplar do outro, sinal de que a espécie passou por um gargalo.",
    "e a variação genética entre eles é baixíssima, sinal de que a espécie passou por um gargalo. Uma análise "
    "de 2003 não achou diferença nenhuma entre as árvores; só técnicas genômicas mais novas, usadas pelo Jardim "
    "Botânico Real de Sydney e pela Universidade de Nova Gales do Sul, revelaram três linhagens, uma dominante "
    "e duas raras.")
CANDIDATOS[11]["fontes"].append({
    "url": "https://www.botanicgardens.org.au/discover-and-learn/plant-conservation-and-discoveries/genetic-diversity-discovered-wollemi-pine",
    "titulo": "Genetic diversity discovered in Wollemi Pine for the first time (Botanic Gardens of Sydney)",
    "idioma": "en",
    "trecho": (
        "Since the surprise discovery of the ancient Wollemi pine (Wollemia nobilis) in 1994, no genetic variation had been detected in this extremely rare tree. [...] "
        "A genetic analysis of the wild populations in 2003 did not reveal any differences between individual trees [...] "
        "New research by the University of NSW and the Royal Botanic Garden Sydney has for the first time found low genetic variation between some individual trees in the wild and research populations. [...] "
        "The findings confirm that there is very low variation in the Wollemi pine population. "
        "Three different “chlorotypes” or genetic lineages were identified, one dominant and two rare."),
})

# 0015: a fonte diz "can grow to 60 m"
substituir(15, "explicacao", "Pode passar de 60 metros de altura", "Pode chegar a 60 metros de altura")

# 0016: a última frase é interpretação dos autores
substituir(16, "explicacao",
    "Usando uma droga que fortalece a memória da recompensa, a planta faz as abelhas voltarem às suas flores e melhora seu sucesso reprodutivo.",
    "Na interpretação dos autores, ao reforçar a lembrança da recompensa, a planta tornaria as abelhas mais fiéis às suas flores e, com isso, aumentaria suas chances de reprodução.")
