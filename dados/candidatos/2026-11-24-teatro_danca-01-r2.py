"""Rodada 2 de Teatro e dança: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-teatro_danca-01.py"))
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


# 0001: pouco se sabe com certeza sobre a vida de Okuni
substituir(1, "explicacao",
    "Okuni nasceu por volta de 1578 perto do grande santuário de Izumo, onde serviu como miko",
    "Pouco se sabe com certeza sobre a vida dela, mas, segundo os relatos, Okuni nasceu por volta de 1578 "
    "perto do grande santuário de Izumo, onde serviu como miko")
acrescentar_trecho(1, 0, "Few concrete details are known about her life")

# 0003: 1681 marca as bailarinas nos palcos, não o começo da dança feminina
substituir(3, "explicacao",
    "Quando as mulheres começaram a dançar balé, em 1681, os sapatos de dança femininos tinham salto.",
    "Em 1681, quando as bailarinas passaram a se apresentar nos palcos de balé, os sapatos de dança femininos tinham salto.")

# 0004: a data da demolição é incerta
substituir(4, "explicacao", "fechado na guerra civil inglesa e demolido em 1644",
    "fechado na guerra civil inglesa e demolido por volta de 1644–45")
acrescentar_trecho(4, 0, "It was pulled down in 1644–45 (the commonly cited document dating the act to 15 April 1644 is not reliable)")

# 0005: "aye" é "sim"
trocar(5, gancho="Na primeira edição impressa de \"Hamlet\", de 1603, o monólogo famoso diz: \"Ser ou não ser, sim, eis o ponto. "
    "Morrer, dormir, é só isso? Sim, só isso\". Esse texto só veio à tona em 1823, e sua origem ainda é discutida.")

# 0006: convenção do palco x resultados de laboratório
trocar(6,
    tipos_espanto=["contraintuitivo", "engenhosidade"],
    confianca="consenso_parcial",
    gancho="No nô japonês, os atores aprendem que erguer certas máscaras as deixa alegres e baixá-las as deixa tristes. "
           "Em laboratório, porém, voluntários viram o contrário, e a explicação parece estar na penumbra do palco.",
    explicacao=(
        "O nô é uma forma de teatro dançado encenada desde o século XIV, e em geral só o ator principal, o shite, "
        "usa máscara. Esculpidas em cipreste japonês, as máscaras estilizam a expressão em vez de eliminá-la, e "
        "algumas usam a luz para mudar de emoção. Pela convenção do palco, erguer levemente o rosto, gesto chamado "
        "de \"iluminar\" a máscara, revela traços que parecem sorrir; baixá-lo, \"nublando\" a máscara, a deixa "
        "triste ou zangada. Quando cientistas testaram isso, o resultado saiu invertido. Em 2000, Lyons e colegas "
        "viram que participantes britânicos e japoneses achavam alegre a máscara inclinada para baixo e triste a "
        "inclinada para cima, e outros estudos acharam a mesma tendência. Em 2013, Kawai e colegas mostraram que "
        "basta sobrepor à foto frontal de uma máscara as sombras dela inclinada para obter o mesmo efeito. A pista "
        "está na boca: inclinada para baixo, a máscara fica com os cantos dos lábios puxados para cima, como num "
        "sorriso, e um estudo de Miyata e colegas apontou a boca como o traço decisivo para julgar a emoção de uma "
        "máscara. No teatro, porém, o palco é escuro e cheio de sombras, e o público vê os atores de longe. Os "
        "autores sugerem que, ali, o formato da boca nem sempre fica visível, e a máscara inclinada para baixo pode "
        "não parecer alegre. Vista de perto, numa tela, a boca passa a dominar."
    ))
CANDIDATOS[5]["fontes"].append({
    "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0071389",
    "titulo": "Shadows Alter Facial Expressions of Noh Masks (Kawai et al., PLoS ONE, 2013)",
    "idioma": "en",
    "trecho": (
        "Experiment 2 further revealed that frontal Noh mask images having shadows of upward/downward tilted masks were evaluated as sad/happy, respectively. "
        "This was consistent with outcomes from preceding studies using actually tilted Noh mask images. [...] "
        "Using Noh masks as facial stimuli, Lyons et al. [5] showed that both British and Japanese participants attributed happiness to a downward tilted mask, and sadness to an upward tilted mask. [...] "
        "Miyata et al. [9] further demonstrated that different facial parts convey different emotions in a Noh mask, and that among the facial parts the mouth serves as a diagnostic feature in the categorical judgment of emotions. [...] "
        "The studies, however, revealed trends opposite to the convention of the Noh drama. "
        "That is, the mask is tilted upwards/downwards when signifying a happy/sad state, the gestures known as terasu (shining) and kumorasu (clouding), respectively [...] "
        "Specifically, the corners of the lips are pulled up for the downward tilted Noh mask, which are elements of a happy expression [...] "
        "In addition, the Noh stage is dark and full of shadows, and observers see the actors from a relatively distant location. "
        "Thus, during the actual Noh play, the shape of the mouth is not necessarily apparent from the observer [...] "
        "viewpoint, where downward tilted masks may not be likely to look happy. "
        "However, when closely looking at the mask alone on a computer monitor, as done in the present study, the shape of the mouth should clearly serve as a distinctive feature in the recognition of emotions [...] "
        "Lyons MJ, Campbell R, Plante A, Coleman M, Kamachi M, et al. (2000) The Noh mask effect [...] "
        "Kawai N, Miyata H, Nishimura R, Okanoya K (2013) Shadows Alter Facial Expressions of Noh Masks."
    ),
})

# 0008: a frase sobre Chaplin é da fonte, não dele
substituir(8, "explicacao",
    "ofício; para Chaplin, essa escola inspirou a comédia de todos os seus filmes.",
    "ofício; os quinze anos de Chaplin no music hall marcaram a comédia de todos os seus filmes.")

# 0009: a pausa da pandemia durou 14 meses
substituir(9, "explicacao", "A pandemia apenas suspendeu as sessões entre 2020 e 2021.",
    "Nem a pandemia encerrou oficialmente a temporada: as sessões ficaram suspensas por 14 meses, de março de "
    "2020 a maio de 2021, e a mesma montagem voltou ao palco do St Martin's.")
acrescentar_trecho(9, 0, "Performances at the St. Martin's Theatre were halted on 16 March 2020, along with all other West End shows, during the COVID-19 pandemic in the United Kingdom. "
    "The Mousetrap re-opened on 17 May 2021 after 14 months without performances.")

# 0011: não foi a estreia dele na dança; Feuillet publicou
substituir(11, "gancho",
    "Luís XIV estreou como bailarino aos catorze anos, no papel do Sol nascente, num balé que durava 13 horas.",
    "Aos catorze anos, Luís XIV dançou o papel do Sol nascente num balé que durava 13 horas.")
substituir(11, "explicacao", "criar um sistema para registrar as coreografias no papel, publicado em 1700.",
    "criar um sistema para registrar as coreografias no papel, publicado por Feuillet em 1700.")

# 0012: o nome é francês; o salão de péla não virou Covent Garden
substituir(12, "gancho", "Os outros driblavam a lei pondo música sob as falas, e chamaram isso de melodrama.",
    "Os outros acabaram driblando a lei pondo música sob as falas, e adotaram para isso um nome francês: melodrama.")
substituir(12, "explicacao",
    "e num antigo salão de jogo de péla que depois deu origem ao teatro de Covent Garden, hoje a Royal Opera House",
    "e num antigo salão de jogo de péla, de onde a segunda companhia se mudou em 1720 para o teatro de Covent "
    "Garden, hoje a Royal Opera House")

# 0013: Prinzler não estava no teatro; ele criou uma barra
substituir(13, "explicacao", "por causa de trincos difíceis de abrir", "em boa parte por causa de trincos difíceis de abrir")
substituir(13, "explicacao",
    "Um sobrevivente, Carl Prinzler, desenvolveu com um arquiteto portas que se abrem com uma simples pressão numa barra.",
    "Carl Prinzler, um vendedor de ferragens que por acaso escapou de estar entre as vítimas, desenvolveu com o "
    "arquiteto Henry H. Dupont uma barra que destrava a porta trancada com uma simples pressão por dentro.")
CANDIDATOS[12]["fontes"].append(wiki("Carl_Prinzler",
    "Carl Jacob Prinzler (June 6, 1870 – May 30, 1949) was an American engineer who invented the \"panic bar\"  device for doors that allowed them to be opened from the inside despite being locked on the outside. "
    "He was manager of the Builders Hardware Department at the Vonnegut Hardware Company in 1903, when, along with his architect and engineer neighbor Henry H. DuPont, he developed the first panic bar. [...] "
    "found employment as a sales clerk at the Lilly and Stalnaker Hardware Company in downtown Indianapolis. [...] "
    "Prinzler had been in Chicago on December 30, 1903, and, by some fortunate twist of fate, escaped becoming a victim of the tragic Iroquois Theatre Fire which claimed 600 lives. [...] "
    "All of the patent designs focused on a single lever bar (and related hardware) that would cause a locked door to pop open when simple interior pressure was exerted upon it.",
    nome="Carl Prinzler"))

# 0014: sem a "proibição de Madras de 1910"; não "restrita" aos templos
trocar(14, gancho="A dança indiana Bharatanatyam, condenada por missionários e autoridades coloniais, foi revivida nos anos "
    "1930 por Rukmini Devi, e o empurrão veio de uma bailarina russa: Anna Pavlova.")
substituir(14, "explicacao",
    "Em 1910, a Presidência de Madras, sob domínio britânico, proibiu a dança nos templos. ", "")
substituir(14, "explicacao", "A proibição provocou protestos, e a arte foi levada para fora dos templos.",
    "A campanha e as restrições provocaram protestos, e a arte foi levada para fora dos templos.")
substituir(14, "explicacao", "ficou restrita aos templos hindus tâmeis até o século XIX",
    "era ligada sobretudo aos templos hindus tâmeis até o século XIX")

# 0015: atrizes inglesas já em 1660; 1662 é a formalização
substituir(15, "gancho", "Na Inglaterra, as mulheres só foram autorizadas a atuar em 1662.",
    "Na Inglaterra, elas só chegaram aos palcos profissionais cerca de um século depois, nos anos 1660.")
substituir(15, "explicacao",
    "as licenças das companhias foram reeditadas em 1662 permitindo, pela primeira vez, que atrizes se apresentassem",
    "as licenças das companhias, reeditadas em 1662, passaram a permitir formalmente que atrizes se apresentassem")
substituir(15, "gancho",
    "commedia dell'arte italiana, na década de 1560. Na Inglaterra, elas só chegaram aos palcos profissionais cerca de um século depois, nos anos 1660.",
    "commedia dell'arte, nos anos 1560. Na Inglaterra, só chegaram aos palcos profissionais cerca de um século depois, nos anos 1660.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(13, "explicacao", "Carl Prinzler, um vendedor de ferragens que por acaso escapou de estar entre as vítimas,", "Carl Prinzler, gerente de um setor de ferragens numa loja de Indianápolis, que por acaso escapou de estar entre as vítimas,")
