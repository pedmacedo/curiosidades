LOTE = "2026-11-25-sono_ritmos-01"
AREA = "corpo_medicina"
TEMA = "sono_ritmos"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/", "fr": "https://fr.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


SPRINGER_CAVERNAS = "https://link.springer.com/article/10.1007/s40656-023-00571-w"
TITULO_CAVERNAS = "Timeless spaces: Field experiments in the physiological study of circadian rhythms, 1938-1963 (Hist Philos Life Sci, 2023)"


CANDIDATOS = [
    # 1 o "primeiro sono" e o "segundo sono"
    {
        "temas_secundarios": ["revolucao_industrial", "costumes_rituais"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Antes da luz elétrica, era comum dormir em dois turnos: um \"primeiro sono\", uma hora ou mais acordado no meio da noite e um \"segundo sono\". Um historiador juntou mais de 500 registros disso.",
        "explicacao": (
            "A tese é do historiador A. Roger Ekirch. Em documentos da Antiguidade, da Idade Média e da era "
            "moderna, ele reuniu mais de 500 menções a um sono partido: deitava-se cedo, acordava-se por volta "
            "da meia-noite e voltava-se para a cama mais tarde. O intervalo acordado servia para rezar, refletir, "
            "interpretar sonhos, escrever, visitar vizinhos, fazer sexo e até cometer pequenos furtos. Para "
            "Ekirch, a iluminação elétrica é o que explica o sumiço desse hábito. Um experimento de 1992 deu peso "
            "à ideia: o pesquisador Thomas Wehr deixou sete homens saudáveis, durante um mês, com 14 horas de "
            "escuro por dia. Depois de pagar a dívida de sono, eles passaram a dormir cerca de quatro horas, "
            "ficar duas ou três acordados e dormir mais umas quatro. O assunto não está encerrado: um estudo de "
            "2015 com três sociedades não industriais perto do equador encontrou sono noturno em um só bloco, "
            "e Ekirch contestou as conclusões. Também não há consenso de que voltar ao sono em dois turnos "
            "traga benefícios."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Segmented_sleep",
            "This pattern was common in preindustrial societies, and it was most common to sleep early (\"first sleep\"), wake around midnight, and return to bed later (\"second sleep\"). [...] "
            "Historian A. Roger Ekirch has argued that before the Industrial Revolution, interrupted sleep was dominant in Western civilization. "
            "Ekirch asserts that the intervening period of wakefulness was used to pray and reflect, and to interpret dreams, which were more vivid at that hour than upon waking in the morning. "
            "This was also a favorite time for scholars and poets to write uninterrupted, whereas still others visited neighbors, engaged in sexual activity, or committed petty crime. [...] "
            "Ekirch draws evidence from more than 500 references to a segmented sleeping pattern in documents from the ancient, medieval, and modern world. [...] "
            "Ekirch suggests that it is due to the modern use of electric lighting that most modern humans do not practice interrupted sleep. "
            "Some have proposed that a sleep pattern based on the historical biphasic sleep schedule might be beneficial, but there is no widespread agreement on this. "
            "A 2015 study of three non-industrial equatorial societies showed that all three experienced monophasic nighttime sleep, but the authors' conclusions were questioned by Ekirch. [...] "
            "In his 1992 study \"In short photoperiods, human sleep is biphasic\", Thomas Wehr had seven healthy men confined to a room for fourteen hours of darkness daily for a month. "
            "At first the participants slept for about eleven hours, presumably making up for their sleep debt. [...] "
            "They would sleep for about four hours, wake up for two to three hours, then go back to bed for another four hours.",
            nome="Polyphasic sleep (Segmented sleep)")],
    },
    # 2 Siffre perdeu 25 dias na caverna
    {
        "temas_secundarios": ["exploracao_espacial", "consciencia"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1962, um espeleólogo francês passou dois meses numa caverna sem relógio. Quando o avisaram de que o teste tinha acabado, em 14 de setembro, ele achava que ainda era 20 de agosto.",
        "explicacao": (
            "Michel Siffre tinha 23 anos e queria fazer a mais longa estadia subterrânea já registrada. Desceu em "
            "julho de 1962 ao abismo de Scarasson, nos Alpes Marítimos, entre a França e a Itália, uma cavidade "
            "glacial gelada e com risco de desabamentos. Levou consigo toda a comida e a água. Por um telefone, "
            "avisava a equipe na superfície cada vez que acordava e ia dormir, mas os colegas tinham ordem de "
            "não lhe dar nenhuma pista da hora lá fora. Sem sol nem relógio, seu ciclo foi escorregando cerca de "
            "meia hora por dia, como se o dia dele durasse umas 24 horas e meia. Pior: alguns períodos de sono "
            "que ele julgava ser cochilos eram noites inteiras, e assim ele perdeu a conta dos dias. Saiu depois "
            "de 63 dias convencido de que era 20 de agosto. Foi um choque. O trabalho chamou a atenção da NASA e "
            "do exército francês, e Siffre repetiu a experiência outras vezes, inclusive seis meses numa caverna "
            "do Texas em 1972."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Michel_Siffre",
                "Le temps psychologique ayant fortement évolué, à la fin de l'expérience, le 14 septembre, Michel Siffre pensait être le 20 août. "
                "En effet, certaines de ses périodes de sommeil n'étaient pas de simples siestes, comme il le croyait, mais de véritables nuits, ce qui l'avait amené à perdre totalement le compte des jours. "
                "De plus, les informations transmises en surface ont montré que ses cycles se décalaient chaque jour d'environ 30 minutes. "
                "Son horloge biologique faisait donc un tour complet en 24 heures et demie",
                nome="Michel Siffre (Wikipédia em francês)", idioma="fr"),
            {"url": SPRINGER_CAVERNAS, "titulo": TITULO_CAVERNAS, "idioma": "en",
             "trecho": "Scarasson was an unexplored glacial cavern with an internal temperature constantly below freezing and a serious risk of rock slides. [...] "
                       "by the young age of 23 had conceived the idea of carrying out the longest underground stay ever recorded. [...] "
                       "After sixty-three days underground, Siffre ‘lost’ two weeks of time as his body began to ‘free run’ – sliding in time, sleeping at progressively later and later hours, and eventually losing entire days. "
                       "The cave was integral to Siffre’s approach –he took care to remove any possible interference or influence from the outside world, even taking all of his food and water down with him, and using a one-way telephone system to allow daily check-ins with colleagues above ground. "
                       "His collaborators were under strict instructions to not give him any impression of the outside time until the experiment was over – which, when the time arrived, was a complete shock to Siffre."},
            wiki("Michel_Siffre",
                "in the abyss of Scarasson (Punta Marguareis) in the Maritime Alps between France and Italy. beginning July 1962. [...] "
                "In 1972, Siffre performed a more extensive underground experiment, staying six months in Midnight Cave in southern Texas. [...] "
                "NASA studied his work, as did the French Army and the US government.",
                nome="Michel Siffre"),
        ],
    },
    # 3 Kleitman e o dia de 28 horas na Mammoth Cave
    {
        "temas_secundarios": ["memoria", "historia_medicina"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 1938, o pai da pesquisa do sono passou 32 dias numa caverna dos EUA tentando viver dias de 28 horas. O corpo do assistente se adaptou. O dele, não. A queixa principal: lençóis úmidos.",
        "explicacao": (
            "O fisiologista Nathaniel Kleitman, da Universidade de Chicago, queria saber se o ritmo diário do "
            "corpo era fixo ou podia ser mudado. Para isso, precisava fugir da luz, da temperatura e da rotina "
            "da sociedade. Escolheu a Mammoth Cave, no Kentucky, onde a temperatura fica em cerca de 12 °C (54 °F), seja meio-dia ou meia-noite. "
            "Ele e o estudante de pós-graduação Bruce Richardson viveram ali num calendário inventado: dias de "
            "28 horas, marcados por despertador, e semanas de seis dias. O hotel próximo mandava duas refeições "
            "diárias em horários ajustados a esse calendário, e as visitas dos funcionários eram o único contato "
            "físico com o mundo. Os dois mediam a temperatura do corpo a cada duas horas. No fim, o ritmo de "
            "temperatura de Kleitman continuava praticamente igual, mas o de Richardson tinha se deslocado em "
            "direção ao dia de 28 horas. Kleitman concluiu que dormir e acordar era em parte um hábito, mais "
            "fácil ou mais difícil de mudar conforme fatores como a idade. A estadia foi confortável: aos "
            "jornalistas, os dois disseram que os únicos problemas eram a umidade dos lençóis e a falta de "
            "outro casal para jogar bridge."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": SPRINGER_CAVERNAS, "titulo": TITULO_CAVERNAS, "idioma": "en",
             "trecho": "Kentucky’s Mammoth Cave in 1938 [...] remains at exactly 54 degrees Fahrenheit whether it is noon or night [...] One hour of the 24 is precisely like any of the others, therefore he could ignore even the sun, turning night to day, and, what was more important, declare a 28-hour day, a six day week, and see if his sleeping mechanism would accept the novelty or go on strike’. [...] "
                       "The Mammoth Cave experiment aimed to test whether it was possible to modify the diurnal body rhythm temperature in two subjects – Kleitman himself and a graduate student assistant named Bruce Richardson. "
                       "To do so, Kleitman needed a space away from what he perceived to be the most important environmental time cues – light, temperature, and ‘society’ [...] "
                       "The experimental protocol consisted of living on an experimental 28-h day, with the researchers kept to schedule by an alarm clock. "
                       "Kleitman provided strict instructions to the nearby Mammoth Cave hotel for the provision of two meals a day [...] "
                       "These visits from the hotel staff were the researchers' only physical contact during their 32-day stay [...] "
                       "oral thermometers for temperature measurements taken every two hours [...] "
                       "At the end of the experiment, Kleitman determined that his temperature rhythms had stayed essentially the same but Richardson’s had moved towards the new 28-h schedule. "
                       "His conclusion was that patterns of sleeping and waking were a ‘habit’ that could be actively shifted – although how well depended on factors including age. [...] "
                       "Kleitman and Richardson’s stay in Mammoth Cave was relatively comfortable – the men remarking to journalists that the only drawback of their subterranean life was a ‘dampness to the sheets’ and the lack of another couple for bridge"},
            wiki("Nathaniel_Kleitman",
                "was an American physiologist and sleep researcher who served as Professor Emeritus in Physiology at the University of Chicago. "
                "He is recognized as the father of modern sleep research",
                nome="Nathaniel Kleitman"),
        ],
    },
    # 4 fragatas dormem em pleno voo
    {
        "temas_secundarios": ["comportamento_animal", "animais_extremos"],
        "tipos_espanto": ["engenhosidade", "escala_absurda"],
        "gancho": "Aves-fragata passam até 10 dias voando sobre o mar sem pousar. Medindo o cérebro delas em voo, cientistas viram que dormem no ar, em cochilos de uns 12 segundos, somando só 42 minutos por dia.",
        "explicacao": (
            "Já se suspeitava que aves dormissem voando, mas ninguém tinha registrado a atividade cerebral de "
            "uma ave em pleno voo longo. Num estudo publicado em 2016, pesquisadores prenderam pequenos aparelhos "
            "de eletroencefalograma na cabeça de fragatas-grandes que voavam sobre o Pacífico, a nordeste das Galápagos. Essas aves passam semanas sobre "
            "o oceano sem descansar na água: as asas compridas, os pés pouco palmados e as penas pouco "
            "impermeáveis dificultam decolar de novo. Os registros mostraram que elas dormem no ar, às vezes com "
            "um hemisfério do cérebro por vez, às vezes com os dois juntos. Dormem sobretudo enquanto sobem em "
            "círculos nas correntes de ar quente, e mantêm aberto o olho ligado ao hemisfério acordado, virado "
            "para a direção do voo. Os episódios de sono em voo duraram em média uns 12 segundos. O total foi de "
            "apenas 0,69 hora por dia, cerca de 42 minutos, ou 7,4% do que as mesmas aves dormem em terra. Para "
            "os autores, a necessidade de atenção durante o voo costuma falar mais alto do que o sono."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [{"url": "https://www.nature.com/articles/ncomms12468",
            "titulo": "Evidence that birds sleep in mid-flight (Nature Communications, 2016)", "idioma": "en",
            "trecho": "Published: 03 August 2016 [...] However, sleep has never been demonstrated in flying birds. "
                      "Here, using electroencephalogram recordings of great frigatebirds (Fregata minor) flying over the ocean for up to 10 days, we show that they can sleep with either one hemisphere at a time or both hemispheres simultaneously. "
                      "Also unexpectedly, frigatebirds sleep for only 0.69 h d−1 (7.4% of the time spent sleeping on land), indicating that ecological demands for attention usually exceed the attention afforded by sleeping unihemispherically. [...] "
                      "frigatebirds are not known to rest on the water despite spending weeks to months flying over the ocean [...] "
                      "Their long wings, poorly webbed feet and reduced feather waterproofing make taking off difficult [...] "
                      "Frigatebirds sleep mostly while circling in rising air currents and keep the eye connected to the awake hemisphere f [...] "
                      "than in flight (11.64±1.00 s [...] Most birds completed a roughly clockwise loop over the ocean north-east of the Galápagos Islands"},
            wiki("Unihemispheric_slow-wave_sleep",
                "Their sleep is more asymmetric in flight than on land, and they sleep mostly while circling air currents during flight. "
                "The eye connected to the awake hemisphere of their brain is the one facing the direction of flight.",
                nome="Unihemispheric slow-wave sleep"),
        ],
    },
    # 5 elefantes dormem duas horas
    {
        "temas_secundarios": ["comportamento_animal", "animais_extremos"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Duas elefantas selvagens monitoradas na África dormiram em média só 2 horas por dia, o menor sono já registrado num mamífero até então. Às vezes ficavam até 46 horas sem dormir.",
        "explicacao": (
            "Antes, o sono dos elefantes era conhecido sobretudo por animais de zoológico e circo, que pareciam "
            "dormir de três a seis horas por noite. Num estudo publicado em 2017, pesquisadores implantaram um "
            "pequeno sensor de movimento na tromba de duas matriarcas no Parque Nacional de Chobe e as "
            "acompanharam com coleira de GPS. Como a tromba quase nunca para, longos períodos de imobilidade "
            "dela indicavam sono. O resultado: cerca de 2 horas por dia, em vários blocos, quase sempre entre 2h "
            "e 6h da madrugada. Elas dormiam em pé e só se deitavam a cada três ou quatro dias, o que pode "
            "limitar o sono REM, que se supõe ocorrer quando o animal está deitado. Em cinco ocasiões passaram "
            "até 46 horas sem dormir, andando uns 30 km em 10 horas, talvez por causa de leões, caçadores ou "
            "um macho no cio, e não compensaram o sono perdido na noite seguinte. Uma ressalva: são só duas "
            "elefantas, e o sensor mede inatividade, não ondas cerebrais."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [{"url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0171903",
            "titulo": "Inactivity/sleep in two wild free-roaming African elephant matriarchs (PLOS ONE, 2017)", "idioma": "en",
            "trecho": "Published: March 1, 2017 [...] The current study provides details of sleep (or inactivity) in two wild, free-roaming African elephant matriarchs studied in their natural habitat with remote monitoring using an actiwatch subcutaneously implanted in the trunk, a standard elephant collar equipped with a GPS system and gyroscope [...] "
                      "We found that these two elephants were polyphasic sleepers, had an average daily total sleep time of 2 h, mostly between 02:00 and 06:00, and displayed the shortest daily sleep time of any mammal recorded to date. "
                      "Moreover, these two elephants exhibited both standing and recumbent sleep, but only exhibited recumbent sleep every third or fourth day, potentially limiting their ability to enter REM sleep on a daily basis. "
                      "In addition, we observed on five occasions that the elephants went without sleep for up to 46 h and traversed around 30 km in 10 h, possibly due to disturbances such as potential predation or poaching events, or a bull elephant in musth. "
                      "They exhibited no form of sleep rebound following a night without sleep. [...] "
                      "it has also been observed that elephants can sleep in a recumbent position, during which time REM (rapid eye movement) sleep is presumed to occur [...] "
                      "Thus, elephants appear to be polyphasic, mostly nocturnal sleepers, that appear to wake at around sunrise after approximately 3–6 hours of sleep each night [...] "
                      "In the Chobe National Park"}],
    },
    # 6 a água-viva que dorme sem cérebro
    {
        "temas_secundarios": ["vida_marinha", "evolucao"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Uma água-viva sem cérebro dorme: à noite, pulsa mais devagar, demora a reagir e, se for mantida acordada, compensa no dia seguinte. O sono parece ser mais antigo que o próprio cérebro.",
        "explicacao": (
            "A água-viva-de-cabeça-para-baixo, do gênero Cassiopea, vive no fundo de águas rasas com o corpo "
            "virado para cima, pulsando sem sair do lugar. Ela não tem sistema nervoso central, só uma rede de "
            "neurônios espalhada pelo corpo, com gânglios na borda. Mesmo assim, num estudo de 2017, ela cumpriu "
            "os três critérios usados para definir sono em animais. Primeiro, fica mais quieta à noite, com "
            "pulsação mais lenta, mas volta ao normal na hora se for estimulada. Segundo, nesse estado ela "
            "responde mais devagar a estímulos. Terceiro, se for privada desse repouso noturno, tem um período "
            "de compensação, com atividade mais baixa, no dia seguinte. Foi o primeiro animal sem sistema "
            "nervoso central em que se observou sono. Depois veio a hidra, um pólipo de água doce. Para os "
            "pesquisadores, isso indica que o sono surgiu antes dos sistemas nervosos centralizados e "
            "provavelmente tem uma função básica na manutenção dos neurônios."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Cassiopea",
                "and are unusual in that they appear to sleep despite lacking a brain. [...] "
                "They are the first animals lacking a central nervous system to have been observed sleeping.",
                nome="Cassiopea"),
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12305049/fullTextXML",
             "titulo": "Sleeping upside-down: Knockdown of a sleep-associated gene induces daytime sleep in the jellyfish Cassiopea (PNAS, 2025)",
             "idioma": "en",
             "trecho": "Nath R. D., et al. , The jellyfish Cassiopea exhibits a sleep-like state. Curr. Biol. 27, 2984–2990 (2017). [...] "
                       "Sleep across animals is defined by three behavioral criteria: reversible quiescence, homeostasis, and latency-to-arousal [...] "
                       "so sleep predates the emergence of centralized nervous systems, and likely serves a function in neural homeostasis. [...] "
                       "naturally orient upside-down on the shallow ocean floor [...] "
                       "1) They display quiescence, a slower pulse rate at night, that is rapidly reversible upon stimulation, 2) they respond slower to stimulation during sleep, evidence of increased latency-to-arousal, and 3) if deprived of this nighttime quiescence they experience a rebound, a compensatory low activity period, the following day (homeostasis). [...] "
                       "its distributed neural architecture [...] "
                       "exhibits sleep, behaviorally controlled by marginal ganglia."},
        ],
    },
    # 7 Konopka, o gene period e o Nobel que não viu
    {
        "temas_secundarios": ["genetica", "insetos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 1971, um estudante achou moscas mutantes com \"dias\" de 19 e de 29 horas: era o primeiro gene do relógio biológico. Ele perdeu o emprego, deixou a ciência, e o achado levou a um Nobel em 2017.",
        "explicacao": (
            "Ronald Konopka era aluno de pós-graduação no laboratório de Seymour Benzer, no Caltech. Usando um "
            "produto químico que provoca mutações, ele procurou moscas-das-frutas com o relógio interno "
            "alterado e achou três: uma sem ritmo nenhum, outra com ciclo de 19 horas e outra com ciclo de 29 "
            "horas, quando o normal é perto de 24. As três mutações estavam no mesmo gene, que ele batizou de "
            "period. Foi a primeira prova de que um gene determina o ritmo de um comportamento. Konopka ganhou "
            "um cargo de professor no Caltech em 1975, mas os colegas criticavam sua relutância em publicar, e "
            "ele não foi efetivado. Na Universidade Clarkson, a história se repetiu, e ele abandonou a ciência. "
            "Morreu em 2015. Dois anos depois, Jeffrey Hall, Michael Rosbash e Michael Young ganharam o Nobel "
            "de Medicina pelos mecanismos moleculares do relógio circadiano, trabalho construído sobre o gene "
            "que Konopka descobriu."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Ronald_J._Konopka",
                "Ronald J. Konopka (1947–2015) was an American geneticist who studied chronobiology. "
                "He made his most notable contribution to the field while working with Drosophila in the lab of Seymour Benzer at the California Institute of Technology. [...] "
                "In 1975, following his discovery of the period mutants, Konopka was awarded a faculty position at the California Institute of Technology. "
                "While there, Konopka's colleagues were critical of his reluctance to publish his work on the period gene, and Konopka was denied tenure. "
                "After his stay at Caltech, Konopka accepted a position at Clarkson University but was again denied tenure and subsequently exited the field of science. [...] "
                "Konopka's discovery and genetic analysis of period and several other circadian rhythm mutations became the basis of the research done by  Drs. Jeffrey C. Hall, Michael Rosbash, and Michael W. Young, who were awarded the 2017 Nobel Prize in Physiology or Medicine. [...] "
                "As a graduate student in Seymour Benzer's lab [...] "
                "He used ethyl methanesulfonate (EMS) to induce point mutations in the Drosophila melanogaster genome, and eventually isolated three mutants with abnormal rhythms in eclosion. [...] "
                "These mutations were alternative alleles of a gene that Konopka subsequently named period. "
                "While wild type flies have a circadian period around 24 hours, Konopka found the per01 mutant was arrhythmic, the perS mutant had a period of 19 hours, and the perL had a period of 29 hours.",
                nome="Ronald J. Konopka"),
            wiki("Circadian_rhythm",
                "Ron Konopka and Seymour Benzer identified the first clock mutation in Drosophila in 1971, naming the gene \"period\" (per) gene, the first discovered genetic determinant of behavioral rhythmicity. [...] "
                "In 2017, Jeffrey C. Hall, Michael W. Young, and Michael Rosbash were awarded Nobel Prize in Physiology or Medicine \"for their discoveries of molecular mechanisms controlling the circadian rhythm\".",
                nome="Circadian rhythm"),
        ],
    },
    # 8 a família que dorme às 19h30
    {
        "temas_secundarios": ["genetica", "insetos"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Há famílias cujo relógio biológico corre adiantado: dormem por volta das 19h30 e acordam às 4h30. Em uma delas, a causa era uma mutação num parente humano do gene do relógio das moscas.",
        "explicacao": (
            "A condição se chama síndrome familiar do avanço de fase do sono. Quem a tem adormece e acorda de "
            "4 a 6 horas antes da média, e o ritmo interno, medido pela melatonina no sangue e pela temperatura "
            "do corpo, fica adiantado de 3 a 4 horas. Em 1999, o pesquisador Louis Ptáček, na Universidade de "
            "Utah, deu nome ao quadro depois de examinar uma paciente com sono incapacitante no começo da noite "
            "e despertar de madrugada, sintomas que se repetiam nos parentes. Nas famílias estudadas, a herança "
            "é dominante: cerca de metade dos parentes diretos é afetada. Em 2001, os grupos de Ptáček e de "
            "Ying-Hui Fu acharam numa família uma mutação no gene PER2, um dos três parentes, nos mamíferos, do "
            "gene period descoberto décadas antes em moscas-das-frutas. Foi a primeira doença humana "
            "ligada diretamente a um gene central do relógio. Outras famílias têm mutações em outros genes, como "
            "o da enzima CK1 delta."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Familial_advanced_sleep_phase_syndrome",
            "A genetic basis has been demonstrated in one form of ASPD, familial advanced sleep phase syndrome (FASPS), which implicates missense mutations in genes hPER2 and CKIdelta in producing the advanced sleep phase phenotype. [...] "
            "Individuals with FASPS fall asleep and wake up 4–6 hours earlier than the average population, generally sleeping from 7:30pm to 4:30am. [...] "
            "Studies of affected lineages have found that approximately 50% of directly related family members experience the symptoms of FASPS, which is an autosomal dominant trait. [...] "
            "In 1999, Louis Ptáček conducted a study at the University of Utah in which he coined the term familial advanced sleep phase disorder after identifying individuals with a genetic basis for an advanced sleep phase. "
            "The first patient evaluated during the study reported \"disabling early evening sleepiness\" and \"early morning awakening\"; similar symptoms were also reported in her family members. [...] "
            "these rhythms were both phase-advanced by 3–4 hours in FASPS subjects compared with control subjects. [...] "
            "In 2001, the research groups of Ptáček and Ying-Hui Fu published a genetic analysis of subjects experiencing the advanced sleep phase, implicating a mutation in the CK1-binding region of PER2 in producing the FASPS behavioral phenotype. "
            "FASPS is the first disorder to link known core clock genes directly with human circadian sleep disorders. [...] "
            "Period2 (Per2) which is a mammalian gene sufficient for the maintenance of circadian rhythms.",
            nome="Familial advanced sleep phase syndrome"),
            wiki("Period_(gene)",
                "The period gene and three mutants (perS, perL, and per0) were isolated in an EMS mutagenesis screen by Ronald Konopka and Seymour Benzer in 1971. [...] "
                "In mammals, there are three known PER family genes: PER1, PER2, and PER3.",
                nome="Period (gene)"),
        ],
    },
    # 9 o "gene do sono curto" que não se confirmou
    {
        "temas_secundarios": ["genetica", "desenvolvimento_humano"],
        "tipos_espanto": ["mito_desmentido", "misterio_aberto"],
        "gancho": "Há pessoas que dormem 4 a 6 horas por noite a vida toda e acordam descansadas. Achou-se que mutações raras explicavam isso, mas outros portadores das mesmas mutações dormem o normal.",
        "explicacao": (
            "O traço se chama sono curto natural familiar. Quem o tem dorme bem menos que a média sem sentir "
            "sono de dia nem os efeitos de privação que uma pessoa comum sentiria. Não é tratado como doença, e "
            "não se conhecem efeitos nocivos à saúde. Em famílias com o traço, o laboratório da geneticista "
            "Ying-Hui Fu apontou mutações em genes como DEC2, ADRB1, NPSR1 e GRM1 como causa, e a explicação se "
            "espalhou. Só que pesquisas posteriores em grandes bancos de dados genéticos mostraram que outras "
            "pessoas com essas mutações, ou com mutações fortes nos mesmos genes, não dormem menos. Isso indica "
            "que o sono curto das famílias estudadas tinha outra base, ainda não identificada. Os estudos "
            "genômicos amplos sugerem que a duração do sono depende de muitos genes, cada um com efeito pequeno. "
            "O maior efeito de uma variante comum achado até agora, no gene PAX8, muda o sono em pouco mais de "
            "3 minutos."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Familial_natural_short_sleep",
            "Familial natural short sleep is a rare, genetic, typically inherited trait where an individual sleeps for fewer hours than average without suffering from daytime sleepiness or other consequences of sleep deprivation. [...] "
            "This sleep type is not considered to be a genetic disorder nor are there any known harmful effects to overall health associated with it [...] "
            "usually 4 to 6 hours (less than the average sleeptime of 8 hours) each night while waking up feeling relatively well-rested [...] "
            "This condition is life-long [...] "
            "Early research, particularly from the lab of Ying-Hui Fu, named several mutations as causing heritable short sleep in studied families. "
            "These mutations implicated the genes DEC2/BHLHE41, ADRB1, NPSR1, and GRM1. "
            "However, subsequent biobank research showed that other carriers of these mutations or of different high-impact mutations in the same genes do not exhibit any reduction in sleep duration. "
            "This indicates that the short sleeper phenotype in the original case reports had a different basis. "
            "Current genome-wide association studies suggest that sleep behaviors such as sleep length are highly polygenic, with most heritability explained by variants with small effects. "
            "The largest non-pathogenic genetic effect on sleep duration found to date is a change of 2.44 or 3.24 minutes associated with variation in the PAX8 gene.",
            nome="Familial natural short sleep")],
    },
    # 10 De Mairan e a planta que "sentia o Sol sem vê-lo"
    {
        "temas_secundarios": ["plantas", "revolucao_cientifica"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "A ciência dos relógios biológicos começou em 1729, com um cientista francês que trancou uma planta no escuro: as folhas seguiram abrindo de dia e fechando à noite. Ele achou que ela \"sentia o Sol\".",
        "explicacao": (
            "Jean-Jacques d'Ortous de Mairan era um filósofo natural que trabalhava com astronomia e propôs que "
            "as auroras boreais eram causadas pelo Sol. Intrigado com uma planta que abria as folhas de dia e as "
            "fechava à noite, ele a deixou em escuridão constante e anotou o que acontecia. O movimento diário "
            "continuou mesmo sem luz. Foi o primeiro experimento feito para separar um relógio interno de uma "
            "simples resposta aos estímulos do dia. Mas De Mairan não concluiu que a planta tinha um relógio: "
            "achou que ela era capaz de \"sentir o Sol sem nunca vê-lo\". Ele mesmo não publicou o resultado, "
            "que foi apresentado por um colega, Jean Marchant, algo comum numa época de viagens lentas. Quase "
            "um século depois, em 1823, o botânico suíço Augustin Pyramus de Candolle mediu o ritmo das folhas "
            "da planta Mimosa pudica em condições constantes e encontrou ciclos de 22 a 23 horas. Um ciclo que não bate com o "
            "dia de 24 horas foi provavelmente a primeira pista de que o ritmo vinha de dentro: hoje se sabe que "
            "relógios assim existem em praticamente todos os seres vivos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Jean-Jacques_d%27Ortous_de_Mairan",
                "was a French natural philosopher (physicist) [...] "
                "made key discoveries in a variety of fields, including ancient texts and astronomy. [...] "
                "he put up a novel hypothesis that the Northern Lights are caused by the Sun [...] "
                "He was intrigued by the daily opening and closing of the heliotrope plant and performed a simple experiment where he exposed the plants to constant darkness and recorded the behaviour. "
                "De Mairan's key conclusion was that the daily rhythmic opening and closing of the leaves persisted even in the absence of sunlight. "
                "However, de Mairan did not infer that heliotropes have internal clocks driving leaf rhythms, but rather that they were able \"to sense the Sun without ever seeing it\". [...] "
                "These results may have gone unnoticed had his colleague, Jean Marchant, not published them for de Mairan. "
                "It was quite common at the time, when travel was slow, for one scientist to present the work of another. [...] "
                "In 1823, almost a century after de Mairan's work, the Swiss botanist Augustin Pyramus de Candolle expanded on it by measuring the free-running period of Mimosa pudica leaf movements in constant conditions, finding them to be 22–23 hours long. "
                "This was probably the first hint of what is now called the circadian (from Latin circa, about, and dies) nature of such endogenous rhythms, found in practically all living organisms",
                nome="Jean-Jacques d'Ortous de Mairan"),
            wiki("Circadian_rhythm",
                "In 1729, French scientist Jean-Jacques d'Ortous de Mairan conducted the first experiment designed to distinguish an endogenous clock from responses to daily stimuli.",
                nome="Circadian rhythm"),
        ],
    },
    # 11 pesadelo era paralisia do sono
    {
        "temas_secundarios": ["palavras_viajantes", "cultura_popular"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "\"Nightmare\", pesadelo em inglês, vem da \"mare\", um demônio que sentava no peito de quem dormia. A palavra nasceu para a paralisia do sono, e o Brasil tem sua versão: a Pisadeira.",
        "explicacao": (
            "Na paralisia do sono, a pessoa acorda consciente mas não consegue se mexer, porque o corpo ainda "
            "está no modo do sono REM. Muitas vezes vem junto uma sensação de peso no peito e a impressão de "
            "uma presença no quarto. O folclore europeu explicava isso com a \"mare\", entidade feminina que "
            "montava no peito dos adormecidos, e daí vem o inglês \"nightmare\", sem ligação conhecida com a "
            "palavra inglesa para égua, também \"mare\". De início, a palavra se referia especificamente a essa "
            "experiência, e em 1829 já tinha passado a significar qualquer sonho ruim. Outras línguas fizeram o "
            "mesmo caminho a partir da ideia de pressão: o francês \"cauchemar\" vem de um verbo antigo que "
            "significa pressionar, e o espanhol \"pesadilla\" vem de \"pesada\". O português \"pesadelo\" também "
            "deriva de \"pesado\". No Brasil, sobretudo em São Paulo e parte de Minas Gerais, a figura é a "
            "Pisadeira, mulher magra de unhas compridas que desce do telhado e pisa no peito de quem foi dormir "
            "de barriga cheia. Na Terra Nova, no Canadá, é a \"Old Hag\", a bruxa velha."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Nightmare",
                "The word nightmare is derived from the European folklorical \"mare\" (cf.  Old English: mare, mære, Old Norse: mara), a mythological female demon or thereof, which sits on the chest of sleeping people and brings on frightening dreams. "
                "The term has no known etymological connection with the Modern English word for a female horse [...] "
                "Originally, \"mare\" or \"nightmare\" referred more specifically to sleep paralysis, in which an experience of terror and paralysis during sleep can be associated with a sense of pressure on the chest and the dreamed presence of entities often pictured as demons, sometimes sitting on the chest. [...] "
                "The meaning of \"nightmare\" had generalized from sleep paralysis to any bad dream by 1829. "
                "In other languages, the word for \"bad dream\" similarly evolved in sense from words for \"sleep paralysis,\" often with senses related to the pressure on the chest. "
                "For example, French cauchemar (the first element from old French chauchier \"to press, trample,\" the second related to \"mare\"); Spanish pesadilla, from pesada \"weight\"",
                nome="Nightmare"),
            wiki("Pisadeira_(folclore)",
                "Pisadeira ou pesadeira é um mito brasileiro que ocorre principalmente no estado de São Paulo e parte de Minas Gerais. [...] "
                "Essa lenda pode ser associada com a paralisia do sono. [...] "
                "Geralmente é descrita como uma mulher muito magra, com dedos compridos e secos, unhas enormes [...] "
                "Vive pelos telhados, sempre à espreita. "
                "Quando uma pessoa janta e vai dormir com o estômago cheio, deitando-se de barriga para cima, a pisadeira entra em ação. "
                "Ela desce de seu esconderijo e senta-se ou pisa fortemente sobre o peito da vítima",
                nome="Pisadeira (folclore)", idioma="pt"),
            wiki("Sleep_paralysis",
                "The underlying mechanism is believed to involve a dysfunction in REM sleep. [...] "
                "If the effects of sleep \"on\" neural populations cannot be counteracted, characteristics of REM sleep are retained upon awakening. [...] "
                "In Newfoundland, which is in eastern Canada, sleep paralysis is referred to as the Old Hag",
                nome="Sleep paralysis"),
            {"url": "https://pt.wiktionary.org/wiki/pesadelo", "titulo": "pesadelo (Wikcionário)", "idioma": "pt",
             "trecho": "(Morfologia) pesado + -elo."},
        ],
    },
    # 12 cegos cujo relógio ainda vê a luz
    {
        "temas_secundarios": ["sentidos", "anatomia"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Alguns cegos sem nenhum cone ou bastonete funcionando ainda têm o relógio biológico acertado pela luz. O olho tem um terceiro tipo de célula sensível à luz, que não serve para enxergar.",
        "explicacao": (
            "Por muito tempo se pensou que só os cones e os bastonetes captavam luz no olho. A primeira pista do "
            "contrário veio de camundongos cegos criados por acaso no começo do século XX: as pupilas deles "
            "ainda reagiam à luz. Em 1991, Russell Foster e colegas mostraram que roedores sem cones e "
            "bastonetes continuavam acertando o relógio interno pela luz. O responsável é um pequeno grupo de "
            "células ganglionares da retina, cerca de 1% delas, que contêm uma proteína sensível à luz azul, a "
            "melanopsina. Elas reagem mais devagar que cones e bastonetes e sinalizam a presença de luz de forma "
            "prolongada, e participam do controle da melatonina e do reflexo da pupila. Em 2007, um estudo com pessoas sem cones nem "
            "bastonetes mostrou que elas mantinham as respostas normais à luz que não dependem da visão. Isso "
            "ajuda a entender por que o distúrbio de sono fora das 24 horas, em que o relógio vai se atrasando "
            "dia após dia, atinge até 70% dos totalmente cegos, mas é raro entre pessoas com baixa visão que "
            "ainda percebem alguma luz."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Intrinsically_photosensitive_retinal_ganglion_cells",
                "Therefore, they constitute a third class of photoreceptors, in addition to rod and cone cells. [...] "
                "Compared to the rods and cones, the ipRGCs respond more sluggishly and signal the presence of light over the long term. "
                "They represent a very small subset (~1%) of the retinal ganglion cells. [...] "
                "They contribute to photic regulation and acute photic suppression of release of the hormone melatonin. [...] "
                "In 2007, Zaidi and colleagues published their work on rodless, coneless humans, showing that these people retain normal responses to nonvisual effects of light. [...] "
                "Clyde E. Keeler observed that the pupils in the eyes of blind mice he had accidentally bred still responded to light. [...] "
                "Research continued in 1991, when Russell G. Foster and colleagues, including Ignacio Provencio, showed that rods and cones were not necessary for photoentrainment, the visual drive of the circadian rhythm [...] "
                "melanopsin, is excited by light mainly in the blue portion of the visible spectrum",
                nome="Intrinsically photosensitive retinal ganglion cells"),
            wiki("Non-24-hour_sleep%E2%80%93wake_disorder",
                "Although this sleep disorder is more common in blind people, affecting up to 70% of the totally blind, it can also affect sighted people. [...] "
                "Non-24 is rare among visually impaired patients who retain at least some light perception. [...] "
                "For example, an individual with a circadian period of 24.5 hours would drift 30 minutes later each day",
                nome="Non-24-hour sleep–wake disorder"),
        ],
    },
    # 13 cães narcolépticos e a orexina
    {
        "temas_secundarios": ["neurociencia", "domesticacao"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "Dobermanns que desabavam de repente quando ficavam empolgados com comida ajudaram a desvendar a narcolepsia humana: o problema estava numa molécula do cérebro descoberta só em 1998.",
        "explicacao": (
            "Na narcolepsia, a pessoa tem sono excessivo de dia e, no tipo 1, em geral crises de cataplexia: "
            "uma perda súbita do tônus dos músculos, disparada por emoções fortes como o riso, durante a qual ela "
            "continua consciente. Cães também podem ter a doença. Em dobermanns e labradores, ela aparece com "
            "cataplexia forte em resposta à comida e ao contato com pessoas ou outros animais. A partir de 1990, "
            "o pesquisador Emmanuel Mignot, em Stanford, buscou o gene responsável nesses cães. Enquanto isso, "
            "em 1998, dois grupos independentes descobriram no cérebro de ratos uma nova molécula, que um "
            "batizou de orexina, de \"apetite\" em grego, e o outro de hipocretina. As duas linhas se "
            "encontraram: a narcolepsia canina era causada por uma mutação no receptor 2 dessa molécula, e "
            "camundongos sem o gene da orexina também ficavam narcolépticos. Na narcolepsia humana, a principal "
            "hipótese é uma destruição pelo sistema imune dos neurônios que fabricam orexina. A molécula se "
            "revelou importante para estabilizar a vigília e o sono."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Narcolepsy",
                "Typical cataplexy is triggered by sudden emotional reactions such as laughter, other positive emotions, anger or surprise. "
                "The person remains conscious throughout the episode. [...] "
                "Cataplexy appears as transient episodes of aberrant muscle tone (typically loss of muscle tone) triggered by strong emotion. [...] "
                "Narcolepsy with cataplexy was identified in breeds including Labrador retrievers and Doberman pinschers [...] "
                "The animals affected exhibited excessive daytime sleepiness with a reduced state of vigilance, and severe cataplexy in response to food and interactions with humans or other animals. [...] "
                "Dogs (and other species including cats and horses) can exhibit spontaneous narcolepsy with symptoms similar to those in humans, and can involve partial or full collapse. [...] "
                "Narcolepsy type 1 features EDS with either cataplexy or cerebrospinal fluid (CSF) orexin levels of less th [...] "
                "A leading consideration for the cause of narcolepsy type 1 is that it is an autoimmune disorder.",
                nome="Narcolepsy"),
            wiki("Orexin",
                "Orexin was discovered in 1998 almost simultaneously by two independent groups of researchers working on the rat brain. "
                "One group named it orexin, from orexis, meaning \"appetite\" in Greek; the other group named it hypocretin [...] "
                "appear to play an important role in stabilizing wakefulness and sleep. "
                "The discovery that an orexin receptor mutation causes the sleep disorder canine narcolepsy in Doberman Pinschers  subsequently indicated a major role for this system in sleep regulation. "
                "Genetic knockout mice lacking the gene for orexin were also reported to exhibit narcolepsy.",
                nome="Orexin"),
            wiki("Emmanuel_Mignot",
                "He is the Craig Reynolds Professor of Sleep Medicine at Stanford Medical School [...] Starting in 1990, he isolated the gene causing canine narcolepsy in doberman and Labrador dogs. "
                "Ten years later, this led to the discovery that mutations in the hypocretin (orexin) receptor 2 cause canine narcolepsy, and that human narcolepsy was caused by an immune mediated destruction of the hypocretin (orexin) producing cells in the br",
                nome="Emmanuel Mignot"),
        ],
    },
    # 14 equipes da NASA vivendo no horário de Marte
    {
        "temas_secundarios": ["exploracao_espacial", "medidas_padroes"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Em várias missões de robôs em Marte, as equipes da NASA trabalharam no horário marciano: como o dia lá tem quase 40 minutos a mais, o expediente começava cada dia mais tarde.",
        "explicacao": (
            "O dia solar de Marte, chamado sol, dura 24 horas, 39 minutos e 35 segundos, cerca de 2,75% a mais "
            "que o da Terra. O termo foi adotado no projeto Viking, em 1976, para não confundir com o dia "
            "terrestre. Os robôs que pousam lá dependem do Sol: precisam de luz para os painéis solares, e a "
            "temperatura sobe e cai depressa. Por isso, nas missões Mars Pathfinder, Spirit e Opportunity, "
            "Phoenix e Curiosity, as equipes de operação trabalharam no \"horário de Marte\", com o expediente "
            "sincronizado com a hora local no ponto de pouso. Na prática, a jornada de trabalho escorregava uns 40 "
            "minutos mais tarde a cada dia no relógio da Terra, e o turno dava a volta no relógio. Muitos integrantes da equipe dos jipes Spirit e Opportunity usavam "
            "relógios de pulso acertados no tempo marciano. A solução para usar programas comuns foi um relógio "
            "de 24 \"horas\" em que horas, minutos e segundos são 2,75% mais longos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Timekeeping_on_Mars",
            "the length of its solar day is 24 h 39 m 35.244 s [...] "
            "thus, Mars's solar day is only about 2.75% longer than Earth's [...] "
            "The term \"sol\" is used by planetary scientists to refer to the duration of a solar day on Mars. "
            "The term was adopted during NASA's Viking project (1976) in order to avoid confusion with an Earth \"day\". [...] "
            "using a 24-hour \"Mars clock\" on which the hours, minutes and seconds are 2.75% longer than their standard (Earth) durations. "
            "This has the advantage that no handling of times greater than 23:59 is needed, so standard tools can be used. [...] "
            "For the Mars Pathfinder, Mars Exploration Rover (MER), Phoenix, and Mars Science Laboratory missions, the operations teams have worked on \"Mars time\", with a work schedule synchronized to the local time at the landing site on Mars, rather than the Earth day. "
            "This results in the crew's schedule sliding approximately 40 minutes later in Earth time each day. "
            "Wristwatches calibrated in Martian time, rather than Earth time, were used by many of the MER team members. "
            "Local solar time has a significant impact on planning the daily activities of Mars landers. "
            "Daylight is needed for the solar panels of landed spacecraft. Its temperature rises and falls rapidly",
            nome="Timekeeping on Mars")],
    },
    # 15 o sono "lava" o cérebro? A disputa
    {
        "temas_secundarios": ["neurociencia", "memoria"],
        "tipos_espanto": ["misterio_aberto", "contraintuitivo"],
        "gancho": "Ficou famosa a ideia de que o sono \"lava\" o cérebro, removendo resíduos. Em 2024, um estudo com camundongos achou o oposto: a limpeza diminuía durante o sono. A disputa segue aberta.",
        "explicacao": (
            "O ponto de partida é o sistema glinfático, uma rede de vias por onde o líquido que banha o cérebro "
            "corre em volta dos vasos sanguíneos, com a ajuda de células chamadas astrócitos, e leva embora "
            "restos do metabolismo. Um estudo de 2013 na revista Science, com camundongos, concluiu que essa "
            "limpeza aumenta no sono profundo, quando o espaço entre as células se expande. A ideia foi "
            "atraente porque parecia explicar para que serve o sono e sugeria que dormir mal por anos poderia "
            "piorar, ou até causar, o Alzheimer. Mas o assunto sempre teve resultados a favor e contra. Em 2024, "
            "outro grupo mediu diretamente o movimento de um corante fluorescente no "
            "cérebro de camundongos acordados, dormindo e anestesiados. O movimento não mudou com o estado de "
            "vigília, e a eliminação do corante foi bem menor, e não maior, durante o sono e a anestesia. Em "
            "2025, a mesma revista publicou uma contestação ao estudo e a resposta dos autores. Por enquanto, "
            "para que serve o sono continua um mistério."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": "https://www.nature.com/articles/s41593-024-01638-y",
             "titulo": "Brain clearance is reduced during sleep and anesthesia (Nature Neuroscience, 2024)", "idioma": "en",
             "trecho": "Published: 13 May 2024 [...] Matters Arising to this article was published on 11 March 2025 [...] "
                       "It has been suggested that the function of sleep is to actively clear metabolites and toxins from the brain. "
                       "Enhanced clearance is also said to occur during anesthesia. "
                       "Here, we measure clearance and movement of fluorescent molecules in the brains of male mice and show that movement is, in fact, independent of sleep and wake or anesthesia. "
                       "Moreover, we show that brain clearance is markedly reduced, not increased, during sleep and anesthesia. [...] "
                       "However, what this is remains a mystery. "
                       "One suggestion is that sleep clears the brain of metabolites and toxins using the ‘glymphatic’ system, a process that cannot operate efficiently during the waking state [...] "
                       "For example, diminished toxin clearance brought about by chronically poor sleep might exacerbate, if not cause, Alzheimer disease [...] "
                       "However, whether sleep does enhance clearance by increased bulk flow is unresolved, with findings both supporting [...] "
                       "Xie, L. et al. Sleep drives metabolite clearance from the adult brain. Science 342, 373–377 (2013). [...] "
                       "Reply to: A curious concept of CNS clearance"},
            wiki("Glymphatic_system",
                "The glymphatic system, glymphatic clearance pathway, or paravascular system is an organ system for removing metabolic waste from the vertebrate central nervous system (CNS). [...] "
                "Clearance of soluble proteins, metabolites, and excess extracellular fluid is accomplished through convective bulk flow, facilitated by astrocytic aquaporin 4 water channels. [...] "
                "During slow-wave sleep, clearance of interstitial solutes increases by expansion and contraction of the extracellular space",
                nome="Glymphatic system"),
        ],
    },
    # 16 Aserinsky, o REM e a ironia final
    {
        "temas_secundarios": ["consciencia", "historia_medicina"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "O sono REM só foi descoberto em 1953, por um estudante que passava horas olhando pálpebras de gente dormindo. Em 1998, ele morreu num acidente de carro que pode ter sido causado por um cochilo ao volante.",
        "explicacao": (
            "Eugene Aserinsky era aluno de pós-graduação de Nathaniel Kleitman na Universidade de Chicago. Ligou "
            "voluntários adormecidos a uma versão antiga do eletroencefalógrafo, que rabiscava cerca de 800 "
            "metros de papel por noite, e notou que, várias vezes a cada noite, os olhos deles disparavam de um "
            "lado para o outro. Kleitman insistiu em repetir o experimento, desta vez com a própria filha, "
            "Esther. Em 1953, os dois apresentaram ao mundo o sono de movimentos rápidos dos olhos, o REM, e "
            "mostraram que ele estava ligado aos sonhos e a mais atividade no cérebro. William Dement, outro "
            "aluno de Kleitman, diria que naquele ano o estudo do sono virou um campo científico de verdade. "
            "Aserinsky e Kleitman costumam ser considerados os fundadores da pesquisa moderna do sono. Em julho "
            "de 1998, aos 77 anos, Aserinsky morreu quando seu carro bateu numa árvore ao norte de San Diego. A "
            "autópsia não esclareceu a causa, mas levantou a possibilidade de que ele tivesse adormecido ao "
            "volante."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Eugene_Aserinsky",
                "was a graduate student at the University of Chicago in 1953 when he discovered REM sleep. [...] "
                "He made the discovery after hours spent studying the eyelids of sleeping subjects. [...] "
                "Because of these discoveries, Aserinsky and Kleitman are generally considered the founders of modern sleep research. "
                "Eugene Aserinsky died on July 22, 1998, when his car hit a tree north of San Diego. "
                "An autopsy was inconclusive about the cause of the accident, but raised the possibility that it had resulted from him having fallen asleep at the wheel. "
                "He was 77",
                nome="Eugene Aserinsky"),
            wiki("Nathaniel_Kleitman",
                "Eugene Aserinsky, one of Kleitman's graduate students, decided to hook sleepers up to an early version of an electroencephalogram machine, which scribbled across 1⁄2 mile (800 m) of paper each night. "
                "In the process, Aserinsky noticed that several times each night the sleepers went through periods when their eyes darted wildly back and forth. "
                "Kleitman insisted that the experiment be repeated yet again, this time on his daughter, Esther. "
                "In 1953, he and Aserinsky introduced the world to \"rapid-eye movement,\" or REM sleep. "
                "Kleitman and Aserinsky demonstrated that REM sleep was correlated with dreaming and brain activity. "
                "Another of Kleitman's graduate students, William C. Dement, who was a professor of psychiatry at the Stanford medical school, described this as the year that \"the study of sleep became a true scientific field.\"",
                nome="Nathaniel Kleitman"),
        ],
    },
]
