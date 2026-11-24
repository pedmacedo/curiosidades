LOTE = "2026-11-23-fisica_particulas-01"
AREA = "fisica_quimica"
TEMA = "fisica_particulas"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o neutrino "mais rápido que a luz" e o cabo solto
    {
        "temas_secundarios": ["relatividade"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 2011, um experimento anunciou neutrinos mais rápidos que a luz, o que desafiaria Einstein. A explicação apareceu meses depois: um cabo de fibra óptica mal encaixado no relógio do detector.",
        "explicacao": (
            "O experimento OPERA usava um feixe de neutrinos que saía do CERN, na fronteira entre França e Suíça, e "
            "chegava a um detector no laboratório de Gran Sasso, na Itália, a mais de 730 km. Em setembro de 2011, a "
            "equipe anunciou que as partículas chegavam cerca de 60,7 nanossegundos antes do que a luz levaria no "
            "vácuo, uma vantagem de mais ou menos uma parte em 40 mil. A estatística parecia sólida, mas ela media "
            "precisão, não exatidão: não protegia contra um cálculo errado ou um instrumento com defeito. Os "
            "cientistas convidaram a comunidade de físicos a examinar o trabalho em detalhe. Em fevereiro de 2012, a "
            "colaboração apontou duas falhas. A principal estava na ligação entre um receptor de GPS e o relógio "
            "mestre: o cabo de fibra não estava totalmente atarraxado, o que reduzia em 73 nanossegundos o tempo de "
            "voo registrado. Pesquisadores de um detector vizinho, o LVD, reforçaram o diagnóstico comparando os "
            "horários de múons de raios cósmicos que atravessavam os dois aparelhos. Com as correções, a velocidade "
            "dos neutrinos ficou compatível com a da luz. Em março de 2012, o porta-voz e o coordenador de física "
            "deixaram seus cargos de liderança no experimento."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("2011_OPERA_faster-than-light_neutrino_anomaly",
            "In 2011, the Oscillation Project with Emulsion-tRacking Apparatus (OPERA) experiment mistakenly observed neutrinos appearing to travel faster than light. [...] "
            "The experiment created a form of neutrinos, muon neutrinos, at CERN's older SPS accelerator, on the Franco–Swiss border, and detected them at the LNGS lab in Gran Sasso, Italy. [...] "
            "The neutrinos were calculated to have arrived approximately 60.7 nanoseconds (60.7 billionths of a second) sooner than light would have if traversing the same distance in vacuum. "
            "After six months of cross checking, on  September 23, 2011, the researchers announced that neutrinos had been observed traveling at faster-than-light speed. [...] "
            "The particles were measured arriving at the detector faster than light by approximately one part per 40,000 [...] "
            "It was, however, a measure of precision, not accuracy, which could be influenced by elements such as incorrect computations or wrong readouts of instruments. [...] "
            "the scientists were \"inviting the broader physics community to look at what they [had] done and really scrutinize it in great detail [...] "
            "In February 2012, the OPERA collaboration announced two possible sources of error that could have significantly influenced the results. "
            "A link from a GPS receiver to the OPERA master clock was loose, which increased the delay through the fiber. "
            "The glitch's effect was to decrease the reported flight time of the neutrinos by 73 ns, making them seem faster than light. [...] "
            "In March 2012 an LNGS seminar was held, confirming the fiber cable was not fully screwed in during data gathering. "
            "LVD researchers compared the timing data for cosmic high-energy muons hitting both the OPERA and the nearby LVD detector [...] "
            "Correcting for the two newly found sources of error, results for neutrino speed appear to be consistent with the speed of light. [...] "
            "spokesperson Ereditato and physics coordinator Autiero resigned their leadership positions anyway on March 30, 2012. [...] "
            "The source at CERN was more than 730 kilometres (450 mi) away from the detector at LNGS (Gran Sasso).",
            nome="2011 OPERA faster-than-light neutrino anomaly")],
    },
    # 2 Pauli, a carta aos "radioativos" e o telegrama
    {
        "temas_secundarios": ["personagens_esquecidos", "palavras_viajantes"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "O neutrino foi proposto em 1930 numa carta que começava com \"Prezadas senhoras e senhores radioativos\". Quando enfim foi detectado, em 1956, o autor, Wolfgang Pauli, respondeu: \"Tudo chega para quem sabe esperar\".",
        "explicacao": (
            "Pauli tentava resolver um enigma do decaimento beta, em que um núcleo atômico emite um elétron. A energia "
            "desse elétron variava de um caso para outro, como se parte dela sumisse, e Niels Bohr chegou a propor que "
            "a conservação de energia talvez não valesse em cada decaimento isolado. Na carta de 4 de dezembro de 1930, "
            "dirigida a Lise Meitner e outros colegas, Pauli sugeriu outra saída: uma partícula neutra, nunca observada, "
            "de massa pequena, que levaria a energia que faltava. Ele a chamou de \"nêutron\", mas em 1932 James "
            "Chadwick deu esse nome a uma partícula bem mais pesada. A palavra \"neutrino\", o \"pequeno neutro\" em "
            "italiano, foi inventada de brincadeira por Edoardo Amaldi numa conversa com Enrico Fermi, em Roma, e Fermi "
            "a usou em congressos. A detecção direta só veio em 1956, quando Clyde Cowan, Frederick Reines e colegas "
            "captaram antineutrinos produzidos num reator nuclear. Pauli soube do resultado dois anos e meio antes de "
            "morrer e agradeceu por telegrama, com a frase sobre saber esperar. Reines recebeu o Nobel de 1995 pelo "
            "trabalho com neutrinos; Cowan tinha morrido em 1974."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Wolfgang_Pauli",
                "In 1930, Pauli considered the problem of beta decay. In a letter of 4 December to Lise Meitner et al., beginning, \"Dear radioactive ladies and gentlemen\", "
                "he proposed the existence of a hitherto unobserved neutral particle with a small mass, no greater than 1% the mass of a proton, to explain the continuous spectrum of beta decay. [...] "
                "The neutrino was first confirmed experimentally in 1956 by Frederick Reines and Clyde Cowan, two and a half years before Pauli's death. "
                "On receiving the news, he replied by telegram: \"Thanks for message. Everything comes to him who knows how to wait. Pauli.\"",
                nome="Wolfgang Pauli"),
            wiki("Neutrino",
                "Many exotic suggestions were discussed, including one from Niels Bohr, who proposed abandoning energy conservation in individual decays while maintaining a statistical version of the law. [...] "
                "Pauli hypothesized an undetected particle that he called a \"neutron\" [...] "
                "James Chadwick discovered a much more massive neutral nuclear particle in 1932 and named it a neutron also, leaving two kinds of particles with the same name. "
                "The word \"neutrino\" entered the scientific vocabulary through Enrico Fermi, who used it during a conference in Paris in July 1932 and at the Solvay Conference in October 1933 [...] "
                "The name (the Italian equivalent of \"little neutral one\") was jokingly coined by Italian physicist Edoardo Amaldi during a conversation with Fermi at the Institute of Physics of via Panisperna in Rome [...] "
                "In the 20 July 1956 issue of Science, Clyde Cowan, Frederick Reines, Francis B. \"Kiko\" Harrison, Herald W. Kruse, and Austin D. McGuire published confirmation that they had detected the neutrino [...] "
                "antineutrinos created in a nuclear reactor by beta decay reacted with protons to produce neutrons and positrons",
                nome="Neutrino"),
            wiki("Cowan–Reines_neutrino_experiment",
                "Only the resulting electron was observed, so its varying energy suggested that energy may not be conserved. [...] "
                "Clyde Cowan died in 1974 at the age of 54. In 1995, Frederick Reines was honored with the Nobel Prize for his work on neutrino physics.",
                nome="Cowan–Reines neutrino experiment"),
        ],
    },
    # 3 a partícula Oh-My-God
    {
        "temas_secundarios": ["galaxias", "cosmologia"],
        "tipos_espanto": ["escala_absurda", "misterio_aberto"],
        "gancho": "Em 1991, um detector nos EUA captou uma única partícula vinda do espaço com a energia de uma bola de beisebol a 100 km/h. Apelidada de \"partícula Oh-My-God\", até hoje não se sabe que partícula era.",
        "explicacao": (
            "O raio cósmico foi registrado em 15 de outubro de 1991 pela câmera Fly's Eye, no campo de provas militar "
            "de Dugway, em Utah. Sua energia foi estimada em cerca de 320 exaelétron-volts, a maior já medida num raio "
            "cósmico: o equivalente a uma bola de beisebol de 140 gramas a uns 100 km/h, concentrado numa só partícula "
            "subatômica. Isso é uns 40 milhões de vezes a energia dos prótons mais energéticos já produzidos num "
            "acelerador na Terra. Se fosse um próton, ela correria tão perto da velocidade da luz que um fóton viajando "
            "ao lado levaria mais de 245 mil anos para abrir 1 centímetro de vantagem. A maioria dos raios cósmicos de "
            "alta energia é feita de prótons, mas não se sabe o que era essa partícula, e a energia dela pôs em dúvida "
            "as teorias da época sobre a origem e a propagação dos raios cósmicos. Desde então, centenas de eventos "
            "parecidos foram registrados. Em 2021, outro observatório em Utah captou a partícula Amaterasu, com mais "
            "de 240 exaelétron-volts. Ela parece ter vindo do Vazio Local, uma região quase vazia que faz fronteira com "
            "a Via Láctea, e nenhum objeto astronômico promissor foi encontrado naquela direção."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Oh-My-God_particle",
            "The Oh-My-God particle (as physicists dubbed it) was an ultra-high-energy cosmic ray detected on 15 October 1991 by the Fly's Eye camera in Dugway Proving Ground, Utah, United States. "
            "As of 2026, it is the highest-energy cosmic ray ever observed. [...] (320 exaelectronvolt). "
            "The particle's energy was unexpected and called into question prevailing theories about the origin and propagation of cosmic rays. [...] "
            "Although most high-energy cosmic rays are protons, it is not known what the ultra-high-energy Oh-My-God particle was. [...] "
            "so if a photon were traveling alongside the proton, it would take over 245,000 years for the photon to gain a 1 cm lead [...] "
            "The energy of the particle was some 40 million times that of the highest-energy protons that have been produced in any terrestrial particle accelerator. [...] "
            "equivalent to a 140-gram (5 oz) baseball travelling at about 28 m/s (100 km/h; 63 mph). [...] "
            "Since the first observation, hundreds of similar events [...] "
            "The Amaterasu particle, named after the sun goddess in Japanese mythology, was detected in 2021 and later identified in 2023, using the Telescope Array observatory in Utah, United States. "
            "It had an energy exceeding 240 exa-electron volts [...] "
            "This particle appears to have emerged from the Local Void, an empty area of space bordering the Milky Way galaxy. [...] "
            "No promising astronomical object matching the direction from which the cosmic ray arrived has been identified.",
            nome="Oh-My-God particle")],
    },
    # 4 Hess, o balão e o eclipse
    {
        "temas_secundarios": ["atmosfera", "historia_astronomia"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 1912, o físico Victor Hess subiu de balão a 5.300 metros e viu a radiação do ar dobrar lá no alto. Voou até durante um eclipse quase total, para descartar o Sol. Tinha descoberto os raios cósmicos.",
        "explicacao": (
            "Depois da descoberta da radioatividade, em 1896, a ionização do ar era atribuída à radiação de elementos "
            "radioativos do solo e aos gases que eles liberam, como o radônio. Mas havia sinais estranhos. Em 1909, "
            "Theodor Wulf mediu mais radiação no alto da Torre Eiffel do que na base, num artigo que não foi muito "
            "aceito. Hess primeiro aumentou muito a precisão dos instrumentos e depois decidiu levá-los ele mesmo ao "
            "céu. Entre 1911 e 1912, fez voos de balão de dia e de noite, correndo riscos consideráveis. Num deles, "
            "levou três eletrômetros a 5.300 metros e viu a taxa de ionização chegar ao dobro da medida no chão. Para "
            "testar se a fonte era o Sol, subiu durante um eclipse quase total: com a Lua bloqueando boa parte da luz "
            "solar, a radiação continuou aumentando com a altitude. Ele concluiu que uma radiação muito penetrante "
            "entrava na atmosfera vinda de cima. A descoberta abriu caminho para outras: o pósitron e o múon foram "
            "achados primeiro em raios cósmicos, ambos por Carl Anderson. Hess e Anderson dividiram o Nobel de Física "
            "de 1936."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Cosmic_ray",
                "After the discovery of radioactivity by Henri Becquerel in 1896, it was generally believed that atmospheric electricity, ionization of the air, was caused only by radiation from radioactive elements in the ground or the radioactive gases or isotopes of radon they produce. [...] "
                "In 1909, Theodor Wulf developed an electrometer, a device to measure the rate of ion production inside a hermetically sealed container, and used it to show higher levels of radiation at the top of the Eiffel Tower than at its base. "
                "However, his paper published in Physikalische Zeitschrift was not widely accepted. [...] "
                "In 1912, Victor Hess carried three enhanced-accuracy Wulf electrometers to an altitude of 5,300 metres in a free balloon flight. "
                "He found the ionization rate increased to twice the rate at ground level. "
                "Hess ruled out the Sun as the radiation's source by making a balloon ascent during a near-total eclipse. "
                "With the moon blocking much of the Sun's visible radiation, Hess still measured rising radiation at rising altitudes. "
                "He concluded that \"The results of the observations seem most likely to be explained by the assumption that radiation of very high penetrating power enters from above into our atmosphere.\"",
                nome="Cosmic ray"),
            wiki("Victor_Francis_Hess",
                "He approached this mystery first by greatly increasing the precision of the measuring equipment, and then by personally taking the equipment aloft in a balloon. "
                "He systematically measured the radiation at altitudes up to 5.3 kilometres (3.3 mi) during 1911–1912. "
                "The daring flights were made both by day and during the night, at significant risk to himself. [...] "
                "In particular, both the positron and the muon were first discovered in cosmic rays by Carl David Anderson. "
                "In 1936, Hess and Anderson shared the Nobel Prize in Physics for their discoveries of cosmic rays and the positron, respectively.",
                nome="Victor Francis Hess"),
        ],
    },
    # 5 Dirac prevê, Anderson fotografa: o pósitron
    {
        "temas_secundarios": ["mecanica_quantica", "historia_matematica"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "A antimatéria foi prevista antes de ser vista: uma equação de Paul Dirac admitia um elétron de carga positiva, e em 1932 Carl Anderson o fotografou em raios cósmicos. Outros já tinham visto os rastros sem entendê-los.",
        "explicacao": (
            "Em 1928, Dirac publicou uma equação que unia a mecânica quântica, a relatividade especial e o spin para "
            "descrever o elétron. Havia um incômodo: além das soluções de energia positiva, ela admitia outras, de "
            "energia negativa, que a mecânica quântica não deixava simplesmente ignorar. Dirac argumentou que um "
            "elétron de energia negativa se moveria como se tivesse carga positiva e chegou a cogitar que essa "
            "partícula fosse o próton, embora admitisse que a massa muito maior do próton era um problema. Robert "
            "Oppenheimer objetou que, nesse caso, o átomo de hidrogênio se autodestruiria rapidamente. Convencido, "
            "Dirac previu em 1931 um \"antielétron\", com a massa do elétron e carga oposta, que se aniquilaria ao "
            "encontrá-lo. Em 2 de agosto de 1932, Anderson, que fazia raios cósmicos atravessarem uma câmara de "
            "nuvens com uma placa de chumbo, cercada por um ímã, viu rastros com a curvatura de um elétron, mas "
            "desviando para o lado de uma carga positiva. Era a primeira evidência de antimatéria. Rastros parecidos "
            "já tinham sido observados por Dmitri Skobeltsyn desde 1923, sem explicação na época, e o casal "
            "Joliot-Curie tinha indícios de pósitrons em fotos antigas, mas os havia tomado por prótons. Anderson "
            "recebeu o Nobel de Física de 1936."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Positron",
            "In 1928, Paul Dirac published a paper proposing that electrons can have both a positive and negative charge. "
            "This paper introduced the Dirac equation, a unification of quantum mechanics, special relativity, and the then-new concept of electron spin to explain the Zeeman effect. [...] "
            "The positive-energy solution explained experimental results, but Dirac was puzzled by the equally valid negative-energy solution that the mathematical model allowed. "
            "Quantum mechanics did not allow the negative energy solution to simply be ignored [...] "
            "He argued that \"... an electron with negative energy moves in an external [electromagnetic] field as though it carries a positive charge.\" [...] "
            "The paper also explored the possibility of the proton being an island in this sea, and that it might actually be a negative-energy electron. "
            "Dirac acknowledged that the proton having a much greater mass than the electron was a problem [...] "
            "Robert Oppenheimer argued strongly against the proton being the negative-energy electron solution to Dirac's equation. "
            "He asserted that if it were, the hydrogen atom would rapidly self-destruct. [...] "
            "Dirac published a paper in 1931 that predicted the existence of an as-yet-unobserved particle that he called an \"anti-electron\" that would have the same mass and the opposite charge as an electron and that would mutually annihilate upon contact with an electron. [...] "
            "Beginning in 1923, while using a Wilson cloud chamber to study the Compton effect, Dmitri Skobeltsyn observed tracks that acted like electrons but curved in the opposite direction in an applied magnetic field. [...] "
            "no one at the time had an explanation for these anomalous tracks. [...] "
            "Anderson discovered the positron on 2 August 1932, for which he won the Nobel Prize for Physics in 1936. [...] "
            "The positron was the first evidence of antimatter and was discovered when Anderson allowed cosmic rays to pass through a cloud chamber and a lead plate. "
            "A magnet surrounded this apparatus, causing particles to bend in different directions based on their electric charge. "
            "The ion trail left by each positron appeared on the photographic plate with a curvature matching the mass-to-charge ratio of an electron, but in a direction that showed its charge was positive. [...] "
            "Frédéric and Irène Joliot-Curie in Paris had evidence of positrons in old photographs when Anderson's results came out, but they had dismissed them as protons.",
            nome="Positron")],
    },
    # 6 o corpo fabrica antimatéria (e o mistério da assimetria)
    {
        "temas_secundarios": ["anatomia", "cosmologia"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "Seu corpo fabrica antimatéria: o potássio radioativo que todos temos gera uns 4 mil pósitrons por dia. Mas por que o universo é quase só matéria, e não meio a meio, segue sendo um dos grandes mistérios da física.",
        "explicacao": (
            "Uma fração pequena do potássio natural, cerca de 0,0117%, é potássio-40, um isótopo radioativo de vida "
            "longa, primordial. Mesmo sendo tão raro, ele é o radioisótopo mais abundante no corpo humano: numa pessoa "
            "de 70 kg, uns 4.400 núcleos de potássio-40 se desintegram a cada segundo. Em cerca de 0,001% desses "
            "decaimentos sai um pósitron, a antipartícula do elétron, o que soma uns 4 mil pósitrons por dia. Cada um "
            "logo encontra um elétron, os dois se aniquilam e viram um par de fótons, num processo parecido, mas muito "
            "mais fraco, com o que acontece num exame de PET nos hospitais. As bananas também carregam potássio-40, e "
            "por isso existe até uma medida informal de radiação, a \"dose equivalente a uma banana\". Antimatéria, "
            "portanto, não é coisa só de laboratório. O enigma aparece na escala do cosmo: há fortes evidências de que "
            "o universo observável é feito quase inteiramente de matéria comum. Essa assimetria entre matéria e "
            "antimatéria é um dos grandes problemas sem solução da física, e a física de partículas do modelo do Big "
            "Bang não consegue explicar por que sobrou mais matéria do que antimatéria."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Positron",
                "Perhaps the best known naturally occurring radioisotope which produces positrons is potassium-40, a long-lived isotope of potassium which occurs as a primordial isotope of potassium. "
                "Even though it is a small percentage of potassium (0.0117%), it is the single most abundant radioisotope in the human body. "
                "In a human body of 70 kg (150 lb) mass, about 4,400 nuclei of 40K decay per second. [...] "
                "About 0.001% of these 40K decays produce about 4,000 natural positrons per day in the human body. "
                "These positrons soon find an electron, undergo annihilation, and produce pairs of 511 keV photons, in a process similar (but much lower intensity) to that which happens during a PET scan nuclear medicine procedure. [...] "
                "The positron or antielectron is the particle with an electric charge of +1e, a spin of 1/2 ħ (the same as the electron), and the same mass as an electron. It is the antiparticle (antimatter counterpart) of the electron.",
                nome="Positron"),
            wiki("Banana_equivalent_dose",
                "general educational example to compare a dose of radioactivity to the dose one is exposed to by eating one average-sized banana. "
                "Bananas contain naturally occurring radioactive isotopes, particularly potassium-40 (40K), one of several naturally occurring isotopes of potassium.",
                nome="Banana equivalent dose"),
            wiki("Antimatter",
                "There is strong evidence that the observable universe is composed almost entirely of ordinary matter, as opposed to an equal mixture of matter and antimatter. "
                "This asymmetry of matter and antimatter in the visible universe is one of the great unsolved problems in physics. [...] "
                "the particle physics of the Big Bang model cannot explain why our universe has more matter than antimatter.",
                nome="Antimatter"),
        ],
    },
    # 7 o Higgs não dá a maior parte da massa
    {
        "temas_secundarios": ["relatividade", "cosmologia"],
        "tipos_espanto": ["contraintuitivo", "mito_desmentido"],
        "gancho": "Não é o bóson de Higgs que dá a maior parte da massa de prótons e nêutrons. A massa dos quarks é só cerca de 1% do total; o resto é energia dos quarks em movimento e dos glúons que os mantêm unidos.",
        "explicacao": (
            "O campo de Higgs, cuja partícula foi anunciada no CERN em 4 de julho de 2012, dá massa de repouso às "
            "partículas elementares do Modelo Padrão: cada uma ganha uma massa que depende de quão fortemente "
            "interage com o campo. É ele que está por trás da massa dos quarks e dos elétrons. Mas prótons e nêutrons "
            "não são elementares. Um próton tem dois quarks up e um down, e a soma das massas de repouso desses três "
            "quarks dá só cerca de 1% da massa dele. O restante, perto de 99%, vem da energia de ligação descrita pela "
            "cromodinâmica quântica, a teoria da força nuclear forte. Ela inclui a energia cinética dos quarks e a "
            "energia dos campos de glúons, partículas sem massa de repouso que prendem os quarks uns aos outros. Por "
            "isso se diz que a maior parte da massa de prótons e nêutrons é explicada pela relatividade especial, e "
            "não pelo Higgs. É comum o engano de achar que o bóson de Higgs responde pela massa em geral, quando quem "
            "dá massa é o campo, e que ele explicaria a maior parte da massa do universo."
        ),
        "nivel": 3, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Proton",
                "Protons are composed of two up quarks of charge +⁠2/3⁠e each, and one down quark of charge −⁠1/3⁠e. "
                "The rest masses of quarks contribute only about 1% of a proton's mass. "
                "The remainder of a proton's mass is due to quantum chromodynamics binding energy, which includes the kinetic energy of the quarks and the energy of the gluon fields that bind the quarks together. [...] "
                "In quantum chromodynamics, the modern theory of the nuclear force, most of the mass of protons and neutrons is explained by special relativity. "
                "The mass of a proton is about 80–100 times greater than the sum of the rest masses of its three valence quarks, while the gluons have zero rest mass.",
                nome="Proton"),
            wiki("Higgs_boson",
                "via the Higgs mechanism, gives a rest mass to all massive elementary particles of the Standard Model, including the Higgs boson itself. [...] "
                "elementary particles acquire a consistent mass based on how strongly they interact with the Higgs field. [...] "
                "On 4 July 2012, the discovery of a new particle with a mass between 125 and 127 GeV/c2 was announced [...] "
                "The Higgs field is pivotal in generating the masses of quarks and charged leptons (through Yukawa coupling) [...] "
                "approximately 99% of the mass of baryons (composite particles such as the proton and neutron) is due instead to quantum chromodynamic binding energy, which is the sum of the kinetic energies of quarks and the energies of the massless gluons mediating the strong interaction inside the baryons. [...] "
                "The Higgs boson is commonly misunderstood as responsible for mass, rather than the Higgs field, and as relating to most mass in the universe.",
                nome="Higgs boson"),
        ],
    },
    # 8 "partícula de Deus": culpa do editor
    {
        "temas_secundarios": ["palavras_viajantes", "religioes"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O bóson de Higgs ganhou o apelido de \"partícula de Deus\" por causa de um editor. O físico Leon Lederman queria chamar seu livro de \"A Partícula Maldita\", e a editora achou o título polêmico demais.",
        "explicacao": (
            "Lederman, ganhador do Nobel de Física e diretor do Fermilab, lançou o livro em 1993. Ele o escreveu "
            "enquanto o governo americano retirava o apoio ao Supercolisor Supercondutor, um acelerador gigantesco, "
            "parcialmente construído, que ele defendia desde o início do projeto, em 1983, e que foi cancelado em "
            "1993; o livro queria mostrar por que aquela máquina importava. No texto, Lederman dá duas razões para o "
            "apelido. A primeira: a editora não deixou usar \"Goddamn Particle\", algo como \"partícula maldita\", "
            "embora esse nome fosse talvez mais apropriado, dada a natureza \"vilã\" da partícula e o gasto que ela "
            "estava causando. A segunda: haveria uma ligação com um livro muito mais antigo. A expressão pegou na "
            "imprensa e pode ter ajudado a despertar interesse pelo assunto, mas muitos cientistas a consideram "
            "inadequada, uma hipérbole sensacionalista que engana o leitor. Um dos críticos é o próprio Peter Higgs. A "
            "partícula foi anunciada no CERN em 4 de julho de 2012, e Higgs e François Englert receberam o Nobel de "
            "Física de 2013 pelas previsões teóricas."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Higgs_boson",
            "In the media, the Higgs boson has often been called the \"God particle\" after the 1993 book The God Particle by Nobel Laureate Leon M. Lederman. "
            "The name has been criticised by physicists, including Peter Higgs. [...] "
            "by Physics Nobel Prize winner and Fermilab director Leon M. Lederman. "
            "Lederman wrote it in the context of failing US government support for the Superconducting Super Collider, a partially constructed titanic competitor to the Large Hadron Collider [...] "
            "that was championed by Lederman since its 1983 inception and shut down in 1993. "
            "The book sought in part to promote awareness of the significance and need for such a project in the face of its possible loss of funding. "
            "Lederman, a leading researcher in the field, writes that he wanted to title his book The Goddamn Particle: If the Universe is the Answer, What is the Question? "
            "Lederman's editor decided that the title was too controversial and convinced him to change the title [...] "
            "One, the publisher wouldn't let us call it the Goddamn Particle, though that might be a more appropriate title, given its villainous nature and the expense it is causing. "
            "And two, there is a connection, of sorts, to another book, a much older one [...] "
            "While media use of this term may have contributed to wider awareness and interest, many scientists feel the name is inappropriate since it is sensational hyperbole and misleads reader [...] "
            "On 4 July 2012, the discovery of a new particle [...] "
            "Physicists from two of the three teams, Peter Higgs and François Englert, were awarded the Nobel Prize in Physics in 2013 for their theoretical predictions.",
            nome="Higgs boson")],
    },
    # 9 Wu: a natureza distingue esquerda de direita
    {
        "temas_secundarios": ["personagens_esquecidos", "geometria_topologia"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Até 1956, os físicos achavam que as leis da natureza não distinguem esquerda de direita. Chien-Shiung Wu mostrou que distinguem, com átomos de cobalto quase no zero absoluto. Os teóricos levaram o Nobel; ela, não.",
        "explicacao": (
            "O princípio em jogo era a conservação da paridade: um processo e sua imagem no espelho deveriam seguir as "
            "mesmas leis, só com esquerda e direita trocadas. Isso já tinha sido verificado no eletromagnetismo e na "
            "força nuclear forte, e a comunidade supunha que valia para todas as forças. Nos anos 1950, porém, dois "
            "kaons aparentemente idênticos decaíam de formas que não se encaixavam nessa regra. Os teóricos Tsung-Dao "
            "Lee e Chen-Ning Yang propuseram que a força fraca, que comanda o decaimento beta, poderia violar a "
            "paridade, e procuraram Wu, especialista nesse decaimento. Ela cancelou uma viagem com o marido para "
            "começar logo, querendo sair na frente do resto da física. Pauli, amigo dela, achava o efeito impossível. "
            "O experimento alinhou núcleos de cobalto-60 com um campo magnético, resfriados quase ao zero absoluto, e "
            "comparou os decaimentos com os núcleos girando num sentido e no outro. O resultado mostrou que a força "
            "fraca viola a paridade, o que dá um jeito operacional de definir esquerda e direita. Lee e Yang ganharam "
            "o Nobel de Física de 1957. Wu foi mencionada no discurso deles, mas só foi premiada pela descoberta em "
            "1978, com o primeiro Prêmio Wolf."
        ),
        "nivel": 3, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Wu_experiment",
            "The Wu experiment was a particle and nuclear physics experiment conducted in 1956 by the Chinese-American physicist Chien-Shiung Wu [...] "
            "A parity transformation negates the coordinates in a theory, creating a mirror image. [...] "
            "The Wu experiment created an atomic system with spin, then compared weak-interaction particle decay for spins clockwise and counterclockwise. "
            "The experiment established that conservation of parity was violated by the weak interaction, thus providing a way to operationally define left and right. "
            "This result was not expected by the physics community, which had previously regarded parity as a symmetry that applied to all forces of nature. "
            "Tsung-Dao Lee and Chen-Ning Yang, the theoretical physicists who originated the idea of parity nonconservation and proposed the experiment, received the 1957 Nobel Prize in Physics for this result. "
            "While not awarded the Nobel Prize, Chien-Shiung Wu's role in the discovery was mentioned in the Nobel Prize acceptance speech of Yang and Lee, but she was not honored until 1978, when she was awarded the first Wolf Prize. [...] "
            "the intuitive idea that our world and its mirror image would behave in the same way, with the only difference being that left and right would be reversed [...] "
            "P-conservation was experimentally verified in the electromagnetic and strong interactions. "
            "However, during the late 1940s and mid-1950s, two different decays of seemingly identical kaon particles were observed. [...] "
            "In the summer of 1956 Lee and Yang approached Chien-Shiung Wu, who was an expert on beta decay spectroscopy [...] "
            "cancelling a planned trip to Geneva and the Far East with her husband, wanting to beat the rest of the physics community to the punch. "
            "Most physicists, such as close friend Wolfgang Pauli, thought it was impossible [...] "
            "The experiment monitored the decay of cobalt-60 (60Co) atoms that were aligned by a uniform magnetic field (the polarizing field) and cooled to near absolute zero",
            nome="Wu experiment")],
    },
    # 10 o bismuto do remédio é radioativo
    {
        "temas_secundarios": ["elementos_quimicos", "farmacos"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "O bismuto, presente em remédios para o estômago, foi tido como estável até 2003, quando se viu que é radioativo. Só que sua meia-vida é de uns 20,1 quintilhões de anos, muito mais que a idade do universo.",
        "explicacao": (
            "Todo o bismuto natural é de um único isótopo, o bismuto-209. Por muito tempo se achou que ele tinha o "
            "núcleo estável mais pesado de todos os elementos, embora houvesse a suspeita de que fosse radioativo, e "
            "a teoria previsse uma meia-vida enorme. Em 2003, uma equipe do Instituto de Astrofísica Espacial, em "
            "Orsay, na França, flagrou o decaimento: o bismuto-209 emite uma partícula alfa e vira tálio-205. A "
            "meia-vida, hoje estimada em 20,1 quintilhões de anos, foi confirmada em 2012 por uma equipe italiana no "
            "laboratório de Gran Sasso. Com um ritmo tão lento, o bismuto é muito menos radioativo do que a carne "
            "humana, não oferece risco real e, na prática, pode ser tratado como não radioativo. Por isso continua nos "
            "usos de sempre, como substituto do chumbo, em cosméticos, tintas e remédios como o Pepto-Bismol. O posto "
            "de núcleo estável mais pesado passou para o chumbo-208. E o recorde de meia-vida mais longa entre todos "
            "os nuclídeos conhecidos nem é do bismuto: pertence ao telúrio-128, que decai de outro jeito, por "
            "decaimento beta duplo."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Bismuth-209",
            "naturally occurring bismuth consists entirely of this isotope. [...] "
            "Bismuth-209 was long thought to have the heaviest stable nucleus of any element, but in 2003, a research team at the Institut d'astrophysique spatiale in Orsay, France, discovered that 209Bi undergoes alpha decay with a half-life now given more precisely as 2.01×1019 years (20.1 quintillion years), over 109 times longer than the estimated age of the universe. "
            "The heaviest nucleus considered to be stable is now lead-208 [...] "
            "Theory had previously predicted a half-life of 4.6×1019 years. It had been suspected to be radioactive for a long time. "
            "The decay produces a 3.14 MeV alpha particle plus thallium-205. "
            "Due to its extremely long half-life, 209Bi can be treated as non-radioactive for nearly all applications. "
            "It is much less radioactive than human flesh, so it poses no real radiation hazard. "
            "Though 209Bi holds the half-life record for alpha decay, it does not have the longest known half-life of any nuclide; this distinction belongs to tellurium-128 (128Te) with a  half-life estimated at 7.7×1024 years by double beta decay. "
            "The half-life of 209Bi was confirmed in 2012 by an Italian team in Gran Sasso [...] "
            "bismuth-209 is used for all normal applications of bismuth, such as being used as a replacement for lead, in cosmetics, in paints, and in several medicines such as Pepto-Bismol.",
            nome="Bismuth-209")],
    },
    # 11 os cadernos radioativos de Marie Curie
    {
        "temas_secundarios": ["personagens_esquecidos", "historia_medicina"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Os papéis de Marie Curie dos anos 1890 ainda são radioativos, e os cadernos devem continuar assim por mais de mil anos. Ficam em caixas forradas de chumbo, e quem quer consultá-los precisa usar roupa de proteção.",
        "explicacao": (
            "Marie Curie trabalhou numa época em que os danos da radiação ionizante não eram conhecidos e sem as "
            "medidas de segurança criadas depois. Ela carregava no bolso tubos de ensaio com isótopos radioativos, "
            "guardava-os na gaveta da escrivaninha e comentava a luz fraca que essas substâncias emitiam no escuro. Na "
            "Primeira Guerra Mundial, também se expôs a raios X de aparelhos sem blindagem, como radiologista em "
            "hospitais de campanha. Morreu em 4 de julho de 1934, aos 66 anos, de anemia aplástica, que se acredita "
            "ter sido causada pela longa exposição à radiação, com danos à medula óssea. A contaminação ficou nos "
            "objetos dela: seus papéis da década de 1890 são considerados perigosos demais para manusear, e até os "
            "livros de receitas são muito radioativos. Por isso ficam em caixas forradas de chumbo, e os "
            "interessados em consultá-los precisam vestir roupa de proteção. Como o rádio-226 tem meia-vida de cerca "
            "de 1.600 anos, a expectativa é que os cadernos continuem radioativos por bem mais de mil anos. Em 1995, "
            "ela se tornou a primeira mulher sepultada no Panteão de Paris por seus próprios méritos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Marie_Curie",
            "Because of their levels of radioactive contamination, her papers from the 1890s are considered too dangerous to handle. "
            "Even her cookbooks are highly radioactive. "
            "Her papers are kept in lead-lined boxes, and those who wish to consult them must wear protective clothing. [...] "
            "on 4 July 1934, she died aged 66 at the Sancellemoz sanatorium in Passy, Haute-Savoie, from aplastic anaemia believed to have been contracted from her long-term exposure to radiation, causing damage to her bone marrow. "
            "The damaging effects of ionising radiation were not known at the time of her work, which had been carried out without the safety measures later developed. "
            "She had carried test tubes containing radioactive isotopes in her pocket, and she stored them in her desk drawer, remarking on the faint light that the substances gave off in the dark. "
            "Curie was also exposed to X-rays from unshielded equipment while serving as a radiologist in field hospitals during the First World [...] "
            "Because radium-226 has a half-life of about 1,600 years, her notebooks are expected to remain radioactive for well over a thousand years. [...] "
            "in 1995, she became the first woman to be entombed on her own merits in the Paris Panthéon",
            nome="Marie Curie")],
    },
    # 12 combustíveis fósseis "envelhecem" o carbono-14
    {
        "temas_secundarios": ["mudancas_climaticas", "pre_historia"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Queimar petróleo e carvão está bagunçando o relógio do carbono-14. Com emissões altas, a datação pode deixar de distinguir algo recém-formado de amostras de até 2.000 anos ainda neste século.",
        "explicacao": (
            "A datação por radiocarbono, criada no fim dos anos 1940 por Willard Libby, usa o carbono-14, formado sem "
            "parar no alto da atmosfera quando raios cósmicos atingem o nitrogênio. Plantas o absorvem pela "
            "fotossíntese, e os animais, ao comê-las. Quando o ser vivo morre, para de trocar carbono com o ambiente, "
            "e o carbono-14 que tinha vai decaindo, com meia-vida de cerca de 5.730 anos; medir o que sobrou indica há "
            "quanto tempo ele morreu. Os combustíveis fósseis ficaram guardados por milhões de anos e não têm mais "
            "carbono-14. Ao serem queimados, despejam no ar carbono \"morto\", que dilui o radioativo, efeito "
            "descrito por Hans Suess em 1955. Um estudo publicado na revista PNAS simulou os cenários de emissão do IPCC: no "
            "ritmo de sempre, até o fim do século a queda de carbono-14 no ar equivaleria a mais de 2.000 anos de decaimento, e "
            "a datação deixaria de dar idades definitivas para amostras de até 2.000 anos. Uma análise posterior, com "
            "cenários ainda mais altos, previu resultados ambíguos para amostras de quase 1.500 anos já em 2050. Isso "
            "afeta a arqueologia, a detecção de falsificações e o combate ao comércio ilegal de marfim. Os testes "
            "nucleares fizeram o contrário: quase dobraram o carbono-14 da atmosfera, com o pico por volta de 1965."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Radiocarbon_dating",
                "The method was developed in the late 1940s at the University of Chicago by Willard Libby. "
                "It is based on the fact that radiocarbon (14C) is constantly being created in the Earth's atmosphere by the interaction of cosmic rays with atmospheric nitrogen. "
                "The resulting 14C combines with atmospheric oxygen to form radioactive carbon dioxide, which is incorporated into plants by photosynthesis; animals then acquire 14C by eating the plants. "
                "When the animal or plant dies, it stops exchanging carbon with its environment, and thereafter the amount of 14C it contains begins to decrease as the 14C undergoes radioactive decay. [...] "
                "The half-life of 14C (the period of time after which half of a given sample will have decayed) is about 5,730 years [...] "
                "fossil fuels contain almost no 14C. [...] "
                "This fossil fuel effect (also known as the Suess effect, after Hans Suess, who first reported it in 1955) [...] "
                "Conversely, nuclear testing increased the amount of 14C in the atmosphere, which reached a maximum in about 1965 of almost double the amount present in the atmosphere prior to nuclear testing.",
                nome="Radiocarbon dating"),
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:26195757%20AND%20SRC:MED&resultType=core&format=json",
             "titulo": "Impact of fossil fuel emissions on atmospheric radiocarbon and various applications of radiocarbon over this century (PNAS, 2015, via Europe PMC)",
             "idioma": "en",
             "trecho": (
                "Radiocarbon analyses are commonly used in a broad range of fields, including earth science, archaeology, forgery detection, isotope forensics, and physiology. [...] "
                "which decreases Δ(14)CO2 because fossil fuels have lost all (14)C from radioactive decay. "
                "Simulations of Δ(14)CO2 using the emission scenarios from the Intergovernmental Panel on Climate Change Fifth Assessment Report [...] "
                "emissions will reduce Δ(14)CO2 to -250‰, equivalent to the depletion expected from over 2,000 y of radioactive decay. [...] "
                "it implies that radiocarbon dating may no longer provide definitive ages for samples up to 2,000 y old."
             )},
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7757245/fullTextXML",
             "titulo": "Changes to Carbon Isotopes in Atmospheric CO2 Over the Industrial Era and Into the Future (Global Biogeochemical Cycles, 2020, via Europe PMC)",
             "idioma": "en",
             "trecho": (
                "Fossil fuels are completely devoid of [...] because they have been stored in geological reservoirs for millions of years [...] "
                "In this scenario, radiocarbon dating would not be able to distinguish newly produced materials from those up to 2,500 years old by the end of this century, "
                "and by 2050, radiocarbon dating would give ambiguous results for samples up to nearly 1,500 years old. [...] "
                "Similarly, applications for forgery detection or illegal ivory trading will be affected because newly produced materials will not be so easily distinguished from older ones."
             )},
        ],
    },
    # 13 múons revelam um vazio na Grande Pirâmide
    {
        "temas_secundarios": ["egito_antigo", "arquitetura"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade", "misterio_aberto"],
        "gancho": "Sem mover uma pedra, físicos acharam um vazio desconhecido de pelo menos 30 metros dentro da Grande Pirâmide de Gizé. Usaram múons, partículas criadas por raios cósmicos que atravessam a rocha.",
        "explicacao": (
            "Quando raios cósmicos atingem a atmosfera, produzem píons que logo decaem em múons. Os múons interagem "
            "pouco com a matéria e chegam a penetrar abaixo do solo, mas parte deles é absorvida no caminho. Contando "
            "quantos chegam a um detector, dá para estimar a espessura de material atravessado em cada direção: é a "
            "muografia. A ideia não é nova. O físico americano Luis Alvarez instalou detectores numa câmara da "
            "pirâmide de Quéfren, em Gizé, para procurar salas escondidas, e não achou nenhuma. O projeto "
            "ScanPyramids, liderado pela Universidade do Cairo e pelo instituto francês HIP, voltou ao tema a partir "
            "de 2015. Em 2 de novembro de 2017, a equipe anunciou na revista Nature um grande vazio acima da Grande "
            "Galeria da pirâmide de Quéops, com pelo menos 30 metros de comprimento. Três instituições de física de "
            "partículas, do Japão e da França, o observaram de forma independente, cada uma com uma técnica de "
            "muografia diferente. O formato exato e a função do vazio continuam desconhecidos, e o egiptólogo Zahi "
            "Hawass reagiu dizendo que o estudo não oferecia nada à egiptologia. Em 2023, a técnica revelou um "
            "corredor atrás da entrada original. A muografia também ajudou a confirmar o derretimento quase completo "
            "de reatores da usina de Fukushima."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("ScanPyramids",
                "The ScanPyramids mission is an international project designed and led by Cairo University and the French HIP Institute (Heritage Innovation Preservation). [...] "
                "The project, launched in October 2015 [...] "
                "On November 2, 2017, the ScanPyramids team published its third discovery in Nature, which was named \"ScanPyramids Big Void\", or \"SP-BV\" for short. "
                "It describes a newly discovered huge void in a circumscribed area above the Grand Gallery. "
                "It is estimated to have a length of at least 30 metres (98 ft) and a similar cross-section as the Grand Gallery. [...] "
                "Three scientific institutions specializing in particle physics have worked independently and each one used a different and complementary muography technique: "
                "Nagoya University, Japan [...] "
                "As long the exact layout and function of the void is still unknown [...] "
                "In March 2023, the team published its finding of the North Facing Corridor (NFC) behind the original entrance [...] "
                "the Egyptologist Zahi Hawass told the New York Times: \"They found nothing...This paper offers nothing to Egyptology. Zero.\"",
                nome="ScanPyramids"),
            wiki("Muon_tomography",
                "In all cases the information about the absorption of the muons was used as a measure of the thickness of the material crossed by the cosmic ray particles. [...] "
                "a team led by Luis Walter Alvarez, who installed detection apparatus in the Belzoni Chamber of the Pyramid of Khafre to search for hidden rooms within the structure. [...] "
                "although none were found at the time [...] "
                "Muography was applied to investigating the conditions of nuclear reactors damaged by the Fukushima nuclear disaster, and helped to confirm its state of near-complete meltdown.",
                nome="Muon tomography"),
            wiki("Cosmic_ray",
                "the charged pions produced by primary cosmic rays in the atmosphere swiftly decay, emitting muons. "
                "Unlike pions, these muons do not interact strongly with matter, and can travel through the atmosphere to penetrate even below ground level.",
                nome="Cosmic ray"),
        ],
    },
    # 14 Kamiokande: feito para ver o próton morrer
    {
        "temas_secundarios": ["estrelas", "cosmologia"],
        "tipos_espanto": ["historia_humana", "misterio_aberto"],
        "gancho": "No Japão, um tanque de água sob uma montanha foi construído para flagrar um próton se desintegrando. Isso nunca foi visto, mas o detector captou neutrinos de uma supernova, em 1987, e rendeu um Nobel.",
        "explicacao": (
            "Teorias que tentam unificar as forças da natureza permitem que o próton decaia, com meia-vida "
            "astronômica, muitas ordens de grandeza acima da idade do universo. Para flagrar um evento tão raro, é "
            "preciso vigiar uma quantidade enorme de prótons, e a água é um bom alvo. Assim nasceu o KamiokaNDE, "
            "sigla em inglês de Experimento de Decaimento de Núcleons de Kamioka, concluído em 1983 sob a direção de "
            "Masatoshi Koshiba: um tanque com 3.058 toneladas de água pura e cerca de 1.000 sensores de luz, os "
            "fotomultiplicadores. Depois de uma reforma para observar neutrinos do Sol, ele ficou sensível o bastante "
            "para registrar dez neutrinos da supernova SN 1987A, vista na Grande Nuvem de Magalhães em fevereiro de "
            "1987. Koshiba dividiu o Nobel de Física de 2002 pela detecção de neutrinos cósmicos. O sucessor, o "
            "Super-Kamiokande, fica a 1.000 metros de profundidade numa mina e guarda 50.220 toneladas de água "
            "ultrapura. Em 12 de novembro de 2001, numa fase de manutenção, cerca de 6.600 fotomultiplicadores "
            "implodiram em cadeia: a onda de choque de cada um trincava os vizinhos. Apesar de muito esforço "
            "experimental, o decaimento do próton nunca foi observado."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Super-Kamiokande",
                "observatory located under Mount Ikeno near the city of Hida, Gifu Prefecture, Japan. [...] "
                "The purpose of the observatory was to determine the existence of proton decay, one of the most fundamental questions of elementary particle physics. "
                "The detector, named KamiokaNDE for Kamioka Nucleon Decay Experiment, was a tank 16.0 m (52 ft) in height and 15.6 m (51.2 ft) in width, containing 3,058 tonnes (3,400 US tons) of pure water and about 1,000 photomultiplier tubes (PMTs) attached to its inner surface. "
                "The detector was upgraded, starting in 1985, to allow it to observe solar neutrinos. "
                "As a result, the detector (KamiokaNDE-II) had become sensitive enough to detect ten neutrinos from SN 1987A, a supernova which was observed in the Large Magellanic Cloud in February 1987 [...] "
                "Super-K is located 1,000 m (3,300 ft) underground in the Mozumi Mine in Hida's Kamioka area. [...] "
                "contains 50,220 tonnes of ultrapure water. [...] "
                "On 12 November 2001, about 6,600 of the photomultiplier tubes imploded in a chain reaction, as the shock wave from the concussion of each imploding tube cracked its neighbours. [...] "
                "Since an accident occurred during maintenance [...] "
                "2002: Masatoshi Koshiba was awarded the  Nobel Prize in Physics jointly with Raymond Davis Jr.  \"for pioneering contributions to astrophysics, in particular for the detection of cosmic neutrinos\"",
                nome="Super-Kamiokande"),
            wiki("Proton_decay",
                "Despite significant experimental effort, proton decay has never been observed. [...] "
                "Grand Unified Theories (GUTs) explicitly break the baryon number symmetry, allowing protons to decay [...] "
                "which is at least twenty orders of magnitude lower. [...] "
                "About 1034 protons are contained in approximately 30 kton of water [...] "
                "The construction of KamiokaNDE experiment under the direction of Masatoshi Koshiba  was completed in 1983.",
                nome="Proton decay"),
        ],
    },
    # 15 Becquerel e os dias nublados
    {
        "temas_secundarios": ["revolucao_cientifica", "cinema_fotografia"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "A radioatividade foi descoberta graças a dias nublados. Em 1896, Becquerel esperava o sol para um teste, guardou chapas fotográficas numa gaveta com sais de urânio e, ao revelá-las, achou imagens fortes.",
        "explicacao": (
            "No início de 1896, a física vivia a euforia dos raios X, descobertos por Wilhelm Röntgen no fim de 1895. "
            "Henri Becquerel estudava a fosforescência, o brilho que certos materiais emitem depois de iluminados, e "
            "suspeitou que eles, expostos ao sol forte, também soltassem uma radiação penetrante, parecida com os "
            "raios X. O teste era embrulhar chapas fotográficas em papel preto grosso, pôr moedas ou outros objetos e "
            "o material fosforescente por cima e deixar tudo ao sol por horas. As chapas reveladas mostravam a sombra "
            "dos objetos, e em 24 de fevereiro ele relatou os primeiros resultados. Nos dias 26 e 27, o céu ficou "
            "encoberto, e ele guardou os conjuntos numa gaveta escura, com as crostas de sal de urânio no lugar. Como "
            "o sol não apareceu nos dias seguintes, revelou as chapas em 1º de março esperando imagens fracas. As "
            "silhuetas estavam tão nítidas quanto as das chapas expostas ao sol. Em maio, depois de testar sais de "
            "urânio não fosforescentes, chegou à explicação certa: a radiação vinha do próprio urânio, sem precisar de "
            "nenhuma fonte externa de energia. O episódio virou um exemplo famoso de serendipidade."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Henri_Becquerel",
            "Becquerel's discovery of spontaneous radioactivity is a famous example of serendipity. "
            "Becquerel had long been interested in phosphorescence, the emission of light of one colour following the object's exposure to light of another colour. "
            "In early 1896, there was a wave of excitement following Wilhelm Röntgen's discovery of X-rays in late 1895. [...] "
            "thought that phosphorescent materials might emit penetrating X-ray-like radiation when illuminated by bright sunlight; he had various phosphorescent materials including some uranium salts for his experiments. "
            "Throughout the first weeks of February, Becquerel layered photographic plates with coins or other objects then wrapped this in thick black paper, placed phosphorescent materials on top, placed these in bright sun light for several hours. "
            "The developed plate showed shadows of the objects. Already on 24 February he reported his first results. "
            "However, the 26 and 27 February were dark and overcast during the day [...] "
            "I kept the apparatuses prepared and returned the cases to the darkness of a bureau drawer, leaving in place the crusts of the uranium salt. "
            "Since the sun did not come out in the following days, I developed the photographic plates on the 1st of March, expecting to find the images very weak. [...] "
            "the object shadows were just as distinct when left in the dark as when exposed to sunlight. [...] "
            "By May 1896, after other experiments involving non-phosphorescent uranium salts, Becquerel arrived at the correct explanation, namely that the penetrating radiation came from the uranium itself, without any need for excitation by an external energy source.",
            nome="Henri Becquerel")],
    },
    # 16 Goiânia: quem ligou os pontos
    {
        "temas_secundarios": ["brasil_republica", "historia_medicina"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "No acidente com césio-137 em Goiânia, em 1987, quem ligou os pontos foi a mulher do dono de um ferro-velho: ao notar muita gente adoecendo ao mesmo tempo, ela mesma levou o material a um hospital.",
        "explicacao": (
            "O Instituto Goiano de Radioterapia mudou de endereço em 1985 e deixou no prédio antigo um aparelho de "
            "radioterapia com césio-137. Em 13 de setembro de 1987, dia em que o vigia do local faltou, dois homens "
            "entraram no prédio, parcialmente demolido, e levaram parte do aparelho para vender como sucata. Naquela "
            "mesma noite, começaram a vomitar. Dias depois, um deles furou a janela da cápsula com uma chave de fenda, "
            "viu uma luz azul intensa e chegou a tentar acender o pó, pensando que fosse pólvora. O material foi "
            "vendido a um ferro-velho. O dono, Devair Ferreira, encantado com o brilho, levou a cápsula para casa e "
            "convidou amigos e parentes para ver o pó; grãos foram distribuídos. Leide das Neves Ferreira, de seis "
            "anos, filha de um irmão dele, passou o pó no corpo e comeu um ovo sentada no chão contaminado. Maria "
            "Gabriela Ferreira, mulher de Devair, foi a primeira a perceber que muita gente à sua volta adoecera "
            "gravemente de uma vez. Em 28 de setembro, recuperou o material e o levou a um hospital; no dia "
            "seguinte, um físico médico confirmou a radioatividade. Quatro pessoas morreram, entre elas Leide e Maria "
            "Gabriela. Cerca de 112 mil pessoas foram examinadas, e 249 estavam contaminadas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Goiânia_accident",
            "was a radioactive contamination accident that occurred on September 13, 1987, in Goiânia, Goiás, Brazil [...] "
            "resulting in four deaths – two of Ferreira's family members and two of his scrapyard employees. "
            "About 112,000 people were examined for radioactive contamination and 249 of them were found to have been contaminated. [...] "
            "In 1985, IGR moved to new premises, but left behind a caesium-137-based radiotherapy unit purchased in 1977. [...] "
            "On September 13, 1987, the guard tasked with protecting the site did not show up for work. "
            "Roberto dos Santos Alves and Wagner Mota Pereira illegally entered the partially demolished and crumbling IGR site. [...] "
            "They thought they might get some scrap value for the unit. They began dismantling the equipment. "
            "That same evening, they both began to vomit due to radiation sickness. [...] "
            "On September 16, Roberto punctured the cesium capsule's aperture window with a screwdriver, allowing him to see a deep blue light coming from the tiny opening he had created. [...] "
            "Thinking it was perhaps a type of gunpowder, he tried to light it, but the powder would not ignite. [...] "
            "On September 18, Roberto sold the items to a nearby scrapyard. "
            "That night, Devair Alves Ferreira, the owner of the scrapyard, noticed the blue glow from the punctured capsule. "
            "Thinking the capsule's contents were valuable or supernatural, he immediately brought it into his house. "
            "Over the next three days, he invited friends and family to view the strange glowing powder. [...] "
            "freed several rice-sized grains of the glowing material from the capsule using a screwdriver. "
            "Ferreira began to share some of them with various friends and family members. [...] "
            "Ivo, Devair's brother, successfully scraped some additional dust out of the source and took it to his house a short distance away. "
            "He spread some of it on the concrete floor. His six-year-old daughter, Leide das Neves Ferreira, later ate an egg while sitting on the floor. "
            "She was also fascinated by the powder's blue glow, applying it to her body and showing it off to her mother. [...] "
            "Maria Gabriela Ferreira had been the first to notice that many people around her had become severely ill at the same time. "
            "On September 28, 1987 – fifteen days after the item was found – she reclaimed the materials from the rival scrapyard and transported them to a hospital. "
            "In the morning of September 29, a visiting medical physicist used a scintillation counter to confirm the presence of radioactivity [...] "
            "fatally poisoning Leide das Neves Ferreira and Maria Gabriela Ferreira.",
            nome="Goiânia accident")],
    },
]
