LOTE = "2026-11-24-jogos_azar-01"
AREA = "esportes_jogos"
TEMA = "jogos_azar"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


MACTUTOR_CARDANO = "https://mathshistory.st-andrews.ac.uk/Biographies/Cardan/"
SPRINGER_DADOS = "https://link.springer.com/article/10.1007/s12520-022-01599-y"
SMITHSONIAN_VOLTAIRE = "https://www.smithsonianmag.com/smart-news/voltaire-enlightenment-philosopher-and-lottery-scammer-180967265/"
YALE_LOTERIAS = "https://cases.som.yale.edu/voltaire-casanova-and-18th-century-lotteries"

CANDIDATOS = [
    # 1 Cardano, o médico jogador que escreveu o primeiro estudo de probabilidade
    {
        "temas_secundarios": ["historia_matematica", "probabilidade"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "O primeiro estudo sistemático de probabilidade foi escrito no século XVI por Gerolamo Cardano, médico que pagava as contas com cartas, dados e xadrez. O livro, que ensina até a trapacear, só saiu em 1663.",
        "explicacao": (
            "Cardano (1501–1576) foi médico, matemático, astrólogo e muitas outras coisas, inclusive jogador. "
            "Depois de torrar a pequena herança do pai, passou a ganhar a vida com cartas, dados e xadrez. Como "
            "entendia de probabilidade melhor que os adversários, em geral ganhava mais do que perdia. O jogo, "
            "porém, virou vício por muitos anos: numa fase ruim, ele precisou penhorar as joias da esposa, e de "
            "1540 a 1542 largou os estudos e não fez outra coisa. Andava sempre com uma faca e, certa vez, cortou "
            "o rosto de um adversário que julgou estar roubando nas cartas. Dessa experiência saiu o Liber de "
            "ludo aleae, \"Livro sobre os jogos de azar\". Usando os dados, Cardano mostrou a vantagem de medir as "
            "chances pela razão entre resultados favoráveis e desfavoráveis, e chegou perto da regra que manda "
            "multiplicar as probabilidades de eventos independentes. O livro traz também uma seção sobre métodos "
            "eficazes de trapaça. Concluído por volta de 1563 ou 1564, só foi publicado em 1663. Àquela altura, "
            "Pascal e Fermat já tinham discutido em cartas, por volta de 1654, o problema da divisão das apostas, "
            "criando conceitos que ainda são a base da teoria da probabilidade."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Gerolamo_Cardano",
                "24 September 1501– 21 September 1576) was an Italian polymath whose interests and proficiencies ranged through those of mathematician, physician, biologist, physicist, chemist, astrologer, astronomer, philosopher, music theorist, writer, and gambler. [...] "
                "Cardano was chronically short of money and kept himself solvent by being an accomplished gambler and chess player. "
                "His book, Liber de ludo aleae (\"Book on Games of Chance\"), written around 1564, but not published until 1663, contains the first systematic treatment of probability, as well as a section on effective cheating methods. "
                "He used the game of throwing dice to understand the basic concepts of probability. "
                "He demonstrated the efficacy of defining odds as the ratio of favourable to unfavourable outcomes [...] "
                "He was also aware of the multiplication rule for independent events but was not certain about what values should be multiplied.",
                nome="Gerolamo Cardano"),
            {"url": MACTUTOR_CARDANO, "titulo": "Girolamo Cardano – MacTutor History of Mathematics (Universidade de St Andrews)", "idioma": "en",
             "trecho": "Cardan squandered the small bequest from his father and turned to gambling to boost his finances. "
                       "Card games, dice and chess were the methods he used to make a living. "
                       "Cardan's understanding of probability meant he had an advantage over his opponents and, in general, he won more than he lost. "
                       "He had to keep dubious company for his gambling. "
                       "Once, when he thought he was being cheated at cards, Cardan, who always carried a knife, slashed the face of his opponent. "
                       "Gambling became an addiction that was to last many years [...] "
                       "things went so badly that he was forced to pawn his wife's jewellery and even some of his furniture. [...] "
                       "From 1540 to 1542 Cardan abandoned his studies and did nothing but gamble; playing chess all day. [...] "
                       "His book Liber de Ludo Aleae Ⓣ was published in 1663 but the book on games of chance was probably completed by 1563."},
            wiki("Problem_of_points",
                "The problem arose again around 1654 when the Chevalier de Méré, Antoine Gombaud posed it to Blaise Pascal. "
                "Pascal discussed the problem in his ongoing correspondence with Pierre de Fermat. "
                "Through this discussion, Pascal and Fermat not only provided a convincing, self-consistent solution to this problem, but also developed concepts that are still fundamental to probability theory.",
                nome="Problem of points"),
        ],
    },
    # 2 astrágalos: os ossinhos que vieram antes dos dados
    {
        "temas_secundarios": ["probabilidade", "grecia_antiga", "roma_antiga"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "Os precursores dos dados devem ter sido ossinhos do tornozelo de animais, os astrágalos. Eles param em só quatro lados, e com chances desiguais: o lado largo sai em cerca de 38% das vezes; os outros, uns 12%.",
        "explicacao": (
            "O astrágalo, ou tálus, é um osso do tornozelo de animais com cascos; na versão grega do jogo, era o "
            "de ovelha. Quase simétrico, ele só consegue parar sobre quatro lados, o que o torna um dos exemplos "
            "mais antigos de jogo de azar. Em escavações de períodos a partir de 5000 a.C., esses ossos aparecem com "
            "frequência bem maior que os demais, e acredita-se que sejam precursores dos dados. Na Grécia e em Roma, "
            "o jogo agradava a crianças e adultos e servia para apostas e adivinhação, com um valor atribuído a cada "
            "face. Os próprios gregos não concordavam sobre quem o inventou: Sófocles creditava o jogo ao herói "
            "mítico Palamedes, na Guerra de Troia; Platão, ao deus egípcio Tot; Heródoto, aos lídios, que o teriam "
            "criado durante uma fome. Os romanos jogavam com os tali, grandes, que levavam só 1, 3, 4 e 6 em quatro "
            "lados, e com as tesserae, dados menores numerados de 1 a 6. Na Ásia Central, os ossinhos de carneiro ou "
            "cabra seguem em uso em jogos e adivinhação, e o shagai dos mongóis entrou em 2014 na lista de "
            "Patrimônio Cultural Imaterial da Humanidade da UNESCO."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Knucklebones",
                "Knucklebones, also known as scatter jacks, snobs, astragaloi (singular: astragalus), tali, dibs, [...] "
                "The name \"knucklebones\" is derived from the Ancient Greek version of the game, which uses the astragalus (a bone in the ankle, or hock) of a sheep. [...] "
                "The talus bones of hooved animals (also known as astragali) are found in archaeological excavations related to the period starting from 5000 BCE much more frequently than other bones. "
                "Astragalus, being almost symmetric, has only four sides on which it may rest and is an early example of the game of chance. "
                "Knucklebones are believed to be an early precursor of dice. "
                "In contrast to dice, the astragalus is not entirely symmetric, with the broad side having a chance ~0.38 and the other sides having a chance ~0.12. [...] "
                "The game was widely popular in ancient Greece and Rome, and was played by children and adults alike. "
                "It was also widely used for gambling and divination, with different faces of the bone assigned specific values. [...] "
                "Sophocles, in a written fragment of one of his works, ascribed the game to the mythical figure Palamedes, who supposedly taught it to his Greek countrymen during the Trojan War. [...] "
                "Plato, in Phaedrus, names the Egyptian god Thoth as its inventor, while Herodotus relates that the Lydians, during a period of famine in the days of King Atys, originated this game [...] "
                "Knucklebones in Central Asian cultures use the astragalus of sheep or goat or the calcaneus of wolves. [...] "
                "They are used in games, fortune-telling, and as musical instruments. [...] "
                "The Mongolian shagai is inscribed in the List of the Intangible Cultural Heritage of Humanity by UNESCO in 2014.",
                nome="Knucklebones"),
            wiki("Dice",
                "There were two sizes of Roman dice. Tali were large dice inscribed with one, three, four, and six pips on four sides. "
                "Tesserae were smaller dice with sides numbered from one to six.",
                nome="Dice"),
        ],
    },
    # 3 dados etruscos e a disputa sobre os números 4 e 6
    {
        "temas_secundarios": ["decifracao", "roma_antiga"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "Até 500 a.C., os dados etruscos punham 1 e 2, 3 e 4, 5 e 6 em faces opostas; depois de 350 a.C., as faces opostas somavam 7, como hoje. Essa mudança foi usada para propor quais palavras etruscas eram 4 e 6.",
        "explicacao": (
            "Há 30 maneiras de numerar de 1 a 6 as faces de um dado, ou 15 se as versões espelhadas contarem como "
            "uma só. Por razões desconhecidas, os romanos usavam em geral a combinação em que faces opostas somam 7, "
            "tradição que seguiu na Europa e virou padrão mundial. Em 2011, uma análise de 91 dados etruscos de "
            "várias épocas e lugares mostrou outra história: os de 500 a.C. ou antes usavam só o padrão 1–2, 3–4, "
            "5–6, em que as faces opostas diferem de 1, e os de 350 a.C. em diante seguiam o padrão romano. Entre "
            "essas datas, um substituiu o outro aos poucos. Isso entrou numa velha disputa sobre a língua etrusca. "
            "Todos concordam que as palavras para 4 e 6 são huθ e śa, mas não sobre qual é qual. Até pouco tempo, "
            "aceitava-se, por inscrições em túmulos, que huθ era 4. Um par de dados de Tuscania traz os números "
            "escritos por extenso, e, nos dois padrões, 3 e 4 ficam em faces opostas. Como a palavra oposta a śa, "
            "ci, era sabidamente 3, os pesquisadores concluíram que śa é 4 e huθ é 6. A questão não está fechada: "
            "outra proposta, que supõe uma contagem de base 12, devolve a huθ o valor 4."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Etruscan_numerals",
            "There has been a longstanding controversy about the assignment of 4 and 6. "
            "All Etruscologists agree that the words are huθ (huth) and śa (sha). "
            "The disagreement is about which is which. "
            "Until recently, it was generally accepted, based on archaeological evidence, that 4 was huθ and 6 was śa. [...] "
            "However, that assignment was challenged in 2011 by a thorough analysis of 91 Etruscan gambling dice, from many different ages and locations, with numbers marked by dots (\"pips\"); "
            "and a lone pair of dice (the \"Tuscanian dice\" or \"dice of Toscanella\") with the numbers written out as words. "
            "Mathematically, there are 30 ways to place the numbers 1–6 on the faces of a die; or 15 if one counts together numberings that are mirror images of each other. [...] "
            "For unknown reasons, Roman dice generally used the last pattern, (1–6, 2–5, 3–4), in which every pair of opposite faces adds to 7; "
            "a tradition that continued in Europe to the present day, and has become the standard all over the world. "
            "However, among the 91 Etruscan dice from many different locations, those from 500 BCE or earlier used only the first pattern, (1–2, 3–4, 5–6), in which the opposite faces differ by 1. "
            "Those from 350 BCE and later, on the other hand, used the Roman (1–6, 2–5, 3–4) pattern. "
            "Between 500 and 350 BCE, the latter gradually replaced the former at all Etruscan sites covered. "
            "On the Tuscany dice, the opposite faces carry the words (θu–huθ, zal–maψ, ci-śa). "
            "In both the \"old\" and \"new\" patterns, however, the values 3 and 4 lie on opposite faces. "
            "Thus, since ci was known to be 3, the researchers concluded that śa must be 4; and since there is no dissent about the words for 1, 2, and 5, huθ had to be 6. [...] "
            "In 2006, S. A. Yatsemirsky presented evidence that zar or śar meant '12' (cf. zal '2' and zaθrum '20') while halψ meant '10'. "
            "According to his interpretation, the attested form huθzar could only mean 'sixteen', and huθ must therefore mean 'four'.",
            nome="Etruscan numerals")],
    },
    # 4 os dados romanos tortos
    {
        "temas_secundarios": ["roma_antiga", "probabilidade"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "De 80% a 90% dos dados romanos são visivelmente tortos, e muitos favorecem o 1 e o 6. Para dois arqueólogos, não era trapaça: quem jogava via o resultado como obra do destino, e um cubo perfeito não parecia essencial.",
        "explicacao": (
            "Hoje esperamos que um dado seja simétrico e que cada face tenha a mesma chance de sair. Muitos dados de "
            "seis lados da época romana, achados em sítios arqueológicos por toda a Europa, fogem disso: são "
            "achatados ou alongados e favorecem certos números, sobretudo o 1 e o 6. Pela visão humana, dá para "
            "notar diferenças de tamanho a partir de uns 5%, e medições mostram que 80% a 90% dos dados romanos "
            "passam desse limite, contra menos da metade dos dados medievais e posteriores. A distorção pesa: em "
            "modelos, um dado 5% maior num eixo já muda de cerca de 33% para quase 40% a chance de cair numa das "
            "faces maiores. Seriam dados de trapaceiro? Num estudo publicado em 2022, Jelmer Eerkens e Alex de "
            "Voogt mediram 28 dados romanos bem datados da atual Holanda e viram uma variação contínua, do cubo "
            "perfeito a peças com um lado mais de 50% maior que o outro, e não tipos separados. Em experimentos, "
            "pessoas sem prática que marcavam os pontos em blocos irregulares tendiam a pôr o 6 na face maior, por "
            "falta de espaço, não para favorecer jogadas. Os autores defendem que tanta variação era aceita porque "
            "fabricantes e jogadores entendiam o resultado como fruto do destino, e não do acaso ou da probabilidade."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [{"url": SPRINGER_DADOS, "titulo": "Why are Roman-period dice asymmetrical? An experimental and quantitative approach (Archaeological and Anthropological Sciences, 2022)", "idioma": "en",
            "trecho": "Published: 23 June 2022 [...] "
                      "Roman-period six-sided dice are common in archaeological sites across Europe. "
                      "While some dice approach true cubes, many are visibly non-cubic (i.e., asymmetric/lopsided) and favor certain rolls, especially the numbers 1 and 6. "
                      "It is unclear if such dice were intentional and distinctive “types” used in specific games or activities, represent “cheaters” dice, or are simply part of a continuum of variation in die shape and configuration. "
                      "To explore this issue, we examine shape distribution of 28 well-dated Roman-period dice from modern-day Netherlands. "
                      "Results show that Roman die asymmetry varies in a continuous fashion from true cube to highly parallelepiped, where the long side is over 50% longer than the short side. "
                      "We then conduct replication experiments to examine how naïve producers configure pips across a range of shapes. "
                      "Our results show a production bias, where makers place the 6 on the largest die face, not to favor certain rolls, but due to space limitations and/or the order in which they place the pips. "
                      "Overall, we interpret asymmetrical Roman dice as part of a single but highly variable artifact category, not distinct types. "
                      "We argue that such extreme variation was acceptable because makers and users understood roll outcomes as the product of fate, rather than chance or probability. "
                      "Conformity to a true symmetrical cube was not perceived as essential to die function [...] "
                      "Human visual perception can distinguish difference in size when two objects vary in magnitude by approximately 5% or more [...] "
                      "Detailed measurements show that 80–90% of Roman dice are visibly asymmetrical (Schmid 1978:58; Swift 2017b:159), compared to less than 50% of later Medieval and post-Medieval dice (Eerkens and de Voogt 2017). [...] "
                      "because in western culture six-sided dice are highly symmetrical, and because we expect the die to roll “fairly,” wherein each side has equal probability of being rolled. [...] "
                      "Modeling by Mungan and Lipscombe (2013) shows that even a small increase in one axis of a cube shifts the probability of rolling one of the larger sides markedly, for example, from approximately 33% for a true cube, to nearly 40% for a die that is 5% larger on one axis."}],
    },
    # 5 o naipe de paus era de tacos de polo, e "naipe" vem do árabe
    {
        "temas_secundarios": ["palavras_viajantes", "mundo_islamico_medieval"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "O naipe de paus já foi de tacos de polo. As cartas chegaram à Europa vindas do Egito dos mamelucos, e os europeus, que mal conheciam o polo, trocaram os tacos por bastões. Até \"naipe\" vem do árabe.",
        "explicacao": (
            "As cartas de baralho provavelmente surgiram na China da dinastia Tang, por volta do século IX, junto "
            "com a impressão em blocos de madeira. Espalharam-se pela Ásia e, a partir do século XI, chegaram ao "
            "Egito. Um baralho mameluco quase completo, do século XV, foi encontrado em 1939 no Palácio de Topkapı, "
            "em Istambul. Tinha originalmente 52 cartas, em quatro naipes: tacos de polo, moedas, espadas e taças. "
            "Cada naipe trazia dez cartas numeradas e três figuras: o rei (malik), o vice-rei (nā'ib malik) e um "
            "segundo vice-rei. Essas figuras não mostravam pessoas, só desenhos abstratos ou caligrafia, talvez por "
            "restrição religiosa. As cartas devem ter entrado na Europa pela Espanha: a menção europeia mais antiga "
            "é de 1371, num dicionário de rimas em catalão que lista a palavra naip, cujo único sentido conhecido é "
            "\"carta de jogar\". O título nā'ib passou ao francês, ao italiano e ao espanhol, e o português naipe "
            "veio do catalão naip. Os europeus mantiveram moedas, espadas e taças, mas o polo era um esporte "
            "obscuro para eles, e os tacos viraram bastões. São esses os naipes dos baralhos tradicionais italiano, "
            "espanhol e português, de onde vêm os nossos paus, ouros, espadas e copas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Playing_card",
                "Playing cards were most likely invented during the Tang dynasty around the 9th century, as a result of the usage of woodblock printing technology. [...] "
                "By the 11th century, playing cards were spreading throughout the Asian continent and later came into Egypt. [...] "
                "A near complete pack of Mamluk playing cards dating to the 15th century, and of similar appearance to the fragments above, was discovered by Leo Aryeh Mayer in the Topkapı Palace, Istanbul, in 1939. [...] "
                "The Topkapı pack originally contained 52 cards comprising four suits: polo-sticks, coins, swords, and cups. "
                "Each suit contained ten pip cards and three court cards, called malik (king), nā'ib malik (viceroy or deputy king), and thānī nā'ib (second or under-deputy). [...] "
                "The Mamluk court cards showed abstract designs or calligraphy not depicting persons possibly due to religious proscription in Sunni Islam, though they did bear the ranks on the cards. "
                "Nā'ib would be borrowed into French (nahipi), Italian (naibi), and Spanish (naipes), the latter word still in common usage. [...] "
                "Playing cards probably came to Europe from the East, specifically those used by the Mamluks in Egypt, and probably arrived first in Spain since the earliest European mention of playing cards appears in 1371 in a Catalan language rhyme dictionary which lists naip among words ending in -ip. "
                "According to Trevor Denning, the only attested meaning of this Catalan word is \"playing card\". [...] "
                "Among the early patterns of playing card were those derived from the Mamluk suits of cups, coins, swords, and polo sticks, which are still used in traditional Latin decks. "
                "As polo was an obscure sport to Europeans then, the polo-sticks became batons or cudgels.",
                nome="Playing card"),
            wiki("Naipe",
                "A palavra naipe, derivada do catalão naip, \"carta\" (que por sua vez é originada do árabe نَائِب, nāʾib, \"representante\")",
                nome="Naipe", idioma="pt"),
            wiki("Tarot",
                "An early pattern of playing cards used the suits of batons or clubs, coins, swords, and cups. "
                "These suits are still used in traditional Italian, Spanish and Portuguese playing card decks",
                nome="Tarot"),
        ],
    },
    # 6 por que o inglês chama o trevo de "clubs" e a lança de "spades"
    {
        "temas_secundarios": ["palavras_viajantes", "europa_medieval"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "Em inglês, o naipe ♣ se chama clubs, \"bastões\", e o ♠ ganhou o nome da espada, spade. Os símbolos franceses chegaram à Inglaterra quando já circulavam lá cartas de naipes latinos, e os nomes antigos ficaram.",
        "explicacao": (
            "Os primeiros baralhos europeus herdaram dos mamelucos os naipes de taças, moedas, espadas e bastões, "
            "que seguem nos baralhos latinos. Quando as cartas passaram da Itália aos países germânicos, os naipes "
            "viraram folhas, corações, sinos e bolotas de carvalho. Por volta de 1480, os fabricantes franceses, "
            "talvez para facilitar a produção em massa, adotaram versões bem simplificadas dos símbolos alemães. "
            "Nasceram assim os trevos, os carreaux (\"ladrilhos\", os nossos ouros), os corações e os piques, que "
            "são lanças. O trevo provavelmente derivou da bolota, e a lança, da folha. Fabricantes de Rouen passaram "
            "a exportar cartas para a Inglaterra por volta de 1480, mas há sinais de cartas no país desde pelo menos "
            "a década de 1450. Segundo o historiador de jogos David Parlett, cartas de naipes latinos já deviam "
            "circular por lá, o que explicaria por que os ingleses deram aos símbolos franceses os nomes latinos que "
            "conheciam: o trevo virou clubs, bastões, e a lança foi batizada com a espada italiana, spade. A "
            "simplicidade desses símbolos, fáceis de produzir em massa, é apontada como uma das razões de o baralho "
            "francês ter se tornado o mais difundido do mundo, ao lado da influência de França, Reino Unido e "
            "Estados Unidos."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Playing_card",
                "Among the early patterns of playing card were those derived from the Mamluk suits of cups, coins, swords, and polo sticks, which are still used in traditional Latin decks. [...] "
                "As cards spread from Italy to Germanic countries, the Latin suits were replaced with the suits of leaves (or shields), hearts (or roses), bells, and acorns. [...] "
                "but around 1480, French card manufacturers, perhaps in order to facilitate mass production, went over to very much simplified versions of the German suit symbols. "
                "A combination of Latin and Germanic suit pictures and names resulted in the French suits of trèfles (clovers), carreaux (tiles), cœurs (hearts), and piques (pikes) around 1480. "
                "The trèfle (clover) was probably derived from the acorn and the pique (pike) from the leaf of the German suits. "
                "The names pique and spade, however, may have derived from the sword (spade) of the Italian suits.",
                nome="Playing card"),
            wiki("French-suited_playing_cards",
                "In comparison to Spanish, Italian, German, and Swiss playing cards, French cards are the most widespread due to the geopolitical, commercial, and cultural influence of France, the United Kingdom, and the United States in the 19th and 20th centuries. "
                "Other reasons for their popularity were the simplicity of the suit insignia, which simplifies mass production, and the popularity of whist and contract bridge. [...] "
                "Card makers from Rouen began exporting to England around 1480. "
                "According to David Parlett, Latin-suited cards must have already been circulating in England since there is evidence of playing cards there from at least the 1450s and French suits were invented sometime after 1470. "
                "This would then explain why the English renamed French suits to the Latin ones with which they were familiar. "
                "Hence the clovers were called clubs and pikes were named after the swords (spade).",
                nome="French-suited playing cards"),
        ],
    },
    # 7 o ás de espadas, o imposto e a forca
    {
        "temas_secundarios": ["leis_julgamentos", "economia_curiosa"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O ás de espadas é tão enfeitado por causa de um imposto. Na Inglaterra, ele provava que o baralho pagara a taxa, e falsificá-lo podia dar forca: em 1805, um homem pego com ases falsos foi enforcado.",
        "explicacao": (
            "O imposto do selo, ideia levada à Inglaterra por Carlos I, foi estendido às cartas de baralho pela "
            "rainha Ana em 1711 e só acabou em 1960. A partir de 1712, uma carta de cada maço, em geral o ás de "
            "espadas, recebia um carimbo feito à mão para mostrar que a taxa fora paga. Em 1765, o carimbo deu "
            "lugar a um ás de espadas oficial, impresso pela própria repartição do selo, com o brasão real. "
            "Falsificar esse ás era crime punido com a morte. Um fabricante de cartas foi apanhado com ases falsos "
            "e com o equipamento para fazê-los. A acusação ficou com o procurador-geral Spencer Perceval, que mais "
            "tarde seria primeiro-ministro e acabaria assassinado em 1812, e o condenado, Richard Harding, foi "
            "enforcado em 1805. Episódios assim podem estar na origem da fama do ás de espadas como carta da morte. "
            "Em 1862, a prova do pagamento passou para uma embalagem oficial, e os fabricantes ficaram livres para "
            "desenhar o ás como quisessem. A maioria manteve o desenho caprichado, e é por isso que, ainda hoje, o "
            "ás de espadas costuma trazer as informações do fabricante do baralho."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Ace_of_spades",
            "The ornate design of the ace of spades, common in packs today, stems from the 17th century, when James I and later Queen Anne imposed laws requiring the ace of spades to bear an insignia of the printing house. "
            "Stamp duty, an idea imported to England by Charles I, was extended to playing cards in 1711 by Queen Anne and lasted until 1960. "
            "Over the years, a number of methods were used to show that duty had been paid. "
            "From 1712 onwards, one of the cards in the pack, usually the ace of spades, was marked with a hand stamp. "
            "In 1765 hand stamping was replaced by the printing of the official ace of spades by the Stamp Office, incorporating the royal coat of arms. [...] "
            "One maker of cards was caught in possession of forged aces and the equipment to produce them. "
            "This was a capital offence, and the prosecutor Attorney General Spencer Perceval (later to become the prime minister assassinated in 1812) obtained the conviction of Richard Harding, who was hanged in 1805. "
            "The association of the ace of spades with death may spring from such events. "
            "The system was changed again in 1862 when official threepenny duty wrappers were introduced and, although the makers were free to use whatever design they wanted, most chose to keep the ornate ace of spades that is popular today. "
            "The ace of spades is thus used to show the card manufacturer's information.",
            nome="Ace of spades")],
    },
    # 8 o curinga nasceu para o euchre
    {
        "temas_secundarios": ["palavras_viajantes"],
        "tipos_espanto": ["origem_inesperada"],
        "gancho": "O curinga nasceu nos EUA, em meados do século XIX, como a carta mais forte de um jogo chamado euchre. E o nome Joker provavelmente vem de Jucker, a grafia alemã original do euchre.",
        "explicacao": (
            "As regras mais antigas do euchre, de 1844, usam 32 cartas comuns. A carta mais forte era o valete do "
            "naipe de trunfo, o right bower, seguido do valete da mesma cor, o left bower. Segundo o historiador de "
            "jogos David Parlett, uma carta extra foi acrescentada ao baralho de 32 na década de 1850 especialmente "
            "para o euchre. Ela aparece pela primeira vez num livro de regras em 1868: a carta em branco que vinha "
            "de amostra no maço passou a valer mais que todas as outras, numa variante chamada \"euchre com o "
            "Joker\". O fabricante Samuel Hart imprimiu em 1863 a primeira carta ilustrada desse tipo, a \"Best "
            "Bower\". Cartas com o nome Joker surgiram no fim dos anos 1860, algumas com palhaços e bobos da corte. "
            "A ideia dos três valetes mais fortes parece ter vindo de jogos alemães, e acredita-se que o nome venha "
            "de Jucker, como o euchre se escrevia originalmente em alemão. Por volta de 1875, a carta passou ao "
            "pôquer, onde valia por qualquer outra, o papel que ela tem até hoje em muitos jogos. Maços com dois "
            "curingas só viraram norma no fim dos anos 1940, por causa da canastra."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "consenso_parcial",
        "fontes": [wiki("Joker_(playing_card)",
            "The Joker originated in the United States during the Civil War, and was created as a trump card for the game of Euchre. "
            "It has since been adopted into many other card games, where it often acts as a wild card [...] "
            "In the earliest rules of 1844, 32 standard cards are used and the Right Bower, the trump Jack, was the \"commanding card\" with the Left Bower, the Jack of the same colour, as the second-highest card. "
            "According to card game historian, David Parlett, the Joker was added to a 32‑card pack in the 1850s specifically for the game of Euchre and is first mentioned in a set of rules in 1868 where the blank specimen card is adapted for use in play. "
            "This gave rise to a variant game called \"Euchre with the Joker\" in which the blank card ranked above all the rest. [...] "
            "Samuel Hart is credited with printing the first illustrated \"Best Bower\" card in 1863 with his \"Imperial Bower\". [...] "
            "Cards labelled \"Joker\" began appearing around the late 1860s, with some depicting clowns and jesters such as Elizabethan jester Richard Tarlton. "
            "The idea behind the three top cards in Euchre appears to have originated from Germany where the games Juckerspiel and Bester Bube (\"Best Bower\") also used Jacks as best, right and left bowers. "
            "It is also believed that the term \"Joker\" comes from Juckerspiel, which is also known as Jucker, the original German spelling of Euchre. [...] "
            "The notion of a Joker was later transferred to the game of Poker where it was initially called the Mistigris. "
            "This happened around 1875, where it functioned as a wild card. "
            "Packs with two Jokers started to become the norm during the late 1940s for the game of Canasta.",
            nome="Joker (playing card)")],
    },
    # 9 o tarô começou como jogo de cartas
    {
        "temas_secundarios": ["costumes_rituais", "europa_medieval"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "O tarô nasceu na Itália do século XV como jogo de cartas, e ainda é jogado assim em boa parte da Europa. O uso para ler a sorte só veio no fim do século XVIII, com a tese, sem provas, de que ele vinha do Egito antigo.",
        "explicacao": (
            "Os primeiros baralhos de tarô aparecem em registros entre 1440 e 1450, em Milão, Ferrara, Florença e "
            "Bolonha. Eram o baralho comum de quatro naipes com cartas extras de ilustrações alegóricas, chamadas "
            "trionfi, \"triunfos\", termo que deu origem ao inglês trumps, \"trunfos\". Serviam para jogos de "
            "vazas, e os exemplares mais antigos que sobreviveram são os do tarô Visconti-Sforza, pintados em meados "
            "do século XV para os governantes do Ducado de Milão. A virada veio em 1781, quando o clérigo francês "
            "Antoine Court de Gébelin publicou que o tarô não era só um jogo: teria origem no Egito antigo e "
            "profundo sentido místico. Ele contou que teve a ideia ao ver um grupo de mulheres jogando cartas. Pouco "
            "depois, o cartomante Etteilla criou, em 1783, um método de adivinhação com o tarô, e também o primeiro "
            "tarô \"egípcio\" feito só para esse fim. A pesquisa histórica mostra que o tarô foi inventado no norte "
            "da Itália em meados do século XV e não acha indício de uso relevante para adivinhação antes do fim do "
            "século XVIII. Os jogos de tarô continuam vivos: na França, o tarô é o segundo jogo de cartas mais "
            "popular."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Tarot",
                "From at least the mid-15th century, the tarot was used to play trick-taking card games such as Tarocchini. [...] "
                "The emergence of custom decks for use in divination via tarot card reading and cartomancy began after French occultists made elaborate, but unsubstantiated, claims about their history and meaning in the late 18th century. [...] "
                "French Tarot itself is now the second most popular card game in France. [...] "
                "The first documented tarot decks were recorded between 1440 and 1450 in Milan, Ferrara, Florence and Bologna, when additional trump cards with allegorical illustrations were added to the common four-suit pack. "
                "These new decks were called carte da trionfi, triumph cards, and the additional cards known simply as trionfi, which became \"trumps\" in English. [...] "
                "The oldest surviving tarot cards are the 15 or so decks of the Visconti-Sforza Tarot painted in the mid-15th century for the rulers of the Duchy of Milan. [...] "
                "However, scholarly research has demonstrated that tarot cards were invented in northern Italy in the mid-15th century and confirmed that there is no historical evidence of any significant use of tarot cards for divination until the late 18th century.",
                nome="Tarot"),
            wiki("Tarot_card_reading",
                "The first was Antoine Court de Gébelin, a French clergyman, who wrote that after seeing a group of women playing cards he had the idea that tarot was not merely a game of cards but was in fact of ancient Egyptian origin, of mystical Qabalistic import, and of deep divine significance. "
                "Court de Gébelin published a dissertation on the origins of the symbolism in the tarot in volume VIII of the work Le Monde primitif in 1781. [...] "
                "Etteilla devised a method of tarot divination in 1783 [...] "
                "he created the first Egyptian tarot to be used exclusively for cartomancy",
                nome="Tarot card reading"),
        ],
    },
    # 10 a loteria de números nasceu de apostas em eleições de Gênova
    {
        "temas_secundarios": ["probabilidade", "europa_medieval"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "A loteria de números nasceu de apostas em eleições. Em Gênova, 5 de 90 candidatos ao Grande Conselho eram sorteados, e o povo apostava nos nomes. Para jogar mais vezes, trocaram os nomes por números.",
        "explicacao": (
            "Na Itália, a primeira loteria registrada aconteceu em Milão, em 9 de janeiro de 1449, organizada pela "
            "República Ambrosiana para financiar a guerra contra Veneza. Mas foi em Gênova que o lotto pegou de "
            "verdade. A cada seis meses, cinco membros do Grande Conselho da cidade eram escolhidos por sorteio entre "
            "noventa candidatos, e as pessoas apostavam em quais nomes sairiam. Essa aposta era chamada de lotto ou "
            "semenaiu. Como o sorteio só acontecia duas vezes por ano, quem queria apostar com mais frequência passou "
            "a trocar os nomes dos candidatos por números. Daí nasceu o lotto moderno, do qual descendem tanto as "
            "loterias legais de hoje quanto o jogo ilegal de números. A ideia viajou: o rei Francisco I conheceu as "
            "loterias nas campanhas militares na Itália e criou uma na França, a Loterie Royale, em 1539, para "
            "reforçar as finanças do reino. Foi um fiasco, pois os bilhetes eram caríssimos e as classes que podiam "
            "comprá-los se opuseram ao projeto. A própria palavra inglesa lottery vem do holandês lot, que quer dizer "
            "\"destino\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Lottery",
            "The English word lottery is derived from the Dutch noun \"lot\" meaning \"fate\". "
            "The first recorded Italian lottery was held on 9 January 1449 in Milan organized by the Golden Ambrosian Republic to finance the war against the Republic of Venice. "
            "However, it was in Genoa that Lotto became very popular. "
            "People used to bet on the name of Great Council members, who were drawn by chance, five out of ninety candidates every six months. "
            "This kind of gambling was called Lotto or Semenaiu. "
            "When people wanted to bet more frequently than twice a year, they began to substitute the candidates names with numbers and modern lotto was born, to which both modern legal lotteries and the illegal numbers game can trace their ancestry. [...] "
            "King Francis I of France discovered the lotteries during his campaigns in Italy and decided to organize such a lottery in his kingdom to help the state finances. "
            "The first French lottery, the Loterie Royale, was held in 1539 and was authorized with the edict of Châteaurenard. "
            "This attempt was a fiasco, since the tickets were very costly and the social classes which could afford them opposed the project.",
            nome="Lottery")],
    },
    # 11 Voltaire e a loteria com defeito de cálculo
    {
        "temas_secundarios": ["probabilidade", "economia_curiosa"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Voltaire enriqueceu com um erro do governo francês: numa loteria de títulos públicos, o bilhete de um título barato custava pouquíssimo, mas tinha a mesma chance. Com amigos, ele comprou esses bilhetes aos montes.",
        "explicacao": (
            "Em 1729, o governo francês passou a sortear prêmios entre os donos dos seus títulos de dívida, para "
            "estimular a compra deles. Só quem tinha título podia jogar, e o preço do bilhete era atrelado ao valor "
            "do título: 1/1000 dele. O vencedor levava o valor de face do título e mais um prêmio de 500 mil libras, "
            "uma fortuna na época. O matemático Charles Marie de La Condamine percebeu o furo: o dono de um título "
            "pequeno pagava muito pouco pelo bilhete, mas tinha a mesma chance de ganhar de quem tinha um título de "
            "100 mil libras e pagava 100 pelo bilhete. Quem juntasse boa parte dos títulos pequenos ficaria com a "
            "maioria das entradas, gastando bem menos que o prêmio. A proposta surgiu num jantar, e a tática rendia "
            "mais em grupo: Voltaire, La Condamine e mais 11 parceiros formaram um consórcio e, em junho de 1730, "
            "todos tinham lucrado bastante. Eles não fraudaram os sorteios: exploraram uma brecha nas regras. A "
            "parte de Voltaire é estimada, conforme a fonte, entre meio milhão e um milhão de libras. O dinheiro, "
            "bem investido, deixou o escritor rico e independente, aos 30 e poucos anos, quando ainda não era nem "
            "rico nem particularmente famoso."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": SMITHSONIAN_VOLTAIRE, "titulo": "Voltaire: Enlightenment Philosopher and Lottery Scammer (Smithsonian Magazine)", "idioma": "en",
             "trecho": "It all unfolded when Voltaire was in his 30s. "
                       "At the time, he was “neither rich nor particularly famous,” writes Andy Williamson for Today I Found Out [...] "
                       "Starting in 1729, the French government started running a lottery on bonds it owned, in an attempt to promote the purchase of these bonds. "
                       "Only bond-holders could buy tickets in this lottery, and the price was pegged to the value of the bond. "
                       "Winners would get the face value of the bond in addition to a 500,000-livre jackpot, a huge sum of money at the time. [...] "
                       "You see, if you owned a bond worth a very small amount, with the lotto ticket for the bond costing just 1/1000th of the value, you could buy the lotto tickets extremely cheaply, yet your lotto ticket had just as much of a chance of winning as someone who owned a bond for 100,000 livres and had to buy their ticket for 100 livres. [...] "
                       "If he owned enough of these small bonds, he could quickly give himself the bulk of the entrees in the lotto while spending much less than the jackpot [...] "
                       "This system worked best if a consortium of players bought tickets together and split the winnings, so, writes Pearson, Voltaire, de la Condamine and 11 compatriots teamed up and by June 1730, all had made a tidy sum. "
                       "Voltaire’s take was around half a million livre"},
            wiki("Voltaire",
                "At a dinner, French mathematician Charles Marie de La Condamine proposed buying up the lottery that was organized by the French government to pay off its debts, and Voltaire joined the consortium, earning perhaps a million livres. "
                "He invested the money cleverly",
                nome="Voltaire"),
            wiki("Charles_Marie_de_La_Condamine",
                "In 1729 La Condamine and his friend Voltaire exploited a loophole in the French government’s lottery, which brought them large profits.",
                nome="Charles Marie de La Condamine"),
            {"url": YALE_LOTERIAS, "titulo": "Voltaire, Casanova, and 18th-Century Lotteries (Yale School of Management, caso 10-030)", "idioma": "en",
             "trecho": "In France, during the 18th century, the writer and philosopher Voltaire, along with mathematician Charles Marie de La Condamine, capitalized on a bond lottery set up by the French government. "
                       "They formed a syndicate, purchasing almost worthless bonds and winning substantial lottery payouts, making Voltaire independently wealthy."},
        ],
    },
    # 12 Casanova, o vendedor de loterias
    {
        "temas_secundarios": ["economia_curiosa", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Casanova, o sedutor, ajudou a criar a loteria do Estado francês e ficou rico vendendo bilhetes. Então rodou a Europa tentando repetir o feito: Frederico, o Grande, não se interessou, e Catarina, a Grande, recusou.",
        "explicacao": (
            "Giacomo Casanova chegou a Paris depois de fugir da prisão dos Piombi, em Veneza, onde tinha sido "
            "trancado por ofensas à religião e à moral. Precisava de um protetor e reencontrou um velho amigo, "
            "Bernis, então ministro das Relações Exteriores da França, que o aconselhou a arranjar um jeito de "
            "levantar dinheiro para o Estado. A ideia foi uma loteria para financiar a Escola Militar. Casanova e "
            "os irmãos Calzabigi foram peças-chave: ele defendeu o projeto em conversas com Madame de Pompadour, com "
            "o matemático d'Alembert e com o intendente da escola. Diferentemente das loterias modernas, nessa o "
            "Estado podia perder, mas os prêmios foram calculados para tornar o prejuízo tão improvável que o lucro "
            "ficava garantido. A loteria funcionou de 1757 a 1836, com interrupções na Revolução. Casanova virou um "
            "dos administradores e um dos melhores vendedores de bilhetes, e fez fortuna depressa. Anos depois, foi "
            "à Inglaterra, em 1763, para vender a ideia ao governo britânico, e então percorreu a Europa de "
            "carruagem, cerca de 7.200 km, tentando repetir o sucesso: o encontro com Frederico, o Grande, não deu "
            "em nada, e Catarina, a Grande, recusou a proposta sem rodeios."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Giacomo_Casanova",
                "Among other exploits, Casanova escaped from the Piombi prison, to which he had been confined by order of the Venetian Council of Ten for offenses against religion and morals, and later helped convince the authorities of the Kingdom of France to establish a state lottery as a source of revenue. [...] "
                "His first task was to find a new patron. "
                "He reconnected with his old friend de Bernis, now the Foreign Minister of France. "
                "Casanova was advised by his patron to find a means of raising funds for the state as a way to gain instant favor. "
                "Casanova promptly became one of the trustees of the first state lottery, and one of its best ticket salesmen. "
                "The enterprise earned him a large fortune quickly. [...] "
                "Casanova traveled to England in 1763, hoping to sell his idea of a state lottery to British officials. [...] "
                "traveled all over Europe, covering about 4,500 miles (7,200 km) by coach over rough roads, and going as far as Moscow and Saint Petersburg [...] "
                "Again, his principal goal was to sell his lottery scheme to other governments and repeat the great success he had with the French government, but a meeting with Frederick the Great bore no fruit and in the surrounding German lands, the same result. "
                "Lacking neither connections nor confidence, Casanova went to Russia and met with Catherine the Great, but she flatly turned down the lottery idea.",
                nome="Giacomo Casanova"),
            wiki("Lottery",
                "Between 1757 and 1836, for a period of about 80 years with some interruption during the French Revolution, the French state ran a profitable Loterie. "
                "The project was born out a series of initiatives to fund the École militaire. "
                "Instrumental to the birth of the Loterie were Giacomo Casanova and the Calzabigi brothers (Giovanni and Ranieri). "
                "Casanova defended the project in a series of conversations with Madame de Pompadour, the French mathematician Jean d'Alembert, Joseph de Pâris Duverney, intendent of the École, and the French minister of foreign affair. "
                "Unlike modern lotteries where the state can never lose, in the French lottery the state could lose, but a wise choice of the payoff made losses so improbable as to ensure a profit for the state.",
                nome="Lottery"),
        ],
    },
    # 13 Thorp, Shannon e o computador escondido no sapato
    {
        "temas_secundarios": ["historia_computacao", "probabilidade"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Em 1961, os matemáticos Edward Thorp e Claude Shannon testaram, no porão de Shannon, um computador escondido no corpo para ganhar na roleta. Thorp o chama de primeiro computador vestível, o que depende da definição.",
        "explicacao": (
            "Thorp ficou famoso por mostrar matematicamente que a vantagem da banca no blackjack podia ser vencida "
            "contando cartas, com cálculos feitos num computador IBM 704. Testou a teoria em cassinos de Nevada com "
            "dinheiro de um jogador profissional, às vezes disfarçado com óculos escuros e barba postiça, e contou "
            "tudo no livro Beat the Dealer, de 1962, que vendeu mais de 700 mil exemplares. Em resposta, os cassinos "
            "passaram a embaralhar bem antes do fim do maço. Quando dava aula no MIT, Thorp conheceu Shannon, e os "
            "dois e a esposa de Shannon, Betty, passaram a ir a Las Vegas nos fins de semana. Entre 1960 e 1961, "
            "Thorp e Shannon desenvolveram juntos um aparelho para a roleta, operado por duas pessoas: uma "
            "observava a roda e a outra recebia sinais sonoros num fone escondido. A versão final foi testada em "
            "junho de 1961 no laboratório que Shannon tinha no porão. Versões do aparelho, escondidas num sapato ou "
            "num maço de cigarros, foram feitas nos anos 1960 e 1970. Desde 1985, usar esse tipo de dispositivo em "
            "cassino é ilegal em Nevada. Quanto ao título de primeiro computador vestível, há outros candidatos, "
            "como um ábaco num anel, e, para computadores de uso geral, ele costuma ir para Steve Mann."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Edward_O._Thorp",
                "Thorp is the author of Beat the Dealer, which mathematically proved that the house advantage in blackjack could be overcome by card counting. "
                "He also developed and applied effective hedge fund techniques in the financial markets, and collaborated with Claude Shannon in creating the first wearable computer. [...] "
                "Thorp used the IBM 704 as a research tool in order to investigate the probabilities of winning while developing his blackjack game theory [...] "
                "Thorp started his applied research using $10,000, with Manny Kimmel, a wealthy professional gambler and former bookmaker, providing the venture capital. [...] "
                "As a countermeasure to his methods, casinos now shuffle long before the end of the deck is reached. "
                "During his Las Vegas casino visits Thorp frequently used disguises such as wraparound glasses and false beards. [...] "
                "he wrote the book Beat the Dealer in 1962 (substantially updated in 1966), widely considered the original guide to card counting, which sold over 700,000 copies [...] "
                "In addition, Thorp, while a professor of mathematics at MIT, met Claude Shannon, and took him and his wife Betty Shannon as partners on weekend forays to Las Vegas to play roulette and blackjack, at which Thorp was very successful. "
                "His team's roulette play was the first instance of using a wearable computer in a casino [...] something which is now illegal, as of May 30, 1985, when the Nevada devices law came into effect as an emergency measure targeting blackjack and roulette devices. "
                "The wearable computer was co-developed with Claude Shannon between 1960 and 1961. "
                "It relied on a pair of operators, where one would watch the wheel and use his toe to input the cadence of the wheel, and the other would receive a message in the form of musical tones through a hidden earpiece. [...] "
                "The final operating version of the device was tested in Shannon's home lab at his basement in June 1961.",
                nome="Edward O. Thorp"),
            wiki("Wearable_computer",
                "the first wearable computer could be as early as the first abacus on a necklace, a 16th-century abacus ring, a wristwatch and 'finger-watch' owned by Queen Elizabeth I of England, or the covert timing devices hidden in shoes to cheat at roulette by Thorp and Shannon in the 1960s and 1970s. "
                "However, a general-purpose computer is not merely a time-keeping or calculating device, but rather a user-programmable item for arbitrary complex algorithms, interfacing, and data management. "
                "By this definition, the wearable computer was invented by Steve Mann [...] "
                "In 1961, mathematicians Edward O. Thorp and Claude Shannon built some computerized timing devices to help them win a game of roulette. "
                "One such timer was concealed in a shoe and another in a pack of cigarettes. "
                "Various versions of this apparatus were built in the 1960s and 1970s. "
                "Thorp refers to himself as the inventor of the first \"wearable compute",
                nome="Wearable computer"),
        ],
    },
    # 14 as frutas do caça-níquel vieram do chiclete
    {
        "temas_secundarios": ["invencoes", "leis_julgamentos"],
        "tipos_espanto": ["origem_inesperada"],
        "gancho": "As frutas dos caça-níqueis vêm de chicletes. Uma versão antiga da máquina podia vender goma de mascar com sabor de fruta, e os rolos ganharam limões, cerejas e laranjas. O símbolo BAR era a figura de um tablete da marca.",
        "explicacao": (
            "O caça-níquel moderno descende da Liberty Bell, criada por Charles Fey, de San Francisco, em algum "
            "momento entre 1887 e 1895. Tinha três rolos e só cinco símbolos: ferraduras, ouros, espadas, copas e "
            "um sino, o Sino da Liberdade que dava nome à máquina. Trocar as cartas de baralho das máquinas "
            "anteriores por poucos símbolos facilitava ler as combinações e permitiu um mecanismo de pagamento "
            "automático. Três sinos pagavam o maior prêmio, dez moedas de 5 centavos. Depois de alguns anos, a "
            "máquina foi proibida na Califórnia, mas virou um sucesso tão grande que foi copiada por vários "
            "fabricantes. Herbert Mills lançou sua versão em 1907 e, mais tarde, uma parecida, a Operator's Bell, "
            "que podia vir com um acessório para vender chiclete. Como o chiclete tinha sabor de fruta, os rolos "
            "passaram a mostrar limões, cerejas, laranjas e ameixas. O sino continuou, e entrou a figura de um "
            "tablete de Bell-Fruit Gum, a origem do símbolo BAR. A combinação agradou e foi adotada por outros "
            "fabricantes. Na época, oferecer prêmios em comida era um jeito comum de escapar das leis contra jogos "
            "em vários estados americanos, e por isso a Justiça desconfiava de máquinas de vender chiclete."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Slot_machine",
            "At some time between 1887 and 1895, Charles Fey of San Francisco, California, devised a much simpler automatic mechanism with three spinning reels containing a total of five symbols: horseshoes, diamonds, spades, hearts and a Liberty Bell; the bell gave the machine its name. "
            "By replacing ten cards with five symbols and using three reels instead of five drums, the complexity of reading a win was considerably reduced, allowing Fey to design an effective automatic payout mechanism. "
            "Three bells in a row produced the biggest payoff, ten nickels (50¢). "
            "Liberty Bell was a huge success and spawned a thriving mechanical gaming device industry. "
            "After a few years, the devices were banned in California, but Fey still could not keep up with the demand for them elsewhere. "
            "The Liberty Bell machine was so popular that it was copied by many slot machine manufacturers. "
            "The first of these, also called the \"Liberty Bell\", was produced by the manufacturer Herbert Mills in 1907. [...] "
            "Later, a similar machine called the Operator's Bell was produced that included the option of adding a gum-vending attachment. "
            "As the gum offered was fruit-flavored, fruit symbols were placed on the reels: lemons, cherries, oranges and plums. "
            "A bell was retained, and a picture of a stick of Bell-Fruit Gum, the origin of the bar symbol, was also present. "
            "This set of symbols proved highly popular and was used by other companies that began to make their own slot machines: Caille, Watling, Jennings and Pace. "
            "A commonly used technique to avoid gambling laws in several states was to award food prizes. "
            "For this reason, several gumball and other vending machines were regarded with mistrust by the courts.",
            nome="Slot machine")],
    },
    # 15 o cassino que salvou os Grimaldi
    {
        "temas_secundarios": ["fronteiras_paises", "economia_curiosa"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "O cassino de Monte Carlo foi criado para salvar da falência a família que reina em Mônaco. O nome Monte Carlo foi escolhido para o bairro do cassino em honra ao príncipe Carlos. E os monegascos são proibidos de jogar lá.",
        "explicacao": (
            "A ideia foi da princesa Carolina, mulher do príncipe Florestan. As finanças dos Grimaldi pioraram de "
            "vez em 1848, quando as cidades de Menton e Roquebrune se declararam independentes de Mônaco e "
            "deixaram de pagar os impostos sobre azeite e frutas. Um primeiro cassino abriu em 1856, mas o lugar "
            "era improvável para um balneário: faltavam estradas até Nice e hospedagem confortável, e vinha muito "
            "menos gente que o previsto. Carolina então foi atrás de François Blanc, que dirigia o cassino de Bad "
            "Homburg, na Alemanha. Ele resistiu, e a princesa chegou a dizer à esposa dele que o clima ameno faria "
            "bem à sua saúde frágil. Blanc assumiu em 1863 e, por insistência dele, a área do cassino, conhecida "
            "como Les Spelugues, \"as cavernas\", ganhou um nome mais atraente: Monte Carlo, em homenagem ao "
            "príncipe Carlos. Blanc também emprestou dinheiro ao governo francês para concluir a Ópera de Paris, e "
            "foi assim que conheceu o arquiteto Charles Garnier, que depois ampliou o cassino. Até recentemente, o "
            "cassino foi a principal fonte de renda dos Grimaldi e da economia de Mônaco. Por iniciativa da "
            "própria Carolina, e por razões morais, os cidadãos de Mônaco não podem entrar nas salas de jogo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Monte_Carlo_Casino",
            "Citizens of Monaco are forbidden to enter the gaming rooms of the casino. "
            "The rule banning all Monégasques from gambling or working at the casino was an initiative of Princess Caroline, the de facto regent of Monaco, who amended the rules on moral grounds. [...] "
            "The idea of opening a gambling casino in Monaco originated with Princess Caroline, the shrewd, business-minded spouse of Prince Florestan. "
            "Revenues from the proposed venture were supposed to save the House of Grimaldi from bankruptcy. "
            "The ruling family's persistent financial problems became especially acute after the loss of tax revenue from two breakaway towns, Menton and Roquebrune, which declared independence from Monaco in 1848 and refused to pay taxes on olive oil and fruit imposed by the Grimaldis. [...] "
            "Aubert and Langlois opened the first casino on 14 December 1856 in Villa Bellevu. [...] "
            "In the late 1850s, Monaco was an unlikely place for a resort to succeed. "
            "The lack of roads needed to connect Monaco to Nice and the rest of Europe, and the absence of comfortable accommodations for visitors, as well as the concessionaires' failure to publicize the new resort, resulted in far fewer customers than was originally anticipated. [...] "
            "Frustrated, she dispatched her private secretary M. Eyneaud to Germany, hoping to recruit François Blanc, a French entrepreneur and operator of the Bad Homburg casino. "
            "Blanc initially declined the offer, and it took a lot of time and persuasion on the part of Princess Caroline to convince him to move to Monaco. "
            "Princess Caroline even appealed to Madame Blanc, whom she befriended during her first visit to Bad Homburg, with a suggestion that Monaco's mild climate would be good for Madame Blanc's ill health. "
            "In 1863, François Blanc finally agreed to take over Monaco's casino business. [...] "
            "On Blanc's insistence, the Spelugues area where the gambling complex was located was renamed to make it sound more attractive to casino visitors. "
            "A few suggestions were considered, and the name Monte Carlo was chosen in Prince Charles' honor. [...] "
            "François Blanc knew Garnier because Blanc had provided a loan of at least 4.9 million gold francs to the cash-strapped government of the French Third Republic so that the opera house, which had been started in 1861, could be completed. [...] "
            "Until recently, the Casino de Monte-Carlo has been the primary source of income for the House of Grimaldi and the Monegasque economy.",
            nome="Monte Carlo Casino")],
    },
    # 16 pachinko: a brecha das fichas-prêmio
    {
        "temas_secundarios": ["leis_julgamentos", "economia_curiosa"],
        "tipos_espanto": ["engenhosidade", "escala_absurda"],
        "gancho": "No Japão, jogar a dinheiro é ilegal, mas o pachinko prospera por uma brecha: as bolinhas ganhas viram fichas-prêmio, que se \"vendem\" num guichê separado. Em 2015, faturou mais que Macau, Las Vegas e Singapura juntas.",
        "explicacao": (
            "A máquina de pachinko lembra um fliperama vertical. Bolinhas de aço de 11 milímetros, alugadas pela "
            "casa, quicam entre pinos de latão, e as que caem em certos copinhos rendem mais bolinhas. O jogo surgiu "
            "nos anos 1920 como brinquedo infantil, inspirado num jogo americano, virou passatempo de adultos em "
            "Nagoya por volta de 1930, e a primeira casa comercial abriu ali em 1948. Como as apostas em dinheiro "
            "são proibidas, as bolinhas não podem ser trocadas por dinheiro no salão, nem levadas embora. Podem, "
            "porém, virar fichas de \"prêmio especial\", que o jogador vende num guichê fora do salão. Esse "
            "comprador, em tese independente, mas muitas vezes do mesmo dono, revende as fichas ao salão pelo mesmo "
            "preço, mais uma pequena comissão, sem violar a letra da lei. A escala impressiona: em 1999, a receita "
            "dos salões equivalia a 5,6% do PIB japonês, conta que inclui o dinheiro devolvido aos jogadores, "
            "estimado em cerca de 85% do que eles gastam. O setor vem encolhendo: em 2022, o Japão tinha 7.665 "
            "salões, menos da metade dos 18.244 de 1997."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Pachinko",
            "Gambling for cash is illegal de jure in Japan, but the widespread popularity of low-stakes pachinko in Japanese society has enabled a specific legal loophole allowing it to exist. "
            "Pachinko balls won from games cannot be exchanged directly for money in the parlor, nor can they be removed from the premises or exchanged with other parlors. "
            "However, they can be legally traded to the parlor for so-called \"special prize\" tokens (tokushu keihin (特殊景品)), which can in turn be \"sold\" for cash to a separate vendor off-premises. "
            "These vendors (ostensibly independent from, but often owned by, the parlor owner) then sell the tokens back to the parlor at the same price paid for them—plus a small commission, creating a cash profit—without technically violating the law. [...] "
            "In 1999, sales and revenue from pachinko parlors contributed 5.6% of Japan's ¥500 trillion GDP [...] "
            "However, the sales amount of these pachinko parlors is calculated based on the total amount that customers rented pachinko balls from pachinko parlors. "
            "It is said that on average, about 85% of the money spent by customers in pachinko parlors is returned to the customers [...] "
            "In 2015, Japan's pachinko market generated more gambling revenue than that of Macau, Las Vegas, and Singapore combined. [...] "
            "and the number of pachinko parlors in 2022 was 7,665, less than half of the 18,244 in 1997, when the number of parlors was at its peak. [...] "
            "A pachinko machine resembles a vertical pinball machine, but is different from Western pinball in several ways. "
            "It uses small (11-millimetre (2⁄5 in) diameter) steel balls, which the owner (usually a \"pachinko parlor\", featuring many individual games in rows) rents to the player [...] "
            "The playing field is populated by numerous brass pins, several small cups into which the player hopes the ball will fall [...] "
            "A ball that enters a catcher triggers a payout, in which a number of balls are dropped into a tray at the front of the machine. [...] "
            "Pachinko machines were first built during the 1920s as a children's toy called the \"Corinth game\" (コリントゲーム, korinto gēmu), based on and named after the American \"Corinthian bagatelle\". [...] "
            "It emerged as an adult pastime in Nagoya around 1930, and spread from there. [...] "
            "the first commercial parlor was opened in Nagoya in 1948.",
            nome="Pachinko")],
    },
]
