LOTE = "2026-11-18-arquitetura-01"
AREA = "artes"
TEMA = "arquitetura"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 a cúpula do Panteão fica mais leve à medida que sobe
    {
        "temas_secundarios": ["roma_antiga", "grandes_obras"],
        "tipos_espanto": ["engenhosidade", "escala_absurda"],
        "gancho": "A cúpula do Panteão de Roma, com quase 2 mil anos, ainda é a maior do mundo em concreto sem armadura. O segredo: o concreto fica mais leve à medida que sobe, até terminar num buraco aberto para o céu.",
        "explicacao": (
            "O Panteão atual foi concluído no reinado do imperador Adriano, que governou de 117 a 138, e está em "
            "uso desde então: desde o ano 609 funciona como igreja, o que ajudou a preservá-lo. O diâmetro interno "
            "e a altura até o óculo, a abertura no topo, são iguais: 43 metros. A "
            "parede da cúpula vai afinando, de 6,4 metros de espessura na base para 1,2 metro junto ao óculo. O "
            "material também muda com a altura. Embaixo, as pedras misturadas ao concreto são de travertino, um "
            "calcário pesado. Mais acima vêm cacos de telha de terracota e, no alto, tufo e pedra-pomes, rochas "
            "porosas e leves. O próprio óculo tira peso justamente da região em que a cúpula seria mais frágil. "
            "Uma simulação feita pelos pesquisadores Mark e Hutchison estimou que, se o concreto tivesse o mesmo "
            "peso do começo ao fim, as tensões na estrutura seriam cerca de 80% maiores. Entre as cúpulas antigas "
            "que restam, as outras foram projetadas com tirantes, correntes ou cintas, ou receberam esses reforços "
            "depois para não cair. A do Panteão segue de pé sem nenhum deles."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Pantheon,_Rome",
            "Almost two thousand years after it was built, the Pantheon's dome is still the world's largest unreinforced concrete dome. "
            "The height to the oculus and the diameter of the interior circle are the same, 43 metres (142 ft). "
            "It is one of the best-preserved of all Ancient Roman buildings, in large part because it has been in continuous use throughout its history. [...] "
            "reconstructed under Hadrian (117–138). [...] "
            "the present building was completed by the emperor Hadrian [...] "
            "The thickness of the dome varies from 6.4 metres (21 ft) at the base of the dome to 1.2 metres (3.9 ft) around the oculus. "
            "The materials used in the concrete of the dome also vary. At its thickest point, the aggregate is travertine, then terracotta tiles, then at the very top, tufa and pumice, both porous light stones. "
            "At the very top, where the dome would be at its weakest and vulnerable to collapse, the oculus lightens the load. [...] "
            "Mark and Hutchison estimated that, if normal weight concrete had been used throughout, the stresses in the arch would have been some 80% greater. [...] "
            "It is the only masonry dome to not require reinforcement. All other extant ancient domes were either designed with tie-rods, chains and banding or have been retrofitted with such devices to prevent collapse. [...] "
            "Since AD 609, it has served as the Roman Catholic Basilica of Saint Mary and the Holy Martyrs",
            nome="Pantheon, Rome")],
    },
    # 2 o concreto romano que fecha as próprias rachaduras
    {
        "temas_secundarios": ["roma_antiga", "quimica_cotidiano", "grandes_obras"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "O concreto romano conserta as próprias rachaduras. Pedrinhas brancas de cal, que por muito tempo pareceram sinal de mistura malfeita, reagem com a água que entra nas fendas e as fecham com cristais novos.",
        "explicacao": (
            "Por décadas, a explicação para a durabilidade das obras romanas foi um ingrediente: a cinza vulcânica "
            "da região de Pozzuoli, perto de Nápoles, levada a todo o império. Mas as amostras antigas têm outra "
            "marca: grãos brancos de poucos milímetros, os \"clastos de cal\", que não existem no concreto moderno "
            "e costumavam ser vistos como fruto de mistura descuidada ou de matéria-prima ruim. Em 2023, uma equipe "
            "liderada por Admir Masic, do MIT, com pesquisadores de Harvard, da Itália e da Suíça, publicou outra "
            "leitura na revista Science Advances. A análise mostrou que os grãos são formas de carbonato de cálcio "
            "criadas a temperaturas extremas, como as que surgem quando se usa cal virgem, que esquenta muito ao "
            "reagir. Os romanos fariam, portanto, uma \"mistura a quente\", o que também acelera a pega. Nesse "
            "processo, os clastos ficam quebradiços. Quando surge uma fissura, ela tende a passar por eles, e a "
            "água que entra dissolve o cálcio, que se recristaliza como carbonato de cálcio e veda a fenda. Para "
            "testar a ideia, a equipe rachou de propósito amostras feitas com a receita quente e passou água "
            "pelas fendas. Em duas semanas elas se fecharam e a água parou de passar. Numa amostra igual sem cal "
            "virgem, a água continuou correndo."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": "https://news.mit.edu/2023/roman-concrete-durability-lime-casts-0106",
             "titulo": "Riddle solved: Why was Roman concrete so durable? (MIT News, 6 jan. 2023)",
             "idioma": "en",
             "trecho": (
                "a team of investigators from MIT, Harvard University, and laboratories in Italy and Switzerland, has made progress in this field, discovering ancient concrete-manufacturing strategies that incorporated several key self-healing functionalities. "
                "The findings are published today in the journal Science Advances, in a paper by MIT professor of civil and environmental engineering Admir Masic [...] "
                "For many years, researchers have assumed that the key to the ancient concrete's durability was based on one ingredient: pozzolanic material such as volcanic ash from the area of Pozzuoli, on the Bay of Naples. "
                "This specific kind of ash was even shipped all across the vast Roman empire to be used in construction [...] "
                "small, distinctive, millimeter-scale bright white mineral features [...] "
                "These are not found in modern concrete formulations [...] "
                "Previously disregarded as merely evidence of sloppy mixing practices, or poor-quality raw materials, the new study suggests that these tiny lime clasts gave the concrete a previously unrecognized self-healing capability. [...] "
                "he and his team determined that the white inclusions were, indeed, made out of various forms of calcium carbonate. "
                "And spectroscopic examination provided clues that these had been formed at extreme temperatures, as would be expected from the exothermic reaction produced by using quicklime instead of, or in addition to, the slaked lime in the mixture. "
                "Hot mixing, the team has now concluded, was actually the key to the super-durable nature. [...] "
                "this increased temperature significantly reduces curing and setting times [...] "
                "During the hot mixing process, the lime clasts develop a characteristically brittle nanoparticulate architecture [...] "
                "As soon as tiny cracks start to form within the concrete, they can preferentially travel through the high-surface-area lime clasts. "
                "This material can then react with water, creating a calcium-saturated solution, which can recrystallize as calcium carbonate and quickly fill the crack [...] "
                "the team produced samples of hot-mixed concrete that incorporated both ancient and modern formulations, deliberately cracked them, and then ran water through the cracks. "
                "Sure enough: Within two weeks the cracks had completely healed and the water could no longer flow. "
                "An identical chunk of concrete made without quicklime never healed, and the water just kept flowing through the sample."
             )},
            wiki("Roman_concrete",
                "Research in 2023 found that lime clasts, previously considered a sign of poor aggregation technique, react with water seeping into any cracks. "
                "This produces reactive calcium, which allows new calcium carbonate crystals to form and reseal the cracks.",
                nome="Roman concrete"),
        ],
    },
    # 3 o solo mole que entortou a Torre de Pisa a salvou dos terremotos
    {
        "temas_secundarios": ["vulcoes_terremotos", "falhas_engenharia"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "O solo mole que entortou a Torre de Pisa também a protegeu: ela resistiu a pelo menos quatro terremotos fortes desde 1280 porque, sobre esse chão macio, ela não entra em ressonância com o tremor.",
        "explicacao": (
            "A torre começou a afundar em 1178, quando a obra chegava ao segundo andar. A fundação tinha só três "
            "metros e estava num subsolo fraco e instável. A construção então parou por quase um século, porque "
            "Pisa vivia em guerra com Gênova, Lucca e Florença, e essa pausa deu tempo para o solo se acomodar. Sem "
            "ela, a torre quase certamente teria caído. Mesmo assim, a inclinação foi piorando e chegou a 5,5 graus "
            "em 1990, quando a torre foi fechada ao público. A partir de 1993, engenheiros puseram contrapesos de "
            "chumbo e retiraram solo de baixo do lado mais alto, até baixar a inclinação para 3,97 graus em 2001. "
            "O mesmo terreno explica a resistência aos terremotos. Um estudo de engenharia de 2018 concluiu que a "
            "altura e a rigidez da torre, somadas à maciez do solo da fundação, mudam o jeito como ela vibra, de "
            "modo que ela não entra em ressonância com o movimento do chão. Ou seja, o solo que levou a torre à "
            "beira do colapso é o mesmo que evitou estragos graves nos tremores."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Leaning_Tower_of_Pisa",
            "In 1178, the tower began to sink after construction progressed to the second floor. "
            "This was due to a mere three-metre foundation, set in weak, unstable subsoil, a design that was flawed from the beginning. "
            "Construction was subsequently halted for the better part of a century, as the Republic of Pisa was almost continually engaged in battles with Genoa, Lucca, and Florence. "
            "This allowed time for the underlying soil to settle. Otherwise, the tower would almost certainly have toppled. [...] "
            "By 1990, the tilt had reached 5.5 degrees. The structure was stabilized by remedial work between 1993 and 2001, which reduced the tilt to 3.97 degrees. [...] "
            "Starting in 1993, 870 tonnes of lead counterweights were added, which straightened the tower slightly. [...] "
            "The tower was closed to the public on 7 January 1990 [...] "
            "by removing 38 cubic metres (1,342 cubic feet) of soil from underneath the raised end. [...] "
            "The tower has survived at least four strong earthquakes since 1280. "
            "A 2018 engineering investigation concluded that the tower withstood the tremors because of dynamic soil-structure interaction: "
            "the height and stiffness of the tower combined with the softness of the foundation soil influences the tower's vibrational characteristics in such a way that it does not resonate with earthquake ground motion. "
            "The same soft soil that caused the leaning and brought the tower to the verge of collapse helped to prevent significant destruction in the event of an earthquake.",
            nome="Leaning Tower of Pisa")],
    },
    # 4 o arranha-céu consertado às escondidas
    {
        "temas_secundarios": ["falhas_engenharia", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1978, um arranha-céu recém-inaugurado em Nova York corria risco de cair com ventos fortes vindos na diagonal. O reforço foi feito às escondidas, à noite, com os escritórios abertos de dia, e só veio a público em 1995.",
        "explicacao": (
            "O Citicorp Center, de 59 andares, se apoia em quatro pilares no meio de cada lado, e não nos cantos, "
            "porque uma igreja luterana precisava ficar no terreno. O engenheiro William LeMessurier fez as contas "
            "de vento sobretudo para ventos que batem de frente nas fachadas, o único caso exigido pelo código de "
            "obras. Para economizar, a fornecedora de aço trocou as juntas soldadas por parafusadas, e o escritório "
            "dele aprovou a mudança sem que ele próprio a examinasse. Em 1978, ao refazer os cálculos com ventos na "
            "diagonal, ele viu que a carga nas juntas parafusadas subia 160%. Um caso desses já havia chamado a "
            "atenção de uma estudante de Princeton, Diane Hartley, que analisava o prédio no seu trabalho de fim de "
            "curso. Se faltasse energia para o amortecedor de massa no topo, um vento de 110 km/h poderia derrubar "
            "a torre. A solução foi soldar chapas de aço sobre as juntas, à noite, a partir de agosto de 1978. "
            "Houve planos secretos de evacuação, e um furacão, o Ella, chegou a ameaçar a cidade, mas mudou de "
            "rumo. O caso só foi contado em 1995, pela revista The New Yorker. A história ganhou uma reviravolta: "
            "uma reavaliação do NIST, instituto de padrões dos EUA, concluiu depois que os ventos diagonais não eram "
            "a ameaça que se pensava, e que talvez o reforço nem fosse necessário."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Citicorp_Center_engineering_crisis",
            "In July 1978, a possible structural flaw was discovered in Citicorp Center (now Citigroup Center), a skyscraper that had recently been completed in New York City. [...] "
            "The reinforcements were done at night while the offices in the building were open for regular operation during the day. [...] "
            "Estimates at the time suggested that if the mass damper was disabled by a power failure, the building could be toppled by a 70-mile-per-hour (110 km/h) quartering wind [...] "
            "The reinforcement effort was kept secret until 1995. [...] "
            "Hurricane Ella did threaten New York during the retrofitting, but it changed course before arriving. "
            "Ultimately, the retrofitting may not have been necessary. "
            "A NIST reassessment using modern technology later determined that the quartering wind loads were not the threat that LeMessurier and Hartley had thought. [...] "
            "is a 59-story skyscraper [...] "
            "a new building for the site's previous occupant, St. Peter's Lutheran Church, was erected at the site's northwest corner [...] "
            "To avoid the church, the tower is supported by four stilts positioned underneath the centers of each of the tower's edges. [...] "
            "To save money, Bethlehem Steel proposed changing the construction plans to use bolted joints, a design modification accepted by LeMessurier's office but unknown to the engineer himself until later. [...] "
            "came to rely primarily on the calculations for perpendicular winds. "
            "Perpendicular winds were the only calculations required by New York City building code. [...] "
            "a tuned mass damper on the roof. [...] "
            "In June 1978, Princeton University engineering student Diane Hartley was writing her senior thesis about Citicorp Center's design [...] "
            "calculated stresses from quartering winds, finding them higher than the maximum expected stress values provided to her by LeMessurier's firm. [...] "
            "quartering winds would create a 40 percent increase in wind loads and a 160 percent increase in the load at the bolted joints. [...] "
            "Citicorp accepted LeMessurier's proposal to weld steel plates over the bolted joints [...] "
            "Construction crews started installing the welded panels at night in August 1978. [...] "
            "Citicorp and local officials created emergency evacuation plans for the immediate neighborhood. "
            "However, these evacuation plans were not publicized at the time [...] "
            "the work was not publicized until 1995, when a lengthy article appeared in The New Yorker.",
            nome="Citicorp Center engineering crisis")],
    },
    # 5 as conchas da Ópera de Sydney saíram de uma mesma esfera
    {
        "temas_secundarios": ["geometria_topologia", "historia_computacao"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Por anos, ninguém achou um jeito viável de construir as conchas da Ópera de Sydney. A saída, em 1961, foi tirar todas de uma mesma esfera: com curvatura igual, as peças podiam sair de moldes comuns.",
        "explicacao": (
            "O dinamarquês Jørn Utzon venceu o concurso em 1957 com desenhos tão simples que o júri os chamou de "
            "quase diagramáticos. Erguer aquelas cascas era outra história. Moldar o concreto no próprio local "
            "custaria uma fortuna, e como nenhuma forma do telhado se repetia, pré-fabricar cada peça sairia ainda "
            "mais caro. De 1957 a 1963, a equipe testou pelo menos 12 versões, com parábolas, nervuras circulares e "
            "elipsoides, num dos primeiros usos de computadores em análise estrutural. Em meados de 1961 veio a "
            "ideia: todas as cascas seriam recortes de uma mesma esfera, que tem 75,2 metros de raio. Com a "
            "curvatura igual em todas as direções, arcos de comprimentos diferentes podiam ser moldados numa forma "
            "comum, e segmentos iguais se encaixavam lado a lado. Quem teve a ideia ainda é disputado: o crédito "
            "foi dado a Utzon, mas engenheiros da firma de Ove Arup lembram de discussões em Londres. Utzon não viu "
            "o fim da obra. Depois da troca de governo em 1965, sob críticas a custos e prazos, ele se demitiu em 1966. A Ópera "
            "foi inaugurada em 1973, e Utzon morreu em 2008 sem ter voltado à Austrália para ver o prédio pronto."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Sydney_Opera_House",
            "a series of large precast concrete \"shells\", each composed of sections of a sphere of 75.2 metres (246 ft 8.6 in) radius [...] "
            "Ove Arup & Partners were unable to find an acceptable solution to constructing them. "
            "The formwork for using in-situ concrete would have been prohibitively expensive, and, because there was no repetition in any of the roof forms, the construction of precast concrete for each individual section would possibly have been even more expensive. "
            "From 1957 to 1963, the design team went through at least 12 iterations of the form of the shells trying to find an economically acceptable form (including schemes with parabolas, circular ribs and ellipsoids) before a workable solution was completed. "
            "The design work on the shells involved one of the earliest uses of computers in structural analysis [...] "
            "In mid-1961, the design team found a solution to the problem: the shells all being created as sections from a sphere. "
            "This solution allows arches of varying length to be cast in a common mould, and a number of arch segments of common length to be placed adjacent to one another, to form a spherical section. "
            "With whom exactly this solution originated has been the subject of some controversy. It was originally credited to Utzon. [...] "
            "\"Utzon came up with an idea of making all the shells of uniform curvature throughout in both directions.\" [...] "
            "the engineers and some of their associates, with equal conviction, recall discussion in both central London and at Ove's house. [...] "
            "The drawings submitted for this scheme are simple to the point of being diagrammatic. [...] "
            "the building was formally opened by Queen Elizabeth II on 20 October 1973, 16 years after Utzon's 1957 selection as winner of an international design competition. [...] "
            "there was a change of government in 1965 [...] "
            "Due to the Ministry's criticism of the project's costs and time, along with their impression of Utzon's designs being impractical, this ultimately led to his resignation in 1966 [...] "
            "Utzon died on 29 November 2008, having never returned to Australia to see the completed Opera House.",
            nome="Sydney Opera House")],
    },
    # 6 Ise: o santuário refeito a cada 20 anos
    {
        "temas_secundarios": ["religioes", "asia_antiga", "paradoxos_logica"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "O Santuário de Ise, o mais sagrado do xintoísmo, é desmontado e refeito idêntico, no terreno ao lado, a cada 20 anos. Os prédios atuais, de 2013, são a 62ª versão: ao mesmo tempo novos e muito antigos.",
        "explicacao": (
            "O costume se chama Shikinen Sengū. A cada ciclo, os dois santuários principais, o Naikū, dedicado à "
            "deusa Amaterasu, e o Gekū, além da ponte de madeira Uji, com 100 metros, são reconstruídos "
            "seguindo especificações rigorosas. A ideia é que os edifícios fiquem para sempre novos e, ao mesmo "
            "tempo, para sempre antigos e originais. O ritual se liga à crença xintoísta de renovar as coisas para "
            "manter seu prestígio divino e também serve para passar as técnicas de construção de uma geração para "
            "outra. A ponte, por exemplo, costuma ficar com carpinteiros menos experientes, que treinam ali antes "
            "de trabalhar no santuário principal. O propósito original do rito é desconhecido. O primeiro prédio "
            "do Naikū foi erguido pelo imperador Tenmu, que reinou de 678 a 686, e a primeira reconstrução "
            "cerimonial coube à sua mulher, a imperatriz Jitō, em 692. As construções são de cipreste japonês, "
            "encaixadas sem pregos. Ao lado de cada uma fica um terreno vazio, coberto de seixos brancos, onde a "
            "próxima versão será erguida. O processo inteiro leva cerca de 17 anos. A versão de 2013 foi paga só "
            "com doações privadas, de 57 bilhões de ienes, e a próxima está prevista para 2033."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Ise_Grand_Shrine",
            "the shrine is Shinto's holiest and most important site. [...] "
            "The old shrines are dismantled and new ones built on an adjacent site to exacting specifications every 20 years at exorbitant expense, so that the buildings will be forever new and forever ancient and original. "
            "The present buildings, dating from 2013, are the 62nd iteration to date and are scheduled for rebuilding in 2033. [...] "
            "The shrine buildings are made of solid cypress wood and use no nails, instead being joined with wood. [...] "
            "The first shrine building at Naikū was erected by Emperor Tenmu (678–686), with the first ceremonial rebuilding being carried out by his wife, Empress Jitō, in 692. [...] "
            "The empty site beside the shrine building, the site where the previous shrine once stood and where the next will be built, is called the kodenchi. "
            "This area is strewn with large white pebbles [...] "
            "The shrine buildings at Naikū and Gekū, as well as the Uji Bridge, are rebuilt every 20 years as a part of the Shinto belief in tokowaka (常若), which means renewing objects to maintain a strong sense of divine prestige in pursuit of eternity, and as a way of passing building techniques from one generation to the next. "
            "The twenty-year renewal process is called the Shikinen Sengū. [...] "
            "The original physical purpose of the Sengū process is unknown. [...] "
            "The entire reconstruction process takes more or less 17 years [...] "
            "in 2013, the shrine was built from private donations alone, totaling 57 billion Japanese Yen (US$550 million). [...] "
            "This 100 meter wooden bridge, built in a traditional Japanese style, stretches across the Isuzu River at the entrance of Naikū. [...] "
            "The bridge is typically built by carpenters with less experience to gain more skills before moving on to take on the task of working on the main shrine. [...] "
            "is dedicated to the worship of Amaterasu",
            nome="Ise Grand Shrine")],
    },
    # 7 Djenné: a mesquita de barro rebocada pela cidade inteira
    {
        "temas_secundarios": ["africa_antiga", "costumes_rituais", "religioes"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "A Grande Mesquita de Djenné, no Mali, o maior edifício de adobe do mundo, recebe reboco novo todo ano numa festa da cidade inteira, com corrida, música e meninos brincando na massa de barro para misturá-la.",
        "explicacao": (
            "A mesquita atual é de 1907, mas a primeira no local foi erguida por volta do século XIII. As paredes "
            "são de tijolos de terra secos ao sol, chamados ferey, assentados com argamassa de areia e terra e "
            "cobertos por um reboco que dá ao prédio seu aspecto liso e esculpido. O barro tem um ponto fraco: as "
            "chuvas de cada ano o desgastam, e as variações de temperatura e umidade abrem rachaduras. Por isso, "
            "uma vez por ano a cidade se junta para refazer o revestimento. Dias antes, o reboco é preparado em "
            "covas e precisa ser mexido de tempos em tempos enquanto cura, tarefa que costuma ficar com os meninos, "
            "que brincam dentro da mistura. Na festa, há uma corrida para ver quem entrega primeiro a massa na "
            "mesquita. Homens sobem nas paredes e espalham o reboco, mulheres e meninas levam a água, a corporação "
            "dos pedreiros dirige o trabalho e os mais velhos assistem de um lugar de honra na praça do mercado. O "
            "próprio prédio facilita a tarefa: feixes de varas de palmeira, os toron, saem cerca de 60 centímetros "
            "das paredes e servem de andaime permanente. O conjunto fica sobre uma plataforma 3 metros acima do "
            "mercado, que o protege das cheias do rio Bani."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Great_Mosque_of_Djenné",
            "The Great Mosque of Djenné in the Sudano-Sahelian architectural style is the largest adobe brick building in the world. [...] "
            "on the flood plain of the Bani River. The first mosque on the site was built around the 13th century, but the current structure dates from 1907. [...] "
            "The walls of the Great Mosque are made of sun-baked earth bricks (called ferey), and sand and earth-based mortar, and are coated with a plaster which gives the building its smooth, sculpted look. "
            "The walls of the building are decorated with bundles of rodier palm (Borassus aethiopum) sticks, called toron, that project about 60 cm (2.0 ft) from the surface. "
            "The toron also serve as readymade scaffolding for the annual repairs. [...] "
            "The mosque is built on a platform measuring about 75 m × 75 m (246 ft × 246 ft) that is raised by 3 metres (9.8 feet) above the level of the marketplace. "
            "The platform prevents damage to the mosque when the Bani River floods. [...] "
            "The entire community of Djenné takes an active role in the mosque's maintenance during an annual festival. "
            "This includes music and food, but is mainly to  repair the damage inflicted on the mosque in the past year (mostly erosion caused by the annual rains and cracks caused by changes in temperature and humidity). "
            "In the days before the festival, the plaster is prepared in pits. "
            "It requires several days to cure but needs to be periodically stirred, a task usually falling to young boys who play in the mixture, thus stirring up the contents. "
            "Men climb onto the mosque's built-in scaffolding and ladders made of palm wood and smear the plaster over the face of the mosque. [...] "
            "A race is held at the beginning of the festival to see who will be the first to deliver the plaster to the mosque. "
            "Women and girls carry water to the pits before the festival and to the workmen on the mosque during it. "
            "Members of Djenné's masons guild direct the work, while elderly members of the community, who have already participated in the festival many times, sit in a place of honour in the market square watching the proceedings",
            nome="Great Mosque of Djenné")],
    },
    # 8 o prédio de Londres que derretia carros
    {
        "temas_secundarios": ["luz_cores", "falhas_engenharia"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Em 2013, a fachada curva de um arranha-céu de Londres virou um espelho côncavo e concentrou o sol na rua: derreteu partes de um carro estacionado, e um repórter fritou um ovo na calçada.",
        "explicacao": (
            "O prédio é o 20 Fenchurch Street, apelidado de \"Walkie-Talkie\" porque lembraria o formato do aparelho. "
            "Ainda durante a obra, descobriu-se que, por até duas horas por dia, quando o sol batia direto, a "
            "fachada de vidro curva funcionava como um espelho côncavo e jogava a luz concentrada nas ruas ao sul. "
            "No verão de 2013, foram medidos pontos a 91 °C e a 117 °C, e o feixe refletido chegava a ser seis "
            "vezes mais brilhante que a luz direta do Sol. O dono de um carro estacionado na rua Eastcheap recebeu "
            "946 libras dos empreendedores para consertar a carroceria derretida, e o capacho de uma loja ficou "
            "chamuscado. Um repórter do jornal City A.M. fritou um ovo numa frigideira posta na calçada, e a "
            "imprensa rebatizou o prédio de \"Walkie-Scorchie\" (de scorch, chamuscar) e \"Fryscraper\" (de fry, "
            "fritar). Primeiro vieram telas provisórias nas ruas e, em 2014, um quebra-sol permanente na face sul. "
            "O arquiteto, Rafael Viñoly, já tinha projetado em Las Vegas o hotel Vdara, com um problema parecido, "
            "que funcionários chamavam de \"raio da morte\". Segundo ele, as venezianas horizontais previstas na face "
            "sul para evitar o reflexo foram retiradas em algum momento do planejamento."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("20_Fenchurch_Street",
            "It has been nicknamed \"The Walkie-Talkie\" because of its distinctive shape, said to resemble a walkie-talkie handset. [...] "
            "During the building's construction, it was discovered that for a period of up to two hours each day if the sun shines directly onto the building, it acts as a concave mirror and focuses light onto the streets to the south. "
            "Spot temperature readings at street-level including up to 91 °C (196 °F) and 117 °C (243 °F) were observed during summer 2013: "
            "the reflection of a beam of light up to six times brighter than direct sunlight shined onto the streets below, damaging parked vehicles, including one on Eastcheap whose owner was paid £946 by the developers for repairs to melted bodywork. "
            "Temperatures in direct line with the reflection became so high that City A.M. reporter Jim Waterson used the intense heat to fry an egg in a frying pan set down on the pavement. "
            "The reflection also burned or scorched the doormat of a shop in the affected area. "
            "The media responded by dubbing the building the \"Walkie-Scorchie\" and \"Fryscraper\". [...] "
            "approved plans to erect temporary screening on the streets to prevent similar incidents [...] "
            "In 2014, a permanent awning was installed on the south side of the higher floors of the tower. "
            "The building's architect, Rafael Viñoly, also designed the Vdara hotel in Las Vegas which has a similar sunlight reflection problem that some employees called the \"Vdara death ray\". [...] "
            "Viñoly said that horizontal louvre windows on the south side that had been intended to prevent this problem were removed at some point during the planning process.",
            nome="20 Fenchurch Street")],
    },
    # 9 Monadnock: o limite do prédio de tijolo
    {
        "temas_secundarios": ["grandes_obras", "cidades", "revolucao_industrial"],
        "tipos_espanto": ["escala_absurda", "engenhosidade"],
        "gancho": "O Monadnock, em Chicago, é o prédio mais alto já feito com paredes de tijolo que sustentam o peso: tem 16 andares e paredes de 1,8 m na base. A ampliação, com estrutura de aço, saiu 15% mais barata e 15% mais leve.",
        "explicacao": (
            "Antes do esqueleto de aço, eram as próprias paredes que seguravam o prédio, e quanto mais alto ele "
            "fosse, mais grossas elas tinham de ser embaixo. A metade norte do Monadnock, projetada pela firma "
            "Burnham & Root e iniciada em 1891, levou essa lógica ao limite. Sua altura, 66 metros, foi calculada "
            "como a máxima que ainda compensava com paredes portantes: elas têm 1,8 metro de espessura na base e "
            "46 centímetros no topo. Subir mais exigiria paredes tão grossas que sobraria pouco espaço para alugar. "
            "O arquiteto Root disse ter se inspirado nas linhas pesadas das pirâmides do Egito e quis a "
            "fachada sem um único ornamento. A metade sul, de 1893, já mostra a virada da época. Projetada pela "
            "firma Holabird & Roche, ela usa estrutura de aço e só uma casca fina de tijolo e terracota, o que "
            "permitiu janelas maiores e obra mais rápida. Saiu 15% mais barata, pesou 15% menos e rendeu 15% mais "
            "área para alugar. O peso da metade norte também cobrou seu preço do solo mole de Chicago: o prédio foi "
            "projetado para afundar 20 centímetros, mas em 1948 já tinha afundado 51, criando um degrau para baixo "
            "entre a calçada e o térreo."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Monadnock_Building",
            "is a 16-story skyscraper located at 53 West Jackson Boulevard in the south Loop area of Chicago, Illinois, United States. "
            "The north half of the building was designed by the firm of Burnham & Root and built starting in 1891. "
            "At 215 feet (66 m), it is the tallest load-bearing brick or masonry building ever constructed. [...] "
            "The later south half, constructed in 1893, was designed by Holabird & Roche [...] "
            "declaring that the heavy lines of an Egyptian pyramid had captured his imagination and that he would \"throw the thing up without a single ornament\". [...] "
            "The Monadnock's final height was calculated to be the highest economically viable for a load-bearing wall design, requiring walls 6 feet (1.8 m) thick at the bottom and 18 inches (46 cm) thick at the top. "
            "Greater height would have required walls of such thickness that they would have reduced the rentable space too greatly. [...] "
            "The building reflected in its design the transition taking place in skyscraper design from load-bearing walls to steel frame construction. [...] "
            "The Wachusett was entirely steel framed. "
            "Where the north half required great thicknesses of brick in the load-bearing walls, the addition employed only a thin facing of brick and terracotta trim, affording larger expanses of glass and faster, less expensive construction. "
            "The south half cost 15 percent less, weighed 15 percent less, and had 15 percent more rentable space than the north [...] "
            "the way tall buildings were built on Chicago's spongy soil. [...] "
            "The building was designed to settle 8 inches (200 mm), but by 1905 had settled that much and \"several inches more\", necessitating reconstruction of the first floor. "
            "By 1948, it had settled 20 inches (51 cm), resulting in a step down from the street to the ground floor.",
            nome="Monadnock Building")],
    },
    # 10 Gaudí projetava de cabeça para baixo
    {
        "temas_secundarios": ["geometria_topologia", "revolucao_cientifica"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Para projetar uma igreja, Gaudí pendurou no teto cordas com saquinhos de chumbo e fotografou o resultado. Virada de cabeça para baixo, a forma que a gravidade dava às cordas virava arcos e abóbadas.",
        "explicacao": (
            "O método foi usado na igreja da Colônia Güell, uma das encomendas que Gaudí recebeu do "
            "conde Güell. Gaudí montou uma maquete \"funicular\" em escala 1:10: cordas de cânhamo penduradas no "
            "teto, carregadas com sacos de chumbo que mostravam as cargas que a obra real sofreria, e lonas no "
            "papel de abóbadas e paredes. Depois fotografava o conjunto, invertia a imagem e desenhava por cima, "
            "acrescentando ornamentos. A lógica é antiga. Numa corrente pendurada, as forças são de tração e seguem a própria "
            "corrente; no arco ideal, a análise é a mesma, só que invertida, e a tração vira compressão. Em 1671, "
            "o inglês Robert Hooke anunciou ter achado a forma ideal de um arco e a "
            "escondeu num anagrama em latim, revelado só em 1705 pelo executor do seu testamento: \"assim como "
            "pende o cabo flexível, assim, invertidas, ficam de pé as peças de um arco\". Gaudí usou o mesmo "
            "processo no planejamento da Sagrada Família, e o método o conduziu a formas como paraboloides hiperbólicos e hiperboloides, "
            "comuns em suas obras. Da igreja, só a cripta, construída de 1908 a 1915, ficou pronta, e da maquete "
            "resta apenas uma imagem num livro."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Colònia_Güell",
                "the Church of Colònia Güell was one of several commissions Gaudí received from Count Güell [...] "
                "To start the designing process of the church, Gaudí used his unique process of gravity and rope, known as a funicular system. "
                "As seen in the planning of La Sagrada Família, Gaudí hung hemp ropes attached to lead-filled sacks from the ceiling. "
                "By doing this, it allowed him to reproduce the curves of the church at a 1:10 scale. "
                "Gaudí also used canvas sheets to imitate the vaults and walls of the structure. "
                "By weighing down the ropes with lead-filled sacks, it allowed him to see the loads that would be exerted on the actual structure. "
                "To turn this hanging structure into his actual design, Gaudí photographed his model, flipped the image, and traced over it while adding some ornament and design. "
                "All that remains of the model for Church of Colònia Güell is an image in a book written by architect Josep Francesc Ràfols i Fontanals. "
                "This method of planning led to the development of a new architectural vocabulary, such as hyperbolic paraboloids and hyperboloids, which are prominent elements in many of Gaudi's designs. [...] "
                "The crypt portion of the church, constructed from 1908 to 1915, was the only segment of the church that was fully completed.",
                nome="Colònia Güell"),
            wiki("Catenary",
                "In 1671, Hooke announced to the Royal Society that he had solved the problem of the optimal shape of an arch, and in 1675 published an encrypted solution as a Latin anagram [...] "
                "He did not publish the solution to this anagram in his lifetime, but in 1705 his executor provided it as ut pendet continuum flexile, sic stabit contiguum rigidum inversum, meaning \"As hangs a flexible cable so, inverted, stand the touching pieces of an arch.\" [...] "
                "any force of tension exerted by the chain is parallel to the chain. "
                "The analysis of the curve for an optimal arch is similar except that the forces of tension become forces of compression and everything is inverted.",
                nome="Catenary"),
        ],
    },
    # 11 o Partenon sem linhas retas e o mito da proporção áurea
    {
        "temas_secundarios": ["grecia_antiga", "geometria_topologia", "percepcao_ilusoes"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "O Partenon quase não tem linhas retas: a base se curva para cima no meio e as colunas se inclinam para dentro. Já a ideia de que ele foi projetado com a proporção áurea nunca foi comprovada.",
        "explicacao": (
            "Medições minuciosas feitas no século XIX mostraram que o templo, erguido em Atenas entre 447 e 438 "
            "a.C., foge das linhas retas de várias formas. A plataforma sobre a qual ficam as colunas sobe no centro "
            "10,3 centímetros a cada 70 metros. As colunas engrossam um pouco no meio e afinam para o alto, e tanto "
            "elas quanto as paredes internas se inclinam levemente para dentro. Por que isso foi feito ainda é "
            "discutido. A explicação principal, proposta por Francis Penrose em 1851, é a de correção óptica: os "
            "ajustes convexos compensariam a aparência côncava que objetos vistos em silhueta podem ter para o "
            "olho humano. Outros apontam razões estruturais, e o matemático Alain Goriely chegou a chamar a correção "
            "óptica de mito, dizendo que os ajustes não têm evidência a seu favor ou são pequenos demais para serem percebidos. Já a proporção áurea "
            "tem história bem mais recente. Quem a associou ao Partenon foi o alemão Adolf Zeising, em 1854. "
            "Pesquisas posteriores questionam se os arquitetos gregos conheciam essa razão e notam que a sua "
            "aplicação ao templo é arbitrária, muitas vezes baseada numa figura desenhada sobre uma fotografia, e "
            "não em plantas medidas. Nenhum texto grego antigo de arquitetura sobreviveu para dizer como o templo "
            "foi de fato projetado."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Parthenon",
            "Construction started in 447 BC when the Delian League was at the peak of its power. It was completed in 438 BC [...] "
            "The close measurement of the Parthenon in the nineteenth century revealed that the temple deviated from strict rectilinearity through several optical refinements. "
            "First, the stylobate is curved, bulging upward at the centre—by 10.3 cm over 70 m (a 1/700 ratio) [...] "
            "Second, the columns exhibit entasis, i.e., swelling that reduces toward the top [...] "
            "Third, both the columns and naos walls incline slightly inward. [...] "
            "The primary explanation is based on the Optical Correction or Irradiance Theory, proposed in An Investigation of the Principles of Athenian Architecture by Francis Penrose in 1851. "
            "The theory asserts that convex adjustments were made to counteract the concave appearance silhouetted objects can have to the human eye. "
            "Others attribute the refinements to structural [...] "
            "The mathematician Alain Goriely in a paper titled \"The illusion of illusions: there are no optical corrections in the Parthenon\" has argued the claim of optical refinements is \"one of the oldest and most enduring myths in human history\", "
            "noting that they are \"either unsupported by evidence or too small to have a perceptible effect under typical viewing conditions\". [...] "
            "No ancient Greek text on architecture has survived to the present day. [...] "
            "Perhaps one of the most common beliefs about the system of proportion used on the Parthenon is that of the Golden Ratio Theory. "
            "That the Golden Section, or phi, the ratio of the sum of two values and their larger value, determined the construction of the temple was first articulated by Adolf Zeising in his Neue Lehre von den Proportionen des menschlichen Körpers (1854). [...] "
            "More recent research has questioned whether ancient architects either had knowledge of phi or made use of it, has pointed out that application of the ratio to the Parthenon was somewhat arbitrary in its construction, "
            "and that the basis of the claim was often a geometric figure superimposed on a photograph rather than from measured drawings. "
            "While Zeising’s hypothesis remains unsubstantiated",
            nome="Parthenon")],
    },
    # 12 Epidauro: os degraus que filtram o som
    {
        "temas_secundarios": ["acustica", "grecia_antiga", "teatro_danca"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "No teatro grego de Epidauro, a última fileira ouve bem o palco. Segundo um estudo de 2007, o segredo são os degraus de calcário: eles abafam sons graves, como o burburinho da plateia, e devolvem os agudos.",
        "explicacao": (
            "Construído no fim do século IV a.C., o teatro de Epidauro, com lugar para 13 a 14 mil pessoas, é tido "
            "como o mais perfeito teatro grego antigo em acústica. Para explicar a fama, já se culpou o vento, que "
            "sopra do palco para a plateia, as máscaras dos atores, que funcionariam como alto-falantes primitivos, "
            "o ritmo da fala grega e a inclinação das arquibancadas. Em 2007, Nico Declercq, do Instituto de "
            "Tecnologia da Geórgia, e a engenheira Cindy Dekeyser publicaram outra resposta no periódico da "
            "Sociedade Acústica dos Estados Unidos. Com ultrassom e simulações, eles viram que as fileiras de "
            "assentos seguram as frequências até 500 hertz e deixam passar as mais altas. A superfície ondulada dos "
            "degraus age como os painéis de espuma com relevo usados para tratar o som de paredes. Isso tira o "
            "ruído grave do público, mas também corta parte dos graves da voz dos atores. Quem resolve é o "
            "cérebro: por um fenômeno chamado \"altura virtual\", ele reconstrói as frequências que faltam, o mesmo "
            "que acontece quando ouvimos música num alto-falante pequeno de celular. Para Declercq, os gregos não "
            "entenderam o papel dos assentos, e teatros posteriores com bancos de madeira não conseguiram repetir o "
            "efeito."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": "https://www.sciencedaily.com/releases/2007/04/070404162237.htm",
             "titulo": "Ancient Greek Amphitheater: Why You Can Hear From Back Row (ScienceDaily, a partir de material do Georgia Institute of Technology, 2007)",
             "idioma": "en",
             "trecho": (
                "Date: April 6, 2007 Source: Georgia Institute of Technology [...] "
                "The theater at Epidaurus has been known for centuries as an acoustic marvel that allowed spectators to hear in the back row. [...] "
                "It’s not the slope, or the wind — it’s the seats. "
                "The rows of limestone seats at Epidaurus form an efficient acoustics filter that hushes low-frequency background noises like the murmur of a crowd and reflects the high-frequency noises of the performers on stage off the seats and back toward the seated audience member, carrying an actor’s voice all the way to the back rows of the theater. "
                "The research, done by acoustician and ultrasonics expert Nico Declercq [...] "
                "and Cindy Dekeyser, an engineer who is fascinated by the history of ancient Greece, appears in the April issue of the Journal of the Acoustics Society of America. [...] "
                "There were theories that the site’s wind — which blows primarily from the stage to the audience — was the cause, while others credited masks that may have acted as primitive loudspeakers or the rhythm of Greek speech. "
                "Other more technical theories took into account the slope of the seat rows. [...] "
                "But as Declercq’s team experimented with ultrasonic waves and numerical simulations of the theater’s acoustics, they discovered that frequencies up to 500 Hz were held back while frequencies above 500 Hz were allowed to ring out. "
                "The corrugated surface of the seats was creating an effect similar to the ridged acoustics padding on walls or insulation in a parking garage. [...] "
                "The human brain is capable of reconstructing the missing frequencies through a phenomenon called virtual pitch. "
                "Virtual pitch helps us appreciate the incomplete sound coming from small loudspeakers (in a laptop or a telephone) [...] "
                "The Greeks’ misunderstanding about the role the limestone seats played in Epidaurus’ acoustics likely kept them from being able to duplicate the effect. "
                "Later theaters included different bench and seat materials, including wood, which may have played a large role in the gradual abandonment of Epidaurus’ design"
             )},
            wiki("Theatre_of_Epidaurus",
                "Constructed in the late 4th century BC, it is considered to be the most perfect ancient Greek theatre with regard to acoustics and aesthetics. [...] "
                "At a maximum capacity of 13,000 to 14,000 spectators",
                nome="Theatre of Epidaurus"),
        ],
    },
    # 13 a igrejinha da Pampulha proibida por 14 anos
    {
        "temas_secundarios": ["brasil_republica", "religioes", "pintura"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "A igrejinha da Pampulha, de Oscar Niemeyer, foi inaugurada em 1943, mas ficou 14 anos proibida ao culto: para o arcebispo de Belo Horizonte, aquela construção de curvas era apenas um galpão.",
        "explicacao": (
            "A Igreja de São Francisco de Assis foi o último prédio inaugurado do conjunto da Pampulha, que Niemeyer "
            "projetou em volta de um lago artificial, com um cassino, uma casa de baile e um iate clube. O cálculo "
            "estrutural foi do engenheiro Joaquim Cardozo, e os jardins, de Burle Marx. Na capela, Niemeyer deixou "
            "de lado a laje apoiada em pilares e experimentou uma abóbada parabólica de concreto armado, forma até "
            "então usada em hangares. A abóbada é, ao mesmo tempo, estrutura e parede, e dispensa a alvenaria. "
            "Foi o começo da marca do arquiteto: o concreto em curvas ousadas. O desenho encantou artistas e "
            "arquitetos, mas chocou o meio cultural ainda provinciano da cidade. As autoridades da Igreja não aceitaram "
            "consagrar o templo, tanto pela forma quanto por um painel de Portinari em que um cachorro faz "
            "o papel do lobo ao lado de São Francisco. O arcebispo Dom Antônio dos Santos Cabral via ali só um "
            "galpão. A história terminou ao contrário: a igreja foi tombada pelo patrimônio nacional em 1947, o "
            "conjunto virou Patrimônio Mundial da Unesco em 2016, e em 2021 a \"igrejinha\" foi elevada a santuário "
            "arquidiocesano."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Igreja_de_São_Francisco_de_Assis_(Belo_Horizonte)",
                "popularmente conhecida como Igrejinha da Pampulha [...] "
                "O santuário tem projeto arquitetônico de Oscar Niemeyer, cálculo estrutural do engenheiro Joaquim Cardozo e foi inaugurado em 1943, sendo o último prédio a ser inaugurado do Conjunto Arquitetônico da Pampulha. [...] "
                "No projeto da capela Niemeyer fez novos experimentos em concreto armado, abandonando a laje sob pilotis e criando uma abóbada parabólica em concreto, até então só utilizada em hangares. "
                "A abóbada na capela da Pampulha seria ao mesmo estrutura e fechamento, eliminando a necessidade de alvenarias. "
                "Inicia aquilo que seria a diretriz de toda a sua obra: uma arquitetura onde será preponderante a plasticidade da estrutura de concreto armado, em formas ousadas, inusitadas e marcantes. "
                "As linhas curvas da igreja seduziram artistas e arquitetos, mas escandalizaram o acanhado ambiente cultural da cidade, de tal forma, que as autoridades eclesiásticas não permitiram, por muitos anos, a consagração da capela devido à sua forma inusitada e ao painel de Portinari onde se vê um cachorro representando um lobo junto à São Francisco de Assis. "
                "A igreja permaneceu durante catorze anos proibida ao culto. "
                "Aos olhos do arcebispo Dom Antônio dos Santos Cabral a igrejinha era apenas um galpão. [...] "
                "Os jardins são assinados por Burle Marx. [...] "
                "Em 4 de outubro de 2021 o arcebispo de Belo Horizonte, Dom Walmor Oliveira de Azevedo elevou, em missa solene, a 'Igrejinha' à categoria de Santuário Arquidiocesano. [...] "
                "A igreja foi tombada pelo Instituto do Patrimônio Histórico e Artístico Nacional em 1947 [...] "
                "em 2016, a igreja e o conjunto foram inscritos na lista do patrimônio da humanidade",
                nome="Igreja de São Francisco de Assis (Belo Horizonte)", idioma="pt"),
            wiki("Pampulha_Modern_Ensemble",
                "It was designed around an artificial lake, Lake Pampulha, in the district of Pampulha and includes a casino (currently Pampulha Art Museum), a ballroom (Casa do Baile), the Golf Yacht Club (currently Iate Tênis Clube) and the Church of Saint Francis of Assisi. "
                "The buildings were designed by the architect Oscar Niemeyer",
                nome="Pampulha Modern Ensemble"),
        ],
    },
    # 14 Beauvais: a catedral que passou do limite
    {
        "temas_secundarios": ["europa_medieval", "falhas_engenharia"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Na corrida por catedrais cada vez mais altas, a de Beauvais, na França, passou do limite: parte da abóbada caiu em 1284, e a torre de 153 m, então a construção mais alta do mundo, desabou em 1573.",
        "explicacao": (
            "A obra começou em 1225, e seus construtores queriam a maior catedral gótica da França, à frente de "
            "Amiens e de Notre-Dame de Paris. Sob o bispo Guillaume de Grez, a altura ganhou mais 4,9 metros para "
            "que ela tivesse a abóbada mais alta da Europa. Os contrafortes foram feitos mais finos para deixar "
            "entrar o máximo de luz. Em 1284, parte da abóbada do coro, recém-terminado, desabou. Hoje se acredita "
            "que a causa foram vibrações em ressonância provocadas por ventos fortes. O coro foi refeito na mesma "
            "altura, mas com mais colunas. A ambição voltou no século XVI: em 1569 ficou pronta uma torre de 153 "
            "metros, que fez da igreja a estrutura mais alta do mundo naquele momento. Quatro anos depois, no dia "
            "da Ascensão de 1573, a torre e as abóbadas do cruzeiro vieram abaixo. Houve planos de uma torre ainda "
            "maior, mas o dinheiro acabou. A catedral segue inacabada: só o coro e o transepto foram construídos, e "
            "a nave nunca saiu do papel. No lugar previsto para ela continua de pé o que sobrou da catedral "
            "românica do século X, conhecida como Basse Œuvre, a \"Obra Baixa\"."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Beauvais_Cathedral",
            "From 1569 to 1573 the cathedral of Beauvais was, with its tower of 153 m (502 ft), the highest human construction of the world. "
            "Its designers had the ambition to make it the largest Gothic cathedral in France, ahead of Amiens and Notre-Dame de Paris. "
            "A victim of two collapses, one in the 13th century, the other in the 16th century, it remains unfinished today; only the choir and the transept were built, and the planned nave was never constructed. "
            "The remnant of the previous 10th-century Romanesque cathedral, known as the Basse Œuvre (\"Lower Work\"), still occupies the intended site of the nave. [...] "
            "Construction on the cathedral began in 1225 [...] "
            "Under Bishop Guillaume de Grez, an extra 4.9 m was added to the height to make it the highest-vaulted cathedral in Europe. [...] "
            "Work was interrupted in 1284 by the collapse of some of the vaulting of the recently completed choir. [...] "
            "the choir was rebuilt at the same height, albeit with more columns in the chevet and choir [...] "
            "the 153 m (502 feet) tower in 1569, making the church the tallest structure in the world at that time. "
            "In 1573 on Ascension day, the collapse of the tower and crossing vaults halted work again. "
            "Repairs to transept vaults were rapidly completed and plans were drawn to construct a significantly taller tower than the structure before the collapse, but few additions were made due to a halt in funding. [...] "
            "Even though the structure was planned to be taller, the buttresses were made thinner in order to permit a maximum amount of light into the cathedral. "
            "It is now believed that the vaulting collapse in 1284 was caused by resonant vibrations due to high winds.",
            nome="Beauvais Cathedral")],
    },
    # 15 a casa Winchester não foi feita para fantasmas
    {
        "temas_secundarios": ["personagens_esquecidos", "psicologia_social"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Conta a lenda que a viúva do herdeiro dos rifles Winchester construiu sem parar uma mansão-labirinto para confundir fantasmas. Não há prova disso, e as portas que dão para o nada vêm de um terremoto.",
        "explicacao": (
            "Sarah Winchester, que viveu de 1839 a 1922, ficou viúva de William Wirt Winchester, filho do fundador "
            "da fábrica de rifles, e herdou uma fortuna. Na Califórnia, ergueu uma mansão em San Jose sem arquiteto "
            "de peso: ela mesma desenhava, cômodo por cômodo, sem plano geral, e derrubava o que não lhe agradava. "
            "No auge, a casa teve cerca de 500 cômodos. Desde 1895, jornais locais especularam que ela temia azar, "
            "e depois a morte, se a obra parasse. A versão mais famosa, a de um médium de Boston chamado Adam Coons "
            "que a mandou construir para os espíritos dos mortos pelos rifles, vem de um livro de 1967. "
            "Pesquisadores procuraram esse nome em diretórios da cidade e num periódico espírita da época e não o "
            "acharam. A obra também não era incessante: ela parava às vezes por meses para descansar, e em 1915, quando "
            "parentes passaram quase um ano lá, não houve obra nenhuma. "
            "As esquisitices têm explicações simples. Janelas com grade eram antigas janelas externas que ficaram "
            "para dentro com os acréscimos. Portas e janelas que se abrem para o nada são resultado do terremoto de "
            "1906, que derrubou uma torre de sete andares e a maior parte das chaminés, e ela não reconstruiu. Os "
            "degraus baixinhos foram feitos por causa da saúde dela, que piorava. Quem a conheceu a descrevia como "
            "inteligente, gentil, boa administradora e nada supersticiosa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Winchester_Mystery_House",
                "In Smith's version of events, Winchester visited a medium in Boston named Adam Coons who told her that she and her family were being haunted by the ghosts of people killed by Winchester rifles, that she must construct a house for these ghosts, and that she must never complete the project. [...] "
                "Emily Mace, a scholar, and others have looked through issues of Banner of Light, which was a spiritualist periodical, and in the Boston city directories, which listed spiritualists in the area, and no one named Adam Coons could be found. [...] "
                "Beginning around 1895, Winchester started appearing in newspapers. [...] "
                "The newspapers declared that the reason that the construction was ongoing was that Winchester feared she would have bad luck if the construction would stop. "
                "This theory eventually grew into stories that she believed she would die if construction stopped. [...] "
                "Winchester would take regular breaks from construction to rest, sometimes for months, since she tired easily. [...] "
                "her relatives stayed at the San Jose home for almost a year in 1915 [...] "
                "No construction happened during this time and the staff closed up the house for a week to attend the fair. [...] "
                "Myths around her decision to move from the East Coast to California are thought to have originated from author Susy Smith in her book Prominent American Ghosts, published in 1967. [...] "
                "At its largest the house had approximately 500 rooms. [...] "
                "According to paranormal investigators Nickell and Ignoffo, these house oddities have simple explanations. "
                "The barred windows were previously exterior windows blocked off as the house additions grew. "
                "The doors and windows that opened to nothing resulted from the 1906 earthquake and the severe damage that happened to the house. "
                "The small steps were built because of Winchester's declining health. [...] "
                "After the damage from the earthquake, Winchester did not rebuild the house.",
                nome="Winchester Mystery House"),
            wiki("Sarah_Winchester",
                "Sarah \"Sallie\" Lockwood Winchester (née Pardee; June 4, 1839 – September 5, 1922) was an American heiress [...] "
                "Despite popular rumor claiming the house was built to trap spirits and ghosts that she thought were following her, there is no evidence for these rumors. [...] "
                "Testimonies and records from those who knew her describe her as intelligent, kind, a savvy financial manager, and not superstitious [...] "
                "Damage to Llanada Villa included a seven-story tower; the third- and fourth-floor additions and most of the chimneys collapsed. [...] "
                "Winchester hired at least two architects, but they would not have been of the caliber she was used to from New Haven. [...] "
                "She did all the drawings and design but did not have an overall plan. She worked room by room. "
                "If she was unhappy with the results, she would tear the section down to rebuild [...] "
                "William was the son of a wealthy shirt manufacturer who would later become known for being the founder of the Winchester Repeating Arms Company.",
                nome="Sarah Winchester"),
        ],
    },
]
