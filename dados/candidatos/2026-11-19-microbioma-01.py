LOTE = "2026-11-19-microbioma-01"
AREA = "corpo_medicina"
TEMA = "microbioma"
W = "https://en.wikipedia.org/wiki/"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


def epmc(pmc, titulo, trecho):
    return {"url": EPMC + pmc + "/fullTextXML", "titulo": titulo, "idioma": "en", "trecho": trecho}


CANDIDATOS = [
    # 1 o mito das 10 bactérias por célula humana
    {
        "temas_secundarios": ["microbiologia", "anatomia"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "Repete-se há décadas que temos 10 bactérias para cada célula humana. Uma recontagem cuidadosa achou cerca de 38 trilhões de bactérias e 30 trilhões de células nossas: quase um empate.",
        "explicacao": (
            "A proporção de dez para um aparece em livros e reportagens, mas, segundo os autores da recontagem, "
            "publicada em 2016 na revista PLoS Biology, as citações levam a uma única conta de guardanapo dos anos 1970. "
            "Ela multiplicava a densidade de bactérias no conteúdo do intestino por 1 litro, a capacidade do tubo "
            "digestivo inteiro, como se ele todo fosse tão povoado quanto o cólon. Só que os trechos anteriores ao "
            "cólon têm pouquíssimas bactérias em comparação. Refazendo a conta para um homem de referência de 70 kg, "
            "com um cólon de cerca de 0,4 litro, e somando as células humanas tipo a tipo, a razão ficou em torno de "
            "1,3 bactéria por célula humana, com incerteza de 25%. Do nosso lado, quem mais pesa na contagem são os "
            "glóbulos vermelhos, pequenos e numerosos: 84% das células. Já as bactérias, juntas, pesam só uns 0,2 kg. "
            "E o placar oscila: como quase todas vivem no cólon, cada evacuação reduz esse conteúdo em um quarto a "
            "um terço."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [epmc("PMC4991899",
            "Revised Estimates for the Number of Human and Bacteria Cells in the Body (Sender, Fuchs e Milo, PLoS Biology, via Europe PMC)",
            "Revised Estimates for the Number of Human and Bacteria Cells in the Body [...] "
            "Our analysis also updates the widely-cited 10:1 ratio, showing that the number of bacteria in the body is actually of the same order as the number of human cells, and their total mass is about 0.2 kg. [...] "
            "Thoroughly revised estimates show that the typical adult human body consists of about 30 trillion human cells and about 38 trillion bacteria. [...] "
            "all papers regarding the number of bacteria in the human gastrointestinal tract that gave reference to the value stated could be traced to a single back-of-the-envelope estimate [...] "
            "The primary source for the often cited value of [...] bacteria in the body dates back to the 1970s [...] "
            "and only consists of a sentence-long “derivation,” which assumes the volume of the alimentary tract to be 1 liter, and multiplies this volume by the number density of bacteria [...] "
            "Yet, the parts of the alimentary tract proximal to the colon contain a negligible number of bacteria in comparison to the colon content [...] "
            "Values for a reference adult man averaged 0.4 L [...] "
            "while each defecation event reduces the content by a quarter to a third [...] "
            "Given the dominance of bacteria in the colon over all other microbiota populations in the body, we conclude that there is about 0.2 kg of bacteria in the body overall. [...] "
            "we can give an updated estimate of B/H = 1.3, with an uncertainty of 25% and a variation of 53% over the population of standard 70 kg males. [...] "
            "The cell count is dominated by red blood cells (84%), among the smallest cell types in the human body [...] "
            "© 2016 Sender et al")],
    },
    # 2 açúcares do leite materno que o bebê não digere
    {
        "temas_secundarios": ["desenvolvimento_humano", "evolucao"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "O leite materno tem cerca de 200 tipos de açúcares complexos que o bebê não consegue digerir. Eles servem de comida para bactérias do intestino dele, sobretudo um tipo de bifidobactéria.",
        "explicacao": (
            "Esses açúcares são os oligossacarídeos do leite humano. Depois da lactose e da gordura, são o terceiro "
            "componente sólido mais abundante do leite, com 11,3 a 17,7 gramas por litro, conforme a fase da "
            "amamentação. Ao contrário dos outros componentes do leite, eles não são absorvidos pelo bebê e viram "
            "alimento para bactérias do intestino, especialmente bifidobactérias. Testes mostraram que favorecem em especial a "
            "subespécie Bifidobacterium longum infantis, que tem um conjunto de genes próprio para levar esses "
            "açúcares para dentro da célula e quebrá-los por completo. Para os pesquisadores, isso pode indicar uma "
            "evolução conjunta entre o leite e a capacidade dessas bactérias de aproveitá-lo. As bifidobactérias "
            "chegam a ser até 90% das bactérias do intestino de um bebê, e caem para cerca de 3% no adulto. Os "
            "oligossacarídeos ainda funcionam como iscas: imitam as moléculas da superfície do intestino onde certos "
            "micróbios nocivos se prendem. Esses açúcares parecem mais abundantes e variados no leite humano que no "
            "de outros animais."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Human_milk_oligosaccharide",
                "The HMO profile of human breast milk shapes the gut microbiota of the infant by selectively stimulating bifidobacteria and other bacteria. [...] "
                "In contrast to the other components of breast milk that are absorbed by the infant through breastfeeding, HMOs are indigestible for the nursing child. "
                "However, they have a prebiotic effect and serve as food for intestinal bacteria, especially bifidobacteria. [...] "
                "Researchers have discovered that HMOs mimic these glycan receptors so the pathogens bind themselves to the HMOs rather than the intestinal cells. [...] "
                "it was discovered that they are highly selective for a commensal bacteria known as Bifidobacteria longum biovar infantis. "
                "The presence of genes unique to B. infantis, including co-regulated glycosidases, and its efficiency at using HMOs as a carbon source may imply a co-evolution of HMOs and the genetic capability of select bacteria to utilize them. [...] "
                "Milk oligosaccharides seem to be more abundant in humans than in other animals and to be more complex and varied. [...] "
                "Human milk oligosaccharides (HMOs) form the third most abundant solid component (dissolved or emulsified or suspended in water) of human milk, after lactose and fat. "
                "HMOs are present in a concentration of 11.3 – 17.7 g/L [...] in human milk, depending on lactation stages. "
                "Approximately 200 structurally different human milk oligosaccharides are known",
                nome="Human milk oligosaccharide"),
            wiki("Bifidobacterium_longum",
                "B. infantis is unique in its ability to digest and consume  human milk oligosaccharides (HMOs). "
                "Unlike the other subspecies, B. infantis contains a 43-kb gene cluster, or HMO Cluster I, that encodes transport proteins and glycolyl hydrolases that allow it to transport HMOs inside the cell and break them down completely. [...] "
                "B. longum colonizes the human gastrointestinal tract, where it, along with other Bifidobacterium species, represents up to 90% of the bacteria of an infant's gastrointestinal tract. "
                "This number gradually drops to 3% in an adult's gastrointestinal tract",
                nome="Bifidobacterium longum"),
        ],
    },
    # 3 a arqueia que transforma hidrogênio em metano
    {
        "temas_secundarios": ["microbiologia", "fermentacao"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "Nem todo micróbio do intestino é bactéria. Muita gente carrega uma arqueia que consome o hidrogênio liberado pelas bactérias na fermentação e o transforma em metano, o que deixa a fermentação mais eficiente.",
        "explicacao": (
            "A espécie mais comum é a Methanobrevibacter smithii. Ela pertence às arqueias, um domínio de vida "
            "separado das bactérias. No intestino grosso, onde não há oxigênio e o trânsito é lento, as bactérias "
            "fermentam fibras e açúcares complexos e soltam hidrogênio e gás carbônico. A arqueia junta os dois e "
            "produz metano e água. Parece um detalhe, mas hidrogênio acumulado atrapalha a fermentação; ao "
            "removê-lo, a arqueia permite que se extraia mais energia dos alimentos. Por isso, ela pode influenciar "
            "quantas calorias uma pessoa tira da comida. Nem todo mundo a tem em quantidade: só cerca de metade das "
            "pessoas tem populações de arqueias metanogênicas fáceis de detectar. A variedade de espécies de "
            "arqueias no intestino é muito menor que a de bactérias. E, até 2007, não se conhecia nenhum exemplo "
            "claro de arqueia causadora de doença. Um dos caminhos para o bebê adquiri-la é a amamentação: ela já "
            "foi encontrada no leite materno."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Methanobrevibacter_smithii",
                "Methanobrevibacter smithii is the predominant methanogenic archaeon in the microbiota of the human gut. [...] "
                "It plays an important role in the efficient digestion of polysaccharides (complex sugars) by consuming the end products of bacterial fermentation (H2, CO2, acetate, and formate). "
                "M. smithii is a hydrogenotrophic methanogen  that utilizes hydrogen by combining it with carbon dioxide to form methane. "
                "The removal of hydrogen by M. smithii is thought to allow an increase in the extraction of energy from nutrients by shifting bacterial fermentation to more oxidized end products. [...] "
                "Methanobrevibacter smithii is an anaerobic archaea which enjoys colonizing the colon and rectum thanks to its anaerobic environment, optimal pH (6.5-7), and slow transit time. [...] "
                "M. smithii is found in breast milk and breast feeding is a major route of M. smithii acquisition and colonization in newborns. [...] "
                "Accumulation of hydrogen in the gut reduces the efficiency of microbial fermentation. [...] "
                "4 H2 + CO2 → CH4 + 2 H2O. [...] "
                "This influences the person's calorie harvest and body fat.",
                nome="Methanobrevibacter smithii"),
            wiki("Human_microbiome",
                "Archaea are present in the human gut, but, in contrast to the enormous variety of bacteria in this organ, the numbers of archaeal species are much more limited. "
                "The dominant group are the methanogens, particularly Methanobrevibacter smithii and Methanosphaera stadtmanae. "
                "However, colonization by methanogens is variable, and only about 50% of humans have easily detectable populations of these organisms. "
                "As of 2007, no clear examples of archaeal pathogens were known",
                nome="Human microbiome"),
            wiki("Gut_microbiota",
                "Methanobrevibacter smithii is unique because it is not a species of bacteria, but rather a member of domain Archaea, and is the most abundant methane-producing archaeal species in the human gastrointestinal microbiota.",
                nome="Gut microbiota"),
        ],
    },
    # 4 os três enterótipos e a polêmica
    {
        "temas_secundarios": ["evolucao", "comportamento_animal"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Em 2011, cientistas propuseram que o intestino de cada pessoa cai em um de três \"enterótipos\", conforme o grupo de bactérias dominante, sem relação com idade, sexo ou país. Chimpanzés têm tipos parecidos.",
        "explicacao": (
            "A proposta foi publicada na revista Nature em abril de 2011 pelo grupo de Peer Bork. No tipo 1, "
            "predominam bactérias do gênero Bacteroides. No tipo 2, elas são poucas e o gênero Prevotella é comum. "
            "No tipo 3, há muitas Ruminococcus. Segundo o estudo, a idade, o sexo, o peso e a nacionalidade não "
            "determinam o enterótipo. A dieta de longo prazo parece pesar mais: quem come muita proteína e gordura "
            "animal, como na dieta ocidental, tende a ter mais Bacteroides, e quem come mais carboidratos, "
            "sobretudo fibras, tende a ter Prevotella. Num estudo com crianças de Burkina Faso, na África, as "
            "Prevotella eram 53% das bactérias do intestino, e estavam ausentes em crianças europeias da mesma "
            "idade. Chimpanzés também têm enterótipos parecidos com os humanos, e amostras colhidas ao longo do "
            "tempo mostraram que o tipo de um mesmo chimpanzé mudava. A própria utilidade de classificar pessoas "
            "em enterótipos foi contestada depois."
        ),
        "nivel": 2, "nota_surpresa": 3, "confianca": "consenso_parcial",
        "fontes": [wiki("Enterotype",
            "An enterotype is a classification of living organisms based on the bacteriological composition of their gut microbiota. "
            "The discovery of three human enterotypes was announced in the April 2011 issue of Nature by Peer Bork and his associates. "
            "They found that enterotypes are not dictated by age, gender, body weight, or national divisions. "
            "There are indications that long-term diet influences enterotype. "
            "Type 1 is characterized by high levels of Bacteroides, type 2 has few Bacteroides but Prevotella are common, and type 3 has high levels of Ruminococcus. "
            "The value of classifying by enterotype has been challenged. "
            "In a study of gut bacteria of children in Burkina Faso (in Africa), Prevotella made up 53% of the gut bacteria, but were absent in age-matched European children. "
            "Studies also indicate that long-term diet is strongly associated with the gut microbiome composition—those who eat plenty of protein and animal fats typical of Western diet have predominantly Bacteroides bacteria, while for those who consume more carbohydrates, especially fibre, the Prevotella species dominate. "
            "Chimpanzees have enterotypes that are compositionally analogous to those found in humans. "
            "Using longitudinal samples, researchers found that the enterotype of individual chimpanzees varied over time.",
            nome="Enterotype")],
    },
    # 5 o microbioma mais diverso já medido: uma aldeia ianomâmi
    {
        "temas_secundarios": ["povos_indigenas", "amazonia", "ecologia"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "Numa aldeia ianomâmi da Venezuela, avistada de helicóptero em 2008, os moradores tinham o microbioma mais diverso já registrado num grupo humano, com bem mais variedade no intestino e na pele que americanos.",
        "explicacao": (
            "A aldeia não aparecia nos mapas e não tinha contato documentado com pessoas ocidentais. Depois de ser "
            "vista por um helicóptero do exército, ela recebeu uma missão médica em 2009, no alto Orinoco. Nessa "
            "primeira expedição, foram colhidas amostras da boca, da pele do antebraço e das fezes de 34 dos 54 "
            "moradores, com idades entre 4 e 50 anos. Os ianomâmis da aldeia viviam de caça e coleta, sem "
            "agricultura nem criação de animais. A análise, publicada em 2015 na revista Science Advances, mostrou a maior "
            "diversidade de bactérias e de funções genéticas já descrita em um grupo humano. No intestino e na pele, "
            "a diversidade era bem maior que a de moradores dos Estados Unidos; na boca, não. Na pele, apareciam "
            "bactérias do ambiente, o que combina com a exposição maior do corpo, em comparação com ocidentais que "
            "usam roupas e passam muito tempo dentro de casa. Para os autores, os resultados sugerem que a "
            "ocidentalização afeta bastante a diversidade do microbioma humano, e por isso vale estudar povos "
            "isolados antes que essa mudança chegue a eles."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [epmc("PMC4517851",
            "The microbiome of uncontacted Amerindians (Clemente et al., Science Advances, via Europe PMC)",
            "The microbiome of uncontacted Amerindians [...] "
            "We characterize the fecal, oral, and skin bacterial microbiome and resistome of members of an isolated Yanomami Amerindian village with no documented previous contact with Western people. "
            "These Yanomami harbor a microbiome with the highest diversity of bacteria and genetic functions ever reported in a human group. [...] "
            "These results suggest that westernization significantly affects human microbiome diversity [...] "
            "Our findings emphasize the need for extensive characterization of the function of the microbiome and resistome in remote nonwesternized populations before globalization of modern practices affects potentially beneficial bacteria harbored in the human body. [...] "
            "were obtained from 34 of the 54 villagers (table S1) at the time of the first medical expedition to an isolated, previously uncharted village in the High Orinoco state of Venezuela. "
            "The age of the subjects was between 4 and 50 years, as estimated by Yanomami health workers. [...] "
            "In 2008, an unmapped village was sighted by an army helicopter, and a medical mission landed there in 2009. [...] "
            "The Yanomami from the uncontacted village were hunters and gatherers, with no agriculture or domestication of livestock. [...] "
            "The microbiome of the uncontacted Amerindians exhibited the highest diversity ever reported in any human group. "
            "Diversity in feces and skin, but not in the mouth, was significantly higher in Yanomami than in U.S. subjects [...] "
            "In the highly diverse skin microbiota of the Yanomami, the presence of environmental bacterial taxa is consistent with their higher body environmental exposure in relation to westernized people who wear clothes and spend much time indoors. [...] "
            "Copyright © 2015, The Authors")],
    },
    # 6 a selva do umbigo
    {
        "temas_secundarios": ["ecologia", "anatomia"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "Ao analisar 60 umbigos, cientistas acharam 2.368 tipos de bactérias, mais que o dobro das espécies de aves da América do Norte. Nenhum tipo estava em todo mundo, e a maioria só aparecia em uma pessoa.",
        "explicacao": (
            "O estudo, publicado em 2012 na revista PLoS ONE, nasceu de um projeto de ciência cidadã nos Estados Unidos que "
            "colheu amostras de umbigo de mais de quinhentos voluntários; a análise usou os 60 primeiros. Dos 2.368 "
            "tipos, 2.188 estavam em menos de 10% das pessoas, e só oito apareciam em mais de setenta por cento delas. Esses "
            "poucos tipos frequentes, que os autores chamaram de \"oligarcas\", pegando emprestada uma ideia da "
            "ecologia de regiões tropicais, respondiam por quase metade das sequências lidas. Era possível prever "
            "quais seriam comuns numa nova amostra de pessoas, mas não quais bactérias uma pessoa específica teria. "
            "Alguns umbigos eram mais de três vezes mais diversos que outros. A contagem ainda é conservadora: cada "
            "tipo provavelmente reúne várias espécies, e as curvas de amostragem não se estabilizaram, sinal de que "
            "mais gente revelaria mais tipos. Houve também três tipos de arqueias, um grupo de micróbios que ainda "
            "não tinha sido registrado na pele humana. Dois deles vieram de um voluntário que disse não tomar banho "
            "havia vários anos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [epmc("PMC3492386",
            "A Jungle in There: Bacteria in Belly Buttons are Highly Diverse, but Predictable (Hulcr et al., PLoS ONE, via Europe PMC)",
            "Bacteria in Belly Buttons are Highly Diverse, but Predictable [...] "
            "sampled within a nation-wide citizen science project. [...] "
            "We then tested the oligarchy hypothesis borrowed from tropical macroecology, namely that the frequency of phylotypes in one sample of humans predicts its frequency in another independent sample. [...] "
            "we compared newly collected samples of skin bacteria and archaea from two independent samples of North Americans. [...] "
            "Although it remains difficult to predict which species of bacteria might be found on a particular human, predicting which species are most frequent (or rare) seems more straightforward [...] "
            "Over the past six months, we have sampled over five hundred volunteers for belly button bacteria. "
            "We focus on the first two subsamples (60 individuals in total) [...] "
            "In the 60 samples of belly buttons considered here, we found 2368 phylotypes of bacteria based on 144,403 sequence reads [...] "
            "These phylotypes likely correspond to far more than 2368 biological species. [...] "
            "the overall rarefaction curves for belly button bacterial phylotypes failed to level off, suggesting additional phylotypes would have been encountered were more individuals sampled [...] "
            "our diversity of bacterial phylotypes was more than twice as great as the species diversity of, for example, North American birds [...] "
            "Of 2368 total phylotypes, 2188 were present on less than 10% of individuals sampled [...] and most of those were present on just one individual. "
            "Conversely, no phylotypes were present on all individuals sampled and just eight phylotypes were present on more than seventy percent of individuals. "
            "These eight phylotypes accounted for nearly half (45%) of the total reads of bacteria in our study. [...] "
            "Of special note are three phylotypes of Archaea, a domain of life often found in extreme environments and not previously reported from human skin [...] "
            "Two of these three phylotypes were from an individual who self-reported not having showered or bathed for several years. [...] "
            "some belly buttons appear more than three times as diverse as others. [...] "
            "© 2012 Hulcr et al")],
    },
    # 7 o tártaro dos neandertais e o amido
    {
        "temas_secundarios": ["pre_historia", "evolucao"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "O tártaro dos dentes guarda DNA de bactérias por milênios. No de neandertais, de até 100 mil anos atrás, cientistas acharam micróbios da boca muito parecidos com os nossos, e diferentes dos de chimpanzés.",
        "explicacao": (
            "Tártaro é placa bacteriana endurecida: minerais da saliva se depositam sobre ela e matam as bactérias, "
            "que ficam presas na pedra. Por isso, em dentes antigos, ele conserva DNA, proteínas e partículas que "
            "revelam o microbioma da boca e pistas da dieta. Um estudo publicado em 2021 na revista PNAS analisou "
            "124 amostras de placa e tártaro de neandertais, humanos antigos e atuais, chimpanzés, gorilas e "
            "bugios. Um núcleo de bactérias que estruturam a placa foi mantido ao longo da evolução e é partilhado "
            "até com os bugios, macacos do Novo Mundo, o que sugere que elas já viviam na boca antes da separação "
            "entre esses grupos de primatas, há cerca de 40 milhões de anos. Já entre o gênero Homo e os chimpanzés, "
            "as diferenças são grandes. Uma delas: estreptococos da nossa boca capturam a amilase da saliva, a "
            "enzima que digere amido, e a usam para se alimentar. Os autores veem nisso um sinal de dietas ricas em "
            "amido desde cedo na evolução humana. Essa interpretação foi contestada numa carta à mesma revista, e os "
            "autores responderam."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            epmc("PMC8157933",
                "The evolution and changing ecology of the African hominid oral microbiome (Fellows Yates et al., PNAS, via Europe PMC)",
                "Human oral microbiome cannot predict Pleistocene starch dietary level, and dietary glucose consumption is not essential for brain growth [...] "
                "Reply to Ben-Dor et al.: Oral bacteria of Neanderthals and modern humans exhibit evidence of starch adaptation [...] "
                "The evolution and changing ecology of the African hominid oral microbiome [...] "
                "we analyzed 124 dental biofilm metagenomes from humans, including Neanderthals and Late Pleistocene to present-day modern humans, chimpanzees, and gorillas, as well as New World howler monkeys for comparison. "
                "We find that a core microbiome of primarily biofilm structural taxa has been maintained throughout African hominid evolution, and these microbial groups are also shared with howler monkeys, suggesting that they have been important oral members since before the catarrhine–platyrrhine split ca. 40 Mya. [...] "
                "the dental biofilms of [...] and chimpanzees are distinguished by major taxonomic and functional differences. "
                "Reconstructing oral metagenomes from up to 100 thousand years ago, we show that the microbial profiles of both Neanderthals and modern humans are highly similar [...] "
                "We find that amylase binding is an apparent [...] specific trait, suggestive of microbial coadaptation to starch-rich diets early in human evolution. [...] "
                "The Mitis, Sanguinis, and Salivarius groups are notable for their ability to express amylase-binding proteins to capture salivary ɑ-amylase [...] "
                "which they use for their own nutrient acquisition from dietary starch, as well as dental adhesion [...] "
                "Copyright © 2021 the Author(s). Published by PNAS."),
            wiki("Dental_calculus",
                "dental calculus or tartar is a form of hardened dental plaque. "
                "It is caused by precipitation of minerals from saliva and gingival crevicular fluid (GCF) in plaque on the teeth. "
                "This process of precipitation kills the bacterial cells within dental plaque [...] "
                "Dental calculus has been shown to contain well preserved microparticles, DNA and protein in archaeological samples. "
                "The information these molecules contain can reveal information about the oral microbiome of the host and the presence of pathogens. "
                "It is also possible to identify dietary sources as well as study dietary shifts",
                nome="Dental calculus"),
        ],
    },
    # 8 a placenta não tem microbioma: era contaminação
    {
        "temas_secundarios": ["desenvolvimento_humano", "historia_medicina"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Em 2014, um estudo anunciou que a placenta tinha um microbioma próprio. Um estudo de 2019 com 537 placentas não achou nenhum: quase todo o DNA de bactéria vinha do parto ou de reagentes de laboratório contaminados.",
        "explicacao": (
            "Por mais de um século, prevaleceu a ideia de que o feto se desenvolve num ambiente estéril e só ganha "
            "seus micróbios no parto e depois dele. Já em 1885, Theodor Escherich descreveu o mecônio, as primeiras "
            "fezes do bebê, como livre de bactérias vivas. Técnicas de sequenciamento de DNA, porém, passaram a "
            "detectar sinais de bactérias na placenta, no líquido amniótico e no mecônio, e o estudo de 2014, na "
            "revista Science Translational Medicine, falou num microbioma placentário único. O problema é que essas "
            "amostras têm pouquíssimo material, e quanto menos DNA bacteriano há numa amostra, maior a fatia que vem "
            "de contaminação. Uma revisão de 2017 notou que cerca de 36% das espécies listadas em 2014 coincidiam "
            "com bactérias conhecidas por aparecer em reagentes e materiais de laboratório. Em 2019, na revista "
            "Nature, pesquisadores analisaram placentas de 537 mulheres com vários métodos e kits diferentes, e "
            "concluíram que a placenta humana não tem microbioma. A exceção foi uma bactéria que pode causar infecção "
            "grave em recém-nascidos, achada em cerca de 5% das amostras colhidas antes do trabalho de parto. Outro argumento forte: dá para obter animais "
            "totalmente livres de micróbios por cesárea feita em condições estéreis, o que seria improvável se o "
            "feto já fosse colonizado no útero."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            epmc("PMC6697540",
                "Human placenta has no microbiome but can harbour potential pathogens (de Goffau et al., Nature, 2019, via Europe PMC)",
                "Human placenta has no microbiome but can harbour potential pathogens [...] "
                "Here we show that there was no evidence for the presence of bacteria in the large majority of placental samples, from both complicated and uncomplicated pregnancies. "
                "Almost all signals were related either to acquisition of bacteria during labour and delivery or contamination of laboratory reagents with bacterial DNA. "
                "The exception was [...] (Group B Streptococcus), where non-contaminant signals were detected in ~5% of samples collected prior to the onset of labour. [...] "
                "the human placenta does not have a microbiome, but it does represent a potential site of perinatal acquisition of [...] a major cause of neonatal sepsis. [...] "
                "We studied placental biopsies from a total of 537 women, including 318 cases of adverse pregnancy outcome and 219 controls using multiple methods of DNA extraction and detection [...] "
                "All these samples were analysed twice using 16S rRNA gene amplicon sequencing from DNA extracted by two different kits."),
            epmc("PMC5410102",
                "A critical assessment of the \"sterile womb\" and \"in utero colonization\" hypotheses (Perez-Muñoz et al., Microbiome, via Europe PMC)",
                "After more than a century of active research, the notion that the human fetal environment is sterile and that the neonate’s microbiome is acquired during and after birth was an accepted dogma. "
                "However, recent studies using molecular techniques suggest bacterial communities in the placenta, amniotic fluid, and meconium from healthy pregnancies. [...] "
                "lacked appropriate controls for contamination [...] "
                "Most importantly, the ability to reliably derive axenic animals via cesarean sections strongly supports sterility of the fetal environment in mammals. [...] "
                "As early as 1885, Theodor Escherich described the meconium (the earliest stool from an infant) to be free of viable bacteria [...] "
                "the lower the amount of bacterial DNA in a sample, the higher the proportion of sequences that can be attributed to contamination. "
                "The authors provided a list of bacterial taxa commonly present in reagents and consumables that are detected in negative controls [...] "
                "Interestingly, around 36% of the total species reported by Aagaard and colleagues [...] as “the placenta microbiome” overlap with taxa on this list. [...] "
                "The placenta harbors a unique microbiome. Sci Transl Med. 2014 [...] "
                "© The Author(s). 2017"),
        ],
    },
    # 9 genes de bactéria marinha no intestino de japoneses
    {
        "temas_secundarios": ["genetica", "vida_marinha"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "Bactérias do intestino de japoneses digerem um açúcar da alga nori que o corpo humano não quebra. Os genes para isso vieram de uma bactéria marinha que vive nessas algas, e o caminho provável foi a comida.",
        "explicacao": (
            "O genoma humano não tem as enzimas para quebrar muitos carboidratos complexos; quem faz esse serviço "
            "são micróbios do intestino. A maioria dessas enzimas lida com plantas terrestres, que dominaram a dieta "
            "humana ao longo da evolução. Num estudo publicado em 2010 na revista Nature, pesquisadores "
            "descreveram as primeiras porfiranases, enzimas que digerem a porfirana, açúcar da parede das algas "
            "vermelhas do gênero Porphyra, a nori. Elas vinham de Zobellia galactanivorans, uma bactéria isolada da "
            "superfície de algas vermelhas na costa da França. Em seguida, acharam genes desse tipo na bactéria "
            "intestinal Bacteroides plebeius, isolada de japoneses. Ao comparar amostras do intestino, as "
            "porfiranases eram frequentes na população japonesa e ausentes nos dados de norte-americanos. Os genes "
            "parecem ter passado de uma bactéria para a outra por transferência horizontal: estão na mesma ordem nos "
            "dois cromossomos e, até 2010, não apareciam em outras espécies do mesmo gênero. No Japão, cada pessoa come "
            "em média 14,2 gramas de algas por dia. Para os autores, algas com bactérias marinhas, comidas sem "
            "esterilização, devem ter sido a ponte."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": EPMC + "search?query=EXT_ID:20376150%20AND%20SRC:MED&resultType=core&format=json",
             "titulo": "Transfer of carbohydrate-active enzymes from marine bacteria to Japanese gut microbiota (Hehemann et al., Nature, 2010, resumo via Europe PMC)",
             "idioma": "en",
             "trecho": "Transfer of carbohydrate-active enzymes from marine bacteria to Japanese gut microbiota. [...] "
                "Université Pierre et Marie Curie, Paris, France. [...] "
                "Gut microbes supply the human body with energy from dietary polysaccharides through carbohydrate active enzymes, or CAZymes, which are absent in the human genome. "
                "These enzymes target polysaccharides from terrestrial plants that dominated diet throughout human evolution. [...] "
                "Here we characterize the first porphyranases from a member of the marine Bacteroidetes, Zobellia galactanivorans, active on the sulphated polysaccharide porphyran from marine red algae of the genus Porphyra. "
                "Furthermore, we show that genes coding for these porphyranases, agarases and associated proteins have been transferred to the gut bacterium Bacteroides plebeius isolated from Japanese individuals. "
                "Our comparative gut metagenome analyses show that porphyranases and agarases are frequent in the Japanese population and that they are absent in metagenome data from North American individuals. "
                "Seaweeds make an important contribution to the daily diet in Japan (14.2 g per person per day), and Porphyra spp. (nori) is the most important nutritional seaweed, traditionally used to prepare sushi. "
                "This indicates that seaweeds with associated marine bacteria may have been the route by which these novel CAZymes were acquired in human gut bacteria, and that contact with non-sterile food may be a general factor in CAZyme diversity in human gut microbes."},
            wiki("Zobellia_galactanivorans",
                "Zobellia galactanivorans is a species of gram-negative marine bacterium isolated from the surface of red algae of the coast of France.",
                nome="Zobellia galactanivorans"),
            wiki("Bacteroides_plebeius",
                "It is able to digest porphyran, a polysacchide from Porphyra seaweed (nori) that humans cannot digest on their own. [...] "
                "In total, 11 genes are believed to have been transferred: they do not occur in other Phocaeicola species (known as of 2010) and have sequence similarity of 48%-69% compared to orthologs in Z. galactanivorans. "
                "Moreover, transferred genes in both species are located in similar orders along their chromosome (i.e. they are syntenic).",
                nome="Phocaeicola plebeius (Bacteroides plebeius)"),
        ],
    },
    # 10 parto normal x cesárea: os primeiros micróbios
    {
        "temas_secundarios": ["desenvolvimento_humano", "anatomia"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "Logo após nascer, bebês de parto normal carregam bactérias parecidas com as da vagina da mãe; os de cesárea, bactérias típicas da pele. E, de início, pele, boca e nariz do bebê têm a mesma comunidade.",
        "explicacao": (
            "No parto, o bebê é exposto pela primeira vez a uma enorme variedade de micróbios, incluindo os da mãe. "
            "Para ver como isso começa, um estudo publicado em 2010 na revista PNAS sequenciou bactérias de mães e "
            "recém-nascidos: quatro bebês nascidos de parto normal e seis de cesárea. As mães tiveram pele, boca e "
            "vagina amostradas uma hora antes do parto. Nos bebês, a pele, a boca e a secreção do nariz e da "
            "garganta foram amostradas minutos depois do nascimento, e o mecônio, as primeiras fezes, no primeiro "
            "dia. Nas mães, cada parte do corpo tinha uma comunidade bem diferente. Nos recém-nascidos, ao "
            "contrário, a comunidade era praticamente a mesma em todos os lugares, qualquer que fosse o tipo de "
            "parto. O que mudava era a origem. Os bebês de parto normal tinham comunidades parecidas com as da "
            "vagina da própria mãe, dominadas por Lactobacillus, Prevotella ou Sneathia. Os de cesárea tinham "
            "comunidades parecidas com as da superfície da pele, com Staphylococcus, Corynebacterium e "
            "Propionibacterium. Com tão poucos bebês, o estudo serve como ponto de partida para acompanhar como o "
            "microbioma de cada parte do corpo se diferencia depois."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [{"url": EPMC + "search?query=EXT_ID:20566857%20AND%20SRC:MED&resultType=core&format=json",
            "titulo": "Delivery mode shapes the acquisition and structure of the initial microbiota across multiple body habitats in newborns (Dominguez-Bello et al., PNAS, 2010, resumo via Europe PMC)",
            "idioma": "en",
            "trecho": "Delivery mode shapes the acquisition and structure of the initial microbiota across multiple body habitats in newborns. [...] "
                "Upon delivery, the neonate is exposed for the first time to a wide array of microbes from a variety of sources, including maternal bacteria. [...] "
                "We used multiplexed 16S rRNA gene pyrosequencing to characterize bacterial communities from mothers and their newborn babies, four born vaginally and six born via Cesarean section. "
                "Mothers' skin, oral mucosa, and vagina were sampled 1 h before delivery, and neonates' skin, oral mucosa, and nasopharyngeal aspirate were sampled [...] 5 min, and meconium [...] 24 h, after delivery. "
                "We found that in direct contrast to the highly differentiated communities of their mothers, neonates harbored bacterial communities that were undifferentiated across multiple body habitats, regardless of delivery mode. "
                "Our results also show that vaginally delivered infants acquired bacterial communities resembling their own mother's vaginal microbiota, dominated by Lactobacillus, Prevotella, or Sneathia spp., and C-section infants harbored bacterial communities similar to those found on the skin surface, dominated by Staphylococcus, Corynebacterium, and Propionibacterium spp. "
                "These findings establish an important baseline for studies tracking the human microbiome's successional development in different body habitats following different delivery modes"}],
    },
    # 11 camundongos sem germes engordam ao ganhar micróbios
    {
        "temas_secundarios": ["microbiologia", "genetica"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Camundongos adultos criados sem nenhum micróbio, ao receber bactérias do intestino de camundongos comuns, ganharam 60% mais gordura corporal em 14 dias, mesmo passando a comer menos.",
        "explicacao": (
            "Os animais livres de germes são criados em isoladores estéreis, com comida e água esterilizadas, e "
            "servem justamente para testar o que os micróbios causam. No experimento, publicado em 2004 na revista "
            "PNAS, os camundongos receberam a microbiota do ceco, um trecho do "
            "intestino, de animais criados normalmente. Além da gordura, eles passaram a ter resistência à insulina. "
            "Os pesquisadores investigaram o porquê. As bactérias aumentam a absorção de açúcares simples pelo "
            "intestino, e o fígado passa a transformar esse excesso em gordura. Além disso, a microbiota desliga, "
            "na parede do intestino, a produção de uma proteína chamada Fiaf, que freia uma enzima responsável por "
            "guardar gordura nas células adiposas. Comparando camundongos normais e sem o gene da Fiaf, eles mostraram "
            "que desligá-la é essencial para a gordura se acumular. A conclusão dos autores é que a microbiota "
            "intestinal é um fator ambiental que influencia quanta energia o corpo extrai da dieta e quanto armazena. "
            "Sem micróbios, os camundongos têm também falhas no sistema imune."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": EPMC + "search?query=EXT_ID:15505215%20AND%20SRC:MED&resultType=core&format=json",
             "titulo": "The gut microbiota as an environmental factor that regulates fat storage (Bäckhed et al., PNAS, 2004, resumo via Europe PMC)",
             "idioma": "en",
             "trecho": "The gut microbiota as an environmental factor that regulates fat storage. [...] "
                "The gut microbial community (microbiota) is essential for processing dietary polysaccharides. "
                "We found that conventionalization of adult germ-free (GF) C57BL/6 mice with a normal microbiota harvested from the distal intestine (cecum) of conventionally raised animals produces a 60% increase in body fat content and insulin resistance within 14 days despite reduced food intake. "
                "Studies of GF and conventionalized mice revealed that the microbiota promotes absorption of monosaccharides from the gut lumen, with resulting induction of de novo hepatic lipogenesis. "
                "Fasting-induced adipocyte factor (Fiaf), a member of the angiopoietin-like family of proteins, is selectively suppressed in the intestinal epithelium of normal mice by conventionalization. "
                "Analysis of GF and conventionalized, normal and Fiaf knockout mice established that Fiaf is a circulating lipoprotein lipase inhibitor and that its suppression is essential for the microbiota-induced deposition of triglycerides in adipocytes. [...] "
                "Our findings suggest that the gut microbiota is an important environmental factor that affects energy harvest from the diet and energy storage in the host."},
            wiki("Germ-free_animal",
                "Germ-free organisms are multi-cellular organisms that have no microorganisms living in or on them. [...] "
                "Typically for experiments, each mouse is housed separately in a sterile isolator to prevent cross-contamination between mice. "
                "The mice are provided with sterilized food and water to prevent contamination. [...] "
                "Germ-free mice have been shown to have defects in their immune system and energy uptake due to lacking a healthy microbiome. [...] "
                "Germ-free animals are routinely used to establish causality in studies of the microbiome.",
                nome="Germ-free animal"),
        ],
    },
    # 12 o microbioma dos hadzas muda com as estações
    {
        "temas_secundarios": ["ecologia", "costumes_rituais"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "O microbioma dos hadzas, caçadores-coletores da Tanzânia, segue um ciclo anual: algumas bactérias ficam indetectáveis numa estação e reaparecem em outra. As que mais oscilam rareiam nos países industrializados.",
        "explicacao": (
            "Os hadzas vivem tradicionalmente em acampamentos de 20 a 30 pessoas e se alimentam sobretudo de mel, tubérculos, frutas "
            "e, especialmente na estação seca, carne. Em 2015, eram de 1.200 a 1.300 pessoas, e só cerca de um terço "
            "ainda vivia exclusivamente da coleta e da caça. Num estudo publicado em 2017 na revista Science, "
            "pesquisadores analisaram 350 amostras de fezes colhidas ao longo de mais de um ano. O resultado foi uma "
            "reconfiguração cíclica do microbioma, que se repete a cada ano: certos grupos de bactérias deixavam de "
            "ser detectados numa estação e voltavam numa estação seguinte. Depois, os dados foram comparados com os "
            "de 18 populações de 16 países, com modos de vida variados. A composição do intestino acompanhava o grau "
            "de modernização. Mais curioso: as bactérias que mais oscilavam entre as estações nos hadzas eram "
            "justamente as que separavam populações industrializadas das tradicionais. Para os autores, isso indica "
            "que algumas linhagens dinâmicas de micróbios ficaram menos comuns e menos abundantes nas populações "
            "modernizadas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": EPMC + "search?query=EXT_ID:28839072%20AND%20SRC:MED&resultType=core&format=json",
             "titulo": "Seasonal cycling in the gut microbiome of the Hadza hunter-gatherers of Tanzania (Smits et al., Science, 2017, resumo via Europe PMC)",
             "idioma": "en",
             "trecho": "Seasonal cycling in the gut microbiome of the Hadza hunter-gatherers of Tanzania. [...] "
                "Here, we examine the microbiome profile of 350 stool samples collected longitudinally for more than a year from the Hadza hunter-gatherers of Tanzania. "
                "The data reveal annual cyclic reconfiguration of the microbiome, in which some taxa become undetectable only to reappear in a subsequent season. "
                "Comparison of the Hadza data set with data collected from 18 populations in 16 countries with varying lifestyles reveals that gut community membership corresponds to modernization: "
                "Notably, the taxa within the Hadza that are the most seasonally volatile similarly differentiate industrialized and traditional populations. "
                "These data indicate that some dynamic lineages of microbes have decreased in prevalence and abundance in modernized populations."},
            wiki("Hadza_people",
                "Hadza people traditionally live in bands or 'camps' of around 20-30 people [...] "
                "Traditionally, they primarily forage for food, eating mostly honey, tubers, fruit, and, especially in the dry season, meat. "
                "In 2015, there were between 1,200 and 1,300 Hadza people living in Tanzania. "
                "Only around a third of the remaining Hadza still survive exclusively by traditional foraging.",
                nome="Hadza people"),
        ],
    },
    # 13 bactérias que se dividiram junto com os hominídeos
    {
        "temas_secundarios": ["evolucao", "genetica"],
        "tipos_espanto": ["conexao_inesperada", "escala_absurda"],
        "gancho": "Algumas linhagens de bactérias do nosso intestino evoluíram junto com os hominídeos: quando humanos, chimpanzés e gorilas se separaram, elas se separaram também, e cada ramo ficou com o seu hospedeiro.",
        "explicacao": (
            "A origem das bactérias que povoam o intestino humano era desconhecida. Um estudo publicado em 2016 na "
            "revista Science comparou linhagens de bactérias do intestino de humanos, chimpanzés, bonobos e gorilas. "
            "Ele concluiu que várias linhagens dos grupos predominantes surgiram por coespeciação, ou seja, se "
            "dividiram em espécies junto com os hospedeiros, ao longo dos últimos 15 milhões de anos. Ramos das "
            "famílias Bacteroidaceae e Bifidobacteriaceae ficaram restritos a uma única linhagem de hospedeiro por "
            "centenas de milhares de gerações. E as datas em que essas bactérias se separaram coincidem com as datas "
            "de separação dos próprios hominídeos. Na prática, o nosso genoma, o das mitocôndrias e o de parte das "
            "bactérias do intestino se diversificaram em conjunto. Parte do microbioma humano, portanto, descende de "
            "simbiontes antigos que se tornaram espécies diferentes ao mesmo tempo que os humanos e os grandes "
            "macacos africanos. Desde a separação dos chimpanzés, no entanto, a microbiota humana perdeu "
            "diversidade e mudou de composição."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": EPMC + "search?query=EXT_ID:27463672%20AND%20SRC:MED&resultType=core&format=json",
             "titulo": "Cospeciation of gut microbiota with hominids (Moeller et al., Science, 2016, resumo via Europe PMC)",
             "idioma": "en",
             "trecho": "Cospeciation of gut microbiota with hominids. [...] "
                "The evolutionary origins of the bacterial lineages that populate the human gut are unknown. "
                "Here we show that multiple lineages of the predominant bacterial taxa in the gut arose via cospeciation with humans, chimpanzees, bonobos, and gorillas over the past 15 million years. "
                "Analyses of strain-level bacterial diversity within hominid gut microbiomes revealed that clades of Bacteroidaceae and Bifidobacteriaceae have been maintained exclusively within host lineages across hundreds of thousands of host generations. "
                "Divergence times of these cospeciating gut bacteria are congruent with those of hominids, indicating that nuclear, mitochondrial, and gut bacterial genomes diversified in concert during hominid evolution. "
                "This study identifies human gut bacteria descended from ancient symbionts that speciated simultaneously with humans and the African apes."},
            wiki("Gut_microbiota",
                "humans' gut biota has decreased in diversity and changed in composition since our evolutionary split from Pan.",
                nome="Gut microbiota"),
        ],
    },
    # 14 as bactérias da pele como impressão digital
    {
        "temas_secundarios": ["leis_julgamentos", "anatomia"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "As bactérias que sua pele deixa num teclado ou num mouse funcionam como assinatura. Em 2010, cientistas distinguiram objetos tocados por pessoas diferentes, mesmo após duas semanas, e os ligaram a seus donos.",
        "explicacao": (
            "A ideia nasceu de uma descoberta anterior: a pele abriga muito mais tipos de bactérias do que se "
            "pensava, e a combinação varia bastante de uma pessoa para outra. Antes, a identificação dependia de "
            "cultivar as bactérias em laboratório, e muitas não cresciam; com a leitura direta de um gene, o 16S, "
            "a estimativa de variedade mudou radicalmente. As regiões em que as pessoas menos se parecem são, por "
            "exemplo, os espaços entre os dedos das mãos e dos pés e as axilas. Partindo disso, uma equipe "
            "testou se as bactérias deixadas em objetos poderiam apontar quem os tocou. Elas "
            "foram recuperadas até de teclas individuais e de mouses, e a comunidade de cada objeto bastou para "
            "distinguir objetos manuseados por pessoas diferentes, mesmo após até 2 semanas em temperatura "
            "ambiente. Comparando o objeto com a pele das pessoas, deu para apontar o dono com alto grau de "
            "certeza. Os autores, no estudo publicado na revista PNAS, avisam que é preciso mais trabalho antes do "
            "uso forense, mas o método poderia um dia servir para conferir provas obtidas pelos meios tradicionais."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": EPMC + "search?query=EXT_ID:20231444%20AND%20SRC:MED&resultType=core&format=json",
             "titulo": "Forensic identification using skin bacterial communities (Fierer et al., PNAS, 2010, resumo via Europe PMC)",
             "idioma": "en",
             "trecho": "Forensic identification using skin bacterial communities. [...] "
                "Fierer N, Lauber CL, Zhou N, McDonald D, Costello EK, Knight R. [...] "
                "Recent work has demonstrated that the diversity of skin-associated bacterial communities is far higher than previously recognized, with a high degree of interindividual variability in the composition of bacterial communities. "
                "Given that skin bacterial communities are personalized, we hypothesized that we could use the residual skin bacteria left on objects for forensic identification, matching the bacteria on the object to the skin-associated bacteria of the individual who touched the object. [...] "
                "We show that skin-associated bacteria can be readily recovered from surfaces (including single computer keys and computer mice) and that the structure of these communities can be used to differentiate objects handled by different individuals, even if those objects have been left untouched for up to 2 weeks at room temperature. [...] "
                "to quantitatively compare the bacterial communities on objects and skin to match the object to the individual with a high degree of certainty. "
                "Although additional work is needed to further establish the utility of this approach, this series of studies introduces a forensics approach that could eventually be used to independently evaluate results obtained using more traditional forensic practices."},
            wiki("Skin_flora",
                "The estimate of the number of bacteria species present on skin has been radically changed by the use of 16S ribosomal RNA to identify bacterial species present on skin samples direct from their genetic material. "
                "Previously such identification had depended upon microbiological culture upon which many varieties of bacteria did not grow and so were hidden to science. [...] "
                "The areas with least similarity between people in species were the spaces between fingers, the spaces between toes, axillae, and umbilical cord stump.",
                nome="Skin flora"),
        ],
    },
]
