LOTE = "2026-11-19-invencoes-01"
AREA = "tecnologia"
TEMA = "invencoes"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Teflon: do cilindro entupido ao Projeto Manhattan e à frigideira
    {
        "temas_secundarios": ["quimica_cotidiano", "segunda_guerra"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "O Teflon surgiu por acaso, num cilindro de gás que parou de soltar gás antes de esvaziar. Um dos primeiros usos foi no Projeto Manhattan; só anos depois, por insistência de uma esposa, ele chegou às frigideiras.",
        "explicacao": (
            "Em abril de 1938, o químico Roy Plunkett, da DuPont, tentava criar um novo gás refrigerante do tipo "
            "CFC. Ao abrir um cilindro de tetrafluoretileno, nada saiu, embora o peso indicasse que ele ainda não "
            "estava vazio. Os químicos serraram o cilindro e acharam o interior coberto por um material branco e "
            "ceroso, estranhamente escorregadio. O gás tinha virado um polímero, o politetrafluoretileno, e o ferro "
            "da parede interna, sob alta pressão, tinha feito o papel de catalisador. O novo plástico resistia à "
            "corrosão e ao calor e tem um dos menores coeficientes de atrito entre os sólidos. Foi essa inércia "
            "química que o levou ao Projeto Manhattan: ele revestiu válvulas e vedações dos canos que carregavam o "
            "hexafluoreto de urânio, um composto muito reativo, na enorme usina de enriquecimento K-25, no "
            "Tennessee. A cozinha veio depois. Em 1954, a francesa Colette Grégoire insistiu para que o marido, o "
            "engenheiro Marc Grégoire, testasse nas panelas dela o material que ele usava em equipamento de pesca. "
            "Dali saíram as primeiras frigideiras antiaderentes, da marca Tefal, nome que junta \"Tef\", de Teflon, "
            "e \"al\", de alumínio."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Polytetrafluoroethylene",
                "PTFE has one of the lowest coefficients of friction of any solid. [...] "
                "Polytetrafluoroethylene (PTFE) was accidentally discovered in 1938 by Roy J. Plunkett while he was working in Chemours Chambers Works plant in New Jersey for DuPont. "
                "On 6 April 1938, while attempting to make a new chlorofluorocarbon refrigerant, Plunkett and his assistant Jack Reebok found that a cylinder of tetrafluoroethylene (TFE) gas contained a white powder: polytetrafluoroethylene. "
                "The gas in its pressure bottle stopped flowing before the bottle's weight had dropped to the point signaling \"empty\". [...] "
                "The chemists in the lab sawed the bottle apart and found the bottle's interior coated with a waxy white material that was oddly slippery. "
                "Analysis showed that it was polymerized perfluoroethylene, with the iron from the inside of the container having acted as a catalyst at high pressure. [...] "
                "An early use was in the Manhattan Project as a material to coat valves and seals in the pipes holding highly reactive uranium hexafluoride at the vast K-25 uranium enrichment plant in Oak Ridge, Tennessee. [...] "
                "In 1954, Colette Grégoire urged her husband, the French engineer Marc Grégoire, to try the material he had been using on fishing tackle on her cooking pans. "
                "He subsequently created the first PTFE-coated non-stick pans under the brand name Tefal (combining \"Tef\" from \"Teflon\" and \"al\" from aluminium).",
                nome="Polytetrafluoroethylene"),
            wiki("Roy_J._Plunkett",
                "The tetrafluoroethylene in the container had polymerized into polytetrafluoroethylene, a waxy solid with that was found to have had properties such as resistance to corrosion, low surface friction, and high heat resistance.",
                nome="Roy J. Plunkett"),
        ],
    },
    # 2 o primeiro paciente de marca-passo sobreviveu ao inventor e ao cirurgião
    {
        "temas_secundarios": ["historia_medicina", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "O primeiro marca-passo implantado num ser humano, na Suécia em 1958, parou após três horas. O paciente, Arne Larsson, usou 26 aparelhos na vida e morreu aos 86 anos, depois do inventor e do cirurgião.",
        "explicacao": (
            "O implante foi feito em 8 de outubro de 1958, no Instituto Karolinska, em Solna, com um aparelho "
            "criado pelo inventor Rune Elmqvist e pelo cirurgião Åke Senning. Os eletrodos foram presos direto no "
            "músculo do coração, por uma abertura no tórax. O primeiro aparelho falhou depois de três horas, e o "
            "segundo durou dois dias. Os modelos suecos daquela época usavam baterias recarregadas de fora do corpo, "
            "por uma bobina de indução. Durar era o grande desafio: as pilhas disponíveis, sobretudo as de mercúrio, "
            "eram pouco confiáveis e tinham vida curta, e o vapor d'água dos fluidos do corpo atravessava a resina "
            "que envolvia o circuito e o danificava. As soluções vieram aos poucos. Uma foi fechar o gerador numa "
            "caixa metálica hermética, que acabou sendo de titânio. Outra foi a pilha de lítio-iodo, criada em 1971 "
            "por Wilson Greatbatch, que aumentou a vida útil dos marca-passos de um ano para até onze. Larsson "
            "acompanhou toda essa evolução no próprio peito: passou por 26 marca-passos e morreu em 2001, aos 86 "
            "anos, tendo sobrevivido tanto ao inventor quanto ao cirurgião que o operaram pela primeira vez."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Artificial_cardiac_pacemaker",
                "The first clinical implantation into a human of a fully implantable pacemaker was on October 8, 1958, at the Karolinska Institute in Solna, Sweden, using a pacemaker designed by inventor Rune Elmqvist and surgeon Åke Senning (in collaboration with Elema-Schönander AB, later Siemens-Elema AB), connected to electrodes attached to the myocardium of the heart by thoracotomy. "
                "The device failed after three hours. A second device was then implanted which lasted for two days. "
                "The world's first implantable pacemaker patient, Arne Larsson, went on to receive 26 different pacemakers during his lifetime. "
                "He died in 2001, at the age of 86, outliving the inventor and the surgeon. [...] "
                "The early Swedish-designed devices used batteries recharged by an induction coil from the outside. [...] "
                "The preceding implantable devices all suffered from the unreliability and short lifetime of the available primary cell technology, mainly the mercury battery. [...] "
                "development in 1971 of the lithium iodide cell by Wilson Greatbatch. [...] "
                "A further impediment to the reliability of the early devices was the diffusion of water vapor from body fluids through the epoxy resin encapsulation, affecting the electronic circuitry. "
                "This phenomenon was overcome by encasing the pacemaker generator in a hermetically sealed metal case [...] "
                "This technology, using titanium as the encasing metal, became the standard by the mid-1970s. [...] "
                "Lithium-iodide or lithium anode cells increased the life of pacemakers from one year to as long as eleven years",
                nome="Artificial cardiac pacemaker"),
        ],
    },
    # 3 Goodyear, Hancock e a briga pela vulcanização
    {
        "temas_secundarios": ["leis_julgamentos", "revolucao_industrial"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Charles Goodyear passou anos na miséria até conseguir vulcanizar a borracha. Na Inglaterra, Thomas Hancock, que tinha visto amostras americanas, patenteou o processo oito semanas antes dele e ganhou na Justiça.",
        "explicacao": (
            "Entre 1831 e 1832, Goodyear se interessou pela borracha natural, cujos produtos ficavam pegajosos e "
            "apodreciam. Insistiu por anos: foi preso por dívidas, a família chegou a caçar rãs e cavar batatas meio "
            "congeladas para comer, e dois filhos dele morreram ainda bebês. Em 1839, descobriu que borracha "
            "misturada com enxofre e aquecida sobre um fogão quente ficava firme: era a vulcanização. Na Inglaterra, "
            "Thomas Hancock registrou em novembro de 1843 uma patente para vulcanizar borracha com enxofre, oito "
            "semanas antes de Goodyear nos Estados Unidos. Hancock não dizia ter descoberto a reação. Contou que, em "
            "1842, um amigo lhe mostrara amostras americanas tratadas com enxofre, e jurou que já fazia "
            "experimentos com enxofre havia anos. Na disputa judicial, químicos testemunharam que estudar o material "
            "de Goodyear não bastaria para descobrir como ele era feito, e a patente de Hancock foi mantida, também "
            "pela falta de proteção internacional e porque Goodyear não guardara segredo. Mesmo assim, Alexander "
            "Parkes, inventor de outro processo de vulcanização, afirmou que Hancock e o amigo tinham admitido a ele "
            "que foram as amostras de Goodyear que lhes permitiram entender o método. Em 1855, Goodyear voltou a "
            "ser preso por dívidas, na Inglaterra e na França, e recebeu a Legião de Honra enquanto estava preso."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Charles_Goodyear",
                "Between the years 1831 and 1832, Goodyear heard about gum elastic (natural rubber) [...] "
                "To their surprise, goods that they had determined to be of good quality were being returned, the gum having rotted, making them useless. [...] "
                "However, when he returned to Philadelphia, a creditor had him arrested and imprisoned. [...] "
                "His family's situation became so desperate that they were reduced to catching frogs and digging half-frozen potatoes to get by. "
                "His two sons died while they were still toddlers, aggravating the impact of poverty. [...] "
                "the rubber goods were constantly growing sticky, decomposing and being returned to the manufacturers. [...] "
                "In 1839, Goodyear was at the Eagle India Rubber Company in Woburn, Massachusetts, where he discovered that combining rubber and sulfur over a hot stove caused the rubber to become rigid, a process which he called vulcanization because of the heat involved. [...] "
                "Both had examined Goodyear's vulcanized rubber in 1842, but several chemists testified that it would not have been possible to determine how it was made by studying it. Hancock prevailed. [...] "
                "In 1855, Goodyear was sent to debtor's prison in both England and France [...] "
                "He was inducted into the Legion of Honour while imprisoned.",
                nome="Charles Goodyear"),
            wiki("Thomas_Hancock_(inventor)",
                "On 21 November 1843, Hancock took out a patent for the vulcanisation of rubber using sulphur, eight weeks before Charles Goodyear did in the US on 30 January 1844. [...] "
                "Hancock did not credit himself with discovering the reaction of sulphur with rubber; he instead said that in 1842 Brockendon had shown him some American rubber samples which had been treated with sulphur. "
                "Hancock’s patent for the vulcanization method, filed 21 November 1843, was later upheld in British courts on the basis of both precedence and a want of international patent protection, together with Goodyear’s failure to maintain secrecy. "
                "Brockendon later said in an affidavit that he never heard or knew of Hancock analysing the Goodyear samples, a claim Hancock verified, declaring that he had experimented with sulphur for many years himself. [...] "
                "Alexander Parkes, inventor of the \"cold cure\" process (vulcanisation of fabrics using sulphur chloride in a carbon disulphide solution), asserted that both Hancock and Brockendon had admitted to him that their experiments on the Goodyear samples had enabled them to understand what Goodyear had done.",
                nome="Thomas Hancock (inventor)"),
        ],
    },
    # 4 sacarina: o doce na mão e a briga com o chefe
    {
        "temas_secundarios": ["quimica_cotidiano", "leis_julgamentos"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "A sacarina foi descoberta quando um químico sentiu, certa noite, gosto doce na própria mão, vindo do composto com que trabalhara no dia. Ele enriqueceu, e o chefe do laboratório o chamou de \"canalha\".",
        "explicacao": (
            "O químico russo Constantin Fahlberg trabalhava no laboratório de Ira Remsen, na Universidade Johns "
            "Hopkins, nos Estados Unidos, estudando derivados do alcatrão de hulha. Uma noite, notou um sabor doce "
            "na mão e o associou à sulfimida benzoica, a substância que manipulara naquele dia. Os dois publicaram "
            "artigos sobre o composto em 1879 e 1880. Em 1884, já trabalhando por conta própria em Nova York, "
            "Fahlberg pediu patentes em vários países e deu à substância o nome de sacarina. Dois anos depois, abriu "
            "uma fábrica perto de Magdeburgo, na Alemanha, e logo ficou rico. Remsen achava que merecia crédito pelo "
            "que nascera no seu laboratório e disse que Fahlberg era um canalha e que tinha náuseas ao ouvir o "
            "próprio nome citado junto com o dele. A briga seguinte foi política. Harvey Wiley, chefe da divisão "
            "de química da FDA, a agência americana de alimentos, disse ao presidente Theodore Roosevelt que quem "
            "comia milho adoçado com sacarina era enganado, pois ingeria um produto do alcatrão sem valor nutritivo e "
            "prejudicial à saúde. Roosevelt, que consumia sacarina, respondeu irritado que quem dissesse que ela "
            "fazia mal era um idiota. O episódio acabou com a carreira de Wiley."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Saccharin",
                "Saccharin was produced first in 1879, by Constantin Fahlberg, a chemist working on coal tar derivatives in Ira Remsen's laboratory at Johns Hopkins University. "
                "Fahlberg noticed a sweet taste on his hand one evening, and connected this with the compound benzoic sulfimide on which he had been working that day. "
                "Fahlberg and Remsen published articles on benzoic sulfimide in 1879 and 1880. "
                "In 1884, then working on his own in New York City, Fahlberg applied for patents in several countries [...] describing methods of producing this substance that he named saccharin. "
                "Two years later, he began production of the substance in a factory in a suburb of Magdeburg in Germany.  "
                "Fahlberg soon grew wealthy, while Remsen believed he deserved credit for substances produced in his laboratory. "
                "On the matter, Remsen commented, \"Fahlberg is a scoundrel. It nauseates me to hear my name mentioned in the same breath with him.\" [...] "
                "Harvey Wiley, then the director of the bureau of chemistry for the FDA [...] "
                "Wiley told President Theodore Roosevelt, \"Everyone who ate that sweet corn was deceived. He thought he was eating sugar, when in point of fact he was eating a coal tar product totally devoid of food value and extremely injurious to health.\" "
                "But Roosevelt himself was a consumer of saccharin, and, in a heated exchange, Roosevelt angrily answered Wiley by stating, \"Anybody who says saccharin is injurious to health is an idiot.\"  "
                "The episode proved the undoing of Wiley's career.",
                nome="Saccharin"),
            wiki("Constantin_Fahlberg",
                "Constantin Fahlberg (Russian: Константин Фальберг; 22 December 1850 in Tambov – 15 August 1910 in Nassau) was a Russian chemist",
                nome="Constantin Fahlberg"),
        ],
    },
    # 5 "rubber": o material ganhou o nome da função de apagar
    {
        "temas_secundarios": ["palavras_viajantes", "quimica_cotidiano"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "Em inglês, a borracha se chama \"rubber\" (\"esfregador\"): a palavra valia para qualquer coisa de esfregar e grudou no material nos anos 1770, quando ele passou a ser vendido para apagar lápis. Antes, usava-se pão.",
        "explicacao": (
            "Antes da borracha de apagar, marcas de grafite ou carvão eram tiradas do papel com tabletes de cera, e "
            "erros de tinta em pergaminho ou papiro eram raspados com pedra áspera, como arenito e pedra-pomes. "
            "Miolo de pão sem casca também servia. Um estudante de Tóquio da era Meiji (1868–1912) lembrou que a "
            "escola distribuía pão para apagar à vontade, e os alunos comiam um pedaço para enganar a fome. Em "
            "1770, segundo os relatos, o fabricante inglês de instrumentos Edward Nairne pôs à venda a primeira "
            "borracha de apagar comercializada em larga escala. Ele contou que pegou por engano um pedaço de "
            "borracha no lugar das migalhas de pão e descobriu que ela apagava. Naquele mesmo ano, o químico Joseph "
            "Priestley escreveu numa nota de rodapé que tinha visto uma substância excelente para limpar do papel a "
            "marca do lápis, vendida pela loja de Nairne. Até então, o material era chamado de \"goma elástica\" ou "
            "pelo nome francês \"caoutchouc\", emprestado do quíchua. \"Rubber\" designava qualquer objeto usado "
            "para esfregar, e entre 1770 e 1778 a palavra se fixou no novo material. A borracha crua, porém, "
            "estragava com o tempo. As borrachas de apagar só se tornaram comuns depois da vulcanização, descoberta "
            "por Charles Goodyear em 1839."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Eraser",
                "Before rubber erasers used today, tablets of wax were used to erase lead or charcoal marks from paper. "
                "Bits of rough stone such as sandstone or pumice were used to remove small errors from parchment or papyrus documents written in ink.  "
                "Crustless bread was used; a Meiji period (1868–1912) Tokyo student said: \"Bread erasers were used in place of rubber erasers, and so they would give them to us with no restriction on amount.  "
                "So we thought nothing of taking these and eating a firm part to at least slightly satisfy our hunger.\" "
                "In 1770, the English optician and scientific instrument maker Edward Nairne reportedly developed the first widely marketed rubber eraser for an inventions competition. "
                "Until that time the material was known as gum elastic or by its French name \"caoutchouc\" borrowed from Quechua. [...] "
                "According to Nairne, he inadvertently picked up a piece of rubber instead of breadcrumbs, discovered rubber's erasing properties, and began selling rubber erasers. "
                "The invention was described by Joseph Priestley on April 15, 1770, in a footnote: \"I have seen a substance excellently adapted to the purpose of wiping from paper the mark of black-lead-pencil. ... It is sold by Mr. Nairne, Mathematical Instrument-Maker, opposite the Royal-Exchange.\" "
                "In 1770 the word \"rubber\" was in general use for any object used for rubbing; the word became attached to the new material sometime between 1770 and 1778. "
                "However, raw rubber was perishable. In 1839 Charles Goodyear discovered the process of vulcanization, a method that would cure rubber, making it durable. "
                "Rubber erasers became common with the advent of vulcanization.",
                nome="Eraser"),
        ],
    },
    # 6 código de barras: Morse na areia e o borrão de tinta
    {
        "temas_secundarios": ["historia_computacao", "economia_curiosa"],
        "tipos_espanto": ["engenhosidade", "origem_inesperada"],
        "gancho": "O código de barras nasceu de pontos e traços do código Morse, esticados com os dedos na areia de uma praia. E as barras retas venceram um rival em forma de alvo por um motivo prosaico: borrão de tinta.",
        "explicacao": (
            "Em 1948, Bernard Silver, estudante de pós-graduação do Instituto Drexel, na Filadélfia, ouviu o "
            "presidente de uma rede de supermercados pedir a um diretor da escola um jeito de ler automaticamente "
            "os produtos no caixa. Contou ao amigo Norman Joseph Woodland, que foi para a Flórida trabalhar na "
            "ideia. Numa praia, Woodland se lembrou do código Morse que aprendera como escoteiro, desenhou pontos e "
            "traços na areia e os puxou para baixo com os dedos: os pontos viraram linhas finas e os traços, linhas "
            "grossas. Para a leitura, adaptou a técnica das trilhas sonoras ópticas do cinema. A patente, pedida em "
            "1949 e concedida em 1952, incluía também um desenho circular, como um alvo, que podia ser lido em "
            "qualquer direção. Um relatório da IBM concluiu que processar os dados exigiria equipamentos ainda "
            "futuros, e o código levou mais de vinte anos para fazer sucesso. Num teste da RCA com a versão "
            "circular, num supermercado de Cincinnati, a impressora às vezes borrava a tinta e o código ficava "
            "ilegível na maioria das direções. Já o código linear era impresso no sentido das barras: a tinta a "
            "mais só as deixava mais compridas, e a leitura continuava possível. Em 1973, a versão linear da IBM, "
            "em que Woodland trabalhou, virou o padrão. Em junho de 1974, um pacote de chicletes Wrigley's foi o "
            "primeiro uso comercial do novo código."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Barcode",
                "The invention was based on Morse code that was extended to thin and thick bars. However, it took over twenty years before this invention became commercially successful. [...] "
                "In 1948, Bernard Silver, a graduate student at Drexel Institute of Technology in Philadelphia, Pennsylvania, US overheard the president of the local food chain, Food Fair, asking one of the deans to research a system to automatically read product information during checkout. "
                "Silver told his friend Norman Joseph Woodland about the request, and they started working on a variety of systems. [...] "
                "His next inspiration came from Morse code, and he formed his first barcode from sand on the beach. "
                "\"I just extended the dots and dashes downwards and made narrow lines and wide lines out of them.\" "
                "To read them, he adapted technology from optical soundtracks in movies [...] "
                "He later decided that the system would work better if it were printed as a circle instead of a line, allowing it to be scanned in any direction. "
                "On 20 October 1949, Woodland and Silver filed a patent application for \"Classifying Apparatus and Method\", in which they described both the linear and bull's eye printing patterns [...] "
                "The patent was issued on 7 October 1952 [...] "
                "The company eventually commissioned a report on the idea, which concluded that it was both feasible and interesting, but that processing the resulting information would require equipment that was some time off in the future. [...] "
                "In July 1972 RCA began an 18-month test in a Kroger store in Cincinnati. [...] "
                "The code proved to have a serious problem; the printers would sometimes smear ink, rendering the code unreadable in most orientations. "
                "However, a linear code, like the one being developed by Woodland at IBM, was printed in the direction of the stripes, so extra ink would simply make the code \"taller\" while remaining readable. "
                "So on 3 April 1973, the IBM UPC was selected as the NAFC standard. [...] "
                "On 26 June 1974, a 10-pack of Wrigley's Juicy Fruit gum was scanned, registering the first commercial use of the UPC.",
                nome="Barcode"),
            wiki("Norman_Joseph_Woodland",
                "While at the beach, Woodland again considered the problem, recalling, from his Boy Scout training, how Morse code dots and dashes are used to send information electronically. "
                "He drew dots and dashes in the sand similar to the shapes used in Morse code. "
                "After pulling them downward with his fingers, producing thin lines resulting from the dots and thick lines from the dashes",
                nome="Norman Joseph Woodland"),
        ],
    },
    # 7 supercola: rejeitada por grudar demais
    {
        "temas_secundarios": ["quimica_cotidiano", "segunda_guerra"],
        "tipos_espanto": ["contraintuitivo", "origem_inesperada"],
        "gancho": "A supercola foi deixada de lado em 1942 por grudar em tudo. Em 1951, testada de novo, grudou demais outra vez e arruinou um aparelho caro de laboratório. Foi aí que o químico Harry Coover viu o que tinha nas mãos.",
        "explicacao": (
            "Os cianoacrilatos surgiram em 1942, numa busca por materiais para fins militares durante a guerra. "
            "Como a fórmula grudava em tudo o que tocava, a equipe de Coover a rejeitou rapidamente. Em 1951, já "
            "na Eastman Kodak, Coover supervisionava químicos que procuravam polímeros resistentes ao calor para as "
            "cúpulas de cabine de jatos, e os cianoacrilatos foram testados outra vez. De novo grudaram demais. "
            "Quando um químico do grupo contou que tinha estragado para sempre um refratômetro caro ao colar suas "
            "peças, Coover percebeu que estava diante de um adesivo único. O produto chegou às lojas em 1958 como "
            "Eastman 910, mais tarde Super Glue. O segredo está na química: o cianoacrilato se polimeriza "
            "depressa na presença de água, formando cadeias longas e fortes, e até a umidade do ar pode endurecer "
            "um tubo aberto. A mesma reação serve à polícia: aquecido, ele solta vapores que reagem com os resíduos "
            "invisíveis das digitais e deixam um polímero branco sobre as linhas. Coover também foi o primeiro a "
            "reconhecer e patentear o uso como adesivo de tecidos do corpo, depois que o filho mais velho fechou "
            "com amostras do laboratório um corte no dedo. Na Guerra do Vietnã, um spray de cianoacrilato foi usado "
            "para conter o sangramento de soldados feridos até que chegassem a um hospital."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Harry_Coover",
                "In 1942, while searching for materials to make more secure cockpit covers for military planes, cyanoacrylate was discovered. "
                "At this time they were deemed too sticky to be of use and were set aside. "
                "In 1951, Coover and his team at Eastman Kodak examined cyanoacrylates again. "
                "Coover was overseeing Kodak chemists investigating heat-resistant polymers for jet canopies when cyanoacrylates were once again tested and proved too sticky. "
                "When a chemist in the group informed Coover that he had permanently damaged an expensive refractometer by gluing it together, Coover recognized that he had discovered a unique adhesive. "
                "In 1958, the adhesive, marketed by Kodak as Eastman 910 and then as Super Glue, was introduced for sale. "
                "Generally, cyanoacrylate is an acrylic resin which rapidly polymerises in the presence of water (specifically hydroxide ions), forming long, strong chains, joining the bonded surfaces together. "
                "Because the presence of moisture causes the glue to set, exposure to moisture in the air can cause a tube or bottle of glue to become unusable over time. [...] "
                "Cyanoacrylate is warmed to produce fumes which react with the invisible fingerprint residues and atmospheric moisture to form a white polymer (polycyanoacrylate) on the fingerprint ridges. [...] "
                "Coover was also the first to recognize and patent cyanoacrylates as a tissue adhesive after his eldest son cut open his finger while making a model and glued the cut closed with the glue he had samples of from the lab",
                nome="Harry Coover"),
            wiki("Cyanoacrylate",
                "as an outgrowth of a search for materials suitable for clear plastic gun sights for the war effort. "
                "In 1942, a team of scientists headed by Harry Coover Jr. stumbled upon a formulation that stuck to everything with which it came in contact. "
                "The team quickly rejected the substance for the wartime application [...] "
                "A cyanoacrylate spray was used in the Vietnam War to reduce bleeding in wounded soldiers until they could be taken to a hospital.",
                nome="Cyanoacrylate"),
        ],
    },
    # 8 Walter Hunt: o alfinete de 15 dólares e a máquina de costura não patenteada
    {
        "temas_secundarios": ["revolucao_industrial", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Walter Hunt criou o alfinete de segurança para pagar uma dívida de 15 dólares e vendeu a patente por 400. Antes, tinha deixado de patentear sua máquina de costura por medo de tirar o emprego das costureiras.",
        "explicacao": (
            "Hunt, um inventor americano prolífico, chegou ao alfinete em 1849 a partir de um pedaço de fio de "
            "latão: uma volta no meio fazia papel de mola, e um fecho numa das pontas protegia o usuário da ponta "
            "afiada. Ele o fez para quitar 15 dólares que devia; segundo sua biografia, o credor era o desenhista "
            "que preparava os desenhos das suas patentes. Vendeu a patente à W. R. Grace and Company por 400 "
            "dólares, pagou a dívida e ficou com 385. A empresa lucrou milhões com o produto. A ideia tinha "
            "parentes: no mesmo ano, o inglês Charles Rowley patenteou, de forma independente, um alfinete parecido, "
            "e a fíbula, um broche dos gregos antigos, já era usada de modo semelhante. A história da máquina de "
            "costura é mais amarga. Anos antes, Hunt construíra uma máquina de ponto fixo, com a agulha furada perto "
            "da ponta e dois fios que se entrelaçavam, em vez de imitar o ponto feito à mão. Não a patenteou porque "
            "temia desempregar as costureiras, e a mulher e a filha, que tinha uma oficina de espartilhos com doze "
            "costureiras, o aconselharam a não vendê-la. Em 1854, na disputa com Elias Howe, que tinha pedido "
            "patente para a mesma ideia, os registros mostraram que Hunt chegara antes. A patente de Howe, porém, "
            "foi mantida: Hunt não tinha cuidado da papelada a tempo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Safety_pin",
                "The fibula, a form of brooch, was invented by the Mycenaeans in the Greek region of Peloponnesus between the 14th and 13th Century BC, and is considered an early precursor to a safety pin since it was used in a similar manner. [...] "
                "The safety pin included a clasp that covered the point and kept it from opening, and a circular twist at the bend to act as a spring and hold it in place. "
                "Charles Rowley (Birmingham, England) independently patented a similar safety pin in October 1849, though they are no longer made. "
                "Hunt made the invention in order to pay off a $15 debt to a friend. "
                "He used a piece of brass wire that was about 8 inches (200 mm) long and made a coil in the center of the wire so it would open up when released. "
                "The clasp at one end was devised in order to shield the sharp edge from the user. [...] "
                "Hunt sold the patent to W.R. Grace and Company for $400 (roughly $15,000 in 2025 dollars). "
                "Using that money, Hunt then paid the $15 owed to a friend and kept the remaining amount of $385 for himself. "
                "In the years to follow, W.R. Grace and Company would make millions of dollars in profits from his invention.",
                nome="Safety pin"),
            wiki("Walter_Hunt_(inventor)",
                "Walter Hunt (July 29, 1796 – June 8, 1859) was an American mechanical engineer. Through the course of his work he became known for being a prolific inventor. [...] "
                "He sold his patent of it for $400 (equivalent to $15,480 in 2025) to W R Grace and Company, to pay a draftsman he owed $15 to (equivalent to $580 in 2025). "
                "J.R. Chapin pressured Hunt to pay off what was due to him for the drafting work he had done on previous inventions that needed patent drawings for application submissions. "
                "Hunt came up with the safety pin (\"C\") in 1849 through experimentation with high tension wire. [...] "
                "It had a characteristic of an eye-pointed needle and used two threads whereby one thread passed through a twisted loop in the other thread and then both interlocked. "
                "The uniqueness of this was that it was the initial time an engineer or technician inventor had not imitated a single stitch done by hand and used two interlocking threads at a seam. [...] "
                "Hunt did not seek a patent for his sewing machine at the time because he worried it would create unemployment with seamstresses. "
                "History records show that his wife and daughter advised him against marketing his sewing apparatus. "
                "Hunt's daughter Caroline operated a corset-making shop with twelve seamstress ladies and was watching out for their interest and thousands of other seamstresses. "
                "This ultimately led to a court case in 1854 when the lockstitch sewing machine concept was applied for by Elias Howe in a patent application. [...] "
                "Records at the Supreme Court show Hunt's invention was made before Howe's machine and the Patent Office identified Hunt's preexistence but it did not issue a patent to him for this. "
                "The reason was because he had not filled out the proper paperwork for a patent before Howe's paperwork application and had abandoned the design experiment of the 1830s. "
                "Hunt acquired public acknowledgement for his invention, however Howe's official patent remained lawful because of the technicality of the timing of the paperwork.",
                nome="Walter Hunt (inventor)"),
        ],
    },
    # 9 o fax comercial antes do telefone (pantelégrafo)
    {
        "temas_secundarios": ["telecomunicacoes", "historia_musica"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Na década de 1860, já funcionava um serviço comercial de fax entre Paris e Lyon, cerca de 11 anos antes da invenção do telefone. A sincronia entre as máquinas dependia de um pêndulo de 8 kg.",
        "explicacao": (
            "O aparelho era o pantelégrafo, do físico italiano Giovanni Caselli, professor da Universidade de "
            "Florença. A ideia de mandar imagens por fio já existia: em 1843, o escocês Alexander Bain patenteara um "
            "telégrafo que imprimia, mas as máquinas dele e as de Frederick Bakewell produziam imagens ruins, porque "
            "transmissor e receptor nunca ficavam de fato sincronizados. Caselli resolveu isso com um relógio "
            "regulador: um pêndulo de 8 kg, num suporte de 2 metros de altura, ligava e desligava a corrente e "
            "mantinha no mesmo passo a agulha que varria a mensagem e a que escrevia do outro lado. O texto ou "
            "desenho era feito com tinta isolante sobre uma placa de metal. Na chegada, o papel vinha embebido em "
            "ferricianeto de potássio, que escurecia onde a corrente passava. Num teste de longa distância entre "
            "Paris e Amiens, a 140 km, a imagem enviada foi a assinatura do compositor Gioachino Rossini, que "
            "escreveu para piano um \"allegretto del pantelegrafo\" para marcar o feito. O serviço comercial começou "
            "na linha Paris–Lyon e depois chegou a Marselha. O uso mais comum era conferir assinaturas em "
            "transações bancárias. E era lento: um papel com cerca de 25 palavras manuscritas levava 108 segundos "
            "para ser transmitido."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Pantelegraph",
                "The pantelegraph (Italian: pantelegrafo; French: pantélégraphe) was an early form of facsimile machine transmitting over normal telegraph lines developed by Giovanni Caselli, used commercially in the 1860s, that was the first such device to enter practical service. [...] "
                "The pantelegraph used a regulating clock with a pendulum which made and broke the current for magnetizing its regulators, and ensured that the transmitter's scanning stylus and the receiver's writing stylus remained in step. "
                "To provide a time base, a large pendulum was used weighing 8 kg (18 lb), mounted on a frame 2 m (6 ft 7 in) high. "
                "Two messages were written with insulating ink on two fixed metal plates [...] "
                "The receiving apparatus reproduced the transmitted image by means of paper impregnated with potassium ferricyanide, which darkened when an electric current passed through it from the synchronized stylus. "
                "In operation the pantelegraph was relatively slow; a sheet of paper 111 mm × 27 mm (4.4 in × 1.1 in), with about 25 handwritten words, took 108 seconds to transmit. "
                "The most common use of the pantelegraph was for signature verification in banking transactions. [...] "
                "While employed teaching physics at the University of Florence, Giovanni Caselli devoted much time to research into the telegraphic transmission of images. [...] "
                "In November 1860 a telegraph line between Paris and Amiens was allotted to Caselli which enabled a true long-distance experiment, which was a complete success, with the signature of the composer Gioachino Rossini as the image sent and received, over a distance of 140 km (87 mi). "
                "The composer wrote a piece, allegretto ‘del pantelegrafo’, for piano, marking the event. [...] "
                "The next year in 1865 the operations started with the Paris to Lyon line and extended to Marseille in 1867.",
                nome="Pantelegraph"),
            wiki("Fax",
                "He received British patent 9745 on May 27, 1843, for his \"Electric Printing Telegraph\". [...] "
                "The Pantelegraph was invented by the Italian physicist Giovanni Caselli. "
                "He introduced the first commercial telefax service between Paris and Lyon in 1865, some 11 years before the invention of the telephone.",
                nome="Fax"),
            wiki("Alexander_Bain_(inventor)",
                "Bain's and Bakewell's laboratory mechanisms reproduced poor quality images and were not viable systems because the transmitter and receiver were never truly synchronized.",
                nome="Alexander Bain (inventor)"),
        ],
    },
    # 10 vidro laminado: o frasco que rachou sem se despedaçar
    {
        "temas_secundarios": ["primeira_guerra", "quimica_cotidiano"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "O vidro laminado dos para-brisas foi inspirado num acidente de laboratório: um frasco revestido de plástico caiu, rachou e não se despedaçou. Caro de início, ele se espalhou nas máscaras de gás da Primeira Guerra.",
        "explicacao": (
            "Em 1903, o químico francês Édouard Bénédictus viu um frasco de vidro que tinha ficado coberto por "
            "nitrato de celulose, um plástico, cair no chão: o vidro se partiu, mas os cacos ficaram no lugar. Em "
            "1909, depois de saber de um acidente de carro em que duas mulheres foram gravemente feridas por "
            "estilhaços, ele pediu patente. Em 1911 fundou a Société du Verre Triplex, que fabricava um composto de "
            "vidro e plástico para reduzir os ferimentos em batidas. A produção era lenta e trabalhosa, o produto "
            "saía caro e as montadoras não o adotaram de imediato. Na Primeira Guerra Mundial, porém, o vidro "
            "laminado foi muito usado nos visores das máscaras contra gases. Bénédictus não estava sozinho na "
            "ideia: em 1902, a empresa francesa Le Carbone patenteara o revestimento de objetos de vidro com "
            "celuloide para que trincassem e quebrassem menos, e em 1905 o advogado inglês John Crewe Wood "
            "patenteou um vidro laminado para para-brisas, com as camadas coladas com bálsamo do Canadá. O "
            "material de hoje veio depois: em 1927, dois químicos canadenses criaram o plástico polivinil butiral, o "
            "PVB, e em 1936 empresas americanas viram que uma camada dele entre dois vidros não perdia a cor e era "
            "difícil de perfurar num acidente."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Laminated_glass",
                "In 1902, the French corporation Le Carbone obtained a patent for coating glass objects with celluloid to render them less susceptible to cracking or breaking. "
                "Laminated glass was invented in 1903 by the French chemist Édouard Bénédictus (1878–1930), inspired by a laboratory accident: a glass flask had become coated with the plastic cellulose nitrate, and when dropped it shattered but did not break into pieces. "
                "In 1909 Bénédictus filed a patent, after hearing about a car accident where two women were severely injured by glass debris. "
                "In 1911, he formed the Société du Verre Triplex, which fabricated a glass-plastic composite to reduce injuries in car accidents. "
                "Production of Triplex glass was slow and painstaking, so it was expensive; it was not immediately widely adopted by automobile manufacturers, but laminated glass was widely used in the eyepieces of gas masks during World War I. [...] "
                "Meanwhile, in 1905, John Crewe Wood, a solicitor in Swindon, Wiltshire, England, patented a laminated glass for use in windshields. "
                "The layers of glass were bonded together by Canada balsam. [...] "
                "In 1927, the Canadian chemists Howard W. Matheson and Frederick W. Skirrow invented the plastic polyvinyl butyral (PVB). "
                "By 1936, United States companies had discovered that laminated \"safety glass\" consisting of a layer of PVB between two layers of glass would not discolor and was not easily penetrated during accidents.",
                nome="Laminated glass"),
        ],
    },
    # 11 Kevlar: a solução turva que iria para o lixo
    {
        "temas_secundarios": ["estados_materia", "quimica_cotidiano"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "O Kevlar dos coletes à prova de bala veio de uma solução turva que normalmente iria para o lixo. A química Stephanie Kwolek convenceu o técnico a fiá-la, apesar do medo de que ela entupisse a máquina.",
        "explicacao": (
            "Em 1964, prevendo falta de gasolina, a DuPont buscava uma fibra leve e resistente para substituir o "
            "aço dos pneus, e o grupo de Kwolek entrou na busca. Os polímeros com que ela trabalhava formavam uma "
            "solução rala, turva, opalescente quando mexida, com aspecto de leitelho. Ela comparou: soluções de "
            "polímero costumam ser claras ou translúcidas e grossas como melaço. Aquele tipo de líquido turvo "
            "normalmente era descartado. Sem saber na hora, Kwolek tinha preparado um cristal líquido, em que as "
            "moléculas, em forma de bastão, ficam muito bem ordenadas. Negaram a ela o uso da fieira, porque se "
            "achava que a solução entupiria o equipamento, mas ela convenceu o técnico que o operava, Charles "
            "Smullen, a fazer o teste. A fibra não se rompia nas condições em que o náilon se romperia e, por peso, "
            "era cinco vezes mais forte que o aço. O Kevlar moderno foi lançado em 1971. Naquele ano, Lester "
            "Shubin, de um instituto federal de pesquisa sobre polícia e justiça criminal, sugeriu trocar o náilon "
            "dos coletes à prova de bala pelo novo material. Ele contou depois que dobraram o tecido algumas vezes, "
            "atiraram, e as balas não atravessaram. Kwolek, que cedeu a patente à DuPont, não lucrou com os "
            "produtos feitos com sua descoberta."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Stephanie_Kwolek",
                "She then extended her work into poly-p-benzamide and poly-p-phenylene terephthalamide, which she noted adopted highly regular rodlike molecular arrangements in solution. [...] "
                "In 1964, in anticipation of a gasoline shortage, Kwolek's group began searching for a lightweight yet strong fiber to replace the steel used in tires. [...] "
                "The solution was unusually (low viscosity), turbid, stir-opalescent and buttermilk in appearance. "
                "Conventional polymer solutions are usually clear or translucent and have the viscosity of molasses, more or less. [...] "
                "This was a liquid crystalline solution, but I did not know it at the time. "
                "This sort of cloudy solution was usually thrown away. "
                "Kwolek was denied the use of the spinneret for her solution because it was thought the solution would clog the machine. "
                "However, Kwolek persuaded technician Charles Smullen, who ran the spinneret, to test her solution. "
                "She was amazed to find that the new fiber would not break when nylon typically would. "
                "Not only was it stronger than nylon, Kevlar was five times stronger than steel by weight. [...] "
                "By 1971, modern Kevlar was introduced. [...] "
                "The polymer molecules, shaped like rods or matchsticks, are highly oriented, which gives Kevlar its extraordinary strength. [...] "
                "She did not profit from DuPont's products, as she signed over the Kevlar patent to the company.",
                nome="Stephanie Kwolek"),
            wiki("Kevlar",
                "In 1971, Lester Shubin, who was then the director of Science and Technology for the National Institute for Law Enforcement and Criminal Justice, suggested using Kevlar to replace nylon in bullet-proof vests. [...] "
                "Shubin later recalled how the idea developed: \"We folded it over a couple of times and shot at it. The bullets didn't go through.\"",
                nome="Kevlar"),
        ],
    },
    # 12 Kearns: o limpador que pisca e a briga com a Ford
    {
        "temas_secundarios": ["leis_julgamentos", "transportes"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "O limpador de para-brisa intermitente foi modelado no piscar do olho. O inventor, Robert Kearns, processou a Ford e a Chrysler, atuou boa parte do tempo como o próprio advogado e venceu as duas.",
        "explicacao": (
            "Kearns, engenheiro americano, dizia que tudo começou na noite de núpcias, em 1953, quando uma rolha de "
            "champanhe o atingiu no olho esquerdo e o deixou legalmente cego dele. Em 1963, dirigindo sob chuva "
            "fraca, irritou-se com o movimento contínuo das palhetas, que incomodava sua visão. Modelou então o "
            "mecanismo no olho humano, que pisca a cada poucos segundos, e não sem parar, e pediu a primeira patente "
            "em 1964. Outros inventores já tinham feito projetos parecidos, que não chegaram às fábricas. Kearns "
            "ofereceu a ideia às três grandes montadoras americanas. Todas recusaram, mas a partir de 1969 passaram "
            "a instalar limpadores intermitentes eletrônicos baseados no projeto dele. Na Justiça, a defesa das "
            "empresas era que o sistema não tinha nenhum componente novo, só peças de prateleira; Kearns respondia "
            "que a novidade estava na combinação. O processo contra a Ford durou de 1978 a 1990. Ele recusou um "
            "acordo de 30 milhões de dólares e foi ao júri, que lhe deu 5,2 milhões; a Ford aceitou pagar 10,2 "
            "milhões para evitar outra rodada. Contra a Chrysler, interrogando ele mesmo as testemunhas, ganhou em "
            "1992. No fim, depois de gastar mais de 10 milhões em honorários, recebeu cerca de 30 milhões da "
            "Chrysler. A mulher dele contou que ouvia desde o primeiro dia que aquilo não era por dinheiro, e que "
            "nenhum advogado acreditava."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Robert_Kearns",
                "His first patent for the invention was filed on December 1, 1964, after a few previous designs by other inventors had failed to gain any traction in manufacturing. [...] "
                "he tried to interest the \"Big Three\" auto makers (General Motors, Ford, and Chrysler) in licensing the technology.  "
                "Each rejected his proposal, yet began to install electronic intermittent wipers based on Kearns's design in their cars, beginning in 1969 [...] "
                "Kearns claimed that the inspiration for his invention stems from an incident on his wedding night in 1953, when an errant champagne cork shot into his left eye, leaving him legally blind in that eye. "
                "Nearly a decade later in 1963, Kearns was driving his Ford Galaxie through a light rain, and the constant movement of the wiper blades irritated his already troubled vision. "
                "He modeled his mechanism on the human eye, which blinks every few seconds, rather than continuously [...] "
                "The lawsuit against the Ford Motor Company was opened in 1978 and ended in 1990. [...] "
                "He turned down a $30 million settlement offer in 1990 and took it to the jury, which awarded him $5.2 million; Ford agreed to pay $10.2 million rather than face another round of litigation. "
                "Kearns mostly acted as his own attorney in the subsequent suit against Chrysler, which began in 1982, even questioning witnesses on the stand. "
                "The Chrysler verdict was decided in Kearns's favor in 1992. [...] "
                "By 1995, after spending over US$10 million in legal fees, Kearns received approximately US$30 million in compensation for Chrysler's patent infringement. [...] "
                "His wife said, \"He told me from day one, 'This is not about money,' no lawyer believed it.\" [...] "
                "Ford claimed that the patent was invalid because Kearns's intermittent windshield wiper system had no new components (it used all \"off-the-shelf\" parts). "
                "Kearns noted that his invention was a novel and non-obvious combination of parts.",
                nome="Robert Kearns"),
        ],
    },
    # 13 corretivo líquido: a secretária demitida pela própria marca
    {
        "temas_secundarios": ["economia_curiosa", "historia_musica"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "O corretivo líquido foi criado por uma secretária que também pintava vitrines e resolveu cobrir os erros de datilografia com tinta. Ela foi demitida depois de assinar uma carta com o nome da própria empresa de corretivo.",
        "explicacao": (
            "Em 1951, Bette Nesmith Graham era secretária executiva do presidente do conselho de um banco do Texas "
            "e usava uma máquina de escrever elétrica da IBM, na qual era difícil consertar erros; um deslize podia "
            "obrigar a datilografar a página inteira de novo. Para ganhar um extra, ela pintava a vitrine de festas "
            "do banco, e o costume de cobrir com tinta um erro no desenho para refazê-lo lhe deu a ideia. Misturou "
            "tinta têmpera branca, à base de água, no tom do papel do escritório e passava sobre os erros com um "
            "pincel de aquarela. Escondeu isso por cinco anos, já que podia parecer trapaça. Quando cerca de uma "
            "dúzia de colegas pediu o produto, ela o chamou de \"Mistake Out\" e passou a prepará-lo no liquidificador "
            "de casa, envasando em frascos vazios de esmalte, ketchup e mostarda. O filho, Michael Nesmith, que "
            "depois seria guitarrista dos Monkees, montava frascos na garagem com os amigos por 1 dólar a hora. Em "
            "1958, ela foi demitida do emprego de secretária por ter assinado uma correspondência, por engano, com a "
            "identificação \"The Mistake Out Company\". Passou a se dedicar só à empresa, rebatizada de Liquid "
            "Paper, que em 1975 produzia 25 milhões de frascos por ano. Em 1979, ela a vendeu à Gillette."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Bette_Nesmith_Graham",
                "Graham founded the Liquid Paper Company in 1958, built it into a multimillion-dollar business with international reach, and sold it to Gillette Corporation in 1979. "
                "She was the mother of musician and actor Michael Nesmith, known primarily as a member of The Monkees. [...] "
                "Nesmith was a musician who later became the guitarist of The Monkees. [...] "
                "In 1951, McMurray was executive secretary for W. W. Overton, the chairman of the board of the Texas Bank and Trust, and used an IBM electric typewriter. "
                "The machine made it difficult to fix typos, and McMurray was frustrated that a small error could make it necessary to retype entire pages. "
                "She painted the bank's holiday window display to earn extra money, and the process of painting over a design mistake to re-do it inspired her to create the first correctional fluid prototypes. "
                "McMurray mixed white water-based tempera paint to match the color of her workplace stationery; she then applied it over errors with a watercolor brush. "
                "Using this method, she successfully concealed mistakes, though it could be seen as cutting corners or cheating at her job. "
                "\"I tried to keep it a secret,\" she said, adding that \"for five years I did just that\". "
                "About a dozen colleagues asked McMurray for the product, so she created a label and the name \"Mistake Out\". "
                "She continued to develop the product from her North Dallas home, mixing it in a kitchen blender and pouring it into empty nail polish bottles, ketchup bottles, and mustard bottles. [...] "
                "McMurray hired her son and his friends to assemble bottles of the product in her garage for $1 an hour. [...] "
                "In 1958, McMurray was fired from her secretarial job after mistakenly signing correspondence with the notation \"The Mistake Out Company\". "
                "After losing her job, McMurray worked at her correctional fluid business full-time. "
                "That same year, she renamed her business the Liquid Paper Company and applied for a patent and trademark. [...] "
                "By 1975, \"Liquid Paper was producing 25 million bottles a year",
                nome="Bette Nesmith Graham"),
        ],
    },
    # 14 esferográfica: tinta de jornal, bolinhas de gude e a "birome"
    {
        "temas_secundarios": ["personagens_esquecidos", "segunda_guerra"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "Na Argentina, a esferográfica se chama \"birome\", mistura dos nomes de dois sócios. Um deles, o húngaro László Bíró, viu que a tinta de jornal não corria numa caneta-tinteiro e trocou a pena por uma bolinha.",
        "explicacao": (
            "A ideia tinha precursor: em 1888, o americano John J. Loud patenteou uma caneta com uma bolinha de aço "
            "giratória, feita para marcar caixas e embalagens. Ela era grosseira demais para escrever cartas, não "
            "teve uso comercial e a patente caducou. Bíró, jornalista, se irritava com o tempo gasto para encher "
            "canetas-tinteiro e com as páginas borradas. Percebeu que a tinta usada na impressão de jornais secava "
            "rápido e não manchava, mas, numa caneta-tinteiro, ela não chegava à ponta, de tão viscosa. Segundo sua "
            "biografia, a solução surgiu em 1930, quando ele viu crianças jogando bolinhas de gude numa poça: elas "
            "deixavam um rastro de água por onde rolavam. Com o irmão György, criou uma ponta com uma esfera livre "
            "para girar num encaixe, que pegava a tinta viscosa do cartucho e a depositava no papel. O equilíbrio "
            "era delicado: encaixe apertado ou tinta grossa demais, e nada saía; encaixe frouxo ou tinta rala "
            "demais, e a caneta vazava. Fugindo dos nazistas, os irmãos se mudaram para a Argentina, onde fundaram "
            "a Biro Pens of Argentina com o sócio Juan Jorge Meyne. O projeto foi licenciado no Reino Unido para as "
            "tripulações da Força Aérea, porque nos aviões as canetas-tinteiro tendiam a vazar. Na Argentina, o Dia "
            "do Inventor é comemorado em 29 de setembro, aniversário de Bíró."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("Ballpoint_pen",
                "The first patent for a ballpoint pen was issued on 30 October 1888 to American inventor John J. Loud [...] "
                "Loud's pen had a small rotating steel ball held in place by a socket. "
                "Loud intended his invention for marking boxes and packaging, not for precision or detail, and it proved too coarse for letter-writing. "
                "With no commercial viability, its potential went unexploited, and the patent eventually lapsed. [...] "
                "If the ball socket was too tight or the ink too thick, it would not reach the paper. "
                "If the socket was too loose or the ink too thin, the pen would leak, or the ink would smear. [...] "
                "László Bíró, a Hungarian newspaper editor (later a naturalized Argentine) frustrated by the amount of time that he wasted filling up fountain pens and cleaning up smudged pages, noticed that inks used in newspaper printing dried quickly, leaving the paper dry and smudge-free. [...] "
                "Their pen was sold in Argentina as the \"Birome\", from the names Bíró and Meyne, which is how ballpoint pens are still known in that country. "
                "This new design was licensed by the British engineer Frederick George Miles and manufactured by his company Miles Aircraft, to be used by Royal Air Force aircrew as the \"Biro\". "
                "Ballpoint pens were found to be more versatile than fountain pens, especially in airplanes, where fountain pens were prone to leak.",
                nome="Ballpoint pen"),
            wiki("László_Bíró",
                "While working as a journalist, Bíró noticed that the ink used in newspaper printing dried quickly, leaving the paper dry and smudge-free. "
                "He tried using the same ink in a fountain pen, but found that it would not flow into the tip, as it was too viscous. "
                "In 1930 he observed children playing with marbles in a puddle, noticing that the marbles left a trail of water in their wake. [...] "
                "Working with his brother György, a chemist, he developed a new tip consisting of a ball that was free to turn in a socket, and as it turned it would pick up a special viscous ink from a cartridge and then roll to deposit it on the paper. [...] "
                "During World War II, Bíró fled the Nazis with his brother. [...] "
                "formed Biro Pens of Argentina (in Argentina and Uruguay the ballpoint pen is known as birome, a portmanteau of the brothers' surname with that of their business partner, Juan Jorge Meyne). [...] "
                "Argentina's Inventors' Day is celebrated on Bíró's birthday, 29 September.",
                nome="László Bíró"),
        ],
    },
    # 15 aço inox: o ácido que não atacava e a corrida de vários inventores
    {
        "temas_secundarios": ["elementos_quimicos", "primeira_guerra"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "O aço inox de Harry Brearley saiu de uma pesquisa para canos de armas. A pista foi um incômodo: as amostras com cromo resistiam ao ácido usado para examiná-las. E outros inventores chegaram lá quase ao mesmo tempo.",
        "explicacao": (
            "Pouco antes da Primeira Guerra, a produção de armas cresceu no Reino Unido, e o desgaste interno dos "
            "canos virou problema. Em Sheffield, Brearley passou a testar aços com cromo, que eleva o ponto de "
            "fusão, buscando resistir à erosão causada pelas altas temperaturas. Para estudar ao microscópio a "
            "estrutura dessas ligas, era preciso polir as amostras e atacá-las com ácido. No aço comum, ácido "
            "nítrico diluído em álcool bastava, mas as novas ligas resistiam muito ao ataque químico. Criado numa "
            "cidade famosa pelos talheres desde o século XVI, Brearley provavelmente por isso viu ali utilidade para "
            "facas e panelas, que enferrujavam se não fossem polidas com frequência, e testou as ligas com vinagre "
            "e suco de limão. Chamou o material de \"aço sem ferrugem\"; o nome \"stainless\" foi sugerido por um "
            "fabricante de talheres da cidade. Segundo relatos, o primeiro aço inox de verdade saiu de um forno "
            "elétrico em agosto de 1913. Ele não estava sozinho. A resistência de ligas de ferro e cromo a alguns "
            "ácidos talvez tenha sido notada já em 1821 pelo francês Pierre Berthier, que sugeriu usá-las em "
            "talheres. Em 1912, engenheiros da Krupp, na Alemanha, patentearam o aço inox hoje chamado 18/8, e o "
            "americano Elwood Haynes pediu patente de outro tipo. Quando Brearley tentou patentear nos Estados "
            "Unidos, em 1915, descobriu que Haynes já tinha registrado um pedido, e os dois acabaram sócios."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Harry_Brearley",
                "In the troubled years immediately before the First World War, arms manufacturing increased significantly in the UK, but practical problems were encountered due to erosion (excessive wear) of the internal surfaces of gun barrels. "
                "Brearley began to research new steels which could better resist the erosion caused by high temperatures (rather than corrosion, as is often mentioned in this regard). "
                "He began to examine the addition of chromium to steel, which was known to raise the material's melting point, as compared to the standard carbon steels. [...] "
                "In order to undertake metallography to study the microstructure of the experimental alloys (the main factor responsible for a steel's mechanical properties), it was necessary to polish and etch the metallic samples produced. "
                "For a carbon steel, a dilute solution of nitric acid in alcohol is sufficient to produce the required etching, but Brearley found that the new chromium steels were highly resistant to chemical attack. [...] "
                "It was probably Harry Brearley's upbringing in Sheffield, a city famous for the manufacture of cutlery since the 16th century, which led him to appreciate the potential of these new steels [...] "
                "Up to that time carbon-steel knives were prone to unhygienic rusting if they were not frequently polished [...] "
                "With this in mind Brearley extended his examinations to include tests with food acids such as vinegar and lemon juice, with very promising results. "
                "Brearley initially called the new alloy \"rustless steel\"; the more euphonic \"stainless steel\" was suggested by Ernest Stuart of R.F. Mosley's, a local cutlery manufacturer at Portland Works [...] "
                "It is reported that the first true stainless steel, a 0.24 wt% C, 12.8 wt% Cr ferrous alloy, was produced by Brearley in an electric furnace on 13 August 1913.",
                nome="Harry Brearley"),
            wiki("Stainless_steel",
                "The corrosion resistance of iron-chromium alloys may have been first recognized in 1821 by Pierre Berthier, who noted their resistance against attack by some acids and suggested their use in cutlery. [...] "
                "On 17 October 1912, Krupp engineers Benno Strauss and Eduard Maurer patented as Nirosta the austenitic stainless steel that became known as 18/8 or AISI type 304. [...] "
                "In 1912, Elwood Haynes applied for a US patent on a martensitic stainless steel alloy, which was not granted until 1919. [...] "
                "Brearley applied for a US patent during 1915 only to find that Haynes had already registered one. "
                "Brearley and Haynes pooled their funding and, with a group of investors, formed the American Stainless Steel Corporation",
                nome="Stainless steel"),
        ],
    },
]
