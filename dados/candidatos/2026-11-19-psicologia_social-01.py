LOTE = "2026-11-19-psicologia_social-01"
AREA = "mente"
TEMA = "psicologia_social"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 Asch: a maioria das respostas desafiou o grupo
    {
        "temas_secundarios": ["experimentos_psicologia", "percepcao_ilusoes"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "O experimento de Asch virou símbolo de conformismo: gente que repetia o erro do grupo ao comparar linhas. Mas dois terços das respostas desafiaram a maioria, e 95% dos voluntários resistiram ao menos uma vez.",
        "explicacao": (
            "Em 1951, Solomon Asch reuniu grupos de oito universitários para dizer em voz alta qual de três linhas "
            "tinha o mesmo comprimento de uma linha de referência. Só um deles era voluntário de verdade, e "
            "respondia por último. Os outros eram atores que, em 12 rodadas, davam juntos a mesma resposta errada. "
            "Sem essa pressão, as pessoas erravam menos de 0,7% das vezes. Com ela, cerca de um terço das respostas "
            "acompanhou o erro do grupo, e 74% dos voluntários cederam pelo menos uma vez. O próprio Asch, porém, "
            "destacou que a independência predominou: 64,3% das respostas ficaram corretas. Mesmo assim, um "
            "levantamento de 2015 com 20 grandes livros didáticos achou só um que dizia que a maioria das respostas "
            "desafiou o grupo, e nenhum mencionava que 95% dos voluntários resistiram ao menos uma vez. Outros "
            "detalhes também costumam ficar de fora. Bastava um único ator dando a resposta certa para que só 5% "
            "continuassem seguindo a maioria. E todos os que cederam subestimaram quantas vezes tinham cedido."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Asch_conformity_experiments",
            "In 1951, Asch conducted his first conformity laboratory experiments at Swarthmore College [...] "
            "Groups of eight male college students participated in a simple \"perceptual\" task. "
            "In reality, all but one of the participants were actors [...] "
            "Each participant was then asked to say aloud which line matched the length of that on the first card. [...] "
            "The group was seated such that the real participant always responded last. [...] "
            "In the control group, with no pressure to conform to actors, the error rate on the critical stimuli was less than 0.7%. "
            "In the actor condition also, the majority of participants' responses remained correct (64.3%) [...] "
            "An examination of all critical trials in the experimental group revealed that one-third of all responses were incorrect. [...] "
            "Overall, 74% of participants gave at least one incorrect answer out of the 12 critical trials. [...] "
            "All conforming respondents underestimated the frequency with which they conformed to the majority. [...] "
            "In studies that had one actor give correct responses to the questions, only 5% of the participants continued to answer with the majority. [...] "
            "Asch's 1956 report emphasized the predominance of independence over yielding [...] "
            "A 2015 survey found no change, with just 1 of 20 major texts reporting that most participant-responses defied majority opinion. "
            "No text mentioned that 95% of subjects defied the majority at least once.",
            nome="Asch conformity experiments")],
    },
    # 2 Milgram: a obediência despencava conforme a situação
    {
        "temas_secundarios": ["experimentos_psicologia", "segunda_guerra"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "No experimento de Milgram, 65% obedeceram até o choque máximo. Mas, quando dois falsos colegas se recusavam a continuar, só quatro de 40 iam até o fim. Com um amigo no papel da vítima, só três dos vinte pares.",
        "explicacao": (
            "Os testes começaram em agosto de 1961, na Universidade Yale. O voluntário fazia o papel de "
            "\"professor\" e aplicava choques cada vez mais fortes num \"aluno\" a cada erro. Os choques eram falsos "
            "e o aluno era um ator, mas o voluntário não sabia. Antes, 40 psiquiatras tinham previsto que pouco mais "
            "de um décimo de um por cento iria até o fim. Na primeira versão, 65% chegaram aos 450 volts. O número ficou "
            "famoso, mas Milgram descreveu 19 variações, e elas mostram o quanto a obediência dependia da situação. "
            "Com as ordens dadas por telefone, ela caiu para 21%. Quando o voluntário tinha de segurar o braço do "
            "aluno sobre a placa de choque, 30% foram até o fim. Ao lado de dois colegas que se recusavam, só quatro de "
            "40 continuaram; ao lado de um que obedecia, 37 de 40. Numa versão em que o voluntário levava um amigo "
            "para ser o aluno, só três dos vinte pares foram até o fim. Há críticas sérias: a psicóloga Gina Perry examinou "
            "os arquivos e concluiu que só metade dos participantes acreditou totalmente que era real, e que, "
            "desses, 66% desobedeceram. Ainda assim, uma meta-análise de repetições achou de 28% a 91% de obediência "
            "total, sem tendência de queda ao longo do tempo."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Milgram_experiment",
            "with every participant going up to 300 volts, and 65% going up to the full 450 volts. [...] "
            "The experiments began in August 1961 at Yale University [...] "
            "Unbeknownst to the subject, both slips said \"teacher\". [...] "
            "In reality, there were no shocks, and the learner simulated suffering increasing levels of pain from the shocks. [...] "
            "Milgram also polled forty psychiatrists from a medical school [...] "
            "they believed that \"only a little over one-tenth of one percent of the subjects would administer the highest shock on the board.\" [...] "
            "Thomas Blass of the University of Maryland, Baltimore County performed a meta-analysis on the results of repeated performances of the experiment. "
            "He found that while the percentage of participants who are prepared to inflict fatal voltages ranged from 28% to 91%, there was no significant trend over time [...] "
            "She wrote that \"only half of the people who undertook the experiment fully believed it was real and of those, 66% disobeyed the experimenter\". [...] "
            "In Obedience to Authority: An Experimental View (1974), Milgram describes 19 variations of his experiment [...] "
            "In the variation where the learner's physical immediacy was closest—where the participant had to hold the learner's arm onto a shock plate—30 percent of participants completed the experiment. [...] "
            "For example, in Experiment 2, where participants received telephonic instructions from the experimenter, compliance decreased to 21 percent. [...] "
            "In Experiment 17, when two additional teachers refused to comply, only four of 40 participants continued in the experiment. [...] "
            "In that variation, 37 of 40 continued with the experiment. [...] "
            "In the RC, participants were required to bring a friend, with one becoming the teacher and the other the learner. "
            "Just three of the twenty pairs of friends in the study delivered each shock.",
            nome="Milgram experiment")],
    },
    # 3 as 38 testemunhas e as câmeras de rua
    {
        "temas_secundarios": ["experimentos_psicologia", "cidades"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "A história das 38 testemunhas que assistiram ao assassinato de Kitty Genovese sem fazer nada, que inspirou o estudo do efeito espectador, era exagerada. E câmeras de rua mostram alguém ajudando em mais de 90% das brigas.",
        "explicacao": (
            "Kitty Genovese, de 28 anos, foi esfaqueada e morta em Nova York em março de 1964. Duas semanas depois, "
            "o New York Times afirmou que 38 testemunhas viram ou ouviram os ataques e que ninguém chamou a polícia "
            "até ela morrer. O caso levou os psicólogos John Darley e Bibb Latané a estudar o efeito espectador: em "
            "experimentos de laboratório, a presença de outras pessoas inibia a ajuda, muitas vezes por larga "
            "margem. Mas a história original não se sustentou. Um artigo de 2007 não achou provas da presença de 38 "
            "testemunhas, nem de que elas tivessem visto o crime e ficado paradas. Em 2016, o próprio jornal chamou "
            "a reportagem de falha: ninguém viu o ataque inteiro, muitos acharam que ouviam uma briga de casal ou "
            "de bêbados, duas pessoas chamaram a polícia, e uma mulher de 70 anos saiu para amparar Kitty até a "
            "chegada do socorro. Em 2019, um estudo examinou mais de 200 gravações de câmeras de segurança de "
            "conflitos de rua no Reino Unido, na Holanda e na África do Sul. Em mais de 90% deles, uma ou mais "
            "pessoas intervieram, e mais espectadores aumentavam a chance de alguém agir. Uma meta-análise de 2011 "
            "já tinha visto que o efeito aparece nas emergências sem perigo, mas não nas perigosas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Bystander_effect",
                "The bystander effect was first demonstrated and popularized in the laboratory by social psychologists John M. Darley and Bibb Latané in 1968 after they became interested in the topic following the murder of Kitty Genovese in 1964. [...] "
                "These experiments have found that the presence of others inhibits helping, often by a large margin. [...] "
                "A 2011 meta-analysis found that the bystander effect was most likely to occur in non-dangerous emergencies but did not occur in dangerous emergencies. [...] "
                "Philpot et al. (2019) examined over 200 sets of real-life surveillance video recordings from the United Kingdom, the Netherlands, and South Africa [...] "
                "They found that intervention was the norm, and in over 90% of conflicts one or more bystanders intervened to provide help. "
                "Increased bystander presence increased the likelihood that someone would intervene.",
                nome="Bystander effect"),
            wiki("Murder_of_Kitty_Genovese",
                "Kitty Genovese, a 28-year-old bartender, was raped and stabbed to death on March 13, 1964 [...] "
                "Two weeks after the murder, The New York Times published an article claiming that thirty-eight witnesses saw or heard the multiple attacks, and that none of them called the police until after she was dead. [...] "
                "In 2007, an article in American Psychologist found \"no evidence for the presence of 38 witnesses, or that witnesses observed the murder, or that witnesses remained inactive\". "
                "In 2016, the Times called its own reporting \"flawed\" [...] "
                "None saw the attack in its entirety. Only a few had glimpsed parts of it, or recognized the cries for help. "
                "Many thought they had heard lovers or drunks quarreling. There were two attacks, not three. "
                "And afterward, two people did call the police. "
                "A 70-year-old woman ventured out and cradled the dying victim in her arms until they arrived.",
                nome="Murder of Kitty Genovese"),
        ],
    },
    # 4 o ensaio fracassado de Robbers Cave
    {
        "temas_secundarios": ["experimentos_psicologia"],
        "tipos_espanto": ["historia_humana", "mito_desmentido"],
        "gancho": "Antes do famoso acampamento de Robbers Cave, em que meninos viraram inimigos, houve um ensaio em 1953 dado como fracasso. Para atiçar a rivalidade, membros da equipe chegaram a derrubar uma barraca dos garotos.",
        "explicacao": (
            "No estudo clássico de 1954, a equipe do psicólogo Muzafer Sherif levou 22 meninos de onze e doze anos, que "
            "não se conheciam, a um acampamento de verão em Oklahoma. Em dois grupos que disputavam prêmios em "
            "jogos, eles passaram a se hostilizar; depois, tarefas que exigiam cooperação reduziram a tensão. O "
            "estudo virou referência sobre como a competição por recursos gera conflito. Mas Robbers Cave foi a "
            "terceira e última tentativa de uma série iniciada em 1949. Na de 1953, que Sherif depois considerou um "
            "fracasso, um menino perguntou para que serviam os microfones pendurados no refeitório, e outro achou "
            "um caderno da equipe com anotações sobre as reações dos grupos, confirmando o boato de que aquilo era "
            "um experimento para fazê-los brigar. Um membro da equipe relembrou à psicóloga Gina Perry, que "
            "investigou os arquivos, o desânimo ao ver colegas derrubarem uma barraca na esperança de que um grupo "
            "culpasse o outro. Inflar o placar de uma equipe para aumentar a rivalidade foi comum em 1953 e em "
            "1954. E, nos estudos anteriores, os meninos chegaram a se unir contra um inimigo comum e, às vezes, "
            "contra os próprios pesquisadores, sinal de que percebiam a manipulação."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Robbers_Cave_experiment",
                "The 1954 Robbers Cave experiment (or Robbers Cave study) by Muzafer Sherif and Carolyn Wood Sherif represents one of the most widely known demonstrations of RCT. "
                "The Sherifs' study was conducted over three weeks in a 200-acre summer camp in Robbers Cave State Park, Oklahoma, focusing on intergroup behavior. "
                "In this study, researchers posed as camp personnel, observing 22 eleven- and twelve-year-old boys who had never previously met [...] "
                "wherein the groups were entered into competition with one another in various camp games. [...] "
                "Valued prizes were awarded to the winners. "
                "This caused both groups to develop negative attitudes and behaviors towards the outgroup. [...] "
                "During this stage, tensions between the groups were reduced through teamwork-driven tasks that required intergroup cooperation. [...] "
                "In two earlier studies, the boys ganged up on a common enemy and, in fact, on occasion ganged up on the experimenters themselves, showing an awareness of being manipulated.",
                nome="Realistic conflict theory (Robbers Cave experiment)"),
            {"url": "https://bps.org.uk/psychologist/view-boys",
             "titulo": "The view from the boys (Gina Perry, The Psychologist, British Psychological Society)",
             "idioma": "en",
             "trecho": "In all three of the intergroup conflict studies that Sherif conducted between 1949 and 1954, the boys showed their curiosity about the men running the camp and looked to the adults for guidance. [...] "
                "In the second study in 1953, which Sherif later wrote off as a failure, one boy asked the staff what the microphones hanging from the rafters in the mess hall were for. [...] "
                "A rumour amongst the boys that the camp was an experiment in which they were expected to fight one another was confirmed when one boy found a staff notebook including detailed observations of the groups' reactions. [...] "
                "For example, artificially inflating the scores of one team over another to increase rivalry was common in both the 1953 and 1954 studies. [...] "
                "One staff member recalled his dismay when other staff pulled one of the tents down in the hope that one group of boys would blame the other and the experiment would move to the next phase. [...] "
                "Robbers Cave was Sherif's third and final try in the intergroup conflict series"},
        ],
    },
    # 5 a Prisão de Stanford sob escrutínio
    {
        "temas_secundarios": ["experimentos_psicologia", "leis_julgamentos"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "O Experimento da Prisão de Stanford, de 1971, virou prova de que qualquer um vira carrasco. Mas gravações mostram a equipe pedindo a um guarda que fosse mais duro, e o primeiro preso a surtar disse em 2017 que fingiu.",
        "explicacao": (
            "Em agosto de 1971, Philip Zimbardo recrutou por anúncio de jornal universitários para uma \"prisão\" "
            "montada no porão do prédio de psicologia de Stanford. Os vinte e quatro escolhidos foram sorteados entre guardas e "
            "presos. O abuso psicológico dos guardas piorou dia a dia, e o estudo foi encerrado no sexto dia. Por "
            "décadas, foi contado como demonstração de que o papel e a situação transformam pessoas comuns. As "
            "críticas, porém, se acumularam. Em 2017, gravações do site oficial do estudo mostraram o assistente que "
            "fazia o papel de diretor da prisão incentivando um guarda a participar mais e ser mais \"durão\", pelo "
            "bem do experimento. Em 2018, o pesquisador francês Thibault Le Texier afirmou que os guardas foram "
            "orientados a agir de certos modos para confirmar conclusões escritas em boa parte antes do "
            "experimento. A maioria dos guardas disse depois que estava atuando de propósito. Douglas Korpi, o "
            "primeiro preso a sair, após um aparente colapso nervoso com 36 horas, disse em 2017 que fingiu para "
            "poder voltar a estudar para um exame. Zimbardo rejeitou as críticas, chamou as de Le Texier de ataque "
            "pessoal e afirmou que Korpi mentiu nessa entrevista."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Stanford_prison_experiment",
            "Twenty-four participants were chosen after assessments of psychological stability and then assigned randomly to the role of prisoners or prison guards. [...] "
            "During the next five days, psychological abuse of the prisoners by the \"guards\" worsened. [...] "
            "He ended the experiment on the sixth day [...] "
            "Zimbardo claimed that Le Texier's article was mostly an ad hominem attack on him [...] "
            "study participants were recruited using an advertisement in the \"help wanted\" section of the Palo Alto Times and The Stanford Daily newspapers in August 1971 [...] "
            "The experiment was performed in a 35 ft (11 m) section of the basement of Jordan Hall, Stanford's psychology building. [...] "
            "Zimbardo assumed the role of Superintendent, and an undergraduate research assistant, David Jaffe, assumed the role of Warden. "
            "Digitized recordings available on the official SPE website were widely discussed in 2017, particularly one in which warden David Jaffe tried to influence the behavior of one of the guards by encouraging him to participate more and be more \"tough\" for the benefit of the experiment. [...] "
            "In 2018, Thibault Le Texier, a French researcher, questioned the scientific validity and merit of the experiment [...] "
            "he has established that the guards were asked directly to behave in certain ways in order to confirm Zimbardo's conclusions, which were largely written in advance of the experiment. [...] "
            "Most of the guards have stated since the SPE that they were intentionally acting. [...] "
            "The first prisoner to leave the experiment was Douglas Korpi, prisoner 8612. After 36 hours, he had an apparent mental breakdown [...] "
            "However, in a 2017 interview, Korpi stated that his breakdown had been fake, and that he did it only so that he could leave and return to studying for his Graduate Record Exam [...] "
            "Further, Zimbardo believes Korpi's 2017 interview was a lie.",
            nome="Stanford prison experiment")],
    },
    # 6 as baratas com plateia
    {
        "temas_secundarios": ["comportamento_animal", "insetos", "experimentos_psicologia"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Num clássico de 1969, baratas com uma plateia de outras baratas corriam mais rápido numa pista reta e mais devagar num labirinto. Em 2020, uma repetição com 120 baratas só confirmou a parte da lentidão.",
        "explicacao": (
            "O estudo de Robert Zajonc e colegas testava uma ideia antiga da psicologia social. Em 1898, Norman "
            "Triplett notou que crianças enrolavam linha mais depressa quando competiam entre si. Zajonc propôs "
            "que a simples presença de outros funciona como uma fonte de excitação, que melhora o desempenho em "
            "tarefas simples e o piora nas complexas. Para ver isso em animais de cognição limitada, usou baratas, "
            "que fogem da luz: um holofote as fazia correr por uma pista reta ou por um labirinto, sozinhas ou com "
            "outras baratas olhando de caixas ao lado. O resultado virou presença constante em livros didáticos. "
            "Em 2020, pesquisadores alemães notaram que a interação famosa nunca tinha sido testada "
            "estatisticamente, e que o estudo provavelmente tinha poucos animais: só 40 nas condições decisivas. "
            "Eles reconstruíram o aparelho, seguiram o procedimento original o mais fielmente possível e usaram "
            "120 baratas de uma espécie um pouco maior. Com plateia, as baratas ficaram mais lentas nas duas "
            "tarefas: a inibição se repetiu, mas não houve sinal de facilitação. Em humanos, uma meta-análise de "
            "241 estudos achou efeitos pequenos nos dois sentidos."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": "https://publikationen.ub.uni-frankfurt.de/files/55447/0956797620902101.pdf",
             "titulo": "Replicating Roaches: A Preregistered Direct Replication of Zajonc, Heingartner, and Herman's (1969) Social-Facilitation Study (Psychological Science)",
             "idioma": "en",
             "trecho": "Psychological Science 2020, Vol. 31(3) [...] "
                "Justus Liebig University Giessen [...] "
                "Fifty years ago, Zajonc, Heingartner, and Herman (1969) conducted a famous experiment on social enhancement and inhibition of performance in cockroaches. "
                "A moderating effect of task difficulty on the effect of the presence of an audience, as revealed by impaired performance in complex tasks and enhanced performance in simple tasks, was presented as the major conclusion of this research. "
                "However, the researchers did not test this interaction statistically. [...] "
                "Results revealed main effects for task difficulty, with faster running times in the runway than the maze, and for audience, with slower running times when the audience was present than when it was absent. "
                "There was no interaction between the presence of an audience and task difficulty. "
                "Although we replicated the social-inhibition effect, there was no evidence for a social-facilitation effect. [...] "
                "analysis of 241 studies (Bond & Titus, 1983) found a small facilitation effect in simple tasks [...] "
                "has been highly cited in textbooks [...] "
                "Moreover, the study is very likely to have been underpowered (with N = 40 for the critical [...] "
                "We precisely rebuilt the apparatus and followed the original procedure as closely as possible. [...] "
                "the cockroaches we used (Blaberus craniifer) are slightly larger than the ones in the original study (Blatta orientalis). [...] "
                "the starting box was illuminated with a floodlight to make the cockroach start running. [...] "
                "We decided to triple the sample size of the original study (resulting in a total sample of 120)"},
            wiki("Social_facilitation",
                "Zajonc's generalized drive hypothesis was the first theory that addressed why the presence of others increased performance sometimes yet decreased it at other times. "
                "He argued that the presence of others serves as a source of arousal, and heightened arousal increases the likelihood of an organism to do better on well-learned or habitual responses. "
                "For this reason, arousal improves performance on simple, or well-learned tasks, but impairs performance on complex, or not well-learned tasks. [...] "
                "In 1898, Norman Triplett pioneered research on social facilitation by studying the competitive nature of children. "
                "In this study, each child was given a string and was told to wind it. "
                "He found that children performed much better while they were competing with one another [...] "
                "In 1969, Zajonc, Heingartner, and Herman found evidence for social facilitation in animals with limited or no cognitive processing.",
                nome="Social facilitation"),
        ],
    },
    # 7 o número de Dunbar e a margem de erro
    {
        "temas_secundarios": ["comportamento_animal", "evolucao"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "O \"número de Dunbar\", de 150 relações estáveis por pessoa, saiu de uma conta com cérebros de primatas. Refeita com dados atualizados, a conta deu margens de erro como de 4 a 520 pessoas: largas demais para valer.",
        "explicacao": (
            "Nos anos 1990, o antropólogo britânico Robin Dunbar notou que, entre primatas, o volume do neocórtex "
            "parece limitar quantos membros do grupo cada animal consegue acompanhar. Em 1992, com dados de 38 "
            "gêneros de primatas, projetou para humanos um grupo médio de 148 pessoas, arredondado para 150. Ele "
            "mesmo tratou o resultado como exploratório, porque a margem de erro já era grande: de 100 a 230. Numa "
            "definição informal, seriam as pessoas com quem você não se sentiria constrangido de se juntar, sem "
            "convite, para um drinque, se as encontrasse num bar. O número ficou famoso e chegou a orientar "
            "empresas: uma agência de viagens australiana se reorganizou em \"tribos\" de no máximo 150 pessoas. "
            "Mas uma reanálise com dados atualizados e outros métodos filogenéticos chegou a médias de 69 a 109 ou "
            "de 16 a 42 pessoas, com intervalos de confiança de 4 a 520 e de 2 a 336. Os autores concluíram que "
            "não dá para derivar desse jeito um limite cognitivo para os grupos humanos. Dunbar respondeu que a "
            "conta deveria usar só dados de grandes símios. Já estudos de campo nos Estados Unidos estimaram uma "
            "média de 290 laços por pessoa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Dunbar%27s_number",
            "This number was first proposed in the 1990s by Robin Dunbar, a British anthropologist who found a correlation between primate brain size and average social group size. [...] "
            "Dunbar explained the principle informally as \"the number of people you would not feel embarrassed about joining uninvited for a drink if you happened to bump into them in a bar.\" [...] "
            "The number of social group members a primate can track appears to be limited by the volume of the neocortex. [...] "
            "In 1992, Dunbar used the correlation observed for non-human primates to predict a social group size for humans. "
            "Using a regression equation on data for 38 primate genera, Dunbar predicted a human \"mean group size\" of 148 (casually rounded to 150), a result he considered exploratory because of the large error measure (a 95% confidence interval of 100 to 230). [...] "
            "Flight Centre, an Australian travel agency, applied Dunbar's number when reorganising the firm into \"families\" (stores), \"villages\" (clusters of stores) and \"tribes\" (aggregates of villages up to a maximum of 150 people). [...] "
            "came up with an estimated mean number of ties, 290, which is roughly double Dunbar's estimate. [...] "
            "A replication of Dunbar's analysis on updated complementary datasets using different comparative phylogenetic methods yielded wildly different numbers. "
            "Bayesian and generalized least-squares phylogenetic methods generated approximations of average group sizes between 69–109 and 16–42, respectively. "
            "However, enormous 95% confidence intervals (4–520 and 2–336, respectively) implied that specifying any one number is of limited value. "
            "The researchers drew the conclusion that a cognitive limit on human group size cannot be derived in this manner. [...] "
            "now stating that his number should not be calculated from data on primates or anthropoids, as in his original study, but on apes.",
            nome="Dunbar's number")],
    },
    # 8 a epidemia de dança de 1518
    {
        "temas_secundarios": ["historia_medicina", "teatro_danca"],
        "tipos_espanto": ["historia_humana", "misterio_aberto"],
        "gancho": "Em 1518, em Estrasburgo, dezenas de pessoas dançaram sem parar por semanas. Os médicos acharam que a cura era dançar mais, e a cidade montou palcos e pagou músicos. A mania só aumentou.",
        "explicacao": (
            "Segundo crônicas da época, tudo começou em julho com uma mulher, Frau Troffea, que passou dias "
            "dançando na rua diante de casa. Em poucos dias, mais de trinta pessoas a imitavam, e as estimativas finais "
            "vão de 50 a 400 dançarinos. Entre as explicações do tempo estava o \"sangue superaquecido\", e os "
            "médicos recomendaram que os doentes dançassem até se livrar do mal. O conselho mandou transformar "
            "salões de corporações em pistas, ergueu tablados nos mercados e pagou dezenas de músicos, além de "
            "dançarinos sadios para animar. Deu errado: muitos espectadores viram ali a fúria de São Vito, que se "
            "acreditava punir pecadores com a dança, e entraram na mania. O conselho então desmontou os palcos, "
            "proibiu quase toda música e dança e mandou os mais afetados ao santuário de São Vito, em Saverne. O "
            "surto acabou em setembro. Se houve mortes, e quantas, é disputado: as fontes da própria cidade na "
            "época não as mencionam. A explicação mais popular, do historiador John Waller, é uma histeria coletiva "
            "provocada pelo estresse de anos de fome e doenças. A hipótese do esporão-do-centeio perdeu força, "
            "porque o envenenamento restringe a circulação nas extremidades e impediria dançar dias seguidos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Dancing_plague_of_1518",
                "was a case of dancing mania that occurred in Strasbourg, Alsace (modern-day France), in the Holy Roman Empire from July 1518 to September 1518. "
                "Somewhere between 50 and 400 people took to dancing for weeks. "
                "There are many theoretical theories behind the phenomenon, the most popular being stress-induced mass hysteria, suggested by John Waller. [...] "
                "Disagreement exists over whether people ultimately danced to death. [...] "
                "but the sources of the city of Strasbourg at the time of the events did not mention the number of deaths, or even if there were fatalities. [...] "
                "Contemporaneous explanations included demonic possession, divine judgement and overheated blood. [...] "
                "since the region where the people danced was riddled with starvation and disease",
                nome="Dancing plague of 1518"),
            {"url": "https://publicdomainreview.org/essay/the-dancing-plague-of-1518/",
             "titulo": "The Dancing Plague of 1518 (Ned Pennant-Rea, The Public Domain Review)",
             "idioma": "en",
             "trecho": "According to his Opus Paramirum, and various chronicles agree, it all started with one woman. "
                "Frau Troffea had started dancing on July 14th on the narrow cobbled street outside her half-timbered home. [...] "
                "within days more than thirty choreomaniacs were in motion [...] "
                "They must dance themselves free of it. [...] "
                "Carpenters and tanners were ordered to transform their guild halls into temporary dance floors [...] "
                "dozens of musicians were paid to play drums, fiddles, pipes, and horns, with healthy dancers brought in for further encouragement. [...] "
                "It backfired horribly. "
                "Being more inclined to a supernatural than a medical explanation of the dance, most of the onlookers saw in the frenzied movements a demonstration of the magnitude of Saint Vitus’ fury. "
                "None being free of sin, many were lured into the mania. [...] "
                "The privy council ordered the stages to be pulled down. [...] "
                "prohibiting almost all dance and music in the city until September. [...] "
                "the council ordered those worst afflicted to be bundled into wagons and taken the three-day ride to the shrine of Saint Vitus [...] "
                "Yes, ergot can cause convulsions and hallucinations, but it also restricts blood flow to the extremities. "
                "Someone poisoned by it simply could not dance for several days in a row."},
        ],
    },
    # 9 a seita do disco voador e a dissonância cognitiva
    {
        "temas_secundarios": ["religioes", "experimentos_psicologia"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Um livro de 1956 virou base da teoria da dissonância cognitiva: quando o fim do mundo não veio, uma seita teria redobrado a fé. Arquivos abertos depois indicam o contrário, e pesquisadores interferindo no grupo.",
        "explicacao": (
            "Em 1954, Dorothy Martin, dona de casa de Chicago que dizia receber mensagens de seres do planeta "
            "Clarion, anunciou que um dilúvio destruiria boa parte dos Estados Unidos e de outros países antes do "
            "amanhecer de 21 de dezembro, e que discos voadores resgatariam os fiéis. Alguns largaram o emprego e "
            "deram dinheiro e bens. Os psicólogos Leon Festinger, Henry Riecken e Stanley Schachter infiltraram "
            "observadores no grupo, sem permissão dos observados. No livro When Prophecy Fails, contaram que, "
            "depois da noite frustrada, o grupo, que antes evitava a imprensa, passou a buscar publicidade e a "
            "recrutar: um jeito de aliviar o choque entre a crença e a realidade. Críticos já apontavam problemas: "
            "muitas vezes, quase um terço dos membros eram observadores, e os próprios cientistas contribuíram para "
            "os eventos. Em 2025, o pesquisador Thomas Kelly, com documentos recém-liberados, afirmou que as teses "
            "centrais do livro são falsas e que os autores sabiam disso. Segundo ele, o grupo já fazia proselitismo "
            "bem antes da data, abandonou a crença logo depois, e Martin se retratou. Kelly também acusa os autores "
            "de fabricar mensagens psíquicas e diz que Riecken se fez passar por autoridade espiritual e admitiu "
            "ter precipitado os eventos decisivos."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "consenso_parcial",
        "fontes": [
            wiki("When_Prophecy_Fails",
                "When Prophecy Fails: A Social and Psychological Study of a Modern Group That Predicted the Destruction of the World is a classic work of social psychology by Leon Festinger, Henry Riecken, and Stanley Schachter, published in 1956 [...] "
                "focusing on the cognitive dissonance between the members' beliefs and actual events [...] "
                "The prophecy came from Dorothy Martin (1900–1992), a Chicago housewife who practised automatic writing [...] "
                "Martin claimed to be receiving messages from superior beings from a planet she referred to as Clarion. [...] "
                "The messages received by Martin included a prophecy that Lake City and large portions of the United States, Canada, Central America, and Europe would be destroyed by a flood before dawn on December 21, 1954. [...] "
                "Some left or lost their jobs, neglected or ended their studies, ended relationships and friendships with non-believers, gave away money, and/or disposed of possessions to prepare for their departure on a flying saucer [...] "
                "with data collected through participant observation, without the permission of the people being observed. [...] "
                "In a reversal of its previous distaste for publicity, the group begins an urgent campaign to spread its message to as broad an audience as possible. [...] "
                "It has been remarked that often almost one-third of the membership of the group consisted of participant observers. "
                "More significantly, the social scientists themselves contributed to the events described. [...] "
                "A 2025 article by Thomas Kelly argued that the main theses of the book are false and were known to be false by the authors.",
                nome="When Prophecy Fails"),
            {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1002/jhbs.70043&format=json&resultType=core",
             "titulo": "Debunking When Prophecy Fails (Thomas Kelly, Journal of the History of the Behavioral Sciences, resumo via Europe PMC)",
             "idioma": "en",
             "trecho": "In 1954, Dorothy Martin predicted an apocalyptic flood and promised her followers rescue by flying saucers. "
                "When neither arrived, she recanted, her group dissolved, and efforts to proselytize ceased. [...] "
                "Drawing on newly unsealed archival material, this article demonstrates that the book's central claims are false, and that the authors knew they were false. "
                "The documents reveal that the group actively proselytized well before the prophecy failed and quickly abandoned their beliefs afterward. "
                "They also expose serious ethical violations by the researchers, including fabricated psychic messages, covert manipulation, and interference in a child welfare investigation. "
                "One coauthor, Henry Riecken, posed as a spiritual authority and later admitted he had"},
        ],
    },
    # 10 os maridos sauditas e a ignorância pluralística
    {
        "temas_secundarios": ["decisoes_economia", "costumes_rituais"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Em Riad, 87% dos jovens maridos de um estudo apoiavam, no anonimato, que mulheres trabalhassem fora, mas subestimavam o apoio dos vizinhos. Ao saber a verdade, mais deles inscreveram a esposa num serviço de empregos.",
        "explicacao": (
            "É um caso de ignorância pluralística: muita gente acredita, por engano, que a maioria pensa diferente "
            "dela e acaba seguindo uma visão que não tem. Na Arábia Saudita, pelo costume da tutela, o marido "
            "costuma ter a palavra final sobre a esposa trabalhar. Os economistas Leonardo Bursztyn, Alessandra "
            "González e David Yanagizawa-Drott reuniram 500 homens casados, de 18 a 35 anos, em sessões de 30 "
            "participantes da mesma região de Riad. Numa pesquisa anônima, 87% concordaram que as mulheres deveriam "
            "poder trabalhar fora de casa. Quando tiveram de adivinhar, valendo recompensa, como os outros da "
            "sessão tinham respondido, cerca de três quartos subestimaram o apoio. Numa amostra nacional, 82% "
            "apoiavam, e 92% subestimaram o apoio dos outros. Depois, parte dos homens, sorteada, viu o resultado "
            "real. No grupo sem essa informação, 23% escolheram inscrever a esposa num serviço de busca de emprego; "
            "com a informação, a taxa subiu 9 pontos, um aumento de 36%. Quatro meses depois, as esposas dos homens "
            "corrigidos tinham mais chance de já ter se candidatado e feito entrevista para um emprego fora de "
            "casa. Uma crença errada sobre o que os outros pensam bastava para frear uma mudança que a maioria "
            "aprovava."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://www.nber.org/system/files/working_papers/w24736/w24736.pdf",
             "titulo": "Misperceived Social Norms: Female Labor Force Participation in Saudi Arabia (Bursztyn, González e Yanagizawa-Drott, NBER Working Paper 24736)",
             "idioma": "en",
             "trecho": "Leonardo Bursztyn [...] Alessandra L. González [...] David Yanagizawa-Drott [...] "
                "Through the custom of guardianship, husbands typically have the final word on their wives’ labor supply decisions in Saudi Arabia [...] "
                "We then show that randomly correcting these beliefs about others increases married men’s willingness to let their wives join the labor force (as measured by their costly sign-up for a job-matching service for their wives). "
                "Finally, we find that this decision maps onto real outcomes: four months after the main intervention, the wives of men in our original sample whose beliefs about acceptability of FLFP were corrected are more likely to have applied and interviewed for a job outside of home. [...] "
                "a sample of 500 Saudi married men aged 18-35, recruited from [...] "
                "These men each attended a 30-participant session [...] "
                "In an anonymous online survey, 87% of the experimental participants agreed with the statement: “In my opinion, women should be allowed to work outside of the home.” "
                "When incentivized to guess how other session participants responded to the same question, about three-quarters of the experimental subjects underestimate the true [...] "
                "In a control group without belief corrections, 23% of participants chose the job matching service. "
                "In the treatment group with feedback on the opinions of other participants, the share went up [...] "
                "by 9 percentage points (a 36% increase). [...] "
                "82% of men agree with the same statement on FLFP used in the main experiment. "
                "When incentivized to guess the responses of other survey respondents, 92% of them underestimate the true share."},
            wiki("Pluralistic_ignorance",
                "In social psychology, pluralistic ignorance (also known as a collective illusion or collective delusion) is a phenomenon in which people mistakenly believe that others predominantly hold an opinion different from their own. "
                "In such cases, many people in a group may go along with a view they do not hold because they think, incorrectly, that most other people in the group hold it.",
                nome="Pluralistic ignorance"),
        ],
    },
    # 11 Klee, Kandinsky e os grupos mínimos
    {
        "temas_secundarios": ["segunda_guerra", "pintura"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Desconhecidos separados em grupos só por preferirem quadros de Klee ou de Kandinsky passaram a favorecer o próprio grupo ao dividir recompensas, mesmo quando isso diminuía o ganho do próprio grupo.",
        "explicacao": (
            "Os experimentos de \"grupos mínimos\" foram criados no início dos anos 1970 pelo psicólogo Henri "
            "Tajfel, na Universidade de Bristol. A intenção era montar grupos com o menor significado possível e ir "
            "acrescentando elementos até descobrir em que ponto a discriminação aparecia. A surpresa foi que ela "
            "aparecia já nas condições mínimas. Os voluntários eram divididos por um critério banal, como a "
            "preferência por pinturas abstratas, ou até por cara ou coroa. Não sabiam quem eram os colegas de grupo "
            "nem esperavam conviver com eles. Depois, distribuíam dinheiro ou pontos entre outros participantes, "
            "identificados só por um número e pelo grupo, sem poder dar nada a si mesmos. Mostravam bastante senso "
            "de justiça, mas davam mais aos do próprio grupo, e muitas vezes preferiam aumentar a vantagem sobre o "
            "outro grupo a maximizar o ganho absoluto do seu. Tajfel tinha razões pessoais para estudar o "
            "preconceito: judeu polonês, lutou pelo exército francês, foi prisioneiro de guerra dos alemães e, ao "
            "voltar, descobriu que nenhum dos parentes próximos tinha sobrevivido ao Holocausto. Desses resultados "
            "nasceu a teoria da identidade social."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Henri_Tajfel",
                "Henri Tajfel (born Hersz Mordche Tajfel; 22 June 1919 – 3 May 1982) was a Polish social psychologist, best known for his pioneering work on the cognitive aspects of prejudice and social identity theory [...] "
                "At the outbreak of World War II, he volunteered to serve in the French army. "
                "A year later, he was taken prisoner-of-war by the Germans. [...] "
                "On his return home he discovered that none of his immediate family, and few of his friends, had survived the Nazi Holocaust. "
                "He was to write later about the profound effect that this had on him and how it led to his later work on the psychology of prejudice and intergroup relations. [...] "
                "Having moved to Bristol University, Tajfel began his work on intergroup relations and conducted the renowned minimal groups experiments. "
                "In these studies, test subjects were divided arbitrarily into two groups, based on a trivial and almost completely irrelevant basis such as preference for the abstract paintings of Klee or Kandinsky. "
                "Participants did not know other members of the group, did not even know who they were, and had no reason to expect that they would interact with them in the future. "
                "Still, members of both groups allocated resources in such a way that showed favouritism for members of their own group in a way that maximized their own group's outcomes in comparison to the alternate group, even at the expense of maximum gains for their own group.",
                nome="Henri Tajfel"),
            wiki("Minimal_group_paradigm",
                "ostensibly on the basis of trivial criteria (e.g., preference for paintings or the toss of a coin). [...] "
                "During this task, participants distribute a valuable resource (e.g., money or points) between other participants who are only identified by code number and group membership [...] "
                "The omission of the self as a recipient in the resource distribution task excludes the influence of direct personal self-interest. [...] "
                "Minimal group experiments tend to find that, although participants show a significant degree of fairness in their allocations, they also show a significant tendency to allocate more money or points to in-group members than to out-group members. "
                "Importantly, this strategy of maximizing relative in-group gain (maximum differentiation) occurs even when it means sacrificing absolute in-group gain [...] "
                "Henri Tajfel and colleagues originally developed the minimal group paradigm in the early 1970s as part of their attempt to understand the psychological basis of intergroup discrimination. "
                "Tajfel's intention was to create groups with as little meaning as possible and then add meaning to discover at what point discrimination would occur. "
                "The surprising finding was that, even in the most minimal group conditions, responses favoring the in-group occurred. [...] "
                "Tajfel instead developed social identity theory's motivational explanation.",
                nome="Minimal group paradigm"),
        ],
    },
    # 12 o efeito Hawthorne e os dados reencontrados
    {
        "temas_secundarios": ["experimentos_psicologia", "revolucao_industrial"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "Entre 1924 e 1927, uma fábrica aumentou a luz e a produção subiu; diminuiu a luz e ela subiu de novo, até na sala de controle. Daí veio o \"efeito Hawthorne\". Quando os dados reapareceram, em 2011, o efeito quase sumiu.",
        "explicacao": (
            "Os estudos foram feitos entre 1924 e 1932 na Hawthorne Works, fábrica da Western Electric nos arredores "
            "de Chicago. No de iluminação, de 1924 a 1927, uma sala tinha a luz alterada e outra servia de controle. "
            "A produtividade melhorou nas duas, tanto quando a luz aumentava quanto quando diminuía, e só caiu "
            "quando ficou fraca como a do luar. Num teste seguinte, com seis operárias montando relés de telefone, "
            "quase toda mudança, até a volta à condição original, parecia aumentar a produção. Pegou a "
            "interpretação de que as pessoas mudam o comportamento quando sabem que estão sendo observadas, e o "
            "nome \"efeito Hawthorne\" foi criado em 1953. Mas o estudo das operárias era mal desenhado e sem "
            "controle, e o psicólogo Richard Nisbett chamou o efeito de \"anedota glorificada\". Os economistas "
            "Steven Levitt e John List passaram muito tempo procurando os dados originais da iluminação, até "
            "achá-los num microfilme da Universidade de Wisconsin em Milwaukee, em 2011. Na reanálise, encontraram "
            "só um leve indício do efeito no longo prazo, nada tão dramático como se dizia. List, ainda assim, diz "
            "continuar confiante de que o efeito é real."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Hawthorne_effect",
            "The Hawthorne effect is a type of behavioral reactivity in which individuals modify an aspect of their behavior in response to their awareness of being observed. [...] "
            "Between 1924 and 1927, the lighting study was conducted [...] "
            "In an Elton Mayo study that ran from 1927 to 1928, a series of changes in work structure were implemented (e.g. changes in rest periods) in a group of six women. "
            "However, this was a methodologically poor, uncontrolled study from which no firm conclusions could be drawn. [...] "
            "The term \"Hawthorne effect\" was coined in 1953 by John R. P. French after the Hawthorne studies were conducted between 1924 and 1932 at the Hawthorne Works (a Western Electric factory in Cicero, outside Chicago). [...] "
            "The experiment ran in two rooms: the experiment room, in which workers went about their workday under various light levels; and the control room, in which workers did their tasks under normal conditions. [...] "
            "However, when the intensity of light was increased in the experiment room, researchers found that productivity had improved in both rooms. "
            "The light level in the experiment room was then decreased, and the results were the same: increased productivity in both rooms. "
            "Productivity only began to decrease in the experiment room when the light level was reduced to about the level of moonlight, which made it hard to see. [...] "
            "Until 1928, the team of women worked in a separate room, assembling telephone relays. [...] "
            "Changing a variable usually increased productivity, even if the variable was just a change back to the original condition. [...] "
            "Richard Nisbett has described the Hawthorne effect as \"a glorified anecdote\" [...] "
            "The economists Steven Levitt and John A. List long pursued without success a search for the base data of the original illumination experiments [...] "
            "before finding it in a microfilm at the University of Wisconsin in Milwaukee in 2011. "
            "Re-analysing it, they found slight evidence for the Hawthorne effect over the long-run, but in no way as drastic as suggested initially. [...] "
            "List has said that he remains confident that the effect is genuine.",
            nome="Hawthorne effect")],
    },
    # 13 os seis graus e as cartas que não chegaram
    {
        "temas_secundarios": ["probabilidade", "experimentos_psicologia"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "A ideia dos \"seis graus de separação\" vem de cartas passadas de conhecido em conhecido até um alvo em Boston, em 1967. Mas, numa das rodadas, 232 das 296 cartas nunca chegaram ao destino.",
        "explicacao": (
            "O experimento foi de Stanley Milgram, o mesmo dos estudos de obediência, e foi divulgado em 1967. "
            "Moradores de Omaha e Wichita, cidades escolhidas por parecerem distantes de Boston, recebiam um pacote "
            "com informações sobre uma pessoa-alvo lá e uma lista onde escrever o próprio nome antes de passar o "
            "pacote adiante. As 64 cartas que chegaram percorreram, em média, cerca de cinco e meio a seis elos, e "
            "daí veio a ideia de que estamos a uns seis passos de qualquer pessoa, embora Milgram nunca tenha usado "
            "a expressão \"seis graus de separação\". Os números guardam surpresas. A maioria das correntes se "
            "perdeu porque alguém se recusava a continuar. Correntes longas têm mais chance de esbarrar num "
            "desistente, então a média pode ter saído menor do que a real; além disso, os primeiros remetentes "
            "foram recrutados por um anúncio que buscava gente que se considerava bem relacionada. E poucos "
            "atalhos concentraram o tráfego: numa rodada com 160 cartas, das 24 que chegaram à casa do alvo, 16 "
            "foram entregues pela mesma pessoa, um comerciante de roupas. Em 2011, uma análise das conexões de 721 "
            "milhões de usuários do Facebook sugeriu um mundo ainda menor."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Small-world_experiment",
            "The experiments are often associated with the phrase \"six degrees of separation\", although Milgram did not use this term himself. [...] "
            "leading to the experiments reported in \"The Small World Problem\" in the May 1967 (charter) issue of the popular magazine Psychology Today [...] "
            "Milgram typically chose individuals in the U.S. cities of Omaha, Nebraska, and Wichita, Kansas, to be the starting points and Boston, Massachusetts, to be the end point of a chain of correspondence. "
            "These cities were selected because they were thought to represent a great distance in the United States, both socially and geographically. [...] "
            "basic information about a target contact person in Boston. "
            "It additionally contained a roster on which they could write their own name [...] "
            "However, a significant problem was that often people refused to pass the letter forward, and thus the chain never reached its destination. "
            "In one case, 232 of the 296 letters never reached the destination. "
            "However, 64 of the letters eventually did reach the target contact. "
            "Among these chains, the average path length fell around five and a half or six. [...] "
            "In an experiment in which 160 letters were mailed out, 24 reached the target in his home in Sharon, Massachusetts. "
            "Of those 24 letters, 16 were given to the target by the same person, a clothing merchant Milgram called \"Mr. Jacobs\". [...] "
            "as they were recruited through an advertisement that specifically sought people who considered themselves well-connected. "
            "Another problem has to do with the attrition rate. "
            "If one assumes a constant portion of non-response for each person in the chain, longer chains will be under-represented because it is more likely that they will encounter an unwilling participant. "
            "Hence, Milgram's experiment should underestimate the true average path length. [...] "
            "In 2011, researchers analyzed the connections between 721 million active Facebook users [...] "
            "suggesting a much smaller world than previously estimated.",
            nome="Small-world experiment")],
    },
    # 14 o mito do pânico nas multidões
    {
        "temas_secundarios": ["futebol", "cidades"],
        "tipos_espanto": ["mito_desmentido", "contraintuitivo"],
        "gancho": "Em tragédias com multidões, a culpa costuma ir para o \"pânico\". Um especialista resume o contrário: as pessoas não morrem porque entram em pânico, entram em pânico porque estão morrendo. O que mata é a densidade.",
        "explicacao": (
            "Até umas cinco pessoas por metro quadrado, uma multidão parece apertada, mas controlável. Com seis ou "
            "sete, os corpos ficam prensados e ninguém se move por vontade própria: a multidão passa a se "
            "comportar como um fluido, atravessada por ondas de pressão. Perto de dez por metro quadrado, a "
            "pressão pode asfixiar as pessoas ainda em pé, ou a massa desaba, e quem cai é esmagado pelo peso de "
            "quem cai por cima. Quem chega atrás muitas vezes não sabe o que acontece na frente e continua "
            "empurrando. Por isso, o fator crítico é a densidade, e não o tamanho da multidão. Mesmo assim, a "
            "imprensa costuma falar em \"estouro\" e pânico. Keith Still, professor de ciência das multidões, diz "
            "que nunca viu, nas análises, um caso de mortes em massa causadas por um estouro, e outro pesquisador "
            "chama a ideia da massa histérica de mito. Esses desastres são produto de falhas de organização, e a "
            "maioria poderia ser evitada com estratégias simples de gestão. Em Hillsborough, em 1989, parte dos "
            "policiais e fiscais estava tão preocupada com o que via como possível vandalismo de torcedores que "
            "tomou atitudes que pioraram a situação. Um sinal de perigo, para quem está no meio da multidão, é "
            "sentir-se tocado pelos quatro lados."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Crowd_crush",
            "When numbers are up to about five people per square meter, the environment may feel cramped but manageable [...] "
            "Under these conditions, the crowd may undergo a progressive collapse where the pressure pushes people off their feet, resulting in people being trampled or crushed by the weight of other people falling on top of them. "
            "At even higher densities, the pressure on each individual can cause them to be crushed or asphyxiated while still upright. "
            "Such incidents are invariably the product of organizational failures, and most major crowd disasters could have been prevented by simple crowd management strategies. [...] "
            "The critical factor is crowd density rather than crowd size. [...] "
            "and at higher densities of six to seven per square meter, individuals become pressed against each other and can be unable to move voluntarily. "
            "At this point a crowd can begin to behave like a fluid, with individuals moved about by the pressure of those around them, and shockwaves can pass through the crowd as pressures within the crowd change. [...] "
            "At even higher densities (approaching ten people per square metre (one per square foot)) a crowd can become so packed that people are crushed together to such an extent they can no longer breathe and are asphyxiated. [...] "
            "In this situation those entering may be unaware of the effect on those in front and continue to press in. [...] "
            "According to Keith Still, professor of crowd science at Manchester Metropolitan University, \"If you look at the analysis, I've not seen any instances of the cause of mass fatalities being a stampede. "
            "People don't die because they panic. They panic because they are dying\". "
            "Paul Torrens, a professor at the Center for Geospatial Information Science at the University of Maryland, remarks that \"the idea of the hysterical mass is a myth\". "
            "Incidents involving crowds are often reported by media as the results of panic. [...] "
            "In the 1989 Hillsborough disaster, some police and stewards were so concerned with what they saw as possible hooliganism that they took actions that actually made matters worse. [...] "
            "For a person in a crowd a signal of danger, and a warning to get out of the crowd if possible, is the sensation of being touched on all four sides.",
            nome="Crowd crush")],
    },
]
