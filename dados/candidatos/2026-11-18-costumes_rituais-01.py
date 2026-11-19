LOTE = "2026-11-18-costumes_rituais-01"
AREA = "sociedade"
TEMA = "costumes_rituais"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o anel kula: colares e braceletes que giram entre ilhas
    {
        "temas_secundarios": ["economia_curiosa", "navegacao_antiga"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Em ilhas da Papua-Nova Guiné, colares de concha circulam de ilha em ilha no sentido horário e braceletes no anti-horário. Não servem para nada prático, e o prestígio vem de passá-los adiante.",
        "explicacao": (
            "O sistema se chama kula e liga 18 comunidades do arquipélago Massim, entre elas as ilhas Trobriand, "
            "com milhares de participantes. Há dois tipos de objeto: colares vermelhos de discos de concha, que "
            "seguem rumo ao norte, girando no sentido horário, e braceletes brancos de concha, que vão para o sul, "
            "no sentido contrário. Quem abre uma troca com um bracelete recebe de volta um colar, e vice-versa. As "
            "pessoas chegam a viajar centenas de milhas de canoa para isso. Os objetos não têm uso: não ficam muito tempo nas "
            "mãos de ninguém e precisam ser repassados a outro parceiro dentro de certo prazo. Ainda assim, até a "
            "posse temporária dá status, e as parcerias, idealmente para a vida toda, trazem deveres de "
            "hospitalidade e proteção. Num livro de 1922, o antropólogo Bronisław Malinowski tornou o kula famoso "
            "com uma pergunta: por que homens arriscariam a vida no mar para dar o que parecem bugigangas sem "
            "valor? A resposta ligava as trocas à autoridade política. Em 1925, Marcel Mauss retomou o caso no "
            "\"Ensaio sobre a dádiva\", e o kula virou peça central do debate sobre as economias baseadas em "
            "presentes. Nas mesmas viagens, porém, também se faz escambo comum, com regateio duro."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Kula_ring",
            "Kula, also known as the Kula exchange or Kula ring, is a ceremonial exchange system conducted in the Milne Bay Province of Papua New Guinea. [...] "
            "His seminal work on the topic, Argonauts of the Western Pacific (1922), directly confronted the question, \"Why would men risk life and limb to travel across huge expanses of dangerous ocean to give away what appear to be worthless trinkets?\" "
            "Malinowski carefully traced the network of exchanges of bracelets and necklaces across the Trobriand Islands and established that they were part of a system of exchange (the Kula ring) and that the exchange system was clearly linked to political authority. "
            "Malinowski's study became the subject of debate with the French anthropologist Marcel Mauss, the author of The Gift (\"Essai sur le don,\" 1925). "
            "Since then, the Kula ring has been central to the continuing anthropological debate on the nature of gift-giving and the existence of gift economies. [...] "
            "The Kula ring spans 18 island communities of the Massim archipelago, including the Trobriand Islands, and involves thousands of individuals. "
            "Participants travel at times hundreds of miles by canoe to exchange Kula valuables, which consist of red shell-disc necklaces (veigun or soulava) that are traded to the north (circling the ring in clockwise direction) and white shell armbands (mwali) that are traded in the southern direction (circling counterclockwise). "
            "If the opening gift was an armband, the closing gift must be a necklace and vice versa. "
            "The exchange of Kula valuables is also accompanied by the trade in other items known as gimwali (barter). [...] "
            "All Kula valuables are non-use items traded purely for purposes of enhancing one's social status and prestige. [...] "
            "relationships between the exchange parties (karayta'u, \"partners\"). [...] "
            "Such a partnership involves strong mutual obligations such as hospitality, protection and assistance. [...] "
            "Kula valuables never remain for long in the hands of the recipients; rather, they must be passed on to other partners within a certain amount of time and thus constantly circle around the ring. "
            "However, even temporary possession brings prestige and status. [...] "
            "the latter, in contrast, often done as part of Kula exchange journeys, involves hard bargaining and serves purely economic purposes.",
            nome="Kula ring")],
    },
    # 2 o potlatch, festa proibida no Canadá
    {
        "temas_secundarios": ["leis_julgamentos", "economia_curiosa"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Do fim do século XIX até 1951, o Canadá proibiu por lei uma festa indígena: o potlatch, em que um anfitrião ganha prestígio dando, e às vezes destruindo, riquezas. A pena prevista ia de dois a seis meses de prisão.",
        "explicacao": (
            "O potlatch é praticado por povos indígenas da costa noroeste do Pacífico, como os haida, os tlingit "
            "e os kwakwaka'wakw. Mais que uma festa, é tradicionalmente a principal instituição de governo e o "
            "sistema econômico desses povos. Acontece em nascimentos, mortes, casamentos e outros marcos, e nele se "
            "transmitem títulos que dão direito a territórios de caça, pesca e coleta. O status de uma família não "
            "sobe com o que ela acumula, mas com o que ela distribui. O nome vem do jargão chinook e quer dizer "
            "\"dar\". Missionários e agentes do governo viam o costume como desperdício, contrário aos valores "
            "\"civilizados\" de acumulação, e uma emenda de 1884 à Lei dos Índios o tornou crime, com pena de dois "
            "a seis meses de prisão. Em 1888, o antropólogo Franz Boas já chamava a proibição de fracasso: as "
            "aldeias eram numerosas demais e o governo não conseguia fiscalizá-las. O potlatch continuou às "
            "escondidas até a lei ser revogada, em 1951. Hoje voltou a ser feito abertamente em várias "
            "comunidades, e a nação haida baseia a sua democracia na lei do potlatch."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Potlatch",
            "Potlatch is the gift-giving feast practiced by Indigenous peoples of the Pacific Northwest Coast of Canada and the United States, among whom it is traditionally the primary governmental institution, legislative body, and economic system. "
            "This includes the Heiltsuk, Haida, Nuxalk, Tlingit, Makah, Tsimshian, Nuu-chah-nulth, Kwakwaka'wakw, and Coast Salish cultures. [...] "
            "A potlatch involves giving away or destroying wealth or valuable items in order to demonstrate a leader's wealth and power. [...] "
            "From 1885 to 1951, the Government of Canada criminalized potlatches. "
            "However, the practice persisted underground despite the risk of government reprisals including mandatory jail sentences of at least two months; [...] "
            "Since the practice was decriminalized in 1951, the potlatch has re-emerged in some communities. "
            "In many it is still the bedrock of Indigenous governance, as in the Haida Nation, which has rooted its democracy in potlatch law. "
            "The word comes from the Chinook Jargon, meaning \"to give away\" or \"a gift\"; [...] "
            "A potlatch was held on the occasion of births, deaths, adoptions, weddings, and other major events. [...] "
            "These ranked titles granted rights to hunting, fishing and berrying territories. [...] "
            "The status of any given family is raised not by who has the most resources, but by who distributes the most resources. [...] "
            "Potlatching was made illegal in Canada in 1884 in an amendment to the Indian Act. "
            "To some extent, this was at the urging of missionaries and government agents who considered it \"a worse than useless custom\" that was seen as wasteful, unproductive, and contrary to 'civilized values' of accumulation. [...] "
            "shall be liable to imprisonment for a term not more than six nor less than two months in any gaol or other place of confinement; [...] "
            "In 1888, the anthropologist Franz Boas described the potlatch ban as a failure: [...] "
            "Besides, the Government is unable to enforce it. "
            "The settlements are so numerous, and the Indian agencies so large, that there is nobody to prevent the Indians doing whatsoever they like. [...] "
            "The potlatch ban was repealed in 1951. [...] "
            "Indigenous people now openly hold potlatches to commit to the restoring of their ancestors' ways.",
            nome="Potlatch")],
    },
    # 3 o Ratoncito Pérez foi escrito para um rei de 8 anos
    {
        "temas_secundarios": ["literatura", "cultura_popular"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O Ratoncito Pérez, o ratinho que troca dentes de leite por presentes na Espanha e na América hispânica, tem autor e data: virou o \"ratinho dos dentes\" num conto de 1894 escrito para o rei Afonso XIII, aos 8 anos.",
        "explicacao": (
            "Um rato chamado Pérez já aparecia em contos populares espanhóis, como marido de uma formiguinha, em "
            "histórias publicadas em 1877. Quem o transformou num negociante de dentes foi o escritor Luis Coloma. "
            "Em 1894, a rainha Maria Cristina encomendou a ele uma história para o filho, o rei Afonso XIII, que "
            "tinha perdido um dente aos oito anos. No conto, o rato mora com a família numa caixa de biscoitos no "
            "porão de uma confeitaria de Madri, a Prast, e foge pelos canos da cidade até os quartos das crianças "
            "que perderam dentes, sempre enganando os gatos pelo caminho. O pequeno rei aparece na história com o "
            "apelido que a mãe lhe dava, \"Buby\". O texto só foi publicado em 1902, e o manuscrito original, com "
            "dedicatória ao rei, está guardado no Palácio Real de Madri. Hoje a tradição é quase universal no "
            "mundo hispânico: a criança põe o dente debaixo do travesseiro, e o ratinho o troca por um pequeno "
            "pagamento ou presente. Em 2003, Madri pôs uma placa no endereço onde o rato \"morava\", e ele se "
            "tornou o primeiro personagem de ficção homenageado assim pela prefeitura da cidade."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Ratoncito_Pérez",
            "El Ratoncito Pérez or Ratón Pérez (lit. transl. Perez the Little Mouse or Perez Mouse) is a fantasy figure of early childhood in Spanish and Hispanic American cultures. "
            "The folklore states that when children lose one of their milk teeth, they should place it underneath their pillow or on their bedside table and he will visit while they sleep, replacing the lost tooth with a small payment or gift, as does the Tooth Fairy in other cultures. "
            "Although he first appeared in oral tradition folktales such as The Vain Little Mouse, it was Luis Coloma who in 1894 turned him into a tooth dealer in a tale written for an eight-year-old King Alfonso XIII. "
            "The tradition is almost universal in Spanish cultures, with some slight differences. [...] "
            "first appeared in the oral tradition folktales La hormiguita (transl. The Little Ant), as her gentle and timid husband, and in The Vain Little Mouse, also as her husband. "
            "These tales were first published in Cuentos, oraciones, adivinanzas y refranes populares (1877) by Fernán Caballero. [...] "
            "In 1894, Queen Maria Christina commissioned Coloma to write a tale for King Alfonso XIII, who had just lost a tooth at the age of eight. "
            "Coloma's story follows Ratón Pérez, who lived with his family in a box of cookies at the basement of Prast confectionery store in Madrid, but frequently ran away from home through the pipes of the city, and into the bedrooms of children who had lost their teeth. "
            "The story details how he cunningly misleads any cats in the vicinity who may be lurking, and includes his interaction with King Buby (Queen Maria Christina's nickname for Alfonso XIII). "
            "The tale was first published in 1902 together with other stories in Nuevas lecturas. [...] "
            "Coloma's original manuscript, with his signature and a dedication to King Alfonso XIII, is now kept in the vault of the Royal Library at Royal Palace of Madrid. "
            "In 2003, the City Council of Madrid paid tribute to Ratón Pérez with a commemorative plaque at the façade of Number 8 Calle del Arenal, where the mouse was said to have lived. [...] "
            "He thus became the first fictional character honored with a plaque by the City Council.",
            nome="Ratoncito Pérez")],
    },
    # 4 o gato de Natal islandês e a lã do outono
    {
        "temas_secundarios": ["mitologia", "moda"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "No folclore de Natal da Islândia, um gato gigante devora quem não ganhou roupa nova. A ameaça era usada nas fazendas para os trabalhadores terminarem de processar a lã do outono antes do Natal.",
        "explicacao": (
            "O Jólakötturinn, o \"gato de Natal\", seria enorme e cruel e rondaria o campo nevado nessa época do "
            "ano. Em algumas versões, ele come as pessoas sem roupa nova; em outras, só a comida delas. A primeira "
            "menção segura está numa coletânea de folclore de 1862, de Jón Árnason, que não indicou de onde tirou a "
            "história. A origem é discutida: um folclorista acha que o monstro nasceu de uma expressão, \"vestir o "
            "gato\", citada numa nota do próprio Jón; um arqueólogo o liga a figuras que acompanhavam São Nicolau em "
            "outras tradições europeias. O uso prático, porém, aparece na tradição: a ameaça do gato servia de "
            "incentivo para os trabalhadores das fazendas terminarem, antes do Natal, de processar a lã colhida no "
            "outono. Quem participava do trabalho ganhava roupa nova; quem não participava ficava sem nada e virava "
            "presa do gato. A fama definitiva veio com um poema de 1932, de Jóhannes úr Kötlum, e depois o gato "
            "passou a ser tratado como bicho de estimação da ogra Grýla e de seus filhos, os rapazes do Natal "
            "islandês. Em 2018, Reykjavík instalou na praça central uma escultura do gato, de 5 metros."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Yule_Cat",
            "The Yule cat (Icelandic: Jólakötturinn, IPA: [ˈjouːlaˌkʰœhtʏrɪn], also called Jólaköttur and the Christmas cat) is a mythical cat in Icelandic Christmas folklore. "
            "It is said to be huge, vicious, to lurk in the snowy countryside during the Christmas season, and to eat people who do not receive new clothing before Christmas Eve. "
            "In other versions of the story, the cat only eats the food of the people who had not received new clothing. [...] "
            "considered the pet of the ogress Grýla and her sons, the Yule Lads. [...] "
            "The first definitive mention of the Yule cat is from an 1862 collection of folklore by Jón Árnason, [...] "
            "Jón gave no source for either story. [...] "
            "folklorist Árni Björnsson points to a footnote by Jón which uses the figure of speech \"to dress the cat\". [...] "
            "archaeologist Guðmundur Ólafsson connects the Yule cat to various entities that, in other European traditions, accompanied Saint Nicholas. [...] "
            "The Yule cat was traditionally used as a threat and incentive for farm workers to finish processing the wool collected in the autumn before Christmas. "
            "Those who took part in the work were rewarded with new clothes, but those who did not would get nothing and thus would be prey for the Yule cat. [...] "
            "The establishment of the Yule cat as part of classic Icelandic Christmas folklore came in 1932, when Jóhannes úr Kötlum published his poetry collection Jólin koma [...] "
            "By the middle of the 20th century, Jólakötturinn was considered the pet of Grýla and her sons. [...] "
            "In 2018, the city of Reykjavík set up a 5 m (16 ft) tall iron sculpture of the Yule cat as a Christmas decoration in the city's central square.",
            nome="Yule Cat")],
    },
    # 5 caixões de segurança contra o enterro em vida
    {
        "temas_secundarios": ["historia_medicina", "invencoes"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "O medo de ser enterrado vivo gerou, nos séculos XVIII e XIX, caixões com sino, tubo de ar e janela. Um médico se fez enterrar e almoçou sopa, cerveja e salsichas lá embaixo. Não há caso registrado de alguém salvo.",
        "explicacao": (
            "O pavor de ser enterrado vivo chegou ao auge nas epidemias de cólera do século XIX, quando o medo do "
            "contágio levava a enterros apressados, sem distinguir bem os mortos dos moribundos. Jornais, médicos e "
            "a literatura alimentavam o medo, e dezenas de modelos de \"caixão de segurança\" foram patenteados. O "
            "primeiro registrado foi encomendado pelo duque Fernando de Brunswick, que morreu em 1792: tinha "
            "janela, tubo de ar e, em vez de tampa pregada, uma fechadura, com as chaves do caixão e do túmulo "
            "num bolso da mortalha. Em 1798, um padre alemão teria sugerido ligar cada caixão aos sinos da igreja "
            "por uma corda, e a ideia inspirou modelos com sino. Em 1822, o médico Adolf Gutsmuth, que se deixou "
            "enterrar várias vezes para demonstrar seu projeto, passou horas debaixo da terra e comeu uma refeição "
            "entregue por um tubo. Os sistemas de cordas presas ao corpo tinham um defeito: na decomposição, o "
            "cadáver incha e se mexe, e o sino tocava em alarmes falsos. Na demonstração de outro modelo, o sistema "
            "de sinalização falhou com um assistente enterrado dentro, que só escapou porque o tubo de ar "
            "funcionou. Apesar de todo o medo, não há nenhum caso documentado de pessoa salva por um caixão desses."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Safety_coffin",
            "A safety coffin or security coffin is a coffin fitted with a mechanism to prevent premature burial or allow the occupant to signal that they have been buried alive. "
            "A large number of designs for safety coffins were patented during the 18th and 19th centuries [...] "
            "The fear of being buried alive peaked during the cholera epidemics of the 19th century, when fear of contagion led to quick burials without making a difference between the dead and the dying, [...] "
            "This fear, known as taphophobia, was heightened by reports of doctors and accounts in literature and the newspapers. [...] "
            "Most consisted of some type of device for communication to the outside world such as a cord attached to a bell that the interred person could ring should they revive after the burial. [...] "
            "The first recorded safety coffin was constructed on the orders of Duke Ferdinand of Brunswick before his death in 1792. "
            "He had a window installed to allow light in, an air tube to provide a supply of fresh air, and instead of having the lid nailed down he had a lock fitted. "
            "In a special pocket of his shroud he had two keys, one for the coffin lid and a second for the tomb door. "
            "P.G. Pessler, a German priest, allegedly suggested in 1798 that all coffins have a tube inserted from which a cord would run to the church bells. [...] "
            "This idea, while highly impractical, led to the first designs of safety coffins equipped with signalling systems. [...] "
            "Dr. Adolf Gutsmuth was buried alive several times to demonstrate a safety coffin of his own design, which was connected to the surface by a pipe. [...] "
            "In 1822 he stayed underground for several hours and even ate a meal of soup, beer and sausages, delivered to him through the pipe. [...] "
            "The systems using cords tied to the body suffered from the drawback that the natural processes of decay often caused the body to swell or shift position, causing accidental tension on the cords and a \"false positive\". [...] "
            "a demonstration in which one of Karnice-Karnicki's assistants had been buried alive ended badly when the signalling systems failed. "
            "Luckily, the breathing tube had activated and the assistant was disinterred unharmed, [...] "
            "Despite the fear of burial while still alive, there are no documented cases of anybody being saved by a safety coffin.",
            nome="Safety coffin")],
    },
    # 6 o salto de Pentecostes e o bungee jump
    {
        "temas_secundarios": ["esportes_tradicionais", "historia_esportes"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "O bungee jump moderno foi inspirado num ritual de Vanuatu: homens saltam de torres de 20 a 30 metros com cipós nos tornozelos. Os primeiros saltos modernos, em 1979, foram ideia de estudantes que discutiam esse ritual.",
        "explicacao": (
            "Na ilha de Pentecostes, em Vanuatu, o salto chamado gol (nanggol, em bislamá) está ligado à colheita "
            "anual do inhame e é feito entre abril e junho: um bom salto ajudaria a garantir uma boa safra. A "
            "época não é escolhida à toa. A torre é erguida na estação seca, quando os cipós estão mais elásticos. "
            "Um ancião escolhe os cipós de cada saltador de acordo com o peso dele, sem cálculo nenhum: se forem "
            "longos demais, o saltador bate com força no chão; curtos demais, ele se choca contra a torre. As "
            "plataformas são feitas para se quebrar no salto, absorvendo parte do impacto, e o ideal é chegar a "
            "roçar os ombros no chão. Em 1974, para a visita da rainha Elizabeth II, a administração colonial "
            "convenceu uma aldeia a saltar fora de época, na estação chuvosa; os cipós não tinham elasticidade, e "
            "um saltador morreu. Em 1º de abril de 1979, membros do Clube de Esportes Perigosos da Universidade de "
            "Oxford saltaram de uma ponte em Bristol presos por cordas, depois de conversar sobre o "
            "\"salto do cipó\" de Vanuatu, e foram presos logo em seguida. O empresário A. J. Hackett, que "
            "popularizou o bungee, também citou o ritual como inspiração, e os ilhéus passaram a pedir compensação "
            "pelo que consideram apropriação da sua cultura."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Land_diving",
                "Land diving (Sa: Gol, Bislama: Nanggol) is a ritual performed by the men of the southern part of Pentecost Island, Vanuatu. "
                "Men jump off wooden towers around 20 to 30 meters (66 to 98 ft) high, with two tree vines wrapped around the ankles. [...] "
                "The land diving ritual is associated with the annual yam harvest. "
                "It is performed annually in the months of April, May, or June. "
                "A good dive helps ensure a bountiful yam harvest. [...] "
                "The time of yam harvest is significant because tower construction is best done during the dry season. "
                "Also, the lianas have the best elasticity during this time. [...] "
                "During the jump, the platform supports snap, causing the platform to hinge downward and absorb some of the force from falling. "
                "The vines are selected by a village elder and matched with each jumper's weight without any mechanical calculations. [...] "
                "If the vine is too long, the diver can hit the ground hard, but if the vine is too short, then the diver can collide with the tower. [...] "
                "The goal is to brush the shoulders against the ground. [...] "
                "In 1974, Queen Elizabeth II of Great Britain visited Vanuatu and observed the spectacle. "
                "The British colonial administration wanted the Queen to have an interesting tour, and convinced the Anglican villagers of the Melanesian Mission at Point Cross to perform a jump. "
                "However, the vines were not elastic enough because it was the wrong season, the middle of the wet season. "
                "One diver had both lianas broken, broke his back from falling, and later died in a hospital.",
                nome="Land diving"),
            wiki("Bungee_jumping",
                "The land-diving ritual on Pentecost has been claimed as an inspiration by A. J. Hackett, prompting calls from the islanders' representatives for compensation for what they view as the unauthorised appropriation of their cultural property. [...] "
                "The first modern bungee jumps were made on 1 April 1979 from the 76-metre (250 ft) Clifton Suspension Bridge in Bristol, England, by David Kirke and Simon Keeling, members of the Oxford University Dangerous Sports Club, and Geoff Tabin, a professional climber who tied the ropes for the jump. "
                "The students had come up with the idea after discussing the \"vine jumping\" ritual of Vanuatu. "
                "The jumpers were arrested shortly after,",
                nome="Bungee jumping"),
        ],
    },
    # 7 o "enterro celeste" tibetano
    {
        "temas_secundarios": ["religioes", "paisagens_extremas"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "No Tibete, muitos mortos são entregues aos abutres num rito que os tibetanos chamam de \"dar esmola aos pássaros\". Há também razões práticas: o chão é duro demais para covas e falta lenha para cremar.",
        "explicacao": (
            "O nome \"enterro celeste\" é ocidental. Para os tibetanos, o rito é \"dar esmola aos pássaros\" ou "
            "\"levar à montanha\": o corpo é deixado no alto de um morro para ser comido por aves como abutres e "
            "corvos. A maioria dos tibetanos segue o budismo vajrayana, que ensina a transmigração do espírito. Nessa "
            "visão, o corpo vira um recipiente vazio depois da morte e não precisa ser preservado; oferecê-lo como "
            "alimento é um ato de generosidade do morto e da família, porque sustenta outros seres vivos. A geografia "
            "pesa tanto quanto a fé. A maior parte do Tibete fica acima do limite das árvores, e a falta de madeira "
            "torna a cremação cara demais, por isso ela ficava restrita a altos lamas e outros dignitários. Cavar "
            "covas também é difícil: a camada de solo que descongela tem poucos centímetros, com rocha ou "
            "permafrost por baixo. Na Revolução Cultural chinesa, o rito foi proibido como superstição, mas "
            "continuou no campo e hoje tem proteção oficial. Mesmo assim, está em declínio, entre outros motivos "
            "porque há cada vez menos abutres."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Sky_burial",
            "Sky burial (Tibetan: བྱ་གཏོར་, Wylie: bya gtor, lit. \"bird-scattered\") is a funeral practice in which a corpse is placed on a mountaintop to decompose while exposed to the elements, or to be eaten by scavenging animals, especially crows, vultures, bears and jackals. [...] "
            "the practice was completely banned during the Cultural Revolution as a superstitious practice; [...] "
            "The majority of Tibetan people and many Mongols adhere to Vajrayana Buddhism, which teaches the transmigration of spirits. "
            "In this tradition there is no need to preserve the body, as it becomes an empty vessel upon death. [...] "
            "In much of Tibet and Qinghai, the ground is too hard and rocky to dig a grave, and due to the scarcity of fuel and timber, sky burials were typically more practical than the traditional Buddhist practice of cremation, which has been limited to high lamas and some other dignitaries. [...] "
            "\"Sky burial\" is a Western term; it is not used by Tibetans, who call it \"giving alms to the birds\" or \"to carry to the mountain.\" [...] "
            "Most of Tibet is above the tree line, and the scarcity of timber makes cremation economically unfeasible. "
            "Additionally, subsurface interment is difficult since the active layer is not more than a few centimeters deep, with solid rock or permafrost underlying the surface. [...] "
            "Sky burial nonetheless continued to be practiced in rural areas and has even received official protection in recent years. "
            "However, the practice continues to diminish for a number of reasons, including restrictions on its practice near urban areas and diminishing numbers of vultures in rural districts. [...] "
            "Jhator is considered an act of generosity on the part of the deceased, since the deceased and their surviving relatives are providing food to sustain living beings.",
            nome="Sky burial")],
    },
    # 8 famadihana, a "virada dos ossos" em Madagascar
    {
        "temas_secundarios": ["doencas_infecciosas", "africa_antiga"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Em Madagascar, famílias tiram os mortos do jazigo, trocam suas mortalhas e dançam com eles ao som de música. O ritual é apontado como um dos fatores de propagação da peste, e foi proibido para quem morreu dela.",
        "explicacao": (
            "O famadihana, a \"virada dos ossos\", é uma tradição funerária dos povos malgaxes. Os parentes tiram "
            "os corpos dos antepassados do jazigo da família, enrolam-nos em panos novos e reescrevem o nome de cada "
            "um no tecido, para que nunca seja esquecido. Depois dançam com os corpos sobre a cabeça, ao som de "
            "música ao vivo, dão a volta no túmulo e os devolvem ao lugar. O costume se baseia na crença de que o "
            "espírito só se junta ao mundo dos ancestrais depois da decomposição completa do corpo e das "
            "cerimônias certas, o que pode levar anos. Em geral, o rito se repete a cada cinco a sete anos e reúne a "
            "família inteira, às vezes até parentes brigados. Na forma atual, parece ser recente, talvez do século "
            "XVII. O contato direto com os corpos tem um lado perigoso: a prática é associada à transmissão da peste "
            "pneumônica no país, e o governo proibiu fazê-la com quem morreu da doença, embora haja relatos de que a "
            "regra é desrespeitada. O costume está em declínio, em parte pelo preço das mortalhas de seda. A Igreja "
            "Católica não se opõe mais a ele, por considerá-lo cultural, e não religioso."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Famadihana",
                "Famadihana is a funerary tradition of the Malagasy peoples of Madagascar. "
                "During this ceremony, known as the turning of the bones, people bring forth the bodies of their ancestors from the family crypts, rewrap the corpses in fresh cloth, and rewrite their names on the cloth so they will always be remembered. "
                "Then they dance to live music while carrying the corpses over their heads and go around the tomb before returning the corpses to the family tomb. [...] "
                "Famadihana appears to be a custom of somewhat recent origin, perhaps only since the 17th century in its present form, [...] "
                "The custom is based upon a belief that the spirits of the dead finally join the world of the ancestors after the body's complete decomposition and appropriate ceremonies, which may take many years. "
                "In Madagascar, this became a regular ritual usually once every five to seven years, and the custom brings together extended families in celebrations of kinship, sometimes even those with troubled relations. "
                "The practice of Famadihana is on the decline due to the expense of silk shrouds and belief by some Malagasy that the practice is outdated. [...] "
                "The Catholic Church, however, no longer objects to the practice, because it regards Famadihana as purely cultural rather than religious. [...] "
                "Additionally, the practice of Famadihana is thought to be connected to pneumonic plague transmission in the region. "
                "The Malagasy government has issued rulings forbidding the practice for individuals who died of plague, but there have been reports of people ignoring this decree.",
                nome="Famadihana"),
            wiki("2017_Madagascar_plague_outbreak",
                "In addition to agricultural factors that increase prevalence of plague, burial practices in Madagascar also spread disease. [...] "
                "This process could take up to several years and involves direct contact with corpses. "
                "This burial practice perpetuates the spread of plague among other diseases.",
                nome="2017 Madagascar plague outbreak"),
        ],
    },
    # 9 o ritual da tucandeira dos Sateré-Mawé
    {
        "temas_secundarios": ["povos_indigenas", "insetos"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "No rito de passagem dos Sateré-Mawé, no Brasil, o jovem calça luvas de palha com dezenas de formigas tucandeiras, de picada dolorosíssima. Segundo descrições, para completar a iniciação, isso se repete 20 vezes.",
        "explicacao": (
            "Os Sateré-Mawé chamam o ritual de Wyamat e se referem a ele como \"meter a mão na luva\"; na região, é "
            "conhecido como Festa da Tocandira. É um rito de passagem em que os adolescentes se tornam homens, e "
            "tradicionalmente o evento que reúne os clãs desse povo. Os cantadores entoam, durante todo o ritual, "
            "cantos épicos que narram o mito de origem, o surgimento dos clãs e as guerras, inclusive a "
            "participação dos Sateré-Mawé na Cabanagem. As luvas são tecidas em palha, pintadas com jenipapo e "
            "enfeitadas com penas de arara e gavião. Segundo descrições do rito, as formigas são antes adormecidas "
            "num sedativo natural e presas na trama com os ferrões para dentro; cerca de 80 vão em cada luva. "
            "Quando acordam, são agitadas com fumaça, e o jovem fica com as mãos nas luvas por 5 a 10 minutos ou "
            "mais. A dor da formiga Paraponera clavata, a \"formiga-bala\", é descrita como ondas de ardor que "
            "duram até 24 horas. Depois, a mão e parte do braço ficam temporariamente paralisadas, e o iniciado pode "
            "tremer por dias. Para completar a iniciação, a prova é repetida 20 vezes, ao longo de meses ou anos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://pib.socioambiental.org/pt/Povo:Sateré_Mawé",
             "titulo": "Sateré Mawé - Povos Indígenas no Brasil (Instituto Socioambiental)", "idioma": "pt",
             "trecho": (
                "nos cantos do Waymat (ritual da tucandeira). "
                "Este ritual de passagem da puberdade para a vida adulta é o evento que tradicionalmente reúne os clãs. [...] "
                "O Wyamat, que os Sateré-Mawé referem-se como “meter a mão na luva”, é conhecido regionalmente como “Festa da Tocandira”, coincidindo com a época do fabrico. "
                "Trata-se de um rito de passagem - onde os adolescentes tornam-se homens - de extraordinária importância para os Sateré-Mawé, possuindo uma coleção de cantos épicos que os paini (os cantadores) cantam durante todo o ritual , narrando o mito de origem, o mito do aparecimento dos clãs, as histórias das guerras que incluem a participação dos Sateré-Mawé na Guerra da Cabanagem. "
                "As luvas utilizadas durante este ritual são tecidas em palha pintada com jenipapo, e adornadas com penas de arara e gavião; nelas, o iniciado enfia a mão para ser ferroado por dezenas de formigas tocandiras (Paraponera clavata).")},
            wiki("Paraponera_clavata",
                "It is described as causing \"waves of burning, throbbing, all-consuming pain that continues unabated for up to 24 hours\". [...] "
                "The Sateré-Mawé people of Brazil use intentional bullet ant stings as part of their initiation rites to become warriors or leaders. "
                "The ants are first rendered unconscious by submersion in a natural sedative, and then 80 of them are woven into gloves (which resemble large oven mitts) made of vines or leaves, stingers facing inward. "
                "When the ants regain consciousness, an initiator repeatedly blows smoke at the ants, with the objective of making them agitated and aggressive. "
                "Once this is done, the initiate has the gloves put on his hands and keeps them on for 5 to 10 minutes or longer. "
                "Afterward, the boy's hand and part of his arm are temporarily paralyzed because of the ant venom, and he may shake uncontrollably for days. [...] "
                "To fully complete the initiation, a boy or man must go through the ordeal 20 times over the course of several months or even years.",
                nome="Paraponera clavata"),
        ],
    },
    # 10 gorjeta já foi proibida nos EUA
    {
        "temas_secundarios": ["economia_curiosa", "leis_julgamentos"],
        "tipos_espanto": ["contraintuitivo", "origem_inesperada"],
        "gancho": "Nos EUA, seis estados já proibiram por lei dar gorjeta. Até o início do século XX, muitos americanos viam o costume como coisa de aristocrata, incompatível com uma sociedade igualitária.",
        "explicacao": (
            "A gorjeta começou na Inglaterra dos Tudor. Na Idade Média, era um costume entre senhor e servo: o "
            "criado recebia um dinheiro extra por um serviço muito bem feito. No século XVII, esperava-se que quem "
            "passava a noite numa casa particular deixasse uma quantia para os empregados do anfitrião, e logo os "
            "fregueses dos cafés de Londres também passaram a dar gorjeta. O hábito foi levado aos Estados Unidos "
            "nas décadas de 1850 e 1860 por americanos que queriam parecer aristocratas. Só que, para muita gente "
            "ali, isso contrariava os valores de uma sociedade democrática, porque a gorjeta marcava a posição "
            "social de quem dava em relação a um \"inferior\". Os patrões, por sua vez, a viam como uma espécie de "
            "suborno ao empregado, por exemplo para conseguir uma porção extragrande. Seis estados aprovaram leis "
            "contra a gorjeta, a primeira em Washington, em 1909, mas elas eram difíceis de aplicar, e a última foi "
            "revogada no Mississippi, em 1926. A Lei Seca, de 1919, mudou o jogo: sem a receita das bebidas, hotéis "
            "e restaurantes passaram a aceitar a gorjeta como complemento do salário. E, ao contrário do que se "
            "pensa, ela não surgiu porque garçons ganhavam mal: na época, era uma profissão razoavelmente bem paga."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Gratuity",
            "The practice of tipping began in Tudor England. "
            "In medieval times, tipping was a master-serf custom wherein a servant would receive extra money for having performed superbly well. "
            "By the 17th century, it was expected that overnight guests to private homes would provide sums of money, known as vails, to the host's servants. "
            "Soon afterwards, customers began tipping in London coffeehouses and other commercial establishments\". "
            "The practice was imported from Europe to America in the 1850s and 1860s by Americans who wanted to seem aristocratic. "
            "However, until the early 20th century, Americans viewed tipping as inconsistent with the values of an egalitarian, democratic society, as the origins of tipping were premised upon noblesse oblige, which promoted tipping as a means to establish social status to inferiors. "
            "Six American states passed laws that made tipping illegal. "
            "Enforcement of anti-tipping laws was problematic. "
            "The earliest of these laws was passed in 1909 (Washington), and the last of these laws was repealed in 1926 (Mississippi). [...] "
            "Also, proprietors regarded tips as equivalent to bribing an employee to do something that was otherwise forbidden, such as tipping a waiter to get an extra large portion of food. "
            "However, the introduction of Prohibition in the US in 1919 had an enormous impact on hotels and restaurants, who lost the revenue of selling alcoholic beverages. "
            "The resulting financial pressure caused proprietors to welcome tips as a way of supplementing employee wages. "
            "Contrary to popular belief, tipping did not arise because of servers' low wages, because the occupation of waiter (server) was fairly well paid in the era when tipping became institutionalized.",
            nome="Gratuity")],
    },
    # 11 o luto branco das rainhas
    {
        "temas_secundarios": ["moda", "europa_medieval"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Entre as rainhas da Europa medieval, a cor do luto mais profundo era o branco. O \"luto branco\" das rainhas da França inspirou até o guarda-roupa todo branco de uma rainha britânica numa viagem a Paris em 1938.",
        "explicacao": (
            "O preto não é o luto universal. Na cultura chinesa, a cor tradicional do luto é o branco, e na "
            "Tailândia, onde hoje se usa preto nos funerais, historicamente também era. Na Europa, as rainhas "
            "medievais usavam branco no luto mais fundo. Em 1393, os parisienses viram o espetáculo raro de um "
            "funeral real todo em branco, o de Leão V, rei da Armênia, que morreu no exílio. Na Espanha, a "
            "tradição real durou até o fim do século XV. O costume das rainhas francesas, o \"deuil blanc\", teve um "
            "eco no século XX: em 1938, a rainha Elizabeth, mulher do rei Jorge VI e futura Rainha-Mãe, estava de "
            "luto pela mãe quando precisou acompanhar o marido numa visita de Estado à França. O estilista Norman "
            "Hartnell resolveu o impasse com um guarda-roupa inteiro branco. Outras cortes também retomaram a cor: "
            "a rainha Guilhermina, da Holanda, reintroduziu o luto branco em 1934, ao perder o marido, e a "
            "tradição ficou na família real holandesa. Em 2004, as quatro filhas da rainha Juliana foram de branco "
            "ao funeral da mãe."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Mourning",
            "White is the traditional color of mourning in Chinese culture, with white clothes and hats formerly having been associated with death. [...] "
            "In Thailand, people wear black when attending a funeral. "
            "Black is considered the mourning color, although historically it was white. [...] "
            "The color of deepest mourning among medieval European queens was white. "
            "In 1393, Parisians were treated to the unusual spectacle of a royal funeral carried out in white, for Leo V, King of Armenia, who died in exile. "
            "This royal tradition survived in Spain until the end of the 15th century. "
            "In 1934, Queen Wilhelmina of the Netherlands reintroduced white mourning after the death of her husband Prince Henry. "
            "It has since remained a tradition in the Dutch royal family. "
            "In 2004, the four daughters of Queen Juliana of the Netherlands all wore white to their mother's funeral. [...] "
            "The custom for the queens of France to wear deuil blanc (\"white mourning\") was the origin of the white wardrobe created in 1938 by Norman Hartnell for Queen Elizabeth (later known as the Queen Mother). "
            "She was required to join her husband King George VI on a state visit to France even while mourning her mother.",
            nome="Mourning")],
    },
    # 12 ohaguro, os dentes pretos do Japão
    {
        "temas_secundarios": ["quimica_cotidiano", "asia_antiga"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Por séculos, no Japão, dentes pintados de preto eram sinal de beleza e maturidade. Num conto do século XII, uma dama que não os tingia tinha os dentes comparados a \"lagartas sem pele\".",
        "explicacao": (
            "O costume se chama ohaguro, \"dentes pretos\", e foi popular do século X ao fim do XIX. Começou na "
            "aristocracia do período Heian como rito de maturidade de meninas adolescentes e se espalhou para "
            "nobres, samurais, que tingiam os dentes pela primeira vez na cerimônia de iniciação, aos quinze ou "
            "dezesseis anos, e depois para mulheres de todas as classes, sobretudo as casadas. A tinta era um bom exemplo de "
            "química caseira: limalha de ferro dissolvida em vinagre, misturada a taninos vegetais, como pó de "
            "galhas de sumagre ou chá. A reação deixava a mistura preta e insolúvel em água, pelo mesmo processo "
            "da tinta ferrogálica de escrever. Além da estética, a prática era tida como boa para a saúde: a "
            "camada funcionaria como selante contra cáries. A cor desbotava rápido e precisava ser reaplicada todo "
            "dia ou a cada poucos dias. A abertura do Japão aos costumes ocidentais na era Meiji acabou com a moda: "
            "em 1870, o governo proibiu o ohaguro para homens, e em 1873 a imperatriz Shōken passou a aparecer em "
            "público com os dentes brancos, o que acelerou o abandono entre as mulheres casadas e nobres."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Ohaguro",
            "is the name given in Japan to the custom of blackening one's teeth with a solution of iron filings and vinegar. "
            "It was especially popular between the Heian and Edo periods, from the 10th century until the late 19th century, but the opening of the country to Western customs during the Meiji period led to its gradual disappearance. "
            "It was a tradition practiced mainly by married women and some men, almost always members of the aristocracy and samurai. "
            "In addition to Japanese society's preference for black teeth, it was also considered beneficial to health, as it prevented tooth decay by acting as a dental sealant. [...] "
            "The word ohaguro is composed of the honorific prefix o- (お), the term ha (歯, 'tooth'), and the term kuro (黒, 'black'). [...] "
            "and in the story Mushi Mezuru Himegimi, in English The Lady Who Loved Insects, from the 12th century, [...] "
            "a maiden describes her completely unplucked eyebrows as \"hairy caterpillars\" and her undyed teeth as \"skinless caterpillars\", [...] "
            "The tradition first appeared among men and women of the Heian period aristocracy between the 9th and 11th centuries, which was soon followed by women of all social classes. "
            "It began as a rite of maturity among adolescent girls that by the end of this period had spread to noblemen. [...] "
            "it was customary to dye their teeth for the first time upon passing their genpuku or initiation ceremony, at the age of fifteen or sixteen. [...] "
            "In 1870 the government banned the practice of ohaguro on men, and the tradition gradually became obsolete, especially from 1873 among married and noblewomen, when the Empress Shōken decided to appear in public with white teeth. [...] "
            "The main ingredient was a dark brown solution of iron acetate called kanemizu (鉄奨水, lit. 'iron juice water'), created by dissolving iron filings in vinegar. "
            "When the solution was combined with vegetable tannins from sources such as powdered galls of the Chinese sumac plant (fushi) or tea, it turned black and ceased to be soluble in water, the same method by which iron gall ink is produced. [...] "
            "The dye faded quickly and had to be applied once a day or every few days to keep the dark shade even.",
            nome="Ohaguro")],
    },
    # 13 a Tomatina e o enterro do tomate
    {
        "temas_secundarios": ["cultura_popular", "historia_pratos"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "A Tomatina, a maior guerra de comida do mundo, nasceu de uma briga num desfile de 1945, na Espanha. Proibida nos anos 1950, voltou de vez em 1957, depois que moradores fizeram o \"enterro\" de um tomate num caixão.",
        "explicacao": (
            "Tudo começou na última quarta-feira de agosto de 1945, na cidade espanhola de Buñol. Jovens assistiam "
            "ao desfile de gigantes e cabeçudos quando a cabeça de um dos participantes caiu. Furioso, ele saiu "
            "batendo em tudo, uma banca de verduras virou alvo e a multidão começou a atirar tomates, até a polícia "
            "local acabar com a briga. No ano seguinte, alguns jovens combinaram a confusão e trouxeram tomates de "
            "casa. A polícia de novo interveio, mas a tradição estava criada, e milhares de pessoas seguiram o "
            "exemplo. No início dos anos 1950, sob o regime de Franco, a festa foi proibida por não ter significado "
            "religioso, e participantes chegaram a ser presos. Houve idas e vindas até 1957, quando os moradores "
            "protestaram com um enterro: carregaram um caixão com um tomate grande dentro, ao som de uma banda "
            "tocando marchas fúnebres. Deu certo, e a Tomatina virou festa oficial. Desde 2013, a entrada é paga e "
            "limitada a 20 mil pessoas, para não sobrecarregar uma cidade de cerca de 9 mil habitantes. Em 2015, "
            "estima-se que foram atirados quase 145 mil quilos de tomate. Depois, a lavagem com mangueiras tem um "
            "efeito curioso: o ácido cítrico dos tomates ajuda a limpar, e certas superfícies ficam mais limpas do "
            "que antes."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("La_Tomatina",
            "La Tomatina (Spanish pronunciation: [la tomaˈtina]) is a Spanish festival in Buñol, Spain where participants throw tomatoes at each other. "
            "It is the biggest food fight in the world. [...] "
            "in 2013 the festival became a ticketed event for no more than 20,000, so as not to overwhelm Buñol's population of about 9,000 people. [...] "
            "La Tomatina Festival started the last Wednesday of August in 1945 when some young people spent time in then square to attend the Giants and Big-Heads figures parade. "
            "One participant's Big-head fell off, as a result of the festivities. "
            "The participant flew into a fit of rage, and began hitting everything in their path. "
            "There was a market stall of vegetables that fell victim to the fury of the crowd, as people started to pelt each other with tomatoes until the local forces ended the fruit fight. "
            "The following year, some young people engaged in a pre-planned quarrel and brought their own tomatoes from home. "
            "Although the local forces broke it up, this began the yearly tradition. "
            "In the following years, the boys' example was followed by thousands of people. "
            "La Tomatina was banned in the early 1950s by Francisco Franco due to the festival's lack of religious significance, however, this did not stop the participants, who were later then arrested. [...] "
            "The festivity was again canceled until 1957 when, as a sign of defiance, a tomato funeral was held: a demonstration in which the residents carried a coffin with a large tomato inside. "
            "The parade was accompanied by a music band that played funeral marches. "
            "The protest was successful, and La Tomatina Festival was finally permitted and became an official festival. [...] "
            "Citric acid in the tomatoes aids in the cleaning process, resulting in some of the town's surfaces being cleaner after being rinsed off than they were before the event. "
            "Since 2013, participation in the event has been restricted to the 20,000 holders of paid tickets. "
            "In 2015, it was estimated that almost 145,000 kg (320,000 lb) of tomatoes were thrown.",
            nome="La Tomatina")],
    },
]
