LOTE = "2026-11-19-cafe_cha_cacau-01"
AREA = "comida"
TEMA = "cafe_cha_cacau"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o cacau foi domesticado na Amazônia, não na Mesoamérica
    {
        "temas_secundarios": ["americas_pre_colombianas", "domesticacao", "amazonia"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "O chocolate lembra maias e astecas, mas o cacau foi domesticado antes na Amazônia do atual Equador, há pelo menos 5.300 anos. Só depois a árvore chegou à Mesoamérica.",
        "explicacao": (
            "O cacaueiro é nativo da floresta amazônica e ainda cresce em estado selvagem no sopé dos Andes e na "
            "bacia do Orinoco, em países como Colômbia e Venezuela. Pelos indícios reunidos até 2018, a "
            "domesticação aconteceu primeiro na América do Sul equatorial, uns 1.500 anos antes de acontecer na "
            "América Central. A pista principal vem do sítio arqueológico de Santa Ana-La Florida, no sudeste do "
            "Equador, onde vivia a cultura Mayo-Chinchipe. Em resíduos deixados em cerâmicas, pesquisadores "
            "encontraram grãos de amido próprios do cacaueiro, restos de teobromina, substância abundante no cacau, "
            "e fragmentos de DNA antigo com sequências que só a planta tem. Dali a árvore se espalhou pela costa do "
            "Pacífico e depois chegou à Mesoamérica, onde a bebida de cacau ganhou prestígio de bebida da elite "
            "entre maias e astecas. Há um detalhe a mais: há indícios de que o que primeiro chamou a atenção para a "
            "planta nas Américas não foi o sabor da semente, mas a polpa doce do fruto, usada numa bebida fermentada "
            "com 5,34% de álcool."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Cocoa_bean",
                "It was first domesticated at least 5,300 years ago, in equatorial South America at the Santa Ana-La Florida (SALF) site in what is present-day southeast Ecuador (Zamora-Chinchipe Province) by the Mayo-Chinchipe culture, before being introduced into Mesoamerica. [...] "
                "It also grows in the foothills of the Andes in the Amazon region and the Orinoco basins of South America, such as in Colombia and Venezuela. Wild cacao still grows there. [...] "
                "As of 2018, evidence suggests that cacao was first domesticated in equatorial South America, before being domesticated in Central America roughly 1,500 years later. [...] "
                "Evidence also indicates that, long before the flavor of the cacao seed (or bean) became popular, the sweet pulp of the chocolate fruit, used in making a fermented (5.34% alcohol) beverage, first drew attention to the plant in the Americas.",
                nome="Cocoa bean"),
            wiki("History_of_chocolate",
                "The cacao tree is native to the Amazon rainforest. Evidence of cacao domestication exists as early as circa 3300 BC in present-day southeast Ecuador by the Mayo-Chinchipe culture, before it was introduced to Mesoamerica. "
                "This emerged from research into residue in ceramics, which revealed starch grains specific to the cacao tree, residue of theobromine (a compound found in high levels in cacao), and fragments of ancient DNA with sequences unique to the cacao tree. "
                "The domesticated cacao tree was then spread along the Pacific coast of South America. [...] "
                "where cacao drinks gained significance as an elite beverage among cultures including the Maya and the Aztecs.",
                nome="History of chocolate"),
        ],
    },
    # 2 sementes de cacau como dinheiro, e falsificadas
    {
        "temas_secundarios": ["dinheiro", "americas_pre_colombianas"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Na Mesoamérica, sementes de cacau eram dinheiro: em 1545, 30 compravam um coelho pequeno e 100, uma perua. Por isso eram falsificadas com massa de amaranto, cera ou pedaços de caroço de abacate.",
        "explicacao": (
            "Antes da conquista espanhola, o cacau circulava como moeda por toda a Mesoamérica. Os conquistadores "
            "registraram o valor das sementes: um relato de 1545 diz que uma semente comprava um tomate grande, "
            "trinta compravam um coelho pequeno e cem, uma perua. Com quantidades menores se pagavam coisas "
            "pequenas, como tamales. Os astecas exigiam dos povos conquistados tributo em cacau, e na época da "
            "conquista havia 1,5 milhão de árvores cultivadas na região do Soconusco. Os pochteca, mercadores que "
            "transportavam o cacau pelo território asteca, carregavam nas costas 24 mil sementes de uma vez, de 23 a "
            "27 kg. Como todo dinheiro valioso, o cacau tinha falsários: as sementes eram imitadas com massa de "
            "amaranto, cera ou pedaços de caroço de abacate. Um último detalhe desfaz uma imagem comum: hoje se "
            "costuma imaginar o chocolate asteca com canela, mas essa especiaria só chegou à Mesoamérica com os "
            "espanhóis."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("History_of_chocolate",
                "The Aztecs required the conquered inhabitants to pay tribute in cacao. At the time of the Spanish conquest, 1.5 million trees were tended in Soconusco. Cacao was transported across Aztec territory by pochteca, carrying 24,000 beans weighing [...] (23 [...] 27 kg) on their backs. [...] "
                "Today, Aztec chocolate drinks are commonly understood to contain cinnamon, despite the spice only being introduced to Mesoamerica by the Spanish conquest. [...] "
                "The Spanish conquistadors recorded the currency value of the cocoa beans, noting in 1545 that thirty beans could buy a small rabbit, one bean could buy a large tomato, and a hundred beans could purchase a turkey hen. "
                "Royal stores were claimed to hold massive amounts of cocoa beans. Cocoa beans were often counterfeited, with substitutes including dough made of amaranth, wax or broken avocado pits.",
                nome="History of chocolate"),
            wiki("Cocoa_bean",
                "The cocoa bean was a common currency throughout Mesoamerica before the Spanish conquest.The bean was utilized in pre-modern Latin America to purchase small items such as tamales and rabbit dinners. A greater quantity of cocoa beans was used to purchase turkey hens and other large items.",
                nome="Cocoa bean"),
        ],
    },
    # 3 os seis cristais da manteiga de cacau
    {
        "temas_secundarios": ["estados_materia", "ciencia_cozinha", "quimica_cotidiano"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "A manteiga de cacau pode cristalizar de seis jeitos diferentes, e só um, a forma V, dá ao chocolate brilho e aquele estalo ao partir. As manchas brancas no chocolate que derreteu são gordura cristalizada do jeito errado.",
        "explicacao": (
            "A manteiga de cacau derrete por volta de 34 a 38 °C. Por isso o chocolate fica sólido na temperatura "
            "ambiente e derrete na boca. Mas ela é polimórfica: tem seis formas cristalinas, numeradas de I a VI, "
            "cada uma com seu ponto de fusão, de 17,3 °C na forma I a 36,3 °C na VI. A indústria busca a forma V, "
            "que funde a 33,8 °C e é a mais estável que se consegue a partir da manteiga derretida; a VI só aparece "
            "depois de muito tempo guardada ou cristalizada em solventes. Uma estrutura uniforme na forma V deixa o "
            "chocolate liso, brilhante e quebradiço. Para chegar a ela existe a temperagem, técnica desenvolvida no "
            "século XX, que elimina os cristais indesejados e favorece a forma V. Quando uma barra derrete num lugar "
            "quente e endurece de novo sem esse controle, surgem formas instáveis e manchas esbranquiçadas na "
            "superfície, o chamado fat bloom. O chocolate continua seguro e com o mesmo sabor, e basta temperá-lo "
            "de novo. A origem também pesa: a manteiga de cacau brasileira cristaliza devagar e dá um chocolate mais "
            "macio que a da Malásia e da Indonésia."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Cocoa_butter",
                "Cocoa butter typically has a melting point of around 34 [...] 38 °C (93 [...] so chocolate is solid at room temperature but readily melts once inside the mouth. "
                "Cocoa butter displays polymorphism, having different crystalline forms with different melting points. "
                "Conventionally the assignment of cocoa butter crystalline forms uses the nomenclature of Wille and Lutton with forms I, II, III, IV, V, and VI having melting points 17.3, 23.3, 25.5, 27.5, 33.8, and 36.3 °C [...] "
                "The production of chocolate aims to crystallize the chocolate so that the cocoa butter is predominantly in form V, which is the most stable form that can be obtained from melted cocoa butter. "
                "(Form VI either develops in solid cocoa butter after long storage or is obtained by crystallization from solvents). "
                "A uniform form V crystal structure will result in smooth texture, sheen, and snap. This structure is obtained by chocolate tempering. "
                "Melting the cocoa butter in chocolate and then allowing it to solidify without tempering leads to the formation of unstable polymorphic forms of cocoa butter. "
                "This can easily happen when chocolate bars are allowed to melt in a hot room and lead to the formation of white patches on the surface of the chocolate called fat bloom or chocolate bloom. [...] "
                "Malaysian and Indonesian cocoa butter generally crystallize faster, and into a harder chocolate than Brazilian cocoa butter. Brazilian cocoa butter, after slowly crystallizing, forms a softer chocolate.",
                nome="Cocoa butter"),
            wiki("Chocolate",
                "In the 20th century, chocolate production further developed, with development of the tempering technique to improve the snap and gloss of chocolate [...] "
                "Cocoa butter is a polymorphic fat with six different crystal forms, but only one of them [...] Form V [...] gives chocolate its characteristic snap, gloss, and stable texture. "
                "Tempering eliminates the undesirable crystal forms and promotes the formation of Form V. [...] "
                "Although visually unappealing, chocolate suffering from bloom is safe for consumption and taste is unaffected. Bloom can be reversed by retempering the chocolate",
                nome="Chocolate"),
        ],
    },
    # 4 a ração D: chocolate feito para não ser gostoso
    {
        "temas_secundarios": ["segunda_guerra", "ciencia_cozinha"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Em 1937, o Exército dos EUA encomendou à Hershey uma barra de chocolate de emergência com gosto só \"um pouco melhor que batata cozida\", para os soldados não a comerem antes da hora. Os soldados a detestaram.",
        "explicacao": (
            "Quem fez a encomenda foi o coronel Paul Logan, do serviço de intendência do Exército. A barra, chamada "
            "ração D, tinha quatro exigências: pesar 113 gramas, ter muita energia, resistir ao calor e ter um "
            "sabor só um pouco melhor que o de batata cozida, para que ninguém a comesse fora de uma emergência. A "
            "receita levava chocolate, açúcar, aveia, gordura de cacau e leite em pó desnatado, com vitamina B1 "
            "contra o beribéri. A mistura resistente ao calor virava uma pasta grudenta que não escorria em "
            "temperatura nenhuma, e cada porção precisou ser amassada, pesada e prensada no molde à mão. O "
            "resultado era um bloco duríssimo, que aguentava até 49 °C; três barras davam as 1.800 calorias "
            "mínimas de um dia. Durante a guerra, a maior parte do chocolate da Hershey foi para os militares: "
            "estima-se que 3 bilhões de unidades de barras especiais tenham sido distribuídas entre 1940 e 1945. "
            "O objetivo foi alcançado com folga. A ração D era quase universalmente detestada pelo gosto amargo, "
            "muitas vezes ia para o lixo, e quem tinha dentes ruins não conseguia comê-la. Os soldados a apelidaram "
            "de \"arma secreta de Hitler\", pelo efeito no intestino."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("D_ration",
            "Army Quartermaster Colonel Paul Logan approached Hershey's Chocolate in April 1937 [...] "
            "Colonel Logan had four requirements for the D ration bar, dictating that it had to: "
            "Weigh 4 ounces (113 grams) Be high in food energy value Be able to withstand high temperatures Taste \"a little better than a boiled potato\" (to keep soldiers from eating their emergency rations in non-emergency situations) "
            "Its ingredients were chocolate, sugar, oatmeal, cacao fat, skim milk powder, and artificial flavoring, fortified with vitamin B1 to prevent beriberi. [...] "
            "However, it was found that the temperature-resistant formula became a gooey paste that would not flow at any temperature. [...] "
            "Each four-ounce portion had to be kneaded, weighed, and pressed into a mold by hand. "
            "The end result was an extremely hard block of dark brown chocolate that would crumble with some effort and was heat-resistant to 120 °F (49 °C). [...] "
            "Three bars made up a daily ration and was intended to furnish the individual combat soldier with the 1,800 calories [...] "
            "During the war years, the bulk of the Hershey Food Corporation's chocolate production was for the military. "
            "Between 1940 and 1945, an estimated three billion units of the specially formulated candy bars were distributed to soldiers around the world. [...] "
            "The D ration was almost universally detested for its bitter taste by US troops, and was often discarded instead of consumed when issued. "
            "Troops called the D ration \"Hitler's Secret Weapon\" for its effect on soldiers' intestinal tracts. "
            "It could not be eaten at all by soldiers with poor dentition",
            nome="Military chocolate (United States)")],
    },
    # 5 chocolate quebra o jejum? um século de debate na Igreja
    {
        "temas_secundarios": ["religioes", "costumes_rituais"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Chocolate quebra o jejum? A Igreja Católica discutiu isso por cerca de cem anos, com tratados inteiros sobre o assunto. Segundo um relato, um papa consultado caiu na gargalhada: nunca tinha visto chocolate.",
        "explicacao": (
            "O problema começou com os primeiros espanhóis na América, que ligaram a bebida de cacau aos rituais "
            "astecas. Depois veio a dúvida sobre o jejum. Pelas regras medievais, o chocolate deveria escapar da "
            "proibição: era tomado como líquido e era de origem vegetal, não carne. Mas muitas vezes levava ovos ou "
            "leite e era claramente um luxo, o que contrariava o espírito do jejum. Os dominicanos lideraram a "
            "campanha para limitar o consumo e, em 1577, mandaram um representante a Roma consultar o papa Gregório "
            "XIII. Segundo um relato, ele riu do pedido, já que nunca tinha visto nem provado chocolate. Seguiram-se "
            "livros a favor e contra, como um tratado de 1636 com a pergunta no título: o chocolate quebra o jejum "
            "eclesiástico? Os jesuítas, que tinham interesses comerciais no cacau, conseguiram em 1664 um parecer "
            "favorável do cardeal Francesco Maria Brancaccio e o reimprimiram pelo menos quatro vezes. Na prática, o "
            "chocolate ficou tão popular que a Igreja pouco pôde fazer. Em 1692, carmelitas de Madri pediram ao "
            "papa Inocêncio XII licença para tomá-lo dentro do convento e ouviram um não, e pelo menos três papas do "
            "século XVIII eram apreciadores da bebida."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://historytoday.com/node/56318", "titulo": "The Theology of Chocolate (History Today)", "idioma": "en",
             "trecho": "Part of the issue was that the original Spaniards who travelled to the Americas quickly associated the drinking of chocolate with Aztec religious rituals. [...] "
                       "It was consumed as a liquid, which meant it did not violate a prohibition against eating only one full and two small meals a day, and was vegetal not animal in nature, so it did not violate another against eating meat. "
                       "Yet chocolate was often prepared with eggs or milk, which were animal products and therefore made certain preparations of it dubiously acceptable at best. "
                       "It was, moreover, clearly a luxury product and consuming luxuries, if not against the letter of the fast [...] "
                       "Debate simmered in the Catholic Church for 100 years. "
                       "The Dominicans, in particular, were at the forefront of a campaign to limit its consumption, even sending a representative to Rome in 1577 to seek Pope Gregory XIII [...] "
                       "In 1636 an Inquisition lawyer, Antonio de Le [...] "
                       "the Jesuits, who by this time had commercial interests in cacao production and distribution, took the case back to Rome. "
                       "They secured a favourable ruling from no less an eminence than the theologian Cardinal Francesco Maria Brancaccio, who put his name to a 16-page opinion De Chocolatis potu (On the use of chocolate, 1664) [...] "
                       "The Jesuits published this immediately, reprinting it at least four times in the next decade. "
                       "In the event, these arguments all proved academic because chocolate consumption became so popular that the Church could do little to shape the behaviour of its faithful in the matter. "
                       "In 1692 Pope Innocent XII even received a request from Carmelites in Madrid for a dispensation to drink chocolate inside the walls of their convent. [...] "
                       "at least three 18th-century popes, Benedict XIII, Clement XII, and Benedict XIV, had been keen chocolate drinkers. [...] "
                       "one account suggests that he burst out laughing at the absurdity of the request. He had neither seen nor tasted chocolate"},
            wiki("History_of_chocolate",
                "From the late-16th century until the early 18th century, there was controversy about whether chocolate was both a food and a drink or just a drink; this distinction was important for determining if consumption violated ecclesiastical fasts.",
                nome="History of chocolate"),
        ],
    },
    # 6 o arábica é filho do robusta
    {
        "temas_secundarios": ["genetica", "evolucao", "plantas"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "O café arábica, o mais plantado do mundo, é um híbrido natural: nasceu do cruzamento de duas espécies de café, e uma delas é justamente a do robusta, o café considerado \"inferior\".",
        "explicacao": (
            "O arábica responde por cerca de 60% da produção mundial, e quase todo o resto é robusta, da espécie "
            "Coffea canephora, menos ácido, mais amargo e com mais cafeína. A genética mostra que os dois são "
            "parentes muito próximos. A maioria das espécies de café é diploide, com duas cópias de cada um dos 11 "
            "cromossomos. O arábica tem quatro cópias, 44 cromossomos ao todo, porque é o resultado do cruzamento "
            "entre duas espécies diploides, Coffea canephora e Coffea eugenioides. Ficou com dois genomas "
            "diferentes, cada um em dose dupla, o que os botânicos chamam de alotetraploide. Esse cruzamento "
            "aconteceu na natureza, numa data estimada entre 1,08 milhão e 543 mil anos atrás, ligada a mudanças "
            "ambientais no leste da África, muito antes de qualquer pessoa tomar café. As populações selvagens do "
            "arábica hoje se limitam a florestas do sul da Etiópia, do Sudão do Sul e do Iêmen, e acredita-se que "
            "ele tenha sido a primeira espécie de café cultivada."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Coffea_arabica",
            "It is believed to be the first species of coffee to have been cultivated and is the dominant cultivar, representing about 60% of global production. "
            "Coffee produced from the less acidic, more bitter, and more highly caffeinated robusta bean (C. canephora) makes up most of the remaining coffee production. "
            "The natural populations of Coffea arabica are restricted to the forests of South Ethiopia, South Sudan, and Yemen. [...] "
            "Coffea arabica is one of the polyploid species of the genus Coffea, as it carries four copies of the eleven chromosomes (44 total) instead of the 2 copies of diploid species. "
            "Specifically, Coffea arabica is itself the result of a hybridization between the diploids Coffea canephora and Coffea eugenioides, thus making it an allotetraploid, with two copies of two different genomes. "
            "This hybridization event at the origin of Coffea arabica is estimated between 1.08 million and 543,000 years ago and is linked to changing environmental conditions in East Africa.",
            nome="Coffea arabica")],
    },
    # 7 a cafeína foi inventada mais de uma vez
    {
        "temas_secundarios": ["evolucao", "genetica", "plantas"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "Café, chá e cacau fazem cafeína, mas provavelmente não herdaram isso de um ancestral comum. O genoma do café, publicado em 2014, indica que cada uma dessas plantas desenvolveu suas enzimas por conta própria.",
        "explicacao": (
            "Uma equipe internacional sequenciou o genoma do Coffea canephora, a espécie do café robusta, que "
            "responde por cerca de 30% da produção mundial, e o comparou com o de outras plantas. O café tem uma "
            "coleção ampliada de N-metiltransferases, enzimas que participam da fabricação da cafeína. O detalhe "
            "revelador: essas enzimas do café são mais aparentadas com outros genes do próprio café do que com as "
            "enzimas que fazem cafeína no chá e no cacau. Se a capacidade tivesse vindo de um ancestral comum, as "
            "enzimas seriam mais parecidas entre as espécies. A conclusão é que a produção de cafeína provavelmente "
            "surgiu de forma independente nas três plantas, um caso de evolução convergente, em que linhagens "
            "diferentes chegam à mesma solução. Cerca de trinta espécies de plantas têm cafeína, entre elas a "
            "erva-mate, o guaraná e a noz-de-cola. O motivo de tanta insistência da natureza ainda é discutido: a "
            "hipótese é que a substância ajude a afastar insetos ou a atrapalhar o crescimento de plantas "
            "concorrentes."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [
            {"url": "https://www.buffalo.edu/news/releases/2014/09/005.html", "titulo": "Coffee genome sheds light on the evolution of caffeine (University at Buffalo)", "idioma": "en",
             "trecho": "Release Date: September 4, 2014 [...] Enzymes that help produce caffeine evolved independently in coffee, tea and chocolate, say scientists who have newly sequenced the coffee plant genome [...] "
                       "By comparing genes in the coffee, tea and chocolate plants, the scientists show that enzymes involved in making caffeine likely evolved independently in these three organisms. [...] "
                       "The research appears in the journal Science on Sept. 5. [...] "
                       "The team created a high-quality draft of the genome of Coffea canephora, which accounts for about 30 percent of the world [...] "
                       "Coffee also has an expanded collection of N-methyltransferases, enzymes that are involved in making caffeine. "
                       "Upon taking a closer look, the researchers found that coffee [...] caffeine enzymes are more closely related to other genes within the coffee plant than to caffeine enzymes in tea and chocolate. "
                       "This finding suggests that caffeine production developed independently in coffee. If this trait had been inherited from a common ancestor, the enzymes would have been more similar between species. [...] "
                       "Scientists theorize that the chemical may help plants repel insects or stunt competitors [...] growth."},
            wiki("Caffeine",
                "Around thirty plant species are known to contain caffeine. [...] "
                "Other sources include the leaves of yaupon holly, South American holly yerba mate, and Amazonian holly guayusa; and seeds from Amazonian maple guarana berries. [...] "
                "The biosynthesis of caffeine is an example of convergent evolution among different species.",
                nome="Caffeine"),
        ],
    },
    # 8 o chá do Ceilão nasceu de um fungo do café
    {
        "temas_secundarios": ["fungos", "imperios_coloniais", "brasil_republica"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "O chá do Ceilão existe por causa de um fungo. A ferrugem do café arrasou as fazendas da ilha, hoje Sri Lanka, a partir de 1867, e os produtores trocaram o café pelo chá. Em 1970, o fungo chegou ao Brasil.",
        "explicacao": (
            "O fungo é a Hemileia vastatrix, causadora da ferrugem-do-cafeeiro. Ela foi registrada no Ceilão, nome "
            "colonial do Sri Lanka, em 1867, e descrita em 1869 por dois micologistas ingleses, a partir de amostras "
            "enviadas da ilha. O nome vastatrix se refere justamente ao poder devastador da doença, e os fazendeiros "
            "a apelidaram de \"Devastating Emily\". Dados da época indicam que a produção de café da ilha caiu 75%, "
            "e a área plantada encolheu 80%, de 68.787 para 14.170 hectares. Muitas fazendas quebraram ou passaram "
            "para culturas que o fungo não atacava, como o chá, e por volta de 1890 a indústria cafeeira local "
            "estava quase destruída. Historiadores sugerem que esse colapso é uma das razões da preferência dos "
            "britânicos pelo chá. A ferrugem afetou o café da Ásia por mais de vinte anos e depois se espalhou pela "
            "África. Chegou ao Brasil em 1970 e, em 1975, já estava em todas as áreas de café do país, de onde "
            "seguiu para a maior parte da América Central e do Sul."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Hemileia_vastatrix",
            "Rust was first reported in the major coffee growing regions of Sri Lanka (then called Ceylon) in 1867. [...] "
            "Berkeley and Broome named the fungus Hemileia vastatrix, \"Hemileia\" referring to the half smooth characteristic of the spores and \"vastatrix\" for the devastating nature of the disease. [...] "
            "Some early data from Ceylon documenting the losses in the late 19th century indicate coffee production was reduced by 75%. "
            "As farmers shifted from coffee to other crops not affected by CLR, land used for growing coffee was reduced by 80%, from 68,787 to 14,170 ha. [...] "
            "The disease coffee leaf rust (CLR) was first described and named by Berkley and Broom in the November 1869 edition of the Gardeners Chronicle. "
            "They used specimens sent from Sri Lanka, where the disease was already causing enormous damage to productivity. "
            "Many coffee estates in Sri Lanka were forced to collapse or convert their crops to alternatives not affected by CLR, such as tea. "
            "The planters nicknamed the disease \"Devastating Emily\" and it affected Asian coffee production for over twenty years. "
            "By 1890, the coffee industry in Sri Lanka was nearly destroyed, although coffee estates still exist in some areas. "
            "Historians suggest that the devastated coffee production in Sri Lanka is one of the reasons why Britons have come to prefer tea, as Sri Lanka switched to tea production as a consequence of the disease. [...] "
            "It reached Brazil in 1970 and from there it rapidly spread at a rate enabling it to infect all coffee areas in the country by 1975. "
            "From Brazil, the disease spread to most coffee-growing areas in Central and South America",
            nome="Hemileia vastatrix")],
    },
    # 9 Robert Fortune, o espião do chá que quase fracassou
    {
        "temas_secundarios": ["espionagem", "imperios_coloniais", "comercio_rotas"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1848, um botânico escocês, às vezes disfarçado de mercador chinês, levou mudas de chá da China para a Índia britânica. Quase todas morreram, e o chá forte que os ingleses queriam vinha de uma planta local, de Assam.",
        "explicacao": (
            "Robert Fortune trabalhou na China entre 1843 e 1861, primeiro para a Sociedade de Horticultura de "
            "Londres e depois a serviço da Companhia Britânica das Índias Orientais. Como outros viajantes europeus "
            "da época, ele se disfarçou de mercador chinês em várias de suas jornadas para além dos portos abertos "
            "aos estrangeiros. Segundo relatos, a compra das mudas era proibida pelo governo chinês, e ele ainda "
            "viajava mais longe do que os europeus podiam ir a partir desses portos. Para manter as plantas vivas "
            "na viagem, usou as caixas de vidro de Ward, pequenas estufas portáteis, e teria levado também "
            "trabalhadores chineses experientes no preparo do chá. Não foi o primeiro a tentar, mas foi a "
            "introdução de chá mais famosa. O resultado imediato decepcionou: fora umas poucas plantas que "
            "sobreviveram em jardins, a maioria das mudas plantadas no noroeste da Índia morreu. Além disso, os "
            "britânicos gostavam de chá forte e escuro, que saía melhor da variedade nativa de Assam, e não da que "
            "ele escolhera. O que realmente frutificou foram a técnica e o conhecimento trazidos da China, "
            "decisivos para o crescimento posterior do chá em Assam e no Sri Lanka."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Robert_Fortune",
            "Following the Treaty of Nanking in 1842, in early 1843, he was commissioned by the Horticultural Society to undertake a three-year plant collection expedition to southern China. [...] "
            "His most famous accomplishment was the successful introduction, although it was not the first by any means, of Chinese tea plants (Camellia sinensis), along with skilled tea makers, from China to India in 1848 on behalf of the British East India Company. "
            "Robert Fortune worked in China for several years in the period from 1843 to 1861. "
            "Similar to other European travellers of the period, such as Walter Medhurst, Fortune disguised himself as a Chinese merchant during several, but not all, of his journeys beyond the newly established treaty port areas. "
            "Not only was Fortune's purchase of tea plants  reportedly forbidden by the Chinese government of the time, but his travels were also beyond the allowable day's journey from the European treaty ports. [...] "
            "He is also known for his use of Nathaniel Bagshaw Ward's portable Wardian cases to sustain the plants. "
            "It is also widely reported that he took skilled workers on contract to India who would facilitate the production of tea in the plantations of the East India Company. "
            "With the exception of a few plants that survived in established Indian gardens, most of the Chinese tea plants Fortune introduced in the northwestern provinces of India perished. "
            "The other reason for the failure in India was that the British preference and fashion was for a strong dark tea brew, which was best made from the local Assam subspecies (Camellia sinensis var. assamica) and not the selection that Fortune had made in China. "
            "The technology and knowledge that was brought over from China was, however, instrumental in the later flourishing of the Indian tea industry in Assam and Sri Lanka.",
            nome="Robert Fortune")],
    },
    # 10 a lenda do pastor Kaldi é de 1671
    {
        "temas_secundarios": ["mundo_islamico_medieval", "africa_antiga"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "A história do pastor Kaldi, que teria descoberto o café ao ver suas cabras agitadas, não aparece em nenhum texto antes de 1671. E o nome Kaldi parece ter sido inventado só no século XX.",
        "explicacao": (
            "Na versão popular, Kaldi era um pastor do século IX que viu as cabras ficarem cheias de energia depois "
            "de comer frutinhas vermelhas de um arbusto. Ele levou as frutas a um mosteiro, um monge as jogou no "
            "fogo, e o aroma da torra teria rendido a primeira xícara de café. O relato mais antigo é de 1671, num "
            "dos primeiros tratados impressos sobre café, escrito em Roma por Antoine Faustus Nairon, professor "
            "maronita de línguas orientais. Ali o pastor, de camelos ou de cabras, não tem nome e vive na Arábia "
            "Feliz, o atual Iêmen. O nome Kaldi parece ter sido criado no século XX e foi difundido pelo americano "
            "William H. Ukers, autor de um livro de 1922 sobre o café. Por isso, a história é provavelmente "
            "apócrifa. O que os documentos mostram é outra coisa: em meados do século XV, monges sufis do Iêmen já "
            "preparavam a bebida para ficar acordados durante as longas orações noturnas, e um cronista do século "
            "XVI atribuiu ao mufti de Áden o primeiro uso do café, por volta de 1454."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("History_of_coffee",
                "One account involves a 9th-century Ethiopian or Arab goatherder, Kaldi, who, noticing the energizing effects when his flock nibbled on the bright red berries of a certain bush, chewed on the fruit himself. "
                "His exhilaration prompted him to bring the berries to a monk in a nearby Islamic monastery. But the monk disapproved of their use and threw them into the fire, from which an enticing aroma billowed [...] "
                "This legend does not appear before 1671, indicating the story is likely apocryphal, first being related by Antoine Faustus Nairon, a Maronite professor of Oriental languages and author of one of the first printed treatises devoted to coffee [...] "
                "(Rome, 1671), which describes a camel or goat herder in the Kingdom of Ayaman, Arabia Felix. "
                "The herder is unnamed in the earliest account and the name Kaldi appears to be a later invention in the twentieth century. [...] "
                "By the mid-15th century, Sufi monks in Yemen regularly made & drank coffee to help them stay awake during long night prayers and religious ceremonies. [...] "
                "who, in 1587, compiled a work tracing the history and legal controversies of coffee [...] "
                "He reported that one Sheikh, Jamal-al-Din al-Dhabhani (d. 1470), mufti of Aden, was the first to adopt the use of coffee (circa 1454).",
                nome="History of coffee"),
            wiki("Kaldi",
                "The herder is unnamed in the earliest account. The name Kaldi appears to be a later invention from the 20th century, propagated by William H. Ukers. [...] "
                "Ukers, William Harrison (1922). All About Coffee.",
                nome="Kaldi"),
        ],
    },
    # 11 o Lloyd's e a Bolsa de Londres nasceram em cafés
    {
        "temas_secundarios": ["economia_curiosa", "comercio_rotas", "cidades"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "O Lloyd's de Londres, famoso mercado de seguros, começou como uma casa de café do século XVII, onde marinheiros e comerciantes iam atrás de notícias de navios. A Bolsa de Londres também nasceu num café.",
        "explicacao": (
            "A casa de café de Edward Lloyd ficava na Tower Street, na City de Londres. Lloyd atraía marinheiros, "
            "mercadores e donos de navios oferecendo notícias confiáveis sobre o movimento das embarcações. O lugar "
            "virou ponto de encontro de gente do mar, que apostava em quais navios voltariam ao porto, e esse foi o "
            "começo do seguro no Lloyd's. O café também era frequentado por gente do tráfico de escravizados, e o "
            "Lloyd's segurou navios negreiros até a abolição do tráfico, em 1807. Em 1691, o pequeno grupo de "
            "seguradores se mudou para a Lombard Street, e só em 1773 os membros formaram a Society of Lloyd's. "
            "O caso não foi isolado. As casas de café inglesas cobravam às vezes um pêni de entrada e davam acesso "
            "a jornais, livros e conversa, o que lhes rendeu o apelido de \"universidades de um pêni\". Em 1675 já "
            "havia mais de 3 mil delas na Inglaterra, apesar de o rei Carlos II ter tentado suprimi-las como focos "
            "de boatos contra o governo. E em 1773 os corretores que se reuniam no New Jonathan's Coffee-house "
            "rebatizaram o lugar de \"The Stock Exchange\", a Bolsa de Valores."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Lloyd%27s_of_London",
                "The market began in Lloyd's Coffee House, owned by Edward Lloyd, on Tower Street in the City of London. [...] "
                "The establishment was a popular place for sailors, merchants, and ship-owners, and Lloyd catered to them with reliable shipping news. [...] "
                "eeting place for people of all types of maritime occupations, who would make bets on which ships would make it back to port. [...] It was the start of Lloyd's insurance. "
                "During this time, the coffee house was also frequented by mariners involved in the slave trade. [...] "
                "e slave trade and maintained it until the abolition of the slave trade in 1807. "
                "Just after Christmas 1691, the small club of marine insurance underwriters relocated to No. 16 Lombard Street [...] "
                "This arrangement carried on until 1773, long after the death of Edward Lloyd in 1713, when the participating members of the insurance arrangement formed a committee [...] "
                "for \"The Society of Lloyd's\".",
                nome="Lloyd's of London"),
            wiki("Coffeehouse",
                "By 1675, there were more than 3,000 coffeehouses in England [...] "
                "Entry gave access to books or print news. "
                "The rich intellectual atmosphere of early London coffeehouses was available to anyone who could pay the sometimes one penny entry fee, giving them the name \"penny universities\". "
                "Though Charles II tried to suppress coffeehouses as places where the \"Idle and disaffected persons\" met [...] "
                "Lloyd's Coffee House was where underwriters of ship insurance met to do business, leading to the establishment of Lloyd's of London insurance market and other related businesses. "
                "In 1773 the stockbrokers who had been meeting at New Jonathan's Coffee-house renamed it \"The Stock Exchange\".",
                nome="Coffeehouse"),
        ],
    },
    # 12 o experimento de Gustavo III com gêmeos
    {
        "temas_secundarios": ["historia_medicina", "leis_julgamentos"],
        "tipos_espanto": ["historia_humana", "mito_desmentido"],
        "gancho": "Conta-se que o rei Gustavo III, da Suécia, quis provar que o café fazia mal usando gêmeos condenados: um tomaria café todo dia, o outro chá. Os médicos e o rei morreram antes deles. A Suécia proibiu o café cinco vezes.",
        "explicacao": (
            "Entre 1756 e 1823, o café foi proibido por decreto real na Suécia em cinco períodos diferentes, sob "
            "três reinados. Antes disso, em 1746, um édito já atacava os \"abusos e excessos\" no consumo de chá e "
            "café, com impostos pesados e multas que incluíam o confisco de xícaras e pratos. Gustavo III via o café "
            "como ameaça à saúde pública e, segundo o relato tradicional, mandou fazer um experimento: dois gêmeos "
            "idênticos condenados à morte tiveram a pena trocada por prisão perpétua, com a condição de que um "
            "bebesse três bules de café por dia e o outro, a mesma quantidade de chá, pelo resto da vida. O gêmeo "
            "do chá teria morrido primeiro, aos 83 anos. A idade do outro na morte é desconhecida, porque os dois "
            "médicos encarregados de acompanhar o estudo morreram antes dele, e o próprio rei foi assassinado em "
            "1792. A autenticidade do episódio é questionada pelos historiadores. Já as proibições estão bem "
            "documentadas e fracassaram: o consumo continuou, e, depois que a última foi derrubada, em 1823, a "
            "Suécia virou um dos países que mais tomam café por pessoa no mundo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Gustav_III_of_Sweden%27s_coffee_experiment",
            "Gustav III of Sweden's coffee experiment was a purported twin study ordered by Gustav III to study the health effects of coffee. "
            "The authenticity of the event has been questioned. [...] "
            "In Sweden, coffee was banned by royal decree across three different reigns, in five separate periods between the 1750s and the 1820s: 1756 [...] 1817 [...] 1823. [...] "
            "In 1746, a royal edict was issued against coffee and tea due to \"the misuse and excesses of tea and coffee drinking\". "
            "Heavy taxes were levied on consumption, and failure to pay the tax on the substance resulted in fines and confiscation of cups and dishes. "
            "Later, coffee was banned completely; despite the ban, consumption continued. [...] "
            "Gustav III viewed coffee consumption as a threat to the public health and was determined to prove its negative health effects. [...] "
            "The king ordered the experiment to be conducted using a pair of identical twins. "
            "Both of the twins had been tried for the crimes they had committed and condemned to death. "
            "Their sentences were commuted to life imprisonment on the condition that one of the twins drink three pots of coffee, and the other drink the same amount of tea, every day for the rest of their lives. "
            "The tea drinking twin died first at the age of 83, long after the death of Gustav III, who was assassinated in 1792. "
            "The age of the coffee-drinking twin at his death is unknown, as both doctors assigned by the king to monitor this study predeceased him. [...] "
            "Once the ban was lifted in 1823, coffee became a dominant beverage in Sweden, which since has been one of the countries with the highest coffee consumption per capita in the world.",
            nome="Gustav III of Sweden's coffee experiment")],
    },
    # 13 o descafeinado nasceu de uma carga molhada e usava benzeno
    {
        "temas_secundarios": ["quimica_cotidiano", "invencoes"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O primeiro descafeinado comercial veio de uma carga de café encharcada por acidente com água do mar, que perdeu a cafeína e quase nada do sabor. O método patenteado em 1906 usava benzeno, hoje sabidamente cancerígeno.",
        "explicacao": (
            "A cafeína foi isolada do café pela primeira vez pelo químico alemão Friedlieb Ferdinand Runge, depois "
            "que o poeta Goethe soube de outro trabalho dele e lhe pediu uma análise dos grãos. Runge, porém, não "
            "explorou a descoberta comercialmente. Quem fez isso foi o comerciante alemão Ludwig Roselius, de "
            "Bremen. Em 1903, ele e colaboradores criaram o primeiro processo de descafeinação de sucesso "
            "comercial, depois de Roselius notar que um lote de grãos molhado por acidente com água do mar tinha "
            "perdido a maior parte da cafeína. O processo patenteado em 1906 tratava os grãos com vapor e ácidos ou "
            "bases e depois usava benzeno como solvente. O café saiu com a marca Kaffee HAG e, nos Estados Unidos, "
            "como Sanka. Métodos parecidos ainda dominam, mas o benzeno, hoje reconhecido como cancerígeno, foi "
            "trocado por diclorometano ou acetato de etila; também se usam CO2 supercrítico e água. A lavagem se "
            "repete de 8 a 12 vezes até a cafeína cair ao exigido: nos EUA, a retirada de pelo menos 97%. E "
            "descafeinado não é sem cafeína: um estudo de 2006 achou, em geral, 1% a 2% da cafeína original nas "
            "bebidas, mas às vezes até 20%."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Decaffeination",
                "The first commercially successful decaffeination process was invented by German merchant Ludwig Roselius and co-workers in 1903, after Roselius observed that a consignment of coffee beans accidentally soaked in sea water had lost most of their caffeine content while losing little of their flavour. "
                "The process was patented in 1906, and involved steaming coffee beans with various acids or bases, then using benzene as a solvent to remove the caffeine. "
                "Coffee decaffeinated this way was sold as Kaffee HAG [...] and later as Sanka brand coffee in the United States. [...] "
                "Methods similar to those first developed by Roselius have continued to dominate [...] "
                "However, because of health concerns regarding benzene (which is recognized today as a carcinogen), other solvents, such as dichloromethane or ethyl acetate, are now used. [...] "
                "The process is repeated between 8 and 12 times until the caffeine content meets the required standard (97% of caffeine removed according to the US standard [...] "
                "A 2006 study found decaffeinated drinks to contain typically 1 [...] 2% of the original caffeine content, but sometimes as much as 20%. [...] "
                "Friedlieb Ferdinand Runge performed the first isolation of caffeine from coffee beans in 1820, after the German poet Goethe heard about his work on belladonna extract, and requested he perform an analysis on coffee beans. "
                "Though Runge was able to isolate the compound, he did not learn much about the chemistry of caffeine itself, nor did he seek to use the process commercially to produce decaffeinated coffee. [...] "
                "solvents such as dichloromethane or ethyl acetate, supercritical CO2, or water to extract caffeine from the beans",
                nome="Decaffeination"),
            wiki("Ludwig_Roselius",
                "was a German coffee merchant and founder of the company Kaffee HAG.  He was born in Bremen and is credited with the development of commercial decaffeination of coffee.",
                nome="Ludwig Roselius"),
        ],
    },
    # 14 tijolos de chá como dinheiro
    {
        "temas_secundarios": ["dinheiro", "asia_antiga", "comercio_rotas"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Na Ásia, tijolos de chá prensado serviram de dinheiro, alguns misturados com sangue ou esterco para aguentar o manuseio. Na Sibéria, ainda eram moeda comestível até a Segunda Guerra Mundial.",
        "explicacao": (
            "Antes da dinastia Ming, o chá prensado em blocos era a forma mais comum de chá na China. Os tijolos "
            "eram compactos e resistiam melhor que folhas soltas às longas viagens das caravanas pela Rota do Chá e "
            "dos Cavalos, uma rede de trilhas de montanha entre Sichuan, Yunnan e o Tibete. O nome vem da troca de "
            "pôneis tibetanos por chá chinês, prática que remonta pelo menos à dinastia Song, quando a China "
            "precisava de cavalos fortes para enfrentar os nômades do norte. Carregadores levavam nas costas de 60 "
            "a 90 kg de chá, muitas vezes mais que o próprio peso. Como o chá valia muito, os tijolos viraram moeda "
            "na China, no Tibete, na Mongólia e na Ásia Central, e os nômades da Mongólia e da Sibéria os preferiam "
            "às moedas de metal. Tinham uma vantagem que nenhuma moeda tem: em tempos de fome, podiam ser comidos. "
            "No Tibete, os tijolos vinham da região de Ya'an, em cinco qualidades com valores diferentes; o tipo mais "
            "usado como dinheiro no fim do século XIX e início do XX já tinha valido oito moedas de prata tibetanas "
            "em Lhasa, e por isso se chamava \"oitavo\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Tea_brick",
                "This was the most commonly produced and used form of tea in ancient China prior to the Ming Dynasty. [...] "
                "Some tea bricks were also mixed with binding agents such as flour, blood, or manure to better preserve their form so they could withstand physical use as currency. [...] "
                "Tea bricks were preferred in Asian trade prior to the 19th century, since they were more compact and less susceptible to physical damage than loose leaf tea. "
                "This was important during transportation over land by caravans on the Tea Horse Road. [...] "
                "Due to the high value of tea in many parts of Asia, tea bricks were used as a form of currency throughout China, Tibet, Mongolia, and Central Asia. [...] "
                "Tea bricks were in fact the preferred form of currency over metallic coins for the nomads of Mongolia and Siberia. "
                "The tea could not only be used as money and eaten as food in times of hunger [...] "
                "Until World War II, tea bricks were still used as a form of edible currency in Siberia. "
                "Tea bricks for Tibet were mainly produced in the area of Ya'an (formerly Yachou-fu) in Sichuan province. "
                "The bricks were produced in five different qualities and valued accordingly. "
                "The kind of brick which was most commonly used as currency in the late 19th and early 20th century was that of the third quality which the Tibetans called brgyad pa ('eighth'), because at one time it was worth eight Tibetan tangkas (standard silver coin of Tibet",
                nome="Tea brick"),
            wiki("Tea_Horse_Road",
                "was a network of caravan paths winding through the mountains of Sichuan, Yunnan and Tibet in Southwest China. [...] "
                "The route earned the name because of the common trade of Tibetan ponies for Chinese tea, a practice dating back at least to the Song dynasty, when the sturdy horses were important for China to fight warring nomads in the north. [...] "
                "Tea porters sometimes carried over 60 [...] 90 kg [...] which was often more than their own body weight in tea.",
                nome="Tea Horse Road"),
        ],
    },
    # 15 guaraná: o dobro da cafeína do café e o mito dos olhos
    {
        "temas_secundarios": ["povos_indigenas", "amazonia", "mitologia"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "A semente do guaraná pode ter até 6% de cafeína, o dobro ou mais que o grão de café verde. Para os Sateré-Mawé, a planta nasceu dos olhos de uma criança, e o fruto aberto lembra mesmo um olho.",
        "explicacao": (
            "O guaraná, Paullinia cupana, é uma trepadeira nativa da bacia amazônica e muito comum no Brasil. Suas "
            "sementes têm mais ou menos o tamanho de um grão de café e podem chegar a cerca de 6% de cafeína, "
            "enquanto o grão de café verde tem de 1% a 3%. Como em outras plantas com cafeína, essa concentração é "
            "uma defesa: a substância é tóxica e afasta insetos do fruto e das sementes. O fruto vai do marrom ao "
            "vermelho e, quando se abre, mostra sementes pretas parcialmente cobertas por uma camada branca, um "
            "contraste que lembra um globo ocular. Disso nasceu um mito de origem atribuído aos Sateré-Mawé, de "
            "cuja língua vem a palavra, de warana. Uma divindade matou uma criança querida da aldeia. Para consolar "
            "o povo, um deus mais benevolente arrancou o olho esquerdo dela e o plantou na floresta, dando origem ao "
            "guaraná selvagem. Depois plantou o olho direito na aldeia, e dele veio o guaraná cultivado. Hoje a "
            "semente vai para refrigerantes no Brasil, terceiro maior consumidor de refrigerantes do mundo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Guarana",
            "is a climbing plant in the family Sapindaceae, native to the Amazon basin and especially common in Brazil. "
            "Guaraná has large leaves and clusters of flowers, and is best known for the seeds from its beans, which are about the size of a coffee bean. [...] "
            "Products containing guaraná can be effective stimulants: the seeds can be up to about 6% caffeine. "
            "For comparison, green coffee beans are about 1 [...] 3% caffeine. [...] "
            "As with other plants producing caffeine, the high concentration of caffeine is a defensive toxin that repels insects from the berry and seeds. "
            "The color of the fruit ranges from brown to red and it contains black seeds that are partly covered by white arils. "
            "The color contrast when the fruit is split open has been compared with the appearance of eyeballs, and has become the basis of an origin myth among the Sateré-Mawé people. [...] "
            "The word guaraná has its origins in the Sateré-Maué word for the plant, warana. [...] "
            "According to a myth attributed to the Sateré-Maué tribe, guaraná's domestication originated with a deity killing a beloved village child. "
            "To console the villagers, a more benevolent god plucked the left eye from the child and planted it in the forest, resulting in the wild variety of guaraná. "
            "The god then plucked the right eye from the child and planted it in the village, giving rise to domesticated guaraná. [...] "
            "Brazil, the third-largest consumer of soft drinks in the world, produces several soft drink brands from the seeds of guaraná.",
            nome="Guaraná")],
    },
]
