LOTE = "2026-11-19-segunda_guerra-01"
AREA = "historia_moderna"
TEMA = "segunda_guerra"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 os balões de papel japoneses e a areia do lastro
    {
        "temas_secundarios": ["atmosfera", "minerais_rochas"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "O Japão lançou uns 9.300 balões de papel com bombas para cruzar o Pacífico na corrente de jato. Para descobrir de onde vinham, geólogos dos EUA estudaram os minerais e as diatomáceas da areia do lastro.",
        "explicacao": (
            "Entre novembro de 1944 e abril de 1945, o Exército japonês soltou os balões da costa de Honshu, "
            "confiando nos ventos fortes de grande altitude que hoje chamamos de corrente de jato. O invólucro era "
            "de washi, um papel resistente, em camadas coladas com pasta de konnyaku; milhares de adolescentes de "
            "escolas foram mobilizadas para montá-lo, e os testes finais ocorriam em grandes salões, como o ginásio "
            "de sumô Ryōgoku Kokugikan, em Tóquio. Para manter a altitude, o balão largava aos poucos sacos de "
            "areia. Uns 300 foram achados ou avistados nos EUA, no Canadá e no México. A areia virou pista: a "
            "Unidade de Geologia Militar do Serviço Geológico dos EUA analisou sua composição e apontou duas "
            "praias prováveis, das quais só a considerada menos provável estava certa. Enquanto isso, a censura "
            "pediu à imprensa silêncio total, e o Japão não soube do resultado. A única tragédia veio em 5 de maio "
            "de 1945, perto de Bly, no Oregon: num piquenique, a esposa grávida de um pastor e cinco crianças da "
            "escola dominical acharam um balão caído, e os seis morreram na explosão. Foram as únicas mortes por "
            "ação inimiga no território continental dos EUA durante a guerra. O silêncio da imprensa acabou em 22 "
            "de maio, para que o público fosse alertado."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Fu-Go_balloon_bomb",
            "The uncontrolled balloons were carried over the Pacific Ocean from Japan to North America by fast, high-altitude air currents, today known as the jet stream, and used a sophisticated sandbag ballast system to maintain their altitude. [...] "
            "Between November 1944 and April 1945, the Imperial Japanese Army launched about 9,300 balloons from sites on coastal Honshu, of which about 300 were found or observed in the U.S., Canada, and Mexico. [...] "
            "A U.S. media censorship campaign prevented the Imperial Army from learning of the offensive's results. [...] "
            "The balloons were constructed from four to five thin layers of washi, a durable paper derived from the paper mulberry (kōzo) bush, which were glued together with konnyaku (Japanese potato) paste. "
            "The Army mobilized thousands of teenage girls at high schools across the country to laminate and glue the sheets together, with final assembly and inflation tests at large indoor arenas including the Nichigeki Music Hall and Ryōgoku Kokugikan sumo hall in Tokyo. [...] "
            "The mineral and diatom composition of sand from the sandbags was studied by the Military Geology Unit of the United States Geological Survey, which assessed its origin as Shiogama, Miyagi, or less likely, Ichinomiya, Chiba, only the latter being correct. [...] "
            "On January 4, 1945, the U.S. Office of Censorship sent a confidential memo to newspaper editors and radio broadcasters asking that they give no publicity to balloon incidents [...] "
            "On May 5, 1945, six civilians were killed near Bly, Oregon, when they discovered one of the balloon bombs in Fremont National Forest, becoming the only fatalities from Axis action in the continental U.S. during the war. "
            "Reverend Archie Mitchell and his pregnant wife Elsie (age 26) drove up Gearhart Mountain that day with five of their Sunday school students for a picnic. [...] "
            "The U.S. press blackout was lifted on May 22 so the public could be warned of the balloon threat.",
            nome="Fu-Go balloon bomb")],
    },
    # 2 o Exército Fantasma
    {
        "temas_secundarios": ["pintura", "acustica"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Uma unidade americana de 1.100 homens enganou os alemães com tanques infláveis, sons de tropas gravados e rádio falso. Muitos eram artistas, como Ellsworth Kelly, e a história ficou em segredo até 1996.",
        "explicacao": (
            "O Exército Fantasma, nome oficial 23rd Headquarters Special Troops, foi ativado em janeiro de 1944 e "
            "chegou à Europa pouco antes do Dia D. Sua missão era confundir o inimigo sobre o tamanho e a posição "
            "das forças aliadas, e ele montou mais de 20 operações de engano até o fim da guerra. Uma parte da "
            "unidade enchia com compressores tanques, canhões, jipes e aviões de borracha e os camuflava mal de "
            "propósito, para que o reconhecimento aéreo alemão os visse. Em poucas horas, erguia aeródromos e "
            "acampamentos falsos, com roupa estendida no varal. Outra parte cuidava do som: com engenheiros dos "
            "Bell Labs, gravou o barulho de unidades blindadas e de infantaria, mixava os efeitos conforme a "
            "encenação e os tocava em alto-falantes potentes, audíveis a 24 km. Muitos soldados vinham de escolas "
            "de arte de Nova York e da Filadélfia, e alguns marcaram a arte americana do pós-guerra, como Ellsworth "
            "Kelly, Bill Blass e Art Kane. A história só foi revelada em 1996, mais de 50 anos depois, e em 2022 "
            "os veteranos receberam a Medalha de Ouro do Congresso."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Ghost_Army",
            "The Ghost Army was a United States Army tactical deception unit during World War II officially known as the 23rd Headquarters Special Troops. "
            "The 1,100-man unit was created to deceive the Axis forces and mislead them as to the size and location of Allied forces, while giving the actual units elsewhere time to maneuver. "
            "Activated on 20 January 1944, the Ghost Army arrived in Europe in May shortly before D-Day and returned to the US at the end of the war in July 1945. "
            "During their tenure, the Ghost Army carried out more than 20 deception campaigns, putting on a \"traveling road show\" using inflatable tanks, sound trucks, fake radio transmissions, scripts and pretense. "
            "Their story was kept a secret for more than 50 years after the war, until it was declassified in 1996. [...] "
            "In February 2022, members of the Ghost Army were awarded the Congressional Gold Medal for their service. [...] "
            "It was equipped with inflatable tanks, cannons, jeeps, trucks, and airplanes that the men would inflate with air compressors and then camouflage imperfectly so that enemy aerial reconnaissance could see them. "
            "They could create dummy airfields, troop bivouacs (complete with fake laundry hanging on clotheslines), motor pools, artillery batteries, and tank formations in a few hours. "
            "Many of the men in this unit were artists, recruited from New York and Philadelphia art schools. [...] "
            "Several of these soldier-artists went on to have a major impact on art in the postwar US. "
            "Bill Blass, Ellsworth Kelly, wildlife artist Arthur Singer, and Art Kane were among the many artists who served in the 603rd. [...] "
            "Aided by engineers from Bell Labs, a team from the 3132 went to Fort Knox to record sounds of armored and infantry units onto a series of sound effects records that they brought to Europe. "
            "For each deception, sounds could be \"mixed\" to match the scenario they wanted the enemy to believe. [...] "
            "and then played back with powerful amplifiers and speakers mounted on halftracks. "
            "These sounds were audible 15 miles (24 km) away.",
            nome="Ghost Army")],
    },
    # 3 os pombos-pilotos de Skinner
    {
        "temas_secundarios": ["experimentos_psicologia", "comportamento_animal"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Na Segunda Guerra, o psicólogo B. F. Skinner treinou pombos para guiar uma bomba bicando a imagem do alvo numa tela. Os militares acharam a ideia excêntrica e a cancelaram; em 2024, ela lhe rendeu um Ig Nobel.",
        "explicacao": (
            "No fim dos anos 1930, Skinner já usava pombos nas pesquisas sobre condicionamento operante, o "
            "aprendizado por recompensa, e os ensinava a fazer truques. Com a entrada dos EUA na guerra, propôs "
            "usar a mesma técnica para que as aves servissem de \"pilotos\". A ideia básica: uma lente no nariz "
            "da bomba projetava a imagem do alvo numa tela, e o pombo, treinado para reconhecê-lo, bicava a "
            "imagem. Se a bomba saía do rumo, a imagem escorregava para a borda, o pombo a seguia, e esse "
            "movimento da tela servia de sinal para corrigir a direção. O treino era à base de grãos de comida, e "
            "uma das aves bicou mais de 10 mil vezes em 45 minutos. Quando havia dois alvos possíveis na tela, Skinner "
            "notou que ao menos dois dos três pombos concordavam, e o terceiro era \"punido pela opinião minoritária\". O projeto ganhou "
            "verba em 1943, mas o comitê de pesquisa de defesa o via como excêntrico e pouco prático. \"Ninguém "
            "nos levava a sério\", queixou-se Skinner. Foi cancelado em outubro de 1944, revivido pela Marinha em "
            "1948 e encerrado de vez em 1953, quando a orientação eletrônica se mostrou confiável. Em 2024, Skinner "
            "ganhou postumamente o Ig Nobel da Paz, recebido pela filha."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Project_Pigeon",
            "During World War II, Project Pigeon (later Project Orcon, for \"organic control\") was American behaviorist B. F. Skinner's attempt to develop a pigeon-controlled guided bomb. [...] "
            "In the late 1930s, behaviorist B. F. Skinner was using pigeons in his research into operant conditioning, successfully training the birds to perform tricks. "
            "After the United States entered World War II, Skinner sought to use the same techniques to train pigeons to act as \"pilots\" for a bomb. [...] "
            "In June 1943, the Office of Scientific Research and Development funded Skinner's proposal [...] "
            "The guidance system consisted of three lenses mounted in the nose of the bomb, which projected an image of the target onto screens affixed in a small compartment inside the nose cone. [...] "
            "One to three pigeons trained to recognize a target were stationed in front of their screens; when they saw the target, they would peck at the screens. "
            "They were trained by being shown an image of the target, with progressively faster pecking required to earn grains of food. "
            "One bird pecked more than 10,000 times in 45 minutes. [...] "
            "if the bomb began to drift off course, the image would move toward the edge of the screen. "
            "The pigeons would follow the image, pecking at it, tilting the screen on its pivots. "
            "When two possible targets were on the screen, Skinner noted that at least two of the birds would be in agreement, and the dissenter would be \"punished for his minority opinion\" [...] "
            "The National Defense Research Committee (part of the OSSRD) regarded the idea of using pigeons to guide glide bombs as eccentric and impractical [...] "
            "Skinner later complained: \"Our problem was no one would take us seriously\". [...] "
            "Project Pigeon was canceled in October 1944 [...] "
            "The project was briefly revived by the U.S. Navy in 1948 as \"Project Orcon\", but was again canceled in 1953 once electronic guidance systems were proven reliable. "
            "In 2024, Skinner was posthumously awarded the Ig Nobel Peace Prize for his work on the project; his daughter Julie Vargas, who received the award in his stead",
            nome="Project Pigeon")],
    },
    # 4 as Bruxas da Noite
    {
        "temas_secundarios": ["personagens_esquecidos", "transportes"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "As \"Bruxas da Noite\", aviadoras soviéticas, atacavam em biplanos de treino projetados em 1928. O avião era tão lento que sua velocidade máxima ficava abaixo da velocidade de estol dos caças alemães.",
        "explicacao": (
            "O 588º Regimento de Bombardeio Noturno foi criado em 1941 por Marina Raskova, aviadora recordista "
            "que usou seu contato pessoal com Stálin para formar unidades de combate só de mulheres. A maioria era "
            "de voluntárias no fim da adolescência ou no começo da vida adulta. O avião era o Polikarpov U-2, de "
            "aço e lona, um projeto de 1928 feito para treinar pilotos e pulverizar lavouras. Obsoleto e lento, "
            "tinha uma vantagem inesperada: sua velocidade máxima era menor que a velocidade de estol dos caças "
            "alemães Bf 109 e Fw 190, o que tornava o U-2 muito difícil de abater para os pilotos alemães. A tática era chegar perto do alvo com o motor em marcha lenta e planar, de modo que só "
            "o vento denunciava o avião. Segundo relatos, os alemães comparavam esse som ao de vassouras, daí o "
            "apelido. Como o avião carregava só 350 kg de bombas, eram comuns oito ou mais missões por noite, e "
            "até 1944 as pilotos voavam sem paraquedas, por causa do peso e da baixa altitude. O regimento fez "
            "mais de 23 mil surtidas; 23 integrantes receberam o título de Herói da União Soviética, e "
            "trinta e duas morreram na guerra."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Night_Witches",
            "\"Night Witches\" was a World War II nickname for the all-female military aviators of the 588th Night Bomber Regiment [...] "
            "Major Marina Raskova used her position and personal contacts with the Soviet leader Joseph Stalin to obtain permission to form female combat units. [...] "
            "On October 8, 1941, an order was issued to deploy three women's air-force units, including the 588th Regiment. "
            "The regiment, formed by Raskova and led by Major Yevdokiya Bershanskaya, was composed primarily of female volunteers in their late teens and early twenties. "
            "An attack technique of the night bombers involved idling the engine near the target and gliding to the bomb-release point with only wind noise left to reveal their presence. "
            "Allegedly, German soldiers likened the sound to broomsticks and hence named the pilots \"Night Witches\". "
            "Due to the weight of the bombs and the low altitude of flight, the pilots did not carry parachutes until 1944. [...] "
            "Raskova had already established several world records in long-distance non-stop flights [...] "
            "The regiment flew over 23,000 sorties, dropping over 3,000 tons of bombs and 26,000 incendiary shells. [...] "
            "twenty-three having been awarded the Hero of the Soviet Union title. "
            "Thirty-two of its members died during the war. "
            "The regiment flew in steel-and-canvas Polikarpov U-2 biplanes, a 1928 design intended for use as training aircraft (hence its original uchebnyy designation prefix of \"U-\") and for crop dusting [...] "
            "The plane could carry only  350 kilograms (770 lb) of bombs, so eight or more missions per night were often necessary. "
            "Although the aircraft was obsolete and slow, the pilots took advantage of its exceptional maneuverability; it also had a maximum speed that was lower than the stalling speed of both the Messerschmitt Bf 109 and the Focke-Wulf Fw 190, which made it very difficult for German pilots to shoot down",
            nome="Night Witches")],
    },
    # 5 os meteorologistas de Svalbard, últimos a se render
    {
        "temas_secundarios": ["clima_tempo", "paisagens_extremas"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "A última tropa alemã a se render na Segunda Guerra foi uma equipe de meteorologia no Ártico, em Svalbard. Souberam do fim da guerra pelo rádio em maio de 1945, mas só se entregaram em setembro, a caçadores de focas.",
        "explicacao": (
            "Na guerra, a previsão do tempo era informação estratégica, e boa parte do clima da Europa se forma no "
            "Atlântico Norte e no Ártico. Por isso, os dois lados disputaram estações meteorológicas em lugares "
            "remotos. Em 1941, uma operação aliada em Spitsbergen teve entre os objetivos calar as estações de "
            "rádio do arquipélago, para que os alemães não recebessem boletins do tempo, e até agosto daquele ano "
            "os Aliados já tinham eliminado estações alemãs na Groenlândia, em Jan Mayen e na Ilha do Urso. A "
            "Alemanha insistiu com novas equipes. A da Operação Haudegen foi levada em setembro de 1944 por um "
            "submarino e um navio de apoio para Svalbard, arquipélago norueguês a uns 1.050 km do Polo Norte. Em "
            "8 de maio de 1945, os homens receberam de seus comandantes a mensagem de que a Alemanha tinha se "
            "rendido. Depois disso, perderam o contato por rádio e só conseguiram pedir ajuda em agosto. No início "
            "de setembro de 1945, foram recolhidos por um barco norueguês de caça de focas e se renderam ao "
            "capitão, quatro meses depois do fim da guerra na Europa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Operation_Haudegen",
            "Operation Haudegen (Unternehmen Haudegen [Operation Broadsword]) was the name of a German operation during the Second World War to establish meteorological stations on the Svalbard archipelago in Norway. "
            "In September 1944, the submarine U-307 and the supply ship Carl J. Busch transported the men of Unternehmen Haudegen to the island. [...] "
            "On May 8, 1945, the staff received a message from their commanders in Tromsø that Germany had surrendered and the war was over. "
            "After that, radio contact was lost. "
            "The soldiers were capable of asking for support only in August 1945 and on 4 or 6 September, were picked up by a Norwegian seal hunting vessel and surrendered to its captain. "
            "The group of men were the last German troops to surrender after the Second World War. [...] "
            "The Svalbard Archipelago is in the Arctic Ocean 650 mi (1,050 km) from the North Pole [...] "
            "Gauntlet's objective was to deny the Germans the coal, mining and shipping infrastructure, equipment and stores on Spitsbergen and suppress the wireless stations on the archipelago, to prevent the Germans from receiving weather reports. [...] "
            "By August 1941, the Allies had eliminated German weather stations on Greenland, Jan Mayen Island, Bear Island (Bjørnøya) and the civil weather reports from Spitzbergen.",
            nome="Operation Haudegen")],
    },
    # 6 as medalhas Nobel dissolvidas em água-régia
    {
        "temas_secundarios": ["elementos_quimicos", "quimica_cotidiano"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Para esconder dos nazistas duas medalhas Nobel de ouro, o químico George de Hevesy as dissolveu em água-régia e deixou o frasco numa prateleira do laboratório. Depois da guerra, tirou o ouro da solução.",
        "explicacao": (
            "As medalhas eram dos físicos alemães Max von Laue e James Franck, que as tinham mandado para a "
            "Dinamarca, para o Instituto Niels Bohr, em Copenhague, para que não fossem confiscadas. O governo "
            "nazista tinha proibido alemães de aceitar ou guardar o Nobel, e era ilegal tirar ouro da Alemanha: se "
            "a remessa fosse descoberta, os dois podiam ser processados. Quando a Alemanha invadiu a Dinamarca, o "
            "risco ficou concreto. Hevesy, químico húngaro que trabalhava no instituto, usou a água-régia, mistura "
            "de ácido nítrico e ácido clorídrico que recebeu esse nome dos alquimistas justamente por dissolver "
            "metais nobres como o ouro. O frasco ficou na prateleira entre talvez centenas de outros, e os "
            "nazistas o ignoraram, achando que continha um produto químico qualquer. O próprio Hevesy, de família "
            "judia, fugiu para a Suécia em 1943, mesmo ano a que corresponde o seu Nobel de Química, pelo uso de "
            "isótopos radioativos como marcadores. Ao voltar, encontrou a solução intacta e precipitou o ouro. "
            "A Fundação Nobel refez as medalhas com o metal recuperado e as devolveu aos dois laureados."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("George_de_Hevesy",
                "was a Hungarian radiochemist and Nobel Prize in Chemistry laureate, recognized in 1943 for his key role in the development of radioactive tracers [...] "
                "Prior to the onset of World War II, Max von Laue and James Franck had sent their gold Nobel Prize medals to Denmark to keep them from being confiscated by the Nazis. "
                "After the Nazi invasion of Denmark this placed them in danger; it was illegal at the time to send gold out of Germany, and were it discovered that Laue and Franck had done so, they could have faced prosecution. "
                "To prevent this, de Hevesy concealed the medals by dissolving them in aqua regia and placing the resulting solution on a shelf in his laboratory at the Niels Bohr Institute in Copenhagen. "
                "After the war, he returned to find the solution undisturbed and precipitated the gold out of the acid. "
                "The Nobel Society then recast the medals using the recovered gold and returned them to the two laureates. "
                "By 1943, Copenhagen was no longer safe for a Jewish scientist and de Hevesy fled to Sweden",
                nome="George de Hevesy"),
            wiki("Aqua_regia",
                "Aqua regia (; from Latin, \"regal water\" or \"royal water\") is a mixture of nitric acid and hydrochloric acid [...] "
                "It was so named by alchemists because it can dissolve noble metals, such as gold and platinum, while leaving many other metals unaffected. [...] "
                "The German government had prohibited Germans from accepting or keeping any Nobel Prize after jailed peace activist Carl von Ossietzky had received the Nobel Peace Prize in 1935. "
                "De Hevesy placed the resulting solution on a shelf in his laboratory at the Niels Bohr Institute. "
                "It was subsequently ignored by the Nazis who thought the jar—one of perhaps hundreds on the shelving—contained common chemicals.",
                nome="Aqua regia"),
        ],
    },
    # 7 Aracy de Carvalho e os vistos na papelada
    {
        "temas_secundarios": ["brasil_republica", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "No consulado do Brasil em Hamburgo, Aracy de Carvalho driblou uma circular secreta que barrava judeus: tirava dos vistos a letra \"J\" e os misturava à papelada que o cônsul assinava. Depois, casou-se com Guimarães Rosa.",
        "explicacao": (
            "Aracy nasceu em Rio Negro, no Paraná, em 1908, filha de mãe alemã, e falava português, alemão, "
            "inglês e francês. Por isso conseguiu, em 1936, um posto no consulado brasileiro em Hamburgo, onde "
            "chefiou a seção de passaportes. Em 1938, entrou em vigor no Brasil de Getúlio Vargas a circular "
            "secreta 1.127, que restringia a entrada de judeus no Brasil. Aracy a ignorou. Como despachava com o "
            "cônsul-geral, punha os vistos no meio dos papéis a assinar e deixava de marcar neles o \"J\" que "
            "identificava os judeus. Segundo o verbete em inglês da Wikipedia, ela começou a ajudar judeus na "
            "Noite dos Cristais, em novembro de 1938, e chegou a dar vistos a pessoas que sabia estarem com "
            "passaportes falsos. No consulado, conheceu o cônsul-adjunto João Guimarães Rosa, com quem se casou, "
            "e que lhe dedicaria \"Grande Sertão: Veredas\". Os dois ficaram na Alemanha até 1942, quando o Brasil "
            "rompeu relações com o país. Em 1982, o Yad Vashem, em Israel, a reconheceu como Justa entre as "
            "Nações; o único outro brasileiro com essa honra é o embaixador Souza Dantas. Aracy morreu em 2011, "
            "aos 102 anos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Aracy_de_Carvalho",
                "Apenas um outro brasileiro, Souza Dantas, foi distinguido com este reconhecimento. "
                "A homenagem de inclusão do nome de Aracy no Jardim dos Justos entre as Nações do Yad Vashem (Museu do Holocausto), em Israel, foi prestada em 8 de julho de 1982 [...] "
                "Aracy nasceu em Rio Negro, no Paraná, em 1908. Era filha de Sidonie Möbius (Moebius), natural da Alta Saxônia, na Alemanha [...] "
                "Por falar quatro línguas (português, inglês, francês e alemão), conseguiu uma nomeação no consulado brasileiro em Hamburgo, onde passou a ser chefe da Seção de Passaportes. "
                "Em 1938, entrou em vigor, no Brasil, a circular secreta 1.127, que restringia a entrada de judeus no país. "
                "Aracy ignorou a circular e continuou preparando vistos para judeus, permitindo sua entrada  no Brasil. "
                "Como despachava com o cônsul-geral, ela colocava os vistos entre a papelada para as assinaturas. "
                "Para obter a aprovação dos vistos, Aracy simplesmente deixava de pôr neles a letra \"J\", que identificava quem era judeu. [...] "
                "Ainda na Alemanha, Aracy casou-se com João Guimarães Rosa, à época cônsul-adjunto. "
                "Os dois permaneceram na Alemanha até 1942, quando o governo brasileiro rompeu relações diplomáticas com aquele país [...] "
                "O livro de Guimarães Rosa \"Grande Sertão: Veredas\", de 1956, foi dedicado a Aracy. [...] "
                "morreu no dia 28 de fevereiro de 2011 em São Paulo, de causas naturais, aos cento e dois anos.",
                nome="Aracy de Carvalho", idioma="pt"),
            wiki("Aracy_de_Carvalho",
                "In 1936, she was appointed to the Brazilian Consulate in Hamburg, Germany, where she was made the Chief of the Passport Section. "
                "She started to help Jewish people during Kristallnacht, on 9 November 1938. "
                "She handed out visas to Jews without the red \"J\" that identified them as such, since Brazilian Dictator Getúlio Vargas non-officially denied visas to Jews. "
                "She was in close relations with underground activists in Germany and would even grant visas to Jews that she knew had forged passports. [...] "
                "She died peacefully at the age of 102",
                nome="Aracy de Carvalho"),
        ],
    },
    # 8 Garbo, o espião dos 27 agentes inventados
    {
        "temas_secundarios": ["espionagem", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "O espião espanhol Juan Pujol enganou os nazistas com uma rede de 27 agentes, todos inventados. Foi condecorado pelos dois lados: recebeu a Cruz de Ferro alemã e uma ordem britânica.",
        "explicacao": (
            "Pujol ofereceu-se como espião à embaixada britânica em Madri e foi recusado. Criou então a identidade "
            "de um funcionário espanhol fanaticamente pró-nazista e virou agente alemão, com ordem de ir à "
            "Grã-Bretanha recrutar uma rede. Em vez disso, foi para Lisboa e fabricou relatórios \"de Londres\" com "
            "um guia turístico, horários de trem, cinejornais e anúncios de revista; cobrava até despesas de "
            "viagem pelos preços de um guia ferroviário britânico. Para justificar erros, inventava subagentes. "
            "Os britânicos só o aceitaram quando viram os alemães gastarem muitos recursos caçando um comboio que "
            "não existia. A partir daí, com o codinome Garbo, ele e seu controlador ampliaram a rede fictícia. "
            "Quando um \"agente\" de Liverpool precisou sumir, ele \"morreu\", ganhou obituário no jornal local, e os "
            "alemães aceitaram pagar pensão à \"viúva\". O golpe maior veio em 1944: as informações falsas de Pujol "
            "ajudaram a convencer os alemães de que o desembarque principal seria em Pas-de-Calais, e grandes "
            "forças ficaram esperando ali mesmo depois do Dia D. Em julho de 1944, recebeu a Cruz de Ferro. "
            "Depois da guerra, com medo de represálias, forjou a própria morte em Angola, em 1949, e foi viver na "
            "Venezuela."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Juan_Pujol_García",
            "Pujol and his wife contacted the British Embassy in Madrid, which rejected his offer. "
            "Undeterred, he created a false identity as a fanatically pro-Nazi Spanish government official and successfully became a German agent. "
            "He was instructed to travel to Britain and recruit additional agents; instead he moved to Lisbon and created bogus reports about Britain from a variety of public sources including a tourist guide to Britain, train timetables, cinema newsreels, and magazine advertisements. [...] "
            "He began inventing fictitious sub-agents who could be blamed for false information and mistakes. "
            "The Allies finally accepted Pujol when the Germans expended considerable resources attempting to hunt down a fictitious convoy. [...] "
            "Pujol and his handler Tomás Harris spent the rest of the war expanding the fictitious network [...] "
            "Eventually the Germans were funding a network of 27 agents, all fictitious. [...] "
            "The false information Pujol supplied helped persuade the Germans that the main attack would be in the Pas de Calais, so that they kept large forces, including the Fifteenth Army, lead by Hans von Salmuth, there before and even after the invasion. "
            "Pujol had the distinction of receiving military decorations from both sides of the war – being awarded the Iron Cross and later becoming a Member of the Order of the British Empire. [...] "
            "He claimed to be travelling around Britain and submitted his travel expenses based on fares listed in a British railway guide. [...] "
            "he reported that his (fabricated) Liverpool agent had fallen ill just before a major fleet movement from that port, and so was unable to report the event. "
            "To support this story, the agent eventually \"died\" and an obituary was placed in the local newspaper as further evidence to convince the Germans. "
            "The Germans were also persuaded to pay a pension to the agent's \"widow\". [...] "
            "After the Second World War, Pujol feared reprisals from surviving Nazis. "
            "With the help of MI5, Pujol travelled to Portuguese Angola and faked his death from malaria in 1949. "
            "He then moved to Lagunillas, Venezuela [...] "
            "As Alaric, he was awarded the Iron Cross Second Class on 29 July 1944",
            nome="Juan Pujol García")],
    },
    # 9 os botânicos que não comeram as sementes no cerco de Leningrado
    {
        "temas_secundarios": ["plantas", "domesticacao"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "No cerco de Leningrado, botânicos guardaram o banco de sementes de Nikolai Vavilov e se recusaram a comê-lo, mesmo passando fome. Vários morreram de inanição ao lado de toneladas de sementes.",
        "explicacao": (
            "Vavilov, obcecado desde jovem com a ideia de acabar com a fome, percorreu o mundo coletando sementes "
            "e criou em Leningrado, hoje São Petersburgo, um instituto que abrigava o maior banco de sementes do "
            "mundo na época. Ele é apontado como o primeiro botânico a perceber a necessidade de um banco de "
            "sementes. Durante os 28 meses do cerco alemão à cidade, as autoridades soviéticas evacuaram a arte "
            "do Museu Hermitage, mas não a coleção do instituto. Uma tentativa de tirar parte das sementes e da "
            "equipe falhou quando os alemães fecharam a última linha de trem. Os cientistas que ficaram "
            "encaixotaram uma amostra representativa, levaram-na para o porão e se revezaram na guarda contra "
            "bombas incendiárias, frio extremo e ratos. A coleção, com cerca de 120 toneladas de sementes, nozes e "
            "raízes, incluindo 6 mil variedades de batata, sobreviveu. Vários guardiões morreram de fome antes do "
            "fim do cerco, na primavera de 1944. O próprio Vavilov não estava lá: tinha sido preso em 1940, "
            "depois de se opor às ideias de Lysenko, que rejeitava a genética e agradavam a Stálin, e morreu na prisão em 1943. Alguns autores "
            "afirmam que ele também morreu de fome."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Vavilov_Institute_of_Plant_Industry",
                "The Institute of Plant Industry was established in 1921 in Leningrad by Nikolai Vavilov who set about to create the world's first and largest collection of plant seeds. "
                "Already in 1916 he did his first collection trip abroad, to Iran, and by 1932 he had collected seeds from almost every country in the world [...] "
                "He was a strong proponent of Lamarckism (the theory that changes to an organism's body during its life would be inherited) and rejected Mendelian hereditary genetics. "
                "This fitted Josef Stalin's world view, as it was seen as a marxist rejection of heritage in favour of environment, but Vavilov objected to it. [...] "
                "While collecting seeds in Ukraine in August 1940, he was arrested and accused of spying and ruining Soviet agriculture. [...] "
                "During the 28-month siege of Leningrad in World War II, a limited evacuation of some institute staff and a small number of seeds failed when the Germans closed the last rail line going out of Leningrad. "
                "The institute's extensive seed collection  (consisting of some 120 tonnes of seeds, nuts and roots, including 6,000 varieties of potato) survived, thanks to the 50 botanists who worked there. "
                "They protected the seeds from German fire bombs, extreme cold, rodents, and their own hunger - as they would rather starve to death than eat the collection.",
                nome="Vavilov Institute of Plant Industry"),
            wiki("Nikolai_Vavilov",
                "Vavilov became obsessed from an early age with ending famine. [...] "
                "He was the first botanist to grasp the need for a seedbank, and he was an expert germplasm collector. "
                "The Leningrad seedbank was preserved and protected through the 28-month long Siege of Leningrad. "
                "While the Soviets had ordered the evacuation of art from the Hermitage Museum, they had not evacuated the 250,000 samples of seeds, roots, and fruits stored in what was then the world's largest seedbank. [...] "
                "up of scientists at the Vavilov Institute boxed up a cross section of seeds, moved them to the basement, and took shifts protecting them. "
                "Those guarding the seedbank refused to eat its contents, even though by the end of the siege in the spring of 1944, a number of them had died of starvation. [...] "
                "in 1943, he died in prison in Saratov as a result of the harsh conditions. [...] "
                "Some authors assert that the actual cause of death was starvation.",
                nome="Nikolai Vavilov"),
        ],
    },
    # 10 o porta-aviões de gelo e serragem
    {
        "temas_secundarios": ["estados_materia", "grandes_obras"],
        "tipos_espanto": ["engenhosidade", "escala_absurda"],
        "gancho": "Os britânicos planejaram um porta-aviões de gelo reforçado com polpa de madeira, com 600 metros de comprimento. Um protótipo foi construído num lago do Canadá e levou três verões quentes para derreter.",
        "explicacao": (
            "A ideia foi de Geoffrey Pyke, do quartel-general de Operações Combinadas britânico: uma escala "
            "flutuante para aviões no meio do oceano, para cobrir a lacuna aérea no meio do Atlântico. "
            "O navio teria 600 m, muito mais que os maiores porta-aviões já construídos. O material criado para o "
            "projeto, o pykrete, batizado em homenagem a Pyke, era mais resistente que o gelo comum, derretia "
            "mais devagar e não afundava. Max Perutz fez testes no mercado de Smithfield, em Londres, e achou a "
            "melhor proporção: 14% de polpa de madeira e 86% de água. Ao ficar imerso, o "
            "material forma uma casca de polpa molhada que isola o interior. O problema é que o gelo escoa "
            "lentamente, e o casco cederia aos poucos se não fosse mantido a −16 °C. No lago Patricia, em Alberta, "
            "objetores de consciência construíram um protótipo de 18 por 9 metros e mil toneladas, mantido "
            "congelado por um motor de 1 cavalo. O projeto foi abandonado pelos custos crescentes e porque aviões "
            "de maior alcance e porta-aviões de escolta fecharam a lacuna no Atlântico. As peças de metal "
            "afundadas do protótipo continuam no lago."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Project_Habakkuk",
            "st ship ever at 600 metres (1,969 ft) long, which would have been much bigger than even the USS Enterprise and the USS Gerald R. Ford [...] "
            "The idea came from Geoffrey Pyke, who worked for Combined Operations Headquarters. [...] "
            "Pyke was not the first to suggest a floating mid-ocean stopping point for aircraft [...] "
            "After promising scale tests and the creation of a prototype on Patricia Lake, Jasper National Park, in Alberta, Canada, the project was shelved due to rising costs, added requirements, and the availability of longer-range aircraft and escort carriers which closed the Mid-Atlantic gap that the project was intended to address. [...] "
            "Meanwhile Perutz had determined via his experiments at Smithfield Market that the optimum structural properties were given by a mixture of 14 per cent wood pulp and 86 per cent water. [...] "
            "Large ice blocks were constructed at Lake Louise, Alberta, and a small prototype was constructed at Patricia Lake, Alberta, measuring  60 by 30 feet (18 metres by 9 metres), weighing 1,000 tons and kept frozen by a one-horsepower motor. "
            "The work was done by conscientious objectors [...] "
            "(The sunken remains of the metal parts of the boat remain there to this day.) [...] "
            "It took three hot summers to completely melt the prototype constructed in Canada. [...] "
            "a mixture of water and woodpulp that when frozen was stronger than plain ice, was slower-melting and would not sink. "
            "Developed by his government group and named after Pyke [...] "
            "and when immersed in water formed an insulating shell of wet wood pulp on its surface that protected its interior from further melting. "
            "However, Perutz found a problem: ice flows slowly, in what is known as plastic flow, and his tests showed that a pykrete ship would slowly sag unless it was cooled to −16 °C (3 °F).",
            nome="Project Habakkuk")],
    },
    # 11 os falsificadores de Sachsenhausen
    {
        "temas_secundarios": ["dinheiro", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Os nazistas puseram presos de um campo de concentração para falsificar libras em massa. Quando a ordem passou a ser falsificar dólares, eles atrasaram o trabalho de propósito: terminar podia custar suas vidas.",
        "explicacao": (
            "A Operação Bernhard reuniu no campo de Sachsenhausen presos judeus escolhidos em vários campos de "
            "concentração, sob o comando do major da SS Bernhard Krüger. As estimativas do que imprimiram até 1945 "
            "variam de 132,6 milhões a 300 milhões de libras. A gravação e a impressão eram consideradas "
            "excelentes, embora o papel fosse inferior ao verdadeiro. As notas pagaram, por exemplo, o espião "
            "Cicero, que roubava segredos do embaixador britânico em Ancara. Quando vieram os dólares, os presos "
            "perceberam que, se completassem a falsificação, deixariam de ser úteis, e passaram a atrasar o "
            "serviço o quanto podiam. Segundo o jornalista Lawrence Malkin, eles achavam que Krüger aprovava em "
            "silêncio, já que o fim da operação o mandaria para a frente de batalha. No fim da guerra, a unidade "
            "foi levada para a Áustria, e a ordem era matar os presos só quando todos estivessem juntos no campo "
            "de Ebensee. Um atraso na última viagem do caminhão, com os Aliados se aproximando, fez os guardas "
            "fugirem, e os presos foram libertados pelo Exército americano. Grande parte das notas foi jogada em "
            "lagos austríacos, mas circularam tantas que o Banco da Inglaterra trocou o desenho das notas depois "
            "da guerra."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Operation_Bernhard",
            "prisoners from Nazi concentration camps were selected and sent to Sachsenhausen concentration camp to work under SS Major Bernhard Krüger. "
            "The unit produced British notes until mid-1945; estimates vary of the number and value of notes printed, from £132.6 million up to £300 million. [...] "
            "Counterfeit notes from the operation were used to pay the Turkish agent Elyesa Bazna—code named Cicero—for his work in obtaining British secrets from the British ambassador in Ankara [...] "
            "In early 1945 the unit was moved to Mauthausen-Gusen concentration camp in Austria, then to the Redl-Zipf series of tunnels and finally to Ebensee concentration camp. [...] "
            "they were liberated shortly afterwards by the American Army. "
            "Much of the output of the unit was dumped into the Toplitz and Grundlsee lakes at the end of the war, but enough went into general circulation that the Bank of England stopped releasing new notes and issued a new design after the war. [...] "
            "He was ordered to use the Jewish prisoners incarcerated in the Nazi concentration camps [...] "
            "Krüger visited several other concentration camps to assemble the peop[...] "
            "The standard of engraving and printing was considered excellent, although the paper used was technically inferior to the genuine notes. [...] "
            "The prisoners realised that if they managed to fully counterfeit the dollars, their lives would no longer be safeguarded by the work they were undertaking, so they slowed their progress as much as they could. "
            "The journalist Lawrence Malkin, who wrote a history of Operation Bernhard, writes that prisoners considered this to have the tacit approval of Krüger, who would face front-line duty if Operation Bernhard ended. [...] "
            "An order had been issued that the prisoners were to be killed, but only once they were together at Ebensee. [...] "
            "Because of the delay with the third journey and the close proximity of the advancing Allied army, on 5 May the first two groups were released from their isolation into the general population and their SS guards fled.",
            nome="Operation Bernhard")],
    },
    # 12 Pilecki, o homem que entrou em Auschwitz
    {
        "temas_secundarios": ["personagens_esquecidos", "espionagem"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Em 1940, o oficial polonês Witold Pilecki entrou em Auschwitz com nome falso, numa missão da resistência: organizar os presos e mandar relatórios para fora. Fugiu em 1943. Em 1948, foi executado pelo regime comunista.",
        "explicacao": (
            "Na época, pouco se sabia sobre Auschwitz, que se imaginava um campo de internação ou uma grande "
            "prisão, e não um campo de extermínio. Pilecki foi um dos 2 mil homens presos em 19 de setembro de "
            "1940, usando os documentos de um certo Tomasz Serafiński, dado por morto por engano. Há duas versões "
            "sobre como foi parar no campo: numa, deixou-se capturar numa batida alemã em Varsóvia justamente para "
            "se infiltrar; por isso muitas fontes dizem que ele se ofereceu como voluntário. Lá dentro, organizou um "
            "movimento de resistência que chegou a centenas de presos e escreveu relatórios contrabandeados por "
            "presos libertados ou fugitivos. O primeiro, de outubro de 1940, já descrevia o extermínio de presos "
            "pela fome e por castigos brutais, e os relatos chegaram aos Aliados ocidentais. Na noite de 26 para 27 "
            "de abril de 1943, escalado para a padaria fora da cerca, fugiu com dois companheiros. Lutou depois na "
            "Revolta de Varsóvia. Fiel ao governo polonês no exílio, foi preso pela polícia secreta em 1947 e, "
            "após tortura e um julgamento de fachada, executado em 1948, aos 47 anos. Sua história ficou quase "
            "esquecida por décadas e só ganhou destaque depois do fim do comunismo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Witold_Pilecki",
            "In 1940, Pilecki let himself be captured by the occupying Germans in order to be voluntarily sent to the Auschwitz concentration camp and infiltrate it. "
            "At Auschwitz, he organized a resistance movement that eventually included hundreds of inmates, and he secretly drew up reports detailing German atrocities at the camp, which were smuggled out to Home Army headquarters and shared with the Western Allies. "
            "After escaping from Auschwitz in April 1943, Pilecki fought in the Warsaw Uprising of August–October 1944. [...] "
            "After the communist takeover of Poland, Pilecki remained loyal to the London-based Polish government-in-exile. [...] "
            "Subsequently, on 25 May 1948, Pilecki was executed [...] "
            "in 1947, he was arrested by the secret police on charges of working for \"foreign imperialism\" and the following year, after being subjected to torture and a show trial, he was executed in Warsaw aged 47. "
            "Pilecki's story, inconvenient to the Polish communist authorities, remained mostly unknown for several decades. [...] "
            "Little was known about how the Germans ran the then-new camp, which was thought to be an internment camp or large prison rather than a death camp. [...] "
            "which years later led to him being described in many sources as having volunteered to infiltrate Auschwitz. [...] "
            "Pilecki was one of 2,000 men arrested on 19 September 1940. "
            "He used the identity documents of Tomasz Serafiński, who had been mistakenly assumed to be dead. "
            "Two backstories exist purporting to explain how Pilecki actually found himself in Auschwitz. "
            "In one version, he allowed himself to be captured by the occupying Germans in one of their Warsaw street round-ups, in order to infiltrate the camp. [...] "
            "with the help of inmates that had been released or escapees. "
            "The first dispatch, delivered in October 1940, described the camp and the ongoing extermination of inmates via starvation and brutal punishments [...] "
            "On the night of 26–27 April 1943 Pilecki was assigned to a night shift at a camp bakery outside the fence, and he and two comrades managed to force open a metal door [...] "
            "From the 1990s, following the fall of communism in Poland and Pilecki's subsequent rehabilitation, he has been a subject of popular discourse.",
            nome="Witold Pilecki")],
    },
    # 13 a fuga dos judeus da Dinamarca
    {
        "temas_secundarios": ["personagens_esquecidos", "fisica_particulas"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Avisados por um diplomata alemão, os judeus da Dinamarca fugiram em massa para a Suécia em barcos de pesca, botes e até caiaques, em outubro de 1943. No fim, 99% deles sobreviveram ao Holocausto.",
        "explicacao": (
            "Os ocupantes alemães planejavam deportar os cerca de 8 mil judeus dinamarqueses. Em 28 de setembro de "
            "1943, o diplomata alemão Georg Ferdinand Duckwitz vazou o plano ao governo da Dinamarca. O aviso "
            "chegou ao rabino Marcus Melchior, que o repassou nos cultos da manhã seguinte, véspera do Ano-Novo "
            "judaico. Pediu-se a todos que se escondessem já e espalhassem o aviso. A batida foi marcada para a noite "
            "de 1º para 2 de outubro, quando os alemães contavam encontrar todos em casa. Os fugitivos foram "
            "levados pelo estreito de Øresund até a Suécia, numa travessia que em média durava menos de uma hora, "
            "em barcos de pesca de até 20 toneladas, botes a remo e caiaques. O resgate custou cerca de 20 milhões "
            "de coroas, metade pagas pelas famílias judias. O físico Niels Bohr, cuja mãe era judia, recusou-se a "
            "seguir da Suécia para os EUA, onde era esperado no Projeto Manhattan, até que o país anunciasse que "
            "acolheria os refugiados; o anúncio saiu no rádio sueco em 2 de outubro. Há historiadores, porém, que "
            "atribuem a decisão sueca a uma política já definida antes. Os 464 judeus capturados foram para o campo "
            "de Theresienstadt, e a pressão dinamarquesa em favor deles ajudou a garantir a sobrevivência de 99%."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Rescue_of_the_Danish_Jews",
            "on September 28, 1943, German diplomat Georg Ferdinand Duckwitz leaked Hitler's plans to do so to the Danish government. [...] "
            "As a result of the rescue, and of the following Danish intercession on behalf of the 464 Danish Jews who were captured and deported to the Theresienstadt concentration camp in the Protectorate of Bohemia and Moravia, 99% of Denmark's Jewish population survived the Holocaust. [...] "
            "The German occupiers began their plans for the deportation to Nazi concentration camps of the 8,000 Danish Jews [...] "
            "who in turn alerted the acting chief rabbi, Marcus Melchior. "
            "At the early morning services, on September 29, the day prior to the Rosh Hashanah services, the Jews were warned of the Nazis' planned action. "
            "They were urged to go into hiding immediately and spread the word to all their friends and relatives. [...] "
            "In Copenhagen, the deportation order was carried out on the Jewish New Year, the night of October 1–2, when the Germans assumed all Jews would be gathered at home. [...] "
            "In all, the rescue is estimated to have cost around 20 million kroner, about half of which were paid by Jewish families, as well as half from donations and collections. [...] "
            "The Danish physicist Niels Bohr, whose mother was Jewish, made a determined stand for his fellow countrymen [...] "
            "When Bohr arrived, Swedish government representatives told him he had to board an aircraft immediately for the United States (to work on the top-secret Manhattan Project). "
            "Bohr refused. "
            "He told the officials [...] that until Sweden announced over its airwaves and through its press that its borders would be open to receive the Danish Jews, he was not going anywhere. [...] "
            "on 2 October Swedish radio broadcast that Sweden was ready to receive the Jewish refugees. [...] "
            "According to Paul A. Levine, however [...] the Swedish Ministry for Foreign Affairs acted on clear instructions given much earlier by Prime Minister Per Albin Hansson and Foreign Minister Christian Günther, following a policy already established in 1942. [...] "
            "The Jews were smuggled and transported over the Øresund strait from Zealand to Sweden — a passage of varying time depending on the specific route and the weather; but averaging under an hour on the choppy winter sea. "
            "Some were transported in large fishing boats of up to 20 tons; others were carried to freedom in rowboats or kayaks.",
            nome="Rescue of the Danish Jews")],
    },
    # 14 a batalha do castelo de Itter
    {
        "temas_secundarios": ["historia_esportes", "personagens_esquecidos"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Cinco dias após a morte de Hitler, soldados americanos e alemães da Wehrmacht defenderam juntos um castelo austríaco contra a SS, ao lado de presos franceses ilustres. Um deles era um astro do tênis.",
        "explicacao": (
            "O castelo de Itter, no Tirol, tinha virado uma prisão para franceses importantes, administrada a "
            "partir do campo de Dachau. Entre os presos estavam os ex-primeiros-ministros Édouard Daladier e Paul "
            "Reynaud, a irmã mais velha de Charles de Gaulle e o tenista Jean Borotra. Nos últimos dias da guerra, "
            "o tenente americano Jack Lee aceitou o pedido de socorro do major alemão Josef Gangl, da Wehrmacht, e "
            "partiu com apenas 14 soldados americanos, o próprio Gangl e um caminhão com dez ex-artilheiros alemães. Um oficial "
            "da SS que os presos tinham feito amigo também ajudou na defesa. Em 5 de maio de 1945, uma força de 100 "
            "a 150 soldados da SS atacou. Lee mandou os franceses se esconderem, mas eles ficaram e lutaram. Com a "
            "comunicação cortada, Borotra pulou o muro e atravessou as linhas da SS para levar informações à tropa "
            "de socorro americana, que chegou à tarde e venceu o ataque. Gangl morreu ao tentar tirar Reynaud da "
            "linha de tiro, o único defensor morto, e virou herói nacional na Áustria. É um dos dois casos "
            "conhecidos de americanos e alemães lutando lado a lado na guerra, dois dias antes da rendição alemã."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Battle_of_Castle_Itter",
            "The Battle of Castle Itter was fought on 5 May 1945, in the Austrian village of Itter in the North Tyrol region of the country [...] "
            "The battle is one of two known times during the war in which Americans and Germans fought side by side, the other being Operation Cowboy [...] "
            "The prison was established to contain high-profile French prisoners valuable to the Reich. "
            "Notable prisoners included tennis player Jean Borotra, former prime ministers Édouard Daladier and Paul Reynaud [...] "
            "Charles de Gaulle’s elder sister Marie-Agnès de Gaulle [...] "
            "and the facility was placed under the administration of the Dachau concentration camp. [...] "
            "Asked to provide relief by Gangl, Lee did not hesitate, volunteering to lead the rescue mission [...] "
            "he set back off accompanied only by 14 American soldiers, Gangl, a driver, and a truck carrying ten former German artillerymen. [...] "
            "Meanwhile, the French prisoners had asked an SS officer, Kurt-Siegfried Schrader, whom they had befriended in Itter during his convalescence from wounds and who was living locally, to take charge of their defense. [...] "
            "a force of 100–150 Waffen-SS soldiers led by Oberführer Georg Bochmann, who had been occupying some hills near the town, decided to attack the castle. "
            "Lee had ordered the French prisoners to hide, but they remained outside and fought alongside the American and Wehrmacht soldiers. [...] "
            "Aware that he had been unable to give the 142nd complete information on the enemy and its disposition before communications had been severed, Lee accepted tennis star Borotra's offer to vault the castle wall and run the gauntlet of SS strong points and ambushes to deliver it. [...] "
            "The relief force arrived around 16:00, and the SS were promptly defeated. [...] "
            "Gangl died during the battle from a 7.92×57mm Mauser round while trying to move former French Prime Minister Paul Reynaud out of harm's way, and was honored as an Austrian national hero [...] "
            "He was the sole defender to die during the battle, though four others were wounded. [...] "
            "The battle was fought five days after Adolf Hitler had committed suicide and only two days before the signing of Germany's unconditional surrender.",
            nome="Battle of Castle Itter")],
    },
]
