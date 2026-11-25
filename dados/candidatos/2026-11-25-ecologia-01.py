LOTE = "2026-11-25-ecologia-01"
AREA = "biologia"
TEMA = "ecologia"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 lobos de Yellowstone: a lenda e o quadro real
    {
        "temas_secundarios": ["comportamento_animal", "agua_doce_gelo"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "A volta dos lobos a Yellowstone virou lenda: os lobos que \"mudaram rios\". O quadro real é mais complicado: num experimento, os salgueiros só voltaram com cerca contra herbívoros e represas imitando as dos castores.",
        "explicacao": (
            "Os lobos foram eliminados do parque por volta de 1930 e reintroduzidos em 1995 e 1996. Sem predador, "
            "os rebanhos de elk, um grande cervo, cresceram e reduziram os bosques de álamos e salgueiros, e as "
            "colônias de castores sumiram. Depois da volta dos lobos, parte dessas perdas se reverteu em alguns "
            "lugares, e a história ficou famosa como exemplo de cascata trófica, inclusive num vídeo popular, "
            "\"How Wolves Change Rivers\", que alguns cientistas consideram exagerado. O sistema é mais complexo. "
            "Ele é aberto, sofre influências de fora do parque, e elks e bisões têm cinco predadores de topo: "
            "ursos-pardos, ursos-negros, pumas, lobos e caçadores humanos em Montana. Ursos-pardos e pumas também "
            "aumentaram no período. Uma análise de 21 anos de dados concluiu que a mudança de comportamento dos "
            "elks provocada pelos lobos pode ser deixada de lado para entender a cascata local. E o parque não "
            "voltou ao estado anterior: sem as represas dos castores, os riachos correram mais rápido, escavaram "
            "o leito e o lençol freático baixou, condições ruins para os salgueiros. Num raro experimento de "
            "campo, só cercar a área contra herbívoros não bastou; os salgueiros se restabeleceram apenas com a "
            "cerca somada a represas artificiais imitando as de castor."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Trophic_cascade",
                "In popular media, the reintroduction of gray wolves (Canis lupus) to Yellowstone National Park is often celebrated as an example of a terrestrial trophic cascade in which the wolves \"changed rivers\" and \"saved\" the park. "
                "In reality, the Greater Yellowstone Ecosystem is too complex to serve as an example of a straightforward trophic cascade. "
                "The system is open, affected by conditions outside of the park, and it has been influenced by a range of human-made and natural, time-varying factors other than the reintroduction of wolves. "
                "Two dominant herbivores, American bison (Bison bison) and elk (Cervus canadensis), are predated on by five top predators, grizzly bears (Ursus arctos horribilis) and black bears (Ursus americanus), cougars (Puma concolor), wolves and human hunters in Montana. [...] "
                "Both the exterpation of gray wolves (Canis lupus) in Yellowstone National Park, complete by about 1930, and the reintroduction of them in 1995 and 1996 was followed by dramatic changes throughout trophic cascades. "
                "Freed from wolf predation, expanding elk herds reduced stands of aspen (Populus tremuloides), cottonwoods (Populus spp.), and willows (Salix spp.), and eliminated riparian plant and animal communities including beaver colonies. [...] "
                "Some of the decreases in plants and animals listed above have been locally reversed after the wolf reintroduction. [...] "
                "The elimination of beavers - and hence their dams - caused increased creek flow rates and erosion. "
                "Creek beds were lowered and with them the water table adjacent to the creek. "
                "These conditions are unfavorable for willow growth and hence beavers. "
                "A rare controlled in-situ experiment established that only the fencing out of herbivores combined with human-made \"beaver\" dams allowed willows to reestablish themselves. "
                "The mere fencing out of ungulates was insufficient. [...] "
                "A complex analysis of 21 years of observations of wolves, elk and aspen in the Northern Range concluded that \"trait-mediated indirect effects,\" changes in elk behavior triggered by the wolves, can be ignored in the understanding of the local trophic cascades. "
                "The reintroduction and subsequent increasing numbers of Yellowstone wolves were paralleled by an increase in grizzly bears (Ursus arctos horribilis) which had been mismanaged by the National Park Service. "
                "Likewise, cougars (Puma concolor) became more abundant.",
                nome="Trophic cascade"),
            wiki("Ecology_of_fear",
                "The YouTube video How Wolves Change Rivers presented a popular account of the subject, but some scientists described it as an overstatement.",
                nome="Ecology of fear"),
        ],
    },
    # 2 Paine, a estrela-do-mar e a espécie-chave
    {
        "temas_secundarios": ["vida_marinha"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Um ecólogo tirou as estrelas-do-mar de um trecho do litoral dos EUA. As poças, que tinham 15 espécies presas às rochas, ficaram com 8 e, dez anos depois, quase só com mexilhões. Assim nasceu a ideia de espécie-chave.",
        "explicacao": (
            "O zoólogo Robert T. Paine estudava os bichos da faixa entre as marés, e num artigo de 1966 descreveu o "
            "sistema da baía de Makah, no estado de Washington. A estrela-do-mar Pisaster ochraceus come de tudo: "
            "quítons, lapas, caracóis, cracas. Mas o prato favorito é um mexilhão que, sem controle, domina o "
            "espaço nas rochas. Quando Paine removeu as estrelas, os mexilhões cresceram por cima dos vizinhos: "
            "das 15 espécies iniciais restaram 8 depois de três anos, e após dez anos as poças estavam tomadas "
            "quase só por eles. Em 1969, Paine propôs o termo espécie-chave, em inglês keystone, a pedra do alto de "
            "um arco: é a que menos sofre pressão, mas sem ela o arco desaba. Do mesmo jeito, uma espécie pouco "
            "abundante pode ter efeito desproporcional no ecossistema. A ideia fez sucesso, talvez até demais: "
            "uma pesquisadora contou 230 espécies chamadas de \"chave\" em uns 157 estudos nos 50 anos seguintes. "
            "E o contexto importa. Outro ecólogo mostrou que a mesma estrela-do-mar era decisiva em costões batidos "
            "por ondas fortes, mas bem menos em locais abrigados, e o próprio Paine dizia que no Alasca, sem aquele "
            "mexilhão como presa, ela era \"só mais uma estrela-do-mar\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Keystone_species",
            "A keystone species is a species that has a disproportionately large effect on its natural environment relative to its abundance. "
            "The concept was introduced in 1969 by the zoologist Robert T. Paine. [...] "
            "The role that a keystone species plays in its ecosystem is analogous to the role of a keystone in an arch. "
            "While the keystone is under the least pressure of any of the stones in an arch, the arch still collapses without it. [...] "
            "Paine developed the concept to explain his observations and experiments on the relationships between marine invertebrates of the intertidal zone (between the high and low tide lines), including starfish and mussels. "
            "He removed the starfish from an area, and documented the effects on the ecosystem. "
            "In his 1966 paper, Food Web Complexity and Species Diversity, Paine had described such a system in Makah Bay in Washington. [...] "
            "The ochre starfish is a generalist predator and feeds on chitons, limpets, snails, barnacles, echinoids, and even decapod crustacea. "
            "The favourite food for these starfish is the mussel which is a dominant competitor for the space on the rocks. [...] "
            "When Paine removed the ochre starfish, the mussels quickly outgrew the other species crowding them out. "
            "At the start, the rock pools held 15 rock-clinging species. "
            "Three years later there were 8 such species; and ten years later the pools were largely occupied by a single species, mussels. [...] "
            "the researcher Ishana Shukla has listed 230 species identified as keystones in some 157 studies in the 50 years since Paine's paper. "
            "Menge's own work has shown that the purple Pisaster sea star that Paine had studied was a powerful keystone species in places exposed to strong wave action, but was far less important in sheltered places. "
            "Paine had indeed stated that in Alaska, without the relevant mussel species as prey, the predatory Pisaster was \"just another sea star\".",
            nome="Keystone species")],
    },
    # 3 a bomba de baleia
    {
        "temas_secundarios": ["vida_marinha", "oceanografia"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Baleias comem em profundidade e fazem cocô na superfície. No golfo do Maine, segundo um estudo, baleias e focas devolvem às águas iluminadas mais nitrogênio por ano do que todos os rios juntos, adubando o plâncton.",
        "explicacao": (
            "No oceano, a tendência é os nutrientes afundarem: restos e detritos descem da superfície para o fundo, "
            "a chamada \"neve marinha\". As baleias invertem parte desse fluxo. Elas se alimentam em profundidade, "
            "onde está o krill, mas ficam presas à superfície para respirar, e suas fezes saem em plumas soltas que "
            "tendem a se dispersar em vez de afundar. Num estudo publicado em 2010, Joe Roman e James McCarthy "
            "coletaram plumas fecais de jubartes e acharam nelas concentrações de nitrogênio até cem vezes maiores "
            "que as da água em volta. Pelas contas dos dois, baleias e focas repõem cerca de 23 mil toneladas de "
            "nitrogênio por ano na camada iluminada do golfo do Maine, mais que todos os rios juntos. Antes da caça "
            "comercial, essa \"bomba de baleia\" era bem mais forte: a reciclagem de nitrogênio pelos mamíferos "
            "marinhos provavelmente passava de três vezes o que chega da atmosfera. Para os autores, matar baleias e "
            "focas por competirem com a pesca pode sair pela culatra, pois reduziria o nitrogênio disponível e a "
            "produtividade do mar. No oceano Antártico, rico em outros nutrientes mas pobre em ferro, as fezes ricas "
            "em ferro das baleias que comem krill cumprem papel parecido."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0013255",
             "titulo": "The Whale Pump: Marine Mammals Enhance Primary Productivity in a Coastal Basin (PLOS ONE, 2010)",
             "idioma": "en",
             "trecho": "we find that marine mammals can enhance primary productivity in their feeding areas by concentrating nitrogen near the surface through the release of flocculent fecal plumes. "
                       "Whales and seals may be responsible for replenishing 2.3×104 metric tons of N per year in the Gulf of Maine's euphotic zone, more than the input of all rivers combined. "
                       "This upward “whale pump” played a much larger role before commercial harvest, when marine mammal recycling of nitrogen was likely more than three times atmospheric N input. [...] "
                       "Published: October 11, 2010 [...] "
                       "Excretion for marine mammals, tethered to the surface for respiration [...] "
                       "releasing fecal material “that tends to disperse rather than sink when it is released.” [...] "
                       "PON concentrations of the humpback fecal plume samples were elevated by as much as two orders of magnitude above typical mixed-layer concentrations for summer in this area [...] "
                       "An unintended effect of bounty programs and culls could be reduced availability of nitrogen in the euphotic zone and decreased overall productivity."},
            wiki("Whale_pump",
                "Whales feed at deeper levels of the ocean where krill is found. "
                "The fecal action of whales thus reverses the usual flow of nutrients of the ocean's \"biological pump\" due to the downward flow of \"marine snow\" and other detritus from surface to bottom. [...] "
                "In addition, the feces of krill-eating whales are rich in iron. [...] "
                "The Southern Ocean is amongst the largest ranges for phytoplankton and has the characteristic of being nutrient-rich in terms of phosphate, nitrate and silicate, while it is iron-deficient at the same time.",
                nome="Whale feces (Whale pump)"),
        ],
    },
    # 4 salmão que vira folha
    {
        "temas_secundarios": ["plantas", "agua_doce_gelo"],
        "tipos_espanto": ["conexao_inesperada", "escala_absurda"],
        "gancho": "Em florestas da costa do Canadá, parte do nitrogênio das plantas vem do mar: ursos levam salmões para a mata e largam os restos. Num estudo, a fatia estimada foi de 10% a 60%, conforme a planta e o rio.",
        "explicacao": (
            "Os salmões do Pacífico nascem em água doce, passam a maior parte da vida adulta no oceano e sobem os "
            "rios para desovar. Depois da desova, morrem, e os nutrientes do corpo deles, vindos do mar, ficam no "
            "rio, nos animais e nas matas da margem. Ursos e lobos ajudam a espalhá-los: levam as carcaças para a "
            "mata, comem só uma parte, e o resto alimenta uma fila de necrófagos, de vertebrados a invertebrados. "
            "Em Haida Gwaii, um único urso chegou a pegar 700 salmões em 40 dias de desova. Para medir quanto "
            "desse nitrogênio chega às plantas, pesquisadores da Colúmbia Britânica usaram a proporção de isótopos "
            "de nitrogênio como marcador. E compararam a vegetação logo acima e logo abaixo de cachoeiras que os "
            "salmões não conseguem subir, em dois rios: assim, solo, clima e distância do mar eram parecidos, mas "
            "só um dos lados recebia salmão. Abaixo das quedas, a assinatura isotópica do nitrogênio era mais forte em "
            "todas as espécies de plantas, indicando que de 10% a 60% do nitrogênio das folhas tinha origem "
            "marinha. Plantas típicas de solo rico em nitrogênio também eram mais comuns ali. Os autores ressalvam "
            "que as estimativas mais altas podem estar infladas."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC156615/fullTextXML",
             "titulo": "Nitrogen uptake in riparian plant communities across a sharp ecological boundary of salmon density (BMC Ecology, 2003)",
             "idioma": "en",
             "trecho": "salmon nutrients are transferred from streams into adjacent forests by bears and wolves where remnants of the partially-consumed carcasses are used by a diverse assemblage of vertebrate and invertebrate scavengers [...] "
                       "Individual bears captured up to 700 salmon over a 40 day salmon spawning period at Bag Harbour, most of which were carried into the riparian zone and only partially consumed [...] "
                       "Interpretations of the nitrogen and carbon isotope ratios, which provide the major proxy for quantifying contribution of salmon-derived nutrients to other taxa, [...] "
                       "we made comparisons across a sharp ecological boundary of salmon density that resulted from a waterfall barrier to salmon migration. [...] "
                       "values were enriched by 1.4‰ to 9.0‰ below the falls depending on species and watershed, providing a relative contribution of marine-derived nitrogen (MDN) to vegetation of 10% to 60%. [...] "
                       "Community structure also differed with higher incidence of nitrogen-rich soil indicator species below the waterfalls. [...] "
                       "enrichment in all species of vegetation across waterfalls that are a barrier to salmon migration on two geographically separated watersheds on the mid-coast of British Columbia. [...] "
                       "Within-watershed comparisons of conspecifics collected immediately above and below the waterfalls minimize differences such as site history, substrate, proximity to the stream and ocean, and microclimate [...] "
                       "It is possible that our estimates of MDN, which reach 60% of total foliar nitrogen, are inflated."},
            wiki("Salmon_run",
                "A salmon run is an annual fish migration event where many salmon species, which are typically hatched in fresh water and live most of their adult life downstream in the ocean, swim back against the stream to the upper reaches of rivers to spawn on the gravel beds of small creeks. "
                "After spawning, most Atlantic salmon and all species of Pacific salmon die [...] "
                "the significant nutrients in their carcasses, rich in nitrogen, sulfur, carbon and phosphorus, are transferred from the ocean and released to inland aquatic ecosystems, terrestrial animals (such as bears) and the wetlands and riparian woodlands adjacent to the rivers.",
                nome="Salmon run"),
        ],
    },
    # 5 ratos em terra, recifes mais pobres
    {
        "temas_secundarios": ["vida_marinha", "oceanografia"],
        "tipos_espanto": ["conexao_inesperada", "escala_absurda"],
        "gancho": "No arquipélago de Chagos, ilhas sem ratos tinham 760 vezes mais aves marinhas. O guano delas aduba o mar: nos recifes em volta, os peixes somavam 48% mais biomassa. Ratos em terra empobrecem o recife.",
        "explicacao": (
            "Aves marinhas pescam em mar aberto e voltam às ilhas para descansar e se reproduzir, deixando no solo o "
            "guano, rico em nitrogênio e fósforo. Ratos-pretos, provavelmente levados por humanos no fim do século "
            "XVIII e começo do XIX, comem ovos, filhotes e até aves adultas. No arquipélago de Chagos, no meio do "
            "oceano Índico, algumas ilhas têm ratos e outras não, o que criou um raro experimento natural. Uma "
            "equipe liderada por Nick Graham, da Universidade de Lancaster, comparou seis ilhas de cada tipo. Nas "
            "ilhas sem ratos, a densidade de aves era 760 vezes maior e a deposição de nitrogênio, 251 vezes. A "
            "marca desse nitrogênio de origem oceânica aparecia no solo e nos arbustos e também, já no mar, em "
            "algas, esponjas e peixes dos recifes vizinhos. Ali, os peixes somavam 48% mais biomassa, e o pastejo "
            "de algas por peixes, que ajuda a deixar uma base firme para novos corais, era 3,2 vezes maior. Para "
            "os autores, cujo estudo saiu na Nature em 2018, erradicar ratos de ilhas oceânicas deveria ser "
            "prioridade, porque devolveria às ilhas e aos recifes os nutrientes que as aves trazem do mar."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:29995864&resultType=core&format=json",
             "titulo": "Seabirds enhance coral reef productivity and functioning in the absence of invasive rats (Nature, 2018), resumo via Europe PMC",
             "idioma": "en",
             "trecho": "Here we address this question using a rare natural experiment in the Chagos Archipelago, in which some islands are rat-infested and others are rat-free. "
                       "We found that seabird densities and nitrogen deposition rates are 760 and 251 times higher, respectively, on islands where humans have not introduced rats. "
                       "Consequently, rat-free islands had substantially higher nitrogen stable isotope [...] "
                       "values in soils and shrubs, reflecting pelagic nutrient sources. [...] "
                       "were also apparent in macroalgae, filter-feeding sponges, turf algae and fish on adjacent coral reefs. [...] "
                       "fish communities had higher biomass across trophic feeding groups, with 48% greater overall biomass. "
                       "Rates of two critical ecosystem functions, grazing and bioerosion, were 3.2 and 3.8 times higher, respectively, adjacent to rat-free islands. [...] "
                       "rat eradication on oceanic islands should be a high conservation priority as it is likely to benefit terrestrial ecosystems and enhance coral reef productivity and functioning by restoring seabird-derived nutrient subsidies from large areas of ocean."},
            {"url": "https://www.lancaster.ac.uk/news/eradicate-rats-to-bolster-coral-reefs",
             "titulo": "Eradicate rats to bolster coral reefs (Lancaster University, 2018)",
             "idioma": "en",
             "trecho": "11 July 2018 [...] "
                       "which feed on bird eggs, chicks, and even adults birds [...] "
                       "Lead author Professor Nick Graham of Lancaster University, UK, said: [...] "
                       "Seabirds are crucial to these kinds of islands because they are able to fly to highly productive areas of open ocean to feed. "
                       "They then return to their island homes where they roost and breed, depositing guano [...] "
                       "This guano is rich in the nutrients, nitrogen and phosphorus. [...] "
                       "thought to have been introduced in the late 1700s and early 1800s. [...] "
                       "close to the six rat-free and six rat-infested islands [...] "
                       "providing a stable base for new coral growth"},
        ],
    },
    # 6 o verme que leva grilos às trutas
    {
        "temas_secundarios": ["insetos", "agua_doce_gelo"],
        "tipos_espanto": ["conexao_inesperada", "escala_absurda"],
        "gancho": "Num riacho do Japão, grilos e gafanhotos infectados por um verme parasita tinham 20 vezes mais chance de entrar na água, onde o verme sai. Uma truta ameaçada os come: eram 60% da energia anual dela.",
        "explicacao": (
            "Os nematomorfos, conhecidos em inglês como vermes-crina-de-cavalo, vivem adultos na água, mas as larvas "
            "crescem dentro de artrópodes, como grilos e gafanhotos. Para completar o ciclo, o parasita precisa "
            "voltar à água, e há evidências de que manipula o hospedeiro para isso. Segundo Thomas e colegas, o "
            "inseto infectado primeiro anda de modo errático, o que cedo ou tarde o leva perto de um riacho, e então "
            "muda de comportamento e entra na água. Takuya Sato e colegas mediram as consequências num riacho de "
            "cabeceira do Japão, em estudo publicado em 2011. Grilos-de-caverna e gafanhotos infectados tinham 20 "
            "vezes mais chance de entrar no riacho. Lá, uma truta japonesa ameaçada de extinção os comia sem "
            "hesitar e, como eram muitos, esses insetos respondiam por 60% da energia que a população de trutas "
            "obtinha no ano. As trutas cresciam mais depressa no outono, justamente quando os parasitas empurravam "
            "os insetos para a água. E, com essa fartura, comiam menos invertebrados do fundo do riacho do que a "
            "abundância deles faria esperar, o que pode ter efeitos em cadeia entre a floresta e o rio. Para os "
            "autores, foi a primeira evidência quantitativa de que um parasita manipulador pode alterar tanto o "
            "fluxo de energia de um ecossistema."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": "https://pubs.usgs.gov/publication/70004681",
             "titulo": "Nematomorph parasites drive energy flow through a riparian ecosystem (Ecology, 2011), resumo no USGS Publications Warehouse",
             "idioma": "en",
             "trecho": "Sato, T., Watanabe, K., Kanaiwa, M., Niizuma, Y., Harada, Y., and Lafferty, K.D., 2011, Nematomorph parasites drive energy flow through a riparian ecosystem [...] "
                       "In a Japanese headwater stream, camel crickets and grasshoppers (Orthoptera) were 20 times more likely to enter a stream if infected by a nematomorph parasite (Gordionus spp.), corroborating evidence that nematomorphs manipulate their hosts to seek water where the parasites emerge as free‐living adults. "
                       "Endangered Japanese trout (Salvelinus leucomaenis japonicus) readily ate these infected orthopterans, which due to their abundance, accounted for 60% of the annual energy intake of the trout population. "
                       "Trout grew fastest in the fall, when nematomorphs were driving energy‐rich orthopterans into the stream. "
                       "When infected orthopterans were available, trout did not eat benthic invertebrates in proportion to their abundance, leading to the potential for cascading, indirect effects through the forest‐stream ecosystem. "
                       "These results provide the first quantitative evidence that a manipulative parasite can dramatically alter the flow of energy"},
            wiki("Nematomorpha",
                "commonly known as horsehair worms, hairsnakes, or Gordian worms) are a phylum of parasitoid animals [...] "
                "The adult worms are free-living, but the larvae are parasitic on arthropods, such as beetles, cockroaches, mantises, orthopterans, and crustaceans. [...] "
                "according to Thomas et al., the \"infected insects may first display an erratic behaviour which brings them sooner or later close to a stream and then a behavioural change that makes them enter the water\"",
                nome="Nematomorpha"),
        ],
    },
    # 7 o medo sozinho encolhe famílias
    {
        "temas_secundarios": ["comportamento_animal", "emocoes"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Pardais com ninhos blindados contra predadores, mas que ouviam gravações de predadores, tiveram 40% menos filhotes no ano. Só o medo, sem nenhum ataque, encolheu as famílias.",
        "explicacao": (
            "O experimento foi feito por Liana Zanette, da Universidade de Western Ontario, e Michael Clinchy com "
            "pardais-cantores em Portland Island e outras ilhotas da Colúmbia Britânica, no Canadá, e saiu na "
            "revista Science em 2011. Cada ninho foi protegido com cerca elétrica e rede de pesca, para que "
            "gaviões, guaxinins e outros predadores não pudessem atacar, e câmeras vigiavam dia e noite para "
            "garantir que nenhum ovo ou filhote fosse morto. Durante os quatro meses da temporada de reprodução, "
            "um grupo de aves ouvia sons de seus predadores naturais; o outro, sons naturais inofensivos. As aves "
            "expostas aos predadores produziram 40% menos filhotes. Para os autores, só a percepção do risco já "
            "pesa na dinâmica das populações: predadores afetam as presas não apenas matando, mas assustando. Se "
            "for assim, o estrago de predadores introduzidos seria pior do que se imaginava, e o sumiço de "
            "predadores nativos teria mexido mais nos ecossistemas do que se pensava. Essa linha de pesquisa é "
            "chamada de \"ecologia do medo\", termo usado num artigo de 1999. Há ressalvas: críticos lembram que "
            "os aspectos cognitivos e emocionais da fuga de predadores continuam incertos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://uvic.ca/news/topics/2011+fear-of-predation-affects-animal-populations+media-release",
             "titulo": "Fear of Predation Affects Animal Populations (University of Victoria, 2011)",
             "idioma": "en",
             "trecho": "December 8, 2011 [...] "
                       "Just the fear of anticipated attack is enough to significantly affect wildlife population numbers, even when predators are prevented from directly killing any prey. [...] "
                       "He and lead study author Liana Zanette, a biologist at the University of Western Ontario, conducted their ground-breaking research on song sparrows nesting on Portland Island and several other small islands in BC’s southern Gulf Islands. "
                       "They protected every nest with both electric fencing and seine (fish) netting, making is impossible for natural predators such as hawks and raccoons to attack. "
                       "Cameras were trained on the nests 24/7 so the researchers were confident no eggs or nestlings were directly killed by predators during the observation period. "
                       "The researchers then played different sounds to different groups of birds throughout the four-month breeding season. "
                       "One group heard sounds associated with their natural predators while the other heard non-threatening natural sounds. "
                       "“The birds that were hearing the predator sounds produced 40 per cent fewer offspring—simply due to the sound of fear—that’s a very significant decrease,” says Clinchy. "
                       "“What this shows is that predators significantly affect the population sizes of their prey not just by killing prey but by scaring them as well. [...] "
                       "This means that the adverse effects of introduced predators are likely worse than previously imagined and the disturbance to native ecosystems due to the loss of native predators has probably been greater than we previously thought.” [...] "
                       "is published in the December issue of Science magazine."},
            wiki("Ecology_of_fear",
                "The term was used in the 1999 paper \"The Ecology of Fear: Optimal Foraging, Game Theory, and Trophic Interactions\" [...] "
                "Some critics argue that the cognitive and emotional aspects of predator avoidance remain uncertain.",
                nome="Ecology of fear"),
        ],
    },
    # 8 sapo-cururu na Austrália
    {
        "temas_secundarios": ["evolucao"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Em 1935, a Austrália importou 102 sapos-cururus para comer besouros da cana. Não há evidência de que tenham reduzido os besouros, mas viraram mais de 200 milhões, e os da frente da invasão evoluíram pernas maiores.",
        "explicacao": (
            "O sapo-cururu é nativo da América do Sul e da América Central. Era usado contra pragas da cana em "
            "Porto Rico desde 1920, e um estudo de 1932 indicou que ele comia larvas de besouros que atacam a cana. "
            "Depois de passar pelo Havaí, chegou à Austrália em junho de 1935: eram 102 sapos, e um morreu na "
            "viagem. Em março de 1937, uns 62 mil filhotes criados em cativeiro já tinham sido soltos no norte de "
            "Queensland. Não há evidência de que tenham afetado o número de besouros da cana. Os sapos, por sua "
            "vez, passaram de 200 milhões em 2011 e foram vistos até nos arredores de Sydney. A invasão virou um "
            "laboratório de evolução. Na frente oeste do avanço, os sapos desenvolveram pernas maiores, o que "
            "parece ligado à capacidade de ir mais longe: o avanço, estimado em 40 km por ano em 1994, foi "
            "calculado em 60 km por ano em 2014. O preço: cerca de 10% desses sapos da vanguarda têm artrite. "
            "Do lado australiano também houve evolução. Em menos de 75 anos, uma cobra nativa, a cobra-preta-de-"
            "barriga-vermelha, ficou mais resistente ao veneno do sapo e passou a preferir menos comê-lo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Cane_toads_in_Australia",
            "Native to South and mainland Middle America, imported cane toads had been used in Puerto Rico to control sugar cane pests since 1920, and an influential 1932 research paper by Raquel Dexter showed that they largely ate beetle larvae that in turn ate sugar cane. "
            "Based on her findings, they were introduced to Hawaii by Cyril Pemberton in the early 1930s, and then introduced to Australia from Hawaii in June 1935 [...] "
            "In June 1935, 102 cane toads were imported to Gordonvale from Hawaii, with one dying in transit due to dehydration. "
            "By March 1937, some 62,000 toadlets were bred in captivity and then released in areas around Cairns, Gordonvale, and Innisfail in northern Queensland. [...] "
            "By 2011 they were estimated to number over 200 million [...] "
            "there is no evidence that they have affected the number of cane beetles which they were introduced to prey upon. [...] "
            "By 2022 cane toads had been sighted as far south as Bankstown, southwest of Sydney. [...] "
            "The toads on the western frontier of their advance have evolved larger legs, which is thought to be related to their ability to travel farther. "
            "As a consequence of their longer legs, larger bodies, and faster movement, about 10% of the leading-edge cane toads have also developed arthritis. "
            "The toads were estimated to be advancing the frontier at a rate if 40 km (25 mi) per year in 1994, and in 2014 the rate of advance was estimated to have risen to 60 km (37 mi) per year on the western front. [...] "
            "One research study concluded that in less than 75 years, the red-bellied black snake had evolved in toad-inhabited regions of Australia to have increased resistance to toad toxin and decreased preference for toads as prey.",
            nome="Cane toads in Australia")],
    },
    # 9 dois coelhos infectados e a Europa sem coelhos
    {
        "temas_secundarios": ["evolucao", "doencas_infecciosas"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Em 1952, um proprietário rural francês inoculou dois coelhos com o vírus da mixomatose para livrar suas terras deles. A doença varreu a Europa e derrubou em 99% a população de coelhos selvagens do Reino Unido.",
        "explicacao": (
            "A mixomatose é uma doença grave e muitas vezes fatal em coelhos-europeus. Na Austrália, onde os "
            "coelhos chegaram em 1788 com os colonos ingleses e viraram praga, o vírus foi solto em 1950 como "
            "controle biológico, com letalidade inicial estimada perto de 99,8%. Na França, em junho de 1952, "
            "Paul-Félix Armand-Delille, dono de uma propriedade no noroeste do país, inoculou o vírus em dois "
            "coelhos selvagens. Queria só acabar com os coelhos dali, mas a doença se espalhou rápido pela Europa "
            "ocidental, pela Irlanda e pelo Reino Unido; em parte, parece ter sido levada de propósito para essas "
            "ilhas. Pelas estimativas, os coelhos selvagens caíram 99% no Reino Unido, de 90% a 95% na França e 95% "
            "na Espanha. O efeito subiu a cadeia alimentar: predadores especializados em coelhos, como o "
            "lince-ibérico e a águia-imperial-ibérica, ficaram à beira da extinção. Com o tempo, nos dois "
            "continentes, o vírus ficou menos letal e os coelhos, mais resistentes. As formas mais brandas do vírus "
            "venceram porque deixavam o coelho doente vivo por mais tempo e assim eram transmitidas com mais "
            "facilidade. O caso virou exemplo clássico de coevolução entre hospedeiro e patógeno."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Myxomatosis",
            "Myxomatosis is the name of the severe and often fatal disease in European rabbits caused by the myxoma virus. [...] "
            "This process is regarded as a classical example of host–pathogen coevolution following cross-species transmission of a pathogen. [...] "
            "European rabbits were brought to Australia in 1788 by early English settlers. "
            "Initially used as a food source, they later became feral and their numbers soared. [...] "
            "In 1950, the SLS strain of myxoma virus from the South American tapeti (Sylvilagus brasiliensis) was released in Australia as a biological control agent against feral rabbits. "
            "The virus was at first highly lethal, with an estimated case fatality rate of close to 99.8%. "
            "Within a few years, however, this strain was replaced by less virulent ones, which permitted longer survival of infected rabbits and enhanced disease transmission. [...] "
            "In June 1952, Paul-Félix Armand-Delille, the owner of an estate in northwestern France, inoculated two wild rabbits with the Lausanne strain of myxoma virus. "
            "His intention was only to eradicate rabbits on his property, but the disease quickly spread through Western Europe, Ireland, and the United Kingdom. "
            "Some dissemination of the virus appeared deliberate, such as its introduction into the islands of Great Britain in 1953 and Ireland in 1954. [...] "
            "According to estimates, the wild rabbit population in the United Kingdom fell by 99%, in France by 90% to 95%, and in Spain by 95%. "
            "This in turn drove specialized rabbit predators, such as the Iberian lynx and the Spanish imperial eagle, to the brink of extinction. [...] "
            "As happened in Australia, the virus has generally become less virulent and the wild rabbit populations more resistant. [...] "
            "These attenuated strains, which allowed rabbits to survive longer, came to dominate because they were more readily transmitt",
            nome="Myxomatosis")],
    },
    # 10 a perca-do-nilo e a lenha
    {
        "temas_secundarios": ["agua_doce_gelo", "economia_curiosa"],
        "tipos_espanto": ["conexao_inesperada", "escala_absurda"],
        "gancho": "A perca-do-nilo, solta no lago Vitória nos anos 1950, é apontada como causa do sumiço de centenas de espécies nativas. E ela precisa ser defumada, não seca ao sol: a procura por lenha subiu numa região já desmatada.",
        "explicacao": (
            "A perca-do-nilo é um dos maiores peixes de água doce: chega a quase 2 metros e até 200 kg. Ela não é "
            "nativa do lago Vitória, na África Oriental, mas foi introduzida lá nos anos 1950 e passou a ser "
            "pescada comercialmente. É um dos exemplos mais citados do estrago que uma espécie exótica pode "
            "causar: a introdução é apontada como causa da extinção, ou quase extinção, de várias centenas de "
            "espécies nativas. No começo, a perca comia sobretudo os ciclídeos nativos; quando eles rarearam, "
            "passou a comer principalmente pequenos camarões e peixinhos. O impacto foi além da água. Os ciclídeos "
            "eram tradicionalmente secos ao sol, mas a perca tem mais gordura e, para não estragar, precisa ser "
            "defumada. Isso aumentou a procura por lenha numa região já castigada por desmatamento, erosão do solo "
            "e desertificação. Ao mesmo tempo, o peixe virou negócio de exportação: em 2003, as vendas para a "
            "União Europeia chegaram a 169 milhões de euros. A teia alimentar do lago parece ter ficado "
            "drasticamente empobrecida e, embora caminhe para um novo equilíbrio, nem o estado anterior do lago "
            "nem o da pesca podem ser recuperados com facilidade. O grupo de especialistas em espécies invasoras "
            "da IUCN inclui a perca-do-nilo entre as 100 piores invasoras do mundo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Nile_perch",
            "The World Conservation Union's Invasive Species Specialist Group considers L. niloticus one of the world's 100 worst invasive species. [...] "
            "One of the largest freshwater fishes, it reaches a maximum length of nearly 2 m (6 ft 7 in), weighing up to 200 kg (440 lb). [...] "
            "a misleading trade name, as the species is not native to Lake Victoria, though they have been introduced there [...] "
            "The introduction of this species to Lake Victoria is one of the most cited examples of the negative effects alien species can have on ecosystems. "
            "The Nile perch was introduced to Lake Victoria in East Africa in the 1950s, and has since been fished commercially. "
            "In 2003, Nile perch sales to the EU reached 169 million euros. [...] "
            "Its introduction was ecologically disruptive and is attributed with causing the extinction or near-extinction of several hundred native species [...] "
            "The Nile perch initially fed on native cichlids, but with decreasing availability of this prey, it now consumes mainly small shrimp and minnows. [...] "
            "Native cichlids were traditionally sun-dried, but because Nile perch have a high fat content (higher than cichlids), they need to be smoked to avoid spoiling. "
            "This has led to an increased demand for firewood in a region already hard-hit by deforestation, soil erosion, and desertification. [...] "
            "the trophic web of Lake Victoria appears to have been drastically impoverished by the introduction of this novel near-top-level predator. "
            "While the ecosystem seems to be moving towards a new equilibrium, neither its former state nor the state of fisheries on Lake Victoria can ever easily be brought back.",
            nome="Nile perch")],
    },
    # 11 ilhas esvaziadas de propósito
    {
        "temas_secundarios": ["insetos"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Para testar uma teoria sobre ilhas, dois ecólogos fumigaram ilhotas de mangue na Flórida até eliminar seus artrópodes. Em um ano, o número de espécies voltou ao de antes, e mais rápido nas ilhas perto do continente.",
        "explicacao": (
            "A biogeografia de ilhas nasceu nos anos 1960 com Robert MacArthur e Edward O. Wilson, que tentaram "
            "prever quantas espécies existiriam numa ilha recém-formada. A teoria propõe que esse número resulta "
            "do saldo entre espécies que chegam e espécies que se extinguem localmente, até um nível de equilíbrio; "
            "a distância do continente afeta a chegada de imigrantes. Wilson e seu aluno Daniel Simberloff testaram "
            "a ideia em ilhotas de mangue nas Florida Keys. Primeiro fizeram um censo das espécies. Depois "
            "fumigaram as ilhas com brometo de metila para eliminar os artrópodes e acompanharam a chegada dos "
            "novos colonizadores. Em um ano, as ilhas tinham voltado aos níveis anteriores, e as mais próximas do "
            "continente se recuperaram mais depressa, como a teoria previa. Para os dois, o número final de "
            "espécies oscilava num quase equilíbrio. O efeito do tamanho não pôde ser testado, porque as ilhas "
            "eram parecidas. O trabalho, parte da tese de doutorado de Simberloff, ganhou em 1971 o prêmio Mercer "
            "da Sociedade Ecológica da América e entrou numa seleção de quarenta artigos clássicos da ecologia. Mais "
            "tarde, Simberloff criticou o uso da teoria para defender que uma reserva grande sempre protege mais "
            "espécies que várias pequenas, uma simplificação não comprovada, em sua opinião."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Insular_biogeography",
                "The field was started in the 1960s by the ecologists Robert H. MacArthur and E. O. Wilson, who coined the term island biogeography in their inaugural contribution to Princeton's Monograph in Population Biology series, which attempted to predict the number of species that would exist on a newly created island. [...] "
                "The theory of insular biogeography proposes that the number of species found in an undisturbed insular environment (\"island\") is determined by immigration and extinction. [...] "
                "Immigration and emigration are affected by the distance of an islan [...] "
                "Over time, the countervailing forces of extinction and immigration result in an equilibrium level of species richness. [...] "
                "The theory of island biogeography was experimentally tested by E. O. Wilson and his student Daniel Simberloff in the mangrove islands in the Florida Keys. "
                "Species richness on several small mangroves islands were surveyed. "
                "The islands were fumigated with methyl bromide to clear their arthropod communities. "
                "Following fumigation, the immigration of species onto the islands was monitored. "
                "Within a year the islands had been recolonized to pre-fumigation levels. "
                "However, Simberloff and Wilson contended this final species richness was oscillating in quasi-equilibrium. "
                "Islands closer to the mainland recovered faster as predicted by the Theory of Island Biogeography. "
                "The effect of island size was not tested, since all islands were of approximately equal size. [...] "
                "conservation planning was taking the view that the one large reserve could hold more species than several smaller reserves [...] "
                "This led to concern by other ecologists, including Dan Simberloff, who considered this to be an unproven over-simplification that would damage conservation efforts.",
                nome="Insular biogeography"),
            wiki("Daniel_Simberloff",
                "Simberloff's doctoral dissertation tested the theory of island biogeography proposed by Robert H. MacArthur and Edward O. Wilson, resulting in a paper that won the Ecological Society of America's Mercer Award in 1971 and was included as one of forty classic papers that represented the foundations of ecology.",
                nome="Daniel Simberloff"),
        ],
    },
    # 12 pica-bois: parceiros ou vampiros?
    {
        "temas_secundarios": ["comportamento_animal"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "Os pássaros que catam carrapatos no lombo de búfalos e girafas são o exemplo clássico de parceria. Só que também abrem feridas para beber sangue, e não se demonstrou que reduzam os parasitas do hospedeiro.",
        "explicacao": (
            "São os pica-bois, ou búfagos, duas espécies africanas do gênero Buphagus, nome que significa "
            "\"comedor de boi\". Vivem nas savanas ao sul do Saara e se alimentam só no corpo de grandes "
            "mamíferos, de zebras e impalas a hipopótamos, rinocerontes e gado. Comem carrapatos, insetos, larvas "
            "de moscas e outros parasitas, e por isso viraram exemplo de mutualismo: a ave se alimenta e o "
            "mamífero fica livre dos parasitas. Em suaíli, o pica-boi-de-bico-vermelho é chamado de \"guarda do "
            "rinoceronte\". Pesquisas mais recentes complicaram a história. Muitas vezes, os carrapatos que eles "
            "comem já se alimentaram do hospedeiro, e não se demonstrou relação estatisticamente significativa "
            "entre a presença das aves e uma carga menor de parasitas. Eles já foram vistos abrindo feridas novas "
            "e alargando as antigas para beber o sangue dos animais em que pousam, e também comem cera de ouvido "
            "e caspa. Alguns hospedeiros não os toleram: elefantes e certos antílopes os enxotam quando pousam. "
            "Hoje, a relação é tema de debate, e há quem classifique os pica-bois como parasitas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Oxpecker",
            "The oxpeckers are two species of bird which make up the genus Buphagus, from Ancient Greek βοῦς (boûs), meaning \"ox\", and φάγος (phágos), meaning \"eater\" [...] "
            "Oxpeckers are endemic to the savanna of Sub-Saharan Africa. "
            "Both the English and scientific names arise from their habit of perching on large mammals (both wild and domesticated) such as cattle, zebras, impalas, hippopotamuses, rhinoceroses, and giraffes, eating ticks, small insects, botfly larvae, and other parasites, as well as the animals' blood. "
            "The behaviour of oxpeckers towards large mammals was thought to be exclusively mutual, though recent research suggests the relationship can be parasitic in nature as well. "
            "The Swahili name for the red-billed oxpecker is Askari wa kifaru (the rhino's guard). [...] "
            "Oxpeckers graze exclusively on the bodies of large mammals. [...] "
            "They are sometimes classified as parasites, because they open wounds on the animals' backs. "
            "Oxpecker/mammal interactions are the subject of some debate and ongoing research. "
            "They were originally thought to be an example of mutualism, but recent evidence suggests that oxpeckers may be parasites instead. "
            "Oxpeckers do eat ticks, but often the ticks have already fed on the ungulate host, and no statistically significant link has been shown between oxpecker presence and reduced ectoparasite load. "
            "Oxpeckers have been observed to open new wounds and enhance existing ones in order to drink the blood of their perches. "
            "Oxpeckers also feed on the earwax and dandruff of mammals [...] "
            "Some oxpeckers' hosts are intolerant of their presence. "
            "Elephants and some antelope will actively dislodge the oxpeckers when they land.",
            nome="Oxpecker")],
    },
    # 13 o cuco que protege o ninho que parasita
    {
        "temas_secundarios": ["comportamento_animal", "evolucao"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "O filhote de um cuco criado por gralhas solta, quando ameaçado, uma secreção fedida que espanta predadores. Num estudo de 16 anos na Espanha, ninhos com o \"intruso\" se saíram melhor. Outro estudo não viu efeito.",
        "explicacao": (
            "O cuco-rabilongo é um parasita de ninhada: põe ovos nos ninhos de corvídeos, como pegas e gralhas, "
            "que criam seus filhotes. Ao contrário do cuco-comum, nem a fêmea nem o filhote jogam fora os ovos do "
            "hospedeiro, mas o filhote do cuco disputa a comida e muitas vezes mata parte dos irmãos adotivos. "
            "Daniela Canestrari e colegas acompanharam 741 ninhos de gralha-preta durante 16 anos em La Sobarriba, "
            "na província de León, e publicaram em 2014, na Science, um resultado inesperado. Quando ameaçado, o "
            "filhote de cuco solta uma secreção de cheiro muito forte, com compostos ácidos e tóxicos, que afasta "
            "aves de rapina e mamíferos. Nos anos com muitos predadores, os ninhos parasitados perderam menos "
            "filhotes, e a relação deixou de ser parasitismo para virar mutualismo, com ganho para os dois lados. "
            "Nos anos de pouca predação, o cuco só cobra seu preço. A ideia não é consenso. Em 2017, um grupo "
            "liderado por Soler não encontrou efeito protetor dos filhotes de cuco em ninhos de pegas e de gralhas "
            "no sul da Espanha. A equipe original respondeu que a secreção repele uns predadores muito mais que "
            "outros, e que a gralha-preta, a principal predadora de ninhos de pega, é a menos sensível a ela."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": "https://cordis.europa.eu/article/id/137674-researchers-discover-that-a-brood-parasite-protects-the-nests-of-another-species-against-pred",
             "titulo": "Researchers discover that a brood parasite protects the nests of another species against predators (CORDIS, Comissão Europeia)",
             "idioma": "en",
             "trecho": "For 16 years, the researchers have been studying and monitoring 741 nests of Carrion Crow (Corvus Corone Corone) and have analyzed their relation with the Great Spotted Cuckoo (Clamator Glandarius), a species of brood parasite of the family of the cuckoo. "
                       "Their work has been led by Daniela Canestrari [...] "
                       "The field experiments demonstrated that the Cuckoo fledglings protect the nest thanks to a secretion that has a very poignant stench that they produce when they are threatened and that scares predators away- [...] "
                       "by keeping birds of prey and mammals away. "
                       "Chemical analyses have proven that the secretion made by the Cuckoo fledlings contains numerous acid and toxic compounds that manage to repel predators. [...] "
                       "The Cuckoo does not expel the fledglings of its host from the nest, but it competes with them for the food that the parents bring to the nest and, frequently, it may kill some of the other fledglings. [...] "
                       "after analyzing the data gathered during 16 years in 741 nests placed in the surroundings of La Sobarriba in León, the researchers proved that in years with a high density of predators, the nests with parasites suffered the lowest number of losses caused by predation. "
                       "In these years, the ecological relation between the Cuckoo and the Carrion Crow stops being parasitic (in which the parasite \"wins\" and the host \"loses\") and it changes into mutualism (they both obtain something positive from the relation)."},
            wiki("Great_spotted_cuckoo",
                "It is a brood parasite that lays its eggs in the nests of corvids, in particular the Eurasian magpie. [...] "
                "Unlike the common cuckoo, neither the hen nor the hatched chick of this species evict the host's eggs, but the young magpies often die because they cannot compete successfully with the cuckoo for food. [...] "
                "Crow chicks benefit only when predators are very active; when there is less predation, losing food to great spotted cuckoo chicks harms the crow chicks without compensation.",
                nome="Great spotted cuckoo"),
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5602529/fullTextXML",
             "titulo": "Formal comment to Soler et al.: Great spotted cuckoo nestlings have no antipredatory effect on magpie or carrion crow host nests in southern Spain (PLOS ONE, 2017)",
             "idioma": "en",
             "trecho": "Soler M, de Neve L, Roldán M, Pérez-Contreras T, Soler JJ. Great spotted cuckoo nestlings have no antipredatory effect on magpie or carrion crow host nests in southern Spain. [...] "
                       "However, previous experiments showed that repellence of great spotted cuckoo secretion varied markedly depending on the species of nest predator, with the carrion crow being the least sensitive [...] "
                       "The carrion crow is the main predator of magpie nes"},
        ],
    },
    # 14 parasitas pesam mais que os predadores
    {
        "temas_secundarios": ["vida_marinha"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Em três estuários da Califórnia e do México, os parasitas somados pesavam mais que os predadores do topo da cadeia. E as larvas que vermes trematódeos soltam num ano superavam a massa de todas as aves.",
        "explicacao": (
            "Parasitas costumam ser vistos como seres minúsculos que quase não contam na balança de um "
            "ecossistema. Uma equipe da Universidade da Califórnia em Santa Bárbara, do Serviço Geológico dos EUA "
            "e de Princeton resolveu pesá-los. Num estudo de cinco anos, levantou a biomassa de espécies de vida "
            "livre e de parasitas em três estuários: o pântano salgado de Carpinteria, na Califórnia, e Bahía San "
            "Quintín e Estero de Punta Banda, na Baja California. Entraram na conta 199 espécies de animais de "
            "vida livre, 15 de plantas e 138 de parasitas. O resultado, publicado na Nature em 2008, foi que a "
            "biomassa de parasitas superava a dos predadores de topo, em alguns casos por um fator de 20. Os "
            "trematódeos, um grupo de vermes parasitas, se destacaram: sua biomassa era comparável à de grupos "
            "abundantes ali, como aves, peixes, camarões escavadores e poliquetas. E a produção anual das larvas "
            "nadadoras que eles soltam para infectar o próximo hospedeiro era maior que a biomassa somada de todos "
            "os parasitas e também maior que a das aves. \"Se desse para ver os trematódeos com binóculos, talvez "
            "você nem se desse ao trabalho de observar aves\", disse o ecólogo Kevin Lafferty, um dos autores."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": "https://pubs.usgs.gov/publication/70177121",
             "titulo": "Ecosystem energetic implications of parasite and free-living biomass in three estuaries (Nature, 2008), resumo no USGS Publications Warehouse",
             "idioma": "en",
             "trecho": "Parasites can have strong impacts but are thought to contribute little biomass to ecosystems. "
                       "We quantified the biomass of free-living and parasitic species in three estuaries on the Pacific coast of California and Baja California. "
                       "Here we show that parasites have substantial biomass in these ecosystems. "
                       "We found that parasite biomass exceeded that of top predators. "
                       "The biomass of trematodes was particularly high, being comparable to that of the abundant birds, fishes, burrowing shrimps and polychaetes. [...] "
                       "The annual production of free-swimming trematode transmission stages was greater than the combined biomass of all quantified parasites and was also greater than bird biomass."},
            {"url": "https://news.ucsb.edu/print/pdf/node/12450",
             "titulo": "Study Shows Parasites Outweigh Predators (UC Santa Barbara, 2008)",
             "idioma": "en",
             "trecho": "July 15, 2008 [...] "
                       "a team of researchers from the University of California, Santa Barbara, the United States Geological Survey, and Princeton University has determined that parasite biomass in those habitats exceeds that of top predators, in some cases by a factor of 20. [...] "
                       "The article grew out of a five-year study [...] "
                       "The researchers quantified parasites and free-living organisms in the Carpinteria Salt Marsh and in the Bahia San Quintín and Estero de Punta Banda estuaries in Baja California. "
                       "Their study included 199 species of free-living animals, 15 species of free-living vascular plants, and 138 species of parasites. [...] "
                       "Kevin Lafferty, a marine ecologist with the United States Geological Survey [...] "
                       "\"If you could see the trematodes with binoculars, you might not bother bird watching.\""},
        ],
    },
    # 15 a craca que transforma caranguejos em babás
    {
        "temas_secundarios": ["vida_marinha", "evolucao"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Uma craca parasita castra o caranguejo e o faz cuidar das larvas dela como se fossem seus ovos. Se o caranguejo é macho, o corpo dele ganha formato de fêmea, e ele chega a fazer as danças de acasalamento das fêmeas.",
        "explicacao": (
            "A Sacculina é uma craca, mas o adulto não lembra em nada as que cobrem cascos de navios: só as larvas "
            "denunciam o parentesco. A larva fêmea anda sobre um caranguejo até achar uma articulação e então "
            "injeta o próprio corpo mole dentro dele, deixando a casca para trás. Lá dentro, espalha raízes que se "
            "enrolam nos órgãos, sobretudo na região que absorve nutrientes. Depois, uma bolsa reprodutiva do "
            "parasita brota sob o abdômen do caranguejo, justamente onde ele incubaria os próprios ovos. O "
            "caranguejo fica estéril para sempre, deixa de trocar de carapaça e perde a capacidade de regenerar "
            "uma garra perdida; a energia que iria para a reprodução fica para o parasita. Em machos, a Sacculina "
            "mexe no equilíbrio hormonal: o abdômen alarga e achata como o de uma fêmea, e o caranguejo passa a "
            "agir como fêmea. Quando as larvas do parasita estão prontas, ele repete o ritual de uma mãe: sobe numa "
            "pedra alta, solta as larvas em pulsos, formando uma nuvem, e agita a água com a garra. Em algumas "
            "populações, até metade dos caranguejos está infectada."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Sacculina",
            "Sacculina is a genus of barnacles that is a parasitic castrator of crabs. [...] "
            "The adults bear no resemblance to the barnacles that cover ships, whales, and piers; they are recognised as barnacles because their larval forms are like other members of the barnacle class Cirripedia. "
            "The prevalence of this crustacean parasite in its crab host can be as high as 50%. [...] "
            "This part is composed of root-like tendrils that wrap themselves around the host's organs [...] "
            "these roots have been discovered to wrap around certain organs of the body, with most around the hepatopancreas of crustaceans. "
            "This area is primarily for absorbing nutrients [...] "
            "The female Sacculina larva finds a crab and walks on it until she finds a joint. "
            "She then molts into a form called a kentrogon, which then injects her soft body into the crab while her shell falls off. "
            "The Sacculina grows in the crab, emerging as a sac, known as an externa, on the underside of the crab's rear thorax, where the crab's eggs would be incubated. "
            "Parasitic Sacculina destroy a crab's genitalia, rendering the crab permanently infertile. "
            "After this invasion of the Sacculina, the crab is unable to perform the normal function of molting. [...] "
            "The natural ability of regrowing a severed claw that is commonly used for defense purposes is therefore lost after the infestation of Sacculina. [...] "
            "When a female Sacculina is implanted in a male crab, it interferes with the crab's hormonal balance. "
            "This sterilizes it and changes the bodily layout of the crab to resemble that of a female crab by widening and flattening its abdomen, among other things. "
            "The female Sacculina then forces the crab's body to release hormones, causing it to act like a female crab, even to the point of performing female mating dances. [...] "
            "Although all energy otherwise expended on reproduction is directed to the Sacculina, the crab develops a nurturing behavior typical of a normal female crab. "
            "The natural hatching process of a crab consists of the female finding a high rock and grooming its brood pouch on its abdomen and releasing the fertilized eggs in the water through a bobbing motion. "
            "The female crab stirs the water with her claw to aid the flow of the water. "
            "When the hatching larvae of Sacculina are ready to emerge from the brood pouch of female Sacculina, the crab performs a similar process. "
            "The crab shoots them out in pulses, creating a large cloud of Sacculina larvae. "
            "The crab uses the familiar technique of stirring the water to aid in flow.",
            nome="Sacculina")],
    },
    # 16 Guam: sem aves, ilha das aranhas
    {
        "temas_secundarios": ["comportamento_animal", "evolucao"],
        "tipos_espanto": ["conexao_inesperada", "escala_absurda"],
        "gancho": "Em Guam, uma cobra invasora acabou com as aves da floresta. Sem quem as comesse, as aranhas se multiplicaram: na estação chuvosa, havia 40 vezes mais teias que em ilhas vizinhas com aves.",
        "explicacao": (
            "A cobra-arbórea-marrom chegou a Guam, no Pacífico, por acidente, depois da Segunda Guerra Mundial. Na "
            "ilha, achou presas em abundância e quase nenhum predador, e sua população atingiu números sem "
            "precedentes. As aves nativas foram as mais atingidas: doze espécies desapareceram, e hoje as aves "
            "florestais de Guam estão funcionalmente extintas. Isso criou um experimento natural. Haldre Rogers e "
            "colegas contaram teias de aranha em trilhas de floresta nativa de Guam e de três ilhas próximas, Rota, "
            "Tinian e Saipan, que não têm a cobra e mantêm populações de aves relativamente saudáveis. Na estação "
            "chuvosa, a densidade de teias em Guam era 40 vezes maior; na seca, 2,3 vezes. Sem aves, a variação "
            "das teias ao longo do ano parece ter sumido, e ao menos uma espécie de aranha passou a tecer teias "
            "maiores em Guam. Segundo os autores, o efeito foi muito maior que o visto na maioria dos experimentos "
            "de manipulação feitos em outros lugares. E a cadeia de consequências não para nas aranhas: ao reduzir "
            "aves nativas e morcegos-das-frutas, importantes polinizadores, a cobra também afetou indiretamente a "
            "diversidade de plantas da ilha."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0043446",
             "titulo": "'Natural experiment' Demonstrates Top-Down Control of Spiders by Birds on a Landscape Level (PLOS ONE, 2012)",
             "idioma": "en",
             "trecho": "Haldre Rogers, Janneke Hille Ris Lambers, Ross Miller, Joshua J. Tewksbury [...] "
                       "We conducted spider web surveys in native forest on Guam and three nearby islands with healthy bird populations. "
                       "Spider web densities on the island of Guam were 40 times greater than densities on islands with birds during the wet season, and 2.3 times greater during the dry season. "
                       "These results confirm the general trend from manipulative experiments conducted in other systems however, the effect size was much greater in this natural experiment than in most manipulative experiments. "
                       "In addition, bird loss appears to have removed the seasonality of spider webs and led to larger webs in at least one spider species in the forests of Guam than on nearby islands with birds. [...] "
                       "All forest birds are functionally extinct on the island of Guam, whereas relatively healthy bird populations remain on three nearby islands of Saipan, Tinian and Rota. [...] "
                       "that have no known snake populations"},
            wiki("Brown_tree_snake",
                "Due to an accidental introduction after the events of World War II, this snake is now infamous for being an invasive species responsible for extirpating the majority of the native bird population in Guam. [...] "
                "As a result of abundant prey resources on Guam and the absence of natural predators apart from the native Mariana monitor and feral pigs, brown tree snake populations reached unprecedented numbers. [...] "
                "The primary population affected by the snake's introduction was native bird species. "
                "The introduction of the brown tree snake into Guam has resulted in extinction of twelve native bird species in total [...] "
                "the introduction of the brown tree snake has had an indirect negative impact on plant diversity, as its intense predatory nature has decreased populations of vital pollinators, including native birds and fruit bats.",
                nome="Brown tree snake"),
        ],
    },
]
