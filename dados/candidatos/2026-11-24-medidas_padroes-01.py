LOTE = "2026-11-24-medidas_padroes-01"
AREA = "tecnologia"
TEMA = "medidas_padroes"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/", "fr": "https://fr.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 O Grand K, o quilograma que "emagrecia"
    {
        "temas_secundarios": ["elementos_quimicos", "mecanica_quantica"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "O quilograma oficial do mundo, um cilindro de platina guardado na França, parecia perder massa em relação às suas cópias. Mas, como ele era o quilograma por definição, não dava para saber quem tinha mudado.",
        "explicacao": (
            "De 1889 a 2019, o quilograma foi a massa de um objeto: o Protótipo Internacional do Quilograma, "
            "apelidado pelos metrologistas de Le Grand K. É um cilindro do tamanho aproximado de uma bola de golfe, "
            "feito de uma liga com 90% de platina e 10% de irídio e guardado num cofre do BIPM, o Bureau "
            "Internacional de Pesos e Medidas, em Saint-Cloud, na França. Vários países receberam cópias oficiais "
            "(a do Brasil é a de número 66), e as comparações com o original foram raras: só três, em 1889, 1948 "
            "e 1989. Ficou claro que as massas iam se afastando lentamente umas das outras. Em um século, o Grand K "
            "perdeu talvez 50 microgramas em relação às cópias. Só que o erro da massa dele era, por definição, zero, "
            "e dá no mesmo dizer que as primeiras cópias ganharam, em média, cerca de 25 microgramas. Nenhum "
            "mecanismo plausível foi proposto para explicar a deriva. Guardados no ar, ainda que sob campânulas de "
            "vidro, os protótipos acumulam contaminação na superfície e precisavam de um método especial de limpeza. "
            "A saída foi abandonar o objeto: desde 20 de maio de 2019, o quilograma é definido fixando um valor exato "
            "para a constante de Planck, e pode ser realizado em laboratório com instrumentos como a balança de Kibble."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("International_Prototype_of_the_Kilogram",
                 "metrologists as the IPK or Le Grand K [...] "
                 "is an object whose mass was used to define the kilogram from 1889, when it replaced the Kilogramme des Archives, until 2019, "
                 "when it was replaced by a new definition of the kilogram based entirely on physical constants. [...] "
                 "The IPK is a roughly golfball-sized object made of a platinum [...] which is 90% platinum and 10% iridium (by mass) [...] "
                 "The IPK itself, stored in the BIPM's vault in Saint-Cloud, France. [...] Brazil (66) [...] "
                 "Before 2019, by definition, the error in the measured value of the IPK's mass was exactly zero; the mass of the IPK was the kilogram. [...] "
                 "The only three verifications occurred in 1889, 1948, and 1989. [...] "
                 "masses of the entire worldwide ensemble of prototypes have been slowly but inexorably diverging from each other. "
                 "It is also clear that the IPK lost perhaps 50 μg of mass over the last century, and possibly significantly more, in comparison to its official copies. "
                 "The reason for this drift has eluded physicists who have dedicated their careers to the SI unit of mass. No plausible mechanism has been proposed [...] "
                 "it is equally valid to state that the first batch of replicas has, as a group, gained an average of about 25 μg over one hundred years in comparison to the IPK. [...] "
                 "Since the IPK and its replicas are stored in air (albeit under two or more nested bell jars), they gain mass through adsorption of atmospheric contamination onto their surfaces. "
                 "Accordingly, they are cleaned in a process the BIPM developed",
                 nome="International Prototype of the Kilogram"),
            wiki("Kilogram",
                 "It is defined by taking the fixed numerical value of the Planck constant h to be [...] "
                 "The new definition took effect on 20 May 2019.",
                 nome="Kilogram"),
            wiki("Kibble_balance",
                 "It is a metrological instrument that can realize the definition of the kilogram unit of mass based on fundamental constants.",
                 nome="Kibble balance"),
        ],
    },
    # 2 Por que o segundo tem 9.192.631.770 oscilações
    {
        "temas_secundarios": ["historia_astronomia", "relatividade"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "O segundo vale 9.192.631.770 oscilações do átomo de césio. O número quebrado vem de uma calibração: foi o que coube no segundo dos astrônomos, baseado no movimento da Terra medido entre 1750 e 1892.",
        "explicacao": (
            "Por muito tempo, o segundo foi a 86.400ª parte do dia solar médio, ou seja, dependia da rotação da Terra. No fim "
            "dos anos 1940, relógios de quartzo ficaram bons o bastante para mostrar que marcavam o tempo melhor que o "
            "próprio giro do planeta. Os metrologistas sabiam que a órbita em torno do Sol era bem mais estável, e em "
            "1956 o segundo foi redefinido como uma fração do ano trópico de 1900. O ano não era medido, e sim "
            "calculado pelas Tabelas do Sol de Simon Newcomb, de 1895, baseadas em observações feitas entre 1750 e "
            "1892. Na prática, o segundo de Newcomb era o segundo solar médio daquele período. Quando os relógios "
            "atômicos de césio começaram a funcionar, em 1955, logo confirmaram que a rotação da Terra oscila de forma "
            "irregular. Depois de três anos comparando o césio com observações da Lua, a equipe de William Markowitz "
            "concluiu, em 1958, que o segundo das efemérides correspondia a 9.192.631.770 ciclos da radiação do "
            "césio, com margem de 20. Em 1967, esse número virou a definição oficial, escolhido para que o segundo "
            "atômico tivesse exatamente a duração do anterior. Como o dia ficou um pouco mais longo desde o século "
            "XIX, por causa do atrito das marés, o segundo do SI já nasceu um pouco mais curto que o segundo solar "
            "médio da época em que foi adotado."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Second",
                 "for a total of 24 × 60 × 60 = 86400 seconds per day. [...] "
                 "is defined by taking the fixed numerical value of the caesium (Cs) frequency, ΔνCs, the unperturbed ground-state hyperfine transition frequency of the Cs-133 atom, to be 9192631770 when expressed in the unit hertz [...] "
                 "MKS was adopted internationally during the 1940s, defining the second as [...] of a mean solar day. [...] "
                 "Sometime in the late 1940s, quartz crystal oscillator clocks with an operating frequency of ~100 kHz advanced to keep time with accuracy better than [...] "
                 "It became apparent that a consensus of such clocks kept better time than the rotation of the Earth. "
                 "Metrologists also knew that Earth's orbit around the Sun (a year) was much more stable than Earth's rotation. [...] "
                 "The Earth's motion was described in Newcomb's Tables of the Sun (1895), which provided a formula for estimating the motion of the Sun "
                 "relative to the epoch 1900 based on astronomical observations made between 1750 and 1892. [...] "
                 "The tropical year in the definition was not measured but calculated from a formula [...] "
                 "In 1956, the second was redefined in terms of a year relative to that epoch. [...] "
                 "This length of a second was selected to correspond exactly to the length of the ephemeris second previously defined.",
                 nome="Second"),
            wiki("Ephemeris_time",
                 "Caesium atomic clocks became operational in 1955, and quickly confirmed the evidence that the rotation of the Earth fluctuated irregularly. [...] "
                 "After three years of comparisons with lunar observations, Markowitz et al. (1958) determined that the ephemeris second corresponded to "
                 "9 192 631 770 ± 20 cycles of the chosen cesium resonance.",
                 nome="Ephemeris time"),
            wiki("Earth's_rotation",
                 "Currently, each of these seconds is slightly longer than an SI second because Earth's mean solar day is now slightly longer than it was "
                 "during the 19th century due to tidal friction. [...] "
                 "The mean solar second between 1750 and 1892 was chosen in 1895 by Simon Newcomb as the independent unit of time in his Tables of the Sun. "
                 "These tables were used to calculate the world's ephemerides between 1900 and 1983, so this second became known as the ephemeris second. "
                 "In 1967 the SI second was made equal to the ephemeris second.",
                 nome="Earth's rotation"),
            wiki("Tidal_acceleration",
                 "(The SI second, when adopted, was already a little shorter than the current value of the second of mean solar time.)",
                 nome="Tidal acceleration"),
        ],
    },
    # 3 O relógio "impossível" de Harrison, testado em 2015
    {
        "temas_secundarios": ["grandes_navegacoes", "invencoes", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "John Harrison, o relojoeiro da longitude, foi ridicularizado ao dizer que projetara um relógio que erraria só um segundo em 100 dias. Montado pelo seu desenho, o relógio foi testado em 2015: atrasou 5/8 de segundo.",
        "explicacao": (
            "Harrison era carpinteiro e consertava relógios nas horas vagas. Ficou famoso no século XVIII pelos "
            "relógios marítimos que permitiam calcular a longitude no mar, problema pelo qual a Lei da Longitude, de "
            "1714, oferecia até 20.000 libras. A Junta da Longitude exigiu novos testes mesmo depois de bons "
            "resultados, e ele só recebeu 8.750 libras do Parlamento em 1773, aos 80 anos, depois que o rei Jorge III "
            "testou um dos seus relógios e tomou o seu partido. O prêmio oficial nunca foi dado a ninguém. Nos "
            "últimos anos de vida, Harrison afirmou ter projetado um relógio de pêndulo, para uso em terra, que "
            "manteria a hora com erro de um segundo em 100 dias. Publicações da época zombaram da ideia, e ele deixou "
            "o desenho sem nunca construí-lo. Em 1970, o relojoeiro Martin Burgess, especialista em Harrison, estudou "
            "os planos e fez duas versões. A segunda, o Clock B, ficou décadas inacabada na oficina, até ser comprada "
            "em 2009 e levada ao Museu Marítimo Nacional, em Greenwich. De 6 de janeiro a 17 de abril de 2015, ela "
            "funcionou numa caixa transparente no Observatório Real, sem ser tocada além da corda, e perdeu só 5/8 de "
            "segundo. O Guinness a declarou o relógio mecânico mais preciso com pêndulo oscilando ao ar livre. Há uma "
            "ressalva: o Clock B usa materiais que Harrison não tinha, como duralumínio e invar."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("John_Harrison",
                 "the British Parliament was offering financial rewards of up to £20,000 [...] under the 1714 Longitude Act, though Harrison never received the full reward due to political rivalries. [...] "
                 "Following his father's trade as a carpenter, Harrison built and repaired clocks in his spare time. [...] "
                 "the Board were persuaded that the accuracy could have been just luck and demanded another trial. [...] "
                 "decided to enlist the aid of King George III. He obtained an audience with the King, who was extremely annoyed with the Board. "
                 "King George tested the watch No. 2 (H5) himself at the palace [...] "
                 "Finally in 1773, when he was 80 years old, Harrison received a monetary award in the amount of £8,750 from Parliament for his achievements, "
                 "but he never received the official award (which was never awarded to anyone). [...] "
                 "he claimed to have designed a clock capable of keeping accurate time to within one second over a span of 100 days. "
                 "At the time, such publications as The London Review of English and Foreign Literature ridiculed Harrison for what was considered an outlandish claim. "
                 "Harrison drew a design but never built such a clock himself, but in 1970 Martin Burgess, a Harrison expert and himself a clockmaker, "
                 "studied the plans and endeavored to build the timepiece as drawn. He built two versions, dubbed Clock A and Clock B. [...] "
                 "Clock B lay unfinished in his workshop for decades until it was acquired in 2009 by Donald Saff. "
                 "The completed Clock B was submitted to the National Maritime Museum in Greenwich for further study. [...] "
                 "over a 100-day period from 6 January to 17 April 2015, Clock B was secured in a transparent case in the Royal Observatory and left to run untouched, "
                 "apart from regular winding. Upon completion of the run, the clock was measured to have lost only 5/8 of a second [...] "
                 "this clock uses materials such as duraluminium and invar unavailable to Harrison [...] "
                 "Guinness World Records has declared Martin Burgess' Clock B the \"most accurate mechanical clock with a pendulum swinging in free air.\"",
                 nome="John Harrison"),
        ],
    },
    # 4 A França e a hora "de Paris atrasada 9 min 21 s"
    {
        "temas_secundarios": ["fronteiras_paises", "calendarios"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1911, a França adotou a hora de Greenwich sem escrever \"Greenwich\": a lei falava na hora de Paris menos 9 minutos e 21 segundos. Em 1884, França e Brasil tinham se abstido na escolha do meridiano.",
        "explicacao": (
            "Em 1884, uma conferência internacional em Washington adotou o meridiano de Greenwich como o meridiano "
            "principal do mundo. A votação foi de 22 a 1: São Domingos, atual República Dominicana, votou contra, e "
            "França e Brasil se abstiveram. Os franceses insistiam num meridiano de caráter neutro, do mesmo jeito que "
            "defendiam o metro como medida neutra, mas pesou o argumento prático de manter a continuidade com a "
            "maioria das cartas náuticas. Desde 1891, por causa dos horários dos trens, a hora oficial francesa era a "
            "do Observatório de Paris, cujo meridiano fica cerca de 2°20′ a leste do de Greenwich. A lei de 9 de março "
            "de 1911 adotou a hora de Greenwich, mas sem citar a cidade inglesa: a referência continuou sendo a hora "
            "de Paris, da qual se subtraíam 9 minutos e 21 segundos. A diferença real é de 9 minutos e 20,921 "
            "segundos, então, a rigor, a hora legal francesa ficava quase um décimo de segundo atrás da de Greenwich. "
            "A fórmula só foi abandonada em 1978, quando a França passou a usar o Tempo Universal Coordenado (UTC) "
            "como base da hora legal. Ainda assim, cartógrafos franceses continuam a indicar o meridiano de Paris em "
            "alguns mapas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("International_Meridian_Conference",
                 "Resolution 2, fixing the meridian at Greenwich, was passed 22–1 (San Domingo, now the Dominican Republic, voted against); France and Brazil abstained. "
                 "The French did not adopt the Greenwich meridian as the beginning of the universal day until 1911. "
                 "Even then it refused to use the name \"Greenwich\", instead using the term \"Paris mean time, retarded by 9 minutes and 21 seconds\". "
                 "France finally replaced this phrase with \"Coordinated Universal Time\" (UTC) in 1978. [...] "
                 "France's insistence that the meridian should have a strictly neutral character in the same way that they maintained that the metre was a neutral measure. [...] "
                 "In the end, the pragmatic argument for continuity with most nautical charts won the day and the French delegation abstained in the vote.",
                 nome="International Meridian Conference"),
            wiki("Heure_en_France",
                 "Par la loi du 9 mars 1911, la France adopte l'heure du méridien de Greenwich [...] "
                 "Notons que le texte de loi ne mentionne pas explicitement la ville anglaise de Greenwich. "
                 "En effet, l'heure de référence reste l'« heure de Paris » à laquelle on soustrait 9 minutes et 21 secondes, pour correspondre à l'heure GMT. [...] "
                 "le décalage horaire entre le méridien de Paris et celui de Greenwich est en réalité de 9 minutes et 20,921 s (arrondies à 21 secondes) [...] "
                 "En toute rigueur, l'heure légale française telle qu'elle est définie retarde donc de près d'un dixième de seconde sur le temps moyen de Greenwich.",
                 nome="Heure en France", idioma="fr"),
            wiki("Time_in_France",
                 "In 1891, to avoid complications with railway timetables, time was unified in Metropolitan France and based on the solar time at the Paris Observatory [...] "
                 "the Paris meridian being approximately 2°20′ east of the Greenwich meridian",
                 nome="Time in France"),
            wiki("Paris_meridian",
                 "In 1884, at the International Meridian Conference in Washington DC, the Greenwich meridian was adopted as the prime meridian of the world. [...] "
                 "Despite this, French cartographers continue to indicate the Paris meridian on some maps.",
                 nome="Paris meridian"),
        ],
    },
    # 5 Os EUA medem pelo metro desde 1893 (e os dois "pés")
    {
        "temas_secundarios": ["leis_julgamentos", "fronteiras_paises"],
        "tipos_espanto": ["contraintuitivo", "origem_inesperada"],
        "gancho": "Os EUA, famosos por não adotar o sistema métrico, definem a jarda e a libra pelo metro e pelo quilograma desde 1893. E até 2022 conviveram com dois \"pés\" oficiais, que diferiam uns 3 milímetros por milha.",
        "explicacao": (
            "Uma lei de 1866 já permitia, sem exigir, o uso do sistema métrico no país e trazia uma tabela de "
            "conversão. Os padrões de referência das unidades tradicionais eram uma jarda e uma libra vindas da "
            "Inglaterra, mas a jarda imperial de 1855 se mostrou instável, encolhendo de forma mensurável. Em 1890, "
            "chegaram aos EUA os metros e quilogramas feitos pelo BIPM, e o escritório de pesos e medidas, que já era "
            "praticamente forçado a usar os padrões métricos por serem mais estáveis, oficializou a troca. Em 5 de "
            "abril de 1893, Thomas Mendenhall, chefe do serviço geodésico americano, determinou que os padrões "
            "fundamentais de comprimento e massa passariam a ser o metro e o quilograma. A ordem não obrigava "
            "ninguém a abandonar polegadas e libras; só mudava a referência por trás delas. A jarda ficou valendo "
            "3.600/3.937 de metro. Em 1959, um acordo entre EUA, Reino Unido, Canadá, Austrália, Nova Zelândia e "
            "África do Sul fixou a jarda em 0,9144 m, o que criou um pé internacional ligeiramente diferente. Mas o mapeamento americano já "
            "tinha sido feito com o pé antigo, que foi mantido com o nome de pé de agrimensura. A diferença, de cerca "
            "de 3 milímetros por milha, é irrelevante num terreno pequeno, mas pesa em sistemas de coordenadas "
            "que se estendem por centenas de milhas. Só em 31 de dezembro de 2022 o NIST e outros órgãos federais "
            "declararam obsoleto o pé de agrimensura."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Mendenhall_Order",
                 "The Mendenhall Order marked a decision to change the fundamental standards of length and mass of the United States from the customary standards "
                 "based on those of England to metric standards. It was issued on April 5, 1893, by Thomas Corwin Mendenhall, superintendent of the United States "
                 "Coast and Geodetic Survey [...] "
                 "The Metric Act of 1866 was passed by Congress and allowed, but did not require, the use of the metric system. "
                 "Included in the law was a table of conversion factors between the traditional and metric units. [...] "
                 "The conversions were 1 yard = 3600⁄3937 meter [...] "
                 "the two meters and two kilograms allocated to the United States arrived in 1890, and were adopted as national standards. [...] "
                 "The imperial standard yard of 1855 was found to be unstable and shortening by measurable amounts. [...] "
                 "the Office of Weights and Measures was \"practically forced\" to use the metric standards because of their superior stability [...] "
                 "By the international yard and pound agreement of July 1, 1959, Australia, Canada, New Zealand, South Africa, the United Kingdom, "
                 "and the United States agreed that 1 yard = 0.9144 meter [...] "
                 "did not require anyone outside of the Office of Weights and Measures to change from the customary units to the metric system.",
                 nome="Mendenhall Order"),
            wiki("United_States_customary_units",
                 "The majority of U.S. customary units were redefined in terms of the meter and kilogram with the Mendenhall Order of 1893 [...] "
                 "this definition was retained for data derived from NAD27, but renamed the US survey foot to distinguish it from the international foot. "
                 "For most applications, the difference between the two definitions is insignificant – one international foot is exactly 0.999998 of a US survey foot, "
                 "for a difference of about [...] (3 mm) per mile – but it affects the definition of the State Plane Coordinate Systems (SPCSs), which can stretch over hundreds of miles.",
                 nome="United States customary units"),
            wiki("Foot_(unit)",
                 "The small difference between the survey foot and the international foot would not be detectable on a survey of a small parcel [...] "
                 "On December 31, 2022, the National Institute of Standards and Technology, the National Geodetic Survey, and the United States Department of Commerce "
                 "deprecated use of the US survey foot",
                 nome="Foot (unit)"),
        ],
    },
    # 6 O smoot, a unidade feita de um estudante
    {
        "temas_secundarios": ["personagens_esquecidos", "cidades"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Em 1958, como trote de fraternidade, um estudante do MIT mediu uma ponte deitando-se no chão várias vezes: deu 364,4 \"smoots\". A polícia passou a usar as marcas, e ele chegou a presidir a ISO, de normas técnicas.",
        "explicacao": (
            "Oliver Smoot queria entrar na fraternidade Lambda Chi Alpha, e a tarefa foi medir a ponte Harvard, entre "
            "Boston e Cambridge, usando a própria altura: 1,7018 m, ou 5 pés e 7 polegadas. Foi escolhido por ser o "
            "mais baixo, o que dava mais trabalho, e por ter o nome \"mais científico\". Ele se deitava, os colegas "
            "marcavam a posição com giz ou tinta, e ele se levantava de novo; quando cansou, passou a ser carregado de "
            "uma posição à outra. O resultado foi 364,4 smoots, \"mais ou menos uma orelha\", com a palavra orelha "
            "escrita com um épsilon, para indicar o erro possível. As marcas, pintadas a cada dez smoots, passaram a "
            "ser repintadas pela fraternidade. Nos anos 1980, quando a ponte foi reformada, a polícia de Cambridge "
            "pediu que elas fossem restauradas, porque eram usadas nos boletins de ocorrência para indicar locais na "
            "ponte. Os engenheiros ainda riscaram a calçada em intervalos de 5 pés e 7 polegadas, em vez dos 6 pés "
            "usuais. Smoot se formou em 1962, estudou direito e, ironicamente, presidiu o Instituto Nacional Americano "
            "de Padrões (ANSI) em 2001 e 2002 e a Organização Internacional de Normalização (ISO) em 2003 e 2004. "
            "Desde 2011, o Google Earth permite medir distâncias em smoots."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Smoot",
                 "created as part of an MIT fraternity pledge to Lambda Chi Alpha by Oliver R. Smoot, who in October 1958 lay down repeatedly on the Harvard Bridge "
                 "between Boston and Cambridge, Massachusetts, so that his fraternity brothers could use his height to measure the length of the bridge. [...] "
                 "One smoot is equal to Oliver Smoot's height at the time of the pledge, 5 feet 7 inches (1.7018 m). "
                 "The bridge's length was measured to be 364.4 smoots [...] \"± 1 εar\" with the \"±\" showing measurement uncertainty and \"ear\" spelled with an epsilon "
                 "to further indicate possible error in the measurement. [...] "
                 "Oliver R. Smoot was selected by his Lambda Chi Alpha fraternity pledgemaster because he was deemed shortest—which made measuring the bridge the most "
                 "labor-intensive—and he was the \"most scientifically named.\" Smoot repeatedly lay down on the bridge, let his companions mark his new position in chalk "
                 "or paint, and then got up again. Eventually, he wearied of the exercise and was carried thereafter by the fraternity brothers to each new position. "
                 "Smoot graduated from MIT in 1962, and then attended Georgetown University Law Center [...] "
                 "He served as chairman of the American National Standards Institute from 2001 to 2002, and then as president of the International Organization for "
                 "Standardization from 2003 to 2004. [...] "
                 "with a number every ten smoots. [...] "
                 "during bridge renovations in the 1980s, the Cambridge, Massachusetts, police department requested that the markings be restored, since they were "
                 "routinely used in police reports to identify locations on the bridge. The renovators at the Massachusetts Highway Department also scored the concrete "
                 "surface of the sidewalk on the bridge at 5-foot-7-inch (1.70 m) intervals instead of the conventional 6 feet (1.83 m). [...] "
                 "Starting in 2011, Google Earth enabled the ability to measure distance using smoots",
                 nome="Smoot"),
        ],
    },
    # 7 A velocidade da luz deixou de ser medida em 1983
    {
        "temas_secundarios": ["relatividade", "luz_cores"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Desde 1983, a velocidade da luz não é mais medida: ela vale exatamente 299.792.458 m/s por definição. Um experimento mais preciso não muda esse número; serve para realizar o metro com mais precisão.",
        "explicacao": (
            "Em 1960, o metro deixou de ser uma barra de metal e passou a ser definido por um número de comprimentos "
            "de onda de uma linha de emissão do criptônio-86. Em 1967, foi a vez de o segundo ganhar uma definição "
            "atômica, baseada no césio-133. Em 1972, com interferometria a laser e essas novas definições, um grupo "
            "do National Bureau of Standards dos EUA, em Boulder, no Colorado, mediu a velocidade da luz como "
            "299.792.456,2 m/s, com margem de 1,1 m/s, uma incerteza cem vezes menor que a do valor aceito até "
            "então. O que restava de incerteza vinha principalmente da própria definição do metro: a régua tinha "
            "ficado pior que o relógio. Em 1975, a Conferência Geral de Pesos e Medidas recomendou usar o valor "
            "299.792.458 m/s, e em 1983 a lógica se inverteu: o metro passou a ser a distância percorrida pela luz "
            "no vácuo numa fração exata de segundo. O valor escolhido concorda com as melhores medições anteriores a "
            "1983. Desde então, técnicas que antes serviriam para medir a velocidade da luz não alteram mais o seu "
            "valor no SI. Em vez disso, permitem realizar o metro com mais precisão, por exemplo medindo melhor o "
            "comprimento de onda do criptônio-86 e de outras fontes de luz."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Speed_of_light",
                 "In 1960, the metre was redefined in terms of the wavelength of a particular spectral line of krypton-86, and, in 1967, the second was redefined "
                 "in terms of the hyperfine transition frequency of the ground state of caesium-133. In 1972, using the laser interferometer method and the new "
                 "definitions, a group at the US National Bureau of Standards in Boulder, Colorado determined the speed of light in vacuum to be c = 299792456.2±1.1 m/s. "
                 "This was 100 times less uncertain than the previously accepted value. The remaining uncertainty was mainly related to the definition of the metre. "
                 "As similar experiments found comparable results for c, the 15th General Conference on Weights and Measures in 1975 recommended using the value "
                 "299792458 m/s for the speed of light. [...] "
                 "In 1983 the metre was defined as \"the length of the path travelled by light in vacuum during a time interval of [...] of a second\", fixing the value "
                 "of the speed of light at 299792458 m/s by definition [...] "
                 "The particular value adopted for the fixed speed of light in the current unit system was chosen to agree with the best measurements available before 1983. [...] "
                 "Improved experimental techniques that, prior to 1983, would have measured the speed of light no longer affect the known value of the speed of light "
                 "in SI units, but instead allow a more precise realization of the metre by more accurately measuring the wavelength of krypton-86 and other light sources.",
                 nome="Speed of light"),
            wiki("Metre",
                 "In 1799, the metre was redefined in terms of a prototype metre bar. The bar used was changed in 1889, and in 1960 the metre was redefined in terms "
                 "of a certain number of wavelengths of a certain emission line of krypton-86.",
                 nome="Metre"),
        ],
    },
    # 8 Huygens, o pêndulo e a "estranha simpatia"
    {
        "temas_secundarios": ["revolucao_cientifica", "invencoes"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "Huygens, inventor do relógio de pêndulo, notou que dois deles presos ao mesmo suporte acabavam balançando em sincronia, em sentidos opostos. A Royal Society registrou o caso como \"um estranho tipo de simpatia\".",
        "explicacao": (
            "Antes do pêndulo, os relógios mecânicos erravam cerca de 15 minutos por dia. Galileu tinha descoberto, "
            "por volta de 1602, que um pêndulo leva o mesmo tempo para ir e voltar qualquer que seja o tamanho do "
            "balanço. Inspirado nisso, o holandês Christiaan Huygens inventou o relógio de pêndulo em 25 de dezembro "
            "de 1656 e o patenteou no ano seguinte. O erro caiu para cerca de 15 segundos por dia, e muitos relógios "
            "antigos foram adaptados com pêndulos. Até os anos 1930, o relógio de pêndulo foi o marcador de tempo "
            "mais preciso do mundo. Huygens também percebeu que a regra de Galileu não é perfeita: balanços largos "
            "demoram um pouco mais que os estreitos. Mostrou, com geometria, que o peso teria de descrever uma "
            "ciclóide, e não um arco de círculo, para que o período não dependesse da amplitude. Foi estudando os "
            "seus relógios que observou as oscilações acopladas: dois deles, montados lado a lado no mesmo suporte, "
            "muitas vezes entravam em sincronia, balançando em sentidos opostos. Ele relatou o fenômeno por carta à "
            "Royal Society, e as atas da sociedade o chamam de \"um estranho tipo de simpatia\". Hoje o conceito é "
            "conhecido como arrastamento, em inglês entrainment."
        ),
        "nivel": 2, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Pendulum_clock",
                 "From its invention in 1656 by Christiaan Huygens, inspired by Galileo Galilei, until the 1930s, the pendulum clock was the world's most precise type of timekeeper. [...] "
                 "The pendulum clock was invented on 25 December 1656 by Dutch scientist and inventor Christiaan Huygens. The invention was patented the following year. [...] "
                 "Huygens was inspired by investigations of pendulums by Galileo Galilei in around 1602, who had discovered the key property that makes pendulums useful "
                 "timekeepers—they behave isochronically, so that they swing with a period that is independent of the size of the swing. [...] "
                 "Before the use of pendulums in clocks, they were accurate to about 15 minutes per day. The introduction of the pendulum, the first harmonic oscillator "
                 "used in timekeeping, increased their accuracy to 15 seconds per day, an improvement that led to their rapid spread. "
                 "Many existing \"verge and foliot\" clocks were fitted with pendulums.",
                 nome="Pendulum clock"),
            wiki("Christiaan_Huygens",
                 "Huygens's motivation came from the observation, made by Mersenne and others, that pendulums are not quite isochronous: their period depends on their "
                 "width of swing, with wide swings taking slightly longer than narrow swings. [...] "
                 "By geometrical methods which anticipated the calculus, Huygens showed it to be a cycloid, rather than the circular arc of a pendulum's bob, and therefore "
                 "that pendulums needed to move on a cycloid path in order to be isochronous. [...] "
                 "Huygens also observed coupled oscillations: two of his pendulum clocks mounted next to each other on the same support often became synchronized, "
                 "swinging in opposite directions. He reported the results by letter to the Royal Society, and it is referred to as \"an odd kind of sympathy\" in the "
                 "Society's minutes. This concept is now known as entrainment.",
                 nome="Christiaan Huygens"),
        ],
    },
    # 9 A candela, da vela de cachalote ao olho humano
    {
        "temas_secundarios": ["luz_cores", "sentidos", "vida_marinha"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "A candela, unidade de intensidade luminosa do SI, tem como ancestral a luz de uma vela de espermacete, a cera da cabeça do cachalote. Hoje ela é definida por uma luz verde e leva em conta a sensibilidade do olho humano.",
        "explicacao": (
            "Candela quer dizer \"vela\" em latim, e uma vela comum emite mais ou menos uma candela. Antes de 1948, "
            "cada país tinha o seu padrão de intensidade luminosa, em geral baseado na chama de uma \"vela padrão\" "
            "de composição definida ou num filamento incandescente. Um dos mais conhecidos era a vela inglesa: a luz "
            "de uma vela de espermacete puro, pesando um sexto de libra e queimando 120 grãos por hora. O espermacete "
            "é uma substância cerosa das cavidades da cabeça do cachalote, extraída por baleeiros desde o século XVII "
            "e usada justamente em velas de valor fotométrico padronizado. Alemanha, Áustria e países escandinavos "
            "preferiam a lâmpada de Hefner. Em 1884, Jules Violle propôs um padrão melhor, a luz de 1 cm² de platina "
            "no ponto de fusão, mas impurezas tornaram a ideia difícil de pôr em prática. A definição atual, em vigor "
            "desde 2019, fixa em 683 lúmens por watt a eficácia de uma radiação de 540 trilhões de hertz, uma luz verde de "
            "cerca de 555 nanômetros, a cor à qual o olho humano adaptado à claridade é mais sensível. Para as outras "
            "cores, cada comprimento de onda entra na conta com um peso dado por uma curva padronizada da "
            "sensibilidade do olho. Ou seja, a candela não mede só a energia da luz, mas quanto dela nós enxergamos."
        ),
        "nivel": 2, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Candela",
                 "A common wax candle has a luminous intensity of roughly 1 cd. The word candela is Latin for candle. [...] "
                 "Prior to 1948, various standards for luminous intensity were in use in a number of countries. These were typically based on the brightness of the "
                 "flame from a \"standard candle\" of defined composition, or the brightness of an incandescent filament of specific design. One of the best-known of "
                 "these was the English standard of candlepower. One candlepower was the light produced by a pure spermaceti candle weighing one sixth of a pound and "
                 "burning at a rate of 120 grains per hour. Germany, Austria and Scandinavia used the Hefnerkerze, a unit based on the output of a Hefner lamp. [...] "
                 "In 1884, Jules Violle had proposed a standard based on the light emitted by 1 cm2 of platinum at its melting point (or freezing point). [...] "
                 "Impurities on the surface of the platinum could directly affect its emissivity [...] "
                 "The new definition, which took effect on 20 May 2019, is: [...] "
                 "luminous efficacy of monochromatic radiation of frequency 540×1012 Hz, Kcd, to be 683 when expressed in the unit lm W−1 [...] "
                 "The frequency chosen is in the visible spectrum near green, corresponding to a wavelength of about 555 nanometres. The human eye, when adapted for "
                 "bright conditions, is most sensitive near this frequency. [...] "
                 "the contribution of each wavelength is weighted by the luminous efficiency function, the model of the sensitivity of the human eye to different "
                 "wavelengths, standardised by the CIE and ISO.",
                 nome="Candela"),
            wiki("Spermaceti",
                 "is a waxy substance found in the head cavities of the sperm whale [...] "
                 "It has been extracted by whalers since the 17th century for human use in cosmetics, textiles, and candles. [...] "
                 "The substance was also used in making candles of a standard photometric value",
                 nome="Spermaceti"),
        ],
    },
    # 10 O dia que fica mais longo: conchas fósseis e eclipses babilônicos
    {
        "temas_secundarios": ["paleontologia", "historia_astronomia", "sistema_solar"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "Conchas fósseis de 70 milhões de anos indicam que o ano tinha 372 dias, cada um com cerca de 23,5 horas. A Lua vem freando a Terra, e eclipses anotados por babilônios e chineses ajudam a medir o ritmo.",
        "explicacao": (
            "A atração da Lua deforma os oceanos e a parte sólida do planeta, criando bojos de maré. Como a Terra gira "
            "mais depressa do que a Lua dá a volta nela, esses bojos são levados um pouco à frente, e a linha que os "
            "une fica inclinada em relação à direção da Lua. O resultado é um torque que empurra a Lua em sua órbita e "
            "freia a rotação da Terra. Por isso, os dias eram mais curtos no passado. As camadas de crescimento de "
            "conchas de moluscos fósseis do fim do Cretáceo, de 70 milhões de anos atrás, indicam anos de 372 dias, "
            "e portanto dias de cerca de 23,5 horas. Sedimentos de maré de 620 milhões de anos são compatíveis com "
            "um dia de 21,9 horas. Para o passado recente, as pistas vêm da história: astrônomos babilônios e "
            "chineses registraram eclipses do Sol e da Lua desde o século VIII a.C. Como a hora e o lugar de um "
            "eclipse dependem da duração do dia, uma diferença de milissegundos por século vira, ao longo dos "
            "séculos, um erro de horas e de milhares de quilômetros nos cálculos. Esses registros indicam que o dia "
            "aumentou cerca de 2,3 milissegundos por século desde então. É por causa desse alongamento que os "
            "relógios atômicos e a rotação da Terra se afastam lentamente."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Tidal_acceleration",
                 "Analysis of layering in fossil mollusc shells from 70 million years ago, in the Late Cretaceous period, shows that there were 372 days a year, "
                 "and thus that the day was about 23.5 hours long then. [...] "
                 "Tidal rhythmites are alternating layers of sand and silt laid down offshore from estuaries having great tidal flows. [...] "
                 "This geological record is consistent with these conditions 620 million years ago: the day was 21.9±0.4 hours [...] "
                 "the water of the oceans bulges out both towards and away from the Moon. [...] In the solid Earth tides, there is a delayed response due to the dissipation of tidal energy. [...] "
                 "there is also a delay associated with the dissipation of energy since the Earth rotates at a faster rate than the Moon's orbital angular velocity. "
                 "This lunitidal interval in the responses causes the tidal bulge to be carried forward. Consequently, the line through the two bulges is tilted with "
                 "respect to the Earth-Moon direction exerting torque between the Earth and the Moon. This torque boosts the Moon in its orbit and slows the rotation of Earth. "
                 "As a result of this process, the mean solar day, which has to be 86,400 equal seconds, is actually getting longer when measured in SI seconds with stable atomic clocks.",
                 nome="Tidal acceleration"),
            wiki("Earth's_rotation",
                 "Earth's rotation is slowing slightly with time; thus, a day was shorter in the past. This is due to the tidal effects the Moon has on Earth's rotation. [...] "
                 "Analysis of historical astronomical records shows a slowing trend; the length of a day has increased by about 2.3 milliseconds per century since the 8th century BCE. [...] "
                 "There are recorded observations of solar and lunar eclipses by Babylonian and Chinese astronomers beginning in the 8th century BCE [...] "
                 "since the length of the day is a critical parameter in the calculation of the place and time of eclipses. A change in day length of milliseconds per "
                 "century shows up as a change of hours and thousands of kilometers in eclipse observations.",
                 nome="Earth's rotation"),
        ],
    },
    # 11 O incêndio das varetas que destruiu a jarda e a libra
    {
        "temas_secundarios": ["dinheiro", "falhas_engenharia"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Em 1834, a queima de velhas varetas de contabilidade do Tesouro inglês incendiou o Parlamento. No fogo sumiram a jarda e a libra-padrão do país, e o plano B previsto em lei para refazê-las não funcionou.",
        "explicacao": (
            "Desde a Idade Média, o Tesouro inglês registrava pagamentos e dívidas em varetas de madeira entalhadas, "
            "as tally sticks, partidas ao meio para que cada lado do acordo guardasse um registro. O sistema foi "
            "usado até 1826. Em 16 de outubro de 1834, dois operários passaram o dia queimando o estoque de varetas "
            "nas duas fornalhas de aquecimento sob a Câmara dos Lordes. Elas tinham sido projetadas para carvão, que "
            "dá muito calor e pouca chama, e não para madeira, que queima com chamas altas. O calor derreteu o "
            "revestimento de cobre dos dutos e iniciou um incêndio na chaminé, que se espalhou e destruiu a maior "
            "parte do Palácio de Westminster. Entre as perdas estavam os padrões britânicos da jarda e da libra. Uma "
            "lei de 1824 tinha previsto um acidente assim: além dos protótipos, definia constantes físicas para "
            "recriá-los, como o comprimento de um pêndulo que bate segundos na latitude de Greenwich e a massa de uma "
            "polegada cúbica de água destilada. Na prática, foi impossível refazer os padrões a partir dessas "
            "definições. Uma lei de 1855 autorizou recriar os protótipos a partir de cópias secundárias reconhecidas, "
            "e a perda levou a uma reforma do sistema britânico de pesos e medidas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Burning_of_Parliament",
                 "The Palace of Westminster, the medieval royal palace used as the home of the British parliament, was largely destroyed by fire on 16 October 1834. "
                 "The blaze was caused by the burning of small wooden tally sticks which had been used as part of the accounting procedures of the Exchequer until 1826. [...] "
                 "Since medieval times the Exchequer had used tally sticks, pieces of carved, notched wood, normally willow, as part of their accounting procedures. [...] "
                 "These sticks were split in two so that the two sides to an agreement had a record of the situation. [...] "
                 "instead opted to burn them in the two heating furnaces of the House of Lords, directly below the peers' chambers. "
                 "The furnaces had been designed to burn coal—which gives off a high heat with little flame—and not wood, which burns with a high flame. [...] "
                 "The process of destroying the tally sticks began at dawn on 16 October and continued throughout the day; two Irish labourers, Joshua Cross and "
                 "Patrick Furlong, were assigned the task. [...] "
                 "Those tending the furnaces were unaware that the heat from the fires had melted the copper lining of the flues and started a chimney fire. [...] "
                 "The British standard measurements, the yard and pound, were both lost in the blaze [...] "
                 "The destruction of the standard measurements led to an overhaul of the British weights and measures system.",
                 nome="Burning of Parliament"),
            wiki("Imperial_units",
                 "The 1824 Act of Parliament defined the yard, pound and gallon by reference to the prototype standards [...] and it also defined the values of certain "
                 "physical constants, to make provision for re-creation of the standards if they were to be damaged. For the yard, the length of a pendulum beating "
                 "seconds at the latitude of Greenwich at mean sea level in vacuo was defined as 39.1393 inches. For the pound, the mass of a cubic inch of distilled water [...] "
                 "Following the destruction of the original prototypes in the 1834 Houses of Parliament fire, it proved impossible to recreate the standards from these "
                 "definitions, and a new Weights and Measures Act 1855 was passed, which permitted the recreation of the prototypes from recognized secondary standards.",
                 nome="Imperial units"),
        ],
    },
    # 12 Ruth Belville, a mulher que vendia a hora
    {
        "temas_secundarios": ["personagens_esquecidos", "cidades"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Até 1940, uma mulher vendia a hora em Londres: Ruth Belville acertava o relógio de bolso em Greenwich e deixava os clientes conferirem os seus. O serviço da família tinha começado com o pai dela, em 1836.",
        "explicacao": (
            "John Henry Belville trabalhava no Observatório de Greenwich e, em 1836, criou um serviço para 200 "
            "clientes: toda manhã acertava o relógio pela hora média de Greenwich e saía de charrete para acertar os "
            "relógios dos assinantes. Quando ele morreu, em 1856, a viúva, Maria, recebeu o direito de continuar o "
            "trabalho como meio de vida e o manteve até se aposentar, em 1892, já na casa dos oitenta anos. A filha, Ruth, "
            "assumiu em seguida. O cliente olhava o relógio dela e ajustava o seu. Ela cobrava cerca de 4 libras por "
            "ano, menos que as 15 libras da assinatura do serviço de hora dos Correios. Em 1908, St John Wynne, "
            "diretor de uma empresa que vendia sinais de hora por telégrafo e principal concorrente dela, fez um "
            "discurso dizendo que os métodos de Ruth estavam ultrapassados e insinuando que ela usava a feminilidade "
            "para conseguir clientes. O Times publicou a fala sem mencionar que ele era concorrente. Repórteres a "
            "cercaram, as vendas subiram, e ela disse que Wynne só tinha lhe dado propaganda de graça. O relógio era "
            "um cronômetro de bolso de John Arnold, de 1794, que ela chamava de \"Mr. Arnold\". Tinha sido feito com "
            "caixa de ouro para o duque de Sussex, que o recusou por achá-lo parecido com um penico. Ruth trabalhou "
            "até 1940; aos 86 anos, ainda viajava cerca de doze milhas até o Observatório."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Ruth_Belville",
                 "also known as the Greenwich Time Lady, was a businesswoman from London. She, her mother Maria Elizabeth, and her father John Henry, sold people the time. "
                 "This was done by setting Belville's watch to Greenwich Mean Time, as shown by the Greenwich clock, each day and then \"selling\" people the time by letting "
                 "them look at the watch and adjust theirs. [...] "
                 "Ruth Belville's father, John Henry Belville (1795–1856), created a service for 200 clients in 1836. Each morning, John Henry went to Greenwich Observatory, "
                 "where he worked and set his watch to Greenwich Mean Time. He would then set off in his buggy and would set the clocks correctly for clients subscribed to the service. "
                 "John Henry continued this service until his death in 1856. His widow, Maria, was granted the privilege of carrying on the work as a means of livelihood and "
                 "continued the business until her retirement in 1892 when she was in her eighties. Ruth Belville then took over the business. She continued the business until 1940. "
                 "Belville charged approximately £4 per year [...] for her services, cheaper than the Post Office time subscription of £15. [...] "
                 "At the age of 86 she was still able to journey about twelve miles from her home and attend at the Observatory by 9 a.m. [...] "
                 "Belville's business came under attack in 1908 from St John Wynne, a director of the Standard Time Company, which sold a telegraphic time signal service and "
                 "was Belville's main competitor. Wynne made a speech at the city United Wards Club attacking Belville, claiming \"that her [Belville's] methods were amusingly "
                 "out of date\"; he also implied that she \"might have been using her femininity to gain business.\" "
                 "The speech was published in The Times newspaper, but the article did not mention the Standard Time Company or that Wynne was Belville's competitor. "
                 "Following the publication of the comments, Belville was besieged by reporters [...] the resulting publicity resulted in an increase in sales. "
                 "Belville said that all Wynne had managed to do was to give her free advertising. [...] "
                 "The watch used by the business was a 1794 John Arnold pocket chronometer [...] which Ruth Belville called \"Mr. Arnold\". "
                 "It had been made, with a gold case, for the Duke of Sussex, who rejected it because it \"looked like a bedpan\".",
                 nome="Ruth Belville"),
        ],
    },
    # 13 Horas que encolhiam no inverno: os relógios japoneses
    {
        "temas_secundarios": ["asia_antiga", "roma_antiga", "calendarios"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "No Japão, até 1873, as horas mudavam de tamanho com as estações: dia e noite tinham seis períodos cada. Os relojoeiros adaptaram os relógios europeus, e um modelo trocava sozinho o ritmo do dia pelo da noite.",
        "explicacao": (
            "A hora surgiu no antigo Oriente Próximo como uma fração variável do dia claro ou da noite, e não como "
            "uma duração fixa. Os romanos dividiam o dia claro em doze horas; nas latitudes do Mediterrâneo, uma hora durava "
            "cerca de 45 minutos no solstício de inverno e 75 no de verão. Na Europa, o relógio mecânico favoreceu "
            "a adoção de horas iguais. O Japão seguiu outro caminho. Francisco Xavier deu um relógio mecânico a um "
            "daimiô em 1551, e, com o isolamento do país a partir de 1641, os relojoeiros japoneses passaram a adaptar "
            "a tecnologia por conta própria ao sistema tradicional, que dividia o dia e a noite em seis períodos cada, "
            "mais longos de dia no verão e mais curtos no inverno. Assim nasceram os wadokei. Em alguns, a hora era "
            "indicada por um ponteiro preso ao peso que descia num trilho, ao lado de marcadores móveis ajustados "
            "conforme a estação. Por volta de 1780 surgiu o relógio de dois reguladores, que acertava sozinho o ritmo "
            "certo para o dia e para a noite. As horas eram numeradas de 9 a 4, em contagem regressiva, porque os "
            "primeiros marcadores de tempo japoneses queimavam incenso; os números 1, 2 e 3 ficavam de fora por "
            "motivos religiosos. Em 1873, o governo adotou as horas iguais e o calendário gregoriano."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Japanese_clock",
                 "is a mechanical clock that has been made to tell traditional Japanese time, a system in which daytime and nighttime are always divided into six periods "
                 "whose lengths consequently change with the season. [...] "
                 "at the start of the isolationist period in Japanese history, which began in 1641. [...] "
                 "Francis Xavier, a Spanish Society of Jesus saint and missionary, gave Ouchi Yoshitaka, a daimyō of the Sengoku period, a mechanical clock in 1551. [...] "
                 "Constant weight and dial adjustments led Japanese clock makers to develop the nichō-tenpu tokei [...] or \"two-bar governor clock\", around 1780. "
                 "The weights in the nichō-tempu tokei were automatically set for the correct time of day or night with the use of two governors or balances [...] "
                 "the daylight hours were longer in summer and shorter in winter, with the opposite at night. [...] "
                 "The typical clock had six numbered hours from 9 to 4, which counted backwards from noon until midnight; the hour numbers 1, 2, and 3 were not used "
                 "in Japan for religious reasons, because these numbers of strokes were used by Buddhists to call to prayer. The count ran backwards because the earliest "
                 "Japanese artificial timekeepers used the burning of incense to count down the time. [...] "
                 "The most practical way was with a pillar clock, where the clock indicated time not on a clock face, but on an indicator attached to a weight that "
                 "descended in a track. Movable time indicators ran alongside the track of the weight and its attached indicator. These indicators could be adjusted "
                 "for the seasons to show the length of the day and nighttime hours. [...] "
                 "In 1873 the Japanese government adopted Western style timekeeping practices, including equal hours that do not vary with the seasons, and the Gregorian calendar.",
                 nome="Japanese clock"),
            wiki("Roman_timekeeping",
                 "An hour was defined as one twelfth of the daytime, or the time elapsed between sunset and sunrise. Since the duration varied with the seasons, this also "
                 "meant that the length of the hour changed. [...] At Mediterranean latitude, one hour was about 45 minutes at the winter solstice, and 75 minutes at summer solstice.",
                 nome="Roman timekeeping"),
            wiki("Hour",
                 "The hour was initially established in the ancient Near East as a variable measure of [...] "
                 "These variable-length hours were variously known as temporal, unequal, or seasonal hours and were in use until the appearance of the mechanical clock, "
                 "which furthered the adoption of equal length hours.",
                 nome="Hour"),
        ],
    },
    # 14 Os fusos dos EUA foram obra das ferrovias
    {
        "temas_secundarios": ["transportes", "revolucao_industrial", "calendarios"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "Os fusos horários dos EUA foram criados em 1883 pelas ferrovias, e não pelo governo, justamente para evitar uma lei. Antes, uma só ferrovia tinha sete zonas de horário na linha. A lei só veio em 1918.",
        "explicacao": (
            "Até 1883, cada ferrovia americana escolhia o seu padrão de hora. Quase todas as que saíam de Nova York "
            "usavam a hora de Nova York, e as que iam de Chicago para o oeste, em geral, a de Chicago. Entre Chicago "
            "e Pittsburgh, o comum era a hora de Columbus, mesmo em linhas que não passavam por lá. A Northern "
            "Pacific tinha sete zonas de horário entre St. Paul e o fim da linha; a Union Pacific, só duas entre Omaha "
            "e Ogden. Desde 1870 havia propostas de fusos, como as de Charles Dowd. A associação das ferrovias temia "
            "que um sistema de hora padrão criado pelo governo saísse desvantajoso para elas, e o seu secretário, "
            "William F. Allen, defendeu que as próprias empresas adotassem cinco fusos, parecidos com os de hoje, "
            "para evitar a ação do governo. Em 11 de outubro de 1883, os chefes das grandes ferrovias aprovaram o "
            "plano num hotel de Chicago e combinaram que, no domingo, 18 de novembro, todas as ferrovias dos EUA e "
            "do Canadá acertariam os relógios por um sinal de telégrafo enviado do Observatório Allegheny, em "
            "Pittsburgh, ao meio-dia no meridiano 90. A maioria cumpriu a data; algumas mudaram antes e outras "
            "depois. A hora padrão só entrou na lei americana em 1918, numa lei que também criou o horário de verão."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Standard_time",
                 "Until 1883, each United States railroad chose its own time standards. [...] "
                 "However, almost all railroads out of New York ran on New York time, and railroads west from Chicago mostly used Chicago time, but between Chicago and "
                 "Pittsburgh/Buffalo the norm was Columbus time, even on railroads such as the PFtW&C and LS&MS, which did not run through Columbus. [...] "
                 "The Northern Pacific Railroad had seven time zones between St. Paul and the 1883 west end of the railroad at Wallula Jct; the Union Pacific Railway was "
                 "at the other extreme, with only two time zones between Omaha and Ogden. In 1870, Charles F. Dowd proposed four time zones [...] "
                 "became increasingly concerned that if the US government adopted a standard time scheme it would be disadvantageous to its member railroads. "
                 "William F. Allen, the Convention secretary, argued that North American railroads should adopt a five-zone standard, similar to the one in use today, "
                 "to avoid government action. On October 11, 1883, the heads of the major railroads met in Chicago at the Grand Pacific Hotel and agreed to adopt Allen's "
                 "proposed system. The members agreed that on Sunday, November 18, 1883, all United States and Canadian railroads would readjust their clocks and watches "
                 "to reflect the new five-zone system on a telegraph signal from the Allegheny Observatory in Pittsburgh at exactly noon on the 90th meridian. "
                 "Although most railroads adopted the new system as scheduled, some did so early on October 7 and others late on December 2. [...] "
                 "Standard time was not enacted into US law until the 1918 Standard Time Act established standard time in time zones; the law also instituted daylight saving time (DST).",
                 nome="Standard time"),
        ],
    },
]
