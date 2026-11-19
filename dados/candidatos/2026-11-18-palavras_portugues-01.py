LOTE = "2026-11-18-palavras_portugues-01"
AREA = "linguas"
TEMA = "palavras_portugues"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 forró não vem de "for all"
    {
        "temas_secundarios": ["musica_brasileira", "cultura_popular"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "\"Forró\" não vem do inglês \"for all\". A palavra é uma redução de \"forrobodó\", e já aparecia num disco de 1937, anos antes da base americana que a lenda cita.",
        "explicacao": (
            "Uma história muito repetida diz que, no começo do século XX, engenheiros britânicos que construíam "
            "uma ferrovia em Pernambuco davam bailes abertos ao público, \"for all\", e que os nordestinos teriam "
            "transformado a expressão em \"forró\". Outra versão troca os britânicos pelos soldados da base "
            "militar dos Estados Unidos instalada em Parnamirim, no Rio Grande do Norte, durante a Segunda Guerra. "
            "Nenhuma das duas tem sustentação. Segundo o filólogo Evanildo Bechara, \"forró\" é uma redução de "
            "\"forrobodó\", variante do antigo galego-português \"forbodó\", que por sua vez seria uma corruptela "
            "do francês \"faux-bourdon\", com o sentido de desafinação. As datas também derrubam a lenda "
            "americana: em 1912 estreou a peça \"Forrobodó\", musicada por Chiquinha Gonzaga, e em 1937 a palavra "
            "\"forró\" já estava gravada em disco, na canção \"Forró na roça\", cinco anos antes da instalação da "
            "base."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Forr%C3%B3",
            "O termo \"forró\", segundo o filólogo pernambucano Evanildo Bechara, é uma redução de forrobodó, que por sua vez é uma variante do antigo vocábulo galego-português forbodó, corruptela do francês faux-bourdon, que teria a conotação de desentoação. [...] "
            "Na etimologia popular (ou pseudoetimologia) é frequente associar a origem da palavra \"forró\" à expressão da língua inglesa for all (para todos). "
            "Para essa versão foi inventada uma engenhosa história: no início do século XX, os engenheiros britânicos, instalados em Pernambuco para construir a ferrovia Great Western, promoviam bailes abertos ao público, ou seja for all. [...] "
            "Outra versão da mesma história substitui os ingleses pelos estadunidenses e Pernambuco por Parnamirim (Rio Grande do Norte) do período da Segunda Guerra Mundial, quando uma base militar dos Estados Unidos foi instalada nessa cidade. "
            "Apesar da versão bem-humorada, não há nenhuma sustentação para tal etimologia do termo. "
            "Em 1912, estreou a peça teatral \"Forrobodó\", escrita por Carlos Bettencourt (1890-1941) e Luís Peixoto (1889-1973), musicada por Chiquinha Gonzaga e em 1937, cinco anos antes da instalação da referida base militar em território potiguar, a palavra \"forró\" já se encontrava registrada na história musical na gravação fonográfica de “Forró na roça”",
            nome="Forró", idioma="pt")],
    },
    # 2 salário e sal
    {
        "temas_secundarios": ["roma_antiga", "dinheiro"],
        "tipos_espanto": ["mito_desmentido"],
        "gancho": "\"Salário\" vem mesmo de \"sal\", mas a história de que os soldados romanos eram pagos com sal não tem base. Ninguém sabe ao certo qual era a ligação.",
        "explicacao": (
            "A palavra salário vem do latim \"salarium\", que quer dizer \"relativo ao sal\". Daí nasceu uma "
            "explicação que aparece em livros, aulas e sites: os legionários romanos receberiam seu pagamento em "
            "sal, mercadoria valiosa na época. Mas não há fontes antigas que mostrem isso. A ligação exata entre o "
            "salarium e o sal é desconhecida. Talvez fosse uma ajuda de custo para comprar sal, mas nem essa "
            "versão mais modesta tem apoio nos textos antigos. O que existe é uma associação antiga entre sal e "
            "sustento: no livro bíblico de Esdras, escrito entre os séculos VI e V antes de Cristo, receber o sal "
            "de alguém equivalia a receber dele o sustento, o pagamento ou estar a seu serviço, numa época em que "
            "a produção de sal era controlada pelos reis. Seja qual for a origem, o salarium pago aos soldados "
            "romanos deu nome ao trabalho assalariado no Ocidente."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Salary",
            "By the time of the Hebrew Book of Ezra (550 to 450 BCE), receiving salt from a person was synonymous with drawing sustenance, taking pay, or being in that person's service. "
            "At that time, salt production was strictly controlled by the monarchy or ruling elite. [...] "
            "The word \"salary\" comes from Latin salarium 'pertaining to salt' (sal 'salt'), but the exact connection is not known; "
            "a persistent modern claim that the Roman Legions were sometimes paid in salt is baseless. "
            "It may have been a salt allowance, but even that is not supported by ancient sources. [...] "
            "Regardless of the exact connection, the salarium paid to Roman soldiers has defined a form of work-for-hire ever since in the Western world",
            nome="Salary")],
    },
    # 3 trabalho e tripalium
    {
        "temas_secundarios": ["roma_antiga", "costumes_rituais"],
        "tipos_espanto": ["origem_inesperada", "mito_desmentido"],
        "gancho": "\"Trabalho\" provavelmente vem do latim \"tripalium\", \"três estacas\". Mas a fama de instrumento de tortura é exagerada: os registros mais antigos falam de uma armação para prender animais.",
        "explicacao": (
            "A maioria dos estudiosos acredita que \"trabalho\", assim como o francês \"travail\" e palavras "
            "parecidas de outras línguas, vem do latim \"tripalium\", literalmente \"três estacas\". Uma minoria "
            "contesta, por causa de uma irregularidade na evolução da primeira sílaba. Costuma-se dizer que o "
            "tripalium era um instrumento de tortura, mas o uso original da palavra ainda é incerto. As "
            "referências mais antigas, da época romana, descrevem uma estrutura de madeira para imobilizar um "
            "animal grande e agitado, como cavalo ou boi, durante exame ou tratamento. Também se amarravam ali "
            "pessoas violentas. O sentido de tortura aparece num texto de 582, do Concílio de Auxerre, que proíbe "
            "clérigos de assistir a sessões de tortura com um instrumento de três estacas usado para punir "
            "escravizados. E o sentido antigo sobreviveu: na França, \"travail\" ainda é o nome da armação de "
            "madeira onde os ferradores prendem o cavalo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Tripalium",
            "Tripalium or trepalium (derived from the Latin roots, \"tri- / tres\" and \"pālus\" – literally, \"three stakes\") is a Latin term believed to name a torture instrument consisting of \"three stakes\" [...] "
            "The original usage of tripalium is still unclear. [...] "
            "The earliest references from the ancient Roman era use the term to describe a wooden structure designed to securely immobilize a large \"fiery animal\" (horse, oxen, cow) during examination or care. "
            "In addition to livestock animals, violent men and women who were thought to behave like a fiery bull had their arms and legs tied down to a tripalium. "
            "In a 582 CE text, the Council of Auxerre, tripalium is used in the context of forbidding clerics to assist torture sessions, and is described as an instrument involving three stakes used to punish only slaves. [...] "
            "Travail is still used in France to describe a wooden structure used by farriers for horse care. [...] "
            "A majority of scholars believe these words to be reflexes of Latin \"tripalium\". "
            "However, this theory has been contested by a small minority, who argue that an irregularity in the development of the first syllable, which is consistent across all reflexes, points to a different etymological origin.",
            nome="Tripalium")],
    },
    # 4 azulejo não vem de azul
    {
        "temas_secundarios": ["arquitetura", "mundo_islamico_medieval", "palavras_viajantes"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "\"Azulejo\" parece vir de \"azul\", mas vem do árabe \"al-zillīj\", \"pedra polida\": a ideia original era imitar os mosaicos romanos e bizantinos.",
        "explicacao": (
            "Como tantos azulejos portugueses são azuis e brancos, é natural pensar que o nome vem da cor. Mas a "
            "palavra vem do árabe \"al-zillīj\", que significa \"pedra polida\", porque a ideia original era imitar "
            "os mosaicos romanos e bizantinos. Na Península Ibérica, a grande produção de azulejos de tradição hispano-mourisca se "
            "concentrou em Sevilha, na Espanha. Portugal adotou a técnica depois que o rei D. Manuel I visitou "
            "Sevilha, em 1503, e os azulejos passaram a cobrir paredes e pisos, como na Sala dos Árabes do Palácio "
            "Nacional de Sintra. Além de enfeitar, eles tinham uma função prática: ajudavam a controlar a "
            "temperatura das casas. Hoje, em português e em espanhol, \"azulejo\" é a palavra comum para "
            "qualquer ladrilho, de qualquer cor."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Azulejo",
            "is a form of Iberian painted tin-glazed ceramic tilework. "
            "They are an ornamental art form, but also had a specific function, such as aiding temperature control in homes. [...] "
            "In Spanish and Portuguese, azulejo is the everyday word for (any) tile. [...] "
            "is derived from the Arabic الزليج (al-zillīj), zellij meaning \"polished stone\" because the original idea was to imitate the Byzantine and Roman mosaics. [...] "
            "The Spanish city of Seville became the major centre of the Hispano-Moresque tile industry. [...] "
            "The same techniques were introduced into Portugal by King Manuel I after a visit to Seville in 1503. "
            "They were applied on walls and used for paving floors, as can be seen in several rooms, especially the Arab Room of the Sintra National Palace",
            nome="Azulejo")],
    },
    # 5 "esquerda" veio do basco
    {
        "temas_secundarios": ["linguas_mundo", "historia_portugues"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "\"Esquerda\" provavelmente veio do basco, língua sem parentesco conhecido com nenhuma outra. É o empréstimo basco mais forte do português e do espanhol.",
        "explicacao": (
            "O basco, falado nos dois lados dos Pireneus, é a única língua isolada conhecida da Europa: não se "
            "conhece parentesco dela com nenhuma outra língua. Já se atribuíram ao basco muitas palavras do espanhol e do português, mas "
            "a maioria tem explicações mais simples a partir do latim, ou derivações bascas pouco convincentes. "
            "Deixando de lado os termos culturais, sobra um candidato forte: o basco \"ezker\", há muito tempo "
            "considerado a origem do português \"esquerdo\", do espanhol \"izquierdo\" e do catalão \"esquerre\". "
            "A maioria dos estudiosos considera o basco o último descendente de uma das línguas faladas na Europa "
            "pré-histórica, antes da chegada das línguas indo-europeias, como o latim. Ou seja, para nomear um dos "
            "dois lados do corpo, o português usa uma palavra que provavelmente vem dessa camada mais antiga."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Basque_language",
            "Basque is Europe's only known language isolate (with no relation to any other known languages) [...] "
            "Most scholars believe Basque to be the last remaining descendant of one of the pre-Indo-European languages of prehistoric Europe. [...] "
            "most of them have more easily-explained Romance etymologies or not particularly convincing derivations from Basque. "
            "Ignoring cultural terms, there is one strong loanword candidate, ezker, long considered the source of the Pyrenean and Iberian Romance words for \"left (side)\" (izquierdo, esquerdo, esquerre).",
            nome="Basque language")],
    },
    # 6 saudade vem de solidão
    {
        "temas_secundarios": ["emocoes", "literatura"],
        "tipos_espanto": ["origem_inesperada"],
        "gancho": "\"Saudade\" vem do latim \"solitatem\", solidão. Passou por \"soidade\" e \"soudade\" e só ganhou a forma atual por influência de \"saúde\" e \"saudar\".",
        "explicacao": (
            "Saudade é uma das palavras mais presentes na poesia de amor em português e em galego e na música "
            "popular. Descreve uma mistura de perda, falta, distância e amor. A origem dela não tem nada de "
            "alegre: vem do latim \"solitatem\", que quer dizer solidão. No galego-português medieval, virou "
            "\"soidade\", que deu as formas antigas \"soidade\" e \"soudade\". Foi a influência de duas palavras "
            "parecidas e de sentido bem diferente, \"saúde\" e \"saudar\", que puxou o som para \"saudade\". Ou "
            "seja, a palavra que se costuma apresentar como intraduzível começou como um nome comum para estar "
            "sozinho."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Saudade",
            "Saudade é uma das palavras mais presentes na poesia de amor da língua portuguesa e da galega e também na música popular. "
            "\"Saudade\" descreve a mistura dos sentimentos de perda, falta, distância e amor. "
            "A palavra vem do latim \"solitatem\" (solidão), passando pelo galego-português \"soidade\", que deu origem às formas arcaicas \"soidade\" e \"soudade\", que sob influência de \"saúde\" e \"saudar\" deram origem à palavra atual.",
            nome="Saudade", idioma="pt")],
    },
    # 7 ônibus, "para todos"
    {
        "temas_secundarios": ["transportes", "cidades"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "\"Ônibus\" é latim: \"omnibus\" quer dizer \"para todos\". O nome surgiu em 1823, num serviço de carruagens em Nantes, na França, e a origem exata ainda tem duas versões.",
        "explicacao": (
            "Em 1823, Stanislas Baudry abriu em Nantes, na França, um serviço de carruagens puxadas a cavalo para "
            "transportar passageiros. É indiscutível que a palavra \"omnibus\" nasceu com a empresa dele. A "
            "versão mais famosa, contada por um museu de transportes, diz que em frente ao ponto inicial havia a "
            "loja de um chapeleiro chamado Omnès, que tinha posto na fachada o trocadilho latino \"Omnès "
            "Omnibus\", \"para todos\". Os moradores teriam passado a chamar o veículo pelo nome da placa. O "
            "problema é que não há registro de nenhum chapeleiro Omnès naquela rua. Em 1892, o filho do guarda-"
            "livros de Baudry contou outra história: Baudry chamava suas carruagens de \"Damas brancas\", e quando "
            "os críticos disseram que o nome não fazia sentido, ele respondeu, em latim, que então seriam "
            "carruagens \"omnibus\", para todos. O nome pegou na hora. Depois, os veículos a motor herdaram a "
            "palavra, que em inglês encolheu para \"bus\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Horse-drawn_omnibus",
            "According to the Museum of Urban, Interurban and Rural Transport, the name \"omnibus\" comes from a shop located in front of the first carriage transport service opened in Nantes, France by Stanislas Baudry in 1823. "
            "A hatter named Omnès had named his shop \"Omnès Omnibus\"—a pun on the Latin omnes omnibus, meaning \"for all\". [...] "
            "Though it is undisputed that the term arose with Stanislas Baudry's company, there is no record of any Omnès hatter living in that street. "
            "In 1892, the son of Baudry's bookkeeper wrote in the Bulletin de la Société archéologique de Nantes that omnibus had a simpler origin. "
            "Baudry used to call his horsecars Dames blanches (White ladies), a name which, critics told him, made no sense. "
            "He then replied, with the Latin word: \"Then, these are omnibus cars!\" (cars for all). The name caught on immediately.",
            nome="Horse-drawn omnibus"),
            wiki("Omnibus", "Bus, short for motor omnibus, a road vehicle designed to carry passengers."),
        ],
    },
    # 8 você era tratamento de rei
    {
        "temas_secundarios": ["historia_portugues", "costumes_rituais"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "\"Você\" começou como \"vossa mercê\", tratamento dado aos reis de Portugal. Foi descendo na escala social até que, no século XIX, um comerciante se ofendeu por ser chamado de você.",
        "explicacao": (
            "\"Você\" é o resultado de um longo desgaste: \"vossa mercê\" virou \"vosmecê\", depois \"vancê\" e, por "
            "fim, \"você\". \"Mercê\" quer dizer graça, concessão. No começo, era o tratamento elevado dado aos "
            "reis de Portugal, na primeira dinastia e no início da seguinte. No século XV, os reis passaram a "
            "exigir \"alteza\", e a \"mercê\" foi descendo para as grandes figuras do reino e depois para os "
            "fidalgos entre si. O mesmo aconteceu com os títulos seguintes: quando os reis adotaram "
            "\"majestade\", a \"excelência\" e a \"senhoria\" foram descendo um degrau cada. No século XIX, o "
            "\"vosmecê\" estava tão banalizado que o escritor Camilo Castelo Branco contou, rindo, que seu "
            "merceeiro tinha se ofendido por ser chamado de você: queria ser tratado por senhoria. Hoje, no "
            "Brasil, \"você\" é a forma comum para quase todo mundo, enquanto em boa parte de Portugal ainda soa "
            "distante e formal."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Voc%C3%AA",
            "Sua origem etimológica encontra-se na expressão de tratamento de deferência vossa mercê, que se transformou sucessivamente em , vosmecê, vancê e você. "
            "Vossa mercê (mercê significa graça, concessão) [...] "
            "Inicialmente, mercê era o elevado tratamento dado na terceira pessoa aos reis de Portugal, durante a dinastia de Borgonha, e inícios da dinastia de Avis que se lhe seguiu. "
            "No século XV, quando os soberanos portugueses adotaram o chamamento de alteza (vossa alteza, sua alteza) foi o título de mercê começado a ser dado às principais figuras do Reino, nas principais casas fora da Família Real, generalizando-se a dado passo como forma de tratamento adotada pelos fidalgos entre si. [...] "
            "o alargado e diminuído tratamento de vossa mercê, contraído no seu uso coloquial em vossemecê, e vosmecê, já estava tão generalizado na Lusofonia que Camilo Castelo Branco ironiza a respeito, escrevendo de modo risonho que o seu merceeiro se ofendera por ele corajosamente o ter tratado por você. "
            "Segundo Camilo, o lojista quereria ser tratado por senhoria [...] "
            "Apesar do uso generalizado do \"você\", tanto no brasil como no Alentejo e na Madeira, em grande parte de Portugal há um uso muito peculiar do pronome, maioritamente para mostrar distanciamento, formalidade e menos intimidade.",
            nome="Você", idioma="pt")],
    },
    # 9 palavras do quimbundo
    {
        "temas_secundarios": ["heranca_africana", "musica_brasileira"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "\"Cafuné\", \"bunda\" e talvez \"samba\" vieram do quimbundo, língua de Angola. \"Samba\" se liga ao \"semba\" angolano, de uma palavra para a umbigada da dança.",
        "explicacao": (
            "O quimbundo é uma língua banta falada em Angola. Algumas palavras do português vêm dele. \"Cafuné\", o carinho de passar os dedos "
            "devagar pelo cabelo de alguém, vem de \"kifuné\". \"Bunda\" vem de \"mbunda\". O nome de Zumbi, o "
            "líder de Palmares, vem de \"nzumbi\", \"espírito\", ou talvez de \"nzambi\", \"deus\". E o semba, "
            "música e dança tradicional de Angola, aparentado do samba brasileiro, tira o nome da palavra "
            "\"semba\", a umbigada, o encontro de barrigas que marca a dança. Em Angola, o português de hoje tem "
            "ainda outras palavras de origem quimbunda, como \"bué\", \"muito\", e \"cota\", \"pessoa mais "
            "velha\"."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "consenso_parcial",
        "fontes": [wiki("Kimbundu_language",
            "There is a small number of words of Kimbundu origin, and many of those are indirect and come via Angolan Portuguese. "
            "bué (pronounced [bwɛ], \"very, a lot\"), cota ([ˈkɔtɐ], \"old person\") mambo ([ˈmɐ̃bu]) Zumbi (\"zombie\"; is the name of the quilombo leader or chief Zumbi dos Palmares), it comes from Kimbundu nzumbi (\"ghost\", \"spirit\") or even nzambi (\"god\"). "
            "Semba, is a traditional Angolan music and type of dance and it is also related to the Brazilian dance style samba ; it comes from Kimbundu semba (\"belly-bump\"). "
            "Cafuné (\"caress\", it is usually passing one's fingers softly through someone's hair or some specific parts in the body), comes from Kimbundu kifuné. "
            "Bunda (\"buttocks\") it originates from Kimbundu mbunda.",
            nome="Kimbundu language")],
    },
    # 10 pipoca, a pele estourada
    {
        "temas_secundarios": ["povos_indigenas", "ciencia_cozinha"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "\"Pipoca\" vem do tupi \"pipoka\", \"pele estourada\". O nome descreve bem o que acontece: a umidade do grão vira vapor e a pressão arrebenta a casca.",
        "explicacao": (
            "A pipoca é feita de uma variedade especial de milho, o milho-pipoca, de grãos pequenos e com amido "
            "duro. Quando o grão é aquecido depressa, a água que existe dentro dele vira vapor. A casca dura "
            "segura a pressão até certo ponto e então arrebenta, e o interior se transforma numa massa leve de "
            "amido e fibras. O nome em português é uma descrição desse processo, feita em tupi: \"pipoka\" junta "
            "\"pira\", pele, e \"pok\", estourar, mais um sufixo que forma o substantivo. É a pele estourada. Em "
            "algumas regiões também se diz \"popoca\", e no Pará a pipoca pode ser chamada de \"pororoca\"."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Pipoca",
            "Pipoca ou popoca (no Pará também chamada pororoca) é um prato feito a partir de uma variedade especial de milho, o milho-pipoca (Zea mays everta), que estoura quando aquecido. "
            "Ao se aquecer os grãos desse milho de maneira rápida, a sua humidade interna é convertida em vapor. "
            "Num determinado ponto, a pressão estoura a casca externa, transformando a parte interna numa massa pouco consistente de amidos e fibras. [...] "
            "\"Pipoca\" originou-se do termo tupi pipoka, \"pele estourada\", formado pela junção de pira (pele), pok (estourar) e a (sufixo substantivador). [...] "
            "Apresenta, como característica, grãos pequenos contendo amido duro ou cristalino.",
            nome="Pipoca", idioma="pt")],
    },
    # 11 oxalá = se Deus quiser
    {
        "temas_secundarios": ["mundo_islamico_medieval", "religioes", "palavras_viajantes"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "Quem diz \"oxalá\" está falando árabe sem saber: a palavra vem de \"in sha Allah\", \"se Deus quiser\", e é prima do espanhol \"ojalá\".",
        "explicacao": (
            "A expressão árabe \"in sha Allah\" quer dizer, literalmente, \"se Deus quiser\". Ela é usada por "
            "muçulmanos, por cristãos árabes e por falantes de árabe de outras religiões quando se fala de algo "
            "que se espera que aconteça no futuro, com um sentido parecido com o de \"tomara\". O português e o "
            "espanhol tomaram a expressão emprestada, como \"oxalá\" e \"ojalá\", e as usam do mesmo jeito: para "
            "desejar que algo dê certo. No árabe falado no dia a dia, a expressão também ganhou outro uso: muitas "
            "vezes indica incerteza ou falta de compromisso firme, como uma resposta em aberto a um pedido ou "
            "promessa."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Inshallah",
            "the phrase is more generally and more commonly used by Muslims, Arab Christians, and Arabic speakers of other religions to refer to events that one hopes will happen in the future, having the same meaning as the English word \"hopefully\". "
            "In the Iberian languages, the expression was borrowed as oxalá or ojalá, and it is used in a similar way. "
            "Although the Arabic phrase directly translates to \"God willing\", its meaning depends on the context. [...] "
            "in everyday speech, it is frequently used to suggest uncertainty, a lack of firm commitment, or as an open-ended response to requests or promises.",
            nome="Inshallah")],
    },
]
