LOTE = "2026-11-19-heranca_africana-01"
AREA = "brasil"
TEMA = "heranca_africana"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o Cais do Valongo, enterrado duas vezes
    {
        "temas_secundarios": ["imperios_coloniais", "cidades"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "O cais por onde até 900 mil africanos escravizados entraram no Rio foi soterrado duas vezes: primeiro para receber a noiva de Pedro II, depois numa reforma urbana. Só reapareceu em 2011.",
        "explicacao": (
            "O Cais do Valongo começou a ser construído em 1811, na zona portuária do Rio, para o desembarque de "
            "africanos escravizados. A UNESCO estima que até 900 mil cativos tenham entrado nas Américas por ali. O "
            "mercado de escravizados já tinha sido transferido para a região em 1774, por ordem do vice-rei, o "
            "marquês do Lavradio, incomodado com o costume de os recém-chegados entrarem na cidade pelas ruas "
            "principais, doentes e nus. Com a proibição do tráfico em 1831, o cais foi fechado e os desembarques "
            "passaram a portos clandestinos. Em 1843, um aterro de 60 centímetros cobriu o Valongo para a "
            "construção de um novo atracadouro, destinado a receber a princesa Teresa Cristina, futura esposa de "
            "D. Pedro II: nascia o Cais da Imperatriz. Esse também acabou enterrado, em 1911, na reforma urbana "
            "do prefeito Pereira Passos. Em 2011, escavações da revitalização da zona portuária para a Olimpíada "
            "de 2016 encontraram os dois cais, um em cima do outro, junto com muitos amuletos e objetos de culto do "
            "Congo, de Angola e de Moçambique. Em 2017, o sítio virou Patrimônio Mundial. Para a UNESCO, é o "
            "vestígio físico mais importante da chegada de africanos escravizados ao continente americano."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://whc.unesco.org/en/list/1548", "titulo": "Valongo Wharf Archaeological Site (UNESCO World Heritage Centre)", "idioma": "en",
             "trecho": "The wharf started being built in 1811 to facilitate the debarkation of enslaved Africans arriving in Brazil. "
                       "It is estimated that up to 900,000 African captives entered the Americas via Valongo. [...] "
                       "It is the most important physical trace of the arrival of African slaves on the American continent."},
            wiki("Valongo_Wharf",
                "In 1774, a new legislation established the transfer of this market to the region of Valongo, on the initiative of the second Marquis of Lavradio [...] "
                "alarmed at \"The terrible custom of as soon as the blacks disembark in the port from the African coast, enter the city through the main public thoroughfares, not only loaded with innumerable diseases but naked\". [...] "
                "In 1831, the transatlantic slave trade was banned, under pressure from England, and Valongo was closed. The traffickers then proceeded to make the landings in clandestine ports. "
                "In 1843, a 60-centimeter thick embankment was made on the dock of Valongo for the construction of a new anchorage, destined to receive Princess Teresa Cristina, future wife of D. Pedro II. "
                "The wharf was then renamed 'Cais da Imperatriz'. But this also would eventually be buried in 1911, during the urban reform undertaken by mayor Pereira Passos. [...] "
                "In 2011, during excavations carried out as part of revitalization efforts in advance of the 2016 Summer Olympic Games, the two wharfs - Valongo and Imperatriz - were discovered, one on top of the other, and, along with them, a large number of amulets and worship objects from Congo, Angola and Mozambique. [...] "
                "The Valongo wharf was officially designated a World Heritage Site in July 2017.",
                nome="Valongo Wharf"),
        ],
    },
    # 2 o Cemitério dos Pretos Novos, achado numa reforma
    {
        "temas_secundarios": ["cidades", "imperios_coloniais"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Em 1996, ao reformar um casarão na Gamboa, no Rio, os donos acharam ossos humanos no solo. Era o Cemitério dos Pretos Novos, onde se calcula que 20 a 30 mil africanos recém-chegados foram enterrados.",
        "explicacao": (
            "\"Pretos novos\" era o nome dado aos africanos que acabavam de chegar ao Rio pelo Cais do Valongo e eram "
            "postos à venda no mercado de escravizados. Quase todos desembarcavam muito debilitados, e uma parte "
            "significativa não resistia às condições da travessia do Atlântico ou do próprio mercado. Entre 1769 e "
            "1830, esses mortos foram enterrados num cemitério criado por ordem do vice-rei, o marquês do Lavradio, "
            "num dos barracões do antigo mercado negreiro, na então Rua do Cemitério. Nos seis últimos anos de "
            "funcionamento, segundo os arquivos da igreja, a média passou de mil enterros por ano. O mercado fechou "
            "em 1830, em parte por causa das queixas de mau cheiro dos vizinhos e em parte para mostrar aos ingleses "
            "que o tratado contra o tráfico estava sendo respeitado. Na prática, a atividade só mudou de endereço. "
            "Em 8 de janeiro de 1996, os proprietários de um casarão do século XVIII na atual Rua Pedro Ernesto "
            "sondaram o solo para uma reforma e encontraram fragmentos de ossos humanos misturados a cerâmica, vidro "
            "e ferro. Hoje o local abriga o Instituto de Pesquisa e Memória Pretos Novos. Em 2017, foi achado ali o "
            "primeiro esqueleto inteiro: o de uma mulher morta com cerca de 20 anos no início do século XIX, que "
            "recebeu o nome de Josefina Bakhita."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Cemitério_dos_Pretos_Novos",
            "Localiza-se nos números 32, 34 e 36 da Rua Pedro Ernesto, em um casarão do século XVIII. [...] "
            "É administrado pelo Instituto de Pesquisa e Memória Pretos Novos. [...] "
            "Pretos Novos era o nome dado aos escravos recém-chegados ao Rio de Janeiro pelo Cais do Valongo e que eram negociados no mercado de vendas de escravizados. [...] "
            "O denominado Cemitério dos Pretos Novos funcionou, entre 1769 e 1830, em um dos barracões do antigo mercado negreiro [...] "
            "O barracão era situado na Rua do Cemitério, atual Rua Pedro Ernesto. O cemitério foi criado por ordem de Luís Melo Silva Mascarenhas, o marquês do Lavradio, então vice-rei do Brasil [...] "
            "Nessas viagens, praticamente todo o negro que chegava na então colônia portuguesa encontrava-se muito debilitado. "
            "Uma porcentagem significativa destes cativos imigrantes africanos não resistia às condições desumanas da travessia do Atlântico ou do mercado de escravos [...] "
            "Calcula-se que foram enterrados, no Cemitério dos Pretos Novos, pelo menos entre 20.000 e 30.000 pessoas. [...] "
            "Nos seus últimos seis anos de funcionamento, segundo pesquisa feita nos arquivos da igreja, a média de enterros no Cemitério dos Pretos Novos foi superior a mil enterros por ano. "
            "Em 1830, o mercado foi fechado, em parte pelo inconveniente das atividades e pelo mau cheiro, que eram objeto de reclamações por parte dos moradores locais, e também como uma forma de as autoridades locais mostrarem, aos ingleses, que estavam respeitando o tratado de extinção do tráfico [...] "
            "Na realidade, porém, a atividade só mudou de endereço. "
            "O achado arqueológico do Cemitério dos Pretos Novos ocorreu no dia 8 de janeiro de 1996. "
            "Os proprietários da sede do instituto resolveram reformar o imóvel do qual são donos e, ao ser feita a sondagem o solo para as obras, foram encontrados fragmentos de ossos humanos misturados a vestígios de cerâmica, vidro, ferro e outros materiais. [...] "
            "Cinco anos depois, em 2017, o primeiro esqueleto inteiro foi encontrado no local. [...] "
            "A ossada é de uma mulher, batizada de Josefina Bakhita, que morreu com aproximadamente 20 anos no início do século XIX.",
            nome="Cemitério dos Pretos Novos", idioma="pt")],
    },
    # 3 Brasil x EUA: 8 vezes mais africanos, população menor
    {
        "temas_secundarios": ["imperios_coloniais", "comercio_rotas"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "O Brasil recebeu cerca de 4,9 milhões de africanos escravizados; os EUA, uns 600 mil. Mesmo assim, em 1860 os EUA tinham 4 milhões de escravizados. A diferença estava em quanto se morria aqui.",
        "explicacao": (
            "Estima-se que cerca de 12,75 milhões de africanos tenham sido embarcados em navios negreiros rumo às "
            "Américas, e que até 2 milhões tenham morrido na viagem. Para os Estados Unidos foram uns 600 mil, "
            "cerca de 5% do total. Para o Brasil, cerca de 4,9 milhões. Ainda assim, o censo americano de 1860 "
            "contou 4 milhões de escravizados. A explicação é demográfica. Nos EUA, os africanos levados pelo "
            "tráfico atlântico tinham número equilibrado de homens e mulheres, e a população escravizada crescia por "
            "reprodução, o que os senhores chamavam de \"aumento natural\": segundo o historiador Michael Tadman, "
            "cerca de 25% por década antes da Guerra Civil. No Brasil e no Caribe, ao contrário, era comum uma queda "
            "natural de 20% por década, resultado do trabalho pesado e da alimentação insuficiente. Os senhores de "
            "engenho preferiam mão de obra masculina e, com tantas mortes, importavam mais cativos sempre que havia "
            "oferta. A expectativa de vida era curta e a população precisava ser reposta sem parar. Por isso, até "
            "1800 e mesmo depois, os nascidos na África, e não os nascidos aqui, eram a maioria dos escravizados "
            "do Brasil."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Atlantic_slave_trade",
                "The current estimate is that about 12.75 million Africans were loaded onto slave ships for transportation to the Americas. Of these, up to 2 million died during the voyage. [...] "
                "The growing demand for sugar and the natural decrease of the slave population (a result of the routine of hard labor and an inadequate diet) were the main drivers for the expansion of the transatlantic slave trade. "
                "Michael Tadman says that among the enslaved population in the antebellum US there was a natural increase of about 25 percent per decade. "
                "In stark contrast to this statistic, Brazilian and Caribbean slaves commonly suffered rates of natural decrease of 20 percent per decade. "
                "By 1800 and even afterwards, Africans, rather than Creoles (those born in-country), composed a majority of the slave populations of Brazil and of the British and French Caribbean. "
                "According to Tadman, sugarcane planters would always demand a predominantly male workforce and would always seek to import slaves when a supply was available because of the high rates of natural decrease in sugar-producing areas.",
                nome="Atlantic slave trade"),
            wiki("Slavery_in_the_United_States",
                "the slave population transported by the Atlantic slave trade to the United States was sex-balanced. [...] "
                "The great majority of enslaved Africans were transported to sugar plantations in the Caribbean and to Portuguese Brazil. "
                "As life expectancy was short, their numbers had to be continually replenished. "
                "Life expectancy was much higher in the United States, and the enslaved population was successful in reproduction, which was called \"natural increase\" by enslavers. "
                "The population of enslaved people in the United States grew to 4 million by the 1860 census. [...] "
                "About 600,000 slaves were transported to the United States, or 5% of the 12 million slaves taken from Africa.",
                nome="Slavery in the United States"),
            wiki("Valongo_Wharf",
                "Brazil received about 4.9 million slaves through the Atlantic trade.",
                nome="Valongo Wharf"),
        ],
    },
    # 4 agudás e tabons: os "brasileiros" da África
    {
        "temas_secundarios": ["africa_antiga", "costumes_rituais", "palavras_viajantes"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "No Benim, descendentes de africanos libertos que voltaram do Brasil festejam o Senhor do Bonfim e se cumprimentam com \"Bom dia, como passou?\". Em Gana, ficaram conhecidos como \"tabom\", de \"tá bom\".",
        "explicacao": (
            "Entre os séculos XVIII e XIX, africanos libertos no Brasil voltaram para a antiga Costa dos Escravos, "
            "que ia de Lagos, na Nigéria, até Acra, em Gana. Houve deportações depois da Revolta dos Malês de 1835, "
            "mas muitos retornos foram voluntários. O pesquisador Milton Guran calcula que de 7 mil a 8 mil "
            "retornados se instalaram na região a partir de 1835. Em geral, não voltavam para a terra onde tinham "
            "nascido, por medo ou porque seu povo já não existia. No Benim, no Togo e na Nigéria, eles e seus "
            "descendentes ficaram conhecidos como agudás, palavra derivada de Ajudá, nome português da cidade de "
            "Uidá, ou simplesmente como \"brasileiros\". Têm sobrenomes como Souza, Silva e Almeida, dançam a "
            "burrinha, uma forma arcaica do bumba-meu-boi, fazem desfiles de Carnaval e se reúnem em torno de uma "
            "feijoada. Os mais velhos ainda trocam o cumprimento \"Bom dia, como passou?\" e respondem \"Bem, "
            "'brigado'\". Na Ilha de Lagos, o estilo dos sobrados coloniais brasileiros trazido pelos retornados "
            "dominava a arquitetura no fim do século XIX. Em Acra, os ex-escravizados que chegaram no século XIX só "
            "falavam português e usavam tanto a expressão \"tá bom\" que o povo gã passou a chamá-los de tabom."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Agudás",
                "Agudás ou amarôs são os os africanos descendentes de escravizados libertos no Brasil entre os séculos XVIII e XIX que retornaram à África ocidental e se restabeleceram na região da antiga Costa dos Escravos, que ia aproximadamente da cidade de Lagos, na Nigéria, até Acra, em Gana [...] "
                "ficaram conhecidos na Nigéria, no Benim e no Togo como \"agudás\", \"amarôs\" ou simplesmente \"brasileiros\" [...] "
                "O termo “agudá” é uma corruptela em iorubá, fon ou mina de Ajudá, nome português da cidade de Uidá [...] "
                "Possuem nomes de família como Souza, Silva, Almeida, entre outros, festejam Nosso Senhor do Bonfim, dançam a burrinha (uma forma arcaica do bumba-meu-boi), fazem desfiles de Carnaval e se reúnem frequentemente em torno de uma feijoada ou de um kousidou. "
                "Ainda hoje é comum os agudás mais velhos se cumprimentarem com um sonoro “Bom dia, como passou?” “Bem, ‘brigado’” é a resposta. [...] "
                "O primeiro momento foi após a Revolta dos Malês que aconteceu na Bahia em janeiro de 1835, em medida repressiva os escravos que participaram da revolta foram deportados para seu continente de origem. [...] "
                "Essa volta era voluntária e espontânea ligada à memória da pátria de origem. [...] "
                "Ao retornarem à África, não voltavam para a região em que nasceram ou que saíram. "
                "Havia diversos motivos: a tribo já ter sido eliminada ou por terem medo de retornar [...] "
                "Milton Guran calcula que entre 7000 e 8000 são o número de retornados a se instalarem na região nesse segundo momento de chegada maciça dos antigos escravos, a partir de 1835. [...] "
                "O estilo brasileiro de arquitetura tornou-se dominante na Ilha de Lagos no final do século XIX.",
                nome="Agudás", idioma="pt"),
            wiki("Tabom_people",
                "The Tabom are a community of Afro-Brazilian descendants who lives in Accra, the capital of Ghana, consisting of the descendants of former enslaved people who, after being freed in Brazil, returned to Africa in the 19th century. "
                "When they arrived in Jamestown, the oldest, seaside neighborhood of Accra, the former slaves and their descendants could speak only Portuguese, and would conspicuously use the phrase \"Tá bom\" (\"Okay\"), so the local Gã people, who primarily inhabited Accra, started to call them the \"Tabom\".",
                nome="Tabom people"),
        ],
    },
    # 5 o Chachá de Uidá
    {
        "temas_secundarios": ["africa_antiga", "imperios_coloniais", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Um traficante de escravizados nascido em Salvador ajudou um príncipe a tomar o trono do Daomé, na África, e ganhou o título de chachá. Na cidade de Uidá, no Benim, ele tem estátua, praça e museu da família.",
        "explicacao": (
            "Francisco Félix de Souza nasceu em Salvador em 1754 e se mudou para a região do atual Benim. Lá "
            "negociou óleo de dendê, ouro e, sobretudo, pessoas escravizadas, a ponto de já ter sido chamado de \"o "
            "maior traficante de escravos\". Depois de ser preso pelo rei Adandozan, do Daomé, ajudou Ghezo a subir "
            "ao trono num golpe de Estado. Com o novo rei, tornou-se o chachá de Uidá, o grande porto negreiro da "
            "região. O título não dava poderes oficiais, mas impunha respeito no reino. Uma explicação curiosa para "
            "a palavra é que ela viria do hábito dele de dizer \"já, já\", prometendo que algo seria feito na hora. "
            "Católico, também praticava o vodum e mantinha um santuário da família. Seguiu no tráfico mesmo depois "
            "da proibição na maioria dos lugares, tinha fama de ter pelo menos 80 filhos e morreu em 1849, sendo "
            "sepultado no Daomé. Hoje é considerado o \"pai\" de Uidá e um patriarca fundador das comunidades "
            "afro-brasileiras de Gana, Togo, Benim e Nigéria. A família De Souza deu ao Benim um presidente, "
            "Paul-Emile de Souza. A vida dele inspirou o romance O Vice-Rei de Uidá, de Bruce Chatwin, que virou o "
            "filme Cobra Verde, de Werner Herzog, com Klaus Kinski."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Francisco_Félix_de_Sousa",
            "Francisco Félix de Souza (5 October 1754 – 8 May 1849) was a Brazilian slave trader who was deeply influential in the regional politics of pre-colonial West Africa (now Benin, Togo and Nigeria). [...] "
            "went on to become the \"chachá\" of Ouidah (the slave-trading hub for the region), a title that conferred no official powers but commanded local respect in the Kingdom of Dahomey, where, after being jailed by King Adandozan of Dahomey, he helped Ghezo ascend the throne in a coup d'état. "
            "He became chacha to the new king, a curious phrase that has been explained as originating from his saying \"(...) já, já.\", a Portuguese phrase meaning something will be done right away. [...] "
            "Souza was a major slave trader and merchant who traded in palm oil, gold and slaves. He migrated from Brazil to what is now the African republic of Benin. He has been called \"the greatest slave trader\". "
            "Trading slaves from what was then the Dahomey region, Souza was known for his extravagance and was reputed to have had at least 80 children with women in his harem. "
            "He continued to market slaves after the trade was abolished in most jurisdictions. [...] "
            "Although a Catholic, he practiced the Vodun religion, and had his own family shrine. He was buried in Dahomey. [...] "
            "Born in Salvador, Bahia, then the capital of Portuguese America, De Souza is regarded as the \"father\" of the city of Ouidah. "
            "The city has a statue of him, a plaza named after him, and a museum dedicated to the de Souza family. [...] "
            "Today he is known as a founding patriarch of the Afro-Brazilian communities in Ghana, Togo, Benin and Nigeria. [...] "
            "Figures like Paul-Emile de Souza, a president of Benin [...] "
            "Bruce Chatwin's 1980 novel The Viceroy of Ouidah was loosely based on de Souza's life [...] "
            "The book was adapted into the 1987 film Cobra Verde, directed by Werner Herzog and starring Klaus Kinski.",
            nome="Francisco Félix de Sousa")],
    },
    # 6 Luiz Gama, vendido pelo pai
    {
        "temas_secundarios": ["personagens_esquecidos", "leis_julgamentos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Luiz Gama nasceu livre, mas aos 10 anos foi vendido como escravo pelo próprio pai, endividado no jogo. Só aprendeu a ler aos 17. Sem diploma, virou advogado e tirou centenas de pessoas do cativeiro.",
        "explicacao": (
            "Gama nasceu em Salvador, filho de uma africana liberta e de um fidalgo português. Em 1840, o pai, cheio "
            "de dívidas de jogo, o vendeu como escravo. Já adulto, Gama entendeu que tinha sido vítima de um crime "
            "previsto no Código Criminal do Império: escravizar uma pessoa livre. Posto à venda, era rejeitado por "
            "ser baiano: depois da Revolta dos Malês, criou-se o estigma de que os cativos da Bahia eram rebeldes "
            "e propensos a fugir. Acabou levado a São Paulo. Em 1847, um estudante de direito hospedado na casa do "
            "senhor lhe ensinou o alfabeto, e no ano seguinte ele conseguiu provar sua liberdade, por meios que "
            "até hoje não estão claros. Trabalhando depois na polícia, estudou direito por conta própria, porque os "
            "alunos da Faculdade do Largo de São Francisco impediram sua matrícula, e se tornou rábula, nome dado a "
            "quem tinha conhecimento para advogar mesmo sem diploma. O chamado \"estilo Gama\" era provar que os "
            "africanos que defendia tinham chegado depois da lei de 1831 contra o tráfico e, portanto, eram "
            "livres. Numa carta, estimou ter libertado mais de 500 pessoas, e só num processo de 1869 garantiu a "
            "liberdade de 217. Em 2015, 133 anos depois de sua morte, a OAB de São Paulo lhe concedeu o título de "
            "advogado."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Luís_Gama",
            "Born to a free black mother and a white father, he was nevertheless made a slave at the age of 10, and remained illiterate until the age of 17. [...] "
            "it is known that he was the son of Luísa Mahin, a freed African ex-slave, and the son of a Portuguese fidalgo who lived in Bahia. [...] "
            "In 1840, his father ended up in debt with gambling, so he resorted to selling Luís Gama as a slave to pay his debts. [...] "
            "As an adult, Gama understood that when he was sold he was a victim of the crime of \"Enslaving a free person, who is in possession of his freedom.\", provided in Article 179 from Criminal Code of the Empire of Brazil [...] "
            "Put up for sale, he was rejected \"for being Bahian\". After the Malê revolt, a stigma was created that Bahian captives were rebellious and more likely to run away. [...] "
            "who took him to be resold in São Paulo. [...] "
            "In 1847, Luís Gama had contact with a law student, Antônio Rodrigues do Prado Júnior, who stayed at his master's house and taught him the alphabet. [...] "
            "Luís Gama was able to prove his freedom and joined the army in 1848. It remains unclear, however, the artifices used by Luis Gama to obtain his freedom [...] "
            "In 1856, he was hired as a clerk at the São Paulo Police Department [...] "
            "However, the students of the Faculty were against it, making it impossible for Luís Gama to enroll, so he began to study on his own [...] "
            "became a \"rábula\", the name given to the individual who had enough legal knowledge to be a lawyer, even without a law degree. [...] "
            "The so-called \"Gama style\" consisted of proving through legal proceedings that the enslaved blacks defended by Gama were brought illegally to Brazil, that is, after the promulgation of the Feijó Law in 1831, and should therefore be freed. [...] "
            "In his autobiographical letter to Lúcio de Mendonça, Gama estimates that he had already freed more than 500 slaves from captivity and in an 1869 court case known as the \"Netto Question\", Gama secured the freedom of 217 slaves [...] "
            "133 years after his death, on November 3, 2015, the Order of Attorneys of Brazil, São Paulo Section, granted him the title of \"lawyer\"",
            nome="Luís Gama")],
    },
    # 7 Esperança Garcia e a carta de 1770
    {
        "temas_secundarios": ["personagens_esquecidos", "leis_julgamentos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Em 1770, uma mulher escravizada no Piauí escreveu ao governador para denunciar as surras que ela e o filho levavam. Em 2022, a OAB reconheceu a autora, Esperança Garcia, como a primeira advogada do Brasil.",
        "explicacao": (
            "Esperança nasceu por volta de 1751 numa fazenda dos jesuítas, onde hoje fica o município de Nazaré do "
            "Piauí, e foi ali que aprendeu a ler e escrever. Quando o Marquês de Pombal expulsou a ordem, ela tinha "
            "9 anos e foi levada como escrava para a casa do capitão Antônio Vieira de Couto. Entre suas tarefas "
            "estavam fazer farinha, limpar algodão, tecer redes e extrair óleo de mamona para lamparinas. Em 6 de "
            "setembro de 1770, enviou uma petição ao governador da capitania denunciando os maus-tratos e as "
            "agressões do feitor contra ela, o filho e companheiras de cativeiro. Pedia também para voltar à "
            "fazenda de origem, onde queria batizar a filha. Pouco depois, fugiu. Ela reaparece numa lista de "
            "escravizados da Fazenda Algodões datada de 1778, casada com o angolano Ignácio. A carta foi "
            "redescoberta em 1979 e é considerada a primeira petição escrita por uma mulher na história do "
            "Brasil, além de um marco das origens da literatura afro-brasileira. O dia do envio, 6 de setembro, é "
            "o Dia Estadual da Consciência Negra no Piauí. Em 2022, o Conselho Pleno da OAB a reconheceu como a "
            "primeira advogada brasileira."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Esperança_Garcia",
                "Esperança Garcia (Fazenda Algodões, circa 1751 - ?) foi uma mulher negra escravizada brasileira, considerada a primeira mulher advogada do Brasil. "
                "Em 6 de setembro de 1770, Esperança enviou uma petição ao então presidente da Capitania de São José do Piauí, Gonçalo Lourenço Botelho de Castro, onde denuncia maus-tratos e abusos físicos contra ela, seu filho e companheiras de cativeiro, feitos pelo feitor da Fazenda Algodões. [...] "
                "Esperança nasceu em uma fazenda de propriedade dos jesuítas, onde hoje fica o município de Nazaré do Piauí. "
                "Aos 9 anos de idade, quando a ordem foi expulsa do Piauí pelo Marquês de Pombal, ela foi levada como escrava para a casa do capitão Antônio Vieira de Couto. [...] "
                "Pedia ainda para retornar à Fazenda Algodões e para ter sua filha batizada. "
                "Fugiu pouco depois, reaparecendo numa relação de trabalhadores escravizados da Fazenda Algodões, datada de 1778, casada com o angolano Ignácio [...] "
                "A carta de Esperança Garcia é considerada a primeira petição escrita por uma mulher na história do Brasil [...] "
                "Também é um documento importante na origem da literatura afro-brasileira. Na data de envio, 6 de setembro, é comemorado o Dia Estadual da Consciência Negra no Piauí. [...] "
                "Em 2022, Esperança Garcia foi reconhecida como a primeira advogada brasileira pelo Conselho Pleno da Ordem dos Advogados do Brasil (OAB).",
                nome="Esperança Garcia", idioma="pt"),
            wiki("Esperança_Garcia",
                "It was on this Jesuit plantation where she learned how to read and write. [...] "
                "Her duties as a slave included making flour, cleaning cotton, weaving hammocks, and extracting castor oil for the purpose of making lamps. [...] "
                "She described her life while as a slave “very unhappy”, and claims that she and her first son were beaten. [...] "
                "In 1979, Esperanca’s letter was rediscovered",
                nome="Esperança Garcia"),
        ],
    },
    # 8 capoeira: de crime a patrimônio
    {
        "temas_secundarios": ["esportes_tradicionais", "africa_antiga", "leis_julgamentos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "A capoeira era crime no Código Penal de 1890. Como ainda era ilegal nos anos 1920, Mestre Bimba chamou seu estilo de \"Luta Regional Baiana\". Em 2014, a roda de capoeira virou patrimônio da humanidade.",
        "explicacao": (
            "Estudiosos apontam raízes da capoeira no engolo, uma arte marcial banta praticada em Angola, embora a "
            "origem exata seja incerta e outras tradições possam ter contribuído. A primeira menção em documento "
            "oficial, de 1789, já a trata como atividade criminosa. No Rio do fim do século XIX, a capoeira de rua "
            "era uma luta mista, com cabeçadas, chutes, golpes de mão aberta, lâminas e bastões, e a navalha era a "
            "arma mais comum. O Código Penal de 1890 a listou como crime. Nos anos 1920, a repressão da polícia na "
            "Bahia empurrou a prática para uma versão mais inofensiva, quase dança. Em reação, Mestre Bimba "
            "(1899-1974) criou as primeiras sequências de ensino da capoeira, o primeiro método para aprendê-la, "
            "que até então só se aprendia olhando e entrando na roda. Como ela ainda era proibida, batizou o estilo "
            "de Luta Regional Baiana. Em 1932, com a concordância do governo baiano, abriu uma escola formal. A "
            "repressão diminuiu com Getúlio Vargas, que apostava num populismo cultural: a partir de 1937, a "
            "capoeira foi legalizada e promovida pelo Estado e virou esporte nacional oficial. Em 2014, a UNESCO "
            "inscreveu a roda de capoeira na Lista Representativa do Patrimônio Cultural Imaterial da Humanidade."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Capoeira",
                "scholars have identified roots in engolo, a traditional Bantu martial art practiced in Angola. "
                "Capoeira is first mentioned in an official document in 1789, as a criminal activity. [...] "
                "Although the exact origins of capoeira remain uncertain, some studies have suggested that engolo was one of the African traditions that may have influenced its development [...] "
                "Some authors argue that other African and Brazilian practices also contributed to the formation of capoeira, rather than a single ancestral tradition [...] "
                "The late 19th century street-fighting capoeiragem was a mixed martial art, combining five main fighting techniques: headbutts, foot kicks, open hand blows, blades, and stick techniques. "
                "The straight razor (navalha) was most common capoeira weapon [...] "
                "Capoeira was listed as a crime in the Brazilian penal code of 1890. [...] "
                "In the 1920s, capoeira in Bahia faced repression from the cavalry squadron of police chief Pedro de Azevedo Gordilho; this led to a more harmless dance version of the art form. "
                "Partly as a response to this domestication, capoeira regional began to take form in the 1920s, when Mestre Bimba (1899-1974) met his future student, José Cisnando Lima. [...] "
                "Bimba created his sequências de ensino (teaching combinations) and created capoeira's first teaching method. "
                "Advised by Cisnando, Bimba decided to call his style Luta Regional Baiana, as capoeira was still illegal at that time. [...] "
                "State repression of capoeira decreased after the military coup of Gétulio Vargas, who advocated a strategy of cultural populism. "
                "Mestre Bimba established a formal school in 1932, when the Bahia local government agreed to allow it [...] "
                "Capoeira was legalized and promoted by the Brazilian state beginning in 1937, and became an official national sport under Vargas' government.",
                nome="Capoeira"),
            wiki("Mestre_Bimba",
                "Bimba was the first to create a method of teaching to help facilitate learning because, until then, capoeira was only learned by watching and participating in the roda.",
                nome="Mestre Bimba"),
            {"url": "https://ich.unesco.org/en/RL/capoeira-circle-00892", "titulo": "Capoeira circle (UNESCO Intangible Cultural Heritage)", "idioma": "en",
             "trecho": "Inscribed in 2014 (9.COM) on the Representative List of the Intangible Cultural Heritage of Humanity"},
        ],
    },
    # 9 Tia Ciata: choro na sala, samba no quintal
    {
        "temas_secundarios": ["musica_brasileira", "religioes"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "No Rio do início do século XX, a polícia perseguia o samba. Na casa da baiana Tia Ciata, o choro tocava na sala da frente, à vista de todos, e os tambores do samba ficavam escondidos no quintal.",
        "explicacao": (
            "Hilária Batista de Almeida nasceu em 1854 em Santo Amaro, na Bahia, e foi iniciada no candomblé em "
            "Salvador. Chegou ao Rio em 1876, aos 22 anos, trabalhou numa barraca de comida e foi morar na região "
            "da Praça Onze, que ficou conhecida como Pequena África. Devota de Oxum, tornou-se a segunda líder mais "
            "importante do terreiro de João Alabá. Apesar das liberdades individuais prometidas pela Constituição "
            "de 1891, a polícia perseguia músicos negros e praticantes de religiões afro-brasileiras. Um samba de "
            "verdade pedia tambores, que eram associados aos cultos. Ciata aprendeu a driblar a repressão: punha os "
            "sambistas nos fundos da casa, a parte mais escondida, e deixava na sala de entrada, o espaço mais "
            "visível e audível, músicos de sopro e corda tocando choro, considerado mais erudito. Quando a polícia "
            "chegava, ela dizia que era uma reunião de choro, e em geral a noite seguia normalmente. Pelo quintal "
            "passaram futuros gigantes como Pixinguinha, João da Baiana e Heitor dos Prazeres, e a casa é apontada "
            "como um dos possíveis berços do samba. Conta-se ainda que o presidente Venceslau Brás, com uma "
            "infecção na perna que nenhum médico curava, recorreu aos tratamentos com ervas de Ciata por "
            "recomendação de um assessor."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Tia_Ciata",
            "a Brazilian mãe-de-santo of Candomblé, and an influential figure in the development of samba. "
            "She was a devotee of the deity Oshun and became the iyakekerê, or second most important leader, in the terreiro of João Alabá in Rio de Janeiro. [...] "
            "Hilária Batista de Almeida was born in 1854 in Santo Amaro, Bahia, and initiated in the Candomblé religion in Salvador [...] "
            "Tia Ciata arrived in Rio de Janeiro in 1876 at the age of 22 and worked as a vendor at a food stall. "
            "She lived on Rua Visconde de Itauna in the neighborhood of Praça Onze (now Cidade Nova), an area which became known as \"Pequena África\" (Little Africa). [...] "
            "Samba musicians, composers, and dancers regularly gathered in her home; her residence may be one of the birthplaces of the genre. "
            "Samba evolved in Ciata's back yard. Here one would find future giants of the genre including Pixinguinha, João da Baiana and Heitor dos Prazeres. [...] "
            "Police persecuted Black musicians and practitioners of Afro-Brazilian religions, despite the individual liberties promised by the 1891 Constitution of Brazil. "
            "Ciata grew smart at evading repression. A true samba party would necessarily require the presence of drums, which have always been negatively associated with the Afro-Brazilian religious cults. "
            "So Ciata would wisely place the samba musicians in the backyards, supposedly the most hidden and safest part of the house. "
            "In the entrance hall, the house's most visible and audible space, brass and string instrumentalists would be playing ‘choro’ music – considered more erudite, and hardly linked to anything close to ‘Black magic’. "
            "When the police came, Ciata would say she was hosting a choro gathering and things would normally be fine for the rest of the night. [...] "
            "When President Venceslau Brás (1914-1918) sought a cure for a long-term leg infection that no doctor could treat, an adviser recommended Ciata's herbal treatments.",
            nome="Tia Ciata")],
    },
    # 10 Pelo Telefone: "música é como passarinho"
    {
        "temas_secundarios": ["musica_brasileira", "historia_musica"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "\"Pelo Telefone\", tido como o primeiro samba gravado, nasceu numa roda, em criação coletiva, mas foi registrado em 1916 só por Donga. A justificativa: música é como passarinho, é de quem pegar primeiro.",
        "explicacao": (
            "Segundo os registros da Biblioteca Nacional, Pelo Telefone é considerado o primeiro samba gravado no "
            "Brasil, embora existam gravações anteriores, como \"Samba - Em Casa da Bahiana\", de 1913, e \"Urubu "
            "Malandro\", de 1914. A música foi composta em 1916 no quintal de Tia Ciata, na Praça Onze, com o "
            "título original de \"Roceiro\", numa criação coletiva que teve a participação de João da Baiana, "
            "Pixinguinha, Caninha, Hilário Jovino Ferreira, Sinhô e outros. Donga foi o primeiro a registrá-la, em "
            "27 de novembro de 1916, só em seu nome, e se justificou com uma máxima atribuída a Sinhô: \"música é "
            "como passarinho, é de quem pegar primeiro\". Depois incluiu como parceiro o jornalista Mauro de "
            "Almeida, autor da letra. Como o sucesso foi enorme, vários músicos reivindicaram a autoria. Em "
            "fevereiro de 1917, um grêmio anunciou no Jornal do Brasil o \"verdadeiro\" Pelo Telefone, de outros "
            "compositores, entre eles a própria Tia Ciata. A letra também tem história: segundo Donga, o trecho "
            "sobre o chefe da polícia era uma paródia criada por jornalistas do jornal A Noite. Em 1913, repórteres "
            "tinham posto uma roleta no Largo da Carioca para mostrar como a polícia tolerava o jogo."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Pelo_Telefone",
            "Pelo Telefone (English: On the Telephone) is a song attributed to the Brazilian guitarist and composer Donga and considered to be the first samba song to be recorded in Brazil, according to records at the National Library of Brazil, although earlier recordings exist, such as \"Samba - Em Casa da Bahiana\" (1913) and \"Urubu Malandro\" (1914). "
            "A collective creation of controversial authorship, the composition is attributed to Ernesto dos Santos, better known as Donga, and to the journalist Mauro de Almeida. "
            "It was registered on the 27th of November, 1916 as being authored only by Donga — who later included de Almeida as a partner [...] "
            "Because it was a huge success and because it was born in a samba circle from improvisations and joint creations, various musicians have claimed authorship. [...] "
            "The song was composed in 1916, in the backyard of Tia Ciata, in Praça Onze (now Cidade Nova). "
            "The song was originally titled \"Roceiro\" and was a collaborative creation, with participation from João da Baiana, Pixinguinha, Caninha, Hilário Jovino Ferreira and Sinhô, and others. "
            "Donga was the first to register the song, which he justified with a maxim attributed to Sinhô: \"music is like a bird, it belongs to whoever catches it first\". [...] "
            "According to a statement by Donga to Brazil's Museum of Image and Sound, \"The chief of police... was a parody created by the journalists of A Noite. "
            "In 1913, newspaper reporters had placed a roulette wheel in Largo da Carioca to demonstrate the police's tolerance of gambling. [...] "
            "Donga claimed that the music was different, but conceded that he was not the author of the lyrics, which were written by Mauro de Almeida. [...] "
            "The Jornal do Brasil newspaper, on February 4, 1917, published a note from Grêmio Fala Gente announcing that \"the true tango 'Pelo Telephone', by composers João da Mata, Germano, Tia Ciata and Hilário, will be sung on Avenida Rio Branco",
            nome="Pelo Telefone")],
    },
    # 11 a cupópia do Cafundó
    {
        "temas_secundarios": ["linguas_mundo", "historia_portugues"],
        "tipos_espanto": ["conexao_inesperada", "misterio_aberto"],
        "gancho": "Numa comunidade quilombola de Salto de Pirapora, a 150 km da capital paulista, descendentes de africanos falam em casa a cupópia, uma \"língua secreta\" com vocabulário banto e base no português caipira.",
        "explicacao": (
            "O Cafundó, cujo nome quer dizer \"lugar remoto\" ou \"de difícil acesso\", é um quilombo que hoje fica "
            "num subúrbio de Salto de Pirapora, no interior de São Paulo. Seus moradores, em sua maioria de "
            "ascendência africana, falam português, mas usam em casa uma língua \"secreta\", chamada cafundó ou "
            "cupópia. No começo, pensava-se que fosse uma língua africana. Um estudo de Carlos Vogt e Peter Fry, "
            "publicado em 1996, mostrou que a gramática e a morfologia são as do português rural do interior do "
            "Sudeste, o caipira, enquanto o vocabulário vem em grande parte de uma ou mais línguas bantas. Por "
            "isso, ela não seria uma língua crioula, como às vezes se diz. A questão ainda rende debate: um estudo "
            "de 2017, de Laura Álvarez López e Anna Jon-And, sugere que, quando os falantes passam do português "
            "para a cupópia, os trechos têm traços gramaticais próprios, e não são apenas português regional "
            "salpicado de palavras africanas. Ou seja, a variedade teria uma gramática particular. A comunidade de "
            "falantes é minúscula: em 1978, eram 40 pessoas, que vivem numa área rural a 150 km da cidade de São "
            "Paulo."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Cafundó_language",
            "Cafundó (Portuguese pronunciation: [kafũˈdɔ]), or Cupópia ([kuˈpɔpjɐ]), is an argot (\"secret language\") spoken in the Brazilian village of Cafundó, São Paulo, now a suburb of Salto de Pirapora. "
            "The language is structurally similar to Portuguese, with many Bantu words in its lexicon. "
            "Cafundó was at first thought to be an African language, but a later study (1996) by Carlos Vogt and Peter Fry showed that its grammatical and morphological structure are those of Brazilian Portuguese, specifically the rural hinterland Southeastern variety, caipira, whereas its lexicon is heavily drawn from some Bantu language(s). "
            "It is therefore not a creole language, as it is sometimes considered. "
            "In contrast to Vogt and Fry (1996), Álvarez López and Jon-And (2017) suggests that when speakers code-switch from Cafundó Portuguese to Cupópia, they produce something different from a contemporary regional variety of Portuguese with a number of African-derived words. "
            "Rather, the passages in which Cupópia is used comprise specific grammatical features, suggesting that the variety has its own grammar. [...] "
            "The name cafundó means \"a remote place\" or \"a hard-to-reach place\", referring to the quilombo of Cafundó. [...] "
            "The speaker community is very small (40 people in 1978). They live in a rural area, 150 km from the city of São Paulo, and are mostly of African descent. "
            "They also speak Portuguese, and use cafundó as a \"secret\" home language.",
            nome="Cafundó language")],
    },
    # 12 acarajé, àkàrà e alforria
    {
        "temas_secundarios": ["comida_brasileira", "africa_antiga", "religioes"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O acarajé baiano tem um parente vivo na Nigéria, no Benim e no Togo: o àkàrà dos iorubás. Na Bahia, o dinheiro das vendedoras de acarajé chegou a comprar a liberdade de familiares escravizados.",
        "explicacao": (
            "O acarajé é um bolinho de feijão-fradinho moído, temperado com sal, pimenta e cebola, frito no dendê "
            "diante do freguês e recheado com vatapá e caruru. Ele descende do àkàrà, criado na terra dos iorubás, "
            "povo que vive em partes da Nigéria, do Benim e do Togo, e chegou ao Brasil com iorubás escravizados. "
            "Por lá, o àkàrà ainda é feito de várias formas, em bolinhas fritas em óleo vegetal ou de dendê. Na "
            "Bahia, as baianas de acarajé, reconhecíveis pelo vestido de algodão todo branco e pelo pano na cabeça, "
            "começaram a vender o bolinho no século XIX. O que ganhavam servia para completar a renda e, em alguns "
            "casos, para comprar a alforria de parentes, até a abolição de 1888. O acarajé é também comida ritual "
            "no candomblé: o primeiro é oferecido ao orixá Exu, os grandes e redondos vão para Xangô e os menores, "
            "para Iansã. Até a versão cozida no vapor, o abará, tem um parente na culinária africana, o moi moi. "
            "Hoje, Salvador tem mais de 500 vendedoras, e o IPHAN reconheceu o acarajé, junto com o papel das "
            "baianas no preparo e na venda, como patrimônio imaterial do Brasil."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Acarajé",
                "This dish is descended from Akara which originated in Yorubaland, from the Yoruba ethnic group inhabiting parts of Nigeria, Benin and Togo. "
                "The dish was then brought to Brazil by enslaved Yoruba citizens from West Africa. [...] "
                "Brazilian acarajé is made from raw and milled cowpeas that are seasoned with salt, pepper and chopped onions molded into the shape of a large scone and deep-fried in dendê with a wok-like pan in front of the customers. "
                "It is served split in half and stuffed with vatapá and caruru [...] "
                "Acarajé can also comes in a second form called abará, in which the ingredients are steamed instead of deep-fried, similar to moi moi. [...] "
                "Today in Bahia, Brazil, most street vendors who serve acarajé are women, known as Baianas do Acarajé, easily recognizable by their all-white cotton dresses and headscarves and caps. "
                "They first appeared in Bahia selling acarajé in the 19th century. "
                "Historically, earnings from the sale of acarajé were used for a variety of reasons including to supplement income and in some cases to buy the freedom of enslaved family members until the abolition of slavery in Brazil in 1888. "
                "The city now has more than 500 acarajé vendors. [...] "
                "Acarajé was listed as a national intangible historic heritage (patrimônio nacional imaterial), by the National Institute of Historic and Artistic Heritage in 2004; the role of baianas in the preparation and sale of acarajé was recognized in the same act. [...] "
                "The first acarajé in a Candomblé ritual is offered to the orixá Exu. "
                "They vary in size based on their offering to a specific deity: large, round acarajé are offered to Xangô; ones smaller in form are offered to Iansã.",
                nome="Acarajé"),
            wiki("Akara",
                "Akara (Yoruba: àkàrà; ) is a type of fritter made from cowpeas or beans (black-eyed peas) that originated in Yorubaland [...] "
                "Akara is the ancestor of Acarajé, traditionally found in Brazil's northeastern state of Bahia, especially in the city of Salvador. "
                "The dish was brought to Brazil by enslaved Yoruba citizens from West Africa, and can still be found in various forms in Nigeria, Benin and Togo. [...] "
                "then beaten to aerate them, and deep-fried in small balls. [...] "
                "Akara is usually fried in vegetable oil (Ororo) or in palm oil (Epo).",
                nome="Akara"),
        ],
    },
    # 13 Casa Branca: o posto de gasolina e o tombamento
    {
        "temas_secundarios": ["religioes", "arquitetura"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Em 1986, um terreiro de Salvador virou o primeiro templo afro-brasileiro tombado pelo IPHAN. A mobilização começou quando parte do terreno, arrendado havia um século, foi vendida e virou posto de gasolina.",
        "explicacao": (
            "O Ilê Axé Iyá Nassô Oká, conhecido como Casa Branca do Engenho Velho, é considerado por muitos o "
            "terreiro de candomblé mais antigo do Brasil. Segundo a tradição oral, nasceu de uma comunidade que "
            "teria sido fundada por três africanas libertas perto da igreja da Barroquinha. Por volta de 1830, uma "
            "delas, Iyá Nassô, saiu para formar o próprio templo. Depois da grande revolta de escravizados de 1835, "
            "da qual seus filhos foram acusados de participar, ela voltou para a África com a família. Em 1839, "
            "Marcelina, uma das mulheres que a acompanharam, retornou à Bahia e liderou a comunidade até morrer, em "
            "1885. Em toda a sua história, o terreiro foi chefiado por mulheres. No início dos anos 1980, a "
            "especulação imobiliária ameaçou sua existência: parte da área que o templo arrendava havia um século "
            "foi vendida, e ali se construiu um posto de gasolina. A comunidade reagiu, com apoio de Mãe Menininha "
            "do Gantois, Jorge Amado, Carybé, Dorival Caymmi, Pierre Verger e Oscar Niemeyer. Em 1982, a prefeitura "
            "de Salvador o declarou patrimônio histórico, e em agosto de 1986 veio o tombamento federal de todo o "
            "terreno, de cerca de 6.800 m², com construções, árvores e objetos sagrados. Foi a primeira vez que o "
            "governo brasileiro reconheceu o valor histórico de um templo de candomblé. Com isso, o terreiro "
            "recuperou a área do posto, e a praça de Oxum ganhou um projeto de Niemeyer."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Casa_Branca_do_Engenho_Velho",
            "Ilê Axé Iyá Nassô Oká is a historic Candomblé temple (or terreiro, in Portuguese) in the city of Salvador, Bahia, in northeastern Brazil. "
            "It is also known as the Casa Branca do Engenho Velho, or simply the Casa Branca. [...] "
            "Considered by many to be the oldest terreiro in Brazil, Ilê Axé Iyá Nassô Oká was the first Afro-Brazilian temple to receive heritage status from the National Institute of Historic and Artistic Heritage (IPHAN). [...] "
            "According to oral tradition, Ilê Axé Iyá Nassô Oká emerged from an earlier religious community that was located in the vicinity of the Barroquinha church, said to have been founded by three African freedwomen: Iyá Nassô, Iyá Akalá and Iyá Detá. "
            "At some point, probably around 1830, Iyá Nassô withdrew to form her own temple. [...] "
            "A few years later, following a major slave uprising in 1835, in which her sons were accused of participating, Iyá Nassô along with her family and other members of her household, including several former captives, returned to Africa. "
            "Iyá Nassô remained there, but in 1839, one of the women who had accompanied her, Marcelina, went back to Bahia, where she assumed leadership of the religious community, a position she held until her death in 1885. [...] "
            "Throughout its history, Ilê Axé Iyá Nassô Oká has been led by women. [...] "
            "In the early 1980s, urban expansion led to real estate speculation, threatening the very existence of Ilê Axé Iyá Nassô Oká. "
            "Part of the property that the temple had been leasing for a century was sold and a gas station was built on the land. [...] "
            "Many public personalities, including the high priestess of the Gantois temple, Mãe Menininha, novelist Jorge Amado, artist Carybé, musician Dorival Caymmi, ethnologist and photographer Pierre Verger, and architect Oscar Niemeyer, lent their voices to advocating for the temple's preservation. "
            "As a result, in 1982 the city of Salvador took what was then an unprecedented step, conceding historic landmark status to the temple. "
            "This was followed in August 1986 by another, even greater precedent: historic heritage status from the National Institute of Historic and Artistic Heritage (IPHAN), which included not only the building where public ceremonies are held but \"the entire site, an area of approximately 6,800 m2, with the buildings, trees and main sacred objects [...] "
            "This permitted the temple to regain control over the land where the gas station had been constructed and gave rise to the renovation project designed by Niemeyer [...] "
            "The community's designation as a national historic monument marked the first time that the historical and cultural value of a Candomblé temple had been recognized by the Brazilian government.",
            nome="Casa Branca do Engenho Velho")],
    },
    # 14 a origem do 20 de novembro
    {
        "temas_secundarios": ["brasil_republica", "personagens_esquecidos"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O Dia da Consciência Negra nasceu em 1971, em Porto Alegre, como alternativa ao 13 de maio. Era a ditadura, e as autoridades teriam confundido o Grupo Palmares, que propôs a data, com uma organização armada.",
        "explicacao": (
            "A proposta foi do poeta Oliveira Silveira, dentro do Grupo Palmares, uma associação de ativistas e "
            "pesquisadores da cultura negra de Porto Alegre. Ele fez uma analogia com Tiradentes, lembrado no dia "
            "de sua morte: celebrar a morte de Zumbi, o líder do Quilombo dos Palmares, poria o protagonismo negro "
            "no centro da memória nacional. A data foi tirada de uma revista da Editora Abril, que dava 20 de "
            "novembro como o dia da morte de Zumbi, em 1695. O país vivia a ditadura militar, três anos depois do "
            "AI-5. Quando um jornal anunciou a homenagem de 20 de novembro de 1971, as autoridades teriam confundido "
            "o Grupo Palmares com a VAR-Palmares, uma organização armada. O grupo foi chamado à Polícia Federal e "
            "teve de entregar o programa completo para aprovação da censura. Dois anos depois da primeira "
            "celebração, o desafio do grupo ao tradicional 13 de maio, dia da Lei Áurea, chegou ao noticiário "
            "nacional, e eventos em novembro se espalharam pelo país. Em 1978, o Movimento Negro Unificado incluiu "
            "a data num manifesto. Ela entrou no calendário escolar em 2003, virou data comemorativa nacional em "
            "2011 e se tornou feriado nacional pela Lei 14.759, de 21 de dezembro de 2023."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Black_Awareness_Day",
            "Conceived in 1971 by poet and activist Oliveira Silveira and the Porto Alegre–based Grupo Palmares, the date was incorporated into the national school calendar in 2003, recognized as a national commemorative date in 2011, and established as a national public holiday on 21 December 2023. [...] "
            "The date was chosen to honor the death of Zumbi of the Quilombo dos Palmares (1695) [...] "
            "In 1971, in Porto Alegre, Oliveira Silveira proposed the date within the Grupo Palmares, an association of activists and researchers of Black Brazilian culture. "
            "Drawing an analogy with the remembrance of Tiradentes on the date of his death, Silveira argued for commemorating Zumbi's death to center Black agency in national memory. "
            "A magazine by Editora Abril listed 20 November as the date of Zumbi's death, which inspired the group's choice [...] "
            "Two years after the first celebration, the group's challenge to the traditional 13 May date reached national news, and events honoring overlooked Black historical figures began to spread across the country every November. "
            "In 1978, the Unified Black Movement (Movimento Negro Unificado) included Black Consciousness Day in a manifesto [...] "
            "The proposal arose during the military dictatorship, three years after AI-5. "
            "When a newspaper announced the 20 November 1971 commemoration under the headline \"Zumbi – The homage of the theater's Black people,\" authorities reportedly confused \"Grupo Palmares\" with the armed organization VAR-Palmares. "
            "The group was summoned by the Federal Police and required to submit the full program to obtain approval by censors. [...] "
            "it was enacted as Law No. 14,759 on 21 December 2023.",
            nome="Black Awareness Day")],
    },
]
