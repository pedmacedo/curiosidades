"""Rodada 2 de Sono e relógio biológico: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-sono_ritmos-01.py"))
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


# 0001: tese restrita ao Ocidente; a dívida de sono é suposição da fonte
trocar(1, gancho="Um historiador reuniu mais de 500 registros de que, antes da luz elétrica, era comum no Ocidente dormir "
    "em dois turnos: um \"primeiro sono\", uma hora ou mais acordado no meio da noite e um \"segundo sono\".")
substituir(1, "explicacao", "Depois de pagar a dívida de sono, eles passaram",
    "Depois de, ao que parece, pagar a dívida de sono, eles passaram")

# 0002: as fontes divergem na duração; sem o número 63
substituir(2, "explicacao", "Saiu depois de 63 dias convencido de que era 20 de agosto. Foi um choque.",
    "Quando a equipe anunciou o fim, depois de quase dois meses, ele estava convencido de que era 20 de agosto. "
    "Foi um choque.")

# 0003: o ritmo do assistente só se moveu em direção ao novo horário
substituir(3, "gancho", "O corpo do assistente se adaptou. O dele, não.",
    "O ritmo do assistente começou a se ajustar. O dele, não.")

# 0004: os 10 dias são a duração dos voos registrados, não um limite
substituir(4, "gancho", "Aves-fragata passam até 10 dias voando sobre o mar sem pousar.",
    "Aves-fragata voam dias seguidos sobre o mar sem pousar.")
trocar(4, nota_surpresa=5)

# 0006: nota
trocar(6, nota_surpresa=5)

# 0009: PAX8 de 2 a 3 minutos; outra base sugerida, não afirmada
substituir(9, "explicacao", "muda o sono em pouco mais de 3 minutos", "muda a duração do sono em apenas 2 a 3 minutos")
substituir(9, "explicacao", "Isso indica que o sono curto das famílias estudadas tinha outra base, ainda não identificada.",
    "Isso sugere que o sono curto das famílias estudadas pode ter outra base, ainda não identificada.")
substituir(9, "explicacao", "mostraram que outras pessoas com essas mutações",
    "mostraram que, em geral, outras pessoas com essas mutações")
substituir(9, "explicacao", "e a explicação se espalhou", "e a ideia de um \"gene do sono curto\" ficou famosa")

# 0012: essas células contribuem um pouco para a visão consciente
substituir(12, "gancho", "que não serve para enxergar.",
    "que quase não participa da visão: serve para acertar o relógio.")
substituir(12, "explicacao", "mantinham as respostas normais à luz que não dependem da visão",
    "mantinham as respostas normais à luz que não dependem da visão, e até percebiam vagamente uma luz azul intensa")
acrescentar_trecho(12, 0, "In work by Zaidi, Lockley and co-authors using a rodless, coneless human, it was found that a very intense "
    "481 nm stimulus led to some conscious light perception, meaning that some rudimentary vision was realized. [...] "
    "Since these cells respond mostly to blue light")
trocar(12, nota_surpresa=5)

# 0016: a descoberta do REM reescrita com palavras e ordem próprias
trocar(16, explicacao=(
    "Eugene Aserinsky era aluno de pós-graduação de Nathaniel Kleitman na Universidade de Chicago e passava horas "
    "observando as pálpebras de voluntários adormecidos. Para acompanhar a noite inteira, recorria a um "
    "eletroencefalógrafo antigo, que consumia uns 800 metros de papel a cada noite. Nos registros, surgiam várias "
    "fases em que os olhos de quem dormia se moviam depressa, de um lado para o outro. Kleitman quis ver o resultado "
    "repetido, e a voluntária da nova rodada foi a filha dele, Esther. Em 1953, os dois apresentaram a descoberta do "
    "sono REM, sigla em inglês para movimentos rápidos dos olhos, e associaram essas fases aos sonhos e a um cérebro "
    "mais ativo. William Dement, outro aluno de Kleitman, diria que naquele ano o estudo do sono virou um campo "
    "científico de verdade. Aserinsky e Kleitman costumam ser considerados os fundadores da pesquisa moderna do sono. "
    "Em julho de 1998, aos 77 anos, Aserinsky morreu quando seu carro bateu numa árvore ao norte de San Diego. A "
    "autópsia não esclareceu a causa, mas levantou a possibilidade de que ele tivesse adormecido ao volante."
))

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
# 0001: a fonte diz "about an hour of wakefulness"
substituir(1, "gancho",
    "uma hora ou mais acordado no meio da noite",
    "cerca de uma hora acordado no meio da noite")
