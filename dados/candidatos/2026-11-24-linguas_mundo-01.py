LOTE = "2026-11-24-linguas_mundo-01"
AREA = "linguas"
TEMA = "linguas_mundo"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Papua-Nova Guiné: 840 línguas e o tok pisin ("business")
    {
        "temas_secundarios": ["palavras_viajantes", "comercio_rotas"],
        "tipos_espanto": ["escala_absurda", "origem_inesperada"],
        "gancho": "A Papua-Nova Guiné tem cerca de 840 línguas vivas, mais que qualquer país. Para se entender, usa o tok pisin, de \"talk pidgin\". E \"pidgin\" nasceu da pronúncia chinesa do inglês \"business\".",
        "explicacao": (
            "Segundo o Ethnologue e outras fontes, a Papua-Nova Guiné, na Oceania, é o país de maior diversidade "
            "linguística do mundo, com 840 línguas vivas. A conta varia porque depende de onde se põe a fronteira "
            "entre língua e dialeto: em 2006, o primeiro-ministro Michael Somare falou em 832. A maioria é de línguas "
            "papuas, nativas da ilha da Nova Guiné; outras são austronésias, trazidas por povos que chegaram há cerca "
            "de 3.500 anos. Para atravessar essa babel, o país tem como língua franca o tok pisin, um crioulo de base "
            "inglesa que é língua oficial e a mais usada no território: no censo de 2011, 68,4% da população sabia "
            "ler e escrever nele. O nome vem do inglês \"talk pidgin\". A palavra \"pidgin\", por sua vez, veio da "
            "pronúncia chinesa de \"business\", negócio, e nos registros da primeira metade do século XIX ainda queria "
            "dizer \"negócio\" ou \"ocupação\". Só depois passou a designar as línguas simplificadas que surgem quando "
            "grupos sem idioma comum precisam negociar. A explicação popular, de que viria de \"pigeon\", o "
            "pombo-correio, é falsa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Languages_of_Papua_New_Guinea",
                "Papua New Guinea, a sovereign state in Oceania, is the most linguistically diverse country in the world. "
                "Ethnologue, among other sources, state that there are 840 living languages spoken in the country, although estimates vary due to the distinction between a language and a dialect. "
                "In 2006, Papua New Guinea Prime Minister Sir Michael Somare stated that \"Papua New Guinea has 832 living languages (languages, not dialects).\" [...] "
                "the country's lingua franca (and vernacular for some) being Tok Pisin, an English-based creole [...] "
                "Most of these are classified as indigenous Papuan languages, which form a diverse sprachbund across the island of New Guinea. "
                "There are also many Austronesian languages spoken in Papua New Guinea [...] "
                "Tok Pisin is an English-based creole language spoken throughout Papua New Guinea. "
                "It is an official language of Papua New Guinea and the most widely used language in the country. [...] "
                "In the 2011 census, 68.4% of the population were literate in Tok Pisin. [...] "
                "People speaking languages belonging to the Austronesian family arrived in New Guinea approximately 3,500 years ago.",
                nome="Languages of Papua New Guinea"),
            wiki("Pidgin",
                "is a grammatically simplified form of contact language that develops between two or more groups of people that do not have a language in common [...] "
                "It is most commonly employed in situations such as trade [...] "
                "Pidgin derives from a Chinese pronunciation of the English word business, and all attestations from the first half of the nineteenth century given in the third edition of the Oxford English Dictionary mean \"business; an action, occupation, or affair\" (the earliest being from 1807). [...] "
                "A popular false etymology for pidgin is English pigeon, a bird sometimes used for carrying brief written messages [...] "
                "For example, the name of the creole language Tok Pisin derives from the English words talk pidgin.",
                nome="Pidgin"),
        ],
    },
    # 2 Unserdeutsch: o crioulo alemão de um orfanato
    {
        "temas_secundarios": ["imperios_coloniais", "desenvolvimento_humano"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "O único crioulo nascido do alemão colonial, o Unserdeutsch (\"nosso alemão\"), surgiu entre crianças de um orfanato católico na Papua-Nova Guiné: palavras alemãs sobre a base do tok pisin.",
        "explicacao": (
            "Entre 1884 e 1914, a metade norte da atual Papua-Nova Guiné foi uma colônia alemã. Em 1898, missionários "
            "católicos abriram em Vunapope, na península de Gazelle, um internato e orfanato para crianças mestiças, "
            "filhas do contato entre colonos, trabalhadores trazidos de outras partes do Pacífico e moradores locais. "
            "As aulas eram em alemão, mas as crianças também conviviam com as línguas dos pais, como cantonês, tagalo "
            "e malaio, e sobretudo com o tok pisin. Desse caldeirão nasceu o Unserdeutsch, um crioulo de vocabulário "
            "alemão que tem o tok pisin como substrato. Segundo histórias contadas na comunidade, as crianças narravam "
            "casos usando palavras alemãs com a gramática do tok pisin, processo que os linguistas chamam de "
            "relexificação. Quando esses alunos formaram família, a língua virou a primeira de alguns dos filhos. "
            "Depois da independência do país, em 1975, a maioria dos falantes migrou para a Austrália. Em pesquisas "
            "de campo feitas entre 2014 e 2017, foram encontrados cerca de 100 falantes lá e uns 10 na Papua-Nova "
            "Guiné, e ninguém mais o aprende como primeira língua."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Unserdeutsch",
                "Unserdeutsch ('Our German'), or Rabaul Creole German, is a German-based creole language that originated in Papua New Guinea. "
                "It is described as a boarding school creole as it emerged among mixed-race children at a Catholic orphanage and school in Vunapope [...] "
                "The children were educated in German and in contact with several other languages, mainly Tok Pisin which greatly influenced the creole. [...] "
                "The Gazelle Peninsula had become the most prosperous part of German New Guinea which brought along European traders and missionaries, who also brought along workers from other parts of the Pacific. [...] "
                "1898, the Missionaries of the Sacred Heart and the Sisters of Our Lady of the Sacred Heart established a boarding school and orphanage at Vunapope for these children. "
                "Contact these children had with German speakers and the languages of their parents (immigrant languages, such as Cantonese, Tagalog, Trukese, Malay, and a host of indigenous languages of Papua New Guinea) helped develop Unserdeutsch. [...] "
                "The language developed into a first language for some when these children had families of their own. "
                "Oral stories tell a version that Unserdeutsch originated by children sharing stories where they used German vocabulary with Tok Pisin grammar, this change in language is referred to as relexification. "
                "The majority of Unserdeutsch speakers and their families migrated to Australia after Papua New Guinea's independence in 1975. "
                "During fieldwork conducted by researchers between 2014 and 2017, there were about 100 speakers found in Australia and around 10 speakers found in Papua New Guinea. "
                "The language is no longer learned as a first language. [...] "
                "it is the only creole that developed from colonial German.",
                nome="Unserdeutsch"),
            wiki("Languages_of_Papua_New_Guinea",
                "From 1884 to 1914, the northern half of the present-day country was a German colony known as German New Guinea, in which German was the official language. [...] "
                "The lexicon is derived from German, while the substrate language is Tok Pisin.",
                nome="Languages of Papua New Guinea"),
        ],
    },
    # 3 os extremos: taa com dezenas de consoantes e cliques, rotokas com seis
    {
        "temas_secundarios": ["acustica", "estruturas_linguisticas"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "O taa, falado em Botsuana e na Namíbia, tem pelo menos 58 consoantes, e numa contagem 82% das palavras básicas começam com um clique. Já o rotokas central, da Papua-Nova Guiné, tem só seis consoantes.",
        "explicacao": (
            "O taa, também chamado de !xóõ, é conhecido por ter talvez o maior número de sons distintos de qualquer "
            "língua. As contagens mudam conforme o pesquisador e o dialeto estudado: pelo menos 58 consoantes, 31 "
            "vogais e quatro tons, segundo os trabalhos de Traill sobre o dialeto do leste, ou pelo menos 87 "
            "consoantes, 20 vogais e dois tons, segundo o projeto DoBeS, que estudou o do oeste. Parte da divergência "
            "vem de decidir quais sons combinados contam como um só. Os cliques são 20 ou 43, conforme a análise. Em "
            "2011, o taa tinha cerca de 2.500 falantes, a maioria em Botsuana. No extremo oposto está o dialeto "
            "central do rotokas, falado por cerca de 4.320 pessoas na ilha de Bougainville. Ele tem um dos menores "
            "inventários de consoantes do mundo, sem nenhuma consoante nasal própria: só seis, contra nove do "
            "dialeto vizinho, o aita. Os nasais aparecem só de vez em quando, por exemplo quando os falantes "
            "pronunciam palavras inglesas: \"bye-bye\" vira algo como \"maemae\". A escrita do rotokas se vira com "
            "12 letras do alfabeto latino, sem nenhum acento."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Taa_language",
                "is a Tuu language notable for its large number of phonemes, perhaps the largest in the world. "
                "It is also notable for having perhaps the heaviest functional load of click consonants, with one count finding that 82% of basic vocabulary items started with a click. "
                "Most speakers live in Botswana, but a few hundred live in Namibia. [...] "
                "In 2011, there were around 2,500 speakers of Taa. [...] "
                "Taa has at least 58 consonants, 31 vowels, and four tones (Traill 1985, 1994 on East [...] "
                "or at least 87 consonants, 20 vowels, and two tones (DoBeS 2008 on West [...] "
                "These include 20 (Traill) or 43 (DoBeS) click consonants and several vowel phonations, though opinions vary as to which of the 122 (DoBeS) or 130 (Traill) consonant sounds are single segments",
                nome="Taa language"),
            wiki("Rotokas_language",
                "Rotokas is a North Bougainville language spoken by about 4,320 people on Bougainville Island in Papua New Guinea. "
                "Central Rotokas is most notable for its extremely small phonemic consonantal inventory, which lacks phonemic nasals. [...] "
                "The Central dialect of Rotokas possesses one of the world's smallest phonemic consonantal inventories. [...] "
                "Whereas Central Rotokas has only six consonantal phonemes, Aita Rotokas has nine [...] "
                "Nasals are rarely heard. "
                "They will sometimes be misused when speakers try to pronounce English words (e.g. \"bye-bye\" being pronounced [maemae]) [...] "
                "The Rotokas orthography uses 12 letters of the Latin alphabet, with no diacritics or ligatures.",
                nome="Rotokas language"),
        ],
    },
    # 4 ubykh: 84 consoantes e o último falante
    {
        "temas_secundarios": ["personagens_esquecidos", "imperios_coloniais"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "O ubykh, do Cáucaso, tinha 84 consoantes e só duas ou três vogais. Seu último falante fluente, Tevfik Esenç, morreu em 1992, depois de ajudar linguistas a registrá-lo em milhares de páginas e gravações.",
        "explicacao": (
            "O ubykh era falado na costa leste do mar Negro, perto de Sochi, até 1864, quando os ubykhs foram "
            "expulsos pelos russos e acabaram fundando vilarejos na Turquia. Ali, o árabe e o circassiano foram "
            "tomando o lugar da língua no dia a dia. Os linguistas se interessaram por ela pelo contraste extremo: 84 "
            "consoantes, recorde entre as línguas sem cliques, quatro delas usadas só em palavras emprestadas e "
            "onomatopeias, e pouquíssimas vogais, duas ou três conforme a análise. O Livro Guinness chegou a apontá-la "
            "como a língua com mais consoantes, até passar o título, em 2017, ao !xóõ, do sul da África. Tevfik "
            "Esenç, nascido em 1904, foi criado pelos avós num desses vilarejos, foi chefe local e depois trabalhou "
            "no serviço público em Istambul. Lá, colaborou com o francês Georges Dumézil e seu associado Georges "
            "Charachidzé, entre outros pesquisadores. Ao encerrar o trabalho, escreveu a Charachidzé: \"Agora você é "
            "a língua ubykh\". Esenç morreu em 7 de outubro de 1992, aos 88 anos, e a língua morreu com ele."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Ubykh_language",
                "The last speaker was Tevfik Esenç, who died in 1992. "
                "Ubykh is ergative and polysynthetic, with a high degree of agglutination, with polypersonal verbal agreement and a very large number of distinct consonants but only two phonemically distinct vowels. [...] "
                "Ubykh was spoken in the eastern coast of the Black Sea around Sochi until 1864, when the Ubykhs were driven out of the region by the Russians. "
                "They eventually came to settle in Turkey, founding the villages of [...] "
                "Arabic and Circassian eventually became the preferred languages for everyday communication [...] "
                "The Ubykh language died out on 7 October 1992, when its last fluent speaker, Tevfik Esenç, died. "
                "Before his death, thousands of pages of material and many audio recordings had been collected and collated by a number of linguists [...] "
                "with the help of some of its last speakers, particularly Tevfik Esenç and Huseyin Kozan. [...] "
                "Ubykh had been cited in the Guinness Book of Records (1996 ed.) as the language with the most consonant phonemes, but since 2017 the !Xóõ language (a member of the Tuu languages) has been considered by the book to have broken that record, with 130 consonants. [...] "
                "Ubykh has 84 phonemic consonants, a record high amongst languages without click consonants, but only 3 phonemic vowels. "
                "Four of these consonants are found only in loanwords and onomatopoeiae.",
                nome="Ubykh language"),
            wiki("Tevfik_Esen%C3%A7",
                "1904 – 7 October 1992) was an Ubykh Circassian citizen of Turkey, known for being the last speaker of the Ubykh language. [...] "
                "Esenç was raised by his Ubykh-speaking grandparents for a time in the village of [...] "
                "and he served a term as the muhtar (mayor) of that village, before receiving a post in the civil service of Istanbul. "
                "There, he was able to do a great deal of work with the French linguist Georges Dumézil and his associate Georges Charachidzé to help record his language [...] "
                "He finished his work for Ubykh with the following speech to his long-time collaborator Georges Charachidzé: [...] "
                "You are now the Ubykh language. [...] "
                "Esenç died on the night of 7 October 1992, at the age of 88",
                nome="Tevfik Esenç"),
        ],
    },
    # 5 canguru não quer dizer "não entendi"
    {
        "temas_secundarios": ["palavras_viajantes", "grandes_navegacoes"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "\"Canguru\" não quer dizer \"não entendi\" numa língua aborígene. A história é lenda: \"gangurru\" é o nome de um tipo de canguru em guugu yimithirr, como um linguista confirmou em 1972.",
        "explicacao": (
            "Em 1770, o navio Endeavour, comandado por James Cook, ficou quase sete semanas parado às margens de um "
            "rio do nordeste da Austrália, para consertar estragos sofridos na Grande Barreira de Coral. Ali, onde hoje "
            "fica a cidade de Cooktown, o naturalista Joseph Banks anotou no diário, em 12 de julho, a palavra "
            "\"kanguru\". Ela vinha do guugu yimithirr, a língua do povo daquela região. Com o tempo, espalhou-se a "
            "versão de que Cook e Banks teriam perguntado a um nativo o nome do bicho, e ele teria respondido algo "
            "como \"não sei\" ou \"não entendo\". O antropólogo Walter Roth já tentava desfazer a lenda em 1898, sem "
            "muito eco. Só em 1972 o linguista John Haviland, pesquisando com os guugu yimithirr, confirmou que "
            "\"gangurru\" era mesmo o nome de uma espécie de canguru. A língua ainda existe: a maioria dos falantes "
            "vive na comunidade de Hope Vale, mas em 2020 só cerca de metade do povo a falava, e há esforços para "
            "ensiná-la às crianças."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Kangaroo",
                "The word kangaroo derives from the Guugu Yimithirr word gangurru, referring to eastern grey kangaroos. "
                "The name was first recorded as \"kanguru\" on 12 July 1770 in an entry in the diary of Sir Joseph Banks; "
                "this occurred at the site of modern Cooktown, on the banks of the Endeavour River, where HMS Endeavour under the command of Lieutenant James Cook was beached for almost seven weeks to repair damage sustained on the Great Barrier Reef. [...] "
                "Guugu Yimithirr is the language of the people of the area. "
                "A common myth about the kangaroo's English name is that it was a Guugu Yimithirr phrase for \"I don't know\" or \"I don't understand\". "
                "According to this legend, Cook and Banks were exploring the area when they happened upon the animal. "
                "They asked a nearby local what the creatures were called. [...] "
                "Anthropologist Walter Roth was trying to correct this legend as far back as in 1898, but few took note until 1972 when linguist John B. Haviland in his research with the Guugu Yimithirr people was able to confirm that gangurru referred to a rare large dark-coloured species of kangaroo.",
                nome="Kangaroo"),
            wiki("Guugu_Yimithirr_language",
                "is an Australian Aboriginal language, the traditional language of the Guugu Yimithirr people of Far North Queensland. [...] "
                "Most of the speakers today live at the community of Hope Vale [...] "
                "However, as of June 2020 only about half of the Guugu Yimithirr nation speak the language. "
                "As such, efforts are being made to teach it to children. "
                "Guugu Yimithirr is the source language of the word kangaroo (gangurru).",
                nome="Guugu Yimithirr language"),
        ],
    },
    # 6 turco assobiado e os dois hemisférios
    {
        "temas_secundarios": ["neurociencia", "linguas_construidas"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Numa região de vales da Turquia, o turco é dito inteiro em assobios, que vão mais longe que gritos. Um estudo viu que, para entender a versão assobiada, o cérebro usa os dois hemisférios por igual.",
        "explicacao": (
            "A \"língua dos pássaros\", o kuş dili, é associada à aldeia de Kuşköy, \"aldeia dos pássaros\", perto do "
            "mar Negro, e tem cerca de 400 anos. Criada para falar a longas distâncias, ela transforma em assobios "
            "toda a informação de palavras e gramática do turco falado, o que permite conversas complexas de um lado "
            "a outro do vale. Em geral, a compreensão da linguagem depende em boa parte do hemisfério esquerdo do "
            "cérebro, o que já foi observado em línguas tonais, em línguas com cliques, na escrita e nas línguas de "
            "sinais. Já o direito se especializa em altura e melodia dos sons, justamente a matéria-prima do assobio. "
            "Num estudo publicado na revista Current Biology, pesquisadores compararam a compreensão do mesmo conteúdo falado e "
            "assobiado em pessoas da região e acharam contribuições simétricas dos dois hemisférios no caso do "
            "assobio. Nas Canárias, o silbo gomero faz o mesmo com o espanhol e alcança até cinco quilômetros. "
            "Estudos de 2004 e 2005 mostraram que quem domina o silbo o processa nas áreas de linguagem do cérebro, "
            "enquanto os outros só ouvem assobio. Nos dois lugares, o telefone reduziu o uso dessas línguas."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:26294179%20AND%20SRC:MED&resultType=core&format=json",
             "titulo": "Whistled Turkish alters language asymmetries (Current Biology, 2015) — resumo no Europe PMC",
             "idioma": "en",
             "trecho": "Whistled languages represent an experiment of nature to test the widely accepted view that language comprehension is to some extent governed by the left hemisphere in a rather input-invariant manner. "
                       "Indeed, left-hemisphere superiority has been reported for atonal and tonal languages, click consonants, writing and sign languages. "
                       "The right hemisphere is specialized to encode acoustic properties like spectral cues, pitch, and melodic lines [...] "
                       "Whistled Turkish uses the full lexical and syntactic information of vocal Turkish, and transforms this into whistles to transport complex conversations with constrained whistled articulations over long distances. "
                       "We tested the comprehension of vocally vs. whistled identical lexical information in native whistle-speaking people of mountainous Northeast Turkey. "
                       "We discovered that whistled language comprehension relies on symmetric hemispheric contributions [...] "
                       "Current biology : CB"},
            wiki("Turkish_bird_language",
                "Turkish bird language (Turkish: kuş dili) is a version of the Turkish language communicated through high-pitched whistles and melodies. "
                "It was originally used by Turkish farmers to communicate over large distances [...] "
                "The language is associated with Kuşköy, a village in northern Turkey's Giresun Province [...] "
                "The language dates back 400 years [...] "
                "The use of cellphones has eliminated the primary utilization of kuş dili. "
                "Since the town of Kuşköy is a farming village with a deep valley, whistling can travel significantly further and be more audible than just yelling.",
                nome="Turkish bird language"),
            wiki("Ku%C5%9Fk%C3%B6y",
                "Kuşköy (English meaning is \"Village of the Birds\") is a village in Çanakçı District of Giresun Province in the Black Sea region of Turkey.",
                nome="Kuşköy"),
            wiki("Silbo_Gomero",
                "is a whistled register of Spanish that is used by inhabitants of La Gomera, in the Canary Islands. "
                "It was historically used to communicate across the deep ravines and narrow valleys that radiate through the island and enabled messages to be exchanged over a distance of up to five kilometres. [...] "
                "Technological developments such as the telephone played a part in reducing the practicality and utility of the language. [...] "
                "Studies by Manuel Carreiras of the University of La Laguna and David Corina of the University of Washington published in 2004 and 2005 involved two participant groups of Spanish-speakers. [...] "
                "show that while non-speakers of Silbo merely process Silbo as whistling, Silbo-speakers process the sounds in the same linguistic centres of the brain as those that process Spanish sentences.",
                nome="Silbo Gomero"),
        ],
    },
    # 7 o hebraico volta a ser língua materna
    {
        "temas_secundarios": ["religioes", "desenvolvimento_humano"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Desde o século II, ninguém tinha o hebraico como língua materna. O primeiro falante nativo moderno, nascido em 1882, foi criado só nessa língua: o pai brigou até com a mãe por cantar uma canção de ninar russa.",
        "explicacao": (
            "Depois do fim do hebraico falado, no século II, a língua seguiu viva na oração, no estudo e na escrita, "
            "mas ninguém mais a aprendia no berço. Os judeus de cada região falavam outras línguas, como o iídiche, o "
            "judeu-espanhol ou o árabe. Eliezer Ben-Yehuda, cuja língua materna era o iídiche, mudou-se para "
            "Jerusalém em 1881 decidido a fazer do hebraico uma língua de uso diário. Em casa, só se falava hebraico, "
            "e o primeiro filho, nascido em 1882 e mais tarde conhecido como o jornalista Itamar Ben-Avi, foi mantido "
            "longe de outros idiomas. Tornou-se o primeiro falante nativo do hebraico moderno. O começo foi lento: "
            "segundo o próprio Ben-Yehuda, dez anos depois de sua chegada só quatro famílias de Jerusalém usavam "
            "exclusivamente o hebraico, e muitas palavras que ele criou nunca pegaram. O salto veio com as escolas "
            "dos assentamentos judaicos, que formaram as primeiras gerações de falantes nativos. Em 1948, 80,9% dos "
            "judeus nascidos na Palestina usavam só o hebraico no dia a dia. Não se conhece outro caso de uma língua "
            "sem falantes nativos que tenha passado a ter milhões deles."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Revival_of_the_Hebrew_language",
                "The process of Hebrew's return to regular usage is unique; there are no other examples of a natural language without any native speakers subsequently acquiring several million native speakers [...] "
                "From the 2nd century CE until the revival of Hebrew as a spoken language circa 1880, Hebrew served as a literary and official language and as the Judaic language of prayer. "
                "After the spoken usage of Mishnaic Hebrew ended in the 2nd century CE, Hebrew had not been spoken as a mother tongue. [...] "
                "The Sephardic Jews who spoke Judaeo-Spanish or Arabic and the Ashkenazi Jews who spoke Yiddish needed a common language for commercial purposes. [...] "
                "He determined that his family would only speak Hebrew, and raised his children to be native Hebrew speakers. "
                "His first child, a son named Itamar Ben-Avi, who was born in Jerusalem on 31 July 1882, became the first native speaker of Modern Hebrew. [...] "
                "According to Ben-Yehuda, ten years after his immigration to Palestine, there were only four families in Jerusalem that used Hebrew exclusively. [...] "
                "The first native speakers of Hebrew, who had mainly learned it in the Hebrew schools of the First Aliyah period and came to speak it as their primary language, reached adulthood during this time. [...] "
                "By the time Israel was established in 1948, 80.9% of Jews who had been born in Palestine spoke Hebrew as their only language in daily life",
                nome="Revival of the Hebrew language"),
            wiki("Eliezer_Ben-Yehuda",
                "immigrated to Jerusalem in 1881 [...] "
                "His native language was Yiddish. [...] "
                "He did not allow his son to be exposed to other languages during childhood, and even berated his wife for singing a Russian lullaby. "
                "His son thus became the first native speaker of Hebrew in modern times. [...] "
                "despite opposition to some of the words he coined. "
                "Many of these words have become part of the language but others never caught on. [...] "
                "Ben-Yehuda's son, journalist Itamar Ben-Avi",
                nome="Eliezer Ben-Yehuda"),
        ],
    },
    # 8 manx e córnico: "extintos" que a UNESCO ressuscitou
    {
        "temas_secundarios": ["europa_medieval"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Em 2009, um atlas da UNESCO declarou extinto o manx, língua celta da Ilha de Man, apesar de ter centenas de falantes. A UNESCO voltou atrás, como fez em 2010 com o córnico, também dado como extinto.",
        "explicacao": (
            "O manx é parente próximo do irlandês e do gaélico escocês. Seu uso despencou no século XIX, e em meados "
            "do século XX só restavam alguns falantes nativos idosos. O último deles, Ned Maddrell, morreu em 27 de "
            "dezembro de 1974. Mas a língua estava bem documentada: havia a Bíblia traduzida e gravações de falantes "
            "nativos, como as feitas pela Comissão de Folclore Irlandesa, que Éamon de Valera mandou à ilha com "
            "equipamento de gravação em 1948. Esse material ajudou o renascimento. Hoje há uma escola primária em "
            "que as crianças estudam quase tudo em manx, e no censo de 2021 cerca de 2.023 pessoas tinham algum "
            "nível de conversação. Quando o atlas da UNESCO o classificou como extinto, a linguista Jennifer Kewley "
            "Draskau protestou que, enquanto houvesse gente conversando nele, o manx estava vivo; depois a "
            "classificação mudou para \"criticamente ameaçado\". O córnico, da Cornualha, deixou de ser língua viva "
            "no fim do século XVIII, foi reconstruído por um movimento iniciado em 1904 e hoje algumas famílias criam "
            "os filhos com ele como primeira língua."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Manx_language",
                "in 2021, around 2,023 people had varying levels of second-language conversational ability. [...] "
                "a Manx-medium primary school. "
                "The revival of Manx has been made easier because the language was well recorded, e.g. the Bible and the Book of Common Prayer had been translated into Manx, and audio recordings had been made of native speakers. [...] "
                "Manx is a Goidelic language, closely related to Irish and Scottish Gaelic. [...] "
                "Following the decline in the use of Manx during the 19th century [...] "
                "By the mid-20th century, only a few elderly native speakers remained (the last of them, Ned Maddrell, died 27 December 1974) [...] "
                "The revival of Manx was aided by the recording work done in the 20th century by researchers. "
                "Most notably, the Irish Folklore Commission was sent in with recording equipment in 1948 by Éamon de Valera. [...] "
                "In 2009, UNESCO's Atlas of the World's Languages in Danger declared Manx an extinct language, despite the presence of hundreds of speakers on the Isle of Man. "
                "Historian and linguist Jennifer Kewley Draskau reacted to this declaration, stating \"Unesco ought to know better than to declare Manx a dead language. "
                "There are hundreds of speakers of Manx and while people are able to have productive conversations in the language then it is very much alive and well.\" "
                "Since then, UNESCO's classification of the language has changed to \"critically endangered\". [...] "
                "who receive nearly all of their education through the medium of the language.",
                nome="Manx language"),
            wiki("Cornish_language",
                "Cornish became extinct as a living language in Cornwall by the end of the 18th century; but knowledge of Cornish persisted with some families and individuals. "
                "A revival started in the early 20th century, and in 2010 UNESCO reclassified the language as critically endangered, stating that its former classification of the language as extinct was no longer accurate. "
                "The language has a growing number of second-language speakers, and a small but increasing number of families now raise children to speak revived Cornish as a first language. [...] "
                "In 1904, the Celtic language scholar and Cornish cultural activist Henry Jenner published A Handbook of the Cornish Language. "
                "The publication of this book is often considered to be the point at which the revival movement started. [...] "
                "The revival focused on reconstructing and standardising the language",
                nome="Cornish language"),
        ],
    },
    # 9 a língua de sinais criada por crianças na Nicarágua
    {
        "temas_secundarios": ["desenvolvimento_humano", "aprendizagem_inteligencia"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Na Nicarágua, a partir de 1977, crianças surdas reunidas em escolas, que só conheciam gestos caseiros, criaram uma língua de sinais no pátio e no ônibus. As mais novas a deixaram mais complexa.",
        "explicacao": (
            "Antes dos anos 1970, os surdos nicaraguenses viviam isolados uns dos outros e se comunicavam com a "
            "família por sistemas simples de gestos caseiros. Em 1977, um centro de educação especial em Manágua "
            "começou a receber crianças surdas, primeiro 50, depois 100; em 1983, duas escolas já tinham mais de 400 "
            "alunos. O ensino apostava no espanhol falado e na leitura labial, com pouco sucesso. Mas no pátio, na "
            "rua e no ônibus escolar, as crianças juntaram seus gestos e sinais caseiros, e uma língua nova surgiu "
            "depressa. Os professores achavam que aquilo era mímica e, sem entender nada, pediram ajuda. Em 1986, o "
            "Ministério da Educação chamou a linguista americana Judy Kegl, do MIT. Ela e outros pesquisadores "
            "notaram que as crianças mais novas tinham levado a língua dos mais velhos a um nível maior de "
            "complexidade, com concordância verbal e outras regras de gramática. Kegl evitou apresentar aos alunos a "
            "língua de sinais americana. Para linguistas como Kegl, o caso mostra que a aquisição da linguagem é "
            "inata no cérebro humano, e Steven Pinker o descreveu como a única vez em que se viu uma língua ser "
            "criada do nada."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Nicaraguan_Sign_Language",
            "Nicaraguan Sign Language (ISN; Spanish: Idioma de Señas de Nicaragua) is a sign language developed by deaf children in several schools in Nicaragua. [...] "
            "Before the 1970s, a deaf community largely socializing with and amongst each other was not present in Nicaragua. "
            "Deaf people were generally isolated from one another and mostly used simple home sign systems and gesture (mímicas) to communicate with their families and friends [...] "
            "The conditions necessary for a language to arise occurred in 1977 when a center for special education established a plan that was initially attended by 50 deaf children. "
            "The number of pupils at the school (in the Managua neighborhood of San Judas) then grew to 100 by 1979 [...] "
            "By 1983 more than 400 deaf pupils were enrolled in the two schools. "
            "Initially, the language plan emphasized spoken Spanish and lipreading [...] "
            "The plan achieved little success [...] "
            "but the schoolyard, the street, and the school bus provided fertile ground for them to communicate with one another. "
            "By combining gestures and elements of their home-sign systems, a new language rapidly began to emerge. [...] "
            "Staff at the school, unaware of the development of this new language, saw the children's gesturing as mime and a failure to acquire Spanish. "
            "Unable to understand what the children were saying, they asked for outside help. "
            "In June 1986, the Nicaraguan Ministry of Education contacted Judy Kegl, an American Sign Language linguist from MIT. "
            "As Kegl and other researchers began to analyze the language they noticed that the young children had taken the language of the older children to a higher level of complexity, with verb agreement and other conventions of grammar. [...] "
            "Kegl carefully avoided introducing the sign languages that she knew, in particular American Sign Language, to the deaf community in Nicaragua. [...] "
            "Some linguists, such as Kegl and R. J. Senghas, view ISN’s development as proof that language acquisition is hard-wired inside the human brain. [...] "
            "And it's the only time that we've seen a language being created out of thin air.",
            nome="Nicaraguan Sign Language")],
    },
    # 10 ayapaneco: os "dois últimos falantes" que não se falavam
    {
        "temas_secundarios": ["americas_pre_colombianas", "povos_indigenas"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Correu o mundo a história dos dois últimos falantes do ayapaneco, no México, que não se falavam por briga. Mas eles não eram os únicos, e o linguista que os estudou diz que a história \"não é bem verdade\".",
        "explicacao": (
            "O ayapaneco, ou zoque de Ayapa, é falado num vilarejo do estado de Tabasco; seus falantes o chamam de "
            "Nuumte Oote, \"voz verdadeira\". Era uma língua viva até meados do século XX, mas recuou com a escola "
            "obrigatória em espanhol, a urbanização e a migração. Em 2010 começou a circular a história de que os "
            "dois últimos falantes, Manuel Segovia e Isidro Velázquez, eram inimigos e não conversavam. Ela saiu na "
            "revista Time e no Huffington Post e, em 2013, virou campanha publicitária da Vodafone. Segundo o "
            "antropólogo Daniel Suslak, da Universidade de Indiana, que trabalhou com os dois por dez anos, eles eram "
            "de longe os melhores falantes, mas não os únicos: ainda havia irmãos de Isidro e um primo de Manuel. "
            "Suslak observou ainda que, diferenças pessoais à parte, um motivo para não conversarem em ayapaneco é "
            "que cada um o falava de um jeito bem diferente. Os dois chegaram a dar aulas da língua juntos a crianças "
            "e adolescentes, e o filho de Manuel passou a manter uma escola de ayapaneco no vilarejo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Ayapaneco_language",
                "Ayapa Zoque (Ayapaneco), or Tabasco Zoque, is a critically endangered  Zoquean language of Ayapa, a village 10 kilometres (6 mi) southeast of Comalcalco, in Tabasco, Mexico. "
                "The native name is Nuumte Oote \"True Voice\". "
                "A vibrant, albeit minority, language until the middle of the 20th century, the language suffered after the introduction of compulsory education in Spanish, urbanisation, and migration of its speakers. [...] "
                "In 2010, a story started circulating that the last two speakers of the Ayapaneco language were enemies and no longer talked to each other. "
                "The story was incorrect, and while it was quickly corrected it came to circulate widely. [...] "
                "In 2013, Vodafone launched an advertisement campaign in which they claimed to have helped the community revitalize the language, proposing an erroneous story of enmity between Don Manuel and Don Isidro. [...] "
                "\"Last Two Speakers of Dying Language Refuse to Talk to Each Other\". Time. [...] "
                "\"Last 2 Speakers Of Dying Language Won't Speak To Each Other\". Huffington Post.",
                nome="Ayapaneco language"),
            {"url": "https://ictnews.org/archive/fighting-off-extinction-the-story-of-indigenous-mexican-languages/",
             "titulo": "Fighting Off Extinction: The Story of Indigenous Mexican Languages (ICT, 2014)",
             "idioma": "en",
             "trecho": "the last two speakers, Manuel Segovia, 78, and Isidro Velazquez (also known as Don Chilo) in his 70s, were not speaking to each other. "
                       "But according to Anthropologist Daniel Suslak of Indiana University, who has worked with the two Ayapaneco men for 10 years, that story is not accurate. "
                       "“The narrative of the last two speakers who don’t speak to each other is a powerful one,” Suslak stated. "
                       "“It strikes a chord with a lot of people. It just happens to not be quite true.” [...] "
                       "“While Manuel and Isidro are far and away the best remaining speakers of Ayapaneco, they are not the only two left,” he asserted. "
                       "“Several of the speakers that I met have passed away in recent years, but a handful still remain, including Isidro’s brothers and sister and a cousin of Manuel.” "
                       "Along with those family members, Segovia’ son, also named Manuel, has been running an Ayapaneco language school in their village"},
            {"url": "https://www.ibtimes.com/why-last-two-speakers-obscure-mexican-language-known-ayapaneco-dont-talk-each-other-1505038",
             "titulo": "Why The Last Two Speakers Of Obscure Mexican Language Known As Ayapaneco Don't Talk To Each Other (IBTimes, 2013)",
             "idioma": "en",
             "trecho": "teach Ayapaneco together to a few dozen children and teenagers. [...] "
                       "In an article for the journal American Anthropologist, Daniel Suslak, associate professor at Indiana University in Bloomington, Ind., notes, “…personal differences aside, one of the reasons why Manuel and Chilo do not speak to each other in Ayapaneco is because they speak it quite differently.”"},
        ],
    },
    # 11 as "100 palavras para neve"
    {
        "temas_secundarios": ["estruturas_linguisticas", "clima_tempo"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "As \"cem palavras dos esquimós para neve\" começaram como uma lista de quatro, em 1911, e foram infladas até cem num editorial de 1984. Mas a resposta real depende do que se conta como palavra.",
        "explicacao": (
            "O ponto de partida foi o antropólogo Franz Boas. Em 1911, ele citou quatro palavras inuítes, como \"aput\", "
            "neve no chão, e \"qana\", neve caindo, num argumento sobre como as línguas recortam as ideias de jeitos "
            "diferentes. Boas não fez contas: notou que essas línguas têm mais ou menos tantas raízes para neve quanto "
            "o inglês. Em 1940, Benjamin Lee Whorf usou o exemplo para defender que a língua molda a visão de mundo. "
            "Depois, outros autores inflaram o número: em 1978 já se falava em cinquenta, e em 1984 um editorial do New York "
            "Times chegou a cem. O linguista Geoffrey Pullum chamou o processo de \"a grande farsa do vocabulário "
            "esquimó\". A complicação é que as línguas inuítes e iupiques formam palavras novas juntando sufixos, e "
            "assim dá para criar um número quase ilimitado de palavras sobre qualquer assunto. Mesmo assim, o "
            "antropólogo Igor Krupnik, do Smithsonian, e colegas mapearam cerca de dez dialetos e concluíram que eles "
            "têm muito mais palavras para neve que o inglês: pelo menos 53 num dialeto do Canadá. E os sámis da "
            "Escandinávia, cujas línguas não funcionam assim, usam pelo menos 180 palavras ligadas a neve e gelo."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Eskimo_words_for_snow",
            "a 2010 study supports the core notion that the Yupik and Inuit languages have many more root words for frozen variants of water than the English language. [...] "
            "Franz Boas did not make quantitative claims but rather pointed out that the Eskaleut languages have about the same number of distinct word roots referring to snow as English does, but have rich derivational morphology which can create many different words from the same root. "
            "A good deal of the ongoing debate thus depends on how one defines \"word\" [...] "
            "calling the process by which the so-called \"myth\" was created the \"Great Eskimo Vocabulary Hoax\". [...] "
            "Languages in the Inuit and Yupik language groups add suffixes to words to express the same concepts expressed in English and many other languages by means of compound words, phrases, and even entire sentences. "
            "One can create a practically unlimited number of new words in the Eskimoan languages on any topic, not just snow [...] "
            "Igor Krupnik, an anthropologist at the Smithsonian Arctic Studies Center in Washington [...] "
            "Krupnik and others charted the vocabulary of about 10 Inuit and Yupik dialects and concluded that they indeed have many more words for snow than English does. [...] "
            "In Nunavimmiutitut, the Inuktitut dialect spoken in Canada's Nunavik region has at least 53 [...] "
            "the Sámi peoples, who live in the northern tips of Scandinavia and Russia, use at least 180 words related to snow and ice [...] "
            "Unlike Inuit dialects, Sámi languages are not polysynthetic [...] "
            "The first reference to Inuit having multiple words for snow is in the introduction to Handbook of American Indian languages (1911) by linguist and anthropologist Franz Boas. [...] "
            "Here we find one word, aput, expressing SNOW ON THE GROUND; another one, qana, FALLING SNOW [...] "
            "The  hypothesis of  linguistic relativity put forth by Edward Sapir and Benjamin Lee Whorf, holds that the language we speak both affects and reflects our view of the world. [...] "
            "In a popular 1940 article on the subject, Whorf referred to Eskimo languages having several words for snow [...] "
            "by 1978, the number quoted had reached fifty, and on February 9, 1984, an unsigned editorial in the New York Times gave the number as one hundred.",
            nome="Eskimo words for snow")],
    },
    # 12 malgaxe: o parente em Bornéu
    {
        "temas_secundarios": ["navegacao_antiga", "africa_antiga"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "A língua de Madagascar, junto à África, tem como parente mais próximo o ma'anyan, falado em Bornéu, na Indonésia. Os primeiros falantes chegaram de ilhas a cerca de 7.300 km de distância.",
        "explicacao": (
            "O malgaxe, falado por cerca de 25 milhões de pessoas em Madagascar e Comores, é a língua austronésia "
            "mais a oeste do mundo. Ele pertence ao grupo das línguas de Barito, nome de um rio do sul de Bornéu. Já "
            "no século XVII se notavam semelhanças com o malaio, e em 1951 o linguista Dahl mostrou um parentesco "
            "especialmente próximo com o ma'anyan, falado em Kalimantan, a parte indonésia de Bornéu. As duas línguas "
            "compartilham boa parte do vocabulário básico. O malgaxe chegou à ilha com povoadores vindos das ilhas da "
            "Sonda por volta do século V, ou talvez entre os séculos VII e XIII. Segundo uma explicação, gente "
            "ma'anyan teria sido levada como mão de obra e como escravos em frotas comerciais malaias e javanesas. "
            "Depois do ano 1000, os povoadores austronésios se misturaram a bantos e árabes, e a língua absorveu "
            "muitas palavras desses idiomas, trazidas por comerciantes e novos colonos. Há ainda empréstimos do "
            "sânscrito, que provavelmente chegaram via javanês, e, mais recentemente, do francês e do inglês."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Malagasy_language",
            "Malagasy is the westernmost Austronesian language, brought to Madagascar with the settlement of Austronesian speakers from the Sunda Islands (about 7,300 kilometres or 4,500 miles away) around the 5th century AD or perhaps between the 7th and 13th centuries. "
            "The Malagasy language is one of the Barito languages and is most closely related to the Maʼanyan language, still spoken on Borneo. [...] "
            "After c. 1000 AD, Malagasy incorporated numerous Bantu and Arabic loanwords brought over by traders and new settlers. "
            "Malagasy is spoken by around 25 million people in Madagascar and the Comoros. [...] "
            "It is known that Ma'anyan people were brought as labourers and slaves by Malay and Javanese people in their trading fleets [...] "
            "Later, c. 1000, the original Austronesian settlers mixed with Bantus and Arabs, amongst others. [...] "
            "Malay) had been observed since the 17th century [...] "
            "Dahl (1951) demonstrated that Malagasy and Maʼanyan Dayak – an East Barito language natively spoken in Central Kalimantan (Indonesia) on the island of Kalimantan – were particularly closely related. [...] "
            "There are some Sanskrit loanwords in Malagasy, which are said to have been borrowed via Javanese (mainly). [...] "
            "the early Malagasy speakers migrated to East Africa. [...] "
            "Malagasy shares much of its basic vocabulary with the Ma'anyan language, a language from the region of the Barito River in southern Borneo. "
            "The Malagasy language also includes some borrowings from Sanskrit, Arabic and Bantu languages [...] and more recently from French and English.",
            nome="Malagasy language")],
    },
    # 13 tocário: indo-europeu no deserto da China
    {
        "temas_secundarios": ["asia_antiga", "comercio_rotas"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "A língua indo-europeia mais a leste, o tocário, foi escrita entre os séculos V e VIII no noroeste da China. E o chinês \"mì\", mel, pode vir dela, primo do inglês \"mead\", hidromel.",
        "explicacao": (
            "Ninguém suspeitava da existência do tocário até que, no início do século XX, expedições como a de Aurel "
            "Stein acharam, em cidades-oásis da bacia do Tarim, hoje na região de Xinjiang, manuscritos numa língua "
            "desconhecida. Logo se viu que eram duas línguas aparentadas, depois chamadas tocário A e tocário B, de "
            "um ramo até então ignorado da família indo-europeia. O tocário A servia como língua litúrgica budista. "
            "A descoberta abalou uma ideia do século XIX: a de que a divisão da família entre línguas \"centum\" e "
            "\"satem\" seguia uma linha oeste-leste, com as centum no oeste. O tocário era centum, apesar de ser o "
            "ramo mais oriental. A maioria dos estudiosos liga os ancestrais dos tocários à cultura de Afanasievo, "
            "no sul da Sibéria, de cerca de 3300 a 2500 a.C. A língua provavelmente desapareceu depois de 840, quando "
            "os uigures se mudaram para a bacia do Tarim. Algumas palavras do chinês moderno podem ter origem "
            "tocária ou aparentada, como \"mì\", mel, que seria parente do eslavo eclesiástico antigo \"medŭ\" e do "
            "inglês \"mead\"."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Tocharian_languages",
            "are an extinct branch of the Indo-European language family spoken by inhabitants of the Tarim Basin, the Tocharians. "
            "The languages are known from manuscripts dating from the 5th to the 8th century AD, which were found in oasis cities on the northern edge of the Tarim Basin (now part of Xinjiang in Northwest China) and the Lop Desert. [...] "
            "The discovered manuscripts record two closely related languages, called Tocharian A [...] "
            "The subject matter of the texts suggests that Tocharian A was more archaic and used as a Buddhist liturgical language [...] "
            "The existence of the Tocharian languages and alphabet was not even suspected until archaeological exploration of the Tarim Basin by Aurel Stein in the early 20th century brought to light fragments of manuscripts in an unknown language [...] "
            "belonging to a hitherto unknown branch of Indo-European, now known as Tocharian [...] "
            "In the 19th century, it was thought that the division between centum and satem languages was a simple west–east division, with centum languages in the west. "
            "The theory was undermined in the early 20th century by the discovery of Hittite, a centum language in a relatively eastern location, and Tocharian, which was a centum language despite being the easternmost branch. [...] "
            "Most scholars identify the ancestors of the Tocharians with the Afanasievo culture of South Siberia (c. 3300–2500 BC) [...] "
            "Tocharian probably died out after 840 when the Uyghurs, expelled from Mongolia by the Kyrgyz, moved into the Tarim Basin. [...] "
            "Some modern Chinese words may ultimately derive from a Tocharian or related source, e.g. Old Chinese *mit (蜜; mì) Cantonese mat6 \"honey\", from Proto-Tocharian [...] "
            "cognate with Old Church Slavonic медъ (transliterated: medŭ) (meaning \"honey\"), and English mead.",
            nome="Tocharian languages")],
    },
    # 14 dene-ieniseiano: Sibéria e navajo
    {
        "temas_secundarios": ["pre_historia", "genetica"],
        "tipos_espanto": ["misterio_aberto", "conexao_inesperada"],
        "gancho": "Uma hipótese ainda em debate liga o ket, língua da Sibéria central, ao navajo e às línguas apaches da América do Norte. Em 2025, um estudo genético trouxe o primeiro apoio do DNA à ideia.",
        "explicacao": (
            "A proposta se chama família dene-ieniseiana: uniria as línguas ieniseianas, da Sibéria central, das "
            "quais só o ket continua vivo, e a família na-dene, da América do Norte, que inclui o navajo, a língua "
            "indígena mais falada ao norte do México. A ligação foi sugerida em 1923, mas ganhou força com o "
            "linguista Edward Vajda, que em 2008 apresentou dez anos de pesquisa: mais de 110 elementos de palavras "
            "possivelmente aparentados e semelhanças na estrutura dos verbos, cheios de prefixos nas duas famílias. "
            "Vários especialistas receberam a proposta bem, às vezes com cautela. Outros, como Lyle Campbell, seguem "
            "achando as provas insuficientes, e o próprio Vajda a chamou de hipótese de parentesco, ainda não uma "
            "classificação pronta. Um estudo de 2014, com métodos estatísticos, sugeriu que o mais provável seria uma "
            "irradiação a partir da Beríngia, com uma volta posterior à Ásia Central, e não uma migração da Ásia para "
            "a América. Em 2025, geneticistas acharam a contribuição de uma mesma população antiga, que vivia a oeste "
            "do lago Baikal, tanto em povos atabascanos do Alasca quanto nos ieniseianos atuais."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "hipotese",
        "fontes": [
            wiki("Dene%E2%80%93Yeniseian_languages",
                "is a proposed language family consisting of the Yeniseian languages of central Siberia and the Na-Dene languages of North America. [...] "
                "The putative relationship between Na–Dene and Yeniseian families was first proposed by Alfredo Trombetti in 1923. [...] "
                "At a symposium in Alaska in 2008, Vajda summarized ten years of research, based on verbal morphology and reconstructions of the proto–languages, indicating that the Yeniseian and Na–Dene families might be related. [...] "
                "The evidence offered by Vajda includes over 110 proposed cognate morphemes and about ten homologous prefix and suffix positions of the verbs. [...] "
                "In his 2012 reply to George Starostin, Vajda clarifies that Dene–Yeniseian \"as it currently stands is a hypothesis of language relatedness but not yet a proper hypothesis of language taxonomy\". [...] "
                "At the time of publication, Vajda's proposals had been favorably reviewed by several specialists of Na–Dene and Yeniseian languages—although at times with caution [...] "
                "Sicoli and Holton 2014, applying Bayesian analysis to typological data from Dene and Yeniseian languages, constructed phylogenies that suggest that the Dene–Yeniseian connection \"more likely represents a radiation out of Beringia with a back migration into Central Asia than a migration from Central Asia or Western Asia to North America\". [...] "
                "As of 2024, Lyle Campbell continues to doubt the validity of Dene–Yeniseian, saying that \"neither the lexical evidence with putative sound correspondences nor the morphological evidence adduced has proven sufficient to support a genealogical relationship between Na–Dene and Yeniseian\". "
                "In 2025, a team of geneticists provided evidence that the ancient Paleo-Siberian genetic contribution to Athabaskan populations in Alaska stemmed from a population that lived to the west of Lake Baikal in the Late Neolithic and Bronze Age, and that this population also contributed genetically to modern Yeniseian populations. "
                "The authors of the study interpret this as \"providing the first genetic data in support of the 'Dene-Yeniseian' hypothesis.\"",
                nome="Dene–Yeniseian languages"),
            wiki("Na-Dene_languages",
                "By far the most widely spoken Na-Dene language today is Navajo, which is also the most spoken indigenous language north of Mexico. "
                "Some linguists have proposed a genetic relationship between Na-Dene and the Yeniseian languages of central Siberia, termed Dene–Yeniseian. "
                "However, this proposal is not universally accepted. [...] "
                "The southwestern division of Athabaskan is also called Southern Athabaskan or Apachean, and includes Navajo and all the Apache languages. [...] "
                "the Na-Dené languages might be related to the Yeniseian (or Yeniseic) languages of Siberia, the only living representative of which is the Ket language. "
                "The core motivations for the proposed family connection are homologies in verb prefixes",
                nome="Na-Dene languages"),
        ],
    },
    # 15 a fábula de Schleicher em protoindo-europeu
    {
        "temas_secundarios": ["pre_historia", "literatura"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Em 1868, um linguista escreveu uma fábula numa língua reconstruída, o protoindo-europeu, da qual não há nenhum texto. Ela foi reescrita várias vezes desde então, porque a reconstrução mudou muito.",
        "explicacao": (
            "O alemão August Schleicher foi o primeiro estudioso a compor um texto em protoindo-europeu. A fábula, "
            "\"*Avis akvāsas ka\", \"A ovelha e os cavalos\", conta que uma ovelha sem lã vê cavalos, um puxando uma "
            "carroça pesada, outro carregando um grande fardo e outro levando um homem depressa. A ovelha diz que lhe "
            "dói o coração ver um homem conduzindo cavalos. Os cavalos respondem que dói neles ver o homem, o dono, "
            "transformar a lã da ovelha num agasalho para si, deixando-a sem lã. Ao ouvir isso, a ovelha foge para a "
            "planície. Desde então, vários estudiosos publicaram versões revistas: Hermann Hirt, publicada em 1939, "
            "Winfred Lehmann e Ladislav Zgusta em 1979, Douglas Adams em 1997, Frederik Kortlandt em 2007, entre "
            "outros. Comparadas lado a lado, as versões mostram o quanto a reconstrução mudou em 150 anos. A de "
            "Schleicher se apoiava muito mais no sânscrito que as modernas. Adams foi o primeiro a incorporar "
            "plenamente a teoria das laringais, sons que se supõe terem existido na língua, e por isso sua versão já "
            "não tem o \"ā\" longo de Schleicher. Kortlandt chegou a trocar os símbolos abstratos dessas laringais "
            "pelos sons que imagina para elas."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Schleicher%27s_fable",
            "Schleicher’s fable is a text composed as a reconstructed version of the Proto-Indo-European language (PIE), published by August Schleicher in 1868. "
            "Schleicher was the first scholar to compose a text in PIE. "
            "The fable is entitled *Avis akvāsas ka (‘The Sheep [Ewe] and the Horses’). "
            "At later dates, various scholars have published revised versions of Schleicher’s fable, as the idea of how PIE should be presented and pronounced has changed over time. "
            "The resulting parallel texts serve as an illustration of the significant changes that the reconstruction of the language has experienced during the last 150 years of scholarly efforts. "
            "The first revision of Schleicher’s fable was made by Hermann Hirt (published by Arntz in 1939). "
            "A second revision was published by Winfred Lehmann and Ladislav Zgusta in 1979. "
            "Another version by Douglas Q. Adams appeared in the Encyclopedia of Indo-European Culture (1997:501). "
            "In 2007 Frederik Kortlandt published yet another version on his internet homepage. [...] "
            "(1) A sheep that had no wool saw horses, one of them pulling a heavy wagon, one carrying a big load, and one carrying a man quickly. "
            "(2) The sheep said to the horses: \"My heart pains me, seeing a man driving horses.\" "
            "(3) The horses said: \"Listen, sheep, our hearts pain us when we see this: a man, the master, makes the wool of the sheep into a warm garment for himself. "
            "And the sheep has no wool.\" [...] "
            "(4) Having heard this, the sheep fled into the plain. [...] "
            "Schleicher’s reconstruction assumed that the o/e vocalism was secondary, and his version of PIE is based much more closely on Sanskrit than modern reconstructions. [...] "
            "Adams was the first one to represent fully the laryngeal theory in his version of the fable. [...] "
            "Consequently, Adams’ text no longer shows long ā. [...] "
            "Second, he substitutes the abstract laryngeal signs with their supposed phonetic values",
            nome="Schleicher's fable")],
    },
    # 16 "uma língua é um dialeto com exército e marinha" e o chinês
    {
        "temas_secundarios": ["fronteiras_paises", "asia_antiga"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "A frase \"uma língua é um dialeto com exército e marinha\" ficou famosa com o linguista Max Weinreich. Mas ele a ouviu de um professor de escola do Bronx, na plateia de uma palestra sua, nos anos 1940.",
        "explicacao": (
            "Weinreich, estudioso do iídiche, publicou a frase pela primeira vez num texto apresentado como discurso "
            "em 5 de janeiro de 1945. Ali, contou que, depois de uma palestra de uma série dada entre 1943 e 1944, um "
            "ouvinte o procurou: um professor de uma escola do Bronx que chegara criança aos Estados Unidos e nunca "
            "tinha ouvido falar que o iídiche tinha história. Ele perguntou a diferença entre dialeto e língua e, "
            "antes que Weinreich respondesse, ofereceu a própria definição. A tirada resumia a situação social do "
            "iídiche e virou o jeito mais curto de dizer que o status de língua depende mais de condições sociais e "
            "políticas que de critérios linguísticos. O chinês é um bom exemplo. Suas centenas de variedades locais "
            "costumam ser chamadas de dialetos, mas muitas não se entendem entre si: diferem pelo menos tanto quanto "
            "as línguas românicas e talvez tanto quanto as indo-europeias como um todo. Nos dois casos, uma língua "
            "imperial se espalhou há cerca de 2.000 anos. A diferença é que a China recuperou a unidade política no "
            "século VI, com a dinastia Sui, e a manteve, enquanto a Europa se dividiu em muitos Estados "
            "independentes."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("A_language_is_a_dialect_with_an_army_and_navy",
                "It was originally said in the context of the \"social plight of Yiddish\", and has been widely adopted as a shorthand for the importance of social and political conditions, rather than purely linguistic considerations, in defining the status of a language or dialect. "
                "The witticism was popularized by the sociolinguist and Yiddish scholar Max Weinreich, who heard it from a member of the audience at one of his lectures in the 1940s. [...] "
                "The earliest known published source is Weinreich's article [...] "
                "originally presented as a speech on 5 January 1945 at the annual YIVO conference. [...] "
                "In the article, Weinreich presents this statement as a remark of an auditor at a lecture series given between 13 December 1943 and 12 June 1944: "
                "A teacher at a Bronx high school once appeared among the auditors. "
                "He had come to America as a child and the entire time had never heard that Yiddish had a history and could also serve for higher matters. [...] "
                "Once after a lecture he approached me and asked, \"What is the difference between a dialect and language?\" "
                "I thought that the maskilic contempt had affected him, and tried to lead him to the right path, but he interrupted me: "
                "\"I know that, but I will give you a better definition. A language is a dialect with an army and navy.\"",
                nome="A language is a dialect with an army and navy"),
            wiki("Varieties_of_Chinese",
                "There are hundreds of local Chinese language varieties forming a branch of the Sino-Tibetan language family, many of which are not mutually intelligible. [...] "
                "Local varieties from different areas of China are often mutually unintelligible, differing at least as much as different Romance languages and perhaps even as much as Indo-European languages as a whole. "
                "As with the Romance languages descended from Latin, the ancestral language was spread by imperial expansion over substrate languages around 2000 years ago [...] "
                "However, a major difference between China and Western Europe is the historical reestablishment of political unity in 6th century China by the Sui dynasty, a unity that has persisted with relatively brief interludes until the present day. "
                "Meanwhile, Europe remained politically decentralized, developing into numerous independent states.",
                nome="Varieties of Chinese"),
        ],
    },
]
