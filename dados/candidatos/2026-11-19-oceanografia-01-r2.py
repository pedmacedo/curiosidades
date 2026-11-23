"""Rodada 2 de Oceanos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-oceanografia-01.py"))
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


# 0001 (opcional): "calcularam" -> "previram"
substituir(1, "explicacao", "Os pesquisadores calcularam ainda que", "Os pesquisadores previram ainda que")

# 0004: desnível, não distância; sem a coluna de 200 m (o verbete se contradiz)
substituir(4, "gancho", "água gelada desce pelo fundo do mar por mais de 3,5 km.",
    "água gelada desce mais de 3,5 km de altura pelo fundo do mar.")
substituir(4, "explicacao",
    "essa água escorre pelo leito ao longo de cerca de 1.000 km, numa coluna de uns 200 m de largura e 200 m de espessura.",
    "essa água escorre pelo leito ao longo de cerca de 1.000 km.")
substituir_trecho(4, 0,
    "The descending column of water is approximately 200 m (660 ft) wide and 200 m (660 ft) thick and descends over a length of around 1,000 km (620 mi).",
    "The descending column of water [...] descends over a length of around 1,000 km (620 mi).")

# 0006: sem recorte de gênero; o gancho diz por que o vale importa
trocar(6, gancho="Proibida de embarcar por ser mulher, Marie Tharp mapeou o fundo do Atlântico pelas sondagens e achou "
    "o vale que indicava a deriva dos continentes. O colega desdenhou: \"conversa de menina\".")
substituir(6, "explicacao", "apontou Tharp como uma das quatro maiores cartógrafas do século XX.",
    "incluiu Tharp entre os quatro maiores cartógrafos do século XX.")

# 0007: a queixa era de cerca de quinze dias, não "várias semanas"
substituir(7, "explicacao", "demoravam várias semanas a mais para chegar a Nova York",
    "demoravam semanas a mais para chegar a Nova York")

# 0008: a causa é a estratificação, não a calmaria
substituir(8, "gancho", "Em águas calmas, um navio pode quase parar,", "Onde água doce cobre a salgada, um navio pode quase parar,")

# 0009: os 45° são da teoria; nas medições, 5° a 20°
substituir(9, "explicacao", "A superfície corre a 45° do vento, e cada camada abaixo",
    "Na teoria de Ekman, a superfície corre a 45° do vento (nas medições reais, o ângulo costuma ficar entre 5° e "
    "20°), e cada camada abaixo")
acrescentar_trecho(9, 0, "The differences between the theory and the observations are that the angle is between 5–20 degrees instead of the 45 degrees as expected")

# 0010: sem a frase do gelo glacial; GPS sem correção; depressão no oceano
substituir(10, "explicacao",
    " Outra feição grande, a elevação do Atlântico Norte, deve-se em parte ao peso do gelo que cobriu a América do "
    "Norte e o norte da Europa na última era glacial.", "")
substituir(10, "explicacao", "e por isso o receptor de um navio pode indicar", "e por isso um receptor sem correção, num navio, pode indicar")
substituir(10, "explicacao", "a −106 m, no sul da Índia,", "a −106 m, no oceano ao sul da Índia,")
substituir_trecho(10, 0,
    " Another large feature is the North Atlantic Geoid High (or North Atlantic Geoid Swell), caused in part by the weight of ice cover over North America and northern Europe in the Late Cenozoic Ice Age.",
    "")

# 0011: Dia D creditado a máquinas de latão derivadas da de Thomson; tempo de um ano ~4 horas (máquinas de 1876/1879)
substituir(11, "gancho", "Uma delas, americana, foi mantida em segredo na Segunda Guerra e usada para prever as marés do Dia D.",
    "Máquinas assim previram as marés do Dia D, e a americana foi mantida em segredo na Segunda Guerra.")
substituir(11, "explicacao",
    "Com um volante pesado, o operador traçava a curva de um ano em uns vinte e cinco minutos.",
    "Um volante pesado deixava o operador girar a máquina depressa, sem trancos nas polias, e as máquinas de 1876 "
    "e 1879 traçavam as marés de um ano para um porto em cerca de quatro horas.")
substituir(11, "explicacao",
    "A máquina americana No. 2 foi classificada como secreta, junto com os dados que produzia, e serviu para prever "
    "as marés do desembarque na Normandia e de todos os desembarques em ilhas na Guerra do Pacífico.",
    "A máquina americana No. 2 foi classificada como secreta, junto com os dados que produzia, e serviu para os "
    "desembarques em ilhas na Guerra do Pacífico; as marés do Dia D são creditadas a máquinas de latão derivadas do "
    "projeto original de Thomson.")
substituir_trecho(11, 0, " and so to run off a year's curve in about twenty-five minutes. [...]", " [...]")
acrescentar_trecho(11, 0, "Brass machines based on Thomson's original tide machine are credited for the accurate tide predictions in the build-up to the 1944 \"D-Day\" Normandy landings of World War II. [...] "
    "A year's tidal predictions for a given place, usually a chosen seaport, could be plotted by the 1876 and 1879 machines in about four hours")
