LOTE = "2026-11-25-decisoes_economia-01"
AREA = "mente"
TEMA = "decisoes_economia"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


IYENGAR = "https://faculty.washington.edu/jdb/345/345%20Articles/Iyengar%20%26%20Lepper%20(2000).pdf"
SCHEIBEHENNE = "https://ideas.repec.org/a/oup/jconrs/v37y2010i3p409-425.html"

CANDIDATOS = [
    # 1 as geleias: 24 contra 6 sabores, e a meta-análise
    {
        "temas_secundarios": ["experimentos_psicologia", "vieses_cognitivos"],
        "tipos_espanto": ["contraintuitivo", "mito_desmentido"],
        "gancho": "Num supermercado da Califórnia, uma banca com 24 geleias atraiu mais gente que uma com 6, mas só 3% de quem parou nela comprou, contra quase 30% na menor. Repetir esse efeito se mostrou difícil.",
        "explicacao": (
            "O experimento, publicado em 2000 por Sheena Iyengar e Mark Lepper, foi feito numa loja de Menlo Park "
            "conhecida pela variedade: vendia mais de 300 tipos de geleia. Dois assistentes vestidos de funcionários "
            "convidavam quem passava a provar geleias da marca Wilkin & Sons. Em dois sábados, a mesa alternava de "
            "hora em hora entre 6 e 24 sabores. A banca grande parecia mais atraente: 60% de quem passou por ela "
            "parou, contra 40% na pequena, e nas duas as pessoas provaram, em média, quantidades parecidas. Todos "
            "ganhavam um cupom de 1 dólar de desconto, e a diferença apareceu na compra: quase 30% de quem viu 6 "
            "opções levou um pote, contra só 3% de quem viu 24. O estudo virou o símbolo do \"excesso de escolhas\". "
            "Mas, em 2010, uma meta-análise reuniu 50 experimentos, publicados ou não, com 5.036 participantes, e "
            "achou um efeito médio praticamente nulo, com grande variação de um estudo para outro. Outra "
            "meta-análise, de 2015, com 99 estudos, concluiu que o efeito aparece quando certas condições se somam, "
            "como escolhas complexas, tarefas difíceis e preferências incertas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            {"url": IYENGAR, "titulo": "Iyengar e Lepper (2000), When Choice is Demotivating", "idioma": "en",
             "trecho": "Journal of Personality and Social Psychology, 2000, Vol. 79 [...] "
                       "store (Draeger's Supermarket) located in Menlo Park, California. [...] "
                       "300 varieties of jam. [...] "
                       "Two research assistants, dressed as store employees, invited passing [...] "
                       "one of two displays. On the table were either 6 (limited-choice condition) [...] "
                       "or 24 (extensive-choice condition) different jams. [...] "
                       "days, the displays were rotated hourly [...] "
                       "wished. All consumers who approached the table received a coupon for a [...] "
                       "$1-discount off the purchase of any Wilkin & Sons jam. [...] "
                       "selection display of jams, 60% (145) actually stopped at the booth. [...] "
                       "display of jams, only 40% (104) stopped. [...] "
                       "Nearly 30% (31) of the consumers in the limited-choice condition subsequently purchased [...] "
                       "only 3% (4) of the consumers in the extensive-choice condition did so"},
            {"url": SCHEIBEHENNE, "titulo": "Scheibehenne, Greifeneder e Todd (2010), Can There Ever Be Too Many Options?", "idioma": "en",
             "trecho": "In a meta-analysis of 63 conditions from 50 published and unpublished experiments (N = 5,036), we found a mean effect size of virtually zero but considerable variance between studies. [...] "
                       "Benjamin Scheibehenne & Rainer Greifeneder & Peter M. Todd, 2010."},
            wiki("The_Paradox_of_Choice",
                "A new meta-analysis, conducted in 2015 and incorporating 99 studies, was able to isolate when reducing choices for your customers is most likely to boost sales. "
                "The study identified four key factors—choice set complexity, decision task difficulty, preference uncertainty, and decision goal—that moderate the impact of assortment size on choice overload.",
                nome="The Paradox of Choice"),
        ],
    },
    # 2 doação de órgãos: o padrão do formulário
    {
        "temas_secundarios": ["leis_julgamentos", "vieses_cognitivos"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Na Alemanha, onde é preciso se cadastrar para ser doador de órgãos, a taxa de consentimento citada é de 12%. Na vizinha Áustria, onde todos são doadores salvo recusa, 99,98%. Mas isso não garante mais transplantes.",
        "explicacao": (
            "É o exemplo mais conhecido do \"efeito padrão\": a opção que vale para quem não faz nada tende a ser a "
            "mais escolhida. Os dois países têm cultura e desenvolvimento econômico muito parecidos; muda a regra. "
            "No sistema de adesão, ninguém é doador até se registrar. No de consentimento presumido, todos são, a "
            "menos que peçam para sair. Há várias explicações para a força do padrão: escolher dá trabalho, sair "
            "dele tem custos, e ele pode ser lido como uma recomendação de quem fez a regra. Ele muda até o peso "
            "moral da escolha: sob o consentimento presumido, recusar-se a doar é visto como falha moral maior. "
            "Só que consentimento no papel não é o mesmo que órgãos doados. A Grécia tem consentimento presumido e "
            "cerca de 6 doadores por milhão de habitantes, enquanto a Espanha, recordista mundial, chegou a 46,9 "
            "por milhão em 2017. O presidente da Organização Nacional de Transplantes espanhola reconheceu que a "
            "lei provavelmente não é a principal razão do sucesso do país, que depende de coordenadores de "
            "transplante nos hospitais e de UTIs com médicos suficientes para identificar possíveis doadores."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Organ_donation",
                "Opt-out legislative systems dramatically increase effective consent rates for donation as a result of the default effect. "
                "For example, Germany, which uses an opt-in system, has an organ donation consent rate of 12% among its population. "
                "In contrast, Austria, a country with a very similar culture and economic development, but which uses an opt-out system, has a consent rate of 99.98%. [...] "
                "Because of public policies, cultural, infrastructural and other factors, presumed consent or opt-out models do not always translate directly into higher effective donation rates. [...] "
                "Some countries with an opt-out system, like Spain (40.2 donors per million inhabitants), Croatia (40.2 donors/million) or Belgium (31.6 donors/million) have high donor rates, however some countries such as Greece (6 donors/million) maintain low donor rates even with this system. "
                "The president of the Spanish National Transplant Organisation has acknowledged that Spain's legislative approach is likely not the primary reason for the country's success in increasing the donor rates, starting in the 1990s. [...] "
                "intensive care units (ICUs) must be staffed with enough doctors to maximize the identification of potential donors [...] "
                "The characteristic that enables the Spanish presumed consent model to be successful is the resource of transplant coordinators [...] "
                "Spain had the highest donor rate in the world, 46.9 per million people in the population, in 2017.",
                nome="Organ donation"),
            wiki("Default_effect",
                "In countries with the opt-in policy, all citizens are automatically considered as non-donors unless they actively register as donors. "
                "In countries with the opt-out policy, all citizens are automatically considered as donors unless they actively seek to be struck from the register. [...] "
                "it may involve too much cognitive effort to base a choice on explicit evaluations. [...] "
                "If an agent faces costs when diverging from a default that surmount the possible benefits from switching to another option, then it is rational to stick with the default option. [...] "
                "That the policy maker sets a default is interpreted as an implicit recommendation to choose that default option. [...] "
                "Under an opt-out policy, in contrast, choosing not to be an organ donor is perceived as morally more deficient.",
                nome="Default effect"),
        ],
    },
    # 3 as canecas de Cornell: o efeito dotação
    {
        "temas_secundarios": ["vieses_cognitivos", "experimentos_psicologia"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Num experimento clássico, estudantes que ganharam uma caneca pediam para vendê-la cerca do dobro do que outros aceitavam pagar por ela. Outros primatas mostram esse apego, mas há quem conteste o efeito.",
        "explicacao": (
            "É o \"efeito dotação\", estudado por Daniel Kahneman, Jack Knetsch e Richard Thaler com alunos da "
            "Universidade Cornell, num trabalho de 1990. Uns recebiam uma caneca e podiam vendê-la; outros podiam "
            "comprá-la. Os donos pediam uns 7 dólares para abrir mão dela, e os compradores ofereciam, em média, "
            "uns 3. Em testes desse tipo, a diferença aparece mesmo quando o objeto chegou às mãos da pessoa minutos "
            "antes. Pela teoria econômica padrão, quanto alguém paga por um bem e quanto aceita para se desfazer "
            "dele deveriam ser iguais. A explicação mais aceita é a aversão à perda: vender é perder algo, e perdas "
            "pesam mais que ganhos. O efeito já foi visto em crianças, grandes macacos e macacos do Novo Mundo, e "
            "uma proposta o trata como predisposição moldada pela evolução. Mas há contestações. Um grupo repetiu o "
            "teste com os mesmos produtos, canecas e barras de chocolate, e achou pouca evidência do efeito em bens "
            "com substitutos. Charles Plott e Kathryn Zeiler atribuíram a diferença a falhas no desenho dos "
            "experimentos. E David Gal propôs que é só inércia: sem saber o valor exato da caneca, nem quem compra "
            "nem quem vende tem motivo para negociar numa faixa de preços intermediária."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Endowment_effect",
            "people's maximum willingness to pay (WTP) to acquire an object is typically lower than the least amount they are willing to accept (WTA) to give up that same object when they own it—even when there is no cause for attachment, or even if the item was only obtained minutes ago. [...] "
            "One of the most famous examples of the endowment effect in the literature is from a study by Daniel Kahneman, Jack Knetsch & Richard Thaler, in which Cornell University undergraduates were given a mug [...] "
            "approximately twice as high as the amount they were willing to pay to acquire the mug [...] "
            "The leading explanation for the aforementioned WTP-WTA gap is that of loss aversion. [...] "
            "a person's willingness to pay (WTP) for a good should be equal to their willingness to accept (WTA) compensation to be deprived of the good [...] "
            "David Gal proposed a psychological inertia account of the endowment effect. "
            "In this account, sellers require a higher price to part with an object than buyers are willing to pay because neither has a well-defined, precise valuation for the object and therefore there is a range of prices over which neither buyers nor sellers have much incentive to trade. "
            "For example, in the case of Kahneman et al.'s (1990) classic mug experiments (where sellers demanded about $7 to part with their mug whereas buyers were only willing to pay, on average, about $3 to acquire a mug) [...] "
            "the endowment effect has been observed using different goods in a wide range of different populations, including children, great apes, and new world monkeys. [...] "
            "Jones (2001) proposed that the endowment effect is an evolved predisposition [...] "
            "They performed a more robust experiment with the same goods used by Kahneman, Knetsch and Thaler (chocolate bars and mugs) and found little evidence of the endowment effect in substitutable goods [...] "
            "More recently, Plott and Zeiler have challenged the endowment effect theory by arguing that observed disparities between WTA and WTP measures are not reflective of human preferences, but rather such disparities stem from faulty experimental designs.",
            nome="Endowment effect")],
    },
    # 4 a mosca do mictório e seus antepassados
    {
        "temas_secundarios": ["invencoes", "vieses_cognitivos"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "A mosca gravada nos mictórios do aeroporto de Amsterdã, o \"empurrãozinho\" favorito do Nobel Richard Thaler, tem antepassados: na Grã-Bretanha do fim do século XIX, já se punham abelhas nas privadas, por piada.",
        "explicacao": (
            "No início dos anos 1990, o aeroporto de Schiphol passou a gravar moscas nos mictórios masculinos para "
            "reduzir a urina que caía no chão. A ideia costuma ser creditada ao gerente Aad Kieboom, mas, segundo "
            "ele, veio do chefe da limpeza, Jos van Bedaf. Nos anos 1960, quando era soldado, van Bedaf notou que "
            "uma latrina em que alguém desenhara um ponto num mictório ficava mais limpa que as outras. E escolheu "
            "a mosca porque, disse, é o bicho em que as pessoas mais gostariam de urinar. O truque tinha "
            "precedentes: os britânicos do século XIX desenhavam abelhas em mictórios, num trocadilho com a "
            "pronúncia de Apis, o gênero da abelha, e Thomas Crapper pôs uma abelha nas privadas da sua empresa. "
            "Segundo testes feitos por funcionários de Schiphol, os respingos caíram 80% e o custo de limpeza, uns "
            "8%. Em 2008, Thaler e Cass Sunstein usaram o caso no livro \"Nudge\", e Thaler o chamou de seu exemplo "
            "favorito. O efeito dos empurrõezinhos em geral, porém, é debatido: uma meta-análise de 2021 achou "
            "efeito, mas com viés de publicação, e outra concluiu que, corrigido esse viés, não há evidência de "
            "efeito. Dados de equipes de governo, com mais de 23 milhões de pessoas, mostraram efeitos bem menores "
            "que os publicados."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Urinal_fly",
                "In late-19th century Great Britain, people would put pictures of bees in urinals and toilets. "
                "They served as a target, but also a joke about the pronunciation of the honeybee's genus, Apis. "
                "Engineer and businessman Thomas Crapper even put a picture of a bee in the toilets his company produced [...] "
                "In the early 1990s, Amsterdam's Schiphol Airport introduced pictures of flies to its men's room urinals in an effort to reduce \"spillage\", or the amount of urine which spills onto the floor and must then be cleaned. "
                "Though sometimes credited to Aad Kieboom, a manager at the airport, according to Kieboom it was the cleaning department's manager, Jos van Bedaf, who had the idea. "
                "Van Bedaf remembered, during his time as a soldier in 1960s, that someone had drawn a dot in one of the urinals, and that the latrine with that urinal was cleaner than others. "
                "He suggested a fly because, he said, it is the animal people would most like to urinate on. [...] "
                "Employees of Schiphol Airport conducted trials to test how effective their etched images of flies were. "
                "The result was an 80% reduction in spillage, cutting cleaning costs by about 8%. "
                "Richard Thaler and Cass Sunstein included urinal targets as an example of what they call \"nudging\" in their 2008 book Nudge [...] "
                "Thaler, a behavioral economist, called it his favorite example of a nudge.",
                nome="Urinal target"),
            wiki("Nudge_theory",
                "A meta-analysis of all unpublished nudging studies carried by nudge units with over 23 million individuals in the United Kingdom and United States found effectiveness in some nudges, but with substantially weaker effects than published studies indicate. [...] "
                "Mertens and colleagues (2021) produced a comprehensive meta-analysis. "
                "They found that nudging is effective but there is a moderate publication bias. "
                "Later, Maier and colleagues found that, after correcting for this publication bias appropriately, there is no evidence that nudging would have any effect.",
                nome="Nudge theory"),
            wiki("Richard_Thaler",
                "In 2017, he was awarded the Nobel Memorial Prize in Economic Sciences for his contributions to behavioral economics.",
                nome="Richard Thaler"),
        ],
    },
    # 5 o problema da doença asiática: o enquadramento
    {
        "temas_secundarios": ["vieses_cognitivos", "experimentos_psicologia"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Diga que um tratamento \"salva 200 de 600 pessoas\", e 72% o escolhem. Diga que, com ele, \"400 morrerão\", e 78% passam a preferir uma alternativa arriscada. Os números são os mesmos; muda só o enquadramento.",
        "explicacao": (
            "É o \"problema da doença asiática\", apresentado por Amos Tversky e Daniel Kahneman num artigo de "
            "1981 sobre o enquadramento das decisões. Os participantes imaginavam uma doença mortal que atingiria "
            "600 pessoas e escolhiam entre dois tratamentos. Com o A, morreriam 400 pessoas, ou seja, 200 seriam "
            "salvas. Com o B, havia 33% de chance de ninguém morrer e 66% de chance de todos morrerem. Quando as "
            "opções eram descritas pelas vidas salvas, 72% ficavam com o A. Quando eram descritas pelas mortes, o "
            "resultado se invertia, e 78% escolhiam o B. Para o modelo do agente racional, que supõe preferências "
            "estáveis e decisões sem viés, a forma de contar não deveria importar. Kahneman e Tversky usaram "
            "resultados como esse para sustentar a teoria da perspectiva, segundo a qual as pessoas tomam decisões "
            "inconsistentes conforme o modo como as opções são apresentadas. O efeito aparece também em decisões "
            "médicas reais: idosos aceitam mais um tratamento descrito em termos positivos do que o mesmo "
            "tratamento descrito de forma neutra ou negativa, e uma mudança na descrição pode levá-los a desfazer "
            "uma decisão já tomada."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Framing_effect_(psychology)",
            "The model includes several core assumptions: rational actors have stable preferences, access to all relevant information, the capability to analyze all possible options and outcomes, and are unbiased and unemotional. [...] "
            "Tversky and Kahneman proposed a new theoretical frame to understand decision-making in their 1981 paper, \"The Framing of Decisions and the Psychology of Choice.\" [...] "
            "They proposed prospect theory, which, unlike traditional economic theories that assume people make rational choices by calculating risks and benefits, recognizes that people make biased or inconsistent decisions in real life based on how options are presented—or, in other words, framed. [...] "
            "the Asian disease problem: participants were asked to choose between two treatments. [...] "
            "Participants were asked to choose between two treatments for 600 people affected by a deadly disease. "
            "Treatment A was predicted to result in 400 deaths, whereas treatment B had a 33% chance that no one would die but a 66% chance that everyone would die. "
            "This choice was then presented to participants either with positive framing, i.e. how many people would live, or with negative framing, i.e. how many people would die. "
            "Treatment A was chosen by 72% of participants when it was presented with positive framing (\"saves 200 lives\"). "
            "When the question was negatively framed, the result reversed, and 78% of participants chose Treatment B. [...] "
            "older adults are significantly more likely to agree to a treatment when it is positively described than they are to agree to the same treatment when it is described neutrally or negatively. "
            "Additionally, framing often leads to inconsistency in choice: a change in description qualities after an initial choice is made can cause older adults to revoke their initial decision in favor of an alternative option.",
            nome="Framing effect (psychology)")],
    },
    # 6 macacos-prego e a aversão à perda (e o debate)
    {
        "temas_secundarios": ["comportamento_animal", "vieses_cognitivos"],
        "tipos_espanto": ["conexao_inesperada", "contraintuitivo"],
        "gancho": "Macacos-prego que usavam fichas como dinheiro preferiam quem mostrava 1 pedaço de maçã e o entregava a quem mostrava 2 e tirava um antes. Mas se a aversão à perda é tão geral ainda se discute.",
        "explicacao": (
            "A aversão à perda, uma das ideias centrais da economia comportamental, diz que uma perda pesa mais do "
            "que um ganho do mesmo tamanho. Em 2005, macacos-prego treinados por vários meses passaram a se "
            "comportar como quem entende o que é um meio de troca e mostraram a mesma tendência humana a evitar "
            "perdas percebidas. Num experimento de 2006, Chen, Lakshminarayanan e Santos puseram os macacos para "
            "trocar suas fichas com dois pesquisadores que, no fim, davam exatamente o mesmo: um pedaço de maçã. Um "
            "mostrava um pedaço e o entregava. O outro mostrava dois e sempre tirava um antes da entrega. Os "
            "macacos preferiram com força o primeiro, como se o pedaço retirado fosse uma perda. O conceito, porém, "
            "vem sendo questionado. Vários estudos não acharam aversão à perda em decisões sob risco, talvez porque "
            "ela não apareça com valores pequenos. David Gal, em 2006, e depois Gal e Rucker, em 2018, argumentaram "
            "que muitos fenômenos atribuídos a ela, como o efeito dotação, se explicam melhor por inércia. Em 2019, "
            "outro grupo replicou a aversão à perda em cinco amostras. E, em 2025, uma nova meta-análise saiu com um "
            "título que diz o contrário: a aversão à perda \"não é robusta\"."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Loss_aversion",
            "Multiple studies have questioned the existence of loss aversion. "
            "In several studies examining the effect of losses in decision-making,  no loss aversion was found under risk and uncertainty. "
            "There are several explanations for these findings: one is that loss aversion does not exist in small payoff magnitudes [...] "
            "David Gal (2006) argued that many of the phenomena commonly attributed to loss aversion, including the status quo bias, the endowment effect, and the preference for safe over risky options, are more parsimoniously explained by psychological inertia than by a loss/gain asymmetry. "
            "Gal and Rucker (2018) made similar arguments. "
            "Mkrva, Johnson, Gächter, and Herrmann (2019) cast doubt on these critiques, replicating loss aversion in five unique samples [...] "
            "In 2005, experiments were conducted on the ability of capuchin monkeys to use money. "
            "After several months of training, the monkeys began showing behavior considered to reflect understanding of the concept of a medium of exchange. "
            "They exhibited the same propensity to avoid perceived losses demonstrated by human subjects and investors. "
            "Chen, Lakshminarayanan and Santos (2006) also conducted experiments on capuchin monkeys to determine whether behavioral biases extend across species. "
            "In one of their experiments, subjects were presented with two choices that both delivered an identical payoff of one apple piece in exchange of their coins. "
            "Experimenter 1 displayed one apple piece and gave that exact amount. "
            "Experimenter 2 displayed two apple pieces initially but always removed one piece before delivering the remaining apple piece to the subject. [...] "
            "It was found that subjects strongly preferred the experimenter who initially displayed only one apple piece, even though both experimenters yielded the same outcome of one apple piece. "
            "This study suggests that capuchins weighted losses more heavily than equivalent gains. [...] "
            "Yechiam, Eldad., and Dana Zeif. 2025. Loss aversion is not robust: A re-meta-analysis.",
            nome="Loss aversion")],
    },
    # 7 os juízes famintos e a ordem dos casos
    {
        "temas_secundarios": ["experimentos_psicologia", "leis_julgamentos"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Um estudo de 2011 com comissões de liberdade condicional em Israel viu 65% de pedidos aceitos no início de cada sessão e quase nenhum antes da pausa para comer. Críticos culpam a ordem dos casos, não a fome.",
        "explicacao": (
            "Publicado na revista PNAS, o estudo deu nome ao \"efeito do juiz faminto\" e chegou perto de 2.500 "
            "citações. Os autores sugeriram que o cansaço mental empurrava as decisões para a manutenção da "
            "situação, e que o descanso e a comida devolviam a disposição para decisões ousadas. Nas audiências de "
            "liberdade condicional, a opção padrão é justamente negar o pedido. Poucos meses depois, a mesma "
            "revista publicou uma carta de pesquisadores que haviam conversado com advogados, um juiz e outros "
            "funcionários: a ordem dos casos não era aleatória. Presos sem advogado costumavam ficar para o fim de "
            "cada sessão, e advogados com vários clientes podiam escolher a ordem por estratégia. Uma análise "
            "posterior, com simulações, sugeriu que ao menos parte do efeito vinha da agenda: casos com desfecho "
            "favorável tomavam mais tempo e não eram encaixados no tempo restante antes de um intervalo. O "
            "psicólogo Daniël Lakens argumentou que o tamanho do efeito é grande demais para ser possível. Mesmo "
            "assim, o estudo segue citado, por exemplo, para justificar algoritmos nos tribunais e no livro "
            "\"Determined\", em que Robert Sapolsky defende que temos menos livre-arbítrio do que pensamos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [
            wiki("Hungry_judge_effect",
                "A study of the decisions of Israeli parole boards was made in 2011. "
                "It found that the granting of parole was 65% at the start of a session but would drop to nearly zero before a meal break. "
                "The authors suggested that mental depletion as a result of fatigue caused decisions to increasingly favour the status quo, while rest and replenishment then restored a willingness to make bold decisions. "
                "The paper, which was published in the Proceedings of the National Academy of Sciences, has been cited many times – close to 2,500 times by 2026. [...] "
                "A few months after the original paper, the Proceedings of the National Academy of Sciences published a letter arguing, based on conversations with attorneys, a judge, and other personnel, that case ordering is not random, as, e.g., within sessions, unrepresented prisoners usually go last and represented prisoners sharing an attorney may have their ordering determined strategically by counsel. [...] "
                "A later analysis and simulations suggested that at least part of the effect might arise from scheduling priorities – that cases with a lenient outcome required more time and so would not be scheduled in the time remaining before a break. "
                "Psychologist Daniël Lakens has argued that the size of the effect in the original study is impossibly large. [...] "
                "Interventions of AI and algorithms in the court such as COMPAS software are usually motivated by the hungry judge effect. [...] "
                "Robert Sapolsky uses this as an example to argue we have lesser free will than we think in his book Determined.",
                nome="Hungry judge effect"),
            wiki("Default_effect",
                "The default option for parole hearings, for example, is to deny prisoners parole.",
                nome="Default effect"),
        ],
    },
    # 8 o salário de 5 dólares de Henry Ford
    {
        "temas_secundarios": ["revolucao_industrial", "economia_curiosa"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "Em 1914, Henry Ford mais que dobrou a diária da maioria dos operários, para 5 dólares. Não era só bondade: setores da fábrica contratavam 300 homens por ano para manter 100 vagas. E havia fiscais da vida privada.",
        "explicacao": (
            "Em 5 de janeiro de 1914, Ford anunciou que o pagamento mínimo diário subiria de 2,34 para 5 dólares "
            "para os homens que se qualificassem. Um jornal de Cleveland escreveu que a notícia rasgou como um "
            "foguete as nuvens escuras da depressão industrial. O problema era a rotatividade: muita gente entrava "
            "e saía, e treinar substitutos custava caro. Com o salário alto, os melhores mecânicos de Detroit "
            "correram para a Ford, a produtividade subiu e os custos de treinamento caíram; os concorrentes tiveram "
            "de aumentar salários ou perder seus melhores trabalhadores. Um estudo de Raff e Summers, de 1987, "
            "concluiu que o caso se encaixa na ideia de \"salário de eficiência\": pagar acima do mercado para "
            "reduzir a rotatividade e aumentar a produtividade. Houve filas por vagas na Ford e lucros maiores. Mas "
            "havia condições. A parte paga como participação nos lucros só valia para quem tinha seis meses de casa "
            "e levava a vida do jeito aprovado pelo \"Departamento Social\" da empresa. Com 50 investigadores e "
            "pessoal de apoio, ele via com maus olhos a bebedeira, o jogo e os pais que abandonavam os filhos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Henry_Ford",
                "Ford was a pioneer of \"welfare capitalism\", designed to improve the lot of his workers and especially to reduce the heavy turnover that had many departments hiring 300 men per year to fill 100 slots. [...] "
                "Ford astonished the world in 1914 by offering a $5 daily wage ($161 in 2025), which more than doubled the rate of most of his workers. "
                "A Cleveland, Ohio newspaper editorialized that the announcement \"shot like a blinding rocket through the dark clouds of the present industrial depression\". "
                "The move proved extremely profitable; instead of constant employee turnover, the best mechanics in Detroit flocked to Ford, bringing their human capital and expertise, raising productivity, and lowering training costs. "
                "Ford announced his $5-per-day program on January 5, 1914, raising the minimum daily pay from $2.34 to $5 for qualifying male workers. "
                "Detroit was already a high-wage city, but competitors were forced to raise wages or lose their best workers. [...] "
                "Real profit-sharing was offered to employees who had worked at the company for six months or more, and, importantly, conducted their lives in a manner that Ford's \"Social Department\" approved. "
                "They frowned on heavy drinking, gambling, and on what are now called deadbeat dads. "
                "The Social Department used 50 investigators and support staff to maintain employee standards",
                nome="Henry Ford"),
            wiki("Efficiency_wage",
                "an efficiency wage is a wage paid in excess of the market-clearing wage to increase the labor productivity of workers. "
                "Specifically, it points to the incentive for managers to pay their employees more than the market-clearing wage to increase their productivity or to reduce the costs associated with employee turnover. [...] "
                "Raff and Summers (1987) conduct a case study on Henry Ford’s introduction of the five dollar day in 1914. "
                "Their conclusion is that the Ford experience supports efficiency wage interpretations. [...] "
                "evidence of substantial queues for Ford jobs, and significant increases in productivity and profits at Ford.",
                nome="Efficiency wage"),
        ],
    },
    # 9 Kahneman, o psicólogo do Nobel de Economia, e Tversky
    {
        "temas_secundarios": ["experimentos_psicologia", "vieses_cognitivos"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Daniel Kahneman ganhou o Nobel de Economia de 2002 sem nunca ter feito um curso de economia: era psicólogo. Segundo ele, o prêmio teria sido dividido com o parceiro Amos Tversky, morto em 1996.",
        "explicacao": (
            "Kahneman dividiu aquele Nobel com o economista experimental Vernon Smith, por levar à economia ideias "
            "da psicologia sobre o julgamento e a decisão sob incerteza. A colaboração com Tversky começou em 1969, "
            "na Universidade Hebraica de Jerusalém, depois que Tversky deu uma palestra num seminário de Kahneman. "
            "No primeiro artigo, publicado em 1971, os dois tiraram cara ou coroa para decidir de quem seria o "
            "primeiro nome e depois foram alternando. A teoria da perspectiva, publicada em 1979 na Econometrica, "
            "virou o artigo mais citado da revista. Nesse período, eram descritos como inseparáveis, \"almas "
            "gêmeas\". A parceria esfriou depois que saíram de Israel, em 1978, em parte porque Tversky recebia a "
            "maior parte do crédito de fora, e Kahneman chegou a dizer que acabou se \"divorciando\" dele. Mesmo "
            "assim, seguiram publicando juntos até o fim da vida de Tversky, que morreu aos 59 anos. Kahneman "
            "escreveu que a colaboração dos dois foi a razão do prêmio. E, a partir de 2020, passou a viver em Nova "
            "York com a psicóloga cognitiva Barbara Tversky, viúva do antigo parceiro."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Daniel_Kahneman",
            "for which he was awarded the 2002 Nobel Memorial Prize in Economic Sciences together with Vernon L. Smith. [...] "
            "Kahneman's lengthy collaboration with Amos Tversky began in 1969, after Tversky gave a guest lecture at one of Kahneman's seminars at Hebrew University. "
            "Their first jointly written paper, \"Belief in the Law of Small Numbers,\" was published in 1971. [...] "
            "They flipped a coin to determine whose name would appear first on their initial paper and alternated thereafter. [...] "
            "The final version was published in 1979 in Econometrica, the leading economic journal at the time. "
            "That paper became the most cited in Econometrica. [...] "
            "\"for having integrated insights from psychological research into economic science, especially concerning human judgment and decision-making under uncertainty\". [...] "
            "\"our collaboration on judgment and decision making was the reason for the Nobel Prize that I received in 2002, which Amos Tversky would have shared had he not died, aged fifty-nine, in 1996\". [...] "
            "During this period they were described as \"inseparable\" and as \"soul mates\". "
            "After leaving Israel in 1978 and accepting positions at different universities, the intensity and exclusivity of their earlier period of joint collaboration was reduced. [...] "
            "Factors contributing to this estrangement included Tversky receiving most of the external credit for the output of the partnership, and a reduction in the generosity with which Tversky and Kahneman interacted with each other, leading Kahneman to say, \"I eventually divorced him\". "
            "However, they would continue to publish together until the end of Tversky's life [...] "
            "From 2020, Kahneman lived in New York City with Barbara Tversky, also a cognitive psychologist, and the widow of his long-time collaborator Amos Tversky. [...] "
            "In 2002, Kahneman received the Nobel Memorial Prize in Economic Sciences, despite being a research psychologist, for his work in prospect theory. "
            "Kahneman stated he has never taken a single economics course.",
            nome="Daniel Kahneman")],
    },
    # 10 Ellsberg: o paradoxo das urnas e os Papéis do Pentágono
    {
        "temas_secundarios": ["guerra_fria", "teoria_jogos"],
        "tipos_espanto": ["conexao_inesperada", "historia_humana"],
        "gancho": "Daniel Ellsberg, que em 1971 vazou os Papéis do Pentágono sobre a Guerra do Vietnã, antes criara um paradoxo famoso da teoria da decisão: preferimos riscos de probabilidade conhecida aos de probabilidade ignorada.",
        "explicacao": (
            "Ellsberg se formou em economia em Harvard em 1952, serviu nos fuzileiros navais e voltou à "
            "universidade em 1957 para estudar decisões sob incerteza. Em 1961, publicou o artigo que popularizou o "
            "paradoxo, e em 1962 concluiu o doutorado com uma tese baseada em experimentos mentais. O mais simples "
            "usa duas urnas com 100 bolas. Uma tem 50 vermelhas e 50 pretas; a outra tem vermelhas e pretas numa "
            "mistura desconhecida. As pessoas costumam achar indiferente apostar no vermelho ou no preto da "
            "primeira urna, mas preferem a primeira à segunda, seja qual for a cor. É uma escolha incompatível com a "
            "teoria da utilidade esperada subjetiva: ao que parece, as pessoas não gostam de situações às quais não "
            "conseguem atribuir probabilidades. O fenômeno ganhou o nome de aversão à ambiguidade e gerou uma grande "
            "literatura a partir dos anos 1980. John Maynard Keynes já publicara uma versão da ideia em 1921. "
            "Ellsberg trabalhava como analista na RAND Corporation quando entregou aos jornais um estudo secreto do "
            "Pentágono sobre as decisões do governo na Guerra do Vietnã. Acusado com base na Lei de Espionagem, com "
            "pena máxima de 115 anos, teve as acusações anuladas em 1973 por má conduta do governo."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Ellsberg_paradox",
                "John Maynard Keynes published a version of the paradox in 1921. "
                "Daniel Ellsberg popularized the paradox in his 1961 paper, \"Risk, Ambiguity, and the Savage Axioms\". "
                "It is generally taken to be evidence of ambiguity aversion [...] "
                "There are two urns each containing 100 balls. "
                "It is known that urn A contains 50 red and 50 black, but urn B contains an unknown mix of red and black balls. [...] "
                "Typically, participants were seen to be indifferent between bet 1A and bet 2A (consistent with expected utility theory) but were seen to strictly prefer Bet 1A to Bet 1B and Bet 2A to 2B. "
                "This result is generally interpreted to be a consequence of ambiguity aversion (also known as uncertainty aversion); people intrinsically dislike situations where they cannot attach probabilities to outcomes [...] "
                "Upon graduating in Economics from Harvard in 1952, Ellsberg left immediately to serve as a US Marine before coming back to Harvard in 1957 to complete his post-graduate studies on decision-making under uncertainty.",
                nome="Ellsberg paradox"),
            wiki("Daniel_Ellsberg",
                "While employed by the RAND Corporation, he precipitated a national political controversy in 1971 when he released the Pentagon Papers – a top-secret Pentagon study of U.S. government decision-making regarding the Vietnam War – to The New York Times, The Washington Post, and other newspapers. "
                "In January 1973, Ellsberg was charged under the Espionage Act of 1917 along with other charges of theft and conspiracy, carrying a maximum sentence of 115 years. "
                "As a result of governmental misconduct and illegal evidence-gathering [...] "
                "dismissed all charges against Ellsberg in May 1973. [...] "
                "Ellsberg completed a PhD in economics from Harvard in 1962. "
                "His dissertation on decision theory was based on a set of thought experiments that showed that decisions under conditions of uncertainty or ambiguity generally may not be consistent with well-defined subjective probabilities. "
                "Now known as the Ellsberg paradox, it formed the basis of a large literature that has developed since the 1980s",
                nome="Daniel Ellsberg"),
        ],
    },
    # 11 Allais e os economistas de Paris
    {
        "temas_secundarios": ["probabilidade", "historia_matematica"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1952, num congresso em Paris, Maurice Allais propôs uma escolha entre loterias hipotéticas a uma plateia de economistas, e eles responderam de um jeito incoerente com a teoria da utilidade esperada.",
        "explicacao": (
            "Na primeira escolha, a opção A dá 1 milhão de dólares com certeza. A B dá 89% de chance de 1 milhão, "
            "10% de chance de 5 milhões e 1% de chance de nada. A maioria fica com a A. Na segunda, as duas opções "
            "têm 89% de chance de não dar nada; no resto, uma oferece 11% de chance de 1 milhão, e a outra, 10% de "
            "chance de 5 milhões e 1% de nada. Aí a maioria prefere a segunda. Mas, descontada a parte de 89% que é "
            "igual dentro de cada par, as duas escolhas são idênticas. Pela teoria da utilidade esperada, "
            "resultados iguais deveriam se anular, e quem escolhe A num caso deveria escolher A no outro. A "
            "explicação mais comum é o efeito certeza: a garantia total atrai mais do que a teoria prevê. A plateia "
            "de Paris não se convenceu e tratou o resultado como uma simples irregularidade. Allais publicou o "
            "paradoxo em 1953, num artigo em francês na revista Econometrica, e sua obra só ganhou tradução para o "
            "inglês em 1979. O paradoxo inspirou alternativas como a teoria da perspectiva, de Kahneman e Tversky. "
            "Allais ganhou o Nobel de Economia em 1988, por contribuições à teoria dos mercados, o que também "
            "aumentou o reconhecimento do paradoxo."
        ),
        "nivel": 2, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Allais_paradox",
            "Likewise, when presented with a choice between 2A and 2B, most people would choose 2B. [...] "
            "presented with a choice between 1A and 1B, most people would choose 1A. [...] "
            "According to expected utility theory, the person should choose either 1A and 2A or 1B and 2B. "
            "The inconsistency stems from the fact that in expected utility theory, equal outcomes added to each of two choices (e.g. the 89% chance of $1 million for both 1A and 1B over 2A and 2B) should have no effect on the relative desirability of one gamble over the other; equal outcomes should \"cancel out\". "
            "In each experiment the two gambles give the same outcome 89% of the time (starting from the top row and moving down, both 1A and 1B give an outcome of $1 million with 89% probability, and both 2A and 2B give an outcome of nothing with 89% probability). "
            "If this 89% 'common consequence' is disregarded, then in each experiment the choice between gambles will be the same – 11% chance of $1 million versus 10% chance of $5 million and 1% chance of nothing. [...] "
            "Difficulties such as this gave rise to a number of alternatives to, and generalizations of, the theory, notably including prospect theory, developed by Daniel Kahneman and Amos Tversky [...] "
            "The most common explanation of the Allais paradox is that individuals prefer certainty over a risky outcome even if this defies the expected utility axiom. [...] "
            "The Allais Paradox was first introduced in 1952, where Maurice Allais presented various choice sets to an audience of economists at Colloques Internationaux du Centre National de la Recherche Scientifique, an economics conference in Paris. "
            "Similar to the choice sets above, the audience provided decisions that were inconsistent with expected utility theory. "
            "Despite this result, the audience was not convinced of the validity of Allais's finding and dismissed the paradox as a simple irregularity. "
            "Regardless, in 1953 Allais published his finding of the Allais paradox in Econometrica [...] "
            "Allais's work had not been translated from French to English until 1979 [...] "
            "Allais's prominence was further promoted when he received the Nobel Prize in Economic Sciences in 1988 for \"his pioneering contributions to the theory of markets and efficient utilization of resources\", thus bolstering the recognition of the paradox. [...] "
            "Allais, M. (1953). \"Le comportement de l'homme rationnel devant le risque: critique des postulats et axiomes de l'école Américaine\". Econometrica.",
            nome="Allais paradox")],
    },
    # 12 o paradoxo de São Petersburgo e a invenção da utilidade
    {
        "temas_secundarios": ["probabilidade", "historia_matematica"],
        "tipos_espanto": ["contraintuitivo", "escala_absurda"],
        "gancho": "Num jogo de cara ou coroa em que o prêmio dobra a cada coroa, o ganho esperado é infinito, mas quase ninguém pagaria caro para jogar. O enigma, de 1713, ajudou a criar a ideia de que o dinheiro vale cada vez menos.",
        "explicacao": (
            "O problema foi proposto por Nicolau Bernoulli numa carta de 1713. Numa versão comum, a aposta começa em "
            "2 dólares e dobra a cada coroa; na primeira cara, o jogo acaba e o jogador leva o valor acumulado. "
            "Metade das vezes ele ganha 2, um quarto das vezes ganha 4, um oitavo das vezes, 8, e assim por diante. "
            "Somadas, essas parcelas crescem sem limite, e a média esperada do ganho é infinita. Pela conta, valeria "
            "pagar qualquer preço para jogar. Mas Daniel Bernoulli, primo de Nicolau, que morou em São Petersburgo, "
            "escreveu em 1738 que qualquer homem razoável venderia sua chance, com prazer, por 20 ducados. A saída "
            "dele foi pensar na utilidade: cada dinheiro a mais vale menos para quem já tem muito, e com essa "
            "\"utilidade marginal decrescente\" o valor do jogo fica finito. Gabriel Cramer, de Genebra, chegara a "
            "parte da ideia em 1728. Há também uma saída prática: nenhuma banca tem dinheiro infinito. Em 1777, o "
            "conde de Buffon calculou que, depois de 29 rodadas, não haveria dinheiro suficiente em todo o Reino da "
            "França para pagar o prêmio."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("St._Petersburg_paradox",
            "The problem was invented by Nicolas Bernoulli, who stated it in a letter to Pierre Raymond de Montmort on September 9, 1713. "
            "However, the paradox takes its name from its analysis by Nicolas' cousin Daniel Bernoulli, one-time resident of Saint Petersburg, who in 1738 published his thoughts about the problem [...] "
            "The initial stake begins at 2 dollars and is doubled every time tails appears. "
            "The first time heads appears, the game ends and the player wins whatever is the current stake. [...] "
            "with probability ⁠1/2⁠, the player wins 2 dollars; with probability ⁠1/4⁠ the player wins 4 dollars; with probability ⁠1/8⁠ the player wins 8 dollars, and so on. [...] "
            "This sum grows without bound so the expected win is an infinite amount of money. [...] "
            "one should therefore play the game at any price if offered the opportunity. [...] "
            "\"Although the standard calculation shows that the value of [the player's] expectation is infinitely great, it has ... to be admitted that any fairly reasonable man would sell his chance, with great pleasure, for twenty ducats.\" [...] "
            "A common utility model, suggested by Daniel Bernoulli, is the logarithmic function U(w) = ln(w) (known as log utility). "
            "It is a function of the gambler's total wealth w, and the concept of diminishing marginal utility of money is built into it. [...] "
            "The expected incremental utility of the lottery now converges to a finite value: [...] "
            "Before Daniel Bernoulli's 1738 publication, mathematician Gabriel Cramer from the Republic of Geneva had already in 1728 found parts of this idea [...] "
            "The classical St. Petersburg game assumes that the casino or banker has infinite resources. [...] "
            "In 1777, Georges-Louis Leclerc, Comte de Buffon calculated that after 29 rounds of play there would not be enough money in the Kingdom of France to cover the bet.",
            nome="St. Petersburg paradox")],
    },
    # 13 a multa da creche que aumentou os atrasos
    {
        "temas_secundarios": ["economia_curiosa", "psicologia_social"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Creches em Israel tinham pais que chegavam tarde para buscar os filhos. Num experimento, passaram a cobrar multa pelo atraso, e os atrasos aumentaram: a multa funcionou como o preço de um serviço.",
        "explicacao": (
            "O experimento de campo foi conduzido por Uri Gneezy e Aldo Rustichini, e o artigo tem um título que "
            "resume a conclusão: \"Uma multa é um preço\". A interpretação deles é que a multa transformou a norma "
            "social da pontualidade numa norma de mercado, de pagar por um serviço. O valor cobrado ainda "
            "sinalizava que atrasar não era tão grave assim, e a relação virou uma troca. O caso é um exemplo "
            "famoso do efeito de \"expulsão\" (crowding out): incentivos financeiros podem enfraquecer a motivação "
            "que já existia. A ideia entrou na economia com Richard Titmuss, que em 1970 argumentou que oferecer "
            "dinheiro por certos comportamentos, contra a intuição, poderia reduzi-los; no caso da doação de "
            "sangue, que ele estudou, as evidências são mistas. Em outro trabalho, Gneezy e Rustichini mostraram "
            "experimentos em que quem recebia incentivo em dinheiro se saía pior do que quem não recebia nada; o "
            "título era \"Pague o suficiente ou não pague nada\". Estudos seguintes de Gneezy e colegas indicam que o "
            "dinheiro pode motivar em tarefas vistas como chatas, mas sai pela culatra nas que já são "
            "interessantes por si."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Uri_Gneezy",
                "One of Gneezy's seminal studies on crowding out was conducted in collaboration with Aldo Rustichini, and it involved daycare centers in Israel. "
                "The centers had a problem with parents who were frequently late to pick up their children. "
                "In a field experiment, Gneezy and Rustichini implemented a fine for late pick-ups to incentivize parents to be more punctual. "
                "Surprisingly, after the fine was introduced, the number of late pick-ups increased. "
                "They observed that the fine had effectively transformed the social norm of punctuality into a market norm of paying for a service. "
                "The fine served as a signal that being late is not that bad, and transformed the interaction into an exchange. "
                "In another paper with Rustichini they present a set of experiments showing that participants who were offered monetary incentives performed worse than those who were offered no compensation. "
                "In subsequent studies, Gneezy and his colleagues explored the conditions under which extrinsic incentives can crowd out intrinsic motivation. "
                "They found that when tasks are perceived as boring or uninteresting, extrinsic incentives can enhance motivation. "
                "However, when tasks are perceived as inherently interesting, the introduction of extrinsic incentives can backfire and lead to a decrease in motivation. [...] "
                "\"Pay Enough or Don't Pay At All\" [...] "
                "\"A Fine is a Price\".",
                nome="Uri Gneezy"),
            wiki("Motivation_crowding_theory",
                "the idea was first introduced into economics much earlier by Richard Titmuss, who argued in 1970 that offering financial incentives for certain behaviors could counter-intuitively lead to a drop in performance of those behaviors. "
                "While the empirical evidence supporting crowding out for blood donation has been mixed",
                nome="Motivation crowding theory"),
        ],
    },
    # 14 a regra do pico-fim: mais dor, melhor lembrança
    {
        "temas_secundarios": ["memoria", "emocoes"],
        "tipos_espanto": ["contraintuitivo"],
        "gancho": "Com a mão em água a 14 °C, as pessoas preferiram repetir 60 segundos seguidos de mais 30 com a água a 15 °C a repetir só os 60 segundos. A memória pesa o pior momento e o final, não a duração.",
        "explicacao": (
            "O estudo, de 1993, teve Daniel Kahneman entre os autores e um título provocador: \"Quando mais dor é "
            "preferível a menos: acrescentando um final melhor\". Numa tentativa, os participantes mantinham uma "
            "mão na água a 14 °C por 60 segundos. Na outra, usavam a outra mão pelos mesmos 60 segundos e mais 30, "
            "enquanto a temperatura subia para 15 °C. Depois, ao escolher qual repetir, mostraram-se mais dispostos "
            "a refazer a segunda, apesar de ela ter mais tempo de desconforto. É a \"regra do pico-fim\": julgamos "
            "uma experiência pelo seu momento mais intenso e pelo final. Em 1996, Kahneman e Donald Redelmeier "
            "viram o mesmo em pacientes de colonoscopia e de litotripsia, que avaliavam o incômodo pela pior dor e "
            "pela do fim, qualquer que fosse a duração. Num estudo seguinte, um grupo de pacientes teve o aparelho "
            "de colonoscopia deixado parado por três minutos a mais, o que incomodava sem doer. Esses pacientes "
            "lembraram o exame como menos desagradável e se mostraram muito mais dispostos a voltar. A regra tem "
            "críticos: um estudo de 2008 a achou um preditor apenas razoável da lembrança, e o momento mais "
            "memorável previu melhor do que o pico ou o fim."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "consenso_parcial",
        "fontes": [wiki("Peak%E2%80%93end_rule",
            "A 1993 study titled \"When More Pain Is Preferred to Less: Adding a Better End\" by Kahneman, Fredrickson, Charles Schreiber, and Donald Redelmeier provided groundbreaking evidence for the peak–end rule. [...] "
            "The first trial had subjects submerge a hand in 14 °C water for 60 seconds. "
            "The second trial had subjects submerge the other hand in 14 °C water for 60 seconds, but then keep their hand submerged for an additional 30 seconds, during which the temperature was raised to 15 °C. "
            "Subjects were then offered the option of which trial to repeat. "
            "Against the law of temporal monotonicity, subjects were more willing to repeat the second trial, despite a prolonged exposure to uncomfortable temperatures. [...] "
            "a 1996 study by Kahneman and Redelmeier assessed patients' appraisals of uncomfortable colonoscopy or lithotripsy procedures [...] "
            "They found that patients consistently evaluated the discomfort of the experience based on the intensity of pain at the worst (peak) and final (end) moments. "
            "This occurred regardless of length or variation in intensity of pain within the procedure. [...] "
            "One underwent a colonoscopy procedure wherein the scope was left in for three extra minutes, but not moved, creating a sensation that was uncomfortable, but not painful. [...] "
            "patients who underwent the longer procedure rated their experience as less unpleasant than patients who underwent the typical procedure. "
            "Moreover, the patients in the prolonged discomfort group were far more likely to return for subsequent procedures [...] "
            "A 2008 study found some support for the peak–end rule, but also found that it was \"not an outstandingly good predictor\" of remembered experiential value, and that the happiness of the most memorable part of an experience predicted remembered happiness better than did the happiness of the peak or of the end.",
            nome="Peak–end rule")],
    },
    # 15 a maldição do vencedor nasceu no petróleo
    {
        "temas_secundarios": ["teoria_jogos", "energia"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "A \"maldição do vencedor\" ganhou nome num artigo de três engenheiros de petróleo, em 1971: nos leilões de áreas no mar, quem vence tende a ser quem mais superestimou o óleo. Ganhar é má notícia.",
        "explicacao": (
            "Os três engenheiros, da Atlantic Richfield, afirmaram que as petroleiras tinham retornos "
            "inesperadamente baixos, \"ano após ano\", nos primeiros leilões de áreas da plataforma continental "
            "dos EUA. O artigo saiu numa revista técnica do setor, o Journal of Petroleum Technology. O mecanismo é "
            "simples. Nesses leilões, o petróleo no subsolo vale praticamente o mesmo para qualquer concorrente, e "
            "cada um só tem a própria estimativa desse valor. Nos anos 1950, não havia método preciso para avaliar "
            "um campo submarino: se um campo valia de fato 10 milhões de dólares, as estimativas podiam ir de 5 a "
            "20 milhões. A empresa que errava para cima e lançava 20 milhões levava a área, para depois descobrir "
            "que ela valia menos. Se a média das estimativas está certa, quem dá o maior lance é justamente quem "
            "mais exagerou. E quanto mais concorrentes, pior a maldição, porque aumenta a chance de alguém "
            "superestimar o valor. Os licitantes espertos se defendem dando lances abaixo da própria estimativa, já "
            "contando com o fato de que vencer significa ter sido o mais otimista. A maldição não vale para tudo: "
            "num leilão de algo que a pessoa quer para si, sem pensar no valor de mercado, ela não aparece."
        ),
        "nivel": 2, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Winner%27s_curse",
            "wherein the winner is the bidder with the most optimistic evaluation of the asset and therefore will tend to overestimate and overpay. [...] "
            "The winner's curse phenomenon was first addressed in 1971 by three Atlantic Richfield petroleum engineers who claimed that oil companies suffered unexpectedly low returns \"year after year\" in early Outer Continental Shelf oil lease auctions. "
            "Outer Continental Shelf auctions are common value auctions, where the value of the oil in the ground is essentially the same to all bidders. [...] "
            "Each player independently estimates the value of the item before bidding. [...] "
            "If we assume that the average bid is accurate, then the highest bidder overestimates the item's value. [...] "
            "Savvy bidders will avoid the winner's curse by bid shading, or placing a bid that is below their ex ante estimation of the value of the item for sale [...] "
            "The key point is that winning the auction is bad news about the value of the item for the winner. "
            "It means that he or she was the most optimistic [...] "
            "The severity of the winner's curse increases with the number of bidders. "
            "This is because the more bidders, the more likely it is that some of them have overestimated the auctioned item's value. [...] "
            "for auctions with private value (i.e. when the item is desired independently of its value in the market), winner's curse does not arise. [...] "
            "In the 1950s, when the term winner's curse was first coined, there was no accurate method to estimate the potential value of an offshore oil field. "
            "So if, for example, an oil field had an actual intrinsic value of $10 million, oil companies might guess its value to be anywhere from $5 million to $20 million. "
            "The company who wrongly estimated at $20 million and placed a bid at that level would win the auction, and later find that it was not worth as much. [...] "
            "the term winner's curse was originated in a paper published in the Journal of Petroleum Technology, volume 23, 1971",
            nome="Winner's curse")],
    },
]
