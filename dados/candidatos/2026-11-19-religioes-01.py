LOTE = "2026-11-19-religioes-01"
AREA = "sociedade"
TEMA = "religioes"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o Buda virou são Josafá
    {
        "temas_secundarios": ["asia_antiga", "palavras_viajantes"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "São Josafá, príncipe indiano que trocou o trono pela vida de eremita, entrou nos calendários de santos católico e ortodoxo. A história dele é uma versão cristianizada da vida do Buda, e o nome vem de \"bodisatva\".",
        "explicacao": (
            "Na lenda, um rei da Índia que perseguia os cristãos ouve de astrólogos que o filho vai se converter e "
            "isola o príncipe Josafá. Mesmo assim, o rapaz conhece o eremita Barlaão e vira cristão. No fim, o pai "
            "também se converte e entrega o trono ao filho, que depois abdica e vai viver recluso com o velho mestre. "
            "Para os estudiosos, o enredo deriva de um texto budista em sânscrito dos séculos II a IV, que passou "
            "por uma versão maniqueísta e por um livro árabe que circulava em Bagdá no século VIII. A primeira "
            "adaptação cristã é uma epopeia georgiana do século X. Um monge georgiano a verteu para o grego, e em "
            "1048 veio a tradução latina que espalhou a história pela Europa. O nome fez a mesma viagem: "
            "\"bodisatva\" virou Bodisav em textos persas e Būdhasaf em árabe, onde um ponto duplicado na escrita "
            "trocou o \"b\" por um \"y\". Depois veio Iodasaph em georgiano, Ioasaph em grego e Josaphat em latim. "
            "Barlaão e Josafá entraram em edições antigas do Martirológio Romano, com festa em 27 de novembro, e no "
            "calendário litúrgico ortodoxo grego. Um dos manuscritos de Marco Polo chega a notar a semelhança entre "
            "o Buda e são Josafá, sem desconfiar da origem da história."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Barlaam_and_Josaphat",
            "Barlaam and Josaphat, also known as Bilawhar and Budhasaf, are Christian saints. [...] "
            "According to tradition, an Indian king persecuted the Christian Church in his realm. After astrologers predicted that his own son would some day become a Christian, the king imprisoned the young prince Josaphat, who nevertheless met the hermit Saint Barlaam and converted to Christianity. "
            "After much tribulation the young prince's father accepted the Christian faith, turned over his throne to Josaphat, and retired to the desert to become a hermit. "
            "Josaphat himself later abdicated and went into seclusion with his old teacher Barlaam. "
            "The story is thought to be a Christianized and later version of the story of Siddhartha Gautama, who became the Buddha. [...] "
            "The tale derives from a second to fourth century Sanskrit Mahayana Buddhist text, via a Manichaean version, then the Arabic Kitāb Bilawhar wa-Būd̠āsaf (Book of Bilawhar and Budhasaf), current in Baghdad in the eighth century [...] "
            "The first Christianized adaptation was the Georgian epic Balavariani dating back to the 10th century. "
            "A Georgian monk, Euthymius of Athos, translated the story into Greek [...] "
            "There the Greek adaptation was translated into Latin in 1048 and soon became well known in Western Europe as Barlaam and Josaphat. [...] "
            "One of the Marco Polo manuscripts notes the remarkable similarity between the tale of \"Sergamoni Borcan\" (i.e. Sakyamuni Burkhan; the name that Polo recorded the Mongols using for the Buddha) and St. Josaphat, apparently unaware of the origins of the Josaphat story. [...] "
            "In this context, the name Josaphat is derived from the Sanskrit bodhisattva. "
            "The Sanskrit word was changed to Bodisav in Middle Persian texts in the 6th or 7th century, then to Būdhasaf or Yūdhasaf in an 8th-century Arabic document (Arabic initial \"b\" ﺑ changed to \"y\" ﻳ by duplication of a dot in handwriting). "
            "This became Iodasaph in Georgian in the 10th century, and that name was adapted as Ioasaph (Ἰωάσαφ) in Greece in the 11th century, and then was assimilated to Iosaphat/Josaphat in Latin. [...] "
            "Barlaam and Josaphat were included in earlier editions of the Roman Martyrology with a joint feast day on 27 November [...] "
            "Barlaam and Josaphat were entered into the Greek Orthodox liturgical calendar on 26 August Julian",
            nome="Barlaam and Josaphat")],
    },
    # 2 a escada imóvel do Santo Sepulcro
    {
        "temas_secundarios": ["leis_julgamentos", "mundo_islamico_medieval"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Na Igreja do Santo Sepulcro, em Jerusalém, uma escada de madeira está encostada na mesma janela desde pelo menos os anos 1720: nada ali pode mudar sem o acordo das seis igrejas cristãs donas do prédio.",
        "explicacao": (
            "A regra vem do chamado Status Quo. Decretos do Império Otomano de 1757 e de 1852 fixaram a divisão dos "
            "santuários entre as denominações cristãs, e todas as autoridades que governaram a região depois, como "
            "os britânicos, a Jordânia e Israel, mantiveram essas regras. A escada aparece numa gravura de 1728 e é "
            "citada no decreto de 1757. Como tudo devia ficar \"como estava\", ela ficou também. Em geral, é "
            "atribuída aos armênios, cujos clérigos que moravam na igreja usavam o parapeito sob a janela como "
            "varanda, chegando a ele pela escada. Em 1964, o papa Paulo VI a descreveu como um símbolo visível da "
            "divisão entre os cristãos. Em 1997, um turista teria escondido a escada dentro da igreja para zombar "
            "do acordo, e ela foi recolocada. A entrada guarda outra curiosidade: duas famílias muçulmanas cuidam "
            "dela. Depois de retomar Jerusalém dos cruzados, em 1187, Saladino confiou à família Joudeh a chave da "
            "igreja, de ferro e com 30 centímetros, enquanto a família Nuseibeh abre a porta como parte neutra "
            "entre as denominações. Os documentos das igrejas registram esse papel desde a época de Saladino."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Immovable_Ladder",
                "The Immovable Ladder is a wooden ladder that has been leaning against a window of the Church of the Holy Sepulchre in the Old City of Jerusalem since at least the 1720s, protected from removal or alteration under the law of the Status Quo. [...] "
                "Its presence in its current location signifies the adherence to an agreement among six Christian denominations, who collectively own the church, not to move, repair, or alter anything in the church without the consent of all six denominations. [...] "
                "The ladder itself belongs to the Armenian Apostolic Church, as Armenians have the right to use the cornice [...] "
                "The ledge served as a balcony for the Armenian clergy resident in the Holy Sepulchre, and they reached it via the ladder. [...] "
                "The earliest record of the ladder is in a 1728 engraving by Elzearius Horn. "
                "In 1757, the same year the Status Quo was introduced, Ottoman sultan Abdul Hamid I mentioned the ladder in a firman, and because everything was to be left \"as it was\" according to the royal decree, the ladder had to stay as it was too. [...] "
                "The division of rights, established by the 1757 firman and reaffirmed by a firman in 1852, became known as \"Status quo\". [...] "
                "The provisions of the Status Quo have been and are strictly adhered to by all authorities under whose jurisdiction these territories have been at various times—British authorities in the British Mandate of Palestine, Jordan, and Israel. [...] "
                "During his pilgrimage to the Holy Land in 1964, Pope Paul VI described the ladder as a visible symbol of Christian division. "
                "In 1997, a tourist allegedly hid the ladder inside the church to ridicule the Status Quo, before it was replaced.",
                nome="Immovable Ladder"),
            wiki("Church_of_the_Holy_Sepulchre",
                "According to their own family lore, the Muslim Nuseibeh family has been responsible for opening the door as a neutral party to the church's denominations already since the seventh century. "
                "However, they themselves admit the documents held by various Christian denominations only mention their role since the 12th century in the time of Saladin, which is the more generally accepted date. "
                "After retaking Jerusalem from the Crusaders in 1187, Saladin entrusted the Joudeh family with the key to the church, which is made of iron and 30 centimetres (12 in) long; the Nuseibehs either became or remained the doorkeepers.",
                nome="Church of the Holy Sepulchre"),
        ],
    },
    # 3 os cristãos ocultos do Japão
    {
        "temas_secundarios": ["costumes_rituais", "palavras_viajantes"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Proibidos no Japão a partir do século XVII, cristãos rezaram escondidos até 1873: a Virgem Maria ganhou a forma de Kannon, deusa budista da misericórdia, e as orações soavam como canto budista.",
        "explicacao": (
            "Com a repressão ao cristianismo pelo xogunato Tokugawa, muitos católicos japoneses passaram à "
            "clandestinidade e deram às práticas religiosas uma aparência budista, que escondia um sentido cristão. "
            "As imagens de \"Maria Kannon\", inspiradas na deusa budista, tornaram-se comuns. As orações, adaptadas "
            "ao som de cantos budistas, guardaram muitas palavras sem tradução do latim, do português e do "
            "espanhol, herança da fé trazida pelos missionários católicos em meados do século XVI. Como livros "
            "podiam ser confiscados, a Bíblia e a liturgia passaram de geração em geração de boca em boca. Em 1865, "
            "quando a Igreja de Ōura foi construída em Nagasaki, o padre católico Bernard Petitjean reconheceu "
            "esses fiéis. Com a volta da liberdade religiosa, em 1873, cerca de 30 mil cristãos secretos saíram "
            "do esconderijo. Parte deles não voltou à Igreja Católica e manteve a tradição dos tempos de "
            "perseguição, que hoje pode ser descrita como quase uma fé à parte. Ela está sumindo: em 2025, "
            "noticiou-se que restavam menos de 100 cristãos ocultos na ilha de Ikitsuki, em Nagasaki, contra 10 "
            "mil nos anos 1940."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Kakure_Kirishitan",
            "Kakure Kirishitan (Japanese: 隠れキリシタン, lit. 'hidden Christians') is a modern term for a member of the Catholic Church in Japan who went underground at the start of the Edo period in the early 17th century (lifted in 1873) due to Christianity's repression by the Tokugawa shogunate [...] "
            "During this time, many believers modified their religious practices to resemble Buddhist ones on a surface level, but which held hidden Christian meaning in reality. "
            "For instance, depictions of the Virgin Mary modeled on the Buddhist deity Kannon (Avalokiteśvara), goddess of mercy, became common among Kakure Kirishitan, and were known as \"Maria Kannon\". "
            "The prayers were adapted to sound like Buddhist chant, yet retained many untranslated words from Latin, Portuguese, and Spanish. "
            "The Bible and other parts of the liturgy were passed down orally, because printed works could be confiscated by authorities. "
            "Kakure Kirishitan were recognized by Bernard Petitjean, a Catholic priest, when Ōura Church was built in Nagasaki in 1865. "
            "Approximately 30,000 secret Christians, some of whom had adopted these new ways of practicing Christianity, came out of hiding when religious freedom was re-established in 1873 after the Meiji Restoration. [...] "
            "Some Kakure Kirishitan did not rejoin the Catholic Church [...] "
            "The Kakure Kirishitan still exist today, forming \"what is arguably a separate faith, barely recognizable as the creed imported in the mid-1500s by Catholic missionaries\". "
            "In 2025, it was reported that there were less than 100 Hidden Christians left on the island of Ikitsuki in Nagasaki, down from 10,000 in the 1940s.",
            nome="Kakure Kirishitan")],
    },
    # 4 Victor Hugo, profeta do caodaísmo
    {
        "temas_secundarios": ["literatura", "costumes_rituais"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "O caodaísmo, religião fundada no Vietnã em 1926, tem Victor Hugo entre seus três principais profetas. Para os fiéis, o escritor francês transmitiu, por meio de médiuns, ensinamentos e várias orações.",
        "explicacao": (
            "Tudo começou em 1925, em Saigon, num clube espírita de funcionários do governo colonial francês, que "
            "faziam sessões de mediunidade e de tabuleiro ouija e liam com avidez os escritos de Allan Kardec, "
            "Victor Hugo e Flammarion. Numa sessão em 1926, o grupo acreditou ter recebido uma mensagem que "
            "anunciava uma futura religião universal, e a fundação foi declarada em 7 de outubro daquele ano. A "
            "doutrina junta preceitos éticos do confucionismo, práticas do taoismo, as ideias de carma e "
            "renascimento do budismo e uma organização hierárquica inspirada no catolicismo, com bispos e "
            "arcebispos. Uma placa na entrada do templo de Tây Ninh mostra os três profetas principais: Victor "
            "Hugo, Sun Yat-sen e Trạng Trình, conhecido como o \"Nostradamus vietnamita\". A escolha de Hugo tem uma "
            "raiz curiosa: ele mesmo praticou o espiritismo na ilha de Jersey, de 1852 a 1855, e previu que seria "
            "o profeta de uma nova religião capaz de fundir o misticismo europeu e o asiático. As estimativas de "
            "fiéis variam; a ONU calculava cerca de 2,5 milhões de caodaístas no Vietnã em 2015."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Caodaism",
            "on that combines \"ethical precepts from Confucianism, practices from Taoism, theories of karma and rebirth from Buddhism, and a hierarchical organization from Catholicism\". "
            "It was officially established in the city of Tây Ninh in Southern Vietnam in 1926. [...] "
            "Estimates of the number of Caodaists in Vietnam vary [...] "
            "The United Nations estimated about 2.5 million Caodaists existed in Vietnam, as of January 2015. [...] "
            "it was founded in 1925 in Saigon as a Spiritualist club named AĂÂ by Cao Quỳnh Cư, Cao Hoài Sang, Lê Văn Trung and Phạm Công Tắc, a group of clerks working in the colonial government, to practice mediumship and ouija sessions. "
            "They were avid readers of medium writings of Allan Kardec, Victor Hugo and Flammarion. "
            "During a séance in 1926, the group believed they had received a revelation message, predicting a future universal religion based on spiritist doctrines. [...] "
            "the “Declaration of the Founding of the Cao Đài Religion” on 7 October 1926 [...] "
            "The Cao Đài pantheon counts three main prophets, as illustrated on a plaque at the entrance of the Tay Ninh Temple: Victor Hugo (to please the French), since he gave many teachings and also the text of a number of important prayers. "
            "He himself practiced spiritism on the island of Jersey from 1852 to 1855, and predicted that he would become the prophet of a new religion to merge European and Asian mysticism. "
            "Sun Yat-sen (for the Chinese) and Trạng Trình, the Vietnamese Nostradamus (for the Vietnamese). [...] "
            "The Sacerdotal Council composed of Priests, Bishops, Archbishops, and Principal Archbishops.",
            nome="Caodaism")],
    },
    # 5 os parsis, os abutres e o diclofenaco
    {
        "temas_secundarios": ["ecologia", "farmacos"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "Um anti-inflamatório dado ao gado quase acabou com os abutres da Índia e abalou um rito funerário: os parsis, zoroastristas que deixam os mortos para as aves no alto de torres, tiveram de buscar alternativas.",
        "explicacao": (
            "Os zoroastristas evitam que os cadáveres contaminem o solo e os outros elementos naturais. Por isso, "
            "nas chamadas torres do silêncio, os corpos ficam expostos ao sol e às aves carniceiras, em geral "
            "abutres, e os ossos depois vão para um poço central. Na tradição parsi, essa exposição também é vista "
            "como um último ato de caridade: dar às aves o que de outro modo seria destruído. Nos anos 1990, porém, "
            "o diclofenaco passou a ser usado no gado. Os abutres que comiam carcaças de animais tratados nos "
            "últimos dias de vida morriam de falência dos rins, e modelos indicaram que bastava uma fração mínima de "
            "carcaças contaminadas, cerca de 0,8%, para derrubar as populações. Até 2008, a queda no subcontinente "
            "indiano passou de 97%. Os parsis de Mumbai notaram já no começo dos anos 1990 que havia menos aves "
            "nas torres, e as poucas que restaram muitas vezes não davam conta dos corpos. Em 2001, as comunidades "
            "estudavam criar abutres em cativeiro e usar concentradores solares, grandes espelhos, para acelerar a "
            "decomposição; algumas tiveram de recorrer ao enterro. O uso do diclofenaco no gado foi proibido na "
            "Índia em 2006."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Tower_of_Silence",
                "raised structure built by Zoroastrians for excarnation (that is, the exposure of human corpses to the elements for decomposition), in order to avoid contamination of the soil and other natural elements by the dead bodies. "
                "Carrion birds, usually vultures, and other scavengers, consume the flesh. "
                "Skeletal remains are gathered into a central pit [...] "
                "In Parsi Zoroastrian tradition, exposure of the dead is also considered to be an individual's final act of charity, providing the birds with what would otherwise be destroyed. "
                "In the late 20th century and early 21st century, the vulture population on the Indian subcontinent declined by over 97% as of 2008, primarily due to diclofenac poisoning of the birds following the introduction of that drug for livestock in the 1990s, until banned for cattle by the Government of India in 2006. "
                "The few surviving birds are often unable to fully consume the bodies. "
                "In 2001, Parsi communities in India were evaluating captive breeding of vultures and the use of \"solar concentrators\" (which are essentially large mirrors) to accelerate decomposition. "
                "Some have been forced to resort to burial",
                nome="Tower of Silence"),
            wiki("Indian_vulture_crisis",
                "Parsis in Mumbai started to notice in the early 1990s that there were fewer birds at the Towers of Silence in Mumbai. [...] "
                "The drug is believed to have been passed onto the vultures through the flesh of dead cattle who were given diclofenac in their last days of life, which then causes kidney failure in vultures. "
                "Data modelling revealed that a tiny proportion (about 0.8%) of livestock carcasses containing diclofenac can cause significant crashes in vulture populations.",
                nome="Indian vulture crisis"),
        ],
    },
    # 6 Maria no Alcorão
    {
        "temas_secundarios": ["mundo_islamico_medieval", "literatura"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Maria, mãe de Jesus, é a única mulher chamada pelo nome no Alcorão, que lhe dedica uma surata inteira. Já no texto mais antigo do Novo Testamento que fala dela, a carta aos Gálatas, ela é só \"uma mulher\".",
        "explicacao": (
            "No islã, Maria, ou Maryam, ocupa um lugar singular: o Alcorão a apresenta como a maior mulher que já "
            "existiu, e a 19ª surata leva o nome dela. A crença islâmica tradicional também sustenta o nascimento "
            "virginal de Jesus, narrado várias vezes no livro. O relato do parto tem detalhes próprios. Maria se "
            "retira para um lugar a leste e, com as dores do parto sob uma tamareira, é consolada por uma voz que "
            "lhe oferece água e frutos. Ao voltar para o seu povo, o recém-nascido fala em defesa da mãe. "
            "Estudiosos ligam esses episódios a escritos cristãos que ficaram fora da Bíblia: um milagre da "
            "tamareira com Maria aparece no Evangelho do Pseudo-Mateus, e o bebê que fala no berço está num "
            "evangelho siríaco da infância de Jesus, mas não em Lucas. No Novo Testamento, as principais fontes "
            "sobre Maria são os Evangelhos e os Atos dos Apóstolos. O relato mais antigo, porém, está na carta aos "
            "Gálatas, escrita antes dos evangelhos, onde ela aparece apenas como \"uma mulher\", sem nome."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Mary_in_Islam",
                "holds a singularly exalted place in Islam. [...] "
                "explicitly identifies her as the greatest woman to have ever lived. "
                "Moreover, she is the only woman referenced by name in the Quran. "
                "In the Quran, her story is related in three Meccan surahs (19, 21, 23) and four Medinan surahs (3, 4, 5, 66). "
                "The nineteenth Surah, Maryam, is named after her. [...] "
                "orthodox Islamic belief has upheld the virgin birth of Jesus [...] "
                "The Quran narrates the virgin birth of Jesus numerous times. [...] "
                "The primary two accounts the Quʾran is thought to recount in some way are found in the Latin Gospel of Pseudo-Matthew which features a Marian date-palm (and spring) miracle in Egypt [...] "
                "Mary withdraws \"to an easterly place,\" encounters the divine \"spirit\" appearing in human form, conceives by God’s command, and—seized by the pains of labor beneath a date-palm—is consoled by a voice that provides water and fruit; "
                "returning to her people, she vows silence, points to the infant, and the newborn speaks in defense of his mother [...] "
                "the newborn's cradle speech present in Islamic scripture and the Syriac Infancy Gospel is not found in Luke.",
                nome="Mary in Islam"),
            wiki("Mary,_mother_of_Jesus",
                "The canonical Gospels and the Acts of the Apostles are the primary sources of historical information about Mary. [...] "
                "The earliest New Testament account of Mary is in the epistle to the Galatians, which was written before the gospels. "
                "She is referred to as \"a woman\" and is not named",
                nome="Mary, mother of Jesus"),
        ],
    },
    # 7 os shakers: celibato e invenções
    {
        "temas_secundarios": ["invencoes", "historia_musica"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Os shakers, cristãos dos EUA que viviam em celibato, chegaram a 6 mil fiéis e ganharam fama de inventores: a eles se atribuem a serra circular, o prendedor de roupa e a vassoura chata. Em 2026, restam dois.",
        "explicacao": (
            "O grupo surgiu na Inglaterra, em 1747, e ficou conhecido como \"Shaking Quakers\", os quacres que "
            "tremem, pelo comportamento extático nos cultos. Os primeiros chegaram à América em 1774 e se fixaram "
            "no atual estado de Nova York. A líder Ann Lee pregava a renúncia ao casamento. Quem entrava assinava "
            "um pacto, entregava os bens e o trabalho à comunidade e passava a viver em celibato; casamentos "
            "anteriores terminavam na entrada. Sem filhos próprios, os shakers recebiam crianças por adoção, "
            "contrato ou conversão, e muitas vezes acolhiam órfãos. Mulheres dividiam a liderança espiritual com os "
            "homens. As fazendas e oficinas eram muito produtivas, e a lista de inovações atribuídas a eles inclui "
            "ainda uma máquina de lavar movida a roda e penas de metal. Uma canção shaker de 1848, \"Simple Gifts\", "
            "serviu de base para o final do balé Appalachian Spring, de Aaron Copland. O auge foi por volta de 1840, "
            "com cerca de 5 mil membros plenos e 6 mil fiéis no total. Depois, o artesanato perdeu para as "
            "fábricas, e leis de meados do século XX tiraram dos grupos religiosos o controle de adoções. Desde "
            "2019, só uma vila segue ativa, a de Sabbathday Lake, no Maine."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Shakers",
            "They were initially known as \"Shaking Quakers\" because of their ecstatic behavior during worship services. "
            "Espousing egalitarian ideals, the Shakers practice a celibate and communal utopian lifestyle [...] "
            "Women took on spiritual leadership roles alongside men, including founding leaders such as Jane Wardley, Ann Lee, and Lucy Wright. "
            "The Shakers emigrated from England and settled in British North America, with an initial settlement at Watervliet, New York (present-day Colonie) in 1774. [...] "
            "Since 2019, there has only been one active Shaker village: Sabbathday Lake Shaker Village, in Maine. [...] "
            "As of November 3, 2026, there are two remaining members. [...] "
            "and others broke off from the Quakers in 1747 [...] "
            "she called her followers to confess their sins, give up all their worldly goods, and take up the cross of celibacy and forsake marriage [...] "
            "Those who signed the covenant had to confess their sins, consecrate their property and their labor to the society, and live as celibates. "
            "If they were married before joining the society, their marriages ended when they joined. [...] "
            "Their industry brought about many industrial improvements, such as perfecting Babbitt metal, and inventing the rotary harrow, the circular saw, the clothespin, the Shaker peg, the flat broom, the wheel-driven washing machine, a machine for setting teeth in textile cards, a threshing machine, metal pens [...] "
            "Children were added to their communities through indenture, adoption, or conversion. "
            "Occasionally a foundling was anonymously left on a Shaker doorstep. They welcomed all, often taking in orphans and the homeless. [...] "
            "Simple Gifts was composed in 1848 by Elder Joseph Brackett [...] "
            "Aaron Copland's 1944 ballet score Appalachian Spring, written for Martha Graham, uses the Shaker tune \"Simple Gifts\" as the basis of its finale. [...] "
            "Shaker artisans could not compete with modern factories [...] "
            "By mid-century, new federal laws were passed denying control of adoption to religious groups, rendering it impossible for children to join the group. [...] "
            "the group reached maximum size of about 5,000 full members in 1840, and 6,000 believers at the peak of the Shaker movement.",
            nome="Shakers")],
    },
    # 8 a Bíblia de Jefferson, feita com navalha e cola
    {
        "temas_secundarios": ["revolucoes_politicas", "literatura"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Thomas Jefferson montou com navalha e cola seu próprio Evangelho, recortando versículos e deixando de fora os milagres e a ressurreição. De 1904 até os anos 1950, novos congressistas dos EUA ganhavam uma cópia.",
        "explicacao": (
            "A obra, A Vida e a Moral de Jesus de Nazaré, ficou pronta em 1820. Jefferson recortou trechos de "
            "Mateus, Marcos, Lucas e João em edições em latim e grego, em francês e em inglês e colou tudo em ordem "
            "cronológica, como uma única narrativa. Saíram os milagres, a maior parte das menções ao sobrenatural e "
            "as passagens que mostram Jesus como divino; ficaram ensinamentos como o Sermão da Montanha e as "
            "parábolas mais conhecidas. Segundo historiadores, quando uma lição moral vinha embutida num milagre, a "
            "lição ficava e o milagre não, mesmo que fosse preciso cortar no meio do versículo. O texto termina com "
            "o corpo de Jesus no sepulcro, fechado por uma grande pedra. Jefferson nunca publicou a obra nem a "
            "chamou de Bíblia. Contou da existência dela a poucos amigos e dizia lê-la antes de dormir. Uma versão "
            "anterior, de 1804, se perdeu: não resta nenhuma cópia. O exemplar completo passou ao neto dele e foi "
            "comprado em 1895 pelo Museu Nacional, em Washington. Em 1904, uma lei do Congresso mandou publicar uma "
            "reprodução, e daí até os anos 1950 os novos parlamentares recebiam um exemplar a cada dois anos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Jefferson_Bible",
            "Jefferson compiled the manuscripts but never published them. "
            "The first, The Philosophy of Jesus of Nazareth, was completed in 1804, but no copies exist today. "
            "The second, The Life and Morals of Jesus of Nazareth, was completed in 1820 by cutting and pasting, with a razor and glue, numerous sections from the New Testament as extractions of the doctrine of Jesus. "
            "Jefferson's condensed composition excludes all miracles by Jesus and most mentions of the supernatural, including sections of the four gospels that contain the Resurrection and most other miracles, and passages that portray Jesus as divine. [...] "
            "Jefferson never referred to his work as a Bible [...] "
            "Using a razor and glue, Jefferson cut and pasted his arrangement of selected verses from a 1794 bilingual Latin/Greek version using the text of the Plantin Polyglot, a French Geneva Bible and the King James Version of the gospels of Matthew, Mark, Luke, and John in chronological order—putting together excerpts from one text with those of another to create a single narrative. [...] "
            "For the teachings of Jesus he concentrated on his milder admonitions (the Sermon on the Mount) and his most memorable parables. [...] "
            "If necessary to exclude the miraculous, Jefferson would cut the text even in mid-verse. [...] "
            "If a moral lesson was embedded in a miracle, the lesson survived in Jeffersonian scripture, but the miracle did not. [...] "
            "And rolled a great stone to the door of the sepulchre, and departed. [...] "
            "he acknowledged the existence of The Life and Morals of Jesus of Nazareth to only a few friends, saying that he read it before retiring at night [...] "
            "was inherited by his grandson, Thomas Jefferson Randolph, and was acquired in 1895 by the National Museum in Washington. "
            "The book was later published as a lithographic reproduction by an act of the United States Congress in 1904. "
            "Beginning in 1904 and continuing every other year until the 1950s, new members of Congress were given a copy of the Jefferson Bible.",
            nome="Jefferson Bible")],
    },
    # 9 o rolo de Isaías e o anúncio no jornal
    {
        "temas_secundarios": ["primeiras_civilizacoes", "sistemas_escrita"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Um pastor que procurava um animal perdido perto do mar Morto atirou uma pedra e ouviu cerâmica quebrando. Ali surgiria um livro de Isaías de cerca de 125 a.C., uns mil anos mais velho que os manuscritos conhecidos.",
        "explicacao": (
            "A descoberta foi feita por três pastores beduínos entre o fim de 1946 e o início de 1947. O mais jovem, "
            "Muhammed edh-Dhib, voltou sozinho antes dos outros e achou uma caverna cheia de jarros, inteiros e "
            "quebrados, e pedaços de rolos. Era o começo dos Manuscritos do Mar Morto, que sairiam de 12 cavernas "
            "até 1956. O Grande Rolo de Isaías, em hebraico e em 17 folhas de pergaminho, traz quase o livro todo e "
            "é a cópia completa mais antiga que se conhece; antes dele, os manuscritos hebraicos mais antigos eram "
            "cerca de mil anos mais novos. O texto é, em geral, coerente com a versão massorética, a base das "
            "bíblias hebraicas, e tem os 66 capítulos na mesma ordem. Mesmo assim, há mais de 2.600 variantes, "
            "entre erros de copista, correções e diferenças em versículos. O caminho até os museus foi tortuoso: o "
            "rolo de Isaías foi um dos quatro que chegaram às mãos de um metropolita sírio-ortodoxo, Mar Samuel. Em "
            "1º de junho de 1954, quatro dos manuscritos foram postos à venda num anúncio do Wall Street Journal. "
            "Depois de negociações delicadas, foram comprados por 250 mil dólares e levados a Jerusalém."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Great_Isaiah_Scroll",
                "The scroll is written in Hebrew and contains almost the entire Book of Isaiah from beginning to end, apart from a few small damaged portions. "
                "Dating from ca. 125 BCE, it is the oldest known complete copy of the Book of Isaiah, being approximately 1000 years older than the previous oldest Hebrew manuscripts known before the scrolls' discovery. [...] "
                "The scroll is written on 17 sheets of parchment. [...] "
                "The scroll was discovered in Qumran Cave 1, by a group of three Ta'amireh shepherds, near the Ein Feshkha spring off the northwest shore of the Dead Sea between late 1946 and early 1947; "
                "initially discovered when one of the shepherds heard the sound of shattering pottery after throwing a rock while searching for a lost member of his flock. "
                "Once the shepherds agreed to return in a few days, the youngest one, Muhammed edh-Dhib returned alone before them, finding a cave filled with broken and whole jars and fragments of scrolls. [...] "
                "The text of the Great Isaiah Scroll is generally consistent with the Masoretic version and preserves all sixty-six chapters of the Hebrew version in the same sequence. [...] "
                "The scroll contains scribal errors, corrections, and more than 2600 textual variants when compared with the Masoretic codex. [...] "
                "Some variants are significant and include differences in one or more verses",
                nome="Great Isaiah Scroll"),
            wiki("Dead_Sea_Scrolls",
                "The Dead Sea Scrolls were discovered in a series of 12 caves around the site originally known as Ein Feshkha near the Dead Sea in the West Bank (then controlled by Jordan) between 1946 and 1956 by Bedouin shepherds and a team of archaeologists. [...] "
                "George Isha'ya, was a member of the Syriac Orthodox Church [...] "
                "News of the find then reached Metropolitan Athanasius Yeshue Samuel, better known as Mar Samuel. [...] "
                "Four scrolls found their way into his hands: the Isaiah Scroll (1QIsaa), the Community Rule, the Habakkuk Pesher (a commentary on the book of Habakkuk), and the Genesis Apocryphon. [...] "
                "Four of the Dead Sea Scrolls eventually went up for sale in an advertisement on 1 June 1954, The Wall Street Journal. "
                "On 1 July 1954, the scrolls, after delicate negotiations and accompanied by three people including Mar Samuel, arrived at the Waldorf-Astoria Hotel in New York. "
                "They were purchased by Professor Mazar and the son of Professor Sukenik, Yigael Yadin, for $250,000 (approximately $3,000,000 in 2025 dollars), and brought to Jerusalem.",
                nome="Dead Sea Scrolls"),
        ],
    },
    # 10 os 16 fragmentos falsos do Museu da Bíblia
    {
        "temas_secundarios": ["crimes_arte", "primeiras_civilizacoes"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "O Museu da Bíblia, nos EUA, abriu as portas exibindo 16 fragmentos dos Manuscritos do Mar Morto. Em 2020, as análises confirmaram: todos eram falsificações modernas.",
        "explicacao": (
            "Os fragmentos de pergaminho foram doados pelo fundador do museu, Steve Green, para a inauguração. "
            "Assim que o catálogo foi divulgado, especialistas de fora estranharam que a procedência das peças não "
            "estivesse bem documentada, e Årstein Justnes, professor de estudos bíblicos da Universidade de Agder, "
            "na Noruega, afirmou que eram falsificações. O museu encomendou análises a um instituto federal alemão "
            "de pesquisa e teste de materiais, mas manteve os fragmentos em destaque na abertura, com testes ainda "
            "incompletos e uma placa dizendo que os estudiosos continuavam a debater a autenticidade. Em 2018, "
            "anunciou que 5 dos 16 eram falsos e os tirou da exposição: segundo os pesquisadores alemães, tinham "
            "características incompatíveis com uma origem antiga. Em março de 2020, todos os 16 estavam confirmados "
            "como falsificações modernas. Eles pertencem a um grupo de cerca de 70 fragmentos que apareceram no "
            "mercado a partir de 2002, provavelmente todos falsos. A história mostra quanto pesa a procedência: "
            "desde 2002, muitos falsos manuscritos do mar Morto surgiram no mercado negro."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Museum_of_the_Bible",
                "Founder Steve Green donated purported Dead Sea Scrolls parchment fragments to the museum collection for its opening. "
                "When the museum catalog was released to the public, however, several outside experts expressed concern that the museum had not adequately accounted for the fragments' provenance. "
                "Arstein Justnes, a professor of biblical studies at the University of Agder in Norway, declared they were outright forgeries. "
                "The museum subsequently enlisted the German Federal Institute for Materials Research and Testing (Bundesanstalt für Materialforschung und Prüfung) to analyze the scrolls. "
                "The museum kept the fragments prominently on display for its official opening, while testing was still incomplete. "
                "The text of display stated that \"scholars continue to debate the authenticity of this fragment\". "
                "In 2018 the museum announced that expert examination had led it to conclude that five of the sixteen fragments of the Dead Sea Scrolls were forgeries and that the museum had removed them from display. "
                "According to the German researchers, those five showed \"characteristics inconsistent with ancient origin\". "
                "By March 2020, all 16 fragments displayed at the museum were confirmed to be modern forgeries. "
                "The forgeries are part of a group of about 70 fragments of the Dead Sea Scrolls which came onto the market in 2002, all of which are likely forgeries",
                nome="Museum of the Bible"),
            wiki("Dead_Sea_Scrolls",
                "Since 2002, many forgeries of Dead Sea Scrolls have appeared on black markets.",
                nome="Dead Sea Scrolls"),
        ],
    },
    # 11 o "Arquivo Secreto" que era só particular
    {
        "temas_secundarios": ["palavras_viajantes", "europa_medieval"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "O \"Arquivo Secreto do Vaticano\" não tinha esse nome por esconder segredos: \"secreto\" estava no sentido antigo de \"particular\", pois o acervo pertence ao papa. Em 2019, Francisco o rebatizou de Arquivo Apostólico.",
        "explicacao": (
            "O arquivo guarda os atos promulgados pela Santa Sé, e o papa, como soberano do Vaticano, é dono do "
            "material até morrer ou renunciar. A palavra \"secreto\" do nome antigo não indicava confidencialidade "
            "no sentido moderno: uma tradução mais fiel seria algo como \"arquivo apostólico particular\", sinal "
            "de que o acervo é propriedade pessoal do papa, e não de algum departamento da Cúria Romana. Há, sim, "
            "partes fechadas a quem é de fora, sobretudo o que trata de pessoas e assuntos recentes, como tudo o "
            "que é posterior a 1958. Durante séculos o arquivo ficou fechado a estranhos, até que o papa Leão XIII "
            "o abriu aos pesquisadores no fim do século XIX; a sala de leitura foi inaugurada em 1º de janeiro de "
            "1881. Hoje, mais de mil estudiosos consultam documentos ali a cada ano. Estima-se que haja 85 "
            "quilômetros de estantes. Entre as peças conhecidas estão o pedido de Henrique VIII da Inglaterra para "
            "anular o casamento, uma transcrição manuscrita do julgamento de Galileu por heresia e cartas em que "
            "Michelangelo reclama de não ter sido pago pelo trabalho na Capela Sistina. A troca de nome foi feita "
            "pelo papa Francisco em outubro de 2019."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Vatican_Apostolic_Archive",
            "The Vatican Apostolic Archive (Latin: Archivum Apostolicum Vaticanum; Italian: Archivio Apostolico Vaticano), formerly known as the Vatican Secret Archive (Latin: Archivum Secretum Vaticanum; Italian: Archivio Segreto Vaticano), is the central repository in the Vatican City of all acts promulgated by the Holy See. "
            "The Pope, as the sovereign of Vatican City, owns the material held in the archive until his death or resi [...] "
            "the archive remained closed altogether to outsiders until the late 19th century, when Pope Leo XIII opened the archive to researchers, more than a thousand of whom now examine some of its documents each year. [...] "
            "The use of the word secret in the former title, \"Vatican Secret Archive\", does not denote the modern meaning of confidentiality. "
            "A fuller and perhaps better translation of the archive's former Latin name may be the \"private Vatican Apostolic archive\", indicating that its holdings are the pope's personal property, not those of any particular department of the Roman Curia or the Holy See. [...] "
            "most of these classified materials, which are actively denied to outsiders, relate to contemporary personalities and activities, including everything dated after 1958 [...] "
            "On 28 October 2019, Pope Francis issued an Apostolic Letter motu proprio dated 22 October, renaming the archives from the Vatican Secret Archive to the Vatican Apostolic Archive. [...] "
            "Pope Leo ordering a reading room constructed for researchers; it opened on 1 January 1881. [...] "
            "The Vatican Apostolic Archive has been estimated to contain 85 kilometres (53 mi) of shelving [...] "
            "Notable documents include Henry VIII of England's request for a marriage annulment, a handwritten transcript of the trial of Galileo for heresy, and letters from Michelangelo complaining he had not been paid for work on the Sistine Chapel.",
            nome="Vatican Apostolic Archive")],
    },
    # 12 Simeão, 36 anos no alto de uma coluna
    {
        "temas_secundarios": ["roma_antiga", "costumes_rituais"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "No século V, o monge sírio Simeão viveu 36 anos no alto de colunas, perto de Aleppo. Subiu para fugir das multidões, mas atraiu ainda mais gente, e até um imperador ouvia seus conselhos.",
        "explicacao": (
            "Filho de um pastor, Simeão levou a vida ascética a tal extremo que os colegas do mosteiro julgaram que "
            "ele não servia para a vida em comunidade e lhe pediram que fosse embora. Passou então a viver numa "
            "encosta rochosa, mas os peregrinos não paravam de procurá-lo em busca de conselhos e orações, e lhe "
            "sobrava pouco tempo para as devoções. A saída foi subir numa coluna que restava entre ruínas. A "
            "primeira tinha pouco mais de 3 metros; ele trocou de plataforma algumas vezes, e a última, segundo os "
            "relatos, passava de 15 metros. No topo havia uma plataforma que, acredita-se, tinha cerca de um metro "
            "quadrado e uma grade em volta. O efeito foi o contrário do planejado: chegavam ainda mais peregrinos e "
            "curiosos. Todas as tardes ele conversava com visitantes, que subiam uma escada até ficar ao alcance da "
            "voz. Escrevia cartas, orientava discípulos e pregava contra a usura. O imperador Teodósio II e a "
            "esposa o tinham em alta conta. Outros ascetas imitaram seu modelo e ficaram conhecidos como estilitas, "
            "da palavra grega para coluna. As ruínas do enorme conjunto erguido em sua honra, quatro basílicas em "
            "forma de cruz em torno da base da coluna, ainda podem ser vistas a cerca de 30 km de Aleppo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Simeon_Stylites",
            "c. 390 – 2 September 459) was a Syrian Christian ascetic who achieved notability by living 36 years on top of a pillar near Aleppo (in modern Syria). "
            "Several other stylites later followed his model (the Greek word style means \"pillar\"). [...] "
            "The son of a shepherd, Simeon was born and raised in Sis [...] "
            "From the first day, he gave himself up to the practice of an austerity so extreme that his brethren judged him to be unsuited to any form of community life. "
            "They asked Simeon to leave the monastery. [...] "
            "Simeon sought a rocky eminence on the slopes of what is now the Sheik Barakat Mountain [...] "
            "But crowds of pilgrims invaded the area to seek him out, asking his counsel or his prayers, and leaving him insufficient time for his own devotions. [...] "
            "Simeon discovered a pillar which had survived among ruins in nearby Telanissa [...] "
            "The first pillar that Simeon occupied was little more than 3 meters (10 ft). "
            "He later moved his platform to others, the last in the series reportedly more than 15 meters (50 ft) from the ground. "
            "At the top of the pillar was a platform, which is believed to have been about one square meter and surrounded by a baluster. [...] "
            "If anything, the new pillar attracted even more people, both pilgrims who had earlier visited him and sightseers as well. "
            "Simeon was available each afternoon to talk with visitors. "
            "By means of a ladder, visitors were able to ascend within speaking distance. "
            "It is known that he wrote letters, the text of some of which have survived to this day, that he instructed disciples, and that he also lectured to those assembled beneath. "
            "He especially preached against profanity and usury. [...] "
            "The Emperor Theodosius II and his wife Aelia Eudocia greatly respected Simeon and listened to his counsels [...] "
            "The ruins of the vast edifice erected in his honour and known in Arabic as the Qalaat Semaan (\"the Fortress of Simeon\") can still be seen. "
            "They are located about 30 km northwest of Aleppo [...] "
            "consist of four basilicas built out from an octagonal court towards the four points of the compass to form a large cross. "
            "In the centre of the court stands the base of the style or column on which Simeon stood.",
            nome="Simeon Stylites")],
    },
    # 13 John Frum e o Exército de Tanna
    {
        "temas_secundarios": ["segunda_guerra", "costumes_rituais"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Na ilha de Tanna, em Vanuatu, seguidores de John Frum, figura retratada como um militar americano da Segunda Guerra, desfilam todo 15 de fevereiro com armas de bambu, à espera da volta dele.",
        "explicacao": (
            "O movimento surgiu no máximo no fim dos anos 1930, quando Vanuatu ainda se chamava Novas Hébridas. "
            "Ganhou força no começo dos anos 1940, quando 50 mil soldados americanos se instalaram no arquipélago, "
            "com uma quantidade enorme de suprimentos, a \"carga\". Cerca de 10 mil homens locais trabalharam num "
            "batalhão de mão de obra dos EUA. É um dos chamados cultos da carga: John Frum traria riqueza e "
            "prosperidade a quem o seguisse. Uma interpretação lê o nome como \"John from (America)\", embora possa "
            "indicar alguém vindo de qualquer lugar fora dali. Em 1957, líderes do movimento criaram o \"Exército de "
            "Tanna\", uma tropa não violenta com bonés que imitavam os americanos, as letras \"T-A USA\" no peito e "
            "fuzis de bambu com baionetas entalhadas. O desfile anual acontece na data em que os fiéis acreditam "
            "que John Frum voltará. Em 1959, o naturalista David Attenborough perguntou a um seguidor por que ele "
            "ainda esperava a carga, prometida 19 anos antes. A resposta: quem espera 2 mil anos pela volta de "
            "Jesus pode esperar mais de 19 por John. A crença está em declínio: segundo relatos, eram mais de 5 mil "
            "membros nos anos 1990, e menos de 500 em 2022."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("John_Frum",
            "John Frum (also called Jon Frum, John Brum, and John Prum) is a figure associated with cargo cults on the island of Tanna in Vanuatu (formerly the New Hebrides). "
            "He is often depicted as an American World War II serviceman who will bring wealth and prosperity to the people if they follow him. [...] "
            "In the 1990s, there were reportedly over 5,000 members of the John Frum movement. "
            "However, belief in John Frum is in decline; as of 2022, there are fewer than 500 practitioners. [...] "
            "The religion centering on John Frum arose no later than the late 1930s, when Vanuatu was known as the New Hebrides. [...] "
            "the movement gained popularity in the early 1940s after 50,000 American troops were stationed in Vanuatu during World War II, bringing with them an enormous amount of supplies (or \"cargo\"). "
            "During the war, approximately 10,000 Ni-Vanuatu men served in the Vanuatu Labor Corps, a labor battalion of the United Stat [...] "
            "Versions of the cult emphasizing the American connection interpret \"John Frum\" as a corruption of  \"John from (America)\" (although it could mean \"John from\" anywhere outside Vanuatu). "
            "In 1957, leaders of the John Frum movement created the \"Tanna Army\", a non-violent faux army that organized military-style parades with men wearing imitation American caps, long trousers, singlets across their chests with the letters \"T-A USA\" (Tanna Army USA), and carried imitation bamboo guns with carved bayonets. [...] "
            "A Tanna Army parade takes place every year on February 15, the date on which followers believe John Frum will return [...] "
            "In 1959, when David Attenborough asked one of the followers why he was still waiting for the cargo after it had been 19 years since it was promised and had not arrived, the man said \"If you can wait two thousand years for Jesus Christ to come 'an 'e no come, then I can wait more than nineteen years for John.\"",
            nome="John Frum")],
    },
    # 14 os samaritanos e o geneticista
    {
        "temas_secundarios": ["genetica", "primeiras_civilizacoes"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Os samaritanos, os da parábola do bom samaritano, ainda existem: são cerca de 900. Como a comunidade é minúscula, todo casamento passa antes pelo aval de um geneticista, para evitar doenças hereditárias.",
        "explicacao": (
            "Eles seguem uma religião aparentada ao judaísmo, mas aceitam como escritura sagrada só a Torá "
            "samaritana e creem que o santuário escolhido por Deus é o monte Gerizim, e não o Monte do Templo, em "
            "Jerusalém. A peregrinação ao Gerizim inclui o sacrifício da Páscoa, o rito mais famoso do grupo. Na "
            "Antiguidade, os samaritanos eram a principal população da Samaria, mas revoltas fracassadas, a "
            "repressão bizantina e, mais tarde, conversões forçadas ao islã reduziram drasticamente seu número: em "
            "1919, eram 141. Desde então, a população voltou a crescer. Em 2024, os cerca de 900 se dividiam entre "
            "Holon, perto de Tel Aviv, e Kiryat Luza, no próprio monte Gerizim, perto de Nablus. Com só quatro "
            "famílias e a recusa geral de aceitar convertidos, é comum casar dentro da família ampliada, até entre "
            "primos, e há histórico de doenças genéticas no grupo. Por isso, todos os casamentos são aprovados "
            "antes por um geneticista do Hospital Tel HaShomer. Para ampliar a variedade genética, a comunidade "
            "também passou a admitir noivas de fora, como judias israelenses e algumas mulheres da Rússia e da "
            "Ucrânia, desde que sigam as práticas samaritanas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Samaritans",
            "Samaritans recognize only the Samaritan Torah as sacred scripture, rejecting most of the later Jewish canon as well as rabbinic tradition, and their central theological distinction from Judaism is the belief that Mount Gerizim, not the Temple Mount in Jerusalem, is God's chosen sanctuary. "
            "Their religion is centered on the hereditary high priesthood, strict observance of biblical law and festivals, and pilgrimages to Mount Gerizim, most famously the Passover sacrifice. "
            "In classical antiquity, the Samaritans were the principal population of Samaria, but their numbers were drastically reduced following a series of failed revolts and severe Byzantine repression [...] "
            "but their population has grown since, reaching around 900 people as of 2024; they are one of the world's smallest surviving ethnoreligious groups, concentrated mainly in Kiryat Luza on Mount Gerizim near Nablus (ancient Shechem) and in the neighborhood of Neve Pinchas in Holon near Tel Aviv. [...] "
            "many Samaritan families were forced to convert to Islam during that time. [...] "
            "There were 100 in 1786 and 141 in 1919, then 150 in 1967. [...] "
            "the parable of the Good Samaritan. [...] "
            "With such a small population, divided into only four families or houses (Cohen, Tsedakah, Danafi, and Marhiv, with the Matar family dying out in 1968), and a general refusal to accept converts, it is common for Samaritans to marry within their extended families, even first cousins. "
            "There has been a history of genetic disorders within the group due to the small gene pool. "
            "To counter this, the Holon Samaritan community has allowed men from the community to marry non-Samaritan (primarily Israeli Jewish) women, provided that the women agree to follow Samaritan religious practices. [...] "
            "all marriages within the Samaritan community are first approved by a geneticist at Tel HaShomer Hospital, in order to prevent the spread of genetic disorders. "
            "In meetings arranged by \"international marriage agencies\", a small number of women from Russia and Ukraine who agree to observe Samaritan religious practices have been allowed to marry into the Qiryat Luza Samaritan community in an effort to expand the gene pool.",
            nome="Samaritans")],
    },
    # 15 são Cristóvão com cabeça de cachorro
    {
        "temas_secundarios": ["pintura", "europa_medieval"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "Na arte bizantina, são Cristóvão às vezes aparece com cabeça de cachorro. As lendas mais antigas o descrevem como um cinocéfalo, um \"homem-cão\" de uma tribo que comia carne humana, antes da conversão.",
        "explicacao": (
            "No Ocidente, a imagem mais comum é a de um gigante com um cajado, atravessando um rio com o menino "
            "Jesus no ombro. Não há, porém, nenhuma prova de que o santo tenha existido, e as lendas variam. A "
            "tradição oriental, mais antiga, dá ao Cristóvão de antes da conversão uma natureza feroz e traços de "
            "animal, em especial a cabeça de cão. A ocidental, mais recente, insiste menos nisso e destaca o "
            "tamanho, a falta de cultura e a feiura. Numa versão antiga, um certo Reprebos, capturado pelos "
            "romanos e obrigado a servir numa unidade militar, é um cinocéfalo de uma tribo de canibais que não "
            "sabe falar a língua deles; depois de rezar, recebe o dom da fala. O bispo e poeta alemão Walter de "
            "Speyer o retratou como um gigante dessa espécie, que comia carne humana e latia. Ao encontrar o menino "
            "Jesus, ele se arrepende, é batizado e ganha aparência humana. Não se sabe quando essas imagens "
            "começaram, porque boa parte da arte cristã antiga foi destruída nas ondas de iconoclastia bizantina "
            "dos séculos VIII e IX. Na liturgia católica, a comemoração dele saiu do calendário geral em 1970 e "
            "ficou restrita a calendários particulares."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Saint_Christopher",
            "the older Eastern tradition describes the pre-conversion Christopher as having a ferocious nature and animal features (in particular, the head of a dog) while the younger Western tradition does not dwell as much on these animal-like mental and physical features but rather emphasizes the lack of culture, the giant size and the ugliness of the saint. [...] "
            "In the iconography of Western Christianity, the saint is often depicted as a giant with a staff crossing a river with the infant Jesus on his shoulder. "
            "In Byzantine art, the saint is depicted in various guises including as a young man, a martyr in a red himation with a cross in his hand, a warrior on horseback or a man with the head of a dog in line with the early legendary tradition. [...] "
            "There is no evidence for the historicity of the saint. [...] "
            "A certain Reprebos is captured by the Romans in battle and then forced to join the Roman numerus Marmaritarum, i.e. a military unit made up by Marmaritae people. "
            "Reprebos is a physically repulsive Cynocephalus (i.e. a man with a dog's head) from a tribe of cannibals who is incapable of speaking \"our language\". "
            "After praying to his God he is granted the gift of language. [...] "
            "The German bishop and poet Walter of Speyer portrayed St. Christopher in his Vita et passio sancti Christopher martyris as a giant of a cynocephalic species in the land of the Chananeans who ate human flesh and barked. "
            "Eventually, Christopher meets the infant Jesus, regrets his former behavior and receives baptism. "
            "He is further rewarded with a human appearan [...] "
            "It is not clear when this type of representation started as most early Christian artworks were destroyed during the 8th and 9th century Byzantine Iconoclasms. [...] "
            "it was dropped in 1970 from the general calendar and restricted to particular calendars of the Roman rite.",
            nome="Saint Christopher")],
    },
    # 16 o Natal proibido pelos puritanos
    {
        "temas_secundarios": ["calendarios", "costumes_rituais"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Em 1659, comemorar o Natal virou infração em Boston, com multa de cinco xelins. Os puritanos viam a festa como sem base na Bíblia. A proibição caiu em 1686, e o Congresso dos EUA só a fez feriado em 1870.",
        "explicacao": (
            "A aversão veio da Inglaterra. Calvinistas, os puritanos queriam tirar do cristianismo o que "
            "consideravam sem base bíblica, incluindo as festas estabelecidas pela Igreja Anglicana. Em 1647, o "
            "Parlamento inglês, controlado por eles, proibiu a celebração do Natal e pôs no lugar um dia de jejum, "
            "tratando a data como uma \"festa papista\" e uma época de desperdício e mau comportamento. Na América, "
            "os peregrinos de Plymouth mostraram o desprezo pela data em 1620: passaram o primeiro Natal no Novo "
            "Mundo construindo a primeira casa. Em Boston, a proibição de 1659 também valeu para New Hampshire e o "
            "Maine, então controlados por Massachusetts. Ela foi revogada em New Hampshire em 1683 e em "
            "Massachusetts em 1686, por Edmund Andros, governador nomeado pela Inglaterra. Mesmo assim, o Natal só "
            "virou moda na região de Boston em meados do século XIX, e antes da independência, em 1776, ele não era "
            "muito comemorado nas colônias americanas. Quem não era puritano lamentava a perda dos feriados de que "
            "os trabalhadores desfrutavam na Inglaterra."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Christmas_in_Puritan_New_England",
            "The Puritans as Calvinists objected to the Christian feast of Christmas. [...] "
            "Puritans sought to remove elements they viewed as unbiblical, from their practice of Christianity, including those feasts established by the Anglican Church. "
            "In 1647, the Puritan-led English Parliament banned the celebration of Christmas, replacing it with a day of fasting and considering it \"a popish festival with no biblical justification\", and a time of wasteful and immoral behavi [...] "
            "The Plymouth Pilgrims put their loathing for the day into practice in 1620 when they spent their first Christmas Day in the New World building their first structure in the New World—thus demonstrating their complete contempt for the day. "
            "Non-Puritans in New England deplored the loss of the holidays enjoyed by the laboring classes in England. "
            "Christmas observance was outlawed in Boston in 1659 in light of the impending Restoration with a fine of five shillings. "
            "It was also banned in the Province of New Hampshire and Maine, which were controlled by Massachusetts. "
            "The ban by the Puritans was revoked in New Hampshire in 1683 by Edward Cranfield and in Massachusetts in 1686 by an English appointed governor, Edmund Andros; however, it was not until the mid-19th century that celebrating Christmas became fashionable in the Boston region. "
            "Before the Declaration of Independence in 1776, it was not widely celebrated in the American Colonies. [...] "
            "Christmas was not proclaimed a holiday by the United States Congress until 1870.",
            nome="Christmas in Puritan New England")],
    },
]
