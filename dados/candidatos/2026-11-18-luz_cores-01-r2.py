"""Rodada 2 de Luz e cores: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-luz_cores-01.py"))
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

# 0001: a fonte só diz que talvez não soubessem do ouro
substituir(1, "gancho", "que os vidreiros talvez nem soubessem que estavam ali.", "e os vidreiros talvez nem soubessem que havia ouro na mistura.")

# 0003: a pesquisa é com universitários americanos
substituir(3, "gancho", "pesquisas de 2002 indicaram que até metade dos universitários ainda acredita em algo assim",
    "uma revisão de 2002 indicou que até metade dos universitários americanos ainda acredita em algo assim")
substituir(3, "explicacao", "até 50% dos universitários adultos acreditam", "até 50% dos universitários adultos nos Estados Unidos acreditam")

# 0005: Io é a mais interna das luas galileanas
substituir(5, "explicacao", "os eclipses de Io, a lua mais interna de Júpiter, eram cronometrados",
    "os eclipses de Io, a mais interna das quatro grandes luas de Júpiter descobertas por Galileu, eram cronometrados")

# 0009: a explicação aceita é a transpiração térmica de Reynolds
substituir(9, "explicacao", "O lado preto esquenta mais, e as moléculas de gás que batem nele ricocheteiam mais rápido, empurrando-o.",
    "O lado preto esquenta mais que o claro, e o gás rarefeito, ao contornar as bordas das palhetas, flui do lado frio para o "
    "quente, um efeito chamado transpiração térmica, proposto por Osborne Reynolds. Isso aumenta a pressão do lado preto e empurra a palheta.")
substituir_trecho(9, 0, "A partial explanation is that gas molecules hitting the warmer side of the vane will pick up some of the heat, bouncing off the vane with increased speed.",
    "The currently accepted theory was formulated by Osborne Reynolds, who theorized that thermal transpiration was the cause of the motion. [...] "
    "As gas moves from the cooler to the hotter side, the pressure on the hotter side increases.")

# 0010: a virada de Ritter no gancho
trocar(10, gancho="Em 1800, Herschel pôs um termômetro além do vermelho do espectro e achou uma luz invisível que esquenta: o infravermelho. "
    "Um ano depois, Ritter buscou além do violeta um raio que esfriasse e achou o ultravioleta.")

# 0016: causalidades corrigidas; Vossius
substituir(16, "explicacao", "mas ela falhava para ângulos maiores, em parte porque ele ajustou os dados para caberem na teoria.",
    "mas ela falhava para ângulos maiores; Ptolomeu se convenceu de que estava certa em parte porque ajustou os dados para caberem na teoria.")
substituir(16, "explicacao",
    "e foi acusado, por Fermat, Huygens e outros, de ter copiado Snell, acusação que hoje se considera injusta. Por isso, na França, ela costuma ser chamada de lei de Snell-Descartes.",
    "e foi acusado por Isaac Vossius, e depois por Fermat e Huygens, de ter copiado Snell, acusação que hoje se considera injusta. Na França, ela costuma ser chamada de lei de Snell-Descartes.")
acrescentar_trecho(16, 0, "In De natura lucis et proprietate (1662) Isaac Vossius said that Descartes had seen Snell's paper and concocted his own proof.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(9, "explicacao", "se a ampola for resfriada no escuro, as palhetas giram ao contrário",
    "se a parte de fora da ampola for resfriada depressa, as palhetas giram ao contrário")
