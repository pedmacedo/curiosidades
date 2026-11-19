LOTE = "2026-11-18-olimpiadas-01"
AREA = "esportes_jogos"
TEMA = "olimpiadas"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Kanakuri e a maratona de 54 anos
    {
        "temas_secundarios": ["limites_humanos", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Na maratona olímpica de 1912, o japonês Shizo Kanakuri largou a prova no meio e voltou para casa sem avisar ninguém. Em 1967, ele voltou a Estocolmo para terminar: tempo oficial de 54 anos e 8 meses.",
        "explicacao": (
            "Kanakuri foi o primeiro atleta do Japão a se classificar para uma Olimpíada. A viagem até a Suécia "
            "levou 18 dias, de navio e depois pela Ferrovia Transiberiana, e ele chegou fraco, sem conseguir "
            "dormir nas noites claras do verão sueco e com dificuldade para comer. A maratona foi disputada sob "
            "uma onda de calor: dezenas de corredores desistiram, e Francisco Lázaro desmaiou no percurso e "
            "morreu, a primeira morte da história olímpica. Com hipertermia, Kanakuri saiu da pista, entrou numa "
            "festa no jardim de uma casa e passou uma hora bebendo suco de laranja. Envergonhado, embarcou de "
            "volta ao Japão sem comunicar os organizadores. Ainda correu as maratonas olímpicas de 1920 e 1924. "
            "Décadas depois, um repórter sueco o achou dando aulas de geografia, e a televisão sueca o convidou "
            "a completar a prova. Em 20 de março de 1967, ele cruzou a linha. O tempo, de 54 anos, 8 meses, 6 "
            "dias, 5 horas e alguns minutos, está no Guinness como a maratona mais demorada já concluída. "
            "Kanakuri brincou que, no caminho, tinha se casado e tido seis filhos e dez netos."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Shizo_Kanakuri",
            "He holds the Guinness World Record for the longest time to complete a marathon with a time of 54 years 8 months 6 days 5 hours 32 minutes 20.3 seconds. "
            "Kanakuri retired from the men's marathon event at the 1912 Stockholm Olympics without informing the authorities, but Sveriges Television gave him the opportunity to complete his marathon in 1967. [...] "
            "Kanakuri was the first Japanese athlete to qualify for an Olympics. He embarked on a difficult 18-day-long trip to Stockholm, first by ship and then by train all through the Trans-Siberian Railway. "
            "When he finally arrived in Stockholm, Kanakuri was weak from the long journey. To make matters worse, he struggled to sleep during the white nights, and he had problems with the local food. [...] "
            "The race was held near Stockholm amidst a heat wave. Throughout the race, dozens of competitors dropped out, including runner Francisco Lázaro, whose mid-race collapse and subsequent death made him the first Olympic fatality. [...] "
            "Kanakuri, too, experienced debilitating hyperthermia. About sixteen miles into the race, an exhausted Kanakuri left the course and desperately stumbled into a nearby garden party, where he drank orange juice for an hour. "
            "Embarrassed by his failure, he silently returned to Japan without notifying race officials. [...] "
            "Kanakuri did compete in the 1920 Summer Olympics held in Antwerp, where he finished in 16th with a time of 2 hours, 48 minutes and 45.4 seconds. "
            "Kanakuri subsequently participated in the 1924 Summer Olympics, where he failed to finish the race. [...] "
            "A Swedish reporter discovered him working as a geography teacher in southern Japan and in 1967, Sveriges Television offered Kanakuri the chance to complete his marathon. He accepted. [...] "
            "On March 20, 1967, he finished the marathon. [...] "
            "He commented, \"It was a long trip. Along the way, I got married, had six children and ten grandchildren.\"",
            nome="Shizo Kanakuri")],
    },
    # 2 a luta de 11 horas e 40 minutos
    {
        "temas_secundarios": ["limites_humanos", "historia_esportes"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Na luta greco-romana da Olimpíada de 1912, um único combate, entre Martin Klein e Alfred Asikainen, durou 11 horas e quarenta minutos. Klein venceu, mas ficou tão exausto que não pôde disputar o ouro.",
        "explicacao": (
            "A categoria dos médios, para lutadores de até 75 kg, reuniu em Estocolmo 38 competidores de 14 "
            "países, de 6 a 15 de julho. O formato era uma espécie de dupla eliminação: cada lutador tirava um "
            "número e enfrentava o do número seguinte, e quem acumulava derrotas ia saindo. Quando sobravam "
            "apenas três, os medalhistas, todos os resultados anteriores eram ignorados e começava uma rodada "
            "final especial entre eles. Asikainen garantiu a vaga nesse trio sem lutar, graças a uma folga na "
            "sétima rodada; Klein e Johanson entraram vencendo seus rivais. O confronto entre Klein e Asikainen, "
            "que acabou sendo a última luta, se arrastou por 11 horas e quarenta minutos e é considerado a luta mais "
            "longa do mundo. Quando enfim venceu, Klein estava completamente esgotado e foi considerado sem "
            "condições de lutar na decisão. O ouro ficou então com Johanson, cuja única derrota na fase "
            "eliminatória tinha sido uma derrota dupla, num combate contra o próprio Asikainen em que os dois "
            "perderam."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Wrestling_at_the_1912_Summer_Olympics_–_Men's_Greco-Roman_middleweight",
            "The event was held from July 6, 1912, to July 15, 1912. The official name was Middleweight A (maximum weight of 75 kilogram/165 lbs). [...] "
            "38 wrestlers from 14 nations competed. [...] "
            "The competition used a form of double-elimination tournament. [...] "
            "each wrestler drew a number. [...] "
            "Each man would face off against the wrestler with the next number [...] "
            "When only three wrestlers remain (the medalists), the double-elimination halts and a special final round is used to determine the order of the medals. [...] "
            "Asikainen and Johanson both received their first loss in their match [...] "
            "Asikainen's bye in the round guaranteed him a medal. Klein defeated Jokinen to join him in the medals round, while Johansson defeated Åberg to make the third. [...] "
            "With three wrestlers remaining, all of the previous results were ignored for the final round. "
            "The bout between Klein and Asikainen turned out to be the last match, which lasted 11 hours and forty minutes, which is the world's longest wrestling match. "
            "After Klein finally claimed victory, he was completely exhausted and was ruled unfit to compete in the final. "
            "Thus Johanson, whose only loss in the elimination rounds had been via a double loss to Asikainen, became the gold medalist.",
            nome="Wrestling at the 1912 Summer Olympics – Men's Greco-Roman middleweight")],
    },
    # 3 Arrhichion, o campeão morto
    {
        "temas_secundarios": ["grecia_antiga", "historia_esportes"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Segundo relatos antigos, em 564 a.C. o lutador Arrhichion morreu estrangulado na final do pancrácio olímpico, mas o rival desistiu no mesmo instante, com o pé deslocado. Os juízes coroaram o cadáver.",
        "explicacao": (
            "O pancrácio misturava boxe e luta livre, com chutes, chaves de articulação e estrangulamentos no "
            "chão, algo parecido com o MMA de hoje. Arrhichion, da cidade de Figália, já tinha vencido a prova "
            "em 572 e 568 a.C. e defendia o título. A luta fatal foi descrita pelo geógrafo Pausânias e por "
            "Filóstrato, o Jovem. Na versão de Pausânias, o último adversário agarrou Arrhichion primeiro, "
            "prendendo-o com as pernas e apertando seu pescoço com as mãos. Arrhichion conseguiu deslocar um "
            "dedo do pé do rival, mas morreu sufocado; o outro, vencido pela dor, desistiu ao mesmo tempo. Os "
            "juízes de Élis então proclamaram vencedor o corpo de Arrhichion. Num outro texto, Filóstrato de "
            "Atenas conta que o treinador dele, Eryxias, teria gritado durante a luta algo como \"Que belo "
            "epitáfio: nunca foi derrotado em Olímpia\", o que explicaria a recusa em se render. Uma estátua de "
            "vencedor foi erguida para ele em Figália, e a peça hoje exposta no museu de Olímpia é tida como a "
            "mesma, uma das mais antigas estátuas datadas de campeões olímpicos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Arrhichion",
            "(died 564 BC) was a champion pankratiast in the ancient Olympic Games.  He died while successfully defending his championship in the pankration at the 54th Olympiad (564 BC). [...] "
            "Arrhichion was the winner of the pankration at the 52nd and 53rd Olympiads (572 BC and 568 BC, respectively). "
            "Pankration was a martial art blending boxing and wrestling as well as kicking and holds, joint-locks and chokes on the ground, making it similar to modern MMA. "
            "Arrhichion's fatal fight was described by the geographer Pausanias and by Philostratus the Younger. [...] "
            "the latter got a grip first, and held Arrhachion, hugging him with his legs, and at the same time he squeezed his neck with his hands. "
            "Arrhachion dislocated his opponent's toe, but expired owing to suffocation; but he who suffocated Arrhachion was forced to give in at the same time because of the pain in his toe. "
            "The Eleans crowned and proclaimed victor the corpse of Arrhachion. [...] "
            "Philostratus of Athens writes in his Gymnasticus that Arrichion's failure to submit to his opponent was the result of his trainer, Eryxias, shouting to him, \"What a noble epitaph, 'He was never defeated at Olympia.'\" "
            "A victor statue of Arrhichion was set up at Phigalia; what is believed to be the same statue is now displayed in the museum at Olympia. It is one of the oldest dated Olympic victor statues.",
            nome="Arrhichion")],
    },
    # 4 os Zanes, estátuas pagas por trapaceiros
    {
        "temas_secundarios": ["grecia_antiga", "leis_julgamentos"],
        "tipos_espanto": ["engenhosidade", "historia_humana"],
        "gancho": "Na Olímpia antiga, as multas dos atletas trapaceiros pagavam estátuas de bronze de Zeus, enfileiradas na entrada do estádio, com o nome do culpado gravado na base para todo mundo ver.",
        "explicacao": (
            "As estátuas se chamavam Zanes, que era o plural de Zeus no dialeto local. Os juízes dos Jogos "
            "aplicavam multas a quem desrespeitasse as regras e, conforme a gravidade, podiam também mandar "
            "castigar o atleta fisicamente ou excluí-lo da competição. Com o dinheiro das multas, encomendavam "
            "estátuas a grandes artistas da época e as instalavam diante da entrada monumental do estádio, a "
            "Cripta, um lugar de passagem escolhido justamente para desencorajar novos trapaceiros. Segundo "
            "Pausânias, as bases traziam inscrições curtas com o nome do infrator, para deixar claro que uma "
            "vitória olímpica se conquistava com força, e não comprada com dinheiro; ter o nome gravado ali "
            "envergonhava o atleta e a cidade dele. As primeiras estátuas teriam vindo da multa de Eupolos, da "
            "Tessália, que subornou três adversários no boxe. Outras foram pagas pelo ateniense Kallipos, que "
            "também comprou rivais no pancrácio. E Sarapion, de Alexandria, foi o primeiro multado por covardia: "
            "ficou nervoso e fugiu de Olímpia na véspera dos Jogos. Das estátuas de bronze não sobrou nenhuma, "
            "mas 16 bases de pedra continuam lá, uma ao lado da outra."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Zanes_of_Olympia",
            "The Zanes were bronze statues of Zeus at ancient Olympia. The name Zanes was the plural of Zeus in the local dialect. "
            "These statues were dedicated to Zeus and they were erected with the money from fines imposed by the judges on those athletes who disrespected and/or violated the rules of the Olympic Games. "
            "Besides the fines, the judges could also impose body punishments or exclude an athlete from the Games depending on the severity of their violation. "
            "Today, only 16 pedestals (stone bases) of the statues survive. They are located one next to the other in front of the monumental entrance to the stadium, the Crypt: "
            "the reason they were placed in such a highly visible location was to dissuade other athletes from cheating. [...] "
            "The Zanes statues were crafted by great artists of their time. "
            "According to Pausanias, the pedestals were inscribed with short texts mentioning the name of the offender; these were to make it clear that Olympic victories were to be won by feats of strength, rather than bought with money. "
            "The inscription of an athlete's name on such a pedestal was shameful both for him and for his city. "
            "According to Pausanias, the first of the Zanes were erected when Eupolos from Thessaly was fined for bribing three of his opponents in the boxing event. "
            "The remaining six statues were erected later on by the Athenian Kallipos, an athlete in the Pankration (\"all force\" wrestling), who also bribed his opponents. "
            "Also, the Alexandrian pankratiast Sarapion was the first athlete to be fined by the judges for cowardice, because he got nervous and fled the sacred grounds of Olympia on the eve of the Games.",
            nome="Zanes of Olympia")],
    },
    # 5 Cinisca, campeã sem conduzir a biga
    {
        "temas_secundarios": ["grecia_antiga", "personagens_esquecidos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "A primeira mulher a vencer nos Jogos Olímpicos antigos, a princesa espartana Cinisca, ganhou duas vezes sem conduzir a biga: mulheres não podiam competir, mas podiam ser donas dos cavalos.",
        "explicacao": (
            "Cinisca era filha do rei Arquídamo II e irmã de Agesilau II, que também seria rei de Esparta. Nas "
            "Olimpíadas, as mulheres só entravam nas provas equestres, e não como competidoras: participavam "
            "como donas e treinadoras dos animais. Cinisca, que criava cavalos, contratou condutores e inscreveu "
            "sua equipe na corrida de carros de quatro cavalos em 396 a.C., quando devia ter uns 40 anos. "
            "Venceu, e repetiu a vitória em 392 a.C. Segundo Xenofonte e Plutarco, foi Agesilau quem a incentivou: "
            "ele achava que vencer essa corrida provava só riqueza, não coragem, e queria expor isso fazendo uma "
            "mulher ganhar. Historiadores de hoje desconfiam de um motivo mais prático, o de usar a fama da irmã "
            "na própria carreira política. Cinisca mandou instalar no templo de Zeus, em Olímpia, estátuas de "
            "bronze dela, do condutor, do carro e dos cavalos, com uma inscrição em que se declarava a única "
            "mulher a ganhar a coroa nas corridas de carros. Depois de morta, ganhou em Esparta um santuário de "
            "herói, honra antes reservada aos reis. Outras mulheres venceram depois, e uma delas, Berenice, do "
            "Egito, encomendou um poema dizendo ter \"roubado\" a glória de Cinisca."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Cynisca",
            "She is famous for being the first woman to win at the Olympic Games. Cynisca first entered the Olympics in 396 BC, where she won first prize competing with a team of horses she had trained herself. "
            "In 392 BC, Cynisca entered her horses in the Olympics for a second time and was awarded another victory in the same event. [...] "
            "she was the daughter of King Archidamus II and his wife Eupolia. "
            "She was probably half-sister to Agis II (r. 427–400 BC) and full sister to Agesilaus II (r. 400–360 BC), both of whom succeeded their father as a kings of Sparta. [...] "
            "Several sources from Xenophon and Plutarch mention how Agesilaus encouraged her to breed horses and compete in the games during her youth. [...] "
            "he believed that chariot racing merely demonstrated wealth, as it required no direct involvement from the horses' owner. "
            "Both of these ancient authors suggested that Agesilaus hoped to expose how the sport was unmanly and aristocratic by having a woman win. [...] "
            "They suspect that he was using her victories and wealth to promote his own political career and gain public support through association [...] "
            "In 396 BC, Cynisca employed charioteers to drive the horses she trained and entered her team at the Olympics for the first time, where it won in the four-horse chariot race [...] "
            "Cynisca is thought to have been approximately 40 years old when she won her first Olympic victory. [...] "
            "Cynisca dedicated a set of bronze statues which depicted herself, her charioteer, her chariot, and her horses at the Temple of Zeus in Olympia. [...] "
            "Cynisca also celebrated her victories with an inscription, declaring that she was the only woman to win the wreath in the chariot events at the Olympic Games. [...] "
            "a heroön (hero-shrine) was erected for Cynisca in Sparta at Plane-tree Grove, where religious ceremonies were held. "
            "Previously, only Spartan kings had been graced in this way; Cynisca was the first woman to receive this honor. [...] "
            "In terms of competing in the Olympic games, women were only allowed to enter the equestrian events, not by participating themselves, but rather by owning and training the horses. [...] "
            "When Berenike of Egypt won in the four-horse chariot race at the Olympics in the early third century BC, she commissioned an epigram by the poet Posidippus in which she explicitly claimed to have \"stolen\" the fame",
            nome="Cynisca")],
    },
    # 6 Nero e a Olimpíada adiada
    {
        "temas_secundarios": ["roma_antiga", "grecia_antiga"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 67 d.C., o imperador Nero subornou os organizadores para adiar a Olimpíada em um ano e poder competir. Ganhou tudo, até uma corrida de carros de dez cavalos em que caiu e não terminou.",
        "explicacao": (
            "Nero se apresentava em público como ator, poeta, músico e condutor de carros de corrida, o que "
            "escandalizava a aristocracia romana, porque esses ofícios costumavam ser de escravos e artistas "
            "de má fama. Plínio o chamou de \"imperador-ator\". Para a Olimpíada de 67, além de conseguir o "
            "adiamento, ele fez incluir competições artísticas entre as provas atléticas. Durante os Jogos, "
            "hospedado numa vila construída para ele em Olímpia, cantou e tocou lira no palco, atuou em "
            "tragédias e disputou corridas de carros. Venceu todas as provas de que participou. Na corrida de "
            "dez cavalos, foi lançado para fora do carro e abandonou a prova, mas recebeu a coroa assim mesmo, "
            "sob o argumento de que teria vencido se tivesse terminado. Segundo o historiador Edward Champlin, a "
            "presença do imperador sufocou qualquer competição de verdade, e Nero parecia não perceber isso. "
            "A glória durou pouco: ele morreu um ano depois, e seu nome foi apagado da lista de vencedores."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Nero",
            "He made public appearances as an actor, poet, musician, and charioteer, which scandalized his aristocratic contemporaries as these occupations were usually the domain of slaves, public entertainers, and infamous persons. [...] "
            "He stayed at the Villa of Nero at Olympia, Greece, during his participation at the Olympic Games of AD 67. [...] "
            "Pliny described Nero as an \"actor-emperor\" (scaenici imperatoris) [...] "
            "In AD 67 Nero participated in the Olympics. He had bribed organizers to postpone the games for a year so he could participate, and artistic competitions were added to the athletic events. "
            "Nero won every contest in which he was a competitor. During the games Nero sang and played his lyre on stage, acted in tragedies and raced chariots. "
            "He won a 10-horse chariot race, despite being thrown from the chariot and leaving the race. "
            "He was crowned on the basis that he would have won if he had completed the race. "
            "After he died a year later, his name was removed from the list of winners. "
            "Champlin writes that though Nero's participation \"effectively stifled true competition, [Nero] seems to have been oblivious of reality.\"",
            nome="Nero")],
    },
    # 7 o revezamento da tocha nasceu em 1936
    {
        "temas_secundarios": ["segunda_guerra", "grecia_antiga"],
        "tipos_espanto": ["mito_desmentido", "origem_inesperada"],
        "gancho": "O revezamento da tocha olímpica parece tradição grega, mas não tem precedente antigo: foi criado para os Jogos de Berlim de 1936, sob o nazismo, com tochas da Krupp e espelho da Zeiss.",
        "explicacao": (
            "Na Grécia antiga havia, sim, fogo sagrado em Olímpia: durante os Jogos, uma chama ficava acesa no "
            "altar do santuário de Héstia, e outros fogos eram acesos nos templos de Zeus e de Hera. Mas ninguém "
            "levava esse fogo de cidade em cidade. Nos Jogos modernos, a primeira chama simbólica apareceu em "
            "Amsterdã, em 1928, numa ideia do arquiteto Jan Wils: ela ardia no alto de uma torre do estádio para "
            "indicar de longe onde aconteciam as provas, e foi acesa por um funcionário da companhia elétrica da "
            "cidade. O revezamento veio oito anos depois, criado por Carl Diem para Berlim. A primeira cerimônia "
            "de acendimento em Olímpia foi em 20 de julho de 1936, com tochas fabricadas pela Krupp e um espelho "
            "da Zeiss, duas empresas ligadas ao governo nazista. A chama percorreu 3.187 km, carregada por 3.331 "
            "corredores durante doze dias e onze noites, e o ministro da Propaganda, Joseph Goebbels, encomendou "
            "a Leni Riefenstahl um filme sobre o trajeto. Até hoje a chama é acesa diante das ruínas do templo "
            "de Hera, com os raios do Sol concentrados por um espelho parabólico."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Olympic_flame",
            "The first time that a symbolic flame made its appearance in the Summer Olympic Games was for the 1928 Summer Olympics in Amsterdam. "
            "The main purpose of this fire, placed in a large bowl on top of a slender tower, named \"Marathon Tower\", was to indicate for miles around where in Amsterdam the Olympic Games were being held. "
            "This tower was associated with the marathon race and all its elements, including the fire, were an idea of the architect Jan Wils who also had designed the stadium. "
            "The idea for the Olympic flame was derived from ancient Greek ceremonies where a sacred fire was kept burning throughout the celebration of the ancient Olympics on the altar of the sanctuary of Hestia. [...] "
            "Every four years, when Zeus was honoured at the Olympic Games, additional fires were lit at his temple and that of his wife, Hera. "
            "The modern Olympic flame is ignited every two years in front of the ruins of the temple of Hera. "
            "When the idea of a symbolic fire was introduced during the 1928 Summer Olympics, an employee of the Electric Utility of Amsterdam lit the first symbolic flame in the Marathon Tower of the Olympic Stadium in Amsterdam. "
            "The Olympic flame and the Olympic torch relay was first introduced to the Summer Olympics at the 1936 Summer Olympics in Berlin by Carl Diem. "
            "The first ever torch-lighting ceremony was held in Olympia, Greece on July 20, 1936. "
            "The torches used were made by Krupp, and the mirror used to light the flame was made by Zeiss Optics, both companies with links to the Nazi government of the time. [...] "
            "a fire is kindled by the light of the Sun, its rays concentrated by a parabolic mirror. [...] "
            "The Olympic torch relay, which transports the Olympic flame from Olympia, Greece to the various designated sites of the Games, had no ancient precedent and was introduced by Carl Diem at the 1936 Summer Olympics in Berlin, Germany. "
            "At the first Olympic torch relay, the flame was transported from Olympia to Berlin over 3,187 kilometers (1,980 miles) by 3,331 runners in twelve days and eleven nights. "
            "Nazi Propaganda Minister Joseph Goebbels commissioned filmmaker and propagandist Leni Riefenstahl to film the event.",
            nome="Olympic flame")],
    },
    # 8 hipismo de 1956 na Suécia por causa da quarentena
    {
        "temas_secundarios": ["domesticacao", "fronteiras_paises"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "A Olimpíada de 1956 foi em Melbourne, mas o hipismo foi na Suécia, meses antes do resto: a quarentena australiana para cavalos era tão rígida que o país não abriu exceção nem para os Jogos.",
        "explicacao": (
            "A Austrália exigia que cavalos importados cumprissem seis meses de quarentena antes do embarque. "
            "Numa reunião em 1953, as autoridades federais decidiram não mudar a lei por causa dos animais "
            "olímpicos, e as provas equestres ficaram impossíveis no país. Em 1954, o Comitê Olímpico "
            "Internacional escolheu Estocolmo como sede alternativa. O resultado foi uma Olimpíada dividida entre "
            "duas cidades, dois países e dois continentes: o hipismo, com adestramento, concurso completo e "
            "saltos, foi de 11 a 17 de junho, no verão do hemisfério norte, e as demais modalidades, em "
            "novembro, no fim da primavera australiana. Foram 158 inscrições de 29 comitês olímpicos. Até a "
            "tocha teve trajeto próprio: todos os que a levaram até Estocolmo foram a cavalo. A separação teve "
            "um efeito curioso: cinco países competiram na Suécia e não foram a Melbourne. Egito e Camboja "
            "ficaram de fora por causa da Crise de Suez, e Holanda, Espanha e Suíça boicotaram a parte "
            "australiana em protesto contra a invasão soviética da Hungria."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Equestrian_at_the_1956_Summer_Olympics",
                "The equestrian events at the 1956 Summer Olympics were held in Stockholm due to the Australian quarantine regulations and included dressage, eventing, and show jumping. [...] "
                "The competitions were held from 11 to 17 June 1956 at Stockholm Olympic Stadium. There were 158 entries from 29 National Olympic Committees [...] "
                "Although Melbourne was awarded the 1956 Olympic Games, Australia had a strict six-month pre-shipment quarantine on horses. "
                "A meeting in 1953 by Australian federal authorities ruled that they would not change the quarantine laws for the Olympic horses. "
                "Therefore, the equestrian competition would not be able to be held in Australia. In 1954, the IOC selected Stockholm, Sweden, as the alternate venue for the equestrian events. "
                "Therefore, the equestrian events were not only separated by city or country, but also continent, with the equestrian event being held in June (summer in the Northern Hemisphere) and the other sports held in November (late spring in the Southern Hemisphere). [...] "
                "Five nations competed in the equestrian events in Stockholm, but did not attend the Games in Melbourne: [...] "
                "Egypt and Cambodia did not compete in Melbourne due to the Suez Crisis, whilst Netherlands, Spain and Switzerland all boycotted the Australian event in protest at the Soviet invasion of Hungary.",
                nome="Equestrian at the 1956 Summer Olympics"),
            wiki("Olympic_flame",
                "In 1956, all carriers in the torch relay to Stockholm, where the equestrian events were held instead of in Melbourne, travelled on horseback.",
                nome="Olympic flame"),
        ],
    },
    # 9 Sohn Kee-chung e a bandeira apagada
    {
        "temas_secundarios": ["imperios_coloniais", "segunda_guerra"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "O campeão da maratona olímpica de 1936 era coreano, mas correu pelo Japão, que dominava a Coreia. Um jornal apagou a bandeira japonesa da camisa dele na foto do pódio, e oito pessoas acabaram presas.",
        "explicacao": (
            "Sohn Kee-chung nasceu em 1912 na Coreia, então sob domínio japonês, e por ordem de Tóquio competiu "
            "com o nome Son Kitei, a pronúncia japonesa dos caracteres do seu nome. Em Berlim, venceu a maratona "
            "em 2h29min19s, recorde olímpico, e o companheiro Nam Sung-yong levou o bronze; as duas medalhas "
            "foram creditadas ao Japão. Na cerimônia, Sohn se recusou a reconhecer o hino japonês e depois disse "
            "a jornalistas que tinha vergonha de correr pelo Japão. Quando o jornal Dong-a Ilbo publicou a foto "
            "do pódio, retocou a imagem para sumir com a bandeira japonesa da camisa. O governador-geral japonês "
            "da Coreia ficou furioso: a polícia militar prendeu oito pessoas ligadas ao jornal, que foi suspenso "
            "por nove meses. Sohn também deveria ter ganhado um capacete coríntio do século VIII a.C., achado em "
            "Olímpia, mas o COI achou que um presente tão valioso violaria as regras do amadorismo. O capacete "
            "ficou 50 anos num museu de Berlim e só lhe foi entregue em 1986. Em 2011, o COI passou a registrar "
            "a nacionalidade coreana no perfil oficial dele."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Sohn_Kee-chung",
            "He became the first  Korean to win a medal at the Olympic Games, winning gold in the marathon at the 1936 Berlin Olympics. "
            "He was born in the Korean Peninsula, but he was forced to compete as a member of the Japanese delegation because Korea was under Japanese rule at the time. "
            "Sohn set an Olympic record of 2 hours 29 minutes 19.2 seconds. [...] "
            "Sohn Kee-chung was born on August 29, 1912 [...] "
            "His teammate Nam Sung-yong took the bronze medal. "
            "As Korea was under Japanese rule at the time, the International Olympic Committee (IOC) officially credited Japan with Sohn's gold and Nam's bronze in the 1936 Summer Olympics medal count. "
            "On December 9, 2011, the IOC recognized Sohn's Korean nationality in his official profile. [...] "
            "Under orders from Tokyo, Sohn Kee-chung had to compete using the Latin alphabet name of Son Kitei. It is the romanization of the Japanese pronunciation of his Korean name in hanja. "
            "Sohn refused to acknowledge the Japanese anthem while it was played at his award ceremony and later told reporters that he was ashamed to run for Japan. "
            "When the Dong-a Ilbo published a photograph of Sohn at the medal ceremony, it altered the image to remove the Japanese flag from his running tunic. "
            "The act enraged the Japanese Governor-General of Korea Minami Jiro in Seoul. "
            "The Kempetai military police imprisoned eight people connected with the newspaper and suspended its publication for nine months. [...] "
            "For winning the marathon, Sohn was to have received an ancient Corinthian helmet from the 8th century BC, which was discovered at Olympia, Greece, and later purchased by a newspaper in Athens to give as an Olympic award. "
            "However, the IOC believed that presenting such a valuable gift to a runner would violate its amateur rules. "
            "The helmet was placed in a Berlin museum and remained there for 50 years. It was finally presented to Sohn in 1986.",
            nome="Sohn Kee-chung")],
    },
    # 10 as "medalhas da amizade" de Nishida e Oe
    {
        "temas_secundarios": ["historia_esportes"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 1936, dois amigos japoneses empataram no salto com vara e se recusaram a desempatar. A equipe deu prata a um e bronze ao outro; no Japão, eles cortaram as medalhas ao meio e juntaram as metades.",
        "explicacao": (
            "Shuhei Nishida, estudante de engenharia da Universidade Waseda, já tinha sido prata no salto com "
            "vara em Los Angeles, em 1932. Em Berlim, quatro anos depois, empatou com o amigo e companheiro de "
            "equipe Sueo Oe. Os dois não quiseram saltar um contra o outro para decidir quem ficava com qual "
            "medalha, e a própria delegação japonesa resolveu a questão: Nishida levou a prata e Oe, o bronze, "
            "com o critério de que Nishida tinha passado a altura com menos tentativas. A disputa aparece numa "
            "cena de Olympia, o documentário de Leni Riefenstahl sobre aqueles Jogos. De volta ao Japão, os dois "
            "pediram a um joalheiro que cortasse as duas medalhas e emendasse as partes, formando duas novas "
            "peças, metade prata e metade bronze, que ficaram conhecidas como \"medalhas da amizade\". Nishida "
            "seguiu no esporte a vida toda: aos 41 anos ganhou um bronze nos Jogos Asiáticos de 1951, foi árbitro "
            "e dirigente, e em 1989 recebeu a Ordem Olímpica em prata."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Shuhei_Nishida",
            "He was a student of the Engineering Department at Waseda University, when selected as a member of the Japanese Olympic team for the 1932 Summer Olympics in Los Angeles, where he won the silver medal in the pole vault event. [...] "
            "He subsequently participated in the 1936 Summer Olympics held in Berlin, Germany where he repeated his performance winning a second silver medal in the same event tying with his friend and teammate Sueo Oe. "
            "When the two declined to compete against each other to decide a winner, Nishida was awarded the silver and Oe the bronze by decision of the Japanese team, on the basis that Nishida had cleared the height in fewer attempts. "
            "The competition was featured in a scene in the documentary Olympia, filmed by Leni Riefenstahl. "
            "On their return to Japan, Nishida and Oe famously had their Olympic medals cut in half, and had a jeweler splice together two new “friendship medals”, half in bronze and half in silver. "
            "At the age of 41, Nishida won a bronze medal at the 1951 Asian Games. "
            "He remained active in sports all of his life, serving as a referee at events, and from 1959 as an honorary vice chairman of the Japan Association of Athletics Federations, and as a member of the Japanese Olympic Committee. "
            "In 1989, he was awarded the silver medal of the Olympic Order.",
            nome="Shuhei Nishida")],
    },
    # 11 Margaret Abbott, campeã sem saber
    {
        "temas_secundarios": ["personagens_esquecidos", "historia_esportes"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "A primeira americana campeã olímpica, Margaret Abbott, venceu um torneio de golfe em Paris, em 1900, sem saber que era Olimpíada. Morreu em 1955 sem nunca ter descoberto.",
        "explicacao": (
            "A Olimpíada de 1900 se misturou à Exposição Universal de Paris e se espalhou de maio a outubro, sem "
            "cerimônia de abertura nem de encerramento. Foi também a primeira com mulheres: 22 entre 997 atletas. "
            "Muitas provas nem eram anunciadas como olímpicas; o golfe feminino aparecia como \"competição da "
            "Exposição\", e o historiador Bill Mallon diz que muitos atletas não sabiam que estavam numa "
            "Olimpíada. Abbott, uma americana que estudava arte em Paris, soube do torneio por um anúncio de "
            "jornal e se inscreveu junto com a mãe. A prova tinha 9 buracos; ela venceu com 47 tacadas, e a mãe "
            "empatou em sétimo. O prêmio foi uma tigela de porcelana, já que o golfe não deu medalhas. Mais "
            "tarde, segundo o filho, ela dizia ter ganhado porque as francesas tinham entendido mal o tipo de "
            "jogo e aparecido de salto alto e saia justa. A façanha só veio à tona depois que Paula Welch, "
            "professora da Universidade da Flórida, pesquisou a vida dela, e o jornal The New York Times publicou "
            "seu obituário, atrasado, em 2018."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Margaret_Abbott",
            "She was the first American woman to win an Olympic event: the women's golf tournament at the 1900 Summer Olympics. [...] "
            "In 1899, she traveled with her mother to Paris to study art. The following year, along with her mother, she signed up for a women's golf tournament without realizing that it was the second modern Olympics. "
            "Abbott won the tournament with a score of 47 strokes; her mother tied for seventh place. Abbott received a porcelain bowl as a prize. [...] "
            "Abbott died at the age of 76 in 1955, never realizing that she won an Olympic event. "
            "She was not well known until Paula Welch, a professor at the University of Florida, researched her life. In 2018, The New York Times published her belated obituary. [...] "
            "The 1900 Summer Olympics, hosted in Paris between May and October, was the second modern Olympics. [...] "
            "In 1900, however, women were allowed to compete for the first time in five sports: golf, tennis, sailing, rowing and equestrianism. Out of a total of 997 athletes, 22 were women. "
            "The events lacked proper equipment, did not have an opening or closing ceremony [...] "
            "The women's event was held over 9 holes [...] "
            "The Olympics coincided with the 1900 Paris Exposition [...] "
            "The golf tournament was billed as the \"Exposition Competition\" or \"Paris World's Fair Competition\" instead of being referred to as an Olympic event. [...] "
            "According to Mallon, many athletes did not know that they were participating in the Olympics. "
            "Abbott learned about the tournament from a newspaper notice. [...] "
            "According to Philip Dunne, his mother would later tell her family she won the tournament \"because all the French girls apparently misunderstood the nature of the game scheduled that day and turned up to play in high heels and tight skirts\". [...] "
            "No medals were awarded for many other events, including golf",
            nome="Margaret Abbott")],
    },
    # 12 "Sangue na água": Hungria x URSS em 1956
    {
        "temas_secundarios": ["guerra_fria"],
        "tipos_espanto": ["historia_humana", "conexao_inesperada"],
        "gancho": "Semanas depois de a URSS esmagar a Revolução Húngara, Hungria e URSS se enfrentaram no polo aquático da Olimpíada de 1956. O jogo foi tão violento que a polícia entrou para evitar um tumulto na torcida.",
        "explicacao": (
            "A rivalidade já vinha de antes: com o controle político sobre a Hungria, os soviéticos tinham "
            "estudado e copiado os métodos de treino dos húngaros, campeões olímpicos. Em outubro de 1956, um "
            "protesto de estudantes em Budapeste virou revolta, e em novembro tanques soviéticos esmagaram o "
            "levante. A seleção húngara treinava nas montanhas acima da cidade e ouvia os tiros. Foi levada à "
            "Tchecoslováquia e só soube da dimensão da repressão ao chegar à Austrália. Na semifinal de 6 de "
            "dezembro, os húngaros tinham um plano: provocar os rivais em russo, língua que haviam aprendido na "
            "escola. Houve chutes e socos desde o início. Com um minuto para o fim e a Hungria vencendo por 4 a 0, "
            "o soviético Valentin Prokopov acertou Ervin Zádor, que saiu da piscina sangrando acima do olho. "
            "Torcedores furiosos desceram até a beira da piscina, os juízes encerraram a partida e a Hungria foi "
            "declarada vencedora. As fotos deram ao jogo o nome de \"Sangue na água\", embora a história de que a "
            "água ficou vermelha seja exagero. A Hungria levou o ouro, e depois Zádor e alguns colegas desertaram "
            "para o Ocidente."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Blood_in_the_Water_match",
            "was a water polo match between Hungary and the USSR at the 1956 Melbourne Olympics. "
            "The semi-final match took place on 6 December 1956 against the background of the recent Hungarian Revolution, and saw Hungary defeat the USSR 4–0. "
            "The name was coined after Hungarian player Ervin Zádor emerged during the last two minutes with blood pouring from above his eye after being punched by Soviet player Valentin Prokopov. "
            "Tensions were at an all-time high between the competing teams; the Soviet armed forces had violently suppressed the Hungarian Revolution just weeks before. [...] "
            "the Soviets had taken advantage of their political control of Hungary to study and copy the training methods and tactics of the Olympic champion Hungarians. "
            "Then, on 23 October 1956, a demonstration by students of the Budapest University of Technology and Economics escalated into an uprising against the government in Budapest. "
            "On 1 November, Soviet tanks started rolling into Hungary and from 4 to 10 November forces began suppressing the uprising [...] "
            "At the time, the Hungarian water polo team was in a mountain training camp above Budapest. They were able to hear the gunfire and see smoke rising. [...] "
            "they were moved into Czechoslovakia to avoid being caught in the revolution. "
            "The players only learned of the true extent of the uprising and the subsequent crackdown after arriving in Australia [...] "
            "The Hungarians had created a strategy before the game to taunt the Soviets, whose language they had studied in school. [...] "
            "From the beginning, kicks and punches were exchanged. [...] "
            "With one minute remaining in the match, Hungary was leading 4–0. [...] "
            "Prokopov struck him, causing a bleeding gash. Zádor left the pool; his bleeding was the final straw for a crowd already in a frenzy. "
            "Many angry spectators jumped onto the concourse beside the water, shook their fists, shouted abuse and spat at the Russians. "
            "To avoid a riot, police entered the arena and shepherded the crowd away. "
            "Pictures of Zádor's injuries were then published by newspapers, leading to the \"Blood in the Water\" moniker. "
            "Reports that the water in the pool turned red were, however, an exaggeration. [...] "
            "The referees stopped the match; Hungary was declared the winner since they had been leading. "
            "Hungary then beat Yugoslavia 2–1 in the final to win their fourth Olympic gold medal. Zádor's injury forced him to miss the match. "
            "After the event was completed, he and some of his teammates defected to the West.",
            nome="Blood in the Water match")],
    },
    # 13 os três segundos jogados três vezes (1972)
    {
        "temas_secundarios": ["guerra_fria"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Na final olímpica de basquete de 1972, os três segundos finais foram jogados três vezes, até a URSS virar sobre os EUA. Os americanos recusaram a prata, e as medalhas seguem guardadas num cofre na Suíça.",
        "explicacao": (
            "Os Estados Unidos nunca tinham perdido um jogo olímpico de basquete: eram sete ouros seguidos desde "
            "1936 e 63 vitórias a zero antes daquela final, em Munique, em plena Guerra Fria. Faltando três "
            "segundos, Doug Collins converteu dois lances livres e pôs os americanos na frente por 50 a 49. "
            "Durante o segundo arremesso, uma buzina soou na mesa: os soviéticos alegavam ter pedido tempo. O "
            "jogo foi interrompido com um segundo restando, e o secretário-geral da FIBA, Renato William Jones, "
            "desceu das arquibancadas e exigiu que os três segundos fossem repetidos. Na segunda tentativa, a "
            "buzina tocou e os americanos comemoraram, mas o relógio não tinha sido ajustado, e a jogada foi "
            "refeita mais uma vez. Na terceira, um árbitro fez um gesto ao americano Tom McMillen, que se afastou "
            "de Ivan Edeshko; livre, Edeshko lançou a bola de uma ponta à outra da quadra, e Alexander Belov "
            "pegou e fez a cesta da vitória quando a buzina soou de vez. O protesto americano foi rejeitado por "
            "um júri de cinco membros, três deles de países aliados da URSS, numa votação que não foi unânime. Os "
            "jogadores votaram, por unanimidade, recusar as medalhas, e o COI exige o aceite de todo o time para "
            "entregá-las."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("1972_Olympic_men's_basketball_final",
            "The final three seconds of the game were played three times under questionable rule interpretations, leading to an ultimate victory by the Soviet team. [...] "
            "was among the contenders to win another in Munich at the 1972 Summer Olympics. [...] "
            "Since the first Olympic basketball tournament at the 1936 Olympics in Berlin, the Americans had not lost a single game, winning seven consecutive gold medals in dominating fashion. "
            "Their record reached an unprecedented 63–0 before the final game. [...] "
            "The United States and Soviet Union sporting rivalry reached its peak during the Cold War. [...] "
            "With three seconds remaining on the game clock, Collins was awarded two free throws and sank the first to tie the score at 49. "
            "Just as Collins lifted the ball to begin his shooting motion in attempting the second free throw, the horn from the scorer's table sounded [...] "
            "scoring to put the U.S. ahead by a score of 50–49. [...] "
            "He asserted that head coach Vladimir Kondrashin had called for a time-out [...] "
            "The game clock was stopped with one second remaining. [...] "
            "Renato William Jones, the secretary general of FIBA at the time [...] "
            "ruling that the entire inbounds sequence would be replayed from the point immediately following the second free throw and that the game clock would thus be reset to three seconds. "
            "Jones, who had had a contentious relationship with American basketball officials for a number of years, came down from the stands to the court to contribute to the officials' ruling, and he insisted upon a complete replay of the final three seconds. [...] "
            "not noticing that clock operator Andre Chopard was still working on getting the game clock set to three seconds. [...] "
            "the U.S. team began a joyful celebration of its apparent one-point victory. [...] "
            "the officials once again ordered the court to be cleared, the players to be brought back into position, the clock to be reset, and the final three seconds be replayed. [...] "
            "On the third inbound try, McMillen was again assigned to use his height to challenge Edeshko's inbound pass. "
            "However, as official Artenik Arabadjian prepared to put the ball into play, he gestured to McMillen. "
            "McMillen responded by backing several feet away from Edeshko, which gave Edeshko a clear view and unobstructed path to throw a long pass down the court. [...] "
            "Belov caught the ball in the air [...] "
            "Belov then gathered himself and made an uncontested layup, scoring the winning points as the horn sounded for the last time. [...] "
            "filed a detailed protest, which was heard by FIBA's five-member jury of appeal. [...] "
            "In announcing the verdict, Hepp steadfastly refused to provide the specifics of the vote count, acknowledging only that the decision was not unanimous. "
            "With three of the five jury members, including Hepp, being from Soviet-allied nations [...] "
            "the U.S. players did not accept the jury's verdict, voting unanimously to refuse their silver medals, and the team did not attend the medal ceremony. "
            "The silver medals are still kept in a vault in Lausanne, Switzerland. [...] "
            "With regard to awarding the medals, the IOC has insisted that for such an action, the entire team would need to consent unanimously.",
            nome="1972 Olympic men's basketball final")],
    },
    # 14 Peter Norman, o terceiro homem do pódio de 1968
    {
        "temas_secundarios": ["personagens_esquecidos", "revolucoes_politicas"],
        "tipos_espanto": ["historia_humana", "origem_inesperada"],
        "gancho": "Na foto do protesto de 1968, o terceiro homem no pódio, o australiano Peter Norman, usava um broche de apoio. E foi ideia dele que Smith e Carlos dividissem um par de luvas pretas, uma para cada um.",
        "explicacao": (
            "Na final dos 200 metros na Cidade do México, o americano Tommie Smith venceu com recorde mundial, "
            "19,83 segundos, e Norman passou John Carlos na chegada para levar a prata com 20,06 segundos, marca que "
            "seguiu como recorde da Oceania por mais de 56 anos. Depois da prova, Smith e Carlos contaram a "
            "Norman o que pretendiam fazer no pódio. Segundo o jornalista Martin Flanagan, perguntaram se ele "
            "acreditava em direitos humanos e, diante do sim, ouviram: \"Eu fico com vocês\". A caminho da "
            "cerimônia, Norman pediu emprestado a um remador americano, Paul Hoffman, o broche do Projeto "
            "Olímpico pelos Direitos Humanos. Como Carlos tinha esquecido as luvas na Vila Olímpica, Norman "
            "sugeriu que os dois dividissem o par de Smith; por isso Smith ergueu o punho direito e Carlos, o "
            "esquerdo. Muito se escreveu que Norman virou pária na Austrália e foi barrado em 1972, mas o "
            "Comitê Olímpico Australiano sustenta que ele não cumpriu os critérios de seleção, e o tema segue "
            "em debate. Quando Norman morreu, em 2006, Smith e Carlos fizeram discursos e carregaram o caixão."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Peter_Norman",
            "He won the silver medal in the 200 metres at the 1968 Summer Olympics in Mexico City, with a time of 20.06 seconds, which remained the Oceania 200 m record for more than 56 years. [...] "
            "He knew the salute was to occur and wore a badge of the Olympic Project for Human Rights in support of fellow athletes John Carlos and Tommie Smith. [...] "
            "On the morning of 16 October, US athlete Tommie Smith won the 200-metre final with a world-record time of 19.83 seconds. "
            "Norman finished second in a time of 20.06 s after passing U.S. athlete John Carlos at the finish line. [...] "
            "Norman died of a heart attack on 3 October 2006 in Melbourne at the age of 64. [...] "
            "both Smith and Carlos gave eulogies and were pallbearers at Norman's funeral. [...] "
            "After the final, Carlos and Smith had told Norman what they were planning to do during the ceremony. "
            "Journalist Martin Flanagan wrote: \"They asked Norman if he believed in human rights. He said he did. [...] "
            "He said, 'I'll stand with you'. [...] "
            "On the way to the medal ceremony, Norman saw the OPHR badge being worn by Paul Hoffman, a white member of the US rowing team, and asked him if he could wear it. "
            "It was Norman who suggested that Smith and Carlos share the black gloves used in their salute, after Carlos left his pair at the Olympic Village. "
            "This is the reason Smith raised a gloved right fist and Carlos raised his gloved left. [...] "
            "he returned home to Australia a pariah, suffering unofficial sanction and ridicule as the Black Power salute's forgotten man. [...] "
            "Various commentators say he was not selected for the Olympic Games in Munich in 1972 despite recording qualifying times, but the Australian Olympic Committee maintains that Norman was not selected for the 1972 Olympics because he did not meet the selection standard",
            nome="Peter Norman")],
    },
    # 15 Takács, campeão com a mão esquerda
    {
        "temas_secundarios": ["limites_humanos", "segunda_guerra"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 1938, uma granada defeituosa feriu gravemente a mão direita do atirador húngaro Károly Takács. Ele treinou escondido com a esquerda e foi campeão olímpico de pistola de tiro rápido em 1948 e 1952.",
        "explicacao": (
            "Em 1936, Takács já estava entre os melhores do mundo na pistola, mas ficou fora da equipe húngara "
            "para Berlim porque era sargento, e só oficiais podiam competir. A regra caiu depois daqueles Jogos, "
            "e ele mirava a Olimpíada de 1940, marcada para Tóquio. Em 1938, durante um treinamento do exército, "
            "uma granada defeituosa explodiu e feriu gravemente sua mão direita. Takács decidiu continuar e "
            "passou a atirar com a esquerda, treinando em segredo; na primavera de 1939, surpreendeu o país ao "
            "vencer o campeonato húngaro, e no mesmo ano fez parte da equipe campeã mundial. As Olimpíadas de "
            "1940 e 1944 foram canceladas pela Segunda Guerra. Em Londres, em 1948, aos 38 anos, ele venceu o "
            "favorito, o argentino Carlos Enrique Díaz Sáenz Valiente, então campeão mundial, e em Helsinque, em "
            "1952, ganhou de novo. Foi o primeiro atirador a conquistar dois ouros na pistola de tiro rápido de "
            "25 metros. Ainda competiu em Melbourne, em 1956, mas terminou em oitavo."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Károly_Takács",
            "was the first shooter to win two Olympic gold medals in the 25 metre rapid fire pistol event, both with his left hand after his right hand was seriously injured. [...] "
            "By 1936, he was a world-class pistol shooter, but he was denied a place in the Hungarian shooting team for the 1936 Summer Olympics on the grounds that he was a sergeant, and only commissioned officers were allowed to compete. "
            "This prohibition was lifted in Hungary after the Berlin Games, and Takács had expectations of success at the 1940 Summer Olympics, scheduled to be held in Tokyo. "
            "During army training in 1938, his right hand was badly injured when a faulty grenade exploded. "
            "Takács was determined to continue his shooting career, and switched to shooting with his left hand. "
            "He practiced in secret, surprising his countrymen when he won the Hungarian national pistol shooting championship in the spring of 1939. "
            "He also was a member of the Hungarian team that won the 1939 UIT World Shooting Championships in the event. [...] "
            "The Olympic Games scheduled for 1940 and 1944 were canceled due to the Second World War. "
            "However, Takács surprised the world by winning the gold medal at the 1948 Summer Olympics in London, aged 38, beating the favourite, Argentine Carlos Enrique Díaz Sáenz Valiente, the reigning world champion. "
            "Takács won a second gold medal in the same event at the 1952 Summer Olympics in Helsinki [...] "
            "Takács also attended the 1956 Summer Olympics in Melbourne, but finished eighth and failed to win a third medal.",
            nome="Károly Takács")],
    },
]
