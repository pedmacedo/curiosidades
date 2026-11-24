"""Rodada 2 de Experimentos de psicologia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-experimentos_psicologia-01.py"))
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


# 0001: a "outra metade" econômica vem só do resumo; os controles reduziram ainda mais o efeito
substituir(1, "gancho",
    "Refeito em 2018 com amostra dez vezes maior, achou só metade do efeito; a origem econômica parecia explicar a outra metade.",
    "Refeito em 2018 com amostra dez vezes maior, achou metade do efeito, que encolheu ainda mais ao considerar a família.")
substituir_trecho(1, 0,
    "The replication suggested that economic background, rather than willpower, explained the other half. [...] ",
    "[...] ")

# 0004: o medo não foi forte nem duradouro; "um dia de diferença" de quem
substituir(4, "explicacao",
    "um coelho, um cachorro e um casaco de pele. ",
    "um coelho, um cachorro e um casaco de pele. O próprio Watson admitiu que o medo não foi forte nem duradouro, "
    "e uma releitura de 1979 achou pouca evidência de uma fobia de verdade. ")
substituir(4, "explicacao",
    "que nasceu com um dia de diferença e deixou o hospital",
    "que nasceu com um dia de diferença de Merritte e deixou o hospital")
acrescentar_trecho(4, 0,
    "However, he admitted in his research article that the fear he generated was neither strong nor lasting. [...] "
    "A detailed review of the original study and its subsequent interpretations by Ben Harris (1979) stated: [...] "
    "Critical reading of Watson and Rayner's (1920) report reveals little evidence either that Albert developed a rat phobia "
    "or even that animals consistently evoked his fear (or anxiety) during Watson and Rayner's experiment.")

# 0005: sem os 24,8 pontos; "mais de duas semanas"
substituir(5, "explicacao",
    "Rosenthal chegou a afirmar ganhos de 24,8 pontos acima dos do grupo de controle. ",
    "Rosenthal chegou a falar em ganhos grandes e duradouros. ")
substituir(5, "explicacao",
    "quando os professores já conheciam os alunos havia duas semanas",
    "quando os professores já conheciam os alunos havia mais de duas semanas")
substituir_trecho(5, 0,
    "Rosenthal had originally claimed the treatment group's IQ gain over time was \"24.8 IQ points in excess of the gain shown by the controls,\" and that these gains were persistent and widespread, but several studies",
    "and that these gains were persistent and widespread, but several studies")

# 0006: o conselho tradicional era evitar o colo para não mimar; Bowlby discordava
substituir(6, "gancho",
    "Na época, achava-se que o contato físico fazia mal aos bebês.",
    "Na época, aconselhava-se evitar o colo para não mimar bebês.")
substituir(6, "explicacao",
    "o contato físico com bebês era considerado prejudicial ao desenvolvimento, e essa visão levou a berçários esterilizados e sem contato pelo país.",
    "o conselho tradicional era limitar o contato físico com bebês para não mimá-los, e havia quem o considerasse "
    "prejudicial ao desenvolvimento, visão que levou a berçários esterilizados e sem contato nos EUA; John Bowlby discordava.")
acrescentar_trecho(6, 0,
    "they contradicted both the traditional pedagogic advice of limiting or avoiding bodily contact in an attempt to avoid spoiling children [...] "
    "B. F. Skinner and the behaviorists took on John Bowlby in a discussion of the mother's importance in the development of the child [...] "
    "Bowlby disagreed, claiming that the mother provides much more than food to the infant")

# 0007: uma única replicação, em 1996
substituir(7, "gancho", "mas não se confirmou ao ser refeito.", "mas falhou ao ser refeito em 1996.")

# 0008: os 41 impostores só existem no relato de Rosenhan; distorções "aparentes"
trocar(8, gancho="Após Rosenhan relatar que falsos pacientes enganaram 12 hospitais psiquiátricos, um hospital duvidou. "
    "Segundo ele, a equipe apontou 41 impostores em três meses, mas ele não tinha mandado nenhum.")
substituir(8, "explicacao", "Dos 193 pacientes que chegaram", "Segundo o relato, dos 193 pacientes que chegaram")
substituir(8, "explicacao",
    "relatou dados inconsistentes e citações imprecisas ou inventadas",
    "apontou aparentes distorções, como dados inconsistentes e citações imprecisas ou inventadas")

# 0009: "chance de imitar"; a leitura é do estudo
substituir(9, "explicacao",
    "imitaram a agressão até cinco vezes mais do que as que já conheciam o brinquedo",
    "tinham até cinco vezes mais chance de imitar a agressão do que as que já conheciam o brinquedo")
substituir(9, "explicacao", "A leitura de Bandura:", "A leitura do estudo:")

# 0010: o que falhou em 2024 foi uma variante, e a hipótese da escolha
trocar(10, gancho="Em 1959, quem ganhou 1 dólar para dizer que uma tarefa chata era divertida passou a gostar mais dela "
    "que quem ganhou 20. Em 2024, 39 laboratórios refizeram uma variante desse tipo de teste, e a previsão central falhou.")

# 0011: o gancho e a biologia do câncer (opção preferida: apagar a frase e o trecho)
trocar(11, gancho="Em 2015, cientistas refizeram 100 estudos de três das principais revistas de psicologia. Dos 97 que "
    "tinham achado um efeito, só 36% o acharam de novo, e no geral os efeitos medidos caíram à metade.")
substituir(11, "explicacao",
    " De fato, em 2021 a versão do projeto para biologia do câncer só conseguiu repetir 50 de 193 experimentos de 53 artigos de destaque, "
    "e os efeitos encontrados foram, em média, 85% menores que os originais.",
    "")
substituir_trecho(11, 0,
    "In 2021, the project showed that of 193 experiments from 53 top papers about cancer published between 2010 and 2012, only 50 experiments from 23 papers could be replicated. "
    "Moreover, it showed that the effect sizes of that fraction were 85% smaller on average than the original findings. [...] ",
    "")

# 0012: Brevia é uma seção da Science
substituir(12, "explicacao",
    "a Science Brevia e a Psychological Science",
    "a seção Brevia da revista Science e a Psychological Science")

# 0004: enxugar para caber em 250 palavras
substituir(4, "explicacao", "Albert brincava com o rato sem medo nenhum. Então, cada vez", "Albert brincava com o rato sem medo. Cada vez")

# 0014: grafia
substituir(14, "explicacao", "se deitava e ganía", "se deitava e gania")
