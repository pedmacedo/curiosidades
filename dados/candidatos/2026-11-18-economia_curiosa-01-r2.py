"""Rodada 2 de Economia curiosa: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-economia_curiosa-01.py"))
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


# 0002: a bolha foi inflada em 1719 e estourou em 1720
substituir(2, "gancho", "A bolha que ele criou em 1720 deu origem à palavra \"milionário\".",
    "A bolha que ele inflou, e que estourou em 1720, deu origem à palavra \"milionário\".")

# 0004: sem o artigo original (Europe PMC não baixou), nada de "drástica" nem de ressalva sem trecho
substituir(4, "gancho", "famílias muito pobres", "famílias pobres")
substituir(4, "explicacao",
    "Em Hunan, onde a base é o arroz, a procura das famílias que receberam o desconto caiu de forma drástica.",
    "Em Hunan, onde a base é o arroz, as famílias que receberam o desconto passaram a comprar menos arroz.")

# 0005: a contagem começa em 1888, ainda no Império
substituir(5, "gancho",
    "Logo após a Proclamação da República, o Brasil viveu uma bolha em que as empresas listadas saltaram de pouco mais de 90 para cerca de 450 em três anos.",
    "Na virada do Império para a República, o Brasil viveu uma bolha em que as empresas listadas saltaram de pouco mais de 90 para cerca de 450 entre 1888 e 1891.")

# 0007: "muitas vezes"; etimologia sem atribuir cada palavra; moeda ruim/boa
substituir(7, "explicacao", "O truque mais esperto era não estragar a própria moeda, e sim fabricar",
    "Muitas vezes, o truque era não estragar a própria moeda, e sim fabricar")
substituir(7, "explicacao",
    "Daí o nome alemão \"Kipper und Wipper\": as balanças (\"Wippen\") que pendiam (\"kippen\") diante da moeda boa.",
    "Daí o nome alemão \"Kipper und Wipper\", tirado do vocabulário das balanças de pesar moedas, que pendiam diante da moeda boa.")
substituir(7, "explicacao", "para quem importasse moeda falsa", "para quem importasse moeda ruim ou exportasse a boa")

# 0010: sem causalidade da compra para o preço; o patrimônio era o da Bache
substituir(10, "gancho",
    "acumularam tanta prata que a onça saltou de menos de US$ 10 para mais de US$ 50 em poucos meses. Em 27 de março de 1980, fechou a US$ 10,80 e deixou corretoras à beira de grandes perdas.",
    "acumularam uma montanha de prata, boa parte em contratos alavancados, enquanto a onça saltava de menos de US$ 10 para mais de US$ 50. Em 27 de março de 1980, ela fechou a US$ 10,80.")
substituir(10, "explicacao",
    "e a SEC suspendeu a negociação das ações da própria Bache, cujo rombo de 122 milhões de dólares nas contas da família teria reduzido muito o patrimônio.",
    "e a SEC suspendeu a negociação das ações da própria Bache: o saldo devedor sem garantia das contas dos Hunt na corretora, de cerca de 122 milhões de dólares, teria reduzido muito o patrimônio da Bache.")

# 0013: a fonte só compara extensões
trocar(13, gancho="A bolha das ferrovias britânicas dos anos 1840 arruinou famílias, mas deixou trilhos de verdade: os projetos de 1844 a 1846 renderam cerca de 10 mil km, extensão equivalente a mais da metade da malha atual.")
substituir(13, "explicacao", "enquanto a rede ferroviária britânica de hoje tem perto de 18 mil km",
    "para comparar, a rede ferroviária britânica inteira de hoje tem perto de 18 mil km")

# 0014: contrato do xarope só até 1921; "provavelmente a grande maioria" das máquinas; plano de 1951
substituir(14, "gancho", "Parte da culpa era das máquinas automáticas, feitas só para essa moeda, e o chefe da empresa chegou a pedir",
    "Parte da culpa era das máquinas automáticas, na maioria feitas só para essa moeda, e o chefe da empresa pediu")
substituir(14, "explicacao", "Um contrato com os engarrafadores favorecia manter o preço.",
    "Até 1921, um contrato que fixava o preço do xarope vendido aos engarrafadores favorecia manter o preço final.")
substituir(14, "explicacao", "e as já instaladas só funcionavam com a moeda de 5 centavos.",
    "e provavelmente a grande maioria das já instaladas só aceitava a moeda de 5 centavos.")
substituir(14, "explicacao", "A equipe de preços bolou então o",
    "Antes disso, em 1951, a equipe de preços da empresa já tinha bolado o")
acrescentar_trecho(14, 0,
    "The contract guarantees the right to buy syrup from the Coca-Cola Company at the nominal price of $0.92 per gallon in perpetuity. [...] "
    "We argue that the model can help explain the Coca-Cola price rigidity, but only until 1921, the year a new contract was signed with bottlers [...] "
    "It is likely, therefore, that a considerable majority of the 400,000 machines were nickel-only machines in 1950. [...] "
    "1951: The “Single Coin Plan” is developed.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(13, "explicacao",
    "foram construídos cerca de 10.010 km de linhas a partir dos projetos de 1844 a 1846, para comparar, a rede ferroviária britânica inteira de hoje tem perto de 18 mil km.",
    "foram construídos 10.010 km de linhas a partir dos projetos de 1844 a 1846. Para comparar, a rede ferroviária britânica inteira de hoje tem perto de 18 mil km.")
