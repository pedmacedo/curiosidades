"""Rodada 2 de Paleontologia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-paleontologia-01.py"))
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


# 0002: Leidy já tinha visto o erro; "recolher" os exemplares; o desafio do cérebro como versão mais contada;
# o corpo doado à ciência; tipos sem escala_absurda
trocar(2, tipos_espanto=["historia_humana", "contraintuitivo"])
substituir(2, "gancho", "destruição de fósseis contra o rival.", "destruição de fósseis.")
substituir(2, "gancho", "Um deles deixou o próprio crânio para a ciência, esperando provar que tinha o cérebro maior.",
    "Um deles deixou o corpo para a ciência e, diz a história mais contada, queria provar que tinha o cérebro maior.")
substituir(2, "explicacao",
    "e humilhou o rival ao apontar que Cope montara o réptil marinho Elasmosaurus com a cabeça na ponta da cauda",
    "e humilhou o rival espalhando que Cope montara o réptil marinho Elasmosaurus com a cabeça na ponta da cauda "
    "(Joseph Leidy já tinha notado o erro em 1870)")
substituir(2, "explicacao", "Cope tentou comprar todos os exemplares da revista com o erro",
    "Cope tentou recolher todos os exemplares do artigo com o erro")
substituir(2, "explicacao",
    "Cope lançou um último desafio: doou o crânio à ciência para que o cérebro fosse medido, esperando que superasse o de Marsh",
    "Segundo a versão mais difundida, Cope lançou um último desafio: doou o corpo à ciência para que o cérebro "
    "fosse medido, esperando que superasse o de Marsh")
acrescentar_trecho(2, 0, "(although Leidy had already pointed out this error shortly after the initial description of the taxon, in 1870)")
CANDIDATOS[1]["fontes"].append(wiki("Edward_Drinker_Cope",
    "Cope was horrified since he had already published a paper on the fossil with the error at the American Philosophical Society. "
    "He immediately tried to buy back the copies [...] "
    "Cope insisted through his will that no graveside service or burial be held; he had donated his body to science. "
    "He issued a final challenge to Marsh at his death: he had his skull donated to science so his brain could be measured, hoping his brain would be larger than that of his adversary;",
    nome="Edward Drinker Cope"))

# 0004: quem descreveu foi Stromer; quem achou foi Markgraf
substituir(4, "gancho", "por tensões entre o descobridor e o diretor do museu, um nazista fervoroso",
    "por tensões entre o paleontólogo que o descreveu e o diretor do museu, um nazista fervoroso")

# 0007: a fama de "fóssil vivo" é discutida, não derrubada; tipos sem mito_desmentido
trocar(7, tipos_espanto=["historia_humana", "escala_absurda"], nota_surpresa=3)
substituir(7, "explicacao",
    "Estudos recentes contestam: os celacantos fósseis tiveram formas e modos de vida bem mais variados do que se "
    "pensava, e a ideia de que o grupo quase não mudou seria uma crença sem base em dados.",
    "Essa fama é discutida: estudos recentes mostram que os celacantos fósseis tiveram formas e modos de vida bem "
    "mais variados do que se pensava, e alguns pesquisadores consideram uma crença sem base em dados a ideia de que "
    "o grupo quase não mudou.")

# 0009: lente dupla como interpretação; sem o ofiúro; consenso_parcial
trocar(9, confianca="consenso_parcial")
substituir(9, "gancho",
    "Em alguns, a lente era dupla e corrigia distorções seguindo princípios de óptica que só seriam descritos no século XVII.",
    "Em alguns, a lente parece ter sido dupla, reduzindo distorções por princípios de óptica que só seriam descritos no século XVII.")
substituir(9, "explicacao", "a calcita formava por dentro uma estrutura dupla",
    "a calcita parece ter formado por dentro uma estrutura dupla")
substituir(9, "explicacao", " Um animal vivo com lentes parecidas é o ofiúro Ophiocoma wendtii.", "")
substituir_trecho(9, 0, "A living species with similar lenses is the brittle star Ophiocoma wendtii. ", "[...] ")

# 0010: o rio Luján não fica no norte da Argentina
trocar(10, nota_surpresa=3)
substituir(10, "explicacao", "às margens do rio Luján, no atual norte da Argentina.",
    "às margens do rio Luján, na atual Argentina.")

# 0011: a saída em 2006 não está confirmada; o nome nunca foi válido
substituir(11, "gancho", "perdeu o nome científico", "ficou sem nome científico válido")
substituir(11, "explicacao", "o tinha comprado com a documentação necessária",
    "o tinha comprado em 1995, com a documentação necessária")
substituir(11, "explicacao",
    "Uma investigação confirmou que o fóssil saiu do Brasil em 2006 e não encontrou licença válida de exportação.",
    "A investigação derrubou essa versão: o museu só o comprou em 2009, o fóssil teria saído do Brasil em 2006, "
    "e nenhuma licença válida de exportação foi encontrada.")

# 0014: a frase de Holtz no contexto certo
substituir(14, "explicacao",
    "Um paleontólogo comentou que ninguém \"em sã consciência\" faria o que ela fez: destruir em ácido um fóssil tão trabalhoso de desenterrar.",
    "Um paleontólogo explicou por que ninguém tinha visto isso antes: nenhum colega sensato destruiria em ácido um "
    "fóssil tão trabalhoso de desenterrar. E concluiu que aquilo era ótima ciência.")
acrescentar_trecho(14, 0, "“It’s great science.”")
