LOTE = "2026-11-25-historia_astronomia-01"
AREA = "espaco"
TEMA = "historia_astronomia"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


RBHC = "https://rbhciencia.emnuvens.com.br/rsbhc/article/download/566/493/1005"
RBHC_TITULO = "Tradições astronômicas tupinambás na visão de Claude D'Abbeville (Lima e Moreira, Revista da SBHC, 2005)"


CANDIDATOS = [
    # 1 o disco celeste de Nebra: saque, arcos dos solstícios e regra de calendário
    {
        "temas_secundarios": ["pre_historia", "calendarios", "crimes_arte"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "O disco de Nebra, de c. 1800–1600 a.C., é a mais antiga representação concreta de fenômenos astronômicos que se conhece. Foi achado por saqueadores, vendido no mercado negro e recuperado numa operação policial.",
        "explicacao": (
            "É um disco de bronze de uns 30 cm e 2,2 kg, com símbolos de ouro: o Sol ou a lua cheia, um crescente "
            "e estrelas, entre elas um grupo de sete pontos lido como as Plêiades. Mais tarde, alguém acrescentou "
            "dois arcos dourados nas bordas. Eles abrangem 82°, exatamente o ângulo entre os pontos onde o Sol se põe "
            "nos solstícios de verão e de inverno na latitude do local, 51° N. Há também uma leitura mais ousada: o "
            "crescente ao lado das Plêiades seria uma regra para encaixar um mês extra e acertar o calendário lunar "
            "com o solar. Essa regra aparece num compêndio babilônico, o MUL.APIN, de c. 700 a.C., embora alguns "
            "assiriólogos e astrônomos rejeitem a comparação. A história moderna do disco é policial. Em 1999, dois "
            "caçadores de tesouros sem licença o acharam com um detector de metais, danificaram-no com a pá e, no dia "
            "seguinte, venderam o lote por 31 mil marcos. Em fevereiro de 2002, o arqueólogo estadual Harald Meller "
            "o recuperou numa armadilha montada pela polícia em Basileia, diante de um casal que pedia 700 mil marcos. "
            "Num acordo judicial, os saqueadores levaram policiais e arqueólogos ao local do achado."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Nebra_sky_disc",
            "is a bronze disc of around 30 cm (12 in) diameter and a weight of 2.2 kg (4.9 lb), having a blue-green patina and inlaid with gold symbols. "
            "These symbols are interpreted generally as the Sun or full moon, a lunar crescent, and stars, including a cluster of seven stars, axiomatically interpreted as the Pleiades. [...] "
            "It is dated by archaeologists to c. 1800–1600 BC [...] "
            "The Nebra sky disc features the oldest concrete depiction of astronomical phenomena known from anywhere in the world. [...] "
            "discovered in 1999 by Henry Westphal and Mario Renner while they were treasure-hunting with a metal detector. "
            "The detectorists were operating without a license and knew their activity constituted looting and was illegal. [...] "
            "They damaged the disc with their spade and destroyed parts of the site. "
            "The next day, Westphal and Renner sold the entire hoard for 31,000 DM to a dealer in Cologne. [...] "
            "In February 2002, the state archaeologist, Harald Meller, acquired the disc in a police-led sting operation in Basel from a couple who had put it on the black market for 700,000 DM. "
            "The original finders were eventually traced. In a plea bargain, they led police and archaeologists to the discovery site. [...] "
            "At some later date, two arcs (constructed from gold of different origins, as shown by their chemical impurities) were added at opposite edges of the disc. [...] "
            "The two arcs span an angle of 82°, correctly indicating the angle between the positions of sunsets at summer and winter solstice as seen at the latitude of the Mittelberg (51°N). [...] "
            "The depiction of the Pleiades on the disc in conjunction with a crescent moon is thought to represent a calendar rule for synchronising solar and lunar calendars [...] "
            "This rule is known from an ancient Babylonian collection of texts with the title MUL.APIN, dating from c. 700 BC. "
            "According to one of the seven rules in the compendium, a leap month should be added when the Pleiades appear next to a crescent moon a few days old in the spring, as depicted on the disc. [...] "
            "However some Assyriologists and astronomers have rejected the comparison of the Nebra Disc with MUL.APIN.",
            nome="Nebra sky disc")],
    },
    # 2 a estrela hóspede de 1054 e o M1 de Messier
    {
        "temas_secundarios": ["estrelas", "asia_antiga", "asteroides_cometas"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "Em 1054, astrônomos chineses registraram uma \"estrela hóspede\" visível de dia por 23 dias. Seus restos são a Nebulosa do Caranguejo, o primeiro item de um catálogo feito para não confundir nebulosas com cometas.",
        "explicacao": (
            "Os chineses chamavam de \"estrelas hóspedes\" os pontos de luz que surgiam no céu por um tempo. A de 1054, "
            "no reinado do imperador Renzong, da dinastia Song, foi descrita como vista à luz do dia, \"como Vênus\", "
            "branco-avermelhada e com raios em todas as direções. Esse brilho diurno durou 23 dias, e a estrela ficou "
            "visível no total por 642 dias, até abril de 1056. Os relatos chineses dão a posição com precisão de um "
            "grau, enquanto os possíveis registros europeus são vagos, e a falta deles na Europa intriga há tempos. "
            "Séculos depois, em 1758, o francês Charles Messier esperava a volta do cometa Halley e confundiu com ele "
            "uma mancha difusa no céu. Como só queria achar cometas, passou a listar os objetos nebulosos que "
            "atrapalhavam a busca, e a mancha virou o primeiro item: M1. Em 1928, Edwin Hubble notou que a nebulosa "
            "crescia num ritmo compatível com uma explosão de uns nove séculos antes e a ligou à estrela hóspede. Em "
            "1942, Jan Oort e Nicholas Mayall deixaram a identificação fora de dúvida razoável. Hoje se sabe que foi "
            "uma supernova, e o núcleo da estrela que explodiu virou um pulsar."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("SN_1054",
                "SN 1054, the Crab Supernova, is a supernova that was first observed on c. 10 July [O.S. c. 4 July] 1054, and remained visible until c. 12 April [O.S. c. 6 April] 1056. [...] "
                "The event was recorded in contemporary Chinese astronomy [...] "
                "The remnant of SN 1054, which consists of debris ejected during the explosion, is known as the Crab Nebula. [...] "
                "The core of the exploding star formed a pulsar, called the Crab Pulsar [...] "
                "When the French astronomer Charles Messier watched for the return of Halley's Comet in 1758, he confused the nebula for the comet, as he was unaware of the former's existence. "
                "Motivated by this error, he created his catalogue of non-cometary nebulous objects, the Messier Catalogue, to avoid such mistakes in the future. "
                "The nebula is catalogued as the first Messier object, or M1. [...] "
                "In 1928, Edwin Hubble was the first to note that the changing aspect of the Crab Nebula, which was growing bigger in size, suggests that it is the remains of a stellar explosion. "
                "He realised that the apparent speed of change in its size signifies that the explosion which it comes from occurred only nine centuries ago [...] "
                "This deduction was subsequently refined, which pushed Mayall and Jan Oort in 1942 to analyse historic accounts relating to the guest star more closely [...] "
                "the identification of the guest star of 1054 is established beyond all reasonable doubt. [...] "
                "Star-like objects that appeared temporarily in the sky were generically called \"guest stars\" (kè xīng 客星) by Chinese astronomers. "
                "The guest star of 1054 occurred during the reign of the Emperor Renzong of the Song dynasty (960–1279). [...] "
                "The last sighting was on 6 April 1056, after a total period of visibility of 642 days. [...] "
                "It had been seen in daylight, like Venus. It had rays stemming in all directions, and its colour was reddish white. Altogether visible for 23 days. [...] "
                "In contrast, the Chinese accounts pin-point within a degree where the supernova occurred [...] "
                "The lack of accounts from European chroniclers has long raised questions.",
                nome="SN 1054"),
            wiki("Messier_object",
                "Because Messier was interested only in finding comets, he created a list of those non-comet objects that frustrated his hunt for them.",
                nome="Messier object"),
        ],
    },
    # 3 Williamina Fleming e o "alfabeto" fora de ordem das estrelas
    {
        "temas_secundarios": ["estrelas", "personagens_esquecidos"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "As classes das estrelas, O B A F G K M, estão fora da ordem alfabética porque nasceram como letras de A a Q, ordenadas pelo hidrogênio. Uma das criadoras tinha sido empregada doméstica do diretor do observatório.",
        "explicacao": (
            "Williamina Fleming emigrou da Escócia para Boston em 1878, aos 21 anos. Abandonada pelo marido, com um "
            "filho pequeno, foi trabalhar como empregada na casa de Edward Pickering, diretor do Observatório do "
            "Harvard College. Por recomendação da mulher dele, foi contratada em 1879 para tarefas administrativas e, "
            "em 1881, aprendeu a analisar espectros de estrelas. Virou uma das fundadoras das \"computadoras de "
            "Harvard\", equipe só de mulheres que examinava chapas fotográficas por um salário de trabalhador não "
            "qualificado, em geral de 25 a 50 centavos de dólar por hora. Com Pickering, ela separou as estrelas pela "
            "intensidade das linhas do hidrogênio: A para as de linhas mais fortes, B para as seguintes, e assim por "
            "diante, até P, mais Q para as que não se encaixavam. Fleming classificou a maior parte dos espectros do "
            "primeiro catálogo Henry Draper, de 1890, com mais de 10 mil estrelas, e em 1888 descobriu a Nebulosa "
            "Cabeça de Cavalo. Em 1901, a colega Annie Jump Cannon reordenou o sistema pela temperatura da superfície: "
            "descartou quase todas as letras e ficou com O, B, A, F, G, K e M, nessa ordem. Em 1922, a União "
            "Astronômica Internacional adotou a versão de Cannon como oficial."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Williamina_Fleming",
                "In 1878, aged 21, she and her husband emigrated to Boston, Massachusetts, US. "
                "After her husband abandoned her and their young son, she worked as a maid in the home of Professor Edward Charles Pickering, the director of the Harvard College Observatory (HCO). "
                "Pickering's wife Elizabeth recommended Williamina as having talents beyond custodial and maternal arts, and in 1879, Pickering hired Fleming to conduct part-time administrative work at the observatory. "
                "In 1881, Pickering formally invited Fleming to join the HCO and taught her how to analyze stellar spectra. "
                "She became one of the founding members of the Harvard Computers, an all-women cadre of human computers [...] "
                "Stars showing hydrogen as the most abundant element were classified A; those of hydrogen as the second-most abundant element, B; and so on. "
                "Later, her colleague Annie Jump Cannon reordered the classification system based on the surface temperature of stars [...] "
                "She is credited with the discovery of the Horsehead Nebula in 1888",
                nome="Williamina Fleming"),
            wiki("Stellar_classification",
                "an early result of this work was the first edition of The Henry Draper Memorial Catalogue of Stellar Spectra, first published in 1890. "
                "Williamina Fleming classified most of the spectra in the first edition of the catalogue and is credited with classifying over 10,000 featured stars [...] "
                "given letters from A to P. Also, the letter Q was used for stars not fitting into any other class. "
                "Fleming worked with Pickering to differentiate 17 different classes based on the intensity of hydrogen spectral lines [...] "
                "In 1901, Annie Jump Cannon returned to the lettered types, but dropped all letters except O, B, A, F, G, K, M, and N used in that order",
                nome="Stellar classification"),
            wiki("Harvard_Computers",
                "Although some of Pickering's female staff were astronomy graduates, their wages were similar to those of unskilled workers. "
                "They usually earned between 25 and 50 cents per hour [...] "
                "in 1922, the International Astronomical Union adopted [Cannon's] as the official classification system for stars",
                nome="Harvard Computers"),
        ],
    },
    # 4 Henrietta Leavitt e a régua das galáxias
    {
        "temas_secundarios": ["galaxias", "estrelas", "personagens_esquecidos"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Henrietta Leavitt criou a régua das distâncias até outras galáxias com uma ideia simples: estrelas de uma mesma nuvem estão quase à mesma distância de nós. Em 1924, quiseram indicá-la ao Nobel; ela morrera em 1921.",
        "explicacao": (
            "Leavitt era uma das \"computadoras\" do Observatório do Harvard College: media chapas fotográficas para "
            "catalogar a posição e o brilho de estrelas. Ela foi perdendo a audição até ficar surda. Estudando chapas "
            "das Nuvens de Magalhães feitas na estação de Harvard em Arequipa, no Peru, identificou 1.777 estrelas "
            "variáveis e notou que, entre as chamadas cefeidas, as mais brilhantes tinham períodos mais longos. Na "
            "época, distâncias de estrelas só eram medidas pela paralaxe, que alcança algumas centenas de anos-luz. O "
            "pulo do gato: ninguém sabia a distância da Pequena Nuvem de Magalhães, mas todas as suas estrelas estão "
            "mais ou menos à mesma distância. Então a relação entre período e brilho aparente valia também para o "
            "brilho real. Num artigo de 1912, com 25 cefeidas, ela mostrou a relação; o texto saiu assinado por "
            "Pickering, mas a primeira frase diz que foi \"preparado pela senhorita Leavitt\". Calibrada com a "
            "paralaxe de uma cefeida próxima, a relação virou uma régua de alcance enorme. Depois da morte dela, "
            "Hubble achou cefeidas em Andrômeda e mostrou que essas nebulosas eram galáxias separadas. Ele dizia "
            "que Leavitt merecia o Nobel. Em 1924, Gösta Mittag-Leffler, da Academia Sueca de Ciências, tentou "
            "indicá-la e soube que ela morrera de câncer três anos antes."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Henrietta_Swan_Leavitt",
            "December 12, 1921) was an American astronomer. [...] "
            "she worked at the Harvard College Observatory as a human computer, tasked with measuring photographic plates to catalog the positions and brightness of stars. "
            "This work led her to discover the relation between the luminosity and the period of Cepheid variables. [...] "
            "the distance to a star were based on stellar parallax. Such techniques can only be used for measuring distances out to several hundred light years. "
            "Leavitt's great insight was that while no one knew the distance to the Small Magellanic Cloud, all its stars must be roughly the same distance from Earth. "
            "Therefore, a relationship she discovered in it, between the period of certain variable stars (Cepheids) and their apparent brightness, reflected a relationship in their absolute brightness. "
            "Once calibrated by measuring the distance to a nearby star of the same type via parallax, her discovery became a measuring stick with vastly greater reach. "
            "After Leavitt's death, Edwin Hubble found Cepheids in several nebulae, including the Andromeda Nebula, and, using Leavitt's Law, calculated that their distance was far too great to be part of the Milky Way and were separate galaxies in their own right. [...] "
            "Leavitt gradually became deaf. [...] "
            "as recorded on photographic plates taken with the Bruce Astrograph of the Boyden Station of the Harvard Observatory in Arequipa, Peru. "
            "She identified 1,777 variable stars. "
            "In 1908, Leavitt published the results of her studies in the Annals of the Astronomical Observatory of Harvard College, noting that the brighter variables had the longer period. "
            "In a 1912 paper, Leavitt examined the relationship between the periods and the brightness of a sample of 25 of the Cepheid variables in the Small Magellanic Cloud. "
            "The paper was communicated and signed by Edward Pickering, but the first sentence indicates that it was \"prepared by Miss Leavitt\". [...] "
            "Hubble often said that Leavitt deserved the Nobel Prize for her work. "
            "Mathematician Gösta Mittag-Leffler, a member of the Swedish Academy of Sciences, tried to nominate her for that prize in 1924, only to learn that she had died of cancer three years earlier.",
            nome="Henrietta Swan Leavitt")],
    },
    # 5 o nariz de Tycho Brahe e a exumação
    {
        "temas_secundarios": ["revolucao_cientifica", "minerais_rochas"],
        "tipos_espanto": ["historia_humana", "mito_desmentido"],
        "gancho": "Tycho Brahe perdeu parte do nariz num duelo, aos 20 anos, após discutir quem era o melhor matemático. A prótese seria de ouro e prata, mas a exumação de 2010 apontou latão e descartou a tese de que ele foi envenenado.",
        "explicacao": (
            "Em dezembro de 1566, quando estudava em Rostock, o jovem nobre dinamarquês brigou bêbado, numa festa de "
            "noivado, com um primo de terceiro grau, Manderup Parsberg: o tema era qual dos dois era o matemático "
            "superior. No dia 29, resolveram a questão num duelo no escuro. Tycho perdeu a ponte do nariz e ganhou uma "
            "cicatriz larga na testa, embora os dois tenham feito as pazes depois. Pelo resto da vida, usou uma "
            "prótese presa com pasta ou cola, que se dizia ser de prata e ouro. A morte dele também virou enigma. "
            "Investigações dos anos 1990 sugeriram envenenamento por mercúrio, e surgiram suspeitos: o assistente "
            "Johannes Kepler, interessado no laboratório e nos dados do mestre, e um primo, Erik Brahe. Em novembro "
            "de 2010, cientistas tchecos e dinamarqueses exumaram o corpo em Praga e colheram ossos, pelos e tecido "
            "das roupas. Em 2012, relataram que a prótese era de latão, pela análise química de um fragmento de osso "
            "do nariz, e que não havia mercúrio suficiente para sustentar um assassinato, nem veneno em nível letal. "
            "A conclusão foi taxativa: \"é impossível que Tycho Brahe tenha sido assassinado\". Avaliações médicas "
            "modernas apontam como causa mais provável um problema na bexiga ou na próstata que levou à retenção "
            "urinária."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Tycho_Brahe",
            "On 29 December 1566 at the age of 20, Tycho lost part of his nose in a sword duel with a fellow Danish nobleman, his third cousin Manderup Parsberg. "
            "At an engagement party at the home of Professor Lucas Bachmeister on 10 December the two had drunkenly quarreled over who was the superior mathematician. "
            "On 29 December, the cousins resolved their feud with a duel in the dark. "
            "Though the two were later reconciled, in the duel Tycho lost the bridge of his nose and gained a broad scar across his forehead. "
            "He received the best possible care at the university and wore a prosthetic nose for the rest of his life. "
            "It was kept in place with paste or glue and said to be made of silver and gold. "
            "In November 2012, Danish and Czech researchers reported that the prosthesis was actually made of brass after chemically analyzing a small bone sample from the nose from the body exhumed in 2010. [...] "
            "Modern medical assessment is that his death was more likely caused by either a burst bladder, prostatic hypertrophy, acute prostatitis, or prostate cancer, which led to urinary retention, overflow incontinence, and uremia. "
            "Investigations in the 1990s suggested that Tycho may not have died from urinary problems, but instead from mercury poisoning. "
            "It was speculated that he had been intentionally poisoned. "
            "The two main suspects were his assistant, Johannes Kepler, whose motives would be to gain access to Tycho's laboratory and chemicals, and his cousin, Erik Brahe [...] "
            "In February 2010, the Prague city authorities approved a request by Danish scientists to exhume the remains, and in November 2010 a group of Czech and Danish scientists from Aarhus University collected bone, hair and clothing samples for analysis. [...] "
            "The team reported in November 2012 that there was not enough mercury present to substantiate murder, and there were no lethal levels of any poisons present. "
            "The team's conclusion was that \"it is impossible that Tycho Brahe could have been murdered\".",
            nome="Tycho Brahe")],
    },
    # 6 a paralaxe que não aparecia e a aberração da luz
    {
        "temas_secundarios": ["revolucao_cientifica", "luz_cores", "estrelas"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Por séculos, um argumento contra a Terra girar em torno do Sol foi que as estrelas não mudavam de posição ao longo do ano. Buscando esse efeito, James Bradley achou outro, que provou que a Terra se move.",
        "explicacao": (
            "Se a Terra dá a volta no Sol, as estrelas mais próximas deveriam parecer oscilar um pouco ao longo do "
            "ano, vistas de pontos opostos da órbita: é a paralaxe estelar. Ninguém conseguia detectá-la, e essa "
            "ausência foi usada como argumento contra o heliocentrismo. Para Tycho Brahe, era uma objeção central: "
            "conciliar Copérnico com a falta de paralaxe exigiria um vazio enorme e improvável entre a órbita de "
            "Saturno e a esfera das estrelas. A resposta copernicana era essa mesma: as estrelas estariam longe "
            "demais. James Bradley e Samuel Molyneux tentaram medir a paralaxe da estrela Gama Draconis. Acharam um "
            "vaivém anual, mas com o calendário errado: o ponto mais ao sul vinha em março, e não em dezembro, como a "
            "paralaxe exigiria. Bradley entendeu que se tratava da aberração da luz, causada pela velocidade finita "
            "da luz somada ao movimento da Terra na órbita. Para todos os efeitos práticos, era uma prova "
            "conclusiva de que a Terra se move, anunciada à Royal Society em janeiro de 1729. A paralaxe em si, "
            "minúscula, só foi medida entre 1832 e 1838, por Thomas Henderson, Friedrich von Struve e Friedrich "
            "Bessel, nas estrelas Alfa Centauri, Vega e 61 Cygni."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Stellar_parallax",
                "Thomas Henderson, Friedrich Georg Wilhelm von Struve, and Friedrich Bessel made the first successful parallax measurements in 1832–1838, for the stars Alpha Centauri, Vega, and 61 Cygni. [...] "
                "Stellar parallax is so small that it was unobservable until the 19th century, and its apparent absence was used as a scientific argument against heliocentrism during the early modern age. "
                "It is clear from Euclid's geometry that the effect would be undetectable if the stars were far enough away, but for various reasons, such gigantic distances involved seemed entirely implausible: "
                "it was one of Tycho Brahe's principal objections to Copernican heliocentrism that for it to be compatible with the lack of observable stellar parallax, there would have to be an enormous and unlikely void between the orbit of Saturn and the eighth sphere (the fixed stars).",
                nome="Stellar parallax"),
            wiki("Tycho_Brahe",
                "Tycho believed that, if the Earth did orbit the Sun, there should be an observable stellar parallax every six months [...] "
                "The lack of any stellar parallax was explained by the Copernican theory as being due to the stars' enormous distances from Earth.",
                nome="Tycho Brahe"),
            wiki("James_Bradley",
                "the aberration of light (1725–1728) [...] "
                "Bradley's discovery of the aberration of light was made while attempting to detect stellar parallax. "
                "Bradley worked with Samuel Molyneux until Molyneux's death in 1728, trying to measure the parallax of Gamma Draconis. [...] "
                "Calculation showed that if there had been any appreciable motion due to parallax, then the star should have reached its most southerly apparent position in December, and its most northerly apparent position in June. "
                "What Bradley found instead was an apparent motion that reached its most southerly point in March, and its most northerly point in September [...] "
                "This discovery of what became known as the aberration of light was, for all realistic purposes, conclusive evidence for the movement of the Earth, and hence for the correctness of Aristarchus', Copernicus', and Kepler's theories; "
                "it was announced to the Royal Society in January 1729.",
                nome="James Bradley"),
            wiki("Aberration_(astronomy)",
                "who attributed it to the finite speed of light and the motion of Earth in its orbit around the Sun.",
                nome="Aberration (astronomy)"),
        ],
    },
    # 7 Le Gentil, o azarado dos trânsitos de Vênus
    {
        "temas_secundarios": ["sistema_solar", "grandes_navegacoes", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Um astrônomo francês passou 11 anos fora tentando ver dois trânsitos de Vênus e perdeu os dois. De volta a Paris, soube que fora declarado morto, que a mulher se casara de novo e que os parentes saquearam seus bens.",
        "explicacao": (
            "Edmond Halley tinha sugerido medir a distância da Terra ao Sol observando, de pontos distantes do "
            "planeta, a passagem de Vênus diante do Sol. Esses trânsitos vêm em pares separados por oito anos, e "
            "cada par fica a 105 ou 121 anos do seguinte. Para o de 1761, mais de cem observadores foram espalhados "
            "pelo mundo. Guillaume Le Gentil saiu de Paris em março de 1760 rumo a Pondicherry, possessão francesa na "
            "Índia. A Guerra dos Sete Anos atrapalhou a viagem e, quando o navio enfim se aproximou, os britânicos "
            "tinham ocupado a cidade. No dia do trânsito o céu estava limpo, mas ele continuava no mar, num navio "
            "que jogava demais para qualquer medição. Decidiu esperar o de 1769. Mapeou a costa de Madagascar, "
            "tentou Manila, foi hostilizado pelas autoridades espanholas e voltou a Pondicherry, já devolvida à "
            "França, onde montou um pequeno observatório. Em 4 de junho de 1769, o céu nublou e ele não viu nada. "
            "Na volta, teve disenteria e uma tempestade o deixou na ilha Bourbon. Chegou a Paris em outubro de "
            "1771: suas cartas tinham se perdido em naufrágios e ataques, e seu lugar na Academia de Ciências fora "
            "ocupado. Só com longos processos e a intervenção do rei recuperou a cadeira."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Guillaume_Le_Gentil",
            "made unsuccessful attempts to observe the 1761 and 1769 transits of Venus from India during an 11-year journey from France [...] "
            "Edmond Halley had suggested the idea, but it required careful measurements from different places on earth, and the project was launched with more than a hundred observers dispatched to different parts of the globe to observe the transit coming up in 1761. "
            "As a part of the French expedition, Le Gentil set out for Pondicherry, a French possession in India. "
            "He set out from Paris in March 1760, and reached Isle de France (now Mauritius) in July. "
            "However, the Seven Years' War had broken out between France and Britain in the meantime, hindering further passage east. [...] "
            "By the time it finally got close to Pondicherry, the captain learned that the British had occupied the city, so the frigate was obliged to return to Isle de France. "
            "When 6 June came the sky was clear, but the ship was still at sea, and he could not take astronomical observations with the vessel rolling about. "
            "Having already completed the trip from Paris, he stayed for the next transit of Venus, which would come in another eight years (they occur in pairs 8 years apart, but each pair is separated from the next by 121 or 105 years). "
            "After spending some time mapping the eastern coast of Madagascar, he decided to record the 1769 transit from Manila in the Philippines. "
            "Encountering hostility from the Spanish authorities there, he headed back to Pondicherry, which had been restored to France by peace treaty in 1763, where he arrived in March 1768. "
            "He built a small observatory to view the transit. On the day of the event, 4 June 1769, the sky became overcast, and Le Gentil saw nothing. "
            "The return trip was first delayed by dysentery, and further when his ship was caught in a storm and dropped him off at Île Bourbon (Réunion) [...] "
            "He finally arrived in Paris in October 1771, having been away for eleven years, only to find that he had been declared legally dead and been replaced in the Royal Academy of Sciences. "
            "His wife had remarried, and all his relatives had \"enthusiastically plundered his estate\". "
            "Due to shipwrecks and wartime attacks on ships, none of the letters he had sent to the academy or to his relatives had reached their destinations. "
            "Lengthy litigation and the intervention of the king were ultimately required before he recovered his seat in the academy",
            nome="Guillaume Le Gentil")],
    },
    # 8 Urano, a "Estrela de Jorge"
    {
        "temas_secundarios": ["sistema_solar", "elementos_quimicos", "mitologia"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "Urano quase se chamou \"Estrela de Jorge\": Herschel o batizou em honra do rei Jorge III, e o almanaque náutico britânico só trocou o nome em 1850. E o planeta já tinha sido anotado como estrela dezenas de vezes antes.",
        "explicacao": (
            "Em 13 de março de 1781, William Herschel observava do jardim de casa, em Bath, na Inglaterra, quando "
            "notou um objeto que anotou como \"estrela nebulosa ou talvez um cometa\". Dias depois, como ele mudara "
            "de lugar, concluiu que era cometa. Mas Anders Lexell calculou a órbita, quase circular, e ela indicava "
            "um planeta: pela primeira vez na história, os limites conhecidos do Sistema Solar se ampliavam. Urano é "
            "visível a olho nu, porém fraco e lento, e já tinha sido registrado sem ser reconhecido: James Bradley o "
            "viu três vezes, e o francês Pierre Le Monnier, pelo menos doze, entre 1750 e 1769. Jorge III deu a "
            "Herschel uma pensão anual de 200 libras, com a condição de que ele se mudasse para Windsor. Herschel "
            "retribuiu com o nome Georgium Sidus, a \"Estrela de Jorge\", para que no futuro se dissesse que o "
            "planeta foi achado \"no reinado do rei Jorge III\". Fora da Grã-Bretanha, a ideia não pegou: Lalande "
            "sugeriu \"Herschel\", e houve quem propusesse \"Netuno\". Em 1782, Johann Bode propôs Urano, o deus "
            "grego do céu: assim como Saturno era pai de Júpiter, o novo planeta levaria o nome do pai de Saturno. "
            "Em 1789, Martin Klaproth batizou o recém-descoberto urânio em apoio a Bode."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Uranus",
            "William Herschel first observed Uranus on 13 March 1781, leading to its discovery as a planet, expanding the known boundaries of the Solar System for the first time in history [...] "
            "James Bradley observed it three times, in 1748, 1750, and 1753. [...] "
            "The French astronomer Pierre Charles Le Monnier observed Uranus at least twelve times between 1750 and 1769, including on four consecutive nights. "
            "William Herschel observed Uranus on 13 March 1781 from the garden of his house at 19 New King Street in Bath, Somerset, England [...] "
            "Herschel recorded in his journal: \"In the quartile near ζ Tauri ... either [a] Nebulous star or perhaps a comet.\" "
            "On 17 March he noted: \"I looked for the Comet or Nebulous Star and found that it is a Comet, for it has changed its place.\" [...] "
            "Anders Johan Lexell, working in Russia, was the first to compute the orbit of the new object. "
            "Its nearly circular orbit suggested that it was a planet rather than [...] "
            "Like the classical planets, Uranus is visible to the naked eye, but it was never recognised as a planet by ancient observers because of its dimness and slow orbit. [...] "
            "King George III gave Herschel an annual stipend of £200 (equivalent to £26,000 in 2025) on condition that he move to Windsor [...] "
            "Herschel decided to name the object Georgium Sidus (George's Star), or the \"Georgian Planet\", in honour of his new patron, King George III. [...] "
            "It would be a very satisfactory answer to say, 'In the reign of King George the Third'. "
            "Herschel's proposed name was not popular outside Britain and Hanover, and alternatives were soon proposed. "
            "The astronomer Jérôme Lalande proposed that it be named Herschel in honour of its discoverer. [...] "
            "Neptune was supported by other astronomers who liked the idea of commemorating the victories of the British Royal Naval fleet [...] "
            "In a March 1782 treatise, Johann Elert Bode proposed Uranus, the Latinised version of the Greek god of the sky, Ouranos. [...] "
            "just as Saturn was the father of Jupiter, the new planet should be named after the father of Saturn. [...] "
            "In 1789, Bode's Royal Academy colleague Martin Klaproth named his newly discovered element uranium in support of Bode's choice. "
            "Ultimately, Bode's suggestion became the most widely used, and became universal in 1850 when HM Nautical Almanac Office, the final holdout, switched from using Georgium Sidus to Uranus.",
            nome="Uranus")],
    },
    # 9 Galileu viu Netuno em 1612
    {
        "temas_secundarios": ["sistema_solar", "revolucao_cientifica"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Galileu viu Netuno em 1612, mais de dois séculos antes da descoberta, e o desenhou como estrela. Deu azar: naquela noite o planeta parecia parado no céu, porque começava justo ali seu movimento retrógrado.",
        "explicacao": (
            "Netuno nunca fica mais brilhante que a magnitude 7,7, fraco demais para o olho nu, então só podia ser "
            "visto depois da invenção do telescópio. Os desenhos de Galileu mostram que ele o observou em 28 de "
            "dezembro de 1612 e de novo em 27 de janeiro de 1613, as duas vezes muito perto de Júpiter, e as duas "
            "vezes o tomou por uma estrela fixa. Em dezembro, o planeta tinha virado retrógrado naquele mesmo dia, ou "
            "seja, estava estacionário, com movimento pequeno demais para ser notado, e seu disco era minúsculo "
            "na luneta. Mesmo assim, há indício de que algo chamou a atenção dele: em 28 de janeiro, Galileu anotou "
            "que uma estrela de fundo parecia ter se movido e marcou a posição dela com uma tinta diferente. Não há "
            "prova clara, porém, de que tenha percebido que era um planeta. Netuno só foi confirmado em setembro de "
            "1846, em Berlim, a partir dos cálculos de Le Verrier. Galileu não foi o único a deixar escapar: o "
            "planeta também foi visto e registrado por Michel Lalande, em 1795, e por John Herschel, em 1830. "
            "Esses registros antigos acabaram sendo úteis para calcular com precisão a órbita de Netuno."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Discovery_of_Neptune",
            "telescopic observations confirming the existence of a major planet were made on the night of September 23–24, autumnal equinox of 1846, at the Berlin Observatory, by astronomer Johann Gottfried Galle (assisted by Heinrich Louis d'Arrest), working from Le Verrier's calculations. [...] "
            "too dim to be visible to the naked eye: its apparent magnitude is never brighter than 7.7. "
            "Therefore, the first observations of Neptune were only possible after the invention of the telescope. "
            "There is evidence that Neptune was seen and recorded by Galileo Galilei in 1613, Michel Lefrançois de Lalande in 1795, and John Herschel in 1830, but none are known to have recognized it as a planet at the time. "
            "These pre-discovery observations were important in accurately determining the orbit of Neptune. [...] "
            "Galileo's drawings show that he observed Neptune on December 28, 1612, and again on January 27, 1613; "
            "on both occasions, Galileo mistook Neptune for a fixed star when it appeared very close (in conjunction) to Jupiter in the night sky. [...] "
            "At the time of his first observation in December 1612, it was stationary in the sky because it had just turned retrograde that very day. "
            "This meant that Neptune's motion was too slight to be detected at that date, and its apparent size was too small to appear clearly as a planet in Galileo's small telescope. "
            "However, there is evidence that Galileo was aware there was something unusual about this \"star\". "
            "On January 28, Galileo recorded in his notebook that a background star (Neptune) had appeared to move, and drew Neptune's position with a dot in a different ink to the fixed stars. [...] "
            "However, there is no clear evidence that he identified this moving object a",
            nome="Discovery of Neptune")],
    },
    # 10 Ulugh Beg e o instrumento gigante de Samarcanda
    {
        "temas_secundarios": ["mundo_islamico_medieval", "calendarios"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Sem telescópio, o sultão-astrônomo Ulugh Beg buscou precisão no tamanho: em Samarcanda, ergueu um sextante com raio de uns 36 metros. Foi morto a mando do próprio filho, e o observatório só foi reencontrado em 1908.",
        "explicacao": (
            "Neto do conquistador Tamerlão, Ulugh Beg passou a governar Samarcanda, no atual Uzbequistão, em 1409, "
            "aos dezesseis anos. Nos anos 1420, mandou construir ali um observatório e convidou mais de 60 "
            "matemáticos e astrônomos. Como não havia lentes, a saída para medir melhor era aumentar a escala: o "
            "sextante Fakhri, o maior instrumento do lugar, tinha raio de cerca de 36 metros. Em 1437, saiu o "
            "Zij-i-Sultani, catálogo de 994 estrelas tido como o maior entre os de Ptolomeu e de Tycho Brahe. Ulugh "
            "Beg mediu o ano tropical em 365 dias, 5 horas, 49 minutos e 15 segundos, com erro de 25 segundos, "
            "mais preciso que a estimativa de Copérnico, que errava por 30. Como governante, saiu-se pior. Depois "
            "da morte do pai, em 1447, entrou numa guerra de sucessão e acabou rendido ao filho mais velho, "
            "Abdal-Latif. O filho o liberou para peregrinar a Meca, mas garantiu que ele nunca chegasse: mandou "
            "matá-lo em 1449. O observatório foi destruído e dezenas de estudiosos se dispersaram. Em 1908, o "
            "arqueólogo russo Vassily Vyatkin achou os restos. Hoje se veem as fundações e a parte enterrada do "
            "grande instrumento de mármore."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Ulugh_Beg",
                "Sixteen-year-old Ulugh Beg subsequently became the governor of the former capital of Samarkand in 1409. [...] "
                "Lacking telescopes to work with, he increased his accuracy by increasing the length of his sextant; "
                "the so-called Fakhri sextant had a radius of about 36 meters (118 feet) [...] "
                "The Fakhri sextant was the largest instrument at the observatory in Samarkand [...] "
                "he compiled the 1437 Zij-i-Sultani of 994 stars, generally considered the greatest star catalogue between those of Ptolemy and Tycho Brahe [...] "
                "However, Ulugh Beg later measured another more precise value of the tropical year as 365d 5h 49m 15s, which has an error of +25 seconds, making it more accurate than Copernicus's estimate which had an error of +30 seconds. [...] "
                "In 1447, upon learning of the death of his father Shah Rukh, Ulugh Beg went to Balkh. [...] "
                "Abd-al-Latif soon reached Samarkand and Ulugh Beg involuntarily surrendered to his son. "
                "Abd-al-Latif released his father from custody, allowing him to make pilgrimage to Mecca. "
                "However, he ensured Ulugh Beg never reached his destination, having him, as well as his brother Abdal-Aziz assassinated in 1449. [...] "
                "He was a grandson of the great conqueror and king, Timur (Tamerlane)",
                nome="Ulugh Beg"),
            wiki("Ulugh_Beg_Observatory",
                "is an observatory in modern day Samarkand, Uzbekistan, which was built in the 1420s by the Timurid astronomer Ulugh Beg. [...] "
                "Over 60 mathematicians and astronomers were invited to the observatory. [...] "
                "Today, the foundations and the buried part of the marble quadrant are all that are visible of the original vestiges of the Ulugh Beg Observatory. [...] "
                "The observatory was destroyed and dozens of talented astronomers and mathematicians were driven away. "
                "In 1908, the Russian archaeologist Vassily Vyatkin uncovered the remains of the observatory.",
                nome="Ulugh Beg Observatory"),
        ],
    },
    # 11 precessão: Hiparco, a estrela polar e os signos desalinhados
    {
        "temas_secundarios": ["grecia_antiga", "calendarios", "mitologia"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Os signos do zodíaco já não batem com as constelações de mesmo nome. A culpa é um bamboleio lento do eixo da Terra, a precessão, que Hiparco notou no século II a.C. comparando suas medidas com as de seus antecessores.",
        "explicacao": (
            "O eixo da Terra gira como o de um pião, e completa uma volta em cerca de 26 mil anos. Com isso, o polo "
            "celeste passeia entre as estrelas. Polaris é hoje a estrela polar, mas em 3000 a.C. o papel era de "
            "Thuban, no Dragão, e de 1500 a.C. a 500 d.C., de Kochab, na Ursa Menor. O ponto do equinócio de março "
            "também desliza: há 5 mil anos ficava perto de Aldebaran, em Touro, e hoje está em Peixes. Os signos da "
            "astrologia ocidental foram batizados pelas constelações que o Sol atravessava, mas ao longo dos séculos "
            "saíram de alinhamento com elas por causa da precessão; a astrologia hindu corrige esse desvio. A "
            "descoberta costuma ser atribuída a Hiparco. Segundo o Almagesto de Ptolomeu, ele mediu a posição da "
            "estrela Espiga durante eclipses lunares e, comparando com dados de Timócaris, que trabalhou no começo "
            "do século III a.C., viu que ela tinha se deslocado uns 2° em relação ao equinócio de outono. Concluiu "
            "que os equinócios andavam pelo zodíaco a pelo menos 1° por século, ou seja, com um ciclo de no máximo "
            "36 mil anos. Quase tudo o que Hiparco escreveu se perdeu, e o conhecemos por Ptolomeu."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Axial_precession",
                "The discovery of precession usually is attributed to Hipparchus (190–120 BC) of Rhodes or Nicaea, a Greek astronomer. "
                "According to Ptolemy's Almagest, Hipparchus measured the longitude of Spica and other bright stars. "
                "Comparing his measurements with data from his predecessors, Timocharis (320–260 BC) and Aristillus (~280 BC), he concluded that Spica had moved 2° relative to the autumnal equinox. [...] "
                "Hipparchus concluded that the equinoxes were moving (\"precessing\") through the zodiac, and that the rate of precession was not less than 1° in a century, in other words, completing a full cycle in no more than 36,000 years. "
                "Virtually all of the writings of Hipparchus are lost, including his work on precession. They are mentioned by Ptolemy [...] "
                "He measured the ecliptic longitude of the star Spica during lunar eclipses [...] "
                "Timocharis of Alexandria (a contemporary of Euclid, who worked with Aristillus early in the 3rd century BC) [...] "
                "completing one circuit in approximately 26,000 years. "
                "Thus, while today the star Polaris in Ursa minor lies approximately at the north celestial pole, this will change over time [...] "
                "The previous pole star was Kochab (Beta Ursae Minoris, β UMi, β Ursae Minoris), the brightest star in the bowl of the \"Little Dipper\", located 16 degrees from Polaris. "
                "It held that role from 1500 BC to AD 500. [...] "
                "Thuban in the constellation Draco, which was the pole star in 3000 BC [...] "
                "5,000 years ago, the March equinox was close to the star Aldebaran in Taurus. "
                "Now, as seen from the yellow grid, it has shifted (indicated by the red arrow) to somewhere in the constellation of Pisces.",
                nome="Axial precession"),
            wiki("Astrological_sign",
                "Each sign was named after a constellation the sun annually moved through while crossing the sky. [...] "
                "Over the centuries, Western astrology's zodiacal divisions have shifted out of alignment with the constellations they were named after by axial precession of the Earth while Hindu astrology measurements correct for this shifting.",
                nome="Astrological sign"),
        ],
    },
    # 12 babilônios calculavam Júpiter com a área de um trapézio
    {
        "temas_secundarios": ["primeiras_civilizacoes", "historia_matematica", "sistema_solar"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Astrônomos da Babilônia calculavam quanto Júpiter andava no céu pela área de um trapézio num gráfico de velocidade por tempo, técnica que se achava ter nascido na Europa do século XIV. As tabuinhas são de 350 a 50 a.C.",
        "explicacao": (
            "Em 2016, o historiador da ciência Mathieu Ossendrijver, da Universidade Humboldt de Berlim, publicou na "
            "revista Science a análise de cinco tabuinhas cuneiformes do Museu Britânico. Duas delas, conhecidas "
            "desde 1955, calculavam a área de um trapézio, mas ninguém entendia para quê: estavam danificadas, tinham "
            "sido escavadas sem método na Babilônia no século XIX e não diziam a que planeta se referiam. A chave foi "
            "uma quinta tabuinha, quase inteira, que o assiriólogo aposentado Hermann Hunger mostrou a ele numa foto "
            "antiga. Ela fazia uma conta equivalente, sem trapézio, que só podia ser sobre Júpiter. Nos 60 dias "
            "depois de reaparecer como estrela da manhã, a velocidade diária de Júpiter cai de forma linear. Num "
            "gráfico de velocidade contra tempo, isso desenha um trapézio, e a área dele dá a distância percorrida. "
            "As tabuinhas ainda acham o dia em que o planeta cobre metade do trajeto, partindo o trapézio em dois de "
            "áreas iguais. Na Europa, o mesmo raciocínio aparece com os calculadores de Oxford, no Merton College, "
            "e com Nicole Oresme, em Paris, ambos no século XIV, ao menos 14 séculos depois. Até então, achava-se "
            "que a astronomia babilônica só usava aritmética, embora a matemática da região usasse geometria desde "
            "1800 a.C."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [{
            "url": "https://www.hu-berlin.de/nachrichten/detail/geometry-in-babylonian-astronomy",
            "titulo": "Geometry in Babylonian Astronomy (Humboldt-Universität zu Berlin, 2016)",
            "idioma": "en",
            "trecho": (
                "28.01.2016 [...] "
                "Babylonian astronomers computed the position of Jupiter with geometrical methods "
                "This is revealed by an analysis of three published and two unpublished cuneiform tablets from the British Museum by Prof. Mathieu Ossendrijver, historian of science of the Humboldt-Universität zu Berlin. "
                "The tablets date from the period between 350 and 50 BCE. "
                "Historians of science thus far assumed that geometrical computations of the kind found on these tablets were first carried out in the 14th century. "
                "Moreover, it was assumed that Babylonian astronomers used only arithmetical methods. [...] "
                "His results are published in the current issue of the journal Science. "
                "On four of these tablets the distance covered by Jupiter is computed as the area of a figure that represents how its velocity changes with time. [...] "
                "Two of these so-called trapezoid texts had been known since 1955, but their meaning remained unclear [...] "
                "One reason for this was the damaged state of the tablets, which were excavated unscientifically in Babylon, near its main temple Esagila, in the 19th century. "
                "Another reason was, that the calculations could not be connected to a particular planet. "
                "The new interpretation of the trapezoid texts was now prompted by a newly discovered, almost completely preserved fifth tablet. [...] "
                "the retired Professor of Assyriology Hermann Hunger, draw the attention of Mathieu Ossendrijver to this tablet. "
                "He presented him with an old photograph of the tablet that was made in the British Museum. "
                "The new tablet does not mention a trapezoid figure, but it does contain a computation that is mathematically equivalent to the other ones. "
                "This computations can be uniquely assigned to the planet Jupiter. [...] "
                "for the first 60 days after Jupiter becomes visible as a morning star. [...] "
                "Jupiter's velocity decreases linearly within the 60 days. "
                "Because of the linear decrease a trapezoidal figure emerges if one draws the velocity against time. [...] "
                "Moreover, the time when Jupiter covers half this distance is also calculated, by dividing the trapezoid into two smaller ones of equal area. [...] "
                "but they were carried out at least 14 centuries earlier [...] "
                "The so-called Oxford calculators, a group of scholastic mathematicians, who worked at Merton College, Oxford, in the 14th century [...] "
                "In the same century Nicole Oresme, a bishop and scholastic philosopher in Paris, devised graphical methods that enabled him to prove this relation. [...] "
                "Furthermore, it was hitherto assumed that the astronomers in Babylon used arithmetical methods but no geometrical ones, even though they were common in Babylonian mathematics since 1800 BCE. [...] "
                "in: Science, January 29, 2016."
            ),
        }],
    },
    # 13 Chankillo, as treze torres do Sol no Peru
    {
        "temas_secundarios": ["americas_pre_colombianas", "calendarios", "arquitetura"],
        "tipos_espanto": ["engenhosidade"],
        "gancho": "No Peru, treze torres em fila num morro formam um horizonte \"dentado\": o Sol nasce atrás de uma torre diferente conforme a época do ano. São do século III a.C. e podem ser o mais antigo observatório das Américas.",
        "explicacao": (
            "Chankillo fica na bacia de Casma-Sechín, no departamento de Áncash, e reúne um forte no alto de um "
            "morro, áreas de moradia e as chamadas Treze Torres. Elas foram erguidas a intervalos regulares sobre a "
            "crista de um morro baixo, alinhado quase de norte a sul, e se espalham por uns 300 metros. Os "
            "pesquisadores identificaram dois prováveis pontos de observação, um a leste e outro a oeste. Vistas de "
            "lá, as torres cobrem quase exatamente o trecho do horizonte por onde o Sol nasce e se põe ao longo do "
            "ano. No solstício de inverno, o Sol nasce atrás da torre da ponta esquerda e, nos seis meses seguintes, "
            "vai passando por trás de cada uma até chegar à da ponta direita, no solstício de verão. Quem soubesse "
            "atrás de qual torre o Sol estava surgindo podia saber a data com erro de um ou dois dias. As torres eram "
            "conhecidas por viajantes havia 200 anos, mas só em 2007 Iván Ghezzi e Clive Ruggles mostraram que se "
            "tratava de um sítio astronômico. Em julho de 2021, o conjunto virou Patrimônio Mundial da Unesco."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Chankillo",
            "Chankillo is an ancient monumental complex in the Peruvian coastal desert, found in the Casma-Sechin basin in the Áncash Department of Peru. "
            "The ruins include the hilltop Chankillo fort, the nearby Thirteen Towers solar observatory, and residential and gathering areas. "
            "The Thirteen Towers have been interpreted as an astronomical observatory built in the third century BC. [...] "
            "The site was awarded UNESCO  World Heritage status in July 2021. [...] "
            "The  regularly-spaced thirteen towers of Chankillo were constructed atop the ridge of a low hill running near north to south, forming a \"toothed\" horizon with narrow gaps at regular intervals. "
            "To the east and west investigators designated two possible observation points. "
            "From these vantages, the 300m long spread of the towers along the horizon corresponds very closely to the rising and setting positions of the sun over the year, albeit they are not all visible. "
            "On the winter solstice, the sun would rise behind the leftmost tower of Chankillo and rise behind each of the towers until it reached the rightmost tower six months later on the summer solstice, marking the passage of time. "
            "The Thirteen Towers of Chankillo could be the earliest known observatory in the Americas. "
            "Inhabitants of Chankillo would have been able to determine an accurate date, with an error of a day or two, by observing the sunrise or sunset from the correct tower. [...] "
            "The towers had been known to travellers for 200 years but were not determined to be an astronomical site until 2007 by Iván Ghezzi and Clive Ruggles.",
            nome="Chankillo")],
    },
    # 14 a ema e o emu feitos de escuridão
    {
        "temas_secundarios": ["povos_indigenas", "galaxias", "mitologia"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "No Brasil e na Austrália, povos indígenas veem no céu uma grande ave feita não de estrelas, mas de manchas escuras da Via Láctea: a ema dos guaranis e o emu dos aborígenes. Nas duas, a cabeça fica junto ao Cruzeiro.",
        "explicacao": (
            "Quase todas as constelações ligam pontos brilhantes. A da Ema, Guyra Nhandu em guarani, usa o "
            "contrário: as faixas escuras da Via Láctea, que são nuvens de poeira. O astrônomo Germano Afonso "
            "localizou-a com a ajuda de guaranis do Paraná. A cabeça é o Saco de Carvão, uma mancha escura junto ao "
            "Cruzeiro do Sul; as estrelas Alfa e Beta do Centauro ficam dentro do pescoço, também escuro; e duas "
            "estrelas da constelação da Mosca são ovos que ela tenta devorar. Em 1614, o missionário francês Claude "
            "d'Abbeville já descrevia entre os tupinambás do Maranhão uma constelação de \"avestruz\" com bico e "
            "dois ovos, provavelmente a mesma ema, e carajás e bororós também têm a sua. Do outro lado do mundo, o "
            "\"Emu no Céu\", usado em quase toda a cultura aborígene australiana, também é feito de nebulosas "
            "escuras contra o fundo da Via Láctea: a cabeça é o mesmo Saco de Carvão, e o corpo e as pernas seguem "
            "a Grande Fenda até o Escorpião. Perto de Sydney, uma gravura na rocha mostra um emu na mesma pose e "
            "orientação da constelação."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": RBHC, "titulo": RBHC_TITULO, "idioma": "pt",
             "trecho": (
                 "de Claude D’Abbeville, publicado em 1614. [...] "
                 "Conhecem uma constelação denominada Iandutim, ou Avestruz branca, formada de estrelas muito grandes e brilhantes, "
                 "algumas das quais representam um bico; dizem os maranhenses que elas procuram devorar duas outras estrelas que lhes estão juntas "
                 "e às quais denominam uirá-upiá, isto é: os dois ovos [...] "
                 "Mas no Brasil não existiam avestruzes e, sim, uma ave parecida chamada ema (Rhea Americana). "
                 "A constelação descrita por D’Abbeville é, provavelmente, correspondente à constelação guarani da Ema (Guyra Nhandu). [...] "
                 "Os Guarani do Paraná nos mostraram a localização exata da constelação da Ema (Guyra Nhandu) que fica na região do céu ocupada "
                 "pelas constelações ocidentais do Cruzeiro do Sul, da Mosca, do Centauro, do Escorpião, do Triângulo Austral e de Altar. [...] "
                 "Saco de Carvão, sendo que a parte superior fica perto da estrela Mimosa e o bico perto de Magalhães, ambas da constelação do Cruzeiro do Sul. "
                 "Perto do seu bico parece existirem dois ovos de pássaro (Guirá-rupiá, em guarani) que ela tenta devorar. "
                 "Esses ovos são as estrelas Alfa e Beta da constelação da Mosca. "
                 "As estrelas Alfa e Beta da constelação do Centauro estão dentro do pescoço da Ema, que também é formado por uma mancha escura da Via Láctea. [...] "
                 "A constelação da Ema aparece em relatos de várias etnias brasileiras. [...] "
                 "os bororós (que não pertencem à família tupi-guarani) também têm uma constelação da Ema"
             )},
            wiki("Emu_in_the_sky",
                "with others, such as Emu in the Sky, describes the dark patches rather than the points lit by the stars. [...] "
                "A constellation used almost everywhere in Australian Aboriginal culture is the \"Emu in the Sky\", which consists of dark nebulae (opaque clouds of dust and gas in outer space) that are visible against the (centre and other sectors of the) Milky Way background. "
                "The Emu's head is the very dark Coalsack Nebula, next to the Southern Cross; the body and legs are that extension of the Great Rift trailing out to Scorpius. [...] "
                "An engraving near the Elvina Track shows an emu in the same pose and orientation as the Emu in the Sky constellation.",
                nome="Australian Aboriginal astronomy"),
        ],
    },
    # 15 os tupinambás, a Lua e as marés
    {
        "temas_secundarios": ["povos_indigenas", "oceanografia", "revolucao_cientifica"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "Em 1614, um missionário francês registrou que os tupinambás do Maranhão atribuíam as marés à Lua. Na mesma época, Galileu rejeitava essa ideia como \"vã quimera\" e tentava explicar as marés só pelos movimentos da Terra.",
        "explicacao": (
            "O capuchinho Claude d'Abbeville publicou em 1614 um relato da missão francesa no Maranhão, hoje um dos "
            "documentos históricos mais importantes sobre o que os indígenas do Brasil sabiam do céu. O livro "
            "descreve constelações, calendários e observações práticas dos tupinambás. Sobre o mar, ele anotou que "
            "eles atribuíam à Lua o fluxo e o refluxo da água e distinguiam bem as duas marés cheias, as que vêm na "
            "lua cheia e na lua nova, ou poucos dias depois. Na época, as causas das marés ainda não eram conhecidas. "
            "Em 1616, Galileu escreveu um discurso sobre o fluxo e o refluxo do mar, depois ampliado no Diálogo de "
            "1632, defendendo que as marés surgiriam só da combinação dos dois movimentos que Copérnico atribuía à "
            "Terra, a rotação e a volta em torno do Sol, sem precisar da \"vã quimera do movimento da Lua\". Estava "
            "errado: a causa é a atração gravitacional da Lua e do Sol, e Newton foi quem mostrou corretamente como "
            "ela age. Séculos depois, o astrônomo Germano Afonso comparou o sistema astronômico descrito por "
            "d'Abbeville com o dos guaranis atuais do Sul do Brasil e o achou muito semelhante, apesar de mais de "
            "3 mil quilômetros e quase 400 anos de distância."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [{"url": RBHC, "titulo": RBHC_TITULO, "idioma": "pt",
            "trecho": (
                "Apresenta-se uma análise de um dos mais importantes documentos históricos brasileiros sobre conhecimentos astronômicos indígenas [...] "
                "de Claude D’Abbeville, publicado em 1614. "
                "A crônica traz descrições de constelações, sistemas de calendário e alguns conhecimentos astronômicos empíricos. [...] "
                "A relação entre a Lua e as marés também é descrita por D’Abbeville: "
                "“Eles atribuem à Lua o fluxo e o refluxo do mar e distinguem muito bem as duas marés cheias que se verificam na Lua cheia e na Lua nova ou poucos dias depois”. [...] "
                "Essa citação tem um significado importante, pois, na época em que D’Abbeville escreveu o livro, as causas das marés ainda não eram conhecidas. "
                "Galileu Galilei escreveu o Discorso del flusso e reflusso del mare [...] "
                "em 1616, e uma expansão do Discorso em Dialogo sopra i due massimi sistemi del mondo [...] "
                "escrito em 1632. [...] "
                "não precisa recorrer à “vã quimera do movimento da Lua” [...] "
                "No Dialogo, Galileu tenta mostrar que apenas pela combinação da rotação axial da Terra com sua revolução orbital – "
                "os dois movimentos que Copérnico atribuiu à Terra – os movimentos de maré que observamos podem surgir. [...] "
                "Mas a causa das marés é a atração gravitacional da Lua e do Sol, e Newton foi o primeiro a mostrar corretamente como as forças geradoras da maré funcionam. [...] "
                "é muito semelhante ao utilizado, atualmente, pelos Guarani do Sul do Brasil [...] "
                "pelo espaço (mais de 3.000 km, em linha reta) e pelo tempo (quase 400 anos)."
            )}],
    },
    # 16 Nicole-Reine Lepaute e a volta do cometa Halley
    {
        "temas_secundarios": ["asteroides_cometas", "personagens_esquecidos", "historia_computacao"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Para prever a volta do cometa Halley em 1759, três franceses dividiram as contas da atração de Júpiter e Saturno e passaram seis meses quase sem parar para comer. Uma delas, Nicole-Reine Lepaute, foi apagada do livro.",
        "explicacao": (
            "Edmond Halley previu que o cometa visto em 1682 voltaria \"por volta do fim de 1758 ou do começo do ano "
            "seguinte\", mas não conseguia ser mais preciso. A gravidade de Júpiter e de Saturno desviava o cometa, "
            "um problema de três corpos que ainda não tinha solução, até Alexis Clairaut achar um método. Em junho "
            "de 1757, ele dividiu o trabalho com Jérôme Lalande e Nicole-Reine Lepaute, que fazia cálculos "
            "astronômicos e já tinha computado tabelas para um tratado de relojoaria do marido. Lepaute e Lalande "
            "calcularam a atração dos dois planetas, e Clairaut, a órbita do cometa. Em novembro de 1758, deram uma "
            "janela para a passagem mais próxima do Sol: de 15 de março a 15 de maio de 1759, centrada em 13 de "
            "abril. O cometa chegou em 13 de março. Era uma precisão dez vezes maior que a de Halley, mas d'Alembert "
            "debochou do trabalho, \"mais trabalhoso que profundo\". Clairaut tirou as menções a Lepaute do livro que "
            "publicou em 1760, supostamente para agradar outra mulher. Ela seguiu calculando: fez almanaques de 1759 "
            "a 1783 e calculou o eclipse solar de 1764. Hoje, um asteroide e uma cratera da Lua levam seu nome."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Nicole-Reine_Lepaute",
            "was a French astronomer and human computer. "
            "Lepaute along with Alexis Clairaut and Jérôme Lalande calculated the date of the return of Halley's Comet. "
            "Her other astronomical feats include calculating the 1764 solar eclipse and producing almanacs from 1759 to 1783. [...] "
            "The asteroid 7720 Lepaute is named in her honour, as is the lunar crater Lepaute. [...] "
            "Madame Lepaute computed for this book a table of numbers of oscillations for pendulums of different lengths [...] "
            "In June 1757, she worked together with Jérôme Lalande and Alexis Clairaut to calculate the date of the next passage of Halley's Comet, last seen in 1682. "
            "Halley couldn't precisely compute the return date beyond \"around the end of the year 1758 or the beginning of the next\", "
            "due to the gravitational pull of Jupiter and Saturn on the comet, which made for a three-body problem that couldn't be solved back then, for which Clairaut had found a solution recently. "
            "In order to solve it, Clairaut, Lalande and Lepaute divided calculations between them and worked in parallel, "
            "with Lepaute and Lalande focusing on the attraction of Jupiter and Saturn, while Clairaut calculated the orbit of the comet itself. "
            "The team worked for more than six months straight, barely stopping for food, in order to produce a date before the comet arrived. "
            "In November 1758, they gave a two-month window for when the comet would reach its perihelion, between 15 March and 15 May,  centered around 13 April 1759. "
            "The comet ended up arriving on 13 March 1759. "
            "Although this was a tenfold improvement over Halley's initial 2 years period, there was still an error of a few days, "
            "which caused the astronomer Jean d'Alembert to ridicule their work and call it \"more laborious than deep\". [...] "
            "Clairault removed mentions of her from the book he published in 1760, Théorie du mouvement des comètes, allegedly to please another woman.",
            nome="Nicole-Reine Lepaute")],
    },
]
