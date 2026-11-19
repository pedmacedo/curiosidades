LOTE = "2026-11-17-anatomia-01"
AREA = "corpo_medicina"
TEMA = "anatomia"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = W if idioma == "en" else "https://pt.wikipedia.org/wiki/"
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


IMPERIAL = "https://www.imperial.ac.uk/news/190943/mystery-arthritis-linked-knee-bone-three-times/"
FLINDERS = "https://researchnow.flinders.edu.au/en/publications/recently-increased-prevalence-of-the-human-median-artery-of-the-f/"
KI = "https://news.ki.se/heart-cells-replaced-throughout-life"
SCIDAILY = "https://sciencedaily.com/releases/2009/04/090402163721.htm"
NKI = "https://www.nki.nl/news-events/news/cancer-researchers-discover-new-salivary-gland/"

CANDIDATOS = [
    # 1 ossículos vindos da mandíbula
    {
        "temas_secundarios": ["evolucao", "sentidos"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "Dois dos ossinhos que transmitem o som dentro do seu ouvido já foram ossos da mandíbula dos ancestrais dos mamíferos.",
        "explicacao": (
            "O ouvido médio dos mamíferos tem três ossículos: martelo, bigorna e estribo. Nos répteis, o tímpano se "
            "liga ao ouvido interno por um único osso, a columela, equivalente ao nosso estribo, enquanto as "
            "mandíbulas têm vários ossos que os mamíferos modernos não têm. Nos répteis, nas aves e nos dinossauros, "
            "a articulação da mandíbula é formada por dois ossos pequenos, o quadrado e o articular. Ao longo da "
            "evolução dos mamíferos, esses dois ossos perderam a função na mandíbula e migraram para o ouvido médio: "
            "o quadrado virou a bigorna e o articular virou o martelo. A pista aparece até hoje no embrião, em que "
            "martelo e bigorna nascem do mesmo arco faríngeo que forma a mandíbula e a maxila. A relação foi "
            "estabelecida pelo anatomista alemão Karl Reichert em 1837, comparando embriões, décadas antes de "
            "Darwin publicar A Origem das Espécies. O resultado da mudança é uma audição bem mais sensível e capaz "
            "de captar frequências mais altas que a dos répteis."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Evolution_of_mammalian_auditory_ossicles",
            "The reptilian quadrate, articular and columella bones are homologs of the mammalian incus, malleus and stapes, respectively. [...] "
            "In reptiles (and early synapsids by association), the eardrum is connected to the inner ear via a single bone, the columella, while the upper and lower jaws contain several bones not found in modern mammals. "
            "Over the course of mammalian evolution, one bone from the upper jaw (the quadrate) and one from the lower jaw (the articular) lost their function in the jaw articulation and migrated to form the middle ear. [...] "
            "the relationship between the reptilian jaw bones and mammalian middle-ear bones was first established on the basis of embryology and comparative anatomy by Karl Bogislaus Reichert in 1837. [...] "
            "Despite publishing decades before the publication of On the Origin of Species in 1859 [...] "
            "During embryonic development, the incus and malleus arise from the same first pharyngeal arch as the mandible and maxilla [...] "
            "All non-mammalian amniotes use this system including lizards, crocodilians, dinosaurs (and their descendants the birds) and therapsids [...] "
            "The net effect of this impedance matching is to greatly increase the overall sensitivity and upper frequency limits of mammalian hearing, as compared to reptilian hearing.")],
    },
    # 2 nervo laríngeo recorrente
    {
        "temas_secundarios": ["evolucao", "animais_extremos"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "O nervo que comanda a laringe desce do cérebro até o peito, contorna a aorta e só então sobe ao pescoço. Na girafa, esse desvio passa de 4 metros.",
        "explicacao": (
            "O nervo laríngeo recorrente é um ramo do nervo vago e comanda quase todos os músculos da laringe, onde "
            "ficam as cordas vocais. Seria de esperar um caminho curto, do cérebro direto para o pescoço. Mas os "
            "nervos vagos descem até o tórax, e os laríngeos recorrentes fazem o caminho de volta: o esquerdo "
            "contorna o arco da aorta, o direito passa por baixo da artéria subclávia, e só então os dois sobem até "
            "a laringe. A explicação está na história evolutiva. Nos ancestrais parecidos com peixes, o nervo ia "
            "direto do cérebro, passando pelo coração, até as guelras, como ainda acontece nos peixes de hoje. Com o "
            "alongamento do pescoço e a descida do coração, o nervo ficou preso ao trajeto original. Na girafa, o "
            "desvio chega a cerca de 4,6 metros, e por isso o nervo é citado como evidência da evolução. O "
            "anatomista Richard Owen descreveu o trajeto completo em 1838, depois de dissecar três girafas."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Recurrent_laryngeal_nerve",
            "The recurrent laryngeal nerve (RLN), also known as nervus recurrens, is a branch of the vagus nerve (cranial nerve X) that supplies all the intrinsic muscles of the larynx, with the exception of the cricothyroid muscles. [...] "
            "The vagus nerves run down into the thorax, and the recurrent laryngeal nerves run up to the larynx. [...] "
            "the left nerve looping under the aortic arch, and the right nerve looping under the right subclavian artery, then traveling upwards. [...] "
            "The extreme detour of the recurrent laryngeal nerves, about 4.6 metres (15 ft) in the case of giraffes, has been cited as evidence of evolution, as the nerve's route would have been direct in the fish-like ancestors of modern tetrapods, traveling from the brain, past the heart, to the gills (as it does in modern fish). "
            "In evolutionary biology, the extension of the neck and lowering of the heart are understood to have left the laryngeal nerve in its original course, explaining its unusually long path. [...] "
            "In 1838, five years before he would introduce the concept of homology to biology, anatomist Richard Owen reported upon the dissection of three giraffes, including a description of the full course of the left recurrent laryngeal nerve.")],
    },
    # 3 fabela
    {
        "temas_secundarios": ["evolucao"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "Um ossinho atrás do joelho, a fabela, estava ficando raro e voltou: em cem anos, a proporção de pessoas que o têm subiu de 11% para 39%.",
        "explicacao": (
            "A fabela é um osso sesamoide, do mesmo tipo da patela: cresce dentro de um tendão, no caso o do músculo "
            "da panturrilha, atrás do joelho. Nem todo mundo tem. Pesquisadores do Imperial College London reuniram "
            "estudos que examinaram 21.676 joelhos em 27 países, desde 1875. Pelo modelo estatístico que montaram, "
            "em 1918 a fabela aparecia em 11,2% da população mundial; em 2018, em 39%, um aumento de 3,5 vezes. O "
            "autor principal, Michael Berthaume, aposta na nutrição: a pessoa média de hoje é mais bem alimentada, "
            "mais alta e mais pesada, com canelas mais longas e panturrilhas maiores, e isso aumenta a pressão sobre "
            "o joelho. A função do osso ainda é desconhecida. Ele pode reduzir o atrito no tendão, redirecionar a "
            "força do músculo ou não fazer nada. E tem desvantagens: quem tem artrose no joelho tem o dobro de chance "
            "de ter fabela, embora não se saiba se ela causa o problema."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": IMPERIAL, "titulo": "Mystery arthritis-linked knee bone three times more common than 100 years ago", "idioma": "en",
             "trecho": "The fabella, a small bone in the knee once lost to human evolution, has made a surprising resurgence over the last century. [...] "
                       "Through the analysis, published today in the Journal of Anatomy, they reviewed 21,676 individual knees over 27 countries. "
                       "The earliest records they looked at, which were from 1875, showed that fabellae were found in 17.9 per cent of the population. [...] "
                       "Their analysis showed that in 1918, fabellae were present in 11.2 per cent of the world population, and by 2018, they were present in 39 per cent [...] a 3.5-fold increase. [...] "
                       "The fabella is a sesamoid bone, meaning it grows in the tendon of a muscle: the kneecap, for instance, is the largest sesamoid bone in the human body. [...] "
                       "The average human, today, is better nourished, meaning we are taller and heavier. This came with longer shinbones and larger calf muscles [...] "
                       "People with osteoarthritis of the knee are twice as likely to have a fabella than people without osteoarthritis - however, it is unknown if the fabella causes osteoarthritis in the knee, and if so, how."},
            wiki("Fabella",
                "The fabella is a small sesamoid bone found in some mammals embedded in the tendon of the lateral head of the gastrocnemius muscle behind the lateral condyle of the femur."),
        ],
    },
    # 4 artéria mediana
    {
        "temas_secundarios": ["evolucao", "desenvolvimento_humano"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Uma artéria do antebraço que deveria sumir no embrião está ficando em cada vez mais adultos: já são cerca de 35% das pessoas, contra 10% no século XIX.",
        "explicacao": (
            "A artéria mediana passa pelo antebraço, entre as artérias radial e ulnar, acompanhando o nervo mediano. "
            "Ela é considerada uma estrutura do embrião: normalmente regride por volta da 8ª semana de gestação. Em "
            "parte das pessoas, porém, continua lá na vida adulta. Pesquisadores da Universidade Flinders, na "
            "Austrália, dissecaram 78 braços de pessoas que morreram em 2015 e 2016 e acharam a artéria em 26. "
            "Juntando esses dados à literatura antiga, viram que a frequência era de cerca de 10% entre os nascidos "
            "em meados da década de 1880 e chegou a 30% entre os nascidos no fim do século XX. Hoje estaria em 35%. "
            "Os autores levantam duas explicações possíveis: mutações em genes ligados ao desenvolvimento da artéria "
            "ou problemas de saúde das mães durante a gravidez. Se a tendência continuar, dizem, os nascidos daqui a "
            "80 anos terão todos a artéria mediana, e ela deixará de ser uma variação para virar a estrutura normal."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": FLINDERS, "titulo": "Recently increased prevalence of the human median artery of the forearm: A microevolutionary change", "idioma": "en",
             "trecho": "The median artery has been considered as an embryonic structure, which normally regresses around the 8th week of gestation. [...] "
                       "A total of 26 median arteries were found in 78 upper limbs obtained from Australians aged 51 to 101 years, who died in the period 2015–2016 [...] "
                       "Second-order polynomial regression of the median artery's prevalence on dates of birth shows that it is now present in 35% of people and predicts that people born 80 years from now will all carry a median artery if the trend continues."},
            wiki("Median_artery",
                "The prevalence was around 10% in people born in the mid-1880s compared to 30% in those born in the late 20th century [...] "
                "When the median artery prevalence reaches 50% or more, it should not be considered as a variant, but as a [...] "
                "This increase could have resulted from mutations of genes involved in median artery development or health problems in mothers during pregnancy, or both. [...] "
                "When present, it is found in the forearm, between the radial artery and ulnar artery. It runs with the median nerve and supplies the same structures as that nerve."),
        ],
    },
    # 5 córnea sem vasos
    {
        "temas_secundarios": ["sentidos", "luz_cores"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "A córnea, a janela transparente do olho, não tem vasos sanguíneos: o oxigênio que ela usa se dissolve nas lágrimas e se espalha pelo tecido.",
        "explicacao": (
            "Quase todos os tecidos do corpo recebem oxigênio e nutrientes pelo sangue. A córnea é uma exceção, e "
            "por um bom motivo: ela precisa ser transparente, e vasos sanguíneos atrapalhariam a passagem da luz. "
            "Por isso a córnea saudável não tem nem precisa de vasos. O oxigênio se dissolve nas lágrimas e se "
            "difunde pelo tecido. Os nutrientes chegam também por difusão, pelos dois lados: pela superfície de "
            "fora, a partir do líquido das lágrimas, e pela de dentro, a partir do humor aquoso, o líquido que "
            "preenche a parte da frente do olho. A camada externa da córnea é um epitélio muito fino, de células "
            "que crescem e se regeneram depressa, mantido úmido pelas lágrimas. A lisura da superfície entre o ar "
            "e o filme de lágrima importa muito: é ela o componente mais importante do poder de refração do olho, "
            "e qualquer irregularidade ali piora a visão."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Cornea",
            "Because transparency is of prime importance, the healthy cornea does not have or need blood vessels within it. Instead, oxygen dissolves in tears and then diffuses throughout the cornea to keep it healthy. [...] "
            "Similarly, nutrients are transported via diffusion from the tear fluid through the outside surface and the aqueous humour through the inside surface. [...] "
            "Corneal epithelium: an exceedingly thin multicellular epithelial tissue layer (non-keratinized stratified squamous epithelium) of fast-growing and easily regenerated cells, kept moist with tears. "
            "Irregularity or edema of the corneal epithelium disrupts the smoothness of the air/tear-film interface, the most significant component of the total refractive power of the eye, thereby reducing visual acuity.")],
    },
    # 6 cristalino: células de antes do nascimento
    {
        "temas_secundarios": ["sentidos", "desenvolvimento_humano"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "No centro do cristalino do seu olho há células formadas quando você ainda era um embrião: ele cresce a vida toda e nunca descarta as células velhas.",
        "explicacao": (
            "O cristalino, a lente que focaliza a luz dentro do olho, cresce durante toda a vida. Novas fibras são "
            "produzidas por células da sua borda, que se alongam, se enchem de proteínas chamadas cristalinas e "
            "perdem o núcleo e as demais organelas ao amadurecer. Como tudo isso acontece dentro de uma cápsula "
            "fechada, as células antigas não têm como ser eliminadas: são empurradas para o centro, e as novas se "
            "acomodam nas camadas de fora. Por isso o cristalino é organizado como uma cebola, em que a parte mais "
            "central e mais antiga é chamada de núcleo embrionário, envolvida pelo núcleo fetal e depois pelo "
            "adulto. Essa memória em camadas é útil para a ciência: o carbono radioativo espalhado pelos testes "
            "nucleares foi medido no cristalino de tubarões-da-groenlândia, incorporado durante o desenvolvimento, "
            "para estimar a idade desses animais."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Lens_(vertebrate_anatomy)",
                "As a result, the vertebrate lens grows throughout life. [...] "
                "Moving outwards from the central, oldest layer, the lens is split into an embryonic nucleus, the fetal nucleus, the adult nucleus, the inner and outer cortex. New lens fibers, generated from the lens epithelium, are added to the outer cortex. [...] "
                "The lens epithelial cells elongate, lose contact with the capsule and epithelium at the back and front of the lens, synthesize crystallin, and then finally lose their nuclei (enucleate) as they become mature lens fibers. [...] "
                "The whole process of differentiation of the epithelial cells into crystallin filled fiber cells without organelles occurs within the confines of the lens capsule. Older cells cannot be shed and are instead internalized towards the center of the lens.",
                nome="Lens (vertebrate anatomy)"),
            wiki("Bomb_pulse",
                "The bomb pulse has also been used to estimate the age of Greenland sharks by measuring the incorporation of 14C in the eye lens during development."),
        ],
    },
    # 7 apêndice
    {
        "temas_secundarios": ["microbioma", "evolucao"],
        "tipos_espanto": ["mito_desmentido", "misterio_aberto"],
        "gancho": "O apêndice, tido como resto inútil, surgiu de forma independente de 32 a 38 vezes na evolução dos mamíferos. Uma hipótese: ele guarda bactérias boas do intestino.",
        "explicacao": (
            "Por muito tempo o apêndice foi visto como um órgão vestigial, sem função. Dois tipos de pista "
            "mudaram essa visão. A primeira vem da evolução: um estudo de 2013 estimou que o apêndice surgiu de "
            "forma independente de 32 a 38 vezes em diferentes animais e foi perdido no máximo seis vezes. Em "
            "pelo menos um grupo, ele se mantém há mais de 80 milhões de anos. Estruturas que somem e reaparecem "
            "tanto costumam ter alguma utilidade. A segunda pista é a hipótese proposta em 2007 por William Parker, "
            "Randy Bollinger e colegas da Universidade Duke: o apêndice serviria de abrigo para bactérias "
            "benéficas quando uma doença ou um antibiótico as expulsa do intestino. Ele fica logo abaixo do fluxo "
            "de mão única da comida e dos germes no intestino grosso, tem muito tecido imunológico e, depois de uma "
            "infecção intestinal, poderia repovoar a flora. A ideia é aceita como plausível, mas ainda é uma "
            "hipótese."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Appendix_(anatomy)",
            "William Parker, Randy Bollinger, and colleagues at Duke University proposed in 2007 that the appendix serves as a haven for beneficial bacteria when illness or antibiotics flush them from the intestines. [...] "
            "including its architecture, its location just below the normal one-way flow of food and germs in the large intestine, and its association with copious amounts of immune tissue. [...] "
            "The appendix, therefore, may act as a reservoir for beneficial bacteria. This reservoir could repopulate the gut flora following a bout of gastrointestinal illness. [...] "
            "Although the appendix has apparently been lost by numerous species, it has also been maintained for more than 80 million years in at least one clade. "
            "A 2013 study estimated that the appendix independently evolved in different animals 32-38 times, but was lost no more than six times.",
            nome="Appendix (anatomy)")],
    },
    # 8 coração e carbono-14
    {
        "temas_secundarios": ["guerra_fria", "elementos_quimicos"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Os testes nucleares da Guerra Fria revelaram que o coração humano troca suas células, devagar: cerca de 1% por ano aos 20 anos e 0,5% aos 75.",
        "explicacao": (
            "Por muito tempo se discutiu se as células do músculo do coração eram as mesmas a vida inteira ou se "
            "eram substituídas. A resposta veio de um efeito colateral da Guerra Fria. Os testes nucleares feitos "
            "ao ar livre nas décadas de 1950 e 1960 provocaram um pico de carbono-14 radioativo na atmosfera, que "
            "foi caindo devagar depois que esses testes pararam, em 1963. O carbono-14 vai parar nas células, e o "
            "DNA de uma célula fica estável depois da última divisão. Assim, a quantidade de carbono-14 no DNA "
            "funciona como uma data de nascimento da célula. Usando esse método, pesquisadores do Instituto "
            "Karolinska, na Suécia, mostraram em 2009 que as células do coração são substituídas aos poucos: "
            "cerca de 1% por ano aos 20 anos, taxa que cai até 0,5% aos 75. Como a troca é lenta, a maioria das "
            "células nunca é substituída, e o coração vira uma colcha de retalhos de células antigas e novas."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": KI, "titulo": "Heart cells replaced throughout life", "idioma": "en",
             "trecho": "3 April 2009 [...] For instance, it has long been mooted whether heart cells remain the same throughout life or whether they are replaced [...] "
                       "In a 20-year old, one per cent of heart cells are renewed every year; this rate then gradually declines over the years, reaching 0.5 per cent in a 75-year old. "
                       "The slow rate of turnover means that the majority of heart cells remain unreplaced during a normal human lifespan, leaving the heart a patchwork of cells that have been there from birth and cells that have been formed later in life. [...] "
                       "The method exploits the fact that the nuclear tests of the Cold War produced a sharp increase in atmospheric concentrations of radioactive carbon-14."},
            {"url": SCIDAILY, "titulo": "Carbon dating shows heart cells regenerate (ScienceDaily)", "idioma": "en",
             "trecho": "from above-ground nuclear testing in the 1950s and 1960 [...] Carbon 14 atmospheric concentration levels remained relatively stable until the Cold War, when above-ground nuclear bomb tests caused a sharp increase, or peak, which decreased slowly after the end of above-ground testing in 1963. "
                       "Because DNA is stable after a cell has gone through its last cell division, the concentration of carbon 14 in DNA serves as a date mark for when a cell was born and can be used to date cells in humans."},
        ],
    },
    # 9 células de gordura
    {
        "temas_secundarios": ["desenvolvimento_humano", "guerra_fria"],
        "tipos_espanto": ["contraintuitivo", "mito_desmentido"],
        "gancho": "Na vida adulta, quem engorda ou emagrece muda sobretudo o tamanho das células de gordura, não o número: ele se define na infância e na adolescência.",
        "explicacao": (
            "É comum imaginar que emagrecer elimina células de gordura. O que acontece, na maior parte dos casos, "
            "é que elas encolhem. O número de células de gordura costuma aumentar na infância e na adolescência e "
            "se manter constante no adulto. Quem engorda depois de adulto, sem ter sido obeso antes, tem células "
            "maiores, não mais numerosas. Já quem é obeso desde a infância costuma ter um número maior delas. "
            "Parte dessa história foi desvendada com o carbono-14 deixado na atmosfera pelos testes nucleares, que "
            "permite datar células: a pesquisadora Kirsty Spalding mostrou que o número de células de gordura é "
            "fixado na infância e na adolescência, e que cerca de 10% delas são renovadas a cada ano, mantendo o "
            "total. Reduzir esse número com dieta é difícil. Há indícios de que ele pode cair se a perda de peso se "
            "mantiver por mais de um ano, algo muito difícil para quem tem células maiores e mais numerosas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Adipocyte",
                "If an adult (who never was obese as a child or adolescent) gains excess weight, fat cells generally increase in size, not number [...] "
                "According to some reports and textbooks, the number of adipocytes can increase in childhood and adolescence, though the amount is usually constant in adults. [...] "
                "People who have been fat since childhood generally have an inflated number of fat cells. [...] "
                "The number of fat cells is difficult to decrease through dietary intervention, though some evidence suggests that the number of fat cells can decrease if weight loss is maintained for a sufficiently long period of time (>1 year; though it is extremely difficult for people with larger and more numerous fat cells to maintain weight loss for that long a time)."),
            wiki("Bomb_pulse",
                "She also showed that the number of fat cells is set during childhood and adolescence. "
                "Considering the amount of 14C present in DNA she could establish that 10% of fat cells are renewed annually."),
        ],
    },
    # 10 ciclo nasal
    {
        "temas_secundarios": ["sono_ritmos", "sentidos"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Você respira mais por uma narina do que pela outra, e elas se revezam sem você perceber, num ciclo que dura em média duas horas e meia.",
        "explicacao": (
            "Dentro do nariz há estruturas chamadas conchas nasais, cobertas de tecido que pode se encher de sangue "
            "e inchar. Ao longo do dia, um lado da cavidade nasal fica parcialmente congestionado enquanto o outro "
            "desincha, e o ar passa mais por uma narina. Depois os papéis se invertem. É o ciclo nasal, controlado "
            "pelo sistema nervoso autônomo, sem nenhuma participação da vontade. A duração média é de duas horas e "
            "meia, mas varia muito com a idade, a postura e outras condições. Em 1927, o médico Heetderks observou o "
            "inchaço alternado das conchas inferiores, as maiores, em 80% de uma população normal. Um detalhe "
            "engenhoso: enquanto os lados se alternam, a resistência total do nariz à passagem do ar se mantém "
            "constante. Quem tem desvio de septo costuma sentir o ciclo: a sensação de nariz entupido muitas vezes "
            "acompanha a fase de congestão do lado mais estreito."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Nasal_cycle",
            "The nasal cycle is the subconscious alternating partial congestion and decongestion of the nasal cavities in humans and other animals. This results in greater airflow through one nostril with periodic alternation between the nostrils. [...] "
            "In 1927, Heetderks described the alternating turgescence of the inferior turbinates in 80% of a normal population. "
            "According to Heetderks, the cycle is the result of alternating congestion and decongestion of the nasal conchae or turbinates, predominantly the inferior turbinates, which are by far the largest of the turbinates in each nasal fossa. [...] "
            "This cycle, which is controlled by the autonomic nervous system, has a mean duration of two and a half hours but varies widely with age, body-posture, and other conditions. [...] "
            "The nasal cycle is an alternation in both time and between left and right sides, with the total resistance in the nose remaining constant. "
            "In patients with a fixed septal deviation and intermittent nasal obstruction, the interplay of the nasal cycle becomes evident; the sensation of obstruction frequently mirrors the congestion phase.")],
    },
    # 11 linhas de Blaschko
    {
        "temas_secundarios": ["desenvolvimento_humano", "genetica"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Sua pele tem um desenho invisível de listras: V nas costas, redemoinhos no peito, ondas na cabeça. Ele só aparece em certas doenças de pele.",
        "explicacao": (
            "As linhas de Blaschko formam um padrão que cobre o corpo todo: um V nas costas, redemoinhos em forma "
            "de S no peito e nas laterais e linhas onduladas na cabeça. Normalmente ninguém as vê. Elas aparecem em "
            "pessoas com doenças de pele em mosaico, em que grupos diferentes de células carregam genes diferentes, "
            "e que podem produzir mais ou menos melanina ou ser mais ou menos suscetíveis a uma doença. Acredita-se "
            "que as linhas registrem o caminho das células durante o desenvolvimento do embrião, e elas não "
            "correspondem a nervos, músculos ou vasos linfáticos. Quem as desenhou pela primeira vez foi Alfred "
            "Blaschko, dermatologista de Berlim, em 1901. Ele estudou mais de 140 pacientes com doenças de pele, "
            "transferiu os padrões que as lesões seguiam para bonecos e estátuas e, a partir deles, montou um "
            "esquema do corpo humano inteiro."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Blaschko's_lines",
            "These lines are only visible in those with a mosaic skin condition or in chimeras where different cell lines contain different genes. These lines may express different amounts of melanin, or become visible due to a differing susceptibility to disease. [...] "
            "They follow a V shape over the back, S-shaped whirls over the chest and sides, and wavy shapes on the head. [...] "
            "The lines are believed to trace the migration of embryonic cells. They do not correspond to underlying nervous, muscular, or lymphatic systems. [...] "
            "Alfred Blaschko, a private practice dermatologist from Berlin, first described and drew the patterns of the lines of Blaschko in 1901. "
            "He obtained his data by studying over 140 patients with various nevoid and acquired skin diseases and transposed the visible patterns the diseases followed onto dolls and statues, then compiled the patterns onto a composite schematic of the human body.",
            nome="Blaschko's lines")],
    },
    # 12 glândulas tubárias
    {
        "temas_secundarios": ["historia_medicina"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Em 2020, médicos holandeses acharam, por acaso, um par de glândulas salivares no fundo do nariz que nenhum livro de anatomia descrevia.",
        "explicacao": (
            "O radio-oncologista Wouter Vogel e o cirurgião bucomaxilofacial Matthijs Valstar, do Instituto do "
            "Câncer da Holanda, estudavam um tipo novo de exame, o PET/CT de PSMA, feito em pacientes com câncer de "
            "próstata. Nesse exame as glândulas salivares aparecem com clareza. No fundo da nasofaringe, a região "
            "atrás do nariz, duas áreas inesperadas se acenderam, parecidas com as glândulas salivares maiores já "
            "conhecidas. Até então se sabia que ali só havia glândulas microscópicas, até mil, espalhadas pela "
            "mucosa. Com colegas do Centro Médico Universitário de Utrecht, eles viram que todas as 100 pessoas "
            "cujos exames estudaram tinham o par de glândulas, que chamaram de tubárias. A descoberta tem uso "
            "prático: analisando 723 pacientes tratados com radioterapia, a equipe viu que, quanto mais radiação "
            "essas áreas recebiam, mais complicações os pacientes tinham depois. Poupar as glândulas pode reduzir "
            "efeitos colaterais do tratamento de câncer de cabeça e pescoço."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [{"url": NKI, "titulo": "Cancer researchers discover new salivary gland", "idioma": "en",
                    "trecho": "16-10-2020 [...] Imagine the surprise of radiation oncologist Wouter Vogel and oral and maxillofacial surgeon Matthijs Valstar who were studying a new type of scan as part of their research when they discovered that, all the way in the back of the nasopharynx, two unexpected areas had lit up. Areas that looked similar to known major salivary glands. [...] "
                              "As far as we knew, the only salivary or mucous glands in the nasopharynx are microscopically small, and up to 1000 are evenly spread out throughout the mucosa. [...] "
                              "In collaboration with their colleagues at UMC Utrecht, they discovered that all 100 people whose scans they studied had a set of these glands. These patients had a new type of scan done because of their prostate cancer: a PSMA PET/CT scan. [...] "
                              "the researchers analyzed the data of 723 patients who had undergone radiation treatment. Their conclusion: the more radiation delivered to these new areas, the more complications the patients experienced afterwards."}],
    },
    # 13 queixo
    {
        "temas_secundarios": ["evolucao", "pre_historia"],
        "tipos_espanto": ["misterio_aberto"],
        "gancho": "Entre os primatas, só os humanos têm queixo. Nem os neandertais tinham, e até hoje ninguém sabe ao certo para que ele serve.",
        "explicacao": (
            "Um queixo bem desenvolvido é uma das características que distinguem o Homo sapiens de outros parentes "
            "humanos, como os neandertais. Os ancestrais humanos mais antigos tinham formatos variados na frente da "
            "mandíbula, mas nenhum com um queixo de verdade. E entre os primatas vivos somos a única espécie que tem "
            "um. Por que ele surgiu é uma pergunta antiga e ainda sem resposta definitiva. Num artigo intitulado "
            "\"O enigma duradouro do queixo humano\", os antropólogos James Pampush e David Daegling revisaram as "
            "várias teorias propostas. Uma das mais estudadas é a da mastigação, que um trabalho de 2015 contestou: "
            "segundo esse estudo, o queixo não teria sido moldado por forças mecânicas como a da mastigação, mas "
            "surgiu como efeito da redução de tamanho e da mudança de forma do rosto, que ficou menor que o de "
            "outros humanos antigos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Chin",
            "The presence of a well-developed chin is considered to be one of the morphological characteristics of Homo sapiens that differentiates them from other human ancestors such as the closely related Neanderthals. "
            "Early human ancestors have varied symphysial morphology, but none of them have a well-developed chin. [...] "
            "2015 research on the development of the chin suggests that the evolution of this unique characteristic was formed not by mechanical forces such as chewing but by evolutionary adaptations involving reduction in size and change in shape of the face. "
            "They claim that this adaptation occurred as the face became smaller compared to that of other ancient humans. [...] "
            "Overall, human beings are unique in the sense that they are the only species among primates who have chins. "
            "In the paper The Enduring Puzzle of the Human Chin, evolutionary anthropologists James Pampush and David Daegling discuss various theories that have been raised to solve the puzzle of the chin.")],
    },
    # 14 branco dos olhos
    {
        "temas_secundarios": ["comportamento_animal", "psicologia_social"],
        "tipos_espanto": ["conexao_inesperada", "misterio_aberto"],
        "gancho": "O branco bem visível dos nossos olhos é raro entre os primatas. Uma hipótese: ele evoluiu para que os outros vejam para onde estamos olhando.",
        "explicacao": (
            "Nos olhos humanos há um contraste forte entre a esclera branca, a íris colorida e a pupila preta, "
            "porque a esclera não tem pigmento. Nos outros primatas ela costuma ser marrom ou escura. A hipótese do "
            "olho cooperativo, proposta em 2007 por Michael Tomasello e colegas do Instituto Max Planck de "
            "Antropologia Evolutiva, na Alemanha, diz que o branco dos olhos evoluiu para facilitar a comunicação: "
            "ele deixa claro para onde a pessoa está olhando. No experimento, os pesquisadores compararam bebês "
            "humanos com grandes macacos. Os macacos seguiam o olhar do pesquisador sobretudo quando ele virava a "
            "cabeça; os bebês, quando ele mexia só os olhos. Os humanos dependem mais do movimento dos olhos do que "
            "do da cabeça para acompanhar o olhar alheio. Há outras hipóteses: o branco dos olhos seria sinal de "
            "boa saúde, útil na escolha de parceiros, ou faria as pessoas se comportarem melhor ao saber que estão "
            "sendo observadas. Uma não exclui a outra."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Cooperative_eye_hypothesis",
            "Unlike other primates, humans have eyes with a distinct colour contrast between the white sclera, the coloured iris, and the black pupil. This is due to a lack of pigment in the sclera. "
            "Other primates mostly have pigmented sclerae that are brown or dark in colour. [...] "
            "The cooperative eye hypothesis was first proposed Michael Tomasello and colleagues in 2007 [...] "
            "The cooperative eye hypothesis was tested by Michael Tomasello and others at the Max Planck Institute for Evolutionary Anthropology in Germany. "
            "Researchers examined the effect of head and eye movement on changing gaze direction in humans and other great apes. [...] "
            "The apes were most likely to follow the gaze of the experimenter when only his head moved. The infants followed the gaze more often when only the eyes moved. "
            "The results suggest that humans depend more on eye movements than head movements when trying to follow the gaze of another. [...] "
            "Other hypotheses include the proposal that white sclerae are a sign of good health, useful in mate selection, or that eye visibility promotes altruistic behaviour by letting people know they are being watched. [...] "
            "these hypotheses are not mutually exclusive")],
    },
]
