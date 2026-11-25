"""Rodada 2 de Corpo em condições extremas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-corpo_extremo-01.py"))
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


# 0003: o calor sai "quase só" por radiação; a evaporação pode formar gelo na boca
substituir(3, "explicacao", "sem ar, o calor só sai por radiação, um processo lento.",
    "sem ar, o calor sai quase só por radiação, um processo lento (a evaporação pode formar um pouco de gelo "
    "na boca, mas isso não é o perigo).")
acrescentar_trecho(3, 0, "Rapid evaporative cooling of skin moisture in a vacuum may create frost, particularly in the mouth, but this is not a significant hazard.")

# 0004: o comprimento médio voltou a perto do de antes
trocar(4, gancho="Nos 340 dias que Scott Kelly passou em órbita, seus telômeros, pontas dos cromossomos ligadas ao "
    "envelhecimento, ficaram mais longos. Na Terra, o comprimento médio voltou a perto do de antes. O gêmeo serviu de controle.")

# 0005-0007: 0007 vai a nota 3
trocar(7, nota_surpresa=3)

# 0008: o estudo de 2021 que achou benefício na força de preensão
substituir(8, "gancho", "outro repetiu o teste e não confirmou.",
    "outro repetiu o teste e não confirmou, e a disputa continua.")
substituir(8, "explicacao", "A questão segue em aberto.",
    "Em 2021, porém, um estudo britânico mediu outra coisa, a força necessária para segurar um objeto molhado, "
    "e viu que os dedos enrugados precisavam de menos força. A questão segue em aberto.")
CANDIDATOS[7]["fontes"].append(
    {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8294484/fullTextXML",
     "titulo": "Water-immersion finger-wrinkling improves grip efficiency in handling wet objects (Davis et al., PLoS ONE, 2021)",
     "idioma": "en",
     "trecho": "Water-immersion finger-wrinkling improves grip efficiency in handling wet objects [...] "
               "Department of Psychology, Manchester Metropolitan University, Manchester, United Kingdom [...] "
               "The results showed that wrinkly fingers reduce the grip force needed to grip a wet object, bringing that force in line with what is needed for handling a dry object."})

# 0012: sem a datação de 3.000 anos; causa do mal crônico com ressalva
substituir(12, "explicacao",
    " A adaptação tibetana é considerada o exemplo mais rápido conhecido de evolução humana: teria levado menos "
    "de 3.000 anos.", "")
substituir(12, "explicacao", "deixam o sangue mais viscoso e estão por trás do mal crônico das montanhas",
    "deixam o sangue mais viscoso e são apontadas como a causa do mal crônico das montanhas")
substituir_trecho(12, 0,
    "The high-altitude adaptation of the Tibetan people is the fastest known example of human evolution, as it is estimated to have occurred in a span of less than 3,000 years [...] ",
    "")

# 0013: 31 °C é o ponto em que a temperatura interna passa a subir sem controle, não o da morte
trocar(13, confianca="consenso_parcial",
    gancho="Calculava-se que o corpo humano aguentaria calor úmido até 35 °C de \"bulbo úmido\". Medido em jovens "
           "saudáveis numa câmara, o ponto em que a temperatura interna passou a subir sem controle ficou perto de 31 °C.")
substituir(13, "explicacao", "até o corpo não conseguir mais manter a temperatura interna.",
    "até o corpo não conseguir mais manter a temperatura interna. Esse ponto não é o da morte: é aquele a partir "
    "do qual a temperatura do corpo passa a subir sem parar, o que, mantido por muito tempo, pode levar à insolação.")
substituir(13, "explicacao", "o limite crítico ficou entre 30 °C e 31 °C; nos quentes e secos, entre 25 °C e 28 °C.",
    "o limite crítico ficou entre 30 °C e 31 °C.")
substituir_trecho(13, 0, "was the maximum a human could endure before they could no longer adequately regulate their body temperature [...] ",
    "was the maximum a human could endure before they could no longer adequately regulate their body temperature, which would potentially cause heat stroke or death over a prolonged exposure. [...] ")

# 0014: "significativamente", não "bem acima"
substituir(14, "explicacao", "o metabolismo basal das mergulhadoras ficava bem acima do registrado no verão",
    "o metabolismo basal das mergulhadoras ficava significativamente acima do registrado no verão")

# 0015: gancho centrado na carta de Paul Bert; nota 3
trocar(15, nota_surpresa=3,
    gancho="Em 1875, três franceses subiram no balão Zénith para bater o recorde de altitude e desmaiaram por falta de "
           "oxigênio; só um acordou. A carta de um fisiologista avisando que o oxigênio levado era pouco não chegou a tempo.")
