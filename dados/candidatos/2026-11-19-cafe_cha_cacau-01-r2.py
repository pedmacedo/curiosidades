"""Rodada 2 de Café, chá e cacau: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-cafe_cha_cacau-01.py"))
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


# 0001: sem a precisão falsa do teor alcoólico
substituir(1, "explicacao", "usada numa bebida fermentada com 5,34% de álcool.", "usada numa bebida fermentada levemente alcoólica.")

# 0006: a data do cruzamento varia entre estudos
substituir(6, "explicacao",
    "Esse cruzamento aconteceu na natureza, numa data estimada entre 1,08 milhão e 543 mil anos atrás, ligada a mudanças ambientais no leste da África",
    "Esse cruzamento aconteceu na natureza há algumas centenas de milhares de anos (as estimativas variam entre estudos), possivelmente ligado a mudanças ambientais no leste da África")

# 0008: o fungo veio da África; "deve sua ascensão"; Berkeley e Broome
substituir(8, "gancho", "O chá do Ceilão existe por causa de um fungo.", "O chá do Ceilão deve sua ascensão a um fungo.")
substituir(8, "gancho", "os produtores trocaram o café pelo chá", "muitos produtores trocaram o café pelo chá")
substituir(8, "explicacao", "descrita em 1869 por dois micologistas ingleses",
    "descrita em 1869 pelo micologista inglês Michael Berkeley e seu colaborador Christopher Broome")
substituir(8, "explicacao", "A ferrugem afetou o café da Ásia por mais de vinte anos e depois se espalhou pela África.",
    "Originário do leste da África, o fungo afetou o café da Ásia por mais de vinte anos e, nos anos 1920, já estava espalhado por boa parte da África e da Ásia.")

# 0009: a maioria no noroeste da Índia; temporadas na China; debate
trocar(9, confianca="consenso_parcial")
substituir(9, "gancho", "Quase todas morreram", "A maioria das que foram plantadas no noroeste da Índia morreu")
substituir(9, "explicacao", "Robert Fortune trabalhou na China entre 1843 e 1861", "Robert Fortune passou vários anos na China, em temporadas entre 1843 e 1861")

# 0010: o pastor sem nome no primeiro relato
substituir(10, "gancho", "E o nome Kaldi parece ter sido inventado só no século XX.", "E, nesse primeiro relato, o pastor nem tinha nome.")
substituir(10, "explicacao", "O nome Kaldi parece ter sido criado no século XX e foi difundido pelo americano William H. Ukers, autor de um livro de 1922 sobre o café.",
    "O nome Kaldi parece ser um acréscimo bem posterior, popularizado no século XX pelo americano William H. Ukers, autor de um livro de 1922 sobre o café.")

# 0011: a abolição britânica
substituir(11, "explicacao", "até a abolição do tráfico, em 1807", "até o Reino Unido abolir o tráfico, em 1807")

# 0012: os médicos morreram antes do bebedor de café; sem mito_desmentido
trocar(12, gancho="Conta-se que Gustavo III, da Suécia, quis provar que o café fazia mal com gêmeos condenados: um tomaria café todo "
    "dia, o outro chá. O rei e os médicos morreram antes do bebedor de café. A Suécia proibiu o café 5 vezes.",
    tipos_espanto=["historia_humana"])
substituir(12, "explicacao", "é questionada pelos historiadores", "é posta em dúvida")

# 0013: "a maior parte da cafeína"; a água do mar como relato
trocar(13, confianca="consenso_parcial",
    gancho="Conta-se que o primeiro descafeinado comercial nasceu de uma carga de café molhada por acidente com água do mar, "
    "que perdeu a maior parte da cafeína. A patente de 1906 usava benzeno, hoje sabidamente cancerígeno.")
substituir(13, "explicacao", "depois de Roselius notar", "depois de, segundo o relato tradicional, Roselius notar")

# 0014: "às vezes mais de"
substituir(14, "explicacao", "Carregadores levavam nas costas de 60 a 90 kg de chá", "Carregadores às vezes levavam nas costas mais de 60 a 90 kg de chá")

# gancho do 0009 encurtado para caber em 220 caracteres
trocar(9, gancho="Em 1848, um botânico escocês, às vezes disfarçado de chinês, levou mudas de chá da China para a Índia. A maioria "
    "das plantadas no noroeste morreu, e o chá forte que os ingleses queriam veio de uma planta local, de Assam.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(9, "explicacao", "Não foi o primeiro a tentar, mas foi a introdução de chá mais famosa.", "Não foi o primeiro a tentar, mas essa virou a façanha mais conhecida dele.")
