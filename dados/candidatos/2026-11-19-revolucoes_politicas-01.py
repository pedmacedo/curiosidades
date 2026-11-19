LOTE = "2026-11-19-revolucoes_politicas-01"
AREA = "historia_moderna"
TEMA = "revolucoes_politicas"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o Motim do Chá de Boston e o chá que ficou mais barato
    {
        "temas_secundarios": ["economia_curiosa", "cafe_cha_cacau"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "O Motim do Chá de Boston, em 1773, não foi um protesto contra chá caro. A lei que o provocou deixava o chá legal mais barato, a ponto de custar menos que o contrabandeado.",
        "explicacao": (
            "Em 1773, a Companhia Britânica das Índias Orientais estava perto da falência, com montanhas de chá "
            "encalhado nos armazéns de Londres. Nas Treze Colônias, a maior parte do chá vinha de contrabando "
            "holandês, que não pagava impostos: cerca de 86% do total, segundo uma estimativa. A Lei do Chá, "
            "aprovada naquele ano, deixou a companhia mandar o produto direto para a América, sem intermediários e "
            "sem os tributos cobrados na Grã-Bretanha. Com isso, a libra-peso do chá legal, que custava uns 3 "
            "xelins, poderia ser vendida por 2, abaixo dos 2 xelins e 1 pêni cobrados pelos contrabandistas. O "
            "pulo do gato estava no que a lei mantinha: um imposto de 3 pence por libra recolhido nas colônias. "
            "Comprando o chá mais barato, os colonos aceitariam na prática o direito do Parlamento de taxá-los. A "
            "resistência juntou quem defendia o princípio de \"nenhum imposto sem representação\" e comerciantes, "
            "alguns deles contrabandistas, que seriam arruinados pela concorrência. Em 16 de dezembro de 1773, "
            "colonos, alguns disfarçados de indígenas, subiram nos navios ancorados em Boston e jogaram ao mar 340 "
            "ou 342 caixas de chá. As punições britânicas que vieram depois aumentaram a tensão que desembocou na "
            "guerra de independência."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Boston_Tea_Party",
                "The protest movement that culminated with the Boston Tea Party was not a dispute about high taxes. "
                "The price of legally imported tea was actually reduced by the Tea Act of 1773. [...] "
                "The familiar \"no taxation without representation\" argument [...] "
                "In 1772, legally imported Bohea, the most common variety of tea, sold for about 3 shillings (3s) per pound [...] "
                "After the Tea Act, colonial consignees would be able to sell tea for 2 shillings per pound (2s), just under the smugglers' price of 2 shillings and 1 penny (2s 1d). [...] "
                "its hidden purpose was to force the colonists to pay a tax of 3 pennies on every pound of tea. [...] "
                "Colonial merchants, some of them smugglers, played a significant role in the protests. "
                "Because the Tea Act made legally imported tea cheaper, it threatened to put smugglers of Dutch tea out of business. [...] "
                "threw 340 or 342 chests into Boston Harbor.",
                nome="Boston Tea Party"),
            wiki("Tea_Act",
                "The principal objective was to reduce the massive amount of tea held by the financially troubled British East India Company in its London warehouses [...] "
                "approximately 86% of all the tea in America at the time was smuggled Dutch tea. "
                "The act granted the company the right to directly ship its tea to North America and the right to the duty-free export of tea from Britain, although the tax imposed by the Townshend Acts and collected in the colonies remained in force. [...] "
                "In Boston, this resistance culminated in the Boston Tea Party on December 16, 1773, when colonists (some disguised as Native Americans) boarded tea ships anchored in the harbour and dumped their tea cargo overboard. [...] "
                "These actions further raised tensions that led to the eruption of the American War of Independence [...] "
                "Colonists would willingly pay for cheaper Company tea, on which the Townshend tax was still collected, thus legitimizing Parliament's ability to tax the colonies.",
                nome="Tea Act"),
        ],
    },
    # 2 Adams e Jefferson morrem no mesmo 4 de julho
    {
        "temas_secundarios": ["personagens_esquecidos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "John Adams e Thomas Jefferson, líderes da independência dos EUA, morreram no mesmo dia: 4 de julho de 1826, 50 anos após a Declaração. Últimas palavras de Adams: \"Jefferson sobrevive\". Errou por horas.",
        "explicacao": (
            "Os dois estiveram juntos no Congresso que aprovou a Declaração de Independência. Anos depois, "
            "Jefferson chamaria Adams de \"pilar\" da defesa do texto no plenário. Depois veio a política. Adams "
            "foi o segundo presidente dos EUA, e Jefferson, seu vice-presidente. Na eleição de 1800, Jefferson, "
            "então descrito como ex-amigo, derrotou Adams. Desde que Adams deixou o cargo, as casas dos dois "
            "ficaram sem contato até 1812, tirando uma breve troca de cartas entre Jefferson e Abigail, mulher de "
            "Adams, que logo descambou para a briga política. No início de 1812, o médico Benjamin Rush, amigo "
            "dos dois, incentivou a reaproximação. Adams mandou um bilhete amistoso no Ano-Novo, Jefferson "
            "respondeu na hora com uma carta cordial, e a amizade renasceu pelo correio. As cartas seguiram até o "
            "fim da vida deles e são tidas como um dos grandes legados da literatura americana. Em 4 de julho de "
            "1826, exatos 50 anos depois da aprovação da Declaração, Adams morreu de um ataque cardíaco em casa, "
            "por volta das 6 e 20 da tarde, aos 90 anos. Entre suas últimas palavras, lembrou o amigo e rival: "
            "\"Thomas Jefferson sobrevive\". Não sabia que Jefferson tinha morrido várias horas antes."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("John_Adams",
            "John Adams (October 30, 1735 – July 4, 1826) was a Founding Father and the second president of the United States from 1797 to 1801. [...] "
            "Adams was the first vice president of the United States, serving from 1789 to 1797. [...] "
            "In his 1800 bid for reelection to the presidency, opposition from Federalists and accusations of despotism from Jeffersonians led to Adams losing to his vice president and former friend, Thomas Jefferson. [...] "
            "Jefferson hailed Adams as \"the pillar of [the Declaration's] support on the floor of Congress, [its] ablest advocate and defender against the multifarious assaults it encountered.\" [...] "
            "Congress approved the Declaration of Independence on July 4. [...] "
            "This initiated a brief correspondence between the two which quickly descended into political rancor. "
            "Jefferson terminated it by not replying to Abigail's fourth letter. "
            "Aside from that, by 1812 there had been no communication between Monticello, the home of Jefferson, and Peacefield since Adams left office. "
            "In early 1812, Adams reconciled with Jefferson. [...] "
            "Their mutual friend Benjamin Rush, who had been corresponding with both, encouraged them to reach out to each other. "
            "On New Year's Day, Adams sent a brief, friendly note to Jefferson [...] "
            "Jefferson replied immediately with a cordial letter, and the two revived their friendship, which they sustained by mail. "
            "Their correspondence lasted the rest of their lives, and has been hailed as among the great legacies of American literature. [...] "
            "On July 4, 1826, the 50th anniversary of the adoption of the Declaration of Independence, Adams died of a heart attack at Peacefield at approximately 6:20 pm. "
            "His last words included an acknowledgement of his longtime friend and rival: \"Thomas Jefferson survives.\" "
            "Adams was unaware that Jefferson had died several hours before. At 90, Adams was the longest-lived US president",
            nome="John Adams")],
    },
    # 3 a Bastilha tinha sete presos e o alvo era a pólvora
    {
        "temas_secundarios": ["arquitetura"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Quando a Bastilha foi tomada, em 1789, havia só sete presos lá dentro, e a fortaleza já estava marcada para demolição. O que a multidão exigia eram as armas e a pólvora guardadas ali.",
        "explicacao": (
            "Antes de chegar à Bastilha, em 14 de julho de 1789, os revolucionários de Paris tinham invadido o "
            "Hôtel des Invalides atrás de armas e levado de 29 mil a 32 mil mosquetes, mas sem pólvora nem "
            "munição. Dias antes, o comandante dos Invalides transferira 250 barris de pólvora para a Bastilha, "
            "que parecia um lugar mais seguro. A multidão se juntou diante da fortaleza pedindo que os canhões "
            "fossem recuados e que as armas e a pólvora fossem liberadas. Depois de quatro horas de luta e 94 "
            "mortos, os insurgentes entraram. A Bastilha era um símbolo do poder do rei, mas quase não funcionava "
            "mais como prisão: lá estavam quatro falsificadores, dois homens tidos como loucos e um conde preso a "
            "pedido da própria família. O Marquês de Sade, que também estivera preso ali, tinha sido transferido "
            "dez dias antes, depois de gritar a quem passava na rua que os presos estavam sendo massacrados. "
            "Manter a velha fortaleza custava caro, e pouco antes já se decidira trocá-la por um espaço público. "
            "Depois da queda, ela foi demolida em cinco meses, e o empreiteiro da demolição vendeu réplicas "
            "esculpidas em tijolos dela. Lafayette deu a chave da Bastilha a George Washington, e ela continua "
            "exposta em Mount Vernon, a casa dele."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Storming_of_the_Bastille",
            "which occurred in Paris, France, on 14 July 1789 [...] "
            "After four hours of fighting and 94 deaths, the insurgents were able to enter the Bastille. [...] "
            "The prison contained only seven inmates at the time of its storming and was already scheduled for demolition but was seen by the revolutionaries as a symbol of the monarchy's abuse of power. [...] "
            "had earlier stormed the Hôtel des Invalides without meeting significant opposition. "
            "Their intention had been to gather the weapons held there (29,000 to 32,000 muskets, but without powder or shot). "
            "The commandant at the Invalides had in the previous few days taken the precaution of transferring 250 barrels of gunpowder to the Bastille for safer storage. [...] "
            "four forgers arrested under warrants issued by the Grand Châtelet court; James F.X. Whyte, an Irish born \"lunatic\" [...] "
            "A previous prisoner the Marquis de Sade had been transferred out ten days earlier, after shouting to passers-by that the prisoners were being massacred. "
            "The high cost of maintaining a garrisoned medieval fortress, for what was seen as having a limited purpose, had led to a decision being made shortly before the disturbances began to replace it with an open public space [...] "
            "calling for the pulling back of the seemingly threatening cannon from the embrasures of the towers and walls and the release of the arms and gunpowder stored inside. [...] "
            "the prison contained only seven inmates: four forgers, two mentally ill men, and a count imprisoned at his family's request. [...] "
            "were all carried out within five months. "
            "In 1790, Lafayette gave the key to the Bastille—weighing one pound three ounces—to U.S. President George Washington. [...] "
            "The key remains on display at Washington's residence of Mount Vernon. "
            "Palloy took bricks from the Bastille and had them carved into replicas of the fortress, which he sold",
            nome="Storming of the Bastille")],
    },
    # 4 o calendário republicano: semana de dez dias e dias com nome de nabo
    {
        "temas_secundarios": ["calendarios", "religioes"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "No calendário da Revolução Francesa, a semana tinha dez dias e cada dia do ano ganhou nome de planta, bicho, mineral ou ferramenta, no lugar dos santos. Os trabalhadores reclamaram: a folga virou um dia em dez.",
        "explicacao": (
            "O calendário republicano foi adotado em 1793 e usado pelo governo francês por cerca de 12 anos. Tinha "
            "12 meses de 30 dias, cada um dividido em três \"décadas\" de dez dias, mais cinco ou seis dias de "
            "festa no fim do ano. Os meses tinham nomes ligados ao clima e ao campo, como Brumário, da névoa, e "
            "Termidor, do calor do verão. A ideia era apagar a influência da Igreja e da monarquia. No calendário "
            "católico, cada dia era dedicado a um santo; o poeta Fabre d'Églantine, que inventou os nomes dos "
            "meses, deu a cada dia um nome tirado da vida rural. Os dias terminados em 5 levavam o nome de um "
            "animal, os terminados em 0, o de uma ferramenta agrícola, e os demais, nomes de plantas, exceto no "
            "Nivoso, o primeiro mês do inverno, em que eram minerais. O décimo dia, o décadi, substituiu o domingo "
            "como dia de descanso, e por um tempo os casamentos só podiam ser celebrados nele. A semana de dez dias "
            "desagradou aos trabalhadores, que passaram a ter um dia livre a cada dez, e não a cada sete, e acabou "
            "suprimida antes do resto. Napoleão aboliu o calendário em 1806. Fabre não viu o fim: foi guilhotinado "
            "em 1794, acusado de falsificação num caso de corrupção ligado à Companhia Francesa das Índias Orientais."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("French_Republican_calendar",
                "used by the French government for about 12 years from late 1793 to 1805 [...] "
                "The calendar consisted of twelve 30-day months, each divided into three 10-day cycles similar to weeks, plus five or six intercalary days at the end to fill out the balance of a solar year. "
                "It was designed in part to remove all religious and royalist influences from the calendar [...] "
                "the republican calendar continued to be used until 1 January 1806, when Napoleon declared it abolished. [...] "
                "poet, actor and playwright Fabre d'Églantine (who invented the names of the months) [...] "
                "The month names were based on nature, principally having to do with the prevailing weather in and around Paris [...] "
                "Brumaire (from French brume 'mist' [...] "
                "Thermidor (from Greek θέρμη, thermē, 'summer heat') [...] "
                "Décadis became an official day of rest instead of Sunday, in order to diminish the influence of the Roman Catholic Church. [...] "
                "required that marriages must only be celebrated on décadis. [...] "
                "The Roman Catholic Church used a calendar of saints, which named each day of the year after an associated saint. "
                "To reduce the influence of the Church, Fabre d'Églantine introduced a rural calendar in which each day of the year had a unique name associated with the rural economy [...] "
                "Every décadi (ending in 0) was named after an agricultural tool. "
                "Each quintidi (ending in 5) was named for a common animal. "
                "The rest of the days were named for \"grain, pasture, trees, roots, flowers, fruits\" and other plants, except for the first month of winter, Nivôse, during which the rest of the days were named after minerals. [...] "
                "the 10-day décade was unpopular and had already been suppressed three years earlier in favor of the seven-day week [...] "
                "The 10-day décade was unpopular with laborers because they received only one full day of rest out of ten, instead of one in seven",
                nome="French Republican calendar"),
            wiki("Fabre_d'Églantine",
                "On 12 January 1794 Fabre was arrested by order of the Committee of Public Safety on a charge of malversation and forgery in connection with the affairs of the French East India Company. [...] "
                "Fabre died under the guillotine on 5 April 1794 with the other Dantonists.",
                nome="Fabre d'Églantine"),
        ],
    },
    # 5 a hora decimal: meio-dia eram "cinco horas"
    {
        "temas_secundarios": ["medidas_padroes", "calendarios"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "A Revolução Francesa tentou decimalizar até o relógio: dias de 10 horas, horas de 100 minutos. Meio-dia virou \"cinco horas\". Fizeram relógios assim, mas a obrigação durou pouco mais de seis meses.",
        "explicacao": (
            "Junto com o metro e o calendário republicano, os revolucionários quiseram aplicar a base 10 também à "
            "hora do dia. O dia passou a ter 10 horas decimais, cada uma com 100 minutos decimais de 100 segundos "
            "decimais, num total de 100.000 segundos por dia. A hora nova equivalia a 144 minutos comuns, e o "
            "segundo novo, a 0,864 segundo comum. Na contagem, meia-noite era \"dez horas\" e meio-dia, \"cinco "
            "horas\". Foram fabricados relógios de parede e de bolso com mostradores que exibiam as duas "
            "contagens, a tradicional e a decimal. Mas o sistema não pegou. O uso nos registros públicos só passou "
            "a valer em 22 de setembro de 1794, e a obrigatoriedade foi suspensa em 7 de abril de 1795, pela "
            "mesma lei que instituiu o sistema métrico. Um dos argumentos contra era que a mudança não trazia "
            "vantagem clara para quase ninguém e ainda poderia prejudicar a aceitação das novas medidas. Algumas "
            "cidades insistiram por mais tempo: em Toulouse, um relógio decimal que só tinha o ponteiro das horas "
            "ficou cinco anos na fachada do Capitólio. A divisão decimal acabou útil mesmo para os astrônomos, e "
            "a França ainda faria outra tentativa de decimalizar o tempo em 1897."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Decimal_time",
                "French Republican calendar time system used from 1794 to 1800, during the French Revolution, which divided the day into 10 decimal hours, each decimal hour into 100 decimal minutes and each decimal minute into 100 decimal seconds (100,000 decimal seconds per day) [...] "
                "Thus, midnight was called dix heures (\"ten hours\"), noon was called cinq heures (\"five hours\"), etc. [...] "
                "Although clocks and watches were produced with faces showing both standard time with numbers 1–24 and decimal time with numbers 1–10, decimal time never caught on; "
                "it was not used for public records until the beginning of the Republican year III, 22 September 1794, and mandatory use was suspended 7 April 1795 (18 Germinal of the Year III). "
                "In spite of this, decimal time was used in many cities, including Marseille and Toulouse, where a decimal clock with just an hour hand was on the front of the Capitole for five years. [...] "
                "As it does not offer almost all of the nation any marked advantage, it would only throw a disadvantage on the new system of measures and the decimal method [...] "
                "Thus, the law of 18 Germinal An III (April 7, 1795) establishing the metric system, rather than including metric units for time, repealed the mandatory use of decimal time, although its use continued for a number of years in some places. "
                "As predicted, it was quickly found to be useful by astrono [...] "
                "The French made another attempt at the decimalization of time in 1897",
                nome="Decimal time"),
            wiki("French_Republican_calendar",
                "Thus an hour was 144 conventional minutes (2.4 times as long as a conventional hour), a minute was 86.4 conventional seconds (44% longer than a conventional minute), and a second was 0.864 conventional seconds (13.6% shorter than a conventional second). "
                "Clocks were manufactured to display this decimal time, but it did not catch on.",
                nome="French Republican calendar"),
        ],
    },
    # 6 o metro e as dúvidas de Méchain
    {
        "temas_secundarios": ["medidas_padroes", "historia_astronomia"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "O metro nasceu na Revolução Francesa, de uma medição da Terra entre Dunquerque e Barcelona. Um dos astrônomos encarregados chegou a ser preso porque desconfiaram que seus instrumentos fossem armas.",
        "explicacao": (
            "Em 1790, a Assembleia revolucionária pediu à Academia de Ciências medidas novas, baseadas na "
            "natureza. A comissão descartou o pêndulo que bate o segundo, porque o comprimento dele muda com a "
            "gravidade de cada lugar, e decidiu que o metro seria a décima milionésima parte da distância entre o "
            "Polo Norte e o Equador, medida ao longo do meridiano de Paris. Os astrônomos Jean-Baptiste Delambre "
            "e Pierre Méchain mediram então o arco entre Dunquerque e Barcelona. Méchain, que começou o trecho "
            "sul em 1791, sofreu com a revolução: foi preso sob suspeita de que seus instrumentos fossem armas, "
            "ficou retido em Barcelona quando estourou a guerra entre França e Espanha e teve os bens em Paris "
            "confiscados durante o Terror. Ao conferir a latitude pelas estrelas, encontrou resultados anômalos e "
            "passou a duvidar da própria precisão. A análise dos números dele mostra que ele manteve as "
            "discrepâncias sempre minúsculas, o que fez suas medições parecerem mais precisas do que seria "
            "razoável com equipamento do século XVIII. As dúvidas o levaram de volta à Espanha em 1804, onde "
            "morreu de febre amarela. Hoje se sabe que o metro ficou 0,197 milímetro mais curto do que a definição "
            "original pretendia, sobretudo por causa de um desvio da vertical no extremo sul da medição. O suposto "
            "erro de Méchain não afetou o valor final."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Pierre_Méchain",
                "the determination of the southern part of the meridian arc of the Earth's surface between Dunkirk and Barcelona beginning in 1791. "
                "This measurement would become the basis of the metric system's unit of length, the meter. "
                "He encountered numerous difficulties on this project, largely stemming from the effects of the French Revolution. "
                "He was arrested after it was suspected his instruments were weapons, he was interned in Barcelona after war broke out between France and Spain, and his property in Paris was confiscated during The Terror. [...] "
                "Méchain was uncertain of the precision of his measurements owing to anomalous results in verifying his latitude by astronomical observation. [...] "
                "Méchain consistently kept the discrepancy very tiny, essentially forcing his individual reported measurements to appear more precise and consistent than would be reasonably expected of a survey involving more than a hundred measurements of mostly rough country using 18th-century equipment; "
                "Méchain's putative error did not affect the final value of the length of the metre nor the measurement of the meridian. [...] "
                "Continuing doubts about his measurements of the Dunkirk-Barcelona arc led him to return to that work. "
                "This took him back to Spain in 1804, where he caught yellow fever and died",
                nome="Pierre Méchain"),
            wiki("History_of_the_metre",
                "In 1790, during the French Revolution, the National Convention tasked the French Academy of Sciences with reforming the units of measurement. "
                "The Academy formed a commission, which rejected using the pendulum as a unit of length and decided that the new measure should be equal to one ten-millionth of the distance from the North Pole to the Equator [...] "
                "This was to be measured along the meridian passing through the centre of Paris Observatory. [...] "
                "this was rejected as it had been discovered that this length varied from place to place with local gravity. [...] "
                "Following the arc measurement of Delambre and Méchain [...] "
                "we now know that the metre is 0.197 millimetres shorter than it should be according to its original proposed definition, mainly due to not taking into account a vertical deflection in the southern end of the arc measurement of Delambre and Méchain.",
                nome="History of the metre"),
        ],
    },
    # 7 Lavoisier e a água no tabaco
    {
        "temas_secundarios": ["elementos_quimicos", "leis_julgamentos"],
        "tipos_espanto": ["historia_humana", "mito_desmentido"],
        "gancho": "Lavoisier, o químico que batizou o oxigênio, recomendou à empresa de impostos de que era sócio pôr 6,3% de água no tabaco. Na Revolução, uma das acusações que o levaram à guilhotina foi molhar o tabaco.",
        "explicacao": (
            "Antoine Lavoisier financiava sua ciência com a Ferme générale, uma companhia que adiantava ao rei a "
            "receita prevista dos impostos e, em troca, ganhava o direito de cobrá-los. Ela detinha o monopólio do "
            "tabaco na França e era uma das instituições mais odiadas do Antigo Regime. Lavoisier estudou as "
            "fraudes dos vendedores, que misturavam cinza e água ao tabaco, e notou que muita água fazia o fumo "
            "fermentar e cheirar mal, mas um pouco melhorava o produto. Por recomendação dele, as fábricas "
            "passaram a acrescentar 6,3% de água, e, para compensar, a companhia entregava 17 onças de tabaco "
            "cobrando 16. Veio a Revolução. Em 1793, foi ordenada a prisão de todos os antigos cobradores, "
            "acusados de fraudar o Estado e de pôr água no tabaco antes de vendê-lo. Lavoisier redigiu a defesa, "
            "mas o tribunal via na condenação um jeito de confiscar fortunas para o Estado. Ele foi guilhotinado "
            "em 8 de maio de 1794, aos 50 anos, com outros 27 réus. A frase atribuída ao juiz, \"a República não "
            "precisa de sábios\", vem de uma lenda popular. Um ano e meio depois, o governo francês o inocentou, e "
            "os bens foram entregues à viúva com um bilhete: \"À viúva de Lavoisier, que foi falsamente "
            "condenado\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Antoine_Lavoisier",
            "He named oxygen (1778) [...] "
            "The Ferme générale was one of the most hated components of the Ancien Régime [...] "
            "All of these political and economic activities enabled him to fund his scientific research. [...] "
            "a tax farming financial company which advanced the estimated tax revenue to the royal government in return for the right to collect the taxes. [...] "
            "The Farmers General held a monopoly of the production, import and sale of tobacco in France [...] "
            "adulterated, most commonly with ash and water. [...] "
            "Lavoisier also found that while adding a lot of water to bulk the tobacco up would cause it to ferment and smell bad, the addition of a very small amount improved the product. "
            "Thereafter the factories of the Farmers General added, as he recommended, a consistent 6.3% of water by volume to the tobacco they processed. "
            "To allow for this addition, the Farmers General delivered to retailers seventeen ounces of tobacco while only charging for sixteen. [...] "
            "On 24 November 1793, the arrest of all the former tax farmers was ordered. "
            "Lavoisier and the other Farmers General faced nine accusations of defrauding the state of money owed to it, and of adding water to tobacco before selling it. "
            "Lavoisier drafted their defense [...] "
            "The court, however, was inclined to believe that by condemning them and seizing the goods of the Farmers General, it would recover huge sums for the state. "
            "Lavoisier was convicted and guillotined on 8 May 1794 in Paris, at the age of 50, along with his 27 co-defendants. "
            "According to popular legend, the appeal to spare his life, in order that he could continue his experiments, was cut short by the judge, Coffinhal: "
            "\"La République n'a pas besoin de savants ni de chimistes; le cours de la justice ne peut être suspendu.\" [...] "
            "A year and a half after his execution, Lavoisier was completely exonerated by the French government. "
            "During the White Terror, his belongings were delivered to his widow. "
            "A brief note was included, reading \"To the widow of Lavoisier, who was falsely convicted\".",
            nome="Antoine Lavoisier")],
    },
    # 8 Guillotin era contra a pena de morte; última guilhotinada em 1977
    {
        "temas_secundarios": ["leis_julgamentos", "historia_medicina"],
        "tipos_espanto": ["contraintuitivo", "historia_humana", "mito_desmentido"],
        "gancho": "O médico que deu nome à guilhotina era contra a pena de morte e só queria execuções menos cruéis. A máquina, estreada em 1792, decapitou alguém na França pela última vez em 1977.",
        "explicacao": (
            "Joseph-Ignace Guillotin não inventou o aparelho: o protótipo foi obra de outro médico, Antoine Louis. "
            "Deputado em 1789, Guillotin tentou abolir a pena de morte e não conseguiu. Na época, a decapitação "
            "com machado ou espada era privilégio dos nobres e nem sempre matava na hora, enquanto os plebeus "
            "eram enforcados, queimados ou mortos na roda. Ele propôs então que todo condenado, de qualquer "
            "classe, fosse decapitado por um mecanismo simples, esperando que uma morte rápida fosse o primeiro "
            "passo para o fim das execuções e atraísse multidões menores. Uma frase atribuída a ele, de que a "
            "máquina cortaria a cabeça \"num piscar de olhos\" sem que a pessoa sentisse nada, virou piada e "
            "canção cômica, e o nome dele grudou no aparelho. Guillotin lamentou isso pelo resto da vida. A "
            "família pediu ao governo que rebatizasse a máquina e, diante da recusa, trocou o próprio sobrenome. "
            "Ao contrário do que muitos dizem, ele não morreu guilhotinado: morreu em casa, de causas naturais, "
            "em 1814. Quem passou pela lâmina foi um médico de Lyon com o mesmo sobrenome. A guilhotina seguiu em "
            "uso por quase dois séculos. A última execução foi a de Hamida Djandoubi, em Marselha, em 10 de "
            "setembro de 1977, também a última decapitação legal do mundo ocidental. A França aboliu a pena de "
            "morte em 1981."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Joseph-Ignace_Guillotin",
                "Although he did not invent the guillotine and opposed the death penalty, his name became an eponym for it. "
                "The actual inventor of the prototype was a French physician, Antoine Louis. [...] "
                "On 2 May 1789, he became one of 10 Paris deputies in the Estates-General of 1789 [...] "
                "His experiences as a doctor had led him to oppose capital punishment: at first, he attempted to abolish it, but was unsuccessful. "
                "At that time, beheading in France was typically by axe or sword, which did not always cause immediate death. "
                "Additionally, beheading was reserved for the nobility, while commoners were typically hanged [...] "
                "Other methods included burning at the stake, the breaking wheel [...] "
                "All punishments for the same class of crime shall be the same, regardless of the criminal [...] "
                "Guillotin was opposed to the death penalty, and hoped that a more humane and less painful method of execution would be the first step towards total abolition. "
                "He also hoped that, as the decapitation machine would kill quickly without prolonged suffering, this would reduce the size and enthusiasm of crowds that often witnessed executions. [...] "
                "He was quoted (or possibly misquoted) as saying, \"Now, with my machine, I cut off your head in the twinkling of an eye, and you never feel it!\" "
                "The statement quickly became a popular joke, and a few days after the debate a comic song about Guillotin and \"his\" machine circulated, forever tying his name to it [...] "
                "the first executions using it took place on 25 April 1792. [...] "
                "for the remainder of his life, he deeply regretted that the machine was named after him. [...] "
                "The association with the guillotine so embarrassed Guillotin's family that they petitioned the French government to rename it; when the government refused, they instead changed their own family name. "
                "By coincidence, another person named Guillotin was indeed executed by the guillotine – he was J.M.V. Guillotin, a doctor of Lyon. "
                "This coincidence may have contributed to erroneous statements that J-I Guillotin was put to death on the machine that bears his name; "
                "however, in reality, Guillotin died at home in Paris in 1814 of natural causes",
                nome="Joseph-Ignace Guillotin"),
            wiki("Hamida_Djandoubi",
                "Djandoubi was the last person to be executed in France before the abolition of capital punishment in 1981, and the last person to be lawfully executed by beheading anywhere in the Western world. [...] "
                "On 10 September 1977 [...] "
                "Djandoubi was executed by guillotine at Baumettes Prison in Marseille.",
                nome="Hamida Djandoubi"),
        ],
    },
    # 9 a indenização que o Haiti pagou à França pela própria liberdade
    {
        "temas_secundarios": ["imperios_coloniais", "dinheiro"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "Para reconhecer o Haiti, a França exigiu, com navios de guerra, 150 milhões de francos de indenização pelos bens perdidos, incluindo os escravizados. Segundo o New York Times, a conta só se encerrou em 1947.",
        "explicacao": (
            "São Domingos, hoje Haiti, era a colônia europeia mais lucrativa do mundo. Seu açúcar respondia por "
            "40% do mercado do Atlântico, e em 1790 viviam ali 425 mil escravizados. Em 1804, depois de uma "
            "grande revolta de escravizados, o país declarou independência. Veio o isolamento: nenhum Estado "
            "aceitava comerciar com ele, e os EUA, com medo de que o exemplo inspirasse seus próprios "
            "escravizados, só reconheceram o Haiti em 1862. Em 1825, navios de guerra franceses levaram a "
            "exigência: 150 milhões de francos, em cinco parcelas anuais de 30 milhões, para compensar os antigos "
            "proprietários pelas perdas da revolução, contando como propriedade as pessoas escravizadas. Em "
            "troca, a França reconheceria o novo país. O Haiti precisou de um empréstimo para pagar a primeira "
            "parcela, e em 1838 a França reduziu o restante para 60 milhões. Para quitar uma dívida, o país "
            "tomava outra, e uma análise publicada pelo New York Times em 2022 concluiu que o último pagamento "
            "ligado a esses empréstimos só foi feito em 1947. O jornal estimou que o Haiti pagou de fato cerca "
            "de 112 milhões de francos de indenização, algo como 560 milhões de dólares de 2022. Em 2016, o "
            "Parlamento francês revogou a ordem de 1825, mas nenhuma reparação foi oferecida."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Haiti_indemnity_controversy",
            "involves an 1825 agreement between Haiti and France that included France demanding an indemnity of 150 million francs in five annual payments of 30 million to be paid by Haiti in claims over property, including Haitian slaves, that was lost through the Haitian Revolution in return for diplomatic recognition. "
            "Haiti was forced to take a loan for the first 30 million, and in 1838 France agreed to reduce the remaining debt to 60 million to be paid over 30 years, with the final payment paid in 1883. "
            "However, according to a 2022 The New York Times analysis, because of other loans taken to pay off this loan, the final payment to debtors was actually made in 1947. "
            "They approximated that 112 million francs was actually paid in indemnity, which is equivalent to $560 million in 2022 after adjusting for inflation. "
            "Restoration France's demand of payments in exchange for recognizing Haiti's independence was delivered to the country by several French warships in 1825 [...] "
            "In 2016, the Parliament of France repealed the 1825 ordinance of Charles X, though no reparations have been offered by France. [...] "
            "Saint-Domingue, now Haiti, was the most profitable and productive European colony in the world going into the 1800s. [...] "
            "The Saint-Domingue population reached 520,000 in 1790, and of those 425,000 were slaves. [...] "
            "while its sugar represented forty percent of the Atlantic market. [...] "
            "with Haitians gaining their independence from France in 1804 [...] "
            "After the declaration of independence, no state was willing to trade with Haiti [...] "
            "The first American ambassador to Haiti – and with it recognition of Haiti's independence – only came in 1862 [...] "
            "Thomas Jefferson, United States President, feared a slave revolt would spread to the United States",
            nome="Haiti indemnity controversy")],
    },
    # 10 os poloneses que mudaram de lado no Haiti
    {
        "temas_secundarios": ["imperios_coloniais", "doencas_infecciosas"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "Napoleão mandou cerca de 5.200 soldados poloneses para esmagar a revolução no Haiti. Centenas mudaram de lado, e o novo país lhes deu cidadania. Seus descendentes ainda vivem numa vila haitiana.",
        "explicacao": (
            "Em 1802, Napoleão enviou a São Domingos uma meia-brigada polonesa de uns 5.200 homens para reforçar "
            "as tropas francesas que tentavam reconquistar a colônia rebelde. Os poloneses talvez esperassem, em "
            "troca, a ajuda da França para recuperar a independência da Polônia, repartida entre Prússia, Rússia "
            "e Áustria; a alguns, disseram que iam enfrentar uma revolta de presos. Mal chegaram, foram jogados "
            "contra os rebeldes negros. Cerca de 4.000 deles morreram, e nas duas tropas, francesa e polonesa, a "
            "febre amarela matou mais que as batalhas. Os sobreviventes passaram a admirar os adversários, em "
            "quem enxergavam a mesma luta por liberdade que queriam para o próprio país, e uns 500 acabaram "
            "passando para o lado dos rebeldes. Depois da independência, Jean-Jacques Dessalines, o primeiro "
            "governante do Haiti, poupou os poloneses do massacre que ordenou contra a maior parte dos brancos "
            "franceses. Deu-lhes cidadania plena e os classificou como \"negros\", a categoria que formava a nova "
            "classe dominante, e chegou a chamá-los de \"os negros brancos da Europa\". Calcula-se que 400 a 500 "
            "se fixaram no país. A vila de Cazale, a uns 30 km de Porto Príncipe, é o principal núcleo dos "
            "descendentes, muitos deles identificáveis por olhos claros e cabelos mais lisos."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Polish_Haitians",
                "Cazale, a small village in the hills about 30 kilometres (19 mi) away from Port-au-Prince, is considered the main center of population of the ethnic Polish community in Haiti [...] "
                "Some 400 to 500 of these Poles are believed to have settled in Haiti after the war. [...] "
                "In May 1802, Napoleon dispatched the 3rd Polish Half-Brigade of around 5,200 men to join French forces in Saint-Domingue [...] "
                "The Poles may have been hoping to receive French support in restoring Poland's independence from its occupiers—Prussia (later Germany), Russia, and Austria [...] "
                "Some were told that there was a revolt of prisoners in Saint-Domingue. [...] "
                "they were quickly thrown into battle against Black rebels. "
                "Both French and Polish soldiers in the colony experienced high mortality rates, with more troops dying of yellow fever than from being killed in action. "
                "Approximately 4,000 of the 5,200 Polish soldiers sent to Saint-Domingue died. "
                "Surviving Polish soldiers admired their opponents, and some 500 or so of them would eventually turn on the French army and joined the rebels. [...] "
                "many would come to believe that the former slaves were fighting for the same ideals of freedom and independence to which they, the Poles, aspired. [...] "
                "After Haiti gained its independence, Dessalines recognized the Poles and spared them when he ordered the massacre of the establishment of slavery, which consisted of most French whites [...] "
                "He granted the Poles classification as Noir (black), who constituted the new ruling class, and in the constitution granted them full Haitian citizenship. [...] "
                "Haiti's first head of state Jean-Jacques Dessalines would join Boisrond-Tonnerre in calling the Polish people \"the White Negroes of Europe\" [...] "
                "To this day, Polish Haitians are mixed race and often identified by such European features as blonde or lighter and straighter hair, light eyes",
                nome="Polish Haitians"),
            wiki("Cazale",
                "It is the main population center of the Polish community in Haiti, called La Pologne (Poland). [...] "
                "The village is populated by descendants of Polish soldiers sent by Napoleon in 1802.",
                nome="Cazale"),
        ],
    },
    # 11 o 8 de março nasceu de uma revolução
    {
        "temas_secundarios": ["calendarios", "costumes_rituais"],
        "tipos_espanto": ["origem_inesperada", "mito_desmentido"],
        "gancho": "O 8 de março é o Dia da Mulher por causa de uma revolução: nesse dia, em 1917, operárias têxteis de Petrogrado iniciaram os protestos que derrubaram o czar. A greve de Nova York em 1857 é mito.",
        "explicacao": (
            "A ideia de um dia das mulheres nasceu entre socialistas. O primeiro \"Dia da Mulher\" foi feito em "
            "Nova York em 1909, e, em 1910, uma conferência em Copenhague aprovou uma data anual, mas sem dia "
            "fixo. Na Rússia de 1917, que ainda usava o calendário juliano, a data caiu em 23 de fevereiro, que no "
            "calendário gregoriano era 8 de março. Naquele dia, operárias têxteis de Petrogrado saíram em protesto "
            "por \"pão e paz\", contra a guerra, a falta de comida e o czarismo, e o movimento tomou a cidade "
            "inteira. Começava a Revolução de Fevereiro. Sete dias depois, o czar Nicolau II abdicou, e o governo "
            "provisório deu às mulheres o direito de voto. Trótski escreveu depois que ninguém imaginava que aquele "
            "Dia da Mulher fosse inaugurar a revolução: as operárias largaram o trabalho contra as ordens e "
            "pediram apoio à greve. Em 1921, numa conferência internacional de mulheres comunistas, uma delegada "
            "russa propôs fixar a data em 8 de março, em memória das manifestações de Petrogrado, e a proposta "
            "passou por unanimidade. A data se espalhou pelos países comunistas e, em 1977, passou a ser "
            "promovida pela ONU. Já a versão de que ela lembra um protesto de costureiras em Nova York em 8 de "
            "março de 1857 é descrita por pesquisadores como mito."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("International_Women's_Day",
                "The holiday was promoted by the United Nations in 1977. [...] "
                "The earliest reported Women's Day event, called \"Woman's Day\", was held on 28 February 1909, in New York City. [...] "
                "There have been claims that the day was commemorating a protest by women garment workers in New York on 8 March 1857, but researchers have described this as a myth. [...] "
                "proposed the establishment of an annual \"Women's Day\", although no date was specified. [...] "
                "On 8 March 1917, in Petrograd (23 February in the Julian calendar), women textile workers began a demonstration that eventually engulfed the whole city, demanding \"Bread and Peace\"—an end to World War I, to food shortages, and to Tsarism. "
                "This marked the beginning of the February Revolution [...] "
                "But we did not imagine that this 'Women's Day' would inaugurate the revolution. "
                "Revolutionary actions were foreseen but without a date. "
                "But in the morning, despite the orders to the contrary, textile workers left their work in several factories and sent delegates to ask for the support of the strike [...] "
                "Seven days later, Tsar Nicholas II abdicated, and the provisional Government granted women the right to vote. [...] "
                "the third world congress of Communist International in 1921 [...] "
                "The date of International Women's Day was also first fixed as March 8 at this Second International Conference of Communist Women. [...] "
                "Nikolaeva, a representative of the RSFSR, proposed to set the current date (March 8) in memory of the participation of Petrograd women in the demonstrations of March 8, 1917 that led to the overthrow of the monarchy, which was approved unanimously. "
                "After its adoption in Soviet Russia, International Women's Day was predominantly celebrated in communist countries [...] "
                "In August 1910, an International Socialist Women's Conference was organized ahead of the general meeting of the Socialist Second International in Copenhagen, Denmark.",
                nome="International Women's Day"),
        ],
    },
    # 12 a "tomada" do Palácio de Inverno que veio do cinema
    {
        "temas_secundarios": ["cinema_fotografia"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "As cenas clássicas da tomada do Palácio de Inverno, em 1917, com combates ferozes, vêm de uma encenação de 1920 e do filme de Eisenstein. Na vida real, o palácio caiu quase sem resistência.",
        "explicacao": (
            "Na noite de 25 de outubro de 1917 pelo calendário então usado na Rússia, multidões de insurgentes "
            "cercaram o Palácio de Inverno, em Petrogrado, sede do Governo Provisório, e muitos já se infiltravam "
            "no prédio. Às 9 e 45 da noite, o cruzador Aurora disparou um tiro de festim. Os primeiros "
            "revolucionários entraram às 10 e 25, a entrada em massa veio três horas depois, e às 2 e 10 da "
            "madrugada os bolcheviques controlavam o palácio. Os cadetes e as 140 voluntárias do Batalhão Feminino "
            "se renderam sem resistir. Mais tarde, historiadores e autoridades soviéticas passaram a contar o "
            "episódio em tom heroico. Em 1920, uma grande encenação chamada \"A Tomada do Palácio de Inverno\" foi "
            "assistida por 100 mil pessoas e virou modelo para os filmes oficiais. O mais famoso, \"Outubro\", de "
            "Serguei Eisenstein, lançado em 1928, se inspirou mais nessa encenação do que no evento real, bem "
            "menos fotogênico. Como não havia filmagens nem fotos do episódio de verdade, as cenas de Eisenstein "
            "acabaram usadas por historiadores e cineastas como se fossem o registro histórico. Segundo as "
            "memórias de Alexander Gorodnitsky, que reproduz um relato do pai, o filme quase não tinha atores "
            "profissionais: Lênin foi interpretado por um operário de uma fábrica de cimento."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Storming_of_the_Winter_Palace",
                "It began through an insurrection in Petrograd (now Saint Petersburg) on 7 November 1917 [O.S. 25 October]. [...] "
                "As the night progressed, crowds of insurgents surrounded the palace, and many infiltrated it. "
                "At 9:45 p.m, the cruiser Aurora fired a blank shot from the harbor. "
                "Some of the revolutionaries entered the palace at 10:25 p.m. and there was a mass entry 3 hours later. "
                "By 2:10 a.m. on 26 October, Bolshevik forces had gained control. "
                "The cadets and the 140 volunteers of the Women's Battalion surrendered rather than resist [...] "
                "While the seizure of the Winter Palace happened almost without resistance, Soviet historians and officials later tended to depict the event in dramatic and heroic terms. "
                "The historical reenactment titled The Storming of the Winter Palace was staged in 1920. "
                "This reenactment, watched by 100,000 spectators, provided the model for official films made later, which showed fierce fighting during the storming of the Winter Palace, although, in reality, the Bolshevik insurgents had faced little opposition.",
                nome="Storming of the Winter Palace"),
            wiki("October:_Ten_Days_That_Shook_the_World",
                "The scene of the storming was based more on The Storming of the Winter Palace (1920) [...] "
                "than the original occasion, which was far less photogenic. "
                "This scene became the legitimate, historical depiction of the storming of the Winter Palace owing to the lack of print or film documenting the actual event, which led historians and filmmakers to use Eisenstein's recreation. [...] "
                "According to the memoirs of Alexander Gorodnitsky, his father Moisei described that \"in the film October there were almost no professional actors. "
                "Lenin, for example was played by Nikandrov, a cement factory worker [...] "
                "1928",
                nome="October: Ten Days That Shook the World"),
        ],
    },
    # 13 a revolução chinesa de 1911 começou com uma bomba acidental
    {
        "temas_secundarios": ["personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "A revolução que derrubou o último imperador da China começou por acidente: uma bomba explodiu sem querer na oficina dos rebeldes. E Sun Yat-sen, o futuro presidente, estava nos EUA e soube pelo jornal.",
        "explicacao": (
            "Em 1911, dois grupos revolucionários de Wuhan preparavam um levante contra a dinastia Qing. Ele foi "
            "marcado para 6 de outubro, na Festa do Meio do Outono, e depois adiado por falta de preparo. Em 9 de "
            "outubro, enquanto o revolucionário Sun Wu supervisionava a fabricação de explosivos na concessão "
            "russa de Hankou, um dos artefatos explodiu e o feriu gravemente. No hospital, descobriram quem ele "
            "era e avisaram as autoridades. Com a identidade dos conspiradores revelada e a prisão iminente, os "
            "rebeldes infiltrados no Novo Exército decidiram agir na hora. Na noite de 10 de outubro, eles se "
            "amotinaram em Wuchang e tomaram a residência do vice-rei. O levante se espalhou, e até o fim de "
            "dezembro 18 províncias do sul e do centro tinham rompido com o governo Qing. Sun Yat-sen, que não "
            "deve ser confundido com Sun Wu, estava nos Estados Unidos pedindo dinheiro a chineses emigrados. "
            "Recebeu um telegrama de um companheiro, mas não conseguiu decifrá-lo, e soube do levante pelos "
            "jornais. Voltou à China, foi eleito presidente provisório e, em 1º de janeiro de 1912, foi fundada a "
            "República da China. Terminavam ali mais de 2.000 anos de governo imperial."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Wuchang_uprising",
                "These groups, led by Jiang Yiwu and Sun Wu respectively, worked closely together [...] "
                "Beginning in September 1911, these two groups began negotiating with the Tongmenghui [...] "
                "The date was originally set for 6 October, on the Mid-Autumn festival. "
                "The date was later postponed, due to inadequate preparations. "
                "On 9 October, while Sun Wu was supervising the making of explosive devices in the Russian concession in Hankou, one of the devices exploded unexpectedly, inflicting serious injuries on Sun. "
                "When he was hospitalized, the hospital staff discovered his identity and alerted the Qing authorities. [...] "
                "With their identities revealed, the revolutionaries in the New Army stationed in Wuchang were facing imminent arrest by the Qing authorities. "
                "The decision was made by Jiang Yiwu of the Wenxueshe to immediately launch the uprising [...] "
                "On the evening of 10 October, Wu Zhaolin as provisional commander led the revolutionary elements of the New Army and staged a mutiny against the Qing garrison in Huguang, capturing the residence of the Viceroy [...] "
                "Sun Yat-sen was traveling in the United States speaking to overseas Chinese to appeal for financial support when the uprising took place. "
                "Although Sun received a telegram from Huang Xing, he was unable to decipher it, and found out about the uprising the next morning in the newspaper. [...] "
                "eighteen provinces in Southern and Central China agreed to secede from the Qing government by the end of December 1911. [...] "
                "Sun returned to China to participate in the provisional presidential election and was elected. "
                "Representatives from the seceding provinces met on 1 January 1912, and declared the founding of the Republic of China",
                nome="Wuchang uprising"),
            wiki("Sun_Yat-sen",
                "to overthrow the last emperor, Puyi. "
                "That put Huang in charge of the revolution that ended over 2000 years of imperial rule in China.",
                nome="Sun Yat-sen"),
        ],
    },
    # 14 a senha da Revolução dos Cravos foi uma canção do Eurovisão
    {
        "temas_secundarios": ["historia_musica"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "A senha para começar a revolução que derrubou a ditadura em Portugal, em 1974, foi tocar no rádio a canção do país no Festival Eurovisão. E os cravos eram de um restaurante que festejava um ano de vida.",
        "explicacao": (
            "Os militares que planejavam derrubar o Estado Novo combinaram dois sinais secretos pelo rádio. Às "
            "22h55 de 24 de abril de 1974, um locutor anunciou a hora e tocou \"E Depois do Adeus\", de Paulo de "
            "Carvalho, que representara Portugal no Eurovisão daquele ano: era o aviso para os capitães "
            "começarem. Às 0h20 do dia 25, a Rádio Renascença tocou \"Grândola, Vila Morena\", de Zeca Afonso, "
            "cantor com muitas músicas proibidas nas rádios, e as tropas partiram para tomar os pontos "
            "estratégicos. As letras eram inofensivas, porque a censura não deixaria passar nada mais "
            "inflamado; o recado estava no simples fato de tocá-las. De manhã, em Lisboa, a faxineira Celeste "
            "Caeiro chegou ao restaurante onde trabalhava, que completava um ano e ia distribuir cravos aos "
            "clientes. Com o golpe, a festa foi cancelada e os funcionários levaram as flores para casa. No "
            "centro, um soldado num veículo militar pediu um cigarro a ela. Celeste não fumava e lhe deu um "
            "cravo, que ele enfiou no cano da arma. Ela distribuiu os outros aos soldados, floristas copiaram a "
            "ideia, e as fotos correram o mundo e deram nome à Revolução dos Cravos. O golpe quase não teve "
            "combates, mas houve mortes: a polícia política atirou contra a multidão e matou quatro civis. O "
            "chefe do governo deposto, Marcelo Caetano, foi mandado para o exílio no Brasil, onde viveu até "
            "morrer."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Carnation_Revolution",
                "was a military coup in Portugal by officers that on 25 April 1974 overthrew Marcelo Caetano and the Estado Novo regime [...] "
                "the disc jockey at Emissores Associados de Lisboa gave the time signal Falta cinco minutos às vinte e três at 22:55 on 24 April before turntabling Paulo de Carvalho's \"E Depois do Adeus\" (Portugal's entry in the 1974 Eurovision Song Contest). "
                "This alerted rebel captains and soldiers to begin the coup. "
                "The second signal came at 00:20 on 25 April, when Rádio Renascença broadcast \"Grândola, Vila Morena\" (a song by Zeca Afonso, an influential political folk musician and singer, many of whose songs were banned from Portuguese radio at the time). "
                "The MFA gave the signals to take over strategic points of power in the country. "
                "The content of the songs was largely uncontroversial—censorship would have prevented more inflammatory songs—but their broadcasting was a signal, not a direct call to arms. [...] "
                "GDS authorities started shooting warning shots towards the crowd outside the building, killing four civilians and injuring 45. [...] "
                "Caetano and Tomás were sent to Brazil; Caetano spent the rest of his life there",
                nome="Carnation Revolution"),
            wiki("Celeste_Caeiro",
                "In 1974 Caeiro was working in a self-service restaurant in Lisbon called \"Sir\" located at Franjinhas Building on Rua Braamcamp as a cleaner. "
                "The restaurant was opened on 25 April 1973 and for its first anniversary, on 25 April 1974, the owners planned to give out red and white carnations to all its customers [...] "
                "The celebration had to be cancelled because of the coup, so the employees were asked to take the carnations home. [...] "
                "She approached two soldiers mounted on a Bravia Chaimite truck to ask what was going on [...] "
                "The same man asked her for a cigarette, but as Caeiro did not smoke [...] "
                "she gave him a carnation from the bouquet she was carrying and he put it in the barrel of his gun. [...] "
                "she gave the rest of the carnations to the soldiers involved, and they placed the flowers in the muzzle of their guns. "
                "The idea was copied and flower sellers donated more flowers to the mutinous soldiers. "
                "The pictures of the soldiers with carnations in their guns appeared on front pages all over the world and the coup became known globally as the Carnation Revolution",
                nome="Celeste Caeiro"),
        ],
    },
    # 15 a Corrente Báltica: 2 milhões de mãos dadas
    {
        "temas_secundarios": ["guerra_fria", "fronteiras_paises"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "Em 1989, cerca de 2 milhões de pessoas deram as mãos numa corrente humana de 675 km, atravessando Estônia, Letônia e Lituânia, contra a ocupação soviética. Os três países somavam uns 8 milhões de habitantes.",
        "explicacao": (
            "A Corrente Báltica aconteceu em 23 de agosto de 1989, nos 50 anos do Pacto Molotov-Ribbentrop, o "
            "acordo entre a União Soviética e a Alemanha nazista que repartiu o Leste Europeu em esferas de "
            "influência e abriu caminho para a ocupação soviética dos países bálticos em 1940. Moscou negava a "
            "existência dos protocolos secretos do pacto e só os admitiu como autênticos dias antes do protesto. "
            "Para que a corrente não tivesse buracos, os organizadores mapearam o percurso e designaram trechos "
            "específicos a cada cidade e vila. Houve ônibus de graça para quem não tinha transporte, e no dia "
            "programas especiais de rádio ajudaram a coordenar tudo. Como a data caiu numa quarta-feira, alguns "
            "patrões não liberaram os funcionários, enquanto outros pagaram os ônibus; a Estônia decretou "
            "feriado. Os líderes da Alemanha Oriental e da Romênia chegaram a oferecer ajuda militar caso os "
            "soviéticos decidissem dispersar a manifestação à força. As autoridades soviéticas reagiram com "
            "discursos duros, mas sem medidas concretas. Sete meses depois, a Lituânia se tornou a primeira "
            "república soviética a declarar independência."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Baltic_Way",
            "was a peaceful political demonstration that occurred on 23 August 1989. "
            "Approximately two million people joined their hands to form a human chain spanning 675 kilometres (419 mi) across the three Baltic states of Estonia, Latvia, and Lithuania, with a combined population of around eight million citizens [...] "
            "It marked the 50th anniversary of the Molotov–Ribbentrop Pact, in which Poland, Finland, Estonia, Latvia, Lithuania, and Romania were (as \"spheres of influence\") divided between the Soviet Union and Nazi Germany. "
            "The Soviet-Nazi pact led to the outbreak of World War II in September 1939 and the Soviet invasion and occupation of the Baltic countries in June 1940. [...] "
            "The Soviet authorities responded to the event with intense rhetoric, but failed to take any constructive actions [...] "
            "Seven months after the protest, Lithuania became the first Soviet republic to declare independence. [...] "
            "The Soviet Union denied the existence of the secret protocols to the Molotov–Ribbentrop Pact [...] "
            "East Germany's head of state, Erich Honecker, and Romania's dictator, Nicolae Ceaușescu, offered to provide military assistance to the Soviet Union in the case the Soviets decided to use force and break up the demonstration. [...] "
            "On 18 August, Pravda published an extensive interview with Alexander Nikolaevich Yakovlev [...] "
            "Yakovlev admitted that the secret protocols were genuine. [...] "
            "The organisers mapped out the chain, designating specific locations to specific cities and towns to ensure that the chain would remain uninterrupted. "
            "Additionally, free bus rides were provided for those who did not have other transportation. [...] "
            "Some employers did not allow workers to take the day off from work (23 August fell on a Wednesday), while others sponsored the bus rides. "
            "On the day of the event, special radio broadcasts helped to coordinate the effort. "
            "Estonia declared a public holiday.",
            nome="Baltic Way")],
    },
]
