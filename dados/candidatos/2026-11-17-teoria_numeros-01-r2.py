"""Rodada 2 de Números: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-17-teoria_numeros-01.py"))
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


# 0001: gancho autoexplicativo; Putney é bairro de Londres
trocar(1, nota_surpresa=3,
       gancho="Hardy achou sem graça o número do seu táxi, 1729. Ramanujan, doente, respondeu que era o menor número que é soma de dois cubos de dois jeitos diferentes.")
substituir(1, "explicacao", "que estava doente em Putney, perto de Londres", "que estava doente em Putney, um bairro de Londres")
substituir(1, "explicacao", "Mas foi a resposta instantânea, dada da cama, que fez de 1729 o número mais famoso da matemática recreativa.",
    "Mas foi a resposta de Ramanujan, dada da cama, que fez de 1729 o mais famoso dos números de táxi.")

# 0002: a caçada custou US$ 2 milhões; PCs só nos 16 recordes da GIMPS
trocar(2, nota_surpresa=3)
substituir(2, "gancho", "que gastou cerca de US$ 2 milhões em placas de vídeo.",
    "que gastou cerca de US$ 2 milhões numa caçada com milhares de placas de vídeo.")
substituir(2, "explicacao", "os anteriores tinham sido encontrados em computadores pessoais",
    "os 16 recordes anteriores achados pela GIMPS tinham saído de computadores pessoais comuns")
acrescentar_trecho(2, 0, "GIMPS volunteers found the 16 latest records, all of them Mersenne primes.")

# 0005: fraude e Benford, sem exagero
substituir(5, "explicacao",
    "Como dados inventados costumam fugir desse padrão, a lei de Benford é usada em auditoria forense e na "
    "detecção de fraudes, inclusive em dados eleitorais, embora esse uso eleitoral seja polêmico.",
    "Números inventados por pessoas tendem a se desviar do padrão, sobretudo nos algarismos depois do "
    "primeiro. Por isso a lei de Benford é usada como teste para detectar fraudes, de dados científicos a "
    "resultados eleitorais, mas não é infalível, e o uso em eleições é polêmico.")
acrescentar_trecho(5, 0, "The first digits of the fabricated coefficients showed approximate Benford behavior, but the higher digits did not. [...] "
    "Such analysis is considered a simple, though not foolproof, method of identifying irregularities in election results.")

# 0006: sem "centenas de páginas"
substituir(6, "gancho", "A prova de verdade levou 358 anos e centenas de páginas.",
    "A prova de verdade levou 358 anos e quase naufragou por causa de uma falha.")

# 0007: sem o aposto sobre Erdős
substituir(7, "explicacao", "O húngaro Paul Erdős, um dos matemáticos mais produtivos da história, resumiu:",
    "O matemático Paul Erdős resumiu:")
substituir(7, "explicacao", "a maioria dos matemáticos acredita", "a maioria dos matemáticos que estudaram o problema acredita")

# 0008: dígitos, não casas decimais; precisão de um átomo
trocar(8, gancho="Com só 39 dígitos de pi, dá para calcular a circunferência do universo observável com precisão de um átomo. Mesmo assim, já se calcularam centenas de trilhões.")

# 0011 (sugestão): abertura menos literal
substituir(11, "explicacao",
    "A conjectura de Goldbach é um dos problemas sem solução mais antigos e conhecidos da matemática.",
    "Poucos problemas em aberto da matemática são tão antigos e tão famosos quanto a conjectura de Goldbach.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(2, "explicacao", "os 16 recordes anteriores achados pela GIMPS tinham saído de computadores pessoais comuns",
    "os recordes anteriores achados pela GIMPS tinham saído de computadores pessoais comuns")
substituir(5, "explicacao", "Números inventados por pessoas tendem a se desviar do padrão, sobretudo nos algarismos depois do primeiro.",
    "Num experimento, números inventados por voluntários seguiram o padrão no primeiro algarismo, mas não nos seguintes.")
substituir(7, "explicacao", "O alemão Lothar Collatz propôs a ideia em 1937.", "O matemático Lothar Collatz propôs a ideia em 1937.")
