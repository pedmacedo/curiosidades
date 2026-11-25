LOTE = "2026-11-25-comida_brasileira-01"
AREA = "comida"
TEMA = "comida_brasileira"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


SC = "https://www.southerncultures.org/article/feijoada-and-hoppin-john"
EID = "https://wwwnc.cdc.gov/eid/article/15/4/08-1450_article"

CANDIDATOS = [
    # 1 a feijoada e o mito das sobras da senzala
    {
        "temas_secundarios": ["heranca_africana", "brasil_colonial", "historia_pratos"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "Conta-se que a feijoada nasceu nas senzalas, com restos de porco desprezados pelos senhores. Estudiosos contestam: orelha e pé eram apreciados na cozinha ibérica, e a feijoada completa era prato de restaurante de elite.",
        "explicacao": (
            "A versão mais difundida no Brasil diz que escravizados das plantações de cana inventaram a feijoada "
            "com sobras de carne descartadas pelos senhores. Vários estudiosos questionam essa origem e veem no "
            "prato mais uma construção europeia ampliada no Brasil do que uma contribuição africana. Ensopados de "
            "carne cozidos em panela de barro existem por toda a Europa, como o cozido português, e as feijoadas "
            "de Portugal já misturavam feijões, linguiças, orelhas e pés de porco. Na cozinha ibérica, miúdos e "
            "vísceras eram valorizados, e pô-los na feijoada seria coisa da elite. O pesquisador Carlos Alberto "
            "Dória faz uma distinção: os escravizados transformaram feijão e farinha numa feijoada simples, comida "
            "de escassez; a feijoada completa, com arroz, couve, laranja e farofa, era servida em restaurantes "
            "das classes mais altas. Uma das menções mais antigas conhecidas é um anúncio de 1827, no Recife, de "
            "uma casa que servia \"excelente feijoada à brasileira\" às quintas-feiras. Câmara Cascudo estima que "
            "a feijoada completa entrou nas cozinhas brasileiras por volta de 1930. Para a autora de um estudo "
            "sobre o tema, a narrativa do prato que mistura todos reforça a imagem do Brasil como \"democracia racial\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": SC,
             "titulo": "Feijoada and Hoppin' John (Southern Cultures)",
             "idioma": "en",
             "trecho": "When expanded into feijoada completa (“complete”), rice, sautéed kale or collard greens, oranges, and toasted manioc flour accompany the beans. [...] "
                       "Brazilian legend holds, and most Brazilians still claim, that feijoada was invented by enslaved Africans who labored on sugarcane plantations and used scraps of meat discarded by their enslavers. "
                       "Although this story of feijoada’s origin is the most widespread, some scholars have called it into question, arguing that feijoada is less an African contribution than a European construct expanded in Brazil. "
                       "Similar clay pot stews appear throughout Europe, such as the Portuguese cozido, Italian bollito, and French cassoulet. [...] "
                       "Brazilian anthropologist Luís da Câmara Cascudo estimates the introduction of feijoada completa into Brazilian kitchens around 1930. "
                       "Culinary scholar Carlos Alberto Dória draws a distinction between feijão (beans), feijoada, and feijoada completa, explaining that the enslaved evolved beans and flour into a simple feijoada, still the food of scarcity and poverty; "
                       "feijoada completa, the dish worthy of celebration and adulation, was reserved for restaurants patronized by the highest social classes. "
                       "In fact, Iberian cuisine is marked by its incorporation of offal and viscera, and the use of those parts in feijoada would have been an option only for the elite. [...] "
                       "As a national dish, the melting pot narrative of feijoada bolsters the image of Brazil as a racial democracy."},
            wiki("Feijoada",
                 "The creation and name of feijoada are related to Portuguese ways of making it, from the regions of Estremadura, Beiras, Trás-os-Montes and Alto Douro, which mix various types of beans - except black beans (of American origin) - sausages, ears and pigs' feet.",
                 nome="Feijoada"),
            wiki("Feijoada",
                 "Esta versão, conhecida como feijoada à brasileira, teve sua primeira menção registrada em 2 de março de 1827, em um anúncio do Diário de Pernambuco, na cidade do Recife, "
                 "O texto informava que, na Locanda d’Águia d’Ouro, na rua das Cruzes, às quintas-feiras era servida uma “excelente feijoada à brasileira, tudo por preço cômodo”.",
                 nome="Feijoada", idioma="pt"),
        ],
    },
    # 2 brigadeiro: doce de candidato derrotado, e o "negrinho" gaúcho
    {
        "temas_secundarios": ["brasil_republica", "palavras_portugues"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O brigadeiro homenageia um candidato que perdeu: o brigadeiro Eduardo Gomes, na eleição de 1945. No Rio Grande do Sul, onde mandava o rival Getúlio Vargas, o doce virou \"negrinho\", segundo memórias de um político.",
        "explicacao": (
            "Segundo historiadores da alimentação, na eleição presidencial de 1945, logo após a queda de Getúlio "
            "Vargas, mulheres engajadas na campanha do brigadeiro da Aeronáutica Eduardo Gomes, candidato da UDN, "
            "organizavam festas para promovê-lo. Um docinho de leite condensado, manteiga, açúcar e chocolate em "
            "pó ajudava a arrecadar fundos, e os convidados passaram a falar no \"docinho do brigadeiro\", que "
            "acabou encurtado. Gomes perdeu para o general Eurico Gaspar Dutra, mas o nome ficou. A versão "
            "tradicional situa a criação entre mulheres do bairro paulistano do Pacaembu, e o contexto ajuda: as "
            "duas únicas fábricas brasileiras de leite condensado, da Nestlé, fundadas em 1921, ficavam em São "
            "Paulo. Versões popularizadas nos anos 1980 levam a invenção para o Rio, a Heloísa Nabuco, de família "
            "tradicional carioca. No Rio Grande do Sul, o doce é o negrinho. Nas memórias do político catarinense "
            "Hercílio Deeke, o motivo é político: com Vargas hegemônico no estado e adversário de Gomes, a "
            "imprensa gaúcha, em boa parte varguista, preferia um substituto para o nome do candidato. Nem a data "
            "é consenso: há pesquisadores que acham que o doce já existia e foi rebatizado, e outros que dizem "
            "que ele só surgiu como é hoje alguns anos depois de 1945."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "consenso_parcial",
        "fontes": [wiki("Brigadeiro_(doce)",
            "No Rio Grande do Sul, ao contrário do resto do país, o brigadeiro é popularmente conhecido pelo nome \"negrinho\". "
            "Tal fato, conforme é relatado nas memórias do político udenista catarinense Hercílio Deeke, se deve também a razões políticas ligadas à candidatura de Eduardo Gomes. "
            "Segundo comenta Hercílio, o forte antagonismo político do caudilho gaúcho Getúlio Vargas - hegemônico na política gaúcha da época e forte opositor da candidatura de Eduardo Gomes - fez com que no Rio Grande do Sul o termo \"brigadeiro\" fosse pouco utilizado, usando-se em seu lugar o termo \"negrinho\" como um substituto \"politicamente aceitável\" para os meios de comunicação majoritariamente varguistas, abertamente hostis ao candidato da UDN. [...] "
            "Conforme relatam historiadores da alimentação, o nome seria uma homenagem ao brigadeiro da Força Aérea Brasileira Eduardo Gomes. "
            "Durante a candidatura do militar à presidência da República pela União Democrática Nacional na eleição de 1945, um grupo de mulheres paulistanas do bairro do Pacaembu, que eram engajadas na campanha do candidato, organizaram festas para promover sua candidatura. "
            "O doce teria sido criado por essas mulheres durante a primeira campanha do candidato à presidência, pela conservadora UDN, logo após a queda de Getúlio Vargas. "
            "A guloseima, feita de leite condensado, manteiga, açúcar e chocolate em pó, inicialmente feita como uma forma de arrecadar fundos para a campanha [...] "
            "estes logo começaram a chamar os amigos para irem comer o \"docinho do brigadeiro\". [...] "
            "Apesar do apoio recebido, Eduardo Gomes foi derrotado no pleito, tendo a eleição sido vencida pelo então general Eurico Gaspar Dutra. [...] "
            "Era justamente no estado de São Paulo em que se encontravam as duas únicas fábricas brasileiras de leite condensado (as fábricas da Nestlé nos municípios de Araras e São Paulo, fundadas em 1921) [...] "
            "Algumas versões, aparentemente derivadas da história acima descrita e popularizadas nos anos 1980, narram histórias similares vinculando o doce à campanha de Eduardo Gomes, alterando no entanto a localidade da criação do doce e alegando que o mesmo foi criado por mulheres do Rio de Janeiro. "
            "Em uma delas cita-se que Heloísa Nabuco, de tradicional família carioca que apoiava o brigadeiro Gomes [...] "
            "Alguns pesquisadores divergem sobre a data da origem do brigadeiro: para Cláudio Fornari e Joyce Galvão, o doce teria surgido anos antes e sido rebatizado na campanha de Gomes, enquanto Viviane Aguiar e Mário Viaro afirmam que ele teria surgido como é conhecido hoje apenas alguns anos após a eleição de 1945.",
            nome="Brigadeiro (doce)", idioma="pt")],
    },
    # 3 pão de queijo: cresce sem fermento e virou rosquinha no Japão
    {
        "temas_secundarios": ["ciencia_cozinha", "povos_indigenas", "palavras_viajantes"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "O pão de queijo cresce sem fermento: o polvilho, amido da mandioca, forma uma massa elástica que prende o ar. Levado ao Japão pelos dekasseguis, ele deu nome e inspiração ao pon de ring, rosquinha da Mister Donut.",
        "explicacao": (
            "A receita é de Minas Gerais. Com a descoberta das minas perto de Ouro Preto, por volta de 1700, não "
            "havia trigo na região, e cozinheiros locais passaram a fazer uma espécie de pão com o amido da "
            "mandioca, que os tupiniquins lhes tinham mostrado. O queijo ralado só entrou no fim do século XIX. "
            "O segredo da textura está no polvilho, doce e azedo: diferente dos pães comuns, o pão de queijo não "
            "leva fermento. Pequenas bolsas de ar na massa se expandem no forno e ficam presas pela elasticidade "
            "da pasta de amido, que deixa o pãozinho crocante por fora e borrachudo por dentro. Sem farinha de "
            "trigo, ele também não tem glúten. O pão de queijo chegou ao Japão com os dekasseguis. Em 2003, a "
            "rede Mister Donut lançou o pon de ring, um anel de oito bolinhas grudadas, batizado a partir do pão "
            "de queijo. Ele popularizou os chamados mochi donuts, que depois chegaram aos Estados Unidos pelo "
            "Havaí. O nome engana: nem o pon de ring nem o pão de queijo costumam levar a farinha de arroz "
            "glutinoso do mochi. Os dois usam, em geral, amido de mandioca, embora a rosquinha japonesa também "
            "leve trigo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Pão_de_queijo",
                 "It is a traditional Brazilian recipe, originating in the state of Minas Gerais. [...] "
                 "The cassava flour is what gives the snack its distinct texture, which is chewy and elastic, being crunchy on the outside. [...] "
                 "In Brazil, traditionally, both sour and sweet cassava flour are used [...] "
                 "With the discovery of mines near Ouro Preto in around 1700, some 20% of the Brazilian population at that time, mainly slaves, occupied a vast territory in southeast Brazil. "
                 "Since wheat was not available, local cooks created a kind of bread from starch derived from the cassava tubers shown to them by Tupiniquins indigenous groups. "
                 "In the late 19th century, grated hard cheese was added. [...] "
                 "The cassava flour is a powerful starch which is key to the texture of the pão de queijo; unlike other types of bread, pão de queijo is not leavened. "
                 "Small pockets of air within the dough expand during baking and are contained by the elasticity of the starch paste. "
                 "Because it is made of cassava flour (as opposed to wheat flour), pão de queijo contains no gluten. [...] "
                 "Pão de queijo arrived in Japan with the dekasegi. [...] "
                 "It also inspired the popular donut chain Mister Donut in its creation of Pon de Ring",
                 nome="Pão de queijo"),
            wiki("Mochi_donut",
                 "In 2003, the Japanese donut chain Mister Donut launched pon de ring (ポン・デ・リング, Pon De Ringu), named after the Brazilian pão de queijo bread. "
                 "This iteration of the hybrid confection was popularized in Japan before spreading to the United States via Hawaii. [...] "
                 "The \"pon de ring\" style is shaped into a ring of eight connected small balls. "
                 "On calling the pon de ring style a mochi donut, Epicurious stated: \"oddly enough, neither pon de ring or pão de queijo are made with glutinous rice flour. "
                 "Both typically use tapioca flour, and while pão de queijo is gluten-free, most recipes for pon de ring also include wheat flour.",
                 nome="Mochi donut"),
        ],
    },
    # 4 açaí: de comida básica ribeirinha a "superalimento"
    {
        "temas_secundarios": ["amazonia", "economia_curiosa"],
        "tipos_espanto": ["contraintuitivo", "mito_desmentido"],
        "gancho": "Na foz do Amazonas, o açaí é comida básica há séculos: em três comunidades caboclas estudadas, chegava a 42% do que se comia, em peso. A tigela com granola surgiu nos anos 1980 e virou \"superalimento\" sem prova.",
        "explicacao": (
            "O açaí é o fruto de uma palmeira das várzeas e áreas alagadas da Amazônia, e o Brasil responde por "
            "99% da produção mundial. Por volta do século XVIII, virou alimento básico nas várzeas, e até hoje é "
            "a planta mais importante da dieta de populações tradicionais: num estudo com três comunidades "
            "caboclas, ele somava até 42% de tudo o que se comia, em peso. Ali, o fruto é amassado e vira pasta "
            "ou bebida, que a maior parte da população amazônica toma diariamente. O resto do mundo só o "
            "descobriu há pouco. Nos anos 1980, a família Gracie passou a vender açaí como bebida energética ou "
            "batido com granola e banana, e só em meados dos anos 1990 começaram o consumo nas cidades e a fama "
            "de comida saudável. Em 2003, um médico famoso nos Estados Unidos o pôs na lista dos "
            "\"superalimentos\", e as promessas exageradas atraíram golpistas: em 2009, os golpes com açaí "
            "lideraram a lista de fraudes da Comissão Federal de Comércio americana, que em 2012 impôs uma "
            "condenação de 80 milhões de dólares a cinco empresas que prometiam emagrecimento. Até 2009, não "
            "havia evidência científica de que o açaí afetasse o peso ou trouxesse qualquer benefício à saúde."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Açaí_palm",
                 "The species is native to the Amazon, mainly in swamps and floodplains, with Brazil holding 99% of global production. [...] "
                 "The fruit became a staple food in floodplain areas around the 18th century, but its consumption in urban areas and promotion as a health food only began in the mid-1990s along with the popularization of other Amazonian fruits outside the region. [...] "
                 "In the 1980s, the Brazilian Gracie family marketed açaí as an energy drink or as crushed fruit served with granola and bananas [...] "
                 "In 2009, açaí scams were ranked No. 1 on the U.S. Federal Trade Commission's \"scams and rip-offs\" list [...] "
                 "In 2003, American celebrity doctor Nicholas Perricone included açaí berries among \"superfoods\", but such extravagant marketing claims regarding açaí as miracle cures for everything from obesity to attention-deficit disorder were challenged in subsequent studies. "
                 "The FTC handed down an $80 million judgement in January 2012 against five companies that were marketing açaí berry supplements with fraudulent claims that their products promoted weight loss and prevented colon cancer. [...] "
                 "Fresh açaí has been consumed as a dietary staple in the region around the Amazon river delta for centuries. [...] "
                 "In a study of three traditional Caboclo populations in the Brazilian Amazon, açaí palm was described as the most important plant species because the fruit makes up a major component of their diet, up to 42% of the total food intake by weight. [...] "
                 "As of 2009, there is no scientific evidence that açaí consumption affects body weight, promotes weight loss or has any positive health effect.",
                 nome="Açaí palm"),
            {"url": EID,
             "titulo": "Oral Transmission of Chagas Disease by Consumption of Açaí Palm Fruit, Brazil (Emerging Infectious Diseases, CDC)",
             "idioma": "en",
             "trecho": "it is crushed to produce a paste or beverage. Most of the Amazonian population consumes açaí juice daily."},
        ],
    },
    # 5 açaí e a doença de Chagas pela boca
    {
        "temas_secundarios": ["doencas_infecciosas", "amazonia"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Na Amazônia, a doença de Chagas costuma chegar pela boca: de 437 casos agudos na região entre 1968 e 2005, 311 vieram de surtos em que o suspeito era o açaí, contaminado por barbeiros na hora de fazer a polpa.",
        "explicacao": (
            "A Amazônia brasileira não era considerada área endêmica da doença de Chagas. Ainda assim, o primeiro "
            "surto da forma aguda na região, registrado em 1968, já levantou a suspeita de transmissão oral, e de "
            "1968 a 2005 foram notificados 437 casos agudos, 311 deles ligados a 62 surtos em que o suspeito era "
            "o consumo de açaí. Acredita-se que a contaminação venha das fezes dos barbeiros, os insetos "
            "transmissores, deixadas no fruto, ou de insetos moídos sem querer junto com ele na hora de fazer a "
            "polpa. Provar era difícil: os surtos atingem grupos pequenos em que todos comem a mesma coisa, o que "
            "impede apontar um alimento. Em 2006, o Pará notificou 178 casos agudos, onze deles em Barcarena, "
            "confirmados pela visão do parasita no sangue. Os investigadores compararam quem adoeceu com quem não "
            "adoeceu. Numa reunião num posto de saúde, 6 pessoas dividiram uma refeição, e 5 delas ficaram "
            "doentes. Tomar suco ou comer pasta grossa de açaí ali se associou à infecção, e o açaí gelado "
            "pareceu proteger. Nenhum barbeiro foi achado nos locais vistoriados, e os autores pedem estudos sobre "
            "a sobrevivência do parasita no açaí: o fruto é parte central da dieta e da economia da região."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [{"url": EID,
            "titulo": "Oral Transmission of Chagas Disease by Consumption of Açaí Palm Fruit, Brazil (Emerging Infectious Diseases, CDC)",
            "idioma": "en",
            "trecho": "In 2006, a total of 178 cases of acute Chagas disease were reported from the Amazonian state of Pará, Brazil. "
                      "Eleven occurred in Barcarena and were confirmed by visualization of parasites on blood smears. "
                      "Using cohort and case–control studies, we implicated oral transmission by consumption of açaí palm fruit. [...] "
                      "Chagas disease has not been considered endemic in the Brazilian Amazon region. "
                      "The first Amazonian outbreak of acute Chagas disease was reported in 1968; oral transmission was suspected (8). "
                      "During 1968–2005, a total of 437 cases of acute Chagas disease were reported in this region. "
                      "Of these cases, 311 were related to 62 outbreaks in which the suspected mode of transmission was consumption of açaí (9). [...] "
                      "Contamination is believed to be caused by triatomine stools on the fruit or insects inadvertently crushed during processing (10). [...] "
                      "Because outbreaks with high attack rates occur in small groups whose members all consume the same foods, açaí has not been epidemiologically implicated in transmission of this disease. [...] "
                      "Of these persons, 6 shared a meal, 5 (83%) of whom were case-patients. [...] "
                      "Exposures associated with infection were consumption of thick açaí paste and drinking açaí juice at the health post; consumption of chilled açaí was protective (Table 2). [...] "
                      "No triatomine insects were identified at any sites of the entomologic investigation. [...] "
                      "Studies are needed to determine viability of T. cruzi in açaí, along with the tree-to-bowl continuum of açaí, to identify sources of contamination. "
                      "Because açaí is a major dietary component in the Amazon region and a component of the local economy, identifying practical prevention measures is essential."}],
    },
    # 6 pastel de feira e os imigrantes japoneses
    {
        "temas_secundarios": ["historia_pratos", "segunda_guerra"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O pastel de feira teria surgido nos anos 1940, em Santos, entre descendentes de japoneses que adaptaram o rolinho-primavera chinês. Segundo relatos, na guerra, pasteleiros japoneses se passavam por chineses.",
        "explicacao": (
            "Em Portugal, pastel costuma ser assado, como o de nata, embora haja fritos, como o de bacalhau. O "
            "pastel de feira brasileiro, frito e em forma de retângulo ou meia-lua, tem outra história. Segundo a "
            "versão mais contada, ele nasceu na década de 1940, em Santos, entre descendentes de imigrantes "
            "japoneses, que adaptaram rolinhos-primavera e guiozas das cozinhas chinesa e japonesa aos "
            "ingredientes disponíveis no Brasil, trocando, por exemplo, o saquê pela cachaça. Algumas versões "
            "acrescentam um detalhe: durante a Segunda Guerra Mundial, imigrantes japoneses abriram pastelarias "
            "apresentando-se como chineses, para escapar da discriminação provocada pela guerra. A receita se "
            "espalhou depressa. Ainda nos anos 1940, o pastel já estava entre os alimentos mais consumidos no "
            "estado de São Paulo, nas feiras livres e nas pastelarias. Chegou ao Rio de Janeiro e a Belo "
            "Horizonte nos anos 1950, ao Paraná nos anos 1960 e ao Rio Grande do Sul e a Santa Catarina nos anos "
            "1970. Hoje faz parte até da política: comer pastel na feira é gesto clássico de candidato, e a "
            "campanha eleitoral ganhou na internet o apelido de \"temporada do pastel\"."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Pastel_(culinária)",
                 "No Brasil, o pastel assume um formato característico retangular ou em meia-lua e geralmente é frito, levando por vezes o nome de \"pastel de feira\", em referência à sua tradicional comercialização em feiras livres pelo país. [...] "
                 "Em Portugal, o pastel consiste em uma porção de massa que assume formatos diversos e geralmente são assados, a exemplo do pastel de nata, do pastel de feijão e do pastel de Vouzela. "
                 "São também populares versões fritas, como o pastel de bacalhau. [...] "
                 "O pastel, como hoje conhecemos no Brasil, se originou na década de 1940 por meio dos descendentes de imigrantes japoneses em Santos, no estado de São Paulo como uma adaptação dos rolinhos-primavera e dos guiozas da culinária chinesa e da culinária japonesa, que adaptaram a receita original dos rolinhos-primavera aos ingredientes que tinham disponíveis no Brasil, substituindo ingredientes como o saquê por cachaça. "
                 "Segundo relatam algumas versões, os imigrantes japoneses, durante a Segunda Guerra Mundial, difundiram o prato, abrindo pastelarias no intuito de se passarem por chineses para se livrarem da discriminação que havia na época em razão da guerra. "
                 "A receita rapidamente se espalhou por São Paulo e depois pelo resto do país, sendo ainda na década de 1940, um dos alimentos mais consumidos no estado de São Paulo, sendo vendido tanto em feiras livres quanto em pastelarias. "
                 "Na década de 1950, o costume de comer pastéis chega ao Rio de Janeiro e em Belo Horizonte. [...] "
                 "Na década de 1960, o costume espalhou-se para o sul do país, sendo em 1962 fundada a primeira pastelaria da cidade de Maringá, no Paraná. "
                 "Posteriormente, na década de 1970, o costume chegou também no Rio Grande do Sul e Santa Catarina. [...] "
                 "O pastel de feira é comum em campanhas eleitorais no Brasil. "
                 "O ato de comer pastel é usado com frequência pelos políticos como forma de se aproximar da população. "
                 "A ação é alvo de repercussão e memes da Internet, que apelidam o período de campanha eleitoral no Brasil de \"temporada do pastel\".",
                 nome="Pastel (culinária)", idioma="pt"),
            wiki("Pastel_(food)",
                 "Popular folklore states that Brazilian pastels originated when Japanese immigrants adapted Chinese fried spring rolls to sell as snacks at weekly street markets.",
                 nome="Pastel (food)"),
        ],
    },
    # 7 Habib's: fast-food árabe criado por um padeiro português
    {
        "temas_secundarios": ["economia_curiosa", "historia_pratos"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O Habib's, rede brasileira de comida árabe, foi fundado em 1988 por um padeiro nascido em Portugal, sem laços com o Oriente Médio. A ideia surgiu quando um senhor idoso de origem árabe lhe pediu emprego.",
        "explicacao": (
            "A cozinha do Oriente Médio chegou ao Brasil com os imigrantes, sobretudo do Líbano e da Síria, e a "
            "esfiha, ou esfirra, apareceu com a chegada dos libaneses. Era popular, mas pouco acessível e "
            "costumava ser cara. Segundo o relato da fundação do Habib's, em 1988 um senhor de origem árabe, já "
            "doente, pediu emprego na padaria de Alberto Saraiva, padeiro nascido em Portugal. Não havia vaga. Ao "
            "saber que o homem tinha sido cozinheiro na terra natal, Saraiva resolveu abrir uma pequena "
            "lanchonete de comida rápida do Oriente Médio, novidade no país, apostando justamente nisso, e "
            "contratou o senhor. O primeiro restaurante abriu no mesmo ano, e a procura reprimida formou filas na "
            "porta quase desde o primeiro dia. A rede cresceu, passou de 475 lojas e ficou conhecida pelos preços "
            "muito baixos. A esfiha também se abrasileirou: aqui ela é assada, pode ser aberta ou fechada em "
            "triângulo e ganhou versões doces, até de chocolate. Ela só se popularizou de vez no fim do século "
            "XX, e redes como o Habib's vendem centenas de milhões de esfihas por ano."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Habib%27s",
                 "It has more than 475 outlets (many of them self-owned) across the country and has recently begun expansion into foreign markets. "
                 "It is known for very low prices and Lebanese-Brazilian dishes. "
                 "Middle Eastern dishes are very popular in Brazil ever since the immigration of people from that area (particularly Lebanon and Syria) into Brazil. [...] "
                 "Habib's was founded by a Portuguese-born baker, Alberto Saraiva, who had no particular ties to the Middle East himself, got the idea early in 1988 after an ailing old man of Arab descent applied for a job in his bakery. "
                 "With no job at hand for the man to apply to, but upon learning that he had been a cook back in his home land, Mr. Saraiva decided to open a small fast-food restaurant focused on Middle-Eastern fast-food, unheard at the time in Brazil, believing the success could rely on the novelty of it, and hired the man. "
                 "The first Habib's restaurant was opened later that same year. "
                 "Before Habib's, Middle Eastern cuisine, despite being popular, was not readily available and the prices were usually high. "
                 "The repressed demand was strong and people queued in front of the restaurant almost since the first day.",
                 nome="Habib's"),
            wiki("Sfiha",
                 "In Brazil, esfiha gained popularity in the late 20th century, and since has become one of the most common fast foods. [...] "
                 "Esfihas in Brazil are oven-baked and may be open-faced flatbreads about four inches in diameter with meat topping, or folded into a triangular pastry like fatayer. [...] "
                 "Esfiha, or esfirra, first appeared in Brazil following the arrival of Lebanese immigrants. "
                 "Esfihas come in both sweet and savory forms, with toppings like sausage or chocolate. [...] "
                 "Brazilian fast food chains that offer Arab cuisine-inspired foods like Habib's sell hundreds of millions of esfihas a year.",
                 nome="Sfiha"),
        ],
    },
    # 8 quindim: gemas de convento, coco do Nordeste e nome banto
    {
        "temas_secundarios": ["heranca_africana", "palavras_viajantes", "brasil_colonial"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "Por que tantos doces portugueses só levam gema? Conventos gastavam muita clara para engomar hábitos. No Brasil, as gemas encontraram o coco do Nordeste e viraram o quindim, nome que vem do quicongo, língua banta.",
        "explicacao": (
            "Em Portugal, conventos e mosteiros usavam grandes quantidades de clara de ovo para engomar roupas, "
            "como os hábitos de frades e freiras. Era comum aproveitar as gemas que sobravam em bolos e doces, e "
            "assim se multiplicaram pelo país receitas como o papo de anjo e os fios de ovos. O próprio pastel de "
            "nata deriva de um doce criado por monges do Mosteiro dos Jerónimos, em Lisboa. No Brasil, essa "
            "tradição de gemas encontrou dois ingredientes fartos no Nordeste colonial: o coco e o açúcar, então "
            "uma grande indústria. A combinação que deu no quindim provavelmente foi criada por africanos "
            "escravizados, no século XVII. O nome também tem raiz africana: vem de dikende, palavra do quicongo, "
            "língua banta, que designa os gestos, os modos ou o humor característicos das meninas adolescentes. O "
            "quindim é um creme assado, de gema, açúcar e coco ralado, desenformado como um copinho virado, "
            "brilhante e de amarelo intenso; feito numa forma grande de anel, vira quindão e é servido em fatias. "
            "O doce batizou até um personagem de Monteiro Lobato, o rinoceronte Quindim."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Quindim",
                 "Quindim (Portuguese pronunciation: [kĩ ˈdʒĩ] ) is a popular Brazilian baked dessert of Portuguese heritage, made chiefly from sugar, egg yolks and ground coconut. "
                 "It is a custard and usually presented as an upturned cup with a glistening surface and intensely yellow color. "
                 "The mixture can also be made in a large ring mold (like a savarin mold) in which case it is called a \"quindão\" and served in slices. [...] "
                 "The word quindim comes from dikende in Kikongo, a Bantu language. "
                 "It means \"the gestures, or demeanor, or humor characteristic of adolescent girls.\" [...] "
                 "The heavy use of egg yolks is characteristic of many Portuguese sweets and pastries, such as the papo de anjo (\"angel's crop\") and fios de ovos (\"egg threads\"). "
                 "Their combination with coconut and sugar was probably created by African slaves in 17th century Brazilian Northeast,  where coconuts were abundant and sugar (from sugarcane) was a major industry. [...] "
                 "Quindim is also a rhinoceros character (named after the dessert) featured in Monteiro Lobato's children's books.",
                 nome="Quindim"),
            wiki("Pastel_de_nata",
                 "Pastéis de nata tarts are pastries inspired by an original recipe called pastéis de Belém, which were created before the 18th century by Catholic monks at the Jerónimos Monastery in the civil parish of Belém, in Lisbon. "
                 "At the time, convents and monasteries used large quantities of egg-whites for starching clothes, such as friars and nuns' religious habits. "
                 "It was quite common for monasteries and convents to use the leftover egg yolks to make cakes and pastries, resulting in the proliferation of sweet pastry recipes throughout the country.",
                 nome="Pastel de nata"),
        ],
    },
    # 9 castanha-do-pará: abelhas grandes, cutias e a Bolívia
    {
        "temas_secundarios": ["amazonia", "ecologia", "plantas"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "A castanha-do-pará quase não dá em plantação: só abelhas grandes de floresta intacta polinizam a árvore, e são cutias que roem o ouriço e enterram as sementes. Na exportação, quem lidera em valor é a Bolívia.",
        "explicacao": (
            "A castanheira, Bertholletia excelsa, está entre as maiores e mais longevas árvores da Amazônia: chega "
            "a 50 metros e pode viver 500 anos ou mais. Suas flores só são polinizadas por abelhas de grande "
            "porte, de gêneros como Bombus, Eulaema e Xylocopa, que faltam nas matas alteradas. Por isso, ela dá "
            "fruto quase só em floresta preservada, e as plantações, de produção baixa, ainda não são "
            "economicamente viáveis. O fruto, o ouriço, tem casca lenhosa, pesa até 2 kg e leva 14 meses para "
            "amadurecer depois da polinização. Dentro há de oito a 24 sementes, as castanhas. Um pequeno furo "
            "numa das pontas permite que roedores grandes, como a cutia, roam a casca. Elas comem parte das "
            "sementes e enterram outras para depois, e algumas dessas germinam. As mudas podem esperar anos "
            "dormentes, até que uma árvore caia e a luz chegue. Como quase toda a castanha exportada é colhida na "
            "mata, o negócio é citado como modelo de renda sem derrubar a floresta. Brasil e Bolívia somaram 87% "
            "da produção mundial em 2024, mas a Bolívia ficou com 54% do valor exportado: o Brasil vende mais "
            "castanha com casca, e Bolívia e Peru, com mais beneficiamento, a castanha descascada."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Brazil_nut",
            "It is one of the largest and longest-lived trees in the Amazon rainforest. [...] "
            "The Brazil nut is a large tree, reaching 50 metres (160 feet) tall, with a trunk 1 to 2 m (3 to 7 ft) in diameter, making it among the largest of trees in the Amazon rainforest. "
            "It may live for 500 years or more, and can often reach a thousand years of age. [...] "
            "Brazil nut trees produce fruit almost exclusively in pristine forests, as disturbed forests lack the large-bodied bees of the genera Bombus, Centris, Epicharis, Eulaema, and Xylocopa, which are the only ones capable of pollinating the tree's flowers [...] "
            "Brazil nuts have been harvested from plantations, but production is low and is currently not economically viable. "
            "The fruit takes 14 months to mature after pollination of the flowers. "
            "The fruit itself is a large capsule 10–15 cm (4–6 in) in diameter, resembling a coconut endocarp in size and weighing up to 2 kg (4 lb 7 oz). "
            "It has a hard, woody shell 8–12 mm (3⁄8–1⁄2 in) thick, which contains eight to 24 wedge-shaped seeds 4–5 cm (1+5⁄8–2 in) long (the \"Brazil nuts\") [...] "
            "The capsule contains a small hole at one end, which enables large rodents like the agouti to gnaw it open. "
            "They then eat some of the seeds inside while burying others for later use; some of these are able to germinate into new Brazil nut trees. "
            "Most of the seeds are \"planted\" by the agoutis in caches during wet season, and the young saplings may have to wait years, in a state of dormancy, for a tree to fall and sunlight to reach it, when it starts growing again. [...] "
            "In 2024, world production of Brazil nuts (in shells) was 79,736 tonnes, most of which derived from tropical Amazon forest regions of Brazil and Bolivia, which together produced 87% of the total (table). "
            "Brazil nuts are traded both in-shell and shelled. "
            "Brazil is the main exporter of in-shell nuts, while Bolivia and Peru are the principal exporters of shelled kernels, reflecting a larger processing sector in the latter two countries. "
            "In 2024 the global Brazil nut export market was valued at about US$326 million, with Bolivia accounting for the largest share at 54% of total export value. [...] "
            "Since most of the production for international trade is harvested in the wild, the business arrangement has been advanced as a model for generating income from a tropical forest without destroying it.",
            nome="Brazil nut")],
    },
    # 10 cupuaçu: domesticado há milênios, virou marca japonesa
    {
        "temas_secundarios": ["povos_indigenas", "domesticacao", "leis_julgamentos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "O cupuaçu foi domesticado na Amazônia a partir do cupuí, há 5.000 a 8.000 anos, segundo um estudo genético. Em 1998, uma empresa japonesa registrou \"cupuaçu\" como marca; o Japão só cancelou o registro em 2004.",
        "explicacao": (
            "Um estudo genético publicado em 2023 concluiu que o cupuaçu não é uma espécie irmã do cupuí, como "
            "se pensava, mas uma forma domesticada dele, provavelmente surgida no médio e alto rio Negro. Um "
            "gargalo genético indica uma primeira fase de domesticação entre 5.000 e 8.000 anos atrás. Parente "
            "do cacau, o fruto teve por muito tempo só a polpa aproveitada, em sorvetes, sucos e doces; as "
            "sementes eram consideradas lixo. No fim dos anos 1980, a pesquisadora Fátima Ribeiro de Nazaré, da "
            "Embrapa em Belém, adaptou o processo do chocolate às sementes e criou o cupulate, que por motivos "
            "legais não pode se chamar chocolate. Mas a Asahi Foods, empresa de Quioto, tinha registrado em 1998 "
            "o nome cupuaçu como marca, e depois o registro valia no Japão, na Europa e nos Estados Unidos. "
            "Pequenos produtores da Amazônia ouviram de importadores alemães que não podiam pôr a palavra "
            "\"cupuaçu\" nos rótulos. ONGs brasileiras contestaram no Japão, com participação do Itamaraty. Em "
            "2004, o escritório de marcas japonês cancelou o registro: era o nome comum de uma matéria-prima e "
            "podia enganar o público. O pedido de patente da empresa para transformar as sementes num produto "
            "parecido com chocolate também foi negado no Japão, porque a Embrapa tinha pedido antes."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.nature.com/articles/s43247-023-01066-z",
             "titulo": "Domestication of the Amazonian fruit tree cupuaçu may have stretched over the past 8000 years (Communications Earth & Environment)",
             "idioma": "en",
             "trecho": "Published: 01 November 2023 [...] "
                       "Our results indicate that cupuaçu is a domesticated variant of its wild relative, cupuí (T. subincanum), probably originating from the Middle-Upper Rio Negro basin. "
                       "A first phase of domestication is observed through a genetic bottleneck that we estimated to have occurred 5000–8000 years before the present. [...] "
                       "Cupuaçu is therefore not a sister species of cupuí, as suggested in phylogenetic studies, but is instead nested within it."},
            {"url": "https://www.ipsnews.net/?p=9381",
             "titulo": "BRAZIL: Amazonian 'Chocolate' Free of Japanese Patent (Inter Press Service)",
             "idioma": "en",
             "trecho": "The Japan Patent Office denied Asahi Foods the patent for processing cupuaçú seeds into a chocolate-like product. "
                       "The refusal was based on the principle of anteriority, given that the Brazilian governmental agricultural research agency, Embrapa, had sought an international patent for the process in 1999 [...] "
                       "The same Asahi Foods registered the indigenous Brazilian name \"cupuaçú\" as its own trademark with the appropriate agencies in Japan, Europe and the United States. "
                       "The company, based in Kyoto, Japan, even set up a subsidiary named \"Cupuacu International, Inc.\" [...] "
                       "Brazilian producers of jellies and sweets made from the fruit were told by German importers that they had to remove the word \"cupuaçú\" from the product labels because it was trademarked and belonged to the Japanese firm. [...] "
                       "Brazil’s foreign ministry is also participating in the petition to cancel the Japanese trademark [...] "
                       "Traditionally, only the pulp was used in making ice cream, juice, sweets and jellies. "
                       "Its seeds were considered waste, and only some were saved for planting more cupuaçú trees. "
                       "Fátima Ribeiro de Nazaré, an Embrapa researcher for more than three decades, had the idea to put the discarded seeds to some use. [...] "
                       "Her research at Embrapa’s Eastern Amazon Centre, based in the Amazonian city of Belém, finally produced the desired results in the late 1980s. "
                       "The processing of the cupuaçú seed produces a butter and a cake-like substance, raw materials for a final product that, for legal reasons of protection of cacao production, cannot be called \"chocolate\", she said. "
                       "The hybrid name \"cupulate\" thus emerged."},
            {"url": "https://www.migalhas.com.br/quentes/3850/cupuacu",
             "titulo": "Brasil vence caso \"CUPUAÇU\" (Migalhas)",
             "idioma": "pt",
             "trecho": "quarta-feira, 3 de março de 2004 [...] "
                       "A medida administrativa apresentada, há quase um ano, pelo IDCID – Instituto de Direito do Comércio Internacional e Desenvolvimento em conjunto com as ONGs Amazonlink, Rede GTA e Associação de Produtores Alternativos de Rondônia, que contestava o registro da marca \"CUPUAÇU\" no Japão pela multinacional Asahi Foods Corporation, foi julgada pelo Escritório de Marcas Japonês (JPO). [...] "
                       "Em 1998, a empresa japonesa registrou o nome Cupuaçu como uma marca comercial. [...] "
                       "Os examinadores do JPO concordaram com os argumentos apresentados pela ação, cancelando o registro da marca. [...] "
                       "o nome seria a designação comum de uma matéria-prima e, portanto, recairia na proibição prevista no artigo 3º, parágrafo 1º, item \"iii\" da Lei de Marcas do Japão; e [...] "
                       "os examinadores do JPO consideraram a marca \"CUPUAÇU\" capaz de ludibriar o público"},
        ],
    },
    # 11 o sanduíche bauru, inventado em São Paulo
    {
        "temas_secundarios": ["nomes_lugares", "historia_pratos"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O sanduíche bauru não nasceu em Bauru: foi pedido em 1934, num restaurante de São Paulo, por um estudante de Direito apelidado de Bauru. Depois, a cidade pôs a receita numa lei municipal, com certificação oficial.",
        "explicacao": (
            "Em 1934, Casemiro Pinto Neto estudava na Faculdade de Direito do Largo de São Francisco e era "
            "chamado de Bauru, porque vinha da cidade paulista de mesmo nome. Num dia, entrou no Ponto Chic, "
            "casa tradicional e ponto de encontro de estudantes, e pediu ao cozinheiro um sanduíche montado do "
            "jeito que ele descreveu. O \"sanduíche do Bauru\" fez sucesso imediato e acabou virando o prato "
            "mais vendido do lugar. A receita tradicional leva queijo derretido em banho-maria, em geral "
            "muçarela, fatias de rosbife, tomate e pepino em conserva, num pão francês sem o miolo. Com a fama, "
            "muitas lanchonetes passaram a vender \"baurus\" bem diferentes, com presunto no lugar do rosbife ou "
            "pão de forma no lugar do pão francês. A cidade de Bauru acabou adotando o sanduíche tradicional "
            "como seu sanduíche oficial, fixou a receita numa lei municipal e criou um programa oficial de "
            "certificação. Assim, o lanche que leva o nome da cidade, inventado na capital, passou a ter a "
            "receita protegida justamente por ela."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Bauru_(sandwich)",
            "The traditional recipe calls for cheese (usually mozzarella) melted in a bain-marie, slices of roast beef, tomato and pickled cucumber in a pão francês with the crumb (the soft inner part) removed. "
            "The Bauru has a fairly well-documented history. "
            "In 1934, a student at the Faculdade de Direito do Largo de São Francisco, in São Paulo, Casemiro Pinto Neto (known as Bauru for coming from the city of the same name in São Paulo state), entered Ponto Chic, a traditional eatery and student hangout, and asked the cook to prepare a sandwich from his specifications. "
            "\"Bauru's Sandwich\" was an immediate hit, and eventually became the best-selling dish at the place. "
            "Many other eateries, though, offer sandwiches named \"Bauru\" with different combinations of ingredients—for instance, using sliced ham instead of roast beef or sliced bread instead of French bread. "
            "The city of Bauru eventually named the traditional Bauru as the city's official sandwich, codifying the recipe in a municipal law and instituting an official certification program.",
            nome="Bauru (sandwich)")],
    },
    # 12 tapioca: do tupi às bolinhas do bubble tea
    {
        "temas_secundarios": ["povos_indigenas", "palavras_viajantes", "asia_antiga"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "As bolinhas do bubble tea de Taiwan são feitas do mesmo amido da tapioca brasileira, tirado da mandioca. E a palavra \"tapioca\" é tupi: tipi'óka quer dizer \"sedimento\", o amido que assenta no fundo do pote.",
        "explicacao": (
            "A tapioca é o amido extraído da raiz da mandioca, planta nativa do Norte e do Nordeste do Brasil "
            "que hoje cresce também na África Ocidental e no Sudeste Asiático. Na produção tradicional dessas "
            "regiões brasileiras, ela é um subproduto da farinha: a massa da raiz já tratada é espremida no "
            "tipiti, o tubo de palha trançada, e escorre um líquido rico em amido. Em repouso, os grãos "
            "microscópicos de amido assentam no fundo; o líquido de cima é descartado, e o sedimento, depois de "
            "seco, vira o pó fino. Daí o nome: tipi'óka, na língua tupi falada no Nordeste quando os portugueses "
            "chegaram, se traduz como \"sedimento\" ou \"coágulo\". Brasil, Tailândia e Nigéria são os maiores "
            "produtores de mandioca, e em 2010 a Tailândia respondia por cerca de 60% das exportações mundiais. "
            "Na indústria, o amido úmido passa sob pressão por uma peneira e vira pérolas. Na Ásia, elas se "
            "chamam boba e vão no bubble tea, dando à bebida doce seu contraste borrachudo. No Brasil, as mesmas "
            "pérolas viram sagu, que no Sul é cozido em vinho tinto com canela e cravo."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Tapioca",
            "Tapioca (; Portuguese: [tapiˈɔkɐ]) is a starch extracted from the tubers of the cassava plant (Manihot esculenta, also known as manioc), a species native to the North and Northeast regions of Brazil, but which is now found in West Africa, Southeast Asia, and elsewhere. [...] "
            "The word \"tapioca\" is derived from tipi'óka, its name in the Tupi language spoken by natives when the Portuguese first arrived in the Northeast Region of Brazil around 1500. "
            "This Tupi word is translated as \"sediment\" or \"coagulant\" and refers to the curd-like starch sediment that is obtained in the extraction process. [...] "
            "In Brazil's north and northeast, traditional community-based tapioca production is a byproduct of manioc flour production from cassava roots. [...] "
            "The wet masa is placed in a long, woven tube called a tipiti. [...] "
            "squeezing a starch-rich liquid out through the weave and ends. "
            "This liquid is collected, and the microscopic starch grains in it are allowed to settle into the bottom of the container. "
            "The supernatant liquid is then poured off, leaving behind a wet starch sediment that needs to be dried and results in the fine-grained tapioca starch powder similar in appearance to corn starch. [...] "
            "Brazil, Thailand, and Nigeria are the world's largest cassava producers. "
            "In 2010, Thailand accounted for about 60% of worldwide exports. [...] "
            "Tapioca pearls, also known as boba in East Asia, are produced by passing the moist starch through a sieve under pressure. "
            "Pearl tapioca is a common ingredient in Asian desserts such as falooda, kolak, sago soup, and in sweet drinks such as bubble tea, fruit slush and taho, where they provide a chewy contrast to the sweetness and smooth texture of the drink. [...] "
            "In Brazil, the pearls are cooked with wine or other liquid to add flavor and are called sagu. [...] "
            "A regional dessert called sagu is also made in Southern Brazil from tapioca pearls traditionally cooked with cinnamon and cloves in red wine [...] "
            "In various Asian countries, tapioca pearls are widely used in desserts and drinks including Taiwanese bubble tea.",
            nome="Tapioca")],
    },
    # 13 erva-mate: o segredo perdido dos jesuítas
    {
        "temas_secundarios": ["domesticacao", "brasil_colonial", "povos_indigenas"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "No século XVII, os jesuítas conseguiram domesticar a erva-mate. Com a expulsão deles, nos anos 1770, as plantações decaíram e o segredo se perdeu: a planta só foi domesticada de novo na virada do século XIX para o XX.",
        "explicacao": (
            "Antes dos europeus, a erva-mate era cultivada e consumida pelos guaranis e por alguns povos tupis, "
            "numa região que hoje é o Paraguai. No guarani, a planta se chama ka'a, que quer dizer simplesmente "
            "\"erva\". No fim do século XVI, o hábito se espalhou entre colonos espanhóis e indígenas, e a erva "
            "virou a principal mercadoria do Paraguai, colhida em árvores silvestres com trabalho indígena. Em "
            "meados do século XVII, os jesuítas conseguiram domesticar a planta e montar plantações nas suas "
            "reduções de Misiones, hoje na Argentina, em forte concorrência com os coletores de erva nativa. Com "
            "a expulsão da ordem, nos anos 1770, as plantações entraram em decadência, e os segredos da "
            "domesticação se foram com elas. A planta só voltou a ser domesticada em projetos brasileiros e "
            "argentinos do fim do século XIX e começo do XX, que abriram caminho para as grandes plantações. Hoje "
            "o Brasil é o maior produtor, com 53%, seguido da Argentina, com 37%, e do Paraguai, com 10%. E o "
            "jeito mais antigo de tomar mate talvez seja frio: os guaranis já bebiam a erva assim, só que sem "
            "gelo, e por isso o tereré é tido como a forma original."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Yerba_mate",
            "The indigenous Guaraní and some Tupi communities (whose territory covered modern Paraguay) first cultivated and consumed yerba mate prior to European colonization of the Americas. [...] "
            "The name given to the plant in the Guaraní language (of the indigenous people who first used mate) is kaʼa, which has the same meaning as 'herb'. [...] "
            "Its consumption became widespread during European colonization, particularly in the Spanish colony of Paraguay in the late 16th century, among both Spanish settlers and indigenous Guaraní, who had, to some extent before the Spanish arrival, consumed it. "
            "This widespread consumption turned it into Paraguay's main commodity above other wares, such as tobacco, and the labour of indigenous peoples was used to harvest wild stands. "
            "In the mid-17th century, Jesuits managed to domesticate the plant and establish plantations in their Indian reductions in Misiones, Argentina, sparking severe competition with the Paraguayan harvesters of wild stands. [...] "
            "After their expulsion in the 1770s, their plantations fell into decay, as did their domestication secrets. [...] "
            "In Brazilian and Argentine projects in the late 19th and early 20th centuries, the plant was domesticated once again, opening the way for plantation systems. [...] "
            "Today, Brazil is the largest producer, with 53%, followed by Argentina, 37%, and Paraguay, 10%. [...] "
            "The Guarani drank it in this format, but without ice, as they lacked the technology to create or store it. "
            "Thus, tereré is accredited to be the first and original way of consuming mate.",
            nome="Yerba mate")],
    },
    # 14 pequi: polinizado por morcegos, armado de espinhos
    {
        "temas_secundarios": ["biomas_brasileiros", "plantas", "alimentos_perigosos"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "O pequi, fruto do Cerrado, é polinizado sobretudo por morcegos. E sob a polpa amarela há um caroço coberto de espinhos finos: quem morde com força pode ficar com eles presos na boca.",
        "explicacao": (
            "O pequizeiro, Caryocar brasiliense, é uma árvore de até 10 metros comum no Cerrado do Brasil "
            "central. Ao contrário da maioria das árvores do bioma, floresce no inverno seco, mais ou menos de "
            "julho a setembro. As flores abrem à tardinha e produzem néctar ralo e farto a noite toda, sem cheiro "
            "agradável, como é comum nas plantas polinizadas por morcegos, que são seus principais "
            "polinizadores. Beija-flores e pequenos pássaros também visitam as flores, mas não se sabe se ajudam "
            "a polinizar. O fruto leva de 5 a 6 meses para amadurecer e fica do tamanho de uma laranja. Dentro, "
            "costuma ter de 1 a 4 gomos de polpa amarela, de cheiro forte, que mistura notas doces, frutadas e de "
            "queijo, vindas sobretudo de ésteres. Sob a polpa, a semente fica numa casca escura coberta de "
            "espinhos lenhosos, finos e resistentes. Por isso, o pequi cru deve ser raspado com os dentes, com "
            "delicadeza: os espinhos se soltam, ferem a boca, doem muito e são difíceis de tirar. A polpa ainda "
            "escurece talheres de prata. Pequi com arroz e frango é um dos pratos mais populares de Goiás, Mato "
            "Grosso, Mato Grosso do Sul e Minas Gerais."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Caryocar_brasiliense",
            "The pequi tree grows up to 10 m (30 ft) tall. "
            "It is common in the central Brazilian cerrado habitat from southern Pará to Paraná and northern Paraguay. [...] "
            "Unlike most other cerrado trees, it bears flowers in the dry winter months, approximately July to September. [...] "
            "Pollination is mainly by bats and, as usual in such cases, the flowers do not have a pleasant smell but produce copious thin nectar. "
            "Flowers open in the evening and produce nectar throughout the night, ceasing in the early morning. [...] "
            "From dusk to the cessation of nectar production, hummingbirds may visit the flowers. [...] "
            "it is not clear whether birds, particularly tanagers, play a role in pollination or are merely making use of an easy early-morning snack [...] "
            "Fruits start off dark purple, turning olive green and finally buff green as they ripen, taking about 5–6 months. "
            "Ripe fruits are about the size of an orange. "
            "They resemble a mangosteen (another distantly related member of the Malpighiales) in having a few (usually 1–4) segments of pulpy pericarp inside the skin, yellow and with a typical strong taste and smell mixing sweet, fruity and cheesy aromas. "
            "This is derived mainly from volatile ethyl esters. "
            "Embedded in the mesocarp is a light-colored seed enclosed in a blackish shell covered with thin and tough woody spines, though spineless individuals exist in the wild. [...] "
            "Pequi pulp is a very popular food in Goiás, Mato Grosso, Mato Grosso do Sul and Minas Gerais, eaten by itself raw or prepared or used as an ingredient in cooking or to flavor beverages. "
            "Pequi with rice and chicken is an especially popular preparation. "
            "Pequi pulp will tarnish silver cutlery and, if eaten raw, the fruit is best enjoyed out of hand. "
            "Care must be taken to gently scrape the pulp off the pit using one's teeth: The spines can detach and hurt the mouth, causing considerable pain and being difficult to remove.",
            nome="Caryocar brasiliense")],
    },
    # 15 abacaxi: fruta sul-americana de nome tupi
    {
        "temas_secundarios": ["grandes_navegacoes", "palavras_viajantes", "domesticacao"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "O abacaxi é sul-americano: a planta silvestre vem das bacias dos rios Paraná e Paraguai. Povos tupi-guaranis o chamavam de nanas, nome que deu o científico Ananas, e os portugueses o levaram do Brasil à Índia.",
        "explicacao": (
            "A planta silvestre surgiu nas bacias dos rios Paraná e Paraguai, entre o sul do Brasil e o "
            "Paraguai. Pouco se sabe de como foi domesticada, mas o cultivo se espalhou pela América do Sul: há "
            "indícios arqueológicos de uso no Peru entre 1200 e 800 a.C., e no México os maias e astecas também o "
            "cultivavam. No fim do século XV, o abacaxi plantado já era alimento básico de povos nativos das "
            "Américas Central e do Sul. Os tupi-guaranis e os caribes o chamavam de nanas, nome adotado em muitas "
            "línguas europeias e que deu o científico Ananas comosus. O primeiro europeu a encontrar a fruta foi "
            "Cristóvão Colombo, na ilha de Guadalupe, em 4 de novembro de 1493; ele a levou para a Espanha com o "
            "nome de \"pinha das Índias\". A primeira referência em inglês, de 1568, é a tradução de um livro do "
            "francês André Thevet, que descrevia uma fruta cultivada e comida pelos tupinambás, perto do atual Rio "
            "de Janeiro. Os portugueses levaram a fruta do Brasil e a introduziram na Índia até 1550."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Pineapple",
            "The first reference in English to the pineapple fruit was the 1568 translation from the French of André Thevet's The New Found World, or Antarctike where he refers to a Hoyriri, a fruit cultivated and eaten by the Tupinambá people, living near modern Rio de Janeiro, and now believed to be a pineapple. [...] "
            "When it was first discovered by explorers, the Tupi-Guarani and Carib people used it as a staple food with the name, nanas. "
            "This usage was adopted in many European languages and led to the plant's scientific binomial Ananas comosus [...] "
            "The wild plant originates from the Paraná–Paraguay River drainages between southern Brazil and Paraguay. "
            "Little is known about its domestication, but it spread as a crop throughout South America. "
            "Archaeological evidence of use is found as far back as 1200–800 BC (3200–2800 BP) in Peru and 200 BC – 700 AD (2200–1300 BP) in Mexico, where it was cultivated by the Mayas and the Aztecs. "
            "By the late 1400s, cropped pineapple was widely distributed and a staple food of Native Central and South Americans. "
            "The first European to encounter the pineapple was Christopher Columbus, in Guadeloupe on 4 November 1493. "
            "The Portuguese took the fruit from Brazil and introduced it into India by 1550. [...] "
            "Columbus brought the plant back to Spain and called it piña de Indes, meaning \"pine of the Indians\".",
            nome="Pineapple")],
    },
]
