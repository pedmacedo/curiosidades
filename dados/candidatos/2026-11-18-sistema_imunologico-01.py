LOTE = "2026-11-18-sistema_imunologico-01"
AREA = "corpo_medicina"
TEMA = "sistema_imunologico"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Metchnikoff e os espinhos na larva de estrela-do-mar
    {
        "temas_secundarios": ["historia_medicina", "vida_marinha"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "As células que \"comem\" invasores no nosso corpo foram descobertas com espinhos espetados em larvas de estrela-do-mar, em 1882. Grandes nomes da época, como Pasteur, receberam a ideia com ceticismo.",
        "explicacao": (
            "O zoólogo Élie Metchnikoff, nascido no Império Russo, deixou a Universidade de Odessa em 1882, em meio à "
            "turbulência política que se seguiu ao assassinato de Alexandre II, e montou um laboratório particular em Messina, na "
            "Sicília. Lá, enfiou pequenos espinhos de planta cítrica em larvas de estrela-do-mar e, depois, encontrou "
            "células incomuns cercando os espinhos. Ele ligou a cena ao que acontece nos animais que têm sangue, em que "
            "os glóbulos brancos se juntam no local de uma inflamação, e levantou a hipótese de que seria assim que "
            "essas células atacavam e matavam bactérias. O zoólogo Carl Claus, de Viena, sugeriu o nome \"fagócito\" "
            "para a célula que envolve e mata patógenos. A teoria esbarrou no ceticismo de especialistas como Louis "
            "Pasteur e Emil von Behring: muitos bacteriologistas da época achavam que os glóbulos brancos engoliam os "
            "micróbios e acabavam espalhando-os pelo corpo. O grande aliado foi Rudolf Virchow, que publicou a pesquisa "
            "na sua revista. A virada veio depois: em 1888, o próprio Pasteur deu a Metchnikoff um posto no Instituto "
            "Pasteur, onde ele ficou até o fim da vida, e a descoberta dos fagócitos lhe rendeu o Nobel de 1908."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Élie_Metchnikoff",
            "known in Western sources as Élie Metchnikoff, was a zoologist from the Russian Empire [...] "
            "In 1882 he resigned from Odessa University due to political turmoil after the assassination of Alexander II. He went to Sicily to set up his private laboratory in Messina. [...] "
            "due to some difficulties, he left in 1888 and went to Paris to seek Pasteur's advice. Pasteur gave him an appointment at the Pasteur Institute, where he remained for the rest of his life. [...] "
            "At Messina he discovered phagocytosis after experimenting on the larvae of starfish. In 1882 he first demonstrated the process when he inserted small citrus thorns into starfish larvae, then found unusual cells surrounding the thorns. "
            "He realized that in animals which have blood, the white blood cells gather at the site of inflammation, and he hypothesised that this could be the process by which bacteria were attacked and killed by the white blood cells. "
            "He discussed his hypothesis with Carl Friedrich Wilhelm Claus, Professor of Zoology at the University of Vienna, who suggested to him the term \"phagocyte\" for a cell which can surround and kill pathogens. [...] "
            "His theory, that certain white blood cells could engulf and destroy harmful bodies such as bacteria, met with scepticism from leading specialists including Louis Pasteur, Emil von Behring, and others. "
            "At the time, most bacteriologists believed that white blood cells ingested pathogens and then spread them further through the body. "
            "His major supporter was Rudolf Virchow, who published his research in his Archiv [...] "
            "His discovery of these phagocytes ultimately won him the Nobel Prize in 1908.",
            nome="Élie Metchnikoff")],
    },
    # 2 a anafilaxia descoberta no iate do príncipe de Mônaco
    {
        "temas_secundarios": ["historia_medicina", "vida_marinha"],
        "tipos_espanto": ["historia_humana", "contraintuitivo", "origem_inesperada"],
        "gancho": "A anafilaxia foi descoberta num navio do príncipe de Mônaco. Cientistas queriam deixar cães imunes à toxina de caravelas-portuguesas, mas uma nova dose, semanas depois, era fatal em vez de proteger.",
        "explicacao": (
            "A anafilaxia é uma reação alérgica grave, que pode matar e avança depressa. Sua descoberta começou em "
            "1901, quando o fisiologista francês Charles Richet e Paul Portier acompanharam o príncipe Alberto I de Mônaco "
            "numa expedição científica pela costa atlântica da França. A bordo do Princesse Alice II, eles extraíram "
            "uma toxina produzida por cnidários como a caravela-portuguesa e a anêmona-do-mar. A expectativa era que o "
            "cão injetado ficasse tolerante à toxina, mas ele teve uma reação forte. Em 1902, de volta ao laboratório, "
            "a dupla repetiu o teste: os cães aguentavam a primeira injeção, mas uma nova aplicação três semanas "
            "depois provocava sempre choque fatal, qualquer que fosse a dose. A primeira exposição, em vez de "
            "proteger, deixava o corpo pronto para reagir de forma desastrosa. Richet batizou o fenômeno de "
            "\"afilaxia\" e depois trocou para \"anafilaxia\", que achava mais sonoro; o termo vem do grego e quer "
            "dizer algo como \"contra a proteção\". O trabalho é visto como o início do estudo científico da alergia, "
            "palavra criada por Clemens von Pirquet em 1906, e ajudou a explicar a febre do feno e a asma. Richet "
            "recebeu o Nobel de Medicina em 1913."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Charles_Richet",
                "was a French physiologist at the Collège de France and immunology pioneer. [...] "
                "Richet, working with Paul Portier, discovered the phenomenon of anaphylaxis. In 1901, they joined Albert I, Prince of Monaco on a scientific expedition around the French coast of Atlantic Ocean. "
                "On board Albert's ship, Princesse Alice II, they extracted a toxin (which they called a hypnotoxin) that is produced by cnidarians such as Portuguese man o' war and sea anemone (Actinia sulcata). "
                "In their first experiment on the ship, they injected a dog with the toxin, expecting the dog to develop immunity (tolerance) to the toxin, but instead it suffered a severe immune reaction (hypersensitivity). "
                "In 1902, they repeated the injections in their laboratory and found that dogs normally tolerated the toxin at first injection, but when given subsequent injections three weeks later, they always developed fatal shock, regardless of the dose of the toxin they were given. "
                "Thus, they discovered that the first dose, instead of inducing tolerance (prophylaxis) as they had expected, caused further doses to be deadly. "
                "In 1902, Richet coined the term aphylaxis to describe the phenomenon; he later changed it to anaphylaxis because he thought it was more euphonious. "
                "The term is from the Greek [...] meaning \"against\", and [...] meaning \"protection\". [...] "
                "Their research is regarded as the beginning of the scientific study of allergy (the word was coined by Clemens von Pirquet in 1906). "
                "It helped explain hay fever and other allergic reactions to foreign substances, asthma, [...] "
                "in 1913 was awarded the Nobel Prize in Physiology or Medicine for his work.",
                nome="Charles Richet"),
            wiki("Anaphylaxis",
                "Anaphylaxis is a serious and potentially fatal allergic reaction that can progress rapidly.",
                nome="Anaphylaxis"),
        ],
    },
    # 3 Onésimo e a inoculação contra a varíola em Boston
    {
        "temas_secundarios": ["historia_medicina", "heranca_africana", "doencas_infecciosas"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Em 1721, Boston adotou a inoculação contra a varíola graças a Onésimo, um africano escravizado que a conhecia da África. Entre os inoculados, a mortalidade foi muito menor.",
        "explicacao": (
            "Onésimo, provavelmente do povo acã, foi dado de presente em 1706 ao pastor puritano Cotton Mather pela "
            "congregação dele. Em 1716 ou pouco antes, contou a Mather que tinha passado, na sua sociedade de origem, "
            "por um procedimento em que se tirava material das feridas de varíola, cortava-se a pele e se pingava uma "
            "gota. Era a variolação, praticada havia muito tempo por povos da África subsaariana. Quando a epidemia "
            "chegou a Boston, em 1721, Mather defendeu a técnica citando Onésimo como fonte, e foi atacado: médicos, "
            "religiosos e autoridades diziam que inocular pessoas sadias espalharia a doença e que era imoral "
            "interferir na providência divina, e Mather foi ridicularizado por confiar no relato de um escravizado. O "
            "médico Zabdiel Boylston aplicou o método mesmo assim, começando pelo próprio filho, de seis anos, e por "
            "duas pessoas que ele escravizava. Na epidemia de 1721–22, morreram seis dos 280 inoculados, cerca de 2,2%, "
            "contra 844 dos 5.889 doentes que não tinham sido inoculados, cerca de 14,3%. A variolação lançou as "
            "bases para o desenvolvimento das vacinas. O reconhecimento a Onésimo demorou: em 2016, uma revista o "
            "incluiu entre os cem maiores personagens da história de Boston."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Onesimus_(Bostonian)",
            "Onesimus (late 1600s–1700s) was an African (likely Akan) man who was instrumental in the mitigation of smallpox in Boston, Massachusetts. "
            "He introduced his enslaver, Puritan clergyman Cotton Mather, to the principle and procedure of the variolation method of inoculation, which prevented smallpox and laid the foundation for the development of vaccines. [...] "
            "He was first documented as living in the colonies in 1706, having been brought to North America as an enslaved person. [...] "
            "Recognition for Onesimus's contributions to medical science came in 2016, when the Boston magazine declared him among the 100 Best Bostonians of All Time. [...] "
            "In December of that year, he was given as a gift to the Puritan minister Cotton Mather by his congregation at North Church. [...] "
            "In 1716 or shortly before, Onesimus had described to Mather the process of inoculation that had been performed on him and others in his society in Africa (as Mather reported in a letter): \"People take Juice of Small-Pox; and Cut the Skin, and put in a drop.\" [...] "
            "The variolation method of inoculation was long practiced in Africa among sub-Saharan people. [...] "
            "When Boston experienced a smallpox outbreak in 1721, Mather promoted inoculation as protection against it, citing Onesimus and African folk medicine as the source of the procedure. "
            "His advocacy for inoculation met resistance from those suspicious of African medicine. "
            "Doctors, ministers, laymen, and Boston city officials argued that the practice of inoculating healthy individuals would spread the disease and that it was immoral to interfere with the working of divine providence. "
            "Also, Mather was ridiculed publicly for relying on the testimony of an enslaved person. [...] "
            "Nonetheless, a physician, Zabdiel Boylston, carried out the method Onesimus had described [...] "
            "Dr. Boylston first inoculated his six-year-old son and two of his slaves. "
            "Two hundred eighty individuals were inoculated during the 1721–22 Boston smallpox epidemic. "
            "The population of 280 inoculated patients experienced only six deaths (approx. 2.2 percent), compared to 844 deaths among the 5,889 non-inoculated smallpox patients (approx. 14.3 percent).",
            nome="Onesimus (Bostonian)")],
    },
    # 4 o timo, "acidente evolutivo", até 1961
    {
        "temas_secundarios": ["historia_medicina", "anatomia"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Até 1961, o timo, uma glândula no peito, era tido como um \"acidente evolutivo\" sem função. Retirando-o de camundongos com um dia de vida, Jacques Miller descobriu que dele saem as células T, peças-chave da imunidade.",
        "explicacao": (
            "O timo fica na frente do peito, logo abaixo da tireoide, e tem dois lobos. Por muito tempo, foi visto "
            "como um órgão vestigial, sem função. Quem mudou isso foi o pesquisador franco-australiano Jacques Miller, "
            "que fazia doutorado em Londres estudando leucemia em camundongos. Ele removeu cirurgicamente o timo de "
            "animais com um dia de vida e notou que lhes faltava uma população de linfócitos, depois batizada de "
            "células T, com o T vindo do nome do órgão. Os camundongos sem timo desde o nascimento não conseguiam "
            "rejeitar tecidos estranhos nem resistir a muitas infecções: o órgão era vital para o sistema imune "
            "adaptativo. Miller mostrou depois que o timo também elimina as células T que atacariam o próprio corpo. "
            "Por causa dessa descoberta, ele chegou a ser descrito como \"a única pessoa viva\" capaz de dizer que foi "
            "o primeiro a descrever as funções de um órgão humano. O timo tem uma vida curiosa: cresce até a "
            "puberdade, chegando a algo entre 20 e 50 gramas, e depois começa a encolher e perder atividade, com parte "
            "do volume ocupada por gordura e tecido conjuntivo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Thymus",
                "The importance of the thymus in the immune system was discovered in 1961 by Jacques Miller, by surgically removing the thymus from one-day-old mice, and observing the subsequent deficiency in a lymphocyte population, subsequently named T cells after the organ of their origin. "
                "Until the discovery of its immunological role, the thymus had been dismissed as an \"evolutionary accident\", without functional importance. [...] "
                "The thymus is located in the anterior mediastinum. It is made up of two lobes that meet in the upper midline, and stretch from below the thyroid in the neck to as low as the cartilage of the fourth rib. [...] "
                "It increases to a mass of 20 to 50 grams by puberty. It then begins to decrease in size and activity in a process called thymic involution. [...] "
                "Fat and connective tissue fill a part of the thymic volume.",
                nome="Thymus"),
            wiki("Jacques_Miller",
                "is a French-Australian research scientist. He is known for having discovered the function of the thymus [...] "
                "He was accepted to the Chester Beatty Research Institute of Cancer Research (part of the Institute of Cancer Research, London) and as a PhD student at the University of London. "
                "Miller chose to study the pathogenesis of lymphocytic leukemia in mice [...] "
                "Miller showed that experimental animals without a thymus at birth were incapable of rejecting foreign tissues and resisting many infections, thus demonstrating that the thymus is vital for the development and function of the adaptive immune system. "
                "Prior to this, the thymus was believed to be a vestigial organ with no function. "
                "His discovery has led many to describe Miller as the \"world's only living person who can claim to have been the first to have described the functions of a human organ\". [...] "
                "Miller went on to show that the thymus produces the T cells, that it removes autoreactive T cells (central T cell tolerance)",
                nome="Jacques Miller"),
        ],
    },
    # 5 AIRE: o timo exibe proteínas de outros órgãos
    {
        "temas_secundarios": ["genetica"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "No timo, algumas células fabricam proteínas que pertencem a outros órgãos do corpo, como um mostruário de si mesmo. As células T que reagem a esse mostruário são eliminadas, o que ajuda a evitar doenças autoimunes.",
        "explicacao": (
            "Cada célula T nasce com um receptor montado pelo embaralhamento aleatório de pedaços de genes. Isso gera "
            "uma variedade enorme, mas também produz células capazes de reconhecer proteínas do próprio corpo, que "
            "precisam ser eliminadas ainda no timo. Para isso entra em cena o gene AIRE. Na parte interna do timo, a "
            "medula, ele faz células epiteliais ativarem uma ampla coleção de genes típicos de outros órgãos e "
            "produzirem proteínas que normalmente só existiriam em tecidos periféricos. Os pesquisadores chamam esse "
            "reflexo do corpo de \"sombra imunológica do próprio\". As células T em formação são expostas a ele, e as "
            "que reagem com força a essas proteínas morrem por apoptose; algumas células T CD4 expostas a elas "
            "sobrevivem como células T reguladoras. Quando o AIRE está defeituoso, células T que reconhecem antígenos "
            "do próprio corpo saem do timo e entram na circulação, o que pode causar várias doenças autoimunes. O gene "
            "foi descrito em 1997 por dois grupos independentes, que o localizaram no cromossomo 21 e mostraram que "
            "mutações nele causam a síndrome poliglandular autoimune do tipo I."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Autoimmune_regulator",
                "AIRE is a transcription factor expressed in the medulla (inner part) of the thymus. It is part of the mechanism which eliminates self-reactive T cells that would cause autoimmune disease. "
                "It exposes T cells to normal, healthy proteins from all parts of the body, and T cells that react to those proteins are destroyed. [...] "
                "T cells receptors are generated by randomly shuffled gene segments which results in a highly diverse population of T cells—each with a unique antigen specificity. "
                "Subsequently, T cells with receptors that recognize the body's own proteins need to be eliminated while still in the thymus. "
                "Through the action of AIRE, medullary thymic epithelial cells (mTEC) express major proteins from elsewhere in the body (tissue-restricted antigens, TRA) and T cells that respond to those proteins are eliminated through cell death (apoptosis). [...] "
                "When AIRE is defective, T cells that recognize antigens normally produced by the body can exit the thymus and enter circulation. This can result in a variety of autoimmune diseases. "
                "The gene was first reported by two independent research groups Aaltonen et al. and Nagamine et al. in 1997 who were able to isolate and clone the gene from human chromosome 21q22.3. "
                "Their work was able to show that mutations in the AIRE gene are responsible for the pathogenesis of autoimmune polyglandular syndrome type I. [...] "
                "In the thymus, the autoimmune regulator (AIRE) induces the transcription of a broad array of organ-specific genes, resulting in the production of proteins that are normally restricted to peripheral tissues. "
                "This ectopic expression creates an \"immunological self-shadow\" that exposes developing T cells to peripheral antigens",
                nome="Autoimmune regulator"),
            wiki("Thymus",
                "Thymocytes that react strongly to self antigens die by apoptosis. Some CD4 positive T cells exposed to self antigens persist as T regulatory cells.",
                nome="Thymus"),
        ],
    },
    # 6 V(D)J: linfócitos recortam o próprio DNA
    {
        "temas_secundarios": ["genetica"],
        "tipos_espanto": ["escala_absurda", "engenhosidade"],
        "gancho": "Seus linfócitos editam o próprio DNA: escolhem pedaços de genes, emendam esses pedaços e apagam o que ficou no meio. Assim, um número limitado de genes gera centenas de bilhões de combinações de anticorpos.",
        "explicacao": (
            "As regiões variáveis dos anticorpos, a parte que se encaixa no invasor, não estão escritas prontas no "
            "genoma. Elas vêm em segmentos de três tipos: V (variável), D (diversidade) e J (junção). Na cadeia "
            "pesada humana, há 44 segmentos V, 27 D e 6 J. Durante o amadurecimento de cada linfócito, na medula óssea "
            "para as células B e no timo para as T, um segmento de cada tipo é escolhido de modo quase aleatório e "
            "emendado aos outros, e o DNA que havia entre eles é apagado do genoma daquela célula. Cada linfócito "
            "termina, assim, com uma receita própria de receptor. As combinações possíveis chegam a centenas de "
            "bilhões, embora parte delas seja descartada por reagir ao próprio corpo. Esse repertório permite "
            "reconhecer antígenos de quase qualquer patógeno, de bactérias e vírus a parasitas e vermes, e até "
            "células alteradas, como as do câncer. O preço é que o reconhecimento às vezes recai sobre o pólen ou "
            "sobre os próprios tecidos, o que leva a alergias e à autoimunidade. Susumu Tonegawa recebeu o Nobel de "
            "Medicina de 1987 por descobrir esse princípio genético da diversidade dos anticorpos."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("V(D)J_recombination",
            "V(D)J recombination (variable–diversity–joining rearrangement) is the mechanism of somatic recombination that occurs only in developing lymphocytes during the early stages of T and B cell maturation. [...] "
            "V(D)J recombination in mammals occurs in the primary lymphoid organs (bone marrow for B cells and thymus for T cells) and in a nearly random fashion rearranges variable (V), joining (J), and in some cases, diversity (D) gene segments. "
            "The process ultimately results in novel amino acid sequences in the antigen-binding regions of immunoglobulins and TCRs that allow for the recognition of antigens from nearly all pathogens including bacteria, viruses, parasites, and worms as well as \"altered self cells\" as seen in cancer. "
            "The recognition can also be allergic in nature (e.g. to pollen or other allergens) or may match host tissues and lead to autoimmunity. "
            "In 1987, Susumu Tonegawa was awarded the Nobel Prize in Physiology or Medicine \"for his discovery of the genetic principle for generation of antibody diversity\". [...] "
            "the human immunoglobulin heavy chain region contains 2 Constant (Cμ and Cδ) gene segments and 44 Variable (V) gene segments, plus 27 Diversity (D) gene segments and 6 Joining (J) gene segments. [...] "
            "DNA rearrangement causes one copy of each type of gene segment to go in any given lymphocyte, generating an enormous antibody repertoire; roughly 3×1011 combinations are possible, although some are removed due to self reactivity. [...] "
            "Any DNA between these two gene segments is deleted. [...] "
            "All other gene segments between V and D segments are now deleted from the cell's genome.",
            nome="V(D)J recombination")],
    },
    # 7 maturação de afinidade: evolução acelerada no linfonodo
    {
        "temas_secundarios": ["evolucao", "genetica"],
        "tipos_espanto": ["conexao_inesperada", "escala_absurda"],
        "gancho": "Numa infecção, seus linfonodos fazem uma evolução acelerada: células B mutam seus genes de anticorpo num ritmo até um milhão de vezes maior que o de outras células, e as que se ligam melhor ao invasor são selecionadas.",
        "explicacao": (
            "O processo se chama maturação de afinidade e acontece nos centros germinativos, estruturas temporárias "
            "que se formam em linfonodos, no baço e nas placas de Peyer do intestino. As células B passam por duas "
            "zonas. Na zona escura, elas se dividem depressa, com ciclos que podem durar só cinco horas, e acumulam "
            "mutações nos trechos do gene que formam a parte do anticorpo que toca o antígeno: cerca de uma ou duas "
            "mutações por trecho a cada geração. Na zona clara, elas disputam recursos escassos, como o antígeno "
            "exibido por células dendríticas foliculares e os sinais de um número limitado de células T auxiliares. "
            "As que fazem anticorpos de maior afinidade levam vantagem e sobrevivem, enquanto a maioria das células "
            "do centro germinativo acaba removida por macrófagos. Repetido rodada após rodada, o ciclo de mutação e "
            "seleção refina os anticorpos, e numa segunda exposição ao mesmo antígeno eles podem ter afinidade várias "
            "vezes maior que na primeira. O mecanismo exato da hipermutação ainda não é conhecido. Laboratórios "
            "imitam a receita, com mutações aleatórias e seleção, para aprimorar anticorpos."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Affinity_maturation",
                "With repeated exposures to the same antigen, a host will produce antibodies of successively greater affinities. "
                "A secondary response can elicit antibodies with several fold greater affinity than in a primary response. [...] "
                "Somatic hypermutation: Mutations in the variable, antigen-binding coding sequences (known as complementarity-determining regions (CDR)) of the immunoglobulin genes. "
                "The mutation rate is up to 1,000,000 times higher than in cell lines outside the lymphoid system. "
                "Although the exact mechanism of the SHM is still not known, a major role for the activation-induced (cytidine) deaminase has been discussed. "
                "The increased mutation rate results in 1-2 mutations per CDR and, hence, per cell generation. [...] "
                "Clonal selection: B cells that have undergone SHM must compete for limiting growth resources, including the availability of antigen and paracrine signals from TFH cells. "
                "The follicular dendritic cells (FDCs) of the germinal centers present antigen to the B cells, and the B cell progeny with the highest affinities for antigen, having gained a competitive advantage, are favored for positive selection leading to their survival. [...] "
                "Because a limited number of TFH cells reside in the germinal center [...] "
                "Like the natural prototype, the in vitro affinity maturation is based on the principles of mutation and selection.",
                nome="Affinity maturation"),
            wiki("Germinal_center",
                "Germinal centers or germinal centres (GCs) are transiently formed structures within B cell zone (follicles) in secondary lymphoid organs – lymph nodes, ileal Peyer's patches, and the spleen – where mature B cells are activated, proliferate, differentiate, and mutate their antibody genes (through somatic hypermutation aimed at achieving higher affinity) during a normal immune response; "
                "most of the germinal center B cells (BGC) are removed by tingible body macrophages. [...] "
                "GC B cells cycle through the two distinct zones of the germinal center: the light zone and the dark zone. [...] "
                "B cells in GC tend to divide rapidly and frequently, and they can have cell cycles as short as only five hours.",
                nome="Germinal center"),
        ],
    },
    # 8 anticorpos de camelo sem cadeias leves
    {
        "temas_secundarios": ["evolucao", "farmacos"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Camelos, lhamas e alpacas têm, além dos anticorpos comuns, uns mais simples, sem as cadeias leves. Pedaços deles, pequenos e resistentes, alcançam alvos escondidos e viraram ferramenta de pesquisa.",
        "explicacao": (
            "Um anticorpo típico tem duas cadeias pesadas e duas leves, e o ponto que se liga ao alvo combina as "
            "regiões variáveis das duas. Em 1989, um grupo liderado por Raymond Hamers, na Universidade Livre de "
            "Bruxelas, investigava o sistema imune de dromedários e achou, além dos anticorpos esperados, outros "
            "formados só por duas cadeias pesadas. O resultado saiu na Nature em 1993. Entre os mamíferos, só os "
            "camelídeos têm esse tipo, que corresponde a cerca de metade dos seus anticorpos. Em 1995, uma equipe da "
            "Universidade de Miami encontrou anticorpos de cadeia pesada de outro tipo em tubarões. As semelhanças "
            "entre os dois são atribuídas a exigências funcionais ou à evolução convergente, e não a um parentesco. "
            "Desses anticorpos de camelídeos foram criados os primeiros anticorpos de domínio único, os nanocorpos. "
            "Eles resistem melhor ao calor e conseguem alcançar alvos inacessíveis a anticorpos inteiros, como o "
            "centro ativo de enzimas, graças a uma alça longa que penetra nessas cavidades. Por serem pequenos, são "
            "fáceis de produzir em bactérias, e bibliotecas montadas com anticorpos de dromedário já foram usadas para "
            "buscar nanocorpos contra o SARS-CoV-2."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Heavy-chain_antibody",
                "A heavy-chain antibody is an antibody which consists only of two heavy chains and lacks the two light chains usually found in antibodies. "
                "In common antibodies, the antigen binding region consists of the variable domains of the heavy and light chains (VH and VL). [...] "
                "In 1989 a group of biologists led by Raymond Hamers at the Free University Brussels investigated the immune system of dromedaries. "
                "In addition to the expected four-chain antibodies, they identified simpler antibodies consisting only of two heavy chains. "
                "This discovery was published in Nature in 1993. In 1995 a research team at the University of Miami found a different type of heavy-chain antibodies in sharks. [...] "
                "The only mammals with heavy-chain (IgG-like) antibodies are camelids such as dromedaries, camels, llamas and alpacas. [...] "
                "It has been reasoned that these similarities are caused by functional requirements, or convergent evolution, rather than a genuine relationship. "
                "About 50% of the antibodies in camelids are of the ordinary mammalian heavy/light-chain type. [...] "
                "Phage-displayed dromedary camel VHH libraries have been made for isolating single-domain antibodies against SARS-CoV-2 and other virus infections. "
                "The smaller size and single domain make these antibodies easier to transform into bacterial cells for bulk production, making them ideal for research purposes.",
                nome="Heavy-chain antibody"),
            wiki("Single-domain_antibody",
                "The first single-domain antibodies were engineered from heavy-chain antibodies found in camelids at the Université Libre de Bruxelles; these are called VHH fragments. [...] "
                "These peptides have similar affinity to antigens as whole antibodies, but are more heat-resistant and stable towards detergents and high concentrations of urea. [...] "
                "Camelid and fish derived sdAbs are able to bind to hidden antigens that are not accessible to whole antibodies, for example to the active sites of enzymes. "
                "This property has been shown to result from their extended CDR3 loop, which is able to penetrate such buried sites.",
                nome="Single-domain antibody"),
        ],
    },
    # 9 CRISPR nasceu como sistema imune de bactérias
    {
        "temas_secundarios": ["microbiologia", "genetica"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "A tesoura genética CRISPR começou como sistema imune de bactérias: elas guardam no próprio DNA pedaços de vírus que já as atacaram, para reconhecê-los numa nova invasão.",
        "explicacao": (
            "As estranhas repetições no DNA bacteriano foram vistas pela primeira vez por acaso, em 1987, por Ishino e "
            "colegas, ao clonar um gene da bactéria E. coli. O microbiologista espanhol Francisco Mojica estudou essas "
            "sequências em arqueias e, em 2001, junto com Jansen, propôs a sigla CRISPR. A função continuou um enigma "
            "até 2005, quando três grupos independentes mostraram que parte dos \"espaçadores\", os trechos entre as "
            "repetições, vinha do DNA de vírus e plasmídeos: eram fragmentos de vírus que já tinham atacado a célula. "
            "Isso sugeria uma forma de imunidade adaptativa em bactérias. Os três estudos foram rejeitados de início "
            "por revistas de prestígio e acabaram publicados em outras. A prova experimental veio em 2007: a bactéria "
            "Streptococcus thermophilus incorporou espaçadores do DNA de um vírus que a infectava, e os pesquisadores "
            "conseguiam mudar a resistência dela acrescentando ou apagando espaçadores. Em 2010, um estudo mostrou que "
            "o sistema corta o DNA de vírus e plasmídeos invasores. Dessa defesa microbiana saiu a técnica de edição "
            "genética CRISPR-Cas9, reconhecida com o Nobel de Química de 2020, dado a Emmanuelle Charpentier e Jennifer "
            "Doudna."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("CRISPR",
            "The development of the CRISPR-Cas9 genome editing technique was recognized by the Nobel Prize in Chemistry in 2020 awarded to Emmanuelle Charpentier and Jennifer Doudna. [...] "
            "The CRISPR/Cas system evolved in nature as a means for bacteria to protect themselves from invading viruses and bacteriophages by inserting pieces of their DNA into the host genome. "
            "This allowed the adaptive immune system to respond accordingly on a subsequent infection. [...] "
            "The first description of what would later be called CRISPR is Ishino, et al. in 1987. They accidentally cloned part of a CRISPR sequence together with the iap gene [...] from Escherichia coli. [...] "
            "Spanish microbiologist Francisco Mojica studied the function of repeats in the archaeal genera Haloferax and Haloarcula. [...] "
            "In 2001, Mojica and Jansen, who were searching for additional interrupted repeats, proposed the acronym CRISPR [...] "
            "However, CRISPR's function remained enigmatic. "
            "In 2005, three independent research groups showed that some CRISPR spacers are derived from phage DNA and extrachromosomal DNA such as plasmids. "
            "In effect, the spacers are fragments of DNA gathered from viruses that previously attacked the cell. "
            "The source of the spacers was a sign that the CRISPR-cas system could have a role in adaptive immunity in bacteria. "
            "All three studies proposing this idea were initially rejected by high-profile journals, but eventually appeared elsewhere. [...] "
            "In 2007, the first experimental evidence that CRISPR was part of the adaptive immune system was published. "
            "A CRISPR region in Streptococcus thermophilus acquired spacers from the DNA of an infecting bacteriophage. "
            "The researchers manipulated the resistance of S. thermophilus to different types of phages by adding and deleting spacers whose sequence matched those found in the phages. [...] "
            "A 2010 study reported that CRISPR-Cas cuts strands of both phage and plasmid DNA in S. thermophilus.",
            nome="CRISPR")],
    },
    # 10 sarampo e a amnésia imune
    {
        "temas_secundarios": ["doencas_infecciosas"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "O sarampo pode apagar parte da memória do sistema imune. Num estudo com 77 crianças, a infecção eliminou de 11% a 73% dos anticorpos protetores que elas já tinham.",
        "explicacao": (
            "O fenômeno ganhou o nome de \"amnésia imune\". O vírus do sarampo mata células que produzem anticorpos e "
            "células de memória, as que guardam a resistência a patógenos já enfrentados. Estudos em primatas sugerem "
            "que, depois da recuperação, o corpo gera novas células de memória, mas voltadas só para o sarampo: a "
            "pessoa fica imune a ele por muito tempo e perde parte das defesas contra outras doenças. A medida mais "
            "direta veio num estudo publicado na Science em 2019. Pesquisadores analisaram o sangue de 77 crianças não "
            "vacinadas de uma comunidade da Holanda, coletado antes e depois de um surto, com o VirScan, ferramenta que "
            "identifica com uma gota de sangue os vírus que já infectaram alguém. A descoberta foi quase acidental: a "
            "equipe estava só ajustando a tecnologia. Conforme a gravidade do caso, as crianças perderam 33% ou 40% do "
            "conjunto total de anticorpos. Em quatro macacos acompanhados por até cinco meses, a perda média foi de 40% "
            "a 60%. Comparações da mortalidade infantil antes e depois da vacinação sugerem que a supressão dura de 2 a "
            "3 anos. A vacina usa uma versão atenuada do vírus, que não esgota a memória imune."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": "https://www.eurekalert.org/news-releases/702178",
             "titulo": "Measles virus infection destroys immune system memory (Howard Hughes Medical Institute, EurekAlert!)",
             "idioma": "en",
             "trecho": "An analysis of blood from 77 unvaccinated children before and after a measles outbreak swept through their Netherlands community revealed that the virus erases the body's memory of previous pathogens. "
                       "Measles eliminated between 11 and 73 percent of the children's protective antibodies [...] "
                       "Researchers report the news October 31, 2019, in the journal Science. [...] "
                       "Researchers had hypothesized that measles might cause a kind of \"immune amnesia,\" where the body forgets the pathogens it had already seen. "
                       "Elledge's group hadn't been planning to test the idea - they were just fine-tuning their virus-detecting technology. "
                       "VirScan, a tool Elledge and his colleagues reported in 2015, identifies all the viruses that have infected an individual, using just a single drop of blood. [...] "
                       "Depending on whether the infection was mild or severe, kids lost 33 or 40 percent of their total antibody collection. [...] "
                       "The researchers repeated the experiment in four macaque monkeys - this time collecting blood samples before and up to five months after infection. "
                       "The results were even more stark. The monkeys lost, on average, 40 to 60 percent of the antibodies that protect them from other pathogens."},
            wiki("Measles",
                "The virus targets the memory cells of the immune system; these are components of the adaptive immune system, providing the body with resistance to pathogens which have previously been encountered. [...] "
                "The measles virus can deplete previously acquired immune memory by killing cells that make antibodies, and thus weakens the immune system [...] "
                "The measles vaccine contains an attenuated strain of the virus which does not deplete immune memory. "
                "This suppression phenomenon, known as \"immune amnesia\", increases the risk of subsequent infections. [...] "
                "Primate studies suggest that immune amnesia arises during infection when the virus destroys existing memory lymphocytes; after recovery, the body generates new memory lymphocytes which are specific to measles virus alone. "
                "This creates lasting immunity to measles re-infection, but destroys existing immunities to other diseases. "
                "Comparison of childhood mortality statistics from before and after the introduction of  measles vaccination suggests that immune amnesia continues for 2–3 years following infection with the measles virus.",
                nome="Measles"),
        ],
    },
    # 11 oftalmia simpática: um olho ferido, os dois atacados
    {
        "temas_secundarios": ["sentidos", "historia_medicina"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Um ferimento que perfura um olho pode, em casos raros, levar o sistema imune a atacar os dois olhos, às vezes anos depois. Suspeita-se que foi assim que Louis Braille perdeu a visão do olho que não tinha se ferido.",
        "explicacao": (
            "A doença se chama oftalmia simpática. Normalmente, o sistema imune não tem contato com as proteínas de "
            "dentro do olho. Quando um trauma penetrante expõe esse conteúdo, ele passa a tratar esses antígenos como "
            "estranhos e os ataca. Hoje se pensa que é uma reação autoimune, uma hipersensibilidade tardia dirigida a "
            "estruturas com melanina da camada de fotorreceptores da retina. O resultado é uma inflamação da úvea dos "
            "dois olhos, que pode deixar a pessoa completamente cega. Os sintomas podem surgir de dias a vários anos "
            "depois do ferimento. É uma complicação rara: atinge de 0,2% a 0,5% dos ferimentos oculares não "
            "cirúrgicos e menos de 0,01% das perfurações cirúrgicas. Há descrições dela em textos da Grécia antiga, "
            "mas o entendimento moderno vem do escocês William MacKenzie, que a caracterizou e lhe deu nome. Na época "
            "dele, o tratamento preferido era mercúrio por via oral e sanguessugas aplicadas no olho. Louis Braille, "
            "inventor do sistema de leitura e escrita para pessoas cegas, feriu um olho aos três anos, com uma "
            "sovela na oficina do pai, e ficou totalmente cego. A biografia dele costuma atribuir a cegueira a uma "
            "infecção que passou para os dois olhos, mas há quem a atribua à oftalmia simpática. O escritor e "
            "humorista americano James Thurber, que perdeu um olho aos seis anos, teve a cegueira adulta "
            "diagnosticada como oftalmia simpática."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Sympathetic_ophthalmia",
            "sympathetic ophthalmia (SO), also called spared eye injury, is a granulomatous diffuse inflammation of the uveal layer (uveitis) of both eyes following trauma to one eye. "
            "It can leave the affected person completely blind. Symptoms may develop from days to several years after a penetrating eye injury. [...] "
            "Sympathetic ophthalmia is currently thought to be an autoimmune inflammatory response toward ocular antigens, specifically a delayed hypersensitivity to melanin-containing structures from the outer segments of the photoreceptor layer of the retina. "
            "The immune system, which normally is not exposed to ocular proteins, is introduced to the contents of the eye following traumatic injury. "
            "Once exposed, it senses these antigens as foreign, and begins attacking them. [...] "
            "Sympathetic ophthalmia is rare, affecting 0.2% to 0.5% of non-surgical eye wounds, and less than 0.01% of surgical penetrating eye wounds. [...] "
            "Although descriptions of sympathetic ophthalmia can be found in ancient Greek texts, modern understanding of SO derives from the works of Scotland's William MacKenzie who characterized and named the disease sympathetic ophthalmitis. "
            "At MacKenzie's time, oral mercury and leeches applied to the conjunctiva were the treatments of choice for SO. "
            "It is thought that Louis Braille, who injured one of his eyes as a child, lost vision in his other eye owing to SO. "
            "James Thurber's adult blindness was also diagnosed as sympathetic ophthalmia deriving from the loss of an eye when he was six years old.",
            nome="Sympathetic ophthalmia"),
            wiki("Louis_Braille",
                "was a French educator and the inventor of a reading and writing system named after him, braille, intended for use by visually impaired people. [...] "
                "Braille was blinded in one eye at the age of three.  This occurred as a result from an accident with a stitching awl in his father's harness-making shop. "
                "Consequently, an infection set in and spread to both eyes, resulting in total blindness.",
                nome="Louis Braille"),
            wiki("James_Thurber",
                "was an American cartoonist, writer, humorist, journalist, and playwright.",
                nome="James Thurber"),
        ],
    },
    # 12 o "pecado original antigênico"
    {
        "temas_secundarios": ["doencas_infecciosas", "historia_medicina"],
        "tipos_espanto": ["contraintuitivo", "origem_inesperada"],
        "gancho": "A primeira gripe da vida deixa uma marca que guia as respostas de anticorpos dali em diante. O efeito ganhou o nome de \"pecado original antigênico\", por analogia com o pecado original cristão.",
        "explicacao": (
            "O fenômeno foi descrito em 1960 por Thomas Francis Jr. Segundo ele, os anticorpos da infância respondem "
            "sobretudo ao antígeno dominante do vírus da primeira gripe do tipo A, e essa marca inicial governa as "
            "respostas seguintes. O mecanismo envolve as células B de memória. Elas surgem na primeira infecção e "
            "reagem a novas infecções bem mais depressa do que as células novatas. Mas os vírus mudam: a superfície "
            "deles sofre mutações que ajudam a escapar da defesa. Diante de uma versão um pouco diferente, o corpo "
            "reativa de preferência as memórias antigas, cujos anticorpos se ligam mal às partes alteradas e ainda "
            "atrapalham a ativação de células novatas que poderiam fazer anticorpos melhores. A resposta fica "
            "\"presa\" à primeira experiência. O efeito já foi descrito para gripe, SARS-CoV-2, dengue, HIV e outros "
            "vírus, e pesa no desenho de vacinas: na dengue, depois de formada a resposta a um dos quatro sorotipos, "
            "é improvável que vacinar contra outro funcione, por isso a primeira dose precisa cobrir os quatro de "
            "forma equilibrada. Ainda assim, o impacto real sobre a proteção não está bem estabelecido e parece "
            "variar com o agente, o lugar e a idade."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Original_antigenic_sin",
            "Original antigenic sin, also known as antigenic imprinting, the Hoskins effect,  immunological imprinting, or primary addiction is the propensity of the immune system to preferentially use immunological memory based on a previous infection when a second slightly different version of that foreign pathogen (e.g. a virus or bacterium) is encountered. "
            "This leaves the immune system \"trapped\" by the first response it has made to each antigen, and unable to mount potentially more effective responses during subsequent infections. [...] "
            "The phenomenon has been described in relation to influenza virus, SARS-CoV-2, dengue fever, human immunodeficiency virus (HIV) and to several other viruses. [...] "
            "This phenomenon was first described in 1960 by Thomas Francis Jr. in the article \"On the Doctrine of Original Antigenic Sin\". "
            "It is named by analogy to the Christian theological concept of original sin. [...] "
            "The antibody of childhood is largely a response to dominant antigen of the virus causing the first type A influenza infection of the lifetime. [...] "
            "The imprint established by the original virus infection governs the antibody response thereafter. [...] "
            "These memory B cells respond to specific epitopes on the surface of viral proteins to produce antigen-specific antibodies and can respond to infection much faster than naive B cells can to novel antigens. [...] "
            "a virus may undergo antigenic drift, in which the viral surface proteins (the epitopes) change through natural mutation. This allows the virus to escape the immune system. "
            "The altered virus preferentially reactivates previously activated high-affinity memory B cells and spurs antibody production. "
            "However, the antibodies produced generally ineffectively bind to the altered epitopes. "
            "In addition, these antibodies inhibit activation of naive B cells that could make more effective antibodies to the second virus. [...] "
            "In dengue fever, for example, once a response against one serotype has been established, it is unlikely that vaccination against a second will be effective. "
            "This implies that balanced responses against all four virus serotypes must be established with the first vaccine dose. [...] "
            "However, the impact of antigenic sin on protection has not been well established and appears to differ with each infectious agent vaccine, geographic location, and age.",
            nome="Original antigenic sin")],
    },
    # 13 a gravidez como um transplante tolerado
    {
        "temas_secundarios": ["desenvolvimento_humano", "evolucao"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Para o sistema imune da mãe, o feto lembra um transplante, porque carrega genes do pai. A placenta usa vários truques para não ser atacada, e um deles é o mesmo que vermes parasitas usam para se esconder.",
        "explicacao": (
            "A tolerância da mãe ao feto contraria a reação que normalmente rejeitaria algo estranho ao corpo. Os "
            "imunologistas o comparam a um órgão transplantado, pois ele traz material genético diferente do da mãe, "
            "herdado do pai. A placenta funciona como uma barreira e cria um lugar protegido do sistema imune. Ela "
            "secreta neurocinina B com moléculas de fosfocolina, o mesmo recurso que nematódeos parasitas usam para "
            "escapar das defesas do hospedeiro. As células do trofoblasto não exibem as moléculas HLA-A e HLA-B, ao "
            "contrário da maioria das células do corpo, e supõe-se que isso evite o ataque das células T da mãe; por "
            "outro lado, mostram as formas atípicas HLA-E e HLA-G, que provavelmente afastam as células natural "
            "killer, que destroem células sem esse tipo de marca. A placenta também forma uma camada contínua de "
            "células fundidas, sem espaços entre elas, que limita a passagem de células imunes; essa fusão parece ser "
            "obra de proteínas herdadas de um retrovírus que se instalou no genoma. Células T reguladoras ajudam a "
            "manter o equilíbrio: mulheres com perdas gestacionais repetidas têm menos delas. Mesmo com tudo isso, a "
            "placenta deixa passar os anticorpos IgG da mãe, que protegem o feto de infecções."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Immune_tolerance_in_pregnancy",
            "Immune tolerance in pregnancy or maternal immune tolerance is the immune tolerance shown towards the fetus and placenta during pregnancy. "
            "This tolerance counters the immune response that would normally result in the rejection of something foreign in the body [...] "
            "The placenta functions as an immunological barrier between the mother and the fetus, creating an immunologically privileged site. [...] "
            "It secretes neurokinin B containing phosphocholine molecules. This is the same mechanism used by parasitic nematodes to avoid detection by the immune system of their host. [...] "
            "The placental trophoblast cells do not express the classical MHC class I isotypes HLA-A and HLA-B, unlike most other cells in the body, and this absence is assumed to prevent destruction by maternal cytotoxic T cells, which otherwise would recognize the fetal HLA-A and HLA-B molecules as foreign. "
            "On the other hand, they do express the atypical MHC class I isotypes HLA-E and HLA-G, which is assumed to prevent destruction by maternal natural killer cells, which otherwise destroy cells that do not express any MHC class I. [...] "
            "It forms a syncytium without any extracellular spaces between cells in order to limit the exchange of migratory immune cells between the developing embryo and the body of the mother [...] "
            "The fusion of the cells is apparently caused by viral fusion proteins from endosymbiotic endogenous retrovirus. [...] "
            "Still, the placenta does allow maternal immunoglobulin G (IgG) to pass to the fetus to protect it against infections. [...] "
            "As a fetus forms, it is seen similarly to an organ transplant due to it being semi-allogenic, having genetic material different to the mother. "
            "Since the fetus has partial paternal genetic material [...] "
            "Results from a study reveals that women with recurrent pregnancy loss have reduced levels of Treg cells.",
            nome="Immune tolerance in pregnancy")],
    },
    # 14 o Paciente de Berlim
    {
        "temas_secundarios": ["doencas_infecciosas", "genetica"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "O primeiro homem considerado curado do HIV recebeu, para tratar uma leucemia, células-tronco de um doador com uma mutação rara que impede o vírus de se prender às células. Depois disso, o HIV deixou de ser detectado.",
        "explicacao": (
            "O americano Timothy Ray Brown descobriu que tinha HIV em 1995, quando estudava em Berlim. Em 2006, "
            "recebeu também o diagnóstico de leucemia mieloide aguda e, em fevereiro de 2007, passou por um "
            "transplante de células-tronco do sangue feito por uma equipe de médicos em Berlim, entre eles Gero "
            "Hütter. Entre 60 doadores compatíveis, a equipe escolheu um que tinha duas cópias de uma variante rara do "
            "receptor CCR5, a CCR5-Δ32, que impede o HIV de se prender à célula. Cerca de 1 em cada 1.000 pessoas de "
            "ascendência europeia herda essa mutação, que é mais rara em outras populações. O transplante foi "
            "repetido um ano depois, por causa de uma recaída da leucemia. Nos três anos seguintes, mesmo sem tomar "
            "antirretrovirais, os pesquisadores não acharam HIV no sangue nem em biópsias dele. Para preservar seu "
            "anonimato, ele foi apresentado em 2008 como \"o Paciente de Berlim\", e só se revelou em 2010. O caso, "
            "porém, não virou receita: Brown teve complicações graves, e os pesquisadores concluíram que o "
            "procedimento não deveria ser repetido em outras pessoas com HIV. Onze anos depois, foi anunciado um "
            "segundo caso aparente de cura, o do \"Paciente de Londres\", também com um doador portador da mutação. "
            "Brown morreu em 2020, depois da volta da leucemia."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Timothy_Ray_Brown",
            "Timothy Ray Brown (March 11, 1966 – September 29, 2020) was an American considered to be the first person cured of HIV/AIDS. "
            "Brown was called \"The Berlin Patient\" at the 2008 Conference on Retroviruses and Opportunistic Infections, where his cure was first announced, in order to preserve his anonymity. He chose to come forward in 2010. [...] "
            "was diagnosed with HIV in 1995 while studying in Berlin. In 2006, he was diagnosed with acute myeloid leukemia. "
            "On February 7, 2007, he underwent a procedure known as hematopoietic stem cell transplantation to treat leukemia (performed by a team of doctors in Berlin, Germany, including Gero Hütter). "
            "From 60 matching donors, they selected a [CCR5]-Δ32 homozygous donor, an individual with two genetic copies of a rare variant of a cell surface receptor. "
            "This genetic trait confers resistance to HIV infection by blocking attachment of HIV to the cell. "
            "Roughly one in 1,000 people of European ancestry have this inherited mutation, but it is rarer in other populations. "
            "The transplant was repeated a year later after a leukemia relapse. "
            "Over the three years after the initial transplant, and despite discontinuing antiretroviral therapy, researchers could not detect HIV in Brown's blood or in various biopsies. [...] "
            "suffered from serious transplant complications, graft-versus-host disease and leukoencephalopathy, which led researchers to conclude that the procedure should not be performed on others with HIV [...] "
            "Eleven years later, at the same conference, it was announced that it appeared that a second man had been cured. He was called \"The London Patient\" [...] "
            "The selected donor also carried the CCR5-Δ32 mutation. [...] "
            "In September 2020, Brown revealed the leukemia that prompted his historic treatment had returned in 2019 and that he was terminally ill. [...] "
            "where he later died on September 29, 2020.",
            nome="Timothy Ray Brown")],
    },
    # 15 bezerros gêmeos e a tolerância imunológica
    {
        "temas_secundarios": ["genetica", "historia_medicina"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Em 1945, um geneticista notou que bezerros gêmeos não idênticos tinham, a vida toda, células do sangue um do outro. Isso mostrou que o sistema imune aprende o que é \"seu\" e abriu caminho para os transplantes.",
        "explicacao": (
            "Ray Owen, criado numa fazenda leiteira em Wisconsin, estudava a herança dos grupos sanguíneos do gado. "
            "Ao analisar gêmeos gerados por touros diferentes, percebeu que cada bezerro tinha os antígenos "
            "sanguíneos dos dois pais. Os gêmeos eram quimeras: carregavam as próprias células do sangue e também as "
            "do irmão, numa mistura estável, que se mantinha por toda a vida. Esses gêmeos dividiam uma mesma "
            "placenta. O achado, publicado na Science em 1945, mostrava "
            "que o \"próprio\" é aprendido pelo sistema imune durante o desenvolvimento, mas teve pouca repercussão até "
            "ser citado em 1949 por Frank Macfarlane Burnet e Frank Fenner. Por meio deles, Peter Medawar soube do "
            "trabalho e o usou para explicar por que bezerros gêmeos fraternos aceitavam enxertos de pele um do outro, "
            "algo que ele observara tentando criar um método infalível para distinguir gêmeos idênticos de fraternos. "
            "Em 1953, Medawar e colegas mostraram que camundongos que recebiam células estranhas no útero ou ao nascer "
            "passavam a aceitar enxertos do mesmo doador. Burnet e Medawar ganharam o Nobel de 1960; Owen ficou de "
            "fora, e Medawar lhe escreveu dizendo que ele também deveria ter sido incluído."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Ray_D._Owen",
                "whose discovery of unusual, “mixed,” red blood cell types in cattle twins in 1945 launched the fields of modern immunology and organ transplantation. "
                "Owen's 1945 findings were published in the journal Science. "
                "This observation demonstrated that self was “learned” by the immune system during development and paved the way for research involving induction of immune tolerance and early tissue grafting. "
                "When Frank Macfarlane Burnet and Sir Peter Brian Medawar were awarded their 1960 Nobel Prize in Physiology or Medicine for the discovery of acquired immunological tolerance, Owen was not mentioned in the prize. "
                "However, in a letter to Owen, Medawar stated that he believed Owen should have also been included in the prize. [...] "
                "Owen was born and raised on a dairy farm in Genesee, Wisconsin [...] "
                "The lab studied blood samples from cattle all over the world, investigating genetic markers and the inheritance of red blood cell antigens. "
                "This research led Owen to investigate a genetic situation involving twin calves fathered by different sires. "
                "Each calf expressed both sets of paternal blood group antigens. "
                "Owen's “analyses revealed that the twins were chimeric, each containing their own blood cells as well as those derived from their twin sibling.” [...] "
                "Owen's findings were published with little attention until Frank Macfarlane Burnet and Frank Fenner published their monograph “The Production of Antibodies” in 1949. "
                "It was through Burnet and Fenner's work that Peter Medawar learned of Owen's findings and used it to help explain his findings that dizygotic twin calves accept each other's skin grafts after birth.",
                nome="Ray D. Owen"),
            wiki("Immune_tolerance",
                "The phenomenon of immune tolerance was first described by Ray D. Owen in 1945, who noted that dizygotic twin cattle sharing a common placenta also shared a stable mixture of each other's red blood cells (though not necessarily 50/50), and retained that mixture throughout life. [...] "
                "This observation was experimentally validated by Leslie Brent, Rupert E. Billingham and Peter Medawar in 1953, who showed by injecting foreign cells into fetal or neonatal mice, they could become accepting of future grafts from the same foreign donor. [...] "
                "we had been goaded by Dr. H.P. Donald into trying to devise a foolproof method of distinguishing monozygotic from dizygotic twins",
                nome="Immune tolerance"),
        ],
    },
]
