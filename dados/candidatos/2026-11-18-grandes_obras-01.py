LOTE = "2026-11-18-grandes_obras-01"
AREA = "tecnologia"
TEMA = "grandes_obras"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o túnel de Eupalinos, cavado pelas duas pontas
    {
        "temas_secundarios": ["grecia_antiga", "geometria_topologia"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "No século 6 a.C., na ilha grega de Samos, duas equipes cavaram um túnel de mais de 1 km pelos dois lados de um morro ao mesmo tempo, guiadas por geometria, e se encontraram no meio da montanha.",
        "explicacao": (
            "A cidade de Samos tinha crescido além do que seus poços e cisternas aguentavam, e a principal fonte de "
            "água doce da ilha ficava do outro lado do monte Kastro. O engenheiro Eupalinos, natural de Mégara, "
            "comandou a abertura de um aqueduto subterrâneo de 1.036 metros, que tinha a vantagem de ficar escondido "
            "de inimigos. Como a galeria era estreita e só cabiam dois escavadores por vez na frente de trabalho, "
            "o túnel foi atacado pelas duas pontas simultaneamente. Pelas contas do pesquisador Hermann Kienast, "
            "a obra levou pelo menos oito anos. É o segundo túnel conhecido cavado a partir das duas extremidades e "
            "o primeiro em que isso foi feito com método geométrico. Para não errar o encontro, Eupalinos desviou as "
            "duas frentes perto do ponto previsto, de modo que se cruzassem quase em ângulo reto, o que aumentava em "
            "17 metros a margem de acerto. Por precaução, também deixou as galerias mais altas perto da junção, mas "
            "o erro vertical acabou sendo de poucos decímetros. Heródoto incluiu o túnel entre as três maiores obras "
            "de engenharia do mundo grego, e ele serviu como aqueduto por 1.100 anos, até se encher de lodo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Tunnel_of_Eupalinos",
            "is a tunnel of 1,036 m (3,399 ft) length running through Mount Kastro in Samos, Greece, built in the 6th century BC to serve as an aqueduct. "
            "The tunnel is the second known tunnel in history which was excavated from both ends [...] "
            "and the first with a geometry-based approach in doing so. [...] "
            "they are responsible for three of the greatest building and engineering feats in the Greek world [...] "
            "by two groups working under the direction of the engineer Eupalinos from Megara [...] "
            "the city of Samos had outgrown the capacity of the wells and cisterns within the city's limits, but the main source of fresh water on the island was on the other side of Mount Kastro from the city. [...] "
            "because the aqueduct ran underground, it could not easily be found by an enemy [...] "
            "The Eupalinian aqueduct was used as an aqueduct for 1100 years, before it began to silt up. [...] "
            "The width of the tunnel means that there would have been space for only two diggers to work at a time. "
            "To speed up the process, the tunnel was dug from both ends simultaneously. "
            "H. J. Kienast calculates that such workers would have been able to dig out 12–15 centimetres (4.7–5.9 in) of stone per day, meaning that the entire tunnel took at least eight years to dig. [...] "
            "Therefore, Eupalinos changed the direction of both tunnels [...] "
            "This gave a catching width that was wider by 17 metres (56 ft), so that a crossing point would be guaranteed, even if the tunnels were previously parallel and far away. "
            "They thus meet at nearly a right angle. [...] "
            "He increased the possibility of the two tunnels meeting each other, by increasing the height of both tunnels at the point near the join. [...] "
            "At the rendezvous, the closing error in altitude for the two tunnels was a few decimeters.",
            nome="Tunnel of Eupalinos")],
    },
    # 2 o túnel sob o Tâmisa e o molusco que fura madeira
    {
        "temas_secundarios": ["biomimetica", "revolucao_industrial", "vida_marinha"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade", "historia_humana"],
        "gancho": "O primeiro túnel construído com sucesso sob um rio navegável, em Londres, usou um escudo de escavação que, segundo se conta, Marc Brunel inventou observando um molusco que perfura madeira, o teredo.",
        "explicacao": (
            "No começo do século 19, as tentativas de cavar sob o Tâmisa tinham fracassado: mineiros acostumados a "
            "rocha dura não adaptaram seus métodos ao barro mole e à areia movediça, e engenheiros concluíram que um "
            "túnel ali era impraticável. O engenheiro Marc Brunel não aceitou a conclusão. Em 1818 ele patenteou o "
            "escudo de escavação, uma enorme armação de ferro dividida em 36 células, cada uma para um operário, que "
            "segurava a terra à frente enquanto pedreiros revestiam de tijolos o trecho de trás. Diz-se que a ideia "
            "veio da concha do teredo, um molusco que ele viu perfurar com eficiência madeira submersa num estaleiro. "
            "A obra durou de 1825 a 1843 e foi perigosa: água do rio, carregada de esgoto, vazava para dentro, e "
            "muitos operários adoeceram. Em 1827 o túnel inundou de repente. Isambard, filho de Brunel, desceu num "
            "sino de mergulho para tapar o rombo no leito do rio com sacos de argila e, depois do conserto, ofereceu "
            "um banquete dentro do túnel. Na inundação seguinte, em 1828, seis homens morreram, e Isambard só "
            "escapou por sorte. Desde 1869 o túnel é usado por trens."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Tunnelling_shield",
                "The first successful rectangular tunnelling shield was developed by Marc Isambard Brunel and patented with Lord Cochrane in January 1818. [...] "
                "Brunel is said to have been inspired in his design by the shell of the shipworm, a mollusc whose efficiency at boring through submerged timber he observed while working in a shipyard.",
                nome="Tunnelling shield"),
            wiki("Thames_Tunnel",
                "It is the first tunnel known to have been constructed successfully underneath a navigable river. "
                "It was built between 1825 and 1843 by Marc Brunel, and his son, Isambard, using the tunnelling shield newly invented by the elder Brunel and Thomas Cochrane. [...] "
                "In 1869 it was converted into a railway tunnel [...] "
                "The Cornish miners were used to hard rock and did not modify their methods for soft clay and quicksand. [...] "
                "The failure of the Thames Archway project led engineers to conclude that \"an underground tunnel is impracticable\". "
                "The Anglo-French engineer Marc Brunel refused to accept this conclusion. [...] "
                "presenting 36 chambers of cells, each for one workman [...] "
                "As the miners worked at one end of the cell, so the bricklayers formed at the other the top, sides and bottom. [...] "
                "The key innovation of the tunnelling shield was its support for the unlined ground in front and around it to reduce the risk of collapses. "
                "However, many workers, including Brunel himself, soon fell ill from the poor conditions caused by filthy sewage-laden water seeping through from the river above. [...] "
                "The tunnel flooded suddenly on 18 May 1827 after 549 ft (167 m) had been dug. "
                "Isambard Kingdom Brunel lowered a diving bell from a boat to repair the hole at the bottom of the river, throwing bags filled with clay into the breach in the tunnel's roof. "
                "Following the repairs and the drainage of the tunnel, he held a banquet inside it. [...] "
                "Six men died when the tunnel flooded again the following year, on 12 January 1828 [...] "
                "Isambard himself was extremely lucky to survive the flooding.",
                nome="Thames Tunnel"),
        ],
    },
    # 3 o terremoto que esticou a ponte Akashi Kaikyō
    {
        "temas_secundarios": ["vulcoes_terremotos", "transportes"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Durante a construção da ponte Akashi Kaikyō, no Japão, um terremoto afastou as duas torres já erguidas, e o vão central teve de ficar 1 metro mais longo do que o projetado.",
        "explicacao": (
            "A ponte pênsil liga Kobe, na ilha de Honshu, à ilha de Awaji, sobre o estreito de Akashi, movimentado "
            "e de águas turbulentas. A ideia de construí-la ganhou força depois de naufrágios em tempestades: o do "
            "Sekirei Maru, em 1945, matou 304 pessoas, e o desastre do Shiun Maru, em 1955, com duas balsas a pique, "
            "matou 168. A obra começou em 1988. Em 17 de janeiro de 1995, o grande terremoto de Hanshin, de "
            "magnitude 7,3 e epicentro a 20 km de Kobe, atingiu a região quando só as duas torres principais estavam "
            "de pé. Elas ficavam a 1.990 metros uma da outra e foram deslocadas pelo tremor, de modo que o vão "
            "central precisou crescer 1 metro. Graças aos métodos antissísmicos, a estrutura não sofreu dano sério, "
            "e a construção terminou no prazo, em 1996. Aberta em 1998, com 1.991 metros de vão central, foi por "
            "anos a ponte pênsil de maior vão do mundo, até ser superada pela ponte de Çanakkale, na Turquia, "
            "inaugurada em 2022. Para enfrentar o vento, as torres têm amortecedores ajustados para operar na "
            "frequência de ressonância da ponte."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Akashi_Kaikyō_Bridge",
            "is a suspension bridge that links the city of Kobe on the Japanese island of Honshu and Iwaya, Awaji on Awaji Island. "
            "It is part of the Kobe-Awaji-Naruto Expressway, and crosses the busy and turbulent Akashi Strait [...] "
            "and at the time, was the longest central span of any suspension bridge in the world, at 1,991 metres (6,532 ft). "
            "Currently, it is the second-longest, behind the 1915 Çanakkale Bridge in Turkey that was opened in March 2022. [...] "
            "The Sekirei Maru sinking in stormy weather in December 1945, while carrying more than three times its capacity of 100 passengers, killed 304 people [...] "
            "In 1955, two ferries sank in the Shiun Maru disaster during a storm, killing 168 people. [...] "
            "Actual construction did not begin until May 1988 [...] "
            "The Great Hanshin Earthquake in January 1995 did not do substantial damage to the bridge due to anti-seismic building methods. "
            "Construction was finished on time in September 1996. "
            "The bridge was opened for traffic on April 5, 1998 [...] "
            "The two towers were originally 1,990 m (6,530 ft) apart, but the Great Hanshin earthquake on January 17, 1995 (magnitude 7.3, with epicenter 20 km west of Kobe) moved the towers (the only structures that had been erected at the time) such that the central span had to be increased by 1 m (3.3 ft). [...] "
            "The bridge also contains tuned mass dampers that are designed to operate at the resonance frequency of the bridge to damp forces.",
            nome="Akashi Kaikyō Bridge")],
    },
    # 4 Tacoma não caiu por ressonância
    {
        "temas_secundarios": ["falhas_engenharia", "acustica"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "A ponte de Tacoma, que desabou em 1940 torcendo-se ao vento, aparece em livros de física como exemplo de ressonância. A explicação está errada: a causa foi o flutter, uma oscilação que se realimenta.",
        "explicacao": (
            "A ponte pênsil sobre o estreito de Tacoma, nos EUA, foi aberta em 1º de julho de 1940. Já durante a "
            "obra o tabuleiro subia e descia tanto com o vento que os operários a apelidaram de \"Galloping Gertie\" "
            "(algo como \"Gertrudes Galopante\"). Em 7 de novembro daquele ano, sob ventos moderados, ela passou a "
            "se torcer, com um lado da pista descendo enquanto o outro subia, até se romper. Morreu um cachorro, "
            "Tubby, que ficou preso num carro, e pessoas se feriram ao fugir. Muitos livros didáticos dizem que o "
            "vento a empurrou no ritmo da sua frequência natural, a ressonância clássica. Em 1991, um trabalho de "
            "Billah e Scanlan mostrou que essa explicação é equivocada. O vento era constante, e a frequência do "
            "movimento destrutivo não batia nem com um modo natural da estrutura nem com a dos vórtices que o vento "
            "soltava. O que houve foi flutter aeroelástico: o movimento da própria ponte, acoplado ao vento, tinha "
            "amortecimento negativo, ou seja, reforçava a oscilação em vez de freá-la. Acima de cerca de 56 km/h de "
            "vento, a amplitude cresceria sem limite, até romper alguma peça vital, no caso os cabos de suspensão. "
            "O desastre impulsionou o estudo da aerodinâmica de pontes, que influenciou todas as grandes pontes "
            "construídas depois."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Tacoma_Narrows_Bridge_(1940)",
            "It opened to traffic on July 1, 1940, and dramatically collapsed into Puget Sound on November 7 of the same year. [...] "
            "From the time the deck was built, it began to move vertically in windy conditions, so construction workers nicknamed the bridge \"Galloping Gertie\". [...] "
            "the deck oscillated in an alternating twisting motion that gradually increased in amplitude until the deck tore apart. "
            "The violent swaying and eventual collapse resulted in the death of a Cocker Spaniel named \"Tubby\", as well as inflicting injuries on people fleeing the disintegrating bridge or attempting to rescue the stranded dog. [...] "
            "In many physics textbooks, the event is presented as an example of elementary forced mechanical resonance, but it was more complicated in reality; "
            "the bridge collapsed because moderate winds produced aeroelastic flutter that was self-exciting and unbounded: "
            "for any constant sustained wind speed above about 35 mph (56 km/h), the amplitude of the (torsional) flutter oscillation would continuously increase, with a negative damping factor, i.e., a reinforcing effect, opposite to damping. "
            "The collapse boosted research into bridge aerodynamics-aeroelastics, which has influenced the designs of all later long-span bridges. [...] "
            "whereby when the left side of the roadway went down, the right side would rise, and vice versa [...] "
            "Eventually, the amplitude of the motion produced by the fluttering increased beyond the strength of a vital part, in this case the suspender cables. [...] "
            "Billah and Scanlan (1991) reported that, in fact, many physics textbooks (for example Resnick et al. and Tipler et al.) wrongly explain that the cause of the failure of the Tacoma Narrows bridge was externally forced mechanical resonance. [...] "
            "According to Farquharson, the wind was steady at 42 miles per hour (68 km/h) and the frequency of the destructive mode was 12 cycles/minute (0.2 Hz). "
            "This frequency was neither a natural mode of the isolated structure nor the frequency of blunt-body vortex shedding of the bridge at that wind speed",
            nome="Tacoma Narrows Bridge (1940)")],
    },
    # 5 Hoover: 125 anos para esfriar e nenhum corpo no concreto
    {
        "temas_secundarios": ["quimica_cotidiano", "termodinamica", "energia"],
        "tipos_espanto": ["escala_absurda", "engenhosidade", "mito_desmentido"],
        "gancho": "Se a represa Hoover tivesse sido concretada de uma vez só, o concreto levaria 125 anos para esfriar e racharia. A solução foi erguê-la em blocos, resfriados por canos com água gelada.",
        "explicacao": (
            "Concreto esquenta e se contrai enquanto cura. Numa estrutura do tamanho da represa Hoover, erguida nos "
            "EUA entre 1931 e 1936, o resfriamento desigual seria um desastre: engenheiros do Bureau of Reclamation "
            "calcularam que, numa concretagem contínua, a massa levaria 125 anos para esfriar, e as tensões fariam "
            "a barragem rachar e se desfazer. Por isso, o terreno foi riscado em retângulos e o concreto foi "
            "despejado em colunas de blocos, alguns com 15 metros de lado e 1,5 metro de altura. Cada camada levava "
            "uma rede de canos de aço de 25 mm, por onde corria primeiro água do rio e depois água gelada de uma "
            "usina de refrigeração. Quando um bloco terminava de curar e parava de encolher, os canos eram "
            "preenchidos com argamassa, que também selava as frestas finas entre as colunas. O jeito de concretar "
            "desmente uma lenda conhecida, a de operários soterrados na barragem até hoje: cada caçamba aumentava a "
            "camada de concreto de um bloco em apenas 25 mm, e os engenheiros não admitiriam o defeito que um corpo "
            "causaria. A obra, ainda assim, teve 112 mortes registradas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Hoover_Dam",
            "Since concrete heats and contracts as it cures, the potential for uneven cooling and contraction of the concrete posed a serious problem. "
            "Bureau of Reclamation engineers calculated that if the dam were to be built in a single continuous pour, the concrete would take 125 years to cool, and the resulting stresses would cause the dam to crack and crumble. "
            "Instead, the ground where the dam would rise was marked with rectangles, and concrete blocks in columns were poured, some as large as 50 ft square (15 m) and 5 feet (1.5 m) high. "
            "Each five-foot form contained a set of 1-inch (25 mm) steel pipes; cool river water would be poured through the pipes, followed by ice-cold water from a refrigeration plant. "
            "When an individual block had cured and had stopped contracting, the pipes were filled with grout. "
            "Grout was also used to fill the hairline spaces between columns [...] "
            "Although there are myths that men were caught in the pour and are entombed in the dam to this day, each bucket deepened the concrete in a form by only 1 inch (25 mm), and Six Companies engineers would not have permitted a flaw caused by the presence of a human body. [...] "
            "There were 112 deaths reported as associated with the construction of the dam. [...] "
            "ween 1931 and 1936, during the Great Depression",
            nome="Hoover Dam")],
    },
    # 6 Vajont: a represa aguentou, o vale não
    {
        "temas_secundarios": ["falhas_engenharia", "geologia_profunda", "vulcoes_terremotos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1963, a represa de Vajont, na Itália, resistiu quase intacta, e mesmo assim matou cerca de 2 mil pessoas: um deslizamento no lago ergueu uma onda de 250 m que passou por cima da barragem.",
        "explicacao": (
            "A barragem, com 262 metros de altura, uma das mais altas do mundo, foi construída entre 1957 e 1960 no "
            "vale do rio Vajont, sob o monte Toc, cerca de 100 km ao norte de Veneza. Avisos não faltaram. Em 1959 "
            "já se notavam deslocamentos e fraturas no chão da encosta do monte. Em 1962, testes em modelo feitos "
            "pelos próprios engenheiros da empresa indicaram que uma onda causada por deslizamento poderia passar "
            "por cima da crista se o lago estivesse a 20 metros ou menos dela. Em vez de ouvir os alertas, o governo "
            "italiano processou os jornalistas que noticiavam os problemas. Em 9 de outubro de 1963, durante o "
            "enchimento do lago, a encosta desabou no reservatório. O impacto deslocou cerca de 115 milhões de "
            "metros cúbicos de água, e 50 milhões passaram por cima da barragem numa onda de 250 metros. A água "
            "arrasou Longarone e outros vilarejos do vale do Piave; as estimativas de mortos vão de 1.900 a 2.500. "
            "A barragem perdeu só cerca de 1 metro do topo, reteve dois terços da água e continua de pé, desativada."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Vajont_Dam",
            "is a disused hydro-electric dam in the valley of the Vajont river under Monte Toc, in the municipality of Erto e Casso, 100 kilometres (60 mi) north of Venice, Italy. "
            "It is one of the tallest dams in the world, with a height of 262 m (860 ft). "
            "The dam was conceived in the 1920s and eventually built between 1957 and 1960 [...] "
            "On 9 October 1963, during initial filling of the lake, a landslide caused a megatsunami in which 50,000,000 m3 (1.8×109 cu ft) of water overtopped the dam in a wave of 250 m (820 ft), bringing massive flooding and destruction to the Piave Valley below, destroying several villages and towns, causing  an estimated 1,900 to 2,500 deaths. "
            "The dam remained almost intact and two-thirds of the water was retained behind it. [...] "
            "By 1959, shifts and fractures in the ground were noticed while building a new road on the side of Monte Toc. [...] "
            "Instead of heeding these warning signs, the Italian government chose to sue the handful of journalists reporting the problems [...] "
            "In July 1962, SADE's own engineers reported the results of model-based experiments on the effects of further landslides from Monte Toc into the lake. "
            "The tests indicated that a wave generated by a landslide could overtop the crest of the dam if the water level was 20 m (66 ft) or less from the dam crest. [...] "
            "The impact displaced 115×10^6 m3 (4,100×10^6 cu ft) of water in about 25 seconds, 50×10^6 m3 (1,800×10^6 cu ft) of which overtopped the dam in a 250-metre-high (820 ft) wave. [...] "
            "The death toll was about 2,000 people [...] "
            "The top 1 m (3.3 ft) or so of masonry was washed away, but the basic structure remained intact and is standing today. [...] "
            "In the Piave Valley the wave destroyed the villages of Longarone, Pirago, Rivalta, Villanova, and Faè, killing approximately 2,000 people",
            nome="Vajont Dam")],
    },
    # 7 Chicago levantou a cidade com macacos de rosca
    {
        "temas_secundarios": ["cidades", "doencas_infecciosas"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Nos anos 1850 e 1860, Chicago ergueu prédios inteiros com macacos de rosca para subir o nível da cidade. Num hotel de seis andares, alguns hóspedes nem perceberam que o prédio estava subindo.",
        "explicacao": (
            "Chicago nasceu num terreno pantanoso, pouco mais alto que a margem do lago Michigan. Sem drenagem, a "
            "água parada favorecia epidemias, e a de cólera de 1854 matou 6% da população. Em 1856, o engenheiro "
            "Ellis Chesbrough propôs uma rede de esgotos para a cidade inteira. Para executá-la, operários "
            "assentaram os drenos, cobriram ruas e calçadas com camadas de terra de vários pés e ergueram a maioria "
            "dos prédios até o novo nível. Em 1858, um edifício de tijolos de quatro andares e 680 toneladas subiu "
            "1,88 m apoiado em 200 macacos, sem dano algum. Em 1860, meia quadra da Lake Street, com cerca de 32 mil "
            "toneladas, foi elevada 1,42 m em cinco dias por 600 homens com 6 mil macacos, e lojas e escritórios "
            "seguiram abertos durante a operação. No ano seguinte foi a vez do Tremont House, um hotel de luxo de "
            "seis andares: um hóspede estranhou que a escada da entrada ficava mais íngreme a cada dia. Muitas casas "
            "de madeira, em vez de erguidas, foram postas sobre roletes e levadas para a periferia, às vezes com "
            "gente comendo e trabalhando lá dentro durante a viagem."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Raising_of_Chicago",
            "During the 1850s and 1860s, engineers carried out a piecemeal raising of the grade of central Chicago to lift the city out of its low-lying swampy ground. "
            "Buildings and sidewalks were raised on jackscrews. [...] "
            "During the 19th century, the elevation of the Chicago area was only a little higher than the shoreline of Lake Michigan. [...] "
            "culminating in the 1854 outbreak of cholera that killed six percent of the city’s population. [...] "
            "In 1856, engineer Ellis S. Chesbrough drafted a plan for the installation of a citywide sewerage system [...] "
            "Workers then laid drains, covered and refinished roads and sidewalks with several feet of soil, and raised most buildings on screwjacks to the new grade. [...] "
            "In January 1858, the first masonry building in Chicago to be thus raised—a four-story, 70-foot-long (21 m), 750-ton (680 metric tons) brick structure situated at the northeast corner of Randolph Street and Dearborn Street—was lifted on two hundred jackscrews to its new grade, which was 6 feet 2 inches (1.88 m) higher than the old one, “without the slightest injury to the building.” [...] "
            "an estimated total weight—including hanging sidewalks—of 35,000 short tons (32,000 t). "
            "Businesses operating in these premises were not closed down during the operation [...] "
            "In five days the entire assembly was elevated 4 feet 8 inches (1.42 m), by a team consisting of 600 men using 6,000 jackscrews [...] "
            "In 1861 a consortium of engineers Ely, Smith and Pullman led a team that raised the Tremont House hotel [...] "
            "This six-story brick building was luxuriously appointed [...] "
            "Some of the guests staying there at the time—among whose number were several VIPs and a US Senator— were oblivious to the process [...] "
            "One patron was puzzled to note that the front steps leading from the street into the hotel were becoming steeper every day [...] "
            "on rollers and moving them to the outskirts of town or to the suburbs was so common as to be considered nothing more than routine traffic. [...] "
            "with people dining, shopping and working in these buildings as they were rolled down the street.",
            nome="Raising of Chicago")],
    },
    # 8 o rio de Chicago corre ao contrário
    {
        "temas_secundarios": ["agua_doce_gelo", "cidades", "ecologia"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Em 1900, Chicago fez seu rio correr ao contrário: em vez de desaguar no lago Michigan, de onde a cidade tira a água que bebe, ele passou a levar o esgoto para o interior, rumo ao Mississippi.",
        "explicacao": (
            "O esgoto de Chicago ia para o rio Chicago, que desembocava no lago Michigan, onde ficam as tomadas de "
            "água potável da cidade, a cerca de 3,2 km da margem. O medo de surtos de tifo, cólera e disenteria "
            "cresceu depois de uma grande tempestade, em 1885, que lavou os dejetos do rio lago adentro. (Relatos "
            "de uma epidemia de cólera naquele ano, porém, não são verdadeiros.) O engenheiro Isham Randolph notou "
            "que uma elevação a cerca de 19 km do lago separava a bacia dos Grandes Lagos da bacia do Mississippi, "
            "passagem que os povos indígenas já usavam desde antes da chegada dos europeus. O plano foi cortar essa "
            "divisa com um canal de 51 km. Aberto em janeiro de 1900, à frente de uma tentativa do Missouri de "
            "barrá-lo na Justiça, o canal inverteu o rio e mandou o esgoto diluído em água do lago para o interior, "
            "até o golfo do México. Foi a maior obra de movimentação de terra feita na América do Norte até então, "
            "e formou engenheiros que depois trabalharam no canal do Panamá. O efeito colateral veio um século "
            "depois: a ligação virou caminho possível para carpas asiáticas invasoras chegarem aos Grandes Lagos, "
            "e foi preciso instalar uma barreira elétrica no canal."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Chicago_Sanitary_and_Ship_Canal",
            "is a 32-mile-long (51 km) canal system that connects the Chicago River to the Des Plaines River in Northeast Illinois, US. "
            "It reverses the direction of the Main Stem and the South Branch of the Chicago River, which now flows out of Lake Michigan rather than into it. [...] "
            "Prior to its opening in 1900, sewage from the city of Chicago was discharged into the Chicago River and flowed into Lake Michigan. [...] "
            "the decision was made to reverse the flow of the river, thereby sending all the sewage inland diluted with lake water [...] "
            "The building of the Chicago canal served as intensive and practical training for engineers who later built the Panama Canal. [...] "
            "The city's water supply also comes from the lake, through water intake cribs located two miles (3.2 km) offshore. "
            "There were fears that sewage could infiltrate the water supply, leading to typhoid fever, cholera, and dysentery. [...] "
            "During a tremendous storm in 1885, the rainfall washed refuse from the river far out into the lake (although reports of an 1885 cholera epidemic are untrue) [...] "
            "Engineer Isham Randolph noted that a ridge about 12 miles (19 km) from the lakeshore divided the Mississippi River drainage system from the Great Lakes drainage system. "
            "This low divide had been known since pre-Columbian time by the Native Americans [...] "
            "through the Des Plaines and Illinois rivers, to the Mississippi River and the Gulf of Mexico. [...] "
            "and in advance of an application by the Missouri Attorney General for an injunction against the opening, opened on January 2, 1900. [...] "
            "Construction of the Ship and Sanitary Canal was the largest earth-moving operation that had been undertaken in North America up to that time. [...] "
            "On November 20, 2009, the Corps of Engineers announced a single sample of DNA from Asian carp had been found above the electric barrier constructed in the canal in an attempt to prevent carp from migrating into the Great Lakes. [...] "
            "It migrated through the Mississippi River system, and could make its way into the Great Lakes, through the man-made canal.",
            nome="Chicago Sanitary and Ship Canal")],
    },
    # 9 Sete Quedas, afogadas por Itaipu
    {
        "temas_secundarios": ["biomas_brasileiros", "agua_doce_gelo", "energia"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "As Sete Quedas, no rio Paraná, estavam entre as cachoeiras de maior vazão do planeta. Em 1982, o lago de Itaipu as cobriu em apenas 14 dias, e Drummond publicou um poema de despedida.",
        "explicacao": (
            "Eram 18 cataratas reunidas em sete grupos, daí o nome, na fronteira entre Brasil e Paraguai, perto de "
            "Guaíra, no Paraná. Ali o rio, com uns 380 metros de largura, se espremia num cânion de 60 metros. O "
            "desnível total chegava a cerca de 114 metros, e o estrondo da água podia ser ouvido a 30 km. As "
            "estimativas de vazão publicadas variam muito, de 13 mil a 50 mil metros cúbicos por segundo. Os dois "
            "países reivindicavam as quedas, e o acordo de 1973 para construir Itaipu inaugurou uma fase de "
            "cooperação entre eles. Enquanto a obra avançava, milhares de pessoas foram vê-las uma última vez. Em 17 "
            "de janeiro de 1982, uma passarela suspensa desabou e matou dezenas de turistas. Quando as águas "
            "começaram a subir, centenas de pessoas fizeram um quarup, ritual indígena de homenagem aos mortos, em "
            "memória das quedas. A inundação, na época das cheias, levou só 14 dias. Carlos Drummond de Andrade "
            "publicou no Jornal do Brasil um poema que ocupou uma página inteira, lamentando um movimento que vira "
            "represa. Já o diretor da construtora disse que as quedas não estavam sendo destruídas, só "
            "\"transferidas\" para o vertedouro de Itaipu."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Guaíra_Falls",
            "were a series of immense waterfalls on the Paraná River along the border between Paraguay and Brazil. "
            "The falls ceased to exist in 1982 when they were inundated by the impoundment of the Itaipu Dam reservoir. "
            "While published figures vary, ranging from 13,000 m3 (470,000 cu ft) per second to 50,000 m3 (1,750,000 cu ft) per second, Guaíra's flow rate was among the greatest of any then-existing falls on Earth. "
            "The falls comprised 18 cataracts clustered in seven groups—hence their Portuguese name, Sete Quedas (Seven Falls)—near the Brazilian municipality of Guaíra, Paraná [...] "
            "At the head of the falls, the river narrowed sharply from a width of about 380 m (1,250 ft) to 60 m (200 ft). "
            "The total height of the falls was approximately 114 m (375 ft) [...] "
            "The roar of the plunging water could be heard from 30 km (20 mi) away. [...] "
            "The building of the dam, authorized by a 1973 bilateral agreement between the Paraguayan and Brazilian regimes of the time, marked a new era of cooperation between the countries, both of which had claimed ownership of Guaíra Falls. "
            "As construction of the Itaipu Dam progressed, thousands of visitors flocked to the area to see the falls before they disappeared forever. "
            "Disaster struck on January 17, 1982, when a suspended footbridge affording access to a particularly spectacular view of the falls collapsed, killing dozens of tourists. "
            "Brazilian poet Carlos Drummond de Andrade wrote a poem expressing his dismay at the destruction of Guaíra Falls. "
            "Set in large type, the poem filled an entire page in the Jornal do Brasil newspaper [...] "
            "A movement becomes a dam. [...] "
            "a demonstration took place, as hundreds of people gathered to participate in a quarup, an indigenous ritual of remembrance for the dead, in memory of the falls. "
            "The inundation took only 14 days, occurring during the rainy season when the level of the Paraná River was high. [...] "
            "The director of the company that built the dam was quoted as saying, \"We're not destroying Seven Falls. We're just going to transfer it to Itaipu Dam, whose spillway will be a substitute for [the falls'] beauty\".",
            nome="Guaíra Falls")],
    },
    # 10 a Roda de Falkirk e o princípio de Arquimedes
    {
        "temas_secundarios": ["transportes", "estados_materia", "energia"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "A Roda de Falkirk, na Escócia, ergue barcos 24 m girando. Pelo princípio de Arquimedes, os dois lados pesam sempre o mesmo, e meia volta gasta a energia de ferver cerca de oito chaleiras.",
        "explicacao": (
            "Os canais Forth and Clyde e Union, no centro da Escócia, eram ligados por uma escada de 11 eclusas que "
            "vencia 35 metros de desnível, gastava 3.500 toneladas de água a cada passagem e tomava quase um dia "
            "inteiro. As eclusas caíram em desuso e foram desmontadas em 1933. Para religar os canais, foi inaugurado "
            "em 2002 um elevador giratório de barcos, o único do tipo no mundo. Dois braços opostos sustentam, um "
            "em cada ponta, dois tanques cheios de água, as gôndolas, que sempre carregam juntos 500 toneladas de "
            "água e barcos. O segredo do equilíbrio é o princípio de Arquimedes: um corpo que flutua desloca o "
            "próprio peso em água. Quando um barco entra numa gôndola, sai dela uma quantidade de água que pesa "
            "exatamente o mesmo que o barco, e os dois braços continuam equilibrados, desde que os níveis sejam "
            "mantidos iguais, com diferença máxima de 37 mm. Com isso, dez motores hidráulicos consomem só 1,5 kWh "
            "por meia volta. Um jogo de engrenagens gira as gôndolas no sentido oposto ao dos braços, na mesma "
            "velocidade, e assim elas ficam sempre niveladas. Mesmo erguendo 24 metros, a roda não basta: os barcos "
            "ainda passam por duas eclusas para chegar ao canal Union."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Falkirk_Wheel",
            "is a rotating boat lift in Tamfourhill, Falkirk, in central Scotland, connecting the Forth and Clyde Canal with the Union Canal. "
            "It opened in 2002 [...] "
            "The wheel raises boats by 24 metres (79 ft), but the Union Canal is still 11 metres (36 ft) higher than the aqueduct which meets the wheel. "
            "Boats must also pass through a pair of locks between the top of the wheel and the Union Canal. "
            "The Falkirk Wheel is the only rotating boat lift of its kind in the world [...] "
            "The two canals served by the wheel were previously connected by a series of 11 locks. "
            "With a 35-metre (115 ft) difference in height, it required 3,500 tonnes (3,400 long tons; 3,900 short tons) of water per run and took most of a day to pass through the flight. "
            "By the 1930s these locks had fallen into disuse, and were dismantled in 1933. [...] "
            "Two diametrically opposed water-filled caissons [...] "
            "The caissons, or gondolas, always carry a combined weight of 500 tonnes (490 long tons; 550 short tons) of water and boats [...] "
            "According to Archimedes' principle, floating objects displace their own weight in water, so when the boat enters, the amount of water leaving the caisson weighs exactly the same as the boat. "
            "Site-wide computer control system maintain the water levels on each side to within a difference of 37 mm (1.5 in) [...] "
            "It takes 22.5 kilowatts (30.2 hp) to power ten hydraulic motors, which consume 1.5 kilowatt-hours (5,100 BTU) per half-turn, roughly the same as boiling eight kettles of water. [...] "
            "The smaller gears engage the large ring gears at the end of the caissons, driving them at the same speed as the wheel but in the opposite direction. "
            "This cancels the rotation due to the arms and keeps the caissons stable and perfectly level.",
            nome="Falkirk Wheel")],
    },
    # 11 Emily Roebling e a ponte do Brooklyn
    {
        "temas_secundarios": ["personagens_esquecidos", "corpo_extremo"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "O projetista da ponte do Brooklyn morreu após um acidente na obra, e o filho que o substituiu ficou de cama com a doença da descompressão. Quem tocou a construção por uma década foi a nora, Emily Roebling.",
        "explicacao": (
            "A ponte foi projetada por John A. Roebling, que morreu de tétano em 1869, depois de um acidente no "
            "canteiro. O filho, Washington Roebling, assumiu como engenheiro-chefe e mergulhou no trabalho, "
            "literalmente: descia às câmaras pressurizadas sob a água, os caixões, onde se escavavam as fundações. "
            "Por subir sem respeitar o ritmo certo, desenvolveu a doença da descompressão, então chamada \"doença "
            "dos caixões\", e ficou acamado. A mulher dele, Emily Warren Roebling, era a única pessoa que o visitava. "
            "Ela passou a levar as instruções do marido aos assistentes e a trazer notícias da obra. Com as aulas "
            "dele, aprendeu resistência dos materiais, análise de tensões, construção de cabos e cálculo de curvas "
            "catenárias. Na década seguinte, assumiu boa parte das funções de engenheiro-chefe, como a supervisão "
            "diária e a gestão do projeto, e negociava com políticos e engenheiros concorrentes, a ponto de muita "
            "gente achar que o projeto era dela. Em 1882, quando o cargo do marido ficou ameaçado pela doença, ela "
            "o defendeu e conseguiu mantê-lo. A ponte ficou pronta em 1883, e Emily foi a primeira a atravessá-la "
            "de carruagem, levando um galo como símbolo de vitória."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Emily_Warren_Roebling",
            "was an engineer known for her contributions over a period of more than 10 years to the completion of the Brooklyn Bridge after her husband Washington Roebling developed caisson disease (a.k.a. decompression sickness) and became bedridden. [...] "
            "Her husband was the chief engineer during construction of the Brooklyn Bridge, which had been designed by his late father, John A. Roebling. [...] "
            "Washington's father died in 1869 of tetanus, following an accident at the bridge site. "
            "Washington Roebling was assigned as chief engineer of the Brooklyn Bridge's construction. "
            "As he immersed himself in the project, Washington developed decompression sickness, which was known at the time as \"caisson disease\", by going to underwater depths to study the placement of caissons and not rising at the proper speed. "
            "It affected him so severely that he became bedridden. "
            "As the only person to visit her husband during his sickness, Emily Roebling relayed information from Washington to his assistants and reported to him the progress of work on the bridge. "
            "She developed an extensive knowledge of strength of materials, stress analysis, cable construction, and calculating catenary curves through Washington's teachings. [...] "
            "For the decade after Washington was confined to his sick bed, Roebling was dedicated to the completion of the Brooklyn Bridge. "
            "She took over much of the chief engineer duties, including day-to-day supervision and project management. [...] "
            "She dealt with politicians, competing engineers, and all those associated with work on the bridge,  to the point where people believed she was behind the bridge's design. "
            "In 1882, Washington's title of chief engineer was in jeopardy because of his extended illness. [...] "
            "the politicians responded well and permitted Washington to remain chief engineer of the Brooklyn Bridge. "
            "The Brooklyn Bridge was completed in 1883. "
            "In advance of the official opening, carrying a rooster as a sign of victory, Emily Roebling was the first to cross the bridge by carriage.",
            nome="Emily Warren Roebling")],
    },
    # 12 represas que provocam terremotos
    {
        "temas_secundarios": ["vulcoes_terremotos", "geologia_profunda", "agua_doce_gelo"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Encher uma grande represa pode provocar terremotos. Em 1967, um tremor de magnitude 6,3 com epicentro perto ou embaixo do reservatório de Koyna, na Índia, matou 180 pessoas.",
        "explicacao": (
            "Num lago artificial grande e fundo, o peso da coluna de água altera as tensões sobre falhas e fraturas "
            "que já existem na rocha. Isso acontece de dois jeitos: a água aumenta a carga direta sobre a falha e, "
            "ao elevar a pressão nos poros da rocha, reduz a tensão efetiva que mantém os blocos travados. A mudança "
            "pode fazer a falha escorregar de repente, gerando um sismo. O primeiro caso registrado foi em 1932, na "
            "barragem de Oued Fodda, na Argélia. O terremoto de Koynanagar, em 1967, teve epicentro, abalos "
            "precursores e réplicas todos perto ou embaixo do reservatório de Koyna; deixou 180 mortos e 1.500 "
            "feridos e foi sentido a 230 km de distância. Esse tipo de sismicidade parece aparecer em represas com "
            "mais de 100 metros de altura e pode surgir logo depois de encher ou esvaziar o lago, ou com algum "
            "atraso. A ciência do fenômeno ainda é limitada, mas a pressão extra da água é a explicação mais aceita. "
            "Há casos polêmicos: um artigo na revista Science sugeriu que a construção e o enchimento da represa de "
            "Zipingpu podem ter desencadeado o terremoto de Sichuan, em 2008, que matou cerca de 68 mil pessoas."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Induced_seismicity",
            "The column of water in a large and deep artificial lake alters in-situ stress along an existing fault or fracture. "
            "In these reservoirs, the weight of the water column can significantly change the stress on an underlying fault or fracture by increasing the total stress through direct loading, or decreasing the effective stress through the increased pore water pressure. "
            "This significant change in stress can lead to sudden movement along the fault or fracture, resulting in an earthquake. [...] "
            "Though understanding of reservoir-induced seismic activity is very limited, it has been noted that seismicity appears to occur on dams with heights larger than 330 feet (100 m). "
            "The extra water pressure created by large reservoirs is the most accepted explanation for the seismic activity. "
            "When the reservoirs are filled or drained, induced seismicity can occur immediately or with a small time lag. "
            "The first case of reservoir-induced seismicity occurred in 1932 in Algeria's Oued Fodda Dam. "
            "The 6.3 magnitude 1967 Koynanagar earthquake occurred in Maharashtra, India with its epicenter, fore- and aftershocks all located near or under the Koyna Dam reservoir. "
            "180 people died and 1,500 were left injured. "
            "The effects of the earthquake were felt 140 mi (230 km) awa [...] "
            "The 2008 Sichuan earthquake, which caused approximately 68,000 deaths, is another possible example. "
            "An article in Science suggested that the construction and filling of the Zipingpu Dam may have triggered the earthquake.",
            nome="Induced seismicity")],
    },
    # 13 a Ferrovia do Diabo
    {
        "temas_secundarios": ["brasil_republica", "amazonia", "fronteiras_paises"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "A ferrovia Madeira-Mamoré, em Rondônia, foi parte do preço pago pelo Acre e ganhou o apelido de Ferrovia do Diabo pelas mortes na obra. Pouco depois de pronta, em 1912, o ciclo da borracha que a justificava acabou.",
        "explicacao": (
            "As corredeiras do rio Madeira impediam a navegação, e a ideia era contorná-las por trilhos para levar "
            "produtos da Bolívia, sobretudo borracha, até o Atlântico pela Amazônia. Nos anos 1870, o americano "
            "George Earl Church tentou duas vezes e fracassou, vencido pelo terreno e por um número terrível de "
            "mortes por malária, acidentes e violência. A obra só saiu do papel com o Tratado de Petrópolis, de "
            "1903: a Bolívia cedeu o Acre ao Brasil em troca de território, de um pagamento e da promessa de uma "
            "ferrovia que contornasse as corredeiras. A construção foi de 1907 a 1912, ligando Porto Velho a "
            "Guajará-Mirim. Não há números precisos de mortos: o governo brasileiro estima 6 mil, um escritor fala "
            "em 7 mil a 10 mil e um livro passa de 30 mil. Parte da lenda, porém, vem das tentativas anteriores de "
            "Church, mais mortíferas, e do próprio ciclo da borracha. Com a concorrência da borracha asiática e da "
            "sintética, o ciclo terminou e a ferrovia ficou sem função. O Brasil teve de mantê-la por causa do "
            "tratado, até que a rodovia BR-364, concluída em 1972, levou ao seu abandono."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Madeira-Mamoré_Railroad",
            "is an abandoned railroad built in the Brazilian state of Rondônia between 1907 and 1912, during the rubber boom. "
            "The railroad links the cities of Porto Velho and Guajará-Mirim. "
            "It became known as the \"Devil's Railroad\" because thousands of construction workers died from tropical diseases and violence. [...] "
            "contracted Lieutenant Lardner Gibbon to study the viability of a rail link between the navigable Amazon River and Bolivian production centres. [...] "
            "During the 1870s, the American George Earl Church made two attempts to overcome the Madeira River rapids in order to gain access to Bolivian rubber markets. "
            "Both efforts were defeated by the difficult terrain and by appalling loss of life to malaria, accidents, and violence. "
            "A successful bid to build the railroad began with the Treaty of Petrópolis (1903) whereby Bolivia gave Brazil the territory of Acre (191,000 km²), in exchange for Brazilian territory, a monetary payment, and a pledge that Brazil would build a rail link to bypass the rapids on the Madeira river. "
            "Construction began in 1907, and on April 30, 1912, the final leg of the Madeira-Mamoré Railway was inaugurated. [...] "
            "There are no accurate figures for the number of lives lost during the construction of the railroad. "
            "In his book Brazil, novelist Errol Lincoln Uys puts the number between 7,000 and 10,000. "
            "The Brazilian government estimates 6,000 workers lost their lives. "
            "Fiorelo Picoli in his book, O Capital e a Devastação da Amazônica, puts the figure at more than 30,000. [...] "
            "However, much of the \"devil's railroad\" legend is based on the much deadlier failed attempts by George Church, and on the Brazilian rubber boom itself, which cost tens of thousands of lives. [...] "
            "The South American rubber boom ended because of competition from Asian producers and synthetic rubber, and the railroad became redundant. "
            "Initially, the Brazilian government was forced to maintain the superfluous facilities because of its obligations under the Treaty of Petrópolis. "
            "However, in 1972 Brazil completed the BR-364 linking Bolivia to navigable regions of the Amazon and the railroad was abandoned.",
            nome="Madeira-Mamoré Railroad")],
    },
    # 14 os qanats: túneis de água de 2.700 anos
    {
        "temas_secundarios": ["agua_doce_gelo", "primeiras_civilizacoes", "conservacao"],
        "tipos_espanto": ["engenhosidade", "escala_absurda"],
        "gancho": "No Irã, um túnel de água cavado há cerca de 2.700 anos, o qanat de Gonabad, ainda leva água a quase 40 mil pessoas. Ele percorre 45 km debaixo da terra, movido só pela gravidade.",
        "explicacao": (
            "O qanat surgiu no antigo Irã há cerca de 3 mil anos. É um túnel com leve declive que capta água de um "
            "aquífero e a conduz, por gravidade, até a superfície num ponto mais baixo e às vezes muito distante, "
            "sem precisar de bomba. Ao longo do trajeto, poços verticais servem para tirar a terra escavada e fazer "
            "manutenção; vistos do alto, parecem uma fileira de crateras de bomba. Como a água viaja enterrada, "
            "quase não evapora no calor do deserto, e o sistema resiste bem a enchentes, terremotos e guerras. Em "
            "meados do século 20, havia cerca de 50 mil qanats em uso no Irã; em 2015 restavam 37 mil. O de "
            "Gonabad, um dos mais antigos e maiores, construído entre 700 e 500 a.C., tem 45 km, e seu poço "
            "principal passa de 360 metros de profundidade. A técnica servia também para fazer gelo no deserto: no "
            "inverno, a água do qanat era desviada para a sombra de um muro, onde congelava mais depressa, e o gelo "
            "era guardado em poços chamados yakhchal para o verão. O ar que vinha dos túneis ainda resfriava salas "
            "subterrâneas das casas. Sistemas desse tipo se espalharam pela Ásia e pelo norte da África e chegaram "
            "à Espanha muçulmana."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Qanat",
            "is a water supply system that was developed in ancient Iran for the purpose of transporting usable water to the surface from an aquifer or a well through an underground aqueduct. "
            "Originating approximately 3,000 years ago, its function is essentially the same in systems across Asia and North Africa [...] "
            "and were later implemented on a larger scale in Muslim-ruled Spain. [...] "
            "a qanat enables water to be transported over long distances by largely eliminating the risk of much of it evaporating on the journey. "
            "The system also has the advantage of being fairly resistant to natural disasters, such as floods and earthquakes; and to man-made disasters, such as wartime destruction and water supply terrorism. [...] "
            "The typical design of a qanat is a gently sloping tunnel accessed by a  series of well-like vertical shafts visible at ground level. "
            "This taps into groundwater and delivers it to the surface at a lower level some distance away, via gravity, therefore eliminating the need for pumping. [...] "
            "The excavated material is usually transported by means of leather bags up the vertical shafts. [...] "
            "From the air, these shafts look like a string of bomb craters. [...] "
            "In the middle of the 20th century, an estimated 50,000 qanats were in use in Iran, each commissioned and maintained by local users. "
            "Of these, only 37,000 remain in use as of 2015. "
            "One of the oldest and largest known qanats is in the Iranian city of Gonabad, and after 2,700 years still provides drinking and agricultural water to nearly 40,000 people. "
            "Its main well depth is more than 360 meters (1,180 ft) and its length is 45 kilometers (28 mi). [...] "
            "is one of the oldest and largest qanats in the world built between 700 BCE to 500 BCE. [...] "
            "In winter, the qanat water would be channeled to the north side of the wall, whose shade made the water freeze more quickly, increasing the ice formed per winter day. "
            "Then the ice was stored in yakhchals [...] "
            "Air flow from the qanat is used to cool an underground summer room (shabestan) found in many older houses and buildings.",
            nome="Qanat")],
    },
    # 15 o túnel da Mancha que começou em 1881 e parou por medo de invasão
    {
        "temas_secundarios": ["fronteiras_paises", "revolucao_industrial", "transportes"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Nos anos 1880, máquinas perfuradoras já tinham aberto mais de 1,6 km de túnel sob o Canal da Mancha de cada lado. A obra parou em 1883 porque militares britânicos temiam uma invasão pelo túnel.",
        "explicacao": (
            "A ideia de ligar Inglaterra e França por baixo do mar é antiga: em 1802, o engenheiro de minas francês "
            "Albert Mathieu-Favier propôs um túnel iluminado por lampiões a óleo, com carruagens puxadas a cavalo e "
            "uma ilha artificial no meio do canal para trocar os animais. Em 1881, o empresário ferroviário Edward "
            "Watkin e Alexandre Lavalley, empreiteiro da companhia francesa do canal de Suez, se juntaram numa "
            "empresa que fez escavações exploratórias nos dois lados. Entre junho de 1882 e março de 1883, a máquina "
            "britânica avançou 1.840 metros no giz, e a francesa, 1.669 metros a partir de Sangatte. Apesar do "
            "sucesso, o projeto foi abandonado em 1883, por medo dos militares britânicos de que um túnel submarino "
            "servisse de rota de invasão. O argumento durou décadas: Churchill escreveu em 1924 um texto rebatendo "
            "essa ideia, e uma proposta posterior chegou a prever reservatórios que poderiam ser inundados à vontade "
            "para bloquear o túnel. Em 1958, as galerias de 1881 foram desobstruídas para um estudo geológico. A obra "
            "atual só começou em 1988 e terminou em 1994. Parte da terra escavada do lado britânico, despejada atrás "
            "de um quebra-mar, criou 30 hectares de terreno novo, hoje um parque."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Channel_Tunnel",
            "The modern project was initiated by Eurotunnel in 1988 and completed in 1994 [...] "
            "The remainder was deposited at Lower Shakespeare Cliff behind a seawall, reclaiming 74 acres (30 hectares) of land. "
            "This reclaimed land was later developed into Samphire Hoe, a country park. [...] "
            "In 1802, Albert Mathieu-Favier, a French mining engineer, proposed a tunnel under the English Channel, with illumination from oil lamps, horse-drawn coaches, and an artificial island positioned mid-Channel for changing horses. [...] "
            "In 1881, British railway entrepreneur Sir Edward Watkin and Alexandre Lavalley, a contractor of the French Suez Canal Company, participated in the Anglo-French Submarine Railway Company, which conducted exploratory work on both sides of the Channel. "
            "From June 1882 to March 1883, the British tunnel boring machine tunnelled, through chalk, a total of 1,840 metres (6,037 ft), while Lavalley used a similar machine to drill 1,669 m (5,476 ft) from Sangatte on the French side. "
            "However, the cross-Channel tunnel project was abandoned in 1883, despite this success, after fears raised by the British military that an underwater tunnel might be used as an invasion route. [...] "
            "In the 1920s, Winston Churchill advocated for the Channel Tunnel, using that exact name in his essay \"Should Strategists Veto The Tunnel?\" "
            "It was published on 27 July 1924 in the Weekly Dispatch, and argued vehemently against the idea that the tunnel could be used by a Continental enemy in an invasion of Britain. [...] "
            "The engineers had addressed the concerns of both nations' military leaders by designing two sumps – one near the coast of each country – that could be flooded at will to block t [...] "
            "In 1958, the 1881 workings were cleared in preparation for a £100,000 geological survey by the Channel Tunnel Study Group.",
            nome="Channel Tunnel")],
    },
]
