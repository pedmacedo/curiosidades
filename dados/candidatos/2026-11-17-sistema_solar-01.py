LOTE = "2026-11-17-sistema_solar-01"
AREA = "espaco"
TEMA = "sistema_solar"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = W if idioma == "en" else "https://pt.wikipedia.org/wiki/"
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 anéis de Saturno jovens e passageiros
    {
        "temas_secundarios": ["paleontologia", "estados_materia"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Os anéis de Saturno são provavelmente mais novos que os dinossauros e estão chovendo sobre o planeta: podem sumir em menos de 100 milhões de anos.",
        "explicacao": (
            "Por muito tempo se pensou que os anéis de Saturno fossem tão antigos quanto o próprio planeta. Os "
            "dados da sonda Cassini sugerem o contrário: eles teriam se formado nos últimos 100 milhões de anos e "
            "teriam entre 10 e 100 milhões de anos. A estimativa vem de uma massa menor que a esperada e da "
            "medição da poeira interplanetária que vai escurecendo os anéis com o tempo: eles ainda são claros "
            "demais para serem velhos. E não vão durar para sempre. Grãos de gelo de água com carga elétrica são "
            "puxados pela gravidade ao longo das linhas do campo magnético e caem em Saturno, um processo chamado "
            "\"chuva dos anéis\". Em 2017, ao passar pelo vão entre os anéis e o planeta, a Cassini detectou ainda um "
            "fluxo de 4.800 a 44.000 kg de material por segundo caindo no planeta. Somando os dois processos, os "
            "anéis podem desaparecer em menos de 100 milhões de anos."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [wiki("Rings_of_Saturn",
            "have been considered to possibly be very old, dating to the formation of Saturn itself. "
            "However, data from Cassini suggest they are much younger, having most likely formed within the last 100 million years, and may thus be between 10 million and 100 million years old. "
            "This recent origin scenario is based on a new, low mass estimate modeling of the rings' dynamical evolution, and measurements of the flux of interplanetary dust, which feed into an estimate of the rate of ring darkening over time. [...] "
            "One mechanism involves gravity pulling electrically charged water ice grains down from the rings along planetary magnetic field lines, a process termed 'ring rain'. [...] "
            "While traversing the gap between the rings and planet in September 2017, the Cassini spacecraft detected an equatorial flow of charge-neutral material from the rings to the planet of 4,800–44,000 kg/s. "
            "Assuming this influx rate is stable, adding it to the continuous \"ring rain\" process implies the rings may be gone in under 100 million years.",
            nome="Rings of Saturn")],
    },
    # 2 Io
    {
        "temas_secundarios": ["vulcoes_terremotos", "luz_cores", "historia_astronomia"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "Io, uma lua de Júpiter, tem mais de 400 vulcões ativos, com plumas de até 500 km de altura. A culpa é das marés: ela é espremida por Júpiter e por duas luas vizinhas.",
        "explicacao": (
            "Io é o objeto geologicamente mais ativo do Sistema Solar, com mais de 400 vulcões ativos. Alguns "
            "lançam plumas de enxofre e dióxido de enxofre a até 500 km acima da superfície. A energia não vem de "
            "um interior quente desde a formação, como na Terra, mas do atrito: Io é puxada entre Júpiter e duas "
            "outras grandes luas, Europa e Ganimedes, e essa deformação constante aquece o seu interior, o "
            "chamado aquecimento por maré. O vulcão mais forte, Loki, responde sozinho, em média, por 25% do calor "
            "que sai de Io. Essa atividade só foi revelada em 1979, pelas duas sondas Voyager. Mas Io já tinha "
            "entrado para a história da ciência muito antes: os horários de seus eclipses atrás de Júpiter foram "
            "usados na primeira medição da velocidade da luz."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Io_(moon)",
            "With over 400 active volcanoes, Io is the most geologically active object in the Solar System. "
            "This extreme geologic activity results from tidal heating from friction generated within Io's interior as it is pulled between Jupiter and two other Galilean moons—Europa and Ganymede. "
            "Several volcanoes produce plumes of sulfur and sulfur dioxide as high as 500 km (300 mi) above the surface. [...] "
            "Loki is also consistently the strongest volcano on Io, contributing on average 25% of Io's global heat output. [...] "
            "Io in particular was used for the first measurement of the speed of light. "
            "In 1979, the two Voyager spacecraft revealed Io to be a geologically active world",
            nome="Io (moon)")],
    },
    # 3 Encélado
    {
        "temas_secundarios": ["astrobiologia", "oceanografia"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Uma lua de Saturno, Encélado, tem mais de 100 gêiseres que lançam água de um oceano escondido sob o gelo. Esse material forma um dos anéis do planeta.",
        "explicacao": (
            "Encélado é uma lua pequena e gelada de Saturno, o corpo mais refletor do Sistema Solar: devolve tanta "
            "luz que a superfície fica, em média, a −198 °C ao meio-dia. Em 2005, a sonda Cassini descobriu plumas "
            "saindo da região do polo sul. São criovulcões, que lançam ao espaço jatos de vapor de água, hidrogênio, "
            "cristais de sal e partículas de gelo, cerca de 200 kg por segundo. Já foram identificados mais de "
            "100 gêiseres. Parte do vapor cai de volta como neve, que já forma uma camada de centenas de metros. O "
            "resto escapa e fornece a maior parte do material do anel E de Saturno. A origem dessa água é um "
            "oceano sob o gelo: em 2014, a NASA anunciou que a Cassini achou indícios de um grande oceano de água "
            "líquida sob o polo sul, com cerca de 10 km de espessura. Isso fez de Encélado um dos lugares mais "
            "promissores para procurar vida fora da Terra."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Enceladus",
            "In 2005, the spacecraft Cassini started multiple close flybys of Enceladus [...] "
            "In particular, Cassini discovered water-rich plumes venting from the south polar region. "
            "Cryovolcanoes near the south pole shoot geyser-like jets of water vapour, molecular hydrogen, other volatiles, and solid material, including sodium chloride crystals and ice particles, into space, totalling about 200 kilograms (440 pounds) per second. "
            "More than 100 geysers have been identified. Some of the water vapour falls back as snow, now several hundred metres thick; the rest escapes and supplies most of the material making up Saturn's E ring. [...] "
            "In 2014, NASA reported that Cassini had found evidence for a large south polar subsurface ocean of liquid water with a thickness of around 10 km (6 mi). [...] "
            "the most reflective body in the Solar System [...] "
            "Because it reflects so much sunlight, its surface only reaches a mean noon temperature of −198 °C (−324 °F)")],
    },
    # 4 Urano deitado
    {
        "temas_secundarios": ["clima_tempo", "sono_ritmos"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Urano gira deitado. Por isso cada um de seus polos passa 42 anos seguidos sob o Sol e depois 42 anos no escuro.",
        "explicacao": (
            "O eixo de rotação da Terra é inclinado cerca de 23 graus, e é isso que produz as estações. O de Urano "
            "é praticamente paralelo ao plano do Sistema Solar: a inclinação pode ser descrita como 82 ou 98 graus, "
            "dependendo de qual polo se toma como norte. O planeta gira como uma bola rolando pela órbita. Como a "
            "volta em torno do Sol leva 84 anos terrestres, cada polo fica cerca de 42 anos de dia contínuo, "
            "seguidos de 42 anos de noite contínua. Urano também tem a menor temperatura mínima de atmosfera entre "
            "os planetas do Sistema Solar: −224 °C. Apesar de tudo isso, ele foi visitado uma única vez, em 1986, "
            "quando a sonda Voyager 2 passou por ele, e os cientistas querem voltar."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Uranus",
            "has the lowest minimum temperature (49 K (−224 °C; −371 °F)) of all of the Solar System's planets. "
            "It has a marked axial tilt of 82.23°, with a retrograde rotation period of 17 hours and 14 minutes. "
            "This means that in an 84-Earth-year orbital period around the Sun, its poles get around 42 years of continuous sunlight, followed by 42 years of continuous darkness. [...] "
            "The Uranian axis of rotation is approximately parallel to the plane of the Solar System, with an axial tilt that can be described either as 82.23° or as 97.77°, depending on which pole is co [...] "
            "it has been visited only once when in 1986 the Voyager 2 probe flew by the planet. [...] "
            "there is much desire to revisit the planet")],
    },
    # 5 gelo em Mercúrio
    {
        "temas_secundarios": ["agua_doce_gelo", "estados_materia"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Mercúrio, o planeta mais perto do Sol, tem gelo: no fundo de crateras dos polos, onde a luz do Sol nunca bate, a temperatura fica abaixo de −170 °C.",
        "explicacao": (
            "A superfície de Mercúrio varia de −173 °C a 427 °C. Mas o eixo do planeta quase não é inclinado, e por "
            "isso o fundo das crateras profundas perto dos polos nunca recebe luz direta do Sol. Ali a temperatura "
            "fica abaixo de 102 kelvin, cerca de −171 °C. Sem atmosfera para espalhar o calor, essas crateras "
            "funcionam como armadilhas frias, onde o gelo pode se acumular. A primeira pista veio do radar: gelo de "
            "água reflete muito bem as ondas de rádio, e observações feitas no início dos anos 1990 com o radar de "
            "Goldstone, de 70 metros, e o VLA revelaram manchas de reflexão intensa perto dos polos. O gelo não era "
            "a única explicação possível, mas era a mais provável. A confirmação veio com imagens das crateras do "
            "polo norte feitas pela sonda MESSENGER. Estima-se que essas crateras guardem de cem trilhões a um "
            "quatrilhão de quilos de gelo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Mercury_(planet)",
            "Due to its very small axial tilt, the planet's poles are permanently shadowed. [...] "
            "The floors of deep craters at the poles are never exposed to direct sunlight, and temperatures there remain below 102 K, far lower than the global average. "
            "This creates a cold trap where ice can accumulate. "
            "Water ice strongly reflects radar, and observations by the 70-meter Goldstone Solar System Radar and the VLA in the early 1990s revealed that there are patches of high radar reflection near the poles. "
            "Although ice was not the only possible cause of these reflective regions, astronomers thought it to be the most likely explanation. "
            "The presence of water ice was confirmed using MESSENGER images of craters at the north pole. "
            "The icy crater regions are estimated to contain about 1014–1015 kg of ice [...] "
            "The surface temperature of Mercury ranges from 100 to 700 K (−173 to 427 °C; −280 to 800 °F).",
            nome="Mercury (planet)")],
    },
    # 6 Grande Mancha Vermelha encolhendo
    {
        "temas_secundarios": ["clima_tempo", "atmosfera"],
        "tipos_espanto": ["misterio_aberto", "escala_absurda"],
        "gancho": "A Grande Mancha Vermelha de Júpiter, uma tempestade que já teve três vezes o diâmetro da Terra, está encolhendo, e ninguém sabe quanto tempo ela ainda vai durar.",
        "explicacao": (
            "A Grande Mancha Vermelha é a maior tempestade anticiclônica do Sistema Solar, uma região de alta "
            "pressão na atmosfera de Júpiter. Há cerca de um século, seu comprimento chegava a 40.000 km, cerca de "
            "três vezes o diâmetro da Terra. Em 2004, já tinha mais ou menos a metade disso. Se o encolhimento "
            "seguir no ritmo atual, ela ficará circular por volta de 2040. A idade da tempestade também é incerta. "
            "Uma mancha foi vista em Júpiter no século XVII, mas pode ter sido outra tempestade, e é possível que a "
            "atual tenha sido avistada pela primeira vez só em 1830. Não se sabe quanto tempo ela vai durar, nem "
            "se a redução faz parte de uma flutuação periódica."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Great_Red_Spot",
            "The Great Red Spot is a persistent, elliptical high-pressure region in the atmosphere of the planet Jupiter, producing the largest anticyclonic storm in the Solar System. [...] "
            "In the 21st century, the major diameter of the Great Red Spot has been observed to be shrinking. "
            "In 2004 its length was about half that of a century earlier, when it reached a size of 40,000 km (25,000 mi), about three times the diameter of Earth. "
            "At the present rate of reduction, it will become circular by 2040. "
            "It is not known how long the spot will last, nor whether the change is a result of periodic fluctuations. [...] "
            "The Great Red Spot may have existed before 1664, but it could be that the present spot was first seen only in 1830 [...] "
            "The storm that was seen in the 17th century may have been different from the storm that exists today.",
            nome="Great Red Spot")],
    },
    # 7 Fobos
    {
        "temas_secundarios": ["asteroides_cometas"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Em Marte, a lua Fobos nasce no oeste e se põe no leste, duas vezes por dia. E ela está condenada: deve ser despedaçada pela gravidade do planeta em 30 a 50 milhões de anos.",
        "explicacao": (
            "Fobos, a maior das duas luas de Marte, é um corpo irregular com raio médio de 11 km e orbita a cerca "
            "de 6.000 km da superfície, mais perto do seu planeta que qualquer outro satélite natural conhecido. "
            "Ela dá a volta em Marte mais depressa do que o planeta gira. Por isso, para quem está em Marte, Fobos "
            "nasce no oeste, cruza o céu em pouco mais de quatro horas e se põe no leste, cerca de duas vezes por "
            "dia marciano. A proximidade tem um preço. A desaceleração por maré está diminuindo aos poucos o raio "
            "da órbita, e quanto mais perto, maior a chance de as forças de maré a despedaçarem. Isso deve "
            "acontecer em cerca de 30 a 50 milhões de anos. Imagens e modelos indicam que Fobos pode ser uma pilha "
            "de entulho mantida por uma crosta fina, que já está sendo rasgada pelas forças de maré."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Phobos_(moon)",
            "Phobos is a small, irregularly shaped object with a mean radius of 11 km (7 mi). "
            "It orbits 6,000 km (3,700 mi) from the Martian surface, closer to its primary body than any other known natural satellite to a planet. [...] "
            "Images and models indicate that Phobos may be a rubble pile held together by a thin crust that is being torn apart by tidal interactions. [...] "
            "meaning that it moves around Mars faster than Mars itself rotates. "
            "Therefore, from the point of view of an observer on the surface of Mars, it rises in the west, moves comparatively rapidly across the sky (in 4 h 15 min or less) and sets in the east, approximately twice each Martian day [...] "
            "Tidal deceleration is gradually decreasing the orbital radius of Phobos [...] "
            "and with decreasing orbital radius the likelihood of breakup due to tidal forces increases, estimated in approximately 30–50 million years",
            nome="Phobos (moon)")],
    },
    # 8 a Lua se afasta
    {
        "temas_secundarios": ["exploracao_espacial", "luz_cores", "medidas_padroes"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Espelhos deixados na Lua pelos astronautas da Apollo ainda são usados: lasers disparados da Terra mostram que a Lua se afasta 3,8 cm por ano.",
        "explicacao": (
            "Em 21 de julho de 1969, a tripulação da Apollo 11 instalou na Lua um conjunto de retrorrefletores, "
            "espelhos especiais que devolvem a luz exatamente na direção de onde ela veio. Outros dois conjuntos "
            "foram deixados pelas missões Apollo 14 e 15, dois pelos jipes soviéticos Lunokhod 1 e 2 e um pela "
            "missão indiana Chandrayaan-3. Observatórios disparam pulsos de laser contra eles e medem quanto tempo "
            "a luz leva para ir e voltar. Como a velocidade da luz é conhecida, isso dá a distância até a Lua com "
            "precisão de milímetros. A primeira medição bem-sucedida foi relatada em 1º de agosto de 1969, dias "
            "depois da instalação. Décadas de medições mostraram que a Lua se afasta da Terra 3,8 cm por ano, uma "
            "taxa considerada anormalmente alta. Os dados revelaram também que a Lua provavelmente tem um núcleo "
            "líquido, com cerca de 20% do seu raio."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Lunar_Laser_Ranging_experiments",
            "The distance can be calculated from the round-trip time of laser light pulses, travelling at the speed of light, which are reflected back to Earth by the Moon's surface or by one of several retroreflectors installed on the Moon. "
            "Three were placed by the United States' Apollo program (11, 14, and 15), two by the Soviet Lunokhod 1 and 2 missions, and one by India's Chandrayaan-3 mission. [...] "
            "This was achieved following the installation of a retroreflector array on July 21, 1969 by the crew of Apollo 11. [...] "
            "Successful lunar laser range measurements to the retroreflectors were first reported on Aug. 1, 1969 [...] "
            "The distance to the Moon can be measured with millimeter precision. "
            "The Moon is spiraling away from Earth at a rate of 3.8 cm/year. This rate has been described as anomalously high. [...] "
            "The Moon probably has a liquid core of about 20% of the Moon's radius.",
            nome="Lunar Laser Ranging experiments")],
    },
    # 9 Titã
    {
        "temas_secundarios": ["clima_tempo", "astrobiologia", "quimica_cotidiano"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Titã, lua de Saturno, tem chuva, rios, lagos e mares, como a Terra. Só que de metano, a −179 °C, sob uma atmosfera mais densa que a nossa.",
        "explicacao": (
            "Titã é a maior lua de Saturno e a única lua conhecida com uma atmosfera densa, mais densa até que a da "
            "Terra, feita principalmente de nitrogênio e metano. A névoa espessa escondeu a superfície até a "
            "missão Cassini-Huygens, que chegou em 2004 e descobriu lagos de hidrocarbonetos líquidos nas regiões "
            "polares. Titã é o único objeto conhecido do Sistema Solar, além da Terra, com corpos estáveis de "
            "líquido na superfície. Um deles, Ligeia Mare, o segundo maior mar de Titã, é quase metano puro. O "
            "clima tem vento e chuva, que esculpem dunas, rios, lagos e mares. O ciclo do metano em Titã lembra "
            "muito o ciclo da água na Terra, mas a uma temperatura de cerca de −179 °C. Por isso Titã é às vezes "
            "chamado de o corpo celeste mais parecido com a Terra no Sistema Solar."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Titan_(moon)",
            "Titan is the largest moon of Saturn and the second largest in the Solar System. "
            "It is the only moon that is known to have a dense atmosphere (denser than that of Earth), and is the only known object in the Solar System besides Earth with stable bodies of surface liquid. [...] "
            "the dense opaque atmosphere prevented understanding of Titan's surface until the Cassini–Huygens mission in 2004 provided new information, including the discovery of liquid hydrocarbon lakes in Titan's polar regions [...] "
            "The atmosphere of Titan is mainly nitrogen and methane [...] "
            "Its climate, including wind and rain, creates surface features similar to those of Earth, such as dunes, rivers, lakes, seas [...] "
            "Ligeia Mare, Titan's second-largest sea, is almost a pure methane sea. [...] "
            "Titan's methane cycle nearly resembles Earth's water cycle, albeit at a much lower temperature of about 94 K (−179 °C; −290 °F). "
            "Due to these factors, Titan is sometimes called the most Earth-like celestial object in the Solar System.",
            nome="Titan (moon)")],
    },
    # 10 Netuno pela ponta da pena
    {
        "temas_secundarios": ["historia_astronomia", "historia_matematica"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Netuno foi descoberto com lápis e papel: um matemático calculou onde ele devia estar, e o planeta foi achado no mesmo dia em que o astrônomo apontou o telescópio.",
        "explicacao": (
            "Em 1846, Urano já tinha dado quase uma volta completa em torno do Sol desde que fora descoberto por "
            "William Herschel, em 1781. Os astrônomos haviam notado irregularidades no seu caminho que a lei da "
            "gravitação de Newton não explicava por inteiro. Elas se resolveriam se a gravidade de um planeta mais "
            "distante e desconhecido estivesse perturbando Urano. O matemático francês Urbain Le Verrier calculou "
            "onde esse planeta deveria estar. Na noite de 23 para 24 de setembro de 1846, no Observatório de "
            "Berlim, o astrônomo Johann Galle, com a ajuda de Heinrich d'Arrest, seguiu os cálculos e encontrou o "
            "planeta. Foi uma confirmação dramática da teoria da gravitação de Newton. Nas palavras de François "
            "Arago, Le Verrier tinha descoberto um planeta \"com a ponta da sua pena\". Depois se descobriu que "
            "Netuno já tinha sido observado várias vezes antes, sem ser reconhecido como planeta."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Discovery_of_Neptune",
            "The planet Neptune was mathematically predicted before it was directly observed. "
            "With a prediction by Urbain Le Verrier, telescopic observations confirming the existence of a major planet were made on the night of September 23–24, autumnal equinox of 1846, at the Berlin Observatory, by astronomer Johann Gottfried Galle (assisted by Heinrich Louis d'Arrest), working from Le Verrier's calculations. "
            "It was a sensational moment of 19th-century science, and dramatic confirmation of Newtonian gravitational theory. "
            "In François Arago's apt phrase, Le Verrier had discovered a planet \"with the point of his pen\". "
            "In retrospect, after it was discovered, it turned out it had been observed many times before but not recognized [...] "
            "By 1846, the planet Uranus had completed nearly one full orbit since its discovery by William Herschel in 1781, and astronomers had detected a series of irregularities in its path that could not be entirely explained by Newton's law of universal gravitation. "
            "These irregularities could, however, be resolved if the gravity of a farther, unknown planet were disturbing it",
            nome="Discovery of Neptune")],
    },
    # 11 pôr do sol azul em Marte
    {
        "temas_secundarios": ["luz_cores", "atmosfera"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Em Marte, o pôr do sol costuma ser azul. A poeira vermelha que enche o ar espalha a luz de um jeito diferente do que acontece na Terra.",
        "explicacao": (
            "Na Terra, o céu do entardecer fica alaranjado porque, quando a luz do Sol atravessa uma camada mais "
            "longa de atmosfera, o azul e o verde são espalhados pelas moléculas do ar e quase somem do feixe. Em "
            "Marte, a história é outra. A atmosfera é fina e quase não tem oxigênio e nitrogênio, então esse tipo "
            "de espalhamento, chamado de Rayleigh, não domina. O ar marciano está cheio de poeira vermelha "
            "levantada por ventos fortes, e é ela que define a cor do céu, por outro processo, o espalhamento de "
            "Mie. O resultado é um pôr do sol com tons de azul. Visto de Marte, o Sol que se põe parece ter cerca "
            "de dois terços do tamanho que tem visto da Terra, por causa da distância maior. E a poeira no alto da "
            "atmosfera pode continuar refletindo a luz do Sol até duas horas depois do pôr do sol."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Sunset",
            "Because the shorter wavelength components, such as blue and green, scatter more strongly, these colors are preferentially removed from the beam. "
            "At sunrise and sunset, when the path through the atmosphere is longer, the blue and green components are removed almost completely [...] "
            "On Mars, the setting Sun appears about two-thirds the size it does from Earth, due to the greater distance between Mars and the Sun. "
            "The colors are typically hues of blue, but some Martian sunsets last significantly longer and appear far redder than is typical on Earth. [...] "
            "Mars has a thin atmosphere, lacking oxygen and nitrogen, so the light scattering is not dominated by a Rayleigh Scattering process. "
            "Instead, the air is full of red dust, blown into the atmosphere by high winds, so its sky color is mainly determined by a Mie Scattering process, resulting in more blue hues than an Earth sunset. "
            "One study also reported that Martian dust high in the atmosphere can reflect sunlight up to two hours after the Sun has set")],
    },
]
