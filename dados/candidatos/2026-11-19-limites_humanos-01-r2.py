"""Rodada 2 de Limites humanos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-limites_humanos-01.py"))
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


# 0002: "um dos voluntários mais frequentes", sem superlativo dos 46,2 g, Murphy propôs os sensores, origem disputada
substituir(2, "gancho", "a Lei de Murphy, nascida em testes anteriores com trenós.",
    "a Lei de Murphy, que teria nascido em testes anteriores com trenós.")
substituir(2, "explicacao", "e a cobaia mais frequente dos testes foi ele mesmo.",
    "e ele próprio foi um dos voluntários mais frequentes dos testes.")
substituir(2, "explicacao", ", a maior aceleração conhecida enfrentada voluntariamente por alguém", "")
substituir(2, "explicacao",
    "Os testes mostraram que, bem preso por cintos, um piloto sobrevive a impactos muito maiores do que se pensava, "
    "e que o assento virado para trás é o mais seguro.",
    "Os testes mostraram que um piloto bem preso por cintos pode sair andando de um acidente, desde que o assento "
    "não se solte, e que o assento virado para trás é o mais seguro.")
substituir(2, "explicacao",
    "Num teste anterior, um engenheiro chamado Edward Murphy instalou sensores no cinto de Stapp; quando eles "
    "falharam por um erro de ligação, Murphy reclamou do técnico, e a frase virou lei.",
    "Anos antes, o engenheiro Edward Murphy propôs medir as forças com sensores presos ao cinto de Stapp; num "
    "teste, os sensores falharam porque tinham sido ligados errado, Murphy pôs a culpa no técnico, e a "
    "reclamação acabou virando lei.")

# 0003: Ross monitorou a saúde; não é dito médico
substituir(3, "gancho", "mas o médico que o acompanhou registrou paranoia",
    "mas quem monitorou sua saúde registrou paranoia")

# 0004: "à base de", transição de dez dias, "nesse paciente", ressalva final
trocar(4, nota_surpresa=3)
substituir(4, "gancho", "só com chá, café, água com gás e vitaminas", "à base de chá, café, água com gás e vitaminas")
substituir(4, "explicacao", "Em 11 de julho de 1966, comeu um ovo cozido",
    "O jejum terminou em 30 de junho de 1966; depois de dez dias de transição, com sal e depois açúcar, em 11 de "
    "julho ele comeu um ovo cozido")
substituir(4, "explicacao", "concluiu que o jejum prolongado não lhe causara efeitos nocivos",
    "concluiu que, nesse paciente, o jejum prolongado não deixara efeitos nocivos")
substituir(4, "explicacao", "por medo de estimular comportamentos perigosos.",
    "por medo de estimular comportamentos perigosos. É um caso isolado, feito com acompanhamento médico e "
    "suplementos, e não uma prova de que jejuns longos sejam seguros.")
acrescentar_trecho(4, 0, "For the next ten days, the doctors placed him on a diet of salt and then sugar in preparation for solid food.")

# 0006: sem citação alterada; túnel entrou depois de 2009
substituir(6, "gancho", "O criador da prova pensou: \"eu faria pelo menos 160\".",
    "O criador da prova pensou que faria pelo menos 160 km.")
substituir(6, "explicacao", "Desde 2009, com a prisão fechada, o trajeto passa por um túnel sob ela.",
    "Depois que a prisão fechou, em 2009, o trajeto passou a incluir um túnel sob ela.")

# 0008: título original do documentário
substituir(8, "explicacao", "no documentário Asas da Esperança, de 1998.",
    "no documentário Wings of Hope (\"Asas da esperança\"), de 1998.")

# 0009: o porquê dos 12 trisavós
substituir(9, "explicacao", "A dúvida, porém, tem solução simples: Jeanne tinha 16 trisavós distintos, e Yvonne, só 12.",
    "A dúvida, porém, tem solução simples: como Jeanne se casou com um primo de segundo grau duplo, Yvonne tinha "
    "só 12 trisavós distintos, contra 16 da mãe.")
acrescentar_trecho(9, 0, "Jeanne married her double second cousin, Fernand Nicolas Calment (1868–1942). "
    "Their paternal grandfathers were brothers, and their paternal grandmothers were sisters.")

# 0011: mais de um século
substituir(11, "explicacao", "A ideia tem quase um século.", "A ideia tem mais de um século.")

# 0012: Wyss-Dunant criou o conceito e o chamou de zona letal
trocar(12, nota_surpresa=3)
substituir(12, "explicacao", "expressão criada em 1953 pelo médico suíço Edouard Wyss-Dunant",
    "conceito criado em 1953 pelo médico suíço Edouard Wyss-Dunant, que a chamou de zona letal")

# 0013: local da batida não informado; data por "dezoito dias depois"
substituir(13, "explicacao", "Andreas Mihavecz tinha 18 anos e estava de passageiro num carro que bateu, em Bregenz.",
    "Andreas Mihavecz, de Bregenz, tinha 18 anos e estava de passageiro num carro que bateu.")
substituir(13, "explicacao", "Em 19 de abril, um policial que foi ao porão", "Dezoito dias depois, um policial que foi ao porão")
