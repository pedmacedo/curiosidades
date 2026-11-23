"""Rodada 2 de Exoplanetas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-exoplanetas-01.py"))
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


# 0003: "mais antiga conhecida"; ninguém percebeu o valor da chapa
trocar(3, gancho="A evidência mais antiga conhecida de um sistema planetário fora do nosso foi registrada em 1917, numa chapa "
                 "de vidro, e passou quase um século num arquivo sem que ninguém percebesse seu valor. Foi reconhecida em 2016.")

# 0004: as ejeções de massa coronal são a principal suspeita, não causa comprovada
substituir(4, "gancho", "E o Sol era também o culpado: suas erupções haviam estragado as rodas.",
    "E o Sol é também o principal suspeito de ter estragado as rodas.")
substituir(4, "explicacao",
    "Mais tarde, as falhas foram atribuídas a corrosão nos rolamentos de aço causada por arcos elétricos, que por sua vez "
    "vinham de ejeções de massa coronal do Sol.",
    "Uma análise posterior ligou as falhas a corrosão nos rolamentos de aço por arcos elétricos, que seriam provocados "
    "por ejeções de massa coronal do Sol. Os testes mostram que o mecanismo é possível, mas dificilmente será provado "
    "que foi isso o que aconteceu no Kepler.")
CANDIDATOS[3]["fontes"].append(
    {"url": "https://hackaday.com/2018/09/11/do-space-probes-fail-because-of-space-weather/",
     "titulo": "Do Space Probes Fail Because Of Space Weather? (Hackaday, 2018)", "idioma": "en",
     "trecho": "As it turns out, the failures of reaction wheels, specifically on the FUSE and Kepler missions, was correlated with space weather, specifically coronal mass ejections (CMEs) from the Sun. "
               "These CMEs induce a voltage across the bearings and the bearing races in the reaction wheels, and after testing, these researchers discovered it doesn’t take much to generate a small arc from the bearing to the bearing race. "
               "This arc causes a small bit of pitting, which over time increases the friction on the reaction wheels, eventually causing it to fail. [...] "
               "While the researchers provide the experimental data showing that bearings can fail due to a voltage across a bearing and a race, it’s unlikely we’ll ever be able to prove Kepler, FUSE, or Dawn suffered a reaction wheel failure because of space weather."})

# 0007: "estimaram"; o 2,53% e o modelo; conversão para Celsius; consenso_parcial
substituir(7, "gancho", "astrônomos mostraram que o planeta TrES-2b reflete", "astrônomos estimaram que o planeta TrES-2b reflete")
substituir(7, "explicacao", "passa de 1.800 graus \"\n            \"Fahrenheit, quente demais".replace('"\n            "', ""),
    "passa de 1.800 °F (quase mil graus Celsius), quente demais")
substituir(7, "explicacao", "Um mundo mais refletor produziria oscilações maiores.",
    "Um mundo mais refletor produziria oscilações maiores. Se toda essa oscilação viesse de luz refletida, o planeta "
    "refletiria 2,53%; mas, como boa parte dela parece ser brilho próprio do calor, a estimativa caiu para menos de 1%.")
acrescentar_trecho(7, 1, "If the entire day–night contrast were due to geometric albedo, it would be 2.53%, but modeling suggests that much of this is dayside emission due to the planet's high temperature and the true albedo is much lower. "
    "It is estimated to be less than 1%")
trocar(7, confianca="consenso_parcial")

# 0008: a massa de Kepler-51d sem o 3,8 (não bate com a densidade)
substituir(8, "explicacao", "tem 9,32 vezes o raio da Terra, quase o tamanho de Saturno, e só 3,8 vezes a massa dela.",
    "tem 9,32 vezes o raio da Terra, quase o tamanho de Saturno, mas massa de só algumas vezes a dela.")
substituir_trecho(8, 0, " Its mass, however, is only 3.8 times that of Earth.", "")

# 0011: TRAPPIST-1b sem atmosfera ou com uma muito tênue
substituir(11, "explicacao",
    "Mas não há evidência de atmosfera em nenhum deles, e as observações de TRAPPIST-1b descartaram que \"\n            \"ele tenha uma.".replace('"\n            "', ""),
    "Mas não há evidência de atmosfera em nenhum deles, e as observações do Webb indicam que TRAPPIST-1b não tem "
    "atmosfera ou tem só uma muito tênue.")
acrescentar_trecho(11, 0, "JWST observations indicate that it has either no atmosphere at all or a very thin one")

# 0015: o vale é de tamanhos raros, não ausentes; primeira frase reescrita
substituir(15, "gancho", "há um \"vale\" de tamanhos que quase não aparecem.", "há um \"vale\" de tamanhos bem mais raros que os vizinhos.")
substituir(15, "explicacao",
    "Segundo a NASA, o tamanho de planeta que ele mais encontrou, entre o da Terra e o de Netuno, não tem nenhum "
    "representante entre os nossos vizinhos, e ainda há muito a aprender sobre esses mundos.",
    "Esses mundos, maiores que a Terra e menores que Netuno, foram o tipo que o Kepler mais achou, e a NASA admite "
    "que ainda se sabe pouco sobre eles.")
