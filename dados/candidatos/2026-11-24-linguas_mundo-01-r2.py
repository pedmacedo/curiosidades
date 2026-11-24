"""Rodada 2 de Línguas do mundo: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-linguas_mundo-01.py"))
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


# 0003: faixa de 58 a 130 consoantes; os 4.320 falantes são da língua rotokas inteira
substituir(3, "gancho",
    "tem pelo menos 58 consoantes, e numa contagem 82% das palavras básicas começam com um clique",
    "tem de 58 a 130 consoantes, conforme a contagem, e numa delas 82% das palavras básicas começam com um clique")
substituir(3, "explicacao",
    "Parte da divergência vem de decidir quais sons combinados contam como um só.",
    "Parte da divergência vem de decidir quais sons combinados contam como um só. Contando todos os sons "
    "consonantais, as listas chegam a 122 (DoBeS) ou 130 (Traill).")
substituir(3, "explicacao",
    "No extremo oposto está o dialeto central do rotokas, falado por cerca de 4.320 pessoas na ilha de Bougainville. Ele tem um dos menores",
    "No extremo oposto está o rotokas, língua falada por cerca de 4.320 pessoas na ilha de Bougainville. Seu "
    "dialeto central tem um dos menores")

# 0004: a despedida foi uma fala, não um texto escrito
substituir(4, "explicacao", "Ao encerrar o trabalho, escreveu a Charachidzé:",
    "Ao encerrar o trabalho, despediu-se de Charachidzé com estas palavras:")

# 0007: deixou de ser língua materna, não de ser falado
substituir(7, "explicacao",
    "Depois do fim do hebraico falado, no século II, a língua seguiu viva",
    "Depois que o hebraico deixou de ser língua materna, no século II, a língua seguiu viva")

# 0009: "quase só" gestos caseiros; a contestação de Stokoe e o debate aberto
substituir(9, "gancho", "que só conheciam gestos caseiros", "que antes usavam quase só gestos caseiros")
substituir(9, "explicacao", "criada do nada.",
    "criada do nada. Outros, como William Stokoe, contestam essa leitura e duvidam que não tenha havido "
    "influência externa; o debate entre inatismo e aprendizado segue aberto.")
acrescentar_trecho(9, 0,
    "William Stokoe, known by many as the father of American Sign Language linguistics, disagreed that the emergence of ISN is evidence of a language acquisition device. "
    "Stokoe also questions assertions that the language has emerged entirely without outside influence from, for example, Spanish or ASL. "
    "There is so far no final evidence available to resolve the controversy surrounding nativism v. cultural learning")

# 0010: antropólogo; os dois negam a briga, mas o repórter não conseguiu reuni-los
substituir(10, "gancho", "o linguista que os estudou", "o antropólogo que os estudou")
substituir(10, "explicacao",
    "Os dois chegaram a dar aulas da língua juntos a crianças e adolescentes, e o filho de Manuel passou a manter uma escola de ayapaneco no vilarejo.",
    "Os dois negam a briga e chegaram a dar aulas da língua juntos a crianças e adolescentes, embora um repórter "
    "que os visitou em 2013 não tenha conseguido reuni-los. O filho de Manuel passou a manter uma escola de "
    "ayapaneco no vilarejo.")
acrescentar_trecho(10, 2,
    "Both men vehemently deny to others that they refuse to talk to one another. "
    "But no one has heard them exchange conversation in quite some time, and this reporter failed to persuade either to pay a visit to the other fellow Ayapaneco-speaker for a little chat. [...] "
    "Published 12/13/13")

# 0013: ramo mais oriental na Antiguidade; uso litúrgico provável
trocar(13, gancho="O ramo mais oriental da família indo-europeia na Antiguidade, o tocário, foi escrito entre os séculos V e "
    "VIII no noroeste da China. E o chinês \"mì\", mel, pode vir dele, primo do inglês \"mead\", hidromel.")
substituir(13, "explicacao", "O tocário A servia como língua litúrgica budista.",
    "O tocário A provavelmente servia como língua litúrgica budista.")

# 0014: o apoio genético de 2025 é tentativo; fonte primária do estudo
substituir(14, "gancho", "Em 2025, um estudo genético trouxe o primeiro apoio do DNA à ideia.",
    "Em 2025, um estudo genético trouxe um apoio, ainda tentativo, à ideia.")
substituir(14, "explicacao",
    "Em 2025, geneticistas acharam a contribuição de uma mesma população antiga, que vivia a oeste do lago Baikal, tanto em povos atabascanos do Alasca quanto nos ieniseianos atuais.",
    "Em 2025, geneticistas acharam sinais, que eles mesmos chamaram de tentativos, de que uma mesma população "
    "antiga, que vivia a oeste do lago Baikal, contribuiu tanto para povos atabascanos do Alasca quanto para os "
    "ieniseianos atuais.")
CANDIDATOS[14 - 1]["fontes"].append({
    "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12342343/fullTextXML",
    "titulo": "Ancient DNA reveals the prehistory of the Uralic and Yeniseian peoples (2025, texto completo no Europe PMC)",
    "idioma": "en",
    "trecho": "One major analytic finding is our identification of Cisbaikal_LNBA as a genetic tracer-dye for the spread of early Yeniseian language speakers. "
              "We further show that ancient Athabaskans from Alaska ~1.1kya are unique among Arctic North Americans in lacking ancestry from Paleo-Eskimo populations but possess tentative signals of ancestry from a [...] "
              "APS population that also contributed distinctively to Yeniseian-speaking groups. "
              "These results help connect the movements of early Yeniseian-speaking groups to the Cis-Baikal region and may also provide [...] "
              "tentative genetic support for the linguistic connection between Yeniseian languages of Siberia and Athabaskan languages of North America",
})

# 0016: registro mais antigo conhecido; "segundo ele"; breves interrupções
substituir(16, "gancho",
    "Mas ele a ouviu de um professor de escola do Bronx, na plateia de uma palestra sua, nos anos 1940.",
    "Mas, segundo ele, a ouviu de um professor de escola do Bronx, na plateia de uma palestra sua, nos anos 1940.")
substituir(16, "explicacao",
    "Weinreich, estudioso do iídiche, publicou a frase pela primeira vez num texto apresentado como discurso em 5 de janeiro de 1945.",
    "O registro publicado mais antigo que se conhece da frase é um texto de Weinreich, estudioso do iídiche, "
    "apresentado como discurso em 5 de janeiro de 1945.")
substituir(16, "explicacao", "e a manteve, enquanto", "e a manteve, com breves interrupções, enquanto")
