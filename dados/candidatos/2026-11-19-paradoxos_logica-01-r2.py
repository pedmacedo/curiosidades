"""Rodada 2 de Lógica e paradoxos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-paradoxos_logica-01.py"))
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


# 0004: a resposta de Einstein, nas palavras dele; sem repetir as caminhadas do 0003
substituir(4, "explicacao", "Em Princeton, Gödel e Einstein ficaram muito amigos e eram conhecidos pelas longas caminhadas juntos de casa até o instituto e de volta. ", "")
substituir(4, "explicacao",
    "Conta-se que ele deu o trabalho a Einstein como presente pelos 70 anos do amigo, e que os universos giratórios fizeram Einstein duvidar da própria teoria.",
    "Conta-se que ele deu o trabalho a Einstein como presente pelos 70 anos do amigo. Einstein respondeu, por escrito, que "
    "valeria a pena avaliar se soluções assim não deveriam ser descartadas por razões físicas.")
acrescentar_trecho(4, 1, "Such cosmological solutions of the gravitation-equations (with not vanishing A-constant) have been found by Mr. Gödel. "
    "It will be interesting to weigh whether these are not to be excluded on physical grounds.")

# 0009: gancho que se explica sozinho; o número vai para a explicação
trocar(9, gancho="Uma regra simples de trocar bases e subtrair 1 gera sequências que crescem de forma absurda e, mesmo assim, "
    "sempre voltam a zero. E a aritmética usual dos números naturais não consegue provar isso.")
substituir(9, "explicacao", "e só então desce, de 1 em 1, até zero.",
    "e só então desce, de 1 em 1, até zero. Ela só chega a zero quando a base atinge 3 × 2 elevado a 402.653.211, menos 1.")
substituir(9, "explicacao", "não pode ser provado na aritmética de Peano;",
    "não pode ser provado na aritmética de Peano (o sistema usual de axiomas dos números naturais);")

# 0012: o sentido religioso é reconstrução de Rendel Harris
substituir(12, "gancho", "E, no original, era uma bronca religiosa sobre o túmulo de Zeus.",
    "E, no poema original, seria uma bronca religiosa sobre o túmulo de Zeus.")

# 0013: "não se sabe de ninguém a quem tenha contado"
substituir(13, "explicacao", "mas ele não falou dela a ninguém até 1970, quando achou que ia morrer",
    "mas não se sabe de ninguém a quem ele tenha contado antes de 1970, quando achou que ia morrer")
