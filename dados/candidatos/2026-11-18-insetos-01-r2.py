"""Rodada 2 de Insetos e artrópodes: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-insetos-01.py"))
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


# 0004: nem todas as abelhas sobrevivem; o que elas aguentam é o calor
substituir(4, "gancho", "A vespa morre; as abelhas aguentam.", "A vespa morre; as abelhas toleram até 50 °C.")

# 0005: as adultas comem a seiva; a bactéria vive no corpo (não necessariamente em glândulas)
substituir(5, "gancho", "As formigas-cortadeiras não comem as folhas que carregam: usam-nas para cultivar um fungo.",
    "As formigas-cortadeiras não carregam folhas para comê-las: usam-nas para cultivar um fungo.")
substituir(5, "explicacao", "que vivem em glândulas do corpo delas e secretam antibióticos",
    "que vivem no corpo delas e secretam antibióticos")
substituir_trecho(5, 0, "This mutualistic micro-organism lives in the metapleural glands of the ant. ", "[...] ")
acrescentar_trecho(5, 0, "This mutualistic relationship is further augmented by another symbiotic partner, a bacterium that grows on the ants and secretes chemicals; essentially, the ants use portable antimicrobials.")

# 0006: a supercolônia global é interpretação contestada
trocar(6, confianca="consenso_parcial",
    gancho="Espalhadas pelo mundo por acidente, as formigas-argentinas formam supercolônias enormes, e estudos indicam "
           "que as de continentes diferentes, apesar da distância, se comportam como uma só.")
substituir(6, "explicacao",
    "Estudos genéticos, químicos e de comportamento concluíram depois que as supercolônias de continentes diferentes formam, na verdade, uma só.",
    "Estudos genéticos, químicos e de comportamento indicaram depois que supercolônias de continentes diferentes "
    "se comportam como uma só. A ideia de supercolônia não é consenso: em 2004, pesquisadores de Stanford "
    "levantaram sérias dúvidas de que exista uma única supercolônia ao longo da Califórnia.")
CANDIDATOS[5]["fontes"].append({
    "url": "https://www.sciencedaily.com/releases/2004/04/040408084620.htm",
    "titulo": "Stanford University, via ScienceDaily (2004): estudos questionam a supercolônia de formigas-argentinas na Califórnia",
    "idioma": "en",
    "trecho": "Stanford University. (2004, April 8). [...] But new studies by Stanford University scientists are raising serious doubts about the existence of a single supercolony running through the Golden State.",
})

# 0008: a primeira mariposa ignora o feromônio da segunda; a média de duas é do gênero Mastophora
substituir(8, "explicacao", "A segunda é repelida pelo feromônio da primeira.",
    "A primeira ignora o feromônio da segunda, mas a segunda é repelida pelo da primeira.")
substituir(8, "explicacao", "Uma fêmea pega em média duas mariposas por noite",
    "Uma fêmea do gênero Mastophora, o das Américas, pega em média duas mariposas por noite")
acrescentar_trecho(8, 0, "Mastophora Holmberg, 1876 (syn. Agathostichus) – North and South America")

# 0009: Photuris não é só norte-americano; dizer de onde vieram os vaga-lumes do estudo
substituir(9, "explicacao", "Há pelo menos 64 espécies de Photuris, todas da América do Norte temperada.",
    "O estudo usou vaga-lumes adultos da região de Ithaca, no estado de Nova York.")
substituir_trecho(9, 0, "(which entomologists regard as beetles, not true flies) [...] ",
    "The study employed adult fireflies (which entomologists regard as beetles, not true flies) from the Ithaca, N.Y., area [...] ")
substituir_trecho(9, 1, " [...] At least 64 species are currently recognized, all restricted to temperate North America.", "")

# 0010: quem só chega ao Texas são as que deixam o México
substituir(10, "explicacao",
    "A primeira geração nova só chega ao Texas e a Oklahoma; a segunda, a terceira e a quarta reocupam o resto.",
    "As que deixam o México só chegam ao Texas e a Oklahoma; são as gerações seguintes, nascidas pelo caminho, "
    "que reocupam o resto dos Estados Unidos e o Canadá.")

# 0012: o ataque por trás é só às vezes
substituir(12, "gancho", "escolhe desvios que a tiram da vista da presa e pode levar até uma hora para atacá-la por trás.",
    "faz desvios de até uma hora, mesmo perdendo a presa de vista, para atacá-la pelo melhor ângulo.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(4, "explicacao", "e poucas delas bastam para vencer", "e poucas vespas bastam para vencer")
substituir(5, "explicacao", "Fora os humanos, só outros dois grupos de insetos", "Além das formigas, só outros dois grupos de insetos")
substituir(6, "explicacao",
    "A ideia de supercolônia não é consenso: em 2004, pesquisadores de Stanford levantaram sérias dúvidas de que exista uma única supercolônia ao longo da Califórnia. Os pesquisadores compararam essa extensão à da sociedade humana, que provavelmente a espalhou por suas viagens.",
    "Os autores desses estudos compararam essa extensão à da sociedade humana, que provavelmente a espalhou por suas viagens. Mas a ideia de uma supercolônia única não é consenso: em 2004, pesquisadores de Stanford levantaram sérias dúvidas de que exista uma só ao longo da Califórnia.")
trocar(6, nota_surpresa=4)
