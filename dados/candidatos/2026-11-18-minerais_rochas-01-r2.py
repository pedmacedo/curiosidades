"""Rodada 2 de Minerais e rochas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-minerais_rochas-01.py"))
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


# 0001 (aprovado, opcional): a caverna está inundada desde 2015, então o calor vai para o passado
substituir(1, "gancho", "Lá dentro faz até 58 °C", "Lá dentro fazia até 58 °C")
substituir(1, "gancho", "uma pessoa aguenta uns dez minutos", "uma pessoa aguentava uns dez minutos")

# 0002: pronome ambíguo no gancho
substituir(2, "gancho", "ele estava em Florença e tinha vindo do espaço.",
    "o cristal já estava em Florença e tinha vindo do espaço.")

# 0007: Brewster batizou o efeito, não a pedra; a repulsão vem depois do contato
substituir(7, "gancho", "atrai cinzas e logo depois as repele", "atrai cinzas e, depois do contato, as repele")
substituir(7, "explicacao", "O nome atual foi dado por David Brewster em 1824.",
    "O nome piroeletricidade, dado ao efeito, veio de David Brewster em 1824.")

# 0011: as lendas foram inventadas (sem "fortes indícios"); Maria Antonieta e o pingente do French Blue
substituir(11, "explicacao",
    "Há fortes indícios de que as histórias de desgraça foram inventadas no início do século XX para dar "
    "mistério à pedra e aumentar seu apelo de venda, além de vender jornais.",
    "As lendas sobre a origem amaldiçoada da pedra foram inventadas no início do século XX, para lhe dar "
    "mistério e aumentar seu apelo de venda, além de vender jornais; e a publicidade em torno da maldição "
    "costumava valorizar a joia.")
substituir(11, "explicacao", "nunca usou o pingente em que ele estava.",
    "nunca usou o pingente do Tosão de Ouro, que levava o diamante azul do qual o Hope foi lapidado depois.")
acrescentar_trecho(11, 0,
    "It was stolen in 1792, re-cut by persons unknown, and recovered after a lapse of years, appearing under the Hope name in an 1839 gem catalogue from the Hope banking family. [...] "
    "In 1749, Louis XIV's great-grandson, Louis XV, had the French Blue set into a more elaborate jeweled pendant for the Order of the Golden Fleece by court jeweler André Jacquemin.")

# 0012: os geomantes faziam experimentos; nenhuma colher foi achada
substituir(12, "explicacao",
    "no século II a.C. geomantes chineses fizeram com ela uma \"colher que aponta para o sul\", usada em adivinhação.",
    "no século II a.C. geomantes chineses faziam experimentos com ela para criar uma \"colher que aponta para o "
    "sul\", usada em adivinhação. Nenhuma dessas colheres feitas de magnetita foi encontrada até hoje pelos "
    "arqueólogos.")
acrescentar_trecho(12, 0,
    "While this has been shown to work, archaeologists have yet to discover an actual spoon made of magnetite in a Han tomb.")

# 0014: desfecho atualizado, com fonte nova checada (anulado em 2022, retomado em julho de 2024)
substituir(14, "explicacao",
    "Em janeiro de 2022, depois de grandes protestos, a primeira-ministra sérvia anunciou o cancelamento do projeto.",
    "Em janeiro de 2022, depois de grandes protestos, a primeira-ministra sérvia anunciou o cancelamento do "
    "projeto. Em julho de 2024, porém, o Tribunal Constitucional da Sérvia considerou inconstitucional o "
    "decreto que o havia anulado, e o governo pôs o projeto de volta nos trilhos com um novo decreto.")
CANDIDATOS[14 - 1]["fontes"].append({
    "url": "https://balkangreenenergynews.com/serbia-officially-revives-rio-tintos-lithium-mining-project-jadar",
    "titulo": "Serbia officially revives Rio Tinto's lithium mining project Jadar (Balkan Green Energy News, 16/07/2024)",
    "idioma": "en",
    "trecho": (
        "Following the ruling of the Constitutional Court of Serbia last week that the decree that annulled the Jadar project in 2022 was unconstitutional, "
        "the Government of Serbia issued a new decree, reinstating the status of Rio Tinto’s proposed investment that the company had before. "
        "Project Jadar for a lithium mine and processing plant in Serbia hit a wall in January 2022, but now it is back on track."),
})

# 0002: gancho dentro dos 220 caracteres; 0014: data da matéria no trecho (sustenta "julho de 2024")
substituir(2, "gancho", "que procurassem um na natureza,", "que buscassem um natural,")
substituir_trecho(14, 1, "Following the ruling", "July 16, 2024 [...] Following the ruling")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(12, "explicacao", "Nenhuma dessas colheres feitas de magnetita foi encontrada até hoje pelos arqueólogos.",
    "Testes mostram que o método funciona, mas os arqueólogos ainda não acharam nenhuma dessas colheres de magnetita em tumbas da dinastia Han.")
