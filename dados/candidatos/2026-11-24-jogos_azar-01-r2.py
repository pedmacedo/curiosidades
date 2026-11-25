"""Rodada 2 de Cartas, dados e azar: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-jogos_azar-01.py"))
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


# 0002: dois lados largos e dois estreitos; números como estimativas
trocar(2, nota_surpresa=3)
trocar(2, gancho="Os dados devem descender dos astrágalos, ossinhos do tornozelo de animais, que param em só "
                 "quatro lados: cada um dos dois lados largos sai em cerca de 38% das vezes; cada um dos dois "
                 "estreitos, uns 12%.")
substituir(2, "explicacao", "só consegue parar sobre quatro lados, o que o torna",
    "só consegue parar sobre quatro lados, dois largos e dois estreitos, e os largos caem para cima bem mais "
    "vezes (cerca de 38% cada, contra uns 12% de cada estreito, segundo estimativas). Isso o torna")

# 0003: foram os dados (3 e 4 opostos), não a mudança; a proposta de base 12 é de 2006
substituir(3, "gancho", "Essa mudança foi usada para propor", "Esses dados foram usados para propor")
substituir(3, "explicacao",
    "A questão não está fechada: outra proposta, que supõe uma contagem de base 12, devolve a huθ o valor 4.",
    "A questão não está fechada: uma proposta de 2006, que supõe uma contagem de base 12, dá a huθ o valor 4.")

# 0004: "pesquisadores"; o 6 na face maior também pela ordem de marcação
substituir(4, "gancho", "Para dois arqueólogos", "Para dois pesquisadores")
substituir(4, "explicacao", "tendiam a pôr o 6 na face maior, por falta de espaço, não para favorecer jogadas",
    "tendiam a pôr o 6 na face maior, por falta de espaço ou pela ordem em que marcavam os pontos, não para "
    "favorecer jogadas")

# 0005: etimologia provável; cronologia da Ásia ao Egito; o nosso baralho é francês com nomes portugueses
substituir(5, "gancho", "Até \"naipe\" vem do árabe.", "Até \"naipe\" deve vir do árabe.")
substituir(5, "explicacao", "Espalharam-se pela Ásia e, a partir do século XI, chegaram ao Egito.",
    "Por volta do século XI já se espalhavam pela Ásia e, depois, chegaram ao Egito.")
substituir(5, "explicacao",
    "O título nā'ib passou ao francês, ao italiano e ao espanhol, e o português naipe veio do catalão naip.",
    "O português naipe veio do catalão naip, que provavelmente vem do título nā'ib, embora a origem exata "
    "ainda seja discutida.")
substituir(5, "explicacao",
    "São esses os naipes dos baralhos tradicionais italiano, espanhol e português, de onde vêm os nossos paus, "
    "ouros, espadas e copas.",
    "São esses os naipes dos baralhos tradicionais italiano, espanhol e português. O baralho que usamos hoje "
    "tem os desenhos franceses (o ♣ é um trevo), mas manteve os nomes do antigo baralho português: paus, ouros, "
    "espadas e copas.")

# 0008: etimologia incerta; Hart "is credited"
substituir(8, "gancho", "E o nome Joker provavelmente vem de Jucker", "E o nome Joker talvez venha de Jucker")
substituir(8, "explicacao", "O fabricante Samuel Hart imprimiu em 1863 a primeira carta ilustrada desse tipo",
    "Atribui-se ao fabricante Samuel Hart a primeira carta ilustrada desse tipo, de 1863")

# 0009: o uso divinatório se difundiu (não começou) no fim do século XVIII; o tarô egípcio de Etteilla é posterior
trocar(9, gancho="O tarô nasceu na Itália do século XV como jogo de cartas, e ainda é jogado em boa parte da Europa. "
                 "O uso para ler a sorte só se difundiu no fim do século XVIII, com a tese, sem provas, de que ele "
                 "vinha do Egito antigo.")
substituir(9, "explicacao",
    "Pouco depois, o cartomante Etteilla criou, em 1783, um método de adivinhação com o tarô, e também o primeiro "
    "tarô \"egípcio\" feito só para esse fim.",
    "Pouco depois, em 1783, o cartomante Etteilla criou um método de adivinhação com o tarô e, alguns anos mais "
    "tarde, o primeiro tarô \"egípcio\" feito só para esse fim.")

# 0010: Francisco I é anterior ao lotto de números
substituir(10, "explicacao",
    "A ideia viajou: o rei Francisco I conheceu as loterias nas campanhas militares na Itália",
    "Antes disso, as loterias italianas em geral já tinham inspirado outros reinos: o rei Francisco I as "
    "conheceu nas campanhas militares na Itália")

# 0011: sem o "nem particularmente famoso"
substituir(11, "explicacao",
    "O dinheiro, bem investido, deixou o escritor rico e independente, aos 30 e poucos anos, quando ainda não era "
    "nem rico nem particularmente famoso.",
    "O dinheiro, bem investido, deixou o escritor, então com 30 e poucos anos e ainda sem fortuna, rico e "
    "independente.")

# 0012: Frederico "bore no fruit"; Casanova se juntou a um projeto que já existia
substituir(12, "gancho", "Frederico, o Grande, não se interessou", "nada conseguiu com Frederico, o Grande")
substituir(12, "explicacao", "A ideia foi uma loteria para financiar a Escola Militar.",
    "O caminho foi um projeto de loteria, nascido de iniciativas para financiar a Escola Militar.")

# 0015: proibição sem atribuí-la a Carolina
trocar(15, nota_surpresa=3)
substituir(15, "explicacao",
    "Por iniciativa da própria Carolina, e por razões morais, os cidadãos de Mônaco não podem entrar nas salas de jogo.",
    "E, até hoje, os cidadãos de Mônaco não podem entrar nas salas de jogo do cassino.")

# 0016: sem a comparação contestada de 2015 no gancho
substituir(16, "gancho",
    "que se \"vendem\" num guichê separado. Em 2015, faturou mais que Macau, Las Vegas e Singapura juntas.",
    "que se \"vendem\" num guichê separado, muitas vezes do próprio dono do salão.")
