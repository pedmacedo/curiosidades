"""Rodada 2 de Segunda Guerra Mundial: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-segunda_guerra-01.py"))
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


# 0002: a medalha foi concedida por lei em 2022; apresentar Ellsworth Kelly; nota 3
trocar(2, nota_surpresa=3)
substituir(2, "gancho", "como Ellsworth Kelly,", "como o artista Ellsworth Kelly,")
substituir(2, "explicacao", "e em 2022 os veteranos receberam a Medalha de Ouro do Congresso.",
    "e em 2022 uma lei concedeu à unidade a Medalha de Ouro do Congresso.")
acrescentar_trecho(2, 0, "U.S. president Joe Biden signed into law S. 1404, the Ghost Army Congressional Gold Medal Act, which provides for the award of a Congressional Gold Medal to the Ghost Army")

# 0003: três lentes e telas; sem causalidade no gancho; motivo oficial do cancelamento
substituir(3, "gancho", "Os militares acharam a ideia excêntrica e a cancelaram;",
    "Os militares a acharam excêntrica, e ela foi cancelada;")
substituir(3, "explicacao",
    "uma lente no nariz da bomba projetava a imagem do alvo numa tela, e o pombo, treinado para reconhecê-lo, bicava a imagem.",
    "três lentes no nariz da bomba projetavam a imagem do alvo em telas, e cada pombo, treinado para reconhecê-lo, bicava a imagem na sua.")
substituir(3, "explicacao", "Foi cancelado em outubro de 1944,",
    "Foi cancelado em outubro de 1944, sob o argumento de que atrasaria projetos mais promissores,")
acrescentar_trecho(3, 0, "because the military believed that \"further prosecution of this project would seriously delay others which in the minds of the Division have more immediate promise of combat application.\"")

# 0004: velocidade máxima "parecida" com a de estol (fonte Polikarpov Po-2); unidades femininas; nota 3
trocar(4, nota_surpresa=3,
    gancho="As \"Bruxas da Noite\", aviadoras soviéticas, atacavam em biplanos de treino projetados em 1928, cuja "
           "velocidade máxima era parecida com a velocidade de estol dos caças alemães. Isso os tornava difíceis de abater.")
substituir(4, "explicacao", "formar unidades de combate só de mulheres", "formar unidades de combate femininas")
substituir(4, "explicacao",
    "sua velocidade máxima era menor que a velocidade de estol dos caças alemães Bf 109 e Fw 190, o que tornava o U-2 muito difícil de abater para os pilotos alemães.",
    "sua velocidade máxima era parecida com a velocidade de estol dos caças alemães Bf 109 e Fw 190, o que tornava o U-2 muito difícil de abater para os pilotos alemães.")
substituir_trecho(4, 0,
    "the pilots took advantage of its exceptional maneuverability; it also had a maximum speed that was lower than the stalling speed of both the Messerschmitt Bf 109 and the Focke-Wulf Fw 190, which made it very difficult for German pilots to shoot down",
    "the pilots took advantage of its exceptional maneuverability")
CANDIDATOS[3]["fontes"].append(wiki("Polikarpov_Po-2",
    "affe fighters found it extremely hard to shoot down the Kukuruznik because of two main factors: the pilots flew at treetop level where they were hard to see or engage and "
    "the stall speed of both the Messerschmitt Bf 109 and the Focke-Wulf Fw 190 was similar to the U-2s maximum speed, making it difficult for the fighters to keep a Po-2 in weapons ra",
    nome="Polikarpov Po-2"))

# 0005: o isolamento (rádio cortado), não resistência; sem a frase sobre o clima da Europa
trocar(5, gancho="A última tropa alemã a se render na Segunda Guerra foi uma equipe de meteorologia em Svalbard, no Ártico. "
                 "Souberam da rendição em maio de 1945, mas, isolados, só se entregaram em setembro, a caçadores de focas.")
substituir(5, "explicacao",
    "Na guerra, a previsão do tempo era informação estratégica, e boa parte do clima da Europa se forma no Atlântico Norte e no Ártico. Por isso, os dois lados disputaram estações meteorológicas em lugares remotos.",
    "Na guerra, a previsão do tempo era informação estratégica, e por isso os dois lados disputaram estações meteorológicas em lugares remotos do Ártico.")

# 0009: o cerco acabou em janeiro de 1944 (sem "primavera"); frase sobre Lysenko
substituir(9, "explicacao", "Vários guardiões morreram de fome antes do fim do cerco, na primavera de 1944.",
    "Vários guardiões morreram de fome antes do fim do cerco.")
substituir(9, "explicacao", "depois de se opor às ideias de Lysenko, que rejeitava a genética e agradavam a Stálin,",
    "depois de se opor a Lysenko, que rejeitava a genética e tinha o apoio de Stálin,")
substituir_trecho(9, 1,
    "Those guarding the seedbank refused to eat its contents, even though by the end of the siege in the spring of 1944, a number of them had died of starvation.",
    "Those guarding the seedbank refused to eat its contents, even though by the end of the siege [...] a number of them had died of starvation.")

# 0010: o pykrete já tinha sido descrito por Mark e Hohenstein
substituir(10, "explicacao", "O material criado para o projeto, o pykrete, batizado em homenagem a Pyke, era mais resistente",
    "O material adotado, o pykrete, já descrito antes por dois pesquisadores no Brooklyn e batizado em homenagem a Pyke, era mais resistente")
acrescentar_trecho(10, 0, "as the material was originally described in a paper by Mark and Hohenstein in Brooklyn.")

# 0011: sem a frase da gravação/papel (era sobre os dólares); quem foi escolhido
substituir(11, "explicacao",
    " A gravação e a impressão eram consideradas excelentes, embora o papel fosse inferior ao verdadeiro.", "")
substituir_trecho(11, 0,
    "The standard of engraving and printing was considered excellent, although the paper used was technically inferior to the genuine notes. [...] ", "")
substituir(11, "explicacao",
    "reuniu no campo de Sachsenhausen presos judeus escolhidos em vários campos de concentração,",
    "reuniu no campo de Sachsenhausen presos de vários campos de concentração, em grande parte judeus, escolhidos por saberem desenhar, gravar, imprimir ou lidar com bancos,")
substituir_trecho(11, 0, "Krüger visited several other concentration camps to assemble the peop[...] ",
    "Krüger visited several other concentration camps to assemble the people he needed, primarily selecting those with skills in draftsmanship, engraving, printing and banking. [...] ")
acrescentar_trecho(11, 0, "The Jewish prisoners working on the operation at the time complained to Krüger at having to work with a criminal")

# 0012: o convite de Włodarkiewicz e as duas versões da prisão
substituir(12, "explicacao",
    "Há duas versões sobre como foi parar no campo: numa, deixou-se capturar numa batida alemã em Varsóvia justamente para se infiltrar; por isso muitas fontes dizem que ele se ofereceu como voluntário.",
    "A missão lhe foi apresentada pelo chefe de seu grupo clandestino como um convite. Pilecki a encarou como castigo por ter discordado dele, mas aceitou, e por isso muitas fontes o descrevem como voluntário. Há duas versões de como foi preso, ambas de propósito: numa batida de rua em Varsóvia ou numa revista de prédio, no apartamento de uma conhecida.")
acrescentar_trecho(12, 0,
    "Włodarkiewicz said it was not an order but an invitation to volunteer, though Pilecki saw it as a punishment for refusing to back Włodarkiewicz's ideology. "
    "Nevertheless, he agreed [...] "
    "In the second version, he did that in the apartment of Eleonora Ostrowska, at ulica Wojska Polskiego (Polish Army Street) during a building search.")

# 0013: os 99% são dos judeus da Dinamarca, não dos deportados
substituir(13, "explicacao", "e a pressão dinamarquesa em favor deles ajudou a garantir a sobrevivência de 99%.",
    "e a pressão dinamarquesa em favor deles, somada à fuga, fez com que 99% dos judeus da Dinamarca sobrevivessem ao Holocausto.")

# 0014: redação
substituir(14, "explicacao",
    "É um dos dois casos conhecidos de americanos e alemães lutando lado a lado na guerra, dois dias antes da rendição alemã.",
    "É um dos dois casos conhecidos de americanos e alemães lutando lado a lado na guerra, e aconteceu só dois dias antes da rendição incondicional da Alemanha.")
substituir(14, "explicacao", "Um oficial da SS que os presos tinham feito amigo também ajudou na defesa.",
    "Um oficial da SS de quem os presos tinham ficado amigos também ajudou na defesa.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(2, "gancho", "Muitos eram artistas, como o artista Ellsworth Kelly,", "Muitos eram artistas, entre eles Ellsworth Kelly,")
substituir(4, "gancho", "cuja velocidade máxima era parecida com a velocidade de estol dos caças alemães. Isso os tornava difíceis de abater.",
    "cuja velocidade máxima era parecida com a de estol dos caças alemães. Isso ajudava a torná-los difíceis de abater.")
substituir(4, "explicacao", "o que tornava o U-2 muito difícil de abater para os pilotos alemães",
    "o que, somado ao voo rente às copas das árvores, tornava o U-2 muito difícil de abater para os pilotos alemães")
acrescentar_trecho(4, 1, "the pilots flew at treetop level where they were hard to see or engage")
