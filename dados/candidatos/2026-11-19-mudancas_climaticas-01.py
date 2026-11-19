LOTE = "2026-11-19-mudancas_climaticas-01"
AREA = "terra"
TEMA = "mudancas_climaticas"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


IPCC_SPM = "https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_SPM.pdf"
NOAA_CO2 = "https://www.climate.gov/news-features/understanding-climate/climate-change-atmospheric-carbon-dioxide"
UVM_CAMP = "https://www.uvm.edu/news/story/greenland-melted-recently-shows-higher-risk-sea-level-rise"
KOCH_2019 = "https://eprints.whiterose.ac.uk/id/eprint/154711/1/1-s2.0-S0277379118307261-main.pdf"
LOULERGUE_2007 = "https://cp.copernicus.org/articles/3/527/2007/"

CANDIDATOS = [
    # 1 Eunice Foote e os cilindros ao sol (1856)
    {
        "temas_secundarios": ["personagens_esquecidos", "termodinamica"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Em 1856, três anos antes do físico John Tyndall, a americana Eunice Foote mostrou com cilindros de vidro ao sol que o CO2 retém calor e sugeriu que mais CO2 no ar aqueceria a Terra. Ficou esquecida por quase um século.",
        "explicacao": (
            "Foote era cientista amadora e ativista dos direitos das mulheres. O experimento era simples: uma bomba "
            "de ar, dois cilindros de vidro e quatro termômetros. Ela enchia os cilindros com gases diferentes, "
            "esperava que ficassem na mesma temperatura e os punha ao sol. O cilindro com gás carbônico, então "
            "chamado de \"gás ácido carbônico\", esquentou mais que os outros, chegou a 52 °C e demorou muito mais "
            "para esfriar. A partir disso, ela propôs que uma atmosfera com mais desse gás daria à Terra uma "
            "temperatura mais alta. O trabalho foi apresentado em agosto de 1856 num congresso científico em Albany, "
            "nos EUA, mas não por ela: quem o leu, por razões que não estão claras, foi Joseph Henry, da Smithsonian. "
            "Depois que ela morreu, em 1888, a contribuição ficou desconhecida por quase cem anos, até ser resgatada "
            "por pesquisadoras no século XX. Há uma ressalva: o aparelho dela não separava a luz do Sol do calor "
            "infravermelho emitido pela Terra, que é o que de fato produz o efeito estufa. Tyndall, com equipamento "
            "melhor, mediu isso em 1859. Ainda se discute se ele chegou a conhecer o trabalho dela."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Eunice_Newton_Foote",
            "Eunice Newton Foote (born Eunice Newton; July 17, 1819 – September 30, 1888) was an American scientist, inventor, and women's rights campaigner. [...] "
            "for almost a hundred years her contributions were unknown, before being rediscovered by women academics in the twentieth century. [...] "
            "Detailed examination of her work by modern scientists has confirmed that three years before Tyndall published his paper in 1859, Foote discovered that water vapor and CO2 absorb heat from sunlight. [...] "
            "An amateur scientist, Foote conducted a series of experiments that demonstrated the interactions of sunlight on different gases. "
            "She used an air pump, two glass cylinders, and four mercury-in-glass thermometers. [...] "
            "When both cylinders reached equal ambient temperatures, they were placed in the sunlight and temperature variances were measured. [...] "
            "She performed this experiment on air, carbon dioxide (CO2) (which was called carbonic acid gas in her era), and hydrogen, finding that the tube filled with carbon dioxide became hotter than the others when exposed to sunlight. [...] "
            "it was many times as long in cooling\". "
            "Foote noted that CO2 reached a temperature of 125 °F (52 °C) [...] "
            "\"An atmosphere of that gas would give to our earth a high temperature; [...] "
            "that she submitted for the tenth annual AAAS meeting, held on August 23, 1856, in Albany, New York. "
            "For reasons that are unclear, Foote did not read her paper to those present [...] "
            "her paper was instead presented by Joseph Henry of the Smithsonian Institution. [...] "
            "According to Jackson and Hayhoe, Foote's simple apparatus could not distinguish between the effects of energy emitted from the sun and infrared energy radiated by the Earth. "
            "Because Tyndall had more sophisticated equipment, Hayhoe noted that he was able to make these distinctions [...] "
            "The rediscovery of Foote also sparked academic debate on whether Tyndall knew of her work.",
            nome="Eunice Newton Foote")],
    },
    # 2 a curva de Keeling "respira"
    {
        "temas_secundarios": ["plantas", "atmosfera"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Medido no alto de um vulcão do Havaí desde 1958, o CO2 do ar sobe e desce todo ano como uma respiração: cai no verão do hemisfério Norte, quando as plantas crescem, e volta a subir no outono e no inverno.",
        "explicacao": (
            "A série foi iniciada pelo cientista Charles David Keeling, que instalou analisadores de gás no vulcão "
            "Mauna Loa em 1958. O lugar foi escolhido por ser isolado, longe dos continentes, e quase sem vegetação. "
            "Logo nos primeiros anos ele notou o ciclo das estações, que tem cerca de 6 ppm (partes por milhão) de "
            "amplitude: o CO2 chega ao máximo em maio, cai na primavera e no verão do Norte, quando as plantas novas "
            "o retiram do ar pela fotossíntese, chega ao mínimo em setembro e sobe de novo quando as folhas caem e "
            "apodrecem. O hemisfério Norte domina essa respiração porque concentra a maior parte das terras e, "
            "portanto, da vegetação. Por baixo das ondas, a curva sobe sem parar: eram 313 ppm em março de 1958. "
            "No começo dos anos 1960, a Fundação Nacional de Ciência dos EUA cortou o apoio à pesquisa, que "
            "considerou \"rotineira\". Hoje é o registro contínuo de CO2 mais longo do mundo. Segundo a NOAA, a "
            "média global de 2024 foi de 422,8 ppm, um recorde, e a última vez que o CO2 esteve tão alto foi há "
            "cerca de 3 milhões de anos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Keeling_Curve",
                "The Keeling Curve is a graph of the annual variation and overall accumulation of carbon dioxide in the Earth's atmosphere based on continuous measurements taken at the Mauna Loa Observatory on the island of Hawaii from 1958 to the present day. [...] "
                "Keeling obtained funding from the Weather Bureau to install infrared gas analyzers at remote locations, including the South Pole and on the volcano of Mauna Loa on the island of Hawaii. "
                "Mauna Loa was chosen as a long-term monitoring site due to its remote location far from continents and its lack of vegetation. [...] "
                "Keeling's Tellus article of 1960 presented the first monthly CO2 records from Mauna Loa and Antarctica (1957 to 1960), finding a \"distinct seasonal cycle [...] "
                "show a steady increase in mean atmospheric CO2 concentration from 313 parts per million by volume (ppm) in March 1958 [...] "
                "The Keeling Curve also shows a cyclic variation of about 6 ppm each year corresponding to the seasonal change in uptake of CO2 by the world's land vegetation. "
                "Most of this vegetation is in the Northern Hemisphere, where most of the land is located. "
                "From a maximum in May, the level decreases during the northern spring and summer as new plant growth takes CO2 out of the atmosphere through photosynthesis. "
                "After reaching a minimum in September, the level rises again in the northern fall and winter as plants and leaves die off and decay, releasing CO2 back into the atmosphere.",
                nome="Keeling Curve"),
            wiki("Charles_David_Keeling",
                "In the early 1960s, the National Science Foundation stopped supporting his research, calling the outcome \"routine\". [...] "
                "The data collection started by Keeling and continued at Mauna Loa is the longest continuous record of atmospheric carbon dioxide in the world",
                nome="Charles David Keeling"),
            {"url": NOAA_CO2, "titulo": "Climate Change: Atmospheric Carbon Dioxide (NOAA Climate.gov)", "idioma": "en",
             "trecho": "global average atmospheric carbon dioxide was 422.8 parts per million (“ppm,” for short) in 2024, a new record high. [...] "
                       "the last time atmospheric carbon dioxide amounts were this high was roughly 3 million years ago"},
        ],
    },
    # 3 o ar das bolhas é mais novo que o gelo
    {
        "temas_secundarios": ["agua_doce_gelo", "estados_materia"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Nos cilindros de gelo tirados da Antártida, o ar preso nas bolhas é mais jovem que o gelo em volta. Num dos pontos de coleta, a neve leva uns 2.500 anos para virar gelo e fechar as bolhas.",
        "explicacao": (
            "Quando a neve se acumula, cada camada comprime as de baixo, que viram firn, um material intermediário e "
            "ainda poroso, por onde o ar continua circulando. Só quando a densidade chega a cerca de 830 kg por metro "
            "cúbico o firn vira gelo e o ar fica selado em bolhas, guardando a composição da atmosfera daquele "
            "momento. Na Groenlândia e na Antártida, isso acontece entre 64 e 115 metros de profundidade. Onde neva "
            "muito, é rápido: no Summit Camp, na Groenlândia, o gelo se fecha aos 77 metros, com 230 anos. Em Dome "
            "C, na Antártida, onde neva pouco, são 95 metros e 2.500 anos. Por isso, ao comparar o CO2 das bolhas "
            "com a temperatura registrada no próprio gelo, os cientistas precisam calcular essa diferença de idade. "
            "Mais fundo, por volta de 1.500 metros, a pressão empurra as moléculas de ar para dentro dos cristais de "
            "gelo, as bolhas somem e o gelo fica mais transparente. O mesmo pouco acúmulo de neve que atrasa o "
            "fechamento faz o registro de Dome C ir tão longe: chega a 800 mil anos."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Ice_core",
                "As snow accumulates, each layer presses on lower layers, making them denser until they turn into firn. "
                "Firn is not dense enough to prevent air from escaping; but at a density of about 830 kg/m3 it turns to ice, and the air within is sealed into bubbles that capture the composition of the atmosphere at the time the ice formed. "
                "The depth at which this occurs varies with location, but in Greenland and the Antarctic it ranges from 64 m to 115 m. "
                "Because the rate of snowfall varies from site to site, the age of the firn when it turns to ice varies a great deal. "
                "At Summit Camp in Greenland, the depth is 77 m and the ice is 230 years old; at Dome C in Antarctica the depth is 95 m and the age 2500 years. "
                "As further layers build up, the pressure increases, and at about 1500 m the crystal structure of the ice changes from hexagonal to cubic, allowing air molecules to move into the cubic crystals and form a clathrate. "
                "The bubbles disappear and the ice becomes more transparent. [...] "
                "The Dome C core had very low accumulation rates, which mean that the climate record extended a long way; by the end of the project the usable data extended to 800,000 years ago.",
                nome="Ice core"),
            {"url": LOULERGUE_2007, "titulo": "New constraints on the gas age-ice age difference along the EPICA ice cores, 0–50 kyr (Climate of the Past, 2007)", "idioma": "en",
             "trecho": "Gas is trapped in polar ice sheets at ~50–120 m below the surface and is therefore younger than the surrounding ice. "
                       "Firn densification models are used to evaluate this ice age-gas age difference (Δage) in the past."},
        ],
    },
    # 4 Terra bola de neve e a saída pelos vulcões
    {
        "temas_secundarios": ["geologia_profunda", "evolucao"],
        "tipos_espanto": ["escala_absurda", "misterio_aberto"],
        "gancho": "Entre 717 e 635 milhões de anos atrás, a Terra pode ter congelado quase inteira. Um cientista soviético calculou que, se isso ocorresse, ela nunca mais descongelaria. A saída teriam sido os vulcões.",
        "explicacao": (
            "A hipótese da \"Terra bola de neve\" vem de rochas deixadas por geleiras em lugares que, pelo "
            "magnetismo registrado nelas, estavam nos trópicos. Os episódios principais são dois, entre cerca de "
            "717 e 635 milhões de anos atrás. Nos anos 1960, o climatologista Mikhail Budyko mostrou com um modelo "
            "simples que, se o gelo avançasse o bastante a partir dos polos, o brilho dele refletiria tanta luz "
            "solar que o planeta esfriaria mais, até congelar todo. Mas concluiu que isso nunca tinha acontecido, "
            "porque o modelo não oferecia saída. Em 1992, Joseph Kirschvink, que cunhou o nome, propôs uma: com a "
            "superfície coberta, as rochas param de reagir com a água e de retirar CO2 do ar, enquanto os vulcões "
            "continuam soltando o gás. Ao longo de 4 a 30 milhões de anos, o CO2 chegaria a algo como 350 vezes o "
            "nível atual, cerca de 13% da atmosfera, até derreter o gelo nos trópicos. Ainda se discute se a Terra "
            "congelou inteira ou se sobrou uma faixa de mar aberto perto do equador, e há quem conteste a própria "
            "ideia de um congelamento global."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [wiki("Snowball_Earth",
            "The Snowball Earth is a geohistorical hypothesis proposing that during one or more of Earth's icehouse climates, the planet's surface was nearly entirely frozen, with little or no liquid water exposed. "
            "This global glaciation hypothesis is most commonly associated with the Cryogenian Period, which included two major glacial episodes: the Sturtian (c. 717–660 Ma) and Marinoan (c. 650–635 Ma). [...] "
            "Opponents of the hypothesis contest the geological evidence for global glaciation [...] "
            "Several unanswered questions remain, including whether Earth was a full \"snowball\" or a \"slushball\" with a thin equatorial band of open (or seasonally open) water. [...] "
            "In the 1960s, Mikhail Budyko, a Soviet climatologist, developed a simple energy-balance climate model to investigate the effect of ice cover on global climate. "
            "Using this model, Budyko found that if ice sheets advanced far enough out of the polar regions, a feedback loop ensued where the increased reflectiveness (albedo) of the ice led to further cooling and the formation of more ice, until the entire Earth was covered in ice and stabilized in a new ice-covered equilibrium. "
            "While Budyko's model showed that this ice-albedo stability could happen, he concluded that it had, in fact, never happened, as his model offered no way to escape from such a feedback loop. [...] "
            "he presented palaeomagnetic data showing that glacial tillites in Svalbard and Greenland were deposited at tropical latitudes. [...] "
            "The term \"snowball Earth\" was coined by Joseph Kirschvink in a short paper published in 1992 [...] "
            "the introduction of a mechanism by which to escape from a completely ice-covered Earth—specifically, the accumulation of CO2 from volcanic outgassing leading to an ultra-greenhouse effect. [...] "
            "The snowball Earth hypothesis was originally devised to explain geological evidence for the apparent presence of glaciers at tropical latitudes. [...] "
            "The carbon dioxide levels necessary to thaw Earth have been estimated as being 350 times what they are today, about 13% of the atmosphere. "
            "Since Earth was almost completely covered with ice, carbon dioxide could not be withdrawn from the atmosphere by release of alkaline metal ions weathering out of siliceous rocks. "
            "Over 4 to 30 million years, enough CO2 and methane, mainly emitted by volcanoes but also produced by microbes converting organic carbon trapped under the ice into the gas, would accumulate to finally cause enough greenhouse effect to make surface ice melt in the tropics",
            nome="Snowball Earth")],
    },
    # 5 Milanković: preso na lua de mel, calculando as eras glaciais
    {
        "temas_secundarios": ["primeira_guerra", "historia_astronomia"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Preso como inimigo no início da Primeira Guerra, logo depois de casar, o sérvio Milutin Milanković abriu a mala na cela e voltou às contas que ligariam as eras glaciais às variações da órbita da Terra.",
        "explicacao": (
            "Milanković casou em junho de 1914 e, a caminho da lua de mel na Suíça, passou pela aldeia natal, Dalj, "
            "então parte da Áustria-Hungria. Ali soube do assassinato de Francisco Ferdinando. Como era oficial da "
            "reserva do exército sérvio, foi detido e levado a um campo de prisioneiros. Na primeira noite, tirou da "
            "mala seus artigos e anotações sobre o \"problema cósmico\" e escreveu até passar da meia-noite. Seu "
            "mentor, Emanuel Czuber, conseguiu que ele passasse o cativeiro em Budapeste com direito a trabalhar, e "
            "lá ele ficou quase toda a guerra, estudando na biblioteca da Academia de Ciências. A ideia central é "
            "que mudanças lentas na forma da órbita, na inclinação e na direção do eixo da Terra redistribuem a luz "
            "do Sol entre estações e latitudes, o bastante para marcar o ritmo das eras glaciais. A obra que reuniu "
            "quase três décadas de cálculos foi para a gráfica em 2 de abril de 1941, quatro dias antes do bombardeio "
            "de Belgrado, que destruiu a gráfica; as folhas impressas escaparam. Os ciclos que ele calculou foram "
            "confirmados, embora sua teoria original seja hoje vista como incompleta."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Milutin_Milankovi%C4%87",
            "Milankovitch married Kristina Topuzović, an amateur opera singer, on 14 June 1914. "
            "They decided to go on their honeymoon to Switzerland, but before that they stopped in Milankovitch's native village of Dalj in Austria-Hungary, where they heard that Franz Ferdinand had been assassinated in Sarajevo [...] "
            "Milankovitch was soon arrested by the Austro-Hungarian authorities because he was a reserve officer in the Royal Serbian Army and at first he spent six weeks under house arrest, but was eventually imprisoned and later sent to a prisoner-of-war camp [...] "
            "In the suitcase  I had my printed works and my notes on the cosmic problem, there was clean paper too and I started writing. "
            "It was far past midnight when I stopped. [...] "
            "Through his social connections, Professor Czuber arranged Milanković's release from prison and permission to spend his captivity in Budapest with the right to work. [...] "
            "enabled him to work undisturbed in the Academy's library and the Central Meteorological Institute. "
            "Milanković spent four years in Budapest, almost the entire war. [...] "
            "rth's orbit that gradually redistribute insolation between the seasons and low- and high-latitude regions (now known as Milankovitch cycles), and he developed a quantitative theory of climate where these insolation cycles were sufficient to cause the recurring ice ages of the Quaternary period. "
            "While the Milankovitch cycles in insolation have been confirmed and further substantiated by subsequent research, the classical Milankovitch theory of climate, in its original formulation, provides an incomplete explanation of glacial–interglacial climate dynamics. [...] "
            "which covered his nearly three decades of research [...] "
            "The manuscript was submitted to print on 2 April 1941 – four days before the attack of Nazi Germany and its allies on the Kingdom of Yugoslavia. "
            "In the bombing of Belgrade on 6 April 1941, the printing house where his work was being printed was destroyed; however, almost all of the printed sheet paper remained undamaged in the printing warehouse.",
            nome="Milutin Milanković"),
            wiki("Milankovitch_cycles",
            "The Earth's orbit varies between nearly circular and mildly elliptical (its eccentricity varies). [...] "
            "In addition, the tilt of the Earth's axis (its obliquity) changes slightly. [...] "
            "Finally, the direction in the fixed stars pointed to by the Earth's axis changes (axial precession)",
            nome="Milankovitch cycles")],
    },
    # 6 Dryas recente: o frio que voltou em poucos anos
    {
        "temas_secundarios": ["plantas", "oceanografia"],
        "tipos_espanto": ["contraintuitivo", "origem_inesperada"],
        "gancho": "Há uns 12.900 anos, quando a Terra saía da última era glacial, o frio voltou de repente. Na Groenlândia, a temperatura caiu até 10 °C, e a queda pode ter levado 3 anos ou menos. A época leva o nome de uma flor.",
        "explicacao": (
            "O episódio se chama Dryas Recente e durou até uns 11.700 anos atrás. O nome vem da Dryas octopetala, "
            "uma flor da tundra alpina cujos fósseis são abundantes nos sedimentos escandinavos dessa época. No "
            "período quente anterior, a planta era rara, e havia árvores na Escandinávia. O resfriamento atingiu o "
            "hemisfério Norte em poucas décadas, com 2 a 6 °C a menos na Europa e cerca de 3 °C a menos na América "
            "do Norte. Enquanto isso, o hemisfério Sul esquentou. Esse efeito de gangorra é a pista da causa: o "
            "consenso é que houve um enfraquecimento forte da grande circulação de correntes do Atlântico, que leva "
            "calor do sul para o norte. O que provocou esse enfraquecimento ainda é debatido. A hipótese mais "
            "tradicional é uma enxurrada de água doce e fria de um lago gigante de degelo na América do Norte, e "
            "uma erupção vulcânica também foi proposta. O fim foi tão brusco quanto o começo, com um aquecimento "
            "forte em cerca de 50 anos, que marca a passagem para a época atual, o Holoceno."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Younger_Dryas",
            "The Younger Dryas (YD, Greenland Stadial GS-1) was the final climatic phase of the Last Glacial Period that occurred from around 12,900 to 11,700 years Before Present [...] "
            "It is primarily known for the sudden or abrupt cooling in the Northern Hemisphere, when the North Atlantic Ocean cooled and annual air temperatures decreased by around 3 °C (5 °F) over North America, 2–6 °C (4–11 °F) in Europe and up to 10 °C (18 °F) in Greenland, in a few decades. "
            "Cooling in Greenland was particularly rapid, taking place over just 3 years or less. "
            "At the same time, the Southern Hemisphere experienced warming. "
            "This period ended as rapidly as it began, with dramatic warming over around 50 years, the transition from the glacial Pleistocene epoch into the current Holocene interglacial. [...] "
            "This \"polar seesaw\" pattern is consistent with changes in thermohaline circulation (particularly the Atlantic meridional overturning circulation or AMOC), which greatly affects how much heat is able to go from the Southern Hemisphere to the North. [...] "
            "The scientific consensus is that severe AMOC weakening explains the climatic effects of the Younger Dryas. [...] "
            "However, there is some debate over what caused the AMOC to become so weak in the first place. "
            "The hypothesis historically most supported by scientists was an interruption from an influx of fresh, cold water from North America's Lake Agassiz into the Atlantic Ocean. [...] "
            "A volcanic eruption as an initial trigger for cooling and sea ice growth has been proposed more recently [...] "
            "The Younger Dryas period is named after the alpine–tundra wildflower Dryas octopetala, because its fossils are abundant in the European (particularly Scandinavian) sediments dating to this timeframe. [...] "
            "On the contrary, Dryas octopetala was rare during the Bølling–Allerød Interstadial. "
            "Instead, European temperatures were warm enough to support trees in Scandinavia",
            nome="Younger Dryas")],
    },
    # 7 o Saara verde e o maior lago da Terra
    {
        "temas_secundarios": ["egito_antigo", "pre_historia", "agua_doce_gelo"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Até uns 5 a 6 mil anos atrás, boa parte do Saara tinha capim, árvores e lagos. O lago Chade ficou ao menos dez vezes maior que hoje e foi o maior lago da Terra. Havia hipopótamos e crocodilos onde hoje é deserto.",
        "explicacao": (
            "É o chamado Período Úmido Africano, que começou há cerca de 14.500 anos. A causa principal foram "
            "mudanças lentas no eixo da Terra, que fortaleceram as monções africanas, reforçadas pela própria "
            "vegetação, pela redução da poeira e por mais gases de efeito estufa. No auge, o \"Megachade\" chegou a "
            "1.000 por 600 quilômetros. Fósseis mostram uma fauna de savana e de rio: elefantes, girafas, "
            "rinocerontes, hipopótamos, crocodilos, pelicanos e peixes como a perca-do-nilo. Pessoas caçavam, "
            "coletavam e criavam gado, cabras e ovelhas onde hoje quase nada vive, e deixaram pinturas como as da "
            "Caverna dos Nadadores, nas montanhas de Gilf Kebir, no Egito, com cenas de gente nadando. Foram essas pinturas em lugares "
            "hoje inóspitos que levaram exploradores a propor um Saara verde, ideia que ganhou nome nos anos 1930. "
            "Quando o período acabou, as populações foram migrando para lugares com água garantida, como o vale do "
            "Nilo e a Mesopotâmia. O período úmido marcou fundo as culturas africanas, inclusive o nascimento da "
            "civilização egípcia. E simular um Saara tão verde ainda é um desafio para os modelos climáticos."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("African_humid_period",
            "The African humid period (AHP; also known by other names) was a climate period in Africa during the late Pleistocene and Holocene geologic epochs, when North Africa was wetter than it is today. "
            "The covering of much of the Sahara by grasses, trees, and lakes was caused by changes in the Earth's axial tilt, changes in vegetation and dust in the Sahara which strengthened the African monsoon, and increased greenhouse gases. [...] "
            "The humid period began about 14,600–14,500 years ago [...] "
            "The AHP ended 6,000–5,000 years ago [...] "
            "The AHP led to the widespread settlement of the Sahara and the Arabian Desert and had a profound effect on African cultures, including the birth of the Ancient Egyptian civilization. "
            "People in the Sahara lived as hunter-gatherers and domesticated cattle, goats, and sheep. [...] "
            "rock paintings such as those in the Cave of Swimmers and in the Acacus Mountains. "
            "Earlier humid periods in Africa were postulated after the discovery of these rock paintings in now-inhospitable parts of the Sahara. "
            "When the period ended, humans gradually abandoned the desert in favour of regions with more secure water supplies, such as the Nile Valley and Mesopotamia [...] "
            "Further discoveries of petroglyphs led desert explorer László Almásy to coin the concept of a Green Sahara in the 1930s. [...] "
            "in general, the simulation of the Green Sahara is considered a problem for Earth system models. [...] "
            "This fauna included antelopes, baboons, birds, cane rats, catfish, clams, cormorants, crocodiles, elephants, frogs, gazelles, giraffes, hartebeest, hares, hippopotamuses, molluscs, Nile perches, pelicans, rhinoceroses [...] "
            "Scenes include animals and everyday life such as swimming which supports the presence of past wetter climates. "
            "One well-known such petroglyph location is the Cave of Swimmers in the Gilf Kebir mountains of Egypt [...] "
            "The largest of them was Lake Chad which increased to at least ten times its present-day size to form Lake Megachad or Megalake Chad, then the largest lake on Earth. "
            "This enlarged Lake Chad reached dimensions of 1,000 by 600 kilometres",
            nome="African humid period")],
    },
    # 8 o evento Azolla: samambaias no Ártico
    {
        "temas_secundarios": ["plantas", "oceanografia", "energia"],
        "tipos_espanto": ["conexao_inesperada", "misterio_aberto"],
        "gancho": "Há uns 49 milhões de anos, uma samambaia aquática pode ter coberto o oceano Ártico por 800 mil anos e, ao afundar, ajudado a tirar CO2 do ar e a esfriar o planeta. É a hipótese do \"evento Azolla\".",
        "explicacao": (
            "Pouco antes, a Terra tinha passado por uma fase de estufa, com calor bastante para tartarugas e "
            "palmeiras nos polos. O Ártico era um mar quase fechado, com uma camada de água doce dos rios boiando sobre a água "
            "salgada, e bastavam alguns centímetros dela para a Azolla, uma samambaia de água doce, se espalhar. Com "
            "calor moderado e até 20 horas de sol, ela pode dobrar de massa em dois ou três dias. As plantas mortas "
            "afundavam num fundo sem oxigênio, onde nada as decompunha, e acabavam enterradas. Em sedimentos de toda "
            "a bacia do Ártico, perfurações acharam uma camada de pelo menos 8 metros com finíssimas lâminas de "
            "Azolla fossilizada. O episódio coincide com uma queda do CO2, de 3.500 ppm no começo do Eoceno para "
            "650 ppm, e a hipótese é que a samambaia possa ter respondido por boa parte dessa queda, ajudando a "
            "virar o clima de estufa para o de gelo nos polos que vivemos hoje. Há céticos: as plantas podem ter "
            "sido levadas ao mar por correntes, vindas de deltas e lagoas. Esses depósitos também atraem interesse "
            "da indústria do petróleo."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "hipotese",
        "fontes": [wiki("Azolla_event",
            "The Azolla event is a paleoclimatology scenario hypothesized to have occurred in the middle Eocene epoch, around 49 million years ago, when blooms of the carbon-fixing freshwater fern Azolla are thought to have happened in the Arctic Ocean. "
            "As the fern died and sank to the stagnant sea floor, it were incorporated into the sediment over a period of about 800,000 years; "
            "the resulting draw-down of carbon dioxide has been speculated to have helped reverse the planet from the \"greenhouse Earth\" state of the Paleocene-Eocene Thermal Maximum, when the planet was hot enough for turtles and palm trees to prosper at the poles, to the current icehouse Earth known as the Late Cenozoic Ice Age. [...] "
            "In sedimentary layers throughout the Arctic basin, a unit reaching at least 8 m in thickness [...] "
            "switch with millimetre-thick laminations comprising fossilised Azolla matter. [...] "
            "The event coincides precisely with a catastrophic decline in carbon dioxide levels, which fell from 3500 ppm in the early Eocene to 650 ppm during this event. [...] "
            "The plant can grow at great speed in favourable conditions – modest warmth and 20 hours of sunlight, both of which were in evidence at the poles during the early Eocene – and can double its biomass over two to three days in such a climate. [...] "
            "During the early Eocene, the continental configuration was such that the Arctic Sea was almost entirely cut off from the wider oceans. [...] "
            "This low-density freshwater formed a nepheloid layer, floating on the surface of the dense sea. "
            "Even a few centimetres of fresh water would be enough to allow colonization by Azolla [...] "
            "The anoxic bottom of the Arctic basin, a result of the stratified water column, permitted just this; the anoxic environment inhibits the activity of decomposing organisms and allows the plants to sit unrotted until they are buried by sediment. [...] "
            "even by very conservative estimates more than enough carbon could be sequestered by plant burial to account for the observed 80% drop in CO2 by this one phenomenon alone. "
            "Other factors almost certainly played a role. [...] "
            "skeptical scientists point out that it would be possible for Azolla colonies in river deltas or freshwater lagoons to be swept into the Arctic Ocean by strong currents [...] "
            "Much of the current interest in oil exploration in the Arctic regions is directed towards the Azolla deposits",
            nome="Azolla event")],
    },
    # 9 Camp Century: o solo esquecido no freezer
    {
        "temas_secundarios": ["guerra_fria", "agua_doce_gelo"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Nos anos 1960, uma base militar secreta dos EUA sob o gelo da Groenlândia tirou um tubo de solo de baixo de mais de um quilômetro de gelo. Esquecido num freezer, ele guardava folhas e musgo de uns 416 mil anos atrás.",
        "explicacao": (
            "A base era Camp Century, escavada em túneis no gelo e movida a reator nuclear. Oficialmente era uma "
            "estação científica, mas servia de teste para o Projeto Iceworm, que pretendia esconder centenas de "
            "mísseis nucleares sob o gelo, perto da União Soviética. Os mísseis nunca foram instalados. Os "
            "cientistas de lá perfuraram o gelo até a base e, no fim, tiraram também um tubo de terra e rocha "
            "de baixo dele. Mas estavam interessados no gelo, não na terra. O material foi de um freezer militar para a "
            "Universidade de Buffalo nos anos 1970, e de lá para um freezer na Dinamarca nos anos 1990, onde se "
            "perdeu. Foi reencontrado por acaso em 2017, e dentro havia folhas e musgo, restos de uma paisagem sem "
            "gelo. Um estudo publicado em 2023 na revista Science, que datou o sedimento pela luminescência dos "
            "grãos, concluiu que o lugar estava livre de gelo há cerca de 416 mil anos, com margem de uns 38 mil, "
            "num período quente parecido com o atual. O derretimento da época teria elevado o nível do mar em pelo "
            "menos cinco pés, cerca de um metro e meio. Para os autores, o gelo da Groenlândia é mais sensível ao aquecimento do que se pensava."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": UVM_CAMP, "titulo": "Greenland Melted Recently, Shows Higher Risk of Sea Level Rise (University of Vermont)", "idioma": "en",
             "trecho": "During the Cold War, a secret U.S. Army mission, at Camp Century in northwestern Greenland, drilled down through 4560 feet of ice on the frozen island—and then kept drilling to pull out a twelve-foot-long tube of soil and rock from below the ice. "
                       "Then this icy sediment was lost in a freezer for decades. "
                       "It was accidentally rediscovered in 2017 and shown to hold not just sediment but also leaves and moss, remnants of an ice-free landscape, perhaps a boreal forest. [...] "
                       "An international team of scientists was amazed to discover that Greenland was a green land only 416,000 years ago (with an error margin of about 38,000 years). "
                       "Their new study was published in the journal Science on July 21, 2023. [...] "
                       "This indicates that the ice sheet on Greenland may be more sensitive to human-caused climate change than previously understood [...] "
                       "The new study presents direct evidence that sediment just beneath the ice sheet was deposited by flowing water in an ice-free environment during a moderate warming period called Marine Isotope Stage 11, from 424,000 to 374,000 years ago. "
                       "This melting caused at least five feet of sea level rise around the globe. [...] "
                       "At Rittenour’s lab, sediment from the Camp Century core was examined for what is called a “luminescence signal.” [...] "
                       "Camp Century was a military base hidden in tunnels under the Greenland ice sheet in the 1960s. "
                       "One strategic purpose of the camp was a top-secret operation, called Project Iceworm, to hide hundreds of nuclear missiles under the ice near the Soviet Union. "
                       "As cover, the Army claimed the camp was an Arctic science station. [...] "
                       "The Camp Century scientists were focused on the ice itself [...] "
                       "They took little interest in the twelve feet of sediment gathered from beneath their ice core. "
                       "Then, in a bizarre story, the ice core was moved in the 1970s from a military freezer to the University at Buffalo—and then to another freezer in Denmark in the 1990s. [...] "
                       "a long interglacial with temperatures similar to or slightly warmer than today."},
            wiki("Camp_Century",
                "Missiles were never fielded at the facility [...] "
                "It consisted of 21 tunnels with a total length of 9,800 feet (3.0 km) and was powered by a nuclear reactor.",
                nome="Camp Century"),
        ],
    },
    # 10 o mito da "era do gelo" prevista nos anos 1970
    {
        "temas_secundarios": ["guerra_fria", "vieses_cognitivos"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Diz-se que nos anos 1970 os cientistas previam uma nova era do gelo. Algumas revistas falaram nisso, mas, entre os estudos da época sobre o clima do século XXI, menos de 10% apontavam para esfriamento.",
        "explicacao": (
            "A origem do mito está em reportagens como a da revista Newsweek de abril de 1975, \"The Cooling World\", "
            "que falava em sinais de que o planeta caminhava para o frio. Havia um fato por trás: a temperatura média "
            "do hemisfério Norte tinha caído um pouco desde os anos 1940. Hoje há consenso de que a causa principal "
            "foi a própria poluição, porque a queima de combustíveis lançava partículas de enxofre que refletem a luz "
            "do Sol. Mas a literatura científica da época estava mais preocupada com o aquecimento pelo efeito "
            "estufa, e a maior parte dos artigos que olhavam para o século XXI previa aquecimento. Em 1959, a revista "
            "Science News já estimava que o CO2 do ar subiria 25% entre 1850 e 2000; o aumento real foi de 29%. Em "
            "junho de 1976, a Organização Meteorológica Mundial alertou que um aquecimento muito significativo era "
            "provável. Quando o esfriamento chegou à imprensa, a temperatura já tinha parado de cair, e depois voltou "
            "a subir com força. Em 2006, mais de 31 anos depois, a Newsweek publicou uma correção admitindo ter errado "
            "\"de forma espetacular\" sobre o futuro próximo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Global_cooling",
            "Some press reports in the 1970s speculated about continued cooling; these did not accurately reflect the scientific literature of the time, which was generally more concerned with warming from an enhanced greenhouse effect. "
            "An overall warming trend from the late Industrial Revolution did slow and reverse slightly from the 1940s to the 1970s due to high industrial emissions of sulfur-based aerosols, but then continued sharply upward into the 2020s. [...] "
            "In the scientific papers which considered climate trends of the 21st century, fewer than 10% were inclined towards future cooling, while most papers predicted future warming. [...] "
            "but Science News in May 1959 forecast a 25% increase in atmospheric carbon dioxide in the 150 years from 1850 to 2000, with a consequent warming trend. "
            "The actual increase in this period was 29%. [...] "
            "By the time the idea of global cooling reached the public press in the mid-1970s temperatures had stopped falling, and there was concern in the climatological community about carbon dioxide's warming effects. "
            "In response to such reports, the World Meteorological Organization issued a warning in June 1976 that \"a very significant warming of global climate\" was probable. [...] "
            "there is now general agreement that aerosol effects were the dominant cause of the mid-20th century cooling. [...] "
            "An April 28, 1975, article in Newsweek magazine was titled \"The Cooling World\", it pointed to \"ominous signs that the Earth's weather patterns have begun to change\" [...] "
            "On October 23, 2006, Newsweek issued a correction, over 31 years after the original article, stating that it had been \"so spectacularly wrong about the near-term future\" [...] "
            "The average surface air temperature in the northern hemisphere increased from the 1880s until about 1940 and has been decreasing thereafter.",
            nome="Global cooling")],
    },
    # 11 acidificação: 0,1 de pH, 26% mais ácido
    {
        "temas_secundarios": ["vida_marinha", "quimica_cotidiano"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Desde 1950, o pH da superfície do oceano caiu só de cerca de 8,15 para 8,05. Parece pouco, mas a escala de pH é logarítmica: isso equivale a uns 26% a mais de íons de hidrogênio, que é o que mede a acidez.",
        "explicacao": (
            "O mar absorve parte do CO2 que a humanidade emite: cerca de 30% das emissões desde o começo da era "
            "industrial. Na água, o gás forma ácido carbônico, que se desfaz e libera íons de hidrogênio, e são "
            "eles que baixam o pH. Como a escala é logarítmica, uma unidade de pH corresponde a dez vezes mais "
            "íons, e por isso um décimo já pesa tanto. Apesar do nome \"acidificação\", a água do mar ainda é "
            "alcalina, com pH acima de 8: o que muda é a direção. O problema é sobretudo para quem constrói concha "
            "ou esqueleto de carbonato de cálcio, como corais, moluscos e pequenos caramujos nadadores, os "
            "pterópodes, que estão na base da cadeia alimentar do Ártico e cujas conchas se dissolvem com mais "
            "acidez. Algo parecido já aconteceu no passado da Terra. O ritmo atual costuma ser comparado ao do "
            "aquecimento de 56 milhões de anos atrás, na passagem do Paleoceno para o Eoceno, que provocou uma "
            "grande extinção de organismos do fundo do mar. Só que hoje o carbono entra no sistema "
            "atmosfera-oceano cerca de dez vezes mais depressa que naquela época."
        ),
        "nivel": 2, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Ocean_acidification",
            "CO2 from the atmosphere is absorbed by the oceans. "
            "This chemical reaction produces carbonic acid (H2CO3) which dissociates into a bicarbonate ion (HCO−3) and a hydrogen ion (H+). "
            "The presence of free hydrogen ions (H+) lowers the pH of the ocean, increasing acidity (this does not mean that seawater is acidic yet; It is still alkaline, with a pH higher than 8). "
            "Marine calcifying organisms, such as mollusks and corals, are especially vulnerable because they rely on calcium carbonate to build shells and skeletons. [...] "
            "Ocean acidification has happened before in Earth's geologic history. [...] "
            "as a result of the uptake of approximately 30% of the anthropogenic carbon dioxide emissions over the past 270 years (since around 1750). [...] "
            "Between 1950 and 2020, the average pH value of the ocean surface is estimated to have decreased from approximately 8.15 to 8.05. "
            "This represents an increase of around 26% in hydrogen ion concentration in the world's oceans (the pH scale is logarithmic, so a change of one in pH unit is equivalent to a tenfold change in hydrogen ion concentration). [...] "
            "Current rates of ocean acidification have been likened to the greenhouse event at the Paleocene–Eocene boundary (about 56 million years ago), when surface ocean temperatures rose by 5–6 °C. "
            "In that event, surface ecosystems experienced a variety of impacts, but bottom-dwelling organisms in the deep ocean actually experienced a major extinction. "
            "Currently, the rate of carbon addition to the atmosphere-ocean system is about ten times the rate that occurred at the Paleocene–Eocene boundary. [...] "
            "Pteropods and brittle stars both form the base of the Arctic food webs and are both seriously damaged from acidification. "
            "Pteropods shells dissolve with increasing acidification",
            nome="Ocean acidification")],
    },
    # 12 o paradoxo do Sol jovem e fraco
    {
        "temas_secundarios": ["estrelas", "astrobiologia"],
        "tipos_espanto": ["misterio_aberto", "contraintuitivo"],
        "gancho": "Quando a Terra era jovem, o Sol brilhava só uns 70% do que brilha hoje. Pelas contas, o planeta deveria estar congelado, mas tinha água líquida e vida. Como isso foi possível ainda é debatido.",
        "explicacao": (
            "O problema foi levantado pelos astrônomos Carl Sagan e George Mullen em 1972. O Sol fica mais "
            "brilhante com a idade: a fusão no núcleo transforma hidrogênio em hélio e reduz o número de partículas, "
            "o núcleo se contrai e esquenta, e a fusão acelera. Modelos indicam que hoje ele é 1,4 vez mais brilhante "
            "do que há 4,6 bilhões de anos. Sagan e Mullen sugeriram que a amônia teria aquecido a Terra primitiva, "
            "mas esse gás é destruído com facilidade pela luz solar. A explicação mais aceita hoje é que havia muito "
            "mais CO2 no ar, mantido por um termostato natural: quando o planeta esfria, chove menos, as rochas se "
            "desgastam menos e param de retirar CO2, que se acumula até reaquecer tudo, num ciclo de centenas de "
            "milhares de anos. As contas indicam que seria preciso ao menos 0,1 bar de CO2 para manter a superfície "
            "acima do congelamento. Mas a quantidade real de CO2 da época ainda é discutida, e uma análise de "
            "minerais de ferro de "
            "rochas antigas sugeriu que micróbios produtores de metano também podem ter ajudado a aquecer. E o "
            "papel das nuvens e do brilho da superfície continua sendo uma das grandes incertezas."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Faint_young_Sun_paradox",
            "The faint young Sun paradox or faint young Sun problem describes the apparent contradiction between observations of liquid water early in Earth's history and the astrophysical expectation that the Sun's output would have been only 70 percent as intense during that epoch as it is during the modern epoch. "
            "The paradox is this: with the young Sun's output at only 70 percent of its current output, early Earth would be expected to be completely frozen, but early Earth seems to have had liquid water and supported life. "
            "The issue was raised by astronomers Carl Sagan and George Mullen in 1972. "
            "Proposed resolutions of this paradox have taken into account greenhouse effects, changes to planetary albedo, astrophysical influences, or combinations of these suggestions. "
            "The predominant theory is that the greenhouse gas carbon dioxide contributed most to the warming of the Earth. [...] "
            "The brightening is caused by a decrease in the number of particles per unit mass due to nuclear fusion in the Sun's core, from four protons and electrons each to one helium nucleus and two electrons. "
            "Fewer particles would exert less pressure. "
            "A collapse under the enormous gravity is prevented by an increase in temperature, which is both cause and effect of a higher rate of nuclear fusion. [...] "
            "More recent modeling studies have shown that the Sun is currently 1.4 times as bright today as it was 4.6 billion years ago [...] "
            "Sagan and Mullen suggested during their descriptions of the paradox that it might be solved by high concentrations of ammonia gas, NH3. "
            "However, it has since been shown that while ammonia is an effective greenhouse gas, it is easily destroyed photochemically in the atmosphere [...] "
            "In particular, during a time of low surface temperatures, rainfall and weathering rates would be reduced, allowing for the build-up of carbon dioxide in the atmosphere on timescales of 0.5 million years. "
            "Specifically, using 1-D models [...] scientists have determined that at 4.5 Ga, with a 30% dimmer Sun, a minimum partial pressure of 0.1 bar of CO2 is required to maintain an above-freezing surface temperature [...] "
            "The amount of carbon dioxide is still under debate. [...] "
            "Then in 2010, Rosing et al. analyzed marine sediments called banded iron formations and found large amounts of various iron-rich minerals [...] "
            "Anaerobic, single-celled organisms that produced methane (CH4) may therefore have contributed to the warming in addition to carbon dioxide. [...] "
            "Clouds continue to be the dominant source of uncertainty in 3-D global climate models",
            nome="Faint young Sun paradox")],
    },
    # 13 as feiras sobre o Tâmisa congelado e a ponte que ajudava
    {
        "temas_secundarios": ["cidades", "grandes_obras"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Na Pequena Idade do Gelo, Londres fazia feiras sobre o Tâmisa congelado; na última, em 1814, um elefante atravessou o rio. Mas o frio não explica tudo: a velha London Bridge ajudava a represar o rio.",
        "explicacao": (
            "A maior parte dessas feiras aconteceu entre o começo do século XVII e o começo do XIX, quando os "
            "invernos britânicos eram mais rigorosos. Mesmo assim, eram raras: de 1400 até 1831, o rio congelou em "
            "Londres em 24 invernos. A mais célebre foi a do Grande Frio de 1683-84, quando o Tâmisa ficou "
            "totalmente congelado por dois meses, com gelo de 28 centímetros. Havia corrida de cavalos e "
            "carruagens, patinação, teatro de bonecos e um impressor que vendia cartões com o nome do freguês e a "
            "prova de que foram impressos sobre o rio; o rei Carlos II comprou um. A geografia ajudava: sem margens "
            "construídas, o rio era mais largo e lento. E os 19 pilares da ponte medieval, protegidos por grossas "
            "caixas de madeira que foram crescendo com os anos, estreitavam os arcos. No inverno, pedaços de gelo "
            "se prendiam ali, fechavam os vãos e faziam a ponte agir como uma represa. Depois de 1814, o clima foi "
            "ficando mais ameno, a ponte foi demolida em 1831, substituída por outra de arcos largos, e o rio "
            "ganhou margens construídas ao longo do século XIX. Nunca mais houve feira."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("River_Thames_frost_fairs",
            "Most were held between the early 17th and early 19th centuries during the period known as the Little Ice Age, when the river froze over most often, though still infrequently. "
            "During that time the British winter was more severe than it is now, and the river was wider and slower, further impeded by the 19 piers of the medieval Old London Bridge which were removed in 1831. [...] "
            "From 1400 until the removal of the medieval London Bridge in 1831, there were 24 winters in which the Thames was recorded to have frozen over at London. [...] "
            "During the Great Frost of 1683–84, the most severe freeze recorded in England, the Thames was completely frozen for two months, with the ice reaching a thickness of 11 inches (28 cm) in London. [...] "
            "The Thames was broader and shallower in the Middle Ages – it was yet to be embanked, meaning that it flowed more slowly. "
            "Moreover, old London Bridge, which carried a row of shops and houses on each side of its roadway, was supported on many closely spaced piers; these were protected by large timber casings which, over the years, were extended – causing a narrowing of the arches below the bridge, thus concentrating the water into swift-flowing torrents. "
            "In winter, large pieces of ice would lodge against these timber casings, gradually blocking the arches and acting like a dam for the river at ebb tide. [...] "
            "Activities included horse and coach racing, ice skating, puppet plays and bull-baiting [...] "
            "For sixpence, the printer Croom sold souvenir cards written with the customer's name, the date, and the fact that the card was printed on the Thames; he was making five pounds a day (ten times a labourer's weekly wage). "
            "King Charles II bought one. [...] "
            "The frost fair of 1814 began on 1 February, and lasted four days, between Blackfriars Bridge and London Bridge. "
            "An elephant was led across the river below Blackfriars. [...] "
            "This was the last frost fair. "
            "The climate was growing milder; old London Bridge was demolished in 1831 and replaced with a new bridge with wider arches, allowing the tide to flow more freely; and the river was embanked in stages during the 19th century, all of which made the river less likely to freeze.",
            nome="River Thames frost fairs")],
    },
    # 14 a Grande Mortandade das Américas e a queda do CO2
    {
        "temas_secundarios": ["grandes_navegacoes", "doencas_infecciosas", "americas_pre_colombianas"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "O gelo da Antártida registra uma queda do CO2 do ar no fim do século XVI e começo do XVII. Um estudo de 2019 atribui boa parte dela às florestas que cresceram nas Américas depois que epidemias mataram 90% dos indígenas.",
        "explicacao": (
            "A queda foi de 7 a 10 ppm, maior que a margem de erro das medições, com o mínimo no começo do século "
            "XVII. A explicação mais citada liga a queda à chegada dos europeus. Pesquisadores do University "
            "College London reuniram 119 estimativas regionais e calcularam que as Américas tinham cerca de 60,5 "
            "milhões de habitantes antes de 1492. No século seguinte, epidemias trazidas pelos europeus mataram "
            "cerca de 90% deles. Roças e áreas manejadas foram abandonadas e a vegetação voltou a crescer em "
            "55,8 milhões de hectares, retirando carbono do ar. Pelas contas do estudo, isso explicaria uma queda de "
            "3,5 ppm e, somados outros efeitos, de 47% a 67% da queda total. O período coincide com um esfriamento "
            "global de cerca de 0,15 °C, e os autores sugerem que a mortandade pode ter contribuído para a fase mais "
            "fria da Pequena Idade do Gelo. Há explicações naturais concorrentes, e as estimativas têm margens "
            "largas. A queda, chamada de \"Orbis spike\", foi proposta por alguns cientistas como marco do início do "
            "Antropoceno, a época em que a humanidade passou a alterar o planeta, mas a ideia é disputada."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [
            {"url": KOCH_2019, "titulo": "Earth system impacts of the European arrival and Great Dying in the Americas after 1492 (Quaternary Science Reviews, 2019)", "idioma": "en",
             "trecho": "Geography, University College London [...] "
                       "Available online 25 January 2019 [...] "
                       "From 1 19 published regional population estimates we calculate a pre-1492 CE population of 60.5 million [...] "
                       "European epidemics removed 90% [...] of the indigenous population over the next century. "
                       "This resulted in secondary succession of 55.8 Mha [...] of abandoned land [...] "
                       "equivalent to a decline in atmospheric CO 2 of 3.5 ppm [...] "
                       "47 e67% of the atmospheric CO 2 decline. [...] "
                       "may have reduced atmospheric CO 2 levels and led to a decline in radiative forcing that may then have contributed to the coldest part of the Little Ice Age [...] "
                       "This analysis shows that the cooling over this period was 0.15 +C."},
            wiki("Orbis_spike",
                "The Orbis Spike is a global dip in atmospheric carbon dioxide levels around the year 1610 CE, as recorded by the Antarctic sea ice record. "
                "There are several hypotheses as to what caused the dip, the chief among them being diseases brought by European explorers. [...] "
                "There has been controversy raised about whether the Orbis Spike should be recognized as the beginning of the Anthropocene [...] "
                "The levels of carbon dioxide decreased by an estimated 7-10ppm, which is higher than the 1-2ppm that is the usual margin of error for such measurements. "
                "While it is certain that atmospheric carbon dioxide decreased at this time, the exact mechanisms responsible for this drop are debated.",
                nome="Orbis spike"),
        ],
    },
    # 15 o mar que continua subindo por séculos (IPCC)
    {
        "temas_secundarios": ["oceanografia", "agua_doce_gelo"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Segundo o IPCC, mesmo que o aquecimento pare em 1,5 °C, o mar seguirá subindo por séculos: 2 a 3 m nos próximos 2.000 anos. Se parar em 2 °C, 2 a 6 m; com 5 °C de aquecimento, 19 a 22 m.",
        "explicacao": (
            "Os números estão no Sumário para Formuladores de Políticas do sexto relatório do IPCC, de 2021. A "
            "razão é a inércia: as águas profundas do oceano continuam esquentando e as grandes camadas de gelo "
            "seguem derretendo, num processo lento. Por isso, segundo o relatório, o nível do mar está comprometido a subir por séculos "
            "a milênios e ficará elevado por milhares de anos, com alta confiança. Mesmo tirando mais CO2 do ar do "
            "que se emite, levaria séculos a milênios para essa subida se inverter. Neste século, a alta é bem "
            "menor e depende do cenário: até 2100, em relação a 1995-2014, a faixa provável vai de 0,28 a 0,55 m no "
            "cenário de emissões muito baixas e de 0,63 a 1,01 m no de emissões muito altas. O passado ajuda a "
            "conferir as projeções longas. Há cerca de 125 mil anos, com temperaturas de 0,5 a 1,5 °C acima do "
            "nível pré-industrial, o mar provavelmente estava de 5 a 10 m acima do atual. Há uns 3 milhões de anos, "
            "com 2,5 a 4 °C a mais, ficava de 5 a 25 m acima."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [{"url": IPCC_SPM, "titulo": "IPCC AR6 WGI: Summary for Policymakers (2021)", "idioma": "en",
            "trecho": "IPCC, 2021: Summary for Policymakers. [...] "
                      "B.5.3  It is virtually certain that global mean sea level will continue to rise over the 21st century. "
                      "Relative to 1995–2014, the likely  global mean sea level rise by 2100 is 0.28–0.55 m under the very low GHG emissions scenario (SSP1-1.9) [...] "
                      "0.63–1.01 m under the very high GHG emissions scenario (SSP5-8.5) [...] "
                      "B.5.4  In the longer term, sea level is committed to rise for centuries to millennia due to continuing deep-ocean warming and  ice-sheet melt and will remain elevated for thousands of years (high confidence). "
                      "Over the next 2000 years, global mean  sea level will rise by about 2 to 3 m if warming is limited to 1.5°C, 2 to 6 m if limited to 2°C and 19 to 22 m with 5°C of  warming [...] "
                      "likely 5–10 m higher than  today around 125,000 years ago, when global temperatures were very likely 0.5°C–1.5°C higher than 1850–1900; "
                      "and very  likely 5–25 m higher roughly 3 million years ago, when global temperatures were 2.5°C–4°C higher (medium confidence). [...] "
                      "it would take several centuries to millennia for global mean sea level to reverse  course even under large net negative CO2 emissions (high confidence)."}],
    },
]
