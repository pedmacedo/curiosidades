"""Rodada 2 de Pré-história: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-17-pre_historia-01.py"))
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


def acrescentar_trecho(n, i_fonte, extra):
    CANDIDATOS[n - 1]["fontes"][i_fonte]["trecho"] += " [...] " + extra


# 0001: "mais de 17 mil anos"; frase de 1955 com palavras próprias
substituir(1, "gancho", "sobreviveram cerca de 17 mil anos no escuro", "sobreviveram mais de 17 mil anos no escuro")
substituir(1, "explicacao",
    "Em 1955, o gás carbônico, o calor, a umidade e outros contaminantes produzidos por 1.200 visitantes por dia já "
    "tinham danificado visivelmente as pinturas.",
    "Sete anos depois, em 1955, o estrago já se via a olho nu: cerca de 1.200 visitantes por dia enchiam as "
    "galerias de gás carbônico, calor e umidade.")

# 0003: sem Stonehenge; data dos pilares; debate sobre a mão de obra
trocar(3, gancho="Há mais de 11 mil anos, na Turquia, caçadores-coletores ergueram grandes pilares de pedra decorados, entre os megálitos mais antigos do mundo, antes mesmo de existir cerâmica na região.")
substituir(3, "explicacao",
    "As evidências indicam que seus habitantes eram caçadores-coletores, que completavam a dieta com formas "
    "iniciais de cereais domesticados e viviam em aldeias ao menos parte do ano.",
    "Quem o construiu vivia sobretudo da caça e da coleta, com algum reforço de cereais nas primeiras fases de "
    "domesticação, e passava ao menos parte do ano em aldeias.")
substituir(3, "explicacao",
    "Experimentos no local sugerem que as estruturas poderiam ter sido erguidas por 12 a 24 pessoas em menos de "
    "quatro meses.",
    "Quanto trabalho isso exigiu ainda é discutido: Klaus Schmidt imaginava centenas de pessoas, mas "
    "experimentos no local sugerem que as construções da fase mais recente já escavadas poderiam ter sido "
    "erguidas por 12 a 24 pessoas em menos de quatro meses.")
acrescentar_trecho(3, 0, "Radiocarbon dating shows that the earliest exposed structures at Göbekli Tepe were built between 9500 and 9000 BCE [...] "
    "Archaeologists disagree on how much labour was needed to construct the site. [...] "
    "he estimated that moving the pillars alone must have involved hundreds of people.")

# 0004: ~2% hoje; o dobro nos primeiros eurasiáticos; seleção como hipótese compatível
trocar(4, nota_surpresa=3,
       gancho="Quem tem ancestrais fora da África subsaariana carrega cerca de 2% de DNA neandertal. Os primeiros humanos modernos da Eurásia tinham o dobro ou mais: a seleção natural foi apagando parte dessa herança.")
substituir(4, "explicacao",
    "O sequenciamento de genomas revelou que todas as populações humanas atuais fora da África carregam "
    "aproximadamente de 1% a 4% de DNA neandertal.",
    "A leitura de genomas antigos e atuais mostrou que os povos de fora da África subsaariana guardam um pedaço "
    "do genoma neandertal: as primeiras estimativas, de 2010, iam de 1% a 4%, e as revisões mais recentes ficam "
    "em torno de 2%.")
substituir(4, "explicacao", "Ou seja, parte dessa herança foi eliminada pela seleção natural ao longo do tempo",
    "Isso é compatível com a ideia de que a seleção natural foi eliminando parte dessa herança ao longo do tempo")
acrescentar_trecho(4, 0, "In 2017, Prüfer et al. revised their estimate to 1.8–2.6% for non-Africans outside Oceania. [...] "
    "Reich states that all present-day non Sub-Saharan Africans have around 2% of Neanderthal ancestry.")

# 0005: "de que se tem certeza"; sem contar as flautas; texto próprio
trocar(5, nota_surpresa=3)
substituir(5, "gancho", "Os instrumentos musicais mais antigos conhecidos são flautas", "Os instrumentos musicais mais antigos de que se tem certeza são flautas")
substituir(5, "explicacao", "Entre eles estavam duas flautas, uma feita de osso de ave e outra de marfim de mamute.",
    "Entre eles havia flautas feitas de osso de ave e de marfim de mamute.")
substituir(5, "explicacao",
    "Com idade de 42 mil a 43 mil anos, são os instrumentos musicais mais antigos conhecidos. Não eram meros "
    "apitos: as flautas podiam tocar melodias distintas. Para os arqueólogos, isso sugere que a música "
    "provavelmente era parte importante da vida das sociedades que viviam na região naquela época, a dos "
    "primeiros humanos modernos na Europa.",
    "Datadas de 42 mil a 43 mil anos, são o registro seguro mais antigo de instrumentos musicais. E não eram "
    "simples apitos: davam para tocar melodias diferentes, sinal de que a música já fazia parte da vida dos "
    "primeiros humanos modernos que chegaram à Europa.")
substituir(5, "explicacao", " Fazer uma flauta de marfim, material maciço que precisa ser cortado, escavado e furado, exigia planejamento e técnica.", "")

# 0006: "grupo humano"; "provavelmente"; nome formal só até 2025
trocar(6, gancho="Um grupo humano foi descoberto pelo DNA de um ossinho de dedo. E os tibetanos provavelmente herdaram dele um gene que ajuda a viver nas alturas.")
substituir(6, "explicacao", "e por isso nem há um nome científico oficial para a espécie.",
    "e por isso, durante anos, não houve um nome científico formal para eles.")
substituir(6, "explicacao", "uma variante do gene EPAS1, vinda dos denisovanos,", "uma variante do gene EPAS1, provavelmente vinda dos denisovanos,")
substituir(6, "explicacao", "Análises de DNA e proteínas de um crânio achado em Harbin, na China, indicaram que ele também é denisovano.",
    "Análises de DNA e proteínas de um crânio achado em Harbin, na China, que já tinha recebido o nome Homo longi, "
    "indicaram que ele também é denisovano.")
acrescentar_trecho(6, 0, "A haplotype of EPAS1 in modern Tibetans, which allows them to live at high elevations in a low-oxygen environment, likely came from Denisovans. [...] "
    "which had been given the name Homo longi, showed that this skull represents a Denisovan.")

# 0007: o DNA foi de esqueletos de Lagoa Santa, não da própria Luzia
substituir(7, "explicacao",
    "Luzia era geneticamente ameríndia, sem ligação próxima com populações da África ou da Austrália.",
    "o DNA de esqueletos da mesma região, Lagoa Santa, mostrou que aquele povo era geneticamente ameríndio, sem "
    "ligação próxima com populações da África ou da Austrália.")
acrescentar_trecho(7, 0, "Lagoa Santa remains from a site nearby to the Luzia remains carry DNA regarded as Native American.")

# 0010: sem "quase o dobro"
substituir(10, "gancho", "quase o dobro da idade que se costumava dar à chegada dos humanos às Américas",
    "bem antes dos 13 mil a 16 mil anos que se costumava dar à chegada dos humanos às Américas")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(4, "gancho", "a seleção natural foi apagando parte dessa herança.", "a seleção natural pode ter apagado parte dessa herança.")
substituir(5, "explicacao",
    "sinal de que a música já fazia parte da vida dos primeiros humanos modernos que chegaram à Europa.",
    "o que sugere que a música já fazia parte da vida dos primeiros humanos modernos da região.")
substituir(6, "gancho", "herdaram dele um gene que ajuda", "herdaram dele uma versão de um gene que ajuda")
