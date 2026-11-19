LOTE = "2026-11-18-brasil_colonial-01"
AREA = "brasil"
TEMA = "brasil_colonial"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 "brasileiro" era nome de profissão
    {
        "temas_secundarios": ["palavras_portugues", "historia_portugues"],
        "tipos_espanto": ["origem_inesperada"],
        "gancho": "\"Brasileiro\" começou como nome de profissão, como \"pedreiro\": segundo estudiosos, era o comerciante de pau-brasil. Pela regra dos gentílicos, o certo seria \"brasiliano\" ou \"brasiliense\".",
        "explicacao": (
            "Em português, a terminação \"-eiro\" costuma indicar um ofício: verdureiro, pedreiro, engenheiro. Os "
            "nomes de quem nasce num lugar costumam seguir outras regras, como em \"paulista\", \"italiano\" ou "
            "\"canadense\". Por essa lógica, quem nasce no Brasil deveria se chamar brasiliano ou brasiliense. O "
            "\"brasileiro\" tem outra origem. Nos primeiros tempos da colonização, segundo estudiosos, a palavra "
            "designava os comerciantes de pau-brasil, a madeira que dava tinta vermelha e era o grande negócio da "
            "nova terra. Esses comerciantes eram, em geral, portugueses, porque a população local era sobretudo "
            "indígena. Por um tempo, os nomes conviveram com sentidos diferentes: \"brasileiro\" era o português "
            "ou estrangeiro estabelecido no Brasil, \"brasiliense\" era quem tinha nascido aqui. Muito antes da "
            "Independência, porém, \"brasileiro\" já tinha virado o nome comum de quem vivia na colônia, e assim "
            "ficou. A própria palavra \"Brasil\" vem da madeira: a terra ficou conhecida como Terra do Brasil, a "
            "terra do pau-brasil."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Brasileiros",
                "No período que se seguiu à descoberta do território brasileiro pelos europeus, a designação \"brasileiro\" foi dada aos comerciantes portugueses de pau-brasil, referindo-se exclusivamente àquela atividade, visto que os habitantes da terra eram, na sua maioria, índios [...] "
                "desde muito antes da Independência e fundação do Império do Brasil, em 1822, tanto no Brasil como em Portugal, já era comum se atribuir o gentílico \"brasileiro\" a uma pessoa [...] "
                "Seguindo as regras gramaticais para formação de gentílicos, o correto seria brasilianos ou brasilienses. "
                "Brasileiro alude a um ofício ou a uma profissão (tal qual \"verdureiro\", \"engenheiro\", \"pedreiro\") e, nas raízes históricas, estudiosos têm escrito que se referia ao comerciante, geralmente português, do pau-brasil, na época do Brasil Colônia [...] "
                "Durante os primórdios da construção do país, tornou-se comum designar brasileiro o português ou o estrangeiro estabelecido no Brasil, brasiliense o natural do Brasil",
                nome="Brasileiros", idioma="pt"),
            wiki("Paubrasilia",
                "Such a vigorous trade resulted from the woods that early sailors and merchants started referring to the land itself as Terra do Brasil, or simply, the \"Land of Brazil\"; from this use, the present name of Brazil was derived."),
        ],
    },
    # 2 pau-brasil e os arcos de violino
    {
        "temas_secundarios": ["historia_musica", "pigmentos", "biomas_brasileiros"],
        "tipos_espanto": ["conexao_inesperada"],
        "gancho": "A árvore que deu nome ao Brasil é a madeira mais usada nos melhores arcos de violino e violoncelo. Depois de séculos de exploração, o pau-brasil está ameaçado de extinção.",
        "explicacao": (
            "Quando os portugueses encontraram o pau-brasil no litoral, reconheceram nele um parente de uma árvore "
            "asiática que a Europa já usava para tingir tecidos de vermelho. A madeira americana logo dominou o "
            "comércio como fonte melhor de corante, e o negócio foi tão intenso que a terra passou a ser chamada "
            "de Terra do Brasil. A exploração excessiva derrubou o número de árvores no século XVIII, e o comércio "
            "entrou em colapso. Mas o pau-brasil, também chamado pau de pernambuco, tinha outra qualidade: o cerne "
            "denso, vermelho-alaranjado e capaz de ganhar muito brilho. Ele se tornou a madeira mais valorizada "
            "para arcos de instrumentos de corda. Hoje a espécie quase desapareceu da maior parte de sua área "
            "original, na Mata Atlântica, e está na lista de espécies ameaçadas. Em 2024, a convenção "
            "internacional que controla o comércio de espécies ameaçadas, a CITES, decidiu que os estoques da "
            "madeira devem ser registrados. Os próprios fabricantes de arcos criaram uma iniciativa para replantar "
            "as árvores, e a escassez ajudou a crescer a indústria de arcos de fibra de carbono."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Paubrasilia",
            "This plant has a dense, orange-red heartwood that takes a high shine, and it is the premier wood used for making bows for stringed instruments. [...] "
            "or pau de pernambuco, named after the Brazilian state of Pernambuco. [...] "
            "When Portuguese explorers found Paubrasilia on the coast of South America, they recognised it as a relative of an Asian species of sappanwood already used in Europe for producing red dye. [...] "
            "The South American trees soon dominated trading as a better source of dye. "
            "Such a vigorous trade resulted from the woods that early sailors and merchants started referring to the land itself as Terra do Brasil [...] "
            "Excessive harvesting led to a steep decrease in the number of brazilwood trees in the 18th century, causing the collapse of this economic activity. "
            "Presently, the species is nearly extirpated in most of its original range. "
            "Brazilwood is listed as an endangered species by the IUCN [...] "
            "At the 2024 annual meeting of the Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES) it was resolved that existing stockpiles of the wood should be registered [...] "
            "The International Pernambuco Conservation Initiative (IPCI), whose members are the bowmakers who rely on pernambuco for their livelihoods, is working to replant the trees. [...] "
            "The shortage of pernambuco has also helped the carbon fiber and composite bow industry to thrive.",
            nome="Paubrasilia")],
    },
    # 3 a língua geral paulista
    {
        "temas_secundarios": ["povos_indigenas", "historia_portugues", "linguas_mundo"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Nos primeiros séculos da colônia, em São Paulo se falava mais uma língua de base tupi do que o português. Muitas crianças paulistas só aprendiam português na vida adulta.",
        "explicacao": (
            "A capitania de São Vicente foi fundada em 1532, e os primeiros colonos eram só homens, muitos deles "
            "degredados e náufragos. O primeiro casal português só desembarcou cinco anos depois. Na região, o que "
            "predominou nas primeiras décadas foi a união entre homens brancos e mulheres tupis, e os filhos "
            "cresciam falando a língua das mães. Com o tempo, esse tupi foi mudando e virou a chamada língua geral "
            "paulista, falada por boa parte da população nos séculos XVII e XVIII. As bandeiras reforçaram o "
            "quadro: os homens passavam meses fora, em busca de ouro e de indígenas para escravizar, e as crianças "
            "ficavam com as mães, falantes de tupi, só tendo contato com o português no início da vida adulta. Nas "
            "próprias bandeiras, a língua geral predominava quase totalmente, e foi levada a áreas dos atuais "
            "Minas Gerais, Goiás, Mato Grosso e Paraná. Em 1757, o Diretório dos Índios, do Marquês de Pombal, "
            "proibiu as línguas gerais, com punições severas para quem as usasse, e impôs o português."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("L%C3%ADngua_geral_paulista",
                "Martim Afonso de Sousa, em 22 de janeiro de 1532. [...] "
                "Somente cinco anos após a fundação da capitania, desembarcou, em São Vicente, o primeiro casal português. [...] "
                "O que predominou, na região, nas primeiras décadas da colonização, foi a união entre homens brancos e mulheres tupis. [...] "
                "Os homens e os filhos saíam em longas expedições de preamento e pesquisas auríferas, deixando os filhos pequenos aos cuidados das mães que, em sua maioria, eram falantes da língua tupi. "
                "Nesse contexto, as crianças paulistas, em seus primeiros anos de vida, eram expostas exclusivamente à língua tupi, tendo contato com a língua portuguesa apenas no início de sua vida adulta. "
                "O predomínio da língua geral paulista nas bandeiras era quase total [...] "
                "Em 1757, é publicado o Diretório dos Índios, por Sebastião José de Carvalho e Melo, Marquês de Pombal, levando a proibição da língua paulista e de outras línguas gerais",
                nome="Língua geral paulista", idioma="pt"),
            wiki("L%C3%ADngua_Geral_Paulista",
                "the Tupi language prevailed among the Paulista population in the first centuries of Portuguese colonisation. [...] "
                "In the 17th and 18th centuries, this language, already widespread among the Paulista population, became known as the \"Paulista general language\". [...] "
                "The Paulista General Language was spoken and taken by the bandeirantes from São Paulo to places corresponding to the present states of Minas Gerais, Goiás, Mato Grosso, Mato Grosso do Sul and Paraná.",
                nome="Língua Geral Paulista"),
        ],
    },
    # 4 a sinagoga do Recife e Nova York
    {
        "temas_secundarios": ["religioes", "cidades", "imperios_coloniais"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "A primeira sinagoga das Américas foi erguida no Recife, em 1636. Quando os holandeses perderam o Brasil, refugiados de lá fundaram em Nova Amsterdã, a futura Nova York, a congregação judaica mais antiga dos EUA.",
        "explicacao": (
            "Em meados do século XVII, os holandeses controlaram por um tempo parte do Nordeste brasileiro. Judeus sefarditas de "
            "origem portuguesa e espanhola, que fugiam da conversão forçada, encontraram refúgio no Recife "
            "holandês. Em 1636 fundaram a sinagoga Kahal Zur Israel, a primeira das Américas, numa rua que ficou "
            "conhecida como Rua dos Judeus. Um dos que ajudaram a criá-la foi Moses Cohen Henriques, que tinha "
            "atuado como corsário a serviço dos holandeses e talvez como pirata. No auge, a comunidade tinha cerca "
            "de 1.450 judeus e um rabino vindo da Europa. Em 1654, os holandeses se renderam aos portugueses, mas "
            "só depois de garantir aos judeus a saída segura da colônia, e a maioria foi embora. Em setembro "
            "daquele ano, 23 desses refugiados chegaram a Nova Amsterdã, colônia holandesa na América do Norte. O "
            "governador Peter Stuyvesant tentou barrá-los, mas eles conseguiram permissão para ficar. Ali nasceu a "
            "congregação Shearith Israel, a mais antiga dos Estados Unidos. O prédio do Recife foi demolido no "
            "início do século XX, e hoje funciona no local um museu judaico."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Kahal_Zur_Israel_Synagogue",
                "The synagogue was established in 1636 by Portuguese and Spanish Sephardic Jews who had taken refuge in Dutch Brazil, fleeing forced conversion [...] "
                "It was the first synagogue erected in the Americas. "
                "The building was destroyed in the early part of the 20th century and a new building constructed on the same site, that now serves as a Jewish museum. [...] "
                "After his retirement circa 1636 from privateering for the Dutch and perhaps pirating, Cohen Henriques assisted his brother, Abraham Cohen, in establishing the Kahal Zur Israel synagogue. [...] "
                "It flourished in the mid-17th century when the Dutch briefly controlled this part of northeastern Brazil. "
                "The synagogue then served a community of approximately 1,450 Jews. [...] "
                "In 1654, the Dutch surrendered to the Portuguese, only after the Jews were guaranteed safe passage from the colony, evading Portuguese persecution. "
                "Aboab da Fonseca and Cohen Henriques, as well as most of the Jews of the Dutch colony, left.",
                nome="Kahal Zur Israel Synagogue"),
            wiki("Congregation_Shearith_Israel",
                "Established in 1654 in New Amsterdam by Jews who arrived from Dutch Brazil, it is the oldest Jewish congregation in the United States. [...] "
                "The first group of Spanish and Portuguese Jews were twenty-three refugees from Dutch Brazil, who arrived in New Amsterdam in September 1654. "
                "After being initially rebuffed by the Director of New Netherland, Peter Stuyvesant, Jews were given official permission to settle in the colony in 1655.",
                nome="Congregation Shearith Israel"),
        ],
    },
    # 5 os tupinambás, Montaigne e Shakespeare
    {
        "temas_secundarios": ["povos_indigenas", "literatura", "costumes_rituais"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "Relatos sobre os tupinambás do litoral brasileiro inspiraram um famoso ensaio de Montaigne, que muitos veem como influência de Shakespeare. E talvez deram nome a um legume francês, o topinambour.",
        "explicacao": (
            "No século XVI, os tupinambás, que viviam em boa parte do litoral, estavam entre os povos indígenas "
            "mais descritos pelos europeus. Os franceses, que tentaram fundar uma colônia na baía de Guanabara "
            "entre 1555 e 1567, deixaram relatos detalhados, como os de André Thevet e Jean de Léry. Em 1550, "
            "numa festa para o rei Henrique II em Rouen, cerca de cinquenta homens chegaram a encenar uma batalha "
            "entre os tupinambás, aliados dos franceses, e outro povo indígena. Os livros de Thevet e Léry "
            "inspiraram o filósofo Michel de Montaigne a escrever, por volta de 1580, o ensaio \"Dos canibais\". "
            "Nele, Montaigne descreve o costume tupinambá de comer os inimigos mortos como questão de honra e o "
            "compara à barbárie da própria Europa do seu tempo. O ensaio ajudou a formar o mito do \"bom "
            "selvagem\". Traduzido para o inglês em 1603, ele é visto desde 1781 como uma influência sobre A "
            "Tempestade, de Shakespeare. E os tupinambás talvez tenham dado nome ao topinambour, como os franceses "
            "chamam o tupinambo, um tubérculo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Tupinamb%C3%A1_people",
                "The Tupinambás were abundantly described in André Thevet's 1572 Cosmographie universelle [...] in Jean de Léry's Histoire d'un voyage faict en la terre du Brésil [...] "
                "Thevet and Léry were an inspiration for Montaigne's famous essay Of Cannibals, and influenced the creation of the myth of the \"noble savage\" during the Enlightenment. "
                "The Tupinambá may have given their name to the common French word for the Jerusalem artichoke, the topinambour.",
                nome="Tupinambá people"),
            wiki("Of_Cannibals",
                "Of Cannibals (Des Cannibales), written circa 1580, is an essay, one of those in the collection Essays, by Michel de Montaigne, describing the ceremonies of the Tupinambá people in Brazil. "
                "In particular, he reported about how the group ceremoniously ate the bodies of their dead enemies as a matter of honor. "
                "In his work, he uses cultural relativism and compares the cannibalism to the \"barbarianism\" of 16th-century Europe. "
                "An English translation, Of the Caniballes, appeared in John Florio's 1603 translation of the Essais. "
                "This has often been viewed (first by Edward Capell in 1781) as an influence on Shakespeare's The Tempest",
                nome="Of Cannibals"),
            wiki("France_Antarctique",
                "France Antarctique (also spelled France antartique) was a French colony in Rio de Janeiro, in modern-day Brazil, which existed between 1555 and 1567 [...] "
                "In 1550, in the royal entry for Henry II of France, at Rouen, about fifty men depicted naked Indians and a battle between the Tupinamba allies of the French, and the Tabajara Indians.",
                nome="France Antarctique"),
        ],
    },
    # 6 o padre voador
    {
        "temas_secundarios": ["invencoes", "transportes", "ciencia_brasileira"],
        "tipos_espanto": ["historia_humana", "engenhosidade", "mito_desmentido"],
        "gancho": "Em 1709, um padre nascido em Santos fez um pequeno balão de ar quente subir até o teto diante da corte portuguesa. Os irmãos Montgolfier só soltariam o seu balão em 1783.",
        "explicacao": (
            "Bartolomeu de Gusmão nasceu em Santos, então parte da colônia, em 1685, estudou com os jesuítas na "
            "Bahia e foi para Portugal, onde se formou em Coimbra. Em 1709, pediu ao rei D. João V apoio para uma "
            "máquina voadora, a passarola. O projeto era fantasioso: uma vela enorme sobre um casco de barco, "
            "movida por ímãs. O teste público da máquina, marcado para junho, não aconteceu. Mas, em 8 de agosto "
            "de 1709, num salão da Casa da Índia, em Lisboa, Gusmão fez um pequeno balão subir até o teto usando o "
            "calor de uma chama, diante da corte. É uma das primeiras demonstrações conhecidas do princípio do "
            "balão de ar quente. O rei o recompensou com cargos, e ele ficou conhecido como o Voador. Uma história "
            "famosa diz que a Inquisição o perseguiu por causa dos voos e que ele fugiu disfarçado, mas isso "
            "provavelmente foi inventado depois: os documentos mostram uma denúncia à Inquisição por outro "
            "motivo. Ele morreu em Toledo, na Espanha, em 1724."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Bartolomeu_de_Gusm%C3%A3o",
                "Bartolomeu Lourenço de Gusmão (December 1685 – 18 November 1724) was a Portuguese Catholic priest and naturalist born in colonial Brazil, who was a pioneer of lighter-than-air aerostat design [...] "
                "Gusmão was born at Santos, then part of the Portuguese colony of Brazil. "
                "He began his novitiate in the Society of Jesus at Bahia [...] He completed his course of study at the University of Coimbra [...] "
                "In 1709, he presented a petition to King John V of Portugal, seeking royal favour for his invention of an airship [...] "
                "The vessel was to be propelled by the agency of magnets which were to be encased in two hollow metal balls. "
                "The public test of the machine, which was set for 24 June 1709, did not take place. "
                "It is known that Gusmão was working on this principle at the public exhibition he gave before the Court on 8 August 1709, in the hall of the Casa da Índia in Lisbon, when he propelled a small balloon to the roof using combustion from a flame. [...] "
                "One account of Gusmão's work suggests that the Portuguese Inquisition forbade him to continue his aeronautic investigations and persecuted him because of them, but this is probably a later invention. [...] "
                "Contemporary documents do attest that information was laid before the Inquisition against Gusmão, but on quite another charge. "
                "The inventor fled to Spain and fell ill of a fever, of which he died in Toledo.",
                nome="Bartolomeu de Gusmão"),
            wiki("Montgolfier_brothers",
                "On 4 June 1783, they flew the balloon at Annonay in front of a group of dignitaries from the états particuliers.",
                nome="Montgolfier brothers"),
        ],
    },
    # 7 a imprensa proibida
    {
        "temas_secundarios": ["imperios_coloniais", "brasil_imperio"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Até 1808, imprimir livros ou jornais era proibido no Brasil. Na Cidade do México, a primeira oficina de impressão tinha sido aberta em 1539.",
        "explicacao": (
            "Na América espanhola, a imprensa chegou cedo. Em 1539, Juan Pablos abriu na Cidade do México a "
            "primeira oficina de impressão documentada do Novo Mundo, e em 1584 foi autorizada outra em Lima. Uma "
            "estimativa conta mais de 11 mil obras publicadas só na Cidade do México até 1821. Na América "
            "portuguesa, a história foi outra: toda atividade de imprensa era reprimida. Em 1706, uma carta real "
            "mandou confiscar o que um comerciante tinha imprimido no Recife, alguns sermões e letras de câmbio. Em "
            "1747, o tipógrafo António Isidoro da Fonseca abriu uma oficina no Rio de Janeiro, mas ela foi fechada "
            "no mesmo ano por ordem da corte. A ordem mandava despachar para Portugal qualquer equipamento de "
            "impressão das colônias e proibia as autoridades locais de autorizar livros, sob pena de prisão. A "
            "imprensa brasileira só nasceu oficialmente em 13 de maio de 1808, com a Impressão Régia, criada no "
            "Rio por D. João com prensas inglesas trazidas na fuga da família real."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Imprensa_no_Brasil",
                "A história da imprensa no Brasil tem seu início em 1808 com a chegada da família real portuguesa ao Brasil, sendo até então coibida toda e qualquer atividade de imprensa — fosse a publicação de jornais, livros ou panfletos. [...] "
                "Em 1539, Juan Pablos instalava sua oficina nessa cidade, sendo o primeiro impressor documentado no Novo Mundo. [...] "
                "A autorização para se estabelecer uma oficina impressora nessa cidade foi concedida em 1584. "
                "Conforme uma estimativa, do começo dos anos 1500 até 1821, 11 625 obras haviam sido publicadas só na Cidade do México [...] "
                "Durante o governo de Francisco de Castro Morais, um comerciante desconhecido montou uma pequena prensa e imprimiu alguns sermões e letras de câmbio. [...] "
                "Temos notícia da iniciativa graças a uma Carta Real de 8 de junho de 1706 proibindo e confiscando o material impresso. [...] "
                "A imprensa brasileira nasceu oficialmente no Rio de Janeiro em 13 de maio de 1808, com a criação da Impressão Régia, hoje Imprensa Nacional, pelo príncipe-regente Dom João Maria de Bragança. "
                "As máquinas impressoras, inglesas, haviam sido trazidas em meio à fuga da família real de Lisboa",
                nome="Imprensa no Brasil", idioma="pt"),
            wiki("Ant%C3%B4nio_Isidoro_da_Fonseca",
                "António Isidoro da Fonseca foi um tipógrafo português que em 1747 estabeleceu uma tipografia no Brasil, no Rio de Janeiro. "
                "A tipografia foi fechada ainda no mesmo ano por ordem da Corte Portuguesa. [...] "
                "A ordem determinava que quaiquer equipamentos tipográficos nas colônias fossem despachados para Portugal [...] "
                "e proibia autoridades locais de autorizar a impressão de livros sob pena de prisão e deportação.",
                nome="António Isidoro da Fonseca", idioma="pt"),
        ],
    },
    # 8 Raposo Tavares
    {
        "temas_secundarios": ["fronteiras_paises", "amazonia", "povos_indigenas"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "Em 1648, o bandeirante Raposo Tavares saiu de São Paulo com mais de mil homens e percorreu mais de 10 mil km pelos rios do continente, até a foz do Amazonas. Poucos chegaram ao fim.",
        "explicacao": (
            "Os bandeirantes eram expedições que partiam de São Paulo para o interior em busca de ouro, pedras "
            "preciosas e, sobretudo nos primeiros tempos, indígenas para escravizar. Elas ajudaram a levar o "
            "domínio português muito além da linha do Tratado de Tordesilhas. António Raposo Tavares, nascido em "
            "Portugal, já tinha comandado ataques a missões jesuíticas espanholas, com milhares de indígenas "
            "capturados. Em 1648 partiu em sua última bandeira, com 200 brancos e mais de mil indígenas. A "
            "expedição seguiu os rios por mais de 10 mil quilômetros: o Paraguai, o Grande, o Mamoré, o Madeira e, "
            "por fim, o Amazonas, ligando numa só viagem as duas grandes bacias da América do Sul e as encostas "
            "dos Andes. Só Raposo Tavares, 59 brancos e alguns indígenas chegaram a Belém, na foz do Amazonas. "
            "Depois os sobreviventes voltaram a São Paulo, onde ele morreu em 1658."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Ant%C3%B3nio_Raposo_Tavares",
            "was a Portuguese bandeirante who explored mainland eastern South America and claimed it for Portugal, extending the territory of the colony beyond the limits imposed by the Treaty of Tordesillas. "
            "He also led the largest expedition ever made in the Americas, covering over 10,000 kilometres (over 6,200 mi) around South America, unifying completely the two large South American river basins and the Andes in a single voyage. [...] "
            "Tavares was born in São Miguel do Pinheiro, Alentejo, Portugal in 1598. [...] "
            "The bandeirantes first attacked some Guarani villages in the upper Parana valley, which were protected by the Spanish Jesuits and brutally killed many people, capturing 2,500 Indians. [...] "
            "He embarked on his last journey with a bandeira in 1648, searching for gold, precious minerals and slaves in the unexplored mainland. "
            "He was joined by 200 white mercenaries from São Paulo and over a thousand Indians. "
            "The bandeirantes travelled for over 10,000 kilometres (6,200 mi) following the courses of the rivers, most notably the Paraguay River, the Grande River, the Mamoré River, the Madeira River and the Amazon River. "
            "Only Tavares, 59 whites and some Indians reached Belém at the mouth of the Amazon River. "
            "After that, the survivors returned to São Paulo, where Raposo Tavares died in 1658.",
            nome="António Raposo Tavares")],
    },
    # 9 diamantes
    {
        "temas_secundarios": ["minerais_rochas", "imperios_coloniais", "dinheiro"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Por mais de 2 mil anos, os diamantes do mundo vieram da Índia. Os primeiros achados fora de lá foram em Minas Gerais, no século XVIII, e a Coroa portuguesa cercou a região.",
        "explicacao": (
            "Durante muito tempo, só se encontravam diamantes em depósitos de rio no sul da Índia. O país liderou "
            "a produção mundial desde cerca do século IX antes de Cristo até meados do século XVIII. Então as "
            "minas indianas se esgotaram, e o Brasil tomou o lugar delas: foi aqui que se acharam os primeiros "
            "diamantes de fora da Índia. Os achados foram em torno do Arraial do Tejuco, a atual Diamantina, em "
            "Minas Gerais, e só foram comunicados oficialmente à Coroa em 1729, pelo governador da capitania. "
            "Portugal reagiu impondo controle total sobre a região. Em 1734 criou a Intendência dos Diamantes, um "
            "regime extremamente controlador e autoritário, e o monopólio da Coroa sobre as jazidas durou até "
            "1845. No século XVIII, a região de Diamantina foi a maior produtora de diamantes do mundo ocidental."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Diamond",
                "Historically, diamonds were found only in alluvial deposits in Guntur and Krishna district of the Krishna River delta in Southern India. "
                "India led the world in diamond production from the time of their discovery in approximately the 9th century BC to the mid-18th century AD, but the commercial potential of these sources had been exhausted by the late 18th century and at that time India was eclipsed by Brazil where the first non-Indian diamonds were found in 1725."),
            wiki("Diamantina,_Minas_Gerais",
                "Diamantina was founded as Arraial do Tejuco in 1713 [...] "
                "Diamantina represented the largest mining of diamonds in the western world in the 18th century, and for nine years, the Portuguese Crown was not aware of the discovery of diamonds in the region, which was done by the governor of the Captaincy, in 1729, the then D. Lourenço de Almeida. "
                "Portugal's response was to impose full control over the diamond regions of Minas Gerais. "
                "In 1734, the Intendency of Diamonds was created, whose regime was totally controlling and authoritarian. "
                "The Portuguese Crown's monopoly over diamond deposits lasted until 1845.",
                nome="Diamantina, Minas Gerais"),
        ],
    },
    # 10 o café no buquê
    {
        "temas_secundarios": ["cafe_cha_cacau", "domesticacao", "amazonia"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O Brasil, maior produtor de café do mundo, plantou o primeiro pé em 1727. Segundo a lenda, as sementes vieram escondidas num buquê dado pela esposa do governador da Guiana Francesa.",
        "explicacao": (
            "O café não é nativo das Américas. No começo do século XVIII, os portugueses queriam entrar nesse "
            "mercado, mas não conseguiam sementes: na vizinha Guiana Francesa, o governador não deixava exportá-las. "
            "O oficial Francisco de Melo Palheta foi mandado para lá numa missão diplomática, para resolver uma "
            "disputa de fronteira. Segundo a lenda, na volta ele trouxe as sementes escondidas porque seduziu a "
            "esposa do governador, que lhe deu em segredo um buquê com sementes no meio. O que se sabe é que "
            "Palheta plantou o primeiro pé de café do Brasil no Pará, em 1727. A planta chegou ao Rio de Janeiro em "
            "1770, mas por décadas só abasteceu o consumo local. Depois o café se espalhou pelo Sudeste, e nos anos "
            "1840 o Brasil já era o maior produtor do mundo. Hoje o país produz cerca de um terço do café do "
            "planeta."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Coffee_production_in_Brazil",
            "Brazil produces about a third of the world's coffee, making the country by far the world's largest producer. [...] "
            "Coffee was not native to the Americas but was imported to the country. "
            "The first crop arrived in Brazil in the 18th century making it the dominant producer by the 1840s. "
            "The first coffee bush in Brazil was planted by Francisco de Melo Palheta in Pará in 1727. "
            "According to legend, the Portuguese were looking for a cut of the coffee market, but could not obtain seeds from bordering French Guiana due to the governor's unwillingness to export the seeds. "
            "Palheta was sent to French Guiana on a diplomatic mission to resolve a border dispute. "
            "On his way back home, he managed to smuggle the seeds into Brazil by seducing the governor's wife who secretly gave him a bouquet spiked with seeds. "
            "Coffee spread from Pará and reached Rio de Janeiro in 1770, but was only produced for domestic consumption until the early 19th century",
            nome="Coffee production in Brazil")],
    },
    # 11 a colônia que virou sede do império
    {
        "temas_secundarios": ["brasil_imperio", "imperios_coloniais", "revolucoes_politicas"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "De 1808 a 1821, a sede do império português não ficava em Lisboa, mas no Rio de Janeiro: a colônia passou a governar a metrópole, o que historiadores chamam de inversão metropolitana.",
        "explicacao": (
            "No fim de 1807, com as tropas de Napoleão invadindo Portugal, a rainha D. Maria I, o príncipe regente "
            "D. João, a família real, a corte e altos funcionários, cerca de 10 mil pessoas, embarcaram para o "
            "Brasil, escoltados por navios britânicos. Partiram poucos dias antes de as forças francesas chegarem a "
            "Lisboa. O Brasil era então uma colônia pouco povoada, com pouco mais de 3 milhões de habitantes, mais "
            "de 1 milhão deles escravizados. Instalada no Rio, a corte transformou a cidade na sede do governo de "
            "todo o império. D. João abriu imediatamente os portos brasileiros aos navios estrangeiros, e o Rio "
            "teve de se adaptar às pressas para receber cerca de 15 mil pessoas, numa cidade sem saneamento básico "
            "nem esgoto. Alguns historiadores chamam esse período de inversão metropolitana: uma colônia "
            "governando um império inteiro. A corte só voltou a Lisboa em 1821, depois da Revolução Liberal do "
            "Porto, e a mudança é vista como o primeiro passo da independência do Brasil."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Transfer_of_the_Portuguese_court_to_Brazil",
            "The Portuguese royal court transferred from Lisbon to the Portuguese colony of Brazil in a strategic retreat of Queen Maria I, Prince Regent John (the future King John VI), the Braganza royal family, its court, and senior officials, totaling nearly 10,000 people, on 27 November 1807. [...] "
            "The Braganza royal family departed for Brazil just days before Napoleonic forces invaded Portugal on 1 December 1807. "
            "The Portuguese crown remained in Brazil from 1808 until the Liberal Revolution of 1820 led to the return of John VI of Portugal on 26 April 1821. "
            "For thirteen years, Rio de Janeiro functioned as the capital of the United Kingdom of Portugal, Brazil and the Algarves in what some historians call a metropolitan reversal (i.e., a colony exercising governance over the entirety of an empire). [...] "
            "represented the first step toward Brazilian independence, since the prince regent immediately opened the ports of Brazil to foreign shipping and turned the colonial capital into the seat of government. [...] "
            "Commodore Graham Moore continued escorting the Portuguese court to Brazil with the British ships of the line Marlborough, London, Bedford, and Monarch. "
            "In 1807, Brazil was a sparsely populated colony, with a little over three million inhabitants. "
            "Over a million of Brazil's inhabitants were slaves [...] "
            "Beyond having to go through infrastructural expansion to accommodate for the arrival of 15,000 people, Rio continued to be modified and upgraded in the early stages of the transferring of the court. "
            "The city lacked basic sanitation and structured sewer systems.",
            nome="Transfer of the Portuguese court to Brazil")],
    },
    # 12 Palmares não era só de africanos
    {
        "temas_secundarios": ["heranca_africana", "povos_indigenas"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Palmares não abrigava só africanos fugidos da escravidão: também indígenas, caboclos e portugueses pobres, entre eles soldados fugindo do serviço militar. E resistiu de 1605 a 1694.",
        "explicacao": (
            "Palmares se formou na capitania de Pernambuco, no atual estado de Alagoas, e "
            "cresceu ao longo de quase todo o século XVII. Hoje é chamado de quilombo, mas nenhum documento da "
            "época usou essa palavra: dizia-se mocambo. A comunidade recebia africanos que fugiam da escravidão, mas "
            "também indígenas, caboclos e portugueses pobres ou marginalizados, sobretudo soldados que escapavam "
            "do serviço militar obrigatório. Uma estimativa fala em 20 mil habitantes nos anos 1690. Estudos "
            "recentes acham o número exagerado, e o historiador Stuart Schwartz calcula cerca de 11 mil, mas ainda "
            "assim foi, sem dúvida, a maior comunidade de fugitivos que já existiu no Brasil. Sua organização "
            "política se inspirava em vários modelos da África Central. Palmares "
            "foi destruído em 1694, e Zumbi, seu líder mais famoso, foi capturado e morto em 20 de novembro de "
            "1695."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Quilombo_dos_Palmares",
            "Palmares, or Quilombo dos Palmares, was a quilombo, a community of escaped slaves and others, in colonial Brazil that developed from 1605 until its suppression in 1694. "
            "It was located in the captaincy of Pernambuco, in what is today the Brazilian state of Alagoas. [...] "
            "No contemporary document called Palmares a quilombo; instead the term mocambo was used. "
            "Palmares was home to not only escaped enslaved Africans, but also to Indigenous peoples, caboclos, and poor or marginalized Portuguese settlers, especially Portuguese soldiers trying to escape forced military service. [...] "
            "One estimate places the population of Palmares in the 1690s at around 20,000 inhabitants, although recent scholarship has questioned whether this figure is exaggerated. "
            "Stuart Schwartz places the number at roughly 11,000, noting that it was, regardless, \"undoubtedly the largest fugitive community to have existed in Brazil\". "
            "These inhabitants developed a society and government that derived from a range of Central African sociopolitical models [...] "
            "Zumbi was wounded. He eluded the Portuguese, but was betrayed, finally captured, and beheaded on November 20, 1695.",
            nome="Quilombo dos Palmares")],
    },
]
