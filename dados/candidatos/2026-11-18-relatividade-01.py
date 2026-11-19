LOTE = "2026-11-18-relatividade-01"
AREA = "fisica_quimica"
TEMA = "relatividade"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o GPS e a relatividade
    {
        "temas_secundarios": ["telecomunicacoes", "medidas_padroes", "exploracao_espacial"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "Os relógios dos satélites de GPS ganham 38 milionésimos de segundo por dia em relação aos da Terra, como prevê a relatividade. Por isso eles saem da fábrica regulados para andar um pouco mais devagar.",
        "explicacao": (
            "Dois efeitos da relatividade agem ao mesmo tempo e em sentidos opostos. Pela relatividade especial, "
            "um relógio em movimento anda mais devagar: como os satélites correm a uns 4 km/s, seus relógios "
            "atrasam cerca de 7,2 microssegundos por dia. Pela relatividade geral, quanto mais fraca a gravidade, "
            "mais rápido o tempo passa, e na altitude dos satélites isso adianta os relógios em cerca de 45,8 "
            "microssegundos por dia. O saldo é de uns 38 microssegundos a mais por dia. Parece pouco, mas o GPS "
            "calcula a posição a partir do tempo que o sinal leva para chegar, e a luz percorre cerca de 300 "
            "metros a cada microssegundo. A correção vem embutida no projeto: antes do lançamento, cada relógio "
            "atômico recebe um ajuste para funcionar a 10,22999999543 MHz em vez de 10,23 MHz. No começo, havia "
            "quem achasse que o GPS não seria afetado pela relatividade geral. Hoje, ele é tido como uma aplicação "
            "prática de engenharia da teoria de Einstein. A ideia de testar a relatividade com relógios atômicos em "
            "satélites foi proposta em 1955 por Friedwardt Winterberg."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Global_Positioning_System",
                "In 1955, Friedwardt Winterberg proposed a test of general relativity—detecting time slowing in a strong gravitational field using accurate atomic clocks placed in orbit inside artificial satellites. "
                "Special and general relativity predicted that the clocks on GPS satellites, as observed by those on Earth, run 38 microseconds faster per day than those on the Earth. "
                "The design of GPS corrects for this difference.",
                nome="Global Positioning System"),
            wiki("Error_analysis_for_the_Global_Positioning_System",
                "where the orbital velocity is v = 4 km/s and c is the speed of light, approximately 3×108m/s. "
                "The result is an error of about -7.2 μs/day in the satellite. [...] "
                "causing the clocks at the altitude of the satellite to be faster by a factor of 5×10−10, or about +45.8 μs/day. [...] "
                "During early development some believed that GPS would not be affected by general relativistic effects [...] "
                "board each satellite is given a rate offset prior to launch, making it run slightly slower than the desired frequency on Earth; specifically, at 10.22999999543 MHz instead of 10.23 MHz. "
                "Since the atomic clocks on board the GPS satellites are precisely tuned, it makes the system a practical engineering application of the scientific theory of relativ",
                nome="Error analysis for the Global Positioning System"),
        ],
    },
    # 2 ouro amarelo e mercúrio líquido
    {
        "temas_secundarios": ["elementos_quimicos", "luz_cores", "minerais_rochas"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "O ouro é amarelo e o mercúrio é líquido por causa da relatividade de Einstein. Nesses átomos pesados, os elétrons mais internos giram a uma fração enorme da velocidade da luz, e isso muda a química.",
        "explicacao": (
            "Num átomo de ouro, com 79 prótons, o elétron mais interno se move a cerca de 58% da velocidade da luz. "
            "Nessa velocidade entram os efeitos relativísticos: os elétrons ficam mais tempo perto do núcleo e certas "
            "órbitas se contraem. No ouro, isso aproxima os níveis de energia de um jeito que o metal passa a "
            "absorver a luz azul mais do que as outras cores. A luz refletida chega aos olhos com falta de azul, e "
            "o que se vê é amarelo. Sem esse efeito, o ouro seria prateado como a maioria dos metais. No mercúrio, "
            "a mesma contração deixa os elétrons de fora tão presos que eles quase não participam das ligações "
            "entre os átomos. As ligações entre átomos de mercúrio vêm sobretudo de forças fracas, de van der "
            "Waals, e o metal fica líquido até cerca de 39 graus negativos, enquanto o vizinho cádmio só derrete a "
            "321 °C. O vapor de mercúrio é formado quase só por átomos soltos, a ponto de às vezes ser chamado de "
            "\"pseudogás nobre\"."
        ),
        "nivel": 3, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Relativistic_quantum_chemistry",
            "A prominent example is an explanation for the color of gold: due to relativistic effects, it is not silvery like most other metals. [...] "
            "For gold with Z = 79, v ≈ 0.58c, so the 1s electron will be moving at 58% of the speed of light. [...] "
            "a result the electrons will be near the nucleus more of the time and thereby contract the radius for small principal quantum numbers. [...] "
            "Mercury (Hg) is a liquid down to approximately −39 °C, its melting point. "
            "Bonding forces are weaker for Hg–Hg bonds than for their immediate neighbors such as cadmium (m.p. 321 °C) [...] "
            "bital is contracted by relativistic effects and may therefore only weakly contribute to any chemical bonding, Hg–Hg bonding must be mostly the result of van der Waals forces. "
            "Mercury gas is mostly monatomic, Hg(g). [...] "
            "The relativistic contraction of the 6s2 orbital leads to gaseous mercury sometimes being referred to as a pseudo noble gas. [...] "
            "Gold absorbs blue light more than it absorbs other visible wavelengths of light; the reflected light reaching the eye is therefore lacking in blue compared with the incident light.",
            nome="Relativistic quantum chemistry")],
    },
    # 3 a bateria do carro
    {
        "temas_secundarios": ["elementos_quimicos", "energia", "transportes"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Dos 12 volts da bateria do seu carro, cerca de 10 vêm de efeitos da relatividade sobre os elétrons do chumbo. Sem eles, uma bateria de estanho, que é parecido com o chumbo, funcionaria igual. Não funciona.",
        "explicacao": (
            "A bateria de chumbo-ácido, inventada em 1859 pelo físico francês Gaston Planté, foi a primeira bateria "
            "recarregável. Ela é pesada e guarda pouca energia para o tamanho, mas fornece correntes altas de uma "
            "vez, por isso é usada para dar a partida nos carros. Cada célula dá cerca de 2,1 volts, e seis delas "
            "somam os 12 volts. Na tabela periódica, o chumbo fica na mesma coluna do estanho, e pela química "
            "clássica os dois deveriam se comportar de modo muito parecido. Então uma bateria de estanho e ácido "
            "deveria funcionar tão bem quanto a de chumbo. Mas o chumbo é bem mais pesado, com 82 prótons contra 50 "
            "do estanho, e nos átomos pesados os elétrons internos se movem perto da velocidade da luz, o que muda "
            "suas órbitas. Cálculos mostram que cerca de 10 dos 12 volts de uma bateria de seis células vêm "
            "puramente desses efeitos relativísticos. É isso que explica por que baterias de estanho e ácido não "
            "funcionam."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Relativistic_quantum_chemistry",
                "Without relativity, lead (Z = 82) would be expected to behave much like tin (Z = 50), so tin–acid batteries should work just as well as the lead–acid batteries commonly used in cars. "
                "However, calculations show that about 10 V of the 12 V produced by a 6-cell lead–acid battery arises purely from relativistic effects, explaining why tin–acid batteries do not work.",
                nome="Relativistic quantum chemistry"),
            wiki("Lead%E2%80%93acid_battery",
                "First invented in 1859 by French physicist Gaston Planté, it was the first type of rechargeable battery ever created. "
                "Compared to the more modern rechargeable batteries, lead–acid batteries have relatively low energy density and heavier weight. "
                "Despite this, they are able to supply high surge currents. "
                "These features, along with their low cost, make them useful for motor vehicles in order to provide the high current required by starter motors. [...] "
                "A lead–acid battery's nominal voltage is 2.1 V for each cell.",
                nome="Lead–acid battery"),
        ],
    },
    # 4 os múons que não deveriam chegar ao chão
    {
        "temas_secundarios": ["fisica_particulas", "atmosfera"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "A cada minuto, uns 10 mil múons, partículas criadas no alto da atmosfera, atravessam cada metro quadrado do chão. Pela física clássica, quase nenhum chegaria: eles vivem tão pouco que se desfariam no caminho.",
        "explicacao": (
            "Os múons nascem quando raios cósmicos se chocam com moléculas da alta atmosfera. São partículas "
            "instáveis, com vida média de 2,2 microssegundos. Mesmo viajando quase à velocidade da luz, nesse "
            "tempo eles percorreriam pouco: sem efeitos relativísticos, metade deles se desfaria em no máximo uns "
            "456 metros. Mas eles chegam à superfície e até a minas profundas. A explicação é a dilatação do tempo "
            "prevista pela relatividade especial: do ponto de vista da Terra, o relógio interno de um múon veloz "
            "anda mais devagar, e ele dura muito mais. Do ponto de vista do múon, quem encolhe é a distância até o "
            "chão, que fica bem mais curta. As duas descrições dão o mesmo resultado. Foi com múons, no experimento "
            "de Rossi e Hall, em 1941, que a dilatação do tempo foi observada pela primeira vez. Hoje esse fluxo "
            "constante de múons atravessa o seu corpo enquanto você lê."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Muon",
            "The muon is an unstable subatomic particle with a mean lifetime of 2.2 μs. [...] "
            "so-called secondary muons, created by cosmic rays hitting the atmosphere, can penetrate the atmosphere and reach Earth's land surface and even into deep mines. [...] "
            "In the Rossi–Hall experiment (1941), muons were used to observe the time dilation (or, alternatively, length contraction) predicted by special relativity, for the first time. [...] "
            "About 10,000 muons reach every square meter of the earth's surface a minute; these charged particles form as by-products of cosmic rays colliding with molecules in the upper atmosphere. [...] "
            "Although their lifetime without relativistic effects would allow a half-survival distance of only about 456 m (2.197 μs × ln(2) × 0.9997 c) at most (as seen from Earth), the time dilation effect of special relativity (from the viewpoint of the Earth) allows cosmic ray secondary muons to survive the flight to the Earth's surface, since in the Earth frame the muons have a longer half-life due to their velocity. "
            "From the viewpoint (inertial frame) of",
            nome="Muon")],
    },
    # 5 o "Sr. Relógio" na poltrona do avião
    {
        "temas_secundarios": ["transportes", "medidas_padroes"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 1971, dois cientistas testaram a relatividade dando a volta ao mundo em voos comerciais com relógios atômicos. Gastaram US$ 7.600 em passagens, incluindo poltronas para o passageiro \"Sr. Relógio\".",
        "explicacao": (
            "O físico Joseph Hafele fez uma conta rápida para uma aula e viu que um relógio atômico num avião "
            "comercial teria precisão suficiente para detectar os efeitos previstos pela relatividade. Passou um ano "
            "tentando, sem sucesso, conseguir dinheiro para o experimento, até que o astrônomo Richard Keating, que "
            "trabalhava com relógios atômicos no Observatório Naval dos EUA, o procurou depois de uma palestra. Os "
            "dois conseguiram US$ 8.000 do Escritório de Pesquisa Naval, num dos testes mais baratos já feitos da "
            "relatividade geral. Levaram quatro relógios atômicos de césio, deram a volta ao mundo primeiro para o "
            "leste e depois para o oeste, e as tripulações forneceram os dados de navegação. Indo para o leste, no "
            "sentido da rotação da Terra, o avião somava velocidade e o relógio perdia tempo; indo para o oeste, "
            "acontecia o contrário. Na volta, os relógios dos aviões e os que ficaram no chão discordavam entre si, "
            "e as diferenças batiam com as previsões das relatividades especial e geral. O experimento foi repetido "
            "com mais precisão em 2010."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Hafele%E2%80%93Keating_experiment",
            "In 1971, Joseph C. Hafele, a physicist, and Richard E. Keating, an astronomer, took four cesium-beam atomic clocks aboard commercial airliners. "
            "They flew twice around the world, first eastward, then westward, and compared the clocks in motion to stationary clocks at the United States Naval Observatory. "
            "When reunited, the three sets of clocks were found to disagree with one another, and their differences were consistent with the predictions of special and general relativity. [...] "
            "a clock aboard the plane moving eastward, in the direction of the Earth's rotation, had a greater velocity (resulting in a relative time loss) than one that remained on the ground, while a clock aboard the p [...] "
            "for a physics lecture when he did a back-of-the-envelope calculation showing that an atomic clock aboard a commercial airliner should have sufficient precision to detect the predicted relativistic effects. "
            "He spent a year in fruitless attempts to get funding for such an experiment, until he was approached after a talk on the topic by Keating, an astronomer at the United States Naval Observatory who worked with atomic clocks. "
            "Hafele and Keating obtained $8000 in funding from the Office of Naval Research for one of the most inexpensive tests ever conducted of general relativity. "
            "Of this amount, $7600 was spent on the eight round-the-world plane tickets, including two seats on each flight for \"Mr. Clock.\" [...] "
            "The crew of each flight helped by supplying the navigational data needed for the comparison with theory. [...] "
            "In June 2010, the National Physical Laboratory again repeated the experiment",
            nome="Hafele–Keating experiment")],
    },
    # 6 Sobral, 1919
    {
        "temas_secundarios": ["brasil_republica", "ciencia_brasileira", "historia_astronomia"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "A primeira confirmação da relatividade geral veio, em boa parte, de Sobral, no Ceará: no eclipse de 1919, as melhores fotos foram as de um telescópio reserva, de 4 polegadas. Einstein agradeceu ao \"céu do Brasil\".",
        "explicacao": (
            "A teoria previa que a luz de uma estrela, ao passar raspando no Sol, seria desviada em cerca de 1,75 "
            "segundo de arco, o dobro do que dava a gravitação de Newton. Para medir isso era preciso fotografar "
            "estrelas perto do Sol durante um eclipse total. Em 1918, pesquisadores do Observatório Nacional "
            "brasileiro concluíram que Sobral era o melhor lugar para ver o eclipse de 29 de maio de 1919, e o "
            "diretor, Henrique Morize, mandou um relatório às instituições científicas do mundo. Foram duas "
            "expedições britânicas: Arthur Eddington foi à ilha de Príncipe, na África, e Andrew Crommelin e "
            "Charles Davidson foram a Sobral. Lá, o dia amanheceu nublado, mas o céu abriu e o eclipse durou 5 "
            "minutos e 13 segundos. O telescópio principal fez imagens borradas, que acabaram descartadas. Já o "
            "pequeno telescópio reserva, de 4 polegadas, fez as imagens mais nítidas, com um desvio um pouco "
            "acima do previsto por Einstein. Para o historiador Daniel Kennefick, sem as fotos de Sobral o "
            "resultado teria sido inconclusivo. Em 1925, Einstein disse à imprensa brasileira: \"O problema "
            "concebido pelo meu cérebro foi resolvido pelo luminoso céu do Brasil\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Eddington_experiment",
            "Observations of the total solar eclipse of 29 May 1919 were carried out by two expeditions, one to the West African island of Príncipe, and the other to the Brazilian town of Sobral. [...] "
            "The Príncipe expedition members were Eddington and Edwin Turner Cottingham, from the Cambridge Observatory, while the Sobral expedition members were Andrew Crommelin and Charles Rundle Davidson, from the Greenwich Observatory in London. [...] "
            "In mid-1918, researchers from the Brazilian National Observatory, determined that the city of Sobral, Ceará, was the best geographical position to observe the Solar Eclipse. "
            "Its director, Henrique Charles Morize, sent a report to worldwide scientific institutions on the subject [...] "
            "a small backup telescope with a 4-inch aperture borrowed from Aloysius Cortie. [...] "
            "The eclipse day started cloudy, but the sky cleared and the Moon's disk began to obscure the Sun shortly before 8:56 am; the eclipse lasted 5 minutes 13 seconds. [...] "
            "The main telescope had blurred images, which were discarded from the final conclusion though its estimated deflections were closer to the Newtonian-based prediction, while the smaller one had the clearest images and was deemed the most trustworthy and had an estimated deflection slightly above the Einsteinian prediction. "
            "Daniel Kennefick defends that without the Sobral photographs, the results of the 1919 eclipse would have been inconclusive [...] "
            "In 1925, Einstein stated to the Brazilian press about the results, \"The problem conceived by my brain was solved by the bright Brazilian sky\". [...] "
            "For light grazing the surface of the Sun, the approximate angular deflection is roughly 1.75 arcseconds. "
            "This is twice the value predicted by calculations using the Newtonian theory of gravity.",
            nome="Eddington experiment")],
    },
    # 7 Vulcano, o planeta que não existia
    {
        "temas_secundarios": ["sistema_solar", "historia_astronomia"],
        "tipos_espanto": ["historia_humana", "mito_desmentido"],
        "gancho": "Mercúrio não se comportava como Newton previa, e astrônomos chegaram a batizar um planeta escondido perto do Sol para explicar: Vulcano. Ele não existia. Quem resolveu o problema, em 1915, foi Einstein.",
        "explicacao": (
            "A órbita de Mercúrio é uma elipse que gira devagar em torno do Sol, e a maior parte desse giro se "
            "explica pela atração dos outros planetas. Em 1859, porém, o francês Urbain Le Verrier analisou as "
            "passagens de Mercúrio diante do Sol entre 1697 e 1848 e viu que o giro real não batia com o previsto "
            "pela teoria de Newton: sobravam 38 segundos de arco por século, número depois recalculado em 43 por "
            "Simon Newcomb, em 1882. Le Verrier sugeriu que outro planeta, ainda não visto, puxasse Mercúrio. A "
            "ideia ganhou crédito porque o mesmo raciocínio já tinha funcionado: Netuno fora encontrado a partir "
            "das perturbações na órbita de Urano. O planeta hipotético ganhou até nome. Em 1908, depois de buscas "
            "fotográficas em três eclipses, o diretor do Observatório Lick deu o problema observacional por "
            "encerrado. Em 1915, a relatividade geral explicou o desvio sem planeta nenhum: é efeito da curvatura "
            "do espaço-tempo. Einstein escreveu ao amigo Michele Besso: \"Movimentos do periélio explicados "
            "quantitativamente... você vai ficar espantado\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Tests_of_general_relativity",
            "This anomalous rate of precession of the perihelion of Mercury's orbit was first recognized in 1859 as a problem in celestial mechanics, by Urbain Le Verrier. "
            "His re-analysis of available timed observations of transits of Mercury over the Sun's disk from 1697 to 1848 showed that the actual rate of the precession disagreed from that predicted from Newton's theory by 38″ (arcseconds) per tropical century (later re-estimated at 43″ by Simon Newcomb in 1882). [...] "
            "Le Verrier suggested that another hypothetical planet might exist to account for Mercury's behavior. "
            "The previously successful search for Neptune based on its perturbations of the orbit of Uranus led astronomers to place some faith in this possible explanation, and the hypothetical planet was even named Vulcan. "
            "Finally, in 1908, W. W. Campbell, Director of the Lick Observatory, after the comprehensive photographic observations by Lick astronomer, Charles D. Perrine, at three solar eclipse expeditions, stated [...] "
            "Subsequently, no evidence of Vulcan was found and Einstein's 1915 general theory accounted for Mercury's anomalous precession. "
            "Einstein wrote to Michele Besso, \"Perihelion motions explained quantitatively ... you will be astonished\". "
            "In general relativity, this remaining precession, or change of orientation of the orbital ellipse within its orbital plane, is explained by gravitation being mediated by the curvature of spacetime",
            nome="Tests of general relativity")],
    },
    # 8 a luz que perde energia subindo 22,5 metros
    {
        "temas_secundarios": ["fisica_particulas", "luz_cores"],
        "tipos_espanto": ["engenhosidade", "escala_absurda"],
        "gancho": "Em 1959, físicos de Harvard mediram a gravidade mudando a cor da luz numa torre de 22,5 metros. Subindo, os raios gama perdiam um tiquinho de energia: 2,56 partes em mil trilhões, como previa Einstein.",
        "explicacao": (
            "A relatividade geral prevê que a luz perde energia ao subir contra a gravidade e ganha ao descer: é o "
            "desvio gravitacional para o vermelho, ligado à dilatação do tempo pela gravidade. Perto da Terra, o "
            "efeito é minúsculo. Robert Pound e seu aluno de pós-graduação Glen Rebka o mediram numa torre do "
            "laboratório Jefferson, em Harvard, isolada das vibrações do resto do prédio. Uma fonte de raios gama "
            "ficava numa ponta e um absorvedor de ferro na outra, a 22,5 metros, com os raios passando por um saco "
            "plástico cheio de hélio para não se espalharem. A medida só foi possível graças ao efeito Mössbauer, "
            "que produz raios gama com energia extremamente bem definida. Eles encontraram uma mudança de "
            "frequência de 2,56 partes em 10 elevado a 15, com margem de erro de 10% em relação ao previsto. Foi "
            "o último dos testes clássicos da relatividade geral a ser confirmado, e o laboratório de Pound "
            "refinou a medida até chegar a 1% de precisão em 1964."
        ),
        "nivel": 3, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Pound%E2%80%93Rebka_experiment",
            "It was proposed by Robert Pound and his graduate student Glen A. Rebka Jr. in 1959, and was the last of the classical tests of general relativity to be verified. [...] "
            "a gravitational potential, and would lose energy when rising through a gravitational potential. [...] "
            "The experiment was carried out in a tower at Harvard University's Jefferson laboratory that was, for the most part, vibrationally isolated from the rest of the building. [...] "
            "The distance between the source and absorber was 22.5 meters (74 ft). "
            "The gamma rays traveled through a Mylar bag filled with helium to minimize scattering of the gamma rays. [...] "
            "they calculated a net fractional frequency shift due to gravitational time dilation of −(2.56±0.25)×10−15, which corresponds to the predicted value with an error margin of 10%. "
            "In the next several years, the Pound lab published successive refinements of the gravitational redshift measurement, finally reaching the 1% level in 1964. [...] "
            "Mössbauer effect",
            nome="Pound–Rebka experiment")],
    },
    # 9 o Nobel de Einstein não foi pela relatividade
    {
        "temas_secundarios": ["mecanica_quantica", "personagens_esquecidos"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Einstein nunca ganhou o Nobel pela relatividade. O prêmio de 1921, entregue só em 1922, foi \"especialmente pela descoberta da lei do efeito fotoelétrico\", quando parte dos físicos ainda desconfiava da relatividade geral.",
        "explicacao": (
            "Em 1905, seu \"ano milagroso\", Einstein publicou quatro artigos que mudaram a física: explicou o efeito "
            "fotoelétrico, explicou o movimento browniano, apresentou a relatividade especial e mostrou que, se ela "
            "estivesse certa, massa e energia seriam equivalentes, a origem de E = mc². O trabalho sobre a "
            "relatividade continuou controverso por muitos anos, embora físicos de ponta, a começar por Max Planck, "
            "o tenham aceitado. A relatividade geral veio em 1915. Quando ele finalmente recebeu o Nobel de Física, "
            "em 1922, o prêmio era o de 1921, e a justificativa citava \"seus serviços à física teórica e, "
            "especialmente, a descoberta da lei do efeito fotoelétrico\". Nessa época, alguns físicos ainda viam a "
            "relatividade geral com ceticismo, e até a menção ao efeito fotoelétrico na justificativa mostrava "
            "certa dúvida. A ironia é que o efeito fotoelétrico, a ideia de que a luz chega em pacotes, foi uma das "
            "bases da física quântica, teoria com a qual Einstein brigaria pelo resto da vida."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Albert_Einstein",
            "In 1905, sometimes described as his annus mirabilis (miracle year), he published four groundbreaking papers. "
            "In them, he outlined a theory of the photoelectric effect, explained Brownian motion, introduced his special theory of relativity, and demonstrated that if the special theory is correct, mass and energy are equiv [...] "
            "Einstein's 1905 work on relativity remained controversial for many years, but was accepted by leading physicists, starting with Max Planck. [...] "
            "In 1922, he was awarded the 1921 Nobel Prize in Physics \"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect\". "
            "At this point some physicists still regarded the general theory of relativity skeptically, and the Nobel citation displayed a degree of doubt even about the work on photoelectricity that it acknowledg [...] "
            "ions to quantum theory. [...] "
            "In 1915, he proposed a general theory of relativity that extended his system of mechanics",
            nome="Albert Einstein")],
    },
    # 10 a primeira onda gravitacional
    {
        "temas_secundarios": ["buracos_negros", "acustica"],
        "tipos_espanto": ["escala_absurda", "engenhosidade"],
        "gancho": "A primeira onda gravitacional detectada, em 2015, encolheu e esticou os braços do detector LIGO em um milésimo da largura de um próton. Transformado em som, o sinal parece o pio de um passarinho.",
        "explicacao": (
            "O sinal chegou em 14 de setembro de 2015 e só foi anunciado em 11 de fevereiro de 2016, depois de os "
            "cientistas se certificarem de que não era um teste simulado. Ele vinha da fusão de dois buracos "
            "negros. Até então, as ondas gravitacionais, ondulações no próprio espaço-tempo previstas pela "
            "relatividade geral, só tinham sido percebidas de forma indireta. A onda mudou o comprimento efetivo "
            "de 1.120 quilômetros do LIGO em um milésimo da largura de um próton, o que equivale a mudar a "
            "distância até a estrela mais próxima fora do Sistema Solar na espessura de um fio de cabelo. Já a "
            "energia liberada foi imensa: no total, o equivalente a cerca de 3 massas solares convertidas em "
            "energia. O sinal durou pouco mais de 0,2 segundo e subiu de 35 para 250 hertz em uns 8 ciclos, uma "
            "faixa audível. Por isso foi comparado ao \"chirp\", o pio de um pássaro, e astrofísicos do mundo todo "
            "saíram imitando o som."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("First_observation_of_gravitational_waves",
            "The first direct observation of gravitational waves was made on 14 September 2015 and was announced by the LIGO and Virgo collaborations on 11 February 2016. "
            "Previously, gravitational waves had been inferred only indirectly [...] "
            "reached Earth as a ripple in spacetime that changed the length of a 1,120 km LIGO effective span by a thousandth of the width of a proton, proportionally equivalent to changing the distance to the nearest star outside the Solar System by one hair's width. "
            "The energy released by the binary as it spiralled together and merged was immense, with the energy of 3.0+0.5−0.5 c2 M☉ [...] "
            "ion as to whether the signals had been real detections or simulated data for testing purposes before it was ascertained that they were not tests. "
            "The chirp signal lasted over 0.2 seconds, and increased in frequency and amplitude in about 8 cycles from 35 Hz to 250 Hz. "
            "The signal is in the audible range and has been described as resembling the \"chirp\" of a bird; astrophysicists and other interested parties the world over excitedly responded by imitating the sign [...] "
            "black holes",
            nome="First observation of gravitational waves")],
    },
]
