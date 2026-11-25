LOTE = "2026-11-24-desenvolvimento_humano-01"
AREA = "corpo_medicina"
TEMA = "desenvolvimento_humano"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 bebês crescem aos saltos
    {
        "temas_secundarios": ["anatomia", "sono_ritmos"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Bebês não crescem aos pouquinhos. Medidos com frequência, eles passam de 2 a 63 dias sem nenhum crescimento mensurável e então dão um salto, às vezes de até um centímetro num único dia.",
        "explicacao": (
            "Por muito tempo, o crescimento humano foi tratado como um processo contínuo, só com a velocidade "
            "mudando ao longo da idade. A antropóloga Michelle Lampl resolveu medir o comprimento de bebês com "
            "uma frequência incomum: uns uma vez por semana, outros duas, e três deles todos os dias, durante os "
            "primeiros 21 meses de vida. O resultado, publicado na revista Science em 1992, mostrou outro padrão: "
            "o comprimento aumentava em surtos irregulares, de 0,5 a 2,5 cm, separados por intervalos de 2 a 63 "
            "dias em que nada mudava. Pelas contas do estudo, de 90% a 95% do desenvolvimento na primeira infância "
            "se passa sem crescimento algum. Lampl chamou o modelo de saltação e estase: os ossos se alongam de "
            "repente, e o bebê pode ganhar até um centímetro num dia, depois de dias ou semanas parado. Em crianças "
            "e adolescentes, as pausas duram de semanas a meses. Num trabalho de 2011, ela e um colega associaram "
            "o crescimento em comprimento dos bebês a períodos de sono prolongado e a mais cochilos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/1439787?resultType=core&format=json",
             "titulo": "Saltation and stasis: a model of human growth (Lampl, Veldhuis e Johnson, Science, 1992), resumo na Europe PMC",
             "idioma": "en",
             "trecho": "Human growth has been viewed as a continuous process characterized by changing velocity with age. "
                       "Serial length measurements of normal infants were assessed weekly (n = 10), semiweekly (n = 18), and daily (n = 3) (19 females and 12 males) during their first 21 months. "
                       "Data show that growth in length occurs by discontinuous, aperiodic saltatory spurts. "
                       "These bursts were 0.5 to 2.5 centimeters in amplitude during intervals separated by no measurable growth (2 to 63 days duration). "
                       "These data suggest that 90 to 95 percent of normal development during infancy is growth-free"},
            wiki("Michelle_Lampl",
                "Lampl discovered that children grow by saltation and stasis, a process characterized by sudden jumps (saltare, Lat) in size abruptly interrupting days of unchanging size. [...] "
                "Increasing size was found to occur as bones suddenly elongate and propel a baby’s length and child’s height by as much as a centimeter in one day, after not growing for days to weeks in infancy, and weeks to months among children and adolescents. [...] "
                "Lampl, M., Veldhuis, J., & Johnson, M. (1992). Saltation and stasis: a model of human growth. Science, 258(5083), 801–803. [...] "
                "Lampl M., Johnson, M.L. (2011). Infant growth in length follows prolonged sleep and increased naps.",
                nome="Michelle Lampl"),
        ],
    },
    # 2 o cérebro faminto da criança de 4 ou 5 anos
    {
        "temas_secundarios": ["evolucao", "neurociencia"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "Aos 5 anos, o cérebro de uma criança usa o dobro da glicose do cérebro de um adulto. Um estudo sugere que é por isso que, nessa fase, o corpo cresce tão devagar: a energia vai para a cabeça.",
        "explicacao": (
            "A pesquisa, liderada pelo antropólogo Christopher Kuzawa, da Universidade Northwestern, e publicada "
            "em 2014, juntou dados já existentes de dois tipos de exame: PET, que mede o consumo de glicose do "
            "cérebro, e ressonância magnética, que mede o volume. Antes, imaginava-se que o peso do cérebro no "
            "orçamento do corpo fosse máximo no nascimento, quando ele é maior em relação ao resto do corpo. Os "
            "dados mostraram que o consumo de glicose atinge o pico aos 5 anos. Aos 4, o cérebro gasta o "
            "equivalente a 66% do que o corpo inteiro usa em repouso, mais de 40% do gasto total de energia. É "
            "também a idade em que o crescimento do corpo chega ao mínimo. Segundo os autores, as crianças "
            "humanas crescem num ritmo mais típico de um réptil que de um mamífero, e isso liberaria combustível "
            "para um cérebro que, nessa fase, tem o maior número de sinapses. Kuzawa nota um efeito que os pais "
            "conhecem: a partir de certa idade fica difícil adivinhar a idade de uma criança pelo tamanho, e é "
            "preciso ouvi-la falar. A ligação entre as duas curvas é uma interpretação dos autores, não uma prova "
            "de causa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": "https://news.northwestern.edu/stories/2014/08/a-long-childhood-feeds-the-hungry-human-brain",
             "titulo": "A Long Childhood Feeds the Hungry Human Brain (Northwestern University, 2014)",
             "idioma": "en",
             "trecho": "August 25, 2014 [...] "
                       "A five-year old’s brain is an energy monster. It uses twice as much glucose (the energy that fuels the brain) as that of a full-grown adult, a new study led by Northwestern University anthropologists has found. [...] "
                       "It shows that energy funneled to the brain dominates the human body’s metabolism early in life and is likely the reason why humans grow at a pace more typical of a reptile than a mammal during childhood. [...] "
                       "The study is the first to pool existing PET and MRI brain scan data -- which measure glucose uptake and brain volume, respectively -- to show that the ages when the brain gobbles the most resources are also the ages when body growth is slowest. [...] "
                       "“After a certain age it becomes difficult to guess a toddler or young child’s age by their size,” Kuzawa said. “Instead you have to listen to their speech and watch their behavior. [...] "
                       "It was previously believed that the brain’s resource burden on the body was largest at birth, when the size of the brain relative to the body is greatest. The researchers found instead that the brain maxes out its glucose use at age 5. "
                       "At age 4 the brain consumes glucose at a rate comparable to 66 percent of the body’s resting metabolic rate (or more than 40 percent of the body’s total energy expenditure). "
                       "“The mid-childhood peak in brain costs has to do with the fact that synapses, connections in the brain, max out at this age"},
        ],
    },
    # 3 o cérebro não fica pronto aos 25
    {
        "temas_secundarios": ["neurociencia", "aprendizagem_inteligencia"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "A ideia de que o cérebro fica pronto aos 25 anos não vem de nenhum estudo específico. Um trabalho de 2025, com exames de 3.802 pessoas, achou que a fiação cerebral segue em fase adolescente até cerca de 32.",
        "explicacao": (
            "A frase \"o córtex pré-frontal só amadurece aos 25\" circula em redes sociais, aulas e consultórios. "
            "É verdade que exames de ressonância mostram essa região, ligada a planejamento e controle de "
            "impulsos, ainda se desenvolvendo depois dos 20 anos. Mas, como lembra o Escritório de Ciência e "
            "Sociedade da Universidade McGill, o 25 resume tendências gerais, sem um estudo definitivo por trás, e "
            "até o psicólogo Larry Steinberg, muito citado no tema, o trata como uma estimativa, não um prazo. "
            "Mesmo assim, o número já foi parar em diretrizes de sentença na Escócia, que tratam os menores de 25 "
            "como um grupo à parte. Em 2025, uma equipe da Universidade de Cambridge analisou exames de difusão, "
            "que mapeiam as conexões do cérebro, de pessoas de zero a noventa anos. Achou quatro grandes pontos de "
            "virada, por volta dos nove, 32, 66 e 83 anos. A fase \"adolescente\", em que a eficiência das conexões "
            "aumenta, vai dos nove anos até o início dos trinta, e a virada dos 32 foi a mais forte de todas. Depois vem a fase adulta, "
            "estável por cerca de três décadas. São médias de um único estudo: nenhum cérebro vira uma chave numa "
            "data marcada."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": "https://www.mcgill.ca/oss/article/critical-thinking-student-contributors/25-really-magic-number",
             "titulo": "Is 25 Really the Magic Number? (McGill University, Office for Science and Society)",
             "idioma": "en",
             "trecho": "Let’s get one thing straight—the frontal lobe, specifically the prefrontal cortex, is indeed the brain’s command center for impulse control, planning, and decision-making. And yes, it’s one of the last regions to mature. MRI studies do show that this area keeps developing into our 20s. [...] "
                       "You’ve probably heard it before—maybe on TikTok, in a health class, or from your therapist: “The frontal lobe isn’t fully developed until 25.” [...] "
                       "The “age 25” marker comes from general trends in brain development, not a single definitive study. Even psychologist Larry Steinberg, often cited in these discussions, frames 25 as more of a ballpark than a deadline. [...] "
                       "In Scotland, sentencing guidelines now treat people under 25 as developmentally distinct"},
            {"url": "https://www.cam.ac.uk/stories/five-ages-human-brain",
             "titulo": "Scientists identify five ages of the human brain over a lifetime (University of Cambridge, 2025)",
             "idioma": "en",
             "trecho": "Published: 25 November 2025 [...] "
                       "Four major turning points around ages nine, 32, 66 and 83 create five broad eras of neural wiring over the average human lifespan. [...] "
                       "compared the brains of 3,802 people between zero and ninety years old using datasets of MRI diffusion scans, which map neural connections by tracking how water molecules move through brain tissue. [...] "
                       "Childhood brain “topology” runs from birth until a turning point at the age of nine, when it transitions to the adolescent phase – an era that lasts right up to the age of 32, on average. [...] "
                       "the adolescent era is the only one in which this efficiency is increasing,” said Mousley. "
                       "These developments peak in the early thirties, on average, which is the “strongest topological turning point” of the entire lifespan say researchers. [...] "
                       "At age 32, the longest era, that of adulthood, begins. Brain architecture stabilises compared to previous phases – with no major turning points for thirty years."},
        ],
    },
    # 4 a poda das sinapses e o gene C4
    {
        "temas_secundarios": ["sistema_imunologico", "genetica", "neurociencia"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Uma peça do sistema imune ajuda a podar as conexões do cérebro jovem. Variantes do gene dela, o C4, que aumentam sua produção no cérebro, elevam o risco de esquizofrenia, que costuma surgir no fim da adolescência.",
        "explicacao": (
            "O cérebro de um bebê produz sinapses, as conexões entre neurônios, em excesso, e ao longo da "
            "infância elas vão sendo eliminadas: sobrevivem as mais usadas. Na adolescência e no começo da vida "
            "adulta, há outra rodada intensa de eliminação em regiões como o córtex pré-frontal, que parece se "
            "estender até a terceira década de vida. Quem ajuda a marcar sinapses para remoção é o sistema "
            "complemento, um conjunto de proteínas da imunidade inata que normalmente reconhece micróbios e restos "
            "de células. Em camundongos, a proteína C3 marca sinapses, e a micróglia, a célula de defesa do "
            "cérebro, as engole. Um grande estudo genético mostrou que a associação genética mais forte "
            "da esquizofrenia, numa região do genoma ligada à imunidade, vem em boa parte de variantes do gene C4: "
            "quanto mais uma variante aumenta a produção de C4A no cérebro, maior o risco. Nos camundongos, o C4 "
            "participou da eliminação de sinapses depois do nascimento. Os autores sugerem que uma poda excessiva "
            "pode ajudar a explicar por que pessoas com esquizofrenia têm menos sinapses, e por que a doença "
            "costuma aparecer justamente no fim da adolescência ou no início da vida adulta. A ideia ainda é "
            "investigada."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4752392/fullTextXML",
             "titulo": "Schizophrenia risk from complex variation of complement component 4 (Sekar et al., Nature, 2016)",
             "idioma": "en",
             "trecho": "Schizophrenia’s strongest genetic association at a population level involves variation in the Major Histocompatibility Complex (MHC) locus [...] "
                       "We show here that schizophrenia’s association with the MHC locus arises in substantial part from many structurally diverse alleles of the complement component 4 [...] "
                       "We found that these alleles promoted widely varying levels of [...] expression and associated with schizophrenia in proportion to their tendency to promote greater expression of [...] "
                       "In mice, C4 mediated synapse elimination during postnatal development. These results implicate excessive complement activity in the development of schizophrenia and may help explain the reduced numbers of synapses in the brains of individuals affected with schizophrenia. [...] "
                       "usually manifest late in adolescence or early in adulthood. [...] "
                       "C4 is a critical component of the classical complement cascade, an innate-immune-system pathway that rapidly recognizes and eliminates pathogens and cellular debris. [...] "
                       "In humans, adolescence and early adulthood bring extensive elimination of synapses in distributed association regions of cerebral cortex, such as the prefrontal cortex [...] "
                       "Synapse elimination in human association cortex appears to continue from adolescence into the third decade of life [...] "
                       "In the developing mouse brain, C3 targets subsets of synapses and is required for synapse elimination by microglia, the principal CNS cells expressing receptors for complement"},
            {"url": "https://www.cam.ac.uk/stories/five-ages-human-brain",
             "titulo": "Scientists identify five ages of the human brain over a lifetime (University of Cambridge, 2025)",
             "idioma": "en",
             "trecho": "From infancy through childhood, our brains are defined by “network consolidation”, as the wealth of synapses – the connectors between neurons – overproduced in a baby’s brain are whittled down, with the more active ones surviving."},
        ],
    },
    # 5 Carrel, o coração de galinha "imortal" e o limite de Hayflick
    {
        "temas_secundarios": ["historia_medicina", "genetica"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Um Nobel manteve células de coração de embrião de galinha se multiplicando por mais de 20 anos, e a ciência passou a crer que células eram imortais. Em 1961, Hayflick mostrou que não: as normais param de se dividir.",
        "explicacao": (
            "Em 1912, no Instituto Rockefeller, o cirurgião Alexis Carrel, premiado com o Nobel naquele ano por "
            "outro trabalho, começou a cultivar tecido de coração de embrião de galinha num frasco de vidro de "
            "seu próprio projeto. Alimentou a cultura por mais de 20 anos, mais do que vive uma galinha, e o caso "
            "virou prova de que as células se multiplicariam sem fim. Ninguém conseguiu repetir o resultado. No "
            "Instituto Wistar, Leonard Hayflick notou que suas culturas de células fetais humanas sempre "
            "degringolavam por volta da 40ª duplicação. Para descartar contaminação, ele e Paul Moorhead "
            "misturaram células masculinas \"velhas\" com femininas \"jovens\": depois de 20 duplicações, só "
            "restavam as femininas, o que indicava um contador interno nas próprias células. Hoje se sabe que "
            "células humanas normais se dividem de 40 a 60 vezes em cultura, e que o limite tem relação com os "
            "telômeros, as pontas dos cromossomos, que encurtam a cada divisão. As células de câncer escapam "
            "graças à enzima telomerase, que repõe os telômeros. E Carrel? Hayflick sugeriu que a alimentação "
            "diária da cultura levava junto células novas, vivas."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Hayflick_limit",
                "The concept of the Hayflick limit was advanced by American anatomist Leonard Hayflick in 1961, at the Wistar Institute in Philadelphia, Pennsylvania. "
                "Hayflick demonstrated that a normal human fetal cell population will divide between 40 and 60 times in cell culture before entering a senescence phase. "
                "This finding refuted the contention by Alexis Carrel that normal cells are immortal. [...] "
                "Prior to Leonard Hayflick's discovery, it was believed that vertebrate cells had an unlimited potential to replicate. [...] "
                "However, other scientists have been unable to replicate Carrel's results [...] "
                "Hayflick checked his research notebook and was surprised to find that the atypical cell cultures had all been cultured to approximately their 40th doubling while younger cultures never exhibited the same problems. [...] "
                "Hayflick mixed equal numbers of normal human male fibroblasts that had divided many times (cells at the 40th population doubling) with female fibroblasts that had divided fewer times (cells at the 15th population doubling). "
                "Unmixed cell populations were kept as controls. After 20 doublings of the mixed culture, only female cells remained. [...] "
                "the cessation of normal cell replication was governed by an internal counting mechanism. [...] "
                "The Hayflick limit has been found to correlate with the length of the telomeric region at the end of chromosomes. [...] "
                "Cellular senescence does not occur in most cancer cells due to expression of an enzyme called telomerase. This enzyme extends telomeres",
                nome="Hayflick limit"),
            wiki("Alexis_Carrel",
                "He was awarded the Nobel Prize in Physiology or Medicine in 1912 for pioneering vascular suturing techniques. [...] "
                "He believed that all cells continued to grow indefinitely, which became a widely accepted view in the early 20th century. "
                "In 1912, Carrel began an experiment at the Rockefeller Institute for Medical Research, where he cultured tissue from an embryonic chicken heart in a stoppered Pyrex flask of his own design. "
                "He supplied the culture with nutrients regularly and maintained it for over 20 years, longer than a chicken's normal lifespan. "
                "This experiment received significant popular and scientific attention, but it was never successfully replicated. [...] "
                "Hayflick suggested that Carrel's daily feeding of nutrients continually introduced new living cells to the culture",
                nome="Alexis Carrel"),
        ],
    },
    # 6 menopausa: avós humanas e avós orcas
    {
        "temas_secundarios": ["vida_marinha", "evolucao", "comportamento_animal"],
        "tipos_espanto": ["conexao_inesperada", "misterio_aberto"],
        "gancho": "Além dos humanos, algumas baleias dentadas, como a orca, vivem décadas depois de parar de se reproduzir. Entre as orcas, avós que já não têm filhotes aumentam a chance de sobrevivência dos netos.",
        "explicacao": (
            "Viver muito além da fase fértil é raro na natureza: o grupo de espécies conhecidas inclui belugas, "
            "narvais, orcas, falsas-orcas e baleias-piloto-de-aleta-curta, e estudos recentes acharam menopausa "
            "também em chimpanzés e gorilas selvagens de Uganda. Para os humanos, a explicação mais discutida é a "
            "\"hipótese da avó\": em vez de seguir tendo filhos, a mulher mais velha ajudaria filhos e netos, que "
            "carregam parte dos genes dela. Em 1957, o biólogo George Williams já sugeria que a menopausa poderia "
            "ser uma adaptação. Entre os hadza, caçadores-coletores da Tanzânia, avós buscam alimentos que as "
            "crianças ainda não conseguem obter sozinhas. As orcas residentes oferecem um teste: os filhotes "
            "não se afastam da mãe, e as avós convivem com filhos e netos. Um estudo com essas orcas mostrou que as avós aumentam a sobrevivência dos netos, sobretudo quando já não se "
            "reproduzem e nos anos de pouco salmão. Uma análise comparativa concluiu que, nas baleias dentadas, a "
            "menopausa surgiu porque as fêmeas passaram a viver mais sem esticar a fase reprodutiva, o mesmo "
            "caminho proposto para os humanos. A hipótese, porém, segue em debate."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Menopause",
                "Humans are joined by a limited number of other species in which females live substantially longer than their ability to reproduce. "
                "Examples of others include cetaceans: beluga whales, narwhals, orcas, false killer whales and short-finned pilot whales. "
                "Research published in 2023 and 2025 showed that wild Ugandan chimpanzees and gorillas, respectively, undergo menopause.",
                nome="Menopause"),
            wiki("Grandmother_hypothesis",
                "It suggests that by redirecting their energy onto those of their offspring, grandmothers can better ensure the survival of their genes through younger generations. [...] "
                "One explanation to this was presented by G.C. Williams who was the first to posit, in 1957, that menopause might be an adaptation. [...] "
                "the post-menopausal Hadza women often help their grandchildren by foraging for food staples that younger children are inefficient at acquiring successfully.",
                nome="Grandmother hypothesis"),
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6936675/fullTextXML",
             "titulo": "Postreproductive killer whale grandmothers improve the survival of their grandoffspring (Nattrass et al., PNAS, 2019)",
             "idioma": "en",
             "trecho": "We show that grandmothers increase the survival of their grandoffspring, and these effects are greatest when grandmothers are no longer reproducing. "
                       "These findings can help explain why killer whales have evolved the longest postreproductive life span of all nonhuman animals. [...] "
                       "The benefits postreproductive grandmothers provide to their grandoffspring are shown to be most important in difficult times where the salmon abundance is low to moderate. [...] "
                       "offspring do not disperse away from their mother [...] "
                       "This results in a close-knit family-based society, where grandmothers regularly group with both their offspring and their maternal grandoffspring."},
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10954554/fullTextXML",
             "titulo": "The evolution of menopause in toothed whales (Ellis et al., Nature, 2024)",
             "idioma": "en",
             "trecho": "Toothed whales are the only mammal taxon in which menopause has evolved several times [...] "
                       "We find that menopause evolved in toothed whales by females extending their lifespan without increasing their reproductive lifespan [...] "
                       "the same pathway that led to menopause in humans can also explain the evolution of menopause in toothed whales."},
        ],
    },
    # 7 recém-nascidos pendurados numa barra (reflexo de preensão)
    {
        "temas_secundarios": ["evolucao", "historia_medicina", "neurociencia"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1891, um médico darwinista testou 60 bebês com menos de um mês pendurados numa barra: segundo ele, aguentavam o próprio peso por pelo menos 10 segundos, e um ficou 2 min 35 s.",
        "explicacao": (
            "O inglês Louis Robinson era evolucionista convicto, e o artigo em que publicou os resultados, em "
            "1891, se chamava \"Darwinism in the nursery\", darwinismo no berçário. O que ele explorava é o reflexo de preensão palmar: ao tocar a palma da mão do bebê, os dedos se fecham sozinhos. "
            "Um feto já o mostra por volta de 28 semanas de gestação, e o reflexo some entre os dois e os seis meses de vida. "
            "Ele é bem mais frequente em primatas cujos filhotes viajam agarrados ao pelo da mãe, e por isso é "
            "visto como um vestígio nos humanos, embora a função seja debatida. Ele é comandado pela medula "
            "espinhal e aparece até em bebês sem a maior parte do cérebro. O que o faz sumir é o amadurecimento "
            "dos lobos frontais, que passam a suprimi-lo. Daí um detalhe curioso: em adultos com lesões cerebrais "
            "ou certas demências, esses reflexos podem voltar, e os médicos os usam como sinal de que o lobo "
            "frontal está falhando. Hoje, o reflexo faz parte do exame neurológico do recém-nascido."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.lancaster.ac.uk/fas/psych/glossary/grasp_response/",
             "titulo": "Grasp response (Lancaster Glossary of Child Development, Lancaster University)",
             "idioma": "en",
             "trecho": "Both grasp response can be elicited in anencephalic infants [...] "
                       "Such a finding supports the contention that palmar and plantar responses in the newborn are mediate by mechanisms at the spinal level [...] "
                       "Whether these responses and other so-called reflexes continue to have functions in human development is matter of debate, with one view treating them as phylogenetic vestiges. [...] "
                       "It was the avid Darwinist Louis Robinson (1857-????) who first described in 1891 that the human newborn was able to support its own weight when holding on to a horizontal rod. "
                       "Testing 60 infants under one month-of-age, he reported they could maintain the grasp for at least 10 seconds, with one infant doing so for 2 minutes and 35 seconds. "
                       "See Robinson, L. Darwinism in the nursery."},
            wiki("Palmar_grasp_reflex",
                "When an object, such as an adult finger, is placed in an infant's palm, the infant's fingers reflexively grasp the object. [...] "
                "A fetus exhibits the reflex in utero by 28 weeks into gestation (sometimes, as early as 16 weeks), and persists until development of rudimentary fine motor skills between two and six months of age. [...] "
                "Biologists have found that the reflex is significantly more frequent in infants of fur carrying primate species. [...] "
                "This suggests that the grasping reflex is vestigial in humans and in other non-fur carrying primates. [...] "
                "That is why the elicitation of this grasp reflex is part of neurological examinations for newborns.",
                nome="Palmar grasp reflex"),
            wiki("Primitive_reflexes",
                "These reflexes are suppressed by the development of the frontal lobes as a child transitions normally into child development. [...] "
                "Primitive reflexes are primarily tested with suspected brain injury or some dementias such as Parkinson's disease for the purpose of assessing frontal lobe functioning. "
                "If they are not being suppressed properly they are called frontal release signs.",
                nome="Primitive reflexes"),
            wiki("Louis_Robinson",
                "An ardent evolutionist, he helped pioneer modern child medicine during the later Victorian era",
                nome="Louis Robinson"),
        ],
    },
    # 8 holandeses e sul-coreanas: um século de altura
    {
        "temas_secundarios": ["genetica", "economia_curiosa"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Em um século, as sul-coreanas ficaram 20 cm mais altas, em média. E os holandeses, conhecidos no século XIX pela baixa estatura, viraram o povo mais alto do mundo: 182,5 cm entre os homens nascidos em 1996.",
        "explicacao": (
            "Os números vêm de um estudo internacional que reuniu medidas de mais de 18,6 milhões de pessoas para "
            "estimar a altura média dos nascidos entre 1896 e 1996 em 200 países. Os maiores ganhos foram das "
            "mulheres da Coreia do Sul, 20,2 cm, e dos homens do Irã, 16,5 cm. Em parte da África subsaariana e "
            "do sul da Ásia, quase nada mudou. Há um século, as mais baixas eram as guatemaltecas nascidas em "
            "1896, com 140,3 cm, a altura de uma menina bem nutrida de 10 anos. Os holandeses mostram como o "
            "ambiente pesa: entre 1830 e 1857, a altura média deles caiu, mesmo com a economia crescendo, e nas "
            "cidades, onde se morria mais, a queda foi maior. No fim do século XIX, o país era conhecido pela "
            "população baixa. Genes explicam parte das diferenças, mas a maior parte vem de outras causas, como "
            "desnutrição e doenças na infância e na adolescência. Um exemplo: crianças maias refugiadas nos "
            "Estados Unidos ficaram, em 2000, 10 cm mais altas que as da Guatemala. Já os americanos, entre os "
            "mais altos há um século, foram os primeiros a ver a altura parar de subir."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4961475/fullTextXML",
             "titulo": "A century of trends in adult human height (NCD Risk Factor Collaboration, eLife, 2016)",
             "idioma": "en",
             "trecho": "We reanalysed 1472 population-based studies, with measurement of height on more than 18.6 million participants to estimate mean height for people born between 1896 and 1996 in 200 countries. "
                       "The largest gain in adult height over the past century has occurred in South Korean women and Iranian men, who became 20.2 cm (95% credible interval 17.5–22.7) and 16.5 cm (13.3–19.7) taller, respectively. "
                       "In contrast, there was little change in adult height in some sub-Saharan African countries and in South Asia over the century of analysis. "
                       "The tallest people over these 100 years are men born in the Netherlands in the last quarter of 20th century, whose average heights surpassed 182.5 cm, and the shortest were women born in Guatemala in 1896 (140.3 cm; 135.8–144.8). [...] "
                       "This may be partly due to genetics, but most differences in height between countries have other causes. "
                       "For example, children and adolescents who are malnourished, or who suffer from serious diseases, will generally be shorter as adults. [...] "
                       "the same as a well-nourished 10-year girl. [...] "
                       "The earliest of these occurred in the USA, which was one of the tallest nations a century a"},
            wiki("Human_height",
                "From 1830 to 1857, the average height of a Dutch person decreased, even while Dutch real GNP per capita was growing at an average rate of more than 0.5% per year. "
                "The worst decline was in urban areas [...] "
                "Urban mortality was also much higher than in rural regions. [...] "
                "In the late nineteenth century, the Netherlands was a land renowned for its short population [...] "
                "Maya refugees, who ranged from six to twelve years old, were significantly taller than their Guatemalan counterparts. By 2000, the American Maya were 10.24 centimetres (4.0 in) taller than the Guatemalan Maya",
                nome="Human height"),
        ],
    },
    # 9 zonas azuis e registros de idade
    {
        "temas_secundarios": ["limites_humanos", "economia_curiosa"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 2010, Tóquio foi homenagear seu homem mais velho e achou um corpo mumificado: ele tinha morrido três décadas antes. Casos assim alimentam a dúvida sobre as \"zonas azuis\", regiões famosas por seus centenários.",
        "explicacao": (
            "Sogen Kato, nascido em 1899, era tido como o homem mais velho de Tóquio. Quando funcionários foram "
            "visitá-lo para o Dia do Respeito aos Idosos, a família recusou várias vezes. A polícia entrou e achou "
            "o corpo na cama; jornais no quarto sugeriam morte por volta de 1978. Parentes receberam a pensão dele, "
            "e um foi condenado por fraude. A busca que se seguiu mostrou que a polícia não sabia se 234.354 "
            "pessoas com mais de 100 anos estavam vivas. As \"zonas azuis\", como Okinawa, a Sardenha, Icária e "
            "Nicoya, foram vendidas como lugares onde o estilo de vida faz viver mais, mas a ideia é contestada. "
            "Em Okinawa, os registros de família foram em grande parte destruídos na batalha de 1945 e "
            "reconstruídos depois, o que alimenta o debate sobre as idades. Os nascidos lá depois de 1945 não "
            "mostram longevidade especial, e em Nicoya os nascidos após 1930 também não. O demógrafo Saul Newman "
            "ganhou um Ig Nobel por pesquisas que contestam os dados sobre as pessoas mais velhas do mundo. "
            "Defensores do conceito dizem ter validado as idades com registros civis e da Igreja."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Sogen_Kato",
                "22 July 1899 – c. November 1978) was a Japanese man thought to have been Tokyo's oldest man until July 2010, when his mummified corpse was found in his bedroom. "
                "It was concluded he had likely died in November 1978, aged 79, and his family had never reported his death. "
                "Relatives had rebuffed attempts by ward officials to see Kato in preparations for Respect for the Aged Day later that year [...] "
                "A study following the discovery of Kato's remains found that police did not know if 234,354 people over the age of 100 were still alive. [...] "
                "One of Kato's relatives was found guilty of fraud; his relatives claimed ¥9,500,000 [...] "
                "Newspapers that were found in the room dated back three decades to the Shōwa period, suggesting that Kato's death may have occurred around November 1978.",
                nome="Sogen Kato"),
            wiki("Blue_zone",
                "The blue zone theory represents a region where some people self-attest to exceptional longevity, which has been variously attributed to lifestyle. [...] "
                "Suggested blue zones include Okinawa Prefecture in Japan, Nuoro Province and Bolotana in Sardinia, Italy, the Nicoya Peninsula in Costa Rica, and Icaria, Greece. "
                "Based on an absence of scientific evidence, the concept of blue zones is commonly challenged as unproven. "
                "Subsequent research contradicted initial claims, such as for Okinawa, which experienced substantial decline in life expectancy during the 21st century, and Nicoya, where people born after 1930 did not have exceptional longevity compared to the broader national population. [...] "
                "A 2025 assessment of long-lived populations in Sardinia, Okinawa, Ikaria, and Nicoya cross-checked civil birth and death records, church archives, and genealogical records to minimize false-age claims [...] "
                "people born before World War II had many centenarians, whereas those born after 1945 had no evidence for longevity [...] "
                "The original Koseki [family register] was largely destroyed during the Battle of Okinawa in 1945 and was later reconstructed by American authorities. "
                "This has led to debates about the reliability of Okinawan longevity claims",
                nome="Blue zone"),
            {"url": "https://reporter.anu.edu.au/all-stories/dr-saul-newman-has-uncovered-the-secret-to-living-to-110",
             "titulo": "Following a Blue Zone lifestyle is purported to help extend your lifespan. But do the numbers add up? (ANU Reporter)",
             "idioma": "en",
             "trecho": "Newman, who completed his Bachelor of Science (Honours) and PhD at ANU, won his Ig Nobel Prize for research debunking data on the world’s oldest people"},
        ],
    },
    # 10 os superidosos
    {
        "temas_secundarios": ["memoria", "neurociencia"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "Há pessoas com mais de 80 anos cuja memória se compara à de gente três décadas mais nova. No cérebro desses \"superidosos\", o córtex não afinou como de costume, e uma região é até mais grossa que a de adultos mais jovens.",
        "explicacao": (
            "Desde 2000, pesquisadores da Universidade Northwestern, nos Estados Unidos, acompanham pessoas de 80 "
            "anos ou mais com memória excepcional, apelidadas de SuperAgers pelo neurologista Marsel Mesulam. Para "
            "entrar no grupo, é preciso lembrar pelo menos 9 de 15 palavras num teste de memória tardia, um "
            "desempenho típico de quem tem 50 ou 60 anos. Passaram pelo estudo 290 participantes, e 79 cérebros "
            "doados foram examinados após a morte. Nos exames de imagem, o córtex, a camada externa do cérebro, "
            "não mostra o afinamento comum da idade, e o córtex cingulado anterior, ligado a decisões, emoção e "
            "motivação, é mais espesso que o de adultos mais jovens. Ao microscópio, eles têm mais neurônios de von "
            "Economo, associados ao comportamento social, e neurônios maiores numa região essencial à memória, o "
            "córtex entorrinal, do que pessoas da mesma idade. Os cientistas viram dois caminhos: alguns não "
            "acumulam as placas e emaranhados típicos do Alzheimer, e outros acumulam, mas sem prejuízo aparente. "
            "Eles também tendem a ser muito sociáveis. O que causa tudo isso ainda é uma pergunta aberta."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": "https://news.northwestern.edu/stories/2025/08/what-makes-a-superager",
             "titulo": "What makes a SuperAger? (Northwestern University, 2025)",
             "idioma": "en",
             "trecho": "For 25 years, scientists at Northwestern Medicine have been studying individuals aged 80 and older — dubbed “SuperAgers” — to better understand what makes them tick. "
                       "These unique individuals, who show outstanding memory performance at a level consistent with individuals who are at least three decades younger, challenge the long-held belief that cognitive decline is an inevitable part of aging. [...] "
                       "The term “SuperAger” was coined by Dr. M. Marsel Mesulam [...] "
                       "Since 2000, a cohort of 290 SuperAger participants has passed through the Mesulam Center’s doors, and the scientists have autopsied 79 donated SuperAger brains. [...] "
                       "“One is resistance: they don’t make the plaques and tangles. Two is resilience: they make them, but they don’t do anything to their brains.” [...] "
                       "Exceptional memory performance: SuperAgers score at least 9 out of 15 on a delayed word recall test — on par with individuals in their 50s and 60s. "
                       "Youthful brain structure: Unlike typically aging brains, SuperAgers show no significant thinning of their cortex — the outer layer of the brain — and even have a thicker anterior cingulate cortex than younger adults. "
                       "This crucial region of the brain plays a significant role in integrating information related to decision-making, emotion and motivation. "
                       "Unique cellular traits: SuperAgers have more von economo neurons, which are specialized cells linked to social behavior, and larger entorhinal neurons, which are critical for memory, than their typically aging peers. "
                       "Sociability as a common trait: Despite having diverse lifestyles and varying approaches to exercise, SuperAgers tend to be highly social"},
        ],
    },
    # 11 progéria: uma letra trocada e o envelhecimento comum
    {
        "temas_secundarios": ["genetica", "farmacos"],
        "tipos_espanto": ["conexao_inesperada", "escala_absurda"],
        "gancho": "Uma única letra trocada no DNA, um C por um T, faz crianças envelhecerem fisicamente de 8 a 10 vezes mais rápido. A proteína defeituosa que resulta disso também aparece em células envelhecidas de pessoas comuns.",
        "explicacao": (
            "É a progéria, ou síndrome de Hutchinson-Gilford, descrita em 1886 e de novo em 1897. Ela afeta cerca "
            "de 1 em cada 20 milhões de nascimentos. As crianças parecem normais ao nascer; entre os primeiros sinais "
            "está a dificuldade de ganhar peso, e depois surgem traços raros fora da velhice, como articulações rígidas. A "
            "inteligência fica preservada. A causa só foi achada em 2003: uma mutação pontual no gene LMNA, na "
            "posição 1824, onde uma citosina vira timina. O gene fabrica a lamina A, proteína que sustenta o "
            "núcleo da célula. Com a troca, sai uma versão encurtada, a progerina, que fica presa à borda do "
            "núcleo e o deforma. Os pais de um menino com a doença, a médica Leslie Gordon e o pediatra Scott "
            "Berns, criaram uma fundação de pesquisa sobre ela. Em 2020, os EUA aprovaram o lonafarnibe, remédio "
            "que ajuda a evitar o acúmulo de progerina. O interesse vai além dos pacientes: células envelhecidas "
            "comuns também ativam a produção de progerina, que talvez tenha um papel no envelhecimento normal, e "
            "por isso a doença pode dar pistas sobre como todos envelhecemos."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Progeria",
                "The affected gene, known as lamin A (LMNA), makes a protein necessary for holding the cell nucleus together. "
                "When this gene mutates, an abnormal form of lamin A protein called progerin is produced. [...] "
                "Most children with progeria appear normal at birth and during early infancy. [...] "
                "The earliest symptoms may include a failure to thrive [...] "
                "stiff joints, hip dislocations, and other symptoms generally absent in the non-elderly population. [...] "
                "This poor processing creates an abnormal nuclear morphology [...] "
                "Despite looking and aging physically at a rate 8 to 10 times faster than normal, children and young adults with progeria have normal-to-above-average intelligence [...] "
                "In 2003, the cause of progeria was discovered to be a point mutation in position 1824 of the LMNA gene, which replaces a cytosine with thymine. [...] "
                "so the abnormal protein is permanently attached to the nuclear rim. [...] "
                "Progerin may also play a role in normal human aging, since its production is activated in typical senescent cells. [...] "
                "Gordon, was a physician who did not know anything about progeria until her own son, Sam, was diagnosed at 22 months. "
                "Gordon and her husband, pediatrician Scott Berns, founded the Progeria Research Foundation. [...] "
                "A study from the Netherlands has shown an incidence of 1 in 20 million births. [...] "
                "Progeria was first described in 1886 by Jonathan Hutchinson. It was also described independently in 1897 by Hastings Gilford. [...] "
                "Scientists are interested in progeria partly because it might reveal clues about the normal process of ag [...] "
                "In November 2020, the U.S. Food and Drug Administration approved lonafarnib, which helps prevent buildup of defective progerin and similar proteins.",
                nome="Progeria"),
        ],
    },
    # 12 o alarme que só jovens ouvem
    {
        "temas_secundarios": ["acustica", "sentidos"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Um alarme britânico afasta jovens da porta de lojas com um zumbido de 17,4 kHz, que em geral só eles escutam. O som acabou virando toque de celular, que tocava na sala de aula sem os professores ouvirem.",
        "explicacao": (
            "O aparelho, chamado Mosquito, foi inventado e patenteado por Howard Stapleton em 2005 e testado "
            "primeiro em Barry, no País de Gales, para reduzir a presença de adolescentes perto de uma mercearia. "
            "Stapleton usou os próprios filhos como cobaias para achar a frequência certa. O truque explora a "
            "presbiacusia: na maioria das pessoas, a capacidade de ouvir sons muito agudos piora com a idade, e "
            "isso já costuma ser perceptível por volta dos 18 anos. Segundo o fabricante, o som em geral só é "
            "ouvido por quem tem menos de 25. As versões mais novas também têm uma frequência de 8 kHz, que "
            "quase todos escutam. O feitiço virou contra o feiticeiro quando o zumbido foi transformado em toque "
            "de celular, apelidado de \"Teen Buzz\". Em 2006, o Mosquito levou o Ig Nobel da Paz, o prêmio "
            "satírico para pesquisas que primeiro fazem rir e depois pensar. Houve críticas sérias: um instituto "
            "alemão de segurança do trabalho alertou que bebês e crianças pequenas correm mais risco, porque os "
            "adultos à volta não percebem o som, e entidades ligadas ao autismo protestaram."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("The_Mosquito",
                "The latest version of the device, launched late in 2008, has two frequency settings, one of approximately 17.4 kHz that can generally be heard only by young people, and another at 8 kHz that can be heard by most people. [...] "
                "the manufacturer's product specification furthermore states that the sound can typically be heard by people below 25 years of age. "
                "The ability to hear high frequencies deteriorates in most humans with age (a condition known as presbycusis), typically observable by the age of 18. [...] "
                "The Mosquito machine was invented and patented by Howard Stapleton in 2005, and was originally tested in Barry, Wales, where it was successful in reducing teenagers loitering near a grocery store. [...] "
                "Using his children as test subjects, he determined the frequency of \"The Mosquito\". [...] "
                "The sound was made into a mobile phone ringtone, which could not be heard by teachers if the phone rang during a class. [...] "
                "This ringtone became informally known as \"Teen Buzz\" [...] "
                "The Mosquito won the satirical Ig Nobel for \"peace\" in 2006. "
                "The Ig Nobels celebrate the quirkier side of serious scientific endeavour, honouring \"achievements that first make people laugh, and then make them think\". [...] "
                "On the other hand small children and infants are especially at risk, due to lengthy exposure to the sound, because the adults themselves do not perceive the noise. [...] "
                "The National Autistic Society said in 2008 that it was \"extremely concerned\" about possible harmful effects of the devices upon autistic people.",
                nome="The Mosquito"),
        ],
    },
    # 13 o problema de Molyneux respondido na Índia
    {
        "temas_secundarios": ["sentidos", "aprendizagem_inteligencia", "neurociencia"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "No século XVII, um filósofo perguntou: um cego de nascença que passasse a ver reconheceria só pelo olhar um cubo que conhece pelo tato? Jovens indianos operados de catarata responderam: não, mas aprendem em dias.",
        "explicacao": (
            "A pergunta foi feita por William Molyneux, cuja esposa era cega, e ficou famosa ao aparecer no Ensaio "
            "sobre o entendimento humano, de John Locke, de 1689. Molyneux e Locke apostavam no \"não\"; Leibniz "
            "achava que sim. No século XII, Ibn Tufail já tinha imaginado uma versão com cores, e com a resposta "
            "oposta. Testar era quase impossível: em 1971, um pesquisador estimou que se conheciam menos de vinte "
            "casos de cegos de nascença que passaram a ver em mil anos. Isso mudou com o Projeto Prakash, do "
            "neurocientista Pawan Sinha, do MIT, que opera crianças com cegueira tratável na Índia. Cinco jovens de "
            "8 a 17 anos, que só distinguiam claro de escuro, foram operados entre 2007 e 2010. Em até 48 horas, "
            "eles distinguiam objetos pela visão quase tão bem quanto pelo tato, mas não ligavam o que viam ao que "
            "tinham tocado: acertavam pouco mais do que no chute. Dias ou meses depois, três deles foram testados de "
            "novo e já acertavam de 80% a 90%. O projeto também contrariou a crença de que operar crianças mais "
            "velhas não traria ganhos: até adultos jovens melhoram bastante a visão."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Molyneux%27s_problem",
                "To which the acute and judicious proposer answers, \"Not. [...] "
                "I agree with this thinking gentleman, whom I am proud to call my friend, in his answer to this problem [...] "
                "It was first formulated by William Molyneux, and notably referenced in John Locke's An Essay Concerning Human Understanding (1689). [...] "
                "The question was originally posed to Locke by philosopher William Molyneux, whose wife was blind. [...] "
                "A similar problem was also addressed earlier in the 12th century by Ibn Tufail (Abubacer), in his philosophical novel, Hayy ibn Yaqdhan (Philosophus Autodidactus). "
                "This version focused on colors rather than shapes, and gave the opposite solution [...] "
                "Leibniz (German philosopher, 1646–1716) also discussed this problem, but derived a different answer. [...] "
                "Hence it is possible to infer from one type of idea to another. [...] "
                "In 1971, Alberto Valvo estimated that fewer than twenty cases have been known in the last 1000 years. "
                "In 2003, Pawan Sinha, a professor at the Massachusetts Institute of Technology, set up a program in the framework of the Project Prakash and eventually had the opportunity to find five individuals who satisfied the requirements for an experiment aimed at answering Molyneux's question. "
                "Prior to treatment, the subjects (aged 8 to 17) were only able to discriminate between light and dark [...] "
                "The surgical treatments took place between 2007 and 2010 [...] "
                "A carefully designed test was submitted to each subject within the next 48 hours. "
                "Based on its result, the experimenters concluded that the answer to Molyneux's problem is, in short, \"no\". "
                "Although after restoration of sight, the subjects could distinguish between objects visually almost as effectively as they would do by touch alone, they were unable to form the connection between an object perceived using the two different senses. "
                "The correlation was barely better than if the subjects had guessed. [...] "
                "However, the experimenters could test three of the five subjects on later dates (5 days, 7 days, and 5 months after, respectively) and found that the performance in the touch-to-vision case improved significantly, reaching 80–90%.",
                nome="Molyneux's problem"),
            {"url": "https://news.mit.edu/2019/mit-professor-pawan-sinha-india-curing-blind-children-research-0125",
             "titulo": "The gift of light, through science and service (MIT News, 2019)",
             "idioma": "en",
             "trecho": "Project Prakash, from the Sanskrit word for light, is a nonprofit organization that provides surgeries to congenitally blind children in India, and observes them during recovery to track the development of sight in the brain. [...] "
                       "Conventional wisdom in childhood blindness suggests that older children should not see significant gains post-surgery, since their brain’s visual machinery should be set. "
                       "However, in one of his first key scientific findings enabled by Project Prakash, Sinha found that even young adults can make significant gains in visual function after surgical intervention."},
        ],
    },
    # 14 o relógio epigenético
    {
        "temas_secundarios": ["genetica", "limites_humanos"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "Marcas químicas no DNA revelam a idade de alguém com erro mediano de 3,6 anos. E esse \"relógio\" mostra que partes do corpo envelhecem em ritmos diferentes: num centenário, o cerebelo parece 15 anos mais novo.",
        "explicacao": (
            "Com a idade, mudam as marcas químicas chamadas grupos metil em certos pontos do DNA, as regiões CpG. "
            "Essas marcas ajudam a regular quais genes ficam ativos. Em 2013, o bioestatístico Steve "
            "Horvath, da Universidade da Califórnia em Los Angeles, publicou o primeiro relógio que funciona em "
            "vários tecidos: usou 8.000 amostras de 51 tecidos e tipos de célula para escolher 353 pontos cujo "
            "padrão de metilação prevê a idade. Como a mesma fórmula vale para qualquer amostra, dá para comparar "
            "a \"idade\" de órgãos diferentes de uma mesma pessoa. Analisando 30 regiões do corpo de seis "
            "centenários, o relógio indicou que o cerebelo envelhece devagar, cerca de 15 anos a menos que o "
            "esperado. Já o tecido mamário feminino parece mais velho que o sangue da mesma mulher. Em células-"
            "tronco embrionárias e em células adultas reprogramadas para virar células-tronco, o relógio marca "
            "perto de zero, e o transplante de medula de um doador jovem rejuvenesce a idade epigenética do "
            "sangue do receptor. Os 353 pontos provavelmente não causam o envelhecimento: eles o registram."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Epigenetic_clock",
                "The method relies on age-related modifications to DNA that occur over time and regulate how genes are expressed. "
                "Many epigenetic clocks are based on the analysis of DNA methylation, measuring the accumulation of methyl groups to CpG regions of DNA molecules. [...] "
                "The first multi-tissue epigenetic clock, Horvath's epigenetic clock, was developed by Steve Horvath, a professor of human genetics  and biostatistics at UCLA (Horvath 2013). [...] "
                "The age estimator was developed using 8,000 samples from 82 Illumina DNA methylation array datasets, encompassing 51 healthy tissues and cell types. "
                "The major innovation of Horvath's epigenetic clock lies in its wide applicability: the same set of 353 CpGs and the same prediction algorithm is used irrespective of the DNA source within the organism [...] "
                "This property allows one to compare the ages of different areas of the human body using the same aging clock. [...] "
                "the 353 clock CpGs, therefore, likely have no causal effect. [...] "
                "it is close to zero for embryonic and induced pluripotent stem cells [...] "
                "The median error of estimated age is 3.6 years across a wide spectrum of tissues and cell types [...] "
                "An application of epigenetic clock to 30 anatomic sites from six centenarians and younger subjects revealed that the cerebellum ages slowly: it is about 15 years younger than expected in a centenarian. [...] "
                "normal breast tissue samples from women without cancer have been found to be substantially older than blood samples collected from the same women at the same time. [...] "
                "Hematopoietic stem cell transplantation, which transplants these cells from a young donor to an older recipient, rejuvenates the epigenetic age of blood to that of the donor.",
                nome="Epigenetic clock"),
        ],
    },
    # 15 a linha neonatal: o nascimento gravado nos dentes
    {
        "temas_secundarios": ["anatomia", "gravidez"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Os dentes de leite guardam a marca do nascimento: uma linha no esmalte, mais escura e larga que as outras, separa o que se formou antes e depois dele. Peritos a usam para saber se um bebê nasceu vivo e quanto viveu.",
        "explicacao": (
            "O esmalte dos dentes se forma em camadas e deixa linhas de crescimento, as estrias de Retzius. "
            "Os dentes de leite começam a se formar antes do nascimento, e por isso "
            "uma dessas linhas é especial: a linha neonatal, mais escura e mais larga que as demais. Ela aparece "
            "tanto no esmalte quanto na dentina e marca uma pausa prolongada na formação do esmalte bem na hora "
            "do nascimento. A causa é o estresse fisiológico da passagem para a vida fora do útero, que muda a "
            "direção e o grau da mineralização. Os fatores exatos que definem a sua formação e a sua largura ainda "
            "não estão claros. A posição da linha varia de dente para dente. Na odontologia forense, ela ajuda a "
            "esclarecer se uma criança morreu antes ou depois de nascer: medindo quanto tecido duro se formou "
            "depois da linha, dá para estimar por quanto tempo o bebê sobreviveu."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Neonatal_line",
                "The neonatal line is a particular band of incremental growth lines seen in histologic sections of both enamel and dentin of primary teeth. "
                "It belongs to a series of a growth lines in tooth enamel known as the Striae of Retzius denoting the prolonged rest period of enamel formation that occurs at the time of birth. "
                "The neonatal line is darker and larger than the rest of the striae of retzius. "
                "The neonatal line is the demarcation between the enamel formation before birth and after birth i.e., prenatal and postnatal enamel respectively. [...] "
                "The position of the neonatal line differs from tooth to tooth [...] "
                "The formation of the neonatal line is caused by changes in the direction and degree of tooth mineralization caused by the biological stress from passing into extra uterine life. "
                "Specific factors underlying its formation and width still remain unclear. [...] "
                "In forensic dentistry, the neonatal line can be used to distinguish matters such as if a child died before or after birth and approximately how long a child lived after birth. "
                "The neonatal line can be used as a marker for the exact period of survival of an infant through the measurement of the amount of postnatal hard tissue formation",
                nome="Neonatal line"),
        ],
    },
]
