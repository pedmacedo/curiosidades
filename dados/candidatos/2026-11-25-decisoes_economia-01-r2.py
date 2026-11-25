"""Rodada 2 de Decisões (economia comportamental): aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-decisoes_economia-01.py"))
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


# 0002: sem superlativo
substituir(2, "explicacao", "É o exemplo mais conhecido do \"efeito padrão\"", "É um exemplo do \"efeito padrão\"")

# 0003: "mais que o dobro"; Gal sem "só"; Shogren aceitou o efeito para bens sem substitutos
substituir(3, "gancho", "pediam para vendê-la cerca do dobro do que outros aceitavam pagar por ela",
    "pediam para vendê-la mais que o dobro do que outros aceitavam pagar por ela")
substituir(3, "explicacao", "E David Gal propôs que é só inércia:", "E David Gal propôs que é inércia:")
substituir(3, "explicacao", "achou pouca evidência do efeito em bens com substitutos.",
    "achou pouca evidência do efeito em bens com substitutos, embora o tenha aceitado para bens sem substitutos.")
acrescentar_trecho(3, 0, "acknowledging the endowment effect as valid for goods without substitutes")

# 0004: abelhas pintadas como alvo e piada; o trocadilho explicado; os 80% nunca confirmados
trocar(4, nota_surpresa=3)
substituir(4, "gancho", "já se punham abelhas nas privadas, por piada.", "já se pintavam abelhas em privadas, como alvo e como piada.")
substituir(4, "explicacao", "num trocadilho com a pronúncia de Apis, o gênero da abelha",
    "num trocadilho com Apis, o gênero da abelha, que em inglês soa como \"a piss\" (\"uma mijada\")")
substituir(4, "explicacao", "Segundo testes feitos por funcionários de Schiphol, os respingos caíram 80% e o custo de limpeza, uns 8%.",
    "Funcionários de Schiphol relataram, em testes internos, queda de 80% nos respingos e de uns 8% no custo de "
    "limpeza, números muito repetidos mas baseados em estimativas por observação, nunca confirmados por um estudo "
    "controlado.")
CANDIDATOS[3]["fontes"] += [
    {"url": "https://thedecisionlab.com/intervention/how-a-picture-of-a-fly-reduced-washroom-cleaning-costs-by-8",
     "titulo": "The Decision Lab: How a picture of a fly reduced washroom cleaning costs by 8%", "idioma": "en",
     "trecho": "Schiphol Airport is often cited as the source for studies on spillage reduction, but no studies have been conducted to corroborate these results. "
               "All effectiveness rates have been based on observational estimates, with no testing methods. "
               "Kieboom estimates that the savings in cleaning costs are closer to 8% – rather than 20% – assuming the 80% spillage reduction is accurate."},
    {"url": "https://mediamatic.net/388865", "titulo": "Mediamatic: Anya Subich", "idioma": "en",
     "trecho": "It turns out that in Victorian England it was common to decorate urinals with the images of honey bees. "
               "In Latin, denomination of a honey bee is apis mellifera, which sounds similar to “a piss”."},
]

# 0005: tratamentos de câncer, não "decisões médicas reais"
substituir(5, "explicacao", "O efeito aparece também em decisões médicas reais: idosos aceitam mais",
    "O efeito aparece também em escolhas sobre tratamentos médicos: em estudos sobre câncer, idosos aceitam mais")
acrescentar_trecho(5, 0, "When considering cancer treatments, framing can shift older adults' focus from short- to long-term survival under a negative and positive frame, respectively.")

# 0006: a crítica de Silberberg, as meta-análises de 2024 e 2025; dentro de 250 palavras
substituir(6, "gancho", "Mas se a aversão à perda é tão geral ainda se discute.",
    "Mas há outra leitura, e a própria aversão à perda está em debate.")
trocar(6, explicacao=(
    "A aversão à perda, uma das ideias centrais da economia comportamental, diz que uma perda pesa mais do que um "
    "ganho do mesmo tamanho. Num experimento de 2006, Chen, Lakshminarayanan e Santos puseram macacos-prego para "
    "trocar suas fichas com dois pesquisadores que, no fim, davam exatamente o mesmo: um pedaço de maçã. Um mostrava "
    "um pedaço e o entregava. O outro mostrava dois e sempre tirava um antes da entrega. Os macacos preferiram com "
    "força o primeiro, como se o pedaço retirado fosse uma perda. Em 2008, Silberberg e colegas propuseram outra "
    "leitura: com novos experimentos com macacos e pessoas, atribuíram o resultado não à aversão à perda, mas a "
    "diferenças no tempo de espera pela recompensa entre as duas opções. O próprio conceito vem sendo questionado. "
    "Vários estudos não acharam aversão à perda em decisões sob risco, talvez porque ela não apareça com valores "
    "pequenos, e Gal e Rucker argumentaram que muito do que se atribui a ela se explica melhor por inércia. Em 2024, "
    "uma meta-análise de 607 estimativas achou perdas pesando, em média, quase o dobro dos ganhos. Em 2025, uma "
    "reanálise desses dados concluiu, já no título, que a aversão à perda \"não é robusta\": nos estudos em que "
    "ganhos e perdas tinham o mesmo tamanho e não eram apresentados em ordem, o peso ficou perto de 1."
))
CANDIDATOS[5]["fontes"] += [
    {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:PMC2251327&resultType=core&format=json",
     "titulo": "Silberberg et al. (2008), On loss aversion in capuchin monkeys", "idioma": "en",
     "trecho": "Chen, Lakshminarayanan, and Santos (2006) claim to show in three choice experiments that monkeys react rationally to price and wealth shocks, but, when faced with gambles, display hallmark, human-like biases that include loss aversion. "
               "We present three experiments with monkeys and humans consistent with a reinterpretation of their data that attributes their results not to loss aversion, but to differences between choice alternatives in delay of reinforcement."},
    {"url": "https://ideas.repec.org/a/aea/jeclit/v62y2024i2p485-516.html",
     "titulo": "Brown et al. (2024), Meta-analysis of Empirical Estimates of Loss Aversion", "idioma": "en",
     "trecho": "We examine 607 empirical estimates of loss aversion from 150 articles in economics, psychology, neuroscience, and several other disciplines. "
               "Our analysis indicates that the mean loss aversion coefficient is 1.955"},
    {"url": "https://ideas.repec.org/a/eee/joepsy/v107y2025ics0167487025000133.html",
     "titulo": "Yechiam e Zeif (2025), Loss aversion is not robust: A re-meta-analysis", "idioma": "en",
     "trecho": "In a recent paper Brown et al. (2024) meta-analyzed the literature on empirical estimates of loss aversion, spanning thirty years [...] "
               "Here, we re-meta-analyzed their dataset [...] "
               "for studies with symmetric gains and losses and no ordering of items, the loss aversion parameter was approximately 1.07 and not significantly above 1.0, suggesting similar weighting of gains and losses."},
]

# 0012: gancho sem soar como inflação; o ducado inicial
trocar(12, gancho="Num cara ou coroa em que o prêmio dobra a cada coroa, o ganho esperado é infinito, mas quase ninguém "
    "pagaria caro para jogar. O enigma, de 1713, inspirou a ideia de que cada moeda extra vale menos a quem tem muito.")
substituir(12, "explicacao", "escreveu em 1738 que qualquer homem razoável venderia sua chance, com prazer, por 20 ducados.",
    "descrevendo o jogo com aposta inicial de 1 ducado, escreveu em 1738 que qualquer homem razoável venderia sua "
    "chance, com prazer, por 20 ducados.")
acrescentar_trecho(12, 0, "Daniel Bernoulli, after describing the game with an initial stake of one ducat, stated")

# 0013: sem o "Pague o suficiente"; a revisão de 2020; consenso_parcial
trocar(13, nota_surpresa=3, confianca="consenso_parcial")
substituir(13, "explicacao",
    " Em outro trabalho, Gneezy e Rustichini mostraram experimentos em que quem recebia incentivo em dinheiro se saía "
    "pior do que quem não recebia nada; o título era \"Pague o suficiente ou não pague nada\".", "")
substituir(13, "explicacao",
    "Estudos seguintes de Gneezy e colegas indicam que o dinheiro pode motivar em tarefas vistas como chatas, mas sai "
    "pela culatra nas que já são interessantes por si.",
    "Estudos seguintes de Gneezy e colegas indicam que o dinheiro pode motivar em tarefas vistas como chatas, mas "
    "sair pela culatra nas que já são interessantes por si. O tema segue em debate: uma revisão de 2020, com mais de "
    "100 testes, concluiu que pagar por tarefas prazerosas melhora o desempenho, e que o problema aparece quando se "
    "retira um pagamento que já era esperado.")
acrescentar_trecho(13, 1, "A 2020 study which reviewed more than 100 tests of motivation crowding theory and conducted its own field experiments found that paying individuals for intrinsically enjoyable tasks boosts their performance, but that taking payment away after it is expected may lead individuals to perform worse than if they were not paid at first.")

# 0014: "a maioria"; o retorno só ligeiramente maior
substituir(14, "gancho", "as pessoas preferiram repetir", "a maioria preferiu repetir")
substituir(14, "explicacao",
    "Esses pacientes lembraram o exame como menos desagradável e se mostraram muito mais dispostos a voltar.",
    "Esses pacientes lembraram o exame como um pouco menos desagradável e, nos anos seguintes, voltaram para "
    "repetir a colonoscopia com frequência ligeiramente maior.")
CANDIDATOS[13]["fontes"].append(
    {"url": "https://yorkspace.library.yorku.ca/items/1237abd1-7e5a-4a48-bb27-c6e37bac1c34/full",
     "titulo": "Redelmeier, Katz e Kahneman (2003), Memories of colonoscopy: a randomized trial", "idioma": "en",
     "trecho": "Rates of returning for a repeat colonoscopy (median duration of follow-up 5.3 years) averaged 50.4% and were slightly higher (odds RATIO=1.41, P=0.038) for those who underwent the longer procedure"})

# 0004: gancho dentro de 220 caracteres
substituir(4, "gancho", "o \"empurrãozinho\" favorito do Nobel Richard Thaler", "o \"empurrãozinho\" favorito de Richard Thaler")
# 0006: o ano do artigo de Silberberg
acrescentar_trecho(6, 0, "Silberberg, A.; et al. (2008). \"On loss aversion in capuchin monkeys\".")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
# 0006: precisar que a ordem é a de tamanho, como no resumo de Yechiam e Zeif
substituir(6, "explicacao",
    "e não eram apresentados em ordem, o peso ficou perto de 1.",
    "e não eram apresentados em ordem de tamanho, o peso ficou perto de 1.")
