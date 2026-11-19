LOTE = "2026-11-17-mecanica_quantica-01"
AREA = "fisica_quimica"
TEMA = "mecanica_quantica"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = W if idioma == "en" else "https://pt.wikipedia.org/wiki/"
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 tunelamento: o Sol e o pendrive
    {
        "temas_secundarios": ["estrelas", "historia_computacao"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "O mesmo efeito quântico, o tunelamento, faz o Sol brilhar e o pendrive apagar dados. E ele impõe um limite ao tamanho dos transistores.",
        "explicacao": (
            "No mundo quântico, uma partícula pode atravessar uma barreira que, pela física clássica, não teria "
            "energia para vencer. É o tunelamento. Ele está no coração do Sol: a temperatura no núcleo das estrelas "
            "em geral não basta para que os núcleos atômicos vençam a repulsão elétrica entre eles e se fundam. O "
            "tunelamento aumenta a chance de atravessar essa barreira. A probabilidade continua baixa, mas o "
            "número de núcleos no centro de uma estrela é tão grande que basta para manter a fusão. O mesmo "
            "efeito trabalha dentro dos aparelhos eletrônicos. A memória flash, a de pendrives e cartões de "
            "memória, está entre as aplicações do tunelamento: as memórias desse tipo usam o tunelamento de "
            "Fowler-Nordheim para apagar dados. E ele também atrapalha: elétrons atravessam com facilidade camadas "
            "isolantes com menos de cerca de 1 nanômetro, o que limita o tamanho mínimo dos componentes da "
            "microeletrônica."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Quantum_tunnelling",
                "Tunnelling plays an essential role in physical phenomena such as nuclear fusion and alpha radioactive decay of atomic nuclei. "
                "Tunnelling applications include the tunnel diode, quantum computing, flash memory, and the scanning tunnelling microscope. "
                "Tunnelling limits the minimum size of devices used in microelectronics because electrons tunnel readily through insulating layers and transistors that are thinner than about 1 nm. [...] "
                "The temperature in stellar cores is generally insufficient to allow atomic nuclei to overcome the Coulomb barrier and achieve thermonuclear fusion. "
                "Quantum tunnelling increases the probability of penetrating this barrier. "
                "Though this probability is still low, the extremely large number of nuclei in the core of a star is sufficient to sustain a steady fusion reaction.",
                nome="Quantum tunnelling"),
            wiki("Flash_memory",
                "Modern EEPROM based on Fowler-Nordheim tunnelling to erase data was invented by Bernward and patented by Siemens in 1974.",
                nome="Flash memory"),
        ],
    },
    # 2 efeito Zenão quântico
    {
        "temas_secundarios": ["paradoxos_logica", "grecia_antiga"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "No mundo quântico, observar um sistema sem parar pode impedi-lo de mudar. O efeito leva o nome de um paradoxo grego sobre uma flecha que nunca se move.",
        "explicacao": (
            "Zenão de Eleia, filósofo grego, propôs um paradoxo: uma flecha em voo, vista em qualquer instante, "
            "está imóvel, parada no espaço que ocupa. Como então ela se move? A mecânica quântica tem um efeito "
            "que lembra esse paradoxo. Pelas regras da teoria, cada medição faz o sistema \"colapsar\" num estado "
            "definido. Se as medições forem feitas em sequência rápida, um sistema instável parece congelado, sem "
            "conseguir mudar. Em 1967, dois físicos sugeriram que, pela matemática, uma partícula instável "
            "observada numa câmara de bolhas não decairia. Em 1977, Baidyanath Misra e George Sudarshan fizeram a "
            "análise matemática do efeito e o associaram à flecha de Zenão. A confirmação experimental só veio em "
            "1990, quando a equipe de Wayne Itano mediu repetidamente íons de berílio aprisionados enquanto "
            "induzia uma transição entre dois níveis de energia."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Quantum_Zeno_effect",
            "This aspect of quantum mechanics lay unexplored until 1967 when Beskow and Nilsson suggested that the mathematics indicated that an unstable particle in a bubble chamber would not decay. "
            "In 1977, Baidyanath Misra and E. C. George Sudarshan presented a mathematical analysis of this quantum effect and proposed its association with Zeno's arrow paradox. "
            "This paradox of Zeno of Elea imagines seeing an flying arrow at any fixed instant: it is immobile, frozen in the space it occupies. "
            "Despite continued theoretical work, experimental confirmation did not appear until 1990 when Itano et al. applied the idea proposed by Cook to study oscillating systems rather than unstable ones. "
            "Itano drove a transition between two levels in trapped 9Be+ ions while simultaneously measuring absorption of laser pulses [...] "
            "In the quantum Zeno effect an unstable state seems frozen – to not 'move' – due to a constant series of observations. [...] "
            "According to the reduction postulate, each measurement causes the wavefunction to collapse to an eigenstate of the measurement basis.",
            nome="Quantum Zeno effect")],
    },
    # 3 fenda dupla com moléculas
    {
        "temas_secundarios": ["luz_cores", "quimica_cotidiano"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Moléculas com até 2.000 átomos já passaram pelo experimento da fenda dupla e se comportaram como ondas, interferindo consigo mesmas.",
        "explicacao": (
            "No experimento da fenda dupla, partículas são lançadas contra uma placa com duas aberturas. Do outro "
            "lado, em vez de dois montes, surge um padrão de faixas, típico de ondas que interferem umas com as "
            "outras. Os impactos chegam um a um, como partículas, e de forma probabilística, algo que a física "
            "clássica não explica. Se alguém detecta por qual fenda cada partícula passou, as faixas somem. "
            "Até 1961, o experimento só tinha sido feito com luz. Naquele ano, Claus Jönsson, da Universidade de "
            "Tübingen, o repetiu com feixes de elétrons. Depois vieram átomos e moléculas cada vez maiores: o "
            "buckminsterfulereno, uma bola de 60 átomos de carbono, em 2002; moléculas de 430 átomos em 2011; e "
            "moléculas de até 2.000 átomos em 2019. A dualidade onda-partícula, que parecia coisa só do mundo "
            "minúsculo, alcança objetos já bem grandes para a escala atômica."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Double-slit_experiment",
            "This phenomenon has been shown to occur with photons, electrons, atoms, and even some molecules: with buckminsterfullerene (C60) in 2002, with 2 molecules of 430 atoms (C60(C12F25)10 and C168H94F152O8N4S4) in 2011, and with molecules of up to 2000 atoms in 2019. [...] "
            "However, such experiments demonstrate that particles do not form the double-slit interference pattern if one detects which slit they pass through [...] "
            "These results demonstrate the principle of wave–particle duality. [...] "
            "Additionally, the detection of individual discrete impacts is observed to be inherently probabilistic, which is inexplicable using classical mechanics. [...] "
            "A slit interference experiment was not performed with anything other than light until 1961, when Claus Jönsson of the University of Tübingen performed it with coherent electron beams and multiple slits.",
            nome="Double-slit experiment")],
    },
    # 4 Micius
    {
        "temas_secundarios": ["telecomunicacoes", "criptografia", "exploracao_espacial"],
        "tipos_espanto": ["escala_absurda", "engenhosidade"],
        "gancho": "Um satélite chinês testou o entrelaçamento quântico entre pontos a 1.200 km de distância e permitiu uma videochamada protegida por física quântica entre China e Áustria.",
        "explicacao": (
            "No entrelaçamento, duas partículas ficam ligadas de tal forma que medir uma revela algo sobre a "
            "outra, a qualquer distância. Isso permite a criptografia quântica: produzindo pares de fótons "
            "entrelaçados, é possível criar chaves secretas em que qualquer tentativa de interceptação é "
            "detectada. O problema é levar esses fótons longe, e o satélite chinês Micius, lançado em 15 de agosto "
            "de 2016, foi feito para isso. O nome homenageia um antigo filósofo chinês. Do espaço, ele testou a "
            "desigualdade de Bell, a prova do entrelaçamento, entre estações a 1.200 km de distância, mais longe "
            "que qualquer experimento até então, e teleportou o estado de um fóton entre uma estação no Tibete e "
            "o satélite. Em parceria com a Universidade de Viena, o projeto criou um canal de chaves quânticas "
            "entre a China e a Áustria, a 7.500 km, que permitiu a primeira videochamada intercontinental "
            "protegida por criptografia quântica."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Micius_(satellite)",
            "QUESS was launched on 15 August 2016. The project consists of the satellite Micius, or Mozi (Chinese: 墨子), after the ancient Chinese philosopher [...] "
            "In addition, QUESS tested Bell's inequality at a distance of 1,200 km (750 mi) – further than any experiment to date – and teleported a photon state between Shiquanhe Observatory in Ali, Tibet Autonomous Region, and the satellite. [...] "
            "QUESS created an international QKD channel between China and the Institute for Quantum Optics and Quantum Information, Vienna, Austria − a ground distance of 7,500 km (4,700 mi), enabling the first intercontinental secure quantum video call [...] "
            "Quantum encryption uses the principle of entanglement to facilitate communication that can absolutely detect whether a third party has intercepted a message in transit thus denying undetected decryption. "
            "By producing pairs of entangled photo",
            nome="Micius (satellite)")],
    },
    # 5 Planck
    {
        "temas_secundarios": ["historia_matematica", "revolucao_cientifica"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Um professor aconselhou o jovem Max Planck a não estudar física teórica, porque ela estaria quase completa. Planck acabou fundando a física quântica, num \"ato de desespero\".",
        "explicacao": (
            "Em 1878, o professor Philipp von Jolly, da Universidade de Munique, tentou dissuadir o aluno Max "
            "Planck de seguir a física teórica. Segundo Planck, Jolly argumentava que a física era uma ciência "
            "\"altamente desenvolvida, quase totalmente madura\", prestes a assumir sua forma final. Planck seguiu "
            "em frente. Em 14 de dezembro de 1900, para explicar a radiação emitida por corpos quentes, apresentou "
            "uma suposição estranha: a energia eletromagnética só poderia ser emitida em pacotes, múltiplos de "
            "uma unidade elementar. Ele mesmo desconfiava da ideia e, mais tarde, chamou o recurso de \"um ato de "
            "desespero\". No começo, considerou a quantização só \"uma suposição puramente formal\", em que não "
            "pensou muito. Hoje essa suposição, incompatível com a física clássica, é vista como o nascimento da "
            "física quântica. Ela rendeu a Planck o Nobel de Física de 1918 pela \"descoberta dos quanta de energia\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Max_Planck",
            "Jolly advised Planck against going into theoretical physics; Planck recalls that in 1878, Jolly argued that physics was almost complete, being a \"highly developed, nearly fully matured science, that through the crowning achievement of the discovery of the principle of conservation of energy will arguably soon take its final stable form\". [...] "
            "thus his recourse to them was, as he later put it, \"an act of despair ... I was ready to sacrifice any of my previous convictions about physics\". "
            "The central assumption behind his new derivation, presented to the DPG on 14 December 1900, was the supposition, now known as the Planck postulate, that electromagnetic energy could be emitted only in quantized form, in other words, the energy could only be a multiple of an elementary unit [...] "
            "At first Planck considered that quantisation was only \"a purely formal assumption ... actually I did not think much about it ...\"; nowadays this assumption, incompatible with classical physics, is regarded as the birth of quantum physics [...] "
            "He was awarded the 1918 Nobel Prize in Physics \"for the services he rendered to the advancement of physics by his discovery of energy quanta\".",
            nome="Max Planck")],
    },
    # 6 bússola quântica das aves
    {
        "temas_secundarios": ["comportamento_animal", "sentidos"],
        "tipos_espanto": ["conexao_inesperada", "misterio_aberto"],
        "gancho": "Aves migratórias parecem \"ver\" o campo magnético da Terra com uma proteína do olho que depende de um efeito quântico, e ondas de rádio podem atrapalhar essa bússola.",
        "explicacao": (
            "Muitos animais percebem o campo magnético da Terra e o usam para se orientar. Em 1972, Roswitha e "
            "Wolfgang Wiltschko mostraram que aves migratórias reagem à direção e à inclinação do campo. O "
            "mecanismo, porém, ficou um mistério por décadas. Experimentos indicam que essas aves usam uma "
            "proteína do olho, o criptocromo, que depende de um mecanismo quântico chamado de par radical para "
            "perceber o campo magnético. Esse efeito é extremamente sensível a campos fracos e, ao contrário de "
            "uma bússola de ferro comum, é facilmente perturbado por interferência de radiofrequência. Uma pista a "
            "favor: a versão dessa proteína (Cry4a) do pisco-de-peito-ruivo, ave migratória europeia, é muito mais "
            "sensível ao magnetismo que a de pombos e galinhas, que não migram. E nas aves migratórias os níveis "
            "dela são mais altos na primavera e no outono, as épocas de migração."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [wiki("Magnetoreception",
            "Experiments on migratory birds provide evidence that they make use of a cryptochrome protein in the eye, relying on the quantum radical pair mechanism to perceive magnetic fields. "
            "This effect is extremely sensitive to weak magnetic fields, and readily disturbed by radio-frequency interference, unlike a conventional iron compass. [...] "
            "In 1972, Roswitha and Wolfgang Wiltschko showed that migratory birds responded to the direction and inclination (dip) of the magnetic field. [...] "
            "Cry4a levels in migratory birds, which rely on navigation for their survival, are highest during the spring and autumn migration periods, when navigation is most critical. "
            "The Cry4a protein from the European robin, a migratory bird, is much more sensitive to magnetic fields than similar but not identical Cry4a from pigeons and chickens, which are non-migratory.")],
    },
    # 7 laser
    {
        "temas_secundarios": ["invencoes", "luz_cores"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Quando o laser foi inventado, em 1960, foi chamado de \"uma solução à procura de um problema\". A ideia por trás dele vinha de um trabalho de Einstein de 1917.",
        "explicacao": (
            "A palavra laser é uma sigla em inglês para \"amplificação da luz por emissão estimulada de "
            "radiação\". A base teórica vem de 1917, quando Albert Einstein publicou sua teoria quântica da "
            "radiação, que previa a emissão estimulada: um átomo excitado, atingido por um fóton, emite outro "
            "fóton idêntico. Em um laser, esses eventos se repetem em cadeia e geram uma enorme quantidade de "
            "fótons com o mesmo comprimento de onda, a mesma fase e a mesma polarização. O primeiro laser foi "
            "construído em 1960 por Theodore Maiman, nos Laboratórios Hughes, com base em trabalhos teóricos de "
            "Charles Townes e Arthur Schawlow e no amplificador óptico patenteado por Gordon Gould. Na época, o "
            "invento foi apelidado de \"uma solução à procura de um problema\", embora Gould já tivesse anotado "
            "várias aplicações possíveis. Hoje os lasers estão por toda parte, em milhares de usos."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Laser",
            "The word laser originated as an acronym for light amplification by stimulated emission of radiation. "
            "The first laser was built in 1960 by Theodore Maiman at Hughes Research Laboratories, based on theoretical work by Charles H. Townes and Arthur Leonard Schawlow and the optical amplifier patented by Gordon Gould. [...] "
            "stimulated emission events, generating a large number of photons at the same wavelength, phase and polarization. [...] "
            "A simple physical model for a laser begins with Albert Einstein's 1917 quantum theory of radiation. [...] "
            "When the laser was first invented, it was called \"a solution looking for a problem\", although Gould noted numerous possible applications in his notebook and patent applications. "
            "Since then, they have become ubiquitous, finding utility in thousands of h")],
    },
    # 8 Bose
    {
        "temas_secundarios": ["estados_materia", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Um físico indiano teve um artigo recusado, mandou-o a Einstein, e Einstein o traduziu ele mesmo para o alemão. Daí vêm a palavra \"bóson\" e um novo estado da matéria.",
        "explicacao": (
            "Satyendra Nath Bose dava aula na recém-fundada Universidade de Dacca, no atual Bangladesh, quando "
            "escreveu um artigo sobre a estatística de partículas idênticas. A revista britânica Philosophical "
            "Magazine o recusou, e não se sabe por quê. Bose então mandou o texto diretamente a Albert Einstein, "
            "na Alemanha. Einstein reconheceu a importância do trabalho, traduziu-o ele mesmo para o alemão e o "
            "submeteu em nome de Bose à revista Zeitschrift für Physik. Depois, estendeu a ideia aos átomos, o que "
            "levou, em 1924 e 1925, à previsão de um novo estado da matéria: o condensado de Bose-Einstein, em que "
            "um gás muito frio se comporta como uma coisa só. Ele só foi produzido em 1995, por Eric Cornell e "
            "Carl Wieman, com átomos de rubídio resfriados a 170 bilionésimos de grau acima do zero absoluto. As "
            "partículas descritas pela estatística de Bose ganharam de Paul Dirac o nome de bósons."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Satyendra_Nath_Bose",
                "In 1921, Satyendra Nath Bose joined as Reader in the Department of Physics of the recently founded University of Dhaka (in present-day Bangladesh). [...] "
                "Though not accepted at once for publication, he sent the article directly to Albert Einstein in Germany. "
                "Einstein, recognising the importance of the paper, translated it into German himself and submitted it on Bose's behalf to the Zeitschrift für Physik. [...] "
                "Bose had already submitted his article to the British Journal Philosophical Magazine, which rejected it before he sent it to Einstein. It is not known why it was rejected. "
                "Einstein adopted the idea and extended it to atoms. [...] "
                "The eponymous particles class described by Bose's statistics, bosons, were named by Paul Dirac.",
                nome="Satyendra Nath Bose"),
            wiki("Bose–Einstein_condensate",
                "Bose–Einstein condensates were first predicted, generally, in 1924–1925 by Albert Einstein, crediting a pioneering paper by Satyendra Nath Bose on the new field now known as quantum statistics. [...] "
                "Eric Cornell and Carl Wieman at the University of Colorado at Boulder NIST–JILA lab, in a gas of rubidium atoms cooled to 170 nanokelvins (nK).",
                nome="Bose–Einstein condensate"),
        ],
    },
    # 9 Solvay 1927
    {
        "temas_secundarios": ["personagens_esquecidos", "cinema_fotografia"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Na conferência de física de Solvay de 1927, que discutiu a nova mecânica quântica, 17 dos 29 participantes tinham ganhado ou ainda ganhariam o Nobel.",
        "explicacao": (
            "As conferências Solvay reúnem, desde o início do século XX, os físicos mais importantes de cada época. "
            "A mais famosa foi a quinta, de 24 a 29 de outubro de 1927, em Bruxelas, com o tema \"Elétrons e "
            "fótons\". Ali os maiores nomes da física se reuniram para discutir a teoria quântica recém-formulada, "
            "e os protagonistas foram Albert Einstein e Niels Bohr, que defendiam visões opostas sobre o "
            "significado da nova teoria. Dos 29 participantes, 17 já tinham ganhado ou ainda ganhariam um prêmio "
            "Nobel. Entre eles estava Marie Curie, a única do grupo premiada em duas ciências diferentes, física e "
            "química. A foto oficial do encontro virou um retrato célebre da geração que construiu a física "
            "quântica."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Solvay_Conference",
            "Perhaps the most famous conference was the fifth Solvay Conference on Physics, which was held from 24 to 29 October 1927. "
            "The subject was Electrons and Photons and the world's most notable physicists met to discuss the newly formulated quantum theory. "
            "The leading figures were Albert Einstein and Niels Bohr. "
            "Seventeen of the 29 attendees were or became Nobel Prize winners, including Marie Skłodowska-Curie who, alone among them, had won Nobel Prizes in two separate scientific disciplines.",
            nome="Solvay Conference")],
    },
    # 10 efeito Casimir
    {
        "temas_secundarios": ["eletromagnetismo", "invencoes"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Duas placas de metal sem carga, no vácuo, se atraem sozinhas quando estão muito perto: a 10 nanômetros, a força equivale a cerca de uma atmosfera de pressão.",
        "explicacao": (
            "Pela física clássica, duas placas condutoras sem carga, no vácuo, não deveriam sentir força nenhuma "
            "uma da outra: não há campo entre elas. A física quântica diz outra coisa. O vácuo não é um nada: ele "
            "tem flutuações do campo eletromagnético, os chamados fótons virtuais, e as placas alteram esse campo. "
            "O resultado é uma força, de atração ou de repulsão conforme o arranjo das placas. É o efeito Casimir, "
            "previsto em 1948 pelo físico holandês Hendrik Casimir. A força cai depressa com a distância, mas a "
            "curtíssimo alcance fica enorme: a 10 nanômetros, cerca de cem vezes o tamanho de um átomo, ela "
            "equivale a uma atmosfera de pressão. Em 1997, um experimento de Steven Lamoreaux mediu a força com "
            "diferença de menos de 5% em relação à teoria. Hoje ela preocupa engenheiros: pode fazer peças "
            "microscópicas de máquinas eletromecânicas grudarem."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Casimir_effect",
            "It is named after the Dutch physicist Hendrik Casimir, who predicted the effect for electromagnetic systems in 1948. [...] "
            "The typical example is of two uncharged conductive plates in a vacuum, placed a few nanometers apart. "
            "In a classical description, the lack of an external field means that no field exists between the plates, and no force connects them. "
            "When this field is instead studied using the quantum electrodynamic vacuum, it is seen that the plates do affect the virtual photons that constitute the field, and generate a net force – either an attraction or a repulsion depending on the plates' specific arrangement. [...] "
            "Because the strength of the force falls off rapidly with distance, it is measurable only when the distance between the objects is small. [...] "
            "In fact, at separations of 10 nm – about 100 times the typical size of an atom – the Casimir effect produces the equivalent of about 1 atmosphere of pressure [...] "
            "In 1997, a direct experiment by Steven K. Lamoreaux quantitatively measured the Casimir force to be within 5% of the value predicted by the theory. [...] "
            "In particular, Casimir effect might be the critical factor in the stiction failure of MEMS.",
            nome="Casimir effect")],
    },
]
