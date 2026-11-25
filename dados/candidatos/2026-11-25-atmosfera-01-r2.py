"""Rodada 2 de Atmosfera: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-atmosfera-01.py"))
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


# 0001: não foi o primeiro CFC; morte sóbria, sem descrição de método
trocar(1, gancho="O mesmo engenheiro americano criou a gasolina com chumbo e levou os CFCs para as geladeiras; esses gases "
                 "depois corroeram a camada de ozônio. Um historiador disse que nenhum ser vivo prejudicou tanto a atmosfera.")
substituir(1, "explicacao",
    "Com Albert Henne, Midgley sintetizou o diclorodifluorometano, o primeiro clorofluorocarboneto, vendido como Freon.",
    "Com Albert Henne, Midgley chegou ao diclorodifluorometano, um clorofluorocarboneto, que foi vendido como Freon e "
    "se espalhou também pelos aerossóis.")
substituir(1, "explicacao",
    "O fim também virou lenda: paralisado pela pólio desde 1940, ele foi achado "
    "estrangulado pelo sistema de cordas e polias que inventara para sair da cama. Costuma-se dizer que "
    "foi um acidente, mas o legista declarou suicídio.",
    "Paralisado pela pólio desde 1940, Midgley morreu em casa em 1944, aos 55 anos; o legista registrou a morte como "
    "suicídio.")
substituir_trecho(1, 0,
    "Midgley contracted polio in 1940 and lost the use of his legs; in 1944, he was found strangled to death by a device he devised to allow him to get out of bed unassisted. It is often reported that he had been accidentally killed by his own invention, but his death was declared by the coroner to be a suicide. ",
    "Midgley contracted polio in 1940 and lost the use of his legs [...] his death was declared by the coroner to be a suicide. ")
substituir_trecho(1, 0,
    "leaving him permanently paralyzed from the legs down. He devised an elaborate system of ropes and pulleys to lift himself out of bed. [...] ",
    "leaving him permanently paralyzed from the legs down. [...] "
    "On November 2, 1944, at the age of 55, he was found dead at his home in Worthington, Ohio. [...] ")
acrescentar_trecho(1, 0, "their use as a propellant in aerosol products")

# 0002: reprovado (fica como está)

# 0003: "prováveis erros"; sem o 1976; Farman começou em 1957
substituir(3, "gancho", "mas os valores, baixos demais, eram marcados como erro pelo controle de qualidade dos dados.",
    "mas o controle de qualidade marcava os valores, baixos demais, como prováveis erros.")
substituir(3, "explicacao", "trabalhava desde 1957 na estação de Halley", "começou a trabalhar em 1957 na estação de Halley")
substituir(3, "explicacao",
    "mas os algoritmos de controle de qualidade as rejeitaram de início como irreais, por "
    "serem baixas demais. Quando o programa rodou de novo sem essas marcas, o buraco apareceu nos dados "
    "desde 1976.",
    "mas os algoritmos de controle de qualidade marcavam esses valores, baixos demais, como prováveis erros, e eles "
    "ficaram fora das análises. Quando os dados brutos foram reprocessados sem essas marcas, o buraco apareceu também "
    "nos anos anteriores.")
substituir_trecho(3, 0, "When the software was rerun without the flags, the ozone hole was seen as far back as 1976. ", "[...] ")

# 0004: sem "verão" na queimadura; duas causas do resfriamento tropical
substituir(4, "gancho", "e o sol do verão em Washington queimaria a pele em cinco minutos",
    "e o sol em cidades como Washington queimaria a pele em cinco minutos")
substituir(4, "explicacao",
    "porque a própria perda de ozônio esfriaria a estratosfera a ponto de formar ali as nuvens que hoje só existem perto "
    "dos polos",
    "porque a perda de ozônio esfriaria a estratosfera e intensificaria a circulação de ar lá em cima, resfriando-a "
    "ainda mais, a ponto de formar ali as nuvens que hoje só existem perto dos polos")
acrescentar_trecho(4, 0, "More surprising, says Stolarski, is that the temperature change intensified the stratosphere’s large-scale, slow-moving circulation pattern. [...] "
    "As the circulation strengthened, the amount of cooling increased")

# 0005: reprovado (fica como está)

# 0006: data debatida; cianobactérias de 3,5 bilhões contestadas
substituir(6, "explicacao", "e só começou a se acumular entre 2,46 e 2,426 bilhões de anos atrás",
    "e só começou a se acumular há cerca de 2,4 bilhões de anos (a data exata é debatida; uma estimativa muito citada "
    "fica entre 2,46 e 2,426 bilhões de anos)")
substituir(6, "explicacao", "As cianobactérias, que podem ter surgido até 3,5 bilhões de anos atrás,",
    "As cianobactérias, que segundo algumas estimativas, ainda contestadas, já existiriam há 3,5 bilhões de anos,")
acrescentar_trecho(6, 0, "there is disagreement on the exact timing of this event. "
    "Scientific publications between 2016–2022 have differed in the inferred timing of the onset of atmospheric oxygenation by approximately 500 million years [...] "
    "the presence of cyanobacteria in the Archaean before the GOE is a highly controversial topic. "
    "Structures that are claimed to be fossils of cyanobacteria exist in rock formed 3.5 Ga.")

# 0007: a leitura do fundo do mar oxigenado foi revista
substituir(7, "explicacao", "o que se interpreta como o momento em que o oxigênio chegou ao fundo dos oceanos.",
    "o que por muito tempo foi lido como o momento em que o oxigênio chegou ao fundo dos oceanos; evidências mais "
    "recentes, porém, sugerem que o mar profundo continuou sem oxigênio por muito mais tempo.")
acrescentar_trecho(7, 0, "The available evidence suggests that the deep ocean remained anoxic and ferruginous as late as 580 Ma, well after the Great Oxygenation Event")

# 0008: aprovado; nota 4
trocar(8, nota_surpresa=4)

# 0009: só parte do potássio-40 vira argônio
substituir(9, "explicacao", "presente no potássio natural, que ao decair se transforma em argônio.",
    "presente no potássio natural; numa parte dos decaimentos ele vira argônio (na maioria, vira cálcio).")
acrescentar_trecho(9, 0, "Naturally occurring 40K, with a half-life of 1.25×109 years, decays to stable 40Ar (11.2%) by electron capture or positron emission, and also to stable 40Ca (88.8%) by beta decay.")

# 0010: insetos respiram ativamente
substituir(10, "explicacao",
    "Insetos não têm pulmões: o oxigênio chega aos tecidos por um sistema "
    "respiratório em boa parte passivo, que funciona mal em corpos grandes.",
    "Insetos não têm pulmões: o oxigênio chega aos tecidos por uma rede de tubos, e a ideia era que esse sistema, tido "
    "como passivo, funcionaria mal em corpos grandes.")
substituir(10, "explicacao", "Por isso há outras hipóteses,",
    "Além disso, pesquisas mostraram que os insetos respiram ativamente, comprimindo e expandindo esses tubos. Por isso "
    "há outras hipóteses,")
acrescentar_trecho(10, 0, "However, this hypothesis was predicated largely on the idea that insects did not actively breathe. "
    "Later research indicates that insects do indeed breathe, with \"rapid cycles of tracheal compression and expansion\".")

# 0012: Tateno não fica perto do Fuji; Post recebe parte do crédito
substituir(12, "explicacao", "dirigia o observatório aerológico de Tateno, perto do monte Fuji.",
    "dirigia o observatório aerológico de Tateno, no Japão.")
substituir(12, "gancho", "e o crédito muitas vezes vai para um aviador americano.",
    "e parte do crédito costuma ir para um aviador americano.")

# 0014: sem os 2.500 °C; a separação dos gases é na termosfera
substituir(14, "explicacao", "chegando a 2.000 °C ou mais conforme a atividade do Sol, e a 2.500 °C perto do topo.",
    "chegando a 2.000 °C ou mais conforme a atividade do Sol.")
substituir(14, "explicacao", "Nessa altitude, os gases deixam até de se misturar", "Na termosfera, os gases deixam até de se misturar")

# 0015 e 0016: aprovados; nota 3
trocar(15, nota_surpresa=3)
trocar(16, nota_surpresa=3)
