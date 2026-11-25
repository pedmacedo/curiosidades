LOTE = "2026-11-24-asteroides_cometas-01"
AREA = "espaco"
TEMA = "asteroides_cometas"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 DART: a batida que encurtou a órbita de Dimorphos em 32 minutos
    {
        "temas_secundarios": ["exploracao_espacial", "sistema_solar"],
        "tipos_espanto": ["engenhosidade", "escala_absurda"],
        "gancho": "Em 2022, a NASA jogou uma sonda contra uma pequena lua de asteroide para ver se dava para desviá-la. A meta mínima era mudar a órbita em 73 segundos. Mudou em 32 minutos, e o empurrão veio mais dos detritos.",
        "explicacao": (
            "A missão DART, sigla em inglês para Teste de Redirecionamento de Asteroide Duplo, mirou Dimorphos, uma "
            "lua que gira em volta do asteroide Didymos. A sonda se chocou contra ela em 26 de setembro de 2022, a "
            "cerca de 23.000 km/h, a uns 11 milhões de quilômetros da Terra. Antes da batida, Dimorphos dava uma volta "
            "em Didymos em 11 horas e 55 minutos; depois, em 11 horas e 23 minutos, segundo a NASA, com margem de "
            "uns 2 minutos. O critério de sucesso fixado antes era bem mais modesto: 73 segundos. O resultado passou "
            "dessa marca mais de 25 vezes. A explicação está no material arrancado da superfície. Os detritos lançados "
            "ao espaço funcionaram como um recuo, e esse recuo foi bem maior do que o empurrão da própria sonda. Para "
            "a NASA, foi a primeira vez que a humanidade mudou de propósito o movimento de um corpo celeste e a "
            "primeira demonstração em escala real de uma técnica para desviar asteroides. Estudos posteriores ainda "
            "concluíram que a batida alterou levemente a órbita do par de asteroides em volta do Sol."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.nasa.gov/news-release/nasa-confirms-dart-mission-impact-changed-asteroids-motion-in-space/",
             "titulo": "NASA Confirms DART Mission Impact Changed Asteroid's Motion in Space", "idioma": "en",
             "trecho": "This marks humanity's first time purposely changing the motion of a celestial object and the first full-scale demonstration of asteroid deflection technology. [...] "
                       "the investigation team has confirmed the spacecraft's impact altered Dimorphos' orbit around Didymos by 32 minutes, shortening the 11 hour and 55-minute orbit to 11 hours and 23 minutes. "
                       "This measurement has a margin of uncertainty of approximately plus or minus 2 minutes. "
                       "Before its encounter, NASA had defined a minimum successful orbit period change of Dimorphos as change of 73 seconds or more. "
                       "This early data show DART surpassed this minimum benchmark by more than 25 times."},
            wiki("Double_Asteroid_Redirection_Test",
                 "the DART spacecraft collided with Dimorphos at 14,000 mph (23,000 km/h) on 26 September 2022 about 6.8 million miles (10.9 million kilometers) from Earth. "
                 "The collision shortened Dimorphos's orbit around Didymos by 32 minutes, greatly in excess of the pre-defined success threshold of 73 seconds. "
                 "Deflection resulted from the ejection of debris which caused a recoil that was substantially larger than the impact itself. [...] "
                 "Scientists later determined that the impact also slightly changed the orbit of the asteroid pair around the Sun",
                 nome="Double Asteroid Redirection Test"),
        ],
    },
    # 2 Tunguska: a explosão que derrubou milhões de árvores sem deixar cratera
    {
        "temas_secundarios": ["paisagens_extremas", "atmosfera"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Em 1908, uma explosão na Sibéria derrubou milhões de árvores numa área de mais de 2.150 km². Quem foi ao local esperava uma cratera e não achou nenhuma: no centro, as árvores continuavam de pé, sem galhos.",
        "explicacao": (
            "O evento de Tunguska, em 30 de junho de 1908, devastou uma região remota da taiga siberiana. A onda de choque jogou testemunhas no chão, matou pelo "
            "menos três pessoas e quebrou janelas num raio de 200 km. A primeira expedição científica, liderada por "
            "Leonid Kulik, foi organizada em 1921, mas ele só achou o epicentro em 1927. A equipe esperava uma "
            "cratera de impacto e se surpreendeu: não havia nenhuma. Havia, sim, uma zona de uns 8 km em que as "
            "árvores estavam chamuscadas e sem galhos, mas em pé. Em volta, os troncos caídos formavam um padrão "
            "radial, como as asas de uma borboleta, e esse desenho indicava uma origem aérea. O consenso científico "
            "atribui o evento a um meteoroide que explodiu na atmosfera. A hipótese preferida é a de uma rocha de "
            "50 a 60 metros que explodiu entre 5 e 10 km de altitude. Nas noites seguintes, o céu ficou tão claro "
            "numa área de uns 12 milhões de km², no oeste da Eurásia, que deu para ler jornal à meia-noite sem luz "
            "artificial."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Tunguska_event",
            "The Tunguska event was a large explosion that occurred on the morning of 30 June [O.S. 17 June] 1908 [...] "
            "The cataclysm occurred in a remote and sparsely populated region of the taiga [...] "
            "devastated the taiga, flattening several million trees over an area of more than 2,150 km2 (830 sq mi), while decimating numerous reindeer and dogs belonging to the Evenks. "
            "Under the effect of the shock wave, the trees were felled in a radial pattern forming the characteristic shape of two \"butterfly wings\" around the central area. "
            "At the epicenter itself, the blast stripped the trees of their branches but left them standing [...] "
            "The shock wave knocked several witnesses to the ground, killed at least three people as well as numerous animals, and shattered windows within a 200 km (120 mi) radius. [...] "
            "researchers favor the hypothesis of a 50–60 m (160–200 ft) diameter meteoroid moving at high speed from the south-east. "
            "The object would have exploded between 5–10 km (3.1–6.2 mi) in altitude [...] "
            "it became possible to read a newspaper or photograph monuments around midnight without artificial lighting. [...] "
            "From 30 June to 3 July, intense bright nights were observed across western Eurasia over an area of about 12,000,000 km2 (4,600,000 sq mi). [...] "
            "it was not until 1921 that a first scientific expedition was organized under the direction of Leonid Kulik, who discovered the site of the epicenter only in 1927. "
            "Kulik and his successors' research revealed that the explosion devastated nearly 2,150 km2 (830 sq mi) of forest in a radial pattern which implied an aerial origin. "
            "The scientific consensus thus attributes this event to a meteor air burst, the atmospheric explosion of a celestial [...] "
            "Kulik led a scientific expedition to the Tunguska blast site in 1927. "
            "He hired local Evenki hunters to guide his team to the centre of the blast area, where they expected to find an impact crater. "
            "To their surprise, there was no crater at ground zero. "
            "Instead, they found a zone, roughly 8 km (5.0 mi) across, where the trees were scorched and devoid of branches, but still standing upright",
            nome="Tunguska event")],
    },
    # 3 Chelyabinsk: o meteoro que ninguém viu chegar e as vidraças
    {
        "temas_secundarios": ["atmosfera", "acustica"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Em 2013, enquanto o mundo esperava a passagem prevista de um asteroide, outro, que ninguém viu chegar porque vinha da direção do Sol, explodiu sobre a Rússia. A maioria dos 1.491 feridos foi atingida por vidro quebrado.",
        "explicacao": (
            "O meteoro de Chelyabinsk, uma rocha de uns 17 a 20 metros segundo a NASA, entrou na atmosfera em 15 de "
            "fevereiro de 2013 e por um instante brilhou mais que o Sol. Ele não foi detectado antes, em parte porque "
            "chegou do lado do céu onde está o Sol. No mesmo dia, cerca de 16 horas depois, passaria pela Terra um "
            "asteroide maior, o 367943 Duende, previsto havia muito tempo; as órbitas mostraram que os dois não tinham "
            "relação. A explosão no ar não feriu ninguém diretamente. Os ferimentos vieram de efeitos indiretos, "
            "sobretudo de vidraças estouradas pela onda de choque, que chegou minutos depois do clarão; cerca de "
            "7.200 prédios foram danificados. Numa escola de Chelyabinsk, a professora Yulia "
            "Karbysheva, sem saber o que era a luz, mandou os 44 alunos se afastarem das janelas e se abrigarem sob "
            "as carteiras. Ela ficou de pé e teve um tendão cortado pelo vidro; nenhum aluno se feriu. O clarão "
            "também causou dor nos olhos e queimaduras parecidas com as de sol."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Chelyabinsk_meteor",
            "was a superbolide that entered Earth's atmosphere over the southern Ural region in Russia on 15 February 2013 [...] "
            "The object approached Earth undetected before its atmospheric entry, in part because its radiant (source direction) was close to the Sun. "
            "1,491 people were injured seriously enough to seek medical treatment. "
            "All of the injuries were due to indirect effects rather than the meteor itself, mainly from broken glass from windows that were blown in when the shock wave arrived, minutes after the superbolide's flash. "
            "Around 7,200 buildings in six cities across the region were damaged [...] "
            "The light from the meteor was briefly brighter than the Sun [...] "
            "The blast created by the meteor's air burst produced extensive ground damage [...] "
            "The earlier-predicted and well-publicized close approach of a larger asteroid on the same day, the roughly 30 meters (100 feet) 367943 Duende, occurred about 16 hours later; "
            "the very different orbits of the two objects showed they were unrelated to each other. [...] "
            "The intense light from the meteor, momentarily brighter than the Sun, also produced injuries, resulting in more than 180 cases of eye pain [...] "
            "Twenty people reported ultraviolet burns similar to sunburn [...] "
            "A fourth-grade teacher in Chelyabinsk, Yulia Karbysheva, was hailed as a hero after saving 44 children from imploding window glass cuts. "
            "Despite not knowing the origin of the intense flash of light, Karbysheva thought it prudent to take precautionary measures by ordering her students to stay away from the room's windows and to perform a duck and cover manoeuvre and then to leave the building. "
            "Karbysheva, who remained standing, was seriously lacerated when the blast arrived and window glass severed a tendon in one of her arms and left thigh; "
            "none of her students, whom she ordered to hide under their desks, suffered cuts. [...] "
            "The United States space agency NASA estimated the diameter of the bolide at about 17 to 20 meters",
            nome="Chelyabinsk meteor")],
    },
    # 4 ʻOumuamua: o visitante interestelar que acelerou sem cauda
    {
        "temas_secundarios": ["exoplanetas", "astrobiologia"],
        "tipos_espanto": ["misterio_aberto", "escala_absurda"],
        "gancho": "O primeiro objeto vindo de fora do Sistema Solar foi visto em 2017, já indo embora. Ele acelerou como um cometa que solta gás, mas não mostrou nenhuma nuvem de gás ou poeira. Do que era feito, ninguém sabe.",
        "explicacao": (
            "ʻOumuamua foi descoberto em 19 de outubro de 2017 por um telescópio no Havaí, uns 40 dias depois de "
            "passar pelo ponto mais próximo do Sol. Já se afastava quando foi notado. A trajetória, fortemente "
            "hiperbólica, mostrou que ele não estava preso ao Sol: veio do espaço interestelar e para lá voltará. Por "
            "ser o primeiro do tipo, ganhou uma nova designação, \"1I\", de interestelar. O nome, em havaiano, quer "
            "dizer algo como \"primeiro mensageiro distante\". Primeiro foi chamado de cometa, depois de asteroide, "
            "porque imagens profundas não mostraram coma, a nuvem que envolve os cometas perto do Sol. Em 2018, porém, "
            "astrônomos mediram uma aceleração que a gravidade não explicava, compatível com um cometa soltando gás ou "
            "com a pressão da luz solar. As propostas se multiplicaram: gelo de nitrogênio, como um pedaço de um "
            "planeta parecido com Plutão, ou gelo de hidrogênio, depois considerado incapaz de sobreviver à viagem. "
            "A composição dele continua desconhecida, e ele saiu de alcance dos telescópios em poucos meses."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("%CA%BBOumuamua",
            "1I/ʻOumuamua is the first confirmed interstellar object detected passing through the Solar System. "
            "Formally designated 1I/2017 U1, it was discovered by Canadian physicist Robert Weryk using the Pan-STARRS telescope at Haleakalā Observatory, Hawaii, on 19 October 2017, "
            "approximately 40 days after it passed its closest point to the Sun on 9 September. [...] "
            "already heading away from the Sun. [...] "
            "Despite its close approach to the Sun, it showed no signs of having a coma,  the usual nebula around comets formed when they pass near the Sun. "
            "Further, it exhibited non‑gravitational acceleration, potentially due to outgassing or a push from solar radiation pressure. [...] "
            "It roughly translates to 'first distant messenger'. [...] "
            "A two-week observation arc had verified a strongly hyperbolic trajectory. [...] "
            "On 27 June 2018, astronomers reported a non-gravitational acceleration to ʻOumuamua's trajectory, potentially consistent with a push from solar radiation pressure. [...] "
            "However, it was later calculated that hydrogen icebergs cannot survive their journey through interstellar space. [...] "
            "Originally classified as comet C/2017 U1, it was later reclassified as asteroid A/2017 U1 due to the absence of a coma. "
            "Once it was unambiguously identified as coming from outside the Solar System, a new designation was created: I, for Interstellar object. [...] "
            "the compositional nature of the object continues to be unknown. [...] "
            "a piece of an exoplanet rich in nitrogen ice, similar to Pluto. [...] "
            "so it will eventually leave the Solar System and continue into interstellar space. [...] "
            "very deep stacked images were taken at the Very Large Telescope later the same day, but the object showed no presence of a coma. [...] "
            "in mid-December 2017, it was too faint and fast-moving to be studied by even the largest ground-based telescopes.",
            nome="ʻOumuamua")],
    },
    # 5 Bennu: ingredientes da vida e água salgada num asteroide
    {
        "temas_secundarios": ["astrobiologia", "genetica"],
        "tipos_espanto": ["conexao_inesperada", "misterio_aberto"],
        "gancho": "A poeira do asteroide Bennu, trazida à Terra em 2023, tem 14 dos 20 aminoácidos das proteínas e as cinco bases do DNA e do RNA. E tem um enigma: os aminoácidos vêm meio \"canhotos\", meio \"destros\", e os da vida não.",
        "explicacao": (
            "A sonda OSIRIS-REx, da NASA, recolheu 121,6 gramas do asteroide Bennu e os entregou à Terra em 2023. As "
            "primeiras análises detalhadas, divulgadas em 2025, acharam 14 dos 20 aminoácidos que a vida terrestre usa "
            "para montar proteínas e todas as cinco bases nitrogenadas que guardam e transmitem instruções genéticas "
            "no DNA e no RNA. Havia também amônia em quantidade excepcional e formaldeído, que podem reagir e formar "
            "moléculas complexas como aminoácidos. Outro grupo identificou 11 minerais que se formam quando água com "
            "sais dissolvidos evapora devagar, como halita e calcita: sinal de uma antiga água salgada, um possível "
            "\"caldo\" para essas reações. Segundo a NASA, isso não é evidência de vida, mas sugere que as condições "
            "para ela surgir eram comuns no início do Sistema Solar. Fica a pergunta: muitos aminoácidos existem em "
            "duas versões espelhadas, como mão esquerda e mão direita. A vida na Terra usa quase só a esquerda, mas "
            "Bennu tem as duas na mesma proporção. Por que a vida \"virou à esquerda\" continua um mistério."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.nasa.gov/news-release/nasas-asteroid-bennu-sample-reveals-mix-of-lifes-ingredients/",
             "titulo": "NASA's Asteroid Bennu Sample Reveals Mix of Life's Ingredients", "idioma": "en",
             "trecho": "a history of saltwater that could have served as the \"broth\" for these compounds to interact and combine. "
                       "The findings do not show evidence for life itself, but they do suggest the conditions necessary for the emergence of life were widespread across the early solar system [...] "
                       "the Bennu samples, which OSIRIS-REx delivered to Earth in 2023. [...] "
                       "amino acids – 14 of the 20 that life on Earth uses to make proteins – and all five nucleobases that life on Earth uses to store and transmit genetic instructions in more complex terrestrial biomolecules, such as DNA and RNA [...] "
                       "Scientists also described exceptionally high abundances of ammonia in the Bennu samples. "
                       "Ammonia is important to biology because it can react with formaldehyde, which also was detected in the samples, to form complex molecules, such as amino acids [...] "
                       "Ranging from calcite to halite and sylvite, scientists identified traces of 11 minerals in the Bennu sample that form as water containing dissolved salts evaporates over long periods of time [...] "
                       "Many amino acids can be created in two mirror-image versions, like a pair of left and right hands. "
                       "Life on Earth almost exclusively produces the left-handed variety, but the Bennu samples contain an equal mixture of both. [...] "
                       "The reason life \"turned left\" instead of right remains a mystery."},
            wiki("OSIRIS-REx",
                 "In total, 121.6 g (4.29 oz) of asteroidal material was recovered from the sample container. [...] "
                 "In January 2025, it was reported that a wide range of carbon- and nitrogen-rich organic compounds have been identified in samples returned from Bennu",
                 nome="OSIRIS-REx"),
        ],
    },
    # 6 Bennu: a sonda teria afundado no asteroide
    {
        "temas_secundarios": ["exploracao_espacial", "estados_materia"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Em 2020, a sonda OSIRIS-REx tocou o asteroide Bennu para colher amostras. A superfície era tão frouxa, de partículas mal presas umas às outras, que ela teria afundado se não acionasse logo os propulsores.",
        "explicacao": (
            "Bennu tem uns 490 metros de diâmetro. Medições dos efeitos gravitacionais e térmicos deram uma "
            "densidade média só um pouco maior que a da água, o que sugere que uns 40% do interior sejam espaços "
            "vazios. Por isso, ele é visto como uma pilha de escombros: o material que o forma veio da quebra de um "
            "corpo muito maior. A sonda OSIRIS-REx, da NASA, tocou a superfície em 20 de outubro de 2020. No contato, "
            "um jato de gás nitrogênio soprou partículas menores que 2 cm para dentro do coletor, na ponta de um "
            "braço robótico. A análise posterior mostrou que as partículas da superfície estão frouxamente "
            "compactadas e pouco presas umas às outras. Segundo a descrição citada pela Wikipedia, a sonda teria "
            "afundado em Bennu se não tivesse disparado os propulsores para se afastar logo depois de pegar poeira "
            "e pedras. A coleta rendeu mais do que o necessário: pedras ficaram presas na aba que deveria manter a "
            "amostra no coletor, e parte do material passou a escapar devagar para o espaço, até o coletor ser "
            "guardado na cápsula de retorno."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("101955_Bennu",
                 "101955 Bennu has a mean diameter of 490 m [...] "
                 "Analysis of the gravitational and thermal effects has given a bulk density of ρ = 1190±13 kg/m3, which is only slightly denser than water. "
                 "Therefore, the predicted macroporosity is 40±10%, suggesting the interior has a rubble pile structure or even hollows. [...] "
                 "Analysis showed that the particles making up Bennu's exterior are loosely packed and lightly bound to each other; "
                 "\"The spacecraft would have sunk into Bennu had it not fired its thrusters to back away immediately after it grabbed dust and rock from the asteroid's surface.\" [...] "
                 "The carbonaceous material that composes Bennu came from the breakup of a much larger parent body",
                 nome="101955 Bennu"),
            wiki("OSIRIS-REx",
                 "On 20 October 2020, OSIRIS-REx touched down on Bennu and successfully collected a sample. [...] "
                 "Upon surface contact by the TAGSAM instrument, a burst of nitrogen gas was released to blow regolith particles smaller than 2 cm (0.8 in) into the sampler head at the end of the robotic arm. [...] "
                 "NASA concluded that there were rocks wedged in the mylar flap meant to keep the sample inside, causing the sample to slowly escape into space. [...] "
                 "more than the 60 g (2.1 oz) needed [...] "
                 "With the collector head secure inside the SRC, pieces of the sample would no longer be lost.",
                 nome="OSIRIS-REx"),
        ],
    },
    # 7 Philae: o pouso que quicou duas vezes
    {
        "temas_secundarios": ["exploracao_espacial"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Após dez anos de viagem, o robô europeu Philae pousou num cometa em 2014, mas os arpões que deviam prendê-lo falharam. Ele quicou duas vezes e parou na sombra de um penhasco, onde só foi localizado em 2016.",
        "explicacao": (
            "Philae viajou a bordo da sonda Rosetta, da Agência Espacial Europeia, e se soltou dela para descer no "
            "cometa 67P/Churyumov-Gerasimenko dez anos e oito meses depois de sair da Terra. Como a velocidade de "
            "escape do cometa é de só 1 metro por segundo, era preciso evitar que a sonda quicasse. Por isso, ela "
            "tinha arpões para se ancorar e um propulsor para segurá-la contra o chão. Em 12 de novembro de 2014, "
            "nenhum dos dois funcionou. Philae quicou duas vezes e parou inclinado, num terreno acidentado, "
            "aparentemente à sombra de um paredão. Mesmo assim, foi o primeiro pouso suave num núcleo de cometa, e a "
            "sonda enviou dados e as primeiras imagens da superfície de um cometa por cerca de 64 horas. A bateria "
            "principal fora feita para durar umas 60 horas, e no local o sol batia só 90 minutos a cada dia do "
            "cometa, de 12,4 horas, pouco para recarregar. Entre junho e julho de 2015, Philae voltou a se comunicar "
            "de vez em quando, mas o contato se perdeu de novo. Fotos da Rosetta de 2 de setembro de 2016 "
            "o acharam deitado de lado numa fenda funda, à sombra de um penhasco. Semanas depois, a Rosetta encerrou a "
            "missão se chocando contra o mesmo cometa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Philae_(spacecraft)",
            "a robotic European Space Agency lander that accompanied the Rosetta spacecraft until it separated to land on comet 67P/Churyumov–Gerasimenko, ten years and eight months after departing Earth. "
            "On 12 November 2014, Philae touched down on the comet, but it bounced when its anchoring harpoons failed to deploy and a thruster designed to hold the probe to the surface did not fire. "
            "After bouncing off the surface twice, Philae achieved the first-ever \"soft\" (nondestructive) landing on a comet nucleus, although the lander's final, uncontrolled touchdown left it in a non-optimal location and orientation. "
            "Philae transmitted images and data back to earth for about 64 hours. "
            "Despite the landing problems, the probe's instruments obtained the first images from a comet's surface. [...] "
            "to avoid bouncing as the comet's escape velocity is only around 1 m/s [...] "
            "It sits in rough terrain, apparently in the shadow of a nearby cliff or crater wall, and is canted at an angle of around 30 degrees [...] "
            "The primary battery was designed to power the instruments for about 60 hours. [...] "
            "but the limited sunlight (90 minutes per 12.4-hour comet day) at the actual landing site was inadequate to maintain Philae's activities [...] "
            "Philae communicated sporadically with Rosetta from 13 June to 9 July 2015, but contact was then lost. [...] "
            "Its location was finally identified in photographs taken by Rosetta on 2 September 2016 as the orbiter was sent on orbits closer to the comet. "
            "The now-silent Philae was lying on its side in a deep crack in the shadow of a cliff. [...] "
            "On 30 September 2016, the Rosetta spacecraft ended its mission by crashing in the comet's Ma'at region.",
            nome="Philae (spacecraft)")],
    },
    # 8 Ann Hodges: atingida por um meteorito, e o processo que veio depois
    {
        "temas_secundarios": ["leis_julgamentos", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Em 1954, um meteorito furou o telhado de uma casa no Alabama e atingiu Ann Hodges no sofá. Depois, disputou a pedra com a dona da casa alugada e não lucrou nada. Quem lucrou foi um agricultor que achou outro pedaço.",
        "explicacao": (
            "Ann Hodges cochilava em casa, em Sylacauga, quando um fragmento de 3,86 kg atravessou o telhado, "
            "quicou num rádio e a acertou na coxa e na mão. Ficou só com um grande hematoma, e é tida como a primeira "
            "pessoa documentada a ser atingida por um meteorito e sobreviver. A pedra foi confiscada pela polícia e "
            "entregue à Força Aérea dos EUA. Enquanto ela estava na base, segundo o marido de Ann, chegaram várias "
            "ofertas, uma delas de quase 5.500 dólares, que não podiam ser aceitas. A pedra também virou disputa: a proprietária "
            "do imóvel alugado a reivindicou, por ter caído na sua propriedade. O casal Hodges fechou acordo "
            "e pagou 500 dólares a ela. Quando o meteorito voltou às mãos deles, mais de um ano depois, o interesse "
            "do público tinha passado e não apareceu comprador. Em 1956, Ann o vendeu ao museu de história natural "
            "do Alabama, contra a vontade do marido, que lembrava de um valor de uns 25 dólares. Já um agricultor da "
            "região, Julius McKinney, achou no dia seguinte à queda o segundo maior fragmento, comprado por um "
            "advogado para o Smithsonian. Com o dinheiro, a família dele comprou um carro e uma casa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Sylacauga_(meteorite)",
            "The Sylacauga meteorite fell on November 30, 1954 [...] "
            "It split into at least three fragments, with one of the fragments falling through a roof and then landing on Hodges, who was napping on her couch. [...] "
            "The meteorite left a 3-foot (91 cm) wide hole in the roof of her house, bounced off a console radio, and hit her on her upper thigh and hand, giving her a large bruise. [...] "
            "The meteorite was confiscated by the Sylacauga police chief, who then turned it over to the United States Air Force. [...] "
            "Both the Hodgeses and their landlord, Bertie Guy, claimed ownership of the rock, Guy's claim being that it had fallen on her property. "
            "The Hodgeses and Guy settled, with the Hodgeses paying $500 for the rock. "
            "However, by the time it was returned to the Hodgeses, over a year later, public attention had diminished, and they were unable to then find a buyer. "
            "The day after the fall, local farmer Julius McKinney came upon the second-largest fragment from the same meteorite. "
            "An Indianapolis-based lawyer bought it for the Smithsonian Institution. "
            "The McKinney family was able to use the money to buy a car and a house. [...] "
            "The Hodges fragment (3.86 kilograms (8.5 lb)) [...] "
            "was an American woman known for being the first documented individual to be struck by a meteorite and survive. [...] "
            "Mr. Hodges indicated they had received several offers for the meteorite while it was at the Air Force Base, but could not accept offers since it was not in their possession. "
            "One offer, he states, was close to $5,500. [...] "
            "In 1956, Mrs. Hodges decided to sell the meteorite to the Alabama Museum of Natural History, against her husband's wishes, and as he recalled, for about $25.",
            nome="Sylacauga (meteorite)")],
    },
    # 9 Shoemaker-Levy 9: o cometa despedaçado que bateu em Júpiter
    {
        "temas_secundarios": ["sistema_solar"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "Em 1994, os pedaços de um cometa despedaçado bateram em Júpiter, um após o outro, e deixaram manchas do tamanho da Terra. A cena também resolveu um enigma: as fileiras de crateras em duas luas do planeta.",
        "explicacao": (
            "O cometa Shoemaker-Levy 9 orbitava Júpiter, que provavelmente o capturou décadas antes. Em julho de 1992, "
            "passou a pouco mais de 40.000 km do topo das nuvens do planeta, dentro do limite de Roche, a distância em "
            "que as forças de maré despedaçam um corpo mantido só pela gravidade. Virou um trem de fragmentos de até "
            "2 km. Entre 16 e 22 de julho de 1994, eles caíram em Júpiter a cerca de 60 km/s, e foram registrados 21 "
            "impactos distintos. O fragmento G deixou uma mancha escura de mais de 12.000 km, quase um diâmetro da "
            "Terra. As cicatrizes ficavam mais visíveis que a Grande Mancha Vermelha e duraram meses. Foi a primeira "
            "observação direta de uma colisão entre corpos do Sistema Solar. Havia, porém, um mistério anterior. As "
            "sondas Voyager tinham fotografado 13 cadeias de crateras em Calisto e três em Ganimedes, luas de Júpiter. "
            "Na Lua, cadeias assim costumam partir de uma cratera maior, mas essas não. O Shoemaker-Levy 9 indicou a "
            "explicação: trens de fragmentos de cometas que se chocaram com as luas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Comet_Shoemaker%E2%80%93Levy_9",
            "a comet that broke apart in July 1992 and collided with Jupiter in July 1994, providing the first direct observation of an extraterrestrial collision of Solar System objects. [...] "
            "had probably been captured by Jupiter around 20 to 30 years earlier. [...] "
            "At that time, the orbit of Shoemaker–Levy 9 passed within Jupiter's Roche limit, and Jupiter's tidal forces had acted to pull the comet apart. "
            "The comet was later observed as a series of fragments ranging up to 2 km (1.2 mi) in diameter. "
            "These fragments collided with Jupiter's southern hemisphere between July 16 and 22, 1994 at a speed of approximately 60 km/s [...] "
            "The prominent scars from the impacts were more visible than the Great Red Spot and persisted for many months. [...] "
            "just over 40,000 km (25,000 mi) above its cloud tops [...] "
            "inside which tidal forces are strong enough to disrupt a body held together only by gravity. [...] "
            "Over the next six days, 21 distinct impacts were observed, with the largest coming on July 18 at 07:33 UTC when fragment G struck Jupiter. "
            "This impact created a giant dark spot over 12,000 km or 7,500 mi (almost one Earth di [...] "
            "planetary scientists identified 13 crater chains on Callisto and three on Ganymede, the origin of which was initially a mystery. "
            "Crater chains seen on the Moon often radiate from large craters, and are thought to be caused by secondary impacts of the original ejecta, but the chains on the Jovian moons did not lead back to a larger crater. "
            "The impact of SL9 strongly implied that the chains were due to trains of disrupted cometary fragments crashing into the satellites.",
            nome="Comet Shoemaker–Levy 9")],
    },
    # 10 Leônidas de 1833: a tempestade de meteoros que criou uma ciência
    {
        "temas_secundarios": ["historia_astronomia", "calendarios"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Na noite de 12 para 13 de novembro de 1833, uma estimativa contou mais de cem mil meteoros por hora na América do Norte. O espetáculo mudou a ciência dos meteoros, até então tidos como fenômenos da atmosfera.",
        "explicacao": (
            "Até então, os meteoros eram tidos como fenômenos da atmosfera. A tempestade de 1833 "
            "foi tão intensa que uma estimativa, feita quando ela já diminuía, passou de 240 mil meteoros nas nove "
            "horas do evento, a leste das Montanhas Rochosas. Houve quem visse ali o sinal da volta iminente de "
            "Cristo. Entre os povos nativos, os cheyennes firmaram um tratado de paz, o calendário lakota foi "
            "recomeçado, e muitos aniversários passaram a ser contados a partir daquela noite. O astrônomo Denison "
            "Olmsted passou semanas juntando relatos e notou que todos os meteoros pareciam partir de um mesmo ponto, "
            "na constelação de Leão, daí o nome Leônidas. Ele sugeriu que vinham de uma nuvem de partículas no "
            "espaço. Em 1866–67, dados reunidos sobre o cometa Tempel-Tuttle o apontaram como a fonte da chuva. "
            "A Terra cruza a trilha de grãos que o cometa solta quando o calor do Sol evapora seus gelos. As tempestades voltam mais ou menos a cada 33 anos. A de 1966, que "
            "passou de 40 meteoros por segundo, veio da poeira solta pelo cometa na passagem de 1899."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Leonids",
            "The Leonids ( LEE-ə-nidz) are a prolific annual meteor shower associated with the comet Tempel–Tuttle, and are also known for their spectacular meteor storms that occur about every 33 years. [...] "
            "The Leonids get their name from the location of their radiant in the constellation Leo [...] "
            "The streams consist of solid particles, known as meteoroids, normally ejected by the comet as its frozen gases evaporate under the heat of the Sun [...] "
            "the Leonids have had a major effect on the scientific study of meteors, which had previously been thought to be atmospheric phenomena. [...] "
            "it was the meteor storm of 12–13 November 1833 that broke into people's modern-day awareness. "
            "One estimate of the peak rate is over one hundred thousand meteors an hour, while another, done as the storm abated, estimated in excess of 240,000 meteors during the nine hours of the storm, over the entire region of North America east of the Rocky Mountains. "
            "The event was marked by several nations of Native Americans: the Cheyenne established a peace treaty and the Lakota calendar was reset. "
            "Many Native American birthdays were calculated by reference to the 1833 Leonid event. [...] "
            "a harbinger of the imminent second coming of Christ. [...] "
            "Denison Olmsted explained the event most accurately. "
            "After spending the last weeks of 1833 collecting information [...] "
            "the meteors radiated from a point in the constellation of Leo and he speculated the meteors had originated from a cloud of particles in space. [...] "
            "It was in 1866–67 that information on Comet Tempel-Tuttle was gathered, pointing it out as the source of the meteor shower and meteor storms. [...] "
            "The 1966 Leonid meteor storm had peak rates exceeding 40 meteors per second, or 144,000 meteors per hour. [...] "
            "the 1966 storm was from the 1899 passage of the comet.",
            nome="Leonids")],
    },
    # 11 o cinturão de asteroides é quase vazio
    {
        "temas_secundarios": ["sistema_solar", "exploracao_espacial"],
        "tipos_espanto": ["mito_desmentido", "escala_absurda"],
        "gancho": "Na imagem popular, naves desviam de pedras num cinturão de asteroides apinhado. O de verdade é quase vazio: sondas o cruzam sem incidente, e várias passaram sem fotografar um asteroide sequer.",
        "explicacao": (
            "Há centenas de milhares de asteroides conhecidos entre Marte e Júpiter, mas eles se espalham por um volume "
            "tão grande que acertar um sem mirar com cuidado seria improvável. Somados, têm uma massa estimada em "
            "apenas 3% a 4% da massa da Lua, e cerca de 60% disso está em só quatro corpos: Ceres, Vesta, Palas e "
            "Higia. Quando a Pioneer 10 se tornou a primeira sonda a entrar no cinturão, em 16 de julho de 1972, havia "
            "o medo de que os detritos a danificassem. Ela passou, e depois dela vieram a Pioneer 11, as duas Voyager "
            "e a Ulysses, que cruzaram a região sem fotografar nenhum asteroide. O cinturão também não é o que sobrou "
            "de um planeta que explodiu, ideia antiga: destruir um planeta exigiria energia demais, a massa total é "
            "pequena, e os asteroides têm químicas muito diferentes entre si. A explicação aceita é que as "
            "perturbações gravitacionais de Marte e de Júpiter impediram que os pequenos corpos dali se juntassem "
            "num planeta. As colisões ficaram violentas demais, e 99,9% da massa original da região se perdeu nos "
            "primeiros 100 milhões de anos do Sistema Solar."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Asteroid_belt",
            "Its total mass is estimated to be 3% that of the Moon, with about 60% contained in the four largest asteroids: Ceres, Vesta, Pallas, and Hygiea. [...] "
            "However, gravitational perturbations from Mars and Jupiter disrupted their accretion into a planet, imparting excess kinetic energy which shattered colliding planetesimals and most of the incipient protoplanets. "
            "As a result, 99.9% of the asteroid belt's original mass was lost in the first 100 million years of the Solar System's history. [...] "
            "The large amount of energy required to destroy a planet, combined with the belt's low combined mass, which is only about 4% of the mass of  Earth's Moon, does not support these hypotheses. "
            "Further, the significant chemical differences between the asteroids become difficult to explain if they come from the same planet. [...] "
            "Contrary to popular imagery, the asteroid belt is mostly empty. "
            "The asteroids are spread over such a large volume that reaching an asteroid without aiming carefully would be improbable. "
            "Nonetheless, hundreds of thousands of asteroids are currently known [...] "
            "The asteroid material is so thinly distributed that numerous uncrewed spacecraft have traversed it without incident. [...] "
            "The first spacecraft to traverse the asteroid belt was Pioneer 10, which entered the region on 16 July 1972. "
            "At the time, there was some concern that the debris in the belt would pose a hazard to the spacecraft, but it has since been safely traversed by multiple spacecraft without incident. "
            "Pioneer 11, Voyagers 1 and 2 and Ulysses passed through the belt without imaging any asteroids.",
            nome="Asteroid belt")],
    },
    # 12 Apophis: de 2,7% de chance de impacto a espetáculo em 2029
    {
        "temas_secundarios": ["probabilidade"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Em dezembro de 2004, o asteroide Apophis chegou a 2,7% de chance de bater na Terra em 2029, o maior alerta já dado. Hoje o choque está descartado, mas ele vai passar mais perto que muitos satélites.",
        "explicacao": (
            "Apophis foi descoberto em 19 de junho de 2004, e os primeiros cálculos da órbita indicavam uma possível "
            "colisão em 13 de abril de 2029. Com novas observações, a incerteza encolheu, mas a probabilidade subiu "
            "temporariamente, até chegar a 2,7%, "
            "ou 1 em 37, em 27 de dezembro de 2004. O asteroide recebeu nível 4 na escala de Torino, a mais alta "
            "classificação já dada a um objeto. No mesmo dia, uma imagem de março de 2004, em que ele aparecia sem "
            "ter sido notado, alongou o registro da órbita e eliminou a chance de impacto em 2029. Restaram chances "
            "pequenas para 2036 e 2068, que foram caindo com observações mais precisas. Em 2021, um impacto nos 100 "
            "anos seguintes foi descartado. Em 13 de abril de 2029, porém, ele vai passar a cerca de 32.000 km da "
            "superfície, segundo a NASA, mais perto do que muitos satélites em órbita geoestacionária, a uns 36.000 "
            "km. Deve ficar visível a olho nu em partes da Europa, da África e do oeste da Ásia, e a gravidade da "
            "Terra vai mudar a órbita dele."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://science.nasa.gov/solar-system/asteroids/apophis/",
             "titulo": "Apophis - NASA Science", "idioma": "en",
             "trecho": "Near-Earth asteroid Apophis is a potentially hazardous asteroid that will safely pass close to Earth on April 13, 2029. "
                       "It will come about 20,000 miles (32,000 kilometers) from our planet's surface — closer than the distance of many satellites in geosynchronous orbit (about 22,236 miles, or 36,000 kilometers, in altitude)."},
            wiki("99942_Apophis",
                 "early orbit calculations indicated a possible collision with Earth on 13 April 2029. "
                 "The estimated probability reached 2.7% on 27 December 2004, and Apophis was rated level 4 on the Torino scale, the highest rating attained by any object. "
                 "Later that day, the identification of a precovery image from March 2004 extended the observation arc and eliminated the possibility of a 2029 impact. "
                 "Small probabilities of impacts on later approaches, including in 2036 and 2068, remained for several years, but increasingly precise observations reduced those risks. "
                 "In 2021, Apophis was removed from the Sentry Risk Table after an impact during the following 100 years was ruled out. [...] "
                 "It is expected to reach magnitude 3.1 and become visible to the naked eye under suitable conditions from parts of Europe, Africa, and western Asia. "
                 "Earth's gravity will alter its orbit [...] "
                 "Subsequent observations decreased the uncertainty in Apophis's trajectory and the probability of an impact event in 2029 temporarily climbed, peaking at 2.7% (1 in 37) on 27 December 2004 [...] "
                 "Apophis was discovered on 19 June 2004",
                 nome="99942 Apophis"),
        ],
    },
    # 13 Halley em 1910: pílulas anticometa
    {
        "temas_secundarios": ["revolucoes_politicas", "historia_astronomia"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Em 1910, a Terra passou pela cauda do cometa Halley, onde se tinha detectado um gás tóxico. Cientistas garantiram que não havia perigo, mas gente comprou máscaras de gás e charlatães venderam \"pílulas anticometa\".",
        "explicacao": (
            "A passagem de 1910 foi a primeira do Halley registrada em fotografias e a primeira com dados de "
            "espectroscopia, a análise da luz do cometa. Entre as substâncias achadas assim na cauda estava o "
            "cianogênio, um gás tóxico. Como a Terra atravessaria a cauda em 19 de "
            "maio, jornais especularam que a vida no planeta poderia correr risco. Os cientistas explicaram que o gás "
            "não representava perigo, mas houve corrida às máscaras de gás e venda de \"pílulas anticometa\". Na "
            "China, o cometa aumentou a inquietação às vésperas da revolução que derrubaria a dinastia Qing em 1911. "
            "Curiosamente, o encontro com o Halley se repete todo ano, de forma inofensiva. Como a órbita dele passa "
            "perto da nossa em dois pontos, o cometa está associado a duas chuvas de meteoros: as Eta Aquáridas, no "
            "começo de maio, e as Oriônidas, no fim de outubro."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Halley%27s_Comet",
            "The 1910 passage was at a relative velocity of 70.56 km/s [...] "
            "It was the first approach of which photographs exist and the first for which spectroscopic data were obtained. [...] "
            "On 19 May, Earth passed through the tail of the comet. "
            "One of the substances discovered in the tail by spectroscopic analysis was the toxic gas cyanogen, which led to press speculation that life on Earth could be endangered. "
            "Despite reassurances from scientists that the gas would not present any danger, public panic buying of gas masks was recorded, and quack \"anti-comet pills\" were sold. "
            "The comet added to the unrest in China on the eve of the Xinhai Revolution, which would end the Qing dynasty in 1911. [...] "
            "Because its orbit comes close to Earth's in two places, Halley is associated with two meteor showers: the Eta Aquariids in early May, and the Orionids in late October.",
            nome="Halley's Comet")],
    },
    # 14 Murchison: grãos mais velhos que o Sol
    {
        "temas_secundarios": ["estrelas", "minerais_rochas"],
        "tipos_espanto": ["escala_absurda", "conexao_inesperada"],
        "gancho": "Um meteorito que caiu na Austrália em 1969 traz grãos de poeira mais antigos que o Sol. Os mais velhos têm cerca de 7 bilhões de anos: são o material mais antigo já achado na Terra.",
        "explicacao": (
            "O meteorito de Murchison caiu perto da cidade de mesmo nome, no estado de Victoria, em 28 de setembro de "
            "1969, depois de uma bola de fogo que se partiu em três no céu. Tem mais de 100 kg e foi visto caindo, o "
            "que o tornou um dos meteoritos mais estudados. É um condrito carbonáceo, grupo rico em compostos "
            "orgânicos, e vários estudos já identificaram nele mais de 15 aminoácidos. Em janeiro de 2020, "
            "pesquisadores relataram que grãos de carbeto de silício que ele carrega são material pré-solar, ou "
            "seja, mais antigo que o próprio Sistema Solar. Os mais antigos têm cerca de 7 bilhões de anos, uns 2,5 bilhões a mais "
            "que a Terra e o Sol, de 4,54 bilhões. Os próprios autores lembram que as estimativas de quanto tempo a "
            "poeira sobrevive no espaço dependem muito de modelos teóricos, com grandes incertezas."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Murchison_meteorite",
            "The Murchison meteorite is a meteorite that fell in Australia in 1969 near Murchison, Victoria. "
            "It belongs to  the carbonaceous chondrite class, a group of meteorites rich in organic compounds. "
            "Due to its mass (over 100 kg or 220 lb) and the fact that it was an observed fall, the Murchison meteorite is one of the most studied of all meteorites. "
            "In January 2020, cosmochemists reported that the oldest material found on Earth to date are the silicon carbide particles from the Murchison meteorite, which have been determined to be 7 billion years old, about 2.5 billion years older than the 4.54-billion-year age of the Earth and the Solar System. "
            "The published study noted that \"dust lifetime estimates mainly rely on sophisticated theoretical models. "
            "These models, however, focus on the more common small dust grains and are based on assumptions with large uncertainties.\" [...] "
            "More than 15 amino acids, some of the basic components of life, have been identified during multiple studies of this meteorite. "
            "In January 2020, astronomers reported that silicon carbide grains from the Murchison meteorite had been determined to be presolar material. [...] "
            "On 28 September 1969 at approximately 10:58 a.m. local time, near Murchison, Victoria, in Australia, a bright fireball was observed to separate into three fragments before disappearing",
            nome="Murchison meteorite")],
    },
    # 15 micrometeoritos nos telhados das cidades
    {
        "temas_secundarios": ["cidades", "minerais_rochas"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Todo ano caem na Terra cerca de 50 vezes mais micrometeoritos, em massa, do que meteoritos comuns. Desde 2016 se sabe que dá para achar esses grãos de poeira cósmica em telhados planos de cidades.",
        "explicacao": (
            "Estima-se que entrem na alta atmosfera cerca de 40 mil toneladas de poeira cósmica por ano, com margem "
            "de 20 mil para mais ou para menos. Menos de 10% disso chega ao chão em forma de partículas, o que ainda "
            "dá uns 2.700 toneladas por ano: cerca de 50 vezes a massa estimada dos meteoritos, que fica perto de 50 "
            "toneladas. Os grãos que derretem ao entrar na atmosfera viram esferas minúsculas, as esférulas cósmicas. "
            "As primeiras foram recolhidas no fundo do mar pela expedição do navio britânico Challenger, entre 1873 e "
            "1876. Por serem raros na superfície, eram buscados sobretudo na neve e no gelo polar. Em 2016, um "
            "estudo mostrou que telhados planos de áreas urbanas são bons lugares para encontrá-los, e com grãos "
            "mais recentes e menos alterados. Amadores podem procurá-los onde a poeira de uma área grande se "
            "concentra, como na saída de uma calha. O desafio é separá-los da poeira terrestre: a origem espacial é "
            "confirmada pela composição e por isótopos que só se formam no espaço."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Micrometeorite",
            "They were previously collected primarily from polar snow and ice because of their low concentrations on the Earth's surface, but in 2016 a method to extract micrometeorites in urban environments was discovered. [...] "
            "Melted micrometeorites (cosmic spherules) were first collected from deep-sea sediments during the 1873 to 1876 expedition of HMS Challenger. [...] "
            "In 2016 a new study showed that flat roofs in urban areas are fruitful places to extract micrometeorites. "
            "The \"urban\" cosmic spherules have a shorter terrestrial age and are less altered than the previous findings. "
            "Amateur collectors may find micrometeorites in areas where dust from a large area has been concentrated, such as from a roof downspout. [...] "
            "The abundances of cosmogenic manganese (53Mn) in iron spherules and of cosmogenic beryllium (10Be), aluminum (26Al), and solar neon isotope in stony MMs are extraterrestrial [...] "
            "An estimated 40,000 ± 20,000 tonnes per year (t/yr) of cosmic dust enters the upper atmosphere each year of which less than 10% (2700 ± 1400 t/yr) is estimated to reach the surface as particles. "
            "Therefore the mass of micrometeorites deposited is roughly 50 times higher than that estimated for meteorites, which represent approximately 50 t/yr",
            nome="Micrometeorite")],
    },
    # 16 asteroides com luas, e a lua feita de duas pedras grudadas
    {
        "temas_secundarios": ["exploracao_espacial", "sistema_solar"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Asteroides podem ter luas. A primeira foi achada em 1993, em fotos de uma sonda. Em 2023, outra sonda viu que a lua de um asteroide de menos de 1 km é feita de duas pedras grudadas, algo nunca visto.",
        "explicacao": (
            "A sonda Galileo, a caminho de Júpiter, passou pelo asteroide Ida em 28 de agosto de 1993. Nas imagens, "
            "uma integrante da missão, Ann Harch, achou um corpo pequeno ao lado dele: Dactyl, com só 1,4 km, cerca de "
            "um vigésimo do tamanho de Ida. Foi o primeiro satélite de asteroide confirmado. A órbita dele ajudou a "
            "estimar a densidade de Ida e a perceber que ele tem poucos metais. Trinta anos depois, em 1º de novembro "
            "de 2023, a sonda Lucy, da NASA, passou a 425 km do asteroide Dinkinesh, de uns 790 metros. Ainda antes "
            "da passagem, a sonda notou que o brilho dele não variava como o previsto, primeira pista de que havia "
            "um companheiro. As imagens mostraram uma lua, batizada de Selam, formada por dois lobos de uns 220 metros "
            "cada, encostados um no outro. Asteroides com esse formato de \"binário de contato\" são comuns no "
            "Sistema Solar, mas Selam é o primeiro exemplo conhecido de uma lua de asteroide assim. O nome Dinkinesh "
            "vem do amárico e quer dizer \"você é maravilhosa\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("243_Ida",
                 "Ida's moon Dactyl was discovered by mission member Ann Harch in images returned from Galileo. [...] "
                 "Dactyl is only 1.4 kilometres (0.87 mi) in diameter, about 1/20 the size of Ida. "
                 "Its orbit around Ida could not be determined with much accuracy, but the constraints of possible orbits allowed a rough determination of Ida's density and revealed that it is depleted of metallic minerals. [...] "
                 "On 28 August 1993, Ida was visited by the uncrewed Galileo spacecraft while en route to Jupiter. [...] "
                 "The discovery of Ida's moon Dactyl, the first confirmed satellite of an asteroid",
                 nome="243 Ida"),
            wiki("152830_Dinkinesh",
                 "the first flyby target of NASA's Lucy mission, which approached 425 km (264 mi) from the asteroid on 1 November 2023. [...] "
                 "Lucy images of Dinkinesh show that it measures approximately 790 m (2,590 ft) across its equator. [...] "
                 "During its flyby of Dinkinesh, the Lucy spacecraft discovered that the asteroid has a contact binary natural satellite or moon consisting of two conjoined lobes each around 220 m (720 ft) in diameter. [...] "
                 "to the flyby, the Lucy spacecraft found that Dinkinesh's brightness did not vary as predicted, which provided the first hints of Dinkinesh's binary nature. [...] "
                 "While contact binary asteroids are common in the Solar System, Selam is the first known example of a contact binary satellite of an asteroid. [...] "
                 "The name means \"you are wonderful\" in the Amharic language",
                 nome="152830 Dinkinesh"),
        ],
    },
]
