LOTE = "2026-11-17-microbiologia-01"
AREA = "biologia"
TEMA = "microbiologia"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None):
    return {"url": W + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": "en", "trecho": trecho}


CANDIDATOS = [
    # 1
    {
        "temas_secundarios": ["geologia_profunda"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Bem abaixo dos nossos pés vivem micróbios com tão pouca energia que uma única célula pode passar milhares de anos sem se dividir.",
        "explicacao": (
            "Durante muito tempo se achou que a vida acabava poucos metros abaixo do solo e do fundo do mar. "
            "Perfurações em minas, poços e sedimentos oceânicos mostraram o contrário: bactérias e arqueias "
            "ocupam rochas e sedimentos profundos, num ambiente escuro, muitas vezes quente e quase sem alimento. "
            "Com tão pouca energia disponível, esses micróbios vivem num ritmo extremamente lento: o metabolismo "
            "pode ser até um milhão de vezes mais devagar do que o dos micróbios da superfície. Em vez de crescer "
            "e se multiplicar, eles basicamente se mantêm vivos. Por isso uma célula pode levar milhares de anos "
            "para se dividir, e ninguém sabe qual é a idade máxima que elas podem atingir. Apesar de invisível, "
            "esse mundo subterrâneo é enorme: o subsolo concentra cerca de 90% da biomassa de bactérias e arqueias "
            "do planeta, algo como 15% de toda a biosfera da Terra."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Deep_biosphere",
            "There is very little energy at greater depths, so metabolisms are up to a million times slower than at the surface. "
            "Cells may live for thousands of years before dividing and there is no known limit to their age. "
            "The subsurface accounts for about 90% of the biomass across two domains of life, Archaea and Bacteria, "
            "and approximately 15% of the Earth's total biosphere.")],
    },
    # 2
    {
        "temas_secundarios": ["vida_marinha", "atmosfera"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "O ser fotossintetizante provavelmente mais abundante da Terra é uma bactéria marinha minúscula que a ciência só descobriu em 1986.",
        "explicacao": (
            "A Prochlorococcus é uma cianobactéria que vive nas camadas iluminadas dos oceanos tropicais e "
            "subtropicais. Ela mede menos de um milésimo de milímetro e é o menor organismo fotossintetizante "
            "conhecido. Justamente por ser tão pequena, passou despercebida: só foi identificada em 1986, pela "
            "oceanógrafa Sallie (Penny) Chisholm e colegas, quando já existiam satélites, computadores e "
            "décadas de biologia marinha. O tamanho reduzido é uma vantagem em águas pobres em nutrientes, "
            "porque uma célula pequena tem muita superfície em relação ao volume e capta melhor o pouco que há. "
            "O resultado é uma população astronômica de células, a ponto de ela ser provavelmente o organismo "
            "fotossintetizante mais abundante do planeta. As estimativas indicam que ela responde por uma fatia "
            "grande do oxigênio produzido por fotossíntese no mundo, entre 13% e 48% conforme o estudo. Ou seja, "
            "uma parte importante do ar que respiramos vem de um ser que ninguém conhecia até 1986."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Prochlorococcus",
            "These bacteria belong to the photosynthetic picoplankton and are probably the most abundant photosynthetic organism on Earth. [...] "
            "Prochlorococcus was discovered in 1986 by Sallie W. [...] "
            "Prochlorococcus is the smallest at just 0.5 to 0.7 micrometres in diameter. [...] "
            "The bacterium accounts for an estimated 13–48% of the global photosynthetic production of oxygen")],
    },
    # 3
    {
        "temas_secundarios": ["oceanografia"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Existem mais vírus que atacam bactérias do que todos os seres vivos da Terra somados, e no mar eles matam uma fatia enorme dos micróbios todo dia.",
        "explicacao": (
            "Os bacteriófagos, ou simplesmente fagos, são vírus que infectam bactérias. Eles injetam seu material "
            "genético na célula, fazem dela uma fábrica de cópias e, em muitos casos, a rompem para liberar a nova "
            "geração. Estima-se que existam mais de 10³¹ fagos no planeta, um número maior do que o de todos os "
            "organismos vivos juntos, bactérias incluídas. Nos oceanos o efeito é especialmente forte: calcula-se "
            "que os vírus marinhos matem cerca de 20% da biomassa de micro-organismos a cada dia. Isso tem um "
            "efeito inesperado na cadeia alimentar. Quando as bactérias se rompem, suas moléculas orgânicas ficam "
            "soltas na água e alimentam novas bactérias e algas, num processo chamado de desvio viral. Em vez de "
            "subir na cadeia alimentar até peixes, parte do carbono gira em círculos entre micróbios. Os vírus, "
            "que costumamos ver só como causadores de doença, são uma das engrenagens que regulam a vida no mar."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Bacteriophage",
                 "It is estimated there are more than 1031 bacteriophages on the planet, more than every living organism on Earth, including bacteria, combined."),
            wiki("Marine_bacteriophage",
                 "In a process known as the viral shunt, organic molecules released from dead bacterial cells stimulate fresh bacterial and algal growth. [...] "
                 "It is estimated marine viruses kill 20% of the microorganism biomass every day."),
        ],
    },
    # 4
    {
        "temas_secundarios": ["doencas_infecciosas"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "O primeiro vírus gigante conhecido foi confundido com uma bactéria por mais de dez anos: era tão grande que aparecia no microscópio comum.",
        "explicacao": (
            "Em 1992, pesquisadores que investigavam a doença dos legionários encontraram, dentro de amebas, um "
            "micro-organismo que parecia uma bactéria. Ele era grande o bastante para ser visto num microscópio "
            "óptico e até reagia à coloração de Gram, um teste clássico para bactérias. Recebeu o nome de "
            "Bradfordcoccus, em referência à cidade inglesa de Bradford, de onde vinha a ameba. Só em 2003 uma "
            "equipe de Marselha mostrou, num artigo na revista Science, que aquilo era um vírus. Ganhou então o "
            "nome de mimivírus, de 'micróbio imitador'. A descoberta desmontou uma ideia antiga: a de que vírus "
            "são, por definição, pequenos demais para o microscópio comum. O mimivírus tem um capsídeo de cerca "
            "de 400 nanômetros e um genoma enorme para um vírus. Depois dele foram encontrados vírus ainda "
            "maiores, e a pergunta sobre onde termina um vírus e começa uma célula ficou bem mais complicada."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Mimivirus",
            "APMV was discovered accidentally in 1992 within the amoeba Acanthamoeba polyphaga, after which it is named, during research into legionellosis by researchers from Marseille and Leeds. "
            "The virus was observed in a Gram stain and mistakenly thought to be a Gram-positive bacterium. "
            "As a consequence it was named Bradfordcoccus, after Bradford, England, where the amoeba had originated. "
            "In 2003, researchers at the Université de la Méditerranée in Marseille, France, published a paper in Science identifying the micro-organism as a virus. [...] "
            "Mimivirus has a capsid diameter of 400 nm.")],
    },
    # 5
    {
        "temas_secundarios": [],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Até vírus pegam vírus: o Sputnik, achado em 2008 numa torre de resfriamento de Paris, só se reproduz parasitando um vírus gigante.",
        "explicacao": (
            "Vírus não se reproduzem sozinhos: precisam invadir uma célula e usar a maquinaria dela. O Sputnik "
            "leva essa dependência um passo adiante. Ele só consegue se multiplicar dentro de amebas que já "
            "estejam infectadas por um vírus gigante, e aproveita as estruturas que esse vírus monta dentro da "
            "célula para fazer suas próprias cópias. No processo, atrapalha a replicação do vírus gigante. Por "
            "isso foi chamado de virófago, por analogia com bacteriófago, o vírus que ataca bactérias. Quando foi "
            "encontrado em 2008, na água de uma torre de resfriamento em Paris, era o primeiro vírus satélite "
            "conhecido que agia como parasita do vírus de que depende. A descoberta reforçou o debate sobre se os "
            "vírus gigantes estão mais perto de seres vivos do que se pensava, já que eles também podem 'ficar "
            "doentes'. Desde então, outros virófagos foram encontrados em lagos e oceanos."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Sputnik_virophage",
            "Sputnik uses the helper virus's machinery for reproduction and inhibits replication of the helper virus. [...] "
            "At its discovery in a Paris water-cooling tower in 2008, Sputnik was the first known satellite virus that inhibited replication of its helper virus and thus acted as a parasite of that virus.",
            "Sputnik virophage")],
    },
    # 6
    {
        "temas_secundarios": ["fisica_particulas", "animais_extremos"],
        "tipos_espanto": ["escala_absurda", "engenhosidade"],
        "gancho": "A bactéria Deinococcus radiodurans resiste a uma dose de radiação mil vezes maior que a capaz de matar uma pessoa, remontando o próprio DNA estilhaçado.",
        "explicacao": (
            "A Deinococcus radiodurans foi descoberta em 1956 de um jeito curioso: uma lata de carne "
            "tinha sido irradiada com uma dose que deveria matar qualquer forma de vida conhecida, mas a carne "
            "estragou mesmo assim. A culpada era essa bactéria. Hoje se sabe que ela aguenta 5.000 grays de "
            "radiação quase sem perdas, enquanto 5 grays podem matar um ser humano. A radiação não deixa de "
            "danificá-la: uma dose dessas quebra o DNA dela em dezenas de pontos. O truque está no conserto. "
            "Cada célula guarda várias cópias do próprio genoma, e as cópias servem de molde para remontar os "
            "pedaços na ordem certa. Por essa resistência fora do comum, ganhou o apelido de 'Conan, a "
            "Bactéria' e já esteve no Guinness como a forma de vida mais resistente à radiação."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Deinococcus_radiodurans",
            "D. radiodurans was discovered in 1956 by Arthur Anderson [...] "
            "A tin of meat was exposed to a dose of radiation that was thought to kill all known forms of life, but the meat subsequently spoiled [...] "
            "Deinococcus radiodurans is capable of withstanding an acute dose of 5,000 grays (Gy), or 500,000 rad, of ionizing radiation with almost no loss of viability, "
            "and an acute dose of 12,000 grays with 10% survivability. [...] "
            "5 Gy can kill a human")],
    },
    # 7
    {
        "temas_secundarios": ["evolucao", "historia_medicina"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "O artigo que defendia que nossas mitocôndrias já foram bactérias livres foi recusado por cerca de quinze revistas científicas antes de sair, em 1967.",
        "explicacao": (
            "As mitocôndrias são as estruturas que produzem a maior parte da energia das nossas células. Elas "
            "têm DNA próprio, se dividem por conta própria e lembram bactérias em vários detalhes. A bióloga "
            "Lynn Margulis defendeu que isso não era coincidência: mitocôndrias e cloroplastos (as estruturas da "
            "fotossíntese nas plantas) seriam descendentes de bactérias que, há muito tempo, passaram a viver "
            "dentro de outras células e nunca mais saíram. O artigo em que ela apresentou a ideia foi rejeitado "
            "por cerca de quinze revistas antes de ser publicado, em 1967. Mesmo depois disso, a proposta foi "
            "praticamente ignorada por mais uma década. Ela só se tornou amplamente aceita quando a genética "
            "permitiu comparar o DNA dessas estruturas com o de bactérias e confirmou o parentesco. Hoje a "
            "origem bacteriana das mitocôndrias está nos livros didáticos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Lynn_Margulis",
            "her formative paper, \"On the Origin of Mitosing Cells\", appeared in 1967 after being rejected by about fifteen journals. [...] "
            "her theory that cell organelles such as mitochondria and chloroplasts were once independent bacteria was largely ignored for another decade, "
            "becoming widely accepted only after it was powerfully substantiated through genetic evidence.")],
    },
    # 8
    {
        "temas_secundarios": [],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Existe bactéria visível a olho nu: filamentos de até 2 centímetros, achados em folhas de mangue no Caribe e descritos só em 2022.",
        "explicacao": (
            "Bactérias costumam medir alguns milésimos de milímetro, e por isso é preciso um microscópio para "
            "vê-las. A Thiomargarita magnifica quebra essa regra. Ela forma filamentos com média de um centímetro "
            "de comprimento, e alguns chegam a dois centímetros, tamanho comparável ao de um cílio. Foi encontrada "
            "presa a folhas caídas de mangue-vermelho, debaixo d'água, no arquipélago de Guadalupe, nas Antilhas. "
            "A descrição formal saiu em 2022. Uma célula desse tamanho tem um problema: a difusão de substâncias "
            "dentro dela fica lenta demais. A Thiomargarita contorna isso com uma organização interna incomum para "
            "bactérias, com o material genético guardado em compartimentos envoltos por membrana espalhados pela "
            "célula. A descoberta mostra que ainda há surpresas grandes, literalmente, no mundo microbiano."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Thiomargarita_magnifica",
            "found growing underwater on detached leaves of red mangroves from the Guadeloupe archipelago in the Lesser Antilles. [...] "
            "These filament-shaped bacteria are the largest known, with an average length of 1 cm, and some individuals reaching 2 centimetres (0.79 in), "
            "making the bacteria visible to humans by unaided eye. [...] The bacterium was described formally in a 2022 publication.",
            "Thiomargarita magnifica")],
    },
    # 9
    {
        "temas_secundarios": ["historia_medicina", "doencas_infecciosas"],
        "tipos_espanto": ["historia_humana", "mito_desmentido"],
        "gancho": "Para provar que uma bactéria causava gastrite e úlceras, o médico Barry Marshall bebeu uma cultura dela. A ideia acabou premiada com o Nobel.",
        "explicacao": (
            "Durante décadas, a medicina tratou a úlcera péptica como resultado de estresse, comida apimentada e "
            "excesso de ácido. Os australianos Robin Warren e Barry Marshall defenderam outra "
            "explicação: a bactéria Helicobacter pylori, que vive no estômago. A ideia enfrentou resistência, e em "
            "1984 as tentativas de infectar leitões para demonstrá-la falharam. Marshall então fez o teste em si mesmo. "
            "Depois de um exame de endoscopia, bebeu um caldo com a bactéria cultivada, esperando desenvolver "
            "uma úlcera talvez anos depois. Em poucos dias teve náusea, mau hálito e vômitos, e uma nova "
            "endoscopia mostrou inflamação intensa do estômago, com a bactéria instalada ali. Ele não chegou a ter "
            "úlcera, mas a gastrite reforçou a tese. Com o tempo, ficou claro que tratar a infecção com antibiótico "
            "curava muitas úlceras. Em 2005, Marshall e Warren receberam o Nobel de Medicina."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Barry_Marshall",
            "challenging decades of medical doctrine holding that ulcers were caused primarily by stress, spicy foods, and too much acid. [...] "
            "After failed attempts to infect piglets in 1984, Marshall had a baseline endoscopy done before drinking a broth containing cultured H. pylori, "
            "with the expectation of developing an ulcer as many as years later. [...] "
            "In 2005, the Karolinska Institute in Stockholm awarded the Nobel Prize in Physiology or Medicine to Marshall and Robin Warren")],
    },
    # 10
    {
        "temas_secundarios": ["eletromagnetismo"],
        "tipos_espanto": ["engenhosidade", "escala_absurda"],
        "gancho": "No lodo do fundo de rios e mares vivem bactérias que formam fios elétricos vivos, levando corrente por mais de um centímetro.",
        "explicacao": (
            "As bactérias-cabo são filamentos formados por milhares de células enfileiradas, que dividem uma "
            "mesma membrana externa. Elas resolvem um problema de logística. No sedimento, o alimento (sulfeto) "
            "fica nas camadas mais fundas, enquanto o oxigênio, de que precisam para 'respirar', só existe perto da "
            "superfície. Em vez de uma célula ter acesso aos dois, o filamento inteiro trabalha como um fio: as "
            "células de baixo retiram elétrons do sulfeto e esses elétrons viajam ao longo de fibras condutoras "
            "internas até as células de cima, onde são entregues ao oxigênio. É uma corrente elétrica biológica "
            "percorrendo mais de um centímetro, uma distância enorme na escala de uma bactéria. E elas podem ser "
            "muitas: em sedimentos já foram medidos até 2 quilômetros de filamento sob cada centímetro quadrado "
            "de superfície."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Cable_bacteria",
            "Cable bacteria are filamentous bacteria that conduct electricity across distances over 1 cm in sediment and groundwater aquifers. [...] "
            "Within a 15 cm thick top layer of sediment, cable bacteria densities reaching up to 2 km per square centimeter of surface were observed.")],
    },
    # 11
    {
        "temas_secundarios": ["vida_marinha", "luz_cores"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Uma lula do Havaí usa bactérias luminosas para apagar a própria sombra à noite, e toda manhã expulsa cerca de 90% delas.",
        "explicacao": (
            "A lula-de-cauda-curta-havaiana caça à noite em águas rasas. Vista de baixo contra o luar, sua "
            "silhueta denunciaria sua posição aos predadores. Para evitar isso, ela abriga na barriga um órgão "
            "de luz colonizado pela bactéria Aliivibrio fischeri, que é bioluminescente. A lula regula a "
            "intensidade dessa luz para imitar a claridade que vem da superfície, e assim praticamente apaga a "
            "própria sombra, uma camuflagem chamada contrailuminação. As bactérias também têm seu truque: só "
            "brilham quando estão em grande número, porque cada uma libera uma molécula sinalizadora e a luz "
            "liga quando a concentração dessa molécula passa de um limite. Esse sistema virou o modelo clássico "
            "de quorum sensing, a 'contagem' de população entre bactérias. Toda manhã a lula expele cerca de 90% "
            "das bactérias, e as restantes se multiplicam de novo até a noite seguinte."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Aliivibrio_fischeri",
            "The organ luminesces at night, providing the squid with counter-illumination camouflage. [...] "
            "This strategy prevents the squid from casting a shadow on the ocean floor, helping it avoid predation during feeding. "
            "The A. fischeri population is maintained by daily cycles. About 90% of A. fischeri are ejected by the squid every morning in a process known as \"venting\". [...] "
            "This system is the model system for Quorum Sensing as a general concept.",
            "Aliivibrio fischeri")],
    },
    # 12
    {
        "temas_secundarios": ["insetos", "doencas_infecciosas"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "Uma bactéria que manipula a reprodução de insetos, chegando a matar os machos ainda larvas, virou arma contra a dengue, inclusive no Brasil.",
        "explicacao": (
            "A Wolbachia vive dentro das células de muitos insetos e é transmitida de mãe para filhos pelos ovos. "
            "Como só as fêmeas a passam adiante, ela evoluiu formas de favorecê-las: em algumas espécies, os "
            "machos infectados morrem ainda na fase de larva; em outras, os machos se desenvolvem como fêmeas. "
            "Ela é tão comum que é considerada possivelmente a bactéria parasita da reprodução mais difundida da "
            "biosfera. O interesse médico veio de outra propriedade: algumas linhagens dificultam a replicação de "
            "vírus como o da dengue dentro do mosquito Aedes aegypti. O World Mosquito Program passou a soltar "
            "mosquitos com Wolbachia para que ela se espalhe pela população local. Num ensaio controlado em "
            "Yogyakarta, na Indonésia, os casos de dengue caíram 77% em relação às áreas de controle. No Brasil, "
            "houve solturas em Niterói entre 2017 e 2019, e a Fiocruz passou a apoiar a expansão do método."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Wolbachia",
            "is possibly the most widespread reproductive parasite bacterium in the biosphere. [...] "
            "Male killing, which occurs when infected males die during larval development, which increases the rate of born, infected females. "
            "Feminization, which results in infected males that develop as females or infertile pseudofemales. [...] "
            "some Wolbachia strains are able to directly reduce viral replication inside the insect. [...] "
            "the trial showed a 77% reduction in dengue cases compared to the control areas. [...] "
            "In 2017–2019, WMP released mosquitos in Niterói, Brazil.")],
    },
    # 13
    {
        "temas_secundarios": ["genetica", "evolucao"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Um domínio inteiro da vida passou despercebido até 1977: as arqueias eram tratadas como bactérias até Carl Woese comparar o RNA delas.",
        "explicacao": (
            "Durante boa parte do século 20, todos os micróbios sem núcleo foram classificados num só grupo, o "
            "das bactérias, com base na forma, na química e no metabolismo. Parecia natural: vistos ao microscópio, "
            "eles são muito parecidos. O microbiologista Carl Woese decidiu olhar para outra coisa, um pedaço de RNA "
            "presente nos ribossomos de todas as células, que muda devagar ao longo da evolução e serve como uma "
            "espécie de relógio de parentesco. Em 1977, ele e George Fox mostraram que alguns desses micróbios eram "
            "tão diferentes das bactérias quanto das plantas e dos animais. Nascia o domínio Archaea, ao lado de "
            "Bacteria e Eukarya. A técnica de comparar esse RNA revolucionou a microbiologia e permitiu "
            "classificar micróbios que nem conseguimos cultivar em laboratório."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Carl_Woese",
            "Woese defined the Archaea (a new domain of life) in 1977 through a pioneering phylogenetic taxonomy of 16S ribosomal RNA, a technique that has revolutionized microbiology. [...] "
            "For much of the 20th century, prokaryotes were regarded as a single group of organisms and classified based on their biochemistry, morphology and metabolism.",
            "Carl Woese")],
    },
    # 14
    {
        "temas_secundarios": ["evolucao", "geologia_profunda"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Animais, plantas e fungos parecem ter surgido de dentro de um grupo de arqueias batizado com nomes de deuses nórdicos, como Loki.",
        "explicacao": (
            "Todos os seres com células de núcleo definido, de fungos a seres humanos, formam o grupo dos "
            "eucariotos. De onde eles vieram é uma das grandes perguntas da biologia. Em 2015, uma equipe liderada "
            "pela Universidade de Uppsala analisou DNA retirado de sedimentos do fundo do Ártico, perto de um campo "
            "de fontes hidrotermais chamado Castelo de Loki, e encontrou arqueias com genes típicos de eucariotos. O "
            "grupo foi batizado de Lokiarchaeota, e parentes descobertos depois ganharam nomes como Thor, Odin e "
            "Heimdall, formando o grupo chamado Asgard. As análises indicam que os eucariotos surgiram de dentro "
            "desse grupo, perto do ramo Heimdall. Se isso se confirmar, a árvore da vida teria dois grandes troncos, "
            "bactérias e arqueias, e nós seríamos um galho das arqueias. Os detalhes ainda são debatidos."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [wiki("Asgard_(archaea)",
            "It appears that the eukaryotes, the domain that contains the animals, plants, fungi and protists, emerged within the Promethearchaeati, in a branch containing the \"Heimdallarchaeia\". "
            "This supports the two-domain system of classification over the three-domain system. [...] "
            "In 2015, an Uppsala University-led team proposed the \"Lokiarchaeota\" phylum",
            "Asgard (archaea)")],
    },
    # 15
    {
        "temas_secundarios": ["clima_tempo", "plantas"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "Proteínas de bactérias que vivem em folhas são usadas para fabricar neve artificial, porque fazem a água congelar em temperaturas bem mais altas.",
        "explicacao": (
            "Água pura pode continuar líquida bem abaixo de zero: sem nada em que o gelo comece a se formar, ela "
            "só congela por volta de 40 graus negativos. Na natureza, partículas de poeira e fuligem servem de "
            "semente para os cristais, mas algumas bactérias fazem isso muito melhor. Elas têm proteínas na "
            "superfície que organizam as moléculas de água no formato do gelo, e com isso a água congela entre 0 e "
            "10 graus negativos. Muitas dessas bactérias são parasitas de plantas: congelar o tecido da folha "
            "provoca lesões que as ajudam a se alimentar. Estações de esqui aproveitam o efeito, usando proteínas "
            "dessas bactérias para fabricar neve com mais facilidade. Há ainda uma hipótese mais ousada, a da "
            "bioprecipitação, proposta nos anos 1970: essas bactérias, levadas ao céu pelo vento, ajudariam a "
            "formar chuva e neve. O tamanho desse papel ainda está em estudo."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Bioprecipitation",
            "Bioprecipitation is the concept of rain-making bacteria and was proposed by David Sands from Montana State University in the 1970s. [...] "
            "biological ice nuclei are capable of catalyzing freezing at much warmer temperatures. "
            "The ice-nucleating bacteria currently known are mostly plant pathogens. [...] "
            "Ice-nucleating proteins derived from ice-nucleating bacteria are used for snowmaking. [...] "
            "Certain species of bacteria and fungi are known to act as efficient biological ice nuclei at temperatures between −10 and 0 °C. "
            "Without ice nuclear agents, to freeze water the temperature has to be at least −40 °C.")],
    },
    # 16
    {
        "temas_secundarios": ["geologia_profunda", "paleontologia"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Micróbios enterrados em sedimentos do fundo do mar desde a época dos dinossauros voltaram a se alimentar e se multiplicar em laboratório.",
        "explicacao": (
            "Em 2020, a revista Nature Communications publicou um experimento com sedimentos "
            "retirados do Giro do Pacífico Sul, uma das regiões mais pobres em nutrientes do oceano. As camadas "
            "analisadas tinham entre 4,3 e 101,5 milhões de anos, ou seja, as mais antigas vinham da época dos "
            "dinossauros. Os pesquisadores ofereceram aos micróbios dormentes ali dentro alimento marcado com "
            "isótopos, para poder rastrear quem o absorvia. A maioria das células analisadas incorporou o "
            "alimento, e em 68 dias de incubação o número de células chegou a crescer quatro ordens de grandeza. "
            "Mesmo na amostra mais antiga, a parte da comunidade que voltou à atividade ficou entre 39,6% e "
            "99,1% da população original, conforme o método de cálculo. Não se sabe se as mesmas células "
            "passaram todo esse tempo vivas ou se houve divisões raríssimas ao longo das eras. Mas o resultado "
            "mostra que, com energia mínima, a vida microbiana pode esperar por escalas de tempo geológicas."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": "https://www.nature.com/articles/s41467-020-17330-1",
             "titulo": "Aerobic microbial life persists in oxic marine sediment as old as 101.5 million years (Nature Communications, 2020)",
             "idioma": "en",
             "trecho": "Published: 28 July 2020 [...] Here we show that diverse aerobic members of communities in SPG sediments (4.3‒101.5 Ma) are capable of readily incorporating carbon and nitrogen substrates and dividing. [...] "
                       "Many cells responded rapidly to incubation conditions, increasing total numbers by 4 orders of magnitude and taking up labeled carbon and nitrogen within 68 days after incubation. [...] "
                       "Even in the sample of oldest sediment (U1365 9H-3, 101.5 Ma13), the revivable heterotrophic population was 39.6–99.1% of the original community."},
        ],
    },
]
