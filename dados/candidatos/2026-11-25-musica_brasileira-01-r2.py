"""Rodada 2 de Música brasileira: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-musica_brasileira-01.py"))
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)

LOTE, AREA, TEMA = _base.LOTE, _base.AREA, _base.TEMA
wiki = _base.wiki
CANDIDATOS = _base.CANDIDATOS

OPOVO_CARMEN = ("https://www.opovo.com.br/vidaearte/2025/08/06/"
                "70-anos-sem-carmen-miranda-por-que-a-quotpequena-notavel-quot-ganhou-fama-internacional.html")


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


# 0002: Getz também estava no grupo; crédito contestado, sem direitos e cachê fixo
substituir(2, "gancho", "Foi escolhida por ser a única do grupo que falava bem inglês",
    "Escolhida por ser a única dos brasileiros do grupo que falava bem inglês")
substituir(2, "explicacao", "Mesmo assim, Astrud nunca recebeu crédito nem direitos e ganhou apenas 120 dólares.",
    "Mesmo assim, Astrud não recebeu direitos sobre a gravação: ganhou um cachê fixo de 120 dólares.")

# 0003: a vaia de 1940 é contestada por Ruy Castro; "americanizada" veio depois
substituir(3, "gancho", "Em 1940, vaiada no Rio por parecer \"americanizada\", respondeu com um samba e ficou 14 anos sem voltar.",
    "Em 1940, recebida com frieza no Rio e chamada de \"americanizada\", respondeu com um samba e ficou 14 anos sem voltar.")
substituir(3, "explicacao", "Foi vaiada até desistir e chorou no camarim.",
    "A saudação foi recebida em silêncio e, segundo o relato mais difundido, ela foi vaiada até desistir e chorou "
    "no camarim (o biógrafo Ruy Castro contesta a vaia e fala em recepção gelada).")
CANDIDATOS[2]["fontes"].append({
    "url": OPOVO_CARMEN,
    "titulo": "70 anos sem Carmen Miranda: por que a \"Pequena Notável\" ganhou fama internacional (O Povo)",
    "idioma": "pt",
    "trecho": (
        "o brasileiro Ruy Castro também escreveu uma biografia sobre Carmen Miranda. "
        "Publicada originalmente em 2005, o livro de 632 páginas desfaz alguns mal-entendidos. "
        "Dois deles: o de que Carmen teria se recusado a gravar \"Brasil Pandeiro\", de Assis Valente, e o de que ela teria sido vaiada no Cassino da Urca na noite de 15 de julho de 1940. [...] "
        "\"Dois meses antes, enfrentara o gelo da plateia de convidados da ditadura Vargas. "
        "Por Carmen ter dito uma ou duas frases em inglês, os muitos políticos, empresários e grã-finos pró-Hitler ali presentes rosnaram que ela voltara americanizada\""
    ),
})

# 0004: só a versão de Araci Cortes é dada como fracasso; a canção demorou a pegar
substituir(4, "gancho", "\"Aquarela do Brasil\" não fez sucesso no início", "\"Aquarela do Brasil\" demorou a estourar")
substituir(4, "explicacao", "e nem ela nem a de Araci Cortes emplacaram.",
    "e a de Araci Cortes, apesar da fama da cantora, não fez sucesso: a canção demorou a pegar.")

# 0005: "algumas", não "muitas"
substituir(5, "explicacao", "Das histórias que ele contou sobre essa década de viagens, muitas são postas em dúvida",
    "Das histórias que ele contou sobre essa década de viagens, algumas são postas em séria dúvida")
trocar(5, nota_surpresa=3)

# 0006: o título como dança folclórica é a versão de Milhaud; ponta brasileira no gancho
substituir(6, "explicacao",
    "O próprio Milhaud disse que o título, \"o boi no telhado\", era o nome de uma dança folclórica brasileira.",
    "Milhaud dizia que o título, \"o boi no telhado\", era o nome de uma dança folclórica brasileira, mas há outras "
    "explicações para ele.")
trocar(6, nota_surpresa=3,
    gancho="Uma obra famosa do compositor francês Darius Milhaud, \"O boi no telhado\", é uma colagem de mais de 20 "
           "músicas brasileiras, de 14 compositores, entre eles Ernesto Nazareth. Ele as ouviu como diplomata no Brasil.")
acrescentar_trecho(6, 0, "There have been various explanations of the title")

# 0007: datas divergentes, a reprovação da elite e as partes de flauta
substituir(7, "explicacao", "e \"Lamentos\", de 1928, e \"Carinhoso\", de 1930, foram atacados por excesso de jazz",
    "e \"Lamentos\" e \"Carinhoso\" foram atacados por excesso de jazz quando saíram")
substituir(7, "explicacao",
    "O grupo tinha músicos brancos e negros e tocava em casas de elite onde artistas negros antes eram barrados, o "
    "que desagradava parte da elite branca do Rio.",
    "O grupo tinha músicos brancos e negros e tocava em casas de elite onde artistas negros antes eram barrados. "
    "Mesmo assim, enfrentou a reprovação de parte da elite branca do Rio, que não aceitava negros se apresentando "
    "em casas populares.")
substituir(7, "explicacao", "Lacerda tocava as partes de flauta escritas para Pixinguinha",
    "Lacerda tocava as partes de flauta que Pixinguinha tinha escrito para ele mesmo tocar")

# 0010: a eliminatória de setembro de 1968 não foi no Rio
substituir(10, "explicacao", "no terceiro Festival Internacional da Canção, no auditório da universidade católica do Rio.",
    "numa eliminatória do terceiro Festival Internacional da Canção, no auditório da Universidade Católica.")

# 0011: sem a carteira de identidade, sem a data exata, primeira frase reescrita
trocar(11, gancho="Para driblar a censura, que barrava as músicas com seu nome, Chico Buarque inventou outro compositor, "
                  "Julinho da Adelaide, que assinou três canções e chegou a dar entrevista a um jornal.")
substituir(11, "explicacao",
    "Na ditadura militar, Chico Buarque já tinha visto \"Apesar de Você\" e \"Cálice\" serem proibidas, e o nome dele "
    "nos créditos bastava para atrair a atenção dos censores.",
    "Na ditadura militar, Chico Buarque já tinha tido \"Apesar de Você\" e \"Cálice\" vetadas, e qualquer canção "
    "assinada por ele passava a ser tratada com rigor máximo pelos censores.")
substituir(11, "explicacao",
    "Não era um simples pseudônimo: para dar ares de verdade à farsa, o compositor fictício ganhou cédula de "
    "identidade e até concedeu uma entrevista a um jornal da época.",
    "Não era um simples pseudônimo: o compositor fictício chegou a conceder entrevista a um jornal da época.")
substituir(11, "explicacao", "E, em 20 de outubro de 1974, um general da Polícia Federal proibiu",
    "E, em 1974, um general da Polícia Federal proibiu")

# 0012: sem aspas na fala de Rui Barbosa; paráfrases próximas reescritas
substituir(12, "explicacao",
    "setores conservadores viram ali uma afronta às convenções, e o senador Rui Barbosa classificou a música como "
    "exemplo da \"vulgarização dos costumes\".",
    "os conservadores se escandalizaram com a quebra de etiqueta, e o senador Rui Barbosa condenou a execução em "
    "discurso, como sinal de rebaixamento dos costumes.")
substituir(12, "explicacao",
    "Quando ela contratou um garoto para vender suas partituras pela cidade, parentes chegavam a rasgá-las.",
    "As partituras que um menino a serviço dela vendia nas ruas muitas vezes voltavam rasgadas por gente da família.")
substituir(12, "explicacao", "Estreou como maestrina em 1885, causando embaraço num meio dominado por homens,",
    "Em 1885, enfim regeu uma orquestra pela primeira vez, para constrangimento de jornalistas, atores e do maestro "
    "titular, pouco acostumados a ver uma mulher naquele posto,")

# 0013: o número de cópias varia entre os relatos
substituir(13, "gancho", "e distribuiu ele mesmo as 25 mil cópias. O sucesso atraiu as gravadoras.",
    "e saiu ele mesmo vendendo os discos pelo interior. O sucesso atraiu as gravadoras.")
substituir(13, "explicacao", "com 25 mil cópias que o próprio Cornélio distribuiu pelo interior de São Paulo.",
    "com 25 mil cópias que o próprio Cornélio distribuiu pelo interior de São Paulo (os números variam entre os "
    "relatos).")

# 0014: causalidade (o canto baixo vinha de Diamantina) e sem generalizar o "microfone único"
trocar(14, gancho="Ao gravar \"Chega de Saudade\", em 1958, João Gilberto pediu um microfone para a voz e outro para o "
                  "violão, o que chocou os produtores. Com o violão captado à parte, o canto quase falado deixava o "
                  "instrumento aparecer.")
substituir(14, "explicacao",
    "Até então, gravava-se com um só, que privilegiava a voz e deixava o violão em segundo plano, já que o "
    "instrumento tem volume modesto.",
    "O costume era não dar ao violão acompanhante um microfone próprio, o que privilegiava a voz e deixava o "
    "instrumento, de volume modesto, em segundo plano.")
substituir(14, "explicacao", "Daí o canto contido, sem vibrato e sem fortíssimos, que virou marca do gênero.",
    "O canto contido, sem vibrato e sem fortíssimos, que ele vinha lapidando desde Diamantina, casou com essa "
    "solução técnica e virou marca do gênero.")

# ganchos dentro do limite de 220 caracteres
substituir(3, "gancho", "símbolo do Brasil em Hollywood,", "símbolo do Brasil nos EUA,")
substituir(13, "gancho", "em 1929, o escritor Cornélio Pires", "em 1929, Cornélio Pires")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(2, "gancho", "Escolhida por ser a única dos brasileiros do grupo que falava bem inglês e recebeu só 120 dólares.", "Escolhida por ser a única dos brasileiros do grupo que falava bem inglês, ganhou só 120 dólares.")
substituir(6, "gancho", "Ele as ouviu como diplomata no Brasil.", "Milhaud as ouviu como diplomata no Brasil.")
substituir(7, "explicacao", "Nas gravações, Lacerda tocava as partes de flauta que Pixinguinha tinha escrito para ele mesmo tocar, que fazia o acompanhamento no saxofone.", "Nas gravações, Lacerda tocava as partes de flauta que Pixinguinha tinha escrito para si mesmo, enquanto Pixinguinha fazia o acompanhamento no saxofone.")
substituir(14, "explicacao", "e no início de 1957 chegou ao Rio.", "e no início de 1957 voltou ao Rio.")
