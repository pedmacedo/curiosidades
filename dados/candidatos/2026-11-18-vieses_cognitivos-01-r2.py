"""Rodada 2 de Vieses cognitivos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-vieses_cognitivos-01.py"))
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


# 0002: medianas, não todos
substituir(2, "explicacao", "As primeiras multiplicações serviam de âncora, e todos ficaram muito abaixo.",
    "As primeiras multiplicações serviam de âncora, e as estimativas medianas dos dois grupos ficaram muito abaixo.")

# 0004: ele mencionou o nome
substituir(4, "explicacao",
    "depois de ouvir falar uma vez do grupo militante alemão Baader-Meinhof, passou a encontrar o nome por "
    "toda parte",
    "depois de mencionar uma vez o nome do grupo militante alemão Baader-Meinhof, passou a encontrá-lo por "
    "toda parte")

# 0005: o relato clássico, com a data
substituir(5, "explicacao", "Em 1913, no Cassino de Monte Carlo, a bola de uma roleta caiu no preto 26 vezes seguidas.",
    "Segundo o relato que se tornou clássico, em 18 de agosto de 1913, no Cassino de Monte Carlo, a bola de "
    "uma roleta caiu no preto 26 vezes seguidas.")
acrescentar_trecho(5, 0, "An example of the gambler's fallacy occurred in a game of roulette at the Monte Carlo Casino on August 18, 1913, when the ball fell in black 26 times in a row.")

# 0006: "pesquisadores"; o efeito, quando aparece, é pequeno
substituir(6, "gancho", "dois economistas acharam", "dois pesquisadores acharam")
substituir(6, "explicacao", "os economistas Joshua Miller e Adam Sanjurjo", "os pesquisadores Joshua Miller e Adam Sanjurjo")
substituir(6, "explicacao", "Outros estudos recentes não acharam nada, e a discussão continua.",
    "Outros estudos recentes não acharam nada. E, onde aparece, o efeito é pequeno e se limita a poucos "
    "jogadores. A discussão continua.")
acrescentar_trecho(6, 0, "Moreover, evidence suggests that only a small subset of players may show a \"hot hand\" and, among those who do, the magnitude (i.e., effect size) of the \"hot hand\" tends to be small.")

# 0007: o resultado do experimento de 1969
substituir(7, "explicacao", "Em 1969, um experimento de Jon Jecker e David Landy testou a ideia.",
    "Em 1969, Jon Jecker e David Landy testaram a ideia: estudantes que ganharam dinheiro num concurso e "
    "depois receberam do próprio pesquisador o pedido de devolvê-lo passaram a gostar mais dele do que os "
    "outros grupos.")
acrescentar_trecho(7, 0, "All three groups were then asked how much they liked the researcher. "
    "The second group liked him the least, the first group the most")

# 0008: estudantes num teste; os limites do efeito
trocar(8, confianca="consenso_parcial",
    gancho="Num teste com estudantes, ninguém quis a assinatura só impressa da Economist, que custava o mesmo que impressa mais digital. Sem essa opção inútil no menu, a maioria passou a escolher a mais barata.")
substituir(8, "explicacao",
    "faz a vizinha mais cara parecer um ótimo negócio.",
    "faz a vizinha mais cara parecer um ótimo negócio. O efeito tem limites, porém: algumas pesquisas não o "
    "encontraram em situações de compra mais realistas.")
acrescentar_trecho(8, 0, "Some research suggests that the attraction effect does not appear in realistic purchasing scenarios, for example when options are presented graphically, or when the target and the competitor are not exactly of the same value.")
