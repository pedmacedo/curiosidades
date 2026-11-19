LOTE = "2026-11-18-revolucao_industrial-01"
AREA = "historia_moderna"
TEMA = "revolucao_industrial"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 a fuligem que escureceu as mariposas
    {
        "temas_secundarios": ["evolucao", "insetos"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Na Inglaterra industrial, a fuligem escureceu os troncos e as mariposas claras viraram alvo fácil dos pássaros. Em Manchester, a forma escura, antes raríssima, chegou a 98% dos registros em 1895.",
        "explicacao": (
            "A mariposa Biston betularia costumava ter asas claras e salpicadas, que se confundiam com os liquens "
            "e a casca das árvores. A variedade escura existia, mas era rara: o primeiro exemplar vivo foi pego em "
            "Manchester em 1848. Nas primeiras décadas da Revolução Industrial, a fumaça das novas fábricas a carvão "
            "cobriu de fuligem o campo entre Londres e Manchester. O dióxido de enxofre matou muitos liquens, os "
            "troncos escureceram e as mariposas claras passaram a contrastar com a casca, enquanto as escuras "
            "ficavam camufladas. O fenômeno ganhou o nome de melanismo industrial. A ligação com a seleção natural "
            "só foi publicada em 1896, por J. W. Tutt, catorze anos depois da morte de Darwin. Entre 1953 e 1956, "
            "Bernard Kettlewell testou a ideia de que os pássaros eram o agente da seleção. O trabalho dele foi "
            "duramente criticado e chegou a ser acusado de fraude, mas um experimento de sete anos de Michael "
            "Majerus, publicado em 2012, confirmou o essencial. A história teve volta: quando leis de ar limpo "
            "reduziram a poluição, a forma clara voltou a predominar."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Peppered_moth_evolution",
            "as a consequence of air pollution during the Industrial Revolution in England in the 19th century. "
            "The frequency of dark-coloured moths increased at that time, an example of industrial melanism. "
            "Later, when pollution was reduced in response to clean air legislation, the light-coloured form again predominated. [...] "
            "It was 14 years after Darwin's death, in 1896, that J. W. Tutt presented it as a case of natural selection. [...] "
            "Bernard Kettlewell was the first to investigate the evolutionary mechanism behind peppered moth adaptation, between 1953 and 1956. [...] "
            "This selective survival was due to birds, which easily caught dark moths on clean trees and white moths on trees darkened with soot. [...] "
            "Kettlewell's story was more sternly attacked, and accused of fraud. [...] "
            "His seven-year experiment beginning in 2001, the most elaborate of its kind in population biology, the results of which were published posthumously in 2012, vindicated Kettlewell's work in great detail. [...] "
            "The first live specimen was caught by R. S. Edleston in Manchester, England in 1848 [...] "
            "The light-bodied moths were able to blend in with the light-coloured lichens and tree bark [...] "
            "During the early decades of the Industrial Revolution in England, the countryside between London and Manchester became blanketed with soot from the new coal-burning factories. "
            "Many of the light-bodied lichens died from sulphur dioxide emissions, and the trees became darkened. [...] "
            "their bodies now dramatically contrasted with the colour of the bark. "
            "Dark-coloured moths, on the other hand, were camouflaged very well by the blackened trees. [...] "
            "by 1895, the percentage of dark-coloured moths in Manchester was reported at 98% [...] "
            "The peppered moth Biston betularia",
            nome="Peppered moth evolution")],
    },
    # 2 os luditas não eram contra máquinas
    {
        "temas_secundarios": ["revolucoes_politicas", "leis_julgamentos"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Os luditas, que quebravam máquinas na Inglaterra a partir de 1811, não eram contra a tecnologia em si: muitos eram operários qualificados. Para contê-los, o governo mobilizou 12 mil soldados.",
        "explicacao": (
            "O nome vinha de \"Ned Ludd\", um aprendiz lendário que teria quebrado duas máquinas de fazer meias em "
            "1779, e servia de assinatura em cartas ameaçadoras a donos de fábricas. Os ataques miravam patrões que "
            "tentavam contornar as práticas de trabalho da época e, em cada região, um tipo de máquina. Em "
            "Yorkshire, onde as tosquiadeiras mecânicas introduzidas por Enoch Taylor deixavam sem emprego os "
            "acabadores de lã, a marreta usada nos ataques ganhou o apelido de \"Enoch\", para zombar dele. No "
            "noroeste, as cartas incluíam pedidos de salário mínimo e de fim do trabalho infantil. O historiador "
            "Malcolm Thomis argumentou que quebrar máquinas era uma das poucas táticas de pressão ao alcance dos "
            "trabalhadores, e Eric Hobsbawm chamou isso de \"negociação coletiva por meio do tumulto\". A reação foi "
            "dura. Segundo Hobsbawm, os 12 mil soldados envolvidos na repressão eram mais do que o exército que o "
            "duque de Wellington levou a Portugal em 1808. Em 1812, quebrar máquinas virou crime punível com a "
            "morte, e os julgamentos em massa de York, em 1813, terminaram com enforcamentos e degredo. Lord Byron "
            "foi uma das poucas figuras de destaque a defendê-los."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Luddite",
            "Members of the group referred to themselves as Luddites, self-described followers of \"Ned Ludd\", a legendary weaver whose name was used as a pseudonym in threatening letters to mill owners and government officials. "
            "The Luddite movement began in Nottingham, England, and spread to the North West and Yorkshire between 1811 and 1816. [...] "
            "They utilised the eponym of Ned Ludd, an apocryphal apprentice who allegedly smashed two stocking frames in 1779 [...] "
            "Malcolm I. Thomis argued in his 1970 history The Luddites that machine-breaking was one of the very few tactics that workers could use to increase pressure on employers [...] "
            "Marxist Historian Eric Hobsbawm called their machine wrecking \"collective bargaining by riot\" [...] "
            "Luddites were not opposed to the use of machines per se (many were skilled operators in the textile industry); they attacked manufacturers who were trying to circumvent standard labour practices of the time. [...] "
            "They wrecked specific types of machinery that posed a threat to the particular industrial interests in each region. [...] "
            "they were more likely to include petitions for governmental reforms, such as increased minimum wages and the cessation of child labour. [...] "
            "In Yorkshire, croppers faced mass unemployment due to the introduction of cropping machines by Enoch Taylor of Marsden. "
            "This sparked the Luddite movement among the croppers of Yorkshire, who used a hammer dubbed \"Enoch\" to break the frames of the cropping machines. "
            "They called it Enoch to mock Enoch Taylor [...] "
            "12,000 government troops, most of them belonging to militia or yeomanry units, were involved in suppression of Luddite activity, which historian Eric Hobsbawm wrote was a larger number than the army that the Duke of Wellington led into Portugal in 1808 during the Peninsular War. [...] "
            "Government officials sought to suppress the Luddite movement with a mass trial at York in January 1813 [...] "
            "The harsh sentences of those found guilty, which included execution and penal transportation, quickly ended the movement. "
            "Parliament made \"machine breaking\" (i.e. industrial sabotage) a capital crime with the Destruction of Stocking Frames, etc. Act 1812. "
            "Lord Byron opposed this legislation, becoming one of the few prominent defenders of the Luddites",
            nome="Luddite")],
    },
    # 3 a hora ferroviária e os relógios de dois ponteiros
    {
        "temas_secundarios": ["medidas_padroes", "transportes", "calendarios"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "Até o século XIX, cada cidade inglesa tinha a sua hora, e Bristol ficava dez minutos atrás de Londres. As ferrovias unificaram os relógios, e o da Bolsa de Bristol ganhou um segundo ponteiro de minutos.",
        "explicacao": (
            "Antes, cada cidade usava a sua hora local, ligada à posição do Sol, e na Grã-Bretanha a diferença "
            "para Londres chegava a vinte minutos: Oxford ficava cinco minutos atrás, Leeds seis. Nas viagens de "
            "diligência, que levavam horas ou dias, bastava acertar o relógio pelo caminho. Com os trens, esses "
            "minutos passaram a causar confusão, transtornos e até acidentes. Em novembro de 1840, a Great Western "
            "Railway adotou a hora de Londres, o primeiro caso registrado de horas locais sincronizadas numa hora "
            "padrão única. As outras companhias seguiram nos sete anos seguintes, e o telégrafo passou a levar "
            "sinais de Greenwich pelos fios ao lado dos trilhos. Muitas cidades resistiram. Em Exeter, o deão da "
            "catedral, cujo relógio era a referência da cidade, demorou a ceder. Em Bristol, o relógio da Bolsa "
            "ganhou um segundo ponteiro de minutos, e Nottingham mandou pôr três ponteiros nos relógios públicos: "
            "dois para a hora local e um para a hora de Londres. A lei só oficializou uma hora única para toda a "
            "Grã-Bretanha em 1880. Na França, os relógios dentro das estações chegaram a ser mantidos cinco "
            "minutos atrasados, para que os passageiros atrasados não perdessem o trem."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Railway_time",
            "Railway time was the standardised time arrangement first applied by the Great Western Railway in England in November 1840, the first recorded occasion when different local mean times were synchronised and a single standard time applied. [...] "
            "The railway companies sometimes faced concerted resistance from local people who refused to adjust their public clocks to bring them into line with London Time. [...] "
            "Railway time was progressively taken up by all railway companies in Great Britain over the following seven years. [...] "
            "although it took until 1880 for the government to legislate on the establishment of a single standard time and a single time zone for the country. [...] "
            "In Britain, local time differed by up to twenty minutes from that of London. "
            "For example, Oxford Time was five minutes behind Greenwich Time, Leeds Time six minutes behind [...] "
            "Before the arrival of the railways, journeys between the larger cities and towns could take many hours or days, and these differences could be dealt with by adjusting the hands of a watch periodically en route. [...] "
            "For instance, Leeds time was six minutes behind London, while Bristol was ten minutes behind [...] "
            "It soon became apparent that even such small discrepancies in times caused confusion, disruption, or even accidents. [...] "
            "By 1855 time signals from Greenwich could be sent through wires alongside the railway lines across the length and breadth of Britain. [...] "
            "in February 1846 the town council of Nottingham ordered that the town clocks be furnished with three hands, two indicating local time and the additional one the railway and post-office London time. [...] "
            "In Exeter this situation arose due to the reluctance of the Dean of Exeter Cathedral to concede to the demands of the railway company, the cathedral clock being the principal timekeeper for the city. [...] "
            "Similarly, the clock at The Bristol Exchange installed in 1822 subsequently had a second minute hand added. [...] "
            "It also required clocks inside railway stations and train schedules to be set five minutes late to allow travelers to arrive late without missing their trains",
            nome="Railway time")],
    },
    # 4 o cavalo de potência como argumento de venda
    {
        "temas_secundarios": ["medidas_padroes", "energia", "termodinamica"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "A potência em cavalos nasceu como argumento de venda. James Watt cobrava uma parte do carvão que suas máquinas a vapor poupavam, mas isso não servia para quem usava cavalos. Então ele mediu o trabalho de um cavalo.",
        "explicacao": (
            "A máquina a vapor de Watt era uma versão melhorada da de Thomas Newcomen. Com os donos das máquinas "
            "antigas, o acordo era receber um terço da economia de carvão. Mas muitos clientes não tinham máquina "
            "nenhuma: moviam tudo com cavalos, e não havia carvão poupado para dividir. A saída foi comparar a "
            "máquina com os animais que ela substituiria. Watt calculou que um cavalo girava uma roda de moinho de "
            "12 pés de raio 144 vezes por hora, puxando com uma força que ele estimou em 180 libras-força. Em 1782, "
            "verificou que um \"cavalo de cervejaria\" rendia 32.400 pés-libra por minuto, e no ano seguinte ele e "
            "Matthew Boulton fixaram o padrão em 33.000. Outros tinham chegado a valores bem diferentes: John "
            "Smeaton estimou 22.916, e John Desaguliers, 44.000. Hoje o hp imperial vale cerca de 745,7 watts, e o "
            "cavalo-vapor métrico, o cv, cerca de 735,5. E um cavalo de verdade pode passar muito disso por "
            "instantes: numa feira de 1925, mediu-se um pico de 14,88 hp por alguns segundos. Para esforço "
            "contínuo, porém, cerca de 1 hp por cavalo é o que recomendavam os manuais agrícolas dos séculos XIX "
            "e XX."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Horsepower",
            "the imperial horsepower, abbreviated hp or bhp, which is about 745.7 watts, and the metric horsepower, also represented as cv or PS, which is approximately 735.5 watts. [...] "
            "The term was adopted in the late 18th century by Scottish engineer James Watt to compare the output of steam engines with the power of draft horses. [...] "
            "The idea was later used by James Watt to help market the Watt steam engine, an improved Newcomen steam engine. "
            "He had previously agreed to take royalties of one-third of the savings in coal from the older Newcomen steam engines. "
            "This royalty scheme did not work with customers who did not have existing steam engines but used horses instead. "
            "Watt determined that a horse could turn a mill wheel 144 times in an hour (or 2.4 times a minute). "
            "The wheel was 12 feet (3.7 m) in radius [...] "
            "Watt judged that the horse could pull with a force of 180 pounds-force (800 N). [...] "
            "John Smeaton initially estimated that a horse could produce 22,916 ft⋅lb (31,070 J) per minute. "
            "John Desaguliers had previously suggested 44,000 ft⋅lb (59,700 J) per minute [...] "
            "\"Watt found by experiment in 1782 that a 'brewery horse' could produce 32,400 ft⋅lb [43,929 J] per minute.\" "
            "James Watt and Matthew Boulton standardized that figure at 33,000 ft⋅lb (44,742.0 J) per minute the next year. [...] "
            "Citing measurements made at the 1925 Iowa State Fair, they reported that the peak power over a few seconds has been measured to be as high as 14.88 hp (11.10 kW) and also observed that for sustained activity, a work rate of about 1 hp (0.75 kW) per horse is consistent with agricultural advice from both the 19th and 20th centuries",
            nome="Horsepower")],
    },
    # 5 o retrato de seda de 24 mil cartões
    {
        "temas_secundarios": ["historia_computacao", "moda", "invencoes"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "Em 1839, um retrato do inventor Jacquard foi tecido em seda por um tear guiado por cerca de 24 mil cartões perfurados. Parecia tanto uma gravura que enganava especialistas. Charles Babbage exibia uma cópia em casa.",
        "explicacao": (
            "O tear de Jacquard era controlado por uma corrente de cartões perfurados. Cada cartão correspondia a "
            "uma fileira do desenho: onde havia furo, uma haste passava e um mecanismo levantava o fio "
            "correspondente; onde havia papelão, o fio ficava no lugar. Trocar os cartões mudava o padrão, e quanto "
            "mais cartões, mais sofisticado o desenho. Como podia ser operado por uma só pessoa, o tear fazia "
            "tecidos decorados mais de 20 vezes mais rápido que os teares tradicionais. O retrato, feito pela casa "
            "Didier Petit, era tão detalhado que, segundo Babbage, dois membros da Royal Academy o tomaram por uma "
            "gravura. Ele recebia a elite britânica em casa e conta que, diante do quadro, o duque de Wellington "
            "perguntou se era uma gravura, e o príncipe Albert, que já conhecia o segredo, respondeu que não. Para "
            "Babbage, o fascínio estava no mecanismo: os cartões de Jacquard inspiraram a máquina analítica, que "
            "ele projetou para receber números e instruções da mesma forma. Ada Lovelace resumiu a ideia ao dizer "
            "que a máquina \"tece padrões algébricos\" assim como o tear de Jacquard tece flores e folhas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.sciencehistory.org/stories/magazine/the-french-connection/",
             "titulo": "The French Connection (Science History Institute, Distillations)", "idioma": "en",
             "trecho": (
                "An 1839 woven silk portrait of French textile merchant and inventor Joseph-Marie Jacquard, recently added to CHF’s collections. [...] "
                "Babbage wanted a copy to show off in his London home, where he often entertained members of the British elite. "
                "Three years later he welcomed a pair of very special guests, the Duke of Wellington and Queen Victoria’s husband, Prince Albert. [...] "
                "When we had arrived in front of the portrait, I pointed it out as the object to which I solicited the Prince’s attention. "
                "“Oh! that engraving?” remarked the Duke of Wellington. “No!” said Prince Albert to the Duke; “it is not an engraving.” "
                "The prince had seen another copy of Jacquard’s portrait, based on a painting by Claude Bonnefond, and knew its secret. "
                "As Babbage explained later, it was a “sheet of woven silk, framed and glazed, but looking so perfectly like an engraving, that it had been mistaken for such by two members of the Royal Academy.” "
                "For Babbage the portrait was much more than a fine example of textile arts: what fascinated him was the mechanism through which it was created. [...] "
                "Each card passed before an array of circular metal rods corresponding to different warp threads. "
                "Whenever a rod came into contact with solid cardboard, its associated warp thread stayed in place. "
                "If it passed through a hole, then a mechanism lifted the thread. [...] "
                "Since his new loom could be overseen by a single person, decorated fabrics could be produced more than 20 times faster than with traditional looms. "
                "Unlike drum-based systems, which were best suited for repeating patterns, there were no limits to the possible outputs of a Jacquard loom—the greater the number of cards, the greater the sophistication of the design. "
                "Didier Petit and Company used approximately 24,000 cards to produce the Jacquard portrait that had caught Babbage’s eye. [...] "
                "he set it aside to pursue a more ambitious project directly inspired by Jacquard’s handiwork. [...] "
                "Lovelace recognized that what distinguished the analytical engine from other calculating machines was the use of punch cards to supply numeric inputs and instructions [...] "
                "“We may say most aptly that the Analytical Engine weaves algebraical patterns just as the Jacquard-loom weaves flowers and leaves.”"
             )},
            wiki("Jacquard_machine",
                "The machine was controlled by a \"chain of cards\"; a number of punched cards laced together into a continuous sequence. "
                "Multiple rows of holes were punched on each card, with one complete card corresponding to one row of the design. [...] "
                "This use of replaceable punched cards to control a sequence of operations is considered an important step in the history of computing hardware, having inspired Charles Babbage's Analytical Engine.",
                nome="Jacquard machine"),
        ],
    },
    # 6 o despertador humano
    {
        "temas_secundarios": ["sono_ritmos", "cidades", "costumes_rituais"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Quando despertadores não eram baratos nem confiáveis, trabalhadores ingleses pagavam alguns centavos por semana a um \"despertador humano\", que batia na janela com uma vara comprida ou até atirava ervilhas secas.",
        "explicacao": (
            "O ofício, chamado em inglês de knocker-up, surgiu durante a Revolução Industrial na Grã-Bretanha, na "
            "Holanda, na Irlanda e em outros países, e era comum em cidades industriais grandes, como Manchester. "
            "Para as portas, usava-se um bastão curto e pesado; para as janelas dos andares de cima, uma vara longa "
            "e leve, muitas vezes de bambu. Alguns só iam embora quando tinham certeza de que o cliente acordara; "
            "outros davam umas batidas e seguiam. O serviço costumava ficar com homens idosos e mulheres grávidas, "
            "e às vezes policiais o faziam nas rondas da madrugada para reforçar o salário. E quem acordava o "
            "despertador? Muitos eram notívagos, que dormiam de dia e levantavam por volta das 4 da tarde. Em "
            "Ferryhill, cidade mineira do condado de Durham, as casas tinham lousas na parede externa, onde os "
            "mineiros escreviam a giz o horário do turno. Uma foto de 1931 mostra Mary Smith, no leste de Londres, "
            "com um tubo para soprar ervilhas, e a filha dela, Molly Moore, dizia ter sido a última a exercer a "
            "profissão. Nos anos 1940 e 1950, o ofício praticamente desapareceu, mas resistiu em alguns cantos "
            "industriais da Inglaterra até o começo dos anos 1970."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Knocker-up",
            "A knocker-up or knocker-upper had the job of rousing sleeping people so they could get to work on time. "
            "The role started during the Industrial Revolution, in Britain, the Netherlands, Ireland and some other countries, when alarm clocks were neither cheap nor reliable. "
            "By the 1940s and 1950s, the job had more or less entirely died out, although it still continued in some pockets of industrial England until the early 1970s. "
            "The knocker-up used a baton or short, heavy stick to knock on the clients' doors or a long and light stick, often made of bamboo, to reach windows on higher floors. "
            "One famous photograph shot in 1931 by John Topham shows Mary Smith in East London using a pea-shooter. "
            "In return for the task, the knocker-up would be paid a few pence a week. "
            "Some knocker-ups would not leave a client's window until they were sure that the client had been awakened, while others simply tapped several times and then moved on. "
            "Many knocker-uppers were night owls who slept during the day and woke around 4pm, thus not requiring a knocker-upper themselves. [...] "
            "There were large numbers of people carrying out the job, especially in larger industrial towns such as Manchester. "
            "Generally the job was done by elderly men and pregnant women but sometimes police constables supplemented their pay by performing the task during early morning patrols. "
            "Molly Moore (daughter of Mary Smith, also a knocker-up [...] "
            "claims to have been the last knocker-up to have been employed as such. "
            "Both Smith and Moore used a long rubber tube to shoot dried peas at their clients' windows. "
            "In Ferryhill, County Durham, miners' houses had slate boards set into their outside walls onto which the miners would write their shift details in chalk",
            nome="Knocker-up")],
    },
    # 7 o paradoxo de Jevons
    {
        "temas_secundarios": ["energia", "economia_curiosa", "mudancas_climaticas"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Em 1865, um economista inglês argumentou que máquinas a vapor mais eficientes não tinham feito o país gastar menos carvão, e sim muito mais. O efeito, chamado paradoxo de Jevons, ainda divide economistas.",
        "explicacao": (
            "William Stanley Jevons expôs a ideia no livro The Coal Question. Na época, muitos britânicos temiam "
            "que as reservas de carvão estivessem acabando depressa, e alguns especialistas confiavam que a "
            "tecnologia reduziria o consumo. Jevons disse que não. A máquina de James Watt era muito mais "
            "eficiente que a de Thomas Newcomen, e isso tornou o carvão uma fonte de força mais vantajosa. O vapor "
            "se espalhou por um grande número de indústrias, e o consumo total disparou, embora cada aplicação "
            "pedisse menos carvão. Para ele, era confusão de ideias achar que usar o combustível com economia "
            "fosse o mesmo que consumir menos. O mecanismo está no preço: quando a eficiência barateia o uso de um "
            "recurso e a demanda reage com força, o uso a mais pode superar a economia. Hoje isso é estudado como "
            "\"efeito rebote\", e há bastante debate sobre o tamanho dele e sobre o peso do paradoxo nas políticas "
            "de conservação de energia. Nem sempre ele acontece: os grandes ganhos de produtividade na agricultura "
            "baixaram o preço da comida sem fazer a demanda por alimentos crescer na mesma medida."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Jevons_paradox",
            "The Jevons paradox (pronounced , JEV-ənz) or Jevons effect is an economic phenomenon said to occur when technological improvements that increase the efficiency of a resource's use lead to a rise, rather than a fall, in total consumption of that resource. "
            "Greater efficiency reduces the amount of the resource needed per application, lowering its effective cost; if demand is sufficiently price elastic, this induces demand, frequently resulting in a net increase of total resource consumption. [...] "
            "Considerable debate exists about the size of the rebound in energy efficiency and the relevance of the Jevons paradox to energy conservation. [...] "
            "The Jevons paradox was first described by the English economist William Stanley Jevons in his 1865 book The Coal Question. "
            "Jevons observed that England's consumption of coal soared after James Watt introduced the Watt steam engine, which greatly improved the efficiency of the coal-fired steam engine from Thomas Newcomen's earlier design. "
            "Watt's innovations made coal a more cost-effective power source, leading to the increased use of the steam engine in a wide range of industries. "
            "This in turn increased total coal consumption, even as the amount of coal required for any particular application fell. "
            "Jevons argued that improvements in fuel efficiency tend to increase (rather than decrease) fuel use, writing: \"It is a confusion of ideas to suppose that the economical use of fuel is equivalent to diminished consumption. The very contrary is the truth.\" "
            "At that time, many in Britain worried that coal reserves were rapidly dwindling, but some experts opined that improving technology would reduce coal consumption. [...] "
            "This increase in demand is known as the rebound effect [...] "
            "As an example of where the paradox did not occur, large improvements in farming productivity (including the Third Agricultural Revolution) led to lower food prices but did not result in increased demand for food",
            nome="Jevons paradox")],
    },
    # 8 Rainhill: a locomotiva movida a cavalo
    {
        "temas_secundarios": ["transportes", "invencoes"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 1829, uma ferrovia inglesa fez um concurso para decidir se usaria locomotivas. Uma das concorrentes era movida por um cavalo andando numa esteira, e saiu da disputa quando o animal atravessou o piso.",
        "explicacao": (
            "A Liverpool and Manchester Railway estava quase pronta, e os diretores ainda pensavam em puxar os trens "
            "com cabos acionados por máquinas a vapor fixas. O engenheiro da linha, George Stephenson, defendia as "
            "locomotivas. Para tirar a dúvida, a companhia organizou as provas de Rainhill, em outubro de 1829, com "
            "prêmio de 500 libras. Dez máquinas foram inscritas, mas só cinco estavam prontas no primeiro dia. A "
            "Cycloped, de Thomas Shaw Brandreth, foi a primeira a sair, depois do acidente com o cavalo. A "
            "Perseverance chegou danificada pelo transporte, passou cinco dias em conserto e não atingiu as 10 "
            "milhas por hora exigidas; ganhou um prêmio de consolação de 25 libras. A Novelty, favorita do público, "
            "chegou a 28 milhas por hora no primeiro dia, mas teve um cano da caldeira danificado. A Sans Pareil "
            "rachou um cilindro. Só a Rocket completou as provas, e os Stephenson ganharam o contrato para fornecer "
            "as locomotivas da linha. Em 2002, réplicas refizeram a disputa, e as contas indicaram que a Rocket "
            "ainda venceria, por ser bem mais confiável."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Rainhill_trials",
            "The Rainhill trials were a competition run from 6 to 14 October 1829 to test George Stephenson's argument that locomotives would have the best motive power for the nearly-completed Liverpool and Manchester Railway (L&MR). "
            "Ten locomotives were entered, of which five were able to compete [...] "
            "The directors of the Liverpool and Manchester Railway had originally intended to use stationary steam engines to haul trains along the railway using cables. "
            "They had appointed George Stephenson as their engineer of the line in 1826, and he strongly advocated for the use of steam locomotives instead. [...] "
            "A prize of £500 (equal to £47,460 today) was offered to the winner of the trials. [...] "
            "Cycloped, a horse-powered locomotive built by Thomas Shaw Brandreth. [...] "
            "Cycloped was the first to drop out of the competition. "
            "It used a horse walking on a drive belt for power and was withdrawn after an accident caused the horse to burst through the floor of the engine. "
            "The next locomotive to retire was Perseverance, which was damaged in transit to the competition. "
            "Burstall spent the first five days of the trials repairing his locomotive, and though it ran on the sixth day, it failed to reach the required 10 miles per hour (16 km/h) speed and was withdrawn from the trial. "
            "It was granted a £25 consolation prize [...] "
            "It completed eight trips before cracking a cylinder. [...] "
            "It was the crowd favourite and reached a then-astonishing 28 miles per hour (45 km/h) on the first day of competition. "
            "It later suffered damage to a boiler pipe which could not be fixed properly on site. [...] "
            "The Rocket was the only locomotive that completed the trials. [...] "
            "The Stephensons were given the contract to produce locomotives for the L&MR. [...] "
            "In a 2002 restaging of the Rainhill trials using replica engines [...] "
            "it was found that Rocket would still have won, as its relatively modern technology made it a much more reliable locomotive than the others.",
            nome="Rainhill trials")],
    },
    # 9 a ponte de ferro com encaixes de carpinteiro
    {
        "temas_secundarios": ["grandes_obras", "arquitetura"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "A primeira grande ponte de ferro fundido do mundo, aberta em 1781 na Inglaterra, foi projetada como se fosse de madeira: suas peças se prendem com encaixes de carpinteiro, como espiga e cauda de andorinha.",
        "explicacao": (
            "A Iron Bridge cruza um desfiladeiro do rio Severn, em Shropshire, perto de Coalbrookdale, onde Abraham "
            "Darby I começara a fundir minério de ferro com coque em 1709. O projeto segue um desenho que os "
            "carpinteiros usavam em estruturas de madeira. Thomas Gregory, encarregado da fundição que desenhou as "
            "peças em detalhe, adotou juntas típicas de marcenaria, como a de espiga e encaixe e a de cauda de "
            "andorinha. A obra consumiu cerca de 384,6 toneladas de ferro, divididas em quase 1.700 componentes, e o "
            "arco tem 30,63 metros de vão. Nada era padronizado: cada peça foi fundida para encaixar nas vizinhas, e "
            "peças \"idênticas\" em pontos diferentes chegam a diferir em vários centímetros. A ponte passou numa "
            "prova dura em 1795, quando uma grande cheia do Severn levou todas as pontes da região, menos ela, cuja "
            "estrutura vazada deixou a água passar. O sucesso inspirou o uso do ferro fundido em muitas pontes "
            "seguintes. E a cor dela mudou: numa restauração concluída em 2018, análises indicaram que o tom "
            "original era um marrom-avermelhado, e a ponte trocou o cinza-azulado por ele."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("The_Iron_Bridge",
            "The Iron Bridge is a cast iron arch bridge that spans the Ironbridge Gorge of the River Severn in Shropshire, England. "
            "Opened in 1781, it was the first major bridge in the world to be made of cast iron. "
            "Its success inspired the widespread use of cast iron as a structural material [...] "
            "Abraham Darby I first smelted local iron ore with coke made from Coalbrookdale coal in 1709 [...] "
            "The bridge is to a carpenters' design typically used for wood structures, built from five sectional cast-iron ribs that give a span of 100 feet 6 inches (30.63 m). [...] "
            "Exactly 378 long tons 10 cwt (847,800 lb or 384.6 t) of iron was used in the construction of the bridge, and there are almost 1,700 individual components [...] "
            "Components were cast individually to fit with each other, rather than being of standard sizes, with discrepancies of up to several centimetres between 'identical' components in different locations. [...] "
            "A foreman at the foundry, Thomas Gregory, drew the detailed designs for the members, resulting in the use of carpentry jointing details such as mortise and tenon joints and dovetails. [...] "
            "In 1795, a large flood in the Severn swept away all the bridges in the vicinity, except the Iron Bridge, where the open structure allowed the floodwaters to pass through. [...] "
            "Following the works the bridge was reopened on 6 December 2018. [...] "
            "the bridge was also reverted from blue-grey to its original red-brown colour after forensic analysis revealed this was how the bridge looked when it was first erected.",
            nome="The Iron Bridge")],
    },
    # 10 a Jenny que não existiu
    {
        "temas_secundarios": ["invencoes", "palavras_viajantes"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "Conta-se que a máquina de fiar \"spinning jenny\" tem o nome de uma filha do inventor, que teria derrubado uma roca. Mas os registros da igreja mostram que ele não tinha filha nem esposa chamada Jenny.",
        "explicacao": (
            "James Hargreaves inventou a máquina por volta de 1764–1765, em Lancashire. Ela fiava vários fios ao "
            "mesmo tempo: no começo, oito fusos girados por uma única roda, número que mais tarde chegou a 120. "
            "Segundo a história mais contada, a filha ou a esposa dele, Jenny, derrubou uma roca, que continuou "
            "girando com o fuso em pé, e Hargreaves percebeu que nada obrigava os fusos a ficarem deitados. Os "
            "registros paroquiais de Church Kirk mostram que ele teve várias filhas, nenhuma chamada Jenny, e a "
            "esposa também não tinha esse nome. Uma explicação mais provável é que \"jenny\" fosse uma abreviação "
            "de \"engine\", máquina. A lenda circula até com o nome da esposa de Thomas Highs, que também se dizia "
            "o inventor. A história verdadeira teve outro tipo de drama: com a máquina, o preço do fio caiu, e os "
            "fiandeiros de Blackburn, revoltados, invadiram a casa de Hargreaves e quebraram as máquinas. Ele fugiu "
            "para Nottingham em 1768, passou a fabricá-las em segredo e as patenteou em 1770. Quando tentou "
            "processar quem usava cópias, o caso desmoronou ao se descobrir que ele próprio já tinha vendido "
            "várias."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Spinning_jenny",
            "It was invented in 1764–1765 by James Hargreaves in Stanhill, Oswaldtwistle, Lancashire in England. "
            "The device reduced the amount of work needed to produce cloth, with a worker able to work eight or more spools at once. "
            "This grew to 120 as technology advanced. [...] "
            "The idea was developed by Hargreaves as a metal frame with eight wooden spindles at one end. [...] "
            "The spinner used their right hand to rapidly turn a wheel which caused all the spindles to revolve, and the thread to be spun. [...] "
            "The price of yarn fell, angering the large spinning community in Blackburn. "
            "Eventually they broke into his house and smashed his machines, forcing him to flee to Nottingham in 1768. [...] "
            "There he set up shop producing jennies in secret for one Mr Shipley [...] "
            "On 12 July 1770, he took out a patent (no. 962) on his invention [...] "
            "but the case eventually fell apart when it was learned he had sold several in the past. [...] "
            "The most common story told about the invention of the device and the origin of the jenny in the machine's name is that one of his daughters (or his wife) named Jenny knocked over one of their own spinning wheels. "
            "The device kept working normally, with the spindle now pointed upright. "
            "Hargreaves realised there was no particular reason the spindles had to be horizontal, as they always had been, and he could place them vertically in a row. [...] "
            "The Registers of Church Kirk show that Hargreaves had several daughters, but none named Jenny (neither was his wife). "
            "A more likely explanation of the name is that jenny was an abbreviation of engine. "
            "Thomas Highs of Leigh has claimed to be the inventor and the story is repeated using his wife's name.",
            nome="Spinning jenny")],
    },
    # 11 Slater, o Traidor
    {
        "temas_secundarios": ["espionagem", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "A lei britânica proibia exportar os projetos das máquinas têxteis. Em 1789, um jovem de 21 anos decorou o que pôde, partiu para os EUA e lá reconstruiu as máquinas de memória. Em casa, virou \"Slater, o Traidor\".",
        "explicacao": (
            "Samuel Slater começou a trabalhar aos dez anos na fiação de algodão de Jedediah Strutt, em Belper, que "
            "usava a water frame, a máquina de fiar movida a água de Richard Arkwright. Depois, como aprendiz de "
            "Strutt, aprendeu a fundo a organização e a prática da fiação. Sabendo do interesse americano por "
            "máquinas assim, e da lei que proibia levar os projetos para fora, memorizou tudo o que conseguiu e "
            "embarcou para Nova York. Em Rhode Island, o industrial Moses Brown tinha comprado uma máquina \"no "
            "padrão de Arkwright\" que ninguém conseguia pôr para funcionar. Slater escreveu oferecendo seus "
            "serviços, com uma promessa: se não fizesse fio tão bom quanto o inglês, não cobraria nada e jogaria "
            "tudo da ponte. Como não havia mecânicos no país, encontrou Oziel Wilkinson e o filho David para fundir "
            "e forjar as peças de ferro, e reconstruiu de memória as máquinas movidas a água. Em 1793, ele e Brown "
            "abriram a primeira fábrica em Pawtucket, a primeira fiação hidráulica bem-sucedida dos EUA. Os "
            "primeiros empregados eram crianças de sete a 12 anos. Nos EUA, Andrew Jackson o chamou de \"pai da "
            "Revolução Industrial americana\"; em Belper, alguns viram traição à cidade que vivia das fábricas de "
            "Strutt."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Samuel_Slater",
            "was an early English-American industrialist known as the \"Father of the American Industrial Revolution\", a phrase coined by Andrew Jackson [...] "
            "In the United Kingdom, he was called \"Slater the Traitor\" and \"Sam the Slate\" because he brought British textile technology to the United States [...] "
            "He memorized the textile factory machinery designs as an apprentice to a pioneer in the British industry before migrating to the U.S. at the age of 21. [...] "
            "At age ten, he began work at the cotton mill opened that year by Jedediah Strutt using the water frame pioneered by Richard Arkwright at nearby Cromford Mill. [...] "
            "Slater was well trained by Strutt and, by age 21, he had gained a thorough knowledge of the organization and practice of cotton spinning. "
            "He learned of the American interest in developing similar machines, and he was also aware of British law against exporting the designs. "
            "He memorized as much as he could, and departed for New York City in 1789. "
            "Some people of Belper called him \"Slater the Traitor\", as they considered his move a betrayal of the town where many earned their living at Strutt's mills. [...] "
            "In August 1789, they acquired a 32-spindle frame \"after the Arkwright pattern\" but could not operate it. "
            "At this point, Slater wrote to them, offering his services. [...] "
            "He promised: \"If I do not make as good yarn, as they do in England, I will have nothing for my services but will throw the whole of what I have attempted over the bridge.\" [...] "
            "Slater found no mechanics in the U.S. when he arrived and had great difficulty finding someone to build the machinery. "
            "Eventually, he located Oziel Wilkinson and his son, David, to produce iron castings and forgings for the machinery. [...] "
            "He was able to single-handedly construct from memory the water-powered spinning machinery. [...] "
            "In 1793, Slater and Brown opened their first factory in Pawtucket. [...] "
            "The result was the first successful water-powered roller spinning textile mill in the U.S. [...] "
            "Children aged seven to 12 were the first employees of the mill",
            nome="Samuel Slater")],
    },
    # 12 os operários famintos que apoiaram Lincoln
    {
        "temas_secundarios": ["revolucoes_politicas", "comercio_rotas"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "No fim de 1862, com as fábricas de algodão do norte da Inglaterra paradas e operários na miséria, trabalhadores reunidos em Manchester declararam apoio a Lincoln contra a escravidão. Ele respondeu com uma carta.",
        "explicacao": (
            "A crise ficou conhecida como a Fome do Algodão, de 1861 a 1865, e não teve uma causa só. Os anos de "
            "1859 e 1860 tinham produzido mais tecido do que se conseguia vender, e a Guerra Civil americana "
            "interrompeu a chegada do algodão, enquanto especuladores seguravam os estoques. O preço do algodão "
            "bruto subiu várias centenas por cento, e os operários de Lancashire passaram de os mais prósperos aos "
            "mais pobres da Grã-Bretanha. Em Stalybridge, no inverno de 1862–1863, só cinco das 39 fábricas da cidade "
            "davam trabalho em tempo integral. A opinião estava longe de ser unânime: muitos donos de fábrica e "
            "operários se ressentiam do bloqueio da União, e bandeiras confederadas tremulavam em várias cidades "
            "algodoeiras. Mesmo assim, em 31 de dezembro de 1862, uma reunião de trabalhadores no Free Trade Hall, "
            "em Manchester, decidiu apoiar a União na luta contra a escravidão e escreveu a Lincoln. Em 19 de "
            "janeiro de 1863, ele agradeceu, lamentou o sofrimento deles e chamou o gesto de exemplo de \"sublime "
            "heroísmo cristão\". O governo americano mandou navios com comida para Lancashire, e um monumento em "
            "Manchester reproduz trechos das duas cartas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Lancashire_cotton_famine",
            "The Lancashire Cotton Famine, also known as the Cotton Famine or the Cotton Panic (1861–1865), was a depression in the textile industry of North West England, brought about by overproduction in a time of contracting world markets. "
            "It coincided with the interruption of baled cotton imports caused by the American Civil War and speculators buying up new stock for storage [...] "
            "The boom years of 1859 and 1860 had produced more woven cotton than could be sold [...] "
            "The price for raw cotton increased by several hundred percent due to blockade and lack of imports. [...] "
            "workers became unemployed and went from being the most prosperous workers in Britain to the most impoverished. [...] "
            "By the winter of 1862–1863 there were 7,000 unemployed operatives in Stalybridge, one of the worst affected towns. "
            "Only five of the town's 39 factories and 24 machine shops were employing people full-time. [...] "
            "Many mill owners and workers resented the blockade and continued to see the war as an issue of tariffs against free trade. [...] "
            "Confederate flags were flown in many cotton towns. "
            "On 31 December 1862, a meeting of cotton workers at the Free Trade Hall in Manchester, despite their increasing hardship, resolved to support the Union in its fight against slavery. [...] "
            "On 19 January 1863, Abraham Lincoln sent an address thanking the cotton workers of Lancashire for their support [...] "
            "I know and deeply deplore the sufferings which the workingmen at Manchester and in all Europe are called to endure in this crisis. [...] "
            "I cannot but regard your decisive utterance upon the question as an instance of sublime Christian heroism which has not been surpassed in any age or in any country. [...] "
            "A monument in Brazenose Street, Lincoln Square, Manchester, commemorates the events and reproduces portions of both documents. [...] "
            "The Federal American government sent a gift of food to the people of Lancashire.",
            nome="Lancashire cotton famine")],
    },
    # 13 a mandíbula que brilhava no escuro
    {
        "temas_secundarios": ["historia_medicina", "elementos_quimicos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "O fósforo branco dos fósforos do século XIX destruía a mandíbula de quem os fabricava, e o osso doente brilhava no escuro. Uma grande fábrica de Londres já fazia fósforos seguros, mas eles custavam mais.",
        "explicacao": (
            "A doença, chamada em inglês de phossy jaw, vinha de respirar o vapor do fósforo branco, sobretudo "
            "quando a mistura era aquecida. Começava com dor de dente e inchaço na gengiva e evoluía para perda dos "
            "dentes, abscessos e necrose do osso; a mortalidade relatada era de cerca de 20%. A Bryant & May, em "
            "Londres, conhecia o problema: quem reclamasse de dor de dente era mandado arrancar os dentes na hora, "
            "sob pena de demissão. A empresa importava da Suécia fósforos de segurança, feitos com fósforo "
            "vermelho, desde 1850, e chegou a fabricá-los a partir de 1855, mas eles não competiam em preço com os "
            "de fósforo branco. Em julho de 1888, cerca de 1.400 mulheres e meninas da fábrica de Bow cruzaram os "
            "braços depois da demissão de uma colega. Venceram: as multas e descontos injustos foram abolidos, e as "
            "refeições passaram a ser feitas numa sala separada, longe do fósforo. Em 1891, o Exército da Salvação "
            "abriu uma fábrica com fósforo vermelho, mas seus fósforos custavam de início o triplo. O fósforo "
            "branco só foi proibido de vez nos fósforos britânicos depois de 31 de dezembro de 1910, seguindo a "
            "Convenção de Berna, de 1906."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Matchgirls%27_strike",
                "In July 1888 the women and teenage girls working at the Bryant & May match factory in Bow, London, England went on strike. [...] "
                "Phossy jaw developed by inhalation of phosphorus vapour—particularly when the ingredient was heated—which caused osteonecrosis of the jaw bone. "
                "This manifested itself in, initially, toothaches and flu-like symptoms, then tooth loss, abscesses, swelling of the gums, the formation of fistula and necrosis of the jaw. "
                "Mortality was reported in around 20 per cent of cases. [...] "
                "Bryant & May were aware of phossy jaw. "
                "If a worker complained of having toothache, they were told to have the teeth removed immediately or be sacked. [...] "
                "This caused management to dismiss a worker (on some other pretext), on or about 2 July 1888, which set off the strike. "
                "Approximately 1,400 women and girls refused to work by the end of the first day after the dismissal. [...] "
                "in which fines, deductions for the cost of materials and other unfair deductions would be abolished. [...] "
                "An important additional term was that meals were to be taken in a separate room, where the food would not be contaminated with phosphorus. [...] "
                "In 1891 the Salvation Army opened up its own match factory in the Bow district of London, using less toxic red phosphorus and paying better wages. [...] "
                "The owners, Francis May and William Bryant, had started importing red-phosphorus based safety matches from John Edvard Lundström, in Sweden, in 1850. [...] "
                "They started using red phosphorus in 1855, but could not compete in price against the much cheaper white phosphorus-based matches [...] "
                "their own matches were initially three times the price of white phosphorus-based matches. [...] "
                "prohibiting the use of white phosphorus in matches after 31 December 1910. "
                "This was the United Kingdom's implementation of the 1906 Berne Convention on the prohibition of white phosphorus in matches.",
                nome="Matchgirls' strike"),
            wiki("Phossy_jaw",
                "It was caused by white phosphorus vapor, which destroys the bones of the jaw. [...] "
                "Affected bones glowed a greenish-white colour in the dark.",
                nome="Phossy jaw"),
        ],
    },
    # 14 Engels, o comunista dono de fábrica
    {
        "temas_secundarios": ["revolucoes_politicas", "economia_curiosa", "cidades"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "Friedrich Engels, coautor do Manifesto Comunista, trabalhou quase vinte anos na firma de algodão da família em Manchester, chegou a sócio e, com esse dinheiro, sustentou Karl Marx enquanto ele preparava O Capital.",
        "explicacao": (
            "Engels era o filho mais velho de um próspero dono de fiação da Prússia. Em 1842, o pai o mandou a "
            "Manchester para trabalhar no escritório de uma fábrica da Ermen & Engels, em parte para afastá-lo da "
            "política radical. Teve o efeito oposto: a cidade, símbolo da Revolução Industrial, deu a ele o "
            "material para o livro A Situação da Classe Trabalhadora na Inglaterra, de 1845. Depois das revoluções "
            "de 1848, com a família de Marx na miséria em Londres, Engels voltou à firma em 1850 para poder "
            "ajudá-los. Levou uma vida dupla. Em público, era um comerciante respeitável, membro da Bolsa e de "
            "clubes exclusivos, que caçava raposas com uma das caçadas mais aristocráticas da Inglaterra. Em "
            "segredo, vivia com a irlandesa Mary Burns, da classe operária, em bairros pobres. Em 1860 já ganhava "
            "mais de mil libras por ano, e em 1864 virou sócio. Ao longo de vinte anos, mandou aos Marx entre 3 mil "
            "e 4 mil libras, o que na prática bancou a pesquisa e a escrita de O Capital. Também serviu de fonte "
            "para o livro, com dados de dentro da indústria, como custos de máquinas, contabilidade e o "
            "funcionamento do mercado do algodão."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Friedrich_Engels",
            "They became active in the Communist League, which commissioned them to write the Manifesto. [...] "
            "In 1842, his father sent him to Manchester, England, to work in a cotton mill in which the family had an investment. "
            "His experiences of the industrial working class there led him to write his first major work, The Condition of the Working Class in England (1845). [...] "
            "Engels participated actively in the Revolutions of 1848, including in armed combat, before being forced into exile in England. "
            "From 1850, he lived in Manchester and worked for the family firm of Ermen & Engels for two decades, leading a double life as a respectable cotton merchant while providing crucial financial support to the impoverished Marx family in London. [...] "
            "He was the eldest of nine children born to Friedrich Engels Sr., a prosperous cotton mill owner [...] "
            "Engels's father sent him to Manchester to work as a clerk in the office of Ermen & Engels's Victoria Mill in Weaste, Salford. "
            "This move, intended to steer him away from radical politics, had the opposite effect. "
            "Manchester, the \"shock-city\" of the Industrial Revolution, provided Engels with the empirical evidence for the communist theories he had absorbed in Germany. [...] "
            "In November 1850, reconciling with his family, he agreed to return to Manchester and resume his position at the Ermen & Engels office to provide financial support for Marx. [...] "
            "he endured this \"purgatory\" for nearly twenty years. [...] "
            "rose through the ranks, becoming a partner in the firm in 1864. "
            "His income grew substantially, reaching over £1,000 a year by 1860 [...] "
            "Over twenty years, he sent a constant stream of funds to the Marx family in London, totalling between £3,000 and £4,000, effectively funding Marx's research and the writing of Das Kapital. [...] "
            "He maintained an official residence in respectable city suburbs while living secretly with Mary Burns, and later her sister Lizzy, in a series of modest houses in working-class districts like Chorlton and Ardwick. "
            "In his public life, Engels became a stalwart of Manchester society. "
            "He was a member of the Royal Exchange [...] "
            "and exclusive gentlemen's clubs like the Albert Club and the Brazenose Club. "
            "A passionate equestrian, he regularly rode with the Cheshire Hounds, one of the most aristocratic fox hunts in England [...] "
            "He provided detailed, real-world information on the workings of capitalist industry, from machinery costs and bookkeeping practices to the structure of the cotton market [...] "
            "the Irish working-class sisters Mary (c. 1822–1863) and Lizzy Burns",
            nome="Friedrich Engels")],
    },
]
