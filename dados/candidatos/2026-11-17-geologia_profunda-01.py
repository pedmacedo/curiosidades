LOTE = "2026-11-17-geologia_profunda-01"
AREA = "terra"
TEMA = "geologia_profunda"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = W if idioma == "en" else "https://pt.wikipedia.org/wiki/"
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


ESA = "https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Swarm/Swarm_probes_weakening_of_Earth_s_magnetic_field"
NASA = "https://www.nasa.gov/missions/icon/nasa-researchers-track-slowly-splitting-dent-in-earths-magnetic-field/"

CANDIDATOS = [
    # 1 poço de Kola
    {
        "temas_secundarios": ["guerra_fria", "microbiologia"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "O buraco mais fundo já cavado, na Rússia, chegou a 12,2 km e parou com 180 °C. Lá embaixo havia água e fósseis de plâncton a 6 km de profundidade.",
        "explicacao": (
            "Em 1970, a União Soviética começou a perfurar a península de Kola, perto da fronteira com a Noruega, "
            "para ir o mais fundo possível na crosta terrestre. Os poços tinham só 23 centímetros de diâmetro. Em "
            "1989, um deles chegou a 12.262 metros, até hoje o buraco artificial mais profundo do planeta. A ideia "
            "era passar dos 15 mil metros, mas as temperaturas foram maiores que o previsto: 180 °C a 11.882 "
            "metros, e a perfuração parou em 1992. As surpresas foram muitas. A camada de basalto esperada a 7 km "
            "nunca apareceu, em nenhuma profundidade: o granito continuava. Entre 3 e 6 km havia água acumulada, "
            "que subira pelo granito até esbarrar numa camada de rocha impermeável. A lama de perfuração saía como "
            "se estivesse \"fervendo\", cheia de gás hidrogênio. E a 6 km de profundidade apareceram fósseis "
            "microscópicos de plâncton. Em 1994 o projeto acabou por falta de dinheiro."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Kola_Superdeep_Borehole",
            "has been the deepest human-made hole on Earth since 1979, attaining a maximum true vertical depth of 12,262 metres (40,230 ft) in 1989. "
            "It is the result of a scientific drilling effort to penetrate as deeply as possible into the Earth's crust conducted by the Soviet Union in the Pechengsky District of the Kola Peninsula, near the Russian border with Norway. [...] "
            "Drilling at Kola SG-3 began in 1970 [...] A total of five 23-centimetre-diameter (9 in) boreholes were drilled [...] "
            "In that year, the hole depth was expected to reach 13,500 metres (44,300 ft) by the end of 1990 and 15,000 metres (49,000 ft) by 1993. [...] "
            "The drilling of the fourth hole was stopped due to higher-than-expected temperatures of 180 °C (356 °F) in 1992 at 11,882 metres (38,983 ft) of depth. [...] "
            "Drilling was stopped in August 1994 at 8,578 metres (28,143 ft) of depth due to lack of funds [...] "
            "During the drilling process, the expected basaltic layers at 7 kilometres (4.3 mi) down were never found, nor were basaltic layers at any depth. [...] "
            "Water pooled 3–6 kilometres (1.9–3.7 mi) below the surface, having percolated up through the granite until it reached a layer of impermeable rock. [...] "
            "The drilling mud that flowed out of the hole was described as \"boiling\" with an unexpected level of hydrogen gas. "
            "Microscopic plankton fossils were found 6 kilometres (3.7 mi) below the surface.",
            nome="Kola Superdeep Borehole")],
    },
    # 2 Projeto Mohole
    {
        "temas_secundarios": ["oceanografia", "guerra_fria", "literatura"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Enquanto disputavam a corrida espacial, os EUA tentaram furar o fundo do mar até o manto da Terra. O projeto foi cancelado, e o manto continua fora de alcance.",
        "explicacao": (
            "O Projeto Mohole, do início dos anos 1960, queria atravessar a crosta e trazer amostras da "
            "descontinuidade de Mohorovičić, a fronteira entre a crosta e o manto. A ideia era ter um equivalente, "
            "nas ciências da Terra, à corrida espacial. Em terra firme seria inviável, mas no oceano o manto fica "
            "bem mais perto do fundo do mar. O grupo de cientistas por trás da proposta tinha um nome bem-humorado: "
            "American Miscellaneous Society, algo como Sociedade Americana de Assuntos Diversos. Os primeiros testes, "
            "em 1961, perto da ilha de Guadalupe, no México, foram narrados pelo escritor John Steinbeck para a "
            "revista Life. Num navio sem âncora, sobre 3.600 metros de água, a equipe furou até 183 metros abaixo "
            "do fundo do mar, algo inédito, e os 13 metros finais eram de basalto. Depois vieram oposição política "
            "e científica, má gestão e custos estourados. Em 1966, a Câmara dos Deputados dos EUA cortou o "
            "dinheiro do projeto."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Project_Mohole",
            "Project Mohole was an attempt in the early 1960s to drill through the Earth's crust to obtain samples of the Mohorovičić discontinuity, or Moho, the boundary between the Earth's crust and mantle. "
            "The project was intended to provide an earth science complement to the high-profile Space Race. "
            "While such a project was not feasible on land, drilling in the open ocean was more feasible because the mantle lies much closer to the sea floor. "
            "Led by a group of scientists called the American Miscellaneous Society with funding from the National Science Foundation, the project suffered from political and scientific opposition, mismanagement, and cost overruns. "
            "The U.S. House of Representatives defunded it in 1966. [...] "
            "initial test drillings into the sea floor occurred off Guadalupe Island, Mexico, in March and April 1961. The event was documented by John Steinbeck for an article in Life magazine. [...] "
            "Five holes were drilled, the deepest to 183 m (601 feet) below the sea floor in 3,600 m (11,700 feet) of water. "
            "This drilling was unprecedented: not because of the hole's depth, but because an untethered platform in deep water was able to drill into the sea floor. [...] "
            "with the lowest 13 m (44 feet) consisting of basalt.",
            nome="Project Mohole")],
    },
    # 3 Inge Lehmann e o núcleo sólido
    {
        "temas_secundarios": ["termodinamica", "estados_materia"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "O centro da Terra é tão quente quanto a superfície do Sol e, mesmo assim, sólido. Quem descobriu esse núcleo sólido foi uma sismóloga dinamarquesa, em 1936.",
        "explicacao": (
            "Até 1936, os cientistas achavam que o núcleo da Terra era uma única esfera de metal derretido. A "
            "dinamarquesa Inge Lehmann mudou isso estudando terremotos. Analisando os dados de um tremor de 1929 "
            "na Nova Zelândia, ela notou ondas fortes registradas em cidades russas onde, pela teoria da época, "
            "não deviam chegar: o núcleo deveria desviar essas ondas e criar uma zona de sombra. As ondas pareciam "
            "atravessar aquela região. Lehmann foi a primeira a interpretá-las como reflexos de um núcleo interno "
            "e concluiu que o núcleo tem duas partes: uma esfera sólida de metal cercada por um núcleo externo "
            "líquido. Publicou a descoberta em 1936, num artigo com um título de uma letra só: P′. Hoje se estima "
            "que a superfície do núcleo interno esteja a cerca de 5.430 °C, mais ou menos a temperatura da "
            "superfície do Sol. Ele continua sólido por causa da pressão altíssima. Lehmann viveu até os 104 anos."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Inge_Lehmann",
                "Inge Lehmann (13 May 1888 – 21 February 1993) was a Danish seismologist and geophysicist who is known for her discovery in 1936 of the solid inner core that exists within the molten outer core of the Earth. [...] "
                "In 1929, Lehmann studied the Murchison earthquake which struck on the South Island of New Zealand. She analysed the seismic data from the earthquake and noticed that there were waves of significant amplitude recorded in the Russian cities of Sverdlovsk and Irkutsk, both unexpected locations. [...] "
                "They were unexpected locations due to the theory that S-waves and some P-waves are deflected by the core creating a shadow area in which waves are not able to pass through. "
                "The waves seemed to pass through that area to reach Russia. [...] "
                "Lehmann was the first to interpret P-wave arrivals as reflections from an inner core. [...] "
                "a solid metal core surrounded by an outer liquid core, overturning the accepted theory of an entirely liquid core [...] "
                "She published these findings in a paper titled P′ (1936). Prior to 1936, scientists believed that the Earth's core was a single, massive molten sphere.",
                nome="Inge Lehmann"),
            wiki("Earth's_inner_core",
                "The temperature at its surface is estimated to be approximately 5,700 K (5,430 °C; 9,800 °F), about the temperature at the surface of the Sun. "
                "The inner core is solid at high temperature because of its high pressure",
                nome="Earth's inner core"),
        ],
    },
    # 4 água no manto (diamante de Juína)
    {
        "temas_secundarios": ["minerais_rochas", "oceanografia", "biomas_brasileiros"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "Um diamante achado em Juína, no Mato Grosso, trouxe a prova de que o manto da Terra guarda água: pode haver ali de uma a três vezes o volume de todos os oceanos.",
        "explicacao": (
            "A ringwoodita é um mineral que só se forma sob pressões enormes, entre 410 e 660 km de profundidade, "
            "na chamada zona de transição do manto. Ela foi identificada pela primeira vez num meteorito, em 1969, e "
            "por muito tempo ninguém tinha visto um pedaço vindo da própria Terra. Até que um diamante "
            "\"ultraprofundo\", achado em Juína, no oeste do Brasil, revelou uma inclusão de ringwoodita, pequena "
            "demais para ser vista a olho nu. A pedra, com cerca de 5 mm, foi trazida à superfície por uma erupção "
            "vulcânica. A inclusão continha água, na forma de hidróxido presa na estrutura do cristal, a prova de "
            "que existe água no manto. Em laboratório, a ringwoodita sintetizada nessas condições guarda até 2,6% "
            "do peso em água. Somando isso à presença do mineral no manto, estima-se que a zona de transição "
            "contenha de uma a três vezes a água de todos os oceanos do mundo, presa dentro das rochas."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [wiki("Ringwoodite",
            "Combined with evidence of its occurrence deep in the Earth's mantle, this suggests that there is from one to three times the world ocean's equivalent of water in the mantle transition zone from 410 to 660 km deep. "
            "This mineral was first identified in the Tenham meteorite in 1969 [...] "
            "Ringwoodite has been synthesized at conditions appropriate to the transition zone, containing up to 2.6 weight percent water. [...] "
            "An \"ultradeep\" diamond (one that has risen from a great depth) found in Juína in western Brazil contained an inclusion of ringwoodite — at the time the only known sample of natural terrestrial origin [...] "
            "The gemstone, about 5mm long, was brought up by a diatreme eruption. The ringwoodite inclusion is too small to see with the naked eye.")],
    },
    # 5 Anomalia do Atlântico Sul
    {
        "temas_secundarios": ["exploracao_espacial", "eletromagnetismo"],
        "tipos_espanto": ["conexao_inesperada", "misterio_aberto"],
        "gancho": "Sobre a América do Sul, o campo magnético da Terra tem um ponto fraco que derruba computadores de satélites e faz astronautas verem clarões.",
        "explicacao": (
            "O campo magnético da Terra é gerado em grande parte pelo ferro líquido que gira no núcleo externo, a "
            "cerca de 3.000 km de profundidade, e funciona como um escudo contra partículas carregadas vindas do "
            "Sol. Sobre a América do Sul e o sul do oceano Atlântico, porém, ele é bem mais fraco: é a Anomalia do "
            "Atlântico Sul. A origem está no próprio núcleo, na inclinação do eixo magnético e no fluxo do metal "
            "derretido. Ali, o cinturão de radiação de Van Allen chega a 200 km de altitude, e as partículas podem "
            "desligar computadores de bordo e atrapalhar a coleta de dados dos satélites que passam pela região. "
            "O telescópio Hubble não faz observações com seus detectores sensíveis de ultravioleta enquanto "
            "atravessa a anomalia, e astronautas relatam ver \"estrelas cadentes\", clarões no campo de visão. A "
            "anomalia está mudando: de 1970 a 2020 o campo mínimo caiu de cerca de 24 mil para 22 mil nanoteslas, "
            "e a área cresceu e se deslocou para oeste, cerca de 20 km por ano. A causa exata intriga os geofísicos."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": NASA, "titulo": "NASA Researchers Track Slowly Splitting 'Dent' in Earth's Magnetic Field", "idioma": "en",
             "trecho": "But over South America and the southern Atlantic Ocean, an unusually weak spot in the field – called the South Atlantic Anomaly, or SAA – allows these particles to dip closer to the surface than normal. "
                       "Particle radiation in this region can knock out onboard computers and interfere with the data collection of satellites that pass through it [...] "
                       "The South Atlantic Anomaly arises from two features of Earth's core: The tilt of its magnetic axis, and the flow of molten metals within its outer core."},
            {"url": ESA, "titulo": "Swarm probes weakening of Earth's magnetic field", "idioma": "en",
             "trecho": "This strange behaviour has geophysicists puzzled and is causing technical disturbances in satellites orbiting Earth. [...] "
                       "The magnetic field is largely generated by an ocean of superheated, swirling liquid iron that makes up the outer core around 3000 km beneath our feet. [...] "
                       "From 1970 to 2020, the minimum field strength in this area has dropped from around 24 000 nanoteslas to 22 000, while at the same time the area of the anomaly has grown and moved westward at a pace of around 20 km per year."},
            wiki("South_Atlantic_Anomaly",
                "The South Atlantic Anomaly (SAA) is an area where Earth's inner Van Allen radiation belt comes closest to Earth's surface, dipping down to an altitude of 200 kilometres (120 mi). [...] "
                "The Hubble Space Telescope does not take observations with its sensitive UV detectors while passing through the SAA. [...] "
                "Astronauts are also affected by this region, which is said to be the cause of peculiar \"shooting stars\" (phosphenes) seen in the visual field of astronauts",
                nome="South Atlantic Anomaly"),
        ],
    },
    # 6 calor interno e geoneutrinos
    {
        "temas_secundarios": ["fisica_particulas", "elementos_quimicos", "energia"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "Metade do calor que sai do interior da Terra vem da radioatividade das rochas, e isso foi medido captando partículas fantasmas, os neutrinos, que atravessam o planeta.",
        "explicacao": (
            "O interior da Terra libera cerca de 47 terawatts de calor para a superfície. Esse calor move a "
            "convecção do manto e a tectônica de placas, e vem de duas fontes principais: o calor primordial, que "
            "sobrou da formação do planeta, e o calor radiogênico, produzido pelo decaimento de isótopos "
            "radioativos no manto e na crosta, como os de urânio, tório e potássio. Medir a proporção de cada um "
            "é difícil, porque não dá para ir até lá. A saída foi engenhosa: o decaimento desses elementos emite "
            "antineutrinos, os geoneutrinos, que atravessam a Terra quase sem interagir com nada. Detectores "
            "enormes, enterrados no subsolo e cheios de um líquido cintilador, registram os raros clarões de luz "
            "que eles provocam. A primeira detecção foi anunciada em 2005 pelo experimento KamLAND, no Japão. As "
            "medições indicaram que cerca de metade do calor interno da Terra é radiogênico. Mesmo assim, esse "
            "calor é só 0,03% da energia na superfície, dominada pelo Sol."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Earth's_internal_heat_budget",
                "The flow of heat from Earth's interior to the surface is estimated at 47±2 terawatts (TW) and comes from two main sources in roughly equal amounts: the radiogenic heat produced by the radioactive decay of isotopes in the mantle and crust, and the primordial heat left over from the formation of Earth. [...] "
                "It drives mantle convection, plate tectonics [...] "
                "Earth's interior heat contributes only 0.03% of Earth's total energy budget at the surface, which is dominated by 173,000 TW of incoming solar radiation. [...] "
                "Initial results from measuring the geoneutrino products of radioactive decay from within the Earth, a proxy for radiogenic heat, yielded a new estimate of half of the total Earth internal heat source being radiogenic [...] "
                "the relative contribution of the two main sources of Earth's heat, radiogenic and primordial heat, are highly uncertain because their direct measurement is difficult.",
                nome="Earth's internal heat budget"),
            wiki("Geoneutrino",
                "Most geoneutrinos are electron antineutrinos originating in β− decay branches of 40K, 232Th and 238U. [...] "
                "large underground liquid scintillator detectors record the flashes of light generated from this interaction. [...] "
                "First detection of geoneutrinos was reported in 2005 by the KamLAND experiment at the Kamioka Observatory in Japan."),
        ],
    },
    # 7 LLSVPs
    {
        "temas_secundarios": ["sistema_solar", "vulcoes_terremotos"],
        "tipos_espanto": ["misterio_aberto", "escala_absurda"],
        "gancho": "No fundo do manto, sob a África e o Pacífico, há duas massas gigantes de rocha diferente, com milhares de km. Uma hipótese: são restos do planeta que bateu na Terra e formou a Lua.",
        "explicacao": (
            "Ondas de terremotos que atravessam o planeta revelaram duas estruturas enormes na base do manto, logo "
            "acima do núcleo externo: as grandes províncias de baixa velocidade de cisalhamento, uma sob a África e "
            "outra sob o Pacífico. Nelas, certas ondas sísmicas andam mais devagar que no resto do manto. Cada uma "
            "se estende por milhares de quilômetros e pode chegar a 1.000 km de altura. Ninguém sabe ao certo o que "
            "elas são. Uma explicação liga essas massas a placas de crosta oceânica que afundaram ao longo de "
            "centenas de milhões de anos. Outra, mais ousada, as relaciona ao grande impacto que teria formado a "
            "Lua, quando a Terra colidiu com um corpo do tamanho de um planeta, chamado Theia. Nesse caso, seriam "
            "pedaços do manto de Theia que afundaram até a fronteira com o núcleo. A densidade maior se explicaria "
            "por um manto mais rico em óxido de ferro."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "hipotese",
        "fontes": [wiki("Large_low-shear-velocity_provinces",
            "the lowermost mantle, above the Earth's outer core. These provinces are characterized by slow shear wave velocities appearing in seismic tomography assays of deep Earth. "
            "The two main provinces are the African LLSVP and the Pacific LLSVP, both extending laterally for thousands of kilometers and possibly up to 1,000 kilometers (620 miles) vertically from the core–mantle boundary. [...] "
            "the accumulation of subducted slabs of oceanic crust. [...] "
            "Another proposed origin for the LLSVPs is related to the hypothesized giant-impact which formed the Moon after Earth collided with a planet-sized body called Theia. "
            "The LLSVPs may represent fragments of Theia's mantle which sank through to Earth's core-mantle boundary. "
            "Their higher density is due to Theia's mantle having higher iron(II) oxide content",
            nome="Large low-shear-velocity provinces")],
    },
    # 8 crosta oceânica jovem
    {
        "temas_secundarios": ["oceanografia", "vulcoes_terremotos"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "O fundo dos oceanos é jovem: quase nunca passa de 200 milhões de anos, menos do que a idade dos dinossauros, porque é reciclado sem parar.",
        "explicacao": (
            "A crosta oceânica nasce nas dorsais meso-oceânicas, cadeias de montanhas submarinas onde o magma sobe "
            "e esfria, formando rocha nova. Por isso as rochas mais jovens do oceano ficam nas dorsais, e a idade "
            "aumenta à medida que se afasta delas. Na outra ponta, a crosta antiga mergulha de volta para o manto "
            "nas zonas de subducção. Esse ciclo consome o fundo do mar mais velho, e por isso a crosta oceânica "
            "raramente tem mais de 200 milhões de anos. As maiores áreas antigas, no oeste do Pacífico e no noroeste "
            "do Atlântico, têm até 180 a 200 milhões de anos. A exceção pode estar no leste do Mediterrâneo, onde "
            "partes do fundo seriam restos do antigo oceano Tétis, com 270 a 340 milhões de anos. O fundo do mar "
            "ainda guarda um registro da história do campo magnético: listras magnéticas paralelas às dorsais, "
            "congeladas no basalto, simétricas dos dois lados."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Oceanic_crust",
            "The youngest oceanic rocks are at the oceanic ridges, and they get progressively older away from the ridges. [...] "
            "The subduction process consumes older oceanic lithosphere, so oceanic crust is seldom more than 200 million years old. [...] "
            "The oldest large-scale oceanic crust is in the west Pacific and north-west Atlantic — both are about up to 180-200 million years old. "
            "However, parts of the eastern Mediterranean Sea could be remnants of the much older Tethys Ocean, at about 270 and up to 340 million years old. [...] "
            "The oceanic crust displays a pattern of magnetic lines, parallel to the ocean ridges, frozen in the basalt. "
            "A symmetrical pattern of positive and negative magnetic lines emanates from the mid-ocean ridge. "
            "New rock is formed by magma at the mid-ocean ridges, and the ocean floor spreads out from this point.",
            nome="Oceanic crust")],
    },
    # 9 a Finlândia cresce
    {
        "temas_secundarios": ["agua_doce_gelo", "fronteiras_paises", "leis_julgamentos"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "A Finlândia ganha cerca de 7 km² de território por ano: o chão ainda está subindo, aliviado do peso do gelo da última era glacial.",
        "explicacao": (
            "Durante a última era glacial, mantos de gelo enormes cobriam o norte da Europa e da América do Norte e "
            "afundavam a crosta com seu peso. Quando o gelo derreteu, o chão começou a subir de volta. A primeira "
            "parte da subida foi quase imediata, uma resposta elástica da crosta. Depois, o movimento passou a "
            "depender do lento escoamento das rochas do manto, que continua até hoje, cada vez mais devagar. As "
            "taxas atuais são de cerca de 1 centímetro por ano ou menos. Na Finlândia, medições de GPS mostram que a "
            "área total do país cresce cerca de sete quilômetros quadrados por ano, à medida que o fundo raso do "
            "mar emerge, e estudos indicam que a subida deve continuar por pelo menos mais 10 mil anos. Isso "
            "criou até uma questão jurídica: na Finlândia, a \"terra nova\" pertence ao dono da área de água, não ao "
            "dono do terreno da margem."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Post-glacial_rebound",
            "The initial uplift following deglaciation was almost immediate due to the elastic response of the crust as the ice load was removed. "
            "After this elastic phase, uplift proceeded by slow viscous flow at an exponentially decreasing rate. "
            "Today, typical uplift rates are of the order of 1 cm/year or less. "
            "In northern Europe, this is clearly shown by the GPS data obtained by the BIFROST GPS network; for example in Finland, the total area of the country is growing by about seven square kilometers per year. "
            "Studies suggest that rebound will continue for at least another 10,000 years. [...] "
            "In areas where the rising of land is seen, it is necessary to define the exact limits of property. "
            "In Finland, the \"new land\" is legally the property of the owner of the water area, not any land owners on the shore.",
            nome="Post-glacial rebound")],
    },
    # 10 inversões do campo magnético
    {
        "temas_secundarios": ["eletromagnetismo", "paleontologia"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Há 780 mil anos, uma bússola apontaria para o sul: o campo magnético da Terra já se inverteu pelo menos 183 vezes nos últimos 83 milhões de anos.",
        "explicacao": (
            "O polo norte magnético nem sempre esteve no norte. De tempos em tempos, o campo magnético da Terra "
            "troca de polaridade, e o que hoje atrai a agulha da bússola passa a repelir. Houve pelo menos 183 "
            "inversões nos últimos 83 milhões de anos, em média uma a cada 450 mil anos, mas os intervalos parecem "
            "aleatórios. A mais recente, chamada Brunhes-Matuyama, aconteceu há 780 mil anos. A duração da troca "
            "é muito debatida: algumas fontes estimam que as quatro últimas levaram em média 7 mil anos. Também há "
            "episódios curtos, as excursões, em que o campo se inverteu por só algumas centenas de anos e depois "
            "voltou, como a excursão de Laschamp. Essas inversões ficam registradas nas rochas: no fundo do mar, a "
            "lava que esfria nas dorsais grava a direção do campo daquele momento, formando listras magnéticas "
            "paralelas e simétricas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Geomagnetic_reversal",
                "Reversal occurrences appear to be statistically random. There have been at least 183 reversals over the last 83 million years (thus on average once every ~450,000 years). "
                "The latest, the Brunhes–Matuyama reversal, occurred 780,000 years ago with widely varying estimates of how quickly it happened. "
                "Some sources estimate that the four most recent reversals took on average 7,000 years to occur. [...] "
                "There have also been episodes in which the field inverted for only a few hundred years (such as the Laschamp excursion). "
                "These events are classified as excursions rather than full geomagnetic reversals.",
                nome="Geomagnetic reversal"),
            wiki("Oceanic_crust",
                "The oceanic crust displays a pattern of magnetic lines, parallel to the ocean ridges, frozen in the basalt. "
                "A symmetrical pattern of positive and negative magnetic lines emanates from the mid-ocean ridge.",
                nome="Oceanic crust"),
        ],
    },
    # 11 zircões de Jack Hills
    {
        "temas_secundarios": ["minerais_rochas", "astrobiologia"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "O material mais antigo da Terra são cristais de zircão de 4,4 bilhões de anos, achados na Austrália. Eles sugerem que já havia água líquida no planeta recém-nascido.",
        "explicacao": (
            "Nas colinas de Jack Hills, no oeste da Austrália, foram encontrados cristais minúsculos de zircão, um mineral extremamente resistente, "
            "formados há cerca de 4,404 bilhões de anos, no éon Hadeano. São o material de origem terrestre mais "
            "antigo já encontrado. E eles contam uma história inesperada. Os isótopos de oxigênio desses cristais "
            "indicam que havia água líquida na superfície, talvez até um oceano, ao contrário da ideia antiga de "
            "que a Terra jovem era só um inferno de lava. Há até grafite dentro de alguns zircões com proporções de "
            "isótopos de carbono que poderiam ter origem biológica, embora isso esteja longe de ser confirmado."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Jack_Hills",
            "The Jack Hills are a range of hills in Mid West Western Australia. They are best known as the source of the oldest material of terrestrial origin found to date: Hadean zircons that formed around 4.404 billion years ago. [...] "
            "Potentially biogenic carbon isotope ratios have been identified for graphite embedded [...] "
            "contrasting with earlier ideas on the earliest phase of Earth's history. Additionally, oxygen isotopic ratios in the zircons provide evidence for the presence of liquid water on the surface, if not a water ocean; also contrasting with earlier ideas on Earth's history.",
            nome="Jack Hills")],
    },
]
