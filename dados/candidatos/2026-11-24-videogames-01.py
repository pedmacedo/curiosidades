LOTE = "2026-11-24-videogames-01"
AREA = "esportes_jogos"
TEMA = "videogames"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Tennis for Two: o jogo do laboratório nuclear
    {
        "temas_secundarios": ["historia_computacao", "invencoes"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Em 1958, o físico que chefiara a eletrônica do Projeto Manhattan criou um jogo de tênis num laboratório nuclear dos EUA, para animar a visita do público. Depois o desmontou, e o jogo caiu no esquecimento.",
        "explicacao": (
            "William Higinbotham dirigia a divisão de instrumentação do Laboratório Nacional de Brookhaven, em Nova "
            "York. Antes, de 1943 a 1945, tinha chefiado a divisão de eletrônica do Projeto Manhattan. Uma vez por ano, "
            "o laboratório recebia o público, e a exposição era quase só visitas guiadas e painéis parados. Lendo o "
            "manual de um computador analógico da casa, ele descobriu que a máquina calculava a trajetória de uma bola "
            "quicando, com resistência do ar, e resolveu transformar isso num jogo. Projetou-o em poucas horas e o "
            "montou em três semanas com o técnico Robert Dvorak. Na tela de um osciloscópio de 5 polegadas, a quadra "
            "aparecia vista de lado; cada jogador tinha um controle de alumínio, com um botão para rebater e um botão "
            "giratório para escolher o ângulo. Centenas de visitantes fizeram fila. Na versão de 1959 dava até para "
            "jogar com a gravidade da Lua ou de Júpiter. Depois disso, as peças foram reaproveitadas. O jogo só voltou "
            "à tona no fim dos anos 1970, quando advogados tentaram usá-lo, sem sucesso, para derrubar patentes de "
            "videogame. Higinbotham não achava que ele merecesse patente: preferia ser lembrado pelo trabalho contra a "
            "proliferação nuclear, e foi o primeiro presidente da Federação de Cientistas Americanos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Tennis_for_Two",
                "The game was displayed on an oscilloscope and played with two custom aluminum controllers. [...] "
                "In 1958, American physicist William Higinbotham worked in the Brookhaven National Laboratory in Upton, New York, as the head of the instrumentation division. [...] "
                "He served as the head of the electronics division of the Manhattan Project from 1943 to 1945, and began working at Brookhaven in 1947, which focused on researching peaceful uses of atomic power. [...] "
                "Once a year, the government research facility held an exhibition for the public [...] "
                "The exhibition largely consisted of tours and static displays [...] "
                "While reading the instruction manual for one of Brookhaven's computers, a Donner Model 30 analog computer, he learned that the computer could calculate ballistic missile trajectories or a bouncing ball with wind resistance, and he decided to use this ability to form the foundation of a game. [...] "
                "Higinbotham designed a game that used an oscilloscope to display the path of a simulated ball on a tennis court viewed from the side. [...] "
                "Pressing the button hit the ball, and turning the knob controlled the angle of the shot. [...] "
                "The device was designed in a few hours and was assembled over three weeks with the help of technician Robert V. Dvorak. [...] "
                "5-inch oscilloscope [...] "
                "Hundreds of visitors lined up to play the new game during its debut. [...] "
                "Players could set the game to simulate the gravity levels of the Moon or Jupiter. [...] "
                "After the 1959 exhibition, the game was dismantled so its components could be put to other uses. [...] "
                "It remained virtually unknown until the late 1970s and early 1980s when Higinbotham was called on to testify in court cases for defendants sued by Magnavox over the video game patents of Ralph H. Baer. "
                "Having discovered the game, the lawyers for the defense unsuccessfully attempted to have the game declared prior art to invalidate Baer's patents on television video games [...] "
                "Higinbotham himself felt that the game was an obvious extension of the Donner Model 30's bouncing ball program and therefore not worthy of patenting or a large part of his legacy; he preferred to be remembered for his post-World War II nuclear non-proliferation work.",
                nome="Tennis for Two"),
            {"url": "https://www.bnl.gov/about/history/firstvideo.php",
             "titulo": "The First Video Game? (Brookhaven National Laboratory)", "idioma": "en",
             "trecho": "The game's creator, William Higinbotham, was a physicist who lobbied for nuclear nonproliferation as the first chair of the Federation of American Scientists."},
        ],
    },
    # 2 Spacewar!: a desculpa da trigonometria e o "Planetário Caro"
    {
        "temas_secundarios": ["historia_computacao", "estrelas"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "O Spacewar!, jogo criado em 1962 no MIT, ganhou um fundo com as estrelas reais do céu, copiadas de cartas celestes. E o autor só o programou porque um colega foi buscar a rotina de cálculo que ele usava como desculpa.",
        "explicacao": (
            "O jogo foi feito para o PDP-1, computador recém-chegado ao MIT: duas naves duelam enquanto são puxadas "
            "pela gravidade de uma estrela. Steve Russell tinha a ideia, mas não pretendia programá-la, e os colegas o "
            "pressionavam. Ele dava desculpas, e uma delas era a falta de uma rotina de funções trigonométricas para "
            "calcular as trajetórias. Alan Kotok ligou para a DEC, fabricante do computador, que já tinha a rotina "
            "pronta; foi de carro buscar a fita, largou-a na frente de Russell e perguntou que outras desculpas ele "
            "tinha. Sem saída, Russell começou a programar. O primeiro fundo de estrelas era aleatório, e a falta de "
            "realismo irritava Peter Samson, que escreveu um programa baseado em cartas celestes reais, com as "
            "estrelas até a quinta magnitude de uma faixa do céu, cada uma com seu brilho relativo. O apelido era "
            "\"Planetário Caro\", por causa do preço do computador. Os jogadores também sofriam com as chaves do painel, "
            "que se gastavam e às vezes faziam alguém desligar a máquina sem querer; Bob Saunders construiu então um "
            "controle separado, um antepassado do gamepad. O código circulava livremente, e o jogo se espalhou para "
            "outras instituições que tinham um PDP-1. Segundo um relato de segunda mão, técnicos da DEC o rodavam para "
            "testar computadores novos, porque ele exercitava todo o hardware."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Spacewar!",
            "Spacewar! is a space combat video game developed in 1962 by Steve Russell in collaboration with Martin Graetz, Wayne Wiitanen, Bob Saunders, Steve Piner, and others. "
            "It was written for the newly installed DEC PDP-1 minicomputer at the Massachusetts Institute of Technology. [...] "
            "The game features two spaceships, \"the needle\" and \"the wedge\", engaged in a dogfight while maneuvering in the gravity well of a star. [...] "
            "Russell hoped someone would implement the game, but had no plans to do so himself. "
            "Other members of the community felt he was the logical choice to create the game, however, and began pressuring him to program it. "
            "In response, Russell began providing various excuses as to why he could not do so. "
            "One of these was the lack of a trigonometric function routine needed to calculate the trajectories of the spacecraft. "
            "This prompted Alan Kotok of the TMRC to call DEC, who informed him that they had such a routine already written. "
            "Kotok drove to DEC to pick up a tape containing the code, slammed it down in front of Russell, and asked what other excuses he had. "
            "Russell, later explaining that \"I looked around and I didn't find an excuse, so I had to settle down and do some figuring\", started writing the code [...] "
            "whereby all programs were freely shared and modified by other programmers [...] "
            "That early version also contained a randomly generated background star field [...] "
            "since the inaccuracy and lack of realism in the starfield annoyed TMRC member Peter Samson, he wrote a program based on real star charts that scrolled slowly through the night sky, including every star in a band between 22.5° N and 22.5° S down to the fifth magnitude, displayed at their relative brightness. "
            "The program was called \"Expensive Planetarium\"—referring to the high price of the PDP-1 computer compared to an analog planetarium [...] "
            "these were controlled using the front-panel test switches on the PDP-1 minicomputer, with four switches for each player, but these proved to be awkward to use and wore out quickly under normal gameplay, as well as causing players to accidentally flip the computer's control and power switches. [...] "
            "To alleviate these problems, Saunders created a detached control device, essentially an early gamepad. [...] "
            "they spread the game to other universities and institutions with a PDP-1 computer. [...] "
            "According to a second-hand account heard by Russell while working at DEC, Spacewar! was reportedly used as a smoke test by DEC technicians on new PDP-1 systems before shipping because it was the only available program that exercised every aspect of the hardware.",
            nome="Spacewar!")],
    },
    # 3 Space Invaders acelera porque o processador desenha menos
    {
        "temas_secundarios": ["historia_computacao"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "No Space Invaders, de 1978, os alienígenas aceleram à medida que você os abate. Não foi planejado: com menos alienígenas, o processador desenhava cada quadro mais depressa, e o criador decidiu manter o efeito.",
        "explicacao": (
            "Tomohiro Nishikado passou um ano projetando o jogo e o próprio hardware para rodá-lo, e mesmo assim a "
            "placa não tinha força para mostrar cores nem para mover os inimigos mais rápido. Programando, ele percebeu "
            "uma coisa: quanto menos alienígenas havia na tela, mais depressa o processador conseguia desenhar cada "
            "quadro da animação. Como a posição dos alienígenas avançava a cada quadro, eles iam ficando mais velozes "
            "conforme eram destruídos, e o som que acompanha a marcha acelerava junto. Em vez de compensar a diferença, "
            "Nishikado deixou o efeito como mecânica do jogo. Mais tarde, disse que isso tornou o jogo mais "
            "interessante e compensou as limitações da máquina. Não foi o único defeito que virou parte do jogo: os "
            "tiros dos invasores não atingiam o canhão quando ele estava muito perto deles. A Taito poderia corrigir, "
            "mas trocar a memória das máquinas já espalhadas ficou caro demais com o sucesso do jogo, e os jogadores "
            "adotaram o erro como estratégia, que ganhou o nome de \"tiro de Nagoya\". Shigeru Miyamoto, criador do "
            "Mario, considera o Space Invaders o videogame mais revolucionário e diz que foi ele que o levou a seguir a "
            "carreira."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Space_Invaders",
            "Space Invaders is a 1978 fixed shooter video game developed and published by Taito for arcades. [...] "
            "Tomohiro Nishikado, who spent a year designing it and developing the necessary hardware to produce it. [...] "
            "the Control Program board was not powerful enough to display the graphics in color or move the enemies faster [...] "
            "While programming, Nishikado discovered that the processor was able to render each frame of the alien's animation graphics faster when there were fewer aliens on the screen. "
            "Since the alien's positions updated after each frame, this caused the aliens to move across the screen at an increasing speed as more were destroyed; the accompanying audio sped up as well. "
            "Rather than design a compensation for the speed increase, he decided to keep this undocumented feature as a gameplay mechanism. "
            "In retrospect, Nishikado noted that this aspect made the game more interesting and compensated for the hardware's limitations. [...] "
            "A gameplay bug was discovered that prevented the invaders' attacks from harming the laser cannon at very close range. "
            "Although a programming fix was possible, Taito's management decided against a second ROM replacement; by then, the game's wide-spread popularity made it cost prohibitive. "
            "Players eventually adopted the bug as a strategy and named it \"Nagoya shooting\" and \"Wall of Death\". [...] "
            "Shigeru Miyamoto, the longtime general manager of Nintendo Entertainment Analysis & Development, considers Space Invaders the most revolutionary video game. [...] "
            "Miyamoto—the creator of Donkey Kong, Mario, and The Legend of Zelda—commented that the game incited his interest in video games, leading him to pursue it as a profession.",
            nome="Space Invaders")],
    },
    # 4 o mito da falta de moedas de 100 ienes
    {
        "temas_secundarios": ["dinheiro", "economia_curiosa"],
        "tipos_espanto": ["mito_desmentido"],
        "gancho": "Conta-se que o Space Invaders causou falta de moedas de 100 ienes no Japão. Numismatas compararam a produção da Casa da Moeda japonesa com a renda do jogo e não acharam sinal disso.",
        "explicacao": (
            "A história é plausível à primeira vista: até o fim de 1978, o jogo já tinha rendido à Taito o equivalente "
            "a 670 milhões de dólares só no Japão. Mas os relatos de "
            "colecionadores de moedas que viviam no Japão na época não indicam nada fora do normal quando o jogo foi "
            "lançado, e o próprio criador, Tomohiro Nishikado, se disse cético. O numismata Mark Fox comparou a "
            "produção da Casa da Moeda do Japão naqueles anos com o faturamento informado do jogo e concluiu que o "
            "Space Invaders não alterou a produção. Ele lembrou também que os donos de fliperama esvaziavam as máquinas "
            "com frequência, o que mantinha as moedas circulando, e atribuiu o mito à produção menor de moedas de 100 "
            "ienes em 1978 e 1979. Escrevendo na revista The Numismatist, Charles Paradis concordou: nem a Casa da "
            "Moeda nem o Banco do Japão tinham qualquer evidência que sustentasse a história. Para ele, o boato nasceu "
            "de jornais que apresentaram mal os fatos e ganhou força porque a Taito nunca o desmentiu."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Space_Invaders",
            "By the end of 1978, the game had grossed Taito US$670 million (equivalent to $3.3 billion in 2025) in Japan alone. [...] "
            "There were reports that its popularity led to a shortage of 100-yen coins in Japan, but descriptions from numismatists living in Japan at the time indicated \"nothing out of the ordinary\" around Space Invaders's release; Nishikado also expressed skepticism. "
            "Numismatist Mark Fox compared the production outputs of the Japan Mint during those years to the game's reported earnings and concluded that its impact did not change the outputs. "
            "He further noted that arcade operators would have regularly emptied their machines, which would keep the currency in circulation, and attributed the myth to lower 100-yen coin productions in 1978 and 1979. "
            "Writing in the The Numismatist, Charles Paradis agreed with Fox's analysis and noted that the Japan Mint and Bank of Japan did not have any evidence to support the myth. "
            "He attributed it to newspapers misrepresenting facts and Taito's lack of denial. [...] "
            "Tomohiro Nishikado, who spent a year designing it",
            nome="Space Invaders")],
    },
    # 5 Pac-Man: um jogo pensado para atrair mulheres, com fantasmas de personalidades diferentes
    {
        "temas_secundarios": ["ia_robotica"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "O Pac-Man foi criado para atrair mulheres aos fliperamas, então dominados por jogos de guerra e esporte; daí o tema de comer. E cada fantasma tem seu jeito: um persegue, outro tenta emboscar, outro foge e volta.",
        "explicacao": (
            "Toru Iwatani, da Namco, achava que os gráficos toscos e a violência dos jogos de fliperama afastavam todo "
            "mundo que não fosse homem, e que os fliperamas eram vistos como lugares mal frequentados. Quis fazer um "
            "jogo alegre e sem violência que trouxesse mulheres e casais, deixando o ambiente mais familiar. Pensou no "
            "que as mulheres faziam com frequência e escolheu a comida, por achar que elas gostavam de doces. O nome "
            "original, Pakkuman, vem de \"paku paku\", onomatopeia japonesa do abre-e-fecha da boca ao comer. O "
            "presidente da empresa queria os quatro fantasmas vermelhos e idênticos; Iwatani insistiu em cores "
            "diferentes e deu a cada um uma estratégia, para o jogo não ficar nem chato nem impossível. Em japonês, os "
            "nomes deles significam perseguir, emboscar, inconstante e se fazer de bobo: o vermelho vai direto atrás do "
            "Pac-Man, o rosa tenta chegar à frente dele, e o laranja alterna entre perseguir e fugir. Deu certo: um "
            "executivo da Midway o chamou de primeiro videogame comercial a envolver um grande número de mulheres. Nos "
            "EUA, o nome Puck Man foi trocado por medo de que vândalos transformassem o P em F."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Pac-Man",
            "Iwatani felt that the crude graphics and violence of arcade games limited their appeal to men only and that arcades were seen as seedy environments. "
            "For his next project, Iwatani chose to create a nonviolent, cheerful game that appealed mostly to women, as he believed that attracting women and couples into arcades would create a more family-friendly atmosphere. "
            "Iwatani considered women's most frequent activities and then decided to center his game around eating, feeling that women like to eat sweets. "
            "His game was initially titled Pakkuman, based on the Japanese onomatopoeia term \"paku paku taberu\", referencing the mouth movement of opening and closing in succession. [...] "
            "Namco president Masaya Nakamura had originally requested that all of the ghosts be colored red and appear indistinguishable from one another. "
            "Iwatani believed that the ghosts should appear in different colors, and his colleagues unanimously supported his idea. "
            "The ghosts were programmed to display their own distinct personalities in order to prevent the game from becoming too boring or impossibly difficult to play. "
            "Each ghost's name provides a hint to its strategy for chasing Pac-Man: Shadow (\"Blinky\") always chases Pac-Man, Speedy (\"Pinky\") tries to get ahead of him, Bashful (\"Inky\") uses a more complicated strategy and Pokey (\"Clyde\") alternates between chasing and escaping. "
            "The ghosts' Japanese names are おいかけ, chase; まちぶせ, ambush; きまぐれ, fickle; and おとぼけ, playing dumb, respectively. [...] "
            "Blinky (red), Pinky (pink), Inky (cyan), and Clyde (orange) [...] "
            "becoming \"the first commercial videogame to involve large numbers of women as players\" according to Midway's Stan Jarocki [...] "
            "The game's title was also changed because Namco executives worried that vandals would change the \"P\" in Puck Man to an \"F\". [...] "
            "Pac-Man was designed by Toru Iwatani, who led a nine-man team",
            nome="Pac-Man")],
    },
    # 6 a fase 256 do Pac-Man e o recorde impossível
    {
        "temas_secundarios": ["historia_computacao"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "A fase 256 do Pac-Man não pode ser vencida: um estouro de número inteiro faz ela carregar errado. Mesmo assim, em 1982 um menino de oito anos recebeu carta do presidente Reagan por um recorde que exigia passar dela.",
        "explicacao": (
            "Os fantasmas ficam mais rápidos à medida que o jogo avança, mas o limite verdadeiro do Pac-Man é um erro de programação: "
            "um estouro de inteiro faz a fase 256 carregar de forma defeituosa, e ela não pode ser concluída. É a "
            "chamada \"kill screen\", a tela que mata o jogo. Isso dá à pontuação um teto. A partida perfeita vale "
            "3.333.360 pontos: comer todos os pontos, energizadores, frutas e fantasmas azuis nas 255 primeiras fases "
            "sem perder uma vida, e depois gastar as seis vidas somando o máximo possível na fase 256. Em dezembro de "
            "1982, Jeffrey Yee, um menino de oito anos, recebeu uma carta do presidente Ronald Reagan parabenizando-o por "
            "um recorde de 6.131.940 pontos, algo só possível se ele tivesse passado da fase 256. Em setembro de 1983, "
            "o chefe de pontuação da Twin Galaxies levou uma equipe para visitar jogadores da Costa Leste que diziam "
            "conseguir passar daquela fase. Nenhum demonstrou essa capacidade. Em 1999, o jogador Billy Mitchell "
            "ofereceu 100 mil dólares a quem passasse da fase 256 antes de 1º de janeiro de 2000. O prêmio nunca foi "
            "reclamado."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Pac-Man",
            "The game increases in difficulty as the player progresses: the ghosts become faster [...] "
            "An integer overflow causes the 256th level to load improperly, rendering it impossible to complete. "
            "This is known as a kill screen. [...] "
            "A perfect score on the original Pac-Man arcade game is 3,333,360 points, achieved when the player obtains the maximum score on the first 255 levels by eating every dot, energizer, fruit and blue ghost without losing a life, then uses all six lives to obtain the maximum possible number of points on level 256. [...] "
            "In December 1982, eight-year-old boy Jeffrey R. Yee received a letter from United States president Ronald Reagan congratulating him on a world record score of 6,131,940 points, possible only if he had passed level 256. "
            "In September 1983, Walter Day, chief scorekeeper at Twin Galaxies at the time, took the US National Video Game Team on a tour of the East Coast to visit gamers who claimed the ability to pass that level. "
            "None demonstrated such an ability. "
            "In 1999, Billy Mitchell offered $100,000 to anyone who could pass level 256 before January 1, 2000. "
            "The offer expired with the prize unclaimed.",
            nome="Pac-Man")],
    },
    # 7 Pong: exercício de treino, cópia do Odyssey e a caixa de moedas transbordando
    {
        "temas_secundarios": ["invencoes", "leis_julgamentos"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "O Pong nasceu como exercício de treino para um engenheiro novato, inspirado num jogo de pingue-pongue de um console doméstico. Testado num bar, o protótipo parou de funcionar: a caixa de moedas tinha transbordado.",
        "explicacao": (
            "Em maio de 1972, Nolan Bushnell viu uma demonstração do Magnavox Odyssey, o primeiro console doméstico, "
            "que tinha um jogo de pingue-pongue. Ao fundar a Atari, encomendou a Allan Alcorn, que nunca tinha "
            "trabalhado com videogames, um jogo de pingue-pongue barato para fliperama. Era só um exercício de treino, "
            "mas Bushnell não contou isso a Alcorn, nem que a ideia vinha do Odyssey. O resultado ficou tão bom que "
            "virou o primeiro produto da empresa. Em agosto de 1972, o protótipo foi instalado no Andy Capp's Tavern, "
            "um bar da região. Fez sucesso desde a primeira noite, e a procura cresceu na semana e meia seguinte. "
            "Poucos dias depois, o dono do bar chamou Alcorn porque a máquina estava com defeito. O problema era o "
            "mecanismo de moedas, que transbordava de tantas moedas. Depois de lançado, o Pong rendia quatro "
            "vezes mais que outras máquinas de moeda. A origem, porém, cobrou seu preço: em 1974, a Magnavox processou "
            "a Atari e outras empresas por violar suas patentes. A Atari fez acordo em 1976 e pagou 1,5 milhão de "
            "dólares por uma licença. Ao longo de 20 anos, essas patentes renderam mais de 100 milhões de dólares em "
            "processos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Pong",
                "Prior to working at Atari, Alcorn had no experience with video games. [...] "
                "In August 1972, Bushnell and Alcorn installed the Pong prototype at a local bar, Andy Capp's Tavern. [...] "
                "the bar's owner and manager, Bill Gaddis [...] "
                "The game was well received the first night and its popularity continued to grow over the next one and a half weeks. [...] "
                "A few days later, the prototype began exhibiting technical issues and Gaddis contacted Alcorn to fix it. "
                "Upon inspecting the machine, Alcorn discovered that the problem was due to the coin mechanism overflowing with quarters. [...] "
                "Following its release, Pong consistently earned four times more revenue than other coin-operated machines.",
                nome="Pong"),
            wiki("Magnavox_Odyssey",
                "The Magnavox Odyssey is the first commercial home video game console. [...] "
                "In May 1972, Nutting Associates chief engineer Nolan Bushnell, designer of the first commercial arcade video game, Computer Space, saw a demonstration of the Odyssey. "
                "Inspired, when he and Ted Dabney quit Nutting to found Atari, he assigned Allan Alcorn to create a cheap ping-pong arcade game as a training exercise, though he did not tell Alcorn that it was for training nor that the idea was based on the Odyssey Table Tennis game. "
                "Alcorn soon developed Pong (1972), which Bushnell recognized as a potential hit, and it became the company's first game. [...] "
                "In April 1974, however, Magnavox sued Atari along with several competitors [...] "
                "Atari's settlement, made in June 1976, granted it a license in exchange for US$1.5 million [...] "
                "formed the basis of a series of lawsuits spanning 20 years, earning Sanders and Magnavox over US$100 million.",
                nome="Magnavox Odyssey"),
        ],
    },
    # 8 o Odyssey: películas na TV, sem placar, e a pistola feita pela Nintendo
    {
        "temas_secundarios": ["invencoes", "brinquedos"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "O primeiro console doméstico, o Magnavox Odyssey (1972), só mostrava pontos brancos e não contava o placar: o cenário vinha de películas de plástico grudadas na TV. E a pistola dele foi fabricada pela Nintendo.",
        "explicacao": (
            "O aparelho nasceu de protótipos do engenheiro Ralph Baer, que, ainda adolescente, fugira com a família "
            "judia da Alemanha nazista em 1938. Na empresa Sanders Associates, ele chegou a uma \"Caixa Marrom\", "
            "batizada assim pela fita adesiva marrom com que a equipe imitava madeira. O console da Magnavox exibia, em "
            "preto e branco, três quadradinhos e uma linha vertical. O resto ficava por conta da imaginação: cada jogo "
            "vinha com uma película plástica que aderia à tela por eletricidade estática e desenhava o cenário, de modo "
            "que os mesmos controles serviam para uma pista de esqui ou para um jogo de imitar. O console não fazia "
            "valer as regras nem marcava pontos; isso ficava com os jogadores, que recebiam dados, fichas de pôquer, "
            "dinheiro de brinquedo e baralho. Baer se irritou com esses acréscimos de jogo de tabuleiro, que achava "
            "inúteis. O único acessório lançado foi um rifle de luz, a primeira pistola de videogame, que registrava o "
            "acerto quando apontada para um ponto luminoso da tela. Ele foi projetado e fabricado pela Nintendo, a partir "
            "de uma pistola de brinquedo que ela lançara em 1970."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Magnavox_Odyssey",
                "The Magnavox Odyssey is the first commercial home video game console. [...] "
                "Magnavox completed development and released it in the United States in September 1972 [...] "
                "It is capable of displaying three square dots and one line of varying height on the screen in monochrome black and white [...] "
                "The Odyssey is capable of displaying three square dots and a vertical line on the screen. [...] "
                "The games include plastic overlays that stick to the television via static cling to create visuals. "
                "Games that use the same game card can have different overlays, which can change a game with the same controls from, for example, a mountain ski path to a movement-based Simon Says game. "
                "In addition to the overlays, the Odyssey came with dice, poker chips, score sheets, play money, and card decks. "
                "One peripheral controller was released for the Odyssey, the first video game light gun. "
                "Named the Electronic Rifle, the rifle-shaped device registered a hit when pointed at a light source such as a dot on the television screen. [...] "
                "The light guns were designed and manufactured by Nintendo, based on their 1970 Beam Gun toy. [...] "
                "Baer was upset with the board game additions, which he felt were pointless add-ons that would go unused by players. [...] "
                "The console does not enforce game rules or keep track of scores for the games; that is left up to the players.",
                nome="Magnavox Odyssey"),
            wiki("Ralph_H._Baer",
                "Baer's Jewish family fled Germany just before World War II [...] "
                "Baer's family, fearing increasing persecution, moved from Germany to New York City in 1938, just two months prior to Kristallnacht, while Baer was a teenager. [...] "
                "They developed the \"Brown Box\" console video game system, so named because of the brown tape in which they wrapped the units to simulate wood veneer. [...] "
                "he was working as an engineer at Sanders Associates (now BAE Systems) in Nashua, New Hampshire, when he conceived the idea of playing games on a television screen around 1966.",
                nome="Ralph H. Baer"),
        ],
    },
    # 9 o easter egg do Adventure
    {
        "temas_secundarios": ["historia_computacao"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "A Atari não punha o nome dos programadores nos jogos. Então um deles escondeu no Adventure (1980) uma sala secreta com \"Criado por Warren Robinett\". A empresa decidiu manter o segredo e chamá-lo de easter egg.",
        "explicacao": (
            "Depois de ser comprada pela Warner, a Atari tirou dos produtos o nome dos criadores, em parte para que "
            "concorrentes não identificassem e contratassem seus programadores, e em parte para negar a eles um trunfo "
            "nas negociações. O descontentamento fez quatro programadores saírem e fundarem a Activision, que passou a "
            "competir com a Atari. Warren Robinett, inspirado em boatos de que os Beatles escondiam mensagens nas "
            "músicas, pôs no Adventure, para o Atari 2600, uma sala quase inacessível com o seu nome. Para entrar, era "
            "preciso achar um ponto cinza de um único pixel, invisível na maior parte das salas, e levá-lo com outros "
            "objetos a um corredor. Ele guardou segredo, nem o manual mencionava a sala, e saiu da Atari antes do "
            "lançamento. Mais tarde contou que ganhava cerca de 22 mil dólares por ano, sem direitos, enquanto o jogo "
            "vendeu um milhão de cópias a 25 dólares cada. Um garoto de quinze anos de Salt Lake City achou a sala e "
            "escreveu à Atari. Refazer o chip de memória custaria cerca de 10 mil dólares, e um diretor defendeu "
            "manter a mensagem, comparando-a a ovos de Páscoa escondidos para os jogadores acharem. Não foi o primeiro segredo "
            "desse tipo, mas foi ele que popularizou a ideia."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Adventure_(1980_video_game)",
            "While not the first such Easter egg, Robinett's secret room pioneered this idea within video games and other forms of media [...] "
            "Atari removed the names of game developers from their products as a means to prevent competitors from identifying and recruiting Atari's programmers. "
            "This also was used as a means to deny the developers a bargaining chip in any negotiations they had with management. [...] "
            "David Crane, Larry Kaplan, Alan Miller, and Bob Whitehead all left Atari due to lack of recognition and royalty payments, and formed Activision as a third-party 2600 developer, making many hit games in competition with Atari. "
            "Unknown to anyone else, Robinett, inspired by popular rumors that the Beatles had hidden messages in songs, embedded his name in his game in the form of a hidden and virtually inaccessible room displaying the text \"Created by Warren Robinett\". "
            "In 2015, Robinett recalled the message had been a means of self-promotion, noting that Atari had paid him only around US$22,000 per year without any royalties while selling one million units of the game at US$25 each. [...] "
            "It is not mentioned in the game's manual, as the manual's author was unaware of it. "
            "After the game was released, Adam Clayton, a fifteen-year-old from Salt Lake City, discovered it and sent a letter of explanation to Atari. [...] "
            "the cost of creating a new read-only memory (ROM) mask, or memory chip, was around US$10,000 [...] "
            "Steve Wright, the director of software development of the Atari Consumer Division, argued for retaining the message, believing it gave players additional incentive to find it and play their games more; he suggested these were like Easter eggs for players to find. "
            "Atari eventually decided to leave the code unchanged and dubbed such hidden features \"Easter eggs\" [...] "
            "The Dot is a single-pixel object which is invisibly embedded in the south wall of a sealed chamber [...] "
            "The player must bring the dot, along with two or more other objects, to the east end of the corridor below the Golden Castle. [...] "
            "After Atari's acquisition by Warner Communications in 1976 [...] "
            "Robinett submitted the source code for Adventure to Atari management in June 1979 and soon left Atari. "
            "Atari released the game in March 1980.",
            nome="Adventure (1980 video game)")],
    },
    # 10 os cartuchos enterrados no Novo México
    {
        "temas_secundarios": ["economia_curiosa"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Por décadas, o enterro de milhões de cartuchos de E.T. num lixão do Novo México foi tido como lenda. Em 2014, uma escavação acompanhada por arqueólogos achou o enterro, mas com cartuchos de dezenas de jogos.",
        "explicacao": (
            "A Atari fabricou 5 milhões de cartuchos do jogo de E.T., lançado em dezembro de 1982, e vendeu só 1,5 "
            "milhão. O programador teve apenas cinco semanas para fazê-lo, e o resultado é tido como um dos piores "
            "jogos já feitos. Com o Pac-Man para o Atari 2600 a empresa tinha feito pior ainda: fabricou 12 milhões de "
            "cartuchos quando só havia cerca de 10 milhões de consoles vendidos. Em 1983, a Atari perdeu 536 milhões de "
            "dólares. Em setembro daquele ano, um jornal local noticiou que de 10 a 20 carretas de caixas, cartuchos e "
            "consoles tinham sido esmagadas e enterradas no aterro de Alamogordo, e crianças da cidade chegaram a "
            "saquear o lixão. Como as informações eram confusas, a história de milhões de E.T. enterrados passou a ser "
            "tratada como lenda urbana. Em abril de 2014, uma produtora que filmava um documentário escavou o local, com "
            "arqueólogos documentando o material. O gerente que comandara o enterro estava lá e disse que foram cerca "
            "de 728 mil cartuchos, não milhões. Só uns 1.300 foram retirados, de 59 jogos diferentes, porque o resto "
            "estava fundo demais. Um dos cartuchos de E.T. desenterrados foi para o acervo do Smithsonian."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Atari_video_game_burial",
            "Since the burial was first reported, there had been doubts as to its veracity and scope, and it was frequently dismissed as an urban legend. [...] "
            "Atari, Inc. went on to lose $536 million in 1983 [...] "
            "When the latter game received its official port to the Atari 2600, Atari was confident that sales figures would be high, and manufactured 12 million cartridges—despite having sold only around 10 million Atari 2600 consoles. [...] "
            "Warshaw had only five weeks to make a full game [...] "
            "the game was critically panned, and is now seen as one of the worst ever made. "
            "Atari manufactured 5 million cartridges for the game; however, upon its release in December 1982, only 1.5 million copies were sold [...] "
            "In September 1983, the Alamogordo Daily News of Alamogordo, New Mexico, reported in a series of articles that between 10 and 20 semi-trailer truckloads of Atari boxes, cartridges, and systems from an Atari storehouse in El Paso, Texas, were crushed and buried at the landfill to the south of city. [...] "
            "kids in this town of 25,000 began robbing the Atari grave [...] "
            "The conflicting information surrounding the burial led to the claim of it being an \"E.T. Dump\" being referred to as an urban legend [...] "
            "On May 28, 2013, the Alamogordo City Commission granted Fuel Industries, a Canadian entertainment company, six months of access to the landfill to film a documentary [...] "
            "Excavation started on April 26, 2014 as an open event to the public. [...] "
            "James Heller, the former Atari manager in charge of the original burial, was also on hand at the excavation. [...] "
            "Contrary to the urban legend that claims millions of cartridges were buried there, Heller stated that only 728,000 cartridges were buried. [...] "
            "A team of archaeologists was present to examine and document the Atari material unearthed by excavation machinery [...] "
            "Only about 1,300 cartridges of the estimated 700,000 were removed from the burial, as the remaining materials were deeper than expected [...] "
            "The cartridges found were from 59 different games [...] "
            "One of the E.T. cartridges that had been dug up was taken by the Smithsonian Institution for its records",
            nome="Atari video game burial")],
    },
    # 11 Nintendo: baralhos de hanafuda e uma palavra portuguesa
    {
        "temas_secundarios": ["jogos_azar", "palavras_viajantes"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "A Nintendo nasceu em 1889, em Kyoto, fabricando baralhos de hanafuda que faziam sucesso nas casas de jogo da yakuza. Esses baralhos japoneses se chamam karuta, palavra que vem do português \"carta\".",
        "explicacao": (
            "O fundador foi o artesão Fusajiro Yamauchi, que produzia à mão as cartas de hanafuda, as \"cartas de "
            "flores\". Elas tinham ganhado popularidade depois que o Japão proibiu, em 1882, a maioria dos jogos de "
            "azar, mas tolerou o hanafuda. As cartas vendiam bem nas casas de jogo comandadas pela yakuza em Kyoto. "
            "Outros fabricantes preferiram sair do mercado para não ficar associados ao crime; Yamauchi insistiu e, em "
            "poucos anos, virou o principal produtor. O negócio tinha um problema curioso: as cartas eram tão duráveis "
            "que demoravam a ser trocadas, o que freava as vendas. Nem o significado do nome é certo. A tradução mais "
            "repetida, algo como \"deixe a sorte com o céu\", não tem comprovação histórica, e nem os descendentes de "
            "Yamauchi sabem o que ele quis dizer. Em 1929, a empresa já era a maior fabricante de baralhos do Japão. A "
            "virada para os brinquedos veio nos anos 1960, e a dos videogames depois, mas a empresa manteve setores "
            "dedicados às cartas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Nintendo",
            "Nintendo was founded as Nintendo Koppai on 23 September 1889 by craftsman Fusajiro Yamauchi in Shimogyō-ku, Kyoto, Japan, as an unincorporated establishment, to produce and distribute Japanese playing cards, or karuta (かるた; from Portuguese carta, 'card'), most notably hanafuda (花札, 'flower cards'). "
            "The name \"Nintendo\" is commonly assumed to mean \"leave luck to heaven\", but the assumption lacks historical validation; it has also been suggested to mean \"the temple of free hanafuda\", but even descendants of Yamauchi do not know the true intended meaning of the name. "
            "Hanafuda cards had become popular after Japan banned most forms of gambling in 1882, though tolerated hanafuda. "
            "Sales of hanafuda cards were popular with the yakuza-run gaming parlors in Kyoto. "
            "Other card manufacturers had opted to leave the market, not wanting to be associated with its criminality, but Yamauchi persisted despite such fears to become the primary producer of hanafuda within a few years. [...] "
            "alongside long durability of the cards, which impacted sales due to the low replacement rate. [...] "
            "By that time, Nintendo was the largest playing card business in Japan. [...] "
            "The history of Nintendo began when craftsman Fusajiro Yamauchi founded the company in 1889 to produce handmade hanafuda playing cards. "
            "After venturing into various lines of business and becoming a public company, Nintendo began producing toys in the 1960s, and later video games. [...] "
            "The company's restructuring preserved a couple of areas dedicated to playing card manufacturing. [...] "
            "and headed the business in 1929.",
            nome="Nintendo")],
    },
    # 12 Tetris: criado na URSS, sem direito a lucro, e um telex mal-entendido
    {
        "temas_secundarios": ["guerra_fria", "leis_julgamentos"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "O Tetris foi criado por um pesquisador soviético nas horas vagas, e a lei da URSS não deixava ninguém lucrar com as próprias criações. O jogo se espalhou de graça, e os direitos viraram uma briga entre vários países.",
        "explicacao": (
            "Alexey Pajitnov pesquisava reconhecimento de fala e inteligência artificial no Centro de Computação "
            "Dorodnitsyn, da Academia de Ciências soviética, e fazia jogos no tempo livre. Inspirou-se num quebra-cabeça "
            "de pentaminós, peças de cinco quadrados, e simplificou para peças de quatro, que têm só sete formatos. O "
            "nome junta \"tetra\" com o esporte preferido dele, o tênis. O computador que usava não tinha gráficos, e "
            "as peças eram desenhadas com colchetes e espaços. Como a lei soviética não protegia direitos de indivíduos "
            "nem permitia que eles ganhassem com suas criações, cópias gratuitas em disquete circularam por Moscou e "
            "pelo Leste Europeu. Um empresário baseado em Londres viu o jogo na Hungria e pediu a licença por telex. Pajitnov "
            "passou dias redigindo uma resposta simpática mas sem compromisso, que o empresário leu como um sim. Só "
            "que, na URSS, apenas órgãos estatais autorizados podiam fechar negócios no exterior. Seguiu-se um "
            "emaranhado de licenças que terminou num tribunal americano, onde, em 1989, a Nintendo ganhou da Atari "
            "Games os direitos para consoles. Pajitnov emigrou para os EUA em 1991, e só em 1996 fechou um acordo "
            "formal para licenciar o jogo por conta própria."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Tetris",
            "In the 1980s, Alexey Pajitnov was a Soviet speech recognition and artificial intelligence researcher at the Dorodnitsyn Computing Center of the Academy of Sciences who operated an Elektronika 60 [...] "
            "While at the center, he developed at least twenty types of video games in his spare time. "
            "Pajitnov bought a pentomino puzzle set from a store and played with it in his office, and he became inspired to adapt the puzzle game to the computer. [...] "
            "so he scaled the concept down to tetrominoes, using seven different shapes. [...] "
            "Because the Elektronika 60 had no graphical interface, Pajitnov represented the pieces using bracket and space characters. [...] "
            "The name Tetris was coined by Pajitnov as a combination of \"tetra\" (meaning \"four\") and his favorite sport, tennis. [...] "
            "Due to the Soviet government's ideology and its bureaucratic nature, Soviet copyright law did not protect the intellectual rights of individuals, nor did it allow them to derive income from their creations. [...] "
            "Floppy disk copies were distributed freely throughout Moscow before spreading to Eastern Europe. "
            "Robert Stein of Andromeda Software saw Tetris in Hungary and contacted the Dorodnitsyn Computing Center to secure a license to release it commercially. [...] "
            "Stein returned to London and contacted Dorodnitsyn Computing Center by telex to obtain the license rights [...] "
            "who spent days attempting to compose, translate to English, and send a favorable yet noncommittal response by telex to Stein. "
            "Despite this attempt, Stein interpreted the response as granting him the license and proceeded to find a publisher for Tetris. "
            "This would not have been a valid contract, as in the Soviet Union, only dedicated corporations authorized by the Ministry of Foreign Trade could enter into foreign trade agreements. [...] "
            "On November 13, 1989, Smith ended the legal battle between Nintendo and Atari Games regarding Tetris before trial by a verbal summary judgment, granting Nintendo the console rights to Tetris. [...] "
            "In 1991, with Rogers' help, Pajitnov and his family emigrated to Seattle [...] "
            "Rogers formed Blue Planet Software and, on January 1, 1996, made a formal agreement with Pajitnov to license Tetris to the new company.",
            nome="Tetris")],
    },
    # 13 o garoto que "zerou" o Tetris do NES
    {
        "temas_secundarios": ["historia_computacao", "limites_humanos"],
        "tipos_espanto": ["engenhosidade", "escala_absurda"],
        "gancho": "Desde 1989, o Tetris do NES era tido como impossível de vencer: a partida só acabava quando as peças chegavam ao topo. Em dezembro de 2023, um garoto de 13 anos o \"zerou\" travando o jogo no nível 157.",
        "explicacao": (
            "No nível 29, as peças passam a cair na velocidade máxima, uma linha da grade por quadro, rápido demais "
            "para quase todo mundo. Os criadores não previam que alguém passasse dali: o contador de níveis nem "
            "mostra direito os números seguintes. Os jogadores, porém, inventaram técnicas. No \"hypertapping\", a "
            "pessoa contrai o bíceps até ele tremer, e o tremor faz o polegar bater no direcional mais de 10 vezes por "
            "segundo. Em 2020 surgiu o \"rolling\": um dedo fica parado no direcional enquanto os dedos da outra mão "
            "tamborilam atrás do controle, empurrando os botões contra ele, até 30 vezes por segundo. Com isso, os "
            "melhores passaram a jogar quase indefinidamente naquela velocidade e esbarraram em defeitos do código, "
            "analisados em 2014 por um pesquisador. A partir do nível 138, um estouro de número faz as cores das peças "
            "virem de áreas aleatórias da memória, e nos níveis 146 e 148 elas ficam pretas sobre o fundo preto. Além "
            "disso, a contagem de pontos pode travar o jogo depois de cerca de 1.550 linhas. Willis Gibson, de "
            "Oklahoma, foi o primeiro a vencer o nível 148 e chegou ao travamento no 157, sendo reconhecido como o "
            "primeiro a \"vencer\" o jogo. Alexey Pajitnov, criador do Tetris, foi conhecê-lo e chamou o feito de "
            "incrível."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Tetris_(NES_video_game)",
            "After level 10, the game speed only increases on levels 13, 16, 19, and 29, at which point the speed no longer increases. "
            "On level 29, pieces fall at 1 grid cell every frame, which is too fast for almost all players, and it is thus called the \"kill screen\". "
            "The developers of the game never intended anyone to play past the kill screen, as the game does not properly display the level numbers past 29 [...] "
            "When hypertapping, horizontal tetromino speed is maximized by rapidly tapping the D-pad more than 10 times per second. "
            "The technique involves flexing the biceps until it tremors, so that the high-speed tremor taps the thumb on the D-pad. [...] "
            "In 2020, the \"rolling\" technique was developed by competitive NES Tetris player Chris \"Cheez_fish\" Martinez. "
            "When rolling, a stationary finger is placed on the D-pad, while the other hand's fingers are drummed across the back of the controller, pushing the buttons up into the stationary hand. [...] "
            "it allows pieces to be shifted horizontally up to 30 times per second, enabling play far past level 29. [...] "
            "\"players were getting good enough to effectively play indefinitely on the same 'Level 29' speed that had been considered an effective kill screen just a few years earlier.\" [...] "
            "In 2014, computer researcher Mike Birken published an analysis of Tetris' game code, including details on unexpected behaviors that occur at very high levels. "
            "An integer overflow bug is first encountered at level 138, where color palettes would be loaded from unrelated areas of memory, creating unusual and unintended game piece colors. "
            "In particular, levels 146 and 148, nicknamed \"dusk\" and \"charcoal\", feature black game pieces that are extremely difficult to see against the black background, hindering further progression. "
            "Additionally, the score-counting code could crash the game after about 1550 lines are cleared, corresponding to level 155. [...] "
            "In December 2023, 13-year-old roller Willis Gibson from Stillwater, Oklahoma, was the first to complete the \"charcoal\" level 148. "
            "He continued playing and reached a game crash at level 157. "
            "Because Tetris had been considered unwinnable (due to games necessarily ending with \"topping out\"), Gibson is credited with being the first person to \"beat the game\" since its release in 1989. [...] "
            "Co-founders Alexey Pajitnov and Henk Rogers met Gibson in January 2024, calling his playthrough an \"amazing, amazing achievement\".",
            nome="Tetris (NES video game)")],
    },
    # 14 a "peste" do World of Warcraft e os epidemiologistas
    {
        "temas_secundarios": ["doencas_infecciosas", "psicologia_social"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "Em 2005, um erro de programação espalhou uma peste pelo mundo virtual de World of Warcraft. Uns jogadores viraram socorristas, outros se isolaram, outros a espalharam de propósito, e epidemiologistas estudaram o caso.",
        "explicacao": (
            "Num desafio novo do jogo, o chefe Hakkar lançava nos personagens o \"Sangue Corrompido\", um efeito nocivo que "
            "passava para quem estivesse perto. Era para durar segundos e ficar restrito àquela área. "
            "Mas os bichos de estimação dos jogadores podiam ser guardados no meio da luta e chamados de volta depois, "
            "e os programadores esqueceram de apagar o feitiço deles. Levados às cidades, os bichos viraram vetores, e "
            "os personagens controlados pelo computador, que não morriam, viraram portadores sem sintomas. Segundo um "
            "jogador da época, em alguns servidores os personagens fracos morriam quase na hora nas grandes cidades. Curandeiros correram para "
            "ajudar e muitas vezes só mantinham os doentes vivos e contagiosos; outros jogadores avisavam do perigo "
            "nas entradas das cidades ou se isolavam no mato. Os chamados griefers pegavam a doença de propósito para "
            "espalhá-la, e a epidemiologista Nina Fefferman os comparou à Maria Tifoide. Outro pesquisador comparou os "
            "bichos de estimação aos patos que espalham a gripe aviária sem adoecer, e as viagens rápidas do jogo às "
            "viagens de avião na epidemia de SARS. O interesse científico vinha de um ponto: no jogo, cada reação é de "
            "uma pessoa real, enquanto os modelos matemáticos precisam supor o comportamento humano. A Blizzard só "
            "acabou com a peste reiniciando os servidores."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Corrupted_Blood_incident",
            "The Corrupted Blood incident (also known as the World of Warcraft pandemic) took place between September 13 and October 8, 2005 [...] "
            "When participating in a certain boss battle at the end of a raid, player characters would become infected with a debuff that was transmitted between characters in close proximity. [...] "
            "The effects of Corrupted Blood were intended to last for 10 seconds, or until the players defeated Hakkar, whichever came first. [...] "
            "Developers had intended to limit the effects of the debuff to the Zul'Gurub region, but a programming oversight led to its spread throughout the in-game universe. "
            "Players with animal companions during boss battles could protect pets infected with Corrupted Blood by placing them into a type of suspended animation mid-fight. "
            "These pets were subsequently re-activated after the completion of the boss battle, but developers had forgotten to include an \"off-switch\" that would recognize the conclusion of the raid and remove the debuff from companions. [...] "
            "They then re-activated their infected pets, who became disease vectors, allowing Corrupted Blood to spread beyond players involved in the raid. "
            "Other NPCs could become infected with the disease, but they were incapable of dying, and instead became asymptomatic carriers for player characters. [...] "
            "Another posted that \"[s]ome servers have gotten so bad that you can't go into the major cities without getting the plague. "
            "And anyone less than like Level 50 nearly immediately dies. [...] "
            "Some players whose characters possessed healing abilities headed to major cities as impromptu first responders [...] "
            "More often, rather than removing the Corrupted Blood infection, healing characters merely kept characters alive and contagious, thereby prolonging the spread of the infection. "
            "Less powerful player characters, meanwhile, would stand at the edges of infected towns, warning other player characters not to enter. [...] "
            "Other players enacted self-quarantine methods, remaining in less-populated wilderness areas of Azeroth [...] "
            "These players would purposely contract Corrupted Blood and travel to densely populated areas to further its spread. [...] "
            "epidemiologist Nina Fefferman [...] "
            "Fefferman compared these players to Typhoid Mary [...] "
            "Ran Balicer of the Ben-Gurion University of the Negev compared the role that pet companions played in the spread of Corrupted Blood to avian influenza, which spread through asymptomatic ducks. "
            "The use of fast travel to quickly spread the disease between distant locations was also compared to the role that air travel played in the  2002–2004 SARS outbreak. [...] "
            "Epidemiologists, meanwhile, took interest in how MMORPGs, unlike mathematical models, could capture individual human responses to disease outbreaks rather than generating assumptions about behavior. [...] "
            "After several failed hotfixes, Blizzard ended the pandemic by performing a hard reset",
            nome="Corrupted Blood incident")],
    },
    # 15 Foldit: jogadores e a protease de um vírus de macaco
    {
        "temas_secundarios": ["microbiologia", "doencas_infecciosas"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "Em 2011, jogadores do Foldit, um game de dobrar proteínas, criaram em dez dias um modelo da enzima de um vírus de macaco parecido com o HIV. Ele ajudou a resolver uma estrutura que desafiava cientistas havia 15 anos.",
        "explicacao": (
            "O Foldit é um quebra-cabeça on-line criado na Universidade de Washington, nos EUA, por um centro de "
            "ciência dos jogos e pelo departamento de bioquímica. O jogador recebe uma proteína e usa ferramentas do "
            "jogo para dobrá-la da melhor forma possível; as soluções com mais pontos são analisadas por "
            "pesquisadores, que conferem se correspondem à forma real da molécula. Um artigo de 2010 na revista Nature "
            "creditou aos 57 mil jogadores resultados úteis, que igualavam ou superavam os de algoritmos. Em 2011, veio "
            "o caso mais famoso: a protease de um retrovírus, o vírus de Mason-Pfizer de macacos, que causa sintomas "
            "parecidos com os da aids. Sua estrutura cristalina estava sem solução havia 15 anos. O desafio ficou "
            "aberto por três semanas, e em dez dias os jogadores produziram um modelo 3D bom o bastante para a técnica "
            "de substituição molecular, usada para decifrar estruturas a partir de cristais. Não foi caso isolado: num "
            "estudo publicado em 2016, uma equipe de jogadores do Foldit chegou ao modelo mais preciso numa competição "
            "com cristalógrafos treinados, estudantes e programas automáticos."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Foldit",
            "Foldit is an online puzzle video game about protein folding. "
            "It is part of an experimental research project developed by the University of Washington, Center for Game Science, in collaboration with the UW Department of Biochemistry. "
            "The objective of Foldit is to fold the structures of selected proteins as perfectly as possible, using tools provided in the game. "
            "The highest scoring solutions are analyzed by researchers, who determine whether or not there is a native structural configuration (native state) that can be applied to relevant proteins in the real world. [...] "
            "A 2010 paper in the science journal Nature credited Foldit's 57,000 players with providing useful results that matched or outperformed algorithmically computed solutions. [...] "
            "In 2011, Foldit players helped decipher the crystal structure of a retroviral protease from Mason-Pfizer monkey virus (M-PMV), a monkey virus which causes HIV/AIDS-like symptoms, a scientific problem that had been unsolved for 15 years. "
            "The puzzle was available for three weeks, and players produced a 3D model of the enzyme in ten days that was accurate enough for molecular replacement. [...] "
            "A September 2016 article in Nature Communications detailed a \"crystallographic model-building competition between trained crystallographers, undergraduate students, Foldit players and automatic model-building algorithms\" in which \"a team of Foldit players achieved the most accurate structure\"",
            nome="Foldit")],
    },
    # 16 amnésicos que viam peças de Tetris ao adormecer
    {
        "temas_secundarios": ["sono_ritmos", "memoria"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Num estudo publicado em 2000, pessoas com amnésia jogaram Tetris e, ao pegar no sono, viram peças caindo, embora não lembrassem de ter jogado. Uma delas já punha os dedos nas teclas certas sem saber por quê.",
        "explicacao": (
            "A equipe de Robert Stickgold, da Escola de Medicina de Harvard, pôs 27 pessoas para jogar Tetris durante "
            "três dias: doze que nunca tinham jogado, dez especialistas com 50 a 500 horas de jogo e cinco pessoas com "
            "amnésia por lesões no hipocampo, sem memória de curto prazo. Os pesquisadores estudaram a fase de "
            "imagens que surge na primeira hora de sono, ao adormecer. Dezessete participantes relataram ver a mesma "
            "coisa: peças geométricas caindo, às vezes girando ou se encaixando. Ninguém viu a moldura da tela, o "
            "placar ou o teclado. A maior surpresa veio dos amnésicos: três dos cinco tiveram essas imagens, embora a "
            "maioria não se lembrasse do jogo de um dia para o outro e precisasse ser ensinada de novo. Um estudante "
            "da equipe notou que uma delas, sem lembrar do jogo, colocava os dedos nas teclas usadas para jogar logo "
            "no início da sessão. Para Stickgold, são memórias que guiam o comportamento sem chegar à consciência. Os "
            "resultados saíram na revista Science, e os autores os tomaram como sinal de que o cérebro usa o sono para "
            "reforçar o aprendizado. Dois especialistas, aliás, viram nas imagens não a versão do laboratório, mas a do "
            "Tetris da Nintendo que jogavam antes."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": "https://www.scientificamerican.com/article/tetris-dreams/",
             "titulo": "Tetris Dreams (Scientific American)", "idioma": "en",
             "trecho": "Robert Stickgold and his colleagues at Harvard Medical School recently conducted a clever set of experiments [...] "
                       "the brain uses dreaming to reinforce learning. They reported their findings in the October 13 issue of Science. [...] "
                       "Stickgold and his team probed yet a third phase of dreaming—the hypnagogic period that occurs within the first hour of sleep. "
                       "They studied three different sets of subjects who all played Tetris over the course of three days [...] "
                       "Twelve of their subjects had never before played the game. "
                       "Another 10 were experts who had logged between 50 and 500 hours of Tetris prior to the experiment. "
                       "And the remaining five were amnesiacs, having no short-term memory due to lesions in the hippocampus. [...] "
                       "Seventeen of these 27 subjects reported seeing the same images during hypnagogic sleep—namely falling geometric pieces [...] "
                       "Two of them, however, described Tetris images associated not with the version they played in the lab but with the version they had played on Nintendo machines [...] "
                       "Perhaps most surprising, three of the five amnesiacs described having the same kinds of hypnagogic dreams as the normal subjects. [...] "
                       "But even for these individuals, most of whom did not remember the game from one day to the next and had to be taught all over again, the Tetris dreams seemed to affect their waking behavior. "
                       "Co-author David Roddenberry, an undergraduate at Harvard, noticed that one of the amnesiacs who didn't remember the game nevertheless placed her fingers on the computer keys used in playing at the start of a session. [...] "
                       "\"In a way, this is Freud's unconscious—things activated in our brain that are in fact memories that guide our behavior but are not conscious.\" [...] "
                       "All the subjects dreamed of pieces falling and sometimes rotating or fitting into empty spaces—and none reported seeing the picture surrounding the pieces, the scoreboard or the keyboard."},
            wiki("Tetris_effect",
                "Stickgold et al. (2000) have proposed that Tetris effect imagery is a separate form of memory, likely related to procedural memory. "
                "This is from their research in which they showed that people with anterograde amnesia, unable to form new declarative memories, reported dreaming of falling shapes after playing Tetris during the day, despite not being able to remember playing the game at all.",
                nome="Tetris effect"),
        ],
    },
    # 17 o Master System no Brasil e a Turma da Mônica
    {
        "temas_secundarios": ["cultura_popular", "brasil_republica"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "O Master System perdeu para a Nintendo no Japão e nos EUA, mas no Brasil a Tectoy diz ter vendido 8 milhões de versões dele, ainda à venda, e transformou jogos japoneses em aventuras da Turma da Mônica.",
        "explicacao": (
            "O console da Sega não conseguiu tirar a liderança da Nintendo no Japão, na América do Norte e na maior "
            "parte da Europa Ocidental. No Brasil, a história foi outra. A Tectoy, fundada em 1987 com fábrica na Zona "
            "Franca de Manaus, convenceu a Sega a deixá-la cuidar de seus produtos aqui e lançou o Master System em "
            "setembro de 1989. A empresa criou um serviço de dicas por telefone, um clube de jogadores e um programa de "
            "dicas exibido nos intervalos da Sessão Aventura, da Rede Globo. A Nintendo só chegou oficialmente em 1993, "
            "quando o mercado já era dominado por clones do NES, e a Tectoy chegou a declarar 80% do mercado de "
            "videogames do país. Ela também adaptou jogos: títulos da série Wonder Boy viraram jogos da Turma da "
            "Mônica, Ghost House virou um jogo do Chapolim, e um jogo próprio do Pica-Pau nasceu depois que a empresa "
            "descobriu que ele era o desenho mais popular da TV brasileira. Como versões novas continuaram saindo por "
            "aqui, muitas publicações consideram o Master System o console de vida mais longa da história, título que "
            "antes era do Atari 2600. Em 2016, a Tectoy dizia ter vendido 8 milhões de unidades com a marca."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Master_System",
                "Though the Master System had newer, improved hardware, it failed to overturn Nintendo's market share advantage in Japan, North America, and most of Western Europe. [...] "
                "The Master System was also successful in Brazil, where it was launched in September 1989 and was distributed by Tectoy [...] "
                "Tectoy introduced a telephone service with game tips, created a Master System club, and presented the program Master Tips during commercial breaks of the television show Sessão Aventura on Rede Globo. "
                "Nintendo did not arrive in Brazil until 1993, and were unable to officially compete, as clones of the NES dominated the Brazilian market. "
                "Tectoy claimed 80% of the Brazilian video game market. [...] "
                "dedicated \"plug and play\" consoles emulating the original hardware continue to be sold by Tectoy [...] "
                "By 2016, Tectoy said they had sold 8 million units of Master System branded systems in Brazil. [...] "
                "certain Wonder Boy titles became Monica's Gang games, and Ghost House became Chapolim vs. Dracula: Um Duelo Assutador [...] "
                "the company developed Férias Frustradas do Pica-Pau after finding out that Woody Woodpecker (named Pica-Pau in Portuguese) was the most popular cartoon on Brazilian television [...] "
                "Due to the continued release of new variants in Brazil, the Master System is considered by many video gaming publications to be the longest lived gaming console in video games history, a title it took from the Atari 2600.",
                nome="Master System"),
            wiki("Tectoy",
                "Tectoy was founded in September 1987 by Daniel Dazcal, Leo Kryss, and Abe Kryss. [...] "
                "Tectoy set its factory in the Free Economic Zone of Manaus to leverage tax incentives. [...] "
                "The company slowly built trust with Sega and was ultimately granted total liberty to manage Sega products in the Brazilian market.",
                nome="Tectoy"),
        ],
    },
    # 18 Mario: o visual ditado pelos pixels e a história contestada do nome
    {
        "temas_secundarios": ["brinquedos"],
        "tipos_espanto": ["engenhosidade", "mito_desmentido"],
        "gancho": "O boné, o bigode e o macacão do Mario vieram da falta de pixels: o boné evitava desenhar e animar cabelo, e o bigode dispensava a boca. Já a história de que o nome veio de um senhorio cobrando aluguel é contestada.",
        "explicacao": (
            "Quando Shigeru Miyamoto criou o personagem para o Donkey Kong, de 1981, o hardware dos fliperamas era "
            "muito limitado. Para que o movimento dos braços aparecesse bem, vestiu-o com macacão e camisa de cores "
            "contrastantes entre si e com o fundo. O boné o livrou de desenhar penteado, testa e sobrancelhas, e "
            "também de animar o cabelo nos pulos. O nariz grande e o bigode davam um rosto humano sem precisar de boca "
            "nem de expressões faciais. No início ele nem se chamava Mario: era o Jumpman, o \"homem que pula\". O nome "
            "veio da filial americana da Nintendo e homenageia Mario Segale, dono do galpão que ela alugava. Segundo a "
            "versão mais difundida, Segale apareceu cobrando aluguel atrasado, discutiu com o presidente da filial e, "
            "depois de convencido de que seria pago, virou nome do personagem. Mas Don James, ex-gerente do depósito, "
            "contou outra coisa em 2012 e repetiu em 2018: ele e o presidente batizaram o personagem como piada, porque "
            "Segale era tão recluso que nenhum funcionário jamais o tinha visto."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Mario",
            "Due to the graphical limitations of arcade hardware at the time, Miyamoto clothed the character in red overalls and a blue shirt to contrast against each other and the background, making the movements of his arms easily perceptible. "
            "A red cap was added to let Miyamoto avoid drawing the character's hairstyle, forehead, and eyebrows, as well as to circumvent the issue of animating his hair as he jumped. "
            "To give distinctly human facial features with the limited graphical abilities, Miyamoto drew a large nose and a mustache, which avoided the need to draw a mouth and facial expressions. [...] "
            "During the development of Donkey Kong, Mario was known as Jumpman [...] "
            "he was named after Nintendo of America's landlord, Mario Segale. [...] "
            "According to a widely circulated story, during the localization of Donkey Kong for American audiences, Nintendo of America's warehouse landlord, Mario Segale, confronted then-president Minoru Arakawa, demanding back rent. "
            "Following a heated argument in which the Nintendo employees eventually convinced Segale he would be paid, they opted to name the character after him. "
            "This story is contradicted by former Nintendo of America warehouse manager Don James, who stated in 2012 that he and Arakawa named the character after Segale as a joke because Segale was so reclusive that none of the employees had ever met him. "
            "James repeated this account in 2018. [...] "
            "is a character created by Japanese video game designer Shigeru Miyamoto. [...] "
            "Donkey Kong (1981)",
            nome="Mario")],
    },
]
