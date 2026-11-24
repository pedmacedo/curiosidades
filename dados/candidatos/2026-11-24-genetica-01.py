LOTE = "2026-11-24-genetica-01"
AREA = "biologia"
TEMA = "genetica"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Mendel ignorado e os dados "bons demais" segundo Fisher
    {
        "temas_secundarios": ["evolucao", "probabilidade", "historia_matematica"],
        "tipos_espanto": ["historia_humana", "misterio_aberto"],
        "gancho": "Mendel publicou suas leis da herança em 1866 e foi quase ignorado por 35 anos. Depois da fama, veio a suspeita: em 1936, o estatístico Ronald Fisher concluiu que os dados das ervilhas eram bons demais.",
        "explicacao": (
            "Mendel apresentou o trabalho sobre cruzamentos de plantas em duas reuniões de uma sociedade de "
            "naturalistas em Brno, em 1865, e o publicou no ano seguinte. Na época, o artigo foi lido como um estudo "
            "sobre híbridos, não sobre herança, e foi citado só umas três vezes nos 35 anos seguintes. Em 1900, Hugo "
            "de Vries, Carl Correns e Erich von Tschermak, cada um num país, confirmaram por conta própria vários "
            "resultados dele e publicaram a redescoberta num intervalo de dois meses. Em 1936, Ronald Fisher, "
            "estatístico e geneticista de populações, reconstruiu os experimentos e notou que as proporções entre "
            "características dominantes e recessivas, como ervilhas amarelas e verdes, ficavam perto demais de 3 para "
            "1, de forma consistente e pouco plausível. Para Fisher, os dados da maioria dos experimentos tinham sido "
            "ajustados para concordar com o que Mendel esperava. Outros estudiosos concordam que os números estão "
            "próximos demais do esperado. Nasceu assim o \"paradoxo mendeliano\": estatisticamente, os dados parecem "
            "bons demais, mas tudo o que se sabe sobre Mendel torna improvável que ele tenha fraudado ou ajustado os "
            "resultados sem perceber. Várias explicações já foram propostas, entre elas o viés de confirmação, e o "
            "caso segue em discussão."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Gregor_Mendel",
            "He published his work in 1866 [...] "
            "Erich von Tschermak, Hugo de Vries and Carl Correns independently verified several of Mendel's experimental findings in 1900 [...] "
            "Mendel presented his paper, Versuche über Pflanzenhybriden (\"Experiments on Plant Hybridization\"), at two meetings of the Natural History Society of Brno in Moravia on 8 February and 8 March 1865. [...] "
            "When Mendel's paper was published in 1866 in Verhandlungen des naturforschenden Vereines in Brünn, it was seen as essentially about hybridization rather than inheritance, had little impact, and was cited only about three times over the next thirty-five years. [...] "
            "All three of these researchers, each from a different country, published their rediscovery of Mendel's work within a two-month span in the spring of 1900. [...] "
            "In 1936, Ronald Fisher, a prominent statistician and population geneticist, reconstructed Mendel's experiments, analyzed results from the F2 (second filial) generation, and found the ratio of dominant to recessive phenotypes (e.g., yellow versus green peas; round versus wrinkled peas) to be implausibly and consistently too close to the expected ratio of 3 to 1. "
            "Fisher asserted that \"the data of most, if not all, of the experiments have been falsified to agree closely with Mendel's expectations\". [...] "
            "Other scholars agree with Fisher that Mendel's various observations come uncomfortably close to Mendel's expectations. [...] "
            "Fisher's analysis gave rise to the Mendelian paradox: Mendel's reported data are, statistically speaking, too good to be true, yet \"everything we know about Mendel suggests that he was unlikely to engage in either deliberate fraud or in an unconscious adjustment of his observations\". "
            "Several writers have attempted to resolve this paradox. One attempted explanation invokes confirmation bias.",
            nome="Gregor Mendel")],
    },
    # 2 o DNA foi isolado pela primeira vez do pus de ataduras
    {
        "temas_secundarios": ["historia_medicina", "sistema_imunologico"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "Os ácidos nucleicos, a família química do DNA, foram isolados pela primeira vez em 1869 a partir de pus. O suíço Friedrich Miescher recolhia ataduras usadas de um hospital para estudar os glóbulos brancos.",
        "explicacao": (
            "Miescher queria entender a química do núcleo das células. A primeira ideia era usar linfócitos, mas eles "
            "eram difíceis de obter em quantidade, e Felix Hoppe-Seyler, dono do laboratório da Universidade de "
            "Tübingen onde ele trabalhava, o incentivou a estudar os neutrófilos. Esses glóbulos brancos estão entre "
            "os primeiros e principais componentes do pus, e um hospital vizinho tinha ataduras de sobra. O problema "
            "era soltar as células do pano sem danificá-las. Miescher testou várias soluções de sais até chegar a uma "
            "com sulfato de sódio. Como ainda não havia centrífugas, ele deixava as células assentarem no fundo de um "
            "béquer e depois tentava separar os núcleos do resto. Desses núcleos, extraiu substâncias ricas em "
            "fosfato, que chamou de nucleína, hoje conhecidas como ácidos nucleicos. O resultado foi publicado em "
            "1871, e a importância dele não ficou clara de imediato. Mais tarde, Miescher chegou a sugerir que os "
            "ácidos nucleicos poderiam ter papel na herança e que talvez existisse algo como um alfabeto capaz de "
            "explicar a variação entre os seres. O trabalho dele abriu caminho para a identificação do DNA como o "
            "portador da herança."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Friedrich_Miescher",
            "He was the first scientist to isolate nucleic acid in 1869. [...] "
            "Miescher had isolated various phosphate-rich chemicals, which he called nuclein (now nucleic acids), from the nuclei of white blood cells in Felix Hoppe-Seyler's laboratory at the University of Tübingen, Germany, paving the way for the identification of DNA as the carrier of inheritance. "
            "The significance of the discovery, first published in 1871, was not at first apparent [...] "
            "Later, Miescher raised the idea that the nucleic acids could be involved in heredity and even posited that there might be something akin to an alphabet that might explain how variation is produced. [...] "
            "Miescher was interested in studying the chemistry of the nucleus. "
            "Lymphocytes were difficult to obtain in sufficient numbers to study, while neutrophils were known to be one of the main and first components in pus and could be obtained from bandages at the nearby hospital. "
            "However, the problem was washing the cells off the bandages without damaging them. [...] "
            "Miescher devised different salt solutions, eventually producing one with sodium sulfate. "
            "The cells were filtered, and since centrifuges were not available at the time, the cells were allowed to settle to the bottom of a beaker. "
            "He then tried to isolate the nuclei free of cytoplasm. [...] "
            "Miescher originally wanted to study lymphocytes, but was encouraged by Felix Hoppe-Seyler to study neutrophils.",
            nome="Friedrich Miescher")],
    },
    # 3 o paradoxo do valor C: cebola e Paris japonica
    {
        "temas_secundarios": ["plantas", "evolucao"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Tamanho do genoma não mede complexidade: o da cebola é maior que o humano, e o de uma flor japonesa, a Paris japonica, é cerca de 50 vezes maior. Boa parte do excesso, em muitas espécies, parece ser DNA \"lixo\".",
        "explicacao": (
            "Os biólogos chamam de valor C a quantidade de DNA de um conjunto de cromossomos de uma espécie. "
            "Imaginava-se que ele acompanhasse a complexidade do organismo, mas em meados do século XX ficou claro que "
            "até espécies aparentadas podiam ter genomas de tamanhos muito diferentes. Entre os animais, o valor C "
            "varia mais de 3.300 vezes; entre as plantas terrestres, cerca de mil vezes. Alho e cebola têm genomas "
            "maiores que o humano, de cerca de 3,1 bilhões de pares de bases. A Paris japonica, planta de regiões "
            "subalpinas do Japão, tem cerca de 150 bilhões e passou o recorde anterior, do peixe pulmonado "
            "marmorizado, com 130 bilhões. Depois disso, mediu-se uma samambaia, Tmesipteris truncata, com cerca de "
            "160 bilhões. A falta de relação entre tamanho e complexidade ganhou o nome de \"paradoxo do valor C\". O "
            "principal da questão foi resolvido no fim dos anos 1960, com a descoberta do DNA repetitivo: o tamanho do "
            "genoma não reflete o número de genes, porque em muitas espécies a maior parte do excesso parece ser DNA "
            "\"lixo\". Ainda assim, vários enigmas sobre por que os genomas variam tanto continuam em aberto."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("C-value",
                "In animals they range more than 3,300-fold, and in land plants they differ by a factor of about 1,000. [...] "
                "Variation in C-values has no bearing on the complexity of an organism or the number of genes contained within; for example, both garlic and onions have a genome that is larger than the human genome. "
                "This observation was deemed counterintuitive before the discovery of repetitive DNA. It became known as the C-value paradox as a result. [...] "
                "The discovery of repetitive DNA in the late 1960s resolved the main question of the C-value paradox: genome size does not reflect gene number in eukaryotes since most of the excess DNA in many species appears to be junk DNA. [...] "
                "the various puzzles that remain with regard to genome size variation",
                nome="C-value"),
            wiki("Paris_japonica",
                "It is native to sub-alpine regions of Japan. [...] "
                "Paris japonica is the previous record-holder of the largest genome of any plant yet assayed, about 150 billion base pairs long. [...] "
                "With 150 billion base pairs of DNA in the haploid genome (50 times larger than that of a human haploid genome). "
                "The flower has 19 billion more base pairs than the previous record holder, the marbled lungfish, whose 130 billion base pairs weigh in at 132.83 picograms per cell. "
                "Since then, other organisms have been assayed and reported to have larger genomes;  The fork fern, Tmesipteris truncata has 160.45 billion base pairs per cell.",
                nome="Paris japonica"),
            wiki("Genome_size",
                "Genome size in eukaryotes was thought to be proportional to the complexity of an organism but by the mid-20th century it became apparent that closely related species could differ substantially in the size of their genomes.",
                nome="Genome size"),
            wiki("Human_genome",
                "The total amount of DNA in this reference genome is 3.1 billion base pairs.",
                nome="Human genome"),
        ],
    },
    # 4 retrovírus endógenos: 5-8% do genoma é resto de vírus
    {
        "temas_secundarios": ["doencas_infecciosas", "evolucao", "microbiologia"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "Entre 5% e 8% do DNA humano é feito de restos de vírus que infectaram nossos ancestrais e ficaram no genoma. As partes que trazem a receita das proteínas ocupam só 1% a 2%.",
        "explicacao": (
            "Esses restos são os retrovírus endógenos. Para se multiplicar, um retrovírus insere uma cópia do seu "
            "genoma, em forma de DNA, no genoma da célula que infecta. Quase sempre isso acontece em células comuns "
            "do corpo, mas às vezes o vírus atinge células da linhagem germinativa, as que produzem óvulos e "
            "espermatozoides. Se dali sair um organismo viável, a cópia viral passa a ser herdada e pode se fixar na "
            "população. No genoma humano há cerca de 98 mil elementos e fragmentos assim (estimativas menores falam em "
            "3% do genoma). A maioria é só vestígio de vírus que se integraram há milhões de anos, com grandes "
            "deleções ou mutações: um estudo publicado em 2005 não achou nenhum capaz de se replicar. Uma família, a "
            "HERV-K (HML2), continuou ativa depois da separação entre humanos e chimpanzés, e há indícios de "
            "atividade nas últimas centenas de milhares de anos, já que algumas pessoas carregam mais cópias dela que "
            "outras. Nem tudo é sucata: pelo menos três desses retrovírus têm função importante comprovada, e uma "
            "proteína da HERV-K se mistura à do HIV e atrapalha a montagem da cápsula desse vírus. Para comparar, o "
            "DNA que codifica proteínas é só 1% a 2% do genoma."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Endogenous_retrovirus",
                "They are abundant in the genomes of jawed vertebrates, and comprise up to 5–8% of the human genome (lower estimates of 3%). [...] "
                "The replication cycle of a retrovirus entails the insertion (\"integration\") of a DNA copy of the viral genome into the nuclear genome of the host cell. "
                "Most retroviruses infect somatic cells, but occasional infection of germline cells (cells that produce eggs and sperm) can also occur. "
                "Rarely, retroviral integration may occur in a germline cell that goes on to develop into a viable organism. [...] "
                "When integration of viral DNA occurs in the germ-line, it can give rise to an ERV, which can later become fixed in the gene pool of the host population. [...] "
                "A gag protein from HERV-K(HML2) is shown to mix with HIV Gag, impairing HIV capsid formation as a result. [...] "
                "Nevertheless, one family of viruses has been active since the divergence of humans and chimpanzees. "
                "This family, termed HERV-K (HML2), makes up less than 1% of HERV elements but is one of the most studied. "
                "There are indications it has even been active in the past few hundred thousand years, e.g., some human individuals carry more copies of HML2 than others. [...] "
                "HERVs comprise a significant part of the human genome, with approximately 98,000 ERV elements and fragments making up 5–8%. "
                "According to a study published in 2005, no HERVs capable of replication had been identified; all appeared to be defective, containing major deletions or nonsense mutations (not true for HERV-K). "
                "This is because most HERVs are merely traces of original viruses, having first integrated millions of years ago.",
                nome="Endogenous retrovirus"),
            wiki("Human_genome",
                "The total amount of coding DNA is about 1-2% of the genome. [...] "
                "Some of these sequences represent endogenous retroviruses, DNA copies of viral sequences that have become permanently integrated into the genome and are now passed on to succeeding generations. "
                "There are also a significant number of retroviruses in human DNA, at least 3 of which have been proven to possess an important function",
                nome="Human genome"),
        ],
    },
    # 5 McClintock e os genes saltadores
    {
        "temas_secundarios": ["plantas", "personagens_esquecidos", "domesticacao"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Nos anos 1940, Barbara McClintock viu no milho genes que mudavam de lugar. A ideia causou estranheza, e o Nobel só veio em 1983. Hoje se sabe que genes saltadores e seus restos são mais da metade do nosso DNA.",
        "explicacao": (
            "McClintock dedicou a carreira à genética do milho. No início de 1948, ela percebeu que dois elementos, "
            "que chamou de Dissociation (Ds) e Activator (Ac), podiam mudar de posição no cromossomo. A pista estava "
            "nos grãos: ela acompanhou os padrões de cor ao longo de gerações de cruzamentos controlados. Quando o Ds "
            "saía do lugar, um gene da cor do grão deixava de ser suprimido por ele. McClintock propôs que esses "
            "\"elementos controladores\" regulavam genes, o que desafiava a visão do genoma como um conjunto fixo de "
            "instruções. Ela descreveu a reação dos colegas como \"perplexidade e, em alguns casos, hostilidade\" e, a "
            "partir de 1953, deixou de publicar sobre o tema. O quadro mudou nos anos 1960, quando François Jacob e "
            "Jacques Monod descreveram a regulação do operon lac, conceito que ela tinha demonstrado com o Ac/Ds em "
            "1951, e outros cientistas confirmaram os mecanismos que ela vira. O Nobel de Fisiologia ou Medicina de "
            "1983 premiou a descoberta mais de 30 anos depois da primeira descrição; até 2025, ela continuava sendo a "
            "única mulher a receber esse prêmio sem dividi-lo. O historiador Nathaniel Comfort, porém, contesta a "
            "ideia de que ela tenha sido marginalizada pelos colegas e chama essa narrativa de \"mito McClintock\". Os "
            "transposons, com seus restos sem função, somam mais da metade do DNA humano."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Barbara_McClintock",
                "In early 1948, she made the surprising discovery that both Dissociation and Activator could transpose, or change position, on the chromosome. "
                "She observed the effects of the transposition of Ac and Ds by the changing patterns of coloration in maize kernels over generations of controlled crosses [...] "
                "When Ds moves, the aleurone-color gene is released from the suppressing effect of the Ds [...] "
                "McClintock's discovery challenged the concept of the genome as a static set of instructions passed between generations. [...] "
                "she described the reception of her research as \"puzzlement and, in some instances, hostility\". [...] "
                "Based on the reactions of other scientists to her work, McClintock felt she risked alienating the scientific mainstream, and from 1953 was forced to stop publishing accounts of her research on controlling elements. [...] "
                "The importance of McClintock's contributions was revealed in the 1960s, when the work of French geneticists François Jacob and Jacques Monod described the genetic regulation of the lac operon, a concept she had demonstrated with Ac/Ds in 1951. [...] "
                "McClintock's research became well understood in the 1960s and 1970s, as other scientists confirmed the mechanisms of genetic change and protein expression that she had demonstrated in her maize research in the 1940s and 1950s. "
                "Awards and recognition for her contributions to the field followed, including the Nobel Prize in Physiology or Medicine, awarded to her in 1983 for the discovery of genetic transposition; as of 2025, she remains the only woman who has received an unshared Nobel Prize in that category. [...] "
                "It was given to her by the Nobel Foundation for discovering \"mobile genetic elements\"; this was more than 30 years after she initially described the phenomenon of controlling elements. [...] "
                "Comfort's biography contests the claim that McClintock was marginalized by other scientists, which he calls the \"McClintock Myth\"",
                nome="Barbara McClintock"),
            wiki("Human_genome",
                "Together with non-functional relics of old transposons, they account for over half of total human DNA. "
                "Sometimes called \"jumping genes\", transposons have played a major role in sculpting the human genome.",
                nome="Human genome"),
        ],
    },
    # 6 HeLa: as células imortais que contaminaram laboratórios
    {
        "temas_secundarios": ["historia_medicina", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Células do tumor de Henrietta Lacks, tiradas sem consentimento em 1951, se multiplicam até hoje em laboratórios. São tão vigorosas que contaminaram outras culturas, e um biólogo propôs que viraram uma nova espécie.",
        "explicacao": (
            "Henrietta Lacks, afro-americana de 31 anos, foi internada no Hospital Johns Hopkins, nos EUA, e tratada "
            "de um câncer do colo do útero. Em 8 de fevereiro de 1951, sem que ela fosse avisada ou consentisse, uma "
            "amostra do tumor foi para o biólogo George Gey. Até então, células humanas em cultura sobreviviam poucos "
            "dias, mas aquelas continuaram se dividindo. Henrietta morreu em outubro do mesmo ano. A linhagem, "
            "batizada de HeLa, serviu por exemplo para testar a vacina de Jonas Salk contra a pólio. O vigor teve um "
            "efeito colateral: as células HeLa se adaptam bem às placas de cultura, invadem e superam outras "
            "linhagens, e estimativas indicam que de 10% a 20% das linhagens celulares estão contaminadas por elas. "
            "Além disso, têm de 76 a 80 cromossomos, um número que não é o humano. Por isso o biólogo evolutivo Leigh "
            "Van Valen as descreveu como uma nova espécie, Helacyton gartleri, proposta que outros especialistas não "
            "levaram a sério. A genética trouxe outro capítulo: em 2013, o genoma de uma linhagem HeLa foi publicado "
            "sem o conhecimento da família, que temia o que ele revelaria sobre filhos e netos de Henrietta. No mesmo "
            "ano, um acordo com o NIH deu à família algum controle sobre o acesso a esses dados."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("HeLa",
                "It is the oldest human cell line and one of the most commonly used. [...] "
                "The cell line is derived from cervical cancer cells extracted from the tumorous mass of Henrietta Lacks,  a 31-year-old African-American woman at the time, without patient notification or consent; this had occurred on February 8, 1951. [...] "
                "Lacks died of cervical cancer on October 4, 1951. [...] "
                "Cell biologist George Otto Gey developed Lacks's cell line upon noticing that her adenocarcinoma cells were particularly easy to be kept alive and multiply. "
                "Previously, cells cultured from other human cells would survive for only a few days, but cells from Lacks's tumor behaved differently, living for a very long time. [...] "
                "HeLa cells were used by Jonas Salk to test the first polio vaccine in the 1950s. [...] "
                "HeLa cells are sometimes difficult to control, because they adapt to growth in tissue culture plates and invade and outcompete other cell lines. [...] "
                "It has been shown that a substantial fraction of in vitro cell lines are contaminated with HeLa cells; estimates range from 10% to 20%. [...] "
                "Roughly speaking, the HeLa karyotype contains 76–80 total chromosomes [...] "
                "HeLa cells were described by evolutionary biologist Leigh Van Valen as an example of the contemporary creation of a new species, dubbed Helacyton gartleri, owing to their ability to replicate indefinitely and their non-human number of chromosomes. [...] "
                "However, this proposal was not taken seriously by other prominent evolutionary biologists, nor by scientists in other disciplines. [...] "
                "The complete genome and transcriptome of the Kyoto strain of HeLa cells were sequenced and published on 11 March 2013, without the Lacks family's knowledge.",
                nome="HeLa"),
            wiki("Henrietta_Lacks",
                "There were objections from the Lacks family about the genetic information that was available for public access. [...] "
                "what information they can obtain from her sequencing that will tell them about her children and grandchildren and going down the line.\" [...] "
                "In August 2013, an agreement was announced between the family and the NIH that gave the family some control over access to the cells' DNA sequence found in the two studies",
                nome="Henrietta Lacks"),
        ],
    },
    # 7 a mãe quimera: Karen Keegan
    {
        "temas_secundarios": ["sistema_imunologico", "desenvolvimento_humano"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Exames para um transplante de rim indicaram que Karen Keegan não era a mãe biológica de dois dos filhos que ela deu à luz. A explicação: ela era uma quimera, formada pela fusão de dois embriões.",
        "explicacao": (
            "O caso foi descrito em 2002 no New England Journal of Medicine. Karen precisava de um rim, e a família "
            "fez a tipagem dos genes HLA, que pesam na compatibilidade de transplantes. O sangue dela mostrava uma "
            "versão herdada do pai e uma da mãe. Dos três filhos, um tinha o esperado, mas os outros dois traziam uma "
            "versão do avô materno que ela não parecia ter. A pista veio de outros tecidos: em amostras de pele, "
            "folículos de cabelo, tireoide, bexiga e mucosa da boca, apareceram também as versões que faltavam. A "
            "explicação mais razoável é que a mãe de Karen liberou dois óvulos ao mesmo tempo, cada um fecundado por "
            "um espermatozoide, e os dois embriões se fundiram logo no início. Ela é uma quimera tetragamética, "
            "formada a partir de quatro gametas, como dois gêmeos não idênticos num corpo só. Não se sabe por que a "
            "medula óssea, de onde vem o sangue, tinha só uma das linhagens. O caso teve um lado bom: com os quatro "
            "conjuntos de antígenos de transplante, ela podia receber o rim de qualquer um dos irmãos ou da mãe sem "
            "medo de rejeição. A maioria das quimeras humanas passa a vida sem saber que é uma."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": "https://biology-pages.info/M/Mosaics.html",
             "titulo": "Genetic Mosaics (Kimball's Biology Pages)",
             "idioma": "en",
             "trecho": (
                "A report by Yu, et. al. in the May 16, 2002 issue of The New England Journal of Medicine documents the discovery of a tetragametic woman; that is a woman derived from four different gametes, not just two. "
                "She came to the doctors' attention because she needed a kidney transplant. "
                "Tissue typing, which is done with blood cells, showed her to have inherited the \"1\" HLA region of her father (who was 1,2) and the \"3\" region of her mother (who was 3,4). [...] "
                "Of her three sons, One was 1,6 which was to be expected, but the other two were both 2,5. "
                "The 5 they got from their father, but where did the 2 come from? "
                "The first thought was that she could not have been their mother, but clearly she knew better. [...] "
                "DNA analysis of her skin cells, hair follicles, thyroid cells, bladder cells, and cells scraped from inside her mouth revealed not only 1 and 3 but also 2 and 4. "
                "It is not clear why her bone marrow was an exception - containing only 1,3 stem cells. [...] "
                "The most reasonable explanation is that Her mother had simultaneously ovulated two eggs [...] "
                "Soon thereafter the resulting early embryos fused into a single embryo. [...] "
                "The HLA region on chromosome 6 carries a set of genes that encode the major transplantation antigens; that is, the antigens that trigger graft rejection. [...] "
                "But because this woman has all four sets of transplantation antigens, she can accept a kidney from any one of her brothers as well as her mother (her father was dead) without fear of rejecting it."
             )},
            wiki("Chimera_(genetics)",
                "Most human chimeras will go through life without realizing they are chimeras. [...] "
                "Another case was that of Karen Keegan, who was also suspected (initially) of not being her children's biological mother, after DNA tests on her adult sons for a kidney transplant she needed seemed to show that she was not their mother. [...] "
                "Put another way, the chimera is formed from the merging of two nonidentical twins.",
                nome="Chimera (genetics)"),
        ],
    },
    # 8 o assassino do Golden State e a genealogia genética
    {
        "temas_secundarios": ["leis_julgamentos", "algoritmos"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "O \"assassino do Golden State\", autor de 13 assassinatos na Califórnia entre 1974 e 1986, foi preso em 2018 graças a parentes distantes que tinham posto o próprio DNA num site de genealogia.",
        "explicacao": (
            "Joseph James DeAngelo, ex-policial, também cometeu ao menos 51 estupros e pelo menos 120 roubos. A "
            "investigação durou décadas: em 2001, o DNA mostrou que duas séries de crimes com apelidos diferentes "
            "eram obra da mesma pessoa, mas o autor seguia sem nome. A virada veio quando os investigadores enviaram "
            "o perfil genético do criminoso, tirado de um kit de exame de estupro guardado no condado de Ventura, ao "
            "site de genealogia GEDmatch. O site apontou de 10 a 20 pessoas que tinham os mesmos tetravós que ele. "
            "Com a genealogista Barbara Rae-Venter, a equipe montou cerca de 25 árvores genealógicas; a que levou a "
            "ele tinha aproximadamente mil pessoas. Usando idade, sexo e local de moradia, os investigadores foram "
            "descartando nomes até restar só DeAngelo. Em abril de 2018, colheram o DNA dele às escondidas, na "
            "maçaneta do carro e num lenço de papel jogado no lixo, e as amostras bateram com as dos crimes. A técnica, "
            "chamada genealogia genética forense, se popularizou depois do caso, mas também gerou críticas sobre o "
            "uso de dados pessoais. Um artigo publicado na Science em 2018 estimou que uma busca desse tipo, para "
            "qualquer pessoa de ascendência europeia, acharia um primo de terceiro grau ou parente mais próximo em 60% "
            "das vezes."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Joseph_James_DeAngelo",
                "is an American serial killer, serial rapist, and former police officer known as the Golden State Killer [...] "
                "who committed thirteen murders and numerous rapes and burglaries across California between 1974 and 1986. "
                "DeAngelo's crimes began in Northern California, where he committed a minimum of 120 burglaries and one murder in the San Joaquin Valley, before moving to Sacramento County, where he committed at least 51 rapes [...] "
                "In 2001, DNA testing indicated that the \"East Area Rapist\" and the \"Original Night Stalker\" were the same person [...] "
                "Once they uploaded the killer's DNA profile from a Ventura County rape kit to the personal genomics website GEDmatch. "
                "The website identified 10 to 20 people who had the same great-great-great-grandparents as the Golden State Killer; a team of five investigators working with genealogist Barbara Rae-Venter used this list to construct a large family tree. [...] "
                "investigators built about 25 different family trees. "
                "The tree that eventually linked to [DeAngelo] alone contained approximately 1,000 people. "
                "Over the course of a few months, investigators used other clues like age, sex, and place of residence to rule out suspects populating these trees, eliminating suspects one by one until only DeAngelo remained.\" "
                "On April 18, 2018, a DNA sample was surreptitiously collected from the door handle of DeAngelo's car; another sample was later collected from a tissue found in DeAngelo's curbside garbage can. "
                "Both were matched to samples associated with Golden State Killer crimes. [...] "
                "On the afternoon of April 24, 2018, Sacramento County Sheriff's deputies arrested DeAngelo",
                nome="Joseph James DeAngelo"),
            wiki("Genetic_genealogy",
                "This investigative, or forensic, genetic genealogy technique became popular after the arrest of the alleged Golden State Killer in 2018, but has received significant backlash [...] "
                "In 2018, a paper in Science Magazine estimated that a DNA genealogy search on anybody of European descent would result in a third cousin or closer match 60% of the time.",
                nome="Genetic genealogy"),
        ],
    },
    # 9 persistência da lactase: digerir leite adulto é a exceção
    {
        "temas_secundarios": ["domesticacao", "evolucao", "pre_historia"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Para a maior parte da humanidade, digerir leite fica difícil depois da infância, como nos outros mamíferos. Quem segue digerindo carrega uma novidade genética recente, que surgiu mais de uma vez, em lugares diferentes.",
        "explicacao": (
            "A lactose do leite é quebrada pela enzima lactase. Na maioria dos mamíferos, a atividade dessa enzima "
            "despenca depois do desmame, quando o leite sai da dieta. Entre os humanos, a maior parte das pessoas do "
            "mundo também perde essa capacidade e, adulta, tem algum grau de intolerância à lactose. A persistência da "
            "lactase surgiu em algumas populações como adaptação ao consumo de leite de outros animais. As variantes "
            "responsáveis não ficam no gene da lactase, mas numa região vizinha, dentro de outro gene, que funciona "
            "como um intensificador da atividade dele. E variam conforme a região: uma é muito frequente no norte da "
            "Europa; outras aparecem sobretudo no leste e no norte da África e no Oriente Médio. É um caso de evolução "
            "convergente, com várias origens. Caçadores-coletores de antes da Revolução Neolítica eram, em sua imensa "
            "maioria, intolerantes, e as variantes mais antigas só chegaram a frequências relevantes nos últimos 10 "
            "mil anos. Em populações do leste da África, a persistência foi de quase ausente a quase universal em só "
            "3 mil anos, sinal de uma seleção muito forte, cujo motivo exato ainda não se conhece. Quem não tem essas "
            "variantes ainda pode tolerar queijo e iogurte, porque a fermentação já quebrou parte da lactose."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Lactase_persistence",
            "Lactase persistence or lactose tolerance is the continued activity of the lactase enzyme in adulthood, allowing the digestion of lactose in milk. "
            "In most mammals, the activity of the enzyme is dramatically reduced after weaning. "
            "In some human populations though, lactase persistence has recently evolved as an adaptation to the consumption of nonhuman milk and dairy products beyond infancy. "
            "Lactase persistence is very high among northern Europeans. "
            "Worldwide, most people are lactase non-persistent, and are affected by varying degrees of lactose intolerance as adults. [...] "
            "They are all located in a region of the gene MCM6 upstream of LCT. "
            "This region is considered as an enhancer region for the transcription of LCT. [...] "
            "The T/G*-13915 allele is found mostly in populations from East and North Africa and the Middle East. "
            "The allele G/C*-14010 was identified in East Africa. [...] "
            "these show that lactase persistence has multiple origins in different parts of the world (i.e. it is an example of convergent evolution). [...] "
            "Hunter-gatherer populations before the Neolithic Revolution were overwhelmingly lactose intolerant, as are modern hunter-gatherers. "
            "Genetic studies suggest that the oldest alleles associated with lactase persistence only reached appreciable levels in human populations in the last 10,000 years. [...] "
            "The evolutionary processes driving the rapid spread of lactase persistence in some populations are not known. "
            "Among some populations inhabiting East Africa, lactase persistence has gone from negligible to near-ubiquitous frequencies in just 3000 years, suggesting a very strong selective pressure. [...] "
            "Individuals may lack the alleles for lactase persistence, but still tolerate dairy products in which lactose is broken down by the fermentation process (e.g. cheese, yoghurt).",
            nome="Lactase persistence")],
    },
    # 10 Eva mitocondrial e Adão do Y não foram um casal
    {
        "temas_secundarios": ["pre_historia", "evolucao"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "A \"Eva mitocondrial\", ancestral de todos nós pela linha materna, e o \"Adão do cromossomo Y\", pela paterna, muito provavelmente não foram um casal. Nem precisam ter vivido na mesma época.",
        "explicacao": (
            "As mitocôndrias passam só de mãe para filhos, e o cromossomo Y só de pai para filho. Seguindo essas "
            "linhas para trás, todas as pessoas vivas convergem numa única mulher, e todos os homens vivos, num único "
            "homem. Como quem ocupa cada posto depende de quais famílias deixaram descendentes, os dois não precisam "
            "ter sido contemporâneos, e as estimativas já oscilaram muito. Um estudo de 2000 pôs o Adão cerca de 84 mil "
            "anos depois da Eva; um de março de 2013 concluiu o oposto, com a Eva uns 140 mil anos depois. A "
            "descoberta, em 2013, de uma linhagem de Y mais antiga, a A00, empurrou o Adão para trás: por estimativas "
            "de 2015, ele viveu há algo entre 200 mil e 300 mil anos, enquanto a separação ligada à Eva foi estimada, "
            "em 2013, em cerca de 155 mil anos. Outro equívoco comum é imaginar que a Eva era a única mulher do seu "
            "tempo. O DNA do núcleo indica que a população efetiva de humanos antigos nunca caiu abaixo de dezenas de "
            "milhares; outras mulheres da época podem ter descendentes hoje, só que não por uma linha exclusiva de "
            "mães. E o título nem é fixo: quando a linhagem de uma filha da Eva some, ele passa para uma descendente "
            "mais recente."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Mitochondrial_Eve",
                "As of 2013, estimates on the age of this split ranged at around 155,000 years ago [...] "
                "As the identity of both matrilineal and patrilineal MRCAs is dependent on genealogical history (pedigree collapse), they need not have lived at the same time. [...] "
                "One common misconception surrounding Mitochondrial Eve is that since all women alive today descended in a direct unbroken female line from her, she must have been the only woman alive at the time. "
                "However, nuclear DNA studies indicate that the effective population size of ancient humans never dropped below tens of thousands. "
                "Other women living during Eve's time may have descendants alive today but not in a direct female line. [...] "
                "When the mitochondrial lineages of daughters of Mitochondrial Eve die out, then the title of \"Mitochondrial Eve\" shifts forward from the remaining daughter through her matrilineal descendants [...] "
                "Sometimes Mitochondrial Eve is assumed to have lived at the same time as Y-chromosomal Adam (from whom all living males are descended patrilineally), and perhaps even met and mated with him. "
                "Even if this were true, which is currently regarded as highly unlikely, this would only be a coincidence. [...] "
                "A recent study (March 2013) concluded however that \"Eve\" lived much later than \"Adam\" – some 140,000 years later.",
                nome="Mitochondrial Eve"),
            wiki("Y-chromosomal_Adam",
                "Thomson et al. 2000, which proposed an age of about 59,000. "
                "This date suggested that the Y-MRCA lived about 84,000 years after his female counterpart mt-MRCA [...] "
                "As of 2018, this is haplogroup A00 (discovered in 2013). [...] "
                "the discovery of the archaic Y-haplogroup has pushed back the estimated age of the Y-MRCA beyond the most likely age of the mt-MRCA. "
                "As of 2015, estimates of the age of the Y-MRCA range around 200,000 to 300,000 years ago",
                nome="Y-chromosomal Adam"),
        ],
    },
    # 11 o genoma humano "completo" só em 2022
    {
        "temas_secundarios": ["historia_computacao", "invencoes"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "O genoma humano foi declarado completo em 2003, mas faltavam cerca de 8%, um volume comparável a um cromossomo inteiro. A sequência sem lacunas só saiu em 2022, e o cromossomo Y só foi concluído em 2023.",
        "explicacao": (
            "O Projeto Genoma Humano, de 3 bilhões de dólares, foi lançado oficialmente em 1990 e declarado concluído "
            "em 14 de abril de 2003. Mas o objetivo era sequenciar só as regiões de eucromatina, que somam 92,1% do "
            "genoma. Os 7,9% restantes ficam em regiões como os centrômeros e os telômeros, mais difíceis de ler e que "
            "ficaram fora dos planos originais. Nessas partes há muito DNA repetitivo, e as técnicas de leitura curta, "
            "que leem algumas centenas de letras por vez, deixavam buracos na montagem. O consórcio Telomere-to-Telomere "
            "(T2T) resolveu isso combinando dois métodos de leitura longa: um lê até 1 milhão de letras de uma vez, "
            "com precisão modesta; o outro, cerca de 20 mil, quase sem erros. Também usou uma linhagem de células com "
            "só uma cópia de cada cromossomo, quando a maioria das células humanas tem duas. A sequência completa saiu "
            "em seis artigos na revista Science em 2022. Os 8% finais incluem vários genes, e a nova referência permitiu "
            "achar mais de 2 milhões de variantes genéticas adicionais. O cromossomo Y, muito repetitivo, só teve a "
            "sequência completa publicada em agosto de 2023."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.genome.gov/news/news-release/researchers-generate-the-first-complete-gapless-sequence-of-a-human-genome",
             "titulo": "Researchers generate the first complete, gapless sequence of a human genome (NHGRI, 2022)",
             "idioma": "en",
             "trecho": (
                "Scientists have published the first complete, gapless sequence of a human genome, two decades after the Human Genome Project produced the first draft human genome sequence. [...] "
                "The T2T consortium used the now-complete genome sequence as a reference to discover more than 2 million additional variants in the human genome. [...] "
                "The full sequencing builds upon the work of the Human Genome Project, which mapped about 92% of the genome [...] "
                "Six papers encompassing the completed sequence appear in Science [...] "
                "That last 8% includes numerous genes and repetitive DNA and is comparable in size to an entire chromosome. "
                "Researchers generated the complete genome sequence using a human cell line with only one copy of each chromosome, unlike most human cells, which carry two copies of each chromosome. [...] "
                "The cost of sequencing a human genome using “short-read” technologies, which provide several hundred bases of DNA sequence at a time, is only a few hundred dollars [...] "
                "However, using these short-read methods alone still leaves some gaps in assembled genome sequences. [...] "
                "The Oxford Nanopore DNA sequencing method can read up to 1 million DNA letters in a single read with modest accuracy, while the PacBio HiFi DNA sequencing method can read about 20,000 letters with nearly perfect accuracy. "
                "Researchers in the T2T consortium used both DNA sequencing methods to generate the complete human genome sequence."
             )},
            wiki("Human_Genome_Project",
                "It was declared complete on 14 April 2003, and included about 92% of the genome. [...] "
                "In April 2022, the Telomere-to-Telomere (T2T) consortium published a complete sequence of the non-Y chromosomes, highlighting the 8% of the human genome that the HGP had not sequenced. [...] "
                "The full sequence of the Y chromosome was only published in August 2023 due to challenges with sequencing and assembling, caused by its highly repetitive nature. [...] "
                "the aim was to sequence only euchromatic regions of the nuclear genome, which make up 92.1% of the human genome. "
                "The remaining 7.9% exists in scattered heterochromatic regions such as those found in centromeres and telomeres. "
                "These regions by their nature are generally more difficult to sequence and so were not included as part of the project's original plans. [...] "
                "The $3 billion project was formally founded in 1990",
                nome="Human Genome Project"),
        ],
    },
    # 12 o gene sonic hedgehog
    {
        "temas_secundarios": ["videogames", "desenvolvimento_humano", "palavras_viajantes"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "Um gene essencial para formar o cérebro, a medula espinhal e os dedos de um embrião se chama \"sonic hedgehog\", em homenagem ao Sonic do videogame. O nome divertido virou problema na hora de falar com pacientes.",
        "explicacao": (
            "A história começa com o gene hedgehog (\"ouriço\") da mosca-das-frutas, identificado em estudos "
            "publicados em 1980 que renderam um Nobel em 1995. Sem esse gene, o embrião da mosca fica coberto de "
            "pequenas pontas, parecidas com os espinhos de um ouriço. Ao procurar equivalentes em vertebrados, "
            "pesquisadores acharam três genes. Dois ganharam nomes de espécies de ouriço: desert hedgehog e Indian "
            "hedgehog. O terceiro foi batizado por Robert Riddle, pós-doutorando no laboratório de Clifford Tabin, "
            "depois que a esposa dele chegou em casa com uma revista que trazia um anúncio do primeiro jogo do Sonic, "
            "de 1991. O gene produz um sinal cuja concentração varia ao longo do embrião e orienta o destino das "
            "células na formação de partes do cérebro, da medula espinhal, dos pulmões e dos dentes; o "
            "desenvolvimento dos membros e dos dedos depende dele. Mutações nesse gene podem causar holoprosencefalia, "
            "em que o cérebro anterior não se divide nos lados direito e esquerdo, com possíveis defeitos graves no "
            "crânio e no rosto. Por isso, alguns médicos e cientistas acharam o nome frívolo demais: falar de uma "
            "mutação no \"sonic hedgehog\" pode soar mal numa conversa sobre uma doença séria. A polêmica esfriou, e "
            "com pacientes e famílias se usam as siglas padronizadas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Sonic_hedgehog_protein",
            "Sonic hedgehog is a morphogen that patterns the developing embryo using a concentration gradient [...] "
            "Mutations in this gene can contribute to the development of holoprosencephaly, a developmental anomaly in which an embryo's forebrain fails to split the right and left sides of the brain. [...] "
            "The hedgehog gene (hh) was first identified in the fruit fly Drosophila melanogaster in the classic Heidelberg screens of Christiane Nüsslein-Volhard and Eric Wieschaus, as published in 1980. "
            "These screens, which led to the researchers winning a Nobel Prize in 1995 along with developmental geneticist Edward B. Lewis [...] "
            "The hh loss of function mutant phenotype causes the embryos to be covered with denticles, i.e. small pointy projections resembling the spikes of a hedgehog. "
            "Investigations aimed at finding a hedgehog equivalent in vertebrates by Philip Ingham, Andrew P. McMahon and Clifford Tabin revealed three homologous genes. "
            "Two of these genes, desert hedgehog and Indian hedgehog, were named for species of hedgehogs,  while sonic hedgehog was named after the video game character Sonic the Hedgehog. "
            "The gene was named by Robert Riddle, a postdoctoral fellow at the Tabin Lab, after his wife Betsy Wilder came home with a magazine containing an advert for the first game in the series, Sonic the Hedgehog (1991). [...] "
            "acting as a morphogen involved in patterning many systems—including the anterior pituitary, pallium of the brain, spinal cord, lungs, teeth and the thalamus [...] "
            "In vertebrates, the development of limbs and digits depends on the secretion of sonic hedgehog [...] "
            "The gene has been linked to a condition known as holoprosencephaly, which can result in severe brain, skull and facial defects, causing a few clinicians and scientists to criticize the name on the grounds that it sounds too frivolous. "
            "It has been noted that mention of a mutation in a sonic hedgehog gene might not be well received in a discussion of a serious disorder with a patient or their family. [...] "
            "This controversy has largely died down [...] "
            "is largely avoided by using standardized abbreviations when speaking with patients and their families.",
            nome="Sonic hedgehog protein")],
    },
    # 13 Ricardo III: o DNA mitocondrial bateu, o Y não
    {
        "temas_secundarios": ["europa_medieval", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "O esqueleto de Ricardo III, achado em 2012 sob um estacionamento, foi identificado pelo DNA de descendentes da irmã dele. Já o cromossomo Y não bateu com o da linha paterna: algum pai registrado não era o biológico.",
        "explicacao": (
            "Ricardo III, último rei inglês morto em batalha, caiu em Bosworth em 1485 e foi enterrado numa cova "
            "tosca na igreja do convento de Greyfriars, em Leicester. O túmulo se perdeu depois que o convento foi "
            "fechado, em 1538, e surgiu até uma versão errada de que os ossos tinham sido jogados num rio. Antes da "
            "escavação, o historiador John Ashdown-Hill usou genealogia para achar descendentes de Ana de York, irmã "
            "do rei, por linha exclusivamente feminina, que herdam o mesmo DNA mitocondrial. Em 2012, nas valas "
            "abertas num estacionamento em Leicester, logo no primeiro dia apareceu o esqueleto de um homem na casa "
            "dos 30 anos, com escoliose e ferimentos graves. O DNA mitocondrial dele coincidiu com o de Michael Ibsen, "
            "descendente de Ana, e com o de outra descendente pela linha materna, numa linhagem relativamente rara. A "
            "geneticista Turi King comparou também o cromossomo Y, herdado de pai para filho, com o de quatro "
            "descendentes vivos de João de Gaunt pela linha masculina. Os quatro batiam entre si, mas não com o "
            "esqueleto, o que sugere uma falsa paternidade em algum ponto das 19 gerações entre Ricardo III e Henry "
            "Somerset, 5º duque de Beaufort. Pesquisas de King e colegas indicam que a taxa histórica de falsa "
            "paternidade fica em torno de 1% a 2% por geração."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Exhumation_and_reburial_of_Richard_III_of_England",
            "On 25 August 2012, in Leicester, England, the remains of Richard III, the last English king killed in battle and last king of the House of York, were discovered within the site of the former Greyfriars Friary. [...] "
            "Richard III, the final ruler of the Plantagenet dynasty, was killed on 22 August 1485 in the Battle of Bosworth Field [...] "
            "His body was taken to Greyfriars, where it was buried in a crude grave in the friary church. "
            "Following the friary's dissolution in 1538 and subsequent demolition, Richard's tomb was lost. "
            "An erroneous account arose that Richard's bones had been thrown into the River Soar at the nearby Bow Bridge. [...] "
            "On the first day, a human skeleton belonging to a man in his thirties was uncovered showing signs of severe injuries. "
            "The skeleton, which had several unusual physical features, most notably scoliosis [...] "
            "In 2005, John Ashdown-Hill announced that he had discovered the mitochondrial DNA sequence of Richard III after identifying two matrilineal descendants of Richard III's sister Anne of York. [...] "
            "It was decided to open two trenches in the Social Services car park [...] "
            "Ashdown-Hill turned instead to genealogical research to identify an all-female-line descendant of Cecily Neville, Richard's mother. [...] "
            "Analysts found a mitochondrial DNA match among the exhumed skeleton, Michael Ibsen, and a second direct maternal line descendant, who shares a relatively rare mitochondrial DNA sequence, haplogroup J1c2c. [...] "
            "Despite the matching mitochondrial DNA, geneticist Turi King continued to pursue a link between the paternally-inherited Y DNA and that of descendants of John of Gaunt. "
            "Four living male-line descendants of Gaunt have been located, and their results are a match to each other. "
            "The Y DNA from the skeleton is somewhat degraded, but proved not to match any of the living male-line relatives, suggesting that a false-paternity event had happened somewhere in the 19 generations between Richard III and Henry Somerset, 5th Duke of Beaufort; "
            "work by Turi King and others has shown that historical rates of false paternity are around 1–2% per generation.",
            nome="Exhumation and reburial of Richard III of England")],
    },
    # 14 Anna Anderson não era Anastasia
    {
        "temas_secundarios": ["revolucoes_politicas", "personagens_esquecidos"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Por décadas, Anna Anderson sustentou ser Anastasia, a filha do último czar que teria escapado do fuzilamento. Anos depois da morte dela, o DNA de um pedaço do seu intestino, guardado num hospital, desfez a história.",
        "explicacao": (
            "Anastasia foi morta com os pais e os irmãos por revolucionários bolcheviques em Iecaterimburgo, em 17 de "
            "julho de 1918, mas o local do corpo dela ficou desconhecido até 2007. Em 1920, uma jovem sem identidade "
            "tentou se matar em Berlim e foi internada; em 1922, ganhou atenção pública a alegação de que ela era uma "
            "grã-duquesa russa. Parentes e pessoas que conheciam Anastasia a chamaram de impostora, e em 1927 uma "
            "investigação paga por um irmão da czarina a identificou como Franziska Schanzkowska, operária polonesa "
            "com histórico de doença mental. Ainda assim, muita gente acreditou nela, e uma longa disputa na justiça "
            "alemã terminou sem que ela provasse ser Anastasia. Anderson morreu em 1984 e foi cremada. Depois do fim "
            "da União Soviética, os restos da família imperial foram achados: o DNA mitocondrial das ossadas femininas "
            "bateu com o do príncipe Philip, duque de Edimburgo, cuja avó materna era irmã da czarina. Os dois últimos "
            "corpos apareceram em 2007, e testes repetidos mostraram que nenhuma das quatro filhas sobreviveu. Restava "
            "um trecho de intestino de Anderson, retirado numa cirurgia em 1979 e guardado num hospital da Virgínia. O "
            "DNA dele não batia com o dos Romanov, mas batia com o de Karl Maucher, neto de uma irmã de Franziska "
            "Schanzkowska."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Anna_Anderson",
            "was an impostor who claimed to be Grand Duchess Anastasia Nikolaevna of Russia. "
            "Anastasia, the youngest daughter of the last Tsar and Tsarina of Russia, Nicholas II and Alexandra, was murdered along with her parents and siblings on 17 July 1918 by Bolshevik revolutionaries in Yekaterinburg, Russia, but the location of her body was unknown until 2007. "
            "In 1920, Anderson was institutionalized in a mental hospital after a suicide attempt in Berlin. [...] "
            "In March 1922, claims that Anderson was a Russian grand duchess received public attention. "
            "Most members of Grand Duchess Anastasia's family and those who had known her, including court tutor Pierre Gilliard, said Anderson was an impostor but others were convinced she was Anastasia. "
            "In 1927, a private investigation funded by the Tsarina's brother, Ernest Louis, Grand Duke of Hesse, identified Anderson as Franziska Schanzkowska, a Polish factory worker with a history of mental illness. "
            "After a lawsuit lasting many years, the German courts ruled that Anderson had failed to prove she was Anastasia [...] "
            "Upon her death in 1984, Anderson's body was cremated [...] "
            "After the collapse of the Soviet Union, the locations of the bodies of the Tsar, Tsarina, and all five of their children were revealed. [...] "
            "mitochondrial DNA from the female bones matched that of Prince Philip, Duke of Edinburgh, whose maternal grandmother Princess Victoria of Hesse and by Rhine was a sister of Alexandra. "
            "The bodies of Tsarevich Alexei and the remaining daughter were discovered in 2007. "
            "Repeated and independent DNA tests confirmed that the remains were the seven members of the Romanov family, and proved that none of the Tsar's four daughters survived the shooting of the Romanov family. "
            "A sample of Anderson's tissue, part of her intestine removed during an operation in 1979, had been stored at Martha Jefferson Hospital, Charlottesville, Virginia. [...] "
            "It did not match that of the Duke of Edinburgh or that of the bones, confirming that Anderson was not related to the Romanovs. "
            "However, the sample matched DNA provided by Karl Maucher, a grandson of Franziska Schanzkowska's sister, Gertrude (Schanzkowska) Ellerik",
            nome="Anna Anderson")],
    },
    # 15 Nancy Wexler e o gene de Huntington
    {
        "temas_secundarios": ["historia_medicina", "neurociencia", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Nancy Wexler, filha de uma mulher com doença de Huntington, ajudou a localizar o gene da doença estudando famílias de vilarejos à beira do lago Maracaibo, na Venezuela. Em 2020, ela contou que também tem a doença.",
        "explicacao": (
            "A doença de Huntington é hereditária e fatal. Na família da mãe de Nancy, Leonore, três irmãos dela "
            "tiveram a doença e morreram com poucos anos de diferença; o diagnóstico foi mantido em segredo, e eles "
            "eram chamados de \"nervosos\". Leonore tinha lido, erradamente, que a doença só atingia homens, e quando "
            "os sintomas dela começaram, o ex-marido escondeu o diagnóstico por cerca de um ano. Ela morreu em 1978. "
            "Nancy, psicóloga clínica cuja única formação formal em biologia foi um curso introdutório, fez a tese "
            "sobre como é viver sob o risco de ter a doença. Em povoados à beira do lago Maracaibo, como Barranquitas "
            "e Lagunetas, a doença era especialmente comum. A partir de 1979, a equipe dela fez ali um estudo de 20 "
            "anos: coletou mais de 4 mil amostras de sangue e documentou 18 mil pessoas para montar uma genealogia "
            "comum. As amostras foram decisivas para que um grupo internacional achasse o gene, na ponta do "
            "cromossomo 4, o que levou a um teste genético. Nancy e a irmã decidiram não ter filhos, e ela passou "
            "anos sem fazer o teste. Em 2020, numa entrevista ao New York Times, revelou que tem a doença."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Nancy_Wexler",
            "The daughter of someone exhibiting Huntington's, she led a research team into a remote part of Venezuela where the disease is prevalent. [...] "
            "The samples her team collected were instrumental in allowing a global collaborative research group to locate the gene that causes the disease. [...] "
            "Leonore looked up Huntington's disease (HD) at the library and read that it was a fatal, inherited disease, and (incorrectly) that it only affecting men. "
            "Leonore's three brothers, Seymour, Paul, and Jesse Sabin, all had HD and died within four years of each other. "
            "The diagnosis was kept a secret from the rest of the family for many years. "
            "The uncles were called \"nervous,\" instead of ill. "
            "When Leonore started showing symptoms of HD, her then ex-husband, Milton, kept the diagnosis from her for about a year. [...] "
            "She earned a Ph.D. in clinical psychology but instead chose to work in the field of genetics. [...] "
            "which constitutes \"[her] only formal education in biology.\" [...] "
            "Wexler did her thesis on Huntington's disease, focusing on how it felt to be at risk for the disease. [...] "
            "Wexler and the team travelled to Barranquitas and Lagunetas, two settlements on Lake Maracaibo, Venezuela, where villagers had a particularly high occurrence of Huntington's. "
            "Starting in 1979, the team conducted a twenty-year-long study in which they collected over 4,000 blood samples and documented 18,000 different individuals to work out a common pedigree. "
            "The discovery that the gene was on the tip of chromosome 4 led to the development of a test for the disease. [...] "
            "She died on Mother's Day, 1978. [...] "
            "\"When my sister and I both decided not to have children,\" she says [...] "
            "Nancy Wexler revealed in a 2020 New York Times interview that she has Huntington's disease. "
            "An episode of The Gene also tells the story of her learning she has Huntington's disease after years of not getting tested.",
            nome="Nancy Wexler")],
    },
]
