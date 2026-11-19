"""Rodada 2 de Brasil colônia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-brasil_colonial-01.py"))
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


# 0002: a decisão da CITES citada é a de 2025
substituir(2, "explicacao",
    "Em 2024, a convenção internacional que controla o comércio de espécies ameaçadas, a CITES, decidiu que os "
    "estoques da madeira devem ser registrados.",
    "Em 2025, a convenção internacional que controla o comércio de espécies ameaçadas, a CITES, orientou "
    "fornecedores e usuários a melhorar a rastreabilidade da madeira e dos instrumentos feitos com ela.")
substituir_trecho(2, 0,
    "At the 2024 annual meeting of the Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES) it was resolved that existing stockpiles of the wood should be registered",
    "Future trade and conservation of the product was discussed at the November 2025 CITES conference, when suppliers and users were directed to improve traceability of the wood and musical instruments made from it.")

# 0004: o rabino, sem dizer de onde veio
substituir(4, "explicacao", "e um rabino vindo da Europa", "e um rabino, Isaac Aboab da Fonseca, enviado ao Recife em 1642")
acrescentar_trecho(4, 0, "It had a cantor, Josue Velosino, and a rabbi, Isaac Aboab da Fonseca, sent to Recife in 1642.")

# 0005: influência SOBRE Shakespeare; o tubérculo só tem nome francês; o mito vem dos relatos
trocar(5, gancho="Relatos sobre os tupinambás inspiraram o ensaio \"Dos canibais\", de Montaigne, visto como influência sobre A Tempestade, de Shakespeare. Na França, um tubérculo talvez leve o nome deles: topinambour.")
substituir(5, "explicacao", "O ensaio ajudou a formar o mito do \"bom selvagem\".",
    "Esses relatos também influenciaram a criação do mito do \"bom selvagem\", no Iluminismo.")

# 0006: Montgolfier já testava em 1782; sem "uma das primeiras demonstrações"; a fuga foi real
trocar(6, tipos_espanto=["historia_humana", "engenhosidade"])
substituir(6, "gancho", "Os irmãos Montgolfier só soltariam o seu balão em 1783.",
    "Joseph Montgolfier só faria um teste parecido em 1782: uma caixa de tafetá que bateu no teto.")
substituir(6, "explicacao", "É uma das primeiras demonstrações conhecidas do princípio do balão de ar quente.",
    "Isso o coloca entre os primeiros estudiosos a entender o princípio do balão de ar quente e a construir um "
    "protótipo que funcionava.")
substituir(6, "explicacao", "Ele morreu em Toledo, na Espanha, em 1724.",
    "Ele de fato fugiu para a Espanha, onde morreu de febre em Toledo, em 1724.")
substituir_trecho(6, 0, "a pioneer of lighter-than-air aerostat design [...]",
    "a pioneer of lighter-than-air aerostat design, being among the first scholars at that time to understand the operational principles of the hot air balloon and to build a functional prototype of such a device. [...]")
CANDIDATOS[5]["fontes"][1]["trecho"] = (
    "Joseph made his first definitive experiments in November 1782 while living in Avignon. [...] "
    "covered the sides and top with lightweight taffeta cloth. He crumpled and lit some paper under the bottom of the box. "
    "The contraption quickly lifted off its stand and collided with the ceiling.")

# 0008: bandeiras x bandeirantes; sem "sobretudo nos primeiros tempos"
substituir(8, "explicacao",
    "Os bandeirantes eram expedições que partiam de São Paulo para o interior em busca de ouro, pedras "
    "preciosas e, sobretudo nos primeiros tempos, indígenas para escravizar. Elas ajudaram a levar o "
    "domínio português",
    "As bandeiras eram expedições que partiam de São Paulo para o interior em busca de ouro, pedras "
    "preciosas e indígenas para escravizar. Algumas, como as de Raposo Tavares, ajudaram a levar o "
    "domínio português")

# 0009: Índia como grande fonte, não a única
trocar(9, gancho="Por mais de 2 mil anos, a Índia foi a grande fonte de diamantes do mundo. No século XVIII, o Brasil tomou esse lugar com as jazidas de Minas Gerais, e a Coroa portuguesa pôs a região sob controle total.")
substituir(9, "explicacao", "Durante muito tempo, só se encontravam diamantes em depósitos de rio no sul da Índia.",
    "Durante muito tempo, a maior parte dos diamantes vinha de depósitos de rio no sul da Índia.")
substituir(9, "explicacao",
    "Então as minas indianas se esgotaram, e o Brasil tomou o lugar delas: foi aqui que se acharam os primeiros "
    "diamantes de fora da Índia.",
    "Então as minas indianas se esgotaram, e o Brasil tomou o lugar delas.")

# 0010: a lenda cobre o relato inteiro
substituir(10, "explicacao", "No começo do século XVIII, os portugueses queriam entrar nesse mercado",
    "Conta a tradição que, no começo do século XVIII, os portugueses queriam entrar nesse mercado")
substituir(10, "explicacao", "Segundo a lenda, na volta ele trouxe as sementes escondidas",
    "Na volta, diz a lenda, ele trouxe as sementes escondidas")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(5, "explicacao", "Traduzido para o inglês em 1603, ele é visto desde 1781",
    "Traduzido para o inglês em 1603, o ensaio de Montaigne é visto desde 1781")
substituir(8, "explicacao", "já tinha comandado ataques a missões jesuíticas espanholas",
    "já tinha participado de ataques a missões jesuíticas espanholas")
