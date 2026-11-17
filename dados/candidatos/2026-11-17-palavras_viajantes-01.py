LOTE = "2026-11-17-palavras_viajantes-01"
AREA = "linguas"
TEMA = "palavras_viajantes"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None):
    return {"url": W + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": "en", "trecho": trecho}


CANDIDATOS = [
    # 1 laranja
    {
        "temas_secundarios": ["comercio_rotas", "asia_antiga"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "A palavra 'laranja' nasceu numa língua do sul da Índia e passou pelo sânscrito, pelo persa e pelo árabe. No caminho, o italiano e o francês perderam o 'n' do começo.",
        "explicacao": (
            "A origem mais distante da palavra está numa língua dravídica, do sul da Índia, possivelmente o tâmil "
            "nāram ou o télugo nāriṃja. Dali ela entrou no sânscrito como nāraṅgaḥ, 'laranjeira', depois no persa "
            "como nārang e no árabe como nāranj. Foi pelo árabe que a palavra chegou às línguas da Europa, junto "
            "com a fruta. Em algumas delas aconteceu uma confusão curiosa, chamada pelos linguistas de "
            "rebracketing: o 'n' inicial foi entendido como parte do artigo que vinha antes, e acabou "
            "desaparecendo. Foi o que ocorreu no italiano e no francês, de onde veio o inglês orange. O espanhol "
            "naranja manteve o 'n'. Em inglês, aliás, a palavra veio antes da cor: o nome da cor laranja foi "
            "tirado da fruta, e antes disso os ingleses falavam em 'amarelo-avermelhado'."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Orange_(word)",
            "The earliest uses of the word in English refer to the fruit, and the color was later named after the fruit. "
            "Before the English-speaking world was exposed to the fruit, the color was referred to as \"yellow-red\" (geoluread in Old English) or \"red-yellow\". [...] "
            "The word ultimately derives from a Dravidian language – possibly Tamil நாரம் nāram or Telugu నారింజ nāriṃja — via Sanskrit नारङ्ग nāraṅgaḥ \"orange tree\". "
            "From there the word entered Persian نارنگ nārang and then Arabic نارنج nāranj. "
            "The initial n was lost through rebracketing in Italian and French, though some varieties of Arabic lost the n earlier. Compare Spanish cognate naranja with initial n",
            "Orange (word)")],
    },
    # 2 chá
    {
        "temas_secundarios": ["cafe_cha_cacau", "grandes_navegacoes", "comercio_rotas"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "Dizemos 'chá' e os ingleses dizem 'tea' porque a palavra saiu da China por caminhos diferentes: os portugueses a pegaram em Macau, e os holandeses, de outro dialeto.",
        "explicacao": (
            "Quase todas as palavras para chá no mundo vêm de pronúncias chinesas do mesmo caractere, e caem em três "
            "famílias: te, cha e chai. Qual delas cada povo usa revela por onde o chá chegou. Os portugueses foram "
            "os primeiros europeus a importar a planta em grande quantidade e, por volta da década de 1550, "
            "tomaram emprestada a palavra 'chá' do cantonês, pelos seus entrepostos no sul da China, sobretudo "
            "Macau. A forma 'tea' chegou ao inglês no século XVII pelos holandeses, que a pegaram do malaio 'teh' "
            "ou da pronúncia 'tê' do chinês min. Já 'chai' é a forma que seguiu por terra pela Rota da Seda até a "
            "Ásia Central, ganhou uma terminação persa e entrou no inglês pelo hindustâni. Em geral, regiões que "
            "receberam o chá por terra dizem algo como 'cha', e muitas que o receberam pelo mar dizem algo como 'te'."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Etymology_of_tea",
            "broad groups: te, cha and chai, present in English as tea, cha or char, and chai. [...] "
            "The more common tea form arrived in the 17th century via the Dutch, who acquired it either indirectly from teh in Malay, or directly from the tê pronunciation in Min Chinese. "
            "The third form chai (used in English almost solely to refer to Indian-style spiced tea) originated from the Chinese pronunciation of cha, "
            "which travelled overland to Central Asia via the Silk Road where it picked up a Persian ending yi, and entered English via Hindustani in the 20th century. [...] "
            "pronounce it along the lines of 'cha', whilst most global maritime regions with a history of sea trade with certain southeast regions of Imperial China (such as Europe), pronounce it like 'teh'. [...] "
            "Portuguese traders were the first Europeans to import the herb in large amounts. "
            "The Portuguese borrowed their word for tea (chá) from Cantonese in the 1550s via their trading posts in the south of China, especially Macau.",
            "Etymology of tea")],
    },
    # 3 pineapple
    {
        "temas_secundarios": ["domesticacao", "povos_indigenas"],
        "tipos_espanto": ["origem_inesperada"],
        "gancho": "Em inglês, o abacaxi se chama 'pineapple', 'maçã de pinheiro': os europeus o compararam a uma pinha, e na época 'apple' servia para qualquer fruta desconhecida.",
        "explicacao": (
            "O abacaxi é nativo da América do Sul e já era cultivado e comido pelos tupinambás, perto do atual Rio "
            "de Janeiro, quando os europeus chegaram. Os espanhóis o chamaram de piña, pela semelhança com a pinha "
            "do pinheiro, e Colombo o levou para a Espanha como piña de Indes. Em inglês, 'pine apple' já existia "
            "desde o século XIV, mas designava a própria pinha. Na época, 'apple' servia para qualquer fruta de "
            "árvore desconhecida que fosse firme e arredondada. Em 1624, o explorador John Smith usou 'pine apple' "
            "para a fruta tropical, e o nome pegou. Enquanto isso, um texto francês traduzido para o inglês em 1568 "
            "já descrevia a fruta com uma palavra tupi, 'nanas', a mesma raiz de 'ananás'."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Pineapple",
            "The pineapple is native to South America, where it has been cultivated for many centuries. [...] "
            "The word pine apple was used by English explorer John Smith referring to the tropical fruit in 1624. "
            "The word apple was given during his time for any unfamiliar tree fruit that had a firm, round shape; a pine apple first referred to the cone (fruit) of the pine tree in the 14th century. [...] "
            "The first reference in English to the pineapple fruit was the 1568 translation from the French of André Thevet's The New Found World, or Antarctike "
            "where he refers to a Hoyriri, a fruit cultivated and eaten by the Tupinambá people, living near modern Rio de Janeiro, and now believed to be a pineapple. "
            "Later in the same English translation, Thavet described the fruit as a \"Nana made in the manner of a Pine apple\", where he used another Tupi word nanas. [...] "
            "Columbus brought the plant back to Spain and called it piña de Indes")],
    },
    # 4 caju
    {
        "temas_secundarios": ["povos_indigenas", "grandes_navegacoes", "comida_brasileira"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "A 'cashew nut' que se vende no mundo inteiro tem nome brasileiro: vem de 'caju', palavra que o português tirou do tupi 'acajú'.",
        "explicacao": (
            "O cajueiro é nativo da América do Sul tropical. Os exploradores portugueses o conheceram no século XVI "
            "e o levaram para a Índia e outras regiões tropicais do mundo, que hoje estão entre os grandes "
            "produtores. Junto com a planta viajou o nome. O inglês cashew vem do português 'caju', também dito "
            "'acaju', que por sua vez vem da palavra tupi 'acajú', traduzida como 'noz que se produz sozinha'. "
            "Assim, quando um americano ou um indiano compra cashews, está usando, sem saber, uma palavra indígena "
            "brasileira que passou pelo português. A castanha, aliás, não é a parte mais óbvia da planta: a parte "
            "carnuda que no Brasil se chama de caju é o pedúnculo, e o fruto verdadeiro é a castanha presa embaixo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Cashew",
            "It is the source of the cashew nut and the cashew apple. [...] "
            "Cashews are native to tropical South America. Portuguese explorers encountered them in the 16th century and spread them to India and other tropical regions of the world. [...] "
            "The English name derives from the Portuguese name for the fruit of the cashew tree: Caju (Portuguese pronunciation: [kaˈʒu]), also known as acaju, "
            "which itself is from the Tupi word acajú, literally meaning \"nut that produces itself\".")],
    },
    # 5 mandarim
    {
        "temas_secundarios": ["asia_antiga", "grandes_navegacoes"],
        "tipos_espanto": ["contraintuitivo", "origem_inesperada"],
        "gancho": "'Mandarim', nome dos antigos funcionários chineses e da língua oficial da China, não é palavra chinesa: chegou pelo português, vinda do malaio e do sânscrito.",
        "explicacao": (
            "Os mandarins eram os funcionários do império chinês, escolhidos por exames, e o nome acabou designando "
            "também a língua usada por eles. Mas a palavra não é chinesa. O inglês mandarin vem do português "
            "'mandarim', que aparece em alguns dos primeiros relatos portugueses sobre a China, como cartas de "
            "sobreviventes presos da embaixada de Tomé Pires, provavelmente escritas em 1524. Já se pensou que "
            "viesse do verbo português 'mandar', mas os dicionários modernos concordam que os portugueses a "
            "pegaram do malaio 'menteri', que por sua vez vem do sânscrito 'mantrin', 'conselheiro' ou 'ministro'. "
            "Mantrin deriva de mantra, 'texto sagrado' ou, ao pé da letra, 'instrumento do pensamento'. Ou seja: o "
            "nome dos sábios burocratas da China veio da Índia, passou pela Malásia e foi espalhado por "
            "navegadores portugueses."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Mandarin_(bureaucrat)",
            "Modern dictionaries, however, agree that the Portuguese borrowed it from the Malay menteri (in Jawi: منتري, [ˈməntəri]), "
            "which is borrowed in turn from the Sanskrit mantrin (Devanagari: म॒न्त्रिन्, meaning counselor or minister), "
            "an agent noun formed from mantra (मन्त्र 'sacred text' or etymologically lit. 'instrument of thought') [...] "
            "appointed through the imperial examination system. [...] "
            "The English term comes from the Portuguese mandarim [...] "
            "The Portuguese word was used in one of the earliest Portuguese reports about China: letters from the imprisoned survivors of the Tomé Pires embassy, most likely written in 1524",
            "Mandarin (bureaucrat)")],
    },
    # 6 arigatō
    {
        "temas_secundarios": ["asia_antiga", "grandes_navegacoes"],
        "tipos_espanto": ["mito_desmentido"],
        "gancho": "O japonês 'arigatō' não vem do português 'obrigado'. A semelhança é coincidência, mas 'pan' (pão) é mesmo herança de missionários portugueses.",
        "explicacao": (
            "É comum ouvir que os japoneses aprenderam a dizer 'obrigado' com os portugueses, que chegaram ao "
            "Japão no século XVI. As evidências mostram outra coisa: 'arigatō' tem origem puramente japonesa. Ela "
            "é uma forma desgastada de 'arigataku', que vem do adjetivo antigo 'arigatashi', composto de 'ari' "
            "(existir) e 'katashi' (difícil), algo como 'isso é raro'. E há registros de 'arigatashi' em textos "
            "muito anteriores, como a antologia poética Man'yōshū. Os portugueses deixaram, sim, outras palavras "
            "no japonês. A mais conhecida é 'pan', pão, introduzida por missionários portugueses e muitas vezes "
            "atribuída por engano ao espanhol ou ao francês. 'Arigatō' e 'obrigado' são o que os linguistas chamam "
            "de falsos cognatos: parecidas e com o mesmo sentido, mas sem parentesco."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("List_of_Japanese_words_of_Portuguese_origin",
            "pan ja:パン bread pão pão bread Often wrongly connected to the Spanish pan or the French pain, both with the same meaning and the same Latinate origin. "
            "The word was introduced into Japan by Portuguese missionaries. [...] "
            "It is often suggested that the Japanese word arigatō derives from the Portuguese obrigado, both of which mean \"Thank you\", "
            "but evidence indicates arigatō has a purely Japanese origin, so these two words are false cognates. "
            "Arigatō is an \"u\"-sound change of arigataku. In turn, arigataku is the adverbial form of an adjective arigatai, from older arigatashi, itself a compound of ari + katashi. "
            "Written records of arigatashi exist dating back to the Man'yōshū",
            "List of Japanese words of Portuguese origin")],
    },
    # 7 azul
    {
        "temas_secundarios": ["minerais_rochas", "pigmentos"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "A palavra 'azul' é o nome de uma pedra: vem do persa 'lāžward', o lápis-lazúli, a mesma raiz do inglês 'azure'.",
        "explicacao": (
            "O lápis-lazúli é uma rocha de um azul intenso, valorizada como pedra semipreciosa desde a "
            "Antiguidade justamente pela cor. É formada sobretudo pelo mineral lazurita, com pontinhos de pirita e "
            "outros minerais. O nome da pedra vem da palavra persa para ela, 'lāžward'. Essa mesma palavra deu "
            "origem ao nome da cor em várias línguas, entre elas o português e o espanhol 'azul' e o inglês "
            "'azure'. Ou seja, quando dizemos que o céu é azul, estamos, pela origem da palavra, comparando-o a uma "
            "pedra preciosa da Ásia Central. É um caso em que um objeto raro e valioso emprestou o nome a uma cor "
            "inteira, como aconteceu também com a laranja e a cor laranja."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Lapis_lazuli",
            "Lapis lazuli (UK: ; US: ) is a deep-blue metamorphic rock used as a semi-precious stone that has been prized since antiquity for its intense color. "
            "Its name originates from the Persian word for the gem, lāžward, and serves as the root for the word for \"blue\" in several languages, including Spanish and Portuguese azul and English azure. "
            "Lapis lazuli is a rock composed primarily of the minerals lazurite, pyrite, diopside, and",
            "Lapis lazuli")],
    },
    # 8 açúcar
    {
        "temas_secundarios": ["mundo_islamico_medieval", "comercio_rotas"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "'Açúcar', 'sugar', 'sucre' e 'Zucker' contam a mesma viagem: a palavra saiu do sânscrito, passou pelo persa e pelo árabe e entrou na Europa junto com o produto.",
        "explicacao": (
            "A história da palavra acompanha a do produto. No sânscrito, 'śarkarā' significava açúcar moído ou "
            "cristalizado. Dali vieram o persa 'shakar' e o árabe 'sukkar'. Foram os árabes que introduziram o "
            "açúcar na Europa, pela Sicília e pela Península Ibérica, e a palavra árabe foi emprestada pelo latim "
            "medieval como 'succarum'. Do latim vieram o francês antigo 'sucre', no século XII, e o inglês "
            "'sugar'. O português 'açúcar' conserva até o 'a' inicial, que vem do artigo árabe, sinal de que a "
            "palavra chegou à península diretamente dos árabes. A mesma família tem um parente doméstico: "
            "'jagra', um açúcar mascavo feito de seiva de palmeira ou de cana, chegou ao inglês como 'jaggery' "
            "pelo português."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Sugar",
            "The etymology of sugar reflects the commodity's spread. From Sanskrit śarkarā, meaning \"ground or candied sugar\", came Persian shakar and Arabic sukkar. "
            "The Arabic word was borrowed in Medieval Latin as succarum, whence came the 12th-century Old French sucre and the English sugar. "
            "Sugar was introduced into Europe by the Arabs in Sicily and Spain. "
            "The English word jaggery, a coarse brown sugar made from date palm sap or sugarcane juice, has a similar etymological origin: Portuguese jága")],
    },
    # 9 xeque-mate
    {
        "temas_secundarios": ["jogos_tabuleiro", "mundo_islamico_medieval"],
        "tipos_espanto": ["origem_inesperada"],
        "gancho": "'Xeque-mate' vem do persa 'shāh māt', 'o rei está indefeso'. Há quem leia 'o rei morreu', pelo árabe, mas no xadrez o rei nunca é capturado.",
        "explicacao": (
            "O xadrez chegou à Europa passando pela Pérsia e pelo mundo árabe, e trouxe palavras dessa viagem. "
            "Segundo o dicionário etimológico de Barnhart, 'xeque-mate' é uma alteração da expressão persa 'shāh "
            "māt', que significa 'o rei está indefeso'. 'Xá' é a palavra persa para rei, e 'xeque', o aviso de que o "
            "rei está atacado, tem a mesma origem. A segunda parte tem leituras diferentes. Como o jogo chegou à "
            "Europa pelo mundo árabe, e em árabe 'māta' quer dizer 'morreu', há quem defenda que a expressão "
            "significaria 'o rei morreu'. A leitura persa combina melhor com as regras: no xadrez o rei não é "
            "capturado nem tirado do tabuleiro. O mate acontece quando ele fica sem nenhuma saída."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "consenso_parcial",
        "fontes": [wiki("Checkmate",
            "The term checkmate is, according to the Barnhart Etymological Dictionary, an alteration of the Persian phrase \"shāh māt\" (شاه مات), which means \"the King is helpless\". [...] "
            "Others maintain that it means \"the King is dead\", as chess reached Europe via the Arab world, and Arabic māta (مَاتَ) me")],
    },
    # 10 ketchup
    {
        "temas_secundarios": ["historia_pratos", "asia_antiga"],
        "tipos_espanto": ["origem_inesperada", "misterio_aberto"],
        "gancho": "A palavra 'ketchup' talvez venha de um molho chinês de salmoura de peixe, e não de tomate. A origem ainda é disputada, e há várias teorias.",
        "explicacao": (
            "Hoje ketchup é sinônimo de molho de tomate, mas a origem da palavra é incerta e tem várias teorias "
            "concorrentes. Uma delas, muito citada, diz que o nome vem do chinês da região de Amoy (Xiamen) e "
            "significaria 'molho de tomate'. Essa explicação é considerada uma etimologia popular. Outra teoria "
            "liga a palavra ao hokkien, falado na região de Fujian, no litoral sul da China. Ali, as formas "
            "'kôe-chiap' e 'kê-chiap' designavam a salmoura de peixe ou frutos do mar em conserva, combinando "
            "'comida em conserva' e 'suco'. Se essa teoria estiver certa, o ancestral do ketchup seria algo mais "
            "parecido com um molho de peixe fermentado do que com o molho vermelho das lanchonetes. A troca de "
            "ingredientes ao longo dos séculos não aparece no nome, que viajou intacto."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Ketchup",
            "The etymology of the word ketchup is unclear; there are multiple competing theories: [...] "
            "A folk etymology is that the word came from the Amoy (Xiamen) region of China into English, as a borrowed word 茄汁 (ke² zap¹, Cantonese, meaning \"tomato sauce\" [...] "
            "Another theory is that the word derives from one of two words from Hokkien of the Fujian region of coastal southern China: "
            "kôe-chiap (in the Amoy / Xiamen dialect and Quanzhou dialect) or kê-chiap (in the Zhangzhou dialect). [...] "
            "where it meant the brine of pickled fish or shellfish (膎, 'pickled food' (usually seafood) + 汁, 'juice')")],
    },
    # 11 marmelada
    {
        "temas_secundarios": ["historia_pratos", "grecia_antiga"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "A 'marmalade' de laranja que os britânicos comem no café da manhã tem nome português: vem de 'marmelada', o doce de marmelo.",
        "explicacao": (
            "Para um britânico, marmalade é uma geleia de laranja, um item clássico do café da manhã, e o doce "
            "favorito do urso Paddington. Mas a palavra conta outra história. O inglês marmalade vem do francês "
            "marmelade, que veio do português 'marmelada', e a raiz mais antiga é o grego 'melimēlon', 'maçã "
            "doce'. Não é coincidência que lembre o nosso doce de marmelo. A marmalade original era feita de "
            "marmelo, num doce espesso parecido com a marmelada, e no século XVI era importada pela Inglaterra. A "
            "versão moderna surgiu no século XVIII, quando os escoceses acrescentaram água para deixá-la menos "
            "sólida e a transformaram num item do café da manhã. Daí em diante, a fruta mudou e o nome ficou."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Marmalade",
            "Originally marmalade was made from quince, essentially creating the thick quince cheese. [...] "
            "Modern marmalade was created in the 1700s when the Scots added water to make it less solid. "
            "The Scots made marmalade a breakfast item, and soon after the rest of Britain followed. "
            "The word marmalade in the English language comes from French marmelade which came from the Portuguese word marmelada, "
            "starting with the Greek word melimēlon that means 'sweet apple'. "
            "The preserve has been mentioned in various books and is the fictional character Paddington Bear's favourite food. [...] "
            "In the 1500s, marmalade was made from quince, and was imported to England")],
    },
    # 12 tchau
    {
        "temas_secundarios": ["europa_medieval", "costumes_rituais"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "'Tchau' vem do italiano 'ciao', que vem do veneziano 's-ciào vostro': 'sou seu escravo'. E 'escravo' vem do nome dos eslavos.",
        "explicacao": (
            "O italiano 'ciao' serve tanto para 'oi' quanto para 'tchau', e se espalhou por muitas línguas, "
            "inclusive o português. A origem está no veneziano, numa saudação educada: 's-ciào vostro', ou seja, "
            "'(sou) seu escravo'. Não era uma afirmação literal, e sim uma promessa de boa vontade entre amigos, "
            "parecida com o 'a seu dispor' ou com o antigo 'seu criado'. A ideia é a mesma do latim medieval "
            "'servus', que ainda se usa como cumprimento em partes da Europa Central e Oriental. A palavra "
            "veneziana para escravo veio do latim medieval 'sclavus', emprestado do grego medieval, e está ligada "
            "ao nome dos povos eslavos, porque a maioria dos escravos da época vinha dos Bálcãs. Assim, um simples "
            "'tchau' guarda um pedaço da história da escravidão na Europa medieval."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Ciao",
            "is an informal salutation in the Italian language that is used for both \"hello\" and \"goodbye\". "
            "Originally from the Venetian language, it has entered the vocabulary of English and of many other languages around the world. [...] "
            "The word derives from the Venetian phrase s-ciào vostro or s-ciào su, literally meaning \"(I am) your slave\". "
            "This greeting is analogous to the medieval Latin servus which is still used colloquially in parts of Central/Eastern Europe [...] "
            "The expression was not a literal statement of fact, but rather a perfunctory promise of good will among friends [...] "
            "The Venetian word for \"slave\", s-ciào [ˈstʃao] or s-ciàvo, derives from Medieval Latin sclavus, a loanword from Medieval Greek Σκλάβος, related to the ethnic \"Slavic\", "
            "since most of the slaves at that time came from the Balkan")],
    },
    # 13 algoritmo
    {
        "temas_secundarios": ["algoritmos", "historia_matematica", "mundo_islamico_medieval"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "'Algoritmo' é o nome de uma pessoa: vem da forma latina do nome do sábio persa al-Khwarizmi, que escreveu sobre os algarismos indianos por volta do ano 825.",
        "explicacao": (
            "Por volta do ano 825, o cientista persa al-Khwarizmi escreveu livros sobre o cálculo com os "
            "algarismos indianos, o sistema de numeração posicional que usamos até hoje. No começo do século XII, "
            "esses textos foram traduzidos para o latim e ajudaram a espalhar o sistema indo-arábico pela Europa. "
            "Nas traduções, o nome do autor virou 'Algoritmi' ou 'Alghoarismi', e um dos textos começava com a "
            "frase 'Dixit Algoritmi', ou seja, 'assim falou al-Khwarizmi'. Com o tempo, o nome do autor passou a "
            "designar o próprio método de calcular com esses algarismos. Em inglês, a forma 'algorism' já aparece "
            "por volta de 1225 com esse sentido. Daí veio 'algoritmo', hoje uma sequência de passos para resolver "
            "um problema, presente em todo programa de computador."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Algorithm",
            "Around 825 AD, Persian scientist and polymath al-Khwarizmi wrote kitāb al-ḥisāb al-hindī (\"Book of Indian computation\") [...] "
            "In the early 12th century, Latin translations of these texts involving the Hindu–Arabic numeral system and arithmetic appeared [...] "
            "Here, alghoarismi or algoritmi is the Latinization of Al-Khwarizmi's name; the text starts with the phrase Dixit Algoritmi, or \"Thus spoke Al-Khwarizmi\". "
            "The word algorism in English came to mean the use of place-value notation in calculations; it occurs in the Ancrene Wisse from circa 1225.")],
    },
    # 14 robô
    {
        "temas_secundarios": ["ia_robotica", "literatura"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "A palavra 'robô' nasceu numa peça de teatro tcheca e vem de 'robota', trabalho forçado: os primeiros robôs da ficção eram, literalmente, servos.",
        "explicacao": (
            "A palavra robô surgiu na peça R.U.R. (Robôs Universais de Rossum), do escritor tcheco Karel Čapek, e "
            "de lá se espalhou para outras línguas, chegando ao inglês em 1923. Na peça, os robôs são "
            "trabalhadores artificiais fabricados em série. O nome não foi escolhido por acaso. Vem do tcheco "
            "'robotník', trabalhador forçado, derivado de 'robota', que quer dizer trabalho forçado, serviço "
            "obrigatório ou labuta. Essa palavra tem parentesco com o eslavo antigo 'rabota', servidão, que vem "
            "de 'rabu', escravo. Ou seja, desde o nome, a ideia de robô carrega a de uma máquina feita para "
            "servir. Muito antes da robótica real, a palavra já trazia a pergunta que a ficção científica "
            "explora até hoje: o que acontece quando os servos artificiais se cansam de servir?"
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Robot",
            "The term robot came from the Czech language in 1923. The word was coined by Czech author Karel Capek, first used in his play R.U.R. (translated as Rossum's Universal Robots). "
            "The term comes from the Czech word robotník ('forced worker'), from robota 'forced labor, compulsory service, drudgery,' from robotiti 'to work, drudge', "
            "from an Old Czech source akin to Old Church Slavonic rabota (работа) 'servitude,' from rabu 'slave'.")],
    },
    # 15 jaguar
    {
        "temas_secundarios": ["povos_indigenas", "comportamento_animal"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "'Jaguar', o nome internacional da onça-pintada, provavelmente vem do tupi-guarani 'yaguara', a 'fera que domina a presa com um salto'.",
        "explicacao": (
            "A onça-pintada é o maior felino das Américas, e seu nome internacional é indígena. A palavra 'jaguar', "
            "usada em inglês e em muitas outras línguas, provavelmente vem do tupi-guarani 'yaguara', traduzido "
            "como 'fera que domina a presa com um salto'. Como 'jaguar' também acabou designando outros animais, "
            "povos indígenas da Guiana chamam a onça de 'jaguareté', com o sufixo 'eté', 'verdadeiro': a fera "
            "verdadeira. O português trocou o caminho: aqui o animal é mais chamado de onça, e essa palavra também "
            "viajou. O inglês 'ounce', nome de um felino pintado, está ligado ao português 'onça', palavra usada "
            "para um gato pintado maior que um lince. É um raro caso de animal cujo nome passou do tupi para o "
            "mundo, enquanto no próprio Brasil prevaleceu outra palavra."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "consenso_parcial",
        "fontes": [wiki("Jaguar",
            "The word \"jaguar\" is possibly derived from the Tupi-Guarani word yaguara meaning 'wild beast that overcomes its prey at a bound'. "
            "Because jaguar also applies to other animals, indigenous peoples in Guyana call it jaguareté, with the added suffix eté, meaning \"true beast\". "
            "\"Onca\" is derived from the Portuguese name onça for a spotted cat that is larger than a lynx; cf. ounce.")],
    },
]
