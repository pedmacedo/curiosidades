LOTE = "2026-11-25-esportes_tradicionais-01"
AREA = "esportes_jogos"
TEMA = "esportes_tradicionais"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/", "de": "https://de.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


ISA_PARESI = "https://pib.socioambiental.org/pt/Povo:Paresí"
ISA_XAVANTE = "https://pib.socioambiental.org/pt/Povo:Xavante"
ISA_KRAHO = "https://pib.socioambiental.org/pt/Povo:Krahô"
HISTORIAR = "https://historiar.uvanet.br/index.php/1/article/download/445/375/1417"
AGENCIA_BRASIL = "https://agenciabrasil.ebc.com.br/geral/noticia/2015-10/jogos-mundiais-indigenas-nao-sao-olimpiadas-dos-povos-tradicionais"

CANDIDATOS = [
    # 1 o lacrosse indígena: mil jogadores, gols a quilômetros e um forte tomado
    {
        "temas_secundarios": ["povos_indigenas", "historia_esportes"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "Partidas indígenas de lacrosse chegavam a reunir de 100 a 1.000 homens, com gols a até 9,7 km um do outro. Em 1763, guerreiros ojíbuas usaram um desses jogos como ardil para entrar num forte britânico.",
        "explicacao": (
            "O lacrosse nasceu como jogo de povos indígenas do nordeste e do sudeste da América do Norte. "
            "As partidas tradicionais eram grandes acontecimentos, que podiam durar vários dias. De 100 a 1.000 "
            "homens de aldeias ou povos rivais se enfrentavam numa planície entre as duas aldeias, e os gols, "
            "marcados por pedras grandes ou árvores, ficavam a uma distância que ia de 460 metros a 9,7 quilômetros. "
            "As regras eram combinadas na véspera, em geral não havia linha lateral, ninguém podia tocar a bola com "
            "as mãos, e muitas vezes se jogava do nascer ao pôr do sol. O jogo servia para resolver disputas entre "
            "povos, para endurecer jovens guerreiros e também como oração coletiva. Em choctaw, um dos seus nomes "
            "quer dizer \"irmão menor da guerra\". Os primeiros europeus a vê-lo foram missionários jesuítas "
            "franceses, que o condenaram nos anos 1630; um deles, Jean de Brébeuf, registrou em 1637 os wendat "
            "jogando \"crosse\", e daí veio o nome. Em 4 de junho de 1763, durante a Guerra de Pontiac, um grupo "
            "de ojíbuas encenou uma partida do lado de fora do Forte Michilimackinac, no atual Michigan, como "
            "pretexto para entrar. Lá dentro, mataram a maior parte dos britânicos e mantiveram o forte por um ano."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("History_of_lacrosse",
                "Lacrosse has its origins in a tribal game played primarily by Northeastern and Southeastern Indigenous nations. [...] "
                "Ishtaboli or kapucha toli (\"little brother of war\") in Choctaw. [...] "
                "Traditional lacrosse games were sometimes major events that could last several days. "
                "As many as 100 to 1,000 men from opposing villages or tribes would participate. "
                "The games were played in open plains located between the two villages, and the goals could range from 500 yards (460 m) to 6 miles (9.7 km) apart. "
                "Rules for these games were decided on the day before. "
                "Generally, there were no out-of-bounds, and the ball could not be touched with the hands. "
                "The goals would be selected as large rocks or trees; in later years wooden posts were used. "
                "Playing time was often from sunup until sundown. [...] "
                "Some games were played to settle inter-tribal disputes. [...] "
                "Lacrosse was also played to toughen young warriors for combat, for recreation, as part of festivals, and for the bets involved. "
                "Finally, lacrosse was played for religious reasons: \"for the pleasure of the Creator,\" and to collectively pray for something. [...] "
                "The first westerners to encounter lacrosse were French Jesuit missionaries in the St. Lawrence Valley. "
                "During the 1630s, they witnessed the game and condemned it. [...] "
                "One missionary, Jean de Brébeuf, was the first to write about lacrosse and thus gave it its name. "
                "He described the Wendat (Huron) in present-day Ontario playing \"crosse\" in 1637.",
                nome="History of lacrosse"),
            wiki("Fort_Michilimackinac",
                "it was built on the northern tip of the lower peninsula of the present-day state of Michigan in the United States. [...] "
                "On June 4, 1763, as part of the larger conflict known as Pontiac's War, a group of Ojibwe staged a game of baaga'adowe (a forerunner of modern lacrosse) outside the fort as a ruse to gain entrance. "
                "After entering the fort, they killed most of the British inhabitants. "
                "They held the fort for a year before the British regained control",
                nome="Fort Michilimackinac"),
        ],
    },
    # 2 a seleção haudenosaunee e os passaportes próprios
    {
        "temas_secundarios": ["fronteiras_paises", "povos_indigenas"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "A confederação indígena haudenosaunee tem seleção de lacrosse e passaporte próprios. Em 2010, o Reino Unido não aceitou esses documentos, e o time ficou fora do Mundial para não viajar como americano ou canadense.",
        "explicacao": (
            "Para os haudenosaunee, também chamados de iroqueses, o lacrosse nasceu como prática espiritual de "
            "louvor e agradecimento ao Criador. Os meninos ganham um pequeno taco de madeira ao nascer, dormem com "
            "o taco por perto a vida toda e são enterrados com ele. A seleção masculina foi criada em 1983 pelo "
            "Grande Conselho da confederação e, em 1988, foi aceita como membro pleno pela federação internacional. "
            "É a única equipe de uma Primeira Nação com reconhecimento internacional como povo soberano. A "
            "confederação emite passaportes próprios desde os anos 1920, e o time chegou a excursionar pela "
            "Inglaterra com eles nos anos 1980. Depois dos atentados de 11 de setembro, porém, os países da União "
            "Europeia deixaram de reconhecê-los. Em 2010, para o Mundial de Manchester, o Reino Unido recusou os "
            "documentos e mandou os 23 jogadores usarem passaportes americanos ou canadenses, a que tinham direito. "
            "Eles se negaram, dizendo que seria um golpe contra sua identidade, e perderam os três jogos da primeira "
            "fase. O time foi bronze no Mundial de 2018, e em 2022 a Irlanda aceitou os passaportes num campeonato "
            "sub-21. Em janeiro de 2025, os governos dos Estados Unidos e do Canadá pediram ao Comitê Olímpico "
            "Internacional que deixasse os haudenosaunee jogarem a Olimpíada de 2028 com bandeira própria."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Haudenosaunee_men's_national_lacrosse_team",
                "The Haudenosaunee Nationals Men's Lacrosse Team, formerly known as the Iroquois Nationals, represents the Haudenosaunee Confederacy in international field lacrosse competition. "
                "They are currently ranked third in the world by World Lacrosse after winning Bronze at the 2018 World Lacrosse Championship. [...] "
                "Lacrosse was originally played as part of a spiritual endeavour meant to praise and give thanks to the Creator [...] "
                "Specifically, males are given a miniature wooden lacrosse stick at birth, sleep with their stick nearby throughout their life, and even take one to the grave. [...] "
                "The Iroquois Nationals men's lacrosse team was formed and sanctioned by the Grand Council of the Haudenosaunee in 1983 [...] "
                "Prior to the 1984 Summer Olympics [...] "
                "The following year, using their Haudenosaunee passports, the Nationals traveled and toured England losing only once. "
                "The Haudenosaunee Nationals team is the only First Nation's team with international recognition as a sovereign people. [...] "
                "The ILF accepted the Iroquois as a full member nation in 1988. [...] "
                "The Haudenosaunee Confederacy began issuing their own passports in 1927 and its holders were able to travel without problem for many years. "
                "However, with stricter security measures following the 9/11 terrorist attack, the European Union member states no longer recognized these passports as legal travel documents. [...] "
                "These passports became an issue when the Iroquois Nationals attempted to enter England for the 2010 World Lacrosse Championship held in Manchester. [...] "
                "The Nationals’ players were told by British officials to obtain either U.S. or Canadian passports if they wished to enter the country, as the team's 23 players were eligible to be issued passports from these countries. "
                "The Iroquois Nationals refused to travel with Canadian or American passports, arguing that this would be a strike against their identity. "
                "As a result, the Nationals were forced to forfeit their three preliminary games. [...] "
                "On January 17, 2025, U.S. President Joe Biden and Canadian Prime Minister Justin Trudeau released a joint statement from the White House calling on the International Olympic Committee (IOC) to allow the Haudenosaunee to compete in lacrosse at the 2028 Los Angeles Olympic Games as their own team under their own flag.",
                nome="Haudenosaunee men's national lacrosse team"),
            wiki("Haudenosaunee_passport",
                "The Haudenosaunee government has issued passports since at least 1923, when Haudenosaunee authorities issued a passport to Cayuga statesman Deskaheh to travel to the League of Nations headquarters in Geneva. [...] "
                "In August 2022, Ireland acknowledged and accepted Haudenosaunee passports for the 2022 Under 21 World Lacrosse Championship.",
                nome="Haudenosaunee passport"),
        ],
    },
    # 3 o ulama, herdeiro vivo do jogo de bola mesoamericano
    {
        "temas_secundarios": ["americas_pre_colombianas", "historia_esportes"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "No México, ainda se joga o ulama, herdeiro do jogo de bola dos astecas: uma bola maciça de borracha de 3 a 4 kg só pode ser rebatida com o quadril. É tido como um dos esportes mais antigos ainda praticados.",
        "explicacao": (
            "O ulama descende da versão asteca do jogo de bola mesoamericano, cujas raízes vão pelo menos ao "
            "segundo milênio antes de Cristo: arqueólogos já acharam bolas de borracha de pelo menos 1600 a.C. e "
            "quase 1.500 quadras antigas. Por causa dos seus aspectos religiosos e rituais, os católicos espanhóis "
            "reprimiram o jogo logo depois da conquista, mas ele sobreviveu onde a influência espanhola foi mais "
            "fraca, como em comunidades do estado de Sinaloa. Hoje passa por um renascimento e tem até um centro "
            "cultural na Cidade do México. Na versão de quadril, cada time tem cinco ou mais jogadores, de tanga "
            "e com protetores de couro no quadril contra a bola pesada. É o mesmo traje das estatuetas mais "
            "antigas de jogadores: quase 3 mil anos de roupa igual. A quadra é traçada na terra e dividida por uma "
            "linha central. O objetivo é manter a bola em jogo, e perde ponto o time que a deixa sair, que a toca "
            "com outra parte do corpo ou até que se esquece de anunciar o placar. Como certas situações zeram a "
            "contagem, as partidas podem ser longas. E o jogo machuca: os jogadores de hoje vivem cheios de "
            "hematomas, e um cronista espanhol de quase 500 anos atrás relatou mortes causadas pela bola."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Ulama_(game)",
                "is a ball game played in Mexico, currently experiencing a revival from its home in a few communities in the state of Sinaloa. "
                "As a descendant of the Aztec version of the Mesoamerican ballgame, the game is regarded as one of the oldest continuously played sports in the world [...] "
                "The roots of ōllamaliztli extend back to at least the 2nd millennium BC [...] "
                "Archaeologists have uncovered rubber balls dating to at least 1600 BC, ballgamer figures from at least 1200 BC, and nearly 1,500 ancient ball courts. "
                "Due to its religious and ritual aspects, Spanish Catholics suppressed the game soon after the Spanish conquest. "
                "It survived in areas such as Sinaloa, where Spanish influence was less pervasive. "
                "As part of its nationwide revival, the game now has a home in the capital Mexico City, at a cultural centre in the Azcapotzalco neighborhood. [...] "
                "The bounds of these long narrow courts are made by drawing or chalking thick lines in the dirt. "
                "The courts are divided into opposing sides by a center line [...] "
                "The scoring system provides for resetting the score to zero under certain conditions, which can make for lengthy games. [...] "
                "A hip ulama team consists of five or more players (but there could be as many as twelve) wearing loincloths, with leather hip pads for some protection against the heavy (3–4 kg, around 7–9 lb) rubber ball. [...] "
                "The object of the game is to keep the ball in play and in-bounds. [...] "
                "A team scores a point when a player of the opposing team hits the ball out of turn, misses the ball, knocks the ball out of bounds, touches the ball with any part of the body aside from the hip, accidentally touches a teammate, lets the ball stop moving before it reaches the center line, or even if they fail to announce the score after they have scored a point.",
                nome="Ulama (game)"),
            wiki("Mesoamerican_ballgame",
                "Today's hip-ulama players are \"perpetually bruised\" while nearly 500 years ago Spanish chronicler Diego Durán reported that some bruises were so severe that they had to be lanced open. "
                "He also reported that players were even killed when the ball \"hit them in the mouth or the stomach or the intestines\". [...] "
                "Loincloths are found on the earliest ballplayer figurines from Tlatilco, Tlapacoya, and the Olmec culture, are depicted in the Weiditz drawing from 1528, and, with hip guards, are the sole outfit of contemporary ulama players (above)—a span of nearly 3000 years.",
                nome="Mesoamerican ballgame"),
        ],
    },
    # 4 o zikonahiti dos Paresí: futebol de cabeça que só acaba quando os dois vencem
    {
        "temas_secundarios": ["povos_indigenas", "futebol"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Os Paresí, de Mato Grosso, jogam uma espécie de futebol só de cabeça, o zikonahiti. Uma disputa entre aldeias só chega ao fim quando as duas equipes tiverem vencido, o que pode levar até um mês.",
        "explicacao": (
            "O zikonahiti é um jogo masculino dos Paresí, que se autodenominam Haliti. A bola, de mangaba e com "
            "cerca de 13 centímetros de diâmetro, é lançada com golpes de cabeça entre duas equipes, num campo "
            "retangular dividido ao meio por uma linha riscada no chão. Cada time reúne homens da mesma aldeia ou "
            "que se consideram \"parentes verdadeiros\". Para haver jogo, uma aldeia convida a outra, e o convite, "
            "que os Paresí chamam de \"desafio\", não pode ser recusado. Antes de cada partida, os jogadores "
            "entregam ao apostador do seu time objetos como anzóis, linhas de pesca, pentes e sabonetes, e as "
            "apostas se repetem até que não haja mais nada a apostar. Em geral, o jogo é suspenso quando uma "
            "equipe esgota suas coisas, mas ele só termina de fato quando ambas tiverem alcançado a vitória. Em "
            "novembro de 1922, no centenário da Independência, os Paresí jogaram no estádio das Laranjeiras, do "
            "Fluminense, então o maior da América Latina. Os jornais do Rio, que grafavam o nome como "
            "\"zicunati\", tentaram enquadrá-lo como um \"futebol indígena\". Segundo um estudo de 2022, porém, o "
            "jogo dos Haliti está ligado à sua concepção ritual e foge da lógica competitiva do futebol daquela época."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": ISA_PARESI,
             "titulo": "Paresí (Povos Indígenas no Brasil, Instituto Socioambiental)",
             "idioma": "pt",
             "trecho": (
                 "O zikonahiti é um jogo masculino disputado com uma bola de mangaba, designada igomaliró, com cerca de 13 cm de diâmetro. "
                 "A principal característica do jogo é o arremesso da bola, com um golpe de cabeça, entre equipes dispostas em um campo retangular dividido em duas partes por uma linha riscada no solo. "
                 "Cada equipe é formada por homens de um mesmo grupo local ou por indivíduos que se consideram ihinaiharé kaisereharé (“parente verdadeiro”). "
                 "Para que haja o jogo é preciso que uma aldeia convide a outra. "
                 "O convite é irrecusável; [...] Os Paresí referem-se ao convite por “desafio”. [...] "
                 "Antes de o jogo ser iniciado cada jogador entrega aos apostadores objetos variados como caixas de fósforo, linhas de pesca, anzois, pentes, sabonetes, peças de vestuário, armas, munição, que serão apostados. [...] "
                 "As apostas são feitas antes de cada partida, e se sucedem até que os apostadores não tenham mais o que apostar. "
                 "Em geral suspende-se o jogo quando uma das equipes esgota sua provisão de coisas, e então o apostador da outra equipe distribui o resultado pelos jogadores. "
                 "Entretanto, um jogo só chega ao final quando ambas as equipes alcançam a vitória, o que pode levar até um mês."
             )},
            {"url": HISTORIAR,
             "titulo": "Entre o zikonahiti e o football: a pátria em jogo nos jornais da capital federal no Centenário da Independência (1922) (Revista Historiar, 2022)",
             "idioma": "pt",
             "trecho": (
                 "escolhemos utilizá-lo assim em detrimento da autodenominação: Halitis, por conta do amplo emprego de sua forma anterior pelos jornais e textos de época. "
                 "3 ZICUNATI, a partida de hontem disputada pelos indios parecis. O Paiz, Sports: Foot-ball,Turf, Rowing e outros. Rio de Janeiro, p. 5. 27/11/1922. [...] "
                 "A apresentação no Centenário foi modelo representativo [...] "
                 "O estádio das Laranjeiras, construído em 1919 para sediar o campeonato sulamericano de futebol, era naquele período o maior da América Latina. 14 Sede do Fluminense F.C. [...] "
                 "Revista Historiar | Vol. 14 | Nº. 27 | Jul./Dez. de 2022 [...] "
                 "tentando fazer do zikonahiti um “futebol indígena”. [...] "
                 "está intrinsecamente relacionado à concepção ritualística dos Haliti, fugindo da perspectiva competitiva ou do lazer, encontrados no futebol naquela altura."
             )},
        ],
    },
    # 5 Jogos Mundiais dos Povos Indígenas: "o importante não é ganhar, e sim celebrar"
    {
        "temas_secundarios": ["povos_indigenas", "olimpiadas"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Os primeiros Jogos Mundiais dos Povos Indígenas, em Palmas (TO), em 2015, tinham o lema \"o importante não é ganhar, e sim celebrar\". O regulamento previa o mesmo prêmio para os quatro melhores de cada prova.",
        "explicacao": (
            "Os Jogos dos Povos Indígenas foram criados em 1996, por iniciativa indígena, e a primeira edição foi "
            "em Goiânia. Em 2015, ganharam uma versão mundial, marcada para outubro, em Palmas, no Tocantins, com "
            "cerca de 2.300 atletas previstos, de 22 etnias brasileiras e de 20 países. A organização ficou com o "
            "Comitê Intertribal, cujo articulador internacional, Marcos Terena, dizia que o evento não era uma "
            "competição entre etnias nem uma busca por medalhas: \"Competir vai contra o pensamento dos povos "
            "indígenas\". Os chamados esportes de integração, como arco e flecha, arremesso de lança, cabo de força, "
            "canoagem e corrida com tora, tinham eliminatórias e finais, mas, em vez de medalhas de valores "
            "diferentes para os três primeiros, os quatro melhores receberiam o mesmo prêmio. Os equipamentos "
            "tinham de seguir a tradição indígena: na natação, óculos e touca eram vetados, e nos 100 metros todos "
            "correriam descalços. Como cada povo faz suas canoas, lanças, cordas e toras do seu jeito, a "
            "organização decidiu padronizar esses itens. Além disso, os povos podiam mostrar jogos próprios, sem "
            "caráter competitivo, como o futebol de cabeça dos Paresi e o peikrãn dos Kayapó, com uma peteca de "
            "palha de milho. O único esporte ocidental do programa era o futebol."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": AGENCIA_BRASIL,
             "titulo": "Jogos Mundiais Indígenas não são as \"Olimpíadas\" dos povos tradicionais (Agência Brasil, 2015)",
             "idioma": "pt",
             "trecho": (
                 "Publicado em 16/10/2015 [...] "
                 "a primeira edição dos Jogos Mundiais dos Povos Indígenas (JMPI), marcada entre os dias 20 e 31 de outubro, em Palmas (TO). [...] "
                 "desde o lema adotado - “o importante não é ganhar, e sim celebrar” - até a inclusão de jogos demonstrativos em seu programa. [...] "
                 "Não é uma competição entre etnias, tampouco uma busca por medalhas”, aponta Marcos Terena, articulador internacional do Comitê Intertribal Memória e Ciência Indígena (ITC), que está à frente da organização dos Jogos, que vão reunir cerca de 2.300 atletas de 22 etnias brasileiras e de 20 países. [...] "
                 "O jikunahati (futebol de cabeça), do povo Paresi; [...] e o Peikrãn (jogo onde uma peteca feita de palha de milho é arremessada entre os jogadores), praticado pelos Kayapós, já estão na lista de jogos demonstrativos. "
                 "Mesmo contando com fase eliminatória e finais, os chamados esportes de integração (arremesso de lança, arco e flecha, cabo de força, canoagem, corrida de velocidade, corrida de fundo, corrida com tora e natação) têm um sistema de premiação próprio e, por vezes, fogem do modelo não indígena. "
                 "Em vez de conferir aos três primeiros colocados medalhas de pesos e simbolismo distintos, os quatro melhores receberão o mesmo prêmio. "
                 "Outra exigência é a utilização de equipamentos confeccionados de acordo com a tradição indígena, vedado o uso de materiais que mudem o ritmo na corrida de velocidade ou óculos e touca na natação. "
                 "“Quando vira apenas um campeonato, perde-se a fraternidade e a reciprocidade dos povos. Competir vai contra o pensamento dos povos indígenas”, explica Terena. [...] "
                 "Uma das definições foi a padronização das canoas, das lanças, das cordas do cabo de força e das toras utilizadas na corrida, uma vez que cada etnia confecciona esses equipamentos de maneira própria. [...] "
                 "Na corrida de rua de 100 metros, por exemplo, a regra é que todos corram descalços. [...] "
                 "o futebol é o único esporte ocidental que estará nos Jogos Mundiais."
             )},
            wiki("Jogos_dos_Povos_Indígenas",
                "Os Jogos dos Povos Indígenas é um evento multiesportivo, criado em 1996 por meio de uma iniciativa indígena brasileira, do Comitê Intertribal - Memória e Ciência Indígena (ITC), com o apoio do Ministério do Esporte do Brasil. [...] "
                "O primeiro foi realizado em Goiânia, capital do estado de Goiás. "
                "Em 2015, o evento tem sua primeira edição mundial e se torna Jogos Mundiais dos Povos Indígenas.",
                nome="Jogos dos Povos Indígenas", idioma="pt"),
        ],
    },
    # 6 a corrida de toras: 80 quilos no ombro, em revezamento
    {
        "temas_secundarios": ["povos_indigenas", "costumes_rituais"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "Na corrida de toras dos Xavante, os corredores se revezam carregando no ombro uma tora de buriti de uns 80 kg (60 kg, na prova das mulheres) por seis a oito quilômetros, até o centro da aldeia.",
        "explicacao": (
            "Entre os Xavante, a corrida de revezamento com toras de buriti se chama uiwede e é uma das suas "
            "atividades esportivas favoritas. Cada corredor dá tudo de si num trecho curto e depois passa a tora "
            "para o ombro de um companheiro de time que o espera, da mesma classe de idade ou da mesma metade. Os "
            "times são formados por classes de idade de metades opostas da aldeia, e a disputa alimenta uma "
            "rivalidade em tom de brincadeira entre elas. As corridas são sempre entre pessoas do mesmo sexo, só "
            "adultos carregam a tora, e toda a comunidade em condições físicas acompanha o trajeto. Entre os "
            "Krahô, a corrida de toras está sempre ligada a um rito em andamento: o par de toras, "
            "geralmente de buriti, é feito com cuidado a cada disputa, com tamanho, formato e ornamentos de acordo "
            "com o rito. Por volta de 1952, um movimento messiânico surgiu entre eles. Um xamã passou a ter visões, e nelas lhe foi "
            "prometido que, numa certa data, os brancos virariam indígenas e os Krahô virariam brancos, desde que "
            "eles abandonassem as corridas de toras e as pinturas de corpo, entre outros costumes. Nada do previsto aconteceu."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": ISA_XAVANTE,
             "titulo": "Xavante (Povos Indígenas no Brasil, Instituto Socioambiental)",
             "idioma": "pt",
             "trecho": (
                 "Duas outras competições esportivas cerimoniais que os Xavante apreciam são as lutas corporais wa’i e as corridas de revezamento com toras de buriti, chamadas uiwede. "
                 "Elas incitam e exibem rivalidades jocosas entre as metades ágamas opostas [...] "
                 "Nas corridas de revezamento, cada participante esforça-se ao máximo ao longo de trechos curtos, portando sobre os ombros uma enorme e pesada tora de buriti (aproximadamente 80 quilos para os homens e 60 para as mulheres). "
                 "Em seguida, trata de transferir a tora aos ombros de algum outro membro de seu “time”, da mesma classe de idade ou da mesma metade ágama que ele, que fica à espera. "
                 "Essas toras extremamente pesadas são transportadas pelos corredores ao longo de trajetos de extensão aproximada entre seis e oito quilômetros, que terminam no centro da aldeia. "
                 "As corridas sempre envolvem pessoas do mesmo sexo e opõem times compostos, cada qual, por classes de idade das metades ágamas. "
                 "Apenas adultos podem transportar as toras. "
                 "Contudo, essas corridas são acompanhadas por todos os membros fisicamente aptos da comunidade, o que faz delas eventos excepcionalmente animados e divertidos. "
                 "O correr com toras é, sem dúvida, uma das atividades esportivas favoritas dos Xavante."
             )},
            {"url": ISA_KRAHO,
             "titulo": "Krahô (Povos Indígenas no Brasil, Instituto Socioambiental)",
             "idioma": "pt",
             "trecho": (
                 "um movimento messiânico entre os Krahô por volta de 1952. "
                 "Um xamã começou a ter visões [...] "
                 "foi-lhe prometido que em determinada data os civilizados iriam se transformar em índios e os Krahô em civilizados. "
                 "Para tanto os Krahô tinham de comportar-se de maneira a propiciar a transformação: abandonar as corridas de toras, as pinturas de corpo, fazer bailes como os dos sertanejos, consumir seus animais domésticos. [...] "
                 "Entretanto, nada do previsto aconteceu [...] "
                 "O par de toras para corrida é cuidadosamente confeccionado, geralmente de tronco de buriti, cada vez que a disputa começa fora da aldeia. [...] "
                 "A corrida de toras sempre está ligada a um rito em andamento, de modo que o tamanho, formato e ornamentação das toras devem estar a ele conformes. "
                 "Cada tora é carregada por um corredor, que deve passá-la a um companheiro da mesma metade."
             )},
        ],
    },
    # 7 a peteca que virou indiaca na Alemanha
    {
        "temas_secundarios": ["povos_indigenas", "brinquedos"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "A peteca, de origem indígena, virou esporte na Alemanha: em 1936, um professor alemão viu jovens jogando na praia de Copacabana e levou o jogo para casa. Lá ele ganhou o nome de indiaca.",
        "explicacao": (
            "O nome peteca vem do verbo tupi petek, que quer dizer golpear com a mão espalmada, e o jogo é de "
            "origem indígena brasileira. As primeiras petecas eram feitas em casa, com pedras envoltas em folhas e "
            "amarradas dentro de uma espiga de milho. Na Olimpíada de Antuérpia, em 1920, a primeira do Brasil, os "
            "atletas brasileiros levaram petecas para se distrair no navio e nos intervalos, e atletas de outros "
            "países quiseram aprender as regras. O problema é que não havia regras: era só diversão. Elas foram "
            "escritas em Belo Horizonte, onde, nos anos 1940, a peteca virou esporte de quadra e ganhou "
            "o formato atual, com quatro penas brancas presas a uma base de camadas finas de borracha. Na "
            "Alemanha, a história foi outra. Em 1936, o professor de esportes Karlhans Krohn, de Colônia, "
            "passeava pela praia de Copacabana quando viu jovens jogando peteca e levou o jogo consigo. Depois da "
            "Segunda Guerra, ele se espalhou por grupos de jovens de igrejas e pela ACM alemã com o nome de indiaca, "
            "junção de \"Indianer\" (indígena, em alemão) e peteca. Lá, um time pode ter cinco jogadores, e no "
            "Brasil, no máximo dois."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Peteca",
                "Early petecas were home-made affairs consisting of stones wrapped in leaves tied inside an ear of corn. [...] "
                "When Brazil was present at the 1920 Summer Olympics in Antwerp, Belgium the Brazilian athletes took with them some shuttlecocks for amusement on the ship and during the intervals between games. "
                "The game of peteca fascinated athletes from many other countries who wanted learn the rules of the game. "
                "The problem was that there were no rules - it was just for pleasure. "
                "Peteca left the streets, the grass and the sand to become a field sport in Belo Horizonte in the 1940s. "
                "It was in Belo Horizonte, the capital city of Minas Gerais state, that the toy shape was transformed to its current format, proper for competitive games. "
                "The typical peteca has four white chicken feathers attached to a base and connected to a bottom made with several thin layers of rubber. "
                "It was also in Belo Horizonte that the rules of the game were first written",
                nome="Peteca"),
            wiki("Peteca",
                "Peteca (do verbo tupi petek, bater, espalmar) é o nome dado tanto a um esporte quanto ao artefato esportivo utilizado em sua prática, sendo ambos de origem indígena brasileira. [...] "
                "O nome \"peteca\" vem do verbo petek do tupi e significa \"esbofetear, golpear com a mão espalmada\"",
                nome="Peteca", idioma="pt"),
            wiki("Indiaca",
                "In the VII Olympic games held in Antwerp (Belgium) in 1920, the Brazilians, who were participating in their first Olympics [...] "
                "The rules of the game are not the same worldwide. "
                "For example, in Brazil Peteca is played with a maximum of two players per team, whereas in Germany a team can have five players.",
                nome="Indiaca"),
            wiki("Indiaca",
                "1936 beobachtete der deutsche Sportlehrer Karlhans Krohn aus Köln beim Spaziergang am Strand von Copacabana Jugendliche beim Peteca-Spiel und brachte das Spiel mit nach Deutschland. "
                "Nach dem Zweiten Weltkrieg verbreitete es sich unter dem Namen „Indiaca“ (als Kofferwort aus „Indianer“ und „Peteca“) zuerst in der kirchlichen Jugendarbeit und im CVJM.",
                nome="Indiaca", idioma="de"),
        ],
    },
    # 8 calcio storico: futebol de briga jogado sob cerco
    {
        "temas_secundarios": ["europa_medieval", "historia_esportes"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1530, com Florença cercada pelas tropas do imperador Carlos V, a cidade fez uma partida de calcio na praça, em desafio aos sitiantes. O jogo, mistura de futebol e luta, ainda é disputado lá todo mês de junho.",
        "explicacao": (
            "O calcio storico é uma forma antiga de futebol que surgiu na Idade Média e ainda é jogada em "
            "Florença. O nome \"calcio\" acabou virando a palavra italiana para o futebol moderno. Em 17 de "
            "fevereiro de 1530, com a cidade sitiada, os florentinos disputaram uma partida na Piazza Santa Croce, "
            "só com soldados de destaque, senhores, nobres e príncipes. O interesse pelo jogo minguou no início do "
            "século XVII, e ele foi reorganizado em 1930, sob Mussolini. Hoje são três partidas por ano na mesma "
            "praça, com um time de cada bairro histórico, e a final cai em 24 de junho, dia de São João Batista, o "
            "padroeiro da cidade. Cada equipe tem 27 jogadores, sem substituições, num campo coberto de areia, e "
            "valem cabeçadas, socos, cotoveladas e estrangulamentos. Por causa de lesões muitas vezes fatais, "
            "golpes traiçoeiros e chutes na cabeça foram proibidos. Torneios já foram cancelados por violência, e "
            "hoje os jogadores precisam ter nascido em Florença ou morar lá há pelo menos dez anos, sem "
            "condenações criminais. O vencedor já levou uma vaca da raça chianina; hoje o prêmio se resume a um "
            "jantar, e os jogadores não ganham mais nada."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Calcio_storico_fiorentino",
                "is an early form of football that originated during the Middle Ages in Italy and is still played in Florence. [...] "
                "There it became known as the giuoco del calcio fiorentino or simply calcio, which is now also the name for association football in the Italian language. [...] "
                "On a famous occasion, the city of Florence held a match on 17 February 1530, in defiance of the imperial troops sent by Emperor Charles V, as the city was under siege. "
                "The \"noble game\" was played in Piazza Santa Croce, only by distinguished soldiers, lords, noblemen and princes. [...] "
                "Interest in calcio waned in the early 17th century. "
                "However, in 1930 it was reorganised as a game in the Kingdom of Italy, under Benito Mussolini. [...] "
                "Today, three matches are played each year in Piazza Santa Croce, in Florence, in the third week of June. "
                "A team from each quartiere of the city is represented [...] "
                "the two winners go into the final, held annually on 24 June, the feast of Saint John the Baptist, the patron saint of Florence. [...] "
                "The modern version of calcio has not changed much from its historical roots, which allow tactics such as head-butting, punching, elbowing, and choking. "
                "However, due to often fatal injuries, sucker punches and kicks to the head are currently banned. [...] "
                "Tournaments have been cancelled on several occasions due to violence or foul play. "
                "These incidents have led to major rule changes, such as ensuring players are born in Florence (or have been resident for at least ten years) and excluding players that have criminal convictions. [...] "
                "Matches last 50 minutes and are played on a field covered in sand [...] "
                "Each team has 27 players and no substitutions are allowed for injured or expelled players. [...] "
                "Along with the pallio, the winning team used to receive a Chianina, a type of pure-bred cow. "
                "However, this has been reduced to a free dinner for the winning team; the players earn no other compensation.",
                nome="Calcio storico fiorentino"),
        ],
    },
    # 9 buzkashi: polo com carcaça de cabra
    {
        "temas_secundarios": ["costumes_rituais"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "No buzkashi, esporte nacional do Afeganistão, cavaleiros disputam uma carcaça de cabra. No Quirguistão, o jogo se chama kok-boru, \"lobo cinzento\": os pastores teriam começado jogando com um lobo morto.",
        "explicacao": (
            "Buzkashi quer dizer \"puxar a cabra\" em persa. No jogo, cavaleiros tentam levar uma carcaça de "
            "cabra ou de bezerro até uma área de gol. Ele começou entre tribos nômades túrquicas das estepes da "
            "Eurásia e se espalhou para o oeste, rumo ao Afeganistão, entre os séculos X e XV. Hoje é jogado com "
            "outros nomes por cazaques, quirguizes, uzbeques, tadjiques e outros povos, e entre os tadjiques de "
            "Xinjiang, na China, existe até uma versão montada em iaque. No Quirguistão, o nome kok-boru significa "
            "\"lobo cinzento\", porque, segundo a explicação corrente, os pastores que começaram a jogar usavam a "
            "carcaça de um lobo. Tradicionalmente, uma partida podia durar vários dias. Os jogadores usam roupas "
            "pesadas e proteção na cabeça contra os chicotes e as botas dos rivais; na antiga União Soviética, "
            "muitos aproveitam capacetes de tanquistas soviéticos. As botas têm salto alto, que se trava na sela "
            "para o cavaleiro poder se debruçar pela lateral do cavalo e apanhar a carcaça. No Afeganistão, onde é "
            "o esporte nacional, o Talibã proibiu o jogo como imoral no seu primeiro governo. Ele voltou depois "
            "da queda do grupo, em 2001, e, quando o Talibã retomou o poder, em 2021, deixou o esporte continuar."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Buzkashi",
                "Buzkashi (Persian: بزکشی, romanized: buzkašī, lit. 'goat-pulling') is a traditional team sport in which horse-mounted players attempt to place a goat or calf carcass into a goal zone. [...] "
                "Buzkashi began among the nomadic Turkic tribes of the Eurasian Steppe, spreading westward from China and Mongolia towards Afghanistan between the 10th and 15th centuries [...] "
                "Games similar to buzkashi are played today by several ethnic groups such as the Hazaras, Uzbeks, Kyrgyz, Turkmens, Kazakhs, Uyghurs, Tajiks, Wakhis and Pashtuns. [...] "
                "In western China, there is not only horse-back buzkashi, but also yak buzkashi among the Tajiks of Xinjiang. [...] "
                "Buzkashi is the national sport of Afghanistan. [...] "
                "Traditionally, games could last for several days [...] "
                "During the first reign of the Taliban government in Afghanistan, buzkashi was banned as they considered the game immoral. "
                "After the Afghan Taliban was ousted in 2001, the sport resumed. "
                "When the Taliban regained power in 2021, they allowed the sport to continue. [...] "
                "The word kok-boru means gray wolf in Kyrgyz, reflecting the fact that when the game was first played by shepherds, they used a wolf carcass, rather than a goat. [...] "
                "Riders usually wear heavy clothing and head protection to protect themselves against other players' whips and boots. "
                "For example, riders in the former Soviet Union often wear salvaged Soviet tank helmets for protection. "
                "The boots usually have high heels that lock into the saddle of the horse to help the rider lean on the side of the horse while trying to pick up the goat.",
                nome="Buzkashi"),
        ],
    },
    # 10 kabaddi: o ataque feito num só fôlego
    {
        "temas_secundarios": ["asia_antiga", "limites_humanos"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "No kabaddi, o atacante invade o campo rival repetindo \"kabaddi, kabaddi\" sem parar. O canto é a prova, para os juízes, de que ele está fazendo todo o ataque num só fôlego, sem inspirar.",
        "explicacao": (
            "O kabaddi é um esporte de contato entre duas equipes de sete jogadores. Na sua vez, um jogador "
            "sozinho, o atacante, entra na metade adversária e tenta tocar nos defensores sem ser agarrado, num "
            "ataque que costuma durar no máximo 30 segundos. Durante a invasão, ele precisa entoar a palavra "
            "kabaddi, o chamado \"cant\", que confirma aos árbitros que tudo acontece numa só expiração. Se não o "
            "fizer, comete falta técnica, e o rival ganha ponto. A origem da palavra é incerta, mas o antropólogo "
            "Joseph Alter observa que ela é feita de consoantes fortemente aspiradas, que exigem movimentos claros "
            "de lábios e língua, de modo que fica evidente se o atacante respira enquanto a pronuncia. Jogos "
            "parecidos aparecem em textos antigos da Índia, mas as regras modernas foram escritas em 1921, no "
            "atual estado de Maharashtra. O kabaddi foi esporte de demonstração na Olimpíada de Berlim, em 1936, "
            "entrou no programa oficial dos Jogos Asiáticos em 1990 e é o esporte nacional de Bangladesh. Pelo "
            "subcontinente indiano, tem outros nomes, como hu-tu-tu e ha-du-du."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Kabaddi",
                "Kabaddi is a contact sport played between two teams of seven players each. "
                "During the game, a lone member of one team (\"raider\") enters the opposite half of the court and tries to tag members of the opposition team (\"defenders\") without being tackled. "
                "In a single raid, often lasting a maximum 30 seconds [...] "
                "evidence of a sport similar to modern kabaddi can be found in ancient Indian texts [...] "
                "is the national sport of Bangladesh [...] "
                "The origin of the word \"kabaddi\" is unclear. [...] "
                "According to medical anthropolgist Joseph Alter: The meaning of the term is ambiguous, but it seems to be comprised of strongly aspirated consonants that require clear lip and tongue movement so that it is clearly apparent if the raider is breathing while the word is being spoken. [...] "
                "ha-du-du in Bengal [...] hu-tu-tu in West India. [...] "
                "The first set of rules were formulated in present-day Maharashtra in 1921 [...] "
                "It was a demonstration sport at the 1936 Summer Olympics in Berlin [...] "
                "It became part of the official programme at the 1990 Asian Games held in Beijing. [...] "
                "While raiding, the raider must chant kabaddi (known as \"cant\"), confirming to referees that the raid is completed on a single breath without inhaling. [...] "
                "If the raider fails to cant or if more than one raider enter the opposition half, a technical foul is declared and the opposition is awarded a point.",
                nome="Kabaddi"),
        ],
    },
    # 11 sepak takraw: um nome de dois países e uma bola que custou uma vida
    {
        "temas_secundarios": ["linguas_mundo", "historia_esportes"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O nome sepak takraw, o \"vôlei com os pés\" do Sudeste Asiático, junta \"chutar\" em malaio e \"bola de ratã\" em tailandês, num acordo entre os dois países. E o relato malaio mais antigo do jogo acaba em morte.",
        "explicacao": (
            "O sepak takraw é disputado por equipes de dois a quatro jogadores, numa quadra parecida com a de "
            "badminton: tem rede, como o vôlei, e a bola é jogada com os pés, como no futebol. Sepak quer dizer "
            "\"chutar\" em malaio, e takraw vem do tailandês e designa a bola trançada de ratã. A escolha do nome "
            "foi, na prática, um meio-termo entre a Malásia e a Tailândia, acertado em Kuala Lumpur, em 1960, quando "
            "dirigentes da Malásia, de Singapura, da Tailândia e de Mianmar padronizaram as regras. Jogos "
            "parecidos existem em vários países da região, com nomes como sepak raga, chinlone e sipa. Na Malásia, "
            "o registro mais antigo está nos Anais Malaios e remonta ao Sultanato de Malaca, no século XV. Numa "
            "partida, uma bola atingida sem querer por Tun Besar, filho do bendahara Tun Perak, derrubou o "
            "adorno de cabeça de Raja Muhammad, filho do sultão Mansur Shah. Furioso, o príncipe matou Tun Besar "
            "a punhaladas. Parentes da vítima quiseram vingança, mas Tun Perak os conteve, dizendo que não "
            "aceitaria mais o príncipe como herdeiro. O sultão mandou o filho embora de Malaca e o instalou como "
            "governante da vizinha Pahang."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Sepak_takraw",
                "Sepak takraw (also Sepaktakraw) is a Southeast Asian team sport. "
                "It is played with a ball made of rattan or plastic between two teams of two to four players on a court resembling a badminton court. [...] "
                "a mixture of volleyball, for its use of a net, and association football, as players use their feet. "
                "The sport's modern version was introduced, developed, and standardised in 1960 when officials from Malaysia, Singapore, Thailand, and Myanmar met in Kuala Lumpur to agree on a name and standard rules for it. [...] "
                "Sepak takraw resembles native sports known as sepak raga in Malaysia and Indonesia; takraw in Thailand; chinlone in Myanmar; sipa in the Philippines [...] "
                "The word sepak is Malay (Jawi: سيڨق) for kick while the word takraw is of Thai (Thai: ตะกร้อ) origin, translated as muzzle or woven rattan ball. [...] "
                "The choice of this name for the sport was essentially a compromise between Malaysia and Thailand in Kuala Lumpur in 1960. [...] "
                "In Malaysia, the first recorded instance of Sepak Takraw, with balls made of woven strips of rattan, was in the Malacca Sultanate (present-day Malaysia) in the 15th century, according to an ancient Malay manuscript, \"Sejarah Melayu\" (Malay Annals). "
                "The Malay Annals described an incident involving Raja Muhammad, a son of Sultan Mansur Shah, who was accidentally hit with a rattan ball by Tun Besar, the son of Bendahara Tun Perak, in a Sepak Raga game. "
                "The ball hit Raja Muhammad's headgear and knocked it to the ground. "
                "Angered, Raja Muhammad immediately stabbed and killed Tun Besar, leading some of Tun Besar's kinsmen to want to kill Raja Muhammad in retaliation. "
                "However, Bendahara Tun Perak managed to restrain them from an act of treason by saying that he would no longer accept Raja Muhammad as the Sultan's heir. "
                "Sultan Mansur Shah ordered his son out of Malacca and had him installed as the ruler of neighbouring Pahang.",
                nome="Sepak takraw"),
        ],
    },
    # 12 GAA: a proibição dos "jogos estrangeiros" e o presidente punido
    {
        "temas_secundarios": ["historia_esportes"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "De 1901 a 1971, a associação dos esportes gaélicos da Irlanda proibia seus membros de jogar e até de assistir a esportes \"estrangeiros\", como o futebol. Até o presidente do país foi punido por ver um jogo.",
        "explicacao": (
            "A Associação Atlética Gaélica, a GAA, é uma organização amadora que promove os esportes tradicionais "
            "irlandeses, como o hurling e o futebol gaélico, além da língua, da música e da dança irlandesas. Em "
            "2014, tinha mais de 500 mil membros, e seu estádio principal, o Croke Park, em Dublin, tem 82.300 "
            "lugares e está entre os cinco maiores da Europa. A Regra 27, conhecida como \"a Proibição\", "
            "vigorou de 1901 a 1971 e vetava aos membros participar de jogos não gaélicos ou mesmo assistir a "
            "eles. Em 13 de novembro de 1938, poucos meses depois de tomar posse como o primeiro presidente da "
            "Irlanda, Douglas Hyde foi a um jogo de futebol entre Irlanda e Polônia, em Dublin. Como isso violava "
            "a proibição, ele perdeu o título de patrono da GAA, que tinha desde 1902. Outra regra, a 21, criada "
            "em 1897 por suspeita de infiltração de espiões da Real Polícia Irlandesa, barrava membros das forças britânicas e só caiu "
            "em 2001. E ainda hoje os campos da GAA não podem receber esportes vistos como concorrentes, que alguns "
            "chamam de \"jogos da guarnição\". O Croke Park só recebeu rúgbi e futebol a partir de 2007, enquanto "
            "o estádio de Lansdowne Road estava em obras."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Gaelic_Athletic_Association",
                "is an Irish international amateur sporting and cultural organisation, focused primarily on promoting indigenous Gaelic games and pastimes, which include the traditional Irish sports of hurling, camogie, Gaelic football, Gaelic handball, and GAA rounders. "
                "The association also promotes Irish music and dance, as well as the Irish language [...] "
                "As of 2014, the organisation had over 500,000 members [...] "
                "With a capacity of 82,300, it ranks among the top five stadiums in Europe by capacity [...] "
                "Rule 42 (Rule 5.1 in the 2009 rulebook) prohibits the use of GAA property for games with interests in conflict with the interests of the GAA referred to by some as \"garrison games\" or foreign sports. [...] "
                "On 16 April 2005 the GAA's congress voted to temporarily relax Rule 42 and allow international soccer and rugby to be played in the stadium while Lansdowne Road Football Ground was closed for redevelopment. "
                "The first soccer and rugby union games permitted in Croke Park took place in early 2007 [...] "
                "Rule 21, instituted in 1897 when it was suspected that Royal Irish Constabulary spies were trying to infiltrate the organization, prohibited members of the British forces from membership of the GAA. "
                "The rule was abolished after an overwhelming majority voted for its removal at a special congress convened in November 2001. "
                "Rule 27, sometimes referred to as The Ban, dated from 1901 and banned GAA members from taking part in or watching non Gaelic games. [...] "
                "Rule 27 was abolished in 1971.",
                nome="Gaelic Athletic Association"),
            wiki("Douglas_Hyde",
                "who served as the first president of Ireland from June 1938 to June 1945. [...] "
                "On 13 November 1938, just months after Hyde's inauguration, Hyde attended an international soccer match between Ireland and Poland at Dalymount Park in Dublin. "
                "This was seen as breaching the GAA's ban on 'foreign games' and he was subsequently removed as patron of the GAA, an honour he had held since 1902.",
                nome="Douglas Hyde"),
        ],
    },
    # 13 caber toss: o arremesso em que a distância não conta
    {
        "temas_secundarios": ["ciencia_esporte", "costumes_rituais"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "No lançamento de tronco dos jogos escoceses, a distância não conta: o tronco, de até 6 m e 70 kg, tem de dar uma cambalhota e cair reto à frente, como o ponteiro de um relógio marcando 12 horas.",
        "explicacao": (
            "O caber toss é uma prova tradicional escocesa, presente sobretudo nos Highland Games. O caber, nome "
            "que vem de uma palavra gaélica para viga de madeira, costuma ser um tronco de lariço de 5 a 6 metros "
            "e de 40 a 70 quilos. O atleta o equilibra em pé, com a ponta mais fina para baixo apoiada no ombro e "
            "no pescoço, enquanto ajudantes o seguram. Depois se agacha, desliza as mãos entrelaçadas até a base "
            "arredondada e ergue o tronco. Mantê-lo de pé com a parte mais pesada no alto não é fácil, e os menos "
            "experientes deixam o tronco tombar para o lado. Em seguida, o arremessador corre alguns passos para "
            "ganhar impulso e joga para cima a ponta que segura, para que a ponta grossa bata primeiro no chão e "
            "o tronco vire por cima de si mesmo, caindo para longe dele. A nota segue as horas do relógio: 12 é o "
            "melhor arremesso, em linha reta; 9 ou 3 é o de um tronco que passou da vertical e caiu de lado. Um "
            "tronco que fica de pé mas volta na direção do atleta vale menos que qualquer cambalhota completa. "
            "Peso e força são essenciais, mas a técnica também conta."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Caber_toss",
                "The caber toss (Scottish Gaelic: tilgeil a' chabair) is a traditional Scottish athletic event in which competitors toss a large tapered pole called a \"caber\" (), normally practiced at the Scottish Highland Games. "
                "The term \"caber\" derives from the Gaelic word cabar, which refers to a wooden beam [...] "
                "In Scotland, the caber is usually made from a larch tree, and it can be 16–20 feet (5–6 metres) tall and weigh 90–150 pounds (40–70 kilograms). [...] "
                "The primary objective is to toss the caber so that it turns end over end, falling away from the tosser. "
                "Ideally it should fall directly away from the tosser in the \"12 o'clock\" position. "
                "The tosser balances the caber upright, tapered end downwards, against his or her shoulder and neck, the caber being supported by stewards or fellow competitors while being placed into position. "
                "The tosser then crouches, sliding their interlocked hands down the caber and under the rounded base, and lifts it in their cupped hands. "
                "The tosser must balance the caber upright; this is not easy with the heavier end at the top, and less experienced tossers may be unable to stop the caber falling to one side after lifting it. "
                "The tosser then walks or runs a few paces forward to gain momentum, and flips the tapered end upwards so that the large end hits the ground first, and, if well tossed, the caber falls directly away from the tosser. "
                "Weight and strength are essential for success, but technique is also important [...] "
                "The straightest end-over-end toss scores highest. "
                "If the caber lands on its end but falls back towards the thrower, the score is lower than for any end-over-end throw [...] "
                "End-over-end tosses are scored according to the hours on a clock, with a 12:00 score being highest (falling directly away from the thrower), down to a 9 or 3 for cabers that reach a vertical, before falling to the side.",
                nome="Caber toss"),
        ],
    },
    # 14 arremesso de haggis: a "tradição" que nasceu como pegadinha
    {
        "temas_secundarios": ["historia_pratos", "costumes_rituais"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "O arremesso de haggis, o bucho de carneiro recheado, costuma ser apresentado como esporte escocês antigo. Em 2004, seu criador contou que o inventou como pegadinha, em 1977. Hoje tem até recorde mundial.",
        "explicacao": (
            "O haggis é um prato escocês feito de coração, pulmão e fígado de carneiro, com temperos, cebola, "
            "gordura, aveia e caldo, tudo cozido dentro do estômago do animal. No arremesso de haggis, vence quem "
            "o joga mais longe e com mais precisão. Os entusiastas costumam lhe atribuir uma origem antiga, mas a "
            "invenção é recente. Em 2004, Robin Dunseath, relações-públicas e ex-presidente da Associação Mundial "
            "de Arremesso de Haggis, disse que criou o esporte como brincadeira para o Encontro dos Clãs de 1977, "
            "em Edimburgo, e que depois o usou para arrecadar dinheiro para caridade nos Highland Games. Na época, "
            "o arremesso apareceu num programa da BBC, e muita gente deve ter percebido que era piada. Mesmo "
            "assim, pegou. Hoje há regras: o haggis esportivo padrão pesa 500 gramas, e um que se rompa ou "
            "estoure é desclassificado na hora, porque precisa continuar bom para comer depois de cair. Por isso, "
            "conta mais a técnica de um pouso suave que a força bruta. O recorde mundial, de 66 metros, foi "
            "registrado em 2011, e um campeonato no Canadá teve 571 arremessadores inscritos em 2014."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Haggis_hurling",
                "Haggis hurling is a Scottish sport involving the hurling of a haggis as far as possible, for distance and accuracy. [...] "
                "Although its proponents often claim an ancient origin, haggis hurling is actually a very recent invention. "
                "In 2004 Robin Dunseath, publicist for Scottish entrepreneur Tom Farmer and ex-president of the World Haggis Hurling Association, said he invented the sport as a practical joke for the 1977 Gathering of the Clans in Edinburgh, later using it to raise funds for charity at Highland games. "
                "It appeared on the BBC TV program That's Life! around that time, when many people would have realised it was basically a joke. [...] "
                "The present world record for haggis hurling was set at 217 feet (66 metres) by Lorne Coltart at the Milngavie Highland Games on 11 June 2011 [...] "
                "a split or burst haggis is immediately disqualified, as the haggis must be fit to eat after landing. "
                "The sport requires subtle technique rather than brute force, as the hurl must result in a gentle landing to keep the haggis skin intact. [...] "
                "The haggis must be of traditional construction, consisting of a tender boiled sheep's heart, lung and liver with spices, onions, suet and oatmeal and stock stuffed in a sheep's paunch, boiled for three hours. [...] "
                "The sporting haggis weighs 500 grams [...] "
                "The 2014 competition had 571 registered Hurlers.",
                nome="Haggis hurling"),
        ],
    },
    # 15 tejo: o alvo que explode
    {
        "temas_secundarios": ["americas_pre_colombianas", "costumes_rituais"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "No tejo, esporte tradicional muito popular na Colômbia, os jogadores atiram discos de metal num alvo de argila. Saber se alguém acertou é fácil: o alvo tem envelopes de pólvora que estouram com o impacto.",
        "explicacao": (
            "No tejo, também chamado turmequé, cada jogador lança um disco de metal, o próprio tejo, a cerca de "
            "18,5 metros de distância, contra uma caixa de 1 metro por 1 metro coberta de argila e inclinada a 45 "
            "graus. A marca registrada do jogo são as mechas: envelopes, geralmente triangulares, com "
            "pólvora dentro, colocados na borda do alvo, que estouram com um barulho parecido com o de um revólver "
            "pequeno quando atingidos. Estourar uma mecha vale 3 pontos; acertar o centro, 6; e fazer as duas "
            "coisas no mesmo arremesso, 9. A origem exata é incerta, mas costuma ser atribuída a povos nativos do "
            "centro da Colômbia, que teriam jogado algo parecido com um disco de ouro chamado zepquagosqua, "
            "palavra que quer dizer \"eu jogo\" em chibcha. No país, só o futebol move uma indústria maior. "
            "Antigamente, as partidas eram regadas a chicha, bebida indígena de milho fermentado; hoje, a cerveja, "
            "e as cervejarias exploram muito o jogo. Há quem tente mudar sua imagem de jogo de bar barulhento para "
            "a de esporte sério, com história rica, e já existem versões com sensores eletrônicos no lugar das mechas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Tejo_(sport)",
                "Tejo (Spanish pronunciation: [ˈtexo]) or turmequé (pronounced [tuɾmeˈke]), is a traditional throwing sport from Colombia that is distinctive for its use of small targets containing gunpowder, which explode on impact. [...] "
                "The exact origins of Tejo are uncertain. "
                "It is widely accepted that the sport has origins in native aboriginals from central Colombia, where it might have been played in a similar form. "
                "This form of tejo used a golden disc called a zepquagosqua, which means \"I play\" in the Chibcha language. [...] "
                "Tejo is a popular sport in Colombia [...] "
                "Only soccer has a larger and more supported industry in Colombia. [...] "
                "In the past, the playing of tejo was accompanied by chicha (an indigenous maize-based alcoholic beverage), whereas modern tejo players refresh themselves with beer. "
                "Tejo has been widely exploited by beer companies in Colombia. "
                "Tejo aficionados are trying to change the image of the sport in popular culture from a rowdy bar game to a serious sport with a rich history. [...] "
                "The game consists of throwing a metal puck/disc (called a tejo) across a field at a 1-by-1-metre (3.3 by 3.3 ft) board at a distance of approximately 18.5 metres (20.2 yd). "
                "The board is covered with clay and set at a 45-degree angle. [...] "
                "A chief characteristic of the sport is its use of small, exploding targets that contain gunpowder, commonly known as mechas. "
                "These usually triangle-shaped envelopes with explosive material inside are set on the edges of the pipe. "
                "When struck by the tejo, they explode loudly, creating a sound similar to the one created by a small revolver. "
                "Modern adaptations of tejo also exist, with electronic sensors instead of the traditional mechas being used to detect a hit. [...] "
                "Hit: grants 3 points to every player that explodes a mecha "
                "Bulls-eye: grants 6 points to the player whose tejo has impacted inside the target "
                "Strike: grants 9 points to the player that scores a hit and a bulls-eye in the same throw",
                nome="Tejo (sport)"),
        ],
    },
    # 16 sumô: mulheres barradas no ringue japonês, protagonistas no Brasil
    {
        "temas_secundarios": ["costumes_rituais", "religioes"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "No Japão, mulheres não podem pisar no ringue do sumô profissional: em 2018, um árbitro mandou sair as que socorriam um prefeito desmaiado. Já o Brasil, com torneios desde 1914, é um centro do sumô feminino.",
        "explicacao": (
            "No sumô profissional japonês, mulheres não competem nem podem entrar no dohyō, o ringue. A "
            "proibição vem de crenças xintoístas e budistas que viam as mulheres como \"impuras\" por causa do "
            "sangue menstrual, embora tenha existido em partes do Japão uma forma de sumô feminino antes do sumô "
            "profissional. Em 2018, numa exibição em Maizuru, o prefeito da cidade desmaiou com uma "
            "hemorragia subaracnoide enquanto discursava. Mulheres que tentavam lhe prestar primeiros "
            "socorros foram mandadas sair por um árbitro. O presidente da Associação de Sumô pediu desculpas e "
            "chamou a reação de inadequada numa situação que podia ser fatal, e a entidade esclareceu que mulheres "
            "podem entrar no ringue em emergências. Dias depois, a prefeita de Takarazuka teve de discursar ao "
            "lado do ringue, e não dentro dele. No Brasil, o sumô chegou com os imigrantes japoneses: o primeiro "
            "torneio foi em 1914, e São Paulo tem o único centro de treino construído especialmente para o sumô "
            "fora do Japão. A partir dos anos 1990, as entidades brasileiras atraíram praticantes sem ascendência "
            "japonesa, que em meados dos anos 2000 eram estimados em 70% do total. O Brasil também é um centro do "
            "sumô feminino."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Sumo",
                "Women are not allowed to compete in professional sumo. "
                "They are also not allowed to enter the wrestling ring (dohyō), a tradition stemming from Shinto and Buddhist beliefs that women are \"impure\" because of menstrual blood. "
                "A form of female sumo (女相撲, onnazumo) existed in some parts of Japan before professional sumo was established. [...] "
                "Brazil is another center of amateur sumo, introduced by Japanese immigrants who arrived during the first half of the twentieth century. "
                "The first Brazilian sumo tournament was held in 1914. "
                "Sumo took root in immigrant centers in southern Brazil, especially São Paulo, which is now home to the only purpose-built sumo training facility outside Japan. "
                "Beginning in the 1990s, Brazilian sumo organizations made an effort to interest Brazilians without Japanese ancestry in the sport, and by the mid-2000s an estimated 70% of participants came from outside the Japanese-Brazilian community. "
                "Brazil is also a center for women's sumo.",
                nome="Sumo"),
            wiki("2018_in_sumo",
                "The following are the events in professional sumo during 2018. [...] "
                "4: Maizuru, Kyoto Prefecture. "
                "Chairman Hakkaku issues an apology after a referee ordered women off the dohyo when they were trying to administer first aid to the mayor of Maizuru, who had just collapsed with a subarachnoid hemorrhage while giving a speech. "
                "Hakkaku says, \"In a situation that could have been life-threatening it was an inappropriate response.\" [...] "
                "6: Takarazuka, Hyogo Prefecture. "
                "The female mayor of Takarazuka, who had to stand next to the dohyo instead of entering it at the exhibition [...] "
                "28: At an extraordinary meeting of its board, the Sumo Association clarifies that women can enter the dohyo in an emergency situation",
                nome="2018 in sumo"),
        ],
    },
]
