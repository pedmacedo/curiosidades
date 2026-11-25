LOTE = "2026-11-25-neurociencia-01"
AREA = "mente"
TEMA = "neurociencia"
W = "https://en.wikipedia.org/wiki/"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


def fonte(url, titulo, trecho, idioma="en"):
    return {"url": url, "titulo": titulo, "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Cajal contra Golgi, com a técnica do próprio Golgi
    {
        "temas_secundarios": ["historia_medicina", "anatomia"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "O Nobel de Medicina de 1906 foi dividido entre dois rivais que não se falavam. Cajal usou a técnica de coloração inventada por Golgi para mostrar que o próprio Golgi estava errado sobre como o cérebro é feito.",
        "explicacao": (
            "Por pressão financeira, o italiano Camillo Golgi foi trabalhar num hospital para doentes crônicos e "
            "montou um laboratório simples numa antiga cozinha do lugar. Ali, em 1873, criou a \"reação negra\": "
            "o tecido nervoso endurecido com dicromato de potássio e depois tratado com nitrato de prata deixava "
            "algumas células, ao acaso, pintadas de preto por inteiro sobre um fundo amarelo. Pela primeira vez "
            "dava para seguir os ramos de um neurônio. Golgi, porém, enxergava ali uma rede única e contínua de "
            "fibras, a chamada teoria reticular. O espanhol Santiago Ramón y Cajal passou a usar o método em "
            "1887, aprimorou-o e, em 1888, relatou que as células nervosas do cérebro de aves não eram "
            "contínuas. Era a base da doutrina do neurônio: o sistema nervoso é feito de células individuais. "
            "Os dois dividiram o Nobel de Fisiologia ou Medicina de 1906, mas, de campos opostos, já se "
            "detestavam. Em Estocolmo, Cajal conseguiu elogiar o rival; Golgi não retribuiu, e sua palestra do "
            "Nobel ainda mostrava parte do cerebelo tomada por uma rede de fibras. A disputa só terminou nos anos "
            "1950, quando o microscópio eletrônico mostrou neurônios separados, ligados por sinapses."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Neuron_doctrine",
                "A landmark development came from Camillo Golgi who invented a silver staining technique in 1873 which he called la reazione nera (black reaction) [...] "
                "Unfortunately Golgi described the nervous system as a continuous single network, in support of a notion called reticular theory. [...] "
                "Santiago Ramón y Cajal started investigating nervous system in 1887 using Golgi stain. "
                "In the first issue of the Revista Trimestral de Histología Normal y Patológica (May, 1888) Ramón y Cajal reported that the nerve cells were not continuous in the brain of birds. [...] "
                "Golgi and Ramón y Cajal were jointly awarded the 1906 Nobel Prize for Physiology or Medicine, but the controversy between the two scientists continued. "
                "The matter was finally resolved in the 1950s with the development of electron microscopy by which it was unambiguously demonstrated that nerve cells were individual cells interconnected through synapses",
                nome="Neuron doctrine"),
            wiki("Camillo_Golgi",
                "Financial pressure prompted him to join the Hospital of the Chronically Ill [...] "
                "he set up a simple laboratory on his own in a refurbished hospital kitchen, and it was there that he started making his most notable discoveries. [...] "
                "he discovered a method of staining nervous tissue that would stain a limited number of cells at random in their entirety. "
                "He first treated the tissue with potassium dichromate to harden it, and then with silver nitrate. [...] "
                "against a yellow background. This makes it easier to trace the structure of the nerve cells in the brain for the first time. [...] "
                "his later works including the Nobel Lecture showed the entire granular layer of the cerebellar cortex occupied by a network of branching and anastomosing nerve processes. "
                "This was due to his strong conviction in the reticular theory. [...] "
                "Cajal and Golgi, being from opposing camps, came to hate each other and would not speak. "
                "When they arrived in Stockholm to receive their joint prize, Cajal managed to put their differences aside enough to praise Golgi, but Golgi did not reciprocate.",
                nome="Camillo Golgi"),
            wiki("Santiago_Ramón_y_Cajal",
                "There he first learned about Golgi's method, a cell staining method which uses potassium dichromate and silver nitrate to stain a subset of neurons a dark black color, while leaving the surrounding cells transparent. "
                "This method, which he improved, was central to his work",
                nome="Santiago Ramón y Cajal"),
        ],
    },
    # 2 o cérebro de Einstein numa caixa de sidra
    {
        "temas_secundarios": ["relatividade", "historia_medicina"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Einstein queria que suas cinzas fossem espalhadas em segredo, mas o patologista da autópsia ficou com o cérebro dele. Fatiado em uns 240 blocos, ele passou mais de vinte anos em potes dentro de uma caixa de sidra.",
        "explicacao": (
            "Einstein morreu em 1955. Na autópsia, o patologista Thomas Harvey retirou o cérebro e o pesou: "
            "1.230 gramas. Se houve consentimento é assunto disputado; pesquisas mais recentes indicam que a "
            "retirada foi feita sem permissão dele nem da família, e o filho mais velho, Hans Albert, só a "
            "aprovou depois do fato. Harvey cortou o órgão em cerca de 240 blocos de mais ou menos 1 cm³, "
            "ficou com parte deles e entregou outros a patologistas. Em 1978, o jornalista Steven Levy "
            "reencontrou as fatias com Harvey, guardadas em álcool em dois grandes potes de vidro dentro de uma "
            "caixa de sidra. Os estudos que vieram depois buscaram a marca da genialidade. Em 1984, a equipe de "
            "Marian Diamond publicou que Einstein tinha mais células da glia por neurônio que 11 homens de "
            "inteligência comum; a diferença, porém, só foi estatisticamente significativa numa região. Os "
            "críticos apontaram problemas: um único Einstein, controles com idade média de 64 anos, contra 76 "
            "dele, e pesquisadores que sabiam qual cérebro era o famoso. Para o neurologista Terence Hines, todo "
            "cérebro humano tem algo de único, e ligar essas diferenças ao gênio vai além das evidências. Em "
            "2010, os herdeiros de Harvey entregaram o que restava a um museu nacional de saúde e medicina dos EUA."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Albert_Einstein's_brain",
            "Albert Einstein's brain was removed shortly after his death, even though he wished for it to not be removed: he wanted his ashes to be spread in secret. [...] "
            "Einstein's autopsy was conducted in the lab of Thomas Stoltz Harvey. Shortly after Einstein died in 1955, Harvey removed and weighed the brain at 1230 g. [...] "
            "He kept some of the pieces to himself while others were given to leading pathologists. [...] "
            "Harvey dissected the brain into about 240 blocks (each about 1 cm3) [...] "
            "Whether or not Einstein's brain was preserved with his prior consent is a matter of dispute. [...] "
            "More recent research has suggested that the brain was removed and preserved without the permission of either Einstein or his close relatives. "
            "Hans Albert Einstein, the physicist's elder son, endorsed the removal after the event. [...] "
            "In 1978, Einstein's brain was rediscovered in Harvey's possession by journalist Steven Levy. "
            "Its sections had been preserved in alcohol in two large mason jars within a cider box for over twenty years. [...] "
            "In 2010, Harvey's heirs transferred all of his holdings constituting the remains of Einstein's brain to the National Museum of Health and Medicine. [...] "
            "In 1984, Marian Diamond and her associates were the first ever to publish research on the brain of Albert Einstein. "
            "She compared the ratio of glial cells in Einstein's brain with that of the preserved brains of 11 other males. [...] "
            "Einstein's brain had more glial cells relative to neurons in all areas studied, but only in the left inferior parietal area was the difference statistically significant. [...] "
            "The limitation that Diamond admits in her study is that she had only one Einstein to compare with 11 brains of normal intelligence individuals. [...] "
            "although Einstein's brain was 76, it was compared to brains that averaged 64 in age [...] "
            "Researchers knew which brain was Einstein's and which were controls, allowing possible conscious or unconscious bias and preventing impartial research. [...] "
            "Hines maintains that all human brains are unique and different from others in some ways. "
            "Therefore, assuming unique features in Einstein's brain were connected with his genius, in Hines' opinion, goes beyond the evidence.",
            nome="Albert Einstein's brain")],
    },
    # 3 Phineas Gage foi guiar diligências no Chile
    {
        "temas_secundarios": ["historia_medicina", "consciencia"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Phineas Gage, que teve a cabeça atravessada por uma barra de ferro em 1848, entrou para os livros como o homem que virou outra pessoa. Mas depois ele passou anos guiando diligências de seis cavalos no Chile.",
        "explicacao": (
            "Em 13 de setembro de 1848, Gage chefiava uma turma que abria caminho para uma ferrovia em Vermont, "
            "nos EUA. A pólvora explodiu antes da hora e disparou a barra de ferro que ele usava para socar a "
            "carga no buraco da rocha: 1,1 metro de comprimento e 6 quilos. A barra entrou pelo rosto, passou "
            "por trás do olho esquerdo e saiu pelo alto do crânio, destruindo boa parte do lobo frontal "
            "esquerdo. Ele sobreviveu. O médico John Harlow descreveu o antigo capataz exemplar como inconstante, "
            "impaciente e dado a palavrões, a ponto de os amigos dizerem que ele \"não era mais o Gage\". O caso "
            "virou presença fixa nos cursos de neurologia e psicologia, mas os relatos científicos e populares "
            "quase sempre exageraram e distorceram essas mudanças. Os registros contam outra história. Em 1852, "
            "Gage foi contratado para guiar diligências no Chile, na rota entre Valparaíso e Santiago, com seis "
            "cavalos, jornadas de 13 horas por estradas ruins e passageiros para atender. Um médico americano que "
            "o conheceu lá em 1858 e 1859 o descreveu com boa saúde e sem nenhum prejuízo das faculdades mentais. "
            "Para o psicólogo Malcolm Macmillan e outros, as mudanças mais graves teriam sido temporárias, e a "
            "rotina do trabalho pode ter ajudado na recuperação. Gage morreu em 1860, depois de crises epilépticas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Phineas_Gage",
            "was an American railroad construction foreman remembered for his improbable[B1] survival of an accident in which a large iron rod was driven completely through his head, destroying much of his brain's left frontal lobe [...] "
            "friends saw him (for a time at least) as \"no longer Gage\". [...] "
            "Gage is a fixture in the curricula of neurology, psychology, and neuroscience [...] "
            "Historically, both scientific and popular accounts of Gage have almost always severely exaggerated and distorted his behavioral changes, frequently contradicting the known facts. "
            "A report of Gage's physical and mental condition shortly before his death implies that his most serious mental changes were temporary, so that in later life he was far more functional, and socially far better adapted, than in the years immediately following his accident. "
            "A social recovery hypothesis suggests that his work as a stagecoach driver in Chile fostered this recovery by providing daily structure that allowed him to regain lost social and personal skills. [...] "
            "On September 13, 1848, Gage was directing a work gang blasting rock while preparing the roadbed for the Rutland & Burlington Railroad south of the village of Cavendish, Vermont. [...] "
            "the tamping iron sparked against the rock and (possibly because the sand had been omitted) the powder prematurely exploded. [...] "
            "three feet seven inches (1.1 m) long, and weighing 13+1⁄4 pounds (6.0 kg) [...] "
            "it passed behind the left eye, through the left side of the brain, then completely out the top of the skull through the frontal bone. [...] "
            "In August 1852, Gage was invited to Chile to work as a long-distance stagecoach driver there, \"caring for horses, and often driving a coach heavily laden and drawn by six horses\" on the Valparaíso–Santiago route. [...] "
            "In February 1860, Gage began to have epileptic seizures. [...] "
            "He is fitful, irreverent, indulging at times in the grossest profanity (which was not previously his custom), manifesting but little deference for his fellows, impatient of restraint or advice when it conflicts with his desires [...] "
            "In 1860, an American physician who had known Gage in Chile in 1858 and 1859 described him as still \"engaged in stage driving [and] in the enjoyment of good health, with no impairment whatever of his mental faculties\". [...] "
            "Macmillan writes that this conclusion is reinforced by the responsibilities and challenges associated with stagecoach work such as that done by Gage in Chile [...] "
            "But above all, they had to have the kind of personality that enabled them to get on well with their passengers. [...] "
            "A day's work for Gage meant \"a 13-hour journey over 100 miles [160 km] of poor roads",
            nome="Phineas Gage")],
    },
    # 4 a célula da avó e o neurônio Jennifer Aniston
    {
        "temas_secundarios": ["memoria", "ia_robotica"],
        "tipos_espanto": ["contraintuitivo", "origem_inesperada"],
        "gancho": "Por volta de 1969, a \"célula da avó\", um neurônio que reconheceria só a sua avó, era piada de aula. Em 2005, registros em pacientes acordados acharam neurônios que disparavam para fotos de Jennifer Aniston.",
        "explicacao": (
            "Por volta de 1969, o cientista cognitivo Jerry Lettvin contava aos alunos do MIT uma anedota "
            "inventada: um neurocirurgião teria achado no cérebro milhares de \"células da mãe\", que só "
            "respondiam à mãe, e as teria removido do personagem Portnoy, do romance de Philip Roth, curando sua "
            "obsessão materna. Daí veio a \"célula da avó\", ideia que de início servia mais para piadas e para "
            "ser derrubada nos livros: um único neurônio dedicado a um único rosto parecia impraticável. Em "
            "2005, a piada ganhou outra cara. Neurocirurgiões da Universidade da Califórnia em Los Angeles, "
            "entre eles Itzhak Fried e Rodrigo Quian Quiroga, registraram neurônios isolados em pacientes com "
            "epilepsia, plenamente conscientes, enquanto viam fotos de celebridades. Certos neurônios disparavam "
            "para uma pessoa específica, como Jennifer Aniston ou Bill Clinton. Um neurônio ligado a Halle Berry "
            "respondia a imagens dela e também ao nome \"Halle Berry\", e não a fotos de várias outras atrizes. "
            "Isso não prova que exista uma célula exclusiva para cada pessoa: o neurônio estudado provavelmente "
            "não era o único a responder àquele conceito. Os próprios pesquisadores falam em codificação "
            "esparsa, em que poucos neurônios, e não um só, representam cada pessoa ou objeto."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Grandmother_cell",
            "The grandmother cell, sometimes called the \"Jennifer Aniston neuron\", is a hypothetical neuron that represents a complex but specific concept or object. [...] "
            "Rather than serving as a serious hypothesis, the \"grandmother cell\" concept was initially largely used in jokes and came to be used as a \"straw man\" or \"foil\" for a discussion of ensemble theories in introductory textbooks. [...] "
            "Around 1969, Lettvin introduced the term \"grandmother cell\" in a course he was teaching at MIT, telling a fictitious anecdote about a neurosurgeon who had discovered a group of \"mother cells\" in the brain that \"responded uniquely only to a mother [...] "
            "the neurosurgeon went on to remove (ablate) all these \"several thousand separate neurons\" from the brain of Portnoy, the title character of Philip Roth's 1969 novel Portnoy's Complaint, thus curing him from his obsession with his mother [...] "
            "the term had \"become a shorthand for invoking all of the overwhelming practical arguments against a one-to-one object coding scheme. "
            "No one wants to be accused of believing in grandmother cells.\" "
            "However, in that year UCLA neurosurgeons Itzhak Fried, mentee Rodrigo Quian Quiroga and others published findings on what they would come to call the \"Jennifer Aniston neuron\". "
            "After operating on patients who experience epileptic seizures, the researchers showed photos of celebrities like Jennifer Aniston. "
            "The patients, who were fully conscious, often had a particular neuron fire, suggesting that the brain has Aniston-specific neurons. [...] "
            "In 2005, a UCLA and Caltech study found evidence of different cells that fire in response to particular people, such as Bill Clinton or Jennifer Aniston. "
            "A neuron for Halle Berry, for example, might respond \"to the concept, the abstract entity, of Halle Berry\", and would fire not only for images of Halle Berry, but also to the actual name \"Halle Berry\". "
            "However, there is no suggestion in that study that only the cell being monitored responded to that concept, nor was it suggested that no other actress would cause that cell to respond (although several other presented images of actresses did not cause it to respond). "
            "The researchers believe that they have found evidence for sparseness, rather than for grandmother cells.",
            nome="Grandmother cell")],
    },
    # 5 o axônio gigante não é da lula-gigante
    {
        "temas_secundarios": ["vida_marinha", "eletromagnetismo"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "O \"axônio gigante da lula\", que revelou como os neurônios disparam, não vem da lula-gigante, mas de uma lula comum. Ele chega a 1,5 mm de espessura: largo o bastante para receber eletrodos por dentro.",
        "explicacao": (
            "Lulas escapam com um jato d'água, expelido por contrações rápidas do corpo, e quem dispara essas "
            "contrações é um axônio enorme, em geral com cerca de 0,5 mm de diâmetro e às vezes 1,5 mm. Sinais "
            "correm mais rápido em fibras largas, e esse axônio não tem mielina, a capa que acelera a condução "
            "nos nervos: o diâmetro grande é o jeito de a lula ganhar velocidade na fuga. Para quem estudava "
            "nervos, era um presente. Em julho de 1939, no laboratório de biologia marinha de Plymouth, na "
            "Inglaterra, Alan Hodgkin e Andrew Huxley enfiaram uma cânula fina no axônio de lulas e registraram "
            "potenciais de ação de dentro da fibra nervosa. Mandaram uma nota à Nature pouco antes da Segunda "
            "Guerra, e a pesquisa parou: Hodgkin foi trabalhar com radar, e Huxley, com o controle por radar de "
            "canhões antiaéreos. Na volta, com aparelhos que eles mesmos construíram e a técnica do grampo de "
            "voltagem, mediram as correntes de íons através da membrana. Em 1952 publicaram um modelo "
            "matemático: o impulso corre pela membrana como uma onda de sódio entrando e potássio saindo. O "
            "modelo virou base da neurociência e rendeu aos dois o Nobel de 1963. A espécie das experiências era "
            "a lula-de-nadadeira-longa do Atlântico, bem longe dos gigantes do fundo do mar."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Squid_giant_axon",
                "The squid giant axon is the very large (up to 1.5 mm in diameter; typically around 0.5 mm) axon that controls part of the water jet propulsion system in squid. [...] "
                "through which water can be rapidly expelled by the fast contractions of the body wall muscles of the animal. "
                "This contraction is initiated by action potentials in the giant axon. "
                "Action potentials travel faster in an axon with a large diameter than a smaller one, and squid have evolved the giant axon to improve the speed of their escape response. [...] "
                "In their Nobel Prize–winning work uncovering ionic mechanism of action potentials, Alan Hodgkin and Andrew Huxley performed experiments on the squid giant axon, using the longfin inshore squid as the model organism. [...] "
                "it allowed them to insert voltage clamp electrodes inside the lumen of the axon. "
                "While the squid axon is very large in diameter, it is unmyelinated, which decreases the conduction velocity substantially.",
                nome="Squid giant axon"),
            wiki("Alan_Hodgkin",
                "He moved all his equipment to the Plymouth Marine Laboratory in July 1939. "
                "There, he and Huxley managed to insert a fine cannula into the giant axon of squids and record action potentials from inside the nerve fibre. "
                "They sent a short note of their success to  Nature just before the outbreak of World War II. [...] "
                "he transferred to the Telecommunications Research Establishment (TRE) where he worked on the development of centimetric radar [...] "
                "they used a technique of electrophysiology, known as the voltage clamp to measure ionic currents through the membranes of squid axons",
                nome="Alan Hodgkin"),
            wiki("Andrew_Huxley",
                "They made their discovery from the giant axon of the Atlantic squid. [...] "
                "Then World War II broke out, and their research was abandoned. "
                "Huxley was recruited by the British Anti-Aircraft Command, where he worked on radar control of anti-aircraft guns. [...] "
                "Continuing their work in Plymouth, they were, within six years, able to solve the problem using equipment they built themselves. "
                "The solution was that nerve impulses, or action potentials, do not travel down the core of the fiber, but rather along the outer membrane of the fiber as cascading waves of sodium ions diffusing inward on a rising pulse and potassium ions diffusing out on a falling edge of a pulse. [...] "
                "This model forms the basis of most of the models used in neurobiology during the following four decades.",
                nome="Andrew Huxley"),
            wiki("Hodgkin–Huxley_model",
                "Alan Hodgkin and Andrew Huxley described the model in 1952 to explain the ionic mechanisms underlying the initiation and propagation of action potentials in the squid giant axon. "
                "They received the 1963 Nobel Prize in Physiology or Medicine for this work.",
                nome="Hodgkin–Huxley model"),
            wiki("Glia",
                "The myelin sheath insulates the nerve fiber from the extracellular fluid and speeds up signal conduction along the nerve fiber.",
                nome="Glia"),
        ],
    },
    # 6 bombas atômicas, carbono-14 e neurônios novos
    {
        "temas_secundarios": ["memoria", "guerra_fria"],
        "tipos_espanto": ["conexao_inesperada", "misterio_aberto"],
        "gancho": "Testes de bombas atômicas deixaram carbono-14 extra em quem viveu nas décadas seguintes. Com essa marca, cientistas concluíram que o cérebro adulto ganha neurônios. Em 2018, um estudo não os achou, e o debate segue.",
        "explicacao": (
            "Durante muito tempo se acreditou que nascemos com um número fixo de neurônios e que não dá para "
            "ganhar novos depois do nascimento, como resume Jonas Frisén, do Instituto Karolinska, na Suécia. O "
            "grupo dele achou um jeito engenhoso de medir isso. Os testes nucleares feitos ao ar livre até 1963 "
            "quase dobraram a concentração de carbono-14 na atmosfera, e essa marca passou aos tecidos de todos "
            "os seres vivos da época; como ela vem caindo uns 4% ao ano desde então, a quantidade dentro de uma "
            "célula indica quando ela se formou. Num estudo publicado em 2013, a equipe concluiu que mais de um "
            "terço dos neurônios do hipocampo, região crucial para aprender e lembrar, se renova ao longo da vida, "
            "cerca de 1.400 por dia num adulto. Em março de 2018, uma equipe de São Francisco examinou 59 "
            "amostras de hipocampo humano, do feto ao adulto, e viu os neurônios jovens rarearem nos primeiros "
            "anos de vida até níveis indetectáveis em adultos. No mês seguinte, cientistas da Universidade "
            "Columbia analisaram cérebros de 28 doadores saudáveis, de 14 a 79 anos, e acharam milhares de "
            "neurônios imaturos tanto nos mais jovens quanto nos mais velhos. A quantidade de neurônios que nascem "
            "no hipocampo adulto continua controversa, e o papel deles no cérebro humano segue incerto."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [
            fonte("https://news.ki.se/new-neurons-generated-in-the-hippocampus-of-adult-humans",
                "New neurons generated in the hippocampus of adult humans (Karolinska Institutet)",
                "The hippocampus is a region in the brain crucial for the ability to learn and remember. "
                "In a new study, published in the journal Cell, researchers at Karolinska Institutet show that a large number of new neurons are generated in the hippocampus of adult humans – which has long been an issue of debate. "
                "To reach this conclusion, the researchers measured the amount of carbon-14 found in humans as a result of nuclear testing during the 50s and 60s. [...] "
                "\"It was thought for a long time that we are born with a certain number of neurons, and that it is impossible to get new neurons after birth,\" says Jonas Frisén. [...] "
                "In the Cell study the researchers show that more than one-third of the neurons in the hippocampus are regularly renewed trough out life. "
                "Each day, about 1,400 neurons are being born in the adult human brain, the rate declining slightly during aging. [...] "
                "Published: 07-06-2013"),
            wiki("Bomb_pulse",
                "The bomb pulse is the sudden increase of carbon-14 (14C) in Earth's atmosphere due to the hundreds of above-ground nuclear tests that started in 1945 and intensified after 1950 until 1963 [...] "
                "These blasts were followed by an almost doubling of the relative concentration of 14C in the atmosphere. [...] "
                "Since the nuclear test ban in 1963, atmospheric 14C relative concentration has been decreasing at 4% per year. "
                "This continuous decrease permits scientists to determine, among other things, the age of deceased people and allows them to study cell activity in tissues. [...] "
                "Doubling of the concentration of 14C in the atmosphere is reflected in the tissues and cells of all organisms that lived around the period of nuclear testing.",
                nome="Bomb pulse"),
            fonte(EPMC + "PMC6179355/fullTextXML",
                "Sorrells et al. (2018), Human hippocampal neurogenesis drops sharply in children to undetectable levels in adults, Nature",
                "Human hippocampal neurogenesis drops sharply in children to undetectable levels in adults [...] "
                "San Francisco, California 94143, USA [...] "
                "We conclude that recruitment of young neurons to the primate hippocampus declines rapidly during the first years of life, and that DG neurogenesis does not continue, or is extremely rare, in the adult human. [...] "
                "We used 59 postmortem and intraoperative samples of the human hippocampus"),
            fonte("https://www.cuimc.columbia.edu/news/even-old-brains-can-make-new-neurons-study-finds",
                "Even Old Brains Can Make New Neurons, Study Finds (Columbia University Irving Medical Center)",
                "April 5, 2018 [...] "
                "A recent study of human brains was also unable to find new neurons in adult brains. [...] "
                "Boldrini and Mann's team used a combination of molecular probes and mathematical modeling to track neurogenesis in brains from 28 healthy donors ranging in age from 14 to 79 years old. [...] "
                "\"We found there were on the order of thousands of neuroprogenitor cells and immature neurons both in the youngest and the oldest people analyzed,\" said Boldrini."),
            wiki("Adult_neurogenesis",
                "The numbers of neurons born in the human adult hippocampus remains controversial [...] "
                "The role of new neurons in human adult brain function thus remains unclear.",
                nome="Adult neurogenesis"),
        ],
    },
    # 7 do verme à mosca: mapas completos de sistemas nervosos
    {
        "temas_secundarios": ["ia_robotica", "insetos"],
        "tipos_espanto": ["escala_absurda", "engenhosidade"],
        "gancho": "O primeiro mapa completo das ligações de um sistema nervoso, o de um verme com 302 neurônios, saiu em 1986, traçado à mão. O do cérebro de uma mosca, com uns 130 mil, exigiu IA e um mutirão de revisores.",
        "explicacao": (
            "O verme Caenorhabditis elegans tem menos de 1 mm e um sistema nervoso com 302 neurônios e cerca de "
            "5 mil conexões. Foi o primeiro animal a ter o conectoma, o \"diagrama de fiação\" dos neurônios, "
            "reconstruído por completo, a partir da anotação manual de imagens de microscópio eletrônico "
            "publicada por John White, Sydney Brenner e colegas em 1986. Em 2019, com outra técnica, o mapa foi "
            "refeito e ganhou 1.500 sinapses que tinham escapado. A mosca-das-frutas pedia outra escala. Um volume "
            "com o cérebro inteiro de uma fêmea foi fotografado em 2017, mas os programas da época não davam "
            "conta de reconstruí-lo. Em 2023, redes neurais artificiais separaram automaticamente os neurônios e "
            "acharam as sinapses, e um grande esforço coletivo de neurocientistas, o FlyWire, corrigiu os erros "
            "à mão. O resultado tem cerca de 50 milhões de sinapses químicas entre uns 130 mil neurônios. Mesmo "
            "assim, o mapa sozinho não basta para simular a mosca: faltam as junções elétricas entre neurônios, "
            "os neuromoduladores, os hormônios e o papel da glia. E, ao comparar conectomas de moscas "
            "diferentes, os pesquisadores viram que os tipos de célula e as ligações fortes se repetem, mas o peso "
            "das conexões varia surpreendentemente de um animal para outro."
        ),
        "nivel": 2, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Connectome",
                "Caenorhabditis elegans., commonly referred to as C. Elegans, is a small (<1 mm) nematode (or roundworm). "
                "It has a very small nervous system with 302 neurons and about 5000 synaptic connections [...] "
                "It was the first animal with a fully reconstructed synaptic connectome [...] "
                "The C. elegans connectome reconstruction began with manual annotation of electron micrographs, published by White, Brenner et al., in 1986.",
                nome="Connectome"),
            wiki("Caenorhabditis_elegans",
                "In 2019 the connectome of the male was published using a technique distinct from that used for the hermaphrodite. "
                "The same paper used the new technique to redo the hermaphrodite connectome, finding 1,500 new synapses.",
                nome="Caenorhabditis elegans"),
            wiki("Drosophila_connectome",
                "The available connectomes show only chemical synapses - other forms of inter-neuron communication such as gap junctions or neuromodulators are not represented. [...] "
                "In 2017, a full adult fly brain (FAFB) volume was imaged by a team at Janelia Research Campus using a novel high-throughput serial section transmission electron microscopy (ssTEM) pipeline. "
                "At the time, however, automated methods could not cope with its reconstruction [...] "
                "Six years later, in 2023, Sebastian Seung's lab at Princeton used convolutional neural networks (CNNs) to automatically segment neurons, while Jan Funke's lab at Janelia used similar techniques to detect pre- and postsynaptic sites. "
                "This automated version was then used as a starting point for a massive community effort among fly neuroscientists to proofread neuronal morphologies by correcting errors and adding information about cell type and other attributes. "
                "This effort, called FlyWire [...] "
                "This full brain connectome (of a female) contains roughly 5x10^7 chemical synapses between ~130,000 neurons. [...] "
                "Comparison of these distinct, adult Drosophila connectomes showed that cell type counts and strong connections were largely stable, but connection weights were surprisingly variable within and across animals. [...] "
                "A natural question is whether the connectome will allow simulation of the fly's behavior. "
                "However, the connectome alone is not sufficient. "
                "A comprehensive simulation would need to include gap junction varieties and locations, identities of neurotransmitters, receptor types and locations, neuromodulators and hormones (with sources and receptors), the role of glial cells",
                nome="Drosophila connectome"),
        ],
    },
    # 8 neurônios-espelho: recusados pela Nature, depois superestimados?
    {
        "temas_secundarios": ["emocoes", "evolucao"],
        "tipos_espanto": ["misterio_aberto", "historia_humana"],
        "gancho": "A Nature recusou o artigo que descreveu os neurônios-espelho por \"falta de interesse geral\". Depois, eles viraram explicação para empatia, linguagem e autismo, e parte dos cientistas vê exagero nessa fama.",
        "explicacao": (
            "Nos anos 1980 e 1990, na Universidade de Parma, na Itália, a equipe de Giacomo Rizzolatti "
            "registrava neurônios isolados no córtex pré-motor de macacos que pegavam pedaços de comida. Alguns "
            "disparavam quando o próprio macaco pegava o alimento e também quando ele via uma pessoa fazer o "
            "mesmo, como se \"espelhassem\" a ação alheia. A Nature rejeitou o achado por \"falta de interesse "
            "geral\", e ele saiu numa revista menos concorrida. Depois, a ideia ganhou o mundo: houve quem ligasse "
            "esses neurônios à empatia, à linguagem e ao autismo, e o neurocientista V. S. Ramachandran os chamou "
            "de \"força motriz\" do grande salto da evolução humana. O problema é que, em humanos, normalmente não "
            "dá para estudar neurônios isolados, e quase toda a evidência é indireta, vinda de exames de imagem. "
            "Em 2009, Greg Hickok listou oito problemas da teoria de que essas células explicam a compreensão das "
            "ações e concluiu que ela nunca foi testada adequadamente em macacos. A tese do \"espelho quebrado\" "
            "no autismo também perdeu força: um grupo achou atividade normal desse sistema em autistas, e hoje "
            "poucos acreditam que uma falha de tudo ou nada nele explique o autismo. Ainda não há um modelo aceito "
            "de como os neurônios-espelho sustentariam funções cognitivas."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Mirror_neuron",
            "A mirror neuron is a neuron that fires both when an animal acts and when the animal observes the same action performed by another. [...] "
            "To date, no widely accepted neural or computational models have been put forward to describe how mirror neuron activity supports cognitive functions. [...] "
            "In the 1980s and 1990s, neurophysiologists Giacomo Rizzolatti, Giuseppe Di Pellegrino, Luciano Fadiga, Leonardo Fogassi, and Vittorio Gallese at the University of Parma placed electrodes in the ventral premotor cortex of the macaque monkey [...] "
            "They found that some neurons responded when the monkey observed a person picking up a piece of food, and also when the monkey itself picked up the food. "
            "The discovery was initially submitted to Nature, but was rejected for its \"lack of general interest\" before being published in a less competitive journal. [...] "
            "It is not normally possible to study single neurons in the human brain, so most evidence for mirror neurons in humans is indirect. [...] "
            "Iacoboni has argued that mirror neurons are the neural basis of the human capacity for emotions such as empathy. [...] "
            "It has also been proposed that problems with the mirror neuron system may underlie cognitive disorders, particularly autism. [...] "
            "Dinstein and colleagues found normal mirror neuron activity in people with autism using fMRI. [...] "
            "Today, very few people believe an all-or-nothing problem with the mirror system can underlie autism. [...] "
            "This has led to suggestions that human language evolved from a gesture performance/understanding system implemented in mirror neurons. [...] "
            "In 2009, Greg Hickok published an extensive argument against the claim that mirror neurons are involved in action-understanding: \"Eight Problems for the Mirror Neuron Theory of Action Understanding in Monkeys and Humans.\" [...] "
            "the proposal has never been adequately tested in monkeys [...] "
            "Heyes rejects the theory advanced by V.S. Ramachandran that mirror neurons have been \"the driving force behind the great leap forward in human evolution.\"",
            nome="Mirror neuron")],
    },
    # 9 o mito dos 10% saiu de um prefácio de autoajuda
    {
        "temas_secundarios": ["aprendizagem_inteligencia", "anatomia"],
        "tipos_espanto": ["origem_inesperada", "mito_desmentido"],
        "gancho": "O mito de que usamos só 10% do cérebro ganhou força com a autoajuda: em 1936, o prefácio de \"Como Fazer Amigos e Influenciar Pessoas\" atribuiu a um psicólogo de Harvard uma porcentagem falsamente precisa.",
        "explicacao": (
            "A origem provável está no psicólogo William James, de Harvard. A partir dos anos 1890, ele dizia em "
            "palestras que as pessoas só alcançam uma fração do seu potencial mental, uma afirmação plausível. A "
            "ideia circulou no movimento de autoajuda dos anos 1920, e o World Almanac de 1929 já dizia que "
            "cientistas e psicólogos garantiam que usamos só uns 10% da capacidade cerebral. Em 1936, o radialista "
            "Lowell Thomas, no prefácio do livro de Dale Carnegie, escreveu que James costumava dizer que o homem "
            "médio desenvolve só 10% de sua capacidade mental latente. A neurociência não deixa espaço para isso. "
            "Quase não há área do cérebro que possa ser lesada sem perda de alguma habilidade, e exames de imagem "
            "mostram todas as regiões com alguma atividade, até durante o sono. O órgão também é caro: corresponde "
            "a cerca de 2% do peso do corpo, mas pode consumir até 20% da energia, mais que qualquer outro. Se a "
            "maior parte dele fosse inútil, cérebros menores e mais eficientes teriam levado vantagem na seleção "
            "natural. E usar tudo de uma vez não seria desejável: atividade descontrolada em todo o cérebro quase "
            "certamente provocaria uma crise epiléptica."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Ten_percent_of_the_brain_myth",
            "A likely origin for the \"10% myth\" is the reserve energy theories of Harvard psychologists William James and Boris Sidis. "
            "In the 1890s, they tested the theory in the accelerated raising of the child prodigy William Sidis. "
            "Thereafter, James told lecture audiences that people only meet a fraction of their full mental potential, which is a plausible claim. "
            "The concept gained currency by circulating within the self-help movement of the 1920s; for example, the 1929 World Almanac states \"There is NO LIMIT to what the human brain can accomplish. "
            "Scientists and psychologists tell us we use only about TEN PERCENT of our brain power.\" [...] "
            "In 1936, American writer and broadcaster Lowell Thomas popularized the idea, in a foreword to Dale Carnegie's How to Win Friends and Influence People, by including the falsely precise percentage: "
            "\"Professor William James of Harvard used to say that the average man develops only ten percent of his latent mental ability\". [...] "
            "Instead, there is almost no area of the brain that can be damaged without loss of abilities. [...] "
            "They reveal that even during sleep, all parts of the brain show some level of activity. [...] "
            "It can require up to 20 percent of the body's energy—more than any other organ—despite making up only 2 percent of the human body weight. "
            "If most of it were unnecessary, there would be a large survival advantage to humans with smaller, more efficient brains. [...] "
            "writes that using all of one's brain would not be desirable either. "
            "Such unfettered activity would almost certainly trigger an epileptic seizure.",
            nome="Ten percent of the brain myth")],
    },
    # 10 o membro fantasma e o rosto que vira mão
    {
        "temas_secundarios": ["sentidos", "percepcao_ilusoes"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Muitos amputados continuam sentindo o membro que perderam. Em alguns, tocar o rosto produz a sensação de toque na mão fantasma: o mapa do corpo no cérebro se reorganiza quando um membro para de mandar sinais.",
        "explicacao": (
            "Entre 50% e 80% das pessoas amputadas sentem um membro fantasma: coceiras, gestos e até dor num braço "
            "ou numa perna que já não existe. O nome foi criado em 1872 pelo médico Silas Weir Mitchell, mas o "
            "cirurgião militar francês Ambroise Paré já descrevia o fenômeno no século XVI. Por muito tempo, a "
            "explicação dominante era a irritação dos nervos no coto. No fim dos anos 1980, Ronald Melzack notou "
            "que isso não podia estar certo, porque muitas pessoas que nasceram sem um membro também sentem um "
            "fantasma. Em 1991, uma equipe dos Institutos Nacionais de Saúde dos EUA mostrou que o córtex "
            "somatossensorial de macacos se reorganiza bastante depois de perder a entrada de sinais. V. S. "
            "Ramachandran propôs que o mesmo valia para humanos e mostrou que tocar diferentes partes do rosto "
            "fazia pacientes sentirem toques em diferentes partes do membro ausente; exames do cérebro de "
            "amputados depois viram essa reorganização. Dele também veio a caixa de espelhos: o membro afetado "
            "fica atrás de um espelho, o paciente vê no lugar dele o reflexo do membro saudável e, ao fazer "
            "movimentos simétricos, tem a ilusão de mexer o fantasma, o que pode ajudar a soltá-lo de posições "
            "dolorosas. A eficácia ainda é debatida: revisões criticam a qualidade de muitos estudos, embora uma "
            "de 2018 tenha concluído que a terapia parece aliviar a dor."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Phantom_limb",
                "with prevalence estimates ranging from 50% to 80% of all individuals who undergo amputation. [...] "
                "People will sometimes feel as if they are gesturing, feel itches, twitch, or even try to pick things up with their non-existing limbs. [...] "
                "The term \"phantom limb\" was coined in 1872 by a physician named Silas Weir Mitchell [...] "
                "One of the first known medical descriptions of the phantom limb phenomenon was written by a French military surgeon, Ambroise Pare, in the sixteenth century. [...] "
                "For many years, the dominant hypothesis for the cause of phantom limbs was irritation in the peripheral nervous system at the amputation site (neuroma). "
                "By the late 1980s, Ronald Melzack had recognized that the peripheral neuroma account could not be correct, because many people born without limbs also experienced phantom limbs. [...] "
                "Pons and colleagues (1991) at the National Institutes of Health (NIH) showed that the primary somatosensory cortex in macaque monkeys undergoes substantial reorganization after the loss of sensory input. "
                "Hearing about these results, V. S. Ramachandran hypothesized that phantom limb sensations in humans could be due to reorganization in the human brain's somatosensory cortex. "
                "Ramachandran and colleagues illustrated this hypothesis by showing that stroking different parts of the face led to perceptions of being touched on different parts of the missing limb. "
                "Later brain scans of amputees showed the same kind of cortical reorganization that Pons had observed in monkeys. [...] "
                "much of the subsequent research has been of poor quality, according to a 2016 review. "
                "A 2018 review, which also criticized the scientific quality of many reports on mirror therapy (MT) [...] "
                "concluded that \"MT seems to be effective in relieving PLP, reducing the intensity and duration of daily pain episodes. [...] "
                "Nevertheless, the debate in the field remains open.",
                nome="Phantom limb"),
            wiki("Mirror_box",
                "It was invented in the 1990s by Vilayanur S. Ramachandran to treat patients whose limb had been amputated and who had phantom limb pain (PLP). "
                "Ramachandran created a visual (and psychological) illusion of two intact limbs by putting the patient's affected limb into a \"mirror box,\" with a mirror down the center (facing toward a patient's intact limb). "
                "The patient then looks into the mirror on the side with the good limb and makes \"mirror symmetric\" movements [...] "
                "Because the subject is seeing the reflected image of the good limb moving, it appears as if the phantom limb is also moving. "
                "Through the use of this artificial visual feedback, it becomes possible for the patient to \"move\" the phantom limb and to unclench it from potentially painful positions.",
                nome="Mirror therapy"),
        ],
    },
    # 11 os taxistas de Londres e o hipocampo
    {
        "temas_secundarios": ["memoria", "cidades"],
        "tipos_espanto": ["conexao_inesperada", "escala_absurda"],
        "gancho": "Para tirar a licença, taxistas de Londres decoram cerca de 25 mil ruas, num estudo que leva de três a quatro anos. Neles, a parte de trás do hipocampo é maior, e tanto mais quanto mais tempo de profissão.",
        "explicacao": (
            "O exame, chamado The Knowledge, é tido como o curso mais exigente do mundo para taxistas. O candidato "
            "precisa dominar 320 rotas-padrão e umas 25 mil ruas num raio de seis milhas a partir de Charing "
            "Cross, no centro de Londres, e passar em pelo menos doze provas orais ao longo do processo, que "
            "costuma levar de três a quatro anos. A neurocientista Eleanor Maguire, da University College London, "
            "estudou o cérebro desses motoristas. O hipocampo, região usada na memória espacial e na navegação, "
            "tinha a parte posterior maior nos taxistas do que na população em geral, e quanto mais tempo de "
            "profissão, maior o aumento. O volume total, porém, não mudava: o ganho na parte de trás vinha com uma "
            "redução relativa na parte da frente. Há também evidências de que o próprio treinamento para o "
            "Knowledge altera de forma mensurável o hipocampo dos aprendizes, o que aponta para o efeito do "
            "estudo, e não só para uma seleção de pessoas de cérebro diferente. Os trabalhos sobre essa "
            "plasticidade do hipocampo interessaram cientistas e ganharam a imprensa no mundo todo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Hippocampus",
                "London's black cab drivers need to learn the locations of a large number of places and the fastest routes between them in order to pass a strict test known as The Knowledge in order to gain a license to operate. "
                "A study showed that the posterior part of the hippocampus is larger in these drivers than in the general public, and that a positive correlation exists between the length of time served as a driver and the increase in the volume of this part. "
                "It was also found the total volume of the hippocampus was unchanged, as the increase seen in the posterior part was made at the expense of the anterior part, which showed a relative decrease in size.",
                nome="Hippocampus"),
            wiki("The_Knowledge",
                "It is the world's most demanding training course for taxi drivers, and applicants will usually need to pass at least twelve \"appearances\" (periodical one-on-one oral examinations undertaken throughout the qualification process), with the whole process typically taking three to four years to pass. [...] "
                "Three hundred and twenty standard routes through central London, or \"runs\", are defined in the Guide to Learning the Knowledge of London [...] "
                "some 25,000 streets within a six-mile radius of Charing Cross are [...] "
                "There is evidence that training for the Knowledge can measurably alter the hippocampus of trainee cab drivers. "
                "The hippocampus is the area of the brain used for spatial memory and navigation, and is generally larger in taxi drivers than in the general population.",
                nome="The Knowledge"),
            wiki("Eleanor_Maguire",
                "Perhaps the most famous of these is her series of studies on London taxi drivers, where she documented changes in hippocampal structure associated with acquiring the knowledge of London's layout. [...] "
                "This work on hippocampal plasticity not only interested scientists, but also engaged the public and media world-wide.",
                nome="Eleanor Maguire"),
        ],
    },
    # 12 viver com metade do cérebro
    {
        "temas_secundarios": ["historia_medicina", "anatomia"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Em epilepsias graves que não cedem a remédios, cirurgiões chegam a remover ou desligar metade do cérebro. Muitos pacientes ficam livres das crises e conservam a fala, a leitura e a capacidade de andar.",
        "explicacao": (
            "A cirurgia se chama hemisferectomia. A primeira remoção de um hemisfério inteiro foi descrita em 1928 "
            "pelo neurocirurgião americano Walter Dandy, contra um tumor; a primeira conhecida para tratar "
            "epilepsia foi feita em 1938 pelo canadense Kenneth McKenzie. Hoje se prefere, na maioria dos centros, "
            "desconectar o hemisfério doente em vez de retirá-lo, com menos complicações. Segundo os estudos, de "
            "54% a 90% dos pacientes ficam totalmente livres das crises. A maioria não tem mudanças cognitivas, "
            "muitos andam sem ajuda, e a maior parte tem linguagem e leitura satisfatórias. Há perdas: quase "
            "todos perdem a metade do campo visual oposta ao lado operado, e pode haver déficits motores. Em 2019, "
            "neurocientistas do Caltech examinaram por ressonância seis adultos operados na infância, todos com "
            "capacidade cognitiva relativamente normal, e acharam no hemisfério restante as mesmas grandes redes "
            "cerebrais de um cérebro com dois hemisférios, com mais conexões entre elas do que o normal, como se "
            "colaborassem mais. Os resultados de longo prazo variam bastante: a Liga Internacional contra a "
            "Epilepsia registra que cerca de um quinto dos pacientes tem trabalho remunerado, e menos ainda vive de "
            "forma independente."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Hemispherectomy",
                "Hemispherectomy is a surgery that is performed by a neurosurgeon where an unhealthy hemisphere of the brain is disconnected or removed. [...] "
                "This surgery is mostly used as a treatment for medically intractable epilepsy, which is the term used when anti-seizure medications are unable to control seizures. [...] "
                "The first anatomical hemispherectomy was performed and described in 1928 by American neurosurgeon Walter Dandy. "
                "This was done as an attempt to treat glioma, a brain tumor, and hemiplegia. "
                "The first known anatomical hemispherectomy performed as a treatment for intractable epilepsy was in 1938 by Kenneth McKenzie, a Canadian neurosurgeon. [...] "
                "This approach is preferred in most modern centers because of its lower complication rates [...] "
                "Most patients do not experience changes in cognition, but some individuals may be at risk. "
                "A visual deficit called contralateral homonymous hemianopsia is expected to occur in most patients, where the entire visual field contralateral to the removed hemisphere is lost. "
                "There is a risk of motor deficits, and this is variable. [...] "
                "some obtaining complete seizure freedom (54–90%) [...] "
                "In terms of postoperative motor function, some patients may have improvement or no change of their weaker extremity, and many can walk independently. "
                "Most patients postoperatively have minimal to no behavioral problems, satisfactory language skills, good reading capability, and only a minority of patients have a decline in IQ. [...] "
                "The International League Against Epilepsy (ILAE) reports that \"about one-fifth of hemispherectomy patients are gainfully employed and even fewer live independently.\"",
                nome="Hemispherectomy"),
            fonte("https://www.caltech.edu/about/news/patients-missing-one-brain-hemisphere-show-surprisingly-intact-neural-connections",
                "Patients Missing One Brain Hemisphere Show Surprisingly Intact Neural Connections (Caltech)",
                "In the most extreme cases of epilepsy, when a patient's seizures are relentless and do not respond to other treatments, doctors may perform a surgery called a hemispherectomy to remove half of the patient's brain. "
                "Remarkably, many of these patients are cured of their seizures and possess basic motor, language, and cognitive skills. [...] "
                "neuroscientists at Caltech describe an investigation of six of these rare patients [...] "
                "The research team performed magnetic resonance imaging (MRI) scans on the patients, all of whom received the surgeries as children and now have relatively normal cognitive abilities. [...] "
                "\"Despite missing an entire brain hemisphere, we found all the same major brain networks that you find in healthy brains with two hemispheres,\" says Dorit Kliemann [...] "
                "The brain scans also revealed an increased number of connections between the brain networks in the patients compared to healthy individuals. [...] "
                "\"It appears that the networks are collaborating more,\" says Kliemann. [...] November 19, 2019"),
        ],
    },
    # 13 a maioria dos neurônios mora no cerebelo
    {
        "temas_secundarios": ["anatomia", "ciencia_esporte"],
        "tipos_espanto": ["contraintuitivo", "mito_desmentido"],
        "gancho": "A maior parte dos neurônios do cérebro não está no córtex, a camada enrugada associada ao pensamento, mas no cerebelo: ele ocupa só 10% do volume e tem mais neurônios do que todo o resto junto.",
        "explicacao": (
            "O segredo são as células granulares do cerebelo, que estão entre os menores neurônios do cérebro e "
            "são os mais numerosos: as estimativas giram em torno de 50 bilhões, cerca de três quartos de todos "
            "os neurônios do cérebro. Pelas contagens mais citadas, o cerebelo tem uns 69 bilhões de neurônios, "
            "contra cerca de 16 bilhões no córtex cerebral. A proporção, de cerca de 3,6 neurônios no cerebelo "
            "para cada um no neocórtex, se repete em muitas espécies de mamíferos. As contagens derrubaram ainda "
            "outra crença antiga: a de que as células da glia, que sustentam e nutrem os neurônios, seriam dez "
            "vezes mais numerosas que eles. Métodos mais novos e a reanálise de dados históricos indicam uma "
            "proporção geral menor que um para um, com cerca de 85 bilhões de células da glia no cérebro humano, "
            "mais ou menos o mesmo número de neurônios. A proporção muda muito de lugar para lugar: no córtex "
            "cerebral há cerca de 3,7 células da glia por neurônio; no cerebelo, só 0,23."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Cerebellum",
                "Because of its large number of tiny granule cells, the cerebellum contains more neurons than the total from the rest of the brain, but takes up only 10% of the total brain volume. [...] "
                "There are about 3.6 times as many neurons in the cerebellum as in the neocortex, a ratio that is conserved across many different mammalian species. [...] "
                "Cerebellar granule cells, in contrast to Purkinje cells, are among the smallest neurons in the brain. "
                "They are also the most numerous neurons in the brain: In humans, estimates of their total number average around 50 billion, which means that about 3/4 of the brain's neurons are cerebellar granule cells.",
                nome="Cerebellum"),
            wiki("Glia",
                "While glia were thought to outnumber neurons by a ratio of 10:1, studies using newer methods and reappraisal of historical quantitative evidence suggests an overall ratio of less than 1:1, with substantial variation between different brain tissues. [...] "
                "There are approximately 85 billion glial cells in the human brain, about the same number as neurons. [...] "
                "The glia to neuron-ratio in the cerebral cortex is 3.72 (60.84 billion glia (72%); 16.34 billion neurons), while that of the cerebellum is only 0.23 (16.04 billion glia; 69.03 billion neurons).",
                nome="Glia"),
        ],
    },
    # 14 o experimento que veio num sonho
    {
        "temas_secundarios": ["sono_ritmos", "historia_medicina"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Otto Loewi sonhou com o experimento que provaria que os nervos se comunicam por química, anotou-o de madrugada e de manhã não entendeu a própria letra. Segundo ele, o sonho voltou na noite seguinte.",
        "explicacao": (
            "No começo do século XX, a dúvida dividia os maiores cientistas: as células nervosas passariam o sinal "
            "adiante por eletricidade ou por substâncias químicas? Segundo o relato do próprio Loewi, no sábado de "
            "Páscoa de 1921 ele sonhou com um experimento que resolveria a questão, rabiscou a ideia num papel no "
            "criado-mudo e voltou a dormir. De manhã, não conseguiu ler o que tinha escrito; aquele, disse ele, "
            "foi o dia mais longo da sua vida. Na noite seguinte o sonho se repetiu, e dessa vez ele foi direto ao "
            "laboratório. Pegou dois corações de rã batendo em solução salina, um deles ainda ligado ao nervo "
            "vago. Ao estimular o nervo com eletricidade, o primeiro coração desacelerou. Loewi passou então um "
            "pouco do líquido que banhava esse coração para o segundo, que também desacelerou: alguma substância "
            "solúvel liberada pelo nervo controlava os batimentos. Ele a chamou de Vagusstoff, \"substância do "
            "vago\"; mais tarde se viu que era a acetilcolina. O Nobel veio em 1936, dividido com o amigo Henry "
            "Dale. Em 1938, na noite da invasão alemã da Áustria, Loewi foi preso pelos nazistas e só foi solto "
            "três meses depois, com a condição de entregar todos os seus bens, inclusive sua pesquisa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Otto_Loewi",
            "For this discovery, he was awarded the Nobel Prize in Physiology or Medicine in 1936, which he shared with Sir Henry Dale, who was a lifelong friend that helped to inspire the neurotransmitter experiment. [...] "
            "In the early 20th century the controversy of whether cells used chemical or electrical transmission divided even the most prominent scientists. [...] "
            "He dissected out of frogs two beating hearts: one with the vagus nerve which controls heart rate attached, the other heart on its own. "
            "Both hearts were bathed in a saline solution (i.e. Ringer's solution). "
            "By electrically stimulating the vagus nerve, Loewi made the first heart beat slower. "
            "Then, Loewi took some of the liquid bathing the first heart and applied it to the second heart. "
            "The application of the liquid made the second heart also beat slower, proving that some soluble chemical released by the vagus nerve was controlling the heart rate. "
            "He called the unknown chemical Vagusstoff, naming it after the nerve and the German word for substance. "
            "It was later found that this chemical corresponded to acetylcholine. [...] "
            "After being arrested, along with two of his sons, on the night of the German invasion of Austria, March 11, 1938, Loewi was released after three months on condition that he \"voluntarily\" relinquish all his possessions, including his research, to the Nazis. [...] "
            "On Easter Saturday 1921, he dreamed of an experiment that would prove once and for all that transmission of nerve impulses was chemical, not electrical. "
            "He woke up, scribbled the experiment onto a scrap of paper on his night-stand, and went back to sleep. "
            "The next morning, he found, to his horror, that he couldn't read his midnight scribbles. "
            "That day, he said, was the longest day of his life, as he could not remember his dream. "
            "That night, however, he had the same dream. "
            "This time, he immediately went to his lab to perform the experiment.",
            nome="Otto Loewi")],
    },
]
