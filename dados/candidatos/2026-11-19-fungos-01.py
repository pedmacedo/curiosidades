LOTE = "2026-11-19-fungos-01"
AREA = "biologia"
TEMA = "fungos"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Prototaxites: troncos de 8 metros que talvez fossem fungo
    {
        "temas_secundarios": ["paleontologia", "plantas"],
        "tipos_espanto": ["misterio_aberto", "escala_absurda"],
        "gancho": "Na época em que a planta Cooksonia mal chegava a 6 cm, já se erguiam em terra \"troncos\" de até 8 metros. Eram os Prototaxites, e até hoje se discute o que eram: o mais aceito é que fossem fungos gigantes.",
        "explicacao": (
            "Os fósseis de Prototaxites vão do fim do Siluriano ao fim do Devoniano. Vistos de longe, parecem troncos "
            "de árvore, com até 1 metro de diâmetro, mas por dentro são feitos de tubinhos "
            "entrelaçados, de uns 50 micrômetros. Foi, de longe, o maior organismo terrestre do seu tempo; a planta "
            "Cooksonia, da mesma época, chegava a só 6 centímetros, e os únicos outros seres complexos em terra eram "
            "invertebrados. O primeiro fóssil foi achado no Canadá em 1843, e o geólogo John William Dawson o "
            "descreveu como uma conífera gigante apodrecida, daí o nome, algo como \"primeiro teixo\". Um rival, "
            "William Carruthers, ridicularizou a ideia e sustentou que era uma alga marinha. Em 2001, depois de 20 "
            "anos de pesquisa, Francis Hueber, do Museu Nacional de História Natural, em Washington, concluiu pela "
            "anatomia que era um fungo, e a proposta foi recebida com descrença. Em 2007, isótopos de carbono "
            "reforçaram a tese: os valores variavam demais para um ser que vivesse só de fotossíntese, sinal de que "
            "ele se alimentava de outras fontes. O debate segue: um estudo de 2026 não achou quitina, peça-chave da "
            "parede dos fungos atuais, em fósseis da Escócia e propôs uma linhagem extinta à parte, conclusão que "
            "recebeu críticas por falhas de método."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [wiki("Prototaxites",
            "Prototaxites formed large trunk-like structures up to 1 metre (3 ft) wide, reaching 8 metres (26 ft) in height, "
            "made up of tiny interwoven tubules around 50 micrometres (0.0020 in) in diameter, making it by far the largest land-dwelling organism of its time. "
            "The taxonomy of Prototaxites has long been the subject of debate. It is widely considered a fungus, but the debate is ongoing. [...] "
            "is an extinct genus of large macroscopic eukaryote dating from the Late Silurian until the Late Devonian periods. [...] "
            "Viewed from afar, the fossils take the form of tree trunks [...] "
            "In 1843, Canadian geologist Sir William Edmond Logan discovered a fossil [...] "
            "John William Dawson studied Prototaxites fossils, which he described as partially rotten giant conifers [...] "
            "rival scientist and British paleobotanist William Carruthers ridiculed the idea. [...] "
            "Carruthers faulted the name Prototaxites (loosely translated as \"first yew\") [...] "
            "Carruthers' interpretation that it was a giant marine alga [...] "
            "It was not until 2001, after 20 years of research, that Francis Hueber, of the National Museum of Natural History in Washington, D.C., "
            "published a long-awaited paper that attempted to place Prototaxites taxonomically. The paper deduced, based on its morphology, that Prototaxites was a fungus. "
            "This idea was received with disbelief, denial, and strong skepticism [...] "
            "In 2007, isotopic analyses by a team including Hueber and K.C. Boyce of the University of Chicago concluded that Prototaxites was a giant fungus. "
            "They detected a highly variable range of values of carbon isotope ratios [...] "
            "The inconsistent ratio observed in Prototaxites appears to show that the organism did not have a solely photosynthetic metabolism, "
            "and Boyce's team deduced that the organism fed on a range of substrates [...] "
            "A 2026 paper found that the chemical composition of Prototaxites fossils from the Rhynie chert assemblage in Scotland is distinct from that of other organisms "
            "in the same environment – including fungi – due to lacking chitin, a key structural element in extant fungi. [...] "
            "The authors propose that Prototaxites represents a completely new extinct lineage, separate from plants, fungi and other eukaryotes. "
            "However, a recent comment to this article pointed out severe methodological errors in the analysis of the spectroscopic data [...] "
            "the contemporaneous Silurian plant Cooksonia reached only 6 centimetres (2.4 in) in height, and invertebrates were the only other land-dwelling complex multi-cellular life.",
            nome="Prototaxites")],
    },
    # 2 o fungo gigante do Oregon
    {
        "temas_secundarios": ["plantas", "animais_extremos"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Um dos maiores seres vivos da Terra é um fungo no Oregon (EUA): um único indivíduo que se espalha sob a floresta por 9,1 km², pode pesar até 35 mil toneladas e teria uns 8 mil anos.",
        "explicacao": (
            "A espécie é a Armillaria ostoyae, cujos cogumelos são chamados em inglês de \"honey mushrooms\". "
            "Quase todo o organismo fica escondido debaixo da terra. O micélio invade a madeira viva das árvores e "
            "avança por longas distâncias, sob a casca ou de uma árvore a outra, por cordões pretos, as rizomorfas, "
            "que lembram cadarços emaranhados. Só no outono ele põe para fora os cogumelos. O exemplar gigante fica "
            "na Floresta Nacional de Malheur, no leste do Oregon, e é considerado a maior colônia de fungo do mundo. "
            "Se for tratado como um só organismo, em área ele só tem um rival conhecido: uma colônia de capim "
            "marinho, a Posidonia australis, no fundo do mar da Austrália. Não é um caso isolado. Em Michigan, uma "
            "análise genética mostrou que outro indivíduo da espécie, com uns 2.500 anos, ocupa 37 hectares e pesa "
            "cerca de 440 toneladas, o equivalente a três baleias-azuis. Ele descende de esporos de um fungo do "
            "Ontário, no Canadá. O gigante não é inofensivo: é um patógeno que causa doença nas raízes de "
            "coníferas, e os pinheiros jovens, de até 10 anos, são os mais vulneráveis. Ele consegue sobreviver "
            "em tocos por 50 anos, e os tratamentos químicos não o erradicam."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Armillaria_ostoyae",
            "The mycelium invades the sapwood of trees, and is able to disseminate, like little entangled strings, over great distances under the bark "
            "or between trees in the form of black mycelial cord (rhizomorphs). [...] "
            "The species grows and spreads primarily underground, such that the bulk of the organism is not visible from the surface. "
            "In the autumn, the subterranean parts of the organism bloom \"honey mushrooms\" as surface fruits. [...] "
            "A spatial genetic analysis estimated that an individual specimen growing over 91 acres (37 ha) in northern Michigan weighs 440 tons [...] "
            "Another specimen in northeastern Oregon's Malheur National Forest is one of the largest organisms on Earth [...] "
            "it covers 3.5 square miles (2,200 acres; 9.1 km2), and weighs as much as 35,000 tons [...] "
            "a 2,500-year old specimen of Armillaria ostoyae in northern Michigan, United States originated from spores of a parent fungus in Ontario, Canada, "
            "then grew over millennia into the 21st century to a mass of 440 tons (4 × 105 kg), making it the equivalent in weight of 3 blue whales. [...] "
            "was found to be the largest fungal colony in the world, spanning an area of 3.5 square miles (2,200 acres; 9.1 km2). "
            "This organism is estimated to be some 8,000 years old and may weigh as much as 35,000 tons. "
            "If this colony is considered a single organism, it is one of the largest known organisms in the world by area, "
            "only knowingly rivalled by a colony of Posidonia australis on the Australian seabed [...] "
            "Younger conifer trees at age 10 and below are more susceptible to infection leading to mortality [...] "
            "Armillaria can remain viable in stumps for 50 years. Chemical treatments do not eradicate the fungus entirely",
            nome="Armillaria ostoyae")],
    },
    # 3 a formiga-zumbi e a folha fóssil de 48 milhões de anos
    {
        "temas_secundarios": ["insetos", "paleontologia"],
        "tipos_espanto": ["engenhosidade", "escala_absurda"],
        "gancho": "O fungo da \"formiga-zumbi\" faz a formiga infectada cravar as mandíbulas numa nervura de folha, a uns 25 cm do chão, e morrer ali. Uma folha fóssil de 48 milhões de anos já mostra as marcas dessa mordida.",
        "explicacao": (
            "O fungo Ophiocordyceps unilateralis, descoberto pelo naturalista Alfred Russel Wallace em 1859, ataca "
            "formigas como as carpinteiras. O esporo gruda na carapaça e a atravessa com pressão mecânica e enzimas. "
            "A formiga infectada abandona o ninho no alto das árvores e as trilhas de sempre, sobe pelo caule de uma "
            "planta e morde com força anormal uma nervura do lado de baixo de uma folha, a cerca de 25 centímetros "
            "do chão. Essa altura é tida como ideal, em umidade e temperatura, para o fungo crescer. Num estudo feito "
            "na Tailândia, essas mordidas aconteciam sincronizadas, no meio-dia solar. Em seguida os músculos da "
            "mandíbula atrofiam, e a formiga fica presa, de cabeça para baixo: é a chamada \"mordida da morte\". O "
            "fungo a mata, reforça o exoesqueleto por dentro e, quando está pronto, faz brotar da cabeça dela a "
            "estrutura que libera os esporos. Tudo leva de 4 a 10 dias. A manipulação depende de enormes populações "
            "de células do fungo ao lado do cérebro e dentro dos músculos. A mordida deixa na folha marcas em forma "
            "de haltere, e marcas semelhantes foram achadas numa folha fóssil do sítio de Messel, na Alemanha, com "
            "48 milhões de anos: sinal de que esse truque é muito antigo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Ophiocordyceps_unilateralis",
            "Ophiocordyceps unilateralis, commonly known as zombie-ant fungus, is an insect-pathogenic fungus, discovered by the British naturalist Alfred Russel Wallace in 1859. [...] "
            "The fungus primarily targets ants from the tribe Camponotini, including carpenter ants (genus Camponotus). [...] "
            "The process, leading up to mortality, takes 4–10 days, and includes a reproductive stage where fruiting bodies grow from the ant's head, rupturing to release the fungus's spores. [...] "
            "The spores attach to their exoskeletons and eventually break through using mechanical pressure and enzymes. [...] "
            "The extended phenotype of O. unilateralis typically depicts the infected ant leaving its canopy nest and its normal foraging path to reach the forest floor "
            "and subsequently climbs to around 25 centimetres (9.8 in) above ground level, a height that is considered optimal for fungal growth due to its humidity level and temperature. [...] "
            "The behavioral manipulation of the ant would not be possible without the presence of huge fungal cell populations beside the host's brain and within muscles [...] "
            "The ant climbs up the stem of a plant and uses its mandibles with abnormal force to secure itself to a leaf vein, leaving dumbbell-shaped marks on it. [...] "
            "A search of plant-fossil databases revealed similar marks on a fossil leaf from the Messel Pit, which is 48 million years old. "
            "Once the mandibles of the ant are secured to the leaf vein, atrophy quickly sets in [...] "
            "The ant is no longer able to control the muscles of the mandible and remains fixed in place, hanging upside-down on the leaf. "
            "This lockjaw trait is popularly known as the death grip and is essential in the fungus's lifecycle. "
            "A study led in Thailand revealed that there is a synchronization of this manipulated biting behavior at solar noon. "
            "The fungus then kills the ant and continues to grow as its hyphae invade more soft tissues and structurally fortify the ant's exoskeleton. [...] "
            "A 48-million-year-old fossil of a leaf stem exhibiting dumbbell-shaped marks characteristic of those made by an ant in the death-grip of Ophiocordyceps unilateralis was discovered in the Messel pit (Germany).",
            nome="Ophiocordyceps unilateralis")],
    },
    # 4 o carvão do Carbonífero e os fungos que demoraram a digerir a lignina
    {
        "temas_secundarios": ["geologia_profunda", "plantas"],
        "tipos_espanto": ["misterio_aberto", "conexao_inesperada"],
        "gancho": "Por que tanto carvão se formou no Carbonífero? Uma hipótese diz que as árvores criaram a lignina antes de surgirem fungos capazes de digeri-la, e a madeira se acumulou sem apodrecer. A ideia é contestada.",
        "explicacao": (
            "O Carbonífero durou 60 milhões de anos, do fim do Devoniano ao começo do Permiano, e o nome quer "
            "dizer \"portador de carvão\", por causa das muitas camadas de carvão formadas no mundo todo nesse período. "
            "Florestas e pântanos imensos cobriam a terra e acabaram virando esses depósitos. A explicação mais "
            "famosa para esse pico é a hipótese do \"atraso na evolução dos fungos\": a lignina, a fibra que endurece "
            "a madeira, teria surgido nas árvores bem antes dos fungos que conseguem decompô-la, e nesse intervalo "
            "montanhas de matéria vegetal teriam se acumulado. Um estudo de 2012 na revista Science, que "
            "reconstruiu a história das enzimas comparando 31 genomas de fungos, reforçou a ideia ao sugerir que os "
            "fungos basidiomicetos com essas enzimas surgiram no Permiano, o período seguinte. A objeção é forte: "
            "grandes depósitos de carvão também se formaram muito depois, no Mesozoico e no Cenozoico, quando esses "
            "fungos já estavam bem estabelecidos, e a capacidade de degradar lignina talvez já existisse no fim do "
            "Devoniano, ainda que com outras enzimas. A hipótese rival diz que o Carbonífero foi único pela "
            "geografia e pelo clima: continentes na faixa equatorial úmida, alta produtividade biológica e bacias "
            "baixas, encharcadas, que afundavam devagar. O debate continua aberto."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "hipotese",
        "fontes": [wiki("Carboniferous",
            "is a geologic period and system of the Paleozoic era that spans 60 million years, from the end of the Devonian Period 358.86 Ma (million years ago) "
            "to the beginning of the Permian Period, 298.9 Ma. [...] "
            "The name Carboniferous means \"coal-bearing\", from the Latin carbō (\"coal\") and ferō (\"bear, carry\"), and refers to the many coal beds formed globally during that time. [...] "
            "Vast swaths of forests and swamps covered the land, which eventually became the coal beds characteristic of the Carboniferous stratigraphy evident today. [...] "
            "There is ongoing debate as to why this peak in the formation of Earth's coal deposits occurred during the Carboniferous. "
            "The first theory, known as the delayed fungal evolution hypothesis, proposes that a delay between the development of trees with the wood fibre lignin "
            "and the subsequent evolution of lignin-degrading fungi gave a period of time where vast amounts of lignin-based organic material could accumulate. "
            "Genetic analysis of basidiomycete fungi, which have enzymes capable of breaking down lignin, supports this theory by suggesting this fungi evolved in the Permian. "
            "However, significant Mesozoic and Cenozoic coal deposits formed after lignin-digesting fungi had become well established, "
            "and fungal degradation of lignin may have already evolved by the end of the Devonian, even if the specific enzymes used by basidiomycetes had not. "
            "The second theory is that the geographical setting and climate of the Carboniferous were unique in Earth's history: "
            "the co-occurrence of the position of the continents across the humid equatorial zone, high biological productivity, "
            "and the low-lying, water-logged and slowly subsiding sedimentary basins [...] "
            "(28 June 2012). \"The Paleozoic Origin of Enzymatic Lignin Decomposition Reconstructed from 31 Fungal Genomes\". Science.",
            nome="Carboniferous")],
    },
    # 5 o melão mofado de Peoria e a penicilina industrial
    {
        "temas_secundarios": ["farmacos", "historia_medicina"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "Uma linhagem de mofo usada na produção industrial de penicilina veio de um melão-cantalupo mofado de uma feira de Peoria, nos EUA. Depois, raios X e luz ultravioleta a fizeram render ainda mais.",
        "explicacao": (
            "Fleming publicou a descoberta da penicilina em 1929, mas fabricá-la em quantidade era outra história. "
            "Nos Estados Unidos, o desafio foi parar num laboratório do Departamento de Agricultura em Peoria, "
            "Illinois, onde Robert Coghill levantou a possibilidade de fermentar o mofo em grandes tanques. O começo "
            "decepcionou: em tanque, o fungo rendia só três a quatro unidades Oxford por centímetro cúbico, contra vinte nas "
            "culturas de superfície. Com a ajuda do Comando de Transporte Aéreo do Exército americano, buscaram mofos "
            "parecidos pelo mundo, e bons candidatos vieram de Chongqing, Bombaim e da Cidade do Cabo. A melhor "
            "amostra, porém, estava num melão-cantalupo vendido numa feira da própria Peoria. O mofo, catalogado como "
            "NRRL 1951, pode ter vindo do próprio laboratório, de esporos que escaparam de lá. Depois, pesquisadores "
            "da Carnegie Institution o expuseram a raios X e obtiveram um mutante que fazia 300 miligramas de "
            "penicilina por litro, o dobro do original. Na Universidade de Wisconsin, a luz ultravioleta gerou outro "
            "mutante, que mais que dobrou a produção, mas de um tipo menos útil, a penicilina K. Acrescentar ácido "
            "fenilacético fez o fungo trocar para a penicilina G, chegando a 550 miligramas por litro. Essa "
            "linhagem do melão é a que foi usada na produção industrial da penicilina G."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("History_of_penicillin",
                "Orville May, the director of the UDSA's Northern Regional Research Laboratory (NRRL) in Peoria, Illinois. [...] "
                "Robert D. Coghill, the chief of the NRRL's fermentation division, who raised the possibility that fermentation in large vessels might be the key to large-scale production. [...] "
                "The initial results were disappointing; penicillin cultured in this manner yielded only three to four Oxford units per cubic centimetre, compared to twenty for surface cultures. "
                "He got the help of U.S. Army's Air Transport Command to search for similar mould in different parts of the world. "
                "Good moulds were found in samples from Chongqing, Bombay and Cape Town. "
                "The best sample, however, was from a cantaloupe sold in a Peoria fruit market in 1943. "
                "The mould was identified as Penicillium chrysogenum and designated as \"NRRL 1951\" or \"cantaloupe strain\". "
                "The spores may have escaped from the NRRL. [...] "
                "researchers at the Carnegie Institution of Washington subjected NRRL 1951 to X-rays to produce a mutant strain designated X-1612 "
                "that produced 300 milligrams of penicillin per litre of mould culture, twice as much as NRRL 1951. "
                "In turn, researchers at the University of Wisconsin used ultraviolet radiation on X-1612 to produce a strain designated Q-176. "
                "This produced more than twice the penicillin of X-1612, but in the form of the less desirable penicillin K. "
                "Phenylacetic acid was added to switch it to producing the highly potent penicillin G. "
                "This strain could produce up to 550 milligrams of penicillin per litre.",
                nome="History of penicillin"),
            wiki("Penicillium_rubens",
                "the Wisconsin strain (NRRL1951) obtained from a cantaloupe in Peoria, Illinois, in 1944 and has been used for industrial production of penicillin G. [...] "
                "he published his discovery in the June 1929 issue of the British Journal of Experimental Pathology.",
                nome="Penicillium rubens"),
        ],
    },
    # 6 os fungos escuros de Chernobyl e a radiação
    {
        "temas_secundarios": ["microbiologia", "astrobiologia"],
        "tipos_espanto": ["misterio_aberto", "contraintuitivo"],
        "gancho": "Nas paredes do reator destruído de Chernobyl vivem fungos escuros, ricos em melanina. Em laboratório, alguns cresceram mais rápido sob radiação 500 vezes acima do normal. A ideia de que \"comem\" radiação ainda é hipótese.",
        "explicacao": (
            "Muitos fungos foram isolados em volta da usina de Chernobyl, e alguns dirigem o crescimento dos seus "
            "filamentos na direção do grafite radioativo do desastre. Um estudo descartou que o atrativo fosse o "
            "carbono, mas não identificou o mecanismo. O que esses fungos têm em comum é a melanina, o pigmento "
            "escuro que também protege contra radiação ultravioleta. Em 2007, uma equipe do Albert Einstein College "
            "of Medicine, em Nova York, testou a ideia de que a radiação poderia até ajudá-los. Células com melanina "
            "de duas espécies, expostas a uma radiação cerca de 500 vezes maior que a natural, cresceram bem mais "
            "rápido e incorporaram 3 vezes mais acetato do que células não irradiadas ou mutantes sem pigmento. A "
            "radiação também acelerou o crescimento de Cladosporium sphaerospermum, fungo abundante em Chernobyl, "
            "com pouco alimento. E a capacidade da melanina de transferir elétrons subiu 4 vezes depois da "
            "irradiação. Mas os fungos sempre tinham algum nutriente, então a radiação pode só tê-los ajudado a "
            "aproveitar a comida melhor. Ninguém sabe ainda que química estaria por trás de uma \"radiossíntese\". "
            "Mesmo assim, a ideia já foi ao espaço: entre dezembro de 2018 e janeiro de 2019, uma camada desse "
            "fungo de uns 1,67 milímetro, cultivada na Estação Espacial, deixou passar menos radiação do que uma "
            "amostra sem fungo, o que inspira a ideia de escudos vivos para astronautas."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "hipotese",
        "fontes": [
            wiki("Radiotrophic_fungus",
                "It has been claimed that radiotrophic fungi have been found in extreme environments such as in the Chernobyl Nuclear Power Plant. [...] "
                "Many fungi have been isolated from the area around the destroyed Chernobyl Nuclear Power Plant, some of which have been observed directing their growth of hyphae "
                "toward radioactive graphite from the disaster, a phenomenon called \"radiotropism\". "
                "Study has ruled out the presence of carbon as the resource attracting the fungal colonies [...] "
                "but were not able to identify the biological mechanism behind this effect. [...] "
                "However, each culture was performed with at least limited nutrients provided to each fungus. "
                "The increase in biomass and other effects could be caused either by the cells directly deriving energy from ionizing radiation, "
                "or by the radiation allowing the cells to utilize traditional nutrients either more efficiently or more rapidly. [...] "
                "The exact biochemical processes in the suggested melanin-based synthesis of organic compounds or other metabolites for fungal growth [...] are unknown. [...] "
                "It is hypothesized that radiotrophic fungi could potentially be used as a biological shield to attenuate ionizing radiation, specifically for the protection of astronauts in deep space. [...] "
                "an experiment was conducted aboard the International Space Station (ISS) from December 2018 through January 2019. "
                "The experiment cultivated the dematiaceous fungus Cladosporium sphaerospermum [...] "
                "Radiation levels measured directly beneath the approximately 1.67 mm-thick fungal growth layer were found to be lower than those beneath a no-growth negative control.",
                nome="Radiotrophic fungus"),
            {"url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0000457",
             "titulo": "Ionizing Radiation Changes the Electronic Properties of Melanin and Enhances the Growth of Melanized Fungi (Dadachova et al., PLoS ONE, 2007)",
             "idioma": "en",
             "trecho": "Many fungi constitutively synthesize melanin [2], which is likely to confer a survival advantage in the environment [3] by protecting against UV and solar radiation [...] "
                       "Most dramatically, melanized fungal species colonize the walls of the highly radioactive damaged reactor at Chernobyl [...] "
                       "Melanized Wangiella dermatitidis and Cryptococcus neoformans cells exposed to ionizing radiation approximately 500 times higher than background grew significantly faster "
                       "as indicated by higher CFUs, more dry weight biomass and 3-fold greater incorporation of 14C-acetate than non-irradiated melanized cells or irradiated albino mutants. "
                       "In addition, radiation enhanced the growth of melanized Cladosporium sphaerospermum cells under limited nutrients conditions. [...] "
                       "an intrinsically melanized fungus found in abundance at the site of nuclear accident in Chernobyl [...] "
                       "electron transfer properties of melanin in the NADH oxidation/reduction reaction increased 4-fold after melanin irradiation. [...] "
                       "Published: May 23, 2007"},
        ],
    },
    # 7 o quitrídio e o declínio dos anfíbios
    {
        "temas_secundarios": ["doencas_infecciosas", "animais_extremos"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "Um fungo microscópico que ataca a pele dos anfíbios foi apontado, numa revisão de 2019, como fator no declínio de pelo menos 501 espécies, 90 delas extintas na natureza. A conta é contestada.",
        "explicacao": (
            "O fungo Batrachochytrium dendrobatidis foi descoberto em 1998 por Lee Berger e descrito como espécie "
            "em 1999. Ele ataca as camadas mais externas da pele, ricas em queratina. Como os anfíbios dependem da "
            "pele para muita coisa, quando a infecção passa de uns 10 mil esporos a maioria das espécies já não "
            "consegue respirar, se hidratar nem controlar a água e a temperatura do corpo direito; no sangue, faltam "
            "sódio, magnésio e potássio. Em uma rã norte-americana, esse desequilíbrio leva à parada do coração. A "
            "comparação de 234 genomas do fungo sugere que uma linhagem da península da Coreia deu início à "
            "pandemia entre os anfíbios, espalhada pelo comércio de rãs. Em 2019, uma revisão na revista Science "
            "calculou que a doença contribuiu para o declínio de ao menos 501 espécies de anfíbios em 50 anos, das "
            "quais 90 foram confirmadas ou presumidas extintas na natureza e outras 124 caíram mais de 90%. Os "
            "autores a chamaram de a maior perda de biodiversidade já registrada causada por uma doença. Um estudo "
            "posterior, também na Science, concluiu que faltavam evidências e que os resultados não se "
            "reproduziam com os mesmos dados e métodos. Ainda não se sabe quantas espécies foram afetadas, mas há "
            "bons dados para algumas, e certas populações se adaptaram depois de uma mortandade inicial."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Chytridiomycosis",
                "B. dendrobatidis predominantly affects the outermost layers of skin containing keratin. "
                "When most species reach a B. dendrobatidis threshold of 10,000 zoospores, they are not able to breathe, hydrate, osmoregulate, or thermoregulate correctly. "
                "This is proven by blood samples that show a lack of certain electrolytes, such as sodium, magnesium, and potassium. [...] "
                "the genomes of 234 Batrachochytrium dendrobatidis isolates were phylogenetically compared and the results strongly suggest "
                "that a lineage found in the Korean peninsula likely seeded the panzootic. [...] "
                "A 2019 Science review assessed that chytridiomycosis was a factor in the decline of at least 501 amphibian species during the past 50 years, "
                "of which 90 species were confirmed or presumed to have gone extinct in the wild and another 124 had declined in numbers by more than 90%. "
                "The review characterized the overall toll as the \"greatest recorded loss of biodiversity attributable to a disease\". "
                "However, a follow-up study in Science found the 2019 study by Scheele et al. to be lacking in the necessary evidence to make these claims "
                "and found the conclusions could not be reproduced with the original study's data and methods. "
                "It remains unclear how many and which species have been impacted by chytridiomycosis, but there are good data for a limited number of species",
                nome="Chytridiomycosis"),
            wiki("Batrachochytrium_dendrobatidis",
                "Since its discovery in 1998 by Lee Berger and species description in 1999 by Joyce E. Longcore [...] "
                "There is more recent information that the species originated on the Korean peninsula and was spread by the trade in frogs. [...] "
                "Some amphibian species have been found to adapt to infection after an initial die-off [...] "
                "One amphibian particular affected by Bd is Lithobates clamitans. "
                "Bd kills this frog by interfering with external water exchange, causing an imbalance in ion exchange that leads to heart failure.",
                nome="Batrachochytrium dendrobatidis"),
        ],
    },
    # 8 os voos mais rápidos da natureza: esporos no esterco
    {
        "temas_secundarios": ["biomimetica", "animais_extremos"],
        "tipos_espanto": ["escala_absurda", "engenhosidade"],
        "gancho": "Fungos que crescem no esterco disparam esporos com acelerações de 20 mil a 180 mil vezes a gravidade: em aceleração, os voos mais rápidos já medidos na natureza. Um deles ainda mira na luz com uma \"lente\".",
        "explicacao": (
            "O ciclo desses fungos passa pelo intestino de herbívoros. O cavalo come o capim com o esporo grudado, "
            "o esporo atravessa o tubo digestivo sem germinar e sai no esterco, onde o fungo cresce. Para recomeçar, "
            "ele precisa lançar novos esporos para longe do monte de esterco, em capim que outro animal vá comer. Em "
            "2008, uma equipe da Universidade Miami, em Ohio, filmou o disparo de quatro espécies com câmeras de "
            "altíssima velocidade. Os esporos saíram a velocidades de 2 a 25 metros por segundo, com acelerações de "
            "20 mil a 180 mil g, e chegaram a até 2,5 metros de distância. O motor é só pressão de água dentro das "
            "células, em níveis comuns nos fungos, sem nenhum mecanismo especial. No Pilobolus, a haste "
            "transparente termina numa bolha que funciona como lente: ela concentra a luz sobre pigmentos na base, "
            "e a estrutura cresce apontada para a fonte de luz, o que joga o pacote de esporos para longe do "
            "esterco. Ao cair numa gota de orvalho, o pacote vira para o lado grudento e fica preso à planta. Há até "
            "caronas: larvas de vermes que parasitam os pulmões de veados e bois sobem na haste do Pilobolus e são "
            "lançadas junto, até serem engolidas pelo próximo hospedeiro."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0003237",
             "titulo": "The Fastest Flights in Nature: High-Speed Spore Discharge Mechanisms among Fungi (Yafetto et al., PLoS ONE, 2008)",
             "idioma": "en",
             "trecho": "analyze the entire launch process in four species of fungi that grow on the dung of herbivores. "
                       "For the first time we have direct measurements of launch speeds and empirical estimates of acceleration in these fungi. "
                       "Launch speeds ranged from 2 to 25 m s−1 and corresponding accelerations of 20,000 to 180,000 g propelled spores over distances of up to 2.5 meters. [...] "
                       "In terms of acceleration, these are the fastest recorded flights in nature. [...] "
                       "Affiliation Department of Botany, Miami University, Oxford, Ohio [...] "
                       "Published: September 17, 2008 [...] "
                       "high speed spore discharge mechanisms in fungi are powered by the same levels of turgor pressure that are characteristic of fungal hyphae "
                       "and do not require any special mechanisms of osmolyte accumulation."},
            wiki("Pilobolus",
                "A herbivorous animal such as a horse then eats the substrate, unknowingly consuming the sporangium as well. "
                "The Pilobolus sporangium survives the passage through the gastrointestinal tract without germinating, and emerges with the excrement. [...] "
                "It consists of a transparent stalk which rises above the excrement to end in a balloon-like subsporangial vesicle. [...] "
                "The shape and transparency of the subsporangial vesicle allow it to act as a lens, focusing light into carotenoid pigments deposited near the base of the vesicle [...] "
                "The developing sporangiophore grows such that the maturing sporangium is aimed directly at the light. [...] "
                "guarantees that the sporangium is shot some distance from the excrement, enhancing the chances that it will attach to vegetation and be eaten by a new host. [...] "
                "leads the sporangium to flip over onto its sticky bottom after landing in a drop of dew, thus allowing it to cling to a plant substrate. [...] "
                "The forcible discharge mechanism of Pilobolus is exploited by parasitic nematodes including lungworms in the genus Dictyocaulus. "
                "Larval lungworm nematodes excreted by infected deer, elk, cattle, horses, and other hosts climb up Pilobolus sporangiophores and are discharged with the sporangium. "
                "They complete their life cycle when they and their Pilobolus vector are eaten by a new host.",
                nome="Pilobolus"),
        ],
    },
    # 9 a "árvore-mãe" e a internet dos fungos: menos evidência do que a fama
    {
        "temas_secundarios": ["plantas", "ecologia"],
        "tipos_espanto": ["mito_desmentido", "misterio_aberto"],
        "gancho": "A ideia de árvores-mães que mandam alimento às filhas por uma \"internet\" de fungos virou livro, documentário e até episódio de série. Uma revisão de 2023 concluiu que ela não tem evidência publicada revisada por pares.",
        "explicacao": (
            "As micorrizas são reais e antigas: fungos se associam às raízes, geralmente com vantagem para os dois "
            "lados. Quando as hifas de um mesmo fungo ligam duas ou mais plantas, forma-se uma rede micorrízica "
            "comum, apelidada de \"Wood Wide Web\". A partir dos trabalhos da ecóloga canadense Suzanne Simard, a "
            "rede ganhou fama de distribuir nutrientes e alertas entre árvores. Em 2023, Justine Karst, Melanie "
            "Jones e Jason Hoeksema avaliaram, na revista Nature Ecology & Evolution, três afirmações populares. "
            "Que essas redes são comuns nas florestas e que transferem recursos que melhoram a vida das mudas: "
            "evidência insuficiente, porque os estudos de campo variam demais, têm explicações alternativas ou são "
            "limitados demais para generalizar. Que árvores adultas mandam recursos e sinais de defesa de "
            "preferência aos próprios descendentes: nenhuma evidência publicada revisada por pares. Os autores "
            "também mostraram que as citações sem respaldo de estudos influentes dobraram em 25 anos, e que há um "
            "viés a favor de citar efeitos positivos. Entre as referências do artigo estão livros de divulgação, "
            "o documentário Fantastic Fungi e um episódio da série Ted Lasso. A conclusão: o conhecimento ainda é "
            "escasso e incerto demais para orientar o manejo das florestas. Não se trata de negar as redes, mas de "
            "não ir além do que os dados mostram."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": "https://www.nature.com/articles/s41559-023-01986-1",
             "titulo": "Positive citation bias and overinterpreted results lead to misinformation on common mycorrhizal networks in forests (Karst, Jones e Hoeksema, Nature Ecology & Evolution, 2023)",
             "idioma": "en",
             "trecho": "Published: 13 February 2023 [...] "
                       "Justine Karst [...] Melanie D. Jones [...] Jason D. Hoeksema [...] "
                       "A common mycorrhizal network (CMN) is formed when mycorrhizal fungal hyphae connect the roots of multiple plants of the same or different species belowground. [...] "
                       "We are concerned, however, that recent claims in the popular media about CMNs in forests are disconnected from evidence, "
                       "and that bias towards citing positive effects of CMNs has developed in the scientific literature. "
                       "We first evaluated the evidence supporting three common claims. "
                       "The claims that CMNs are widespread in forests and that resources are transferred through CMNs to increase seedling performance are insufficiently supported "
                       "because results from field studies vary too widely, have alternative explanations or are too limited to support generalizations. "
                       "The claim that mature trees preferentially send resources and defence signals to offspring through CMNs has no peer-reviewed, published evidence. "
                       "We next examined how the results from CMN research are cited and found that unsupported claims have doubled in the past 25 years [...] "
                       "We conclude that knowledge on CMNs is presently too sparse and unsettled to inform forest management. [...] "
                       "Wohlleben, P. The Hidden Life of Trees [...] "
                       "Schwartzberg, L. Fantastic Fungi. Moving Art (2019). [...] "
                       "Braff, Z. Midnight train to Royston. Ted Lasso (2021)."},
            wiki("Mycorrhizal_network",
                "Mycorrhizal relationships are most commonly mutualistic, with both partners benefiting [...] "
                "Suzanne Simard, professor of forest ecology at the University of British Columbia in Canada. [...] "
                "the \"Wood Wide Web\". Many of the claims made about common mycorrhizal networks, including that they are ubiquitous in forests, "
                "that resources are transferred between plants through them, and that they are used to transfer warnings between trees, "
                "have been criticised as being not strongly supported by evidence. [...] "
                "The keyword \"common\" requires that two or more individual plants are connected by the same underground fungal network",
                nome="Mycorrhizal network"),
        ],
    },
    # 10 o líquen não é dupla: o terceiro sócio
    {
        "temas_secundarios": ["microbiologia", "evolucao"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Desde 1867, o líquen é descrito como uma parceria entre um fungo e uma alga. Em 2016, achou-se em muitos liquens um terceiro sócio, uma levedura, o que pode explicar por que é tão difícil cultivá-los em laboratório.",
        "explicacao": (
            "Em 1867, o botânico suíço Simon Schwendener propôs que o líquen não é um ser só, mas a combinação de "
            "um fungo com algas ou cianobactérias. Muitos dos principais liquenólogos da época, como Nylander, "
            "rejeitaram a ideia, porque o consenso era que todo ser vivo era autônomo. A prova experimental veio "
            "com o tempo, e em 1939 Eugen Thomas publicou a primeira recombinação bem-sucedida dos parceiros. Na "
            "parceria, a alga faz fotossíntese e fornece açúcares, e o fungo retém água e capta minerais. Cerca de "
            "20% das espécies de fungos vivem assim. Mas a história tinha mais um capítulo. Em 2016, Toby "
            "Spribille e colegas, combinando microscopia e genética molecular, acharam leveduras de outro grupo, "
            "os basidiomicetos, no córtex de liquens da América do Norte, uma descoberta inesperada. Parece que "
            "muitos liquens, provavelmente a maioria, abrigam esse terceiro parceiro. As leveduras formam a camada "
            "externa do líquen e podem influir na sua forma, e a falta delas talvez explique por que é tão difícil "
            "fazer líquen crescer em laboratório. O próprio Spribille tem trajetória fora do comum: nascido nos "
            "Estados Unidos, estudou em casa, não tinha as qualificações tradicionais e foi estudar na "
            "Universidade de Göttingen, na Alemanha. Antes da carreira acadêmica, trabalhou com florestas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Lichen",
                "it was not until 1867, when Swiss botanist Simon Schwendener proposed his dual theory of lichens, that lichens are a combination of fungi with algae or cyanobacteria [...] "
                "Many of the leading lichenologists at the time, such as James Crombie and Nylander, rejected Schwendener's hypothesis because the consensus was that all living organisms were autonomous. [...] "
                "Further experimental proof of the dual nature of lichens was obtained when Eugen Thomas published his results in 1939 on the first successful re-synthesis experiment. [...] "
                "Toby Spribille and colleagues found that many types of lichen that were long thought to be ascomycete–algae pairs were actually ascomycete–basidiomycete–algae trios. [...] "
                "It appears many, probably the majority, of lichens also live in a symbiotic relationship with an order of basidiomycete yeasts called Cyphobasidiales. "
                "The absence of this third partner could explain why growing lichen in the laboratory is difficult. "
                "The yeast cells are responsible for the formation of the characteristic cortex of the lichen thallus, and could also be important for its shape. [...] "
                "since about 20% of all fungal species have acquired this mode of life. [...] "
                "The fungal partner protects the alga by retaining water, serving as a larger capture area for mineral nutrients [...] "
                "they reduce atmospheric carbon dioxide into organic carbon sugars to feed both symbionts.",
                nome="Lichen"),
            wiki("Toby_Spribille",
                "Toby Spribille was born in the US and educated at home. He was interested in science but lacked conventional qualifications. "
                "Therefore, he studied at University of Göttingen in Germany. [...] "
                "He first worked in forestry. [...] "
                "In 2016, he and colleagues identified the presence of basidiomycota yeasts within the structure of lichen species in North America "
                "through using a combination of microscopy and molecular genetic methods. "
                "This was a new, unexpected, discovery since lichens were considered to consist of one fungus and one (or two) photosynthetic algal or bacterial components.",
                nome="Toby Spribille"),
        ],
    },
    # 11 o cogumelo com milhares de "sexos"
    {
        "temas_secundarios": ["evolucao", "genetica"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Um cogumelo comum em madeira podre, o Schizophyllum commune, tem milhares de \"sexos\": seus tipos de acasalamento se combinam de tantas formas que quase qualquer outro indivíduo da espécie é um parceiro possível.",
        "explicacao": (
            "Em boa parte dos fungos, \"macho\" e \"fêmea\" não fazem sentido. O que decide quem pode cruzar com quem "
            "são os tipos de acasalamento, definidos por genes. No Schizophyllum commune, cada célula tem dois "
            "desses locais no genoma, chamados A e B, e cada um aparece em muitas versões. Segundo um levantamento, "
            "são mais de 339 tipos A e 64 tipos B, e uma estimativa das combinações possíveis chega a 23.328. Dois "
            "indivíduos só são compatíveis quando diferem tanto em A quanto em B, mas, com tanta variedade, isso "
            "acontece quase sempre: a chance de achar um parceiro compatível na natureza chega perto de 100%. Num "
            "fungo com sistema mais simples, o carvão-do-milho, a chance fica em torno de 50%. Acredita-se que "
            "sistemas com tantas versões favoreçam o cruzamento com indivíduos de fora da família. O cogumelo tem "
            "outro truque: as lâminas sob o chapéu se partem ao meio quando ele seca, o que lhe valeu em inglês o "
            "nome de \"split gill\", e ele pode ficar seco por décadas e voltar à ativa com a umidade."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Mating_in_fungi",
                "Not all fungi reproduce sexually and many that do are isogamous; thus, for many members of the fungal kingdom, the terms \"male\" and \"female\" do not apply. [...] "
                "It is believed that multi-allelic systems favor outcrossing in Basidiomycota. "
                "For example, in the case of U. maydis, which bears more than 25 b but only 2 a mating types, an individual has an approximately 50% chance to encounter a compatible mate in nature. "
                "However, species such as C. cinerea, which has more than 240 A and B mating types, each, and S. commune, which has more than 339 A mating types and 64 B mating types, "
                "approach close to 100% chance of encountering a compatible partner in nature, due to the huge number of mating types generated by these systems.",
                nome="Mating in fungi"),
            wiki("Schizophyllum_commune",
                "The gills, which produce basidiospores on their surface, split when the mushroom dries out, earning this mushroom the common name split gill. "
                "The mushrooms can remain dry for decades and then be revived with moisture. [...] "
                "It has a tetrapolar mating system with each cell containing two mating-type loci (called A and B) [...] "
                "When combined this gives an estimated 9×32×9×9=23328 potential mating type specificities. [...] "
                "compatibility between haploid individuals exists only when for both the A and the B mating-type locus at least the α or β are different. [...] "
                "It is common in rotting wood.",
                nome="Schizophyllum commune"),
        ],
    },
    # 12 o submarino Turtle iluminado por fungo
    {
        "temas_secundarios": ["espionagem", "invencoes"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "O Turtle, de 1775, tido como o primeiro submarino com uso registrado em combate, tinha os ponteiros dos instrumentos iluminados por pedaços de madeira com fungo luminoso. No frio, a luz falhou.",
        "explicacao": (
            "A luz é o \"fogo-fátuo\" das florestas, em inglês \"foxfire\": o brilho verde-azulado de certos fungos "
            "que crescem em madeira podre, produzido por uma reação química entre luciferina e a enzima luciferase. "
            "Aristóteles já falava, em 382 a.C., de uma luz que, ao contrário do fogo, era fria ao toque. O Turtle "
            "foi construído por David Bushnell, durante a Guerra de Independência dos Estados Unidos, para prender "
            "explosivos no casco de navios britânicos. Era tripulado por uma só pessoa, tinha ar para uns 30 "
            "minutos e seis pequenos vidros no topo deixavam entrar a luz do dia. Embaixo d'água, para ver a "
            "bússola e o barômetro, o tripulante contava com pedacinhos de madeira luminosa presos "
            "aos ponteiros. Nos testes de novembro de 1775, Bushnell descobriu que a iluminação falhava quando a "
            "temperatura caía demais. Ele pediu várias vezes a Benjamin Franklin que sugerisse alternativas, mas "
            "Franklin não sugeriu nenhuma, e o submarino ficou parado durante o inverno. Costuma-se dizer que a "
            "ideia do fungo foi de Franklin, mas as cartas de Benjamin Gale mostram que ele só foi consultado "
            "sobre alternativas. Em 1776, as tentativas de prender explosivos a navios britânicos no porto de Nova "
            "York falharam todas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Turtle_(submersible)",
                "Turtle (also called American Turtle) was an American vessel that is regarded as the world's first submarine, or by modern standards a submersible, "
                "with a documented record of use in naval combat. [...] "
                "developing a submersible that could be used to attach explosive charges to the hull of a harboured ship for use against the Royal Navy during the American Revolutionary War. [...] "
                "Several attempts were made using Turtle to affix explosives to the undersides of British warships in New York Harbor in 1776. All failed [...] "
                "It was manned and operated by one person and contained enough air for about 30 minutes. [...] "
                "Six small pieces of thick glass in the top of the submarine provided natural light. "
                "The internal instruments had small pieces of bioluminescent foxfire affixed to the needles to indicate their position in the dark. "
                "During trials in November 1775, Bushnell discovered that this illumination failed when the temperature dropped too low. "
                "He repeatedly requested that Benjamin Franklin suggest possible alternatives, but Franklin did not suggest any and Turtle was sidelined for the winter.",
                nome="Turtle (submersible)"),
            wiki("Foxfire",
                "Foxfire, also called fairy fire and chimpanzee fire, is the bioluminescence created by some species of fungi present in decaying wood. "
                "The bluish-green glow is attributed to a luciferase, an oxidative enzyme, which emits light as it reacts with a luciferin. [...] "
                "The oldest recorded documentation of foxfire is from 382 B.C., by Aristotle, whose notes refer to a light that, unlike fire, was cold to the touch. [...] "
                "Foxfire was used to illuminate the needles on the barometer and the compass of Turtle, an early submarine. "
                "This is commonly thought to have been suggested by Benjamin Franklin; a reading of the correspondence from Benjamin Gale, however, "
                "shows that Benjamin Franklin was only consulted for alternative forms of lighting when the cold temperatures rendered the foxfire inactive.",
                nome="Foxfire"),
        ],
    },
    # 13 os dois fungos que Ötzi carregava
    {
        "temas_secundarios": ["pre_historia", "farmacos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Ötzi, o homem do gelo de 5.300 anos, levava dois fungos presos em tiras de couro: um para acender fogo e outro com uma substância tóxica para um verme intestinal que, como se viu depois, ele mesmo tinha.",
        "explicacao": (
            "Entre os pertences da múmia achada nos Alpes havia frutinhas, dois cestos de casca de bétula e dois "
            "tipos de cogumelos-orelha, os poliporos, atravessados por tiras de couro. Um deles era um fungo "
            "isqueiro, parte do que parece ter sido um kit complexo de acender fogo: pedaços de mais de uma dúzia "
            "de plantas, além de sílex e pirita para tirar faíscas. O outro era o poliporo-da-bétula, que cresce "
            "quase só nessa árvore. Ele contém ácido agárico, venenoso para o tricurídeo, Trichuris trichiura, um "
            "verme do intestino, e tem fama de vermífugo; por isso, os pesquisadores acham provável que Ötzi o "
            "usasse como remédio. Há quem especule que servisse de laxante para expulsar os vermes. O detalhe que "
            "fecha a história veio do próprio corpo: o exame mostrou que Ötzi estava infectado por esse mesmo "
            "verme, embora não se saiba a gravidade da infecção. No estômago dele também havia restos de "
            "samambaia, tóxica para humanos, e uma das hipóteses é que ele a tenha comido como remédio contra os "
            "parasitas. Seja qual for o uso exato, os fungos mostram que, há mais de cinco milênios, um viajante "
            "dos Alpes levava consigo o fogo e, possivelmente, a farmácia."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Ötzi",
                "Among Ötzi's possessions were berries, two birch bark baskets, and two species of polypore mushrooms with leather strings through them. "
                "One of these, the birch fungus, is known to have anthelmintic properties, and was probably used for medicinal purposes. "
                "The other was a type of tinder fungus, included with part of what appeared to be a complex firelighting kit. "
                "The kit featured pieces of over a dozen different plants, in addition to flint and pyrite for creating sparks. [...] "
                "He was infected with Trichuris trichiura (whipworm), an intestinal parasite. The severity of the infection is unknown. [...] "
                "traces of Bracken fern, which is toxic to humans, were found in his stomach. "
                "Researchers hypothesized that he either consumed it as medicine to treat the parasites in his intestine",
                nome="Ötzi"),
            wiki("Fomitopsis_betulina",
                "commonly known as the birch polypore, birch bracket, or razor strop, is a common bracket fungus and, as the name suggests, grows almost exclusively on birch trees. [...] "
                "Agaric acid, found in the fruit body of the fungus, is poisonous to the parasitic whipworm Trichuris trichiura. "
                "The fungus was carried by \"Ötzi the Iceman\" — the 5,300 year old mummy found in Tyrol — "
                "with speculation that the fungus may have been used as a laxative to expel whipworm.",
                nome="Fomitopsis betulina"),
        ],
    },
    # 14 Candida auris: o fungo que talvez tenha aprendido a suportar calor
    {
        "temas_secundarios": ["doencas_infecciosas", "mudancas_climaticas"],
        "tipos_espanto": ["misterio_aberto", "conexao_inesperada"],
        "gancho": "Um fungo descrito só em 2009, no ouvido de uma paciente em Tóquio, surgiu como causa de infecções hospitalares em vários continentes. Uma hipótese é que o aquecimento global o fez tolerar o calor do corpo.",
        "explicacao": (
            "A Candida auris recebeu o nome do latim \"auris\", orelha, porque foi isolada do canal do ouvido de "
            "uma mulher de 70 anos num hospital geriátrico de Tóquio. Logo se viu que ela já circulava antes: os "
            "três primeiros casos de doença, na Coreia do Sul, publicados em 2011, incluíam uma amostra guardada "
            "desde 1996, e todos tinham sido confundidos com outra espécie. O fungo, que cresce como levedura, "
            "coloniza a pele, persiste por muito tempo em superfícies e equipamentos hospitalares e resiste a "
            "vários remédios. Quando chega ao sangue ou a órgãos, a mortalidade é de 30% a 60%. Em 2022, a "
            "Organização Mundial da Saúde o colocou em \"prioridade crítica\" entre 19 fungos ameaçadores. O "
            "mistério é a origem. Ao contrário de outras espécies de Candida, ele gosta de ambientes quentes e "
            "salgados e cresce a 40–42 °C. Há cinco grupos genéticos distintos, com distribuições geográficas "
            "diferentes, e o surgimento em três continentes foi atribuído ao aquecimento global. Para o "
            "microbiologista Arturo Casadevall, seria o começo da adaptação dos fungos a temperaturas mais altas. "
            "Outra análise de DNA aponta uma separação das linhagens há pelo menos 4 mil anos e liga a "
            "resistência ao uso de fungicidas do tipo azol na agricultura. As explicações ainda são especulativas."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "hipotese",
        "fontes": [wiki("Candida_auris",
            "Candida auris (Candidozyma auris) is a species of fungus that grows as a yeast. [...] "
            "A colonizer of the skin in people most commonly in long term care medical facilities and other healthcare settings, "
            "C. auris may also persist on inanimate surfaces and medical devices for long periods of time. [...] "
            "It has attracted widespread attention because of its multiple drug resistance. "
            "In cases where the fungus spreads to the bloodstream or distal organs, the mortality rate is 30-60%. [...] "
            "Candida auris was first described in 2009 after it was isolated from the ear canal of a 70-year-old Japanese woman in Tokyo, Japan. [...] "
            "Candida auris thrives in warmer environments with high salt (unlike other candida species) and is thought to have emerged as a human pathogen due to global warming. "
            "It is grouped into five different clades, each with distinct genetic and clinical (such as virulence and anti-fungal resistance) properties, as well as different geographic distributions. "
            "DNA analysis of four distinct but drug-resistant strains of C. auris indicate an evolutionary divergence taking place at least 4,000 years ago, "
            "with a common leap among the four varieties into drug-resistance possibly linked to widespread azole-type antifungal use in agriculture. "
            "However, explanations for its emergence remain speculative. [...] "
            "in 2022 the World Health Organization (WHO) classified C. auris as one of its 19 fungal \"priority pathogens\" [...] "
            "with Candida auris being designated \"critical priority\" by the WHO. [...] "
            "Its name comes from the Latin word for ear, aus (genitive auris). [...] "
            "the ear canal of a 70-year-old Japanese woman at the Tokyo Metropolitan Geriatric Hospital in Japan. [...] "
            "The first three cases of disease-causing C. auris were reported from South Korea in 2011. "
            "Two isolates had been obtained during a 2009 study, and a third was discovered in a stored sample from 1996. [...] "
            "Notably, the isolates initially were misidentified as Candida haemulonii [...] "
            "The emergence of Candida auris on three continents is proposed to be as a result of global warming caused by climate change [...] "
            "candida auris can grow in culture at unusually high temperatures (40-42 degrees Celsius). [...] "
            "What this study suggests is this is the beginning of fungi adapting to higher temperatures",
            nome="Candida auris")],
    },
    # 15 Beatrix Potter, micóloga barrada
    {
        "temas_secundarios": ["literatura", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "A criadora de Pedro Coelho, Beatrix Potter, estudou fungos ao microscópio. Seu artigo sobre esporos foi lido por um homem na Sociedade Lineana, pois mulheres não podiam participar. Em 1997, a sociedade pediu desculpas.",
        "explicacao": (
            "Na década de 1890, o interesse científico de Beatrix Potter se concentrou nos fungos. Ela começou "
            "atraída pelas cores e pela vida curta dos cogumelos, que adorava pintar. Em 1892, conheceu o "
            "naturalista Charles McIntosh, que a ajudou a deixar os desenhos mais precisos, ensinou taxonomia e lhe "
            "mandava exemplares vivos no inverno. Curiosa sobre como os fungos se reproduzem, passou a desenhar "
            "esporos ao microscópio e, em 1895, formulou uma teoria sobre a germinação deles. Por meio de um tio "
            "químico, consultou botânicos do jardim de Kew e convenceu um deles, George Massee. Mas o diretor de "
            "Kew a rejeitou por ser mulher e amadora. Em 1897, ela enviou à Sociedade Lineana de Londres o artigo "
            "\"Sobre a germinação dos esporos das Agaricíneas\"; quem o apresentou foi Massee, porque mulheres não "
            "podiam assistir às sessões nem ler os próprios trabalhos. Depois, ela retirou o artigo, ao perceber "
            "que algumas amostras estavam contaminadas. Só nos seus trinta anos publicou, por conta própria, o "
            "livro de Pedro Coelho, e passou a se dedicar aos livros infantis. Os desenhos de fungos que doou a um "
            "museu de Ambleside, na Inglaterra, ainda são consultados por micologistas para identificar espécies. "
            "Em 1997, a Sociedade Lineana pediu desculpas póstumas pelo sexismo com que tratou a pesquisa dela."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Beatrix_Potter",
            "Potter's study and watercolours of fungi led to her being widely respected in the field of mycology. "
            "In her thirties, Potter self-published the highly successful children's book The Tale of Peter Rabbit. "
            "Following this, Potter began writing and illustrating children's books full-time. [...] "
            "By the 1890s, her scientific interests centred on mycology. "
            "First drawn to fungi because of their colours and evanescence in nature and her delight in painting them, "
            "her interest deepened after meeting Charles McIntosh, a revered naturalist and amateur mycologist, during a summer holiday in Dunkeld in Perthshire in 1892. "
            "He helped improve the accuracy of her illustrations, taught her taxonomy, and supplied her with live specimens to paint during the winter. "
            "Curious as to how fungi reproduced, Potter began microscopic drawings of fungus spores (the agarics) and in 1895 developed a theory of their germination. "
            "Through the connections of her uncle Sir Henry Enfield Roscoe, a chemist and vice-chancellor of the University of London, she consulted with botanists at Kew Gardens, "
            "convincing George Massee of her ability to germinate spores [...] "
            "Rebuffed by William Thiselton-Dyer, the Director at Kew, because of her sex and amateur status, "
            "Potter wrote up her conclusions and submitted a paper, On the Germination of the Spores of the Agaricineae, to the Linnean Society in 1897. "
            "It was introduced by Massee because, as a woman, Potter could neither attend proceedings nor read her paper. "
            "She subsequently withdrew it, realising that some of her samples were contaminated [...] "
            "Potter later gave her other mycological and scientific drawings to the Armitt Museum and Library in Ambleside, where mycologists still refer to them to identify fungi. [...] "
            "In 1997, the Linnean Society issued a posthumous apology to Potter for the sexism displayed in its handling of her research.",
            nome="Beatrix Potter")],
    },
]
