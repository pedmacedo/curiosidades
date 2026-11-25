"""Rodada 2 de Cidades: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-cidades-01.py"))
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


# 0002: aquedutos sem o número onze; gancho novo (o Fórum sobre o pântano aterrado)
trocar(2, gancho="O Fórum Romano, coração da Roma antiga, foi erguido sobre um pântano aterrado e drenado pela Cloaca "
                 "Máxima, um dos esgotos mais antigos do mundo. Ela ainda escoa a água da chuva do centro de Roma.")
substituir(2, "explicacao",
    "No século I d.C., os onze aquedutos que abasteciam a cidade desaguavam nela depois de passar por termas, fontes e casas",
    "Com o tempo, a água dos aquedutos que abasteciam a cidade passou a desaguar nela, depois de correr por termas, fontes e casas")

# 0003: tese militar debatida, não desmentida; a negação de Haussmann vale para os trechos que ele acrescentou
trocar(3, tipos_espanto=["contraintuitivo", "historia_humana"])
substituir(3, "gancho", "Haussmann usou esse argumento para tirar verba do Estado, mas negou que fosse o motivo.",
    "Haussmann usou o argumento para tirar verba do Estado, mas escreveu que nunca pensou nisso.")
substituir(3, "explicacao", "Mas escreveu que nunca pensou no valor estratégico delas.",
    "Mas escreveu que, ao acrescentar ao plano os trechos que ele mesmo propôs, nunca pensou no valor estratégico "
    "deles, embora nas mesmas memórias comemorasse ter rasgado com o Boulevard de Sébastopol o bairro dos motins e "
    "das barricadas.")
substituir(3, "explicacao",
    "O historiador Patrice de Moncan aponta outros motivos: a reforma incluiu esgotos, aquedutos, parques, hospitais e "
    "escolas, e os bairros abertos estavam entre os mais atingidos pela cólera.",
    "O historiador Patrice de Moncan lembra que boa parte da reforma (esgotos, aquedutos, parques, hospitais e escolas) "
    "não tinha valor militar. E os primeiros grandes eixos cortaram justamente os bairros onde a cólera tinha sido pior.")
substituir(3, "explicacao", "e os rebeldes perderam sobretudo por estarem em minoria de cinco para um",
    "e os rebeldes perderam por estarem em minoria de cinco para um, com menos armas, sem comando único e sem plano de defesa")
acrescentar_trecho(3, 0,
    "In his memoirs, he wrote that his new Boulevard Sébastopol resulted in the \"gutting of old Paris, of the quarter of riots and barricades\". [...] "
    "they had fewer weapons and fewer people trained to use them, they had no hope of getting support from outside Paris, they had no plan for the defence of the city; "
    "they had very few experienced officers; there was no single commander")

# 0004: a crítica de Mokhtarian e Chen (2004); gancho mais preciso
substituir(4, "gancho", "A média fica em torno de uma hora por dia", "Na média geral, o total fica perto de uma hora por dia")
substituir(4, "explicacao", "Por isso, o urbanista Robert Cervero",
    "A regularidade tem críticos. Uma revisão da literatura empírica publicada em 2004 por Patricia Mokhtarian e "
    "Cynthia Chen concluiu que o tempo de viagem só parece constante, se tanto, nas médias de populações inteiras. "
    "De pessoa para pessoa, ele varia com renda, emprego, posse de carro e densidade do bairro. "
    "Ainda assim, o urbanista Robert Cervero")
CANDIDATOS[3]["fontes"].append({
    "url": "https://ideas.repec.org/a/eee/transa/v38y2004i9-10p643-675.html",
    "titulo": "TTB or not TTB, that is the question: a review and analysis of the empirical literature on travel time (and money) budgets",
    "idioma": "en",
    "trecho": (
        "TTB or not TTB, that is the question: a review and analysis of the empirical literature on travel time (and money) budgets [...] "
        "Mokhtarian, Patricia L. & Chen, Cynthia, 2004. [...] "
        "We conclude (with prior researchers) that travel time expenditures are not constant except, perhaps, at the most aggregate level. [...] "
        "Travel time expenditure is strongly related to individual and household characteristics (e.g., income level, gender, employment status, and car ownership) [...] "
        "and characteristics of residential areas (e.g., density"
    ),
})

# 0006: a prática finlandesa é relato sem documentação; bloquear "nem sempre resolve"
substituir(6, "gancho", "Na Finlândia, há planejadores que visitam os parques",
    "Conta-se que, na Finlândia, planejadores visitam os parques")
substituir(6, "explicacao",
    "A neve facilita o trabalho, porque esconde as trilhas antigas e deixa à mostra só as pegadas novas.",
    "A neve facilita o trabalho, porque esconde as trilhas antigas e deixa à mostra só as pegadas novas. O relato "
    "finlandês circula muito em textos de urbanismo, mas não há estudo que documente a prática.")
substituir(6, "explicacao", "Proibir costuma funcionar mal:", "Bloquear com cercas ou placas nem sempre resolve:")
trocar(6, confianca="consenso_parcial")

# 0008: sem o 214.529 sem data; quem demarcou os lotes
substituir(8, "explicacao",
    "o Plano Piloto nunca chegou aos 500 mil moradores previstos e tem 214.529, enquanto Ceilândia sozinha tinha 350.347 em 2021.",
    "o Plano Piloto nunca chegou aos 500 mil moradores previstos e tem pouco mais de 200 mil, enquanto Ceilândia "
    "sozinha tinha 350.347 em 2021.")
substituir(8, "explicacao", "e a campanha, presidida pela primeira-dama, demarcou mais de 17 mil lotes",
    "criou-se uma campanha, presidida pela primeira-dama, e foram demarcados mais de 17 mil lotes")

# 0009: "apoio experimental", replicações com efeitos menores; sem mito_desmentido
substituir(9, "gancho", "tem um lado confirmado:", "tem um lado com apoio experimental:")
substituir(9, "explicacao", "resultado publicado na revista Science.",
    "resultado publicado na revista Science. Replicações posteriores acharam efeitos menores e dependentes do contexto.")
trocar(9, tipos_espanto=["contraintuitivo", "conexao_inesperada"])

# 0010: deixar claro que era habitação popular
substituir(10, "gancho", "A implosão do conjunto Pruitt-Igoe, nos EUA, em 1972,",
    "A implosão do conjunto habitacional popular Pruitt-Igoe (EUA), em 1972,")

# 0014: baixa pressão diurna; chuva "em parte" pela ilha de calor, do lado para onde o vento leva o ar da cidade
substituir(14, "explicacao", "e a baixa pressão criada sobre a cidade atrai ar úmido das áreas rurais",
    "e, durante o dia, a baixa pressão criada sobre a cidade atrai ar úmido das áreas rurais")
substituir(14, "explicacao", "A chuva mensal costuma ser maior a favor do vento das cidades.",
    "Em parte por isso, a chuva mensal costuma ser maior do lado para onde o vento leva o ar da cidade do que do "
    "lado de onde ele vem.")

# limites de 220 caracteres nos ganchos alterados
substituir(3, "gancho", "Paris ganhou bulevares largos para", "Paris ganhou bulevares para")
substituir(9, "gancho", "em experimentos na Holanda,", "na Holanda,")
substituir(10, "gancho", "conjunto habitacional popular Pruitt-Igoe (EUA)", "conjunto habitacional Pruitt-Igoe (EUA)")
substituir(10, "gancho", "Mas o fracasso não foi só do projeto", "Mas a culpa não foi só do projeto")
substituir(10, "gancho", "a manutenção dependia dos aluguéis", "a manutenção vivia dos aluguéis")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(9, "explicacao", " Replicações posteriores acharam efeitos menores e dependentes do contexto.", "")
trocar(9, nota_surpresa=3)
substituir(10, "explicacao", "o consenso atual é que o projeto estava \"condenado desde o início\".", "o consenso atual é que o conjunto, sem verba suficiente, estava \"condenado desde o início\".")
