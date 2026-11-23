"""Rodada 2 de Eletricidade e magnetismo: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-eletromagnetismo-01.py"))
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


# 0001: o capítulo do alho é da edição de 1589; 1558 é duvidoso
substituir(1, "gancho", "Em 1558, um italiano testou com o próprio bafo", "No século XVI, um italiano testou com o próprio bafo")

# 0002: o número de monges varia entre os relatos
substituir(2, "gancho", "ligou cerca de duzentos monges com pedaços de fio de ferro, numa roda de 1,6 km, e descarregou neles um choque.",
           "ligou centenas de monges com pedaços de fio de ferro, numa grande roda, e descarregou neles um choque.")
substituir(2, "explicacao", "Na versão mais conhecida, eram uns duzentos monges",
           "Na versão mais conhecida (os números variam entre os relatos), eram uns duzentos monges")

# 0003: sem sugerir reação a Dalibard; carga induzida na pipa também; gravurista desacordado
substituir(3, "explicacao", "Franklin teve então a ideia de erguer a haste com uma pipa.",
           "Franklin teve a ideia de erguer a haste com uma pipa.")
substituir(3, "explicacao", "a nuvem carregada induziu carga na linha de cânhamo",
           "a nuvem carregada induziu carga na pipa e na linha de cânhamo")
substituir(3, "explicacao", "explosão derrubou o gravurista que o acompanhava", "explosão deixou desacordado o gravurista que o acompanhava")

# 0006: os pais não puderam mantê-lo na escola (não "deixou"); explicação reescrita com palavras próprias
trocar(6, nota_surpresa=3,
    gancho="As quatro \"equações de Maxwell\" dos livros não foram escritas assim por Maxwell, que usou 20 equações com 20 "
           "variáveis. A forma enxuta é de Oliver Heaviside, um telegrafista que só pôde estudar na escola até os 16 anos.",
    explicacao=(
        "Depois dos 16 anos, Heaviside não teve mais nenhum ensino formal: era um aluno de destaque, mas a família não "
        "conseguiu mantê-lo na escola, e ele passou mais um ano estudando por conta própria. O trabalho veio por um "
        "parente. O tio por casamento Charles Wheatstone, um dos inventores do primeiro telégrafo que deu certo no "
        "comércio, mandou o sobrinho em 1867 para Newcastle, numa das suas empresas de telégrafo, e dois anos depois o "
        "rapaz já era operador de telégrafo. Em 1873, caiu-lhe nas mãos o tratado de Maxwell em dois volumes, recém-"
        "lançado. Pelas palavras dele, sabia só a álgebra e a trigonometria da escola, quase esquecidas, e precisou de "
        "anos para entender a obra. No mesmo ano, a Sociedade de Engenheiros de Telégrafo barrou sua entrada, alegando "
        "não querer \"funcionários de telégrafo\". Em 1884, ele deu à teoria a roupa que ela veste até hoje: com o "
        "rotacional e o divergente do cálculo vetorial, condensou 12 das 20 equações de Maxwell em apenas quatro. E "
        "as duas versões não são idênticas: a de Heaviside é até mais fácil de adaptar à física quântica. Na velhice, conforme o relato de um colega, fugia "
        "tanto de gente que deixava os manuscritos numa mercearia para os editores buscarem. Punha \"W.O.R.M.\" "
        "depois do nome nas cartas e, conta-se, pintava as unhas de rosa e mobiliou a casa com blocos de granito. Em "
        "1922, a recém-criada Medalha Faraday teve nele o seu primeiro premiado."
    ))
substituir_trecho(6, 0, "Less well known is that Heaviside's equations and Maxwell's are not exactly the same [...] ",
    "Less well known is that Heaviside's equations and Maxwell's are not exactly the same, and in fact it is easier to modify the former to make them compatible with quantum physics. [...] ")
acrescentar_trecho(6, 0, "In 1922, he became the first recipient of the Faraday Medal, which was established that year.")

# 0008: o recorde documentado é de 22 anos (1995 a pelo menos 2017), pela Eos e pelo Observatório Real da Bélgica;
# os 100 mil anos são estimativa para correntes assim em geral
trocar(8, nota_surpresa=4,
    gancho="Numa bobina de um gravímetro na Bélgica, uma corrente elétrica circulou sem bateria nem gerador de 1995 a "
           "pelo menos 2017, 22 anos seguidos. Experimentos indicam que correntes assim durariam ao menos 100 mil anos.",
    explicacao=(
        "Lord Kelvin argumentava que, em temperaturas baixas o bastante, a resistência elétrica de qualquer material "
        "cresceria sem limite. Foi isso que levou o holandês Heike Kamerlingh Onnes a estudar a resistência perto do "
        "zero absoluto, usando o hélio líquido que acabara de ser produzido. Em 8 de abril de 1911, ao esfriar mercúrio "
        "sólido a 4,2 kelvin, ele viu a resistência sumir de repente: tinha descoberto a supercondutividade, e Kelvin "
        "estava errado. Abaixo da temperatura crítica, uma corrente posta para girar num anel supercondutor pode "
        "continuar indefinidamente, sem bateria nem gerador, e é isso que se aproveita nos eletroímãs das máquinas de "
        "ressonância magnética. Para correntes assim em geral, experimentos indicam uma duração de pelo menos 100 mil "
        "anos, e estimativas teóricas podem passar do tempo de vida estimado do universo. Um caso real fica em Membach, "
        "na Bélgica. Num gravímetro supercondutor, bobinas de fio de nióbio mantêm suspensa uma esfera de nióbio de 4 "
        "gramas, do tamanho de uma bola de pingue-pongue, a menos de 9,2 kelvin. O aparelho foi ligado em 4 de agosto "
        "de 1995 e, em 18 de setembro de 2017, completou 8.081 dias de medição contínua, um recorde mundial. A corrente "
        "injetada em 1995 nunca tinha se dissipado. Os próprios pesquisadores lembram que isso não é física nova: em "
        "teoria, uma corrente supercondutora pode fluir para sempre. O fenômeno só se explica pela mecânica quântica."
    ),
    fontes=[
        wiki("Superconductivity",
            "An electric current through a loop of superconducting wire can persist indefinitely with no power source. [...] "
            "Like ferromagnetism and atomic spectral lines, superconductivity is a phenomenon which can only be explained by quantum mechanics. [...] "
            "a property exploited in superconducting electromagnets such as those found in MRI machines. "
            "Experiments have demonstrated that currents in superconducting coils can persist for years without any measurable degradation. "
            "Experimental evidence points to a lifetime of at least 100,000 years. "
            "Theoretical estimates for the lifetime of a persistent current can exceed the estimated lifetime of the universe, depending on the wire geometry and the temperature. [...] "
            "Lord Kelvin had argued, using the law of corresponding states, that the resistivity of all substances diverges at sufficiently low temperatures. "
            "This argument influenced Onnes to investigate the low temperature limit of resistivity. Onnes result would later go onto prove Kelvin incorrect. "
            "Superconductivity was discovered in solid mercury on April 8, 1911, by Heike Kamerlingh Onnes, who was studying the resistance of mercury at cryogenic temperatures using the recently produced liquid helium as a refrigerant. "
            "At the temperature of 4.2 K, he observed that the resistance abruptly disappeared.",
            nome="Superconductivity"),
        {"url": "https://eos.org/science-updates/recording-belgiums-gravitational-history",
         "titulo": "Recording Belgium's Gravitational History (Eos, AGU)", "idioma": "en",
         "trecho": "The niobium sphere, about the size of a ping-pong ball, is encased in a metal cylinder [...] "
                   "As long as the temperature inside the container is kept below 9.2 K, niobium’s superconducting transition temperature [...] "
                   "Niobium wire coils, also kept at this low temperature, offer no resistance to the electrical current that flows through them, producing the perfectly stable magnetic field that levitates the niobium sphere. [...] "
                   "On 18 September 2017, this instrument, which began operation 4 August 1995, had monitored gravity changes continuously for 8,081 days—22 years and 45 days. [...] "
                   "In 1995, currents were injected into the superconducting coils, causing the sphere to levitate. "
                   "More than 22 years later, the currents persist. "
                   "The SG measurement principle is based on monitoring the levitation of a 4-gram superconducting niobium sphere. [...] "
                   "This isn’t new physics—in theory, a superconducting current can flow forever"},
        {"url": "https://www.astro.oma.be/en/world-record-in-the-underground-laboratory-of-membach/",
         "titulo": "World record in the underground laboratory of Membach (Royal Observatory of Belgium, 2017)", "idioma": "en",
         "trecho": "World record in the underground laboratory of Membach: A sphere of mass 4 grams has been levitating for 8081 days [...] "
                   "The total duration is 22 years and 45 days, or 8081 days. [...] "
                   "In 1995, currents were injected into superconducting coils causing the sphere to levitate; the currents have never been dissipated ever since."},
    ])

# 0009: "sem gastar energia" engana (a rã precisou de um eletroímã potentíssimo)
substituir(9, "explicacao", "pode flutuar em equilíbrio estável, sem gastar energia.", "pode flutuar em equilíbrio estável.")

# 0010: duas causas da confusão (o filme e o nome da companhia); nota 3
trocar(10, nota_surpresa=3)
substituir(10, "gancho", ", como se repete. Ele não estava lá, e essa disputa tinha acabado dez anos antes. A confusão veio de um filme.",
           ". Ele não estava lá, e essa disputa tinha acabado dez anos antes. A confusão veio de um filme e de um nome.")
# 0010 (opcional): "cordas", como na fonte ("large ropes")
substituir(10, "explicacao", "estrangulada por cabos ligados a um guincho a vapor.",
           "estrangulada por cordas grossas puxadas por um guincho a vapor.")

# 0011: em 1800 ele presenciou; o relato saiu depois
substituir(11, "gancho", "Em 1800, Humboldt contou ter visto poraquês", "Humboldt relatou ter visto, em 1800, poraquês")

# 0013: retoques de redação
substituir(13, "gancho", "Hoje está em uns 300 milhões de alto-falantes e afins por ano.",
           "Hoje entra em uns 300 milhões de alto-falantes e afins por ano.")
substituir(13, "explicacao", "entre eles alto-falantes de laptops e celulares, fones de ouvido.",
           "entre eles alto-falantes de laptops e celulares e fones de ouvido.")
