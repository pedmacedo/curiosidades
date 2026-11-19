"""Rodada 2 de Literatura: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-literatura-01.py"))
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


# 0005: dois terços dos papéis foram à Bodleiana em 1961
substituir(5, "gancho", "O destino do acervo só se decidiu na Justiça de Israel, em 2016.", "Parte dela só teve destino decidido pela Justiça de Israel em 2016.")
substituir(5, "explicacao", "levando uma mala de papéis de Kafka,", "levando uma mala de papéis de Kafka,")
acrescentar_trecho(5, 0, "In 1961, at the request of Kafka's heirs (the daughters of his sisters), approximately two-thirds of Kafka's papers were given to the Bodleian Library, at the University of Oxford.")

# 0007: autor fictício, não personagem
substituir(7, "gancho", "Malba Tahan, o sábio árabe de \"O Homem que Calculava\", nunca existiu.", "Malba Tahan, o suposto autor árabe de \"O Homem que Calculava\", nunca existiu.")

# 0012: o gancho passa para o chinês aprendido escondido
trocar(12, gancho="A autora do \"Genji\", um dos primeiros romances do mundo (Japão, c. 1000), aprendeu chinês ouvindo as aulas "
    "do irmão. Na corte, fingia não saber a língua, mas a ensinava em segredo à imperatriz.",
    tipos_espanto=["historia_humana", "contraintuitivo"])
substituir(12, "explicacao", "Na época, as damas da corte eram conhecidas", "Nem o nome verdadeiro dela é conhecido. Na época, as damas da corte eram conhecidas")

# 0013: a cena da roupa é anedota não confirmada
substituir(13, "gancho", "Segundo colegas, começou a tirar a roupa de emoção.", "Conta-se que começou a tirar a roupa de emoção.")
substituir(13, "explicacao",
    "Segundo relatos de colegas da sala de leitura, no dia em que entendeu o que estava lendo, ele começou a tirar peças de roupa e a correr pela sala gritando de alegria.",
    "Segundo uma anedota atribuída a colegas da sala de leitura, impossível de confirmar, no dia em que entendeu o que "
    "estava lendo ele começou a tirar peças de roupa e a correr pela sala gritando de alegria.")

# 0015: Robinson; coleção posta à venda
substituir(15, "explicacao", "a coleção de um professor americano vendida pela casa Christie's",
    "a coleção do americano David Moore Robinson, posta à venda pela casa Christie's em 2011")
substituir(5, "explicacao", "com diários, notas e esboços.",
    "com diários, notas e esboços. Em 1961, a pedido dos herdeiros de Kafka, cerca de dois terços dos papéis foram para "
    "a Biblioteca Bodleiana, em Oxford; o resto ficou com Brod.")
substituir(7, "gancho", "que nunca pisou nos desertos que descrevia e que, na escola, chegou a ser reprovado em álgebra.",
    "que nunca pisou nos desertos que descrevia e, na escola, foi reprovado em álgebra.")
