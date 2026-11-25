"""Rodada 2 de Asteroides e cometas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-asteroides_cometas-01.py"))
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


# 0002: o porquê das árvores de pé; "corpo" em vez de "rocha"
substituir(2, "explicacao", "esse desenho indicava uma origem aérea.",
    "esse desenho indicava uma origem aérea. O padrão se explica pela geometria da explosão: logo abaixo dela, a "
    "onda de choque desceu quase na vertical, arrancou os galhos e deixou os troncos em pé; mais longe, chegou "
    "quase na horizontal e deitou as árvores.")
substituir(2, "explicacao", "A hipótese preferida é a de uma rocha de 50 a 60 metros",
    "A hipótese preferida é a de um corpo de 50 a 60 metros (se asteroide ou cometa, ainda se discute)")
acrescentar_trecho(2, 0, "The trees directly below the explosion are stripped as the blast wave moves vertically downward, but remain "
    "standing upright, while trees farther away are knocked over because the blast wave is travelling closer to horizontal when it reaches them.")

# 0003: "em parte" pelo lado do Sol; o clarão também feriu
substituir(3, "gancho", "outro, que ninguém viu chegar porque vinha da direção do Sol, explodiu",
    "outro, que ninguém viu chegar, vindo do lado do Sol, explodiu")
substituir(3, "explicacao", "A explosão no ar não feriu ninguém diretamente.", "Nenhum pedaço do meteoro atingiu alguém.")

# 0004: "visitante confirmado"; hipóteses de 2023 e os "cometas escuros"; tipo de espanto
substituir(4, "gancho", "O primeiro objeto vindo de fora do Sistema Solar", "O primeiro visitante confirmado de fora do Sistema Solar")
substituir(4, "explicacao",
    "As propostas se multiplicaram: gelo de nitrogênio, como um pedaço de um planeta parecido com Plutão, ou gelo de "
    "hidrogênio, depois considerado incapaz de sobreviver à viagem. A composição dele continua desconhecida",
    "As propostas se multiplicaram: gelo de nitrogênio, como um pedaço de um planeta parecido com Plutão; gelo de "
    "hidrogênio puro, depois considerado incapaz de sobreviver à viagem; e, em 2023, hidrogênio formado por radiação "
    "dentro de um corpo rico em gelo de água e liberado perto do Sol, o que faria dele um cometa interestelar parecido "
    "com os nossos. Em 2024 já se conheciam 14 asteroides com o mesmo comportamento estranho, hoje chamados de "
    "\"cometas escuros\". Mesmo assim, a composição dele continua desconhecida")
trocar(4, tipos_espanto=["misterio_aberto", "contraintuitivo"])
acrescentar_trecho(4, 0, "On 22 March 2023, astronomers proposed the observed acceleration was \"due to the release of entrapped molecular "
    "hydrogen that formed through energetic processing of an H2O-rich icy body\", consistent with ʻOumuamua being an interstellar comet")
acrescentar_trecho(4, 0, "But by 2024, astronomers had identified 14 asteroids with the same unusual behavior. "
    "This makes ʻOumuamua the first member of another new class of objects called dark comets.")

# 0006: a frase do afundamento é da NASA; fonte da NASA
substituir(6, "explicacao", "Segundo a descrição citada pela Wikipedia, a sonda teria afundado", "Segundo a NASA, a sonda teria afundado")
CANDIDATOS[5]["fontes"].append({
    "url": "https://www.nasa.gov/missions/surprise-again-asteroid-bennu-reveals-its-surface-is-like-a-plastic-ball-pit",
    "titulo": "Surprise Again: Asteroid Bennu Reveals Its Surface Is Like a Plastic Ball Pit", "idioma": "en",
    "trecho": "After analyzing data gathered when NASA's OSIRIS-REx spacecraft collected a sample from asteroid Bennu in October 2020, "
              "scientists have learned something astonishing: The spacecraft would have sunk into Bennu had it not fired its thrusters "
              "to back away immediately after it grabbed dust and rock from the asteroid's surface. "
              "It turns out that the particles making up Bennu's exterior are so loosely packed and lightly bound to each other"})

# 0007: velocidade de escape "cerca de 1 m/s, ou menos"
substituir(7, "explicacao", "Como a velocidade de escape do cometa é de só 1 metro por segundo",
    "Como a velocidade de escape do cometa é de cerca de 1 metro por segundo, ou menos")

# 0008: doação x venda; "a pedra" na base aérea
substituir(8, "explicacao",
    "Em 1956, Ann o vendeu ao museu de história natural do Alabama, contra a vontade do marido, que lembrava de um valor de uns 25 dólares.",
    "Em 1956, a pedra foi parar no museu de história natural do Alabama: os registros falam em doação, e o marido "
    "lembrava de uma venda, contra a vontade dele, por uns 25 dólares.")
substituir(8, "explicacao", "Enquanto ela estava na base,", "Enquanto a pedra estava na base aérea,")
acrescentar_trecho(8, 0, "The Hodgeses donated it to the Alabama Museum of Natural History in 1956.")

# 0009: "quase" do tamanho da Terra; "tornou muito provável"
trocar(9, gancho="Em 1994, os pedaços de um cometa despedaçado bateram em Júpiter e deixaram manchas quase do tamanho da Terra. "
    "A cena também ajudou a explicar um enigma: as fileiras de crateras em duas luas do planeta.")
substituir(9, "explicacao", "O Shoemaker-Levy 9 indicou a explicação: trens de fragmentos",
    "O Shoemaker-Levy 9 tornou muito provável a explicação: trens de fragmentos")

# 0011: a chance de colisão, em vez de "sem fotografar"
trocar(11, gancho="Na imagem popular, naves desviam de pedras num cinturão de asteroides apinhado. O de verdade é quase vazio: "
    "a chance de uma sonda que o atravessa bater num asteroide é estimada em menos de 1 em 1 bilhão.")
acrescentar_trecho(11, 0, "Due to the low density of materials within the belt, the odds of a probe running into an asteroid are "
    "estimated at less than 1 in 1 billion.")

# 0012: o recorde vigente é o nível 4 na escala de Torino
trocar(12, gancho="Em dezembro de 2004, o asteroide Apophis chegou a 2,7% de chance de bater na Terra em 2029 e ao nível 4 de 10 "
    "na escala de risco, recorde até hoje. O choque foi descartado, mas passará mais perto que muitos satélites.")
acrescentar_trecho(12, 1, "This possibility kept it at Level 1 on the 0 to 10 Torino impact hazard scale")

# 0013: a Terra cruza os restos, não o cometa
substituir(13, "explicacao", "Curiosamente, o encontro com o Halley se repete todo ano, de forma inofensiva.",
    "Curiosamente, a Terra cruza restos do Halley todo ano, de forma inofensiva.")

# 0014: o grão mais velho, 3 ± 2 bilhões a mais; fragmentos somam 100 kg
substituir(14, "gancho", "Os mais velhos têm cerca de 7 bilhões de anos: são o material mais antigo já achado na Terra.",
    "O mais velho tem cerca de 7 bilhões de anos: é o material mais antigo já achado na Terra.")
substituir(14, "explicacao", "Os mais antigos têm cerca de 7 bilhões de anos, uns 2,5 bilhões a mais que a Terra e o Sol, de 4,54 bilhões.",
    "O mais antigo deles teria uns 3 bilhões de anos a mais que a Terra e o Sistema Solar, de 4,54 bilhões, ou seja, "
    "perto de 7 bilhões, com margem de erro de 2 bilhões para mais ou para menos.")
substituir(14, "explicacao", " Os próprios autores lembram que as estimativas de quanto tempo a poeira sobrevive no espaço dependem muito "
    "de modelos teóricos, com grandes incertezas.", "")
substituir(14, "explicacao", "Tem mais de 100 kg", "Os fragmentos recolhidos somam mais de 100 kg")
acrescentar_trecho(14, 0, "The oldest of these grains was found to be 3 ± 2 billion years older than the 4.54 billion years age of the "
    "Earth and Solar System, making it the oldest material found on Earth to date.")

# 0016: Dactyl notada em 1994; "dois blocos grudados"
substituir(16, "gancho", "A primeira foi achada em 1993, em fotos de uma sonda.",
    "A primeira foi fotografada por uma sonda em 1993 e notada nas imagens em 1994.")
substituir(16, "gancho", "é feita de duas pedras grudadas, algo nunca visto", "é feita de dois blocos grudados, algo inédito")
substituir(16, "gancho", "a lua de um asteroide de menos de 1 km", "a lua de um asteroide de 790 m")
substituir(16, "explicacao", "Nas imagens, uma integrante da missão, Ann Harch, achou um corpo pequeno ao lado dele",
    "Nas imagens, que por uma falha na antena só chegaram em parte em fevereiro de 1994, uma integrante da missão, "
    "Ann Harch, achou um corpo pequeno ao lado dele")
acrescentar_trecho(16, 0, "Transmission of many Ida images was delayed due to a permanent failure in the spacecraft's high-gain antenna. [...] "
    "The remaining images were sent in February 1994, when the spacecraft's proximity to the Earth allowed higher speed transmissions.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(14, "explicacao", "Os fragmentos recolhidos somam mais de 100 kg e foi visto caindo, o que o tornou um dos meteoritos mais estudados.", "Os fragmentos recolhidos somam mais de 100 kg, e o meteorito foi visto caindo, o que o tornou um dos mais estudados do mundo.")
substituir(16, "explicacao", "que por uma falha na antena só chegaram em parte em fevereiro de 1994", "das quais uma parte, por uma falha na antena, só chegou em fevereiro de 1994")
