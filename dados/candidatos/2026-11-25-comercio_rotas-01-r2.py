"""Rodada 2 de Comércio e rotas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-comercio_rotas-01.py"))
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


# 0003: tira a parte da África Ocidental (frases sem referência e contestadas); o relato de Heródoto só fala de ouro
substituir(3, "explicacao",
    "A prática ganhou o nome de comércio silencioso ou escambo mudo, e há registros dela em "
    "várias partes da África. Na África Ocidental, o ouro extraído ao sul do Sahel era trocado pelo sal do "
    "deserto, e a comunicação era feita com tambores. O método resolvia dois problemas: permitia negociar "
    "sem falar a mesma língua e talvez ajudasse a guardar o segredo de onde vinham o ouro e o sal.",
    "A prática ganhou o nome de comércio silencioso ou escambo mudo. A ideia por trás dela é engenhosa: "
    "permitia negociar sem falar a mesma língua e talvez ajudasse a guardar o segredo de onde vinha o ouro.")

# 0005: "parte delas" em vez de "muitas"; a crítica à escavação fica atribuída aos críticos
substituir(5, "gancho", "Muitas tinham motivos persas e inscrições do Corão, pensadas para outros mercados.",
    "Parte delas trazia motivos persas e inscrições do Corão, pensadas para outros mercados.")
substituir(5, "explicacao",
    "A escavação, feita às pressas e com fins comerciais, foi criticada por arqueólogos, e o Smithsonian "
    "adiou em 2011 uma exposição do tesouro.",
    "Arqueólogos criticaram a escavação como comercial e apressada demais, e o Smithsonian adiou em 2011 "
    "uma exposição do tesouro.")

# 0007: duração da travessia, 1815 em meio à guerra, e as ressalvas sobre o Havaí
substituir(7, "explicacao",
    "no fim de junho ou começo de julho e chegavam a Acapulco "
    "em março ou abril do ano seguinte; a travessia levava pelo menos quatro meses.",
    "no fim de junho ou começo de julho, e a travessia até "
    "Acapulco levava pelo menos quatro meses.")
substituir(7, "explicacao", "A rota durou "
    "até 1815, quando estourou a guerra de independência mexicana.",
    "A rota durou até 1815, em meio à guerra de independência mexicana.")
substituir(7, "explicacao",
    "à falta de meios dos espanhóis para explorar direito o Pacífico.",
    "à falta de meios dos espanhóis para explorar direito o Pacífico. Há pontas soltas: uma carta náutica "
    "espanhola capturada pelos ingleses em 1743 mostra ilhas na latitude do Havaí, e tradições orais havaianas "
    "falam de estrangeiros chegados antes de Cook, mas os historiadores não as consideram provas confiáveis.")
substituir(7, "explicacao",
    "Por isso, os navios iam "
    "abarrotados até nos conveses e cabines e, em casos extremos, rebocavam barcaças com mais carga, mesmo "
    "que isso tornasse a viagem lenta e arriscada.",
    "Por isso, os navios iam "
    "abarrotados até nos conveses e cabines e, em casos extremos, rebocavam barcaças com mais carga.")
acrescentar_trecho(7, 0,
    "A Spanish chart captured by the British in 1743 depicts islands in the latitude of Hawaii [...] "
    "he recorded several folk stories about foreigners who had visited Hawaii prior to first contact with Cook. [...] "
    "Scholars have dismissed these claims as lacking credibility.")

# 0010: só os caracteres que mantêm o búzio também na escrita simplificada
substituir(10, "gancho", "e em chinês \"comprar\" e \"preço\" levam o desenho de um búzio.",
    "e em chinês \"riqueza\" e \"gastar\" levam o desenho de um búzio.")
substituir(10, "explicacao", "como os de preço, "
    "gastar, comprar e riqueza.", "como os de gastar e riqueza.")

# 0012: o século VI é da fabricação; datas da descoberta em Berenice se contradizem no verbete
substituir(12, "gancho", "E, no século VI, uma estatueta de Buda do norte da Índia foi parar numa ilha da Suécia.",
    "E uma estatueta de Buda feita no norte da Índia no século VI foi parar numa ilha da Suécia.")
substituir(12, "explicacao", "A estátua egípcia foi achada em partes, em 2018 e 2022, no pátio",
    "A estátua egípcia foi achada em partes, em escavações recentes, no pátio")
substituir(12, "explicacao", "uma concha de batismo do Egito, ambas do século VI.",
    "uma concha de batismo do Egito, ambas feitas no século VI. Acredita-se que o Buda só tenha chegado à "
    "ilha na Era Viking.")
CANDIDATOS[11]["fontes"].append(wiki("Helg%C3%B6_Buddha",
    "The Helgö Buddha is a small Buddha figure of the 6th century Gupta Empire period, found during excavations at the site of a former trading post on the island of Helgö in Sweden. [...] "
    "It is believed to have come to Helgö during the Viking Age. It is North Indian",
    nome="Helgö Buddha"))

# 0014: "sobretudo", como na fonte ("especially")
substituir(14, "explicacao", "sempre ligado ao comércio de especiarias", "sobretudo ligado ao comércio de especiarias")
trocar(14, nota_surpresa=3)
