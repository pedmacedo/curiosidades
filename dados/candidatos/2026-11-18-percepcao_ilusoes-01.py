LOTE = "2026-11-18-percepcao_ilusoes-01"
AREA = "mente"
TEMA = "percepcao_ilusoes"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o gorila nas tomografias dos radiologistas
    {
        "temas_secundarios": ["experimentos_psicologia", "historia_medicina"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Radiologistas procuravam nódulos de câncer em tomografias do pulmão. Numa das imagens havia um gorila do tamanho de uma cartela de fósforos. Dos especialistas, 83% não o notaram.",
        "explicacao": (
            "O fenômeno se chama cegueira por desatenção. O teste mais famoso foi publicado em 1999 por Daniel "
            "Simons e Christopher Chabris: os voluntários assistiam a um vídeo de dois times trocando passes de "
            "basquete e tinham de contar os passes. No meio da cena, alguém fantasiado de gorila atravessava a "
            "quadra, e na maioria dos grupos metade das pessoas não relatou tê-lo visto. Em 2013, o psicólogo "
            "Trafton Drew e colegas levaram a ideia aos especialistas: inseriram a imagem de um gorila numa "
            "tomografia de tórax e pediram a radiologistas que buscassem nódulos de câncer. A grande maioria não "
            "percebeu o intruso. Segundo Drew, o problema não era para onde iam os olhos: eles olhavam direto para "
            "o gorila, mas, como não procuravam um gorila, não o enxergavam. Num estudo divulgado em 2020, 50 "
            "radiologistas avaliaram sete tomografias em busca de câncer de pulmão, e a última trazia uma massa na "
            "mama e um gânglio linfático anormal. Dois terços não notaram a massa, e um terço não viu o gânglio. A "
            "experiência profissional não fez diferença. Quando a tarefa pedia anomalias em geral, só 3% deixaram "
            "passar a massa."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": "https://www.eurekalert.org/news-releases/577138",
             "titulo": "Missing the radiological forest for the trees (University of Utah, via EurekAlert!)",
             "idioma": "en",
             "trecho": "18-Nov-2020 [...] "
                "adds Drew, associate professor of psychology [...] "
                "So, in 2013, Drew and colleagues conducted an experiment to understand how trained experts could miss those clear signs. "
                "In that study, the authors presented radiologists with chest computed tomography (CT) scans and asked them to look for lung cancer nodules. "
                "But the authors had also placed an image of a gorilla into the scan [...] "
                "Drew and his colleagues found that 83% of radiologists did not notice the gorilla. [...] "
                "They asked 50 radiologists to evaluate seven chest CT scans for lung cancer, but this time the final scan included two clear abnormalities: "
                "a significant breast mass and a lymphadenopathy (an abnormal lymph node). "
                "Two-thirds of the radiologists did not notice the potentially cancerous mass. A third did not notice the lymphadenopathy. [...] "
                "Experience wasn't a factor in whether or not the radiologists noticed the abnormalities [...] "
                "the researchers asked radiologists to look at the same scan and report on a broader range of abnormalities. "
                "This time, only 3% missed the mass and 10% missed the lymphadenopathy."},
            {"url": "https://www.kunc.org/npr-news/2013-02-11/why-even-radiologists-can-miss-a-gorilla-hiding-in-plain-sight",
             "titulo": "Why Even Radiologists Can Miss A Gorilla Hiding In Plain Sight (NPR)",
             "idioma": "en",
             "trecho": "He wanted to see if they would notice a gorilla the size of a matchbook glaring angrily at them from inside the slide. "
                "But they didn't: 83 percent of the radiologists missed it, Drew says. "
                "This wasn't because the eyes of the radiologists didn't happen to fall on the large, angry gorilla. [...] "
                "\"They look right at it, but because they're not looking for a gorilla, they don't see that it's a gorilla,\" Drew says."},
            wiki("Inattentional_blindness",
                "The best-known study demonstrating inattentional blindness is the Invisible Gorilla Test, conducted by Daniel Simons of the University of Illinois at Urbana–Champaign and Christopher Chabris of Harvard University. [...] "
                "was published in the journal Perception in 1999. [...] "
                "asked subjects to watch a short video of two groups of people (either wearing black or white T-shirts) passing a basketball around. "
                "The subjects are told either to count the passes made by one of the teams or to keep count of bounce passes vs. aerial passes. "
                "In different versions of the video a person walks through the scene carrying an umbrella (as discussed above) or wearing a full gorilla suit. [...] "
                "In most groups, 50% of the subjects did not report seeing the gorilla (or the person with the umbrella).",
                nome="Inattentional blindness"),
        ],
    },
    # 2 o cego que desviou de obstáculos (visão cega)
    {
        "temas_secundarios": ["neurociencia", "consciencia"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Um homem perdeu toda a visão consciente depois que dois AVCs destruíram o córtex visual. Mesmo assim, atravessou sem bengala um corredor cheio de obstáculos, sem bater em nenhum.",
        "explicacao": (
            "O fenômeno se chama visão cega, termo criado por Lawrence Weiskrantz e colegas num artigo de 1974. "
            "Ele aparece em pessoas que ficaram cegas por lesões no córtex visual primário: elas reagem a estímulos que dizem não ver. Obrigadas a chutar se "
            "há algo no campo cego, algumas acertam mais do que o acaso permitiria. A maioria dos pacientes, porém, "
            "perdeu só metade do campo visual, e a visão que resta poderia ajudar. Por isso chama atenção o caso do "
            "homem conhecido como TN: aos 52 anos, dois AVCs destruíram o córtex visual primário dos dois lados do "
            "cérebro. Pesquisadores o convenceram a andar por um corredor cheio de obstáculos, sem bengala e sem "
            "conhecer o lugar. Ele foi até o fim sem esbarrar em nada e chegou a se encostar na parede para "
            "contornar uma lixeira. Em outro teste, TN adivinhou acima do acaso a emoção de rostos que não "
            "enxergava. A existência da visão cega ainda é debatida: há quem defenda que seja apenas uma visão "
            "consciente muito degradada."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [wiki("Blindsight",
            "Blindsight is the ability of people who are cortically blind to respond to visual stimuli that they do not consciously see due to lesions in the primary visual cortex [...] "
            "The term was coined by Lawrence Weiskrantz and his colleagues in a paper published in a 1974 issue of Brain. [...] "
            "The assumed existence of blindsight is controversial, with some arguing that it is merely degraded conscious vision. [...] "
            "The majority of studies on blindsight are conducted on patients who are hemianopic (i.e. blind in one-half of their visual field) [...] "
            "if forced to guess about whether a stimulus is present in their blind field, some observers do better than chance. [...] "
            "A potential weak point of case studies like the ones above is that the participants were not completely blind, and therefore it is not out of the question that their existing vision could have assisted them in some way. "
            "So a particularly noteworthy patient is a man known as \"TN\", who suffered two strokes at age 52 that resulted in the destruction of the primary visual cortex (V1) in both hemispheres of the brain, and hence complete loss of (conscious) sight. "
            "In one famous case, researchers persuaded TN to walk down an obstacle-filled hallway, without his cane or any prior knowledge of the layout. "
            "He was able to navigate the full length of the hallway without hitting a single object, at one point even hugging the wall to get past a trashcan. [...] "
            "While he could not guess the gender or shape accurately, he correctly guessed what emotion was shown at an above chance level.",
            nome="Blindsight")],
    },
    # 3 síndrome de Charles Bonnet
    {
        "temas_secundarios": ["neurociencia", "historia_medicina"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Quem perde muito da visão pode passar a ver pessoas, bichos e paisagens que não existem, quase sempre sabendo que são ilusões. Em 1760, o naturalista Charles Bonnet descreveu isso no avô quase cego.",
        "explicacao": (
            "A condição leva o nome dele: síndrome de Charles Bonnet. O avô, de 87 anos, estava quase cego por "
            "catarata nos dois olhos e passou a ver homens, mulheres, pássaros, carruagens, prédios e tapeçarias, "
            "sem ter nenhum transtorno psiquiátrico. Aos 40 anos, o próprio Bonnet perdeu gravemente a visão, por "
            "causa nunca revelada, e também teve as alucinações. Elas são só visuais e podem ser simples, como "
            "formas e grades, ou complexas, como figuras silenciosas, multidões ou paisagens cheias de detalhes. Às "
            "vezes os personagens são minúsculos. As mais comuns são rostos ou desenhos animados. A teoria mais "
            "aceita é que, sem os sinais dos olhos, o córtex visual fica desinibido e dispara sozinho. Entre idosos "
            "com perda importante de visão, estudos relatam que 10% a 40% passam por isso. O número real é incerto, "
            "porque muitos não contam a ninguém, com medo de serem tomados por loucos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Charles_Bonnet_syndrome",
            "Visual release hallucinations, also known as Charles Bonnet syndrome (CBS), are a type of psychophysical visual disturbance in which a person with partial or severe blindness experiences visual hallucinations. "
            "First described by Charles Bonnet in 1760 [...] "
            "These can vary greatly in apparent size, sometimes \"lilliputian\" (smaller than normal) [...] "
            "Simple hallucinations often involve shapes, photopsias, and grid-like patterns. "
            "Complex hallucinations may depict silent, non-interactive figures, whether multitudes of people, animals, or surreal objects, that appear life-like, as well as highly detailed landscapes or objects. "
            "The most common hallucination is of faces or cartoons. "
            "Those affected understand that the hallucinations are not real, although in some cases, particularly when cognitive decline progresses, they may begin to perceive them as genuine. "
            "Hallucinations are purely visual [...] "
            "Among older adults (> 65 years) with significant vision loss, the prevalence of Charles Bonnet syndrome has been reported to be between 10% and 40% [...] "
            "Underreporting is thought to be a result of those with the condition being afraid to discuss the symptoms out of fear that they will be labeled of unsound mind. [...] "
            "The most commonly accepted theory for Charles Bonnet syndrome proposes that extreme visual impairment promotes sensory deafferentation, leading to disinhibition, thus resulting in sudden neural firings of the visual cortical regions. [...] "
            "The disease was first noted by the Swiss naturalist Charles Bonnet, who described the condition in 1760. "
            "He documented it in his 87-year-old grandfather who was nearly blind from cataracts in both eyes. [...] "
            "His hallucinations consisted of perceptions of men, women, birds, carriages, buildings, tapestries, physically impossible circumstances and scaffolding patterns. "
            "Even though his health was in good shape and he had an absence of any psychiatric disorders, the source of the hallucinations remained unknown. "
            "At forty years old, Charles Bonnet himself developed an unrevealed cause of severe vision loss and experienced the hallucinations.",
            nome="Charles Bonnet syndrome")],
    },
    # 4 Müller-Lyer e as culturas
    {
        "temas_secundarios": ["arquitetura", "experimentos_psicologia"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Duas linhas iguais, uma com pontas de seta para fora e outra para dentro, parecem ter tamanhos diferentes. Num estudo de 1963, os San do Kalahari foram os que menos caíram no truque, e os europeus, os que mais.",
        "explicacao": (
            "A ilusão foi criada em 1889 pelo sociólogo alemão Franz Carl Müller-Lyer. Na virada para o século 20, W. H. R. "
            "Rivers já relatava que os nativos da ilha Murray, na Austrália, eram menos suscetíveis a ela do que "
            "os europeus. Em 1963, Marshall Segall, Donald Campbell e Melville Herskovits compararam amostras de "
            "europeus, africanos e filipinos: o erro médio na avaliação das linhas ia de 1,4% a 20,3%. As três "
            "amostras de origem europeia foram as mais enganadas, e os San, caçadores-coletores do deserto do "
            "Kalahari, as menos. Num artigo de 1966, com dezessete culturas, os autores propuseram uma explicação: quem "
            "vive em cidades está cercado de retas, ângulos retos e cantos quadrados, um mundo \"carpinteirado\", e por isso seria "
            "mais suscetível. A ideia não está resolvida. Gustav Jahoda "
            "comparou membros de um mesmo povo africano vivendo no campo e na cidade e não achou diferença "
            "significativa, e sugeriu que a pigmentação da retina tenha papel. Já um estudo de 1978 na Zâmbia "
            "achou moradores urbanos bem mais suscetíveis. Vale lembrar que todos os povos testados caem na "
            "ilusão em algum grau, segundo as pesquisas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Müller-Lyer_illusion",
            "The illusion was devised by Franz Carl Müller-Lyer (1857–1916), a German sociologist, in 1889. "
            "Research suggests all humans are susceptible to the illusion across cultures. [...] "
            "Around the turn of the 20th century, W. H. R. Rivers wrote that indigenous people of the Australian Murray Island were less susceptible to the Müller-Lyer illusion than were Europeans. [...] "
            "In 1963, Segall, Campbell and Herskovitz compared susceptibility to four different visual illusions in three population samples of Caucasians, twelve of Africans, and one from the Philippines. "
            "For the Müller-Lyer illusion, the mean fractional misperception of the length of the line segments varied from 1.4% to 20.3%. "
            "The three European-derived samples were the three most susceptible samples, while the San foragers of the Kalahari desert were the least susceptible. [...] "
            "In their definitive paper of 1966, they investigated seventeen cultures and showed that people in different cultures differ substantially on how they experience the Müller-Lyer stimuli. "
            "They wrote that \"European and American city dwellers have a much higher percentage of rectangularity in their environments than non-Europeans and so are more susceptible to that illusion.\" "
            "They also used the word \"carpentered\" for the environments that Europeans mostly live in - characterized by straight lines, right angles, and square corners. "
            "These conclusions were challenged in later work by Gustav Jahoda, who compared members of an African tribe living in a traditional rural environment with members of same group living in African cities. "
            "Here, no significant difference in susceptibility to the M-L illusion was found. "
            "Subsequent work by Jahoda suggested that retinal pigmentation may have a role in the differing perceptions on this illusion [...] "
            "A later study was conducted in 1978 by Ahluwalia on children and young adults from Zambia. "
            "Subjects from rural areas were compared with subjects from urban areas. "
            "The subjects from urban areas were shown to be considerably more susceptible to the illusion",
            nome="Müller-Lyer illusion")],
    },
    # 5 a ilusão da Lua
    {
        "temas_secundarios": ["historia_astronomia", "sistema_solar"],
        "tipos_espanto": ["misterio_aberto", "contraintuitivo"],
        "gancho": "No horizonte, a Lua parece bem maior do que no alto do céu, embora ali esteja um pouco mais longe de nós. A ilusão é conhecida desde a Antiguidade e ainda não tem uma explicação aceita por todos.",
        "explicacao": (
            "Medida com instrumento, a Lua ocupa o mesmo ângulo no céu em qualquer altura, e fotos mostram o mesmo "
            "tamanho. Perto do horizonte ela está até cerca de 1,5% mais distante e, portanto, um tiquinho menor. "
            "Um teste caseiro: uma pedrinha de 8,4 milímetros, segurada com o braço esticado, cobre a Lua tanto "
            "no alto quanto no horizonte. Mesmo assim, a ilusão costuma aumentar o diâmetro aparente em cerca de "
            "50%. Ptolomeu tentou explicá-la pela refração da atmosfera, e o astrônomo Cleomedes, por volta do ano "
            "200, a atribuiu à refração e a mudanças na distância aparente. Entre 1011 e 1022, Ibn al-Haytham propôs que os objetos entre nós "
            "e o horizonte mudam a nossa noção de distância. Só no século 17 a ilusão passou a ser aceita como "
            "fenômeno psicológico. Hoje a pista mais forte é ver o terreno até o horizonte, e a explicação mais "
            "popular a compara à ilusão de Ponzo. Mesmo assim, o debate segue: um livro de 2002 que revisou as "
            "teorias concluiu que nenhuma saiu vitoriosa, e um livro de 2013 reuniu 19 capítulos de pesquisadores "
            "que chegam a conclusões diferentes."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Moon_illusion",
            "The Moon illusion is the optical illusion of the Moon appearing larger near the horizon than it does higher up in the sky. "
            "It has been known since ancient times and recorded by various cultures. "
            "The illusion is seen also with other celestial objects (such as in a sunset or sunrise, and constellations) and remains inconclusively explained, with the ponzo illusion as a popular explanation. [...] "
            "The Moon is actually only about 1.5% farther away and thus smaller in angular size when at the horizon than when above. "
            "The angle that the diameter of the full Moon subtends at an observer's eye can be measured directly with a theodolite to show that it remains constant as the Moon rises or sinks in the sky. "
            "Photographs of the Moon at different elevations also show that its size remains the same. "
            "A simple way of demonstrating that the effect is an illusion is to hold a small pebble (say, 0.33 inches or 8.4 millimetres wide) at arm's length [...] "
            "The 2013 book The Moon Illusion, edited by Hershenson, offers 19 chapters written by various illusion researchers reaching different conclusions. "
            "After reviewing the many different explanations in their 2002 book The Mystery of the Moon Illusion, Ross and Plug conclude \"No single theory has emerged victorious.\" "
            "They argue that the size of the illusion is variable, but is usually an apparent increase in diameter of about 50 percent. "
            "The most important factor is the sight of the terrain [...] "
            "Ptolemy attempted to explain the Moon illusion through atmospheric refraction in the Almagest [...] "
            "Similarly Cleomedes (about 200 A.D.), in his book on astronomy, ascribed the illusion both to refraction and to changes in apparent distance. "
            "In the Book of Optics (1011–1022 A.D.), Ibn al-Haytham (Alhazen) repeated refraction as an explanation, but also proposed a more detailed explanation based on intervening objects and apparent distance. [...] "
            "the Moon illusion came to be accepted as a psychological phenomenon in the 17th century.",
            nome="Moon illusion")],
    },
    # 6 o efeito Thatcher
    {
        "temas_secundarios": ["neurociencia", "evolucao"],
        "tipos_espanto": ["contraintuitivo", "origem_inesperada"],
        "gancho": "Numa foto de rosto de cabeça para baixo, olhos e boca invertidos passam quase despercebidos. Desvire a foto, e o rosto fica grotesco. O truque foi criado em 1980 com uma foto de Margaret Thatcher.",
        "explicacao": (
            "O criador foi o psicólogo Peter Thompson, da Universidade de York, que usou a foto da então "
            "primeira-ministra britânica, e por isso o fenômeno ficou conhecido como efeito Thatcher. Basta "
            "inverter verticalmente os olhos e a boca, deixando o resto do rosto como está. De cabeça para baixo, a "
            "alteração quase não se nota; na posição normal, salta aos olhos. A explicação mais aceita é que o "
            "cérebro tem processos especializados em rostos na posição de sempre. Para distinguir caras tão "
            "parecidas entre si, ele usaria tanto a configuração, ou seja, a relação entre os traços, quanto os "
            "detalhes de cada olho, nariz e boca. Há "
            "indícios de que macacos-rhesus e chimpanzés também caem no efeito, o que sugere que parte desse "
            "maquinário de rostos pode vir de um ancestral comum de mais de 30 milhões de anos. Já pessoas com "
            "prosopagnosia congênita, a dificuldade de reconhecer rostos, reagem bem menos à ilusão."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Thatcher_effect",
            "The Thatcher effect, or Thatcher illusion, is a phenomenon in which changes to facial features are difficult to detect when a face is upside-down, even though the same changes are obvious in an upright face. "
            "It is named after the then British prime minister Margaret Thatcher, on whose photograph the effect was first demonstrated. "
            "The effect was originally created in 1980 by Peter Thompson, professor of psychology at the University of York. [...] "
            "The second picture is altered so that the eyes and mouth are vertically flipped, though the changes are not immediately obvious until the image is viewed upright. "
            "The Thatcher effect is thought to be due to specific psychological cognitive modules involved in face perception which are tuned especially to upright faces. [...] "
            "It has been hypothesized that humans develop specific processes to differentiate between faces that rely as much on the configuration (the structural relationship between individual features on the face) as the details of individual face features, such as the eyes, nose and mouth. "
            "There is evidence that rhesus monkeys as well as chimpanzees experience the Thatcher effect, raising the possibility that some brain mechanisms involved in processing faces may have evolved in a common ancestor more than 30 million years ago. [...] "
            "However, people with congenital prosopagnosia have been shown to exhibit an overall much weaker response to the illusion compared to people without such condition.",
            nome="Thatcher effect")],
    },
    # 7 a mão de borracha e a suspeita de sugestão
    {
        "temas_secundarios": ["experimentos_psicologia", "neurociencia"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "Esconda a mão de alguém, ponha uma mão de borracha à vista e acaricie as duas com um pincel ao mesmo tempo: muita gente passa a sentir a falsa como sua. Hoje se discute quanto disso é sugestão.",
        "explicacao": (
            "A ilusão da mão de borracha foi relatada em 1998 por Botvinick e Cohen. Quando a mão escondida e a "
            "falsa recebem pinceladas sincronizadas e na mesma direção, a pessoa começa a vivê-la como parte do "
            "corpo; se as pinceladas são desencontradas, não. Pedidas para apontar a própria mão, as cobaias "
            "costumam indicar a de borracha. Em exames de imagem, a sensação coincide com a ativação do córtex "
            "pré-motor. Quando a mão falsa é ameaçada com uma agulha, acende uma região ligada à expectativa de "
            "dor, e os voluntários reagiam puxando a mão verdadeira, que nunca esteve em perigo. Até macacos-rhesus caem no truque. "
            "Desde 2019, porém, Lush e colegas questionam a interpretação clássica. Num estudo "
            "com 353 participantes, a força da ilusão acompanhou a sugestionabilidade hipnótica de cada um, e eles "
            "argumentaram que as expectativas dos voluntários nunca foram bem controladas nesses experimentos e "
            "que podem explicar parte, ou até tudo, do efeito. Em 2022, Slater e Ehrsson responderam que "
            "os dados não sustentam essa conclusão e que o motor principal é a integração entre visão e tato."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Body_transfer_illusion",
                "The rubber hand illusion was originally reported by Botvinick and Cohen in 1998. [...] "
                "Subjects with normal brain function were positioned with their left hand hidden out of sight. "
                "They saw a lifelike rubber left hand in front of them. "
                "The experimenters stroked both the subjects hidden left hand and the visible rubber hand with a paintbrush. "
                "The experiment showed that if the two hands were stroked synchronously and in the same direction, the subjects began to experience the rubber hand as their own. "
                "When asked to use their right hand to point to their left hand, most of the time they pointed toward the rubber hand. "
                "If the real and rubber hands were stroked in different directions or at different times, the subjects did not experience the rubber hand as their own. [...] "
                "as the subjects began to experience the rubber hand as their own, in the premotor cortex [...] "
                "Then, threatened the rubber hand by making a stabbing movement toward it with a needle (not actually making contact with the rubber hand). "
                "MRI scans showed increase activity in a region of the brain called the anterior cingulate cortex that is normally activated when a person anticipates pain [...] "
                "The anticipation of the needle made the subjects react as if the rubber hand was their own, moving their real hand to avoid the needle even though it was never actually in danger. "
                "The rubber hand illusion can be induced in rhesus monkeys [...] "
                "In 2019, Lush et al., reported correlations between response to the rubber hand illusion and both response to imaginative suggestions in hypnosis and participant expectations for illusion experience and argued that body transfer illusions may be suggestion effects generated by participants' expectations. "
                "In 2020, Lush reported that demand characteristics (contextual cues which prime participant expectations) have not been controlled in rubber hand illusion experiments, and argued that existing reports of body transfer illusions may be entirely accounted for by suggestion effects. "
                "In 2022, Slater and Ehrsson argued that Lush's claims were not supported by the data and that the major factor driving the rubber hand illusion is multisensory integration.",
                nome="Body transfer illusion"),
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7519080/fullTextXML",
             "titulo": "Trait phenomenological control predicts experience of mirror synaesthesia and the rubber hand illusion (Nature Communications, 2020, via Europe PMC)",
             "idioma": "en",
             "trecho": "In large sample studies (of 156, 404 and 353 participants), we report substantial relationships between hypnotisability and experimental measures of experiential change in mirror-sensory synaesthesia and the rubber hand illusion [...] "
                "we collected RHI and hypnotisability measures from 353 participants across groups [...] "
                "These embodiment effects may or may not be entirely attributable to demand characteristics and phenomenological control."},
        ],
    },
    # 8 o coelho cutâneo
    {
        "temas_secundarios": ["sentidos", "neurociencia"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "Toques rápidos perto do pulso e depois perto do cotovelo são sentidos como pulinhos subindo pelo braço, inclusive no meio, onde nada tocou. O efeito aparece até ao longo de um bastão apoiado nos dedos.",
        "explicacao": (
            "É a ilusão do coelho cutâneo, descoberta no início dos anos 1970 por Frank Geldard e Carl Sherrick, "
            "da Universidade de Princeton. Eles compararam a sensação à de um coelho saltitando sobre a pele. Ela "
            "funciona melhor onde a pele distingue mal os pontos, como o antebraço, e só aparece se os toques "
            "vierem bem seguidos: com mais de cerca de 0,3 segundo entre eles, some. Os toques fantasmas ativam a "
            "mesma área do mapa sensorial do cérebro que toques reais ativariam. Quando voluntários apoiaram um "
            "bastão entre as pontas dos indicadores e receberam os toques por ele, sentiram os pulinhos ao longo do "
            "bastão, como se o objeto fizesse parte do corpo. Os mecanismos neurais exatos são desconhecidos. Um "
            "modelo estatístico reproduz bem o efeito supondo que o cérebro espera que estímulos na pele fiquem "
            "parados ou se movam devagar: diante de toques muito rápidos, conclui que eles estavam mais próximos "
            "do que estavam. Em 2009, pesquisadores da Philips mostraram uma jaqueta que aproveitava a ilusão para "
            "fazer sentir na pele cenas de filme com menos motores."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Cutaneous_rabbit_illusion",
            "The cutaneous rabbit illusion (also known as cutaneous saltation and sometimes the cutaneous rabbit effect or CRE) is a tactile illusion evoked by tapping two or more separate regions of the skin in rapid succession. "
            "The illusion is most readily evoked on regions of the body surface that have relatively poor spatial acuity, such as the forearm. "
            "A rapid sequence of taps delivered first near the wrist and then near the elbow creates the sensation of sequential taps hopping up the arm from the wrist towards the elbow, although no physical stimulus was applied between the two actual stimulus locations. [...] "
            "The illusion was discovered by Frank Geldard and Carl Sherrick of Princeton University, in the early 1970s [...] "
            "Geldard and Sherrick likened the perception to that of a rabbit hopping along the skin, giving the phenomenon its name. [...] "
            "the illusion disappears if the temporal separation between taps exceeds about 0.3 seconds (300 milliseconds). [...] "
            "Another study showed that the illusory taps are associated with neural activity in the same area of the brain's sensory map that is activated by real taps to the skin. "
            "Nevertheless, the specific neural mechanisms that underlie the rabbit illusion are unknown. [...] "
            "When subjects supported a stick across their index fingertips and received the taps via the stick, they reported sensing the illusory taps along the stick. "
            "This suggests that the cutaneous rabbit effect involves not only the intrinsic somatotopic representation but also the representation of the extended body schema that results from body-object interactions. [...] "
            "In 2009, researchers of Philips Electronics demonstrated a jacket lined with actuator motors and designed to evoke various tactile sensations while watching a movie. "
            "The device takes advantage of the cutaneous rabbit illusion to reduce the number of actuators needed. [...] "
            "A Bayesian perceptual model closely replicates the cutaneous rabbit and other tactile spatiotemporal illusions. "
            "According to this model, brain circuitry encodes the expectation, acquired through sensory experience, that tactile stimuli tend to be stationary or to move only slowly. [...] "
            "The expectation that stimuli tend to move slowly results in the perceptual conclusion that rapidly successive stimuli are more likely to be closer together on the skin.",
            nome="Cutaneous rabbit illusion")],
    },
    # 9 o phi colorido: a cor muda antes da hora
    {
        "temas_secundarios": ["consciencia", "cinema_fotografia"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "Pisque um ponto azul e, logo depois, um vermelho em outro lugar: muita gente vê um só ponto que anda e muda de cor no meio do caminho. Só que relatam ver a troca de cor antes de o ponto vermelho surgir.",
        "explicacao": (
            "O efeito se chama phi colorido e foi descrito pelos psicólogos Paul Kolers e Michael von Grünau. Eles "
            "o investigaram para responder a uma pergunta do filósofo Nelson Goodman: o que acontece com a ilusão "
            "de movimento aparente, a mesma que faz uma sequência de imagens paradas parecer animada, quando as "
            "duas imagens têm cores diferentes? No experimento clássico, projeta-se um ponto azul no alto da tela "
            "e, em seguida, um vermelho embaixo. Com certas combinações de distância e intervalo, o espectador vê "
            "o primeiro ponto deslizar e mudar de cor bruscamente na metade do trajeto. Aí está o enigma: a troca "
            "é percebida num ponto do caminho em que o ponto vermelho ainda não foi mostrado, o que não poderia "
            "ser vivido de fato naquele instante. O filósofo Daniel Dennett usou o fenômeno em seu argumento contra o chamado materialismo "
            "cartesiano, e outros pesquisadores propõem explicações mais simples, de modo que a interpretação "
            "continua em disputa."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [wiki("Color_phi_phenomenon",
            "The color phi phenomenon is the fact that, when apparent motion is induced between objects with different colors, the color of the apparently moving object abruptly changes midway along the path. "
            "It is a perceptual illusion described by psychologists Paul Kolers and Michael von Grünau in which a disembodied perception of motion is produced by a succession of still images. [...] "
            "Kolers and von Grünau originally investigated the phenomenon in response to a question posed by the philosopher Nelson Goodman, who asked what the effect of the color change would have on the phi phenomenon. [...] "
            "The first image depicts a blue dot at the top of the frame. The second image depicts a red dot on the bottom of the frame. [...] "
            "At certain combinations of spacing and timing of the two images, a viewer will report a sensation of motion in the space between the two dots. "
            "The first spot will begin to appear to be moving, and will then \"change color abruptly in the middle of its illusory path\". [...] "
            "When asked to describe their experience, subjects report seeing the abrupt color change before the second dot is presented. "
            "However, it is impossible for a subject to actually experience the color change before the second dot has been presented. "
            "Philosopher Daniel Dennett utilizes the color phi phenomenon in his argument against a philosophy known as Cartesian materialism. "
            "Psychobiologist John Staddon contrasts a simple \"new behaviorism\" interpretation of color phi with Dennett and Kinsbourne's account. [...] "
            "Alternatively, phi can be explained without Dennett's argument.",
            nome="Color phi phenomenon")],
    },
    # 10 a ilusão tamanho-peso e as caixas de fósforos
    {
        "temas_secundarios": ["sentidos", "ciencia_esporte"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Ponha um peso dentro de uma de três caixas de fósforos vazias. Erguida sozinha, ela parece mais pesada do que as três juntas, empilhadas com ela no topo. É a ilusão tamanho-peso.",
        "explicacao": (
            "A ilusão foi demonstrada em experimento pelo médico francês Augustin Charpentier: entre dois objetos "
            "de mesma massa, o maior parece mais leve. Algo parecido acontece com material e cor: um recipiente de "
            "metal parece mais leve que um de madeira de mesmo tamanho e massa, e objetos escuros parecem mais "
            "pesados que claros. A primeira explicação era mecânica: esperando que o objeto grande pese mais, a "
            "pessoa o ergue com mais força, e ele sobe fácil demais. Mas a ilusão aparece também quando os objetos "
            "são apenas pousados sobre mãos apoiadas, sem levantamento nenhum. E estudos mostraram que a força "
            "usada para erguer se ajusta rápido à massa real, enquanto a ilusão continua. Por isso ela é vista como "
            "uma recalibração da percepção a partir do que se esperava. Há quem a chame de \"anti-bayesiana\", "
            "porque o cérebro daria peso demais à informação inesperada em vez de fazer uma média; outros "
            "pesquisadores acham que ela resulta de uma inferência ótima, só que mais complexa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Size–weight_illusion",
            "The size–weight illusion, also known as the Charpentier illusion, is named after the French physician Augustin Charpentier because he was the first to demonstrate the illusion experimentally. [...] "
            "The illusion occurs when a person underestimates the weight of a larger object (e.g. a box) when compared to a smaller object of the same mass. [...] "
            "Similar illusions occurs with differences in material and colour: metal containers feel lighter than wooden containers of the same size and mass, and darker objects feel heavier than brighter objects of the same size and mass. [...] "
            "An early explanation of these illusions was that people judge the weight of an object from its appearance and then lift it with a pre-determined force. "
            "They expect a larger object to be heavier and therefore lift it with greater force: the larger object is then lifted more easily than the smaller one, causing it to be perceived as lighter. "
            "This hypothesis was disproved by an experiment in which two objects of the same mass, same cross section, but different height were placed on observers' supported hands, and produced a passive size–weight illusion. "
            "Recent studies have also shown that the lifting force quickly adapts to the true mass of the objects, but the size–weight illusion remains. "
            "The illusion therefore cannot be explained by the manner of lifting, and must be due to some perceptual rescaling based on prior expectations. "
            "The rescaling has been described as sub-optimal (anti-Bayesian), in that the central nervous system integrates prior expectations with current proprioceptive information in a way that emphasises the unexpected information rather than taking an average of all information. "
            "It has also recently been suggested that the illusion may not be anti-Bayesian, but may instead rely on more complex yet still optimal inference processes than traditionally suggested. [...] "
            "It has also been demonstrated that, taking three empty matchboxes, and putting a weight in one of them, the weighted box lifted on its own feels heavier than all three boxes lifted together with the heavy one on top.",
            nome="Size–weight illusion")],
    },
    # 11 sinestesia aprendida com letras magnéticas
    {
        "temas_secundarios": ["brinquedos", "memoria"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "Há pessoas que veem cada letra com uma cor fixa. Num estudo com 6.588 delas nos EUA, ao menos 400 tinham as cores de um brinquedo: um conjunto de letras magnéticas da Fisher-Price vendido de 1971 a 1990.",
        "explicacao": (
            "É a sinestesia grafema-cor, em que letras ou números são percebidos como se tivessem cor própria. O "
            "estudo, publicado em 2015 por Witthoft e colegas, analisou as cores "
            "que 6.588 sinestetas americanos atribuíam às 26 letras em testes on-line. Os pesquisadores compararam "
            "essas escolhas com as cores do brinquedo, letras imantadas. Cerca de 6% dos participantes "
            "tinham dez ou mais letras com a mesma cor do conjunto, algo que, numa simulação com as respostas "
            "embaralhadas, ocorreu em menos de 0,009% dos casos. Para os nascidos em alguns períodos de cinco anos "
            "logo depois do lançamento, a fração chegou perto de 15%. E nenhum dos nascidos cinco anos ou mais "
            "antes da fabricação tinha as cores do brinquedo. Os autores frisam que o ímã foi a origem das "
            "combinações, não a causa da sinestesia: a única diferença aparente entre esses sinestetas e os outros "
            "era a exposição ao brinquedo. Ou seja, uma condição que parece inata pode ganhar o conteúdo do que a "
            "criança tinha na porta da geladeira."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [{"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4349591/fullTextXML",
            "titulo": "Prevalence of learned grapheme-color pairings in a large online sample of synesthetes (PLoS ONE, 2015, via Europe PMC)",
            "idioma": "en",
            "trecho": "2015 Witthoft et al [...] "
                "In this paper we estimate the minimum prevalence of grapheme-color synesthetes with letter-color matches learned from an external stimulus, by analyzing a large sample of English-speaking grapheme-color synesthetes. "
                "We find that at least 6% (400/6588 participants) of the total sample learned many of their matches from a widely available colored letter toy. "
                "Among those born in the decade after the toy began to be manufactured, the proportion of synesthetes with learned letter-color pairings approaches 15% for some 5-year periods. "
                "Among those born 5 years or more before it was manufactured, none have colors learned from the toy. "
                "Analysis of the letter-color matching data suggests the only difference between synesthetes with matches to the toy and those without is exposure to the stimulus. [...] "
                "In this paper we examine the grapheme-color pairings of 6588 American synesthetes [...] "
                "6588 synesthetes provided demographic information and performed tasks online at [...] "
                "26 letters. [...] "
                "Photograph of the Fisher-Price letter set owned by a child who is now an adult synesthete with colors influenced by the toy. [...] "
                "have 10 or more matches to the magnet set in the empirical data. "
                "The probability of 10 or more matches to the magnet set for a ‘participant’ in the shuffled data was less than 0.009% across 5000 shuffles [...] "
                "though we stress that this is the source of the letter-color pairings rather than the cause of their synesthesia [...] "
                "This particular toy was only produced between 1971 and 1990"},
            wiki("Synesthesia",
                "In one common form of synesthesia, known as grapheme–color synesthesia or color–graphemic synesthesia, letters or numbers are perceived as inherently colored.",
                nome="Synesthesia"),
        ],
    },
    # 12 cantarolar para parar uma roda; cenoura diante da TV
    {
        "temas_secundarios": ["cinema_fotografia", "sentidos"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "Mastigar algo crocante, como cenoura, diante da TV pode fazer a imagem tremular: a mastigação vibra os olhos. Um cientista, em 1967, fez uma roda girando parecer parada só cantarolando.",
        "explicacao": (
            "Tudo vem do efeito roda de carroça, a ilusão em que uma roda com raios parece girar mais devagar, "
            "ficar parada ou rodar para trás. Nos faroestes do cinema e da TV, a causa é o chamado aliasing temporal: a "
            "roda só é registrada em instantes separados. O mesmo ocorre sob luz que pisca. Em 1967, Rushton viu o efeito sob luz contínua enquanto cantarolava: o "
            "zumbido faz os olhos vibrarem nas órbitas, o que cria um efeito estroboscópico dentro do próprio "
            "olho. Cantarolando numa frequência múltipla da rotação, ele fez a roda parecer parada; um pouco acima "
            "ou abaixo, ela girava devagar para um lado ou para o outro. A cenoura faz o mesmo com a TV quando a "
            "mastigação vibra os olhos num múltiplo da taxa de quadros. Mais estranho é que o efeito aparece até "
            "sob luz do sol, sem vibração nenhuma, como notou Schouten no mesmo ano. Uma hipótese diz que a visão "
            "funciona em quadros, como um filme; outra, que detectores de movimento no sentido contrário também "
            "disparam. Há evidências para as duas, mas o peso pende para a segunda."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Wagon-wheel_effect",
            "The wagon-wheel effect (alternatively called stagecoach-wheel effect) is an optical illusion in which a spoked wheel appears to rotate differently from its true rotation. "
            "The wheel can appear to rotate more slowly than the true rotation, it can appear stationary, or it can appear to rotate in the opposite direction from the true rotation (reverse rotation effect). "
            "The wagon-wheel effect is most often seen in film or television depictions of stagecoaches or wagons in Western movies [...] "
            "In these recorded media, the effect is a result of temporal aliasing. "
            "It can also commonly be seen when a rotating wheel is illuminated by flickering light. [...] "
            "Stroboscopic conditions ensure that the visibility of a rotating wheel is broken into a series of very brief episodes, interrupted by episodes of invisibility. [...] "
            "Rushton (1967) observed the wagon-wheel effect under continuous illumination while humming. "
            "The humming vibrates the eyes in their sockets, effectively creating stroboscopic conditions within the eye. "
            "By humming at a frequency of a multiple of the rotation frequency, he was able to stop the rotation. "
            "By humming at slightly higher and lower frequencies, he was able to make the rotation reverse slowly and to make the rotation go slowly in the direction of rotation. "
            "A similar stroboscopic effect is now commonly observed by people eating crunchy foods, such as carrots, while watching TV: the image appears to shimmer. "
            "The crunching vibrates the eyes at a multiple of the frame rate of the TV. [...] "
            "The first to observe the wagon-wheel effect under truly continuous illumination (such as from the sun) was Schouten (1967). [...] "
            "There are two broad theories for the wagon-wheel effect under truly continuous illumination. "
            "The first is that human visual perception takes a series of still frames of the visual scene and that movement is perceived much like a movie. "
            "The second is Schouten's theory: that moving images are processed by visual detectors sensitive to the true motion and also by detectors sensitive to opposite motion from temporal aliasing. "
            "There is evidence for both theories, but the weight of evidence favours the latter.",
            nome="Wagon-wheel effect")],
    },
    # 13 imagem parada na retina desaparece
    {
        "temas_secundarios": ["sentidos", "neurociencia"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Se uma imagem acompanhar cada movimento do olho e ficar sempre no mesmo ponto da retina, ela some em pouco tempo. A visão precisa de mudança: sem ela, até o que está bem à frente desaparece.",
        "explicacao": (
            "Os cientistas conseguem fixar uma imagem na retina de três jeitos: com um projetor minúsculo preso a "
            "uma lente de contato, que se move junto com o olho; rastreando o olhar e deslocando a imagem para "
            "compensar cada movimento; ou com a pós-imagem de um flash forte, a mancha que fica depois de uma "
            "foto. Em todos os casos, o estímulo esmaece e some após pouco tempo. É a adaptação neural, um "
            "princípio geral dos sentidos: estímulos que não variam saem da consciência. Um papelzinho pousado no "
            "antebraço deixa de ser sentido, mas volta a ser notado se o braço se mexe. Sem aparelho nenhum, dá "
            "para ver uma versão disso, o desvanecimento de Troxler, descrito pelo médico suíço Ignaz Troxler em "
            "1804: ao fixar o olhar num ponto, uma mancha fixa na visão periférica se apaga. O efeito é mais forte "
            "se ela for pequena, de pouco contraste, borrada ou distante do ponto fixado. Na periferia, os "
            "pequenos movimentos involuntários do olho não bastam para levar a imagem a células novas. Em 2006, "
            "um estudo mostrou que pelo menos parte desse apagamento acontece no cérebro, não nos olhos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Troxler's_fading",
            "When one fixates on a particular point for even a short period of time, an unchanging stimulus away from the fixation point will fade away and disappear. [...] "
            "Troxler's fading was first identified by Swiss physician Ignaz Paul Vital Troxler in 1804, who was practicing in Vienna at the time. [...] "
            "Troxler's fading has been attributed to the adaptation of neurons vital for perceiving stimuli in the visual system. "
            "It is part of the general principle in sensory systems that unvarying stimuli soon disappear from our awareness. "
            "For example, if a small piece of paper is dropped on the inside of one's forearm, it is felt for a short period of time. "
            "Soon, however, the sensation fades away. [...] "
            "But if one jiggles one's arm up and down, giving varying stimulation, one will continue to feel the paper. [...] "
            "A similar \"sensory fading\", or filling-in, can be seen of a fixated stimulus when its retinal image is made stationary on the retina (a stabilized retinal image). [...] "
            "First, one can mount a tiny projector on a contact lens. The projector shines an image into the eye. "
            "As the eye moves, the contact lens moves with it, so the image is always projected onto the same part of the retina; "
            "Second, one can monitor eye movements and move the stimulus to cancel the eye movements; "
            "Third, one can induce an afterimage, usually by an intense, brief flash, such as when one is photographed using a photographic flash [...] "
            "In all these cases, the stimulus fades away after a short time and disappears. "
            "The Troxler effect is enhanced if the stimulus is small, is of low contrast (or \"equiluminant\"), or is blurred. "
            "The effect is enhanced the further the stimulus is away from the fixation point. [...] "
            "This means that the small, involuntary eye movements made when fixating on something fail to move the stimulus onto a new cell's receptive field, in effect giving unvarying stimulation. "
            "Hsieh and Tse showed in 2006 that at least some portion of the perceptual fading occurred in the brain, not in the eyes.",
            nome="Troxler's fading")],
    },
    # 14 o efeito Kuleshov: o rosto que o público inventou
    {
        "temas_secundarios": ["cinema_fotografia", "emocoes"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "O mesmo rosto neutro de um ator, alternado com um prato de sopa, uma menina num caixão e uma mulher num divã, pareceu ao público mostrar fome, luto e desejo. Não se sabe se o filme do teste existiu.",
        "explicacao": (
            "O experimento é atribuído ao cineasta russo Lev Kuleshov, nos anos 1910 e 1920. Ele teria montado "
            "trechos de filmes antigos, com o rosto inexpressivo do astro Ivan Mozzhukhin intercalado com aquelas "
            "imagens. Segundo o relato de Vsevolod Pudovkin, de 1929, a plateia elogiou a atuação: a melancolia "
            "diante da sopa, a tristeza diante da criança morta, a cobiça diante da mulher. Mas era sempre a mesma "
            "tomada. Kuleshov e Pudovkin contaram versões diferentes da história, e não se conhece filme ou foto "
            "que tenha sobrevivido. A ideia, porém, virou base da montagem soviética e foi explicada por Alfred "
            "Hitchcock em entrevistas. A ciência demorou a testá-la. Em 1992, uma recriação com 137 pessoas não "
            "achou o efeito, mas usava um único teste por participante, sujeito a ruído. Um estudo com ressonância "
            "magnética de 2006 e outro de 2016, com 36 participantes e 24 sequências, encontraram o efeito: um "
            "rosto neutro após uma cena triste parecia triste, e após uma cena alegre, alegre. Hoje os "
            "pesquisadores concordam que o contexto muda bastante a leitura de um rosto."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Kuleshov_effect",
            "The Kuleshov effect (Russian: Эффект Кулешова) is a film editing (montage) effect demonstrated by Russian filmmaker Lev Kuleshov in the 1910s and 1920s. [...] "
            "When, where, and how Lev Kuleshov created this later cinematic research is not precisely known. "
            "He, like his collaborator Vsevolod Pudovkin, recounted differing versions, beginning soon after the work was done. "
            "No film or photo documentation is known to survive (if any edited film was ever created at all). "
            "Kuleshov edited a short film in which a shot of the expressionless face of Tsarist-era movie star Ivan Mozzhukhin (later known by the French name Ivan Mosjoukine) was alternated with various other shots (a bowl of soup, a girl in a coffin, a woman on a divan). "
            "The film was shown to an audience who believed that the expression on Mosjoukine's face was different each time he appeared, depending on whether he was \"looking at\" the bowl of soup, the girl in the coffin, or the woman on the divan, showing an expression of hunger, grief, or desire, respectively. "
            "The footage of Mosjoukine was actually the same shot each time. "
            "Vsevolod Pudovkin (who later claimed to have been the co-creator of the experiment) described in 1929 how the audience \"raved about the acting [...] "
            "the heavy pensiveness of his mood over the forgotten soup, were touched and moved by the deep sorrow with which he looked on the dead child, and noted the lust with which he observed the woman. [...] "
            "The experiment itself was created by assembling fragments of pre-existing film from the Tsarist film industry, with no new material. [...] "
            "formed the theoretical basis of Soviet montage cinema [...] "
            "Alfred Hitchcock refers to the effect in his conversations with François Truffaut [...] "
            "The Kuleshov effect has been studied by psychologists only in recent years. "
            "Prince and Hensley (1992) recreated the original study design but did not find the alleged effect. "
            "The study had 137 participants but was a single-trial between-subject experiment, which is prone to noise in the data. "
            "Dean Mobbs et al. did a within-subject fMRI study in 2006 and found an effect for negative, positive, or neutral valence. "
            "When a neutral face was shown behind a sad scene, it seemed sad; when it was shown behind a happy scene, it seemed happy. "
            "In 2016, Daniel Barratt et al. tested 36 participants using 24 film sequences across five emotional conditions [...] "
            "researchers now agree that the context in which a face is shown has a significant effect on how the face is perceived.",
            nome="Kuleshov effect")],
    },
]
