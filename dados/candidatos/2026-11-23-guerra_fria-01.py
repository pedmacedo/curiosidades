LOTE = "2026-11-23-guerra_fria-01"
AREA = "historia_moderna"
TEMA = "guerra_fria"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Petrov e o alarme falso de 1983
    {
        "temas_secundarios": ["teoria_jogos", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Em 1983, o alerta soviético por satélite indicou cinco mísseis americanos a caminho. O oficial de plantão, Stanislav Petrov, apostou num defeito e não tratou o aviso como ataque. Era o Sol refletido em nuvens altas.",
        "explicacao": (
            "Logo depois da meia-noite de 26 de setembro de 1983, o tenente-coronel Stanislav Petrov estava de "
            "plantão num bunker perto de Moscou, centro de comando dos satélites soviéticos de alerta antecipado. "
            "Pela doutrina da época, um ataque detectado exigia um contra-ataque nuclear imediato. Os computadores "
            "apontaram primeiro um míssil intercontinental vindo dos EUA e, depois, mais quatro. Petrov pesou três "
            "coisas: pelo que aprendera, um primeiro ataque americano envolveria centenas de mísseis ao mesmo tempo, e "
            "não cinco; o sistema de detecção era novo e, para ele, ainda pouco confiável; e o radar em terra não "
            "confirmava nada, mesmo minutos depois. Ele considerou o aviso um alarme falso. Os relatos divergem sobre "
            "se ele chegou a informar os superiores. Mais tarde, concluiu-se que o sistema tinha mesmo falhado: o "
            "alarme veio de um alinhamento raro entre a luz do Sol, nuvens em grande altitude e a órbita dos "
            "satélites. O momento era de tensão extrema: semanas antes, os soviéticos tinham derrubado um avião de "
            "passageiros sul-coreano. Petrov não recebeu recompensa. Segundo ele, porque o caso constrangia os "
            "superiores e os cientistas responsáveis pelo sistema. O episódio só veio a público em 1998."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("1983_Soviet_nuclear_false_alarm_incident",
            "On 26 September 1983, during the Cold War, the Soviet nuclear early warning system Oko reported the launch of one intercontinental ballistic missile with four more missiles behind it, from the United States. [...] "
            "On 1 September 1983, the Soviet military shot down a South Korean passenger jet, Korean Air Lines Flight 007 [...] "
            "On 26 September 1983, Stanislav Petrov, a lieutenant colonel in the Soviet Air Defense Forces, was the officer on duty at the Serpukhov-15 bunker near Moscow which housed the command center of the Soviet early warning satellites, code-named Oko. [...] "
            "the Soviet Union's strategy was an immediate and compulsory nuclear counter-attack against the United States (launch on warning) [...] "
            "Shortly after midnight, the bunker's computers reported that one intercontinental ballistic missile was heading toward the Soviet Union from the United States. "
            "Petrov considered the detection a computer error, since a first-strike nuclear attack by the United States was likely to involve hundreds of simultaneous missile launches [...] "
            "Petrov dismissed the warning as a false alarm, though accounts of the event differ as to whether he notified his superiors or not [...] "
            "It was subsequently determined that the false alarms were caused by a rare alignment of sunlight on high-altitude clouds and the satellites' Molniya orbits [...] "
            "Petrov cited his belief and training that any U.S. first strike would be massive, so five missiles seemed an illogical start. "
            "In addition, the launch detection system was new and in his view not yet wholly trustworthy, while ground radar had failed to pick up corroborative evidence even after several minutes of the false alarm. [...] "
            "(and the first to reveal it to the public in 1998) [...] "
            "He received no reward. According to Petrov, this was because the incident and other bugs found in the missile detection system embarrassed his superiors and the influential scientists who were responsible for it",
            nome="1983 Soviet nuclear false alarm incident")],
    },
    # 2 Arkhipov e o submarino B-59
    {
        "temas_secundarios": ["personagens_esquecidos", "teoria_jogos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Em 1962, navios americanos soltaram cargas de profundidade de sinalização perto de um submarino soviético que levava um torpedo nuclear. O capitão, achando que a guerra começara, quis disparar. Um oficial se opôs.",
        "explicacao": (
            "Era 27 de outubro de 1962, auge da Crise dos Mísseis de Cuba. Onze destróieres e um porta-aviões dos "
            "EUA detectaram perto de Cuba o B-59, submarino soviético a diesel armado com torpedo nuclear. Mesmo em "
            "águas internacionais, a Marinha americana soltou cargas de profundidade de sinalização para forçá-lo a "
            "emergir e se identificar. Fazia dias que não havia contato com Moscou, e, fugindo em profundidade, a "
            "tripulação não recebia rádio: ninguém a bordo sabia se a guerra já tinha começado. O capitão Valentin "
            "Savitsky achava possível que sim e queria lançar o torpedo. Na maioria dos submarinos soviéticos com "
            "torpedos nucleares, bastava a autorização do capitão e do oficial político. No B-59, era preciso uma "
            "terceira assinatura, porque o imediato, Vasili Arkhipov, também era chefe do estado-maior da flotilha. "
            "Ele foi o único contra e acabou convencendo o capitão a emergir e esperar ordens. Na volta, muitos "
            "tripulantes foram repreendidos. A história se apoia sobretudo em depoimentos dados décadas depois: um "
            "tripulante a contou com menos drama, dizendo que o capitão perdeu a calma, mas se acalmou. E, em 2024, "
            "um historiador observou que documentos liberados pelo Ministério da Defesa russo em 2022 não mencionam "
            "o episódio."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Vasily_Arkhipov",
            "At the time of the crisis, Arkhipov was chief of staff of a Soviet submarine flotilla and was aboard the submarine B-59 as executive officer. [...] "
            "On 27 October 1962, during the Cuban Missile Crisis, a group of 11 United States Navy destroyers and the aircraft carrier USS Randolph (CV-15) detected the Soviet diesel-powered, nuclear-armed Foxtrot-class submarine B-59 near Cuba. [...] "
            "Although in international waters, the U.S. Navy dropped signaling depth charges to force B-59 to surface for identification. "
            "There was no contact from Moscow for several days. Earlier the crew had intercepted U.S. civilian broadcasts, but at depth they could not receive radio traffic while evading pursuit. "
            "The men did not know whether war had already begun. "
            "Captain Valentin Grigoryevich Savitsky believed hostilities might have started and wanted to launch a nuclear T-5 torpedo. "
            "On most Soviet submarines armed with nuclear torpedoes, only the captain and political officer were required to authorize a launch. "
            "On B-59, a third signature was needed because Vasili Arkhipov was also chief of staff of the brigade [...] "
            "An argument followed, with only Arkhipov opposing the launch. [...] "
            "He eventually persuaded Savitsky to surface and await orders. [...] "
            "On returning to the Soviet Union, many crew members were reprimanded. [...] "
            "In 2002, retired Commander Vadim Orlov, who was aboard B-59, confirmed the submarines carried nuclear torpedoes and credited Arkhipov with preventing their use. "
            "He described the situation less dramatically, saying Captain Savitsky lost his temper but calmed down. [...] "
            "In 2024, historian Sergey Radchenko argued that evidence on Arkhipov's role relied on oral testimony published by Svetlana Savranskaya. "
            "When the Russian Ministry of Defense declassified documents in 2022, the Arkhipov incident was not mentioned.",
            nome="Vasily Arkhipov")],
    },
    # 3 a linha direta nunca foi telefone
    {
        "temas_secundarios": ["telecomunicacoes", "teoria_jogos"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "O \"telefone vermelho\" entre Washington e Moscou nunca foi telefone. A linha direta, criada em 1963, usava teleimpressoras, só com texto, porque a fala podia ser mal interpretada.",
        "explicacao": (
            "Na Crise dos Mísseis de Cuba, em 1962, os EUA levaram quase doze horas para receber e decodificar a "
            "primeira proposta de acordo de Nikita Khrushchev, uma mensagem de 3.000 palavras. Quando a resposta "
            "ficou pronta, Moscou já tinha mandado outra, mais dura. O susto convenceu os dois lados de que "
            "precisavam de um canal mais rápido, e o acordo da linha direta foi assinado em junho de 1963. Na cultura "
            "popular, ela virou o \"telefone vermelho\", mas nunca foi uma linha telefônica. Foi pensada só para "
            "texto: cada líder escrevia na própria língua, e a tradução era feita na chegada. Os EUA mandaram a "
            "Moscou teleimpressoras com alfabeto latino, e os soviéticos mandaram a Washington aparelhos com "
            "alfabeto cirílico. A primeira mensagem, de 30 de agosto de 1963, foi um pangrama em inglês, frase que "
            "usa todas as letras, para testar a impressão de cada caractere. O sistema passou a usar fax em 1986 e, "
            "desde 2008, é uma rede de computadores segura, com e-mail. Nos tempos do cabo, a linha principal chegou "
            "a ser cortada por acidente perto de Copenhague, por um tratorista dinamarquês, e por um agricultor "
            "finlandês que a arrancou com o arado."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Moscow%E2%80%93Washington_hotline",
            "Although in popular culture it is known as the \"red telephone\", the hotline was never a telephone line, and no red phones were used. "
            "The first implementation used Teletype equipment, and shifted to fax machines in 1986. "
            "Since 2008, the Moscow–Washington hotline has been a secure computer link over which messages are exchanged by a secure form of email. [...] "
            "The 1962 Cuban Missile Crisis made the hotline a priority. [...] "
            "During the crisis, the United States took nearly twelve hours to receive and decode Nikita Khrushchev's 3,000-word-initial settlement message – a dangerously long time. "
            "By the time Washington had drafted a reply, a tougher message from Moscow had been received [...] "
            "The two countries signed the Hot Line Agreement on June 20, 1963 [...] "
            "The Moscow–Washington hotline was intended for text only; speech might be misinterpreted. "
            "Leaders wrote in their native language and messages were translated at the receiving end. [...] "
            "In July 1963 the United States sent four sets of teleprinters with the Latin alphabet to Moscow for the terminal there. "
            "A month later the Soviet equipment, four sets of East German teleprinters with the Cyrillic alphabet made by Siemens, arrived in Washington. [...] "
            "The first message transmitted over the hotline was on August 30, 1963. [...] "
            "(a pangram to test printing of each character in the alphabet) [...] "
            "The primary link was accidentally cut several times, for example near Copenhagen by a Danish bulldozer operator, and by a Finnish farmer who ploughed it up once.",
            nome="Moscow–Washington hotline")],
    },
    # 4 Projeto A119: uma bomba na Lua
    {
        "temas_secundarios": ["exploracao_espacial", "sistema_solar"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Em 1958, a Força Aérea dos EUA estudou em segredo explodir uma bomba atômica na Lua, com um clarão visível da Terra, para levantar o moral americano. Um dos cientistas do estudo era o jovem Carl Sagan.",
        "explicacao": (
            "Com o Sputnik, em 1957, a União Soviética tinha saído na frente na corrida espacial, e os EUA buscavam "
            "uma resposta. No projeto secreto A119, uma equipe de dez pessoas no Instituto de Tecnologia de "
            "Illinois, liderada por Leonard Reiffel, estudou se a explosão seria visível, o que ela traria para a "
            "ciência e o que faria com a superfície lunar. A ideia de usar uma bomba de hidrogênio foi vetada pela "
            "Força Aérea, porque ela seria pesada demais para o míssil. A escolha recaiu sobre uma ogiva leve, de "
            "1,7 quiloton, bem mais fraca que a bomba de Hiroshima. Ela explodiria no impacto, no lado sombreado da "
            "Lua, e a nuvem de poeira iluminada pelo Sol poderia ser vista daqui. O doutorando Carl Sagan, aluno do "
            "astrônomo Gerard Kuiper, cuidou da projeção matemática de como essa nuvem se expandiria. A Força Aérea "
            "cancelou o plano em janeiro de 1959, ao que parece por medo do risco à população se o lançamento desse "
            "errado; Reiffel citou também a contaminação radioativa, que atrapalharia pesquisas futuras na Lua. O "
            "projeto só foi revelado em 2000, pelo próprio Reiffel, e o governo americano nunca o reconheceu "
            "oficialmente. Os soviéticos tiveram um projeto parecido, que também não saiu do papel."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Project_A119",
            "Project A119, also known as A Study of Lunar Research Flights, was a top-secret plan developed in 1958 by the United States Air Force. "
            "The aim of the project was to detonate a nuclear bomb on the Moon [...] "
            "the flash of explosive light would have been faintly visible to people on Earth with their naked eye. "
            "This was meant as a show of force resulting in a possible boosting of domestic morale in the capabilities of the United States, a boost that was needed after the Soviet Union took an early lead in the Space Race. [...] "
            "An identical project by the Soviet Union (Project E-4) also never came to fruition [...] "
            "The existence of the US project was revealed in 2000 by a former executive at the National Aeronautics and Space Administration (NASA), Leonard Reiffel, who had led the project in 1958. [...] "
            "despite Reiffel's revelations, the United States government has never officially acknowledged its involvement in the study. [...] "
            "During the Cold War, the Soviet Union took the lead in the Space Race with the launch of Sputnik 1 on 4 October 1957. [...] "
            "A ten-member team, led by Leonard Reiffel, was assembled at the Illinois Institute of Technology in Chicago to study the potential visibility of the explosion, the benefits to science, and the implications for the lunar surface. "
            "Among the members of the research team were astronomer Gerard Kuiper and his doctoral student Carl Sagan. "
            "Sagan was responsible for the mathematical projection of the expansion of a dust cloud in space around the Moon, an essential element in determining its visibility from Earth. "
            "Scientists initially considered using a hydrogen bomb for the project, but the United States Air Force vetoed that idea due to the weight of such a device, because it would be too heavy to be propelled by the missile which would have been used. "
            "It was then decided to use a W25 warhead, a small, lightweight warhead with a relatively low 1.7 kiloton yield. "
            "By contrast, the Little Boy bomb dropped on the Japanese city of Hiroshima in 1945 had a yield of 13–18 kilotons. "
            "The W25 would be carried by a rocket toward the shadowed side of the Moon where it would detonate on impact. "
            "The dust cloud resulting from the explosion would be lit by the Sun and therefore visible from Earth. [...] "
            "The project was canceled by the Air Force in January 1959, seemingly out of fear of the risk to the population if anything went wrong with the launch. "
            "Another factor, cited by project leader Leonard Reiffel, was the possible problem of nuclear fallout which would affect future lunar research projects and Moon colonization.",
            nome="Project A119")],
    },
    # 5 Starfish Prime: bomba no espaço
    {
        "temas_secundarios": ["exploracao_espacial", "eletromagnetismo", "telecomunicacoes"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "Em 1962, os EUA explodiram uma bomba de hidrogênio a 400 km de altitude, sobre o Pacífico. A 1.450 km dali, no Havaí, o pulso eletromagnético apagou uns 300 postes, e a radiação liberada inutilizou satélites.",
        "explicacao": (
            "O teste Starfish Prime subiu num foguete Thor lançado do atol Johnston em 9 de julho de 1962 e detonou "
            "com cerca de 1,4 megaton, o maior teste nuclear já feito no espaço. O pulso eletromagnético foi tão "
            "maior que o previsto que jogou boa parte dos instrumentos para fora da escala. No Havaí, além de apagar "
            "postes, disparou vários alarmes antifurto e danificou um link de micro-ondas da companhia telefônica, o "
            "que cortou as ligações da ilha de Kauai para as outras ilhas. No céu, auroras artificiais iluminaram "
            "uma área enorme do Pacífico, perto da explosão e também do outro lado do equador. Segundo um veterano "
            "dos testes, alguns hotéis havaianos promoveram festas no terraço para ver a \"bomba arco-íris\". O "
            "efeito mais duradouro veio dos elétrons de alta energia: parte deles ficou presa no campo magnético e "
            "formou cinturões de radiação em volta da Terra. Nos meses seguintes, esses cinturões artificiais "
            "fizeram falhar seis ou mais satélites, cujos painéis solares ou circuitos foram danificados pela "
            "radiação. Entre eles estavam o Telstar 1, primeiro satélite comercial de retransmissão de comunicações, "
            "e o Ariel 1, primeiro satélite do Reino Unido. Um ano depois do teste, EUA e URSS assinaram o tratado "
            "que proibiu testes nucleares acima do solo."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Starfish_Prime",
            "It was launched from Johnston Atoll on July 9, 1962, and was the largest nuclear test conducted in outer space [...] "
            "A Thor rocket carrying a W49 thermonuclear warhead [...] "
            "The explosion took place at an altitude of 250 miles (400 km) [...] "
            "It had a yield of 1.4 Mt [...] "
            "Starfish Prime caused an electromagnetic pulse (EMP) that was far larger than expected, so much larger that it drove much of the instrumentation off scale [...] "
            "causing electrical damage in Hawaii, about 900 miles (1,450 km) away from the detonation point, knocking out about 300 streetlights, setting off numerous burglar alarms, and damaging a telephone company microwave link. "
            "The EMP damage to the microwave link shut down telephone calls from Kauai to the other Hawaiian Islands. [...] "
            "bright auroras were observed in the detonation area, as well as in the southern conjugate region on the other side of the equator from the detonation. [...] "
            "a very large area of the Pacific was illuminated by the auroral phenomena [...] "
            "According to U.S. atomic veteran Cecil R. Coale, some hotels in Hawaii offered \"rainbow bomb\" parties on their roofs for Starfish Prime [...] "
            "other high-energy electrons became trapped and formed radiation belts around the Earth. [...] "
            "In the months that followed, these man-made radiation belts eventually caused six or more satellites to fail, as radiation damaged their solar arrays or electronics, including the first commercial relay communication satellite, Telstar 1, as well as the United Kingdom's first satellite, Ariel 1. [...] "
            "A year after the test, in 1963, the US and USSR signed the Partial Nuclear Test Ban Treaty, which banned all above-ground nuclear testing.",
            nome="Starfish Prime")],
    },
    # 6 bombas atômicas para obras e para apagar incêndios
    {
        "temas_secundarios": ["grandes_obras", "energia"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Na Guerra Fria, EUA e URSS buscaram usos pacíficos para bombas atômicas. Os EUA estudaram abrir com 22 explosões o caminho de uma rodovia na Califórnia. A URSS chegou a usá-las para apagar poços de gás em chamas.",
        "explicacao": (
            "O programa americano, organizado em 1957, se chamava Plowshare, \"relha de arado\", na ideia de "
            "transformar a espada atômica em arado. Ao todo, detonou 35 ogivas em 27 testes. O presidente da "
            "Comissão de Energia Atômica disse com todas as letras que um dos objetivos era criar uma opinião pública "
            "mundial mais favorável ao desenvolvimento e aos testes de armas. As propostas incluíam alargar o Canal "
            "do Panamá, abrir um canal ao nível do mar pela Nicarágua e, no Projeto Carryall, de 1963, cortar as "
            "montanhas Bristol, no deserto de Mojave, com 22 explosões nucleares, para dar passagem à rodovia "
            "Interstate 40 e a uma ferrovia. Um memorando de 1963 chegou a prever 520 explosões de 2 megatons para "
            "abrir no deserto do Negev, em Israel, uma alternativa ao Canal de Suez. A oposição pública, alimentada "
            "pelos efeitos negativos dos testes, levou ao fim do programa em 1977. A União Soviética teve um "
            "programa bem mais intenso, com explosões para procurar gás pelo eco das ondas sísmicas, estimular poços "
            "de petróleo e gás e criar reservatórios subterrâneos. Cinco delas serviram para apagar grandes jorros de "
            "gás em chamas. Em 1966, por exemplo, uma explosão de 30 quilotons fechou no Uzbequistão um poço de gás "
            "que jorrava sem controle desde 1963."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Operation_Plowshare",
                "Project Plowshare was the overall United States program for the development of techniques to use nuclear explosives and large non-nuclear explosions for peaceful construction purposes. "
                "The program was organized in June 1957 as part of the worldwide Atoms for Peace efforts. "
                "As part of the program, 35 nuclear warheads were detonated in 27 separate tests. [...] "
                "Negative impacts from Project Plowshare's tests generated significant public opposition, which eventually led to the program's termination in 1977. [...] "
                "announced that the Plowshares project was intended to \"highlight the peaceful applications of nuclear explosive devices and thereby create a climate of world opinion that is more favorable to weapons development and tests\". "
                "These tests were to demonstrate that atomic bombs can be used for peaceful purposes, that the atomic sword could be beaten into a plowshare. [...] "
                "Proposed uses for nuclear explosives under Project Plowshare included widening the Panama Canal, constructing a new sea-level waterway through Nicaragua nicknamed the Pan-Atomic Canal [...] "
                "Project Carryall, proposed in 1963 by the Atomic Energy Commission, the California Division of Highways (now Caltrans), and the Santa Fe Railway, would have used 22 nuclear explosions to excavate a massive roadcut through the Bristol Mountains in the Mojave Desert, to accommodate construction of Interstate 40 and a new rail line. "
                "A project proposed in a 1963 memorandum by Lawrence Livermore National Laboratory would have used 520 2-megaton nuclear explosions to excavate a canal through the Negev Desert in Israel [...] "
                "to serve as an alternative route to the Suez Canal.",
                nome="Project Plowshare"),
            wiki("Nuclear_Explosions_for_the_National_Economy",
                "Once underway the Soviets conducted a much more vigorous program than the Americans' Operation Plowshare [...] "
                "39 explosions for geological exploration (trying to find new natural gas deposits by studying seismic waves produced by small nuclear explosions) "
                "25 explosions to intensify oil and gas debits "
                "22 explosions to create underground storage for natural gas "
                "5 explosions to extinguish large natural gas fountains that were burning [...] "
                "For example, one 30-kiloton explosion was used to close the Uzbekistan Urtabulak gas well in 1966 that had been blowing since 1963",
                nome="Nuclear Explosions for the National Economy"),
        ],
    },
    # 7 o gato-espião da CIA
    {
        "temas_secundarios": ["espionagem", "comportamento_animal"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Nos anos 1960, a CIA implantou um microfone e um transmissor num gato para espionar soviéticos. Conta-se que ele foi atropelado por um táxi na estreia. Um ex-dirigente da agência contestou: o gato viveu muito e feliz.",
        "explicacao": (
            "O projeto Acoustic Kitty, da diretoria de ciência e tecnologia da CIA, pretendia usar gatos para "
            "espionar o Kremlin e embaixadas soviéticas. Numa cirurgia de uma hora, um veterinário pôs um microfone "
            "no canal do ouvido do animal, um pequeno transmissor de rádio na base do crânio e um fio fino entre os "
            "pelos. Como o gato se distraía, foi preciso outra operação para lidar com a fome dele. Segundo Victor "
            "Marchetti, ex-funcionário da CIA, o projeto custou cerca de 20 milhões de dólares, e na primeira "
            "missão, escutar dois homens num parque em frente à embaixada soviética em Washington, o gato foi solto "
            "ali perto e atropelado por um táxi quase na hora. Em 2013, Robert Wallace, que dirigiu o escritório de "
            "serviços técnicos da agência, deu outra versão: o projeto foi abandonado pela dificuldade de treinar o "
            "gato, o equipamento foi retirado, o animal foi costurado de novo e viveu \"uma vida longa e feliz\". O "
            "memorando de encerramento, de 1967, dizia que era possível treinar gatos para percorrer distâncias "
            "curtas, mas que, numa situação real no exterior, a técnica não seria prática. O caso veio a público em "
            "2001, com a liberação de documentos da CIA."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Acoustic_Kitty",
            "Acoustic Kitty was a Central Intelligence Agency (CIA) project launched by the Directorate of Science & Technology in the 1960s, which was intended to use cats to spy on the Kremlin and Soviet embassies. [...] "
            "In an hour-long procedure, a veterinary surgeon implanted a microphone in the cat's ear canal, a small radio transmitter at the base of its skull, and a thin wire into its fur. [...] "
            "Due to problems with distraction, the cat's sense of hunger had to be addressed in another operation. "
            "Victor Marchetti, a former CIA officer, said Project Acoustic Kitty cost about $20 million. "
            "The first Acoustic Kitty mission was to eavesdrop on two men in a park outside the Soviet embassy in Washington, D.C. "
            "According to Marchetti, the cat was released nearby, but was hit and allegedly killed by a taxi almost immediately. "
            "However, this was disputed in 2013 by Robert Wallace, a former director of the Office of Technical Service, who said that the project was abandoned due to the difficulty of training the cat to behave as required, and "
            "\"the equipment was taken out of the cat; the cat was re-sewn for a second time, and lived a long and happy life afterwards\". [...] "
            "The project was cancelled in 1967. "
            "A closing memorandum said that the CIA researchers believed that they could train cats to move short distances, but that \"the environmental and security factors in using this technique in a real foreign situation force us to conclude that for our (intelligence) purposes, it would not be practical.\" "
            "The project was disclosed in 2001, when some CIA documents were declassified.",
            nome="Acoustic Kitty")],
    },
    # 8 o túnel de Berlim que os soviéticos conheciam
    {
        "temas_secundarios": ["espionagem", "telecomunicacoes"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Nos anos 1950, a CIA e o serviço secreto britânico cavaram um túnel de 450 m até a zona soviética de Berlim para grampear cabos militares. Os soviéticos sabiam de tudo desde o início, por um espião, e deixaram.",
        "explicacao": (
            "A Operação Gold surgiu porque o Exército Vermelho tinha trocado o rádio por linhas telefônicas nas "
            "comunicações mais seguras. Os americanos financiaram e cavaram o túnel, e os britânicos, que já tinham "
            "feito algo parecido em Viena, cuidaram de grampear os cabos. A escavação começou em setembro de 1954, a "
            "partir de um falso armazém no setor americano, sob a fronteira mais vigiada do mundo, até cabos que "
            "ficavam a menos de meio metro de uma rua movimentada. Durante quase um ano, foram gravadas cerca de 90 "
            "mil comunicações. Só que George Blake, espião soviético infiltrado na inteligência britânica, esteve "
            "nas primeiras reuniões e avisou a KGB. Para não expor um agente tão valioso, os soviéticos preferiram "
            "sacrificar parte de seus segredos. A KGB não avisou ninguém na Alemanha, nem os militares soviéticos que "
            "usavam os cabos, e estes continuaram passando por ali informações de valor. Segundo um relatório da CIA, "
            "não houve tentativa conhecida de plantar desinformação. O túnel só foi \"descoberto\" em 21 de abril "
            "de 1956. Orçada em 50 mil dólares, a obra passou de 6,5 milhões."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Operation_Gold",
            "(SIS) in the 1950s to tap into landline communication of the Soviet Army headquarters in Berlin using a tunnel into the Soviet-occupied zone. [...] "
            "Construction of the tunnel began in September 1954 and was completed in eight months. "
            "The Americans wanted to hear any warlike intentions being discussed by their military and were able to listen to telephone conversations for nearly a year, eventually recording roughly 90,000 communications. "
            "The Soviet authorities were informed about Operation Gold from the very beginning by their  mole George Blake but decided not to \"discover\" the tunnel until April 21, 1956, in order to protect Blake from exposure. [...] "
            "After the Red Army followed the Soviet diplomatic department and transferred its most secure communications from radio to telephone landlines [...] "
            "The resulting agreement was that the US would supply most of the financing and construct the tunnel (as the closest access point was in their sector), while the British would use their expertise from Operation Silver to tap the cables [...] "
            "One of those who attended the early meetings was George Blake, a mole in the British intelligence apparatus. Blake apparently alerted the KGB immediately [...] "
            "The KGB decided to let Operation Gold proceed since, in order to attack the tunnel, the Soviets would have to compromise Blake, and they found it preferable to sacrifice some information rather than their valuable agent. [...] "
            "The KGB did not inform anyone in Germany, including the East Germans or the Soviet users of the cables, about the taps. "
            "According to a CIA report, \"there were no known attempts to feed disinformation to the CIA.\" "
            "Although the British SIS suspected the opposite, the CIA report states that \"the Soviet military continued to use the cables for communications of intelligence value.\" [...] "
            "The first project was the construction of a \"warehouse\", which acted as a disguise [...] "
            "The covert construction of the 450-meter (1,476 ft) tunnel under the world's most heavily patrolled border to intersect a series of cables less than 47 centimeters (19 in.) below a busy street was an exceptional engineering challenge. [...] "
            "From 1948 onwards, under Operation Silver, the British SIS had undertaken a number of such operations in then still occupied-Vienna [...] "
            "Originally costed at $50,000, the final cost of the completed tunnel was over US$6.5M",
            nome="Operation Gold")],
    },
    # 9 Schabowski e o "imediatamente"
    {
        "temas_secundarios": ["revolucoes_politicas", "fronteiras_paises"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1989, o porta-voz da Alemanha Oriental leu numa coletiva as novas regras de viagem e, perguntado quando valiam, improvisou: \"imediatamente\". O texto só devia sair no dia seguinte. Naquela noite, o Muro se abriu.",
        "explicacao": (
            "Em 9 de novembro de 1989, pouco antes da entrevista coletiva do dia, o líder Egon Krenz entregou a "
            "Günter Schabowski um texto com regras provisórias: os alemães-orientais poderiam pedir para viajar ao "
            "exterior sem as exigências de antes e emigrar por qualquer posto de fronteira, inclusive entre Berlim "
            "Oriental e Ocidental. O texto estava sob embargo até a manhã seguinte. Schabowski não estava presente "
            "quando o assunto foi discutido, mas se sentiu à vontade: mais tarde, disse que para conduzir uma "
            "coletiva bastava falar alemão e ler um texto sem errar. Leu a nota no fim da entrevista. Um repórter "
            "perguntou quando as regras entrariam em vigor. Schabowski deduziu pelo texto que seria no mesmo dia e, "
            "depois de alguns segundos, respondeu: \"Até onde sei... imediatamente, sem demora\". Até hoje há "
            "versões diferentes sobre quem fez a pergunta: dois jornalistas sentados na primeira fila dizem ter sido "
            "eles. Naquela mesma noite, multidões foram até o Muro e forçaram a abertura, depois de 28 anos. Logo "
            "toda a fronteira entre as duas Alemanhas foi aberta, e pouco depois a Alemanha Oriental deixou de existir."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("G%C3%BCnter_Schabowski",
            "He gained worldwide fame in November 1989 when he improvised a slightly mistaken answer to a press conference question about the future of the Berlin Wall, that seemed to announce the Wall's immediate end [...] "
            "Massive crowds gathered at the Wall the same night, which forced its opening after 28 years. "
            "Soon afterward, the entire inner German border was opened; not much later, East Germany ceased to exist. [...] "
            "On 9 November 1989, shortly before that day's press conference, Krenz handed Schabowski a text containing new, temporary travel regulations. "
            "The text stipulated that East German citizens could apply for permission to travel abroad without having to meet the previous requirements for those trips, and it allowed for permanent emigration across all border crossings, including those between East and West Berlin. "
            "The text was supposed to be embargoed until the next morning. "
            "Schabowski had not been on hand when Krenz read the text earlier in the day to several Politbüro members [...] "
            "However, he felt comfortable discussing it at the press conference; he said later that all one needed to do to conduct a press conference was to be able to speak German and read a text without mistakes. "
            "Accordingly, he read the note aloud at the end of the press conference. "
            "One of the reporters asked when the regulations would come into effect. "
            "Schabowski assumed that it would be the same day based on the wording of the note, and he replied after a few seconds' pause: \"As far as I know... effective immediately, without delay.\" [...] "
            "Accounts differ on who asked that question. "
            "Both Riccardo Ehrman, the Berlin correspondent of the ANSA news agency, and the German Bild Zeitung (a tabloid) reporter Peter Brinkmann were sitting in the front row at the press conference and claimed to have asked when the regulations would come into force.",
            nome="Günter Schabowski")],
    },
    # 10 o código 00000000 dos Minuteman
    {
        "temas_secundarios": ["falhas_engenharia"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Segundo um especialista em segurança nuclear, o código que destravava os mísseis nucleares Minuteman dos EUA ficou anos em 00000000, para não faltar numa emergência. A Força Aérea nega que ele tenha habilitado míssil.",
        "explicacao": (
            "Armas nucleares americanas ganharam travas chamadas permissive action links, que impedem armar ou lançar "
            "a arma sem a inserção de um código ou combinação. As primeiras eram simples cadeados mecânicos de "
            "combinação, instalados em sistemas como o do míssil Minuteman. Segundo Bruce Blair, especialista em "
            "segurança nuclear, o Comando Aéreo Estratégico temia que, na hora da necessidade, os códigos dos "
            "Minuteman não estivessem disponíveis. Por isso, decidiu fixar a combinação em 00000000 em todos os "
            "centros de controle de lançamento. Blair disse ainda que as listas de verificação dos lançamentos "
            "traziam um item para confirmar essa combinação, até 1977. Num artigo de 2014, a revista Foreign Policy "
            "relatou que a Força Aérea declarou a uma comissão da Câmara dos EUA que um código de oito zeros nunca "
            "foi usado para habilitar um Minuteman. As duas versões não chegam a se contradizer: a Força Aérea fala "
            "de mísseis que nunca foram de fato disparados; Blair, de qual era o código. Os mísseis contam com "
            "outras salvaguardas: os dois operadores precisam conferir a ordem com um código lacrado num cofre de "
            "duas fechaduras, girar juntos as chaves de lançamento, e outra equipe, num segundo centro de controle, "
            "precisa fazer o mesmo."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Permissive_action_link",
            "A permissive action link (PAL) is an access control security device for nuclear weapons. "
            "Its purpose is to prevent unauthorized arming or detonation of a nuclear weapon. [...] "
            "A device included in or attached to a nuclear weapon system to preclude arming and/or launching until the insertion of a prescribed discrete code or combination. [...] "
            "The precursors of permissive action links were simple mechanical combination locks that were set into the control systems of nuclear weapons, such as the Minuteman ICBM. [...] "
            "According to nuclear safety expert Bruce G. Blair, the US Air Force's Strategic Air Command worried that in times of need the codes for the Minuteman ICBM force would not be available, so it decided to set the codes to 00000000 in all missile launch control centers. "
            "Blair said the missile launch checklists included an item confirming this combination until 1977. "
            "A 2014 article in Foreign Policy said that the US Air Force told the United States House Committee on Armed Services that \"A code consisting of eight zeroes has never been used to enable a MM ICBM, as claimed by Dr. Bruce Blair.\" "
            "The Air Force's statement (that 00000000 was never used to enable an ICBM, i.e. the weapons were not actually launched) does not contradict Blair's statement (that 00000000 was the code for doing so). [...] "
            "In the case of Minuteman missile launch crews, both operators must agree that the launch order is valid by comparing the order's authorization code against a code from a \"sealed authenticator\" [...] "
            "The sealed authenticators are stored in a safe that has two separate locks so that a single crew member cannot open the safe alone. "
            "Both crew members must simultaneously turn the four launch keys. "
            "An additional safeguard is provided by requiring the crew in another launch control center to do the same for the missiles to be launched.",
            nome="Permissive action link")],
    },
    # 11 a "marinha" da Pepsi
    {
        "temas_secundarios": ["economia_curiosa", "dinheiro"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Em 1989, a PepsiCo recebeu da URSS 17 submarinos desativados, uma fragata, um cruzador e um destróier em troca de refrigerante. Mas a fama de que a Pepsi teve uma das marinhas mais fortes do mundo é exagero.",
        "explicacao": (
            "Em 1959, numa exposição americana em Moscou, a PepsiCo conseguiu uma foto do vice-presidente Richard "
            "Nixon e do líder soviético Nikita Khrushchev bebendo Pepsi. Em 1972, a empresa negociou o monopólio dos "
            "refrigerantes de cola na URSS, e a Pepsi se tornou o primeiro produto de consumo americano produzido e "
            "vendido no país. Como os soviéticos restringiam a saída de rublos, o negócio era de troca: xarope de "
            "Pepsi em troca de vodca Stolichnaya, vendida no Ocidente. Em 1989, com as vendas da vodca em queda, a "
            "PepsiCo aceitou outra moeda: dois petroleiros novos, 17 submarinos desativados, a 150 mil dólares cada, "
            "uma fragata, um cruzador e um destróier, que ela poderia revender por moeda forte. Os petroleiros foram "
            "arrendados por meio de uma empresa norueguesa, e os navios de guerra foram logo vendidos como sucata. Um "
            "acordo do ano seguinte previa 85 navios em dez anos, mas só dez chegaram antes do fim da URSS, em 1991. "
            "Desses negócios nasceu a lenda de que a PepsiCo teve, por um tempo, uma das marinhas mais poderosas do "
            "mundo. Na verdade, os únicos navios de guerra que ela recebeu eram embarcações pequenas, velhas, "
            "obsoletas e sem condições de navegar."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("PepsiCo",
            "In 1959, the USSR held an exhibition of Soviet technology and culture in New York. "
            "The United States reciprocated with an exhibition in Sokolniki Park, Moscow, which led to the famous kitchen debate. "
            "One of the American products exhibited was Pepsi Cola. "
            "After obtaining a photo of then–US vice president Richard Nixon and Soviet premier Nikita Khrushchev sipping Pepsi, PepsiCo executive Donald Kendall was able to capture the attention of the Soviet people, and in 1972 he negotiated a cola monopoly in the USSR and Pepsi became the first US consumer product to be produced and marketed in the Soviet Union. "
            "Due to Soviet restrictions on transporting roubles abroad, PepsiCo struck a barter deal whereby Stolichnaya vodka would be exchanged for Pepsi syrup. "
            "In 1989, amidst declining vodka sales, PepsiCo bartered for 2 new Soviet oil tankers, 17 decommissioned submarines (for $150,000 each), a frigate, a cruiser and a destroyer, which they could in turn sell for non-Soviet currency. "
            "The oil tankers were leased out through a Norwegian company, while the other ships were immediately sold for scrap. "
            "A deal struck the following year would've seen Pepsi acquire 85 ships worth nearly $3 billion over the next 10 years, but it only acquired 10 additional ships before the fall of the Soviet Union in 1991. [...] "
            "These deals also originated an erroneous factoid which claims that, after acquiring the Soviet fleet, PepsiCo briefly possessed one of the most powerful navies in the world. "
            "In actuality, the only warships acquired by PepsiCo were \"small, old, obsolete, unseaworthy vessels\".",
            nome="PepsiCo")],
    },
    # 12 Goldsboro: a bomba que quase explodiu
    {
        "temas_secundarios": ["falhas_engenharia"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Em 1961, um B-52 se partiu no ar sobre a Carolina do Norte e soltou duas bombas de hidrogênio. Numa delas, segundo engenheiros, só um interruptor de baixa voltagem evitou a explosão. Parte da outra segue enterrada lá.",
        "explicacao": (
            "O bombardeiro, numa missão de alerta aéreo, levava duas bombas Mark 39 de 3,8 megatons cada. Em 24 de "
            "janeiro de 1961, um vazamento de combustível na asa o obrigou a voltar à base, e na descida os pilotos "
            "perderam o controle. Ao se soltarem do avião, as duas bombas iniciaram a sequência de disparo, apesar "
            "das travas que deviam impedir isso. Na primeira, o paraquedas abriu e tudo se passou quase como num "
            "lançamento intencional. Só não houve detonação porque o interruptor de armar ficou em \"seguro\". Em "
            "1969, um supervisor do laboratório Sandia escreveu que \"um simples interruptor de baixa voltagem\" "
            "separou os EUA de uma grande catástrofe. A segunda bomba caiu sem paraquedas e se cravou na lama. Ali, "
            "a equipe de desarme achou o interruptor marcando \"armar\", cena que um oficial disse que nunca "
            "esqueceria. A análise mostrou, porém, que o indicador tinha girado com o impacto, sem fazer contato, e "
            "que essa bomba não poderia ter explodido, porque o temporizador não terminara a contagem. Um componente "
            "dela, o estágio termonuclear, foi dado como irrecuperável. Em 1962, o dono do terreno recebeu mil "
            "dólares para ceder aos EUA, para sempre, um círculo de 61 metros de raio sobre os restos, onde é "
            "proibido escavar abaixo de cerca de um metro e meio."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("1961_Goldsboro_B-52_crash",
            "occurred near Goldsboro, North Carolina, United States, on 24 January 1961. "
            "A Boeing B-52 Stratofortress carrying two 3.8-megaton Mark 39 nuclear bombs broke up in mid-air, dropping its nuclear payload in the process. [...] "
            "Both of the weapons began their firing sequences upon separation from the aircraft, despite safeguards meant to prevent that from occurring. "
            "One of its nuclear bombs was judged by nuclear weapons engineers at the time to have been only one safety switch away from detonation [...] "
            "The other bomb did not get as far into its firing sequence, but became deeply embedded in a muddy field, and one of its major weapons components (the thermonuclear \"secondary\" stage) was regarded as irrecoverably lost after an extensive, failed effort to recover it. [...] "
            "part of the Strategic Air Command's airborne alert mission [...] "
            "his B-52 had a fuel leak in the right wing. [...] "
            "The aircraft was immediately directed to return and land at Seymour Johnson Air Force Base. "
            "As the aircraft descended through 10,000 feet (3,000 m) on its approach to the airfield, the pilots were no longer able to keep it in stable descent [...] "
            "This switch was found by the initial explosive ordnance disposal (EOD) team on the scene to be in the \"Safe\" position, and did not pass its current on further. [...] "
            "weapon no. 1 \"underwent a normal release sequence in which the parachute opened and the components of the weapon which were given an opportunity to actuate by the pulling of the Bisch rods did behave in the manner expected. "
            "Full operation of this weapon was prevented by the MC-772 Arm/Safe Switch, the primary safing device.\" [...] "
            "Parker F. Jones, a supervisor at Sandia, concluded in a reassessment of the accident in 1969 that \"one simple, dynamo-technology, low voltage switch stood between the United States and a major catastrophe.\" [...] "
            "However, because the weapon had been released at such a low altitude, and its parachute had failed to open, it collided with the ground at high speed. [...] "
            "\"Until my death I will never forget hearing my sergeant say, 'Lieutenant, we found the arm/safe switch.' And I said, 'Great.' He said, 'Not great. It's on arm.'\" [...] "
            "while the switch's indicator drum had rotated to the \"Arm\" position, it had disconnected from its contacts, and was never electrically \"armed.\" "
            "They concluded that this was damage caused by the impact shock of the bomb hitting the ground [...] "
            "For Bomb No. 2, because its timer had not run out by the time it struck the ground, it could not have detonated even if its Arm-Safe Switch had been set to \"Arm\" [...] "
            "In 1962, the landowner was paid $1,000 to grant the United States of America a perpetual 200-foot (61 m) radius circular easement over the remains of the buried second bomb. [...] "
            "No drilling, digging, boring, excavating or other disturbances of the land will be permitted below a depth of five (5) feet.",
            nome="1961 Goldsboro B-52 crash")],
    },
    # 13 a CIA, Fidel e a barba
    {
        "temas_secundarios": ["espionagem", "revolucoes_politicas"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Para desmoralizar Fidel Castro, a CIA planejou pôr sais de tálio nos sapatos dele, para fazer cair a famosa barba. Depois vieram planos para matá-lo: uma comissão do Senado dos EUA confirmou ao menos oito.",
        "explicacao": (
            "Entre março e agosto de 1960, a CIA estudou formas de minar a imagem pública de Castro mexendo no "
            "comportamento e na aparência dele. Uma ideia era borrifar no estúdio de onde ele fazia transmissões um "
            "composto parecido com o LSD, abandonada porque a substância não era confiável. Outra era tratar uma "
            "caixa de charutos dele com uma substância que causava desorientação temporária. O plano do tálio, um "
            "depilatório potente, aproveitaria uma viagem ao exterior: Castro deixaria os sapatos na porta do quarto "
            "do hotel para serem engraxados. Ele cancelou a viagem, e o plano morreu. Vieram depois ideias de "
            "assassinato igualmente estranhas: uma roupa de mergulho contaminada com fungo e com o bacilo da "
            "tuberculose, conchas explosivas, uma caneta com agulha envenenada. Em 1975, a Comissão Church, do "
            "Senado americano, afirmou ter confirmado pelo menos oito complôs da CIA para matar Castro. Fabián "
            "Escalante, encarregado por muito tempo da proteção dele, fala em 638 planos ou tentativas. Já o famoso "
            "charuto explosivo, a trama mais conhecida, é tratado por algumas fontes como mito."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Operation_Mongoose",
            "From March through August 1960, the CIA had plans aimed at undermining Castro and his appeal to the public by sabotaging his speeches. "
            "The schemes thought up were aimed at discrediting Castro by influencing his behavior and by changing his appearance. "
            "One plan discussed was to spray his broadcast studio with a chemical compound similar to LSD. "
            "It was scrapped because the chemical was unreliable. "
            "Another plot was to lace a box of Castro's cigars with a chemical known to cause temporary disorientation. "
            "The CIA's plans to undermine Castro's public image included a plan to line his shoes with thallium salts which would cause his beard to fall out, while he was on a trip outside Cuba. "
            "He was expected to leave his shoes outside his hotel room to be polished, at which point the salts would be administered. "
            "The plan was abandoned because Castro canceled the trip. [...] "
            "The CIA even tried to embarrass Castro by attempting to sneak thallium salts, a potent depilatory, into Castro's shoes [...] "
            "In early 1963, The CIA devised a plot to provide Castro with a diving suit contaminated with fungus and \"contaminating the breathing apparatus with tubercle bacilli\". [...] "
            "Various other methods of assassination that had been thought of by the CIA included exploding seashells, having a former lover slip him poison pills, and exposing him to various other poisoned items such as a fountain pen and even ice cream. [...] "
            "The US Senate's Church Committee of 1975 stated that it had confirmed at least eight separate CIA run plots to assassinate Castro. "
            "Fabian Escalante, who was long tasked with protecting the life of Castro, contends that there have been 638 separate CIA assassination schemes or attempts on Castro's life. "
            "Many assassination ideas were floated by the CIA during Operation Mongoose. "
            "The most infamous was the CIA's alleged plot to capitalize on Castro's well-known love of cigars by slipping into his supply a very real and lethal \"exploding cigar.\" "
            "While numerous sources state the exploding cigar plot as fact, at least one source asserts it to be simply a myth",
            nome="Operation Mongoose")],
    },
    # 14 Projeto Azorian e a "resposta Glomar"
    {
        "temas_secundarios": ["espionagem", "oceanografia"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "A resposta \"não podemos confirmar nem negar\" ganhou nome numa operação da CIA: em 1974, um navio disfarçado de mineradora do bilionário Howard Hughes içou do fundo do Pacífico parte de um submarino soviético.",
        "explicacao": (
            "O submarino K-129, armado com mísseis nucleares, afundou em 1968 a cerca de 2.510 km a noroeste do "
            "Havaí. A URSS não conseguiu localizá-lo, mas os EUA acharam a área por um evento acústico registrado "
            "por seus sensores. Os destroços estavam a mais de 4.900 metros de profundidade, muito além de qualquer "
            "resgate de navio já tentado. A CIA pagou a construção do Hughes Glomar Explorer, equipado com uma garra "
            "gigante, e criou uma fachada: o navio, que levava o nome de Hughes, estaria minerando nódulos de "
            "manganês no leito oceânico. Hughes emprestou o nome, mas nem ele nem suas empresas participaram da "
            "operação. O Projeto Azorian custou cerca de 800 milhões de dólares da época. Na subida, garras se "
            "partiram e a maior parte da seção içada voltou ao fundo. Segundo testemunhas, só a proa, de 12 metros, "
            "chegou ao navio, com dois torpedos nucleares e os corpos de seis tripulantes, sepultados no mar com "
            "honras militares. Mais tarde, uma jornalista pediu à CIA, pela lei de acesso à informação, documentos "
            "sobre as tentativas da agência de impedir a publicação de reportagens sobre o caso. A CIA se recusou a "
            "confirmar ou negar que eles existissem. Esse tipo de resposta passou a ser chamado de \"resposta "
            "Glomar\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Project_Azorian",
            "Project Azorian (also called \"Jennifer\" by the press after its Top Secret Security Compartment) was a U.S. Central Intelligence Agency (CIA) project to recover the sunken Soviet submarine K-129 from the Pacific Ocean floor in 1974 using the purpose-built ship Hughes Glomar Explorer. "
            "The 1968 sinking of K-129 occurred about 1,560 miles (2,510 km) northwest of Hawaii. "
            "Project Azorian was one of the most complex, expensive, and covert intelligence operations of the Cold War at a cost of about US$800 million [...] "
            "The Soviet Union was unable to locate K-129, but the US determined its general location from data recorded by four Air Force Technical Applications Center (AFTAC) sites and the Adak Sound Surveillance System (SOSUS) array. "
            "The US identified an acoustic event on March 8 that likely originated from an explosion aboard the submarine [...] "
            "The recovery operation in international waters about six years later used mining for manganese nodules as its cover story. "
            "The mining company and ship were nominally owned by reclusive billionaire Howard Hughes, but secretly backed by the CIA, who paid for the construction of the Hughes Glomar Explorer. [...] "
            "a Soviet Project 629A ballistic missile submarine [...] "
            "agreed to lend his name to the project to support the cover story that the ship was mining manganese nodules from the ocean floor, but Hughes and his companies had no actual involvement in the project. "
            "K-129 was photographed at a depth of over 16,000 feet (4,900 m), and thus the salvage operation would be well beyond the depth of any ship salvage operation ever attempted. [...] "
            "Hughes Glomar Explorer employed a large mechanical claw [...] "
            "Video evidence and eyewitness reports have stated that multiple claws of Clementine sheared off, causing  a 100-foot (30 m) section of the submarine to fall back to the seafloor. "
            "Eyewitnesses have stated that only the 38-foot (12 m) bow section was raised [...] "
            "The recovered section included two nuclear torpedoes [...] "
            "The bodies of six crewmen were also recovered, and were given a memorial service and with military honors, buried at sea in a metal casket because of radioactivity concerns. [...] "
            "After stories had been published about the CIA's attempts to stop publication of information about Project Azorian, Harriet Ann Phillippi, a journalist, filed a Freedom of Information Act (FOIA) request with the CIA for any records about the CIA's attempts. "
            "The CIA refused to either confirm or deny the existence of such documents. "
            "This type of non-responsive reply has since come to be known as the \"Glomar response\" or \"Glomarization\".",
            nome="Project Azorian")],
    },
    # 15 Palomares: o pescador e a bomba
    {
        "temas_secundarios": ["probabilidade", "oceanografia"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 1966, uma bomba de hidrogênio americana caiu no mar da Espanha. Um pescador que a viu afundar ajudou a guiar a busca, que usou cálculo de probabilidades. Achada a bomba, ele foi à Justiça dos EUA pedir recompensa.",
        "explicacao": (
            "Em 17 de janeiro de 1966, um bombardeiro B-52 colidiu com o avião-tanque que o reabastecia sobre o "
            "Mediterrâneo, perto da vila de Palomares. Levava quatro bombas termonucleares. Três caíram em terra; em "
            "duas, o explosivo convencional detonou com o impacto, sem explosão nuclear, e espalhou plutônio por "
            "cerca de 2 km². A quarta afundou no mar. A busca usou um método matemático então novo, a teoria "
            "bayesiana de busca, liderada por John Craven: cada quadrado do mapa recebe uma probabilidade, "
            "atualizada à medida que a procura avança. As probabilidades iniciais aproveitaram o relato do pescador "
            "Francisco Simó Orts, que viu a bomba entrar na água e foi contratado pela Força Aérea para ajudar. Ele "
            "ficou conhecido como \"Paco el de la bomba\". Depois de 80 dias, o submersível Alvin encontrou a bomba. "
            "Simó Orts então foi a um tribunal federal em Nova York reivindicar direitos de salvamento. Segundo "
            "Craven, pelo costume do direito marítimo, quem localiza o que é resgatado ganha um percentual do valor, "
            "e o secretário de Defesa avaliara a bomba em 2 bilhões de dólares: cada ponto percentual valeria 20 milhões. A Força "
            "Aérea fez um acordo fora dos tribunais, por valor não divulgado. Anos depois, o pescador reclamava que "
            "os americanos não cumpriram a promessa de compensação."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Palomares_incident",
            "The Palomares accident occurred on 17 January 1966, when a United States Air Force B-52G bomber collided with a KC-135 tanker during mid-air refueling at 31,000 feet (9,450 m) over the Mediterranean Sea, near the Spanish village of Palomares in Almería province. [...] "
            "At the time of the accident, the B-52G was carrying four B28FI Mod 2 Y1 thermonuclear bombs. "
            "Three of these bombs fell on land near Palomares; the conventional explosives in two detonated upon impact (there was no nuclear explosion triggered), dispersing plutonium and contaminating approximately 2 square kilometers (0.77 sq mi) of terrain. "
            "The fourth bomb fell into the Mediterranean Sea and was recovered intact after an extensive 80-day search involving the U.S. Navy, including the use of submersibles such as DSV Alvin. [...] "
            "Dr. John P. Craven [...] "
            "The search for the fourth bomb was carried out by means of a novel mathematical method, Bayesian search theory, led by Craven. "
            "This method assigns probabilities to individual map grid squares, then updates these as the search progresses. "
            "Initial probability input is required for the grid squares, and these probabilities made use of the fact that a local fisherman, Francisco Simó Orts, popularly known since as \"Paco el de la bomba\" (\"Bomb Paco\" or \"Bomb Frankie\"), witnessed the bomb entering the water at a certain location. "
            "Simó Orts was hired by the U.S. Air Force to assist in the search operation. [...] "
            "the bomb was located by the DSV Alvin on 17 March [...] "
            "Once the bomb was located, Simó Orts appeared at the United States District Court for the Southern District of New York with his lawyer, Herbert Brownell, formerly Attorney General of the United States under President Dwight D. Eisenhower, claiming salvage rights on the recovered thermonuclear bomb. "
            "According to Craven: [...] "
            "It is customary maritime law that the person who identifies the location of a ship to be salved has the right to a salvage award if that identification leads to a successful recovery. [...] "
            "But the thing salved off Palomares was a thermonuclear bomb, the same bomb valued by no less an authority than the Secretary of Defense at $2 billion—each percent of which is, of course, $20 million. "
            "The Air Force settled out of court for an undisclosed sum. "
            "In later years, Simó Orts was heard to complain that the Americans had promised him financial compensation but had not kept their promise.",
            nome="Palomares incident")],
    },
]
