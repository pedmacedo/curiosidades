"""Rodada 2 de Navegadores antigos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-navegacao_antiga-01.py"))
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


# 0001: aprovado; nota 4
trocar(1, nota_surpresa=4)

# 0002: o sistema "avatea" é uma leitura de 2019, debatida
trocar(2, confianca="consenso_parcial",
    gancho="Em 1769, o sacerdote e navegador Tupaia, das ilhas da Sociedade, desenhou para James Cook um mapa do "
           "Pacífico. Segundo uma leitura de 2019, ele usou um truque para traduzir sua navegação à bússola: o "
           "\"sol do meio-dia\".")
substituir(2, "explicacao", "Para os ingleses entenderem, Tupaia inventou um sistema:",
    "Segundo esses autores, para os ingleses entenderem, Tupaia teria inventado um sistema:")
substituir(2, "explicacao", "virava rumos de bússola.",
    "virava rumos de bússola. A leitura é debatida por outros especialistas, que interpretam o mapa de outro modo.")

# 0003: "evidência", não "prova"
substituir(3, "explicacao", "A chegada ao Taiti foi tomada como prova",
    "Para os acadêmicos, a chegada ao Taiti foi uma evidência")

# 0004: sem a frase das variedades maoris
substituir(4, "explicacao", " Na Nova Zelândia, as variedades maoris tinham tubérculos compridos de casca branca.", "")
substituir_trecho(4, 0, " [...] In New Zealand, the Māori varieties bore elongated tubers with white skin and a whitish flesh, which points to pre-European cross-Pacific travel.", "")

# 0005: aprovado; acrescenta a leitura do "mar solidificado" como gelo à deriva
substituir(5, "explicacao", "onde não se podia andar nem navegar.",
    "onde não se podia andar nem navegar. Esse mar provavelmente era o gelo à deriva da primavera, que o teria "
    "impedido de seguir mais ao norte.")
acrescentar_trecho(5, 0, "The mare concretum appears to match Strabo's pepēguia thalatta and is probably the same as the topoi (\"places\") "
    "mentioned in Strabo's apparent description of spring drift ice, which would have stopped his voyage further north")

# 0006: zenús sem "costa do Pacífico"; DNA "sugere"
substituir(6, "gancho", "Mas o DNA mostrou um contato real, mais provável com polinésios indo à América.",
    "Mas o DNA sugere que houve contato, mais provável com polinésios indo à América.")
substituir(6, "explicacao", "a parecença maior é com os zenús da costa do Pacífico da Colômbia",
    "a parecença maior é com os zenús, povo indígena da Colômbia")

# 0007: "verossímil" e os céticos Lloyd e Haywood
substituir(7, "gancho", "Hoje, é justo esse detalhe que dá crédito ao relato.",
    "Hoje, é justo esse detalhe que torna o relato verossímil.")
substituir(7, "explicacao", "Se tudo for verdade,",
    "Há céticos, porém: o egiptólogo A. B. Lloyd duvidou, em 1977, que um faraó autorizasse uma viagem assim, e o "
    "historiador John Haywood questiona como os fenícios teriam se abastecido e vencido as correntes e os ventos da "
    "costa oeste da África. Se tudo for verdade,")
acrescentar_trecho(7, 0, "Egyptologist A. B. Lloyd disputed in 1977 that an Egyptian Pharaoh would authorize such an expedition, except for the reasons of Asiatic conquest and trade in the ancient maritime routes. "
    "John Haywood has questioned whether the Phoenicians could have provisioned themselves how Herodotus describes, and also how they managed to get past the currents and winds on the West coast of Africa.")

# 0009: reprovado; fica como está

# 0012: o uso comercial é suposição da maioria
substituir(12, "explicacao", "e servia sobretudo ao comércio, mas em guerras também acelerou campanhas",
    "e, para a maioria dos estudiosos, servia sobretudo ao comércio, embora isso seja uma suposição, já que pouco se "
    "sabe desse uso; em guerras, também acelerou campanhas")
acrescentar_trecho(12, 0, "Little is known of its success in increasing trade")

# 0013: desmontagem atestada no Reino Médio; "um" babuíno
substituir(13, "gancho", "Nas viagens à terra de Punt, os navios egípcios eram desmontados",
    "No Reino Médio, os navios egípcios que iam a Punt eram desmontados")
substituir(13, "explicacao", "o DNA mitocondrial de outro babuíno mumificado",
    "o DNA mitocondrial de um babuíno mumificado")

# 0015: gancho com o dado mais forte; nota 3
trocar(15, nota_surpresa=3,
    gancho="Nos séculos XIII ou XIV, polinésios chegaram às ilhas Auckland, no mar frio ao sul da Nova Zelândia, "
           "comeram focas e albatrozes e foram embora. É o vestígio polinésio mais ao sul que se conhece.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(12, 'explicacao',
    'embora isso seja uma suposição, já que pouco se sabe desse uso',
    'embora isso seja uma suposição, já que pouco se sabe do quanto ele de fato impulsionou o comércio')
