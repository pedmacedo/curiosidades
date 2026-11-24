LOTE = "2026-11-24-experimentos_psicologia-01"
AREA = "mente"
TEMA = "experimentos_psicologia"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o teste do marshmallow encolheu
    {
        "temas_secundarios": ["desenvolvimento_humano", "decisoes_economia"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "O teste do marshmallow parecia mostrar que crianças que esperavam pelo doce iam melhor na vida. Refeito em 2018 com amostra dez vezes maior, achou só metade do efeito; a origem econômica parecia explicar a outra metade.",
        "explicacao": (
            "A série de estudos começou no fim dos anos 1960, com Walter Mischel e colegas, na Universidade "
            "Stanford: a criança podia comer logo uma guloseima ou esperar para ganhar uma recompensa maior ou "
            "preferida. O marshmallow só entrou num estudo de 1972; antes, eram biscoitos de bichinhos e palitos "
            "de pretzel. Nos acompanhamentos, quem tinha esperado mais tendia a ter notas melhores no exame SAT, "
            "mais escolaridade e melhor índice de massa corporal. Mas as crianças originais vinham de uma "
            "pré-escola da própria Stanford. A repetição de Watts, Duncan e Quan, de 2018, usou uma população bem "
            "mais diversa: sobrou uma ligação com testes de desempenho aos 15 anos, menor que a original, que "
            "encolheu ainda mais quando se levaram em conta a capacidade cognitiva precoce, a família e o ambiente "
            "de casa. Outro estudo, de 2012, mexeu na confiança: antes do teste, metade das crianças viu o adulto "
            "quebrar uma promessa, e a outra metade o viu cumprir. As do segundo grupo esperaram até quatro vezes "
            "mais, 12 minutos. Para os autores, isso põe em dúvida a leitura de que tudo se resume a autocontrole: "
            "esperar pode ser uma estratégia que só faz sentido quando se confia em quem prometeu. Em 2024, um "
            "estudo concluiu que o desempenho no teste não prevê com segurança como a pessoa estará na vida adulta."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Stanford_marshmallow_experiment",
            "The Stanford marshmallow experiment refers to a series of studies on delayed gratification led by psychologist Walter Mischel and collaborators at Stanford University starting in the late 1960s. "
            "The studies involved offering child participants a smaller, immediate reward, or a larger (or more preferred) reward if they waited for a period of time. "
            "Marshmallows were first introduced as a reward in the 1972 study by Mischel, Ebbe B. Ebbesen, and Antonette Raskoff Zeiss [...] "
            "Prior to that, Mischel and Ebbesen had run a 1970 delay-of-gratification study using animal cookies and pretzel sticks. [...] "
            "In follow-up studies, the researchers found that children who were able to wait longer for the preferred rewards tended to have better life outcomes, as measured by SAT scores, educational attainment, body mass index (BMI), and other life measures. "
            "A replication attempt with a sample from a more diverse population that was over 10 times larger than the original study showed only half the effect of the original study. "
            "The replication suggested that economic background, rather than willpower, explained the other half. [...] "
            "A 2012 study at the University of Rochester (with a smaller N= 28) altered the experiment by dividing children into two groups: one group was given a broken promise before the marshmallow test was conducted (the unreliable tester group), and the second group had a fulfilled promise before their marshmallow test (the reliable tester group). "
            "The reliable tester group waited up to four times longer (12 min) than the unreliable tester group for the second marshmallow to appear. "
            "The authors argue that this calls into question the original interpretation of self-control as the critical factor in children's performance, since self-control should predict ability to wait, not strategic waiting when it makes sense. [...] "
            "Participants of the original studies at the Bing School at Stanford University appeared to have no doubt that they would receive a reward [...] "
            "Watts, Duncan, and Quan's 2018 conceptual replication yielded mostly statistically insignificant correlations with behavioral problems but a significant correlation with achievement tests at age 15. [...] "
            "These effects were lower than in the original experiment and reduced further when controlling for early cognitive ability and behavior, family background, and home environment. [...] "
            "A 2024 study extended the approach of Watts et al and found that \"Marshmallow Test performance does not reliably predict adult outcomes.\"",
            nome="Stanford marshmallow experiment")],
    },
    # 2 a força de vontade que não se esgota
    {
        "temas_secundarios": ["vieses_cognitivos", "decisoes_economia"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "A psicologia ensinou por anos que a força de vontade se esgota com o uso, como um músculo cansado. Em 2016, uma repetição em 23 laboratórios não achou o efeito. Outra, com 36 laboratórios e 3.531 pessoas, também não.",
        "explicacao": (
            "A ideia, chamada de esgotamento do ego, foi proposta pelo psicólogo Roy Baumeister e colegas: o "
            "autocontrole seria como um músculo, que se fortalece mas também se cansa. Num experimento de 1998, "
            "quem antes tinha resistido à tentação de chocolates desistia mais cedo de um quebra-cabeça difícil e "
            "frustrante. Vieram muitos estudos, e até a proposta de que o combustível do autocontrole seria a "
            "glicose do sangue, parte da qual depois foi questionada. Até meados da década de 2010, a confiança no "
            "efeito era grande. Então análises apontaram viés de publicação: os estudos eram pequenos demais, e os "
            "resultados negativos que deveriam aparecer simplesmente não estavam nas revistas. Martin Hagger e Nikos "
            "Chatzisarantis, autores de uma meta-análise de 2010 que parecia apoiar o efeito, organizaram uma "
            "replicação pré-registrada: 2.141 participantes em duas dezenas de laboratórios, com um protocolo único. "
            "Nenhum sinal de esgotamento. Baumeister e Kathleen Vohs reclamaram que o protocolo original tinha sido "
            "recusado. Veio então outro projeto, liderado pela própria Vohs, com 36 laboratórios e 3.531 "
            "participantes. Também não achou o efeito: o tamanho medido ficou uma ordem de grandeza abaixo da "
            "estimativa da meta-análise de 2010. As conclusões desses estudos ainda não são aceitas por todos, mas "
            "a ideia passou a ser citada como exemplo da crise de replicação."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Ego_depletion",
                "Some meta-analyses and studies have questioned the size and existence of the ego depletion effect. "
                "The ultimate validity and conclusions of those later studies are not universally agreed upon. "
                "Martin Hagger and Nikos Chatzisrantis, whose 2010 meta-analysis seemed to support the existence of the ego depletion effect, subsequently performed a pre-registered 23-lab replication study that did not find an ego-depletion effect. [...] "
                "American social psychologist Roy Baumeister and his colleagues proposed a model that described self-control like a muscle, which can become both strengthened and fatigued. [...] "
                "An experiment by Baumeister, Ellen Bratslavsky, Mark Muraven, and Dianne Tice in 1998 [...] "
                "They showed that people who initially resisted the temptation of chocolates were subsequently less able to persist on a difficult and frustrating puzzle task. [...] "
                "Multiple experiments have connected self-control depletion to reduced blood glucose, and suggested that self-control performance could be replenished by consuming glucose. "
                "Some of the findings were later questioned. [...] "
                "Although up until the mid-2010s there was widespread confidence in the robustness of the ego depletion effect, a substantial body of research has since cast doubt on the replicability of the effect. [...] "
                "Based on the low power of studies, one would expect a large number of non-significant results, but these results are missing from published articles. "
                "This finding supports Carter and McCullough's meta-analysis that showed publication bias with a different statistical method. [...] "
                "In 2016, a major multi-lab replication study (2141 participants) carried out at two dozen labs across the world using a single protocol failed to find any evidence for ego depletion. "
                "In response, Baumeister and Vohs argued that Baumeister's original protocol was rejected by the project coordinators [...] "
                "However, a subsequent, separate multi-lab replication project, led by Kathleen Vohs and involving 36 labs testing 3531 participants, also failed to find an ego-depletion effect (d = 0.06; an order of magnitude smaller than the effect size estimate in the original Hagger meta-analysis).",
                nome="Ego depletion"),
            wiki("Replication_crisis",
                "Some areas of psychology once considered solid, such as social priming and ego depletion, have come under increased scrutiny due to failed replications.",
                nome="Replication crisis"),
        ],
    },
    # 3 a pose de poder renegada pela própria autora
    {
        "temas_secundarios": ["emocoes", "vieses_cognitivos"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Ficar alguns minutos numa postura expansiva mudaria os hormônios e daria confiança, dizia um estudo de 2010 que virou palestra TED famosa. Em 2016, a autora principal do estudo declarou não acreditar mais no efeito.",
        "explicacao": (
            "O estudo, de Dana Carney, Amy Cuddy e Andy Yap, teve 42 participantes. Os autores relataram que, depois "
            "da pose, a testosterona subia e o cortisol caía, e imaginaram usos em entrevistas de emprego e "
            "negociações de salário. Cuddy levou a ideia a uma palestra TED em 2012, que em 2017 já somava cerca de "
            "47 milhões de visualizações. Em 2015, uma repetição com amostra maior, de Ranehill e colegas, só "
            "confirmou que as pessoas se sentiam mais poderosas: não apareceu efeito nenhum nos hormônios nem no "
            "comportamento. Em 2016, Carney, que tinha sido a primeira autora do artigo original, publicou no site "
            "da Universidade da Califórnia em Berkeley que não acreditava que os efeitos da pose de poder fossem "
            "reais. Em 2017, uma edição especial de revista reuniu onze estudos novos, pré-registrados, e também "
            "não achou efeito sobre comportamentos. A discussão não terminou ali: uma revisão de 128 estudos "
            "encontrou um efeito confiável sobre pensamentos e sentimentos, como humor e autoestima, mas nenhum "
            "sobre medidas fisiológicas, como hormônios e pressão. E poucos estudos tiveram um grupo com postura "
            "neutra: muitos compararam a pose expansiva só com a postura curvada, e assim não dá para saber de "
            "qual das duas vem a diferença."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Power_posing",
            "Power posing is the practice of standing in a posture mentally associated with being powerful, in the hope of feeling more confident and behaving more assertively. [...] "
            "simply by assuming a \"powerful\" or \"expansive\" posture for a few minutes before an interaction in which confidence is needed. [...] "
            "Power posing was first suggested in a 2010 paper by Dana R. Carney, Amy Cuddy, and Andy Yap in the journal Psychological Science, and came to prominence through a popular TED talk by Cuddy in 2012. "
            "However, in 2015 several researchers began reporting that the effect could not be replicated, and, in 2016, Carney issued a statement abandoning the theory. [...] "
            "The study included 42 participants, who were coached by researchers to assume a physical position of power. "
            "Hormone levels were measured before and after, and the authors stated that they found an increase in testosterone and a decrease in cortisol after posing. [...] "
            "which can lead to better outcomes in work-related situations, such as job interviews and wage negotiations. [...] "
            "A 2015 article, published in Psychological Science by Ranehill et al. reported the results of a conceptual replication of the study using a larger sample. "
            "The researchers confirmed Carney et al.'s results about felt power but could not detect any physiological or behavioral effects of power posing. [...] "
            "In 2016, Dana Carney, who had been the lead author on the original 2010 paper and had supported the publication of the 2015 Ranehill et al. replication attempt, published a statement on the University of California, Berkeley website, stating that she no longer believed the effect was valid: "
            "\"I do not believe that 'power pose effects' are real...the evidence against the existence of power poses is undeniable.\" [...] "
            "arranged a special issue on power posing that published in June 2017; the issue included eleven new studies, along with a meta-analyses, which found that the effect of power posing on power behaviors was not replicated. "
            "The published studies were designed to answer whether the power-posing hypothesis was real and included high quality research features like pre-registration of endpoints. [...] "
            "A comprehensive meta-analytic review that analyzed 128 studies on the topic of body postures such as power posing, considering both published and unpublished papers, suggests that power posing has a reliable effect on thoughts and feelings (e.g., positive mood, self-esteem, feelings of dominance). "
            "However, power posing has no effect on physiological measures (e.g., hormone levels, blood pressure, skin conductance). [...] "
            "Few studies have included a control group (neutral posture), so it remains unclear whether the effect comes from dominant postures (so-called high power poses) or from submissive, slumped postures (so-called low power poses). [...] "
            "Many studies compared an expansive \"power pose\" only with a contractive pose, such as slouching, and failed to include a neutral, ordinary pose as a baseline. [...] "
            "by 2017 her TED talk had been viewed by about 47 million viewers",
            nome="Power posing")],
    },
    # 4 quem era o Pequeno Albert?
    {
        "temas_secundarios": ["desenvolvimento_humano", "emocoes"],
        "tipos_espanto": ["historia_humana", "misterio_aberto"],
        "gancho": "Num estudo publicado em 1920, John Watson fez um bebê ter medo de um rato branco batendo numa barra de aço atrás dele. Quem era o \"Pequeno Albert\"? Pesquisadores já apontaram dois bebês diferentes.",
        "explicacao": (
            "Watson e sua aluna de pós-graduação Rosalie Rayner, da Universidade Johns Hopkins, seguiram os "
            "procedimentos de Pavlov com cães para tentar criar uma fobia numa criança. Aos 9 meses, Albert brincava "
            "com o rato sem medo nenhum. Então, cada vez que ele tocava no animal, alguém golpeava com um martelo "
            "uma barra de aço às suas costas. Depois de algumas repetições, bastava ver o rato para o bebê chorar e "
            "engatinhar para longe, e a aflição pareceu se estender a um coelho, um cachorro e um casaco de pele. "
            "A mãe o tirou do estudo antes que se tentasse desfazer o medo. Em 2009, Hall Beck e Sharman Levinson "
            "propuseram que Albert era Douglas Merritte, filho de uma provável ama de leite do hospital. Merritte "
            "tinha hidrocefalia e morreu aos 6 anos, o que contrariava a descrição de um bebê saudável. Russ "
            "Powell, Nancy Digdon e Ben Harris contestaram: o prontuário de Merritte o descrevia como totalmente "
            "cego, o que não combina com os filmes do experimento. O candidato deles é Albert Barger, que nasceu "
            "com um dia de diferença e deixou o hospital exatamente na idade registrada no estudo. Barger morreu em "
            "2007, aos 87 anos. Uma sobrinha contou que ele tinha aversão a cães e que a família brincava com isso. "
            "Não há como saber se isso tinha relação com o experimento."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Little_Albert_experiment",
            "It was carried out by John B. Watson and his graduate student, Rosalie Rayner, at Johns Hopkins University. "
            "The results were first published in the February 1920 issue of the Journal of Experimental Psychology. [...] "
            "The aim of Watson and Rayner was to condition a phobia in an emotionally stable child. [...] "
            "Watson followed the procedures which Ivan Pavlov had used in his experiments with dogs. [...] "
            "Albert showed no fear of any of these items during the baseline tests. "
            "For the proper experiment, by which point Albert was 9 months old, he was put on a mattress on a table in the middle of a room. "
            "A white laboratory rat was placed near Albert and he was allowed to play with it. "
            "At this point, Watson and Rayner made a loud sound behind Albert's back by striking a suspended steel bar with a hammer each time the baby touched the rat. "
            "Albert responded to the noise by crying and demonstrating fear. "
            "After several such pairings of the two stimuli, Albert was presented with only the rat. "
            "Upon seeing the rat, Albert became very distressed, crying and crawling away. [...] "
            "He became distressed at the sight of several other furry objects, such as a rabbit, a furry dog, a fur coat [...] "
            "Albert's mother, who had not been fully informed of the nature of the experiment, withdrew her son from the study before any reversal could take place [...] "
            "In 2009, psychologists Hall P. Beck and Sharman Levinson published an article in which they claimed to have discovered the true identity of \"Albert B.\" [...] "
            "Beck argued that \"Albert B.\" was a pseudonym for Douglas Merritte, the son of Arvilla Merritte, then a woman who appears to have been a wet nurse at the Harriet Lane Home. "
            "It was later found that Douglas Merritte had hydrocephalus, from which he died at the age of 6. [...] "
            "this disputes the claim that the child in question was average and healthy. [...] "
            "The identity claimed by Beck, et al., has been contested by psychology researchers Russ Powell, Nancy Digdon and Ben Harris, who offer an alternative identity based on available data. "
            "Albert Barger had been born within a day of Merritte, and his mother had also worked at the hospital where the experiment was conducted. [...] "
            "the exact age Albert Barger had been when he left the hospital. "
            "Finally, when Powell et al. were allowed to independently verify Douglas Merritte's clinical file, it was revealed that he was \"completely blind\", which is at odds with the experiment's films [...] "
            "the researchers learned Barger had died in 2007 at age 87 and identified one close living relative, a niece. "
            "In an interview, Barger's niece stated that she and her uncle had been quite close throughout his life, and acknowledged Barger's antipathy toward dogs as a well-known fact that family members, particularly his wife, would tease him about (the researchers noted there was no way to determine whether or not this behavior was linked to Watson's experiment).",
            nome="Little Albert experiment")],
    },
    # 5 o efeito Pigmalião e o relógio que bate 13
    {
        "temas_secundarios": ["aprendizagem_inteligencia", "vieses_cognitivos"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "No estudo do efeito Pigmalião, professores ouviram que alguns alunos, sorteados, iam desabrochar, e o QI deles teria subido. Um crítico notou que, pelo teste usado, uma turma comum tinha QI médio na faixa da deficiência.",
        "explicacao": (
            "Robert Rosenthal e Lenore Jacobson aplicaram um teste de QI disfarçado em todos os alunos de uma "
            "escola primária da Califórnia. Aos professores, disseram que alguns alunos, cerca de 20% da escola, "
            "escolhidos na verdade por sorteio, deviam \"desabrochar\" intelectualmente naquele ano. No fim, todos "
            "refizeram o teste. As seis séries tiveram ganho médio de QI, tanto no grupo dos \"desabrochadores\" "
            "quanto no de controle, mas a vantagem dos escolhidos só foi significativa na primeira e na segunda "
            "série. Rosenthal chegou a afirmar ganhos de 24,8 pontos acima dos do grupo de controle. O psicólogo "
            "educacional Robert Thorndike apontou que o instrumento era muito falho: numa turma regular, a média "
            "de QI de raciocínio caía na faixa da deficiência intelectual, algo improvável numa escola comum. Ele "
            "citou um colega: quando o relógio bate treze, a dúvida recai não só sobre a última badalada, mas sobre "
            "todas as anteriores. Uma meta-análise de Raudenbush mostrou que, quando os professores já conheciam "
            "os alunos havia duas semanas, o efeito da expectativa induzida caía praticamente a zero. Desde os "
            "anos 1980, vários estudos não reproduziram os resultados e acharam só um efeito muito fraco, numa "
            "pequena minoria de 5% a 10% dos alunos. Uma meta-análise de 2005 concluiu que profecias "
            "autorrealizáveis na sala de aula acontecem, mas costumam ser pequenas e passageiras."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Pygmalion_effect",
            "All students in a single California elementary school were given a disguised IQ test at the beginning of the study. "
            "These scores were not disclosed to teachers. "
            "Teachers were told that some of their students (about 20% of the school chosen at random) could be expected to be \"intellectual bloomers\" that year, doing better than expected in comparison to their classmates. [...] "
            "At the end of the study, all students were again tested with the same IQ test used at the beginning of the study. "
            "All six grades in both experimental and control groups showed a mean gain in IQ from before the test to after the test. "
            "However, first- and second-graders showed statistically significant gains favoring the experimental group of \"intellectual bloomers\". [...] "
            "The educational psychologist Robert L. Thorndike described the poor quality of the Pygmalion study. "
            "The problem with the study was that the instrument used to assess the children's IQ scores was seriously flawed. "
            "The average reasoning IQ score for the children in one regular class was in the mentally disabled range, a highly unlikely outcome in a regular class in a garden variety school. [...] "
            "Quoting a colleague, Thorndike wrote about the measurement problems of the study in this way: \"When the clock strikes thirteen, doubt is cast not only on the last stroke but also all that have gone before\" [...] "
            "Moreover, a meta-analysis conducted by Raudenbush showed that when teachers had gotten to know their students for two weeks, the effect of a prior expectancy induction was reduced to virtually zero. "
            "A 2005 meta-analysis of 35 years of research on teacher expectations found that, while self-fulfilling prophecies in the classroom do occur, the effects are usually small and temporary. [...] "
            "Rosenthal had originally claimed the treatment group's IQ gain over time was \"24.8 IQ points in excess of the gain shown by the controls,\" and that these gains were persistent and widespread, but several studies since the 1980s have failed to replicate these results. "
            "Instead, they have found only a very weak effect, and only in a very small minority (5 to 10%) of students.",
            nome="Pygmalion effect")],
    },
    # 6 as mães de pano de Harlow
    {
        "temas_secundarios": ["comportamento_animal", "desenvolvimento_humano"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Filhotes de macaco escolhiam entre uma \"mãe\" de arame com leite e outra de pano, sem comida. Ficavam agarrados à de pano e só iam à de arame para mamar. Na época, achava-se que o contato físico fazia mal aos bebês.",
        "explicacao": (
            "Os experimentos foram feitos pelo psicólogo americano Harry Harlow, na Universidade de "
            "Wisconsin-Madison. O contexto ajuda a entender o impacto: o contato físico com bebês era considerado "
            "prejudicial ao desenvolvimento, e essa visão levou a berçários esterilizados e sem contato pelo país. "
            "A escola dominante, o behaviorismo, tratava as emoções como desprezíveis, e a alimentação era vista "
            "como o principal fator do vínculo entre mãe e filho. Harlow criou mães artificiais para filhotes de "
            "macaco-rhesus e testou as duas combinações: leite só na de arame, ou só na de pano. Os filhotes "
            "preferiram, de longe, passar o tempo agarrados à de pano. Em ambiente novo, com a mãe de pano por "
            "perto, eles se agarravam a ela, saíam para explorar e voltavam quando se assustavam; sem ela, ficavam "
            "paralisados de medo, encolhidos e chupando o dedo. Os criados só com a mãe de arame ganhavam peso no "
            "mesmo ritmo, mas tinham mais diarreia e dificuldade de digerir o leite. Harlow chamou o fator de "
            "\"conforto do contato\". Seus experimentos posteriores, porém, deixaram filhotes em isolamento por até "
            "24 meses, de onde saíam intensamente perturbados, e alguns pesquisadores os citam como um fator no "
            "surgimento do movimento de libertação animal nos EUA. Críticos lembram ainda que se agarrar é questão "
            "de sobrevivência para o filhote de rhesus, mas não para o bebê humano."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Harry_Harlow",
            "Harry Frederick Harlow (October 31, 1905 – December 6, 1981) was an American psychologist [...] "
            "He conducted most of his research at the University of Wisconsin–Madison [...] "
            "Later in his career, he cultivated infant monkeys in isolation chambers for up to 24 months, from which they emerged intensely disturbed. "
            "Some researchers cite the experiments as a factor in the rise of the animal liberation movement in the United States. [...] "
            "Physical contact with infants was considered harmful to their development, and this view led to sterile, contact-less nurseries across the country. [...] "
            "To investigate the debate, Harlow created inanimate surrogate mothers for the rhesus infants from wire and wood. [...] "
            "In one situation, the wire mother held a bottle with food, and the cloth mother held no food. "
            "In the other situation, the cloth mother held the bottle, and the wire mother had nothing. "
            "Overwhelmingly, the infant macaques preferred spending their time clinging to the cloth mother. "
            "Even when only the wire mother could provide nourishment, the monkeys visited her only to feed. "
            "Harlow concluded that there was much more to the mother–infant relationship than milk, and that this \"contact comfort\" was essential to the psychological development and health of infant monkeys and children. [...] "
            "When the infant's surrogate mother was present, it clung to her, but then began venturing off to explore. "
            "If frightened, the infant ran back to the surrogate mother and clung to her for a time before venturing out again. "
            "Without the surrogate mother's presence, the monkeys were paralyzed with fear, huddling in a ball and sucking their thumbs. [...] "
            "Both groups gained weight at equal rates, but the monkeys raised on a wire-mother had softer stool and trouble digesting the milk, frequently suffering from diarrhea. [...] "
            "the insistence of the predominant behaviorist school of psychology that emotions were negligible. "
            "Feeding was thought to be the most important factor in the formation of a mother–child bond. [...] "
            "Critics of Harlow's research have observed that clinging is a matter of survival in young rhesus monkeys, but not in humans",
            nome="Harry Harlow")],
    },
    # 7 o Rat Park, o vício e a repetição que não veio
    {
        "temas_secundarios": ["farmacos", "comportamento_animal"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Ratos sozinhos em gaiolas pequenas beberam mais água com morfina que ratos num \"parque\" amplo, com companhia e brinquedos. O Rat Park virou símbolo de que o vício nasce do isolamento, mas não se confirmou ao ser refeito.",
        "explicacao": (
            "Os estudos foram feitos no fim dos anos 1970 pelo psicólogo canadense Bruce Alexander e colegas, na "
            "Universidade Simon Fraser, e publicados entre 1978 e 1981. Na época, as pesquisas com morfina em "
            "animais usavam gaiolas metálicas pequenas e solitárias, e Alexander suspeitou que isso inflava o "
            "consumo. O Rat Park tinha 200 vezes a área de uma gaiola comum, 16 a 20 ratos dos dois sexos, bolas e "
            "rodas. Os ratos podiam escolher entre água pura e uma solução adoçada de morfina. Numa das condições, "
            "os machos engaiolados beberam 19 vezes mais morfina que os do parque. Ratos forçados a tomar morfina "
            "por 57 dias, levados depois ao parque, preferiram a água pura. Só que um aluno de pós-graduação do "
            "próprio Alexander, Bruce Petrie, tentou repetir o estudo em 1996 e não conseguiu, talvez por diferenças "
            "entre linhagens de ratos. Os originais também tinham problemas: poucos animais, morfina amarga tomada "
            "pela boca, medições diferentes entre os grupos, falhas de equipamento, dados perdidos e mortes de "
            "ratos. Em 2015, o jornalista Johann Hari levou o estudo a uma palestra TED, e o canal Kurzgesagt fez "
            "um vídeo baseado no livro dele que passou de 19 milhões de visualizações; depois, o canal o tirou do "
            "ar, dizendo ter representado mal as evidências. O que fica é um alerta mais modesto: gaiolas pobres "
            "afetam o comportamento dos animais de laboratório, e o ambiente pode contribuir para o vício, sem ser "
            "o único fator."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Rat_Park",
            "Rat Park was a series of studies into drug addiction conducted in the late 1970s and published between 1978 and 1981 by Canadian psychologist Bruce K. Alexander and his colleagues at Simon Fraser University in British Columbia, Canada. "
            "At the time of the studies, research exploring the self-administration of morphine in animals often used small, solitary metal cages. "
            "Alexander hypothesized that these conditions may be responsible for exacerbating self-administration. "
            "To test this hypothesis, Alexander and his colleagues built Rat Park, a large housing colony 200 times the floor area of a standard laboratory cage. "
            "There were 16–20 rats of both sexes in residence, food, balls and wheels for play, and enough space for mating. [...] "
            "One dispenser contained a sweetened morphine solution and the other plain tap water. [...] "
            "with the caged males drinking 19 times more morphine than the Rat Park males in one of the experimental conditions. [...] "
            "In another experiment, he forced rats in ordinary lab cages to consume the morphine-laced solution for 57 days without other liquid available to drink. "
            "When they moved into Rat Park, they were allowed to choose between the morphine solution and plain water. "
            "They drank the plain water. [...] "
            "Bruce Petrie (1996), a graduate student of Alexander's, attempted to replicate the study [...] "
            "The study was not able to replicate the results. "
            "The author suggested that strain differences between the rats that Alexander's research group used could be the reason. [...] "
            "Issues included the small number of subjects used, the use of oral morphine, which does not mimic actual conditions of use (and introduces a confound because of the bitterness of morphine), and the measurement of morphine consumption, which differed between conditions. "
            "Other problems included equipment failures, lost data and rat deaths. [...] "
            "Journalist Johann Hari gave a popular TED Talk about the results of the study in 2015. [...] "
            "The YouTube channel Kurzgesagt created and published a video based on Hari's book, which garnered over 19 million views. "
            "The channel later took down the video, stating that they improperly represented the evidence. "
            "Researchers have reiterated that the results of Alexander's studies highlight concerns about observations of rats kept in bare-bones lab environments, and may implicate the environment as a contributing factor in addiction. [...] "
            "it is a mistake to conclude from the study that the environment is the only factor in addiction.",
            nome="Rat Park")],
    },
    # 8 Rosenhan e os impostores que nunca existiram
    {
        "temas_secundarios": ["historia_medicina", "vieses_cognitivos"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Depois que Rosenhan contou que falsos pacientes enganaram 12 hospitais psiquiátricos, um hospital garantiu que com ele isso não aconteceria. Em três meses, apontou 41 impostores. Rosenhan não tinha mandado nenhum.",
        "explicacao": (
            "O estudo saiu em 1973 na revista Science, com o título \"On Being Sane in Insane Places\". Segundo o "
            "psicólogo David Rosenhan, da Universidade Stanford, ele e sete pessoas sem histórico de doença mental "
            "se apresentaram a hospitais psiquiátricos dizendo ouvir uma voz que repetia palavras como \"vazio\", "
            "\"oco\" e \"tum\". Todos foram internados, e depois passaram a agir normalmente. Ficaram de 7 a 52 dias, "
            "a maioria com diagnóstico de esquizofrenia, e só saíram aceitando o rótulo e os remédios, que jogavam "
            "no vaso. Uma enfermeira registrou as anotações de um deles como \"comportamento de escrita\". Nas três "
            "primeiras internações, 35 dos 118 pacientes de verdade desconfiaram que eles eram sãos. Um hospital "
            "universitário que conhecia o estudo duvidou que errasse assim, e Rosenhan combinou que mandaria "
            "falsos pacientes ao longo de três meses. Dos 193 pacientes que chegaram, a equipe apontou 41 como "
            "impostores e outros 42 como suspeitos. Todos eram pacientes comuns. Hoje o próprio estudo está sob "
            "suspeita: num livro de 2019, a escritora Susannah Cahalan relatou dados inconsistentes e citações "
            "imprecisas ou inventadas nos documentos de Rosenhan, e só conseguiu identificar dois dos oito "
            "pseudopacientes. Em 2023, Andrew Scull, da Universidade da Califórnia em San Diego, chamou o experimento de \"fraude científica bem-sucedida\"."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [wiki("Rosenhan_experiment",
            "The study was arranged by psychologist David Rosenhan, a Stanford University professor, and published by the journal Science in 1973 with the title On Being Sane In Insane Places. [...] "
            "It has been alleged that at least part of the published results were distorted or falsified. [...] "
            "Rosenhan himself and seven mentally healthy associates, termed \"pseudopatients\", attempted to gain admission to psychiatric hospitals by telephoning for an appointment and feigning auditory hallucinations. [...] "
            "None had a history of mental illness. [...] "
            "which were often unclear, but which seemed to pronounce the words \"empty\", \"hollow\", or \"thud\", and nothing else. [...] "
            "If admitted, the pseudopatients were instructed to \"act normally\", reporting that they felt fine and no longer heard voices. [...] "
            "All were admitted, to 12 psychiatric hospitals across the United States [...] "
            "Though presented with identical symptoms, seven were diagnosed with schizophrenia at public hospitals [...] "
            "Their stays ranged from 7 to 52 days, and the average was 19 days. [...] "
            "In the first three hospitalizations, 35 of the total of 118 patients expressed a suspicion that the pseudopatients were sane [...] "
            "For example, one nurse labeled the note-taking of one pseudopatient as \"writing behavior\" and considered it pathological. [...] "
            "Once admitted and diagnosed, the pseudopatients were not able to obtain their release until they agreed with the psychiatrists that they were mentally ill and began taking antipsychotic medications, which they flushed down a toilet. [...] "
            "For this experiment, Rosenhan used a well-known research and teaching hospital, the staff of which had learned of the results of the initial study but claimed that similar errors could not be made at their institution. "
            "Rosenhan arranged with them that during a three-month period, one or more pseudopatients would attempt to gain admission and the staff would rate every incoming patient as to the likelihood they were an impostor. "
            "Of 193 patients, 41 were considered to be impostors and a further 42 were considered suspect. "
            "In reality, Rosenhan had sent no pseudopatients; all patients suspected as impostors by the hospital staff were ordinary patients. [...] "
            "In The Great Pretender, a 2019 book on Rosenhan, author Susannah Cahalan questions the veracity and validity of the Rosenhan experiment. "
            "Examining documents left by Rosenhan after his death, Cahalan finds apparent distortion in the Science article: inconsistent data, misleading descriptions, and inaccurate or fabricated quotations from psychiatric records. "
            "Moreover, despite an extensive search, she is only able to identify two of the eight pseudopatients [...] "
            "In February 2023, Andrew Scull of the University of California at San Diego published an article in the peer-reviewed journal History of Psychiatry in support of Cahalan's allegations, labelling the experiment a \"successful scientific fraud\".",
            nome="Rosenhan experiment")],
    },
    # 9 o boneco Bobo: a punição não apagou o aprendizado
    {
        "temas_secundarios": ["aprendizagem_inteligencia", "desenvolvimento_humano"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Crianças que viram um adulto ser punido por bater num boneco inflável bateram menos nele depois. Mas, quando ganharam doces e figurinhas para imitar o adulto, a agressão subiu: tinham aprendido do mesmo jeito.",
        "explicacao": (
            "São os experimentos do boneco Bobo, de Albert Bandura, feitos na escola maternal da Universidade "
            "Stanford. No de 1961, com 72 crianças de 37 a 69 meses, um adulto socava o boneco, batia nele com um "
            "martelo de brinquedo e gritava frases como \"Chuta ele!\". Quem viu esse modelo agressivo depois "
            "repetiu mais agressões físicas e verbais do que quem viu um adulto calmo ou nenhum adulto. Num estudo "
            "de 1963, o efeito foi parecido com um adulto ao vivo, filmado ou com um gato de desenho animado, e "
            "ver a agressão não serviu de \"válvula de escape\". Em 1965, 66 crianças viram o adulto ser elogiado e "
            "ganhar doces, ser repreendido ou não ter consequência nenhuma. O grupo da punição imitou bem menos, "
            "sobretudo as meninas. Depois, ofereceram às crianças doces, suco e figurinhas para imitar o que tinham "
            "visto, e a agressão subiu muito nos três grupos. A leitura de Bandura: a punição alheia não impede o "
            "aprendizado, só a exibição do comportamento. Há críticas. O laboratório é artificial, e numa repetição "
            "de 1990 crianças que nunca tinham visto um boneco desses imitaram a agressão até cinco vezes mais do "
            "que as que já conheciam o brinquedo, o que sugere que parte do efeito vem da novidade."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "consenso_parcial",
        "fontes": [wiki("Bobo_doll_experiment",
            "The Bobo doll experiment was used by psychologist Albert Bandura to test his social learning theory. "
            "Between 1961 and 1963, he studied children's behaviour after watching an adult model act aggressively towards a Bobo doll. [...] "
            "For his 1963 study, Albert Bandura wanted to vary his original 1961 study [...] "
            "For his 1965 study, Albert Bandura wanted to see if children's learned behaviour would be influenced by vicarious reinforcement [...] "
            "The participants in these experiments consisted of 72 children from the Stanford University nursery school between the ages of 37 months and 69 months. [...] "
            "Examples of this aggressive behaviour include hitting or punching the Bobo doll and using the toy mallet to hit the Bobo doll in the face. "
            "The aggressive model would also verbally assault the Bobo doll, yelling phrases such as \"Sock him,\" \"Hit him down,\" \"Kick him,\" \"Throw him in the air,\" or \"Pow.\" [...] "
            "The non-aggressive adult model simply played with other toys for the entire 10-minute period. [...] "
            "Bandura found that the children exposed to the aggressive model were more likely to pursue physically aggressive behaviour than those who were not exposed to the aggressive model. [...] "
            "Bandura also found that the children exposed to the aggressive model were more likely to act in verbally aggressive ways than those who were not exposed to the aggressive model. [...] "
            "The first group watched a live model become aggressive towards a Bobo doll. "
            "The second group watched a movie version of the human model becoming aggressive toward a Bobo doll, and the third group watched a cartoon version of a cat becoming aggressive towards a Bobo doll. [...] "
            "The study results show that compared to the control group, all three groups showed similar increases in aggressive behaviour. [...] "
            "He also found that watching aggressive behaviour does not cause a cathartic effect. [...] "
            "In the experiment, 66 children, 33 boys and 33 girls were divided into one of three groups. "
            "The first group would witness a model display aggressive behaviours toward a Bobo doll, followed by a researcher praising the model for his behaviour and rewarding him with candy. "
            "The second group would witness the same scripted scenario of aggressive behaviours, but the model was instead reprimanded for his actions [...] "
            "The third group served as the control group, and the model was neither rewarded nor punished after his displayed behaviour. [...] "
            "The experiment would be repeated a second time, and this time the children would be incentivized with various rewards including candy, juice, and stickers to mimic the behaviour they just witnessed. [...] "
            "The study showed little difference between the reward and control groups; however, the punishment group displayed much less aggressive behavior, especially girls. "
            "In all three groups, personal incentives substantially increased aggressive behavior for both boys and girls. "
            "An analysis of the study shows that reinforcement and punishment do not influence learned aggressive behavior, only the outward expression of it. [...] "
            "Laboratory studies of imitation often have low ecological validity [...] "
            "When the Bobo doll experiment was repeated in 1990, findings showed that children who had not previously been exposed to a Bobo doll were up to five times more likely to imitate aggressive behavior compared to children who had been. "
            "Researchers proposed that the sheer novelty of the Bobo doll alone could be a potential third variable that increases the probability that a child imitates the adult.",
            nome="Bobo doll experiment")],
    },
    # 10 1 dólar contra 20 dólares, e a replicação de 2024
    {
        "temas_secundarios": ["vieses_cognitivos", "decisoes_economia"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Num clássico de 1959, quem ganhou 1 dólar para dizer que uma tarefa chata era divertida passou a gostar mais dela do que quem ganhou 20. Em 2024, 39 laboratórios testaram a ideia central disso e não a confirmaram.",
        "explicacao": (
            "No experimento de Leon Festinger e Merrill Carlsmith, setenta e um estudantes da Universidade Stanford passaram "
            "uma hora em tarefas tediosas, como girar pinos um quarto de volta. Depois, pedia-se a eles que "
            "convencessem outro participante, na verdade um ator, de que a tarefa era interessante. Uns receberam 20 "
            "dólares, outros 1 dólar, e um grupo de controle não precisou mentir. Na avaliação final, quem ganhou 1 "
            "dólar deu notas melhores à tarefa. A explicação foi a dissonância cognitiva: \"eu disse que era "
            "interessante\" brigava com \"achei chato\", e quem ganhou pouco não tinha uma desculpa externa, então "
            "ajustou a própria opinião. Esse tipo de experimento, chamado de obediência induzida, virou um dos mais "
            "usados para estudar a dissonância. Em 2024, uma replicação em 39 laboratórios de 19 países, com 4.898 "
            "participantes, refez uma versão posterior dele, de Croyle e Cooper: escrever uma redação contra a "
            "própria opinião, por livre escolha ou não. A previsão central falhou: ter escolhido ou não escrever "
            "não fez diferença na mudança de atitude. Escrever a redação contrária mudou a opinião em comparação "
            "com escrever uma neutra, mas, para os autores, os resultados põem em dúvida se esse tipo de "
            "experimento é uma prova robusta da dissonância cognitiva."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Cognitive_dissonance",
                "In the Cognitive Consequences of Forced Compliance (1959), the investigators Leon Festinger and Merrill Carlsmith asked students to spend an hour doing tedious tasks; e.g. turning pegs a quarter-turn, at fixed intervals. "
                "This procedure included seventy-one male students attending Stanford University. [...] "
                "Once the subjects had done the tasks, the experimenters asked one group of subjects to speak with another subject (an actor) and persuade that impostor-subject that the tedious tasks were interesting and engaging. "
                "Subjects of one group were paid twenty dollars ($20); those in a second group were paid one dollar ($1) and those in the control group were not asked to speak with the imposter-subject. "
                "At the conclusion of the study, when asked to rate the tedious tasks, the subjects of the second group (paid $1) rated the tasks more positively than did the subjects in the first group (paid $20) [...] "
                "\"I told someone that the task was interesting\" and \"I actually found it boring.\" "
                "The subjects paid one dollar were induced to comply, compelled to internalize the \"interesting task\" mental attitude because they had no other justification. "
                "The subjects paid twenty dollars were induced to comply by way of an obvious, external justification",
                nome="Cognitive dissonance"),
            {"url": "https://experts.arizona.edu/en/publications/a-multilab-replication-of-the-induced-compliance-paradigm-of-cogn/",
             "titulo": "A Multilab Replication of the Induced-Compliance Paradigm of Cognitive Dissonance (Vaidis et al., 2024)",
             "idioma": "en",
             "trecho": (
                "One of the most popular experimental paradigms used to produce such attitude change is the induced-compliance paradigm. [...] "
                "We therefore conducted a multilab constructive replication of the induced-compliance paradigm based on Croyle and Cooper (Experiment 1). "
                "In a total of 39 labs from 19 countries and 14 languages, participants (N = 4,898) were assigned to one of three conditions: writing a counterattitudinal essay under high choice, writing a counterattitudinal essay under low choice, or writing a neutral essay under high choice. "
                "The primary analyses failed to support the core hypothesis: No significant difference in attitude was observed after writing a counterattitudinal essay under high choice compared with low choice. "
                "However, we did observe a significant difference in attitude after writing a counterattitudinal essay compared with writing a neutral essay. [...] "
                "Overall, the results call into question whether the induced-compliance paradigm provides robust evidence for cognitive dissonance. [...] "
                "Priolo, D. (2024). A Multilab Replication of the Induced-Compliance Paradigm of Cognitive Dissonance. [...] "
                "Advances in Methods and Practices in Psychological Science, 7(1)")},
        ],
    },
    # 11 o Projeto de Reprodutibilidade de 2015
    {
        "temas_secundarios": ["probabilidade"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Em 2015, pesquisadores refizeram 100 estudos publicados em três das principais revistas de psicologia. Dos 97 que tinham achado um efeito, só 36% das repetições o acharam de novo, e com metade do tamanho, em média.",
        "explicacao": (
            "Foi o Projeto de Reprodutibilidade: Psicologia, coordenado por Brian Nosek, da Universidade da "
            "Virgínia, e pelo Centro para a Ciência Aberta, que ele ajudou a fundar. O trabalho começou em novembro "
            "de 2011 e escolheu estudos publicados em 2008 em três revistas de prestígio. A comparação foi feita pelo "
            "critério estatístico usual, o valor p abaixo de 0,05. Entre as repetições que falharam, 25% "
            "contradisseram diretamente o original, e 49% foram inconclusivas por falta de participantes suficientes. "
            "A taxa variou entre as revistas: 23% no Journal of Personality and Social Psychology contra 48% "
            "no Journal of Experimental Psychology: Learning, Memory, and Cognition. Os autores "
            "frisaram que o problema atinge a ciência toda, não só a psicologia. De fato, em 2021 a versão do "
            "projeto para biologia do câncer só conseguiu repetir 50 de 193 experimentos de 53 artigos de destaque, "
            "e os efeitos encontrados foram, em média, 85% menores que os originais. O projeto ajudou a mudar "
            "práticas de publicação. E teve um efeito colateral medido: leigos que souberam da baixa taxa de "
            "replicação passaram a confiar menos na psicologia do que os que ouviram que a maioria dos estudos "
            "tinha se confirmado."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Reproducibility_Project",
                "The project was led by the Center for Open Science and its co-founder, Brian Nosek, who started the project in November 2011. [...] "
                "Brian Nosek of University of Virginia and colleagues sought out to replicate 100 different studies, all published in 2008. [...] "
                "In 2021, the project showed that of 193 experiments from 53 top papers about cancer published between 2010 and 2012, only 50 experiments from 23 papers could be replicated. "
                "Moreover, it showed that the effect sizes of that fraction were 85% smaller on average than the original findings. [...] "
                "The authors emphasized that the findings reflect a problem that affects all of science and not just psychology [...] "
                "The project, along with broader action in response to the replication crisis, has helped spur changes in scientific culture and publishing practices. [...] "
                "Lay people who learned about the low replication rate found in the Reproducibility Project subsequently reported a lower trust in psychology, compared to people who were told that a high number of the studies had replicated.",
                nome="Reproducibility Project"),
            wiki("Replication_crisis",
                "In August 2015, the first open empirical study of reproducibility in psychology was published, called The Reproducibility Project: Psychology. "
                "Coordinated by psychologist Brian Nosek, researchers redid 100 studies in psychological science from three high-ranking psychology journals (Journal of Personality and Social Psychology, Journal of Experimental Psychology: Learning, Memory, and Cognition, and Psychological Science). "
                "Of 97 original studies with significant effects, 36% replicated successfully (p value below 0.05), with effect sizes averaging half the original magnitude. "
                "Among non-replications, 25% directly contradicted the original while 49% were inconclusive due to underpowered designs. [...] "
                "Study replication rates were 23% for the Journal of Personality and Social Psychology, 48% for Journal of Experimental Psychology: Learning, Memory, and Cognition",
                nome="Replication crisis"),
        ],
    },
    # 12 Daryl Bem e os experimentos que "viam o futuro"
    {
        "temas_secundarios": ["probabilidade", "paradoxos_logica"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 2011, uma revista de ponta publicou experimentos de Daryl Bem que pareciam mostrar que dá para sentir o futuro. Quem refez um deles e nada achou teve o artigo recusado por três revistas por ser só uma replicação.",
        "explicacao": (
            "O artigo \"Feeling the Future\" saiu no Journal of Personality and Social Psychology, uma das revistas "
            "mais respeitadas da área, e trazia evidência estatística de precognição. Vindo de um pesquisador "
            "respeitado e de uma revista de primeira linha, provocou muita polêmica. Stuart Ritchie, Chris French "
            "e Richard Wiseman repetiram um dos nove experimentos e não acharam sinal de precognição. A própria "
            "revista de Bem, a Science Brevia e a Psychological Science recusaram o artigo por ser uma replicação. "
            "Uma quarta revista o recusou depois das ressalvas de um parecerista que, soube-se depois, era o próprio "
            "Bem. A réplica acabou saindo na PLoS ONE. Em 2012, duas análises independentes notaram que nove "
            "resultados positivos em dez testes eram um número anormalmente alto para experimentos daquele tamanho. "
            "No mesmo ano, a revista que publicou Bem divulgou sete experimentos que não acharam nenhuma evidência "
            "de precognição. Em 2017, Bem disse à revista Slate que era a favor do rigor, mas preferia que outros o "
            "praticassem. Em 2023, uma grande replicação pré-registrada, planejada com a participação dele e de "
            "outros defensores da percepção extrassensorial, não encontrou precognição. O episódio virou peça "
            "central da crise de replicação: muitos dos procedimentos estatísticos falhos de Bem eram prática comum "
            "na psicologia."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Daryl_Bem",
                "In 2011, Bem published the article \"Feeling the Future: Experimental Evidence for Anomalous Retroactive Influences on Cognition and Affect\" in the Journal of Personality and Social Psychology that offered statistical evidence for psi. [...] "
                "Its presentation by a respected researcher, and its publication by an upper-tier journal, engendered much controversy. [...] "
                "One of the nine experiments in Bem's study (\"Retroactive Facilitation of Recall\") was repeated by scientists Stuart J. Ritchie, Chris French, and Richard Wiseman. "
                "Their attempt to replicate was published in PLoS ONE and found no evidence of precognition. [...] "
                "The Journal of Personality and Social Psychology, Science Brevia and Psychological Science each rejected the paper on the grounds that it was a replication. "
                "A fourth journal, the British Journal of Psychology, refused the paper after reservations from one referee, later confirmed to be Bem himself [...] "
                "In 2012, two independent articles found that the number of rejections of the null hypothesis reported by Bem (nine out of ten tested) is abnormally high, given the properties of the experiments and reported effect sizes [...] "
                "In 2012, the same journal that published Bem's original experiments, The Journal of Personality and Social Psychology (Vol. 103, No. 6), published \"Correcting the Past: Failures to Replicate Psi\" [...] "
                "The paper reported seven experiments testing for precognition that \"found no evidence supporting its existence.\" "
                "In a 2017 follow-up article in Slate magazine on the \"Feeling the Future\" experiments, Bem is quoted as saying, \"I'm all for rigor, but I prefer other people do it. [...] "
                "A large-scale pre-registered replication in 2023, which included Bem and other ESP proponents in its design, found no evidence for precognition.",
                nome="Daryl Bem"),
            wiki("Replication_crisis",
                "According to Romero, what the community found particularly upsetting was that many of the flawed procedures and statistical tools used in Bem's studies were part of common research practice in psychology.",
                nome="Replication crisis"),
        ],
    },
    # 13 a caminhada lenta dos "velhinhos" e a expectativa do experimentador
    {
        "temas_secundarios": ["vieses_cognitivos", "percepcao_ilusoes"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Num estudo famoso de 1996, quem montou frases com palavras ligadas à velhice saiu do laboratório andando mais devagar. Refeito com sensores em Bruxelas, o efeito só apareceu quando quem aplicava o teste esperava por ele.",
        "explicacao": (
            "O estudo de John Bargh e colegas usava palavras ligadas ao estereótipo do idoso, como \"Flórida\", "
            "\"esquecido\" e \"ruga\", sem nenhuma menção a lentidão. Virou um dos pilares da ideia de que o "
            "comportamento é guiado por estímulos que nem percebemos, e foi muito citado e ensinado. No início dos anos 2010, uma "
            "equipe da Universidade Livre de Bruxelas o refez com sensores infravermelhos escondidos no corredor, "
            "em vez do cronômetro manual do original, e uma amostra maior. O efeito não apareceu. Num segundo "
            "experimento, metade dos aplicadores foi levada a esperar que os participantes andassem mais devagar, "
            "e a outra metade, o contrário. Eles também cronometravam a caminhada à mão. O efeito surgiu, mas só "
            "com os aplicadores que esperavam a lentidão. Para os autores, as expectativas de quem conduz o teste "
            "ajudam a explicar o resultado, e a conversa final sugeria que os participantes tinham notado as "
            "palavras. Não foi só profecia autorrealizável: com um aplicador que esperava pressa, os participantes "
            "não andaram mais rápido. O caso entrou na crise de replicação. Daniel Kahneman, prêmio Nobel, "
            "escreveu uma carta aberta dizendo que o priming tinha virado símbolo das dúvidas sobre a psicologia "
            "e, em 2022, chamou a pesquisa de priming comportamental de \"efetivamente morta\"."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Priming_(psychology)",
                "An example of this was done by John Bargh et al. in 1996. "
                "Subjects were implicitly primed with words related to the stereotype of elderly people (example: Florida, forgetful, wrinkle). "
                "While the words did not explicitly mention speed or slowness, those who were primed with these words walked more slowly upon exiting the testing booth than those who were primed with neutral stimuli. [...] "
                "Nobel laureate and psychologist Daniel Kahneman has called on priming researchers to check the robustness of their findings in an open letter to the community, claiming that priming has become a \"poster child for doubts about the integrity of psychological research.\" "
                "In 2022, Kahneman described behavioral priming research as \"effectively dead.\"",
                nome="Priming (psychology)"),
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3261136/fullTextXML",
             "titulo": "Behavioral priming: it's all in the mind, but whose mind? (Doyen et al., PLoS ONE, 2012)",
             "idioma": "en",
             "trecho": (
                "Bargh, Chen, and Burrows' (1996) famous study, in which participants unwittingly exposed to the stereotype of age walked slower when exiting the laboratory, was instrumental in defining this perspective. "
                "Here, we present two experiments aimed at replicating the original study. "
                "Despite the use of automated timing methods and a larger sample, our first experiment failed to show priming. "
                "Our second experiment was aimed at manipulating the beliefs of the experimenters: Half were led to think that participants would walk slower when primed congruently, and the other half was led to expect the opposite. "
                "Strikingly, we obtained a walking speed effect, but only when experimenters believed participants would indeed walk slower. "
                "This suggests that both priming and experimenters' expectations are instrumental in explaining the walking speed effect. "
                "Further, debriefing was suggestive of awareness of the primes. [...] "
                "Second, walking speed was measured using a manual stopwatch — a method that is prone to error and bias. [...] "
                "took place in an empty hallway located on a vacant floor of a Université Libre de Bruxelles building. [...] "
                "Two infrared sensors were hidden in the hallway [...] "
                "we also asked the experimenters to measure participants' walking time using a manual stopwatch [...] "
                "as the primed participants did not walk faster when tested by an experimenter who believed they would walk faster.")},
            wiki("Replication_crisis",
                "In the early 2010s, two direct replication attempts failed to reproduce results from social psychologist John Bargh's much-cited \"elderly-walking\" study (originally published in 1996). "
                "This experiment was part of a series of three studies that had been widely cited throughout the years, was regularly taught in university courses",
                nome="Replication crisis"),
        ],
    },
    # 14 o desamparo aprendido estava ao contrário
    {
        "temas_secundarios": ["neurociencia", "comportamento_animal"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Em experimentos de 1967, cães que levavam choques inescapáveis desistiam de fugir até quando podiam: teriam aprendido que nada adiantava. Em 2016, os dois criadores da teoria escreveram que ela estava ao contrário.",
        "explicacao": (
            "Martin Seligman começou a pesquisa em 1967, na Universidade da Pensilvânia. Num dos primeiros "
            "experimentos, cães presos a arreios levavam choques. Uns podiam desligá-los apertando uma alavanca; "
            "outros, ligados a esses, recebiam choques iguais, mas sua alavanca não fazia nada. Depois, numa caixa "
            "em que bastava pular uma barreira baixa para escapar, os primeiros aprendiam logo, e a maioria dos "
            "outros se deitava e ganía. Para \"curá-los\", os pesquisadores precisaram mover as patas dos cães pelo "
            "caminho da fuga pelo menos duas vezes; ameaças, recompensas e demonstrações não funcionaram. A "
            "explicação, de Seligman e Maier, era que os animais aprendiam que suas ações não importavam. "
            "Em 2016, num artigo de revisão, Maier e Seligman afirmaram que o mecanismo, hoje bem mapeado na "
            "biologia, mostra o oposto: a passividade diante de um sofrimento prolongado não é aprendida. É a "
            "reação padrão, comandada pela atividade da serotonina no núcleo dorsal da rafe, que "
            "inibe a fuga. O que se aprende é o controle: quando o animal detecta que pode agir, o córtex "
            "pré-frontal medial freia aquele núcleo. Os autores especulam que isso pode ter implicações importantes "
            "para o tratamento da depressão."
        ),
        "nivel": 2, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [
            wiki("Learned_helplessness",
                "American psychologist Martin Seligman initiated research on learned helplessness in 1967 at the University of Pennsylvania as an extension of his interest in depression. [...] "
                "In Part 1 of this study, three groups of dogs were placed in harnesses. [...] "
                "Dogs in Group 2 were given electric shocks at random times, which the dog could end by pressing a lever. "
                "Each dog in Group 3 was paired with a Group 2 dog; whenever a Group 2 dog got a shock, its paired dog in Group 3 got a shock of the same intensity and duration, but its lever did not stop the shock. [...] "
                "All of the dogs could escape shocks on one side of the box by jumping over a low partition to the other side. "
                "The dogs in Groups 1 and 2 quickly learned this task and escaped the shock. "
                "Most of the Group 3 dogs‍—‍which had previously learned that nothing they did had any effect on shocks‍—‍simply lay down passively and whined when they were shocked. [...] "
                "To change this expectation, experimenters physically picked up the dogs and moved their legs, replicating the actions the dogs would need to take in order to escape from the electrified grid. "
                "This had to be done at least twice before the dogs would start willfully jumping over the barrier on their own. "
                "In contrast, threats, rewards, and observed demonstrations had no effect on the \"helpless\" Group 3 dogs.",
                nome="Learned helplessness"),
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:PMC4920136&resultType=core&format=json",
             "titulo": "Learned helplessness at fifty: Insights from neuroscience (Maier e Seligman, Psychological Review, 2016)",
             "idioma": "en",
             "trecho": (
                "Learned helplessness at fifty: Insights from neuroscience. [...] "
                "Maier SF, Seligman ME. [...] "
                "Seligman and Maier (1967) theorized that animals learned that outcomes were independent of their responses-that nothing they did mattered-and that this learning undermined trying to escape. "
                "The mechanism of learned helplessness is now very well-charted biologically, and the original theory got it backward. "
                "Passivity in response to shock is not learned. "
                "It is the default, unlearned response to prolonged aversive events and it is mediated by the serotonergic activity of the dorsal raphe nucleus, which in turn inhibits escape. "
                "This passivity can be overcome by learning control, with the activity of the medial prefrontal cortex, which subserves the detection of control leading to the automatic inhibition of the dorsal raphe nucleus. [...] "
                "We speculate that default passivity and the compensating detection and expectation of control may have substantial implications for how to treat depression. [...] "
                "\"pubYear\":\"2016\"")},
        ],
    },
]
