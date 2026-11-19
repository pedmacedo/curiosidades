LOTE = "2026-11-18-animais_extremos-01"
AREA = "biologia"
TEMA = "animais_extremos"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 tardígrados no espaço
    {
        "temas_secundarios": ["astrobiologia", "exploracao_espacial", "corpo_extremo"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Em 2007, tardígrados desidratados passaram 10 dias expostos ao vácuo do espaço. De volta à Terra, reidratados, os que só pegaram vácuo não mostraram efeito significativo nenhum.",
        "explicacao": (
            "Os tardígrados, ou ursos-d'água, são animais de cerca de meio milímetro, comuns em musgos e líquens. Quando o ambiente seca, eles perdem quase toda a água do corpo e entram num "
            "estado de vida suspensa em que podem passar anos. Nesse estado resistem a temperaturas de 272 graus "
            "negativos a 149 graus positivos, ao menos por pouco tempo, além de falta de oxigênio, vácuo, "
            "radiação e pressões altíssimas. Em 2007, a missão espacial FOTON-M3 levou 30 tardígrados e 30 ovos, "
            "todos desidratados, e os deixou expostos por 10 dias ao vácuo, em alguns casos também à luz "
            "ultravioleta do Sol. De volta à Terra, as amostras foram reidratadas para ver quem voltava à atividade "
            "e se os ovos se desenvolviam. A exposição só ao vácuo não teve efeito significativo em nenhuma das "
            "medidas. Já a combinação de vácuo com ultravioleta matou muitos deles."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Tardigrade",
            "Further, in that state they become highly resistant to environmental stresses, including temperatures from as low as −272 °C (−458 °F) to as much as +149 °C (300 °F) (at least for short periods of time), lack of oxygen, vacuum, ionising radiation, and high pressure. [...] "
            "Tardigrades have survived exposure to space. "
            "In 2007, samples of 30 tardigrades and 30 eggs, all dehydrated, were taken on the FOTON-M3 mission and exposed to vacuum, to both vacuum and UVA & B light, or to both vacuum and the full range of solar ultraviolet, for 10 days. "
            "Back on Earth, the samples were rehydrated to assess their activity, egg laying, and egg quality (viability). "
            "Vacuum exposure alone had no significant effect on any metric, but, when combined with UV exposure, killed many of the tuns. [...] "
            "Tardigrades are usually about 0.5 mm (0.02 in) long when fully grown. [...] "
            "Tardigrades are prevalent in mosses and lichens",
            nome="Tardigrade")],
    },
    # 2 o tubarão de quase 400 anos
    {
        "temas_secundarios": ["vida_marinha", "corpo_extremo"],
        "tipos_espanto": ["escala_absurda"],
        "gancho": "O tubarão-da-groenlândia é o vertebrado que mais vive: pelo menos 272 anos. Um deles foi estimado em cerca de 392 anos, e a espécie só se reproduz por volta dos 150.",
        "explicacao": (
            "O tubarão-da-groenlândia é um dos maiores tubarões que existem: pode "
            "passar de 6 metros e de uma tonelada, mas cresce devagar. Como saber a idade de um animal desses? "
            "Pesquisadores dataram, por radiocarbono, os cristais do cristalino dos olhos. As estimativas indicam que a espécie vive pelo menos 272 anos, o maior "
            "tempo de vida conhecido entre os vertebrados. O indivíduo mais velho foi estimado em 392 anos, com "
            "margem de erro de 120 anos para mais ou para menos. A lentidão vale para tudo: as fêmeas só atingem "
            "a maturidade sexual por volta dos 150 anos, quando passam de 4 metros, e a gestação é estimada entre "
            "8 e 18 anos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Greenland_shark",
            "They are among the largest extant shark species, reaching a maximum confirmed length of 6.4 m (21 ft) and weighing more than 1,000 kg (2,200 lb). "
            "They reach sexual maturity around 150 years of age and their pups are born alive after an estimated gestation period of 8 to 18 years. [...] "
            "The Greenland shark has the longest known lifespan of all vertebrates. "
            "It is estimated that the species has a lifespan of at least 272 years, with the oldest individual estimated to be 392 ± 120 years of age. "
            "Estimates of age were made using radiocarbon dating of crystals within the lenses of their eyes. "
            "Greenland sharks are estimated to reach sexual maturity around 150 years of age when females measure around 4.19 ± 0.04 m",
            nome="Greenland shark")],
    },
    # 3 a água-viva que volta a ser jovem
    {
        "temas_secundarios": ["vida_marinha", "desenvolvimento_humano", "evolucao"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Uma pequena água-viva, a Turritopsis dohrnii, consegue voltar ao estágio de pólipo depois de adulta, como se uma borboleta virasse lagarta de novo. Por isso é chamada de água-viva imortal.",
        "explicacao": (
            "Como outros hidrozoários, a Turritopsis dohrnii começa a vida como uma larva minúscula que nada "
            "livre. A larva se fixa no fundo e forma uma colônia de pólipos, que depois liberam águas-vivas, a "
            "fase adulta e sexualmente madura, que nada sozinha. Até aí, nada de especial. O estranho é o que "
            "acontece quando a água-viva adulta sofre algum estresse, é atacada, adoece ou envelhece: em vez de morrer, ela pode "
            "voltar inteira ao estágio de pólipo, imaturo e preso ao fundo, e recomeçar o ciclo. É um dos poucos "
            "casos conhecidos de animal capaz de reverter completamente a um estágio imaturo depois de atingir a "
            "maturidade sexual. Em tese, o ciclo pode se repetir sem fim, por isso ela é chamada de "
            "biologicamente imortal. Na prática, na natureza, a maioria morre comida por predadores ou por "
            "doenças."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Turritopsis_dohrnii",
            "Turritopsis dohrnii, commonly known as the immortal jellyfish, is a species of small, biologically immortal Medusozoa (jellyfish) found worldwide in temperate to tropic waters. "
            "It is one of the few known cases of an animal capable of completely reverting to a sexually immature, sedentary polyps colonial stage after having reached sexual maturity as a solitary individual. "
            "Like most other hydrozoans, T. dohrnii begin their lives as tiny, free-swimming larvae known as planulae. "
            "As a planula settles down, it gives rise to a colony of pol [...] "
            "If the T. dohrnii jellyfish is exposed to environmental stress, physical assault, or is sick or old, it can revert to the polyp stage, forming a new polyp colony. [...] "
            "Theoretically, this process can go on indefinitely, effectively rendering the jellyfish biologically immortal, although in practice individuals can still die. "
            "In nature, most Turritopsis dohrnii are likely to succumb to predation or disease in the medusa stage without reverting to the polyp form.",
            nome="Turritopsis dohrnii")],
    },
    # 4 o soco da tamarutaca
    {
        "temas_secundarios": ["vida_marinha", "biomimetica", "estados_materia"],
        "tipos_espanto": ["escala_absurda", "engenhosidade"],
        "gancho": "O camarão-louva-a-deus ataca com um apêndice que acelera a 10.400 g e chega a 83 km/h. O golpe é tão rápido que ferve a água: forma bolhas que, ao estourar, batem de novo na presa.",
        "explicacao": (
            "Os camarões-louva-a-deus, ou tamarutacas, são crustáceos marinhos com um par de apêndices "
            "especializados para atacar. Algumas espécies os usam como lança; outras, como a Odontodactylus "
            "scyllarus, como um martelo. O golpe parte do repouso com aceleração de 10.400 vezes a da gravidade e "
            "atinge 23 metros por segundo, uns 83 km/h. É tão rápido que a pressão da água entre o apêndice e o "
            "alvo cai a ponto de formar bolhas de vapor, o fenômeno chamado cavitação. Quando essas bolhas "
            "colapsam, produzem uma força adicional sobre a presa, além do impacto do próprio golpe, que chega a "
            "1.500 newtons. Ou seja, cada ataque atinge a vítima duas vezes: uma com o apêndice, outra com o "
            "colapso das bolhas. Com isso, a tamarutaca quebra conchas e pode ferir animais muito maiores que ela."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Mantis_shrimp",
            "can inflict serious damage on victims significantly greater in size than themselves. "
            "In Odontodactylus scyllarus, these two weapons are employed with blinding quickness, with an acceleration of 10,400 g (102,000 m/s2 or 335,000 ft/s2) and speeds of 23 m/s (83 km/h; 51 mph) from a standing start. "
            "Because they strike so rapidly, they generate vapor-filled bubbles in the water between the appendage and the striking surface—known as cavitation bubbles. "
            "The collapse of these cavitation bubbles produces measurable forces on their prey in addition to the instantaneous forces of 1,500 newtons that are caused by the impact of the appendage against the striking surface",
            nome="Mantis shrimp")],
    },
    # 5 a rã que congela
    {
        "temas_secundarios": ["corpo_extremo", "clima_tempo"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "No Alasca, a rã-da-floresta passa o inverno congelada: sem batimento cardíaco, sem respiração, sem atividade cerebral detectável. Fica assim cerca de 193 dias seguidos e, na primavera, volta à vida.",
        "explicacao": (
            "A rã-da-floresta vive na América do Norte, do sul dos Montes Apalaches até além do Círculo Polar "
            "Ártico; é a única rã norte-americana que chega tão ao norte. Para passar o inverno, ela fica perto da "
            "superfície do solo ou sob as folhas e deixa congelar o sangue e outros tecidos. Para sobreviver, "
            "prepara o corpo: acumula ureia e transforma grandes quantidades de glicogênio do fígado em glicose "
            "assim que o gelo começa a se formar. A ureia e a glicose funcionam como anticongelantes, limitando a "
            "quantidade de gelo e evitando que as células murchem demais. Enquanto está congelada, a rã não tem "
            "sinais vitais detectáveis: nem batimento, nem respiração, nem circulação, nem atividade cerebral. No "
            "Alasca, em hibernação natural, as rãs ficam congeladas por cerca de 193 dias consecutivos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Wood_frog",
            "It is the only North American frog that occurs north of the Arctic Ci [...] "
            "wood frogs can tolerate the freezing of their blood and other tissues. "
            "Urea is accumulated in tissues in preparation for overwintering, and liver glycogen is converted in large quantities to glucose in response to internal ice formation. "
            "Both urea and glucose act as cryoprotectants to limit the amount of ice that forms and to reduce osmotic shrinkage of cells. [...] "
            "wood frogs in Interior Alaska exhibit even greater tolerance, with some of their body water freezing while still surviving. "
            "When frozen, wood frogs have no detectable vital signs: no heartbeat, breathing, blood circulation, muscle movement, or detectable brain activity. "
            "Wood frogs in natural hibernation remain frozen for 193 +/- 11 consecutive days",
            nome="Wood frog")],
    },
    # 6 o voo sem escalas do maçarico
    {
        "temas_secundarios": ["comportamento_animal", "oceanografia"],
        "tipos_espanto": ["escala_absurda"],
        "gancho": "Em 2022, um jovem maçarico-de-bico-virado voou do Alasca à Tasmânia sem pousar: pelo menos 13.560 km em 11 dias. É o voo sem escalas mais longo já registrado de uma ave.",
        "explicacao": (
            "O maçarico-de-bico-virado é uma ave limícola que se reproduz na tundra, da Escandinávia ao Alasca, e "
            "passa o inverno em praias da Austrália e da Nova Zelândia. Uma das subespécies faz a travessia do "
            "Pacífico do Alasca à Nova Zelândia sem parar: é o voo sem escalas mais longo conhecido de qualquer "
            "ave, e a jornada mais longa de qualquer animal sem parar para comer. Ida e volta passam de 29 mil "
            "quilômetros. Em 2022, um jovem marcado com a etiqueta B6 saiu do Alasca em 13 de outubro e voou sem "
            "parar até a Tasmânia, uma rota nunca antes registrada para uma ave marcada. Percorreu pelo menos "
            "13.560 quilômetros em 11 dias e 1 hora, um recorde. Para aguentar, as aves dessa população acumulam "
            "muito mais gordura, em proporção ao corpo, do que as de outras subespécies."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Bar-tailed_godwit",
            "The migration of the subspecies Limosa lapponica baueri across the Pacific Ocean from Alaska to New Zealand is the longest known non-stop flight of any bird, and also the longest journey without pausing to feed by any animal. "
            "The round-trip migration for this subspecies is over 29,000 km (18,020 mi). [...] "
            "In 2022, a juvenile godwit flagged 'B6' left Alaska on 13 October and flew non-stop to Tasmania, the first time a tagged bird has flown this route. "
            "It flew a minimum of 13,560 km (8,430 mi) in 11 days 1 hour, a record non-stop distance. "
            "To fuel such long journeys, L. l. baueri birds in New Zealand deposit much more fat for their body size than other subspecies",
            nome="Bar-tailed godwit")],
    },
    # 7 o rato-toupeira-pelado sem oxigênio
    {
        "temas_secundarios": ["corpo_extremo", "microbioma"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "O rato-toupeira-pelado aguenta 18 minutos sem nenhum oxigênio sem sofrer danos aparentes. Nesse tempo, ele troca de combustível: passa a queimar frutose, como fazem as plantas.",
        "explicacao": (
            "O rato-toupeira-pelado é um roedor que cava túneis nas savanas secas do leste da África. Ele é estranho em muitos sentidos: quase não sente dor na pele, "
            "vive muito para um roedor e resiste ao câncer. Também resiste à falta de ar. Passa pelo menos cinco "
            "horas em ar com só 5% de oxigênio sem sinais de sofrimento, e numa atmosfera sem oxigênio nenhum "
            "sobrevive 18 minutos aparentemente sem danos, embora nenhum tenha resistido a um teste de 30 minutos. "
            "Durante esse período ele desmaia, o coração cai de cerca de 200 para 50 batimentos por minuto e a "
            "respiração para. O segredo parece ser a frutose: sem oxigênio, o animal passa a obter energia "
            "quebrando frutose, numa via que não é travada pela acidez que se acumula no corpo, como acontece com "
            "a glicose."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Naked_mole-rat",
            "The naked mole-rat is native to the drier parts of the tropical grasslands of East Africa [...] "
            "Naked mole-rats lack pain sensitivity in their skin, and have very low metabolic and respiratory rates. "
            "The animal is also remarkable for its longevity and resistance to cancer and oxygen deprivation. [...] "
            "survives for at least five hours in air that contains only 5% oxygen; it does not show any significant signs of distress and continues normal activity. [...] "
            "In zero-oxygen atmosphere, it can survive 18 minutes apparently without suffering any harm (but none survived a test of 30 minutes). "
            "During the anoxic period it loses consciousness, its heart rate drops from about 200 to 50 beats per minute, and breathing stops apart from sporadic breathing attempts. "
            "When deprived of oxygen, the animal uses fructose in its anaerobic glycolysis, producing lactic acid. "
            "This pathway is not inhibited by acidosis as happens with glycolysis of glucose.",
            nome="Naked mole-rat")],
    },
    # 8 o camarão-pistola e o flash de luz
    {
        "temas_secundarios": ["vida_marinha", "acustica", "luz_cores"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "O estalo da garra do camarão-pistola cria uma bolha que, ao colapsar, emite um flash de luz. Se a luz fosse térmica, a bolha teria de passar de 4.700 °C, quase a temperatura da superfície do Sol.",
        "explicacao": (
            "Os camarões-pistola, da família Alpheidae, têm uma garra maior que funciona como uma arma: uma parte "
            "se dobra para trás, como o cão de um revólver, e depois bate com força na outra. O movimento lança um "
            "jato de água tão rápido que forma uma bolha de cavitação, capaz de atordoar peixes maiores e até "
            "quebrar pequenos frascos de vidro. A bolha sai da garra a cerca de 90 km/h, e a pressão é suficiente "
            "para matar peixes pequenos, com um pico de 218 decibéis na água. Quando a bolha colapsa, ainda emite "
            "um breve flash de luz, um fenômeno chamado sonoluminescência. Se essa luz viesse do calor, a "
            "temperatura teria de passar de 5.000 kelvin, uns 4.700 °C; a superfície do Sol tem cerca de 5.500 °C. "
            "O flash é fraco demais para ser visto a olho nu."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Alpheidae",
            "When released, it snaps into the other part of the claw, emitting an enormously powerful wave of bubbles capable of stunning larger fish and breaking small glass jars. [...] "
            "As it ejects from the claw, the bubble reaches speeds of 25 m/s (90 km/h; 56 mph). "
            "The pressure is high enough to kill small fish. "
            "It corresponds to a peak pressure level of 218 decibels relative to one micropascal [...] "
            "snap can also produce sonoluminescence from the collapsing cavitation bubble. "
            "As it collapses, the cavitation bubble emits a short flash of light with a broad spectrum. "
            "If the light were of thermal origin, a temperature of the emitter over 5,000 K (4,700 °C) would be required. "
            "In comparison, the surface temperature of the Sun is estimated to be around 5,772 K (5,500 °C). "
            "The light is of lower intensity than the light produced by typical sonoluminescence, and is not visible to the naked eye.",
            nome="Alpheidae")],
    },
    # 9 rotíferos de 24 mil anos
    {
        "temas_secundarios": ["microbiologia", "paleontologia", "agua_doce_gelo"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Em 2021, cientistas reanimaram rotíferos, animais microscópicos, que estavam congelados havia 24 mil anos no permafrost da Sibéria. E esse grupo vive há mais de 25 milhões de anos sem sexo.",
        "explicacao": (
            "Os rotíferos bdeloides são animais microscópicos, de 0,15 a 0,7 milímetro, que vivem em água doce, "
            "musgos e solos úmidos. A olho nu, mal aparecem como pontinhos brancos. Eles têm duas características "
            "fora do comum. A primeira é a resistência: podem secar por completo em qualquer fase da vida e "
            "entrar num estado de dormência, voltando à atividade quando a água retorna. Em junho de 2021, "
            "biólogos relataram ter reanimado bdeloides que estavam congelados havia 24 mil anos no permafrost "
            "siberiano, o solo permanentemente gelado. A segunda é a reprodução: os bdeloides se reproduzem só por "
            "partenogênese, sem machos. São chamados de \"assexuados antigos\", porque fósseis indicam que vivem "
            "assim há mais de 25 milhões de anos, algo raríssimo entre os animais."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Bdelloidea",
            "exclusively parthenogenetic reproduction and the ability to survive in dry, harsh environments by entering a state of desiccation-induced dormancy (anhydrobiosis) at any life stage. "
            "They are often referred to as \"ancient asexuals\" due to their unique asexual history that spans back to over 25 million years ago through fossil evidence. "
            "Bdelloid rotifers are microscopic organisms, typically between 150 and 700 μm in length. "
            "Most are slightly too small to be seen with the naked eye, but appear as tiny white dots through even a weak hand lens, especially in bright light. "
            "In June 2021, biologists reported the restoration of bdelloid rotifers after being frozen for 24,000 years in the Siberian permafrost.",
            nome="Bdelloidea")],
    },
]
