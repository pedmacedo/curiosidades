LOTE = "2026-11-19-plantas-01"
AREA = "biologia"
TEMA = "plantas"
W = "https://en.wikipedia.org/wiki/"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


def resumo(pmid, titulo, trecho):
    """Resumo de artigo pelo Europe PMC (busca por PMID, resultType=core)."""
    url = EPMC + "search?query=EXT_ID:" + pmid + "%20AND%20SRC:MED&resultType=core&format=json"
    return {"url": url, "titulo": titulo, "idioma": "en", "trecho": trecho}


def artigo(pmcid, titulo, trecho):
    """Texto completo de artigo aberto pelo Europe PMC."""
    return {"url": EPMC + pmcid + "/fullTextXML", "titulo": titulo, "idioma": "en", "trecho": trecho}


CANDIDATOS = [
    # 1 o salgueiro de Van Helmont e o gás que ele mesmo batizou
    {
        "temas_secundarios": ["revolucao_cientifica", "quimica_cotidiano"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "No século XVII, Van Helmont cultivou um salgueiro num vaso por cinco anos: a árvore ganhou 74 kg e a terra quase não perdeu peso. Ele concluiu que tudo vinha da água, e acertou só em parte.",
        "explicacao": (
            "Jan Baptist van Helmont, químico e médico de Bruxelas que viveu de 1580 a 1644, fez um dos primeiros "
            "estudos quantitativos sobre como as plantas crescem. Ele pesou a terra, a árvore e a água que "
            "acrescentava ao vaso. Passados cinco anos, o salgueiro estava cerca de 74 kg mais pesado, e o solo "
            "tinha perdido apenas 57 gramas. Como a água era a única coisa que ele punha no vaso, deduziu que todo "
            "o ganho viera dela. Hoje se sabe que boa parte dessa massa vem também do gás carbônico do ar, que a "
            "planta captura na fotossíntese. A ironia é que o próprio Van Helmont estudou esse gás: percebeu que o "
            "\"gas sylvestre\" liberado pelo carvão em brasa era o mesmo produzido pelo mosto em fermentação. Foi "
            "ele também quem levou a palavra \"gás\" para o vocabulário da ciência, inspirada no grego \"caos\". O "
            "experimento só saiu depois da morte dele, num livro de 1648, e talvez tenha se inspirado em testes "
            "parecidos de Santorio. Mesmo com a conclusão errada, apontou para uma ideia central: o grosso "
            "do corpo de uma planta não sai do solo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Jan_Baptist_van_Helmont",
                "12 January 1580 – 30 December 1644) was a chemist, physiologist, and physician from Brussels. [...] "
                "Van Helmont is remembered today largely for his 5-year willow tree experiment, his introduction of the word \"gas\" (from the Greek word chaos) into the vocabulary of science [...] "
                "Helmont's experiment on a willow tree has been considered among the earliest quantitative studies on plant nutrition and growth and as a milestone in the history of biology. "
                "The experiment was only published posthumously in Ortus Medicinae (1648) and may have been inspired by similar experiments by Santorio, published in Ars de statica medicina (1614). "
                "Helmont grew a willow tree and measured the amount of soil, the weight of the tree and the water he added. "
                "After five years the plant had gained about 164 lbs (74 kg). "
                "Since the amount of soil was nearly the same as it had been when he started his experiment (it lost only 57 grams), he deduced that the tree's weight gain had come entirely from water. [...] "
                "He perceived that his \"gas sylvestre\" (carbon dioxide) given off by burning charcoal, was the same as that produced by fermenting must",
                nome="Jan Baptist van Helmont"),
            wiki("Photosynthesis",
                "he hypothesized that the mass of the growing plant must come from the water, the only substance he added to the potted plant. "
                "His hypothesis was partially accurate – much of the gained mass comes from carbon dioxide as well as water. "
                "However, this was a signaling point to the idea that the bulk of a plant's biomass comes from the inputs of photosynthesis, not the soil itself.",
                nome="Photosynthesis"),
        ],
    },
    # 2 a rubisco, enzima mais abundante e atrapalhada
    {
        "temas_secundarios": ["evolucao", "atmosfera"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "A enzima mais abundante da Terra, a rubisco, que prende o gás carbônico na fotossíntese, é lenta e se confunde: em cerca de 25% das vezes agarra oxigênio no lugar do CO2 e desperdiça energia.",
        "explicacao": (
            "A rubisco é a peça da fotossíntese que fixa o carbono do ar em moléculas que viram açúcar. É a "
            "proteína mais abundante das folhas: nas plantas do tipo C3, responde por cerca de "
            "metade da proteína solúvel da folha. Ela também é relativamente lenta: cada "
            "molécula fixa algo como 3 a 10 moléculas de CO2 por segundo. Outra é o erro. O mesmo sítio ativo "
            "aceita oxigênio, e cerca de 25% das reações acabam usando O2, gerando um produto que a planta precisa "
            "reciclar a um custo alto, a fotorrespiração. Isso pode reduzir a produção fotossintética das plantas "
            "C3 em até 25%. A enzima surgiu há cerca de quatro bilhões de anos, antes de haver oxigênio na Terra, e "
            "levando em conta que hoje o O2 é cerca de 500 vezes mais abundante que o CO2 no ar, ela até favorece "
            "bastante o gás carbônico. Várias plantas desenvolveram truques para concentrar CO2 perto dela, como o "
            "metabolismo C4 e o CAM. E há quem tente consertar o problema: num teste agrícola, uma via sintética "
            "que substituiu a fotorrespiração aumentou em 40% o crescimento da lavoura."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("RuBisCO",
                "It emerged approximately four billion years ago in primordial metabolism prior to the presence of oxygen on Earth. "
                "It is the most abundant enzyme on Earth. [...] "
                "RuBisCO is the most abundant protein in leaves. It accounts for about 50% of soluble leaf protein in C3 plants [...] "
                "RuBisCO has a relatively low catalytic turnover, fixing about 3–10 molecules of CO2 per second. [...] "
                "Some plants, algae and photosynthetic bacteria concentrate CO2 around RuBisCO, reducing the frequency of oxygenation. "
                "These mechanisms include C4 carbon fixation, crassulacean acid metabolism and the use of pyrenoids.",
                nome="RuBisCO"),
            wiki("Photorespiration",
                "where the enzyme RuBisCO oxygenates ribulose 1,5-bisphosphate (RuBP), wasting some of the energy produced by photosynthesis. [...] "
                "approximately 25% of reactions by RuBisCO instead add oxygen to RuBP (oxygenation), creating a product that cannot be used within the Calvin–Benson cycle. "
                "This process lowers the efficiency of photosynthesis, potentially lowering photosynthetic output by 25% in C3 plants. [...] "
                "this represents significant favouring of CO2, when the relative abundance of the two gases is taken into account: in the current atmosphere, O2 is approximately 500 times more abundant [...] "
                "However, in an agricultural setting, replacing the native photorespiration pathway with an engineered synthetic pathway to metabolize glycolate in the chloroplast resulted in a 40 percent increase in crop growth.",
                nome="Photorespiration"),
        ],
    },
    # 3 a planta que faz divisão para o amido durar até o amanhecer
    {
        "temas_secundarios": ["sono_ritmos", "algoritmos"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "No escuro, a planta Arabidopsis gasta o amido guardado num ritmo que faz a reserva durar quase exatamente até o amanhecer, mesmo se a noite chegar mais cedo. Para pesquisadores, ela faz uma divisão.",
        "explicacao": (
            "Durante o dia, a Arabidopsis acumula amido nas folhas, e mais da metade do carbono captado na "
            "fotossíntese pode ser guardado assim. À noite, o estoque diminui de forma quase linear, e cerca de 95% "
            "dele é consumido até o amanhecer. O padrão é muito robusto e se mantém mesmo quando o escuro chega "
            "antes do esperado: a planta ajusta o ritmo de gasto à quantidade guardada e ao tempo que falta para o "
            "dia, que ela acompanha com seu relógio circadiano interno. Num estudo publicado em 2013 na revista "
            "eLife, Antonio Scialdone e colegas argumentaram que esse ajuste exige uma conta de dividir: estoque de "
            "amido pelo tempo até o amanhecer. Eles propuseram modelos químicos em que a quantidade de amido e o "
            "tempo restante são representados pela concentração de dois tipos de molécula, e a taxa de consumo é "
            "uma dividida pela outra. As previsões dos modelos foram testadas com sucesso em plantas expostas a um "
            "período de luz no meio da noite e em mutantes com falhas na degradação do amido. Os experimentos "
            "sugerem que uma enzima chamada PWD pode ser o ponto onde o resultado da conta entra no consumo. Ao "
            "contrário de um computador, que usa lógica digital, a divisão seria feita pela dinâmica analógica "
            "entre moléculas."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [
            artigo("PMC3691572", "Arabidopsis plants perform arithmetic division to prevent starvation at night (eLife, 2013)",
                "mulate in Arabidopsis leaves during the day decrease approximately linearly with time at night to support metabolism and growth. "
                "We find that the rate of decrease is adjusted to accommodate variation in the time of onset of darkness and starch content, such that reserves last almost precisely until dawn. "
                "Generation of these dynamics therefore requires an arithmetic division computation between the starch content and expected time to dawn. "
                "We introduce two novel chemical kinetic models capable of implementing analog arithmetic division. "
                "Predictions from the models are successfully tested in plants perturbed by a night-time light period or by mutations in starch degradation pathways. [...] "
                "Plants are able to track the time to dawn using their internal circadian clock [...] "
                "These experiments also revealed that an enzyme called PWD may be the point at which results of the division computation are integrated into the starch consumption pathway. [...] "
                "whereas computers rely on digital logic, Scialdone et al. show that arithmetic computations can also be performed by exploiting the analogue dynamics that take place between molecules. [...] "
                "more than half of the carbon assimilated via photosynthesis may be stored as semi-crystalline starch granules inside chloroplasts. "
                "At night, starch content decreases approximately linearly with time such that 95% of starch is utilized by dawn [...] "
                "This pattern of utilization is extremely robust, and is achieved even when darkness comes unexpectedly early [...] "
                "Copyright © 2013, Scialdone et al"),
        ],
    },
    # 4 a dioneia conta toques
    {
        "temas_secundarios": ["insetos", "eletromagnetismo"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "A dioneia, planta carnívora, conta. A armadilha só fecha se seus pelos sensíveis forem tocados duas vezes em até 20 segundos, e só passa a fazer enzimas digestivas após pelo menos cinco sinais elétricos.",
        "explicacao": (
            "Cada toque num dos pelos-gatilho da dioneia dispara um potencial de ação, um sinal elétrico "
            "que corre pela folha junto com uma onda de cálcio. O primeiro sinal eleva o cálcio "
            "sem chegar ao limiar. Se um segundo vier a tempo, o limiar é ultrapassado, e as duas metades da folha "
            "se fecham em cerca de um décimo de segundo. A planta, portanto, guarda uma espécie de memória de "
            "alguns segundos. Essa exigência evita gastar energia com gotas de chuva ou objetos sem valor "
            "nutritivo. Depois de fechada, a armadilha segue contando: os sinais extras gerados pela presa que se "
            "debate acionam o hormônio do toque, o ácido jasmônico, que leva a folha a se selar e a digerir o "
            "bicho. A produção de uma das enzimas, a que quebra a carapaça dos insetos, começa com pelo menos "
            "cinco sinais. Em 2023, pesquisadores da Universidade de Würzburg descreveram um mutante que ainda "
            "dispara os sinais elétricos, mas não fecha a armadilha nem inicia a caçada, por não conseguir ler e "
            "contar os sinais de cálcio. O mutante foi batizado de DYSCALCULIA, ou discalculia."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Venus_flytrap",
                "The mechanism is so highly specialized that it can distinguish between living prey and non-prey stimuli, such as falling raindrops; "
                "two trigger hairs must be touched in succession within 20 seconds of each other or one hair touched twice in rapid succession, whereupon the lobes of the trap will snap shut, typically in about one-tenth of a second. [...] "
                "The requirement of repeated, seemingly redundant triggering in this mechanism serves as a safeguard against energy loss and to avoid trapping objects with no nutritional value [...] "
                "Flytraps show an example of memory in plants; the plant knows if one of its trigger hairs have been touched, and remembers this for a few seconds. [...] "
                "One of these enzymes includes GH18 chitinase, which breaks down chitin-containing exoskeleton of trapped insects. "
                "Synthesis of this enzyme begins with at least five action potentials",
                nome="Venus flytrap"),
            resumo("36693369", "DYSCALCULIA, a Venus flytrap mutant without the ability to count action potentials (Current Biology, 2023)",
                "The Venus flytrap Dionaea muscipula estimates prey nutrient content by counting trigger hair contacts initiating action potentials (APs) and calcium waves traveling all over the trap. [...] "
                "A first AP is associated with a subcritical rise in cytosolic calcium concentration, but when the second AP arrives in time, calcium levels pass the threshold required for fast trap closure. "
                "Consequently, memory function and decision-making are timed via a calcium clock. [...] "
                "For higher numbers of APs elicited by the struggling prey, the Ca [...] "
                "clock connects to the networks governed by the touch hormone jasmonic acid (JA), which initiates slow, hermetic trap sealing and mining of the animal food stock. [...] "
                "Two distinct phases of trap closure can be distinguished within Dionaea's hunting cycle: (1) very fast trap snapping requiring two APs and crossing of a critical cytosolic Ca [...] "
                "The Dionaea mutant DYSC is still able to fire touch-induced APs but does not snap close its traps and fails to enter the hunting cycle after prolonged mechanostimulation. [...] "
                "DYSCALCULIA, a Venus flytrap mutant without the ability to count action potentials. [...] "
                "University of Würzburg [...] "
                "\"dateOfPublication\":\"2023 Feb\" [...] "
                "indicates that DYSC cannot properly read, count, and decode touch/AP-induced calcium signals that are key in prey capture and processing."),
        ],
    },
    # 5 girassol adulto não segue o Sol
    {
        "temas_secundarios": ["sono_ritmos", "insetos"],
        "tipos_espanto": ["mito_desmentido", "engenhosidade"],
        "gancho": "O girassol adulto não acompanha o Sol: a flor aberta fica virada para o leste o dia todo. Quem gira é a planta jovem, guiada por um relógio interno, que de madrugada se volta para o leste à espera do dia.",
        "explicacao": (
            "A crença de que a flor do girassol segue o Sol é antiga, e antiga também é a dúvida: em 1597, o "
            "botânico inglês John Gerard escreveu que nunca conseguira observar isso no seu jardim. Quem se move é "
            "a planta jovem, ainda em botão. De dia, o topo dela acompanha o Sol de leste a oeste. À noite, volta "
            "a apontar para o leste antes do amanhecer. O movimento é um ritmo circadiano, acertado pelo Sol, que "
            "continua em dias nublados ou sob luz constante. Ele acontece porque os lados leste e oeste do caule "
            "se alongam em fases alternadas. Quando o caule para de crescer e a flor amadurece, o "
            "movimento cessa, e ela fica voltada para o leste. Um estudo publicado na Science em 2016 mostrou as "
            "vantagens: o acompanhamento do Sol aumenta a massa da planta jovem, e a flor virada para o leste "
            "esquenta rápido pela manhã e recebe mais visitas de polinizadores. O alinhamento de uma plantação "
            "inteira, todas as flores na mesma direção, ajuda a manter a falsa impressão de que elas seguem o Sol."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Common_sunflower",
                "A common misconception is that flowering sunflower heads track the Sun across the sky. "
                "Although immature flower buds exhibit this behaviour, the mature flowering heads point in a fixed (and typically easterly) direction throughout the day. "
                "This old misconception was disputed in 1597 by the English botanist John Gerard, who grew sunflowers in his famous herbal garden: \"[some] have reported it to turn with the Sun, the which I could never observe [...] "
                "The uniform alignment of sunflower heads in a field might give some people the false impression that the flowers are tracking the Sun. [...] "
                "Their heliotropic motion is a circadian rhythm, synchronized by the sun, which continues if the sun disappears on cloudy days or if plants are moved to constant light. [...] "
                "When growth of the flower stalk stops and the flower is mature, the heliotropism also stops and the flower faces east from that moment onward. "
                "This eastward orientation allows rapid warming in the morning, and as a result, an increase in pollinator visits.",
                nome="Common sunflower"),
            resumo("27493185", "Circadian regulation of sunflower heliotropism, floral orientation, and pollinator visits (Science, 2016)",
                "Young sunflower plants track the Sun from east to west during the day and then reorient during the night to face east in anticipation of dawn. "
                "In contrast, mature plants cease movement with their flower heads facing east. "
                "We show that circadian regulation of directional growth pathways accounts for both phenomena and leads to increased vegetative biomass and enhanced pollinator visits to flowers. "
                "Solar tracking movements are driven by antiphasic patterns of elongation on the east and west sides of the stem. [...] "
                "\"dateOfPublication\":\"2016 Aug\""),
        ],
    },
    # 6 plantas que esquentam: lótus e repolho-gambá
    {
        "temas_secundarios": ["termodinamica", "insetos"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Algumas plantas produzem o próprio calor. A flor do lótus-sagrado se mantém entre 30 e 35 °C mesmo com o ar a 10 °C, e o repolho-gambá derrete o chão congelado para florescer.",
        "explicacao": (
            "As plantas termogênicas conseguem ficar mais quentes que o ar à sua volta. O calor sai das "
            "mitocôndrias, com ajuda de uma enzima chamada oxidase alternativa e de proteínas desacopladoras parecidas com as "
            "encontradas em mamíferos. A oxidase alternativa desvia a respiração celular de um jeito "
            "ineficiente: em vez de virar energia útil, boa parte vira calor. De quebra, torna essa respiração "
            "resistente ao cianeto. O repolho-gambá-oriental, da família das aráceas, chega a ficar de 15 a "
            "35 °C acima do ar e abre caminho pelo solo congelado, florescendo quando ainda há neve. O lótus-"
            "sagrado faz algo mais sofisticado: regula a temperatura da flor dentro de uma faixa estreita, de 30 a "
            "35 °C, mesmo com o ar a 10 °C. Pesquisadores acham que isso pode atrair insetos polinizadores, que "
            "têm sangue frio. A explicação mais aceita para o calor em geral é que ele ajuda a espalhar o cheiro "
            "que chama os polinizadores. A flor-cadáver, por exemplo, usa vapor d'água aquecido para levar seu odor "
            "de carne podre acima do ar frio que se acumula à noite. Ainda assim, o processo é pouco compreendido."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Thermogenic_plant",
                "Thermogenic plants have the ability to raise their temperature above that of the surrounding air. "
                "Heat is generated in the mitochondria, as a secondary process of cellular respiration called thermogenesis. "
                "Alternative oxidase and uncoupling proteins similar to those found in mammals enable the process, which is still poorly understood. [...] "
                "The most widely accepted theory states that the endogenous heat helps in spreading chemicals that attract pollinators to the plant. [...] "
                "Thermogenic plants are found in a variety of families, but the Araceae in particular contains many such species. "
                "Examples from this family include the dead-horse arum (Helicodiceros muscivorus), the eastern skunk cabbage (Symplocarpus foetidus) [...] "
                "The titan arum (Amorphophallus titanum) uses thermogenically created water vapor to disperse its scent—that of rotting meat—above the cold air that settles over it at night in its natural habitat. [...] "
                "Plants containing this alternative oxidase are unaffected by the effects of cyanide [...] "
                "which in turn is very inefficient yielding a drop in free energy from Ubiquinol to oxygen which is released in heat.",
                nome="Thermogenic plant"),
            wiki("Nelumbo_nucifera",
                "Lotus flowers regulate their temperature to within a narrow range, maintaining temperatures of 30–35 °C (86–95 °F), even with air temperatures as low as 10 °C (50 °F). "
                "Researchers think that this may be to attract cold-blooded insect pollinators to the flowers.",
                nome="Nelumbo nucifera"),
            wiki("Symplocarpus_foetidus",
                "Eastern skunk cabbage belongs to a select group of thermogenic plants for its capacity to create temperatures of up to 15–35 °C (27–63°F) above air temperature through cyanide-resistant cellular respiration (via alternative oxidase) in order to melt its way through frozen ground. [...] "
                "Eastern skunk cabbage blooms while there is snow and ice on the ground",
                nome="Symplocarpus foetidus"),
        ],
    },
    # 7 a vitória-régia prende besouros por um dia
    {
        "temas_secundarios": ["amazonia", "insetos"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "A flor da vitória-régia abre branca e perfumada ao anoitecer e depois se fecha com besouros presos dentro. Passa o dia seguinte alimentando-os, fica rosada e só os solta, cheios de pólen, na outra noite.",
        "explicacao": (
            "A vitória-régia, nativa da bacia amazônica, tem folhas de até 3 metros de diâmetro e flores de até 40 "
            "centímetros e 1,6 kg, superadas em massa só pelas do gênero Rafflesia. As flores começam a abrir "
            "quando o Sol se põe. Brancas, elas soltam um cheiro de fruta que atrai besouros do gênero Cyclocephala. "
            "Ao anoitecer, a flor para de exalar o perfume e se fecha, deixando os besouros presos numa cavidade de "
            "tecido esponjoso e rico em amido, que lhes serve de comida. Ela continua fechada no dia seguinte, "
            "enquanto produz antocianinas, pigmentos que mudam as pétalas de branco para rosa avermelhado, sinal de "
            "que a flor já foi polinizada. Na noite do segundo dia, a flor se abre o bastante para soltar os "
            "insetos, que saem cobertos de pólen e voam até outra flor recém-aberta. O sistema impede a "
            "autofecundação: numa mesma noite, todas as flores de uma planta estão na fase feminina ou todas na "
            "masculina, e o pólen precisa vir de outro indivíduo. O processo foi descrito em detalhe pelo botânico "
            "Ghillean Prance e por Jorge Arius."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Victoria_amazonica",
                "It is called Vitória-Régia or Iaupê-Jaçanã (\"the jacana's waterlily\") in Brazil [...] "
                "Its native region is tropical South America, specifically Guyana and the Amazon Basin. [...] "
                "Victoria amazonica has very large leaves (lamina; commonly called \"pads\" or \"lily pads\"), up to 3 m (10 ft) in diameter [...] "
                "In their native habitat, the flowers first begin to open as the sun starts to set and can take up to 48 hours to fully open. "
                "These flowers can grow up to 40 cm (16 in) in diameter and 1.6 kg (3.5 lb) in weight, exceeded in mass only by members of the genus Rafflesia. "
                "All of the flowers of one particular plant will, on a given evening, all be in the female phase or all in the male phase, so that pollination must be by a different individual, precluding self-pollination. [...] "
                "they have co-evolved a mutualistic relationship with a species of scarab beetle of the genus Cyclocephala as a pollinator. "
                "All the buds in a single patch will begin to open at the same time and as they do, they give off a fruity smell. "
                "At this point, the flower petals are white, and the beetles are attracted both to the colour and the smell of the flower. "
                "At nightfall the flower stops producing the odor, and it closes, trapping the beetles inside its carpellary appendages. "
                "Here, the stamens are protected by the paracarpels, and for the next day, the flower continues to remain closed. "
                "The cavity in which the beetle is trapped is composed of a spongy, starchy tissue that provides nourishment for the beetle. "
                "During this time, anthocyanins start to be released by the plant, which in turn changes the petals from white to a reddish pink colour, a sign that the flower will have been pollinated. [...] "
                "During the evening of the second day, the flowers will have opened enough to release the beetle, and as it pushes its way through the stamens, it becomes covered in pollen. "
                "These insects will then go on to find a newly opened water lily and pollinate with the pollen they are carrying from the previous flower. "
                "This process was described in detail by Sir Ghillean Prance and Jorge Arius.",
                nome="Victoria amazonica"),
        ],
    },
    # 8 Rafflesia: flor gigante sem genoma de cloroplasto
    {
        "temas_secundarios": ["genetica", "evolucao"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "A Rafflesia, gênero da maior flor do mundo, não tem folhas, caule nem raiz: vive escondida dentro de um cipó. E pode ser a primeira planta conhecida sem um genoma de cloroplasto reconhecível.",
        "explicacao": (
            "As Rafflesias, do Sudeste Asiático, são parasitas totais de cipós do gênero Tetrastigma, parentes da "
            "videira. Espalham dentro do tecido do hospedeiro um órgão que suga nutrientes, e a única parte que "
            "aparece do lado de fora é a flor de cinco pétalas. Na Rafflesia arnoldii, ela pode passar de 100 centímetros "
            "de diâmetro e pesar até 10 kg; uma flor que abriu em Sumatra em 2020 mediu 111 centímetros, o maior "
            "registro já feito. Com aspecto e cheiro de carne podre, atrai moscas que levam o pólen. O gênero perdeu "
            "a capacidade de fazer fotossíntese. Um estudo publicado em 2014 foi mais longe. Ao sequenciar a Rafflesia lagascae, das Filipinas, a "
            "equipe montou o genoma das mitocôndrias, que é bem maior, mas achou só pequenos fragmentos do genoma "
            "do cloroplasto, nenhum com gene intacto. Cerca de um terço desses restos talvez tenha vindo do próprio "
            "cipó hospedeiro, por transferência horizontal de genes. Os autores concluíram que a Rafflesia pode ser "
            "a primeira planta sem genoma de cloroplasto reconhecível, ou então que ele existe de forma oculta, em "
            "níveis muito baixos."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Rafflesia",
                "is a genus of parasitic flowering plants in the family Rafflesiaceae. "
                "The species have enormous flowers, the buds rising from the ground or directly from the lower stems of their host plants; one species has the largest flower in the world. [...] "
                "all of them are found in Southeast Asia. [...] "
                "The plant has no stems, leaves or roots. "
                "It is a holoparasite of vines in the genus Tetrastigma (a plant in the Vitaceae, the grape vine family), spreading its absorptive organ, the haustorium, inside the tissue of the vine. "
                "The only part of the plant that can be seen outside the host vine is the five-petalled flower. "
                "In some species, such as Rafflesia arnoldii, the flower may be over 100 centimetres (40 in) in diameter, and weigh up to 10 kilograms (22 lb). "
                "A Rafflesia that bloomed in West Sumatra in January 2020 was measured to be 111 centimetres (44 in) in diameter, the largest flower ever recorded [...] "
                "The flowers look and smell like rotting flesh. "
                "The foul odour attracts insects such as carrion flies, which transport pollen from male to female flowers.",
                nome="Rafflesia"),
            resumo("24458431", "Possible loss of the chloroplast genome in the parasitic flowering plant Rafflesia lagascae (Molecular Biology and Evolution, 2014)",
                "Rafflesia is a genus of holoparasitic plants endemic to Southeast Asia that has lost the ability to undertake photosynthesis. "
                "With short-read sequencing technology, we assembled a draft sequence of the mitochondrial genome of Rafflesia lagascae Blanco, a species endemic to the Philippine island of Luzon [...] "
                "we were only able to identify small fragments of plastid sequences at low coverage depth [...] "
                "None of the identified plastid gene sequences had intact reading frames. "
                "Phylogenetic analysis suggests that ∼33% of these remnant plastid genes may have been horizontally transferred from the host plant genus Tetrastigma [...] "
                "despite success in identifying and developing a draft assembly of the much larger mitochondrial genome--suggests that the parasitic plant genus Rafflesia may be the first plant group for which there is no recognizable plastid genome, or if present is found in cryptic form at very low levels. [...] "
                "\"dateOfPublication\":\"2014 Apr\""),
        ],
    },
    # 9 Nepenthes rajah, o vaso sanitário dos musaranhos
    {
        "temas_secundarios": ["comportamento_animal", "ecologia"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Em Bornéu, uma planta carnívora virou banheiro: o jarro da Nepenthes rajah oferece néctar na tampa a um mamífero, o tupaia-da-montanha, que come ali e defeca dentro dele. As fezes adubam a planta.",
        "explicacao": (
            "A Nepenthes rajah só existe no monte Kinabalu e no vizinho monte Tambuyukon, em Bornéu, na Malásia. "
            "Seus jarros, armadilhas cheias de líquido digestivo, chegam a 41 centímetros de altura e a 3,5 litros "
            "de capacidade, provavelmente os maiores do gênero. A maior parte das presas são insetos, sobretudo "
            "formigas, e há registros de ratos afogados. Mas a planta tem outra fonte de "
            "nitrogênio. A face interna da tampa solta um néctar doce, e a distância entre a boca do jarro e esse "
            "néctar é igual ao comprimento médio do corpo do tupaia-da-montanha. "
            "Enquanto lambe o néctar, o animal defeca no jarro, aparentemente para marcar território. "
            "Acredita-se que essas fezes forneçam à planta a maior parte do nitrogênio de que ela precisa. Até a "
            "cor da parte de baixo da tampa combina com as faixas de verde e azul que o tupaia enxerga melhor. Em "
            "2011, pesquisadores relataram que um rato da montanha faz o mesmo papel à noite, quando o tupaia, "
            "ativo de dia, não está lá. Os dois visitantes deixam quantidades parecidas de fezes por dia."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Nepenthes_rajah",
                "It is endemic to Mount Kinabalu and neighbouring Mount Tambuyukon in Sabah, Malaysian Borneo. [...] "
                "for the giant urn-shaped traps it produces, which can grow up to 41 cm (16 in) high and 20 cm (7.9 in) wide. "
                "These are capable of holding 3.5 L (0.92 US gal) of water and in excess of 2.5 L (0.66 US gal) of digestive fluid, making them probably the largest in the genus. [...] "
                "There exist at least two records of drowned rats found in N. rajah pitchers. [...] "
                "Insects, and particularly ants, comprise the majority of prey in both aerial and terrestrial pitchers. [...] "
                "Nepenthes rajah has evolved a mutualistic relationship with mountain treeshrews (Tupaia montana) in order to collect their droppings. "
                "The inside of the reflexed lid exudes a sweet nectar. "
                "The distance from the pitcher mouth to the exudate is the same as the average body length of the mountain treeshrew. "
                "As it feeds, the treeshrew defecates, apparently as a method of marking its feeding territory. "
                "It is thought that in exchange for providing nectar, the faeces provide the plant with the majority of the nitrogen it requires. "
                "In N. lowii, N. macrophylla and N. rajah, the colour of the lower lid surface corresponds to visual sensitivity maxima of the mountain treeshrew in the green and blue wavebands [...] "
                "In 2011, it was reported that N. rajah has a similar mutualistic relationship with the summit rat (Rattus baluensis). "
                "Whereas the mountain treeshrew visits pitchers during daylight hours, the summit rat is primarily active at night; this may be an example of resource partitioning. "
                "Daily scat deposition rates were found to be similar for both mammalian species.",
                nome="Nepenthes rajah"),
        ],
    },
    # 10 o bambu que floresce a cada 48 anos e traz ratos e guerra
    {
        "temas_secundarios": ["ecologia", "asia_antiga"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana", "escala_absurda"],
        "gancho": "A cada 48 a 50 anos, um bambu floresce todo de uma vez no nordeste da Índia. A fartura de sementes faz os ratos explodirem e depois devorarem as lavouras. Na fome de 1958–1959, um grupo de socorro virou guerrilha.",
        "explicacao": (
            "O fenômeno se chama mautam e acontece em estados do nordeste da Índia, como Mizoram, Manipur e "
            "Tripura, e em partes de Mianmar. O bambu Melocanna baccifera floresce de forma quase totalmente "
            "sincronizada numa área enorme e produz até 80 toneladas de frutos por hectare. Com tanta comida, a "
            "população de ratos-pretos dispara. Quando as sementes acabam, os ratos deixam a floresta e atacam os "
            "grãos plantados e armazenados, causando fome. No mautam de 1958–1959, em Mizoram, formou-se a Frente "
            "Nacional Mizo contra a Fome, para levar socorro às áreas isoladas. Ela depois virou a Frente Nacional "
            "Mizo, que em 1966 iniciou uma grande revolta. Sob o líder Laldenga, o grupo travou 20 anos de luta "
            "separatista contra o Exército indiano, até um acordo de 1986 garantir a Mizoram autonomia como estado "
            "separado. Laldenga chegou depois a ministro-chefe. O último mautam foi em 2007–2008, e, se o padrão "
            "continuar, o próximo será em 2055–2056. Surtos de ratos ligados à floração de bambus também ocorrem "
            "no Laos, no Japão, em Madagascar e na América do Sul."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Mautam",
                "is a cyclic ecological phenomenon that occurs every 48–50 years in the northeastern Indian states of Tripura, Mizoram and Manipur [...] "
                "and Chin State in Myanmar [...] "
                "It begins with a rat population boom, which in turn creates a widespread famine in those areas. "
                "During mautam, Melocanna baccifera, a species of bamboo, flowers at one time across a wide area. "
                "This event is followed invariably by a plague of black rats in what is called a rat flood. "
                "The bamboo flowering brings a temporary windfall of seeds, and rats multiply, exhaust the bamboo seeds, leave the forests, forage on stored grain, and cause devastating famine. "
                "Regular rodent outbreaks associated with bamboo flowering (and subsequent fruiting and seeding) also occur in the nearby Indian states of Arunachal Pradesh, Assam, Manipur, and Nagaland, as well as in Laos, Japan, Madagascar, and South America. [...] "
                "and 2007–2008 [...] "
                "The next predicted events if this pattern continues are mautam in 2055–2056 [...] "
                "During the mautam period of 1958 and 1959, the Mizo National Famine Front (MNFF) was set up to provide relief to the far-flung areas. "
                "This body later became the Mizo National Front (MNF), which staged a major uprising in 1966. "
                "Under its leader Laldenga (who later became the chief minister of Mizoram), MNF fought a bitter separatist struggle for 20 years against the Indian Army until an accord that guaranteed Mizoram's autonomy as a separate state was signed in 1986.",
                nome="Mautam"),
            wiki("Melocanna_baccifera",
                "Melocanna baccifera flowers almost fully synchronically every 48 years. [...] "
                "the population of black rats Rattus rattus burgeons owing to the plentiful food supply provided by the bamboo fruit (up to 80 tonnes per hectare), and once this is exhausted, famine follows as the rats move on to consume local crops",
                nome="Melocanna baccifera"),
        ],
    },
    # 11 a planta de 32 mil anos ressuscitada da toca de esquilos
    {
        "temas_secundarios": ["mudancas_climaticas", "paleontologia"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "Uma planta que estava congelada havia cerca de 32 mil anos na Sibéria voltou a crescer e florescer em laboratório. O material veio de despensas de esquilos soterradas no permafrost.",
        "explicacao": (
            "Em 2007, cientistas da Rússia, da Hungria e dos Estados Unidos investigaram cerca de 70 tocas antigas "
            "de esquilos-terrestres às margens do rio Kolimá, no nordeste da Sibéria, de 20 a 40 metros abaixo da "
            "superfície atual. Os roedores tinham guardado ali mais de 600 mil frutos e sementes. Uma enchente ou "
            "outro evento soterrou a área, e o material congelou quase na hora, sem nunca mais descongelar. Entre "
            "os achados estavam frutos de Silene stenophylla, uma pequena planta da tundra que ainda vive na região. "
            "As sementes maduras não germinaram, mas a equipe conseguiu cultivar plantas adultas a partir do tecido "
            "do fruto: foram 36 exemplares. Em 2012, os pesquisadores anunciaram que a datação por radiocarbono dava "
            "ao material 31.800 anos, com margem de 300. O recorde anterior de planta trazida de volta era de "
            "sementes de tamareira da Judeia com 2 mil anos. As plantas ressuscitadas pareciam iguais às atuais até "
            "florescerem: as pétalas eram mais longas e mais espaçadas, por motivos desconhecidos. As sementes "
            "que elas produziram germinaram em 100% dos casos. O líder do trabalho, David Gilichinsky, morreu pouco "
            "antes da publicação."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Silene_stenophylla",
                "It is typically 5–25 cm (2–10 in) tall [...] "
                "It grows in the Arctic tundra of far eastern Siberia and the mountains of northern Japan. "
                "Frozen samples, estimated via radiocarbon dating to be around 32,000 years old, were discovered in the same area as current living specimens and, in 2012, a team of scientists successfully regenerated a plant from the samples. [...] "
                "A team of scientists from Russia, Hungary and the United States recovered frozen Silene stenophylla seeds and remains from the Pleistocene in 2007, while investigating about 70 ancient ground squirrel [...] "
                "on the right bank of the lower Kolyma River in Sakha Republic, northeastern Siberia, in the plant's present-day range. [...] "
                "The burrows were found 20–40 m (66–131 ft) below the present-day surface. "
                "Usually the rodents would eat the food in their larders, but in this case a flood or other weather event buried the whole area. "
                "Since the rodents had placed the larders at the level of the permafrost, the material froze almost immediately, and did not thaw out at any time since. "
                "More than 600,000 fruits and seeds were located at the site. [...] "
                "In February 2012, a team of scientists from the Institute of Cell Biophysics of the Russian Academy of Sciences announced they had successfully regenerated specimens from fruit that had been frozen for 31,800 (±300) years according to their radiocarbon dating. "
                "The accomplishment surpasses the previous record for the oldest plant material brought back to life, of 2000 years set by Judean date palm (Phoenix dactylifera) seeds. "
                "The team led by David Gilichinsky used material recovered in 2007 by Stakhov et al. "
                "Gilichinsky, who for many years was head of the Geocryology Lab in the Institute for Physicochemical and Biological Problems in Soil Science at the Russian Academy of Sciences in Moscow, died in February 2012, just before the paper was published. [...] "
                "Initially, the researchers attempted to germinate mature seeds recovered from the fruit. "
                "When these attempts failed, they turned to the fruit itself and were able to culture adult plants from placental tissue. "
                "The team grew 36 specimens from the tissue. "
                "The plants looked identical to modern specimens until they flowered, at which time the petals were observed to be longer and more widely spaced than modern versions of the plant. "
                "The reasons for the observed variations are not known. "
                "Seeds produced by the regenerated plants germinated at a 100% success rate",
                nome="Silene stenophylla"),
        ],
    },
    # 12 o pinheiro-de-wollemi, achado em 1994
    {
        "temas_secundarios": ["paleontologia", "evolucao"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1994, exploradores de cânions acharam, a 150 km de Sydney, uma árvore desconhecida, parente das araucárias. Na natureza há menos de 60 adultos, geneticamente indistinguíveis, num local mantido em segredo.",
        "explicacao": (
            "Por volta de 10 de setembro de 1994, David Noble, Michael Casteleyn e Tony Zimmerman exploravam "
            "sistematicamente o Parque Nacional Wollemi, na Austrália, em busca de cânions novos. Num conjunto de "
            "desfiladeiros estreitos de arenito, Noble, que entendia de botânica, estranhou a casca de algumas "
            "árvores. Era uma espécie nova, tão diferente que ganhou um gênero novo, Wollemia, e o nome da espécie "
            "homenageia Noble. Ela é um dos três únicos gêneros vivos da família das araucárias, ao lado de "
            "Araucaria e Agathis. Apesar de muitas vezes ser chamada de \"fóssil vivo\", não há fósseis que se "
            "possam atribuir a ela sem dúvida. Na natureza, são menos de 60 árvores adultas, em quatro pontos "
            "próximos, e os testes genéticos não distinguem um exemplar do outro, sinal de que a espécie passou por "
            "um gargalo. A localização segue sem divulgação, e mesmo assim em 2005 as árvores foram infectadas por "
            "um patógeno que, segundo os guardas-parque, chegou com visitantes não autorizados. Nos incêndios de "
            "2019–2020, bombeiros especializados salvaram o bosque com um sistema de irrigação e lançamento de "
            "retardante. Como a árvore pode ser clonada, mudas foram plantadas pelo mundo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Wollemia",
                "The species represents one of only three living genera in the family, alongside Araucaria and Agathis (being more closely related to the latter), which was discovered in 1994 in a temperate rainforest wilderness area of the Wollemi National Park in New South Wales. "
                "It was growing in a remote series of narrow, steep-sided, sandstone gorges 150 km (93 mi) north-west of Sydney. [...] "
                "Although often described as a \"living fossil\", there are no unambiguous fossils of Wollemia and potential fossil records of it have been considered uncertain. [...] "
                "The discovery, on or about 10 September 1994, by David Noble, Michael Casteleyn, and Tony Zimmerman, occurred only because the group had been systematically exploring the area, looking for new canyons. "
                "Noble had good botanical knowledge, and quickly recognised the trees as unusual because of the unique bark, and worthy of further investigation. [...] "
                "The species was subsequently named after David Noble. [...] "
                "it has been placed into a new genus, beside the genera Agathis and Araucaria. [...] "
                "After it was discovered that the trees could be successfully cloned, new specimens were planted widely around the world in regions with mild temperate climates. [...] "
                "Fewer than 60 adult trees are known to be growing wild in four locations, not far apart. [...] "
                "Genetic testing has revealed that all the specimens are genetically indistinguishable, suggesting that the species has been through a genetic bottleneck [...] "
                "In November 2005, wild-growing trees were found to be infected with Phytophthora cinnamomi. "
                "New South Wales park rangers believe the virulent water mould was introduced by unauthorised visitors to the site, the location of which is still undisclosed to the public. [...] "
                "The grove of Wollemia trees was endangered by fire during the 2019–2020 Australian bushfire season. "
                "They were saved by specialist firefighters from the National Parks and Wildlife Service, supported by the Rural Fire Service who installed an irrigation system as well as dropping retardant.",
                nome="Wollemia"),
        ],
    },
    # 13 gympie-gympie: veneno de planta com estrutura de veneno de aranha
    {
        "temas_secundarios": ["farmacos", "evolucao"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "A dor causada pela gympie-gympie, uma urtiga-árvore australiana, pode voltar por semanas. Em 2020 veio a explicação: seus pelos injetam miniproteínas com estrutura parecida com a de toxinas de aranhas.",
        "explicacao": (
            "A gympie-gympie, Dendrocnide moroides, é da família das urtigas e cresce nas florestas tropicais de "
            "Queensland e Nova Gales do Sul, na Austrália. Ao tocar a pele, seus pelos rígidos provocam uma dor "
            "aguda que costuma durar horas, com crises intermitentes que podem persistir por dias e semanas. Duas "
            "pessoas já precisaram de 36 horas de terapia intensiva, com uma dor que, segundo relatos, não cedia "
            "à morfina. Atribuía-se o efeito a pequenas moléculas, como neurotransmissores e substâncias "
            "inflamatórias, mas elas não explicavam tudo. Num estudo publicado em 2020 na Science Advances, "
            "pesquisadores encontraram nos pelos uma família desconhecida de peptídeos, batizados de gimpietídeos. "
            "São miniproteínas que ativam neurônios sensoriais de camundongos e atrasam a inativação dos canais de "
            "sódio dependentes de voltagem. A forma delas é travada por um \"nó de cistina\", o mesmo arranjo de "
            "neurotoxinas presentes no veneno de aranhas e de caracóis-cone. Para os autores, é um caso de evolução "
            "convergente entre reinos: animais e uma planta chegaram a venenos com o mesmo modo de aplicação, "
            "estrutura e ação farmacológica. Essa estrutura muito estável ajudaria a explicar por que a dor dura tanto."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            artigo("PMC7494335", "Neurotoxic peptides from the venom of the giant Australian stinging tree (Science Advances, 2020)",
                "Stinging trees from Australasia produce remarkably persistent and painful stings upon contact of their stiff epidermal hairs, called trichomes, with mammalian skin. [...] "
                "-induced acute pain typically lasts for several hours, and intermittent painful flares can persist for days and weeks. "
                "Pharmacological activity has been attributed to small-molecule neurotransmitters and inflammatory mediators, but these compounds alone cannot explain the observed sensory effects. "
                "We show here that the venoms of Australian [...] "
                "species contain heretofore unknown pain-inducing peptides that potently activate mouse sensory neurons and delay inactivation of voltage-gated sodium channels. "
                "These neurotoxins localize specifically to the stinging hairs and are miniproteins of 4 kDa, whose 3D structure is stabilized in an inhibitory cystine knot motif, a characteristic shared with neurotoxins found in spider and cone snail venoms. "
                "Our results provide an intriguing example of inter-kingdom convergent evolution of animal and plant venoms with shared modes of delivery, molecular structure, and pharmacology. [...] "
                "has been implicated in hospitalization of two individuals requiring intensive care for 36 hours who suffered from acute pain that reportedly did not respond to morphine and ongoing symptoms lasting months"),
            wiki("Dendrocnide_moroides",
                "is a plant in the nettle family Urticaceae found in rainforest areas of Queensland and New South Wales in Australia. [...] "
                "In 2020 a previously unknown family of disulfide-rich peptides was identified by a group of researchers and given the name gympietides. [...] "
                "Moreover, their complex structure – resembling the inhibitor cystine knot – made them highly stable, explaining how the sting lasts for such a long time.",
                nome="Dendrocnide moroides"),
        ],
    },
    # 14 o cipó-chumbo fareja o tomateiro
    {
        "temas_secundarios": ["sentidos", "ecologia"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "O cipó-chumbo, planta parasita quase sem clorofila, acha a vítima pelo cheiro: num estudo de 2006, suas mudas cresceram rumo ao aroma de tomateiros e preferiram o do tomate ao do trigo.",
        "explicacao": (
            "No Brasil, as plantas do gênero Cuscuta têm nomes como cipó-chumbo, fios-de-ovos e cipó-dourado. São "
            "trepadeiras amarelas ou alaranjadas, com folhas reduzidas a escamas e pouquíssima clorofila. Algumas "
            "espécies ainda fazem um pouco de fotossíntese, mas outras dependem totalmente da planta hospedeira. "
            "Num estudo publicado na Science em 2006, pesquisadores da Universidade Estadual da Pensilvânia "
            "mostraram que as mudas de Cuscuta pentagona encontram a vítima pelos compostos voláteis que ela solta "
            "no ar. Elas cresciam em direção a tomateiros próximos e também em direção a voláteis extraídos de "
            "tomateiros, apresentados sem nenhuma outra pista. Diante de cheiros de tomate e de trigo, preferiam o "
            "tomate. Vários compostos isolados das duas plantas atraíam as mudas, mas um composto do trigo as "
            "repelia. Na época, o papel desses voláteis na interação entre espécies de plantas era muito debatido. "
            "Depois de alcançar o hospedeiro, a cuscuta se enrola nele e enfia estruturas chamadas haustórios no "
            "sistema vascular, de onde tira água e nutrientes. A raiz original, já inútil, morre. Pela conexão "
            "passam também moléculas de RNA e pequenos peptídeos entre as duas plantas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            resumo("17008532", "Volatile chemical cues guide host location and host selection by parasitic plants (Science, 2006)",
                "The importance of plant volatiles in mediating interactions between plant species is much debated. "
                "Here, we demonstrate that the parasitic plant Cuscuta pentagona (dodder) uses volatile cues for host location. "
                "Cuscuta pentagona seedlings exhibit directed growth toward nearby tomato plants (Lycopersicon esculentum) and toward extracted tomato-plant volatiles presented in the absence of other cues. [...] "
                "Moreover, seedlings can distinguish tomato and wheat volatiles and preferentially grow toward the former. "
                "Several individual compounds from tomato and wheat elicit directed growth by C. pentagona, whereas one compound from wheat is repellent. [...] "
                "Pennsylvania State University [...] "
                "\"dateOfPublication\":\"2006 Sep\""),
            wiki("Cuscuta",
                "is a genus of over 201 species of yellow, orange, or red (rarely green) parasitic plants. "
                "The genus possess minimal chlorophyll and utilize haustoria to extract nutrient and water from host's vascular system. [...] "
                "some species such as Cuscuta reflexa can photosynthesize slightly, while others such as C. europaea are entirely dependent on the host plants for nutrition. [...] "
                "After a dodder attaches itself to a plant, it wraps itself around it. "
                "If the host contains food beneficial to dodder, the dodder produces haustoria that insert themselves into the vascular system of the host. [...] "
                "The vestigial root of the dodder in the soil then dies. [...] "
                "exchange of mRNA, small RNA, and small peptides occurs between the host and the dodder through this connection.",
                nome="Cuscuta"),
            wiki("Cuscuta",
                "Possui diversos nomes comuns no Brasil, dentre os quais cipó-chumbo (nome que também é dado a espécies de Cassytha), fios-de-ovos, cipó-dourado, aletria, espaguete, tinge-ovos e cuscuta. [...] "
                "São trepadeiras com folhas escamiformes (no geral, reduzidas) ou ausentes",
                nome="Cuscuta", idioma="pt"),
        ],
    },
    # 15 açacu, a árvore que dispara sementes a 250 km/h
    {
        "temas_secundarios": ["amazonia", "biomimetica"],
        "tipos_espanto": ["escala_absurda", "engenhosidade", "origem_inesperada"],
        "gancho": "O fruto do açacu, árvore da Amazônia, explode ao amadurecer e lança as sementes a 70 m/s, cerca de 250 km/h. Filmagens em alta velocidade mostraram que elas voam girando para trás, o que reduz o arrasto.",
        "explicacao": (
            "O açacu, ou assacu, nome de origem tupi, é a Hura crepitans, árvore da família das euforbiáceas, nativa das "
            "regiões tropicais das Américas, Amazônia incluída. Pode passar de 60 metros de altura, e seu tronco é "
            "coberto de espinhos que, nas árvores maduras, ficam tão juntos que as bases se tocam. O fruto parece "
            "uma pequena abóbora, com 16 gomos dispostos em círculo. Quando amadurece, ele estoura, se parte em pedaços "
            "e atira as sementes achatadas, de uns 2 centímetros, a 70 metros por segundo. As estimativas de "
            "alcance variam: uma fonte fala em até 45 metros, com 30 metros como o mais comum. A análise de vídeos "
            "em alta velocidade revelou um detalhe: as sementes giram para trás, e não para a frente como se "
            "supunha, o que as mantém orientadas para sofrer menos arrasto. A seiva leitosa é tóxica e foi usada "
            "para envenenar peixes e pontas de flecha. Em inglês, a árvore se chama \"sandbox tree\", árvore da "
            "caixa de areia: na época das penas de escrever, os frutos verdes eram serrados ao meio e viravam "
            "potinhos para a areia que secava a tinta."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Hura_crepitans",
                "Hura crepitans, known by the common names sandbox tree, possumwood, monkey no-climb, assacu (from Tupi asaku), and jabillo, is a species of evergreen tree in the family Euphorbiaceae, native to tropical regions of North and South America including the Amazon rainforest. [...] "
                "Because its fruit explodes when ripe, it has also received the colloquial nickname \"dynamite tree\". [...] "
                "The sandbox tree can grow to 60 metres (200 ft) in height [...] "
                "The fruit are large, pumpkin-shaped capsules, 3–5 cm (1–2 in) long, 5–8 cm (2–3 in) diameter, with 16 carpels arranged radially. "
                "Its seeds are flattened and about 2 cm (3⁄4 in) diameter. "
                "The capsules explode when ripe, splitting into segments and launching seeds at 70 m/s (250 km/h; 160 mph). [...] "
                "Another source states that seeds are thrown as far as 45 m (150 ft) from a tree, most commonly 30 m (100 ft). "
                "High-speed video analysis of its exploding fruit revealed that sandbox seeds fly with backspin as opposed to topspin, which had been previously assumed. "
                "Backspin helps seeds remain oriented to minimize their drag during flight. "
                "The trunk is covered in sharp spikes that grow to more than 1 inch (25 mm) long, and on mature trees may be so thick that the bases of the spines touch. "
                "The sap is milky and contains toxins, including huratoxin. "
                "It has been traditionally used as a fish poison (piscicide), arrow poison [...] "
                "In a time when most writing pens left wet ink on the page, the trees' unripe seed capsules were sawn in half to make decorative boxes (also called pounce pots) to hold the \"sand\" used to dry the ink, hence the name \"sandbox tree\".",
                nome="Hura crepitans"),
            wiki("Hura_crepitans",
                "Hura crepitans L. é uma árvore da família das euforbiáceas originária da Amazônia, de madeira aproveitável e cujo látex venenoso é usado para matar peixes em pesca fluvial, mais conhecida como açacu.",
                nome="Hura crepitans", idioma="pt"),
        ],
    },
    # 16 cafeína no néctar melhora a memória das abelhas
    {
        "temas_secundarios": ["cafe_cha_cacau", "insetos", "memoria"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "A cafeína também aparece no néctar das flores de café e de cítricos, e age como droga nas abelhas: num estudo, as que a provaram tiveram três vezes mais chance de lembrar o cheiro da flor.",
        "explicacao": (
            "Plantas produzem cafeína como defesa. No chá, por exemplo, ela fica guardada nas folhas, onde "
            "provavelmente desencoraja insetos que as mastigam e ajuda a barrar fungos. Mas a substância também "
            "aparece, em doses pequenas, no néctar de espécies de Coffea, o gênero do café, e de Citrus. Num estudo "
            "publicado na Science em 2013, uma equipe liderada pela Universidade de Newcastle, no Reino Unido, "
            "treinou abelhas a associar um cheiro floral a uma recompensa. As que receberam recompensa com "
            "cafeína tiveram três vezes mais chance de lembrar o cheiro do que as que receberam só açúcar. A "
            "cafeína bloqueia receptores de adenosina e reforça a resposta de neurônios dos chamados corpos "
            "pedunculados, envolvidos no aprendizado e na memória dos cheiros. Um detalhe importante: a "
            "concentração no néctar natural não passava do limiar em que as abelhas sentem o gosto amargo. Para os "
            "autores, isso indica que os polinizadores selecionam um néctar com efeito farmacológico, mas que não "
            "os afaste. Usando uma droga que fortalece a memória da recompensa, a planta faz as abelhas voltarem às "
            "suas flores e melhora seu sucesso reprodutivo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            resumo("23471406", "Caffeine in floral nectar enhances a pollinator's memory of reward (Science, 2013)",
                "Newcastle University [...] "
                "\"dateOfPublication\":\"2013 Mar\" [...] "
                "Plant defense compounds occur in floral nectar, but their ecological role is not well understood. "
                "We provide evidence that plant compounds pharmacologically alter pollinator behavior by enhancing their memory of reward. "
                "Honeybees rewarded with caffeine, which occurs naturally in nectar of Coffea and Citrus species, were three times as likely to remember a learned floral scent as were honeybees rewarded with sucrose alone. "
                "Caffeine potentiated responses of mushroom body neurons involved in olfactory learning and memory by acting as an adenosine receptor antagonist. "
                "Caffeine concentrations in nectar did not exceed the bees' bitter taste threshold, implying that pollinators impose selection for nectar that is pharmacologically active but not repellent. "
                "By using a drug to enhance memories of reward, plants secure pollinator fidelity and improve reproductive success."),
            wiki("Caffeine",
                "Caffeine is stored in tea leaves in two places. "
                "Firstly, in the cell vacuoles where it is complexed with polyphenols. "
                "This caffeine probably is released into the mouth parts of insects, to discourage herbivory. "
                "Secondly, around the vascular bundles, where it probably inhibits pathogenic fungi from entering and colonizing the vascular bundles.",
                nome="Caffeine"),
        ],
    },
]
