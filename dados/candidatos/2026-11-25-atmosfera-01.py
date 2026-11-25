LOTE = "2026-11-25-atmosfera-01"
AREA = "terra"
TEMA = "atmosfera"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Midgley: um só inventor, dois venenos do ar
    {
        "temas_secundarios": ["invencoes", "elementos_quimicos"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "O mesmo engenheiro americano criou a gasolina com chumbo e o primeiro CFC, gás que depois corroeu a camada de ozônio. Um historiador ambiental disse que ninguém prejudicou tanto a atmosfera quanto ele.",
        "explicacao": (
            "Thomas Midgley Jr., que viveu de 1889 a 1944, trabalhava num laboratório ligado à General Motors "
            "quando, em dezembro de 1921, viu que o chumbo tetraetila acabava com a \"batida\" dos motores. A "
            "empresa batizou o aditivo de \"Ethyl\" e evitou citar o chumbo na publicidade. A toxicidade era "
            "conhecida: houve mortes de operários nas fábricas, e o próprio Midgley teve intoxicação por chumbo. "
            "Mesmo assim, numa entrevista coletiva em 1924, ele lavou as mãos com o produto e inalou o vapor por "
            "60 segundos para mostrar que era seguro. No fim dos anos 1920, a Frigidaire, também da GM, queria "
            "um gás de geladeira que não fosse tóxico nem inflamável. Com Albert Henne, Midgley sintetizou o "
            "diclorodifluorometano, o primeiro clorofluorocarboneto, vendido como Freon. Os estragos dos CFCs "
            "na camada de ozônio só seriam entendidos décadas depois da morte dele. O historiador J. R. McNeill "
            "escreveu que Midgley teve mais impacto negativo sobre a atmosfera do que qualquer outro organismo "
            "na história da Terra. O fim também virou lenda: paralisado pela pólio desde 1940, ele foi achado "
            "estrangulado pelo sistema de cordas e polias que inventara para sair da cama. Costuma-se dizer que "
            "foi um acidente, mas o legista declarou suicídio."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Thomas_Midgley_Jr.",
            "Thomas Midgley Jr. (May 18, 1889 – November 2, 1944) was an American mechanical and chemical engineer. He played a major role in developing leaded gasoline (tetraethyl lead) and some of the first chlorofluorocarbons (CFCs) [...] "
            "Midgley contracted polio in 1940 and lost the use of his legs; in 1944, he was found strangled to death by a device he devised to allow him to get out of bed unassisted. It is often reported that he had been accidentally killed by his own invention, but his death was declared by the coroner to be a suicide. "
            "While the harmful effects of CFCs were not understood until decades after Midgley's death, tetraethyl lead was known to be acutely toxic by those involved in the development of leaded gasoline. [...] "
            "In December 1921, while working under the direction of Charles Kettering at Dayton Research Laboratories, a subsidiary of General Motors, he discovered (after discarding tellurium due to the difficult-to-eradicate smell) that the addition of tetraethyllead (TEL) to gasoline prevented knocking in internal combustion engines. "
            "The company named the substance \"Ethyl\", avoiding all mention of lead in reports and advertising. [...] "
            "after two deaths and several cases of lead poisoning at the TEL prototype plant in Dayton, Ohio [...] "
            "Midgley experienced lead poisoning himself [...] "
            "On October 30, 1924, Midgley participated in a press conference to demonstrate the apparent safety of TEL, in which he poured TEL over his hands, placed a bottle of the chemical under his nose, and inhaled its vapor for sixty seconds [...] "
            "In the late 1920s, air conditioning and refrigeration systems employed compounds such as ammonia [...] "
            "The Frigidaire division of General Motors, at that time a leading manufacturer of such systems, sought a non-toxic, non-flammable alternative to these refrigerants. "
            "Midgley, working with Albert Leon Henne [...] "
            "The team eventually synthesized dichlorodifluoromethane, the first chlorofluorocarbon (CFC), which they named \"Freon\". [...] "
            "In 1940, at the age of 51, Midgley contracted polio, leaving him permanently paralyzed from the legs down. He devised an elaborate system of ropes and pulleys to lift himself out of bed. [...] "
            "Environmental historian J. R. McNeill opined that Midgley \"had more adverse impact on the atmosphere than any other single organism in Earth's history\"",
            nome="Thomas Midgley Jr.")],
    },
    # 2 Rowland e Molina: a "ficção científica" que ganhou o Nobel
    {
        "temas_secundarios": ["quimica_cotidiano", "elementos_quimicos"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Em 1974, dois químicos propuseram que os CFCs de aerossóis e geladeiras subiam à estratosfera e destruíam o ozônio. O presidente do conselho da DuPont chamou a ideia de \"conto de ficção científica\". Ela rendeu um Nobel.",
        "explicacao": (
            "A pista veio de James Lovelock: num cruzeiro pelo Atlântico Sul, em 1971, ele constatou que quase "
            "todos os CFCs fabricados desde a invenção deles, em 1930, continuavam no ar. Esses gases quase não "
            "reagem perto do chão, e por isso eram considerados seguros. Frank Sherwood Rowland, professor da "
            "Universidade da Califórnia em Irvine, e seu pós-doutorando, o mexicano Mario Molina, concluíram que "
            "justamente essa estabilidade os levava intactos até a estratosfera. Lá, a luz ultravioleta os "
            "quebraria e soltaria átomos de cloro, que destroem ozônio em cadeia: em média, um único átomo de "
            "cloro reage com 100 mil moléculas de ozônio antes de sair do ciclo. O artigo saiu na revista Nature "
            "em 1974, e a dupla pediu a proibição total de novas emissões de CFCs. A indústria de aerossóis e de "
            "halocarbonetos reagiu com força. O presidente do conselho da DuPont chamou a teoria de \"conto de "
            "ficção científica\" e \"bobagem completa\", e o inventor da válvula de spray escreveu ao reitor da "
            "universidade para reclamar de Rowland. Em três anos, porém, a maior parte das premissas foi "
            "confirmada em laboratório e por observação direta da estratosfera. Rowland e Molina dividiram o "
            "Nobel de Química de 1995 com Paul Crutzen, e Molina se tornou o primeiro cientista nascido no "
            "México a receber esse prêmio."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Ozone_depletion",
                "In 1974 Frank Sherwood Rowland, Chemistry Professor at the University of California at Irvine, and his postdoctoral associate Mario J. Molina suggested that long-lived organic halogen compounds, such as CFCs, might behave in a similar fashion as Crutzen had proposed for nitrous oxide. "
                "James Lovelock had recently discovered, during a cruise in the South Atlantic in 1971, that almost all of the CFC compounds manufactured since their invention in 1930 were still present in the atmosphere. "
                "Molina and Rowland concluded that, like N2O, the CFCs would reach the stratosphere where they would be dissociated by UV light, releasing chlorine atoms. [...] "
                "The Rowland–Molina hypothesis was strongly disputed by representatives of the aerosol and halocarbon industries. "
                "The Chair of the Board of DuPont was quoted as saying that ozone depletion theory is \"a science fiction tale ... a load of rubbish ... utter nonsense\". "
                "Robert Abplanalp, the President of Precision Valve Corporation (and inventor of the first practical aerosol spray can valve), wrote to the Chancellor of UC Irvine to complain about Rowland's public statements. "
                "Nevertheless, within three years most of the basic assumptions made by Rowland and Molina were confirmed by laboratory measurements and by direct observation in the stratosphere. [...] "
                "Crutzen, Molina, and Rowland were awarded the 1995 Nobel Prize in Chemistry for their work on stratospheric ozone. [...] "
                "A single chlorine atom is able to react with an average of 100,000 ozone molecules before it is removed from the catalytic cycle.",
                nome="Ozone depletion"),
            wiki("Mario_Molina",
                "He was the first Mexican-born scientist to receive a Nobel Prize in Chemistry [...] "
                "In 1974, as a postdoctoral researcher at University of California, Irvine, Molina and F. Sherwood Rowland co-authored a paper in the journal Nature highlighting the threat of CFCs to the ozone layer [...] "
                "in which they called for a complete ban on further releases of CFCs into the atmosphe",
                nome="Mario Molina"),
        ],
    },
    # 3 o buraco de ozônio: descoberto do chão, descartado pelo software
    {
        "temas_secundarios": ["paisagens_extremas", "exploracao_espacial"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "O buraco na camada de ozônio foi revelado em 1985 por medições feitas do chão da Antártida. Satélites também viam a queda, mas os valores, baixos demais, eram marcados como erro pelo controle de qualidade dos dados.",
        "explicacao": (
            "Joseph Farman, do British Antarctic Survey, trabalhava desde 1957 na estação de Halley, na "
            "plataforma de gelo de Brunt, onde instalou instrumentos atmosféricos, entre eles um "
            "espectrofotômetro Dobson, aparelho que mede o ozônio acima do observador. No início de 1982, o "
            "instrumento, já com 25 anos, começou a registrar quedas, e em outubro daquele ano os valores "
            "desabaram. Farman e os colegas Brian Gardiner e Jon Shanklin só publicaram quando tiveram certeza de "
            "que as medidas estavam certas: o artigo saiu na Nature em maio de 1985 e chocou os cientistas, porque "
            "a perda era muito maior do que se previa. Ao mesmo tempo, as medições do satélite Nimbus 7 mostravam "
            "a destruição, mas os algoritmos de controle de qualidade as rejeitaram de início como irreais, por "
            "serem baixas demais. Quando o programa rodou de novo sem essas marcas, o buraco apareceu nos dados "
            "desde 1976. A química do fenômeno foi proposta por Susan Solomon: no frio do inverno antártico, "
            "nuvens na estratosfera convertem o cloro em formas ativas. Com o sol de setembro, o ozônio sobre o "
            "polo sul cai de cerca de 300 para até 100 unidades Dobson. Para ter uma ideia, 300 unidades "
            "equivalem a uma camada de só 3 milímetros de ozônio puro, se todo ele fosse trazido à pressão e à "
            "temperatura da superfície."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Ozone_depletion",
                "The discovery of the Antarctic \"ozone hole\" by British Antarctic Survey scientists Farman, Gardiner and Shanklin (first reported in a paper in Nature in May 1985) came as a shock to the scientific community, because the observed decline in polar ozone was far larger than had been anticipated. "
                "Satellite measurements (TOMS onboard Nimbus 7) showing massive depletion of ozone around the south pole were becoming available at the same time. "
                "However, these were initially rejected as unreasonable by data quality control algorithms (they were filtered out as errors since the values were unexpectedly low); the ozone hole was detected only in satellite data when the raw data was reprocessed following evidence of ozone depletion in in situ observations. "
                "When the software was rerun without the flags, the ozone hole was seen as far back as 1976. "
                "Susan Solomon, an atmospheric chemist at the National Oceanic and Atmospheric Administration (NOAA), proposed that chemical reactions on polar stratospheric clouds (PSCs) in the cold Antarctic stratosphere caused a massive, though localized and seasonal, increase in the amount of chlorine present in active, ozone-destroying forms.",
                nome="Ozone depletion"),
            wiki("Joseph_Farman",
                "Farman began work at the Halley research station on the Brunt Ice Shelf in Antarctica in 1957, where he deployed instruments for making atmospheric measurements including a Dobson meter, for measuring ozone. "
                "In early 1982, Farman noticed that the 25-year old instrument began to show dips in recorded ozone levels. "
                "In October 1982, the ozone values fell to remarkably low levels. "
                "Once Farman and colleagues were confident that the measurements were correct, they published their observations in the journal Nature",
                nome="Joseph Farman"),
            {"url": "https://earthobservatory.nasa.gov/features/WorldWithoutOzone",
             "titulo": "The World We Avoided by Protecting the Ozone Layer (NASA Earth Observatory)",
             "idioma": "en",
             "trecho": "British researchers stationed on the ice of Halley Bay, Antarctica, discovered the hole with ground-based measurements (red). [...] "
                       "The September sunrise over Antarctica triggers ozone-destroying reactions by these reactive kinds of chlorine, and the ozone concentration over the South Pole drops from about 300 Dobson Units to as low as 100 Dobson Units."},
            wiki("Dobson_unit",
                "A typical column amount of 300 DU of atmospheric ozone therefore would form a 3 mm layer of pure gas at the surface of the Earth if its temperature and pressure conformed to STP",
                nome="Dobson unit"),
        ],
    },
    # 4 o mundo que o Protocolo de Montreal evitou
    {
        "temas_secundarios": ["guerra_fria", "decisoes_economia"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Uma simulação da NASA recriou o mundo sem o Protocolo de Montreal: em 2065, quase dois terços do ozônio da Terra teriam sumido, e o sol do verão em Washington queimaria a pele em cinco minutos.",
        "explicacao": (
            "O Protocolo de Montreal, acordado em 16 de setembro de 1987 e em vigor desde 1º de janeiro de 1989, "
            "eliminou aos poucos os gases que destroem a camada de ozônio. Foi o primeiro tratado da história da "
            "ONU ratificado por todos: são 198 partes, 197 Estados e a União Europeia. Em 2009, uma equipe "
            "liderada por Paul Newman, do Centro Goddard da NASA, perguntou o que teria acontecido sem ele. O "
            "modelo deixou as emissões de CFCs crescerem 3% ao ano, ritmo anterior às restrições, e rodou o "
            "planeta de 1975 a 2065. Em 2020, 17% do ozônio global já teria sido destruído, com um buraco anual "
            "também sobre o Ártico. Em 2040, o \"buraco\" seria global, e o índice ultravioleta nas cidades de "
            "latitude média chegaria a 15 ao meio-dia de verão, quando hoje 10 já é extremo. Nos anos 2050 veio "
            "uma surpresa: o ozônio sobre os trópicos despencaria a quase zero em seis anos, porque a própria "
            "perda de ozônio esfriaria a estratosfera a ponto de formar ali as nuvens que hoje só existem perto "
            "dos polos. Em 2065, a queda chegaria a 67% em relação aos anos 1970. Os autores avisam que os números "
            "podem não ser exatos. No mundo real, a previsão é que a camada volte aos níveis de 1980 por volta de "
            "2040 na maior parte do planeta e de 2066 sobre a Antártida."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://earthobservatory.nasa.gov/features/WorldWithoutOzone",
             "titulo": "The World We Avoided by Protecting the Ozone Layer (NASA Earth Observatory)",
             "idioma": "en",
             "trecho": "May 13, 2009 [...] "
                       "The year is 2065. Nearly two-thirds of Earth’s ozone is gone—not just over the poles, but everywhere. [...] "
                       "The ultraviolet (UV) radiation falling on mid-latitude cities like Washington, D.C., is strong enough to cause sunburn in just five minutes. [...] "
                       "Led by Goddard scientist Paul Newman, the team used a state-of-the-art model to learn “what might have been” if chlorofluorocarbons (CFCs) and similar chemicals had not been banned [...] "
                       "The researchers let global emissions of CFCs and similar compounds in the model world increase by 3 percent per year, the rate at which they were growing before regulation in the late 1980s. "
                       "Then they let the simulated world turn from 1975 to 2065. [...] "
                       "By the simulated year 2020, 17 percent of global ozone is destroyed, and an ozone hole forms each year over the Arctic as well as the Antarctic. "
                       "By 2040, the ozone “hole”—concentrations below 220 Dobson Units—is global. "
                       "The UV index in mid-latitude cities reaches 15 around noon on a clear summer day (10 is considered extreme today). [...] "
                       "In the 2050s, something strange happens: ozone levels in the stratosphere over the tropics collapse to near zero in a span of six years. [...] "
                       "“So, by itself, loss of ozone leads to cooling, which is something we expected to see.” [...] "
                       "allowing stratospheric clouds—today confined to polar latitudes—to form over the tropics. Runaway ozone destruction followed. "
                       "By the end of the model run in 2065, global ozone drops to less than 110 DU, a 67 percent drop from the 1970s. [...] "
                       "“The quantities may not be absolutely correct, but the basic results clearly indicate what could have happened to the atmosphere."},
            wiki("Montreal_Protocol",
                "It was agreed on 16 September 1987, and was entered into force on 1 January 1989. [...] "
                "The Montreal Protocol has been ratified by 198 parties (197 states and the European Union), making it the first universally ratified treaty in United Nations history. [...] "
                "Climate projections indicate that the ozone layer will return to 1980 levels between 2040 across much of the world and 2066 over Antarctica.",
                nome="Montreal Protocol"),
        ],
    },
    # 5 os hemisférios de Magdeburgo e a cidade que renascia
    {
        "temas_secundarios": ["revolucao_cientifica", "europa_medieval"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 1654, diante do imperador, 30 cavalos não conseguiram separar duas meias-esferas de cobre das quais se tirara o ar. Quem fez a demonstração era o prefeito de Magdeburgo, cidade quase dizimada na guerra.",
        "explicacao": (
            "Otto von Guericke, cientista e prefeito de Magdeburgo, inventou uma bomba de vácuo inspirado no "
            "vácuo artificial que Evangelista Torricelli produzira poucos anos antes. Para exibi-la, mandou fazer "
            "duas meias-esferas de cobre com cerca de 50 cm de diâmetro, de bordas vedadas com graxa. Depois de "
            "retirado o ar de dentro, era a pressão da atmosfera do lado de fora que as mantinha unidas. Em 8 de "
            "maio de 1654, em Regensburg, diante da Dieta Imperial e do imperador Fernando III, duas parelhas de "
            "15 cavalos não conseguiram separá-las; bastava abrir a válvula para que se soltassem com facilidade. "
            "Com vácuo total, a força que as prendia seria de uns 20 quilonewtons, o bastante para erguer um "
            "carro. Ele repetiu o feito em Magdeburgo com 16 cavalos e, em 1663, em Berlim, com 24. Os "
            "espectadores notaram que o som não atravessava a esfera vazia, mas a luz sim. A demonstração "
            "servia também a outro propósito: mostrar a recuperação de Magdeburgo, que duas décadas antes sofrera "
            "o saque considerado a pior atrocidade da Guerra dos Trinta Anos, com 20 mil habitantes massacrados. "
            "No fim da guerra, em 1648, restavam só 4 mil. As esferas originais estão no Deutsches Museum, em "
            "Munique."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Magdeburg_hemispheres",
            "When the rims were sealed with grease and the air was pumped out, the sphere contained a vacuum and could not be pulled apart by teams of horses. "
            "Once the valve was opened, air rushed in and the hemispheres were easily separated. "
            "The Magdeburg hemispheres were invented by German scientist and mayor of Magdeburg, Otto von Guericke, to demonstrate the air pump that he had invented and the concept of atmospheric pressure. [...] "
            "Sound did not transmit through the sphere, indicating that sound needed a medium in order to travel and/or be sensed, while light did not. "
            "The first artificial vacuum had been produced a few years earlier by Evangelista Torricelli and inspired Guericke to design the world's first vacuum pump [...] "
            "The original hemispheres are on display in the Deutsches Museum in Munich. "
            "Aside from its scientific importance, the experiment served to prove the recovery of the city of Magdeburg, which only two decades earlier had undergone the  Sack of Magdeburg – considered the worst atrocity of the Thirty Years' War – when 20,000 of its inhabitants were massacred, and only 4,000 remained at the end of the war in 1648. [...] "
            "The Magdeburg hemispheres, around 50 cm (20 inches) in diameter [...] "
            "the hemispheres would have been held together with a force of around 20 kilonewtons (4,500 lbf; 2.2 short tons-force), equivalent to lifting a car or small elephant [...] "
            "Guericke's demonstration was performed on 8 May 1654 in front of the Imperial Diet, and the Emperor Ferdinand III in Regensburg. "
            "Thirty horses, in two teams of fifteen, could not separate the hemispheres until the valve was opened to equalize the air pressure. "
            "In 1656 he repeated the demonstration with sixteen horses (two teams of eight) in his hometown of Magdeburg, where he was mayor. [...] "
            "In 1663 the same demonstration was given in Berlin before Frederick William, Elector of Brandenburg with twenty-four horses.",
            nome="Magdeburg hemispheres")],
    },
    # 6 a Grande Oxidação: o oxigênio como primeira grande poluição
    {
        "temas_secundarios": ["microbiologia", "evolucao", "mudancas_climaticas"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "O oxigênio do ar começou como uma espécie de poluição: o gás liberado por cianobactérias era tóxico para a maior parte da vida de então e pode ter causado uma extinção em massa há uns 2,4 bilhões de anos.",
        "explicacao": (
            "Os geólogos chamam o episódio de Grande Evento de Oxidação, mas ele também é conhecido como "
            "Catástrofe do Oxigênio. Antes dele, a atmosfera era feita sobretudo de nitrogênio e gás carbônico, e "
            "o oxigênio livre estava em apenas 0,001% dos níveis recentes. As cianobactérias, que podem ter "
            "surgido até 3,5 bilhões de anos atrás, faziam fotossíntese e soltavam oxigênio como resíduo. Por "
            "muito tempo, porém, o gás foi consumido pelo ferro dissolvido, pelo enxofre e pelo metano, e só "
            "começou a se acumular entre 2,46 e 2,426 bilhões de anos atrás. Para os seres da época, quase todos "
            "anaeróbios, esse gás muito reativo era um veneno, capaz de oxidar moléculas orgânicas e sobretudo o "
            "material genético. Muitos organismos podem ter sido extintos, embora o evento costume ficar fora "
            "das listas das grandes extinções, porque é muito difícil contar micróbios em rochas tão antigas. O "
            "oxigênio também destruiu boa parte do metano do ar, um gás de efeito estufa forte, e o trocou por "
            "gás carbônico, mais fraco. Esse resfriamento é apontado como gatilho possível das glaciações "
            "huronianas, entre 2,45 e 2,22 bilhões de anos atrás. A crise também abriu portas: arqueias "
            "sobreviventes que se associaram a bactérias que usavam oxigênio, as futuras mitocôndrias, podem ter "
            "dado origem às células complexas."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Great_Oxidation_Event",
            "The Great Oxidation Event (GOE) or Great Oxygenation Event, also called the Oxygen Catastrophe, Oxygen Revolution, Oxygen Crisis, or Oxygen Holocaust, was a time interval during the Earth's Paleoproterozoic era when the Earth's atmosphere and shallow seas first experienced a rise in the concentration of free oxygen. "
            "This began approximately 2.46–2.426 billion years ago (Ga) [...] "
            "The appearance of highly reactive free oxygen, which can oxidize organic compounds (especially genetic materials) and thus is toxic to the then-mostly anaerobic biosphere, may have caused the extinction/extirpation of many early organisms on Earth [...] "
            "Although the event is inferred to have constituted a mass extinction, due in part to the great difficulty in surveying microscopic organisms' abundances, and in part to the extreme age of fossil remains from that time, the Great Oxidation Event is typically not counted among conventional lists of \"great extinctions\" [...] "
            "The GOE is inferred to have been caused by cyanobacteria, which evolved chlorophyll-based photosynthesis that releases dioxygen as a byproduct of water photolysis. "
            "The continually produced oxygen eventually depleted all the surface reducing capacity from ferrous iron, sulfur, hydrogen sulfide and atmospheric methane over nearly a billion years. [...] "
            "The subsequent adaptation of surviving archaea via symbiogenesis with aerobic proteobacteria (which went endosymbiont and became mitochondria) may have led to the rise of eukaryotic organisms [...] "
            "However, the bulk was likely nitrogen N2, and carbon dioxide CO2 [...] "
            "Oxygen in its O2 form, meanwhile, was present in the atmosphere at just 0.001% of recent atmospheric levels. [...] "
            "The rise in oxygen is attributed to photosynthesis by cyanobacteria, which are thought to have evolved as early as 3.5 billion years ago. [...] "
            "Oxygen likely oxidized atmospheric methane (a strong greenhouse gas) to carbon dioxide (a weaker one) and water. "
            "This weakened the greenhouse effect of the Earth's atmosphere, causing planetary cooling, which has been proposed to have triggered a series of ice ages known as the Huronian glaciation, bracketing an age range of 2.45–2.22 Ga.",
            nome="Great Oxidation Event")],
    },
    # 7 como se sabe que o ar antigo não tinha oxigênio
    {
        "temas_secundarios": ["minerais_rochas", "geologia_profunda"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "Como saber que o ar de mais de 2 bilhões de anos atrás quase não tinha oxigênio? Sedimentos dessa idade guardam grãos de pirita e uraninita, minerais que o oxigênio destrói depressa e que somem das rochas mais novas.",
        "explicacao": (
            "A pista foi seguida a partir dos anos 1970 pelo geólogo americano Preston Cloud. Ele notou que "
            "sedimentos formados por grãos desgastados e transportados, com mais de uns 2 bilhões de anos, "
            "traziam pirita, uraninita e siderita, minerais com ferro ou urânio em forma reduzida. Numa "
            "atmosfera com oxigênio, esses grãos se oxidam rapidamente, e é por isso que não aparecem em "
            "sedimentos mais jovens. Cloud também viu que, mais ou menos na mesma época, começaram a surgir as "
            "\"camadas vermelhas\" nos continentes, cuja cor vem da hematita, um óxido de ferro: era a ferrugem "
            "do planeta aparecendo. Outra testemunha são as formações ferríferas bandadas, rochas de camadas "
            "finas que alternam sílica e óxidos de ferro. Elas só se formam quando muito ferro dissolvido chega "
            "às bacias de sedimentação, e um oceano oxigenado impede isso, porque transforma o ferro em compostos "
            "insolúveis. Essas formações tiveram seu auge há cerca de 2,5 bilhões de anos e quase desaparecem do "
            "registro geológico há 1,85 bilhão de anos, o que se interpreta como o momento em que o oxigênio "
            "chegou ao fundo dos oceanos. Hoje o ar tem quase 21% de oxigênio."
        ),
        "nivel": 2, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Great_Oxidation_Event",
            "The modern atmosphere contains abundant oxygen (nearly 21%), making it an oxidizing atmosphere. [...] "
            "The scientific understanding of when and how the Earth's atmosphere changed from a weakly reducing to a strongly oxidizing atmosphere largely began with the work of the American geologist Preston Cloud in the 1970s. "
            "Cloud observed that detrital sediments older than about 2 billion years contained grains of pyrite, uraninite, and siderite, all minerals containing reduced forms of iron or uranium that are not found in younger sediments because they are rapidly oxidized in an oxidizing atmosphere. "
            "He further observed that continental red beds, which get their color from the oxidized (ferric) mineral hematite, began to appear in the geological record at about this time. "
            "Banded iron formation largely disappears from the geological record at 1.85 Ga, after peaking at about 2.5 Ga. "
            "Banded iron formation can form only when abundant dissolved ferrous iron is transported into depositional basins, and an oxygenated ocean blocks such transport by oxidizing the iron to form insoluble ferric iron compounds. "
            "The end of the deposition of banded iron formation at 1.85 Ga is therefore interpreted as marking the oxygenation of the deep ocean. [...] "
            "Banded iron formations are composed of thin alternating layers of chert (a fine-grained form of silica) and iron oxides (magnetite and hematite).",
            nome="Great Oxidation Event")],
    },
    # 8 a atmosfera que passa da Lua
    {
        "temas_secundarios": ["exploracao_espacial", "sistema_solar"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "A parte mais externa da atmosfera da Terra, uma nuvem raríssima de hidrogênio, chega a 630 mil km, quase o dobro da distância até a Lua. Os astronautas da Apollo 16 estavam dentro dela e não sabiam.",
        "explicacao": (
            "Onde a atmosfera se funde com o espaço há uma nuvem de átomos de hidrogênio, a geocorona, que brilha "
            "em ultravioleta quando recebe a luz do Sol. Como esse tipo de luz é absorvido pelo ar, ela só pode "
            "ser observada do espaço. Pesquisadores do Instituto de Pesquisa Espacial da Rússia resgataram do "
            "arquivo imagens feitas pelo instrumento SWAN, da sonda SOHO, da ESA e da NASA, em três ocasiões "
            "entre 1996 e 1998. A análise mostrou que a geocorona alcança 630 mil km, ou 50 vezes o diâmetro da "
            "Terra. \"A Lua voa através da atmosfera da Terra\", resumiu o autor principal, Igor Baliukin. É "
            "um gás finíssimo: no lado iluminado, há 70 átomos por centímetro cúbico a 60 mil km de altura e "
            "cerca de 0,2 na distância da Lua, o que aqui embaixo chamaríamos de vácuo. Em 1972, o primeiro "
            "telescópio instalado na Lua, levado pela Apollo 16, fotografou a geocorona em volta da Terra, sem "
            "que se soubesse que ela envolvia os próprios astronautas. Essa borda também vaza: a Terra perde "
            "hoje cerca de 3 kg de hidrogênio e uns 50 g de hélio por segundo para o espaço."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            {"url": "https://www.esa.int/Science_Exploration/Space_Science/Earth_s_atmosphere_stretches_out_to_the_Moon_and_beyond",
             "titulo": "Earth's atmosphere stretches out to the Moon – and beyond (ESA)",
             "idioma": "en",
             "trecho": "A recent discovery based on observations by the ESA/NASA Solar and Heliospheric Observatory, SOHO, shows that the gaseous layer that wraps around Earth reaches up to 630 000 km away, or 50 times the diameter of our planet. "
                       "“The Moon flies through Earth’s atmosphere,” says Igor Baliukin of Russia’s Space Research Institute, lead author of the paper presenting the results. [...] "
                       "Where our atmosphere merges into outer space, there is a cloud of hydrogen atoms called the geocorona. [...] "
                       "SOHO’s SWAN instrument imaged Earth and its extended atmosphere on three occasions between 1996 and 1998. "
                       "Jean-Loup and Igor’s research team in Russia decided to retrieve this data set from the archives for further analysis. [...] "
                       "The first telescope on the Moon, placed by Apollo 16 astronauts in 1972, captured an evocative image of the geocorona surrounding Earth and glowing brightly in ultraviolet light. "
                       "“At that time, the astronauts on the lunar surface did not know that they were actually embedded in the outskirts of the geocorona,” says Jean-Loup. [...] "
                       "Since this type of light is absorbed by Earth’s atmosphere, it can only be observed from space. [...] "
                       "The denser dayside region of hydrogen is still rather sparse, with just 70 atoms per cubic centimeter at 60 000 kilometers above Earth’s surface, and about 0.2 atoms at the Moon’s distance. "
                       "“On Earth we would call it vacuum"},
            wiki("Atmospheric_escape",
                "currently losing about 3 kg/s of hydrogen. The Earth additionally loses approximately 50 g/s of helium primarily through polar wind escape.",
                nome="Atmospheric escape"),
        ],
    },
    # 9 o argônio do ar saiu das rochas
    {
        "temas_secundarios": ["elementos_quimicos", "fisica_particulas", "geologia_profunda"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "Quase todo o argônio do ar, 0,934% do que respiramos, saiu das rochas: nasce do potássio radioativo da crosta. Por isso o argônio da Terra pesa mais que o potássio, inversão que intrigou os químicos.",
        "explicacao": (
            "O argônio é o terceiro gás mais abundante da atmosfera, mais de duas vezes mais comum que o vapor "
            "d'água e 23 vezes mais que o gás carbônico. Quase todo ele é argônio-40, um isótopo que não veio "
            "pronto do espaço: é produzido na crosta terrestre pelo potássio-40, um isótopo radioativo de vida "
            "longa presente no potássio natural, que ao decair se transforma em argônio. No resto do universo a "
            "história é outra. Lá predomina o argônio-36, o mais fácil de fabricar nas supernovas. Essa origem "
            "explica uma esquisitice da tabela periódica: por causa de tanto argônio-40, o peso atômico do "
            "argônio terrestre é maior que o do potássio, o elemento seguinte. Quando o gás foi descoberto, isso "
            "intrigou os químicos. Mendeleev ordenava os elementos pelo peso atômico, mas o argônio, que não "
            "reage com nada, parecia pertencer a uma posição antes do potássio, um metal alcalino muito reativo. "
            "O impasse só foi resolvido quando Henry Moseley mostrou que a tabela segue, na verdade, outra "
            "grandeza, o número atômico."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Argon",
            "Argon is the third most abundant gas in Earth's atmosphere, at 0.934% (9340 ppmv). "
            "It is more than twice as abundant as water vapor (which averages about 4000 ppmv, but varies greatly), 23 times as abundant as carbon dioxide (400 ppmv) [...] "
            "Nearly all argon in Earth's atmosphere is radiogenic argon-40, derived from the decay of potassium-40 in Earth's crust. "
            "In the universe, argon-36 is by far the most common argon isotope, as it is the most easily produced by stellar nucleosynthesis in supernovas. [...] "
            "The predominance of radiogenic 40Ar is the reason the standard atomic weight of terrestrial argon is greater than that of the next element, potassium, a fact that was puzzling when argon was discovered. "
            "Mendeleev positioned the elements on his periodic table in order of atomic weight, but the inertness of argon suggested a placement before the reactive alkali metal. "
            "Henry Moseley later solved this problem by showing that the periodic table is actual [...] "
            "Most of the argon in Earth's atmosphere was produced by electron capture of long-lived 40K (40K + e− → 40Ar + ν) present in natural potassium within Earth.",
            nome="Argon")],
    },
    # 10 a Meganeura e a dúvida sobre o oxigênio
    {
        "temas_secundarios": ["insetos", "paleontologia", "evolucao"],
        "tipos_espanto": ["misterio_aberto", "contraintuitivo"],
        "gancho": "A Meganeura, parente das libélulas com até 75 cm de envergadura, costuma ser explicada pelo excesso de oxigênio no ar do Carbonífero. Mas insetos gigantes parecidos ainda voavam depois que o oxigênio caiu.",
        "explicacao": (
            "Os fósseis da Meganeura, de cerca de 300 milhões de anos, apareceram em 1880 nas minas de carvão de "
            "Commentry, na França. Cada asa chegava a 32 cm, e a envergadura ficava entre 65 e 75 cm, muito acima "
            "da maior libélula atual. Era um predador de outros insetos. A explicação mais popular para o "
            "tamanho envolve o ar. Insetos não têm pulmões: o oxigênio chega aos tecidos por um sistema "
            "respiratório em boa parte passivo, que funciona mal em corpos grandes. No Carbonífero, o oxigênio "
            "da atmosfera subiu de níveis baixos no começo do período até picos de 25% a 30%, mais que os 21% de "
            "hoje, e isso teria permitido corpos maiores. O problema é que meganisópteros gigantes, o grupo da "
            "Meganeura, continuavam existindo no fim do Permiano, quando o oxigênio já tinha caído. Por isso há "
            "outras hipóteses, como a ausência de grandes predadores voadores na época. O sumiço desses insetos "
            "enormes pode estar ligado ao surgimento de vertebrados voadores, como os pterossauros. A discussão "
            "segue aberta."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Meganeura",
                "is a genus of extinct insects from the Late Carboniferous (about 300 million years ago). [...] "
                "Fossils of Meganeura were first discovered in Late Carboniferous (Stephanian) Coal Measures of Commentry, France, in 1880. [...] "
                "With single wing length reaching 32 centimetres (13 in), a wingspan around 65–75 cm (2.13–2.46 ft) [...] "
                "is considerably larger than the biggest modern dragonfly [...] "
                "Like other odonatopterans, meganeurids such as Meganeura were predatory, with their diet mainly consisting of other insects. [...] "
                "as insects’ largely passive respiratory system diffuses oxygen to their tissues with difficulty at large body sizes. "
                "Much debate exists regarding how Meganeura attained such a large body size, with hypotheses ranging from a correlation with the high oxygen content of the Late Carboniferous (though this is contradicted by the presence of giant meganisopterans in the Late Permian, after oxygen levels had dropped) to the absence of other big aerial predators. "
                "The extinction of meganisopterans as a whole and the absence of similarly large flying insects may correlate with the evolution of flying tetrapods such as pterosaurs.",
                nome="Meganeura"),
            wiki("Carboniferous",
                "Atmospheric oxygen levels, originally thought to be consistently higher than today throughout the Carboniferous, have been shown to be more variable, increasing from low levels at the beginning of the Period to highs of 25–30%.",
                nome="Carboniferous"),
            wiki("Great_Oxidation_Event",
                "The modern atmosphere contains abundant oxygen (nearly 21%)",
                nome="Great Oxidation Event"),
        ],
    },
    # 11 Glaisher e Coxwell: o voo mais alto e o piloto esquecido
    {
        "temas_secundarios": ["transportes", "limites_humanos", "clima_tempo"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Em 1862, um meteorologista inglês subiu de balão para medir o ar e desmaiou a uns 8.800 m. O piloto, sem sentir as mãos, subiu no cordame e abriu a válvula. Um filme de 2019 trocou o piloto por uma personagem fictícia.",
        "explicacao": (
            "James Glaisher, meteorologista do Observatório Real de Greenwich, fez muitas subidas de balão entre "
            "1862 e 1866, quase sempre com Henry Coxwell como piloto, para medir a temperatura e a umidade do ar "
            "nas maiores altitudes que se conseguia alcançar. Na subida de 5 de setembro de 1862, os dois "
            "bateram o recorde mundial de altitude, mas Glaisher perdeu a consciência por volta de 8.800 metros, "
            "antes de conseguir fazer uma leitura. As estimativas indicam que o balão passou de 9.500 metros e "
            "talvez tenha chegado a 10.900. Coxwell perdeu toda a sensibilidade das mãos, e a corda da válvula "
            "tinha se enroscado. Com muito esforço, ele subiu no cordame e conseguiu abrir a saída de gás, e o "
            "balão desceu para altitudes mais seguras. Um dos pombos levados na viagem morreu. O episódio "
            "inspirou o filme \"The Aeronauts\", de 2019, que trocou Coxwell por uma piloto fictícia. O chefe da "
            "biblioteca da Royal Society lamentou a omissão, lembrando que Coxwell salvou a vida de um cientista "
            "importante."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("James_Glaisher",
            "was an English meteorologist, aeronaut and astronomer. [...] "
            "before moving to the Royal Observatory, Greenwich, where he served as Superintendent of the Department of Meteorology and Magnetism at Greenwich for 34 years. [...] "
            "Between 1862 and 1866, usually with Henry Tracey Coxwell as his co-pilot, Glaisher made numerous ascents to measure the temperature and humidity of the atmosphere at the greatest altitudes attainable at that time. "
            "Their ascent on 5 September 1862 broke the world record for altitude but he passed out around 8,800 metres (28,900 feet) before a reading could be taken. "
            "One of the pigeons making the trip with him died. "
            "Estimates suggest that he rose to more than 9,500 metres (31,200 feet) and as much as 10,900 metres (35,800 feet) above sea level. "
            "Glaisher lost consciousness during the ascent and Coxwell lost all sensation in his hands. "
            "The valve-line had become entangled so he was unable to release the mechanism; with great effort, he climbed onto the rigging and was finally able to release the vent before losing consciousness. "
            "This allowed the balloon to descend to a lower altitude. [...] "
            "ed in 2019, includes a fictionalised account of the 5 September 1862 flight. [...] "
            "The film omits Henry Coxwell entirely with Wren becoming the pilot. "
            "A report in The Daily Telegraph quotes Keith Moore, Head of Library at the Royal Society as saying: \"It’s a great shame that Henry isn’t portrayed because he performed very well and saved the life of a leading scientist\".",
            nome="James Glaisher")],
    },
    # 12 Oishi: a corrente de jato descoberta em esperanto
    {
        "temas_secundarios": ["linguas_construidas", "clima_tempo", "segunda_guerra"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "A corrente de jato foi detectada nos anos 1920 por um meteorologista japonês que publicou seus relatórios em esperanto. Fora do Japão, quase ninguém percebeu, e o crédito muitas vezes vai para um aviador americano.",
        "explicacao": (
            "Wasaburo Oishi, que viveu de 1874 a 1950, dirigia o observatório aerológico de Tateno, perto do "
            "monte Fuji. Ele soltava balões-piloto e acompanhava a subida deles para medir a velocidade e a "
            "direção do vento em altitude. O primeiro relatório oficial do observatório, de 1926, foi escrito em "
            "esperanto. Ao separar os dados por estação, o perfil de inverno trouxe a primeira evidência conhecida "
            "dos ventos de oeste fortes e persistentes sobre o Japão que depois seriam chamados de corrente de "
            "jato. Oishi era também um esperantista importante: presidiu o Instituto Japonês de Esperanto de 1930 "
            "a 1945. Tentando alcançar um público estrangeiro que não respondia, publicou 19 relatórios entre "
            "1926 e 1944, somando 1.246 páginas, todos na língua inventada. O trabalho passou quase despercebido "
            "fora do país, embora, pela cronologia, a descoberta seja dele. O americano Wiley Post, o primeiro a "
            "dar a volta ao mundo voando sozinho, costuma receber parte do crédito: com um traje pressurizado que "
            "ele mesmo inventou, voou alto e notou que às vezes avançava em relação ao chão muito mais rápido do "
            "que pelo ar. Na Segunda Guerra, os estudos de Oishi ajudaram o Japão a lançar balões incendiários "
            "rumo à América do Norte."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Wasaburo_Oishi",
                "(大石 和三郎, Ōishi Wasaburō; 15 March 1874 – 18 December 1950) was a Japanese meteorologist. [...] "
                "He was also an important Esperantist, serving as the second board president of the Japanese Esperanto Institute from 1930 to 1945. [...] "
                "He wrote the first official report from Japan's Aerological Observatory (written in 1926 and in the auxiliary language of Esperanto). "
                "In this report (Raporto de Aerologia Observatorio de Tateno) data was stratified by season and used to produce the mean seasonal wind profiles. "
                "The profile for winter gave the first known evidence of the persistent strong westerlies over Japan that would later become known as the jet stream. "
                "In an attempt to reach an unresponsive foreign audience, Wasaburo Oishi published nineteen reports between 1926 and 1944, all of them written in Esperanto, in total 1246 pages. "
                "Wasaburo Oishi was not only the director of Japan's Tateno atmospheric observatory [...] "
                "Oishi's studies on the jet stream enabled Japan to attack North America during World War II with at least 9,000 incendiary bombs carried by stratospheric balloons",
                nome="Wasaburo Oishi"),
            wiki("Jet_stream",
                "In the 1920s Japanese meteorologist Wasaburo Oishi detected the jet stream from a site near Mount Fuji. "
                "He tracked pilot balloons (\"pibals\"), used to measure wind speed and direction, as they rose in the air. "
                "Oishi's work largely went unnoticed outside Japan because it was published in Esperanto, though chronologically he has to be credited for the scientific discovery of jet streams. "
                "American pilot Wiley Post (1898–1935), the first man to fly around the world solo in 1933, is often given some credit for discovery of jet streams. "
                "Post invented a pressurized suit that let him fly above 6,200 metres (20,300 ft). "
                "In the year before his death, Post made several attempts at a high-altitude transcontinental flight and noticed that at times his ground speed greatly exceeded his air speed.",
                nome="Jet stream"),
        ],
    },
    # 13 nuvens noctilucentes: as mais altas, e só no verão
    {
        "temas_secundarios": ["clima_tempo", "vulcoes_terremotos", "exploracao_espacial"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "As nuvens mais altas da Terra, a uns 80 km, aparecem no verão porque é nessa estação que aquela camada do ar fica mais fria, abaixo de −120 °C. Não há registro confirmado delas antes de 1885.",
        "explicacao": (
            "São as nuvens noctilucentes, \"que brilham à noite\", feitas de cristais de gelo de até 100 "
            "nanômetros, entre 76 e 85 km de altura, acima de qualquer outra nuvem. Só dá para vê-las no "
            "crepúsculo, quando o observador e as camadas baixas do ar já estão na sombra da Terra, mas elas, "
            "lá no alto, ainda recebem sol. Essa região, a mesosfera, é extremamente seca: tem cerca de um "
            "centésimo de milionésimo da umidade do ar do Saara. Por isso o gelo só se forma abaixo de uns "
            "−120 °C. E, ao contrário da intuição, ela é mais fria no verão: nessa estação, ventos verticais "
            "fazem o ar subir e se expandir, e o ar que se expande esfria. As primeiras observações conhecidas "
            "são de 1885, dois anos depois da erupção do Krakatoa. Na época se pensou que fossem cinzas do "
            "vulcão, mas as nuvens continuaram depois que as cinzas assentaram. Até hoje não se sabe se a erupção "
            "teve algo a ver com elas ou se apenas mais gente passou a olhar para o céu, atraída pelos pores do "
            "sol espetaculares. A exaustão dos ônibus espaciais, quase só vapor d'água, chegou a criar pequenas "
            "nuvens desse tipo, e estudos recentes sugerem que o aumento do metano no ar também as reforça."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Noctilucent_cloud",
            "Noctilucent roughly means \"night shining\" in Latin. [...] "
            "Too faint to be seen in daylight, they are visible only when the observer and the lower layers of the atmosphere are in Earth's shadow while these very high clouds are still in sunlight. "
            "Recent studies suggest that increased atmospheric methane emissions produce additional water vapour through chemical reactions once the methane molecules reach the mesosphere [...] creating, or reinforcing existing, noctilucent clouds. [...] "
            "No confirmed record of their observation exists before 1885 [...] "
            "Noctilucent clouds are composed of tiny crystals of water ice up to 100 nm in diameter and exist at a height of about 76 to 85 km (249,000 to 279,000 ft), higher than any other clouds in Earth's atmosphere. [...] "
            "The exhaust from Space Shuttles, in use between 1981 and 2011, which was almost entirely water vapour after the detachment of the Solid Rocket Booster at a height of about 46 km (151,000 ft), was found to generate minuscule individual clouds. [...] "
            "As the mesosphere contains very little moisture, approximately one hundred millionth that of air from the Sahara, and is extremely thin, the ice crystals can form only at temperatures below about −120 °C (−184 °F). "
            "This means that noctilucent clouds form predominantly during summer when, counterintuitively, the mesosphere is coldest as a result of seasonally varying vertical winds, leading to cold summertime conditions in the upper mesosphere (upwelling, resulting in adiabatic cooling) [...] "
            "Noctilucent clouds are first known to have been observed in 1885, two years after the 1883 eruption of Krakatoa. "
            "It remains unclear whether their appearance had anything to do with the volcanic eruption or whether their discovery was due to more people observing the spectacular sunsets caused by the volcanic debris in the atmosphere. [...] "
            "Scientists at the time assumed the clouds were another manifestation of volcanic ash, but after the ash had settled out of the atmosphere, the noctilucent clouds persisted.",
            nome="Noctilucent cloud")],
    },
    # 14 termosfera: 2.000 °C e frio
    {
        "temas_secundarios": ["termodinamica", "exploracao_espacial", "acustica"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Na camada da atmosfera onde orbita a Estação Espacial, o gás pode passar de 2.000 °C. Mesmo assim, um termômetro comum ali marcaria bem abaixo de zero à noite, e acima de 160 km nem o som consegue se propagar.",
        "explicacao": (
            "É a termosfera, que começa por volta de 80 km de altitude. O nome vem do grego para \"calor\", e "
            "faz sentido: o gás dali absorve a radiação solar mais energética, e a temperatura sobe com a altura, "
            "chegando a 2.000 °C ou mais conforme a atividade do Sol, e a 2.500 °C perto do topo. Mas temperatura "
            "é só a medida da agitação das moléculas, e lá elas são pouquíssimas, quase um vácuo. Não há "
            "colisões suficientes para passar calor a um objeto. Um termômetro comum perderia mais energia "
            "irradiando do que ganharia em contato com o gás, e por isso marcaria bem abaixo de 0 °C à noite. "
            "Acima de 160 km, as moléculas se encontram tão raramente que o som não se transmite. Nessa "
            "altitude, os gases deixam até de se misturar e se separam em camadas de acordo com a massa das "
            "moléculas. A radiação também carrega eletricamente as partículas, e por isso essa camada reflete "
            "ondas de rádio para além do horizonte. Pelo critério da linha de Kármán, a 100 km, quase toda a "
            "termosfera já conta como espaço. Mesmo assim, ela abriga as únicas casas humanas fora do chão: a "
            "Estação Espacial Internacional e a estação chinesa Tiangong orbitam dentro dela."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Thermosphere",
            "Taking its name from the Greek θερμός (pronounced thermos) meaning heat, the thermosphere begins at about 80 kilometres (50 miles) above sea level. "
            "At these high altitudes, the residual atmospheric gases sort into strata according to molecular mass (see turbosphere). "
            "Thermospheric temperatures increase with altitude due to absorption of highly energetic solar radiation. "
            "Temperatures are highly dependent on solar activity, and can rise to 2,000 °C (3,630 °F) or more. "
            "Radiation causes the atmospheric particles in this layer to become electrically charged, enabling radio waves to be refracted and thus be received beyond the horizon. [...] "
            "by the judging criteria set for the definition of the Kármán line 100 km (62 mi), most of the thermosphere is part of outer space. [...] "
            "The highly attenuated gas in this layer can reach 2,500 °C (4,530 °F). "
            "Despite the high temperature, an observer or object will experience low temperatures in the thermosphere, because the extremely low density of the gas (practically a hard vacuum) is insufficient for the molecules to conduct heat. "
            "A normal thermometer will read significantly below 0 °C (32 °F) at night because the energy lost by thermal radiation would exceed the energy acquired from the atmospheric gas by direct contact. "
            "In the anacoustic zone above 160 kilometres (99 mi), the density is so low that molecular interactions are too infrequent to permit the transmission of sound. [...] "
            "The thermosphere is uninhabited with the exception of the International Space Station, which orbits the Earth within the middle of the thermosphere between 408 and 410 kilometres (254 and 255 mi) and the Tiangong space station",
            nome="Thermosphere")],
    },
    # 15 Scheele: o oxigênio parado na gráfica
    {
        "temas_secundarios": ["elementos_quimicos", "revolucao_cientifica", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Um farmacêutico da Suécia isolou o oxigênio por volta de 1771, antes de Priestley e de Lavoisier, e o chamou de \"ar de fogo\". Mas seu livro ficou parado na gráfica de 1775 a 1777, e os dois rivais publicaram antes.",
        "explicacao": (
            "Carl Wilhelm Scheele, químico e farmacêutico alemão-sueco, trabalhava sem os equipamentos caros de "
            "um Lavoisier e mesmo assim acumulou descobertas. Na época, reinava a teoria do flogisto, uma "
            "\"matéria do fogo\" que seria liberada por tudo o que queima. Estudando o ar, que se considerava "
            "um elemento só, Scheele concluiu que ele era uma mistura de dois gases: o \"ar de fogo\", que "
            "alimentava a combustão, e o \"ar viciado\". Obteve o mesmo gás aquecendo várias substâncias, como "
            "salitre, dióxido de manganês e óxido de mercúrio. Ele escreveu sobre os resultados a Lavoisier, que "
            "percebeu a importância deles. O livro de Scheele, \"Tratado químico do ar e do fogo\", foi entregue "
            "ao impressor em 1775, mas só saiu em 1777, quando Joseph Priestley e Antoine Lavoisier já tinham "
            "publicado seus dados. Por isso o crédito pelo oxigênio costuma ser dividido entre os três. Scheele "
            "nunca abandonou a teoria do flogisto, e coube a Lavoisier dar ao gás o nome de oxigênio. A lista "
            "de feitos dele inclui ainda o cloro e o tungstênio. Como muitos químicos do seu tempo, cheirava e "
            "provava as substâncias novas, e os médicos atribuíram sua morte, em 1786, ao envenenamento por "
            "mercúrio."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Carl_Wilhelm_Scheele",
            "Carl Wilhelm Scheele (German: [ˈʃeːlə], Swedish: [ˈɧêːlɛ]; 9 December 1742 – 21 May 1786) was a German-Swedish pharmaceutical chemist. [...] "
            "Scheele discovered oxygen (although Joseph Priestley published his findings first), and identified the elements molybdenum, tungsten, barium, nitrogen, and chlorine, among others. [...] "
            "Doctors said that he died of mercury poisoning, having spent his life working as a chemist. [...] "
            "When Scheele discovered oxygen he called it \"fire air\" as it supported combustion. [...] "
            "Air was thought to be an element that made up the environment in which chemical reactions took place but did not interfere with the reactions. "
            "Scheele's investigation of air enabled him to conclude that air was a mixture of \"fire air\" and \"foul air\"; in other words, a mixture of two gases. "
            "Scheele performed numerous experiments in which he heated substances such as saltpetre (potassium nitrate), manganese dioxide, heavy metal nitrates, silver carbonate and mercuric oxide. "
            "In all of these experiments, he isolated the same gas [...] "
            "However, his first publication, Chemische Abhandlung von der Luft und dem Feuer, was delivered to the printer Swederus in 1775, but not published until 1777, at which time both Joseph Priestley and Antoine Lavoisier had already published their experimental data and conclusions concerning oxygen and the phlogiston theory. "
            "Scheele was credited for finding oxygen with two other people, Joseph Priestley and Antoine Lavoisier. [...] "
            "Scheele achieved prolific and important results without the expensive laboratory equipment to which his Parisian contemporary Antoine Lavoisier was accustomed. [...] "
            "Although Scheele was unable to grasp the significance of his discovery of the substance that Lavoisier later named oxygen [...] "
            "Scheele would smell and taste any new substances he discovered. [...] "
            "Scheele wrote about his findings to Lavoisier who was able to see the significance of the results. "
            "His discovery of oxygen (ca. 1771) was chronologically earlier than the corresponding work of Priestley and Lavoisier, but he did not publish this discovery until 1777, after both of his rivals had published. "
            "Although Scheele would always believe in some form of the phlogiston theory",
            nome="Carl Wilhelm Scheele")],
    },
    # 16 a Amazônia não é o pulmão do mundo
    {
        "temas_secundarios": ["amazonia", "ecologia", "plantas"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "A Amazônia não fornece 20% do oxigênio do mundo. Ela produz muito, mas as próprias árvores e os micróbios da floresta consomem quase tudo de volta: a contribuição líquida dela para o ar fica perto de zero.",
        "explicacao": (
            "A floresta faz fotossíntese, mas também respira. Segundo a equipe do ecólogo Yadvinder Malhi, da "
            "Universidade de Oxford, as árvores consomem pouco mais da metade do oxigênio que produzem, "
            "sobretudo à noite, quando não há luz. O resto é usado pelos incontáveis micróbios que decompõem a "
            "matéria morta. O saldo de oxigênio da Amazônia, como o de qualquer outro bioma, gira em torno de "
            "zero. A conta bruta também não chega a 20%: pelas estimativas de Malhi, a Amazônia gera uns 16% do "
            "oxigênio produzido em terra firme e uns 9% quando se inclui o fitoplâncton dos oceanos. Há ainda um "
            "argumento físico: cada molécula de gás carbônico absorvida devolve mais ou menos uma de oxigênio, e "
            "o ar tem menos de 0,5% de gás carbônico contra 21% de oxigênio. Não daria para uma floresta fabricar "
            "uma fatia tão grande. O oxigênio que respiramos é herança de bilhões de anos, acumulada porque parte "
            "do plâncton morto foi enterrada no fundo do mar antes de apodrecer. Ninguém sabe ao certo de onde "
            "veio o mito. Uma hipótese é a confusão com a fatia da Amazônia no oxigênio produzido pela "
            "fotossíntese em terra. Isso não diminui a floresta: ela tira muito carbono do ar, ajuda a regular "
            "as chuvas da América do Sul e é o ecossistema terrestre mais biodiverso."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.nationalgeographic.com/environment/article/why-amazon-doesnt-produce-20-percent-worlds-oxygen",
             "titulo": "Why the Amazon doesn't really produce 20% of the world's oxygen (National Geographic)",
             "idioma": "en",
             "trecho": "The Amazon rainforest is often called the “lungs of the Earth” and credited with producing some 20 percent of the world’s oxygen. "
                       "But that’s often a repeated, yet misleading claim. In fact, it’s a gross overestimate. "
                       "The Amazon’s net contribution to the oxygen we breathe likely hovers around zero. [...] "
                       "For every batch of carbon dioxide molecules trees pull out of the air, they push a comparable number of oxygen molecules back out. "
                       "Given that the atmosphere contains less than half a percent of carbon dioxide, but 21 percent oxygen, it’s not possible for the Amazon to generate that much oxygen. [...] "
                       "Yadvinder Malhi, an ecosystem ecologist at Oxford University’s Environmental Change Institute [...] "
                       "That would mean the Amazon generates around 16 percent of oxygen produced on land, explains Malhi. "
                       "That percentage sinks to 9 percent when taking into account the oxygen produced by phytoplankton in the ocean. [...] "
                       "During the night when there’s no sun around for photosynthesis, they’re net absorbers of oxygen. [...] "
                       "Malhi’s research team reckons that trees inhale a little over half the oxygen they produce this way. "
                       "The rest is probably used up by the countless microbes that live in the Amazon, which inhale oxygen to break down dead organic matter of the forest. "
                       "“The net [oxygen] effect of the Amazon, or really any other biome, is around zero,” he explains. [...] "
                       "The oxygen we breathe is the legacy of phytoplankton in the ocean that have over billions of years steadily accumulated oxygen that made the atmosphere breathable [...] "
                       "This oxygen could only accumulate because the plankton became trapped at the bottom of the ocean before they could rot. [...] "
                       "Nevertheless, the 20 percent myth has been making the rounds for decades, though it’s unclear where it originated. "
                       "Malhi and Coe reckon it stems from the fact that the Amazon contributes around 20 percent of the oxygen produced by photosynthesis on land [...] "
                       "In its pristine state, it makes a significant contribution to pulling tons of carbon dioxide out of the atmosphere. [...] "
                       "The Amazon also plays an important role in stabilizing rainfall cycles in South America [...] "
                       "the Amazon is the most biodiverse ecosystem on land"},
            wiki("Amazon_rainforest",
                "Though often referenced as producing more than a quarter of the Earth's oxygen, this often stated, but misused statistic actually refers to oxygen turnover. "
                "The net contribution of the ecosystem is approximately zero.",
                nome="Amazon rainforest"),
        ],
    },
]
