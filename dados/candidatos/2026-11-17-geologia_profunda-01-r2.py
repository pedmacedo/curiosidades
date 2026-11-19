"""Rodada 2 de Interior da Terra: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-17-geologia_profunda-01.py"))
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


# 0001: furos diferentes; meta de 15 mil m; 1994 foi a última tentativa
trocar(1, nota_surpresa=3,
       gancho="O buraco mais fundo já cavado, na Rússia, passou de 12 km e esbarrou em rochas a 180 °C. No caminho apareceram água e, a 6 km de profundidade, fósseis microscópicos de plâncton.")
substituir(1, "explicacao", "A ideia era passar dos 15 mil metros", "A meta era chegar a 15 mil metros")
substituir(1, "explicacao", "e a perfuração parou em 1992.", "e essa tentativa, num novo ramo do poço, parou em 1992.")
substituir(1, "explicacao", "Em 1994 o projeto acabou por falta de dinheiro.", "Uma última tentativa foi interrompida em 1994 por falta de dinheiro.")

# 0002: o inédito era a plataforma solta; posicionamento dinâmico
trocar(2, gancho="Em plena corrida espacial, os EUA tentaram furar o fundo do mar até o manto da Terra. O projeto foi cancelado, mas inventou um jeito de manter um navio parado em alto-mar sem ancorá-lo.")
substituir(2, "explicacao",
    "Num navio sem âncora, sobre 3.600 metros de água, a equipe furou até 183 metros abaixo do fundo do mar, "
    "algo inédito, e os 13 metros finais eram de basalto.",
    "Para isso, a equipe inventou o que hoje se chama posicionamento dinâmico: quatro grandes motores de popa, "
    "guiados por um comando central e por técnicas acústicas, mantinham o navio CUSS I num raio de 180 metros. "
    "Assim, sobre 3.600 metros de água, ele furou até 183 metros abaixo do fundo do mar. O inédito não era a "
    "profundidade, e sim perfurar a partir de uma plataforma solta em águas profundas. Os 13 metros finais "
    "eram de basalto.")
acrescentar_trecho(2, 0, "Project Mohole expanded its operational depth by inventing what is now known as dynamic positioning. "
    "By mounting four large outboard motors on the ship, positioning the ship within surrounding moorings using acoustic techniques, "
    "and guiding the motors by a central joy stick, CUSS I could maintain a position within a radius of 180 m (600 feet).")

# 0004: 525–660 km; "evidência", não "prova"
trocar(4, gancho="Um diamante achado em Juína (MT) trouxe do manto um mineral com água presa nos cristais. Estima-se que essas rochas profundas guardem de uma a três vezes a água de todos os oceanos.")
substituir(4, "explicacao", "entre 410 e 660 km de profundidade, na chamada zona de transição do manto.",
    "entre cerca de 525 e 660 km de profundidade, na parte inferior da chamada zona de transição do manto (de 410 a 660 km).")
substituir(4, "explicacao", "a prova de que existe água no manto.", "uma evidência de quantidades significativas de água no manto.")
acrescentar_trecho(4, 0, "formed at high temperatures and pressures of the Earth's mantle between 525 and 660 km (326 and 410 mi) depth. [...] "
    "providing evidence of significant amounts of water")

# 0005: o que intriga é o enfraquecimento
substituir(5, "explicacao", "A causa exata intriga os geofísicos.", "Esse enfraquecimento progressivo ainda intriga os geofísicos.")

# 0006: estimativa, não medição direta
trocar(6, gancho="Cerca de metade do calor que sai do interior da Terra vem da radioatividade das rochas, segundo estimativas feitas captando neutrinos, partículas fantasmas que atravessam o planeta.")
substituir(6, "explicacao", "As medições indicaram que cerca de metade do calor interno da Terra é radiogênico.",
    "As primeiras medições indicaram que cerca de metade do calor interno da Terra é radiogênico, em linha com "
    "estimativas anteriores, mas a divisão exata ainda é bem incerta.")

# 0007: a origem por placas subduzidas é a hipótese mais aceita
substituir(7, "explicacao", "Uma explicação liga essas massas", "A hipótese hoje mais aceita liga essas massas")
acrescentar_trecho(7, 0, "The current leading hypothesis")

# 0008: sem a comparação com os dinossauros; listras ficam para o 0010
trocar(8, gancho="O fundo dos oceanos é jovem: quase nunca passa de 200 milhões de anos, uma fração da idade da Terra, porque é reciclado sem parar.")
substituir(8, "explicacao",
    " O fundo do mar \"\n            \"ainda guarda",
    "") if False else None
_e = CANDIDATOS[7]["explicacao"]
CANDIDATOS[7]["explicacao"] = _e[: _e.index(" O fundo do mar ainda guarda")]

# 0010: "até 780 mil anos atrás"
substituir(10, "gancho", "Há 780 mil anos, uma bússola apontaria para o sul", "Até 780 mil anos atrás, uma bússola apontaria para o sul")
substituir(10, "explicacao", "e o que hoje atrai a agulha da bússola passa a repelir", "e a agulha da bússola passa a apontar para o sul")
trocar(10, nota_surpresa=3)

# 0011: "formado na Terra"; grafite em um zircão
substituir(11, "gancho", "O material mais antigo da Terra são", "O material mais antigo formado na Terra são")
substituir(11, "explicacao", "Há até grafite dentro de alguns zircões", "Há até grafite dentro de um desses zircões")

# --- ajuste pontual da rodada 2 (aplicado sem 3ª verificação) ---
substituir(11, "explicacao", "Há até grafite dentro de um desses zircões com proporções",
    "Há até grafite dentro de outro zircão do local, um pouco mais novo, com proporções")
acrescentar_trecho(11, 0, "graphite embedded within a 4.1 billion-year-old zircon")
