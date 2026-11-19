"""Rodada 2 de Grandes navegações: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-17-grandes_navegacoes-01.py"))
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


# 0001: sem causalidade inventada para a Linha de Data
substituir(1, "explicacao", "É por isso que hoje existe a Linha Internacional de Data.",
    "Hoje esse descompasso é corrigido na Linha Internacional de Data: quem a cruza viajando para o oeste "
    "adianta o calendário em um dia.")
substituir_trecho(1, 0, "Back by one hour for every 15° of longitude crossed",
    "Back by one hour for every 15° of longitude crossed, and Forward by 24 hours upon crossing the International Date Line.")

# 0002: a cura era conhecida e foi ignorada; sem o número contraditório de Magalhães
trocar(2, tipos_espanto=["escala_absurda", "contraintuitivo", "historia_humana"],
    gancho="O escorbuto matou pelo menos 2 milhões de marinheiros entre 1500 e 1800. Laranja e limão já eram usados contra ele no século XVI, mas os médicos levaram dois séculos para aceitar a cura.",
    explicacao=(
        "Nos navios das grandes navegações, a comida durava meses, mas frutas e verduras frescas não. O "
        "resultado era o escorbuto, causado pela falta de vitamina C. Um relato da viagem de Fernão de "
        "Magalhães conta que as gengivas de alguns homens cresciam por cima dos dentes, a ponto de eles não "
        "conseguirem comer. Segundo um levantamento citado pelo historiador Jonathan Lamb, em 1499 Vasco da "
        "Gama perdeu 116 de seus 170 tripulantes, a maioria por escorbuto. O remédio não era segredo: em 1579, "
        "um livro espanhol recomendava laranja e limão, tratamento que a marinha espanhola já conhecia. Em "
        "1601, o capitão inglês James Lancaster deu suco de limão à tripulação de só um de seus quatro navios, "
        "e foram os outros três que adoeceram. Mesmo assim, os médicos influentes continuavam achando que o "
        "escorbuto era um problema de digestão. Em 1747, o médico escocês James Lind fez um dos primeiros "
        "experimentos clínicos controlados da história e mostrou o efeito das frutas cítricas, mas nem ele "
        "defendeu o limão como cura única. Só em 1795 a Marinha britânica decidiu dar suco de limão como ração "
        "diária a todos os navios de guerra."
    ))
CANDIDATOS[1]["fontes"][0]["trecho"] = (
    "Researchers have estimated that during the Age of Exploration (between 1500 and 1800), scurvy killed at least two million sailors. "
    "Jonathan Lamb wrote: \"In 1499, Vasco da Gama lost 116 of his crew of 170; [...] all mainly to scurvy.\" [...] "
    "In the 1519-1521 circumnavigation, Magellan's crew suffered from scurvy: \"above all other calamities this was the worst: in some men the gums grew over the teeth, both lowers and uppers, so that they could not eat in any way [...] "
    "In 1579, the Spanish friar and physician Agustin Farfán published a book in which he recommended oranges and lemons for treating scurvy, a remedy that was already known in the Spanish navy. "
    "In February 1601, Captain James Lancaster [...] Captain Lancaster conducted an experiment using four ships under his command. "
    "One ship's crew received routine doses of lemon juice while the other three did not receive such treatment. "
    "As a result, members of the non-treated ships started to contract scurvy [...] "
    "his assertion had no impact on the prevailing opinion of the influential physicians of the age, that scurvy was a digestive complaint. [...] "
    "It was not until 1747 that James Lind formally demonstrated that scurvy could be treated by supplementing the diet with citrus fruit, in one of the first controlled clinical experiments reported in the history of medicine. [...] "
    "Lind himself never actively promoted lemon juice as a single 'cure'. [...] "
    "In March 1795, it was reported that the Suffolk had arrived in India after a four-month voyage without a trace of scurvy [...] "
    "lemon juice and sugar should in future be issued as a daily ration to the crews of all warships.")

# 0003: sem a frase contraditória sobre a lenda
substituir(3, "explicacao",
    "Segundo a tradição, os maiores navios tinham quase o dobro do comprimento de qualquer navio de madeira "
    "registrado, embora isso seja lenda.",
    "Já a primeira viagem reuniu 317 navios e quase 28 mil tripulantes. Pela lenda, os maiores tinham quase o "
    "dobro do comprimento de qualquer navio de madeira já registrado.")
acrescentar_trecho(3, 0, "Zheng He's first voyage departed 11 July 1405, from Suzhou and consisted of a fleet of 317 ships holding almost 28,000 crewmen.")

# 0004: o tamanho do erro de Colombo
substituir(4, "explicacao",
    "Os críticos de Colombo estavam certos sobre a distância: ele só não morreu no meio do oceano porque havia "
    "um continente no caminho.",
    "Pelas contas de Colombo, o Japão ficava a uns 5 mil km de distância. Na verdade, são cerca de 20 mil km. "
    "Os críticos estavam certos, e a tripulação, já ficando sem comida e água, só se salvou porque havia um "
    "continente desconhecido no caminho.")
substituir_trecho(4, 0, "most European and Middle Eastern [...]", "most European and Middle Eastern scholars espoused Earth's sphericity. [...]")
acrescentar_trecho(4, 0, "The combined effect of these mistakes was that Columbus estimated the distance to Japan to be only about 5,000 km (or only to the eastern edge of the Caribbean) while the true figure is about 20,000 km. [...] "
    "they were running out of food and water with no chance of any new supplies within sailing distance. [...] "
    "Columbus' expedition was saved by reaching the Americas, about which he knew nothing, precisely at the point he thought he would reach Japan.")

# 0005: sem "troca" nem julgamento; a disputa com apoio no trecho
substituir(5, "explicacao", "Ingleses e holandeses disputaram a ilha.",
    "Em 1616, os moradores juraram lealdade aos ingleses, e um pequeno grupo de defensores resistiu a um cerco "
    "holandês por 1.540 dias.")
substituir(5, "explicacao",
    "Na época, a troca parecia boa para a Holanda, que garantia o controle da noz-moscada. Hoje, Manhattan é o "
    "coração de Nova York.",
    "Com isso, os holandeses mantiveram o monopólio da noz-moscada e do macis, que só acabou nas Guerras "
    "Napoleônicas. Já a ilha que os ingleses conservaram virou o coração de Nova York.")
acrescentar_trecho(5, 0, "In 1616, fearing the Dutch, the natives of the island pledged their allegiance to the employees of English East India Company [...] "
    "Courthope and 39 European defenders with their native allies held off the Dutch for 1540 days [...] "
    "The Dutch monopoly on nutmeg and mace lasted up till the Napoleonic Wars")

# 0006: as duas manobras separadas
trocar(6, gancho="Para voltar das ilhas do Atlântico, os navegadores portugueses primeiro se afastavam muito para o oeste. Rumo à Índia, o desvio os levava para perto do Brasil. Era a \"volta do mar\".")

# 0007: sem a frase duvidosa dos tomates selvagens; as datas no gancho
trocar(7, nota_surpresa=3,
    gancho="O tomate só chegou à Itália depois das viagens de Colombo: o primeiro livro de receitas italiano com molho de tomate é de 1692, e massa com molho só aparece em 1790.")
substituir(7, "explicacao",
    "O tomate é americano. Cultivadores levaram tomates selvagens da América Central para a América do Sul, "
    "e, pouco depois das viagens de Colombo, a planta chegou à Espanha",
    "O tomate é americano. Pouco depois das viagens de Colombo, a planta chegou à Espanha")
substituir_trecho(7, 0, "cultivators brought wild tomatoes from Central America to South America. ", "")

# 0008: a origem americana tem forte apoio, mas o debate não se encerrou de todo
trocar(8, tipos_espanto=["historia_humana", "origem_inesperada"], confianca="consenso_parcial")
substituir(8, "gancho", "Sua origem ainda é debatida.", "As evidências mais recentes apontam para as Américas.")
substituir(8, "explicacao",
    "A origem continua em debate. Uma hipótese diz que a doença veio das Américas com os marinheiros de "
    "Colombo; a outra, que já existia na Europa sem ser reconhecida. Sabe-se que doenças aparentadas existiam "
    "nas Américas muito antes do contato com os europeus.",
    "A origem foi debatida por muito tempo: uma hipótese dizia que a doença veio das Américas com os "
    "marinheiros de Colombo; a outra, que já existia na Europa sem ser reconhecida. Análises genéticas de "
    "2008 e 2024 indicam que a família de bactérias da sífilis surgiu nas Américas, há no máximo cerca de 9 "
    "mil anos. Isso não prova que foram os marinheiros de Colombo que a levaram, e uma das autoras do estudo "
    "de 2024 acha que o debate vai continuar.")
acrescentar_trecho(8, 0, "Phylogenetic analyses in 2008 and 2024 showed syphilis originated in the Americas around 9,000 years ago")
CANDIDATOS[7]["fontes"].append({
    "url": "https://www.smithsonianmag.com/smart-news/ancient-dna-offers-crucial-hints-to-the-origin-of-syphilis-a-decades-long-mystery-that-has-divided-scientists-180985713/",
    "titulo": "Ancient DNA Offers Crucial Hints to the Origin of Syphilis, a Decades-Long Mystery That Has Divided Scientists",
    "idioma": "en",
    "trecho": "The researchers also inferred that these ancient American variants of the bacteria shared a common ancestor that dates to 9,000 years ago at most [...] "
        "Though the study can’t prove that Columbus’ crew picked up the disease and brought it back to Europe, the researchers do suggest it was European colonization that spread syphilis throughout the rest of the world. [...] "
        "I think the narrative will continue to be debated.",
})

# 0009 (aprovado): tipo mais fiel
trocar(9, tipos_espanto=["historia_humana"])

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(2, "gancho", "mas os médicos levaram dois séculos para aceitar a cura.", "mas a Marinha britânica só adotou a cura em 1795.")
substituir(6, "explicacao", "Sem entender esses ventos, dizem os historiadores, os impérios marítimos europeus não teriam existido.",
    "Sem entender esses ventos, os impérios marítimos europeus não teriam existido.")
