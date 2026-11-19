LOTE = "2026-11-17-historia_computacao-01"
AREA = "tecnologia"
TEMA = "historia_computacao"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = W if idioma == "en" else "https://pt.wikipedia.org/wiki/"
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


FAPESP = "https://revistapesquisa.fapesp.br/o-legado-do-patinho-feio/"

CANDIDATOS = [
    # 1 o "bug" é mais antigo que o computador
    {
        "temas_secundarios": ["insetos", "invencoes"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "A famosa mariposa presa num computador em 1947 não deu origem à palavra \"bug\": Thomas Edison já chamava defeitos de bugs em 1878, e os operadores fizeram um trocadilho.",
        "explicacao": (
            "Conta-se muitas vezes que a palavra bug, \"inseto\" em inglês, passou a significar defeito por causa "
            "de uma mariposa. A mariposa existiu: por volta de 1947, na Universidade Harvard, operadores do "
            "computador eletromecânico Mark II rastrearam um erro até uma mariposa presa num relé. Ela foi retirada "
            "e colada no caderno de registros com a anotação \"primeiro caso real de bug encontrado\". A pioneira da "
            "computação Grace Hopper, que trabalhava com essas máquinas, popularizou a história. Mas o termo era "
            "bem mais antigo. Bug já era jargão de engenharia para defeito pelo menos desde a década de 1870. Em "
            "1878, Thomas Edison escreveu a um colega que, em todas as suas invenções, depois da intuição inicial "
            "surgiam as dificuldades, os \"bugs\", como eram chamadas essas pequenas falhas. Os operadores do Mark II "
            "conheciam o termo e, provavelmente, fizeram um trocadilho ao juntar os dois sentidos da palavra."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Bug_(engineering)",
            "The term bug to describe a defect has been engineering jargon since at least as far back as the 1870s, long before electronic computers and computer software. "
            "For instance, Thomas Edison wrote the following words in a letter to an associate in 1878: It has been just so in all of my inventions. "
            "The first step is an intuition, and comes with a burst, then difficulties arise—this thing gives out and [it is] then that \"Bugs\"—as such little faults and difficulties are [...] "
            "U.S. Navy Rear Adm. Grace Hopper, a computer pioneer, popularized a story about a moth that caused a problem in an early electromechanical computer. "
            "While Hopper was working on the Mark II and Mark III as Harvard faculty in about 1947, operators traced an error in the Mark II to a moth trapped in a relay. "
            "The moth was removed from the mechanism and taped in a log book with the note \"First actual case of bug being found.\" "
            "Reportedly, the operators, including William \"Bill\" Burke, later of the Naval Weapons Laboratory, Dahlgren, Virginia, were familiar with the engineering term and probably making a pun by conflating the two meanings of bug (biological and technical).",
            nome="Bug (engineering)")],
    },
    # 2 as programadoras do ENIAC
    {
        "temas_secundarios": ["personagens_esquecidos", "segunda_guerra"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "O ENIAC, um dos primeiros computadores eletrônicos, foi programado por seis mulheres. Na época, programar era visto como trabalho de escritório, e elas ficaram sem crédito.",
        "explicacao": (
            "Antes de existir o computador eletrônico, \"computador\" era uma profissão: pessoas, muitas delas "
            "mulheres, faziam cálculos com calculadoras mecânicas para estudos científicos e projetos de "
            "engenharia. Foi desse grupo que o matemático Herman Goldstine escolheu as primeiras programadoras do "
            "ENIAC, construído para o Laboratório de Pesquisa Balística do Exército dos Estados Unidos. Eram seis: "
            "Kay McNulty, Betty Jennings, Betty Snyder, Marlyn Wescoff, Fran Bilas e Ruth Lichterman. Elas não só "
            "descobriram como inserir os programas na máquina, como entenderam o funcionamento interno dela. "
            "McNulty desenvolveu o uso de sub-rotinas para ampliar a capacidade de cálculo. Os contemporâneos, "
            "porém, consideravam a programação uma tarefa burocrática e não reconheceram publicamente o papel "
            "delas. O reconhecimento veio depois: três supercomputadores do Exército americano em uso em 2020, "
            "Jean, Kay e Betty, receberam os nomes de três delas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("ENIAC",
            "Mathematician Herman Goldstine selected the original ENIAC programmers, whom he called operators, from this group. "
            "Six women were chosen to be the programmers of ENIAC for the Army's Ballistic Research Laboratory [...] "
            "ENIAC's six primary programmers, Kay McNulty, Betty Jennings, Betty Snyder, Marlyn Wescoff, Fran Bilas and Ruth Lichterman, not only determined how to input ENIAC programs, but also developed an understanding of ENIAC's inner workings. [...] "
            "McNulty developed the use of subroutines to increase ENIAC's computational capability. "
            "Though contemporaries considered programming a clerical task and did not publicly recognize the programmers' effect on the successful operation and announcement of ENIAC, McNulty, Jennings, Snyder, Wescoff, Bilas, and Lichterman have since been recognized for their contributions to computing. "
            "Three of the current (2020) Army supercomputers, Jean, Kay, and Betty, are named after Jean Bartik (Betty Jennings), Kay McNulty, and Betty Snyder respectively. [...] "
            "thematical calculations for scientific studies or engineering projects, usually with a mechanical calculator.")],
    },
    # 3 Colossus
    {
        "temas_secundarios": ["segunda_guerra", "espionagem", "criptografia"],
        "tipos_espanto": ["historia_humana", "mito_desmentido"],
        "gancho": "O primeiro computador eletrônico programável foi britânico, quebrava códigos nazistas e ficou em segredo até os anos 1970. E não foi projetado por Alan Turing.",
        "explicacao": (
            "Entre 1943 e 1945, os decifradores de códigos britânicos usaram uma série de máquinas chamadas Colossus "
            "para quebrar a cifra Lorenz, usada pelo alto-comando alemão para falar com os comandos do exército na "
            "Europa ocupada. Com válvulas eletrônicas fazendo operações lógicas e contagens, o Colossus é "
            "considerado o primeiro computador digital eletrônico programável do mundo. Antes dele havia máquinas "
            "eletromecânicas, como a Z3 do alemão Konrad Zuse, de 1941. O projeto foi do engenheiro de telefonia "
            "Tommy Flowers, a partir de planos do matemático Max Newman, em Bletchley Park. É um equívoco comum "
            "dizer que Turing o projetou para quebrar a Enigma: a máquina de Turing para a Enigma foi outra, a "
            "Bombe, eletromecânica. Depois da guerra, quase todas as Colossus foram desmontadas em pedaços tão "
            "pequenos que ninguém poderia deduzir para que serviam, e a própria existência delas ficou em segredo "
            "até meados dos anos 1970."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Colossus_computer",
            "computers developed by British codebreakers in the years 1943–1945 to help in the cryptanalysis of the Lorenz cipher. "
            "Colossus used thermionic valves (vacuum tubes) to perform Boolean and counting operations. "
            "Colossus is regarded as the world's first programmable, electronic, digital computer. "
            "There were earlier electromechanical computers, the first being Konrad Zuse's Z3, completed in Berlin in 1941. "
            "Colossus was designed by General Post Office (GPO) research telephone engineer Tommy Flowers, based on plans developed by mathematician Max Newman at the Government Code and Cypher School at Bletchley Park. [...] "
            "It is sometimes erroneously said that Colossus was designed by Turing, not Flowers, to aid the cryptanalysis of the Enigma but an earlier machine that Turing designed was the electromechanical Bombe. [...] "
            "intercepted radiotelegraphy messages between the German High Command (OKW) and their army commands throughout occupied Europe. "
            "The existence of the Colossus machines was kept secret until the mid-1970s. "
            "All but two machines were dismantled into such small parts that their use could not be inferred.",
            nome="Colossus computer")],
    },
    # 4 memória de corda tecida
    {
        "temas_secundarios": ["exploracao_espacial", "moda"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "O software que levou a Apollo à Lua foi tecido à mão: operárias passavam fios por dentro ou por fora de anéis magnéticos, e cada passagem era um bit.",
        "explicacao": (
            "O computador de bordo das missões Apollo, construído pela Raytheon, guardava seus programas numa "
            "memória de corda, uma tecnologia em que a informação fica na própria fiação. Nela, um fio de leitura "
            "passa por dentro de um núcleo magnético, um pequeno anel, para representar um bit, normalmente o 1, ou "
            "por fora dele, para representar o outro. Para ler, uma corrente forte inverte a polaridade dos "
            "núcleos, o que induz uma pequena tensão nos fios que passam por dentro. O software era escrito por "
            "programadores do Instituto de Tecnologia de Massachusetts, o MIT, e depois tecido na memória por "
            "operárias em fábricas. Alguns programadores apelidaram o resultado de memória LOL, sigla em inglês "
            "para \"memória das velhinhas\". A técnica já tinha sido usada nos anos 1960 nas primeiras sondas da "
            "NASA para Marte."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Core_rope_memory",
            "It was later used in the 1960s by early NASA Mars space probes and then in the Apollo Guidance Computer (AGC), which was built by Raytheon. "
            "The software for the AGC was written by programmers at the Massachusetts Institute of Technology (MIT) Instrumentation Lab, and was woven into core rope memory by female workers in factories. "
            "Some programmers nicknamed the finished product LOL memory, for Little Old Lady memory. [...] "
            "Sense: A sense wire can detect a change in a core's polarity. "
            "It can pass through a core to indicate one bit state (typically '1') or bypass it to represent the other (typically '0'). [...] "
            "To read from core rope memory, the set/reset wire is given a strong current to change the polarity of the cores. "
            "This induces a small voltage on the sense wires pass",
            nome="Core rope memory")],
    },
    # 5 a primeira webcam
    {
        "temas_secundarios": ["telecomunicacoes", "cafe_cha_cacau"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "A primeira webcam do mundo vigiava uma cafeteira na Universidade de Cambridge, para ninguém andar até a sala e encontrar o bule vazio.",
        "explicacao": (
            "Em 1991, no Laboratório de Computação da Universidade de Cambridge, na Inglaterra, Quentin "
            "Stafford-Fraser e Paul Jardetzky montaram uma câmera apontada para a cafeteira da Sala Troiana. O "
            "objetivo era poupar quem trabalhava no prédio da decepção de atravessar os corredores e encontrar o "
            "bule vazio. A câmera, em preto e branco e com só 128 por 128 pixels, mandava a imagem pela rede interna "
            "do laboratório. Em 1993, os navegadores da web passaram a exibir imagens, e a câmera foi ligada à "
            "internet. A cafeteira ficou famosa no mundo todo como uma atração da web ainda engatinhando, até ser "
            "aposentada em 2001. O desligamento saiu na primeira página do The Times e do Washington Post. A "
            "última das cafeteiras que apareceram na câmera, uma Krups, foi leiloada no eBay por 3.350 libras."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Trojan_Room_coffee_pot",
            "The Trojan Room coffee pot was a coffee machine located in the Computer Laboratory of the University of Cambridge, England. "
            "It was the subject of the world's first webcam, created by Quentin Stafford-Fraser and Paul Jardetzky in 1991. "
            "To save people working in the building the disappointment of finding the coffee machine empty after making the trip to the room [...] "
            "the coffee pot gained international renown as a feature of the fledgling World Wide Web, until being retired in 2001. [...] "
            "The 128×128 px greyscale camera was connected to the laboratory's local network [...] "
            "In 1993, web browsers gained the ability to display images [...] "
            "front-page mentions in The Times and The Washington Post [...] "
            "The last of the four or five coffee machines seen online, a Krups, was auctioned on eBay for £3,350",
            nome="Trojan Room coffee pot")],
    },
    # 6 Anticítera
    {
        "temas_secundarios": ["grecia_antiga", "historia_astronomia", "navegacao_antiga"],
        "tipos_espanto": ["escala_absurda", "engenhosidade"],
        "gancho": "Um naufrágio grego guardava um computador analógico de mais de 2 mil anos, capaz de prever eclipses. Nada tão complexo voltou a ser feito até o século XIV.",
        "explicacao": (
            "Em 1901, mergulhadores que recolhiam esponjas acharam um naufrágio perto da ilha grega de Anticítera. "
            "Entre os destroços estava um bloco corroído que, no ano seguinte, revelou ter uma engrenagem dentro. "
            "Era o mecanismo de Anticítera, um modelo do Sistema Solar movido à mão, construído no século II antes de "
            "Cristo. É o exemplo mais antigo conhecido de computador analógico. Com ele era possível prever "
            "posições de astros e eclipses com décadas de antecedência, e até acompanhar o ciclo de quatro anos "
            "dos Jogos Olímpicos da Antiguidade. Hoje o mecanismo está dividido em 82 fragmentos. A maior "
            "engrenagem tinha cerca de 13 centímetros de diâmetro e 223 dentes. Em 2005, tomografias de raio X "
            "permitiram ler inscrições apagadas. Máquinas de complexidade parecida só voltaram a aparecer no século "
            "XIV, na Europa Ocidental."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Antikythera_mechanism",
            "is an ancient Greek hand-powered orrery (model of the Solar System) built in the 2nd century BC and discovered in 1901. "
            "It is the oldest known example of an analogue computer. "
            "It could be used to predict astronomical positions and eclipses decades in advance. "
            "It could also be used to track the four-year cycle of athletic games similar to an olympiad, the cycle of the ancient Olympic Games. "
            "The artefact was among wreckage retrieved from a shipwreck off the coast of the Greek island Antikythera in 1901. [...] "
            "Machines with similar complexity did not appear again until the 14th century in western Europe. [...] "
            "a crew of sponge divers from Symi island discovered the Antikythera wreck [...] "
            "which are now divided into 82 separate fragments after conservation efforts. [...] "
            "The largest gear is about 13 cm (5 in) in diameter and originally had 223 teeth. [...] "
            "In 2005, a team from Cardiff University led by Mike Edmunds used computer X-ray tomography and high resolution scanning to image inside fragments of the crust-encased mechanism and read faint inscriptions",
            nome="Antikythera mechanism")],
    },
    # 7 cartões perfurados vêm do tear
    {
        "temas_secundarios": ["revolucao_industrial", "moda", "invencoes"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "Os cartões perfurados dos primeiros computadores vieram de um tear de tecidos, de 1804. A ideia passou por um censo americano e ajudou a criar a IBM.",
        "explicacao": (
            "Em 1804, o francês Joseph Marie Jacquard criou um tear controlado por uma corrente de cartões "
            "perfurados: cada cartão correspondia a uma linha do desenho do tecido, e os furos indicavam quais fios "
            "seriam levantados. Antes, quem fazia essa seleção à mão era um ajudante. Usar cartões substituíveis "
            "para controlar uma sequência de operações é considerado um passo importante na história da "
            "computação. Charles Babbage conhecia o tear e planejou usar cartões para guardar os programas da sua "
            "Máquina Analítica. No fim do século XIX, Herman Hollerith levou a ideia adiante: criou máquinas que "
            "liam cartões perfurados e as usou no censo americano de 1890. O processamento, que tinha levado oito "
            "anos no censo de 1880, caiu para seis. A empresa de Hollerith se fundiu com outras em 1911 e, em "
            "1924, passou a se chamar International Business Machines, a IBM."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Jacquard_machine",
                "This use of replaceable punched cards to control a sequence of operations is considered an important step in the history of computing hardware, having inspired Charles Babbage's Analytical Engine. [...] "
                "The heddles with warp ends to be pulled up were manually selected by a second operator, the draw boy, not the weaver. [...] "
                "d by Joseph Marie Jacquard in 1804 [...] "
                "The machine was controlled by a \"chain of cards\"; a number of punched cards laced together into a continuous sequence. "
                "Multiple rows of holes were punched on each card, with one complete card corresponding to one row of the design. [...] "
                "Charles Babbage knew of Jacquard machines and planned to use cards to store programs in his Analytical Engine. "
                "In the late 19th century, Herman Hollerith took the idea of using punched cards to store information a step further when he created a punched card tabulating machine which he used to input data for the 1890 United States census.",
                nome="Jacquard machine"),
            wiki("Herman_Hollerith",
                "reduced the time required to process the census from eight years for the 1880 census to six years for the 1890 census. [...] "
                "ith founded a company that was amalgamated in 1911 with several other companies to form the Computing-Tabulating-Recording Company. "
                "In 1924, the company was renamed \"International Business Machines\" (IBM)",
                nome="Herman Hollerith"),
        ],
    },
    # 8 Patinho Feio
    {
        "temas_secundarios": ["ciencia_brasileira", "brasil_republica"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "O primeiro computador brasileiro, o Patinho Feio, da USP, não funcionou na inauguração em 1972: um fotógrafo pisou no fio e desligou a máquina.",
        "explicacao": (
            "O Patinho Feio nasceu em 1972 como trabalho final de uma disciplina de pós-graduação da Escola "
            "Politécnica da USP. Os alunos tiveram de projetar e construir tudo, do hardware aos programas e às "
            "interfaces com os periféricos, porque nada disso era produzido no Brasil. A máquina pesava 100 quilos "
            "e tinha 4 kilobytes de memória. O nome foi uma brincadeira: a Unicamp tinha anunciado, com a Marinha, a "
            "construção do que seria o primeiro computador brasileiro, o Cisne Branco. \"Dizíamos que estávamos "
            "construindo o Patinho Feio, mas que ele seria o primeiro a funcionar\", contou um dos alunos. Só o "
            "Patinho saiu do papel. Na inauguração, em 24 de julho de 1972, com o governador de São Paulo, o reitor "
            "da USP e um bispo que benzeu a máquina, não houve demonstração: um fotógrafo afoito pisou no fio e o "
            "computador demorou a ser religado. O projeto deu origem ao G-10, protótipo do primeiro computador "
            "comercial do país."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [{"url": FAPESP, "titulo": "O legado do Patinho Feio (Revista Pesquisa FAPESP)", "idioma": "pt",
                    "trecho": "Detalhe do painel frontal do computador, que pesava 100 quilos e tinha 4 kilobytes de memória [...] "
                              "O Patinho Feio, o primeiro computador brasileiro, nasceu em 1972 como o trabalho final da disciplina Arquitetura de Computadores da pós-graduação em Engenharia Elétrica do então Departamento de Engenharia de Eletricidade da Escola Politécnica da Universidade de São Paulo (Poli-USP). [...] "
                              "Ela serviu de base para o desenvolvimento de outro computador, o G-10 [...] "
                              "O G-10, por sua vez, foi o protótipo para o primeiro computador comercial do país [...] "
                              "Os alunos da USP tiveram que projetar e construir o hardware, os softwares e as interfaces com os periféricos [...] "
                              "Nada disso era produzido no Brasil naquela época. [...] "
                              "O nome Patinho Feio surgiu de uma brincadeira do então mestrando Paulo Wanderlei Patullo. "
                              "A Universidade Estadual de Campinas (Unicamp) havia anunciado um convênio com a Marinha do Brasil para construir o que seria o primeiro computador brasileiro, o Cisne Branco. "
                              "“Dizíamos que estávamos construindo o Patinho Feio, mas que ele seria o primeiro a funcionar. Por fim, foi o único dos dois a ser concretizado”, contou Patullo na cerimônia dos 50 anos. "
                              "A inauguração do Patinho Feio ocorreu no dia 24 de julho de 1972 e teve as presenças do governador de São Paulo à época, Laudo Natel, do então reitor da USP, Miguel Reale, e do bispo dom Ernesto de Paula, que benzeu a máquina. "
                              "O detalhe é que não houve uma demonstração do computador funcionando. "
                              "Um fotógrafo afoito pisou no fio e desligou o equipamento, que demorou para ser reiniciado."}],
    },
    # 9 o mouse alemão
    {
        "temas_secundarios": ["invencoes"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "O mouse de bolinha não nasceu na Califórnia: uma empresa alemã o anunciou em 1968, dois meses antes da demonstração famosa de Douglas Engelbart.",
        "explicacao": (
            "A primeira demonstração pública de um mouse controlando um computador foi feita por Douglas Engelbart "
            "em 1968, na apresentação que ficou conhecida como \"a mãe de todas as demonstrações\". O protótipo dele "
            "tinha sido construído em 1964 com a ajuda de Bill English e usava duas rodinhas separadas, uma para "
            "cada direção. Mas a ideia do mouse com uma bola embaixo veio de outro lugar. Em 2 de outubro de 1968, "
            "mais de dois meses antes da demonstração de Engelbart, a empresa alemã AEG-Telefunken mostrou num "
            "folheto de vendas um aparelho chamado Rollkugelsteuerung, \"controle por bola rolante\", oferecido "
            "como acessório de um terminal gráfico. Ele derivava de um dispositivo ainda mais antigo, o trackball, "
            "inventado em 1946 por Ralph Benjamin para um sistema de radar militar do pós-guerra."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Computer_mouse",
            "The first public demonstration of a mouse controlling a computer system was done by Douglas Engelbart in 1968 as part of The Mother of All Demos. "
            "Mice originally used two separate wheels to directly track movement across a surface in each dimension. [...] "
            "The trackball, a related pointing device, was invented in 1946 by Ralph Benjamin as part of a post-World War II-era fire-control radar plotting system [...] "
            "In 1964, Bill English joined ARC, where he helped Engelbart build the first mouse prototype. [...] "
            "On 2 October 1968, three years after Engelbart's prototype but more than two months before his public demo, a mouse device named Rollkugelsteuerung (German for \"Trackball control\") was shown in a sales brochure by the German company AEG-Telefunken as an optional input device for the SIG 100 vector graphics terminal",
            nome="Computer mouse")],
    },
    # 10 spam e Monty Python
    {
        "temas_secundarios": ["cinema_fotografia", "palavras_viajantes", "historia_pratos"],
        "tipos_espanto": ["origem_inesperada"],
        "gancho": "O nome spam vem de uma carne enlatada, por meio de um esquete do Monty Python em que vikings cantam \"Spam\" sem parar num restaurante.",
        "explicacao": (
            "Spam é o envio em massa de mensagens não solicitadas, por e-mail, celular, redes sociais, fóruns e "
            "muitos outros canais. O nome vem do Spam, uma marca de carne enlatada, mas por um caminho indireto: um "
            "esquete do grupo de humor britânico Monty Python. Nele, um casal tenta pedir comida num restaurante em "
            "que quase todos os pratos têm Spam, enquanto um grupo de vikings canta \"Spam\" repetidamente, "
            "abafando a conversa. A repetição irritante e impossível de evitar virou o apelido das mensagens que "
            "inundam caixas de entrada. E o spam continua existindo por uma razão econômica: quem o envia quase não "
            "tem custo, além de manter listas de endereços, servidores e infraestrutura."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Spamming",
            "It is named after Spam, a luncheon meat, by way of a Monty Python sketch about a restaurant that has Spam in almost every dish, in which Vikings annoyingly sing \"Spam\" repeatedly. "
            "Spamming remains economically viable because advertisers have no operating costs beyond the management of their mailing lists, servers, infrastructures, IP ranges, and domain names")],
    },
]
