"""Rodada 2 de Biomimética: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-biomimetica-01.py"))
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


# 0002: os 10%/15% vêm de divulgação e valem para o redesenho inteiro
substituir(2, "explicacao",
    "Segundo as descrições do projeto, o novo nariz reduziu o ruído e permitiu andar 10% mais rápido gastando 15% menos energia.",
    "Segundo os relatos mais divulgados do caso, o redesenho reduziu o ruído e permitiu andar 10% mais rápido gastando 15% menos energia.")

# 0003: o 0,6% é da gota; o nome "efeito lótus" veio depois de 1977
substituir(3, "gancho", "fazem a gota encostar em só 0,6% da superfície",
    "fazem só 0,6% da superfície da gota tocar a folha")
substituir(3, "explicacao", "o descreveu com Ehler em 1977 e o chamou de \"efeito lótus\"",
    "começou a descrevê-lo com Ehler em 1977 e depois o batizou de \"efeito lótus\"")

# 0004: o Eastgate dispensa ar-condicionado, mas usa ventiladores
substituir(4, "gancho", "foi projetado para se refrescar só com ventilação natural, imitando cupinzeiros",
    "foi projetado para se refrescar sem ar-condicionado, imitando cupinzeiros")

# 0005: o estudo de 2015 contradiz trabalhos anteriores
trocar(5, confianca="consenso_parcial")

# 0006: "não de água" era forte demais; o Teflon é exceção à aderência, não à limpeza
substituir(6, "explicacao", "e não de água ou de química especial",
    "e não de cola, sucção ou química especial")
substituir(6, "explicacao", " A exceção é o Teflon.", "")
substituir(6, "explicacao",
    "Como os geckos aderem a quase qualquer material foi assunto de estudo por mais de um século.",
    "Como os geckos aderem a quase qualquer material (o Teflon é exceção) foi assunto de estudo por mais de um século.")

# 0007: o estudo testou só quatro espécies; e não achou áreas que atraem água
substituir(7, "explicacao",
    "Num estudo de 2010 em câmara de neblina, só Onymacris unguicularis assumiu a postura",
    "Num estudo de 2010 em câmara de neblina, das quatro espécies testadas, só Onymacris unguicularis assumiu a postura")
substituir(7, "explicacao",
    "A conclusão dos autores: o comportamento pesa mais que a textura das costas.",
    "O mesmo estudo não encontrou áreas que atraem água nas carapaças de nenhuma das quatro espécies. "
    "A conclusão dos autores: o comportamento pesa mais que a textura das costas.")
acrescentar_trecho(7, 1,
    "However, no hydrophilic areas could be identified either on the elytra, pronotum or head in any of our")

# 0009: a autolimpeza vale para o modelo britânico original, não para toda tacha
trocar(9, gancho="As tachas refletivas \"olho de gato\" originais, criadas na Inglaterra em 1934, se limpam sozinhas: "
                 "quando um carro passa, a borracha afunda e um limpador esfrega os refletores. Já o gato da história é incerto.")
substituir(9, "explicacao",
    "e a água de chuva acumulada na base melhora a limpeza.",
    "e a água de chuva acumulada na base melhora a limpeza. Nem toda tacha faz isso: as fixas, como a "
    "equivalente mais próxima usada nos EUA, não têm o mecanismo de autolimpeza.")
acrescentar_trecho(9, 1,
    "The closest equivalent in the United States is the Stimsonite retroreflective raised pavement marker, a fixed marker without the rubber self-cleaning property.")

# 0011: Watts e Fish estimaram por modelagem; os tubérculos têm um custo
substituir(11, "explicacao",
    "Em testes, os pesquisadores Watts e Fish mediram 4,8% a mais de sustentação num perfil com tubérculos.",
    "Num dos primeiros estudos, com modelagem em computador, os pesquisadores Watts e Fish estimaram 4,8% a "
    "mais de sustentação num perfil com tubérculos. Outros trabalhos mostraram um custo: os tubérculos podem "
    "baixar a sustentação máxima, em troca de uma perda mais suave depois do estol.")
acrescentar_trecho(11, 0,
    "Using computational modeling, it was determined that the presence of tubercles produces a delay in the angle of attack until stall [...] "
    "Leading-edge tubercles have been found to reduce the point of maximum lift and increase the region of post-stall lift.")

# 0012: o azul da Morpho é iridescente
substituir(12, "explicacao", "e o resultado é um azul vibrante que não muda com o ângulo de visão",
    "e o resultado é um azul vibrante")
substituir(12, "explicacao", "A pista é antiga:", "O fenômeno é conhecido há séculos:")
