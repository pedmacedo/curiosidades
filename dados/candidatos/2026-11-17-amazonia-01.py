LOTE = "2026-11-17-amazonia-01"
AREA = "brasil"
TEMA = "amazonia"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = W if idioma == "en" else "https://pt.wikipedia.org/wiki/"
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


NASA = "https://www.nasa.gov/content/goddard/nasa-satellite-reveals-how-much-saharan-dust-feeds-amazon-s-plants"

CANDIDATOS = [
    # 1
    {
        "temas_secundarios": ["paisagens_extremas", "atmosfera", "plantas"],
        "tipos_espanto": ["conexao_inesperada", "escala_absurda"],
        "gancho": "A floresta amazônica é adubada pelo Saara: todo ano caem sobre ela milhões de toneladas de poeira africana carregada de fósforo.",
        "explicacao": (
            "Os solos da Amazônia são pobres em nutrientes. Quase tudo o que a floresta precisa fica guardado nas "
            "próprias plantas: folhas e matéria orgânica caídas se decompõem e são rapidamente reabsorvidas pelas "
            "raízes. Mas parte de alguns nutrientes, como o fósforo, é levada pela chuva para córregos e rios. A "
            "reposição vem de longe. Com dados do satélite CALIPSO, da NASA, que usa pulsos de laser para medir "
            "partículas na atmosfera, pesquisadores calcularam que os ventos tiram do Saara, em média, 182 milhões "
            "de toneladas de poeira por ano, e que cerca de 27,7 milhões de toneladas caem sobre a bacia amazônica. "
            "Uma fonte importante é a depressão de Bodélé, no Chade, um antigo leito de lago cujos minerais, "
            "formados por micro-organismos mortos, são ricos em fósforo. A poeira entrega cerca de 22 mil toneladas "
            "de fósforo por ano, mais ou menos o que a Amazônia perde com a chuva e as enchentes."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [{"url": NASA, "titulo": "NASA Satellite Reveals How Much Saharan Dust Feeds Amazon's Plants", "idioma": "en",
                    "trecho": "Specifically the dust picked up from the Bodélé Depression in Chad, an ancient lake bed where rock minerals composed of dead microorganisms are loaded with phosphorus. [...] "
                              "Instead they are locked up in the plants themselves. Fallen, decomposing leaves and organic matter provide the majority of nutrients, which are rapidly absorbed by plants and trees after entering the soil. "
                              "But some nutrients, including phosphorus, are washed away by rainfall into streams and rivers [...] "
                              "The phosphorus that reaches Amazon soils from Saharan dust, an estimated 22,000 tons per year, is about the same amount as that lost from rain and flooding [...] "
                              "The data show that wind and weather pick up on average 182 million tons of dust each year [...] "
                              "27.7 million tons – enough to fill 104,908 semi trucks – fall to the surface over the Amazon basin."}],
    },
    # 2
    {
        "temas_secundarios": ["vulcoes_terremotos", "agua_doce_gelo"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Por milhões de anos o rio Amazonas correu ao contrário, de leste para oeste, até a subida dos Andes inverter seu caminho rumo ao Atlântico.",
        "explicacao": (
            "Hoje o Amazonas tem suas nascentes mais remotas no altiplano andino, a pouca distância do oceano "
            "Pacífico, e atravessa o continente inteiro até desaguar no Atlântico. Estudos geológicos indicam que, "
            "por milhões de anos, o sentido foi o oposto: o rio corria de leste para oeste. A mudança veio com a "
            "formação da cordilheira dos Andes. À medida que as montanhas se ergueram, bloquearam a saída da água "
            "para o Pacífico, e o rio acabou trocando de direção até chegar à foz atual, no Atlântico. É por isso "
            "que o maior rio da América do Sul nasce tão perto de um oceano e vai desaguar no outro, depois de "
            "cruzar quase todo o continente."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Amazon_River",
            "Geological studies suggest that for millions of years, the Amazon River flowed in the opposite direction – from east to west. "
            "Eventually the Andes Mountains formed, blocking its flow to the Pacific Ocean and causing it to switch directions to its current mouth in the Atlantic Ocean. [...] "
            "Its most remote sources are found on the inter-Andean plateau, just a short distance from the Pacific Ocean.")],
    },
    # 3
    {
        "temas_secundarios": ["grandes_obras"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Nenhuma ponte cruza o rio Amazonas de margem a margem. O motivo não é a largura, mas a falta de estradas e cidades dos dois lados.",
        "explicacao": (
            "Seria natural imaginar que o Amazonas é largo demais para uma ponte. Não é isso: em boa parte do "
            "percurso, engenheiros conseguiriam construir uma travessia sem grande dificuldade. O que falta é "
            "motivo. O rio atravessa a floresta amazônica, onde há pouquíssimas estradas e cidades, e na maior parte "
            "do tempo a travessia é feita de balsa. A ponte que liga Manaus a Iranduba, a mais famosa da região, "
            "não cruza o Amazonas: ela atravessa o rio Negro, um afluente, pouco antes do encontro dos dois. Há "
            "ainda outro detalhe que complica qualquer obra: todo ano o rio sobe mais de 9 metros e inunda as "
            "florestas ao redor, as chamadas matas de várzea."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Amazon_River",
            "Every year, the river rises more than 9 m (30 ft), flooding the surrounding forests, known as várzea (\"flooded forests\"). [...] "
            "There are no bridges across the entire width of the river. This is not because the river would be too wide to bridge; "
            "for most of its length, engineers could build a bridge across the river easily. For most of its course, the river flows through the Amazon Rainforest, "
            "where there are very few roads and cities. Most of the time, the crossing can be done by a ferry. "
            "The Manaus Iranduba Bridge linking the cities of Manaus and Iranduba spans the Rio Negro, the second-largest tributary of the Amazon, just before their confluence.")],
    },
    # 4
    {
        "temas_secundarios": ["americas_pre_colombianas", "povos_indigenas", "domesticacao"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Em meio aos solos pobres da Amazônia existem manchas de terra preta muito fértil, criadas ou melhoradas por povos indígenas há mais de mil anos.",
        "explicacao": (
            "O solo amazônico típico tem baixa fertilidade. Por isso chamam a atenção, em vários pontos da bacia, "
            "manchas de um solo muito escuro e fértil, conhecido como terra preta de índio. Ele foi produzido por "
            "comunidades agrícolas pré-colombianas entre cerca de 450 a.C. e 950 d.C., com a mistura de carvão, "
            "ossos, cacos de cerâmica, composto e esterco à terra original. O carvão é o segredo: é estável, fica "
            "no solo por milhares de anos e ajuda a reter nutrientes e micro-organismos, resistindo à lavagem pela "
            "chuva. A cor preta vem justamente desse carvão envelhecido. Há debate sobre o ponto de partida: "
            "pesquisas recentes sugerem que parte dessas manchas já era naturalmente mais fértil, e que os povos "
            "antigos as aproveitaram e melhoraram de propósito."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Terra_preta",
            "Terra preta owes its characteristic black color to its weathered charcoal content, and was made by adding a mixture of charcoal, bones, broken pottery, compost and manure to the low fertility Amazonian soil. "
            "A product of indigenous Amazonian soil management and slash-and-char agriculture, the charcoal is stable and remains in the soil for thousands of years [...] "
            "The combination accumulates nutrients, minerals and microorganisms and withstands leaching. "
            "Terra preta soils were created by the pre-Columbian farming communities between 450 BCE and 950 CE. [...] "
            "Recent research has reported that terra preta may be of natural origin, suggesting that pre-Columbian people intentionally utilized and improved existing areas of soil fertility")],
    },
    # 5
    {
        "temas_secundarios": ["geologia_profunda", "agua_doce_gelo"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "O famoso 'rio subterrâneo' sob o Amazonas não é bem um rio: seria um aquífero a quase 4 km de profundidade, cuja água anda mais devagar que uma geleira.",
        "explicacao": (
            "Em 2011, pesquisadores anunciaram indícios de um fluxo de água subterrânea sob a bacia amazônica, a "
            "quase 4 quilômetros de profundidade, seguindo de oeste para leste o caminho aproximado do Amazonas. A "
            "notícia correu como a descoberta de um 'rio subterrâneo' de cerca de 6 mil quilômetros, apelidado de "
            "rio Hamza em homenagem ao geofísico Valiya Hamza, do Observatório Nacional. A imagem de um rio "
            "correndo debaixo da terra, porém, está errada. O que os dados sugerem é um aquífero de água salgada "
            "que se move com uma lentidão maior que a de uma geleira. O próprio Hamza explicou que a equipe usou a "
            "palavra 'rio' em sentido amplo, e no título do trabalho original ela aparece entre aspas. O fluxo foi "
            "deduzido de forma indireta, combinando dados sísmicos com temperaturas medidas em 241 poços de "
            "petróleo desativados."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Hamza_River",
            "The Hamza River (Portuguese: Rio Hamza) is an unofficial name for what appears to be a slowly flowing aquifer in Brazil and Peru, approximately 6,000 kilometres (3,700 mi) long at a depth of nearly 4 kilometres (2.5 mi). "
            "Its discovery was announced in 2011 [...] Valiya Mannathal Hamza, of Brazil's National Observatory [...] "
            "Its own water has a high salt content. [...] "
            "A combination of seismic data and anomalous temperature variation with depth measured in 241 inactive oil wells helped locate the aquifer. [...] "
            "The speed of flow is slower than that of an average glacier, and Hamza himself says that the team uses the term \"river\" in a general sense, not in the conventional sense. "
            "In the title to the original paper, the word \"river\" appears in quotation marks.")],
    },
    # 6
    {
        "temas_secundarios": ["personagens_esquecidos", "revolucao_industrial"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Henry Ford ergueu uma cidade americana na Amazônia para produzir borracha, com regras que proibiam até bebida em casa. Nunca a visitou, e o projeto fracassou.",
        "explicacao": (
            "Em 1928, Henry Ford fundou na floresta amazônica, no Pará, uma cidade pré-fabricada planejada para 10 "
            "mil moradores. O objetivo era garantir uma fonte própria de borracha para a fábrica de automóveis nos "
            "Estados Unidos. Fordlândia ganhou até piscina, campo de golfe, quadras de tênis e cinema. Também tinha "
            "regras rígidas: álcool, tabaco e prostituição eram proibidos, inclusive dentro das casas dos "
            "trabalhadores, e gerentes americanos iam de casa em casa para fiscalizar. Os trabalhadores driblavam a "
            "proibição remando até barcos de comerciantes ancorados fora dos limites da cidade. O problema maior foi "
            "agrícola: as seringueiras foram plantadas bem juntas, presa fácil de doenças e pragas. A empresa "
            "abandonou Fordlândia em 1934 e, apesar do investimento e dos convites, Henry Ford nunca a visitou."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Fordl%C3%A2ndia",
            "It was established by American industrialist Henry Ford in the Amazon rainforest in 1928 as a prefabricated industrial town intended to be inhabited by 10,000 people "
            "to secure a source of cultivated rubber for the automobile manufacturing operations of the Ford Motor Company in the United States. [...] "
            "a swimming pool, golf course, tennis courts, and a movie theater were also constructed. [...] "
            "Alcohol, tobacco and prostitution were forbidden within the town, including inside the workers' own homes. American managers would go from house to house to enforce these rules. "
            "Workers circumvented these prohibitions by paddling out to merchant riverboats moored beyond the town jurisdiction [...] "
            "In Fordlândia, however, the trees were planted close together in plantations, easy prey for tree blight [...] "
            "Fordlândia was abandoned by the Ford Motor Company in 1934 [...] "
            "In spite of the huge investment and numerous invitations, Henry Ford never visited either of his ill-fated towns.",
            "Fordlândia")],
    },
    # 7
    {
        "temas_secundarios": ["imperios_coloniais", "plantas"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "O Brasil perdeu o monopólio da borracha por causa de 70 mil sementes de seringueira levadas por um inglês em 1876 e plantadas em colônias britânicas.",
        "explicacao": (
            "No século XIX, a Amazônia viveu o ciclo da borracha, quando a extração do látex das seringueiras "
            "nativas abastecia a indústria mundial. Em 1876, o inglês Henry Wickham comandou uma operação que tirou "
            "do Brasil, às escondidas, 70 mil sementes de seringueira. Das sementes saíram as árvores que o governo "
            "britânico plantou em suas colônias na Malásia, no Sri Lanka e na África tropical. Essas plantações "
            "conseguiam produzir látex com mais eficiência do que a coleta espalhada pela floresta. A borracha "
            "asiática acabou sendo a principal causa da perda do monopólio brasileiro, e a ferrovia "
            "Madeira-Mamoré, terminada em 1912 para escoar a borracha amazônica, ficou pronta tarde demais."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [{"url": W + "Amazon_rubber_cycle", "titulo": "Amazon rubber cycle", "idioma": "en",
                    "trecho": "Henry Wickham, who in 1876 directed an operation smuggling 70,000 rubber tree seeds [...] "
                              "was the principal cause of the loss of the Brazilian monopoly The Madeira–Mamoré Railroad, finished in 1912, arrived too late. [...] "
                              "as the British government had planted rubber trees in its colonies in Malaysia, Sri Lanka, and tropical Africa. "
                              "These rubber trees were planted from seeds that Henry Wickham had smuggled out of Brazil in 1876. [...] "
                              "These plantations were able to produce latex with greater efficiency"}],
    },
    # 8
    {
        "temas_secundarios": ["eletromagnetismo", "animais_extremos"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Um poraquê amazônico só reconhecido como espécie própria em 2019 dá descargas de até 860 volts, o maior gerador de eletricidade conhecido da natureza.",
        "explicacao": (
            "Por muito tempo se pensou que o poraquê, o peixe elétrico da Amazônia, fosse uma única espécie, "
            "Electrophorus electricus. Em 2019, uma análise mostrou que havia mais de uma: as populações eram "
            "geneticamente bem distintas e produziam voltagens diferentes. Uma das espécies separadas recebeu o "
            "nome de Electrophorus voltai, em homenagem ao físico Alessandro Volta, considerado o criador da pilha "
            "elétrica. A homenagem é justa: ela produz descargas de até 860 volts, o maior valor conhecido para a "
            "geração de eletricidade por um ser vivo. Essa espécie vive sobretudo em rios de terras altas do "
            "Escudo Brasileiro que correm para o norte. O caso mostra que até um animal famoso e de grande porte "
            "pode esconder espécies que ninguém tinha separado."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Electrophorus_voltai",
            "It is the strongest known bioelectricity generator in nature, producing up to 860 volts. [...] "
            "It was previously classified within Electrophorus electricus when that species was considered the only one in the genus Electrophorus, "
            "but a 2019 analysis described it and E. varii as distinct species based on both their deep genetic divergences and differences in the voltage produced by each species. [...] "
            "It is named in honor of the physicist Alessandro Volta, who is widely credited as the creator of the electric battery. [...] "
            "It inhabits upland habitats, primarily north-flowing rivers of the Brazilian Shield",
            "Electrophorus voltai")],
    },
    # 9
    {
        "temas_secundarios": ["vida_marinha", "oceanografia"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Na foz do Amazonas, sob a água barrenta onde se achava impossível haver recifes, existe um recife de mais de mil quilômetros, revelado em 2016.",
        "explicacao": (
            "Recifes costumam prosperar em águas limpas de plataformas tropicais. Por isso se acreditava que a foz "
            "do Amazonas, com sua pluma de água carregada de sedimentos, fosse uma lacuna natural na distribuição de "
            "recifes no Atlântico ocidental. Em abril de 2016 foi publicada a descoberta de um sistema de recifes ali "
            "mesmo, com mais de mil quilômetros de extensão e mais de 9.300 quilômetros quadrados de área. O segredo "
            "é a profundidade: o recife fica abaixo da camada de água doce que o rio despeja sobre o oceano. A maior "
            "parte dele não é coral, e sim rodolitos, formações de algas vermelhas que lembram corais. Nas áreas "
            "do norte, mais cobertas pela pluma, predominam esponjas e animais carnívoros como hidroides. "
            "Organismos unicelulares seriam a principal fonte de nutrientes desse ecossistema."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Amazon_Reef",
            "estimating its length at over 1,000 kilometres (600 miles), and its area as over 9,300 km2 (3,600 mi2). "
            "Publication of its discovery was released in April 2016 [...] "
            "Before the reef's discovery, it was originally believed that the Amazon, with its sediment-rich plume, represented a significant gap in reef distribution across the Western Atlantic, "
            "correlating with the accepted view that corals thrived in clear waters along tropical shelves. "
            "The reef primarily owes its existence to its depth, as it is below the freshwater layer of discharge from the Amazon into the Atlantic Ocean [...] "
            "The majority of the reef is made up of beds of rhodolith, various species of red algae, which superficially resemble coral. [...] "
            "northern areas are populated with sponges and carnivorous species such as hydroids. [...] "
            "It is believed that single-celled organisms are central to the reef's ecosystem, providing the main source of nutrients",
            "Amazon Reef")],
    },
    # 10
    {
        "temas_secundarios": ["agua_doce_gelo", "termodinamica"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Perto de Manaus, as águas escuras do rio Negro e as barrentas do Solimões correm lado a lado por quilômetros sem se misturar.",
        "explicacao": (
            "No Encontro das Águas, os dois rios se juntam, mas por cerca de 6 quilômetros seguem lado a lado, cada "
            "um com sua cor. Depois correm mais 60 quilômetros até a mistura se completar. A explicação está nas "
            "grandes diferenças entre eles. O rio Negro é mais quente, perto de 28 graus, e lento, a cerca de 2 "
            "quilômetros por hora. Sua água escura quase não tem sedimento e é tingida por folhas e plantas em "
            "decomposição. O Solimões é mais frio, por volta de 22 graus, corre entre 4 e 6 quilômetros por hora e "
            "traz muito sedimento dos Andes, o que lhe dá a cor clara e barrenta. Com temperatura, velocidade e "
            "carga de sedimentos tão diferentes, as duas águas demoram a se misturar."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Meeting_of_Waters",
            "For 6 km (3.7 mi) the waters of the two rivers run side by side without mixing. [...] "
            "The river then flows another 60 km (37 mi) before mixing fully [...] "
            "This phenomenon is due to the vast differences in temperature, speed, and amount of dissolved sediments in the waters of the two rivers. "
            "The Rio Negro flows at near 2 km/h (1.2 mph) at a temperature of 28 °C (82 °F), while the Rio Solimões flows between 4 and 6 km/h (2.5–3.7 mph) at a temperature of 22 °C (72 °F). "
            "The light-colored water is rich with sediment from the Andes Mountains [...] "
            "is nearly sediment-free and colored by decayed leaf and plant matter.",
            "Meeting of Waters")],
    },
    # 11
    {
        "temas_secundarios": ["clima_tempo", "plantas"],
        "tipos_espanto": ["conexao_inesperada"],
        "gancho": "Parte da chuva que cai no Sudeste, no Sul e no Centro-Oeste do Brasil vem da Amazônia, levada por 'rios voadores' de vapor que as árvores soltam.",
        "explicacao": (
            "As árvores retiram água do solo e liberam parte dela como vapor pelas folhas. Somada à evaporação, essa "
            "evapotranspiração alimenta, sobre a Amazônia, correntes de ar saturadas de vapor d'água, chamadas de "
            "rios atmosféricos, rios voadores ou rios aéreos. O nome é só uma analogia: esses fluxos são invisíveis "
            "e não têm margens definidas como os rios de verdade. Na América do Sul, eles começam em certas regiões "
            "da Amazônia e transportam a umidade da floresta para outras regiões. No Brasil, costumam estar ligados a "
            "chuvas intensas e duradouras no Sudeste, no Sul e no Centro-Oeste. No mundo todo, os rios "
            "atmosféricos respondem por mais de 90% do transporte de vapor d'água no sentido norte-sul, embora "
            "ocupem menos de 10% da circunferência da Terra."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Rios_voadores",
            "Os rios atmosféricos, também conhecidos como rios voadores ou rios aéreos, consistem em fluxos concentrados de vapor de água em médios e altos níveis da atmosfera. "
            "Embora se use a terminologia \"rio\" para o fenômeno, trata-se apenas de uma analogia; os rios atmosféricos são invisíveis e não tem margens claramente definidas [...] "
            "os rios atmosféricos respondem por mais de 90% do transporte global de vapor de água no sentido meridional (norte-sul). Contudo, sua atuação recobre menos de 10% da circunferência da Terra. [...] "
            "Na América do Sul, o fenômeno dos rios atmosféricos tem início a partir de certas regiões da Amazônia. "
            "Estes fluxos de ar saturado com vapor d'água são alimentados pela umidade fornecida pela floresta, transportando umidade e vapor de água advindos da evapotranspiração das árvores para outras regiões. "
            "No Brasil, normalmente estão relacionados ao registro de chuvas intensas e duradouras nas regiões sudeste, sul e centro-oeste.",
            "Rios voadores", idioma="pt")],
    },
    # 12
    {
        "temas_secundarios": ["oceanografia", "esportes_tradicionais"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "A pororoca, onda que o mar empurra rio Amazonas acima, chega a 4 metros, pode avançar até 800 km terra adentro e virou palco de campeonatos de surfe.",
        "explicacao": (
            "A pororoca é um macaréu, uma onda que sobe o rio contra a correnteza. Nas luas nova e cheia, quando a "
            "maré do oceano está mais alta, a água do Atlântico entra pela foz do Amazonas em vez de sair. O fluxo "
            "do rio se inverte e uma elevação de água corre rio acima com grande força, fazendo um barulho que se "
            "ouve de longe. As ondas chegam a 4 metros e podem avançar até 800 quilômetros pelo Amazonas e por rios "
            "vizinhos do Pará. O nome talvez venha do tupi, numa expressão que significaria algo como 'grande "
            "estrondo'. Desde 1999 acontece um campeonato anual de surfe em São Domingos do Capim, no rio Guamá. "
            "Surfar ali é especialmente perigoso, porque a água carrega muitos detritos."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Pororoca",
            "The Pororoca (Portuguese pronunciation: [pɔɾɔˈɾɔkɐ], [poɾoˈɾɔkɐ]) is a tidal bore, with waves up to 4 m (13 ft) high that travel as much as 800 km (500 mi) inland upstream on the Amazon River and adjacent rivers. [...] "
            "Its name might come from the indigenous Tupi language, where it could translate into \"great roar\". [...] "
            "During new and full moons, when the ocean tide is highest, water flows in from the Atlantic, rather than the other way around. The Amazon's flow reverses [...] "
            "a water bulge speeds upstream often with great force, forming a tidal bore with an audible noise. [...] "
            "Since 1999, an annual championship has been held in São Domingos do Capim (on the adjacent Guamá River). "
            "However, surfing the Pororoca is especially dangerous, as the water contains a significant amount of debris")],
    },
    # 13
    {
        "temas_secundarios": ["biomimetica", "arquitetura", "plantas"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "A folha da vitória-régia inspirou o jardineiro que projetou o Palácio de Cristal de Londres. Ele testou sua resistência pondo a filha sobre uma folha.",
        "explicacao": (
            "As primeiras sementes da vitória-régia chegaram à Inglaterra vindas da Amazônia, mas as plantas "
            "cresciam sem florescer. Em 1849, uma muda foi entregue a Joseph Paxton, jardineiro-chefe do Duque de "
            "Devonshire em Chatsworth. Em dois meses as folhas tinham 1,4 metro de diâmetro, e logo veio a flor. A "
            "planta cresceu tanto que foi preciso construir uma estufa nova só para ela. Paxton ficou impressionado "
            "com a folha, que chamou de 'um feito natural de engenharia'. A rigidez vinha de nervuras que se "
            "irradiam do centro, ligadas por nervuras transversais flexíveis. Para testar, ele pôs a filha, Annie, "
            "sobre uma folha flutuando. Paxton aplicou o princípio às estufas, e anos de experimentos levaram ao "
            "projeto que inspirou o Palácio de Cristal, construído para a Grande Exposição de 1851."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Joseph_Paxton",
            "Crystal Palace, which was built in Hyde Park, London to house the Great Exhibition of 1851 [...] "
            "He offered the 20-year-old Paxton the position of head gardener at Chatsworth [...] "
            "The next great building at Chatsworth was built for the first seeds of the Victoria regia lily which had been sent to Kew from the Amazon in 1836. "
            "Although they had germinated and grown they had not flowered and in 1849 a seedling was given to Paxton to try out at Chatsworth. "
            "He entrusted it to Eduard Ortgies, a young gardener and within two months the leaves were 4.5 ft (1.4 m) in diameter, and a month later it flowered. "
            "It continued growing and it became necessary to build a much larger house, the Victoria Regia House. "
            "Inspired by the waterlily's huge leaves – 'a natural feat of engineering' – he found the structure for his conservatory which he tested by floating his daughter Annie on a leaf. "
            "The secret was in the rigidity provided by the radiating ribs connecting with flexible cross-ribs. "
            "Constant experimentation over a number of years led him to devise the glasshouse design that inspired the Crystal Palace.",
            "Joseph Paxton")],
    },
    # 14
    {
        "temas_secundarios": ["americas_pre_colombianas", "cidades"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Sob a floresta amazônica do Equador, um mapeamento a laser revelou cidades com milhares de plataformas de terra, habitadas desde cerca de 500 a.C.",
        "explicacao": (
            "No vale do rio Upano, no leste do Equador, há sinais de ocupação antiga conhecidos desde os anos 1970, "
            "e o arqueólogo francês Stéphen Rostain escava a região desde os anos 1990. A vegetação, porém, "
            "escondia o tamanho do que havia ali. Em 2015, o governo equatoriano financiou um levantamento com "
            "LIDAR, um laser disparado de aeronaves que mapeia o relevo do chão. Os resultados, publicados na "
            "revista Science em janeiro de 2024, mostraram assentamentos espalhados por cerca de 300 quilômetros "
            "quadrados, com cerca de 6 mil plataformas de terra para construções e uma rede de estradas de até 25 "
            "quilômetros ligando as áreas habitadas. As ocupações começaram por volta de 500 a.C., mais de mil anos "
            "antes de qualquer outra sociedade complexa conhecida na Amazônia."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Upano_Valley_sites",
            "The sites comprise several cities; they are believed to have been inhabited as early as 500 BC, predating any other known complex Amazonian society by over a millennium. [...] "
            "The earliest evidence of premodern settlement in the Upano Valley region was found in the 1970s. [...] "
            "began excavations in the region during the 1990s. Exploration of the sites accelerated after the government of Ecuador funded a LIDAR survey of the Upano Valley in 2015 [...] "
            "Rostain's team published their findings from the LIDAR survey in Science in January 2024. [...] "
            "The known sites spread across 300 square kilometres (120 square miles) in the Upano River valley. [...] "
            "Around 6,000 of these platforms were discovered [...] "
            "A system of roads, extending as far as 25 kilometres (16 miles), connected the valley's residential areas.",
            "Upano Valley sites")],
    },
]
