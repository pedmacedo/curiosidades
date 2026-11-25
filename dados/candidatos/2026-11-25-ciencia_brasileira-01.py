LOTE = "2026-11-25-ciencia_brasileira-01"
AREA = "brasil"
TEMA = "ciencia_brasileira"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 César Lattes, primeiro autor do píon, e o Nobel que foi só para Powell
    {
        "temas_secundarios": ["fisica_particulas", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "O curitibano César Lattes era o primeiro autor do artigo de 1947 que anunciou o píon, uma partícula subatômica nova. O Nobel de Física de 1950, ligado a essa descoberta, foi só para o chefe do grupo.",
        "explicacao": (
            "Lattes, filho de imigrantes italianos, formou-se em matemática e física na USP em 1943. Em 1946 foi "
            "para a Universidade de Bristol, na Inglaterra, juntar-se ao antigo professor Giuseppe Occhialini no "
            "grupo de Cecil Powell, que estudava raios cósmicos com emulsões fotográficas, chapas em que as "
            "partículas deixam rastros. Lattes melhorou a emulsão do grupo acrescentando mais boro. Em 1947, Lattes, "
            "Powell, Occhialini e Hugh Muirhead descobriram o píon, ou méson pi, e no mesmo ano mediram a massa da "
            "nova partícula. Para registrar mais rastros, Lattes levou chapas a uma estação meteorológica no alto "
            "do monte Chacaltaya, na Bolívia, a 5.200 metros. No ano seguinte, na Universidade da Califórnia em "
            "Berkeley, ele e Eugene Gardner detectaram píons fabricados num cíclotron, bombardeando átomos de "
            "carbono com partículas alfa. Mesmo assim, o Nobel de Física de 1950 foi dado apenas a Powell, pelo "
            "método fotográfico e pelas descobertas sobre mésons feitas com ele. De volta ao Brasil, Lattes ajudou "
            "a fundar o Centro Brasileiro de Pesquisas Físicas e esteve entre os articuladores do CNPq. Por isso, "
            "a Plataforma Lattes, o banco nacional de currículos de cientistas, leva o nome dele."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("César_Lattes",
            "also known as César Lattes, was a Brazilian experimental physicist, one of the discoverers of the pion, a subatomic particle composed of a quark and an antiquark. [...] "
            "Lattes was born to a family of Italian immigrants in Curitiba, Paraná, Brazil. [...] "
            "He proceeded to enroll in the University of São Paulo, graduating in 1943, in mathematics and physics. [...] "
            "He travelled to England arriving in February 1946, to join his teacher Occhialini who had arrived the previous year, to work in the group directed by Cecil Powell at the H. H. Wills Physics Laboratory of the University of Bristol. "
            "There, he improved on the nuclear emulsion used by Powell by adding more boron to it. "
            "In 1947, he collaborated with Powell, Occhialini and Hugh Muirhead in the experimental discovery of the pion (or pi meson). "
            "In the same year he, along Powell and Occhialini, determined the mass of the new particle. "
            "In April 1947 he visited a weather station on top of the 5,200-meter-high Chacaltaya mountain in Bolivia, using photographic plates to register rays and reveal more 'pion decay events'. "
            "A year later, working with Eugene H. Gardner (1913-1950) at UC Berkeley, Lattes was able to detect the artificial production of pions in the lab's cyclotron by bombarding carbon atoms with alpha particles. [...] "
            "He was considered one of the greatest scientific leaders of Brazilian Physics and was one of the main personalities behind the creation of the important Brazilian National Research Council (Conselho Nacional de Desenvolvimento Científico e Tecnológico). "
            "Due to his contribution in this process, the Brazilian national science database was named Lattes Platform after him. [...] "
            "Although he was the main researcher and the first author of the historical Nature article describing the pion, only Cecil Powell was awarded the Nobel Prize for Physics in 1950 for \"his development of the photographic method of studying nuclear processes and his discoveries regarding mesons made with this method\".",
            nome="César Lattes"),
            wiki("José_Leite_Lopes",
            "Together with César Lattes, a young physicist from São Paulo who had achieved international fame due to his co-discovery of a new kind of nuclear particle, the pion (pi-meson), Leite Lopes was instrumental in creating in January 1949, in Rio de Janeiro, the Centro Brasileiro de Pesquisas Físicas",
            nome="José Leite Lopes")],
    },
    # 2 processo Urca: neutrinos, estrelas e o cassino carioca
    {
        "temas_secundarios": ["estrelas", "jogos_azar"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "Um processo que ajuda a esfriar restos de estrelas, soltando neutrinos, tem nome de cassino carioca. Gamow e o brasileiro Mário Schenberg compararam a energia que some ali ao dinheiro dos apostadores na roleta da Urca.",
        "explicacao": (
            "Na astrofísica, chama-se processo Urca a reação em que um núcleo absorve um elétron e, depois, sofre "
            "decaimento beta, num ciclo que pode se repetir muitas vezes. A cada volta escapa um neutrino, partícula "
            "que quase nunca é reabsorvida e leva energia embora. Por isso o processo é tido como um mecanismo de "
            "resfriamento de anãs brancas e estrelas de nêutrons, os restos de estrelas que já gastaram seu "
            "combustível. A ideia foi discutida pela primeira vez pelo físico George Gamow e pelo brasileiro Mário "
            "Schenberg, nascido no Recife em 1914, quando visitavam o Cassino da Urca, no Rio de Janeiro. Na "
            "autobiografia, Gamow contou que o nome homenageava o cassino e também lembrava que a energia térmica "
            "some depressa do interior da estrela, como o dinheiro do bolso de quem jogava ali. Numa versão "
            "registrada no verbete de Schenberg, foi ele quem fez a comparação com a roleta. Gamow ainda notou que, "
            "no dialeto russo dele, \"urka\" pode significar ladrão. Schenberg também descreveu, com Subrahmanyan "
            "Chandrasekhar, em 1942, o limite de massa que leva o nome dos dois, e foi crítico de arte."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Urca_process",
                "an Urca process is a reaction which emits a neutrino and which is assumed to take part in cooling processes in neutron stars and white dwarfs. "
                "The process was first discussed by George Gamow and Mário Schenberg while they were visiting a casino named Cassino da Urca in Urca, Rio de Janeiro. "
                "Gamow wrote in his autobiography that the name was chosen in part to commemorate the gambling establishment where the two physicists had first met, and \"partially because the Urca Process results in a rapid disappearance of thermal energy from the interior of a star, similar to the rapid disappearance of money from the pockets of the gamblers on the Casino de Urca.\" "
                "In Gamow's South Russian dialect, urca (Russian: урка) can also mean a robber or gangster. [...] "
                "The Urca process is especially important in the cooling of white dwarfs, where a lepton (usually an electron) is absorbed by the nucleus of an ion and then convectively carried away from the core of a star. "
                "Then, a beta decay occurs. Convection then carries the element back into the interior of the star, and the cycle repeats many times. "
                "Because the neutrinos emitted during this process are unlikely to be reabsorbed, this is effectively a cooling mechanism for white dwarfs.",
                nome="Urca process"),
            wiki("Mário_Schenberg",
                "Schenberg was born on 2 July 1914 in Recife, Brazil as Mayer Schönberg. [...] "
                "George Gamow (1904–1968) was inspired to name the process Urca after the name of the Urca Casino in Rio de Janeiro, when Schönberg remarked to him that \"the energy disappears in the nucleus of the supernova as quickly as the money disappeared at that roulette table.\" [...] "
                "Together with Indian physicist Subrahmanyan Chandrasekhar (1910–1995), he discovered and published in 1942 the so-called Schönberg–Chandrasekhar limit, which is the maximum mass of the core of a star that can support the overlying layers against gravitational collapse once the core hydrogen is exhausted.",
                nome="Mário Schenberg"),
        ],
    },
    # 3 Leite Lopes e o bóson neutro de 1958
    {
        "temas_secundarios": ["fisica_particulas", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Em 1958, o físico recifense José Leite Lopes sugeriu que a força nuclear fraca era parente do eletromagnetismo e propôs um bóson neutro, o futuro Z0. Steven Weinberg o citou na palestra do Nobel de 1979.",
        "explicacao": (
            "Na época, as interações fracas, que comandam, por exemplo, a desintegração do nêutron, eram "
            "explicadas sem partículas intermediárias claras. Leite Lopes, que fez o doutorado em Princeton e "
            "trabalhou com Wolfgang Pauli, imaginou que essa força seria transmitida por bósons vetoriais e, como "
            "o fóton da luz também é vetorial, achou que as duas forças teriam \"um laço de família\". No artigo de "
            "1958, publicado na revista Nuclear Physics, igualou a constante da interação fraca à carga do elétron "
            "e propôs também um bóson neutro, que hoje se chama Z0. Segundo ele contou em entrevista, pouca gente "
            "leu o trabalho na época. A unificação das duas forças, a teoria eletrofraca, deu o Nobel de Física de "
            "1979 a Steven Weinberg, Sheldon Glashow e Abdus Salam. Na palestra do Nobel, Weinberg listou o artigo "
            "de Leite Lopes, ao lado de um de Sidney Bludman, entre as especulações de 1958 sobre as correntes "
            "neutras, que dependem do Z0. O bóson neutro só seria descoberto na década de 80. Leite Lopes ajudou a "
            "fundar o Centro Brasileiro de Pesquisas Físicas e, em 1969, teve os direitos políticos cassados pela "
            "ditadura e foi afastado do centro que havia criado."
        ),
        "nivel": 3, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("José_Leite_Lopes",
                "Prediction of the existence of neutral vectorial bosons (Z0 boson), in 1958, by devising an equation which showed the analogy of the weak nuclear interactions with electromagnetism. "
                "Steven Weinberg, Sheldon Glashow and Abdus Salam used later these results to develop the electroweak unification. "
                "They were awarded with the Nobel Prize of Physics in 1979. [...] "
                "In 1969, the new military regime in Brazil took away his political rights, together with several other professors, supposedly on the basis of his participation in a \"communist conspiracy\". "
                "He was dismissed summarily from the very Center he had created",
                nome="José Leite Lopes"),
            {"url": "https://revistapesquisa.fapesp.br/um-fisico-a-toda-prova/", "titulo": "Um físico a toda prova (Revista Pesquisa FAPESP)", "idioma": "pt",
             "trecho": "a predição de existência do bóson Z0, descoberto depois já na década de 80. São achados científicos de 1958. [...] "
                "trabalhei com Pauli sobre as forças nucleares, mas depois passei a estudar as interações fracas – aquelas que comandam a desintegração do nêutron em próton, elétron e neutrino [...] "
                "Aí eu imediatamente pensei que haveria bósons w+ w- que eram intermediários entre nêutron, próton, elétron e neutrino, e deviam ser vetoriais. "
                "Como o fóton da luz também é vetorial, achei que deviam ter um laço de família. [...] "
                "Fiz um trabalho em 1958 em que propus uma relação entre o bóson e o fóton, e a partir daí uma igualdade entre a interação fraca e a constante eletromagnética que é dada pela carga do elétron. [...] "
                "Propus no mesmo trabalho a existência de um bóson neutro, que hoje se chama Z0 (z-zero), que se devia buscar na interação de elétrons com nêutrons. [...] "
                "Mas pouca gente tinha lido meu trabalho, embora tivesse sido publicado na Nuclear Physics"},
            {"url": "https://www.nobelprize.org/uploads/2018/06/weinberg-lecture.pdf", "titulo": "Steven Weinberg, Conceptual foundations of the unified theory of weak and electromagnetic interactions (Nobel Lecture, 1979)", "idioma": "en",
             "trecho": "Of course, the possibility of neutral currents was nothing new. There had been speculations [35] about possible neutral currents as far back as 1937 by Gamow and Teller, Kemmer, and Wentzel, and again in 1958 by Bludman and Leite-Lopes. [...] "
                "Leite-Lopes, J. Nucl. Phys. 8, 234 (1958)."},
            wiki("José_Leite_Lopes",
                "Leite Lopes doutorou-se em física na Universidade de Princeton, orientado por Wolfgang Pauli.",
                nome="José Leite Lopes (pt)", idioma="pt"),
        ],
    },
    # 4 Nise da Silveira: punida por recusar eletrochoque, criou ateliês e chamou Jung
    {
        "temas_secundarios": ["consciencia", "pintura"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Por se recusar a aplicar eletrochoque, a psiquiatra Nise da Silveira foi mandada para a terapia ocupacional, setor desprezado pelos médicos. Lá abriu ateliês de pintura, e Carl Jung a incentivou a expor as obras.",
        "explicacao": (
            "Alagoana, Nise formou-se em 1926 na Faculdade de Medicina da Bahia, a única mulher numa turma de 157 "
            "homens. Denunciada por ter livros marxistas, ficou presa de 1936 a 1937, no Rio. Na prisão, "
            "conheceu Graciliano Ramos, que a pôs nas \"Memórias do Cárcere\". Quando voltou ao serviço "
            "público, em 1944, no hospital psiquiátrico do Engenho de Dentro, encontrou eletrochoques, coma "
            "induzido por insulina e lobotomia. Recusou-se a usá-los e foi transferida para a terapia ocupacional, "
            "que então se resumia a pôr os internos para limpar e consertar coisas. Em vez disso, abriu ateliês de "
            "pintura e modelagem. Em 1952, fundou o Museu de Imagens do Inconsciente, para guardar e estudar as "
            "obras. Intrigada com as mandalas que surgiam nas pinturas, escreveu a Jung em 1954. Ele a incentivou "
            "a expor os trabalhos num congresso de psiquiatria em Zurique, em 1957, e, ao visitar a mostra com "
            "ela, recomendou que estudasse mitologia para entendê-los. Nise também foi pioneira ao usar animais, "
            "como cães e gatos, que chamava de coterapeutas: a ideia veio de ver um paciente melhorar ao cuidar de "
            "uma cadela abandonada no hospital."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Nise_da_Silveira",
                "De 1921 a 1926 cursou a Faculdade de Medicina da Bahia, onde se formou como a única mulher entre os 157 homens daquela turma. [...] "
                "Durante a Intentona Comunista, foi denunciada por uma enfermeira pela posse de livros marxistas. "
                "Ficou presa entre 1936-1937 no presídio Frei Caneca. [...] "
                "Graciliano tornou-se seu grande amigo – fazendo de Nise um dos personagens do clássico Memórias do Cárcere, que narra justamente este momento. [...] "
                "Em 1944 foi reintegrada ao serviço público e iniciou seu trabalho no Centro Psiquiátrico Nacional Pedro II, no Engenho de Dentro, no Rio de Janeiro. [...] "
                "Ao se deparar com procedimentos como eletrochoques, coma insulínico e lobotomia, Nise da Silveira se rebelou. "
                "Por sua discordância com os métodos adotados nas enfermarias, recusando-se a aplicá-lo nos pacientes, foi transferida para o trabalho com terapia ocupacional, atividade então menosprezada pelos médicos. [...] "
                "No lugar das tradicionais tarefas de limpeza e manutenção que os pacientes exerciam sob o título de terapia ocupacional, ela criou ateliês de pintura e modelagem [...] "
                "Em 1952, ela fundou o Museu de Imagens do Inconsciente, no Rio de Janeiro, um centro de estudo e pesquisa destinado à preservação dos trabalhos produzidos nos estúdios de modelagem e pintura que criou na instituição [...] "
                "Ela percebeu essa possibilidade de tratamento ao observar como melhorou um paciente a quem delegara os cuidados de uma cadela abandonada no hospital [...] "
                "Ela expôs parte deste processo em seu livro \"Gatos, A Emoção de Lidar\", publicado em 1998. [...] "
                "Interessada em seu estudo sobre os mandalas, tema recorrente nas pinturas de seus pacientes, ela escreveu em 1954 a Carl Gustav Jung, iniciando uma proveitosa troca de correspondência. "
                "Jung a estimulou a apresentar uma mostra das obras de seus pacientes, que recebeu o nome \"A Arte e a Esquizofrenia\", ocupando cinco salas no \"II Congresso Internacional de Psiquiatria\", realizado em 1957, em Zurique, Suíça. "
                "Ao visitar com ela a exposição, ele a orientou a estudar mitologia como uma chave para a compreensão dos trabalhos criados pelos internos.",
                nome="Nise da Silveira (pt)", idioma="pt"),
            wiki("Nise_da_Silveira",
                "Nise da Silveira was born in Maceió, in the northeastern state of Alagoas, Brazil, in 1905. [...] "
                "She was also a pioneer in researching affective bonds between patients and animals, whom she referred to as co-therapists.",
                nome="Nise da Silveira"),
        ],
    },
    # 5 Rocha Lima e a bactéria batizada com dois mortos pelo tifo
    {
        "temas_secundarios": ["doencas_infecciosas", "primeira_guerra"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "A bactéria do tifo epidêmico homenageia dois cientistas que morreram da doença que estudavam. Quem a batizou foi o brasileiro Henrique da Rocha Lima, que também pegou tifo pesquisando-a, num campo de prisioneiros alemão.",
        "explicacao": (
            "Rocha Lima, carioca formado em medicina em 1905, foi um dos fundadores do Instituto Oswaldo Cruz e, a "
            "partir de 1909, dirigiu o departamento de patologia de um instituto de doenças tropicais em Hamburgo, "
            "na Alemanha. Durante a Primeira Guerra, ele e o colega Stanislaus von Prowazek estudavam o tifo "
            "epidêmico no hospital de um campo de prisioneiros de guerra em Cottbus, e os dois se infectaram. "
            "Prowazek morreu em 1915. Em 1916, Rocha Lima descreveu o micróbio causador da doença, transmitido "
            "pelas fezes de piolhos, e lhe deu o nome de Rickettsia prowazekii. A primeira parte homenageia o "
            "patologista americano Howard Taylor Ricketts, que em 1910 foi investigar um grande surto de tifo na "
            "Cidade do México e morreu da doença dias depois de isolar o organismo que julgava ser o causador. A "
            "segunda homenageia Prowazek. Rocha Lima sobreviveu, recebeu a Cruz de Ferro do Império Alemão e "
            "ajudou a fundar a Escola Paulista de Medicina e a Universidade de São Paulo. Em 2007, uma bactéria "
            "recebeu o nome dele: Bartonella rochalimae."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Rickettsia_prowazekii",
                "is the etiologic agent of epidemic typhus, transmitted in the feces of lice. [...] "
                "Henrique da Rocha Lima, a Brazilian doctor, discovered this bacterium in 1916. "
                "He named it after his colleague Stanislaus von Prowazek, who had died from typhus in 1915. "
                "Both Prowazek and Rocha Lima had been infected with typhus while studying its causative agent in a prisoner-of-war camp hospital in Cottbus, Germany.",
                nome="Rickettsia prowazekii"),
            wiki("Henrique_da_Rocha_Lima",
                "Henrique da Rocha Lima (24 November 1879 – 12 April 1956) was a Brazilian physician, pathologist and infectologist born in Rio de Janeiro. [...] "
                "Rocha Lima named the organism after Prowazek and American bacteriologist Howard Taylor Ricketts (1871-1910). "
                "Henrique da Rocha Lima received his M.D. degree from the Medical School of Rio de Janeiro in 1905. "
                "He was one of the founders of the Oswaldo Cruz Institute [...] "
                "and from 1909, as director of the department of pathology at the Institute for Maritime and Tropical Diseases in Hamburg. "
                "In Brazil, he was a scientific and educational leader, as he participated in the foundation of the Paulista School of Medicine, and of the University of São Paulo. [...] "
                "such as the Iron Cross of the German Empire [...] "
                "In 2007, a new strain of Gram-negative bacteria was named after Rocha Lima, Bartonella rochalimae.",
                nome="Henrique da Rocha Lima"),
            wiki("Howard_Taylor_Ricketts",
                "Howard Taylor Ricketts (February 9, 1871 – May 3, 1910) was an American pathologist [...] "
                "In 1910, Ricketts became interested in a strain of murine-carried typhus known as tabardillo due to a major outbreak in Mexico City, and the apparent similarity of the disease to spotted fever. "
                "Days after isolating the organism that he believed caused typhus, he himself died of the disease.",
                nome="Howard Taylor Ricketts"),
        ],
    },
    # 6 Kerr e as abelhas africanizadas que escaparam em Rio Claro
    {
        "temas_secundarios": ["insetos", "ecologia"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "As abelhas africanizadas, as \"assassinas\" que se espalharam da Argentina aos EUA, descendem de 26 enxames que escaparam em 1957 de um apiário de pesquisa em Rio Claro (SP). A ideia era ter abelhas que dessem mais mel.",
        "explicacao": (
            "O geneticista Warwick Kerr trouxe abelhas africanas ao Brasil em 1956 e passou a cruzá-las com "
            "abelhas europeias. Queria uma linhagem que produzisse mais mel no clima tropical do que as europeias "
            "usadas então nas Américas. As colmeias africanas, de temperamento especialmente defensivo, ficavam "
            "num apiário da universidade em Rio Claro e tinham telas que barravam a saída das rainhas e dos "
            "zangões, maiores que as operárias, para que não cruzassem com as abelhas da região. Segundo o relato "
            "de Kerr, em outubro de 1957 um apicultor de fora achou que as telas atrapalhavam as operárias e as "
            "tirou: 26 enxames escaparam. Eles se misturaram às colônias europeias locais, e o híbrido se espalhou "
            "pela América do Sul. Chegou à América do Norte em 1985, e as primeiras colônias permanentes entraram "
            "no Texas, vindas do México, em 1990. Em 2002, já ia do norte da Argentina a estados do sul dos EUA. "
            "Hoje a africanizada é a abelha preferida dos apicultores brasileiros e "
            "domina a apicultura na América Central e do Sul."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Africanized_bee",
                "The Africanized bee, also known as the Africanized honey bee (AHB) and colloquially as the \"killer bee\" [...] "
                "African honey bees were first introduced to Brazil in 1956 to increase honey production, but 26 swarms with their queens escaped from their experimental apiary in 1957. "
                "Since then, the hybrid has spread throughout South America and arrived in North America in 1985. [...] "
                "The Africanized honey bees in the Western Hemisphere are descended from hives operated by biologist Warwick E. Kerr, who had interbred honey bees from Europe and southern Africa. "
                "Kerr was attempting to breed a strain of bees that would produce more honey in tropical conditions than the European strain of honey bee then in use throughout North, Central, and South America. "
                "The hives containing this particular African subspecies were housed at an apiary in the São Paulo State University Rio Claro campus, in the southeast of Brazil, and were noted to be especially defensive. "
                "These hives had been fitted with special excluder screens (called queen excluders) to prevent the larger queen bees and drones from leaving and mating with the local European bee population. "
                "According to Kerr, in October 1957 a visiting beekeeper, noticing that the queen excluders were interfering with the worker bees' movement, removed them, resulting in the accidental release of 26 Tanganyikan swarms of A. m. scutellata. "
                "Following this accidental release, the Africanized honey bee swarms spread out and crossbred with local European honey bee colonies. [...] "
                "The first permanent colonies arrived in Texas from Mexico in 1990. [...] "
                "they have now become the dominant type of honey bee for beekeeping in Central and South America [...] "
                "As of 2002, the Africanized honey bees had spread from Brazil south to northern Argentina and north to Central America, Trinidad (the West Indies), Mexico, Texas, Arizona, Nevada, New Mexico, Florida, and southern California. [...] "
                "The Africanized honey bee is now considered the honey bee of choice for beekeeping in Brazil.",
                nome="Africanized bee"),
        ],
    },
    # 7 Bertha Lutz: a zoóloga das rãs e os direitos das mulheres na Carta da ONU
    {
        "temas_secundarios": ["leis_julgamentos", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "A menção à igualdade de direitos de homens e mulheres na Carta da ONU, de 1945, deve muito a uma zoóloga brasileira especialista em rãs, Bertha Lutz, que insistiu nela contra a vontade da delegada dos EUA.",
        "explicacao": (
            "Filha do médico Adolpho Lutz, Bertha estudou ciências naturais na Sorbonne e, em 1919, foi contratada "
            "pelo Museu Nacional, no Rio. Dedicou-se aos anfíbios, sobretudo rãs venenosas e pererecas, e publicou "
            "estudos como um sobre um notável coro de rãs no Brasil. Quatro espécies de rãs e duas de lagartos "
            "levam o nome dela. Ao mesmo tempo, liderou a campanha pelo voto feminino no Brasil e chegou à Câmara "
            "dos Deputados. Na conferência de São Francisco que criou a ONU, em 1945, o primeiro rascunho da Carta "
            "não mencionava as mulheres. Bertha Lutz, ao lado da dominicana Minerva Bernardino e de outras "
            "latino-americanas, insistiu na frase final do preâmbulo sobre os direitos iguais de homens e mulheres, "
            "contra a vontade da delegada americana Virginia Gildersleeve e de assessoras britânicas. Ela é "
            "apontada como a defensora mais tenaz da inclusão dos direitos das mulheres no documento, que assinou. "
            "As coleções científicas dela no Museu Nacional foram destruídas no incêndio de setembro de 2018."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Bertha_Lutz",
                "Lutz became a leading figure in both the Pan American feminist movement and human rights movement. "
                "She was instrumental in gaining women's suffrage in Brazil and represented her country at the United Nations Conference on International Organization, signing her name to the United Nations Charter [...] "
                "She has four frog species and two lizard species named after her. [...] "
                "Her father, Adolfo Lutz (1855–1940), was a pioneering physician and epidemiologist of Swiss origin [...] "
                "Bertha Lutz studied natural sciences, biology and zoology at the University of Paris – Sorbonne graduating in 1918. [...] "
                "making Lutz one of the few Brazilian Congresswomen of the era. [...] "
                "During the 1945 United Nations Conference on International Organization in San Francisco, Lutz, along with Minerva Bernardino, fought for the inclusion of the word \"women\" in the preamble to the United Nations Charter. "
                "The first draft did not mention the word \"women\", and against the wishes of US delegate Virginia Gildersleeve and some British female advisors, Lutz and other women from Latin America insisted in the final clause read: \" ...faith in fundamental human rights, in the dignity of the human person, in the equal rights of men and women and of nations large and small\". [...] "
                "She is credited with being the most prominent and tenacious advocate for the inclusion of women's rights in the UN Charter [...] "
                "After returning to Brazil in 1918, Lutz dedicated herself to the study of amphibians, especially poison dart frogs and frogs of the family Hylidae. "
                "In 1919, she was hired by the Museu Nacional do Rio de Janeiro. [...] "
                "\"A notable frog chorus in Brazil\" (1946) [...] "
                "Bertha Lutz's collections held at the Museu Nacional in Rio de Janeiro were destroyed in the fire that devastated most of the museum's collections in September 2018.",
                nome="Bertha Lutz"),
        ],
    },
    # 8 Emílio Ribas e Adolfo Lutz se deixam picar por mosquitos (1903)
    {
        "temas_secundarios": ["doencas_infecciosas", "historia_medicina"],
        "tipos_espanto": ["historia_humana", "mito_desmentido"],
        "gancho": "Em 1903, para provar que a febre amarela vinha de um mosquito, e não do contato com doentes, os médicos Emílio Ribas e Adolfo Lutz se deixaram picar, em São Paulo, por mosquitos que tinham sugado o sangue de um doente.",
        "explicacao": (
            "No fim do século XIX, muitos médicos achavam que a febre amarela passava de pessoa para pessoa, pelo "
            "contato com o doente ou com suas roupas e dejetos: eram os \"contagionistas\". Emílio Ribas, "
            "sanitarista nascido em Pindamonhangaba, combatia surtos da doença no interior paulista desde 1895. "
            "Ele acompanhou os trabalhos do americano Walter Reed e do cubano Carlos Finlay em Cuba e passou a "
            "defender a tese de Finlay: o transmissor seria um mosquito, o atual Aedes aegypti. A posição provocou "
            "uma onda de protestos de médicos. Em 1903, Ribas repetiu na capital paulista os experimentos feitos em "
            "Cuba e se deixou picar por mosquitos infectados, junto com Adolfo Lutz, Oscar Moreira e outros "
            "voluntários. No mesmo ano, no Hospital de Isolamento, que hoje leva o seu nome, tocou em dejetos de "
            "doentes e deitou-se ao lado deles para mostrar que a doença não pegava pelo contato. Ainda em 1903, "
            "num congresso de medicina, declarou sem valor a tese dos contagionistas. Lutz, que dirigia o "
            "Instituto Bacteriológico de São Paulo, é apontado como o primeiro cientista latino-americano a "
            "estudar a fundo e confirmar como o Aedes aegypti transmite a febre amarela."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Emílio_Ribas",
                "Emílio Marcondes Ribas (Pindamonhangaba, 11 de abril de 1862 — São Paulo, 19 de dezembro de 1925) foi um médico sanitarista brasileiro. [...] "
                "Em 1895, foi nomeado como inspetor sanitário e passou a trabalhar em São Paulo no combate a epidemias, em especial de febre amarela nas regiões de Araraquara, Jaú, Rio Claro e Pirassununga. [...] "
                "Acompanhou os trabalhos do médico norte-americano Walter Reed e do médico cubano Carlos Finlay no combate à febre amarela em Cuba. "
                "Enfrentou críticas por defender a tese de Finlay, de maneira correta, que o transmissor da doença era o mosquito Aedes aegypti, o que levantou uma onda de protestos de vários médicos da época. "
                "Em 1903, repetiu na capital paulista as experiências de Cuba, onde se deixou picar, junto de Adolfo Lutz, Oscar Moreira e outros voluntários, por mosquitos infectados pelo sangue de um portador da doença. "
                "A intenção do grupo era de provar que o verdadeiro transmissor era o Stegomyia fasciata, hoje chamado de Aedes aegypti. "
                "No mesmo ano, fez a experiência de entrar em contato com os dejetos dos doentes, de deitar-se ao lado deles para mostrar, mais uma vez, que o contágio não era por toque ou contato, no Hospital de Isolamento (hoje nomeado Instituto de Infectologia Emílio Ribas). "
                "No V Congresso Brasileiro de Medicina e Higiene, em 1903, declarou que a tese dos \"contagionistas\" não tem valor, reforçando a transmissão via insetos.",
                nome="Emílio Ribas (pt)", idioma="pt"),
            wiki("Adolpho_Lutz",
                "returning in 1892 to Brazil, attending an invitation from the government of the state of São Paulo to direct the Bacteriological Institute [...] "
                "Lutz was the first Latin American scientist to study in depth and to confirm the mechanisms of transmission of yellow fever by the Aedes aegypti species of mosquitoes",
                nome="Adolfo Lutz"),
        ],
    },
    # 9 Juliano Moreira: filho de ex-escravizada, contra a tese racista da loucura
    {
        "temas_secundarios": ["heranca_africana", "historia_medicina"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Filho de uma ex-escravizada, o baiano Juliano Moreira entrou em medicina antes dos 15 anos. Psiquiatra, tirou as grades das janelas do hospício nacional e rebateu a tese de que a miscigenação causava doença mental.",
        "explicacao": (
            "Moreira nasceu em Salvador em 1872. A mãe, Galdina, era alforriada e trabalhava na casa de um "
            "professor da Faculdade de Medicina da Bahia, que virou padrinho do menino e o apoiou nos estudos. "
            "Ele entrou no curso em 1886 e se formou em 1891, ainda adolescente pelos padrões de hoje. Depois de "
            "estudar psiquiatria na Alemanha, na Inglaterra, na França, na Itália e na Escócia, dirigiu de 1903 a "
            "1930 o Hospício Nacional de Alienados, no Rio. Ali humanizou o atendimento, acabou com o "
            "aprisionamento dos internos e eliminou as grades das janelas. No meio acadêmico da época, era comum "
            "atribuir os problemas mentais da população brasileira à mistura de raças. Moreira defendeu que eles "
            "vinham de fatores físicos e de condições de vida, como falta de higiene e de acesso à educação. Foi "
            "também o primeiro professor universitário do país a usar a teoria psicanalítica no ensino de "
            "medicina. Mas não escapou de todas as ideias do seu tempo: aceitava parte da eugenia e propunha a "
            "esterilização de alcoólatras e criminosos. Em 1930, foi afastado do cargo pelo governo de Getúlio "
            "Vargas. Uma colônia psiquiátrica no Rio leva o seu nome."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Juliano_Moreira",
                "Nascido em Salvador, negro, filho de Galdina Joaquina do Amaral, ex-escravizada (alforriada) que trabalhava na residência do Dr. Luís Adriano Alves de Lima Gordilho, Barão de Itapuã, médico e professor catedrático de Clínica Médica na Faculdade de Medicina da Bahia. [...] "
                "Graças ao apoio do Dr. Gordilho, seu padrinho, fez concurso e ingressou no curso de medicina, em 1886. "
                "Formou-se em 1891, aos 19 anos [...] "
                "\"Adentrei-me na Faculdade de Medicina da Bahia, em Salvador, com menos de 15 anos de idade, conforme era possível na época [...] "
                "De 1895 a 1902, realizou cursos e estágios sobre doenças psiquiátricas na Alemanha, Inglaterra, França, Itália e Escócia [...] "
                "Durante seu trabalho como diretor do Hospício Nacional dos Alienados, no Rio de Janeiro, realizou mudanças significativas no tratamento dos internos: Humanização do atendimento, suspensão do aprisionamento, eliminação das grades nas janelas etc. [...] "
                "Moreira defendeu a ideia de que a origem das doenças mentais se devia a fatores físicos e situacionais, como a falta de higiene e falta de acesso à educação, contrariando um pensamento racista em voga no meio acadêmico, que atribuía os problemas psicológicos da população brasileira à miscigenação. [...] "
                "Apesar de avesso ao racismo científico, Moreira também aceitava certos aspectos do pensamento eugênico, por exemplo propunha que fosse afastada dos alienados, delinquentes, degenerados e alcoólatras a possibilidade de reprodução, através da prescrição da esterilização destes. [...] "
                "Em 8 de dezembro de 1930, Juliano Moreira foi destituído da direção do Hospital Nacional de Alienados, onde também morava.",
                nome="Juliano Moreira (pt)", idioma="pt"),
            wiki("Juliano_Moreira",
                "Juliano Moreira (6 January 1872 – 2 May 1933) was a Brazilian psychiatrist [...] "
                "Moreira was the first Brazilian university professor to cite and use the psychoanalytic theory in teaching medicine. [...] "
                "From 1903 to 1930, Moreira was the director of the Hospício Nacional de Alienados (National Asylum for the Insane) [...] "
                "Moreira spoke against the pseudoscientific racist beliefs espoused at the time, such as that racial miscegenation caused mental illnesses; he defended that they were due to physical and situational factors such as poor hygiene and lack of access to education. [...] "
                "Despite opposing racism, Moreira was a member of eugenist organizations and defended practices such as the sterilization of criminals and alcoholics. [...] "
                "Colônia Juliano Moreira, a psychiatric colony near Rio de Janeiro was named after him.",
                nome="Juliano Moreira"),
        ],
    },
    # 10 Gaspar Vianna: tratamento da leishmaniose e a morte numa necropsia
    {
        "temas_secundarios": ["doencas_infecciosas", "farmacos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 1912, o paraense Gaspar Vianna apresentou um tratamento que fazia secar as feridas da leishmaniose tegumentar, até então sem remédio eficaz. Dois anos depois, morreu aos 29, infectado ao fazer uma necropsia.",
        "explicacao": (
            "Na construção da ferrovia que ligaria Bauru, em São Paulo, a Mato Grosso, eram comuns os casos da "
            "\"úlcera de Bauru\", uma forma de leishmaniose que deforma a pele e as mucosas. Gaspar Vianna, que "
            "saiu de Belém em 1903 para estudar medicina no Rio e chegou ao Instituto Oswaldo Cruz em 1909, "
            "descreveu em 1911 o parasita como uma espécie nova, a Leishmania braziliensis. Como não havia "
            "remédio eficaz, testou primeiro o arsênico, usado contra a doença do sono, e depois passou ao "
            "tártaro emético, um composto de antimônio. As feridas dos pacientes secaram, e ele apresentou o "
            "resultado num congresso de medicina em Belo Horizonte, em 1912. O tratamento teve repercussão "
            "internacional e foi levado a outros países. No ano seguinte, com Henrique Aragão, usou o mesmo "
            "composto contra o granuloma venéreo, outra doença sem cura na época. Vianna costumava ficar no "
            "laboratório até as 23 horas ou mais. Em 1914, ao fazer a necropsia de um paciente com tuberculose, "
            "levou no rosto um jato do líquido da cavidade torácica, que entrou pela boca e pelo nariz. Dois "
            "meses depois, em junho, morreu de tuberculose miliar aguda."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            {"url": "https://agencia.fiocruz.br/sites/agencia.fiocruz.br/files/revistaManguinhosMateriaPdf/RM30pag66e67DespedidaPrematura.pdf",
             "titulo": "Despedida prematura (Revista de Manguinhos, Fiocruz, dez. 2014)", "idioma": "pt",
             "trecho": "contribuiu para o tratamento da leishmaniose tegumentar, doença que até então não tinha cura. [...] "
                "Vianna faleceu prematuramente, aos 29 anos [...] "
                "é conhecida por infligir graves lesões na pele e nas mucosas das vítimas [...] "
                "de Belém que em 1903 se mudou para a capital federal para estudar na Faculdade de Medicina do Rio de Janeiro [...] "
                "Ele chegou ao Instituto em 1909, convidado por Cruz [...] "
                "Durante a construção da estrada de ferro que ligaria Bauru (SP) ao Mato Grosso, eram comuns casos de leishmaniose, conhecida à época como \"úlcera de Bauru\" [...] "
                "em 1911, Vianna descreveu o parasito como uma nova espécie de Leishmania, que nomeou Leishmania braziliensis. [...] "
                "já que na época não existia um medicamento eficaz. "
                "Depois de tentar arsênico, que era usado contra a doença do sono, ele optou pelo tártaro emético [...] "
                "As feridas dos pacientes foram secando e eles se curaram. "
                "O feito alcançou repercussão internacional e o tratamento criado por ele foi levado a outros países [...] "
                "O êxito da descoberta foi apresentado pelo pesquisador a seus pares no 7º Congresso Brasileiro de Medicina e Cirurgia, em Belo Horizonte, em 1912. "
                "Um ano depois, Vianna encontrou outro uso para o tártaro emético. "
                "Em conjunto com Henrique Aragão, tratou o granuloma venéreo – uma enfermidade que até então também não tinha cura – com sucesso. [...] "
                "normalmente continuava no Instituto até 23h (ou mais) [...] "
                "ao fazer a necropsia em um paciente tuberculoso, recebeu no rosto um jato do líquido que estava na cavidade torácica. "
                "O líquido entrou pela boca e pelo nariz [...] "
                "Dois meses depois, em junho de 1914, Vianna morreu de tuberculose miliar aguda, aos 29 anos."},
            wiki("Gaspar_Vianna",
                "Em 1912, Vianna comprovou que o tártaro emético ou antimonial era eficaz para conter a enfermidade",
                nome="Gaspar Vianna (pt)", idioma="pt"),
        ],
    },
    # 11 o Cerrado que virou lavoura: calcário, fósforo e soja tropical
    {
        "temas_secundarios": ["biomas_brasileiros", "plantas"],
        "tipos_espanto": ["engenhosidade", "escala_absurda"],
        "gancho": "Até meados dos anos 1960, o solo do Cerrado era considerado pobre demais para lavouras. Pesquisadores acharam o remédio em calcário e fósforo e criaram soja para o clima tropical, uma planta até então de clima temperado.",
        "explicacao": (
            "Por muito tempo, o Cerrado serviu quase só à criação extensiva de gado, porque os solos naturais "
            "da região não eram férteis o bastante para plantações. A virada veio com a pesquisa agropecuária. "
            "Pesquisadores da Embrapa, empresa pública criada em 1973, descobriram que o solo podia ser corrigido "
            "com fósforo e calcário, e a quantidade usada impressiona: no fim dos anos 1990, o Brasil jogava de "
            "14 milhões a 16 milhões de toneladas de calcário por ano nas lavouras, e em 2003 e 2004 foram 25 "
            "milhões, cerca de cinco toneladas por hectare. Também foram desenvolvidas variedades de soja adaptadas "
            "aos trópicos. Hoje o Cerrado responde por mais de 70% da produção de gado de corte do país e é "
            "grande produtor de soja, milho, feijão e arroz, e o Brasil é o maior exportador mundial de soja. Em "
            "2006, três pessoas ganharam o Prêmio Mundial da Alimentação pelos esforços em ciência e política que "
            "abriram o Cerrado à agricultura: os brasileiros Edson Lobato e Alysson Paolinelli e o americano Colin "
            "McClung. O custo ambiental é alto: estimativas recentes indicam que só 21,3% da vegetação original "
            "segue intacta, e a expansão da soja é o principal motor da perda."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Cerrado",
                "Until the mid-1960s, agricultural activities in the Cerrado were very limited, since natural cerrado soils are not fertile enough for crop production, directed mainly at the extensive production of beef cattle for subsistence of the local market. [...] "
                "The soil in the Cerrado had historically been challenging for agriculture until researchers at Brazil's agricultural and livestock research agency, Embrapa, discovered that it could be made fit for industrial crops by appropriate additions of phosphorus and lime. "
                "In the late 1990s, between 14 million and 16 million tons of lime were being poured on Brazilian fields each year. "
                "The quantity rose to 25 million tons in 2003 and 2004, equaling around five tons of lime per hectare. [...] "
                "Researchers also developed tropical varieties of soybeans, until then a temperate crop, and currently, Brazil is the world's main soyabeans exporter [...] "
                "Today the Cerrado region provides more than 70% of the beef cattle production in the country, being also a major production center of grains, mainly soya, beans, maize, and rice. [...] "
                "As of recent estimates, only 432,814 km2 (43,281,400 ha)—or 21.3% of the original vegetation—remains intact. [...] "
                "This change is largely being driven by expansion of soy production.",
                nome="Cerrado"),
            wiki("Embrapa",
                "Since its inception on April 26, 1973, it has been devoted to developing technologies, knowledge and technical-scientific information aimed at Brazilian agriculture",
                nome="Embrapa"),
            wiki("World_Food_Prize",
                "2006 Edson Lobato Brazil For individual efforts in science and policy that opened the Cerrado region of Brazil to agricultural [...] "
                "Alysson Paolinelli [...] Andrew Colin McClung",
                nome="World Food Prize"),
        ],
    },
    # 12 Johanna Döbereiner: soja sem adubo nitrogenado
    {
        "temas_secundarios": ["microbiologia", "plantas"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Muitas lavouras de soja do Brasil dispensam adubo nitrogenado: bactérias em nódulos das raízes tiram nitrogênio do ar. Quem apostou nisso foi Johanna Döbereiner, agrônoma nascida na Tchecoslováquia.",
        "explicacao": (
            "O nitrogênio é o nutriente que mais falta nos solos do mundo e o que mais se aplica nas lavouras, e "
            "fornecê-lo por adubo traz sérios problemas ambientais. Mas plantas leguminosas, como a soja, têm uma "
            "alternativa: bactérias do solo chamadas rizóbios infectam suas raízes e formam nódulos, onde "
            "capturam o nitrogênio do ar e o transformam em amônia, que a planta usa para crescer. Johanna "
            "Döbereiner nasceu em 1924 em Ústí nad Labem, hoje na República Tcheca, formou-se em Munique e se "
            "naturalizou brasileira em 1956. Estudou bactérias úteis ao solo brasileiro, como a Azospirillum, e "
            "teve papel importante na soja do país ao incentivar variedades que dependessem só da fixação "
            "biológica de nitrogênio. Como resultado, muitas plantações brasileiras recebem todo o nitrogênio "
            "dos rizóbios, sem adubo nitrogenado. Isso pesa no mundo: Brasil e EUA produzem cerca de metade da "
            "soja do planeta, uma das principais fontes de proteína, em geral via ração animal. Döbereiner "
            "recebeu o Prêmio de Ciência da UNESCO em 1989. Em 2025, outra pesquisadora brasileira, Mariangela "
            "Hungria, ganhou o Prêmio Mundial da Alimentação por avanços na fixação biológica de nitrogênio na "
            "agricultura tropical."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Johanna_Döbereiner",
                "was a Brazilian agronomist and pioneer in soil biology. [...] "
                "Döbereiner was born in Ústí nad Labem in Czechoslovakia (now in the Czech Republic) on 28 November 1924. [...] "
                "Johanna Döbereiner received her degree from the Ludwig-Maximilians-Universität München (LMU), but settled in Brazil and became a Brazilian citizen in 1956. "
                "Her early work includes studies of Azospirillum and other bacteria that could be useful to Brazilian soil. "
                "She later played an important role in Brazil's soybean production by encouraging a reliance on varieties that solely depended on biological nitrogen fixation. "
                "As a consequence of her research and ideas, numerous soybean plantations in Brazil are now completely supplied for nitrogen (N) by rhizobia and not using any N-fertilizers. "
                "This movement has had big benefits, because Brazil, together with the U.S., are the main producers of soybean in the world (ca. 50% world production). "
                "Considering that soybeans are one of the most important global sources of protein (mainly fed to animals that in turn becomes animal protein for human consumption)",
                nome="Johanna Döbereiner"),
            wiki("Rhizobia",
                "Rhizobia are a \"group of soil bacteria that infect the roots of legumes to form root nodules\". "
                "Rhizobia are found in the soil and, after infection, produce nodules in the legume where they fix nitrogen gas (N2) from the atmosphere, turning it into a more readily useful form of nitrogen: ammonia (NH3). "
                "From here, the nitrogen is exported from the nodules and used for growth in the legume. [...] "
                "Nitrogen is the most commonly deficient nutrient in many soils around the world and it is the most commonly supplied plant nutrient. "
                "The supply of nitrogen through fertilizers has severe environmental concerns.",
                nome="Rhizobia"),
            wiki("José_Leite_Lopes",
                "A engenheira agrônoma Johanna Döbereiner recebeu este prêmio em 1989.",
                nome="José Leite Lopes (pt)", idioma="pt"),
            wiki("World_Food_Prize",
                "2025 Mariangela Hungria Brazil For her extraordinary scientific advancements in biological nitrogen fixation, transforming the sustainability of soil health and crop nutrition for tropical agriculture.",
                nome="World Food Prize"),
        ],
    },
    # 13 o carro flex que deduz a mistura por software (e o álcool de 1943)
    {
        "temas_secundarios": ["energia", "invencoes"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "O carro flex brasileiro não precisa de um sensor próprio para saber quanto álcool há no tanque: um software criado no Brasil deduz a mistura com a sonda que já mede a queima em qualquer motor com injeção.",
        "explicacao": (
            "O Brasil mistura álcool à gasolina há muito tempo. Um decreto de 1931 tornou obrigatório adicionar "
            "5% de etanol à gasolina importada, e em 1943, com submarinos alemães ameaçando o abastecimento de "
            "petróleo, a mistura chegou a 50%. Depois da crise do petróleo de 1973, o governo lançou o Proálcool, "
            "em 1975. O engenheiro aeronáutico Urbano Ernesto Stumpf, do Centro Técnico Aeroespacial, passou de "
            "1973 a 1976 adaptando motores ao álcool, e em 1979 chegou às lojas o Fiat 147, o primeiro carro "
            "moderno vendido no mundo para rodar só com etanol. O flex veio depois. Os primeiros carros "
            "bicombustíveis americanos tinham um sensor dedicado para medir a mistura, o que os encarecia. A "
            "solução brasileira foi aproveitar a sonda lambda, que já existia para avaliar a combustão: um "
            "programa feito por engenheiros brasileiros, o \"Software Fuel Sensor\", usa os dados dos sensores de "
            "série para descobrir que mistura está queimando e ajustar o motor. A tecnologia foi desenvolvida pela "
            "subsidiária brasileira da Bosch em 1994 e lançada comercialmente em 2003, no Gol Total Flex. Em agosto "
            "de 2009, os flex já eram 94% dos carros vendidos no país."
        ),
        "nivel": 2, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Pró-Álcool",
                "A decree was issued on February 20, 1931, mandating the blend of 5% hydrated ethanol to all imports of gasoline by volume. [...] "
                "Due to German submarine attacks threatening oil supplies, the mandatory blend was as high as 50 percent in 1943. [...] "
                "As a response to the 1973 oil crisis, the Brazilian government began promoting bioethanol as a fuel. "
                "The National Alcohol Program -Pró-Álcool- (Portuguese: Programa Nacional do Álcool), launched in 1975 [...] "
                "the first 16 gasoline stations began supplying hydrous ethanol in May 1979 for a fleet of 2,000 neat ethanol adapted vehicles, and by July, the Fiat 147 was launched to the market, becoming the first modern commercial neat ethanol-powered car (E100) sold in the world. [...] "
                "A key innovation in the Brazilian flex technology was avoiding the need for an additional dedicated sensor to monitor the ethanol-gasoline mix, which made the first American M85 flex fuel vehicles too expensive. "
                "This was accomplished through the lambda probe, used to measure the quality of combustion in conventional engines, is also required to tell the engine control unit (ECU) which blend of gasoline and alcohol is being burned. "
                "This task is accomplished automatically through software developed by Brazilian engineers, called \"Software Fuel Sensor\" (SFS), fed with data from the standard sensors already built-in the vehicle. "
                "The technology was developed by the Brazilian subsidiary of Bosch in 1994 [...] "
                "In March 2003, Volkswagen launched in the Brazilian market the Gol 1.6 Total Flex, the first commercial flexible fuel vehicle capable of running on any blend of gasoline and ethanol. [...] "
                "Flexible-fuel vehicles were 22% of the car sales in 2004, 73% in 2005, 87.6% in July 2008, and reached a record 94% in August 2009.",
                nome="History of ethanol fuel in Brazil"),
            wiki("Urbano_Ernesto_Stumpf",
                "Urbano Ernesto Stumpf (Passo Fundo, 15 de janeiro de 1916 – 17 de maio de 1998) foi um coronel-aviador, engenheiro aeronáutico, professor e inventor brasileiro. [...] "
                "Quando da primeira crise do petróleo em 1973, o Centro Técnico Aeroespacial (CTA), incumbiu-o de realizar estudos técnicos sobre o etanol que permitiram que o governo mais tarde criasse o pró-álcool. "
                "Durante três anos, de 1973 a 1976, realizou experiências com diversos tipos de motores adaptando-os para o uso do álcool combustível.",
                nome="Urbano Ernesto Stumpf (pt)", idioma="pt"),
        ],
    },
]
