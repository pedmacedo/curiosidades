LOTE = "2026-11-18-vieses_cognitivos-01"
AREA = "mente"
TEMA = "vieses_cognitivos"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Dunning-Kruger pode ser em parte efeito estatístico
    {
        "temas_secundarios": ["aprendizagem_inteligencia", "probabilidade"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "No estudo original do efeito Dunning-Kruger, quem ficou entre os piores se colocou acima da média. Mas parte do efeito talvez seja só estatística: a regressão à média produz um padrão parecido.",
        "explicacao": (
            "Em 1999, David Dunning e Justin Kruger testaram estudantes em raciocínio lógico, gramática inglesa e "
            "senso de humor, e pediram que cada um estimasse o próprio desempenho. Quem ficou no quarto de pior "
            "desempenho tinha nota equivalente ao percentil 12, mas se colocou, em média, no percentil 62. A "
            "explicação clássica é metacognitiva: quem tem pouca habilidade também não consegue perceber a "
            "diferença entre o próprio trabalho e o dos outros. Mas há explicações rivais. Uma delas diz que o "
            "efeito seria em grande parte um artefato estatístico: quando duas medidas não estão perfeitamente "
            "correlacionadas, quem tem um valor extremo numa delas tende a ter um valor mais perto da média na "
            "outra, a chamada regressão à média. Somado à tendência geral de cada um se achar melhor que a média, "
            "isso produziria o padrão mesmo sem nenhum problema especial de autoconhecimento. O debate continua."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Dunning%E2%80%93Kruger_effect",
            "The effect was formalized and empirically studied by the psychologists David Dunning and Justin Kruger in 1999. [...] "
            "The metacognitive explanation holds that poor performers misjudge their abilities because they lack the ability to recognize the qualitative difference between their performances and the performances of others. "
            "The statistical explanation holds that the empirical effect may largely be the result of a mere statistical effect and the fact that people have a general tendency to think that they are better than average. [...] "
            "inductive, deductive, and abductive logical reasoning; English grammar; and appreciation of humor. "
            "Across four studies, the research indicates that the participants who scored in the bottom quartile overestimated their test performance and their abilities. "
            "Their test scores placed them in the 12th percentile, but they ranked themselves in the 62nd percentile. [...] "
            "sees the Dunning–Kruger effect as mainly a statistical artifact. "
            "It is based on the idea that the statistical effect known as regression toward the mean explains the empirical findings. "
            "This effect happens when two variables are not perfectly correlated",
            nome="Dunning–Kruger effect")],
    },
    # 2 ancoragem: a roleta e a multiplicação
    {
        "temas_secundarios": ["decisoes_economia", "experimentos_psicologia"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Pessoas que viram uma roleta parar no 65 estimaram que 45% dos países da ONU eram africanos. As que a viram parar no 10 disseram 25%. Um número sem relação nenhuma puxou a resposta.",
        "explicacao": (
            "Os psicólogos Amos Tversky e Daniel Kahneman fizeram vários experimentos sobre o que chamaram de "
            "ancoragem: a tendência de partir de um número disponível e ajustar pouco a partir dele. Num deles, "
            "antes de estimar a porcentagem de países africanos na ONU, os participantes viam uma roleta, "
            "arranjada para parar no 10 ou no 65. Quem viu 10 chutou, em média, 25%; quem viu 65, 45%. Em outro, "
            "pediram uma estimativa, em 5 segundos, do produto 1 × 2 × 3 × 4 × 5 × 6 × 7 × 8, ou da "
            "mesma conta escrita de trás para a frente. Quando a sequência começava pelos números pequenos, a "
            "estimativa mediana era 512; quando começava pelos grandes, 2.250. A resposta certa é 40.320. As "
            "primeiras multiplicações serviam de âncora, e todos ficaram muito abaixo. O efeito aparece em "
            "negociações de salário, compras e até sentenças judiciais."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Anchoring_effect",
            "asked to compute, within 5 seconds, the product of the numbers one through to eight, either as 1 × 2 × 3 × 4 × 5 × 6 × 7 × 8 or reversed as 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1. [...] "
            "When these first multiplications gave a small answer – because the sequence started with small numbers – the median estimate was 512; "
            "when the sequence started with the larger numbers, the median estimate was 2,250. (The correct answer is 40,320.) "
            "In another study by Tversky and Kahneman, participants were asked to estimate the percentage of African countries in the United Nations. "
            "Before estimating, the participants first observed a roulette wheel that was predetermined to stop on either 10 or 65. "
            "Participants whose wheel stopped on 10 guessed lower values (25% on average) than participants whose wheel stopped at 65 (45% on average). [...] "
            "anchoring occurs not only in abstract estimation tasks (like guessing the height of Mount Everest) but also in real-world contexts such as legal sentencing, consumer purchasing, salary negotiations, and forecasting.",
            nome="Anchoring effect")],
    },
    # 3 os gatos que caem de mais alto
    {
        "temas_secundarios": ["comportamento_animal", "probabilidade"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "Um estudo de 1987 achou que gatos que caem de mais de seis andares se machucam menos que os que caem de menos. Talvez seja física. Ou só porque os gatos que morrem não chegam ao veterinário.",
        "explicacao": (
            "Em 1987, um estudo com gatos levados a uma clínica veterinária depois de cair de prédios encontrou um "
            "padrão estranho: os que caíram de menos de seis andares e sobreviveram tinham ferimentos mais graves "
            "do que os que caíram de mais de seis. Uma explicação proposta é física: o gato atinge a velocidade "
            "terminal, a máxima da queda, por volta do quinto andar, depois de se endireitar no ar. A partir daí "
            "ele relaxaria o corpo, o que reduziria os ferimentos. Mas em 1996 uma coluna de jornal sugeriu outra "
            "explicação, o viés de sobrevivência: gatos que morrem na queda têm menos chance de serem levados ao "
            "veterinário do que os feridos. Se muitos dos gatos mortos nas quedas mais altas nunca entraram nos "
            "dados, a amostra mostra só os que tiveram sorte. É o mesmo raciocínio do estatístico Abraham Wald na "
            "Segunda Guerra, que estudou os danos nos aviões que voltavam das missões para decidir onde reforçar a "
            "blindagem."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "hipotese",
        "fontes": [wiki("Survivorship_bias",
            "During World War II, the statistician Abraham Wald described methods of estimating the vulnerability of various parts of an aircraft based on damage to surviving planes. [...] "
            "In his comments on his memos, Wald proposed that his conclusions could be used as guide for locating the placement of protective armor. [...] "
            "In a 1987 study, it was reported that cats who fall from fewer than six stories and are still alive have greater injuries than cats who fall from higher than six stories. "
            "It has been proposed that this might happen because cats reach terminal velocity after righting themselves at about five stories. "
            "After this point they relax, leading to less severe injuries in cats who have fallen from six or more stories. "
            "In 1996, The Straight Dope newspaper column proposed that another possible explanation for this phenomenon would be survivorship bias. "
            "Cats that die in falls are less likely to be brought to a veterinarian than injured cats",
            nome="Survivorship bias")],
    },
    # 4 o nome do fenômeno Baader-Meinhof
    {
        "temas_secundarios": ["percepcao_ilusoes", "memoria"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "Aprendeu uma palavra e agora a vê em todo lugar? É a ilusão de frequência, apelidada de fenômeno Baader-Meinhof por causa de um leitor que, em 1994, não parava de esbarrar no nome de um grupo terrorista.",
        "explicacao": (
            "Em 1994, um leitor chamado Terry Mullen escreveu a um jornal de Saint Paul, nos Estados Unidos, "
            "contando que, depois de ouvir falar uma vez do grupo militante alemão Baader-Meinhof, passou a "
            "encontrar o nome por toda parte. Outros leitores mandaram cartas com experiências parecidas, e o "
            "\"fenômeno Baader-Meinhof\" ganhou fama. Só em 2005 o linguista Arnold Zwicky, da Universidade "
            "Stanford, deu ao efeito um nome descritivo: ilusão de frequência. Para ele, a ilusão resulta de dois "
            "processos. O primeiro é a atenção seletiva: depois de conhecer algo, o cérebro passa a notá-lo no "
            "meio de todo o resto, que antes passava despercebido. O segundo é o viés de confirmação: cada novo "
            "encontro parece confirmar que aquilo ficou mais comum. A coisa não aparece mais vezes; só passa a ser "
            "notada."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Frequency_illusion",
            "The frequency illusion, also known as the Baader–Meinhof phenomenon, is a cognitive bias in which a person notices a specific concept, word, or product more frequently after recently becoming aware of it. "
            "The name \"Baader–Meinhof phenomenon\" was coined in 1994 by Terry Mullen in a letter to the St. Paul Pioneer Press. "
            "The letter describes how, after mentioning the name of the German militant group Baader–Meinhof once, he kept noticing it. "
            "This led to other readers sharing their own experiences of the phenomenon, leading it to gain recognition. "
            "It was not until 2005, when Stanford linguistics professor Arnold Zwicky wrote about this effect on his blog, that the name \"frequency illusion\" was coined. [...] "
            "Zwicky considered this illusion a result of two psychological processes: selective attention and confirmation bias.",
            nome="Frequency illusion")],
    },
    # 5 Monte Carlo, 1913
    {
        "temas_secundarios": ["jogos_azar", "probabilidade"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Em 1913, uma roleta de Monte Carlo deu preto 26 vezes seguidas. Os jogadores perderam milhões de francos apostando no vermelho, certos de que ele \"tinha\" de sair.",
        "explicacao": (
            "A falácia do jogador é acreditar que um resultado que saiu pouco está \"atrasado\" e por isso tem mais "
            "chance de sair, mesmo quando cada rodada é independente. O exemplo mais famoso deu a ela outro nome, "
            "falácia de Monte Carlo. Em 1913, no Cassino de Monte Carlo, a bola de uma roleta caiu no preto 26 "
            "vezes seguidas. Era algo extremamente improvável: numa roleta com um só zero, a chance de uma "
            "sequência de 26 giros dar sempre a mesma cor é de cerca de 1 em 68,4 milhões. Mas cada giro "
            "continuava tendo a mesma chance de antes. Os jogadores, convencidos de que a sequência tinha "
            "desequilibrado a roleta e de que viria uma longa série de vermelhos, perderam milhões de francos "
            "apostando contra o preto. A roda não tem memória: depois de 25 pretos, o 26º tinha a mesma chance de "
            "qualquer outro."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Gambler%27s_fallacy",
            "The gambler's fallacy, also known as the Monte Carlo fallacy or the fallacy of the maturity of chances, is the belief that an independent and equally probable outcome which happened less frequently than expected is more likely to happen in the future (or vice versa). [...] "
            "The term Monte Carlo fallacy originates from an example of the phenomenon, in which the roulette wheel spun black 26 times in succession at the Monte Carlo Casino in 1913. [...] "
            "for any given sequence of 26 spins, the probability of either red or black occurring 26 times in a row on a single zero roulette wheel is 2×(⁠18/37⁠)26 or around 1 in 68.4 million, assuming the mechanism is unbiased. "
            "Gamblers lost millions of francs betting against black, reasoning incorrectly that the streak was causing an imbalance in the randomness of the wheel, and that it had to be followed by a long streak of red.",
            nome="Gambler's fallacy")],
    },
    # 6 a "mão quente" talvez exista
    {
        "temas_secundarios": ["probabilidade", "ciencia_esporte"],
        "tipos_espanto": ["contraintuitivo", "misterio_aberto"],
        "gancho": "Por 30 anos, a \"mão quente\" do basquete foi o exemplo clássico de viés. Em 2015, dois economistas acharam um erro estatístico no estudo original: a sequência quente talvez exista mesmo.",
        "explicacao": (
            "Em 1985, os psicólogos Thomas Gilovich, Amos Tversky e Robert Vallone testaram a crença de que um "
            "jogador de basquete que acerta alguns arremessos seguidos fica mais propenso a acertar o próximo, a "
            "chamada mão quente. Analisando arremessos, concluíram que cada tentativa era independente das "
            "anteriores. A mão quente virou o exemplo de manual de como as pessoas enxergam padrões no acaso. Em "
            "2015, os economistas Joshua Miller e Adam Sanjurjo reexaminaram o estudo e acharam uma falha de "
            "método: em sequências curtas, um viés estatístico faz as viradas parecerem mais prováveis do que as "
            "continuações. Corrigido isso, a conclusão se inverteu, e eles concluíram que a mão quente pode "
            "existir. Um estudo de 2021 com dados dos torneios de três pontos da NBA, de 1986 a 2020, encontrou "
            "evidência considerável do efeito. Outros estudos recentes não acharam nada, e a discussão continua."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Hot_hand",
            "The fallacy was first described in a 1985 paper by Thomas Gilovich, Amos Tversky, and Robert Vallone. [...] "
            "In 2015, an examination of the 1985 study by Joshua Miller and Adam Sanjurjo found flaws in the methodology of the 1985 study and showed that, in fact, the hot hands may exist. [...] "
            "The authors concluded that people were right to believe that the hot hand exists in basketball. "
            "A 2021 study, using data from NBA Three-Point Contests over the period 1986–2020, found \"considerable evidence of hot hand shooting in and across individuals\". "
            "However, other recent studies have not observed evidence of the \"hot hand\". [...] "
            "the researchers accounted for a statistical bias caused by the “law of small numbers”—a tendency for reversals to appear more likely than continuations in short sequences of data.",
            nome="Hot hand")],
    },
    # 7 o efeito Ben Franklin
    {
        "temas_secundarios": ["psicologia_social", "revolucoes_politicas"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Para conquistar um rival, Benjamin Franklin não lhe fez um favor: pediu um. Pediu emprestado um livro raro, e o adversário virou amigo. Pedir ajuda pode aumentar a simpatia de quem ajuda.",
        "explicacao": (
            "Na autobiografia, Benjamin Franklin conta como lidou com a hostilidade de um colega da Assembleia da "
            "Pensilvânia, no século XVIII. Sabendo que o rival tinha na biblioteca um livro muito raro, escreveu-"
            "lhe pedindo o favor de emprestá-lo por alguns dias. O homem mandou o livro na hora. Franklin o "
            "devolveu uma semana depois, com um bilhete de agradecimento. Na sessão seguinte, o rival falou com ele "
            "pela primeira vez, com grande cortesia, e os dois viraram amigos até a morte dele. Franklin citou "
            "uma velha máxima: quem já te fez um favor estará mais disposto a fazer outro do que alguém a quem você "
            "fez um favor. Em 1969, um experimento de Jon Jecker e David Landy testou a ideia. A explicação mais "
            "comum é a coerência: se ajudei alguém, devo gostar dessa pessoa, e a atitude se ajusta ao "
            "comportamento."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Ben_Franklin_effect",
            "In this way, the effect shows how people adjust their attitudes to maintain consistency in their self-concept. [...] "
            "\"He that has once done you a kindness will be more ready to do you another, than he whom you yourself have obliged.\" "
            "Franklin explains how he dealt with the animosity of a rival legislator when he served as a member of the Pennsylvania Provincial Assembly in the 18th century: "
            "Having heard that he had in his library a certain very scarce and curious book, I wrote a note to him, expressing my desire of perusing that book, and requesting he would do me the favour of lending it to me for a few days. "
            "He sent it immediately, and I return'd it in about a week with another note, expressing strongly my sense of the favour. "
            "When we next met in the House, he spoke to me (which he had never done before), and with great civility; and he ever after manifested a readiness to serve me on all occasions, so that we became great friends, and our friendship continued to his death. [...] "
            "A study of the effect was done by Jon Jecker and David Landy in 1969",
            nome="Ben Franklin effect")],
    },
    # 8 a opção que ninguém escolhe
    {
        "temas_secundarios": ["decisoes_economia", "comercio_rotas"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Ninguém escolheu a assinatura só impressa da Economist, que custava o mesmo que impressa mais digital. Mas, quando ela foi tirada do menu, a maioria passou a preferir a opção mais barata.",
        "explicacao": (
            "No livro \"Previsivelmente Irracional\", o economista comportamental Dan Ariely conta um caso real da "
            "revista The Economist. A página de assinaturas tinha três opções: só digital, por 59 dólares; só "
            "impressa, por 125; e impressa mais digital, também por 125. Num experimento de Ariely com estudantes, "
            "16% escolheram a digital, ninguém escolheu a só impressa e 84% ficaram com o pacote completo. Quando "
            "ele tirou a opção que ninguém queria, o resultado se inverteu: 68% escolheram a digital e só 32% o "
            "pacote. É o efeito chamariz: uma opção claramente pior que outra, sem ser escolhida, muda a forma "
            "como comparamos as demais e faz a vizinha mais cara parecer um ótimo negócio."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Decoy_effect",
            "Another example shown in Dan Ariely's book Predictably Irrational was a true case used by The Economist magazine. "
            "The subscription screen presented three options: "
            "Economist.com subscription - US$59.00. [...] "
            "Print subscription - US$125.00. [...] "
            "Print & web subscription - US$125.00. [...] "
            "Given these choices, 16% of the students in the experiment conducted by Ariely chose the first option, 0% chose the middle option, and 84% chose the third option. "
            "Even though nobody picked the second option, when he removed that option the result was the inverse: 68% of the students picked the online-only option, and 32% chose the print and web option.",
            nome="Decoy effect")],
    },
    # 9 o efeito IKEA
    {
        "temas_secundarios": ["decisoes_economia", "emocoes"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Num estudo de 2011, pessoas aceitaram pagar 63% a mais por um móvel que elas mesmas montaram do que por um igual já montado. É o efeito IKEA: o trabalho basta para aumentar o apego.",
        "explicacao": (
            "Os pesquisadores Michael Norton, de Harvard, Daniel Mochon, de Yale, e Dan Ariely, de Duke, quiseram "
            "saber se as pessoas valorizam mais o que ajudaram a fazer. Em três experimentos, os participantes "
            "montaram peças de Lego, dobraram figuras de origami e montaram caixas da IKEA. Uma parte montava a "
            "caixa; outra só examinava uma já pronta. Depois, todos diziam quanto pagariam pelo objeto. Quem tinha "
            "montado aceitou pagar 63% a mais pelo próprio móvel do que os outros pelo móvel pré-montado. Os "
            "autores resumiram: só o trabalho já basta para fazer alguém gostar mais do resultado do próprio "
            "esforço. O nome homenageia a loja sueca, famosa pelos móveis vendidos desmontados."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("IKEA_effect",
            "The name refers to Swedish manufacturer and furniture retailer IKEA, which sells many items of furniture that require assembly. "
            "A 2011 study found that subjects were willing to pay 63% more for furniture they had assembled themselves than for equivalent pre-assembled items. [...] "
            "The IKEA effect was identified and named by Michael I. Norton of Harvard Business School, Daniel Mochon of Yale, and Dan Ariely of Duke, who published the results of three studies in 2011. "
            "They described the IKEA effect as \"labor alone can be sufficient to induce greater liking for the fruits of one's labor [...] "
            "The research consisted of three different experiments in which the participants built Lego items, folded origami figures and assembled IKEA boxes. "
            "In the first part of the experiment, part of the subjects were given the task of assembling IKEA furniture, while others were allowed to examine a pre-built version of the same furniture.",
            nome="IKEA effect")],
    },
]
