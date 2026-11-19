"""Rodada 2 de Som e ondas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-acustica-01.py"))
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

EPMC = _base.EPMC

# 0003: "aparentemente"; a altura diminuiu; Bidone passou despercebido
substituir(3, "gancho", "por um canal sem mudar de forma nem perder velocidade.", "por um canal, aparentemente sem mudar de forma nem perder velocidade.")
substituir(3, "explicacao", "Russell a seguiu a cavalo e só a perdeu depois de uma ou duas milhas, nas curvas do canal.",
    "Russell a seguiu a cavalo, a umas oito ou nove milhas por hora. A altura foi diminuindo aos poucos, e ele a perdeu "
    "depois de uma ou duas milhas, nas curvas do canal.")
substituir(3, "explicacao", "mas quase ninguém notou", "mas o trabalho passou despercebido pelos pesquisadores britânicos e holandeses")
acrescentar_trecho(3, 0, "overtook it still rolling on at a rate of some eight or nine miles an hour [...] "
    "Its height gradually diminished, and after a chase of one or two miles I lost it in the windings of the channel [...] "
    "Bidone's work seems to have gone unnoticed by researchers in the Netherlands and Britain")

# 0006: fator Q não é tempo; "o mesmo tipo de onda"
substituir(6, "gancho", "Hoje a mesma onda prende luz em esferinhas de vidro.", "Hoje o mesmo tipo de onda prende luz em esferinhas de vidro.")
substituir(6, "explicacao",
    "a luz dá voltas quase sem perdas e fica presa muito mais tempo do que o som numa galeria, o que serve para",
    "a luz dá voltas quase sem perdas, guiada pela reflexão interna total, e perde muito menos energia a cada oscilação "
    "do que o som nos melhores ressonadores acústicos, o que serve para")
acrescentar_trecho(6, 0, "The light waves are guided around almost perfectly by total internal reflection, leading to Q factors in excess of 1010 being achieved. "
    "This is far greater than the best values, about 104, that can be obtained in acoustics.")

# 0011: título certo; o contraponto do estudo controlado de 2009
substituir(11, "explicacao", "\"Ghosts in the Machine\"", "\"The Ghost in the Machine\"")
substituir(11, "explicacao", "A relação, porém, segue como sugestão a confirmar.",
    "Mas o experimento de 2003 não saiu numa revista científica, e um teste controlado de 2009, com 79 voluntários "
    "numa sala com e sem infrassom, achou sensações estranhas nas duas condições, mais ligadas à sugestionabilidade "
    "das pessoas do que ao som. A relação segue sem confirmação.")
CANDIDATOS[10]["fontes"].append(
    {"url": EPMC + "search?query=EXT_ID:18635163%20AND%20SRC:MED&resultType=core&format=json",
     "titulo": "The \"Haunt\" project (French, Haque, Bunton-Stasyshyn e Davis, Cortex, 2009) — resumo via Europe PMC", "idioma": "en",
     "trecho": "Participants (N=79) were required to spend 50 min in a specially constructed chamber, within which they were exposed to infrasound, complex EMFs, both or neither. [...] "
        "Although many participants reported anomalous sensations of various kinds, the number reported was unrelated to experimental condition but was related to TLS scores. "
        "The most parsimonious explanation for our findings is in terms of suggestibility."})

# 0014: lugares, não desertos; a sujeira é uma das explicações; som mais agudo
substituir(14, "gancho", "Em cerca de 35 desertos do mundo", "Em cerca de 35 lugares desérticos do mundo")
substituir(14, "explicacao", "e um pouco de sujeira nos grãos basta para silenciá-la",
    "e, segundo uma das explicações, um pouco de sujeira nos grãos basta para silenciá-la")
substituir(14, "explicacao", "em menor escala", "com um som mais agudo")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(11, "explicacao", "Mas o experimento de 2003 não saiu numa revista científica, e um teste controlado de 2009",
    "Mas um teste controlado de 2009")
substituir(11, "explicacao", "numa sala com e sem infrassom, achou sensações estranhas nas duas condições",
    "expostos a infrassom, a campos eletromagnéticos, aos dois ou a nenhum, achou sensações estranhas em todas as condições")
