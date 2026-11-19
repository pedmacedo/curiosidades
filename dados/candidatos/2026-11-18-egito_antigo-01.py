LOTE = "2026-11-18-egito_antigo-01"
AREA = "historia_antiga"
TEMA = "egito_antigo"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o diário de Merer: o papiro mais antigo fala da Grande Pirâmide
    {
        "temas_secundarios": ["grandes_obras", "sistemas_escrita"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Os papiros com texto mais antigos que se conhecem são o diário de bordo de um inspetor chamado Merer, que levava de barco blocos de calcário para Gizé no reinado de Quéops, o faraó da Grande Pirâmide.",
        "explicacao": (
            "Os papiros foram achados em 2013 por uma missão francesa liderada por Pierre Tallet e Gregory "
            "Marouard, em Wadi al-Jarf, no litoral do mar Vermelho, enterrados diante de cavernas escavadas para "
            "guardar barcos. Têm mais de 4.500 anos. Merer era um funcionário de escalão médio, com o título de "
            "inspetor, e comandava cerca de quarenta barqueiros. O que ele anotou é quase uma planilha: no alto, o mês e a "
            "estação; embaixo, os dias, e para cada dia o que a equipe fez e onde dormiu. As partes mais inteiras "
            "registram meses de viagens levando calcário branco das pedreiras de Tura até Gizé. A cada dez dias, "
            "mais ou menos, a turma fazia duas ou três viagens de ida e volta, com talvez 30 blocos de 2 a 3 "
            "toneladas cada, cerca de 200 blocos por mês. O diário não diz onde as pedras seriam usadas, mas Tallet "
            "acha provável que fossem para o revestimento externo da Grande Pirâmide, cujo nome original aparece no "
            "texto: Akhet-Khufu, \"Horizonte de Quéops\". O arqueólogo egípcio Zahi Hawass chamou o achado de a maior "
            "descoberta no Egito no século XXI."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Diary_of_Merer",
            "papyrus logbooks written over 4,500 years ago by Merer, a middle-ranking official with the title inspector (sḥḏ, sehedj). "
            "They are the oldest known papyri with text [...] the reign of Pharaoh Khufu [...] "
            "The best preserved sections (Papyrus Jarf A and B) document the transportation of white limestone blocks from the Tura quarries to Giza by boat. "
            "Buried in front of man-made caves that served to store the boats at Wadi al-Jarf on the Red Sea coast, the papyri were found and excavated in 2013 by a French mission under the direction of archaeologists Pierre Tallet of Paris-Sorbonne University and Gregory Marouard. [...] "
            "The Egyptian archaeologist Zahi Hawass describes the Diary of Merer as \"the greatest discovery in Egypt in the 21st century.\" [...] "
            "Though the diary does not specify where the stones were to be used or for what purpose, given the diary may date to what is widely considered the very end of Khufu's reign, Tallet believes they were most likely for cladding the outside of the Great Pyramid. "
            "About every ten days, two or three round trips were done, shipping perhaps 30 blocks of 2–3 tonnes each, amounting to 200 blocks per month. "
            "About forty boatmen worked under Merer. [...] "
            "At the top there is a heading naming the month and the season. Under that there is a horizontal line listing the days of the months. [...] "
            "The diary also mentions the original name of the Great Pyramid: Akhet-Khufu, meaning \"Horizon of Khufu\".",
            nome="Diary of Merer")],
    },
    # 2 a adaga de Tutancâmon é feita de meteorito
    {
        "temas_secundarios": ["asteroides_cometas", "elementos_quimicos"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "A lâmina de ferro de uma adaga enterrada com Tutancâmon veio do espaço: a composição, com cerca de 11% de níquel e 0,6% de cobalto, bate com a dos meteoritos de ferro.",
        "explicacao": (
            "Tutancâmon reinou por volta de 1334 a 1325 a.C., em plena Idade do Bronze, quando fundir ferro era "
            "coisa rara. Objetos de ferro serviam para arte, rituais e presentes reais, não para o dia a dia. No "
            "túmulo dele havia dezenove objetos de ferro, e alguns foram enrolados junto com a múmia, entre eles uma "
            "lâmina de adaga com cabo de ouro. Desde a década de 1960, o alto teor de níquel da lâmina era visto como "
            "sinal de origem meteorítica. Um estudo publicado em junho de 2016, com espectrometria de fluorescência "
            "de raios X, confirmou: a lâmina é quase toda de ferro, com cerca de 11% de níquel e 0,6% de cobalto, "
            "proporções compatíveis com as de meteoritos de ferro conhecidos. E não é um caso isolado. No Egito, os "
            "indícios de fundição de ferro só começam no século VI a.C., mas o uso mais antigo de ferro metálico "
            "conhecido vem quase três milênios antes, de um enterro de Naqada II, por volta de 3400 a.C. Um estudo "
            "de 2013 mostrou que o ferro desse achado também veio de um meteorito. Os egípcios trabalharam metal "
            "caído do céu muito antes de saber tirar ferro das rochas."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Tutankhamun%27s_meteoric_iron_dagger",
            "the ancient Egyptian Pharaoh Tutankhamun (reigned c. 1334–1325 BC). "
            "The iron material for the blade is believed to have originated from a meteorite due to its chemical composition. [...] "
            "At the time of King Tutankhamun's mummification in approximately 1323 BC (the Bronze Age), iron smelting and manufacture were rare. "
            "Iron objects were used for only artistic, ornamental, ritual, gift giving and ceremonial purposes as well as for pigmentation. [...] "
            "Nineteen iron objects were discovered in the tomb of Tutankhamun [...] "
            "Other iron objects were wrapped with Tutankhamun's mummy; these include a miniature headrest contained inside the golden death mask, an amulet attached to a golden bracelet and a dagger blade with gold haft. [...] "
            "Since the 1960s, the high nickel content in the blade has been accepted as indicative of meteoric origin. "
            "A more recent study published in June 2016 derived from x-ray fluorescence spectrometer analysis shows that the blade's composition is mostly iron (Fe) and 11% nickel (Ni) and 0.6% cobalt (Co), consistent with the composition of known iron meteorites. "
            "Evidence of iron smelting in Egypt begins in the 6th century BC, but the earliest known use of metallic iron is almost three millennia earlier, from a Naqada II burial c. 3400 BC. "
            "A 2013 study determined that the iron from that find was also of meteorite origin.",
            nome="Tutankhamun's meteoric iron dagger")],
    },
    # 3 marrom-múmia: tinta feita de múmias
    {
        "temas_secundarios": ["pigmentos", "pintura"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Pintores europeus usaram por mais de um século uma tinta feita de múmias egípcias moídas, o \"marrom-múmia\". Quando soube disso, o pintor Edward Burne-Jones enterrou o seu tubo no jardim.",
        "explicacao": (
            "O pigmento era feito com a carne de múmias, misturada com piche branco e mirra, e dava um marrom "
            "transparente, entre a terra de sombra queimada e a natural. Antes disso, as múmias já tinham fama de "
            "remédio e eram usadas contra males que iam da dor de dente à disenteria. O registro mais antigo do uso "
            "como tinta é de 1712, quando uma loja de material artístico em Paris, chamada \"À la momie\", vendia "
            "tintas, verniz e múmia em pó. A cor fez sucesso de meados do século XVIII ao XIX, sobretudo entre os "
            "pré-rafaelitas. Às vezes faltavam múmias egípcias de verdade, e corpos recentes de escravizados ou de "
            "criminosos as substituíam. Depois da Revolução Francesa, corações de reis da França retirados da abadia "
            "de Saint-Denis também viraram tinta. Em 1881, Burne-Jones, que achava que o nome era só uma "
            "descrição da cor, ouviu do colega Lawrence Alma-Tadema que ele tinha visto uma múmia na oficina do "
            "fornecedor antes de ser moída, e quis dar ao tubo um \"enterro decente\" na hora. Em 1915, um fabricante "
            "de Londres dizia que uma única múmia bastaria para atender os clientes por vinte anos. Em 1964, a revista "
            "Time noticiou que o último fornecedor, a C. Roberson, tinha ficado sem múmias alguns anos antes."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Mummy_brown",
            "Mummy brown, also known as Egyptian brown or Caput Mortuum, is a shade of brown   with good transparency, sitting between burnt umber and raw umber in tint. "
            "Its bituminous pigment was made from the flesh of mummies mixed with white pitch and myrrh. "
            "Mummy brown was extremely popular from the mid-eighteenth to the nineteenth centuries, predominantly with Western European artists. [...] "
            "Mummy brown was one of the favourite colours of the Pre-Raphaelites. [...] "
            "People used materials derived from mummies to treat a wide range of medical complaints, from toothaches to dysentery. [...] "
            "The earliest record of the use of mummy brown dates back to 1712 when an artist supply shop called \"À la momie\" in Paris sold paints, varnish, and powdered mummy. [...] "
            "However, the demand for mummy brown sometimes exceeded the available supply of true Egyptian mummies, leading to occasional substitution of contemporary corpses of enslaved people or criminals. "
            "In aftermath of the French Revolution, the hearts of French kings were taken from the then Abbey of Saint-Denis, and used to make paint. [...] "
            "In 1881, the artist Edward Burne-Jones (a member of the so-called \"Pre-Raphaelite Brotherhood\") was reported to have ceremonially buried his tube of mummy brown in his garden when he discovered its true origins. "
            "According to Georgiana Burne-Jones, \"Edward scouted the idea of the pigment having anything to do with a mummy − said the name must be only borrowed to describe a particular shade of brown,\" but after being assured by fellow painter Lawrence Alma-Tadema, who saw a mummy in his colourman workshop before it was ground up, Edward insisted on giving his only tube of mummy brown a \"decent burial there and then.\" [...] "
            "By 1915, demand for mummy brown had slowed so much that one London colourman claimed he could satisfy his customers' requests for twenty years from a single Egyptian mummy. [...] "
            "In 1964, Time magazine reported that the sole distributor of the pigment, London colourmaker C. Roberson, had run out of mummies a few years prior.",
            nome="Mummy brown")],
    },
    # 4 múmias de animais em escala industrial, muitas falsas
    {
        "temas_secundarios": ["religioes", "comercio_rotas"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Os egípcios mumificaram animais aos milhões como oferenda aos deuses: só em Tuna el-Gebel há cerca de quatro milhões de íbis. Muitas dessas múmias são \"falsas\", com só uns ossos, penas ou cacos dentro.",
        "explicacao": (
            "Quem queria um favor de um deus deixava uma oferenda no templo. No começo, eram estatuetas de bronze "
            "de animais; depois, as múmias de animais, uma alternativa mais barata, viraram a oferenda mais popular. "
            "Os bichos eram criados nos próprios templos e vendidos já mumificados a peregrinos e moradores. "
            "Tomografias, que examinam o esqueleto sem desfazer as faixas, sugerem que eles eram criados só para "
            "isso, e muitos tinham o pescoço quebrado. Gatos dedicados à deusa Bastet costumavam morrer "
            "estrangulados ou com o pescoço partido. A escala é de fábrica. O culto à íbis, ave do deus Toth, "
            "concentra-se nos períodos ptolomaico e romano, e uma datação por radiocarbono de 2015 situou as múmias "
            "estudadas entre cerca de 450 e 250 a.C. Saqqara guarda quase 500 mil delas e teria produzido 10 mil "
            "oferendas mumificadas por ano. Com a produção em massa, o capricho diminuiu: estudos mostraram que muitas "
            "oferendas grandes são \"falsas\", com apenas alguns ossos, penas, juncos, madeira ou pedaços de cerâmica "
            "dentro das faixas. Um ex-diretor do Museu de História Natural britânico desenrolou várias múmias de gato "
            "e achou muitas recheadas só com partes avulsas de gatos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Animal_mummy",
            "If an Egyptian sought a favor from a deity, an offering would be made or purchased, then placed at the appropriate temple. "
            "Before animal mummification became common, these offerings were usually bronze statues depicting the animals. "
            "However, eventually animal mummies—a cheaper alternative to bronze statues—became the most popular form of offering. "
            "As such, millions of these mummified animals have been discovered throughout Egypt. "
            "Inspection of those mummies, usually done through CT scans which allow researchers to examine the skeletons of the mummies without damaging the outer wrappings, has suggested that these types of animals were bred for the sole purpose of offerings. "
            "As the process of animal mummification for the purpose of offerings grew, mummification techniques became progressively less meticulous. "
            "Studies have revealed many of the large-scale animal offerings to be \"fakes\" (the wrappings containing only a few bones, feathers, reeds, wood, or pieces of pottery). "
            "The animals were raised on temple grounds and then sold to pilgrims or regular citizens. "
            "The necks of the animals were often broken [...] "
            "Cats were mummified as religious offerings in enormous quantities and were believed to represent the war goddess Bastet. [...] "
            "Cats who were bred to become offerings of this type usually died due to strangulation or the breaking of their necks. [...] "
            "Sir T. C. S. Morrison-Scott, former Director of the British Museum of Natural History, unwrapped a large number of cat mummies, but discovered many were simply stuffed with random body parts of cats and not mummified with detailed care. [...] "
            "The ibis cult was established primarily during the Ptolemaic and Roman periods and was dedicated to the god of wisdom, Thoth. "
            "Research from 2015 using 14C radiocarbon dating suggests that the Egyptian ibis mummies in the study were from time frame that falls between approximately 450 BCE and 250 BCE. [...] "
            "Saqqara alone is estimated to contain nearly 500,000 of these mummies and is also thought to have produced 10,000 mummified offerings per year. "
            "In addition, approximately four million ibis burials have been uncovered at the catacombs of Tuna el-Gebel.",
            nome="Animal mummy")],
    },
    # 5 a greve de Deir el-Medina
    {
        "temas_secundarios": ["economia_curiosa", "leis_julgamentos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Por volta de 1170 a.C., os artesãos que decoravam os túmulos dos faraós cruzaram os braços porque a comida não chegava. \"Estamos com fome\", disseram. Pode ter sido a primeira greve registrada.",
        "explicacao": (
            "Os trabalhadores moravam em Deir el-Medina, vila a uma curta caminhada do Vale dos Reis, e eram "
            "funcionários do Estado. Recebiam em rações, até três vezes o que ganhava um trabalhador do campo, e hoje seriam "
            "considerados classe média. No 29º ano do reinado de Ramsés III, cansados dos atrasos no abastecimento, "
            "largaram as ferramentas e abandonaram o serviço, no que pode ter sido a primeira greve com ocupação da "
            "história registrada. Escreveram ao vizir reclamando da falta de trigo. Os líderes da vila tentaram "
            "convencê-los, mas eles responderam com \"grandes juramentos\" e diziam que dezoito dias do mês já "
            "tinham passado sem as rações; tiveram de comprar o próprio trigo. Exigiram que o caso fosse levado ao "
            "faraó ou ao vizir. Quando as autoridades ouviram e atenderam as queixas, voltaram ao trabalho no dia "
            "seguinte. Outras paralisações vieram, até o abastecimento se normalizar. Como os chefes da vila tinham "
            "ficado do lado das autoridades, os trabalhadores deixaram de confiar neles e passaram a escolher "
            "representantes próprios. Há queixas dos artesãos registradas ainda quarenta e cinquenta anos depois, sob "
            "Ramsés IX e Ramsés X."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Deir_el-Medina",
            "is an ancient Egyptian workmen's village that was home to the artisans who worked on the tombs in the Valley of the Kings [...] "
            "within easy walking distance of the Valley of the Kings [...] "
            "Based on analysis of income and prices, the workmen of the village would, in modern terms, be considered middle class. "
            "As salaried state employees they were paid in rations at up to three times the rate of agricultural labourers [...] "
            "In about the 29th year of the reign of Ramesses III (c. 1170 BC) the tomb laborers were so exasperated by delays in supplies that they threw down their tools and walked off the job in what may have been the first sit-down strike action in recorded history. "
            "They wrote a letter to the vizier complaining about lack of wheat rations. "
            "Village leaders attempted to reason with them but they refused to return to work until their grievances were addressed. "
            "They responded to the elders with \"great oaths\". \"We are hungry\", the crews claimed; \"eighteen days have passed this month\" and they still had not received their rations. "
            "They were forced to buy their own wheat. They told the leaders to send to the pharaoh or vizier to address their concerns. "
            "After the authorities had heard their complaints they addressed them and the workers went back to work the next day. "
            "Several strikes followed. [...] "
            "they soon restored the regular wheat supplies and the strikes came to an end for the remaining years of Ramesses III. "
            "However, since the chiefs supported the authorities the workers no longer trusted them and chose their own representatives. "
            "Further complaints by the artisans are recorded forty and fifty years after the initial dispute, during the reigns of Ramesses IX and Ramesses X.",
            nome="Deir el-Medina")],
    },
    # 6 a múmia de Ramsés II em Paris
    {
        "temas_secundarios": ["historia_medicina", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "mito_desmentido"],
        "gancho": "Em 1976, a múmia de Ramsés II voou a Paris para tratamento e foi recebida no aeroporto com honras militares de rei. A história de que ganhou passaporte é mito, mas a viagem foi real.",
        "explicacao": (
            "Em 1975, o médico francês Maurice Bucaille examinou a múmia no Museu do Cairo e a achou em mau estado. "
            "O presidente Valéry Giscard d'Estaing convenceu as autoridades egípcias a mandá-la à França para "
            "tratamento. Em setembro de 1976, ela chegou ao aeroporto de Le Bourget, onde foi recebida com honras "
            "militares completas, próprias de um rei, e seguiu para um laboratório do Musée de l'Homme. A versão "
            "popular de que o faraó recebeu um passaporte para a viagem é falsa; ela talvez venha do uso da palavra "
            "francesa \"passeport\" para a extensa papelada exigida. Em Paris, a múmia passou por exames forenses, e "
            "a análise microscópica das raízes dos cabelos mostrou que eles eram originalmente ruivos, e não "
            "tingidos pela mumificação, como se supunha. Isso tinha peso simbólico: no Egito antigo, os ruivos eram "
            "associados ao deus Set, e o pai de Ramsés, Seti I, tinha um nome que significa \"seguidor de Set\". Para "
            "eliminar fungos e insetos, a múmia foi irradiada e voltou ao Egito em maio de 1977."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Ramesses_II",
            "In 1975, Maurice Bucaille, a French doctor, examined the mummy at the Cairo Museum and found it in poor condition. "
            "French President Valéry Giscard d'Estaing succeeded in convincing Egyptian authorities to send the mummy to France for treatment. "
            "In September 1976, it was greeted at Paris–Le Bourget Airport with full military honours befitting a king, then taken to a laboratory at the Musée de l'Homme. "
            "Persistent claims that the mummy was issued with a passport for the journey are incorrect, but may be based on the French word passeport being used to describe the extensive documentation required. "
            "The mummy was forensically tested in 1976 [...] "
            "Subsequent microscopic inspection of the roots of Ramesses II's hair proved that the king's hair originally was red. "
            "Unlike Maspero, who had assumed the hair had been dyed by the mummification process, Bucaille confirmed that the red hair was natural [...] "
            "in ancient Egypt people with red hair were associated with the deity Set [...] "
            "the name of Ramesses II's father, Seti I, means \"follower of Set\" [...] "
            "After being irradiated in an attempt to eliminate fungi and insects, the mummy was returned from Paris to Egypt in May 1977.",
            nome="Ramesses II")],
    },
    # 7 as pirâmides não foram feitas por escravos
    {
        "temas_secundarios": ["grandes_obras", "economia_curiosa"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "As pirâmides de Gizé não foram erguidas por escravos. Ao lado delas, arqueólogos acharam a vila dos operários, com padarias, cervejarias e até um hospital, e os túmulos onde eles foram enterrados com honras.",
        "explicacao": (
            "A ideia de multidões escravizadas começou com o historiador grego Heródoto, que visitou Gizé por volta "
            "de 450 a.C. e ouviu de sacerdotes que a Grande Pirâmide tinha exigido 400 mil homens ao longo de 20 "
            "anos, em turnos de 100 mil. Representações na cultura pop espalharam a imagem. A arqueologia conta outra "
            "história. Fora do muro que cerca o conjunto, a equipe de Mark Lehner achou a cidade onde os "
            "trabalhadores moravam: alojamentos coletivos, padarias, cervejarias, cozinhas, uma oficina de cobre e "
            "um hospital. Pão, carne de boi e peixe eram a base da dieta. No cemitério, alguns esqueletos mostram "
            "traumas típicos de acidentes de obra. Em 1990 foram achados túmulos dos próprios construtores, junto às "
            "pirâmides. Eles não foram mumificados, mas receberam túmulos de tijolo de barro com cerveja e pão para "
            "a vida após a morte. A proximidade das pirâmides e o cuidado no enterro reforçam que eram trabalhadores "
            "pagos, orgulhosos da obra. A maioria parece ter vindo de famílias pobres, e especialistas como "
            "arquitetos, pedreiros e carpinteiros trabalhavam de forma permanente para o rei."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Giza_pyramid_complex",
            "When Greek historian Herodotus visited Giza in 450 BC, he was told by Egyptian priests that \"the Great Pyramid had taken 400,000 men 20 years to build, working in three-month shifts 100,000 men at a time.\" [...] "
            "The Giza pyramid complex is surrounded by a large stone wall, outside which Mark Lehner and his team discovered a town where the pyramid workers were housed. [...] "
            "Among the discoveries at the workers' village are communal sleeping quarters, bakeries, breweries, and kitchens (with evidence showing that bread, beef, and fish were dietary staples), a copper workshop, a hospital, and a cemetery (where some of the skeletons were found with signs of trauma associated with accidents on a building site). [...] "
            "This archaeological evidence directly opposes previous beliefs that the pyramids were the result of intensive slave labor. "
            "This misconception began with Greek Historian Herodotus, and was later popularized in pop cultural depictions of the building of the pyramids. [...] "
            "In 1990, tombs belonging to the pyramid workers were discovered alongside the pyramids, with an additional burial site found nearby in 2009. "
            "Although not mummified, they had been buried in mudbrick tombs with beer and bread to support them in the afterlife. "
            "The tombs' proximity to the pyramids and the manner of burial supports the theory that they were paid laborers who took pride in their work and were not slaves, as was previously thought. [...] "
            "Most of the workers appear to have come from poor families. "
            "Specialists such as architects, masons, metalworkers, and carpenters were permanently employed by the king to fill positions that required the most skill.",
            nome="Giza pyramid complex")],
    },
    # 8 azul egípcio: o primeiro pigmento sintético brilha no infravermelho
    {
        "temas_secundarios": ["pigmentos", "luz_cores", "quimica_cotidiano"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "O azul egípcio, tido como o primeiro pigmento sintético, emite um brilho forte no infravermelho. Com isso, cientistas acham traços dele em peças que a olho nu parecem sem pintura alguma.",
        "explicacao": (
            "Os egípcios valorizavam muito o azul e queriam imitar pedras raras como a turquesa e o lápis-lazúli. "
            "Minerais azuis naturais eram escassos e difíceis de trabalhar, então eles passaram a fabricar o próprio "
            "pigmento: um silicato de cálcio e cobre feito aquecendo areia de quartzo, um composto de cobre, "
            "carbonato de cálcio e um pouco de álcali a temperaturas entre 800 e 1.000 °C por várias horas. O indício "
            "de uso mais antigo é uma tigela de cerca de 3250 a.C. A cor atravessou milênios e foi o azul por "
            "excelência da Roma antiga, até que, no século IV d.C., o segredo da fabricação se perdeu. Nenhum texto "
            "egípcio conhecido explica a receita; ela só aparece com o romano Vitrúvio, no século I a.C., e o "
            "interesse moderno começou com Humphry Davy, em 1815. A surpresa veio da física: sob luz visível, o "
            "pigmento emite uma luminescência intensa e duradoura no infravermelho próximo. Isso permite detectá-lo "
            "em objetos que parecem sem pintura e até em quadros do século XVI, muito depois de seu uso ser dado como "
            "extinto. A mesma propriedade fez pesquisadores pensarem em usos modernos, como imagens biomédicas e "
            "tintas de segurança."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Egyptian_blue",
            "is a pigment with the chemical formula CaCuSi4O10 that was used in ancient Egypt for thousands of years. "
            "It is considered to be the first synthetic pigment. [...] "
            "They also desired to imitate the semiprecious stones turquoise and lapis lazuli, which were valued for their rarity and stark blue color. "
            "Use of naturally occurring minerals such as azurite to acquire this blue was impractical, as these minerals were rare and difficult to work. [...] "
            "is on an alabaster bowl dated to the late pre-dynastic period or Naqada III (circa 3250 BC) [...] "
            "only dying out in the fourth century AD, when the secret to its manufacture was lost. "
            "No written information exists in ancient Egyptian texts about the manufacture of Egyptian blue in antiquity, and it was first mentioned only in Roman literature by Vitruvius during the first century BC. [...] "
            "investigated by Humphry Davy in 1815 [...] "
            "produced by heating together quartz sand, a copper compound, calcium carbonate, and a small amount of an alkali (ash from salt-tolerant, halophyte plants or natron) at temperatures ranging between 800 and 1,000 °C [...] "
            "Due to its almost exclusive use, Egyptian blue is the blue pigment par excellence of Roman antiquity [...] "
            "Egyptian blue's extremely powerful and long-lived infrared luminescence under visible light has enabled its presence to be detected on objects which appear unpainted to the human eye. "
            "This property has also been used to identify traces of the pigment on paintings produced as late as the sixteenth century, long after its use was presumed to have died out. [...] "
            "also indicates it may have several high-technology applications, such as in biomedicine (e.g. bioimaging), telecommunications, laser technology, and security inks.",
            nome="Egyptian blue")],
    },
    # 9 a "maldição" de Tutancâmon
    {
        "temas_secundarios": ["vieses_cognitivos", "doencas_infecciosas"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Não havia maldição escrita no túmulo de Tutancâmon. Das 58 pessoas presentes na abertura do túmulo e do sarcófago, só oito morreram nos doze anos seguintes, e Howard Carter viveu até 1939.",
        "explicacao": (
            "A lenda decolou com a morte de Lord Carnarvon, que financiou a escavação aberta em 1922. Ele foi picado "
            "por um mosquito, cortou a picada sem querer ao se barbear, e a ferida infeccionou. A revista médica "
            "The Lancet, revendo documentos, concluiu que a causa foi uma pneumonia sobre uma erisipela, uma "
            "infecção estreptocócica da pele, num homem propenso a infecções pulmonares graves. Duas semanas antes "
            "da morte dele, a romancista Marie Corelli tinha publicado uma carta citando um livro obscuro que prometia \"castigo "
            "terrível\" a quem invadisse um túmulo selado, e a imprensa passou a dizer que uma maldição fora achada "
            "no túmulo, o que era falso. Arthur Conan Doyle, criador de Sherlock Holmes, sugeriu que \"elementais\" "
            "criados pelos sacerdotes guardavam o rei. Os números contam outra história. Um estudo mostrou que das "
            "58 pessoas presentes quando o túmulo e o sarcófago foram abertos, só oito morreram em doze anos. Carter, "
            "que chamava as maldições de bobagem, morreu de linfoma em 1939, aos 64 anos. Lady Evelyn Herbert, filha "
            "de Carnarvon e uma das primeiras a entrar, viveu mais 57 anos."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Curse_of_the_pharaohs",
            "Despite popular misconceptions, no curse was found inscribed in the Pharaoh's tomb. [...] "
            "Carter's team opened the tomb of Tutankhamun (KV62) in 1922, launching the modern era of Egyptology. [...] "
            "The first of the deaths was that of Lord Carnarvon, who financed the excavation. "
            "He had been bitten by a mosquito, and later slashed the bite accidentally while shaving. "
            "It became infected and that resulted in blood poisoning. "
            "Two weeks before Carnarvon died, Marie Corelli wrote an imaginative letter that was published in the New York World magazine, in which she quoted an obscure book that confidently asserted that \"dire punishment\" would follow any intrusion into a sealed tomb. "
            "A media frenzy followed, with reports that a curse had been found in the King's tomb, though this was untrue. [...] "
            "Sir Arthur Conan Doyle, creator of Sherlock Holmes and spiritualist, suggested that Lord Carnarvon's death had been caused by \"elementals\" created by Tutankhamun's priests to guard the royal tomb [...] "
            "A study of documents and scholarly sources led The Lancet to conclude [...] "
            "The cause of Carnarvon's death was reported as \"'pneumonia supervening on [facial] erysipelas,' (a streptococcal infection of the skin and underlying soft tissue). [...] "
            "The Earl had been \"prone to frequent and severe lung infections\" [...] "
            "Howard Carter was entirely sceptical of such curses, dismissing them as 'tommy-rot' [...] "
            "A study showed that of the 58 people who were present when the tomb and sarcophagus were opened, only eight died within a dozen years. "
            "All the others were still alive, including Howard Carter, who died of lymphoma in 1939 at the age of 64. "
            "The last survivors included Lady Evelyn Herbert, Lord Carnarvon's daughter, who was among the first people to enter the tomb after its discovery in November 1922, who lived for a further 57 years and died in 1980",
            nome="Curse of the pharaohs")],
    },
    # 10 papiro Edwin Smith: cirurgia sem magia e a primeira descrição do cérebro
    {
        "temas_secundarios": ["historia_medicina", "anatomia", "neurociencia"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "Um manual egípcio de cirurgia de cerca de 1600 a.C. descreve 48 casos de ferimentos sem recorrer à magia e traz a primeira descrição conhecida da superfície do cérebro e do líquido que o envolve.",
        "explicacao": (
            "É o papiro Edwin Smith, nome do americano que o comprou em Luxor em 1862. É o tratado cirúrgico mais "
            "antigo que se conhece sobre traumas, um rolo de 4,68 metros escrito em hierático, com tinta preta e "
            "comentários em vermelho. A cópia é de cerca de 1600 a.C., mas a gramática e os termos arcaicos sugerem "
            "um original bem mais antigo. Os 48 casos vão da cabeça para baixo, como numa anatomia moderna, e cada "
            "um segue um roteiro: tipo de lesão, exame do paciente (olhar, cheirar, apalpar, tomar o pulso), "
            "diagnóstico, prognóstico e tratamento. O médico escolhia entre três veredictos: \"um mal que vou "
            "tratar\", \"um mal com que vou lutar\" e \"um mal que não deve ser tratado\". Entre os tratamentos há "
            "suturas, talas, mel para prevenir e curar infecções e carne crua para estancar sangramentos. O texto "
            "registra que a posição de uma lesão no crânio se relaciona com o lado do corpo afetado e que "
            "esmagamentos de vértebras prejudicam movimento e sensibilidade. Por isso se pensa que era um manual para "
            "feridas de guerra. Ao contrário de outros papiros médicos egípcios, só recorre a feitiços no verso e em "
            "dois casos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Edwin_Smith_Papyrus",
            "The Edwin Smith Papyrus is an ancient Egyptian medical text, named after Edwin Smith who bought it in 1862, and the oldest known surgical treatise on trauma. "
            "This document, which may have been a manual of military surgery, describes 48 cases of injuries, fractures, wounds, dislocations and tumors. "
            "It is unique among the surviving Egyptian medical papyri because it presents a rational and scientific approach to medicine in ancient Egypt and avoids prescribing magic. "
            "This copy dates to Dynasties 16–17 of the Second Intermediate Period in ancient Egypt, c. 1600 BCE but the original may date from the Old Kingdom. [...] "
            "The papyrus is a scroll 4.68 meters or 15.3 feet in length. [...] "
            "It is written right-to-left in hieratic, the Egyptian cursive form of hieroglyphs, in black ink with explanatory glosses in red ink. [...] "
            "The verso side consists of eight magic spells and five prescriptions. "
            "The spells of the verso side and two incidents in Case 8 and Case 9 are the exceptions to the practical nature of this medical text. [...] "
            "evidenced by archaic grammar, terminology, form and commentary. [...] "
            "The papyrus begins by addressing injuries to the head, and continues with treatments for injuries to neck, arms and torso, detailing injuries in descending anatomical order like a modern anatomical exposition. [...] "
            "The objective examination process included visual and olfactory clues, palpation and taking of the pulse. "
            "Following the examination are the diagnosis and prognosis, where the physician judges the patient’s chances of survival and makes one of three diagnoses: \"An ailment which I will treat,\" \"An ailment with which I will contend,\" or \"An ailment not to be treated\". [...] "
            "Among the treatments are closing wounds with sutures (for wounds of the lip, throat, and shoulder), bandaging, splints, poultices, preventing and curing infection with honey, and stopping bleeding with raw meat. [...] "
            "It contains the first known descriptions of the cranial structures, the meninges, the external surface of the brain, the cerebrospinal fluid, and the intracranial pulsations. [...] "
            "The relationship between the location of a cranial injury and the side of the body affected is also recorded, while crushing injuries of vertebrae were noted to impair motor and sensory functions. "
            "Due to its practical nature and the types of trauma investigated, it is believed that the papyrus served as a textbook for the trauma that resulted from military battles. [...] "
            "Edwin Smith, an American Egyptologist, purchased it in Luxor, Egypt in 1862",
            nome="Edwin Smith Papyrus")],
    },
    # 11 as 12 horas da noite vieram de um relógio de estrelas
    {
        "temas_secundarios": ["historia_astronomia", "calendarios", "medidas_padroes"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "A divisão da noite em 12 horas vem do Egito, onde ela era medida pelas estrelas: diagramas pintados em tampas de caixões acompanham o nascer de 36 estrelas ou constelações, os \"decanos\".",
        "explicacao": (
            "Os egípcios já dividiam a noite em intervalos antes dos Textos das Pirâmides, do século XXIV a.C. "
            "Por volta de 2150 a.C., tampas de caixões traziam diagramas de estrelas, chamados de \"relógios "
            "estelares\", que mostram exatamente 12 dessas divisões. O calendário civil egípcio tinha \"semanas\" de "
            "dez dias, e para cada uma havia um decano, uma estrela ou constelação cujo nascer antes do Sol era "
            "observado. A cada noite, o nascer de onze decanos marcava a passagem do tempo e dividia a escuridão em "
            "12 partes; as do meio duravam uns 40 minutos. Eram horas sazonais, mais longas no verão do que no "
            "inverno. Depois, o dia claro também foi dividido, e essas subdivisões passaram para a Grécia e, mais "
            "tarde, para Roma. Com os séculos, as estrelas saíam do lugar previsto, e na época de Amenófis III, "
            "por volta de 1350 a.C., os sacerdotes de Karnak já usavam relógios de água. As horas eram sagradas: "
            "cada uma era vista como uma região do céu ou do mundo dos mortos atravessada pela barca do deus-sol "
            "Rá, e a palavra para astrônomo, usada como sinônimo de sacerdote, significava \"um das horas\"."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Hour",
                "The ancient Egyptians began dividing the night into wnwt at some time before the compilation of the Dynasty V Pyramid Texts in the 24th century BC. "
                "By 2150 BC (Dynasty IX), diagrams of stars inside Egyptian coffin lids—variously known as \"diagonal calendars\" or \"star clocks\"—attest that there were exactly 12 of these. [...] "
                "The coffin diagrams show that the Egyptians took note of the heliacal risings of 36 stars or constellations (now known as \"decans\"), one for each of the ten-day \"weeks\" of their civil calendar. [...] "
                "Each night, the rising of eleven of these decans were noted, separating the night into 12 divisions whose middle terms would have lasted about 40 minutes each. [...] "
                "The original decans used by the Egyptians would have fallen noticeably out of their proper places over a span of several centuries. "
                "By the time of Amenhotep III (c. 1350 BC), the priests at Karnak were using water clocks to determine the hours. [...] "
                "By the New Kingdom, each hour was conceived as a specific region of the sky or underworld through which Ra's solar barge travelled. [...] "
                "The Egyptian word for astronomer, used as a synonym for priest, was wnwty, \"one of the wnwt\", as it were \"one of the hours\". [...] "
                "the Egyptians divided the night into 12 equal intervals. "
                "These were seasonal hours, longer in the summer than in the winter. "
                "Subsequently, the day was divided into intervals as well, which eventually became more important than the nightly intervals. "
                "These subdivisions of a day spread to Greece, and later to Rome.",
                nome="Hour"),
        ],
    },
    # 12 hieróglifos: 14 séculos achando que eram só símbolos
    {
        "temas_secundarios": ["decifracao", "sistemas_escrita"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "A última inscrição em hieróglifos é de 394 d.C. Depois a leitura se perdeu, e por séculos os estudiosos falharam por achar que cada sinal era uma ideia simbólica. Na verdade, muitos representam sons.",
        "explicacao": (
            "No século IV, poucos egípcios ainda liam hieróglifos. Em 391, o imperador romano Teodósio I fechou os "
            "templos não cristãos, e o uso monumental da escrita acabou; a última inscrição conhecida, em Filas, é "
            "de 394. Na Idade Média, o conhecimento se perdeu por completo. As tentativas de decifração, de autores "
            "árabes dos séculos IX e X a europeus do início da era moderna, esbarravam num pressuposto: o de que os "
            "hieróglifos registravam ideias, e não os sons da língua. Sem textos bilíngues, qualquer \"tradução\" "
            "simbólica podia ser proposta sem jamais ser testada. Só em meados do século XVII Athanasius Kircher "
            "considerou que os sinais também pudessem representar sons, mas a crença no caráter místico deles o "
            "atrapalhou. A virada veio com a Pedra de Roseta, achada em 1799, que traz o mesmo texto em hieróglifos, "
            "em demótico e em grego. Em 1822, Champollion descreveu um sistema ao mesmo tempo figurativo, simbólico "
            "e fonético, às vezes na mesma palavra. Hoje se sabe que a maioria dos sinais que não são "
            "determinativos funciona pelo som, como num rébus, e que alguns representam uma única consoante, como "
            "um alfabeto."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Egyptian_hieroglyphs",
            "phonetic glyphs, including single-consonant characters that function like an alphabet [...] "
            "By the 4th century AD, few Egyptians were capable of reading hieroglyphs, and the \"myth of allegorical hieroglyphs\" was ascendant. "
            "Monumental use of hieroglyphs ceased after the closing of all non-Christian temples in 391 by the Roman Emperor Theodosius I; the last known inscription is from Philae, known as the Graffito of Esmet-Akhom, from 394. [...] "
            "Knowledge of the hieroglyphs had been lost completely in the medieval period. "
            "Early attempts at decipherment were made by some such as Dhul-Nun al-Misri and pseudo-Ibn Wahshiyya (9th and 10th century, respectively). "
            "All medieval and early modern attempts were hampered by the fundamental assumption that hieroglyphs recorded ideas and not the sounds of the language. "
            "As no bilingual texts were available, any such symbolic 'translation' could be proposed without the possibility of verification. "
            "It was not until Athanasius Kircher in the mid 17th century that scholars began to think the hieroglyphs might also represent sounds. "
            "Kircher was familiar with Coptic, and thought that it might be the key to deciphering the hieroglyphs, but was held back by a belief in the mystical nature of the symbols. "
            "The breakthrough in decipherment came only with the discovery of the Rosetta Stone by Napoleon's troops in 1799 [...] "
            "As the stone presented a hieroglyphic and a demotic version of the same text in parallel with a Greek translation [...] "
            "In his Lettre à M. Dacier (1822), he wrote: [...] "
            "It is a complex system, writing figurative, symbolic, and phonetic all at once, in the same text, the same phrase, I would almost say in the same word. [...] "
            "Most non-determinative hieroglyphic signs are phonograms, whose meaning is determined by pronunciation, independent of visual characteristics. "
            "This follows the rebus principle",
            nome="Egyptian hieroglyphs")],
    },
    # 13 cartas de Amarna: faraós em cuneiforme e um rei reclamando de ouro falso
    {
        "temas_secundarios": ["sistemas_escrita", "primeiras_civilizacoes", "linguas_mundo"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "A correspondência diplomática dos faraós com reis vizinhos, no século XIV a.C., não era em egípcio: era quase toda em acadiano, em escrita cuneiforme mesopotâmica. Numa carta, um rei reclama de estátuas de ouro \"falsas\".",
        "explicacao": (
            "São as cartas de Amarna, um arquivo de tábuas de argila achado na antiga capital do faraó Akhenaton. "
            "Por volta de 1887, moradores da região desenterraram a maior parte em segredo e as venderam no mercado "
            "de antiguidades; hoje estão espalhadas por museus da Alemanha, do Reino Unido, do Egito, da França e de outros países. "
            "São 382 tábuas e fragmentos conhecidos, 350 deles cartas, que cobrem no máximo 30 anos. Elas foram "
            "escritas em cuneiforme, quase todas numa variedade do acadiano, a língua regional da diplomacia na "
            "época, e mostram as relações do Egito com Babilônia, Assíria, Chipre, os hititas e o reino de Mitanni. "
            "O acadiano dos escribas de Canaã vem cheio de marcas da língua materna deles, um ancestral das línguas "
            "que dariam origem ao hebraico e ao fenício, e por isso as cartas também são uma janela para essas "
            "línguas séculos antes de seus primeiros registros. Há episódios bem humanos. Tushratta, rei de Mitanni, "
            "reclama em várias cartas que Akhenaton lhe mandou estátuas de madeira folheadas a ouro, e não de ouro "
            "maciço, como o pai dele havia prometido no acerto do casamento da filha de Tushratta."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Amarna_letters",
            "are an archive, written on clay tablets, primarily consisting of diplomatic correspondence between the Egyptian administration and its representatives in Canaan and Amurru, or neighboring kingdom leaders, during the New Kingdom, spanning a period of no more than 30 years in the middle of the 14th century BC. "
            "The letters were found in Upper Egypt at el-Amarna, the modern name for the ancient Egyptian capital of Akhetaten, founded by pharaoh Akhenaten [...] "
            "The Amarna letters are unusual in Egyptological research, because they are written not in the language of ancient Egypt, but in cuneiform, the writing system of ancient Mesopotamia. "
            "Most are in a variety of Akkadian [...] "
            "The known tablets total 382 and fragments (350 are letters [...] "
            "Though most are written in Akkadian, the Akkadian of the letters is heavily colored by the mother tongue of their writers, who probably spoke an early form of Proto-Canaanite, the language(s) which would later evolve into the mother languages of Hebrew and Phoenician. "
            "These \"Canaanisms\" provide valuable insights into the proto-stage of those languages several centuries prior to their first actual manifestation. [...] "
            "The letters, comprising cuneiform tablets written primarily in Akkadian—the regional language of diplomacy for this period—were first discovered around 1887 by local Egyptians who secretly dug most of them from the ruined city of Amarna, and sold them in the antiquities market. [...] "
            "The initial group of letters recovered by local Egyptians have been scattered among museums in Germany, the United Kingdom, Egypt, France, Russia, and the United States [...] "
            "These tablets shed much light on Egyptian relations with Babylonia, Assyria, Syria, Canaan, and Alashiya (Cyprus) as well as relations with the Mitanni, and the Hittites. [...] "
            "Tushratta complains in numerous letters that Akhenaten had sent him gold-plated statues rather than statues made of solid gold; the statues formed part of the bride-price that Tushratta received for letting his daughter Tadukhepa marry Amenhotep III and then later marry Akhenaten. [...] "
            "But my brother [i.e., Akhenaten] has not sent the solid [gold] statues that your father was going to send. You have sent plated ones of wood.",
            nome="Amarna letters")],
    },
]
