"""Rodada 2 de Revolução científica: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-revolucao_cientifica-01.py"))
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


# 0001: "escreveu ou copiou"; a pedra filosofal "provavelmente"
substituir(1, "gancho", "Isaac Newton escreveu cerca de um milhão de palavras sobre alquimia e buscava a pedra filosofal.",
    "Isaac Newton escreveu ou copiou cerca de um milhão de palavras sobre alquimia e provavelmente buscava a pedra filosofal.")
substituir(1, "explicacao", "e a maior parte nunca foi impressa. ",
    "e a maior parte nunca foi impressa. Muitos dos escritos alquímicos são cópias de outros manuscritos, com "
    "anotações dele. ")
acrescentar_trecho(1, 1, "Of an estimated ten million words of writing in Newton's papers, about one million deal with alchemy. "
    "Many of Newton's writings on alchemy are copies of other manuscripts, with his own annotations.")

# 0004: Kepler assumiu a defesa (não "parou as pesquisas")
substituir(4, "gancho", "O astrônomo parou suas pesquisas para defendê-la, e ela foi absolvida",
    "O astrônomo assumiu pessoalmente a defesa, e ela foi absolvida")

# 0007: lido pelos grandes astrônomos, não "muito lido"
trocar(7, gancho="O livro de Copérnico ficou conhecido como \"o livro que ninguém leu\". Um historiador examinou por 35 "
    "anos os exemplares antigos: quase todos os grandes astrônomos da época o leram, mas ignoravam a parte do Sol "
    "no centro.")

# 0008: a exceção de Ibn al-Nafis; tipo contraintuitivo no lugar de mito_desmentido
substituir(8, "explicacao", "uma sucessão de "
    "anatomistas afirmou achá-las também. ",
    "uma sucessão de "
    "anatomistas afirmou achá-las também. Houve exceções: no século XIII, o médico árabe Ibn al-Nafis já negava a "
    "existência dessas passagens, mas o manuscrito em que fazia isso só foi encontrado em 1924, numa biblioteca de "
    "Berlim. ")
trocar(8, tipos_espanto=["historia_humana", "contraintuitivo"])
CANDIDATOS[7]["fontes"].append(wiki("Ibn_al-Nafis",
    "c. 1210/1211 - 1288/1289 CE), known as Ibn al-Nafīs [...] was an Arab polymath whose areas of work included medicine [...] "
    "But there is no passage between these cavities, for the substance of the heart is solid in this region and has neither a visible passage, as was thought by some persons, nor an invisible one which could have permitted the transmission of blood, as was alleged by Galen. [...] "
    "In 1924, Egyptian physician, Muhyo Al-Deen Altawi, discovered a manuscript entitled, Sharh tashrih al-qanun li’ Ibn Sina, or \"Commentary on Anatomy in Avicenna's Canon\" in the Prussian State Library in Berlin",
    nome="Ibn al-Nafis"))

# 0009: reescrita com o texto do próprio Harvey (contas por meia hora, comparadas ao sangue do corpo)
trocar(9,
    gancho="William Harvey derrubou Galeno com uma conta: mesmo usando estimativas baixas de propósito, o coração "
           "bombeava em meia hora mais sangue do que o corpo inteiro contém. O sangue só podia estar circulando.",
    explicacao=(
        "Em 1628, o médico inglês publicou De Motu Cordis, seu tratado sobre a circulação do sangue. A visão aceita, "
        "herdada de Galeno, era que o fígado produzia o sangue das veias. Harvey atacou essa ideia com aritmética, "
        "escolhendo de propósito números baixos. Supôs que o ventrículo esquerdo cheio guardasse duas onças, três ou "
        "uma onça e meia (num cadáver, ele achou mais de duas) e que a cada contração saísse só uma fração disso: um "
        "quarto, um quinto, um sexto ou até um oitavo. Em meia hora, o coração bate mais de mil vezes. Multiplicando, "
        "o sangue lançado na aorta passava, em qualquer das hipóteses, de todo o sangue contido no corpo. Repetiu a "
        "conta para a ovelha e o cão: mil escrúpulos em meia hora, umas três libras e meia, quando nenhum dos dois "
        "tem mais de quatro libras de sangue, o que ele próprio verificou na ovelha. Nenhuma alimentação repõe tanto: "
        "o sangue tinha de ir do coração às extremidades e voltar, num movimento circular. Harvey reforçou o "
        "argumento com ligaduras, inclusive no braço de um homem: com o garrote bem apertado, as artérias param de "
        "pulsar abaixo dele e incham acima. Ele sabia da ousadia e escreveu temer ter a humanidade inteira como "
        "inimiga. Depois do livro, sua clínica de fato encolheu."
    ),
    fontes=[
        {"url": "https://sourcebooks.web.fordham.edu/mod/harvey-blood.asp",
         "titulo": "William Harvey: On the Motion of the Heart and Blood in Animals, 1628 (Internet Modern History Sourcebook, Fordham University)",
         "idioma": "en",
         "trecho": (
            "Let us assume either arbitrarily or from experiment, the quantity of blood which the left ventricle of the heart will contain when distended, to be, say two ounces, three ounces, or one ounce and a half, in the dead body I have found it to hold upwards of two ounces. [...] "
            "let us suppose as approaching the truth that the fourth, or fifth, or sixth, or even but the eighth part of its charge is thrown into the artery at each contraction [...] "
            "Now in the course of half an hour, the heart will have made more than one thousand beats [...] "
            "Multiplying the number of drachms propelled by the number of pulses, we shall have either one thousand half ounces, or one thousand times three drachms, or a like proportional quantity of blood, according to the amount which we assume as propelled with each stroke of the heart, sent from this organ into the artery; "
            "a larger quantity in every case than is contained in the whole body! "
            "In the same way, in the sheep or dog, say that but a single scruple of blood passes with each stroke of the heart, in one half hour we should have one thousand scruples, or about three pounds and a half of blood injected into the aorta; "
            "but the body of neither animal contains above four pounds of blood, a fact which I have myself ascertained in the case of the sheep. [...] "
            "it is still manifest that more blood passes through the heart in consequence of its action, than can either be supplied by the whole of the ingesta [...] "
            "the blood circulates, revolves, propelled and then returning, from the heart to the extremities, from the extremities to the heart, and thus that it performs a kind of circular motion. [...] "
            "Now let anyone make an experiment upon the arm of a man [...] "
            "let a ligature be thrown about the extremity, and drawn as tightly as can be borne, it will first be perceived that beyond the ligature, neither in the wrist nor anywhere else, do the arteries pulsate, "
            "at the same time that immediately above the ligature the artery begins to rise higher at each diastole, to throb more violently, and to swell"
         )},
        wiki("William_Harvey",
            "In 1628 he published in Frankfurt his completed treatise on the circulation of the blood, the De Motu Cordis. "
            "As a result of negative comments by other physicians Harvey \"fell mightily in his practice\" [...] "
            "Coming into conflict with Galen's accepted view of the liver as the origin of venous blood [...] "
            "All of these estimates were purposefully low, so that people could see the vast amount of blood Galen's theory required the liver to produce. [...] "
            "I not only fear injury to myself from the envy of a few, but I tremble lest I have mankind at large for my enemies",
            nome="William Harvey"),
    ])

# 0010: Newton "viu ali um sinal"; os dois efeitos (rotação e achatamento) se somam
substituir(10, "gancho", "Newton concluiu daí que a Terra não é uma esfera: é mais larga no equador.",
    "Newton viu ali um sinal de que a Terra não é uma esfera, mas mais larga no equador.")
substituir(10, "explicacao", "Newton tirou a conclusão: se a gravidade",
    "Newton comentou depois: se a gravidade")
substituir(10, "explicacao", "Hoje se sabe que a gravidade varia cerca de 0,5% entre o equador e os polos, por causa do "
    "achatamento da Terra, e relógios",
    "Hoje se sabe que a gravidade varia cerca de 0,5% entre o equador e os polos por dois efeitos que se somam: a "
    "rotação, que reduz a gravidade aparente no equador, e o achatamento, que deixa o equador mais longe do centro. "
    "Huygens e Newton tinham, cada um, parte da razão. Relógios")
CANDIDATOS[9]["fontes"].append(wiki("Gravity_of_Earth",
    "At latitudes nearer the Equator, the outward centrifugal force produced by Earth's rotation is larger than at polar latitudes. "
    "This counteracts the Earth's gravity to a small degree [...] "
    "The second major reason for the difference in gravity at different latitudes is that the Earth's equatorial bulge (itself also caused by centrifugal force from rotation) causes objects at the Equator to be further from the planet's center than objects at the poles. [...] "
    "In combination, the equatorial bulge and the effects of the surface centrifugal force due to rotation mean that sea-level gravity increases from about 9.780 m/s2 at the Equator to about 9.832 m/s2 at the poles, so an object will weigh approximately 0.5% more at the poles than at the Equator.",
    nome="Gravity of Earth"))

# 0012: "muitas, ao menos em parte"; sem "Segundo a Wikipédia"; tipo conexao_inesperada
substituir(12, "gancho", "Quase todas já se realizaram.", "Muitas delas já se realizaram, ao menos em parte.")
substituir(12, "explicacao", "Segundo a Wikipédia, todas "
    "as 24 ideias, com poucas exceções, se tornaram realidade.",
    "Hoje, boa parte delas se tornou realidade, ao menos em parte, embora a conta dependa de como se interpreta "
    "cada item.")
trocar(12, tipos_espanto=["engenhosidade", "conexao_inesperada"])

# 0013: "um dos primeiros" livros com ilustrações ao microscópio
substituir(13, "explicacao", "e o "
    "primeiro livro com ilustrações de insetos e plantas vistos ao microscópio",
    "e um dos "
    "primeiros livros com ilustrações de insetos e plantas vistos ao microscópio")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(8, "explicacao", "só foi encontrado em 1924", "só foi redescoberto em 1924")
