"""Rodada 2 de Dinheiro: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-dinheiro-01.py"))
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


# 0001: não eram o dinheiro do dia a dia; raramente movidas; "alguns economistas"
trocar(1, gancho="Em Yap, na Micronésia, discos de pedra de até 4 toneladas mudavam de dono sem sair do lugar. Uma pedra que afundou no mar continuou sendo negociada.")
substituir(1, "explicacao", "e levadas de canoa.",
    "e levadas de canoa ou, as maiores, em jangadas de bambu. Serviam para transações sociais importantes e "
    "raras, como casamentos, heranças e acordos políticos.")
substituir(1, "explicacao", "Como as grandes eram pesadas demais para mudar de lugar",
    "Como as grandes eram pesadas demais e raramente eram movidas")
substituir(1, "explicacao", "Economistas costumam usar as pedras rai", "Alguns economistas usam as pedras rai")
acrescentar_trecho(1, 0, "On the return, the stones could be carried by canoe or (for the larger specimens) on bamboo rafts. [...] "
    "Rai stones were, and still are, used in rare important social transactions, such as marriage, inheritance, political deals")

# 0004: a conta tem de fechar
substituir(4, "explicacao", "Veio o cruzeiro, em 1942;", "Veio o cruzeiro, em 1942, valendo mil réis;")
substituir(4, "explicacao", "o cruzeiro de novo, em 1970;", "o cruzeiro de novo, em 1970, só uma troca de nome;")
substituir(4, "explicacao", "outra vez o cruzeiro, em 1990, com o Plano Collor;",
    "outra vez o cruzeiro, em 1990, com o Plano Collor, de novo só no nome;")

# 0005: "em muitas prisões"; sem "ex-prisioneiro"
substituir(5, "gancho", "Nas prisões dos EUA, depois da proibição do fumo,", "Em muitas prisões dos EUA, depois da proibição do fumo,")
substituir(5, "explicacao", "o economista R. A. Radford, ex-prisioneiro de guerra, descreveu", "o economista R. A. Radford descreveu")

# 0006: o inglês adotou o "daler" baixo-alemão
substituir(6, "explicacao",
    "Dessa família vem o \"dólar\", primeiro em espanhol e depois em inglês, que hoje dá nome a várias moedas do mundo.",
    "O inglês adotou a forma baixo-alemã \"daler\" por volta de 1550, e ela virou \"dollar\" por volta de 1600. "
    "Hoje o nome batiza várias moedas do mundo.")
acrescentar_trecho(6, 0, "The Low German word was adopted in English as daler by 1550, modified to dollar by about 1600.")

# 0007: "o mais habilidoso"; levou à forca
substituir(7, "gancho", "e mandou para a forca o maior falsificador do reino.", "e levou à forca o falsificador mais habilidoso do reino.")

# 0008: sem "muito cobre"; séculos XVII e XVIII
substituir(8, "gancho", "Na Suécia do século XVII, a maior moeda", "Na Suécia dos séculos XVII e XVIII, a maior moeda")
substituir(8, "explicacao", "A Suécia tinha muito cobre e pouca prata.", "A prata andava escassa na Suécia.")
acrescentar_trecho(8, 0, "As silver became scarce, the silver daler rose in value relative to the copper daler")

# 0009: custo atual; sem afirmar a lei
trocar(9, gancho="Fabricar uma moeda de 1 centavo nos EUA chegou a custar 3,69 centavos em 2024. Em novembro de 2025, a Casa da Moeda parou de produzi-las para circulação.")
substituir(9, "explicacao",
    "No começo dos anos 2010, o preço dos metais subiu tanto que fabricar cada moeda chegou a custar mais de "
    "2 centavos, o dobro do seu valor de face.",
    "Desde 2006, fabricar cada moeda custa mais do que ela vale. Em 2024, o custo chegou a 3,69 centavos, "
    "quase quatro vezes o valor de face.")
substituir(9, "explicacao",
    " Em setembro de 2026, o Congresso transformou a decisão em lei e permitiu que o comércio arredonde "
    "pagamentos em dinheiro para os 5 centavos mais próximos.",
    "")
acrescentar_trecho(9, 0, "Since 2006, the mint's costs for cents have exceeded the face value of the coin. [...] "
    "The cost to mint a cent in 2024 was 3.69 cents.")
