LOTE = "2026-11-18-estrelas-01"
AREA = "espaco"
TEMA = "estrelas"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o núcleo do Sol rende como uma composteira
    {
        "temas_secundarios": ["termodinamica", "fisica_particulas"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Metro cúbico por metro cúbico, o centro do Sol produz pouca energia: cerca de 276,5 watts, mais ou menos o mesmo que uma pilha de compostagem. O Sol brilha tanto porque o núcleo é gigantesco.",
        "explicacao": (
            "No total, o Sol converte massa em energia a uma taxa de 4,26 bilhões de quilos por segundo, para "
            "isso consumindo 600 bilhões de quilos de hidrogênio, e despeja no espaço cerca de 384,6 yottawatts. "
            "Mas essa potência enorme vem sobretudo do tamanho e da densidade do núcleo, e não de uma reação "
            "intensa em cada pedaço dele. Os modelos do interior do Sol indicam que a densidade de potência "
            "máxima, no centro do núcleo, é de aproximadamente 276,5 watts por metro cúbico. Segundo o "
            "divulgador Karl Kruszelnicki, é mais ou menos a densidade de potência de uma pilha de compostagem. "
            "Isso acontece porque a fusão de hidrogênio é extremamente lenta para cada partícula: em média, um "
            "próton do núcleo leva cerca de 9 bilhões de anos para se fundir. E a taxa de fusão se regula "
            "sozinha. Se ela aumentasse um pouco, o núcleo esquentaria e se expandiria contra o peso das camadas "
            "de cima, o que reduziria a fusão de novo."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Sun",
            "releases energy at the mass–energy conversion rate of 4.26 billion kg/s (which requires 600 billion kg of hydrogen), for 384.6 yottawatts (3.846×1026 W) [...] "
            "The large power output of the Sun is mainly due to the huge size and density of its core (compared to Earth and objects on Earth), with only a fairly small amount of power being generated per cubic metre. "
            "Theoretical models of the Sun's interior indicate a maximum power density, or energy production, of approximately 276.5 watts per cubic metre at the centre of the core, which, according to Karl Kruszelnicki, is about the same as the power density inside a compost pile. "
            "The fusion rate in the core is in a stable equilibrium: a slightly higher rate of fusion would cause the core to heat up more and expand slightly against the weight of the outer layers [...] "
            "However, each proton (on average) takes around 9 billion years",
            nome="Sun")],
    },
    # 2 a luz que leva milênios para sair do Sol
    {
        "temas_secundarios": ["luz_cores", "fisica_particulas"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "A luz do Sol leva 8 minutos para chegar à Terra, mas pode ter levado de 10 mil a 170 mil anos só para sair do núcleo até a superfície. Já os neutrinos fazem esse trajeto em 2,3 segundos.",
        "explicacao": (
            "A energia nasce no núcleo como fótons de raios gama, que são absorvidos pelo plasma quase de "
            "imediato, em geral depois de andar só alguns milímetros. Cada fóton é emitido de novo numa direção "
            "aleatória, em geral com um pouco menos de energia, e o processo se repete. Com essa sequência de emissões e absorções, a radiação demora muito para "
            "chegar à superfície: as estimativas do tempo de viagem vão de 10 mil a 170 mil anos. Os neutrinos, "
            "partículas quase sem interação com a matéria, levam apenas 2,3 segundos para atravessar o mesmo "
            "caminho, e respondem por cerca de 2% de toda a energia produzida pelo Sol. Depois de sair da "
            "superfície, a luz chega à Terra, na distância média, em cerca de 8 minutos e 20 segundos. Ou seja, "
            "a luz que bate em você agora passou milênios presa dentro do Sol."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Sun",
            "With this sequence of emissions and absorptions, it takes a long time for radiation to reach the Sun's surface. "
            "Estimates of the photon travel time range between 10,000 and 170,000 years. "
            "In contrast, it takes only 2.3 seconds for neutrinos, which account for about 2% of the total energy production of the Sun, to reach the surface. [...] "
            "gamma ray photons initially released with fusion reactions in the core are almost immediately absorbed by the solar plasma of the radiative zone, usually after travelling only a few millimetres. "
            "Re-emission happens in a random direction and usually at slightly lower energy. [...] "
            "At its average distance, light travels from the Sun's horizon to Earth's horizon in about 8 minutes and 20 seconds.",
            nome="Sun")],
    },
    # 3 Cecilia Payne e a tese "quase certamente irreal"
    {
        "temas_secundarios": ["elementos_quimicos", "personagens_esquecidos", "historia_astronomia"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Em 1925, uma doutoranda descobriu que as estrelas são feitas sobretudo de hidrogênio. Pressionada por um astrônomo famoso, escreveu na tese que o resultado era \"quase certamente irreal\". Ela estava certa.",
        "explicacao": (
            "A astrônoma Cecilia Payne fez o doutorado pela Radcliffe College, porque Harvard não dava diplomas "
            "de doutorado a mulheres na época. Na tese, ela concluiu que o Sol e as estrelas são compostos "
            "principalmente de hidrogênio e hélio. Isso contrariava o consenso de então, de que o Sol e a Terra "
            "tinham composição parecida. Henry Norris Russell, um dos astrônomos mais importantes da época, "
            "chamou a conclusão de \"espúria\" e insistiu que ela não afirmasse que o Sol era feito "
            "predominantemente de hidrogênio. Payne manteve todos os cálculos, mas acomodou a crítica e incluiu "
            "a frase de que os resultados eram \"quase certamente irreais\". Quatro anos depois, Russell chegou à "
            "mesma conclusão por outro caminho e acabou levando boa parte do crédito. Quase 40 anos mais tarde, o "
            "astrônomo Otto Struve chamou o trabalho dela de \"a tese de doutorado mais brilhante já escrita em "
            "astronomia\". Hoje se sabe que a Via Láctea tem cerca de 74% de hidrogênio e 24% de hélio. Em 1956, "
            "Payne se tornou a primeira mulher promovida a professora titular dentro da Faculdade de Artes e "
            "Ciências de Harvard."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Cecilia_Payne-Gaposchkin",
            "composed primarily of hydrogen and helium in her 1925 doctoral thesis. "
            "Her groundbreaking conclusion was initially rejected by leading astrophysicists, including Henry Norris Russell, because it contradicted the science of the time, which held that no significant elemental differences distinguished the Sun and Earth. [...] "
            "Henry Norris Russell, a pre-eminent astronomer of the day who adhered to the theories of American physicist Henry Rowland, urged her not to assert that the composition of the Sun was predominantly hydrogen [...] "
            "Consequently, Russell described her scientific conclusion as \"spurious\". "
            "Although she included all calculations and results, Payne accommodated the criticism of her reviewer by including a statement in her thesis that her results were \"almost certainly not real\". "
            "Four years later, however, Russell realized that [...] "
            "yet Russell was generally credited for the conclusions Payne had reached four years prior. "
            "Nearly 40 years after Payne's thesis was published, professional recognition of her discovery was given to her by astronomer Otto Struve when he described her work as \"the most brilliant PhD thesis ever written in astronomy\". "
            "Today's accepted ratios for hydrogen and helium in the Milky Way Galaxy are ~74% hydrogen and ~24% helium [...] "
            "as the university did not grant doctoral degrees to women at the time. "
            "Instead, she received her doctoral degree from Radcliffe College [...] "
            "in 1956 she became the first woman to be promoted to full professor from within the faculty at Harvard's Faculty of Arts and Sciences.",
            nome="Cecilia Payne-Gaposchkin")],
    },
    # 4 o "homenzinho verde" que era um pulsar
    {
        "temas_secundarios": ["personagens_esquecidos", "telecomunicacoes", "buracos_negros"],
        "tipos_espanto": ["historia_humana", "misterio_aberto"],
        "gancho": "Em 1967, uma estudante achou num papel de registro um sinal de rádio que pulsava a cada 1,33 segundo, regular como um relógio. Foi apelidado de \"Homenzinho Verde 1\". Era o primeiro pulsar conhecido.",
        "explicacao": (
            "Jocelyn Bell fazia o doutorado em Cambridge e tinha passado dois anos ajudando a construir um "
            "radiotelescópio, o Interplanetary Scintillation Array, criado para estudar quasares. Os dados saíam "
            "em rolos de papel de um registrador e tinham de ser conferidos à mão, às vezes 29 metros de papel "
            "por noite. Em 28 de novembro de 1967, ela notou um \"pedacinho de sujeira\" no registro que se movia "
            "pelo céu junto com as estrelas. O sinal já aparecia em dados de agosto, mas levou três meses para "
            "ser encontrado. Ela mostrou que ele pulsava com enorme regularidade, cerca de uma vez a cada um "
            "segundo e um terço. Provisoriamente, a fonte ganhou o apelido de LGM-1, \"Little Green Man\", e "
            "depois de alguns anos foi identificada como uma estrela de nêutrons girando muito rápido. A "
            "descoberta rendeu o Nobel de Física de 1974, mas ela não estava entre os premiados, o que gerou "
            "polêmica. Em 2018, ao receber o Prêmio Breakthrough, ela doou os 3 milhões de dólares a um fundo de "
            "bolsas para promover mais diversidade na física."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Jocelyn_Bell_Burnell",
            "while conducting research for her doctorate in 1967, discovered the first known pulsar. "
            "This discovery was recognized by the Nobel Prize in Physics in 1974, though she was not among its recipients. [...] "
            "At Cambridge, she worked with Antony Hewish and others to construct the Interplanetary Scintillation Array just outside Cambridge to study quasars [...] "
            "On 28 November 1967, while a postgraduate student at Cambridge, Bell Burnell detected a \"bit of scruff\" on her chart-recorder papers that tracked across the sky with the stars. "
            "The signal had been visible in data taken in August, but as the papers had to be checked by hand, it took her three months to find it. "
            "She established that the signal was pulsing with great regularity, at a rate of about one pulse every one and a third seconds. "
            "Temporarily dubbed \"Little Green Man 1\" (LGM-1) the source (now known as PSR B1919+21) was identified after several years as a rapidly rotating neutron star. [...] "
            "Controversially, Bell did not receive recognition in the 1974 Nobel Prize in Physics. "
            "She helped build the Interplanetary Scintillation Array over two years and initially noticed the anomaly, sometimes reviewing as much as 96 feet (29 m) of paper data per night. [...] "
            "She donated the three million dollars of the Breakthrough Prize to the Bell Burnell Scholarship Fund to promote greater diver [...] "
            "In 2018, she was awarded the Special Breakthrough Prize in Fundamental Physics.",
            nome="Jocelyn Bell Burnell")],
    },
    # 5 telégrafos funcionando com a aurora
    {
        "temas_secundarios": ["telecomunicacoes", "eletromagnetismo", "sistema_solar"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1859, uma tempestade solar foi tão forte que telegrafistas de Boston e Portland desligaram as baterias e trocaram mensagens por duas horas usando só a corrente induzida pela aurora.",
        "explicacao": (
            "É o Evento Carrington, a tempestade geomagnética mais intensa já registrada, com pico em 1º e 2 de "
            "setembro de 1859. Ela veio, muito provavelmente, de uma ejeção de massa da coroa solar que atingiu a "
            "magnetosfera da Terra depois de cruzar 150 milhões de quilômetros em 17,6 horas, quando o comum são "
            "vários dias. Pouco antes, os astrônomos britânicos Richard Carrington e Richard Hodgson tinham "
            "registrado, cada um por conta própria, um clarão muito forte no Sol: os primeiros registros de uma "
            "erupção solar. As auroras foram vistas no mundo todo, até perto do equador, em lugares como Cuba, "
            "Havaí e Colômbia. Nas Montanhas Rochosas, o brilho acordou garimpeiros, que começaram a fazer o café "
            "da manhã achando que já era dia. As correntes induzidas derrubaram sistemas de telégrafo na Europa e "
            "na América do Norte e provocaram faíscas e até incêndios em estações. Na noite de 2 de setembro, os "
            "operadores de Boston e de Portland desconectaram as baterias e seguiram trabalhando com a corrente "
            "da aurora, a primeira vez registrada em que se transmitiu mais do que uma ou duas palavras assim. "
            "Uma tempestade dessa força hoje poderia causar apagões em larga escala."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Carrington_Event",
            "The Carrington Event was the most intense geomagnetic storm in recorded history, peaking on 1–2 September 1859 during solar cycle 10. "
            "It created strong auroral displays that were reported globally and caused sparking and even fires in telegraph stations. "
            "The geomagnetic storm was most likely the result of a coronal mass ejection (CME) from the Sun colliding with Earth's magnetosphere. [...] "
            "It was observed and recorded independently by British astronomers Richard Carrington and Richard Hodgson—the first records of a solar flare. "
            "A geomagnetic storm of this magnitude occurring today has the potential to cause widespread electrical disruptions and blackouts [...] "
            "taking 17.6 hours to make the 150×10^6 km (93×10^6 mi) journey. Typical CMEs take several days to arrive at Earth [...] "
            "the glow awakened gold miners, who were reported to have begun to prepare breakfast because they thought it was morning. [...] "
            "The aurora was also visible from the poles to low latitude areas such as south-central Mexico, Cuba, Hawaii, Queensland, southern Japan and China, New Zealand, and even at lower latitudes very close to the equator, such as Colombia. [...] "
            "telegraph systems all over Europe and North America failed [...] "
            "on the night of 2 September 1859 [...] "
            "The conversation was carried on for around two hours using no battery power and working solely with the current induced by the aurora, the first time on record that more than a word or two was transmitted in such manner.",
            nome="Carrington Event")],
    },
    # 6 o hélio foi achado no Sol antes da Terra
    {
        "temas_secundarios": ["elementos_quimicos", "historia_astronomia", "vulcoes_terremotos"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O hélio foi descoberto no Sol, numa linha amarela da luz de um eclipse em 1868, 27 anos antes de ser isolado na Terra. Por isso tem o nome do deus grego do Sol, Hélio.",
        "explicacao": (
            "Durante o eclipse total de 18 de agosto de 1868, observado em Guntur, na Índia, o astrônomo francês "
            "Jules Janssen registrou no espectro da cromosfera do Sol uma linha amarela brilhante, de 587,49 "
            "nanômetros. Primeiro, ela foi tomada por sódio. Em 20 de outubro do mesmo ano, o inglês Norman "
            "Lockyer observou a linha da Grã-Bretanha e a chamou de D3, por estar perto das linhas D1 e D2 do "
            "sódio. Só Lockyer propôs que ela vinha de um elemento novo, e o batizou a partir de helios, \"Sol\" "
            "em grego antigo. A terminação -io costuma ser reservada a metais, e provavelmente Lockyer, por ser "
            "astrônomo, não conhecia a convenção dos químicos. Em 1881, o físico italiano Luigi Palmieri detectou "
            "a linha D3 em material de uma erupção recente do Vesúvio, a primeira detecção do hélio na Terra. A "
            "descoberta formal veio em 1895, quando os químicos William Ramsay, Per Teodor Cleve e Nils Abraham "
            "Langlet encontraram o gás saindo de um minério de urânio."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Helium",
            "Helium (from Ancient Greek: ἥλιος, romanized: helios, lit. 'sun') is a chemical element [...] "
            "However, only Lockyer proposed that the line was due to a new element, which he named after the Sun. "
            "The formal discovery of the element was made in 1895 by chemists Sir William Ramsay, Per Teodor Cleve, and Nils Abraham Langlet, who found helium emanating from the uranium ore cleveite [...] "
            "gust 18, 1868, as a bright yellow line with a wavelength of 587.49 nanometers in the spectrum of the chromosphere of the Sun. "
            "The line was detected by French astronomer Jules Janssen during a total solar eclipse in Guntur, India. "
            "This line was initially assumed to be sodium. "
            "On October 20 of the same year, English astronomer Norman Lockyer observed a yellow line in the solar spectrum, which he named the D3 because it was near the known D1 and D2 Fraunhofer lines of sodium. [...] "
            "s unusual, as it normally applies only to metallic elements; probably Lockyer, being an astronomer, was unaware of the chemical conventions. [...] "
            "In 1881, Italian physicist Luigi Palmieri detected helium on Earth for the first time through its D3 spectral line, when he analyzed a material that had been sublimated during a recent eruption of Mount Vesuv [...] "
            "while Lockyer observed it from Britain.",
            nome="Helium")],
    },
    # 7 o ouro das estrelas de nêutrons
    {
        "temas_secundarios": ["elementos_quimicos", "buracos_negros", "relatividade"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "Em 2017, detectores captaram a colisão de duas estrelas de nêutrons a 130 milhões de anos-luz. Calcula-se que o choque fabricou cerca de 10 vezes a massa da Terra só em ouro e platina.",
        "explicacao": (
            "O sinal chegou primeiro como onda gravitacional, um tremor no próprio espaço-tempo, captado pelos "
            "detectores LIGO e Virgo em 17 de agosto de 2017. Ele vinha dos últimos instantes de duas estrelas de "
            "nêutrons que giravam uma em torno da outra até se fundir, na galáxia NGC 4993. Ao contrário das "
            "colisões de buracos negros detectadas antes, esta apareceu também em luz: 1,7 segundo depois da onda "
            "gravitacional, satélites registraram um surto de raios gama, e 11 horas depois telescópios acharam o "
            "brilho no céu. No total, 70 observatórios de sete continentes e do espaço acompanharam o evento, um "
            "marco da chamada astronomia multimensageira. O brilho, uma quilonova, era alimentado pelo "
            "decaimento radioativo de núcleos pesados recém-fabricados. Estima-se que se formaram cerca de 16 mil "
            "massas terrestres de elementos pesados. O resultado reforçou que colisões assim, e não só explosões "
            "de supernova como se supunha, são a principal fonte dos elementos mais pesados que o ferro, como o "
            "ouro e a platina."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("GW170817",
            "GW170817 was a gravitational wave (GW) observed by the LIGO and Virgo detectors on 17 August 2017, originating within the shell elliptical galaxy NGC 4993, about 130 million light-years away. "
            "The wave was produced by the last moments of the inspiral of a binary pair of neutron stars, ending with their merger. [...] "
            "k holes and thus not expected to have detectable electromagnetic signals—the aftermath of this merger was seen across the electromagnetic spectrum by 70 observatories on 7 continents and in space, marking a significant breakthrough for multi-messenger astronomy. [...] "
            "was detected by the Fermi and INTEGRAL spacecraft beginning 1.7 seconds after the GW emitted by the merger. [...] "
            "11 hours after the signal, an astronomical transient SSS17a, later designated kilonova AT 2017gfo, was observed in the galaxy NGC 4993. [...] "
            "of 16,000 times the mass of the Earth in heavy elements is believed to have formed, including approximately 10 Earth masses just of the two elements gold and platinum. [...] "
            "previously assumed to be associated with supernova explosions—and are therefore the primary source of r-process elements heavier than iron, including gold and platinum. [...] "
            "a spherically expanding optical afterglow powered by the radioactive decay of heavy r-process nuclei produced and ejected at the",
            nome="GW170817")],
    },
    # 8 os neutrinos que faltavam
    {
        "temas_secundarios": ["fisica_particulas", "historia_astronomia"],
        "tipos_espanto": ["misterio_aberto", "historia_humana"],
        "gancho": "Por quase 40 anos, os detectores acharam só cerca de um terço dos neutrinos que o Sol deveria emitir. O Sol estava certo: os neutrinos mudam de tipo no caminho, e isso rendeu dois prêmios Nobel.",
        "explicacao": (
            "O Sol produz energia fundindo hidrogênio, e cada reação solta neutrinos, partículas que saem do "
            "núcleo e chegam à Terra sem ser absorvidas. No fim dos anos 1960, o Experimento Homestake, de Ray "
            "Davis e John Bahcall, foi o primeiro a medir esse fluxo, com um detector à base de cloro, e encontrou "
            "um déficit em relação ao previsto pelo modelo solar que o próprio Bahcall ajudara a criar. Outros "
            "experimentos confirmaram a falta: só cerca de um terço do esperado. Ajustar o modelo do Sol não "
            "resolvia, porque uma parte dos dados pedia um núcleo mais frio e outra, um núcleo mais quente. A "
            "solução estava nos neutrinos: há três tipos deles, e o Sol produz só o tipo elétron, o único que os "
            "primeiros detectores viam. No caminho, parte deles se transforma nos outros tipos. O problema foi "
            "dado como resolvido por volta de 2002. Davis e Masatoshi Koshiba dividiram o Nobel de 2002, e Takaaki "
            "Kajita e Arthur McDonald ganharam o de 2015. Curiosamente, até o comitê do Nobel errou num detalhe: "
            "nos neutrinos de alta energia vistos por um dos experimentos, a mudança vem de um efeito ligado à "
            "matéria do Sol, chamado Mikheyev–Smirnov–Wolfenstein."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Solar_neutrino_problem",
            "The solar neutrino problem concerned a large discrepancy between the flux of solar neutrinos as predicted from the Sun's luminosity and as measured directly. "
            "The discrepancy was first observed in the mid-1960s and was resolved around 2002. [...] "
            "The neutrinos travel from the Sun's core to Earth without any appreciable absorption by the Sun's outer layers. "
            "In the late 1960s, Ray Davis and John N. Bahcall's Homestake Experiment was the first to measure the flux of neutrinos from the Sun and detect a deficit. "
            "The experiment used a chlorine-based detector. [...] "
            "ar neutrinos was computed using the standard solar model, which Bahcall had helped establish. [...] "
            "while the overall lower neutrino flux (which the Homestake experiment results found) required a reduction in the solar core temperature, details in the energy spectrum of the neutrinos required a higher core temperature. [...] "
            "According to the Standard Model of particle physics, there are three flavors of neutrinos: electron neutrinos, muon neutrinos, and tau neutrinos. "
            "Electron neutrinos are the ones produced in the Sun and the ones detected by the above-mentioned experiments [...] "
            "In 2002, Ray Davis and Masatoshi Koshiba won part of the Nobel Prize in Physics for experimental work which found the number of solar neutrinos to be around a third of the number predicted [...] "
            "Takaaki Kajita from the Super-Kamiokande Observatory and Arthur McDonald from the Sudbury Neutrino Observatory (SNO) were awarded the 2015 Nobel Prize for Physics. "
            "The Nobel Committee for Physics, however, erred in mentioning neutrino oscillations in regard to the SNO Experiment: for the high-energy solar neutrinos observed in that experiment, it is not neutrino oscillations, but rather the Mikheyev–Smirnov–Wolfenstein effect",
            nome="Solar neutrino problem")],
    },
    # 9 Betelgeuse: o apagão e a companheira
    {
        "temas_secundarios": ["historia_astronomia", "luz_cores"],
        "tipos_espanto": ["misterio_aberto", "contraintuitivo"],
        "gancho": "Em 2019, Betelgeuse, o ombro de Órion, perdeu dois terços do brilho, e muitos acharam que ia explodir. Era uma nuvem de poeira que a própria estrela soltou. E em 2025 acharam uma companheira dela.",
        "explicacao": (
            "A partir de outubro de 2019, a supergigante vermelha começou a escurecer, e em meados de fevereiro de "
            "2020 seu brilho tinha caído cerca de três vezes. Ela saiu da lista das 10 estrelas mais brilhantes do "
            "céu e ficou mais fraca que a vizinha Aldebarã. A imprensa especulou sobre uma supernova iminente, mas "
            "os astrônomos lembraram que a explosão é esperada para algum momento dos próximos 100 mil anos. "
            "Estudos com o telescópio espacial Hubble indicaram a causa: a estrela lançou material da superfície a "
            "milhões de quilômetros, e esse material esfriou e virou a poeira que bloqueou a luz. O episódio "
            "ficou conhecido como \"Grande Escurecimento\". Em julho de 2025, foram anunciadas observações de uma "
            "provável estrela companheira, bem menor e mais fraca, batizada de Siwarha, \"o bracelete dela\" em "
            "árabe. Ainda não está totalmente confirmado que ela esteja presa à Betelgeuse pela gravidade. Quando "
            "Betelgeuse explodir, deve brilhar como a meia-lua por mais de três meses, sem risco para a vida na "
            "Terra."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Betelgeuse",
            "Starting in October 2019, Betelgeuse began to dim noticeably, and by mid-February 2020 its brightness had dropped by a factor of approximately 3, from magnitude 0.5 to 1.7. [...] "
            "The episode is sometimes referred to as the \"Great Dimming event\". [...] "
            "A study using the Hubble Space Telescope suggests that occluding dust was created by a surface mass ejection; this material was cast millions of miles from the star, and then cooled to form the dust that caused the dimming. "
            "Betelgeuse is likely a binary star. "
            "The companion star, named Betelgeuse B or Siwarha, is not yet fully confirmed to be gravitionally bound to Betelgeuse, but likely is given other, indirect evidence for a companion. "
            "It would be much smaller and fainter than the red supergiant [...] "
            "with the Gemini North Observatory (instrument ‘Alopeke) was announced in July 2025 [...] "
            "proposed the name Siwarha, which means her bracelet in Arabic. [...] "
            "This dropped Betelgeuse from one of the top 10 brightest stars in the sky to outside the top 20, noticeably dimmer than its near neighbor Aldebaran. "
            "2019 mainstream media reports discussed speculation that Betelgeuse might be about to explode as a supernova, but astronomers note that the supernova is expected to occur within approximately the next 100,000 years and is thus unlikely to be imminent. [...] "
            "When Betelgeuse detonates as a brilliant type II supernova, it will shine as bright as the half-Moon for more than three months; life on Earth will be unharmed.",
            nome="Betelgeuse")],
    },
    # 10 a coroa mais quente que a superfície
    {
        "temas_secundarios": ["termodinamica", "eletromagnetismo"],
        "tipos_espanto": ["misterio_aberto", "contraintuitivo"],
        "gancho": "A superfície do Sol tem uns 6.000 graus, mas a coroa, a camada externa e rarefeita acima dela, passa de 1 milhão. Como algo fica mais quente longe da fonte de calor ainda é discutido.",
        "explicacao": (
            "A fotosfera, a superfície visível do Sol, está a cerca de 6.000 kelvin, enquanto a coroa chega a "
            "1 a 2 milhões de kelvin. Essa temperatura mostra que a coroa é aquecida por outra coisa que não a "
            "simples condução de calor a partir da superfície. Acredita-se que a energia venha do movimento "
            "turbulento da zona de convecção, logo abaixo da fotosfera, e há duas explicações principais. Na "
            "primeira, essa turbulência produz ondas, sonoras, gravitacionais ou magnéticas, que sobem e "
            "despejam sua energia na coroa na forma de calor. Na segunda, o movimento da superfície acumula "
            "energia nos campos magnéticos, que se rompem e se reconectam, liberando-a em grandes erupções solares "
            "e numa miríade de eventos menores, as nanoexplosões. Ainda não está claro se as ondas são um meio "
            "eficiente de aquecimento: quase todas se dissipam ou se desviam antes de chegar à coroa, e as que "
            "chegam, as ondas de Alfvén, não se dissipam com facilidade lá em cima."
        ),
        "nivel": 2, "nota_surpresa": 3, "confianca": "consenso_parcial",
        "fontes": [wiki("Sun",
            "The temperature of the photosphere is approximately 6,000 K, whereas the temperature of the corona reaches 1,000,000–2,000,000 K. "
            "The high temperature of the corona shows that it is heated by something other than direct heat conduction from the photosphere. "
            "It is thought that the energy necessary to heat the corona is provided by turbulent motion in the convection zone below the photosphere, and two main mechanisms have been proposed to explain coronal heating. "
            "The first is wave heating, in which sound, gravitational or magnetohydrodynamic waves are produced by turbulence in the convection zone. [...] "
            "The other is magnetic heating, in which magnetic energy is continuously built up by photospheric motion and released through magnetic reconnection in the form of large solar flares and myriad similar but smaller events—nanoflares. "
            "Currently, it is unclear whether waves are an efficient heating mechanism. "
            "All waves except Alfvén waves have been found to dissipate or refract before reaching the corona. "
            "In addition, Alfvén waves do not easily dissipate in the corona.",
            nome="Sun")],
    },
    # 11 o paradoxo do Sol jovem e fraco
    {
        "temas_secundarios": ["mudancas_climaticas", "atmosfera", "astrobiologia"],
        "tipos_espanto": ["misterio_aberto", "contraintuitivo"],
        "gancho": "No começo da história da Terra, o Sol brilhava só 70% do que brilha hoje, e o planeta deveria estar congelado. Mas há sinais de água líquida e de vida. Explicar isso é o paradoxo do Sol jovem e fraco.",
        "explicacao": (
            "As estrelas como o Sol ficam mais brilhantes com a idade, porque o núcleo vai acumulando hélio. "
            "Desde o início de sua vida estável, o Sol aumentou de raio em 15% e ficou 48% mais luminoso. Com só "
            "70% da potência atual, a Terra primitiva deveria ter sido uma bola de gelo, mas os indícios apontam "
            "água líquida e vida. A questão foi levantada pelos astrônomos Carl Sagan e George Mullen em 1972. Eles "
            "sugeriram que muita amônia na atmosfera teria segurado o calor, mas depois se mostrou que a amônia, "
            "embora seja um bom gás de efeito estufa, é destruída com facilidade pela luz solar. As propostas de "
            "solução envolvem gases de efeito estufa, mudanças na refletividade do planeta, influências "
            "astronômicas ou combinações disso. A teoria predominante é que o gás carbônico, em concentração bem "
            "maior que a atual, foi o principal responsável por aquecer a Terra nessa época."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Faint_young_Sun_paradox",
                "The faint young Sun paradox or faint young Sun problem describes the apparent contradiction between observations of liquid water early in Earth's history and the astrophysical expectation that the Sun's output would have been only 70 percent as intense during that epoch as it is during the [...] "
                "with the young Sun's output at only 70 percent of its current output, early Earth would be expected to be completely frozen, but early Earth seems to have had liquid water and supported life. "
                "The issue was raised by astronomers Carl Sagan and George Mullen in 1972. "
                "Proposed resolutions of this paradox have taken into account greenhouse effects, changes to planetary albedo, astrophysical influences, or combinations of these suggestions. "
                "The predominant theory is that the greenhouse gas carbon dioxide contributed most to the warming of the Earth. [...] "
                "Sagan and Mullen suggested during their descriptions of the paradox that it might be solved by high concentrations of ammonia gas, NH3. "
                "However, it has since been shown that while ammonia is an effective greenhouse gas, it is easily destroyed photochemically in the at [...] "
                "It is now thought that carbon dioxide was present in higher concentrations during this period of lower solar radiation.",
                nome="Faint young Sun paradox"),
            wiki("Sun",
                "since the beginning of its main sequence life, it has expanded in radius by 15% and the surface has increased in temperature from 5,620 K (9,660 °F) to 5,772 K (9,930 °F), resulting in a 48% increase in luminosity from 0.677 solar luminosities to its present-day 1.0 solar luminosity. "
                "This occurs because the helium atoms in the core have a higher mean",
                nome="Sun"),
        ],
    },
]
