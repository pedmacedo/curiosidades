LOTE = "2026-11-24-exploracao_espacial-01"
AREA = "espaco"
TEMA = "exploracao_espacial"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Gagarin saltou de paraquedas e a URSS escondeu por causa da FAI
    {
        "temas_secundarios": ["guerra_fria", "corpo_extremo"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Gagarin não pousou dentro da nave: foi ejetado a 7 km de altura e desceu de paraquedas. As regras de recorde da época exigiam pousar com a nave, e a URSS só admitiu o salto em 1971.",
        "explicacao": (
            "O voo da Vostok 1, em abril de 1961, deu uma única volta na Terra e levou 108 minutos do lançamento "
            "ao pouso. Na descida, com a cápsula ainda a 7 km do chão, a escotilha se soltou e, dois segundos "
            "depois, Iuri Gagarin foi ejetado. O paraquedas dele abriu quase de imediato e ele tocou o solo uns dez "
            "minutos mais tarde; a cápsula desceu à parte, com o próprio paraquedas. Uma camponesa e a neta viram "
            "uma figura de traje laranja e capacete branco descer do céu e começaram a recuar com medo. Segundo "
            "Gagarin, ele as tranquilizou dizendo que era um cidadão soviético que tinha descido do espaço e "
            "precisava de um telefone. O salto tinha peso político: em 1961, as regras da FAI, que homologa "
            "recordes aeronáuticos, exigiam que o piloto pousasse junto com a nave. A União Soviética afirmou "
            "oficialmente que ele tinha pousado na Vostok, o governo o obrigou a mentir em entrevistas e a FAI "
            "homologou os recordes. A verdade só foi admitida em 1971. Mesmo assim, a FAI manteve os recordes e "
            "mudou as regras, reconhecendo que o essencial, o lançamento, a órbita e o retorno seguros do piloto, "
            "tinha sido cumprido."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Vostok_1",
            "The Vostok 3KA space capsule was launched from Baikonur Cosmodrome on 12 April 1961, with Soviet cosmonaut Yuri Gagarin aboard [...] "
            "The flight took 108 minutes from launch to landing. Gagarin parachuted to the ground separately from his capsule after ejecting at 7 km (23,000 ft) altitude. [...] "
            "At 07:55 UTC, when Vostok 1 was still 7 km (23,000 ft) from the ground, the hatch of the spacecraft was released, and two seconds later Gagarin was ejected. "
            "At 2.5 km (8,200 ft) altitude, the main parachute was deployed from the Vostok spacecraft. "
            "Gagarin's parachute opened almost immediately, and about ten minutes later, at 08:05 UTC, Gagarin landed. [...] "
            "A kolkhoz woman Annihayat Nurskanova and her granddaughter, Rita, observed the strange scene of a figure in a bright orange suit with a large white helmet landing near them by parachute. "
            "Gagarin later recalled, \"When they saw me in my space suit and the parachute dragging alongside as I walked, they started to back away in fear. "
            "I told them, don't be afraid, I am a Soviet citizen like you, who has descended from space and I must find a telephone to call Moscow!\" [...] "
            "The FAI rules in 1961 required that a pilot must land with the spacecraft to be considered an official spaceflight for the FAI record books. "
            "Although some contemporary Soviet sources stated that Gagarin had parachuted separately to the ground, the Soviet Union officially insisted that he had landed with the Vostok; "
            "the government forced the cosmonaut to lie in press conferences, and the FAI certified the flight. "
            "The Soviet Union did not admit until 1971 that Gagarin had ejected and landed separately from the Vostok descent module. "
            "Gagarin's spaceflight records were nonetheless certified and reaffirmed by the FAI, which revised its rules, and acknowledged that the crucial steps of the safe launch, orbit, and return of the pilot had been accomplished.",
            nome="Vostok 1")],
    },
    # 2 o traje de Leonov inflou na primeira caminhada espacial
    {
        "temas_secundarios": ["corpo_extremo", "guerra_fria"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Na primeira caminhada espacial, em 1965, o traje de Alexei Leonov estufou tanto que ele não conseguia voltar para a nave. Ele soltou parte da pressão do traje, abaixo do limite seguro, sem avisar pelo rádio.",
        "explicacao": (
            "A Voskhod 2 tinha uma câmara de descompressão inflável, por onde Leonov saiu enquanto o colega Pavel "
            "Belyayev ficava na cápsula. A caminhada durou 12 minutos e 9 segundos. No vácuo, o traje Berkut "
            "inchou como um balão: Leonov não alcançava nem o disparador da câmera presa ao peito, que ficava na "
            "coxa, e no fim o traje estava tão rígido que ele não conseguia entrar de volta na câmara. A saída foi "
            "baixar a pressão interna para que as juntas voltassem a dobrar, chegando abaixo dos limites de "
            "segurança e flertando com a doença descompressiva. Relatos posteriores dizem que ele ainda entrou de "
            "cabeça, contra o procedimento, e ficou entalado de lado ao se virar para fechar a escotilha. Ele não "
            "comentou nada disso pelo rádio, para não alarmar ninguém. Os médicos registraram que a temperatura "
            "do corpo dele subiu 1,8 °C em 20 minutos, e Leonov contou que o suor chegava aos joelhos dentro do "
            "traje. Na época, a agência oficial TASS informou apenas que ele estava bem; a história completa veio "
            "de documentos russos divulgados depois da Guerra Fria. Leonov também disse que levava uma pílula de "
            "suicídio, para o caso de não conseguir voltar e Belyayev ter de abandoná-lo em órbita."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Voskhod_2",
            "was a Soviet crewed space mission in March 1965. [...] "
            "Alexei Leonov became the first person to leave the spacecraft in a specialised spacesuit to conduct a 12-minute spacewalk. [...] "
            "Duration: 12 minutes 9 seconds [...] "
            "Cosmonaut Alexei Leonov donned a Berkut spacesuit and left the spacecraft while the other cosmonaut of the two-man crew, Pavel Belyayev, remained inside. [...] "
            "However, when he tried to use the still camera on his chest, the suit had ballooned and he was unable to reach down to the shutter switch on his leg. "
            "After his 12 minutes and 9 seconds outside the Voskhod, Leonov found that his suit had stiffened, due to ballooning out, to the point where he could not re-enter the airlock. "
            "He was forced to bleed off some of his suit's pressure, in order to be able to bend the joints, eventually going below safety limits. "
            "Leonov did not report his action on the radio to avoid alarming others [...] "
            "The government news agency, TASS, reported that, \"outside the ship and after returning, Leonov feels well\"; however, post-Cold War Russian documents reveal a different story [...] "
            "Later accounts report Cosmonaut Leonov violated procedure by entering the airlock head-first, then became stuck sideways when he turned to close the outer hatch, "
            "forcing him to flirt with decompression sickness (the \"bends\") by lowering the suit pressure so he could bend to free himself. "
            "Leonov said that he had a suicide pill to swallow had he been unable to re-enter the Voskhod 2, and Belyayev been forced to abandon him in orbit. "
            "Doctors reported that Leonov nearly suffered heatstroke — his core body temperature increased by 1.8 °C (3.2 °F) in 20 minutes; "
            "Leonov said he was up to his knees in sweat, which sloshed in the suit.",
            nome="Voskhod 2")],
    },
    # 3 Soyuz 11: os únicos mortos no espaço, e a troca de equipe
    {
        "temas_secundarios": ["corpo_extremo", "guerra_fria"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Os únicos humanos que morreram no espaço foram os três da Soyuz 11, em 1971, quando uma válvula se abriu na volta. Eles só voaram porque um raio X sugeriu tuberculose num membro da equipe titular.",
        "explicacao": (
            "A Soyuz 11 levou Georgy Dobrovolsky, Vladislav Volkov e Viktor Patsayev à Salyut 1, a primeira "
            "estação espacial do mundo, onde passaram 22 dias, um recorde de permanência na época. A equipe "
            "original era outra: Alexei Leonov, Valery Kubasov e Pyotr Kolodin. Quatro dias antes do lançamento, "
            "um raio X indicou que Kubasov poderia ter tuberculose, e as regras da missão mandavam trocar a equipe "
            "inteira pela reserva. Na volta, os módulos da nave se separavam com parafusos explosivos que deviam "
            "disparar em sequência, mas dispararam juntos. O tranco afrouxou uma válvula de equalização de "
            "pressão, que se abriu a 168 km de altitude, acima da linha de Kármán. A perda de pressão matou em "
            "menos de um minuto, e a válvula ficava embaixo dos assentos, impossível de achar e bloquear a tempo. "
            "O corpo de Patsayev estava perto dela; talvez ele tentasse fechá-la quando perdeu a consciência. A "
            "cápsula pousou sozinha e, por fora, estava intacta. A equipe de resgate bateu na lateral e ninguém "
            "respondeu. Depois do acidente, a Soyuz foi bastante redesenhada para levar só dois cosmonautas, e o "
            "espaço extra permitiu que eles usassem trajes pressurizados Sokol no lançamento e no pouso."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Soyuz_11",
            "was the only crewed mission (but failed) to board the world's first space station, Salyut 1. "
            "The crew – Georgy Dobrovolsky, Vladislav Volkov, and Viktor Patsayev – arrived at the space station on 7 June 1971, and departed on 29 June 1971. "
            "The mission ended in disaster when the crew capsule depressurised during preparations for re-entry, killing the three-person crew. "
            "The crew members of Soyuz 11 are the only humans to have died in space (i.e. above the Kármán line). [...] "
            "The original prime crew for Soyuz 11 consisted of Alexei Leonov, Valery Kubasov, and Pyotr Kolodin. "
            "A medical X-ray examination four days before launch suggested that Kubasov might have tuberculosis, and according to the mission rules, the prime crew was replaced with the backup crew. [...] "
            "the cosmonauts remained on board for 22 days, setting space endurance records [...] "
            "When the recovery team opened the capsule of the Soyuz 11, they found all three men dead. [...] "
            "Outwardly, there was no damage whatsoever. They knocked on the side, but there was no response from within. [...] "
            "The two modules were held together by explosive bolts designed to fire sequentially; in fact, they had fired simultaneously. "
            "The explosive force of the simultaneous bolt firing caused the internal mechanism of the pressure equalisation valve to loosen a seal [...] "
            "The valve opened at an altitude of 168 kilometres (104 mi; 91 nmi), and the resultant loss of pressure was fatal in less than a minute. "
            "The valve was located beneath the seats and was impossible to find and block before the air was lost. [...] "
            "Patsayev's body was found positioned near the valve, and he may have been attempting to close or block the valve at the time he lost consciousness. [...] "
            "The Soyuz spacecraft was extensively redesigned after this incident to carry only two cosmonauts. "
            "The extra room meant that the crew could wear Sokol space suits during launch and landing.",
            nome="Soyuz 11")],
    },
    # 4 os alarmes 1202 da Apollo 11
    {
        "temas_secundarios": ["historia_computacao", "falhas_engenharia"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Na descida da Apollo 11, o computador de bordo disparou os alarmes 1202 e 1201: estava sobrecarregado. O pouso seguiu porque o software largava sozinho as tarefas menos importantes e mantinha as vitais.",
        "explicacao": (
            "Os alarmes avisavam que o computador tinha ficado sem as áreas de memória de que precisava para rodar "
            "as tarefas, e a resposta a eles era um reinício parcial. A culpa era do radar de encontro, que "
            "acompanha o módulo de comando em órbita e tinha sido deixado em espera para o caso de um aborto. Um "
            "documento de interface falho não exigia sincronia de fase entre duas fontes de 800 Hz, uma do radar "
            "e outra usada pelo computador como referência de tempo. Com isso, a antena, parada, parecia tremer "
            "sem parar, e o computador recebia 6.400 interrupções por segundo, cerca de 13% de carga extra sobre "
            "os quase 85% habituais nessa fase. Quando Buzz Aldrin pediu uma tela que comparava a altitude medida "
            "pelo radar com a calculada, mais 10% de carga estouraram a conta. Mas o software tinha prioridades: "
            "a cada reinício, descartava as tarefas menos importantes, inclusive a tela de Aldrin, e preservava "
            "a navegação e o controle. Em Houston, o controlador Steve Bales e a equipe dele, que incluía Jack "
            "Garman, deram vários \"GO\", e o pouso deu certo. O problema já tinha sido documentado em testes da "
            "Apollo 9, mas, como tinha ocorrido uma só vez, preferiram voar com o equipamento já testado a trocar "
            "por um radar novo."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Apollo_Guidance_Computer",
            "PGNCS generated unanticipated warnings during Apollo 11's lunar descent, with the AGC showing a 1202 alarm (\"Executive overflow - NO CORE SETS\"), and then a 1201 alarm (\"Executive overflow - NO VAC AREAS\"). "
            "The response of the AGC to either alarm was a soft restart. "
            "The cause was a rapid, steady stream of spurious cycle steals from the rendezvous radar (tracking the orbiting command module), intentionally left on standby during the descent in case it was needed for an abort. "
            "During this part of the approach, the processor would normally be almost 85% loaded. "
            "The extra 6,400 cycle steals per second added the equivalent of 13% load, leaving just enough time for all scheduled tasks to run to completion. "
            "Five minutes into the descent, Buzz Aldrin gave the computer the command 1668, which instructed it to periodically calculate and display DELTAH (the difference between altitude sensed by the radar and the computed altitude). "
            "The 1668 added another 10% to the processor workload, causing executive overflow and a 1202 alarm. [...] "
            "The AGC software had been designed with priority scheduling, and automatically recovered, deleting lower priority tasks including the 1668 display task, to complete its critical guidance and control tasks. "
            "Guidance controller Steve Bales and his support team that included Jack Garman issued several \"GO\" calls and the landing was successful. [...] "
            "It was caused by a flawed interface control document (ICD) between the PGNCS and the ATCA (Attitude and Translation Control Assembly), that failed to specify phase synchronization between two 800 Hz signals"
            "—a problem already known and documented during the launch site testing of LM-3 in Apollo 9. "
            "However, because the problem had only occurred once during testing, they concluded that it was safer to fly with the existing hardware that they had already tested, than to fly with a newer but largely untested radar system . "
            "In the actual hardware, the position of the rendezvous radar was encoded with synchros excited by a different source of 800 Hz AC than the one used by the computer as a timing reference. "
            "The two 800 Hz sources were frequency locked but not phase locked, and the random phase offset made it appear as though the antenna was rapidly \"dithering\" in position, even though it was completely stationary.",
            nome="Apollo Guidance Computer")],
    },
    # 5 Skylab: o Sol derrubou a estação e Esperance multou a NASA
    {
        "temas_secundarios": ["clima_tempo", "economia_curiosa"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Quando a estação Skylab caiu sobre a Austrália, em 1979, o condado de Esperance multou a NASA em 400 dólares australianos por jogar lixo. A multa foi paga em 2009, com dinheiro de ouvintes de uma rádio.",
        "explicacao": (
            "O Skylab, primeira estação espacial dos EUA, caiu antes do que a NASA esperava. Em 1973, o "
            "matemático britânico Desmond King-Hele previu a queda para 1979 por causa do aumento da atividade "
            "solar: um Sol mais ativo que o previsto aquece as camadas externas da atmosfera e aumenta o arrasto "
            "sobre o que está em órbita. Na reentrada, em julho de 1979, os controladores tentaram mirar o sul do "
            "Oceano Índico, com sucesso parcial. A estação não queimou tão rápido quanto se calculava e, por um "
            "erro de cálculo de quatro por cento, os destroços caíram numa área quase desabitada do oeste da "
            "Austrália. A queda virou evento de mídia, com apostas sobre hora e local, e um jornal de San "
            "Francisco prometeu 10 mil dólares a quem entregasse primeiro um pedaço da estação. Stan Thornton, que "
            "achou 24 fragmentos em casa, em Esperance, tirou o primeiro passaporte da vida e voou para buscar o "
            "prêmio. O condado de Esperance, em tom de brincadeira, multou a NASA em 400 dólares australianos por "
            "jogar lixo. A multa foi cancelada três meses depois, mas em abril de 2009 o radialista Scott Barley "
            "arrecadou o valor com os ouvintes do seu programa matinal e a pagou em nome da NASA."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Skylab",
            "Skylab was the United States' first space station launched by NASA [...] "
            "Before re-entry, NASA ground controllers tried to adjust Skylab's orbit to minimize the risk of debris landing in populated areas, targeting the south Indian Ocean, which was partially successful. [...] "
            "British mathematician Desmond King-Hele of the Royal Aircraft Establishment (RAE) predicted in 1973 that Skylab would de-orbit and crash to Earth in 1979, sooner than NASA's forecast, because of increased solar activity. "
            "Greater-than-expected solar activity heated the outer layers of Earth's atmosphere and increased drag on Skylab. [...] "
            "wagering on the time and place of re-entry, and nightly news reports. "
            "The San Francisco Examiner offered a US$10,000 prize (equivalent to $44,000 today) for the first piece of Skylab delivered to its offices [...] "
            "and re-entry began at approximately 16:37 UTC, July 11, 1979. The station did not burn up as fast as NASA expected. "
            "Debris landed about 300 miles (480 km) east of Perth, Western Australia due to a four-percent calculation error [...] "
            "the debris landed in an almost unpopulated area [...] "
            "Stan Thornton found 24 pieces of Skylab at his home in Esperance. After obtaining his first passport, Thornton flew to San Francisco. [...] "
            "he collected the Examiner prize [...] "
            "The Shire of Esperance light-heartedly fined NASA A$400 for littering, and while the fine was indeed written off three months later, "
            "it was nonetheless eventually paid on behalf of NASA in April 2009, after Scott Barley of Highway Radio raised the funds from his morning show listeners.",
            nome="Skylab")],
    },
    # 6 o espelho do Hubble e os "óculos"
    {
        "temas_secundarios": ["luz_cores", "falhas_engenharia"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "O espelho do Hubble foi polido com precisão extrema, mas no formato errado: a borda ficou plana demais por cerca de 2.200 nanômetros. Como o erro era exato, deu para corrigi-lo com \"óculos\" instalados no espaço.",
        "explicacao": (
            "O Hubble foi lançado em 1990 e logo se viu que tinha aberração esférica: a luz refletida na borda do "
            "espelho focava num ponto diferente da luz refletida no centro. O espelho estava entre os mais bem "
            "acabados já feitos, liso na escala de 10 nanômetros, mas sua borda estava cerca de 2.200 nanômetros "
            "mais plana do que devia. Uma comissão chefiada por Lew Allen, diretor do Jet Propulsion Laboratory, "
            "achou a origem: o corretor nulo refletivo, aparelho de teste que a fabricante Perkin-Elmer usou na "
            "etapa final do polimento, tinha sido montado com uma lente fora do lugar por 1,3 mm. Alguns testes "
            "com corretores convencionais chegaram a mostrar a aberração, mas foram descartados porque o aparelho "
            "novo era considerado mais preciso. Trocar o espelho em órbita era impossível, e trazer o telescópio "
            "de volta seria caro e demorado. Justamente por o espelho ter sido polido com tanta precisão na forma "
            "errada, deu para medir o erro e projetar componentes ópticos com exatamente o mesmo erro, no sentido "
            "oposto. Instalados por astronautas na missão de serviço STS-61, em 1993, eles funcionaram como "
            "óculos e devolveram ao telescópio a qualidade prevista no projeto."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Hubble_Space_Telescope",
            "Hubble was launched on STS-31 in 1990, but its main mirror had been ground incorrectly, resulting in spherical aberration that compromised the telescope's capabilities. "
            "The optics were corrected to their intended quality by a servicing mission, STS-61, in 1993. [...] "
            "Although it was believed to be one of the most precisely figured optical mirrors ever made, smooth to about 10 nanometers, the outer perimeter was too flat by about 2200 nanometers [...] "
            "This difference was catastrophic, introducing severe spherical aberration, a flaw in which light reflecting off the edge of a mirror focuses on a different point from the light reflecting off its center. [...] "
            "A commission headed by Lew Allen, director of the Jet Propulsion Laboratory, was established to determine how the error could have arisen. "
            "The Allen Commission found that a reflective null corrector, a testing device used to achieve a properly shaped non-spherical mirror, had been incorrectly assembled. "
            "(One lens was out of position by 1.3 mm (0.051 in).) [...] "
            "for the final manufacturing step (figuring), they switched to the custom-built reflective null corrector [...] "
            "During fabrication, a few tests using conventional null correctors correctly reported spherical aberration. "
            "But these results were dismissed, thus missing the opportunity to catch the error, because the reflective null corrector was considered more accurate. [...] "
            "it would have been impossible to replace the mirror in orbit, and too expensive and time-consuming to bring the telescope back to Earth for a refit. "
            "Instead, the fact that the mirror had been ground so precisely to the wrong shape led to the design of new optical components with exactly the same error but in the opposite sense, "
            "to be added to the telescope at the servicing mission, effectively acting as \"spectacles\" to correct the spherical aberration.",
            nome="Hubble Space Telescope")],
    },
    # 7 Disco de Ouro: relógio de urânio e ondas cerebrais
    {
        "temas_secundarios": ["musica_ciencia", "elementos_quimicos"],
        "tipos_espanto": ["engenhosidade", "conexao_inesperada"],
        "gancho": "O Disco de Ouro das Voyager leva na capa uma amostra de urânio-238 que serve de relógio para datá-lo. E guarda as ondas cerebrais de uma mulher que pensava, entre outras coisas, em como é se apaixonar.",
        "explicacao": (
            "As duas sondas Voyager, lançadas em 1977, carregam cópias idênticas de um disco de cobre de 30 cm "
            "banhado em ouro, com sons e imagens escolhidos para mostrar a diversidade da vida e da cultura na "
            "Terra a alguma forma de vida inteligente que os encontre. A capa traz instruções em desenho: um mapa "
            "com a posição do Sistema Solar em relação a 14 pulsares e um diagrama do átomo de hidrogênio, cuja "
            "transição entre os dois estados mais baixos serve de unidade de tempo. Nessa unidade, escrita em "
            "binário, a capa informa que o disco leva 3,6 segundos para dar uma volta. Sobre a capa de alumínio "
            "foi depositada uma amostra ultrapura de urânio-238, cuja meia-vida é de 4,468 bilhões de anos: pela "
            "proporção entre o urânio que restou e outros elementos, uma civilização poderia calcular a idade do "
            "disco. Entre peças de Bach, Mozart, Beethoven, Chuck Berry e de muitas culturas, há uma gravação de "
            "uma hora das ondas cerebrais de Ann Druyan, diretora criativa do projeto, comprimida num minuto de "
            "áudio. Enquanto era gravada, ela pensou na história da Terra, nas civilizações e seus problemas e em "
            "como é se apaixonar. A equipe também quis incluir \"Here Comes the Sun\", dos Beatles, mas a gravadora "
            "dona dos direitos recusou."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Voyager_Golden_Record",
            "The Voyager Golden Records are two identical phonograph records, with one copy aboard each of the two Voyager spacecraft launched in 1977. "
            "The records contain sounds and data to reconstruct raster scan images selected to portray the diversity of life and culture on Earth, "
            "and are intended for any intelligent extraterrestrial life form who may find them. [...] "
            "featuring works by composers such as J. S. Bach, Mozart, Beethoven and Stravinsky. "
            "The disc also includes music by Guan Pinghu, Blind Willie Johnson, Louis Armstrong, Chuck Berry [...] "
            "Ann Druyan as creative director [...] "
            "The Golden Record also carries an hour-long recording of the brainwaves of Ann Druyan, compressed into a minute of audio. "
            "During the recording of the brainwaves, Druyan thought of many topics, including Earth's history, civilizations and the problems they face, and what it was like to fall in love. [...] "
            "Sagan's team wanted to include the Beatles 1969 song \"Here Comes the Sun\" on the record, but the record company EMI, which held the copyrights, declined. [...] "
            "The record is a copper disk 12 inches (30 cm) in diameter plated first with nickel and then gold. "
            "The record's cover is aluminum and electroplated upon it is an ultra-pure sample of the isotope uranium-238. "
            "Uranium-238 has a half-life of 4.468 billion years. "
            "It is possible (e.g., via mass spectrometry) that a civilization that encounters the record will be able to use the ratio of remaining uranium to the other elements to determine the age of the record. [...] "
            "Written around it in binary notation is the correct time of one rotation of the record, 3.6 seconds, expressed in time units of 0.70 billionths of a second, "
            "the time period associated with the radiation emitted or absorbed by a fundamental transition of the hydrogen atom. [...] "
            "It shows the location of the Solar System with respect to 14 pulsars, whose precise periods are given. "
            "The drawing containing two circles in the lower right-hand corner is a drawing of the hydrogen atom in its two lowest states, "
            "with a connecting line and digit 1 to indicate that the time interval associated with the transition from one state to the other is to be used as the fundamental time scale",
            nome="Voyager Golden Record")],
    },
    # 8 Ingenuity: o tecido do avião dos Wright e o aeroporto JZRO
    {
        "temas_secundarios": ["transportes", "sistema_solar"],
        "tipos_espanto": ["conexao_inesperada", "engenhosidade"],
        "gancho": "O helicóptero Ingenuity, que voou em Marte, levava um pedacinho do tecido da asa do avião dos irmãos Wright, de 1903. E a área de onde decolou ganhou da aviação civil um código de aeroporto: JZRO.",
        "explicacao": (
            "O Ingenuity fez seu primeiro voo em 19 de abril de 2021, o primeiro voo motorizado e controlado de "
            "uma aeronave fora da Terra. A NASA e o JPL o chamaram de seu \"momento irmãos Wright\", em referência "
            "ao primeiro voo bem-sucedido de um avião motorizado. Para marcar a ligação, um pedacinho do tecido da "
            "asa do Wright Flyer, de 1903, foi preso a um cabo sob o painel solar do helicóptero. Não era a "
            "primeira vez: em 1969, Neil Armstrong levou à Lua, no módulo lunar Eagle, um artefato semelhante do "
            "mesmo avião. A área de decolagem e pouso em Marte foi batizada de Campo Irmãos Wright, e a OACI, a "
            "agência da ONU para aviação civil, deu a ela o código JZRO, de cratera Jezero. Voar ali é difícil: o "
            "ar de Marte tem cerca de 1/100 da densidade do ar terrestre ao nível do mar, o mesmo que a 27 mil "
            "metros de altitude, onde nenhum helicóptero jamais chegou. Por isso, as pás precisavam girar entre "
            "2.400 e 2.900 rotações por minuto, cerca de dez vezes mais rápido do que na Terra. Planejado para "
            "apenas cinco voos, o Ingenuity fez 72 em quase três anos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Ingenuity_(helicopter)",
            "Ingenuity made its first flight on 19 April 2021, demonstrating that flight is possible in the extremely thin atmosphere of Mars, "
            "and became the first aircraft to conduct a powered and controlled extraterrestrial flight. [...] "
            "Originally intended to make only five flights, Ingenuity completed 72 flights over the course of nearly three years. [...] "
            "The planet's atmospheric density is about 1⁄100 that of Earth's at sea level, or about the same as at 27,000 m (87,000 ft), an altitude never reached by existing helicopters. [...] "
            "To keep Ingenuity aloft, its specially shaped blades of enlarged size must rotate between 2400 and 2900 rpm, or about 10 times faster than what is needed on Earth. [...] "
            "NASA and JPL officials described the first Mars Ingenuity helicopter flight as their \"Wright Brothers moment\", by analogy to the first successful powered airplane flight on Earth. "
            "A small piece of the wing cloth from the Wright brothers' 1903 Wright Flyer is attached to a cable underneath Ingenuity's solar panel. "
            "In 1969, Apollo 11's Neil Armstrong carried a similar Wright Flyer artifact to the Moon in the Lunar Module Eagle. "
            "NASA named Ingenuity's first take-off and landing airstrip Wright Brothers Field, which the UN agency ICAO gave an airport code of JZRO for Jezero Crater",
            nome="Ingenuity (helicopter)")],
    },
    # 9 o mito da caneta espacial contra o lápis
    {
        "temas_secundarios": ["invencoes", "guerra_fria"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "É falsa a história da NASA gastando milhões numa caneta espacial enquanto os russos usavam lápis. A caneta foi criada com dinheiro privado, e os soviéticos acabaram comprando o mesmo modelo.",
        "explicacao": (
            "A lenda diz que a NASA gastou uma fortuna para criar uma caneta que escrevesse sem gravidade, enquanto "
            "os soviéticos resolveram tudo com lápis. Na verdade, a NASA também usava lápis: há um pedido de "
            "lapiseiras de 1965. Só que o lápis é um problema no espaço: pontas quebradas e pó de grafite "
            "flutuando ameaçam a eletrônica, a madeira pega fogo, e anotações que borram ou se apagam não servem "
            "como registro. A Space Pen foi desenvolvida com capital privado: a tinta especial custou a Paul Fisher "
            "cerca de 1 milhão de dólares, e a NASA nunca encomendou a caneta nem a financiou. Fisher a inventou "
            "por conta própria e, em 1965, pediu à agência que a testasse. Depois de muitos testes, ela foi "
            "adotada nas missões Apollo, e em 1967 noticiou-se que a NASA comprou cerca de 400 unidades a 2,95 "
            "dólares cada. O truque está no cartucho selado, em que nitrogênio comprimido empurra a tinta, o que "
            "permite escrever em qualquer ângulo. Os cosmonautas soviéticos usavam lápis e lápis dermatográficos "
            "em pranchetas de plástico até 1969, quando também adotaram a caneta, com uma compra de 100 unidades."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Space_pen",
            "An urban legend states that NASA spent a large amount of money to develop a pen that would write in space (the result purportedly being the Fisher Space Pen), while the Soviets just used pencils. [...] "
            "However, the claim that NASA spent millions on the Space Pen is incorrect, as the Fisher pen was developed using private capital, not government funding. "
            "The development of the thixotropic ink cost Paul Fisher around $1 million [...] "
            "NASA programs previously used pencils (as demonstrated by an order in 1965 for mechanical pencils) but because of the substantial dangers that broken pencil tips and graphite dust pose to electronics in zero gravity, "
            "the flammable nature of wood present in pencils, and the inadequate quality documentation produced by non-permanent or smeared recordkeeping, a better solution was needed. "
            "Soviet cosmonauts used pencils, and grease pencils on plastic slates until also adopting a space pen in 1969 with a purchase of 100 units for use on all future missions. "
            "NASA never approached Paul Fisher to develop a pen, nor did Fisher receive any government funding for the pen's development. "
            "Fisher invented it independently and then, in 1965, asked NASA to try it. "
            "After extensive testing, NASA decided to use the pens in future Apollo missions. "
            "Subsequently, in 1967 it was reported that NASA purchased approximately 400 pens for $2.95 apiece [...] "
            "The ink is forced out by compressed nitrogen at a pressure of nearly 310 kPa [...] "
            "The pen can write without the help of gravity, at any angle.",
            nome="Space pen")],
    },
    # 10 do "Flopnik" ao objeto mais antigo em órbita
    {
        "temas_secundarios": ["guerra_fria", "energia"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Em 1957, o primeiro foguete dos EUA a tentar pôr um satélite em órbita subiu cerca de um metro e explodiu: virou o \"Flopnik\". O satélite do mesmo programa lançado em 1958 é o objeto artificial mais antigo em órbita.",
        "explicacao": (
            "Depois dos Sputnik 1 e 2, os Estados Unidos tentaram responder com o Vanguard TV-3, em 6 de dezembro "
            "de 1957. Uns dois segundos após a decolagem, o foguete perdeu empuxo, voltou a cair sobre a "
            "plataforma e explodiu. O pequeno satélite foi arremessado e parou no chão ali perto, ainda emitindo "
            "seu sinal de rádio. Os jornais brincaram com o nome do Sputnik e falaram em \"Flopnik\", \"Kaputnik\" e "
            "\"Stayputnik\", a Bolsa de Nova York suspendeu por um tempo a negociação das ações da principal "
            "fabricante, e um delegado soviético na ONU perguntou se os EUA tinham interesse em receber ajuda "
            "reservada a países subdesenvolvidos. Em março de 1958, o Vanguard 1 enfim chegou à órbita. Era uma "
            "esfera de alumínio de 1,46 kg, que Khrushchev chamou de \"satélite toranja\", e o primeiro satélite "
            "com energia solar: seu transmissor ligado a células solares funcionou por mais de seis anos. O "
            "contato acabou em 1964, mas ele continua lá, junto com o estágio superior do foguete: são os objetos "
            "artificiais mais antigos ainda em órbita. A previsão inicial era de 2 mil anos em órbita; a pressão "
            "da radiação solar e o arrasto da atmosfera em períodos de Sol ativo reduziram a estimativa para cerca "
            "de 240 anos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Vanguard_TV-3",
                "Vanguard TV-3 (also called Vanguard Test Vehicle-Three), was the first attempt of the United States to launch a satellite into orbit around the Earth, after the successful Soviet launches of Sputnik 1 and Sputnik 2. [...] "
                "At its launch attempt on 6 December 1957, at Cape Canaveral Air Force Station, the booster ignited and began to rise, but about two seconds after liftoff, after rising about 1.2 m (four feet), "
                "the rocket lost thrust and fell back to the launch pad. As it settled, the fuel tanks ruptured and exploded, destroying the rocket and severely damaging the launch pad. "
                "The Vanguard 1A satellite was thrown clear and landed on the ground a short distance away with its transmitters still sending out a beacon signal. [...] "
                "After the launch failure, trading in the stock of the Martin Company, the prime contractor for the project, was temporarily suspended by the New York Stock Exchange. "
                "Newspapers in the United States published prominent headlines and articles describing the failure with plays on the name of the Russian satellite, Sputnik, such as \"Flopnik\", \"Kaputnik\", \"Oopsnik\", \"Dudnick\"  and \"Stayputnik\". [...] "
                "A few days after the incident, a Soviet delegate to the United Nations inquired whether the United States was interested in receiving aid earmarked for \"undeveloped countries\".",
                nome="Vanguard TV-3"),
            wiki("Vanguard_1",
                "It was launched 17 March 1958. Vanguard 1 was the first satellite to have solar electric power. "
                "Although communications with the satellite were lost in 1964, it remains the oldest artificial object still in orbit, together with the upper stage of its launch vehicle. [...] "
                "was described by the Soviet Premier, Nikita Khrushchev, as \"the grapefruit satellite\". [...] "
                "The spacecraft is a 1.46 kg (3.2 lb) aluminum sphere [...] "
                "Original estimates had the orbit lasting for 2,000 years, but it was discovered that solar radiation pressure and atmospheric drag during high levels of solar activity produced significant perturbations in the perigee height of the satellite, "
                "which caused a significant decrease in its expected lifetime to about 240 years. [...] "
                "The solar-cell-powered transmitter operated for more than six years.",
                nome="Vanguard 1"),
        ],
    },
    # 11 o acidente do VLS em Alcântara (2003)
    {
        "temas_secundarios": ["brasil_republica", "falhas_engenharia"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Em 2003, um motor do foguete brasileiro VLS-1 teve uma ignição não planejada na plataforma de Alcântara e matou 21 pessoas. É oficialmente o quarto desastre mais mortal da exploração espacial.",
        "explicacao": (
            "O VLS-1 deveria pôr dois satélites em órbita. As tentativas anteriores, em 1997 e 1999, tinham "
            "falhado em voo. Na terceira, em 22 de agosto de 2003, dias antes da data marcada para o lançamento, "
            "um dos motores do primeiro estágio pegou fogo enquanto havia gente trabalhando nos cinco andares da "
            "torre móvel de integração. Em cerca de oito segundos, a torre foi envolvida por fumaça e gases a até "
            "3.000 °C, e ela desabou cinco minutos depois. As normas de segurança permitiam só seis pessoas na "
            "área naquele tipo de atividade, mas havia muito mais. Contra o regulamento, o sistema de ignição tinha "
            "sido instalado em dois motores na manhã do acidente, embora o cronograma o previsse para o dia "
            "seguinte. O relatório final, apresentado em 2004 com a participação de especialistas russos, apontou "
            "a descarga eletrostática como a hipótese mais forte e não identificou nenhum erro ou violação que "
            "tivesse causado o acidente diretamente. Mas citou a verba limitada e a falta de pessoal como fatores "
            "que contribuíram. O acidente atrasou muito o programa espacial brasileiro, e o projeto do VLS-1 foi "
            "encerrado pela Agência Espacial Brasileira em 2016."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [
            wiki("2003_Alcântara_VLS_accident",
                "was an accident during the Brazilian Space Agency's third attempt to launch the VLS-1 rocket, which was intended to launch two satellites into orbit. "
                "The rocket ignited on its launch pad at the Alcântara Launch Center, killing 21 people. "
                "It is officially the fourth deadliest space exploration related disaster in history. [...] "
                "The rocket, proposed in 1979 had two launch attempts until the accident: one in 1997, which ended up in the Atlantic Ocean due to the failure of one of the first stage engines to start "
                "and another in 1999, destroyed remotely due to a flame penetrating the top of the second stage block after takeoff. [...] "
                "The accident occurred three days before the scheduled launch date, at 1:26:06 pm (Brasília time) on August 22, 2003, "
                "between frames 26 and 27 recorded by the Closed Circuit TV of the Mobile Integration Tower, with professionals spread across the five floors of the tower. [...] "
                "An unplanned ignition, which began in a first-stage engine that caught fire after ignition, destroyed the launch vehicle while it was on the CLA launch pad. [...] "
                "It took about eight seconds before the tower was enveloped by smoke and gases heated up to 3,000 °C. The mobile tower stood upright for five minutes, collapsing at 1:31. [...] "
                "However, the number of people at the base was well above safety standards, which allowed for only six people to be present. "
                "The accident significantly delayed the Brazilian space program. "
                "It was later revealed that, contrary to the regulations, on the morning of the 22nd, the ignition system was installed in only two engines, even though the schedule indicated that this should have been done on the 23rd [...] "
                "The report was presented by the ministers of Defense and Science on 16 March 2004. "
                "The conclusion of both the Brazilian and Russian investigators was that the cause of the accident was due to the unplanned start of the A-booster. [...] "
                "The electrostatic discharge hypothesis was found to be superior [...] "
                "Overall, the report did not identify any \"active failure\" (error or violation) that caused the accident. "
                "However, it cited limited funding and a shortage of staff as contributing factors to the incident.",
                nome="2003 Alcântara VLS accident"),
            wiki("VLS-1",
                "The 2003 Alcântara VLS accident caused a considerable setback to the Brazilian space program. [...] "
                "The project was terminated by Brazilian Space Agency in 2016.",
                nome="VLS-1"),
        ],
    },
    # 12 Apollo 12: dois raios e o "SCE to Aux"
    {
        "temas_secundarios": ["eletromagnetismo", "clima_tempo"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "A Apollo 12 foi atingida por dois raios logo depois de decolar, em 1969, e o painel se encheu de alertas. Um controlador lembrou de um teste antigo e sugeriu uma chave obscura: \"SCE to Aux\". Funcionou.",
        "explicacao": (
            "O lançamento foi num dia chuvoso, sob céu totalmente encoberto. Aos 36,5 segundos de voo, um raio, "
            "desencadeado pelo próprio foguete, atingiu o Saturno V. A descarga desligou as três células de "
            "combustível, e a nave ficou dependendo de baterias que não davam conta da demanda. Um segundo raio, "
            "aos 52 segundos, derrubou o indicador de atitude. Os dados que chegavam a Houston viraram uma "
            "confusão, e os astronautas viam o painel cheio de luzes de alerta sem saber o que estava errado. O "
            "foguete seguia normalmente, porque seu sistema de guiagem funcionava de forma independente da nave. "
            "No controle da missão, John Aaron reconheceu o padrão de falha de um teste anterior e pediu para "
            "passar o condicionador de sinais, o SCE, para a alimentação reserva. Nem o diretor de voo nem o "
            "comandante Pete Conrad sabiam que chave era essa; Alan Bean, o engenheiro da nave, sabia onde ficava "
            "e a acionou. A telemetria voltou e mostrou que não havia pane grave. Sobrou um temor, que não foi "
            "contado à tripulação: o raio podia ter danificado os parafusos explosivos que abriam o compartimento "
            "dos paraquedas. Como abortar não mudaria esse risco, a missão seguiu. No fim, os paraquedas abriram "
            "normalmente."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Apollo_12",
            "It was launched on November 14, 1969, by NASA from the Kennedy Space Center in Florida [...] "
            "Commander Charles \"Pete\" Conrad and Lunar Module Pilot Alan L. Bean [...] "
            "Shortly after being launched on a rainy day at Kennedy Space Center, Apollo 12 was twice struck by lightning, causing instrumentation problems but little damage. [...] "
            "There were completely overcast rainy skies [...] "
            "Lightning struck the Saturn V 36.5 seconds after lift-off, triggered by the vehicle itself. "
            "The static discharge caused a voltage transient that knocked all three fuel cells offline, meaning the spacecraft was being powered entirely from its batteries, which could not supply enough current to meet demand. "
            "A second strike at 52 seconds knocked out the \"8-ball\" attitude indicator. "
            "The telemetry stream at Mission Control was garbled, but the Saturn V continued to fly normally; "
            "the strikes had not affected the Saturn V instrument unit guidance system, which functioned independently from the CSM. "
            "The astronauts unexpectedly had a board red with caution and warning lights, but could not tell exactly what was wrong. "
            "The Electrical, Environmental and Consumables Manager (EECOM) in Mission Control, John Aaron, remembered the telemetry failure pattern from an earlier test "
            "when a power loss caused a malfunction in the CSM signal conditioning electronics (SCE) [...] "
            "Aaron made a call, \"Flight, EECOM. Try SCE to Aux\", to switch the SCE to a backup power supply. "
            "The switch was fairly obscure, and neither Flight Director Gerald Griffin, CAPCOM Gerald P. Carr, nor Conrad knew what it was; "
            "Bean, who as LMP was the spacecraft's engineer, knew where to find it and threw the switch, after which the telemetry came back online, revealing no significant malfunctions. [...] "
            "Initially, it was feared that the lightning strike could have damaged the explosive bolts that opened the Command Module's parachute compartment. "
            "The decision was made not to share this with the astronauts and to continue with the flight plan, "
            "since they would die if the parachutes failed to deploy, whether following an Earth-orbit abort or upon a return from the Moon, so nothing was to be gained by aborting. "
            "The parachutes deployed and functioned normally at the end of the mission.",
            nome="Apollo 12")],
    },
    # 13 os trajes da Apollo e a fábrica de sutiãs
    {
        "temas_secundarios": ["moda", "invencoes"],
        "tipos_espanto": ["origem_inesperada", "historia_humana"],
        "gancho": "Os trajes que os astronautas da Apollo usaram na Lua foram feitos por uma divisão da Playtex, fabricante de sutiãs. Costureiras trabalhavam com tolerância de menos de 1/64 de polegada por ponto.",
        "explicacao": (
            "A International Latex Corporation, fundada em 1932 e mais tarde conhecida como Playtex, ficou famosa "
            "pelas roupas íntimas femininas. Uma divisão dela, sediada em Dover, nos EUA, fazia capacetes e trajes "
            "pressurizados para grandes altitudes. Em 1965, essa divisão ganhou o contrato do traje lunar da "
            "Apollo graças ao seu jeito de fazer juntas flexíveis em trajes cheios de ar. Segundo a revista "
            "Smithsonian, a equipe, liderada por um mecânico de automóveis e um ex-técnico de televisão, entrou na "
            "concorrência por conta própria e passou seis semanas trabalhando dia e noite, até criar um traje que "
            "superou com folga os dois concorrentes convidados. Parte das costureiras veio da divisão Playtex; outras, "
            "de fábricas de roupas e malas da região. Elas tiveram de aprender a trabalhar devagar, com tecidos "
            "novos e com regras de engenharia da NASA muito mais rígidas que as da confecção comum: o desvio "
            "tolerado nas costuras era menor que 1/64 de polegada. Cada traje era feito sob medida, e para cada um "
            "dos 12 voos tripulados a empresa produziu 15. Hoje, mais de 300 trajes espaciais, entre eles o de "
            "Neil Armstrong, estão no acervo do Museu Nacional do Ar e do Espaço, envoltos em musselina para "
            "absorver o ácido clorídrico que liberam."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("ILC_Dover",
                "ILC outfitted every United States astronaut in the Apollo program, including the twelve that walked on the Moon. [...] "
                "ILC Dover initially formed as a branch of the International Latex Corporation,  the company founded in 1932 by Abram Spanel and later known as Playtex best known for manufacture of women's undergarments. [...] "
                "Located at that time in Dover, Delaware, ILC's earliest work was on high-altitude pressure helmets and high-altitude pressure suits for the U.S Navy and Air Force. "
                "In 1965, ILC (then known as the Government and Industrial Division of the International Latex Corporation) was awarded the prime contract for the Apollo Lunar Space Suit, "
                "based on its unique approach to designing flexible joints in air filled suits. [...] "
                "Apollo spacesuits were custom-made for each of the astronauts in the program, and for each of the 12 crewed flights carried out, ILC produced 15 suits.",
                nome="ILC Dover"),
            wiki("ILC_Dover_seamstresses",
                "Some of the women had been recruited from the Playtex division of ILC, while other came from nearby clothing and luggage manufacturers. [...] "
                "However to succeed at ILC, the women had to be willing to learn new sewing techniques, perform their tasks at a slow pace, work with novel textiles, and perform to exacting standards. [...] "
                "The production line at ILC followed NASA-mandated engineering guidelines that were significantly stricter than typical clothing manufacturing processes. "
                "Tolerance for variation in the stitches were less than 1/64 of an inch from the seam.",
                nome="ILC Dover seamstresses"),
            {"url": "https://www.smithsonianmag.com/legacy_blog/what-did-playtex-have-to-do-with-neil-armstrong/",
             "titulo": "What Did Playtex Have to Do With Neil Armstrong? (Smithsonian Magazine)", "idioma": "en",
             "trecho": "Over 300 spacesuits, including the one Armstrong wore on the Apollo 11 mission, are in the Smithsonian collection at the National Air and Space Museum. "
                       "They are lovingly cared for, conserved and covered in muslin (to absorb the hydrochloric acid the suits emit) [...] "
                       "was a product of the industrial division of the women’s bra manufacturer Playtex. [...] "
                       "ILC’s team , a motley group of seamstresses and engineers, led by a car mechanic and a former television repairman, "
                       "manages to convince NASA to let them enter their “test suit” in a closed, invitation-only competitive bid at their own expense. "
                       "They spend six weeks working around the clock—at times breaking into their own offices to work 24-hour shifts—to arrive at a suit solution that starkly outperforms the two invited competitors."},
        ],
    },
    # 14 a anomalia das Pioneer era calor
    {
        "temas_secundarios": ["termodinamica", "sistema_solar"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Por anos, as sondas Pioneer 10 e 11 frearam um pouco mais do que a gravidade explicava, e houve quem propusesse mudar as leis da física. A culpa era do calor da própria nave, irradiado mais para um lado.",
        "explicacao": (
            "As duas sondas, lançadas em 1972 e 1973, estão saindo do Sistema Solar, freadas aos poucos pela "
            "gravidade do Sol. Depois de passarem de cerca de 20 unidades astronômicas, os dados de navegação "
            "mostraram que elas freavam um pouquinho além do esperado, o equivalente a perder 1 km/h de velocidade "
            "a cada dez anos. A diferença foi notada já em 1980, mas só passou a ser investigada a sério em 1994. "
            "As propostas iam de causas banais, como erro de medida, vazamento de gás ou calor irradiado de forma "
            "desigual, até \"física nova\", com mudanças na gravitação, como a hipótese MOND. Uma explicação "
            "gravitacional esbarrava num problema: o efeito não aparecia nas órbitas dos planetas externos. Entre "
            "1998 e 2012, uma explicação se firmou. Cada sonda é alimentada por um gerador a radioisótopo e, "
            "cercada de vácuo, só consegue perder calor por radiação. Se o formato da nave faz o calor sair mais "
            "para um lado, o recuo dos fótons térmicos empurra a sonda de leve no sentido oposto. Em 2012, "
            "vários grupos refizeram com cuidado as contas dessas forças térmicas e mostraram que elas explicam "
            "a anomalia inteira: a causa é banal e não exige mudar as leis da física."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Pioneer_anomaly",
            "The Pioneer anomaly, or Pioneer effect, was the observed deviation from predicted accelerations of the Pioneer 10 and Pioneer 11 spacecraft after they passed about 20 astronomical units [...] "
            "has been subsequently explained by anisotropic radiation pressure caused by the spacecraft's heat loss. "
            "Both Pioneer spacecraft are escaping the Solar System but are slowing under the influence of the Sun's gravity. "
            "Upon very close examination of navigational data, the spacecraft were found to be slowing slightly more than expected. [...] "
            "which is equivalent to a reduction of the outbound velocity by 1 km/h over a period of ten years. "
            "The two spacecraft were launched in 1972 and 1973. The anomalous acceleration was first noticed as early as 1980 but not seriously investigated until 1994. [...] "
            "Over the period from 1998 to 2012, one particular explanation became accepted. "
            "The spacecraft, which are surrounded by an ultra-high vacuum and are each powered by a radioisotope thermoelectric generator (RTG), can shed heat only via thermal radiation. "
            "If, due to the design of the spacecraft, more heat is emitted in a particular direction by what is known as a radiative anisotropy, "
            "then the spacecraft would accelerate slightly in the direction opposite of the excess emitted radiation due to the recoil of thermal photons. [...] "
            "By 2012, several papers by different groups, all reanalyzing the thermal radiation pressure forces inherent in the spacecraft, showed that a careful accounting of this explains the entire anomaly; "
            "thus the cause is mundane and does not point to any new phenomenon or need to update the laws of physics. [...] "
            "other proposed explanations fell into two classes –\"mundane causes\" or \"new physics\". "
            "Mundane causes include conventional effects that were overlooked or mis-modeled in the initial analysis, such as measurement error, thrust from gas leakage, or uneven heat radiation. "
            "The \"new physics\" explanations proposed revision of our understanding of gravitational physics. [...] "
            "However, this acceleration does not show up in the orbits of the outer planets [...] "
            "MOND hypothesis proposed that the force of gravity deviates from the traditional Newtonian value",
            nome="Pioneer anomaly")],
    },
    # 15 Korolev, o Projetista-Chefe sem nome
    {
        "temas_secundarios": ["guerra_fria", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "O engenheiro por trás do Sputnik e do voo de Gagarin era apresentado só como \"projetista-chefe\": nem alguns cosmonautas sabiam seu nome. Anos antes, ele perdera a maioria dos dentes num campo do Gulag.",
        "explicacao": (
            "Sergei Korolev dirigiu o desenvolvimento do R-7, o primeiro míssil balístico intercontinental do "
            "mundo, e versões dele lançaram o Sputnik 1, a cadela Laika e o voo de Iuri Gagarin. Antes disso, em "
            "1938, durante o Grande Expurgo de Stálin, ele foi preso com acusações depois reconhecidas como "
            "falsas. Chegou a ser condenado à morte, pena trocada por trabalhos forçados, e passou quase seis anos "
            "entre prisões e campos. Em Kolyma, no extremo leste da Sibéria, trabalhou meses numa mina de ouro e "
            "perdeu a maior parte dos dentes por escorbuto. Depois, com a ajuda do antigo mentor Andrei Tupolev, "
            "foi transferido para uma prisão onde cientistas e engenheiros trabalhavam em projetos do Estado. "
            "Na era espacial, os nomes dos chefes do programa soviético viraram segredo: o relatório sobre o "
            "Sputnik 1 saiu anônimo no Pravda, e Korolev escrevia artigos como \"Professor K. Sergeyev\". Em público, "
            "era só o \"projetista-chefe\", em parte para protegê-lo de atentados durante a Guerra Fria. Sua "
            "identidade só foi revelada depois que ele morreu, em 1966. Segundo uma das versões sobre a morte, "
            "durante uma cirurgia os médicos não conseguiram intubá-lo porque as mandíbulas dele, feridas no "
            "Gulag, não tinham se recuperado direito."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Sergei_Korolev",
            "Korolev directed development of the R-7 rocket, the world's first intercontinental ballistic missile (ICBM) and was a leader in the Soviet space programme which used modified versions of the R-7 for several notable achievements. "
            "Under his leadership, the Soviet Union launched Sputnik 1, the first artificial satellite; Laika, the first animal to orbit Earth; [...] "
            "He also directed the missions that carried Yuri Gagarin into space aboard Vostok 1 [...] "
            "In 1938 he was arrested during the Great Purge on charges later shown to be false and spent nearly six years in prison and labour camps, including several months in Kolyma. "
            "Prior to his imprisonment, Korolev had been initially condemned to be executed under Joseph Stalin's orders among 74 military specialists and engineers before his sentence was commuted to hard prison labour. [...] "
            "During his lifetime, Korolev was publicly identified only as glavny konstruktor (главный конструктор; lit. 'chief designer'), partly to protect him from possible assassination attempts during the Cold War. "
            "Even some cosmonauts who worked with him did not know his name. "
            "His identity was publicly disclosed only after his death in 1966 [...] "
            "Korolev was on his way from prison to a Gulag forced labour camp in Kolyma in the far east of Siberia, where he spent several months in a gold mine before word reached him of his retrial. [...] "
            "Korolev sustained injuries, including possibly a heart attack and lost most of his teeth from scurvy before being returned to Moscow in late 1939. [...] "
            "However, due to the intervention by his old mentor, Andrei Tupolev, he was relocated to a prison for scientists and engineers in September 1940. [...] "
            "For security reasons, the names of chief individuals in the Soviet space program became a secret. "
            "They were allowed to prepare a report detailing the design and construction of Sputnik 1, however, which was published anonymously by Pravda on 9 October. "
            "Korolev also began writing other articles under the pseudonym \"Professor K. Sergeyev\". [...] "
            "Doctors tried to provide intubation to allow him to breathe freely, but his jaws, injured during his time in a Gulag, had not healed properly and impeded the installation of the breathing tube.",
            nome="Sergei Korolev")],
    },
    # 16 Snoopy, o módulo da Apollo 10 que não podia pousar
    {
        "temas_secundarios": ["asteroides_cometas", "guerra_fria"],
        "tipos_espanto": ["historia_humana", "misterio_aberto"],
        "gancho": "Em 1969, o módulo lunar da Apollo 10 desceu a 15,6 km da Lua sem poder pousar: tinha só metade do combustível para voltar. Depois foi mandado para uma órbita em torno do Sol, e talvez tenha sido reencontrado.",
        "explicacao": (
            "A NASA descreveu a Apollo 10 como o \"ensaio geral\" do primeiro pouso, feito dois meses depois pela "
            "Apollo 11. O módulo lunar, chamado Snoopy, levou Stafford e Cernan até 15,6 km da superfície. Pousar "
            "estava fora de questão: segundo um dirigente da NASA, aquele módulo era um modelo antigo, pesado "
            "demais para decolar da Lua e voltar à nave-mãe. Além disso, o estágio de subida levava só o "
            "combustível que sobraria depois de uma decolagem real, cerca de metade do necessário. Cernan contou "
            "depois que havia quem pensasse: não deem a esses caras a chance de pousar, porque eles podem pousar. "
            "Depois do reencontro com o módulo de comando, chamado Charlie Brown, o combustível restante do Snoopy "
            "foi queimado para mandá-lo a uma órbita em torno do Sol, destino único entre os módulos lunares da "
            "Apollo. A órbita deixou de ser acompanhada depois de 1969. Em 2011, astrônomos amadores britânicos "
            "começaram a procurá-lo e, em 2019, a Royal Astronomical Society anunciou uma possível redescoberta: "
            "o pequeno asteroide 2018 AV2 seria o Snoopy, com \"98%\" de certeza. Se for, é a única nave que já "
            "levou tripulantes e que segue vagando pelo espaço vazia."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Apollo_10",
            "NASA, the mission's operator, described it as a \"dress rehearsal\" for the first Moon landing (Apollo 11, two months later). [...] "
            "The mission's call signs were the names of the Peanuts characters Charlie Brown for the CSM and Snoopy for the LM [...] "
            "The ascent stage was loaded with the amount of fuel and oxidizer it would have had remaining if it had lifted off from the surface and reached the altitude at which the Apollo 10 ascent stage fired; "
            "this was only about half the total amount required for lift off and rendezvous with the CSM. [...] "
            "Nelson quoted Cernan as saying \"A lot of people thought about the kind of people we were: 'Don't give those guys an opportunity to land, 'cause they might!' "
            "So the ascent module, the part we lifted off the lunar surface with, was short-fueled. The fuel tanks weren't full. "
            "So had we literally tried to land on the Moon, we couldn't have gotten off.\" "
            "Mueller, NASA's Associate Administrator for Manned Space Flight, stated, [...] "
            "It was an early design that was too heavy for a lunar landing, or, to be more precise, too heavy to be able to complete the ascent back to the command module. [...] "
            "Cernan and Stafford surveyed ALS-2, coming within 15.6 kilometers (8.4 nautical miles; 9.7 miles) of the surface [...] "
            "The rest of the LM's ascent-stage engine fuel was burned to send it on a trajectory past the Moon and into a heliocentric orbit. "
            "It was the only Apollo LM to meet this fate. [...] "
            "Snoopy's ascent stage orbit was not tracked after 1969, and its whereabouts were unknown. "
            "In 2011, a group of amateur astronomers in the UK started a project to search for it. "
            "In June 2019, the Royal Astronomical Society announced a possible rediscovery of Snoopy, determining that small Earth-crossing asteroid 2018 AV2 is likely to be the spacecraft with \"98%\" certainty. "
            "It is the only once-crewed spacecraft known to still be in outer space without a crew.",
            nome="Apollo 10")],
    },
]
