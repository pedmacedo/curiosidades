LOTE = "2026-11-19-literatura-01"
AREA = "artes"
TEMA = "literatura"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/", "fr": "https://fr.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


def fonte(url, titulo, idioma, trecho):
    return {"url": url, "titulo": titulo, "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Cervantes e Shakespeare: mesma data, dias diferentes
    {
        "temas_secundarios": ["calendarios", "teatro_danca"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "O Dia Mundial do Livro cai em 23 de abril porque Cervantes e Shakespeare teriam morrido nessa data, em 1616. Mas não no mesmo dia: Shakespeare morreu 11 dias depois, e o 23 de Cervantes é o do enterro.",
        "explicacao": (
            "A data que a UNESCO escolheu em 1995 para o Dia Mundial do Livro e do Direito de Autor homenageia, "
            "entre outros, William Shakespeare e o Inca Garcilaso de la Vega, que morreram num 23 de abril. A ideia "
            "de um dia do livro vinha de antes: em 1922, o diretor de uma editora de Barcelona a propôs para "
            "honrar Cervantes, e a festa passou para 23 de abril em 1930, tida como a data da morte do autor de "
            "Dom Quixote. A coincidência com Shakespeare é só de calendário. Em 1616, a Espanha já usava o "
            "calendário gregoriano, adotado ali em 1582, enquanto a Inglaterra ainda seguia o juliano. O 23 de "
            "abril inglês em que Shakespeare morreu corresponde a 3 de maio no calendário gregoriano. Do lado "
            "espanhol, hoje se aceita que Cervantes morreu em 22 de abril, e que o dia 23, por muito tempo tomado "
            "como a data da morte, é na verdade a do sepultamento. Resultado: os dois morreram com 11 dias de "
            "diferença, e a coincidência que inspirou a data só existe no papel."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("World_Book_Day",
                "The first World Book Day was celebrated on 23 April in 1995 [...] "
                "The original idea was conceived in 1922 by Vicente Clavel, director of Cervantes publishing house in Barcelona, as a way to honour the author Miguel de Cervantes and boost the sales of books. "
                "It was first celebrated in Spain on 7 October 1926, Cervantes' birthday, before being moved to his death date, 23 April, in 1930. [...] "
                "In 1995, UNESCO decided that the World Book and Copyright Day would be celebrated on 23 April, as the date is also the anniversary of the death of William Shakespeare and Inca Garcilaso de la Vega [...] "
                "Shakespeare and Cervantes died on the same date—23 April 1616—but not on the same day, as at the time, Spain used the Gregorian calendar and England used the Julian calendar; "
                "Shakespeare actually died 11 days after Cervantes died, on 3 May of the Gregorian calendar, and Cervantes died on 22 April but was buried a day after, on 23 April.",
                nome="World Book Day"),
            wiki("Miguel_de_Cervantes",
                "It is generally accepted Cervantes died on 22 April 1616 (NS; the Gregorian calendar had superseded the Julian in 1582 in Spain and some other countries). "
                "The date of 23 April 1616 was long considered his death date, but is now understood to be his date of burial.",
                nome="Miguel de Cervantes"),
        ],
    },
    # 2 o Quixote falso e a vingança de Cervantes
    {
        "temas_secundarios": ["leis_julgamentos", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 1614, um anônimo lançou uma falsa segunda parte de Dom Quixote. Cervantes respondeu na ficção: na continuação verdadeira, o Quixote vê o livro falso, muda de planos e faz um personagem da farsa jurar que nunca o viu.",
        "explicacao": (
            "A primeira parte de Dom Quixote saiu em 1605 e ganhou fama até fora da Espanha. Cervantes ainda escrevia a "
            "continuação quando, por volta de setembro de 1614, apareceu em Tarragona um \"segundo volume\" "
            "assinado por Alonso Fernández de Avellaneda, pseudônimo de alguém até hoje não identificado. Entre "
            "os suspeitos estão amigos do dramaturgo Lope de Vega, rival de Cervantes, e Jerónimo de Pasamonte, "
            "um aragonês que inspirou um personagem da primeira parte. Cervantes correu para publicar a "
            "continuação legítima, que saiu em 1615, um ano antes de sua morte, e transformou a afronta em "
            "ficção. Na segunda parte, o Quixote encontra pessoas que leram a primeira e conhecem suas aventuras. "
            "No capítulo 59, ele topa com leitores do livro de Avellaneda, fica indignado com o retrato que o "
            "impostor faz dele e desiste de ir aos torneios de Zaragoza só porque a farsa o levava para lá. Mais "
            "adiante, visita em Barcelona uma gráfica onde o livro falso está sendo impresso, e convence Don "
            "Álvaro Tarfe, personagem de Avellaneda, a declarar em cartório que nunca tinha visto o verdadeiro "
            "Dom Quixote. Para alguns estudiosos, sem o estímulo da farsa Cervantes talvez nem tivesse escrito a "
            "segunda parte."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Don_Quixote",
                "published in two parts in 1605 and 1615. [...] "
                "It is not certain when Cervantes began writing Part Two of Don Quixote, but he had probably not proceeded much further than Chapter LIX by late July 1614. "
                "In about September, however, a spurious Part Two, entitled Second Volume of the Ingenious Gentleman Don Quixote of La Mancha: by the Licenciado (doctorate) Alonso Fernández de Avellaneda, of Tordesillas, was published in Tarragona by an unidentified Aragonese who was an admirer of Lope de Vega, rival of Cervantes. [...] "
                "In Cervantes's Segunda Parte, Don Quixote visits a printing-house in Barcelona and finds Avellaneda's Second Part being printed there, in an early example of metafiction. [...] "
                "This rushed Cervantes into writing and publishing a genuine second part in 1615, which was a year before his own death. "
                "Don Quixote had been growing in favour, and its author's name was now known beyond the Pyrenees.",
                nome="Don Quixote"),
            wiki("Alonso_Fernández_de_Avellaneda",
                "The identity of Avellaneda has been the subject of many theories, but there is no consensus on who he was. [...] "
                "One theory holds that Avellaneda's work was a collaboration by friends of Lope de Vega, although none of them were from Aragon. "
                "Another theory is that it was by Gerónimo de Passamonte, born in Aragon, the real-life inspiration for the character Ginés de Pasamonte of Part I. [...] "
                "However, it is possible that Cervantes would never have composed his own continuation without the stimulus Avellaneda provided. "
                "Throughout Part 2 of Cervantes' book, Don Quixote meets characters who know of him from their reading of his Part 1, but in Chapter 59, Don Quixote first learns of Avellaneda's Part 2. "
                "In that chapter, Don Quixote meets two characters who are reading Avellaneda's recently published book. [...] "
                "Don Quixote is outraged because Avellaneda portrays him as being no longer in love with Dulcinea del Toboso. "
                "As a result, Don Quixote decides not to go to Zaragoza to take part in the jousts, as he had planned, because such an incident features in that book. "
                "From then on, Avellaneda's work is ridiculed frequently; Don Quixote even meets one of its characters, Don Alvaro Tarfe, and gets him to swear an affidavit that he has never met the true Don Quixote before.",
                nome="Alonso Fernández de Avellaneda"),
        ],
    },
    # 3 Aladim e Ali Babá vieram de um sírio em Paris
    {
        "temas_secundarios": ["mundo_islamico_medieval", "personagens_esquecidos"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "Aladim e Ali Babá não estão nos manuscritos árabes antigos das Mil e Uma Noites. Entraram no livro pelo tradutor francês, que os recebeu em Paris, em 1709, de um jovem sírio de Alepo, sem lhe dar crédito.",
        "explicacao": (
            "O francês Antoine Galland traduziu, no começo do século XVIII, um manuscrito árabe incompleto das "
            "Mil e Uma Noites, e sua versão logo ficou popular no Ocidente. Para completar a obra, ele incluiu "
            "histórias que ouviu de Hanna Diyab, um cristão maronita de Alepo que tinha chegado a Paris como "
            "assistente de um viajante a serviço de Luís XIV. Os dois se conheceram em março de 1709, e o diário "
            "de Galland resume as histórias contadas por Diyab naquela primavera. Entre elas estavam as versões "
            "mais conhecidas de Aladim e de Ali Babá e os Quarenta Ladrões, as chamadas \"histórias órfãs\", sem "
            "nenhuma fonte árabe autêntica conhecida. Aladim saiu em 1710, sem menção a Diyab. Mais tarde "
            "apareceram em Paris dois manuscritos árabes com Aladim, e um deles chegou a ser publicado como "
            "original; o arabista Muhsin Mahdi mostrou que ambos eram retraduções do texto francês de Galland. "
            "Diyab passou séculos conhecido só como \"Hanna de Alepo\", até que sua autobiografia, escrita em 1763 "
            "e guardada na Biblioteca do Vaticano, foi traduzida e publicada em 2015. Hoje há pesquisadores que o "
            "consideram o autor original de algumas dessas histórias."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Aladdin",
                "It is one of the best-known tales associated with One Thousand and One Nights (often known in English as The Arabian Nights), despite not being part of the original text; "
                "it was added by the Frenchman Antoine Galland, based on a folk tale that he heard from the Syrian storyteller Hanna Diyab. [...] "
                "Known along with Ali Baba as one of the \"orphan tales\", the story was not part of the original Nights manuscripts and any authentic Arabic textual source has not been found. [...] "
                "It was included in his volumes ix and x of the Nights, published in 1710, without any mention or published acknowledgment of Hanna's contribution. "
                "Payne later recorded the discovery in the Bibliothèque Nationale in Paris of two Arabic manuscripts containing Aladdin [...] "
                "The Arabist Hermann Zotenberg believed in the authenticity of Sabbagh Manuscript, so he published a critical edition of the Arabic version of Sabbagh in 1888. [...] "
                "the Arabist scholar Muhsin Mahdi has shown that both the Chavis and Sabbagh manuscripts are \"back-translations\" of Galland's French text into Arabic.",
                nome="Aladdin"),
            wiki("Hanna_Diyab",
                "was a Syrian Maronite writer and storyteller. He originated the best-known versions of the tales of Aladdin and Ali Baba and the Forty Thieves which have been added to the One Thousand and One Nights since French orientalist Antoine Galland translated and included them, after which they soon became popular across the West. "
                "Diyab was long known only from brief mentions in the diary of Antoine Galland, but the translation and publication of his Arabic manuscript autobiography in 2015 expanded knowledge about his life. [...] "
                "despite Diyab only having been named as \"Hanna from Aleppo\" in Galland's diary. [...] "
                "Literary scholars Ruth Bottigheimer and Paulo Lemos Horta have argued that Diyab should be understood as the original author of some of the stories published by Galland [...] "
                "Most of what is known about Diyab's life comes from his autobiography, which he composed in 1763, around the age of 75. It survives as Vatican Library MS Sbath 254 [...] "
                "he met the Frenchman Paul Lucas, who was on an expedition in search of antiquities on behalf of Louis XIV of France. [...] "
                "While in Paris, Diyab first met the Orientalist Antoine Galland on Sunday, March 17, 1709. Galland's diary contains extended summaries of stories told by Diyab on March 25. Galland recorded more stories, apparently from oral telling, throughout May and into June that year. "
                "He went on to include these works as a continuation of his French translation of an incomplete Arabic manuscript of the Thousand and One Nights",
                nome="Hanna Diyab"),
        ],
    },
    # 4 Dante: exílio revogado em 2008 e ossos escondidos
    {
        "temas_secundarios": ["europa_medieval", "leis_julgamentos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Florença condenou Dante ao exílio perpétuo e só revogou a sentença em 2008. O túmulo que a cidade lhe fez em 1829 está vazio: em Ravena, os guardiões do corpo chegaram a esconder os ossos numa parede falsa.",
        "explicacao": (
            "Em 1302, numa guerra de facções em Florença, Dante foi acusado de corrupção pelo período em que "
            "ocupara o cargo mais alto da cidade e condenado a exílio e multa. Ele não pagou, em parte por se "
            "achar inocente, e a pena virou exílio perpétuo: se voltasse sem pagar, podia ser queimado na "
            "fogueira. Dante passou o resto da vida fora e morreu em Ravena, em 1321, onde foi enterrado. Em 1329, "
            "um cardeal tachou de herética uma obra política dele e quis queimar seus ossos; aliados do próprio "
            "cardeal intercederam para salvá-los. Com o tempo, Florença se arrependeu e pediu várias vezes os "
            "restos do poeta de volta. Ravena sempre recusou, e os guardiões do corpo chegaram a escondê-lo numa "
            "parede falsa do mosteiro. Em 1829, Florença ergueu um túmulo para Dante na basílica de Santa Croce, "
            "que continua vazio. Em 1945, o governo fascista ainda discutiu levar os restos para o reduto alpino "
            "onde pretendia resistir aos Aliados, mas nada foi feito. Em junho de 2008, quase sete séculos depois "
            "da morte dele, a câmara municipal de Florença aprovou a revogação da sentença."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Dante_Alighieri",
            "In March 1302, Dante, a White Guelph by affiliation, along with the Gherardini family, was condemned to exile for two years and ordered to pay a large fine. "
            "Dante was accused of corruption and financial wrongdoing by the Black Guelphs for the time that Dante was serving as city prior (Florence's highest position) for two months in 1300. [...] "
            "Dante did not pay the fine, in part because he believed he was not guilty and in part because all his assets in Florence had been seized by the Black Guelphs. "
            "He was condemned to perpetual exile; if he had returned to Florence without paying the fine, he could have been burned at the stake. "
            "(In June 2008, nearly seven centuries after his death, the city council of Florence passed a motion rescinding Dante's sentence.) [...] "
            "Dante died in Ravenna on September 14, 1321 [...] He was buried in Ravenna at the Church of San Pier Maggiore (later called Basilica di San Francesco). [...] "
            "In 1329, Bertrand du Pouget, Cardinal and nephew of Pope John XXII, classified Dante's Monarchia as heretical and sought to have his bones burned at the stake. "
            "Ostasio I da Polenta and Pino della Tosa, allies of Pouget, interceded to prevent the destruction of Dante's remains. "
            "Florence eventually came to regret having exiled Dante. The city made repeated requests for the return of his remains. "
            "The custodians of the body in Ravenna refused, at one point going so far as to conceal the bones in a false wall of the monastery. "
            "Florence built a tomb for Dante in 1829, in the Basilica of Santa Croce. That tomb has been empty ever since, with Dante's body remaining in Ravenna. [...] "
            "In 1945, the fascist government discussed bringing Dante's remains to the Valtellina Redoubt, the Alpine valley in which the regime intended to make its last stand against the Allies. [...] "
            "but ultimately, no action was taken.",
            nome="Dante Alighieri")],
    },
    # 5 Kafka mandou queimar; os papéis viraram processo até 2016
    {
        "temas_secundarios": ["leis_julgamentos", "segunda_guerra"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Kafka pediu ao amigo Max Brod que queimasse seus inéditos. Brod recusou, publicou os romances e fugiu dos nazistas com uma mala de papéis do amigo. O destino do acervo só se decidiu na Justiça de Israel, em 2016.",
        "explicacao": (
            "Franz Kafka morreu de tuberculose em 1924, aos 40 anos, pouco conhecido. Tinha nomeado o amigo Max "
            "Brod como executor literário, com a instrução de queimar o que não tinha sido publicado. Brod se "
            "recusou e contou que já tinha avisado Kafka disso em vida. Graças a ele saíram \"O Processo\" (1925), "
            "\"O Castelo\" (1926) e \"Amerika\" (1927), obras que acabaram aclamadas. Em 1939, com a ocupação de Praga pelos nazistas, Brod emigrou para a Palestina sob mandato "
            "britânico levando uma mala de papéis de Kafka, com diários, notas e esboços. Quando morreu, em 1968, "
            "deixou os inéditos, que seriam milhares, para a secretária, Esther Hoffe. Ela vendeu peças avulsas, como o manuscrito "
            "original de \"O Processo\", leiloado em 1988 por 2 milhões de dólares, e o resto ficou com as filhas. "
            "Em 2008 começou uma briga judicial entre elas e a Biblioteca Nacional de Israel, que via os papéis "
            "como bens culturais do povo judeu. Um tribunal de família de Tel Aviv deu razão à biblioteca em 2012, "
            "e a Suprema Corte de Israel confirmou a decisão em dezembro de 2016."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Max_Brod",
                "Kafka named Brod as his literary executor, instructing Brod to burn his unpublished work upon his death. Brod refused and had Kafka's works published instead. "
                "In 1939, as the Nazis occupied Prague, he immigrated to Mandatory Palestine, taking with him a suitcase of Kafka's papers, many of them unpublished notes, diaries, and sketches. [...] "
                "He justified this move by stating that when Kafka personally told him to burn his unpublished work, Brod replied that he would outright refuse [...] "
                "fka's works were posthumously published (The Trial arrived in 1925, followed by The Castle in 1926 and Amerika in 1927) [...] "
                "Upon his death, this trove of materials was passed to Esther Hoffe, who maintained most of them until her own death in 2007 (one original manuscript of The Trial was auctioned in 1988 for $2 million).",
                nome="Max Brod"),
            wiki("Franz_Kafka",
                "He died relatively unknown in 1924 of tuberculosis, aged 40. His literary executor and friend Max Brod ignored Kafka's wishes to destroy his remaining works, publishing them to eventual acclaim. [...] "
                "When Brod died in 1968, he left Kafka's unpublished papers, which are believed to number in the thousands, to his secretary Esther Hoffe. "
                "She released or sold some, but left most to her daughters, Eva and Ruth, who also refused to release the papers. "
                "A court battle began in 2008 between the sisters and the National Library of Israel [...] "
                "while the National Library of Israel argues they are \"cultural assets belonging to the Jewish people\". [...] "
                "The Tel Aviv Family Court ruled in October 2012, six months after Ruth's death, that the papers were the property of the National Library. "
                "The Israeli Supreme Court upheld the decision in December 2016.",
                nome="Franz Kafka"),
        ],
    },
    # 6 o romance de Agatha Christie que salvou uma criança
    {
        "temas_secundarios": ["elementos_quimicos", "historia_medicina"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "Médicos de Londres não descobriam o que tinha uma menina de 19 meses trazida do Catar. Uma enfermeira que lia um romance de Agatha Christie reconheceu os sintomas: era envenenamento por tálio, de um veneno de baratas.",
        "explicacao": (
            "Em \"O Cavalo Amarelo\" (The Pale Horse), de 1961, Agatha Christie usa o tálio como arma de "
            "assassinato, e a primeira pista do método é a queda de cabelo das vítimas. A escritora conhecia "
            "venenos de perto: nas duas guerras mundiais, trabalhou como auxiliar na farmácia de hospitais. O "
            "livro ficou famoso por ter ajudado a salvar pelo menos duas vidas. Num dos casos, uma "
            "menina de 19 meses que morava no Catar foi levada ao Hospital Hammersmith, em Londres, com sintomas "
            "que intrigavam os médicos. A enfermeira Marsha Maitland, que estava lendo o romance, sugeriu que fosse "
            "tálio, e acertou: a fonte era um veneno contra baratas usado em casa, com sulfato de tálio. Em outro "
            "episódio, uma mulher na América do Sul desconfiou que um amigo estava sendo envenenado pela esposa, "
            "porque reconheceu os sinais descritos no livro."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Thallium_poisoning",
                "Agatha Christie, who worked as an apothecary's assistant, used thallium in 1961 as the agent of murder in her detective fiction novel The Pale Horse – the first clue to the murder method coming from the hair loss of the victims. "
                "This novel is notable as being credited with having saved at least two lives after readers recognised the symptoms of thallium poisoning that Christie described. [...] "
                "In 1977, a 19 month-old girl living in Qatar fell ill due to thallium poisoning (from pesticides used by her parents). "
                "While doctors could not identify the cause, a nurse named Marsha Maitland managed to do it from the description of the symptoms given in The Pale Horse.",
                nome="Thallium poisoning"),
            fonte("https://hekint.org/?p=42421", "Agatha Christie's poisons: Better dying through chemistry (Hektoen International)", "en",
                "She volunteered for service at a hospital in England for wounded soldiers during the Great War. "
                "She started as a dishwasher, was promoted to floor sweeper, then nurses’ assistant, and finally, assistant in the hospital pharmacy. [...] "
                "During the Second World War, she volunteered again as a pharmacy assistant at the University College Hospital, London. [...] "
                "In 1975, a woman in South America suspected a friend was being poisoned by his wife. "
                "She had read The Pale Horse and recognized the signs and symptoms of thallium poisoning from the novel. [...] "
                "a nineteen-month-old girl from Qatar was brought to the Hammersmith Hospital in London with puzzling findings. "
                "Luckily, a nurse recognized—again from The Pale Horse—the symptoms of thallium intoxication. "
                "The child was, indeed, suffering from thallium poisoning, and the offending substance was a roach poison used at home containing thallium sulfate."),
        ],
    },
    # 7 Malba Tahan era um professor carioca
    {
        "temas_secundarios": ["historia_matematica", "mundo_islamico_medieval"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "Malba Tahan, o sábio árabe de \"O Homem que Calculava\", nunca existiu. Era o professor carioca Júlio César de Mello e Souza, que nunca pisou nos desertos que descrevia e que, na escola, chegou a ser reprovado em álgebra.",
        "explicacao": (
            "Júlio César de Mello e Souza nasceu no Rio de Janeiro em 1895 e cresceu em Queluz, no interior "
            "paulista. Não foi bom aluno: numa carta de 1905, o irmão contou aos pais que ele era fraco na escrita e "
            "\"um fracasso em matemática\", e no Colégio Pedro II foi reprovado num exame de álgebra. Em 1918, "
            "jornalista no Rio, ofereceu contos ao chefe, que nem os leu. Dias depois, voltou com os mesmos textos "
            "dizendo que eram traduções de um tal R. S. Slady, sucesso em Nova York, e eles saíram na primeira "
            "página. A lição o levou a inventar um autor estrangeiro. Escolheu um árabe, porque considerava os "
            "árabes insuperáveis na arte de contar histórias, e passou anos estudando árabe e cultura islâmica. "
            "Nasceu Malba Tahan, com biografia completa e um \"tradutor\" igualmente fictício. O sobrenome Tahan "
            "veio de uma aluna dele. Os livros, que misturam problemas de matemática a contos inspirados nas Mil e "
            "Uma Noites, fizeram dele uma celebridade nacional. Mesmo assim, as viagens dele ao exterior se "
            "resumiram a Buenos Aires, Montevidéu e Lisboa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Malba_Tahan",
            "Júlio César de Mello e Souza (Rio de Janeiro, May 6, 1895 – Recife, June 18, 1974), was a Brazilian writer and mathematics teacher. "
            "He was well known in Brazil and abroad for his books on recreational mathematics, most of them published under the pen name of Malba Tahan, a fictitious Persian scholar. [...] "
            "Júlio César's most popular books, including The Man Who Counted, are collections of mathematical problems, puzzles, curiosities, and embedded in tales inspired by the Arabian Nights. [...] "
            "Yet Júlio César's travels outside Brazil were limited to short visits to Buenos Aires, Montevideo, and Lisbon: he never set foot in the deserts and cities he described in his books. [...] "
            "Júlio César was born in Rio de Janeiro but spent most of his childhood in Queluz, a small rural town in the State of São Paulo. [...] "
            "In a 1905 letter to their parents, João Batista tells that little Júlio \"is bad at writing, and a failure in mathematics\".  "
            "His grade reports at Colégio Pedro II show that he once failed an Algebra exam, and barely passed one on Arithmetic. [...] "
            "In 1918, at the age of 23, Júlio César presented five of his tales to the editor of the newspaper O Imparcial, where he worked, but his boss did not even look at them.  "
            "Undaunted, Júlio picked up the manuscripts and brought them back a few days later, this time pretending that they were translations of the work of a certain \"R. S. Slady,\" supposedly the rage in New York City. "
            "The first of those tales, The Jew's Revenge, was published in the front page of the next issue of the newspaper; and the rest followed suit. "
            "This experience convinced Júlio to assume a \"foreign\" pen name.  "
            "He chose an Arabian identity — because, as he declared in an interview, the Arabs were unsurpassed in the art of storytelling. "
            "For the next seven years he prepared himself by studying Arabic and reading all he could on Islamic culture. [...] "
            "and ostensibly translated by an equally fictitious \"Professor Breno Alencar Bianco\". [...] "
            "his books were a resounding success, and he became a national celebrity. [...] "
            "but Tahan was in fact the surname of one of Julio Souza's students, Maria Zechsuk Tahan.",
            nome="Malba Tahan")],
    },
    # 8 Carolina Maria de Jesus e os cadernos do lixo
    {
        "temas_secundarios": ["brasil_republica", "cidades"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Catadora numa favela de São Paulo, com dois anos de escola, Carolina Maria de Jesus escrevia um diário em cadernos achados no lixo. Publicado em 1960, \"Quarto de Despejo\" virou best-seller e saiu em mais de dez línguas.",
        "explicacao": (
            "Carolina nasceu em 1914 em Sacramento, Minas Gerais, filha de lavradores analfabetos, e estudou só "
            "dois anos, o bastante para aprender a ler e escrever. Em São Paulo, depois de perder o emprego de "
            "empregada doméstica, foi morar na favela do Canindé, num barraco que ela mesma montou com restos de "
            "madeira, latas e papelão, e sustentava três filhos catando material reciclável. Entre o que recolhia "
            "apareciam cadernos, e neles passou a registrar a vida na favela, para irritação dos vizinhos. Em "
            "1958, o jornalista Audálio Dantas a ouviu gritar a um grupo que expulsava crianças de um parquinho: "
            "\"Vou pôr os nomes de vocês no meu livro!\". Ela lhe mostrou os cadernos, e um trecho saiu no jornal. O "
            "livro, lançado em agosto de 1960, esgotou rapidamente a primeira edição de 10 mil exemplares, ganhou "
            "novas tiragens e foi traduzido para pelo menos treze línguas. O título vinha da ideia dela de que a "
            "favela era o quarto de despejo da cidade. Dantas editou bastante o texto, e houve quem duvidasse da "
            "autoria, mas os manuscritos dela foram preservados."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Carolina_Maria_de_Jesus",
            "She is best known for her diary, published in August 1960 as Quarto de Despejo (lit. \"Junk Room\") after attracting the attention of a Brazilian journalist, which became a bestseller and won international acclaim. [...] "
            "De Jesus spent a significant part of her life in the Canindé [pt] favela in North São Paulo, supporting herself and three children as a scrap collector. [...] "
            "Carolina Maria de Jesus was born in 1914 in Sacramento, Minas Gerais, which at that time was a small rural town. Her parents were illiterate sharecroppers. [...] "
            "Her formal education lasted a meagre two years, though by then she was already able to read and write. [...] "
            "These reasons led to her dismissal by the family for which she was a maid, and she ended up needing to live in the nearby favela, Canindé. [...] "
            "De Jesus made her own shack out of scrap plywood, cans, cardboard, or pretty much anything she could obtain. "
            "Among the materials she collected, there would be an occasional journal or notebook, as well as books, which encouraged her to start recording her day-to-day activities and write about life in the favela. "
            "It angered her neighbours that she was always writing [...] "
            "She had been discovered by journalist Audálio Dantas in April 1958. [...] "
            "Dantas saw de Jesus standing at the edge of the playground shouting, \"If you continue mistreating these children, I'm going to put all of your names in my book!\". [...] "
            "He asked her for a small sample and subsequently ran it in the newspaper. [...] "
            "The inspiration for the book's title came from de Jesus' believing the favela was society's junk room [...] "
            "The first edition quickly sold its 10,000 initial copies. [...] "
            "the book was translated into thirteen (another source says fourteen) languages and became a bestseller in North America and Europe. [...] "
            "The book was heavily edited by Dantas, and some critics suspected it a fraud; but the original manuscript was preserved",
            nome="Carolina Maria de Jesus")],
    },
    # 9 a tragédia da Piedade: Euclides e o filho mortos pelo mesmo homem
    {
        "temas_secundarios": ["brasil_republica", "leis_julgamentos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Euclides da Cunha, autor de \"Os Sertões\", morreu em 1909 ao atacar a tiros o amante da esposa, que reagiu. Em 1916, o filho do escritor tentou vingá-lo e foi morto pelo mesmo homem, absolvido nas duas vezes.",
        "explicacao": (
            "Euclides da Cunha, engenheiro e jornalista, ficou célebre com \"Os Sertões\", de 1902, sobre a Guerra de "
            "Canudos, e entrou para a Academia Brasileira de Letras em 1903. Ele viajava muito a trabalho, e a "
            "mulher, Ana Emília, começou em 1905 um caso com Dilermando de Assis, um cadete de 17 anos. Em 15 de "
            "agosto de 1909, Euclides arranjou uma arma e foi à casa onde Dilermando estava, no Rio, dizendo que "
            "ia \"matar ou morrer\". Feriu o irmão do rapaz e acertou o próprio Dilermando, que tinha treino militar "
            "e o matou com dois tiros. A imprensa tratou Dilermando como vilão, mas o júri o absolveu por legítima "
            "defesa, e ele se casou com a viúva em 1911. Em 4 de julho de 1916, Euclides da Cunha Filho, o "
            "\"Quidinho\", de 22 anos, atirou pelas costas em Dilermando num cartório do fórum do Rio. Ferido, "
            "Dilermando reagiu e o matou. Foi absolvido de novo, mas carregou para sempre a marca das duas mortes: "
            "quando morreu, em 1951, chegou a ter o enterro negado num cemitério de São Paulo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Euclides_da_Cunha",
                "His most important work is Os Sertões (Rebellion in the Backlands), a non-fictional account of the military expeditions promoted by the Brazilian government against the rebellious village of Canudos, known as the War of Canudos. [...] "
                "In 1903 he was elected to the Academia Brasileira de Letras (Brazilian Academy of Letters) [...] "
                "Ana Emília had an affair with Dilermando de Assis, a young Army lieutenant. [...] "
                "The jury decided for the latter scenario and acquitted Dilermando. [...] "
                "1902 Os Sertões",
                nome="Euclides da Cunha"),
            wiki("Dilermando_de_Assis",
                "Dilermando começou um relacionamento com a esposa de Euclides da Cunha, Ana Emília Ribeiro da Cunha, em 1905 [...] "
                "Ana tinha três filhos com Euclides e 33 anos de idade quando se apaixonou pelo jovem cadete do Exército Brasileiro, Dilermando, que tinha apenas 17 anos. [...] "
                "Euclides viajava muito a serviço, ficando longos períodos fora de casa [...] "
                "Euclides tinha passado em casa de parentes, onde conseguira uma arma, no dia 15 de agosto de 1909, um domingo. "
                "O escritor entra gritando no aposento, berrando que estava ali para “matar ou morrer”. "
                "Ele acerta Dinorah, irmão de Dilermando, e ainda acerta 3 tiros no amante da esposa, mas Dilermando tinha treinamento militar e conseguiu sacar sua arma antes e desferir dois tiros em Euclides da Cunha, que morreu no local. [...] "
                "A imprensa brasileira logo fez de Dilermando o vilão da história por ter matado o Imortal da Academia Brasileira de Letras. [...] "
                "Ele foi absolvido por legítima defesa, mas mesmo assim a visão do público não mudou e ele continuou carregando o estigma do assassinato. [...] "
                "Em 4 de julho de 1916 Dilermando sofre novo atentado, desta feita por parte de Euclides da Cunha Filho, apelidado familiarmente de “Quidinho”, então com 22 anos de idade. "
                "Ele estava em um cartório do fórum do Rio de Janeiro, quando foi alvejado pelas costas por Quidinho. "
                "Mesmo ferido, Dilermando reagiu, matando seu agressor. "
                "Um novo escândalo resulta em uma nova absolvição, mas sua biografia já estava permanentemente marcada pelas duas mortes. [...] "
                "Em 12 de maio de 1911, logo após sua absolvição em 5 de maio, Dilermando se casou com a viúva Ana da Cunha. [...] "
                "Dilermando morreu em São Paulo, em 13 de novembro de 1951 [...] "
                "Na ocasião de sua morte, seu sepultamento no Cemitério do Santíssimo Sacramento, em São Paulo, foi negado, devido seu envolvimento na morte de Euclides da Cunha e seu filho.",
                nome="Dilermando de Assis", idioma="pt"),
        ],
    },
    # 10 Ern Malley: o poeta falso que virou cânone
    {
        "temas_secundarios": ["crimes_arte", "personagens_esquecidos"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Para ridicularizar a poesia modernista, dois australianos escreveram numa só tarde versos sem sentido, com palavras tiradas a esmo de livros, e os atribuíram a um poeta morto inventado. Hoje esses poemas são celebrados.",
        "explicacao": (
            "James McAuley e Harold Stewart, escritores conservadores, desprezavam a poesia de vanguarda da "
            "revista Angry Penguins, editada pelo jovem poeta Max Harris. Criaram então Ern Malley, mecânico e "
            "vendedor de seguros que teria morrido aos 25 anos deixando poemas inéditos. O método, segundo eles: "
            "abrir ao acaso um dicionário, as obras de Shakespeare e um livro de citações, juntar palavras em frases "
            "sem nexo, errar citações de propósito e escolher rimas desajeitadas. Fingindo ser a irmã do morto, "
            "mandaram os poemas a Harris, que os achou geniais e dedicou a eles uma edição da revista, publicada em "
            "1944. Pouco depois, um jornal revelou a farsa e os autores. A polícia da Austrália do Sul processou Harris "
            "por obscenidade; a única testemunha de acusação, um detetive, admitiu não saber o que era "
            "\"incestuoso\", mas achar que soava indecente. Harris foi condenado a uma multa. Nas décadas "
            "seguintes, o caso foi um duro golpe para a poesia modernista na Austrália. Desde os anos 1970, porém, os poemas passaram a ser elogiados como "
            "boa poesia surrealista por críticos e poetas como John Ashbery, e hoje são mais lidos que a obra dos "
            "próprios autores."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Ern_Malley",
            "Its name derives from that of a fictitious poet, Ernest Lalor \"Ern\" Malley, whose biography and body of work were created in one day in 1943 by conservative writers James McAuley and Harold Stewart. "
            "Their aim was to hoax the Angry Penguins, a modernist art and literary movement centred around a journal of the same name, co-edited by poet Max Harris [...] "
            "Imitating the modernist poetry they despised, the hoaxers deliberately created what they thought was bad verse and, pretending to be Ethel, Ern Malley's surviving sister, mailed sixteen poems to Harris. "
            "Harris and other members of the Heide Circle fell for the hoax and, enraptured by the poetry, devoted the next issue of Angry Penguins to Malley, hailing him as a genius. [...] "
            "In the decades that followed, the hoax proved to be a significant setback for modernist poetry in Australia. "
            "Since the 1970s, however, the Ern Malley poems, though known to be a hoax, became celebrated as a successful example of surrealist poetry in their own right, lauded by poets and critics such as John Ashbery, Kenneth Koch and Robert Hughes. "
            "The poems of Ern Malley are more widely read than those of his creators [...] "
            "Max Harris was a 22-year-old avant-garde poet and critic in Adelaide [...] "
            "The biography stated that Malley had died the year before at the age of 25.  "
            "The entire body of work attributed to Malley—17 poems, none longer than a page and intended to be read in sequence under the title The Darkening Ecliptic—was written in a single afternoon. [...] "
            "lifting words and phrases from the Concise Oxford Dictionary, a Collected Shakespeare, and a Dictionary of Quotations: "
            "\"We opened books at random, choosing a word or phrase haphazardly. We made lists of these and wove them in nonsensical sentences. "
            "We misquoted and made false allusions. We deliberately perpetrated bad verse, and selected awkward rhymes from a Ripman's Rhyming Dictionary.\" [...] "
            "After his mother's death in August 1933, Ern Malley left school to work as an auto mechanic. [...] "
            "worked as an insurance salesman [...] "
            "The Autumn 1944 edition of Angry Penguins appeared in June 1944 owing to wartime printing delays. [...] "
            "A week later, on 25 June 1944, The Sun disclosed that James McAuley and Harold Stewart were the authors of the poems [...] "
            "The South Australian police prosecuted Harris for publishing immoral and obscene material. "
            "The only prosecution witness was a police detective, whose evidence included the statement 'I don't know what \"incestuous\" means, but I think there is a suggestion of indecency about it'. "
            "Despite this, and several distinguished expert witnesses arguing for Harris, he was found guilty and fined £5.",
            nome="Ern Malley")],
    },
    # 11 o romance sem a letra e
    {
        "temas_secundarios": ["estruturas_linguisticas", "segunda_guerra"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "Georges Perec escreveu um romance de 300 páginas sem nenhuma letra \"e\". Sem ela, o órfão do Holocausto não podia escrever \"pai\", \"mãe\" nem o próprio nome em francês. A tradução brasileira também não usa o \"e\".",
        "explicacao": (
            "\"La Disparition\" (\"O Sumiço\"), de 1969, é um lipograma: um texto que se proíbe de usar certa letra. "
            "Perec abriu mão justamente da mais usada do francês, o que elimina palavras como \"je\" (eu), \"et\" (e) e "
            "\"le\" (o). A trama acompanha um grupo à procura de um companheiro desaparecido, Anton Voyl, e o livro "
            "brinca com a própria regra: os personagens acabam descobrindo qual símbolo falta, e quem tenta falar "
            "dele corre risco de morte. Os capítulos são numerados até 26, mas não existe o 5, posição do \"e\" no "
            "alfabeto. Para críticos como Warren Motte, a ausência tem um fundo pessoal. O pai de Perec morreu como soldado na "
            "Segunda Guerra, e a mãe, no Holocausto. Sem o \"e\", o livro não pode conter \"père\", \"mère\", "
            "\"parents\" nem \"famille\", e o autor não pode assinar Georges Perec. Os tradutores aceitaram o desafio. "
            "A versão espanhola não tem a letra \"a\"; a russa não tem \"o\"; a japonesa evita as sílabas com som de "
            "\"i\". A tradução brasileira, \"O Sumiço\", de 2015, também foi feita sem o \"e\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("A_Void",
                "is a 300-page French lipogrammatic novel, put out in 1969 by Georges Perec, written wholly without using the letter e, following Oulipo constraints. [...] "
                "A Void's plot follows a group looking for a missing companion, Anton Vowl. [...] "
                "A Void's protagonists finally work out which symbol is missing, but find it a hazardous topic to discuss, as any who try to bypass this story's constraint risk fatal injury. [...] "
                "Georges Perec's direct kin passed away in World War II: his father as a GI, his mother in the Holocaust. Perec was brought up by his aunt and uncle. "
                "Warren Motte finds the lack of any e in the book as a stand-in for Perec's own notion of loss and sp [...] "
                "if one is willing to reflect on the struggles of a Holocaust orphan trying to make sense out of absence [...] "
                "Perec cannot say the words père [\"father\"], mère [\"mother\"], parents [\"parents\"], famille [\"family\"] in his novel, nor can he write the name Georges Perec. [...] "
                "All translators have asked that the text follow the lipogrammatic constraint of the original work, avoiding the most commonly used letter of the alphabet. "
                "This precludes the use of words normally considered crucial such as je (\"I\"), et (\"and\"), and le (masculine \"the\") in French [...] "
                "The Spanish version contains no a, which is the second most common suffix in the Spanish language (first being e), while the Russian version contains no о. "
                "In Japan, \"A Void\" contains no syllables with the sound \"i\" (い, き, し, etc.) at all.",
                nome="A Void"),
            wiki("La_Disparition_(roman)",
                "La Disparition est un roman en lipogramme de Georges Perec publié en 1969, qui sur près de trois cents pages, ne comporte pas une seule fois la lettre e, pourtant la plus utilisée dans la langue française. "
                "Partant de sa propre contrainte, le roman décrit les événements tragiques qui suivent la disparition d'Anton Voyl. [...] "
                "le fait que le roman comporte 25 chapitres numérotés de 1 à 4 et de 6 à 26 : il manque le cinquième (e est la 5e lettre de l'alphabet du français) [...] "
                "(pt) (Brésil) O Sumiço (Zéfere, 2015) qui ne contient pas de « e »",
                nome="La Disparition (roman)", idioma="fr"),
        ],
    },
    # 12 a autora do Genji não tem nome conhecido
    {
        "temas_secundarios": ["asia_antiga", "sistemas_escrita"],
        "tipos_espanto": ["historia_humana", "misterio_aberto"],
        "gancho": "Não se sabe o nome da autora do \"Genji Monogatari\", um dos primeiros romances do mundo, escrito no Japão por volta do ano 1000. \"Murasaki Shikibu\" é um apelido, e \"Shikibu\" lembra o ministério onde o pai trabalhava.",
        "explicacao": (
            "A autora viveu na corte imperial japonesa no período Heian e escreveu o \"Genji\" entre cerca de 1000 e "
            "1012. Na época, as damas da corte eram conhecidas por nomes ligados ao posto de um parente homem. "
            "\"Shikibu\" remete ao Ministério das Cerimônias, onde o pai dela era funcionário, e \"Murasaki\" talvez "
            "venha da personagem feminina principal do próprio romance. Uma hipótese é que ela fosse Fujiwara no "
            "Kaoruko, dama citada num diário da corte de 1007, mas não há certeza. A biografia também guarda uma "
            "ironia. Mulheres nobres eram mantidas longe do chinês, a língua escrita do governo. O irmão dela "
            "aprendia os clássicos chineses para seguir carreira, e a menina, ouvindo as lições, entendia melhor "
            "que ele os trechos difíceis. O pai, um erudito, lamentava que ela não tivesse nascido homem. Já na "
            "corte, ela fingia não saber chinês, mas deu aulas da língua em segredo à imperatriz Shōshi. Uma rival "
            "passou a chamá-la, com desdém, de \"Dama das Crônicas\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Murasaki_Shikibu",
            "was a Japanese novelist, poet and lady-in-waiting at the Imperial court in the Heian period. "
            "She was best known as the author of The Tale of Genji, widely considered to be one of the world's first novels, written in Japanese between about 1000 and 1012. "
            "Murasaki Shikibu is a descriptive name; her personal name is unknown, but she may have been Fujiwara no Kaoruko (藤原香子), who was mentioned in a 1007 court diary as an imperial lady-in-waiting. "
            "Heian women were traditionally excluded from learning Chinese, the written language of government [...] "
            "A court lady, as well as being known by the title of her own position, if any, took a name referring to the rank or title of a male relative. "
            "Thus \"Shikibu\" is not a modern surname, but refers to Shikibu-shō, the Ministry of Ceremonials where Murasaki's father was a functionary. "
            "\"Murasaki\", an additional name possibly derived from the color violet associated with wisteria, the meaning of the word fuji (an element of her clan name), may hav [...] "
            "e to the name she herself had given to the main female character in \"Genji\". [...] "
            "Chinese was taught to Murasaki's brother as preparation for a career in government, and during her childhood, living in her father's household, she learned and became proficient in classical Chinese. "
            "In her diary she wrote, \"When my brother ... was a young boy learning the Chinese classics, I was in the habit of listening to him and I became unusually proficient at understanding those passages that he found too difficult to understand and memorize. "
            "Father, a most learned man, was always regretting the fact: 'Just my luck,' he would say, 'What a pity she was not born a man!'\" [...] "
            "Murasaki pretended to not know the language, regarding it as pretentious and affected. [...] "
            "Murasaki taught Chinese to Shōshi who was interested in Chinese art and Juyi's ballads. Upon becoming Empress [...] "
            "Murasaki, who was reticent about her Chinese education, held the lessons between the two women in secret [...] "
            "A lady-in-waiting who disliked Murasaki accused her of flaunting her knowledge of Chinese and began calling her \"The Lady of the Chronicles\"",
            nome="Murasaki Shikibu")],
    },
    # 13 George Smith e o dilúvio de Gilgamesh
    {
        "temas_secundarios": ["primeiras_civilizacoes", "decifracao"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Ex-aprendiz de gravador de cédulas, George Smith estudava cuneiforme no almoço. Em 1872, leu numa tabuinha um relato do Grande Dilúvio, parte da Epopeia de Gilgamesh. Segundo colegas, começou a tirar a roupa de emoção.",
        "explicacao": (
            "George Smith vinha de uma família operária e teve pouca escola formal. Aos catorze anos, virou aprendiz de "
            "gravação de cédulas numa editora de Londres. Fascinado pela Assíria, passava o horário de almoço no "
            "Museu Britânico estudando publicações sobre as tabuinhas de argila escavadas perto de Mosul, no "
            "atual Iraque. O talento chamou a atenção dos especialistas, e em 1870 ele já era assistente sênior de "
            "assiriologia do museu. Em 1872, "
            "traduziu um relato caldeu do Grande Dilúvio, hoje conhecido como a décima primeira tabuinha da Epopeia de "
            "Gilgamesh, uma das obras literárias mais antigas que se conhecem. Segundo relatos de colegas da sala "
            "de leitura, no dia em que entendeu o que estava lendo, ele começou a tirar peças de roupa e a correr "
            "pela sala gritando de alegria. Na apresentação pública, em dezembro, estava na plateia o "
            "primeiro-ministro, William Gladstone. O jornal The Daily Telegraph pagou então uma expedição de Smith "
            "a Nínive para procurar os pedaços que faltavam da história, e ele achou parte das tabuinhas perdidas. "
            "Smith morreu em 1876, de disenteria, durante uma nova expedição."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("George_Smith_(Assyriologist)",
            "was a pioneering English Assyriologist who first discovered and translated the Epic of Gilgamesh, one of the oldest-known written works of literature. [...] "
            "As the son of a working-class family in Victorian England, Smith was limited in his ability to acquire a formal education. "
            "At age fourteen, he was apprenticed to the London-based publishing house of Bradbury and Evans to learn banknote engraving, at which he excelled. [...] "
            "Smith was appointed Senior Assistant in the Assyriology Department early in 1870. [...] "
            "he spent his lunch hours at the British Museum, studying publications on the cuneiform tablets that had been unearthed near Mosul in present-day Iraq [...] "
            "In 1872, Smith achieved worldwide fame by his translation of the Chaldaean account of the Great Flood, which he read before the Society of Biblical Archaeology on 3 December. "
            "The audience included the sitting prime minister, William Ewart Gladstone. "
            "According to the accounts of his coworkers in the reading room, on the day of the discovery, when Smith realized what he was reading he \"began to remove articles of his clothing\" and run around the room shouting in delight. "
            "This work is better known today as the eleventh tablet of the Epic of Gilgamesh, one of the oldest known works of literature [...] "
            "The following January, Edwin Arnold, the editor of The Daily Telegraph, arranged for Smith to go to Nineveh at the expense of that newspaper and carry out excavations with a view to finding the missing fragments of the Flood story. "
            "This journey resulted not only in the discovery of some missing tablets [...] "
            "In March 1876, the trustees of the British Museum sent Smith once more to excavate the rest of the Library of Ashurbanipal. [...] "
            "he fell ill with dysentery. He died in Aleppo on 19 August.",
            nome="George Smith (Assyriologist)")],
    },
    # 14 a madeleine de Proust já foi torrada
    {
        "temas_secundarios": ["memoria", "historia_pratos"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "A famosa madeleine molhada no chá, de Proust, começou como torrada nos rascunhos e depois foi biscoito duro. E o livro foi recusado por editoras: um dos que o rejeitaram, André Gide, depois pediu desculpas.",
        "explicacao": (
            "No primeiro volume de \"Em Busca do Tempo Perdido\", o narrador prova um pedaço de madeleine molhado "
            "no chá, e o gosto devolve de uma vez as lembranças da infância em Combray, quando a tia Léonie lhe "
            "dava o bolinho aos domingos. A cena virou símbolo da memória involuntária, e \"madeleine de Proust\" "
            "ainda é expressão francesa para um estímulo dos sentidos que dispara uma lembrança. Os manuscritos "
            "mostram que o doce mudou no caminho. Num rascunho de 1907, publicado por uma editora de Paris em "
            "2015, era pão torrado com mel; no seguinte, uma biscotte, espécie de torrada dura; só na terceira "
            "versão surgiu a madeleine macia. O próprio livro teve começo difícil. Várias editoras recusaram o "
            "primeiro volume, entre elas a Nouvelle Revue Française, onde André Gide deu parecer contra depois de "
            "folhear o manuscrito. Proust pagou do próprio bolso a edição de 1913 pela Grasset. No começo de 1914, "
            "Gide escreveu a ele dizendo que a recusa ficaria como o erro mais grave da revista e um dos maiores "
            "arrependimentos de sua vida."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            fonte("https://www.thelocal.fr/20151028/prousts-madeleine-cakes-began-life-as-toast/", "Proust's Madeleine cakes started life as toast (The Local / AFP)", "en",
                "A first draft of Proust's huge novel dating from 1907 had the author reminiscing not about madeleines -- a sensory trigger for a childhood memory about his aunt -- but about toasted bread mixed with honey. "
                "A second draft, the manuscripts showed, had the evocative edible as a biscotto, a hard biscuit. "
                "It was only in the third draft that Proust wrote that he had bitten into a soft little madeleine. "
                "[...] Published: 21 Oct, 2015 [...] "
                "A Paris publishing house, Saint-Peres, showed the shifting food reference in three handwritten manuscripts by Proust that it will print into a special three-part notebook set for retail. [...] "
                "the French today still use the expression \"Proust's madeleine\" to refer to a sensory cue that triggers a memory."),
            fonte("https://www.nybooks.com/online/2013/02/22/sweet-troubles-proust/", "Sweet Troubles: Proust (The New York Review of Books)", "en",
                "What appears in a 1910 draft of Swann’s Way is the banal word “biscottes,” easy to spot in the manuscript."),
            wiki("In_Search_of_Lost_Time",
                "Swann's Way (Du côté de chez Swann, also translated as The Way by Swann's and The Swann Way), published in 1913, was rejected by a number of publishers, including Fasquelle, Ollendorff, and the Nouvelle Revue Française (NRF). "
                "André Gide was famously given the manuscript to read to advise the NRF on publication and, leafing through the seemingly endless collection of memories and philosophising or melancholic episodes, came across a few minor syntactic errors, which made him decide to turn the work down in his audit. "
                "Proust eventually arranged with the publisher Grasset to pay the cost of publication himself. [...] "
                "In early 1914 Gide, who had been involved in the NRF's rejection of the book, wrote to Proust to apologise and to offer congratulations on the novel: [...] "
                "The rejection of this book will remain the most serious mistake ever made by the NRF and, since I bear the shame of being very much responsible for it, one of the most stinging and remorseful regrets of my life [...] "
                "the taste of a madeleine cake dipped in tea inspires a nostalgic incident of involuntary memory. "
                "He remembers having a similar snack as a child with his invalid aunt Léonie, and it leads to more memories of Combray. [...] "
                "The taste was that of the little piece of madeleine which on Sunday mornings at Combray (because on those mornings I did not go out before mass), when I went to say good morning to her in her bedroom, my aunt Léonie used to give me, dipping it first in her own cup of tea or tisane.",
                nome="In Search of Lost Time"),
        ],
    },
    # 15 o poema perdido de Safo e o papiro suspeito
    {
        "temas_secundarios": ["grecia_antiga", "crimes_arte"],
        "tipos_espanto": ["misterio_aberto", "historia_humana"],
        "gancho": "Dos cerca de 10 mil versos de Safo, sobraram uns 650. Em 2014, reapareceu um poema dela perdido desde a Antiguidade. Mas ninguém conseguiu provar de onde veio o papiro, e em 2022 ele foi recolhido pela polícia.",
        "explicacao": (
            "Safo, poeta grega de Lesbos que viveu entre cerca de 630 e 570 a.C., teria escrito uns 10 mil "
            "versos, mas quase toda a sua obra se perdeu: um só poema chegou completo, e muitos fragmentos "
            "guardam uma única palavra. Em 2014, o papirólogo Dirk Obbink, que chefiava um projeto de papiros em Oxford, e colegas publicaram "
            "fragmentos com nove poemas dela, três deles desconhecidos, a maior ampliação da obra conhecida de "
            "Safo em 92 anos. O destaque era o \"Poema dos Irmãos\", com 20 versos que citam pela primeira vez, na "
            "obra dela, os nomes de dois irmãos. Logo surgiram perguntas sobre a origem do papiro, que pertencia a "
            "um colecionador anônimo. Vieram versões contraditórias: um oficial alemão, um papiro reaproveitado "
            "em cartonagem de múmia, a coleção de um professor americano vendida pela casa Christie's. Nenhuma foi "
            "comprovada, e há pesquisadores que suspeitam de um papiro saqueado e contrabandeado do Egito. O papiro foi oferecido "
            "à venda em 2013 e 2015, não achou comprador e ficou num depósito da Christie's até ser levado pela "
            "polícia em 2022. Fragmentos ligados a ele foram devolvidos ao Egito em 2020."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Brothers_Poem",
            "is a series of lines of verse attributed to the archaic Greek poet Sappho (c. 630 – c. 570 BC), which had been lost since antiquity until being rediscovered in 2014. [...] "
            "It mentions two of her brothers, Charaxos and Larichos, the only known mention of their names in Sappho's writings [...] "
            "Sappho is thought to have written around 10,000 lines of poetry, of which only around 650 survive. "
            "Only one poem, the Ode to Aphrodite, is known to be complete; many preserve only a single word.  "
            "In 2014, Dirk Obbink, Simon Burris, and Jeffrey Fish published five fragments of papyrus, containing nine separate poems by Sappho. "
            "Three were previously unknown, and the find amounted to the largest expansion of the surviving corpus of Sappho's work for 92 years. [...] "
            "P. Sapph. Obbink preserves 20 lines of the Brothers Poem [...] "
            "Soon after the discovery of P. Sapph. Obbink was made public in January 2014, scholars began to raise questions about its provenance.  "
            "The initial version of Obbink's article announcing the discovery said that the papyrus was in a private collection, but did not discuss its origin or ownership history [...] "
            "Since then, several contradictory claims have been made about the history of P. Sapph. Obbink. [...] "
            "Bettany Hughes reported in the Sunday Times that the papyrus was originally owned by a German officer, while Obbink wrote in the Times Literary Supplement that it was found in mummy cartonnage. [...] "
            "He claimed that the papyrus derived from the collection of David Moore Robinson, who had purchased it in 1954 from an Egyptian dealer, Sultan Maguid Sameda, and on his death left it to the University of Mississippi Library.  "
            "Part of the Robinson collection was offered for sale through Christie's in 2011 [...] "
            "It was this anonymous owner who gave Obbink, the head of Oxford University's Oxyrhynchus Papyri project, access to the papyrus and permission to publish it. "
            "However the presence of the papyrus in the 2011 sale is unverifiable. [...] "
            "Theodore Nash argues that \"the convoluted cartonnage narrative was simply a red herring to legitimise a recently looted papyrus\". [...] "
            "Roberta Mazza, who also believes that the papyri were illegally smuggled out of Egypt [...] "
            "In 2013 and in 2015 P. Sapph. Obbink was privately offered for sale through Christie's. "
            "The papyrus was never bought, and remained in storage at Christie's until taken by the police in 2022. "
            "The related Green Collection fragments were returned to Egypt in 2020.",
            nome="Brothers Poem")],
    },
]
