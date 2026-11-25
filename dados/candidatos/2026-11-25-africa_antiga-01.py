LOTE = "2026-11-25-africa_antiga-01"
AREA = "historia_antiga"
TEMA = "africa_antiga"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 as pirâmides núbias: mais que o dobro das egípcias, e a tumba fica embaixo
    {
        "temas_secundarios": ["egito_antigo", "arquitetura"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "O Sudão tem mais pirâmides que o Egito: os reis de Cuxe ergueram cerca de 255, mais que o dobro das egípcias. São estreitas, muito inclinadas e não guardam o morto dentro: a tumba fica embaixo.",
        "explicacao": (
            "No reino de Cuxe, no atual norte do Sudão, reis, rainhas e gente rica foram enterrados sob pirâmides "
            "por quase mil anos, de cerca de 700 a.C. a 350 d.C. As mais antigas, em El-Kurru, são de 751 a.C., e "
            "a última pirâmide da África foi erguida em Meroé por volta de 350 d.C. A ideia veio do Egito, mas o "
            "desenho mudou. As pirâmides núbias têm de 6 a 30 metros de altura, sobem de bases pequenas e se "
            "inclinam a uns 70 graus; as egípcias de altura parecida costumavam ter bases ao menos cinco vezes "
            "maiores e ângulos de 40 a 50 graus. A maior diferença está no subsolo: em vez de abrigar a tumba, a "
            "pirâmide núbia fica em cima da câmara funerária. Isso confundiu os arqueólogos por muito tempo, até "
            "George Reisner descobrir que as entradas eram aterradas e escondidas depois do funeral. A pirâmide "
            "funcionava, assim, como uma lápide monumental. Há até um vestígio da obra dentro delas: o mastro "
            "central do shadoof, um guindaste de contrapeso usado na construção, era deixado enterrado no meio da "
            "pirâmide e coberto pela pedra do topo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Nubian_pyramids",
            "The Nubian pyramids were constructed by the rulers of the ancient Kushite kingdoms in the region of the Nile Valley known as Nubia, located in present-day northern Sudan. [...] "
            "the pyramids were integral to burial customs for royalty and other wealthy figures of the Kushite kingdom [...] "
            "These customs endured for almost a thousand years from 700 BC to 350 AD. [...] "
            "The earliest pyramids in El Kurru were constructed in 751 BC [...] "
            "The last Nubian pyramid (and the last African pyramid) was built at Meroe around 350 AD. [...] "
            "One of the tools used was shadoof counterbalanced lever hoist, of which the central pivot poles were left buried in the center of the pyramid and covered by their respective cap stones. [...] "
            "Approximately 255 pyramids are known to have been constructed by the Nubians, more than double the number constructed in Ancient Egypt. [...] "
            "range approximately 6–30 metres (20–98 ft) in height, but rise from fairly small foundation footprints, resulting in tall, narrow structures inclined at approximately 70°. [...] "
            "Egyptian pyramids of similar height generally had foundation footprints at least five times larger and were inclined at angles between 40–50°. "
            "The most striking difference, however, is that while Egyptian pyramids house tombs of rulers within, Nubian pyramids are built on top of the burial chambers. "
            "This was a longtime source of confusion to archaeologists until George Reisner discovered that the entryways were filled in and concealed following the ruler's funeral. "
            "In this way, the pyramids served as elaborate tombstones",
            nome="Nubian pyramids")],
    },
    # 2 a cabeça de Augusto enterrada sob a escada de um templo em Meroé
    {
        "temas_secundarios": ["roma_antiga", "egito_antigo"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Em 24 a.C., tropas de uma rainha de Cuxe saquearam estátuas de Augusto no Egito romano. Uma cabeça de bronze do imperador foi enterrada sob a escada de um templo em Meroé, talvez para ser pisada por quem entrasse.",
        "explicacao": (
            "A cabeça, maior que o tamanho natural, foi desenterrada em dezembro de 1910 pelo arqueólogo britânico "
            "John Garstang em Meroé, no atual Sudão, que tinha sido por séculos a capital do reino de Cuxe. Estava "
            "num bolsão de areia limpa, sob o que fora a escadaria de um templo, e o clima quente e seco a "
            "conservou por mais de 1.900 anos. O geógrafo grego Estrabão conta que os cuxitas atacaram o sul do "
            "Egito, então romano, enquanto o prefeito Élio Galo estava numa expedição à Arábia, e destruíram "
            "estátuas de Augusto. Quem comandava Cuxe era a rainha Amanirenas, que tinha o título de candace. A "
            "guerra durou de 25 a 22 a.C.: os romanos revidaram e arrasaram Napata, mas, no fim, Augusto atendeu "
            "aos embaixadores da rainha e não cobrou mais tributos. A cabeça estava sob uma escadaria monumental "
            "que levava a um altar da vitória. A hipótese mais citada é que pô-la ali servia para rebaixar o "
            "imperador aos olhos da aristocracia de Meroé: quem entrava no templo pisava em Augusto. A peça foi "
            "doada ao Museu Britânico em 1911, onde está até hoje."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Meroë_Head",
                "The Meroë Head, or Head of Augustus from Meroë, is a larger-than-life-size bronze head depicting the first Roman emperor, Augustus, that was found in the ancient Nubian site of Meroë in modern Sudan in 1910. [...] "
                "It was looted from Roman Egypt in 24 BC by the forces of queen Amanirenas of Kush and brought back to Meroë, where it was buried beneath the staircase of a temple. [...] "
                "The head was excavated by the British archaeologist John Garstang in December 1910 at Meroë, which had been the capital of the Kingdom of Kush for several centuries. "
                "It was found near a mound (M292) under what was once a temple staircase. "
                "The statue had been purposely buried over 1900 years prior and had been well preserved due to the hot, dry conditions. [...] "
                "buried in a clean pocket of sand [...] "
                "The bust was donated to the British Museum by the Sudan Excavation Committee with the support of the National Art Collections Fund in 1911. [...] "
                "The sculpture was buried beneath a monumental stairway that led to an altar of victory. "
                "The placing of the Emperor's head below the shrine's steps was designed to symbolically denigrate the reputation of Augustus in the eyes of the Meroitic aristocracy and Kushite queen Amanirenas. [...] "
                "everyone who enters the temple is welcome to step on Augustus's head buried under the doorstep, symbolising Meroë's triumph over the emperor.",
                nome="Meroë Head"),
            wiki("Amanirenas",
                "Queen Amanirenas is one of the most famous Meroitic queens because of her role in leading the Kushite army against the Romans in a war that lasted three years (25 BC to 22 BC). [...] "
                "According to Strabo's account, the Kushite forces launched an attack on Thebais and Syene while then-prefect Aelius Gallus was away on his ill-fated expedition to Arabia in 25 BC. "
                "They were successful in taking Syene, Elephantine, and Philae. As they took the city, they enslaved inhabitants and destroyed the statues of Caesar Augustus. [...] "
                "Amanirenas, who bore the title of kandake [...] "
                "Her entreaty was ignored and the city was razed. [...] "
                "Augustus imposed no further tributes and fulfilled the ambassadors' wishes.",
                nome="Amanirenas"),
        ],
    },
    # 3 Candace não era nome: era o título das rainhas de Cuxe
    {
        "temas_secundarios": ["palavras_viajantes", "religioes"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "Na Bíblia, um eunuco serve a \"Candace, rainha dos etíopes\". Só que Candace não era nome: kandake era o título das rainhas de Cuxe, no atual Sudão, que gregos e romanos tomaram por nome próprio.",
        "explicacao": (
            "Kandake, ou kentake, era uma palavra da língua meroítica para a rainha ou a rainha-mãe do reino de "
            "Cuxe. Ela aparece em registros de seis ou sete mulheres: algumas governaram, outras provavelmente "
            "eram só esposas do rei. A candace que reinava por conta própria levava também o título de qore, o "
            "mesmo dos reis homens. Os autores gregos e romanos trataram a palavra, por engano, como se fosse um "
            "nome. O geógrafo Estrabão descreveu uma \"Candace caolha\" que guerreou contra Roma, e Plínio escreveu "
            "que a rainha dos \"etíopes\" tinha o título de Candace. No livro dos Atos dos Apóstolos, Filipe, o "
            "Evangelista, encontra na estrada um eunuco, alto funcionário de \"Candace, rainha dos etíopes\", que "
            "cuidava de todo o tesouro dela, e o batiza. É desse uso no Novo Testamento que deriva o nome Candace. "
            "Quatro rainhas ficaram conhecidas no mundo greco-romano como \"as Candaces\": Amanishakheto, "
            "Amanirenas, Nawidemak e Malegereabar. A tradição etíope também fala de rainhas com esse título, mas "
            "não há prova arqueológica nem inscrição de que ele tenha sido usado na Etiópia."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Kandake",
            "was one Meroitic term for a queen or queen mother of Kingdom of Kush. It is attested for six or seven women. "
            "Some were rulers, while others were most likely just wives of a king. [...] "
            "A kandake who ruled in her own right bore in addition the title qore, the same title carried by male rulers. "
            "Contemporary Greek and Roman sources treated it, incorrectly, as a name. "
            "The name Candace is derived from the way the word is used in the New Testament (Acts 8:27). [...] "
            "the \"one-eyed Candace\" [...] "
            "Pliny writes that the \"Queen of the \"Aethiopians\" bore the title Candace [...] "
            "Four African queens were known to the Greco-Roman world as the \"Candaces\": Amanishakheto, Amanirenas, Nawidemak, and Malegereabar. [...] "
            "a treasury official of \"Candace, queen of the Aethiopians\", returning from a trip to Jerusalem, met with Philip the Evangelist [...] "
            "an Aethiopian eunuch, a court official of Candace, queen of the Aethiopians, who was in charge of all her treasure. [...] "
            "he was promptly baptised in some nearby water. [...] "
            "There is no archaeological or epigraphic evidence that title “Kandake” was used historically within Ethiopia.",
            nome="Kandake")],
    },
    # 4 Axum, uma das quatro grandes potências do mundo segundo Mani
    {
        "temas_secundarios": ["dinheiro", "comercio_rotas", "religioes"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "No século III, o profeta Mani apontou as quatro grandes potências do mundo: Roma, Pérsia, China e Axum, reino africano na atual Etiópia e Eritreia. Axum cunhava moedas de ouro, achadas até no sul da Índia.",
        "explicacao": (
            "Mani, fundador do maniqueísmo, pôs o reino de Axum ao lado de Roma, da Pérsia e da China. Axum era "
            "uma potência na rota comercial entre Roma e a Índia, e sua moeda ajudava esse comércio pelo mar "
            "Vermelho. A cunhagem começou por volta de 270, no reinado de Endybis, com moedas de ouro, prata e "
            "cobre, e algumas foram escavadas em Cesareia e no sul da Índia. As inscrições costumavam vir em grego, "
            "a língua de boa parte dos parceiros comerciais, com dizeres como \"rei de Axum\". O ouro era muito "
            "puro: nas moedas do rei Aphilas, o teor mais baixo já registrado é de 90%. As moedas também contam a "
            "virada religiosa do reino. O rei Ezana, influenciado na infância pelo tutor Frumêncio, levou o "
            "cristianismo a Axum no século IV, e as moedas da segunda metade do seu reinado trocaram o disco e o "
            "crescente pela cruz, apontada como a primeira cruz cristã a aparecer numa moeda. Algumas dessas "
            "moedas cristãs ainda seguem o peso anterior à reforma de Constantino, de 324, sinal de que a "
            "conversão pode ter vindo antes disso ou poucos anos depois. A cunhagem decaiu no século VII, quando "
            "o comércio com o mundo romano foi cortado pelas conquistas árabes."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Kingdom_of_Aksum",
                "The Kingdom of Aksum was considered one of the four great powers of the 3rd century by Mani, the founder of Manichaeism, alongside Persia, Rome, and China. [...] "
                "During the reign of Endybis (270–310), Aksum began minting coins that have been excavated as far away as Caesarea and southern India. "
                "As the kingdom became a major power on the trade route between Rome and India [...] "
                "an official currency with coinage struck in gold, silver, and copper [...] "
                "Trade with the Roman and Byzantine world came to a halt as the Arabs seized the eastern Roman provinces.",
                nome="Kingdom of Aksum"),
            wiki("Aksumite_currency",
                "Aksumite currency was coinage produced and used within the Kingdom of Aksum (or Axum) centered in present-day Ethiopia and Eritrea and Yemen. "
                "Its mintages were issued and circulated from the reign of King Endybis around AD 270 until it began its decline in the first half of the 7th century [...] "
                "It also facilitated the Red Sea trade on which it thrived. [...] "
                "For example, the lowest purity of gold recorded thus far for Aphilas is 90 percent. [...] "
                "The coins were often inscribed in Greek, as much of its trade was with the \"Graecised Orient.\" [...] "
                "meaning \"King of Aksum\" or King of the Aksumites\" [...] "
                "those of his second half employ revolutionary designs. "
                "With his conversion to Christianity, Ezana began to feature the Cross on his coins, the first time the Christian cross had ever been featured in coinage in the world. "
                "Some of his gold Christian coins are of the weight before Constantine I's weight reform in 324, indicating a conversion before this date or perhaps a few years after [...] "
                "Along with the adoption of the Cross on his coins came, of course, the abandonment of the star and crescent symbol on the coins.",
                nome="Aksumite currency"),
            wiki("Obelisk_of_Axum",
                "King Ezana (c. 321 – c. 360), influenced by his childhood tutor Frumentius, introduced Christianity to Axum",
                nome="Obelisk of Axum"),
        ],
    },
    # 5 o obelisco de Axum: levado por Mussolini, voltou de avião em três pedaços
    {
        "temas_secundarios": ["imperios_coloniais", "grandes_obras"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Levado à Itália em 1937 como butim de guerra, o obelisco de Axum, de 24 metros e 160 toneladas, só voltou à Etiópia em 2005, cortado em três e de avião. O aeroporto local teve a pista reformada para isso.",
        "explicacao": (
            "A estela foi provavelmente talhada e erguida no século IV pelo reino de Axum, e as grandes estelas "
            "como ela marcavam câmaras funerárias subterrâneas da realeza. Quando a ocupação italiana da Etiópia "
            "terminou, em 1937, ela foi cortada em três partes, levada de caminhão até o porto de Massawa, embarcada "
            "para Nápoles e remontada em Roma, diante do Ministério da África Italiana, para comemorar os quinze anos "
            "da Marcha sobre Roma. Num acordo da ONU de 1947, a Itália se comprometeu a devolvê-la, mas pouco se "
            "fez por mais de 50 anos, em parte pelas dificuldades técnicas do transporte. Em 2002, um raio atingiu "
            "o monumento em Roma e causou danos consideráveis. Quando a devolução enfim andou, a pista do "
            "aeroporto de Axum era curta demais para um avião de carga levando um só dos pedaços, as estradas "
            "eram precárias e o porto de Massawa estava fora de cogitação pela tensão entre Eritreia e Etiópia. A "
            "pista foi reformada, e os três pedaços voaram num Antonov An-124 em abril de 2005, carga descrita "
            "como a maior e mais pesada já transportada por via aérea. A operação custou à Itália 7,7 milhões de "
            "dólares, e a estela foi reerguida em Axum em 2008."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Obelisk_of_Axum",
            "The Obelisk of Axum [...] is a 4th-century AD, 24-metre (79 ft) tall phonolite stele, weighing 160 tonnes [...] "
            "The steles were probably carved and erected during the 4th century AD by subjects of the Kingdom of Aksum [...] "
            "Their function is supposed to be as \"markers\" for underground burial chambers. "
            "The largest of the grave markers were for royal burial chambers [...] "
            "The Italian occupation of Ethiopia ended in 1937 with looting, in which the Obelisk of Axum was taken to Italy as war spoil. "
            "The monolith was cut into three pieces and transported by truck along the tortuous route between Axum and the port of Massawa [...] "
            "arriving in Naples on March 27, 1937. It was then transported to Rome, where it was restored, reassembled and erected on Porta Capena square in front of the Ministry for Italian Africa [...] "
            "The obelisk was officially unveiled on October 28, 1937 to commemorate the fifteenth anniversary of the March on Rome. [...] "
            "In a 1947 UN agreement, Italy agreed to return the stele to Ethiopia [...] "
            "little action was taken to return the stele for more than 50 years, partly as a consequence of the considerable technical difficulties related to its transportation. [...] "
            "The runway at Axum Airport was considered too short for a cargo plane carrying even one of the thirds into which the stele had been cut; "
            "the roads and bridges between Addis Ababa and Axum were thought to be not up to the task of road transport; "
            "and access through the nearby Eritrean port of Massawa—which was how the stele originally left Africa—was impossible due to the strained state of relations between Eritrea and Ethiopia. "
            "The runway at Axum airport was then upgraded specifically to facilitate the return of the stele. [...] "
            "until 19 April 2005 when the middle piece was repatriated by use of an Antonov An-124, amidst much local celebration. "
            "It has been described as the largest and heaviest piece of air freight ever carried. "
            "The second piece was returned on 22 April 2005, with the final piece returned on 25 April 2005. "
            "The operation cost Italy $7.7 million. [...] "
            "the monument was re-erected in its original home and unveiled on 4 September 2008. [...] "
            "When the obelisk was hit by lightning during a violent thunderstorm over Rome on 27 May 2002, this caused \"considerable\" damage.",
            nome="Obelisk of Axum")],
    },
    # 6 os Evangelhos de Garima: "escritos num só dia" e talvez os mais antigos ilustrados
    {
        "temas_secundarios": ["religioes", "literatura"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Num mosteiro etíope há evangelhos que, pela tradição, foram escritos num só dia, com Deus segurando o sol. A ciência os datou de séculos antes do que se pensava: talvez o mais antigo livro cristão ilustrado completo.",
        "explicacao": (
            "Os Evangelhos de Garima são manuscritos em ge'ez, a língua do antigo reino de Axum, guardados no "
            "mosteiro de Abba Garima, na Etiópia, com os quatro evangelhos. A tradição dos monges conta que o "
            "santo Abba Garima, que teria chegado à Etiópia em 494, escreveu e ilustrou tudo num único dia, porque "
            "Deus impediu o sol de se pôr até ele terminar. Para os monges, os livros são menos antiguidades do "
            "que relíquias do santo. Estudiosos ocidentais, pela análise da escrita, julgavam que eram de por "
            "volta de 1100 ou mais recentes. A datação por radiocarbono mudou o quadro: amostras do Garima 2, o "
            "mais antigo, indicaram de cerca de 390 a 570, e as do Garima 1, de 530 a 660. Com isso, o Garima 2 é "
            "considerado o mais antigo manuscrito cristão ilustrado e completo que sobreviveu, e os dois são os "
            "manuscritos etíopes mais antigos que se conhecem. O Garima 2 tem 322 páginas e retratos dos "
            "evangelistas. Não se sabe de nenhuma vez em que os livros tenham saído do mosteiro: chegaram a constar "
            "no catálogo de uma exposição que circulou pelos EUA de 1993 a 1996, mas nunca foram emprestados."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Garima_Gospels",
            "The Garima Gospels are three ancient Geʽez manuscripts containing all four canonical Gospel Books [...] "
            "Garima 2, the earliest, is believed to be the earliest surviving complete illuminated Christian manuscript. [...] "
            "samples from Garima 2 proposed a date of c. 390–570, while counterpart dating of samples from Garima 1 proposed a date of c. 530–660. [...] "
            "are the oldest surviving Ethiopian manuscripts of any kind known to modern scholars. "
            "Western scholarship had previously believed both gospels to date from c. 1100 or later on the basis of palaeographic analysis. "
            "The Gospels are housed in Ethiopia's Abba Garima Monastery. They are not known ever to have left the monastery [...] "
            "The Gospels were included in the catalog of an American museum exhibition that toured from 1993 to 1996, African Zion: the Sacred Art of Ethiopia, but were never actually lent to the exhibition. [...] "
            "Monastic tradition ascribes the gospel books to Saint Abba Garima, said to have arrived in Ethiopia in 494. [...] "
            "the monks regard the Gospels less as significant antiquities than as sacred relics of Abba Garima. "
            "According to tradition, Abba Garima wrote and illustrated the complete Gospels in a single day: God stopped the sun from setting until the Saint completed his work. [...] "
            "the Ethiopic language of the Kingdom of Axum from the 4th to the 7th centuries [...] "
            "Garima 2, also in Geʽez, is a 322-page folio written by a different scribe. It has seventeen illuminated pages, including four fine Evangelist portraits",
            nome="Garima Gospels")],
    },
    # 7 Lalibela: igrejas escavadas de cima para baixo para recriar Jerusalém
    {
        "temas_secundarios": ["arquitetura", "religioes"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Na Etiópia, onze igrejas foram escavadas de cima para baixo na rocha, algumas como blocos soltos da montanha. O conjunto quis recriar Jerusalém, e o riacho que o atravessa se chama Jordão.",
        "explicacao": (
            "As igrejas ficam perto da cidade de Lalibela, a cerca de 2.480 metros de altitude, e levam o nome do "
            "rei Gebre Meskel Lalibela, da dinastia Zagwe, que reinou por volta de 1181 a 1221. Segundo a tradição, "
            "antes de subir ao trono ele foi guiado por Cristo numa visita a Jerusalém e recebeu a ordem de "
            "construir uma segunda Jerusalém na Etiópia. A técnica é de subtração: em vez de empilhar pedras, os "
            "construtores abriram, com martelos e cinzéis, trincheiras em volta de blocos de basalto e foram "
            "esvaziando o interior, sempre de cima para baixo. Das onze igrejas, quatro são monolíticas e "
            "isoladas, e sete continuam presas à montanha por uma parede. Cinco ficam ao norte do rio Jordão da "
            "cidade e cinco ao sul, ligadas por túneis e trincheiras; a décima primeira, Biete Giorgis, fica à "
            "parte. A tradição atribui a obra ao rei, mas é mais provável que o conjunto tenha chegado à forma "
            "atual em várias fases, inclusive com a reforma de estruturas que já existiam. O lugar segue em uso "
            "pela Igreja Ortodoxa Etíope e é destino de peregrinação. Coberturas provisórias instaladas em 2008 "
            "para proteger cinco igrejas ficaram tanto tempo que hoje ameaçam desabar sobre elas."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Rock-Hewn_Churches,_Lalibela",
            "The eleven Rock-hewn Churches of Lalibela are monolithic churches located in the western Ethiopian Highlands near the town of Lalibela, named after the late-12th and early-13th century King Gebre Meskel Lalibela of the Zagwe dynasty, who commissioned the massive building project of 11 rock-hewn churches to recreate the holy city of Jerusalem in his own kingdom. "
            "The site remains in use by the Ethiopian Orthodox Christian Church to this day, and it remains an important place of pilgrimage for Ethiopian Orthodox worshipers. [...] "
            "Tradition holds that in Ethiopia prior to his accession to the throne, Gebre Meskel Lalibela was guided by Christ on a tour of Jerusalem, and instructed to build a second Jerusalem in Ethiopia. "
            "The churches are said to have been built during the Zagwe dynasty, under the rule of King Gebre Mesqel Lalibela (r. ca. 1181–1221 AD), although it is more likely that they evolved into their current form over the course of several phases of construction and alteration of preexisting structures. [...] "
            "At an altitude of around 2,480 metres (8,140 ft), the archaeological site consists of five churches north of the town's river Jordan, five south of the river, and one independently located. "
            "The churches in each grouping are connected by a system of tunnels and trenches. Biete Giorgis, the eleventh church, is connected to the others by trenches. [...] "
            "The rock-hewn churches at Lalibela are made through a subtractive processes in which space is created by removing material. "
            "Out of the 11 churches, 4 are free-standing (monolithic) and 7 share a wall with the mountain out of which they are carved. [...] "
            "All 11 churches were the result of a process using the basic tools of hammers and chisels to excavate trenches surrounding the monolithic and semi-monolithic structures [...] "
            "out of the scoriaceous basalt. The \"construction\" was done from top to bottom. [...] "
            "four shelters were erected in 2008 to cover five of the site's churches in an attempt to provide a temporary mode of protection [...] "
            "the shelters have remained in place now for far longer than they were meant to stay standing, and now consequently pose serious dangers to  the buildings underneath as they threaten to collapse",
            nome="Rock-Hewn Churches, Lalibela")],
    },
    # 8 Grande Zimbábue: a Rodésia censurava quem dissesse que africanos o construíram
    {
        "temas_secundarios": ["imperios_coloniais", "cidades"],
        "tipos_espanto": ["historia_humana", "mito_desmentido"],
        "gancho": "Na Rodésia dos anos 1960 e 1970, a versão oficial era que a cidade de pedra do Grande Zimbábue não fora erguida por negros. Um arqueólogo contou que podia dizer que \"povos amarelos\" a fizeram, mas não citar datações.",
        "explicacao": (
            "O Grande Zimbábue foi uma cidade de muralhas de pedra seca, sem argamassa, no sudeste do atual "
            "Zimbábue. Foi ocupada por ancestrais do povo shona a partir de cerca do ano 1000, e as grandes obras "
            "foram do século XI ao XV; o Grande Recinto tem muros de 11 metros de altura. Mas os colonos brancos da "
            "Rodésia achavam inconcebível que africanos a tivessem construído, e surgiram teorias que a "
            "atribuíam a judeus, árabes, fenícios, a qualquer um menos aos shona. A origem africana só virou "
            "consenso entre os estudiosos nos anos 1950. Mesmo assim, nos anos 1960 e 1970 o governo rodesiano "
            "manteve a linha oficial e censurou os arqueólogos que discordavam. Paul Sinclair, arqueólogo que "
            "trabalhava no sítio, relatou que um membro do conselho do museu ameaçou demiti-lo se dissesse em "
            "público que negros tinham construído a cidade; atribuí-la a \"povos amarelos\" podia, mas falar das "
            "datações por radiocarbono, não. Guias, exposições, livros escolares e filmes eram censurados. "
            "Arqueólogos de destaque, como Peter Garlake, acabaram deixando o país. Em 1980, o país independente "
            "ganhou o nome do sítio, e as aves de pedra-sabão achadas nas ruínas, que já estavam na bandeira e no "
            "brasão da Rodésia, passaram para a bandeira do Zimbábue."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Great_Zimbabwe",
            "Great Zimbabwe was a city in the south-eastern hills of the modern country of Zimbabwe, near Masvingo. "
            "It was settled by ancestral Shona people from around 1000 AD [...] "
            "Major construction on the city began in the 11th century and continued until the 15th century. [...] "
            "The Great Enclosure, with its 11 m (36 ft) high dry stone walls (constructed without mortar) [...] "
            "Its African origin did not become consensus among scholars until the 1950s. [...] "
            "Mired in racial prejudice, Rhodesians found it inconceivable that the structures could have been built by indigenous Africans [...] "
            "The refutation of various fantastical and dehumanising theories ascribing the construction to Jews, Arabs, Phoenicians, and anyone but the Shona [...] "
            "The official line in Rhodesia during the 1960s and 1970s was that the structures were built by non-blacks. "
            "Archaeologists who disputed the official statement were censored by the government. "
            "According to Paul Sinclair, interviewed for None But Ourselves:  I was the archaeologist stationed at Great Zimbabwe. [...] "
            "Censorship of guidebooks, museum displays, school textbooks, radio programmes, newspapers and films was a daily occurrence. "
            "Once a member of the Museum Board of Trustees threatened me with losing my job if I said publicly that blacks had built Zimbabwe. "
            "He said it was okay to say the yellow people had built it, but I wasn't allowed to mention radio carbon dates [...] "
            "This suppression of archaeology culminated in the departure from the country of prominent archaeologists of Great Zimbabwe, including Peter Garlake [...] "
            "In 1980 the new internationally recognised independent country was renamed for the site, and its famous soapstone bird carvings were retained from the Rhodesian flag and Coat of Arms as a national symbol and depicted in the new Zimbabwean flag.",
            nome="Great Zimbabwe")],
    },
    # 9 os "bronzes" do Benin são de latão alemão
    {
        "temas_secundarios": ["comercio_rotas", "dinheiro", "minerais_rochas"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "Os célebres bronzes do Benin, na Nigéria, são em sua maioria de latão, e o metal veio da Alemanha: um estudo de 2023 ligou-o à Renânia, de onde saíam as manilhas, braceletes usados como moeda no comércio português.",
        "explicacao": (
            "As cabeças, placas e figuras do antigo reino do Benin, no sul da atual Nigéria, foram feitas pelo "
            "povo edo pela técnica da cera perdida, e mais de 700 análises químicas mostram que a maioria é de "
            "latão, às vezes com chumbo, e não de bronze. Desde o fim do século XV, com a abertura do comércio "
            "português, centenas de milhares de anéis de cobre e latão em forma de ferradura, as manilhas, foram "
            "levados da Europa à África Ocidental. Suspeitava-se que fossem a matéria-prima das esculturas, mas "
            "estudos anteriores não achavam ligação. A equipe de Tobias Skowronek analisou manilhas de naufrágios "
            "e sítios em terra, datados do século XVI ao XIX, separando-as por tipo. As manilhas portuguesas mais "
            "antigas, chamadas \"tacoais\", têm isótopos de chumbo compatíveis com os minérios de chumbo e zinco da "
            "Renânia, região de forte indústria de latão entre Colônia e Aachen, e os isótopos dos bronzes do "
            "Benin são notavelmente parecidos com os desses minérios. Um contrato de 1548 entre a família de "
            "mercadores alemães Fugger e o rei de Portugal já previa dois tipos de manilha, conforme a região "
            "africana, porque os compradores eram exigentes. Os autores ressalvam que as manilhas talvez não "
            "tenham sido a única fonte de metal."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283415",
             "titulo": "German brass for Benin Bronzes: Geochemical analysis insights into the early Atlantic trade (PLOS ONE, 2023)",
             "idioma": "en",
             "trecho": "Utilizing geochemical analysis, this study identifies the sources of European brass used in the casting of the renowned Benin Bronzes, produced by the Edo people of Nigeria. "
                       "It is commonly believed that distinctive brass rings known as “manillas”, used as currency in the European trade in West Africa, also served as a metal source for the making of the Bronzes. "
                       "However, prior to the current study, no research had conclusively connected the Benin artworks and the European manillas. "
                       "For this research, manillas from shipwrecks in African, American and European waters dating between the 16th and 19th Century were analysed [...] "
                       "Over 700 available chemical analyses of Benin Bronzes [3] indicate that the majority are either brass or leaded brass, sometimes with small amounts of tin. [...] "
                       "Documentary sources indicate that hundreds of thousands of open horseshoe-shaped copper and brass rings, known as manillas, were shipped from Europe to West Africa with the opening of the Portuguese trade in the late 15th century [...] "
                       "the source of the early Portuguese “tacoais” manillas and, ultimately, the Benin Bronzes was the German Rhineland. "
                       "Written sources [17] suggest that beginning in the 15th century large quantities of manillas were produced in the German Rhineland industries between Cologne and Aachen [...] "
                       "The lead isotope ratios of the Benin Bronzes have striking similarity with the lead-zinc ores of the German Rhineland. [...] "
                       "African traders are said to have been extraordinarily particular on which manillas they would accept [...] "
                       "A contract between the German merchant family of Fugger and the Portuguese King dating to 1548 clearly identifies two types of manillas [...] "
                       "(2023) German brass for Benin Bronzes: Geochemical analysis insights into the early Atlantic trade. PLoS ONE 18(4): e0283415. [...] "
                       "However, the difference in trace elemental patterns between manillas and Benin Bronzes does not allow postulating that they have been the only source."},
            wiki("Benin_Bronzes",
                "The Kingdom of Benin, which occupied southern parts of present-day Nigeria [...] "
                "The metal pieces were made using lost-wax casting",
                nome="Benin Bronzes"),
        ],
    },
    # 10 a devolução dos bronzes do Benin e o museu que abriu sem nenhum
    {
        "temas_secundarios": ["imperios_coloniais", "crimes_arte"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Após anos de pressão, museus da Europa e dos EUA começaram a devolver à Nigéria os bronzes do Benin saqueados em 1897. Em 2023, um decreto deu as peças ao rei do Benin, e o museu feito para exibi-las abriu sem nenhuma.",
        "explicacao": (
            "Em 1897, uma expedição punitiva britânica tomou a cidade de Benin, na atual Nigéria, e levou a maior "
            "parte das placas e esculturas do palácio do oba, o rei. Duzentas peças foram para o Museu Britânico, "
            "e o resto se espalhou por museus europeus e americanos. Em 1988, talvez só umas cinquenta continuassem na "
            "Nigéria, contra cerca de 2.400 em coleções da Europa e dos EUA. As devoluções ganharam força bem "
            "depois: em julho de 2022, a Alemanha assinou uma declaração conjunta para restituir 1.130 bronzes, e o "
            "Smithsonian, nos EUA, transferiu a propriedade de 29 peças. Em 23 de março de 2023, porém, o presidente "
            "Muhammadu Buhari, em fim de mandato, decretou que todos os objetos devolvidos, inclusive os futuros, "
            "pertencem à família real do Benin, o que os tornou propriedade privada. O oba Ewuare II anunciou um "
            "museu perto do palácio. O Museu de Arte da África Ocidental, escolhido antes para exibir as peças e "
            "financiado em parte pelo governo alemão, abriu em 2024 sem nenhum bronze no acervo. Uma etnóloga "
            "suíça chamou a política alemã de restituição de \"fiasco\". As devoluções continuaram: em 2025, os "
            "Países Baixos entregaram 119 peças."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Benin_Bronzes",
            "Most of the plaques and other objects were taken by British forces during the Benin Expedition of 1897 [...] "
            "Following the expedition, two hundred pieces were taken to the British Museum in London, while the rest were taken to other European museums. [...] "
            "By 1988, perhaps as few as fifty pieces remained in Nigeria while approximately 2,400 pieces were held in European and American collections. [...] "
            "On 23 March 2023, departing president Muhammadu Buhari declared by decree that all repatriated objects from the Benin Expedition, including those repatriated in the future, belong to the Benin Royal Family in Benin City, thereby converting the bronzes into private property. "
            "Oba Ewuare II subsequently announced plans to put the bronzes in a future museum on or near his palace grounds. "
            "As a result, the Museum of West African Art, (MOWAA) which had been chosen to display the bronzes and was partially funded by the German government, opened in 2024 with no bronzes in its collection. [...] "
            "Swiss ethnologist Brigitta Hauser-Schäublin concluded that Germany's 2022 restitution policy was a \"fiasco\". [...] "
            "In July 2022, Germany became the first European country to sign a joint political declaration to restitute 1,130 bronzes. [...] "
            "The Smithsonian Institution's National Museum of African Art signed over ownership of 29 Benin bronzes to the NCMM on 11 October 2022 [...] "
            "In February 2025, Nigeria and the Netherlands concluded an agreement for the return of 119 bronzes [...] "
            "The palace of the Oba (king) of Benin in Benin City",
            nome="Benin Bronzes")],
    },
    # 11 as cabeças de Ife e a "Atlântida" de Frobenius
    {
        "temas_secundarios": ["mitologia", "imperios_coloniais"],
        "tipos_espanto": ["historia_humana", "mito_desmentido"],
        "gancho": "Diante das cabeças de metal realistas de Ife, na Nigéria, o etnólogo alemão Leo Frobenius disse que eram obra de gregos antigos e talvez a origem da lenda da Atlântida. Eram de artistas iorubás.",
        "explicacao": (
            "Ife é o centro religioso e real do povo iorubá, que a considera o lugar onde os deuses criaram os "
            "seres humanos. Quando Frobenius encontrou ali a primeira cabeça desse tipo, ela abalou a visão "
            "ocidental sobre a África: os especialistas não queriam acreditar que o continente tivesse tido uma "
            "civilização capaz de obras assim. Para explicar a \"anomalia\", Frobenius propôs que as peças tinham "
            "sido fundidas por uma colônia de gregos antigos do século XIII a.C., que poderia ser a origem da "
            "lenda da Atlântida, e a imprensa espalhou a ideia. Em janeiro de 1911, o New York Times noticiou que "
            "um alemão tinha descoberto a Atlântida na África, por causa de um \"Poseidon de bronze\". Em 1938, "
            "obras numa casa em Ife revelaram por acaso dezoito esculturas de liga de cobre, quase todas cabeças, "
            "provavelmente dos séculos XIV e XV. Hoje se reconhece que elas pertencem a uma tradição africana "
            "própria, de grande realismo, e as semelhanças sugerem um único artista ou uma só oficina. O cobre "
            "parece vir de minérios locais da Nigéria. Uma das cabeças foi levada do país e está no Museu "
            "Britânico desde 1939; o achado levou o governo colonial a controlar a exportação de antiguidades."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Ife_Head",
                "is one of eighteen copper alloy sculptures that were unearthed in 1938 at Ife in Nigeria, the religious and royal centre of the Yoruba people. "
                "It is believed to represent a king (Ooni). It was probably made in the 14th-15th century CE. "
                "The realism and sophisticated craftsmanship of the objects challenged the dismissive and patronising Western conceptions of African art. "
                "The naturalistic features of the Ife heads are unique and the stylistic similarities of these works \"suggest that they were made by an individual artist or in a single workshop.\" [...] "
                "The Ife Head was found by accident in 1938 at the Wunmonije Compound, Ife, during house-building works amongst sixteen other brass and copper heads and the upper half of a brass figure. [...] "
                "the British Museum in 1939. "
                "The discovery of the sculptures was the spur for the government to control the export of antiquities from Nigeria. [...] "
                "Ife is regarded by the Yoruba people as the place where their deities created humans. "
                "The copper used in this sculpture is thought to be from local Nigerian ores [...] "
                "When  Frobenius discovered the first example of a similar head it undermined existing Western understanding of African civilisation. "
                "Experts did not want to believe that Africa had ever had a civilisation capable of creating artefacts of this quality. "
                "Attempting to explain what was thought an anomaly, Frobenius offered his theory that these had been cast by a colony of ancient Greeks established in the thirteenth century BC. "
                "He made a claim, widely circulated in the popular press, that his hypothesised ancient Greek colony could be the origin of the ancient legend of the lost civilization of Atlantis. "
                "It is now recognised that these statues represent an indigenous African tradition that attained a high level of realism and refinement.",
                nome="Ife Head"),
            wiki("Leo_Frobenius",
                "Leo Viktor Frobenius (29 June 1873 – 9 August 1938) was a German self-taught ethnologist and archaeologist [...] "
                "\"German Discovers Atlantis In Africa; Leo Frobenius Says Find of Bronze Poseidon Fixes Lost Continent's Place\". The New York Times. 30 January 1911.",
                nome="Leo Frobenius"),
        ],
    },
    # 12 a cabeça Nok que serviu de espantalho
    {
        "temas_secundarios": ["pre_historia", "crimes_arte"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Uma cabeça de terracota da cultura Nok, na Nigéria, passou um ano como espantalho numa roça de inhame até ser reconhecida. Fora a arte egípcia, a escultura Nok é a mais antiga arte figurativa grande da África.",
        "explicacao": (
            "As primeiras terracotas Nok apareceram por acaso em 1928, a 7 metros de profundidade, numa mina de "
            "estanho perto da aldeia de Nok, no centro da Nigéria. Em 1943, a mineração revelou mais peças. Um "
            "funcionário da mina levou uma cabeça para casa e a usou como espantalho num campo de inhame, função "
            "que ela cumpriu com sucesso por um ano. Quem a notou foi Bernard Fagg, administrador colonial que "
            "tinha estudado arqueologia em Cambridge: ela lembrava a escultura achada em 1928. Ficou claro então "
            "que a mineração de estanho estava revelando e destruindo material arqueológico. As figuras são ocas, "
            "montadas com rolos de argila, com cabeças e corpos quase em tamanho natural, penteados minuciosos e "
            "muitas joias. As mais antigas podem ser de cerca de 900 a.C., e a cultura pode ter durado até 1 a.C. "
            "Para que serviam ainda não se sabe: as hipóteses vão de retratos de ancestrais e marcadores de "
            "túmulos a amuletos contra quebra de safra, infertilidade e doença. Peças grandes e inteiras são raras "
            "e muito valorizadas no mercado internacional de arte, e quando um projeto alemão começou a procurar "
            "sítios Nok, a maioria dos que encontrou já tinha sido saqueada."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Nok_culture",
            "Nok culture may have emerged in 1500 BCE and continued to persist until 1 BCE. [...] "
            "The earliest Nok terracotta sculptures may have developed in 900 BCE. [...] "
            "Excluding ancient Egyptian figurative art, Nok sculptures are regarded to be the earliest examples of large three-dimensional (sculptural) figurative art in continental Africa. [...] "
            "The first Nok terracotta was discovered in 1928 by Colonel Dent Young, a co-owner of a mining partnership, near the village of Nok in Kaduna State, Nigeria. "
            "The terracotta was accidentally unearthed at a level of 24 feet (7 m) from an alluvial tin mine. [...] "
            "Fifteen years later, in 1943 near the village of Nok, in the center of Nigeria, a new series of clay figurines were discovered by accident while mining tin. "
            "A clerk in charge of the mine had found a head and had taken it back to his home for use as a scarecrow, a role that it filled (successfully) for a year in a yam field. "
            "This scarecrow was eventually noticed by Bernard Fagg who at the time was an administrative officer who had studied archaeology at the University of Cambridge. "
            "Fagg noticed that the head on the scarecrow looked similar to the sculpture that Young had found. [...] "
            "Eventually it became clear that the tin mining in Nok and Jema'a areas was revealing and destroying archaeological material. [...] "
            "they started finding distinct Nok culture sites, although most had been looted. [...] "
            "The function of Nok terracotta sculptures is still unknown. [...] "
            "Rarely are works of great size conserved intact making them highly valued on the international art market. "
            "The terracotta figures are hollow, coil built, nearly life sized human heads and bodies that are depicted with highly stylized features, abundant jewelry, and varied postures. [...] "
            "theories include ancestor portrayal, grave markers, and charms to prevent crop failure, infertility, and illness.",
            nome="Nok culture")],
    },
    # 13 moedas de Kilwa numa praia da Austrália
    {
        "temas_secundarios": ["comercio_rotas", "dinheiro", "navegacao_antiga"],
        "tipos_espanto": ["misterio_aberto", "conexao_inesperada"],
        "gancho": "Em 1944, um militar australiano achou numa praia do norte da Austrália moedas do sultanato de Kilwa, na costa da atual Tanzânia, cunhadas séculos antes. Como elas foram parar lá ninguém sabe.",
        "explicacao": (
            "Durante a Segunda Guerra, Morry Isenberg servia numa estação de radar da força aérea australiana na "
            "ilha Marchinbar, a maior das ilhas Wessel, no Território do Norte. Pescando perto dali, achou nove "
            "moedas: quatro holandesas, de 1690 à década de 1780, e cinco com inscrições em árabe, do sultanato "
            "de Kilwa. Kilwa Kisiwani, ilha da costa sul da Tanzânia, foi um porto rico: a partir do século XI, "
            "seus sultões controlavam o comércio de ouro, marfim e escravizados. As inscrições identificam um "
            "sultão, mas não está claro se ele reinou no século X ou no XIV. As hipóteses vão de um navio árabe a "
            "um navio português que levasse moedas de Kilwa depois que Portugal destruiu o sultanato, em 1505; "
            "também se cogita um naufrágio ou até um colecionador. Nem se sabe se as moedas africanas e as "
            "holandesas chegaram juntas. Uma expedição de 2013 localizou o ponto marcado num mapa que Isenberg "
            "desenhou décadas depois, mas a origem das moedas continuou indefinida. Em 2018, uma moeda parecida, "
            "tida como do sultanato de Kilwa, foi achada na ilha Elcho, no mesmo arquipélago."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Marchinbar_Island",
                "Marchinbar Island is the largest island in the Wessel Islands in the Northern Territory of Australia in the Arafura Sea. [...] "
                "In 1944, nine coins were discovered at Djinjan creek immediately south of Jensen Bay. "
                "Four of the coins were later identified as Dutch duits dating from 1690 to the 1780s while five with Arabic inscriptions were identified as being from the Kilwa Sultanate of east Africa. [...] "
                "The inscriptions on the Jensen Bay coins identify a ruling Sultan of Kilwa, but it is unclear whether the ruler was from the 10th century or the 14th century. [...] "
                "A similar coin, also thought to be from the Medieval Kilwa sultanate, was found in 2018 on Elcho Island, also in the Wessel Islands group.",
                nome="Marchinbar Island"),
            {"url": "https://www.australiangeographic.com.au/?p=15761",
             "titulo": "Unravelling the mystery of Arnhem Land's ancient African coins (Australian Geographic)",
             "idioma": "en",
             "trecho": "found on one of the archipelago’s beaches during WWII by RAAF serviceman Morry Isenberg. [...] "
                       "The island of Kilwa Kisiwani, off the south coast of Tanzania, was once a thriving seaport. "
                       "From the 11th century, the sultans of Kilwa grew rich controlling the gold, ivory and slave trade [...] "
                       "a map that late RAAF serviceman Morry Isenberg had drawn in the early 1980s. "
                       "That was more than 30 years after he’d found the Kilwa coins (along with four Dutch coins from the 17th and 18th centuries) while fishing, not far from the Marchinbar radar station at which he was based. [...] "
                       "In the end, the provenance of the coins proved to be elusive. "
                       "It is unclear whether the Kilwa and Dutch coins Isenberg found arrived on the island together. "
                       "They may have been carried to Marchinbar by early traders, or given to the Yolngu much later in exchange for use of the freshwater lagoon at Jensen Bay. "
                       "Perhaps they were left by a collector, or were washed up after a shipwreck. [...] "
                       "speculates the coins could be from an Arab ship, similar to a wreck discovered off Sumatra in 1998. "
                       "Or they may have come off a Portuguese vessel that carried Kilwa coins after the Portuguese destroyed the African sultanate in 1505. [...] "
                       "So in July 2013"},
        ],
    },
    # 14 "Abubakari II", o rei navegador que nunca reinou
    {
        "temas_secundarios": ["grandes_navegacoes", "navegacao_antiga", "mundo_islamico_medieval"],
        "tipos_espanto": ["mito_desmentido", "misterio_aberto"],
        "gancho": "Mansa Musa contou no Cairo que seu antecessor partiu pelo Atlântico com uma frota enorme e nunca voltou. O rei costuma ser chamado de Abubakari II, mas esse nome nasceu de um erro de tradução do século XIX.",
        "explicacao": (
            "Em 1324, a caminho de Meca, Mansa Musa, governante do império do Mali, passou três meses no Cairo e "
            "ficou amigo de um emir. Perguntado sobre como virou rei, contou que o antecessor não acreditava ser "
            "impossível achar o limite do Atlântico: mandou 200 navios com homens e outros 200 com ouro, água e "
            "comida. Só um voltou, e o capitão falou de um \"rio\" de forte correnteza no mar aberto onde os outros "
            "sumiram. O rei então partiu em pessoa, com 2.000 navios, deixou Musa no governo e nunca mais foi visto. "
            "O relato foi registrado pelo historiador árabe al-Umari e é a única fonte sobre a viagem: nem outros "
            "historiadores árabes medievais nem a tradição oral do oeste africano a mencionam. O \"rio\" no mar "
            "seria a corrente das Canárias, que corre da África para as Américas. O nome Abubakari, ou Abu Bakr II, "
            "vem de uma tradução errada de Ibn Khaldun pelo barão de Slane: no original árabe, Abu Bakr aparece só "
            "como ancestral da linhagem de Musa, não como rei. Pela lista de Ibn Khaldun, o antecessor de Musa foi "
            "Muhammad ibn Qu. Se algum navio chegou às Américas, ninguém sabe: nunca se achou prova incontestável "
            "de contato entre a África e a América antes de Colombo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Abu_Bakr_II",
            "In 1324, while staying in Cairo during his hajj, Mansa Musa, the ruler of the Mali Empire, told an Egyptian official whom he had befriended that he had come to rule when his predecessor led a large fleet in an attempt to cross the Atlantic Ocean and never returned. "
            "This account, recorded by the Arab historian al-Umari, has attracted considerable interest and speculation as a possible instance of pre-Columbian trans-oceanic contact. "
            "The voyage is popularly attributed to a Mansa Abu Bakr II, but no such mansa ever reigned. [...] "
            "Mansa Musa stayed in Cairo for three months in 1324 while en route to Mecca for the hajj. While there, he befriended an emir [...] "
            "The king who was my predecessor did not believe that it was impossible to discover the furthest limit of the Atlantic Ocean and wished vehemently to do so. "
            "So he equipped 200 ships filled with men and the same number equipped with gold, water, and provisions enough to last them for years [...] "
            "Then one ship returned [...] "
            "there appeared in the open sea [as it were] a river with a powerful current. [...] "
            "Then that sultan got ready 2,000 ships, 1,000 for himself and the men whom he took with him and 1,000 for water and provisions. "
            "He left me to deputize for him and embarked on the Atlantic Ocean with his men. That was the last we saw of him [...] "
            "Al-Umari’s record of this conversation is the only known account of this voyage, as it is not mentioned by other medieval Arab historians or West African oral tradition. [...] "
            "According to the Arab historian Ibn Khaldun, writing several decades later, Musa's predecessor as mansa was Muhammad ibn Qu (Mansa Muhammad). [...] "
            "However, the inclusion of a Mansa Abu Bakr II in the list of Malian rulers is an error that originated in a mistranslation of Ibn Khaldun’s text by the 19th-century European historian Baron de Slane. [...] "
            "However, in the original Arabic text, Abu Bakr is only mentioned in his role as the progenitor of Musa's lineage, not as a ruler. [...] "
            "No uncontroversial evidence of pre-Columbian contact between Africa and the Americas has ever been found. [...] "
            "The river on the sea described by the survivor of the first expedition is presumably the Canary Current. [...] "
            "The Canary Current flows from West Africa to the Americas",
            nome="Abu Bakr II")],
    },
    # 15 a África subsaariana pulou a Idade do Bronze
    {
        "temas_secundarios": ["pre_historia", "minerais_rochas", "elementos_quimicos"],
        "tipos_espanto": ["misterio_aberto", "contraintuitivo"],
        "gancho": "Na África ao sul do Saara, em geral não houve Idade do Bronze: o trabalho com cobre não veio antes do ferro. E até hoje se discute se a metalurgia do ferro foi inventada ali ou chegou de fora.",
        "explicacao": (
            "A divisão em idades da pedra, do bronze e do ferro funciona para o norte da África e o Chifre, que "
            "seguem o padrão do Oriente Próximo e do Mediterrâneo, mas não para a África subsaariana, onde em "
            "geral a metalurgia do cobre não antecede a do ferro. A origem desse ferro é discutida desde os anos "
            "1860. Entre 1945 e 1965, a maioria dos arqueólogos achava que a técnica tinha cruzado o Saara a partir "
            "de Cartago ou subido o Nilo a partir de Meroé. No fim dos anos 1960, datações por radiocarbono "
            "surpreendentemente antigas no Níger e na África central reavivaram a ideia de invenção independente. "
            "As armadilhas são muitas: no Níger, tocos carbonizados de árvores antigas, que fornecem carvão bem "
            "mais velho que a fundição, já foram confundidos com fornos. Em 2007, uma forja em Oboui, na República "
            "Centro-Africana, deu oito datas consistentes de cerca de 2000 a.C., o que a tornaria o sítio de "
            "trabalho com ferro mais antigo do mundo; os arqueólogos africanistas se dividiram, e um deles "
            "argumentou que o sítio estava revolvido. Em 2014 e em 2018, dois especialistas concluíram que a "
            "invenção independente é a hipótese mais provável, mas a resposta definitiva ainda não existe."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Iron_metallurgy_in_Africa",
            "Whereas the development of iron metallurgy in North Africa and the Horn closely mirrors that of the Ancient Near East and Mediterranean region, the three-age system is ill-suited to Sub-Saharan Africa, where copper metallurgy generally does not precede iron working. [...] "
            "on working in Africa have been the subject of scholarly interest since the 1860s, it is still not known whether this technology diffused into sub-Saharan Africa from the Mediterranean region, or whether it was invented there independently of iron working elsewhere. [...] "
            "archaeologists writing between 1945 and 1965 mostly favored diffusion of iron smelting technology from Carthage across the Sahara to West Africa and/or from Meroe on the upper Nile to central Africa. [...] "
            "By the late 1960s some surprisingly early radiocarbon dates had been obtained for iron smelting sites in both Niger and central Africa (Rwanda, Burundi), reviving the view that iron-making was independently invented [...] "
            "This is a particular problem in Niger, where the charred stumps of ancient trees are a potential source of charcoal, and have sometimes been misidentified as smelting furnaces. [...] "
            "Controversy flared again in 2007 with the publication of excavations by Étienne Zangato and colleagues in the Central African Republic. "
            "At Oboui they excavated an undated iron forge yielding eight consistent radiocarbon dates of 2000 BCE. "
            "This would make Oboui the oldest iron-working site in the world [...] "
            "Opinion among African archaeologists is sharply divided. Some specialists accept this interpretation, but archaeologist Bernard Clist has argued that Oboui is a highly disturbed site [...] "
            "In 2014, archaeo-metallurgist Manfred Eggert argued that, though still inconclusive, the evidence overall suggests an independent invention of iron metallurgy in sub-Saharan Africa. "
            "In a 2018 study, archaeologist Augustin Holl also argues that an independent invention is most likely.",
            nome="Iron metallurgy in Africa")],
    },
    # 16 o resgate dos manuscritos de Tombuctu
    {
        "temas_secundarios": ["mundo_islamico_medieval", "literatura"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Em 2012 e 2013, com jihadistas ocupando Tombuctu, no Mali, bibliotecários e moradores tiraram da cidade cerca de 350 mil manuscritos antigos em baús, por estrada e pelo rio Níger. Muitos mensageiros eram adolescentes.",
        "explicacao": (
            "Por séculos, famílias de Tombuctu guardaram em casa manuscritos sobre arte, medicina, filosofia e "
            "ciência, além de cópias do Corão, datados do fim do século XIII ao início do XX. Quando grupos "
            "jihadistas tomaram o norte do Mali, em 2012, o bibliotecário Abdel Kader Haidara organizou uma "
            "retirada secreta com a americana Stephanie Diakité. Segundo a reportagem de Joshua Hammer na revista "
            "Smithsonian, a equipe comprou quase 2.500 baús nos mercados, encheu-os de dia, a portas fechadas, e de "
            "madrugada os levou em carroças de mula para casas seguras. Depois, os baús desceram para o sul, rumo "
            "a Bamako, em carros e em barcos que andavam dia e noite pelo rio, no máximo 15 baús por barco. Os "
            "mensageiros eram muitas vezes filhos e sobrinhos adolescentes dos donos das bibliotecas. Perto do lago "
            "Debo, homens armados detiveram uma flotilha de 20 barcos e só a liberaram com a promessa de um "
            "pagamento. Antes de fugir da cidade, em janeiro de 2013, os ocupantes juntaram 4.202 manuscritos no "
            "pátio do Instituto Ahmed Baba e puseram fogo. Nunca desceram, porém, ao porão, onde havia 10.603 "
            "manuscritos restaurados. Em Bamako, os textos salvos enfrentaram outro inimigo: o mofo e a umidade."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Timbuktu_Manuscripts",
                "manuscripts that have been preserved for centuries in private households in Timbuktu, a city in northern Mali. "
                "The collections include manuscripts about art, medicine, philosophy, and science, as well as copies of the Quran. [...] "
                "The dates of the manuscripts range between the late 13th and the early 20th centuries [...] "
                "Some 350,000 manuscripts were transported to safety, and 300,000 of them were still in Bamako in 2022. [...] "
                "following the fall of Timbuktu in the Northern Mali conflict between 2012 and 2013 [...] "
                "U.S.-based book preservation expert Stephanie Diakité and Dr. Abdel Kader Haidara, curator of one of the most important libraries of Timbuktu [...] "
                "organized the evacuation of the manuscripts to Bamako in the south of Mali. [...] "
                "Once in the south, the manuscripts faced new dangers: mold and humidity.",
                nome="Timbuktu Manuscripts"),
            {"url": "https://www.smithsonianmag.com/history/Race-Save-Mali-Artifacts-180947965/",
             "titulo": "The Race to Save Mali’s Priceless Artifacts (Smithsonian Magazine)",
             "idioma": "en",
             "trecho": "The objective: to carry 350,000 manuscripts to safety in the government-held south. "
                       "The treasures moved by road and by river, by day and by night, past checkpoints manned by armed Islamic police. [...] "
                       "he began purchasing footlockers in the markets of Timbuktu and Mopti [...] "
                       "During the day, behind closed doors, Haidara and his assistants packed the manuscripts into the chests. "
                       "Then, in the dead of night, when the militants slept, mule carts transported the chests to safe houses scattered around the city. "
                       "Over three months, they bought, distributed and packed nearly 2,500 footlockers. [...] "
                       "his couriers—often the teenage sons and nephews of Timbuktu library owners—made the same perilous journey. [...] "
                       "each pinasse would have two couriers and two captains, so they could keep moving on the river 24 hours a day. "
                       "No vessel could carry more than 15 footlockers [...] "
                       "It was during this period that the 20-boat flotilla was hijacked by gunmen near Lake Debo. [...] "
                       "he said to the hijackers, ‘Trust me on this, we will get you your money,’” says Diakité. "
                       "After some consideration, the gunmen allowed the boats and their footlockers, containing 75,000 manuscripts, to continue. [...] "
                       "On Friday, January 25, they entered the restoration and digitization rooms [...] "
                       "they put 4,202 manuscripts in a pile in the courtyard, doused them with gasoline and set them on fire. [...] "
                       "the jihadists had never once ventured downstairs to the basement to inspect a dry, dark storage room behind a locked door. "
                       "Inside were stacks containing 10,603 restored manuscripts"},
        ],
    },
    # 17 Afonso I do Congo e a carta de 1526 contra os sequestros
    {
        "temas_secundarios": ["heranca_africana", "imperios_coloniais", "grandes_navegacoes"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1526, o rei Afonso I do Congo escreveu ao rei de Portugal que mercadores sequestravam seu povo, até parentes do rei, para vendê-los como escravizados. Mas ele mesmo vendia cativos de guerra aos portugueses.",
        "explicacao": (
            "Nascido Mvemba a Nzinga, por volta de 1456, ele se converteu ao catolicismo e reinou no Congo de "
            "1509 até 1542 ou 1543. Quase tudo o que se sabe do reino nesse período vem das suas longas cartas, "
            "escritas em português, sobretudo aos reis Manuel I e João III. Afonso mandou filhos e nobres "
            "estudarem na Europa, e um deles, Henrique, foi elevado a bispo em 1518. O comércio com Portugal "
            "envolvia marfim, cobre e tecido de palmeira, e também gente escravizada: numa carta, Afonso conta a "
            "D. Manuel ter enviado 410 cativos de uma guerra de 1512, e pagava com escravizados a educação de nobres "
            "congoleses e mercadorias como armas de fogo. A lei do Congo proibia escravizar ou vender "
            "para fora pessoas livres do reino. Com a procura portuguesa crescendo, porém, nobres passaram a "
            "exportar gente ilegalmente, e alguns sequestravam congoleses livres. Na carta de 1526, Afonso "
            "protestou que a cada dia os mercadores levavam sua gente, inclusive membros da família real, e que a "
            "terra estava se despovoando; contou que os capturados eram marcados com ferro em brasa. Ele não "
            "aboliu o tráfico: ameaçou encerrá-lo se Portugal não controlasse seus mercadores, exigiu o respeito à "
            "lei congolesa e criou uma junta para fiscalizar o comércio."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Afonso_I_of_Kongo",
            "Mvemba a Nzinga, Nzinga Mbemba, Funsu Nzinga Mvemba or Dom Afonso (c. 1456 – 1542 or 1543), also known as King Afonso I [...] "
            "He reigned over the Kongo Empire from 1509 to late 1542 or 1543. [...] "
            "Afonso sent many of his children and nobles to Europe to study, including his son Henrique Kinu a Mvemba, who was elevated to the status of bishop in 1518. [...] "
            "Trade between Portugal and Kongo at the start of Afonso's reign mainly consisted of ivory, copper, and palm cloth, but also an increasing trickle of slaves. [...] "
            "In 1512, Afonso led a military campaign against the Kingdom of Ndongo to the south; in correspondence with King Manuel of Portugal, Afonso mentioned that he had sent him 410 slaves captured during the war. [...] "
            "Slaves became increasingly used as currency in the Kongo, with Afonso sending slaves to Portugal to pay for the education of Kongolese notables and to buy trade goods, such as firearms. [...] "
            "Kongo had traditions in place that regulated the slave trade—the sale or enslavement of Kongolese freemen was prohibited, as was the export of female slaves. [...] "
            "However, as the Portuguese demand for slaves grew, these laws were increasingly subverted. [...] "
            "To pay for these imports, some Kongolese nobles illegally exported slaves to the Portuguese, with some going so far as to kidnap and enslave freeborn Kongolese. "
            "These developments worried and angered Afonso, who issued a letter protesting the circumvention of Kongolese law in 1526. [...] "
            "Each day the traders are kidnapping our people – children of this country, sons of our nobles and vassals, even people of our own family. "
            "This corruption and depravity are so widespread that our land is entirely depopulated. [...] "
            "As soon as the captives are in the hands of white men they are branded with a red-hot iron. "
            "To counter the trade in illegally-exported Kongolese slaves, Afonso threatened to end the slave trade if Portugal did not intervene and better regulate its merchants. "
            "To reform the trade, Afonso reiterated the need to follow Kongolese law and not enslave Kongolese freemen, while also establishing a board to better regulate the slave trade. [...] "
            "Virtually all that is known about Kongo in the time of Afonso's reign is known from his long series of letters, written in Portuguese, primarily to the kings Manuel I and João III of Portugal. [...] "
            "Afonso became a fervent convert to Catholicism",
            nome="Afonso I of Kongo")],
    },
]
