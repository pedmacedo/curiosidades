LOTE = "2026-11-24-comportamento_animal-01"
AREA = "biologia"
TEMA = "comportamento_animal"
W = "https://en.wikipedia.org/wiki/"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


def resumo(consulta, titulo, trecho):
    """Resumo de artigo via API do Europe PMC (consulta já no formato da URL)."""
    return {"url": EPMC + "search?query=" + consulta + "&resultType=core&format=json",
            "titulo": titulo, "idioma": "en", "trecho": trecho}


CANDIDATOS = [
    # 1 a corva Betty e o gancho de arame
    {
        "temas_secundarios": ["aprendizagem_inteligencia", "evolucao"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Em Oxford, quando o parceiro levou o arame em gancho, a corva Betty dobrou um arame reto, fez o próprio gancho e pescou um baldinho de comida num tubo. Era a primeira vez que essas aves recebiam arame.",
        "explicacao": (
            "Betty e Abel eram dois corvos-da-nova-caledônia observados em 2002 por Alex Kacelnik e colegas, na "
            "Universidade de Oxford. O teste pedia que escolhessem entre um arame reto e um curvo para alcançar "
            "pedacinhos de coração de porco, a comida preferida deles, num baldinho dentro de um tubo vertical. O "
            "talento de Betty apareceu por acaso: quando Abel fugiu com o arame curvo, ela entortou o reto, em geral "
            "prendendo uma ponta embaixo de algo, e içou o balde. Em estudos seguintes, das dez vezes em que pegou a "
            "comida, ela dobrou o arame em nove. Na natureza, a espécie já fabrica ferramentas: cutuca larvas em "
            "frestas até que elas mordam o graveto e arranca tiras de folhas de pandano, cujas farpas servem de "
            "anzol. O arame, porém, era um material novo. Outros testes mostraram que esses corvos usam uma "
            "ferramenta para conseguir outra: com um graveto curto demais para a comida, iam buscar numa caixa um "
            "graveto mais longo. Seis de sete aves resolveram isso na primeira tentativa, algo antes só visto em "
            "primatas. E, num estudo da Sociedade Max Planck, corvos montaram ferramentas compostas encaixando de 2 a "
            "4 galhinhos curtos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("New_Caledonian_crow",
            "In 2002, researcher Alex Kacelnik and colleagues at the University of Oxford observed of a couple of New Caledonian crows called Betty and Abel [...] "
            "Betty's toolmaking abilities came to light by accident during an experiment in which she and Abel had to choose between a hooked and a straight wire for retrieving small pieces of pig heart, their favorite food. "
            "When Abel made off with the hooked wire, Betty bent the straight wire into a hook and used the tool to lift a small bucket of food from a vertical pipe. "
            "This experiment was the first time the crows had been presented with wire. [...] "
            "Out of ten successful retrievals, Betty bent the wire into a hook nine times. [...] "
            "usually by snagging one end of the wire under something [...] "
            "The New Caledonian crow sometimes captures grubs in nooks or crevices by poking a twig at the grub to agitate it into biting the twig [...] "
            "The crows can also make leaf tools by tearing rectangular strips off the edges of Pandanus spp. [...] "
            "the barbs running along the edges of these leaves can be used as hooks [...] "
            "The crows were given a stick that was too short to reach the food.  However, this short stick could be used to retrieve a longer stick from another box, which could then be used to retrieve the food. [...] "
            "It was solved by six of seven birds on the first attempt.  This behaviour had previously only been observed in primates. "
            "In a study conducted at the Max Planck Society crows have been shown to create compound tools from 2–4 short branches that could be slotted together.",
            nome="New Caledonian crow")],
    },
    # 2 corvos que ensinam uns aos outros um rosto perigoso
    {
        "temas_secundarios": ["aprendizagem_inteligencia", "psicologia_social"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Pesquisadores usaram uma máscara ao capturar corvos em Seattle. Depois, corvos que nunca tinham sido pegos, até filhotes, também davam gritos de alarme contra quem usasse a máscara: o perigo passou de corvo para corvo.",
        "explicacao": (
            "O experimento foi feito pelo laboratório de John Marzluff, professor da Universidade de Washington. "
            "Usando uma máscara de \"rosto perigoso\", a equipe capturou, anilhou e soltou de 7 a 15 corvos-americanos "
            "selvagens em cada um de cinco locais em volta de Seattle. Os corvos capturados passaram a atacar a "
            "máscara com gritos assim que a viam, sinal de que tinham aprendido o perigo. O surpreendente veio depois: "
            "corvos que nunca tinham sido capturados também gritavam contra ela, o que indica que aprenderam com o "
            "bando que se juntou durante as capturas. Filhotes de pais capturados também aprenderam a atacar a "
            "máscara, ou seja, a informação passou tanto entre colegas quanto de pais para filhos. Os corvos "
            "capturados diretamente distinguiam melhor a máscara perigosa de uma máscara neutra do que os que "
            "aprenderam com os outros. Num dos locais, ao longo de cinco anos, a frequência dos ataques à máscara "
            "dobrou e se espalhou por pelo menos 1,2 km a partir do ponto inicial. É um exemplo de transmissão "
            "cultural: um conhecimento que circula pelo grupo sem que cada indivíduo precise passar pela experiência."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Observational_learning",
                "The University of Washington studied this phenomenon with crows [...] "
                "The experimenters exposed wild crows to a unique \"dangerous face\" mask as they trapped, banded, and released 7–15 birds at five different study places around Seattle, WA. "
                "An immediate scolding response to the mask after trapping by previously captured crows illustrates that the individual crow learned the danger of that mask. [...] "
                "That response indicates conditioning from the mob of birds that assembled during the capture. "
                "Horizontal social learning (learning from peers) is consistent with the lone crows that recognized the dangerous face without ever being captured. "
                "Children of captured crow parents were conditioned to scold the dangerous mask, which demonstrates vertical social learning (learning from parents). "
                "The crows that were captured directly had the most precise discrimination between dangerous and neutral masks than the crows that learned from the experience of their peers. "
                "The ability of crows to learn doubled the frequency of scolding, which spread at least 1.2  km from where the experiment started to over a 5-year period at one site.",
                nome="Observational learning"),
            wiki("John_Marzluff",
                "John Marzluff (born 1958) is a professor of wildlife science at the University of Washington and an author. [...] "
                "His lab once banded American crows while wearing various masks, which demonstrated that crows identify and remember people's faces. "
                "After the people wearing the mask left, even crows that did not witness the tagging scolded the mask, showing an example of cultural transmission in crows.",
                nome="John Marzluff"),
        ],
    },
    # 3 a dança das abelhas, decifrada e relativizada
    {
        "temas_secundarios": ["insetos", "luz_cores"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "A abelha que acha flores dança no favo: o ângulo da dança em relação ao \"para cima\" copia o ângulo da flor em relação ao Sol. Mas, num experimento, 93% das que seguiram a dança foram a lugares que já conheciam.",
        "explicacao": (
            "O austríaco Karl von Frisch foi um dos primeiros a decifrar a chamada dança do requebrado. A abelha "
            "percorre um oito: faz uma corrida reta requebrando, contorna de volta ao ponto de partida e repete. Nos "
            "favos verticais, dentro do ninho escuro, a corrida apontada para cima representa a direção do Sol, e um "
            "ângulo à direita ou à esquerda da vertical indica o mesmo ângulo em relação ao Sol. A distância vai na "
            "duração do requebrado: segundo von Frisch, cerca de um segundo para cada quilômetro. Abelhas que passam "
            "muito tempo dançando corrigem o ângulo conforme o Sol se move no céu. Von Frisch também concluiu que, "
            "sob nuvens, elas podem se guiar pelo padrão de luz polarizada do céu azul, invisível para nós. A teoria, descrita num livro de "
            "1927, enfrentou ceticismo e só décadas depois foi reconhecida; em 1973, von Frisch dividiu o Nobel de "
            "Fisiologia ou Medicina com Konrad Lorenz e Nikolaas Tinbergen. O quanto as abelhas usam essa informação, "
            "porém, segue em debate. Num experimento com a abelha-europeia, a maioria das que acompanharam a dança "
            "com atenção ignorou direção e distância, e 93% voltaram a áreas que já conheciam. As abelhas também "
            "acham comida pelo cheiro e pela memória, e a dança pesa mais quando o alimento é escasso."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Waggle_dance",
                "Austrian ethologist and Nobel laureate Karl von Frisch was one of the first who translated the meaning of the waggle dance. [...] "
                "A worker bee's waggle dance involves running through a small figure-eight pattern: a waggle run (aka waggle phase) followed by a turn to the right to circle back to the starting point [...] "
                "flowers that are located directly in line with the sun are represented by waggle runs in an upward direction on the vertical combs, and any angle to the right or left of the sun is coded by a corresponding angle to the right or left of the upward direction. "
                "The distance between hive and recruitment target is encoded in the duration of the waggle runs. [...] "
                "Waggle dancing bees that have been in the nest for an extended time adjust the angles of their dances to accommodate the changing direction of the sun. [...] "
                "Honeybees are able to successfully forage independently using olfactory cues and by remembering the location of previously rewarding food sites. [...] "
                "the waggle dance plays a significantly larger role in foraging when food sources are not as abundant. [...] "
                "the cavity-nesting bees are able to use gravity and orient their dances in their dark nests. [...] "
                "In an experiment on the honeybee Apis mellifera, most individuals who thoroughly followed a waggle dance ignored the resource direction and location information. "
                "Instead, 93% of the foragers returned to foraging areas they had previous knowledge of.",
                nome="Waggle dance"),
            wiki("Karl_von_Frisch",
                "Karl Ritter von Frisch (20 November 1886 – 12 June 1982) was a German-Austrian ethologist who received the Nobel Prize in Physiology or Medicine in 1973, along with Nikolaas Tinbergen and Konrad Lorenz. [...] "
                "His theory, described in his 1927 book [...] "
                "was disputed by other scientists and met with widespread skepticism at the time, only decades later being appreciated as both zoologically accurate [...] "
                "He discovered that bees can recognize the desired compass direction in three different ways: by the Sun, by the polarization pattern of the blue sky, and by the Earth's magnetic field, whereby the Sun is used as the main compass, with the alternatives reserved for the conditions arising under cloudy skies or within a dark beehive. "
                "Light scattered in a blue sky forms a characteristic pattern of partially polarized light which is dependent on the position of the Sun and invisible to human eyes. [...] "
                "The distance to the food source is relayed by the time taken to traverse the straight stretch, one second indicating a distance of approximately one kilometer",
                nome="Karl von Frisch"),
        ],
    },
    # 4 o enxame que escolhe a casa por "votação"
    {
        "temas_secundarios": ["insetos", "decisoes_economia"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Um enxame de abelhas sem casa escolhe o novo lar quase por votação: de 20 a 50 batedoras visitam ocos e fazem campanha dançando, e o enxame só parte quando um local reúne um quórum de apoiadoras.",
        "explicacao": (
            "O enxame é o jeito de uma colônia de abelhas se reproduzir: ela se divide em duas ou mais. Antes, as "
            "operárias param de alimentar a rainha, porque uma rainha em postura fica pesada demais para voos longos. "
            "Ao sair, o enxame não vai longe: pousa num galho a poucos metros e se aglomera em volta da rainha, "
            "enquanto de 20 a 50 batedoras procuram ocos adequados. Cada batedora que volta anuncia o local achado "
            "com a dança do requebrado, que indica direção, distância e qualidade, e quanto mais animada ela está, "
            "mais animada é a dança. Se convence outras, elas vão conferir e, se aprovarem, também passam a promover "
            "o local. No começo, vários candidatos disputam apoio; depois de horas, às vezes dias, um favorito vai "
            "emergindo. Há pressa: o enxame só aguenta cerca de três dias com o mel que levou no estômago. A decisão "
            "costuma sair quando há um quórum de 20 a 30 batedoras num mesmo local. Então o enxame inteiro decola e "
            "pode voar um quilômetro ou mais, guiado por batedoras que passam rápido por cima do grupo na direção "
            "certa. Esse processo coletivo costuma acertar o melhor local e manter o enxame unido."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Swarming_(honey_bee)",
            "Swarming is a honey bee colony's natural means of reproduction. In the process of swarming, a single colony splits into two or more distinct colonies. [...] "
            "A laying queen is too heavy to fly long distances. Therefore, the workers will stop feeding her before the anticipated swarm date and the queen will stop laying eggs. [...] "
            "When a honey bee swarm emerges from a hive they do not fly far at first. They may gather in a tree or on a branch only a few metres (yards) from the hive. "
            "There they cluster about the queen and send 20 to 50 scout bees out to find suitable new nest locations. [...] "
            "An individual scout returning to the cluster promotes a location she has found. She uses the waggle dance to indicate its direction, distance, and quality to others in the cluster. "
            "The more excited she is about her findings, the more excitedly she dances. "
            "If she can convince other scouts to check out the location she found, they take off, check out the proposed site, and choose to promote the site further upon their return. "
            "Several sites may be promoted by different scouts at first. After several hours and sometimes days, a favorite location gradually emerges from this decision-making process. "
            "In order for a decision to be made in a relatively short amount of time (the swarm can only survive for about three days on the honey on which they gorged themselves before leaving the hive), "
            "a decision will often be made when somewhere around 80% of the scouts have agreed upon a single location and/or when there is a quorum of 20–30 scouts present at a potential nest site. [...] "
            "When the scout bees agree where to nest, the whole clustered swarm takes off and flies to it. "
            "A swarm may fly a kilometer or more to the scouted location, with the scouts guiding the rest of the bees by quickly flying overhead in the proper direction. "
            "This collective decision-making process is remarkably successful in identifying the most suitable new nest site and keeping the swarm intact.",
            nome="Swarming (honey bee)")],
    },
    # 5 Santino, o chimpanzé que planejava ataques
    {
        "temas_secundarios": ["aprendizagem_inteligencia", "consciencia"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "No zoológico sueco de Furuvik, o chimpanzé Santino juntava pedras de manhã, calmo, antes de o público chegar, para atirá-las nos visitantes horas depois. Mais tarde, passou a escondê-las sob montes de feno.",
        "explicacao": (
            "Santino nasceu em 1978 no zoológico de Munique e foi levado aos cinco anos para Furuvik, na Suécia. Em "
            "1997, começou a recolher pedras do fosso em volta da ilha onde vivia e a guardá-las horas antes de "
            "atirá-las nos visitantes que chegavam, em exibições de dominância. Ao limpar a ilha, os tratadores "
            "acharam montes de pedras na margem voltada para o público, e uma tratadora escondida o viu empilhá-las "
            "pela manhã. A partir de 1998, ele também arrancava pedaços soltos do concreto para usar como projéteis. "
            "Chamou a atenção que ficasse calmo ao juntar as pedras e agitado só na hora dos arremessos, sinal de "
            "preparação para algo futuro. Em 2010, o pesquisador Mathias Osvath, da Universidade de Lund, e Elin "
            "Karvonen registraram uma novidade: Santino passou a cobrir projéteis com feno e a deixá-los atrás de "
            "troncos, perto dos visitantes, e se aproximava sem a exibição agressiva de costume antes de atirar. Das "
            "46 pedras recolhidas no período, 35 estavam escondidas. Há quem questione como interpretar esses dados. "
            "Para conter o comportamento, os tratadores castraram Santino. Ele morreu em 2022, baleado após fugir do "
            "recinto."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [
            {"url": EPMC + "PMC3348900/fullTextXML",
             "titulo": "Spontaneous innovation for future deception in a male chimpanzee (PLoS ONE, via Europe PMC)",
             "idioma": "en",
             "trecho": "The male chimpanzee, Santino, was born in 1978 at Munich Zoo in West Germany. At the age of five, he was transferred to Furuvik Zoo, Sweden [...] "
                       "In 1997 the chimpanzee started to gather stones from the water moat surrounding the outside compound and storing them hours before he threw them in dominance displays at the arriving zoo visitors. [...] "
                       "When cleaning the island compound, the zookeepers found five stone caches placed at the shoreline facing the visitors' area. "
                       "Following days a zookeeper placed herself in a blind to observe the chimpanzee behaviour during the morning hours. "
                       "He was found to retrieve stones from the moat and place them in piles. "
                       "In 1998, the chimpanzee started to manufacture projectiles by breaking off loose pieces from the compound's concrete surface [...] "
                       "calm during the gathering process, agitated during the throwing sessions [...] "
                       "he typically collected projectiles in the morning before the zoo opened [...] "
                       "manufactured concealments from hay, as well as used naturally occurring concealments. "
                       "All were placed near the visitors' observation area [...] "
                       "hiding projectiles and inhibiting dominance display behaviour [...] "
                       "This study was carried out in 2010 [...] "
                       "In all, 46 projectiles were recovered, of which 35 came from concealments. [...] "
                       "18 were placed behind logs [...] "
                       "concerns have been raised over how the findings should be interpreted"},
            wiki("Santino_(chimpanzee)",
                "Santino (20 April 1978 – 14 December 2022) was a male chimpanzee held at Furuvik Zoo in Sweden. [...] "
                "Dr. Mathias Osvath, a cognitive zoologist from Lund University, together with Elin Karvonen, studied the phenomenon [...] "
                "To control his behaviour, and keep his hormone levels down, zookeepers castrated Santino. [...] "
                "Santino was shot after escaping his enclosure in December 2022, and later died from his injuries.",
                nome="Santino (chimpanzee)"),
        ],
    },
    # 6 o polvo que carrega cascas de coco
    {
        "temas_secundarios": ["vida_marinha", "evolucao"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "Um polvo da Indonésia recolhe metades de casca de coco jogadas fora por humanos, carrega-as por até 20 metros e as encaixa em volta do corpo como abrigo. Pode ser o primeiro caso conhecido de ferramenta em invertebrados.",
        "explicacao": (
            "O polvo-do-coco (Amphioctopus marginatus) vive em águas tropicais do Pacífico ocidental e do Índico e "
            "prefere fundos de areia com muitas conchas ou lixo. Em 2009, pesquisadores do Museu de Melbourne, na "
            "Austrália, descreveram polvos dessa espécie, filmados em Bali e no norte de Sulawesi, recolhendo do fundo "
            "do mar metades de casca de coco descartadas por pessoas. Eles levavam as cascas por até 20 metros e "
            "depois as montavam em volta do corpo, formando um esconderijo esférico parecido com uma concha de "
            "molusco. Outros polvos já tinham sido vistos usando conchas para se esconder. A novidade foi juntar e "
            "transportar o material para usar mais tarde, o que o museu chamou de \"uso verdadeiro de ferramenta\". "
            "A espécie também se abriga em conchas de moluscos e até em garrafas. E tem outra esquisitice: é uma das "
            "duas únicas espécies de polvo conhecidas que andam sobre dois braços. Enquanto \"caminha\" com dois, usa os "
            "outros seis para se disfarçar, e os pesquisadores especularam que o disfarce imitaria um coco rolando."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Veined_octopus",
            "Amphioctopus marginatus, also known as the coconut octopus and veined octopus, is a medium-sized cephalopod found in the tropical waters of the western Pacific Ocean and the Indian Ocean. "
            "It prefers sandy substrates with plentiful shells or litter. "
            "It commonly preys upon shrimp, crabs, and clams, and displays unusual behavior for octopuses, being one of only two species known to exhibit bipedal walking. [...] "
            "This involves rolling two arms to walk while the other six arms are used to disguise itself; the researchers speculated that the disguise might be meant to mimic the appearance of a rolling coconut. [...] "
            "In 2009, researchers from the Melbourne Museum in Australia observed the coconut octopus using tools for concealment and defense by gathering available debris to create a shelter. "
            "The researchers filmed the octopus collecting coconut half-shells from the sea floor that had been discarded by humans. "
            "They were then carried up to 20 meters (66 ft) and arranged around the body of the octopus to form a spherical hiding place similar to a clamshell. "
            "This behavior was observed in specimen in Bali and North Sulawesi, Indonesia, and is likely the first evidence of tool use in invertebrates. "
            "Other species of octopus had been observed using shells for hiding, but this was the first case in which shells were prepared and collected for later use, in what the Melbourne Museum has described as \"true tool use\". [...] "
            "The coconut octopus has been observed using a variety of materials for shelter, including coconut shells, clamshells, and man-made litter such as bottles.",
            nome="Veined octopus")],
    },
    # 7 o pássaro-lira e a fama das motosserras
    {
        "temas_secundarios": ["musica_ciencia", "acustica"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "O pássaro-lira imita motosserras e obturadores de câmera, mas bem menos do que a fama sugere: no famoso trecho de Attenborough que mostra essas imitações, duas das três aves filmadas viviam em cativeiro.",
        "explicacao": (
            "Os pássaros-lira da Austrália são imitadores extraordinários. Reproduzem com fidelidade o canto de "
            "outras aves e o alarido de bandos, além de sons de gambás, coalas e dingos. Há registros deles imitando "
            "serrote, motosserra, motores e alarmes de carro, tiros, obturadores de câmera, cães latindo, bebês "
            "chorando, toques de celular e até a voz humana. Mas a imitação de ruídos humanos, embora muito "
            "divulgada, é exagerada. No episódio da série \"The Life of Birds\", de David Attenborough, um macho "
            "aparece imitando alarme de carro, motosserra e obturadores, só que duas das três aves mostradas eram de "
            "cativeiro. Partes do canto natural do pássaro-lira lembram efeitos sonoros, o que alimentou a lenda "
            "urbana de que eles imitam com frequência sons de videogames e filmes. As imitações humanas existem: a "
            "gravação de um pássaro-lira imitando um jogo eletrônico de tiro, operários e motosserras entrou em 2013 "
            "no registro Sounds of Australia, do arquivo nacional de som e imagem do país. Já a história de um "
            "pássaro-lira de estimação que, nos anos 1930, teria aprendido melodias de um flautista e as levado para "
            "a mata nunca foi comprovada: um grupo de pesquisa não conseguiu provar que a ave tinha sido de estimação."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Lyrebird",
                "Lyrebirds render with great fidelity the individual songs of other birds and the chatter of flocks of birds, and also mimic other animals, such as possums, koalas, and dingoes. "
                "Lyrebirds have been recorded mimicking human sounds such as a mill whistle, a cross-cut saw, chainsaws, car engines and car alarms, fire alarms, rifle-shots, camera shutters, dogs barking, crying babies, music, mobile-phone ring tones, and even the human voice. "
                "While the mimicry of human noises is widely reported, the extent to which it happens is exaggerated. "
                "Parts of the lyrebird's own song can resemble human-made sound effects, which has given rise to the urban legend that they frequently imitate video game or film sounds. [...] "
                "A recording of a superb lyrebird mimicking sounds of an electronic shooting game, workmen, and chainsaws was added to the National Film and Sound Archive's Sounds of Australia registry in 2013. [...] "
                "in the 1930s, a flute player living on a farm adjoining the park used to play tunes near his pet lyrebird. [...] "
                "However, a \"flute lyrebird\" research group (including Curtis and Fenton) formed to investigate the veracity of this story [...] "
                "Neither was able to prove that a lyrebird chick had been a pet",
                nome="Lyrebird"),
            wiki("Superb_lyrebird",
                "In David Attenborough's Life of Birds (ep. 6), the superb lyrebird is described as able to imitate twenty bird species' calls, and a male is shown mimicking a car alarm, chainsaw, and various camera shutters. "
                "However, two of the three lyrebirds featured were captive birds.",
                nome="Superb lyrebird"),
        ],
    },
    # 8 o drongo e os alarmes falsos
    {
        "temas_secundarios": ["teoria_jogos", "ecologia"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "Uma ave africana, o drongo, avisa outros bichos quando há predador. Mas às vezes dá alarme falso, até imitando o alarme deles, para que larguem a comida e ele a roube. E muda o grito quando a vítima para de acreditar.",
        "explicacao": (
            "O drongo-de-cauda-forcada (Dicrurus adsimilis) passa cerca de 29% do tempo seguindo outros animais que "
            "procuram comida no chão, como suricatos e uma ave chamada Turdoides bicolor. Ele costuma dar alarmes "
            "verdadeiros quando um predador aparece. Mas, quando vê um desses animais segurando comida, pode soltar "
            "um alarme falso: o alvo corre para se abrigar, larga o alimento e o drongo o pega. Um estudo de campo "
            "mostrou que os alarmes falsos podem ser do repertório do próprio drongo ou imitações do alarme "
            "de outras espécies, e que não diferem na estrutura dos alarmes verdadeiros. Em experimentos com "
            "gravações, suricatos e Turdoides caíram nos dois tipos. O problema de mentir é que a vítima aprende. Um "
            "estudo posterior confirmou que as espécies-alvo passam a reagir menos a um alarme falso repetido, mas "
            "mantêm o medo quando o chamado muda. E os drongos exploram justamente isso: trocam de tipo de alarme "
            "quando tentam roubar várias vezes da mesma espécie, driblando o limite que costuma tornar a mentira "
            "pouco vantajosa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            resumo("PMCID:PMC3081750",
                "Fork-tailed drongos use deceptive mimicked alarm calls to steal food (Proceedings of the Royal Society B, 2011, resumo via Europe PMC)",
                "Here, I show that wild fork-tailed drongos (Dicrurus adsimilis) make both drongo-specific and mimicked false alarm calls when watching target species handling food, in response to which targets flee to cover abandoning their food. "
                "The drongo-specific and mimicked calls made in false alarms were structurally indistinguishable from calls made during true alarms at predators by drongos and other species. "
                "Furthermore, I demonstrate by playback experiments that two of these species, meerkats (Suricata suricatta) and pied babblers (Turdoides bicolor), are deceived by both drongo-specific and mimicked false alarm calls."),
            resumo("EXT_ID:24786078%20AND%20SRC:MED",
                "Deception by flexible alarm mimicry in an African bird (Science, 2014, resumo via Europe PMC)",
                "Deception is common in nature, but victims of deception discriminate against and ultimately ignore deceptive signals when they are produced too frequently. [...] "
                "Fork-tailed drongos (Dicrurus adsimilis) use false alarm calls to scare other species away from food that they then steal. "
                "We show that drongos mimic the alarms of targeted species. "
                "Further, target species reduce their response to false alarm calls when they are repeated. "
                "However, the fear response is maintained when the call is varied. "
                "Drongos exploit this propensity by changing their alarm-call type when making repeated theft attempts on a particular species. "
                "Our results show that drongos can evade the frequency-dependent constraints that typically limit deception payoffs through flexible variation of their alarm calls."),
            wiki("Fork-tailed_drongo",
                "The drongo will give genuine alarm calls to signal the presence of predators to other animals, but occasionally, it will issue a false alarm call to displace those animals and steal their food. [...] "
                "It has been observed that fork-tailed drongos spend approximately 29% of their time trailing other animals. "
                "Species such as southern pied babblers, sociable weavers, wattled starlings and meerkats, which forage on the ground, are often targeted",
                nome="Fork-tailed drongo"),
        ],
    },
    # 9 o "centésimo macaco" que nunca existiu
    {
        "temas_secundarios": ["aprendizagem_inteligencia", "vieses_cognitivos"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "O \"efeito do centésimo macaco\", em que um hábito saltaria sozinho para ilhas vizinhas ao atingir massa crítica, é lenda. Os macacos japoneses que lavavam batata aprenderam devagar, e eram só 59 em 1962.",
        "explicacao": (
            "A história real começou na ilha japonesa de Koshima, onde, em 1952 e 1953, primatólogos deixavam "
            "batata-doce e trigo na praia para estudar um bando de macacos-japoneses. Em 1954, um artigo relatou que "
            "uma macaca, Imo, lavava as batatas na água. O hábito se espalhou aos poucos, primeiro entre os jovens e "
            "suas famílias, por observação e imitação; os mais velhos em geral não aprendiam, e a fração de lavadores "
            "cresceu à medida que eles morriam e nasciam filhotes. Imo inventou ainda um jeito de separar trigo da "
            "areia: jogava punhados na água e pegava os grãos que boiavam. Nos anos 1970, o escritor Lyall Watson "
            "transformou o caso numa parábola: ao chegar a um número crítico, o hábito teria passado de repente a "
            "macacos de ilhas vizinhas. Ken Keyes popularizou a versão num livro de 1984, e ela virou lenda da Nova "
            "Era. Em 1985, uma revisão dos relatórios originais concluiu que eles não sustentavam a história. Além "
            "disso, os bandos das várias ilhas tinham os pesquisadores em comum, e a colônia de Koshima somava 59 "
            "macacos em 1962: não havia nem um centésimo macaco. O estudo original continua útil para entender a "
            "transmissão cultural entre animais."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Hundredth_monkey_effect",
            "The hundredth monkey effect is an esoteric idea claiming that a new behavior or idea is spread rapidly by unexplained means from one group to all related groups once a critical number of members of one group exhibit the new behavior or acknowledge the new idea. [...] "
            "The \"hundredth monkey\" effect was popularized in the mid-to-late 1970s by Lyall Watson [...] "
            "Between 1952 and 1953, primatologists conducted a behavioral study of a troop of Macaca fuscata (Japanese macaque or snow monkeys) on the island of Kōjima. "
            "The researchers would supply these troops with such foods as sweet potatoes and wheat in open areas, often on beaches. [...] "
            "In 1954, a paper was published indicating the first observances of one monkey, Imo, washing her sweet potatoes in the water. [...] "
            "The young first teach their contemporaries and immediate family [...] "
            "The young monkey who started potato washing also learned how to sift wheat grains out of the sand by throwing handfuls of sand and wheat into the water, then catching the wheat that floated to the top. [...] "
            "This story was further popularized by Ken Keyes Jr. with the publication of his book The Hundredth Monkey (1984). [...] "
            "In 1985, Elaine Myers re-examined the original published research [...] "
            "she found that the original research reports by the Japan Monkey Centre in the 2nd, 5th, and 6th volumes of Primates were insufficient to support Watson's story. [...] "
            "The story as told by Watson and Keyes is popular among New Age authors and personal-growth gurus, as well as becoming an urban legend and part of New Age mythology. [...] "
            "The original research continues to prove useful in the study of cultural transmission in animals. [...] "
            "Claims that the practice spread suddenly to other isolated populations of monkeys may be called into question given the fact that the monkeys had the researchers in common. [...] "
            "Moreover, the number of monkeys in the colony was counted as 59 in 1962, indicating that even in numbers no \"hundredth monkey\" existed. [...] "
            "older monkeys who did not know how to wash tended not to learn. "
            "As the older monkeys died and younger monkeys were born the proportion of washers naturally increased.",
            nome="Hundredth monkey effect")],
    },
    # 10 a ave que guia caçadores de mel
    {
        "temas_secundarios": ["ecologia", "insetos"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "Na África, uma ave guia caçadores de mel até colmeias silvestres e depois come a cera que sobra. Em Moçambique, ela responde a um chamado tradicional dos caçadores, um \"brrrr-hmm\".",
        "explicacao": (
            "O indicador-grande (Indicator indicator), parente dos pica-paus, deve o nome ao hábito de guiar pessoas "
            "até ninhos de abelhas. Ele chama a atenção com notas trêmulas e tagarelas, voa na direção de uma colmeia "
            "ocupada (conhece a localização de muitas no seu território) e para perto dela. Os caçadores abrem a "
            "colmeia com fogo, fumaça e machados, e a ave come a cera que fica. A parceria rende aos humanos. Entre "
            "os boranas, do leste da África, a ajuda corta em cerca de dois terços o tempo de busca, e um assobio "
            "próprio para chamar a ave, o fuulido, dobra a chance de encontrá-la. No norte da Tanzânia, os "
            "indicadores aumentaram em 560% a taxa com que os hadzas achavam colmeias. No norte de Moçambique, um "
            "estudo com os caçadores yao mostrou que as aves respondem ao chamado tradicional \"brrrr-hmm\", que "
            "aumenta muito a chance de achar uma colmeia. Nem todos retribuem: os hadzas costumam queimar, enterrar "
            "ou esconder a cera, para manter a ave com fome e disposta a guiar de novo. E a ideia, repetida em muitas "
            "fontes, de que ela também guia o texugo-do-mel é contestada: os relatos em primeira mão são todos de "
            "guiadas incompletas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Greater_honeyguide",
            "The greater honeyguide (Indicator indicator) is a bird in the paleotropical family Indicatoridae, that is related to the woodpeckers. "
            "Its English and scientific names refer to its habit of guiding people to bee colonies. "
            "Claims that it also guides non-human animals are disputed. [...] "
            "A guiding bird attracts a person's attention with wavering, chattering \"'tya' notes compounded with peeps or pipes\", sounds it also gives in aggression. "
            "The guiding bird flies toward an occupied nest (greater honeyguides know the sites of many bees' nests in their territories) and then stops nearby the nest. "
            "Honey-hunters then do a final search for the bee colony, and if deemed suitable, harvest honey from the bee colony through the use of fire and smoke to subdue the bees, and axes and machetes to expose the colony. "
            "After harvesting the honey, the honeyguide eats wax that is left. "
            "One study found that use of honeyguides by the Boran people of East Africa reduces their search time for honey by approximately two-thirds. [...] "
            "The fuulido doubles the encounter rate with honeyguides. "
            "In northern Tanzania, Honeyguides increased the Hadza's rate of finding bee nests by 560% [...] "
            "Another study of the Yao honey-hunters in northern Mozambique showed that the honeyguides responded to the traditional brrrr-hmm call of the honey-hunters. "
            "The chances of finding a bee-hive were greatly increased when the traditional call was used. [...] "
            "The Hadza people of northern Tanzania frequently burn, bury, or hide the wax that lays with the intent of keeping the bird hungry, and more likely to guide again. [...] "
            "Many sources say that this species also guides honey badgers. [...] "
            "the first-hand accounts given in his review in support of this association are all of incomplete guiding sequences.",
            nome="Greater honeyguide")],
    },
    # 11 a guerra dos chimpanzés de Gombe
    {
        "temas_secundarios": ["evolucao", "psicologia_social"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Entre 1974 e 1978, Jane Goodall acompanhou uma \"guerra\" entre chimpanzés na Tanzânia: um grupo que se separou do bando original foi atacado até perder todos os machos. Muitos cientistas não acreditaram nela.",
        "explicacao": (
            "A comunidade Kasakela, estudada por Goodall em Gombe, foi se dividindo até que seis machos "
            "adultos, três fêmeas e seus filhotes passaram a viver no sul e formaram a comunidade Kahama. Em 7 de "
            "janeiro de 1974, seis machos Kasakela emboscaram Godi, um macho Kahama que comia sozinho numa árvore, e "
            "o espancaram até ele parar de se mexer; ele provavelmente morreu pouco depois. Foi a primeira vez que se "
            "viu machos de chimpanzé tentarem deliberadamente matar outro macho. Vieram outros ataques, e em quatro "
            "anos todos os machos Kahama foram mortos ou desapareceram. Os vencedores tomaram o território, mas logo o "
            "perderam para comunidades vizinhas mais numerosas. Goodall, que via os chimpanzés como \"mais "
            "bonzinhos\" que os humanos, ficou chocada. O relato não foi aceito por todos: houve quem a acusasse de "
            "antropomorfismo e quem dissesse que a presença dela, e o hábito de alimentar os animais, tinham criado "
            "o conflito. Pesquisas posteriores, com métodos menos invasivos, confirmaram que chimpanzés na natureza "
            "fazem guerra. Um estudo de 2018 atribuiu o conflito a uma disputa de poder entre três machos de alto "
            "escalão, agravada pela falta de fêmeas férteis."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Gombe_Chimpanzee_War",
            "The Gombe Chimpanzee War, also known as the Four-Year War, was a violent conflict between two communities of chimpanzees in Gombe Stream National Park in the Kigoma region of Tanzania between 1974 and 1978. "
            "The two groups were once unified in the Kasakela community. [...] "
            "a large party of chimpanzees separated themselves into the southern area of Kasakela and were renamed the Kahama community. "
            "The separatists consisted of six adult males, three adult females and their young. [...] "
            "During the four-year conflict, all males of the Kahama community were killed, effectively disbanding the community. "
            "The victorious Kasakela then expanded into further territory but were later repelled by two other communities of chimpanzees. [...] "
            "First blood was drawn by the Kasakela community on 7 January 1974, when a party of six adult Kasakela males consisting of Humphrey, Figan, Jomeo, Sherry, Evered, and Rodolf ambushed the isolated Kahama male Godi while he was feeding on a tree. [...] "
            "the attackers seized him, threw him on the ground and beat him until he stopped moving. [...] "
            "but probably died of his injuries soon after. "
            "This was the first time male chimpanzees had been seen to deliberately attempt to kill a fellow male chimpanzee. [...] "
            "After Charlie's death, Willy Wally disappeared and was never found. [...] "
            "Cowed by the superior strength and numbers of the Kalande [...] "
            "The outbreak of the war shocked her, as she had previously considered chimpanzees to be, although similar to human beings, \"rather 'nicer'\". [...] "
            "When Goodall reported on the events of the Gombe War, her account of a naturally occurring war between chimpanzees was not universally believed. [...] "
            "Some scientists accused her of excessive anthropomorphism; others suggested that her presence, and her practice of feeding the chimpanzees, had created violent conflict in a naturally peaceful society. "
            "However, later research using less intrusive methods confirmed that chimpanzee societies, in their natural state, indeed wage war. "
            "A 2018 study published in the American Journal of Physical Anthropology concluded that the Gombe War was most likely a consequence of a power struggle between three high-ranking males, which was exacerbated by an unusual scarcity of fertile females.",
            nome="Gombe Chimpanzee War")],
    },
    # 12 pombos que separam Picasso de Monet
    {
        "temas_secundarios": ["pintura", "percepcao_ilusoes"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Pombos treinados aprenderam a distinguir quadros de Picasso e de Monet e acertaram até telas que nunca tinham visto. Com os Monet de cabeça para baixo, porém, eles se confundiam; com os cubistas invertidos, não.",
        "explicacao": (
            "O experimento foi descrito num artigo de 1995 por Watanabe, Sakamoto e Wakita. Os pombos foram "
            "treinados primeiro com um conjunto limitado de pinturas. Diante de um Picasso, bicar repetidamente "
            "rendia comida; diante de um Monet, bicar não adiantava nada. Com o tempo, as aves passaram a bicar só "
            "quando viam um Picasso. Depois, generalizaram: separavam corretamente quadros dos dois pintores que "
            "ainda não tinham visto e até pinturas cubistas e impressionistas, as duas escolas a que Picasso e Monet "
            "pertencem. O detalhe mais curioso veio quando as telas foram viradas: com os Monet de ponta-cabeça, os "
            "pombos deixaram de classificá-los direito, mas inverter as obras cubistas não teve esse efeito. O "
            "trabalho rendeu aos autores o Ig Nobel de Psicologia de 1995, paródia do Nobel que premia feitos que "
            "\"primeiro fazem rir e depois fazem pensar\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Pigeon_intelligence",
                "In an article from 1995, Watanabe, Sakamoto, and Wakita described an experiment which showed that pigeons can be trained to discriminate between paintings by Picasso and by Monet. "
                "The birds were first trained on a limited set of paintings. "
                "The experiment has shown that a pigeon was able to obtain food by repeated pecking when shown a painting from Picasso; when it was a Monet, pecking had no effect. "
                "After a while, the pigeons would only peck when shown Picasso paintings. "
                "They were then able to generalize and correctly discriminate between paintings of the two painters not previously shown, and even between cubist and impressionist paintings (cubism and impressionism being the two stylistic schools Picasso and Monet belong to). "
                "When the Monet paintings were shown upside down, the pigeons were not able to properly categorize anymore. "
                "Showing the cubist works upside down did not have such an effect. "
                "In 1995, the authors won the Ig Nobel Prize in psychology for this work.",
                nome="Pigeon intelligence"),
            wiki("List_of_Ig_Nobel_Prize_winners",
                "A parody of the Nobel Prizes, the Ig Nobel Prizes are awarded each year in mid-September, around the time the recipients of the genuine Nobel Prizes are announced, for ten achievements that \"first make people laugh, and then make them think\".",
                nome="List of Ig Nobel Prize winners"),
        ],
    },
    # 13 golfinhos com "nome" próprio
    {
        "temas_secundarios": ["linguas_mundo", "vida_marinha"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Cada golfinho-nariz-de-garrafa cria, no primeiro ano de vida, um assobio só seu, que funciona quase como um nome. Outros golfinhos o reconhecem até sem o timbre da voz e lembram dele depois de mais de 20 anos.",
        "explicacao": (
            "O assobio-assinatura é um tipo de assobio aprendido e individual que identifica quem o emite, e é tido "
            "como o sinal mais parecido com um nome já encontrado em animais não humanos. O filhote o constrói a "
            "partir dos sons que ouve, em geral de modo que fique diferente dos assobios de companheiros próximos. "
            "Costuma estar pronto no primeiro ano de vida e muda pouco na idade adulta; nas fêmeas, não se viu "
            "mudança depois de formado. Os golfinhos o usam muito quando o grupo se separa e para se apresentar ao "
            "encontrar outros grupos. Num estudo, eles reconheceram a identidade de quem assobiava mesmo com as "
            "características da voz removidas do som. Também copiam o assobio de outros, algo raro e mais comum entre "
            "golfinhos com laços próximos. Há até algo parecido com o jeito de falar com bebês: num acervo de "
            "gravações de Sarasota, nos EUA, as 19 mães analisadas alteravam o próprio assobio quando o filhote estava "
            "perto, subindo a frequência ou ampliando a faixa. Outros estudos mostram que golfinhos lembram o assobio "
            "de antigos companheiros depois de mais de duas décadas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Signature_whistle",
            "A signature whistle is a learned, individually distinctive whistle type in a bottlenose dolphin's (Tursiops truncatus) acoustic repertoire that gives the identity of the whistle owner. [...] "
            "More often than not, calves develop signature whistles by the sounds they hear while making sure that they differ from close associates. "
            "They are believed to be the most name-like signal found, so far, in non-human animals [...] "
            "Researchers define signature whistles as unique calls given most frequently during periods of group separation [...] "
            "A dolphin's signature whistle development is influenced by auditory experience, and usually fully develops within the first year of life, rarely changing throughout adulthood. [...] "
            "Females, by contrast, have not been found to alter their signature whistle after development. [...] "
            "In all 19 cases, the mother dolphin inflected the signature whistle when their calf was present, by reaching a higher frequency, or using a wider frequency range. [...] "
            "Dolphins also use signature whistles to provide identity information when meeting new groups of dolphins. [...] "
            "Janik et al. demonstrate that bottlenose dolphins are able to recognize identity from signature whistles even with voice features removed [...] "
            "dolphins have been shown to remember other dolphins after over 20 years without contact, just from their whistles. [...] "
            "Although this behavior is rare, dolphins with close relationships are more likely to demonstrate vocal copying.",
            nome="Signature whistle")],
    },
    # 14 golfinhos que caçam com esponja no focinho
    {
        "temas_secundarios": ["vida_marinha", "evolucao"],
        "tipos_espanto": ["engenhosidade", "origem_inesperada"],
        "gancho": "Em Shark Bay, na Austrália, alguns golfinhos arrancam esponjas do fundo e as vestem no focinho para caçar peixes enterrados. O truque parece passar de mãe para filho: quem o usa descende de uma só linhagem materna.",
        "explicacao": (
            "Numa comunidade de golfinhos-nariz-de-garrafa-do-indo-pacífico em Shark Bay, no oeste da Austrália, um "
            "grupo de cerca de 41 a 54 animais usa esponjas marinhas cônicas como ferramenta. O golfinho arranca a "
            "esponja e a encaixa sobre o rostro, o \"bico\", enquanto vasculha o fundo. Os alvos são sobretudo peixes "
            "sem bexiga natatória que se enterram no sedimento, um nicho em que a ecolocalização e a visão funcionam "
            "mal; a esponja protegeria o focinho. O hábito costuma começar no segundo ano de vida, e o golfinho "
            "carrega a mesma esponja por várias subidas à superfície. Há custos: os usuários de esponja são mais "
            "solitários, mergulham mais fundo e passam mais tempo caçando, mas criam filhotes com o mesmo sucesso que "
            "os demais. O comportamento é muito mais comum em fêmeas, e análises genéticas sugerem que todos os que o "
            "praticam descendem de uma única linhagem materna, sinal de transmissão cultural, provavelmente aprendida "
            "de mãe para filhote. Até hoje, só foi visto em Shark Bay, onde alguns golfinhos também usam conchas de "
            "búzio para tirar peixes do fundo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Tool_use_by_animals",
            "A community of Indo-Pacific bottlenose dolphins (Tursiops sp.) in Shark Bay, Western Australia, made up of approximately 41-54 animals, are known to use conical sponges (Echinodictyum mesenterinum) as tools while foraging. "
            "This behaviour, termed \"sponging\", occurs when a dolphin breaks off a sponge and wears it over its rostrum while foraging on the seafloor. "
            "Sponging behaviour typically begins in the second year of life. "
            "During sponging, dolphins mainly target fish that lack swim bladders and burrow in the substrate. "
            "Therefore, the sponge may be used to protect their rostrums as they forage in a niche where echolocation and vision are less effective hunting techniques. "
            "Dolphins tend to carry the same sponge for multiple surfacings but sometimes change sponges. "
            "Spongers typically are more solitary, take deeper dives, and spend more time foraging than non-spongers. "
            "Despite these costs, spongers have similar calving success to non-spongers. [...] "
            "Sponging is heavily sex-biased to females. "
            "Genetic analyses suggest that all spongers are descendants of a single matriline, suggesting cultural transmission of the use of sponges as tools. "
            "Sponging may be socially learned from mother to offspring. [...] "
            "Sponging has only been observed in Shark Bay. "
            "Indo-Pacific bottlenose dolphins in Shark Bay have also been observed carrying conch shells. [...] "
            "Dolphins appear to use the conch shells to scoop fish from the substrate",
            nome="Tool use by animals")],
    },
    # 15 os alarmes "descritivos" dos cães-da-pradaria
    {
        "temas_secundarios": ["estruturas_linguisticas", "ecologia"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "Segundo o biólogo Con Slobodchikoff, o alarme dos cães-da-pradaria diz que predador vem, de que tamanho e cor é e a que velocidade. A colônia reage de jeitos diferentes a falcão, humano, coiote ou cachorro.",
        "explicacao": (
            "Os cães-da-pradaria são roedores que cavam tocas nos campos da América do Norte. Eles enxergam "
            "predadores de longe e avisam os vizinhos com um chamado agudo. Slobodchikoff e outros pesquisadores "
            "defendem que esses chamados formam um sistema sofisticado: segundo ele, trazem informação sobre o tipo "
            "de predador, o tamanho, a cor e a velocidade com que se aproxima, o que já foi descrito como uma forma de "
            "gramática. Ele afirma ainda que os animais têm chamados para coisas que nem são predadores, e vê nisso "
            "sinal de uma linguagem muito descritiva. O que se observa "
            "é que os alarmes variam com o predador, e as reações também. Se o aviso é de um falcão mergulhando, os "
            "que estão na rota de voo se jogam nas tocas, e os de fora ficam de pé olhando. Para humanos, a colônia "
            "toda corre para dentro na hora. Para coiotes, os animais vão até a entrada da toca e ficam vigiando, e "
            "os que estavam lá dentro saem para olhar. Para cachorros domésticos, ficam parados onde estavam, "
            "observando."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Prairie_dog",
            "Prairie dogs (genus Cynomys) are herbivorous burrowing ground squirrels native to the grasslands of North America. [...] "
            "Prairie dogs are stout-bodied rodents [...] "
            "Using its dichromatic color vision, it can detect predators from a great distance; it then alerts other prairie dogs of the danger with a special, high-pitched call. "
            "Con Slobodchikoff and others assert that prairie dogs use a sophisticated system of vocal communication to describe specific predators. "
            "According to him, prairie dog calls contain specific information as to what the predator is, how big it is, what color it is and how fast it is approaching. "
            "These have been described as a form of grammar. [...] "
            "He also writes that prairie dogs have calls for things that are not predators to them. "
            "This is cited as evidence that the animals have a very descriptive language and have calls for any potential threat. "
            "The prairie dog's alarm calls vary with different predators. [...] "
            "Alarm response behavior varies according to the type of predator announced. "
            "If the alarm indicates a hawk diving toward the colony, all the prairie dogs in its flight path dive into their holes, while those outside the flight path stand and watch. "
            "If the alarm is for a human, all members of the colony immediately rush inside the burrows. "
            "For coyotes, the prairie dogs move to the entrance of a burrow and stand outside the entrance, observing the coyote, while those prairie dogs that were inside the burrows come out to stand and watch, as well. "
            "For domestic dogs, the response is to observe, standing in place where they were when the alarm was sounded",
            nome="Prairie dog")],
    },
    # 16 elefantes que reconhecem vozes de masais
    {
        "temas_secundarios": ["sentidos", "linguas_mundo"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Elefantes do Quênia reconhecem vozes humanas: ao ouvir homens masais falando, eles se agrupam em defesa e farejam o ar. Vozes de mulheres e meninos masais, que oferecem pouco perigo, os assustam bem menos.",
        "explicacao": (
            "Num estudo de campo, pesquisadores tocaram gravações de vozes humanas para famílias de "
            "elefantes-africanos livres no Parque Nacional de Amboseli, no Quênia. As vozes eram de dois grupos "
            "étnicos que representam níveis diferentes de ameaça para os animais. Ao ouvir falas de masais, os "
            "elefantes ficaram bem mais propensos a se juntar num agrupamento defensivo e a farejar para investigar. "
            "A reação dependia também de quem falava: vozes de mulheres e meninos masais, que em geral oferecem pouco "
            "risco, provocaram essas respostas com frequência bem menor. Ou seja, os elefantes distinguiam pela voz "
            "não só a etnia, mas também o sexo e a idade de quem falava. Outros animais já tinham mostrado que "
            "separam categorias de pessoas pela visão ou pelo cheiro, mas a voz pode carregar muito mais "
            "informação. Os autores sugerem que, dada a longa história de ameaça humana à fauna, a capacidade de "
            "reconhecer pela voz quem é perigoso pode ter sido favorecida também em outras espécies de cognição "
            "avançada."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [resumo("PMCID:PMC3986134",
            "Elephants can determine ethnicity, gender, and age from acoustic cues in human voices (PNAS, 2014, resumo via Europe PMC)",
            "Although a number of prey species have proved able to discriminate between certain human categories on the basis of visual and olfactory cues, vocalizations potentially provide a much richer source of information. "
            "We now use controlled playback experiments to investigate whether family groups of free-ranging African elephants (Loxodonta africana) in Amboseli National Park, Kenya can use acoustic characteristics of speech to make functionally relevant distinctions between human subcategories differing not only in ethnicity but also in sex and age. "
            "Our results demonstrate that elephants can reliably discriminate between two different ethnic groups that differ in the level of threat they represent, significantly increasing their probability of defensive bunching and investigative smelling following playbacks of Maasai voices. "
            "Moreover, these responses were specific to the sex and age of Maasai presented, with the voices of Maasai women and boys, subcategories that would generally pose little threat, significantly less likely to produce these behavioral responses. "
            "Considering the long history and often pervasive predatory threat associated with humans across the globe, it is likely that abilities to precisely identify dangerous subcategories of humans on the basis of subtle voice characteristics could have been selected for in other cognitively advanced animal species.")],
    },
    # 17 ratos que libertam o companheiro: empatia ou vontade de companhia?
    {
        "temas_secundarios": ["emocoes", "experimentos_psicologia"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "Num experimento, ratos aprenderam a abrir um tubo para libertar um companheiro preso e, em geral, dividiram com ele um chocolate. Empatia? Outros pesquisadores acham que o motivo é só a vontade de ter companhia.",
        "explicacao": (
            "O estudo colocava um rato solto numa arena com um companheiro de gaiola preso num tubo que só abria por "
            "fora. Depois de algumas sessões, o rato livre aprendeu a abrir o tubo de propósito e depressa. Ele não "
            "abria tubos vazios nem com objetos dentro, e libertava o companheiro mesmo quando o contato social entre "
            "os dois era impedido. Quando um segundo tubo guardava chocolate, os ratos abriam os dois e em geral "
            "dividiam o doce. Os autores viram aí forte evidência de raízes biológicas para a ajuda motivada por "
            "empatia. A interpretação é contestada. Num estudo posterior, seis ratos num labirinto preferiram libertar "
            "um rato preso a entrar numa caixa vazia, mas não mostraram preferência entre soltar um rato preso e "
            "soltar outro cujo tubo não estava trancado. E preferiram a caixa com um rato num tubo aberto à caixa "
            "vazia. Para esses pesquisadores, o que move os ratos é o valor do contato social, e não a empatia. A "
            "pergunta sobre o que motiva esse comportamento continua em debate."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            resumo("EXT_ID:22158823%20AND%20SRC:MED",
                "Empathy and pro-social behavior in rats (Science, 2011, resumo via Europe PMC)",
                "To test for empathically motivated pro-social behavior in rodents, we placed a free rat in an arena with a cagemate trapped in a restrainer. "
                "After several sessions, the free rat learned to intentionally and quickly open the restrainer and free the cagemate. "
                "Rats did not open empty or object-containing restrainers. "
                "They freed cagemates even when social contact was prevented. "
                "When liberating a cagemate was pitted against chocolate contained within a second restrainer, rats opened both restrainers and typically shared the chocolate. "
                "Thus, rats behave pro-socially in response to a conspecific's distress, providing strong evidence for biological roots of empathically motivated helping behavior."),
            resumo("EXT_ID:30047125%20AND%20SRC:MED",
                "Does a rat free a trapped rat due to empathy or for sociality? (2018, resumo via Europe PMC)",
                "This report evaluates whether a rat releasing a trapped rat from a restraint tube is better explained as due to its empathic motivation or to the pursuit of social contact. "
                "In the first condition, each of six rats chose in an E maze between entering an empty goal box versus entering a goal box where its entrance caused a rat trapped in a restraint tube to be released. "
                "Rats preferred the goal box with the trapped rat over the empty goal box. "
                "In the second condition, these rats chose between releasing a restraint-tube-trapped rat in one goal box and another rat in the second goal box that was not locked into its restraint tube. "
                "Rats showed no preference between alternatives. "
                "In the third condition, rats chose between a goal box containing a rat with an open restraint tube and an empty goal box. "
                "Rats preferred the rat with the open restraint tube over the empty goal box. "
                "These results support attributing the response of releasing a rat from a restraint tube to the reinforcing power of social contact rather than interpreting this response as empathically motivated."),
        ],
    },
]
