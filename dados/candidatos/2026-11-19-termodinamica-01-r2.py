"""Rodada 2 de Calor e energia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-termodinamica-01.py"))
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


# 0001: o gancho não pode pressupor que o efeito existe
substituir(1, "gancho", "mas os físicos ainda discutem quando e por que ele acontece.",
    "mas os físicos ainda discutem se, quando e por que ele acontece.")

# 0002: a fervura saiu da definição em 1948 (ponto triplo), não em 2019; "buscava precisão" sem apoio
trocar(2, nota_surpresa=3)
substituir(2, "explicacao", "O que ele buscava era precisão: mostrou que", "No mesmo trabalho, mostrou que")
substituir(2, "explicacao",
    "Hoje a água nem entra na definição: desde 2019, ela se apoia na constante de Boltzmann, sem depender de "
    "nenhuma propriedade da água. Assim, a fervura da água pura sob uma atmosfera virou um valor medido, cerca de "
    "99,974 °C na escala de calibração ITS-90.",
    "A fervura deixou de definir a escala já em 1948, quando a referência passou a ser o ponto triplo da água; "
    "desde 2019, a definição usa a constante de Boltzmann e nem depende mais da água. Com isso, a fervura da água "
    "pura sob uma atmosfera virou um valor medido: cerca de 99,974 °C na escala de calibração ITS-90.")
acrescentar_trecho(2, 0,
    "The melting and boiling points of water are no longer part of the definition of the Celsius temperature scale. "
    "In 1948, the definition was changed to use the triple point of water. [...] "
    "When the melting and boiling points of water ceased being part of the definition, they became measured quantities instead.")

# 0003: anacronismo "nascido nos EUA"
substituir(3, "explicacao", "Benjamin Thompson, nascido nos EUA e feito conde",
    "Benjamin Thompson, nascido na colônia britânica de Massachusetts e feito conde")
acrescentar_trecho(3, 0, "Born in Woburn, Massachusetts")

# 0005: o porquê da cachoeira, com a carta do próprio Joule (1845)
trocar(5, nota_surpresa=3)
substituir(5, "explicacao",
    "de medir a diferença de temperatura entre o alto e o pé da cascata de Sallanches. A tentativa "
    "se mostrou impraticável.",
    "de medir a diferença de temperatura entre o alto e o pé da cascata de Sallanches: se trabalho vira calor, a "
    "água que despenca deveria chegar um pouco mais quente lá embaixo. Numa carta publicada em 1845, ele já tinha "
    "proposto esse teste aos leitores e calculado que o Niágara esquentaria cerca de um quinto de grau Fahrenheit "
    "na queda. A tentativa se mostrou impraticável.")
acrescentar_trecho(5, 0,
    "He wrote a letter to the Philosophical Magazine, published in September 1845 describing his experiment.")
CANDIDATOS[4]["fontes"].append(
    {"url": "https://chemteam.info/Chem-History/Joule-Heat-1845.html",
     "titulo": "On the Existence of an Equivalent Relation between Heat and the ordinary Forms of Mechanical Power, J. P. Joule (Philosophical Magazine, 1845; texto reproduzido no ChemTeam)",
     "idioma": "en",
     "trecho": "Any of your readers who are so fortunate as to reside amid the romantic scenery of Wales or Scotland could, I doubt not, confirm my experiments by trying the temperature of the water at the top and at the bottom of a cascade. "
               "If my views be correct, a fall of 817 feet will course generate one degree of heat, and the temperature of the river Niagra will be raised about one fifth of a degree by its fall of 160 feet."})

# 0007: "abaixo de zero kelvin" sugere abaixo do zero absoluto; concordância
trocar(7, nota_surpresa=4)
substituir(7, "gancho", "Há sistemas com temperatura abaixo de zero kelvin, e eles não são frios",
    "Há sistemas com temperatura negativa na escala kelvin, e eles não são frios")
substituir(7, "gancho", "Em contato com elas, cedem calor, nunca recebem.",
    "Em contato com elas, eles cedem calor, nunca recebem.")

# 0008: o mecanismo é a expansão adiabática
trocar(8, nota_surpresa=4)
substituir(8, "explicacao", "e um gás que se expande assim esfria, como mostra o efeito Joule-Thomson",
    "e um gás que se expande assim, sem receber calor de fora, esfria (é a chamada expansão adiabática)")
substituir_trecho(8, 2, "making it the coldest natural place currently known.",
    "making it the coldest natural place currently known. [...] "
    "Cooling to sub cmbr temperature is by adiabatic expansion.")

# 0010: Blagden achava que o suor não explicava todo o resfriamento
substituir(10, "gancho", "O segredo era o suor.", "O suor era parte do segredo.")
substituir(10, "explicacao", "primeiro cientista ocidental a reconhecer oficialmente o papel do suor no controle da temperatura do "
    "corpo.",
    "primeiro cientista ocidental a reconhecer oficialmente o papel do suor no controle da temperatura do "
    "corpo. Ele próprio achava, porém, que o suor ajudava muito, mas não explicava todo o resfriamento.")
acrescentar_trecho(10, 1,
    "probably its effect was very considerable, but by no means sufficient to account for the whole of the cooling")

# 0014: a anedota de von Neumann não é confirmada
trocar(14, confianca="consenso_parcial", nota_surpresa=3)
substituir(14, "gancho", "segundo um relato,", "numa história não confirmada,")
substituir(14, "explicacao", "Segundo um dos relatos, von Neumann o aconselhou",
    "Segundo um dos relatos que circulam, von Neumann o aconselhou")
substituir(14, "explicacao",
    "Há outra versão da conversa, com palavras diferentes, e o próprio relato diz que Shannon talvez nem conhecesse "
    "bem a semelhança com a termodinâmica.",
    "A história, porém, não é confirmada: ela muda conforme quem a conta, existe outra versão com palavras "
    "diferentes, e a fonte observa que, no começo, Shannon parecia não ter muita noção da semelhança com a "
    "termodinâmica.")

# 0015: "engenheiro" John Perry sem apoio
substituir(15, "explicacao", "Em 1895, o engenheiro John Perry já contestava", "Em 1895, John Perry já contestava")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(5, "explicacao", "A tentativa se mostrou impraticável.", "A tentativa em Sallanches se mostrou impraticável.")
substituir(7, "gancho", "Em contato com elas, eles cedem calor, nunca recebem.", "Em contato com um corpo comum, eles cedem calor, nunca recebem.")
