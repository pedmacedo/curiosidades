"""Rodada 2 de Brinquedos e brincadeiras: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-brinquedos-01.py"))
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)

LOTE, AREA, TEMA = _base.LOTE, _base.AREA, _base.TEMA
wiki = _base.wiki
web = _base.web
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


# 0001: o episódio da mola é relato da família; "naval", não "da Marinha"; "mola maluca"
trocar(1, nota_surpresa=4,
    gancho="O Slinky, a mola maluca, nasceu em 1943 quando, segundo a família, um engenheiro naval viu uma mola cair da "
           "prateleira e descer \"andando\". Anos depois, o brinquedo serviu de antena de rádio a soldados no Vietnã.")
substituir(1, "explicacao", "Richard T. James, engenheiro mecânico da Marinha dos EUA, viu uma mola cair de uma prateleira",
    "Segundo o relato da família, Richard T. James, engenheiro mecânico naval, viu uma mola cair de uma prateleira")

# 0002: "mola maluca (Slinky)" no gancho, com a concordância ajustada
trocar(2, nota_surpresa=4)
substituir(2, "gancho", "Solte um Slinky pendurado e", "Solte uma mola maluca (Slinky) pendurada e")

# 0003: a demanda caiu (não sumiu); nota 3
trocar(3, nota_surpresa=3)
substituir(3, "gancho", "Quando esse mercado sumiu, uma professora teve a ideia de usá-la com crianças.",
    "Quando a demanda caiu, uma professora a levou para a sala de aula e ela virou brinquedo.")

# 0004: sem atribuir causa à morte de Page
trocar(4, nota_surpresa=4)
substituir(4, "explicacao", "Page, pressionado pelos problemas da empresa e temendo sua quebra, se matou em 1957.",
    "Page morreu por suicídio em 1957.")

# 0005: o "cerca de um mês" é lembrança de Rubik; "de forma independente"
trocar(5, nota_surpresa=4,
    gancho="Ernő Rubik não queria criar um quebra-cabeça: buscava peças que girassem sem o conjunto desmontar. Só viu o "
           "desafio ao embaralhar o cubo pela primeira vez e, segundo ele, levou cerca de um mês para resolvê-lo.")
substituir(5, "explicacao", "fazer muitas peças pequenas se moverem sozinhas",
    "fazer muitas peças pequenas se moverem de forma independente")

# 0006: Flores popularizou o desenho filipino, não o inventou
trocar(6, nota_surpresa=3)
substituir(6, "gancho", "A grande inovação veio de um filipino nos EUA, um laço na corda que deixa o ioiô girar parado.",
    "A grande inovação foi popularizada por um filipino nos EUA: um laço na corda que deixa o ioiô girar parado.")
substituir(6, "explicacao", "Flores usava um fio contínuo",
    "O modelo filipino que Flores popularizou usava um fio contínuo")

# 0007: "não foi lançada para crianças"
trocar(7, nota_surpresa=4)
substituir(7, "gancho", "numa boneca alemã que não era para crianças:", "numa boneca alemã que não foi lançada para crianças:")

# 0008: dizer que brinquedo é; visor (o vidro virou plástico)
trocar(8, nota_surpresa=4,
    gancho="O Etch A Sketch, a tela mágica de dois botões, não pinta linha nenhuma: o visor é coberto por dentro com pó de "
           "alumínio preso por eletricidade estática, e uma ponta raspa esse pó, revelando o escuro lá dentro.")
substituir(8, "explicacao", "o pó de alumínio sai do vidro", "o pó de alumínio sai do visor")
substituir(8, "explicacao", "espalham de novo o pó sobre o vidro", "espalham de novo o pó sobre o visor")
substituir(8, "explicacao", "A tela original era de vidro comum, criticada por quebrar fácil e ser um perigo para as crianças.",
    "A tela original era de vidro comum, criticada por quebrar fácil e ser um perigo para as crianças, e depois foi "
    "trocada por plástico.")
acrescentar_trecho(8, 0, "The Food and Drug Administration responded that the toy had been redesigned, replacing the glass plate with plastic.")

# 0009: o vínculo com a bola vem do próprio Hunt
trocar(9, nota_surpresa=4,
    gancho="O nome Super Bowl, final do futebol americano, veio de um brinquedo, segundo o próprio criador do termo: ele "
           "viu os filhos brincando com uma Super Ball, a bolinha superelástica da moda.")
substituir(9, "explicacao",
    "Lamar Hunt, fundador da American Football League, viu os filhos com uma dessas bolas e, numa carta de 1966",
    "Lamar Hunt, fundador da American Football League, contou que se inspirou nos filhos brincando com uma dessas "
    "bolas; numa carta de 1966")

# 0011: o urso do cartum foi encolhendo; o pedido de permissão é relato da família
trocar(11, nota_surpresa=4)
substituir(11, "explicacao",
    "O cartunista Clifford Berryman desenhou a cena no Washington Post, mas com um filhote dócil no lugar do urso velho.",
    "O cartunista Clifford Berryman desenhou a cena no Washington Post, e, de um desenho para outro, o urso foi ficando "
    "menor e mais fofo, até virar um filhote dócil, bem longe do animal velho e ferido da caçada.")
substituir(11, "explicacao", "e pediram a Roosevelt permissão para usar o nome.",
    "e, segundo a família, pediram a Roosevelt permissão para usar o nome.")
acrescentar_trecho(11, 1, "While the initial cartoon depicted an adult black bear lassoed by a handler and a disgusted Roosevelt, "
    "later issues of that and other Berryman cartoons made the bear smaller and cuter.")

# 0012: campanha "apontada como" a primeira; sem causalidade inventada; nota 3
trocar(12, nota_surpresa=3)
substituir(12, "explicacao", "numa campanha que também foi a primeira dirigida diretamente às crianças;",
    "numa campanha também apontada como a primeira dirigida diretamente às crianças;")
substituir(12, "explicacao",
    "Ajudaram a disparada na venda de televisores e um grande surto de pólio em 1952, que deixou as crianças mais tempo em casa.",
    "O momento era propício: a venda de televisores tinha disparado, e um grande surto de pólio em 1952 deixou as "
    "crianças mais tempo em casa.")

# 0010: aprovado; nota do verificador
trocar(10, nota_surpresa=3)

# 0013, 0014 e 0015: aprovados sem mudança

# 0007: encurtar o gancho para caber em 220 caracteres depois da correção
substituir(7, "gancho", "como presente de brincadeira para adultos", "como piada para adultos")
