"""Rodada 2 de Códigos e criptografia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-23-criptografia-01.py"))
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


# 0005: 330 e 309 = "máscara" e ponto final; sem o "até 1811"
substituir(5, "explicacao",
    "deduziu que dois números desconhecidos significavam \"máscara\": seria o Homem da Máscara de Ferro.",
    "deduziu que os números desconhecidos 330 e 309 queriam dizer \"máscara\" e ponto final: o general seria o "
    "Homem da Máscara de Ferro.")
substituir(5, "explicacao", "Versões modificadas serviram ao exército francês até 1811. ", "")
substituir(5, "explicacao", "Depois, muitos documentos dos arquivos franceses ficaram ilegíveis",
    "Quando a cifra caiu em desuso, muitos documentos dos arquivos franceses ficaram ilegíveis")
substituir_trecho(5, 0, "Modified forms were in use by the French Peninsular army until the summer of 1811. ", "")

# 0009: "primeiro" e "sem anotar nada na hora"
substituir(9, "gancho",
    "foi concebida antes, em segredo, na inteligência britânica. Clifford Cocks chegou ao futuro RSA em 1973 e nem anotou a ideia.",
    "foi concebida primeiro em segredo, na inteligência britânica. Clifford Cocks chegou ao futuro RSA em 1973 sem anotar nada na hora.")

# 0010: "mais de 600 voluntários"
substituir(10, "gancho", "com uma mensagem cifrada.", "com uma cifra.")
substituir(10, "gancho", "Entre 1993 e 1994, 600 voluntários resolveram.",
    "Entre 1993 e 1994, mais de 600 voluntários a quebraram.")

# 0014: é o próprio manuscrito; "ou ao menos o conde Veltheim"
substituir(14, "explicacao",
    "Um documento ligado ao manuscrito sugere que os Oculistas eram maçons preservando ritos proibidos pelo papa Clemente XII.",
    "O próprio manuscrito sugere que os Oculistas, ou ao menos o conde Veltheim, que os liderava, eram maçons "
    "preservando ritos proibidos pouco antes pelo papa Clemente XII.")
acrescentar_trecho(14, 0, "The Oculists were a group of ophthalmologists led by Count Friedrich August von Veltheim")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
# 0009: na fonte, é o próprio receptor que soma e depois subtrai o ruído.
substituir(9, "explicacao", "que protegia conversas por voz somando um ruído aleatório que o receptor depois subtraía.", "que protegia conversas por voz fazendo o próprio receptor somar um ruído aleatório à linha e depois subtraí-lo.")
