LOTE = "2026-11-18-especiarias-01"
AREA = "comida"
TEMA = "especiarias"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Edmond Albius e a polinização da baunilha
    {
        "temas_secundarios": ["plantas", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Quase toda a baunilha do mundo é polinizada à mão, com uma técnica inventada em 1841 por Edmond Albius, um menino escravizado de 12 anos na ilha da Reunião.",
        "explicacao": (
            "Na década de 1820, colonos franceses levaram a baunilha, uma orquídea americana, para as ilhas da "
            "Reunião e de Maurício, no oceano Índico. As plantas cresciam, mas não davam vagens: o inseto que as "
            "poliniza não existe fora da região de origem. Em 1837, o botânico belga Charles Morren publicou um "
            "método de polinização manual, mas ele era lento e trabalhoso demais para render dinheiro. Em 1841, "
            "Albius, nascido escravizado e então com 12 anos, achou um jeito rápido: com uma lasca fina ou um talo "
            "de capim, ergue-se a pequena aba que separa a parte masculina da feminina da flor e, com o polegar, "
            "espalha-se o pólen pegajoso sobre o estigma. O gesto é usado até hoje, e como cada flor dura cerca de "
            "um dia, os produtores precisam vistoriar as plantações diariamente. Graças a ele, a Reunião foi por um "
            "tempo a maior fornecedora de baunilha do mundo, e a técnica levou o cultivo a Madagascar, hoje um dos "
            "maiores produtores. Um botânico francês afirmou tê-la descoberto antes, mas a alegação foi desmentida. "
            "Albius ficou livre em 1848, quando a França aboliu a escravidão nas colônias. Moradores da ilha "
            "tentaram, sem sucesso, conseguir para ele uma recompensa ou pensão do governo, e ele morreu pobre, "
            "em 1880."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Edmond_Albius",
                "Born into slavery, Albius became an important figure in the cultivation of vanilla. "
                "At the age of 12, he invented a technique for pollinating vanilla orchids quickly and profitably. "
                "Albius's technique revolutionized the cultivation of vanilla and made it possible to profitably grow Vanilla planifolia away from its native habitat (Mexico to Brazil). [...] "
                "French colonists brought vanilla seeds to Réunion and nearby Mauritius in the 1820s with the hope of starting production there. "
                "However, the plant didn't develop any fruits (seed pods) because of the absence of the pollinating insect outside of the plant's natural range. "
                "In 1837, Charles Morren, a professor of botany at the University of Liège in Belgium, published a method of hand-pollination, "
                "but his technique was slow and required too much effort to make cultivating vanilla a moneymaking proposition. [...] "
                "In 1841, Albius invented a method to quickly pollinate the vanilla orchid using a thin stick or blade of grass and a simple thumb gesture. "
                "Using the stick or grass blade, field hands lift the rostellum, the flap that separates the male anther from the female stigma, "
                "and then, with their thumbs, smear the sticky pollen from the anther over the stigma. "
                "Albius's manual pollination method is still used today, as nearly all vanilla is pollinated by hand. "
                "After Albius's discovery, Réunion became for a time the world's largest supplier of vanilla. "
                "French colonists used Albius's technique in Madagascar to cultivate vanilla [...] "
                "Noted French botanist and plant collector Jean Michel Claude Richard claimed to have discovered the technique three or four years earlier but this has been debunked. [...] "
                "locals on Réunion attempted (unsuccessfully) to obtain a reward or a government stipend for Albius. "
                "In 1848, France outlawed slavery in its colonies [...] "
                "Albius died in poverty in St. Suzanne in 1880.",
                nome="Edmond Albius"),
            wiki("Vanilla",
                "Indonesia and Madagascar are the world's largest producers. [...] "
                "Edmond Albius, a 12-year-old enslaved child who lived on the French island of Réunion in the Indian Ocean [...] "
                "The vines grew, but would not fruit outside Mexico. [...] "
                "The flowers of V. planifolia last about one day, sometimes less, so growers have to inspect their plantations every day for open flowers, a labor-intensive task.",
                nome="Vanilla"),
        ],
    },
    # 2 baunilha de cravo e de fábrica de papel
    {
        "temas_secundarios": ["quimica_cotidiano", "plantas"],
        "tipos_espanto": ["origem_inesperada", "escala_absurda"],
        "gancho": "O sabor de baunilha artificial já foi feito com óleo de cravo e com resíduo de fábrica de papel. Em 1981, uma só fábrica de celulose, no Canadá, fornecia 60% da vanilina sintética do mundo.",
        "explicacao": (
            "A vanilina é a principal responsável pelo aroma da baunilha, embora a vagem de verdade contenha "
            "centenas de compostos diferentes. Ela foi isolada da baunilha em 1858, e a procura por esse sabor "
            "há muito tempo supera a oferta de vagens. No fim do século XIX, já se vendia vanilina feita a partir do "
            "eugenol, substância do óleo de cravo, e a produção comercial seguiu assim até a década de 1920. Nos anos "
            "1930, o cravo deu lugar a um resíduo das fábricas de papel: o líquido rico em lignina que sobra "
            "quando a madeira é transformada em polpa. Em 1981, uma única fábrica de papel e celulose em Thorold, "
            "no Ontário, abastecia 60% do mercado mundial de vanilina sintética. Hoje, cerca de 15% da produção "
            "ainda sai da lignina, e uns 85% vêm de matérias-primas petroquímicas, como o guaiacol. A baunilha "
            "natural é uma fração pequena: em 2001, a demanda anual foi de 12 mil toneladas de vanilina, das "
            "quais só 1.800 eram naturais. Já o castóreo, secreção de glândulas do castor, chegou a ser usado em "
            "substitutos de baunilha, mas hoje a indústria consome só uns 100 kg por ano, contra mais de 1,2 "
            "milhão de kg de vanilina."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Vanillin",
                "The demand for vanilla flavoring has long exceeded the supply of vanilla beans. "
                "As of 2001, the annual demand for vanillin was 12,000 tons, but only 1,800 tons of natural vanillin were produced. [...] "
                "Vanillin was commercially produced from eugenol until the 1920s. [...] "
                "By the late 19th century, semisynthetic vanillin derived from the eugenol found in clove oil was commercially available. "
                "Synthetic vanillin became significantly more available in the 1930s, when production from clove oil was supplanted by production from the lignin-containing waste produced by sulfite pulping for preparing wood pulp for the paper industry. "
                "By 1981, a single pulp and paper mill in Thorold, Ontario, supplied 60% of the world market for synthetic vanillin. [...] "
                "Today, approximately 15% of the world's production of vanillin is still made from lignin wastes, while approximately 85% is synthesized in a two-step process from the petrochemical precursors guaiacol and glyoxylic acid.",
                nome="Vanillin"),
            wiki("Vanilla",
                "Real seedpod extract is a complex mixture of several hundred different compounds [...] "
                "The chemical compound vanillin (4-hydroxy-3-methoxybenzaldehyde) is a major contributor to the characteristic flavor and aroma of real vanilla [...] "
                "Vanillin was first isolated from vanilla pods by Gobley in 1858.",
                nome="Vanilla"),
            wiki("Castoreum",
                "Historically, compounds isolated from castoreum were used in strawberry and raspberry flavorings and vanilla substitutes, "
                "but at present, the annual industry consumption is very low, around 100 kilograms (220 lb), whereas vanillin is over 1.2 million kg (2.6 million lb) annually.",
                nome="Castoreum"),
        ],
    },
    # 3 açafrão: um clone estéril
    {
        "temas_secundarios": ["plantas", "domesticacao"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "A planta do açafrão não é encontrada em estado selvagem e não dá sementes: é um clone estéril que só se multiplica porque pessoas desenterram e replantam seus bulbos. Cada quilo do tempero exige umas 150 mil flores.",
        "explicacao": (
            "O tempero é o estigma vermelho da flor do Crocus sativus, uma planta desconhecida em estado "
            "selvagem. Ela possivelmente descende de uma espécie silvestre do Mediterrâneo oriental e, segundo o "
            "escritor de culinária Harold McGee, foi domesticada na Grécia ou perto dela, na Idade do Bronze. O detalhe "
            "genético é que ela é triploide: tem três conjuntos de cromossomos, 24 no total, e por isso não "
            "consegue se reproduzir sexualmente. As flores roxas não produzem sementes viáveis. A única saída é a "
            "mão humana: os bulbos subterrâneos, os cormos, precisam ser desenterrados, divididos e replantados. "
            "Foi assim, como um clone geneticamente uniforme, que a planta se espalhou devagar por boa parte da "
            "Eurásia. A colheita é igualmente artesanal. Cada flor tem só três estigmas, e um quilo de açafrão "
            "exige cerca de 440 mil deles, o equivalente a 150 mil flores. Colher 150 mil flores leva 40 horas de "
            "trabalho. É por isso que o açafrão de primeira costuma passar de 5 mil dólares o quilo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Saffron",
                "The domesticated saffron crocus, Crocus sativus, is an autumn-flowering perennial plant unknown in the wild. "
                "It possibly descends from the eastern Mediterranean autumn-flowering Crocus cartwrightianus [...] "
                "As a genetically monomorphic clone incapable of seed production, it was slowly propagated by humans throughout much of Eurasia. [...] "
                "It is a sterile triploid form, which means that three homologous sets of chromosomes make up each specimen's genetic complement; "
                "C. sativus bears eight chromosomal bodies per set, making for 24 in total. "
                "Being sterile, the purple flowers of C. sativus fail to produce viable seeds; reproduction hinges on human assistance: "
                "clusters of corms, underground, bulb-like, starch-storing organs, must be dug up, divided, and replanted. [...] "
                "Harold McGee states that it was domesticated in or near Greece during the Bronze Age. [...] "
                "premium saffron regularly exceeds US$5,000 per kilogram, sustained by its labor-intensive hand-harvesting process. [...] "
                "which require some 440,000 hand-picked saffron stigmas per kilogram (200,000 stigmas/lb) – equivalently, 150,000 crocus flowers per kilogram (70,000 flowers/lb). "
                "Forty hours of labour are needed to pick 150,000 flowers.",
                nome="Saffron"),
            wiki("Crocus_sativus",
                "The corm plants generally bloom with purple flowers in the autumn. These flowers are sterile, each have six petals and three red or orange stigmas.",
                nome="Crocus sativus"),
        ],
    },
    # 4 a Guerra do Açafrão e as execuções em Nuremberg
    {
        "temas_secundarios": ["europa_medieval", "comercio_rotas"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Na Idade Média, o roubo de um carregamento de açafrão por nobres deu início a uma guerra de 14 semanas. Em Nuremberg, quem vendesse açafrão adulterado podia ser executado.",
        "explicacao": (
            "No século XIV, a peste negra fez a procura por remédios à base de açafrão chegar ao auge. A Europa "
            "importava grandes quantidades em navios venezianos e genoveses, vindos de lugares como a ilha de "
            "Rodes. Quando nobres roubaram um desses carregamentos, o episódio desencadeou a chamada Guerra do "
            "Açafrão, que durou 14 semanas. O conflito e o medo de que a pirataria de açafrão se alastrasse "
            "estimularam o cultivo da planta na própria Europa, primeiro em Basileia, que prosperou com isso. "
            "Depois a cultura chegou a Nuremberg, onde a falsificação era tão comum que a cidade criou um código "
            "próprio, o Safranschou, que punia os culpados com multa, prisão e até execução. As fraudes não "
            "acabaram: até hoje se mistura ao açafrão beterraba, fibras de romã, fios de seda tingidos ou os "
            "estames amarelos da própria flor, sem gosto nem cheiro. Outra tática é molhar os fios com mel ou óleo "
            "para que pesem mais. O açafrão em pó é ainda mais fácil de falsificar, com cúrcuma e páprica."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Saffron",
            "The 14th-century Black Death caused demand for saffron-based medicaments to peak, and Europe imported large quantities of threads via Venetian and Genoan ships from southern and Mediterranean lands such as Rhodes. "
            "The theft of one such shipment by noblemen sparked the fourteen-week-long Saffron War. "
            "The conflict and resulting fear of rampant saffron piracy spurred corm cultivation in Basel; it thereby grew prosperous. "
            "The crop then spread to Nuremberg, where endemic and insalubrious adulteration brought on the Safranschou code—whereby culprits were variously fined, imprisoned, and executed. [...] "
            "Adulteration was first documented in Europe's Middle Ages, when those found selling adulterated saffron in Nuremberg were executed under the Safranschou code. "
            "Typical methods include mixing in extraneous substances like beetroot, pomegranate fibres, red-dyed silk fibres, or the saffron crocus's tasteless and odourless yellow stamens. "
            "Other methods included dousing saffron fibres with viscid substances like honey or vegetable oil to increase their weight. "
            "Powdered saffron is more prone to adulteration, with turmeric, paprika, and other powders used as diluting fillers.",
            nome="Saffron")],
    },
    # 5 pimenta no nariz de Ramsés II
    {
        "temas_secundarios": ["egito_antigo", "navegacao_antiga", "comercio_rotas"],
        "tipos_espanto": ["conexao_inesperada", "misterio_aberto"],
        "gancho": "A múmia do faraó Ramsés II, morto em 1213 a.C., tinha grãos de pimenta-do-reino enfiados nas narinas. A pimenta vinha da Índia, e ninguém sabe bem como chegou ao Egito.",
        "explicacao": (
            "Os grãos foram colocados no nariz do faraó como parte dos rituais de mumificação, pouco depois da "
            "morte dele. A pimenta-preta é nativa do sul ou do sudeste da Ásia, talvez da costa do Malabar, na "
            "Índia, onde até hoje é muito cultivada, e a cozinha indiana a conhece desde pelo menos "
            "2000 a.C. O problema é que quase nada se sabe sobre o uso da pimenta no Egito antigo, nem sobre o "
            "caminho que ela fez do Malabar até o Nilo. Os gregos já a conheciam pelo menos desde o século IV "
            "a.C., provavelmente como artigo raro. Os detalhes da rota só chegaram até nós da época do Império "
            "Romano: depois que Roma conquistou o Egito, em 30 a.C., atravessar o mar Arábico em mar aberto até a "
            "costa do Malabar virou quase rotina, e um antigo guia de navegação grego descreve esse comércio. Dali, a carga subia o mar Vermelho, seguia por terra ou por "
            "canal até o Nilo, descia de barcaça até Alexandria e embarcava para a Itália. Em linhas gerais, esse "
            "caminho dominaria o comércio de pimenta para a Europa por um milênio e meio."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Black_pepper",
            "Black pepper is native either to Southeast Asia or South Asia, perhaps including the Malabar Coast of India where the Malabar pepper is extensively cultivated. [...] "
            "Black pepper has been known to Indian cooking since at least 2000 BCE. [...] "
            "Black peppercorns were found stuffed in the nostrils of Ramesses II, placed there as part of the mummification rituals shortly after his death in 1213 BCE. "
            "Little else is known about the use of pepper in ancient Egypt and how it reached the Nile from the Malabar Coast of India. "
            "Pepper (both long and black) was known in Greece at least as early as the fourth century BCE, though it was probably an uncommon and [...] "
            "especially after Rome's conquest of Egypt in 30 BCE, open-ocean crossing of the Arabian Sea direct to Chera dynasty southern India's Malabar Coast was near routine. "
            "Details of this trading across the Indian Ocean have been passed down in the Periplus of the Erythraean Sea. [...] "
            "Returning from India, the ships travelled up the Red Sea, from where the cargo was carried overland or via the Nile-Red Sea canal to the Nile River, barged to Alexandria, and shipped from there to Italy and Rome. "
            "The rough geographical outlines of this same trade route would dominate the pepper trade into Europe for a millennium and a half to come.",
            nome="Black pepper")],
    },
    # 6 o resgate de Alarico
    {
        "temas_secundarios": ["roma_antiga", "dinheiro"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Para levantar o cerco de Roma, em 408, o rei godo Alarico exigiu ouro, prata, túnicas de seda e 3 mil libras de pimenta-do-reino. E recebeu.",
        "explicacao": (
            "No fim de 408, os visigodos de Alarico cercaram Roma, que talvez tivesse até 800 mil habitantes e "
            "fosse a maior cidade do mundo na época. O pânico tomou as ruas. Nas negociações, um enviado romano "
            "perguntou o que sobraria aos cidadãos, e Alarico respondeu: \"A vida deles\". No fim, a cidade teve "
            "de entregar aos godos 5 mil libras de ouro, 30 mil libras de prata, 4 mil túnicas de seda, 3 mil "
            "peles tingidas de escarlate e 3 mil libras de pimenta, em troca do fim do cerco. Para juntar o "
            "valor, cada senador devia contribuir de acordo com seus recursos. A pimenta estava na lista por um "
            "bom motivo: era tão valiosa que muitas vezes servia de garantia de empréstimos e até de moeda. "
            "Séculos antes, Plínio, o Velho, já reclamava que não havia ano em que a Índia não drenasse do Império "
            "Romano 50 milhões de sestércios, e se espantava que um tempero sem doçura nem boa aparência, cuja "
            "única qualidade era um certo ardor, tivesse virado moda a ponto de ser trazido da Índia. Alarico voltaria a Roma, e em 410 a cidade seria saqueada."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Sack_of_Rome_(410)",
                "The sack of Rome on 24 August 410 AD was undertaken by the Visigoths led by their king, Alaric. [...] "
                "The city of Rome may have held as many as 800,000 people, making it the largest in the world at the time. "
                "The Goths under Alaric laid siege to the city in late 408. Panic swept through its streets [...] "
                "One envoy asked what would be left to the citizens of Rome. Alaric replied, \"Their lives.\" "
                "Ultimately, the city was forced to give the Goths 5,000 pounds of gold, 30,000 pounds of silver, 4,000 silken tunics, 3,000 hides dyed scarlet, and 3,000 pounds of pepper in exchange for lifting the siege. [...] "
                "To raise the needed money, Roman senators were to contribute according to their means.",
                nome="Sack of Rome (410)"),
            wiki("Black_pepper",
                "Pliny also complains, \"There is no year in which India does not drain the Roman Empire of 50 million sesterces\", and further moralises on pepper: "
                "It is quite surprising that the use of pepper has come so much into fashion, seeing that in other substances which we use, it is sometimes their sweetness, and sometimes their appearance that has attracted our notice; "
                "whereas, pepper has nothing in it that can plead as a recommendation to either fruit or berry, its only desirable quality being a certain pungency; "
                "and yet it is for this that we import it all the way from India! [...] "
                "Pepper was so valuable that it was often used as collateral or even currency. [...] "
                "Alaric, king of the Visigoths, included 3,000 pounds of pepper as part of the ransom he demanded from Rome when he besieged the city in the fifth century.",
                nome="Black pepper"),
        ],
    },
    # 7 o pássaro da canela e a origem escondida
    {
        "temas_secundarios": ["comercio_rotas", "mitologia"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Por séculos, os europeus não sabiam de onde vinha a canela. Heródoto contou que aves gigantes faziam ninhos com ela, e um cronista do século XIII ouviu que era pescada com redes nas nascentes do Nilo.",
        "explicacao": (
            "A canela era tão valorizada na Antiguidade que servia de presente digno de reis, e os comerciantes "
            "mantiveram sua origem em segredo por séculos, para proteger o monopólio. Heródoto, Aristóteles e "
            "outros autores diziam que ela vinha da Arábia. Segundo Heródoto, aves gigantes buscavam os paus de "
            "canela numa terra desconhecida e com eles faziam ninhos presos a penhascos. Para pegá-los, os árabes "
            "deixavam pedaços de bois perto dos ninhos; as aves levavam a carne para cima, e o peso derrubava os "
            "ninhos. Plínio, o Velho, já desconfiava: para ele, essas histórias eram invenção dos próprios "
            "vendedores para encarecer a mercadoria. Ainda assim, o mistério sobreviveu. Na Idade Média, os "
            "europeus sabiam, pelos autores latinos, que a canela subia o mar Vermelho até os portos do Egito, mas "
            "não de onde ela saía. Em 1248, o cronista Joinville acompanhou o rei Luís IX da França ao Egito e "
            "relatou, acreditando, que ela era pescada com redes na nascente do Nilo, no fim do mundo. A primeira "
            "menção de que a especiaria crescia na região da Índia aparece numa obra de Maimônides, por volta de "
            "1180."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Cinnamon",
                "Cinnamon was so highly prized among ancient nations that it was regarded as a gift fit for monarchs. "
                "Its source was kept a trade secret in the Mediterranean world for centuries by those in the spice trade to protect their monopoly as suppliers. [...] "
                "Herodotus, Aristotle and other authors named Arabia as the source of cinnamon; they recounted that giant \"cinnamon birds\" collected the cinnamon sticks from an unknown land where the cinnamon trees grew and used them to construct their nests. [...] "
                "However, the source of the spice remained a mystery to the Western world. "
                "From reading Latin writers who quoted Herodotus, Europeans had learned that cinnamon came up the Red Sea to the trading ports of Egypt, but where it came from was less than clear. "
                "When the Sieur de Joinville accompanied his king, Louis IX of France to Egypt on the Seventh Crusade in 1248, he reported—and believed—what he had been told: "
                "that cinnamon was fished up in nets at the source of the Nile out at the edge of the world (i.e., Ethiopia). [...] "
                "The first mention that the spice grew in the area of India was in Maimonides's Mishneh Torah, about 1180.",
                nome="Cinnamon"),
            wiki("Cinnamon_bird",
                "used them to construct their nests, fastened to sheer cliffs. The Arabians employed a trick to obtain the cinnamon. "
                "They cut oxen and other beasts of burden into pieces, laid them near the birds' nests and withdrew to a distance; "
                "the birds were then tempted down to carry the chunks of meat back to their nests, where the weight of the carcasses broke them from the cliffs, leaving the Arabians to collect the fallen cinnamon. [...] "
                "Pliny the Elder adopted a more skeptical view of the cinnamon bird [...] "
                "by asserting that the tales were invented by the natives to raise the price of their commodities.",
                nome="Cinnamon bird"),
        ],
    },
    # 8 canela-cássia e cumarina
    {
        "temas_secundarios": ["quimica_cotidiano", "alimentos_perigosos"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "A maior parte da canela vendida no mundo não é a \"canela verdadeira\", e sim a cássia, que pode ter muito mais cumarina. Uma colher de chá pode passar do limite diário recomendado para uma pessoa pequena.",
        "explicacao": (
            "A canela verdadeira, ou canela-do-ceilão, vem de uma árvore do Sri Lanka, mas a maior parte da "
            "canela do comércio internacional sai de outras espécies, chamadas mais corretamente de cássia, como "
            "a chinesa, a indonésia e a vietnamita. A diferença química está na cumarina, uma substância "
            "aromática. Medições citadas na literatura dão à canela-do-ceilão de 0,005 a 0,090 mg de cumarina por "
            "grama, contra 1,74 a 7,67 mg por grama na cássia chinesa. Em doses altas, a cumarina é moderadamente "
            "tóxica para o fígado e os rins de roedores, e a Autoridade Europeia para a Segurança dos Alimentos "
            "confirmou em 2008 uma ingestão diária tolerável de 0,1 mg por quilo de peso. Pelas contas do "
            "instituto alemão de avaliação de riscos, uma colher de chá de cássia em pó tem de 5,8 a 12,1 mg de "
            "cumarina, o que pode superar esse limite para pessoas de menor peso. O instituto, porém, só alerta "
            "contra o consumo alto e diário e diz que um excesso por pouco tempo não é perigoso. A União Europeia "
            "fixou teores máximos de cumarina em massas e produtos de padaria. E a troca também é fraude: amostras de mercado "
            "vendidas como canela-do-ceilão já apareceram com cumarina demais, sinal de mistura com cássia."
        ),
        "nivel": 2, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Cinnamon",
                "is considered to be \"true cinnamon\", but most cinnamon in international commerce is derived from four other species, usually and more correctly referred to as \"cassia\": "
                "C. burmanni (Indonesian cinnamon or Padang cassia), C. cassia (Chinese cinnamon or Chinese cassia), C. loureiroi (Saigon cinnamon or Vietnamese cassia) [...] "
                "In 2008, the European Food Safety Authority considered the toxicity of coumarin, a component of cinnamon, and confirmed a maximum recommended tolerable daily intake (TDI) of 0.1 mg of coumarin per kg of body weight. "
                "Coumarin is known to cause liver and kidney damage in high concentrations [...] "
                "the European Union set a guideline for maximum coumarin content in foodstuffs of 50 mg per kg of dough in seasonal foods, and 15 mg per kg in everyday baked foods. [...] "
                "but market samples contained coumarin with levels as high as 3462 mg/kg, indicating probable contamination with cassia in the counterfeit cinnamon.",
                nome="Cinnamon"),
            wiki("Coumarin",
                "Coumarin is moderately toxic to the liver and kidneys of rodents [...] "
                "Ceylon cinnamon or true cinnamon (Cinnamomum verum): 0.005 to 0.090 mg/g Chinese cinnamon or Chinese cassia (C. cassia): 1.74 to 7.67 mg/g [...] "
                "The German Federal Institute for Risk Assessment has established a tolerable daily intake (TDI) of 0.1 mg coumarin per kg body weight, but also advises that higher intake for a short time is not dangerous. [...] "
                "One teaspoon of cassia cinnamon powder therefore contains 5.8 to 12.1 mg of coumarin, which may be above the tolerable daily intake value for smaller individuals. "
                "However, the BFR only cautions against high daily intake of foods containing coumarin.",
                nome="Coumarin"),
        ],
    },
    # 9 pimenta-de-sichuan e jambu: o tempero que vibra
    {
        "temas_secundarios": ["sentidos", "comida_brasileira", "plantas"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "A pimenta-de-sichuan, parente dos cítricos, deixa a boca dormente e formigando, como se vibrasse a uns 50 hertz. O jambu do tacacá, de outra família de plantas, faz algo parecido com outra molécula.",
        "explicacao": (
            "Apesar do nome, a pimenta-de-sichuan não é parente próxima da pimenta-do-reino nem das pimentas do "
            "gênero Capsicum: é a casca seca do fruto de plantas da família dos cítricos e da arruda. O efeito "
            "vem de uma molécula, o hidroxi-alfa-sanshool, e é descrito como uma dormência formigante parecida "
            "com uma vibração de 50 hertz, típica de certos sensores mecânicos de vibração do corpo humano. O sanshool tem "
            "estrutura semelhante à da capsaicina, mas parece agir sobretudo bloqueando canais de potássio, e "
            "excita fibras nervosas ligadas ao tato leve. O escritor de culinária Harold McGee compara a "
            "sensação à de bebidas gaseificadas ou à de encostar na língua os polos de uma bateria de 9 volts. Na "
            "China, ela se junta às pimentas vermelhas no sabor chamado málà, \"dormência e ardor\". No Pará, um efeito "
            "parecido vem do jambu, planta da família das margaridas, usada em pratos como o tacacá. O botão da "
            "flor dá um formigamento forte, dormência e muita saliva. O responsável ali é outra molécula, o "
            "espilantol, que pertence ao mesmo grupo químico, o das amidas de ácidos graxos."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Sichuan_pepper",
                "Sichuan pepper (Chinese: 花椒; pinyin: huājiāo) is a spice made from the dried pericarp (outer shell of the fruit) of a plant of the genus Zanthoxylum in the family Rutaceae. [...] "
                "Despite its name, Sichuan pepper is not closely related to black pepper or chili pepper. "
                "Instead, Zanthoxylum plants are in the same family as citrus and rue. [...] "
                "is often added to chili peppers to create a flavor known as málà (Chinese: 麻辣; 'numb-spiciness'). [...] "
                "induces a tingling numbness in the mouth, akin to a 50-hertz vibration (typical of RA1 mechanical vibrotactile sensors in humans), due to the presence of hydroxy-alpha sanshool. "
                "Food historian Harold McGee describes the effect of sanshools thus: \"...they produce a strange, tingling, buzzing, numbing sensation that is something like the effect of carbonated drinks or of a mild electric current (touching the terminals of a nine-volt battery to the tongue).",
                nome="Sichuan pepper"),
            wiki("Hydroxy-alpha-sanshool",
                "The chemical structure of hydroxy-alpha-sanshool resembles capsaicin as both are fatty acid amides, but the mechanism of action by which it induces nerve sensations has been a matter of debate. [...] "
                "evidence suggests that the inhibition of tandem pore domain potassium channels KCNK3, KCNK9, and KCNK18 are primarily responsible for sanshool's effects. "
                "Hydroxy-alpha-sanshool excites D-hair afferent nerve fibers, a distinct subset of the sensitive light touch receptors in the skin",
                nome="Hydroxy-alpha-sanshool"),
            wiki("Acmella_oleracea",
                "Acmella oleracea is a species of flowering herb in the family Asteraceae. "
                "Common names include toothache plant, Szechuan buttons, paracress, jambu, buzz buttons, tingflowers and electric daisy. [...] "
                "Both fresh and cooked leaves are used in dishes such as stews like tacacá in northern Brazil, especially in the state of Pará. [...] "
                "The flower bud has a grassy taste followed by a strong tingling or numbing sensation and often excessive salivation [...] "
                "The most important taste-active molecules present are fatty acid amides such as spilanthol, which is responsible for the trigeminal and saliva-inducing effects of the plant.",
                nome="Acmella oleracea"),
        ],
    },
    # 10 anis-estrelado e o Tamiflu
    {
        "temas_secundarios": ["farmacos", "doencas_infecciosas", "plantas"],
        "tipos_espanto": ["conexao_inesperada", "escala_absurda"],
        "gancho": "O remédio contra a gripe Tamiflu nasceu de uma molécula tirada do anis-estrelado. Até 2012, a fabricante chegou a usar até 90% da safra mundial do tempero para produzi-lo.",
        "explicacao": (
            "O anis-estrelado, fruto em forma de estrela de uma árvore nativa do sul da China e do norte do Vietnã, "
            "é a principal fonte do ácido chiquímico, ponto de partida da síntese do oseltamivir, o princípio ativo do Tamiflu. O "
            "remédio foi descoberto por cientistas da empresa Gilead justamente a partir dessa molécula, que no "
            "início só podia ser obtida como extrato do anis-estrelado chinês. A Gilead licenciou as patentes à "
            "Roche em 1996, e a Roche chegou a consumir até 90% da safra anual de anis-estrelado do mundo para "
            "fazer o medicamento. A saída veio da "
            "biotecnologia: em 2005 foi descoberto um método industrial de produzir ácido chiquímico pela "
            "fermentação da bactéria E. coli, e em 2006 cerca de 30% do suprimento já vinha dela. O método foi "
            "usado na pandemia de gripe suína de 2009 para enfrentar a falta de Tamiflu e acabou revertendo a alta "
            "de preço do anis-estrelado. Em 2012, a Roche trocou o tempero por E. coli geneticamente "
            "modificada. Atenção: o anis-estrelado chinês não é tóxico, mas uma espécie parecida, o "
            "anis-estrelado-japonês, é muito tóxica e não se come."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Illicium_verum",
                "is a medium-sized evergreen tree native to South China and northeast Vietnam. Its star-shaped pericarp fruits harvested just before ripening are a spice [...] "
                "Until 2012, when it switched to using genetically modified E. coli, Roche Pharmaceuticals used up to 90% of the world's annual star anise crop to produce oseltamivir (Tamiflu) via shikimic acid. [...] "
                "Star anise is the major source of the chemical compound shikimic acid, a primary precursor in the pharmaceutical synthesis of the anti-influenza drug oseltamivir (Tamiflu). "
                "An industrial method for the production of shikimic acid using fermentation of E. coli bacteria was discovered in 2005, "
                "and applied in the 2009 swine flu pandemic to address Tamiflu shortages, eventually reversing price increases for star anise as a raw material of shikimic acid. [...] "
                "Illicium verum is not toxic. However, other related species are toxic. "
                "Japanese star anise (Illicium anisatum), a similar tree, is highly toxic and inedible",
                nome="Illicium verum"),
            wiki("Oseltamivir",
                "Oseltamivir was discovered by scientists at Gilead Sciences using shikimic acid as a starting point for synthesis; "
                "shikimic acid was originally available only as an extract of Chinese star anise; "
                "but by 2006, 30% of the supply was manufactured recombinantly in E. coli. "
                "Gilead exclusively licensed their relevant patents to Roche in 1996.",
                nome="Oseltamivir"),
        ],
    },
    # 11 o massacre de Banda
    {
        "temas_secundarios": ["imperios_coloniais", "grandes_navegacoes"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Para controlar a noz-moscada, a Companhia Holandesa das Índias Orientais massacrou e expulsou o povo das ilhas Banda em 1621. Depois teve de devolver centenas de sobreviventes às ilhas: os colonos não sabiam cultivá-la.",
        "explicacao": (
            "Até meados do século XIX, as ilhas Banda, na atual Indonésia, eram a única fonte do mundo de "
            "noz-moscada e de macis. Em 1621, o governador-geral da companhia, Jan Pieterszoon Coen, desembarcou "
            "soldados bem armados nas ilhas e obrigou os líderes locais, os orang kaya, a assinar sob a mira de "
            "armas um tratado impossível de cumprir. As supostas violações serviram de pretexto para um massacre "
            "punitivo. Mercenários japoneses contratados pelos holandeses decapitaram 40 dos líderes e expuseram "
            "as cabeças em lanças de bambu. Antes da conquista, as ilhas tinham por volta de 13 mil a 15 mil "
            "habitantes. Os números exatos de mortos, expulsos e fugidos são incertos, mas as fontes sugerem que "
            "só cerca de mil bandaneses ficaram nas ilhas, como trabalhadores forçados. A maioria dos sobreviventes fugiu para "
            "ilhas de parceiros comerciais, e outros foram mandados como escravos para Batávia, a atual Jacarta. As terras viraram 68 "
            "lotes entregues a colonos holandeses, trabalhados por escravos trazidos de fora. Só que faltava aos "
            "recém-chegados saber cultivar noz-moscada, e uns 530 bandaneses enviados a Batávia foram devolvidos "
            "às ilhas por causa dessa experiência."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Banda_Islands",
            "Until the mid-19th century the Banda Islands were the world's only source of the spices nutmeg and mace, produced from the nutmeg tree. [...] "
            "Newly appointed VOC governor-general Jan Pieterszoon Coen set about enforcing Dutch monopoly over the Banda's spice trade. "
            "In 1621 well-armed soldiers were landed on Bandaneira Island [...] "
            "The orang kaya were forced at gunpoint to sign an unfeasibly arduous treaty, one that was in fact impossible to keep, thus providing Coen an excuse to use superior Dutch force against the Bandanese. "
            "The Dutch quickly noted a number of alleged violations of the new treaty, in response to which Coen launched a punitive massacre. "
            "Japanese mercenaries were hired to deal with the orang kaya, forty of whom were beheaded with their heads impaled and displayed on bamboo spears. [...] "
            "The Dutch carved 68 parcels out of the islands after the enslavement and slaughter of the natives. "
            "The population of the Banda Islands prior to Dutch conquest is generally estimated to have been around 13,000–15,000 people [...] "
            "The actual numbers of Bandanese who were killed, forcibly expelled or fled the islands in 1621 remain uncertain. "
            "But readings of historical sources suggest around one thousand Bandanese likely survived in the islands, and were spread throughout the nutmeg groves as forced labourers. [...] "
            "Most survivors fled as refugees to the islands of their trading partners [...] "
            "Shipments of surviving Bandanese were also sent to Batavia (Jakarta) to work as slaves in developing the city and its fortress. "
            "Some 530 of these individuals were later returned to the islands because of their much-needed expertise in nutmeg cultivation (something sorely lacking among newly arrived Dutch [...] "
            "With few Bandanese left to work them, slaves from elsewhere were brought in.",
            nome="Banda Islands")],
    },
    # 12 cardamomo da Guatemala
    {
        "temas_secundarios": ["comercio_rotas", "cafe_cha_cacau"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "O cardamomo é nativo da Índia, mas em 1979–1980 a Guatemala passou a produzir mais que os indianos. Quem levou a planta para lá foi um cafeicultor alemão, e os guatemaltecos quase não a consomem.",
        "explicacao": (
            "A espécie cultivada na Guatemala, Elettaria cardamomum, é nativa da costa do Malabar, na Índia, e o "
            "cardamomo aparece já em registros dos sumérios e da medicina ayurvédica. A planta chegou à América "
            "Central antes da Primeira Guerra Mundial, levada por um cafeicultor alemão, Oscar Majus Kloeffer. "
            "Depois da Segunda Guerra, a produção guatemalteca subiu para 13 a 14 mil toneladas por ano, e na "
            "safra de 1979–1980 o país superou a Índia na produção mundial. Em 2022, Índia, Indonésia e Guatemala "
            "somaram 85% da produção mundial, numa estatística da ONU que inclui noz-moscada e macis. Um único departamento guatemalteco, Alta Verapaz, produz 70% do "
            "cardamomo do país. O curioso é para onde vai tanta especiaria: o consumo local na Guatemala é "
            "irrisório, e quase tudo é exportado. Na Índia é o contrário: cerca de 95% da produção fica no "
            "próprio país, que é de longe o maior consumidor. Entre os grandes importadores estão a Arábia "
            "Saudita e o Kuwait. No Oriente Médio, o cardamomo moído é um tempero tradicional do café e do chá, "
            "e em alguns países os grãos de café e de cardamomo são moídos juntos num pilão de madeira."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Cardamom",
            "The first references to cardamom are found in Sumer, and in Ayurveda. [...] "
            "In 2022, world production of cardamom (included with nutmeg and mace for reporting to the United Nations) was 138,888 tonnes, "
            "led by India, Indonesia and Guatemala, which together accounted for 85% of the total (table). [...] "
            "In 1979–1980, Guatemala surpassed India in worldwide production. "
            "Guatemala cultivates Elettaria cardamomum, which is native to the Malabar Coast of India. "
            "Alta Verapaz Department produces 70 percent of Guatemala's cardamom. "
            "Cardamom was introduced to Guatemala before World War I by the German coffee planter Oscar Majus Kloeffer. "
            "After World War II, production was increased to 13,000 to 14,000 tons annually. [...] "
            "Importing leaders mentioned are Saudi Arabia and Kuwait [...] "
            "However, some 95% of cardamom produced in India is for domestic purposes, and India is itself by far the most important consuming country for cardamoms in the world. [...] "
            "In contrast, Guatemala's local consumption is negligible, which supports the exportation of most of the cardamom that is produced. [...] "
            "In the Middle East, green cardamom powder is used as a spice for sweet dishes, and as a traditional flavouring in coffee and tea. [...] "
            "In some Middle Eastern countries, coffee and cardamom are often ground in a wooden mortar",
            nome="Cardamom")],
    },
    # 13 curcumina, a falsa promessa
    {
        "temas_secundarios": ["farmacos", "historia_medicina"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "A curcumina, pigmento da cúrcuma e ingrediente comum de suplementos, dá positivo na maioria dos testes usados para descobrir remédios. Por isso mesmo os químicos a tratam como pista falsa.",
        "explicacao": (
            "A curcumina é o pigmento amarelo da cúrcuma, ou açafrão-da-terra, e aparece em muitos suplementos. "
            "Nos ensaios usados para descobrir remédios, ela costuma dar positivo, mas os químicos medicinais a "
            "classificam entre os \"compostos de interferência pan-ensaio\": substâncias que interferem nos próprios testes "
            "e podem levar a interpretações erradas. Ela atrai atenção experimental, mas não avança como remédio. Além disso, é "
            "instável, insolúvel em água e mal absorvida: muito pouca curcumina escapa do trato digestivo, e a "
            "maior parte sai nas fezes sem alteração. Entre 1995 e 2017, o governo dos Estados Unidos financiou "
            "150 milhões de dólares em pesquisas sobre ela, sem achar apoio para seu uso como tratamento. Apesar "
            "de muitos estudos de laboratório e clínicos, ela não tem uso médico reconhecido. A área também teve "
            "escândalo: Bharat Aggarwal, ex-pesquisador de câncer do MD Anderson, no Texas, que estudava "
            "propriedades anticâncer de temperos, sobretudo da curcumina, teve 29 artigos retratados por fraude "
            "até julho de 2021. E entre 2018 e 2023 a agência americana FDA enviou 29 cartas de advertência a "
            "fabricantes de suplementos com curcumina que alegavam falsos efeitos contra doenças."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Curcumin",
            "Extensive studies have consistently failed to show any medical value for curcumin. "
            "It is difficult to study because it is both unstable and poorly bioavailable. [...] "
            "Curcumin, which shows positive results in most drug discovery assays, is regarded as a false lead that medicinal chemists include among \"pan-assay interference compounds\". "
            "This attracts undue experimental attention while failing to advance as viable therapeutic or drug leads [...] "
            "Factors that limit the bioactivity of curcumin or its analogs include chemical instability, water insolubility, absence of potent and selective target activity, low bioavailability [...] "
            "Very little curcumin escapes the GI tract and most is excreted in feces unchanged. [...] "
            "Although curcumin has been assessed in numerous laboratory and clinical studies, it has no medical uses. [...] "
            "Curcumin exhibits numerous interference properties which may lead to misinterpretation of results. "
            "Between 1995 and 2017, the US government funded US$150 million in biomedical research into curcumin through the National Center for Complementary and Integrative Health. "
            "No support was found for curcumin as a medical treatment. [...] "
            "Bharat Aggarwal, a former cancer researcher at the University of Texas MD Anderson Cancer Center, had 29 papers retracted due to research fraud as of July 2021. "
            "Aggarwal's research had focused on potential anti-cancer properties of herbs and spices, particularly curcumin [...] "
            "Between 2018 and 2023, the U.S. FDA issued 29 warning letters to American manufacturers of dietary supplements for making false claims of anti-disease effects",
            nome="Curcumin")],
    },
    # 14 a bomba de óleo de mostarda
    {
        "temas_secundarios": ["plantas", "quimica_cotidiano"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "A semente de mostarda não arde enquanto está inteira: a planta guarda o ingrediente e a enzima que geram o ardor em células separadas. Por isso a mostarda forte é feita com água fria, e não quente.",
        "explicacao": (
            "O mecanismo é uma defesa contra animais que comem a planta, apelidada de \"bomba de óleo de "
            "mostarda\". As sementes guardam substâncias inofensivas, os glucosinolatos, e uma enzima, a "
            "mirosinase. Para não se envenenar, a planta mantém as duas coisas em compartimentos ou células "
            "diferentes, que só se encontram quando o tecido é danificado. Ao ser mastigada, cortada ou moída, a "
            "semente libera a enzima, que transforma os glucosinolatos em isotiocianatos, o chamado óleo de "
            "mostarda, picante e tóxico para pragas. Na cozinha, isso explica a receita: misturar o pó das "
            "sementes com água dispara a reação. Líquidos quentes e ácidos fortes, como o vinagre, desnaturam a "
            "enzima e deixam o condimento mais suave. Por isso, com tudo mais igual, mostarda feita com água "
            "fria fica mais forte do que feita com água quente. O mesmo sistema dá boa parte do ardor da raiz-forte e do "
            "wasabi, que é ativado quando ele é ralado."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Mustard_(condiment)",
                "Mixing ground mustard seeds with water causes a chemical reaction between two compounds in the seed: the enzyme myrosinase and various glucosinolates such as sinigrin and sinalbin. "
                "The myrosinase enzyme turns the glucosinolates into various isothiocyanate compounds known generally as mustard oil. [...] "
                "The temperature of the water and concentration of acids, such as vinegar, also determine the strength of a prepared mustard; "
                "hotter liquids and stronger acids denature the enzymes that give mustard its strong flavour. "
                "Thus, \"hot\" mustard is made with cold water, whereas using hot water produces a milder condiment, all else being equal.",
                nome="Mustard (condiment)"),
            wiki("Myrosinase",
                "is a family of enzymes involved in plant defense against herbivores, specifically the mustard oil bomb. [...] "
                "When the plant is attacked by pathogens, insects, or other herbivores, the plant uses myrosinase to convert glucosinolates, which are otherwise-benign, into toxic products like isothiocyanates, thiocyanates, and nitriles. [...] "
                "Myrosinase is responsible for generating much of the characteristic pungency of mustard, horseradish and wasabi. "
                "Myrosinase is found in specialist myrosin cells within mustard seeds. "
                "Upon crushing them, myrosinase is released and hydrolyses the glucosinolates present in the seed. [...] "
                "In wasabi, the action of grating similarly activates endogenous myrosinase",
                nome="Myrosinase"),
            wiki("Glucosinolate",
                "The pungency of those plants is due to mustard oils produced from glucosinolates when the plant material is chewed, cut, or otherwise damaged. [...] "
                "To prevent damage to the plant itself, the myrosinase and glucosinolates are stored in separate compartments of the cell or in different cells in the tissue, and come together only or mainly under conditions of physical injury",
                nome="Glucosinolate"),
        ],
    },
]
