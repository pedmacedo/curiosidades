LOTE = "2026-11-18-historia_esportes-01"
AREA = "esportes_jogos"
TEMA = "historia_esportes"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 os 42,195 km
    {
        "temas_secundarios": ["olimpiadas", "medidas_padroes"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "A maratona tem 42,195 km por causa da Olimpíada de Londres de 1908: a largada foi no Castelo de Windsor e a chegada, diante do camarote real. Em 1921, essa distância virou a oficial.",
        "explicacao": (
            "Para os Jogos de Londres, em 1908, o Comitê Olímpico Internacional combinou cerca de 25 "
            "milhas, uns 40 km. Os organizadores desenharam então um percurso de 26 milhas, saindo do Castelo de "
            "Windsor até a entrada real do estádio White City, seguido de uma volta na pista para terminar em "
            "frente ao camarote real. Depois, o trajeto foi alterado para usar outra entrada do estádio, com uma "
            "volta parcial de 385 jardas até o mesmo ponto de chegada. Em maio de 1921, a federação internacional "
            "de atletismo fixou a distância oficial da maratona copiando exatamente a de Londres: 42,195 "
            "quilômetros. Ou seja, os metros quebrados de toda maratona do mundo vêm do lugar onde a família real "
            "britânica assistia à prova."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Marathon",
            "The International Olympic Committee agreed in 1907 that the distance for the 1908 London Olympic marathon would be about 25 miles or 40 kilometers. "
            "The organizers decided on a course of 26 miles from the start at Windsor Castle to the royal entrance to the White City Stadium, followed by a lap (586 yards 2 feet; 536 m) of the track, finishing in front of the Royal Box. "
            "The course was later altered to use a different entrance to the stadium, followed by a partial lap of 385 yards to the same finish. "
            "The modern 42.195 km (26.219 mi) standard distance for the marathon was set by the International Amateur Athletic Federation (IAAF) in May 1921 directly from the length used at the 1908 Summer Olympics in London.",
            nome="Marathon")],
    },
    # 2 os atletas nus da Grécia
    {
        "temas_secundarios": ["grecia_antiga", "olimpiadas", "costumes_rituais"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Nas Olimpíadas da Grécia antiga, os atletas competiam nus. Segundo uma tradição antiga, o costume começou em 720 a.C., quando um corredor perdeu a roupa de propósito porque corria melhor sem ela.",
        "explicacao": (
            "Por boa parte da história dos Jogos Olímpicos antigos, as provas eram disputadas com os atletas nus, "
            "um hábito que os gregos viam como algo que os distinguia dos outros povos. Nem sempre foi assim: "
            "achados arqueológicos do fim do século VI antes de Cristo mostram atletas usando um tipo de tanga, o "
            "perizoma. Sobre a origem do costume há versões diferentes. O escritor Pausânias conta que o primeiro "
            "corredor nu foi Orsipo, vencedor da corrida do estádio em 720 antes de Cristo, que teria deixado a "
            "roupa cair de propósito porque correr sem ela era mais fácil. Já o historiador Tucídides, do século "
            "V antes de Cristo, atribui aos espartanos a introdução do hábito de tirar a roupa em público para os "
            "exercícios."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "consenso_parcial",
        "fontes": [wiki("Ancient_Olympic_Games",
            "as the perizoma was initially worn by athletes at the ancient Olympic Games. "
            "Archaeological evidence from late sixth-century BC reveals athletes sporting this garment during competitions. "
            "For most of its history, Olympic events were performed in the nude, a habit which the Greeks felt distinguished them from non-Greeks. "
            "Pausanias says that the first naked runner was Orsippus, winner of the stadion race in 720 BC, who simply lost his garment on purpose because running without it was easier. "
            "The 5th-century BC historian Thucydides credits the Spartans with introducing the custom of \"publicly strip",
            nome="Ancient Olympic Games")],
    },
    # 3 o basquete e os cestos de pêssego
    {
        "temas_secundarios": ["invencoes", "brinquedos"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "Nos primeiros jogos de basquete, a cesta era um cesto de pêssegos com fundo: a cada ponto, alguém tinha de tirar a bola. Os cestos só foram trocados por aros de metal em 1906.",
        "explicacao": (
            "Em 1891, o professor de educação física James Naismith, de Springfield, nos Estados Unidos, procurava "
            "um jogo vigoroso para manter os alunos ativos durante os longos invernos da Nova Inglaterra. Depois de descartar ideias violentas demais ou que não cabiam num ginásio fechado, inventou um "
            "jogo em que os jogadores passavam a bola entre si e tentavam marcar pontos jogando-a num cesto preso "
            "na parede. Naismith pregou um cesto de pêssegos numa pista elevada, ainda com o fundo, de modo que a "
            "bola tinha de ser retirada à mão depois de cada ponto. Como isso logo ficou cansativo, ele tirou o "
            "fundo, e a bola passou a ser empurrada para fora com uma vara comprida. No começo, a bola só andava "
            "por passes: o drible veio depois e já era comum em 1896. Os cestos de pêssego foram usados até 1906, "
            "quando deram lugar a aros de metal com tabela."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Basketball",
            "Invented in 1891 by Canadian-American gym teacher James Naismith in Springfield, Massachusetts, in the United States [...] "
            "He sought a vigorous indoor game to keep his students occupied and at proper levels of fitness during the long New England winters. "
            "After rejecting other ideas as either too rough or poorly suited to walled-in gymnasiums, he invented a new game in which players would pass a ball to teammates and try to score points by tossing the ball into a basket mounted on a wall. "
            "Naismith wrote the basic rules and nailed a peach basket onto an elevated track. "
            "Naismith initially set up the peach basket with its bottom intact, which meant that the ball had to be retrieved manually after each \"basket\" or point scored. "
            "This quickly proved tedious, so Naismith removed the bottom of the basket to allow the balls to be poked out with a long dowel after each scored basket. [...] "
            "Dribbling was common by 1896, with a rule against the double dribble by 1898. "
            "The peach baskets were used until 1906 when they were finally replaced by metal hoops with backboards.",
            nome="Basketball")],
    },
    # 4 o vôlei nasceu como "mintonette"
    {
        "temas_secundarios": ["invencoes", "olimpiadas"],
        "tipos_espanto": ["origem_inesperada"],
        "gancho": "O vôlei foi inventado em 1895 com outro nome, \"mintonette\", para ser uma alternativa menos cansativa ao basquete, criado quatro anos antes a poucos quilômetros dali.",
        "explicacao": (
            "Em 1895, William G. Morgan, diretor de educação física da ACM, a Associação Cristã de Moços, em "
            "Holyoke, no estado americano de Massachusetts, criou um jogo novo. Ele o chamou de \"mintonette\" e "
            "queria uma alternativa ao basquete que exigisse menos do corpo. O basquete tinha sido inventado em "
            "1891, também numa ACM de Massachusetts, em Springfield, cidade vizinha. O jogo de Morgan se "
            "espalhou depressa pela rede de associações da ACM nos Estados Unidos e no exterior. Mais tarde ganhou "
            "o nome de volleyball, de \"volley\", rebater a bola antes que ela toque o chão. O vôlei entrou no "
            "programa olímpico em Tóquio, em 1964, e o vôlei de praia, em Atlanta, em 1996."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Volleyball",
                "Volleyball was invented in 1895 by the American educator William G. Morgan, a YMCA physical education director in Holyoke, Massachusetts. "
                "Morgan intended the game, which he originally called \"mintonette\", to be an alternative to basketball that was less physically demanding. "
                "It spread rapidly through YMCA networks in the United States and abroad. [...] "
                "It has been part of the official program of the Summer Olympic Games since Tokyo 1964. "
                "Beach volleyball was introduced to the program at the Atlanta 1996 Summer Olympics.",
                nome="Volleyball"),
            wiki("Basketball",
                "Invented in 1891 by Canadian-American gym teacher James Naismith in Springfield, Massachusetts",
                nome="Basketball"),
        ],
    },
    # 5 o cabo de guerra olímpico
    {
        "temas_secundarios": ["olimpiadas", "esportes_tradicionais"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "O cabo de guerra foi esporte olímpico de 1900 a 1920. Como cada país podia inscrever mais de um clube, os Estados Unidos chegaram a levar as três medalhas, em 1904.",
        "explicacao": (
            "Hoje parece brincadeira de festa escolar, mas o cabo de guerra foi disputado como prova por equipes "
            "em todas as Olimpíadas de 1900 a 1920. No início, quem competia não eram seleções nacionais, mas "
            "clubes. Um mesmo país podia inscrever mais de um clube, o que permitia a uma única nação ganhar "
            "várias medalhas. Foi o que aconteceu nos Jogos de 1904, em Saint Louis, quando os Estados Unidos "
            "ficaram com as três. Depois de 1920, a prova saiu do programa olímpico."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Tug_of_war_at_the_Summer_Olympics",
            "Tug of war was contested as a team event in the Summer Olympics at the Games of every Olympiad from 1900 to 1920. "
            "Originally the competition was entered by groups called clubs. "
            "A country could enter more than one club in the competition, making it possible for one country to earn multiple medals. "
            "This happened in 1904, when the United States won al",
            nome="Tug of war at the Summer Olympics")],
    },
    # 6 medalhas olímpicas de arte
    {
        "temas_secundarios": ["olimpiadas", "literatura", "pintura"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "De 1912 a 1948, as Olimpíadas deram medalhas de arte: pintura, escultura, música, literatura e arquitetura. O próprio fundador dos Jogos, Coubertin, ganhou um ouro com um pseudônimo.",
        "explicacao": (
            "O barão Pierre de Coubertin, criador das Olimpíadas modernas, queria que os Jogos unissem esporte e "
            "arte. Por isso, de 1912 a 1948, houve competições oficiais de arte, com medalhas para obras inspiradas "
            "no esporte, em cinco categorias: arquitetura, literatura, música, pintura e escultura. O conjunto "
            "ganhou o apelido de \"Pentatlo das Musas\". Em 1912, o próprio Coubertin inscreveu um poema, \"Ode ao "
            "esporte\", assinado com os pseudônimos Georges Hohrod e Martin Eschbach, e levou a medalha de ouro de "
            "literatura. As competições acabaram depois de uma decisão do Comitê Olímpico Internacional, em 1949: "
            "como a maioria dos concorrentes era de artistas profissionais, a disputa contrariava o espírito "
            "amador exigido dos atletas. Desde então, as cidades-sede organizam exposições de arte, sem medalhas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Art_competitions_at_the_Summer_Olympics",
            "Art competitions formed part of the modern Olympic Games during its early years, from 1912 to 1948. "
            "The competitions were part of the original intention of the Olympic Movement's founder, Pierre de Frédy, Baron de Coubertin. "
            "Medals were awarded for works of art inspired by sport, divided into five categories: architecture, literature, music, painting, and sculpture, which led to the events' initial moniker of \"Pentathlon of the Muses\". "
            "The juried art competitions halted after a 1949 decision by the IOC that since the majority of art contestants worked as professional artists, the competitions contradicted the Olympic spirit of amateur competition, which was more strictly enforced for athletes. "
            "Art exhibitions replaced the competitions in the following years [...] "
            "In 1912 Pierre de Coubertin, under the pseudonym \"Georges Hohrod and Martin Eschbach\", entered Ode to sport, which won a gold medal in literature.",
            nome="Art competitions at the Summer Olympics")],
    },
    # 7 a maratona de 1904
    {
        "temas_secundarios": ["olimpiadas", "farmacos", "limites_humanos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Na maratona olímpica de 1904, o primeiro a chegar tinha feito parte do percurso de carro. O vencedor real terminou alucinando, depois de receber de seus treinadores conhaque, ovos crus e estricnina.",
        "explicacao": (
            "A maratona dos Jogos de 1904, em Saint Louis, nos Estados Unidos, foi um caos por causa da má "
            "organização e da arbitragem. Dos corredores de sete países que largaram, só 14 terminaram. Frederick "
            "Lorz foi recebido como vencedor, mas acabou desclassificado quando se descobriu que tinha pegado "
            "carona num carro em parte do caminho. O vencedor de verdade, Thomas Hicks, chegou quase desmaiando "
            "e tendo alucinações, efeito do que seus treinadores lhe deram durante a prova: conhaque, ovos crus e "
            "estricnina, um veneno que em doses pequenas era usado como estimulante. E o cubano Andarín Carvajal, "
            "que terminou em quarto, parou no meio da corrida para tirar um cochilo depois de comer maçãs "
            "estragadas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Athletics_at_the_1904_Summer_Olympics_%E2%80%93_Men%27s_marathon",
            "The men's marathon at the 1904 Summer Olympics in St. Louis, Missouri, United States, took place on August 30 of that year [...] "
            "coming from seven nations (the United States, France, Cuba, Greece, the Orange River Colony, Great Britain, and Canada) competed, only 14 managed to complete the race, which was a bizarre affair due to poor organization and officiating. "
            "Frederick Lorz was greeted as the apparent winner, but was later disqualified as he had hitched a ride in a car for part of the race. "
            "The actual winner, Thomas Hicks, was near collapse and hallucinating by the end of the race, a side effect of being administered brandy, raw eggs, and strychnine by his trainers. "
            "The fourth-place finisher, Andarín Carvajal, took a nap during the race after eating spoiled apples.",
            nome="Athletics at the 1904 Summer Olympics – Men's marathon")],
    },
    # 8 15, 30, 40 no tênis
    {
        "temas_secundarios": ["medidas_padroes", "calendarios"],
        "tipos_espanto": ["misterio_aberto", "mito_desmentido"],
        "gancho": "Ninguém sabe por que o tênis conta 15, 30, 40. A explicação mais famosa, a de um relógio no placar, esbarra num problema: na Idade Média os relógios quase não tinham ponteiro de minutos.",
        "explicacao": (
            "A contagem do tênis parece vir da França medieval. A referência mais antiga é uma balada de Charles "
            "d'Orléans, de 1435, que fala em \"quarante cinq\", 45, que depois virou 40. Em 1522 há uma frase em "
            "latim com \"30\" e \"45\". As primeiras teorias publicadas sobre a origem do 15 são de 1555 e 1579, "
            "mas a origem continua obscura. A teoria mais conhecida diz que se usava um mostrador de relógio para "
            "marcar o placar: cada ponto movia o ponteiro um quarto, para 15, 30 e 45, e chegar a 60 encerrava o "
            "game. O 45 teria virado 40 para caber a regra do empate, o deuce, com saltos de 10. O problema é a "
            "cronologia: as primeiras referências são do século XV, quando os relógios mostravam só as horas. Os "
            "ponteiros de minutos só se tornaram comuns por volta de 1690, com o pêndulo mais preciso."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Tennis_scoring_system",
            "The origins of the 15, 30, and 40 scores are believed to be medieval French. "
            "The earliest reference is in a ballad by Charles D'Orleans in 1435 which refers to quarante cinq (\"forty-five\"), which gave rise to modern 40. "
            "In 1522, there is a sentence in Latin, \"we are winning 30, we are winning 45\". "
            "The first recorded theories about the origin of 15 were published in 1555 and 1579. "
            "However, the origins of this convention remain obscure. "
            "Some believe that clock faces were used to keep score on court, with a quarter move of the minute hand to indicate a score of 15, 30, and 45. "
            "When the hand moved to 60, the game was over. [...] "
            "To make the score stay within the 60 ticks on the clock face, the 45 was changed to 40. [...] "
            "the first reference to tennis scoring (as mentioned above) is in the 15th century, and at that time clocks measured only the hours (1 to 12). "
            "It was not until about 1690, when the more accurate pendulum escapement was invented, that clocks regularly had minute hands.",
            nome="Tennis scoring system")],
    },
    # 9 o jogo de bola mesoamericano
    {
        "temas_secundarios": ["americas_pre_colombianas", "futebol", "costumes_rituais"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "Há pelo menos 3.600 anos, povos da Mesoamérica jogavam com bolas de borracha maciça de até 4,1 quilos. Quando jogadores foram levados à Espanha, os europeus se espantaram: nunca tinham visto bola quicar assim.",
        "explicacao": (
            "O jogo de bola mesoamericano, também chamado pok-ta-pok, é praticado desde pelo menos 1650 antes de "
            "Cristo por povos do atual México e da América Central. Na versão mais comum, os jogadores batiam na "
            "bola com os quadris, embora algumas variantes permitissem antebraços, raquetes ou bastões. A bola era "
            "de borracha natural maciça e podia pesar até 4,1 quilos. Os campos eram corredores longos e estreitos, "
            "com paredes onde a bola quicava. O jogo tinha um forte lado ritual, e as grandes partidas eram "
            "cerimônias. Depois da conquista, Hernán Cortés mandou um grupo de jogadores para se apresentar ao "
            "imperador Carlos V, na Espanha, e os europeus ficaram impressionados com as bolas de borracha que "
            "quicavam. Uma versão moderna do jogo, o ulama, ainda é praticada por indígenas no México."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Mesoamerican_ballgame",
            "also called pok-ta-pok, was a sport with ritual associations played since at least 1650 BCE (the middle Mesoamerican Preclassic period of the pre-Columbian era) by the people of Ancient Mesoamerica. [...] "
            "a modernized version of the game, ulama, is still played by the indigenous peoples of Mexico in some places. [...] "
            "In the most common theory of the game, the players struck the ball with their hips, although some versions allowed the use of forearms, rackets, bats, or handstones. "
            "The ball was made of solid natural rubber and weighed as much as 9 pounds (4.1 kg) [...] "
            "The game had important ritual aspects, and major formal ballgames were held as ritual events. [...] "
            "all have long, narrow alleys with slanted side-walls or vertical walls against which the balls could bounce. [...] "
            "Cortés sent a troupe of ōllamanime (ballplayers) to Spain to perform for Charles V [...] "
            "Besides the fascination with their exotic visitors, the Europeans were amazed by the bouncing rubber balls.",
            nome="Mesoamerican ballgame")],
    },
]
