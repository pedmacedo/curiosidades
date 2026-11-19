"""Rodada 2 de História da computação: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-17-historia_computacao-01.py"))
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


# 0001: o trocadilho é provável
substituir(1, "gancho", "e os operadores fizeram um trocadilho.", "e os operadores provavelmente fizeram um trocadilho.")

# 0004: a fonte diz "tecido por operárias" (sem "à mão")
substituir(4, "gancho", "O software que levou a Apollo à Lua foi tecido à mão: operárias passavam fios",
    "O software que levou a Apollo à Lua foi tecido por operárias, que passavam fios")

# 0006: navio romano; 1900 e 1901; data provável
trocar(6, nota_surpresa=3)
substituir(6, "gancho", "Um naufrágio grego guardava", "Um naufrágio perto de uma ilha grega guardava")
substituir(6, "explicacao",
    "Em 1901, mergulhadores que recolhiam esponjas acharam um naufrágio perto da ilha grega de Anticítera. "
    "Entre os destroços estava um bloco corroído que, no ano seguinte, revelou ter uma engrenagem dentro.",
    "Em 1900, mergulhadores que pescavam esponjas acharam os restos de um navio de carga romano perto da ilha "
    "grega de Anticítera. Entre os objetos resgatados em 1901 estava um bloco corroído que, no ano seguinte, "
    "revelou ter uma engrenagem dentro.")
substituir(6, "explicacao", "construído no século II antes de Cristo", "construído provavelmente no século II antes de Cristo")
acrescentar_trecho(6, 0, "Captain Dimitrios Kontos (Δημήτριος Κοντός) and a crew of sponge divers from Symi island discovered the Antikythera wreck in early 1900 [...] "
    "This wreck of a Roman cargo ship was found at a depth of 45 metres")

# 0007: Jacquard aproveitou ideias anteriores; mecanismo, não tear; o censo mudou por vários motivos
trocar(7, nota_surpresa=3,
       gancho="Os cartões perfurados dos primeiros computadores vieram de teares de tecido. A ideia, popularizada pelo tear de Jacquard (1804), passou por um censo americano e ajudou a criar a IBM.")
substituir(7, "explicacao", "criou um tear controlado por", "patenteou um mecanismo para teares controlado por")
substituir(7, "explicacao", "Antes, quem fazia essa seleção à mão era um ajudante.",
    "Nos teares tradicionais, essa seleção era feita à mão por um ajudante. Jacquard aproveitou ideias de "
    "inventores franceses anteriores, como Basile Bouchon, que em 1725 já usava uma fita de papel perfurada.")
substituir(7, "explicacao", "O processamento, que tinha levado oito anos no censo de 1880, caiu para seis.",
    "Somando as máquinas dele a várias outras mudanças no censo, o processamento, que tinha levado oito anos "
    "em 1880, caiu para seis.")
acrescentar_trecho(7, 0, "The machine was patented by Joseph Marie Jacquard in 1804, based on earlier inventions by the Frenchmen Basile Bouchon (1725), Jean Baptiste Falcon (1728), and Jacques Vaucanson (1740). [...] "
    "An improvement of the draw loom took place in 1725, when Basile Bouchon introduced the principle of applying a perforated band of paper.")
acrescentar_trecho(7, 1, "The net effect of the many changes from the 1880 census: the larger population, the data items to be collected, the Census Bureau headcount, the scheduled publications, and the use of Hollerith's electromechanical tabulators,")

# 0008: sem demonstração (não "não funcionou"); texto menos colado à fonte
trocar(8, gancho="O primeiro computador brasileiro, o Patinho Feio, da USP, ficou sem demonstração na própria inauguração, em 1972: um fotógrafo apressado pisou no cabo e a máquina apagou.")
substituir(8, "explicacao", "O Patinho Feio nasceu em 1972 como trabalho final de uma disciplina",
    "O Patinho Feio surgiu em 1972 como projeto de conclusão de uma disciplina")
substituir(8, "explicacao", "um fotógrafo afoito pisou no fio e o computador demorou a ser religado",
    "na pressa de registrar a cena, um fotógrafo pisou no cabo de energia, a máquina apagou e levou um bom "
    "tempo para voltar a funcionar")

# 0009: invenção paralela; trackball da própria Telefunken
trocar(9, tipos_espanto=["contraintuitivo", "historia_humana"])
substituir(9, "gancho", "dois meses antes da demonstração", "mais de dois meses antes da demonstração")
substituir(9, "explicacao", "Mas a ideia do mouse com uma bola embaixo veio de outro lugar.",
    "Mas o primeiro mouse com uma bola embaixo surgiu em outro lugar, numa invenção paralela e independente.")
substituir(9, "explicacao",
    "Ele derivava de um dispositivo ainda mais antigo, o trackball, inventado em 1946 por Ralph Benjamin para um "
    "sistema de radar militar do pós-guerra.",
    "Ele foi criado a partir de um trackball que a própria Telefunken já usava em mesas de controle de tráfego "
    "aéreo por radar. O trackball, por sua vez, já existia desde 1946, quando Ralph Benjamin o inventou para um "
    "sistema de radar militar do pós-guerra.")
acrescentar_trecho(9, 0, "Based on an even earlier trackball device, the mouse device had been developed by the company in 1966 in what had been a parallel and independent discovery. [...] "
    "As noted above, the device was based on an earlier trackball-like device (also named Rollkugel) that was embedded into radar flight control desks.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(8, "gancho", "O primeiro computador brasileiro, o Patinho Feio, da USP, ficou",
    "O Patinho Feio, da USP, considerado o primeiro computador brasileiro, ficou")
substituir(9, "explicacao", "O protótipo dele tinha sido construído em 1964 com a ajuda de Bill English",
    "O protótipo dele tinha sido construído com a ajuda de Bill English, que entrou na equipe em 1964,")
