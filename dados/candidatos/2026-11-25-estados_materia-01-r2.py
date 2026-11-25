"""Rodada 2 de Estados da matéria: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-estados_materia-01.py"))
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


# 0001, 0007, 0009, 0010, 0012: aprovados sem mudança
# 0004 e 0015: reprovados (duplicados), ficam como estão

# 0002: tirar a frase do maior campo de estabilidade, que deformava a fonte
substituir(2, "explicacao",
    "Ele é também a fase molecular do gelo com o maior campo de estabilidade, que vai de pressão alta a temperatura baixa. ",
    "")
substituir_trecho(2, 0, "Thus, ice VII has the largest stability field of all of the molecular phases of ice. [...] ", "")

# 0003: o gelo cristalino não é "raríssimo" no espaço; confiança e tipos
trocar(3,
    gancho="Nas nuvens geladas entre as estrelas, a água congela sem formar cristais, num gelo desordenado como vidro. "
           "Por isso, esse gelo amorfo é provavelmente a forma mais comum de água no universo.",
    confianca="consenso_parcial",
    tipos_espanto=["contraintuitivo", "conexao_inesperada"])
substituir(3, "explicacao",
    "Por isso, o gelo do meio interestelar é dominado pela forma amorfa, enquanto o gelo cristalino hexagonal, que "
    "predomina na Terra, é raríssimo lá fora, e os exemplos conhecidos costumam estar ligados a vulcanismo.",
    "Por isso, a água do meio interestelar está sobretudo na forma amorfa, ao contrário da Terra, onde predomina o "
    "gelo cristalino hexagonal.")
substituir_trecho(3, 0,
    "In outer space, hexagonal crystalline ice (the predominant form found on Earth) is extremely rare. "
    "Known examples are typically associated with volcanic action. ",
    "hexagonal crystalline ice (the predominant form found on Earth) [...] ")

# 0005: a data de 2 de agosto de 1911 não se sustenta
substituir(5, "explicacao",
    "já tivesse visto essa transição em 2 de agosto de 1911, sem perceber,",
    "já tivesse visto essa transição em 1911, sem perceber,")

# 0006: anunciados em 2016, publicados em 2017
substituir(6, "gancho", "Em 2017, duas equipes criaram uma versão dele.", "Em 2017, duas equipes relataram uma versão dele.")

# 0008: Kistler fez trabalho pioneiro, não "propôs o reforço do Gorilla Glass"
substituir(8, "gancho", "O inventor também propôs o reforço do Gorilla Glass.", "Ele também abriu caminho para o Gorilla Glass.")
substituir(8, "explicacao",
    "Em 1962, Kistler publicou um método de reforçar vidro trocando íons de sódio por íons maiores de potássio; a "
    "Corning desenvolveu a técnica, hoje usada no Gorilla Glass e similares.",
    "Em 1962, Kistler publicou um trabalho pioneiro sobre reforçar vidro trocando íons de sódio por íons maiores de "
    "potássio; a técnica, desenvolvida depois e comercializada pela Corning, hoje é usada no Gorilla Glass e similares.")

# 0011: quem deu nome aos cristais líquidos; os 80 anos de curiosidade
substituir(11, "explicacao",
    "o interesse logo caiu. Lehmann seguiu estudando e, em 1904, cunhou o nome dos cristais líquidos colestéricos.",
    "o interesse logo caiu. Lehmann seguiu estudando o fenômeno e foi quem deu nome aos cristais líquidos, que "
    "continuaram uma pura curiosidade científica por cerca de 80 anos.")
substituir_trecho(11, 0, "(the name coined by Otto Lehmann in 1904) [...] ", "")
acrescentar_trecho(11, 0, "liquid crystals were not popular among scientists and the material remained a pure scientific curiosity for about 80 years.")
acrescentar_trecho(11, 1, "he accidentally discovered some of the properties of liquid crystals (named later by Otto Lehmann).")

# 0013: as duas etapas do problema nas soldas
substituir(13, "explicacao",
    "que no frio pode se soltar em pó não condutor e causar curtos-circuitos.",
    "que no frio vira pó não condutor e se solta; reaquecido, esse pó volta a ser estanho metálico, que conduz, e o "
    "ciclo pode causar curtos-circuitos.")
substituir_trecho(13, 0,
    "and falls off the leads. [...] This cycle can cause",
    "and falls off the leads. After reheating, it changes back to β-modification white tin, which is electrically conductive. This cycle can cause")

# 0014: motivos dos sacos plásticos, mecanismo da expansão, "microscópicas", tipo único
trocar(14, tipos_espanto=["contraintuitivo"])
substituir(14, "gancho", "gotículas dele", "gotículas microscópicas dele")
substituir(14, "explicacao",
    "aumenta 3,10% de volume ao solidificar, como a água, por isso é vendido em sacos plásticos, e não em frascos que podem rachar.",
    "aumenta 3,10% de volume ao solidificar, como a água. O motivo está nos mesmos pares de átomos: no sólido, eles "
    "ocupam mais espaço; ao derreter, as ligações dos pares se rompem e o líquido fica mais compacto. Por causa da "
    "expansão, e também porque molha o vidro, o gálio costuma ser vendido em sacos de polietileno.")
acrescentar_trecho(14, 0, "In gallium, this anomalous behaviour is a result of the breaking of the Ga2 dimeric bonds present in the solid.")
substituir(14, "explicacao",
    "Ao contrário do mercúrio, o gálio líquido molha o vidro e a pele, e pintado no vidro vira um espelho brilhante.",
    "Ao contrário do mercúrio, ele molha também a pele, e pintado no vidro vira um espelho brilhante.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
# 0008: o sujeito da última frase do gancho é o inventor, não o aerogel
substituir(8, "gancho",
    "Ele também abriu caminho para o Gorilla Glass.",
    "O inventor também abriu caminho para o Gorilla Glass.")
