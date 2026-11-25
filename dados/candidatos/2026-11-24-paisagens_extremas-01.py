LOTE = "2026-11-24-paisagens_extremas-01"
AREA = "terra"
TEMA = "paisagens_extremas"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Atacama: estações que nunca viram chuva e os testes das Viking
    {
        "temas_secundarios": ["astrobiologia", "exploracao_espacial", "clima_tempo"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "Algumas estações meteorológicas do deserto do Atacama, no Chile, nunca registraram chuva. Lá, repetiram no solo os testes de vida das sondas Viking, enviadas a Marte, e eles não acharam nenhum sinal.",
        "explicacao": (
            "O Atacama é o deserto não polar mais seco do mundo; só alguns pontos dos Vales Secos de McMurdo, na "
            "Antártida, são mais secos. A chuva média fica em torno de 15 mm por ano, e há lugares que recebem só "
            "de 1 a 3 mm. Há indícios de que talvez não tenha caído chuva significativa entre 1570 e 1971. A secura "
            "vem do relevo: o deserto está espremido entre os Andes e a Cordilheira da Costa, altas o bastante para "
            "barrar a umidade vinda tanto do Pacífico quanto do Atlântico, uma sombra de chuva dos dois lados. Em "
            "2003, uma equipe publicou um estudo em que reproduziu os experimentos que as sondas Viking 1 e 2 usaram "
            "para procurar vida em Marte. No solo da região de Yungay, eles não detectaram sinal algum. Aplicados a "
            "outros ambientes parecidos com Marte, como os vales secos da Antártida e outras partes do Atacama, os "
            "mesmos testes deixaram escapar sinais de vida que estavam presentes nas amostras. A NASA usa a região "
            "para testar instrumentos de futuras missões a Marte."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Atacama_Desert",
            "The Atacama Desert is the driest nonpolar desert in the world, and the second driest overall, behind some specific spots within the McMurdo Dry Valleys. [...] "
            "The average rainfall is about 15 mm (0.6 in) per year, although some locations receive only 1 to 3 mm (0.04 to 0.12 in) in a year. "
            "Moreover, some weather stations in the Atacama have never received rain. [...] "
            "Evidence suggests that the Atacama may not have had any significant rainfall from 1570 to 1971. [...] "
            "the aridity of the Atacama is explained by its being situated between two mountain chains (the Andes and the Chilean Coast Range) of sufficient height to prevent moisture advection from either the Pacific or the Atlantic Oceans, a two-sided rain shadow. [...] "
            "In 2003, a team of researchers published a report in which they duplicated the tests used by the Viking 1 and Viking 2 Mars landers to detect life and were unable to detect any signs in Atacama Desert soil in the region of Yungay. "
            "The region may be unique on Earth in this regard and is being used by NASA to test instruments for future Mars missions. "
            "The team duplicated the Viking tests in Mars-like Earth environments and found that they missed present signs of life in soil samples from Antarctic dry valleys, the Atacama Desert of Chile and Peru, and other locales.",
            nome="Atacama Desert")],
    },
    # 2 Dallol: o lugar habitado mais quente, feito de sal
    {
        "temas_secundarios": ["clima_tempo", "comercio_rotas"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "Dallol, na Etiópia, tem o recorde de maior temperatura média anual de um lugar habitado: cerca de 35 °C, medida nos anos 1960. Lá se ergueram prédios de blocos de sal, e caravanas de camelos ainda vão buscar sal.",
        "explicacao": (
            "Dallol fica na Depressão de Danakil, no nordeste da Etiópia, a cerca de 130 metros abaixo do nível do "
            "mar. Entre 1960 e 1966, a média anual registrada ali foi de 34,6 °C, o recorde para um lugar habitado. "
            "A média das máximas do ano é de 41,2 °C, e no mês mais quente a máxima média chega a 46,7 °C. O calor "
            "vem de uma soma de fatores: a altitude baixíssima, a posição nos trópicos, a proximidade do mar "
            "Vermelho e noites que quase não refrescam. A região também é hiperárida, com poucos dias de chuva "
            "mensurável. O que atraiu gente para lá foram o sal e a potassa. Uma ferrovia construída em 1917 e 1918 "
            "levava sal até um porto na Eritreia, e uma empresa italiana extraiu 25 mil toneladas de silvita entre "
            "1925 e 1929. Os britânicos desmontaram a linha depois da Segunda Guerra. Em 2004, ainda havia prédios "
            "de pé no vilarejo, todos de blocos de sal, e hoje ele é descrito como cidade-fantasma. Mesmo com "
            "estradas asfaltadas desde 2015, o principal meio de transporte, além dos veículos off-road, continua a "
            "ser a caravana de camelos que vai à região recolher sal."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Dallol,_Ethiopia",
            "Located in Kilbet Rasu, Afar Region, in the Afar Depression, it has a latitude and longitude of 14°14′19″N 40°17′38″E with an elevation of about 130 metres (430 ft) below sea level. "
            "The Central Statistical Agency has not published an estimate for the 2005 population of the village, which has been described as a ghost town. "
            "Dallol currently holds the official record for record high average temperature for an inhabited location on Earth, and an average annual temperature of 35 °C (95 °F) was recorded between 1960 and 1966. "
            "Dallol is also one of the most remote places on Earth, but paved roads in the area were built in 2015. "
            "Still, the most important mode of transport besides off-road vehicles are the camel caravans that travel to the area to collect salt. [...] "
            "A railway from the port of Mersa Fatma in Eritrea to a point 28 km (17 mi) from Dallol was completed in April 1918. "
            "Built from 1917 to 1918 [...] it transported salt from the \"Iron Point\" rail terminal near Dallol via Kululli to the port. [...] "
            "Potash production is said to have reached about 51,000 metric tons after the railway was constructed. [...] "
            "Between 1925 and 1929, an Italian company mined 25,000 tons of sylvite, averaging 70% KCl, which was transported by rail to Mersa Fatma. "
            "After World War II, the British administration dismantled the railway and removed all traces of it. [...] "
            "As of 2004, some buildings still stand in Dallol, all built with salt blocks. [...] "
            "an average annual temperature of 34.6 °C (94.3 °F) was recorded between the years 1960 and 1966. "
            "The annual average high temperature is 41.2 °C (106.1 °F) and the hottest month has an average high of 46.7 °C (116.1 °F). [...] "
            "the climate of the lowlands of the Danakil Depression is also extremely dry and hyperarid in terms of annual average rainy days as only a few days record measurable precipitation. "
            "The hot desert climate of Dallol is particularly hot due to the extremely low elevation, it being inside the tropics and near the hot Red Sea during winters, the very low seasonality impact, the constants of the extreme heat and the lack of nighttime cooling.",
            nome="Dallol, Ethiopia")],
    },
    # 3 Danakil: um oceano nascendo
    {
        "temas_secundarios": ["geologia_profunda", "vulcoes_terremotos", "oceanografia"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Na Depressão de Danakil, na Etiópia, um oceano está nascendo: a crosta do continente se estica e afina, e o mar Vermelho já invadiu o vale ao menos quatro vezes, deixando mais de 500 m de sal.",
        "explicacao": (
            "A Depressão de Danakil é um vale de cerca de 200 por 50 km, uns 125 metros abaixo do nível do mar, "
            "entre o planalto etíope e os Alpes Danakil. É um rifte: a placa Núbia e a microplaca Danakil se afastam "
            "de 8 a 18 milímetros por ano. Esse afastamento começou há cerca de 11 milhões de anos e foi afinando a "
            "crosta e afundando a bacia. Sob a cadeia vulcânica de Erta Ale, as rochas indicam que não há mais "
            "crosta continental: as placas provavelmente já se separaram ali, e o rifte está perto da ruptura do "
            "continente e da formação de um oceano, embora a crosta ainda seja de transição. No Pleistoceno, o mar "
            "Vermelho inundou a bacia pelo menos quatro vezes, a última há cerca de 130 mil anos, e deixou depósitos "
            "de sal com mais de 500 metros de espessura. Em 2022, a União Internacional de Ciências Geológicas "
            "incluiu o lugar entre 100 sítios do patrimônio geológico mundial, citando o nascimento de um oceano "
            "visto por meio da tectônica e do vulcanismo. Ali perto, a lagoa Gaet'ale, com 43% de sal, é o corpo "
            "d'água mais salgado da Terra; segundo moradores, ela surgiu depois de um terremoto, em 2005."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Danakil_Depression",
            "The Danakil Depression is a large valley of approximately 200 by 50 km (124 by 31 mi), across the north of the Afar Region of Ethiopia and Eritrea. "
            "It is about 125 m (410 ft) below sea level and is bordered to the west by the Ethiopian Plateau and to the east by the Danakil Alps, beyond which is the Red Sea. [...] "
            "The Danakil Depression is a large valley caused by the extension between the Nubian plate and the Danakil (or Arrata) microplate (on which lie the Danakil Alps). "
            "The velocity between these two plates is approximately 18 mm/yr in the south of the Depression and 8 mm/yr in the north of it. [...] "
            "The formation of the rift started approximately 11 million years ago (Ma) with the counterclockwise rotation of the Danakil microplate. "
            "Since then, tectonic extension caused the thinning of the crust and the subsidence of the basin [...] "
            "The petrology and geochemistry of these rocks indicate an absence of continental crust under the volcanic range, suggesting that the Nubian and Danakil plates are probably detached there. "
            "This indicates that the rift is at an advanced stage of evolution, close to continental breakup and oceanisation. "
            "However, the Erta Ale range does not represent a normal oceanic crust yet, but rather a transitional crust. [...] "
            "During the Mid- and Late Pleistocene, the basin was flooded at least four times by the Red Sea during periods of high sea-level. "
            "The last flooding happened approximately 130,000 years ago. "
            "These floods are testified by fossil coral reefs and by thick (>500m) evaporite deposits (mainly halite, i.e. salt) found in the central part of the basin. [...] "
            "With a salinity of 43%, the pond is the saltiest water body on Earth. "
            "The pond was created in January 2005 following an earthquake, according to residents of Ahmed'ela village, which reactivated the hot spring. [...] "
            "In recognition of it demonstrating \"the ongoing birth of an ocean witnessed through tectonics and volcanism in an extreme evaporite arid environment\", the International Union of Geological Sciences (IUGS) included The Danakil Rift depression and its volcanism in its assemblage of 100 geological heritage sites around the world in a listing published in October 2022.",
            nome="Danakil Depression")],
    },
    # 4 Vales Secos de McMurdo: neve que evapora e solo sem vida detectada
    {
        "temas_secundarios": ["astrobiologia", "agua_doce_gelo"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Nos Vales Secos de McMurdo, na Antártida, ventos gelados que descem das montanhas fazem a neve evaporar em poucas horas. Em 2013, num desses vales, cientistas não detectaram vida microbiana ativa no solo congelado.",
        "explicacao": (
            "Os Vales Secos são a maior área sem gelo da Antártida, com cerca de 4.500 km², e formam o deserto mais "
            "frio e seco do mundo. Duas coisas os mantêm assim. As Montanhas Transantárticas, com picos de uns "
            "3.000 metros, criam uma sombra que barra a neve e impedem o avanço do gelo das geleiras vizinhas. E os "
            "ventos catabáticos, ar frio e denso puxado morro abaixo pela gravidade, secam tudo: a neve que cai "
            "evapora rápido, e pouco dela derrete no solo; no verão, isso pode levar só algumas horas. A "
            "precipitação média é de cerca de 100 mm por ano, quase toda em forma de neve. O chão fica coberto de "
            "cascalho solto, e a temperatura já chegou a −65,7 °C no lago Vida. Esse clima fez dos vales um análogo "
            "de Marte, usado em pesquisas desde o programa Viking, nos anos 1970. Em 2013, pesquisadores irlandeses "
            "e americanos foram ao University Valley testar uma broca projetada para Marte e examinar o permafrost "
            "das áreas mais secas. Não acharam organismos vivos, o que fez do vale o primeiro lugar visitado por "
            "humanos sem vida microbiana ativa detectada. Mesmo assim, há bactérias vivendo no interior úmido de "
            "rochas da região."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("McMurdo_Dry_Valleys",
            "The Dry Valleys are the coldest and driest desert in the world, and the largest ice-free region in Antarctica [...] "
            "Surrounding mountains prevent the flow of ice from nearby glaciers. [...] "
            "endolithic photosynthetic bacteria have been found living in the relatively moist interior of rocks. [...] "
            "At approximately 4,500 square kilometres (1,700 mi2), the valleys constitute around 0.03% of the continent and form its largest ice-free region. "
            "The region's low precipitation is the result of the snow shadow that is created from the Transantarctic Mountains the valleys are situated in; the highest peaks in the region are some 3,000 metres (9,800 ft). "
            "As a result, much of the valley floors remain exposed and covered with loose gravel [...] "
            "The conditions in the Dry Valleys are caused, in part, by katabatic winds; these occur when cold, dense air is pulled downhill by the force of gravity. "
            "The dry wind evaporates the snow rapidly and little melts into the soil. During the summer, this process can take only hours. [...] "
            "Precipitation averages around 100 millimetres (4 in) per year over a century of records, almost exclusively in the form of snow. [...] "
            "The maximum and minimum air temperatures recorded in the Dry Valleys are 12.0 °C (53.6 °F) at Taylor Glacier and −65.7 °C (−86.3 °F) at Lake Vida, respectively. [...] "
            "The valleys' hyper-arid, cold-desert climate was soon identified as a high-fidelity terrestrial analogue for the environment of Mars, and geologists and astrophysicists have subsequently used the Valleys as a testing ground for analog-based studies since NASA's Viking Program in the 1970s. [...] "
            "Irish and American researchers conducted a field expedition in 2013 to University Valley in order to examine the microbial population and to test a drill designed for sampling on Mars in the permafrost of the driest parts of the valleys, the areas most analogous to the Martian surface. "
            "They found no living organisms in the permafrost, making University Valley the first location on the planet visited by humans with no detected active microbial life.",
            nome="McMurdo Dry Valleys")],
    },
    # 5 Lut: o chão mais quente medido por satélite
    {
        "temas_secundarios": ["clima_tempo", "atmosfera"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "O chão mais quente já medido fica no deserto de Lut, no Irã: um satélite da NASA registrou 70,7 °C na superfície em 2005, e dados mais novos indicaram 80,83 °C. Até 2020, nem havia estação meteorológica fixa lá.",
        "explicacao": (
            "Dasht-e Lut, \"planície do vazio\" em persa, ocupa cerca de 51.800 km² no sudeste do Irã. Entre 2003 e "
            "2010, o sensor MODIS, a bordo do satélite Aqua, da NASA, registrou ali a superfície terrestre mais "
            "quente do planeta: 70,7 °C em 2005. Só que isso é a temperatura do chão, não a do ar. Na mesma hora, o "
            "ar poderia estar em qualquer valor entre 30 e 54 °C. Por isso esses números não entram nos recordes "
            "oficiais: a Organização Meteorológica Mundial usa a temperatura do ar, medida a 1,5 metro do chão e "
            "protegida do sol direto, porque leituras do solo e de satélite costumam ser pouco confiáveis. Em 2019, "
            "um estudo com dados mais novos do mesmo sensor relatou 80,83 °C na superfície. O clima exato do Lut é "
            "incerto: até 2020 não havia estações meteorológicas permanentes ali, e pelas estações vizinhas a chuva "
            "deve ficar abaixo de 30 mm por ano. A paisagem também é extrema: no centro, o vento esculpiu cristas "
            "paralelas que se estendem por mais de 150 km e chegam a 75 metros de altura, e no sudeste há dunas de "
            "300 metros, entre as mais altas do mundo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Lut_Desert",
                "Lut Desert (Persian: دشت لوت, romanized: Dasht-e Lut, lit. 'Plain of Emptiness') [...] "
                "The surface of its sand has been measured at temperatures as high as 70.7 °C (159.3 °F), which is the highest-known land surface temperature on Earth. [...] "
                "The area of the desert is about 51,800 square kilometres (20,000 sq mi) [...] "
                "the center has been sculpted by the wind into a series of parallel ridges and furrows, extending over 150 km (93 mi) and reaching 75 metres (246 ft) in height. [...] "
                "The southeast is a vast expanse of sand, like a Saharan erg, with dunes 300 metres (980 ft) high, among the tallest in the world. [...] "
                "The hottest land surface on Earth recorded by the Moderate-Resolution Imaging Spectroradiometer installed on NASA's Aqua satellite from 2003 to 2010 was in Dasht-e Lut, with land surface temperatures reaching 70.7 °C (159.3 °F) in 2005, although the air temperature at that time could have been anywhere from 30 to 54 °C (86 to 129 °F). [...] "
                "In 2019, authors reported a land surface temperature of 80.83 °C (177.49 °F), based on newer MODIS data. "
                "As of 2020, there are no permanent weather stations in Dasht-e Lut, which makes the exact climate uncertain. "
                "Based on neighboring stations, Dasht-e Lut likely receives less than 30 millimetres (1.2 in) of precipitation a year.",
                nome="Lut Desert"),
            wiki("Highest_temperature_recorded_on_Earth",
                "Air measurements are used as the standard measurement because of persistent issues with unreliable ground and satellite readings. "
                "Air measurements are considered by the World Meteorological Organization (WMO) and Guinness World Records among others as the standard to be used for determining the official record. [...] "
                "The standard measuring conditions for temperature are in the air, 1.5 metres (4 ft 11 in) above the ground, and shielded from direct sunlight.",
                nome="Highest temperature recorded on Earth"),
        ],
    },
    # 6 o recorde líbio cancelado e a dúvida sobre o Vale da Morte
    {
        "temas_secundarios": ["clima_tempo", "medidas_padroes"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Por 90 anos, o recorde mundial de calor foi de 57,8 °C, na Líbia. Em 2012, a OMM o cancelou: um observador inexperiente deve ter lido errado um instrumento novo. A marca voltou ao Vale da Morte, também contestada.",
        "explicacao": (
            "A leitura foi feita em 13 de setembro de 1922, em Aziziya, na Líbia, e superou os 56,7 °C registrados "
            "em 10 de julho de 1913 em Furnace Creek, no Vale da Morte, na Califórnia. Em janeiro de 2012, depois de "
            "uma investigação, a Organização Meteorológica Mundial cancelou o número líbio: concluiu-se que um "
            "observador inexperiente provavelmente leu mal um instrumento novo, que não tinha sido treinado para "
            "interpretar. O título voltou ao Vale da Morte, mas o caso levou pesquisadores a reexaminar também a "
            "leitura de 1913. Já em 1949, Arnold Court tinha sugerido que uma tempestade de areia poderia ter "
            "lançado material superaquecido contra o abrigo do termômetro. Historiadores do tempo como Christopher "
            "Burt dizem que o número de 1913 está pelo menos 2,2 a 2,8 °C acima do real, e um estudo publicado em "
            "2026 no Bulletin of the American Meteorological Society calculou um excesso de cerca de 7,8 °C. A OMM "
            "mantém o recorde e diz que só abrirá investigação se surgirem novos materiais. Se ele cair, o primeiro "
            "lugar será dividido por três medições de 54,0 °C: no Vale da Morte, em 2013; no Kuwait, em 2016; e na "
            "Palestina, então sob mandato, em 1942."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Highest_temperature_recorded_on_Earth",
            "For about 90 years, a temperature measured in Libya in 1922 held the world record, until it was decertified in 2012 on the basis of a variety of evidences that it was inaccurate. [...] "
            "If the current record were to be decertified then the holder would be a three-way tie at 54.0 °C (129.2 °F), recorded at Furnace Creek (2013), in Kuwait (2016), and in Mandatory Palestine (1942). [...] "
            "According to the World Meteorological Organization (WMO), the highest registered air temperature on Earth was 56.7 °C (134 °F) in Furnace Creek Ranch, California, located in Death Valley in the United States, on 10 July 1913. "
            "This record was surpassed by a reading of 57.8 °C (136.0 °F), registered nine years later on 13 September 1922, in ʽAziziya, Libya. [...] "
            "This record was decertified by the WMO in January 2012 after investigation concluded that an inexperienced observer probably misread a new instrument that they had not been trained to interpret. "
            "The decertification of this former record led researchers to also investigate the former and current recordings made in Death Valley in 1913. "
            "One of the earliest objections came in 1949 by Dr. Arnold Court, who concluded that the temperature may have been the result of a sandstorm that occurred at the time. "
            "Court stated that \"such a storm may have caused superheated surface materials to hit upon the temperature in the shelter.\" "
            "Modern weather historians such as Christopher C. Burt and William Taylor Reid have also claimed that the 1913 Death Valley reading is \"a myth\", and is at least 2.2 to 2.8 °C (4 to 5 °F) too high. "
            "A 2026 peer-reviewed study published in the Bulletin of the American Meteorological Society concluded that the 1913 reading is about 7.8 °C (14 °F) too high, which would invalidate it as the world record. "
            "The WMO has come out in support of the current record, stating that \"We accept that Death Valley temperature extreme record. If any new materials on it surface, we will be prepared to open an investigation",
            nome="Highest temperature recorded on Earth")],
    },
    # 7 Son Doong: a maior caverna, achada e esquecida
    {
        "temas_secundarios": ["minerais_rochas", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Em 1990, um vietnamita que buscava madeira valiosa achou a entrada da maior caverna do mundo. Assustado com o barulho de água e o vento que saíam dela, foi embora e esqueceu onde era. Só a reachou em 2008.",
        "explicacao": (
            "O homem, Hồ Khanh, procurava agarwood, uma madeira valiosa, quando encontrou a entrada em 10 de "
            "dezembro de 1990. Chegou a se aproximar, mas o ronco de água corrente e o vento forte que saía da "
            "abertura o desanimaram. Sem achar que fosse importante, ao voltar para casa já não lembrava o local "
            "exato. Mais tarde, comentou a descoberta com dois membros da Associação Britânica de Pesquisa de "
            "Cavernas, que exploravam a região e lhe pediram que tentasse reencontrar a entrada. Ele conseguiu em "
            "2008 e, em 2009, guiou a expedição. A Sơn Đoòng, no parque nacional Phong Nha–Kẻ Bàng, tem a maior "
            "galeria de caverna conhecida em volume: mais de 5 km de comprimento, 200 metros de altura e 150 de "
            "largura. Seu interior comportaria um quarteirão inteiro de Nova York, com arranha-céus, e um Boeing 747 "
            "passaria voando sem que as asas tocassem as paredes. Em dois pontos o teto desabou, abrindo dolinas por "
            "onde entra a luz do sol, e ali crescem árvores e outras plantas. A caverna guarda estalagmites de até "
            "80 metros e pérolas de caverna do tamanho de bolas de beisebol. Uma parede de 60 metros, apelidada de "
            "Grande Muralha do Vietnã, só foi vencida em 2010."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Hang_Son_Doong",
            "in Phong Nha–Kẻ Bàng National Park, Quảng Trị province, Vietnam, is the world's largest natural cave. [...] "
            "The entrance to Hang Sơn Đoòng was found on December 10, 1990 by a local man named Hồ Khanh, while searching for agarwood, a valuable timber. "
            "Although he initially went to investigate further, he was discouraged upon approach by the sound of rushing water and the strong wind issuing from the entrance. "
            "Not thinking it to be of any great importance, by the time he returned to his home, he had forgotten the exact location of the entrance. "
            "Later, he mentioned his discovery in passing to two members of the British Cave Research Association (BCRA), who were exploring in the local area. "
            "They asked him to attempt to rediscover the entrance, which he eventually managed to do in 2008, and in 2009, he led an expedition from the BCRA to the entrance. [...] "
            "Their progress in exploring the cave's full length was stopped by a large, 60-metre (200 ft) high flowstone-coated wall, which the expedition named the Great Wall of Vietnam. "
            "The expedition returned in March 2010 and successfully traversed the wall [...] "
            "the main Sơn Đoòng cave passage is the largest known cave passage in the world by volume [...] "
            "It is more than 5 kilometres (3.1 mi) long, 200 metres (660 ft) high and 150 metres (490 ft) wide. [...] "
            "The cave runs for about 9 km (5.6 mi) and is punctuated by two large dolines, areas where the ceiling of the cave has collapsed. "
            "The dolines allow sunlight to enter sections of the cave, resulting in the growth of trees and other vegetation. [...] "
            "The cave contains some of the tallest known stalagmites in the world, which are up to 80 m (260 ft) tall. "
            "Behind the Great Wall of Vietnam were found cave pearls the size of baseballs, an abnormally large size. "
            "The cave's interior is so large that it could fit an entire New York block inside, including skyscrapers, or could have a Boeing 747 fly through it without its wings touching either side.",
            nome="Hang Sơn Đoòng")],
    },
    # 8 Salar de Uyuni: régua para satélites
    {
        "temas_secundarios": ["exploracao_espacial", "medidas_padroes", "minerais_rochas"],
        "tipos_espanto": ["escala_absurda", "engenhosidade"],
        "gancho": "O Salar de Uyuni, na Bolívia, tem 10.582 km² de sal, e a altitude varia menos de um metro em toda essa área. É tão plano e claro que agências espaciais o usam para calibrar instrumentos de satélites.",
        "explicacao": (
            "O salar fica a cerca de 3.656 metros de altitude, perto do alto dos Andes, e é o maior do mundo, com "
            "uns 10.582 km². Ele surgiu da secagem progressiva de uma série de lagos pré-históricos; um deles, o "
            "paleolago Tauca, chegou a 140 metros de profundidade. Ficou para trás uma crosta de sal que cobre uma "
            "salmoura excepcionalmente rica em lítio. A combinação de área enorme, céu limpo e superfície plana faz "
            "do salar um lugar ideal para calibrar os altímetros de satélites de observação da Terra. Como ele "
            "reflete a maior parte da luz do sol que recebe, também serve para ajustar sensores ópticos: o "
            "instrumento do Landsat-5 foi calibrado em voo usando o salar como alvo estável. Em 2014, poucas semanas "
            "depois do lançamento, o satélite europeu Sentinel-1A sobrevoou o salar para calibrar medições de relevo "
            "feitas por radar. E depois da chuva, uma lâmina fina de água parada transforma o salar no maior "
            "espelho do mundo, com 129 km de ponta a ponta."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Salar_de_Uyuni",
            "Salar de Uyuni is the largest salt flat in the world, with an area of approximately 10,582 square kilometres (4,086 mi2). "
            "It is situated in southwestern Bolivia, within the Daniel Campos Province of the Potosí Department, near the crest of the Andes Mountains, at an elevation of 3,656 m (11,995 ft) above sea level. "
            "The Salar was formed as a result of transformations of seven Late Pleistocene lakes whose progressive desiccation led to the accumulation of extensive evaporitic salt deposits. [...] "
            "The average elevation varies by less than one meter over the entire area of the Salar. "
            "The crust serves as a source of salt and covers a pool of brine, which is exceptionally rich in lithium. "
            "The large area, clear skies, and exceptional flatness of the surface make the Salar ideal for calibrating the altimeters of Earth observation satellites. "
            "Following rain, a thin layer of dead calm water transforms the flat into the world's largest mirror, 129 km (80 miles) across. [...] "
            "Paleo Lake Tauca having a maximal depth of 140 meters (460 ft) [...] "
            "Its exceptionally high albedo, which reflects the majority of incoming sunlight, together with its vast, uniform terrain, makes it uniquely well-suited for remote sensing applications. [...] "
            "the Landsat-5 satellite's Thematic Mapper (TM) was calibrated “in-flight” by using the salar as a radiometrically stable target [...] "
            "In April 2014, the European Space Agency’s (ESA) Sentinel‑1A satellite surveyed the salar a few weeks after its launch as part of the Copernicus programme. "
            "The mission focused on calibrating radar-based measurements of surface topography.",
            nome="Salar de Uyuni")],
    },
    # 9 La Rinconada: 30 dias sem salário a 5.000 m
    {
        "temas_secundarios": ["corpo_extremo", "economia_curiosa", "cidades"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Em La Rinconada, no Peru, o maior povoado permanente mais alto do mundo, a até 5.100 m, muitos mineiros de ouro trabalham 30 dias sem salário. Num dia, trabalham para si e levam o minério que aguentam nos ombros.",
        "explicacao": (
            "A cidade fica nos Andes peruanos, entre 4.900 e 5.100 metros de altitude, na encosta do monte Ananea e "
            "ao pé de uma geleira. A cidade de população comparável mais alta, Nagqu, fica mais de 500 metros "
            "abaixo. O clima lembra mais o da costa oeste da Groenlândia do que o de um lugar a 14° do equador: a "
            "média anual é de 1,3 °C, e as noites têm temperaturas de congelamento o ano inteiro. O que atraiu gente "
            "foi o ouro. Entre 2001 e 2009, o preço do metal subiu 235%, e a National Geographic estimou que o "
            "antigo acampamento de garimpeiros chegou a 30 mil habitantes, número que os censos não confirmam. "
            "Muitos mineiros trabalham na mina da Corporación Ananea, a única empresa com licença do governo para "
            "minerar ali, sob o sistema chamado cachorreo: 30 dias sem pagamento e um dia trabalhando para si, "
            "quando podem levar todo o minério que conseguirem carregar nos ombros. Se a pedra tem ouro ou não, é "
            "questão de sorte, e um mineiro contou que nesse dia os homens costumam ser mandados para áreas onde não "
            "há nada. Às vezes o sistema termina com o trabalhador sem receber nada."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("La_Rinconada,_Peru",
            "La Rinconada is a town in the Peruvian Andes near a gold mine. "
            "At up to 5,100 m (16,700 ft; 3.2 mi) above sea level, it is the highest larger permanent settlement in the world. "
            "Between 2001 and 2009, the population was estimated by National Geographic to have increased to 30,000 people from a small gold prospector camp because the price of gold rose 235% over that period, although this number has not been reflected by the 2007 or 2017 censuses. [...] "
            "The town lies at a height of 4,900 m (16,100 ft; 3.0 mi) to 5,100 m (16,700 ft; 3.2 mi) with the center at 5,000 m (16,000 ft; 3.1 mi) above sea level, on the side of Mount Ananea and at the foot of a glacier [...] "
            "the highest city of comparable population (Nagqu) being over 500 m (1,600 ft; 0.31 mi) closer to sea level. [...] "
            "climatic conditions more closely resemble those of the west coast of Greenland than somewhere only 14° from the equator. "
            "The town has rainy summers and dry winters with a large diurnal variation seeing cool to cold days and freezing night time temperatures throughout the year, with snowfalls common. "
            "The average annual temperature in La Rinconada is 1.3 °C (34.3 °F) [...] "
            "The only company with a governmental license to mine in La Rinconada is called Corporación Ananea, thus many miners work at the gold mine owned by Corporación Ananea. "
            "Under the cachorreo system, they work for 30 days without payment and for one day they are allowed to work for themselves. "
            "At this day of the month, the miners are allowed to take with them as much ore as they can carry on their shoulders. "
            "However, a miner stated \"The problem is, though, that on the crucial day the men are usually sent to areas where there's nothing to find.\" "
            "Whether the ore contains any gold or not is a matter of luck. Pocketing of nuggets or promising chunks of rich ore is tolerated. "
            "This system sometimes ends with miners not being compensated for their work.",
            nome="La Rinconada, Peru")],
    },
    # 10 Lençóis Maranhenses: o "deserto" que não é deserto
    {
        "temas_secundarios": ["biomas_brasileiros", "agua_doce_gelo"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "Os Lençóis Maranhenses parecem um deserto, mas não são: recebem cerca de 1.200 mm de chuva por ano, e deserto, por definição, tem menos de 250 mm. Na seca, um peixe das lagoas se enterra na lama e espera.",
        "explicacao": (
            "O parque nacional, no litoral do Maranhão, protege 155 mil hectares de dunas, com 70 km de costa. A "
            "areia vem do interior, trazida pelos rios Parnaíba e Preguiças, e depois é empurrada pelo vento até "
            "50 km para dentro do continente, formando dunas de até 40 metros. Cerca de 70% da chuva cai entre "
            "janeiro e maio. Nessa época, a água enche os vales entre as dunas e forma lagoas de água doce de até "
            "100 metros de comprimento e 3 de profundidade, que somadas podem cobrir 41% da área do parque. Elas não "
            "escoam porque há uma camada de rocha impermeável sob a areia. Quando a seca volta, as lagoas evaporam "
            "depressa, perdendo até 1 metro de profundidade por mês. Mesmo assim, há peixes e insetos nelas. Um "
            "desses peixes, chamado em inglês de wolf fish, se enterra em camadas úmidas de lama e fica dormente "
            "durante a estação seca. Em 2024, os Lençóis foram declarados Patrimônio Mundial pela UNESCO."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Len%C3%A7%C3%B3is_Maranhenses_National_Park",
            "In July 2024, the site was declared a UNESCO World Heritage Site [...] "
            "bordered by 70 kilometres (43 mi) of beaches along the Atlantic Ocean. [...] "
            "The park encompasses an area of 155,000 hectares (380,000 acres), composed mainly of expansive coastal dune fields [...] "
            "While much of the park has the appearance of a desert, the area receives about 1,200 millimetres (47 in) of rain per year, while deserts, by definition, receive less than 250 millimetres (10 in) annually. "
            "About 70% of this rainfall occurs between the months of January and May. "
            "The sand is carried to the park from the interior of the continent by the Parnaíba and Preguiças rivers, where it is then driven back inland up to 50 kilometres (31 mi) by winds, creating a series of sand dunes rising as much as 40 metres (130 ft) tall. "
            "During the rainy season, between the months of January and June, the rainstorms fill the spaces among the dunes with fresh water lagoons of up to 100 metres (330 ft) in length and 3 metres (10 ft) in depth, and together comprising as much as 41% of the area of the park. "
            "The water in the lagoons is prevented from draining by a layer of impermeable rock located beneath the sandy surface. [...] "
            "When the dry season returns, the pools quickly evaporate, losing as much as 1 metre (3 ft) of depth per month. [...] "
            "They are home to a number of fish and insect species, including the wolf fish, which burrows down into wet layers of mud and remains dormant during the dry season.",
            nome="Lençóis Maranhenses National Park")],
    },
    # 11 Lechuguilla: o vento sob o entulho e a caverna escavada de baixo para cima
    {
        "temas_secundarios": ["minerais_rochas", "geologia_profunda"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Nos anos 1950, exploradores ouviram vento rugindo sob o entulho de uma caverna pequena no Novo México. Cavaram e, em 1986, abriram caminho para a Lechuguilla, com 244,8 km de galerias escavadas de baixo para cima.",
        "explicacao": (
            "Até 1986, a Lechuguilla, no Parque Nacional das Cavernas de Carlsbad, era um sítio histórico sem "
            "importância: um poço de entrada de 27 metros e uns 122 metros de passagens secas e sem saída, de onde "
            "se extraiu guano de morcego por um ano, com base numa licença de mineração de 1914. O vento que subia "
            "do chão coberto de entulho fez as pessoas concluírem que havia mais caverna embaixo. Em 1984, um grupo "
            "de espeleólogos do Colorado, liderado por Dave Allured, conseguiu autorização para cavar e, em 25 de "
            "maio de 1986, rompeu para galerias amplas. Hoje são 244,8 km explorados, o que faz dela a nona caverna "
            "mais longa conhecida. A origem também é incomum. O mecanismo habitual dissolve o calcário de cima para "
            "baixo, com ácido carbônico. A Lechuguilla foi dissolvida de baixo para cima, por ácido sulfúrico, que "
            "teria vindo de sulfeto de hidrogênio migrado de jazidas de petróleo próximas. A abundância de gipsita "
            "e enxofre lá dentro sustenta essa explicação: há lustres de gipsita de 6,1 metros e depósitos de enxofre "
            "amarelo-limão."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Lechuguilla_Cave",
            "At 152.11 miles (244.80 km), it is the ninth-longest explored cave in the world. [...] "
            "Lechuguilla Cave was known until 1986 as a small, insignificant historic site in the park's back country. "
            "Small amounts of bat guano were mined from the entrance passages for a year under a mining claim filed in 1914. "
            "The historic cave contained a 90-foot (27 m) entrance pit known as Misery Hole, which led to 400 feet (122 m) of dry, dead-end passages. "
            "The cave was visited infrequently after mining activities ceased. "
            "However, in the 1950s, cavers heard wind roaring up from the rubble-choked cave floor. "
            "Although no route was obvious, people concluded that more cave passages were present below the rubble. "
            "Led by Dave Allured, a group of cavers from the Colorado Grotto gained permission from the National Park Service to begin digging in 1984. "
            "On May 25, 1986, they broke through into large, naturally-occurring walking passages. [...] "
            "Lechuguilla Cave holds a variety of rare speleothems, including lemon-yellow sulfur deposits, 20-foot (6.1 m) gypsum chandeliers [...] "
            "The profusion of gypsum and sulfur supports speleogenesis by sulfuric acid dissolution. "
            "The sulfuric acid is believed to be derived from hydrogen sulfide that migrated from nearby oil deposits. "
            "The cavern formed from the bottom up, unlike the normal top-down carbonic acid dissolution mechanism of cave formation.",
            nome="Lechuguilla Cave")],
    },
    # 12 as pedras que andam no Vale da Morte
    {
        "temas_secundarios": ["agua_doce_gelo", "clima_tempo"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "No Vale da Morte, pedras do peso de uma pessoa deixam rastros no leito seco de um lago, e por décadas ninguém as viu andar. Em 2013, GPS e câmeras flagraram o motor: placas de gelo de milímetros e vento fraco.",
        "explicacao": (
            "Os rastros da Racetrack Playa, na Califórnia, são estudados desde o começo do século XX; o primeiro "
            "relato documentado é de 1915, de um garimpeiro. Por décadas, as hipóteses dividiram os geólogos: "
            "ventos fortes sobre a lama molhada, colares de gelo que ajudariam a pegar vento, placas de gelo que "
            "fariam as pedras flutuar. Algumas pedras pesam tanto quanto uma pessoa, o que parecia demais para o "
            "vento da região. Flagrar o movimento era difícil, porque ele acontece mais ou menos uma vez a cada três "
            "anos. Uma equipe passou a monitorar o lugar com GPS e fotografia em intervalos e, em 20 de dezembro de "
            "2013, registrou o maior movimento: mais de 60 pedras, algumas das quais percorreram até 224 metros "
            "entre dezembro e janeiro, em vários episódios. O que se viu contrariou as hipóteses de vento forte e de "
            "gelo grosso. Nas noites frias, a água de uma lagoa temporária congela em placas de poucos milímetros. "
            "Em manhãs de sol, elas começam a se partir e, levadas por vento leve, empurram as pedras a até 5 metros "
            "por minuto. Alguns deslocamentos medidos duraram até 16 minutos, e várias pedras se moveram mais de "
            "cinco vezes naquele inverno."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Sailing_stones",
            "most famously at Racetrack Playa, Death Valley National Park, California [...] "
            "At Racetrack Playa, these tracks have been studied since the early 1900s, yet the origins of stone movement were not confirmed and remained the subject of research for which several hypotheses existed. [...] "
            "The first documented account of the sliding rock phenomenon dates to 1915, when a prospector named Joseph Crook from Fallon, Nevada, visited the Racetrack Playa site. [...] "
            "Most hypotheses favored by interested geologists posit that strong winds when the mud is wet are at least in part responsible. "
            "Some stones weigh as much as a human, which some researchers, such as geologist George M. Stanley, who published a paper on the topic in 1955, feel is too heavy for the area's winds to move. [...] "
            "the difficulty of capturing the Racetrack's stealthy rocks, as movements only occur about once every three years [...] "
            "News articles reported the mystery solved when researchers observed rock movements using GPS and time-lapse photography. "
            "The largest rock movement the research team witnessed and documented was on December 20, 2013, and involved more than 60 rocks, with some rocks moving up to 224 meters (245 yards) between December 2013 and January 2014 in multiple movement events. "
            "These observations contradicted earlier hypotheses of strong winds or thick ice floating rocks off the surface. "
            "Instead, rocks move when large ice sheets a few millimeters thick floating in an ephemeral winter pond start to break up during sunny mornings. "
            "These thin, floating ice panels, frozen during cold winter nights, are driven by light winds, and shove rocks at up to 5 m/min (0.3 km/h; 0.2 mph). "
            "Some GPS-measured moves lasted up to 16 minutes, and a number of stones moved more than five times during the existence of the playa pond in the winter of 2013–14. [...] "
            "Sliding Rocks on Racetrack Playa, Death Valley National Park: First Observation of Rocks in Motion",
            nome="Sailing stones")],
    },
    # 13 Darvaza: a "Porta do Inferno" de origem incerta
    {
        "temas_secundarios": ["energia", "guerra_fria"],
        "tipos_espanto": ["misterio_aberto", "historia_humana"],
        "gancho": "A cratera de gás em chamas de Darvaza, no Turcomenistão, a \"Porta do Inferno\", tem origem incerta. A versão mais contada fala numa perfuração soviética em 1971, mas os registros faltam, são secretos ou inacessíveis.",
        "explicacao": (
            "A cratera fica no meio do deserto de Karakum, a cerca de 260 km da capital, Ashgabat, e tem de 60 a 70 "
            "metros de diâmetro e uns 30 de profundidade. É um campo de gás natural que desabou numa cavidade, e "
            "centenas de chamas iluminam o fundo e a borda. A teoria mais comum diz que uma perfuração atingiu uma "
            "caverna de gás, o teto desabou e, segundo algumas fontes, engenheiros puseram fogo para evitar que "
            "gases venenosos se espalhassem. Os detalhes mudam conforme quem conta. Uns afirmam que engenheiros "
            "soviéticos perfuraram ali em 1971 em busca de petróleo, o terreno desabou em poucos dias e eles "
            "subestimaram o volume de gás ao queimá-lo. Geólogos locais dizem que o desabamento ocorreu nos anos "
            "1960 e que o fogo só foi aceso nos anos 1980. Os documentos da época faltam nos arquivos, são "
            "secretos ou estão inacessíveis. Em 2013, o explorador George Kourounis foi o primeiro a pisar no fundo "
            "da cratera, com roupa aluminizada e ar próprio, para coletar amostras de solo. Depois, o governo "
            "anunciou planos de apagar o fogo; em 2025, as autoridades disseram que as chamas tinham diminuído a um "
            "terço, e poços foram perfurados em volta para captar metano."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Darvaza_gas_crater",
            "The Darvaza gas crater (Turkmen: Garagum ýalkymy), also known as the Door to Hell or Gates of Hell, and known officially as the Shining of Karakum, is a burning natural gas field collapsed into a cavern near Darvaza, Turkmenistan. "
            "Hundreds of natural gas fires illuminate the floor and rim of the crater. [...] "
            "The most common theory for the forming of the crater is that drilling punctured a natural-gas cavern, the cavern's roof collapsed, and (some sources say) engineers ignited the crater to prevent poisonous gases from spreading. "
            "The crater is near the village of Darvaza in the middle of the Karakum Desert. "
            "Located about 260 kilometres (160 mi) north of Ashgabat (the capital of Turkmenistan), it has a diameter of 60–70 metres (200–230 ft) and a depth of about 30 metres (98 ft). [...] "
            "The early years of the crater's history are still being determined. "
            "Relevant records are either absent from the archives, classified, or inaccessible. "
            "Some local geologists have claimed that the collapse of a crater happened in the 1960s; it was set on fire only in the 1980s to prevent the emission of poisonous gases. "
            "Others assert that the site was drilled by Soviet engineers in 1971 as an oil field but collapsed within days, forming the crater, with the engineers choosing to flare the crater to prevent the emission of poisonous gases but underestimating the volume of the gas. [...] "
            "announced plans to extinguish the crater, citing deleterious effects on local health, the environment, and the natural gas industry. [...] "
            "In 2025, authorities declared that the size of the fire had been reduced three-fold over an unspecified timeframe, while several wells were drilled around the crater to capture methane. [...] "
            "In 2013, George Kourounis became the first person to set foot at the bottom of the crater; he was gathering soil samples for the Extreme Microbiome Project. [...] "
            "Kourounis used a custom-made Kevlar harness and multiple Technora ropes attached to a full-body aluminized suit with a self-contained breathing apparatus.",
            nome="Darvaza gas crater")],
    },
    # 14 o frio da Antártida que não entra no recorde
    {
        "temas_secundarios": ["clima_tempo", "atmosfera", "termodinamica"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "O recorde oficial de frio é de −89,2 °C, medido no ar na estação Vostok, na Antártida, em 1983. Mas satélites acharam vários pontos do alto da Antártida onde a superfície da neve chega a cerca de −98 °C.",
        "explicacao": (
            "A medição de 21 de julho de 1983 foi feita no chão, na então soviética estação Vostok, e continua "
            "sendo o recorde de temperatura registrada diretamente. Antes dela, a própria Vostok tinha marcado "
            "−88,3 °C, em 1968. Em 10 de agosto de 2010, observações de satélite registraram −92 °C numa crista "
            "entre os domos Argus e Fuji, a 3.900 metros de altitude. O número foi apresentado em 2013, num "
            "encontro da União Geofísica Americana, e é provisório. Ele não conta como recorde por dois motivos: "
            "foi obtido por sensoriamento remoto, e não por termômetros no chão, e mede a superfície do gelo, e não "
            "o ar acima dela, como em Vostok. Por isso as duas medidas não são diretamente comparáveis. Trabalhos "
            "posteriores mostraram muitos pontos no alto da Antártida onde a superfície cai a cerca de −98 °C. Como "
            "a temperatura muda muito logo acima da superfície, isso indica que o ar junto ao chão chega a mínimas "
            "de aproximadamente −94 °C, abaixo do recorde oficial."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Lowest_temperature_recorded_on_Earth",
            "The lowest natural temperature ever directly recorded at ground level on Earth is −89.2 °C (−128.6 °F; 184.0 K) at the then-Soviet Vostok Station in Antarctica on 21 July 1983 by ground measurements. "
            "On 10 August 2010, satellite observations showed a surface temperature of −92 °C (−134 °F; 181 K) at 81.8°S 59.3°E [...] "
            "along a ridge between Dome Argus and Dome Fuji, at 3,900 m (12,800 ft) elevation. "
            "The result was reported at the 46th annual meeting of the American Geophysical Union in San Francisco, California, in December 2013; it is a provisional figure, and may be subject to revision. "
            "The value is not listed as the record lowest temperature as it was measured by remote sensing from satellite and not by ground-based thermometers, unlike the 1983 record. "
            "The temperature announced reflects that of the ice surface, while the Vostok readings measured the air above the ice, and so the two are not directly comparable. "
            "Later work shows many locations in the high Antarctic where surface temperatures drop to approximately −98 °C (−144 °F; 175 K). "
            "Due to the very strong temperature gradient near the surface, these imply near-surface air temperature minima of approximately −94 °C (−137 °F; 179 K). [...] "
            "The next world record low temperature was a reading of −88.3 °C (−126.9 °F; 184.8 K), measured at the Soviet Vostok Station in 1968, on the Antarctic Plateau.",
            nome="Lowest temperature recorded on Earth")],
    },
    # 15 caverna Movile: um mundo selado
    {
        "temas_secundarios": ["animais_extremos", "astrobiologia", "ecologia"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "Na Romênia, uma caverna achada em 1986 durante uma obra abriga 57 espécies de animais, 37 delas exclusivas dali. Selada há cerca de 5,5 milhões de anos, tem uma cadeia alimentar que não começa na luz do Sol.",
        "explicacao": (
            "A caverna Movile fica perto de Mangalia, a poucos quilômetros do mar Negro, e foi descoberta em 1986 "
            "por Cristian Lascu durante obras de construção. São cerca de 200 metros de galerias em calcário, em "
            "parte inundadas por águas termais, a 21 °C constantes e com umidade relativa de quase 100%. O ar lá "
            "dentro é muito diferente do de fora: tem só de 7% a 10% de oxigênio, contra 21% na atmosfera, cerca de "
            "100 vezes mais gás carbônico, além de metano, amônia e sulfeto de hidrogênio. A caverna está isolada "
            "da superfície há cerca de 5,5 milhões de anos, e a vida ali se baseia na quimiossíntese: bactérias que "
            "tiram energia oxidando sulfeto de hidrogênio e metano formam a base da cadeia alimentar. Delas se "
            "alimentam pastadores, que são caçados por predadores. Das 57 espécies animais conhecidas, entre elas "
            "sanguessugas, aranhas, pseudoescorpiões e um escorpião-d'água, 37 são endêmicas. O maior predador é uma "
            "centopeia, a Cryptops speleorex. Nem todos chegaram ao mesmo tempo: o único caracol da caverna vive ali "
            "há pouco mais de 2 milhões de anos. Muitas espécies não têm olhos funcionais. O acesso é restrito a "
            "poucos pesquisadores por ano."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Movile_Cave",
            "Movile Cave (Romanian: Peștera Movile) is a cave near Mangalia, Constanța County, Romania discovered in 1986 by Cristian Lascu during construction work a few kilometers from the Black Sea coast. [...] "
            "Life in the cave has been separated from the outside for the past 5.5 million years and it is based completely on chemosynthesis. [...] "
            "Movile Cave is a network of paths in limestone that are approximately 200 metres (660 ft) long, with portions that are partially or fully submerged by hydrothermal waters. "
            "The temperature of the air and water is a constant 21 °C (70 °F) and the relative humidity is about 100%. "
            "Access to the cave is limited to a few researchers per year, to minimize external impact on the delicate ecosystem. [...] "
            "(7–10% O2 in the cave atmosphere, compared to 21% O2 in air), and about 100 times more carbon dioxide (2–3.5% CO2 in the cave atmosphere, versus 0.04% CO2 in air). "
            "It also contains 1–2% methane (CH4) and both the air and waters of the cave contain high concentrations of hydrogen sulfide (H2S) and ammonia (NH3). [...] "
            "These bacteria derive energy from oxidizing hydrogen sulfide and methane, forming the base of the food web. [...] "
            "The cave is known to contain 57 animal species, among them leeches, spiders, pseudoscorpions, woodlice, centipedes (Cryptops speleorex), water scorpions (Nepa anophthalma), and also snails. "
            "Of these, 37 are endemic. "
            "While animals have lived in the cave for 5.5 million years, not all of them arrived simultaneously. "
            "One of the most recent animals recorded is the cave's only species of snail, Heleobia dobrogica, which has inhabited the cave for slightly more than 2 million years. [...] "
            "Many of these species lack functional eyes [...] "
            "with grazers feeding on bacterial biofilms and higher level consumers preying on the primary consumers. [...] "
            "The largest invertebrate and top predator in the cave is the centipede Cryptops speleorex",
            nome="Movile Cave")],
    },
]
