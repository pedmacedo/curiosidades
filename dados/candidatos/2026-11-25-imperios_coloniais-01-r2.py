"""Rodada 2 de Impérios coloniais: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-imperios_coloniais-01.py"))
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


# 0001: "mais de 150" navios; "Na VOC" no lugar do "Nela" ambíguo
substituir(1, "explicacao", "mantinha cerca de 150 navios mercantes", "mantinha mais de 150 navios mercantes")
substituir(1, "gancho", "Nela, o capital ficava preso", "Na VOC, o capital ficava preso")

# 0003: gancho diz o que ele descobriu; Morel não foi o primeiro a denunciar, trouxe os números
trocar(3, gancho="Um funcionário de uma companhia de navegação de Liverpool percebeu o trabalho forçado no Congo de "
    "Leopoldo II pelas cargas: os navios voltavam com borracha e marfim e iam com armas, correntes e explosivos.")
substituir(3, "explicacao", "o que saía do Congo valia cinco vezes o que entrava.",
    "o que saía do Congo valia cinco vezes o que entrava. Denúncias já circulavam havia uma década, desde o "
    "americano George Washington Williams, mas faltavam números; Morel trouxe os dados do comércio.")
acrescentar_trecho(3, 0, "In 1900, Morel put new life into the campaign against Congo misrule (begun a decade before by the American George Washington Williams) "
    "with a series of articles detailing his discoveries about the Congo Free State trade imbalances.")

# 0005: a ocupação efetiva valia para o litoral e bastava uma base costeira
substituir(5, "explicacao",
    "e estabeleceu o princípio da ocupação efetiva: para ter uma colônia reconhecida, uma potência precisava "
    "exercer autoridade real no território.",
    "e fixou o princípio da ocupação efetiva: para ter reconhecida uma posse no litoral africano, a potência "
    "precisava notificar as demais e mostrar presença ali. Na versão final, bastava uma base costeira, sem "
    "controle real do interior.")
acrescentar_trecho(5, 0, "agreed on a common framework for the recognition of European ''effective occupation'' of African coastal territory [...] "
    "any power attempting to take possession of or assume a protectorate over any territory within the African continent would be required to notify the other signatory powers before the possession or colony could be officially recognised. [...] "
    "the powers ultimately agreed that effective occupation could be established by a European state setting up a coastal base, from which it could expand into the interior. "
    "The conference participants did not view the rules of occupation as requiring full European hegemony on the ground.")

# 0007: o exército estava "em grande parte" armado com fuzis modernos
substituir(7, "explicacao", "armado com fuzis modernos comprados da França e da Rússia",
    "em grande parte armado com fuzis modernos comprados da França e da Rússia")

# 0009: gancho com a ironia explícita
trocar(9, gancho="Depois de denunciar os campos de concentração britânicos na Guerra dos Bôeres, a inglesa Emily Hobhouse "
    "foi impedida de desembarcar na África do Sul. Hoje, suas cinzas estão lá, num monumento, e ela é vista como heroína.")
trocar(9, nota_surpresa=3)

# 0010: em 1869 o governo mandou ligar os trechos
substituir(10, "explicacao", "Em 1869, ela foi ligada de ponta a ponta, do Himalaia até perto da baía de Bengala",
    "Em 1869, o governo mandou ligá-la de ponta a ponta, do Himalaia até perto da baía de Bengala")

# 0011: "um quinto do dinheiro em circulação", faixa de estimativas e "um dos fatores"
trocar(11, gancho="No fim do século XVII, a Escócia apostou cerca de um quinto do dinheiro que circulava no país numa colônia "
    "no Panamá. O fracasso arruinou o país e ajudou a enfraquecer a resistência à união com a Inglaterra, em 1707.")
substituir(11, "explicacao", "400 mil libras em poucas semanas, de gente de todas as classes",
    "400 mil libras em poucas semanas, de gente de todas as classes (as estimativas da fatia do capital escocês "
    "envolvida vão de 15% a 40%)")
substituir(11, "explicacao", "O Ato de União previu",
    "Historiadores apontam o desastre como um dos fatores que levaram a elite escocesa a aceitar a união. O Ato de União previu")
acrescentar_trecho(11, 0, "An estimated 15–40% of all the actual capital in Scotland was invested in this project.")

# 0012: sem a Austrália; o projeto com o papa era de colonizar os "mares do Sul" (NDB)
substituir(12, "gancho", " O duque chegou a propor ao papa conquistar terras na Austrália.",
    " O duque chegou a negociar com o papa um plano de colonizar os \"mares do Sul\".")
substituir(12, "explicacao",
    "No mesmo período, ofereceu ao papa Inocêncio X 40 navios de guerra e 24 mil homens para conquistar terras "
    "na Austrália, com o papa entrando com o dinheiro. O plano morreu com o papa, em 1655.",
    "Chegou ainda a negociar com o papa Inocêncio X um projeto de colonização nos \"mares do Sul\", abandonado "
    "com a morte do papa, em 1655.")
substituir_trecho(12, 0,
    "In 1651, the duke contacted Pope Innocent X with an offer of 40 Men-of-wars and 24,000 soldiers and sailors to conquer land in Australia. "
    "Courland would receive the commercial profits of the venture, while the Pope would provide the necessary monetary backing [...] ",
    "")
CANDIDATOS[11]["fontes"].append({
    "url": "https://www.deutsche-biographie.de/ppn118775812.html",
    "titulo": "Jakob Kettler (Deutsche Biographie)",
    "idioma": "de",
    "trecho": "Mit dem Papst wurde ein Projekt zur Südseekolonisation verhandelt.",
})

# 0014: "estopim" (primary catalyst); 3 de junho em Taiwan no lugar do 26 de junho
trocar(14, gancho="Em 1839, o mandarim Lin Zexu escreveu à rainha Vitória pedindo o fim do tráfico de ópio, destruiu 1,2 "
    "milhão de kg da droga e pediu perdão aos deuses do mar por poluí-lo. Foi o estopim da Guerra do Ópio.")
substituir(14, "explicacao",
    "Hoje é visto na China como herói da luta contra as drogas, e o Dia Internacional contra o Abuso e o Tráfico "
    "de Drogas, 26 de junho, homenageia o seu trabalho.",
    "Hoje é visto na China como herói da luta contra as drogas, e em Taiwan o 3 de junho, dia em que começou a "
    "destruição, é lembrado informalmente como Dia do Movimento de Supressão do Ópio.")
substituir_trecho(14, 0,
    "June 26 is recognized as the International Day against Drug Abuse and Illicit Trafficking in honour of Lin's work.",
    "June 3—the day when Lin confiscated the chests of opium—is unofficially celebrated as Opium Suppression Movement Day in Taiwan")

# 0015: C. ledgeriana é hoje sinônimo de C. calisaya
substituir(15, "explicacao",
    "Ali, a nova espécie, batizada Cinchona ledgeriana, rendeu de 8% a 13% de quinino na casca",
    "Ali, a planta, batizada Cinchona ledgeriana (hoje vista como uma forma da espécie C. calisaya), rendeu de "
    "8% a 13% de quinino na casca")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(11, "gancho", "O fracasso arruinou o país e ajudou", "O fracasso foi ruinoso e ajudou")
