"""Rodada 2 de História dos pratos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-historia_pratos-01.py"))
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


# 0002: o que não tem registro é o episódio, não a visita; ingredientes, não necessariamente a combinação
trocar(2, nota_surpresa=3)
substituir(2, "gancho", "Mas nenhum jornal da época noticiou a visita", "Mas nenhum jornal da época registrou o episódio")
substituir(2, "explicacao", "nenhum veículo de imprensa da época registrou a suposta visita",
    "nenhum veículo de imprensa da época registrou o suposto episódio")
substituir(2, "explicacao", "Além disso, a combinação já circulava em Nápoles décadas antes.",
    "Além disso, os mesmos ingredientes já apareciam em pizzas de Nápoles décadas antes.")

# 0004: al-Idrisi não diz que os moinhos faziam a massa nem que ela era seca
substituir(4, "gancho",
    "um geógrafo árabe já descrevia na Sicília moinhos que faziam massa seca aos montes e a exportavam em navios.",
    "um geógrafo árabe já descrevia na Sicília uma produção enorme de massa em fios, exportada em muitos navios.")

# 0006: "tempero" é tão plausível quanto "tempora"
substituir(6, "gancho", "O nome viria do latim \"tempora\", os dias de jejum católico.",
    "O nome talvez venha de \"tempora\", os dias de jejum católico, ou de \"tempero\".")
substituir(6, "explicacao", "Outra possibilidade é o português \"tempero\".",
    "Outra possibilidade, tão plausível quanto, é o português \"tempero\"; a questão segue em aberto.")

# 0007: a viagem de 1492 não chegou à América Central
substituir(7, "explicacao",
    "Colombo encontrou a pimenta na viagem de 1492 à América Central, e no máximo em 1528",
    "Colombo encontrou a pimenta na primeira viagem à América, iniciada em 1492, e no máximo em 1528")

# 0008: o frango tikka seco; Bangladesh; Robin Cook no gancho
trocar(8, nota_surpresa=3)
substituir(8, "gancho", "que um chanceler britânico chamou", "que o chanceler Robin Cook chamou")
substituir(8, "explicacao", "para um cliente que queria algo para acompanhar a carne seca",
    "para um cliente que achou o frango tikka seco demais e pediu um molho")
substituir(8, "explicacao", "provavelmente por um cozinheiro bengali", "provavelmente por um cozinheiro de Bangladesh")

# 0012: ligação com o pescado frito é crença difundida; judeus só a partir dos anos 1650; "uma das primeiras" lojas
trocar(12, nota_surpresa=3, confianca="consenso_parcial",
    gancho="O peixe frito do fish and chips, símbolo da Inglaterra, teria chegado ao país com judeus de origem "
           "portuguesa e espanhola vindos da Holanda. Frito na sexta, o peixe podia ser comido frio no Shabat.")
substituir(12, "explicacao",
    "Segundo o verbete sobre o prato, esse costume chegou à Grã-Bretanha com judeus espanhóis e portugueses que "
    "viviam na Holanda, alguns já no século XVI; a grande leva para Londres veio nos anos 1850.",
    "A versão mais repetida é que esse costume chegou à Inglaterra com judeus espanhóis e portugueses que viviam "
    "na Holanda, a partir dos anos 1650, quando a proibição à presença de judeus foi suspensa; a maior leva para "
    "Londres veio nos anos 1850. Ainda assim, a ligação direta com o fish and chips é tratada como crença "
    "difundida, não como fato provado.")
substituir(12, "explicacao", "A primeira loja registrada a vender os dois foi aberta por volta de 1860",
    "Uma das primeiras lojas registradas a vender os dois foi aberta por volta de 1860")
acrescentar_trecho(12, 1,
    "There is a general belief that pescado frito was possibly an inspiration for the English fish and chips, brought to England by Spanish Jews; "
    "Sephardim began to settle in England in small numbers after Oliver Cromwell lifted the formal ban in the 1650s.")

# 0013: gancho sem juntar 1939 e a tese dos Aliados; contradição explícita; cacio e uova; achado de 2026 (Il Post).
# O Il Post registra uma receita de abril de 1952 num jornal de Lille, anterior à de Chicago (dezembro de 1952):
# por isso o gancho e a explicação falam das "primeiras receitas", fora da Itália, em vez de só Chicago.
trocar(13, gancho="A carbonara, ícone de Roma, não tem receita impressa conhecida antes de 1952, e as primeiras saíram "
                  "fora da Itália: na França e em Chicago. A primeira italiana, de 1954, ainda levava alho e queijo gruyère.")
substituir(13, "explicacao", "No mesmo ano, um grande livro de cozinha italiano, Il cucchiaio d'argento, nem a menciona. ",
    "No mesmo ano, o livro de cozinha italiano Il cucchiaio d'argento nem a menciona. ")
substituir(13, "explicacao",
    "A primeira receita conhecida saiu em 1952, num livro ilustrado publicado em Chicago por Patricia Bronté. "
    "A primeira italiana, de 1954, levava pancetta, alho e queijo gruyère.",
    "As primeiras receitas conhecidas são de 1952: uma, assinada pelo ator Aldo Fabrizi, num jornal de Lille, na "
    "França, e outra num livro de Patricia Bronté sobre Chicago. A primeira italiana, de 1954, levava pancetta, "
    "alho e gruyère.")
substituir(13, "explicacao",
    "Para o escritor Alan Davidson e os historiadores Luca Cesari e Eleonora Cozzella, o prato surgiu depois que "
    "os Aliados tomaram Roma, em 1944.",
    "Uma tese difundida, defendida pelo escritor Alan Davidson e pelos historiadores Luca Cesari e Eleonora "
    "Cozzella, diz que o prato surgiu depois que os Aliados tomaram Roma, em 1944. Mas a menção de 1939 é "
    "anterior à chegada deles, e, quando ela veio a público, em 2026, o próprio Cesari disse que a história da "
    "carbonara precisa ser reescrita.")
substituir(13, "explicacao", "O nome segue sem explicação certa:",
    "Outra corrente liga a carbonara ao cacio e uova, massa com ovos e queijo documentada desde 1839, que alguns "
    "italianos nascidos antes da guerra associam a esse nome. O nome segue sem explicação certa:")
acrescentar_trecho(13, 0,
    "Cacio e uova is documented as far back as 1839 and, according to some researchers, anecdotal evidence indicates that some Italians born before World War II associate that name with the dish now known as \"carbonara\".")
CANDIDATOS[12]["fontes"].append({
    "url": "https://www.ilpost.it/2026/02/16/carbonara-attestazione-americani/",
    "titulo": "Forse la carbonara non la portarono gli americani",
    "idioma": "it",
    "trecho": "Ma una nuova prova attesta la prima menzione della carbonara al 23 agosto 1939, quindi anni prima dell’occupazione americana. [...] "
              "«La storia della carbonara è da riscrivere completamente», ha detto Cesari. [...] "
              "In entrambi i casi comunque sono solo citazioni del piatto, mentre la prima ricetta risale all’aprile del 1952 ed era stata trovata un anno fa dal critico e studioso di gastronomia Luca Cesari. "
              "Fu stampata sul giornale di Lille La Croix du Nord e fu scritta dall’attore Aldo Fabrizi. [...] "
              "Un’attestazione di poco successiva (dicembre del 1952) si trova su una guida ai ristoranti di Chicago dalla giornalista Patricia Bronté [...] "
              "La menzione del 1939 invece attesta che una qualche forma di “pasta alla carbonara” esisteva già prima, visto che gli americani arrivarono nel Lazio nel 1944.",
})

# 0014: "picante, sem o lado doce"; Zuo natural de Hunan
trocar(14, nota_surpresa=3)
substituir(14, "explicacao", "No começo, o prato era picante, não agridoce, e foi adaptado ao gosto americano.",
    "No começo, o prato era só picante, sem o lado doce, e foi adaptado ao gosto americano.")
substituir(14, "explicacao", "estadista e chefe militar da província de Hunan",
    "estadista e chefe militar natural da província de Hunan")

# 0013: texto reorganizado para caber em 250 palavras, mantendo as frases pedidas pelo verificador
trocar(13, explicacao=(
    "O nome spaghetti alla carbonara surge impresso em 1939, num jornal das Índias Orientais "
    "Holandesas que cita um restaurante do Trastevere, em Roma, sem descrever o prato. Em 1950, o jornal La Stampa "
    "contou que oficiais americanos procuravam a carbonara no Trastevere havia anos, mas um livro de cozinha "
    "italiano do mesmo ano, Il cucchiaio d'argento, nem a menciona. As primeiras receitas conhecidas são de 1952: "
    "uma, assinada pelo ator Aldo Fabrizi, num jornal de Lille, na França, e outra num livro de Patricia Bronté "
    "sobre Chicago. A primeira italiana, de 1954, levava pancetta, alho e gruyère. O guanciale e o pecorino "
    "entraram no fim dos anos 1950 e nos anos 1960, e o creme de leite só saiu da maioria das receitas nos anos "
    "1990. Uma tese difundida, defendida pelo escritor Alan Davidson e pelos historiadores Luca Cesari e Eleonora "
    "Cozzella, diz que o prato surgiu depois que os Aliados tomaram Roma, em 1944; segundo Cozzella, viria de um "
    "\"spaghetti breakfast\", bacon com ovos sobre o espaguete, pedido pelos soldados. Mas a menção de 1939 é "
    "anterior à chegada deles, e, quando ela veio a público, em 2026, o próprio Cesari disse que a história da "
    "carbonara precisa ser reescrita. Outra corrente liga a carbonara ao cacio e uova, massa com ovos e queijo "
    "documentada desde 1839, que alguns italianos nascidos antes da guerra associam a esse nome. O nome segue sem "
    "explicação certa: há quem pense em carvoeiros e quem pense na sociedade secreta dos Carbonari."
))
CANDIDATOS[12]["fontes"][1]["trecho"] = "Lunedì 16 febbraio 2026 [...] " + CANDIDATOS[12]["fontes"][1]["trecho"]

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(13, "explicacao", "O guanciale e o pecorino entraram no fim dos anos 1950 e nos anos 1960", "O guanciale e o pecorino se firmaram no fim dos anos 1950 e nos anos 1960")
substituir(13, "gancho", "A primeira italiana, de 1954, ainda levava alho e queijo gruyère.", "A primeira italiana, de 1954, levava alho e queijo gruyère.")
