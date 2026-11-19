LOTE = "2026-11-19-termodinamica-01"
AREA = "fisica_quimica"
TEMA = "termodinamica"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 efeito Mpemba: o sorvete quente que congelou primeiro
    {
        "temas_secundarios": ["ciencia_cozinha", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "misterio_aberto"],
        "gancho": "Em 1963, um estudante da Tanzânia viu sua mistura de sorvete quente congelar antes da fria. O fenômeno ganhou o nome dele, efeito Mpemba, mas os físicos ainda discutem quando e por que ele acontece.",
        "explicacao": (
            "Erasto Mpemba estava numa aula de culinária na escola Magamba, no então Tanganica, quando notou que "
            "uma mistura de sorvete posta quente no congelador endureceu antes de outra que já estava fria. Anos "
            "depois, Denis Osborne, físico da universidade de Dar es Salaam, foi dar uma palestra na escola de "
            "Mpemba, e o rapaz perguntou: por que, com dois recipientes iguais de água, um a 35 °C e outro a "
            "100 °C, o mais quente congela primeiro? Osborne achou que o aluno estava enganado, mas repetiu o teste "
            "no próprio laboratório, viu o mesmo resultado, e os dois publicaram juntos em 1969. A ideia não era "
            "nova: Aristóteles já escrevia que a água aquecida antes congela mais depressa. O difícil é provar. O "
            "resultado depende do recipiente, dos gases dissolvidos, do jeito de resfriar e até do que se chama de "
            "\"congelar\": a primeira película de gelo ou o bloco inteiro. Um estudo de 2016, que mediu o tempo até "
            "a água chegar a 0 °C, concluiu que não há evidência de observações significativas do efeito. Já um "
            "trabalho de 2024 com gotas pequenas viu as quentes congelarem sempre antes. Os físicos seguem divididos "
            "sobre a definição e o mecanismo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Mpemba_effect",
            "The effect is named after Erasto Mpemba, a Tanzanian teenager who studied it scientifically in the 1960s for the first time, along with Denis Osborne. [...] "
            "Studies of the effect in water have mixed results, with some experiments finding no reproducible effect. "
            "Physicists remain divided on the effect's precise definition and underlying mechanisms. [...] "
            "Even this definition does not specify whether \"freezing\" refers to the point at which a visible surface layer of ice has formed, or the point at which the liquid is completely frozen. [...] "
            "who described it in 1963 in Form 3 of Magamba Secondary School, Tanganyika; when freezing a hot ice cream mixture in a cookery class, he noticed that it froze before a cold mixture. [...] "
            "The headmaster invited Dr. Denis Osborne from the University College in Dar es Salaam to give a lecture on physics. "
            "After the lecture, Mpemba asked him, \"If you take two similar containers with equal volumes of water, one at 35 °C (95 °F) and the other at 100 °C (212 °F), and put them into a freezer, the one that started at 100 °C (212 °F) freezes first. Why?\" "
            "Osborne thought the student was mistaken at first, but, intrigued by the question, he experimented on the issue back at his workplace, and was amused to see he was able to confirm Mpemba's finding. "
            "Osborne and Mpemba later published the results together in 1969 [...] "
            "\"The fact that the water has previously been warmed contributes to its freezing quickly: for so it cools sooner. [...] "
            "the amount of allowed dissolved gas and other impurities, the size, shape and material of the container, the method of cooling, and the temperature of the refrigerator. [...] "
            "In 2016, Burridge and Linden studied a slightly different measure, the time it took water samples to reach 0 °C but not freeze. [...] "
            "They concluded that \"there is no evidence to support meaningful observations of the Mpemba effect.\" [...] "
            "In 2024, Argelia Ortega, et al. studied the freezing of small (1 to 20 mL or 0.03 to 0.7 US fl oz) drops in a Peltier cell with a thermographic camera, and found that hot drops consistently froze faster than cold ones",
            nome="Mpemba effect")],
    },
    # 2 a escala Celsius nasceu de cabeça para baixo
    {
        "temas_secundarios": ["medidas_padroes", "revolucao_cientifica"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "Na escala que Celsius criou em 1742, a água fervia a 0 grau e congelava a 100. Outros a inverteram depois. E, pela definição atual, a água pura sob uma atmosfera ferve um pouco abaixo de 100 °C.",
        "explicacao": (
            "O astrônomo sueco Anders Celsius propôs sua escala em 1742 com o zero na fervura da água e o cem no "
            "derretimento do gelo. O que ele buscava era precisão: mostrou que o ponto de fusão do gelo quase não "
            "muda com a pressão e mediu com cuidado como o ponto de ebulição varia com ela. A forma atual teve "
            "vários autores. Em 1743, o francês Jean-Pierre Christin, de Lyon, já usava 0 para o congelamento e 100 "
            "para a fervura. O botânico Lineu fez a mesma inversão num termômetro para as suas estufas, mais ou "
            "menos quando Celsius morreu, em 1744, e outros cientistas e fabricantes de instrumentos também recebem "
            "crédito por ela. O nome \"Celsius\" só foi oficializado em 1948; antes, a escala era chamada de "
            "centígrada. Hoje a água nem entra na definição: desde 2019, ela se apoia na constante de Boltzmann, sem "
            "depender de nenhuma propriedade da água. Assim, a fervura da água pura sob uma atmosfera virou um valor "
            "medido, cerca de 99,974 °C na escala de calibração ITS-90. A diferença não importa na cozinha, até "
            "porque subir só 28 centímetros já muda o ponto de ebulição em um milésimo de grau."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Celsius",
                "The degree Celsius is the unit of temperature on the Celsius temperature scale (originally known as the centigrade scale in English) [...] "
                "In 1948, the International Committee for Weights and Measures renamed it to honor Celsius [...] "
                "In 1742, Swedish astronomer Anders Celsius (1701–1744) created a temperature scale that was the reverse of the scale now known as \"Celsius\": 0 represented the boiling point of water, while 100 represented the freezing point of water. "
                "In his paper Observations of two persistent degrees on a thermometer, he recounted his experiments showing that the melting point of ice is essentially unaffected by pressure. "
                "He also determined with remarkable precision how the boiling point of water varied as a function of atmospheric pressure. [...] "
                "In 1743, the French physicist Jean-Pierre Christin, permanent secretary of the Academy of Lyon, inverted the Celsius temperature scale so that 0 represented the freezing point of water and 100 represented the boiling point of water. [...] "
                "In 1744, coincident with the death of Anders Celsius, the Swedish botanist Carl Linnaeus (1707–1778) reversed Celsius's scale. "
                "His custom-made \"Linnaeus-thermometer\", for use in his greenhouses [...] "
                "numerous physicists, scientists, and instrument makers are credited with having independently developed this same scale [...] "
                "In 2019, the definition was changed to use the Boltzmann constant, completely decoupling the definition of the kelvin from the properties of water. [...] "
                "When calibrated to ITS-90 (a calibration standard comprising many definition points and commonly used for high-precision instrumentation), the boiling point of VSMOW was slightly less, about 99.974 °C. [...] "
                "For example, an altitude change of only 28 cm (11 in) causes the boiling point to change by one millikelvin.",
                nome="Celsius"),
            wiki("Anders_Celsius",
                "His thermometer was calibrated with a value of 0 for the boiling point of water and 100 for the freezing point.",
                nome="Anders Celsius"),
        ],
    },
    # 3 Rumford, os canhões e a viúva de Lavoisier
    {
        "temas_secundarios": ["revolucao_cientifica", "revolucao_industrial"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 1798, o conde Rumford fez água ferver só com o atrito de uma broca furando um canhão e concluiu que calor é movimento, não um fluido. Anos depois, casou com a viúva de Lavoisier, que popularizara o calor-fluido.",
        "explicacao": (
            "No fim do século XVIII, a explicação dominante era a teoria do calórico: o calor seria um fluido "
            "invisível que passa dos corpos quentes para os frios. Lavoisier ajudou a levar essa ideia a um público "
            "amplo no seu influente livro-texto de 1789. Benjamin Thompson, nascido nos EUA e feito conde do Sacro "
            "Império em 1791, passou anos a serviço da Baviera e notou o calor gerado ao furar canhões no arsenal de "
            "Munique. Para testar, mergulhou um cano de canhão na água e o furou com uma broca propositalmente cega. "
            "A água ferveu em cerca de duas horas e meia, e o calor parecia inesgotável. Ele ainda comparou o metal "
            "raspado com o restante e não achou mudança física. Se o calor fosse uma substância guardada no metal, "
            "não deveria brotar sem fim; para Rumford, a única coisa transmitida ao cano era movimento. Na época, o "
            "resultado não foi visto como ameaça ao calórico, e as incertezas do experimento foram muito debatidas, "
            "mas ele inspirou Joule e outros em meados do século XIX. A vida do conde foi "
            "agitada: lutou ao lado dos britânicos na independência americana, criou uma sopa para os pobres e "
            "lareiras que não enchiam a sala de fumaça. Em 1804, casou com Marie-Anne Lavoisier, viúva do químico, "
            "e os dois se separaram três anos depois."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Benjamin_Thompson",
                "he supported the Loyalist cause during the American War of Independence, commanding the King's American Dragoons during the conflict. [...] "
                "He also invented Rumford's Soup, a soup for the poor [...] "
                "The Rumford fireplace created a sensation in London [...] "
                "so all the smoke would go up into the chimney rather than lingering and entering the room. [...] "
                "in 1804, he married Marie-Anne Lavoisier, the widow of the great French chemist Antoine Lavoisier. "
                "Thompson separated from his second wife after three years [...] "
                "Rumford's most important scientific work took place in Munich, and centred on the nature of heat, which he contended in \"An Inquiry Concerning the Source of the Heat Which Is Excited by Friction\" (1798) was not the caloric of then-current scientific thinking but a form of motion. "
                "Rumford had observed the frictional heat generated by boring cannon at the arsenal in Munich. "
                "Rumford immersed a cannon barrel in water and arranged for a specially blunted boring tool. "
                "He showed that the water could be boiled within roughly two and a half hours and that the supply of frictional heat was seemingly inexhaustible. "
                "Rumford confirmed that no physical change had taken place in the material of the cannon by comparing the specific heats of the material machined away and that remaining. "
                "Rumford argued that the seemingly indefinite generation of heat was incompatible with the caloric theory. "
                "He contended that the only thing communicated to the barrel was motion. [...] "
                "Count of the Holy Roman Empire, 1791.",
                nome="Benjamin Thompson (Count Rumford)"),
            wiki("Caloric_theory",
                "The caloric theory is a superseded scientific theory that heat consists of a self-repellent fluid called \"caloric\" that flows from hotter bodies to colder bodies. [...] "
                "In his influential 1789 textbook Traité Élémentaire de Chimie, Lavoisier clarified the concept of caloric and introduced it to a wider audience. [...] "
                "He had found that boring a cannon repeatedly does not result in a loss of its ability to produce heat, and therefore no loss of caloric. "
                "This suggested that caloric could not be a conserved \"substance\", though the experimental uncertainties in his experiment were widely debated. "
                "His results were not seen as a \"threat\" to caloric theory at the time [...] "
                "Rumford's experiment inspired the work of James Prescott Joule and others towards the middle of the 19th century.",
                nome="Caloric theory"),
        ],
    },
    # 4 Carnot: o livro que fundou a termodinâmica e quase sumiu
    {
        "temas_secundarios": ["revolucao_industrial", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "O livro que fundou a termodinâmica, de 1824, teve 600 exemplares pagos pelo próprio autor e quase sumiu das livrarias. Sadi Carnot morreu de cólera aos 36 anos, na obscuridade. Só depois virou o \"pai da termodinâmica\".",
        "explicacao": (
            "Sadi Carnot era engenheiro do exército francês e filho de Lazare Carnot, figura importante do período "
            "napoleônico. Em 1824, publicou \"Reflexões sobre a potência motriz do fogo\", a única obra que lançou. "
            "Na época, as máquinas a vapor aproveitavam só uns 5 a 7% da energia do combustível, e ele fez uma "
            "pergunta de fundo: existe um limite para o trabalho que se tira de uma fonte de calor? A resposta foi "
            "a primeira teoria bem-sucedida da eficiência máxima de uma máquina térmica. Carnot raciocinava com a "
            "teoria do calórico, o calor como fluido, embora anotações privadas indiquem que, em 1832, já a tinha "
            "abandonado. O livro quase não teve leitores. Em 1832, aos 36 anos, ele morreu de cólera. Em 1834, "
            "outro engenheiro, Émile Clapeyron, publicou um comentário detalhado da obra, e foi por ele que William "
            "Thomson, o futuro Lord Kelvin, conheceu as ideias de Carnot em 1845. O original, Thomson só conseguiu "
            "ler no fim de 1848. Com essa base, Kelvin criou uma escala absoluta de temperatura, e Rudolf Clausius "
            "definiu a entropia e formulou a segunda lei da termodinâmica."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Nicolas_L%C3%A9onard_Sadi_Carnot",
            "1 June 1796 – 24 August 1832), known as Sadi Carnot, was a French military engineer and physicist. [...] "
            "In that book, which would be his only publication, Carnot developed the first successful theory of the maximum efficiency of heat engines. [...] "
            "Thomson used Carnot's analysis to develop an absolute thermodynamic temperature scale, while Clausius used it to define the concept of entropy, thus formalizing the second law of thermodynamics. "
            "Carnot was the son of Lazare Carnot, an eminent mathematician, engineer, and commander of the French Revolutionary Army and later of the Napoleonic army. [...] "
            "Carnot died in relative obscurity at the age of 36, but today he is often characterized as the \"father of thermodynamics\". [...] "
            "According to the hospital record, he was cured from \"mania\" but then died of cholera on 24 August. [...] "
            "published in Paris in June of 1824 by Bachelier, with Carnot himself paying for the printing of the 600 copies. "
            "The work attracted little attention during his lifetime and virtually disappeared from booksellers and libraries. "
            "An article published in 1834 (two years after Carnot's death and ten years after the publication of his book) by the engineer and fellow polytechnicien Émile Clapeyron finally succeeded in calling attention to Carnot's work [...] "
            "\"Is there a limit to the work that can be generated from a given heat source?\" [...] "
            "the efficiency of a typical engine – the useful work it was able to do when a given quantity of fuel was burned – was only about 5–7%. [...] "
            "William Thomson read Clapeyron's paper in 1845, while visiting the Paris laboratory of Henri Regnault, but it was only at the end of 1848 that Thomson was able to read Carnot's original work [...] "
            "there is material indicating that Carnot had, by the spring of 1832, rejected the caloric theory and accepted the equivalence of heat and work.",
            nome="Nicolas Léonard Sadi Carnot")],
    },
    # 5 Joule, o cervejeiro recusado que media cachoeiras na lua de mel
    {
        "temas_secundarios": ["revolucao_industrial", "energia"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "James Joule, que mostrou que trabalho vira calor e deu nome à unidade de energia, administrava a cervejaria da família. A Royal Society recusou publicar um artigo dele, e na lua de mel ele planejou medir uma cachoeira.",
        "explicacao": (
            "Joule nasceu em 1818, filho de um cervejeiro rico, e foi aluno particular de John Dalton. Adulto, "
            "cuidava da cervejaria, e a ciência era um passatempo levado a sério. Por volta de 1840, quis saber se "
            "os novos motores elétricos poderiam substituir as máquinas a vapor da fábrica, e a pergunta financeira "
            "virou outra: quanto trabalho se tira de uma fonte de energia? Em 1843, apresentou seus resultados num "
            "encontro científico em Cork e foi recebido com silêncio. No ano seguinte, a Royal Society ouviu um "
            "artigo dele, mas recusou publicá-lo, e o texto saiu em 1845 na revista Philosophical Magazine. Seu "
            "experimento mais famoso usava um peso em queda para girar pás dentro de um barril isolado cheio de "
            "água, que esquentava. Assim ele mediu quanto trabalho mecânico equivale a uma quantidade de calor. Em "
            "1847, casou com Amelia Grimes e, dias depois do casamento, combinou com William Thomson, o futuro Lord "
            "Kelvin, de medir a diferença de temperatura entre o alto e o pé da cascata de Sallanches. A tentativa "
            "se mostrou impraticável. Hoje a unidade de energia do Sistema Internacional, o joule, leva o seu nome."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("James_Prescott_Joule",
            "The SI unit of energy, the joule (J), is named after him. [...] "
            "James Joule was born in 1818, the son of Benjamin Joule, a wealthy brewer [...] "
            "Joule was tutored as a young man by the famous scientist John Dalton [...] "
            "As an adult, Joule managed the brewery. Science was merely a serious hobby. "
            "Sometime around 1840, he started to investigate the feasibility of replacing the brewery's steam engines with the newly invented electric motor. [...] "
            "However, Joule's interest diverted from the narrow financial question to that of how much work could be extracted from a given source [...] "
            "He announced his results at a meeting of the chemical section of the British Association for the Advancement of Science in Cork in August 1843 and was met by silence. [...] "
            "Joule read his paper to the Royal Society on 20 June 1844, but his paper was rejected for publication by the Royal Society and he had to be content with publishing in the Philosophical Magazine in 1845. [...] "
            "involving the use of a falling weight, in which gravity does the mechanical work, to spin a paddle wheel in an insulated barrel of water which increased the temperature. [...] "
            "Joule married Amelia Grimes on 18 August and the couple went on honeymoon. "
            "Marital enthusiasm notwithstanding, Joule and Thomson arranged to attempt an experiment a few days later to measure the temperature difference between the top and bottom of the Cascade de Sallanches waterfall, though this subsequently proved impractical. [...] "
            "Joule married Amelia Grimes in 1847.",
            nome="James Prescott Joule")],
    },
    # 6 o demônio de Maxwell e o calor de apagar um bit
    {
        "temas_secundarios": ["historia_computacao", "paradoxos_logica"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Em 1867, Maxwell imaginou um ser que separaria moléculas rápidas e lentas, esquentando um lado sem gastar trabalho. A saída mais aceita para o enigma: apagar informação produz calor, algo medido em 2012.",
        "explicacao": (
            "No experimento mental, um ser minúsculo controla uma portinhola entre duas câmaras de gás e só deixa "
            "passar as moléculas rápidas para um lado e as lentas para o outro. Um lado esquenta, o outro esfria, e "
            "a entropia total cairia sem gasto de trabalho, contrariando a segunda lei da termodinâmica. Maxwell, "
            "que era muito religioso, falava em \"ser finito\"; quem o chamou de demônio foi Lord Kelvin. Em 1929, "
            "Leó Szilárd sugeriu que medir as moléculas custaria energia. Em 1961, Rolf Landauer, da IBM, propôs que "
            "o custo inevitável está em outro lugar: apagar um bit de memória libera um mínimo de calor, que cresce "
            "com a temperatura. Em 1982, Charles Bennett aplicou isso ao demônio: cedo ou tarde ele enche a memória "
            "com o que observou e precisa apagá-la, e esse apagamento paga a conta da entropia. Em 2012, físicos "
            "mediram pela primeira vez o calor minúsculo liberado ao apagar um único bit, usando uma partícula num "
            "poço duplo. O limite de Landauer é aceito pela maioria, mas pesquisadores como John Earman e John "
            "Norton argumentam que a explicação é circular, e o debate continua. À temperatura ambiente, o limite é "
            "tão baixo que, em 2012, os computadores gastavam cerca de um bilhão de vezes mais por operação."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Maxwell%27s_demon",
                "Maxwell's demon is a thought experiment that appears to disprove the second law of thermodynamics. "
                "It was proposed by the physicist James Clerk Maxwell in 1867. [...] "
                "Lord Kelvin would later call it a \"demon\". "
                "In the thought experiment, a demon controls a door between two chambers containing gas. "
                "As individual gas molecules (or atoms) approach the door, the demon quickly opens and closes the door to allow only fast-moving molecules to pass through in one direction, and only slow-moving molecules to pass through in the other. [...] "
                "the demon's actions cause one chamber to warm up and the other to cool down. "
                "This would decrease the total entropy of the system, seemingly without applying any work, thereby violating the second law of thermodynamics. [...] "
                "The concept of Maxwell's demon has provoked substantial debate in the philosophy of science and theoretical physics, which continues to the present day. [...] "
                "In his letters and books, Maxwell described the agent opening the door between the chambers as a \"finite being\". "
                "Being a deeply religious man, he never used the word \"demon\". [...] "
                "One of the most famous responses to this question was suggested in 1929 by Leó Szilárd [...] "
                "the act of acquiring information would require an expenditure of energy. [...] "
                "In 1982, Charles Bennett showed that, however well prepared, eventually the demon runs out of information storage space and must begin to erase the information it has previously gathered. [...] "
                "the minimum heat dissipated by erasing information was experimentally measured by Antoine Bérut et al. in 2012, using a colloidal particle in a double-well potential [...] "
                "John Earman and John D. Norton have argued that Szilárd and Landauer's explanations of Maxwell's demon begin by assuming that the second law of thermodynamics cannot be violated by the demon [...] "
                "It would therefore be circular to invoke these derived properties to defend the second law from the demonic argument.",
                nome="Maxwell's demon"),
            wiki("Landauer%27s_principle",
                "Landauer's principle states that the minimum energy needed to erase one bit of information is proportional to the temperature at which the system is operating. [...] "
                "As of 2012, modern computers use about a billion times as much energy per operation. [...] "
                "Rolf Landauer first proposed the principle in 1961 while working at IBM. [...] "
                "In a 2012 article published in Nature, a team of physicists from the École normale supérieure de Lyon, University of Augsburg and the University of Kaiserslautern described that for the first time they have measured the tiny amount of heat released when an individual bit of data is erased. [...] "
                "The principle is widely accepted as physical law, but it has been challenged for using circular reasoning and faulty assumptions.",
                nome="Landauer's principle"),
        ],
    },
    # 7 temperaturas abaixo de zero kelvin são mais quentes que o infinito
    {
        "temas_secundarios": ["mecanica_quantica", "luz_cores"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Há sistemas com temperatura abaixo de zero kelvin, e eles não são frios: são mais quentes que qualquer coisa a temperatura positiva. Em contato com elas, cedem calor, nunca recebem.",
        "explicacao": (
            "O truque está no que a temperatura mede de fato. Nas temperaturas comuns, as partículas ocupam mais os "
            "estados de energia baixa do que os de energia alta. Numa temperatura negativa, essa distribuição se "
            "inverte e os estados de energia alta ficam mais cheios. Isso só é possível em sistemas que têm um teto "
            "de energia, como spins nucleares num campo magnético. Num gás comum, as partículas podem sempre correr "
            "mais, então não há teto e não há temperatura negativa. Perto do teto, colocar mais energia passa a "
            "reduzir o número de arranjos possíveis, e a entropia cai: é aí que a temperatura fica negativa. Por "
            "isso, ela não está abaixo do zero absoluto, e sim \"acima do infinito\". Lars Onsager previu "
            "a possibilidade em 1949, e os primeiros sinais experimentais vieram em 1951, com Purcell e Pound, nos "
            "spins nucleares de um cristal de fluoreto de lítio. O exemplo clássico é a inversão de população dos "
            "lasers. Em 2013, uma equipe conseguiu temperatura negativa também no movimento de átomos de "
            "potássio-39 presos numa rede de laser."
        ),
        "nivel": 3, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Negative_temperature",
            "Certain thermodynamic systems can achieve negative thermodynamic temperature; that is, their temperature can be expressed as a negative quantity on the Kelvin or Rankine scales. [...] "
            "At ordinary positive temperatures, lower-energy states are more likely to be occupied than higher-energy states. "
            "At negative temperatures, this distribution is reversed, so higher-energy states become more populated than lower-energy ones. "
            "For this reason, a system with a truly negative temperature on the Kelvin scale is hotter than any system with a positive temperature. "
            "If a negative-temperature system and a positive-temperature system come in contact, heat will flow from the negative- to the positive-temperature system. "
            "A standard example of such a system is population inversion in laser physics. [...] "
            "This is the case for ordinary particles, such as atoms or dust, whose kinetic energy can increase without bound. [...] "
            "Negative temperatures are only possible in systems that have a maximum energy they can hold. "
            "As such systems approach this maximum energy, the number of accessible states begins to decrease with further increases in energy, causing the entropy to fall and making the temperature negative. "
            "Examples of such systems include two-level systems and nuclear spin ensembles in an external magnetic field. [...] "
            "The possibility of negative temperatures was first predicted by Lars Onsager in 1949. [...] "
            "It seems negative temperatures were first found experimentally in 1951, when Purcell and Pound observed evidence for them in the nuclear spins of a lithium fluoride crystal placed in a magnetic field [...] "
            "A substance with a negative temperature is not colder than absolute zero, but rather it is hotter than infinite temperature. [...] "
            "Negative temperatures have also been achieved in motional degrees of freedom. "
            "Using an optical lattice, upper bounds were placed on the kinetic energy, interaction energy and potential energy of cold potassium-39 atoms. [...] "
            "Braun, S.; Ronzheimer, J. P.; Schreiber, M.; Hodgman, S. S.; Rom, T.; Bloch, I.; Schneider, U. (2013). \"Negative Absolute Temperature for Motional Degrees of Freedom\".",
            nome="Negative temperature")],
    },
    # 8 a nebulosa mais fria que o fundo do espaço
    {
        "temas_secundarios": ["estrelas", "cosmologia"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "O lugar natural mais frio que se conhece é uma nebulosa a 5 mil anos-luz. Seu gás se expande tão rápido que esfriou abaixo da temperatura do próprio fundo do espaço, a menos de meio grau do zero absoluto.",
        "explicacao": (
            "A Nebulosa do Bumerangue, na constelação do Centauro, é o gás expelido por uma estrela gigante vermelha "
            "no fim da vida. O espaço vazio não é totalmente frio: a radiação que sobrou do Big Bang o mantém a "
            "cerca de 2,725 graus acima do zero absoluto. Em observações de 1995, astrônomos notaram que a nebulosa "
            "absorvia essa radiação, sinal de que estava mais fria que ela. O frio vem da expansão: o gás corre para "
            "fora a mais de 150 km por segundo, e um gás que se expande assim esfria, como mostra o efeito "
            "Joule-Thomson. Cálculos de 2017, com o radiotelescópio ALMA, indicam menos de meio kelvin. A estrela "
            "sozinha não teria força para lançar tanta matéria tão depressa; a explicação proposta é que uma estrela "
            "companheira pequena tenha mergulhado no coração da gigante. O fenômeno é passageiro: a nebulosa já está "
            "esquentando aos poucos, e congeladores cósmicos como ele talvez sejam comuns, mas durariam pouco."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": "https://public.nrao.edu/?p=6540",
             "titulo": "ALMA Returns to Boomerang Nebula (NRAO, 2017)",
             "idioma": "en",
             "trecho": "News Release: June 5, 2017 at 11:00 am EDT [...] "
                       "An ancient, red giant star in the throes of a frigid death has produced the coldest known object in the cosmos — the Boomerang Nebula. [...] "
                       "may be that a small companion star has plunged into the heart of the red giant, ejecting most the matter of the larger star as an ultra-cold outflow of gas and dust. "
                       "This outflow is expanding so rapidly — about 10 times faster than a single star could produce on its own — that its temperature has fallen to less than half a degree Kelvin (minus 458.5 degrees Fahrenheit). [...] "
                       "The Boomerang Nebula is located about 5,000 light-years from Earth in the constellation Centaurus. [...] "
                       "When the Boomerang Nebula was first observed in 1995, astronomers noted that it was absorbing the light of the Cosmic Microwave Background, which is the leftover radiation from the Big Bang. "
                       "This radiation provides the natural background temperature of space — only 2.725 degrees above absolute zero. [...] "
                       "Traveling more than 150 kilometers per second [...] "
                       "Even now, the Boomerang Nebula is slowly warming. [...] "
                       "It's possible these super cosmic freezers are quite common in the universe, but they can only maintain such extreme temperatures for a relatively short time."},
            {"url": "https://science.nrao.edu/science/highlights/fy2014-1/the-coldest-place-in-the-universe",
             "titulo": "The Coldest Place in the Universe (NRAO Science Highlights)",
             "idioma": "en",
             "trecho": "The pre-planetary nebula, the Boomerang Nebula, is the coldest known place in the Universe, refrigerated by an expanding molecular outflow (Joule-Thomson effect), to roughly 1deg K."},
            wiki("Boomerang_Nebula",
                "making it the coldest natural place currently known.",
                nome="Boomerang Nebula"),
        ],
    },
    # 9 efeito Leidenfrost: a gota que dura mais na panela mais quente
    {
        "temas_secundarios": ["ciencia_cozinha", "revolucao_industrial"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Numa chapa bem quente, uma gota d'água dura mais do que numa menos quente. Em testes do século XIX, uma gota sumiu quase na hora a 168 °C, mas resistiu 152 segundos a 202 °C, flutuando num colchão de vapor.",
        "explicacao": (
            "É o efeito Leidenfrost, descrito pelo médico alemão Johann Gottlob Leidenfrost num tratado de 1756. "
            "Quando a superfície passa bem do ponto de ebulição, a parte de baixo da gota vira vapor no instante do "
            "contato, e esse vapor sustenta o resto da gota logo acima da chapa. Como o vapor conduz calor muito pior "
            "que o metal, a gota esquenta devagar e desliza de um lado para o outro. Para a água, o fenômeno começa "
            "por volta de 193 °C, mas o ponto exato é difícil de prever e depende da superfície e das impurezas. O "
            "efeito preocupava os engenheiros de caldeiras: o engenheiro vitoriano William Fairbairn notou que ele "
            "reduzia muito a passagem de calor do ferro quente para a água e citou os testes com aquela gota. O "
            "mesmo efeito explica por que gotas de nitrogênio líquido rolam pela pele sem machucar. Em 2009, a "
            "equipe do programa MythBusters mostrou que uma pessoa consegue molhar a mão e mergulhá-la rapidamente "
            "em chumbo derretido sem se ferir. Não é para tentar em casa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Leidenfrost_effect",
            "The Leidenfrost effect or film boiling is a physical phenomenon in which a liquid, close to a solid surface of another body that is significantly hotter than the liquid's boiling point, produces an insulating vapor layer that keeps the liquid from boiling rapidly. [...] "
            "The effect is named after the German doctor Johann Gottlob Leidenfrost, who described it in A Tract About Some Qualities of Common Water. [...] "
            "If the pan's temperature is at or above the Leidenfrost point, which is approximately 193 °C (379 °F) for water, the water skitters across the pan and takes longer to evaporate than it would take if the water droplets had been sprinkled onto a cooler pan. [...] "
            "the bottom part of the water droplet vaporizes immediately on contact with the hot pan. "
            "The resulting gas suspends the rest of the water droplet just above it, preventing any further direct contact between the liquid water and the hot pan. "
            "As steam has much poorer thermal conductivity than the metal pan, further heat transfer between the pan and the droplet is slowed down dramatically. [...] "
            "The temperature at which the Leidenfrost effect appears is difficult to predict. "
            "Even if the volume of the drop of liquid stays the same, the Leidenfrost point may be quite different, with a complicated dependence on the properties of the surface, as well as any impurities in the liquid. [...] "
            "The effect was also described by the Victorian steam boiler designer, William Fairbairn, in reference to its effect on massively reducing heat transfer from a hot iron surface to water, such as within a boiler. "
            "In a pair of lectures on boiler design, he cited the work of Pierre Hippolyte Boutigny (1798–1884) and Professor Bowman of King's College, London, in studying this. "
            "A drop of water that was vaporized almost immediately at 168 °C (334 °F) persisted for 152 seconds at 202 °C (396 °F). [...] "
            "allowing liquid nitrogen droplets to harmlessly roll off exposed skin. [...] "
            "In 1756, Leidenfrost observed that water droplets supported by the vapor film slowly evaporate as they move about on the hot surface. [...] "
            "In the 2009 season 7 finale of MythBusters, \"Mini Myth Mayhem\", the team demonstrated that a person can wet their hand and briefly dip it into molten lead without injury",
            nome="Leidenfrost effect")],
    },
    # 10 Blagden e a sala a 127 °C onde o bife cozinhava
    {
        "temas_secundarios": ["corpo_extremo", "historia_medicina"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1775, o médico britânico Charles Blagden e colegas entraram numa sala a cerca de 127 °C. Ovos assaram até endurecer e um bife ficou quase seco, mas a temperatura do corpo deles mal mudou. O segredo era o suor.",
        "explicacao": (
            "Os testes começaram em 1774, quando o médico George Fordyce convidou colegas para ver como o corpo "
            "resistia a um ar muito mais quente que ele próprio. Já se sabia, por exemplo, que os russos usavam "
            "banhos a cerca de 160 graus Fahrenheit. Charles Blagden, que relatou os experimentos à Royal Society, "
            "foi aumentando a temperatura. Na sessão mais extrema, um termômetro passou de 260 °F, uns 127 °C, e ele "
            "ficou oito minutos lá dentro, de roupa, luvas, meias grossas e um pano diante do rosto para não se "
            "queimar com o ferro em brasa que aquecia a sala. Depois de sete minutos, sentiu um aperto no peito e "
            "saiu. Para provar que o termômetro não mentia, o grupo deixou ovos e bifes perto dele: em uns vinte "
            "minutos, os ovos estavam duros, e em 47 minutos um bife estava cozido e quase seco. Ainda assim, "
            "segundo Blagden, a temperatura do corpo deles não mudou de forma sensível. No relato de 1775, ele foi o "
            "primeiro cientista ocidental a reconhecer oficialmente o papel do suor no controle da temperatura do "
            "corpo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Charles_Blagden",
                "Blagden experimented on human ability to withstand high temperatures. "
                "In 1775 he showed that human beings could withstand room temperatures as high as 260 degrees Fahrenheit (127 degrees Celsius). "
                "In his report to the Royal Society in 1775, he was first Western scientist to officially recognise the role of perspiration in thermoregulation.",
                nome="Charles Blagden"),
            {"url": "https://jimclifford.ca/philosophical-transactions-ocr-1665-1869/articles/jstor-106218/",
             "titulo": "Further Experiments and Observations in an Heated Room, Charles Blagden (Philosophical Transactions, 1775, texto OCR)",
             "idioma": "en",
             "trecho": "without any sensible alteration in the temperature of our bodies. [...] "
                       "a very large thermometer, placed at a distance from the door of the room, but nearer to the wall than to the cockle, and defended from the immediate action of the cockle by a piece of paper hung before it, rose one or two degrees above $260^\\circ$ [...] "
                       "with the addition, to my common cloaths, of a pair of thick worsted stockings drawn over my shoes, and reaching some way above my knees; I also put on a pair of gloves, and held a cloth constantly between my face and the cockle: all these precautions were necessary to guard against the scorching of the red-hot iron. "
                       "I remained eight minutes in this situation [...] "
                       "For seven minutes my breathing continued perfectly good; but after that time I began to feel an oppression in my lungs [...] "
                       "we put some eggs and a beef-steak upon a tin frame, placed near the standard thermometer [...] "
                       "In about twenty minutes the eggs were taken out, roasted quite hard; and in forty-seven minutes the steak was not only dressed, but almost dry."},
            {"url": "https://jimclifford.ca/philosophical-transactions-ocr-1665-1869/articles/jstor-106183/",
             "titulo": "Experiments and Observations in an Heated Room, Charles Blagden (Philosophical Transactions, 1775, texto OCR)",
             "idioma": "en",
             "trecho": "ABOUT the middle of January, several gentlemen and myself received an invitation from Dr. GEORGE FORDYCE, to observe the effects of air heated to a much higher degree than it was formerly thought any living creature could bear. [...] "
                       "the Russians use their baths heated to \\(60^\\circ\\) of Reaumur's thermometer, about \\(160\\) of Fahrenheit's"},
            {"url": "https://publicdomainreview.org/collection/experiments-and-observations-in-a-heated-room-1774/",
             "titulo": "Experiments and Observations in a Heated Room (1774) (The Public Domain Review)",
             "idioma": "en",
             "trecho": "In 1774 and 1775 the British physician and scientist Charles Blagden conducted a series of experiments concerned with exploring the effects on the human body of extremely high temperatures [...] "
                       "Beginning at a modest 100 degrees Fahrenheit (38 degrees Celsius), by the 1775 session they progressed to temperatures upward of a whopping 260 degrees Fahrenheit (127 degrees Celsius)."},
        ],
    },
    # 11 o hélio não congela nem no zero absoluto
    {
        "temas_secundarios": ["mecanica_quantica", "elementos_quimicos"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "O hélio é o único elemento que não congela nem no zero absoluto, se estiver à pressão normal. Para virar sólido, precisa ser espremido a cerca de 25 bar. A culpa é da física quântica.",
        "explicacao": (
            "Em 1908, o holandês Heike Kamerlingh Onnes liquefez o hélio pela primeira vez, resfriando o gás abaixo "
            "de 5 kelvin. Tentou então solidificá-lo baixando ainda mais a temperatura e fracassou. Não era falta de "
            "frio: à pressão atmosférica, o hélio continua líquido até o zero absoluto, algo que nenhum outro "
            "elemento faz. O motivo é quântico. Mesmo no frio máximo, os átomos guardam uma energia mínima, a "
            "energia de ponto zero, e no hélio ela é alta demais para que se prendam num cristal. A solução veio em "
            "1926, quando Willem Keesom, aluno de Onnes, conseguiu um centímetro cúbico de hélio sólido aplicando "
            "pressão. O sólido exige cerca de 1 a 1,5 kelvin e uns 25 bar. Mesmo assim, é difícil distingui-lo do "
            "líquido, porque os dois desviam a luz quase do mesmo jeito, e ele é tão compressível que dá para "
            "reduzir o seu volume em mais de 30% no laboratório. O hélio líquido mais frio tem outras manias: escapa "
            "de recipientes abertos subindo pelas paredes numa película de uns 30 nanômetros."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Helium",
            "In 1908, helium was first liquefied by Dutch physicist Heike Kamerlingh Onnes by cooling the gas to less than 5 K (−268.15 °C; −450.67 °F). "
            "He tried to solidify it by further reducing the temperature but failed, because helium does not solidify at atmospheric pressure. "
            "Onnes' student Willem Hendrik Keesom was eventually able to solidify 1 cm3 of helium in 1926 by applying additional external pressure. [...] "
            "Unlike any other element, however, helium remains liquid down to a temperature of absolute zero. "
            "This is a direct effect of quantum mechanics: specifically, the zero point energy of the system is too high to allow freezing. [...] "
            "Helium II will escape from a vessel that is not sealed by creeping along the sides until it reaches a warmer region where it evaporates. "
            "It moves in a 30 nm-thick film regardless of surface material. [...] "
            "Helium remains liquid down to absolute zero at atmospheric pressure, but it freezes at high pressure. "
            "Solid helium requires a temperature of 1–1.5 K (about −272 °C or −457 °F) at about 25 bar (2.5 MPa) of pressure. "
            "It is often hard to distinguish solid from liquid helium since the refractive index of the two phases are nearly the same. "
            "The solid has a sharp melting point and has a crystalline structure, but it is highly compressible; applying pressure in a laboratory can decrease its volume by more than 30%.",
            nome="Helium")],
    },
    # 12 gelo a milhares de graus
    {
        "temas_secundarios": ["sistema_solar", "estados_materia"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Existe gelo a milhares de graus. Em 2019, lasers espremeram água a milhões de atmosferas e criaram, por bilionésimos de segundo, um gelo \"superiônico\", que pode formar uma camada dentro de Urano e Netuno.",
        "explicacao": (
            "Gelo é água com as moléculas presas num cristal, e isso não exige frio: basta pressão suficiente. Há "
            "mais de 30 anos, físicos previram que, esmagada com força extrema, a água viraria um material "
            "superiônico, meio sólido e meio líquido. Os átomos de oxigênio formam uma rede cristalina, enquanto os "
            "núcleos de hidrogênio, os prótons, circulam livres por ela como um líquido. Isso torna esse gelo quase "
            "tão bom condutor de eletricidade quanto um metal, e ele seria preto. Em 2019, uma equipe do laboratório "
            "Lawrence Livermore usou seis feixes de laser gigantes para mandar ondas de choque por uma camada fina "
            "de água, a pressões de 1 a 4 milhões de vezes a do nível do mar e temperatura de metade da superfície "
            "do Sol. Flashes de raios X, disparados no momento exato, mostraram que o oxigênio tinha se arrumado em "
            "cristal, e a equipe propôs chamar a nova forma de gelo XVIII. Um físico de fora pediu mais testes para "
            "comprovar de vez o caráter superiônico. Se essa camada existe nos gigantes de gelo, ela pode ajudar a "
            "explicar os campos magnéticos tortos de Urano e Netuno."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": "https://www.nationalgeographic.com/science/2019/05/bizarre-hot-ice-xviii-seen-on-earth-superionic-uranus-neptune/",
             "titulo": "Bizarre form of hot ice seen on Earth (National Geographic, 2019)",
             "idioma": "en",
             "trecho": "As the team reports today in the journal Nature, this ice exists at pressures between one and four million times that at sea level and temperatures half as hot as the surface of the sun. "
                       "“Yes, we’re talking about ice,” says study leader Marius Millot, a physicist at Lawrence Livermore National Laboratory in California. "
                       "“But the sample is at several thousand degrees.” [...] "
                       "And more than 30 years ago, physicists predicted that crushing pressure should squeeze water into superionic forms. "
                       "Superionic materials are dual beasts, part solid and part liquid [...] "
                       "In water—aka H2O—the oxygen atoms would crunch into a solidified crystal while the hydrogen’s protons would zip around like a liquid. [...] "
                       "In their latest tests, the researchers used six giant laser beams to generate a sequence of shockwaves that crunched a thin layer of liquid water into solidified ice at millions of times Earth’s surface pressure and between 3,000 and 5,000 degrees Fahrenheit. "
                       "Precisely timed x-ray flashes probed the configuration, which again only lasted for a few billionths of a second, and revealed that the oxygen atoms had indeed taken on a crystalline form. [...] "
                       "The team has proposed calling this new formation Ice XVIII. "
                       "While there was some overlap in conditions between the team’s two experiments, more investigations will be necessary to definitively prove that the ice is superionic, says Roberto Car, a Princeton University physicist who was not involved in the work. [...] "
                       "The new experiments indicate that Uranus and Neptune should have a superionic ice layer that acts like our planet’s mantle [...] "
                       "And that could help explain why they have unusual magnetic fields."},
            wiki("Superionic_water",
                "In superionic water, water molecules break apart and the oxygen ions crystallize into an evenly spaced lattice while the hydrogen ions float around freely within the oxygen lattice. "
                "The freely mobile hydrogen ions make superionic water almost as conductive as typical metals, making it a superionic conductor. "
                "The ice appears black in color. [...] "
                "The first definitive evidence for the crystal structure of the oxygen lattice in superionic water came from x-ray measurements on laser-shocked water which were reported in 2019.",
                nome="Ice (fases), seção Superionic water"),
        ],
    },
    # 13 a coisa mais quente já feita é um líquido quase perfeito
    {
        "temas_secundarios": ["fisica_particulas", "cosmologia"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "A matéria mais quente já criada, uma sopa de quarks feita no CERN em 2012 a mais de 5 trilhões de graus, não se comporta como gás: esse tipo de matéria flui como um líquido quase perfeito, quase sem atrito interno.",
        "explicacao": (
            "Prótons e nêutrons são feitos de partículas menores, os quarks, colados por glúons. Acima de cerca de "
            "1,66 trilhão de kelvin, esses blocos \"derretem\" e os quarks e glúons ficam soltos num plasma. "
            "Acredita-se que o universo inteiro esteve nesse estado logo depois do Big Bang. Para recriá-lo, o "
            "experimento ALICE, no Grande Colisor de Hádrons, choca íons de chumbo a 99% da velocidade da luz. Em "
            "13 de agosto de 2012, a equipe anunciou ter passado de 5 trilhões de kelvin, talvez 5,5 trilhões, uns "
            "38% acima do recorde anterior, de 4 trilhões, obtido em 2010 nos EUA. O porta-voz avisou que a medida "
            "ainda era bastante incerta. A surpresa maior tinha vindo antes: os teóricos esperavam algo parecido "
            "com um gás de partículas livres, mas experimentos no colisor RHIC, nos EUA, mostraram em 2005 que o "
            "plasma se comporta como líquido. Os experimentos do RHIC indicaram que ele resiste menos ao escoamento do "
            "que qualquer outra substância conhecida: é o líquido mais perfeito já observado em laboratório."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.guinnessworldrecords.com/world-records/highest-man-made-temperature",
             "titulo": "Highest artificial temperature (Guinness World Records)",
             "idioma": "en",
             "trecho": "On 13 August 2012 scientists at CERN’s Large Hadron Collider, Geneva, Switzerland, announced that they had achieved temperatures of over 5 trillion K and perhaps as high as 5.5 trillion K. "
                       "The team had been using the ALICE experiment to smash together lead ions at 99% of the speed of light to create a quark gluon plasma – an exotic state of matter believed to have filled the universe just after the Big Bang."},
            {"url": "https://blogs.nature.com/blog/hot-stuff-cern-physicists-create-record-breaking-subatomic-soup/",
             "titulo": "Hot stuff: CERN physicists create record-breaking subatomic soup (Nature blogs, 2012)",
             "idioma": "en",
             "trecho": "have achieved the hottest manmade temperatures ever, by colliding lead ions to momentarily create a quark–gluon plasma [...] "
                       "say that they have achieved a quark–gluon plasma 38% hotter than a record 4-trillion-degree plasma achieved in 2010 by a similar experiment at Brookhaven National Laboratory in New York, which had been anointed the Guinness record holder. "
                       "ALICE spokesman Paolo Giubellino says that the team’s measurement is relatively uncertain"},
            wiki("Quark%E2%80%93gluon_plasma",
                "It is a very low viscosity liquid composed of the elementary particles, quarks and gluons [...] "
                "A series of Au-Au collision studies from the RHIC published in 2005 showed that the collisions produce something like a liquid in contrast to early theoretical models. [...] "
                "RHIC experiments have shown that this is the most perfect liquid ever observed in any laboratory experiment at any scale. "
                "The new phase of matter, consisting of dissolved hadrons, exhibits less resistance to flow than any other known substance. [...] "
                "the resulting matter does not behave as a quasi-ideal state of free quarks and gluons, but, rather, as an almost perfect dense fluid. [...] "
                "which amounts to a temperature exceeding 1.66 trillion K.",
                nome="Quark–gluon plasma"),
        ],
    },
    # 14 entropia: a palavra feita para não dizer nada
    {
        "temas_secundarios": ["historia_computacao", "palavras_viajantes"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "Clausius criou a palavra \"entropia\" em 1865 imitando de propósito \"energia\". Décadas depois, segundo um relato, von Neumann sugeriu o nome a Shannon porque \"ninguém sabe o que a entropia é de verdade\".",
        "explicacao": (
            "O físico alemão Rudolf Clausius, um dos fundadores da termodinâmica, precisava de um nome para a "
            "grandeza que mede, grosso modo, a energia que se perde para o trabalho útil. Preferiu buscar nas "
            "línguas antigas, para que o termo significasse o mesmo em todos os idiomas vivos, e partiu da palavra "
            "grega para \"transformação\", tropé. Depois explicou que escolheu \"entropia\" para soar parecida com "
            "\"energia\", porque as duas grandezas seriam muito análogas no sentido físico. O físico Leon Cooper "
            "comentou, com ironia, que assim Clausius cunhou uma palavra que significava a mesma coisa para todo "
            "mundo: nada. A palavra ganhou outro destino no século XX. Claude Shannon, ao criar a teoria da "
            "informação, procurava nome para a sua medida de incerteza e pensou em \"informação\" ou \"incerteza\". "
            "Segundo um dos relatos, von Neumann o aconselhou a usar \"entropia\" por dois motivos: a fórmula já "
            "existia com esse nome na mecânica estatística, e, mais importante, como ninguém sabe o que a entropia "
            "é de verdade, num debate ele sempre levaria vantagem. Há outra versão da conversa, com palavras "
            "diferentes, e o próprio relato diz que Shannon talvez nem conhecesse bem a semelhança com a "
            "termodinâmica."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Entropy",
                "In 1865, German physicist Rudolf Clausius, one of the leading founders of the field of thermodynamics [...] "
                "I prefer going to the ancient languages for the names of important scientific quantities, so that they may mean the same thing in all living tongues. "
                "I propose, therefore, to call S the entropy of a body, after the Greek word \"transformation\". "
                "I have designedly coined the word entropy to be similar to energy, for these two quantities are so analogous in their physical significance, that an analogy of denominations seems to me helpful. "
                "Leon Cooper added that in this way \"he succeeded in coining a word that meant the same thing to everybody: nothing\". [...] "
                "From the prefix en-, as in 'energy', and from the Greek word τροπή [tropē], which is translated in an established lexicon as turning or change",
                nome="Entropy"),
            wiki("History_of_entropy",
                "that Shannon was not particularly aware of the close similarity between his new quantity and earlier work in thermodynamics. [...] "
                "During their discussions, regarding what Shannon should call the \"measure of uncertainty\" or attenuation in phone-line signals with reference to his new information theory, according to one source: "
                "My greatest concern was what to call it. I thought of calling it ‘information’, but the word was overly used, so I decided to call it ‘uncertainty’. "
                "When I discussed it with John von Neumann, he had a better idea. "
                "Von Neumann told me, ‘You should call it entropy, for two reasons: In the first place your uncertainty function has been used in statistical mechanics under that name, so it already has a name. "
                "In the second place, and more important, nobody knows what entropy really is, so in a debate you will always have the advantage. "
                "According to another source, when von Neumann asked him how he was getting on with his information theory",
                nome="History of entropy"),
        ],
    },
    # 15 Kelvin e a idade da Terra calculada pelo resfriamento
    {
        "temas_secundarios": ["geologia_profunda", "evolucao"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Lord Kelvin calculou a idade da Terra pelo tempo que ela levaria para esfriar e chegou a 20 a 40 milhões de anos. Faltaram a radioatividade, então desconhecida, e o calor levado pela convecção no manto.",
        "explicacao": (
            "Em 1862, William Thomson, o futuro Lord Kelvin, supôs que a Terra nasceu toda derretida e calculou "
            "quanto tempo ela levaria para chegar ao ritmo atual de aumento da temperatura com a profundidade. A "
            "primeira estimativa ia de 20 a 400 milhões de anos. Com o tempo, ele a estreitou: em 1897, disse que a "
            "Terra tinha mais de 20 e menos de 40 milhões de anos, provavelmente mais perto de 20. O cálculo deixava "
            "de fora duas coisas. Uma era o calor gerado pela radioatividade, processo ainda desconhecido. A outra, "
            "mais importante, era a convecção no interior do planeta, que mantém o manto superior quente por muito "
            "mais tempo. Em 1895, o engenheiro John Perry já contestava as suposições de Kelvin sobre a condução do "
            "calor. Em 1904, Ernest Rutherford, que falava sobre radioatividade, viu Kelvin na plateia, notou o "
            "velho físico acordar na parte crítica e saiu-se com elegância: Kelvin teria limitado a idade da Terra "
            "\"desde que nenhuma nova fonte fosse descoberta\", e essa fonte era o rádio. Hoje, com datação "
            "radiométrica de meteoritos, a idade estimada é de 4,54 bilhões de anos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Age_of_the_Earth",
            "The age of Earth is estimated to be 4.54 ± 0.05 billion years. [...] "
            "Estimates are based on radiometric dating of meteoritic material [...] "
            "In 1862, the physicist William Thomson, 1st Baron Kelvin published calculations that fixed the age of Earth at between 20 million and 400 million years. "
            "He assumed that Earth had formed as a completely molten object, and determined the amount of time it would take for the near-surface temperature gradient to decrease to its present value. "
            "His calculations did not account for heat produced via radioactive decay (a then unknown process) or, more significantly, convection inside Earth, which allows the temperature in the upper mantle to remain high much longer [...] "
            "In 1895 John Perry challenged Kelvin's figure on the basis of his assumptions on conductivity [...] "
            "The last estimate Kelvin gave, in 1897, was: \"that it was more than 20 and less than 40 million year old, and probably much nearer 20 than 40\". [...] "
            "Rutherford wrote of addressing a meeting of the Royal Institution in 1904: "
            "I came into the room, which was half dark, and presently spotted Lord Kelvin in the audience and realized that I was in trouble at the last part of my speech dealing with the age of the Earth, where my views conflicted with his. "
            "To my relief, Kelvin fell fast asleep, but as I came to the important point, I saw the old bird sit up, open an eye, and cock a baleful glance at me! "
            "Then a sudden inspiration came, and I said, \"Lord Kelvin had limited the age of the Earth, provided no new source was discovered. "
            "That prophetic utterance refers to what we are now considering tonight, radium!\"",
            nome="Age of the Earth")],
    },
]
