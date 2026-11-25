LOTE = "2026-11-25-musica_brasileira-01"
AREA = "brasil"
TEMA = "musica_brasileira"
W = "https://en.wikipedia.org/wiki/"
UNICAMP_CAIPIRA = "https://www.iar.unicamp.br/wp-content/uploads/2021/07/V2_ED03_A4_Musicacaipiraeodisco.pdf"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 a Garota de Ipanema processada pelos herdeiros dos autores
    {
        "temas_secundarios": ["leis_julgamentos", "cidades"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "A moça real de \"Garota de Ipanema\", Helô Pinheiro, foi processada em 2001 pelos herdeiros de Tom Jobim e Vinicius de Moraes por usar o nome da canção na sua grife. E ela ganhou.",
        "explicacao": (
            "A canção foi escrita em 1962, com música de Jobim e letra de Vinicius. A inspiração foi Heloísa, então "
            "com 17 anos, que morava na Rua Montenegro, em Ipanema, e todo dia passava diante do bar Veloso a caminho "
            "da praia. Às vezes entrava para comprar cigarros para a mãe e saía ouvindo assobios. Ao compor, os dois "
            "se lembraram do que sentiam quando a viam passar, e a jovem ficou famosa depois do lançamento. Em 1999, "
            "Helô lançou uma grife de moda praia chamada justamente Garota de Ipanema. Em 2001, os "
            "herdeiros dos compositores, donos dos direitos da canção, foram à Justiça: alegavam que ser a musa não "
            "lhe dava direito a um nome que, legalmente, pertencia a eles. O público ficou do lado dela, e a defesa "
            "usou um comunicado dos próprios Jobim e Vinicius que a apontava como a verdadeira Garota de Ipanema, "
            "sinal de que eles quiseram lhe dar o título. O tribunal decidiu a favor de Helô. A canção, que ganhou o "
            "Grammy de gravação do ano em 1965, é tida como a segunda canção pop mais gravada da história, atrás de "
            "\"Yesterday\", dos Beatles, e no levantamento do Ecad de 2023 aparecia em primeiro lugar entre as mais "
            "regravadas do Brasil."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("The_Girl_from_Ipanema",
                "It was a worldwide hit in the mid-1960s and won a Grammy for Record of the Year in 1965. "
                "It was written in 1962, with music by Antônio Carlos Jobim and Portuguese lyrics by Vinícius de Moraes [...] "
                "It is believed to be the second-most-recorded pop song in history, after \"Yesterday\" by the Beatles. [...] "
                "The song was inspired by Heloísa Eneida Menezes Paes Pinto (now known as Helô Pinheiro), a 17-year-old girl living on Montenegro Street in Ipanema. "
                "Every day, she would stroll past the Veloso bar-café, not just to the beach [...] "
                "She would sometimes enter the bar to buy cigarettes for her mother and leave to the sound of wolf whistles. "
                "Later when they were writing the song, the composers remembered how they felt when the girl passed by the bar. "
                "She became famous after the song was released. [...] "
                "In 2001, the song's copyright owners (the heirs of their composer fathers) sued Pinheiro for using the title of the song as the name of her boutique (Garota de Ipanema). "
                "In their complaint, they stated that her status as the Girl from Ipanema (Garota de Ipanema) did not entitle her to use a name that legally belonged to them. "
                "Public support was strongly in favor of Pinheiro. "
                "A press release by Jobim and Moraes, the composers, in which they had named Pinheiro as the real Girl from Ipanema  was used as evidence that they had intended to bestow this title on her. "
                "The court ruled in favor of Pinheiro.",
                nome="The Girl from Ipanema"),
            wiki("Helô_Pinheiro",
                "Em 1999 Helô lançou sua própria grife de moda de praia, intitulada Garota de Ipanema, o qual abriu lojas em diversos estados do país.",
                nome="Helô Pinheiro", idioma="pt"),
            wiki("Garota_de_Ipanema",
                "Segundo levantamento do Escritório Central de Arrecadação e Distribuição (Ecad) divulgado em 2021, Garota de Ipanema era a terceira canção mais regravada do Brasil, com 402 gravações até a data. "
                "No levantamento de 2023, a canção aparecia na 1ª posição.",
                nome="Garota de Ipanema", idioma="pt"),
        ],
    },
    # 2 Astrud Gilberto: a voz amadora de 120 dólares
    {
        "temas_secundarios": ["historia_musica", "linguas_mundo"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "A voz da \"Garota de Ipanema\" que fez sucesso no mundo era de Astrud Gilberto, que não era cantora profissional. Foi escolhida por ser a única do grupo que falava bem inglês e recebeu só 120 dólares.",
        "explicacao": (
            "Numa sessão em Nova York com João Gilberto, Tom Jobim e o saxofonista Stan Getz, surgiu a ideia de "
            "gravar a canção também em inglês, com letra de Norman Gimbel. Entre os brasileiros, só Astrud, então "
            "mulher de João, falava bem a língua, e ela acabou escolhida. Era totalmente inexperiente: Getz contou, "
            "vinte anos depois, que João e Jobim não a queriam cantando, e o produtor Creed Taylor a apoiou por "
            "razões comerciais, de olho numa voz feminina numa língua \"menos exótica\". Ela precisou de cinco "
            "tomadas. A voz sem os maneirismos de cantores treinados caiu como uma luva: o compacto, uma versão "
            "encurtada da faixa do álbum Getz/Gilberto, chegou ao quinto lugar da parada Billboard Hot 100. Mesmo "
            "assim, Astrud nunca recebeu crédito nem direitos e ganhou apenas 120 dólares. O clima no estúdio também "
            "não era só harmonia. Segundo o jornalista Ruy Castro, João, impaciente com Getz e sem falar inglês, "
            "pediu a Jobim: \"Diga a esse gringo que ele é burro\". Jobim traduziu como \"Stan, o João está dizendo "
            "que o sonho dele sempre foi gravar com você\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("The_Girl_from_Ipanema",
                "This version had been shortened from  the version on the album Getz/Gilberto [...] "
                "In the US, the single peaked at number five on the Billboard Hot 100 [...] "
                "During a recording session in New York City with João Gilberto, Antônio Carlos Jobim, and Stan Getz, the idea of cutting an English-language version came up. "
                "Norman Gimbel wrote the English lyrics. "
                "João's wife, Astrud Gilberto, was the only one of the Brazilians who could speak English well, and was chosen to sing. "
                "Her voice, without any of the mannerisms of trained singers, proved a perfect fit for the song. "
                "She was never credited, though, nor did she receive any royalties, and was paid only $120 for her part.",
                nome="The Girl from Ipanema"),
            wiki("Garota_de_Ipanema",
                "Ruy Castro, em suas pesquisas sobre os bastidores do disco, conta que João e Stan frequentemente discordavam na escolha do melhor take entre os gravados e por isso cabia a Creed Taylor fazer o desempate. "
                "Em determinado momento, Gilberto, impaciente com as sutilezas rítmicas do saxofonista e sem dominar a língua inglesa, disse a Jobim: \"Diga a esse gringo que ele é burro\", ao que Jobim traduziu: \"Stan, John is saying that his dream has always been to record with you\" (em português: \"Stan, o João está dizendo que o sonho dele sempre foi gravar com você\"). [...] "
                "Ela só foi ao estúdio no segundo dia de gravação e era completamente inexperiente como cantora. "
                "Stan Getz lembrou-se vinte anos depois: \"Gilberto e Jobim não queriam Astrud cantando. [...] "
                "O produtor Creed Taylor também apoiou as ambições vocais de Astrud: por razões comerciais, teve o melhor sentido de ter uma voz feminina no álbum, cantando \"em uma linguagem menos exótica\". [...] "
                "o cantor finalmente precisou de cinco takes",
                nome="Garota de Ipanema", idioma="pt"),
        ],
    },
    # 3 Carmen Miranda: portuguesa, vaiada por "americanizada"
    {
        "temas_secundarios": ["cinema_fotografia", "moda"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Carmen Miranda, símbolo do Brasil em Hollywood, nasceu em Portugal e manteve a nacionalidade portuguesa. Em 1940, vaiada no Rio por parecer \"americanizada\", respondeu com um samba e ficou 14 anos sem voltar.",
        "explicacao": (
            "Maria do Carmo nasceu em 1909 numa aldeia de Marco de Canaveses, no norte de Portugal, e chegou ao Rio "
            "com menos de um ano. Nunca voltou à terra natal. O famoso turbante de frutas veio de 1939, do filme "
            "\"Banana da Terra\", numa versão glamourosa do traje da baiana pobre e negra; e, ao contrário do que se "
            "pensa, as frutas nunca foram de verdade. Nos Estados Unidos, ela virou a \"Brazilian Bombshell\" com "
            "apoio do governo americano, que via em artistas como ela um reforço para a política de boa vizinhança "
            "com a América Latina. Em 1945, era a mulher mais bem paga do país. A volta ao Brasil foi amarga. Em 15 "
            "de julho de 1940, num show beneficente organizado pela primeira-dama Darci Vargas, ela cumprimentou a "
            "plateia da alta sociedade em inglês e cantou \"The South American Way\". Foi vaiada até desistir e "
            "chorou no camarim. Parte da elite a achava \"negra demais\", e a imprensa a chamou de americanizada. "
            "Semanas depois, ela respondeu cantando \"Disseram que Voltei Americanizada\". O chapéu, aliás, inspirou "
            "a personagem da banana Chiquita, criada pela United Fruit Company."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Carmen_Miranda",
            "Miranda was born Maria do Carmo Miranda da Cunha in 1909 in Várzea da Ovelha e Aliviada, a village in the northern Portuguese municipality of Marco de Canaveses. [...] "
            "In 1909, her father emigrated to Brazil and settled in Rio de Janeiro, where he opened a barber shop. "
            "Her mother followed in 1910 with their daughters Olinda and Carmen, who was less than a year old. "
            "Although Carmen never returned to Portugal, she retained her Portuguese nationality. [...] "
            "By 1945, she was the highest-paid woman in the United States. [...] "
            "Although she became synonymous with colorful fruit hats during her later career, she began wearing them only in 1939, and contrary to popular belief, they were never made from real fruit. "
            "Miranda appeared in the film Banana da Terra that year in a glamorous version of the traditional dress of a poor black girl in Bahia: a flowing dress and a fruit-hat turban. [...] "
            "Miranda was encouraged by the US government as part of Roosevelt's Good Neighbor policy, designed to strengthen ties with Latin America. "
            "It was believed that performers like her would give the policy a favorable impression with the American public. [...] "
            "Members of the upper class felt that her image was \"too black\" [...] "
            "On 15 July, Miranda appeared in a charity concert organized by Brazilian First Lady Darci Vargas and attended by members of Brazil's high society. "
            "She greeted the audience in English and was met with silence. "
            "When Miranda began singing \"The South American Way\", a song from one of her club acts, the audience began to boo her. "
            "Although she tried to finish her act, she gave up and left the stage when the audience refused to let up. "
            "The incident deeply hurt Miranda, who wept in her dressing room. "
            "The following day, the Brazilian press criticized her as \"too Americanized\". "
            "Weeks later, Miranda responded to the criticism with the Portuguese song \"Disseram que Voltei Americanizada\" (\"They Say I've Come Back Americanized\"). [...] "
            "Upset by the criticism, Miranda did not return to Brazil for 14 years. [...] "
            "On 10 July 1940, she returned to Brazil and was welcomed by cheering fans. [...] "
            "The United Fruit Company created a banana-woman character in 1944, Chiquita, whose fruit hat resembled Miranda's.",
            nome="Carmen Miranda")],
    },
    # 4 Aquarela do Brasil: fracasso, briga com Villa-Lobos, Disney e Terry Gilliam
    {
        "temas_secundarios": ["cinema_fotografia", "brasil_republica"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "\"Aquarela do Brasil\" não fez sucesso no início, e Ary Barroso rompeu com Villa-Lobos, presidente do júri que a deixou fora do pódio no Carnaval de 1940. A Disney a levou ao mundo, e ela batizou um filme de Terry Gilliam.",
        "explicacao": (
            "Ary Barroso compôs o samba no início de 1939, numa noite em que um temporal o impediu de sair de casa; "
            "o \"aquarela\" do título alude à chuva. A gravação de Francisco Alves, com arranjo de Radamés Gnattali, "
            "saiu em agosto daquele ano, e nem ela nem a de Araci Cortes emplacaram. Em 1940, a música ficou fora das "
            "três primeiras do Carnaval carioca. O júri era presidido por Villa-Lobos, e Barroso, ofendido, rompeu "
            "com ele: os dois só voltaram a se falar quinze anos depois. Houve outros tropeços. A censura do governo "
            "Vargas quis cortar o verso \"terra do samba e do pandeiro\", visto como depreciativo, e Barroso convenceu "
            "os censores a mantê-lo. Na gravação original, Alves cantou \"mulato risoneiro\" em vez de \"inzoneiro\" "
            "porque não conseguiu decifrar a letra do compositor. A virada veio com o desenho \"Saludos Amigos\", da "
            "Disney, de 1942. A canção se espalhou pelo mundo, foi a primeira brasileira "
            "tocada mais de um milhão de vezes nas rádios americanas e, como \"Brazil\", deu nome ao filme de Terry "
            "Gilliam de 1985."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Aquarela_do_Brasil",
            "Ary Barroso wrote \"Aquarela do Brasil\" in early 1939, when he was prevented from leaving his home one rainy night due to a heavy storm. "
            "Its title, a reference to watercolor painting, is a clear reference to the rain. [...] "
            "It was then recorded by Francisco de Morais Alves, arranged by Radamés Gnattali and his orchestra, and released by Odeon Records in August 1939. "
            "It was also recorded by Araci Cortes, but despite the singer's huge popularity at the time, the song was not a success. "
            "\"Aquarela do Brasil\" took a while to succeed. "
            "In 1940, it was not among the top three songs of that year's Carnival in Rio. "
            "The president of the jury was Heitor Villa-Lobos, and Barroso, offended that his masterpiece was not on the list, ended his relationship with him. "
            "The two men would only speak to each other again fifteen years later, when both received the National Order of Merit. "
            "The song only became famous after it was included in Walt Disney's 1942 animated film Saludos Amigos, sung by Aloísio de Oliveira. "
            "After that, the song became known not only in Brazil, but worldwide, becoming the first Brazilian song to be played over a million times on American radio. [...] "
            "The Department of Press and Propaganda, the official censorship body of the regime, wanted to censor the line \"terra do samba e do pandeiro\" (\"land of samba and the pandeiro\"), which was seen as being \"derogatory\" for Brazil's image. "
            "Barroso persuaded the censors to keep the line. [...] "
            "On the original recording, Alves sang \"mulato risoneiro\" (laughing mulatto) instead of \"inzoneiro\" because he was unable to understand Barroso's illegible handwriting. [...] "
            "The song was featured prominently in Terry Gilliam's 1985 film Brazil, which was named after it.",
            nome="Aquarela do Brasil")],
    },
    # 5 Villa-Lobos: os canibais duvidosos e o cilindro de Roquette-Pinto
    {
        "temas_secundarios": ["povos_indigenas", "historia_musica"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Villa-Lobos contava ter sido capturado por canibais nas viagens pelo interior, relato visto com forte desconfiança. Já o canto indígena de uma de suas obras veio de um cilindro gravado por Roquette-Pinto em 1912.",
        "explicacao": (
            "Por volta de 1905, Villa-Lobos começou a percorrer o interior do Brasil e a absorver a música "
            "que encontrava. Das histórias que ele contou sobre essa década de viagens, muitas são postas em dúvida, "
            "inclusive a de que teria sido capturado por canibais e escapado por pouco: há quem as considere invenção "
            "ou romantização exagerada. A música indígena documentada, por outro lado, aparece de fato no Chôros nº 3, "
            "\"Pica-pau\", composto em São Paulo em 1925 e dedicado a Tarsila do Amaral e Oswald de Andrade. É uma das "
            "poucas grandes obras do compositor baseadas principalmente em música indígena registrada. O tema "
            "principal é \"Nozani-ná\", um canto de festa do povo paresí, gravado num cilindro por Edgar "
            "Roquette-Pinto em 1912, na Serra do Norte, em Mato Grosso. Villa-Lobos acrescentou trechos de outros "
            "dois cantos da mesma coleção, uma imitação de pica-pau que dá nome à peça e um grito final de "
            "\"Brasil!\". O sentido das palavras de \"Nozani-ná\" ainda divide os especialistas. A estreia europeia "
            "foi em Paris, em 1927."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Heitor_Villa-Lobos",
                "Around 1905 Villa-Lobos started explorations of Brazil's \"dark interior\", absorbing the native Brazilian musical culture. "
                "Serious doubt has been cast on some of Villa-Lobos's tales of the decade or so he spent on these expeditions, and about his capture and near escape from cannibals, with some believing them to be fabrications or wildly embellished romanticism.",
                nome="Heitor Villa-Lobos"),
            wiki("Chôros_No._3",
                "Chôros No. 3 was composed in São Paulo in 1925, the year after Chôros Nos. 2 and 7 were written, and the score is dedicated to the painter Tarsila do Amaral and the poet Oswald de Andrade. [...] "
                "The first European performance took place on 5 December 1927 in Paris [...] "
                "Chôros No. 3 is one of the few major works in Villa-Lobos's catalogue based principally on documented Amerindian music. "
                "Its main musical subject, presented in canon or fugato at the beginning, is a feasting song of the Pareci tribe, \"Nozani-ná\", which had been collected in the Serra do Norte, Mato Grosso, on a cylinder recording by Edgar Roquette-Pinto in 1912. [...] "
                "To this are added fragments from two other Pareci songs from Roquette-Pinto's collection, \"Noal anaue\" and \"Ena-mô-kocê\". [...] "
                "followed by the Indianist imitation of a woodpecker that gives the work its subtitle. [...] "
                "until the work comes to an end with a unison shout of the word \"Brasil!\". "
                "Concerning the sense of the words to \"Nozani-ná\", opinions differ.",
                nome="Chôros No. 3"),
        ],
    },
    # 6 o "Boi no telhado" de Milhaud, cheio de música brasileira
    {
        "temas_secundarios": ["historia_musica", "teatro_danca"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "\"Le Bœuf sur le toit\", peça do francês Darius Milhaud que deu nome a um célebre cabaré de Paris, cita mais de 20 músicas de 14 compositores brasileiros. Milhaud passou dois anos no Brasil como diplomata.",
        "explicacao": (
            "Durante a Primeira Guerra Mundial, Milhaud trabalhou dois anos no Brasil no serviço diplomático francês "
            "e se encantou com o choro. Entre 1919 e 1920, escreveu uma peça de cerca de 15 "
            "minutos pensada como fundo musical para qualquer filme mudo de Charlie Chaplin. O tema de abertura é "
            "invenção dele, mas o resto é recheado de música brasileira: uma análise publicada em 2002 identificou "
            "citações de mais de 20 peças de 14 compositores, entre elas \"Escovado\", de Ernesto Nazareth. O próprio "
            "Milhaud disse que o título, \"o boi no telhado\", era o nome de uma dança folclórica brasileira. Jean "
            "Cocteau o convenceu a transformar a música num balé, que estreou em fevereiro de 1920 com personagens de "
            "cabeças de papelão e um enredo absurdo, em que um policial tem a cabeça cortada por um ventilador. O "
            "balé deu nome a um célebre cabaré de Paris, aberto em 1921, que virou ponto de encontro de Cocteau e "
            "seu círculo. Milhaud ganhou ali a condição de sócio vitalício."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Le_Bœuf_sur_le_toit",
                "Le Bœuf sur le toit (literally \"the ox on the roof\"), Op. 58 is a 15-minute piece for small orchestra by the composer Darius Milhaud, written in 1919–20. "
                "Milhaud conceived the piece as incidental music for any one of the comic silent films of Charlie Chaplin, but it received its premiere as the music for a ballet staged by Jean Cocteau in February 1920. [...] "
                "The composer spent two years in Brazil in the French diplomatic service during the First World War, and was influenced by its music in his own compositions. [...] "
                "Milhaud himself said that it was the title of a Brazilian folk dance. [...] "
                "Milhaud quoted extensively from Brazilian tunes. "
                "An analysis published in 2002 cites more than 20 pieces by 14 Brazilian composers referred to in the score. "
                "One of them is Ernesto Nazareth's Escovado.The lively opening motif – Milhaud's own invention and not a borrowing – recurs throughout: [...] "
                "Jean Cocteau persuaded Milhaud to let the music be used for a ballet. [...] "
                "All wear cardboard heads two or three times life-size. [...] "
                "an electric fan comes down from the ceiling and cuts off the policeman's head. [...] "
                "The ballet gave its name to a celebrated Parisian cabaret-bar, Le Bœuf sur le toit, which opened in 1921 and became a meeting-place for Cocteau and his associates. "
                "Milhaud was given life membership.",
                nome="Le Bœuf sur le toit"),
            wiki("Choro",
                "The French composer Darius Milhaud was enchanted by choro when he lived in Brazil (in 1917)",
                nome="Choro"),
        ],
    },
    # 7 Pixinguinha acusado de jazz e obrigado a vender a coautoria
    {
        "temas_secundarios": ["historia_musica", "heranca_africana"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Pixinguinha, hoje um pilar do choro, foi acusado de se deixar contaminar pelo jazz. E, em aperto financeiro, vendeu seus direitos a um parceiro que virou coautor até de músicas feitas quando o parceiro era menino.",
        "explicacao": (
            "Em 1919, Pixinguinha formou com o irmão e outros músicos os Oito Batutas, que tocavam no saguão do cinema "
            "Palais e logo ficaram mais populares que os próprios filmes. O grupo tinha músicos brancos e negros e "
            "tocava em casas de elite onde artistas negros antes eram barrados, o que desagradava parte da elite "
            "branca do Rio. Com patrocínio de Arnaldo Guinle, os Batutas passaram seis meses tocando no cabaré "
            "Schéhérazade, em Paris. Pixinguinha voltou com outra cabeça: pôs saxofones, trompetes, trombones, piano e "
            "bateria na banda. Críticos acharam que o jazz americano estava estragando a música dele, e \"Lamentos\", "
            "de 1928, e \"Carinhoso\", de 1930, foram atacados por excesso de jazz. Hoje as duas são clássicos do "
            "choro. Mais tarde, tocando no regional do flautista Benedito Lacerda, Pixinguinha enfrentou dificuldades "
            "econômicas e precisou vender a ele os direitos de suas composições. Por isso Lacerda aparece como "
            "coautor de muitas delas, inclusive de algumas compostas quando ele ainda era garoto. Nas gravações, "
            "Lacerda tocava as partes de flauta escritas para Pixinguinha, que fazia o acompanhamento no saxofone."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Pixinguinha",
            "In 1919, Pixinguinha, along with his brother and other musicians formed the musical group called Os Oito Batutas [...] "
            "Performing in the lobby of the Cine Palais movie theater, the band's music soon became more popular than the films themselves. [...] "
            "Os Oito Batutas became a sensation across Brazil, despite facing disapproval from the white Rio elite against black men performing in popular venues. [...] "
            "The band had white and black musicians and performed mainly in upper-class venues where black artists had previously been prohibited. [...] "
            "Some critics claimed that Pixinguinha's compositional style and instrumental incorporation of trumpets and saxophones were negatively influenced by American jazz. [...] "
            "Os Oito Batutas were discovered by Arnaldo Guinle, who sponsored their first European tour [...] "
            "In Paris, they served as ambassadors for Brazilian music, performing for six months at the Schéhérazade cabaret. [...] "
            "Pixinguinha returned from Paris with a broadened musical perspective. "
            "He began to incorporate jazz standards and ragtime music into his band's repertoire, changing the lineup dramatically by adding saxophones, trumpets, trombones, piano, and a drum kit. [...] "
            "Pixinguinha left Orquestra Victor Brasileira to join flautist Benedito Lacerda's band [...] "
            "Due to economic issues and the fact that the regionals fell out of favor during the late 40s, Pixinguinha had to sell the rights to his compositions to Benedito Lacerda. "
            "For this reason, Benedito Lacerda is credited as the co-composer on many of Pixinguinha's tunes, even those composed while Lacerda was a young boy. "
            "Pixinguinha played supporting parts on the saxophone for the recordings with Lacerda. "
            "Lacerda plays the flute parts written and meant to be played by Pixinguinha. [...] "
            "When he released \"Lamentos\" in 1928 and \"Carinhoso\" in 1930, Pixinguinha was criticized for incorporating too many jazz elements into his compositions. "
            "These pieces have since become respected parts of the choro canon.",
            nome="Pixinguinha")],
    },
    # 8 o choro é alegre e ninguém sabe de onde vem o nome
    {
        "temas_secundarios": ["palavras_portugues", "heranca_africana"],
        "tipos_espanto": ["misterio_aberto", "origem_inesperada"],
        "gancho": "O choro, considerado o primeiro gênero tipicamente brasileiro de música popular urbana, costuma ser rápido e alegre. De onde vem o nome ninguém sabe ao certo: há ao menos três explicações em disputa.",
        "explicacao": (
            "O choro nasceu no Rio do século XIX, quando músicos cariocas, já impregnados de ritmos afro-brasileiros "
            "como o lundu e o batuque, passaram a tocar do seu jeito polcas, valsas, mazurcas e habaneras europeias. "
            "No começo, \"choro\" era o nome de um estilo de tocar ou de um conjunto: nos anos 1870, o flautista "
            "Joaquim Antônio da Silva Calado formou o \"Choro Carioca\", com flauta, dois violões e cavaquinho. Só "
            "depois a palavra passou a designar o gênero. A origem dela é controversa. Uma hipótese junta o verbo "
            "\"chorar\" ao latim \"chorus\", coro, numa alusão ao acompanhamento melancólico das danças de salão "
            "europeias. Outra vê ali uma abreviação de \"choromeleiros\", corruptela de \"charameleiros\", os "
            "tocadores de charamela, um antigo instrumento de sopro; o termo depois passou a valer para qualquer "
            "grupo musical. Uma terceira aponta para o \"xolo\", dança popular entre africanos escravizados no Brasil "
            "rural, que teria virado \"xoro\" e, na cidade, \"choro\". Os primeiros chorões, aliás, eram em boa parte "
            "trabalhadores dos correios, das ferrovias e do telégrafo, que tocavam em festas, botecos e bailes "
            "caseiros."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Choro",
            "Choro (Portuguese pronunciation: [ˈʃoɾu], \"cry\" or \"lament\"), also popularly called chorinho (\"little cry\" or \"little lament\"), is an instrumental Brazilian popular music genre which originated in 19th century Rio de Janeiro. "
            "Despite its name, the music often has a fast and happy rhythm. [...] "
            "Choro is considered the first characteristically Brazilian genre of urban popular music. [...] "
            "There is some controversy as to the origin of the name choro: some sources claim it to be a conflation of the Portuguese word for \"to cry\" (chorar) and the Latin word chorus (\"choir\"), in reference to the originally melancholic accompaniments of European salon dances. "
            "Others affirm it to be an abbreviation of choromeleiros, which itself is a corruption of charameleiros, derived from charamela (\"shawm\"), later on extended to mean any musical group. "
            "Yet another source states that the name comes from xolo, a type of dance popular amongst the enslaved Africans in rural Brazil, which was rewritten as xoro (ironically, in order to avoid confusion with the identically pronounced word choro) and then, once it made its way into the cities, changed back into choro. "
            "In the 19th century, choro resulted from the style of playing several musical genres (polka, schottische, waltz, mazurka and habanera) by carioca musicians, who were already strongly influenced by Afro-Brazilian rhythms, principally the lundu and the batuque. "
            "The term “choro” was used informally at first to refer to the style of playing, or a particular instrumental ensemble, (e.g. in the 1870s flutist Joaquim Antônio da Silva Calado formed an ensemble called \"Choro Carioca\", with flute, two guitars and cavaquinho), and later the term referred to the music genre of these ensembles. [...] "
            "In the beginning (by the 1880s to 1920s), the success of choro came from informal groups of friends (principally composed of workers from the postal, railway and telegraphic services) which played at parties, pubs (botecos), streets and home balls (forrobodós).",
            nome="Choro")],
    },
    # 9 a Lambada era uma canção boliviana
    {
        "temas_secundarios": ["leis_julgamentos", "teatro_danca"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "\"Lambada\", o hit mundial de 1989 cantado em português, era uma versão não autorizada de uma canção boliviana, \"Llorando se fue\". Os produtores franceses a registraram em nome de um compositor inventado.",
        "explicacao": (
            "A canção original é de 1981, do grupo andino boliviano Los Kjarkas, e foi registrada pelos irmãos "
            "Gonzalo e Ulises Hermosa. Era lenta e triste, no ritmo afro-boliviano da saya. Em 1984, o grupo peruano "
            "Cuarteto Continental gravou uma versão animada, com acordeão, e em 1986 a cantora brasileira Márcia "
            "Ferreira lançou a versão em português, \"Chorando se foi\". Em 1988, dois empresários franceses de "
            "passagem por Porto Seguro, na Bahia, descobriram a lambada, compraram os direitos de mais de 400 músicas "
            "do gênero e montaram em Paris o grupo Kaoma, com músicos do Brasil, da África e do Caribe. Na gravação de "
            "1989, música e letra foram creditadas a um tal \"Chico de Oliveira\", que não existia, e a letra de "
            "Márcia foi alterada. Só naquele ano, segundo o New York Times, o disco vendeu cinco milhões de cópias no "
            "mundo. A conta chegou na Justiça: em 1990, Los Kjarkas venceram uma ação por plágio, e em 1991 um "
            "tribunal francês reconheceu Márcia Ferreira e José Ari como autores da versão em português."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Lambada_(song)",
            "Overall, \"Lambada\" sold five million copies worldwide in 1989 alone, according to the New York Times. [...] "
            "Kaoma's Lambada was an unauthorized version of the song \"Llorando se fue\", originally composed, performed and recorded by the Bolivian Andean folk group Los Kjarkas in 1981. "
            "The song's lyrics and music had been lawfully registered by the founding members of Los Kjarkas, Gonzalo and Ulises Hermosa [...] "
            "Their song was written in a sad and slow Afro-Bolivian Saya rhythm. "
            "In 1984, an upbeat version of \"Llorando se fue\", introducing the accordion, was released by the Peruvian group Cuarteto Continental [...] "
            "The first Portuguese version of \"Llorando se fue\" – as \"Chorando Se Foi\" – was released by Brazilian singer Márcia Ferreira in 1986 on her third album. "
            "In March 1988, during their visit to Porto Seguro, Bahia, Brazil, French managers Olivier Lamotte d'Incamps (known as Olivier Lorsac) and Jean Georgakarakos (known as Jean Karakos) discovered the lambada music genre, and Márcia Ferreira's version. "
            "The two bought the musical rights to over 400 lambada songs from the Brazilian music publisher Continental. "
            "Lorsac and Georgakarakos then returned to Paris, and eventually the two formed the band Kaoma in France, which included musicians from Brazil, Africa and the Caribbean. [...] "
            "Kaoma released the song on July 1989. "
            "In the Kaoma single version and on the album Worldbeat, the composition of the music and the writing of the lyrics was credited to a fictional composer called Chico de Oliveira, in addition to making significant changes to Márcia Ferreira's lyrics. [...] "
            "The unauthorized cover by Kaoma resulted in successful lawsuits for plagiarism, the first being in 1990 by Los Kjarkas, against Kaoma's producer Jean-Claude Bonaventure, and the second in 1991, where a French court ruled that co-writers Márcia Ferreira and José Ari were the authors of the Portuguese version",
            nome="Lambada (song)")],
    },
    # 10 Tropicália: vaiada pela esquerda, presa pela ditadura
    {
        "temas_secundarios": ["brasil_republica", "guerra_fria"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Em 1968, Caetano Veloso foi vaiado por estudantes de esquerda, que viam no tropicalismo uma rendição à cultura pop americana e britânica. No fim daquele ano, ele e Gilberto Gil foram presos pela ditadura.",
        "explicacao": (
            "Os tropicalistas, vindos da Bahia, rejeitavam os dois nacionalismos da época: o patriotismo conservador "
            "dos militares e o anti-imperialismo da esquerda. O interesse deles pela psicodelia dos Beatles irritava "
            "estudantes de inspiração marxista, que defendiam formas musicais \"tradicionais\" brasileiras e viam ali "
            "a contaminação da cultura capitalista ocidental. A tensão estourou em 12 de setembro de 1968, no "
            "terceiro Festival Internacional da Canção, no auditório da universidade católica do Rio. Caetano entrou "
            "de túnica de plástico verde, com fios elétricos e colares de dentes de animais, acompanhado dos Mutantes "
            "em trajes igualmente extravagantes. Veio uma descarga de música psicodélica em volume alto, e a plateia "
            "respondeu com gritos, xingamentos e vaias. Do outro lado, o regime militar também via o movimento com "
            "desconfiança. Em 27 de dezembro de 1968, Caetano e Gil foram presos pelo conteúdo político de sua obra. "
            "Soltos dois meses depois, foram forçados ao exílio em Londres, de onde só voltaram em 1972. Na canção "
            "\"Tropicália\", de 1968, Caetano cita Carmen Miranda, que a geração de Caetano rejeitava e "
            "o movimento resgatou como alegoria do Brasil visto de fora."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Tropicália",
            "The movement was begun by a group of musicians from Bahia [...] "
            "The tropicalists' rejection of both sides' version of nationalism (the military's conservative patriotism and the ineffectual bourgeois anti-imperialism) was met with criticism and harassment. [...] "
            "The tropicalistas' passionate interest in the new wave of American and British psychedelic music of the period - most notably the work of the Beatles - also put them at odds with Marxist-influenced students on Brazil's left, whose aesthetic agenda was strongly nationalistic, and oriented towards 'traditional' Brazilian musical forms. "
            "This leftist faction vigorously rejected anything - especially tropicalismo - which they perceived as being tainted by the corrupting influences of Western capitalist popular culture. "
            "The politico-artistic tensions between leftist students and the tropicalistas reached a climax in September 1968, with Caetano Veloso's watershed performances at the third International Song Festival, held in the auditorium of Rio's Catholic University, where the audience not surprisingly included a large contingent of left-wing students. [...] "
            "In the first round of the competition on 12 September, Veloso was initially greeted by enthusiastic applause, but the mood quickly changed when the music started. "
            "Veloso came on dressed in a bright green plastic tunic, festooned with electrical wires and necklaces strung with animal teeth, and his backing band Os Mutantes were also dressed in similarly outlandish attire. "
            "The ensemble launched into a barrage of psychedelic music, played at high volume, and Veloso further outraged the students with his overtly sexual stage movements. "
            "The crowd reacted angrily, shouting abuse at the performers and booing loudly [...] "
            "On December 27, 1968, Veloso and Gil were arrested and imprisoned by the military government over the political content of their work. "
            "After two months, the two were released and subsequently forced to seek exile in London, where they lived and resumed their musical careers until they were able to return to Brazil in 1972. [...] "
            "This widespread interest attracted the attention and suspicion of the military, who feared tropicália's influence of protest in the cultural realm. [...] "
            "In Caetano Veloso's 1968 song \"Tropicália\", the musician references Carmen Miranda whose vulgar iconography were an inspiration. "
            "Caetano Veloso has said Carmen Miranda was a \"culturally repulsive object\" for his generation. "
            "Scholar Christopher Dunn says that by embracing Carmen, Veloso treats her as \"an allegory of Brazilian culture and its reception abroad\".",
            nome="Tropicália")],
    },
    # 11 Julinho da Adelaide, o compositor inventado por Chico Buarque
    {
        "temas_secundarios": ["brasil_republica", "espionagem"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Para driblar a censura, implacável com qualquer música que trouxesse seu nome, Chico Buarque inventou um compositor, Julinho da Adelaide. O personagem chegou a ter carteira de identidade e a dar entrevista a um jornal.",
        "explicacao": (
            "Na ditadura militar, Chico Buarque já tinha visto \"Apesar de Você\" e \"Cálice\" serem proibidas, e o "
            "nome dele nos créditos bastava para atrair a atenção dos censores. A saída foi criar outro autor. Julinho "
            "da Adelaide assinou só três canções: \"Milagre Brasileiro\", \"Acorda Amor\" e \"Jorge Maravilha\". Não "
            "era um simples pseudônimo: para dar ares de verdade à farsa, o compositor fictício ganhou cédula de "
            "identidade e até concedeu uma entrevista a um jornal da época. A censura daqueles anos rendia episódios "
            "quase cômicos. Com \"Flor da Idade\", os censores liberaram a música dentro de um filme proibido para "
            "menores, mas não no disco da trilha, vendido à parte, por medo de \"perder o controle\" sobre sua "
            "difusão. Eles leram na paráfrase do poema \"Quadrilha\", de Drummond, apologia da homossexualidade e do "
            "incesto. E, em 20 de outubro de 1974, um general da Polícia Federal proibiu a peça \"Calabar\", de Chico "
            "e Ruy Guerra, proibiu o próprio nome \"Calabar\" e proibiu que a proibição fosse divulgada."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Julinho_da_Adelaide",
            "teve suas canções Apesar de você (que dizem ser uma alusão negativa ao presidente Emílio Garrastazu Médici, mas que Chico sustenta ser em referência à situação) e \"Cálice\" proibidas pela censura brasileira. "
            "Adotou o pseudônimo de Julinho da Adelaide, com o qual publicou apenas três canções: Milagre Brasileiro, Acorda amor e Jorge Maravilha. [...] "
            "Julinho da Adelaide, aliás, não era só um pseudônimo, mas sim a forma que o compositor encontrou para driblar a censura, então implacável ao perceber seu nome nos créditos de uma música. "
            "Para completar a farsa e dar-lhe ares de veracidade, Julinho da Adelaide chegou a ter cédula de identidade e até mesmo a conceder entrevista a um jornal da época. [...] "
            "No mesmo filme, figurou \"Flor da Idade\", música que a censura chegou a liberar para o filme em si, proibido para menores, mas não para a trilha sonora lançada separadamente, pois o órgão temia \"perder o controle\" sobre sua difusão. "
            "Os censores interpretaram a parte final da letra, que parafraseia o poema \"Quadrilha\" de Carlos Drummond de Andrade, como uma apologia à homossexualidade (\"Pedro que amava Beto que amava Juca\" / \"Lea que amava Lia\") e ao incesto (\"Pedro que amava a filha\"). [...] "
            "Calabar: o Elogio da Traição, foi escrita no final de 1973, em parceria com o cineasta Ruy Guerra [...] "
            "em 20 de outubro de 1974, o general Antônio Bandeira, da Polícia Federal, sem motivo aparente, proibiu a peça, proibiu o nome \"Calabar\" e proibiu que a proibição fosse divulgada.",
            nome="Chico Buarque (seção sobre Julinho da Adelaide)", idioma="pt")],
    },
    # 12 o Corta-Jaca no Palácio do Catete
    {
        "temas_secundarios": ["brasil_republica", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1914, a primeira-dama Nair de Teffé tocou ao violão, no Palácio do Catete, o maxixe \"Corta-Jaca\", de Chiquinha Gonzaga. Ritmo popular na sede do governo virou escândalo, e Rui Barbosa o atacou em discurso.",
        "explicacao": (
            "Chiquinha Gonzaga compôs \"Corta-Jaca\" em 1895, para uma opereta burlesca. Quando a primeira-dama a "
            "tocou num sarau do palácio presidencial, setores conservadores viram ali uma afronta às convenções, e o "
            "senador Rui Barbosa classificou a música como exemplo da \"vulgarização dos costumes\". A própria "
            "compositora vivia na contramão. Casada aos 16 anos com um oficial da Marinha escolhido pelo pai, "
            "deixou o marido, o que na época era escândalo, e o pai passou a considerá-la morta: o nome dela não podia "
            "ser dito em casa. Quando ela contratou um garoto para vender suas partituras pela cidade, parentes "
            "chegavam a rasgá-las. Mesmo no leito de morte, o pai se recusou a recebê-la. Chiquinha seguiu em frente. "
            "Estreou como maestrina em 1885, causando embaraço num meio dominado por homens, e em 1899 compôs \"Ó "
            "Abre Alas\", considerada a primeira canção carnavalesca brasileira. Em 1917, cansada de ver suas músicas "
            "usadas sem permissão, fundou a Sociedade Brasileira de Autores Teatrais, pioneira na defesa dos direitos "
            "autorais no país."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Chiquinha_Gonzaga",
                "Seu pai considerou Chiquinha morta e seu nome era impronunciável dentro de casa. [...] "
                "Quando Chiquinha contratou um garoto para vender suas músicas pela cidade, o nome Gonzaga se espalhou rapidamente. "
                "Muitas vezes o garoto voltava com a mercadoria danificada, pois pessoas da família de Chiquinha rasgavam suas composições quando o viam. [...] "
                "Só em 1885 ela conseguiu enfim estrear como maestrina, o que causou um embaraço em jornalistas, atores, empresários e o maestro diretor da orquestra, por ver uma mulher em um reduto típico de homens. [...] "
                "Em 1895, ela compôs a canção Corta Jaca, integrante da opereta burlesca Zizinha Maxixe. "
                "Anos mais tarde, em 1914, a obra esteve no centro de uma controvérsia política quando a primeira-dama do Brasil, Nair de Teffé, a executou ao violão em um sarau no Palácio do Catete, então sede da Presidência da República. "
                "A apresentação, que levou um ritmo popular aos salões da elite, foi interpretada por setores conservadores como uma afronta às convenções da época e motivou severas críticas ao governo. "
                "O episódio ganhou grande repercussão após o discurso do senador Rui Barbosa, que condenou publicamente a execução da música, classificando o Corta Jaca como exemplo da “vulgarização dos costumes”. [...] "
                "Chiquinha sempre quis se reconciliar com o pai e esperava que no leito de morte talvez ele a perdoasse. [...] "
                "Mas, ressentido, Basileu disse que sua filha Chiquinha estava morta havia muito tempo. [...] "
                "Surgiu assim Ó Abre Alas, a primeira canção carnavalesca brasileira, que nascia como marcha-rancho.",
                nome="Chiquinha Gonzaga", idioma="pt"),
            wiki("Chiquinha_Gonzaga",
                "In 1863, at age 16, Francisca married Jacinto Ribeiro do Amaral, a young man of 24 and an official of the Imperial Navy. [...] "
                "Jacinto do Amareal was chosen by her father to marry Chiquinha even though she had expressed her disagreement with this arranged marriage. [...] "
                "Chiquinha left her husband and asked for divorce, a scandal at the time. [...] "
                "author of the first carnival march, \"Ó Abre Alas\" (1899). [...] "
                "Due to the popularity of her music, many people began to use her music and content without permission. "
                "Their abuse of her work as a musician led to Chiquinha founding the Brazilian Society of Theater Authors in 1917, which was the first society put into place to copyright and protect works by Brazilian artists.",
                nome="Chiquinha Gonzaga"),
        ],
    },
    # 13 Cornélio Pires bancou os primeiros discos caipiras
    {
        "temas_secundarios": ["economia_curiosa", "invencoes"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "A música caipira estreou em disco por conta própria: em 1929, o escritor Cornélio Pires financiou a gravação de duplas do interior paulista e distribuiu ele mesmo as 25 mil cópias. O sucesso atraiu as gravadoras.",
        "explicacao": (
            "Cornélio Pires, de Tietê, era jornalista e escritor, e nos anos 1920 virou um dos autores mais vendidos "
            "do país. Em 1929, decidiu bancar, junto à representante da gravadora Columbia no Brasil, a gravação de "
            "músicas de duplas caipiras. Segundo um estudo publicado pela Unicamp, o material saiu em cinco discos, "
            "com 25 mil cópias que o próprio Cornélio distribuiu pelo interior de São Paulo. A primeira tiragem se "
            "esgotou depressa, apesar de os discos "
            "custarem dois mil-réis a mais que os outros da mesma gravadora. Foi o que despertou o interesse comercial "
            "das grandes companhias pelo gênero, ponto de partida do que se chamaria música sertaneja. O sociólogo "
            "José de Souza Martins vê nessa passagem uma transformação. A música caipira original vinha sempre ligada "
            "a algum ritual de religião, de trabalho ou de lazer, como as folias do Divino e a catira. Ao virar "
            "produto da indústria do disco, ela perdeu esse vínculo e se tornou mercadoria. Uma das primeiras músicas "
            "sertanejas, a \"Moda do bonde camarão\", já fazia uma ironia ferina sobre o mundo moderno."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": UNICAMP_CAIPIRA,
             "titulo": "A Música Caipira e o advento do disco (João Paulo do Amaral Pinto, IA-Unicamp)",
             "idioma": "pt",
             "trecho": (
                "Cornélio Pires decidiu financiar junto a Byington & Company (representante da Columbia) a gravação pioneira de músicas caipiras de duplas do interior paulista. "
                "Os registros foram agrupados em cinco discos, to talizando 25.000 cópias esgotadas rapidamente na primeira tiragem distribuída pelo próprio Cornélio por todo interior paulista. "
                "A repercussão favorável da venda dos discos, que inclusive eram vendidos a dois mil reis mais caros que os outros da mesma gravadora, despertou o interesse comercial das gravadoras da época para este tipo de música. [...] "
                "a indústria fo nográfica passou a se interessar por este filão, iniciando o chamado segmento de música sertaneja. "
                "O professor José de Souza Martins fez a distinção entre música caipira e música sertaneja apontando que a primeira é sempre acompanhada de “algum ritual de religião, de trabalho ou de lazer”, e a segunda, ao ser apropriada pela indústria do disco, perde esse vínculo ao converter-se num produto, numa “mercadoria”"
             )},
            wiki("Cornélio_Pires",
                "Cornélio Pires (13 July 1884 – 17 February 1958) was a Brazilian journalist, writer, composer, film director, and folklorist. [...] "
                "At the age of 17, he left his hometown Tietê and moved to São Paulo [...] "
                "During the 1920s, Cornélio had his highest success in his writing career with As Estrambóticas Aventuras de Joaquim Bentinho. "
                "The book was so successful that Pires became one of Brazil's best-selling authors at that time. "
                "Cornélio Pires released 78 rpm records of Caipira music recordings, as opposed to sertanejo music, in 1929.",
                nome="Cornélio Pires"),
            wiki("Cornélio_Pires",
                "a música caipira é originalmente música litúrgica do catolicismo popular, presente nas folias do Divino, no cateretê e na catira [...] "
                "O melhor exemplo disso é a \"Moda do bonde camarão\", uma das primeiras músicas sertanejas e uma ferina ironia sobre o mundo moderno.",
                nome="Cornélio Pires", idioma="pt"),
        ],
    },
    # 14 João Gilberto e os dois microfones
    {
        "temas_secundarios": ["acustica", "musica_ciencia"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "O canto quase falado de João Gilberto tem lógica técnica. Ao gravar \"Chega de Saudade\", ele pediu um microfone para a voz e outro para o violão, contra o costume, e cantou baixo para não encobrir o instrumento.",
        "explicacao": (
            "Em 1955, João foi para Porto Alegre e, oito meses depois, para Diamantina, Minas Gerais, morar com a "
            "irmã recém-casada. Nos estudos daqueles meses, percebeu que, se cantasse mais baixo e sem vibrato, podia "
            "adiantar ou atrasar a voz em relação ao ritmo, desde que a batida do violão continuasse constante. Depois "
            "de sete meses ali, foi para Juazeiro, onde compôs \"Bim Bom\", e no início de 1957 chegou ao Rio. Em "
            "1958, acompanhou Elizeth Cardoso em duas faixas que são as primeiras gravações da batida da bossa nova, e "
            "em agosto lançou o 78 rotações com \"Chega de Saudade\" e \"Bim Bom\". Ali entrou a ideia dos dois "
            "microfones, que chocou os produtores. Até então, gravava-se com um só, que privilegiava a voz e deixava o "
            "violão em segundo plano, já que o instrumento tem volume modesto. Com um microfone para cada fonte, voz e "
            "violão podiam disputar de igual para igual, desde que a voz ficasse num volume próximo ao da fala comum, "
            "pois qualquer exagero encobriria o violão. Daí o canto contido, sem vibrato e sem fortíssimos, que virou "
            "marca do gênero."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("João_Gilberto",
                "Em 1955, João dirigiu-se a Porto Alegre, no Rio Grande do Sul, com seu amigo Luís Telles. [...] "
                "Depois de oito meses, João decidiu se dirigir a Diamantina, Minas Gerais, para viver com a irmã Dadainha, recém-casada e com uma filha recém-nascida. "
                "Durante os estudos, João percebeu que, se cantasse mais baixo, sem vibrato, poderia adiantar ou atrasar o canto em relação ao ritmo, desde que a batida fosse constante, criando assim seu próprio tempo. "
                "Depois de sete meses em Diamantina, João partiu para Juazeiro, onde passou dois meses com a família. "
                "Lá, compôs \"Bim Bom\", confiante de que havia encontrado a batida que queria. [...] "
                "No início de 1957, João Gilberto partiu para o Rio de Janeiro, para sua consagração. [...] "
                "João inovou na gravação do Chega de Saudade ao pedir dois microfones, um para a voz e outro para o violão. "
                "O motivo é óbvio, apesar do choque que causou nos produtores do disco. "
                "Até então, gravava-se com apenas um microfone, com destaque para a voz em detrimento do violão. "
                "Além disso, é da própria natureza acústica do violão ficar restrito, em termos de volume de som, com qualquer instrumento de orquestra ou com o piano. "
                "Com a voz, o violão pode concorrer de igual, se a voz se mantiver numa intensidade natural, pois com qualquer elevação de volume da voz já há um encobrimento do violão. "
                "Desse modo, é necessária a emissão da voz num volume próximo à da fala comum. [...] "
                "Entre as várias técnicas que usava, estão a ausência de vibratos [...] a retirada do forte e do fortíssimo da dinâmica",
                nome="João Gilberto", idioma="pt"),
            wiki("João_Gilberto",
                "In July 1958, Elizete Cardoso released the famous LP, Canção do Amor Demais, containing songs by Tom Jobim and Vinicius de Moraes. [...] "
                "Gilberto accompanied Cardoso on guitar on the tracks \"Chega de Saudade\" and \"Outra Vez\", these being the first recordings of the so-called \"bossa nova beat\". "
                "In August of that year, Gilberto released a 78 rpm record containing \"Chega de Saudade\" and \"Bim Bom\"",
                nome="João Gilberto"),
        ],
    },
]
