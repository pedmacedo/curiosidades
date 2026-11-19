LOTE = "2026-11-17-grandes_navegacoes-01"
AREA = "historia_moderna"
TEMA = "grandes_navegacoes"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = W if idioma == "en" else "https://pt.wikipedia.org/wiki/"
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o dia perdido da volta ao mundo
    {
        "temas_secundarios": ["calendarios", "medidas_padroes"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Os sobreviventes da primeira volta ao mundo anotaram todos os dias da viagem e, ao chegar a Cabo Verde, descobriram que tinham \"perdido\" um dia.",
        "explicacao": (
            "A frota de Fernão de Magalhães saiu da Espanha em 20 de setembro de 1519, com cinco navios e cerca de "
            "270 homens. Magalhães morreu em combate nas Filipinas em 1521, e só um navio, o Victoria, comandado por "
            "Juan Sebastián Elcano, completou a volta ao mundo, com 18 homens. Em julho de 1522, já perto de casa, a "
            "tripulação parou em Cabo Verde para buscar mantimentos. No diário de bordo era quarta-feira, 9 de "
            "julho. Os moradores disseram que era quinta, 10 de julho. Os marinheiros se espantaram, porque tinham "
            "registrado cada dia dos três anos de viagem sem falhar nenhum. A explicação: quem dá a volta ao mundo "
            "para o oeste acompanha o Sol e, a cada volta completa, vê um nascer do sol a menos. O efeito tinha "
            "sido previsto no século XIV pelo geógrafo árabe Abulfeda. É por isso que hoje existe a Linha "
            "Internacional de Data."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("International_Date_Line",
                "The 14th-century Arab geographer Abulfeda predicted that circumnavigators would accumulate a one-day offset to the local date. "
                "This phenomenon was confirmed in 1522 at the end of the Magellan–Elcano expedition, the first successful circumnavigation. "
                "After sailing westward around the world from Spain, the expedition called at Cape Verde for provisions on Wednesday, 9 July 1522 (ship's time). "
                "However, the locals told them that it was actually Thursday, 10 July 1522. "
                "The crew was surprised, as they had recorded each day of the three-year journey without omission. [...] "
                "People traveling westward around the world must set their clocks: Back by one hour for every 15° of longitude crossed",
                nome="International Date Line"),
            wiki("Magellan_expedition",
                "The five-ship fleet left Spain on 20 September 1519 with about 270 men. [...] "
                "Only 18 men and one ship—the Victoria—completed the circumnavigation, and Magellan himself died in battle in the Philippines in April 1521.",
                nome="Magellan expedition"),
        ],
    },
    # 2 escorbuto
    {
        "temas_secundarios": ["historia_medicina", "especiarias"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "O escorbuto, a falta de vitamina C, matou pelo menos 2 milhões de marinheiros na era das navegações. A cura, frutas cítricas, só foi demonstrada em 1747.",
        "explicacao": (
            "Nos navios das grandes navegações, a comida durava meses, mas frutas e verduras frescas não. O "
            "resultado era o escorbuto. A viagem de Fernão de Magalhães deixou uma descrição: em alguns homens, as "
            "gengivas cresciam por cima dos dentes, de cima e de baixo, e eles não conseguiam comer. Segundo um "
            "levantamento citado pelo historiador Jonathan Lamb, em 1499 Vasco da Gama perdeu 116 de seus 170 "
            "tripulantes, e em 1520 Magalhães perdeu 208 de 230, quase todos por escorbuto. Pesquisadores estimam "
            "que, entre 1500 e 1800, a doença matou pelo menos 2 milhões de marinheiros. Houve quem desconfiasse "
            "da dieta, mas só em 1747 o médico escocês James Lind demonstrou formalmente que o escorbuto podia ser "
            "tratado com frutas cítricas, num dos primeiros experimentos clínicos controlados da história da "
            "medicina."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Scurvy",
            "Researchers have estimated that during the Age of Exploration (between 1500 and 1800), scurvy killed at least two million sailors. "
            "Jonathan Lamb wrote: \"In 1499, Vasco da Gama lost 116 of his crew of 170; In 1520, Magellan lost 208 out of 230; ... all mainly to scurvy.\" [...] "
            "In the 1519-1521 circumnavigation, Magellan's crew suffered from scurvy: \"above all other calamities this was the worst: in some men the gums grew over the teeth, both lowers and uppers, so that they could not eat in any way [...] "
            "It was not until 1747 that James Lind formally demonstrated that scurvy could be treated by supplementing the diet with citrus fruit, in one of the first controlled clinical experiments reported in the history of medicine.")],
    },
    # 3 a girafa de Zheng He
    {
        "temas_secundarios": ["asia_antiga", "mitologia", "animais_extremos"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "No século XV, a frota chinesa de Zheng He levou uma girafa da África para a China, e a corte a recebeu como um qilin, criatura mítica sinal de bom governo.",
        "explicacao": (
            "Décadas antes de os portugueses chegarem à Índia, a China já mandava frotas enormes pelo oceano "
            "Índico. Entre 1405 e 1433, o almirante Zheng He comandou sete viagens dos chamados navios do tesouro, "
            "a serviço dos imperadores da dinastia Ming. Segundo a tradição, os maiores navios tinham quase o dobro "
            "do comprimento de qualquer navio de madeira registrado, embora isso seja lenda. A frota levava ouro, "
            "prata, porcelana e seda, e trazia novidades da costa africana: avestruzes, zebras, camelos e marfim. A "
            "peça mais famosa foi uma girafa trazida de Malindi, no atual Quênia. Na China, ela foi tomada por um "
            "qilin, animal mítico da tradição chinesa, e apresentada como prova de que o governo tinha o Mandato "
            "do Céu, a aprovação divina para reinar."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Zheng_He",
            "Between 1405 and 1433, Zheng commanded seven treasure voyages across Asia under the commission of the Yongle Emperor and the succeeding Xuande Emperor (r. 1425–1435). "
            "According to legend, Zheng's largest ships were almost twice as long as any wooden ship ever recorded, and carried hundreds of sailors on four decks. [...] "
            "Zheng He presented gifts of gold, silver, porcelain, and silk, and in return, China received such novelties as ostriches, zebras, camels, and ivory from the Swahili Coast. "
            "The giraffe that he brought back from Malindi was considered to be a qilin and taken as proof of the Mandate of Heaven upon the administration.",
            nome="Zheng He")],
    },
    # 4 o mito da Terra plana
    {
        "temas_secundarios": ["europa_medieval", "historia_astronomia", "literatura"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "Ninguém precisou convencer os sábios do tempo de Colombo de que a Terra era redonda. A discussão era sobre o tamanho dela, e quem errou feio foi Colombo.",
        "explicacao": (
            "A ideia de uma Terra esférica aparece claramente entre os gregos desde o século V antes de Cristo, e "
            "Eratóstenes calculou a circunferência do planeta por volta de 240 antes de Cristo. Na Idade Média, a "
            "maioria dos estudiosos europeus e do Oriente Médio sabia que a Terra era redonda. Então de onde veio a "
            "cena de Colombo enfrentando sábios que temiam cair da borda do mundo? Boa parte veio de uma biografia "
            "romanceada escrita em 1828 pelo americano Washington Irving, que muitos tomaram por obra acadêmica. "
            "Nela, Irving inventou que membros ignorantes de uma comissão espanhola teriam feito objeções "
            "religiosas à Terra esférica. Na verdade, a questão nos anos 1490 era o tamanho do planeta e a "
            "posição da costa da Ásia. Os críticos de Colombo estavam certos sobre a distância: ele só não morreu no "
            "meio do oceano porque havia um continente no caminho."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Myth_of_the_flat_Earth",
            "The earliest clear documentation of the idea of a spherical Earth comes from the ancient Greeks (5th century BC). "
            "The belief was widespread in the Greek world when Eratosthenes calculated the circumference of Earth around 240 BC. "
            "This knowledge spread with Greek influence such that during the Early Middle Ages (c. 600 –1000 AD), most European and Middle Eastern [...] "
            "In 1828, Washington Irving's highly romanticized biography, A History of the Life and Voyages of Christopher Columbus, was published and mistaken by many for a scholarly work. "
            "In Book II, Chapter IV of this biography, Irving gave a largely fictional account of the meetings of a commission established by the Spanish sovereigns to examine Columbus's proposals. "
            "One of his more fanciful embellishments was a highly unlikely tale that the more ignorant and bigoted members on the commission had raised scriptural objections to Columbus's assertions that the Earth was spherical. "
            "The issue in the 1490s was not the shape of the Earth, but its size, and the position of the east coast of Asia",
            nome="Myth of the flat Earth")],
    },
    # 5 Run por Manhattan
    {
        "temas_secundarios": ["especiarias", "imperios_coloniais", "cidades"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Num acordo de 1667, a Holanda ficou com uma ilhota de noz-moscada na Indonésia, com 3 km de comprimento, e a Inglaterra ficou com Manhattan.",
        "explicacao": (
            "No século XVII, a minúscula ilha de Run, a mais ocidental das ilhas Banda, na atual Indonésia, tinha "
            "enorme valor econômico por causa das especiarias que produzia: a noz-moscada e o macis. Ela tem cerca "
            "de 3 km de comprimento e 1 km de largura. Ingleses e holandeses disputaram a ilha. Do outro lado do "
            "mundo, o duque de York tinha ocupado em 1664 a colônia holandesa de Nova Amsterdã, na ilha de Manhattan, "
            "e rebatizado a cidade de Nova York. Depois da Segunda Guerra Anglo-Holandesa, os dois países "
            "assinaram o Tratado de Breda, em 1667, e cada um ficou com o que tinha: os ingleses mantiveram "
            "Manhattan, e Run foi formalmente deixada para os holandeses. Na época, a troca parecia boa para a "
            "Holanda, que garantia o controle da noz-moscada. Hoje, Manhattan é o coração de Nova York."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Run_(island)",
            "In the 17th century, the tiny island of Run was of great economic importance because of the value of the spices it produced: nutmeg and mace. [...] "
            "Run is the westernmost island of the Banda Islands, with a length of 3 kilometres (1.9 mi) and width of 1 kilometre (0.62 mi). [...] "
            "After the Second Anglo-Dutch War (1665–1667), England and the United Provinces of the Netherlands agreed in the Treaty of Breda to the status quo: "
            "the English kept the island of Manhattan, which the Duke of York (the future James II, brother of Charles II), had occupied in 1664, renaming the city on that island from New Amsterdam to New York. "
            "In return, Run was formally abandoned to the Dutch.",
            nome="Run (island)")],
    },
    # 6 volta do mar
    {
        "temas_secundarios": ["navegacao_antiga", "clima_tempo", "brasil_colonial"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "Para voltar da África ou ir para a Índia, os navegadores portugueses se afastavam muito para o oeste, rumo ao Brasil. Era a \"volta do mar\", um truque com os ventos.",
        "explicacao": (
            "No oceano Atlântico, os ventos e as correntes giram em grandes círculos. No Atlântico Norte, o giro é "
            "no sentido horário; no Sul, no sentido anti-horário. Os navegadores portugueses do século XV "
            "aprenderam a tirar proveito disso. Para voltar das ilhas atlânticas para Portugal, em vez de ir em "
            "linha reta contra o vento, o piloto primeiro navegava para bem longe a oeste, até encontrar ventos "
            "favoráveis, e só então seguia para casa. Era uma rota que parecia absurda, quase perpendicular ao "
            "destino. Colombo só conseguiu voltar das Américas usando a mesma técnica. No Atlântico Sul, as "
            "viagens portuguesas rumo à Índia, depois de cruzar o equador, também se afastavam muito para o oeste, "
            "chegando perto do Brasil. Sem entender esses ventos, dizem os historiadores, os impérios marítimos "
            "europeus não teriam existido."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Volta_do_mar",
            "is a navigational technique perfected by Portuguese navigators during the Age of Discovery in the late fifteenth century, using the dependable phenomenon of the great permanent wind circle, the North Atlantic Gyre. "
            "This was a major step in the history of navigation, when an understanding of winds in the age of sail was crucial to success: the European sea empires would not have been established without an understanding of the trade winds. [...] "
            "The volta do mar was a sailing technique discovered in successfully returning from the Atlantic islands, where the pilot first had to sail far to the west in order to catch usable following winds, and return to Europe. "
            "This was a counter-intuitive sailing direction, as it required the pilot to steer in a direction that was perpendicular to the ports of Portugal. [...] "
            "for example Christopher Columbus would never have returned from the Americas without applying the volta do mar [...] "
            "A similar phenomenon occurs in the South Atlantic, with the exception that the South Atlantic Gyre circulates counterclockwise. "
            "As India-bound Portuguese explorers and traders crossed the equator with the intention of passing the entire western coast of Africa, their voyages took them far to the West (in the vicinity of Brazil.)",
            nome="Volta do mar")],
    },
    # 7 o tomate italiano
    {
        "temas_secundarios": ["historia_pratos", "domesticacao"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "O molho de tomate italiano é mais novo do que parece: o tomate veio das Américas, e a primeira receita italiana com o molho só foi publicada em 1692.",
        "explicacao": (
            "O tomate é americano. Cultivadores levaram tomates selvagens da América Central para a América do Sul, "
            "e, pouco depois das viagens de Colombo, a planta chegou à Espanha e dali a outros países europeus, "
            "inclusive a Itália. Em 1544, o médico e botânico toscano Pietro Andrea Mattioli registrou que lá o "
            "tomate era comido frito no azeite. O primeiro livro de culinária italiano com molho de tomate, Lo "
            "Scalco alla Moderna, do chef Antonio Latini, saiu em dois volumes, em 1692 e 1694. E o molho de "
            "tomate com massa só apareceu num livro de receitas italiano em 1790. Essa troca de plantas entre os "
            "continentes, o chamado intercâmbio colombiano, mudou a comida do mundo: milho, batata, mandioca e "
            "pimenta também são americanos. Estima-se que a batata tenha respondido por 12% a 25% do crescimento "
            "populacional da Afro-Eurásia entre 1700 e 1900."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Columbian_exchange",
            "American crops such as maize, potatoes, tomatoes, tobacco, cassava, sweet potatoes, and chili peppers became important crops around the world. [...] "
            "Potatoes eventually became an important staple food in the diets of many Europeans, contributing to an estimated 12 to 25% of the population growth in Afro-Eurasia between 1700 and 1900. [...] "
            "cultivators brought wild tomatoes from Central America to South America. "
            "Soon after Columbus's visit, tomatoes were brought to Spain, and from there to other European countries, including Italy. "
            "In 1544, Pietro Andrea Mattioli, a Tuscan physician and botanist, wrote that the tomato was eaten fried in oil there. "
            "The first Italian cookbook to include tomato sauce, Lo Scalco alla Moderna (\"The Modern Steward\"), was written by Italian chef Antonio Latini and was published in two volumes in 1692 and 1694. "
            "In 1790, the use of tomato sauce with pasta appeared for the first time, in the Italian cookbook",
            nome="Columbian exchange")],
    },
    # 8 os nomes da sífilis
    {
        "temas_secundarios": ["doencas_infecciosas", "palavras_viajantes"],
        "tipos_espanto": ["historia_humana", "misterio_aberto"],
        "gancho": "Na Itália, a sífilis era a \"doença francesa\"; na França, a \"italiana\"; para os holandeses, \"espanhola\"; para os russos, \"polonesa\". Sua origem ainda é debatida.",
        "explicacao": (
            "O primeiro surto registrado de sífilis na Europa aconteceu em 1494 e 1495, em Nápoles, durante uma "
            "invasão francesa. Como os soldados franceses espalharam a doença ao voltar da campanha, ela ficou "
            "conhecida como \"mal francês\". O nome sífilis só foi usado a partir de 1530, pelo médico e poeta "
            "italiano Girolamo Fracastoro. Até lá, cada povo culpava o vizinho: era a doença francesa na Itália, em "
            "Malta, na Polônia e na Alemanha; a italiana na França; a espanhola para os holandeses; a polonesa "
            "para os russos; e, para os turcos, a doença dos cristãos. Os nomes refletiam mais as rixas políticas "
            "do que a ciência. A origem continua em debate. Uma hipótese diz que a doença veio das Américas com os "
            "marinheiros de Colombo; a outra, que já existia na Europa sem ser reconhecida. Sabe-se que doenças "
            "aparentadas existiam nas Américas muito antes do contato com os europeus."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("History_of_syphilis",
            "The first recorded outbreak of syphilis in Europe occurred in 1494/1495 in Naples, Italy, during a French invasion. "
            "Because it was spread geographically by French troops returning from that campaign, the disease was known as \"French disease\", and it was not until 1530 that the term \"syphilis\" was first applied by the Italian physician and poet Girolamo Fracastoro. [...] "
            "hilis had been called the \"French disease\" (Italian: mal francese) in Italy, Malta, Poland and Germany, and the \"Italian disease\" in France. "
            "In addition, the Dutch called it the \"Spanish disease\", the Russians called it the \"Polish disease\", and the Turks called it the \"Christian disease\" or \"Frank (Western European) disease\" (frengi). "
            "These \"national\" names were generally reflective of contemporary political spite between nations [...] "
            "one, first proposed in the 1880s, was that syphilis was carried to Europe from the Americas by the crew(s) of Christopher Columbus as a byproduct of the Columbian exchange. "
            "The other hypothesis, first proposed in the 1930s, was that syphilis previously existed in Europe but went unrecognized. [...] "
            "There is no doubt that treponematosis existed in the Americas long before contact with Europe and Afro-Eurasia.",
            nome="History of syphilis")],
    },
    # 9 padrões de pedra
    {
        "temas_secundarios": ["imperios_coloniais", "fronteiras_paises", "africa_antiga"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Os navegadores portugueses levavam colunas de pedra já esculpidas em Portugal e as fincavam nas costas que alcançavam, como prova de que tinham chegado primeiro.",
        "explicacao": (
            "Um padrão era uma coluna de pedra deixada pelos exploradores portugueses dos séculos XV e XVI para "
            "registrar uma chegada importante e marcar a prioridade e a posse de Portugal. Costumava ser posto em "
            "promontórios, cabos ou na foz de grandes rios. Os primeiros marcos eram simples colunas ou cruzes de "
            "madeira, que apodreciam depressa no clima tropical. Por isso passaram a ser de pedra, com uma cruz no "
            "alto e o brasão real. O primeiro a levar padrões de pedra foi Diogo Cão, na viagem pela costa africana "
            "de 1482 a 1484. As colunas tinham sido esculpidas antes, em Portugal, e iam no navio por ordem do rei "
            "D. João II. Cão as fincou em pontos dos atuais Gabão, Angola e Namíbia, e o primeiro ficou na foz do "
            "rio Congo."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Padr%C3%A3o",
            "is a stone pillar left by Portuguese maritime explorers in the 15th and 16th centuries to record significant landfalls and thereby establish primacy and possession. "
            "They were often placed on promontories and capes or at the mouths of major rivers. "
            "Early markers were simple wooden pillars or crosses but they deteriorated quickly in the tropical climate where they were often erected. "
            "Later, padrões were carved from stone in the form of a pillar surmounted by a cross and the royal coat of arms. [...] "
            "Diogo Cão was the first to place stone padrões on his voyage of discovery along the coast of Africa in 1482–1484. "
            "They had been carved ahead of time in Portugal and carried in his ship at the behest of King João II. "
            "Cão placed the pillars at points in what is now Gabon, Angola and Namibia. "
            "The first was installed at the mouth of the river Congo.",
            nome="Padrão")],
    },
]
