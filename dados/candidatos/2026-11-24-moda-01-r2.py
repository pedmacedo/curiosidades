"""Rodada 2 de Roupas e moda: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-moda-01.py"))
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


# 0001: não generalizar ("todo verde vinha do arsênico")
substituir(1, "gancho", "O verde da moda no século XIX vinha do arsênico.",
    "O verde vivo da moda no século XIX costumava vir do arsênico.")

# 0003: frase truncada; o abandono de 1740 é do salto alto de moda, segundo Semmelhack
substituir(3, "explicacao",
    "ganhava 10 cm com saltos de sola e salto sempre vermelhos e, nos anos 1670,",
    "ganhava 10 cm com saltos, sempre com sola e salto vermelhos, e, nos anos 1670,")
substituir(3, "explicacao",
    "e por volta de 1740 os homens o tinham abandonado.",
    "e, segundo Semmelhack, por volta de 1740 os homens tinham deixado o salto alto de lado; ficaram só saltos "
    "baixos e robustos, como os das botas de montaria.")
trocar(3, nota_surpresa=3)
acrescentar_trecho(3, 1,
    "By this time, heels for men were chunky squares attached to riding boots or tall formal dress boots [...] "
    "Over the course of the Enlightenment, men's heels began to concentrate on either practical riding boots or tall leather boots worn for status.")

# 0005: gancho com a graça da bolsa no braço
trocar(5, gancho="Por séculos, o bolso das mulheres era uma bolsinha à parte, amarrada na cintura sob a saia. Com os "
    "vestidos retos e finos do fim do século XVIII, ele ficou inútil, e elas passaram a levar a bolsa no braço.")

# 0006 (aprovado, retoque opcional): William Wilde, médico e pai de Oscar Wilde
substituir(6, "explicacao",
    "Emily e Mary, filhas ilegítimas de William Wilde, morreram queimadas",
    "Emily e Mary, filhas ilegítimas do médico William Wilde, pai de Oscar Wilde, morreram queimadas")
CANDIDATOS[5]["fontes"].append(wiki("William_Wilde",
    "was an Irish oto-ophthalmologic surgeon and the author of significant works on medicine, archaeology and folklore, particularly concerning his native Ireland. "
    "He was the father of Oscar Wilde. [...] "
    "Emily and Mary both died in 1871 following a Halloween party at which their dresses accidentally caught fire.",
    nome="William Wilde"))

# 0007 (aprovado, retoque opcional): deixar claro de que denim se fala
substituir(7, "explicacao",
    "Outra diz que o denim vinha de Nîmes, na França; era americano.",
    "Outra diz que o denim usado nas primeiras calças vinha de Nîmes, na França; era de um fabricante americano.")

# 0008: "chegar às roupas" é contestado
substituir(8, "gancho", "O zíper demorou décadas para chegar às roupas.",
    "O zíper demorou décadas para se firmar nas roupas.")
substituir(8, "explicacao", "Só em 1925 ele chegou às roupas, em jaquetas de couro.",
    "Em 1925, a marca Schott NYC passou a usá-lo em jaquetas de couro.")

# 0012: as aranhas tecendo teias são do desenho bordado
substituir(12, "explicacao",
    "Depois de tecida, a capa ganhou 6 mil horas de bordado, com dezenas de aranhas tecendo teias.",
    "Depois de tecida, a capa ganhou 6 mil horas de bordado, num desenho com dezenas de aranhas tecendo teias entre flores.")
substituir_trecho(12, 2, "includes scores of spiders weaving webs and floral motifs",
    "includes scores of spiders weaving webs and floral motifs to illustrate the spiders' natural habitat")
