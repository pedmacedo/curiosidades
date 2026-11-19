"""Rodada 2 de Clima do passado e do futuro: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-mudancas_climaticas-01.py"))
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


# 0005: quase todas as folhas escaparam
substituir(5, "explicacao", "que destruiu a gráfica; as folhas impressas escaparam.",
    "que destruiu a gráfica; quase todas as folhas já impressas escaparam no depósito.")
acrescentar_trecho(5, 0, "almost all of the printed sheet paper remained undamaged in the printing warehouse")

# 0006: sem os "3 anos ou menos"; o Atlântico Norte
substituir(6, "gancho", "Na Groenlândia, a temperatura caiu até 10 °C, e a queda pode ter levado 3 anos ou menos.",
    "Em poucas décadas, a Groenlândia ficou até 10 °C mais fria.")
substituir(6, "explicacao", "O resfriamento atingiu o hemisfério Norte em poucas décadas", "O resfriamento atingiu o Atlântico Norte em poucas décadas")

# 0008: florações; sem o par de ppm sem fonte primária; "alguns milhões de anos antes"
substituir(8, "gancho", "pode ter coberto o oceano Ártico por 800 mil anos", "pode ter florescido no oceano Ártico por 800 mil anos")
substituir(8, "explicacao",
    "O episódio coincide com uma queda do CO2, de 3.500 ppm no começo do Eoceno para 650 ppm, e a hipótese é que a samambaia possa ter respondido por boa parte dessa queda,",
    "O episódio coincide com uma queda forte do CO2 do ar, e a hipótese é que a samambaia tenha contribuído para ela, ao lado de outros fatores,")
substituir(8, "explicacao", "Pouco antes, a Terra tinha passado", "Alguns milhões de anos antes, a Terra tinha passado")

# 0009: a base era pública; secreto era o Projeto Iceworm
substituir(9, "gancho", "uma base militar secreta dos EUA sob o gelo da Groenlândia", "uma base militar dos EUA escavada no gelo da Groenlândia")

# 0015: os números de 2.000 anos são de baixa confiança
substituir(15, "gancho", "Segundo o IPCC, mesmo que", "Pelas estimativas do IPCC, mesmo que")
substituir(15, "explicacao", "ficará elevado por milhares de anos, com alta confiança.",
    "ficará elevado por milhares de anos, com alta confiança. Já os números exatos para os próximos 2.000 anos são "
    "classificados pelo próprio relatório como de baixa confiança, pela incerteza sobre o comportamento das camadas de gelo.")
acrescentar_trecho(15, 0, "and it will continue to rise over subsequent millennia ( low confidence)")
