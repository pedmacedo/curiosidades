"""Rodada 2 de Alimentos perigosos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-alimentos_perigosos-01.py"))
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


# 0001: a origem bacteriana é a explicação mais aceita, ainda debatida
substituir(1, "gancho",
    "não é feito pelo peixe: vem de bactérias que entram pela cadeia alimentar. Criado longe delas, o baiacu fica sem veneno.",
    "não é feito pelo peixe: vem da comida, e as principais suspeitas são bactérias. Criado longe delas, o baiacu fica sem veneno.")
substituir(1, "explicacao",
    "Pesquisadores concluíram que o peixe não fabrica a toxina. Ele a acumula ao comer outros animais contaminados por bactérias, como "
    "espécies de Vibrio e Shewanella,",
    "Pesquisadores concluíram que o peixe não fabrica a toxina. Ele a acumula ao comer outros animais, e a explicação mais aceita é "
    "que ela venha de bactérias, como espécies de Vibrio e Shewanella,")

# 0002: tipo de espanto
trocar(2, tipos_espanto=["engenhosidade", "contraintuitivo"])

# 0003: prática, não regra; o papel das sementes vem de um estudo
substituir(3, "gancho", "só pode ser colhido depois de se abrir sozinho na árvore",
    "só é colhido depois de se abrir sozinho na árvore")
substituir(3, "gancho", "Ao amadurecer, as sementes ajudam a tirar o veneno da polpa.",
    "Ao amadurecer, as sementes parecem ajudar a tirar o veneno da polpa.")
substituir(3, "explicacao", "Em 2011, descobriu-se uma parte do porquê:", "Um estudo de 2011 sugeriu uma parte do porquê:")

# 0004: os surtos diminuíam; a recomendação "pode ter ajudado"
substituir(4, "explicacao", "e sumiam semanas depois, com as chuvas da monção",
    "e diminuíam semanas depois, com as chuvas da monção")
substituir(4, "explicacao",
    "em 2014, com a recomendação de medir e corrigir a glicose logo na chegada, a mortalidade caiu para 31%.",
    "em 2014, a mortalidade caiu para 31%, e o CDC acha que a recomendação de medir e corrigir a glicose logo na chegada "
    "pode ter ajudado.")

# 0005: "podem dar sintomas"; surtos "associados" às panelas lentas
trocar(5, gancho="Feijão-vermelho cru faz mal: quatro ou cinco grãos já podem dar náusea e vômitos, e panelas elétricas de "
    "cozimento lento já foram ligadas a surtos. A proteína culpada virou ferramenta de laboratório.")
acrescentar_trecho(5, 0, "Several outbreaks have been associated with beans cooked in slow cookers")

# 0006: intoxicações graves são raras; data do surto da escola
substituir(6, "explicacao",
    "Intoxicações são raras, mas acontecem: em 1979, 78 alunos de um internato no Reino Unido",
    "Intoxicações graves são raras, mas acontecem: no fim da década de 1970, 78 alunos de uma escola no Reino Unido")
acrescentar_trecho(6, 0, "Though fatalities from solanine poisoning are rare, there have been several notable cases of human solanine poisonings.")

# 0007: sem a redistribuição na Segunda Guerra; casos graves mal documentados
trocar(7, gancho="Na Primeira Guerra Mundial, as folhas do ruibarbo, que são tóxicas, foram recomendadas por engano como "
    "alimento na Grã-Bretanha, e houve intoxicações. Da planta, só o talo é comestível.",
    temas_secundarios=["primeira_guerra", "plantas", "ciencia_cozinha"])
substituir(7, "explicacao",
    " Na Segunda Guerra, o material impresso com o conselho foi redescoberto e distribuído de novo, "
    "e houve mais mortes.", "")
substituir(7, "explicacao",
    "Os casos sérios vieram do consumo em grande quantidade e por muito tempo, como numa dieta de guerra.",
    "Os casos graves, aliás, são mal documentados e parecem ter vindo do consumo em grande quantidade e por muito tempo, "
    "como numa dieta de guerra.")
acrescentar_trecho(7, 0, "Serious cases of rhubarb poisoning are not well documented.")

# 0008: "pode correr mais risco"
substituir(8, "explicacao", "e quem já reagiu ao urushiol corre mais risco", "e quem já reagiu ao urushiol pode correr mais risco")

# 0009: data do episódio; não é mito desmentido
substituir(9, "gancho", "Em 401 a.C., soldados gregos", "No fim do século V a.C., soldados gregos")
trocar(9, tipos_espanto=["historia_humana", "conexao_inesperada"])

# 0010: favismo no Mediterrâneo; duas explicações; soldados na Coreia
substituir(10, "explicacao", "A condição é comum na bacia do Mediterrâneo", "O favismo é mais comum na bacia do Mediterrâneo")
substituir(10, "explicacao",
    "O motivo provável é a malária: o parasita é muito sensível a danos oxidativos, e células infectadas parecem ser "
    "eliminadas mais depressa pelo baço",
    "O motivo provável é a malária. Há duas explicações propostas: o parasita é muito sensível a danos oxidativos, e as "
    "células infectadas podem ser eliminadas mais depressa pelo baço")
substituir(10, "explicacao", "e muitos soldados de origem mediterrânea e norte-africana tiveram anemia",
    "e muitos soldados tiveram anemia")

# 0011: datas; quais predadores
substituir(11, "gancho", "Em 1913, a mesma causa virou a suspeita principal de uma morte na Antártida.",
    "É também a suspeita principal da morte de um explorador na Antártida, em 1913.")
substituir(11, "explicacao", "Em 1913, na Antártida, o suíço Xavier Mertz e Douglas Mawson perderam o companheiro Belgrave Ninnis",
    "Na Antártida, o suíço Xavier Mertz e Douglas Mawson perderam o companheiro Belgrave Ninnis")
substituir(11, "explicacao", "Mertz morreu no caminho.", "Mertz morreu no caminho, em janeiro de 1913.")
substituir(11, "explicacao", "Esses predadores chegam a ter",
    "Alguns predadores do Ártico, como o urso-polar e a foca-barbuda, chegam a ter")

# 0012: gancho diz o que é o chícharo; sem "não afeta a inteligência"
trocar(12, gancho="O chícharo, uma leguminosa, dá colheita quando as outras falham. Mas, se vira a base da dieta por meses, "
    "pode paralisar as pernas para sempre. Goya gravou essa tragédia na Espanha de Napoleão.")
substituir(12, "explicacao", "A paralisia é irreversível, mas não afeta a inteligência nem encurta a vida.",
    "A paralisia é irreversível, mas não encurta a vida.")

# 0013: "enfeitiçadas", não "possuídas"
substituir(13, "gancho", "as \"possuídas\" de Salem", "as \"enfeitiçadas\" de Salem")

# 0009: gancho dentro do limite de 220 caracteres depois da troca da data
substituir(9, "gancho", "soldados gregos comeram favos de mel perto do mar Negro e caíram no chão como se",
    "soldados gregos comeram favos perto do mar Negro e caíram como se")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(1, "explicacao", "como espécies de Vibrio e Shewanella, e com o tempo fica insensível a ela.", "como espécies de Vibrio e Shewanella; com o tempo, o peixe fica insensível a ela.")
substituir(11, "gancho", "passando mal, já em 1597. É também a suspeita principal", "passando mal em 1597. Esse excesso é a suspeita principal")
substituir(13, "explicacao", "No ano seguinte, os pesquisadores Nicholas Spanos e Jack Gottlieb", "Menos de um ano depois, os pesquisadores Nicholas Spanos e Jack Gottlieb")
