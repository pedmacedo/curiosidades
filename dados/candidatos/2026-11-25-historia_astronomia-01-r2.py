"""Rodada 2 de História da astronomia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-historia_astronomia-01.py"))
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


# 0001: sem "exatamente"; a contestação de 2020 da datação e a resposta
substituir(1, "explicacao", "Eles abrangem 82°, exatamente o ângulo entre", "Eles abrangem 82°, o ângulo entre")
substituir(1, "explicacao", "lido como as Plêiades. ",
    "lido como as Plêiades. A data vem dos objetos enterrados com ele e de análises do próprio disco e do local. "
    "Em 2020, dois arqueólogos propuseram uma data bem mais recente, da Idade do Ferro, mas outra equipe rebateu "
    "a proposta no mesmo ano, e as análises seguem confirmando a Idade do Bronze. ")
acrescentar_trecho(1, 0,
    "A paper published in 2020 by Rupert Gebhard and Rudiger Krause questioned the Early Bronze Age dating of the Nebra disc and proposed a later Iron Age date instead. "
    "A response paper was published in the same year by Ernst Pernicka and colleagues, rejecting the arguments of Gebhard and Krause. "
    "Scientific analyses of the disc, the items found with the disc, and the find spot have all confirmed the Early Bronze Age dating.")

# 0002: aprovado
trocar(2, nota_surpresa=4)

# 0003: Cannon manteve também N, P e Q
substituir(3, "explicacao", "descartou quase todas as letras e ficou com O, B, A, F, G, K e M, nessa ordem.",
    "descartou a maioria das letras e pôs as que restaram na ordem O, B, A, F, G, K, M e N, além de P e Q para casos especiais.")
substituir_trecho(3, 1, "dropped all letters except O, B, A, F, G, K, M, and N used in that order",
    "dropped all letters except O, B, A, F, G, K, M, and N used in that order, as well as P for planetary nebulae and Q for some peculiar spectra.")

# 0004: aprovado
trocar(4, nota_surpresa=4)

# 0005: o motivo atribuído a Kepler, nos termos da fonte
substituir(5, "explicacao", "interessado no laboratório e nos dados do mestre",
    "que ganharia acesso ao laboratório e aos produtos químicos do mestre")

# 0006: aprovado
trocar(6, nota_surpresa=4)

# 0007: sem declaração de morte, novo casamento ou saque (versão duvidosa)
trocar(7, gancho="Um astrônomo francês passou 11 anos fora para ver dois trânsitos de Vênus e perdeu os dois, um por causa "
    "da guerra e outro por céu nublado. Na volta, sua vaga na Academia já era de outro.")
substituir_trecho(7, 0, "His wife had remarried, and all his relatives had \"enthusiastically plundered his estate\". ", "[...] ")

# 0008: mais de 20 avistamentos, com Flamsteed e Mayer; homenagem, não retribuição
substituir(8, "gancho", "dezenas de vezes antes", "mais de 20 vezes antes")
substituir(8, "explicacao", "James Bradley o viu três vezes, e o francês Pierre Le Monnier, pelo menos doze, entre 1750 e 1769",
    "John Flamsteed o observou pelo menos seis vezes em 1690 e o catalogou como a estrela 34 Tauri; James Bradley o "
    "viu três vezes, Tobias Mayer uma, e o francês Pierre Le Monnier pelo menos doze, entre 1750 e 1769")
substituir(8, "explicacao", "Herschel retribuiu com o nome Georgium Sidus", "Herschel homenageou o novo patrono com o nome Georgium Sidus")
substituir_trecho(8, 0, "James Bradley observed it three times, in 1748, 1750, and 1753. [...] ",
    "The earliest definite sighting was in 1690, when John Flamsteed observed it at least six times, cataloguing it as 34 Tauri. "
    "James Bradley observed it three times, in 1748, 1750, and 1753. Tobias Mayer observed it once in 1756. ")

# 0009: aprovado
trocar(9, nota_surpresa=4)

# 0010: raio de ~40 m; catálogo de cerca de mil estrelas, o melhor entre Ptolomeu e Tycho
substituir(10, "gancho", "um sextante com raio de uns 36 metros", "um sextante com raio de cerca de 40 metros")
substituir(10, "explicacao", "tinha raio de cerca de 36 metros",
    "tinha raio de cerca de 40 metros, o maior instrumento astronômico do mundo na época")
substituir(10, "explicacao", "catálogo de 994 estrelas tido como o maior entre os de Ptolomeu e de Tycho Brahe",
    "catálogo de cerca de mil estrelas, considerado o melhor feito no intervalo entre Ptolomeu e Tycho Brahe")
substituir_trecho(10, 0, "Lacking telescopes to work with, he increased his accuracy by increasing the length of his sextant; "
    "the so-called Fakhri sextant had a radius of about 36 meters (118 feet) [...] ",
    "Lacking telescopes to work with, he increased his accuracy by increasing the length of his sextant [...] ")
acrescentar_trecho(10, 1,
    "The radius of the sextant was 40.04 meters, which made it the largest astronomical instrument in the world at the time. [...] "
    "listed around 1,000 stars")

# 0011: aprovado, nota 3
trocar(11, nota_surpresa=3)

# 0012: a queda linear é o modelo das tabuinhas; nota 5
substituir(12, "explicacao", "Nos 60 dias depois de reaparecer como estrela da manhã, a velocidade diária de Júpiter cai de forma linear.",
    "Nas tabuinhas, nos 60 dias depois de Júpiter reaparecer como estrela da manhã, a velocidade diária do planeta cai de forma linear.")
trocar(12, nota_surpresa=5)

# 0013: aprovado
trocar(13, nota_surpresa=4)

# 0014: só cabeça e pescoço da ema guarani são manchas escuras
trocar(14, gancho="No Brasil e na Austrália, indígenas veem no céu uma grande ave cuja cabeça não é estrela, mas uma mancha "
    "escura da Via Láctea junto ao Cruzeiro do Sul: a ema dos guaranis e o emu dos aborígenes.")
substituir(14, "explicacao", "A da Ema, Guyra Nhandu em guarani, usa o contrário: as faixas escuras da Via Láctea, que são nuvens de poeira.",
    "A da Ema, Guyra Nhandu em guarani, mistura as duas coisas: a cabeça e o pescoço são manchas escuras da Via "
    "Láctea, nuvens de poeira, e o corpo e a cauda são estrelas do Escorpião, do Lobo, do Triângulo Austral e do Altar.")
substituir(14, "explicacao", "também é feito de nebulosas escuras contra o fundo da Via Láctea",
    "é feito inteiramente de nebulosas escuras contra o fundo da Via Láctea")
substituir_trecho(14, 0, "também é formado por uma mancha escura da Via Láctea. [...] ",
    "também é formado por uma mancha escura da Via Láctea. "
    "A cauda da Ema é formada por Antares, Al niyatn e outras estrelas da constelação do Escorpião. [...] "
    "A parte de baixo do corpo da Ema começa a ser formado pela estrela Beta da constelação do Triângulo Austral (Triangulum Australe) "
    "e por estrelas da constelação da Altar (Ara), sendo que a parte de cima de seu corpo é formado principalmente por estrelas "
    "pertencentes às constelações de Escorpião e do Lobo [...] ")

# 0015: aprovado
trocar(15, nota_surpresa=4)

# 0016: referente do gancho
substituir(16, "gancho", "Uma delas, Nicole-Reine Lepaute, foi apagada do livro.", "A mulher do trio, Nicole-Reine Lepaute, sumiu do livro.")
