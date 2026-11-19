LOTE = "2026-11-19-roma_antiga-01"
AREA = "historia_antiga"
TEMA = "roma_antiga"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 os papiros de Herculano e a palavra "púrpura"
    {
        "temas_secundarios": ["vulcoes_terremotos", "decifracao", "ia_robotica"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "O Vesúvio transformou uma biblioteca romana inteira em carvão, e muitos rolos foram jogados fora como tal. Em 2023, um estudante de 21 anos leu, em raios X, a primeira palavra de um rolo fechado: \"púrpura\".",
        "explicacao": (
            "Os papiros de Herculano são mais de 1.800 rolos achados no século XVIII numa casa de campo da cidade, "
            "a Vila dos Papiros. Na erupção de 79, o calor intenso os carbonizou num cômodo sem oxigênio, e eles "
            "viraram blocos compactos e muito frágeis. É a única biblioteca da Antiguidade que chegou inteira até "
            "nós, com muitos textos gregos de filosofia. Quando apareceram, pareciam pedaços de carvão, e vários "
            "acabaram no lixo. Abrir os outros foi um desastre: muitos foram destruídos, e o primeiro desenrolado "
            "com a máquina inventada pelo padre Antonio Piaggio levou quatro anos, milímetro a milímetro. A saída "
            "foi tentar ler sem abrir, mas a tinta, à base de carbono, quase não se distingue do papiro carbonizado "
            "numa tomografia. O que denuncia a tinta é que o rolo fica um pouco mais espesso onde há letra. Em "
            "2023, o concurso Vesuvius Challenge premiou Luke Farritor, estudante de computação da Universidade de "
            "Nebraska, por detectar num rolo nunca aberto a palavra porphyras, \"púrpura\" em grego. Em junho de "
            "2026, a equipe anunciou a leitura de ponta a ponta de um rolo inteiro: 22 colunas de um tratado de "
            "filosofia estoica."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Herculaneum_papyri",
            "The Herculaneum papyri are more than 1,800 scrolls of papyrus discovered in the 18th century in the Villa of the Papyri in Herculaneum. "
            "They had been carbonized when the villa was engulfed by the eruption of Mount Vesuvius in 79 AD. "
            "The papyri, containing a number of Greek philosophical texts, come from the only surviving library from antiquity that exists in its entirety. [...] "
            "This intense parching took place over an extremely short period of time, in a room deprived of oxygen, resulting in the scrolls' carbonization into compact and highly fragile blocks. [...] "
            "In appearance the rolls resembled lumps of charcoal; and many were thrown away as such. [...] "
            "Opening a scroll would often damage or destroy the scroll completely. [...] "
            "With X-ray micro-computed tomography (micro-CT), no ink can be seen, as carbon-based ink is not visible on carbonized papyrus. [...] "
            "In 1756, Abbot Piaggio, conserver of ancient manuscripts in the Vatican Library, used a machine he also invented, to unroll the first scroll, which took four years (millimeters per day). [...] "
            "The Herculaneum papyri were written using a carbon-based ink, the chemical composition of which is extremely similar to that of the surrounding carbonized parchment. [...] "
            "However, the presence of ink at a particular point on the parchment results in the scroll being slightly thicker at that point than in its immediate vicinity. [...] "
            "a competition to \"decipher Herculaneum scrolls using 3D X-ray software\". [...] "
            "On 12 October 2023, the project awarded $40,000 to Luke Farritor, a 21-year-old computer science student at the University of Nebraska, for successfully detecting the first word in an unopened scroll: porphyras [...] "
            "In June 2026, the Vesuvius Challenge team announced that PHerc. 1667, known within the project as \"Scroll 4\", had been virtually unwrapped and read end-to-end. [...] "
            "In the PHerc. 1667, 22 columns of text were recovered, containing \"a Stoic philosophical treatise that may be attributable to Chrysippus\".",
            nome="Herculaneum papyri")],
    },
    # 2 o Monte Testaccio, morro de ânforas
    {
        "temas_secundarios": ["comercio_rotas", "cidades", "elementos_quimicos"],
        "tipos_espanto": ["escala_absurda", "engenhosidade"],
        "gancho": "Em Roma há um morro de 35 metros feito quase só de cacos de ânforas de azeite, cerca de 53 milhões delas. Não era um lixão qualquer: foi erguido em terraços, com cal por cima contra o cheiro de óleo rançoso.",
        "explicacao": (
            "O Monte Testaccio fica perto do rio Tibre, junto aos armazéns onde o Estado guardava a reserva de "
            "azeite no fim do século II. Tem 2 hectares na base e quase um quilômetro de circunferência, e devia "
            "ser bem mais alto na Antiguidade. A Roma imperial, a maior cidade do mundo na época, com pelo menos "
            "um milhão de habitantes, consumia azeite em quantidades enormes. As ânforas vinham sobretudo da "
            "Bética, no sul da atual Espanha. Escavações de 1991 mostraram que o morro foi montado em terraços, com "
            "muros de contenção feitos de ânforas quase inteiras cheias de cacos. Os vasos vazios provavelmente "
            "subiam no lombo de burros ou mulas e eram quebrados lá em cima. Por que só as de azeite? Uma hipótese "
            "é que esse modelo se partia em cacos grandes e curvos, difíceis de reaproveitar. Outra é química: os "
            "cacos ficavam gordurosos, e o óleo reage com a cal, ingrediente do concreto, formando sabão, o que "
            "estragaria a obra. Já as ânforas de trigo e de vinho podiam virar concreto. As inscrições pintadas "
            "nos vasos, com o peso do azeite, os nomes de quem pesou e a região de origem, são hoje uma janela "
            "rara para a economia romana."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Monte_Testaccio",
            "is an artificial mound in Rome composed almost entirely of testae (Italian: cocci), fragments of broken ancient Roman pottery, nearly all discarded amphorae [...] "
            "covering an area of 2 hectares (4.9 acres) at its base and with a volume of approximately 580,000 cubic metres (760,000 cu yd), containing the remains of an estimated 53 million amphorae. "
            "It has a circumference of nearly a kilometre (0.6 mi) and stands 35 metres (115 ft) high, though it was probably considerably higher in ancient times. "
            "It stands a short distance away from the east bank of the River Tiber, near the Horrea Galbae where the state-controlled reserve of olive oil was stored in the late 2nd  century AD. [...] "
            "The huge numbers of broken amphorae at Monte Testaccio illustrate the enormous demand for oil of imperial Rome, which was at the time the world's largest city, with a population of at least one million people. [...] "
            "Monte Testaccio was not simply a haphazard waste dump; it was a highly organised and carefully engineered creation [...] "
            "Excavations carried out in 1991 showed that the mound had been raised as a series of level terraces with retaining walls made of nearly intact amphorae filled with sherds to anchor them in place. "
            "Empty amphorae were probably carried up the mound intact on the backs of donkeys or mules and then broken up on the spot [...] "
            "Lime appears to have been sprinkled over the broken pots to neutralise the smell of rancid oil. [...] "
            "The hill was constructed using mostly the fragments of large globular 70-liter (15 imp gal; 18 U.S. gal) vessels from Baetica (the Guadalquivir region of modern Spain) [...] "
            "The Dressel 20 amphora, however, broke into large curved fragments that could not readily be reduced to small shards. [...] "
            "Another reason for not re-cycling olive oil amphorae into concrete of the opus signinum type may have been that the fragments were too fatty due to residual oil. "
            "Also, oil happens to react chemically with lime (a major component of concrete) and the product of this chemical reaction is soap; the resulting concrete would have had unsatisfactory quality.  "
            "Wheat amphorae and wine amphorae on the other hand were certainly \"clean\" enough to be recycled into concrete. [...] "
            "Monte Testaccio has provided archaeologists with a rare insight into the ancient Roman economy. "
            "The amphorae deposited in the mound were often labelled with tituli picti, painted or stamped inscriptions which record information such as the weight of the oil contained in the vessel, the names of the people who weighed and documented the oil and the name of the district where the oil was originally bottled.",
            nome="Monte Testaccio")],
    },
    # 3 o ano de 445 dias e o "bissexto"
    {
        "temas_secundarios": ["calendarios", "palavras_portugues", "leis_julgamentos"],
        "tipos_espanto": ["escala_absurda", "origem_inesperada"],
        "gancho": "O ano 46 a.C. teve 445 dias. Júlio César o esticou para realinhar o calendário com o Sol, depois de anos em que sacerdotes alongavam o ano, ou deixavam de alongá-lo, conforme a conveniência política.",
        "explicacao": (
            "O ano romano comum tinha 355 dias, e de vez em quando os pontífices inseriam depois de fevereiro um "
            "mês extra, que somava 22 ou 23 dias ao ano, para acompanhar as estações. Só que muitos pontífices "
            "eram políticos, e o mandato dos magistrados durava um ano civil. A regra virou arma: dava para alongar "
            "o ano em que um aliado estava no cargo, ou recusar o alongamento quando quem mandava era o adversário. "
            "César, ele próprio pontífice, decidiu acertar tudo de uma vez. O ano 46 a.C., que já tinha ganhado o "
            "mês extra e passado de 355 para 378 dias, recebeu mais 67 dias, em dois meses extraordinários entre "
            "novembro e dezembro. Ele ficou conhecido como o \"último ano da confusão\". A partir de 45 a.C. valeu o "
            "calendário juliano, de 365 dias, feito para ficar alinhado ao Sol sem intervenção humana. Mesmo "
            "assim, no começo os pontífices erraram e puseram o dia extra a cada três anos, e não a cada quatro. "
            "Esse dia era contado como um \"sexto dia repetido\" antes das calendas de março, bis sextum, e o ano "
            "em que ele caía era o annus bissextus. Daí vem o nosso \"ano bissexto\", que nada tem a ver com os "
            "dois seis de 366, como às vezes se diz."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Julian_calendar",
                "The ordinary year in the previous Roman calendar consisted of 12 months, for a total of 355 days. [...] "
                "The net effect was to add 22 or 23 days to the year, forming an intercalary year of 377 or 378 days. [...] "
                "However, since the pontifices were often politicians, and because a Roman magistrate's term of office corresponded with a calendar year, this power was prone to abuse: "
                "a pontifex could lengthen a year in which he or one of his political allies was in office, or refuse to lengthen one in which his opponents were in power. "
                "Caesar's reform was intended to solve this problem permanently, by creating a calendar that remained aligned to the sun without any human intervention. [...] "
                "The first step of the reform was to realign the start of the calendar year (1 January) to the tropical year by making 46 BC 445 days long, compensating for the intercalations which had been missed during Caesar's pontificate. "
                "This year had already been extended from 355 to 378 days by the insertion of a regular intercalary month in February. [...] "
                "he added 67 more days by inserting two extraordinary intercalary months between November and December. [...] "
                "this extra-long year was, and is, referred to as the \"last year of confusion\". "
                "The new calendar began operation after the realignment had been completed, in 45 BC. [...] "
                "creating a regular Julian year of 365 d [...] "
                "the pontifices initially added a leap day every three years, instead of every four. [...] "
                "The new leap day was dated as ante diem bis sextum Kalendas Martias ('the sixth doubled day before the Kalends of March') [...] "
                "The year in which it occurred was termed annus bissextus",
                nome="Julian calendar"),
            wiki("Ano_bissexto",
                "A origem do nome bissexto advém da implantação do Calendário Juliano em 45 a.C. [...] "
                "Hoje a expressão bissexto vez ou outra é associada ao duplo seis (66) da expressão 366, o que expressa uma coerência mnemônica popular, porém, aos estudiosos é um grande e histórico equívoco.",
                nome="Ano bissexto", idioma="pt"),
        ],
    },
    # 4 o trono leiloado em 193
    {
        "temas_secundarios": ["dinheiro", "leis_julgamentos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 193, a Guarda Pretoriana matou o imperador e pôs o trono em leilão. Venceu um ex-cônsul que, barrado na porta, gritava os lances do lado de fora: 25 mil sestércios por soldado. Ele reinou só 66 dias.",
        "explicacao": (
            "Os pretorianos assassinaram o imperador Pertinax em 28 de março de 193 e anunciaram que o trono seria "
            "vendido a quem pagasse mais. Dentro do acampamento da guarda estava Sulpiciano, sogro do morto, que "
            "começou a fazer ofertas. Didio Juliano, cônsul anos antes, chegou depois e, como não o deixaram "
            "entrar, gritava as suas de fora. Depois de horas de disputa, Sulpiciano prometeu 20 mil sestércios a "
            "cada soldado, e Juliano, com medo de perder, subiu para 25 mil. Os guardas abriram os portões e o "
            "aclamaram, e o Senado, sob ameaça dos militares, confirmou. Ter comprado o cargo o tornou "
            "profundamente impopular: em público, era recebido com gritos de \"ladrão\" e \"parricida\", e uma "
            "multidão chegou a apedrejá-lo. Três generais se rebelaram, e o mais próximo de Roma, Septímio Severo, "
            "marchou sobre a capital. Abandonado pelo Senado e pela própria guarda, Juliano foi morto no palácio "
            "por um soldado em 2 de junho. Segundo o historiador Cássio Dio, que viveu na época, suas últimas "
            "palavras foram: \"Mas que mal eu fiz? Quem eu matei?\". Severo dissolveu a Guarda Pretoriana e executou "
            "os assassinos de Pertinax."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Didius_Julianus",
            "He is known for having purchased the title of emperor in an auction run by the Praetorian Guard. [...] "
            "He was appointed to the consulship in 175 along with Pertinax as a reward [...] "
            "After the murder of Pertinax on 28 March 193, the Praetorian guard announced that the throne was to be sold to the man who would pay the highest price. "
            "Titus Flavius Claudius Sulpicianus, prefect of Rome and Pertinax's father-in-law, who was in the Praetorian camp ostensibly to calm the troops, began making offers for the throne. "
            "Meanwhile, Julianus also arrived at the camp, and since his entrance was barred, shouted out offers to the guard. "
            "After hours of bidding, Sulpicianus promised 20,000 sesterces to every soldier; Julianus, fearing that Sulpicianus would gain the throne, then offered 25,000. "
            "The guards closed with the offer of Julianus, threw open the gates, and proclaimed him emperor. "
            "Threatened by the military, the Senate also declared him emperor. [...] "
            "Because Julianus bought his position rather than acquiring it conventionally through succession or conquest, he was a deeply unpopular emperor. "
            "When Julianus appeared in public, he frequently was greeted with groans and shouts of \"robber and parricide\". "
            "Once, a mob even obstructed his progress to the Capitol by pelting him with large stones. [...] "
            "Julianus declared Severus a public enemy because he was the nearest of the three to Rome [...] "
            "Abandoned by the Senate and the Praetorian Guard, Julianus was killed by a soldier in the palace and succeeded by Severus. [...] "
            "Julianus was killed in the palace by a soldier on 2 June 193 AD, after a mere 66 days of ruling.  "
            "According to the contemporary Roman historian Cassius Dio, Julianus' last words were: \"But what evil have I done? Whom have I killed?\" [...] "
            "Severus dismissed the Praetorian Guard and executed the soldiers who had killed Pertinax",
            nome="Didius Julianus")],
    },
    # 5 Diocleciano, os repolhos e o mausoléu que virou catedral
    {
        "temas_secundarios": ["religioes", "cidades", "arquitetura"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Diocleciano, o primeiro imperador romano a renunciar por vontade própria, plantou repolhos num palácio que hoje é meia cidade velha de Split. Seu mausoléu virou catedral, com relíquias de um bispo que ele mandou matar.",
        "explicacao": (
            "Diocleciano governou de 284 a 305 e comandou a última, maior e mais sangrenta perseguição oficial aos "
            "cristãos no Império. Enfraquecido pela doença, deixou o cargo em 1º de maio de 305, e o historiador "
            "A. H. M. Jones chegou a dizer que talvez sua maior façanha tenha sido reinar vinte e um anos e depois sair por "
            "vontade própria. Ele se retirou para um palácio fortificado na costa da Dalmácia, perto de onde "
            "nascera, e passava os dias nos jardins. Quando lhe pediram que voltasse ao trono para resolver as "
            "brigas entre os sucessores, respondeu que, se vissem os repolhos que tinha plantado com as próprias "
            "mãos, jamais pensariam em pedir aquilo. O palácio ganhou depois uma segunda vida. No século VII, a "
            "cidade vizinha de Salona foi destruída por ávaros e eslavos, refugiados se abrigaram atrás das "
            "muralhas, e o lugar nunca mais deixou de ser habitado: hoje forma cerca de metade da cidade velha de "
            "Split, na Croácia, com uns 3 mil moradores. Em meados do século VII, o mausoléu do imperador foi "
            "convertido em catedral, e lá foram postas as relíquias de São Domnio, bispo de Salona decapitado em "
            "304 durante as perseguições de Diocleciano."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Diocletian",
                "was Roman emperor from 284 until his abdication in 305. [...] "
                "The Diocletianic Persecution (303–312), the empire's last, largest, and bloodiest official persecution of Christianity [...] "
                "Weakened by illness, Diocletian left the imperial office on 1 May 305, becoming the first Roman emperor to abdicate the position voluntarily. "
                "He lived out his retirement in his palace on the Dalmatian coast, tending to his vegetable gardens. [...] "
                "At Carnuntum people begged Diocletian to return to the throne, to resolve the conflicts that had arisen through Constantine's rise to power and Maxentius's usurpation. "
                "Diocletian's reply: \"If you could see the cabbages I have planted here with my own hands, you surely would never have thought to request this.\" "
                "Diocletian lived for four more years, spending his days in his palace gardens. [...] "
                "The historian A.H.M. Jones observed that \"It is perhaps Diocletian's greatest achievement that he reigned twenty-one years and then abdicated voluntarily, and spent the remaining years of his life in peaceful retirement.\" [...] "
                "Diocletian retired to his homeland, Dalmatia. He moved into the expansive Diocletian's Palace, a heavily fortified compound",
                nome="Diocletian"),
            wiki("Diocletian%27s_Palace",
                "Today the palace forms about half of the old town of Split, with 3,000 inhabitants [...] "
                "Its second life came when Salona was largely destroyed in the invasions of the Avars and Slavs in the 7th century [...] "
                "Part of the expelled population, now refugees, found shelter inside the palace's strong walls and with them a new, organized city life began. "
                "Since then, the palace has been continuously occupied",
                nome="Diocletian's Palace"),
            wiki("Cathedral_of_Saint_Domnius",
                "Saint Domnius was martyred with seven other Christians in the persecutions of the Emperor Diocletian. "
                "He was born in Antioch, in modern-day Turkey, and beheaded in 304 at Salona. [...] "
                "The mausoleum of an emperor once known for persecuting Christians was transformed in the mid-7th century into a cathedral, where altars with the relics of Saint Domnius and Saint Anastasius—martyrs executed in nearby Salona—were placed in positions of honor.",
                nome="Cathedral of Saint Domnius"),
        ],
    },
    # 6 Crasso e as casas em chamas
    {
        "temas_secundarios": ["economia_curiosa", "cidades"],
        "tipos_espanto": ["historia_humana", "mito_desmentido"],
        "gancho": "Em Roma, onde incêndios e desabamentos eram comuns, Crasso juntou mais de 500 escravos construtores e comprava por uma ninharia casas em chamas e as vizinhas. Assim, diz Plutarco, ficou dono de boa parte da cidade.",
        "explicacao": (
            "Marco Licínio Crasso, aliado de Júlio César, ficou conhecido como \"o homem mais rico de Roma\". Na "
            "biografia que escreveu sobre ele, Plutarco conta um dos métodos. Crasso percebeu como eram frequentes, na cidade, "
            "os incêndios e os desabamentos, porque os prédios eram pesados demais e colados uns aos outros. "
            "Passou então a comprar escravos que fossem arquitetos e construtores. Quando já tinha mais de 500, "
            "comprava casas que estavam pegando fogo, e também as vizinhas, que os donos, com medo e sem saber o "
            "que viria, entregavam por um preço irrisório. Segundo Plutarco, foi assim que a maior parte de Roma "
            "passou às mãos dele. O mesmo autor diz que a fortuna de Crasso foi de menos de 300 para 7.100 "
            "talentos, boa parte obtida \"pelo fogo e pela guerra\", fazendo das calamidades públicas sua maior "
            "fonte de renda. Uma versão mais dramática, que circula até hoje, diz que Crasso montou a primeira "
            "brigada de incêndio de Roma, com 500 homens que só apagavam o fogo se o dono aceitasse vender a casa. "
            "O trecho de Plutarco, porém, não fala em brigada nem em fogo deixado de propósito: fala de "
            "construtores, de casas compradas em chamas e de donos assustados."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Lives/Crassus*.html",
             "titulo": "Plutarch, Life of Crassus (tradução de Bernadotte Perrin, Loeb, em LacusCurtius)",
             "idioma": "en",
             "trecho": "observing how natural and familiar at Rome were such fatalities as the conflagration and collapse of buildings, owing to their being too massive and close together, he proceeded to buy slaves who were architects and builders. "
                       "Then, when he had over five hundred of these, he would buy houses that were afire, and houses which adjoined those that were afire, and these their owners would let go at a trifling price owing to their fear and uncertainty. "
                       "In this way the largest part of Rome came into his possession."},
            wiki("Marcus_Licinius_Crassus",
                "Often called \"the richest man in Rome\" [...] "
                "A political and financial patron of Julius Caesar [...] "
                "says the wealth of Crassus increased from less than 300 talents at first, to 7,100 talents. [...] "
                "most of which Plutarch declares Crassus got \"by fire and war, making the public calamities his greatest source of revenue.\" [...] "
                "The first ever Roman fire brigade was created by Crassus. "
                "Fires were almost a daily occurrence in Rome, and Crassus took advantage of the fact that Rome had no fire department by creating his own brigade—500 men strong—which rushed to burning buildings at the first cry of alarm. [...] "
                "If the owner agreed to sell the property, his men would put out the fire; if the owner refused, then they would simply let the structure burn to the ground.",
                nome="Marcus Licinius Crassus"),
        ],
    },
    # 7 a Floresta de Teutoburgo que não é a da batalha
    {
        "temas_secundarios": ["nomes_lugares", "fronteiras_paises"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "A Floresta de Teutoburgo, na Alemanha, ganhou o nome no século XIX por uma teoria sobre onde Roma perdeu três legiões. O local provável da luta só foi achado em 1987, a 100 km dali, por um amador com detector de metais.",
        "explicacao": (
            "Em setembro do ano 9, uma aliança de povos germânicos emboscou três legiões romanas comandadas por "
            "Públio Quintílio Varo. O líder era Armínio, chefe germânico e oficial das tropas auxiliares do próprio "
            "Varo. Levado pelos romanos como refém aos 10 anos, mais ou menos, ele recebeu em Roma educação "
            "aristocrática, cidadania e formação militar, e por isso sabia antecipar as reações romanas. As baixas "
            "de Roma são estimadas entre 15 mil e 20 mil mortos. Segundo Suetônio, Augusto ficou tão abalado que "
            "batia a cabeça nas paredes gritando \"Quintílio Varo, devolva minhas legiões!\", e os números das três, "
            "XVII, XVIII e XIX, nunca mais foram usados. Onde tudo aconteceu virou um enigma. No século XIX, uma "
            "teoria venceu o debate, e uma serra chamada Osning, perto de Bielefeld, foi rebatizada de Floresta de "
            "Teutoburgo. Em 1987, o major britânico Tony Clunn, procurando por hobby \"uma ou outra moeda romana\", "
            "achou na colina de Kalkriese moedas da época de Augusto, nenhuma posterior, e projéteis romanos de "
            "funda feitos de chumbo. As pesquisas seguintes acharam ali 6 mil peças de equipamento romano. "
            "Kalkriese, a uns 100 km da serra rebatizada, já tinha sido sugerida no século XIX pelo historiador "
            "Theodor Mommsen."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Battle_of_the_Teutoburg_Forest",
            "was a major battle fought between an alliance of Germanic peoples and the Roman Empire between 8 and 11 September 9 AD, possibly near modern Kalkriese. "
            "Fighting began with an ambush by the Germanic alliance on three Roman legions being led by Publius Quinctilius Varus and their auxiliaries; "
            "the alliance was led by Arminius, a Germanic chieftain and officer of Varus's auxilia. "
            "Arminius had received Roman citizenship and a Roman military education, thus allowing him to deceive the Romans methodically and anticipate their tactical responses. [...] "
            "he had been taken hostage by the Romans after Drusus defeated the tribe in combat in 8 BCE, when Arminius would have been about 10 years old. "
            "He received an aristocratic education in Rome [...] "
            "Roman casualties have been estimated at 15,000–20,000 dead [...] "
            "and the finds at Kalkriese of 6,000 pieces of Roman equipment [...] "
            "Upon hearing of the defeat, the Emperor Augustus, according to the Roman historian Suetonius in The Twelve Caesars, was so shaken that he stood butting his head against the walls of his palace, repeatedly shouting:  "
            "Quintili Vare, legiones redde! (Quintilius Varus, give me back my legions!) "
            "The legion numbers XVII, XVIII and XIX were not used again by the Romans. [...] "
            "During the 19th century, theories as to the site abounded, and the followers of one theory successfully argued for a long wooded ridge called the Osning, near Bielefeld. "
            "This was then renamed the Teutoburg Forest. "
            "Late 20th-century research and excavations were sparked by finds in 1987 by a British amateur archaeologist, Major Tony Clunn, who was casually prospecting at Kalkriese Hill [...] "
            "with a metal detector in the hope of finding \"the odd Roman coin\". "
            "He discovered coins from the reign of Augustus (and none later), and some ovoid leaden Roman sling bolts. [...] "
            "This site, some 100 kilometres (62 mi) north west of Osning, was first suggested by the 19th-century historian Theodor Mommsen",
            nome="Battle of the Teutoburg Forest")],
    },
    # 8 as tabuinhas de Vindolanda
    {
        "temas_secundarios": ["sistemas_escrita", "bebidas_alcoolicas", "costumes_rituais"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Num forte romano no norte da Inglaterra, plaquinhas de madeira achadas em 1973 pareciam aparas sem valor. Eram cartas: há até um pedido de mais cerveja para a tropa e um convite de aniversário assinado por uma mulher.",
        "explicacao": (
            "As tabuinhas de Vindolanda são folhas finas de madeira local, do tamanho de um cartão-postal, escritas "
            "com tinta de carbono e dobradas ao meio. Até então, nunca se tinham achado tabuinhas romanas de "
            "madeira escritas a tinta. Em março de 1973, foram tomadas por aparas de madeira até que um escavador "
            "achou duas grudadas, separou-as e viu a escrita do lado de dentro. Em contato com o ar, a madeira "
            "escureceu, e só fotos em infravermelho trouxeram as letras de volta, numa cursiva que ainda precisou "
            "ser decifrada. A maioria é de antes de 105, um pouco mais antiga que a Muralha de Adriano, e hoje já "
            "passam de 1.700. Há de tudo: um decurião de cavalaria pede ao comandante instruções para o dia "
            "seguinte e mais cerveja, porque a guarnição tinha acabado com o estoque; uma tabuinha confirma que os "
            "soldados usavam cueca; outra revela como os romanos chamavam os bretões da região, Brittunculi, "
            "\"bretõezinhos\", um termo de desprezo. A mais famosa, de por volta do ano 100, é o convite de Claudia "
            "Severa, mulher do comandante de um forte vizinho, para Sulpicia Lepidina ir à sua festa de "
            "aniversário. A maior parte foi escrita por um escriba, mas as saudações finais saíram da mão da "
            "própria Claudia, num dos mais antigos textos em latim escritos por uma mulher que se conhecem."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Vindolanda_tablets",
            "Written on fragments of thin, postcard-sized wooden leaf-tablets with carbon-based ink, the tablets date to the 1st and 2nd centuries AD (roughly contemporary with Hadrian's Wall).  "
            "Although similar records on papyrus were known from elsewhere in the Roman Empire, wooden tablets with ink text had not been recovered until 1973 [...] "
            "at the site of Vindolanda, a Roman fort in northern England. [...] "
            "As of 2023, more than 1,700 tablets have been discovered. [...] "
            "The Vindolanda tablets are made from birch, alder and oak that grew locally [...] "
            "They were scored down the middle and folded to form diptychs with ink writing on the inner faces [...] "
            "First discovered in March 1973, the tablets were initially thought to be wood shavings until one of the excavators found two stuck together and peeled them apart to discover writing on the inside. [...] "
            "but rapid oxygenation of the wood meant that they were black and unreadable by the time he was able to view them. [...] "
            "which led to infrared photographs showing the scripts for researchers for the first time. [...] "
            "analysed the previously unknown form of cursive script and were able to produce transcriptions. [...] "
            "The tablets were produced in periods 2 and 3 (c. 95–105), with the majority written before 105. [...] "
            "the cavalry decurion Masculus wrote a letter to prefect Flavius Cerialis inquiring about the instructions for his men for the following day, including a polite request for more beer to be sent to the garrison (which had entirely consumed its previous stock of beer). [...] "
            "One of the tablets confirms that Roman soldiers wore underpants (subligaculum) [...] "
            "The best-known document is perhaps Tablet 291, written around 100 by Claudia Severa, the wife of the commander of a nearby fort, to Sulpicia Lepidina, inviting her to a birthday party. "
            "The invitation is one of the earliest known examples of writing in Latin by a woman. "
            "There are two handwriting styles in the tablet, with the majority of the text written in a professional hand (thought to be the household scribe) and with closing greetings personally added by Claudia Severa [...] "
            "Brittunculi (diminutive of Britto; hence 'little Britons'), found on one of the Vindolanda tablets, is now known to be a derogatory, or patronising, term",
            nome="Vindolanda tablets")],
    },
    # 9 o dodecaedro romano
    {
        "temas_secundarios": ["geometria_topologia", "crimes_arte"],
        "tipos_espanto": ["misterio_aberto", "engenhosidade"],
        "gancho": "Desde 1739, já foram achados mais de cem dodecaedros romanos de bronze, ocos, com um furo em cada face e bolinhas nos cantos. Há mais de cinquenta explicações publicadas para o que eles eram, e ninguém sabe.",
        "explicacao": (
            "São peças de liga de cobre fundidas pela técnica da cera perdida: doze faces pentagonais, cada uma com "
            "um furo redondo de tamanho diferente, e uma bolinha de metal em cada vértice. Medem de 4 a 11 "
            "centímetros e pesam de 35 gramas a 1 quilo. Datam dos séculos II a IV e foram feitas sobretudo na "
            "Gália. Aparecem na Grã-Bretanha, na França, na Alemanha e em outros países da Europa, mas não no "
            "coração do Império, a Itália. Quase não mostram desgaste e não trazem letras nem números. Como nenhum "
            "texto ou imagem da época as menciona, sobram hipóteses: instrumento para estimar distâncias, peça de "
            "tricô para fazer luvas, brinquedo, objeto de adivinhação, gabarito para checar se moedas tinham o "
            "diâmetro certo e não tinham sido raspadas, ou prova de habilidade de um artesão do metal. Todas têm "
            "problemas. Não há marcas que indiquem um instrumento de medida, o primeiro registro conhecido do "
            "tricô em carretel é de 1535, e, para servir de arma, elas são leves demais. Algumas apareceram em "
            "tesouros de moedas, sinal de que os donos as consideravam valiosas. Em 2023, arqueólogos amadores "
            "acharam mais uma, em ótimo estado, num vilarejo de Lincolnshire, na Inglaterra."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Roman_dodecahedron",
            "A Roman dodecahedron or Gallo-Roman dodecahedron is a type of small hollow object made of copper alloy that has been cast into a regular dodecahedral shape with twelve flat pentagonal faces. "
            "Each face has a circular hole of varying diameter in the middle, the holes connecting to the hollow center, and each corner has a protruding knob. "
            "They rarely show signs of wear and do not have any inscribed numbers or letters. "
            "Since the first known example was recorded in 1739, over one hundred such objects have been discovered, dating from the 2nd to the 4th centuries AD. "
            "Their purpose or meaning has been long debated but remains unknown. [...] "
            "The dodecahedra vary in size from 4–11 cm (1.6–4.3 inches) [...] "
            "The lightest known example weighs 35 g (1.2 ounces); the heaviest 1 kg (2.2 pounds). "
            "The dodecahedra are cast using the lost wax technique. [...] "
            "about 130 similar objects have been found in Austria, Belgium, France, Germany, Hungary, Luxembourg, the Netherlands, Switzerland, and the United Kingdom, but not in the Roman heartland in Italy. [...] "
            "In 2023, a dodecahedron in excellent condition was found by amateur archeologists in the small village of Norton Disney in Lincolnshire, UK [...] "
            "They were mostly made in Gaul between the second and fourth centuries AD. [...] "
            "more than fifty possible explanations have been published. "
            "Identifying their purpose with certainty is made more difficult as no mention of dodecahedra has been found in contemporary accounts or pictures. "
            "Speculative uses include as a survey instrument for estimating distances to (or sizes of) distant objects, though this is questioned, as there are no markings to indicate that they would be a mathematical instrument; "
            "as spool knitting devices for making gloves (though the earliest known reference to spool knitting is from 1535 [...] "
            "or as part of a child's toy. [...] "
            "It has been suggested that they might have been fortune-telling devices. [...] "
            "Several dodecahedra were found in coin hoards, suggesting either that their owners considered them valuable objects, or that their use was connected with coins—as, for example, for easily checking that coins fit a certain diameter and were not clipped. "
            "It has also been suggested that they might have been an object to test the skill of a metalsmith [...] "
            "but other scholars have suggested that the dodecahedra are too light to make an effective weapon.",
            nome="Roman dodecahedron")],
    },
    # 10 a Lex Oppia e o protesto das romanas
    {
        "temas_secundarios": ["leis_julgamentos", "moda"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 195 a.C., mulheres romanas bloquearam as ruas e os acessos ao Fórum para derrubar uma lei que limitava seu ouro e suas roupas. No dia seguinte, cercaram as portas dos tribunos que a defendiam. E a lei caiu.",
        "explicacao": (
            "A Lex Oppia foi criada em 215 a.C., no auge da Segunda Guerra Púnica, logo depois da derrota "
            "catastrófica de Canas. Proibia qualquer mulher de ter mais de meia onça de ouro, de vestir roupas de "
            "várias cores, sobretudo as debruadas de púrpura, e de andar em veículo puxado por animais na cidade, "
            "salvo em festas religiosas públicas. Era antes de tudo uma medida econômica de guerra. Vencida "
            "Cartago, a riqueza das conquistas começou a fluir para Roma, e dois tribunos da plebe propuseram "
            "revogar a lei. O cônsul Catão, o Velho, a defendeu: disse que o desejo das mulheres de gastar era uma "
            "doença que não se cura, apenas se contém. Do outro lado, Lúcio Valério lembrou que a lei fora uma "
            "medida temporária de emergência e provocou os homens: o cavalo deles andava mais enfeitado do que as "
            "esposas. Segundo o historiador Tito Lívio, nem a autoridade dos magistrados nem as ordens dos maridos "
            "conseguiram manter as matronas em casa. Elas lotaram o Capitólio, bloquearam as ruas e imploraram aos "
            "homens que desciam ao Fórum. No dia seguinte, voltaram em número ainda maior e cercaram as portas dos "
            "dois tribunos chamados Bruto, que apoiavam a lei. Eles cederam, e a Lex Oppia foi revogada."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Lex_Oppia",
            "The Lex Oppia was a law established in ancient Rome in 215 BC, at the height of the Second Punic War during the days of national catastrophe after the Battle of Cannae, and repealed in 195 BC. [...] "
            "Specifically, it forbade any woman to possess more than half an ounce of gold, to wear a multi-colored garment (particularly those trimmed in purple), or to ride in an animal-drawn vehicle in the city or any town or within a mile thereof, except in the case of public religious festivals. [...] "
            "The Lex Oppia had been primarily an economic measure in response to serious financial issues during the Second Punic War. [...] "
            "Following the Second Punic War, with Rome victorious over Carthage, wealth from the conquered areas began to flow into the hands of the Roman ruling class [...] "
            "Consequently, two tribunes of the plebs, Marcus Fundanius and Lucius Valerius, proposed repealing the Lex Oppia. "
            "The supporters of the Lex Oppia were led by two tribunes of the plebs, Marcus Junius Brutus and Publius Junius Brutus, and consul Marcus Porcius Cato, also known as Cato the Elder [...] "
            "He also declared that a woman's desire to spend money was a disease that could not be cured, but only restrained [...] "
            "Lucius Valerius Flaccus had further argued that the Lex Oppia was only an emergency temporary law passed after the disastrous defeat of Roman soldiers in Cannae by Hannibal. [...] "
            "Even your horse will be more beautifully arrayed than your wife is clothed. [...] "
            "As nobles spoke for or against the repeal of the Lex Oppia, the matrons of Rome crowded the Capitol. "
            "As Livy writes, the women could not be kept indoors by either the authority of the magistrates or the orders of their husbands or their own sense of propriety [...] "
            "They blocked all the streets of the city and the approaches to the Forum, and implored the men as they descended to the Forum to allow the women to resume their former adornments.  "
            "After the speeches against and in favor of the Lex Oppia, the women poured into the streets the next day in greater numbers and besieged the doors of the two Brutuses.  "
            "The dissenting tribunes eventually gave in to the persistent demanding of the Roman matrons, and the Lex Oppia was repealed in 195 BC.",
            nome="Lex Oppia")],
    },
    # 11 em que dia o Vesúvio entrou em erupção?
    {
        "temas_secundarios": ["vulcoes_terremotos", "calendarios"],
        "tipos_espanto": ["misterio_aberto", "mito_desmentido"],
        "gancho": "Por séculos se ensinou que o Vesúvio soterrou Pompeia em 24 de agosto de 79. Frutas de outono, roupas pesadas e uma inscrição a carvão achada em 2018 apontam para outubro. A data ainda está em disputa.",
        "explicacao": (
            "O 24 de agosto vem de uma carta de Plínio, o Jovem, ao historiador Tácito. Plínio viu a erupção e "
            "deixou o único relato de testemunha ocular que se conhece. Mas não há nenhuma cópia romana da carta: "
            "ela passou por catorze séculos de cópias à mão até ser impressa em 1508, e a data pode ter se "
            "corrompido no caminho. Por causa do jeito romano de escrever as datas, especialistas em manuscritos "
            "acham que o original dizia 24 de agosto, 30 de outubro, 1º de novembro ou 23 de novembro. A grande "
            "maioria das cópias medievais traz o equivalente a 24 de agosto. Desde o fim do século XVIII, porém, "
            "uma minoria de pesquisadores desconfia. Escavações acharam restos de frutas de outono, como romãs, "
            "vítimas com roupas pesadas e grandes jarros cheios de vinho, sinal de que a uva já tinha sido colhida. "
            "Um estudo de 2007 mostrou que o rastro das cinzas, para o sudeste, combina com os ventos do outono, e "
            "não com os de junho a agosto, que sopram quase sempre para o oeste. Em 2018, numa casa em reforma, "
            "arqueólogos acharam uma inscrição a carvão com a data de 17 de outubro, provavelmente deixada por um "
            "trabalhador. Ela não traz o ano, e um teste mostrou que esse tipo de inscrição pode durar mais de um "
            "ano. Um estudo de 2022 propôs o fim de outubro, e também foi contestado."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Eruption_of_Mount_Vesuvius_in_79_AD",
            "For more than five centuries, until approximately 2018, articles about the eruption of Vesuvius typically stated that the eruption began on August 24, 79 AD. "
            "This date came from a 1508 printed copy of a letter addressed by Pliny the Younger to the Roman historian Tacitus [...] "
            "Pliny was a witness to the eruption and provided the only known eyewitness account. "
            "Over fourteen centuries of manuscript hand-copying up to the 1508 printing of his letters, the date given in Pliny's original letter may have been corrupted. "
            "Manuscript experts believe that the date originally given by Pliny was one of August 24, October 30, November 1, or November 23. "
            "This odd scattered set of dates is due to the Romans' convention for describing calendar dates. "
            "The large majority of extant medieval manuscript copies (there are no surviving Roman copies) indicate a date corresponding to August 24. [...] "
            "Since at least the late 18th century, a minority among archaeologists and other scientists have suggested that the eruption began after August 24, during the autumn, perhaps in October or November. [...] "
            "More recently, in 1990 and 2001, archaeologists discovered more remnants of autumnal fruits (such as the pomegranate), the remains of victims of the eruption in heavy clothing, and large earthenware storage vessels laden with wine (at the time of their burial by Vesuvius). "
            "The wine-related discovery suggests that the eruption might have happened after the grape harvest. "
            "In 2007, a study of prevailing winds in Campania showed that the southeasterly debris pattern of the first-century eruption is quite consistent with an autumn event and inconsistent with an August date. "
            "During June, July, and August, the prevailing winds flow to the west [...] "
            "In October 2018, Italian archaeologists uncovered a charcoal inscription reading \"the 16th day before the calends (first) of November,\" or October 17, that was probably \"made by a worker renovating a home\" [...] "
            "While the \"graffito does not have a year listed [...] "
            "a study by the Pompeii Archeological Park showed that charcoal graffiti can last for more than a year at the site of the discovered ancient graffito, casting doubt on whether the October date was in 79 AD. "
            "A collaborative study in 2022 has determined a date of \"between October 24th and November 1st\" for the eruption in 79 AD. "
            "This conclusion has been challenged.",
            nome="Eruption of Mount Vesuvius in 79 AD")],
    },
    # 12 o rosto raspado no Tondo Severiano
    {
        "temas_secundarios": ["pintura", "crimes_arte"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Num retrato de família pintado por volta do ano 200, o imperador Septímio Severo, a mulher e os dois filhos aparecem juntos. Um rosto foi raspado: segundo a maioria dos estudiosos, o de Geta, morto a mando do irmão.",
        "explicacao": (
            "O Tondo Severiano é um painel de madeira redondo, de 30,5 centímetros de diâmetro, pintado com tinta "
            "à base de ovo e ligado ao estilo dos retratos de múmia do Fayum, no Egito. Mostra Septímio Severo, "
            "Júlia Domna e os filhos Caracala e Geta, todos com coroas de ouro. Depois da morte de Severo, em 211, "
            "os irmãos deveriam governar juntos, mas em dezembro daquele mesmo ano Caracala mandou matar Geta. O "
            "Senado então condenou oficialmente a memória do morto, a chamada damnatio memoriae: imagens de Geta foram "
            "removidas e desfiguradas pelo Império inteiro, e o nome e o título dele foram apagados das "
            "inscrições. Fontes antigas registram que essas imagens eram besuntadas de lama, vísceras, tinta e até "
            "excremento, e o tondo é uma das raras obras sobreviventes que mostram uma desfiguração desse tipo. "
            "Ele revela ainda que a prática não ficava nos monumentos públicos: chegava a objetos privados. Para "
            "o dono, raspar o rosto era um jeito de continuar exibindo o retrato e, ao mesmo tempo, provar lealdade "
            "ao novo imperador. Há uma ressalva: se Geta, o filho mais novo, for o menino menor, o rosto apagado "
            "seria o de Caracala, talvez numa retaliação posterior. A maioria, porém, aposta em Geta."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Severan_Tondo",
            "The Severan Tondo or Berlin Tondo is a circular wooden panel portraying the Roman emperor Septimius Severus (r. 193–211) with his wife, the augusta Julia Domna, and their two sons and co-augusti Caracalla (r. 198–217) and Geta [...] "
            "The face of Geta, one of the two brothers, has been deliberately erased in connection with his damnatio memoriae [...] "
            "The Severan Tondo is one of the few preserved examples of panel painting from classical antiquity to attest to the deliberate manipulation of a portrait for the purpose of dishonoring an individual. [...] "
            "The dating of the piece has caused some debate among scholars, with the final consensus being c. 200 AD. "
            "The tondo has many stylistic connections to Fayum Mummy portraiture [...] "
            "The work is a tempera, or egg-based painting, on a tondo, with a diameter of 30.5 centimetres (12.0 in). "
            "It portrays the Imperial family wearing gold wreaths [...] "
            "Most scholars believe it is Septimius's son Geta whose face has been removed through a deliberate act of iconoclasm, most likely after his murder by Caracalla's Praetorian Guard and the ensuing damnatio memoriae. "
            "However, it is also possible that Geta (as the younger son) is the smaller boy, and it is Caracalla's face which was eradicated, perhaps as a compensatory retaliation [...] "
            "After Severus's death in February of 211, the empire was supposed to be jointly ruled by his sons, Caracalla and Geta.  "
            "In December that year, Caracalla had Geta murdered [...] "
            "After his murder, Geta was subjected to damnatio memoriae. In this official action, the Senate declared against his memory. "
            "This led to great removal, defacement, and erasure of Geta throughout the entire Roman empire. [...] "
            "the act of smearing mud, offal, paint or even excrement was recorded as a practice in ancient sources. [...] "
            "By removing Geta's figure from the tondo, the owner would be able to continue to support the new emperor, Caracalla [...] "
            "This display of damnatio memoriae of Geta's image shows that this practice of defacement did not only occur on public monuments and artworks, but in private settings as well. "
            "Geta's name and title, along with his image, were erased from almost every inscription pertaining to him.",
            nome="Severan Tondo")],
    },
    # 13 "alea iacta est" foi dito em grego?
    {
        "temas_secundarios": ["expressoes", "teatro_danca", "grecia_antiga"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "Ao cruzar o Rubicão e começar uma guerra civil, César talvez nem tenha dito \"alea iacta est\" em latim. Segundo Plutarco, ele gritou em grego \"que se lance o dado\", frase que provavelmente vem de uma comédia de Menandro.",
        "explicacao": (
            "Em 10 de janeiro de 49 a.C., César atravessou com seus soldados o Rubicão, rio que marcava o limite "
            "da província que governava. Fazer isso era desafiar uma ordem direta do Senado e começar uma guerra "
            "civil. A frase do momento chegou até nós por três autores que escreveram muito depois. Suetônio, em "
            "latim, registra \"iacta alea est\", \"o dado está lançado\", uma constatação de que o rumo já estava "
            "decidido. Plutarco, que escreveu em grego mais de um século depois, afirma com todas as letras que "
            "César falou em grego, em voz alta: \"anerrhíphthō kýbos\", algo como \"que se lance um dado\", que soa "
            "mais como um incentivo para arriscar. Apiano, também em grego, traz uma frase muito parecida e diz que "
            "ela já era conhecida. A origem provável é a comédia Arrephoros, de Menandro, perdida: sobrou só um "
            "diálogo citado por outro autor, Ateneu, em que a expressão se refere a um casamento já combinado, mas "
            "ainda não realizado. César falava grego fluentemente e considerava Menandro um grande dramaturgo. A "
            "forma mais repetida hoje, \"alea iacta est\", é a de Suetônio, com a ordem das palavras trocada."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Alea_iacta_est",
            "It is a variation of the words spoken by Julius Caesar at the crossing of the Rubicon on 10 January 49 BC. [...] "
            "The Rubicon river in northern Italy marked the southern boundary of Caesar's province of Cisalpine Gaul [...] "
            "By leading his soldiers across the river, Caesar was defying a direct order from the Roman Senate and beginning a civil war. "
            "The ancient historian Suetonius reports that Caesar actually said iacta alea est [...] "
            "Plutarch states that Caesar was speaking in Greek [...] "
            "literally \"let a die be cast\", metaphorically \"let the game be played\". "
            "Suetonius's Latin version is a statement about the inevitability of what is to come, while the Greek version contains a self-encouragement to venture forward. "
            "The Greek version is probably a quotation from a play by Menander [...] "
            "The Latin version is the most commonly cited in modern sources, but with the word order changed to alea iacta est. [...] "
            "The phrase probably originated with the ancient Greek playwright Menander, in his comedic play [...] "
            "The full text of that play has been lost, but a short dialogue from it has been preserved in quotation by Athenaeus. "
            "The dialogue uses the phrase to refer to a marriage that has been agreed but not yet performed. "
            "Caesar was fluent in Greek and considered Menander a great playwright. "
            "The crossing of the Rubicon is described by Plutarch in Parallel Lives, written in Greek over a century after the events. "
            "He explicitly reports that Caesar spoke in Greek, but does not mention Menander: [...] "
            "He [Caesar] declared in Greek with loud voice to those who were present \"Let a die be cast\" and led the army across. "
            "Appian wrote a history of Caesar's civil war, also in Greek around the same time as Plutarch was writing. "
            "He reports a very similar phrase and asserts that it was already well-known.",
            nome="Alea iacta est")],
    },
    # 14 a cesariana não vem do nascimento de César
    {
        "temas_secundarios": ["historia_medicina", "palavras_portugues"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "A cesariana não deve o nome a um parto de Júlio César. Na Roma antiga, a operação era, ao que tudo indica, sempre fatal para a mãe, e a mãe de César viveu quase 50 anos depois de dar à luz.",
        "explicacao": (
            "A ideia de que César nasceu por cesariana e batizou a cirurgia é popular, mas não se sustenta. Até a "
            "era moderna, a operação parece ter sido invariavelmente fatal para a mãe, e nenhuma fonte clássica "
            "registra uma mulher que tenha sobrevivido a ela. Já Aurélia, mãe de César, não só sobreviveu ao parto "
            "como viveu por quase 50 anos. Na Roma antiga, uma lei atribuída ao rei Numa Pompílio mandava retirar "
            "do ventre o bebê de uma mulher morta no parto. E, se a mãe estava viva, a prática romana exigia que "
            "ela estivesse no décimo mês de gestação, sinal de que se sabia que ela não sobreviveria. A origem do "
            "nome continua incerta. Uma explicação o liga ao verbo latino caedere, \"cortar\", e os bebês nascidos "
            "assim seriam chamados caesones. Plínio, o Velho, dizia que o sobrenome Caesar vinha de um antepassado "
            "de César \"cortado do ventre\", e essa é uma das raízes possíveis da confusão. O mito, porém, durou "
            "muito: a primeira e a segunda edições do dicionário Oxford de inglês, de 1888 e 1989, afirmavam que "
            "a operação tinha sido feita no caso de Júlio César."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Caesarean_section",
            "A popular idea is that the Roman statesman Julius Caesar was born via caesarean section and is the namesake of the procedure, but if this is the true etymology, it is probably based on a misconception: "
            "until the modern era, C-sections seem to have been invariably fatal to the mother, and Caesar's mother Aurelia not only survived her son's birth but lived for nearly 50 years afterward. [...] "
            "Roman Lex Regia (royal law), later the Lex Caesarea (imperial law), of Numa Pompilius (715–673 BC), required the child of a mother who had died during childbirth to be cut from her womb. [...] "
            "Roman practice required a living mother to be in her tenth month of pregnancy before resorting to the procedure, reflecting the knowledge that she could not survive the delivery. "
            "Speculations that the Roman dictator Julius Caesar was born by the method now known as C-section are false. "
            "Although caesarean sections were performed in Roman times, no classical source records a mother surviving such a delivery, while Caesar's mother lived for years after his birth. [...] "
            "The term has also been explained as deriving from the verb caedere, 'to cut', with children delivered this way referred to as caesones. "
            "Pliny the Elder refers to a certain Julius Caesar (an ancestor of the famous Roman statesman) as ab utero caeso, 'cut from the womb' giving this as an explanation for the cognomen Caesar which was then carried by his descendants. "
            "Nonetheless,  the false etymology has been widely repeated until recently. "
            "For example, the first (1888) and second (1989) editions of the Oxford English Dictionary say that caesarean birth \"was done in the case of Julius Cæsar\". [...] "
            "The origin of the term is not definitively known.",
            nome="Caesarean section")],
    },
    # 15 o chumbo romano no gelo do Ártico
    {
        "temas_secundarios": ["mudancas_climaticas", "agua_doce_gelo", "doencas_infecciosas"],
        "tipos_espanto": ["conexao_inesperada", "escala_absurda"],
        "gancho": "O gelo do Ártico registra o chumbo que a mineração romana soltou no ar: ele despenca nas crises e na Peste Antonina e só foi superado na Idade Média. Um estudo estima que custou aos romanos 2,5 a 3 pontos de QI.",
        "explicacao": (
            "A economia romana se apoiava na mineração e na fundição de minérios de prata e chumbo, que soltavam "
            "chumbo na atmosfera. Parte dele caiu sobre o Ártico, e os testemunhos de gelo de lá, datados com "
            "precisão de menos de um ano, guardam esse registro. A curva acompanha a história. No século I a.C., "
            "durante a crise da República, a deposição caiu quase ao nível natural. Por volta de 15 a.C., logo "
            "depois do início do Império, subiu de forma brusca e ficou alta durante a Pax Romana. Despencou com a "
            "Peste Antonina, de 165 aos anos 180, ao mesmo tempo em que o teor de prata das moedas romanas caía. "
            "Os níveis da Pax Romana só voltaram a ser superados na Idade Média, no início do segundo milênio. Um "
            "estudo de 2025 usou esse registro e modelos da atmosfera para estimar o chumbo no ar de toda a "
            "Europa romana. Para a maioria rural e pobre, essa poluição de fundo pode ter sido a principal via de "
            "exposição. Com relações tiradas da epidemiologia moderna, os autores estimaram que o chumbo no sangue "
            "de crianças pequenas subiu cerca de 2,4 microgramas por decilitro, o bastante para uma queda de 2,5 a "
            "3 pontos de QI em todo o Império. É uma estimativa feita por modelo, não uma medição em pessoas da "
            "época."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [{"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11760502/fullTextXML",
            "titulo": "Pan-European atmospheric lead pollution, enhanced blood lead levels, and cognitive decline from Roman-era mining and smelting (PNAS, 2025, via Europe PMC)",
            "idioma": "en",
            "trecho": "Issue date 2025 Jan 21. [...] "
                      "The most significant exposure for the rural, nonelite population may have been to background air pollution from silver mining and smelting that underpinned the Roman economy. "
                      "Using detailed records of Roman-era lead pollution measured in Arctic ice cores and atmospheric modeling, we show that lead emissions from these activities elevated air concentrations throughout Europe. "
                      "Based on modern epidemiological studies, this air pollution enhanced childhood blood lead levels (BLLs) by about 2.4 µg/dl leading to widespread cognitive decline including an estimated 2.5-to-3 point reduction in intelligence quotient. [...] "
                      "the most significant for the nonelite, rural majority of the population may have been through background air pollution from mining and smelting of silver and lead ores that underpinned the Roman economy. [...] "
                      "Exploiting the precise dating of the subannually resolved Arctic ice-core records [...] "
                      "Deposition declined nearly to background levels during the 1st century BCE crisis of the Roman Republic and then sharply increased starting about 15 BCE soon after the start of the Roman Empire. "
                      "The high lead fluxes that characterized the Pax Romana ended with the Antonine Plague from 165 to the 180s CE that severely affected the Roman Empire and the sustained high levels of nbPb flux during the Pax Romana were not exceeded until the High Middle Ages in the early 2nd millennium CE [...] "
                      "Especially pronounced declines in lead pollution coincided with well-documented plague outbreaks such as the Antonine Plague (165 to 180 s CE) that severely affected the ancient world, with coeval reductions in the silver content of Roman coinage"},
        ],
    },
]
