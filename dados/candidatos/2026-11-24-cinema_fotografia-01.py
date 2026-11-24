LOTE = "2026-11-24-cinema_fotografia-01"
AREA = "artes"
TEMA = "cinema_fotografia"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 a foto mais antiga: oito horas ou vários dias?
    {
        "temas_secundarios": ["luz_cores"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "A foto mais antiga que sobreviveu, feita por Niépce em 1827, costuma ser descrita como fruto de oito horas de exposição. O museu que a guarda fala em vários dias. E ela ficou sumida por 47 anos.",
        "explicacao": (
            "Nicéphore Niépce fez a imagem entre junho e julho de 1827, na sua propriedade de Le Gras, no interior "
            "da França: são telhados e o campo vistos de uma janela alta. Ele usou uma câmara escura para projetar "
            "a cena sobre uma placa de estanho com chumbo, coberta por uma camada fina de betume da Judeia, um "
            "asfalto natural. Onde batia mais luz, o betume endurecia; nas partes escuras, continuava solúvel e "
            "era removido com uma mistura que levava óleo de lavanda. A conta tradicional de oito horas vem de um "
            "detalhe da imagem: o sol ilumina os prédios dos dois lados, como se tivesse passado de um lado para "
            "o outro. Mas um pesquisador moderno que estudou as anotações de Niépce e refez o processo concluiu "
            "que a exposição deve ter durado vários dias, e o Harry Ransom Center, da Universidade do Texas, onde "
            "a placa está, também descreve vários dias ao sol. Depois de uma última exibição pública em 1905, a "
            "imagem caiu no esquecimento por 47 anos, até que os historiadores Helmut e Alison Gernsheim a "
            "localizaram em 1952. Hoje ela fica numa vitrine sem oxigênio, monitorada o tempo todo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("View_from_the_Window_at_Le_Gras",
                "is the oldest surviving photograph. It was created by French inventor Nicéphore Niépce between June 4 and July 18, 1827, in Saint-Loup-de-Varennes, France, and shows parts of the buildings and surrounding countryside of his estate, Le Gras, as seen from a high window. [...] "
                "Niépce captured the scene with a camera obscura projected onto a [...] "
                "pewter plate thinly coated with bitumen of Judea, a naturally occurring asphalt. The bitumen hardened in the brightly lit areas, but in the dimly lit areas it remained soluble and could be washed away with a mixture of lavender oil and white petroleum. [...] "
                "Sunlight strikes the buildings on opposite sides, suggesting an exposure that lasted about eight hours, which has become the traditional estimate; however, a modern researcher who studied Niépce's notes and recreated his processes found that the exposure must have continued for several days. [...] "
                "View from the Window at Le Gras was last publicly shown in 1905 and then fell into obscurity for 47 years. [...] "
                "Historians Helmut Gernsheim and his wife, Alison Gernsheim, tracked down the photograph in 1952 [...] "
                "the metal plate is pewter (tin alloyed with lead [...] "
                "in a continuously monitored, stabilized, oxygen-free environment.",
                nome="View from the Window at Le Gras"),
            {"url": "https://www.hrc.utexas.edu/niepce-heliograph/", "titulo": "The Niépce Heliograph (Harry Ransom Center, Universidade do Texas)", "idioma": "en",
             "trecho": "He inserted the plate into a camera obscura and positioned it near a window in his second-story workroom. After several days of exposure to sunlight, the plate yielded an impression of the courtyard, outbuildings, and trees outside."},
        ],
    },
    # 2 a primeira pessoa fotografada: o homem que engraxava as botas
    {
        "temas_secundarios": ["percepcao_ilusoes"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "A foto mais antiga que se conhece com uma pessoa, de cerca de 1838, mostra uma avenida movimentada de Paris aparentemente vazia. Só um homem que engraxava as botas ficou parado o bastante para aparecer.",
        "explicacao": (
            "Louis Daguerre fez a imagem do Boulevard du Temple da janela do seu estúdio, às oito da manhã, num "
            "dia entre 24 de abril e 4 de maio de 1837 ou 1838. A rua devia estar cheia de gente e de cavalos, mas "
            "a exposição levava de quatro a cinco minutos, e tudo o que se movia sumiu. Ficaram duas figuras quase "
            "imóveis numa esquina: um homem com as botas sendo engraxadas e, ao que tudo indica, o engraxate, "
            "embora haja quem especule que a segunda figura seja uma bomba d'água. Quando a placa foi exposta em "
            "Munique, uma revista de Leipzig já comentava o homem que devia estar extremamente quieto. É, segundo "
            "a visão mais aceita, a foto mais antiga que sobreviveu com um ser humano, mas talvez não a primeira: "
            "Hippolyte Bayard disse ter feito autorretratos em 1837, que não sobreviveram. A placa original foi "
            "arruinada por uma restauração malsucedida depois de 1970, e as reproduções de hoje vêm de cópias do "
            "historiador Beaumont Newhall. Em 15 de outubro de 2026, uma placa comemorativa foi instalada na "
            "Place de la République, no ponto exato em que as duas pessoas estavam."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Boulevard_du_Temple_(photograph)",
                "is one of the earliest surviving daguerreotype plates produced by Louis Daguerre. Although the image seems to be of a deserted street, it is widely considered to be the earliest surviving photograph to include an image of a human. [...] "
                "The photograph was taken at 8:00 AM between 24 April and 4 May, either in 1837 or 1838, from a window in Daguerre's studio [...] "
                "The Boulevard du Temple would have been busy with people and horse traffic, but because an exposure time of four to five minutes would have been required, the only people recorded were two keeping still – a bootblack and his customer, at the corner of the street shown at lower left of the plate. It has been speculated, however, that this is not a bootblack, but a water pump. [...] "
                "The triptych was put on display at the Munich Arts Association where it immediately attracted attention, with the Leipzig Pfennig-Magazin saying of the 8:00 AM image that \"there appeared to be a man having his boots polished who must have been standing extremely still.\" [...] "
                "in 1936 or 1937, the American historian of photography Beaumont Newhall rediscovered them and made reproductions [...] "
                "in 1970, they were given out on loan to the Munich City Museum. Restoration was attempted, but ended in disaster, ruining the originals even further. Since then, daguerreotype facsimiles have been reproduced from Newhall's copies. [...] "
                "There may have been photographs of people before 1838. Hippolyte Bayard claimed to have taken photographic self-portraits in 1837, but these have not survived. [...] "
                "On 15 October 2026, a memorial plaque to the photograph and the two people coincidentally captured on it was unveiled on Place de la République. [...] "
                "is located at precisely the location the two people were at in 1838.",
                nome="Boulevard du Temple (photograph)"),
        ],
    },
    # 3 por que não se sorria nas fotos antigas
    {
        "temas_secundarios": ["costumes_rituais", "emocoes"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "Nas fotos antigas ninguém sorria só por causa do longo tempo de exposição? Nos anos 1850 já dava para fotografar em segundos. Pesava mais a etiqueta: sorriso largo lembrava bebedeira, loucura e vulgaridade.",
        "explicacao": (
            "A parte técnica é real: nos primeiros retratos em daguerreótipo, a exposição passava de 15 minutos, e "
            "apoios de pescoço e de cabeça seguravam o modelo no lugar. Um sorriso mantido por tanto tempo virava "
            "careta. Mas o tempo de exposição caiu depressa, e um curador do George Eastman Museum lembra que, já nos "
            "anos 1850, era possível, em boas condições, fazer fotos com poucos segundos. Mesmo assim, "
            "o sorriso só começou a virar a expressão padrão a partir dos anos 1920. O motivo principal era cultural: a "
            "fotografia de estúdio herdou as convenções do retrato pintado, em que mostrar os dentes num sorriso "
            "largo era associado à lascívia, à loucura, à bebedeira e às classes baixas. Em Londres, o fotógrafo "
            "Richard Beard pedia aos clientes que dissessem \"prunes\" (ameixas secas), para obter uma boca pequena "
            "e contida, vista como sinal de decoro. Os dentes ruins da época também entram na conta, embora haja "
            "historiadores que duvidem desse fator. A virada veio com a foto amadora: a partir da câmera Kodak de "
            "1888, a propaganda da empresa ligou a fotografia a momentos de lazer e felicidade, e o sorriso foi "
            "aos poucos tomando conta dos retratos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": "https://www.getty.edu/news/why-no-smile-photographs-history-education-question-answer/", "titulo": "Say Prunes! (Getty News)", "idioma": "en",
             "trecho": "The exposure time for early photographs was long: over 15 minutes in the earliest days of the portrait daguerreotype. Though this rapidly decreased to just over a minute as scientists fine-tuned the process, sitters had to remain still the entire time to avoid blur. Neck braces and head clamps, such as this one, were commonly used to hold sitters in place. A natural smile could easily turn into a grimace when held for so long. [...] "
                       "Much early studio photography in Europe and North America reflected the conventions of Western European portraiture [...] "
                       "Smiling widely and showing your teeth wasn't a good look for anyone who wanted to be considered a serious person. As scholars such as Angus Trumble and Nicholas Jeeves have detailed, a broad grin was associated with lewdness, lunacy, drunkenness, and the lower classes. [...] "
                       "In London, daguerreotypist Richard Beard instructed sitters to \"say prunes\" before their portrait was made, to achieve the perfect tart mouth—then considered the very image of decorum. [...] "
                       "With the advent of snapshot photography in 1888, Kodak marketed to the world a vision of photography as a joyous pursuit."},
            {"url": "https://time.com/4568032/smile-serious-old-photos/", "titulo": "Now You Know: Why Do People Always Look So Serious in Old Photos? (TIME)", "idioma": "en",
             "trecho": "it took until the 1920s and ’30s for smiles to start becoming the standard expression in photographs. [...] "
                       "Some dismiss the idea that bad teeth could have been a possible cause for early photography’s close-lipped images [...] "
                       "says Todd Gustavson, technology curator at the George Eastman Museum. [...] "
                       "But he says that technology has been overplayed as the limiting factor. By the 1850s and ’60s it was possible in the right conditions to take photographs with only a few seconds of exposure time"},
        ],
    },
    # 4 Muybridge e o cavalo no ar
    {
        "temas_secundarios": ["comportamento_animal", "percepcao_ilusoes"],
        "tipos_espanto": ["mito_desmentido", "engenhosidade"],
        "gancho": "Pintores retratavam o cavalo a galope com as patas esticadas para a frente e para trás, todas no ar. Em 1878, as fotos de Muybridge mostraram que as quatro saem do chão, sim, mas encolhidas sob o corpo.",
        "explicacao": (
            "Leland Stanford, industrial e ex-governador da Califórnia, criava cavalos de corrida e estava convencido "
            "de que as pinturas da época mostravam errado o animal correndo. Em 1873, contratou o fotógrafo "
            "Eadweard Muybridge, mas a primeira tentativa rendeu só uma imagem borrada. Em 15 de junho de 1878, "
            "numa pista de Palo Alto, Muybridge montou uma bateria de 12 câmeras diante de um fundo branco. Fios "
            "passavam sob a pista e, ao serem rompidos um a um pela roda da charrete puxada pelo cavalo, "
            "disparavam os obturadores em sequência, com exposições que, segundo se anunciou, duravam um milésimo "
            "de segundo. As fotos revelaram posições tão estranhas que muita gente achou ridículas, mas a "
            "quantidade de imagens publicadas e as animações em zootrópios venceram as dúvidas. Elas mostraram que "
            "os quatro cascos de fato ficam no ar, mas no momento em que as pernas estão recolhidas sob o corpo. "
            "Já a famosa aposta de US$ 25 mil que Stanford teria feito sobre o assunto nunca foi comprovada. "
            "Muybridge depois projetou versões pintadas das sequências com o seu zoopraxiscópio: é a mais antiga "
            "exibição conhecida de imagens em movimento feitas a partir de registros reais."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("The_Horse_in_Motion",
                "Muybridge's work was commissioned by Leland Stanford, the industrialist, former Governor of California, and horseman [...] "
                "Stanford was convinced that most depictions of running horses made by human artists were wrong. The great majority of oil paintings at the time portrayed the animal above the ground with its forelegs both extended forward at the same time as its rear legs were both extended to the rear [...] "
                "In 1873, Stanford approached Muybridge to photograph his favorite trotter Occident in action. [...] "
                "Nonetheless, the best result was a very blurry and shadowy image of the trotting horse. [...] "
                "Wires ran under the surface, from a battery of 12 cameras [...] "
                "On 15 June 1878, in the presence of invited turfmen and members of the press, Stanford's racehorse Abe Edgington was sent trotting [...] "
                "with the sulky wheel tripping all the wires one by one, breaking the electrical circuit and thus causing each camera shutter to open in turn, for a duration that was claimed to last the 1/1000 part of a second. [...] "
                "The photographs showed that all four feet are sometimes simultaneously off the ground and that when galloping this occurs when the feet are \"gathered\" beneath the body, not when the fore and hindlimbs are \"extended\" as sometimes depicted in older paintings. [...] "
                "Some of the registered positions were deemed ridiculous and seemed off to many people [...] "
                "would be smothered by the evidence in the large number of pictures that were published, by the praise of experts, by looking at animations of the sequences in zoetropes [...] "
                "The projection of moving painted versions of Muybridge's pictures with the zoopraxiscope was the earliest known motion picture exhibition based on actual recordings of motion.",
                nome="The Horse in Motion"),
            wiki("Eadweard_Muybridge",
                "There are stories that Stanford had made a $25,000 bet on his theories about horse locomotion, but no evidence has been found of such a wager.",
                nome="Eadweard Muybridge"),
        ],
    },
    # 5 o pânico do trem dos Lumière
    {
        "temas_secundarios": ["percepcao_ilusoes"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "A plateia que fugiu apavorada do trem dos irmãos Lumière provavelmente nunca existiu: não há relato da época de pânico. A história pode ter nascido de comédias que zombavam de caipiras no cinema.",
        "explicacao": (
            "O curta \"A chegada de um trem à estação de La Ciotat\", de uns 50 segundos, mostra uma locomotiva a "
            "vapor entrando numa estação do sul da França. Ao contrário do que se costuma dizer, ele nem fez parte "
            "da primeira sessão pública dos Lumière, em 28 de dezembro de 1895, em Paris: só foi exibido em "
            "janeiro de 1896, em Lyon. O historiador Martin Loiperdinger observa que não existem relatos da época "
            "sobre espectadores em pânico, o que, nas salas lotadas de então, provavelmente teria causado feridos "
            "e aparecido nos jornais locais. Houve, sim, quem se assustasse: o escritor Máximo Gorki descreveu a "
            "impressão de que a máquina ia mergulhar na escuridão da plateia. O pesquisador Stephen Bottomore "
            "juntou muitos relatos de sustos, mas nenhum caso confirmado de alguém que acreditasse que o trem era "
            "real. Já em 1901 havia comédias mostrando um homem do campo que foge da tela ao ver um trem chegando, "
            "e Loiperdinger sugere que essa piada às custas dos caipiras pode ter alimentado a crença. Outra "
            "hipótese é a confusão com uma versão em 3D que Louis Lumière refilmou e exibiu em 1934."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("L'Arrivée_d'un_train_en_gare_de_La_Ciotat",
                "Contrary to popular belief, it was not shown at the Lumières' first public film screening on 28 December 1895 in Paris, France: the programme of ten films shown that day makes no mention of it. Its first public showing took place in January 1896 in Lyon. [...] "
                "This 50-second silent film shows the entry of a train pulled by a steam locomotive into the Gare de La Ciotat, the train station of the French southern coastal town of La Ciotat [...] "
                "Martin Loiperdinger notes that there are no contemporary reports of audiences panicking at the sight, which likely would have caused injuries in the crowded exhibition rooms of the era and probably would have received coverage in local newspapers. [...] "
                "Russian journalist Maxim Gorky wrote: \"A train appears on the screen. It speeds right at you—watch out! It seems as though it will plunge into the darkness in which you sit [...] "
                "Bottomore collected many other anecdotes about audience reactions to L'Arrivée d'un Train and similar films, finding many firsthand accounts of spectators being startled or frightened by the images on the screen, but no confirmed instances of people actually believing that it was real. "
                "As early as 1901, filmmakers parodied the idea of past audiences being terrified by L'Arrivée d'un Train, making comedic motion pictures that showed a naive rural person attending a showing and then fleeing in terror at the sight of an approaching train on the screen [...] "
                "Loiperdinger suggests that this joke at the expense of \"country rubes\" may have provided the basis for the widespread belief that audiences really reacted that way. [...] "
                "Louis Lumière eventually re-shot L'Arrivée d'un Train with a stereoscopic film camera and exhibited it (along with a series of other 3D shorts) at a 1934 meeting of the French Academy of Science. Given the contradictory accounts that plague early cinema and pre-cinema accounts, it is plausible that early cinema historians conflated the audience reactions at these separate screenings",
                nome="L'Arrivée d'un train en gare de La Ciotat"),
        ],
    },
    # 6 Louis Le Prince, que filmou antes e sumiu
    {
        "temas_secundarios": ["personagens_esquecidos"],
        "tipos_espanto": ["misterio_aberto", "historia_humana"],
        "gancho": "Em 1888, Louis Le Prince filmou a família num jardim na Inglaterra: é tido como o filme mais antigo que sobreviveu. Dois anos depois, ia pegar um trem para Paris e sumiu. Nem a bagagem foi achada.",
        "explicacao": (
            "Le Prince, inventor francês radicado em Leeds, usou uma câmera de lente única e filme de papel da "
            "Eastman. Em 14 de outubro de 1888, filmou o filho Adolphe, os sogros e uma amiga caminhando no "
            "jardim da casa dos sogros; a sogra morreu dez dias depois. O trabalho dele parece anteceder o de "
            "outros pioneiros, como os irmãos Lumière e a equipe de Thomas Edison. Em setembro de 1890, ele se "
            "preparava para viajar aos Estados Unidos, supostamente para apresentar o invento, e antes foi a "
            "Dijon visitar o irmão. Em 16 de setembro, partiu para Paris de trem, mas os amigos que o esperavam "
            "descobriram que ele não estava a bordo. A polícia francesa, a Scotland Yard e a família procuraram "
            "sem sucesso, e as teorias vão de assassinato a suicídio, sem prova conclusiva. A viúva suspeitou de "
            "crime ligado à disputa de patentes com Edison. Em 1898, o filho Adolphe testemunhou num processo em "
            "que Edison dizia ser o único inventor do cinema; três anos depois, foi achado morto, tendo se matado "
            "com um tiro. Em 2003, surgiu nos arquivos da polícia de Paris a foto de um afogado de 1890 muito "
            "parecido com Le Prince, mas há quem diga que o corpo era baixo demais para ser o dele."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Louis_Le_Prince",
                "In October 1888, Le Prince filmed moving-picture sequences of family members in Leeds, in the 1888 short films Roundhay Garden Scene, and Accordion Player (showing his son Adolphe Le Prince playing the accordion), using his single-lens camera and Eastman's paper negative film. [...] "
                "His work appears to precede the inventions of his contemporaries, such as Friese-Greene and Donisthorpe as well as being years ahead of the Lumière brothers and Dickson (who did the moving image work for Thomas Edison). Le Prince disappeared on 16 September 1890. Numerous conspiracy theories emerged about his disappearance, including murder, disappearance in order to start a new life, and suicide. However, no conclusive evidence was found for any of these theories. [...] "
                "In September 1890, Le Prince was preparing for a trip to the United States, supposedly to publicly premiere his work and join his wife and children. Before this journey, he decided to return to France to visit his brother in Dijon. Then, on 16 September, he took a train to Paris, but having taken a later train than planned, his friends in Paris discovered that he was not on board. He was never seen again by his family or friends, nor was the luggage he was traveling with ever found. [...] "
                "The French police, Scotland Yard and the family undertook exhaustive searches, but never found him. [...] "
                "His widow assumed foul play though no concrete evidence has ever emerged [...] "
                "In 1898, Le Prince's elder son Adolphe, who had assisted his father in many of his experiments, was called as a witness for the American Mutoscope Company in their litigation with Edison [...] "
                "Three years later, 28-year-old Adolphe was found dead on Fire Island near New York, having died by suicide by shooting himself through his forehead. [...] "
                "A photograph of a drowned man pulled from the Seine in 1890, strongly resembling Le Prince, was discovered in 2003 during research in the Paris police archives. [...] "
                "However, it has been claimed that the body was too short to be Le Prince. [...] "
                "in which Edison claimed to be the first and sole inventor of cinematography",
                nome="Louis Le Prince"),
            wiki("Roundhay_Garden_Scene",
                "is a short silent motion picture filmed by French inventor Louis Le Prince at Oakwood Grange in Roundhay, Leeds, in Yorkshire, England on 14 October 1888. It is believed to be the oldest surviving film. [...] "
                "Oakwood Grange, the home of Joseph and Sarah Whitley [...] "
                "Joseph (1816–1891) and Sarah (née Robinson, 1816–1888) were the parents of Elizabeth, Louis Le Prince's wife, and Hartley is believed to have been a friend of the Le Princes. Sarah Whitley died ten days after the scene was filmed.",
                nome="Roundhay Garden Scene"),
        ],
    },
    # 7 os filmes enterrados sob o rinque de Dawson City
    {
        "temas_secundarios": ["agua_doce_gelo", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Em 1929, centenas de rolos de filmes mudos serviram de aterro para nivelar um rinque de hóquei no Yukon, no Canadá. O solo congelado os conservou, e em 1978 uma obra os trouxe de volta.",
        "explicacao": (
            "Dawson City, cidade da corrida do ouro do Klondike, exibia filmes desde 1903. Os rolos que não eram "
            "devolvidos ficavam guardados num banco local e depois no porão da biblioteca da cidade. A associação "
            "esportiva tinha transformado uma piscina num rinque de gelo, mas a conversão malfeita deixava o gelo "
            "com temperatura irregular no meio. Em 1929, Clifford Thomson, funcionário do banco e tesoureiro da "
            "associação de hóquei, resolveu os dois problemas de uma vez: empilhou na piscina 500 mil pés de "
            "filme, cobriu tudo com tábuas e nivelou com uma camada de terra. Os filmes de nitrato que continuaram "
            "chegando depois ajudaram a alimentar o incêndio que destruiu o complexo em 1951. Os enterrados, "
            "protegidos pelo permafrost, sobreviveram. Em 1978, a escavação para um novo centro de recreação "
            "revelou 533 rolos com 372 títulos, feitos entre 1903 e 1929, incluindo filmes dados como perdidos e "
            "imagens raras da World Series de beisebol de 1919. Para algumas produtoras, essas cópias são o último "
            "registro que restou. Por serem quimicamente instáveis, os rolos foram levados em transporte militar "
            "para os arquivos nacionais do Canadá e para a Biblioteca do Congresso dos EUA."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Dawson_Film_Find",
                "The Dawson Film Find (DFF) was the accidental discovery in 1978 of 372 film titles preserved in 533 reels of silent-era nitrate films in the Klondike Gold Rush town of Dawson City, Yukon, Canada. The reels had been buried under an abandoned hockey rink in 1929 and included lost films of feature movies and newsreels. [...] "
                "The 533 film reels date \"between 1903 and 1929 [...] "
                "rare footage of historic events, including the 1919 World Series. [...] "
                "Beginning in 1903, the Dawson Amateur Athletic Association (DAAA) began showing films in Dawson City, Yukon, Canada. The unreturned films were deposited in the local Canadian Bank of Commerce and later stored in the local Carnegie Library basement. The DAAA later converted a swimming pool to an ice rink, but because of improper conversion the ice rink suffered from uneven temperatures in the middle of the rink. In 1929, Clifford Thomson, then employed by the Canadian Bank of Commerce and also treasurer of the hockey association, solved the problem of the library's stock of film and the inadequate ice rink. Thomson took 500,000 feet of film and stacked the reels in the pool, covered the reels with boards and leveled the rink with a layer of earth. The DAAA continued to receive new nitrate films which would later fuel the destruction of the entire complex in a fire in 1951. The films stored under the ice rink were preserved by permafrost and were later uncovered in 1978 when a new recreation center was being built. "
                "The Dawson Film Find material was collected and preserved, with these prints becoming the last surviving records of some movie studios. Owing to its dangerous chemical volatility, the historical find was moved by military transport to Library and Archives Canada and the U.S. Library of Congress",
                nome="Dawson Film Find"),
        ],
    },
    # 8 o filme que queima debaixo d'água e o incêndio da Fox
    {
        "temas_secundarios": ["quimica_cotidiano", "elementos_quimicos"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "O filme de nitrato do cinema antigo queima até debaixo d'água: ele traz o próprio oxigênio. Em 1937, numa onda de calor, um depósito pegou fogo sozinho e destruiu a maior parte dos filmes mudos da Fox.",
        "explicacao": (
            "Por décadas, a película de cinema foi feita de nitrocelulose, o chamado filme de nitrato. Ao "
            "contrário da maioria dos materiais inflamáveis, ela não precisa de ar para continuar queimando, "
            "porque a própria molécula contém oxigênio suficiente para manter a chama. Um filme de treinamento "
            "para projecionistas mostrava um rolo aceso que seguia queimando mesmo totalmente submerso, e jogar "
            "água pode até aumentar a fumaça. Com o tempo, o nitrato se decompõe num processo que se acelera "
            "sozinho e solta gases. Em julho de 1937, em Little Ferry, Nova Jersey, uma onda de calor com "
            "máximas de 38 °C, somada aos gases do filme em decomposição e à ventilação ruim, causou combustão "
            "espontânea num depósito da 20th Century-Fox. Mais de 40 mil rolos de negativos e cópias viraram "
            "cinza dentro das latas, e um menino de 13 anos que morava perto morreu queimado. Mais de 75% dos "
            "longas da Fox anteriores a 1930 estão completamente perdidos. Incêndios, decomposição e o descarte "
            "deliberado de filmes velhos explicam por que a grande maioria dos filmes mudos se perdeu. No Reino "
            "Unido, até hoje é proibido mandar filme de nitrato pelo correio."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Nitrate_film",
                "A training film for projectionists included footage of a controlled ignition of a reel of nitrate film, which continued to burn even when fully submerged in water. Once burning, it is extremely difficult to extinguish. Unlike most other flammable materials, nitrocellulose does not need a source of air to continue burning, since it contains sufficient oxygen within its molecular structure to sustain a flame. For this reason, immersing burning film in water may not extinguish it, and could actually increase the amount of smoke produced. Owing to public safety precautions, the United Kingdom's Health and Safety Executive to this day forbids transportation of nitrate film by post or public transit [...] "
                "Many films produced during the early 20th century were lost through this accelerating, self-catalyzed disintegration or through studio warehouse fires, and many others were deliberately destroyed specifically to avoid the fire risk.",
                nome="Nitrocellulose (seção sobre filme de nitrato)"),
            wiki("1937_Fox_vault_fire",
                "The early motion-picture industry primarily used film stock made of nitrocellulose, commonly called nitrate film. [...] "
                "In Little Ferry, gasses produced by decaying film, combined with high temperatures and inadequate ventilation, resulted in spontaneous combustion. [...] "
                "Northern New Jersey experienced a heat wave in July 1937, with daytime temperatures of 100 °F (38 °C) and warm nights. [...] "
                "All three were seriously burned, and 13-year-old Charles died from his injuries on July 19. [...] "
                "with more than 40,000 reels of negatives and prints burned to ashes inside their film cans. [...] "
                "more than 75% of Fox's feature films from before 1930 are completely lost.",
                nome="1937 Fox vault fire"),
            wiki("Silent_film",
                "The vast majority of the silent films produced in the late 19th and early 20th centuries are considered lost.",
                nome="Silent film"),
        ],
    },
    # 9 o cartão Shirley e a pele clara como padrão
    {
        "temas_secundarios": ["luz_cores", "invencoes"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "Por décadas, laboratórios acertavam a cor das fotos comparando com o retrato de uma funcionária branca da Kodak, a \"Shirley\". O filme favorecia a pele clara, e Godard chegou a recusar o Kodak por isso.",
        "explicacao": (
            "Os cartões Shirley surgiram em meados dos anos 1950. Em 1954, o governo americano agiu para quebrar "
            "o monopólio da Kodak, que então revelava quase todo o filme colorido do país. A empresa criou uma "
            "impressora para laboratórios independentes e mandava junto um kit com fotos de referência, para que "
            "cada laboratório conferisse se as cores e a densidade batiam. A modelo das fotos era Shirley Page, "
            "funcionária da Kodak, e o nome pegou: qualquer modelo que viesse depois continuava sendo \"a "
            "Shirley\". No começo, todas eram brancas, muitas vezes com a palavra \"normal\" no cartão. Para a "
            "pesquisadora Lorna Roth, da Universidade Concordia, no Canadá, a faixa de tons que os filmes "
            "registravam, tanto de foto quanto de cinema, era enviesada a favor da pele branca. Havia queixas de "
            "que, numa mesma foto com pessoas negras e brancas, parte da imagem saía clara ou escura demais. Em "
            "1978, o cineasta Jean-Luc Godard se recusou a usar filme Kodak em Moçambique, declarando que ele era "
            "racista. Nos anos 1970, um fotógrafo da Kodak passou a usar muitos modelos negros nos testes, e a "
            "empresa acabou fazendo cartões multirraciais, como um de 1995 com três mulheres de tons de pele "
            "diferentes."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.npr.org/transcripts/363517842", "titulo": "How Kodak's Shirley Cards Set Photography's Skin-Tone Standard (NPR)", "idioma": "en",
             "trecho": "Shirley cards go back to the mid-1950s. At the time, Kodak sold almost all the color film used in the U.S. After a customer shot the film, they'd bring the roll to a Kodak store to be printed. In 1954, the federal government stepped in to break up Kodak's monopoly. [...] "
                       "Kodak came up with its S5 printer for independent photo labs. And to make sure the colors and densities of the prints were calibrated correctly, Kodak sent out a kit with color prints and original, unexposed negatives. [...] "
                       "Each reference card was an original shot of Shirley Page, who worked as a studio model for Kodak's new products. [...] "
                       "It was just known as the Shirley. And it didn't make any difference which model came in later to do it. It was still called the Shirley. [...] "
                       "In the early days, all of them were white and often tagged with the word normal. [...] "
                       "Lorna Roth is a media professor at Concordia University in Canada who has researched the history of Kodak's Shirley cards. [...] "
                       "Roth says the dynamic range of the film, both still photo stock and motion picture, was biased towards white skin. In 1978, the filmmaker Jean-Luc Godard famously refused to use Kodak film to shoot in Mozambique because he declared the film was racist. People also complain that photos of blacks and whites in the same shot would turn out partially under- or overexposed. [...] "
                       "In the 1970s, photographer Jim Lyon joined Kodak's first photo tech division and research laboratories. He says the company recognized there was a problem with the all-white Shirley cards. [...] "
                       "I started incorporating black models pretty heavily in our testing [...] "
                       "And Kodak started making multiracial norm-reference cards"},
            wiki("Shirley_card",
                "In 1995, Kodak designed a multiracial norm reference card. This card showed three women (Caucasian, Asian, African) with different skin colors and brightly contrasted clothing.",
                nome="Color chart (seção Shirley cards)"),
        ],
    },
    # 10 Méliès, a câmera emperrada e o precedente de Edison
    {
        "temas_secundarios": ["percepcao_ilusoes", "teatro_danca"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "Méliès contou que descobriu o truque de fazer coisas sumirem quando a câmera emperrou: na projeção, um ônibus virou carro funerário. Mas um filme da companhia de Edison já usava o truque antes.",
        "explicacao": (
            "Georges Méliès, mágico de palco que virou cineasta, contou a história num texto de 1907. O aparelho "
            "rudimentar que ele usava no início vivia rasgando ou travando o filme. Um dia, enquanto filmava a "
            "Place de l'Opéra, em Paris, precisou parar por um minuto para soltar a película. Nesse intervalo, "
            "pedestres, ônibus e carros mudaram de lugar. Quando projetou o filme, emendado no ponto da falha, "
            "viu um ônibus da linha Madeleine-Bastille se transformar num carro funerário, e homens virarem "
            "mulheres. Estava criado o truque de substituição: parar a filmagem, mudar algo na cena e retomar com "
            "o mesmo enquadramento. Dois dias depois, segundo ele, já fazia as primeiras metamorfoses e sumiços "
            "de propósito. O historiador Jacques Deslandes considera mais provável que Méliès tenha aprendido o "
            "efeito examinando uma cópia de \"A execução de Maria Stuart\", filme de 1895 da companhia de Edison "
            "em que uma versão primitiva do truque aparece na decapitação. De qualquer forma, foi o efeito mais "
            "importante da obra de Méliès. Estudos mostraram que boa parte da ilusão vinha do cuidado dele em "
            "casar os quadros na montagem, e a colorização à mão ajudava a disfarçar os cortes."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Stop_trick",
                "The pioneering French filmmaker Georges Méliès claimed to have accidentally developed the stop trick, as he wrote in Les Vues Cinématographiques in 1907 [...] "
                "An obstruction of the apparatus that I used in the beginning (a rudimentary apparatus in which the film would often tear or get stuck and refuse to advance) produced an unexpected effect, one day when I was prosaically filming the Place de L'Opéra; I had to stop for a minute to free the film and to get the machine going again. During this time passersby, omnibuses, cars, had all changed places, of course. When I later projected the film, reattached at the point of the rupture, I suddenly saw the Madeleine-Bastille bus changed into a hearse, and men changed into women. The trick-by-substitution, called the stop trick, had been invented and two days later I performed the first metamorphosis of men into women and the first sudden disappearances [...] "
                "According to the film scholar Jacques Deslandes, it is more likely that Méliès discovered the trick by carefully examining a print of the Edison Manufacturing Company's 1895 film The Execution of Mary Stuart, in which a primitive version of the trick appears. In any case, the substitution splice was both the first special effect Méliès perfected, and the most important in his body of work. "
                "Film historians such as Richard Abel and Elizabeth Ezra established that much of the effect was the result of Méliès's careful frame matching during the editing process [...] "
                "the addition of painted color acts as a sleight of hand technique allowing the cuts to pass by unnoticed.",
                nome="Substitution splice (stop trick)"),
            wiki("Georges_Méliès",
                "was a French filmmaker, actor, magician, and toymaker. [...] "
                "This same stop trick effect had already been used by Thomas Edison when depicting a decapitation in The Execution of Mary Stuart",
                nome="Georges Méliès"),
        ],
    },
    # 11 Méliès: pirateado, derretido em saltos de sapato, vendendo brinquedos
    {
        "temas_secundarios": ["primeira_guerra", "brinquedos"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Na Primeira Guerra, o Exército francês confiscou mais de quatrocentas cópias de filmes de Méliès e as derreteu para tirar prata e celuloide, que virou salto de sapato. Arruinado, ele foi vender doces numa estação.",
        "explicacao": (
            "Georges Méliès, pioneiro dos efeitos especiais, fez sucesso mundial com \"Viagem à Lua\", de 1902. "
            "Mas viu o filme ser copiado sem controle: uma cópia vendida para exibição só na Argélia foi parar "
            "nas mãos de um funcionário da empresa de Thomas Edison e foi duplicada. Em 1904, Edison e outras "
            "companhias americanas vendiam o filme, muitas vezes sem nenhum crédito a Méliès. Endividado, ele "
            "faliu e não fez mais filmes depois de 1912. Na guerra, o Exército transformou seu estúdio principal "
            "em hospital e confiscou mais de quatrocentas cópias originais da sua produtora, a Star Films, para derretê-las. "
            "Ele próprio chegou a destruir seus negativos. No fim de 1925, quando se casou com a atriz Jehanne "
            "d'Alcy, estava esquecido e arruinado, e o casal vivia de uma pequena barraca de doces e brinquedos "
            "no saguão da estação Gare Montparnasse. Jornalistas o redescobriram, e em 1931 ele recebeu a Legião "
            "de Honra das mãos de Louis Lumière. Dos mais de 500 filmes que fez, só cerca de 200 existem hoje. "
            "Uma cópia colorida à mão de \"Viagem à Lua\", dada como perdida, apareceu em 1993."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Georges_Méliès",
                "During the war, the French Army confiscated over four hundred of Star Films' original prints and melted them down to recover silver and celluloid, the latter of which the army used to make shoe heels. [...] "
                "Méliès was largely forgotten and financially ruined by December 1925, when he married his long-time mistress, the actress Jehanne d'Alcy. The couple scraped together a living by working at a small candy and toy stand d'Alcy owned in the main hall of the Gare Montparnasse. [...] "
                "Eventually Méliès was made a Chevalier de la Légion d'honneur, the medal of which was presented to him in October 1931 by Louis Lumière. [...] "
                "Méliès was bankrupt and unable to continue making films. [...] "
                "Although he never made another film after 1912 [...] "
                "In 1917, the French Army turned the main studio building at his Montreuil property into a hospital for wounded soldiers. [...] "
                "only roughly 200 out of over 500 Méliès's films remain in existence today. These factors include Méliès's destruction of his original negatives, the French army's confiscation of his prints",
                nome="Georges Méliès"),
            wiki("A_Trip_to_the_Moon",
                "is a 1902 French science-fiction adventure trick film written, directed and produced by Georges Méliès. [...] "
                "Méliès sold a print of the film to the Paris photographer Charles Gerschel for use in an Algiers theatre, under strict stipulation that the print only be shown in Algeria. Gerschel sold the print, and various other Méliès films, to the Edison Manufacturing Company employee Alfred C. Abadie, who sent them directly to Edison's laboratories to be duplicated and sold by Vitagraph. Copies of the print spread to other firms, and by 1904 Siegmund Lubin, the Selig Polyscope Company, and Edison were all redistributing it. [...] "
                "Méliès was often uncredited altogether [...] "
                "An original hand-coloured print was discovered in 1993",
                nome="A Trip to the Moon"),
        ],
    },
    # 12 Prokudin-Gorsky e a Rússia dos czares em cores
    {
        "temas_secundarios": ["luz_cores", "revolucoes_politicas"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Há fotos coloridas da Rússia dos czares, de 1909 a 1915: cada cena virava três fotos em preto e branco, com filtros vermelho, verde e azul. Juntá-las com facilidade só foi possível quase um século depois, no computador.",
        "explicacao": (
            "Sergei Prokudin-Gorsky, químico que estudou com Mendeleev, percorreu o Império Russo num vagão de "
            "trem com laboratório fotográfico, cedido pelo czar Nicolau II, e com licenças para entrar em áreas "
            "restritas. O método de três cores fora sugerido por Maxwell em 1855: a mesma cena era registrada em "
            "três fotos em preto e branco, cada uma atrás de um filtro. Para ver as cores, era preciso projetar as "
            "três imagens sobrepostas, com filtros iguais, num aparelho próprio. Como as três exposições não eram "
            "simultâneas, tudo o que se mexia ganhava contornos ou \"fantasmas\" coloridos. Ao deixar o país, "
            "depois da Revolução, cerca de metade do material foi confiscada. Os negativos de vidro restantes "
            "acabaram guardados no porão de um prédio em Paris, e a Biblioteca do Congresso dos EUA os comprou "
            "dos herdeiros em 1948. Por meio século, só uma centena de imagens foi usada, de tão trabalhoso que "
            "era fazer cópias coloridas. Em 2004, um cientista da computação combinou automaticamente as cores "
            "dos 1.902 negativos, e as imagens viraram um retrato vívido de um mundo desaparecido às vésperas da "
            "Primeira Guerra."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Sergey_Prokudin-Gorsky",
                "Using a railway-car darkroom provided by Emperor Nicholas II, Prokudin-Gorsky travelled the Russian Empire from around 1909 to 1915 using his three-image colour photography to record its many aspects. [...] "
                "where Prokudin-Gorsky enrolled in Saint Petersburg State Institute of Technology to study chemistry under Dmitri Mendeleev. [...] "
                "The method of color photography used by Prokudin-Gorsky was first suggested by James Clerk Maxwell in 1855 and demonstrated in 1861 [...] "
                "by capturing it in the form of three black-and-white photographs, one taken through a red filter, one through a green filter, and one through a blue filter. The resulting three photographs could be projected through filters of the same colors and exactly superimposed on a screen [...] "
                "When the three color-filtered photographs were not taken at the same time, anything in the scene that did not hold steady during the entire operation would exhibit colored \"fringes\" around its edges in the resulting color image. If it moved continuously across the scene, three separate strongly-colored \"ghost\" images could result. [...] "
                "Outfitted with a specially equipped railroad-car darkroom provided by Tsar Nicholas II and in possession of two permits that granted him access to restricted areas [...] "
                "His photographs offer a vivid portrait of a lost world—the Russian Empire on the eve of World War I [...] "
                "Upon leaving the country and exporting all his photographic material, about half of the photos were confiscated by Russian authorities [...] "
                "were finally stored in the basement of a Parisian apartment building, and the family was worried about them getting damaged. The United States Library of Congress purchased the material from Prokudin-Gorsky's heirs in 1948 [...] "
                "only about a hundred of the images were used in exhibits, books and scholarly articles during the half-century after the Library of Congress acquired them. [...] "
                "It was only with the advent of digital image processing that multiple images could be quickly and easily combined into one. [...] "
                "In 2004, the Library of Congress contracted with computer scientist Blaise Agüera y Arcas to produce an automated color composite of each of the 1,902 negatives",
                nome="Sergey Prokudin-Gorsky"),
        ],
    },
    # 13 Lippmann: fotos coloridas sem corante
    {
        "temas_secundarios": ["luz_cores", "exploracao_espacial"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Em 1891, Gabriel Lippmann fez fotos coloridas sem corante algum: um espelho de mercúrio fazia a luz interferir consigo mesma e gravar as cores em camadas finíssimas. A ideia lhe deu o Nobel de Física de 1908.",
        "explicacao": (
            "No método de Lippmann, uma placa de vidro recebia uma emulsão sensível quase transparente, de grãos "
            "finíssimos, com um espelho encostado atrás, originalmente de mercúrio líquido. Na exposição, a luz "
            "atravessava a emulsão, batia no espelho e voltava sobre si mesma, formando ondas estacionárias. Isso "
            "deixava na emulsão várias camadas escurecidas, separadas por distâncias que correspondem ao "
            "comprimento de onda de cada cor. Depois de revelada, a placa devolve a luz branca reforçando só as "
            "cores certas, e o resultado reproduz as cores originais usando um processo fotográfico de preto e "
            "branco. A imagem só aparece no reflexo de uma luz difusa, num ângulo limitado, e não pode ser copiada "
            "com técnicas comuns. O processo exigia exposições demoradas para as emulsões da época, nunca entrou "
            "em uso geral e perdeu espaço para as placas autocromo dos irmãos Lumière, mas sobreviveu como "
            "experimento de física. A durabilidade dessas placas inspirou uma nova aplicação: guardar dados. Em "
            "2019, 150 amostras gravadas pelo mesmo princípio foram levadas à Estação Espacial Internacional e, "
            "após nove meses de exposição a raios cósmicos, não mostraram sinais de perda de dados."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Lippmann_plate",
                "It was invented by French scientist Gabriel Lippmann in 1891 and consists of first focusing an image onto a light-sensitive plate, placing the emulsion in contact with a mirror (originally liquid mercury) during the exposure to introduce interference [...] "
                "Lippmann won the Nobel Prize in Physics in 1908 \"for his method of reproducing colours photographically based on the phenomenon of interference\". "
                "Images made with this method are created on a Lippmann plate: a clear glass plate (having no anti-halation backing), coated with an almost transparent (very low silver halide content) emulsion of extremely fine grains [...] "
                "the light rays which strike the transparent light-sensitive film are reflected back on themselves and, by interference, create standing waves. [...] "
                "The result is an image having very similar colours as the original using a black and white photographic process. [...] "
                "The colour image can only be viewed in the reflection of a diffuse light source from the plate, making the field of view limited, and therefore not easily copied with conventional techniques. The method was very insensitive with the emulsions of the time and it never came into general use. Another reason Lippmann's process of colour photography did not succeed can be found in the invention of the autochrome plates by the Lumière brothers. [...] "
                "Because the photographs are so durable, researchers have reworked Lippmann plates for use in archival data storage to replace hard drives. [...] "
                "150 standing-wave storage samples placed on the ISS during 2019 showed no signs of data degradation after exposure to cosmic rays for nine months.",
                nome="Lippmann plate"),
            {"url": "https://www.nobelprize.org/prizes/physics/1908/lippmann/facts/", "titulo": "Gabriel Lippmann – Facts (NobelPrize.org)", "idioma": "en",
             "trecho": "In the 1890s Gabriel Lippmann discovered a method for color photography based on interference—interaction between light waves. Using a mirror, light was reflected through a photographic emulsion in which the interference phenomenon produces a number of blackened layers. The distance between the layers corresponds to certain wavelengths and can be transmuted into a color image. The method never came into widespread usage, but lived on as a physics experiment."},
        ],
    },
    # 14 o filme sonoro de Dickson, reunido mais de cem anos depois
    {
        "temas_secundarios": ["historia_musica", "invencoes"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "O filme mais antigo que se conhece com som gravado ao vivo, de 1894 ou 1895, mostra dois homens dançando ao som de um violino. Imagem e som só foram reunidos mais de cem anos depois: o cilindro de cera estava partido.",
        "explicacao": (
            "O curta foi feito por William Dickson no \"Black Maria\", o estúdio de Thomas Edison em Nova Jersey, "
            "para o Kinetofone, um visor de filmes acompanhado de um fonógrafo de cilindro. Dickson toca violino "
            "diante de uma corneta que grava o som num cilindro de cera, enquanto dois homens dançam à frente. Não "
            "há sinal de que o filme tenha sido exibido no formato original. Uma cópia muda foi parar no Museu de "
            "Arte Moderna de Nova York. O som ficou esquecido: um cilindro numa lata com o nome de Dickson foi "
            "achado no laboratório de Edison no início dos anos 1960 e, quando a lata foi aberta, em 1964, ele "
            "estava quebrado em dois. Só em 1998 pesquisadores ligaram o cilindro ao filme, mandaram consertá-lo "
            "e recuperaram o áudio. O premiado montador Walter Murch sincronizou digitalmente imagem e som, e a "
            "versão restaurada foi projetada em 2002. No cilindro, antes da música, um homem pergunta se já está "
            "funcionando. Um livro de 1981 afirmou, sem citar fonte, que o filme se chamava \"The Gay Brothers\"; "
            "o título se espalhou, mas não há evidência de que tenha existido."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Dickson_Experimental_Sound_Film",
                "The Dickson Experimental Sound Film is a film made by William Dickson in late 1894 or early 1895. It is the first known film with live-recorded sound and appears to be the first motion picture made for the Kinetophone, the proto-sound-film system developed by Dickson and Thomas Edison. (The Kinetophone, consisting of a Kinetoscope accompanied by a cylinder-playing phonograph [...] "
                "The film was produced at the \"Black Maria\", Edison's New Jersey film studio. There is no evidence that it was ever exhibited in its original format. [...] "
                "The film features Dickson playing a violin into a recording horn for an off-camera wax cylinder. [...] "
                "In front of Dickson, two men dance to the music. [...] "
                "A soundless 35mm nitrate print of the movie, described as precisely forty feet long, was acquired by the Museum of Modern Art [...] "
                "The soundtrack was inventoried at the Edison National Historic Site in the early 1960s when a wax cylinder in a metal canister labeled \"Dickson—Violin by W.K.L. Dixon with Kineto\" was found in the music room of the Edison laboratory. In 1964, researchers opened the canister only to find that the cylinder was broken in two [...] "
                "The connection between the film and the cylinder was not made until 1998 when Loughney and Edison NHS sound recordings curator Jerry Fabris arranged for the cylinder to be repaired and its contents recovered [...] "
                "award-winning film editor Walter Murch be enlisted on the project [...] "
                "By digitally converting the film and editing the media together, Murch synchronized the visual and audio elements. [...] "
                "This version was projected on a 20' screen at the Edison National Historic Site on June 1, 2002 [...] "
                "On the cylinder, before the camera starts rolling, a man's voice can be heard to say, \"I asked if it's working. Is it working already? Go ahead.\" [...] "
                "In his book The Celluloid Closet (1981), film historian Vito Russo discusses the film, claiming, without attribution, that it was titled The Gay Brothers. Russo's unsupported naming of the film has been adopted widely online and in at least three books [...] "
                "In addition to there being no evidence for the title Russo gives the film",
                nome="Dickson Experimental Sound Film"),
        ],
    },
    # 15 as fadas de Cottingley e Conan Doyle
    {
        "temas_secundarios": ["crimes_arte", "literatura"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1917, duas primas inglesas de 16 e 9 anos fotografaram \"fadas\" recortadas de um livro infantil. Conan Doyle, o criador de Sherlock Holmes, publicou as fotos como prova. Elas só admitiram a farsa em 1983.",
        "explicacao": (
            "Elsie Wright e Frances Griffiths brincavam num riacho no fundo do quintal, na vila de Cottingley, e "
            "diziam ir até lá para ver fadas. Para provar, Elsie pegou emprestada a câmera do pai. Ele, fotógrafo "
            "amador, logo achou que as figuras eram recortes de papelão, mas a mãe acreditou nelas. As fotos se "
            "tornaram públicas em 1919 e chegaram a Arthur Conan Doyle, que as usou para ilustrar um artigo sobre "
            "fadas na revista The Strand, no Natal de 1920, tratando-as como prova do sobrenatural. Ao todo, foram "
            "cinco fotos. Décadas depois, análises de céticos e de um editor de revista de fotografia concluíram "
            "que eram falsas. Em 1983, as primas admitiram: Elsie copiara fadas de um livro ilustrado, recortara "
            "as figuras e as prendera com alfinetes de chapéu, jogando tudo no riacho depois. Mesmo assim, as duas "
            "sustentavam que tinham visto fadas de verdade. Disseram que ficaram envergonhadas de desmentir um "
            "homem tão brilhante. Só discordaram sobre a quinta foto, que Frances jurava ser verdadeira; um "
            "especialista sugeriu uma dupla exposição acidental, o que explicaria por que as duas diziam, "
            "sinceramente, tê-la tirado."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Cottingley_Fairies",
                "They appear in a series of five photographs taken by Elsie Wright and Frances Griffiths, two young cousins who lived in Cottingley, near Bradford in England. In 1917, when the first two photographs were taken, Elsie was 16 years old and Frances was 9. The pictures came to the attention of writer Sir Arthur Conan Doyle, who used them to illustrate an article on fairies he had been commissioned to write for the Christmas 1920 edition of The Strand Magazine. Doyle was enthusiastic about the photographs, and interpreted them as clear and visible evidence of supernatural phenomena. [...] "
                "The two girls often played together beside the beck at the bottom of the garden [...] "
                "Frances and Elsie said they only went to the beck to see the fairies, and to prove it, Elsie borrowed her father's camera [...] "
                "Elsie's father, Arthur, was a keen amateur photographer [...] "
                "he dismissed the figures as cardboard cutouts. [...] "
                "His wife Polly, however, believed the photographs to be authentic. [...] "
                "The photographs became public in mid-1919 [...] "
                "Geoffrey Crawley, editor of the British Journal of Photography [...] "
                "He also concluded that the pictures were fakes. [...] "
                "In 1983, the cousins admitted in an article published in the magazine The Unexplained that the photographs had been faked, although both maintained that they really had seen fairies. Elsie had copied illustrations of three dancing fairies by Claude Shepperson from a book [...] "
                "They said they had then cut out the cardboard figures and supported them with hatpins, disposing of their props in the beck once the photograph had been taken. But the cousins disagreed about the fifth and final photograph [...] "
                "Elsie maintained it was a fake, just like all the others, but Frances insisted that it was genuine. [...] "
                "Both Frances and Elsie claimed to have taken the fifth photograph. [...] "
                "suggesting that the photograph was \"an unintended double exposure of fairy cutouts in the grass\", and thus \"both ladies can be quite sincere in believing that they each took it\". [...] "
                "Elsie said that she and Frances were too embarrassed to admit the truth after fooling Doyle, the author of Sherlock Holmes",
                nome="Cottingley Fairies"),
        ],
    },
    # 16 o cinema mudo era colorido
    {
        "temas_secundarios": ["pigmentos", "luz_cores"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "O cinema mudo não era só preto e branco: no início dos anos 1920, 80% dos filmes tinham algum tipo de cor. Foi o som que a fez sumir, porque os corantes atrapalhavam a trilha gravada na própria película.",
        "explicacao": (
            "Sem processos práticos de cor natural, as cópias dos filmes mudos eram muitas vezes mergulhadas em "
            "corantes, com um código de cores: azul para cenas noturnas, amarelo ou âmbar para o dia, vermelho "
            "para fogo e verde para um clima de mistério. Havia também a viragem, que trocava a prata da imagem "
            "por sais ou corantes, como o conhecido tom sépia, e a colorização à mão, usada nos EUA desde 1895 e "
            "muito explorada pelo francês Georges Méliès. Alguns processos chegavam a cores bastante naturais, "
            "com duas cores, como o Kinemacolor e o Technicolor. Quando o som passou a ser gravado na própria "
            "película, os corantes passaram a atrapalhar a alta resolução de que a trilha sonora precisava, e "
            "essas técnicas foram abandonadas. O Technicolor de três tiras, lançado em meados dos anos 1930, era "
            "caro e cheio de limitações. Resultado: por quase quatro décadas, a cor não foi tão comum no cinema "
            "quanto tinha sido na era muda."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Silent_film",
                "Another misconception is that all silent films lacked color. In fact, color was more prevalent in silent films than in the first few decades of sound films. By the early 1920s, 80 percent of movies could be seen in some sort of color, usually in the form of film tinting or toning or hand coloring, but also with fairly natural two-color processes such as Kinemacolor and Technicolor. Traditional colorization processes ceased with the adoption of sound-on-film technology. Traditional film colorization, which involved the use of dyes in some form, interfered with the high resolution required for built-in recorded sound, and was therefore abandoned. The innovative three-strip technicolor process introduced in the mid-1930s was costly and fraught with limitations, and color would not have the same prevalence in film as it did in the silents for nearly four decades. [...] "
                "With the lack of natural color processing available, films of the silent era were frequently dipped in dyestuffs and dyed various shades and hues to signal a mood or represent a time of day. Hand tinting dates back to 1895 in the United States [...] "
                "Blue represented night scenes, yellow or amber meant day. Red represented fire and green represented a mysterious atmosphere. Similarly, toning of film (such as the common silent film generalization of sepia-toning) with special solutions replaced the silver particles in the film stock with salts or dyes of various colors. [...] "
                "Hand coloring was often used in the early \"trick\" and fantasy films of Europe, especially those by Georges Méliès.",
                nome="Silent film"),
        ],
    },
]
