LOTE = "2026-11-19-doencas_infecciosas-01"
AREA = "corpo_medicina"
TEMA = "doencas_infecciosas"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 a alavanca da bomba de Broad Street não acabou com o surto
    {
        "temas_secundarios": ["historia_medicina", "probabilidade"],
        "tipos_espanto": ["mito_desmentido", "engenhosidade"],
        "gancho": "A retirada da alavanca da bomba de Broad Street virou lenda como o gesto que acabou com um surto de cólera em Londres, em 1854. Mas, segundo o próprio John Snow, os casos já vinham caindo.",
        "explicacao": (
            "Em 31 de agosto de 1854, a cólera explodiu no Soho, em Londres: em três dias morreram 127 pessoas, e "
            "no fim do surto eram 420. Muitos médicos achavam que a doença vinha de um \"miasma\", um ar ruim. O "
            "médico John Snow conversou com os moradores, com a ajuda do reverendo Henry Whitehead, e apontou como "
            "fonte a bomba pública de água de Broad Street. As autoridades da paróquia mandaram tirar a alavanca. A "
            "cena ficou famosa, mas o próprio Snow escreveu que os casos já tinham diminuído antes disso, em parte "
            "porque muita gente tinha fugido do bairro. Uma anomalia reforçava a pista: nenhum funcionário da "
            "cervejaria da rua adoeceu. Eles recebiam uma cota diária de cerveja e não bebiam a água do poço, e a "
            "fabricação da cerveja inclui uma fervura. O argumento mais forte de Snow, porém, veio de um "
            "\"experimento natural\". Duas companhias abasteciam a cidade, muitas vezes casas vizinhas: uma tirava "
            "água de trechos do Tâmisa poluídos por esgoto, a outra captava mais acima no rio. Nas casas atendidas "
            "pela primeira, a mortalidade por cólera era 14 vezes maior. Passado o surto, as autoridades "
            "recolocaram a alavanca e rejeitaram a teoria dele."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("1854_Broad_Street_cholera_outbreak",
            "The outbreak (also known as Golden Square outbreak), which killed 420 people, is best known for the physician John Snow's study of its causes and his hypothesis that germ-contaminated water was the cause, rather than something in the air called \"miasma\". [...] "
            "On 31 August 1854, after several other outbreaks elsewhere in the city, there was a major outbreak of cholera in Soho. [...] "
            "Over the next three days, 127 people on or near Broad Street died. [...] "
            "By talking to local residents (with the help of Reverend Henry Whitehead), Snow identified the outbreak's source as the public water pump on Broad Street [...] "
            "persuaded the St James parish authorities to disable the pump by removing its handle. "
            "Although this action has been popularly reported as ending the outbreak, the epidemic may have already been in rapid decline, as explained by Snow: [...] "
            "There is no doubt that the mortality was much diminished, as I said before, by the flight of the population, which commenced soon after the outbreak; but the attacks had so far diminished before the use of the water was stopped [...] "
            "Snow also performed a statistical comparison between the Southwark and Vauxhall Waterworks Company and a waterworks at Seething Wells (owned by the Lambeth Waterworks Company) that was further upriver and hence had cleaner water; he showed that houses supplied by the former had a cholera mortality rate 14 times that of those supplied by the latter. [...] "
            "There was one significant anomaly: none of the workers in the nearby Broad Street brewery contracted cholera. As they were given a daily allowance of beer, they did not consume water from the nearby well. During the brewing process, the wort (un-fermented beer) is boiled in part so that hops can be added. [...] "
            "Snow showed that the Southwark and Vauxhall Waterworks Company was taking water from sewage-polluted sections of the Thames [...] "
            "After the cholera epidemic subsided, government officials replaced the Broad Street pump handle. They had responded only to the urgent threat posed to the population, and afterwards they rejected Snow's theory. [...] "
            "what is now known as a double-blind experiment fell right into his lap. [...] "
            "In many cases a single house has a supply different from that on either side.",
            nome="1854 Broad Street cholera outbreak")],
    },
    # 2 Semmelweis e as grávidas que preferiam parir na rua
    {
        "temas_secundarios": ["historia_medicina", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Na Viena do século XIX, grávidas fingiam ter dado à luz a caminho do hospital para escapar de uma das maternidades. Tinham razão: os médicos de lá iam das autópsias direto para os partos.",
        "explicacao": (
            "O Hospital Geral de Viena tinha duas maternidades. Na Primeira Clínica, onde atuavam médicos e "
            "estudantes, a mortalidade média por febre puerperal, uma infecção depois do parto, rondava 10%. Na "
            "Segunda, onde se formavam parteiras, ficava abaixo de 4%. As mulheres imploravam para não ir para a "
            "primeira, e algumas davam à luz na rua e diziam que o parto tinha acontecido no caminho. O médico "
            "húngaro Ignaz Semmelweis estranhou que essas mulheres quase não tivessem a febre. A pista decisiva veio "
            "em 1847: um amigo dele morreu depois de se ferir com o bisturi de um estudante numa autópsia, com "
            "sinais parecidos com os das mães. Semmelweis concluiu que médicos e estudantes levavam nas mãos "
            "\"partículas cadavéricas\" da sala de autópsia até as pacientes, e passou a exigir que lavassem as mãos "
            "numa solução clorada. A mortalidade, que era de 18,3% em abril, caiu para 2,2% em junho e 1,2% em julho. "
            "Mesmo assim, a ideia foi ignorada ou ridicularizada, e alguns médicos se ofenderam com a sugestão de "
            "que mãos de cavalheiros pudessem estar sujas. Em 1865, ele foi internado num asilo e morreu duas "
            "semanas depois, de uma ferida infeccionada na mão, possivelmente causada por um espancamento dos "
            "guardas. Só com a teoria dos germes, anos depois, suas observações ganharam explicação."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Ignaz_Semmelweis",
            "There were two maternity clinics at the Viennese hospital. The First Clinic had an average maternal mortality rate of about 10% due to puerperal fever. The Second Clinic's rate averaged less than 4%. Women begged to be admitted to the Second Clinic, due to the reputation of the First Clinic. [...] "
            "Women began purposefully giving birth in the streets, pretending to have given birth en route to the hospital so they could avoid being admitted to the clinic where the risk of infection, birth complications and death were substantially higher. "
            "Semmelweis was puzzled that puerperal fever was rare among women giving street births [...] "
            "Semmelweis' breakthrough occurred in 1847, following the death of his good friend Jakob Kolletschka, who had been accidentally poked with a student's scalpel while performing a post mortem examination. Kolletschka's autopsy showed a pathology similar to that of the women who were dying from puerperal fever. [...] "
            "He proposed that he and the medical students carried \"cadaverous particles\" on their hands from the autopsy room to the patients they examined in the First Obstetrical Clinic. This explained why the student midwives in the Second Clinic, who were not engaged in autopsies and had no contact with corpses, saw a much lower mortality rate. [...] "
            "He instituted a policy of using a solution of chlorinated lime (calcium hypochlorite) for washing hands between autopsy work and the examination of patients. [...] "
            "The mortality rate in April 1847, before the new hand washing procedures were instituted, was 18.3%. The new procedures started in mid-May leading to lower rates:  June 2.2%, July 1.2%, and August 1.9%. [...] "
            "Semmelweis's hypothesis, that there was only one cause, that the primary factor was cleanliness, was extreme at the time and was largely ignored, rejected, or ridiculed. [...] "
            "Some doctors, for instance, were offended at the suggestion that they should wash their hands, feeling that their social status as gentlemen was inconsistent with the idea that their hands could be unclean. [...] "
            "He died after two weeks, on 13 August 1865, aged 47, from a gangrenous wound, due to an infection on his right hand which might have been caused by the struggle. [...] "
            "In the asylum, he was beaten by the guards. He died 14 days later from a gangrenous wound on his right hand that may have been caused by the beating. "
            "Semmelweis's findings only gained widespread acceptance years after his death, when Louis Pasteur confirmed the germ theory of disease, giving Semmelweis's observations a scientific explanation",
            nome="Ignaz Semmelweis")],
    },
    # 3 Mary Mallon, a "Maria Tifoide"
    {
        "temas_secundarios": ["historia_medicina", "leis_julgamentos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Mary Mallon, a \"Maria Tifoide\", se sentia saudável, mas espalhou febre tifoide como cozinheira em Nova York. Foi confinada numa ilha de 1915 até morrer, em 1938. Outros portadores tiveram tratamento mais brando.",
        "explicacao": (
            "Imigrante irlandesa, Mallon cozinhava para famílias ricas de Nova York. Em 1906, depois de um surto de "
            "febre tifoide numa casa de veraneio em Oyster Bay, o dono do imóvel contratou George Soper, engenheiro sanitário "
            "e epidemiologista, para achar a causa. Soper viu que ela tinha trabalhado para oito famílias, sete delas "
            "com casos da doença. Como cozinhar mata a bactéria, ele estranhou, até saber que ela servia um sorvete "
            "com pêssegos frescos. Soper conhecia a ideia de portadores assintomáticos, gente infectada sem nenhum "
            "sinal da doença. Mallon, que não acreditava estar infectada, o recebeu empunhando um garfo de trinchar, "
            "e depois resistiu à polícia. Os exames acharam o bacilo nas fezes dela, e em 1907 ela foi levada a um "
            "hospital de isolamento na ilha North Brother. Solta em 1910, com a promessa de não trabalhar mais como "
            "cozinheira, foi contratada em 1914, com o nome de Mary Brown, por uma maternidade, que no início de 1915 "
            "teve um surto com 25 casos e duas mortes. Ela voltou à ilha e lá ficou até morrer. O caso ainda levanta "
            "questões éticas: durante o confinamento dela, foram identificados outros 400 portadores sem sintomas, e "
            "nenhum ficou isolado por tanto tempo; alguns, que trabalhavam com comida, ganharam emprego e aluguel "
            "pagos pelo Estado."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Mary_Mallon",
            "was an Irish-born cook who lived in the United States from a young age and is believed to have infected up to fifty-seven people with the bacteria that cause typhoid fever. [...] "
            "She was the first person in the U.S. to be identified as an asymptomatic carrier of Salmonella typhi bacteria. [...] "
            "In 1907, she was forcibly quarantined at the Riverside Hospital, an institution for those with quarantinable diseases, on North Brother Island in New York City's East River. She was released in 1910 after she swore to report to the health department every quarter and not return to cooking as a career. "
            "A further typhoid outbreak at the Sloane Maternity Hospital in early 1915 resulted in twenty-five cases and two deaths. Mallon was identified as the responsible party and was returned to North Brother Island. She remained there until her death in 1938. [...] "
            "Mallon's case raises ethical questions about the balance between protection of individual liberty and the requirements of public health. She was treated differently from the four hundred other asymptomatic typhoid carriers identified during her confinement. Others who worked in the food industry were given jobs and had their rents paid for by the state, and none were confined for the same length of time as she was. [...] "
            "Mallon was soon employed as a private cook with a series of wealthy New York families [...] "
            "Mallon worked as a cook for Charles Henry Warren, a New York banker in 1906. He and his family spent the summer that year at Oyster Bay on the North Shore of Long Island, where they had rented a house from George Thompson. [...] "
            "he hired George Soper, a sanitation engineer and epidemiologist for the New York Department of Health, to investigate the source of the problem. [...] "
            "At first, he was unsure whether a cook could be the source, since cooking would kill the bacteria; he became more convinced, however, when he learned that Mallon prepared an ice cream dessert with fresh peaches. [...] "
            "He saw she had worked for eight families, seven of whom had suffered typhoid outbreaks. [...] "
            "Soper was aware of the existence of asymptomatic carriers—carriers that are infected with a pathogen, but show no signs or symptoms [...] "
            "It did not take Mary long to react to this suggestion. She seized a carving fork and advanced in my direction. [...] "
            "Mallon's refusal was based on her belief that she was not infected. [...] "
            "Her stools were tested three times a week and showed the presence of Bacillus typhosus. [...] "
            "the earliest confirmed instance of Mallon being employed as a cook after her release from North Brother Island was in October 1914, when she was hired under the name Mary Brown by the Sloane Maternity Hospital.",
            nome="Mary Mallon")],
    },
    # 4 Finlay, o mosquito e Jesse Lazear
    {
        "temas_secundarios": ["insetos", "historia_medicina"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 1881, um médico cubano propôs que a febre amarela era transmitida por mosquitos e foi alvo de zombaria. Em 1900, a ideia foi confirmada, e um dos pesquisadores morreu depois de se deixar picar.",
        "explicacao": (
            "Carlos Finlay, nascido em Cuba em 1833, defendeu na Conferência Sanitária Internacional de 1881 que um "
            "mosquito que picasse um doente de febre amarela poderia, depois, infectar uma pessoa sadia. A ideia foi "
            "mal recebida e motivo de deboche. No ano seguinte, ele apontou um mosquito do gênero Aedes como o "
            "transmissor e recomendou controlar a população do inseto. Quase vinte anos depois, em 1900, a Comissão "
            "Walter Reed, do Exército americano, confirmou a hipótese. Um de seus membros, o médico Jesse Lazear, era "
            "o único com experiência com mosquitos e usou larvas do laboratório de Finlay. Ele deixou de propósito "
            "que um mosquito infectado o picasse, para estudar a doença. Adoeceu e morreu aos 34 anos, dezessete dias "
            "depois de escrever à mulher que achava estar na pista do \"germe verdadeiro\". Na época, a versão "
            "divulgada foi a de que ele tinha confundido o mosquito com um inofensivo; o caráter deliberado só veio "
            "à tona em 1947, no caderno do próprio Lazear. Reed deu a Finlay o crédito pela descoberta do "
            "transmissor. O cubano foi indicado sete vezes ao Nobel de Medicina e nunca ganhou."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Carlos_Finlay",
                "Carlos Juan Finlay (December 3, 1833 – August 20, 1915) was a Cuban epidemiologist [...] "
                "He was the first to theorize, in 1881, that a mosquito was a carrier, now known as a disease vector, of the organism causing yellow fever: a mosquito that bites a victim of the disease could subsequently bite and thereby infect a healthy person. "
                "He presented this theory at the 1881 International Sanitary Conference, where it was not well-received, and in fact made him subject to ridicule and mockery.  A year later Finlay identified a mosquito of the genus Aedes as the organism transmitting yellow fever. His theory was followed by the recommendation to control the mosquito population as a way to control the spread of the disease. "
                "His hypothesis and exhaustive proofs were confirmed nearly twenty years later by the Walter Reed Commission of 1900. [...] "
                "Reed himself credited Finlay with the discovery of the yellow fever vector [...] "
                "Finlay was nominated seven times for the Nobel Prize in Physiology or Medicine, although he was never awarded the prize.",
                nome="Carlos Finlay"),
            wiki("Jesse_William_Lazear",
                "In 1900 he reported for duty as the assistant surgeon at Columbia Barracks (Quemados, Cuba) for the United States Army. [...] "
                "Lazear was the only member of the commission who had experience working with mosquitoes, and he used mosquito larvae from Finlay's laboratory. He wrote to his wife in a letter dated September 8, 1900, \"I rather think I am on the track of the real germ.\" Lazear deliberately allowed an infected mosquito to bite him in order to study the disease. He contracted the disease and died at age 34, seventeen days after writing his hopeful letter. The fact that this was a deliberate act was covered up at the time—for reasons unknown, but possibly connected with family insurance policies—and the story put about that Lazear had mistaken the mosquito for an uninfected one of a different species. The truth was discovered in 1947 by Philip S. Hench from Lazear's own notebook.",
                nome="Jesse William Lazear"),
        ],
    },
    # 5 Canal do Panamá: o médico "obcecado" por mosquitos
    {
        "temas_secundarios": ["grandes_obras", "insetos", "imperios_coloniais"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Na obra do Canal do Panamá, o chefe da comissão pediu a Theodore Roosevelt que afastasse o médico com uma \"obsessão cara\" por mosquitos. Roosevelt manteve o médico, e a febre amarela quase sumiu da zona do canal.",
        "explicacao": (
            "Quando os EUA assumiram o projeto, em 1904, o istmo do Panamá era famoso pelas doenças tropicais: "
            "estima-se que mais de 22 mil trabalhadores tinham morrido durante a tentativa francesa de abrir o canal. "
            "Por muito tempo se acreditou que a febre amarela vinha da sujeira e a malária de vapores nocivos, mas "
            "pesquisas feitas entre 1897 e 1902 mostraram que as duas eram espalhadas por mosquitos. O coronel "
            "William Gorgas, chefe de saneamento, montou uma guerra contra eles: inspetores procuravam larvas de "
            "casa em casa, a água parada era eliminada ou coberta com óleo, pântanos foram drenados e todos os "
            "prédios foram fumigados. A \"teoria do mosquito\" ainda era vista como controversa, e o custo era alto. "
            "Theodore Shonts, chefe da comissão do canal, pediu a Roosevelt que tirasse Gorgas do projeto. O "
            "presidente consultou dois médicos de renome e ouviu que teria o canal se ficasse com Gorgas. Deu a ele "
            "apoio total. Em 1906, houve um único caso de febre amarela, e as mortes por malária também caíram "
            "muito. A proteção, porém, foi desigual: os trabalhadores negros, a maioria da mão de obra, muitas vezes "
            "moravam fora da área controlada e, em 1906, morreram dez vezes mais que os brancos. No total, morreram "
            "350 trabalhadores brancos e 4.500 negros, bem menos que na época francesa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Health_measures_during_the_construction_of_the_Panama_Canal",
            "By the time the United States took control of the Panama Canal project on May 4, 1904, the Isthmus of Panama was notorious for tropical diseases. An estimated 12,000 workers had died during the construction of the Panama Railway and over 22,000 during the French effort to build a canal. [...] "
            "Traditionally, yellow fever had been thought to be caused by contact with filth and malaria by noxious vapors. However, between 1897 and 1902, both diseases were shown to be spread by mosquitoes [...] "
            "The Panama Canal Commission appointed Colonel William Crawford Gorgas in March 1904 as head of hospitals and sanitation. [...] "
            "There was initially considerable resistance to this program, as the \"mosquito theory\" was still considered controversial and unproven. [...] "
            "In each district, inspectors searched houses and buildings for mosquito larvae. [...] "
            "by eliminating standing water where possible and by spreading oil on the surface of any remaining pools, the larvae could be destroyed. [...] "
            "Gorgas organized a major program to drain and fill swamps and wetlands around the Canal Zone. [...] "
            "Within a year of Stevens's appointment, every building in Panama had been fumigated [...] "
            "In 1906, only one case of yellow fever was reported, and by the end of the Panama Canal's construction, there were zero every year. [...] "
            "Gorgas continuously faced opposition because of the cost- and manpower-intensive nature of the eradication work, as well as entrenched ideas that mosquitoes were irrelevant to disease spread. At one stage, Theodore P. Shonts, head of the commission responsible for the canal, requested U.S. President Theodore Roosevelt to remove Gorgas from the project because of his costly obsession with mosquitoes. Roosevelt asked advice from two leading physicians in the U.S. He was told that he had a choice between Shonts and Gorgas, and that he would get his canal if he supported Gorgas. Thereafter, Roosevelt gave Gorgas his full backing. "
            "In the end, these efforts were a success: by 1906, yellow fever was virtually wiped out in the Canal Zone, and the number of deaths caused by the other tropical disease, malaria, was also reduced significantly. [...] "
            "While disease reduction dramatically improved the health of white workers, black workers—the majority of the canal workforce—continued to die in large numbers, at ten times the rate of white workers in 1906. While medical care was provided to all, housing was not provided to workers, many of whom had to live in tents and tenements outside the mosquito-controlled zone. In the end, 350 white workers and 4,500 black workers had died. While the loss was tragic, it was far less than during the French era.",
            nome="Health measures during the construction of the Panama Canal")],
    },
    # 6 verme-da-guiné: quase erradicado sem vacina nem remédio
    {
        "temas_secundarios": ["microbiologia", "agua_doce_gelo"],
        "tipos_espanto": ["engenhosidade", "escala_absurda"],
        "gancho": "Em 1986, o verme-da-guiné infectava cerca de 3,5 milhões de pessoas por ano. Em 2025, foram 10 casos. E a doença está quase erradicada sem vacina nem remédio: com filtros de pano para a água e educação.",
        "explicacao": (
            "A dracunculíase é causada por um verme que entra no corpo quando a pessoa bebe água com pequenos "
            "crustáceos, os copépodes, que carregam as larvas. Cerca de um ano depois, a fêmea adulta chega a um "
            "ponto de saída, em geral na perna, e forma uma bolha muito dolorosa. O verme sai pela ferida aos "
            "poucos, ao longo de semanas. Para aliviar a dor, o doente mergulha a perna na água, e é aí que o verme "
            "libera novas larvas, fechando o ciclo. Não existe medicamento para tratar nem para prevenir a doença: o "
            "tratamento ainda é enrolar o verme num pauzinho, alguns centímetros por dia. A campanha de erradicação "
            "começou nos anos 1980, depois do sucesso contra a varíola, e se apoia em medidas simples: filtros de "
            "náilon ou de pano fino que retêm os copépodes, educação de aldeia em aldeia para ninguém mergulhar "
            "feridas em fontes de água de beber e vigilância de cada caso. Os casos humanos caíram de cerca de 3,5 "
            "milhões por ano em 1986 para 10 em 2025, sobretudo no Chade, na Etiópia e no Sudão do Sul. Um obstáculo "
            "inesperado são os cães, que também se infectam e ajudaram a reacender a transmissão no Chade em 2010. "
            "Se a campanha der certo, esta será a segunda doença humana erradicada, depois da varíola."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Dracunculiasis",
            "A person becomes infected by drinking water contaminated with larvae that reside inside copepods (a type of small crustacean). [...] "
            "Around a year later, the adult female worm migrates to an exit site — usually the lower leg — and induces an intensely painful blister on the skin. Eventually, the blister bursts, creating a painful wound from which the worm gradually emerges over several weeks. [...] "
            "The female worm releases larvae when the host submerges the wound in water in attempts to relieve the pain, thus continuing the life cycle. "
            "There is no medication to treat or prevent dracunculiasis. Instead, the mainstay of treatment is the careful wrapping of the emerging worm around a small stick or gauz to encourage and speed up its exit. Each day, a few more centimeters of the worm emerge [...] "
            "Prevention efforts center on filtering drinking water to remove copepods as well as public education campaigns to discourage people from soaking affected limbs in sources of drinking water [...] "
            "The effort to eradicate dracunculiasis began in the 1980s following the successful eradication of smallpox in 1977. [...] "
            "Dracunculiasis has become rare, with 10–15 human cases reported worldwide per year (15 in 2021, 13 in 2022, 14 in 2023, 15 in 2024, and 10 in 2025). This is down from 27 cases in 2020 and dramatically less than the estimated 3.5 million annual cases in 20 countries in 1986 [...] "
            "Dracunculiasis remains endemic primarily in three countries –  Chad, Ethiopia and South Sudan. [...] "
            "Nylon filters, finely woven cloth, or specialized filter straws can all remove copepods from drinking water, eliminating transmission risk. [...] "
            "The second phase involved the training and distribution of staff and volunteers to provide public education village-by-village, surveil for cases, and deliver water filters. [...] "
            "Infections of domestic dogs have been particularly common in Chad, where they helped reignite dracunculiasis transmission in 2010. [...] "
            "If the eradication program succeeds, dracunculiasis is expected to become the second human disease to be eradicated, after smallpox.",
            nome="Dracunculiasis")],
    },
    # 7 peste bovina: a segunda doença erradicada
    {
        "temas_secundarios": ["ecologia", "imperios_coloniais", "domesticacao"],
        "tipos_espanto": ["conexao_inesperada", "escala_absurda"],
        "gancho": "A segunda doença erradicada pela humanidade não atacava pessoas: era a peste bovina, extinta em 2011. Nos anos 1890, ela matou até 90% do gado do leste e do sul da África, e a fome pode ter levado um terço da Etiópia.",
        "explicacao": (
            "A peste bovina, ou rinderpest (\"peste do gado\", em alemão), era causada por um vírus que atacava o "
            "gado, parente mais próximo do vírus do sarampo. No fim do século XIX, uma epidemia varreu a África e, "
            "segundo as estimativas, matou de 80% a 90% de todo o gado do leste e do sul do continente. Para povos "
            "que dependiam do pastoreio, da caça e da agricultura, o resultado foi fome em massa. Estima-se que as "
            "mortes humanas chegaram a um terço da população da Etiópia e a dois terços do povo massai da Tanzânia. "
            "O despovoamento teve um efeito em cadeia na paisagem: arbustos espinhosos tomaram as terras, criando "
            "o hábitat ideal para a mosca tsé-tsé, que transmite a doença do sono e torna a região imprópria para "
            "o gado. Depois de uma campanha mundial iniciada em meados do século XX, o último caso confirmado foi "
            "diagnosticado em 2001. Em 2010, a FAO, agência da ONU para alimentação e agricultura, anunciou o fim "
            "dos trabalhos de campo, e em junho de 2011 a erradicação global foi declarada oficialmente. Foi só a "
            "segunda doença da história a ser eliminada por completo, depois da varíola."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Rinderpest",
            "The term Rinderpest (German: [ˈʁɪndɐpɛst] ) is a German word meaning \"cattle plague\". Rinderpest virus (RPV) belongs to the genus Morbillivirus, alongside measles virus – its closest relative – and canine distemper virus. [...] "
            "After a global eradication campaign that began in the mid-20th century, the last confirmed case of rinderpest was diagnosed in 2001. In 2010, the United Nations Food and Agriculture Organization (FAO) announced that field activities in the decades-long, worldwide campaign to eradicate the disease were ending, paving the way for a formal declaration in June 2011 of the global eradication of rinderpest. This makes it only the second disease in history to be fully wiped out, following smallpox. [...] "
            "The outbreak in the 1890s killed an estimated 80–90% of all cattle in eastern and southern Africa. [...] "
            "the consequent human toll was mass starvation in the absence of herding, hunting, and farming. The human losses were estimated to be as high as one-third of the population of Ethiopia and two-thirds of the Maasai people of Tanzania. This famine caused significant depopulation in sub-Saharan Africa, allowing thornbush to colonise. This formed ideal habitat for tsetse fly, which carries sleeping sickness and is unsuitable for livestock",
            nome="Rinderpest")],
    },
    # 8 o sarampo veio de um vírus do gado
    {
        "temas_secundarios": ["evolucao", "domesticacao", "cidades"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "O vírus do sarampo descende de um vírus de gado. Um estudo de 2020 estimou que os dois se separaram por volta do século VI a.C., quando surgiam cidades grandes o bastante para o sarampo circular sem parar.",
        "explicacao": (
            "O parente mais próximo do vírus do sarampo é o da peste bovina, uma doença do gado hoje erradicada. "
            "Os dois descendem de um ancestral comum, muito provavelmente um vírus que infectava bois. Estimar "
            "quando se separaram é difícil: análises genéticas anteriores apontavam para os séculos XI "
            "e XII, com margem que chegava ao século V. Em 2020, um estudo sequenciou o genoma de um vírus de "
            "sarampo de 1912, recuperado de um pulmão conservado, e recalculou a separação para o "
            "século VI a.C., com média em 528 a.C. e um intervalo provável que vai de 1174 a.C. a 165 d.C. Essa época "
            "coincide com o surgimento das primeiras povoações humanas grandes o bastante para manter o sarampo "
            "circulando de forma contínua. A data marca a separação dos dois ramos: a passagem para humanos, e "
            "portanto o nascimento do sarampo como doença nossa, pode ter acontecido em qualquer ponto entre essa "
            "separação e o ancestral comum mais recente de todas as linhagens conhecidas, datado de 1880. Hoje, os "
            "humanos são os hospedeiros naturais do sarampo, e não se conhece nenhum reservatório animal."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Rinderpest",
                "The measles virus may have diverged from rinderpest around the 6th century BC, coinciding with the first human settlements large enough to sustain endemic measles transmission. [...] "
                "Measles virus and rinderpest virus diverged from a common ancestor, most likely a cattle-infecting virus. Earlier molecular clocks estimates have been superseded by a 2020 study, which sequenced the genome of a 1912 measles virus recovered from a preserved lung specimen and revised the estimated time of divergence to the 6th century BC (mean 528 BC, with a 95% credible interval of 1174 BC to 165 CE), coinciding with the rise of large cities. The spillover to humans; and thus the emergence of measles; could have occurred at any point between this divergence and the most recent common ancestor of all known measles virus strains, estimated at 1880 CE.",
                nome="Rinderpest"),
            wiki("Measles_morbillivirus",
                "Humans are the natural hosts of the virus; no animal reservoirs are known to exist. [...] "
                "The measles virus evolved from the now eradicated rinderpest virus which infected cattle. Sequence analysis has suggested that the two viruses most probably diverged in the 11th and 12th centuries, though the periods as early as the 5th century fall within the 95% confidence interval of these calculations.",
                nome="Measles morbillivirus"),
        ],
    },
    # 9 a máscara de bico não é da Peste Negra
    {
        "temas_secundarios": ["europa_medieval", "moda", "historia_medicina"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "A máscara de bico, símbolo da peste, não é da Peste Negra nem da Idade Média: nada indica que tenha sido usada antes do século XVII. Alguns historiadores até defendem que a figura nasceu como ficção.",
        "explicacao": (
            "O traje do \"médico da peste\" tinha chapéu de couro, máscara com olhos de vidro e um bico curvo, "
            "luvas, botas, túnica de linho encerado e uma vara para examinar os doentes sem tocar neles. O bico era "
            "recheado de coisas aromáticas, como flores secas, ervas, cânfora ou uma esponja com vinagre. A lógica "
            "vinha da teoria do miasma: um \"ar ruim\" seria a causa da doença, e os aromas protegeriam do mau "
            "cheiro. A teoria estava errada, mas o traje provavelmente protegia um pouco, porque cobria o corpo, e a "
            "túnica encerada impedia que as pulgas, as verdadeiras transmissoras da peste, se agarrassem ao tecido. "
            "A primeira descrição da roupa é atribuída a Charles de Lorme, médico do rei Luís XIII, durante um surto "
            "em Paris em 1619, com uma máscara de \"nariz de meio pé\" em forma de bico; pesquisas recentes, porém, "
            "pedem cautela com o relato dele. Um texto de 1373 já recomendava máscaras aos médicos, mas sem descrever como eram. A origem exata do traje é obscura, porque a maioria das imagens vem de textos "
            "satíricos e charges. Só se conhecem dois exemplares de máscara, ambos do século XVII e achados na "
            "Alemanha. A figura inspirou um personagem da commedia dell'arte e virou uma das máscaras típicas do "
            "Carnaval de Veneza."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Plague_doctor_costume",
            "Contrary to popular belief, no evidence suggests that the beak mask costume was worn during the Black Death or the Middle Ages. The costume started to appear in the 17th century when physicians studied and treated plague patients. [...] "
            "The costume consists of a leather hat, mask with glass eyes and a beak, stick to remove clothes of a plague victim, gloves, waxed linen robe, and boots. [...] "
            "The beak could hold dried flowers (commonly roses and carnations), herbs (commonly lavender and peppermint), camphor, or a vinegar sponge [...] "
            "The purpose of the mask was to keep away bad smells, such as the smell of decaying bodies. The smell taken with the most caution was known as miasma, a noxious form of \"bad air.\" This was thought to be the principal cause of the disease. [...] "
            "Though these particular theories about the plague's nature were incorrect, it is likely that the costume actually did afford the wearer some protection. "
            "The garments covered the body, shielding against splattered blood, lymph, and cough droplets, and the waxed robe prevented fleas (the true carriers of the plague) from touching the body or clinging to the linen. [...] "
            "Doctors used wooden canes in order to point out areas needing attention and to examine patients without touching them. [...] "
            "The exact origins of the costume are unclear, as most depictions come from satirical writings and political cartoons. An early reference to plague doctors wearing masks is in 1373 when Johannes Jacobi recommends their use but he offers no physical description of what these masks looked like. [...] "
            "though some historians insist that the plague doctor was originally fictional and inspired the real plague doctors later. [...] "
            "The garments were first mentioned by a physician to King Louis XIII of France, Charles de Lorme, who wrote in a 1619 plague outbreak in Paris [...] "
            "De Lorme wrote that the mask had a \"nose half a foot long, shaped like a beak, filled with perfume [...] "
            "Recent research has revealed that strong caveats must be applied with regard to De Lorme's assertions, however. [...] "
            "There are only two known artifacts of plague masks, both dated to the 17th century and both found in Germany. [...] "
            "The costume is also associated with a commedia dell'arte character called Il Medico della Peste ('The Plague Doctor'), who wears a distinctive plague doctor's mask. [...] "
            "is one of the distinctive masks worn during the Carnival of Venice.",
            nome="Plague doctor costume")],
    },
    # 10 quarentena começou como "trintena"
    {
        "temas_secundarios": ["palavras_viajantes", "europa_medieval", "navegacao_antiga"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "A quarentena começou como \"trintena\": em 1377, Ragusa, hoje Dubrovnik, mandou quem chegava esperar 30 dias isolado, para ver se surgiam sinais da peste. Depois o prazo subiu para 40 dias, a \"quarantena\" dos venezianos.",
        "explicacao": (
            "Entre 1348 e 1359, a Peste Negra matou, segundo as estimativas, cerca de 30% da população da Europa. "
            "Diante de surtos que voltavam, governos passaram a criar medidas de contenção. Veneza saiu na frente e "
            "nomeou três guardiões da saúde pública já nos primeiros anos da epidemia. Um documento de 1377 da "
            "cidade-república de Ragusa, na Dalmácia, hoje Dubrovnik, na Croácia, determinava que os recém-chegados "
            "passassem 30 dias num local separado, de início ilhas próximas, esperando para ver se desenvolviam "
            "sintomas. Em 1448, o Senado de Veneza ampliou a espera para 40 dias. A palavra vem do veneziano "
            "\"quarantena\", ou do francês \"quarantaine\", que significam \"quarenta dias\", o período em que navios "
            "tinham de ficar isolados antes que passageiros e tripulantes pudessem desembarcar. O isolamento de "
            "quarenta dias se mostrou uma fórmula eficaz contra os surtos de peste. Veneza fundou um lazareto numa "
            "ilhota junto à cidade em 1403, Gênova seguiu o exemplo em 1467, e em 1476 o antigo hospital de leprosos "
            "de Marselha virou hospital da peste. O mesmo recurso foi usado depois contra outras doenças, como a "
            "febre amarela na Espanha do início do século XIX e a cólera asiática em 1831."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Quarantine",
            "The word quarantine comes from quarantena or quarantaine, meaning \"forty days\", used in the Venetian language in the 14th and 15th centuries and also in France. The word is designated in the period during which all ships were required to be isolated before passengers and crew could go ashore during the Black Death plague. The quarantena followed the trentino, or \"thirty-day isolation\" period, first imposed in 1377 in the Republic of Ragusa, Dalmatia (modern Dubrovnik in Croatia). [...] "
            "Between 1348 and 1359, the Black Death wiped out an estimated 30% of Europe's population, and a significant percentage of Asia's population. Such a disaster led governments to establish measures of containment to handle recurrent epidemics. A document from 1377 states that before entering the city-state of Ragusa in Dalmatia (modern Dubrovnik in Croatia), newcomers had to spend 30 days (a trentine) in a restricted place (originally nearby islands) waiting to see whether the symptoms of Black Death would develop. In 1448 the Venetian Senate prolonged the waiting period to 40 days, thus giving birth to the term \"quarantine\". The forty-day quarantine proved to be an effective formula for handling outbreaks of the plague. [...] "
            "the advent of yellow fever in Spain at the beginning of the 19th century, and the arrival of Asiatic cholera in 1831. Venice took the lead in measures to check the spread of plague, having appointed three guardians of public health in the first years of the Black Death (1348). [...] "
            "Venice founded the first lazaret (on a small island adjoining the city) in 1403. In 1467 Genoa followed the example of Venice, and in 1476 the old leper hospital of Marseille was converted into a plague hospital.",
            nome="Quarantine")],
    },
    # 11 Carlos Chagas achou o parasita antes da doença
    {
        "temas_secundarios": ["ciencia_brasileira", "insetos", "brasil_republica"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Carlos Chagas achou primeiro um parasita novo no intestino do barbeiro e só depois foi atrás da doença. Em 1909, descreveu parasita, inseto transmissor, hospedeiros e sintomas de uma doença até então desconhecida.",
        "explicacao": (
            "Em 1907, Oswaldo Cruz mandou o jovem médico Carlos Chagas conter um surto de malária entre os "
            "trabalhadores de uma ferrovia em construção no interior de Minas Gerais. Acampado em Lassance, Chagas "
            "notou que as casas da roça estavam infestadas de um inseto grande que se alimenta de sangue, o barbeiro, "
            "chamado assim porque picava o rosto das pessoas à noite. Desconfiou na hora que ele pudesse transmitir "
            "algum parasita. No intestino dos insetos achou um protozoário de espécie nova, que batizou de "
            "Trypanosoma cruzi, em homenagem ao amigo. Depois o encontrou no sangue de um gato e, em 14 de abril de "
            "1909, no de Berenice, uma menina de dois anos que ele tinha visto na mesma casa onde o gato estivera. "
            "Em seguida, relacionou o parasita a lesões no coração e no cérebro, sugeriu o tatu como reservatório "
            "natural, descreveu 27 casos da forma aguda e fez mais de 100 autópsias de doentes crônicos. Descrever "
            "de uma vez uma doença desconhecida, com agente, vetor, hospedeiro, quadro clínico e epidemiologia, dá "
            "ao trabalho dele um lugar único na história da medicina. Chagas foi indicado ao Nobel em 1913 e em "
            "1921, mas não ganhou. Uma explicação possível é a forte oposição que enfrentou no Brasil, onde houve "
            "quem chegasse a duvidar da existência da doença."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Carlos_Chagas",
            "Chagas's work holds a unique place in the history of medicine, Chagas described in detail a previously-unknown infectious disease, its pathogen, vector (Triatominae), host, clinical manifestations, and epidemiology. [...] "
            "In 1907, there was an outbreak of malaria at the Minas Gerais hinterland, largely affecting railroad workers and greatly hampered the construction on new railway from Rio de Janeiro to the city of Belém in the Amazon. The Brazilian government asked Cruz for help. Cruz immediately assigned Chagas, with an assistant, Belisario Penna, to make the investigation. Camping at Lassance [...] "
            "During his investigation of malaria in Lassance, Chagas observed the peculiar infestation of the rural houses with a large hematophagous insect of the genus Triatoma, a kind of \"assassin bug\" or \"kissing bug\" (barbeiro, \"barber\" in Portuguese, so-called because it sucked the blood at night by biting the faces of its victims). [...] "
            "if by any chance it were, as I immediately supposed, a transmitter of any parasite of man or of another vertebrate. "
            "He discovered that the intestines of these insects harbored flagellate protozoans, a new species of the genus Trypanosoma [...] "
            "Chagas named this new parasite Trypanosoma cruzi  in honor of Oswaldo Cruz [...] "
            "he soon found the parasites in the blood of a cat. He then looked for a girl, later identified as Berenice Soares de Moura, a two-year-old girl whom he had seen in the same hut where that cat had been a few weeks before. He took Berenice's blood samples on 14 April 1909, discovering for the first time the same Trypanosoma parasite in the human blood. He also observed parasitic inclusions in the brain and myocardium, which would explain some of the clinical manifestations in diseased people, and closed the proposed lifecycle of the parasite by suggesting that the armadillo could be its natural reservoir. To complete his work on the pathology of the new disease, Chagas described 27 cases of the acute form of the disease and performed more than 100 autopsies on patients who exhibited the chronic form. [...] "
            "Chagas was twice nominated for the Nobel Prize in Physiology or Medicine, in 1913 and 1921, but never received any. [...] "
            "The reason why the prize was not awarded to Chagas may have been the strong opposition that he faced in Brazil, from some physicians and researchers of that time. They went as far as questioning the existence of Chagas disease",
            nome="Carlos Chagas")],
    },
    # 12 a pólio virou epidemia quando as cidades ficaram mais limpas
    {
        "temas_secundarios": ["sistema_imunologico", "cidades", "desenvolvimento_humano"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "As grandes epidemias de paralisia infantil surgiram quando as cidades ficaram mais limpas. Com menos contato com o vírus na primeira infância, mais gente se infectava mais velha, quando a paralisia é bem mais comum.",
        "explicacao": (
            "Grandes epidemias de pólio eram desconhecidas antes do século XX: surtos localizados de paralisia "
            "começaram a aparecer na Europa e nos EUA por volta de 1900. Antes disso, a infecção raramente era vista "
            "em bebês com menos de 6 meses, e a maioria dos casos ocorria entre os 6 meses e os 4 anos. Crianças "
            "pequenas que pegam pólio costumam ter sintomas leves e, com isso, ficam imunes para sempre. No fim do "
            "século XIX e começo do XX, os países ricos melhoraram o saneamento, com esgoto e água limpa. Com mais "
            "higiene, bebês e crianças pequenas tinham menos chance de encontrar o vírus e criar imunidade, e o "
            "primeiro contato passou a acontecer no fim da infância ou na vida adulta. E a idade pesa: a paralisia "
            "aparece em 1 de cada 1.000 crianças infectadas, mas em 1 de cada 75 adultos. Em 1950, nos EUA, o pico de "
            "casos paralíticos já tinha passado dos bebês para crianças de 5 a 9 anos, e cerca de um terço dos casos "
            "era em maiores de 15 anos. A epidemia americana de 1952, a pior da história do país, teve 57.628 casos e "
            "3.145 mortes, e ajudou a voltar a atenção do público para a necessidade de uma vacina."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("History_of_polio",
            "Major polio epidemics were unknown before the 20th century; localized paralytic polio epidemics began to appear in Europe and the United States around 1900. [...] "
            "Prior to the 20th century, polio infections were rarely seen in infants before 6 months of age, and most cases occurred in children 6 months to 4 years of age. Young children who contract polio generally develop only mild symptoms, but as a result they become permanently immune to the disease.  In developed countries during the late 19th and early 20th centuries, improvements were being made in community sanitation, including improved sewage disposal and clean water supplies. Better hygiene meant that infants and young children had fewer opportunities to encounter and develop immunity to polio. Exposure to poliovirus was therefore delayed until late childhood or adult life, when it was more likely to take the paralytic form. "
            "In children, paralysis due to polio occurs in one in 1,000 cases, while in adults, paralysis occurs in one in 75 cases. By 1950, the peak age incidence of paralytic poliomyelitis in the United States had shifted from infants to children aged 5 to 9 years; about one-third of the cases were reported in persons over 15 years of age. [...] "
            "In the United States, the 1952 polio epidemic was the worst outbreak in the nation's history, and is credited with heightening parents' fears of the disease and focusing public awareness on the need for a vaccine.  Of the 57,628 cases reported that year, 3,145 died",
            nome="History of polio")],
    },
    # 13 cocoliztli, a peste misteriosa do México colonial
    {
        "temas_secundarios": ["americas_pre_colombianas", "imperios_coloniais", "microbiologia"],
        "tipos_espanto": ["misterio_aberto", "escala_absurda"],
        "gancho": "No século XVI, uma doença misteriosa matou de 5 a 15 milhões de pessoas no México colonial. Os astecas a chamavam de cocoliztli, \"peste\". Em 2018, DNA dos dentes de vítimas apontou um suspeito, mas o caso segue aberto.",
        "explicacao": (
            "As epidemias de cocoliztli, marcadas por febre alta e sangramentos, devastaram as terras altas do "
            "México, e a de 1545 costuma ser chamada de a pior epidemia da história do país. Pelo menos 12 surtos são "
            "atribuídos à doença, os maiores em 1545, 1576, 1736 e 1813, e em geral eles vinham até dois anos depois "
            "de uma grande seca. Os indígenas foram os mais atingidos, seguidos pelos africanos; os europeus "
            "morreram menos. Médicos espanhóis e indígenas não souberam identificá-la, e um médico espanhol que "
            "viu o surto de 1576 fazia questão de usar o nome em náuatle. Em 2018, a equipe do bioquímico alemão "
            "Johannes Krause extraiu DNA dos dentes de 29 pessoas de um cemitério de Oaxaca, o único ligado com "
            "segurança às vítimas do surto de 1545 a 1548. Em dez delas apareceu uma variedade rara de salmonela, a "
            "Paratyphi C, que causa uma febre parecida com a tifoide e não estava no solo nem em pessoas de antes do "
            "contato com os europeus. A bactéria já existia na Europa: foi achada num cemitério norueguês do século "
            "XIII. Mas a geneticista María Ávila-Arcos contesta a conclusão, porque os sintomas não batem bem, e "
            "vírus de RNA nem foram investigados. Outra hipótese é uma febre hemorrágica nativa, agravada pela pior "
            "seca da região em 500 anos e pelas condições impostas aos indígenas depois da conquista."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Cocoliztli_epidemics",
            "The Cocoliztli Epidemic or the Great Pestilence was an outbreak of a mysterious illness characterized by high fevers and bleeding which caused 5–15 million deaths in the North American territory of New Spain during the 16th century. The Aztec people called it cocoliztli, Nahuatl for pestilence. It ravaged the Mexican highlands in epidemic proportions [...] "
            "Based on the death toll, this outbreak is often referred to as the worst epidemic in the history of Mexico. Subsequent outbreaks continued to baffle both Spanish and native physicians, with little consensus among modern researchers on the pathogenesis. [...] "
            "Others believe cocoliztli was caused by an indigenous viral hemorrhagic fever, perhaps exacerbated by the worst droughts to affect that region in 500 years and poor living conditions for Indigenous peoples of Mexico following the Spanish conquest (c. 1519). [...] "
            "At least 12 epidemics are attributed to cocoliztli, with the largest occurring in 1545, 1576, 1736, and 1813. [...] "
            "Cocoliztli epidemics usually occurred within two years of a major drought. [...] "
            "However, the modern consensus is that Indigenous people were most affected by cocoliztli, followed by Africans. Europeans experienced lower mortality rates than other groups. [...] "
            "Francisco Hernández de Toledo, a Spanish physician, insisted on using the Nahuatl word when describing the disease to correspondents in the Old World. [...] "
            "According to Francisco Hernández de Toledo, a physician who witnessed the outbreak in 1576 [...] "
            "In 2018, Johannes Krause, a German biochemist at the Max Planck Institute for the Science of Human History, and colleagues discovered new evidence for an Old World culprit. DNA samples from the teeth of 29 sixteenth-century skeletons in the Oaxaca region of Mexico [...] "
            "The Contact-era site has the only cemetery to be conclusively linked to victims of the outbreak of 1545–1548. [...] "
            "Within ten individuals, they identified Salmonella enterica subsp. enterica serovar Paratyphi C, which causes enteric fevers in humans. This strain of Salmonella is unique to humans and was not found in any soil samples or pre-contact individuals that were used as controls. Enteric fevers, also known as typhoid or paratyphoid [...] "
            "The recent discovery of S. Paratyphi C within a 13th-century Norwegian cemetery supports these findings. [...] "
            "Evolutionary geneticist, María Ávila-Arcos, has questioned this evidence since S. enterica's symptoms are poorly matched with the disease. Ávila-Arcos, Krause’s team, and authors of earlier historical analyses point out that RNA viruses, among other non-bacterial pathogens, have not been investigated.",
            nome="Cocoliztli epidemics")],
    },
    # 14 o último caso natural de varíola virou vacinador
    {
        "temas_secundarios": ["personagens_esquecidos", "sistema_imunologico"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "O último caso natural de varíola do mundo foi um cozinheiro de hospital na Somália, em 1977. Segundo ele, tinha evitado a vacina por medo da injeção. Décadas depois, morreu trabalhando como vacinador contra a pólio.",
        "explicacao": (
            "Ali Maow Maalin trabalhava como cozinheiro no hospital de Merca, no sul da Somália, e às vezes ajudava "
            "uma equipe de vacinação da OMS. Em outubro de 1977, guiou um carro que levava duas crianças com varíola, "
            "vindas de um acampamento nômade, para o isolamento. Acredita-se que ele tenha se infectado nessa curta "
            "viagem. Uma das crianças, Habiba Nur Ali, de seis anos, morreu dois dias depois, a última pessoa a "
            "morrer de varíola adquirida naturalmente. Maalin teve febre e foi tratado como se fosse malária; quando "
            "surgiram as manchas, acharam que era catapora. Como não queria ser isolado, não se apresentou, até que "
            "uma colega o denunciou. Ele teve a forma mais branda da doença e se recuperou. As versões sobre a "
            "vacina dele divergem: um epidemiologista do CDC disse que ela não pegou, e em 2007 o próprio Maalin "
            "contou que fugiu dela porque a agulhada parecia doer. A OMS rastreou 161 contatos, 54.777 pessoas foram "
            "vacinadas em duas semanas, e ninguém mais adoeceu. Em 1979, a varíola foi declarada erradicada. Maalin "
            "depois foi um dos 10 mil voluntários da campanha que livrou a Somália da pólio em 2008, e contava sua "
            "história a pais que recusavam a vacina. Morreu de malária em 2013, durante a vacinação que se seguiu à "
            "volta do vírus da pólio ao país."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Ali_Maow_Maalin",
            "was a Somali hospital cook and health worker from Merca who is the last person known to have been infected with naturally occurring Variola minor smallpox. The disease was diagnosed in October 1977 and Maalin made a full recovery. [...] "
            "Smallpox was declared to have been eradicated globally by the World Health Organization (WHO) two years later. Maalin was subsequently involved in the successful poliomyelitis eradication campaign in Somalia, and he died of malaria while carrying out polio vaccinations after the re-emergence of the poliovirus in 2013. [...] "
            "He worked as a hospital cook, as well as an occasional vaccinator for a WHO smallpox eradication team. [...] "
            "According to CDC epidemiologist Jason Weisfeld, one of the people who led the later containment effort in Merca, Maalin had received the smallpox vaccine but it had failed to take effect, and he had not been protected. Other sources state that he had not been vaccinated. It was later revealed in an interview in 2007, Maalin said that he had not been vaccinated, explaining: \"I was scared of being vaccinated then. It looked like the shot hurt.\" [...] "
            "On 12 October 1977, two children with smallpox symptoms were discovered at an encampment [...] "
            "Maalin, then aged 23, served as a guide to the party taking them in a closed Land Cruiser from the hospital where he worked either to the home of a surveillance supervisor or directly to the isolation camp. He is believed to have been infected during the journey, which lasted no more than 5–15 minutes. One of the children, a six-year-old girl named Habiba Nur Ali, died two days later. She was the last person to die from naturally acquired smallpox. [...] "
            "On 22 October, Maalin fell ill with fever and headache, and received malaria treatment in hospital. After four days a rash appeared. Perhaps working on the assumption that he had been successfully vaccinated against smallpox, Maalin was then believed to have chickenpox and was discharged from hospital. [...] "
            "Not wishing to be put into isolation, Maalin failed to report himself. On 30 October, a nurse colleague reported him [...] "
            "In August 1977, an outbreak developed in a Somali nomadic group of twenty families [...] "
            "A total of 161 contacts were identified [...] "
            "A total of 54,777 people were vaccinated in the two weeks following Maalin's isolation. [...] "
            "Maalin remains the last case of naturally acquired smallpox in the world. On 26 October 1979, two years after the day when Maalin's rash appeared, WHO declared that smallpox had been eradicated globally. [...] "
            "Maalin was among the 10,000 volunteers who participated in the effort to eradicate poliomyelitis from Somalia, which succeeded in 2008. [...] "
            "\"Now when I meet parents who refuse to give their children the polio vaccine, I tell them my story. [...] "
            "V. minor was the rarer of the two strains, and causes a much less severe disease",
            nome="Ali Maow Maalin")],
    },
    # 15 tatus e esquilos com hanseníase
    {
        "temas_secundarios": ["ecologia", "grandes_navegacoes", "europa_medieval"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Tatus do sul dos EUA carregam a bactéria da hanseníase e podem passá-la a pessoas. Pela genética, eles a pegaram de humanos há no máximo alguns séculos, provavelmente dos primeiros europeus nas Américas.",
        "explicacao": (
            "A bactéria da hanseníase, Mycobacterium leprae, só se multiplica dentro de células vivas e não pode "
            "ser cultivada em meios de laboratório, mas há infecções naturais em alguns primatas, em tatus e em "
            "esquilos-vermelhos. No centro-sul dos EUA, de 15% a 20% dos tatus de uma espécie carregam a bactéria. "
            "Como a temperatura do corpo deles é baixa, seus tecidos costumam acumular quantidades enormes do "
            "micróbio. A análise genética das linhagens dos tatus indica origem humana de no máximo algumas "
            "centenas de anos, e por isso se suspeita que os animais a pegaram, por acaso, dos primeiros exploradores "
            "europeus. A infecção se manteve entre os tatus e pode voltar a pessoas que manuseiam os bichos ou comem "
            "sua carne. Na Grã-Bretanha, descobriu-se em 2016 que os esquilos-vermelhos, uma espécie ameaçada, "
            "também carregam a doença. A linhagem achada na ilha de Brownsea equivale a uma que se julgava extinta "
            "entre humanos desde a Idade Média, e um crânio anterior à conquista normanda, escavado em Suffolk em "
            "2017, tinha DNA de uma linhagem muito parecida. Há quem sugira que o comércio de peles de esquilo, "
            "muito valorizadas na época, tenha alimentado a hanseníase medieval na Europa. Hoje, porém, o risco de "
            "transmissão dos esquilos selvagens para pessoas parece baixo: o último caso humano adquirido no Reino "
            "Unido foi registrado há mais de 200 anos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Leprosy",
            "M. leprae and M. lepromatosis are obligate intracellular pathogens and cannot grow or be cultured outside of host tissues. [...] "
            "Naturally occurring infections have been reported in nonhuman primates (including the African chimpanzee, the sooty mangabey, and the cynomolgus macaque), armadillos, and red squirrels. Multilocus sequence typing of the armadillo M. leprae strains suggests that they were of human origin for at most a few hundred years. Thus, it is suspected that armadillos first acquired the organism incidentally from early European explorers of the Americas. This incidental transmission was sustained in the armadillo population. It may be transmitted back to humans, making leprosy a zoonotic disease (spread between humans and animals). Red squirrels (Sciurus vulgaris), a threatened species in Great Britain, were found to carry leprosy in November 2016. It has been suggested that the trade in red squirrel fur, highly prized in the medieval period and intensively traded, may have been responsible for the leprosy epidemic in medieval Europe. A pre-Norman era skull excavated in Hoxne, Suffolk, in 2017 was found to carry DNA from a strain of M. leprae which closely matched the strain carried by modern red squirrels on Brownsea Island. [...] "
            "Humans can acquire a leprosy infection from armadillos by handling them or consuming armadillo meat. [...] "
            "The M. leprae strain discovered on Brownsea Island is equated to one thought to have died out in the human population in medieval times. Despite this, and speculation regarding past transmission through trade in squirrel furs, there does not seem to be a high risk of squirrel to human transmission from the wild population. Although leprosy continues to be diagnosed in immigrants to the UK, the last known human case of leprosy arising in the UK was recorded over 200 years ago. [...] "
            "Between 15 and 20% of Mexican long-nosed armadillos(Dasypus mexicanus) in the south-central United States carry M. leprae. As a result of their low body temperature, their tissues commonly contain massive numbers of organisms",
            nome="Leprosy")],
    },
    # 16 Revolta da Vacina: a dinamite de papel prateado e a epidemia de 1908
    {
        "temas_secundarios": ["brasil_republica", "cidades", "historia_medicina"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1904, a Revolta da Vacina, no Rio, levou o governo a suspender a vacinação obrigatória contra a varíola. Em 1908, a cidade enfrentou uma epidemia da doença que matou quase 6.400 pessoas.",
        "explicacao": (
            "No começo do século XX, o Rio de Janeiro, então capital, sofria com febre amarela, peste bubônica e "
            "varíola. O médico Oswaldo Cruz, que assumiu a Saúde Pública em 1903, comandou campanhas de saneamento, "
            "enquanto o prefeito Pereira Passos fazia uma reforma urbana que derrubou cortiços e provocou uma crise "
            "de moradia. Em 31 de outubro de 1904, foi aprovada uma lei que tornava obrigatória a vacinação contra a "
            "varíola, apesar de forte campanha contrária. Entre 10 e 16 de novembro, a cidade viveu uma semana de "
            "motins. Militares florianistas e positivistas tentaram aproveitar a revolta para dar um golpe de "
            "Estado, que fracassou. No bairro da Saúde, um dos maiores focos, verificou-se depois que a dinamite "
            "pendurada em volta das trincheiras era feita de pedaços de madeira embrulhados em papel prateado, e o "
            "canhão, um cano de iluminação pública montado sobre rodas de carroça. No dia 16, o governo decretou "
            "estado de sítio e suspendeu a vacinação obrigatória. A repressão deixou 945 presos na Ilha das Cobras, "
            "30 mortos, 110 feridos e 461 deportados para o Acre, muitos deles sem prova de que tivessem participado. "
            "Quatro anos depois, veio a epidemia de varíola de 1908, com quase 6.400 mortos."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Revolta_da_Vacina",
                "A Revolta da Vacina foi um motim popular ocorrido entre 10 e 16 de novembro de 1904 na cidade do Rio de Janeiro, então capital do Brasil. Seu pretexto imediato foi uma lei que determinava a obrigatoriedade da vacinação contra a varíola, mas também é associada a causas mais profundas, como as reformas urbanas que estavam sendo realizadas pelo prefeito Pereira Passos e as campanhas de saneamento lideradas pelo médico Oswaldo Cruz. [...] "
                "Um grupo de militares florianistas e positivistas, com o apoio de alguns setores civis, tentou se aproveitar do descontentamento popular para realizar um golpe de Estado na madrugada do dia 14 para o dia 15 de novembro, que, no entanto, foi derrotado. No dia 16 de novembro, foi decretado o estado de sítio e a suspensão da vacinação obrigatória. [...] "
                "Os maiores focos de revolta estavam concentrados na Saúde e no Sacramento. [...] "
                "O saldo total foi de 945 pessoas presas na Ilha das Cobras, 30 mortos, 110 feridos e 461 deportados para o estado do Acre. [...] "
                "ico Oswaldo Cruz, que assumiu a Diretoria Geral de Saúde Pública em 1903, coube a campanha de saneamento da cidade, que visava erradicar a febre amarela, a peste bubônica e a varíola. [...] "
                "A lei gerou debates exaltados entre os legisladores e a população e, apesar da forte campanha de oposição, foi aprovada no dia 31 de outubro. [...] "
                "A demolição dos velhos casarões, àquela altura já quase todos transformados em pensões e cortiços, provocou uma crise de habitação [...] "
                "Verificou-se também que as dinamites e bocas-de-fogo não passavam de um engodo. As primeiras eram, na verdade, peças de madeira envoltas em papel prateado, dependuradas por arames em torno das trincheiras, enquanto a boca-de-fogo não passava de um cano de iluminação pública co [...] "
                "As vítimas da repressão que se seguiu foram, em geral, os indivíduos mais pobres, que poderiam ter tomado parte na revolta, embora sua participação nem sempre fosse comprovada. [...] "
                "a população do Rio de Janeiro teria de suportar uma epidemia de varíola em 1908, na qual morreram quase 6 400 pessoas.",
                nome="Revolta da Vacina", idioma="pt"),
            wiki("Vaccine_Revolt",
                "On 16 November, a state of emergency was decreed and mandatory vaccination was suspended. [...] "
                "the population of Rio de Janeiro would have to endure a smallpox epidemic in 1908, in which almost 6,400 people died.",
                nome="Vaccine Revolt"),
        ],
    },
]
