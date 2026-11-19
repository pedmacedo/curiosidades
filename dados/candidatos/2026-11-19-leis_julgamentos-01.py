LOTE = "2026-11-19-leis_julgamentos-01"
AREA = "sociedade"
TEMA = "leis_julgamentos"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


SENADO_1876 = "https://www12.senado.leg.br/noticias/materias/2016/04/04/ha-140-anos-a-ultima-pena-de-morte-do-brasil"

CANDIDATOS = [
    # 1 porcos enforcados e ratos com advogado
    {
        "temas_secundarios": ["europa_medieval", "comportamento_animal"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Na Europa medieval, animais iam a julgamento de verdade. Em 1386, em Falaise, um porco que matou uma criança sofreu as mesmas mutilações e foi enforcado. E ratos acusados por um tribunal da Igreja ganharam defensor.",
        "explicacao": (
            "Há registros de processos contra animais na Europa do século XIII ao XVIII, sobretudo na França, "
            "tanto em tribunais civis quanto em tribunais da Igreja. O rito imitava o dos processos de pessoas: "
            "havia acusação, testemunhas eram ouvidas e, nos tribunais eclesiásticos, os bichos tinham advogado. "
            "A justiça civil cuidava de animais domésticos, como porcos, touros e cavalos, que tinham ferido ou "
            "matado alguém. Os porcos eram réus frequentes, porque viviam no meio das pessoas e podiam ser "
            "perigosos para crianças pequenas: um levantamento achou 15 casos de porcos executados por matar "
            "crianças entre os séculos XIII e XVI. A execução era pública, feita por carrasco profissional, e às "
            "vezes o animal era vestido com roupas de gente. Já as pragas, como lagartas, toupeiras e "
            "sanguessugas, iam a tribunais da Igreja, que buscavam condená-las e fazê-las ir embora. O jurista "
            "francês Bartholomé Chassenée defendeu com sucesso os ratos de Autun, que não tinham atendido à "
            "intimação: argumentou que eles faltaram porque temiam pela própria vida e conseguiu mais prazo. "
            "Animais selvagens, como lobos e ursos, nunca eram processados. E havia críticos desde aquela época: "
            "Tomás de Aquino escreveu que animais não podem ser sujeitos da lei, porque não entendem palavras nem "
            "pensam racionalmente."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Animal_trial",
            "Records of such trials show that they took place in Europe from the thirteenth to the eighteenth century. [...] "
            "In the thirteenth to the twentieth century, \"animal trials were held in many European regions, especially in France [...] "
            "The animal species involved were almost invariably either domesticated ones (most often pigs, bulls, horses, donkeys, mules and cows, for secular courts) or pests such as rats and weevils for ecclesiastical courts. "
            "In contrast, \"wild beasts, like wolves or bears, were never subject to such legal action [...] "
            "Human witnesses were often heard, and in ecclesiastical courts the animals were provided with lawyers [...] "
            "The carrying out of sentences was solemn and public and was usually performed by professional executioners. [...] "
            "Sometimes the animal was dressed in human attire prior to being killed. [...] "
            "a pig that killed a child in the Norman city of Failaise in 1386 and, in so doing, mutilated its face and arms, was subjected to the same mutilations prior to being hung. [...] "
            "including caterpillars, flies, moles, worms, snails, and leeches. The objective of these trials was to find the pests guilty and to cause them to leave. [...] "
            "Pigs were often the target of criminal cases because they lived amongst humans and could be dangerous, especially for young children. "
            "An inventory of such cases between from the thirteenth to the sixteenth century finds 15 cases where pigs were executed for killing children. [...] "
            "A notable French jurist, Bartholomé Chassenée (1480-1542), successfully defended the rats of Autun through various largely procedural arguments. "
            "He won an extension for the rats (who had failed to honour a summons and appear in ecclesiastical court) by arguing that they did so because they feared for their lives. [...] "
            "Thomas Aquinas asserts in Summa Theologiae that animals are not subjects of law because they cannot understand words or think rationally.",
            nome="Animal trial")],
    },
    # 2 o Sínodo do Cadáver
    {
        "temas_secundarios": ["religioes", "europa_medieval"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Em 897, o papa Estêvão VI mandou desenterrar o papa Formoso, morto havia uns nove meses, sentou o cadáver num trono e o julgou. O morto foi condenado. Meses depois, quem o julgou foi estrangulado na prisão.",
        "explicacao": (
            "O episódio ficou conhecido como Sínodo do Cadáver e aconteceu por volta de janeiro de 897, na "
            "Basílica de São João de Latrão, em Roma. Era uma época de grande instabilidade: entre 896 e 904, "
            "houve em média um papa novo por ano, e em geral se presume que o julgamento teve motivação política. "
            "Com o corpo apoiado no trono, um diácono foi designado para responder pelo morto. As acusações "
            "retomavam brigas antigas: Formoso teria cometido perjúrio, trocado de diocese contra as regras da "
            "Igreja e servido como bispo sendo na verdade um leigo. Declarado culpado, o cadáver perdeu as vestes "
            "papais e, segundo o cronista Liutprando de Cremona e outras fontes, os três dedos da mão direita "
            "usados para abençoar. Todos os atos de Formoso foram anulados, e o corpo acabou amarrado a pesos e "
            "jogado no rio Tibre. O espetáculo virou a opinião pública contra Estêvão: uma revolta o depôs e o "
            "prendeu, e ele foi estrangulado na cadeia em julho ou agosto de 897. Em dezembro, o papa seguinte "
            "anulou o sínodo e mandou sepultar Formoso de novo, na Basílica de São Pedro. Em 898, outros sínodos "
            "mandaram destruir as atas do julgamento e proibiram que qualquer cadáver voltasse a ser julgado."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Cadaver_Synod",
            "the ecclesiastical trial of Pope Formosus, who had been dead for about nine months, in the Basilica of St. John Lateran in Rome during January 897. [...] "
            "Between 872 and 965, two dozen popes were appointed, and between 896 and 904 there was, on average, a new pope every year. [...] "
            "The Cadaver Synod is generally presumed to have been politically motivated. [...] "
            "Probably around January 897, Stephen VI ordered that the corpse of his predecessor Formosus be removed from its tomb and brought to the papal court for judgment. "
            "With the corpse propped up on a throne, a deacon was appointed to answer for the deceased pontiff. "
            "Formosus was accused of transmigrating sees in violation of canon law, of perjury, and of serving as a bishop while actually a layman. [...] "
            "Eventually, the corpse was found guilty. Liutprand of Cremona and other sources say that, after having the corpse stripped of its papal vestments, Stephen then cut off the three fingers of the right hand (the blessing fingers), next formally invalidating all of Formosus's acts and ordinations [...] "
            "to be dug up once again, tied to weights, and cast into the Tiber River. [...] "
            "The macabre spectacle excited a tumult and turned public opinion in Rome against Stephen. [...] "
            "A public uprising deposed and imprisoned Stephen. He was strangled in prison in July or August 897. "
            "In December 897 Pope Theodore II (897) convened a synod that annulled the Cadaver Synod, rehabilitated Formosus, and ordered that his body, which had been recovered from the Tiber, be reburied in Saint Peter's Basilica in pontifical vestments. "
            "In 898, John IX (898–900) also nullified the Cadaver Synod, convening one synod in Rome, and another in Ravenna. "
            "The two synods, which affirmed the findings of Theodore II's synod, ordered the acta of the Cadaver Synod destroyed, excommunicated seven cardinals involved in the Cadaver Synod, and prohibited any trial of a corpse in the future.",
            nome="Cadaver Synod")],
    },
    # 3 o ordálio que talvez funcionasse
    {
        "temas_secundarios": ["europa_medieval", "decisoes_economia", "teoria_jogos"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "No ordálio medieval, o acusado segurava ferro em brasa e era inocente se a ferida sarasse. Uma teoria econômica diz que isso separava bem culpados e inocentes: quem tinha culpa e temia a Deus confessava antes.",
        "explicacao": (
            "O ordálio era tido como um juízo de Deus: partia da premissa de que Deus faria um milagre para "
            "ajudar o inocente. Na prova do fogo, o acusado andava sobre relhas de arado em brasa ou segurava um "
            "ferro quente. O mais comum era a ferida ser enfaixada e examinada três dias depois por um padre, que "
            "declarava se Deus a tinha curado ou se ela estava infeccionando. Parece um sorteio cruel, mas o "
            "economista Peter Leeson propôs que o sistema podia funcionar. Se os réus acreditavam na intervenção "
            "divina, só os inocentes topariam a prova, e os culpados confessariam ou fariam acordo. Com isso, as "
            "autoridades da Igreja e da justiça podiam manipular a prova para que os participantes, "
            "presumivelmente inocentes, passassem. Como indícios, Leeson aponta a ampla liberdade dos padres para "
            "conduzir e interpretar o ordálio e a alta taxa de absolvição, quando seria de esperar que quase todo "
            "mundo que carregasse ferro em brasa se queimasse feio. Um relato do cronista Eadmer vai na mesma "
            "linha: o rei inglês Guilherme II duvidou do método depois que 50 homens acusados de crimes nas "
            "florestas reais foram inocentados pelo ferro quente. Há outras leituras: o historiador Peter Brown vê "
            "o ordálio como um jeito de produzir consenso numa sociedade de convívio apertado e pouco poder central. "
            "Em 1215, o Quarto Concílio de Latrão proibiu os clérigos de participar dos ordálios, e os registros "
            "judiciais ingleses não têm nenhum caso depois de 1219."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Trial_by_ordeal",
            "a procedure based on the premise that God would help the innocent by performing a miracle on their behalf. [...] "
            "In Europe, the ordeal typically required that the accused walk a certain distance, usually 9 feet (2.7 metres) or a certain number of paces, usually three, over red-hot plowshares or holding a red-hot iron. "
            "Innocence was sometimes established by a complete lack of injury, but it was more common for the wound to be bandaged and re-examined three days later by a priest. "
            "It would either be pronounced that God had intervened to heal the wound, or that it was festering [...] "
            "In a famous story from Eadmer's Historia novorum in Anglia, William Rufus expresses skepticism about the ordeal after 50 men accused of forest offenses were exonerated by the ordeal of hot iron. [...] "
            "In 1215, clergy were forbidden to participate in ordeals by the Fourth Lateran Council. "
            "The English plea rolls contain no cases of trial by ordeal after 1219 [...] "
            "According to a theory put forward by economics professor Peter Leeson, trial by ordeal may have been effective at sorting the guilty from the innocent. "
            "On the assumption that defendants were believers in divine intervention for the innocent, then only the truly innocent would choose to endure a trial; guilty defendants would confess or settle cases instead. "
            "Therefore, the theory goes, church and judicial authorities could routinely rig ordeals so that the participants—presumably innocent—could pass them. "
            "To support this theory, Leeson points to the great latitude given to the priests in administering the ordeal and interpreting the results of the ordeal. "
            "He also points to the overall high exoneration rate of accused persons undergoing the ordeal, when intuitively one would expect a very high proportion of people carrying a red hot iron to be badly burned and thus fail the ordeal. "
            "Peter Brown explains the persistence and eventual withering of the ordeal by stating that it helped promote consensus in a society where people lived in close quarters and there was little centralized power.",
            nome="Trial by ordeal")],
    },
    # 4 o "verso do pescoço"
    {
        "temas_secundarios": ["europa_medieval", "religioes", "expressoes"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "Por séculos, na Inglaterra, um condenado podia escapar da forca lendo um versículo da Bíblia, como se fosse clérigo. Muitos analfabetos decoravam o trecho, que ganhou o apelido de \"verso do pescoço\".",
        "explicacao": (
            "O benefício do clero nasceu como privilégio da Igreja: clérigos acusados de crimes podiam pedir para "
            "ser julgados por tribunais eclesiásticos, vistos como bem mais brandos que os do rei. No começo, era "
            "preciso se apresentar com tonsura e roupa religiosa. Com o tempo, a prova virou um teste de leitura "
            "de um trecho da Bíblia em latim, e em 1351 uma lei estendeu o benefício a todos que soubessem ler. O "
            "trecho tradicional era o terceiro versículo do Salmo 51, o \"Miserere mei, Deus\", um pedido de "
            "piedade a Deus. Quem o decorasse passava no teste sem saber ler, e ele ficou conhecido como \"verso "
            "do pescoço\", porque salvava o pescoço da corda. Os juízes usavam o benefício como forma de clemência: "
            "na Inglaterra elisabetana, chegavam a concedê-lo a mais de 90% dos réus que podiam pedi-lo, muito "
            "acima da taxa de alfabetização da época. Para conter os abusos, a partir de 1488 quem não provasse ser "
            "clérigo tinha o polegar marcado a ferro, o que o impedia de usar o recurso de novo. O dramaturgo Ben "
            "Jonson escapou da forca assim em 1598, e os dois soldados condenados por homicídio no Massacre de "
            "Boston, em 1770, também, com marca no polegar. O mecanismo só foi abolido em 1827."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Benefit_of_clergy",
            "clergymen accused of a crime could claim that they were outside the jurisdiction of the secular courts and be tried instead in an ecclesiastical court under canon law. "
            "The ecclesiastical courts were generally seen as being more lenient in their prosecutions and punishments [...] "
            "The legal mechanism was abolished in the United Kingdom in 1827 with the passage of the Criminal Law Act 1827. [...] "
            "At first, to plead the benefit of clergy, one had to appear before the court tonsured and otherwise wear an ecclesiastical dress. "
            "Over time, this proof of clergyhood was replaced by a literacy test: defendants demonstrated their clerical status by reading from the Latin Bible. [...] "
            "In 1351, under Edward III, this loophole was formalised in statute, and the benefit of clergy was officially extended to all who could read. "
            "For example, the English dramatist Ben Jonson avoided hanging by pleading benefit of clergy in 1598 when charged with manslaughter. "
            "In the British colony of Massachusetts, the two soldiers convicted of manslaughter in the 1770 Boston Massacre were spared execution under the benefit of clergy. "
            "Still, they underwent branding of their right thumbs [...] "
            "the Biblical passage traditionally used for the literacy test was, appropriately, the third verse of Psalm 51 [...] "
            "Miserere mei, Deus, secundum magnam misericordiam tuam [...] "
            "Thus, an illiterate person who had memorized the appropriate Psalm could also claim the benefit of clergy. "
            "Psalm 51:3 became known as the \"neck verse\" because knowing it could \"save one's neck\" [...] "
            "The benefit of clergy was commonly applied as a means of judicial mercy: in Elizabethan England, courts might allow more than 90% of clergyable offenders the benefit of clergy, which was far higher than the literacy rate of the period. [...] "
            "In 1488, Henry VII decreed that non-clergymen should be allowed to plead the benefit of clergy only once: those claiming the benefit of clergy but not able to prove through documentation of their holy orders that they were clergy members, were branded on the thumb, and the brand disqualified them from pleading the benefit of clergy in the future.",
            nome="Benefit of clergy")],
    },
    # 5 o deodand: o objeto culpado
    {
        "temas_secundarios": ["revolucao_industrial", "transportes", "europa_medieval"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Por séculos, a lei inglesa confiscava \"em nome de Deus\" o objeto que causasse uma morte: um cavalo, uma carroça e, no fim, até um trem. A regra só caiu em 1846, depois que júris passaram a usá-la contra as ferrovias.",
        "explicacao": (
            "O nome era deodand, do latim \"deo dandum\", \"a ser dado a Deus\". A regra remontava ao século XI: "
            "quando o júri de um legista concluía que um bem, como um cavalo ou um monte de feno, tinha causado a "
            "morte de alguém, o bem era declarado perdido para a Coroa, que em tese o venderia e usaria o dinheiro "
            "para fins piedosos. Na prática, o júri avaliava o objeto e o dono pagava uma multa no mesmo valor. As "
            "distinções eram curiosas: um cavalo em movimento que matasse alguém era confiscado; se a pessoa "
            "caísse de um cavalo parado, só contava se fosse adulta, e não uma criança. Nos anos 1830, a rápida "
            "expansão das ferrovias trouxe uma epidemia de mortes, e as famílias das vítimas não tinham direito a "
            "indenização pela perda emocional e econômica. Os júris então passaram a usar o deodand para punir as "
            "companhias. Na véspera do Natal de 1841, um trem bateu num deslizamento de terra e matou oito "
            "passageiros; o júri fixou um deodand de 1.000 libras para o trem. A multa foi derrubada na apelação, "
            "mas alertou os legisladores. O resultado foram duas leis de 1846: uma criou a indenização para "
            "famílias de vítimas de acidentes fatais e a outra aboliu o deodand."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Deodand",
            "In law, a  deodand is an object or instrument forfeited because it has caused a person's death. "
            "The English common law of deodands traces back to the 11th century and was applied, on and off, until Parliament abolished it in 1846. "
            "Under this law, a chattel (i.e. some personal property, such as a horse or a haystack) was considered a deodand whenever a coroner's jury decided that it had caused the death of a human being. "
            "In theory, deodands were forfeited to the Crown, which was supposed to sell the chattel and then apply the profits to some pious end. "
            "The term deodand derives from the Latin phrase deo dandum, which means 'to be given to God'. "
            "In reality, the juries who decided that a particular animal or object was a deodand also appraised its value, and the owners were expected to pay a fine equal to the value of the deodand. [...] "
            "If a horse or other animal in motion killed a person, whether infant or adult, or if a cart ran over him, it was forfeited as a deodand. "
            "On the other hand, if death were caused by falling from a cart or a horse at rest, the law made the chattel a deodand if the person killed were an adult, but not if he were below the years of discretion. [...] "
            "The rapid development of the railways during the 1830s saw an epidemic of railway deaths. [...] "
            "The families of fatal accident victims had no claim for purely emotional and economic loss. "
            "As a result, coroner's juries started to award deodands as a way of penalising the railways. "
            "On Christmas Eve 1841, in an accident on the Great Western Railway, a train ran into a landslip in Sonning Cutting and eight passengers were killed. "
            "The inquest jury assigned a deodand value of £1,000 to the train. "
            "Subsequently, a Board of Trade inspector exonerated the company from blame and the deodand was quashed on appeal, on technicalities. "
            "This alerted legislators [...] "
            "The bill led to the Fatal Accidents Act 1846, also known as Lord Campbell's Act. "
            "Campbell also introduced a bill to abolish deodands. The latter proposal, which became law as the Deodands Act 1846",
            nome="Deodand")],
    },
    # 6 a pena do saco
    {
        "temas_secundarios": ["roma_antiga", "mitologia"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Na Roma antiga, quem matasse o pai ou a mãe podia ser costurado num saco de couro junto com animais vivos, como um cão, uma cobra, um macaco e um galo, e jogado na água.",
        "explicacao": (
            "Era a \"poena cullei\", a pena do saco, reservada ao parricídio. A forma dela mudou muito ao longo "
            "dos séculos. O caso mais antigo bem documentado é de cerca de 100 a.C.: Publicius Malleolus, "
            "condenado por matar a mãe, teve a cabeça coberta por um saco de pele de lobo, foi envolto num saco de "
            "couro e lançado num rio, mas sem bicho nenhum. Os animais só aparecem nos registros no início do "
            "Império, e de começo só se falava em cobras. A versão mais famosa, com galo, cão, macaco e víbora, "
            "está documentada no tempo do imperador Adriano, no século II, quando a pena passou a ser opcional: a "
            "alternativa era ser jogado às feras na arena. O historiador Theodor Mommsen reuniu elementos citados "
            "por várias fontes ao longo de séculos, como o açoite, os tamancos de madeira e a carroça puxada por "
            "bois pretos até um rio ou o mar, e ele próprio notou que o macaco dificilmente era parte antiga do "
            "ritual. A pena saiu de uso no século III, foi revivida por Constantino só com serpentes e "
            "restabelecida por Justiniano com os quatro animais. Ainda houve ecos muito tardios: na Saxônia, na "
            "primeira metade do século XVIII, há casos documentados de condenados afogados num saco com animais "
            "vivos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Poena_cullei",
            "Poena cullei (Latin, 'penalty of the sack') under Roman law was a type of death penalty imposed on a subject who had been found guilty of parricide. "
            "The punishment consisted of being sewn up in a leather sack, with an assortment of live animals including a dog, snake, monkey, and a chicken or rooster, and then being thrown into water. "
            "The punishment may have varied widely in its frequency and precise form during the Roman period. "
            "For example, the earliest fully documented case is from ca. 100 BC [...] "
            "Inclusion of live animals in the sack is only documented from Early Imperial times, and at the beginning, only snakes were mentioned. "
            "At the time of Emperor Hadrian (2nd century AD), the best-known form of the punishment was documented, where a rooster, a dog, a monkey and a viper were inserted in the sack. "
            "At the time of Hadrian, poena cullei was made into an optional form of punishment for parricide (the alternative was being thrown to the beasts in the arena). "
            "During the 3rd century AD up to the accession of Emperor Constantine, poena cullei fell out of use; Constantine revived it, now with only serpents to be added in the sack. "
            "Well over 200 years later, Emperor Justinian reinstituted the punishment with the four animals [...] "
            "with late cases of being drowned in a sack along with live animals being documented from Saxony in the first half of the 18th century. [...] "
            "Mommsen, for example, notes that the monkey hardly can have been an ancient element in the execution ritual. "
            "The person was first whipped, or beaten, with virgis sanguinis (\"blood-colored rods\", probably) and his head was covered in a bag made of a wolf's hide. "
            "On his feet were placed clogs, or wooden shoes, and he was then put into the poena cullei, a sack made of ox-leather. [...] "
            "The sack was put on a cart, and the cart driven by black oxen to a running stream or to the sea. [...] "
            "\"He who has been convicted of murdering his parent shall be completely wrapped and bound in a leather sack and thrown in a running stream\"... "
            "Malleolus was convicted of matricide. Immediately after he had received sentence, his head was wrapped in a bag of wolf's hide [...] "
            "in this early reference, no mention is made of live animals as co-inhabitants within the sack",
            nome="Poena cullei")],
    },
    # 7 Richard Parker, de Poe ao bote do Mignonette
    {
        "temas_secundarios": ["literatura", "navegacao_antiga"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "Num romance de 1838, Edgar Allan Poe pôs náufragos famintos sacrificando um deles como comida, e um personagem chamado Richard Parker. Em 1884, náufragos de verdade mataram e comeram um grumete: Richard Parker.",
        "explicacao": (
            "O iate inglês Mignonette afundou em 1884, e os quatro tripulantes ficaram num bote sem provisões. "
            "Depois de quase três semanas no mar, Tom Dudley e Edwin Stephens decidiram matar o grumete Richard "
            "Parker, de 17 anos, que estava muito doente por ter bebido água do mar, para comê-lo. Os sobreviventes "
            "foram resgatados por um veleiro alemão e, de volta à Inglaterra, contaram tudo com franqueza: "
            "achavam que a necessidade de sobreviver justificava o canibalismo como último recurso. O tribunal "
            "discordou. O caso R v Dudley and Stephens firmou um precedente seguido em todo o mundo da common law: "
            "a necessidade não serve de defesa contra a acusação de homicídio. Os dois foram condenados à pena de "
            "morte prevista em lei, com recomendação de clemência, e a pena acabou trocada por seis meses de "
            "prisão. Até hoje o caso é ensinado a todos os estudantes de direito da Inglaterra e do País de Gales, "
            "e é padrão no primeiro ano das faculdades americanas. A coincidência com o romance de Poe, A "
            "Narrativa de Arthur Gordon Pym, foi apontada numa carta de leitor que o escritor Arthur Koestler "
            "publicou no Sunday Times em 1974. E o nome seguiu viajando: em As Aventuras de Pi, de 2001, Yann "
            "Martel batizou o tigre de Richard Parker em homenagem ao personagem de Poe."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("R_v_Dudley_and_Stephens",
                "is a leading English criminal case which established a precedent throughout the common law world that necessity is not a defence to a charge of murder. [...] "
                "In 1884, the four-man crew of the wrecked yacht Mignonette were cast adrift in a small lifeboat without provisions. "
                "After nearly three weeks at sea, and with little hope of rescue, two of the crew, Tom Dudley and Edwin Stephens, decided that in order to save their own lives they would need to kill and eat the ship's 17-year-old cabin boy Richard Parker, who by that time had fallen seriously ill after drinking seawater. "
                "The defendants were found guilty and were sentenced to the statutory death penalty, though with a recommendation of mercy. [...] "
                "Dudley, Stephens and Brooks were picked up by the German sailing barque Moctezuma [...] "
                "All three were candid, with Dudley and Stephens believing that their acts were justified by necessity – the need to ensure their own survival by practising cannibalism at sea as a last resort before starvation. [...] "
                "on 12 December, Harcourt decided on six months' imprisonment. [...] "
                "The case is one of a few criminal cases taught to all law students in England and Wales [...] "
                "It is also a standard legal case taught to first-year American law students [...] "
                "Yann Martel in Life of Pi (2001) named the shipwrecked Bengal tiger Richard Parker.",
                nome="R v Dudley and Stephens"),
            wiki("The_Narrative_of_Arthur_Gordon_Pym_of_Nantucket",
                "The Narrative of Arthur Gordon Pym of Nantucket, written and published in 1838, is the only complete novel by the American writer Edgar Allan Poe. [...] "
                "On May 5, 1974, author and journalist Arthur Koestler published a letter from reader Nigel Parker in The Sunday Times of a striking coincidence between a scene in Poe's novel and an actual event that happened decades later: "
                "In 1884, the yacht Mignonette sank, with four men cast adrift. "
                "After weeks without food, they decided that one of them should be sacrificed as food for the other three, just as in Poe's novel. "
                "The loser was a young cabin boy named Richard Parker, coincidentally the same name as Poe's fictional character. [...] "
                "Yann Martel named a character in his Booker Prize-winning novel Life of Pi (2001) after Poe's fictional character, Richard Parker.",
                nome="The Narrative of Arthur Gordon Pym of Nantucket"),
        ],
    },
    # 8 a bola de fumaça e as 100 libras
    {
        "temas_secundarios": ["historia_medicina", "economia_curiosa"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Em 1891, uma empresa prometeu 100 libras a quem pegasse gripe depois de usar sua \"bola de fumaça\". Uma mulher usou, pegou gripe e cobrou. A Justiça lhe deu razão, e o caso virou lição básica de direito.",
        "explicacao": (
            "A bola de fumaça carbólica era uma bola de borracha com um tubo, cheia de ácido carbólico, hoje "
            "chamado fenol: o tubo ia no nariz, e a pessoa apertava a bola para soltar os vapores. O anúncio, "
            "publicado em novembro de 1891, dizia ainda que a empresa tinha depositado 1.000 libras num banco para "
            "provar sua sinceridade. Louisa Carlill comprou uma, usou três vezes por dia por quase dois meses e "
            "pegou gripe em 17 de janeiro de 1892. A empresa ignorou duas cartas do marido dela, que era advogado, "
            "e depois alegou que não tinha feito nenhuma oferta com valor legal. O Tribunal de Apelação rejeitou "
            "os argumentos por unanimidade: o anúncio era uma oferta a quem cumprisse as condições, e usar a bola "
            "valia como aceitação, formando um contrato. Por isso, Carlill v Carbolic Smoke Ball Company costuma "
            "ser um dos primeiros casos que estudantes de direito estudam na matéria de contratos. A empresa não "
            "afundou de imediato: o dono criou uma nova companhia e publicou outro anúncio dizendo que só três "
            "pessoas tinham pedido o prêmio, prova de que o remédio funcionava, e agora oferecia 200 libras. O "
            "advogado que perdeu o caso pela empresa na primeira instância, H. H. Asquith, viria a ser "
            "primeiro-ministro do Reino Unido. Louisa viveu até os 96 anos. Morreu em 1942, segundo o médico, "
            "principalmente de velhice, mas outra causa foi anotada: gripe."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Carlill_v_Carbolic_Smoke_Ball_Co",
            "Carlill is frequently discussed as an introductory contract case, often one of the first cases a law student studies in the law of contract. [...] "
            "The smoke ball was a rubber ball with a tube attached. It was filled with carbolic acid (now known as phenol). "
            "The tube would be inserted into a user's nose and the ball would be squeezed at the bottom to release the vapours. "
            "The Company published advertisements in the Pall Mall Gazette and other newspapers on November 13, 1891, stating that it would pay £100 [...] "
            "to anyone who got sick with influenza after using its product according to the instructions provided with it: [...] "
            "£1000 is deposited with the ALLIANCE BANK, Regent Street, shewing our sincerity in the matter. [...] "
            "Louisa Elizabeth Carlill saw the advertisement, bought one of the balls and used it three times daily for nearly two months until she contracted the flu on 17 January 1892. "
            "She claimed £100 from the Carbolic Smoke Ball Company. They ignored two letters from her husband, a solicitor. [...] "
            "The company argued that they had made no legally binding offer which was capable of acceptance, and thus there could be no contract. [...] "
            "The Court of Appeal unanimously rejected the company's arguments and held that they had made a binding contract with Carlill. [...] "
            "that satisfying the stated conditions for using the smoke ball constituted acceptance of the offer [...] "
            "After the action, Roe formed a new company with limited liability, and started up advertising again. [...] "
            "\"Many thousand Carbolic Smoke Balls were sold on these advertisements, but only three people claimed the reward of £100, thus proving conclusively that this invaluable remedy will prevent and cure the above mentioned diseases. "
            "The CARBOLIC SMOKE BALL COMPANY LTD. now offer £200 REWARD [...] "
            "The unsuccessful defence counsel in the lower court, H. H. Asquith, went on to become Prime Minister of the United Kingdom. "
            "Louisa Carlill lived until she was 96. She died on March 10, 1942, according to her doctor, Joseph M. Yarman, principally of old age. "
            "But there was one other cause noted: influenza.",
            nome="Carlill v Carbolic Smoke Ball Co")],
    },
    # 9 o homem dos direitos de Miranda
    {
        "temas_secundarios": ["personagens_esquecidos", "psicologia_social"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "O \"você tem o direito de permanecer calado\" nasceu do caso de Ernesto Miranda, cuja condenação foi anulada em 1966. Julgado de novo sem a confissão, foi condenado outra vez. Solto, vendia o aviso em cartões autografados.",
        "explicacao": (
            "Em 1963, em Phoenix, no Arizona, Miranda foi preso como suspeito de sequestrar e estuprar uma jovem "
            "de 18 anos. Depois de duas horas de interrogatório, escreveu à mão uma confissão. As folhas traziam "
            "impressa uma declaração de que ele conhecia plenamente seus direitos, mas ninguém o avisou de que "
            "podia ficar calado nem de que podia ter um advogado. Condenado com base sobretudo na confissão, ele "
            "levou o caso à Suprema Corte dos EUA. Na decisão Miranda v. Arizona, de 1966, a corte determinou que "
            "todo suspeito sob custódia deve ser informado, antes do interrogatório, de que tem o direito de ficar "
            "em silêncio, de que o que disser será usado contra ele e de que pode ter um advogado, nomeado para "
            "ele se não puder pagar. Por causa disso, as polícias dos EUA passaram a distribuir aos agentes "
            "cartões com o aviso para ler aos presos. O Arizona julgou Miranda de novo, com a confissão excluída "
            "das provas, e ele foi condenado mais uma vez. Em liberdade condicional desde 1972, vendia cartões de "
            "aviso autografados por 1,50 dólar. Em 1976, aos 34 anos, morreu esfaqueado numa briga de bar em "
            "Phoenix. Foram encontrados com ele vários cartões de Miranda."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Ernesto_Miranda",
            "whose criminal conviction was set aside in the landmark U.S. Supreme Court case Miranda v. Arizona [...] "
            "After the Supreme Court decision invalidated Miranda's initial conviction, the state of Arizona tried him again. "
            "At the second trial, with his confession excluded from evidence, he was convicted. [...] "
            "Late in the evening of March 2, 1963, 18-year old Patricia Weir was kidnapped [...] "
            "After two hours of interrogation, some of which regarded another offense for which Miranda was separately tried and convicted, Miranda hand-wrote a confession to the kidnapping and rape of Weir. [...] "
            "with full knowledge of my legal rights [...] "
            "he was not informed of his right to have an attorney present, nor of his right to remain silent when he was arrested or before his interrogation. [...] "
            "Miranda was convicted of rape and kidnapping, based largely on the confession [...] "
            "The person in custody must, prior to interrogation, be clearly informed that he has the right to remain silent, and that anything he says will be used against him in court; "
            "he must be clearly informed that he has the right to consult with a lawyer and to have the lawyer with him during interrogation, and that, if he is indigent, a lawyer will be appointed to represent him. "
            "The opinion was released on June 13, 1966. "
            "Because of the decision, police departments throughout the U.S. started to issue Miranda warning cards for their officers to recite. [...] "
            "Miranda was paroled in 1972. After his release, he started selling autographed Miranda warning cards for $1.50. [...] "
            "On January 31, 1976, a fight erupted at the Amapola Bar at 233 South 2nd Street in downtown Phoenix in which Miranda was stabbed. [...] "
            "He was 34. Several Miranda cards were found on his person.",
            nome="Ernesto Miranda")],
    },
    # 10 o café do McDonald's não era frescura
    {
        "temas_secundarios": ["cafe_cha_cacau", "vieses_cognitivos"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "O processo do café quente do McDonald's virou símbolo de ação judicial absurda. Mas a cliente, de 79 anos, teve queimaduras de terceiro grau e precisou de enxertos, e a empresa já tinha mais de 700 relatos de queimados.",
        "explicacao": (
            "Em fevereiro de 1992, Stella Liebeck comprou um café no drive-thru de um McDonald's em Albuquerque, "
            "nos EUA. Com o carro parado, pôs o copo entre os joelhos para tirar a tampa e derramou tudo no colo. "
            "A calça de moletom absorveu o café e o manteve contra a pele. Ela ficou oito dias internada para "
            "enxertos de pele e perdeu quase 20% do peso. Pediu 20 mil dólares para cobrir as despesas, e a "
            "empresa ofereceu 800. No julgamento, em 1994, veio à tona que o McDonald's exigia das franquias café "
            "a 82–88 °C, e um especialista disse ao júri que, a 88 °C, a bebida pode causar queimadura de terceiro "
            "grau em uns três segundos. Documentos mostraram que, de 1982 a 1992, a empresa tinha recebido mais de "
            "700 relatos de pessoas queimadas pelo seu café. O júri considerou o McDonald's 80% responsável e "
            "fixou 2,7 milhões de dólares em danos punitivos, mas o juiz reduziu esse valor para três vezes o da "
            "indenização, e as partes acabaram fazendo um acordo sigiloso antes da apelação. Mesmo assim, o caso "
            "virou bandeira de quem critica os processos frívolos nos EUA: a rede ABC chegou a chamá-lo de "
            "\"garoto-propaganda\" dos processos excessivos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Liebeck_v._McDonald%27s_Restaurants",
            "On February 27, 1992, the plaintiff, Stella Liebeck, aged 79, purchased hot coffee from a McDonald's restaurant, accidentally spilled it in her lap, and suffered third-degree burns in her pelvic region. [...] "
            "Liebeck sought to settle with McDonald's for $20,000 to cover her medical expenses. [...] "
            "The jury found that McDonald's was 80% responsible for the incident. "
            "Liebeck was awarded a net $160,000 in compensatory damages to cover medical expenses, and $2.7 million [...] "
            "The trial judge reduced the punitive damages to three times the amount of the compensatory damages, totaling $640,000. "
            "The parties settled for a confidential amount before an appeal was decided. [...] "
            "It was cited by some as an example of frivolous litigation; ABC News called the case \"the poster child of excessive lawsuits\" [...] "
            "ordered a 49-cent cup of coffee from the drive-through window of a McDonald's restaurant in Albuquerque, New Mexico. [...] "
            "Her grandson parked so that she could add cream and sugar to her coffee. "
            "She placed the coffee cup between her knees and pulled the far side of the lid toward her to remove it. "
            "In the process, she spilled the entire cup of coffee on her lap. "
            "She was wearing cotton sweatpants, which absorbed the coffee and held it against her skin [...] "
            "She remained in the hospital for eight days while she underwent skin grafting. "
            "During this period, she lost 20 pounds (9.1 kg), nearly 20% of her body weight [...] "
            "McDonald's offered only $800. [...] "
            "The trial took place from August 8 to 17, 1994 [...] "
            "McDonald's required franchisees to hold coffee at 180–190 °F (82–88 °C). [...] "
            "190 °F (88 °C) coffee may produce third-degree burns (where skin grafting is necessary) in about three seconds [...] "
            "from 1982 to 1992, McDonald's had received more than 700 reports of people burned by its coffee to varying degrees of severity",
            nome="Liebeck v. McDonald's Restaurants")],
    },
    # 11 a médium presa pela lei de bruxaria
    {
        "temas_secundarios": ["segunda_guerra", "religioes"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Em 1944, em plena guerra, uma médium escocesa foi condenada por uma lei de bruxaria de 1735. Só que a lei não punia bruxas: partia da ideia de que ninguém tem poderes mágicos e punia quem dissesse ter.",
        "explicacao": (
            "O Witchcraft Act de 1735 marcou o fim da caça às bruxas na Grã-Bretanha. As leis anteriores supunham "
            "que bruxas eram reais e tinham poderes vindos de pactos com Satanás. A nova lei supunha o contrário: "
            "que ninguém tinha poder mágico, e que quem alegava ter era um trapaceiro arrancando dinheiro de "
            "crédulos. A pena máxima era de um ano de prisão. Helen Duncan ficou famosa por sessões em que dizia "
            "materializar espíritos soltando ectoplasma pela boca; análises mostraram que o material era feito de "
            "gaze, papel e clara de ovo. Em novembro de 1941, numa sessão em Portsmouth, ela disse que o espírito "
            "de um marinheiro contara que o encouraçado HMS Barham tinha afundado. O naufrágio só foi anunciado ao "
            "público no fim de janeiro de 1942, e a Marinha passou a se interessar por ela. Em janeiro de 1944, "
            "policiais à paisana a prenderam numa sessão. As autoridades acharam na lei de 1735 uma acusação que "
            "ia a júri, mais grave que a de vadiagem, e ela foi condenada a nove meses de prisão. O processo talvez "
            "se explique pelo clima de desconfiança da época: as autoridades temiam que ela continuasse revelando "
            "informações sigilosas, fosse qual fosse a fonte. Winston Churchill reclamou do uso dos tribunais com essa \"bobagem obsoleta\". "
            "O caso quase certamente contribuiu para a revogação da lei, em 1951."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Witchcraft_Act_1735",
                "which made it a crime for a person to claim that any human being had magical powers or was guilty of practising witchcraft. "
                "With this, the law abolished the hunting and executions of witches in Great Britain. "
                "The maximum penalty set out by the act was a year's imprisonment. [...] "
                "Instead of assuming as the earlier laws did that witches were real and had real magical power derived from pacts with Satan, the new law assumed that there were no real witches, no one had real magic power and those claiming such powers were cheaters extorting money from gullible people.",
                nome="Witchcraft Act 1735"),
            wiki("Helen_Duncan",
                "was a Scottish medium best known as the last person to be imprisoned under the Witchcraft Act 1735 [...] "
                "In 1926, she developed from clairvoyant to physical medium by offering séances in which she claimed to be able to permit the spirits of recently deceased persons to materialise, by emitting ectoplasm from her mouth. [...] "
                "An early examination of pieces of Duncan's ectoplasm revealed that it was made of cheesecloth, paper mixed with the white of egg and lavatory paper stuck together. [...] "
                "During World War II, in November 1941, Duncan held a séance in Portsmouth at which she claimed the spirit materialization of a sailor told her HMS Barham had been sunk. "
                "Because the sinking of HMS Barham was revealed, in strict confidence, only to the relatives of casualties, and not announced to the public until late January 1942, the Navy started to take an interest in her activities. "
                "Two lieutenants were among her audience at a séance on 14 January 1944. [...] "
                "This was followed up on 19 January, when undercover policemen arrested her at another séance [...] "
                "She was initially arrested under section 4 of the Vagrancy Act 1824, a minor offence tried by magistrates. "
                "The authorities regarded the case as more serious, and eventually discovered section 4 of the Witchcraft Act 1735, covering fraudulent \"spiritual\" activity, which was triable before a jury. [...] "
                "The prosecution may be explained by the mood of suspicion prevailing at the time: the authorities were afraid that she could continue to reveal classified information, whatever her source was. [...] "
                "Duncan was imprisoned for nine months [...] "
                "After the verdict, Winston Churchill wrote a memo to Home Secretary Herbert Morrison, complaining about the misuse of court resources on the \"obsolete tomfoolery\" of the charge. [...] "
                "In 1944, Duncan was one of the last people convicted under the Witchcraft Act 1735 [...] "
                "Duncan's trial almost certainly contributed to the repeal of the Witchcraft Act 1735, which was contained in the Fraudulent Mediums Act 1951",
                nome="Helen Duncan"),
        ],
    },
    # 12 a selfie do macaco
    {
        "temas_secundarios": ["ia_robotica", "cinema_fotografia", "comportamento_animal"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Macacos fizeram selfies com a câmera de um fotógrafo, e as fotos rodaram o mundo em 2011. A briga sobre quem é o dono delas chegou à Justiça dos EUA, que decidiu: animal não pode ter direito autoral.",
        "explicacao": (
            "O fotógrafo britânico David Slater tinha ido à Indonésia fotografar macacos-de-celebes, uma espécie "
            "criticamente ameaçada. Segundo ele, a câmera estava num tripé, e os macacos brincavam com o cabo do "
            "disparador enquanto ele afastava outros do grupo. Quando a Wikimedia Commons publicou as imagens, "
            "Slater pediu que as tirassem do ar e ouviu um não: para a fundação, os direitos são de quem cria, um "
            "criador não humano não pode tê-los, e as fotos estariam em domínio público. Ele disse ter perdido pelo "
            "menos 10 mil libras. Em 2014, o Escritório de Direitos Autorais dos EUA afirmou que não registra obras "
            "produzidas pela natureza, por animais ou por plantas, e deu como exemplo \"uma fotografia tirada por "
            "um macaco\". Em 2015, a ONG PETA processou Slater em nome do macaco, que batizou de Naruto. A "
            "advogada da editora do livro de Slater observou que a PETA talvez estivesse processando em nome do "
            "macaco errado. Em 2018, um tribunal de apelação decidiu que animais não podem ser titulares de "
            "direitos autorais. O caso ganhou uma segunda vida com a inteligência artificial: em 2023, uma "
            "orientação do mesmo escritório sobre obras com material gerado por IA citou o processo como exemplo "
            "da exigência de autoria humana."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Monkey_selfie_copyright_dispute",
            "Between 2011 and 2018, a series of disputes took place about the copyright status of selfie photographs taken by Celebes crested macaques, using equipment belonging to British wildlife photographer David J. Slater. [...] "
            "The Wikimedia Foundation's 2014 refusal to remove the pictures from its Wikimedia Commons image library was based on the understanding that copyright is held by the creator, that a non-human creator (not being a legal person) cannot hold copyright, and that the images are thus in the public domain. "
            "Slater stated in August 2014 that, as a result of the pictures being available on Wikipedia, he had lost at least £10,000 [...] "
            "In April 2018, the appeals court ruled against PETA, stating in its judgement that animals cannot legally hold copyrights [...] "
            "Since 2008, British nature photographer David Slater had travelled to Indonesia to take photographs of the critically endangered Celebes crested macaques. [...] "
            "the portrait was shot when his camera had been mounted on a tripod, with the primates playing around with a remote cable release as he fended off other monkeys. [...] "
            "The Office will not register works produced by nature, animals, or plants.\" "
            "The compendium specifically highlights \"a photograph taken by a monkey\" as an example of something that cannot be copyrighted. [...] "
            "On 22 September 2015, People for the Ethical Treatment of Animals (PETA) filed a lawsuit against Slater and Blurb [...] "
            "to request that the monkey, whom they named Naruto, be assigned copyright [...] "
            "In November, Angela Dunning, the attorney for Blurb, noted that PETA may have been suing on behalf of the wrong monkey. [...] "
            "In 2023, the U.S. Copyright Office published a guidance on the registration of works containing AI-generated material; Naruto v. Slater was cited as an example of the human authorship requirement.",
            nome="Monkey selfie copyright dispute")],
    },
    # 13 o júri trancado de William Penn
    {
        "temas_secundarios": ["religioes", "revolucoes_politicas"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Em 1670, um juiz de Londres trancou um júri sem comida, água nem aquecimento porque ele não condenava William Penn, futuro fundador da Pensilvânia. Os jurados resistiram, e o caso firmou a independência do júri.",
        "explicacao": (
            "Penn e William Mead, ambos quacres, tinham sido presos em agosto de 1670 por violar uma lei que "
            "proibia reuniões religiosas de mais de cinco pessoas fora da Igreja da Inglaterra. O júri os "
            "considerou \"culpados de falar na Gracechurch Street\", mas se recusou a declarar a reunião ilegal. "
            "Furioso, o juiz avisou que os jurados só seriam liberados com um veredito que o tribunal aceitasse e "
            "os trancou durante a noite. Penn, amarrado e amordaçado por ordem do juiz, gritou aos jurados que não "
            "abrissem mão do seu direito, e o presidente do júri, Edward Bushel, respondeu que nunca o fariam. "
            "Depois de dois dias de jejum, o júri voltou com um veredito de inocência. O juiz então multou os "
            "jurados por desacato e os mandou para a prisão até que pagassem. Bushel se recusou a pagar e pediu "
            "habeas corpus. Em novembro de 1670, o presidente do Tribunal de Pleitos Comuns, John Vaughan, decidiu "
            "que um júri não pode ser punido simplesmente por causa do veredito que deu, embora um jurado ainda "
            "pudesse ser punido se ficasse provado que agiu de forma imprópria. O caso de Bushel estabeleceu de "
            "vez a independência do júri, e hoje ele é lembrado nas discussões sobre o poder dos jurados de "
            "absolver contra a lei."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Bushel%27s_Case",
            "was a landmark English decision on the role of juries. It established beyond question the independence of the jury. [...] "
            "two Quakers charged with unlawful assembly, William Penn (the future founder of Pennsylvania) and William Mead. "
            "They had been arrested in August 1670 for violating the Conventicle Act, which forbade religious assemblies of more than five people outside the auspices of the Church of England. "
            "The jury found the two \"guilty of speaking in Gracechurch Street\" but refused to find \"an unlawful assembly\". "
            "The infuriated judge charged the jury that they \"shall not be dismissed until we have a verdict that the court will accept\". [...] "
            "whereupon the judge had them locked up overnight without food, water or heat. "
            "The judge ordered Penn bound and gagged. "
            "Penn protested, shouting to the jury, \"You are Englishmen, mind your Privilege, give not away your Right\", to which foreman of the jury Edward Bushel replied, \"Nor shall we ever do.\" "
            "Finally, after a two-day fast in the Tower of London, the jury returned a not guilty verdict. "
            "The judge fined the jury for contempt of court for returning a verdict contrary to their own findings of fact and removed them to prison until the fine was paid. [...] "
            "nonetheless refused to pay the fine and was released through a writ of habeas corpus. [...] "
            "Sir John Vaughan, Chief Justice of the Court of Common Pleas [...] "
            "Vaughan ruled in November 1670 that a jury could not be punished simply on account of the verdict it returned, but that individual jurors could still be punished if it could be demonstrated that they had acted improperly. [...] "
            "Jury nullification",
            nome="Bushel's Case")],
    },
    # 14 o "Julgamento do Macaco" foi encenado
    {
        "temas_secundarios": ["evolucao", "religioes"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "O famoso \"Julgamento do Macaco\", de 1925, contra um professor que teria ensinado a evolução, foi armado para dar fama a uma cidadezinha. O réu nem sabia se tinha ensinado o assunto, mas topou ser acusado.",
        "explicacao": (
            "A Lei Butler, do Tennessee, proibia ensinar a evolução humana nas escolas públicas, e a ACLU, "
            "entidade americana de liberdades civis, tinha se oferecido para defender quem fosse acusado de "
            "violá-la, para contestar a lei. Em abril de 1925, numa farmácia de Dayton, o gerente de uma "
            "mineradora, George Rappleyea, convenceu o superintendente escolar e um advogado local de que o "
            "processo daria publicidade à cidade. Chamaram John Scopes, professor de 24 anos que tinha substituído "
            "o de biologia. Havia uma ironia: o estado exigia um livro didático que descrevia e defendia a "
            "evolução, e assim os professores eram, na prática, obrigados a infringir a lei. Scopes não lembrava "
            "se tinha ensinado evolução em aula, mas aceitou ser réu e até orientou alunos a depor contra ele. A "
            "acusação ganhou William Jennings Bryan, três vezes candidato à presidência, e a defesa, o famoso "
            "advogado Clarence Darrow. Mais de 200 repórteres foram a Dayton, e foi o primeiro julgamento dos EUA "
            "transmitido por rádio para todo o país. Depois de oito dias, o júri levou nove minutos para considerar "
            "Scopes culpado, e ele foi multado em 100 dólares. A condenação foi anulada por um detalhe técnico: a "
            "multa deveria ter sido fixada pelo júri, e não pelo juiz."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Scopes_trial",
            "a high school teacher, John T. Scopes, was accused of violating the Butler Act, a Tennessee state law which outlawed the teaching of human evolution in public schools. "
            "The trial was deliberately staged in order to attract publicity to the small town of Dayton, Tennessee, where it was held. "
            "Scopes was unsure whether he had ever actually taught evolution, but he incriminated himself deliberately so the case could have a defendant. "
            "Scopes was represented by the American Civil Liberties Union, which had offered to defend anyone accused of violating the Butler Act in an effort to challenge the constitutionality of the law. "
            "Scopes was found guilty and was fined $100 [...] "
            "but the verdict was overturned on a technicality. "
            "William Jennings Bryan, a three-time presidential candidate and former secretary of state, argued for the prosecution, while famed labor and criminal lawyer Clarence Darrow served as the principal defense attorney for Scopes. [...] "
            "being the first trial in American history to be nationally broadcast by radio. [...] "
            "On April 5, 1925, George Rappleyea, the local manager for the Cumberland Coal and Iron Company, arranged a meeting with county superintendent of schools Walter White and local attorney Sue K. Hicks at Robinson's Drug Store in Dayton, convincing them that the controversy of such a trial would give Dayton much needed publicity. [...] "
            "The men then summoned 24-year-old John T. Scopes, a Dayton high school science and math teacher. "
            "The group asked Scopes, who had substituted for the regular biology teacher, to admit to teaching the theory of evolution. "
            "Rappleyea pointed out that, while the Butler Act prohibited the teaching of the theory of evolution, the state required teachers to use George William Hunter's textbook, Civic Biology: Presented in Problems, which explicitly described and endorsed the theory of evolution [...] "
            "and that teachers were, therefore, effectively required to break the law. [...] "
            "Scopes urged students to testify against him and coached them in their answers. [...] "
            "After eight days of trial, it took the jury only nine minutes to deliberate. [...] "
            "the court set aside the conviction on appeal because of a legal technicality: the jury should have decided the fine, not the judge [...] "
            "More than 200 newspaper reporters from all parts of the country and two from London were in Dayton.",
            nome="Scopes trial")],
    },
    # 15 Mota Coqueiro não foi o último enforcado
    {
        "temas_secundarios": ["brasil_imperio", "heranca_africana"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Diz-se que o fazendeiro Mota Coqueiro, enforcado em 1855, foi o último executado no Brasil. Não foi: a última execução foi a de um escravizado, Francisco, em 1876. E a forca parou sem que a lei fosse revogada.",
        "explicacao": (
            "Mota Coqueiro, apelidado de \"Fera de Macabu\", foi condenado como mandante da chacina de uma família "
            "de colonos que vivia em suas terras, no norte fluminense, em 1852. Muitos acreditam que um inocente "
            "foi executado, e surgiu a versão de que dom Pedro II, abalado, nunca mais deixou ninguém subir à "
            "forca. Mas, depois dele, pelo menos oito homens livres foram de fato executados entre 1855 e 1865, e "
            "no mínimo 30 escravizados foram enforcados entre 1855 e 1876. A última execução de um homem livre "
            "foi em 1861. Francisco foi enforcado em Pilar, Alagoas, em 28 de abril de 1876, diante de cerca de 2 "
            "mil curiosos. Tinha sido condenado por matar o senhor e a mulher dele, com base numa lei de 1835, "
            "feita para conter as revoltas escravas, que punia com a morte o escravizado que matasse ou ferisse "
            "gravemente o senhor ou alguém da família. Dom Pedro II negou clemência poucos dias antes de partir "
            "para uma temporada no exterior. Depois dessa viagem, ninguém mais foi para a forca no Brasil: o "
            "imperador passou a ceder aos pedidos de clemência ou a engavetá-los, embora os tribunais seguissem "
            "condenando à morte. A lei de 1835 só foi revogada oficialmente em 1890, depois da Proclamação da "
            "República."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": SENADO_1876, "titulo": "Há 140 anos, a última pena de morte do Brasil (Agência Senado)", "idioma": "pt",
             "trecho": "A pacata cidade de Pilar, na província de Alagoas, amanheceu tumultuada em 28 de abril de 1876. "
                       "Calcula-se em 2 mil o público de curiosos, inclusive vindos das vilas vizinhas, que se aglomerou para assistir à execução do negro Francisco. "
                       "O escravo fora condenado à forca por matar a pauladas e punhaladas um dos homens mais respeitados de Pilar e sua mulher. [...] "
                       "O monarca, poucos dias antes de partir para uma temporada fora do Brasil, assinou o despacho: não haveria clemência imperial. [...] "
                       "Há exatos 140 anos, essa foi a última pena capital executada no Brasil. [...] "
                       "Ela dizia que seria condenado à morte o escravo que matasse ou ferisse gravemente seu senhor ou qualquer membro da família dele. [...] "
                       "o projeto da lei de 1835 foi proposto pela Regência como forma de conter as crescentes rebeliões escravas. [...] "
                       "O monarca cada vez mais cedia às súplicas. A última execução de um homem livre ocorreu em 1861. [...] "
                       "Apesar de os tribunais continuarem sentenciando a pena de morte até o fim do Império, em 1889 [...] "
                       "De fato, depois dessa viagem, ninguém mais no Brasil foi para a forca. [...] "
                       "Quando o processo era perfeito, sem deixar dúvida de que o escravo matou seu senhor, o imperador simplesmente engavetava o pedido de clemência. [...] "
                       "Ela só foi oficialmente revogada em 1890, logo depois da Proclamação da República."},
            wiki("Manuel_da_Mota_Coqueiro",
                "apelidado de \"A Fera de Macabu\", foi um rico fazendeiro da região norte fluminense condenado à pena de morte por ter (supostamente) mandado matar toda uma família de colonos residente em suas terras. "
                "O caso é um dos crimes mais infames do Brasil, pois muitos consideram que um inocente foi executado. [...] "
                "Em uma noite chuvosa de 1852, Francisco Benedito e toda sua família foram mortos [...] "
                "insiste em afirmar que a execução de Mota Coqueiro foi a última no Brasil Imperial, em decorrência do imperador D. Pedro II ter ficado abalado por mandar executar \"um inocente\". "
                "Desde então, não teria mais permitido a aplicação da pena de morte no país. [...] "
                "Mota Coqueiro não foi o último executado, nem mesmo o último homem livre executado no Brasil. "
                "Depois de sua execução, o Imperador mandou executar pelo menos dezesseis homens livres: entre 1855 e 1865, oito réus foram efetivamente executados; "
                "sobre cinco faltam informações, e três tiveram a sua pena comutada posteriormente. "
                "Entre 1855 e 1876, no mínimo 30 escravos foram executados por enforcamento.",
                nome="Manuel da Mota Coqueiro", idioma="pt"),
        ],
    },
]
