LOTE = "2026-11-19-geometria_topologia-01"
AREA = "matematica"
TEMA = "geometria_topologia"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Perelman recusa a Medalha Fields e o US$ 1 milhão
    {
        "temas_secundarios": ["historia_matematica"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "A conjectura de Poincaré, sobre a forma de espaços de três dimensões, resistiu por um século. Quem a provou, Grigori Perelman, recusou a Medalha Fields e também um prêmio de US$ 1 milhão.",
        "explicacao": (
            "Em 1904, Henri Poincaré propôs que um espaço finito de três dimensões em que todo laço pode ser "
            "apertado continuamente até virar um ponto é, necessariamente, uma esfera tridimensional. A superfície "
            "de uma bola tem essa propriedade; a de uma rosquinha não, porque nela há laços que não se desfazem. As "
            "tentativas de resolver a questão impulsionaram boa parte da topologia geométrica do século XX. Em "
            "novembro de 2002 e março de 2003, o russo Grigori Perelman postou no repositório arXiv textos que "
            "completavam o programa de Richard Hamilton, baseado numa ferramenta chamada fluxo de Ricci. Outros "
            "matemáticos passaram anos preenchendo e explicando os detalhes. Em 2006, Perelman recusou a Medalha "
            "Fields, dizendo não ter interesse em dinheiro nem fama e não querer ser exibido como um animal no "
            "zoológico; foi a única pessoa a recusar esse prêmio. Em 2010, o Instituto Clay lhe concedeu o Prêmio do "
            "Milênio, de US$ 1 milhão, e ele recusou de novo: achou a decisão injusta porque sua contribuição não "
            "teria sido maior que a de Hamilton. É o único dos Problemas do Milênio com solução verificada. Perelman "
            "declarou ter deixado a matemática profissional, decepcionado com os padrões éticos da área, e vive "
            "recluso em São Petersburgo."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Poincaré_conjecture",
                "The Clay Mathematics Institute, having included the Poincaré conjecture in their well-known Millennium Prize Problem list, offered Perelman their prize of US$1 million in 2010 for the conjecture's resolution. "
                "He declined the award, saying that Hamilton's contribution had been equal to his own. "
                "As of 2026, the Poincaré conjecture is the only Millennium Prize Problem with a verified solution. [...] "
                "Originally conjectured by Henri Poincaré in 1904, the theorem concerns spaces that locally look like ordinary three-dimensional Euclidean space but which are finite in extent. "
                "Poincaré hypothesized that if such a space has the additional property that each loop in the space can be continuously tightened to a point, then it is necessarily a three-dimensional sphere. "
                "Attempts to resolve the conjecture drove much progress in the field of geometric topology during the 20th century. "
                "The eventual proof built upon Richard S. Hamilton's program of using the Ricci flow to solve the problem. "
                "By developing a number of new techniques and results in the theory of Ricci flow, Grigori Perelman modified and completed Hamilton's program. [...] "
                "The surface of a ball has trivial fundamental group, meaning that any loop drawn on the surface can be continuously deformed to a single point. "
                "By contrast, the surface of a torus has nontrivial fundamental group, as there are loops on the surface which cannot be so",
                nome="Poincaré conjecture"),
            wiki("Grigori_Perelman",
                "In 2005, Perelman resigned from his research post in Steklov Institute of Mathematics and in 2006 stated that he had quit professional mathematics, owing to feeling disappointed over the ethical standards in the field. "
                "He lives in seclusion in Saint Petersburg [...] "
                "the former of which had been a famous open problem in mathematics for the past century. "
                "The full details of Perelman's work were filled in and explained by various authors over the following several years. "
                "In August 2006, Perelman was offered the Fields Medal for \"his contributions to geometry and his revolutionary insights into the analytical and geometric structure of the Ricci flow\", but he declined the award, stating: \"I'm not interested in money or fame; I don't want to be on display like an animal in a zoo.\" [...] "
                "On 1 July 2010, he rejected the prize of one million dollars, saying that he considered the decision of the board of the Clay Institute to be unfair, in that his contribution to solving the Poincaré conjecture was no greater than that of Richard S. Hamilton [...] "
                "In November 2002 and March 2003, Perelman posted two preprints to arXiv [...] "
                "Perelman declined to accept the medal, which made him the only person to have ever declined the prize.",
                nome="Grigori Perelman"),
        ],
    },
    # 2 virar uma esfera do avesso
    {
        "temas_secundarios": ["paradoxos_logica"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Dá para virar uma esfera do avesso sem rasgá-la nem criar vincos, desde que a superfície possa atravessar a si mesma. Quando Stephen Smale provou isso, o orientador dele disse que estava obviamente errado.",
        "explicacao": (
            "Imagine uma bola de um material ideal, que pode se esticar e passar através de si mesma, mas não pode "
            "ser cortada nem formar quinas. Ela pode ser revirada, com o lado de dentro indo para fora, num "
            "movimento suave e contínuo? Em 1958, Stephen Smale apresentou uma prova de que sim. O resultado "
            "surpreende leigos e também quem conhece a teoria, e costuma ser chamado de paradoxo verídico: algo "
            "verdadeiro que, à primeira vista, parece falso. O orientador de Smale, Raoul Bott, disse de início que "
            "aquilo estava obviamente errado. Bott raciocinou que uma certa grandeza, o grau da aplicação de Gauss, "
            "teria de se conservar no processo, e é essa grandeza que impede um círculo de ser revirado dentro do "
            "plano. Mas, para a esfera no espaço, ela vale o mesmo, 1, na versão normal e na revirada, e não há "
            "obstáculo. A prova de Smale era indireta: garantia que o movimento existe, sem mostrar como fazê-lo. O "
            "primeiro exemplo concreto saiu do esforço de vários matemáticos, entre eles Arnold Shapiro e Bernard "
            "Morin, que era cego. Depois, animações de computador, como o filme \"Outside In\", tornaram o processo "
            "mais fácil de visualizar."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Sphere_eversion",
            "In differential topology, sphere eversion is a theoretical process of turning a sphere inside out in a three-dimensional space (the word eversion means \"turning inside out\"). "
            "It is possible to smoothly and continuously turn a sphere inside out in this way (allowing self-intersections of the sphere's surface) without cutting or tearing it or creating any crease. "
            "This is surprising, both to non-mathematicians and to those who understand regular homotopy, and can be regarded as a veridical paradox; that is something that, while being true, on first glance seems false. [...] "
            "An existence proof for crease-free sphere eversion was first created by Stephen Smale (1958). [...] "
            "The first example was exhibited through the efforts of several mathematicians, including Arnold S. Shapiro and Bernard Morin, who was blind. "
            "On the other hand, it is much easier to prove that such a \"turning\" exists, and that is what Smale did. "
            "Smale's graduate adviser Raoul Bott at first told Smale that the result was obviously wrong [...] "
            "His reasoning was that  the degree of the Gauss map must be preserved in such \"turning\"—in particular it follows that there is no such turning of S1 in R2. "
            "But the degrees of the Gauss map for the embeddings f and −f in R3 are both equal to 1, and do not have opposite sign as one might incorrectly guess. [...] "
            "so there is no obstacle. [...] "
            "Smale's original proof was indirect [...] "
            "This is illustrated in the computer-graphics animation Outside In",
            nome="Sphere eversion")],
    },
    # 3 bola cabeluda e o vento
    {
        "temas_secundarios": ["clima_tempo"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Um teorema garante que é impossível pentear uma bola cabeluda sem deixar um redemoinho. Por causa dele, em cada camada da atmosfera há sempre um ponto da Terra onde o vento não sopra na horizontal.",
        "explicacao": (
            "O teorema da bola cabeluda diz que, se você atribuir a cada ponto de uma esfera uma seta tangente à "
            "superfície, variando de forma contínua, haverá pelo menos um ponto em que a seta se anula. Em "
            "linguagem informal: quem tentar pentear todos os fios de um coco, deitando-os sobre a casca, vai sempre "
            "deixar um redemoinho. Henri Poincaré o provou em 1885 para a esfera comum, e L. E. J. Brouwer o "
            "estendeu em 1912 para dimensões pares maiores. Por trás dele está a característica de Euler, um número "
            "que descreve a forma da superfície: na esfera, ele vale 2, e isso força a existência de um zero. Numa "
            "rosquinha, ele vale 0, e por isso dá para \"pentear uma rosquinha cabeluda\" sem redemoinho nenhum. Se o "
            "vento na superfície da Terra for tratado como uma seta em cada ponto, o teorema sugere que sempre há um "
            "ciclone em algum lugar. Essa versão é idealizada demais, porque o ar também se move na vertical. O que "
            "vale de fato é mais modesto: em cada \"casca\" da atmosfera ao redor do planeta, existe um ponto onde o "
            "vento não se move na horizontal. O teorema também aparece em modelagem por computador, inclusive no "
            "desenvolvimento de videogames."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Hairy_ball_theorem",
            "For the ordinary sphere, or 2‑sphere, if f is a continuous function that assigns a vector in ℝ3 to every point p on a sphere such that f(p) is always tangent to the sphere at p, then there is at least one pole, a point where the field vanishes [...] "
            "The theorem was first proven by Henri Poincaré for the 2-sphere in 1885, and extended to higher even dimensions in 1912 by L. E. J. Brouwer. "
            "The theorem has been expressed colloquially as \"you can't comb a hairy ball flat without creating a cowlick\" or \"you can't comb the hair on a coconut\". [...] "
            "of the 2-sphere is two. Therefore, there must be at least one zero. [...] "
            "In the case of the torus, the Euler characteristic is 0; and it is possible to \"comb a hairy doughnut flat\". [...] "
            "If one idealizes the wind in the Earth's atmosphere as a tangent-vector field, then the hairy ball theorem implies that given any wind at all on the surface of the Earth, there must at all times be a cyclone somewhere. "
            "Note, however, that wind can move vertically in the atmosphere, so the idealized case is not meteorologically sound. "
            "(What is true is that for every \"shell\" of atmosphere around the Earth, there must be a point on the shell where the wind is not moving horizontally.) "
            "The theorem also has implications in computer modeling (including video game design)",
            nome="Hairy ball theorem")],
    },
    # 4 antípodas com a mesma temperatura e pressão
    {
        "temas_secundarios": ["clima_tempo"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Agora mesmo, há dois pontos exatamente opostos na Terra com a mesma temperatura e a mesma pressão do ar. Não é coincidência: um teorema de topologia garante isso, desde que as duas variem sem saltos.",
        "explicacao": (
            "O teorema de Borsuk-Ulam diz que toda função contínua que leva os pontos de uma esfera a um plano "
            "acaba levando algum par de pontos antípodas ao mesmo ponto do plano. Antípodas são pontos em direções "
            "exatamente opostas a partir do centro, como os polos Norte e Sul. Na Terra, temperatura e pressão "
            "atmosférica formam, juntas, um par de números para cada lugar, ou seja, uma função da esfera no plano. "
            "O teorema garante, então, que em qualquer momento existe um par de pontos opostos com os dois valores "
            "iguais ao mesmo tempo. A versão mais simples vale para qualquer círculo: ao longo do equador, sempre há "
            "dois pontos opostos com a mesma temperatura. Tudo depende de as grandezas variarem de forma contínua "
            "no espaço, o que nem sempre acontece na realidade. O teorema leva o nome de dois matemáticos: a "
            "primeira prova foi dada por Karol Borsuk em 1933, e a formulação do problema foi atribuída a Stanisław "
            "Ulam. Ele vale em qualquer número de dimensões, e desde então muitas outras provas foram encontradas."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Borsuk–Ulam_theorem",
            "In topology, the Borsuk–Ulam theorem states that every continuous map from the sphere to the plane maps some pair of antipodal points to the same point. "
            "The theorem is named after mathematicians Karol Borsuk and Stanisław Ulam. [...] "
            "true in higher dimensions [...] "
            "Two points on a sphere are called antipodal if they lie in exactly opposite directions from the center—like the North and South Poles. [...] "
            "The case n=1 can be illustrated by saying that there always exist a pair of opposite points on the Earth's equator with the same temperature. "
            "The same is true for any circle. This assumes the temperature varies continuously in space, which is, however, not always the case. "
            "The case n=2 is often illustrated by saying that at any moment, there is always a pair of antipodal points on the Earth's surface with equal temperatures and equal barometric pressures, assuming that both parameters vary continuously in space. [...] "
            "The first proof was given by Karol Borsuk (1933), where the formulation of the problem was attributed to Stanisław Ulam.  "
            "Since then, many alternative proofs have been found by various authors",
            nome="Borsuk–Ulam theorem")],
    },
    # 5 Marjorie Rice e os pentágonos na mesa da cozinha
    {
        "temas_secundarios": ["personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Uma mãe de cinco filhos, com só o ensino médio, descobriu na mesa da cozinha quatro tipos novos de pentágono capazes de cobrir um plano sem deixar buracos. Ela escondia os desenhos quando a família chegava.",
        "explicacao": (
            "Marjorie Rice (1923–2017), de San Diego, era leitora fiel da coluna \"Mathematical Games\", de Martin "
            "Gardner, na revista Scientific American. Em julho de 1975, a coluna tratou dos polígonos convexos que "
            "se encaixam perfeitamente, sem sobreposição nem frestas, cobrindo um plano inteiro. Gardner repetia a "
            "afirmação de que a lista dos pentágonos com essa propriedade estava completa. Em menos de um mês, um "
            "leitor mandou a ele um tipo novo. Inspirada, Rice passou a procurar outros nas horas vagas, com "
            "desenhos feitos na mesa da cozinha quando não havia ninguém por perto e escondidos quando o marido e "
            "os filhos chegavam. Criou até uma notação própria. Gardner encaminhou o material a Doris "
            "Schattschneider, especialista em ladrilhamentos, que de início estranhou aquela notação, parecida com "
            "\"hieróglifos\", mas acabou confirmando os resultados. Entre 1976 e 1977, Rice encontrou quatro tipos "
            "novos. Hoje se conhecem 15 tipos de pentágono convexo que ladrilham o plano usando um só formato; o "
            "mais recente foi achado em 2015, com ajuda de um algoritmo de computador. Em 2017, Michaël Rao anunciou "
            "uma prova de que não existem outros, ainda sujeita à revisão por pares, segundo a Wikipedia."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Marjorie_Rice",
                "Marjorie Ruth Rice (née Jeuck, 1923–2017) was an American amateur mathematician most famous for her discoveries of pentagonal tilings. [...] "
                "Marjorie Rice was a San Diego mother of five, who had become an ardent follower of Martin Gardner's long-running column, \"Mathematical Games\", which appeared monthly, 1957–1986, in the pages of Scientific American magazine. [...] "
                "In 1975, Rice read Gardner's July column, \"On Tessellating the Plane with Convex Polygon Tiles\", that discussed what kinds of convex polygons can fit together perfectly without any overlaps or gaps to fill the plane. [...] "
                "Gardner was repeating Kershner's claim that the list of convex pentagon tilers was complete.  "
                "But within a month, Gardner received an example, by one of his readers, Richard James III, of a new convex pentagon tiler [...] "
                "Despite having only a high-school education, but a keen interest in art, she began devoting her free time to discovering new pentagonal tilings [...] "
                "\"by drawing diagrams on the kitchen table when no one was around and hiding them when her husband and children came home, or when friends stopped by\". "
                "She even developed her own system of notation [...] "
                "He, in turn, sent Rice's work to Doris Schattschneider, an expert in tiling patterns, who was skeptical at first, saying that Rice's idiosyncratic notation system seemed odd, like \"hieroglyphics\". "
                "But with careful examination, she was able to validate Rice's results.",
                nome="Marjorie Rice"),
            wiki("Pentagonal_tiling",
                "Fifteen types of convex pentagons are known to tile the plane monohedrally (i.e., with one type of tile). "
                "The most recent one was discovered in 2015. This list has been shown to be complete by Rao (2017), result subject to peer review. [...] "
                "Marjorie Rice, an amateur mathematician, discovered four new types of tessellating pentagons in 1976 and 1977. [...] "
                "discovered a 15th monohedral tiling convex pentagon in 2015 using a computer algorithm.",
                nome="Pentagonal tiling"),
        ],
    },
    # 6 o "chapéu": a peça única que nunca se repete
    {
        "temas_secundarios": ["padroes_fractais", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 2022, um matemático amador achou o \"chapéu\": uma única peça que cobre o plano inteiro sem frestas, mas só num padrão que nunca se repete. Foi a solução da versão mais exigente do \"problema do einstein\".",
        "explicacao": (
            "Os ladrilhamentos de Penrose, estudados nos anos 1970, mostraram que dá para cobrir o plano sem que o "
            "desenho jamais se repita periodicamente. Mas precisavam de mais de um formato: a versão original tinha "
            "quatro, depois reduzidos a dois. Faltava saber se uma única peça bastaria. A pergunta ficou conhecida "
            "como problema do einstein, trocadilho com \"ein Stein\", \"uma pedra\" em alemão, e com o físico. "
            "Variantes do problema foram resolvidas a partir dos anos 1990, com concessões: uma solução permitia "
            "que as peças se sobrepusessem; outra exigia regras de encaixe ligadas a desenhos sobre as peças, ou "
            "então uma peça desconexa. Em novembro de 2022, o amador David Smith descobriu uma peça em forma de "
            "chapéu, feita de oito pipas iguais coladas lado a lado, que parecia ladrilhar o plano apenas sem "
            "repetição. Ele chamou o matemático Craig S. Kaplan e, depois, Joseph Samuel Myers e Chaim "
            "Goodman-Strauss. Em março de 2023, o grupo divulgou a prova. Havia um detalhe: o chapéu precisa ser "
            "usado junto com sua imagem no espelho. Em maio, os quatro apresentaram o \"espectro\", forma aparentada "
            "que dispensa as cópias espelhadas. A prova do chapéu saiu numa revista científica em julho de 2024."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Einstein_problem",
                "In plane discrete geometry, the einstein problem asks about the existence of a single prototile that by itself forms an aperiodic set of prototiles; that is, a shape that can tessellate space but only in a nonperiodic way. "
                "Such a shape is called an einstein, a word play on ein Stein, German for \"one stone\", and physicist Albert Einstein. "
                "Several variants of the problem, depending on the particular definitions of nonperiodicity and the specifications of what sets may qualify as tiles and what types of matching rules are permitted, were solved beginning in the 1990s. "
                "The strictest version of the problem was solved in 2023, after an initial discovery in 2022. [...] "
                "In 1996, Petra Gummelt constructed a decorated decagonal tile and showed that when two kinds of overlaps between pairs of tiles are allowed, the tiles can cover the plane, but only non-periodically. [...] "
                "This construction requires matching rules, rules that restrict the relative orientation of two tiles and that make reference to decorations drawn on the tiles [...] "
                "Alternatively, an undecorated tile with no matching rules may be constructed, but the tile is not connected. [...] "
                "In November 2022, the amateur mathematician David Smith discovered a \"hat\"-shaped tile formed from eight copies of a 60°–90°–120°–90° kite (deltoidal trihexagonals), glued edge-to-edge, which seemed to only tile the plane aperiodically. "
                "Smith recruited mathematician Craig S. Kaplan, and subsequently Joseph Samuel Myers and Chaim Goodman-Strauss, and in March 2023 they posted a preprint proving that the \"hat\", when considered with its mirror image, forms an aperiodic prototile set. [...] "
                "This result was formally published in the journal Combinatorial Theory in July 2024. "
                "In May 2023 they (Smith, Myers, Kaplan, and Goodman-Strauss) posted a new preprint about a family of shapes related to the \"hat\", called \"spectres\", each of which can tile the plane using only rotations and translations.",
                nome="Einstein problem"),
            wiki("Penrose_tiling",
                "A Penrose tiling is an example of an aperiodic tiling. [...] "
                "Penrose tilings are named after mathematician and physicist Roger Penrose, who investigated them in the 1970s. "
                "There are several variants of Penrose tilings with different tile shapes. "
                "The original form of Penrose tiling used tiles of four different shapes, but this was later reduced to only two shapes",
                nome="Penrose tiling"),
        ],
    },
    # 7 girih: mosaicos islâmicos e os ladrilhamentos de Penrose
    {
        "temas_secundarios": ["arquitetura", "mundo_islamico_medieval"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "Segundo um estudo de 2007, mosaicos islâmicos de um santuário de 1453, no Irã, têm propriedades dos padrões que nunca se repetem descritos pelo matemático Roger Penrose só nos anos 1970.",
        "explicacao": (
            "Artesãos do mundo islâmico decoravam edifícios com o girih, desenhos de linhas entrelaçadas; a palavra "
            "persa quer dizer \"nó\". Desde cerca do ano 1200, eles usavam um conjunto de cinco peças, todas com "
            "lados do mesmo comprimento e ângulos múltiplos de 36 graus, entre elas um decágono e um pentágono. Na "
            "parede pronta, em geral só aparecem as linhas, não as bordas das peças. Os arranjos ficaram muito mais "
            "sofisticados a partir do santuário Darb-i Imam, em Isfahan, construído em 1453. Em 2007, os físicos "
            "Peter Lu e Paul Steinhardt sugeriram que esses desenhos têm propriedades compatíveis com os "
            "ladrilhamentos de Penrose, que cobrem o plano sem formar um padrão periódico e podem ter simetria de "
            "rotação de ordem cinco. A proposta se apoiou em prédios preservados e em rolos persas do século XV. "
            "Não se sabe quanto da matemática os arquitetos dominavam: rolos de modelos, como o de Topkapi, com 29,5 "
            "metros, podem ter sido consultados, e as próprias peças permitiam compor desenhos muito complexos sem "
            "entender os princípios por trás deles. O tema ganhou peso em 2011, quando o Nobel de Química premiou a "
            "descoberta dos quasicristais, e os ladrilhamentos de Penrose foram lembrados por ajudarem a entendê-la."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Girih_tiles",
                "Girih tiles are a set of five tiles that were used in the creation of Islamic geometric patterns using strapwork (girih) for decoration of buildings in Islamic architecture. "
                "They have been used since about the year 1200 and their arrangements found significant improvement starting with the Darb-i Imam shrine in Isfahan in Iran built in 1453. [...] "
                "All sides of these figures have the same length, and all their angles are multiples of 36° [...] "
                "Specifically, the decagon has tenfold rotational symmetry (rotation by 36°); and the pentagon has fivefold rotational symmetry [...] "
                "The tiles are used to form girih patterns, from the Persian word گره, meaning \"knot\".  "
                "In most cases, only the girih (and other minor decorations like flowers) are visible rather than the boundaries of the tiles themselves. [...] "
                "In 2007, the physicists Peter J. Lu and Paul J. Steinhardt suggested that girih tilings possess properties consistent with self-similar fractal quasicrystalline tilings such as Penrose tilings. "
                "This finding was supported both by analysis of patterns on surviving structures, and by examination of 15th-century Persian scrolls. "
                "There is no indication of how much more the architects may have known about the mathematics involved. [...] "
                "Templates found on scrolls such as the 97-foot (29.5 metres) long Topkapi Scroll may have been consulted. [...] "
                "In this way, craftsmen could make highly complex designs without resorting to mathematics and without necessarily understanding their underlying principles.",
                nome="Girih tiles"),
            wiki("Penrose_tiling",
                "A Penrose tiling is an example of an aperiodic tiling. [...] "
                "However, despite their lack of translational symmetry, Penrose tilings may have both reflection symmetry and fivefold rotational symmetry. "
                "Penrose tilings are named after mathematician and physicist Roger Penrose, who investigated them in the 1970s. [...] "
                "Peter J. Lu and Paul Steinhardt have presented evidence that a Penrose tiling underlies examples of medieval Islamic geometric patterns, such as the girih (strapwork) tilings at the Darb-e Imam shrine in Isfahan. [...] "
                "The 2011 Nobel Prize in Chemistry  was awarded to Dan Shechtman for \"The discovery of quasicrystals.\" "
                "Penrose tiling was mentioned for having \"'helped pave the way for the understanding of the discovery o",
                nome="Penrose tiling"),
        ],
    },
    # 8 Bolyai: "deixe as paralelas em paz"
    {
        "temas_secundarios": ["historia_matematica", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "\"Deixe a ciência das paralelas em paz\", implorou um matemático ao filho. O filho insistiu e criou uma geometria nova. Gauss leu e disse que elogiá-la seria elogiar a si mesmo: já tinha chegado lá, sem publicar.",
        "explicacao": (
            "Por pelo menos mil anos, geômetras acharam que o quinto postulado de Euclides, o das paralelas, poderia "
            "ser provado a partir dos outros quatro. Numa forma equivalente, ele diz que, por um ponto fora de uma "
            "reta, passa exatamente uma reta que não a cruza. O húngaro Farkas Bolyai gastou anos no assunto e, em "
            "1820, escreveu ao filho János pedindo que desistisse: dizia ter atravessado aquela \"noite sem fundo\", "
            "que tinha apagado toda a luz e a alegria da sua vida. János insistiu e concluiu que o postulado é "
            "independente dos demais axiomas, e que negá-lo permite construir geometrias diferentes e consistentes. "
            "Na hiperbólica, passam infinitas retas pelo ponto sem cruzar a reta dada, e os ângulos de um triângulo "
            "somam menos de 180 graus. Em 1823, ele escreveu ao pai que, \"do nada\", tinha criado \"um estranho "
            "universo novo\". O trabalho saiu em 1832, como apêndice a um livro do pai. Gauss chamou o jovem de "
            "gênio de primeira ordem, mas escreveu a Farkas que elogiá-lo seria elogiar a si mesmo, pois o conteúdo "
            "coincidia com o que vinha pensando havia 30 ou 35 anos. Gauss de fato já tinha revelado a descoberta "
            "numa carta de 1827 e, em 1829, escreveu que temia a reação se publicasse. János passou a suspeitar que "
            "o pai havia contado tudo a Gauss, e os dois se afastaram."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("János_Bolyai",
                "the son of Zsuzsanna Benkő and the well-known mathematician Farkas Bolyai. [...] "
                "Bolyai became so obsessed with Euclid's parallel postulate that his father, who had pursued the same subject for many years, wrote to him in 1820: "
                "\"You must not attempt this approach to parallels. I know this way to the very end. I have traversed this bottomless night, which extinguished all light and joy in my life. I entreat you, leave the science of parallels alone...Learn from my example.\" "
                "János, however, persisted in his quest and eventually came to the conclusion that the postulate is independent of the other axioms of geometry and that different consistent geometries can be constructed on its negation. "
                "In 1823, he wrote to his father: \"I have discovered such wonderful things that I was amazed...out of nothing I have created a strange new universe.\" [...] "
                "Bolyai's work was published in 1832 as an appendix to a mathematics textbook by his father. "
                "Carl Friedrich Gauss, on reading the Appendix, wrote in a letter, \"I regard this young geometer Bolyai as a genius of the first order.\" "
                "To his old friend Farkas Bolyai, however, Gauss wrote: \"To praise it would amount to praising myself. For the entire content of the work...coincides almost exactly with my own meditations which have occupied my mind for the past thirty or thirty-five years.\" "
                "Indeed, Gauss had disclosed his discovery of a consistent non-Euclidean geometry in a letter in 1827, and in 1829 wrote that he feared backlash if he published about it. "
                "János suspected that Gauss had been secretly informed about his discoveries by his father, causing a rift between him and his father.",
                nome="János Bolyai"),
            wiki("Non-Euclidean_geometry",
                "Euclid's fifth postulate, the parallel postulate, is equivalent to Playfair's postulate, which states that, within a two-dimensional plane, for any given line l and a point p, which is not on l, there is exactly one line through p that does not intersect l. "
                "In hyperbolic geometry, by contrast, there are infinitely many lines through p not intersecting l [...] "
                "For at least a thousand years, geometers were troubled by the disparate complexity of the fifth postulate, and believed it could be proved as a theorem from the other four. [...] "
                "The sum of the measures of the angles of any triangle is less than 180° if the geometry is hyperbolic",
                nome="Non-Euclidean geometry"),
        ],
    },
    # 9 a bola que encolhe nas dimensões altas
    {
        "temas_secundarios": ["ia_robotica"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Uma bola de raio 1 tem o maior volume possível na 5ª dimensão. Daí em diante ela encolhe, e o volume tende a zero conforme as dimensões aumentam. O cubo que a envolve, ao contrário, só cresce.",
        "explicacao": (
            "A noção de volume pode ser estendida a qualquer número de dimensões, e existe uma fórmula para o "
            "volume de uma bola de raio R em n dimensões. Para raio 1, o volume cresce da dimensão 0 até a 5, "
            "chega ao máximo na 5 e depois diminui; com n indo ao infinito, ele tende a zero. Já o cubo que envolve "
            "essa bola, com lado igual ao dobro do raio, tem volume que cresce sem parar, e por isso a fração do cubo "
            "ocupada pela bola fica insignificante. Ao mesmo tempo, a distância do centro às quinas do cubo cresce "
            "sem limite. A consequência é estranha: se pontos forem sorteados ao acaso num cubo de muitas "
            "dimensões, quase todos ficam longe do centro, mas também longe das quinas, e o volume se concentra "
            "perto da superfície de uma esfera de raio intermediário. Isso tem efeito prático. Faz parte da chamada "
            "maldição da dimensionalidade, expressão criada por Richard E. Bellman, que aparece em áreas como "
            "aprendizado de máquina, mineração de dados e bancos de dados: quando o número de dimensões aumenta, o "
            "volume do espaço cresce tão depressa que os dados disponíveis ficam esparsos, e a quantidade de dados "
            "necessária para um resultado confiável costuma crescer exponencialmente."
        ),
        "nivel": 3, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Volume_of_an_n-ball",
                "In particular, for any fixed value of R the volume tends to a limiting value of 0 as n goes to infinity. "
                "Which value of n maximizes Vn(R) depends upon the value of R; for example, the volume Vn(1) is increasing for 0 ≤ n ≤ 5, achieves its maximum when n = 5, and is decreasing for n ≥ 5.",
                nome="Volume of an n-ball"),
            wiki("Curse_of_dimensionality",
                "The expression was coined by Richard E. Bellman when considering problems in dynamic programming. [...] "
                "Dimensionally cursed phenomena occur in domains such as numerical analysis, sampling, combinatorics, machine learning, data mining and databases. "
                "The common theme of these problems is that when the dimensionality increases, the volume of the space increases so fast that the available data becomes sparse. "
                "In order to obtain a reliable result, the amount of data needed often grows exponentially with the dimensionality. [...] "
                "while the volume of the cube is (2r)d. "
                "As the dimension d of the space increases, the hypersphere becomes an insignificant volume relative to that of the hypercube. [...] "
                "Furthermore, the distance between the center and the corners is rd, which increases without bound for fixed r. [...] "
                "Thus, when uniformly generating points in high dimensions, both the \"middle\" of the hypercube, and the corners are empty, and all the volume is concentrated near the surface of a sphere of \"intermediate\" radius",
                nome="Curse of dimensionality"),
        ],
    },
    # 10 Viazovska e as esferas em 8 e 24 dimensões
    {
        "temas_secundarios": ["algoritmos"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "Qual o jeito mais compacto de arrumar esferas iguais? Em 2016, Maryna Viazovska provou a resposta em 8 dimensões e, logo depois, com colegas, em 24. Em 4 dimensões, ainda não se sabe.",
        "explicacao": (
            "O problema do empacotamento de esferas pergunta qual arranjo de esferas iguais ocupa a maior fração do "
            "espaço, e ele pode ser posto em qualquer número de dimensões. Até então, só estava resolvido para três "
            "dimensões ou menos, e a prova do caso tridimensional, a conjectura de Kepler, tinha exigido longos "
            "cálculos de computador. Em 2016, a ucraniana Maryna Viazovska provou que o arranjo chamado reticulado E8 "
            "é o mais denso possível no espaço de oito dimensões, mesmo comparado a arranjos irregulares. Logo "
            "depois, ela e colaboradores provaram o mesmo para o reticulado de Leech, em 24 dimensões. A prova dela "
            "foi descrita como \"espantosamente simples\". Em 2022, Viazovska recebeu a Medalha Fields, a segunda "
            "mulher a ganhá-la, depois de Maryam Mirzakhani. Hoje, entre os arranjos regulares, os reticulados, o "
            "melhor é conhecido nas dimensões 1 a 8 e 24; considerando todos os arranjos, só nas dimensões 1 a 3, 8 "
            "e 24. É possível que, em algumas dimensões, o arranjo mais denso seja irregular. O assunto não é só "
            "abstrato: empacotar esferas tem relação direta com o projeto de códigos corretores de erros, e o "
            "código de Golay, por exemplo, é aparentado ao reticulado de Leech."
        ),
        "nivel": 3, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Maryna_Viazovska",
                "She was awarded the Fields Medal in July 2022, making her the second woman (after Maryam Mirzakhani) [...] "
                "In 2016, Viazovska solved the sphere-packing problem in dimension 8. "
                "Her dimension 8 solution quickly led to collaboration with others, and a solution in dimension 24. "
                "Previously, the problem had been solved only for three or fewer dimensions, and the proof of the three-dimensional version (the Kepler conjecture) involved long computer calculations. "
                "In contrast, Viazovska's proof for 8 and 24 dimensions has been described as \"stunningly simple\".",
                nome="Maryna Viazovska"),
            wiki("Sphere_packing",
                "Maryna Viazovska announced a proof of the E8 lattice [...] "
                "providing the optimal packing (regardless of regularity) in eight-dimensional space. "
                "Soon afterwards, she and a group of collaborators announced a similar proof of the Leech lattice [...] "
                "being optimal in 24 dimensions. [...] "
                "res are known for 1–8 and 24 dimensions. "
                "Comparatively little is known about non-lattice hypersphere packings, the optimal result being known only in dimensions 1–3, 8, and 24; it is possible that in some dimensions the densest packing may be irregular. [...] "
                "Sphere packing on the corners of a hypercube (with Hamming balls, spheres defined by Hamming distance) corresponds to designing error-correcting codes [...] "
                "There are other, subtler relationships between Euclidean sphere packing and error-correcting codes. "
                "For example, the binary Golay code is closely related to the 24-dimensional Leech lattice.",
                nome="Sphere packing"),
        ],
    },
    # 11 a conjectura de Kepler, das balas de canhão ao "99% certos"
    {
        "temas_secundarios": ["historia_matematica", "algoritmos"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Um pedido de Walter Raleigh para contar balas de canhão empilhadas levou a um problema que Kepler propôs em 1611. A prova só veio em 1998, com tanto cálculo de computador que os revisores ficaram \"99% certos\".",
        "explicacao": (
            "A conjectura de Kepler diz que nenhum arranjo de esferas iguais preenche o espaço com densidade média "
            "maior que a do empilhamento em camadas hexagonais, cada uma assentada nos vãos da anterior: cerca de "
            "74,05%. Bolinhas despejadas ao acaso num pote chegam a uns 65%. A história começa com Sir Walter "
            "Raleigh, que pediu ao amigo e assistente Thomas Harriot fórmulas para contar balas de canhão "
            "empilhadas. Isso levou Harriot a se perguntar qual seria o melhor jeito de empilhá-las, e ele publicou "
            "um estudo sobre isso em 1591. Foi a troca de cartas com Harriot, em 1606, que levou Kepler a estudar "
            "arranjos de esferas; em 1611, ele enunciou a conjectura num texto sobre o floco de neve de seis "
            "pontas. Em 1831, Gauss provou que nenhum arranjo regular, em forma de rede, é mais denso. Em 1998, "
            "Thomas Hales anunciou uma prova que examinava um grande número de casos com cálculos complexos de "
            "computador. A revista Annals of Mathematics aceitou publicá-la se fosse aprovada por doze revisores, que, "
            "depois de quatro anos, disseram estar \"99% certos\", sem conseguir conferir todos os cálculos. Para "
            "encerrar a dúvida, Hales liderou o projeto Flyspeck, uma prova formal conferida por programas de "
            "verificação. Em 2007, ele estimou que levaria uns 20 anos de trabalho; o projeto foi concluído em 2014."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Kepler_conjecture",
                "It states that no arrangement of equally sized spheres filling space has a greater average density than that of the cubic close packing (face-centered cubic) and hexagonal close packing arrangements. "
                "The density of these arrangements is around 74.05%. "
                "In 1998, the American mathematician Thomas Hales, following an approach suggested by Fejes Tóth (1953),  announced that he had a proof of the Kepler conjecture. "
                "Hales' proof is a proof by exhaustion involving the checking of many individual cases using complex computer calculations. "
                "Referees said that they were \"99% certain\" of the correctness of Hales' proof, and the Kepler conjecture was accepted as a theorem. "
                "In 2014, the Flyspeck project team, headed by Hales, announced the completion of a formal proof of the Kepler conjecture using a combination of the Isabelle and HOL Light proof assistants. [...] "
                "Experiment shows that dropping the marbles in randomly, with no effort to arrange them tightly, will achieve a density of around 65%. [...] "
                "For the first layer of marbles, arrange them in a hexagonal lattice (the honeycomb pattern) "
                "Put the next layer of marbles in the lowest lying gaps you can find above and between the marbles in the first layer [...] "
                "The conjecture was first stated by Johannes Kepler (1611) in his paper 'On the six-cornered snowflake'. "
                "He had started to study arrangements of spheres as a result of his correspondence with the English mathematician and astronomer Thomas Harriot in 1606. "
                "Harriot was a friend and assistant of Sir Walter Raleigh, who had asked Harriot to find formulas for counting stacked cannonballs, an assignment which in turn led Raleigh's mathematician acquaintance into wondering about what the best way to stack cannonballs was. "
                "Harriot published a study of various stacking patterns in 1591 [...] "
                "Despite the unusual nature of the proof, the editors of the Annals of Mathematics agreed to publish it, provided it was accepted by a panel of twelve referees. "
                "In 2003, after four years of work, the head of the referee's panel, Gábor Fejes Tóth, reported that the panel were \"99% certain\" of the correctness of the proof, but they could not certify the correctness of all of the computer calculations. [...] "
                "At the start of this project, in 2007, Hales estimated that producing a complete formal proof would take around 20 years of work.",
                nome="Kepler conjecture"),
            wiki("Sphere_packing",
                "In 1831, Carl Friedrich Gauss proved these packings have the highest density amongst all possible lattice packings.",
                nome="Sphere packing"),
        ],
    },
    # 12 Britney Gallivan e as 12 dobras
    {
        "temas_secundarios": ["personagens_esquecidos"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Dizem que nenhum papel pode ser dobrado ao meio mais de oito vezes. Em 2002, uma estudante do ensino médio dobrou 12 vezes uma tira de papel higiênico de 1,2 km, depois de calcular o comprimento necessário.",
        "explicacao": (
            "O limite não está no papel em si, mas no material que se perde a cada dobra: ao dobrar ao meio, uma "
            "parte do papel fica gasta na curva, contornando as camadas de dentro, e essa perda aumenta a cada nova "
            "dobra. Em dezembro de 2001, a californiana Britney Gallivan, então aluna do ensino médio, deduziu uma "
            "fórmula para o comprimento mínimo de material necessário para dobrá-lo ao meio, sempre na mesma "
            "direção, um certo número de vezes. Na fórmula, esse comprimento é proporcional à espessura do material "
            "e depende de potências de 2 elevadas ao número de dobras, o que faz cada dobra extra exigir uma tira "
            "muito mais longa. A conta mostrava, porém, que não existe um limite fixo: com uma tira comprida o "
            "suficiente, dá para ir além. Em janeiro de 2002, ela dobrou ao meio 12 vezes, na mesma direção, um "
            "pedaço de papel higiênico de cerca de 1.200 metros, desmentindo a crença antiga de que papel não pode "
            "ser dobrado ao meio mais de oito vezes."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Mathematics_of_paper_folding",
            "The maximum number of times an incompressible material can be folded has been derived. "
            "With each fold a certain amount of paper is lost to potential folding.  "
            "The loss function for folding paper in half in a single direction was given to be L=πt6(2n+4)(2n−1), where L is the minimum length of the paper (or other material), t is the material's thickness, and n is the number of folds possible. [...] "
            "This result was derived by Britney Gallivan, a high schooler from California, in December 2001. "
            "In January 2002, she folded a 4,000-foot-long (1,200 m) piece of toilet paper twelve times in the same direction, debunking a long-standing myth that paper cannot be folded in half more than eight times.",
            nome="Mathematics of paper folding")],
    },
    # 13 duplicar o cubo: impossível com régua e compasso, possível com origami
    {
        "temas_secundarios": ["grecia_antiga", "historia_matematica"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Dobrar o volume de um cubo só com régua e compasso, um desafio dos gregos antigos, foi provado impossível em 1837. Mas com algumas dobras de papel dá: a construção por origami foi apresentada em 1986.",
        "explicacao": (
            "O problema leva o nome de Delos. Numa versão da história, os habitantes da ilha consultaram o oráculo "
            "de Delfos para se livrar de uma peste mandada por Apolo; na de Plutarco, para resolver brigas "
            "políticas internas. Nesta, o oráculo mandou dobrar o tamanho do altar de Apolo, que era um cubo, e os "
            "délios, intrigados, foram consultar Platão, que leu a resposta como um problema de geometria. Ainda "
            "segundo Plutarco, Platão passou o desafio a Eudoxo, Arquitas e Menecmo, que o resolveram com meios "
            "mecânicos e levaram uma bronca por não usar geometria pura. Duplicar um cubo de lado 1 exige construir "
            "um segmento igual à raiz cúbica de 2. Cada passo com régua e compasso só produz pontos ligados a "
            "equações de grau no máximo 2, e em 1837 Pierre Wantzel provou que a raiz cúbica de 2 não pode ser "
            "obtida assim. Trissectar um ângulo qualquer também é impossível nessas regras. A dobradura de papel "
            "segue regras diferentes, que permitem resolver equações de até quarto grau. Em 1980, foi apresentada "
            "uma trissecção de ângulos por dobradura e, em 1986, Peter Messer mostrou como duplicar o cubo: o "
            "quadrado de papel é vincado em três faixas iguais, e um canto e uma marca são encaixados em posições "
            "certas."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Doubling_the_cube",
                "The problem owes its name to a story concerning the citizens of Delos, who consulted the oracle at Delphi in order to learn how to defeat a plague sent by Apollo. "
                "According to Plutarch, however, the citizens of Delos consulted the oracle at Delphi to find a solution for their internal political problems at the time [...] "
                "The oracle responded that they must double the size of the altar to Apollo, which was a regular cube. "
                "The answer seemed strange to the Delians, and they consulted Plato, who was a [...] "
                "ho was able to interpret the oracle as the mathematical problem of doubling the volume of a given cube [...] "
                "According to Plutarch, Plato gave the problem to Eudoxus and Archytas and Menaechmus, who solved the problem using mechanical means, earning a rebuke from Plato for not solving the problem using pure geometry. [...] "
                "The nonexistence of a compass-and-straightedge solution was finally proven by Pierre Wantzel in 1837. "
                "In algebraic terms, doubling a unit cube requires the construction of a line segment of length x, where x3 = 2; in other words, x = 23, the cube root of two. [...] "
                "of a new point constructed by a compass and straightedge are roots of polynomials over the field generated by the coordinates of previous points, of no greater degree than a quadratic.",
                nome="Doubling the cube"),
            wiki("Mathematics_of_paper_folding",
                "Some classical construction problems of geometry — namely trisecting an arbitrary angle or doubling the cube — are proven to be unsolvable using compass and straightedge, but can be solved using only a few paper folds. "
                "Paper fold strips can be constructed to solve equations up to degree 4. [...] "
                "A square of paper is first creased into three equal strips as shown in the diagram. "
                "Then the bottom edge is positioned so the corner point P is on the top edge and the crease mark on the edge [...] "
                "In 1986, Messer reported a construction by which one could double the cube, which is impossible with Euclidean constructions. [...] "
                "In 1980 a construction was reported which enabled an angle to be trisected. Trisections are impossible under Euclidean rules.",
                nome="Mathematics of paper folding"),
        ],
    },
    # 14 triângulo de Reuleaux e a broca de furo quadrado
    {
        "temas_secundarios": ["invencoes"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "Existe broca que faz furos quase quadrados. O truque é o triângulo de Reuleaux, uma forma de largura constante: ele gira dentro de um quadrado tocando os quatro lados o tempo todo e só não alcança os cantos.",
        "explicacao": (
            "O triângulo de Reuleaux é a interseção de três discos iguais, cada um centrado na borda dos outros "
            "dois. O resultado parece um triângulo de lados abaulados. Como o círculo, ele tem largura constante: "
            "a distância entre duas retas paralelas que o tocam é a mesma em qualquer direção. Por isso, ele "
            "consegue dar uma volta completa dentro de um quadrado sempre encostado nos quatro lados, varrendo cerca "
            "de 98,8% da área e deixando de fora só pequenas regiões perto dos cantos. A broca de furo quadrado da "
            "Watts Brothers Tool Works usa esse formato, com cavidades que servem de gume, montada num mandril que "
            "deixa a broca girar sem um centro fixo. Henry Watts a patenteou em 1914, mas brocas parecidas já "
            "existiam antes. A largura constante também faz dele uma resposta à pergunta sobre que forma, além do "
            "círculo, uma tampa de bueiro pode ter sem cair pelo buraco. Uma plataforma sobre rolos com esse perfil "
            "anda lisa e plana, mas uma roda com eixo nesse formato pula, porque não gira em torno de um centro fixo. "
            "Já o rotor do motor Wankel, muitas vezes citado como exemplo, tem os lados um pouco mais achatados que "
            "os de um triângulo de Reuleaux."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Reuleaux_triangle",
            "A Reuleaux triangle [ʁœlo] is a curved triangle with constant width, the simplest and best known curve of constant width other than the circle. "
            "It is formed from the intersection of three equally sized circular disks, each centered on the boundary of the other two. "
            "Constant width means that the separation of every two parallel supporting lines is the same, independent of their orientation. "
            "Because its width is constant, the Reuleaux triangle is one answer to the question \"Other than a circle, what shape can a manhole cover be made so that it cannot fall down through the hole?\" [...] "
            "It can perform a complete rotation within a square while at all times touching all four sides of the square, and has the smallest possible area of shapes with this property. "
            "However, although it covers most of the square in this rotation process, it fails to cover a small fraction of the square's area, near its corners. [...] "
            "The shape traced out by the rotating Reuleaux triangle covers approximately 98.8% of the area of the square. [...] "
            "The Watts Brothers Tool Works square drill bit has the shape of a Reuleaux triangle, modified with concavities to form cutting surfaces. "
            "When mounted in a special chuck which allows for the bit not having a fixed centre of rotation, it can drill a hole that is nearly square. "
            "Although patented by Henry Watts in 1914, similar drills invented by others were used earlier. [...] "
            "can roll but makes a poor wheel because it does not roll about a fixed center of rotation. "
            "An object on top of rollers that have Reuleaux triangle cross-sections would roll smoothly and flatly, but an axle attached to Reuleaux triangle wheels would bounce up an [...] "
            "The rotor of the Wankel engine is shaped as a curvilinear triangle that is often cited as an example of a Reuleaux triangle. "
            "However, its curved sides are somewhat flatter than those of a Reul",
            nome="Reuleaux triangle")],
    },
    # 15 a pizza dobrada e o mapa impossível
    {
        "temas_secundarios": ["ciencia_cozinha", "grandes_navegacoes"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "O truque de dobrar a fatia de pizza para a ponta não cair é explicado pelo mesmo teorema de Gauss que prova que nenhum mapa plano da Terra, nem de um pedaço dela, pode ser perfeito.",
        "explicacao": (
            "Em 1827, Carl Friedrich Gauss provou um resultado que batizou de Theorema Egregium, \"teorema "
            "notável\". Ele trata da curvatura gaussiana, uma medida de quanto uma superfície se curva. O teorema "
            "diz que essa curvatura pode ser obtida só com medições feitas sobre a própria superfície, como ângulos "
            "e distâncias, e que ela não muda quando a superfície é dobrada sem ser esticada. Um plano tem "
            "curvatura zero; uma esfera de raio R tem curvatura constante, igual a 1/R². Como os valores não batem, "
            "não dá para estender um pedaço de esfera sobre um plano sem distorcer distâncias: quem pisa numa casca "
            "de ovo vazia vê as bordas rachando antes de ela ficar achatada. Para a cartografia, isso significa que "
            "nenhum mapa plano da Terra pode ser perfeito, e toda projeção distorce algumas distâncias. A pizza "
            "mostra o outro lado da mesma regra. A fatia plana tem curvatura zero e, ao ser curvada ao longo de uma "
            "linha, precisa manter a curvatura perto de zero. Com a curva criada numa direção, a direção "
            "perpendicular fica obrigada a permanecer reta, e a fatia ganha rigidez: segura a forma tempo suficiente "
            "para ser comida sem sujeira. O papelão ondulado e as chapas onduladas de ferro galvanizado usam o mesmo princípio."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Theorema_Egregium",
            "Gauss's Theorema Egregium (Latin for \"remarkable theorem\") is a major result of differential geometry, proved by Carl Friedrich Gauss in 1827, that concerns the curvature of surfaces.  "
            "The theorem says that Gaussian curvature can be determined entirely by measuring angles, distances and their rates of change on a surface, without reference to the particular manner in which the surface is embedded in the ambient 3-dimensional Euclidean space.  "
            "In other words, the Gaussian curvature of a surface does not change if one bends the surface without stretching it. [...] "
            "A sphere of radius R has constant Gaussian curvature which is equal to 1/R2. At the same time, a plane has zero Gaussian curvature. [...] "
            "Conversely, the surface of a sphere cannot be unfolded onto a flat plane without distorting the distances. "
            "If one were to step on an empty egg shell, its edges have to split in expansion before being flattened. "
            "Mathematically, a sphere and a plane are not isometric, even locally. "
            "This fact is significant for cartography: it implies that no planar (flat) map of Earth can be perfect, even for a portion of the Earth's surface. "
            "Thus every cartographic projection necessarily distorts at least some distances. [...] "
            "This is of practical use in construction, as well as in a common pizza-eating strategy: A flat slice of pizza can be seen as a surface with constant Gaussian curvature 0. "
            "Gently bending a slice must then roughly maintain this curvature [...] "
            "This creates rigidity in the direction perpendicular to the fold, an attribute desirable for eating pizza, as it holds its shape long enough to be consumed without a mess. "
            "This same principle is used for strengthening in corrugated materials, most familiarly with corrugated fiberboard and corrugated galvanised iron",
            nome="Theorema Egregium")],
    },
]
