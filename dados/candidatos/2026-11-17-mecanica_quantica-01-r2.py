"""Rodada 2 de Física quântica: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-17-mecanica_quantica-01.py"))
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


# 0002 (sugestão opcional do verificador): observar não exige um observador
substituir(2, "explicacao", "cada medição faz o sistema \"colapsar\" num estado definido.",
    "cada medição faz o sistema \"colapsar\" num estado definido, e a \"observação\" pode ser só a absorção de "
    "uma partícula, sem ninguém olhando.")
acrescentar_trecho(2, 0, "an observation can simply be the absorption of a particle, without the need of an observer in any conventional sense.")

# 0003: os recordes vieram de grades de difração
trocar(3, gancho="Moléculas com até 2.000 átomos já se comportaram como ondas e formaram padrões de interferência, como no famoso experimento da fenda dupla.")
substituir(3, "explicacao",
    "Depois vieram átomos e moléculas cada vez maiores: o buckminsterfulereno, uma bola de 60 átomos de "
    "carbono, em 2002; moléculas de 430 átomos em 2011; e moléculas de até 2.000 átomos em 2019.",
    "Depois vieram átomos e moléculas cada vez maiores, muitas vezes em versões do experimento com grades de "
    "difração no lugar das duas fendas: o buckminsterfulereno, uma bola de 60 átomos de carbono; moléculas de "
    "430 átomos em 2011; e moléculas de até 2.000 átomos em 2019.")
acrescentar_trecho(3, 0, "In 2013, a quantum interference experiment (using diffraction gratings, rather than two slits) was successfully performed with molecules that each comprised 810 atoms (whose total mass was over 10,000 daltons). The record was raised to 2000 atoms")

# 0004: o canal China-Áustria não usou entrelaçamento; Bell testa a física local
substituir(4, "explicacao",
    "Isso permite a criptografia quântica: produzindo pares de fótons entrelaçados, é possível criar chaves "
    "secretas em que qualquer tentativa de interceptação é detectada.",
    "Propriedades quânticas da luz também permitem a criptografia quântica, com chaves secretas em que "
    "qualquer tentativa de interceptação é detectada.")
substituir(4, "explicacao", "lançado em 15 de agosto de 2016", "lançado em agosto de 2016")
substituir(4, "explicacao", "testou a desigualdade de Bell, a prova do entrelaçamento,",
    "testou a desigualdade de Bell, que põe à prova se o mundo pode ser explicado por uma física \"local\" clássica,")
substituir(4, "explicacao", "a primeira videochamada intercontinental protegida por criptografia quântica.",
    "a primeira videochamada intercontinental protegida por chaves quânticas.")
acrescentar_trecho(4, 0, "QUESS was able to test the principle of locality over 1,200 km")

# 0005: o "ato de desespero" foi recorrer a Boltzmann
substituir(5, "gancho", "num \"ato de desespero\".", "com o que ele mesmo chamou de \"ato de desespero\".")
substituir(5, "explicacao",
    "Planck seguiu em frente. Em 14 de dezembro de 1900, para explicar a radiação emitida por corpos quentes, "
    "apresentou uma suposição estranha: a energia eletromagnética só poderia ser emitida em pacotes, múltiplos "
    "de uma unidade elementar. Ele mesmo desconfiava da ideia e, mais tarde, chamou o recurso de \"um ato de "
    "desespero\".",
    "Planck seguiu em frente. Em 1900, tentando explicar a radiação emitida por corpos quentes, recorreu aos "
    "métodos estatísticos de Boltzmann, dos quais desconfiava profundamente, e mais tarde chamou essa guinada de "
    "\"um ato de desespero\". Em 14 de dezembro de 1900, apresentou a suposição que saiu dali: a energia "
    "eletromagnética só poderia ser emitida em pacotes, múltiplos de uma unidade elementar.")
acrescentar_trecho(5, 0, "Planck was deeply suspicious of the philosophical and physical implications of such an interpretation of Boltzmann's approach")

# 0006: o mecanismo do par radical e o experimento das cabanas
trocar(6, nota_surpresa=4)
substituir(6, "explicacao",
    "Experimentos indicam que essas aves usam uma proteína do olho, o criptocromo, que depende de um mecanismo "
    "quântico chamado de par radical para perceber o campo magnético. Esse efeito é extremamente sensível a "
    "campos fracos e, ao contrário de uma bússola de ferro comum, é facilmente perturbado por interferência de "
    "radiofrequência.",
    "A principal explicação hoje é o criptocromo, uma proteína da retina: ao absorver luz azul, ela forma um "
    "\"par radical\", duas moléculas com elétrons desemparelhados cujos estados oscilam de um jeito que até o "
    "campo fraquíssimo da Terra consegue influenciar. Uma bússola de ferro não liga para ondas de rádio, mas "
    "essa bússola química, sim: num experimento com piscos-de-peito-ruivo em cabanas de madeira, as aves só se "
    "orientaram bem quando as cabanas foram blindadas, com a blindagem aterrada, contra o ruído elétrico dos "
    "aparelhos do campus.")
acrescentar_trecho(6, 0, "The mechanism requires two molecules, each with unpaired electrons, at a suitable distance from each other. [...] "
    "That oscillation is extremely sensitive to magnetic fields. [...] "
    "exposure to blue light excites an electron in a chromophore, which causes the formation of a radical-pair [...] "
    "Suspecting extremely weak radio-frequency interference from other electrical equipment on the campus, he tried shielding the huts with aluminium sheeting, which blocks electrical noise but not magnetic fields. "
    "When he earthed the sheeting, the robins oriented correctly; when the earthing was removed, the robins oriented at random.")

# 0008: o ano de 1995 no trecho
CANDIDATOS[7]["fontes"][1]["trecho"] = CANDIDATOS[7]["fontes"][1]["trecho"].replace(
    "Eric Cornell and Carl Wieman at the University", "On 5 June 1995, the first gaseous condensate was produced by Eric Cornell and Carl Wieman at the University")
