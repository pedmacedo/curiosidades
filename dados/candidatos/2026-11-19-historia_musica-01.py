LOTE = "2026-11-19-historia_musica-01"
AREA = "artes"
TEMA = "historia_musica"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


BL_TURING = "https://blogs.bl.uk/sound-and-vision/2016/09/restoring-the-first-recording-of-computer-music.html"

CANDIDATOS = [
    # 1 o hino hurrita de Ugarit e as cinco leituras rivais
    {
        "temas_secundarios": ["primeiras_civilizacoes", "decifracao"],
        "tipos_espanto": ["misterio_aberto", "escala_absurda"],
        "gancho": "A obra musical escrita quase completa mais antiga que se conhece é um hino de cerca de 1400 a.C., em tabuleta de argila achada na Síria. A escrita é legível, mas há ao menos cinco versões rivais de como ele soava.",
        "explicacao": (
            "Nos anos 1950, escavações no palácio real de Ugarit, cidade antiga no norte da Síria, revelaram "
            "fragmentos de tabuletas de argila com cerca de 36 hinos em escrita cuneiforme, numa camada do "
            "século XIV a.C. Só um deles, um hino a Nikkal, deusa dos pomares, chegou até nós quase inteiro, e "
            "por isso é considerado a obra musical notada substancialmente completa mais antiga do mundo. Ele "
            "antecede em cerca de mil anos outras músicas antigas conhecidas, como o Epitáfio de Seikilos. A "
            "tabuleta traz a letra em hurrita e, abaixo, instruções em acádio para um cantor acompanhado por um "
            "instrumento de nove cordas, muito provavelmente uma lira: nomes de intervalos seguidos de números. "
            "O nó está aí. As diferenças entre as transcrições dependem de como se interpretam esses pares de "
            "sinais e de como eles se ligam ao texto. As primeiras reconstruções leram a escala de cabeça para "
            "baixo, com as notas mais agudas virando as mais graves. Hoje há pelo menos cinco decifrações "
            "rivais, que produzem resultados completamente diferentes, embora a escrita em si seja bem "
            "compreendida e quase sem ambiguidade. A primeira execução moderna foi em 1974, e a tabuleta "
            "pertence ao Museu Nacional de Damasco."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Hurrian_songs",
            "The Hurrian songs (or Hurrian Hymns) are a collection of music written in cuneiform on clay tablets excavated from the ancient city of Ugarit, a headland in northern Syria, which date to approximately 1400 BCE. "
            "One of these tablets, which is nearly complete, contains the Hurrian Hymn to Nikkal [...] "
            "making it the oldest surviving substantially complete work of notated music in the world. [...] "
            "The complete song is one of about 36 such hymns in cuneiform writing, found on fragments of clay tablets excavated in the 1950s from the Royal Palace at Ugarit (present-day Ras Shamra, Syria), in a stratum dating from the fourteenth century BCE, but is the only one surviving in substantially complete form. [...] "
            "Tablet h.6 contains the lyrics for a hymn to Nikkal, an Ancient Near Eastern goddess of orchards, and instructions for a singer accompanied by a nine-stringed sammûm, a type of harp or, much more likely, a lyre. "
            "The hymn was given its first modern performance in 1974 [...] "
            "The Hurrian hymn pre-dates several other surviving early works of music (e.g., the Seikilos epitaph and the Delphic Hymns) by a millennium [...] "
            "The first reconstructions interpreted the musical scale upside down, with the highest tones incorrectly becoming the lowest. [...] "
            "this is only one of at least five \"rival decipherments of the notation, each yielding entirely different results\". "
            "These reconstructions (not decipherments in the correct sense of the word, because the script is well understood and mostly unambiguous) [...] "
            "The tablet is in the collection of the National Museum of Damascus. [...] "
            "Below this is found the Akkadian musical instructions, consisting of interval names followed by number signs. "
            "Differences in transcriptions hinge on interpretation of the meaning of these paired signs, and the relationship to the hymn text.",
            nome="Hurrian songs")],
    },
    # 2 Guido d'Arezzo, o dó-ré-mi e o treino que caiu de 10 anos para 1 ou 2
    {
        "temas_secundarios": ["europa_medieval", "aprendizagem_inteligencia"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "Os nomes dó, ré, mi, fá, sol, lá vêm das sílabas iniciais de versos de um hino a São João. No século XI, o monge Guido d'Arezzo usou o truque para ensinar canto, e o treino de um cantor caiu de 10 anos para um ou dois.",
        "explicacao": (
            "Guido, monge beneditino italiano nascido entre 990 e 999, é tido como inventor, ou para alguns "
            "aperfeiçoador, da pauta musical moderna. Na abadia de Pomposa, ele reclamava do tempo enorme que os "
            "cantores gastavam decorando melodias e propôs um sistema que dispensaria a memorização. Os métodos "
            "novos despertaram o ressentimento dos colegas, e ele se mudou em 1025 para Arezzo, onde passou a "
            "formar os cantores da catedral. Ali, o treino padrão de dez anos para um cantor caiu para um ou "
            "dois. Um dos recursos era um mnemônico. No hino latino \"Ut queant laxis\", em honra de São João "
            "Batista, cada meio verso da primeira estrofe começa uma nota acima do anterior, e as sílabas "
            "iniciais, ut, re, mi, fa, sol, la, viraram os nomes das seis notas. O \"ut\" foi trocado na Itália, "
            "nos anos 1600, pelo \"dó\", de som mais aberto. Como o sistema de Guido tinha só seis notas, a "
            "sétima ganhou depois o nome \"si\", tirado de \"Sancte Iohannes\", as palavras do último verso. A "
            "fama do método chegou ao papa João XIX, que chamou Guido a Roma para explicá-lo ao clero."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Guido_of_Arezzo",
                "A monk from the Order of Saint Benedict, he is regarded as the inventor—or by some, developer—of the modern staff notation [...] "
                "By around 1013 he began teaching at Pomposa Abbey, but his antiphonary Prologus in antiphonarium and novel teaching methods based on staff notation brought considerable resentment from his colleagues. "
                "He thus moved to Arezzo in 1025 and under the patronage of Bishop Tedald of Arezzo he taught singers at the Arezzo Cathedral. [...] "
                "Interested in his innovations, Pope John XIX called him to Rome. After arriving and beginning to explain his methods to the clergy [...] "
                "Guido was born sometime between 990 and 999. [...] "
                "In the prologue to the antiphonary, Guido expressed his frustration with the large amount of time singers spent to memorize music. "
                "The system, he explained, would prevent the need for memorization [...] "
                "Guido lessened the standard 10-year training for the ideal cantor to only one or two years.",
                nome="Guido of Arezzo"),
            wiki("Ut_queant_laxis",
                "is a Latin hymn in honor of John the Baptist [...] "
                "the first six musical phrases of each stanza begin on a successively higher notes of the hexachord, giving ut–re–mi–fa–so–la; though ut is replaced by do in modern solfège. "
                "The naming of the notes of the hexachord by the first syllable of each hemistich (half line of verse) of the first verse is usually attributed to Guido of Arezzo. [...] "
                "it was originally called \"si\" from \"Sancte Ioannes\" (Johannes).",
                nome="Ut queant laxis"),
            wiki("Solf%C3%A8ge",
                "\"Ut\" was changed in the 1600s in Italy to the open syllable \"Do\". "
                "Guido's system had only six notes, but \"si\" was added later as the seventh note of the diatonic scale.",
                nome="Solfège"),
        ],
    },
    # 3 o trítono "proibido pela Igreja"
    {
        "temas_secundarios": ["musica_ciencia", "europa_medieval"],
        "tipos_espanto": ["mito_desmentido"],
        "gancho": "Conta-se que a Igreja medieval proibia o trítono, o \"intervalo do diabo\", e punia quem o cantasse. Histórias de punição são provavelmente fantasia, e não se conhece nenhum registro medieval do apelido.",
        "explicacao": (
            "O trítono é o intervalo de três tons inteiros, como de fá a si. Até o fim do Renascimento, a maioria "
            "dos teóricos o considerava instável e o rejeitava como consonância, e evitá-lo por razões musicais é "
            "prática antiga, que remonta ao organum paralelo do tratado medieval Musica Enchiriadis. Daí nasceu a lenda de que "
            "a Igreja o teria banido, chegando a excomungar cantores. Segundo o artigo da Wikipedia sobre o "
            "intervalo, essas histórias de punição são provavelmente fantasiosas. O próprio apelido \"diabolus "
            "in musica\" tem história curiosa. Os registros conhecidos vêm do século XVIII: Andreas Werckmeister "
            "o cita em 1702, Johann Joseph Fux em 1725 e Johann Mattheson em 1739, sempre atribuindo a expressão "
            "aos antigos. Mas não há citações conhecidas do termo na Idade Média, como se costuma afirmar. E a "
            "frase original encontrada, \"mi contra fa est diabolus in musica\", se referia à segunda menor, não "
            "ao trítono; Werckmeister a aplicava também ao choque entre notas como fá e fá sustenido. Há quem "
            "pense diferente: o musicólogo Denis Arnold sugere que o apelido já surgiu na própria música "
            "medieval, na época de Guido d'Arezzo. De todo modo, foi a associação simbólica com o diabo que "
            "levou a cultura ocidental a usar o trítono para sugerir o mal na música."
        ),
        "nivel": 2, "nota_surpresa": 3, "confianca": "consenso_parcial",
        "fontes": [wiki("Tritone",
            "a tritone is a musical interval spanning three whole tones. For instance, the interval from F to the B above it (in short, F–B) is a tritone [...] "
            "From then until the end of the Renaissance, the tritone was regarded as an unstable interval and rejected as a consonance by most theorists. [...] "
            "being that the original found example of the term \"diabolus en musica\" is \"Mi Contra Fa est diabolus en musica\" (\"Mi against Fa is the devil in music\"), referring to the minor second. "
            "Andreas Werckmeister cites this term in 1702 as being used by \"the old authorities\" for both the tritone and for the clash between chromatically related tones such as F♮ and F♯ [...] "
            "Johann Joseph Fux cites the phrase in his seminal 1725 work Gradus ad Parnassum [...] "
            "and Johann Mattheson, in 1739, writes that the \"older singers with solmization called this pleasant interval 'mi contra fa' or 'the devil in music'.\" "
            "Although the latter two of these authors cite the association with the devil as from the past, there are no known citations of this term from the Middle Ages, as is commonly asserted. "
            "However Denis Arnold, in the New Oxford Companion to Music, suggests that the nickname was already applied early in the medieval music itself [...] "
            "when Guido of Arezzo developed his system of hexachords [...] "
            "That original symbolic association with the devil and its avoidance led to Western cultural convention seeing the tritone as suggesting evil in music. "
            "However, stories that singers were excommunicated or otherwise punished by the Church for invoking this interval are likely fanciful. "
            "At any rate, avoidance of the interval for musical reasons has a long history, stretching back to the parallel organum of the Musica Enchiriadis.",
            nome="Tritone")],
    },
    # 4 Vivaldi esquecido e a volta graças a uma falsificação
    {
        "temas_secundarios": ["crimes_arte", "personagens_esquecidos"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Vivaldi morreu pobre e foi quase esquecido por dois séculos: nem \"As Quatro Estações\" eram conhecidas na edição original. A volta dele deve muito a uma falsificação e a volumes achados num mosteiro em 1926.",
        "explicacao": (
            "Em vida, Vivaldi foi popular em muitos países da Europa, mas acabou indo para Viena atrás do apoio "
            "do imperador Carlos VI, que morreu logo depois da sua chegada, e o compositor morreu na pobreza "
            "menos de um ano mais tarde. Depois do Barroco, seus concertos publicados ficaram praticamente "
            "ignorados, e As Quatro Estações, hoje a obra mais famosa dele, eram desconhecidas na edição "
            "original durante os períodos clássico e romântico. A virada veio no começo do século XX, por um "
            "caminho torto. O violinista Fritz Kreisler fez passar por obra original de Vivaldi um Concerto em "
            "Dó que ele mesmo tinha escrito no estilo do italiano, e a peça levou o estudioso francês Marc "
            "Pincherle a pesquisar a fundo a obra de Vivaldi. Kreisler só revelou a autoria desses pastiches, "
            "atribuídas também a Tartini e Pugnani, em 1935. Quando críticos reclamaram, respondeu que eles "
            "mesmos já as tinham julgado valiosas: \"O nome muda, o valor fica\". Em 1926, num mosteiro do "
            "Piemonte, pesquisadores acharam volumes encadernados de Vivaldi que se julgavam perdidos nas "
            "Guerras Napoleônicas, com 300 concertos e 19 óperas, entre outras obras. Muitos manuscritos "
            "redescobertos foram comprados pela Biblioteca Nacional Universitária de Turim com o patrocínio de "
            "dois empresários da cidade, Roberto Foa e Filippo Giordano, em memória dos filhos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Antonio_Vivaldi",
                "After meeting the Emperor Charles VI, he moved to Vienna, hoping for royal support, but the emperor died soon after his arrival, and Vivaldi died in poverty less than a year later. "
                "After almost two centuries of decline, Vivaldi's musical reputation underwent a revival in the early 20th century [...] "
                "During his lifetime, Vivaldi was popular in many countries throughout Europe, including France, but after his death his popularity dwindled. "
                "After the end of the Baroque period, Vivaldi's published concerti became relatively unknown, and were largely ignored. "
                "Even his most famous work, The Four Seasons, was unknown in its original edition during the Classical and Romantic periods. [...] "
                "In the early 20th century, Fritz Kreisler's Concerto in C, in the Style of Vivaldi (which he passed off as an original Vivaldi work) helped revive Vivaldi's reputation. "
                "Kreisler's concerto in C spurred the French scholar Marc Pincherle to begin an academic study of Vivaldi's oeuvre. "
                "Many Vivaldi manuscripts were rediscovered, and were acquired by the Turin National University Library as a result of the generous sponsorship of Turinese businessmen Roberto Foa and Filippo Giordano, in memory of their sons. [...] "
                "In 1926, in a monastery in Piedmont, researchers discovered fourteen bound volumes of Vivaldi's work (later discovered to be fifteen) that were previously thought to have been lost during the Napoleonic Wars. [...] "
                "The volumes contained 300 concertos, 19 operas and over 100 vocal-instrumental works.",
                nome="Antonio Vivaldi"),
            wiki("Fritz_Kreisler",
                "Some of Kreisler's compositions were pastiches ostensibly in the style of other composers. "
                "They were originally ascribed to earlier composers, such as Gaetano Pugnani, Giuseppe Tartini and Antonio Vivaldi, and then,  in 1935, Kreisler revealed that it was he who wrote the pieces. "
                "When critics complained, Kreisler replied that they had already deemed the compositions worthy: \"The name changes, the value remains\", he said.",
                nome="Fritz Kreisler"),
        ],
    },
    # 5 o crânio roubado de Haydn e o túmulo com dois crânios
    {
        "temas_secundarios": ["historia_medicina", "crimes_arte"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Dias depois do enterro de Haydn, em 1809, dois adeptos da frenologia subornaram o coveiro e levaram a cabeça do compositor. O crânio só se juntou ao corpo em 1954, e o túmulo dele guarda hoje dois crânios.",
        "explicacao": (
            "Haydn morreu em Viena em 31 de maio de 1809, aos 77 anos, com a cidade ocupada pelas tropas de "
            "Napoleão, e teve um funeral simples. Logo depois, Joseph Carl Rosenbaum, ex-secretário da família "
            "Esterházy, para quem Haydn trabalhara, e Johann Nepomuk Peter, diretor de uma prisão, pagaram ao "
            "coveiro para cortar e roubar a cabeça. Os dois admiravam Franz Joseph Gall e a frenologia, teoria "
            "hoje desacreditada que tentava ligar capacidades mentais à anatomia do crânio, e que se interessava "
            "especialmente pelos gênios. Depois do exame, Peter concluiu que a \"protuberância da música\" era "
            "de fato bem desenvolvida. Em 1820, o príncipe Nikolaus Esterházy II mandou exumar o corpo para "
            "levá-lo a Eisenstadt e achou uma peruca sobre o pescoço cortado. Os ladrões escaparam com várias "
            "manobras, incluindo crânios falsos. Durante uma busca na casa de Rosenbaum, o crânio estava "
            "escondido num colchão de palha, e a mulher dele se deitou na cama dizendo estar menstruada, o que "
            "manteve os investigadores longe. Por fim, ele entregou ao príncipe um outro crânio. O verdadeiro "
            "passou de mão em mão até chegar, em 1895, à Sociedade dos Amigos da Música de Viena. Só em 1954 ele "
            "foi levado ao túmulo na Bergkirche de Eisenstadt, encerrando um enterro de 145 anos. O crânio "
            "substituto não foi retirado."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Haydn%27s_head",
                "The skull of composer Joseph Haydn was stolen shortly after his death in 1809; the perpetrators were interested in examining it for purposes of phrenology. [...] "
                "only in 1954 was it reunified for burial with the rest of Haydn's remains. [...] "
                "Haydn died in Vienna, aged 77, on 31 May 1809, after a long illness. As Austria was at war and Vienna occupied by Napoleon's troops,  a rather simple funeral was held [...] "
                "Following the burial, two men conspired to bribe the gravedigger and thereby sever and steal the dead composer's head. "
                "These were Joseph Carl Rosenbaum, a former secretary of the Esterházy family (Haydn's employers), and Johann Nepomuk Peter, governor of the provincial prison of Lower Austria. [...] "
                "Peter and Rosenbaum's motivation was an interest in phrenology, a now-discredited scientific movement that attempted to associate mental capacities with aspects of cranial anatomy; Peter and Rosenbaum were acquainted with and admired the work of Franz Joseph Gall, a leading phrenologist. "
                "Of particular interest to phrenology was the anatomy of individuals held to have exhibited great genius during their lifetime. [...] "
                "Peter concluded that \"the bump of music\" in Haydn's skull was indeed \"fully developed\". [...] "
                "In 1820, Haydn's old patron Prince Nikolaus Esterházy II [...] "
                "having Haydn's remains transferred from Gumpendorf to the family seat in Eisenstadt. "
                "Upon exhumation, they found a body with a wig above its severed neck. Haydn's head was missing. [...] "
                "However, through a series of devious maneuvers (blaming a deceased doctor, two fake skulls; one rejected) Peter and Rosenbaum managed to maintain possession of the skull. "
                "Rosenbaum hid the skull in a straw mattress. "
                "During the search of Rosenbaum's house, his wife Therese lay on the bed and claimed to be menstruating—with the result that the searchers did not go near the mattress. "
                "Eventually Rosenbaum gave Prince Esterházy a different skull. [...] "
                "After Rosenbaum's death in 1829, the skull passed from hand to hand. [...] "
                "Carl von Rokitansky who in 1895 gave it to the Vienna Gesellschaft der Musikfreunde (Society of the Friends of Music). [...] "
                "it was only in 1954 that the skull could be transferred, in a splendid ceremony, from the Gesellschaft der Musikfreunde to this tomb, thus completing the 145-year-long burial process. "
                "When the composer's skull was finally restored to the remainder of his skeleton, the substitute skull was not removed. "
                "Thus Haydn's tomb now contains two skulls.",
                nome="Haydn's head"),
            wiki("Bergkirche_(Eisenstadt)",
                "A side chapel is dominated by a large marble sarcophagus, the tomb of the composer Joseph Haydn [...] "
                "The remains of most of Haydn's body have rested here since 1932; the skull was added (with due pomp and ceremony) only in 1954",
                nome="Bergkirche (Eisenstadt)"),
        ],
    },
    # 6 a cantata perdida de Mozart e Salieri
    {
        "temas_secundarios": ["personagens_esquecidos", "cinema_fotografia"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Em 2015, um musicólogo achou num arquivo de Praga uma cantata perdida composta em parceria por Mozart, Salieri e um terceiro autor. É uma pista de que os dois \"rivais\" podiam ter uma relação amigável.",
        "explicacao": (
            "A peça, \"Per la ricuperata salute di Ofelia\" (pela saúde recuperada de Ofélia), é de 1785 e "
            "celebrava a volta da soprano Nancy Storace, que tinha perdido a voz temporariamente e levou três "
            "meses para se recuperar. Ela interpretava obras dos dois compositores e seria a primeira Susanna de "
            "\"As Bodas de Fígaro\". O libreto é de Lorenzo Da Ponte, poeta da corte de Viena. A cantata, para "
            "soprano e fortepiano, dura uns quatro minutos e tem três partes, cada uma de um compositor: Salieri, "
            "Mozart e um certo Cornetti, cuja identidade ainda é especulada. A música era considerada perdida até "
            "novembro de 2015, quando o musicólogo alemão Timo Jouko Herrmann a identificou nos arquivos do Museu "
            "Tcheco da Música, em Praga, enquanto procurava obras de um suposto aluno de Salieri. Os nomes dos "
            "autores apareciam num tipo de código de assinatura comum na época. Para um diretor da Fundação "
            "Mozarteum, a imagem pintada pelo filme \"Amadeus\" é falsa: Salieri não envenenou Mozart, embora os "
            "dois trabalhassem em Viena e fossem concorrentes. O crítico Alex Ross foi menos entusiasmado com a "
            "obra: para ele, a história por trás da música interessa mais do que a própria música."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Per_la_ricuperata_salute_di_Ofelia",
            "Per la ricuperata salute di Ofelia (For the recovered health of Ophelia), K.6 477a, is a solo cantata for soprano and fortepiano composed in 1785 by Antonio Salieri and Wolfgang Amadeus Mozart, and a third, unknown composer, Cornetti, to a libretto written by the Vienna court poet Lorenzo Da Ponte. "
            "It is speculated that \"Cornetti\" may refer to [...] "
            "The music had been considered lost until November 2015, when German musicologist and composer Timo Jouko Herrmann identified the score while searching for music by one of Salieri's ostensible pupils, Antonio Casimir Cartellieri, in the archives of the Czech Museum of Music in Prague. [...] "
            "Conceived, written and composed to celebrate the newly recovered health of Nancy Storace, the Vienna-based, Anglo-Italian soprano destined to become the first Susanna of Figaro, and to welcome her back to the stage after a temporary loss of her singing voice [...] "
            "the short work is compelling evidence of what may indeed have been an amicable and cooperative relationship between Salieri and Mozart. "
            "The brisk, four-minute cantata consists of three parts, each by a different composer. "
            "Madame Storace was known for interpreting works by both Mozart and Salieri, as well as by her brother. [...] "
            "Her recovery took three months. [...] "
            "bearing the names of Mozart and Salieri \"in a kind of signature code that was common at the time,\" [...] "
            "Ulrich Leisinger, Director of the Research Department at the International Mozarteum Foundation, has said: We all know the picture drawn by the movie Amadeus. It is false. "
            "Salieri did not poison Mozart, but they both worked in Vienna and were competitors... [...] "
            "As for the cantata's artistic merits, Alex Ross observed in The New Yorker, ...(T)he story behind the music...holds more interest than the music itself",
            nome="Per la ricuperata salute di Ofelia")],
    },
    # 7 Tchaikovsky e von Meck: 13 anos de mesada e nenhum encontro
    {
        "temas_secundarios": ["personagens_esquecidos", "emocoes"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Por treze anos, a milionária russa Nadejda von Meck sustentou Tchaikovsky com uma mesada generosa, e os dois trocaram mais de 1.200 cartas. A condição dela era que nunca se encontrassem.",
        "explicacao": (
            "Viúva de um engenheiro que ficou milionário construindo ferrovias, von Meck era uma pianista competente e, "
            "após a morte do marido, passou a viver quase reclusa. Começou encomendando peças a Tchaikovsky e "
            "depois lhe deu uma mesada de 6.000 rublos por ano, o bastante para ele largar o posto de professor no "
            "Conservatório de Moscou e se dedicar só a compor. Para comparar, um funcionário público de baixo "
            "escalão sustentava a família com 300 a 400 rublos anuais. Entre 1877 e 1890, os dois trocaram mais de "
            "1.200 cartas, e ele se abriu com ela sobre a vida e o processo criativo como com nenhuma outra pessoa. "
            "Tchaikovsky lhe dedicou a Sinfonia nº 4. Os dois só se viram de longe: em Florença, ele via o cortejo "
            "dela passar todas as manhãs, e uma vez se avistaram na ópera, encontro talvez arranjado por ela. Em "
            "outubro de 1890, von Meck mandou um ano de mesada adiantado, com uma carta que encerrava o "
            "patrocínio, alegando falência. Na época, estava gravemente doente, com tuberculose, e sob pressão dos "
            "filhos, que se incomodavam com a relação. Ela também contratou um jovem Claude Debussy como professor "
            "de música das filhas. Ele quis se casar com uma delas, e a mãe não deu permissão."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Nadezhda_von_Meck",
            "She is best known today for her artistic relationship with Pyotr Ilyich Tchaikovsky, supporting him financially for thirteen years, so that he could devote himself full-time to composition, while stipulating that they were never to meet. "
            "Tchaikovsky dedicated his Symphony No. 4 in F minor to her. [...] "
            "A serious student of music in her youth, Nadezhda became a capable pianist [...] "
            "his investments made him a multi-millionaire. The railway lines for which he was responsible included [...] "
            "After the death of her husband, von Meck took no part in social life, withdrawing into almost complete seclusion. [...] "
            "She hired Claude Debussy as a music tutor for her daughters, and he wanted to marry one of them. She would not give her permission [...] "
            "she commissioned some pieces for violin and piano to be played at her house. [...] "
            "she subsequently provided him with an allowance of 6,000 rubles a year, large enough that he could leave his professorship at the Moscow Conservatory to focus on creative work full-time. "
            "This was a substantial income. A minor government official in those days had to support his family on 300–400 rubles a year. [...] "
            "They carried on a significant correspondence, exchanging over 1,200 letters between 1877 and 1890. "
            "The details they shared were extraordinary for two people who never met. "
            "He was more open to her about much of his life and his creative processes than to any other person. [...] "
            "while staying at her villa in Florence, Tchaikovsky had seen her and her entourage pass by every morning; and they also glimpsed each other once at the opera, but only from a distance. "
            "Alexander Poznansky says of this last encounter: \"It is not clear whether their both being at the theater was wholly accidental or arranged by Mrs. von Meck in order to see him, as seems not unlikely.\" [...] "
            "In October 1890, von Meck sent Tchaikovsky a year's allowance in advance, along with a letter ending her patronage. She claimed bankruptcy. [...] "
            "By 1890, she was gravely ill.  She was in the latter stages of tuberculosis [...] "
            "She was under intense family pressure to end the relationship. Her children were embarrassed by her closeness with Tchaikovsky.",
            nome="Nadezhda von Meck")],
    },
    # 8 a harmônica de vidro de Franklin e o boato da loucura
    {
        "temas_secundarios": ["invencoes", "historia_medicina"],
        "tipos_espanto": ["conexao_inesperada", "mito_desmentido"],
        "gancho": "Benjamin Franklin inventou em 1761 um instrumento de tigelas de vidro girando num eixo, para o qual Mozart compôs. Em terras alemãs, correu o boato de que ele enlouquecia músicos e ouvintes.",
        "explicacao": (
            "Franklin teve a ideia depois de ver, em 1761, taças de vinho com água sendo tocadas em Cambridge, na "
            "Inglaterra. Com um vidreiro de Londres, criou um arranjo radicalmente novo: na versão dele, 37 "
            "tigelas ficavam enfileiradas na horizontal num eixo de ferro, girado por um pedal, e o som saía por "
            "atrito. Chamou a invenção de armonica, do italiano armonia, e descreveu seus "
            "tons como \"incomparavelmente doces\". O instrumento fez sucesso: mais de cem compositores escreveram "
            "para ele, entre eles Mozart, em 1791, e Beethoven o usou numa obra de 1814. Franz Anton Mesmer, o do "
            "mesmerismo, fazia dele parte central do seu método. A popularidade, porém, não passou muito do "
            "século XVIII. Uma explicação é o volume baixo, fácil de abafar por outros instrumentos. Outra seriam "
            "boatos de que tocá-lo enlouquecia músicos e plateias, ao que parece restritos à Alemanha, talvez só a "
            "Viena. Um musicólogo alemão chegou a escrever que ele afundava o tocador numa melancolia que era um "
            "método de \"lenta autoaniquilação\". Uma versão moderna diz que os músicos se envenenavam com o "
            "chumbo do vidro, mas não há base científica conhecida para isso. Na época, o chumbo vinha em "
            "quantidades bem maiores de outras fontes, como remédios e utensílios de cozinha."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Glass_harmonica",
            "a type of musical instrument that uses a series of glass bowls or goblets graduated in size to produce musical tones by means of friction [...] "
            "It was invented in 1761 by Benjamin Franklin and produces sound that is ethereal and haunting [...] "
            "When Benjamin Franklin invented his mechanical version of the instrument in 1761, he called it the armonica, based on the Italian word armonia, which means \"harmony\". [...] "
            "Benjamin Franklin invented a radically new arrangement of the glasses in 1761 after seeing water-filled wine glasses played by Edward Delaval at Cambridge in England in May 1761. "
            "Franklin worked with London glassblower Charles James to build one [...] "
            "\"The advantages of this instrument are, that its tones are incomparably sweet beyond those of any other [...] "
            "In Franklin's treadle-operated version, 37 bowls were mounted horizontally on an iron spindle. "
            "The whole spindle turned by means of a foot pedal. [...] "
            "Franz Mesmer also played the armonica and used it as an integral part of his Mesmerism. [...] "
            "and more than 100 others composed works for the glass harmonica [...] "
            "Wolfgang Amadeus Mozart wrote his 1791 K. 617 and K.356 (K.617a) for the glass harmonica. "
            "Ludwig van Beethoven used the instrument in his 1814 melodrama Leonore Prohaska. [...] "
            "The instrument's popularity did not last far beyond the 18th century. "
            "This may have been due to the inability to amplify the volume so as not to be drowned out by other instruments. "
            "Some claim this was due to strange rumors that using the instrument caused both musicians and their listeners to go mad. "
            "It is a matter of conjecture how pervasive that belief was; all the commonly cited examples of this rumor seem to be German, if not confined to Vienna. "
            "One example of alleged effects from playing the glass harmonica was noted by German musicologist Johann Friedrich Rochlitz [...] "
            "plunges the player into a nagging depression and hence into a dark and melancholy mood, that is an apt method for slow self-annihilation. [...] "
            "A modern version of the \"purported dangers\" claims that players suffered lead poisoning because armonicas were made of lead glass. "
            "However, there is no known scientific basis for the theory that merely touching lead glass can cause lead poisoning. [...] "
            "doctors prescribed lead compounds for a long list of ailments, and lead or lead oxide was used as a food preservative and in cookware and eating utensils. "
            "Trace amounts of lead that armonica players in Franklin's day received from their instruments would likely have been dwarfed by lead from other sources",
            nome="Glass harmonica")],
    },
    # 9 Moreschi, o último castrato gravado
    {
        "temas_secundarios": ["invencoes", "religioes"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "A voz de um castrato não é só lenda: Alessandro Moreschi, do coro da Capela Sistina, gravou discos solo em 1902 e 1904. Ele é o único castrato que fez isso, pouco antes de um papa trocar essas vozes por meninos.",
        "explicacao": (
            "Por séculos, meninos com talento vocal eram castrados bem antes da puberdade para manter a voz aguda. "
            "Moreschi nasceu em 1858 perto de Frascati, nos Estados Papais. Talvez tenha sido castrado por causa "
            "de uma hérnia, já que a castração ainda era vista como cura na Itália do século XIX, ou talvez por "
            "volta de 1865, segundo a prática antiga. Ele virou primeiro soprano da Capela Sistina, posto que "
            "ocupou por trinta anos, e era a única esperança de manter ali a tradição do célebre Miserere de "
            "Allegri: os outros seis castrati do coro não davam conta da parte aguda. Em abril de 1902, os "
            "irmãos Gaisberg, da Gramophone & Typewriter Company, de Londres, montaram o equipamento numa sala do "
            "Vaticano de paredes cobertas de Ticianos e Rafaéis e gravaram o coro, incluindo quatro solos de "
            "Moreschi. Em 1904 houve uma segunda sessão, e as gravações dele somam dezessete faixas. Em novembro "
            "de 1903, o novo papa, Pio X, determinou que as partes de soprano e contralto fossem cantadas por "
            "meninos, e Moreschi e os poucos colegas restantes deveriam ser aposentados. Ele seguiu oficialmente "
            "no coro até 1913. Os críticos divergem sobre os discos: uns ouvem um cantor medíocre; outros, o que "
            "restava de um cantor talentoso."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Alessandro_Moreschi",
            "Alessandro Moreschi (1 November 1858 – 21 April 1922) was an Italian chorister of the late 19th century and the only castrato to make solo recordings. [...] "
            "the town of Monte Compatri in the Papal States, near Frascati (Lazio). "
            "It is possible that he was born with an inguinal hernia, for which castration was still thought to be a cure in 19th-century Italy. "
            "Another possibility is that he was castrated later, around 1865, which would have been more in line with the centuries-old practice of castrating vocally talented boys well before puberty. [...] "
            "he was appointed First Soprano there, a post he held for the next thirty years. [...] "
            "realised that Moreschi was, amongst other things, the only hope for the continuation of the Sistine tradition of performing the famous setting of the Miserere by Gregorio Allegri during Holy Week. "
            "When Moreschi joined the Sistine choir, there were still six other castrato members, but none of them were capable of sustaining this work's taxing soprano tessitura. [...] "
            "He made additional recordings in 1904 with seventeen tracks total. [...] "
            "His successor was Pope Pius X, a powerful advocate of Cecilianism. "
            "Among the pontiff's first official acts was the promulgation of the motu proprio, Tra le sollecitudini (\"Amidst the Cares\") on St Cecilia's Day, 22 November 1903, stating: "
            "\"Whenever ... it is desirable to employ the high voices of sopranos and contraltos, these parts must be taken by boys, according to the most ancient usage of the Church.\" "
            "Moreschi and his few remaining colleagues were to be pensioned and replaced by boys. "
            "Officially, Alessandro was a member of the Sistine choir until Easter 1913 [...] "
            "The first series of recordings was made on 3 and 5 April 1902 by Will and Fred Gaisberg. "
            "Eighteen usable sides by the members of the Sistine Chapel Choir were captured on wax, four of them solos by Moreschi. [...] "
            "\"Selecting a great salon with walls covered with Titians, Raphaels, and Tintorettos, we mounted our grimy machine right in the middle of the floor.\" "
            "The second set of recordings was made in Rome in April 1904 [...] "
            "Some say they are of little interest other than the novelty of preserving the voice of a castrato, and that Moreschi was a mediocre singer, while others detect the remains of a talented singer",
            nome="Alessandro Moreschi")],
    },
    # 10 a música do computador de Turing, gravada no tom errado
    {
        "temas_secundarios": ["historia_computacao", "acustica"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "A gravação mais antiga de música tocada por computador, de 1951, soava no tom errado. Pesquisadores notaram isso porque ela tinha notas que a máquina do laboratório de Turing jamais conseguiria produzir.",
        "explicacao": (
            "Em 1951, uma equipe externa da BBC gravou num disco de acetato três melodias tocadas pelo enorme "
            "computador do laboratório de Alan Turing, em Manchester: o hino nacional britânico, a cantiga \"Baa, "
            "Baa, Black Sheep\" e \"In the Mood\", de Glenn Miller. A máquina tinha uma instrução que soltava um "
            "pulso curto no alto-falante; repetida em certos padrões, a sequência de cliques soava como uma nota "
            "contínua. Turing usava esses sons para indicar o que o computador estava fazendo, e foi o jovem "
            "professor Christopher Strachey quem, numa noite sozinho na máquina, programou o hino. Segundo Jack "
            "Copeland e o compositor Jason Long, é mito a ideia de que as primeiras notas de computador soaram em "
            "1957 nos EUA: no laboratório de Turing, elas já saíam do alto-falante no outono de 1948. O computador "
            "foi sucateado há muito tempo, e o disco é a única janela para o seu som. Os dois calcularam, a partir "
            "do manual de programação de Turing, todas as frequências que a máquina podia gerar e viram que "
            "muitas das que o disco tocava eram impossíveis para ela. A diferença revelou a velocidade errada, "
            "provavelmente porque o prato do gravador portátil girava rápido demais. Corrigida a velocidade e "
            "filtrado o ruído, pesquisadores da Universidade de Canterbury, na Nova Zelândia, restauraram o som "
            "em 2016."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": BL_TURING, "titulo": "Restoring the first recording of computer music (British Library, Sound and Vision blog)", "idioma": "en",
             "trecho": "An important case in point is the earliest known recording of computer-generated music. "
                "In 1951, a BBC outside broadcast unit in Manchester used a portable acetate disc cutter to capture three melodies played by a primeval computer. "
                "This gigantic computer filled much of the ground floor of Alan Turing's Computing Machine Laboratory. [...] "
                "The computer itself was scrapped long ago, so the archived recording is our only window on that historic soundscape. [...] "
                "it's an urban myth of the music world that the first computer-generated musical notes were heard in 1957, at Bell Labs in America. [...] "
                "computer-generated notes were emerging from a loudspeaker in Turing's computing lab as early as the autumn of 1948. "
                "The Manchester computer had a special instruction that caused the loudspeaker—Turing called it the 'hooter'—to emit a short pulse of sound, lasting a tiny fraction of a second. [...] "
                "Turing realized that if the 'hoot' instruction were repeated not simply over and over again, but in different patterns, then the ear would hear different musical notes [...] "
                "he used the different notes to indicate what was going on in the computer [...] "
                "A young schoolteacher named Christopher Strachey [...] "
                "Turing knew the precocious Strachey well enough to let him use the computer for a night. [...] "
                "leaving him alone at the computer's console until the following morning. [...] "
                "In the morning, to onlookers' astonishment the computer raucously hooted out the National Anthem. [...] "
                "included not only the National Anthem but also an endearing, if rather brash, rendition of the nursery rhyme Baa Baa Black Sheep as well as a reedy and wooden performance of Glenn Miller’s famous hit In the Mood. [...] "
                "We found there was enough information in Turing's wonderfully pithy Programmers' Handbook to enable us to calculate all the audible frequencies that the Mark II could produce. [...] "
                "So distant was the recording from the original that many of the recorded frequencies were actually ones that it was impossible for the Mark II to play. [...] "
                "revealed that the recorded music was in fact playing at an incorrect speed. "
                "This was most likely the result of the mobile recorder's turntable running too fast while the acetate disc was being cut [...] "
                "We also filtered out extraneous noise from the recording"},
            wiki("Computer_music",
                "this is recognized as the earliest recording of a computer to play music as the CSIRAC music was never recorded. [...] "
                "Researchers at the University of Canterbury, Christchurch declicked and restored this recording in 2016",
                nome="Computer music"),
        ],
    },
    # 11 a Sinfonia de Leningrado e a Operação Squall
    {
        "temas_secundarios": ["segunda_guerra", "psicologia_social"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Em 1942, na Leningrado cercada pelos nazistas, músicos famintos tocaram uma sinfonia de Shostakovich, ouvida por alto-falantes até pelos alemães. Antes, os soviéticos bombardearam a artilharia alemã para calá-la.",
        "explicacao": (
            "A sinfonia foi começada em Leningrado e concluída em dezembro de 1941 em Kuibyshev, hoje Samara, onde "
            "estreou em março de 1942. Na cidade sitiada, a única orquestra sinfônica que restava era a da Rádio "
            "de Leningrado, regida por Karl Eliasberg, e só 15 integrantes ainda estavam disponíveis: os outros "
            "tinham morrido de fome ou ido lutar. Cartazes convocaram todos os músicos da cidade, e os da orquestra "
            "passaram a receber rações extras. Com o cerco, a partitura chegou de avião, à noite, no início de "
            "julho, e uma equipe de copistas passou dias preparando as partes apesar da falta de material. Alguns "
            "músicos protestaram contra gastar suas poucas forças numa obra complexa, e Eliasberg ameaçou cortar "
            "as rações extras. O concerto aconteceu em 9 de agosto de 1942, data que Hitler tinha escolhido para "
            "celebrar a queda da cidade com um banquete no Hotel Astoria. Alto-falantes levaram a música à cidade "
            "inteira e às linhas alemãs, numa jogada de guerra psicológica. Para que a artilharia inimiga ficasse "
            "calada durante a execução, o general Govorov, comandante soviético da frente, ordenou a Operação "
            "Squall (\"rajada\"): três mil projéteis de grosso calibre contra as posições alemãs. Na Alemanha, a "
            "sinfonia só estreou depois da guerra, em 1946."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Symphony_No._7_(Shostakovich)",
            "nicknamed the Leningrad Symphony, was begun in Leningrad, completed in the city of Samara (then known as Kuybyshev) in December 1941, and premiered in that city on March 5, 1942. [...] "
            "The Leningrad Radio Orchestra under Karl Eliasberg was the only remaining symphonic ensemble. [...] "
            "Only 15 members were still available; the others had either starved to death or left to fight the enemy. "
            "Posters went up, requesting all Leningrad musicians to report to the Radio Committee. [...] "
            "Orchestral players were given additional rations. [...] "
            "Because the city was still blockaded at the time, the score was flown by night in early July for rehearsal. "
            "A team of copyists worked for days to prepare the parts despite shortages of materials. "
            "At rehearsal, some musicians protested, not wanting to waste their little strength on an intricate and not very accessible work. "
            "Eliasberg threatened to hold back the additional rations, quelling any dissent. "
            "The concert was given on 9 August 1942. "
            "Whether this date was chosen intentionally, it was the day Hitler had chosen previously to celebrate the fall of Leningrad with a lavish banquet at the Astoria Hotel. "
            "Loudspeakers broadcast the performance throughout the city as well as to the German forces in a move of psychological warfare. "
            "The Soviet commander of the Leningrad front, General Govorov, ordered a bombardment of German artillery positions in advance to ensure their silence during the performance of the symphony; a special operation, code-named \"Squall,\" was executed for precisely this purpose. "
            "Three thousand high-caliber shells were lobbed onto the enemy. "
            "The symphony was not premiered in Germany until after the war. It took place in Berlin on 22 December 1946",
            nome="Symphony No. 7 (Shostakovich)")],
    },
    # 12 o Quarteto para o Fim do Tempo, num campo de prisioneiros
    {
        "temas_secundarios": ["segunda_guerra", "religioes"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Uma das obras mais importantes de Olivier Messiaen foi composta num campo de prisioneiros nazista, com papel e lápis dados por um guarda. Estreou ali em 1941, tocada por colegas presos, para uns 400 ouvintes.",
        "explicacao": (
            "Messiaen tinha 31 anos quando a França entrou na Segunda Guerra. Convocado como auxiliar médico, foi "
            "capturado em junho de 1940 e mandado ao Stalag VIII-A, em Görlitz, na Alemanha, hoje Zgorzelec, na "
            "Polônia. Entre os prisioneiros havia três músicos profissionais: o clarinetista Henri Akoka, o "
            "violinista Jean le Boulaire e o violoncelista Étienne Pasquier. Com papel e um lápis pequeno obtidos "
            "de um guarda simpático, Carl-Albert Brüll, Messiaen escreveu um trio curto para eles e depois o "
            "ampliou, com ele próprio ao piano. A formação, clarinete, violino, violoncelo e piano, era incomum, "
            "mas tinha precedentes. O resultado, o \"Quarteto para o Fim do Tempo\", em oito movimentos, foi "
            "inspirado num trecho do Apocalipse em que um anjo jura que não haverá mais tempo. A estreia foi em 15 "
            "de janeiro de 1941, e o violoncelo foi comprado com doações dos presos. Mais tarde, Messiaen disse que "
            "5 mil pessoas assistiram e que os instrumentos estavam em péssimo estado, relatos hoje considerados "
            "\"um tanto exagerados\". Ele também recordou que nunca tinha sido ouvido com tanta atenção e "
            "compreensão. Meses depois, foi libertado com a ajuda de Brüll e de um apelo do seu antigo professor "
            "de órgão, Marcel Dupré."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Quatuor_pour_la_fin_du_temps",
            "is an eight-movement piece of chamber music by the French composer Olivier Messiaen. [...] "
            "The work is scored for clarinet (in B-flat), violin, cello, and piano [...] "
            "Messiaen wrote the piece while a prisoner of war in German captivity and it was first performed by his fellow prisoners. "
            "It is generally considered one of his most important works. [...] "
            "Messiaen was 31 years old when France entered World War II. He was drafted into the French army as a medical auxiliary. "
            "In June 1940, he was captured by the German army and imprisoned in Stalag VIII-A, a prisoner-of-war camp in Görlitz, Germany (now Zgorzelec, Poland). "
            "While in transit to the camp, Messiaen showed the clarinetist Henri Akoka, also a prisoner [...] "
            "Two other professional musicians, violinist Jean le Boulaire and cellist Étienne Pasquier, were among his fellow prisoners, and after he managed to obtain some paper and a small pencil from a sympathetic guard (Carl-Albert Brüll, 1902–1989), Messiaen wrote a short trio for them [...] "
            "Later, he decided to write for the same trio with himself at the piano, developing it into its current state. "
            "The combination of instruments was unusual at the time, but not without precedent [...] "
            "The quartet was premiered at the camp on 15 January 1941 in front of about 400 prisoners and guards. "
            "Messiaen claimed that 5,000 people attended the performance and that the musicians had decrepit instruments, but those claims are now considered \"somewhat exaggerated\". "
            "The cello was bought with donations from camp members. "
            "Messiaen later recalled, \"Never was I listened to with such rapt attention and comprehension.\" "
            "Several months later, Messiaen was released (with the help of Brüll) thanks to an entreaty by his former organ teacher and professor at the Paris Conservatoire, Marcel Dupré [...] "
            "Messiaen wrote in the Preface to the score that the work was inspired by text from the Book of Revelation [...] "
            "sware by him that liveth for ever and ever [...] "
            "that there should be time no longer",
            nome="Quatuor pour la fin du Temps")],
    },
    # 13 a peça de Cage que vai durar 639 anos
    {
        "temas_secundarios": ["calendarios", "religioes"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Numa igreja da Alemanha, um órgão toca desde 2001 uma peça de John Cage que só deve terminar em 2640. Sacos de areia seguram os pedais, e a próxima mudança de nota está marcada para outubro de 2027.",
        "explicacao": (
            "A peça é Organ²/ASLSP, sigla de \"As Slow as Possible\", o mais lento possível. Cage escreveu a "
            "versão para piano em 1985, que costuma durar de 20 a 70 minutos, e a adaptou para órgão em 1987. "
            "Numa conferência em 1997, músicos e filósofos discutiram a instrução do compositor, já que um órgão "
            "bem mantido pode sustentar um som indefinidamente. Uma fundação de Halberstadt decidiu então tocar a "
            "obra por 639 anos, o intervalo entre a instalação do primeiro órgão permanente documentado da "
            "catedral da cidade, por volta de 1361, e a data de início proposta, 2000. Por falta de dinheiro, a "
            "largada atrasou um ano. Na Igreja de São Burchardi, a execução começou em 5 de setembro de 2001 com "
            "uma pausa: os primeiros tubos só soaram em 5 de fevereiro de 2003. Um órgão foi construído só para "
            "isso, e um fole mantém o ar sempre fluindo para os tubos. Todas as mudanças acontecem no dia 5 do "
            "mês; a mais recente foi em agosto de 2026. Para financiar a empreitada, a fundação vendeu, até 2021, "
            "placas que homenageiam cada ano até 2640. Em 2011, o órgão foi coberto com vidro acrílico para "
            "reduzir o volume. É a execução musical não computadorizada mais longa em andamento."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("As_Slow_as_Possible",
            "Organ²/ASLSP (As Slow as Possible) is a musical piece by John Cage [...] "
            "Cage wrote it in 1987 for organ, as an adaptation of his 1985 composition ASLSP for piano. "
            "A performance of the piano version usually lasts 20 to 70 minutes. "
            "An organ in St. Burchardi church in Halberstadt in 2001 began a performance that is due to end in 2640. "
            "This makes it the longest running non-computerized piece currently being performed. [...] "
            "The next note will be played on October 5, 2027. [...] "
            "Musicians and philosophers discussed Cage's instruction to play \"as slow as possible\" at a conference in 1997, because a properly maintained pipe organ could sound indefinitely. "
            "The John Cage Organ Foundation Halberstadt decided to play the piece for 639 years, to mark the time between the first documented permanent organ installation in Halberstadt Cathedral, circa 1361, and the originally proposed start date of 2000. "
            "Because of a lack of money, the date was postponed by one year. [...] "
            "Until August 2021 the Foundation sold plaques commemorating the years through 2640 to fund the performance. [...] "
            "An organ was built specifically for the performance. [...] "
            "In 2011, the organ was encased in acrylic glass to reduce the volume [...] "
            "The Halberstadt performance started on September 5, 2001, with a rest lasting until February 5, 2003, when the first pipes played. "
            "Sandbags depress the organ's pedals to maintain the notes. [...] "
            "The bellows provide a constant supply of air to keep the pipes playing. [...] "
            "The note last changed on August 5, 2026. The performance is scheduled to end on September 5, 2640. "
            "All notes are played on the 5th day of the month.",
            nome="As Slow as Possible")],
    },
    # 14 Bing Crosby e a fita magnética
    {
        "temas_secundarios": ["invencoes", "telecomunicacoes"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "Os gravadores de fita da Ampex, que revolucionaram o rádio e a indústria fonográfica dos EUA, foram criados a pedido de Bing Crosby, que não gostava de fazer seu programa ao vivo. O modelo era alemão, da guerra.",
        "explicacao": (
            "No fim da Segunda Guerra, o major Jack Mullin, do Corpo de Sinais do Exército americano, foi "
            "encarregado de investigar experimentos alemães de rádio e eletrônica. Numa visita à Rádio Frankfurt, "
            "conheceu o Magnetophon, um gravador de fita com fidelidade muito melhor que a dos discos de "
            "goma-laca. Com a derrota alemã, as patentes desses aparelhos perderam efeito na prática, e Mullin "
            "levou para os EUA dois deles e 50 rolos de fita, que modificou. Crosby, então um grande astro do "
            "rádio, detestava a rigidez das transmissões ao vivo e preferia o clima descontraído do estúdio. Ele "
            "já tinha pedido à rede NBC para pré-gravar o programa em discos, sem sucesso, e chegou a passar um "
            "ano fora do rádio ao vivo. Em junho de 1947, ao ouvir uma demonstração dos gravadores de Mullin, viu "
            "na hora o potencial da tecnologia e encomendou uma gravação de teste do seu programa. A empresa "
            "Ampex, que desenvolveu os gravadores a partir do Magnetophon, entregou seu primeiro modelo em abril de "
            "1948, e as unidades de número de série 1 e 2 foram para o programa de Crosby. A Ampex virou líder em fita e criou formatos "
            "analógicos usados em música e cinema até os anos 1990."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Ampex",
            "Ampex's first great success was a line of reel-to-reel tape recorders developed from the German wartime Magnetophon system at the behest of Bing Crosby. "
            "Ampex quickly became a leader in audio tape technology, developing many of the analog recording formats for both music and movies that remained in use into the 1990s. [...] "
            "Near the end of the war, while serving in the U.S. Army Signal Corps, Major Jack Mullin was assigned to investigate German radio and electronics experiments. "
            "He discovered the Magnetophons with AC biasing on a trip to Radio Frankfurt. "
            "The device produced much better fidelity than shellac records. "
            "The technological processes in tape recording and equipment developed by German companies before and during the 1939–1945 war were subject to patents which were effectively voided after Germany's 1945 surrender and defeat. "
            "Mullin acquired two Magnetophon recorders and 50 reels of BASF Type L tape, and brought them to America, where he produced modified versions. [...] "
            "Bing Crosby, a big star on radio at the time, was receptive to the idea of pre-recording his radio programs. "
            "He disliked the regimentation of live broadcasts, and much preferred the relaxed atmosphere of the recording studio. "
            "He had already asked the NBC network to let him pre-record his 1944–45 series on transcription discs, but the network refused; so Crosby had withdrawn from live radio for a year [...] "
            "In June 1947, Mullin, who was pitching the technology to the major Hollywood movie studios, got the chance to demonstrate his modified tape recorders to Crosby. "
            "When Crosby heard a demonstration of Mullin's tape recorders, he immediately saw the potential of the new technology and commissioned Mullin to prepare a test recording of his radio show. [...] "
            "The company's first tape recorder, the Ampex Model 200A, was first shipped in April 1948. "
            "The first two units, serial numbers 1 and 2, were used to record Bing Crosby's show. "
            "The American Broadcasting Company used these recorders along with 3M Scotch 111 gamma ferric oxide coated acetate tape for the first-ever U.S. delayed radio broadcast of Bing Crosby's Philco Radio Time. "
            "Ampex tape recorders revolutionized the radio and recording industries because of their superior audio quality and ease of operation over audio disk cutting lathes.",
            nome="Ampex")],
    },
    # 15 Paganini, 36 anos sem sepultura
    {
        "temas_secundarios": ["religioes", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Quando Paganini morreu, em 1840, a Igreja negou ao violinista um enterro católico em Gênova, em parte pela fama de ter parte com o diabo. O corpo dele só foi sepultado em 1876.",
        "explicacao": (
            "Os últimos anos de Paganini foram difíceis. Em 1836, ele montou um cassino em Paris, que fracassou "
            "na hora e o deixou arruinado; para cobrir as perdas, leiloou seus bens, inclusive os instrumentos. "
            "Doente, foi para Marselha e depois para Nice. Em maio de 1840, o bispo de Nice mandou um padre para "
            "lhe dar a extrema-unção, mas Paganini achou que era cedo e recusou. Uma semana depois, em 27 de maio, "
            "morreu aos 57 anos, de hemorragia interna, antes que se pudesse chamar um padre. Por isso, e pelos "
            "boatos muito difundidos de que ele tinha ligação com o diabo, a Igreja recusou ao corpo um enterro "
            "católico em Gênova. Foram precisos quatro anos e um apelo ao papa para que o corpo "
            "pudesse ser levado a Gênova, mas nem assim ele foi enterrado. O sepultamento só aconteceu em 1876, num "
            "cemitério de Parma. E a história não parou aí: em 1893, o violinista tcheco František Ondříček "
            "convenceu o neto de Paganini a deixar que o corpo fosse visto. Depois desse episódio, os restos foram "
            "transferidos, em 1896, para um novo cemitério de Parma."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Niccol%C3%B2_Paganini",
            "In 1836, Paganini returned to Paris to set up a casino. "
            "Its immediate failure left him in financial ruin, and he auctioned off his personal effects, including his musical instruments, to recoup his losses. "
            "At Christmas of 1838, he left Paris for Marseille and, after a brief stay, traveled to Nice where his condition worsened. "
            "In May 1840, the Bishop of Nice sent Paganini a local parish priest to perform the last rites. "
            "Paganini assumed the sacrament was premature, and refused. "
            "A week later, on 27 May 1840, the 57-year-old Paganini died from internal hemorrhaging before a priest could be summoned. "
            "Because of this, and his widely rumored association with the devil, the Church denied his body a Catholic burial in Genoa. "
            "It took four years and an appeal to the Pope before the Church let his body be transported to Genoa, but it was still not buried. "
            "His body was finally buried in 1876, in a cemetery in Parma. "
            "In 1893, the Czech violinist František Ondříček persuaded Paganini's grandson, Attila, to allow a viewing of the violinist's body. "
            "After this episode, Paganini's body was finally reinterred in a new cemetery in Parma in 1896.",
            nome="Niccolò Paganini")],
    },
]
