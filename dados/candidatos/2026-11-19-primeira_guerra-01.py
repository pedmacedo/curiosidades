LOTE = "2026-11-19-primeira_guerra-01"
AREA = "historia_moderna"
TEMA = "primeira_guerra"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o Canhão de Paris e a rotação da Terra
    {
        "temas_secundarios": ["atmosfera", "invencoes"],
        "tipos_espanto": ["escala_absurda", "engenhosidade"],
        "gancho": "Em 1918, um canhão alemão bombardeou Paris a 120 km de distância. Os projéteis subiam a mais de 40 km de altura, e os parisienses, sem ouvir avião nem tiro, acharam que eram bombas de um zepelim.",
        "explicacao": (
            "Era o Canhão de Paris, usado de março a agosto de 1918. O projétil, de 106 kg, chegava a uma altitude "
            "máxima de 42,3 km, um recorde para objetos feitos por humanos que só caiu com o primeiro voo bem-"
            "sucedido do foguete V-2, em 1942. Cada tiro levava 182 segundos de voo. Lá em cima, o ar rarefeito "
            "freava pouco o projétil, e era isso que permitia o alcance enorme. A distância era tanta que os "
            "artilheiros precisavam levar em conta a rotação da Terra, o efeito Coriolis, nos cálculos. Havia "
            "outro problema: cada disparo arrancava aço do interior do cano. Por isso, os projéteis eram numerados "
            "em ordem crescente de diâmetro e tinham de ser disparados nessa sequência, sob o risco de um deles "
            "entalar e o canhão explodir. Depois de 65 tiros, o cano voltava à fábrica Krupp para ser alargado. "
            "Como arma, foi pouco eficaz: a carga explosiva era pequena e a pontaria só servia para alvos do "
            "tamanho de uma cidade. O objetivo alemão era abalar o moral. No primeiro dia, quinze pessoas morreram, e "
            "em poucos dias se formaram filas de milhares de pessoas nas estações para deixar Paris."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Paris_Gun",
            "They were in service from March to August 1918. When the guns were first employed, Parisians believed they had been bombed by a high-altitude Zeppelin, because the sound of neither an airplane nor a gun could be heard. [...] "
            "As military weapons, the Paris Guns were not a great success: the payload was small, the barrel required frequent replacement, and the guns' accuracy was good enough for only city-sized targets. "
            "The German objective was to build a psychological weapon to attack the morale of the Parisians, not to destroy the city itself. [...] "
            "The gun was capable of firing a 106-kilogram (234 lb) shell to a range of 130 kilometres (81 mi) and a maximum altitude of 42.3 km (26.3 mi)—the greatest height reached by a human-made projectile until the first successful V-2 flight test in October 1942. "
            "At the start of its 182-second flight [...] "
            "The distance was so far that the Coriolis effect—the rotation of the Earth—was substantial enough to affect trajectory calculations. [...] "
            "climbing to an altitude of 40 km (25 mi) at the top of its trajectory. [...] "
            "This reduced drag from air resistance, allowing the shell to achieve a range of over 130 kilometres (81 mi). [...] "
            "The shells were propelled at such a high velocity that each successive shot wore away a considerable amount of steel from the rifled bore. "
            "Each shell was sequentially numbered according to its increasing diameter, and had to be fired in numeric order, lest the projectile lodge in the bore and the gun explode. [...] "
            "After 65 rounds had been fired, each of progressively larger caliber to allow for wear, the barrel was sent back to Krupp and rebored with a new set of shells. [...] "
            "The Paris gun was used to shell Paris at a range of 120 km (75 mi). [...] "
            "On the first day, fifteen people were killed and thirty-six wounded. "
            "The effect on morale in Paris was immediate: by 27 March, queues of thousands had started at the Gare d'Orsay",
            nome="Paris Gun")],
    },
    # 2 as minas de Messines e a que explodiu com um raio em 1955
    {
        "temas_secundarios": ["geologia_profunda", "grandes_obras"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "Em 1917, minas cavadas por britânicos sob as linhas alemãs na Bélgica explodiram quase juntas e abriram 19 crateras; relatos dizem que se ouviu em Londres. Uma mina que sobrou foi detonada por um raio em 1955.",
        "explicacao": (
            "Por quase dois anos, companhias de túneis britânicas, canadenses e australianas cavaram galerias numa "
            "camada de argila azul, a 24–37 metros de profundidade, até ficarem sob as posições alemãs na serra de "
            "Messines. Um geólogo militar, Edgeworth David, ajudou a planejar o sistema. Os alemães cavavam contra-"
            "minas e chegaram a poucos metros de algumas câmaras. Em abril de 1917, o oficial que comandava as "
            "escavações alemãs chegou a relatar que um ataque com grandes minas já não era possível; em maio, mudou "
            "de ideia, mas o alerta não levou à retirada. Às 3h10 de 7 de junho, as cargas, com 454 toneladas de "
            "explosivos, foram detonadas no intervalo de 20 segundos. Na véspera, um general britânico disse à "
            "imprensa que talvez não fizessem história, mas certamente mudariam a geografia. O tremor foi tomado por "
            "terremoto no departamento de geologia da universidade de Lille. O número de mortos, divulgado muitas "
            "vezes como 10 mil, foi contestado pelo historiador Simon Jones, que estima no máximo 500 alemães mortos "
            "pelas minas e 7.344 feitos prisioneiros. Nem todas as minas explodiram: em 17 de julho de 1955, um raio "
            "detonou uma delas e matou só uma vaca. Acredita-se que outra esteja sob uma casa de fazenda, e ninguém "
            "tentou removê-la."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Mines_in_the_Battle_of_Messines_(1917)",
                "The mines, secretly planted and maintained by tunnelling companies of the Royal Engineers beneath the German front position, killed many German soldiers and created 19 large craters. [...] "
                "To overcome the technical difficulties, two military geologists assisted the miners from March, including Edgeworth David, who planned the system of mines. [...] "
                "the 1st Canadian, 3rd Canadian and 1st Australian Tunnelling companies [...] "
                "Sappers dug the tunnels into a layer of blue clay 24–37 m (80–120 ft) below the surface [...] "
                "German tunnellers came within metres of several British mine chambers [...] "
                "that were charged with 454 t (447 long tons) of ammonal and gun cotton. [...] "
                "The evening before the attack, Harington, the Second Army Chief of Staff, remarked to the press, \"Gentlemen, we may not make history tomorrow, but we shall certainly change the geography\". [...] "
                "A subterranean attack by mine-explosions on a large scale beneath the front line to precede an infantry assault against the Messines Ridge was no longer possible. [...] "
                "Soon after the conference, Füßlein changed his mind and on 10 May, reported to the 4th Army his suspicions that the British had prepared several deep mines [...] "
                "Starting from 3:10 a.m. on 7 June, the mines at Messines were fired within the space of 20 seconds. [...] "
                "Reports suggested that the sound was heard in London and Dublin; at the Lille University geology department, the shock wave was mistaken for an earthquake. [...] "
                "the historian, Simon Jones, challenged the death toll of the mines using primary sources and suggested that the mine explosions killed no more than 500 German troops and that 7,344 were taken prisoner.",
                nome="Mines in the Battle of Messines (1917)"),
            wiki("Mining_(military)",
                "The near simultaneous explosions created 19 large craters and ranks among the largest non-nuclear explosions of all time. "
                "Two mines were not ignited in 1917 because they had been abandoned before the battle, and four were outside the area of the offensive. "
                "On 17 July 1955, a lightning strike set off one of these four latter mines. There were no human casualties, but one cow was killed. "
                "Another of the unused mines is believed to have been found in a location beneath a farmhouse, but no attempt has been made to remove it.",
                nome="Mining (military)"),
        ],
    },
    # 3 a colheita de ferro e a zona vermelha
    {
        "temas_secundarios": ["quimica_cotidiano", "ecologia"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Agricultores da França e da Bélgica ainda desenterram, todo ano, granadas da Primeira Guerra ao arar a terra. Só o serviço francês recolhe cerca de 900 toneladas por ano, e limpar tudo pode levar séculos.",
        "explicacao": (
            "Estima-se que 1,5 bilhão de projéteis de artilharia foram disparados na frente ocidental, e até um em "
            "cada quatro não explodiu. Muitos se enterraram no impacto ou afundaram na lama. Com o tempo, obras, o "
            "arado e a própria natureza trazem o metal enferrujado à superfície, sobretudo no plantio da primavera "
            "e na aração do outono. Os agricultores deixam o material na beira dos campos, e o exército recolhe; "
            "na Bélgica, ele é destruído num centro em Poelkapelle. O nome dado a isso é \"colheita de ferro\". O "
            "risco continua real: desde 1946, cerca de 630 desminadores franceses morreram manuseando essas "
            "munições, e perto de cinco por cento dos projéteis da guerra continham gás, que ainda causa queimaduras quando um "
            "obus de gás mostarda se rompe. Depois da guerra, a França isolou mais de 1.200 km² de terras, a "
            "\"zona vermelha\", considerada destruída demais para a vida humana, e alguns vilarejos, como "
            "Fleury-devant-Douaumont, nunca foram reconstruídos. As restrições diminuíram muito, mas existem até "
            "hoje. Pela estimativa do órgão francês responsável, no ritmo atual seriam necessários de 300 a 700 "
            "anos para limpar a área por completo. Em 2005–2006, encontraram até 300 projéteis por hectare nos "
            "primeiros 15 centímetros de solo dos piores trechos."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Iron_harvest",
                "The iron harvest (French: récolte de fer or moisson de fer) is the annual collection of unexploded ordnance, barbed wire, shrapnel, bullets and other remnant war materiel collected by Belgian and French farmers after ploughing their fields. [...] "
                "During World War I, an estimated 1.5 billion shells were fired on the Western front. [...] "
                "As many as one in every four shells fired did not detonate. [...] "
                "Unexploded weapons—in the form of shells, bullets, and grenades—buried themselves on impact or were otherwise quickly swallowed in the mud. "
                "As time passes, construction work, field ploughing, and natural processes bring the rusting shells to the surface. "
                "Most of the iron harvest is found during the spring planting and autumn ploughing [...] "
                "Farmers collect the munitions and place them along the boundaries of fields or other collection points for authorities. [...] "
                "The French Département du Déminage, 'Department of Mine Clearance' recovers about 900 tons of unexploded munitions every year. "
                "Since 1946, approximately 630 French ordnance disposal workers have been killed handling unexploded munitions. [...] "
                "Close to five percent of the shells fired during the First World War contained poisonous gas, and ordnance disposal experts continue to suffer burns from mustard gas shells that were split open. [...] "
                "where they are regularly collected by the Belgian army for disposal by controlled explosion at a specialist centre in Poelkapelle.",
                nome="Iron harvest"),
            wiki("Zone_rouge",
                "The Zone rouge (French for 'Red Zone') is a chain of non-contiguous areas throughout northeastern France that the French government isolated after the First World War. "
                "The land, which originally covered more than 1,200 square kilometres (460 square miles), was deemed too physically and environmentally damaged by conflict for human habitation. [...] "
                "Restrictions within the Zone rouge still exist today, although the control areas have been greatly reduced. [...] "
                "Some towns and villages were never permitted to be rebuilt after the war, such as Fleury-devant-Douaumont. [...] "
                "According to the Sécurité Civile, the French agency in charge of the land management of Zone rouge, 300 to 700 more years at this current rate will be needed to clean the area completely. "
                "Some experiments conducted in 2005–2006 discovered up to 300 shells per hectare (120 per acre) in the top 15 centimetres (6 inches) of soil in the worst areas.",
                nome="Zone rouge"),
        ],
    },
    # 4 a esquadra brasileira (DNOG) e a gripe em Dacar
    {
        "temas_secundarios": ["brasil_republica", "doencas_infecciosas"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "A principal participação militar do Brasil na Primeira Guerra foi uma esquadra enviada à costa da África. A gripe espanhola a deixou quase dois meses parada no Senegal, e ela chegou a Gibraltar na véspera do armistício.",
        "explicacao": (
            "O Brasil declarou guerra em 26 de outubro de 1917, depois que submarinos alemães afundaram navios "
            "brasileiros, como o vapor Macau. Foi o único país da América do Sul envolvido diretamente no conflito. "
            "Sua contribuição principal foi no mar: a Divisão Naval em Operações de Guerra (DNOG), comandada pelo "
            "contra-almirante Pedro Max Fernando Frontin, com cruzadores, contratorpedeiros, um navio de apoio e um "
            "rebocador, somando 1.515 voluntários. Sob ordens britânicas, ela deveria patrulhar o mar entre Dacar, "
            "Cabo Verde e Gibraltar. A frota partiu em 1º de agosto de 1918. Em Freetown, onde ficou 14 dias, os "
            "tripulantes começaram a adoecer de gripe espanhola. Na noite de 25 de agosto, torpedos passaram entre "
            "os navios sem acertá-los; houve contra-ataque, e o Almirantado britânico creditou aos brasileiros a "
            "destruição de um submarino, embora não houvesse certeza. Em Dacar, a gripe atingiu quase todos e "
            "paralisou a divisão: fontes falam em mais de cem mortos, e a Wikipédia em português registra 464. Os "
            "navios só chegaram a Gibraltar em 10 de novembro; no dia seguinte, foi assinado o armistício. Um "
            "detalhe bem-humorado: o navio de apoio Belmonte ganhou o apelido de \"Guiomar Novais\", nome da "
            "pianista famosa, porque, como ela, em cada porto fazia um \"conserto\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Brazil_during_World_War_I",
                "Brazil then became the only country in South America to be directly involved in the war. "
                "Brazil's major contribution was the Brazilian Navy's patrol of areas in the Atlantic Ocean. [...] "
                "October 18, 1917: U-93 torpedoed the steamship Macau near the coast of Spain and took the captain prisoner "
                "October 26, 1917: Brazil declared war on the Central Powers with limited popular support [...] "
                "Brazil's main military involvement in World War I took place at sea. [...] "
                "The DNOG was initially tasked to patrol the Atlantic maritime area covered by the triangle between the city of Dakar on the African coast, the island of São Vicente, Cape Verde, and Gibraltar at the entrance to the Mediterranean. "
                "The Division would remain under the orders of the British Admiralty [...] "
                "On August 9, 1918, the mission reached Freetown in Sierra Leone, with the fleet staying 14 days, during which the crew began falling ill with Spanish flu during a pandemic. "
                "On the night of August 25, while sailing from Freetown to Dakar, the division suffered a torpedo attack by German submarines, but no casualties or damage were suffered by the Brazilian vessels; the torpedoes passed harmlessly between the Brazilian ships. "
                "A successful counter-attack using depth charges was launched, and the Royal Navy credited the Brazilians with the destruction of a U-boat. "
                "Subsequently, after anchoring in the port of Dakar, the crews were again severely hit by the Spanish flu, which claimed the lives of over a hundred sailors and kept the Division restricted to port for almost two months.",
                nome="Brazil during World War I"),
            wiki("Divis%C3%A3o_Naval_em_Opera%C3%A7%C3%B5es_de_Guerra",
                "Diante da pressão da opinião pública, o governo brasileiro declarou guerra aos países da Tríplice Aliança no dia 26 de outubro de 1917. [...] "
                "o Contra-Almirante Pedro Max Fernando Frontin, nomeado a 30 de janeiro de 1918. [...] "
                "Tender Belmonte, sob o comando de Benjamin Goulart, ex-Valésia, navio alemão arrestado, popularmente conhecido à época pelo apelido de Guiomar Novais, pois como a famosa pianista, em cada porto fazia um conserto; e o "
                "Rebocador Laurindo Pitta [...] "
                "Entre oficiais e praças, totalizavam 1 515 homens, embarcados pelo sistema de voluntariado. [...] "
                "Finalmente, em 1 de agosto de 1918, às 8 horas da manhã, a DNOG suspendeu ferros com destino a Gibraltar [...] "
                "Embora não tenha havido certeza da destruição, o Almirantado Britânico homologou a perda inimiga, creditando-a aos brasileiros. [...] "
                "Estendeu-se, porém, por causa da Gripe Espanhola que se alastrava entre os brasileiros, contagiando a quase todos, paralisando os serviços e descontrolando os planos. Faleceram 464 homens. [...] "
                "No dia 10 de novembro, a DNOG, assim desfalcada, fundeou em Gibraltar; no dia seguinte, era assinado o armistício.",
                nome="Divisão Naval em Operações de Guerra", idioma="pt"),
        ],
    },
    # 5 o café paulista no Tratado de Versalhes
    {
        "temas_secundarios": ["brasil_republica", "economia_curiosa"],
        "tipos_espanto": ["conexao_inesperada", "origem_inesperada"],
        "gancho": "O Tratado de Versalhes, que pôs fim à guerra com a Alemanha, tem um artigo sobre café paulista: os alemães tiveram de garantir ao Brasil o dinheiro do café de São Paulo vendido em Hamburgo e outros portos.",
        "explicacao": (
            "É o artigo 263, na parte financeira do tratado. Café pertencente ao estado de São Paulo tinha sido "
            "vendido nos portos de Hamburgo, Bremen, Antuérpia e Trieste, e o dinheiro ficou depositado no banco "
            "Bleichröder, em Berlim. A Alemanha impediu que a quantia fosse transferida a São Paulo no momento "
            "devido. Pelo tratado, ela garantiu ao governo brasileiro o reembolso dessas somas, com juros, e "
            "aceitou que a conta fosse feita pelo câmbio do dia do depósito, e não por outro posterior. O café era "
            "o principal produto de exportação do país, e a guerra tinha atrapalhado esse comércio: em 1917, por "
            "exemplo, a Grã-Bretanha proibiu a importação de café para priorizar cargas mais vitais em seus navios. "
            "O Brasil, que declarou guerra às Potências Centrais em 1917, sentou-se à mesa da paz com uma "
            "delegação chefiada por Epitácio Pessoa, futuro presidente, e foi um dos fundadores da Liga das Nações. "
            "Além do café, saiu da conferência com o direito de ficar com mais de 70 navios que tinha apreendido "
            "dos países inimigos, incorporados à marinha mercante brasileira, e foi indenizado pelos navios "
            "afundados por submarinos alemães."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://avalon.law.yale.edu/imt/partix.asp",
             "titulo": "Treaty of Versailles, Part IX: Financial Clauses (The Avalon Project, Yale Law School)",
             "idioma": "en",
             "trecho": "ARTICLE 263. Germany gives a guarantee to the Brazilian Government that all sums representing the sale of coffee belonging to the State of Sao Paolo in the ports of Hamburg, Bremen, Antwerp and Trieste, which were deposited with the Bank of Bleichroder at Berlin, shall be reimbursed together with interest at the rate or rates agreed upon. "
                       "Germany having prevented the transfer of the sums in question to the State of Sao Paolo at the proper time, guarantees also that the reimbursement shall be effected at the rate of exchange of the day of the deposit."},
            wiki("Brazil_during_World_War_I",
                "as an attempt to maintain markets for its export products, mainly coffee, latex, and industrially manufactured items. [...] "
                "as well as a British ban on the importation of coffee into England in 1917; the latter was introduced because the British government began prioritizing the shipping of more vital goods given the great losses of merchant ships as a result of German attacks. [...] "
                "October 26, 1917: Brazil declared war on the Central Powers with limited popular support [...] "
                "After the war's end, Brazil participated in the Versailles Peace Conference with a delegation led by Epitácio Pessoa, Brazil's future president. "
                "Brazil was also a founder of the League of Nations after the end of the war. [...] "
                "The Treaty of Versailles allowed Brazil to keep over 70 ships that it had seized from the Central Powers during the war, which were then incorporated into the Brazilian merchant fleet. "
                "Brazil was also financially compensated by Germany for the lost coffee shipments and ships that were sunk by German U-boats during the war.",
                nome="Brazil during World War I"),
        ],
    },
    # 6 as seis horas entre a assinatura e o fim, e Henry Gunther
    {
        "temas_secundarios": ["personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "O armistício da Primeira Guerra foi assinado às 5h da manhã, mas só valeu às 11h. A luta seguiu nessas horas, e o último dia da guerra teve 2.738 mortos; um deles caiu um minuto antes do fim.",
        "explicacao": (
            "Os negociadores alemães pediram um cessar-fogo imediato, mas o marechal francês Foch recusou. Muitas "
            "unidades de artilharia continuaram atirando, entre outros motivos para não ter de carregar a munição "
            "que sobrava, e os Aliados queriam estar na melhor posição caso a guerra recomeçasse. Resultado: no "
            "último dia houve 10.944 baixas, das quais 2.738 mortos. O americano Henry Gunther costuma ser apontado "
            "como o último soldado morto em combate. Filho de uma família de origem alemã de Baltimore, ele tinha "
            "sido rebaixado de sargento a soldado raso porque o censor militar interceptou uma carta em que ele "
            "descrevia as condições \"miseráveis\" da frente. Às 10h59, contra a ordem do seu sargento, ele avançou "
            "sobre duas metralhadoras alemãs. Os alemães, que já sabiam do armistício, tentaram fazer sinais para "
            "ele ir embora; como continuou vindo, foi morto. Colegas contaram a um repórter que ele vivia remoendo "
            "o rebaixamento. O exército lhe devolveu a patente depois da morte. As mortes do último dia causaram "
            "vergonha, e o Congresso americano abriu uma investigação sobre o motivo. E a notícia do fim só chegou "
            "às tropas alemãs na África cerca de duas semanas depois."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Armistice_of_11_November_1918",
                "Many artillery units continued to fire on German targets to avoid having to haul away their spare ammunition. "
                "The Allies also wished to ensure that, should fighting restart, they would be in the most favourable position. "
                "Consequently, there were 10,944 casualties, of whom 2,738 men died, on the last day of the war. [...] "
                "Henry Gunther, an American, is generally recognized as the last soldier killed in action in World War I. [...] "
                "News of the armistice only reached Germany's African forces, still fighting in Northern Rhodesia (today's Zambia), about two weeks later. [...] "
                "After the war, there was a deep shame that so many soldiers died on the final day of the war, especially in the hours after the treaty had been signed but had not yet taken effect. "
                "In the United States, Congress opened an investigation to find out why [...] "
                "\"The armistice was signed at five o'clock this morning, and hostilities are to cease on all fronts at 11 a.m. to-day.\"",
                nome="Armistice of 11 November 1918"),
            wiki("Henry_Gunther",
                "He was killed at 10:59 a.m., about one minute before the Armistice was to take effect at 11:00 a.m. [...] "
                "Gunther was born into a German-American family in east Baltimore, Maryland [...] "
                "A critical letter home, in which he reported on the \"miserable conditions\" at the front and advised a friend to try anything to avoid being drafted, was intercepted by the Army postal censor. "
                "As a result, he was demoted from sergeant to private. [...] "
                "Gunther got up, against the orders of his close friend and sergeant Ernest Powell, and charged the position with a Browning automatic rifle. "
                "The German soldiers, already aware of the armistice that would take effect in one minute, tried to wave Gunther away. He kept coming [...] "
                "He wrote that Gunther had \"brooded a great deal over his recent reduction in rank, and became obsessed with a determination to make good before his officers and fellow soldiers\". [...] "
                "The Army posthumously restored his rank of sergeant [...] "
                "Marshal Foch refused to accede to the German negotiators' request to declare an immediate ceasefire",
                nome="Henry Gunther"),
        ],
    },
    # 7 a última parcela, paga em 2010
    {
        "temas_secundarios": ["dinheiro", "economia_curiosa"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "A Alemanha só quitou as últimas dívidas ligadas às reparações da Primeira Guerra em 3 de outubro de 2010, quase um século depois do fim do conflito. A última parcela foi de 94 milhões de dólares.",
        "explicacao": (
            "As reparações foram impostas pelo Tratado de Versalhes. Nos anos 1920, a Alemanha as pagou sobretudo "
            "com empréstimos estrangeiros. Em 1930, o Plano Young fixou pela primeira vez uma data final: os "
            "pagamentos terminariam em 1988. Mas, ao chegar ao poder em 1933, Hitler suspendeu as reparações e, em "
            "grande parte, repudiou também os empréstimos, embora juros a donos de títulos de reparação tenham sido "
            "pagos até 1939. Depois da Segunda Guerra, a Alemanha Ocidental retomou o assunto. No Acordo de Londres, "
            "de 1953, ela aceitou pagar 50% dos empréstimos que tinham entrado em calote, mas parte da dívida ficou "
            "adiada até a reunificação das duas Alemanhas. Ela veio, e em 1995 o país começou a pagar o que faltava. "
            "A parcela final, de 94 milhões de dólares, saiu em 3 de outubro de 2010, encerrando as dívidas de "
            "empréstimos ligadas às reparações. Vale notar que o economista John Maynard Keynes chamou o tratado de "
            "uma paz \"cartaginesa\", capaz de destruir a economia alemã, mas o consenso dos historiadores de hoje é "
            "que as reparações cabiam na capacidade de pagamento do país, se houvesse vontade política."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("World_War_I_reparations",
            "British economist John Maynard Keynes called the treaty a Carthaginian peace that would economically destroy Germany. "
            "The consensus of contemporary historians is that reparations were not as intolerable as the Germans or Keynes had suggested and were within Germany's capacity to pay had there been the political will to do so. [...] "
            "after coming to power in 1933, Hitler ceased payment of reparations, although Germany still paid interest to holders of reparation bonds until 1939. "
            "Following World War II, West Germany took up payments. [...] "
            "The \"Young Plan\" was accepted and ratified by the German government on 12 March 1930. [...] "
            "with a new payment schedule that would see reparations completed by 1988 – the first time a final date had been set. [...] "
            "Germany's payment of reparations during the 1920s was funded mostly through foreign loans. "
            "In 1933, as well as stopping all reparations payments, the new German Chancellor Adolf Hitler, in large part, repudiated payment of these loans [...] "
            "In June 1953, an agreement was reached on this existing debt with West Germany. "
            "West Germany agreed to repay 50% of the loan amounts that had been defaulted on in the 1920s, but deferred some of the debt until West and East Germany were unified. "
            "In 1995, following reunification, Germany began making the final payments towards the loans. "
            "A final installment of US$94 million was made on 3 October 2010, settling German loan debts in regard to reparations.",
            nome="World War I reparations")],
    },
    # 8 Haber-Bosch: comida e explosivos do ar
    {
        "temas_secundarios": ["quimica_cotidiano", "elementos_quimicos"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "A reação química que hoje sustenta a comida de metade da humanidade permitiu à Alemanha fabricar explosivos sob bloqueio na Primeira Guerra. Sem ela, avalia-se, o país teria perdido em poucos meses.",
        "explicacao": (
            "É o processo de Haber-Bosch, que junta o nitrogênio do ar com hidrogênio, sobre um catalisador de ferro, "
            "e produz amônia. Fritz Haber o fez funcionar no laboratório em 1909, e Carl Bosch o levou à escala "
            "industrial para a empresa BASF. A primeira fábrica abriu em 1913, em Oppau. Na guerra, munição exigia "
            "nitratos em grande quantidade, e a grande fonte natural era o salitre do Chile, explorado por empresas "
            "britânicas. Mesmo que os alemães tivessem acesso legal a ele, os Aliados dominavam as rotas marítimas e "
            "mantinham um bloqueio eficaz. A amônia sintética virou ácido nítrico, matéria-prima dos explosivos, e o "
            "processo foi considerado tão essencial que se tem como praticamente certo que, sem ele, a Alemanha "
            "teria sido derrotada em questão de meses. Hoje, o mesmo processo produz adubos que sustentam a base "
            "alimentar de metade da população mundial. Haber tem uma biografia ainda mais dividida: na guerra, "
            "chefiou o desenvolvimento do gás cloro como arma e acompanhou pessoalmente o primeiro ataque, em "
            "Ypres, em 1915. Recebeu o Nobel de Química de 1918 pela síntese da amônia, sob pressões para que o "
            "prêmio lhe fosse retirado por causa da guerra química."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Haber_process",
                "Haber showed it working in the laboratory in 1909, and Bosch scaled it up for the German company BASF. "
                "The first industrial plant opened in 1913 at Oppau. [...] "
                "In the Haber process, nitrogen and hydrogen gas react on the surface of a solid catalyst, usually iron, to form ammonia. [...] "
                "During World War I, the production of munitions required large amounts of nitrate. "
                "The Allied powers had access to large deposits of sodium nitrate in Chile (Chile saltpetre) controlled by British companies. [...] "
                "Moreover, even if German commercial interests had nominal legal control of such resources, the Allies controlled the sea lanes and imposed a highly effective blockade which would have prevented such supplies from reaching Germany. "
                "The Haber process proved so essential to the German war effort that it is considered virtually certain Germany would have been defeated in a matter of months without it. "
                "Synthetic ammonia from the Haber process was used for the production of nitric acid, a precursor to the nitrates used in explosives.",
                nome="Haber process"),
            wiki("Fritz_Haber",
                "received the Nobel Prize in Chemistry in 1918 for his invention of the Haber process, a method used in industry to synthesize ammonia from nitrogen gas and hydrogen gas. [...] "
                "In addition to leading the teams developing chlorine gas and other deadly gases for use in trench warfare, Haber was on hand personally when it was first released by the German military at the Second Battle of Ypres (22 April to 25 May 1915) in Belgium. [...] "
                "The food base of half the current world population is based on the Haber–Bosch process. [...] "
                "He received the Nobel Prize for Chemistry, yet there were moves to strip him of the award because of his work on gas warfare.",
                nome="Fritz Haber"),
        ],
    },
    # 9 castanhas-da-índia, bactérias e acetona (Weizmann)
    {
        "temas_secundarios": ["fermentacao", "microbiologia"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "Na Primeira Guerra, o governo britânico pediu a todos, até às crianças, que juntassem castanhas-da-índia. O amido delas ia alimentar bactérias que produziam acetona para explosivos, num método de Chaim Weizmann.",
        "explicacao": (
            "A acetona era o solvente usado na fabricação da cordite, o propelente das munições britânicas. "
            "Weizmann, químico e professor em Manchester, tinha descoberto como usar uma bactéria, a Clostridium "
            "acetobutylicum, para fermentar amido e obter acetona, butanol e etanol. Por isso é considerado o pai da "
            "fermentação industrial. Winston Churchill soube da descoberta no início de 1915, e David Lloyd George, "
            "então ministro das Munições, também apoiou o projeto. O teste em escala piloto foi feito numa fábrica "
            "de gim em Londres, e em 1916 seis destilarias foram requisitadas para a produção, que chegou a 30 mil "
            "toneladas de acetona ao longo da guerra. O processo aceitava qualquer amido. Quando o milho não bastou, "
            "o governo lançou uma campanha nacional de coleta de castanhas-da-índia, escolhidas para não desviar "
            "comida da população. O resultado decepcionou: as castanhas eram uma fonte ruim, e a fábrica só produziu "
            "acetona com elas por três meses. Mesmo assim, voltaram a ser recolhidas na Segunda Guerra. Weizmann "
            "também foi líder sionista e, de 1949 até morrer, em 1952, o primeiro presidente de Israel."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Chaim_Weizmann",
                "later as the first president of Israel from 1949 until his death in 1952. [...] "
                "As a biochemist, Weizmann is considered to be the 'father' of industrial fermentation. "
                "He developed the acetone–butanol–ethanol fermentation process, which produces acetone, n-butanol and ethanol through bacterial fermentation. [...] "
                "While serving as a lecturer in Manchester he became known for discovering how to use bacterial fermentation to produce large quantities of desired substances. [...] "
                "He used the bacterium Clostridium acetobutylicum (the Weizmann organism) to produce acetone. "
                "Acetone was used in the manufacture of cordite explosive propellants critical to the Allied war effort [...] "
                "Winston Churchill became aware of the possible use of Weizmann's discovery in early 1915, and David Lloyd George, as Minister of Munitions, joined Churchill in encouraging Weizmann's development of the process. "
                "Pilot plant development of laboratory procedures was completed in 1915 at the J&W Nicholson & Co gin factory in Bow, London, so industrial scale production of acetone could begin in six British distilleries requisitioned for the purpose in early 1916. "
                "The effort produced 30000 tonnes of acetone during the war, although a national collection of horse-chestnuts was required when supplies of maize were inadequate for the quantity of starch needed for fermentation.",
                nome="Chaim Weizmann"),
            wiki("Aesculus_hippocastanum",
                "During World War I, there was a campaign to ask for everyone (including children) to collect the seeds and donate them to the government. "
                "The conkers were used as a source of starch for fermentation using the Clostridium acetobutylicum method devised by Chaim Weizmann to produce acetone for use as a solvent for the production of cordite, which was then used in military armaments. "
                "Weizmann's process could use any source of starch, but the government chose to ask for conkers to avoid causing starvation by depleting food sources. "
                "Conkers were found to be a poor source and the factory only produced acetone for three months, but they were collected again during World War II for the same reason.",
                nome="Aesculus hippocastanum"),
        ],
    },
    # 10 a camuflagem "dazzle": chamar atenção para confundir
    {
        "temas_secundarios": ["pintura", "percepcao_ilusoes"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Na Primeira Guerra, navios foram pintados com listras e zigue-zagues berrantes. A ideia não era esconder, e sim confundir: o inimigo teria dificuldade de saber o rumo e a velocidade do alvo.",
        "explicacao": (
            "A camuflagem \"dazzle\" (ofuscante) é creditada ao pintor de marinhas britânico Norman Wilkinson; um "
            "zoólogo, John Graham Kerr, reivindicou a prioridade, mas não foi reconhecido. Em 1917, os submarinos "
            "alemães afundavam navios mercantes em grande número, e tornar um navio invisível com tinta era "
            "impossível em todas as condições de luz. Wilkinson apostou no oposto: formas geométricas em cores de "
            "contraste violento, para quebrar o contorno do casco. Assim, um observador teria dificuldade de saber "
            "se via a proa ou a popa, ou se o navio se aproximava ou se afastava. Alguns esquemas incluíam até uma "
            "falsa onda de proa, para enganar sobre a velocidade. Com uma equipe de estudantes de arte, ele testou "
            "modelos sobre uma plataforma giratória vistos por um periscópio. A marinha mercante britânica adotou a "
            "pintura em outubro de 1917, e a Marinha dos EUA também. Se funcionou, ninguém sabe ao certo: em 1918, "
            "o Almirantado analisou as perdas e não chegou a conclusões claras. A arte também se meteu: Picasso "
            "disse que os cubistas é que a tinham inventado, e Edward Wadsworth, que supervisionou a camuflagem de "
            "mais de 2 mil navios, depois pintou uma série de quadros desses navios."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Dazzle_camouflage",
            "Credited to the British marine artist Norman Wilkinson, though with a rejected prior claim by the zoologist John Graham Kerr, it consisted of complex patterns of geometric shapes in contrasting colours interrupting and intersecting each other. "
            "Unlike other forms of camouflage, the intention of dazzle is not to conceal but to make it difficult to estimate a target's range, speed, and heading. [...] "
            "Dazzle was adopted by the Admiralty in the UK, and then by the United States Navy. [...] "
            "Dazzle attracted the notice of artists such as Picasso, who claimed that Cubists like he had invented it. "
            "Edward Wadsworth, who supervised the camouflaging of over 2,000 ships during the First World War, painted a series of canvases of dazzle ships after the war, based on his wartime work. [...] "
            "The approach was developed after Allied navies were unable to develop effective means to hide ships in all weather conditions. [...] "
            "An observer would find it difficult to know exactly whether the stern or the bow was in view; and it would be correspondingly difficult to estimate whether the observed vessel was moving towards or away from the observer's position. "
            "Wilkinson advocated \"masses of strongly contrasted colour\" to confuse the enemy about a ship's heading. [...] "
            "Assembling a team of art students and artists in Royal Naval Reserve uniform, including the Vorticist Edward Wadsworth, Wilkinson experimented with models mounted on a turntable which could be observed through a periscope. "
            "He then outmaneuvered the reluctant Admiralty by going straight to Joseph Maclay, the Minister of Shipping, resulting in the British Merchant Service adopting dazzle painting in October 1917 [...] "
            "Patterns sometimes also included a false bow wave to make it difficult for an enemy to estimate the ship's speed. [...] "
            "In 1918, the Admiralty analysed shipping losses, but was unable to draw clear conclusions. [...] "
            "At sea in 1917, heavy losses of merchant ships to Germany's unrestricted submarine warfare campaign led to new desire for camouflage.",
            nome="Dazzle camouflage")],
    },
    # 11 a gripe "espanhola" e a gripe "brasileira"
    {
        "temas_secundarios": ["doencas_infecciosas", "brasil_republica"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "A gripe espanhola não tem esse nome por ter surgido na Espanha: neutra na guerra, a Espanha noticiava a doença sem censura e pareceu o foco. No Senegal, ela chegou a ser chamada de \"gripe brasileira\".",
        "explicacao": (
            "A pandemia estourou no fim da Primeira Guerra, quando os censores dos países em guerra abafavam más "
            "notícias para não abalar o moral. A Espanha, neutra, não tinha essa máquina de propaganda, e seus "
            "jornais falavam livremente da epidemia. Por isso o país pareceu o centro do surto. A censura funcionou "
            "tão bem que as autoridades de saúde espanholas nem sabiam que os vizinhos também estavam sendo "
            "atingidos. Em outubro de 1918, numa carta a uma revista médica americana, um funcionário espanhol "
            "protestou: a epidemia não tinha nascido na Espanha, e isso deveria ser registrado como reparação "
            "histórica. A origem geográfica real continua indeterminada, com hipóteses concorrentes. Cada lugar "
            "tendia a culpar outro. Soldados britânicos e alemães falavam em gripe ou febre \"de Flandres\", por "
            "causa de um campo de batalha na Bélgica. A imprensa francesa começou com \"gripe americana\" e mudou "
            "para não ofender um aliado. Na Espanha, ela era a \"gripe francesa\". No Senegal, foi chamada de "
            "\"gripe brasileira\" e, no Brasil, de \"gripe alemã\". Os mortos no mundo são estimados entre 17 "
            "milhões e 50 milhões, talvez até 100 milhões; no Brasil, foram 300 mil."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Spanish_flu",
            "Estimates of deaths range from 17 million to 50 million, and possibly as high as 100 million, making it one of the deadliest pandemics in history. "
            "The pandemic broke out near the end of World War I, when wartime censors in the belligerent countries suppressed bad news to maintain morale, but newspapers freely reported the outbreak in neutral Spain, creating a misleading impression of Spain as the epicenter and leading to the disease being known as Spanish flu. "
            "Limited historical epidemiological data make the pandemic's geographic origin indeterminate, with competing hypotheses [...] "
            "Spain was a neutral country unconcerned with appearances of combat readiness, and without a wartime propaganda machine to prop up morale, so its newspapers freely reported epidemic effects, making Spain the apparent locus of the epidemic. "
            "The censorship was so effective that Spain's health officials were unaware its neighboring countries were similarly affected. "
            "In an October 1918 \"Madrid Letter\" to the Journal of the American Medical Association, a Spanish official protested [...] "
            "...this epidemic was not born in Spain, and this should be recorded as a historic vindication.\" [...] "
            "French press initially used 'American flu', but adopted 'Spanish flu' in lieu of antagonizing an ally. "
            "In the spring of 1918, British soldiers called it 'Flanders flu', while German soldiers used 'Flandern-Fieber' (Flemish fever), both after a battlefield in Belgium where many soldiers on both sides fell ill. "
            "In Senegal it was named 'Brazilian flu', and in Brazil, 'German flu'. "
            "In Spain it was also known as the 'French flu' (gripe francesa) [...] "
            "In Brazil, 300,000 died",
            nome="Spanish flu")],
    },
    # 12 Lawrence Bragg: Nobel aos 25, caçando canhões pelo som
    {
        "temas_secundarios": ["acustica", "minerais_rochas"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Lawrence Bragg tinha 25 anos e servia no exército britânico quando ganhou o Nobel de Física de 1915, junto com o pai. Na guerra, ele ajudava a localizar canhões inimigos pelo som dos disparos.",
        "explicacao": (
            "Bragg e o pai, William Henry Bragg, dividiram o Nobel pela análise da estrutura de cristais com raios "
            "X, base da cristalografia. Ele continua sendo o mais jovem premiado em qualquer área científica. Em "
            "1915, foi destacado para os Engenheiros Reais com uma tarefa: achar a posição da artilharia inimiga a "
            "partir do estrondo dos tiros. Em 2 de setembro desse ano, o irmão dele morreu na campanha de Galípoli; "
            "pouco depois, veio o Nobel. O problema técnico era sério. Os canhões pesados produziam um som grave "
            "demais para os microfones da época, e era preciso separar o estampido do disparo do estrondo do "
            "próprio projétil. Depois de meses de fracassos, a solução veio em 1916, de um cabo da equipe, William "
            "Sansome Tucker: um microfone de baixa frequência com um fio de platina aquecido, que esfriava quando a "
            "onda sonora do disparo passava, e essa variação podia ser registrada. O sistema britânico funcionou "
            "muito bem, ganhou uma unidade em cada exército e foi adotado pelos americanos. Décadas depois, Bragg "
            "dirigia o Laboratório Cavendish, em Cambridge, quando Watson e Crick anunciaram a estrutura do DNA."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Lawrence_Bragg",
                "who uniquely shared a Nobel Prize with his father William Henry Bragg – the 1915 Nobel Prize in Physics \"for their services in the analysis of crystal structure by means of X-rays\", an important step in the development of X-ray crystallography. [...] "
                "Bragg was the director of the Cavendish Laboratory, Cambridge, when James D. Watson and Francis Crick reported the discovery of the structure of DNA [...] "
                "In 1915 he was seconded to the Royal Engineers to develop a method to localise enemy artillery from the boom of their firing. "
                "On 2 September 1915 his brother was killed during the Gallipoli Campaign. "
                "Shortly afterwards, he and his father were awarded the Nobel Prize in Physics. "
                "He was 25 years old and remains the youngest science laureate. "
                "The problem with sound ranging was that the heavy guns boomed at too low a frequency to be detected by a microphone. "
                "After months of frustrating failure he and his group devised a hot wire air wave detector that solved the problem. [...] "
                "British sound ranging was very effective; there was a unit in every British Army and their system was adopted by the Americans when they entered the war.",
                nome="Lawrence Bragg"),
            wiki("Artillery_sound_ranging",
                "care needed to be taken to separate the sonic boom of the shell from the actual sound of the firing. "
                "This problem was solved in mid-1916 when one of Bragg's detachment, Lance Corporal William Sansome Tucker, formerly of the Physics Department, London University, invented the low-frequency microphone. "
                "This separated the low frequency sound made by the firing of the gun from the sonic boom of the shell. "
                "It used a heated platinum wire that was cooled by the sound wave of a gun firing.",
                nome="Artillery sound ranging"),
        ],
    },
    # 13 a árvore de Natal de Boston e a explosão de Halifax
    {
        "temas_secundarios": ["costumes_rituais", "falhas_engenharia"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "A árvore de Natal oficial de Boston é um presente da Nova Escócia, no Canadá: um agradecimento pela ajuda após a explosão de Halifax, em 1917, a maior explosão causada por humanos até então.",
        "explicacao": (
            "Em 6 de dezembro de 1917, o cargueiro francês Mont-Blanc, carregado de TNT, ácido pícrico, benzol e "
            "algodão-pólvora para a guerra, bateu em baixa velocidade no norueguês Imo, no porto de Halifax. O "
            "choque danificou barris de benzol, e as faíscas puseram fogo no navio. Uns 20 minutos depois, ele "
            "explodiu, com energia equivalente a cerca de 2,9 quilotons de TNT. Pelo menos 1.782 pessoas morreram, "
            "e cerca de 9 mil ficaram feridas. Milhares tinham parado para ver o incêndio, muitas atrás de janelas, "
            "e os estilhaços de vidro causaram ferimentos terríveis: oftalmologistas fizeram 249 remoções de olhos. "
            "Uma onda gerada pela explosão destruiu uma comunidade mi'kmaq. Um despachante ferroviário, Vince "
            "Coleman, voltou ao posto para telegrafar um alerta e parar um trem que chegava, e morreu ali. A ajuda "
            "da Cruz Vermelha de Boston e de um comitê de Massachusetts chegou logo. Em 1918, Halifax mandou a "
            "Boston uma árvore de Natal como agradecimento. O gesto foi retomado em 1971 por produtores de árvores "
            "da Nova Escócia, como doação anual, e depois assumido pelo governo da província. A árvore é a oficial "
            "da cidade e fica acesa no Boston Common durante as festas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Halifax_Explosion",
            "On the morning of 6 December 1917, the French cargo ship SS Mont-Blanc and the Norwegian vessel SS Imo collided in the harbour of Halifax, Nova Scotia, Canada. [...] "
            "At least 1,782 people, largely in Halifax and Dartmouth, were killed by the blast, debris, fires, or collapsed buildings, and an estimated 9,000 others were injured. "
            "The blast was the largest human-made explosion at the time. "
            "It released the equivalent energy of roughly 2.9 kilotons of TNT (12 TJ). [...] "
            "At roughly 8:45 am, she collided at low speed [...] "
            "On Mont-Blanc, the impact damaged benzol barrels stored on deck, causing them to leak vapours, which were ignited by sparks from the collision, setting off a fire on board that quickly grew out of control. "
            "Around 20 minutes later at 9:04:35 am, Mont-Blanc exploded. [...] "
            "A tsunami created by the blast wiped out a community of Mi'kmaq [...] "
            "The vessel was fully loaded with the explosives trinitrotoluene (TNT) and picric acid, the highly flammable fuel benzol, and guncotton. [...] "
            "Coleman remembered that an incoming passenger train from Saint John, New Brunswick, was due to arrive at the railyard within minutes. "
            "He returned to his post alone and continued to send out urgent telegraph messages to stop the train. [...] "
            "Coleman was killed at his post. [...] "
            "Thousands of people had stopped to watch the ship burning in the harbour, many from inside buildings, leaving them directly in the path of glass fragments from shattered windows. "
            "According to an article in the British Journal of Ophthalmology, ophthalmologists responding to the disaster performed 249 enucleations [...] "
            "In 1918, Halifax sent a Christmas tree to Boston in thanks and remembrance for the help that the Boston Red Cross and the Massachusetts Public Safety Committee provided immediately after the disaster. "
            "That gift was revived in 1971 by the Lunenburg County Christmas Tree Producers Association, which began an annual donation of a large tree [...] "
            "The gift was later taken over by the Nova Scotia government [...] "
            "The tree is Boston's official Christmas tree and is lit on Boston Common throughout the holiday season.",
            nome="Halifax Explosion")],
    },
    # 14 o telegrama Zimmermann: "Não posso negar"
    {
        "temas_secundarios": ["criptografia", "espionagem"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1917, os britânicos decifraram um telegrama em que a Alemanha oferecia ao México o Texas, o Arizona e o Novo México. Faltava provar que era verdadeiro, e quem resolveu foi o autor: \"Não posso negar\".",
        "explicacao": (
            "Em janeiro de 1917, o ministro do Exterior alemão, Arthur Zimmermann, instruiu o embaixador no México: "
            "se os Estados Unidos entrassem na guerra, a Alemanha proporia uma aliança, com apoio financeiro e a "
            "promessa de que o México reconquistaria os territórios perdidos. Os britânicos tinham cortado os cabos "
            "telegráficos internacionais alemães no início da guerra, e a mensagem viajou por rádio e escondida em "
            "mensagens de diplomatas de dois países neutros, os próprios Estados Unidos e a Suécia. O presidente "
            "Wilson tinha deixado a Alemanha usar o canal diplomático americano. Tudo passava pela Sala 40, a "
            "central de decifração do Almirantado britânico. O dilema era revelar o conteúdo sem expor que os "
            "britânicos quebravam códigos alemães e ainda espionavam a comunicação americana. A versão pública foi "
            "a de que o texto tinha sido \"comprado no México\". Publicado, o telegrama ainda despertou dúvidas, e o "
            "governo americano não podia mostrar suas provas. Então, numa entrevista coletiva em 3 de março de 1917, "
            "o próprio Zimmermann disse a um jornalista americano: \"Não posso negar. É verdade.\" Em 6 de abril, o "
            "Congresso americano votou a declaração de guerra à Alemanha."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Zimmermann_Telegram",
            "With Germany's aid, Mexico would recover Texas, Arizona, and New Mexico. "
            "The telegram was intercepted by British intelligence. [...] "
            "The message came in the form of a coded telegram dispatched by Arthur Zimmermann, the State Secretary of Foreign Affairs of the German Empire on January 17, 1917. "
            "The message was sent to the German ambassador to Mexico, Heinrich von Eckardt. [...] "
            "we shall give ample financial support, and it is understood that Mexico is to reconquer her lost territory of New Mexico, Texas and Arizona. [...] "
            "It went by radio, and passed via telegraph cable inside messages sent by diplomats of two neutral countries (the United States and Sweden). "
            "Direct telegraph transmission of the telegram was impossible because the British had cut the German international cables at the outbreak of war. [...] "
            "After the Germans' telegraph cables had been cut, the German Foreign Office appealed to the United States for use of their diplomatic telegraphic messages for peace messages. "
            "President Wilson agreed [...] "
            "All traffic passing through British hands came to British intelligence, particularly to the codebreakers and analysts in Room 40 at the Admiralty. [...] "
            "the disclosure would expose the German codes broken in Room 40 and British eavesdropping on United States diplomatic traffic. [...] "
            "Balfour could obscure the real source with the half-truth that it had been \"bought in Mexico\". [...] "
            "The British had provided evidence confidentially to the United States that the message was genuine, but Wilson could not make the evidence public without compromising the British codebreaking operation. "
            "This problem was resolved, however, when  doubts as to the authenticity of the telegram were removed by Zimmermann himself. "
            "At a press conference on March 3, 1917, he told an American journalist, \"I cannot deny it. It is true.\" [...] "
            "On April 6, 1917, Congress voted to declare war on Germany.",
            nome="Zimmermann Telegram")],
    },
    # 15 os primeiros bancos de sangue, antes de Passchendaele
    {
        "temas_secundarios": ["historia_medicina", "sistema_imunologico"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Os precursores dos bancos de sangue nasceram na Primeira Guerra: em 1917, um médico do exército americano estocou sangue de soldados doadores em frascos com citrato, à espera de uma grande batalha na Bélgica.",
        "explicacao": (
            "O problema era o tempo. Feridos morriam de choque e hemorragia antes de chegar a um lugar onde se "
            "pudesse fazer transfusão, e o sangue coagulava fora do corpo. Em 1914, o belga Albert Hustin e o "
            "argentino Luis Agote fizeram transfusões indiretas usando citrato de sódio, que impede a coagulação. "
            "Em fevereiro de 1916, Peyton Rous e o colega Joseph R. Turner, do Instituto Rockefeller, relataram que, numa mistura "
            "de sangue com solução de citrato e de glicose, as células se mantinham intactas por cerca de quatro "
            "semanas. Oswald Hope Robertson, médico e oficial do exército americano, trabalhou com Rous e aprendeu "
            "os métodos. Em 1917, a serviço do corpo médico britânico, organizou os primeiros depósitos de sangue, "
            "com soldados como doadores, preparando-se para a Terceira Batalha de Ypres. O sangue era tirado da veia, "
            "misturado ao citrato e guardado em frascos nos postos de atendimento perto da frente. Ele também testou "
            "guardar glóbulos vermelhos separados em frascos com gelo. Há um detalhe que confunde muita gente: outro "
            "Robertson, o canadense Lawrence Bruce, foi quem convenceu o corpo médico britânico a adotar "
            "transfusões, e fez a primeira dele na guerra em outubro de 1915, com uma seringa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Blood_bank",
                "Francis Peyton Rous at the Rockefeller University (then The Rockefeller Institute for Medical Research) wanted to solve the problems of blood transfusion. "
                "With a colleague, Joseph R. Turner, he made two critical discoveries [...] "
                "The first non-direct transfusion was performed on March 27, 1914, by the Belgian doctor Albert Hustin, though this was a diluted solution of blood. "
                "The Argentine doctor Luis Agote used a much less diluted solution in November of the same year. "
                "Both used sodium citrate as an anticoagulant. [...] "
                "In February 1916, they reported in the Journal of Experimental Medicine the key method for blood preservation. "
                "They replaced the additive, gelatine, with a mixture sodium citrate and glucose (dextrose) solution and found: [...] "
                "the cells remain intact for about 4 weeks. [...] "
                "Canadian Lieutenant Lawrence Bruce Robertson was instrumental in persuading the Royal Army Medical Corps (RAMC) to adopt the use of blood transfusion at the Casualty Clearing Stations for the wounded. "
                "In October 1915, Robertson performed his first wartime transfusion with a syringe [...] "
                "Oswald Hope Robertson, a medical researcher and U.S. Army officer, worked with Rous at the Rockefeller between 1915 and 1917, and learned the blood matching and preservation methods. "
                "He was attached to the RAMC in 1917, where he was instrumental in establishing the first blood banks, with soldiers as donors, in preparation for the anticipated Third Battle of Ypres. "
                "He used sodium citrate as the anticoagulant, and the blood was extracted from punctures in the vein, and was stored in bottles at British and American Casualty Clearing Stations along the Front. "
                "He also experimented with preserving separated red blood cells in iced bottles.",
                nome="Blood bank"),
            wiki("Oswald_Hope_Robertson",
                "Recognizing the critical need to treat shock and hemorrhage closer to the front lines where wounded soldiers were dying before they could reach traditional transfusion stations, Robertson set out to solve the problem of blood storage and transport. "
                "In 1917, working with the Expeditionary Force, he established the first experimental \"blood depots\" (effectively the precursors to modern blood banks).",
                nome="Oswald Hope Robertson"),
        ],
    },
]
