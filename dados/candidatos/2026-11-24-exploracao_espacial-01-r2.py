"""Rodada 2 de Exploração espacial: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-exploracao_espacial-01.py"))
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


# 0004: "cycle steals" são ciclos roubados, não interrupções
substituir(4, "explicacao", "e o computador recebia 6.400 interrupções por segundo,",
    "e o radar roubava do computador 6.400 ciclos de processamento por segundo,")

# 0005: o erro de 4% explica a queda em terra; a área quase desabitada é constatação separada
trocar(5, nota_surpresa=3)
substituir(5, "explicacao",
    "A estação não queimou tão rápido quanto se calculava e, por um erro de cálculo de quatro por cento, os "
    "destroços caíram numa área quase desabitada do oeste da Austrália.",
    "A estação não queimou tão rápido quanto se calculava e, por um erro de cálculo de quatro por cento, os "
    "destroços caíram em terra, cerca de 480 km a leste de Perth, no oeste da Austrália. Por sorte, era uma área "
    "quase desabitada.")

# 0007: a recusa da EMI é a versão de Druyan, contestada; frase removida
substituir(7, "explicacao",
    " A equipe também quis incluir \"Here Comes the Sun\", dos Beatles, mas a gravadora dona dos direitos recusou.", "")
substituir_trecho(7, 0,
    "Sagan's team wanted to include the Beatles 1969 song \"Here Comes the Sun\" on the record, but the record company EMI, which held the copyrights, declined. [...] ",
    "")

# 0011: ranking "quarto mais mortal" é frágil; regra das seis pessoas nos termos da fonte
substituir(11, "gancho", "É oficialmente o quarto desastre mais mortal da exploração espacial.",
    "Foi o maior acidente da história do programa espacial brasileiro.")
substituir(11, "explicacao",
    "As normas de segurança permitiam só seis pessoas na área naquele tipo de atividade, mas havia muito mais.",
    "Segundo as normas de segurança, só seis pessoas poderiam estar no local, mas havia muito mais.")
CANDIDATOS[10]["fontes"].append({
    "url": "https://olhardigital.com.br/2023/08/22/ciencia-e-espaco/acidente-na-base-de-alcantara-completa-20-anos/",
    "titulo": "Base de Alcântara: 20 anos do maior acidente da história do Programa Espacial Brasileiro (Olhar Digital)",
    "idioma": "pt",
    "trecho": "o Veículo Lançador de Satélites VLS-1 V03, um foguete de 21 metros de altura, explodiu em uma ignição prematura "
              "na Torre Móvel de Integração (TMI) por volta das 13h30 (hora local), matando 21 técnicos, engenheiros e cientistas – "
              "se tornando o maior acidente da história do Programa Espacial Brasileiro.",
})

# 0013: a frase da equipe vem de uma resenha citada pela Smithsonian; tolerância na costura; "hoje" é 2012
substituir(13, "gancho", "Costureiras trabalhavam com tolerância de menos de 1/64 de polegada por ponto.",
    "Nas costuras, as costureiras tinham uma tolerância de menos de 1/64 de polegada (cerca de 0,4 mm).")
substituir(13, "explicacao", "Segundo a revista Smithsonian, a equipe, liderada por",
    "Segundo uma resenha do livro Spacesuit: Fashioning Apollo, de Nicholas de Monchaux, citada pela revista "
    "Smithsonian, a equipe, liderada por")
substituir(13, "explicacao", "Hoje, mais de 300 trajes espaciais",
    "Em 2012, segundo a Smithsonian, mais de 300 trajes espaciais")
substituir_trecho(13, 2, "was a product of the industrial division of the women’s bra manufacturer Playtex. [...] ",
    "was a product of the industrial division of the women’s bra manufacturer Playtex. "
    "The L.A. Review of Books, in reviewing Spacesuit: Fashioning Apollo, described how [...] ")
substituir_trecho(13, 2, "Over 300 spacesuits,",
    "August 27, 2012 [...] From the book Spacesuit: Fashioning Apollo, by Nicholas de Monchaux [...] Over 300 spacesuits,")

# 0016: 14,4 km; só o estágio de subida foi à órbita solar; os 98% são do líder da busca; lógica da última frase
trocar(16, gancho="Em 1969, o módulo lunar da Apollo 10 chegou a 14,4 km da Lua sem poder pousar: tinha só metade do "
    "combustível para voltar. Sua parte de cima foi mandada para uma órbita em torno do Sol, e talvez tenha sido reencontrada.")
substituir(16, "explicacao", "levou Stafford e Cernan até 15,6 km da superfície",
    "levou Stafford e Cernan até 14,4 km da superfície")
substituir(16, "explicacao", "o combustível restante do Snoopy foi queimado para mandá-lo a uma órbita em torno do Sol",
    "o combustível restante do estágio de subida do Snoopy foi queimado para mandá-lo a uma órbita em torno do Sol")
substituir(16, "explicacao",
    "em 2019, a Royal Astronomical Society anunciou uma possível redescoberta: o pequeno asteroide 2018 AV2 seria o "
    "Snoopy, com \"98%\" de certeza.",
    "em 2019, o grupo anunciou uma possível redescoberta: o pequeno asteroide 2018 AV2 seria o Snoopy, com \"98%\" de "
    "certeza, segundo o astrônomo amador Nick Howes, que liderava a busca.")
substituir(16, "explicacao", "Se for, é a única nave que já levou tripulantes e que segue vagando pelo espaço vazia.",
    "Até onde se sabe, é a única nave que já levou tripulantes e que segue vagando pelo espaço, vazia.")
substituir_trecho(16, 0, "Cernan and Stafford surveyed ALS-2, coming within 15.6 kilometers (8.4 nautical miles; 9.7 miles) of the surface [...] ",
    "when the craft came within 14.4 kilometers (7.8 nautical miles; 9 miles) of the Moon, its closest approach. [...] ")
CANDIDATOS[15]["fontes"].append({
    "url": "https://www.universetoday.com/articles/apollo-10s-snoopy-lunar-lander-may-have-been-found-in-space",
    "titulo": "Apollo 10's Snoopy Lunar Lander May Have Been Found in Space (Universe Today)",
    "idioma": "en",
    "trecho": "Then in 2011, a group of amateur astronomers in the UK began looking for Snoopy. "
              "At the time, Universe Today covered the effort by amateur astronomer Nick Howes to search for Snoopy. [...] "
              "Now, 8 years later, Howes thinks they've found Snoopy at long last. [...] "
              "A report on Sky News says that the team is almost certain they've found it. Or 98% certain, anyway. [...] "
              "Howes stressed that some agency will have to get a better look at it before they can confirm that the object is Snoopy.",
})

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(13, "explicacao", "entre eles o de Neil Armstrong, estão no acervo", "entre eles o de Neil Armstrong, estavam no acervo")
substituir(16, "explicacao", 'de certeza, segundo o astrônomo amador Nick Howes, que liderava a busca.', 'de certeza, segundo a equipe do astrônomo amador Nick Howes, que liderava a busca.')
