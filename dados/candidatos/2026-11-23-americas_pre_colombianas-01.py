LOTE = "2026-11-23-americas_pre_colombianas-01"
AREA = "historia_antiga"
TEMA = "americas_pre_colombianas"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


ANTIQUITY = {
    "url": "https://www.cambridge.org/core/journals/antiquity/article/running-out-of-empty-space-environmental-lidar-and-the-crowded-ancient-landscape-of-campeche-mexico/FFDB435047017853F26CFC5D8804B08D",
    "titulo": "Running out of empty space: environmental lidar and the crowded ancient landscape of Campeche, Mexico (Antiquity, 2024)",
    "idioma": "en",
}

CANDIDATOS = [
    # 1 Valeriana: a cidade maia achada em dados de laser feitos para medir floresta
    {
        "temas_secundarios": ["ia_robotica", "cidades"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Num estudo publicado em 2024, uma cidade maia com pirâmides e quadra de jogo de bola apareceu em dados de laser coletados para monitorar uma floresta. Ficava junto à única rodovia da região, e a ciência não sabia dela.",
        "explicacao": (
            "O lidar dispara pulsos de laser de um avião e monta um modelo 3D do terreno, mesmo sob mata fechada. "
            "Em 2013, um projeto de monitoramento florestal no México, voltado a reduzir emissões do desmatamento, "
            "fez um levantamento desse tipo em Campeche e deixou os dados livres. Pesquisadores da Universidade "
            "Tulane, liderados pelo doutorando Luke Auld-Thomas, reexaminaram cerca de 122 km² desse material com "
            "olhos de arqueólogo. Acharam mais de 6.500 estruturas pré-hispânicas e uma grande cidade desconhecida, "
            "que batizaram de Valeriana, por causa de uma lagoa vizinha. Ela tem todas as marcas de uma capital maia "
            "clássica: praças fechadas ligadas por uma calçada larga, templos-pirâmide, quadra de jogo de bola e um "
            "reservatório feito ao represar um riacho sazonal. Segundo Auld-Thomas, ficava junto à única rodovia da "
            "área, perto de uma cidade onde se planta entre as ruínas há anos, e nem o governo nem os cientistas "
            "sabiam dela. Como os dados não foram coletados com perguntas arqueológicas em mente, funcionam quase "
            "como uma amostra ao acaso. Isso pesa num debate: os mapas feitos em torno de sítios famosos, como Tikal, "
            "exageravam a densidade maia? Para os autores, não: cidades e povoamento denso eram comuns em grandes "
            "áreas das terras baixas maias centrais."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            dict(ANTIQUITY, trecho=(
                "Published online by Cambridge University Press: 29 October 2024 [...] "
                "Here, we present an archaeological analysis of approximately 122km2 of high-quality airborne lidar data collected in 2013 as part of a forest monitoring project called Alianza M-REDD+ (Reducing Emissions from Deforestation and Degradation in Mexico) [...] "
                "made freely available by Alianza M-REDD+ [...] "
                "these expedient datasets have the advantage of being effectively random with regards to the archaeological record; as the data were collected without regard for archaeological questions [...] "
                "Block 2 directly overlies the epicentre of a major urban area that was previously unknown to the scientific community. "
                "This city, which we call Valeriana (Figures 3, 4 & 5) after an adjacent freshwater lagoon [...] "
                "The larger of Valeriana's two monumental precincts has all the hallmarks of a Classic Maya political capital: multiple enclosed plazas connected by a broad causeway; temple pyramids; a ballcourt; a reservoir formed by damming an arroyo (a seasonal watercourse) [...] "
                "we can only conclude that cities and dense settlement are simply ubiquitous across large swaths of the central Maya Lowlands."
            )),
            {"url": "https://www.sciencedaily.com/releases/2024/10/241029121056.htm",
             "titulo": "Have we found all the major Maya cities? Not even close, new research suggests (Tulane University via ScienceDaily)",
             "idioma": "en",
             "trecho": (
                 "was led by Tulane University anthropology doctoral student Luke Auld-Thomas and his advisor, Professor Marcello A. Canuto. [...] "
                 "Their findings included evidence of more than 6,500 pre-Hispanic structures, including a previously unknown large city complete with iconic stone pyramids. [...] "
                 "Lidar technology uses laser pulses to measure distances and create three-dimensional models of specific areas. [...] "
                 "We also found a large city with pyramids right next to the area's only highway, near a town where people have been actively farming among the ruins for years. "
                 "The government never knew about it; the scientific community never knew about it. [...] "
                 "The counterargument was that lidar surveys were still too tethered to known, large sites, such as Tikal, and therefore had developed a distorted image of the Maya lowlands."
             )},
        ],
    },
    # 2 Chasquis: correio a pé em revezamento e peixe vivo em Cusco
    {
        "temas_secundarios": ["telecomunicacoes", "transportes"],
        "tipos_espanto": ["engenhosidade", "escala_absurda"],
        "gancho": "Sem usar a roda, o Império Inca mandava recados por corredores em revezamento, com postos a cada 2,5 km. Segundo um cronista, o imperador recebia em Cusco peixe do mar ainda vivo, vindo de 350 a 400 km.",
        "explicacao": (
            "A rede de estradas inca, o Qhapaq Ñan, somava cerca de 40.000 km e era percorrida a pé: a roda não era "
            "usada para transporte. Ao longo dela havia postos chamados chaskiwasi, a uns 2,5 km uns dos outros, onde "
            "jovens mensageiros, os chasquis, vigiavam a estrada à espera do próximo colega. Ao avistar o posto, o "
            "corredor que chegava gritava e soprava uma trombeta de concha para alertar o substituto. Depois repetia "
            "o recado mais de uma vez, até o outro entender perfeitamente, e o novo corredor partia descansado. Os "
            "chasquis levavam mensagens faladas, pequenos pacotes e quipus, cordões com nós que registravam "
            "sobretudo números, como impostos ou soldados a deslocar; não há prova de que soubessem lê-los. "
            "Estima-se que o sistema levasse um recado ou um presente por até 300 km num dia. O cronista Martín de "
            "Murúa conta que, quando o Inca queria peixe fresco do mar, ele chegava vivo a Cusco, a 350 a 400 km do "
            "litoral, coisa que o próprio cronista achou incrível. Em 2014, a rede de estradas incas virou "
            "Patrimônio Mundial da UNESCO."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Chasqui",
                "they were in charge of carrying messages in the form of quipus, oral information, or small packets. "
                "Along the Inca road system there were relay stations called chaskiwasi (house of chasqui), placed at about 2.5 kilometres (1.6 mi) from each other, where the chasqui switched, exchanging their message(s) with the fresh messenger. "
                "The chasqui system could deliver a message or a gift along a distance of up to 300 kilometres (190 mi) per day. [...] "
                "Quipus could represent the amount of taxes to be paid by a village or a province or the number of soldiers to be moved. "
                "There is no evidence that the chasquis could read the quipus [...] "
                "The waiting chasquis would constantly surveil the road to spot the incoming runner, the latter of which shouted within sight of the hut and played his seashell trumpet, in order to alert the new one to take his place. "
                "He gave his message, repeating it more than once, until the new chasqui understood it perfectly. [...] "
                "Murúa confirms that \"When the Inca wanted to eat fresh fish from the sea, since it was seventy or eighty leagues [350 to 400 kilometres (220 to 250 mi)] (from the coast) to Cuzco, where he lived, they would bring it to him alive, which indeed seems an incredible thing",
                nome="Chasqui"),
            wiki("Inca_road_system",
                "It was about 40,000 kilometres (25,000 mi) long in total. [...] "
                "Transportation was done on foot as in pre-Columbian America; the use of wheels for transportation was not known. [...] "
                "In 2014 the road system became a UNESCO World Heritage Site.",
                nome="Inca road system"),
        ],
    },
    # 3 Machu Picchu: o nome talvez errado e o descobridor que chegou antes de Bingham
    {
        "temas_secundarios": ["nomes_lugares", "personagens_esquecidos"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "Machu Picchu talvez não se chamasse Machu Picchu. Um estudo de 2021 sugere que o lugar era Huayna Picchu, ou só Picchu, e que o nome atual pegou com as publicações de Hiram Bingham, a partir de 1911.",
        "explicacao": (
            "A cidadela inca fica numa sela estreita entre dois picos. Em quíchua, machu quer dizer velho, wayna "
            "quer dizer jovem e pikchu é pico: Machu Picchu é o pico velho, e Huayna Picchu, o menor ao lado. Um "
            "estudo publicado em 2021 na revista Ñawpa Pacha, do Instituto de Estudos Andinos, usou anotações de "
            "campo de Bingham, mapas antigos e documentos históricos para concluir que o nome original provavelmente "
            "era Huayna Picchu, ou apenas Picchu. No fim do século XVI, espanhóis registraram indígenas falando em "
            "voltar a \"Huayna Picchu\", e um atlas de 1904 marcava o lugar com esse nome. Bingham, que procurava a "
            "capital perdida do Estado neoinca, também não foi o primeiro explorador a chegar lá: o sítio era "
            "conhecido pelos moradores da região. Em 1902, o peruano Agustín Lizárraga escreveu a carvão \"A. "
            "Lizárraga 1902\" na janela central do Templo das Três Janelas. Em 1911, Bingham viu a inscrição e, "
            "decepcionado de início, anotou no diário de campo que Lizárraga era o descobridor de Machu Picchu. "
            "Mas foi Bingham quem levou as ruínas à fama internacional."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Machu_Picchu",
                "Although the site was known locally and reached in the early 20th century by the Peruvian explorer Agustín Lizárraga, it was brought to international attention in 1911 by the American historian Hiram Bingham III. [...] "
                "The site is on a narrow saddle between two mountain peaks, Machu Picchu and Huayna Picchu. "
                "In the Quechua language, machu means 'old' or 'old person' and wayna (spelled huayna in standard Spanish orthography) means 'young', while pikchu refers to a 'summit', 'peak', or 'pyramid'. [...] "
                "a 2021 study in Ñawpa Pacha: Journal of the Institute of Andean Studies suggests that the site was likely called \"Huayna Picchu\", after the smaller peak nearby, or simply \"Picchu\". "
                "According to the research, the association of the name Machu Picchu with the ruins likely began with American explorer Hiram Bingham's 1911 publications, a conclusion supported by Bingham's field notes, early maps, and historical documents. [...] "
                "In the late 16th century, Spaniards who had gained control of the area documented that indigenous individuals mentioned returning to \"Huayna Picchu\" [...] "
                "a 1904 atlas labeled it as Huayna Picchu. [...] "
                "During that visit, Lizárraga marked his surname and the year, \"A. Lizárraga 1902\", in charcoal on the central window of the Temple of the Three Windows. "
                "In 1911, American historian and explorer Hiram Bingham traveled the region looking for the lost capital of the Neo-Inca state [...] "
                "Bingham found the surname of Lizárraga and the 1902 date on the temple. "
                "Initially disappointed, he documented in his pocket field journal: \"Agustín Lizárraga is discoverer of Machu Picchu",
                nome="Machu Picchu"),
        ],
    },
    # 4 Cahokia: a cidade indígena que pode ter sido maior que Londres
    {
        "temas_secundarios": ["cidades", "povos_indigenas"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Do outro lado do rio Mississippi, diante da atual St. Louis, nos EUA, houve no século XII uma cidade indígena que pode ter sido maior que Londres. Seu maior monte de terra tem 30 m de altura.",
        "explicacao": (
            "Cahokia foi o maior centro da cultura do Mississippi, que se espalhou por boa parte do centro e do "
            "sudeste dos atuais EUA a partir do ano 1000. Antes de cerca de 1050, morava ali umas mil pessoas; "
            "depois, a cidade cresceu depressa, ao que parece com muitos imigrantes de outras regiões. No auge, "
            "cobria uns 16 km² e tinha cerca de 120 montes de terra. As estimativas de população variam muito, de "
            "6.000 a 40.000 habitantes. Se as mais altas estiverem certas, nenhuma cidade dos EUA foi maior até a "
            "década de 1780, quando Filadélfia passou dos 40.000. Para erguer montes e praças, milhares de "
            "trabalhadores moveram, ao longo de décadas, mais de 1,6 milhão de m³ de terra em cestos trançados. O "
            "maior monte, o Monks Mound, cobre 5,7 hectares, sobe 30 m e era coroado por uma grande construção de "
            "madeira de mais 15 m. O nome original da cidade é desconhecido. \"Cahokia\" vem de um povo indígena que "
            "vivia na área quando os primeiros exploradores franceses chegaram, no século XVII, séculos depois do "
            "abandono da cidade. Hoje o sítio é Patrimônio Mundial da UNESCO."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Cahokia",
                "is the site of a Native American city which existed c. 1050 – c. 1350 AD, directly across the Mississippi River from present-day St. Louis. [...] "
                "At its apex around 1100 AD, the city covered about 6 square miles (16 km2), included about 120 earthworks [...] "
                "Cahokia was the largest and most influential urban settlement of the Mississippian culture, which developed advanced societies across much of what is now the Central and the Southeastern United States, beginning around 1000 AD. [...] "
                "The city's original name is unknown. "
                "The mounds were later named after the Cahokia tribe, a historic Illiniwek people living in the area when the first French explorers arrived in the 17th century. "
                "As this was centuries after Cahokia was abandoned by its original inhabitants [...] "
                "It is also one of the 26 UNESCO World Heritage Sites within the United States. [...] "
                "Home to about 1,000 people before circa 1050, its population grew rapidly after that date. [...] "
                "Archaeologists estimate the city's population at between 6,000 and 40,000 at its peak. "
                "If the highest population estimates are correct, Cahokia was larger than any subsequent city in the United States until the 1780s, when Philadelphia's population grew beyond 40,000. "
                "Its population in the 12th century may have been larger than that of London and Paris. "
                "Studies of Cahokia's rise see large-scale immigration as an essential contributor to the city's initial rapid growth. [...] "
                "thousands of workers over decades moved more than an estimated 55 million cubic feet (1,600,000 m3) of earth in woven baskets to create this network of mounds and community plazas. "
                "Monks Mound, for example, covers 14 acres (5.7 ha), rises 100 ft (30 m), and was topped by a massive 5,000 ft2 (460 m2) building another 50 ft (15 m) high.",
                nome="Cahokia"),
        ],
    },
    # 5 Caral: cidade da era das pirâmides egípcias, sem cerâmica e sem sinal de guerra
    {
        "temas_secundarios": ["primeiras_civilizacoes", "egito_antigo", "cidades"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "Enquanto o Egito erguia as grandes pirâmides, uma cidade com pirâmides próprias prosperava no Peru: Caral. Não tinha cerâmica, e ali não apareceu sinal de guerra: nem muralhas, nem armas, nem corpos mutilados.",
        "explicacao": (
            "Caral fica no vale do rio Supe, no litoral norte do Peru, e foi habitada de cerca de 2600 a 2000 a.C. "
            "É o maior sítio registrado nos Andes com datas anteriores a 2000 a.C., e seus escavadores a descrevem "
            "como o centro urbano mais antigo das Américas, título que outros pesquisadores contestam. Ela pertence "
            "à civilização de Caral-Supe, ou Norte Chico, que surgiu mil anos depois da Suméria e quase dois mil "
            "anos antes dos olmecas, na Mesoamérica. Essa sociedade não conhecia cerâmica, e dela não sobrou nenhuma "
            "arte visual. Também não há indícios de guerra: os povoados não tinham defesas. Isso contraria a teoria "
            "de que os primeiros Estados nasceram para defender recursos escassos. A economia ligava o litoral e o "
            "interior. Em Caral, os restos de animais são quase todos marinhos, com muita anchova e sardinha, e o "
            "algodão, principal produto da irrigação, virava redes de pesca e tecidos. Resumindo o trabalho da "
            "arqueóloga Ruth Shady, a BBC sugeriu que anchovas secas talvez servissem até como uma espécie de moeda "
            "para pagar quem trabalhava nas grandes obras."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Caral",
                "Caral was a thriving metropolis at roughly the same time as the great pyramids were being built in Egypt [...] "
                "Caral is the largest recorded site in the Andean region, with dates older than 2000 BC. [...] "
                "Caral was inhabited from around 2600 BC to 2000 BC [...] "
                "Caral has been described by its excavators as the oldest urban center in the Americas. This claim has been challenged [...] "
                "No indications of warfare, such as battlements, weapons, or mutilated bodies, have been found at Caral.",
                nome="Caral"),
            wiki("Norte_Chico_civilization",
                "Complex society in the Caral–Supe arose a millennium after Sumer in Mesopotamia, was contemporaneous with the Egyptian pyramids, and predated the Mesoamerican Olmecs by nearly two millennia. "
                "In archaeological nomenclature, Caral–Supe is a pre-ceramic culture of the pre-Columbian Late Archaic; it completely lacked ceramics and no evidence of visual art has survived. [...] "
                "Shady notes that \"animal remains are almost exclusively marine\" at Caral, including clams and mussels, and large amounts of anchovies and sardines. [...] "
                "In its summation of the 2001 Shady paper, the BBC suggests workers would have been \"paid or compelled\" to work on centralized projects of this sort, with dried anchovies possibly serving as a form of currency. [...] "
                "Although not edible, cotton was the most important product of irrigation in the Caral–Supe culture, vital to the production of fishing nets (that in turn provided maritime resources) as well as to textiles and textile technology. [...] "
                "There is no evidence of warfare \"of any kind or at any level during the Preceramic Period\". "
                "Mutilated bodies, burned buildings, and other tell-tale signs of violence are absent and settlement patterns are completely non-defensive. "
                "The evidence of the development of complex government in the absence of warfare contrasts markedly to archaeological theory, which suggests that human beings move away from kin-based groups to larger units resembling \"states\" for mutual defense of often scarce resources.",
                nome="Norte Chico civilization"),
        ],
    },
    # 6 Trepanação inca com sobrevivência melhor que na Guerra Civil americana
    {
        "temas_secundarios": ["historia_medicina", "anatomia"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "No Peru antigo, abrir buracos no crânio era cirurgia frequente. No tempo dos incas, de 75% a 83% dos operados sobreviviam, segundo um estudo de 2018. Na Guerra Civil americana, cerca de metade morria.",
        "explicacao": (
            "Mais de 800 crânios pré-históricos com marcas de trepanação, de um a sete buracos cada, já foram "
            "achados no litoral e nos Andes do Peru, os mais antigos de cerca de 400 a.C. São mais do que todos os "
            "crânios pré-históricos trepanados do resto do mundo somados. O neurologista David Kushner, da "
            "Universidade de Miami, e os antropólogos John Verano, de Tulane, e Anne Titelbaum compararam esse "
            "acervo com cirurgias de crânio de outras épocas. Para medir a sobrevivência, olharam a remodelação do "
            "osso em volta do buraco, sinal de cicatrização; sem ela, assumiram que o paciente morreu na cirurgia "
            "ou poucos dias depois. Entre 400 e 200 a.C., os resultados eram piores que na Guerra Civil americana, "
            "quando cerca de metade dos pacientes morria. Mas, de 1000 a 1400, a sobrevivência chegou a 91% em "
            "algumas amostras, e no período inca ficou em média entre 75% e 83%. Com o tempo, os cirurgiões "
            "andinos aprenderam quais técnicas eram mais seguras. Não se sabe o que usavam como anestesia. Segundo "
            "Verano, talvez folhas de coca, ou uma bebida fermentada, mas não há registros escritos."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": "https://news.miami.edu/stories/2018/06/holes-in-the-head.html",
             "titulo": "Holes in the head (University of Miami News, 2018)",
             "idioma": "en",
             "trecho": (
                 "By Maya Bell 06-08-2018 [...] "
                 "In their study published in the June issue of World Neurosurgery [...] "
                 "Kushner and his co-authors—biological anthropologists John W. Verano, a world authority on Peruvian trepanation at Tulane University, and his former graduate student, Anne R. Titelbaum [...] "
                 "Neither do we know what they used as anesthesia, but since there were so many (cranial surgeries) they must have used something—possibly coca leaves. "
                 "Maybe there was something else, maybe a fermented beverage. There are no written records, so we just don’t know. [...] "
                 "More than 800 prehistoric skulls with evidence of trepanation—at least one but as many as seven telltale holes—have been found in the coastal regions and the Andean highlands of Peru, the earliest dating back to about 400 B.C. "
                 "That’s more than the combined total number of prehistoric trepanned skulls found in the rest of the world. [...] "
                 "The researchers gauged survival by classifying the extent of bone remodeling around the trepanned holes, which indicates healing. "
                 "If there was no evidence of healing the researchers assumed th [...] "
                 "The long-term survival rates from such “shallow surgeries” in Peru during those early years, from about 400 to 200 B.C., proved to be worse than those in the Civil War, when about half the patients died. "
                 "But, from 1000 to 1400 A.D., survival rates improved dramatically, to as high as 91 percent in some samples, to an average of 75 to 83 percent during the Incan period, the study showed. "
                 "“Over time, from the earliest to the latest, they learned which techniques were better"
             )},
        ],
    },
    # 7 Vikings na América em 1021, datados por um pico de radiação cósmica
    {
        "temas_secundarios": ["navegacao_antiga", "historia_astronomia", "grandes_navegacoes"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "Os vikings cortaram árvores na Terra Nova, no Canadá, no ano de 1021, séculos antes de Colombo. A data exata saiu de uma marca deixada nos anéis das árvores por um pico de radiação cósmica no ano 993.",
        "explicacao": (
            "L'Anse aux Meadows, na ponta norte da ilha de Terra Nova, é o único sítio indiscutível de contato "
            "transoceânico de europeus com as Américas antes de Colombo, fora a Groenlândia. Faltava saber quando os "
            "nórdicos estiveram lá: as datas por radiocarbono iam de 990 a 1050. A pista veio do céu. No ano 993, "
            "um evento de radiação cósmica fez subir de repente a produção de carbono radioativo na atmosfera, e o salto ficou gravado, "
            "ao mesmo tempo, nos anéis de árvores do mundo todo. Os pesquisadores acharam esse salto em três peças de "
            "madeira do sítio, cortadas com ferramentas de metal, que os povos indígenas da região não fabricavam na "
            "época. Como as peças conservavam a borda logo abaixo da casca, deu para contar os anéis até o último e "
            "chegar ao ano exato em que as árvores foram derrubadas. As três, de árvores diferentes, deram o mesmo "
            "ano, 1021, coincidência que os autores do estudo, publicado na Nature em 2021, chamaram de notável e "
            "inesperada. É a única data segura de presença europeia do outro lado do Atlântico antes das viagens de "
            "Colombo. Para os autores, ela marca também o primeiro momento conhecido em que os seres humanos "
            "fecharam a volta ao globo."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": "https://www.nature.com/articles/s41586-021-03972-8",
             "titulo": "Evidence for European presence in the Americas in AD 1021 (Nature)",
             "idioma": "en",
             "trecho": (
                 "Published: 20 October 2021 [...] "
                 "Transatlantic exploration took place centuries before the crossing of Columbus. [...] "
                 "Here we provide evidence that the Vikings were present in Newfoundland in ad 1021. "
                 "We overcome the imprecision of previous age estimates by making use of the cosmic-ray-induced upsurge in atmospheric radiocarbon concentrations in ad 993 (ref. 6). "
                 "Our new date lays down a marker for European cognisance of the Americas, and represents the first known point at which humans encircled the globe. [...] "
                 "However, such time series have also revealed that production of the isotope rapidly increased in the years ad; 775 and ad 993 [...] "
                 "These sudden increases were caused by cosmic radiation events, and appear synchronously in dendrochronological records all around the world [...] "
                 "if the bark edge (or more specifically, the waney edge) is also present, it becomes possible to determine the exact felling year of the tree [...] "
                 "they had all been modified by metal tools, evident from their characteristically clean, low angle-in cuts30. "
                 "Such implements were not manufactured by the Indigenous inhabitants of the area at the time [...] "
                 "Our result of ad 1021 for the cutting year constitutes the only secure calendar date for the presence of Europeans across the Atlantic before the voyages of Columbus. "
                 "Moreover, the fact that our results, on three different trees, converge on the same year is notable and unexpected."
             )},
            wiki("L%27Anse_aux_Meadows",
                "With carbon dating estimates between 990 and 1050 CE (mean date 1014) and tree-ring dating of 1021, L'Anse aux Meadows is the only undisputed site of pre-Columbian trans-oceanic contact of Europeans with the Americas outside of Greenland.",
                nome="L'Anse aux Meadows"),
        ],
    },
    # 8 Chinchorro: as múmias artificiais mais antigas do mundo
    {
        "temas_secundarios": ["egito_antigo", "costumes_rituais", "microbiologia"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "As múmias feitas de propósito mais antigas do mundo não são egípcias: são do deserto do Atacama, no Chile, feitas pelo povo chinchorro desde cerca de 5050 a.C. E não só para a elite: crianças também.",
        "explicacao": (
            "Os chinchorros eram caçadores-coletores marinhos que viviam no litoral do norte do Chile e do sul do "
            "Peru. O Atacama, hiperárido e com solo rico em nitratos, já conservava corpos sozinho: o mais antigo "
            "conhecido desse povo, o Homem de Acha, morreu por volta de 7020 a.C. Por volta de 5050 a.C., eles "
            "passaram a mumificar os mortos de propósito, e o exemplo mais antigo é uma criança enterrada no vale "
            "de Camarones. Segundo a UNESCO, desmontavam e remontavam sistematicamente os corpos de homens, mulheres "
            "e crianças de toda a escala social. Os métodos incluíam reforçar os corpos e modelá-los com argila, e "
            "os arqueólogos reconhecem vários estilos, como as múmias negras, as vermelhas, as cobertas de barro e "
            "as enfaixadas. A prática durou cerca de 3.000 anos e acabou por volta de 1800 a.C. Hoje, as múmias "
            "enfrentam um inimigo vivo. No acervo da Universidade de Tarapacá, em Arica, a pele de algumas escureceu "
            "e começou a verter líquido. Pesquisadores acharam ali bactérias e fungos capazes de quebrar colágeno e "
            "queratina, e o estrago acelera muito com umidade relativa de 75% a 80%. Em 2021, os sítios chinchorro "
            "viraram Patrimônio Mundial da UNESCO."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Chinchorro_mummies",
                "The oldest known naturally preserved Chinchorro individual dates to about 7020 BCE, while deliberate mummification began by about 5050 BCE, making the Chinchorro mummies the oldest known examples of purposefully preserved human bodies in the world. "
                "The Chinchorro artificially preserved men, women and children from across their communities rather than restricting elaborate funerary treatment to a social elite. "
                "Their methods included reconstructing and reinforcing bodies, modelling them with clay [...] "
                "In 2021, settlements and cemeteries associated with the Chinchorro culture and its tradition of artificial mummification in Chile's Arica and Parinacota Region were designated a World Heritage Site by UNESCO. [...] "
                "known as Acha Man, died around 7020 BCE. His body was preserved by the hyper-arid conditions of the Atacama Desert. "
                "By about 5050 BCE, the Chinchorro had begun preserving their dead through artificial mummification. "
                "The earliest known example is a child buried in the Camarones Valley [...] "
                "Artificial mummification continued for about 3,000 years before ending around 1800 BCE. "
                "Archaeologists recognise several forms of Chinchorro mummification, including black, red, mud-coated and bandage mummies. [...] "
                "the previous decade among mummies held at the University of Tarapacá in Arica, northern Chile. "
                "Areas of preserved skin had darkened and begun to ooze. "
                "Researchers from Harvard University and the University of Tarapacá found bacteria and fungi on the damaged skin, including microorganisms capable of breaking down collagen and keratin, important proteins in human skin. "
                "Experiments showed that deterioration increased sharply at 75–80 percent relative humidity. [...] "
                "The soil is very rich in nitrates which, when combined with other factors such as the aridity of the Atacama Desert, ensure organic preservation.",
                nome="Chinchorro mummies"),
            {"url": "https://whc.unesco.org/en/list/1634/",
             "titulo": "Settlement and Artificial Mummification of the Chinchorro Culture in the Arica and Parinacota Region (UNESCO World Heritage)",
             "idioma": "en",
             "trecho": (
                 "they bear testimony to a culture of marine hunter-gatherers who resided in the arid and hostile northern coast of the Atacama Desert [...] "
                 "Over time, the Chinchorro perfected complex mortuary practices, whereby they systematically dismembered and reassembled bodies of deceased men, women and children of the entire social spectrum to create “artificial” mummies."
             )},
        ],
    },
    # 9 Chuño: batata liofilizada pelas noites geladas do Altiplano
    {
        "temas_secundarios": ["conservacao", "domesticacao", "ciencia_cozinha"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Nos Andes, batata é liofilizada sem máquina há séculos: congela nas noites do Altiplano, seca ao sol e é pisoteada pela família. Leve e durável, o chuño era comida de soldado inca em marcha.",
        "explicacao": (
            "O chuño é feito por comunidades quíchuas e aimarás da Bolívia e do Peru com uma variedade de batata "
            "amarga e resistente à geada. Em junho e julho, acima de 3.800 m de altitude, as noites chegam a uns "
            "−5 °C. As batatinhas são espalhadas bem juntas no chão, congelam à noite e perdem água de dia, por "
            "cerca de três noites: é uma liofilização natural. O congelamento rompe as paredes das células, o que "
            "facilita tirar a água que resta. Aí entra a família inteira, que faz montinhos de batata e \"dança\" em "
            "cima deles, espremendo a água e soltando as cascas. Lavado por cerca de uma semana e seco ao sol, vira "
            "o chuño branco; sem a lavagem, o chuño negro. A técnica é anterior ao Império Inca: há chuño em sítios "
            "arqueológicos de Tiwanaku, perto do lago Titicaca. Por ser portátil, durar muito e alimentar bem, era "
            "levado pelos soldados incas em marcha. Carl Troll chegou a defender que as noites abaixo de zero que "
            "permitem fazer chuño favoreceram a ascensão do império. A palavra vem do quíchua ch'uñu, \"batata "
            "congelada\"."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Chu%C3%B1o",
                "is a preserved potato product traditionally made by Quechua and Aymara communities of Bolivia and Peru [...] "
                "obtained by exposing a bitter, frost-resistant variety of potatoes to the very low night temperatures of the Andean Altiplano, freezing them, and subsequently exposing them to the intense sunlight of the day [...] "
                "The word comes from Quechua ch'uñu, meaning 'frozen potato' [...] "
                "The existence of chuño dates back to before the time of the Inca Empire in the 13th century, based on findings that have been made of the product at various archaeological sites. "
                "Specifically, they have been found at Tiwanaku [...] "
                "Due to its portability, long shelf life, and nutritional value, chuño was eaten by Inca soldiers on marches. "
                "Indeed Carl Troll argued that the nighttime sub-freezing temperatures of southern Peruvian highlands that allowed for chuño production favoured the rise of the Inca Empire. [...] "
                "Chuño is made at the beginning of winter during June and July, during which time the temperatures reach around −5 °C (23 °F) at elevations of over 3,800 metres (12,500 ft). [...] "
                "These small potatoes are spread closely on flat ground, and allowed to freeze with the low night temperatures and dehydrate in the daytime, for about three nights. "
                "This process results in natural freeze-drying. [...] "
                "During the process of manually squeezing water out of the potatoes via stepping on them, whole families will participate. "
                "The previous freeze-drying breaks down cell walls, making it easier to remove water from the potatoes. "
                "They build a small pile of potatoes with their feet and then \"dance\" on the pile, removing the skins as they do so. [...] "
                "This washing typically takes about a week. The final step is drying in the sun. [...] "
                "Black chuño is obtained directly from the original freezing, trampling, and refreezing process. "
                "The product is not washed or exposed to water again",
                nome="Chuño"),
            wiki("Waru_Waru",
                "is most commonly associated with the Tiwanaku culture of the Lake Titicaca region",
                nome="Waru Waru"),
        ],
    },
    # 10 Nazca: IA quase dobra o número de figuras conhecidas
    {
        "temas_secundarios": ["ia_robotica", "algoritmos"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Levou quase um século para achar 430 figuras desenhadas no deserto de Nazca, no Peru. Com a ajuda de inteligência artificial, uma equipe achou mais 303 em só seis meses de campo, quase dobrando a conta.",
        "explicacao": (
            "Além das famosas figuras gigantes, o deserto de Nazca guarda geoglifos menores, em relevo, muito "
            "difíceis de enxergar. Pesquisadores do Instituto Nazca da Universidade de Yamagata, no Japão, com a IBM "
            "Research, usaram um sistema de inteligência artificial para varrer imagens de toda a região e apontar "
            "candidatos. Só a triagem das fotos indicadas pela IA tomou 1.200 horas de trabalho, e a checagem a pé, "
            "entre setembro de 2022 e fevereiro de 2023, mais 1.440 horas. O resultado, publicado em 2024, foram 303 "
            "figuras novas confirmadas, entre elas papagaios, gatos, macacos, orcas e cabeças decepadas. Com o "
            "acervo maior, deu para comparar os dois tipos. As figuras gigantes de linha retratam sobretudo animais "
            "selvagens (64%) e ficam, em média, a 34 m da rede de linhas e trapézios usada em cerimônias. Já 81,6% "
            "das figuras em relevo mostram humanos ou coisas modificadas por humanos, como camelídeos domesticados e "
            "cabeças decepadas, e ficam em média a 43 m de antigas trilhas que cruzam o deserto. Para os autores, as "
            "grandes provavelmente serviam a rituais da comunidade, e as pequenas eram feitas e vistas por "
            "indivíduos ou pequenos grupos de passagem."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11459208/fullTextXML",
             "titulo": "AI-accelerated Nazca survey nearly doubles the number of known figurative geoglyphs and sheds light on their purpose (PNAS, 2024)",
             "idioma": "en",
             "trecho": (
                 "It took nearly a century to discover a total of 430 figurative Nazca geoglyphs, which offer significant insights into the ancient cultures at the Nazca Pampa. "
                 "Here, we report the deployment of an AI system to the entire Nazca region, a UNESCO World Heritage site, leading to the discovery of 303 new figurative geoglyphs within only 6 mo of field survey, nearly doubling the number of known figurative geoglyphs. "
                 "Even with limited training examples, the developed AI approach is demonstrated to be effective in detecting the smaller relief-type geoglyphs, which unlike the giant line-type geoglyphs are very difficult to discern. [...] "
                 "We find that relief-type geoglyphs depict mainly human motifs or motifs of things modified by humans, such as domesticated animals and decapitated heads (81.6%). "
                 "They are typically located within viewing distance (on average 43 m) of ancient trails that crisscross the Nazca Pampa and were most likely built and viewed at the individual or small-group level. "
                 "On the other hand, the giant line-type figurative geoglyphs mainly depict wild animals (64%). "
                 "They are found an average of 34 m from the elaborate linear/trapezoidal network of geoglyphs, which suggests that they were probably built and used on a community level for ritual activities."
             )},
            wiki("Nazca_Lines",
                "In 2024, a team of archaeologists from the Yamagata University's Nazca Institute, in collaboration with IBM Research, used artificial intelligence (AI) to discover 303 previously unknown geoglyphs depicting parrots, cats, monkeys, killer whales, and even severed heads near the Nazca Lines in Peru. "
                "The field survey took place between September 2022 and February 2023 and was conducted on foot for ground truthing [...] "
                "It required 1,440 labor hours and resulted in 303 newly confirmed figurative geoglyphs. [...] "
                "A total of 1,200 labor hours were spent screening the AI-model geoglyph candidate photos.",
                nome="Nazca Lines"),
        ],
    },
    # 11 Azul maia: anil + argila, uma cor que resiste a ácido
    {
        "temas_secundarios": ["pigmentos", "quimica_cotidiano", "minerais_rochas"],
        "tipos_espanto": ["engenhosidade", "misterio_aberto"],
        "gancho": "Murais pintados há mais de mil anos no México mantêm um azul vivo num dos climas mais duros do mundo. O segredo do azul maia é juntar anil com uma argila, o que o torna resistente até a ácido nítrico.",
        "explicacao": (
            "O azul maia, um turquesa intenso, foi fabricado por povos da Mesoamérica, como maias e astecas. Aparece "
            "por volta do ano 800 e foi usado em murais, cerâmicas, esculturas e códices. Murais de Chichén Itzá, "
            "Bonampak e Cacaxtla conservam a cor há mais de mil anos. O pigmento junta duas partes: o corante "
            "índigo, tirado das folhas do anil, e a paligorsquita, uma argila natural. A combinação é extremamente "
            "estável: resiste a solventes, ácidos, álcalis e à biodegradação, e só se desfaz com um tratamento ácido "
            "muito intenso. A composição só foi descoberta nos anos 1950, por difração em pó. Depois da conquista, o "
            "azul ainda foi usado no século XVI em conventos do México colonial, mas a técnica se perdeu. Uma receita "
            "para reproduzi-lo só foi publicada em 1993, pelo historiador e químico mexicano Constantino "
            "Reyes-Valerio, que juntou a leitura de crônicas antigas com análises microscópicas e espectroscopia das "
            "pinturas. Hoje o pigmento inspira químicos a criar cores novas, como o \"violeta maia\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Maya_blue",
                "is a unique bright turquoise or azure blue pigment manufactured by cultures of pre-Columbian Mesoamerica, such as the Mayas and Aztecs [...] "
                "It is found in mural paintings on architectural buildings, ceramic pieces, sculptures, codices [...] "
                "Murals painted more than 1,000 years ago in Chichén Itzá, Bonampak and Cacaxtla, in what is today Mexico, have maintained their color, despite existing in one of the world's harshest climates. [...] "
                "primarily indigo dyes derived from the leaves of anil (Indigofera suffruticosa, called ch'oj in Mayan) plants combined with palygorskite, a natural clay [...] "
                "Maya blue first appeared around 800, and it was still used in the 16th century in several Convents of Colonial Mexico [...] "
                "After that, the techniques for its production were lost in Mexico [...] "
                "The color has resisted chemical solvents and acids such as nitric acid. "
                "Its resistance against chemical aggression (acids, alkalis, solvents, etc.) and biodegradation was tested, and it was shown that Maya blue is an extremely resistant pigment, but it can be destroyed using very intense acid treatment under reflux. "
                "Because of its exceptionally durable colour properties, Maya Blue is an iconic system that led to paleo-inspired chemistry, i.e. the recreation of new pigments such as Maya Violet [...] "
                "The chemical composition of the compound was determined by powder diffraction in the 1950s [...] "
                "An actual recipe to reproduce Maya blue pigment was published in 1993 by a Mexican historian and chemist, Constantino Reyes-Valerio. [...] "
                "through a thorough revision of primary texts (Sahagún, Hernandez, Jimenez, and others), microscopic analysis of the mural paintings and fourier transform infrared spectroscopy.",
                nome="Maya blue"),
        ],
    },
    # 12 Q'eswachaka: a última ponte de corda inca, refeita todo ano
    {
        "temas_secundarios": ["grandes_obras", "costumes_rituais", "povos_indigenas"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "No Peru, uma ponte de capim trançado sobre o rio Apurímac é refeita todo ano por quatro comunidades quíchuas, com técnicas incas. É a última ponte de corda inca que resta.",
        "explicacao": (
            "A Q'eswachaka é uma ponte suspensa sobre um desfiladeiro do rio Apurímac, no sul dos Andes. A "
            "renovação dura só três dias, na segunda semana de junho, mas organiza o ano inteiro das comunidades de "
            "Huinchiri, Chaupibanda, Choccayhua e Ccollana Quehue. Primeiro, as famílias cortam e torcem capim para "
            "fazer cordas finas de uns 70 m. Dois mestres construtores guiam a torção dessas cordas em cordas "
            "médias, que depois são trançadas em seis cabos grossos. Os homens amarram os cabos a bases de pedra "
            "antigas, e os artesãos tecem a ponte, cada um partindo de uma margem. No tempo dos incas, o trabalho "
            "teria sido uma forma de imposto, a mit'a. Hoje existe uma ponte moderna ali perto, mas os construtores "
            "dizem que mantêm a tradição para honrar os antepassados e a Pachamama, a Mãe Terra. Em 2013, a UNESCO "
            "pôs os saberes e rituais da renovação na lista do patrimônio cultural imaterial da humanidade. Sem "
            "manutenção na pandemia de covid-19, a ponte desabou em março de 2021 e foi reconstruída nas semanas "
            "seguintes."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://ich.unesco.org/en/RL/knowledge-skills-and-rituals-related-to-the-annual-renewal-of-the-qeswachaka-bridge-00594",
             "titulo": "Knowledge, skills and rituals related to the annual renewal of the Q’eswachaka bridge (UNESCO)",
             "idioma": "en",
             "trecho": (
                 "Inscribed in 2013 (8.COM) on the Representative List of the Intangible Cultural Heritage of Humanity [...] "
                 "The Q’eswachaka bridge is a rope suspension bridge over a gorge of the Apurimac River in the southern Andes. "
                 "It is renewed every year, using traditional Inca techniques and raw materials. "
                 "The Quechua-speaking peasant communities of Huinchiri, Chaupibanda, Choccayhua and Ccollana Quehue [...] "
                 "Although the renewal lasts only three days, it structures the life of the participating communities all year round [...] "
                 "The process begins with families cutting and twisting straw to form thin ropes about 70 m long. "
                 "Two bridge-builders then guide the process of twisting them together to form medium-sized ropes, which are then braided to form six great ropes. "
                 "When these are ready, men from the community tie the ropes tightly to ancient stone bases. "
                 "The craftspeople then lead the weaving of the bridge, each starting from opposite ends."
             )},
            wiki("Q%27eswachaka",
                "is the last remaining Inca rope bridge, consisting of grass ropes that span the Apurímac River [...] "
                "Even though there is a modern bridge nearby, the residents of the region keep the ancient tradition and skills alive by renewing the bridge annually, during the second week of June. [...] "
                "In ancient times the effort would have been a form of tax (Mit'a), with participants expected to perform the rebuilding; nowadays the builders have indicated that the effort is performed to honor their ancestors and the Pachamama (Earth Mother). [...] "
                "Due to a lack of maintenance during the COVID-19 pandemic in 2020 and early 2021, the bridge collapsed in March 2021. "
                "In the following weeks the bridge was rebuilt.",
                nome="Q'eswachaka"),
        ],
    },
    # 13 Teotihuacan: nome dado pelos astecas e um poder sem rosto
    {
        "temas_secundarios": ["cidades", "nomes_lugares"],
        "tipos_espanto": ["misterio_aberto", "origem_inesperada"],
        "gancho": "Teotihuacan, a maior cidade das Américas no seu auge, foi batizada pelos astecas séculos depois de cair, como \"lugar onde nasceram os deuses\". Seu nome original é desconhecido, e quem a governava também.",
        "explicacao": (
            "Teotihuacan fica a 40 km da Cidade do México e é famosa pelas pirâmides do Sol e da Lua. Apesar da "
            "proximidade, não era asteca: é séculos mais antiga que o império deles. No auge, talvez na primeira "
            "metade do primeiro milênio, foi a maior cidade das Américas, provavelmente com cerca de 100.000 "
            "moradores, e tudo indica que reunia vários povos. Por volta de 550, seus monumentos foram saqueados e "
            "queimados. Os astecas, falantes de náuatle, deram ao lugar o nome Teōtīhuacān, traduzido como "
            "\"lugar onde nasceram os deuses\", porque acreditavam que os deuses tinham criado o universo ali. O "
            "nome original é desconhecido; em textos hieroglíficos maias, a cidade aparece como puh, \"lugar dos "
            "juncos\". O poder também intriga. Cidades maias e zapotecas da época, e antes delas os olmecas, "
            "deixaram palácios reais e cenas de guerra, conquista e cativos humilhados, marcas de dinastias "
            "autoritárias. Em Teotihuacan, nada disso foi achado, e muitos estudiosos concluem que ela tinha alguma "
            "forma de governo coletivo. Mesmo assim, sua influência ia longe: em 378, um chefe guerreiro retratado "
            "com símbolos de Teotihuacan conquistou Tikal, a 1.000 km dali, e trocou o rei maia."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Teotihuacan",
                "is located in the State of Mexico, 40 kilometers (25 mi) northeast of modern-day Mexico City. "
                "Teotihuacan is known today as the site of many of the most architecturally significant Mesoamerican pyramids built in the pre-Columbian Americas, namely the Pyramid of the Sun and the Pyramid of the Moon. "
                "Although close to Mexico City, Teotihuacan was not a Mexica (i.e. Aztec) city, and it predates the Aztec Empire by many centuries. "
                "At its zenith, perhaps in the first half of the first millennium (1 CE to 500 CE), Teotihuacan was the largest city in the Americas. "
                "Its population has been estimated to be at least 25,000, but likely sat around 100,000 during its height [...] "
                "Its major monuments were sacked and systematically burned around 550 CE. [...] "
                "The name Teōtīhuacān was given by the Nahuatl-speaking Aztecs centuries after the fall of the city around 550 CE. "
                "The term has been glossed as \"birthplace of the gods\", or \"place where gods were born\" [...] "
                "This is because the Aztecs believed that the gods created the universe at that site. [...] "
                "The original name of the city is unknown, but it appears in hieroglyphic texts from the Maya region as puh, or \"Place of Reeds\". [...] "
                "Contemporaneous cities in the same region, including Mayan and Zapotec, as well as the earlier Olmec civilization, left ample attestations of dynastic authoritarian sovereignty in the form of royal palaces, ceremonial ball courts, and depictions of war, conquest, and humiliated captives. "
                "However, no such artifacts have been found in Teotihuacan. "
                "Many scholars have thus concluded that Teotihuacan was led by some sort of \"collective governance.\" "
                "In January 378, the warlord Sihyaj K'ahk' [...] depicted with artifacts and the feather-serpent imagery associated with Teotihuacan culture, conquered Tikal, 1,000 kilometres (600 mi) away from Teotihuacan, removing and replacing the Maya king [...] "
                "Archeological evidence suggests that Teotihuacan was a multi-ethnic city",
                nome="Teotihuacan"),
        ],
    },
    # 14 Os astecas não se chamavam astecas
    {
        "temas_secundarios": ["nomes_lugares", "palavras_viajantes"],
        "tipos_espanto": ["origem_inesperada", "mito_desmentido"],
        "gancho": "Os astecas não se chamavam de astecas: eram os mexicas. Num relato da migração deles, o próprio deus Huitzilopochtli avisa que o nome do povo não é mais Azteca. O uso moderno do termo vem de Humboldt, em 1810.",
        "explicacao": (
            "Em náuatle, aztēcatl quer dizer \"gente de Aztlán\", um lugar de origem mítico reivindicado por vários "
            "povos do centro do México. A palavra aparece nos relatos de migração dos mexicas para descrever as "
            "tribos que saíram juntas de Aztlán, mas não era o nome que eles usavam para si. Num desses relatos, "
            "Huitzilopochtli, o deus protetor dos mexicas, diz aos seguidores, no meio da jornada, que eles já não se "
            "chamam Azteca, e sim Mexitin, ou seja, mexicas. Os moradores de Tenochtitlan, cidade numa ilha do lago "
            "Texcoco, onde hoje fica a Cidade do México, chamavam a si mesmos de Mēxihcah. Foi o cientista alemão "
            "Alexander von Humboldt quem, em 1810, deu origem ao uso moderno de \"asteca\" como nome coletivo para "
            "todos os povos ligados ao Estado mexica e à Tríplice Aliança por comércio, costumes, religião e língua. "
            "Essa aliança, que chamamos de Império Asteca, era uma confederação de três cidades-Estado formada em "
            "1427: Tenochtitlan, Texcoco e Tlacopan. Hoje o termo \"asteca\" ora se refere só aos mexicas de "
            "Tenochtitlan, ora a vários povos de língua náuatle do centro do México."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Aztecs",
                "The Aztec Empire was a confederation of three city-states established in 1427: Tenochtitlan (the capital of Mexica), Tetzcoco, and Tlacopan. "
                "Although the term Aztecs is often narrowly restricted to the Mexica of Tenochtitlan, it is also broadly used to refer to Nahua polities or peoples of central Mexico in the pre-Hispanic era [...] "
                "mean \"people from Aztlán\", a mythical place of origin for several ethnic groups in central Mexico. "
                "The term was not used as an endonym by the Aztecs themselves, but it is found in the different migration accounts of the Mexica, where it describes the different tribes who left Aztlan together. "
                "In one account of the journey from Aztlan, Huitzilopochtli, the tutelary deity of the Mexica tribe, tells his followers on the journey that \"now, no longer is your name Azteca, you are now Mexitin [Mexica]\". "
                "In today's usage, the term \"Aztec\" often refers exclusively to the Mexica people of Tenochtitlan (now the location of Mexico City), situated on an island in Lake Texcoco, who referred to themselves as Mēxihcah [...] "
                "Alexander von Humboldt originated the modern usage of \"Aztec\" in 1810, as a collective term applied to all the people linked by trade, custom, religion, and language to the Mexica state and the Triple Alliance. [...] "
                "German scientist Alexander von Humboldt",
                nome="Aztecs"),
        ],
    },
    # 15 Chinampas: os "jardins flutuantes" que não flutuavam
    {
        "temas_secundarios": ["domesticacao", "agua_doce_gelo", "biomimetica"],
        "tipos_espanto": ["engenhosidade", "mito_desmentido"],
        "gancho": "Os \"jardins flutuantes\" dos astecas não flutuavam: eram ilhas artificiais erguidas no fundo raso do lago, cercadas por varas e juncos. Com água ao redor o ano todo, davam até sete colheitas por ano.",
        "explicacao": (
            "As chinampas eram canteiros retangulares construídos em lagos e pântanos de água doce do vale do "
            "México. Os agricultores fincavam estacas no leito raso e cercavam o retângulo com um trançado de varas; "
            "lá dentro, o acúmulo de terra e de plantas aquáticas formava a ilha. Canais largos o bastante para uma "
            "canoa separavam um canteiro do outro. Com água por perto o tempo todo, as plantas não dependiam da "
            "chuva, e a produtividade era altíssima: até sete colheitas por ano. Os astecas não inventaram a "
            "técnica, mas foram os primeiros a usá-la em grande escala, e as chinampas cercavam Tenochtitlan, a "
            "capital. Ali, os canteiros mediam de 90 m × 5 m a 90 m × 10 m. A ideia tem parentes nos Andes: perto do "
            "lago Titicaca, os waru waru alternavam canteiros elevados e canais, e a terra elevada protegia as "
            "plantações da geada noturna. As chinampas que restam, como as de Xochimilco, receberam da ONU em 2018 o "
            "título de patrimônio agrícola mundial. Mas sofrem com a expansão urbana, a falta de água e a poluição "
            "por esgoto não tratado."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Chinampa",
                "They are built up on wetlands of a lake or freshwater swamp for agricultural purposes [...] "
                "This method was also used and occupied most of Lake Xochimilco. "
                "The United Nations designated it a Globally Important Agricultural Heritage System in 2018. [...] "
                "The Aztecs did not invent the chinampa technology but rather were the first to develop it to a large-scale cultivation. "
                "Sometimes called \"floating gardens,\" chinampas did not float but are artificial islands that were created by interweaving reeds with stakes beneath the lake's surface, creating underwater fences. [...] "
                "making crops grown there independent of rainfall. "
                "Chinampas were separated by channels wide enough for a canoe to pass. "
                "These raised, well-watered beds had very high crop yields with up to 7 harvests a year. [...] "
                "In Tenochtitlan, the chinampas ranged from 90 m × 5 m (300 ft × 20 ft) to 90 m × 10 m (300 ft × 30 ft) "
                "They were created by staking out the shallow lake bed and then fencing in the rectangle with wattle. [...] "
                "Chinampa farms also ringed Tenochtitlan, the Aztec capital [...] "
                "Other challenges include limited water supply, the use of pesticides, climate change, urban sprawl, and water pollution caused by untreated sewage and toxic waste.",
                nome="Chinampa"),
            wiki("Waru_Waru",
                "This type of altiplano field agriculture consists of parallel canals alternated by raised planting beds [...] "
                "By trapping solar radiation during the day, this raised field agricultural method also protected crops from freezing overnight. [...] "
                "is most commonly associated with the Tiwanaku culture of the Lake Titicaca region",
                nome="Waru Waru"),
        ],
    },
]
