"""Rodada 2 da microbiologia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-17-microbiologia-01.py"))
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)

LOTE, AREA, TEMA = _base.LOTE, _base.AREA, _base.TEMA
wiki = _base.wiki
CANDIDATOS = _base.CANDIDATOS


def trocar(n, **campos):
    CANDIDATOS[n - 1].update(campos)


# 0002: tirar os 13–48% e a frase do oxigênio; usar a abundância; "identificada"
trocar(2,
    temas_secundarios=["vida_marinha"],
    gancho="O ser fotossintetizante provavelmente mais abundante da Terra é uma bactéria marinha minúscula que só foi identificada em 1986.",
    explicacao=(
        "A Prochlorococcus é uma cianobactéria que vive nas camadas iluminadas dos oceanos tropicais e "
        "subtropicais. Ela mede de 0,5 a 0,7 milésimo de milímetro e é o menor organismo fotossintetizante "
        "conhecido. Já havia registros esparsos de cianobactérias minúsculas no oceano, mas ela só foi "
        "reconhecida como um organismo próprio em 1986, por Sallie (Penny) Chisholm e colaboradores, com a "
        "ajuda da citometria de fluxo, uma técnica que conta e mede células uma a uma. O tamanho reduzido é uma "
        "vantagem em águas pobres em nutrientes. A população que resulta disso é astronômica: um único "
        "mililitro de água da superfície do mar pode conter 100 mil células ou mais, e estima-se que existam "
        "cerca de 3×10²⁷ delas no mundo, mais ou menos o número de átomos em uma tonelada de ouro. Por isso ela "
        "é provavelmente o organismo fotossintetizante mais abundante do planeta."
    ),
    fontes=[wiki("Prochlorococcus",
        "These bacteria belong to the photosynthetic picoplankton and are probably the most abundant photosynthetic organism on Earth. [...] "
        "a single millilitre of surface seawater may contain 100,000 cells or more. Worldwide, the average yearly abundance is (2.8 to 3.0)×1027 individuals "
        "(for comparison, that is approximately the number of atoms in a ton of gold). [...] "
        "Although there had been several earlier records of very small chlorophyll-b-containing cyanobacteria in the ocean, Prochlorococcus was discovered in 1986 by Sallie W. [...] "
        "using flow cytometry. [...] "
        "Prochlorococcus is the smallest at just 0.5 to 0.7 micrometres in diameter.")],
)

# 0004: não foi o "primeiro" vírus gigante; tirar a 'ideia antiga'; usar o genoma
trocar(4,
    gancho="O mimivírus foi confundido com uma bactéria por mais de dez anos: era tão grande que aparecia na coloração de Gram, ao microscópio comum.",
    explicacao=(
        "Em 1992, pesquisadores que investigavam a doença dos legionários encontraram, dentro de amebas, um "
        "micro-organismo que parecia uma bactéria. Ele foi visto numa coloração de Gram, um teste clássico para "
        "bactérias, e classificado como uma bactéria Gram-positiva. Recebeu o nome de Bradfordcoccus, em "
        "referência à cidade inglesa de Bradford, de onde vinha a ameba. Só em 2003 uma equipe de Marselha "
        "mostrou, num artigo na revista Science, que aquilo era um vírus. Ganhou o nome de mimivírus, de "
        "'micróbio imitador'. O capsídeo tem cerca de 400 nanômetros, e o genoma tem 1.181.404 pares de "
        "bases: é maior que o de pelo menos 30 grupos de seres celulares. Ele ainda carrega genes que se "
        "achava serem exclusivos de células, como os das enzimas que preparam os aminoácidos para a "
        "fabricação de proteínas. Depois dele foram descritos vírus ainda maiores."
    ),
    fontes=[wiki("Mimivirus",
        "APMV was discovered accidentally in 1992 within the amoeba Acanthamoeba polyphaga, after which it is named, during research into legionellosis by researchers from Marseille and Leeds. "
        "The virus was observed in a Gram stain and mistakenly thought to be a Gram-positive bacterium. "
        "As a consequence it was named Bradfordcoccus, after Bradford, England, where the amoeba had originated. "
        "In 2003, researchers at the Université de la Méditerranée in Marseille, France, published a paper in Science identifying the micro-organism as a virus. [...] "
        "Until 2013, when a larger virus Pandoravirus was described [...] "
        "Mimivirus has a capsid diameter of 400 nm. [...] "
        "The mimivirus genome is a linear, double-stranded molecule of DNA with 1,181,404 base pairs in length. [...] "
        "it is larger than at least 30 cellular clades. [...] "
        "including aminoacyl tRNA synthetases, and other genes previously thought only to be encoded by cellular organisms.")],
)

# 0005: "vírus têm parasitas"; tirar a frase sem apoio; 70% e lise 3x; 2ª fonte
trocar(5,
    gancho="Até vírus têm parasitas: o Sputnik, achado em 2008 numa torre de resfriamento de Paris, só se reproduz atrapalhando um vírus gigante.",
    explicacao=(
        "Vírus não se reproduzem sozinhos: precisam invadir uma célula e usar a maquinaria dela. O Sputnik "
        "leva essa dependência um passo adiante. Ele só se multiplica dentro de amebas que já estejam "
        "infectadas por um vírus gigante, e usa a maquinaria desse outro vírus para fazer suas próprias "
        "cópias. No processo, atrapalha a replicação do vírus gigante. Por isso foi chamado de virófago, por "
        "analogia com bacteriófago, o vírus que ataca bactérias. Encontrado em 2008 na água de uma torre de "
        "resfriamento em Paris, foi o primeiro vírus satélite conhecido que agia como parasita do vírus de que "
        "depende. O efeito é mensurável: o Sputnik reduziu em 70% a produção de partículas infecciosas do "
        "vírus gigante e diminuiu em três vezes a destruição das amebas em 24 horas. Ou seja, o parasita do "
        "vírus acaba protegendo, em parte, a célula infectada."
    ),
    fontes=[
        wiki("Sputnik_virophage",
             "Sputnik uses the helper virus's machinery for reproduction and inhibits replication of the helper virus. [...] "
             "At its discovery in a Paris water-cooling tower in 2008, Sputnik was the first known satellite virus that inhibited replication of its helper virus and thus acted as a parasite of that virus. [...] "
             "Sputnik decreased the yield of infective viral particle by 70% and also reduced the amoeba lysis by threefold at 24h.",
             "Sputnik virophage"),
        wiki("Marine_bacteriophage", "The first virophage was discovered in a cooling tower in Paris in 2008.", "Marine bacteriophage"),
    ],
)

# 0007: reconhecer predecessores; recusas segundo ela
trocar(7,
    gancho="O artigo que defendia que nossas mitocôndrias já foram bactérias livres foi recusado, segundo a autora, por cerca de quinze revistas antes de sair, em 1967.",
    explicacao=(
        "As mitocôndrias são as estruturas que produzem a maior parte da energia das nossas células, e lembram "
        "bactérias em vários detalhes. A ideia de que elas, e os cloroplastos das plantas, seriam descendentes "
        "de bactérias que passaram a viver dentro de outras células não nasceu com Lynn Margulis: ela tinha "
        "predecessores desde meados do século XIX, como Schimper, Mereschkowski, Kozo-Polyansky e Wallin. Mas "
        "estava à margem da biologia, e Margulis a retomou e a fortaleceu. O artigo em que ela defendeu a "
        "teoria saiu em 1967 depois de ser recusado, segundo ela contou, por cerca de quinze revistas "
        "científicas. Mesmo publicado, foi praticamente ignorado por mais uma década. A teoria só se tornou "
        "amplamente aceita quando a genética trouxe evidências fortes do parentesco. Margulis também ajudou a "
        "dar reconhecimento aos pioneiros que a antecederam."
    ),
    fontes=[wiki("Lynn_Margulis",
        "her formative paper, \"On the Origin of Mitosing Cells\", appeared in 1967 after being rejected by about fifteen journals. [...] "
        "her theory that cell organelles such as mitochondria and chloroplasts were once independent bacteria was largely ignored for another decade, "
        "becoming widely accepted only after it was powerfully substantiated through genetic evidence. [...] "
        "The paper, however, was \"rejected by about fifteen scientific journals,\" she recalled. [...] "
        "Margulis' work on symbiosis and her endosymbiotic theory had important predecessors, going back to the mid-19th century – "
        "notably Andreas Franz Wilhelm Schimper, Konstantin Mereschkowski, Boris Kozo-Polyansky, and Ivan Wallin – "
        "and Margulis not only promoted greater recognition for their contributions")],
)

# 0008: vacúolo explica a difusão; pepins à parte; uma única célula
trocar(8,
    gancho="Existe bactéria visível a olho nu: uma única célula em forma de filamento com até 2 centímetros, achada em folhas de mangue no Caribe e descrita só em 2022.",
    explicacao=(
        "Bactérias costumam medir alguns milésimos de milímetro. A Thiomargarita magnifica quebra essa regra: "
        "cada filamento é uma única célula, com média de um centímetro de comprimento, e algumas chegam a dois. "
        "Ela foi encontrada presa a folhas caídas de mangue-vermelho, debaixo d'água, no arquipélago de "
        "Guadalupe, nas Antilhas. O descobridor achou de início que era um fungo, e levou anos até se confirmar "
        "que era uma bactéria. A descrição formal saiu em 2022. Uma célula desse tamanho enfrenta um problema: "
        "as substâncias se difundem devagar demais lá dentro. A solução é um vacúolo gigante, que ocupa de 65% a "
        "80% do volume e empurra o citoplasma para uma camada fina junto à borda, de modo que as distâncias "
        "ficam curtas. Há outra esquisitice: o DNA fica guardado em compartimentos com membrana, os pepins, um "
        "arranjo que lembra um meio-termo entre as bactérias e as células com núcleo."
    ),
    fontes=[wiki("Thiomargarita_magnifica",
        "found growing underwater on detached leaves of red mangroves from the Guadeloupe archipelago in the Lesser Antilles. [...] "
        "These filament-shaped bacteria are the largest known, with an average length of 1 cm, and some individuals reaching 2 centimetres (0.79 in), "
        "making the bacteria visible to humans by unaided eye. [...] "
        "Gros thought his find to be a fungus; it took Gros and other researchers five years to determine that it was a bacterium [...] "
        "The bacterium was described formally in a 2022 publication. [...] "
        "Ca. T. magnifica's cell includes a similar vacuole that occupies most of the cell (65–80% by volume) and pushes the cytoplasm to the periphery of the cell [...] "
        "Researchers have named these compartments pepins. [...] "
        "it suggests a form intermediate between prokaryotes",
        "Thiomargarita magnifica")],
)

# 0010: a densidade de 2 km/cm² foi pico em sedimento incubado em laboratório
CANDIDATOS[9]["explicacao"] = (
    "As bactérias-cabo são filamentos formados por milhares de células enfileiradas, que dividem uma mesma "
    "membrana externa. Elas resolvem um problema de logística. No sedimento, o alimento (sulfeto) fica nas "
    "camadas mais fundas, enquanto o oxigênio ou o nitrato, que recebem os elétrons no fim do processo, só "
    "estão perto da superfície. O filamento inteiro trabalha como um fio: as células de baixo retiram "
    "elétrons do sulfeto, e esses elétrons viajam por fibras condutoras internas até as células de cima. É "
    "uma corrente elétrica biológica percorrendo mais de um centímetro, uma distância enorme na escala de "
    "uma bactéria. E elas podem ser muitas: num experimento com sedimento marinho exposto ao oxigênio em "
    "laboratório, a densidade de filamentos chegou, depois de 21 dias, a cerca de 2 quilômetros sob cada "
    "centímetro quadrado de superfície."
)
CANDIDATOS[9]["fontes"] = [
    wiki("Cable_bacteria",
         "Cable bacteria are filamentous bacteria that conduct electricity across distances over 1 cm in sediment and groundwater aquifers. [...] "
         "Cable bacteria couple the reduction of oxygen or nitrate at the sediment surface to the oxidation of sulfide [...] "
         "but the outer cell membrane is shared by all cells in a filament."),
    {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4030233/",
     "titulo": "Succession of cable bacteria and electric currents in marine sediment (ISME Journal, 2014)", "idioma": "en",
     "trecho": "we followed a population for 53 days after exposing sulphidic sediment with initially no detectable filaments to oxygen. "
               "After 10 days, cable bacteria and electric currents were established throughout the top 15 mm of the sediment, "
               "and after 21 days the filament density peaked with a total length of 2 km cm−2."},
]

# 0013: tirar a frase sem apoio; incluir a resistência a Woese
trocar(13,
    explicacao=(
        "Durante boa parte do século XX, todos os micróbios sem núcleo foram classificados num só grupo, com "
        "base na forma, na química e no metabolismo. O microbiologista Carl Woese decidiu olhar para outra "
        "coisa: um RNA presente nos ribossomos de todas as células, que muda devagar ao longo da evolução e "
        "serve como relógio de parentesco. Em 1977, ele e George Fox mostraram que alguns desses micróbios "
        "formavam um grupo à parte, e Woese definiu as arqueias como um novo domínio da vida. A aceitação foi "
        "lenta. Biólogos de prestígio como Salvador Luria e Ernst Mayr se opuseram, e uma década de trabalho "
        "minucioso rendeu a Woese a fama de excêntrico. Com o acúmulo de dados, a comunidade científica só "
        "aceitou as arqueias em meados dos anos 1980. Hoje a técnica que ele usou é considerada uma revolução "
        "na microbiologia."
    ),
    fontes=[wiki("Carl_Woese",
        "Woese defined the Archaea (a new domain of life) in 1977 through a pioneering phylogenetic taxonomy of 16S ribosomal RNA, a technique that has revolutionized microbiology. [...] "
        "For much of the 20th century, prokaryotes were regarded as a single group of organisms and classified based on their biochemistry, morphology and metabolism. [...] "
        "Acceptance of the validity of Woese's phylogenetically valid classification was a slow process. "
        "Prominent biologists including Salvador Luria and Ernst Mayr objected to his division of the prokaryotes. [...] "
        "A decade of labor-intensive oligonucleotide cataloging left him with a reputation as \"a crank,\" [...] "
        "The growing body of supporting data led the scientific community to accept the Archaea by the mid-1980s.",
        "Carl Woese")],
)

# 0016: trocar o qualificador impreciso
CANDIDATOS[15]["explicacao"] = CANDIDATOS[15]["explicacao"].replace(
    "conforme o método de cálculo", "dependendo do alimento oferecido em cada incubação")

# 0012: sugestão opcional do verificador (acordo da Fiocruz em 2023)
CANDIDATOS[11]["explicacao"] = CANDIDATOS[11]["explicacao"].replace(
    "e a Fiocruz passou a apoiar a expansão do método.",
    "e em 2023 a Fiocruz fechou acordo para financiar uma grande fábrica de mosquitos com Wolbachia.")
CANDIDATOS[11]["fontes"][0]["trecho"] += (
    " In March 2023, Brazil's Oswaldo Cruz Foundation signed an agreement with WMP to provide funds for a large \"")

# Rodada 2: ajustes pontuais pedidos pelo verificador (aplicados sem nova verificação)
CANDIDATOS[9]["gancho"] = CANDIDATOS[9]["gancho"].replace("No lodo do fundo de rios e mares", "No lodo do fundo de lagos e mares")
CANDIDATOS[15]["explicacao"] = (CANDIDATOS[15]["explicacao"]
    .replace("ofereceram aos micróbios dormentes ali dentro alimento marcado com isótopos",
             "ofereceram aos micróbios que sobreviviam ali com quase nenhuma energia alimento marcado com isótopos")
    .replace(", dependendo do alimento oferecido em cada incubação.", ", conforme a incubação."))
