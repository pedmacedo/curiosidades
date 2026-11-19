"""Rodada 2 de Percepção e ilusões: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-percepcao_ilusoes-01.py"))
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


# 0001: nem todos olharam direto para o gorila (o artigo original não baixou: HTTP 500 no Europe PMC)
substituir(1, "explicacao",
    "Segundo Drew, o problema não era para onde iam os olhos: eles olhavam direto para "
    "o gorila, mas, como não procuravam um gorila, não o enxergavam.",
    "Segundo Drew, o problema não era para onde iam os olhos: muitos olharam direto para "
    "o gorila, mas, como não procuravam um gorila, não o enxergaram.")

# 0002: "a maioria dos estudos", não "a maioria dos pacientes"
substituir(2, "explicacao",
    "A maioria dos pacientes, porém, perdeu só metade do campo visual, e a visão que resta poderia ajudar.",
    "A maioria dos estudos, porém, é feita com pacientes que perderam só metade do campo visual, e a visão "
    "que resta poderia ajudar.")

# 0003: a idade do avô diverge entre fontes
substituir(3, "explicacao", "O avô, de 87 anos, estava quase cego", "O avô, já muito idoso, estava quase cego")

# 0004: reescrito como mito desmentido (a diferença cultural está desacreditada)
trocar(4,
    tipos_espanto=["mito_desmentido", "contraintuitivo"],
    confianca="consenso_parcial",
    gancho="Nos anos 1960, um estudo famoso concluiu que os San do Kalahari caíam pouco numa ilusão de óptica "
           "clássica e explicou isso pela falta de cantos retos ao redor. Hoje a ideia está desacreditada.",
    explicacao=(
        "A ilusão de Müller-Lyer, criada em 1889, faz duas linhas iguais parecerem de tamanhos diferentes "
        "conforme as pontas de seta apontem para dentro ou para fora. Na virada para o século 20, W. H. R. "
        "Rivers relatou que os nativos da ilha Murray, na Austrália, eram menos suscetíveis a ela do que os "
        "europeus. Em 1963, Marshall Segall, Donald Campbell e Melville Herskovits compararam várias "
        "populações: o erro médio ia de 1,4% a 20,3%, as três amostras de origem europeia foram as mais "
        "enganadas e os San, caçadores-coletores do Kalahari, as menos. Num artigo de 1966, com dezessete "
        "culturas, os autores atribuíram a diferença ao mundo \"carpinteirado\" das cidades, cheio de retas e "
        "ângulos retos, que treinaria a visão. Vieram resultados conflitantes: Gustav Jahoda não achou "
        "diferença entre membros de um mesmo povo africano no campo e na cidade, e um estudo de 1978 na Zâmbia "
        "achou os moradores urbanos mais suscetíveis. Hoje a hipótese é amplamente contestada. A ilusão "
        "funciona com linhas curvas e até com pontos no lugar das linhas. Crianças cegas a vida toda que fazem "
        "cirurgia para trocar o cristalino caem nela logo depois de começar a enxergar. E aves, peixes, répteis "
        "e insetos também parecem cair. Para os pesquisadores Dorsa Amir e Chaz Firestone, os estudos clássicos "
        "provavelmente refletem práticas hoje vistas como problemáticas, como descartar dados inconvenientes e "
        "não fazer os testes estatísticos adequados."
    ),
)
acrescentar_trecho(4, 0,
    "The illusion appears to be experienced by all human beings seeing it, even those who have been blind. "
    "This suggests susceptibility to the illusion is neurologically constant across humans, and undermines hypothesis promulgated in the twentieth century proposing that susceptibility was culturally determined. "
    "Such hypotheses were based on research that suffered from poor methodology and contamination by false cultural assumptions. "
    "Non-human animals are also susceptible to the illusion.")
acrescentar_trecho(4, 0,
    "The fins can point inwards to form an arrow \"head\" or outwards to form an arrow \"tail\". "
    "The line segment forming the shaft of the arrow with two tails is perceived to be longer than that forming the shaft of the arrow with two heads.")
CANDIDATOS[3]["fontes"].append({
    "url": "https://www.scientificamerican.com/article/does-culture-change-visual-perception-debunking-the-carpentered-world/",
    "titulo": "Why a Classic Psychology Theory about Vision Has Fallen Apart (Scientific American, 2025)",
    "idioma": "en",
    "trecho": "August 22, 2025 [...] "
        "psychologists in the 1960s had apparently discovered something remarkable about the illusion: only European and American urbanites fell for the trick. "
        "The illusion worked less well, or didn't work at all, on groups surveyed across Africa and the Philippines. [...] "
        "is now widely disputed, including by Amir herself. [...] "
        "The researchers theorized that the prevalence of carpentry features, such as rectangular spaces and right angles, trained the visual systems of people in more wealthy, industrialized cultures to perceive these angles in a way that make them more prone to the Müller-Lyer illusion. [...] "
        "For starters, the illusion still works when the lines are curved or even when there are no lines at all and dots take their place [...] "
        "Even more convincing, kids who have been blind their whole life and undergo lens replacement surgery are susceptible to the illusion shortly after gaining sight. "
        "And even some animals, such as birds, fish, reptiles, insects and nonhuman mammals, seem to fall for the trick. [...] "
        "these were the results of “research practices now recognized to be problematic by modern methodological standards (including discarding inconvenient data points, and failing to conduct appropriate statistical tests),” Amir and Firestone wrote.",
})

# 0011: "fabricado", não "vendido"
substituir(11, "gancho", "vendido de 1971 a 1990", "fabricado de 1971 a 1990")

# 0012: Rushton abre o gancho; a cenoura vira relato
trocar(12, gancho="Em 1967, um cientista fez uma roda girando parecer parada só cantarolando: o zumbido vibra os olhos "
                  "nas órbitas e cria um efeito estroboscópico dentro do próprio olho.")
substituir(12, "explicacao",
    "A cenoura faz o mesmo com a TV quando a "
    "mastigação vibra os olhos num múltiplo da taxa de quadros.",
    "Há relatos de algo parecido com quem mastiga algo crocante, como cenoura, diante da TV: a imagem "
    "parece tremular, porque a mastigação vibraria os olhos num múltiplo da taxa de quadros.")

# 0014: "ar pensativo"; "influencia de forma significativa"
substituir(14, "explicacao", "a melancolia diante da sopa", "o ar pensativo diante da sopa")
substituir(14, "explicacao", "o contexto muda bastante a leitura de um rosto",
    "o contexto influencia de forma significativa a leitura de um rosto")
