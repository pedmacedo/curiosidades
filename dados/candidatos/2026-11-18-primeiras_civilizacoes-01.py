LOTE = "2026-11-18-primeiras_civilizacoes-01"
AREA = "historia_antiga"
TEMA = "primeiras_civilizacoes"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o código de Ur-Nammu: mais antigo que Hamurabi e sem "olho por olho"
    {
        "temas_secundarios": ["leis_julgamentos", "dinheiro"],
        "tipos_espanto": ["contraintuitivo", "mito_desmentido"],
        "gancho": "O código de leis mais antigo que chegou até nós não é o de Hamurabi: é o de Ur-Nammu, três séculos mais velho. E ele não mandava \"olho por olho\": quem cegasse alguém pagava meia mina de prata.",
        "explicacao": (
            "O código leva o nome de Ur-Nammu, rei de Ur entre 2112 e 2095 a.C., embora alguns estudiosos atribuam o "
            "texto ao filho dele, Shulgi. Escrito em sumério, é o mais antigo código de leis conhecido que sobreviveu. "
            "Sabe-se que houve outros antes, como o de Urukagina, mas deles não restou o texto. O primeiro fragmento foi "
            "traduzido em 1952 por Samuel Kramer, que quase deixou a peça passar: só soube dela por uma carta de F. R. "
            "Kraus, que, quando era curador do museu de Istambul, tinha juntado dois pedaços de uma tabuinha com leis "
            "sumérias. As leis já usam o formato \"se acontecer tal crime, então tal pena\", que quase todos os códigos "
            "posteriores repetiram. A surpresa está nos ferimentos: em vez da retaliação do \"olho por olho\", princípio "
            "das leis babilônicas mais tardias, o código fixa indenizações em prata. Cegar o olho de outro homem custava "
            "meia mina; cortar-lhe o pé, dez siclos; arrancar-lhe um dente, dois siclos. Homicídio, roubo, adultério e "
            "estupro, porém, eram punidos com a morte."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Code_of_Ur-Nammu",
            "The Code of Ur-Nammu is the oldest known surviving law code. It is from Mesopotamia and is written on tablets, in the Sumerian language. [...] "
            "was translated by Samuel Kramer in 1952. [...] "
            "In all probability I would have missed the Ur-Nammu tablet altogether had it not been for an opportune letter from F. R. Kraus [...] "
            "in the course of his duties as curator in the Istanbul Museum, he had come upon two fragments of a tablet inscribed with Sumerian laws, had made a \"join\" of the two pieces [...] "
            "The preface directly credits the laws to king Ur-Nammu of Ur (2112–2095 BC). [...] "
            "Some scholars have attributed it to Ur-Nammu's son Shulgi. [...] "
            "Although it is known that earlier law-codes existed, such as the Code of Urukagina, this represents the earliest extant legal text. "
            "It is three centuries older than the Code of Hammurabi. "
            "The laws are arranged in casuistic form of IF (crime) THEN (punishment)—a pattern followed in nearly all later codes. "
            "It institutes fines of monetary compensation for bodily damage as opposed to the later lex talionis ('eye for an eye') principle of Babylonian law. "
            "However, murder, robbery, adultery and rape were capital offenses. [...] "
            "If a man knocks out the eye of another man, he shall weigh out half a mina of silver. [...] "
            "If a man has cut off another man's foot, he is to pay ten shekels. [...] "
            "If a man knocks out a tooth of another man, he shall pay two shekels of silver.",
            nome="Code of Ur-Nammu")],
    },
    # 2 "mesquinho" vem do "homem comum" do Código de Hamurabi
    {
        "temas_secundarios": ["palavras_viajantes", "leis_julgamentos"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "\"Mesquinho\" tem raiz na Babilônia: no Código de Hamurabi, \"muškēnum\" era o homem comum, de classe baixa. O termo sobreviveu no árabe \"miskīn\", pobre, que deu \"mesquinho\" em português.",
        "explicacao": (
            "O Código de Hamurabi não tratava todos do mesmo jeito: idade, profissão, classe e sexo mudavam a pena ou a "
            "reparação. O texto distingue três tipos de pessoa. O awīlum era algo como um \"cavalheiro\", de classe alta; "
            "o muškēnum, o homem comum; e havia os escravos e escravas. O famoso \"olho por olho\" aparece, por exemplo, "
            "na lei que manda cegar quem cegar outro awīlum. O muškēnum não era simplesmente punido com mais rigor: a "
            "vida dele podia valer menos, mas algumas multas também eram menores. A palavra sempre deu trabalho aos "
            "tradutores, e houve quem a vertesse como \"leproso\" e até como \"nobre\". O assiriólogo Wolfram von Soden "
            "propôs que ela venha de um verbo acadiano que significa \"curvar-se, suplicar\". Como nome para gente de "
            "posição social baixa, ela atravessou os milênios e chegou ao árabe miskīn, ao italiano meschino, ao "
            "espanhol mezquino e ao francês mesquin. No português, o dicionário Priberam registra a origem de "
            "\"mesquinho\" no árabe miskin, \"pobre, desgraçado, infeliz\". Daí os dois sentidos que a palavra ainda tem: "
            "o de quem tem poucos recursos e o de quem é apegado demais ao dinheiro."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Code_of_Hammurabi",
                "Persons were not equal before the law; not just age and profession but also class and gender dictated the punishment or remedy they received. "
                "Three main kinds of person, awīlum, muškēnum, and wardum (male)/amtum (female), are mentioned throughout the Code. "
                "A wardum/amtum was a male/female slave. [...] "
                "with awīlum meaning something like \"gentleman\" and muškēnum something like \"commoner\". "
                "The penalties were not necessarily stricter for a muškēnum than an awīlum: a muškēnum's life may have been cheaper, but so were some of his fines. [...] "
                "Wolfram von Soden, in his Akkadisches Handwörterbuch, proposed that muškēnum was derived from šukênum, \"to bow down/supplicate\". "
                "As a word for a man of low social standing, it has endured, possibly from a Sumerian root, into Arabic (miskīn), Italian (meschino), Spanish (mezquino), and French (mesquin). "
                "However, some earlier translators, also seeking to explain the muškēnum's special treatment, translated it as \"leper\" and even \"noble\". [...] "
                "If an [awīlum] should blind the eye of another [awīlum], they shall blind his eye.",
                nome="Code of Hammurabi"),
            {"url": "https://dicionario.priberam.org/mesquinho",
             "titulo": "Mesquinho (Dicionário Priberam da Língua Portuguesa)", "idioma": "pt",
             "trecho": "Que tem poucos recursos. [...] "
                       "Que ou quem é muito apegado ao dinheiro e não gosta de o gastar. [...] "
                       "Origem:árabe miskin, pobre, desgraçado, infeliz."},
        ],
    },
    # 3 George Smith tira a roupa ao ler o dilúvio de Gilgamesh
    {
        "temas_secundarios": ["literatura", "religioes", "decifracao"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Em 1872, ao ler numa tabuinha de barro uma história de dilúvio, com barco, animais e aves soltas depois da cheia, o inglês George Smith teria começado a tirar a roupa e a correr pela sala de tanta euforia.",
        "explicacao": (
            "Smith vinha de família operária e teve pouca educação formal. Aos catorze anos virou aprendiz de gravador de "
            "cédulas numa editora de Londres e passava a hora do almoço no Museu Britânico, estudando as publicações "
            "sobre as tabuinhas cuneiformes achadas perto de Mossul, no atual Iraque. O talento chamou atenção, e o "
            "museu acabou por contratá-lo. A peça decisiva tinha sido desenterrada em Nínive e ainda não fora traduzida: "
            "era a décima primeira tabuinha do Épico de Gilgamesh, uma das obras literárias mais antigas que se conhecem. Nela, o deus "
            "Ea avisa Utnapishtim do dilúvio planejado pelos deuses; ele constrói um barco, embarca parentes, artesãos e "
            "animais e, no sétimo dia, solta uma pomba, uma andorinha e um corvo, e só o corvo não volta. Segundo colegas "
            "da sala de leitura, ao entender o que lia, Smith começou a tirar peças de roupa e a correr gritando de "
            "alegria. Ele apresentou a tradução em 3 de dezembro de 1872, com o primeiro-ministro Gladstone na plateia. "
            "O jornal The Daily Telegraph pagou então uma expedição a Nínive, e em 7 de maio de 1873 Smith achou um "
            "fragmento com a parte que faltava da história. Hoje os estudiosos em geral consideram que o dilúvio do "
            "Gênesis foi adaptado de tradições mesopotâmicas mais antigas, sobretudo a de Gilgamesh."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("George_Smith_(Assyriologist)",
                "As the son of a working-class family in Victorian England, Smith was limited in his ability to acquire a formal education. "
                "At age fourteen, he was apprenticed to the London-based publishing house of Bradbury and Evans to learn banknote engraving, at which he excelled. [...] "
                "he spent his lunch hours at the British Museum, studying publications on the cuneiform tablets that had been unearthed near Mosul in present-day Iraq [...] "
                "In 1872, Smith achieved worldwide fame by his translation of the Chaldaean account of the Great Flood, which he read before the Society of Biblical Archaeology on 3 December. "
                "The audience included the sitting prime minister, William Ewart Gladstone. "
                "According to the accounts of his coworkers in the reading room, on the day of the discovery, when Smith realized what he was reading he \"began to remove articles of his clothing\" and run around the room shouting in delight. "
                "This work is better known today as the eleventh tablet of the Epic of Gilgamesh, one of the oldest known works of literature [...] "
                "Edwin Arnold, the editor of The Daily Telegraph, arranged for Smith to go to Nineveh at the expense of that newspaper and carry out excavations with a view to finding the missing fragments of the Flood story.",
                nome="George Smith (Assyriologist)"),
            wiki("Gilgamesh_flood_myth",
                "The first Gilgamesh flood tablet was discovered by Hormuzd Rassam in Nineveh and was in the collection of the British Museum, but had not been translated. [...] "
                "Smith found a portion of a tablet on 7 May 1873 containing the missing part of the flood story [...] "
                "But the god Ea (Sumerian god Enki) repeated the plan to Utnapishtim through a reed wall in a reed house. "
                "Ea commanded Utnapishtim to demolish his house and build a boat [...] "
                "His relatives and craftsmen, and \"all the beasts and animals of the field\" boarded the boat. [...] "
                "On the seventh day he released a dove that flew away but came back to him. "
                "He released a swallow, but it also came back to him. "
                "He released a raven that was able to eat and scratch, and did not circle back to the boat.",
                nome="Gilgamesh flood myth"),
            wiki("Genesis_flood_narrative",
                "Scholars generally believe it was adapted from older Mesopotamian flood traditions, especially the Epic of Gilgamesh",
                nome="Genesis flood narrative"),
        ],
    },
    # 4 o incêndio que salvou a biblioteca de Assurbanípal
    {
        "temas_secundarios": ["sistemas_escrita", "literatura"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Quando Nínive foi destruída, em 612 a.C., o fogo provavelmente ajudou a salvar a biblioteca do rei Assurbanípal: as tabuinhas de argila ficaram parcialmente cozidas e resistiram. As tábuas de cera se perderam.",
        "explicacao": (
            "Assurbanípal, o último grande rei da Assíria, tinha fama de comandante militar implacável, mas também era um "
            "intelectual: sabia ler e escrever e dominava o acadiano e o sumério. Para formar a coleção, escreveu a "
            "cidades e centros de estudo de toda a Mesopotâmia pedindo cópias de tudo o que havia sido escrito, mandou "
            "escribas a todas as regiões do império atrás de textos antigos e contratou estudiosos para copiá-los. Muitas "
            "tabuinhas levam um carimbo dizendo que pertenciam ao palácio. Há leis, cartas diplomáticas, finanças, "
            "presságios, encantamentos, hinos, medicina, astronomia e literatura, inclusive o Épico de Gilgamesh. Em 612 "
            "a.C., uma coalizão de babilônios, citas e medos destruiu Nínive. Acredita-se que, no incêndio do palácio, o "
            "fogo tenha atingido a biblioteca e cozido em parte as tabuinhas de argila, um desastre que acabou "
            "ajudando a preservá-las. Parte dos textos, porém, provavelmente estava em tábuas de cera, que, por serem de "
            "material orgânico, sumiram. O Museu Britânico conta 30.943 \"tabuinhas\" na coleção da biblioteca de Nínive. "
            "Descontados os fragmentos de um mesmo texto, a biblioteca original teria uns 10 mil textos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Library_of_Ashurbanipal",
            "named after Ashurbanipal, the last great king of the Assyrian Empire, is a collection of more than 30,000 clay tablets and fragments [...] "
            "Among its holdings was the famous Epic of Gilgamesh. [...] "
            "Ashurbanipal was known as a tenacious martial commander; however, he was also a recognized intellectual who was literate, and a passionate collector of texts and tablets. "
            "In collecting texts for his library, he wrote to cities and centers of learning across Mesopotamia, instructing them to send him copies of all work written in the region. "
            "As an apprentice scribe he mastered both the Akkadian and the Sumerian languages. "
            "He sent scribes into every region of the Neo-Assyrian Empire to collect ancient texts. "
            "He hired scholars and scribes to copy texts, mainly from Babylonian sources. [...] "
            "Many of these tablets contain a stamp stating that they belonged to his palace. [...] "
            "included colloquial compositions in the form of legislation, foreign correspondences and engagements, aristocratic declarations, and financial matters. "
            "The remaining texts contained divinations, omens, incantations and hymns to various gods, while others were concerned with medicine, astronomy, and literature. [...] "
            "Nineveh was destroyed in 612 BCE by a coalition of Babylonians, Scythians and Medes, an ancient Iranian people. "
            "It is believed that during the burning of the palace, a great fire must have ravaged the library, causing the clay cuneiform tablets to become partially baked. "
            "This potentially destructive event helped preserve the tablets. "
            "As well as texts on clay tablets, some of the texts may have been inscribed onto wax boards which, because of their organic nature, have been lost. "
            "The British Museum's collections database counts 30,943 \"tablets\" in the entire Nineveh library collection [...] "
            "If all smaller fragments that actually belong to the same text are deducted, it is likely that the \"library\" originally included some 10,000 texts in all.",
            nome="Library of Ashurbanipal")],
    },
    # 5 Nabonido, o rei arqueólogo, e o museu da filha Ennigaldi
    {
        "temas_secundarios": ["personagens_esquecidos", "calendarios"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "O último rei da Babilônia escavava templos antigos e tentou datar o que achava: errou por uns 1.500 anos. Sua filha montou o museu público mais antigo que se conhece, com etiquetas de barro em três línguas.",
        "explicacao": (
            "Nabonido reinou de 556 a.C. até 539 a.C., quando a Babilônia caiu diante de Ciro, o Grande, e às vezes é "
            "chamado de \"primeiro arqueólogo\". Os reis mesopotâmicos já costumavam escavar as fundações dos templos para "
            "reconstruí-los segundo o plano original, mas ele descrevia os achados com bem mais detalhe que seus "
            "antecessores e, em três casos conhecidos, tentou datar os reis que os tinham deixado. Ao escavar um templo "
            "erguido por Naram-Sin, rei da Acádia, calculou que ele vivera 3.200 anos antes. Errou por cerca de 1.500 anos, "
            "mas é a datação de um artefato arqueológico mais antiga que se conhece, e uma boa estimativa para quem não "
            "tinha técnica precisa nenhuma. A filha, Ennigaldi, consagrada por ele sacerdotisa em Ur, aprendeu com o pai "
            "a apreciar antiguidades. Por volta de 530 a.C., ela guardou num templo ao lado de onde morava peças do sul "
            "da Mesopotâmia, algumas do século XX a.C., e as usava para explicar a história da região. Em 1925, o "
            "arqueólogo Leonard Woolley achou dezenas de objetos arrumados lado a lado, com idades separadas por séculos. "
            "Concluiu que eram peças de museu porque vinham com \"etiquetas\": cilindros de barro escritos em três línguas, "
            "uma delas o sumério."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Nabonidus",
                "was the last king of the Neo-Babylonian Empire, ruling from 556 BC to the fall of Babylon to the Achaemenid Empire under Cyrus the Great in 539 BC. [...] "
                "Ennigaldi-Nanna (Akkadian: En-nigaldi-Nanna) – a daughter. Consecrated by her father as an entum-priestess in Ur. [...] "
                "Nabonidus has sometimes been described as the \"first archaeologist\". "
                "Nabonidus conducted excavations founded on the well-established Mesopotamian idea that in order to properly renovate and rebuild a temple, its foundations had to be excavated so that it could be restored in accordance with its original plans. [...] "
                "Nabonidus on the other hand is more explicit and in three known instances even attempted to date these preceding rulers [...] "
                "Naram-Sin of Akkad (r. c. 2254–2218 BC) 3200 years before his own reign. "
                "His attempted dating of Naram-Sin's reign, based on what was found during the excavation of a temple built by the king, is the earliest known dating of an archaeological artifact, "
                "and though Nabonidus's proposed date is off by about 1,500 years, it was still a very good estimate considering the lack of accurate dating technology.",
                nome="Nabonidus"),
            wiki("Ennigaldi-Nanna's_museum",
                "Ennigaldi-Nanna's museum is the earliest known public museum. It dates to circa 530 BCE. "
                "The curator was Ennigaldi, the daughter of Nabonidus, the last king of the Neo-Babylonian Empire. [...] "
                "The museum was discovered in 1925, when archaeologist Leonard Woolley excavated portions of the palace and temple complex at Ur. "
                "He found dozens of artifacts, neatly arranged side by side, whose ages varied by centuries. "
                "He determined that they were museum pieces, because they were accompanied by \"museum labels\"; clay drums written in three different languages, including Sumerian. [...] "
                "He taught her to appreciate ancient artifacts and influenced her to create her educational antiquity museum. "
                "The artifacts came from the southern regions of Mesopotamia. "
                "Many had originally been excavated by Nabonidus and were from as early as the 20th century BCE. [...] "
                "Ennigaldi stored the artifacts in a temple next to the palace where she lived. "
                "She used the museum pieces to explain the history of the area",
                nome="Ennigaldi-Nanna's museum"),
        ],
    },
    # 6 Uruk e as tigelas descartáveis feitas em massa
    {
        "temas_secundarios": ["cidades", "dinheiro", "sistemas_escrita"],
        "tipos_espanto": ["escala_absurda", "engenhosidade"],
        "gancho": "Por volta de 3100 a.C., Uruk era provavelmente a maior área urbana do mundo. Seu objeto mais típico é uma tigela tosca, feita em massa e jogada fora aos montes: uns três quartos da cerâmica dos sítios dessa cultura.",
        "explicacao": (
            "No auge, Uruk, no sul da Mesopotâmia, pode ter tido até 50 mil moradores, com outros 80 mil a 90 mil "
            "vivendo nos arredores, e ocupava 250 hectares no fim do período que leva o seu nome. Teve algumas das "
            "primeiras construções monumentais da história. Mas o que os arqueólogos mais acham ali é bem mais humilde: "
            "as tigelas de borda chanfrada. Sem nenhuma decoração, elas costumam ter uns 10 cm de altura e 18 cm de boca, "
            "e a maioria cabe entre 0,78 e 1,21 litro. São de barro cozido em baixa temperatura e aparecem descartadas em "
            "grande quantidade, muitas vezes inteiras e empilhadas. O método de fabricação não é conhecido com certeza, "
            "mas a teoria mais aceita é o uso de um molde, o que tornaria viável produzi-las em massa. A interpretação "
            "mais difundida é que serviam para medir rações de grãos pagas a trabalhadores: seriam usadas uma ou duas "
            "vezes e depois jogadas fora, quase como um descartável. A ideia é contestada, e há quem pense em formas de "
            "assar pão ou em oferendas. Cedo se sugeriu até que um sinal da escrita protocuneiforme tenha derivado "
            "desse tipo de tigela. Ela é tão característica que basta encontrá-la para saber que a cultura de Uruk "
            "esteve ali."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Uruk",
                "At its peak around 3100 BC, the city may have had up to 50,000 residents, with 80,000–90,000 people living in its environs, making it the largest urban area in the world at the time. [...] "
                "Uruk has some of the first monumental constructions in architectural history, and certainly the largest of its era. [...] "
                "By the end of the Uruk period c. 3100 BC) Uruk had reached a size of 250 ha",
                nome="Uruk"),
            wiki("Bevelled_rim_bowl",
                "Beveled rim bowls (traditionally called Glockentöpfe) are small, undecorated, mass-produced clay bowls most common in the 4th millennium BC during the Late Chalcolithic period. "
                "They constitute roughly three quarters of all ceramics found in Uruk culture sites, are therefore a unique and reliable indicator of the presence of the Uruk culture in ancient Mesopotamia. [...] "
                "Early on it was suggested that one of the signs of  Proto-cuneiform, and perhaps a corresponding sign in Cuneiform (GAR/NINDA/AKALU), was derived from the bevelled rim bowl. [...] "
                "Beveled rim bowls are usually considered to be uniform in size standing roughly 10 cm (4 in) tall with the mouth of the bowl being approximately 18 cm (7.1 in) in diameter. [...] "
                "Most BRBs hold 0.78–1.21 litres. [...] "
                "The porous vegetable tempered bowls are made of low fired clay [...] "
                "The most unusual aspects of bevelled rim bowls are that they are undecorated and found discarded in large quantities. [...] "
                "While the exact method for production of beveled rim bowls is unknown, the most widely accepted theory is the use of a mold. [...] "
                "mass production with a mold is far more feasible than making them by hand. [...] "
                "bevelled rim bowls are widely thought to be used for measurement of grain rations (barley, spelt, or emmer wheat). "
                "The rations would be given as payment to laborers for services rendered as part of a Corvée labor system. "
                "It is also supported by the fact that the bowls are often found whole and in large piles as if they were disposable. "
                "The bowls would have been used for rationing once or twice and then discarded in a central location [...] "
                "The use of BRBs as ration bowls has been challenged. "
                "An alternate theory is that the bowls were used for baking bread [...] "
                "it was suggested that they functioned as votive offerings.",
                nome="Bevelled rim bowl"),
        ],
    },
    # 7 Taram-Kubi, empresária de Assur
    {
        "temas_secundarios": ["comercio_rotas", "personagens_esquecidos", "moda"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "No século XIX a.C., a assíria Taram-Kubi fazia tecidos de luxo em Assur e os mandava por caravana ao marido, que os vendia na atual Turquia. As cartas de barro dela misturam negócios, cobranças e saudade.",
        "explicacao": (
            "Em Kanesh, hoje Kültepe, na Anatólia central, mercadores vindos de Assur mantinham um bairro comercial, o "
            "kārum. As mais de 23 mil tabuinhas cuneiformes achadas nas casas formam a maior coleção de textos de locais "
            "não administrativos do antigo Oriente Próximo. O comércio era tocado por famílias, não pelo Estado, e as "
            "cartas trazem uma quantidade extraordinária de informação sobre a vida das mulheres. Taram-Kubi morava em "
            "Assur e era sócia do marido, Innaya, que vivia e trabalhava em Kanesh. Ela fazia tecidos muito procurados; "
            "ele os vendia e mandava a prata de volta, e as cartas iam e vinham com as caravanas. Rica, ela emprestou "
            "prata ao irmão para comprar uma casa e pagou uma dívida do marido com a administração da cidade, exigindo "
            "depois o reembolso. Também tratou com as autoridades de um processo contra Innaya por vendas suspeitas de "
            "lápis-lazúli. As brigas eram sérias: antes de partir, ele esvaziou a casa de cevada, e quando veio a fome ela "
            "ficou sem comida para si e para o filho. Mesmo assim, nas cartas, pedia que ele voltasse para ficar ao "
            "lado dela."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Kültepe_texts",
            "was a Bronze Age (broadly, 3300–1200 BC) settlement and trading center on the Central Anatolian plateau in modern Turkey. [...] "
            "a kārum (the Assyrian word for trading district) was established in the beginning of the 2nd millennium BC. "
            "The over 23,000 cuneiform tablets recovered from residences at Kültepe constitute the largest collection of texts found in non-administrative locales of the ancient Near East. [...] "
            "The trade was run by families rather than the state. [...] "
            "The cuneiform archives provide an extraordinary amount of information about daily life for women at Kaneš [...] "
            "Taram-Kubi was an Assyrian businesswoman of the 19th c. BCE. "
            "She was married to Innaya, had a son, Ikuppiya [...] "
            "Taram-Kubi lived in Assur while her husband lived and worked in Kaneš. "
            "Taram-Kubi was business partners with Innaya, and they communicated through cuneiform clay tablets transported by caravans between Assur and Kaneš. "
            "Taram-Kubi crafted textiles that were highly sought after, which were then sent to Innaya in Kaneš, where he would sell them and send silver back. "
            "Taram-Kubi was wealthy, having enough funds to lend silver to her brother for purchasing a house. "
            "She also covered a debt her husband had to city administration in Assur, which she then demanded he repay afterward. "
            "She also worked with authorities to resolve a lawsuit her husband had been involved in regarding suspicious sales of lapis lazuli. [...] "
            "she still missed him and in her letters requested he return to Assur to be by her side. "
            "One example of their quarrels included Innaya emptying their house of barley before he left for Kaneš, and then a famine coming, leaving Taram-Kubi with no food for her and their child.",
            nome="Kültepe")],
    },
    # 8 a língua indo-europeia mais antiga registrada, em cartas de mercadores assírios
    {
        "temas_secundarios": ["linguas_mundo", "historia_portugues", "comercio_rotas"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "O registro mais antigo de uma língua indo-europeia, a família do português, não vem da Grécia nem da Índia: são palavras e nomes hititas soltos em cartas de mercadores assírios na Turquia, do século XX a.C.",
        "explicacao": (
            "O hitita, hoje extinto, era falado na Anatólia durante a Idade do Bronze. Ele aparece sobretudo nos arquivos "
            "da cidade de Hattusa, entre os séculos XVII e XIII a.C. Mas já no século XX a.C. palavras e nomes de pessoas "
            "em hitita surgem, isolados, em documentos escritos em acadiano em Kanesh, a atual Kültepe. Ali, mercadores "
            "vindos de Assur mantinham um bairro comercial e deixaram milhares de tabuinhas. Os textos estão em assírio "
            "antigo, mas os empréstimos e nomes hititas que aparecem neles são o registro mais antigo de qualquer língua "
            "indo-europeia. É a família que inclui o latim e as línguas que vieram dele, como o espanhol, o francês, o "
            "italiano e o português. A cidade ficou até no nome da língua: os textos hititas marcavam os trechos no "
            "idioma com a palavra nesili, \"na fala de Neša\", outro nome de Kanesh. E o hitita intriga os linguistas: "
            "apesar de ser o mais antigo registrado, não tinha a divisão entre masculino e feminino que aparece no latim "
            "clássico, no grego antigo ou no sânscrito védico. Em vez disso, usava um sistema rudimentar de classes de "
            "substantivos."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Hittite_language",
                "Hittite, also known as Nesite, is an extinct Indo-European language formerly spoken in Anatolia during the Bronze Age. "
                "The language is attested in cuneiform texts, primarily from the archives of the city of Hattusa, between the 17th century BC to the 13th century BC. "
                "Isolated Hittite words and personal names appear in Akkadian documents in Kanesh from as early as the 20th century BC, making it the earliest attested use of the Indo-European languages. [...] "
                "passages written in Hittite are preceded by the adverb nesili (or nasili, nisili), \"in the [speech] of Neša (Kaneš)\" [...] "
                "Hittite is the oldest attested Indo-European language, yet it lacks several grammatical features that are exhibited by other early-attested Indo-European languages such as Vedic Sanskrit, Classical Latin, Ancient Greek, Old Persian and Old Avestan. "
                "Notably, Hittite did not have a masculine–feminine gender system. "
                "Instead, it had a rudimentary noun-class system",
                nome="Hittite language"),
            wiki("Kültepe_texts",
                "Assyrian merchants then established the kārum of the city: \"Kaneš\". [...] "
                "The Kültepe texts are the oldest documents from Anatolia. "
                "Although they are written in Old Assyrian, the Hittite loanwords and names in the texts are the oldest record of any Indo-European language.",
                nome="Kültepe"),
            wiki("Indo-European_languages",
                "Latin and its descendants, the Romance languages, such as Spanish, Portuguese, French, Italian and Romanian.",
                nome="Indo-European languages"),
        ],
    },
    # 9 a escrita do Indo, indecifrada
    {
        "temas_secundarios": ["decifracao", "sistemas_escrita"],
        "tipos_espanto": ["misterio_aberto"],
        "gancho": "A escrita do Vale do Indo nunca foi decifrada, apesar de mais de cem tentativas, e nem está provado que seja uma escrita. Em 2025, o governante de Tamil Nadu, na Índia, ofereceu US$ 1 milhão a quem conseguir.",
        "explicacao": (
            "Os símbolos aparecem sobretudo em pequenos selos, a maioria com 2 a 3 centímetros de lado, além de cerâmica, "
            "placas de cobre e bronze, ferramentas e armas. Em 2025, falava-se em cerca de 5 mil inscrições escavadas desde "
            "1924, com mais de 400 sinais diferentes. O problema é que elas são curtíssimas: em média, uns cinco sinais. "
            "Com tão pouco contexto, nem computadores conseguiram decifrá-las. Também não existe nenhuma inscrição "
            "bilíngue, como a Pedra de Roseta, e nenhum governante do Indo aparece nos registros de outros povos, ao "
            "contrário de Ramsés e Ptolomeu, cujos nomes os decifradores dos hieróglifos já conheciam por textos em grego. "
            "Nem a língua falada é conhecida. Por isso há quem duvide que os sinais registrem um idioma: poderiam ser algo "
            "como marcas de comerciante ou uma protoescrita. Um estudo publicado na Science em 2009 argumentou que o padrão "
            "dos símbolos lembra o das línguas faladas, mas críticos responderam que o método não distingue sistemas "
            "linguísticos de não linguísticos. Os poucos consensos são modestos: a maioria das inscrições é lida da "
            "direita para a esquerda, e certos traços parecem ser números."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Indus_script",
                "Despite many attempts, the script has not yet been deciphered. "
                "There is no known bilingual inscription to help decipher the script [...] "
                "with over 400 distinct signs represented across known inscriptions. [...] "
                "In 2025, it was reported around 5,000 inscriptions have been excavated since 1924. "
                "Indus script symbols have primarily been found on stamp seals, pottery, bronze and copper plates, tools, and weapons. [...] "
                "with most being just 2–3 centimetres in length on each side. [...] "
                "Inscriptions are very short. The average length of the inscriptions is around five signs [...] "
                "There are doubts whether the Indus script records a written language or is instead a system of non-linguistic signs or proto-writing similar to merchant's marks and house marks [...] "
                "The spoken Harappan language has not been identified [...] "
                "No digraphic or bilingual texts, like the Rosetta Stone, have been found. "
                "No names, such as those of Indus rulers or personages, are known to be attested in surviving historical records or myths, as was the case with rulers like Rameses and Ptolemy, who were known to hieroglyphic decipherers from records attested in Greek. [...] "
                "The few points on which there exists scholarly consensus are the right-to-left direction of the majority of the inscriptions, numerical nature of certain stroke-like signs [...] "
                "Over 100 (mutually exclusive) attempts at decipherment have been published since the 1920s [...] "
                "In 2025, Tamil Nadu Chief Minister M. K. Stalin announced a $1 million (USD) prize for deciphering the Indus Valley Script",
                nome="Indus script"),
            wiki("Indus_Valley_Civilisation",
                "The Harappan script is yet undeciphered, indeed it has not even been demonstrated to be a writing system, and therefore the language remains unknown. [...] "
                "In a 2009 study by P.N. Rao et al. published in Science, computer scientists, comparing the pattern of symbols to various linguistic scripts and non-linguistic systems, including DNA and a computer programming language, found that the Indus script's pattern is closer to that of spoken words [...] "
                "They conclude that the method used by Rao et al. cannot distinguish linguistic systems from non-linguistic ones. "
                "The messages on the seals have proved to be too short to be decoded by a computer.",
                nome="Indus Valley Civilisation"),
        ],
    },
    # 10 Shu-ilishu, tradutor da língua de Meluhha
    {
        "temas_secundarios": ["comercio_rotas", "decifracao", "linguas_mundo"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "No fim do período acádio, um mesopotâmico chamado Shu-ilishu tinha um selo de \"tradutor da língua de Meluhha\", provável nome do Vale do Indo. Talvez ele lesse a escrita que ninguém decifra hoje.",
        "explicacao": (
            "Meluhha aparece em inscrições da Mesopotâmia como uma terra de onde vinham navios e mercadores que traziam "
            "ouro em pó, cornalina e lápis-lazúli. A maioria dos estudiosos acha que era o nome sumério da civilização do "
            "Vale do Indo. Os contatos deixaram rastros: uns vinte selos do Indo apareceram em cidades mesopotâmicas como "
            "Ur, Babilônia e Kish, e documentos cuneiformes mostram ao menos uma aldeia de gente de Meluhha na Acádia, com "
            "moradores chamados \"filho de Meluhha\". O selo cilíndrico de Shu-ilishu, que o arqueólogo Gregory Possehl "
            "data do fim do período acádio, por volta de 2020 a.C., diz que ele era tradutor dessa língua. A peça não veio "
            "de escavação: pertencia a uma coleção do século XIX formada com objetos comprados de comerciantes, e por isso "
            "não se sabe de onde saiu. Hoje está no Louvre. Para Possehl, especialista no Indo, um tradutor oficial sugere "
            "alguém talvez letrado, capaz de ler a escrita do Indo, que continua indecifrada. Daí a esperança de que "
            "existam, em algum lugar da Mesopotâmia, tabuinhas bilíngues em acádio e na língua de Meluhha, o tipo de texto "
            "que permitiu decifrar os hieróglifos. O próprio Possehl admite que esses documentos podem não existir."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": "https://www.penn.museum/sites/expedition/shu-ilishus-cylinder-seal/",
             "titulo": "Shu-ilishu's Cylinder Seal (Gregory L. Possehl, Expedition Magazine, Penn Museum, 2006)", "idioma": "en",
             "trecho": "I found a reference to the personal cylin­der seal of a translator of the Meluhhan language. "
                       "His name was Shu-ilishu and he lived in Mesopotamia during the Late Akkadian period (ca. 2020 BC, according to the new, low chronology). "
                       "I was interested in this man because Meluhha is widely believed to have been the Indus Civilization of the Greater Indus Valley in India and Pakistan [...] "
                       "Based on cuneiform documents from Mesopotamia we know that there was at least one Meluhhan village in Akkad at that time, with people called “Son of Meluhha” living there. [...] "
                       "Gathered together in the 19th century by a wealthy man, this collection is composed of objects purchased from dealers with little, if any, provenience data presented. "
                       "Therefore, we do not know where Shu-ilishu’s cylinder came from. [...] "
                       "The “Collection de Clercq”had found its way to the Louvre [...] "
                       "The writing of Meluhha (the Indus script) remains undeciphered, in spite of many claims to the contrary. [...] "
                       "To break the code, what is probably needed is a body of bilingual texts, like Jean-Francois Champollion had when he deciphered the Egyptian hieroglyphics on the Rosetta Stone. "
                       "The presence in Akkad of a translator of the Meluhhan language suggests that he may have been literate and could read the undeciphered Indus script. "
                       "This in turn suggests that there may be bilingual Akkadian/Meluhhan tablets some­where in Mesopotamia. "
                       "Although such documents may not exist"},
            wiki("Meluhha",
                "In an inscription, Sargon of Akkad (2334–2279 BCE) referred to ships coming from Meluhha, Magan and Dilmun. [...] "
                "Gudea of Lagash (c. 21st century BCE) referred to the Meluhhans who came to Sumer to sell gold dust, carnelian, etc. [...] "
                "he mentions his procurement of \"blocks of lapis lazuli and bright carnelian from Meluhha\". [...] "
                "Several Indus seals with Harappan script have been found in Mesopotamia, particularly in Ur, Babylon and Kish. [...] "
                "Only some twenty Indus seals have turned up in Mesopotamia since the earliest discoveries [...] "
                "Most scholars suggest that Meluhha was the Sumerian name for the Indus Valley Civilisation.",
                nome="Meluhha"),
        ],
    },
    # 11 cidades do Indo: esgoto para todos, nenhum palácio
    {
        "temas_secundarios": ["cidades", "grandes_obras"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "As cidades do Vale do Indo tinham ruas em grade, esgoto coberto e, só em Mohenjo-daro, mais de 700 poços. Mas nenhum palácio ou templo foi identificado com certeza, e ninguém sabe quem as governava.",
        "explicacao": (
            "Na fase madura, de 2600 a 1900 a.C., a civilização do Indo ocupava boa parte do atual Paquistão e o noroeste "
            "da Índia, e era a mais extensa das três primeiras civilizações, ao lado do Egito e da Mesopotâmia. Mohenjo-daro "
            "e Harappa provavelmente chegaram a ter de 30 mil a 60 mil habitantes. A maioria das cidades seguia uma grade "
            "uniforme e bem planejada, e em Harappa, Mohenjo-daro e Rakhigarhi estão os sistemas de saneamento urbano mais "
            "antigos que se conhecem: a água usada num cômodo de banho seguia para canais cobertos ao longo das ruas "
            "principais. Em Mohenjo-daro, os poços passam de 700, cerca de um para cada três casas, número sem paralelo "
            "no Egito ou na Mesopotâmia da época. Ao contrário dessas vizinhas, porém, o Indo não ergueu grandes "
            "monumentos, e não há prova conclusiva de palácios ou templos. Algumas casas eram maiores que outras, mas "
            "todas tinham acesso a água e esgoto, o que dá a impressão de uma sociedade com pouca concentração de riqueza. "
            "Quem mandava continua em aberto: há quem veja nos pesos e medidas padronizados sinal de um poder central, e "
            "quem pense em cidades-Estado independentes. Até a famosa estátua do \"Rei-Sacerdote\" ganhou o apelido dos "
            "arqueólogos, sem nenhuma prova de que sacerdotes ou reis governassem a cidade."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Indus_Valley_Civilisation",
                "and in its mature form from 2600 BCE to 1900 BCE. "
                "Together with ancient Egypt and Mesopotamia, it was one of the three early civilisations of the Near East and South Asia; of the three, it was the most widespread: it spanned much of Pakistan, northwestern India, and northeast Afghanistan. [...] "
                "Mohenjo-daro and Harappa very likely grew to contain between 30,000 and 60,000 individuals [...] "
                "As seen in Harappa, Mohenjo-daro and the 2010s partially excavated Rakhigarhi, this urban plan included the world's first known city sanitation systems. [...] "
                "From a room that appears to have been set aside for bathing, waste water was directed to covered drains, which lined the major streets. [...] "
                "In sharp contrast to this civilisation's contemporaries, Mesopotamia and ancient Egypt, no large monumental structures were built. "
                "There is no conclusive evidence of palaces or temples. [...] "
                "Although some houses were larger than others, Indus Valley Civilisation cities were remarkable for their apparent, if relative, egalitarianism. "
                "All the houses had access to water and drainage facilities. "
                "This gives the impression of a society with relatively low wealth concentration. [...] "
                "Archaeological records provide no immediate answers for the question of who ruled Harappan cities and how. [...] "
                "the majority of the cities were constructed in a highly uniform and well-planned grid pattern [...] "
                "There was a single state or federation ruling all or most of the Indus Valley. "
                "Proponents of this theory believe that the presence of standardised weights and measures demonstrates the presence of a central authority. "
                "There was no single ruler, with each city being a self-governing city state.",
                nome="Indus Valley Civilisation"),
            wiki("Mohenjo-daro",
                "With the excavations done so far, over 700 wells are present at Mohenjo-daro, alongside drainage and bathing systems. "
                "This number is unheard of when compared to other civilisations at the time, such as Egypt or Mesopotamia, and the quantity of wells transcribes as one well for every three houses. [...] "
                "Though there is no evidence that priests or monarchs ruled Mohenjo-daro, archaeologists dubbed this dignified figure a \"Priest-King\".",
                nome="Mohenjo-daro"),
        ],
    },
    # 12 a partilha que dividiu colares ao meio
    {
        "temas_secundarios": ["fronteiras_paises", "imperios_coloniais", "crimes_arte"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Quando Índia e Paquistão se separaram, os cerca de 12 mil objetos achados em Mohenjo-daro foram divididos meio a meio. Às vezes ao pé da letra: as contas de colares e cintos foram separadas em dois montes.",
        "explicacao": (
            "Os achados de Mohenjo-daro, cidade do Vale do Indo no atual Paquistão, ficaram primeiro no Museu de Lahore. "
            "Depois foram levados para a sede do Serviço Arqueológico da Índia, em Nova Délhi, onde se planejava um grande "
            "museu para a nova capital do domínio britânico. A independência da Índia já era esperada, mas a partilha do "
            "território em dois países só foi prevista tarde no processo. Com a separação, as novas autoridades do "
            "Paquistão pediram de volta as peças escavadas em seu território, e a Índia recusou. O acordo final dividiu os "
            "cerca de 12 mil objetos, a maioria cacos de cerâmica, em partes iguais. Em alguns casos, a regra foi seguida "
            "ao pé da letra: colares e cintos tiveram as contas repartidas em duas pilhas. As duas esculturas mais "
            "célebres foram para lados opostos. O Paquistão pediu e recebeu o \"Rei-Sacerdote\", de pedra-sabão, e a "
            "Índia ficou com a \"Dançarina\", estatueta de bronze bem menor, de 10,5 centímetros, além do selo de "
            "Pashupati. Hoje a maior parte das peças está no Museu Nacional da Índia, em Nova Délhi, e no Museu Nacional "
            "do Paquistão, em Karachi."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Mohenjo-daro",
            "The finds from Mohenjo-daro were initially deposited in the Lahore Museum, but later moved to the ASI headquarters at New Delhi, where a new \"Central Imperial Museum\" was being planned for the new capital of the British Raj, in which at least a selection would be displayed. "
            "It became apparent that Indian independence was approaching, but the Partition of India was not anticipated until late in the process. "
            "The new Pakistani authorities requested the return of the Harappan pieces excavated on their territory, but the Indian authorities refused. "
            "Eventually an agreement was reached, whereby the finds, totalling some 12,000 objects (most sherds of pottery), were split equally between the countries; "
            "in some cases this was taken very literally, with some necklaces and girdles having their beads separated into two piles. "
            "In the case of the \"two most celebrated sculpted figures\", Pakistan asked for and received the Priest-king, while India retained the much smaller Dancing Girl, and also the Pashupati seal. "
            "Most of the objects from Mohenjo-daro retained by India are in the National Museum of India in New Delhi and those returned to Pakistan in the National Museum of Pakistan in Karachi [...] "
            "A bronze statuette dubbed the \"Dancing Girl\", 10.5 centimetres (4.1 in) high [...] "
            "In 1927, a seated male soapstone figure was found",
            nome="Mohenjo-daro")],
    },
    # 13 o massacre ariano que não houve
    {
        "temas_secundarios": ["clima_tempo", "mudancas_climaticas"],
        "tipos_espanto": ["historia_humana", "misterio_aberto"],
        "gancho": "Em 1953, o arqueólogo Mortimer Wheeler culpou invasores arianos pelo fim da civilização do Indo, citando esqueletos de um suposto massacre. Os corpos eram de depois do abandono da cidade, e as marcas nos crânios, erosão.",
        "explicacao": (
            "Wheeler, diretor do Serviço Arqueológico da Índia desde 1944, propôs que a migração de povos arianos vindos da "
            "Ásia Central causara o declínio do Indo. As provas eram um grupo de 37 esqueletos achados em vários pontos de "
            "Mohenjo-daro e trechos dos Vedas que falam de batalhas e fortes. Logo os estudiosos começaram a rejeitar a "
            "tese: os esqueletos eram de um período posterior ao abandono da cidade, e nenhum estava perto da cidadela. Em "
            "1994, Kenneth Kennedy reexaminou os ossos e mostrou que as marcas nos crânios tinham sido causadas pela "
            "erosão, não por violência. As pesquisas posteriores apontam para um vilão menos cinematográfico, o clima. A "
            "partir de cerca de 1800 a.C., a região ficou bem mais fria e seca, com o enfraquecimento das monções. Segundo "
            "um estudo de 2012 liderado por Liviu Giosan, os agricultores do Indo não tinham irrigação e dependiam das "
            "cheias de verão trazidas pelas monções. Quando elas se deslocaram para o sul, as cheias ficaram irregulares "
            "demais, e a população migrou para o leste, em direção à bacia do Ganges, onde formou aldeias menores. Mesmo "
            "assim, o fim não foi súbito: muitos elementos da civilização do Indo aparecem em culturas posteriores, e o "
            "debate sobre o seu declínio continua."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Indus_Valley_Civilisation",
                "Mortimer Wheeler, the Director of ASI from 1944 [...] "
                "In 1953, Sir Mortimer Wheeler proposed that migration by the Aryans, from Central Asia into South Asia, had caused the decline of the Indus civilisation. "
                "As evidence, he cited a group of 37 skeletons found in various parts of Mohenjo-daro, and passages in the Vedas referring to battles and forts. "
                "However, scholars soon started to reject Wheeler's theory, since the skeletons belonged to a period after the city's abandonment and none were found near the citadel. "
                "Subsequent examinations of the skeletons by Kenneth Kennedy in 1994 showed that the marks on the skulls were caused by erosion, and not by violence. [...] "
                "The Indus Valley climate grew significantly cooler and drier from about 1800 BCE, linked to a general weakening of the monsoon at that time. [...] "
                "According to Giosan et al. (2012), the IVC residents did not develop irrigation capabilities, relying mainly on the seasonal monsoons leading to summer floods. "
                "As the monsoons kept shifting south, the floods grew too erratic for sustainable agricultural activities. "
                "The residents then migrated towards the Ganges basin in the east, where they established smaller villages and isolated farms. [...] "
                "However, the Indus Valley Civilisation did not disappear suddenly, and many elements of the Indus civilisation appear in later cultures.",
                nome="Indus Valley Civilisation"),
            wiki("Lothal",
                "While the wider debate over the end of Indus Civilisation continues",
                nome="Lothal"),
        ],
    },
    # 14 os Jardins Suspensos talvez não fossem da Babilônia
    {
        "temas_secundarios": ["arquitetura", "grandes_obras"],
        "tipos_espanto": ["misterio_aberto", "mito_desmentido"],
        "gancho": "Os Jardins Suspensos são a única das Sete Maravilhas cujo local nunca foi confirmado, e nenhum texto babilônico os menciona. Uma hipótese: ficavam em outra cidade, Nínive, e eram obra de um rei assírio.",
        "explicacao": (
            "Segundo uma lenda, Nabucodonosor II, que reinou de 605 a 562 a.C., construiu os jardins para a esposa meda, "
            "Amitis, que sentia falta dos montes e vales verdes de sua terra. Quem conta isso é o sacerdote babilônio "
            "Beroso, que escreveu por volta de 290 a.C. e foi citado depois por Josefo. O problema é o silêncio das fontes "
            "da época: Nabucodonosor deixou inscrições longas e completas sobre suas obras, e nenhuma fala de jardim. "
            "Heródoto, que descreveu a Babilônia, também não os menciona, e nenhuma prova arqueológica foi achada na "
            "cidade. Há três explicações. Os jardins podem ser um mito, um ideal romântico de jardim oriental criado por "
            "autores gregos e romanos; podem ter existido e sido destruídos por volta do século I d.C.; ou podem ser outro "
            "jardim, bem documentado. É a hipótese de Stephanie Dalley, de Oxford: seriam os jardins do rei assírio "
            "Senaqueribe em Nínive, perto da atual Mossul, e os dois lugares teriam se confundido com o tempo. "
            "Senaqueribe chamou seu palácio e seu jardim de \"maravilha para todos os povos\" e descreveu parafusos para "
            "elevar a água. Para irrigá-los, levou canais por mais de 50 quilômetros até as montanhas e cruzou um vale com "
            "um aqueduto de mais de dois milhões de pedras talhadas. E deu às portas de Nínive nomes de deuses, como se "
            "quisesse que ela fosse vista como \"uma Babilônia\", nome que significa \"Porta dos Deuses\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Hanging_Gardens_of_Babylon",
            "According to one legend, the Hanging Gardens were built alongside a grand palace known as The Marvel of Mankind, by the Neo-Babylonian King Nebuchadnezzar II (who ruled between 605 and 562 BC), for his Median wife, Queen Amytis, because she missed the green hills and valleys of her homeland. "
            "This was attested to by the Babylonian priest Berossus, writing in about 290 BC, a description that was later quoted by Josephus. [...] "
            "The Hanging Gardens are the only one of the Seven Wonders whose location has not been definitively established. "
            "No extant Babylonian texts mention the gardens and no definitive archaeological evidence has been found in Babylon. "
            "Three theories have been suggested to account for this: first, that the gardens were purely mythical, and the descriptions found in ancient Greek and Roman writings (including those of Strabo, Diodorus Siculus and Quintus Curtius Rufus) represented a romantic ideal of an eastern garden; "
            "second, that they existed in Babylon but were destroyed sometime around the first century AD; "
            "and third, that the legend refers to a well-documented garden that the Assyrian King Sennacherib (704–681 BC) built in his capital city of Nineveh on the River Tigris, near the modern city of Mosul. [...] "
            "Many records exist of Nebuchadnezzar's works, yet his long and complete inscriptions do not mention any garden. [...] "
            "Herodotus, who describes Babylon in his Histories, does not mention the Hanging Gardens [...] "
            "Oxford scholar Stephanie Dalley has proposed that the Hanging Gardens of Babylon were actually the well-documented gardens constructed by the Assyrian king Sennacherib [...] "
            "Dalley posits that during the intervening centuries the two sites became confused [...] "
            "The name Babylon, meaning \"Gate of the Gods\", was the name given to several Mesopotamian cities. "
            "Sennacherib renamed the city gates of Nineveh after gods, which suggests that he wished his city to be considered \"a Babylon\". [...] "
            "Sennacherib called his new palace and garden \"a wonder for all peoples\". "
            "He describes the making and operation of screws to raise water in his garden. [...] "
            "The canals stretched over 50 kilometres (31 mi) into the mountains. [...] "
            "An enormous aqueduct crossing the valley at Jerwan was constructed of over two million dressed stones.",
            nome="Hanging Gardens of Babylon")],
    },
    # 15 Çatalhöyük: a cidade sem ruas
    {
        "temas_secundarios": ["pre_historia", "cidades", "arquitetura"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Em Çatalhöyük, na Turquia, por volta de 7000 a.C., não havia ruas: as casas de barro eram grudadas umas às outras, entrava-se por um buraco no teto e os mortos eram enterrados sob o chão e as camas.",
        "explicacao": (
            "Çatalhöyük foi uma protocidade muito grande do Neolítico, ocupada de cerca de 7500 a 5600 a.C. na planície "
            "de Konya. As casas de tijolo de barro formavam um aglomerado compacto, como um labirinto em favo de mel, sem "
            "trilhas ou ruas entre elas. A maioria era acessada por aberturas no teto, que também eram a única "
            "ventilação, e por portas laterais alcançadas por escadas. Na prática, os telhados eram as ruas e, com tempo "
            "bom, talvez uma praça, onde mais tarde se ergueram fornos comunitários. Dentro, paredes e plataformas eram "
            "rebocadas até ficarem lisas, e os cômodos eram mantidos impecavelmente limpos: o lixo ia para montes do lado "
            "de fora. Os mortos ficavam dentro do povoado, em covas sob o chão, sob as lareiras, as plataformas e as camas. "
            "Para renovar uma casa, demolia-se parte dela e construía-se a nova sobre o entulho, e assim o morro foi "
            "crescendo. As primeiras estimativas falavam em 5 mil a 7 mil habitantes, mas trabalhos mais recentes "
            "calculam de 600 a 800 pessoas num ano típico da fase intermediária. Também não se acharam casas que indiquem "
            "realeza ou hierarquia religiosa, e homens e mulheres parecem ter tido nutrição e status semelhantes."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Çatalhöyük",
            "is a tell (a mounded accretion resulting from long-term human settlement) of a very large Neolithic and Chalcolithic proto-city settlement in southern Anatolia, which existed from around 7500 BC to 5600 BC and flourished around 7000 BC. "
            "Çatalhöyük overlooks the Konya Plain [...] "
            "Initial estimates suggested an average population of between 5,000 and 7,000. "
            "However, more recent work using revised ideas of the distribution of residential buildings, and employing archaeological and ethnographic data exploring building use, suggests that between 600 and 800 people would have lived at Çatalhöyük East during an average year during the Middle phase (6700–6500 BC). [...] "
            "The inhabitants lived in mudbrick houses that were crammed together in an aggregate structure. "
            "No footpaths or streets were used between the dwellings, which were clustered in a honeycomb-like maze. "
            "Most were accessed by holes in the ceiling and doors on the side of the houses, with doors reached by ladders and stairs. "
            "The rooftops were effectively streets. "
            "The ceiling openings also served as the only source of ventilation [...] "
            "All interior walls and platforms were plastered to a smooth finish. [...] "
            "All rooms were kept scrupulously clean. "
            "Archaeologists identified very little rubbish in the buildings, finding middens outside the ruins [...] "
            "In good weather, many daily activities may also have taken place on the rooftops, which may have formed a plaza. "
            "In later periods, large communal ovens appear to have been built on these rooftops. "
            "Over time, houses were renewed by partial demolition and rebuilding on a foundation of rubble, which was how the mound was gradually built up. [...] "
            "As a part of ritual life, the people of Çatalhöyük buried their dead within the village. "
            "Human remains have been found in pits beneath the floors and especially beneath hearths, the platforms within the main rooms, and beds. [...] "
            "Çatalhöyük has strong evidence of an egalitarian society, as no houses with distinctive features (belonging to royalty or religious hierarchy for example) have been found so far. "
            "The most recent investigations also reveal little social distinction based on gender, with men and women receiving equivalent nutrition and seeming to have equal social status",
            nome="Çatalhöyük")],
    },
    # 16 a Lista dos Reis Sumérios e seus reinados de dezenas de milhares de anos
    {
        "temas_secundarios": ["mitologia", "calendarios"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "Segundo a Lista dos Reis Sumérios, oito reis governaram antes do dilúvio por um total de 241.200 anos. A lista servia de propaganda política, e a única rainha citada nela aparece como \"a taberneira\".",
        "explicacao": (
            "A lista é uma composição em sumério que enumera cidades, os reis que as governaram e a duração de cada "
            "reinado. Provavelmente foi criada e reescrita para legitimar as pretensões de poder de cidades e reinos do "
            "sul da Mesopotâmia no fim do terceiro milênio e no início do segundo milênio a.C. A versão mais antiga "
            "conhecida é do período de Ur III. Numa parte que nem toda cópia traz, a lista diz que a realeza desceu do céu "
            "para Eridu e enumera oito reis em cinco cidades, com reinados de 28.800 a 43.200 anos, até que \"o dilúvio "
            "varreu\" a terra. Depois do dilúvio, a realeza vai para Kish, cujos 23 reis governam de 300 a 1.500 anos "
            "cada; Mashda, por exemplo, teria reinado 840 anos. Durante boa parte do século XX, muitos estudiosos usaram "
            "a lista como fonte histórica importante. Hoje, a parte anterior a Sargão da Acádia é considerada ficcional, "
            "povoada de personagens míticos com reinados de centenas de anos, embora alguns desses reis apareçam em "
            "inscrições da época. No meio da lista há uma dinastia de Kish com uma só governante, Kug-Bau, \"a "
            "taberneira\", provavelmente a única rainha registrada nela. E o próprio Sargão aparece como copeiro de um "
            "rei de Kish antes de fundar a sua dinastia."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Sumerian_King_List",
            "is an ancient literary composition written in Sumerian that was likely created and redacted to legitimize the claims to power of various city-states and kingdoms in southern Mesopotamia during the late third and early second millennium BC. "
            "It does so by repetitively listing Sumerian cities, the kings that ruled there, and the lengths of their reigns. "
            "Especially in the early part of the list, these reigns often span thousands of years. "
            "In the oldest known version, dated to the Ur III period [...] "
            "This section, which is not present in every copy of the text, opens with the line \"After the kingship descended from heaven, the kingship was in Eridu.\" [...] "
            "This first section lists eight kings who ruled over five cities [...] "
            "In this first section, the reigns vary between 43,200 and 28,800 years for a total of 241,200 years. "
            "The section ends with the line \"Then the flood swept over\". [...] "
            "the section goes on to list 23 kings of Kish, who ruled between 1500 and 300 years for a total of 24,510 years. [...] "
            "\"Mashda, the son of Atab, ruled for 840 years\" [...] "
            "The following third dynasty of Kish consists of a single ruler Kug-Bau (\"the woman tavern keeper\"), thought to be the only queen listed in the Sumerian King List. [...] "
            "Sargon of Akkad is mentioned in the Sumerian King List as cup-bearer to Ur-zababa of Kish, and he defeated Lugal-zage-si of Uruk before founding his own dynasty. [...] "
            "During much of the 20th century, many scholars accepted the Sumerian King List as a historical source of great importance [...] "
            "Thus, in the absence of independent sources from the Early Dynastic period itself, the pre-Sargonic part of the SKL must be considered fictional. "
            "Many of the rulers in the pre-Sargonic part (i.e. prior to Sargon of Akkad) of the list must therefore be considered as purely fictional or mythological characters to which reigns of hundreds of years were assigned. "
            "However, there is a small group of pre-Sargonic rulers in the SKL whose names have been attested in Early Dynastic inscriptions.",
            nome="Sumerian King List")],
    },
]
