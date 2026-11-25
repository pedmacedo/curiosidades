LOTE = "2026-11-24-europa_medieval-01"
AREA = "historia_antiga"
TEMA = "europa_medieval"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


SPYROU = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9217749/fullTextXML"
PASTEUR = "https://pasteur.fr/en/node/17588"
NATURE_MA = "https://www.nature.com/articles/s41586-024-08496-5"
BIORXIV_MA = "https://www.biorxiv.org/content/10.1101/2023.03.14.532615v1.full"


CANDIDATOS = [
    # 1 a Peste Negra começou num vale do Quirguistão
    {
        "temas_secundarios": ["doencas_infecciosas", "genetica"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Lápides de 1338 e 1339 num vale do Quirguistão citam uma \"pestilência\". Em 2022, o DNA desses mortos revelou a bactéria da peste, numa cepa que seria a ancestral das que causaram a Peste Negra.",
        "explicacao": (
            "Os dois cemitérios ficam no vale do Chüy, perto do lago Issyk-Kul, e foram escavados entre 1885 e 1892. "
            "As lápides, com inscrições em siríaco, registram o nome do morto, o ano e muitas vezes a causa da morte, "
            "e mostram um número desproporcional de enterros em 1338 e 1339, alguns atribuídos a uma pestilência não "
            "especificada. Num artigo publicado em 2022, pesquisadores extraíram DNA dos dentes de sete pessoas "
            "enterradas ali e acharam a Yersinia pestis, a bactéria da peste. Os dois genomas reconstruídos são de uma "
            "única cepa, situada na raiz de uma grande diversificação da bactéria associada ao início da pandemia. "
            "Comparada às cepas atuais dos reservatórios da região do Tian Shan, onde a bactéria vive sobretudo em "
            "marmotas e seus parasitas, ela aponta para um surgimento local. Era uma região de comunidades diversas, "
            "que viviam do comércio e tinham ligações com várias partes da Eurásia. O início da Peste Negra costuma ser "
            "associado a surtos em volta do mar Negro em 1346, oito anos depois. Nem todos leem os achados do mesmo "
            "jeito: para o historiador John Norris, o surto de Issyk-Kul foi pequeno e esporádico, sem grande alcance."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": SPYROU, "titulo": "The source of the Black Death in fourteenth-century central Eurasia (Spyrou et al., Nature, 2022)",
             "idioma": "en",
             "trecho": "These sites are thought to have housed victims of a fourteenth-century epidemic as tombstone inscriptions directly dated to 1338–1339 state ‘pestilence’ as the cause of death for the buried individuals [...] "
                       "Here we report ancient DNA data from seven individuals exhumed from two of these cemeteries, Kara-Djigach and Burana. "
                       "Our synthesis of archaeological, historical and ancient genomic data shows a clear involvement of the plague bacterium [...] "
                       "genomes represent a single strain and are identified as the most recent common ancestor of a major diversification commonly associated with the pandemic’s emergence, here dated to the first half of the fourteenth century. "
                       "Comparisons with present-day diversity from [...] reservoirs in the extended Tian Shan region support a local emergence of the recovered ancient strain. [...] "
                       "Excavations of these cemeteries between 1885 and 1892 revealed a unique archaeological assemblage [...] "
                       "these cemeteries showed a disproportionally high number of burials dating between 1338 and 1339, with some inscriptions stating that the cause of death was due to an unspecified pestilence [...] "
                       "we found that the Chüy Valley housed ethnically diverse communities that relied on trade and maintained connections with several regions across Eurasia [...] "
                       "most extant 0.ANT strains have been isolated from marmots and their ectoparasites known to be the primary [...] "
                       "The onset of the Black Death has been conventionally associated with outbreaks that occurred around the Black Sea region in 1346 (refs. [...] eight years after the Kara-Djigach epidemic."},
            wiki("Black_Death",
                "In 2022, in an article called \"The source of the Black Death in fourteenth-century central Eurasia\", researchers pointed to the earliest victims of the plague found at two cemeteries in the Chüy Valley near Lake Issyk-Kul in modern Kyrgyzstan. "
                "Here graves had tombstones with Syriac inscription, providing the name of the deceased, year of death and often the cause of death, showing a spike due to \"pestilence\" in 1338–1339. "
                "The article reported DNA data to provide genetic evidence from the teeth of seven individuals from the two cemeteries at Kara-Djigach and Burana finding evidence of Yersinia pestis. [...] "
                "According to John Norris, evidence from Issyk-Kul indicates a small sporadic outbreak characteristic of transmission from rodents to humans with no wide-scale effect.",
                nome="Black Death"),
        ],
    },
    # 2 a peste moldou nossos genes imunes? estudo e contestação
    {
        "temas_secundarios": ["genetica", "sistema_imunologico", "evolucao"],
        "tipos_espanto": ["misterio_aberto", "conexao_inesperada"],
        "gancho": "Um estudo de 2022 concluiu que a Peste Negra favoreceu genes de defesa, como o ERAP2, hoje ligados a doenças autoimunes. Em 2025, outros geneticistas contestaram os números. A questão segue em aberto.",
        "explicacao": (
            "O estudo, publicado na Nature, comparou DNA antigo de pessoas que morreram pouco antes, durante e depois "
            "da Peste Negra em Londres, além de restos de cinco lugares da Dinamarca. Os autores apontaram quatro genes "
            "envolvidos na defesa contra patógenos, com destaque para o ERAP2: quem tinha duas cópias da versão "
            "funcional teria sobrevivido muito mais, com uma chance estimada de 40% a 50% maior. Em laboratório, células "
            "de defesa com a versão funcional neutralizavam a bactéria da peste com mais eficiência. O que chamou "
            "atenção é que esses mesmos genes estão hoje associados a mais risco de doenças autoimunes, como a doença de "
            "Crohn e a artrite reumatoide: o que salvou numa época poderia prejudicar em outra. Em fevereiro de 2025, a "
            "própria Nature publicou a contestação de outro grupo. Segundo ele, o sinal nos genes imunes desaparece com "
            "um teste estatístico adequado, um erro técnico na estimativa das frequências tira os quatro genes dos "
            "critérios do próprio estudo, e não há mudança significativa na variante do ERAP2. Os críticos admitem que "
            "é plausível que a peste tenha selecionado genes imunes, mas dizem que ainda não se sabe com que força nem "
            "quais."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "hipotese",
        "fontes": [
            {"url": PASTEUR, "titulo": "The Black Death shaped the evolution of immunity genes (Institut Pasteur, 2022)", "idioma": "en",
             "trecho": "Their study was published on Wednesday October 19, 2022, in the journal Nature. [...] "
                       "They screened ancient DNA samples extracted from the remains of individuals who had died before, during or after the Black Death in London, where there are several particularly well preserved, well dated cemeteries. "
                       "Additional samples were taken from human remains buried in five other locations across Denmark. [...] "
                       "Four genes under selection were identified, all of which are involved in the production of proteins that defend our systems from pathogens. [...] "
                       "Individuals with two identical copies of a functional gene, known as ERAP2, survived the pandemic at a much higher rate than those with non-functional versions of ERAP2. "
                       "Researchers estimate that people with the ERAP2 protective functional allele (the good copy of the gene) were 40 to 50 per cent more likely to survive than those who did not. [...] "
                       "copies of the ERAP2 gene allowed for more efficient neutralization of Y. pestis by immune cells. [...] "
                       "The same genes that once conferred protection against the Black Death are today associated with an increased susceptibility to autoimmune diseases such as Crohn's and rheumatoid arthritis. [...] "
                       "what enabled people to survive in one era may have a negative impact on survival in another"},
            {"url": NATURE_MA, "titulo": "Insufficient evidence for natural selection associated with the Black Death (Nature, Matters Arising, 2025)", "idioma": "en",
             "trecho": "Published: 19 February 2025 [...] "
                       "Klunk et al.1 analysed ancient DNA from before, during and after the Black Death, and claimed that large allele frequency changes at immune genes in aggregate, and at four specific variants, reflected natural selection. "
                       "These claims are unsupported for four reasons. "
                       "First, the enrichment in immune genes disappears if an appropriate randomization test is carried out; second, after correcting an error in the estimation of allele frequencies, none of the four reported loci pass the original filtering thresholds; [...] "
                       "Finally, we find no evidence of significant change in frequency of the ERAP2 variant rs2549794"},
            {"url": BIORXIV_MA, "titulo": "Insufficient evidence for natural selection associated with the Black Death (bioRxiv, 2023)", "idioma": "en",
             "trecho": "While it remains plausible that immune genes were subject to natural selection during the Black Death, the magnitude of this selection and which specific genes may have been affected remains unknown."},
        ],
    },
    # 3 a lei que tentou congelar salários depois da peste
    {
        "temas_secundarios": ["economia_curiosa", "leis_julgamentos", "doencas_infecciosas"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "A Peste Negra matou de 30% a 40% dos britânicos e deixou faltar mão de obra. Em 1351, o Parlamento inglês reagiu com uma lei que tabelava salários no nível de antes da peste e prendia quem recusasse trabalho.",
        "explicacao": (
            "Com tanta gente morta, quem sobrou para trabalhar a terra ganhou poder de barganha e passou a exigir "
            "pagamentos maiores, o que também alimentou a inflação. A elite reclamou da mudança. Primeiro veio uma "
            "ordenança do rei Eduardo III, em 1349, e depois o Estatuto dos Trabalhadores, de 1351, aprovado pelo "
            "Parlamento. O texto da lei registra a queixa: os servos se recusavam a servir a não ser por pagamentos "
            "duas ou três vezes maiores que os de antes. A resposta foi um teto: os salários deviam voltar aos valores "
            "de 1346, com preços fixados para lavradores, pastores, ceifeiros e debulhadores. Quem tivesse corpo "
            "capaz, menos de 68 anos e nada de que viver era obrigado a servir a quem o chamasse, sob pena de prisão. "
            "A lei também limitava o deslocamento em busca de condições melhores. A versão mais difundida "
            "diz que ela foi mal aplicada e não impediu a alta dos salários reais, mas há um porém: logo depois da "
            "peste, os salários reais não subiram, apesar da falta de braços. O estatuto foi uma das causas da "
            "Revolta dos Camponeses de 1381."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Statute_of_Labourers_1351",
            "The Statute of Labourers (25 Edw. 3. Stat. 2) was an act of the Parliament of England under King Edward III in 1351 in response to a labour shortage, which aimed at regulating the labour force by prohibiting requesting or offering a wage higher than pre-Plague standards and limiting movement in search of better conditions. "
            "The popular narrative about its success and enforcement holds that it was poorly enforced and did not stop the rise in real wages. "
            "However, immediately after the Black Death, real wages did not rise, despite the labour shortage. [...] "
            "The Black Death, a pandemic of bubonic plague, killed more than one-third of the population of Europe and 30–40% of the population in Britain and caused a dramatic decrease in the supply of labour. [...] "
            "Labourers had increased bargaining power and commanded higher wages. The increase in labour cost also led to inflation throughout the economy. "
            "The elite class lamented the sudden shift in economic power. "
            "In an attempt to control labour costs and price levels, Edward III issued the Ordinance of Labourers 1349 (23 Edw. 3). "
            "Parliament attempted to reinforce the Ordinance with the Statute of Labourers. "
            "It was one of the causes, among others, of the Peasants' Revolt in 1381. [...] "
            "The statute set a maximum wage for labourers that was commensurate with wages paid before the Black Death, specifically, in the year 1346. [...] "
            "That every person, able in body and under the age of 68 years, not having enough to live upon, being required, shall be bound to serve him that doth require him, or else be committed to gaol [...] "
            "unless they have livery and wages double or treble of what they were wont to take in the twentieth year and earlier [...] "
            "Item that carters, ploughmen, drivers of ploughs, shepherds, swineherds, day men, and all other servants shall take the liveries and wages accustomed in the twentieth year [...] "
            "and reapers of corn in the first week of August 2 d [...] "
            "Item that none take for the threshing of a quarter of wheat or rye over 2½ d",
            nome="Statute of Labourers 1351")],
    },
    # 4 536, o ano em que o Sol ficou fraco
    {
        "temas_secundarios": ["mudancas_climaticas", "vulcoes_terremotos", "doencas_infecciosas"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "Em 536, o Sol brilhou fraco e azulado por meses, e o verão europeu esfriou até 2,5 °C. Eram erupções vulcânicas. Um historiador chamou o ano de começo de um dos piores períodos para se estar vivo, se não o pior ano.",
        "explicacao": (
            "No começo de 536, ou talvez no fim de 535, uma erupção lançou na atmosfera uma grande quantidade de "
            "aerossóis de sulfato, que barraram parte da luz do Sol. Hoje se sabe que houve pelo menos três erupções, "
            "e de onde vieram ainda é incerto. Em março de 536, Constantinopla já via o céu escurecido. O historiador "
            "Procópio escreveu que o Sol dava luz sem brilho, como num eclipse. O estadista romano Cassiodoro descreveu "
            "raios fracos e azulados, sombras que sumiam ao meio-dia e geadas na colheita que endureciam maçãs e "
            "azedavam uvas. Anais irlandeses registraram falta de pão, e textos chineses falam de grande frio, fome e "
            "neve em agosto. Anéis de carvalhos irlandeses mostram crescimento anormalmente baixo em 536. Novas "
            "erupções, em 539 e 540, esfriaram o verão europeu em até 2,7 °C. Vieram quebras de safra, fome e a Peste "
            "de Justiniano, com milhões de mortes, e começou um período frio que durou de 536 a 660. A frase sobre o "
            "pior ano é do historiador Michael McCormick."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Volcanic_winter_of_536",
            "The volcanic winter was caused by at least three eruptions of uncertain origin, with several possible locations proposed in various continents. "
            "In early AD 536 (or possibly late 535), an eruption ejected great amounts of sulfate aerosols into the atmosphere, reducing the solar radiation reaching the Earth's surface and cooling the atmosphere for several years. "
            "In March 536, Constantinople began experiencing darkened skies and lower temperatures. "
            "Summer temperatures in 536 fell by as much as 2.5 °C (4.5 °F) below European normal. "
            "The lingering effect of the volcanic winter of 536 was augmented in the years 539 and 540, when another volcanic eruption caused summer temperatures to decline as much as 2.7 °C (4.9 °F) below European normal. [...] "
            "The volcanic eruptions caused crop failures, and were accompanied by the Plague of Justinian, famine, and millions of deaths and initiated the Late Antique Little Ice Age, which lasted from 536 to 660. "
            "Historian Michael McCormick has called the year 536 \"the beginning of one of the worst periods to be alive, if not the worst year.\" [...] "
            "For the sun gave forth its light without brightness... and it seemed exceedingly like the sun in eclipse [...] "
            "The sun's rays were weak, and they appeared a \"bluish\" colour. "
            "At noon, no shadows from people were visible on the ground. [...] "
            "Frosts during harvest, which made apples harden and grapes sour. [...] "
            "\"A failure of bread in AD 536\" – the Annals of Ulster [...] "
            "The Bei Shi (北史; History of the North), which mentions the \"great cold\" and \"famine\" that occurred in autumn 536. [...] "
            "Low temperatures, even snow during the summer (snow reportedly fell in August in China, which caused the harvest there to be delayed). [...] "
            "shows abnormally little growth in Irish oak in 536",
            nome="Volcanic winter of 536")],
    },
    # 5 Guédelon, o castelo do século XIII em obras desde 1997
    {
        "temas_secundarios": ["arquitetura", "grandes_obras"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Na França, um castelo é construído desde 1997 só com ferramentas, materiais e técnicas do século XIII. O que se reaprendeu nessa obra foi usado para reconstruir a Notre-Dame de Paris após o incêndio de 2019.",
        "explicacao": (
            "O castelo de Guédelon fica numa floresta perto de Treigny, a duas horas ao sul de Paris. É um projeto de "
            "arqueologia experimental: para entender a tecnologia da Idade Média, a obra usa só técnicas, ferramentas "
            "e até roupas da época, e a madeira e a pedra vêm do próprio local. O terreno, uma antiga pedreira de "
            "arenito no meio da mata, com um lago perto, foi escolhido justamente porque transportar materiais era "
            "caro na Idade Média. O projeto segue o modelo de castelo desenvolvido nos séculos XII e XIII sob o rei "
            "Filipe II da França. A obra começou sob o comando do empresário Michel Guyot, que restaurava as ruínas de "
            "outro castelo, o de Saint-Fargeau, a 13 km dali. A primeira pedra foi posta em 20 de junho de 1997. Em 1998, a muralha "
            "já tinha um metro de altura, e em 2010 a torre principal chegava a 15 metros. Entre as técnicas "
            "recuperadas estão os guindastes movidos por gente caminhando dentro de uma grande roda. Em 2014, o "
            "canteiro recebia cerca de 300 mil visitantes por ano e foi chamado de maior experimento arqueológico do "
            "mundo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Gu%C3%A9delon_Castle",
            "Guédelon Castle (French: Château de Guédelon [ʃɑto d(ə) ɡedlɔ̃]) is a castle under construction near Treigny, France. "
            "The castle is the focus of an experimental archaeology project aimed at recreating a 13th-century castle and its environment using period techniques, dress, and materials. "
            "In order to fully investigate the technology required in the medieval past, the project is using only period construction techniques, tools, and costumes. "
            "Materials, including wood and stone, are all obtained locally. "
            "Jacques Moulin, chief architect for the project, designed the castle according to the architectural model developed during the 12th and 13th centuries by Philip II of France. "
            "Construction started in 1997 under Michel Guyot, owner of Château de Saint-Fargeau, a castle in Saint-Fargeau 13 kilometres (8.1 mi) away. "
            "The site was chosen according to the availability of construction materials: an abandoned stone quarry, in a large forest, with a nearby pond. [...] "
            "In 1979, French entrepreneur Michel Guyot purchased the ruins of the Château de Saint-Fargeau and began restoring it [...] "
            "A former sandstone quarry was chosen as the site of Guédelon Castle because of its relative elevation and abundance of local natural resources, which would have been expensive to transport in the Middle Ages. "
            "The castle location is in a woodland, two hours south of Paris, near Treigny. "
            "The ceremonial first stone was laid on 20 June 1997 [...] "
            "By 1998 the castle perimeter had been built up to a metre (3 ¼ feet) in height, following which Guédelon was opened to the public. "
            "By June 2010, the great tower stood at 15 metres (49 ft). "
            "By 2014, the castle was attracting about 300,000 visitors annually [...] "
            "The techniques redeveloped for Guédelon Castle were used in the reconstruction of Notre-Dame cathedral in Paris after its catastrophic 2019 fire. [...] "
            "the project was described as \"the world's biggest archaeological experiment\". [...] "
            "explored the use of medieval treadmill cranes in its construction.",
            nome="Guédelon Castle")],
    },
    # 6 a Tapeçaria de Bayeux é um bordado e escapou de Himmler
    {
        "temas_secundarios": ["pintura", "segunda_guerra"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "A Tapeçaria de Bayeux nem é tapeçaria: é um bordado de quase 70 metros. Na Segunda Guerra, Himmler a cobiçou, e a SS foi buscá-la no Louvre quando o museu já estava de novo em mãos francesas.",
        "explicacao": (
            "Numa tapeçaria verdadeira, a imagem é tecida no próprio pano. Na de Bayeux, as figuras foram bordadas "
            "com fio de lã sobre um linho grosso, com quatro tipos de ponto e dez cores de tintas naturais. Ela tem "
            "cerca de 50 centímetros de altura e conta, em 58 cenas, os fatos que levaram à conquista normanda da "
            "Inglaterra e à Batalha de Hastings, em 1066. Há 623 figuras humanas, 994 animais e 41 navios e barcos, "
            "além da primeira imagem conhecida do cometa Halley. As cenas finais se perderam. Em geral se acredita que "
            "foi encomendada pelo bispo Odo de Bayeux, meio-irmão de Guilherme, o Conquistador, e feita na Inglaterra "
            "nos anos seguintes à conquista. Durante a ocupação alemã da França, Heinrich Himmler a considerava "
            "importante para a história germânica. Em 27 de junho de 1944, a Gestapo a levou ao Louvre, e em 18 de "
            "agosto Himmler mandou transferi-la para \"um lugar seguro\", provavelmente Berlim, numa mensagem "
            "interceptada em Bletchley Park. A SS só tentou pegá-la em 22 de agosto, tarde demais. Em setembro de "
            "2026, a obra saiu da França pela primeira vez, emprestada ao Museu Britânico."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Bayeux_Tapestry",
            "The Bayeux Tapestry (French: Tapisserie de Bayeux) is an embroidered cloth nearly 70 metres (230 feet) long and 50 centimetres (20 inches) tall that depicts the events leading up to the Norman conquest of England, led by William, Duke of Normandy, and the Battle of Hastings in 1066. [...] "
            "Despite its name, the work is technically an embroidery rather than a true tapestry, since the images are stitched rather than woven into the fabric. "
            "It was worked in wool thread on a coarse linen ground using four different stitches and ten natural dye colours. "
            "The cloth now consists of 58 scenes, all with Medieval Latin tituli. "
            "The surviving piece depicts 623 human figures, 994 animals, 438 plants, 37 buildings and fortifications, 41 ships and boats [...] "
            "The final scenes are missing. [...] "
            "It is generally thought to have been commissioned by Bishop Odo of Bayeux, William's half-brother who appears four times, and produced in England in the years following the Conquest. [...] "
            "In September 2026 the tapestry travelled outside France for the first time in its history, on loan to the British Museum [...] "
            "The picture of Halley's Comet, which appears in the upper border at (scene 32), is also the first known picture of this comet. [...] "
            "during the German occupation of France and the Normandy landings. "
            "During the war Heinrich Himmler coveted the work, regarding it as \"important for our glorious and cultured Germanic history\". [...] "
            "On 27 June 1944 the Gestapo took the tapestry to the Louvre, and on 18 August, three days before the Wehrmacht withdrew from Paris, Himmler sent a message (intercepted by Bletchley Park) ordering it to be taken to \"a place of safety\", thought to be Berlin. "
            "It was only on 22 August that the SS attempted to take possession of the tapestry, by which time the Louvre was again in French hands.",
            nome="Bayeux Tapestry")],
    },
    # 7 o Domesday de 1086 e o Domesday digital de 1986
    {
        "temas_secundarios": ["historia_computacao", "telecomunicacoes"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "O Domesday Book, levantamento da Inglaterra de 1086, ainda está guardado e legível. Sua versão digital, feita pela BBC em 1986 em laserdiscs, preocupava já em 2002: quase não sobravam máquinas para lê-la.",
        "explicacao": (
            "Em 1085, Guilherme, o Conquistador, mandou agentes a cada condado para listar terras, gente, gado e o que "
            "cada propriedade rendia ao seu senhor, e o colofão do livro diz que o levantamento terminou em 1086. O "
            "manuscrito em pergaminho está hoje nos Arquivos Nacionais, em Kew, Londres. O nome é uma alusão ao Juízo "
            "Final: por volta de 1179, Richard FitzNeal escreveu que as decisões do livro eram inalteráveis, como as "
            "do Juízo Final, e que sua sentença não podia ser anulada. Para os 900 anos, a BBC e parceiros criaram um novo Domesday multimídia, publicado em "
            "1986, com textos sobre a vida local escritos sobretudo por crianças de mais de 9 mil escolas, além de "
            "mapas, fotos, vídeos e o censo de 1981. Tudo foi gravado em laserdiscs adaptados, que só funcionavam num "
            "computador BBC Master ligado a um toca-discos especial da Philips. Em 2002, surgiu o temor de que os "
            "discos ficassem ilegíveis, porque computadores e leitores capazes de usá-los tinham ficado raros. Um "
            "projeto das universidades de Leeds e de Michigan conseguiu resgatar o conteúdo por emulação. O caso virou "
            "exemplo clássico de obsolescência digital."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("BBC_Domesday_Project",
                "The BBC Domesday Project was a partnership between Acorn Computers, Philips, Logica, and the BBC (with some funding from the European Commission's ESPRIT programme) to mark the 900th anniversary of the original Domesday Book, an 11th-century census of England. "
                "It has been cited as an example of digital obsolescence on account of the physical medium used for data storage. "
                "This new multimedia edition of Domesday was compiled between 1984 and 1986 and published in 1986. "
                "It included a new \"survey\" of the United Kingdom, in which people, mostly school children, wrote about geography, history or social issues in their local area or just about their daily lives. "
                "This was linked with maps, and many colour photos, statistical data, video and \"virtual walks\". "
                "The project also incorporated professionally prepared video footage, virtual reality tours of major landmarks and other prepared datasets such as the 1981 census. "
                "Over a million people participated in the project, including children from more than 9,000 schools. [...] "
                "The project was stored on adapted LaserDiscs [...] "
                "Viewing the discs required the BBC Master AIV, a Acorn BBC Master computer expanded with a SCSI controller and the 65C102 \"Turbo\" co-processor - which controlled a Philips VP415 LaserVision laserdisc player. [...] "
                "In 2002, concerns emerged over the potential unreadablility of the discs as computers capable of reading the format became rare and drives capable of accessing the discs even rarer. [...] "
                "the CAMiLEON project (a partnership between the University of Leeds and University of Michigan, led by Margaret Hedstrom and managed by researcher Paul Wheatley) had developed a system capable of accessing the discs using emulation techniques.",
                nome="BBC Domesday Project"),
            wiki("Domesday_Book",
                "at the behest of William the Conqueror [...] "
                "The Anglo-Saxon Chronicle states that in 1085 the king sent his agents to survey every shire in England, to list his holdings and dues owed to him. [...] "
                "The survey's main purpose was to record the annual value of every piece of landed property to its lord, and the resources in land, labour force, and livestock from which the value derived. [...] "
                "Richard FitzNeal wrote in the Dialogus de Scaccario (c. 1179) that the book was so called because its decisions were unalterable, like those of the Last Judgment, and its sentence could not be quashed. "
                "The manuscript is now held at the National Archives in Kew, London. [...] "
                "the book's colophon states the survey was completed in 1086. [...] "
                "copied out by one person on parchment (prepared sheepskin)",
                nome="Domesday Book"),
        ],
    },
    # 8 os gansos que nasceriam de cracas
    {
        "temas_secundarios": ["comportamento_animal", "vida_marinha", "revolucao_cientifica"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Na Idade Média, corria que certos gansos nasciam de cracas presas em madeira à deriva no mar. O imperador Frederico II mandou buscar essas madeiras no norte para examinar e concluiu que era lenda.",
        "explicacao": (
            "As cracas-pescoço-de-ganso, presas a troncos boiando, têm um pedúnculo comprido que lembra o pescoço de "
            "uma ave, e o ganso-de-faces-brancas nunca era visto fazendo ninho na Europa. A lenda juntou as duas "
            "coisas. Por volta de 1188, o clérigo Geraldo de Gales escreveu que essas aves nasciam em madeira de "
            "pinheiro à deriva, cresciam presas pelo bico dentro de conchas e um dia caíam na água ou voavam, e "
            "garantiu ter visto com os próprios olhos mais de mil embriões pendurados num só pedaço de madeira. Os "
            "bestiários, copiados em mosteiros, espalharam a história. Frederico II, imperador e estudioso de aves, "
            "fez o contrário: no tratado sobre caça com aves que escreveu por volta de 1241, contou que enviou "
            "emissários ao norte para trazer as tais madeiras e que as formações parecidas com conchas não lembravam em "
            "nada o corpo de uma ave. Para ele, a lenda nasceu porque esses gansos se reproduzem em lugares tão "
            "remotos que ninguém sabia onde faziam ninho. Só no fim do século XIX se mostrou que eles migram para se "
            "reproduzir na Groenlândia ou no norte da Escandinávia. Conta-se ainda que o papa Inocêncio III proibiu, "
            "em 1215, comer esses gansos na Quaresma como se não fossem carne, mas as atas do concílio não registram "
            "essa proibição."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Barnacle_goose_myth",
            "The barnacle goose myth is a widely reported historical misconception about the breeding habits of the barnacle goose (Branta leucopsis) and brant goose (Branta bernicla). "
            "One version of the myth is that these geese emerge fully formed from goose barnacles (Cirripedia). [...] "
            "The main vector for the myth into modern times was monastic manuscripts and in particular the bestiary. "
            "The myth owes its long-standing popularity to an early ignorance of the migration patterns of geese. [...] "
            "It was not until the late 19th century that bird migration research showed that such geese migrate northwards to nest and breed in Greenland or northern Scandinavia. [...] "
            "whilst in the curvature of its stalk they saw a resemblance to the long neck of the bird. [...] "
            "Topographia Hibernica, compiled by Gerald of Wales around 1188. [...] "
            "there are many birds called barnacles (bernacae) … nature produces them in a marvellous way for they are born at first in gum-like form from fir-wood adrift in the sea. "
            "Then they cling by their beaks like sea-wood, sticking to wood, enclosed in a shell-fish shells for freer development … thus in the process of time dressed in a firm clothing of feathers, they either fall into the waters or fly off into freedom of the air. [...] "
            "Holy Roman Emperor Frederick II   (1194–1250), an ornithologist and learned scholar, is best remembered  for his seminal work, De Arte Venandi cum Avibus (On the Art of Hunting With Birds). "
            "This book was written in Latin around the year 1241. [...] "
            "I have often seen with my own eyes more than a thousand minute embryos of birds of this species on the seashore, hanging from one piece of timber, covered with shells, and, already formed. [...] "
            "We have made prolonged research into the origin and truth of this legend and even sent special envoys to the north with order to bring back specimens of these mythical timbers for our inspection. "
            "When we examined them we did observe shell-like formations clinging to the rotten wood, but these bore no resemblance to any avian body. "
            "We therefor doubt the truth of this legend in the absence of corroborative evidence. "
            "In our opinion this superstition arose from the fact that barnacle geese breed in such remote latitudes that men in ignorance of their real nesting places invented this explanation. [...] "
            "considered it necessary in 1215 to prohibit the eating of barnacle geese in Lent [...] "
            "However the records of the 4th Lateran Council do not include reference to such a ban amongst any of its decisions.",
            nome="Barnacle goose myth")],
    },
    # 9 as varetas de contagem que incendiaram o Parlamento
    {
        "temas_secundarios": ["dinheiro", "economia_curiosa", "medidas_padroes"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Por séculos, o Tesouro inglês registrou impostos e dívidas em varetas de madeira entalhadas. Abolido o sistema, mandaram queimá-las em fornalhas do Parlamento, em 1834. O fogo escapou e destruiu quase todo o prédio.",
        "explicacao": (
            "O sistema foi introduzido na Inglaterra por Henrique I, por volta de 1100, numa época de pouca moeda. "
            "Cada valor virava um entalhe numa vareta de aveleira, e a largura do corte dizia o montante: a largura da "
            "palma da mão valia mil libras, a de um polegar, cem, a do dedo mínimo, vinte, e um grão de cevada inchado "
            "marcava uma libra. Depois a vareta era rachada ao meio no sentido do comprimento, e cada parte ficava com "
            "uma metade. Como as irregularidades da madeira rachada só deixavam as duas metades originais se "
            "encaixarem, era quase impossível fraudar: um entalhe a mais numa metade não apareceria na outra. As "
            "varetas registravam impostos pagos, mas logo passaram a circular como \"dinheiro de madeira\", aceitas "
            "com desconto como pagamento. Em 1697, ajudaram a formar o Banco da Inglaterra, que trocou ações por "
            "varetas da dívida da Coroa. O Tesouro só abandonou o método em 1826. Em 1834, seis séculos de registros "
            "foram queimados em duas fornalhas do Parlamento, a chaminé pegou fogo e o incêndio se espalhou até "
            "destruir a maior parte do edifício. Charles Dickens contou o episódio num artigo de 1855."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Tally_stick",
            "The split tally became a prevalent technique in medieval Europe, a time characterised by a scarcity of coinage, to document bilateral exchanges and debts. "
            "Typically fashioned from squared hazelwood, the stick was inscribed with a series of notches before being split lengthwise. "
            "Each party in the transaction retained one half of the marked stick, both pieces bearing identical records. [...] "
            "The natural irregularities in the surfaces of the tallies where they were split would mean that only the original two halves would fit back together perfectly, and so would verify that they were matching halves of the same transaction. "
            "If one party tried to unilaterally change the value of his half of the tally stick by adding more notches, the absence of those notches would be apparent on the other party's tally stick. [...] "
            "when Henry I introduced the tally stick system in medieval England in around 1100. "
            "The tally sticks recorded a payment of taxes, but soon began to circulate in a secondary discount market, being accepted as payment for goods and services at a discount [...] "
            "and circulated as \"wooden money\". [...] "
            "At the top of the tally a cut is made, the thickness of the palm of the hand, to represent a thousand pounds; then a hundred pounds by a cut the breadth of a thumb; twenty pounds, the breadth of the little finger; a single pound, the width of a swollen barleycorn [...] "
            "Royal tallies (debt of the Crown) also played a role in the formation of the Bank of England at the end of the 17th century. "
            "In 1697, the bank issued £1 million worth of stock in exchange for £800,000 worth of tallies at par [...] "
            "The split tally of the Exchequer remained in continuous use in England until 1826 [...] "
            "In 1834, following the passing of 4 Will. 4. c .15, tally sticks representing six centuries' worth of financial records were ordered to be burned in two furnaces in the Houses of Parliament. "
            "The resulting fire set the chimney ablaze and then spread until most of the building was destroyed. "
            "This event was described by Charles Dickens in an 1855 article on administrative reform.",
            nome="Tally stick")],
    },
    # 10 os anacoretas, emparedados por vontade própria
    {
        "temas_secundarios": ["religioes", "costumes_rituais"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Na Idade Média, havia quem se fechasse para sempre numa cela colada à parede de uma igreja. Na entrada, rezava-se um rito parecido com um funeral, e a pessoa passava a ser tida como morta para o mundo.",
        "explicacao": (
            "Eram os anacoretas. Diferentemente dos eremitas, faziam voto de ficar num lugar só, e a cela costumava "
            "ser um cômodo simples encostado à igreja da aldeia. Em terras de língua germânica, desde pelo menos o "
            "século X, o bispo rezava o Ofício dos Mortos quando o recluso entrava, e às vezes, se a pessoa era "
            "emparedada, punha seu selo na parede. A cela tinha em geral no máximo 3,7 a 4,6 metros de lado e três "
            "janelinhas: uma dava para o altar, para acompanhar a missa e receber a comunhão; outra servia a quem "
            "trazia comida e levava os dejetos; a terceira deixava entrar luz. Pela janela, os anacoretas "
            "aconselhavam visitantes e ganhavam fama de sábios. O compromisso era tão sério que alguns se recusaram a "
            "sair nem quando piratas ou saqueadores atacaram a cidade, e morreram queimados quando a igreja foi "
            "incendiada. Na Inglaterra, chegaram a cerca de 200 no século XIII, e as mulheres eram maioria, às vezes "
            "quatro para cada homem. Uma delas, Juliana de Norwich, morta depois de 1416, escreveu o texto místico Revelações do Amor "
            "Divino. A tradição inglesa acabou com o fechamento dos mosteiros por Henrique VIII, entre 1536 e 1539."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Anchorite",
            "Anchorites are frequently considered to be a type of hermit, but unlike hermits, they were required to take a vow of stability of place, opting for permanent enclosure in cells often attached to churches. "
            "Also unlike hermits, anchorites were subject to a religious rite of consecration that closely resembled the funeral rite, following which they would be considered dead to the world and a type of living saint. [...] "
            "Their highest number—around 200 anchorites—was recorded in the 13th century. "
            "From the 12th to the 16th centuries, female anchorites consistently outnumbered their male counterparts, sometimes by as many as four to one in the 13th century. [...] "
            "Between 1536 and 1539, the dissolution of the monasteries ordered by Henry VIII of England effectively brought the anchorite tradition to an end in England. [...] "
            "They tended to be a simple cell (also called anchorhold) built against one of the walls of the local village church. "
            "In Germanic-speaking areas, from at least the tenth century it was customary for the bishop to say the Office of the Dead as the anchorite entered their cell, to signify the anchorite's death to the world [...] "
            "Sometimes, if the anchorite was walled up inside the cell, the bishop would put his seal upon the wall to stamp it with his authority. [...] "
            "Most anchorholds were small, perhaps at most 3.7 to 4.6 m (12 to 15 ft) square, with three windows. "
            "Viewing the altar, hearing Mass, and receiving the Eucharist were possible through one small, shuttered window in the common wall facing the sanctuary [...] "
            "Anchorites provided spiritual advice and counsel to visitors through these windows, gaining a reputation for wisdom. "
            "Another small window allowed access to those who saw to the anchorite's physical needs. "
            "A third window, often facing the street but covered with translucent cloth, allowed light into the cell. [...] "
            "Some refused to leave their cells even when pirates or looters were pillaging their towns and consequently burned to death when the church was torched. [...] "
            "providing food and water and removing waste. [...] "
            "Julian of Norwich (died after 1416) wrote the mystic text Revelations of Divine Love",
            nome="Anchorite")],
    },
    # 11 o relógio nasceu sino
    {
        "temas_secundarios": ["medidas_padroes", "palavras_viajantes", "invencoes"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "Os primeiros relógios mecânicos das torres da Europa muitas vezes não tinham mostrador nem ponteiros: só tocavam sino nas horas de oração. Por isso clock, relógio em inglês, vem de clocca, sino em latim medieval.",
        "explicacao": (
            "O avanço decisivo foi o escape de verga, um mecanismo que libera a força de um peso aos poucos e tornou "
            "possíveis os primeiros relógios mecânicos, por volta de 1300. Entre 1280 e 1320, os registros de igrejas "
            "passam a citar relógios com mais frequência, o que provavelmente indica a chegada desse novo tipo. Os "
            "relógios mais simples, feitos para avisar, ficavam em torres e anunciavam as horas canônicas, os "
            "horários de oração, que mudavam de duração conforme o nascer e o pôr do sol. Por isso dispensavam "
            "mostrador. O nome conta essa história: em inglês, clock vem do latim medieval clocca, sino, e tem "
            "parentes em várias línguas europeias, como o holandês médio clocke. Um exemplo que sobreviveu é o relógio "
            "da Catedral de Salisbury, na Inglaterra, de ferro forjado e sem mostrador, que se acredita ser de cerca de "
            "1386. Movido por dois grandes pesos de pedra, ele serve para tocar um sino na hora certa. É chamado de "
            "relógio mais antigo do mundo ainda funcionando, mas há dúvidas sobre a data, e outros relógios "
            "reivindicam o título."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Clock",
                "The word clock derives from the medieval Latin word for 'bell'—clocca—and has cognates in many European languages. [...] "
                "Middle Dutch clocke, all of which mean 'bell'. [...] "
                "In Europe, between 1280 and 1320, there was an increase in the number of references to clocks and horologes in church records, and this probably indicates that a ne [...] "
                "Simple clocks intended mainly for notification were installed in towers and did not always require faces or hands. "
                "They would have announced the canonical hours or intervals between set times of prayer. "
                "Canonical hours varied in length as the times of sunrise and sunset shifted. [...] "
                "A major advance occurred with the invention of the verge escapement, which made possible the first mechanical clocks around 1300 in Europe [...] "
                "This controlled release of power – the escapement – marks the beginning of the true mechanical clock",
                nome="Clock"),
            wiki("Salisbury_Cathedral_clock",
                "The Salisbury Cathedral clock is a large iron-framed tower clock without a dial, in Salisbury Cathedral, England. "
                "Thought to date from about 1386, it is a well-preserved example of the earliest type of mechanical clock, called verge and foliot clocks, and is said to be the oldest working clock in the world, although similar claims are made for other clocks. [...] "
                "Like many of these more practical devices, its main purpose was to strike a bell at precise times. "
                "It probably did not have a dial. "
                "The wheels and gears are mounted in a four-post wrought iron frame. [...] "
                "The power was supplied by two large stone weights. [...] "
                "There are some doubts that the clock displayed in Salisbury Cathedral is actually the clock mentioned in 1386",
                nome="Salisbury Cathedral clock"),
        ],
    },
    # 12 ninguém morria aos 30 na Idade Média
    {
        "temas_secundarios": ["desenvolvimento_humano", "probabilidade", "vieses_cognitivos"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "Não é verdade que, na Idade Média, adultos morriam por volta dos 30 ou 40 anos. A média era puxada para baixo pelas mortes de crianças: um homem de 21 anos na Inglaterra medieval podia esperar viver até os 64.",
        "explicacao": (
            "A confusão vem da expectativa de vida ao nascer, uma média que inclui todos os que morrem, até os bebês. "
            "Em todas as sociedades antes da era moderna, a idade em que mais gente morria era o primeiro ano de vida. "
            "Quando a mortalidade infantil é alta, essa média fica muito sensível às mortes dos primeiros anos e "
            "engana: numa sociedade com expectativa de vida ao nascer de 40 anos, poucos morrem exatamente aos 40, e a "
            "maioria morre antes dos 30 ou depois dos 55. Além da mortalidade infantil, mortes de jovens adultos por "
            "acidentes, epidemias, guerras e partos também baixavam a média. Por isso, demógrafos usam outras medidas, "
            "como a expectativa de vida aos 5 anos, que exclui o efeito das mortes de bebês. Numa sociedade com "
            "expectativa de vida de 30 anos ao nascer, ainda pode ser comum que uma criança de 5 anos tenha mais 40 "
            "anos pela frente. Ler a média ao nascer como idade típica de morte leva à ideia errada de que quase não "
            "havia velhos. No caso medieval, a conta para quem já era adulto era bem maior, como mostra o exemplo do "
            "homem inglês de 21 anos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("List_of_common_misconceptions_about_history",
                "Adults in the Middle Ages did not die in their 30s or 40s on average, as it is commonly inferred from the life expectancy of the time. "
                "While such an estimate was the life expectancy at birth, this was skewed by high infant and adolescent mortality. "
                "The life expectancy among adults was much higher; a 21-year-old man in medieval England, for example, could expect to live to the age of 64.",
                nome="List of common misconceptions about history"),
            wiki("Life_expectancy",
                "In all pre-modern societies the most common age at death is the first year of life [...] "
                "A combination of high infant mortality and deaths in young adulthood from accidents, epidemics, plagues, wars, and childbirth, before modern medicine was widely available, significantly lowers LEB. "
                "For example, a society with a LEB of 40 would have relatively few people dying at exactly 40: most will die before 30 or after 55. "
                "In populations with high infant mortality rates, LEB is highly sensitive to the rate of death in the first few years of life. "
                "Because of this sensitivity, LEB can be grossly misinterpreted, leading to the belief that a population with a low LEB would have a small proportion of older people. "
                "A different measure, such as life expectancy at age 5 (e5), can be used to exclude the effect of infant mortality [...] "
                "For instance, in a society with a life expectancy of 30, it may nevertheless be common to have a 40-year remaining timespan at age 5.",
                nome="Life expectancy"),
        ],
    },
    # 13 donzela de ferro e cinto de castidade não são medievais
    {
        "temas_secundarios": ["leis_julgamentos", "crimes_arte"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "Dois símbolos da \"Idade Média cruel\" não são da Idade Média: não há menção à donzela de ferro antes do século XIX, e muitos cintos de castidade de museus são hoje tidos como falsificações do século XIX.",
        "explicacao": (
            "A donzela de ferro, um armário de metal com espinhos por dentro, ficou famosa com o exemplar de "
            "Nuremberg, exposto talvez desde 1802 e destruído num bombardeio aliado em 1945. Alguns historiadores "
            "dizem que o escritor Johann Philipp Siebenkees inventou uma história para ela, com uma suposta execução "
            "de um falsificador de moedas em 1515. Um professor de história do direito defende que as donzelas de "
            "ferro foram montadas com peças achadas em museus, para criar objetos espetaculares de exibição. Com o "
            "cinto de castidade, a história é parecida. A lenda diz que as esposas dos cruzados o usavam, mas não há "
            "prova confiável de que existisse antes do século XV, mais de um século depois da última cruzada no "
            "Oriente Médio. A primeira descrição detalhada é um desenho num tratado militar de 1405, que pode ter sido "
            "uma piada. Os cintos expostos no Museu de Cluny, em Paris, no Museu Britânico e em Nuremberg foram em "
            "boa parte retirados de exibição porque sua autenticidade como peças medievais passou a ser questionada. "
            "O uso mais difundido veio no século XIX, em aparelhos médicos contra a masturbação."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Iron_maiden",
                "The iron maiden is an apocryphal torture device, believed to have been first invented in the 19th century. "
                "It consists of a solid iron cabinet with a hinged front and spike-covered interior, sufficiently tall to enclose a human being. "
                "While often popularly thought to have been used in the medieval period, there is no known mention of the iron maiden from before the 19th century. [...] "
                "Wolfgang Schild, a professor of criminal law, criminal law history, and philosophy of law at the Bielefeld University, has argued that putative iron maidens were pieced together from artifacts found in museums to create spectacular objects intended for (commercial) exhibition. [...] "
                "The most famous iron maiden that popularized the design was that of Nuremberg, first displayed possibly as far back as 1802. "
                "The original was lost in the Allied bombing of Nuremberg in 1945. [...] "
                "Some historians have argued that Johann Philipp Siebenkees (1759–1796) made up a history for the (imaginary) device. "
                "According to Siebenkees' colportage, it was first used on August 14, 1515, to execute a coin forger.",
                nome="Iron maiden"),
            wiki("Chastity_belt",
                "According to modern myths, the chastity belt was used as an anti-temptation device during the Crusades. [...] "
                "However, there is no credible evidence that chastity belts existed before the 15th century (over a century after the last Middle Eastern Crusade), and their main period of apparent use falls within the Renaissance rather than the Middle Ages. [...] "
                "they first became widely available in the form of 19th-century anti-masturbation medical devices. [...] "
                "The first detailed actual mention of what could be interpreted as \"chastity belts\" in the West is in Konrad Kyeser von Eichstätt's Bellifortis (1405), which describes the military technology of the era. [...] "
                "Polidoro argues that Kyeser's references are meant to be humorous or ironic [...] "
                "Two belts have been exhibited at the Musée de Cluny in Paris. [...] "
                "There are other such belts at the Germanisches Nationalmuseum in Nuremberg and the British Museum in London. "
                "Most have been removed from public display to avoid any further embarrassment because the authenticity of these belts as medieval devices has since been called into question. "
                "Many contemporary historians accept that these alleged \"artifacts\" date from the 19th century, and are thus inauthentic.",
                nome="Chastity belt"),
        ],
    },
]
