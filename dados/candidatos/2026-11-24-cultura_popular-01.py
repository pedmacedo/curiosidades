LOTE = "2026-11-24-cultura_popular-01"
AREA = "brasil"
TEMA = "cultura_popular"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Parintins: a Coca-Cola azul e a torcida que vale nota
    {
        "temas_secundarios": ["amazonia", "teatro_danca"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "No festival de Parintins (AM), a rivalidade entre os bois Garantido, vermelho, e Caprichoso, azul, faz até a Coca-Cola trocar de cor: a marca aparece em azul para conversar com a torcida do Caprichoso.",
        "explicacao": (
            "O festival nasceu em 1965, organizado por jovens católicos para juntar dinheiro para a catedral da "
            "cidade. Garantido e Caprichoso, que já eram rivais, nem foram convidados naquele ano; estrearam em 1966, "
            "apresentando-se separados por medo de briga entre as torcidas. O primeiro duelo, em 1967, foi decidido "
            "no aplauso do público, e um corpo de jurados só entrou em 1970. Os dois bois adaptam o bumba-meu-boi, "
            "com a morte e a ressurreição de um boi, em espetáculos de arena com lendas amazônicas e referências "
            "indígenas, num bumbódromo para 35 mil pessoas. A própria torcida, chamada de galera, é um dos itens "
            "julgados: ganha nota alta se mostrar animação e sincronia nas coreografias. A rivalidade transborda "
            "para o comércio. Marcas tradicionalmente vermelhas, como a Coca-Cola, aparecem em azul em pontos "
            "ligados ao Caprichoso, e marcas azuis, como Nestlé e Visa, adotam o vermelho do Garantido. Não é uma "
            "mudança da identidade global da Coca-Cola, e sim uma adaptação local ao clima da festa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Parintins_Folklore_Festival",
                "it centres on competitive performances by the boi-bumbá associations Boi Garantido and Boi Caprichoso. "
                "The festival adapts elements of the Bumba-meu-boi tradition, especially the story of the death and resurrection of a bull, into large-scale arena spectacles. "
                "Caprichoso, whose colours are blue and white, and Garantido, whose colours are red and white. present themed productions combining toadas (songs), percussion, dance, theatrical narrative, costumes, scenery, Amazonian legends, and references to Indigenous cultures. [...] "
                "During the festival period, businesses and national brands frequently adapt their visual identities to the colors associated with the competing associations: blue for Caprichoso and red for Garantido. "
                "This practice is particularly visible in the case of Coca-Cola, whose standard corporate color is red. [...] "
                "In Parintins, Coca-Cola's branding can consequently appear in blue in locations associated with Caprichoso, a striking departure from the company's conventional global visual identity. [...] "
                "Rather than representing a permanent change to Coca-Cola's global branding, the blue Coca-Cola imagery is a localized adaptation to the cultural context of the festival. [...] "
                "Garantido and Caprichoso had developed a local rivalry before the creation of the festival [...] "
                "The first Parintins Folklore Festival was held in 1965. It was organised by young people associated with Juventude Alegre Católica (JAC) to raise funds for the construction of the Cathedral of Our Lady of Mount Carmel [...] "
                "Garantido and Caprichoso were not invited, and there was no contest between them. "
                "In 1966, Garantido and Caprichoso participated in the festival for the first time. "
                "Their appearances were not yet organised as a regular title contest: the associations performed separately, reflecting concerns about confrontations between their supporters. [...] "
                "The first competitive encounter between the two associations occurred on 24 June 1967. "
                "After the two presentations, the master of ceremonies invited the audience to indicate, by applause, which performance it preferred. [...] "
                "the festival entered a new phase in 1970 with the introduction of a judging panel to evaluate the performances of the two bulls.",
                nome="Parintins Folklore Festival"),
            wiki("Festival_Folclórico_de_Parintins",
                "Centro Cultural de Parintins — mais conhecido como Bumbódromo, com capacidade para 35 mil espectadores. [...] "
                "Galera  Conjunto de torcedores dispostos nas arquibancadas laterais gratuitas. Pessoas que formam coreografias uníssonas e organizadas no contexto do espetáculo. "
                "Para ser considerada uma galera com nota alta, o tem precisa mostrar animação, sincronia [...] "
                "empresas adaptam suas identidades visuais às cores dos bois. "
                "Marcas historicamente vermelhas, como a Coca-Cola, transfiguram-se em azul para dialogar com o Boi Caprichoso, enquanto marcas de identidade azul, como: Telemar, Derby, Cielo, Visa, Trip, Nestlé, Azul Linhas Aéreas assumem o vermelho em homenagem ao Boi Garantido.",
                nome="Festival Folclórico de Parintins", idioma="pt"),
        ],
    },
    # 2 a corda do Círio de Nazaré
    {
        "temas_secundarios": ["religioes", "amazonia"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "A corda de 400 metros que os fiéis puxam no Círio de Nazaré, em Belém, nasceu de um improviso: em 1855, a água da baía transbordou no caminho da procissão, e a berlinda da santa precisou ser puxada.",
        "explicacao": (
            "O Círio acontece em Belém desde 1793, no segundo domingo de outubro, e reúne hoje cerca de dois milhões "
            "de pessoas. O nome vem do latim cereum, \"vela grande\": no começo, a procissão era noturna, à luz de "
            "velas, e só passou para a manhã em 1854, por causa das chuvas fortes do ano anterior. Até então, a "
            "imagem de Nossa Senhora de Nazaré ia num palanquim, nas mãos de um capelão. Em 1855 ela passou a ir "
            "numa carruagem, que era puxada por cavalos. Naquele ano, a água da Baía do Guajará transbordou na área "
            "do Ver-o-Peso, e uma corda entrou na procissão para puxar a berlinda. O improviso só foi oficializado em "
            "1868. Nem sempre agradou: entre 1926 e 1930, quando a berlinda foi trocada por um andor, a corda também "
            "saiu de cena, sob o pretexto de que era violenta, e voltou em 1931. Hoje ela tem duas polegadas de "
            "diâmetro e é dividida em cinco estações, como o rosário católico. O Círio foi registrado pelo Iphan em "
            "2004 e reconhecido pela UNESCO em 2013."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Círio_de_Nazaré",
                "It has been observed annually since 1793, on the second Sunday of October, and currently attracts approximately two million participants. [...] "
                "In Brazil, it was originally an evening or nighttime pilgrimage, which explains the use of candles. "
                "In 1854, to avoid the heavy rainfall that had occurred the previous year, the procession was moved to the morning.",
                nome="Círio de Nazaré"),
            wiki("Círio_de_Nazaré",
                "A corda do círio foi introduzida pela primeira vez na procissão em 1855 com o objetivo de puxar a berlinda que levava a imagem de Nossa Senhora de Nazaré devido a água que transbordava da Baía do Guajará na área do Ver-o-peso. "
                "O elemento só foi oficializado em 1868. [...] "
                "Desde 2004, a corda utiliza um formato linear, com cinco estações confirme o rosário católico, além do núcleo da cabeça que inicia a corda e o núcleo da berlinda que leva a imagem peregrina. "
                "A corda possui 400 metros de comprimento e duas polegadas de diâmetro. [...] "
                "até 1854, a imagem de Nossa Senhora de Nazaré era carregada no colo de um capelão do Palácio do Governo em um palanquim, carregado por quatro ou seis homens. "
                "Em 1855, a imagem passou a ser levada por uma carruagem, que servia como uma espécie de berlinda. [...] "
                "Até a introdução da corda, o carro era puxado por cavalos. "
                "Em 1926, a berlinda é substituída por um andor, fruto de mudanças sugeridas pelo então Arcebispo de Belém, Dom João Irineu Joffily, ficando até 1930, quando voltou a ser utilizada. "
                "Entre esse período, a corda também deixou de ser utilizada com um pretexto de ser violenta, voltando em 1931 junto com a berlinda. [...] "
                "Foi, em 2004, reconhecido como patrimônio cultural imaterial pelo Instituto do Patrimônio Histórico e Artístico Nacional (Iphan) e, em 2013, declarado Patrimônio Cultural da Humanidade pela UNESCO. [...] "
                "O termo \"círio\" vem do latim \"cereum\", que significa \"vela grande\".",
                nome="Círio de Nazaré", idioma="pt"),
        ],
    },
    # 3 a quadrilha e o francês do anarriê
    {
        "temas_secundarios": ["teatro_danca", "palavras_viajantes"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "\"Anarriê\", \"alavantu\" e \"balancê\" são francês abrasileirado: en arrière (para trás), en avant tous (todos para a frente) e balancer. A quadrilha junina descende de uma dança dos salões aristocráticos.",
        "explicacao": (
            "A quadrille era uma dança de salão para quatro pares em formação retangular, com seu auge no século "
            "XIX, quando fazia parte do protocolo dos bailes das cortes europeias. Câmara Cascudo a chamou de \"a "
            "grande dança palaciana do séc. XIX\" e contou que ela chegou ao Brasil trazida por mestres de orquestra "
            "franceses. Aqui a dança se esticou: ganhou comandos inesperados, gritados por um marcante, e se "
            "espalhou da Corte Imperial até os sertões. Os comandos guardam a origem. Além do anarriê e do "
            "alavantu, há o changê (de changer, trocar o par), o returnê (voltar ao lugar) e o tur (de tour, dar uma "
            "volta). Segundo a pesquisadora Ana Valéria, do curso de Dança da Universidade Federal da Paraíba, com a "
            "queda da Monarquia a elite cultural passou a recusar o que lembrava a Corte, e a quadrilha se manteve "
            "entre os mais pobres e nas regiões rurais, dançada para celebrar a colheita do milho. Nas escolas dos "
            "anos 1950, ela ainda ganhou a caricatura do homem do campo, de roupa remendada e dente preto."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Quadrilha_(dança)",
                "Quadrilha (do francês quadrille) é uma modalidade de dança de salão que, no dizer de Câmara Cascudo, foi \"a grande dança palaciana do séc. XIX\". "
                "Era originalmente dançada por quatro pares em formação retangular. [...] "
                "teve seu auge no século XIX [...] "
                "No século XIX era uma dança que compunha o protocolo dos bailes palacianos das cortes europeias [...] "
                "\"trazida por mestres de orquestras de dança francesas, como Milliet e Cavallier, que tocavam as músicas de Musard, \"o pai das quadrilhas\", e Tolbecque\", no registro de Cascudo. "
                "Sua popularização no Brasil fez com que sua execução em cinco partes ganhasse comandos inesperados e grande duração que terminavam por se constituir no próprio baile (e não uma das danças dele); "
                "esses comandos eram gritados pelo \"marcante\", muitas vezes com repetições e sua prática se espalhou desde a Corte Imperial aos sertões.",
                nome="Quadrilha (dança)", idioma="pt"),
            {"url": "https://ufs.br/uploads/page_attach/path/8705/quadrilha.pdf",
             "titulo": "Quadrilha: uma tradição francesa, com certeza! (Universidade Federal de Sergipe)",
             "idioma": "pt",
             "trecho": "Anavã ou Alavantú (en avant/ tous)- todos os casais vão para a frente. [...] "
                       "Anarriê (en arrière) – casais vão para trás. [...] "
                       "Changê (changer/changez) – trocar/troquem o par. [...] "
                       "Balancê (balancer) – balançar o corpo no ritmo da música, marcando o passo, sem sair do lugar. [...] "
                       "Returnê (returner) – voltar aos seus lugares. [...] "
                       "Tur (tour) – dar uma volta"},
            {"url": "https://www.brasildefato.com.br/2023/06/22/quadrilha-conheca-a-historia-de-um-dos-simbolos-das-festas-juninas/",
             "titulo": "Quadrilha: conheça a história de um dos símbolos das festas juninas (Brasil de Fato)",
             "idioma": "pt",
             "trecho": "a pesquisadora e professora do Curso de Dança da Universidade Federal da Paraíba (UFPB), Ana Valéria, explicou que com a destituição da Monarquia e a chegada da República, os elementos ligados ao imaginário da Corte Portuguesa foram recusados pela então elite cultural. "
                       "\"Foi nesse período que a prática da dança da quadrilha começou a se manter nas populações mais pobres e regiões rurais, onde se dançava em celebração à colheita do milho, criando assim uma tradição\" [...] "
                       "a dança acabou ganhando um aspecto \"caricatural\" no meio urbano, principalmente por contrastar com uma visão de Brasil que, nos anos de 1950 [...] "
                       "nas escolas as quadrilhas eram inseridas com esse homem sendo tratado de forma pejorativa e caricatural: pobre, de roupa remendada, dente preto"},
        ],
    },
    # 4 o curupira de Anchieta, 1560
    {
        "temas_secundarios": ["mitologia", "povos_indigenas"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "O registro mais antigo do curupira, de José de Anchieta em 1560, não fala de um duende travesso: descreve demônios que atacavam indígenas na mata com açoites, até matá-los, e que eram aplacados com oferendas.",
        "explicacao": (
            "Na carta escrita em São Vicente em 30 de maio de 1560, Anchieta conta que era coisa sabida por todos: "
            "certos demônios, chamados corupira, atacavam os indígenas no mato, feriam-nos com açoites e os matavam. "
            "Para aplacá-los, os indígenas subiam ao alto de um monte e deixavam penas de aves, abanos e flechas. Em "
            "1584, outro jesuíta, Fernão Cardim, escreveu que o curupira era o demônio mais temido, embora não lhe "
            "fizessem ídolos. Com a influência europeia, essa figura temida, que deixava corpos marcados, foi "
            "virando um espírito trapaceiro e meio atrapalhado, que muitas vezes é enganado pelos humanos. Hoje ele "
            "é o guardião da floresta, que faz se perder quem derruba árvores sem necessidade. Os pés virados para "
            "trás deixam pegadas no sentido contrário, de modo que quem foge dele acaba indo ao seu encontro. O "
            "historiador Sérgio Buarque de Holanda defendeu, em 1957, que esse detalhe do mito podia vir de uma "
            "tática real dos povos da floresta: usar calçados para despistar inimigos. O nome, segundo a etimologia "
            "mais citada, quer dizer algo como \"pele áspera\", ou \"coberto de feridas\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Curupira",
                "The Curupira according to early Jesuits in São Paulo was a feared being known to leave gruesomely scarred  bodies, to be appeased by offerings. "
                "But it underwent a mutation via European influence, and was recast into more of a mischievous trickster type spirit, often bungling and letting humans outsmart it, though it could still cause misfortune and death. [...] "
                "The name Curupira means \"covered in wounds or blisters\" [...] thus \"rough or pimply skin\". [...] "
                "It punishes humans who wantonly harvest lumber by making him lose his way, wander timelessly in the forest, so he becomes unable to reach his home. [...] "
                "Notably, the Curupira has his feet turned backwards, to mislead trackers with footprints proceeding in the opposite direction, so that one trying to flee the Curupira actually pursues it. [...] "
                "The oldest mention of his name is by the Jesuit José de Anchieta, in São Vicente, on 30 May 1560: "
                "\"It's a well-known thing and it's rumored by everyone that there are certain demons, which the Brazilians call corupira, that often attack Indians in the bush, wound them with the whip, tormenting and killing them. [...] "
                "Therefore, the Indians [in order to appease the demons] traverse the path through the sertão hinterlands, full of rough woodland and steep hills, to reach the highest mountain, leaving  bird feathers, fans, arrows and such things [as a kind of oblation], begging [the demons] to do them no harm\". "
                "Other early mentions were made by Jesuit Fernão Cardim (1584) [...] "
                "Sérgio Buarque de Holanda (Caminhos e Fronteiras 1957) argued the \"fabulous Mutayu\" and the Curupira myth to be a product derived from the rainforest people's tactical practice of wearing shoes to throw enemies off their path. [...] "
                "Cardim records that Curupira is the devil the indigenous people revere and fear above all else, but do not craft any idols of them.",
                nome="Curupira"),
        ],
    },
    # 5 boitatá, a "coisa de fogo"
    {
        "temas_secundarios": ["mitologia", "quimica_cotidiano"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "Boitatá quer dizer \"coisa de fogo\" em tupi. Anchieta o registrou em 1560 como um facho brilhante que atacava indígenas. O mito é ligado ao fogo-fátuo, e em Sergipe e Alagoas virou \"Jean de la foice\".",
        "explicacao": (
            "O nome junta as palavras tupis mba'e, \"coisa\", e tatá, \"fogo\". Em 1560, Anchieta descreveu os "
            "baetatá como fantasmas que viviam sobretudo nas praias e perto de rios: não se via nada além de um "
            "facho cintilante correndo, que atacava os indígenas e os matava, como os curupiras. O próprio jesuíta "
            "admitia que não se sabia ao certo o que era aquilo. Para o biólogo Hitoshi Nomura, a imagem da serpente "
            "veio desse fogo que se deslocava deixando um rastro luminoso. No folclore, o boitatá virou uma cobra "
            "de fogo gigante, guardiã dos campos, que queima quem põe fogo no mato. A origem do mito é associada ao "
            "fogo-fátuo: a matéria orgânica em decomposição solta gases que se inflamam ao contato com o ar, e a "
            "corrente de ar de alguém passando pode mover as chamas, que parecem perseguir a pessoa. O nome muda "
            "pelo país: baitatá ou batatá no Sul, biatatá na Bahia, batatão no Nordeste e, em Sergipe e Alagoas, "
            "Jean de la foice ou Jean Delafosse. Na Europa, fogos-fátuos em forma de serpente também aparecem no "
            "folclore."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Boitatá",
                "O termo mais difundido é boitatá, que é a junção das palavras tupis mba'e e tatá, significando coisa e fogo, respectivamente. [...] "
                "No Sul, é chamado de baitatá ou batatá e até mesmo de boitatá. Na Bahia, aparece como biatatá. Em Minas Gerais chamam-no de bata. No Nordeste, é comum o termo batatão. "
                "Nos estados de Sergipe e Alagoas, recebem os nomes de Jean de la foice ou Jean Delafosse. [...] "
                "Em 1560 registrou o Padre José de Anchieta: "
                "\"Há também outros (fantasmas), máxime nas praias, que vivem a maior parte do tempo junto do mar e dos rios, e são chamados baetatá, que quer dizer coisa de fogo, o que é o mesmo como se se dissesse o que é todo de fogo. "
                "Não se vê outra coisa senão um facho cintilante correndo para ali; acomete rapidamente os índios e mata-os, como os curupiras; o que seja isto, ainda não se sabe com certeza.\" [...] "
                "O biólogo Hitoshi Nomura afirma: \"Como aquele fogo vivo se deslocava, deixando um rasto luminoso, um facho cintilante correndo para ali, anotava o jesuíta, veio a imagem da marcha ondulada da serpente\". [...] "
                "No folclore brasileiro, o Boitatá (Mboitatá) é uma gigantesca cobra-de-fogo [...] "
                "É o guardião do campo [...] queimando aqueles que põem fogo nos campos, matas e florestas. "
                "A origem deste mito está ligada ao fenômeno da natureza denominado fogo-fátuo. "
                "A decomposição de matéria orgânica, seja de vegetação ou animais mortos, libera gases que inflamam-se espontaneamente em contato com ar. "
                "Correntes de ar causadas pela passagem de uma pessoa nas proximidades podem deslocar as chamas fazendo com que pareçam uma cobra de fogo que a persegue.",
                nome="Boitatá", idioma="pt"),
            wiki("Boitatá",
                "Boitatá (from Tupi language), in Brazilian native folklore, refers to either a will-o'-the-wisp, a mythical fire snake which guards against humans setting fire to the fields or forests, or a bull-like creature. "
                "Snake-like will-o'-the-wisps also appear as \"firedrake\" in European folklore.",
                nome="Boitatá"),
        ],
    },
    # 6 a Iara é invenção do século XIX
    {
        "temas_secundarios": ["mitologia", "literatura", "amazonia"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "A Iara, sereia de canto irresistível, não aparece nos textos coloniais. Para Câmara Cascudo, ela é do século XIX, uma sereia europeia aclimatada. As lendas indígenas antigas falavam de um monstro que comia gente.",
        "explicacao": (
            "Os relatos indígenas mais antigos sobre os rios não traziam uma moça de cabelos longos e voz doce, e "
            "sim o ipupiara, um homem marinho bruto que devorava pessoas. Também havia a mãe-d'água, que era uma "
            "cobra-d'água sem nenhum poder de sedução. A Iara sedutora surgiu, segundo o folclorista Luís da Câmara "
            "Cascudo, quando a sereia trazida pelos portugueses se misturou a essas figuras: seria a \"mãe-d'água "
            "dos brancos\", desconhecida dos indígenas. Cascudo atribui a Gonçalves Dias o primeiro uso de \"Iara\" "
            "como sinônimo de sereia. A aparência também mudou. Em 1881, o naturalista João Barbosa Rodrigues "
            "insistia que a Iara original tinha cabelos pretos, olhos escuros e pele morena. Os poetas românticos do "
            "século XIX lhe deram cabelos loiros, ou verdes como a vegetação, e Cascudo não conhecia registro da "
            "Iara loira de olhos azuis antes de meados daquele século. As histórias de sedução atribuídas ao boto "
            "também são tardias e nasceram em paralelo, sob a mesma influência europeia. O nome vem do nheengatu, a "
            "língua geral amazônica, e quer dizer algo como \"senhora das águas\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Iara",
                "Trata-se de uma lenda amazônica surgida no século XIX, não havendo referência a ela nos textos coloniais. "
                "Surgiu quando confundiram a sereia europeia com a mãe-d'água das águas brasileiras, que é a cobra-d'água e não tem poder algum de sedução. "
                "Segundo o folclorista brasileiro Luís da Câmara Cascudo, Iara é a Mãe-d'Água dos brancos, vinda dos portugueses, que trouxeram as sereias da Europa, com modificações negras, desconhecida pelo indígena brasileiro. [...] "
                "As estórias de sedução atribuídas aos botos, que podem se transformar em homem ou em mulher, são também tardias, surgidas em paralelo às da Iara sedutora, sofrendo igualmente a influência europeia [...] "
                "Cascudo informa que o primeiro a usar “Iara” como sinônimo de “sereia” teria sido Gonçalves Dias [...] "
                "Não há lenda indígena que tenha registrado a Iara de cabelos longos e voz maviosa; lendas indígenas mais velhas citam sempre o terrível homem marinho, o bruto ipupiara, comedor de gente, de quem a Iara também empresta alguns atributos.",
                nome="Iara", idioma="pt"),
            wiki("Iara_(mythology)",
                "The word derives from Nheengatu iiyara, from ií \"water\" + yara \"lord; lady\". [...] "
                "João Barbosa Rodrigues (1881) insisted the freshwater Iara, in the original telling, were ascribed black hair, dark eyes, and dark skin (tez morena). [...] "
                "Later, the poetry by Romantic writers in the 19th century would give her blonde hair, or green hair of the color of vegetation. "
                "These were European-influenced alterations of indigenous folklore. [...] "
                "The blond, blue-eyed image was not attested until after the mid-nineteenth century, to the best knowledge of Camara Cascudo.",
                nome="Iara (mythology)"),
        ],
    },
    # 7 Pirenópolis: imperador por sorteio e Carlos Magno a cavalo
    {
        "temas_secundarios": ["europa_medieval", "religioes", "teatro_danca"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Em Pirenópolis (GO), o \"imperador\" da Festa do Divino é escolhido por sorteio, seja rico ou pobre. Depois da festa, dois exércitos de doze cavaleiros encenam a guerra de cristãos contra mouros dos tempos de Carlos Magno.",
        "explicacao": (
            "A devoção ao Divino Espírito Santo vem de Portugal: segundo a tradição, foi instituída por volta de 1320 "
            "pela rainha Isabel de Aragão, que teria prometido peregrinar com uma cópia da coroa se o marido, o rei "
            "Dinis, fizesse as pazes com o filho. Em Pirenópolis, a festa dura doze dias e culmina no Domingo do "
            "Divino, cinquenta dias depois da Páscoa. Sua figura central é o imperador, que com sua corte representa "
            "o rei e a corte de Lisboa. Qualquer morador pode se inscrever no sorteio: o rico paga a festa com seus "
            "bens, o pobre com a ajuda do povo, e há quem já tenha sido imperador duas ou três vezes. A coroa e o "
            "cetro, de prata, foram encomendados em 1826 pelo padre Manuel Amâncio da Luz, quando ele mesmo era o "
            "imperador. No mesmo ano, o padre introduziu as cavalhadas, num espetáculo chamado \"O Batalhão de Carlos "
            "Magno\". Durante três dias, os dois exércitos de cavaleiros se enfrentam diante de milhares de "
            "pessoas. No Brasil, esse tipo de encenação foi trazido pelos jesuítas, com autorização da Coroa, para "
            "catequizar. A festa é patrimônio imaterial registrado pelo Iphan desde 2010."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Festa_do_Divino_Espírito_Santo_de_Pirenópolis",
                "A Festa do Divino de Pirenópolis foi registrada como Patrimônio cultural imaterial brasileiro, reconhecido pelo IPHAN, em 15 de abril de 2010. [...] "
                "Com duração de doze dias, tem seu ápice no Domingo do Divino, cinquenta dias após a Ressurreição. [...] "
                "A presença do Imperador, figura central da Festa, bem como sua corte, faz representar o Rei e a Corte lisbonense, com toda sua pompa. [...] "
                "Ambos em pura prata. Foram mandados fazer em 1826 pelo Padre Manuel Amâncio da Luz, quando Imperador. [...] "
                "A escolha do Imperador é feita por sorteio. Todos os Pirenopolinos que se julgam em condições de realizar a festa podem se inscrever. "
                "Não se faz distinção entre ricos e pobres. Se rico, promove a festa com suas posses, se pobre, com a ajuda do povo. "
                "Não há limite de vezes para uma pessoa ser Imperador, bastando ser sorteada, inclusive várias pessoas já o foram por duas ou três vezes.",
                nome="Festa do Divino Espírito Santo de Pirenópolis", idioma="pt"),
            wiki("Cavalhadas_de_Pirenópolis",
                "A encenação é apresentada após a Festa do Divino Espírito Santo, quando dois exércitos contendo doze cavaleiros cada, durante três dias, se apresentam para um público de milhares de pessoas. [...] "
                "A tradição foi introduzida em Pirenópolis em 1826 pelo padre Manuel Amâncio da Luz, como um espetáculo chamado de \"O Batalhão de Carlos Magno\". [...] "
                "a \"rixa\" entre muçulmanos e cristão [...] "
                "No Brasil esta representação dramática foi introduzida, sob autorização da Coroa, pelos jesuítas, com o objetivo de catequizar os gentios e escravos africanos",
                nome="Cavalhadas de Pirenópolis", idioma="pt"),
            wiki("Festa_do_Divino",
                "Há referências históricas que indicam que foi inicialmente instituída, em 1321, pelo convento franciscano de Alenquer sob proteção da rainha Santa Isabel de Portugal e Aragão. "
                "A celebração do Divino Espírito Santo no planeta teve origem na promessa da rainha, Isabel de Aragão, por volta de 1320. "
                "A rainha teria prometido ao Divino Espírito Santo peregrinar o mundo com uma cópia da coroa e uma pomba no alto da coroa, que é o símbolo do Divino Espírito Santo, arrecadando donativos em benefício da população pobre, caso o esposo, o rei Dinis, fizesse as pazes com seu filho legítimo, Afonso, herdeiro do trono.",
                nome="Festa do Divino", idioma="pt"),
        ],
    },
    # 8 frevo: capoeiristas, cabos de guarda-chuva e "ferver"
    {
        "temas_secundarios": ["teatro_danca", "heranca_africana", "musica_brasileira"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "A sombrinha do frevo tem raiz em briga de rua: capoeiristas iam à frente dos blocos do Recife para intimidar rivais, armados de porretes ou cabos de guarda-chuva. E \"frevo\" vem de \"frever\", corruptela de \"ferver\".",
        "explicacao": (
            "No fim do século XIX, bandas de regimentos do Exército no Recife desfilavam no Carnaval e ganharam "
            "torcidas. As mais famosas, a Espanha e a do 14º Regimento de Infantaria, passaram a competir e a tocar "
            "cada vez mais rápido e mais alto. Os confrontos entre os grupos eram comuns, e capoeiristas saíam à "
            "frente dos blocos para intimidar os rivais e proteger o seu. Eles usavam porretes ou cabos de "
            "guarda-chuvas velhos como arma. Quando a polícia passou a persegui-los, os capoeiras trocaram as facas "
            "pelos guarda-chuvas e disfarçaram os golpes como passos de dança. Assim nasceu o passo, a dança do "
            "frevo, que hoje tem mais de 120 passos catalogados. O guarda-chuva preto, de cabo de madeira, foi "
            "encolhendo até virar a sombrinha pequena e colorida dos passistas. O pesquisador Evandro Rabello achou "
            "um dos primeiros registros impressos da palavra frevo no Jornal Pequeno de 9 de fevereiro de 1907. Em "
            "2012, a UNESCO declarou o frevo Patrimônio Imaterial da Humanidade."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Frevo",
                "Muito executado durante o carnaval, eram comuns conflitos entre blocos de frevo, em que capoeiristas saíam à frente dos seus blocos para intimidar blocos rivais e proteger seu grupo. [...] "
                "Da junção da capoeira com o ritmo do frevo nasceu o passo. "
                "A dança do frevo foi utilizada inicialmente como arma de defesa dos passistas que remete diretamente a luta, resistência e camuflagem, herdada da capoeira e dos capoeiristas, que faziam uso de porretes ou cabos de velhos guarda-chuvas como arma contra grupos rivais. [...] "
                "O frevo possui mais de 120 passos catalogados. [...] "
                "A palavra frevo vem de ferver, por sua corruptela, frever [...] "
                "Segundo a pesquisa de Rabello, em 9 de fevereiro de 1907, o vespertino Jornal Pequeno, que mantinha uma seção carnavalesca assinada pelo jornalista Oswaldo Oliveira, registrou  a execução de uma música denominada O frevo [...] "
                "Foi declarado Patrimônio Imaterial da Humanidade pela UNESCO no ano de 2012",
                nome="Frevo", idioma="pt"),
            wiki("Frevo",
                "The word frevo is said to come from frever, a variant of the Portuguese word ferver (to boil). [...] "
                "By the end of the 19th century, bands from the Brazilian Army regiments based in the city of Recife started a tradition of parading during the Carnival. [...] "
                "The two most famous bands were the Espanha (meaning Spain), whose conductor was of Spanish origin, and the 14, from the 14th Infantry Regiment. "
                "The bands started to compete with each other and also started playing faster and faster, louder and louder. [...] "
                "In order to end the violence, the police started to pursue the capoeiras and arrested many during their exhibitions. "
                "The latter reacted in a clever way by carrying umbrellas instead of knives and also disguising the capoeira movements as dance movements. [...] "
                "The umbrella also developed from regular black umbrellas with wooden handles to a small and also colorful umbrella.",
                nome="Frevo"),
        ],
    },
    # 9 maracatu e os reis do Congo
    {
        "temas_secundarios": ["heranca_africana", "brasil_colonial"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "O maracatu de Pernambuco descende da coroação dos \"reis do Congo\": escravizados que recebiam da administração portuguesa um papel de liderança sobre os demais. Já em 1674 se coroavam esses reis no Recife.",
        "explicacao": (
            "No Recife, há registro de coroações de reis do Congo na Igreja do Rosário dos Pretos já em 1674. Elas "
            "eram organizadas pelas irmandades negras de Nossa Senhora do Rosário, que funcionavam ao mesmo tempo "
            "como associações religiosas e espaços de convívio para africanos e seus descendentes. Os reis do Congo "
            "eram escravizados a quem a administração portuguesa concedia liderança dentro da comunidade "
            "escravizada. Com a abolição, em 1888, a instituição deixou de existir, mas os grupos de maracatu, "
            "chamados nações, continuaram a escolher líderes simbólicos e a evocar as cerimônias de coroação. Num "
            "cortejo tradicional desfilam um rei e uma rainha, com uma corte vestida à moda da corte portuguesa "
            "barroca, e um batuque de 80 a 100 percussionistas. Uma dama do paço carrega a calunga, boneca sagrada "
            "que representa divindades e fica guardada o ano inteiro na sede do grupo. Embora o desfile seja "
            "profano, as nações tradicionais se organizam em torno de terreiros de candomblé ou de jurema. Hoje há "
            "grupos inspirados no maracatu em cidades como Berlim, Toronto, Nova York e Lisboa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Maracatu",
                "Maracatu nação’s origins lie in the investiture ceremonies of the Reis do Congo (Kings of Congo), who were enslaved people who were granted leadership roles within the enslaved community by the Portuguese administration. "
                "When slavery was abolished in Brazil in 1888, the institution of the Kings of Congo ceased to exist. "
                "Nonetheless, nações continued to choose symbolic leaders and evoke coronation ceremonies for those leaders. "
                "Although a maracatu performance is secular, traditional nações are grouped around Candomblé or Jurema (Afro-Brazilian religions) terreiros (bases), and the principles of Candomblé infuse their activities. "
                "Traditional nações perform by parading with a drumming group of 80–100, a singer and chorus, and a coterie of dancers and stock characters including a king and a queen. "
                "Dancers and stock characters dress and behave to imitate the Portuguese royal court of the Baroque period. "
                "The performance also enacts pre-colonial African traditions, like parading the calunga, a doll representing tribal deities that is kept throughout the year in a special place in the nação's headquarters. [...] "
                "carrying this spiritual figurehead of the group is a great responsibility for the female Dama de Paço (Lady-in-Waiting) of the cortège. [...] "
                "The genre has inspired the establishment of performing groups in a number of cities outside Brazil, including Lisbon, Toronto, Quebec City, New York City, Austin, Washington, D.C., Cologne, Berlin",
                nome="Maracatu"),
            wiki("Congada",
                "Em 1674, já se realizavam coroações de reis do Congo na Igreja do Rosário dos Pretos do Recife, vinculadas às irmandades negras. "
                "Essas irmandades desempenharam papel central na organização religiosa e social de africanos e seus descendentes, funcionando simultaneamente como instituições devocionais e espaços de sociabilidade.",
                nome="Congada", idioma="pt"),
        ],
    },
    # 10 o cordel que não ficava no cordão
    {
        "temas_secundarios": ["literatura", "palavras_portugues"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "Apesar do nome, não há registro de que o cordel nordestino fosse vendido, como regra, pendurado em cordões; isso era costume em Portugal. E o nome \"cordel\" só se impôs aqui a partir dos anos 1950.",
        "explicacao": (
            "Em Portugal, os folhetos de poesia popular ficavam pendurados em cordões, os cordéis, para a venda, e "
            "daí veio o nome. No Nordeste, porém, o hábito do barbante não se firmou: o folheto podia estar exposto "
            "assim ou não. Quem examinou o caso a fundo foi o historiador Ulpiano Bezerra de Meneses, da USP, relator "
            "do pedido que levou o Iphan a registrar a literatura de cordel como patrimônio imaterial, em 2018. No "
            "parecer, ele observa que a exposição em cordinhas não está atestada como norma, e que o nome só virou a "
            "denominação geral a partir dos anos 1950, por influência do pesquisador Raymond Cantel. Antes, poetas e "
            "leitores usavam muitos nomes: folheto, \"foieto\", livro, folhinha, romance, poesia de matuto. O cordel "
            "brasileiro ganhou impulso depois que a impressão local foi liberada, em 1821, e os folhetos mais "
            "antigos já coletados são de 1890. Leandro Gomes de Barros, que viveu de 1865 a 1918, é o cordelista "
            "mais antigo de que se tem notícia. O pedido de registro, encaminhado ao Iphan em 2010, foi assinado "
            "por 85 poetas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://scielo.br/pdf/rieb/n72/2316-901X-rieb-72-225.pdf",
             "titulo": "A literatura de cordel como patrimônio cultural (Ulpiano T. Bezerra de Meneses, Revista do IEB, 2019)",
             "idioma": "pt",
             "trecho": "Subscrito por 85 poetas, o pedido de registro da literatura de cordel como patrimônio imaterial foi encaminhado ao Iphan em 2010 pela Academia Brasileira de Cordel (ABLC). [...] "
                       "Todavia, que fossem, como padrão, suspensos em cordinhas (daí a denominação) não é atestado como norma corrente, nem como denominação exclusiva, senão a partir de 1950s, por influência de Raymond Cantel, um especialista na littérature de colportage . "
                       "Aliás, as denominações variam segundo várias categorias, conforme o suporte (folheto, “foieto”, livro, folhinha, romance), tradição (folheto antigo), lugar (arrecifes, poesia da rua), editores (livro de Athayde), conteúdo (histórias de João Grilo), origem social (poesia de matuto) [...] "
                       "o cordel brasileiro começa a ganhar impulso próprio a partir da liberação da impressão local de publicações no reino, a partir de 1821. "
                       "Esse perfil ganha intensidade no final do século 19. Os primeiros folhetos coletados datam de 1890. "
                       "Leandro Gomes de Barros (1865-1918) é considerado o cordelista mais antigo de que se tem notícia."},
            wiki("Literatura_de_cordel",
                "O nome tem origem na forma como tradicionalmente os folhetos eram expostos para venda, pendurados em cordas, cordéis ou barbantes em Portugal. "
                "No Nordeste do Brasil o nome foi herdado, mas a tradição do barbante não se perpetuou: o folheto brasileiro pode ou não estar exposto em barbantes. [...] "
                "Em setembro de 2018, o Instituto do Patrimônio Histórico e Artístico Nacional reconheceu a literatura de cordel como patrimônio cultural imaterial do Brasil.",
                nome="Literatura de cordel", idioma="pt"),
        ],
    },
    # 11 o entrudo e os limões de cera
    {
        "temas_secundarios": ["brasil_imperio", "costumes_rituais"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Antes do Carnaval, o Rio brincava o entrudo: guerras de água com tinas, bacias e \"limões\" de cera recheados. Machado de Assis escreveu que o Carnaval nasceu \"um pouco por decreto\", para dar cabo dele.",
        "explicacao": (
            "O entrudo era um folguedo de origem galego-portuguesa, nos três dias antes da Quaresma. Os foliões "
            "atiravam água, ovos e limões de cheiro uns nos outros e se sujavam de farinha. No Rio do século XIX, os "
            "limões eram bolas de cera cheias de água, e as batalhas iam de casa em casa, entre a rua e as janelas. "
            "Em meados do século, parte da elite letrada passou a combater a brincadeira. Campanhas de saúde "
            "alertavam que os banhos podiam provocar tuberculoses fatais. Editais da polícia fixavam multas e até "
            "gorjetas para quem levasse à polícia, \"pelo cós das calças\", um menino negro vendedor de limões de "
            "cera. Em 1893, Machado de Assis "
            "lembrou que o Carnaval tinha nascido para acabar com o entrudo, com a alta sociedade organizando suas "
            "sociedades carnavalescas, e contou que o limão de cera também "
            "tinha uso secreto: o namorado o esmagava no peito da moça. O entrudo, dado como morto desde os anos "
            "50 do século XIX, teimava em voltar: uma charge de 1885 ainda mostra as batalhas de água em plena força."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://seer.ufu.br/index.php/cdhis/article/download/13726/9490/64966",
             "titulo": "As tentativas de regrar o carnaval no Rio de Janeiro (Fabiana Lopes da Cunha, Cadernos de Pesquisa do CDHIS, UFU, 2011)",
             "idioma": "pt",
             "trecho": "Os meus patrícios iam ter um bom carnaval,- velha festa, que está a fazer quarenta anos, se já não os fez. "
                       "Nasceu um pouco por decreto, para dar cabo do entrudo, costume velho, datado da colônia e vindo da metrópole. [...] "
                       "organizaram-se sociedades, cujos nomes e gestos [...] "
                       "As batalhas de água e limões, as guerras às cartolas e os chamados máscaras avulsos, fantasiados de velhos, pai João ou de índio começam a incomodar parte da elite letrada da capital federal em meados do século XIX. [...] "
                       "O limão de cera, que de longe podia es - calavrar um olho, tinha um ofício mais próximo e inteiramente secreto. "
                       "Servia a molhar o peito das moças; era esmigalhado nele pela mão do próprio namorado [...] "
                       "apesar da grande campanha contra o entrudo, e da comemoração de sua morte desde a década de 50 do século XIX, ele reaparecia sempre no carnaval seguinte. "
                       "Não bastaram para extingui-lo comentários e artigos reche - ados de irritação, campanhas de saúde, alertando para o perigo do entrudo e de sua molhaçada, que tais “banhos” poderiam provocar tuberculoses fatais, ou avisos e proibições feitas pela polícia. "
                       "Tais editais ou circulares estabelecem penalidades, especificando-as para o caso de escravos e comerciantes, fixam multas e até gorjetas para cada ‘pretinho’ vendedor de limões de cera que fosse levado à polícia ‘pelo cós das calças’ por qualquer cidadão. [...] "
                       "ele ainda se dava com grande intensidade em 1885 [...] "
                       "ASSIS, Machado de. “A Semana”. Gazeta de Notícias, 12 de fevereiro de 1893. [...] "
                       "Eram tinas d’água; eram limões de cera. "
                       "Davam-se batalhas porfiadas de casa a casa, entre a rua e as janelas, não contando as bacias d’água despejadas à traição."},
            wiki("Entrudo",
                "era um antigo folguedo Galaico-Português realizado nos três dias que antecedem a entrada da Quaresma, na qual os foliões arremessavam baldes de água, limões de cheiro, ovos, tangerinas, pastelões, luvas cheias de areia, golpeavam-se com vassouras e colheres de pau e se sujavam com farinha",
                nome="Entrudo", idioma="pt"),
        ],
    },
    # 12 a Cuca era um dragão português (e uma abóbora com vela)
    {
        "temas_secundarios": ["mitologia", "europa_medieval", "literatura"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "A Cuca das cantigas de ninar veio de Portugal. Lá, \"coca\" é um dragão que ainda luta com São Jorge numa festa em Monção, e também o nome de abóboras furadas com uma vela dentro, como as do Halloween.",
        "explicacao": (
            "Na Península Ibérica, o coco ou a coca é um papão que leva as crianças desobedientes, e pais cantam "
            "cantigas de ninar avisando que ele vem pegá-las. No Brasil, a figura virou a Cuca. Câmara Cascudo, em "
            "\"Geografia dos Mitos Brasileiros\", a liga à Coca que aparecia nas procissões do Minho, em Portugal. "
            "Em Monção sobrevive uma dessas cocas: na festa de Corpus Christi, a dragoa enfrenta São Jorge numa "
            "espécie de torneio. Se ela vencer, assustando o cavalo, o ano será de colheita ruim e fome; se São "
            "Jorge lhe arrancar uma orelha e a língua, as colheitas serão fartas. Curiosamente, o povo torce pela "
            "Coca. O Minho guarda outro parentesco: lá, cuca é também o nome popular de uma abóbora furada com olhos "
            "e boca e iluminada por uma vela, à maneira do Halloween americano. O nome tem a ver com cabeça: em "
            "português e em galego, coco e cuca podem significar cabeça. No livro \"O Saci\", de 1921, Monteiro "
            "Lobato descreve a Cuca apenas com \"cara de jacaré\" e dedos em garra; foram as adaptações e os "
            "ilustradores que a transformaram num jacaré com forma humana."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Cuca",
                "Em seu livro \"Geografia dos Mitos Brasileiros\", Luís da Câmara Cascudo (1898-1986) diz que a Cuca é um mito de origem portuguesa relacionado à Coca, figura que aparecia nas procissões da província do Minho, em Portugal. "
                "Também no Minho, \"cuca\" é o nome popular de uma espécie de abóbora que costumava-se perfurar com contornos de olhos e boca, e dentro da qual era colocada uma vela acesa (de forma semelhante ao que se faz no Halloween americano).",
                nome="Cuca", idioma="pt"),
            wiki("Cuca_(folklore)",
                "The \"monster\" will come to the house of disobedient children at night and take them away. [...] "
                "either coco or cuca means \"head\" in both Portuguese and Galician. [...] "
                "In the only book she appears, O saci (1921), Cuca's description is vague, Monteiro Lobato only states that she had an \"alligator face\" and \"clawed fingers\". [...] "
                "they sing lullabies or tell rhymes warning their children that if they don't obey their parents, el Coco will come and get them and then eat them. [...] "
                "In Portugal one still survives in Monção; she fights in some sort of medieval tournament with Saint George during the Corpus Christi celebrations. [...] "
                "If she defeats Saint George by scaring the horse, there will be a bad year for the crops and famine; if the horse and Saint George win by cutting off one of her ears with earring and her tongue, the crops will be fertile. "
                "Oddly enough, the people cheer for Saint Coca. [...] "
                "Artists illustrating these books depicted the Cuca as an anthropomorphic alligator.",
                nome="Cuca (folklore)"),
        ],
    },
    # 13 festa junina: solstício europeu no inverno brasileiro
    {
        "temas_secundarios": ["calendarios", "povos_indigenas", "religioes"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "A festa junina vem das festas do solstício de verão europeu, mas no Brasil cai em pleno inverno. No século XVI, o jesuíta Fernão Cardim já via indígenas da Bahia pulando as fogueiras de São João.",
        "explicacao": (
            "As festas juninas celebram o nascimento de São João Batista, em 24 de junho, e as vésperas dos dias de "
            "Santo Antônio, de São João e de São Pedro e São Paulo. Trazidas pelos portugueses no período colonial, "
            "elas adaptam celebrações do solstício de verão europeu, como a grande fogueira. No hemisfério sul, "
            "porém, junho é inverno. Por isso, no interior paulista, onde as noites de junho costumam ser frias, "
            "não faltam bebidas quentes, como o quentão. Já no Nordeste, de clima árido ou semiárido, a festa "
            "coincide com o fim da estação das chuvas na maioria dos estados e virou uma ocasião para agradecer a "
            "São João pela chuva. A primeira menção à festa no Brasil é do jesuíta Fernão Cardim, no seu Tratado da "
            "Terra e da Gente do Brasil, do século XVI. Segundo ele, a de São João estava entre as festas mais "
            "celebradas nas aldeias indígenas da Bahia: as aldeias se enchiam de fogueiras, e os indígenas saltavam "
            "sobre elas com entusiasmo, sem se importar com a roupa, às vezes até se queimando de leve."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Festa_junina_no_Brasil",
                "Festas juninas no Brasil, também conhecidas como festas de São João por celebrarem a natividade de São João Batista (24 de junho), são as comemorações anuais brasileiras adaptadas do solstício de verão europeu que ocorre no meio do inverno do hemisfério sul. "
                "Estas festividades, introduzidas pelos portugueses durante o período colonial (1500-1822), são celebradas durante o mês de junho em todo o país. "
                "A festa é celebrada principalmente nas vésperas das solenidades católicas de Santo Antônio, São João Batista, São Pedro e São Paulo. [...] "
                "Como as noites de junho normalmente são frias no território paulista, bebidas alcoólicas aquecidas, tais como o quentão e o vinho quente também estão sempre presentes nessas festividades. "
                "Na região Nordeste do Brasil, em decorrência da predominância do clima árido ou semiárido, essas festas não apenas coincidem com o fim das estações chuvosas da maioria dos estados da região, como também oferecem às pessoas a oportunidade de agradecer a São João pela chuva. [...] "
                "A primeira menção sobre a festa junina e o São João no Brasil, ocorre em palavras do jesuíta Fernão Cardim, em seu Tratado da Terra e da Gente do Brasil (século XVI), relatando que a festa de São João era uma das mais celebradas pelos povos indígenas das aldeias da Bahia, especialmente na região do recôncavo baiano. "
                "De acordo com Cardim, as aldeias eram tomadas por fogueiras, e os indígenas pulavam sobre elas com entusiasmo, muitas vezes sem se preocuparem com vestimentas, chegando inclusive a se queimar levemente. [...] "
                "Vários aspectos do festival têm origem nas celebrações do solstício de verão europeu, como a criação de uma grande fogueira.",
                nome="Festa junina no Brasil", idioma="pt"),
        ],
    },
]
