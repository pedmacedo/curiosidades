"""Rodada 2 de Química do cotidiano: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-quimica_cotidiano-01.py"))
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


# 0002: "largely replaced" = substituído em grande parte
substituir(2, "explicacao",
    "nos anos 1950 os detergentes já tinham substituído o sabão na lavagem de roupa nos países desenvolvidos.",
    "nos anos 1950 os detergentes já tinham substituído, em grande parte, o sabão na lavagem de roupa nos países desenvolvidos.")

# 0004: a fonte diz "possible mechanism"
substituir(4, "gancho",
    "É um mecanismo provável do cheiro de terra molhada",
    "É um mecanismo possível do cheiro de terra molhada")

# 0006: sem o "só" absoluto
trocar(6, gancho="Num letreiro \"de neon\", o gás neon puro dá um brilho vermelho-alaranjado. A maioria das outras cores vem de "
                 "outros gases, como argônio com mercúrio, cuja luz ultravioleta faz brilhar um revestimento por dentro do tubo.")
substituir(6, "explicacao",
    "Mesmo assim, o nome \"neon\" ficou para todas.",
    "Mesmo assim, o nome \"neon\" ficou para todos os letreiros, qualquer que seja o gás.")

# 0008: sem a data do relatório de Barrow; o bicarbonato é uma opção
substituir(8, "explicacao",
    "Nos anos 1930, o químico e bibliotecário William Barrow publicou um relatório",
    "O químico e bibliotecário americano William Barrow publicou um relatório")
substituir(8, "explicacao",
    "A resposta foi o papel sem ácido, tratado com bicarbonato de cálcio ou de magnésio, que deixa",
    "A resposta foi o papel sem ácido, que pode ser tratado com bicarbonato de cálcio ou de magnésio, que deixa")

# 0009: alergia e jantar como história da família
trocar(9, confianca="consenso_parcial",
    gancho="Em 1843, o farmacêutico inglês Alfred Bird criou um fermento químico em pó para a esposa, que, segundo a "
           "história da família, não tolerava ovo nem levedura. Antes, fizera para ela um creme sem ovo, que virou marca.")
substituir(9, "explicacao",
    "Em casa, os convidados recebiam o creme de verdade, até que",
    "Segundo a história contada na família, os convidados recebiam o creme de verdade, até que")

# 0013: a molécula se forma sobre a pele, por íons de ferro
substituir(13, "gancho",
    "uma molécula criada na hora pela pele: o ferro reage com gorduras oxidadas dela.",
    "uma molécula criada na hora sobre a própria pele: íons de ferro reagem com gorduras oxidadas dela.")
