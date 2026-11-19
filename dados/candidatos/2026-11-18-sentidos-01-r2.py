"""Rodada 2 de Sentidos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-sentidos-01.py"))
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


# 0001: "escocesa" não está nas fontes
substituir(1, "gancho", "Uma escocesa, Joy Milne,", "Uma mulher, Joy Milne,")

# 0002: a ausência pode indicar, não indica sempre
substituir(2, "explicacao", "sua ausência indica perda auditiva", "sua ausência pode indicar perda auditiva na cóclea")

# 0004: duas estimativas de duração; a FDA negou em 1974
substituir(4, "explicacao",
    "O efeito dura uma ou duas horas, até as papilas voltarem a perceber pH neutro, e o mecanismo detalhado ainda não é conhecido.",
    "O efeito dura de cerca de meia hora a uma ou duas horas, conforme a fonte, e o mecanismo detalhado ainda não é conhecido.")
substituir(4, "explicacao",
    "Nos anos 1980, uma tentativa de vendê-la nos Estados Unidos como forma de adoçar sem calorias esbarrou na agência reguladora FDA, que a classificou como aditivo alimentar e exigiu provas de segurança.",
    "Em 1974, a agência reguladora americana FDA negou o uso da miraculina como aditivo alimentar, o que barrou uma tentativa de vendê-la nos Estados Unidos como forma de adoçar sem calorias.")
substituir_trecho(4, 0, " [...] Des Marchais", " [...] This effect lasts until the protein is washed away by saliva (up to about 30 minutes). [...] Des Marchais")
substituir_trecho(4, 0, " In the 1980s in the United States, an attempt was made to commercialize the fruit for its ability to mask non-sweet foods as sweet without a caloric cost, but the Food and Drug Administration classified the berry as a food additive and required evidence of safety.", "")
acrescentar_trecho(4, 1, "The use of miraculin as a food additive was denied in 1974 by the United States Food and Drug Administration.")

# 0005: sem o ano (a Wikipedia erra: o estudo é de 2011); a ressalva sobre V1
substituir(5, "explicacao", "Em 2014, Thaler e colegas puseram", "Num estudo de Thaler e colegas, os pesquisadores puseram")
substituir(5, "explicacao",
    "O resultado surpreendeu porque essas áreas costumam funcionar só em tarefas visuais. A explicação é a neuroplasticidade: o cérebro remapeia a função dessa região.",
    "Isso foge à regra, já que essa região normalmente só trabalha quando os olhos estão em ação. Os pesquisadores "
    "atribuem a mudança à neuroplasticidade, a capacidade do cérebro de reaproveitar uma área para outra função. "
    "Ainda não se sabe quanto essa ativação contribui de fato para a habilidade.")
acrescentar_trecho(5, 0, "Despite this evidence, the extent to which activation in the visual cortex in blind echolocators contributes to echolocation abilities is unclear.")

# 0006: "mais de 20 anos"; 180 ms é onde o efeito começa a enfraquecer
substituir(6, "gancho", "há 20 anos", "há mais de 20 anos")
substituir(6, "explicacao",
    "Ele resiste até a um atraso: o som pode chegar 180 milissegundos depois da imagem e ainda assim ser fortemente influenciado por ela.",
    "Ele resiste até a um descompasso: o efeito continua forte quando o som chega até 180 milissegundos depois "
    "da imagem, e só a partir daí começa a enfraquecer.")
substituir_trecho(6, 0, "even when it lagged the visual stimuli by 180 milliseconds",
    "even when it lagged the visual stimuli by 180 milliseconds (point at which McGurk effect begins to weaken)")

# 0007: sem "a briga segue"
substituir(7, "gancho", "e a briga segue.", "e a questão segue sem resposta.")

# 0008: a cura espontânea existe; sem "muita gente evita"
trocar(8, nota_surpresa=3,
    gancho="Uma das causas mais comuns de vertigem são cristaizinhos de cálcio que se soltam dentro do ouvido. O "
           "tratamento é uma sequência de movimentos de cabeça que os tira do lugar errado, mas que provoca tontura forte.")
substituir(8, "explicacao",
    "Mesmo assim, há quem sofra à toa durante anos: a cura dificilmente acontece por acaso, porque as manobras eficazes provocam uma vertigem forte, e a pessoa naturalmente resiste a esses movimentos.",
    "Sem tratamento, o quadro pode sumir sozinho em dias ou meses, mas pode voltar. E as manobras têm um preço: "
    "como as eficazes provocam uma vertigem forte, a pessoa tende a resistir a elas. Além disso, a manobra certa "
    "depende de qual canal foi afetado.")
acrescentar_trecho(8, 0, "When untreated, it might resolve in days to months; however, it may recur in some people. [...] "
    "it is essential to determine the kind of nystagmus ( horizontal, vertical, or diagonal ) to select the correct cure maneuver.")

# 0010: "não viam diferença nenhuma" exagera
substituir(10, "explicacao", "que não viam diferença nenhuma", "que, apesar disso, não enxergavam cores a mais")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(8, "gancho", "mas que provoca tontura forte.", "mas que costuma provocar tontura forte.")
