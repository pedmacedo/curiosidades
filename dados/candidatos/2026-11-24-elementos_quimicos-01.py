LOTE = "2026-11-24-elementos_quimicos-01"
AREA = "fisica_quimica"
TEMA = "elementos_quimicos"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Ytterby, a aldeia que batizou quatro elementos
    {
        "temas_secundarios": ["minerais_rochas", "nomes_lugares"],
        "tipos_espanto": ["escala_absurda", "origem_inesperada"],
        "gancho": "Uma única mina numa ilha do arquipélago de Estocolmo deu nome a quatro elementos químicos: ítrio, térbio, érbio e itérbio. Outros cinco elementos também foram descobertos em pedras tiradas de lá.",
        "explicacao": (
            "Ytterby, cujo nome quer dizer \"aldeia de fora\", fica na ilha de Resarö, perto de Estocolmo. A mina "
            "local tirava quartzo desde os anos 1600 e, mais tarde, feldspato para porcelana. Em 1787, o tenente "
            "Carl Axel Arrhenius, que examinava a área para uma possível fortificação e gostava de química, notou "
            "uma pedra preta estranhamente pesada. Em 1794, o químico finlandês Johan Gadolin a analisou e viu que "
            "38% dela era uma \"terra\" desconhecida; o mineral passou a se chamar gadolinita. Dessa e de outras "
            "amostras da mesma pedreira, os químicos foram separando, ao longo de décadas, elemento após elemento. "
            "Quatro receberam pedaços do nome da aldeia: ítrio (descrito em 1794), érbio e térbio (1843) e itérbio "
            "(1878). Também foram descobertos ali o escândio, o hólmio (de Estocolmo), o túlio (de Thule, nome "
            "mítico do extremo norte), o gadolínio (homenagem a Gadolin) e, em 1802, o tântalo. Por isso Ytterby "
            "é considerada a fonte mais rica de descobertas de elementos do mundo. A mina fechou em 1933, chegou "
            "a guardar combustível de avião e hoje tem uma placa comemorativa na antiga entrada."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Ytterby",
            "is a village on the Swedish island of Resarö, in Vaxholm Municipality in the Stockholm archipelago. [...] "
            "The Swedish name of the village translates literally into \"outer village\". Ytterby is the single richest source of elemental discoveries in the world; "
            "the chemical elements yttrium (Y), terbium (Tb), erbium (Er), and ytterbium (Yb) are all named after Ytterby, and the elements holmium (Ho), scandium (Sc), thulium (Tm), tantalum (Ta), and gadolinium (Gd) were also first discovered there. [...] "
            "Quartz was mined in the area beginning in the 1600s for the ironworks in Uppland. Feldspar was mined for local porcelain manufacture [...] "
            "Feldspar and quartz mining continued until 1933, when the mine was shut down. [...] "
            "In 1953, the mine was renovated and used for the storage of jet fuel [...] "
            "The mine's elemental history began in 1787, when Lieutenant Carl Axel Arrhenius found an unidentified black mineral. "
            "He had previously explored the area for a potential fortification. His hobby interest in chemistry led him to notice the unusually heavy black rock [...] "
            "It was not until 1794 that Finnish chemist Johan Gadolin fully analysed the mineral and found that 38% of its composition was a new, unidentified earth element. [...] "
            "These elements include yttrium (Y), erbium (Er), terbium (Tb) and ytterbium (Yb), which were first described in 1794, 1843, 1843, and 1878, respectively. "
            "In 1989 the ASM International society installed a plaque at the former entrance to the mine [...] "
            "holmium (Ho, named after Stockholm), thulium (Tm, named after Thule, a mythic analogue of Scandinavia), and gadolinium (Gd, after the chemist Johan Gadolin)—can trace their discovery to the same quarry. "
            "The transition metal tantalum (Ta, after the Greek mythological figure Tantalus) was also discovered in a mineral sample from Ytterby in 1802.",
            nome="Ytterby")],
    },
    # 2 o fósforo saiu da urina de um alquimista
    {
        "temas_secundarios": ["revolucao_cientifica", "historia_medicina"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "O fósforo foi descoberto por volta de 1669 por um alquimista de Hamburgo que buscava a pedra filosofal fervendo urina. Ele usou cerca de 5.700 litros para obter só 120 gramas, e jogou fora a parte mais rica.",
        "explicacao": (
            "Hennig Brand tinha sido oficial na Guerra dos Trinta Anos. Gastou o dinheiro da primeira esposa na "
            "busca da pedra filosofal, que transformaria metais comuns em ouro, e seguiu com os recursos da segunda, "
            "uma viúva rica. Como outros alquimistas, apostava na urina e a combinava com vários materiais. Ao "
            "aquecer até o rubro os resíduos de urina fervida, viu o recipiente se encher de vapores luminosos e "
            "pingar um líquido que pegava fogo. Guardado num frasco, ele endureceu e seguiu brilhando com luz "
            "verde-pálida. Brand o batizou com a palavra grega para \"portador de luz\". O que ocorria: a urina "
            "contém fosfatos e compostos de carbono, e no calor forte o carbono arranca o oxigênio do fosfato, "
            "liberando o elemento. A indústria usa a mesma reação básica até hoje, com minério de fosfato e fornos "
            "elétricos. O rendimento de Brand foi péssimo, porque o sal que ele descartava continha a maior parte "
            "do fosfato. Fiel ao costume dos alquimistas, ele guardou segredo e tentou, sem sucesso, fazer ouro com "
            "o fósforo. Mais tarde vendeu a receita por 200 táleres. Johann Kunckel, em 1678, e Robert Boyle, em "
            "1680, chegaram ao fósforo de forma independente."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Hennig_Brand",
            "was a German alchemist who lived and worked in Hamburg. In 1669, Brand accidentally discovered the chemical element phosphorus while searching for the \"philosopher's stone\", a substance which was believed to transmute base metals into gold. [...] "
            "He held a post as a junior army officer during the Thirty Years' War [...] "
            "By the time his first wife died he had exhausted her money on this pursuit. He then married his second wife Margaretha, a wealthy widow whose financial resources allowed him to continue the search. "
            "Like many before him, he was interested in urine and tried combining it with various other materials, in hundreds of combinations. [...] "
            "Around 1669 he heated residues from boiled-down urine on his furnace until the retort was red hot, where all of a sudden glowing fumes filled it and liquid dripped out, bursting into flames. "
            "He could catch the liquid in a jar and cover it, where it solidified and continued to give off a pale-green glow. "
            "What he collected was phosphorus, which he named from the Greek word for \"light-bearing\" or \"light-bearer.\" [...] "
            "Brand kept his discovery secret, as alchemists of the time did, and worked with the phosphorus trying unsuccessfully to use it to produce gold. [...] "
            "Urine contains phosphates PO3−4, as sodium phosphate (with Na+) in the form of microcosmic salt, and various carbon-based organics. "
            "Under strong heat the oxygen atoms from the phosphate react with carbon to produce carbon monoxide CO, leaving elemental phosphorus P, which comes off as a gas. [...] "
            "This same essential reaction is still used today (but with mined phosphate ores, coke for carbon, and electric furnaces). "
            "Brand's process yielded far less phosphorus than it could have. The salt part he discarded contained most of the phosphate. "
            "He used about 1,500 US gallons (5,700 L) of urine to produce just 120 grams of phosphorus. [...] "
            "he later sold the recipe for 200 thalers to a Johann Daniel Kraft from Dresden. "
            "Subsequently, both Swedish chemist Johann Kunckel (in 1678) and Irish chemist Robert Boyle (in 1680) were able to independently discover phosphorus",
            nome="Hennig Brand")],
    },
    # 3 Mendeleev corrige a densidade do gálio
    {
        "temas_secundarios": ["revolucao_cientifica", "historia_matematica"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1875, o francês que descobriu o gálio mediu a densidade do metal e recebeu uma carta de Mendeleev pedindo que medisse de novo. Deu exatamente o valor que o russo previra em 1871, quando o elemento nem era conhecido.",
        "explicacao": (
            "Ao montar sua tabela, Dmitri Mendeleev deixou casas vazias e arriscou descrever os elementos que "
            "faltavam. Em 1871, chamou de \"eka-alumínio\" o que ficaria logo abaixo do alumínio e previu várias "
            "propriedades dele: densidade, ponto de fusão, o tipo de óxido, como se ligaria ao cloro. Disse até que "
            "seria achado com o espectroscópio. Em 1875, Paul-Émile Lecoq de Boisbaudran viu duas linhas violetas "
            "desconhecidas no espectro de um minério de zinco, a esfalerita, e no mesmo ano obteve o metal. "
            "Batizou-o de gálio, de Gallia, o nome latino da França. A primeira medida de densidade deu 4,7 g/cm³, "
            "e foi a única propriedade que não bateu com a previsão. Mendeleev escreveu ao francês sugerindo refazer "
            "a medida, e o novo resultado foi 5,9 g/cm³, o número que ele havia previsto. As demais previsões também "
            "se confirmaram. Houve ainda quem visse no nome um trocadilho com o próprio descobridor, já que \"le "
            "coq\" é galo em francês e \"gallus\" é galo em latim, mas Lecoq negou isso num artigo de 1877."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Gallium",
                "In 1871, the existence of gallium was first predicted by Russian chemist Dmitri Mendeleev, who named it \"eka-aluminium\" from its position in his periodic table. "
                "He also predicted several properties of eka-aluminium that correspond closely to the real properties of gallium, such as its density, melting point, oxide character, and bonding in chloride. "
                "Mendeleev further predicted that eka-aluminium would be discovered by means of the spectroscope [...] "
                "All of these predictions were later proven accurate. Gallium was discovered using spectroscopy by French chemist Paul-Émile Lecoq de Boisbaudran in 1875 from its characteristic spectrum (two violet lines) in a sample of sphalerite. "
                "Later that year, Lecoq obtained the free metal by electrolysis [...] "
                "He named the element \"gallia\", from Latin Gallia meaning 'Gaul', a name for his native land of France. "
                "It was later claimed that, in a multilingual pun of a kind favoured by men of science in the 19th century, he had also named gallium after himself: "
                "Le coq is French for 'the rooster', and the Latin word for 'rooster' is gallus. In an 1877 article, Lecoq denied this conjecture. "
                "Originally, de Boisbaudran determined the density of gallium as 4.7 g/cm3, the only property that failed to match Mendeleev's predictions; "
                "Mendeleev then wrote to him and suggested that he should remeasure the density, and de Boisbaudran then obtained the correct value of 5.9 g/cm3, that Mendeleev had predicted exactly.",
                nome="Gallium"),
            wiki("Mendeleev's_predicted_elements",
                "In 1871, Mendeleev predicted the existence of a yet-undiscovered element he named eka-aluminium (because of its proximity to aluminium in the periodic table).",
                nome="Mendeleev's predicted elements"),
        ],
    },
    # 4 Mendeleev e os elementos mais leves que o hidrogênio
    {
        "temas_secundarios": ["revolucao_cientifica", "estrelas"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Mendeleev, famoso por prever elementos que depois apareceram, também propôs gases mais leves que o hidrogênio, quase sem massa, que permeariam toda a matéria e o espaço. Essa previsão falhou: nunca foram detectados.",
        "explicacao": (
            "Depois de aceitar a descoberta do hélio e do argônio, Mendeleev criou em 1902 um \"grupo zero\" para "
            "esses gases que quase não reagem. Ele desconfiava da teoria atômica e, por isso, não via razão para o "
            "hidrogênio ser o elemento mais leve. Sugeriu que um membro ainda mais leve desse grupo poderia ter "
            "passado despercebido e seria o responsável pela radioatividade. Um dos candidatos era o \"corônio\", "
            "nome dado a uma linha misteriosa no espectro da coroa solar. Para o mais leve, calculou uma massa "
            "minúscula e uma velocidade de 2.500.000 metros por segundo, e imaginou esses gases atravessando toda a "
            "matéria, raramente reagindo. Em 1904, publicou o livreto \"Uma concepção química do éter\", com dois "
            "elementos mais leves que o hidrogênio formando uma atmosfera entre as estrelas, alimentada sobretudo "
            "pelo Sol. Nada disso se confirmou, e nenhum elemento assim jamais foi detectado. O corônio teve um fim "
            "sem glamour: corrigida uma calibração errada, a linha da coroa foi atribuída em 1939 a átomos de ferro "
            "que tinham perdido muitos elétrons. É um lembrete de que até o grande acertador da tabela periódica também "
            "errou feio."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Mendeleev's_predicted_elements",
            "In 1902, having accepted the evidence for elements helium and argon, Mendeleev placed these noble gases in Group 0 in his arrangement of the elements. "
            "As Mendeleev was doubtful of atomic theory to explain the law of definite proportions, he had no a priori reason to believe hydrogen was the lightest of elements, "
            "and suggested that a hypothetical lighter member of these chemically inert Group 0 elements could have gone undetected and be responsible for radioactivity. "
            "Currently some periodic tables of elements put lone neutrons in this place (see neutronium) but no such element has ever been detected. "
            "The heavier of the hypothetical proto-helium elements Mendeleev identified with coronium, named by association with an unexplained spectral line in the Sun's corona. "
            "A faulty calibration gave a wavelength of 531.68 nm, which was eventually corrected to 530.3 nm, which Grotrian and Edlén identified as originating from Fe XIV (i.e. Fe13+) in 1939. [...] "
            "The kinetic velocity of this gas was calculated by Mendeleev to be 2,500,000 meters per second. "
            "Nearly massless, these gases were assumed by Mendeleev to permeate all matter, rarely interacting chemically. [...] "
            "Mendeleev later published a theoretical expression of the ether in a small booklet entitled A Chemical Conception of the Ether (1904). "
            "His 1904 publication again contained two atomic elements smaller and lighter than hydrogen. "
            "He treated the \"ether gas\" as an interstellar atmosphere composed of at least two elements lighter than hydrogen. "
            "He stated that these gases originated due to violent bombardments internal to stars, the Sun being the most prolific source of such gases.",
            nome="Mendeleev's predicted elements")],
    },
    # 5 tecnécio: o primeiro elemento artificial veio pelo correio
    {
        "temas_secundarios": ["estrelas", "fisica_particulas"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "O primeiro elemento artificial saiu de uma peça descartada: uma folha de molibdênio radioativa de um cíclotron americano, mandada pelo correio para Palermo. Ali, em 1937, foi identificado o tecnécio, o elemento 43.",
        "explicacao": (
            "A tabela de Mendeleev já tinha um buraco entre o molibdênio e o rutênio, e em 1914 Henry Moseley "
            "confirmou que faltava o número 43. Pela posição, parecia fácil de achar, mas não foi: todos os "
            "isótopos do tecnécio são radioativos, e ele é o mais leve elemento com essa característica. Em 1925, "
            "químicos alemães anunciaram o \"masúrio\", mas ninguém repetiu o resultado, e um estudo posterior "
            "mostrou que a quantidade possível no minério deles seria indetectável. Em 1936, o italiano Emilio Segrè "
            "visitou o laboratório de Ernest Lawrence, inventor do cíclotron, e pediu peças descartadas que tinham "
            "ficado radioativas. Lawrence lhe enviou pelo correio uma folha de molibdênio do defletor da máquina. "
            "Em Palermo, Segrè e Carlo Perrier mostraram por química comparada que ali havia o elemento 43. Em "
            "1947, ele foi batizado com a palavra grega para \"artificial\". Hoje um de seus isótopos é usado em "
            "uns dez milhões de exames médicos por ano. E houve uma reviravolta: em 1952, o astrônomo Paul Merrill "
            "detectou tecnécio na luz de estrelas gigantes vermelhas. Como o elemento dura pouco, ele só podia estar "
            "sendo produzido nelas, o que reforçou a ideia de que as estrelas fabricam os elementos pesados."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Technetium",
            "It is the lightest element whose isotopes are all radioactive. [...] "
            "From the 1860s through 1871, early forms of the periodic table proposed by Dmitri Mendeleev contained a gap between molybdenum and ruthenium. [...] "
            "Although the location of technetium in the periodic table suggested that it should be easier to find than other undiscovered elements, this would not be the case due to technetium's radioactivity. "
            "In 1914, Henry Moseley determined the atomic number all elements known at the time, and found that atomic number 43 was missing [...] "
            "German chemists Walter Noddack, Otto Berg, and Ida Tacke reported the discovery of element 75 and element 43 in 1925, and named element 43 masurium [...] "
            "Later experimenters could not replicate the discovery, and it was dismissed as an error. [...] "
            "they are disproved by Paul Kuroda's study on the amount of technetium that could have been present in the ores they studied: "
            "it could not have exceeded 3 × 10−11 μg/kg of ore, and thus would have been undetectable by the Noddacks' methods. [...] "
            "The discovery of element 43 was finally confirmed in a 1937 experiment at the University of Palermo in Sicily by Carlo Perrier and Emilio Segrè. "
            "In mid-1936, Segrè visited the United States, first Columbia University in New York and then the Lawrence Berkeley National Laboratory in California. "
            "He persuaded cyclotron inventor Ernest Lawrence to let him take back some discarded cyclotron parts that had become radioactive. "
            "Lawrence mailed him a molybdenum foil that had been part of the deflector in the cyclotron. "
            "Segrè enlisted his colleague Perrier to attempt to prove, through comparative chemistry, that the molybdenum activity was indeed from an element with the atomic number 43, which they did. [...] "
            "In 1947, element 43 was named after the Greek word technetos (τεχνητός), meaning 'artificial', since it was the first element to be artificially produced. [...] "
            "They isolated the metastable isotope technetium-99m, which is now used in some ten million medical diagnostic procedures annually. "
            "In 1952, the astronomer Paul W. Merrill detected the spectral signature of technetium [...] in light from S-type red giants. "
            "The stars were near the end of their lives but were rich in the short-lived element, which indicated that it was being produced in the stars by nuclear reactions. "
            "That evidence bolstered the hypothesis that heavier elements are the product of nucleosynthesis in stars.",
            nome="Technetium")],
    },
    # 6 frâncio e Marguerite Perey
    {
        "temas_secundarios": ["personagens_esquecidos", "fisica_particulas"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "O último elemento descoberto na natureza, o frâncio, foi achado em 1939 por Marguerite Perey, ex-assistente de Marie Curie. Ela não tinha diploma, e por isso a descoberta foi apresentada à Academia por outro cientista.",
        "explicacao": (
            "Desde 1870 os químicos esperavam um metal alcalino abaixo do césio, e vários disseram tê-lo achado, já "
            "com nome: \"russium\", \"alkalinium\", \"virginium\" e \"moldavium\". Todos foram descartados. Perey "
            "entrou aos 19 anos no Instituto do Rádio, em Paris, como assistente pessoal de Marie Curie, e passou "
            "uma década purificando actínio. Em 1939, ao examinar actínio bem puro, notou uma radiação que não "
            "deveria estar ali. Depois de descartar outros elementos, concluiu que vinha de um produto novo, com "
            "química de metal alcalino: o elemento 87. A nota à Academia de Ciências foi apresentada pelo físico "
            "Jean Perrin, porque ela era só assistente de laboratório, sem diploma universitário. Ironia: o mesmo "
            "Perrin chegou a apoiar o \"moldavium\" de um rival em vez do achado de Perey, que acabou reconhecida "
            "como única descobridora. Ela propôs primeiro o nome \"catium\", mas Irène Joliot-Curie se opôs, pela "
            "lembrança de \"cat\", gato; ficou frâncio, em homenagem à França. O elemento é tão instável que nunca "
            "se viu uma amostra dele a olho nu. Em 1962, Perey se tornou a primeira mulher eleita para a Academia "
            "de Ciências da França, honra que fora negada a Marie Curie."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Francium",
                "As a consequence of its extreme instability, bulk francium has never been seen. [...] "
                "Francium was discovered by Marguerite Perey in France (from which the element takes its name) on January 7, 1939. [...] "
                "It was the last element first discovered in nature, rather than by synthesis. [...] "
                "As early as 1870, chemists thought that there should be an alkali metal beyond caesium. [...] "
                "in which he named the element russium after his home country. [...] "
                "They announced their discovery of element 87 and proposed the name alkalinium, as it would be the heaviest alkali metal. [...] "
                "Allison requested that it be named virginium after his home state of Virginia [...] "
                "Hulubei and Cauchois reported their discovery and proposed the name moldavium [...] "
                "Jean Baptiste Perrin, Nobel Prize winner and Hulubei's mentor, endorsed moldavium as the true eka-caesium over Marguerite Perey's recently discovered francium. "
                "Perey took pains to be accurate and detailed in her criticism of Hulubei's work, and finally she was credited as the sole discoverer of element 87. [...] "
                "Various tests eliminated the possibility of the unknown element being thorium, radium, lead, bismuth, or thallium. "
                "The new product exhibited chemical properties of an alkali metal [...] "
                "in 1946, she proposed the name catium (Cm) for her newly discovered element [...] "
                "Irène Joliot-Curie, one of Perey's supervisors, opposed the name due to its connotation of cat rather than cation [...] "
                "Perey then suggested francium, after France.",
                nome="Francium"),
            wiki("Marguerite_Perey",
                "In 1962, she was the first woman to be elected to the French Académie des Sciences, an honor denied to her mentor Curie. [...] "
                "In 1929 at the age of 19, Perey interviewed for a role as a personal assistant (technician) to Marie Curie at Curie's Radium Institute in Paris, France, and was hired. [...] "
                "Perey spent a decade sifting out actinium from all the other components of uranium ore [...] "
                "She confirmed this by isolating extremely pure actinium and studying its radiation very quickly [...] "
                "Perey's discovery was announced by Perrin, not Perey herself, because she was only a laboratory assistant with no university degree.",
                nome="Marguerite Perey"),
        ],
    },
    # 7 seabórgio: um elemento para alguém vivo
    {
        "temas_secundarios": ["leis_julgamentos", "guerra_fria"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Glenn Seaborg poderia receber cartas endereçadas só com nomes de elementos: seabórgio, laurêncio, berquélio, califórnio, amerício. Foi o primeiro homenageado com um elemento ainda vivo, e quase perdeu a honra.",
        "explicacao": (
            "Seaborg foi descobridor principal ou codescobridor de dez elementos, entre eles o plutônio, e dividiu "
            "o Nobel de Química de 1951. Quando a equipe de Albert Ghiorso, da qual ele fazia parte, foi reconhecida "
            "como descobridora do elemento 106, os oito membros sugeriram nomes que iam de Newton a Magalhães, sem "
            "consenso. Ghiorso convenceu sete deles a propor \"seabórgio\" e então pediu o consentimento do amigo "
            "de 50 anos, que ficou atônito e, depois de consultar a esposa, aceitou. O nome foi anunciado em março "
            "de 1994. Em agosto, a IUPAC, que oficializa os nomes, decidiu que nenhum elemento poderia homenagear "
            "uma pessoa viva e tirou \"seabórgio\" da lista. Houve protestos no mundo todo, e a Sociedade "
            "Americana de Química manteve o nome nas suas revistas, desafiando a IUPAC. Seaborg reclamou que seria "
            "a primeira vez que descobridores incontestes perderiam o privilégio de batizar um elemento. Em 1997, a "
            "IUPAC recuou e oficializou o nome. Seaborg disse que aquela era a maior honra que já recebera, maior "
            "até que o Nobel. O endereço de brincadeira, notado pela revista Discover, juntava o seabórgio ao "
            "laurêncio (do laboratório onde ele trabalhava), ao berquélio, ao califórnio e ao amerício. O único "
            "outro elemento batizado em homenagem a alguém vivo é o oganessônio, de 2016, por Yuri Oganessian."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Glenn_T._Seaborg",
                "Seaborg was the principal or co-discoverer of ten elements: plutonium, americium, curium, berkelium, californium, einsteinium, fermium, mendelevium, nobelium and element 106, "
                "then called unnilhexium, which while he was still living, was named seaborgium in his honor. "
                "He said about this naming, \"This is the greatest honor ever bestowed upon me—even better, I think, than winning the Nobel Prize. [...] "
                "He shared the Nobel Prize in Chemistry in 1951 with Edwin McMillan [...] "
                "He influenced the naming of so many elements that with the announcement of seaborgium, it was noted in Discover magazine's review of the year in science that he could receive a letter addressed in chemical elements: "
                "seaborgium, lawrencium (for the Lawrence Berkeley Laboratory where he worked), berkelium, californium, americium. "
                "Seaborgium is the first element ever to have been officially named after a living person. "
                "The second element to be so named is oganesson, in 2016, after Yuri Oganessian.",
                nome="Glenn T. Seaborg"),
            wiki("Seaborgium",
                "The eight members of the Ghiorso group suggested a wide range of names honoring Isaac Newton, Thomas Edison, Leonardo da Vinci, Ferdinand Magellan, the mythical Ulysses, George Washington, and Finland [...] "
                "He approached the team members one by one, until seven of them had agreed. He then told his friend and colleague of 50 years: "
                "\"We have seven votes in favor of naming element 106 seaborgium. Will you give your consent?\" My father was flabbergasted, and, after consulting my mother, agreed. "
                "The name seaborgium and symbol Sg were announced at the 207th national meeting of the American Chemical Society in March 1994 [...] "
                "However, IUPAC resolved in August 1994 that an element could not be named after a living person, and Seaborg was still alive at the time. [...] "
                "with seaborgium being dropped entirely as a name. "
                "This decision ignited a firestorm of worldwide protest [...] "
                "the American Chemical Society stood firmly behind the name seaborgium for element 106, together with all the other American and German naming proposals for elements 104 to 109, approving these names for its journals in defiance of IUPAC. [...] "
                "This would be the first time in history that the acknowledged and uncontested discoverers of an element are denied the privilege of naming it. [...] "
                "Finally, IUPAC rescinded these previous compromises and made a final, new recommendation in August 1997, in which the American and German proposals for elements 104 to 109 were all adopted, including seaborgium for element 106",
                nome="Seaborgium"),
        ],
    },
    # 8 háfnio: a teoria de Bohr indicou onde procurar
    {
        "temas_secundarios": ["mecanica_quantica", "minerais_rochas"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "Os químicos procuravam o elemento 72 entre as terras-raras. A teoria atômica de Niels Bohr indicava outro esconderijo: minérios de zircônio. Foi lá que ele apareceu, em 1923, e ganhou o nome latino de Copenhague.",
        "explicacao": (
            "Em 1914, os raios X de Henry Moseley passaram a definir o lugar de cada elemento pelo número atômico e "
            "mostraram que faltavam os de número 43, 61, 72 e 75. Começou a corrida. O francês Georges Urbain dizia ter achado o 72 entre "
            "as terras-raras, grupo de elementos muito parecidos entre si, e o chamou de \"céltio\". Mas os "
            "espectros e a química dele não batiam com o elemento encontrado depois. Em 1921, o químico Charles "
            "Bury sugeriu que o 72 lembraria o zircônio e não seria uma terra-rara, e no início de 1923 Niels Bohr "
            "e outros concordaram, apoiados nas teorias de Bohr sobre o átomo. Animados, Dirk Coster e George de "
            "Hevesy foram procurar em minérios de zircônio e acharam o elemento por espectroscopia de raios X, num "
            "zircão da Noruega, trabalhando em Copenhague. O nome veio de Hafnia, Copenhague em latim, cidade natal "
            "de Bohr. A briga também opôs químicos, que confiavam em métodos químicos, a físicos, que confiavam nos "
            "raios X. O disfarce era bom: o háfnio é tão parecido com o zircônio que até hoje separá-los é difícil "
            "e caro. Ele e o rênio foram os dois últimos elementos estáveis a ser descobertos."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Hafnium",
            "With this method, Moseley determined the number of lanthanides and showed the gaps in the atomic number sequence at numbers 43, 61, 72, and 75. [...] "
            "The X-ray spectroscopy done by Henry Moseley in 1914 showed a direct dependency between spectral line and effective nuclear charge. "
            "This led to the nuclear charge, or atomic number of an element, being used to ascertain its place within the periodic table. [...] "
            "Georges Urbain asserted that he found element 72 in the rare earth elements in 1907 and published his results on celtium in 1911. "
            "Neither the spectra nor the chemical behavior he claimed matched with the element found later [...] "
            "The controversy was partly because the chemists favored the chemical techniques which led to the discovery of celtium, while the physicists relied on the use of the new X-ray spectroscopy method [...] "
            "In 1921, Charles R. Bury suggested that element 72 should resemble zirconium and therefore was not part of the rare earth elements group. "
            "By early 1923, Niels Bohr and others agreed with Bury. These suggestions were based on Bohr's theories of the atom [...] "
            "Dirk Coster and Georg von Hevesy were motivated to search for the new element in zirconium ores. "
            "Hafnium was discovered by the two in 1923 in Copenhagen, Denmark, validating the original 1869 prediction of Mendeleev. "
            "It was ultimately found in zircon in Norway through X-ray spectroscopy analysis. "
            "The place where the discovery took place led to the element being named for the Latin name for \"Copenhagen\", Hafnia, the home town of Niels Bohr. [...] "
            "thus making elements 75 (rhenium) and 72 (hafnium) the last two stable elements to be discovered. [...] "
            "It is very similar to zirconium [...] "
            "hafnium is rare and difficult to separate from other elements, making it expensive.",
            nome="Hafnium")],
    },
    # 9 níquel e cobalto: metais com nome de duende
    {
        "temas_secundarios": ["mitologia", "palavras_viajantes"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O níquel tem nome de duende. Mineiros alemães culpavam um espírito travesso, o Nickel, por um minério que parecia de cobre e não dava cobre. Em 1751, um sueco extraiu dele um metal branco e lhe deu o nome do duende.",
        "explicacao": (
            "Nas Montanhas Metálicas, na Alemanha medieval, aparecia um mineral amarelado parecido com minério de "
            "cobre. Como não se conseguia extrair cobre dele, os mineiros puseram a culpa num espírito travesso do "
            "folclore alemão chamado Nickel e apelidaram a pedra de Kupfernickel, algo como \"cobre do Nickel\". "
            "Em 1751, o barão sueco Axel Fredrik Cronstedt tentou de novo tirar cobre dela e obteve, em vez disso, "
            "um metal branco, que batizou com o nome do espírito. O mineral, hoje chamado nicolita, é um arseneto "
            "de níquel. O cobalto tem uma história parecida: as primeiras tentativas de fundir seus minérios para "
            "obter cobre ou prata só davam um pó, e o arsênico que eles contêm aumentava a má fama. O dicionário "
            "dos irmãos Grimm ligava o nome desse minério às travessuras atribuídas aos kobolds, espíritos das "
            "minas, embora a origem exata da palavra seja discutida. Por volta de 1735, o químico sueco Georg "
            "Brandt mostrou que o cobalto era um metal novo e que era ele, e não o bismuto, que dava a cor azul ao "
            "vidro. Foi o primeiro metal descoberto desde a pré-história: ferro, cobre, ouro e os outros metais "
            "antigos não têm descobridor registrado."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Nickel",
                "In medieval Germany, a metallic yellow mineral was found in the Ore Mountains that resembled copper ore. "
                "But when miners were unable to get any copper from it, they blamed a mischievous sprite of German mythology, Nickel (similar to Old Nick), for besetting the copper. "
                "They called this ore Kupfernickel from German Kupfer 'copper'. This ore is now known as the mineral nickeline (formerly niccolite), a nickel arsenide. "
                "In 1751, Baron Axel Fredrik Cronstedt tried to extract copper from kupfernickel at a cobalt mine in the village of Los, Sweden, "
                "and instead produced a white metal that he named nickel after the spirit that had given its name to the mineral.",
                nome="Nickel"),
            wiki("Cobalt",
                "The first attempts to smelt those ores for copper or silver failed, yielding simply powder (cobalt(II) oxide) instead. "
                "Because the primary ores of cobalt always contain arsenic, smelting the ore oxidized the arsenic into the highly toxic and volatile arsenic oxide, adding to the notoriety of the ore. [...] "
                "Swedish chemist Georg Brandt (1694–1768) is credited with discovering cobalt c. 1735, showing it to be a previously unknown element, distinct from bismuth and other traditional metals. [...] "
                "He showed that compounds of cobalt metal were the source of the blue color in glass, which previously had been attributed to the bismuth found with cobalt. "
                "Cobalt became the first metal to be discovered since the pre-historical period. "
                "All previously known metals (iron, copper, silver, gold, zinc, mercury, tin, lead and bismuth) had no recorded discoverers.",
                nome="Cobalt"),
            wiki("Kobold",
                "And under \"kobalt\" it considered the name of cobalt ore derived from the supposed mischief caused by the kobold or Bergmännchen (mountain manikin, mountain spirit) in these mines.",
                nome="Kobold"),
        ],
    },
    # 10 platina: a "pratinha" que os espanhóis jogavam fora
    {
        "temas_secundarios": ["americas_pre_colombianas", "imperios_coloniais"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "Para os espanhóis, a platina achada nas Américas era uma impureza que atrapalhava o ouro: muitas vezes era jogada fora, e um decreto proibia misturá-la ao ouro. O nome vem de \"platina\", diminutivo de \"plata\", prata.",
        "explicacao": (
            "Em 1557, o humanista italiano Júlio César Scaliger descreveu um metal nobre achado entre o Darién e o "
            "México que nenhum fogo nem artifício espanhol conseguia derreter. O problema era o ponto de fusão "
            "altíssimo. Muito antes, povos nativos perto da atual Esmeraldas, no Equador, ligados à cultura La "
            "Tolita, tinham contornado isso: misturavam pós de ouro e platina e os aqueciam sem derreter, técnica "
            "chamada sinterização, obtendo uma liga macia o bastante para ser trabalhada. Já os colonizadores viam "
            "a platina como algo que estragava o ouro. Em 1735, os espanhóis Antonio de Ulloa e Jorge Juan viram "
            "indígenas minerando o metal durante uma viagem pela Colômbia e pelo Peru. A partir de amostras "
            "colombianas, William Brownrigg apresentou em 1750 uma descrição detalhada à Royal Society de Londres, "
            "e químicos de toda a Europa passaram a estudá-la. Na Espanha, com apoio do rei Carlos III, Pierre-"
            "François Chabaneau tentou purificá-la e obtinha resultados inconsistentes, porque o minério ainda "
            "tinha outros metais do grupo da platina, como irídio e ósmio, então desconhecidos. Depois de meses, "
            "chegou a 23 quilos de platina maleável e abriu o que se chamou de \"era da platina\" espanhola."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Platinum",
            "platina, a diminutive of plata \"silver\". [...] "
            "The metal was used by Native Americans near modern-day Esmeraldas, Ecuador to produce artifacts of a white gold-platinum alloy. "
            "Archeologists usually associate the tradition of platinum-working in South America with the La Tolita Culture [...] "
            "To work the metal, they would combine gold and platinum powders by sintering. The resulting gold–platinum alloy would then be soft enough to shape with tools. [...] "
            "The first European reference to platinum appears in 1557 in the writings of the Italian humanist Julius Caesar Scaliger as a description of an unknown noble metal found between Darién and Mexico, "
            "\"which no fire nor any Spanish artifice has yet been able to liquefy\". "
            "From their first encounters with platinum, the Spanish generally saw the metal as a kind of impurity in gold, and it was treated as such. "
            "It was often simply thrown away, and there was an official decree forbidding the adulteration of gold with platinum impurities. "
            "In 1735, Antonio de Ulloa and Jorge Juan y Santacilia saw Native Americans mining platinum while the Spaniards were travelling through Colombia and Peru for eight years. [...] "
            "In 1741, Charles Wood, a British metallurgist, found various samples of Colombian platinum in Jamaica, which he sent to William Brownrigg for further investigation. "
            "In 1750, after studying the platinum sent to him by Wood, Brownrigg presented a detailed account of the metal to the Royal Society [...] "
            "Other chemists across Europe soon began studying platinum [...] "
            "In 1786, Charles III of Spain provided a library and laboratory to Pierre-François Chabaneau to aid in his research of platinum. [...] "
            "but in truth the ore still contained the yet-undiscovered platinum-group metals. This led to inconsistent results in his experiments. "
            "At times, the platinum seemed malleable, but when it was alloyed with iridium, it would be much more brittle. [...] "
            "After several months, Chabaneau succeeded in producing 23 kilograms of pure, malleable platinum [...] "
            "This started what is known as the \"platinum age\" in Spain.",
            nome="Platinum")],
    },
    # 11 einstênio: achado na poeira da bomba H
    {
        "temas_secundarios": ["guerra_fria", "estrelas"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "O einstênio foi descoberto nos resíduos da primeira bomba de hidrogênio, em 1952, em filtros de papel levados por aviões através da nuvem da explosão. A descoberta ficou em segredo militar até 1955.",
        "explicacao": (
            "O teste Ivy Mike, em 1º de novembro de 1952 no atol de Enewetak, no Pacífico, foi o primeiro teste bem-"
            "sucedido de uma arma termonuclear. Nos resíduos apareceu um isótopo de plutônio que só se formaria se "
            "núcleos de urânio-238 tivessem engolido vários nêutrons de uma vez, algo considerado raríssimo. A "
            "equipe de Albert Ghiorso, de Berkeley, analisou então papéis de filtro que aviões tinham passado pela "
            "nuvem e, depois, detritos de coral do atol. No fim, recuperou menos de 200 átomos do elemento 99. Ele "
            "nasceu de núcleos de urânio que capturaram 15 nêutrons e sofreram sete decaimentos beta, o que só o "
            "fluxo de nêutrons altíssimo da explosão permitia. Surgiu também o elemento 100, o férmio. Os militares "
            "americanos mantiveram tudo em segredo até 1955, por causa da Guerra Fria. Como o projeto da bomba se "
            "chamava PANDA, o elemento 99 ganhou o apelido de \"Pandemônio\", mas os nomes oficiais homenagearam "
            "Einstein e Fermi, que morreram entre a proposta e o anúncio, em agosto de 1955. Os dados também "
            "interessavam à astronomia: a captura rápida de tantos nêutrons oferecia uma confirmação experimental "
            "do processo que ajuda a explicar como certos elementos pesados surgem no universo."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Einsteinium",
            "Einsteinium was first identified in December 1952 by Albert Ghiorso and co-workers at University of California, Berkeley [...] in the fallout from the Ivy Mike nuclear test. "
            "The test was done on November 1, 1952, at Enewetak Atoll in the Pacific Ocean and was the first successful test of a thermonuclear weapon. "
            "Initial examination of the debris from the explosion had shown the production of a new isotope of plutonium [...] "
            "At the time, the multiple neutron absorption was thought to be an extremely rare process [...] "
            "Ghiorso and co-workers analyzed filter papers which had been flown through the explosion cloud on airplanes [...] "
            "Larger amounts of radioactive material were later isolated from coral debris of the atoll [...] "
            "fewer than 200 atoms of einsteinium were recovered in the end. [...] "
            "It was produced by the capture of 15 neutrons by uranium-238 nuclei followed by seven beta decays [...] "
            "Such multiple neutron absorption was made possible by the high neutron flux density during the detonation [...] "
            "as well as in the 255Fm isotope of another new element, fermium. [...] "
            "Meanwhile, isotopes of element 99 (as well as of new element 100, fermium) were produced in the Berkeley and Argonne laboratories [...] "
            "The discovery of the new elements and the associated new data on multiple neutron capture were initially kept secret on the orders of the U.S. military until 1955 due to Cold War tensions and competition with Soviet Union in nuclear technologies. "
            "However, the rapid capture of so many neutrons would provide needed direct experimental confirmation  of the r-process multi-neutron absorption needed to explain the cosmic nucleosynthesis (production) of certain heavy elements [...] "
            "As the effort which had led to the design of Ivy Mike was codenamed Project PANDA, element 99 had been jokingly nicknamed \"Pandemonium\" "
            "but the official names suggested by the Berkeley group derived from two prominent scientists, Einstein and Fermi [...] "
            "Both Einstein and Fermi died between the time the names were originally proposed and when they were announced. "
            "The discovery of these new elements was announced by Albert Ghiorso at the first Geneva Atomic Conference held on 8–20 August 1955.",
            nome="Einsteinium")],
    },
    # 12 tungstênio: W de "espuma de lobo" e o elemento que foi a juízo
    {
        "temas_secundarios": ["palavras_viajantes", "leis_julgamentos"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O símbolo do tungstênio é W porque vem de \"espuma de lobo\": o minério parecia devorar o estanho na fundição. E é o único elemento que já foi objeto de processo de patente: a GE tentou patenteá-lo e perdeu.",
        "explicacao": (
            "Em 1781, o sueco Carl Wilhelm Scheele obteve um ácido novo de um mineral que então se chamava "
            "\"tungsten\", \"pedra pesada\" em sueco. Em 1783, os irmãos José e Fausto Elhuyar, na cidade "
            "espanhola de Bergara, isolaram o metal a partir do mesmo ácido tirado de outro mineral, a volframita, "
            "e o chamaram de \"wolfram\". Esse nome tem uma origem curiosa. Em 1546, Georgius Agricola chamou o "
            "mineral de \"lupi spuma\", espuma de lobo em latim, porque ele consumia grandes quantidades de estanho "
            "durante a extração, como se o devorasse feito um lobo. Em 1747, Johan Gottschalk Wallerius traduziu "
            "a ideia para o alemão \"wolf rahm\". Em 1949, a IUPAC adotou \"wolfram\" como nome oficial, mas "
            "cientistas de língua inglesa protestaram e, no ano seguinte, voltou-se a aceitar \"tungsten\", com o "
            "símbolo W mantido. Na Alemanha e em vários países europeus, o metal ainda se chama wolfram. A briga "
            "nos tribunais foi outra: em 1913, William Coolidge, da General Electric, obteve uma patente americana "
            "envolvendo o tungstênio, e em 1928 um tribunal dos Estados Unidos rejeitou a tentativa da empresa de "
            "patentear o elemento, anulando a patente."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Tungsten",
            "In 1781, Carl Wilhelm Scheele discovered that a new acid, tungstic acid, could be made from scheelite (at the time called tungsten). [...] "
            "In 1783, José and Fausto Elhuyar found an acid made from wolframite that was identical to tungstic acid. "
            "Later that year, at the Royal Basque Society in the town of Bergara, Spain, the brothers succeeded in isolating tungsten by reduction of this acid with charcoal, "
            "and they are credited with the discovery of the element (they called it \"wolfram\" or \"volfram\"). [...] "
            "Tungsten is unique amongst the elements in that it has been the subject of patent proceedings. "
            "In 1928, a US court rejected General Electric's attempt to patent it, overturning U.S. patent 1,082,933 granted in 1913 to William D. Coolidge. [...] "
            "The name tungsten (which means 'heavy stone' in Swedish and was the old Swedish name for the mineral scheelite and other minerals of similar density) [...] "
            "is derived from the mineral wolframite, which is the origin of the chemical symbol W. "
            "The name wolframite is derived from German wolf rahm ('wolf soot, wolf cream'), the name given to tungsten by Johan Gottschalk Wallerius in 1747. "
            "This, in turn, derives from Latin lupi spuma, the name Georg Agricola used for the mineral in 1546, which translates into English as 'wolf's froth' "
            "and is a reference to the large amounts of tin consumed by the mineral during its extraction, as though the mineral devoured it like a wolf. "
            "The name wolfram was accepted by the International Union of Pure and Applied Chemistry in 1949; this decision was disputed by English-speaking scientists, "
            "and the next year it was revised to reflect the widespread use of the name tungsten in that region, though the symbol W was kept. "
            "In Germany and several other European countries, the name wolfram is still prefe",
            nome="Tungsten")],
    },
    # 13 oganessônio: um "gás nobre" que talvez seja sólido
    {
        "temas_secundarios": ["relatividade", "estados_materia"],
        "tipos_espanto": ["misterio_aberto", "contraintuitivo"],
        "gancho": "O oganessônio, elemento 118, fica na coluna dos gases nobres, mas cálculos sugerem que seria sólido e bem reativo, por efeitos da relatividade. Ninguém conferiu: o único isótopo conhecido tem meia-vida de 0,7 ms.",
        "explicacao": (
            "A ideia de um sétimo gás nobre é antiga. Em 1895, um ano depois da descoberta do argônio, o químico "
            "dinamarquês Julius Thomsen previu um gás inerte com peso atômico de 292, perto dos 294 do único "
            "isótopo confirmado hoje. Em 1922, Niels Bohr disse que ele teria número atômico 118. O elemento só foi "
            "produzido em 2002, em Dubna, na Rússia, por uma equipe russo-americana. "
            "O isótopo conhecido tem meia-vida de 0,7 milésimo de segundo, curta demais para qualquer estudo "
            "químico, de modo que nenhuma propriedade além das nucleares foi medida. O que se sabe vem de cálculos. "
            "Num átomo tão pesado, os elétrons sentem efeitos da relatividade, e as simulações indicam um ponto de "
            "fusão de cerca de 325 kelvin, acima da temperatura ambiente; sem esses efeitos, ele derreteria por "
            "volta de 220 kelvin. Seria, portanto, provavelmente sólido, e talvez até um semicondutor, enquanto os "
            "gases nobres mais leves são isolantes. Também poderia ser bem mais reativo que o radônio, o gás nobre "
            "logo acima dele. Por via das dúvidas, a IUPAC recomendou em 2016 a terminação \"-on\" para os novos "
            "elementos desse grupo, tenham ou não propriedades de gás nobre."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "hipotese",
        "fontes": [wiki("Oganesson",
            "It was first synthesized in 2002 at the Joint Institute for Nuclear Research (JINR) in Dubna, near Moscow, Russia, by a joint team of Russian and American scientists. [...] "
            "Its only known isotope, oganesson-294, is highly radioactive, with a half-life of 0.7 ms. This half-life is too short for chemical studies. "
            "Because of relativistic effects, theoretical studies predict that it would be a solid at room temperature, and significantly reactive, unlike the other members of group 18 (the noble gases). [...] "
            "Danish chemist Hans Peter Jørgen Julius Thomsen predicted in April 1895, the year after the discovery of argon, that there was a whole series of chemically inert gases similar to argon [...] "
            "have an atomic weight of 292, close to the 294 now known for the first and only confirmed isotope of oganesson. "
            "Danish physicist Niels Bohr noted in 1922 that this seventh noble gas should have atomic number 118 [...] "
            "a new IUPAC recommendation published in 2016 recommended using the \"-on\" ending for new group 18 elements, regardless of whether they turn out to have the chemical properties of a noble gas. [...] "
            "Other than nuclear properties, no properties of oganesson or its compounds have been measured [...] "
            "However, theoretical calculations have shown that it could be significantly more reactive. [...] "
            "Monte Carlo simulations of oganesson's molecular dynamics predict it has a melting point of 325±15 K and a boiling point of 450±10 K due to relativistic effects (if these effects are ignored, oganesson would melt at ≈220 K). "
            "Thus oganesson would probably be a solid rather than a gas under standard conditions [...] "
            "spin–orbit effects may cause bulk oganesson to be a semiconductor, with a band gap of 1.5±0.6 eV predicted. All the lighter noble gases are insulators instead",
            nome="Oganesson")],
    },
    # 14 o falso elemento 118 de Berkeley
    {
        "temas_secundarios": ["fisica_particulas", "experimentos_psicologia"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Em 1999, um laboratório de Berkeley anunciou a criação dos elementos 118 e 116. Ninguém conseguiu repetir o resultado, nem o próprio laboratório. Em 2002, veio a explicação: os dados tinham sido fabricados.",
        "explicacao": (
            "Em 1998, o físico polonês Robert Smolańczuk publicou cálculos indicando que dava para criar o elemento "
            "118 fundindo chumbo com criptônio, com uma probabilidade parecida com a da reação que tinha produzido o "
            "elemento 106. Isso contrariava a previsão de que essas fusões ficariam exponencialmente mais raras a "
            "cada elemento mais pesado. Em 1999, pesquisadores do Lawrence Berkeley National Laboratory seguiram a "
            "pista e anunciaram, na revista Physical Review Letters e logo depois na Science, a descoberta dos "
            "elementos 118 e 116. Outros laboratórios tentaram reproduzir o experimento e falharam; Berkeley também "
            "não conseguiu. Em 2001 veio a retratação e, em junho de 2002, o diretor do laboratório anunciou que a "
            "alegação se baseava em dados fabricados pelo autor principal, Victor Ninov. Experimentos e teorias "
            "posteriores confirmaram a queda exponencial. O elemento 118 de verdade foi observado em 2002, em Dubna, "
            "na Rússia, mas com muito cuidado: a equipe esperou um experimento de confirmação em 2005 antes de "
            "anunciar, em 2006, três ou talvez quatro núcleos. Para registrar o primeiro, foram quatro meses de "
            "bombardeio de um alvo de califórnio com íons de cálcio. Ele só foi oficialmente reconhecido em 2015 "
            "e recebeu o nome de oganessônio."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Oganesson",
            "In late 1998, Polish physicist Robert Smolańczuk published calculations on the fusion of atomic nuclei towards the synthesis of superheavy atoms, including oganesson. "
            "His calculations suggested that it might be possible to make element 118 by fusing lead with krypton under carefully controlled conditions, "
            "and that the fusion probability (cross section) of that reaction would be close to the lead–chromium reaction that had produced element 106, seaborgium. "
            "This contradicted predictions that the cross sections for reactions with lead or bismuth targets would go down exponentially as the atomic number of the resulting elements increased. "
            "In 1999, researchers at Lawrence Berkeley National Laboratory made use of these predictions and announced the discovery of elements 118 and 116, in a paper published in Physical Review Letters, "
            "and very soon after the results were reported in Science. [...] "
            "In 2001, they published a retraction after researchers at other laboratories were unable to duplicate the results and the Berkeley lab could not duplicate them either. "
            "In June 2002, the director of the lab announced that the original claim of the discovery of these two elements had been based on data fabricated by principal author Victor Ninov. "
            "Newer experimental results and theoretical predictions have confirmed the exponential decrease in cross sections [...] "
            "The first genuine decay of atoms of oganesson was observed in 2002 at the Joint Institute for Nuclear Research (JINR) in Dubna, Russia [...] "
            "the announcement of the discovery was delayed until after a 2005 confirmatory experiment aimed at producing more oganesson atoms. [...] "
            "On 9 October 2006, the researchers announced that they had indirectly detected a total of three (possibly four) nuclei of oganesson-294 [...] "
            "produced via collisions of californium-249 atoms and calcium-48 ions. [...] "
            "the experiment took four months and involved a beam dose of 2.5×1019 calcium ions that had to be shot at the californium target to produce the first recorded event [...] "
            "In December 2015, it was recognized as one of four new elements by the Joint Working Party of the international scientific bodies IUPAC and IUPAP.",
            nome="Oganesson")],
    },
    # 15 argônio: o gás escondido numa diferença de 0,5%
    {
        "temas_secundarios": ["atmosfera", "medidas_padroes"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "O argônio, que forma 0,934% do ar, foi descoberto por causa de uma diferença de 0,5%: o nitrogênio tirado de compostos químicos era mais leve que o tirado do ar. A pista rendeu um Nobel a Lord Rayleigh.",
        "explicacao": (
            "Lord Rayleigh fazia medidas cuidadosas da densidade dos gases. Notou que o nitrogênio obtido de "
            "compostos químicos era 0,5% mais leve que o separado do ar atmosférico. A diferença era pequena, mas "
            "ocupou a atenção dele e de William Ramsay por meses, até concluírem que havia outro gás misturado ao "
            "nitrogênio do ar. Em 1894, no University College London, os dois retiraram de uma amostra de ar o "
            "oxigênio, o gás carbônico, a água e o nitrogênio. Para isso, repetiram um experimento de Henry "
            "Cavendish, que mais de cem anos antes, em 1785, já desconfiava de um componente do ar que não reagia: "
            "faíscas elétricas faziam o nitrogênio reagir, e uma solução alcalina absorvia os produtos. Sobrou um "
            "gás que não reagia com nada. Eles o chamaram de argônio, do grego para \"preguiçoso\" ou \"inativo\". "
            "Foi o primeiro gás nobre descoberto. Rayleigh ganhou o Nobel de Física de 1904 por suas investigações "
            "das densidades dos gases mais importantes e pela descoberta do argônio que veio delas. Hoje se sabe "
            "que o argônio é 0,934% do volume da atmosfera."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Argon",
                "Argon (Ancient Greek ἀργόν, neuter singular form of ἀργός meaning \"lazy\" or \"inactive\") is named in reference to its chemical inactivity. "
                "This chemical property of this first noble gas to be discovered impressed the namers. "
                "An unreactive gas was suspected to be a component of air by Henry Cavendish in 1785. "
                "Argon was first isolated from air in 1894 by Lord Rayleigh and Sir William Ramsay at University College London by removing oxygen, carbon dioxide, water, and nitrogen from a sample of clean air. "
                "They first accomplished this by replicating an experiment of Henry Cavendish's. [...] "
                "The alkali absorbed the oxides of nitrogen produced by the arc and also carbon dioxide. [...] "
                "Before isolating the gas, they had determined that nitrogen produced from chemical compounds was 0.5% lighter than nitrogen from the atmosphere. "
                "The difference was slight, but it was important enough to attract their attention for many months. "
                "They concluded that there was another gas in the air mixed in with the nitrogen. [...] "
                "Argon constitutes 0.934% by volume and 1.288% by mass of Earth's atmosphere.",
                nome="Argon"),
            {"url": "https://www.nobelprize.org/prizes/physics/1904/summary/", "titulo": "The Nobel Prize in Physics 1904", "idioma": "en",
             "trecho": "The Nobel Prize in Physics 1904 was awarded to Lord Rayleigh (John William Strutt) \"for his investigations of the densities of the most important gases and for his discovery of argon in connection with these studies\""},
        ],
    },
    # 16 iodo: das cinzas de algas da pólvora de Napoleão
    {
        "temas_secundarios": ["revolucoes_politicas", "historia_medicina"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "O iodo foi descoberto em 1811 nas cinzas de algas usadas para fazer salitre, ingrediente da pólvora, nas guerras de Napoleão. Investigando por que os tachos de cobre corroíam, Bernard Courtois viu subir um vapor violeta.",
        "explicacao": (
            "Courtois vinha de uma família de fabricantes de salitre, muito procurado na França das guerras "
            "napoleônicas. A produção usava uma substância extraída de algas recolhidas nas costas da Normandia e da "
            "Bretanha: as algas eram queimadas e as cinzas, lavadas. Ao investigar a corrosão dos recipientes de "
            "cobre, Courtois pôs ácido sulfúrico em excesso nos resíduos e viu subir uma nuvem de vapor violeta, "
            "que se condensava em cristais escuros nas superfícies frias. Suspeitou de um elemento novo, mas não "
            "tinha dinheiro para continuar a pesquisa e distribuiu amostras a outros cientistas. Em 1813, "
            "Gay-Lussac concluiu que era um elemento e propôs o nome \"iode\", do grego para \"violeta\", pela cor "
            "do vapor. Humphry Davy chegou à mesma conclusão quase ao mesmo tempo, e os dois brigaram pela "
            "prioridade, mas ambos reconheceram Courtois como o descobridor. O iodo virou antisséptico, e em 1908 "
            "um cirurgião introduziu a tintura de iodo para esterilizar a pele antes das operações. Courtois, porém, "
            "lutou com dificuldades financeiras a vida toda e morreu em 1838 sem bens para deixar à viúva e ao "
            "filho. Um jornal de química médica observou que, se ele tivesse tirado uma patente da descoberta, teria "
            "feito fortuna."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Iodine",
                "In 1811, iodine was discovered by French chemist Bernard Courtois, who was born to a family of manufacturers of saltpetre (an essential component of gunpowder). "
                "At the time of the Napoleonic Wars, saltpetre was in great demand in France. "
                "Saltpetre produced from French nitre beds required sodium carbonate, which could be isolated from seaweed collected on the coasts of Normandy and Brittany. "
                "To isolate the sodium carbonate, seaweed was burned and the ashes washed with water. "
                "While investigating the cause of corrosion to the copper vessels used in the process, Courtois added an excess of sulfuric acid to the waste remaining and a cloud of violet vapour arose. "
                "He noted that the vapour crystallised on cold surfaces, forming dark crystals. "
                "Courtois suspected that this material was a new element but lacked funding to pursue it further. [...] "
                "On 6 December 1813, Gay-Lussac found and announced that the new substance was either an element or a compound of oxygen and he found that it is an element. "
                "Gay-Lussac suggested the name \"iode\" (anglicised as \"iodine\"), from the Ancient Greek Ιώδης (iodēs, \"violet\"), because of the colour of iodine vapour. [...] "
                "Arguments erupted between Davy and Gay-Lussac over who identified iodine first, but they both ultimately recognized Courtois as the discoverer of the element. "
                "In 1873, the French medical researcher Casimir Davaine (1812–1882) discovered the antiseptic action of iodine. [...] "
                "In 1908, he introduced tincture of iodine as a way to rapidly sterilise the human skin in the surgical field.",
                nome="Iodine"),
            wiki("Bernard_Courtois",
                "He struggled financially for the rest of his life and died 27 September 1838. He was 61 years old and had no assets to leave to his widow or son. [...] "
                "If, on making this discovery, Courtois had taken out a certificate of invention, he would have realized a large estate.",
                nome="Bernard Courtois"),
        ],
    },
]
