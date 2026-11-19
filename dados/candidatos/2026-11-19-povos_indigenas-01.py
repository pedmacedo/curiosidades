LOTE = "2026-11-19-povos_indigenas-01"
AREA = "brasil"
TEMA = "povos_indigenas"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


ISA_SANGUE = "https://site-antigo.socioambiental.org/en/print/4283"
ISA_FULNIO = "https://pib.socioambiental.org/pt/Povo:Fulni-ô"
ISA_HIXKARYANA = "https://pib.socioambiental.org/pt/Povo:Hixkaryana"
CENSO = "https://agenciagov.ebc.com.br/noticias/202510/censo-2022-brasil-tem-391-etnias-e-295-linguas-indigenas"


CANDIDATOS = [
    # 1 hixkaryana: a onça comeu o homem
    {
        "temas_secundarios": ["estruturas_linguisticas", "linguas_construidas"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Em hixkaryana, língua indígena do rio Nhamundá, \"toto yonoye kamara\" quer dizer \"a onça comeu o homem\", embora \"toto\" seja homem. O objeto vem antes do verbo e o sujeito, no fim: uma das ordens mais raras do mundo.",
        "explicacao": (
            "A grande maioria das línguas põe o sujeito antes do objeto. Cerca de 45% delas usam a ordem sujeito, objeto e "
            "verbo, como o japonês, e uns 42% usam sujeito, verbo e objeto, como o português. A ordem objeto, verbo e "
            "sujeito está entre as mais raras de todas. O hixkaryana, língua da família caribe falada por cerca de 600 "
            "pessoas às margens do rio Nhamundá, afluente do Amazonas, é um dos poucos exemplos. Na frase \"toto yonoye "
            "kamara\", toto é \"homem\", yonoye é uma forma do verbo \"comer\" e kamara é \"onça\". Mesmo assim, ela "
            "não pode ser lida como \"o homem comeu a onça\": o único sentido possível é \"a onça comeu o homem\". "
            "Quem documentou isso foi o linguista Desmond Derbyshire, que começou a estudar a língua em 1958 com a "
            "mulher, Gracie. O trabalho dele resultou na primeira descrição, na literatura linguística, de uma língua "
            "que usa essa ordem como padrão. A ordem soa tão estranha que foi escolhida para o klingon, a língua "
            "inventada para os alienígenas de Jornada nas Estrelas, justamente para parecer alienígena e "
            "contraintuitiva."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Hixkaryana_language",
                "is a Cariban language spoken by 600 people on the Nhamundá River, a tributary of the Amazon River in Brazil. "
                "It is one of 17 languages that have object–verb–subject word order, initially described by linguist Desmond C. Derbyshire. [...] "
                "The example below, toto yonoye kamara, cannot be given the AVO reading 'the man ate the jaguar'; the OVA reading – 'the jaguar ate the man' – is the only possible one.",
                nome="Hixkaryana language"),
            wiki("Língua_hixkaryana",
                "Aqui está um exemplo: toto yonoye kamara. Traduzido como \"a onça comeu o homem\". "
                "Toto significa \"homem\", yonoye é variação do verbo \"comer\" e kamara quer dizer \"onça\".",
                nome="Língua hixkaryana", idioma="pt"),
            wiki("Word_order",
                "about 45% of the world's languages employ subject–object–verb order (SOV); "
                "about 42% of the world's languages employ subject–verb–object order (SVO); "
                "a smaller fraction of languages employ verb–subject–object (VSO) order; "
                "the remaining three arrangements are rarer: verb–object–subject (VOS) is slightly more common than object–verb–subject (OVS), and object–subject–verb (OSV) is the rarest by a significant margin. [...] "
                "SOV is the order used by the largest number of distinct languages; languages using it include Japanese",
                nome="Word order"),
            wiki("Desmond_C._Derbyshire",
                "Derbyshire's study of the language (as a linguist with the Summer Institute of Linguistics) resulted in the first description in the linguistics literature of a language with this word order as its default.",
                nome="Desmond C. Derbyshire"),
            {"url": ISA_HIXKARYANA, "titulo": "Hixkaryana - Povos Indígenas no Brasil (ISA)", "idioma": "pt",
             "trecho": "O estudo linguístico da língua hixkaryana teve início em 1958 a partir do trabalho do casal do SIL, Desmond e Gracie Derbyshire."},
            wiki("Object–verb–subject_word_order",
                "This sequence was chosen for the constructed language Klingon, a language spoken by the extraterrestrial Klingon race in the fictional universe of the Star Trek series, to make the language sound deliberately alien and counterintuitive.",
                nome="Object–verb–subject word order"),
        ],
    },
    # 2 tukano: casar só com quem fala outra língua
    {
        "temas_secundarios": ["linguas_mundo", "costumes_rituais"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Entre os Tukano, no noroeste da Amazônia, um homem não pode se casar com uma mulher que fale a mesma língua que ele. Por isso, em cada casa convivem várias línguas, e as crianças já crescem multilíngues.",
        "explicacao": (
            "Os Tukano vivem às margens do rio Uaupés e arredores, a maioria na Colômbia e uma parte no Brasil. A "
            "regra que organiza o casamento entre eles se chama exogamia linguística: cada grupo de descendência tem a "
            "sua língua, e um homem precisa buscar esposa num grupo que fale outra, porque casar com alguém da mesma "
            "língua seria visto como uma espécie de incesto. Como as mulheres se mudam para a casa do marido, numa "
            "mesma aldeia se ouvem a língua dos homens, as línguas das mulheres vindas de vários povos vizinhos e uma "
            "língua de comércio regional. A criança cresce ouvindo uma língua do pai, outra da mãe e outras das demais "
            "mulheres da casa. O resultado é que é normal um Tukano falar duas, três ou mais línguas da família tukano, "
            "e trocar de língua no meio de uma conversa é comum. É tão natural que muitos nem sabem dizer de pronto "
            "quantas línguas falam: precisam ser estimulados a listá-las. Nem todos seguem a regra: os Cubeo, por "
            "exemplo, não praticam essa exogamia. No Brasil, o Censo 2022 permitiu declarar até três línguas indígenas "
            "por pessoa e apontou o Alto Rio Negro entre as regiões brasileiras de forte multilinguismo."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Tucano_people",
                "are a group of Indigenous South Americans in the northwestern Amazon, along the Vaupés River and the surrounding area. "
                "They are mostly in Colombia, but some are in Brazil. [...] "
                "The Tucano are multilingual because men must marry outside their language group: no man may have a wife who speaks his language, which would be viewed as a kind of incest. "
                "Men choose women from various neighboring tribes who speak other languages. "
                "Furthermore, on marriage, women move into the men's households or longhouses. "
                "Consequently, in any village several languages are used: the language of the men; the various languages spoken by women who originate from different neighboring tribes; and a widespread regional 'trade' language. "
                "Children are born into the multilingual environment: the child's father speaks one language (considered the Tucano language), the child's mother another, other women with whom the child has daily contact, and perhaps still others. [...] "
                "Multilingualism is taken for granted, and moving from one language to another in the course of a single conversation is very common. [...] "
                "They cannot readily tell an outsider how many languages they speak, and they must be suitably prompted to enumerate the languages that they speak [...] "
                "Members of a linguistic descent group marry outside their own linguistic descent group. "
                "As a result, it is normal for Tucano people to speak two, three, or more Tucanoan languages [...] "
                "Cubeo (the Cubeo do not practice exogamy)",
                nome="Tucano people"),
            wiki("Linguistic_exogamy",
                "Linguistic exogamy is a form of cultural exogamy in which marriage occurs between speakers of different languages. "
                "The custom is common among indigenous groups in the northwest Amazon, such as the Tucano tribes.",
                nome="Exogamy"),
            {"url": CENSO, "titulo": "Orgulho de ser indígena eleva em 28% o registro de etnias e em 8% o de línguas (Agência Gov, via IBGE)", "idioma": "pt",
             "trecho": "Dados do Censo Demográfico 2022 mostram a existência de 391 etnias, povos ou grupos indígenas no Brasil [...] O Censo permitiu a declaração de até três línguas indígenas por pessoa, revelando regiões com forte multilinguismo, como o Alto Rio Negro, o Norte do Pará e o Parque do Xingu."},
        ],
    },
    # 3 munduruku: números só até cinco
    {
        "temas_secundarios": ["teoria_numeros", "aprendizagem_inteligencia"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "A língua dos Munduruku, do Pará, só tem palavras para números até cinco. Mesmo assim, eles fazem contas aproximadas com quantidades bem maiores, e seu jeito de dispor os números intrigou neurocientistas.",
        "explicacao": (
            "Os Munduruku vivem sobretudo no vale do rio Tapajós, no Pará, e uma estimativa de 2014 os contava em 13.755 pessoas. "
            "Sua língua, do tronco tupi, não tem palavras para números acima de cinco, e mesmo as que existem são "
            "menos exatas que \"três\" ou \"quatro\" em português. Isso não os impede de fazer cálculos aproximados "
            "com quantidades maiores, como mostrou um estudo publicado em 2004 na revista Science pelo linguista "
            "Pierre Pica, com o neurocientista Stanislas Dehaene e colegas. Num trabalho publicado em 2008, o grupo "
            "investigou como eles imaginam a escala dos números. Os Munduruku a organizam de forma logarítmica, em "
            "que o que pesa é a proporção entre as quantidades, e não a diferença. Para alguns pesquisadores, isso "
            "sugere que essa intuição é inata, e que a escala linear, com distâncias iguais entre números vizinhos, "
            "precisa ser aprendida com estudo. O caso deles é diferente do de outro povo amazônico, os Pirahã, que "
            "não têm palavras para números específicos. Por isso os dois grupos viraram referência para quem estuda "
            "o que há de universal na noção de número."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Munduruku_people",
                "They had an estimated population in 2014 of 13,755. [...] "
                "Traditionally the Munduruku's territory, called Mundurukânia in the 19th century, was the Tapajós river valley. [...] "
                "The Munduruku language is part of the Tupi language family. [...] "
                "Unlike the Pirahã, the Munduruku have a numeracy system, albeit limited [...] "
                "Pierre Pica was instrumental (in a work done in collaboration with Stanislas Dehaene and Elizabeth Spelke) in revealing the psychophysics and linguistic properties of the Munduruku counting system to the Western world. "
                "The Munduruku have number words up to only five, although each word is not as definite in meaning as number words in English, and the lexical limitation is no obstacle to their making calculations involving larger numbers. "
                "Furthermore, the Munduruku use logarithmic mapping of numbers to assess scales, a point cited as possible evidence for the notion that this kind of numbering is innate, whereas the linear mode has to be acquired by study. [...] "
                "Dehaene, S.; Izard, V.; Spelke, E.; Pica, P. (2008). \"Log or linear Distinct Intuitions of the number scale in Western and Amazonian Indigene Culture\". Science. [...] "
                "Pica, P.; Lemer, C.; Izard, V.; Dehaene, S. (15 October 2004). \"Exact and approximate arithmetic in an Amazonian Indigene Group\". Science.",
                nome="Munduruku people"),
            wiki("Mundurukú_language",
                "Munduruku is a Tupi language spoken by 10,000 people in the Tapajós River basin in north central Brazil. [...] "
                "Munduruku lacks words for numbers above 5.",
                nome="Mundurukú language"),
            wiki("Numerical_cognition",
                "The numeracy of indigenous peoples is studied to identify universal aspects of numerical cognition in humans. "
                "Notable examples include the Pirahã people who have no words for specific numbers and the Munduruku people who only have number words up to five.",
                nome="Numerical cognition"),
        ],
    },
    # 4 pirahã: a língua que desafiaria Chomsky
    {
        "temas_secundarios": ["estruturas_linguisticas", "linguas_mundo"],
        "tipos_espanto": ["misterio_aberto", "contraintuitivo"],
        "gancho": "Segundo o linguista Daniel Everett, o pirahã, falado por poucas centenas de pessoas no Amazonas, não põe uma frase dentro de outra. Se for verdade, abala uma ideia central de Chomsky, e a briga segue aberta.",
        "explicacao": (
            "Os Pirahã vivem às margens do rio Maici, afluente do Amazonas, e a língua deles tem, pelas estimativas, "
            "entre 250 e 380 falantes, quase todos monolíngues. O americano Daniel Everett, que publicou mais de duas "
            "dezenas de artigos e um livro sobre ela, afirma que o pirahã não permite encaixar uma oração dentro de "
            "outra, o que os linguistas chamam de recursão. Não daria para dizer \"a casa do irmão do João\": seria "
            "preciso dizer \"João tem um irmão. Esse irmão tem uma casa\", em duas frases. Para Everett, isso "
            "contraria a gramática universal de Noam Chomsky, segundo a qual todas as línguas mostrariam esse tipo de "
            "estrutura. Muitos linguistas contestam, com exemplos tirados de trabalhos antigos do próprio Everett; ele "
            "responde que interpretou mal aquelas frases quando ainda conhecia pouco a língua. Chomsky, por sua vez, "
            "diz que a recursão é uma capacidade inata que pode aparecer ou não numa língua específica. O debate é "
            "difícil de resolver porque pouquíssimos linguistas têm experiência de campo com o pirahã. A língua "
            "tem outras raridades: pode ser assobiada, cantarolada ou codificada em música, e o falante precisa "
            "indicar no verbo a fonte da informação, se viu, deduziu ou ouviu falar."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Pirahã_language",
                "is the indigenous language of the Pirahã people of Amazonas, Brazil. "
                "The Pirahã live along the Maici River, a tributary of the Amazon River. "
                "Pirahã is estimated to have between 250 and 380 speakers. "
                "It is not in immediate danger of extinction, as its use is vigorous and the Pirahã community is mostly monolingual. [...] "
                "the number of linguists with field experience in Pirahã is very small. [...] "
                "Everett, over the course of more than two dozen papers and one book about the language, has ascribed various surprising features to it, including: [...] "
                "An extremely limited clause structure, not allowing for nested recursive sentences like \"Mary said that John thought that Henry was fired\". [...] "
                "Daniel Everett claims that the absence of recursion in the language, if real, falsifies the basic assumption of modern Chomskyan linguistics. "
                "This claim is contested by many linguists, who claim that recursion has been observed in Pirahã by Daniel Everett himself, while Everett argues that those utterances that superficially seemed recursive to him at first were misinterpretations caused by his earlier lack of familiarity with the language. [...] "
                "Other verbal suffixes indicate that an action is deduced from circumstantial evidence, or based on hearsay. "
                "Unlike in English, in Pirahã speakers must state their source of information: they cannot be ambiguous. [...] "
                "Everett stated that Pirahã cannot say \"John's brother's house\" but must say, \"John has a brother. This brother has a house.\" in two separate sentences. "
                "According to Everett, the statement that Pirahã is a finite language without embedding and without recursion presents a challenge for proposals by Noam Chomsky and others concerning universal grammar—on the grounds that if these proposals are correct, all languages should show evidence of recursive (and similar) grammatical structures. "
                "Chomsky has replied that he considers recursion to be an innate cognitive capacity that is available for use in language but that the capacity may or may not manifest itself in any one particular language. [...] "
                "Everett's observation that the language does not allow recursion has also been vigorously disputed by other linguists, who call attention to data and arguments from Everett's own previous publications [...] "
                "Pirahã can be whistled, hummed, or encoded in music.",
                nome="Pirahã language"),
        ],
    },
    # 5 curare: do veneno de flecha à anestesia
    {
        "temas_secundarios": ["farmacos", "historia_medicina", "amazonia"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "O curare, veneno de flecha de povos indígenas da América do Sul, paralisa a caça, mas a carne pode ser comida sem risco. No século XX, esse mesmo veneno virou peça-chave da anestesia nas cirurgias.",
        "explicacao": (
            "Curare é o nome dado a vários venenos de flecha que povos indígenas das Américas Central e do Sul "
            "preparam, sobretudo para caçar. A palavra vem do caribe falado pelos Macuxi da Guiana. O preparo junta "
            "plantas como o cipó Strychnos toxifera, que são fervidas até virar uma pasta escura, passada em flechas "
            "ou nos dardos de zarabatana. As substâncias do curare bloqueiam os receptores que transmitem o comando "
            "dos nervos aos músculos. A presa atingida morre asfixiada, porque os músculos da respiração deixam de se "
            "contrair. Mas o curare quase não é absorvido pelo intestino, e por isso a carne do animal pode ser "
            "comida com segurança. A pista médica veio de experimentos. Em 1825, o inglês Charles Waterton manteve "
            "viva uma jumenta envenenada com curare, enchendo os pulmões dela com um fole por um corte na traqueia. "
            "Em 1857, Claude Bernard mostrou que o veneno age na junção entre o nervo e o músculo. Em 23 de janeiro "
            "de 1942, num hospital de Montreal, os médicos Griffith e Johnson introduziram formalmente a "
            "tubocurarina, extraída do curare, na prática da anestesia, para relaxar os músculos durante cirurgias. "
            "Com o tempo, ela foi substituída por remédios sintéticos de efeito parecido."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Curare",
                "Curare is a collective term for plant-derived arrow poisons traditionally prepared and used by Indigenous peoples of Central and South America, especially for hunting. "
                "Curare preparations are complex mixtures of alkaloids obtained from numerous plants, principally species of the Menispermaceae and Strychnaceae families, including Chondrodendron tomentosum and Strychnos toxifera. "
                "Traditional preparations are made by boiling plant material and concentrating the liquid into a dark paste that can be applied to arrows or blowgun darts. "
                "Curare alkaloids act as non-depolarizing neuromuscular blockers. "
                "Compounds such as d-tubocurarine and toxiferine competitively block nicotinic acetylcholine receptors at the neuromuscular junction, preventing nerve impulses from activating skeletal muscles. [...] "
                "Curare is ineffective when swallowed because its compounds are poorly absorbed through the gastrointestinal tract, allowing animals killed with curare-poisoned weapons to be eaten safely. [...] "
                "Curare and its derivatives subsequently became widely used to produce muscle relaxation during medical and surgical procedures, although d-tubocurarine was later largely superseded by synthetic neuromuscular blockers such as pancuronium and rocuronium. [...] "
                "The word 'curare' is derived from wurari, from the Carib language of the Macusi of Guyana. [...] "
                "The prey was shot by arrows or blowgun darts dipped in curare, leading to asphyxiation owing to the inability of the victim's respiratory muscles to contract. [...] "
                "In 1825, Charles Waterton described a classical experiment in which he kept a curarized female donkey alive by artificial respiration with a bellows through a tracheostomy. [...] "
                "In 1857, Claude Bernard (1813–1878) published the results of his experiments in which he demonstrated that the mechanism of action of curare was a result of interference in the conduction of nerve impulses from the motor nerve to the skeletal muscle, and that this interference occurred at the neuromuscular junction.",
                nome="Curare"),
            wiki("Tubocurarine_chloride",
                "Griffith and Johnson are credited with pioneering the formal clinical introduction of tubocurarine as an adjunct to anesthetic practice on 23 January 1942, at the Montreal Homeopathic Hospital.",
                nome="Tubocurarine chloride"),
        ],
    },
    # 6 mandioca brava, tipiti e tucupi
    {
        "temas_secundarios": ["comida_brasileira", "alimentos_perigosos", "domesticacao"],
        "tipos_espanto": ["engenhosidade", "escala_absurda"],
        "gancho": "A mandioca, provavelmente domesticada no Brasil e base da comida de 800 milhões de pessoas, pode ter muito cianeto. Para comer a brava, indígenas criaram o tipiti, que espreme o veneno. Fervido, o caldo vira tucupi.",
        "explicacao": (
            "Os parentes selvagens da mandioca se concentram no centro-oeste do Brasil, onde ela foi provavelmente "
            "domesticada há no máximo 10 mil anos. No século XVI, comerciantes portugueses a levaram do Brasil para a "
            "África, e hoje a Nigéria é a maior produtora. O próprio nome vem do tupi-guarani. A raiz, porém, tem "
            "uma armadilha química: guarda substâncias que, quebradas por uma enzima da própria planta, soltam ácido "
            "cianídrico. As variedades mansas podem ter só 20 miligramas de cianeto por quilo de raiz fresca; as "
            "bravas, até 1.000. Para aproveitá-las, a massa ralada precisa perder o líquido venenoso. A ferramenta "
            "que povos indígenas e ribeirinhos do Brasil usam para isso é o tipiti, um tubo de palha trançada. Na "
            "versão mais elaborada, a massa vai dentro dele e pesos o esticam, espremendo o caldo. Hans Staden já o "
            "descreveu, em livro de 1557, no dia a dia dos tupinambás de Ubatuba. Nem o caldo se perde: cozido, ele "
            "perde o veneno, fermenta de 3 a 5 dias e vira o tucupi, base do pato no tucupi e do tacacá."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Cassava",
                "Wild populations of M. esculenta subspecies flabellifolia, shown to be the progenitor of domesticated cassava, are centered in west-central Brazil, where it was likely first domesticated no more than 10,000 years ago. [...] "
                "Portuguese traders introduced cassava to Africa from Brazil in the 16th century. [...] "
                "The largest producer is Nigeria [...] "
                "The generic name Manihot and the common name \"manioc\" both derive from the Guarani (Tupi) name mandioca or manioca for the plant. [...] "
                "Worldwide, 800 million people depend on cassava as their primary food staple. [...] "
                "Cassava roots, peels, and leaves are dangerous to eat raw because they contain linamarin and lotaustralin, which are toxic cyanogenic glycosides. "
                "These are decomposed by the cassava enzyme linamarase, releasing poisonous hydrogen cyanide. [...] "
                "Sweet cultivars can contain as little as 20 milligrams of cyanide per kilogram of fresh roots, whereas bitter cultivars may contain as much as 1000 milligrams per kilogram.",
                nome="Cassava"),
            wiki("Tipiti",
                "Tipiti é uma espécie de prensa ou espremedor de palha trançada usado para escorrer e secar raízes, normalmente mandioca. "
                "O objeto é utilizado principalmente por povos indígenas e ribeirinhos do Brasil, especialmente da região amazônica. [...] "
                "O tipiti é mencionado no livro de Hans Staden, publicado em 1557. "
                "O objeto foi mencionado como parte do cotidiano tupinambá, da aldeia de Ubatuba. [...] "
                "O tipiti mais avançado, o tipiti de peso, recebia a mandioca ralada em seu interior e era esticado com auxílio de pesos. "
                "Na prensagem da massa da mandioca escorria um líquido que continha uma substância venenosa, o ácido cianídrico, e era chamado maniaca. "
                "Quando ele era fervido, recebia o nome de tucupi.",
                nome="Tipiti", idioma="pt"),
            wiki("Tucupi",
                "Inicialmente venenoso devido à presença do ácido cianídrico, o líquido é cozido (processo que elimina o veneno) e fermentado de 3 a 5 dias para, então, ser usado como molho na culinária. [...] "
                "o pato no tucupi é previamente assado e após destrinchado, é levado a uma fervura leve num molho de tucupi [...] "
                "Servido numa cuia natural, o tucupi fervente é derramado sobre uma goma feita a partir do amido da mandioca.",
                nome="Tucupi", idioma="pt"),
        ],
    },
    # 7 o Homem do Buraco
    {
        "temas_secundarios": ["amazonia"],
        "tipos_espanto": ["historia_humana", "misterio_aberto"],
        "gancho": "Por décadas, um homem viveu sozinho na floresta de Rondônia, último sobrevivente conhecido de um povo massacrado. Ninguém soube seu nome nem sua língua. Em cada casa que deixava, havia um buraco fundo.",
        "explicacao": (
            "Ele ficou conhecido como Homem do Buraco, ou índio do Tanaru. A maior parte do seu povo teria sido morta "
            "por colonos nos anos 1970, e os últimos sobreviventes, menos ele, foram mortos num ataque de garimpeiros "
            "ilegais em 1995. Como o grupo vivia isolado, nunca se soube como se chamava, que língua falava (talvez "
            "do tronco tupi) nem qual era o nome dele. Os Guaratira contestam essa versão e dizem que ele era um "
            "sobrevivente do povo deles. A FUNAI soube da sua existência em 1996 e, ao longo dos anos, identificou "
            "mais de 50 cabanas que ele construiu. Ele caçava, coletava frutos e mel e plantava milho e mandioca. Em "
            "cada casa abandonada havia um buraco estreito com mais de 1,8 metro de profundidade. Pensou-se que "
            "servissem para pegar animais ou para se esconder, mas há quem suspeite de um sentido espiritual. Em "
            "2007, a FUNAI demarcou 8 mil hectares como Terra Indígena Tanaru, mas em 2009 ele ainda sobreviveu a um "
            "ataque de pistoleiros. Em 24 de agosto de 2022, foi encontrado morto na rede, enfeitado com penas de "
            "arara, \"como se esperasse a morte\". Teria morrido em julho, com cerca de 60 anos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Man_of_the_Hole",
                "The Man of the Hole (c. 1960s – c. July 2022), or the Tanaru Indian, was an Indigenous person who lived alone in the Amazon rainforest in the Brazilian state of Rondônia. [...] "
                "It is not known what language the Man of the Hole spoke (although it may have been Tupian), what his people called themselves, or what his name was. "
                "He was the last surviving member of his people following their genocide by Brazilian settlers in the 1970s through 1990s and chose to remain isolated until his death in 2022. [...] "
                "The majority of his people are believed to have been killed by settlers in the 1970s [...] "
                "The remaining survivors, apart from the Man of the Hole, were killed in an attack by illegal miners in 1995. [...] "
                "However, the Guaratira claim that the Man of the Hole was not the last member of his people, but rather a Guaratira survivor. [...] "
                "FUNAI first became aware of the Man of the Hole's isolated existence in 1996. [...] "
                "He hunted wild game, collected fruits and honey, and also planted maize and cassava. "
                "Over the years, more than 50 huts that he built were identified by FUNAI. "
                "His nickname derives from the deep hole found in each home that he abandoned. "
                "It was originally believed that these holes were used to trap animals or to hide in, but some observers have also speculated that they might have been of spiritual significance. "
                "The holes were narrow and more than 1.8 m (5 ft 11 in) deep. [...] "
                "In 2007, FUNAI officially demarcated 8,000 hectares (31 sq mi) of his land as a protected Indigenous territory, the Tanaru Indigenous Territory. [...] "
                "the Man of the Hole was attacked by gunmen in November 2009 but managed to survive. [...] "
                "On 24 August 2022, the Man of the Hole was found dead in his last home by FUNAI agent Altair José Algayer. "
                "He was found \"lying down in the hammock, and ornamented [with macaw feathers] as if waiting for death\". [...] "
                "It was estimated that he had died in July and was about 60 years old at the time of his death.",
                nome="Man of the Hole"),
        ],
    },
    # 8 povos isolados: escolha, não "tribos perdidas"
    {
        "temas_secundarios": ["amazonia"],
        "tipos_espanto": ["mito_desmentido", "escala_absurda"],
        "gancho": "O Brasil abriga a maioria dos povos isolados do planeta: 124 dos 196 grupos com evidências sólidas, segundo um relatório de 2025. E eles não são \"tribos perdidas\": em geral sabem do mundo lá fora e evitam o contato.",
        "explicacao": (
            "A imagem de povos que nunca viram ninguém de fora tem raiz colonial: exploradores europeus os "
            "imaginavam como \"tribos perdidas\". Na realidade, os chamados povos isolados costumam saber que o mundo "
            "exterior existe e têm ou tiveram contato com povos vizinhos, às vezes até contato prolongado com a "
            "sociedade nacional no passado. São contemporâneos da modernidade, e não restos de um estado natural. A "
            "experiência brasileira sugere que eles poderiam até querer trocas com outros, mas escolhem o isolamento "
            "por medo de conflitos ou de exploração. Em 2014, por exemplo, um grupo do Acre só procurou uma aldeia e "
            "depois o governo após sofrer ataques de traficantes. Em 2025, a ONG Survival International publicou o "
            "primeiro levantamento mundial e achou evidências sólidas de 196 povos isolados em dez países, 124 deles "
            "no Brasil. O que se sabe deles vem sobretudo de povos vizinhos e de imagens aéreas. Em 1987, a FUNAI "
            "criou um departamento dedicado a eles, e o Vale do Javari, no Amazonas, maior que a Áustria, guarda, "
            "segundo um servidor da FUNAI, a maior concentração de grupos isolados do mundo. O mesmo relatório prevê "
            "que quase metade desses 196 povos pode desaparecer em 10 anos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Uncontacted_peoples",
                "Generally such peoples are aware of the outside world, and have or had interactions with neighboring peoples, or may have had sustained contact with the wider world in the past. [...] "
                "In 2025, Survival International published the first comprehensive report on uncontacted peoples worldwide. "
                "It found robust evidence of 196 uncontacted peoples living in ten countries across South America, Asia and the Pacific. "
                "The vast majority of uncontacted peoples live in the Amazon rainforest in South America, especially Brazil, where Survival has found evidence of 124 groups. "
                "Knowledge of uncontacted peoples comes mostly from encounters with neighbouring indigenous communities and aerial footage. [...] "
                "As such, uncontacted peoples are contemporaries of modernity, not living in an anachronistic state of nature. [...] "
                "Historically, European colonial ideas of uncontacted peoples, and their colonial claims over them, were informed by the imagination of and search for Prester John, king of a wealthy Christian realm in isolation, as well as the Ten Lost Tribes of Israel, identifying uncontacted peoples as \"lost tribes\". [...] "
                "Survival International predicted that almost half of the world's 196 uncontacted peoples could be wiped out within 10 years. [...] "
                "It was those threats, combined with attacks on their tribe by illegal cocaine traffickers, that led a group of Acre Indians to make contact with a village in Brazil and subsequently with the federal government in 2014. "
                "This behaviour suggests that many tribes are aware of the outside world and choose not to make contact unless motivated by fear or self-interest. [...] "
                "experience in Brazil suggests isolating peoples might want to have trading relationships and positive social connections with others, but choose isolation out of fear of conflict or exploitation. [...] "
                "In 1987, it set up the Department of Isolated Indians inside FUNAI",
                nome="Uncontacted peoples"),
            wiki("Vale_do_Javari",
                "encompassing 85,444.82 km2 (32,990 mi2) – an area larger than Austria. [...] "
                "According to Fabricio Amorim from the Brazilian National Indigenous People Foundation (FUNAI), the region contains \"the greatest concentration of isolated groups in the Amazon and the world\".",
                nome="Vale do Javari"),
        ],
    },
    # 9 o sangue yanomami que voltou para casa
    {
        "temas_secundarios": ["genetica", "costumes_rituais"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Em 1967, cientistas americanos colheram sangue de Yanomami no Brasil. A tradição deles proíbe guardar partes do corpo de quem morreu, e só em 2015, após anos de cobrança, 2.693 amostras voltaram para ser enterradas.",
        "explicacao": (
            "A coleta foi feita pelo geneticista James Neel e pelo antropólogo Napoleon Chagnon em aldeias da região "
            "do Toototobi, no Amazonas, com apoio de missionários. Segundo os Yanomami, ela foi trocada por bens "
            "manufaturados e pela promessa de tratamento médico, sem que soubessem o que seria feito do sangue nem "
            "que ele ficaria guardado por décadas nos EUA. Isso fere uma regra religiosa yanomami: não se deve manter "
            "nenhuma parte do corpo de alguém depois da sua morte. O líder Davi Kopenawa, que teve o sangue colhido "
            "quando tinha uns 6 anos, só descobriu em 2001, pelo livro \"Trevas no Eldorado\", de Patrick Tierney, que "
            "as amostras ainda eram usadas em laboratórios americanos, e passou a exigir a devolução. Com a ajuda do "
            "Ministério Público Federal e do Itamaraty, a Universidade Estadual da Pensilvânia devolveu 2.693 "
            "amostras de sangue processado e DNA purificado. Em abril de 2015, na aldeia Piau, cerca de 300 Yanomami "
            "participaram da cerimônia: protegidos por luvas cirúrgicas, dois xamãs despejaram o sangue numa cova "
            "enquanto os demais choravam os parentes mortos. O ritual durou quase três horas e terminou com mingau de "
            "pupunha e tabaco oferecidos aos mortos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": ISA_SANGUE, "titulo": "Yanomami enterram as primeiras amostras de sangue repatriadas dos Estados Unidos (ISA)", "idioma": "pt",
             "trecho": "O enterro do sangue ocorreu no dia 3/4, na aldeia Piau, região do Toototobi, no Amazonas, próxima à fronteira entre Brasil e Venezuela. "
                       "Cerca de 300 Yanomami participaram da cerimônia, entre moradores da aldeia, grupos aliados e familiares de aldeias vizinhas. [...] "
                       "Em seguida, a caixa com as 2.693 amostras de sangue processado e DNA purificado foi deixada ao lado de uma cova de pouco mais de um metro de profundidade. [...] "
                       "À medida que dois xamãs, protegidos por luvas cirúrgicas, abriam os recipientes e despejavam o sangue de seus familiares na terra, os demais lembravam e choravam os falecidos de seu parentesco com as pessoas ali presentes. [...] "
                       "Esse ritual durou quase três horas, até todas as amostras serem cuidadosamente despejadas. "
                       "Por fim, antes de cobrirem a cova, os xamãs ofereceram mingau de pupunha e tabaco aos mortos. [...] "
                       "O caso começou em 2001, quando o líder indígena Davi Kopenawa Yanomami tomou conhecimento, por meio do livro de Patrick Tierney “Trevas no Eldorado”, de que amostras de sangue Yanomami coletadas no Brasil, na sua infância, ainda estavam conservadas e sendo utilizadas por diversos laboratórios norte-americanos em pesquisas genéticas [...] "
                       "As amostras foram coletadas pelo geneticista James Neel e o antropólogo Napoleon Chagnon, em 1967, em várias aldeias da região do Toototobi, com o apoio de missionários locais da Missão Novas Tribos do Brasil (MNTB). "
                       "Segundo os Yanomami, a coleta foi feita em troca da distribuição de bens manufaturados e de promessa de futuros tratamentos médicos, mas em nenhum momento os índios foram devidamente informados sobre o que de fato seria feito com o sangue e nem que ele seria mantido por décadas nos EUA. "
                       "O próprio Davi, com cerca de 6 anos de idade, lembra de ter seu sangue coletado pelos americanos. [...] "
                       "Em esforço realizado nos últimos dois anos, o MPF em Roraima e o Itamaraty conseguiram viabilizar a repatriação, feita pela Universidade do Estado da Pennsylvania."},
            wiki("Yanomami",
                "Although Yanomami religious tradition prohibits the keeping of any bodily matter after the death of that person, the donors were not warned that blood samples would be kept indefinitely for experimentation. [...] "
                "In 2015 the blood samples were returned and buried by the Yanomami.",
                nome="Yanomami"),
        ],
    },
    # 10 Santarém, Óbidos, Alenquer: os nomes de Pombal
    {
        "temas_secundarios": ["nomes_lugares", "historia_portugues", "brasil_colonial"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "No Pará e no Amazonas há cidades chamadas Santarém, Óbidos, Alenquer, Faro e Barcelos, como em Portugal. Os nomes vêm de quando o governo de Pombal proibiu a língua geral amazônica, o nheengatu.",
        "explicacao": (
            "O nheengatu, ou língua geral amazônica, é uma língua da família tupi-guarani que se espalhou pela "
            "Amazônia com a colonização. Ali, os falantes de outras línguas eram tão mais numerosos que os colonos "
            "que os próprios portugueses se adaptaram. Um colono registrou que, para conversar no Grão-Pará, tinha de "
            "usar o nheengatu, porque ninguém falava português, a não ser no palácio do governo em Belém e entre os "
            "próprios portugueses. A língua acabou proibida pelo governo do Marquês de Pombal, que queria impor o "
            "português no Brasil. Por isso, muitos lugares trocaram o nome na língua geral por nomes de cidades de "
            "Portugal, como Santarém, Aveiro, Barcelos, Óbidos, Faro e Alenquer. Mesmo assim, o nheengatu sobreviveu. "
            "Em dezembro de 2002, virou língua oficial, ao lado do português, em São Gabriel da Cachoeira, no "
            "Amazonas, que hoje tem quatro línguas oficiais. E em 2023 a Constituição de 1988 ganhou sua primeira "
            "tradução para uma língua indígena, justamente o nheengatu, feita por 15 indígenas bilíngues do Alto Rio "
            "Negro e do Médio Tapajós. Até então, ela só tinha versões em espanhol e inglês."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Nheengatu_language",
                "is a Tupi–Guarani language. [...] "
                "Nheengatu subsequently spread throughout the Amazon as a tool of colonization, Portuguese dominion, and linguistic standardization. [...] "
                "Speakers of other languages vastly outnumbered the Portuguese settlers in the Amazon, to the point that the Portuguese themselves adapted to the native language. "
                "A Portuguese colonist stated: \"To speak or converse in the colony of Grão Pará, I had to use Nheengatu; if not, I would be talking to myself, since no one used Portuguese, except in the government palace in Belém and among the Portuguese themselves.\" [...] "
                "The language was banned by Pombal's government, who intended to impose the Portuguese language in Brazil. "
                "Hence, many places had their names changed from the Northern General language to names of places and cities in Portugal, such as Santarém, Aveiro, Barcelos, Belém, Óbidos, Faro, Alenquer, and Moz. [...] "
                "In December 2002, Nheengatu gained official language status alongside Portuguese in the municipality of São Gabriel da Cachoeira in accordance with local law 145/2002. "
                "Now Nheengatu is one of the four official languages of the municipality. [...] "
                "In 2023, the Brazilian Constitution was translated into Nheengatu, marking the first time it was rendered into an Indigenous language—until then, it had been translated only into Spanish and English. "
                "The translation was carried out by 15 bilingual Indigenous individuals from the Upper Negro River and Middle Tapajós regions [...] "
                "In 2023, the Constitution of the Federative Republic of Brazil (Brazilian Constitution), promulgated in 1988, was translated into Nheengatu for the first time.",
                nome="Nheengatu language"),
        ],
    },
    # 11 Fulni-ô: a língua que resistiu no Nordeste
    {
        "temas_secundarios": ["linguas_mundo", "religioes"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "Os Fulni-ô, de Pernambuco, são o único povo do Nordeste que manteve viva a própria língua, o iatê. E todo ano passam semanas recolhidos num ritual, o Ouricuri, sobre o qual todos têm como regra não falar.",
        "explicacao": (
            "Segundo o Instituto Socioambiental, os Fulni-ô são o único grupo indígena do Nordeste que conseguiu "
            "manter ativa sua própria língua, o iatê (ou yaathê), que significa \"nossa fala\". Ela é considerada "
            "uma língua isolada, sem parentes conhecidos, embora alguns linguistas a incluam no tronco macro-jê. Em "
            "2020 havia cerca de 500 falantes fluentes entre os 7 mil Fulni-ô; hoje todos falam também português, "
            "e o iatê é usado sobretudo por adultos e idosos. O território deles fica em Águas Belas, no agreste "
            "pernambucano, e a cidade está no meio da reserva, totalmente cercada por ela. A língua tem papel central "
            "no Ouricuri, um retiro religioso de cerca de três meses numa aldeia sagrada separada. Nesse período o iatê é a língua preferida, e é ali que os jovens aprendem "
            "os códigos do grupo. Quem trabalha na cidade pede licença para ir. Lá dentro são proibidos bebida "
            "alcoólica, música e até assobio, e todos seguem a regra de não falar do ritual. Os anciãos dizem que "
            "quem quebrou o segredo teve morte estranha."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": ISA_FULNIO, "titulo": "Fulni-ô - Povos Indígenas no Brasil (ISA)", "idioma": "pt",
             "trecho": "Os Fulni-ô são o único grupo do Nordeste que conseguiu manter viva e ativa sua própria língua - o Ia-tê - assim como um ritual a que chamam Ouricuri, que atualmente realizam no maior sigilo. "
                       "Na parte central das terras da reserva indígena se encontra assentada a cidade de Águas Belas rodeada totalmente pelo território Fulniô. [...] "
                       "Os preparativos para a mudança para a aldeia do Ouricuri se iniciam nas últimas semanas do mês de agosto. "
                       "Todos os Fulni-ô que trabalham fora de Águas Belas, como funcionários, professores, policiais, durante a primeira semana do ritual pedem licença para se ausentarem do trabalho e se concentrarem na aldeia do Ouricuri [...] "
                       "Todos os Fulni-ô têm como norma a proibição de falar do ritual. "
                       "Os anciãos asseguram que aqueles que infringiram esta norma tiveram morte estranha. [...] "
                       "Está proibido também tomar bebidas alcoólicas, escutar música, e inclusive assobiar. [...] "
                       "No ritual do Ouricuri, o Ia-tê desempenha um papel fundamental, já que é a língua preferencialmente falada durante as suas quatorze semanas de duração. "
                       "É aí que se socializam os membros mais jovens pelo ensino de um código simbólico diferente daquele utilizado pela sociedade envolvente. [...] "
                       "Atualmente todos os índios em Águas Belas falam português; em Ia-tê se comunicam principalmente os adultos e idosos"},
            wiki("Yatê_language",
                "the Fulni-ô language (Fulniô pronunciation: [ja:the]), is a language isolate of Brazil, and the only indigenous language remaining in the northeastern part of that country. [...] "
                "The Fulniô dialect is used primarily during a three-month religious retreat. "
                "Today, the language is spoken in Águas Belas, Pernambuco. "
                "As of 2020, there were 500 fluent speakers of Yatê out of 7,000 Fulni-ô. [...] "
                "The name \"Yatê\" means 'our speech' in the language, from ja 'our' and athe 'speech'. [...] "
                "Kaufman (1990, 1994, 2007) classified Fulniô as one of the Macro-Jê languages. "
                "However, Eduardo Ribeiro of the University of Chicago, who is working on large-scale classification of Brazilian languages, finds no evidence to support this, and treats it as an isolate.",
                nome="Yatê language"),
        ],
    },
    # 12 Tupã: o trovão que virou Deus
    {
        "temas_secundarios": ["religioes", "brasil_colonial"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "Para falar de Deus aos tupis, os jesuítas adotaram a palavra Tupã, ligada ao trovão. Em 1576, um missionário francês protestou: entre os indígenas, \"Toupan\" não significava Deus, mas trovão.",
        "explicacao": (
            "Na religião tupi-guarani, Tupã está ligado às águas, à chuva, ao relâmpago e ao trovão. Quando chegaram "
            "ao Brasil, os jesuítas procuravam entre os indígenas algo parecido com a religião europeia e não "
            "acharam. Em 1559, na Bahia, o padre Manuel da Nóbrega escreveu que aqueles povos não adoravam nada e "
            "só chamavam os trovões de \"Tupane\", algo como \"coisa divina\". Como não havia palavra melhor, a "
            "solução foi chamar Deus de \"Pai Tupane\". José de Anchieta levou a estratégia adiante na catequese: "
            "Deus Pai virou Tupã-túba e Nossa Senhora, Tupansy, a \"mãe de Deus\". Nem todos concordavam. O pastor "
            "francês Jean de Léry escreveu em 1576 que, entre os nativos, Toupan não significava Deus, mas trovão. "
            "Até hoje o assunto divide estudiosos. Câmara Cascudo chegou a dizer que Tupã era um deus criado pela "
            "catequese; o etnólogo Curt Nimuendajú reconhecia nele uma divindade indígena, mas criticava o abuso que "
            "os missionários fizeram do nome. O certo é que o uso de Tupã para o Deus cristão se espalhou pelo "
            "Brasil, pelo Paraguai e por boa parte da Argentina, do Uruguai e da Bolívia."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Tupã",
                "é o deus das águas, do mar, dos rios, da chuva, do relâmpago e do trovão na religião e mitologia tupi-guarani. "
                "Após a chegada dos europeus à América do Sul, Tupã foi ressignificado pelos jesuítas e passou a designar também o Deus cristão [...] "
                "O padre jesuíta português Manuel da Nóbrega, de fato, escreveu em 1559 na Bahia: \"Esta gentilidade nenhuma coisa adora, nem conhece Deus, somente aos trovões chama Tupane; que é como quem diz coisa divina. "
                "E assim nós não temos outro vocábulo mais conveniente para os trazer ao conhecimento de Deus, que chamar-lhe Pai Tupane\". "
                "Nóbrega e outros jesuítas esperavam encontrar entre os nativos formas religiosas análogas às do continente europeu [...] "
                "Na obra catequética do padre jesuíta espanhol José de Anchieta ainda no século XVI, as menções a Tupã foram usadas como uma estratégia de inculturação [...] "
                "a “Deus Pai” ele se referia como Tupã-túba (“Deus-pai”) e a Maria, Nossa Senhora, como Tupansy (“mãe-de-Deus”). [...] "
                "O pastor, missionário e escritor francês Jean de Léry, em 1576, escreveu que “Toupan entre eles [os nativos] não significa Deus, mas trovão”. [...] "
                "afirma que Tupã é um \"deus criado pela catequese católica\" [...] "
                "como o etnólogo alemão-brasileiro Curt Nimuendajú (nascido Curt Unckel), que viveu parte de sua vida com os apapocuvas/nhandevas — quando falam do abuso feito de seu nome pelos missionários que o introduziram para designar o Deus cristão em todo o Brasil, Paraguai, grande parte da Argentina, Uruguai e Bolívia. [...] "
                "Curt Nimuendaju, que reconhece a divindade indígena de Tupã",
                nome="Tupã", idioma="pt"),
        ],
    },
    # 13 Censo 2022: São Paulo, o estado com mais etnias
    {
        "temas_secundarios": ["cidades"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "O estado brasileiro com mais etnias indígenas não é o Amazonas: é São Paulo. O Censo 2022 registrou 271 povos lá, e só a capital paulista reúne 194, mais que Manaus.",
        "explicacao": (
            "O Censo 2022 contou 1.694.836 indígenas no Brasil, que declararam 391 etnias, povos ou grupos e falam "
            "295 línguas indígenas. Em 2010 eram 305 etnias e 274 línguas, e o IBGE atribui o aumento sobretudo à "
            "maior disposição das pessoas de se identificar com suas origens. O ranking de diversidade surpreende: "
            "São Paulo é a unidade da federação com mais etnias declaradas, 271, à frente do Amazonas, com 259, e da "
            "Bahia, com 233. Entre os municípios, a capital paulista lidera com 194, seguida de Manaus, com 186, e do "
            "Rio de Janeiro, com 176. Note que isso mede a variedade de povos, não o tamanho da população. A etnia "
            "mais numerosa é a Tikúna, com 74.061 pessoas, e o tikúna também é a língua indígena com mais falantes. "
            "No outro extremo, 21 etnias têm menos de 15 pessoas, e o Censo captou até línguas faladas por uma única "
            "pessoa. Segundo um gerente do IBGE, a diversidade em cidades médias, como Campinas, cresceu com a "
            "presença de universidades, políticas de inclusão e a mobilização indígena."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            {"url": CENSO, "titulo": "Orgulho de ser indígena eleva em 28% o registro de etnias e em 8% o de línguas (Agência Gov, via IBGE)", "idioma": "pt",
             "trecho": "Dados do Censo Demográfico 2022 mostram a existência de 391 etnias, povos ou grupos indígenas no Brasil e de 295 línguas indígenas faladas no País. "
                       "No Censo anterior, de 2010, eram 305 etnias e 274 línguas. "
                       "Os aumentos, de 28% e 8%, respectivamente, podem ser atribuídos à crescente auto-identificação das pessoas com suas origens, reflexo de políticas públicas de proteção. "
                       "Essa é uma interpretação do próprio IBGE. "
                       "Do total da população indígena em 2022 (1.694.836 pessoas), 74,51% declararam etnia, sendo as etnias mais populosas Tikúna (74.061), Kokama (64.327) e Makuxí (53.446). [...] "
                       "As três línguas com maior número de falantes são: Tikúna (51.978), Guarani Kaiowá (38.658) e Guajajara (29.212), mas a pesquisa captou línguas faladas por grupos menores e até por uma única pessoa. [...] "
                       "São Paulo é a Unidade da Federação com o maior número de etnias, povos ou grupos indígenas identificados pelo Censo. "
                       "Ao todo, foram 271 etnias declaradas. "
                       "Em seguida, destacam-se o Amazonas, com 259 etnias, e a Bahia, com 233. [...] "
                       "Os municípios com maiores quantitativos de etnias eram São Paulo/SP (194 etnias), seguido de Manaus/AM (186), Rio de Janeiro/RJ (176) e Salvador/BA (142). [...] "
                       "Fora das capitais, os que apresentaram maiores quantitativos foram Campinas (SP), com 96 etnias, Santarém (PA), com 87 e Iranduba (AM), com 77. "
                       "Fernando Damasco, gerente de Territórios Tradicionais e Áreas Protegidas do IBGE, atribui o aumento da diversidade étnica em cidades médias à presença de universidades, políticas de inclusão e mobilizações indígenas. [...] "
                       "Por outro lado, 21 etnias, povos ou grupos indígenas apresentaram menos de 15 pessoas."},
        ],
    },
]
