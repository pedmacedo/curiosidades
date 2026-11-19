LOTE = "2026-11-17-teoria_numeros-01"
AREA = "matematica"
TEMA = "teoria_numeros"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = W if idioma == "en" else "https://pt.wikipedia.org/wiki/"
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o táxi 1729
    {
        "temas_secundarios": ["personagens_esquecidos", "historia_matematica"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Um matemático comentou que o número do seu táxi, 1729, era sem graça. O colega indiano, doente na cama, respondeu na hora que era um número muito interessante.",
        "explicacao": (
            "Por volta de 1919, o matemático inglês G. H. Hardy foi visitar Srinivasa Ramanujan, que estava doente "
            "em Putney, perto de Londres. Hardy contou depois que tinha ido no táxi de número 1729 e comentou que o "
            "número parecia bem sem graça, e que esperava que não fosse um mau presságio. \"Não\", respondeu "
            "Ramanujan, \"é um número muito interessante: é o menor número que pode ser escrito como soma de dois "
            "cubos de duas maneiras diferentes.\" De fato, 1729 é 1³ + 12³ e também 9³ + 10³. Por causa da "
            "história, números com essa propriedade passaram a ser chamados de números de táxi, e 1729 ganhou o "
            "apelido de número de Hardy-Ramanujan. Ramanujan não foi o primeiro a notar o fato: as duas somas já "
            "tinham sido publicadas em 1657 pelo francês Bernard Frénicle de Bessy. Mas foi a resposta instantânea, "
            "dada da cama, que fez de 1729 o número mais famoso da matemática recreativa."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Taxicab_number",
                "also known as the Hardy–Ramanujan number. The name is derived from a conversation ca. 1919 involving mathematicians G. H. Hardy and Srinivasa Ramanujan. As told by Hardy: "
                "I remember once going to see him [Ramanujan] when he was lying ill at Putney. I had ridden in taxi-cab No. 1729, and remarked that the number seemed to be rather a dull one, and that I hoped it was not an unfavourable omen. "
                "\"No,\" he replied, \"it is a very interesting number; it is the smallest number expressible as the sum of two cubes in two different ways.\" [...] "
                "The pairs of summands of the Hardy–Ramanujan number Ta(2) = 1729 were first mentioned by Bernard Frénicle de Bessy, who published his observation in 1657.",
                nome="Taxicab number"),
            wiki("1729_(number)",
                "It is the first nontrivial taxicab number, expressed as the sum of two cubic positive integers in two different ways.",
                nome="1729 (number)"),
        ],
    },
    # 2 o maior primo conhecido
    {
        "temas_secundarios": ["historia_computacao", "algoritmos"],
        "tipos_espanto": ["escala_absurda", "historia_humana"],
        "gancho": "O maior número primo conhecido tem mais de 41 milhões de algarismos. Foi achado em 2024 por um ex-funcionário da Nvidia que gastou cerca de US$ 2 milhões em placas de vídeo.",
        "explicacao": (
            "Um número primo só é divisível por 1 e por ele mesmo, e Euclides já provou que eles nunca acabam. Mas "
            "achar primos enormes é difícil. O recorde atual é 2 elevado a 136.279.841, menos 1, um número que tem "
            "41.024.320 algarismos. Ele foi encontrado em 12 de outubro de 2024 por Luke Durant, um pesquisador da "
            "Califórnia e ex-funcionário da Nvidia, que participava da GIMPS, uma busca coletiva de primos pela "
            "internet. Durant passou cerca de um ano e gastou uns 2 milhões de dólares montando uma rede de "
            "milhares de placas gráficas na nuvem. Foi a primeira vez que um primo desse tipo, chamado primo de "
            "Mersenne, foi achado com placas de vídeo em vez de processadores comuns: os anteriores tinham sido "
            "encontrados em computadores pessoais. Os 18 últimos recordes foram todos primos de Mersenne. E, ao "
            "contrário do que se costuma dizer, achar primos cada vez maiores não ajuda a criar criptografia mais "
            "forte."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Largest_known_prime_number",
            "a number that has 41,024,320 digits when written in the decimal system. "
            "It was found on October 12, 2024, on a cloud-based virtual machine volunteered by Luke Durant, a researcher from San Jose, California, to the Great Internet Mersenne Prime Search (GIMPS). "
            "A prime number is a natural number greater than 1 with no divisors other than 1 and itself. "
            "Euclid's theorem proves that for any given prime number, there will always be a higher one [...] "
            "The last 18 record primes were Mersenne primes. [...] "
            "Finding larger prime numbers is sometimes presented as a means to stronger encryption, but this is not true. [...] "
            "They were found on ordinary personal computers until the most recent one, found by ex-Nvidia employee Luke Durant using a network of thousands of dedicated graphics processing units (GPUs). "
            "Durant spent about a year and $2 million on the hunt. "
            "This is the first time a Mersenne prime has been discovered using GPUs instead of central processing units (CPUs).",
            nome="Largest known prime number")],
    },
    # 3 cigarras e números primos
    {
        "temas_secundarios": ["insetos", "evolucao"],
        "tipos_espanto": ["conexao_inesperada", "misterio_aberto"],
        "gancho": "Certas cigarras passam 13 ou 17 anos debaixo da terra antes de sair, todas juntas. Uma hipótese: ciclos de anos primos dificultam a vida dos predadores.",
        "explicacao": (
            "As cigarras periódicas da América do Norte passam cerca de 99,5% da vida debaixo da terra, como "
            "ninfas, sugando a seiva das raízes das árvores. Na primavera do 13º ou do 17º ano, saem todas ao "
            "mesmo tempo. A emergência em massa já é uma defesa: aparecem tantos insetos que os predadores não "
            "conseguem comer todos. Mas por que 13 e 17, dois números primos? Uma hipótese diz que ciclos primos "
            "ajudam a escapar de predadores com ciclos de vida mais curtos. Um predador que se reproduz a cada "
            "três anos, por exemplo, e que se fartou numa emergência, estará fora de sincronia na próxima: terá "
            "passado por quatro ciclos mais um ano (12 + 1) ou cinco ciclos mais dois anos (15 + 2). Com um número "
            "primo, as cigarras raramente coincidem com o pico de um predador periódico. É uma hipótese, e não a "
            "única explicação proposta para esses ciclos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "hipotese",
        "fontes": [wiki("Periodical_cicadas",
            "Magicicada species spend around 99.5% of their lives underground in an immature state called a nymph. "
            "While underground, the nymphs feed on xylem fluids from the roots of broadleaf forest trees in the eastern United States. "
            "In the spring of their 13th or 17th year, mature cicada nymphs emerge [...] "
            "there are after synchronized emergence simply too many individuals for the predators to consume; many individuals thus remain behind to procreate. "
            "It has been hypothesized that the prime-number development times (13 and 17 years) improve avoidance of predators with shorter reproductive cycles and for this reason have been selected for. "
            "A predator with, for example, a three-year reproductive cycle, which happened to benefit from a brood emergence in a given year, will have gone through either four cycles plus one year (12 + 1) or five cycles plus two years (15 + 2) by the next time that the same brood emerges.",
            nome="Periodical cicadas")],
    },
    # 4 o zero
    {
        "temas_secundarios": ["primeiras_civilizacoes", "historia_matematica", "mundo_islamico_medieval"],
        "tipos_espanto": ["origem_inesperada", "contraintuitivo"],
        "gancho": "Os babilônios tinham um sistema numérico sofisticado e nenhum zero: 1, 60 e 3.600 eram escritos do mesmo jeito. O zero como número veio da Índia.",
        "explicacao": (
            "Por volta da metade do 2º milênio antes de Cristo, os babilônios usavam um sistema posicional de base "
            "60, sofisticado para a época. Mas, para indicar uma casa vazia, deixavam só um espaço entre os "
            "algarismos. Mais tarde, escribas passaram a usar sinais para marcar o lugar: numa tábua achada em "
            "Kish, de até 700 antes de Cristo, são três ganchos; por volta de 300 antes de Cristo, duas cunhas "
            "inclinadas. Esses sinais nunca eram usados sozinhos nem no fim de um número, e por isso não "
            "representavam o conceito de zero. Na prática, 1, 60 e 60 vezes 60 eram escritos da mesma forma. O zero "
            "como número de verdade veio da matemática indiana. No século VII, o astrônomo Brahmagupta escreveu "
            "regras para operar com ele, como a de que zero mais zero é zero, e errou ao tentar descrever a "
            "divisão por zero. A ideia chegou à Europa por meio de matemáticos islâmicos medievais e foi "
            "popularizada por Fibonacci. Os maias também chegaram ao zero, de forma independente."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("0",
            "By the middle of the 2nd millennium BC, Babylonian mathematics had a sophisticated base 60 positional numeral system, but a positional value of zero was indicated by a space between numerals. "
            "In a tablet unearthed at Kish (dating to as early as 700 BC), the scribe Bêl-bân-aplu used three hooks as a placeholder. "
            "By 300 BC, a punctuation symbol (two slanted wedges) was repurposed as a placeholder. "
            "Significantly, however, these placeholder signs were not considered a numerical value, they were never used alone [...] "
            "They were also not written at the end of a number (so 1 and 60 and 60×60 were all written as ). [...] "
            "This use of zero derives from Indian mathematics, which was transmitted to Europe by medieval Islamic mathematicians and popularized by Fibonacci. "
            "It was independently used by the Maya civilization. [...] "
            "Rules governing the use of zero appeared in Brahmagupta's Brahmasputha Siddhanta (7th century), which states the sum of zero with itself as zero, and incorrectly describes division by zero",
            nome="0 (número)")],
    },
    # 5 lei de Benford
    {
        "temas_secundarios": ["probabilidade", "leis_julgamentos", "economia_curiosa"],
        "tipos_espanto": ["contraintuitivo", "historia_humana"],
        "gancho": "Em muitos conjuntos de números reais, o algarismo 1 aparece na frente em cerca de 30% dos casos, e o 9 em menos de 5%. O padrão ajuda a detectar fraudes.",
        "explicacao": (
            "Seria natural imaginar que, numa lista de números da vida real, cada algarismo de 1 a 9 apareceria na "
            "primeira posição com a mesma frequência, cerca de 11,1% das vezes. Em muitos conjuntos de dados não é "
            "assim: o 1 lidera em cerca de 30% dos casos, e o 9 aparece na frente em menos de 5%. É a lei de "
            "Benford, e ela surge quando os valores se espalham de maneira uniforme numa escala logarítmica. A "
            "descoberta começou com um detalhe curioso. Em 1881, o astrônomo Simon Newcomb notou que, nas tabelas "
            "de logaritmos, as primeiras páginas, com números começados por 1, estavam muito mais gastas que as "
            "outras. O físico Frank Benford voltou ao assunto em 1938, e a lei ficou com o nome dele. Como dados "
            "inventados costumam fugir desse padrão, a lei de Benford é usada em auditoria forense e na detecção "
            "de fraudes, inclusive em dados eleitorais, embora esse uso eleitoral seja polêmico."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Benford's_law",
            "is an observation that in many real-life sets of numerical data, the leading digit is likely to be small. "
            "In sets that obey the law, the number 1 appears as the leading significant digit about 30% of the time, while 9 appears as the leading significant digit less than 5% of the time. "
            "Uniformly distributed digits would each occur about 11.1% of the time. [...] "
            "Benford's law may be derived by assuming the dataset values are uniformly distributed on a logarithmic scale. [...] "
            "The law is named after physicist Frank Benford, who stated it in 1938 in an article titled \"The Law of Anomalous Numbers\", although it had been previously stated by Simon Newcomb in 1881. [...] "
            "The discovery of Benford's law goes back to 1881, when the Canadian-American astronomer Simon Newcomb noticed that in logarithm tables the earlier pages (that started with 1) were much more worn than the other pages. [...] "
            "argued that Benford's law is problematic and misleading as a statistical indicator of election fraud. [...] "
            "Benford's law has also been applied for forensic auditing and fraud detection",
            nome="Benford's law")],
    },
    # 6 o último teorema de Fermat
    {
        "temas_secundarios": ["historia_matematica"],
        "tipos_espanto": ["historia_humana", "escala_absurda"],
        "gancho": "Fermat anotou na margem de um livro que tinha uma prova \"maravilhosa\" que não cabia ali. A prova de verdade levou 358 anos e centenas de páginas.",
        "explicacao": (
            "Por volta de 1637, o francês Pierre de Fermat escreveu na margem de um exemplar da Aritmética, de "
            "Diofanto, que não existem números inteiros positivos a, b e c tais que a elevado a n mais b elevado a "
            "n seja igual a c elevado a n, para n maior que 2. E acrescentou: \"descobri uma prova "
            "verdadeiramente maravilhosa disso, que esta margem é estreita demais para conter\". Outras afirmações "
            "de Fermat foram provadas, mas essa resistiu, e muitos passaram a duvidar que ele tivesse uma prova "
            "correta. Depois de 358 anos de tentativas, o inglês Andrew Wiles anunciou a solução. Ele trabalhou em "
            "segredo por seis anos e, em 1993, apresentou a prova, num artigo enorme. Na revisão, acharam uma "
            "falha em uma parte, e Wiles levou mais um ano, com a ajuda do ex-aluno Richard Taylor, para "
            "consertá-la. A prova completa saiu em 1994 e foi publicada em 1995."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Fermat's_Last_Theorem",
            "The proposition was first stated as a theorem by Pierre de Fermat around 1637 in the margin of a copy of Arithmetica. "
            "Fermat wrote that \"I have discovered a truly marvelous proof of this, which this margin is too narrow to contain.\" [...] "
            "Fermat's Last Theorem resisted proof, leading to doubt that Fermat ever had a correct proof. [...] "
            "After 358 years of effort by mathematicians, the first successful proof was released in 1994 by Andrew Wiles and formally published in 1995. [...] "
            "In 1993, after six years of working secretly on the problem, Wiles succeeded in proving enough of the conjecture to prove Fermat's Last Theorem. "
            "Wiles's paper was massive in size and scope. "
            "A flaw was discovered in one part of his original paper during peer review and required a further year and collaboration with a past student, Richard Taylor, to resolve.",
            nome="Fermat's Last Theorem")],
    },
    # 7 Collatz
    {
        "temas_secundarios": ["paradoxos_logica", "algoritmos"],
        "tipos_espanto": ["misterio_aberto", "contraintuitivo"],
        "gancho": "Pegue um número: se for par, divida por 2; se for ímpar, multiplique por 3 e some 1. Repita. Ninguém conseguiu provar que sempre se chega a 1.",
        "explicacao": (
            "A conjectura de Collatz parece brincadeira de criança. Comece com qualquer número inteiro positivo. Se "
            "ele for par, o próximo é a metade. Se for ímpar, o próximo é o triplo mais 1. A conjectura diz que, "
            "repetindo isso, qualquer número inicial acaba chegando a 1. Os valores sobem e descem várias vezes "
            "antes disso, como granizo dentro de uma nuvem, e por isso a sequência também é chamada de números "
            "granizo. O alemão Lothar Collatz propôs a ideia em 1937. Computadores já conferiram todos os números "
            "até cerca de 2,36 sextilhões, e todos chegaram a 1. Mas isso não é prova, e a maioria dos matemáticos "
            "acredita que a conjectura seja verdadeira sem conseguir demonstrá-la. O húngaro Paul Erdős, um dos "
            "matemáticos mais produtivos da história, resumiu: \"A matemática talvez não esteja pronta para "
            "problemas assim.\""
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Collatz_conjecture",
            "The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1. "
            "It concerns sequences of integers in which each term is obtained from the previous term as follows: if a term is even, the next term is one half of it. "
            "If a term is odd, the next term is 3 times the previous term plus 1. "
            "The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence. [...] "
            "It is named after the mathematician Lothar Collatz, who introduced the idea in 1937 [...] "
            "is sometimes referred to as the hailstone sequence, hailstone numbers or hailstone numerals (because the values are usually subject to multiple descents and ascents like hailstones in a cloud) [...] "
            "Paul Erdős said about the Collatz conjecture: \"Mathematics may not be ready for such problems.\" [...] "
            "most mathematicians who have looked into the problem think the conjecture is true because experimental evidence and heuristic arguments support it. [...] "
            "The conjecture has been checked by computer for all starting values up to 271 ≈ 2.36×1021. All values tested so far converge to 1. "
            "This computer evidence is still not rigorous proof",
            nome="Collatz conjecture")],
    },
    # 8 pi: 39 casas bastam
    {
        "temas_secundarios": ["cosmologia", "historia_computacao"],
        "tipos_espanto": ["escala_absurda", "contraintuitivo"],
        "gancho": "Com só 39 casas decimais de pi, dá para calcular a circunferência do universo observável com erro menor que um átomo. Mesmo assim, já se calcularam centenas de trilhões.",
        "explicacao": (
            "Pi tem infinitas casas decimais, sem padrão aparente. Mas quantas são necessárias na prática? Segundo "
            "Jörg Arndt e Christoph Haenel, 39 dígitos bastam para a maioria dos cálculos da cosmologia, porque essa "
            "é a precisão necessária para calcular a circunferência do universo observável com erro de um átomo. "
            "Somando os dígitos extras para compensar erros de arredondamento, umas poucas centenas de casas "
            "dariam conta de qualquer aplicação científica. Mesmo assim, matemáticos e cientistas da computação "
            "já estenderam pi a centenas de trilhões de dígitos. Parte disso é a vontade humana de bater recordes, "
            "que costuma virar manchete. Mas há usos práticos: calcular pi serve para testar supercomputadores e "
            "algoritmos de multiplicação de alta precisão, e, na matemática pura, fornece dados para estudar se os "
            "dígitos de pi se distribuem ao acaso."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Pi",
            "According to Jörg Arndt and Christoph Haenel, thirty-nine digits are sufficient to perform most cosmological calculations, because that is the accuracy necessary to calculate the circumference of the observable universe with a precision of one atom. "
            "Accounting for additional digits needed to compensate for computational round-off errors, Arndt concludes that a few hundred digits would suffice for any scientific applicatio [...] "
            "mathematicians and computer scientists have extended the decimal representation of π to hundreds of trillions of digits. [...] "
            "This effort may be partly ascribed to the human compulsion to break records, and such achievements with π often make headlines around the world. "
            "They also have practical benefits, such as testing supercomputers, testing numerical analysis algorithms (including high-precision multiplication algorithms) – and within pure mathematics itself, providing data for evaluating the randomness of the dig [...] "
            "The digits of π have no apparent pattern")],
    },
    # 9 números perfeitos
    {
        "temas_secundarios": ["grecia_antiga", "religioes"],
        "tipos_espanto": ["misterio_aberto", "historia_humana"],
        "gancho": "Números perfeitos, como 6 e 28, são a soma dos próprios divisores. Os gregos já os estudavam, e até hoje ninguém sabe se existe algum ímpar.",
        "explicacao": (
            "Um número é perfeito quando é igual à soma dos seus divisores, sem contar ele mesmo: 6 = 1 + 2 + 3, e "
            "28 = 1 + 2 + 4 + 7 + 14. A definição é antiga e aparece nos Elementos de Euclides, que a chama de "
            "\"número perfeito\". Por volta de 300 antes de Cristo, Euclides mostrou uma regra para fabricá-los a "
            "partir de certos números primos, os primos de Mersenne. Dois mil anos depois, Leonhard Euler provou "
            "que todos os perfeitos pares seguem essa regra. A fama dos números perfeitos foi além da matemática: "
            "no início do século V, Santo Agostinho repetiu a ideia de que Deus criou o mundo em seis dias porque 6 "
            "é o menor número perfeito. Até hoje, duas perguntas simples continuam sem resposta: se existe algum "
            "número perfeito ímpar e se existem infinitos números perfeitos."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Perfect_number",
            "This definition is ancient, appearing as early as Euclid's Elements (Book VII, Definition 22) where it is called τέλειος ἀριθμός (téleios arithmós; 'perfect', 'ideal', or 'complete number'). [...] "
            "now called a Mersenne prime. Two millennia later, Leonhard Euler proved that all even perfect numbers are of this form. [...] "
            "It is not known whether there are any odd perfect numbers, nor whether infinitely many perfect numbers exist. [...] "
            "In about 300 BC Euclid showed that if 2p−1 is prime then 2p−1(2p−1) is perfect. [...] "
            "in the early 5th century AD, repeating the claim that God created the world in 6 days because 6 is the smallest perfect number.",
            nome="Perfect number")],
    },
    # 10 base 60
    {
        "temas_secundarios": ["primeiras_civilizacoes", "medidas_padroes", "calendarios"],
        "tipos_espanto": ["origem_inesperada", "engenhosidade"],
        "gancho": "Uma hora tem 60 minutos por causa dos sumérios: eles contavam em base 60 há mais de 4 mil anos. O 60 é ótimo para dividir, porque tem 12 divisores.",
        "explicacao": (
            "O sistema sexagesimal, de base 60, surgiu com os sumérios no 3º milênio antes de Cristo e passou para "
            "os babilônios. Ele sobrevive, com modificações, em três lugares do dia a dia: na medida do tempo, nos "
            "ângulos e nas coordenadas geográficas. Uma hora tem 60 minutos, e um minuto tem 60 segundos; um "
            "horário como 3:23:17 é, na prática, um número escrito em base 60. A vantagem do 60 é ter muitos "
            "divisores: são doze (1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30 e 60). Por isso muitas frações ficam simples. "
            "Uma hora pode ser dividida em partes iguais de 30, 20, 15, 12, 10, 6, 5, 4, 3, 2 ou 1 minuto. O 60 é "
            "também o menor número divisível por todos os números de 1 a 6."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Sexagesimal",
            "It originated with the ancient Sumerians in the 3rd millennium BC, was passed down to the ancient Babylonians, and is still used—in a modified form—for measuring time, angles, and geographic coordinates. "
            "The number 60, a superior highly composite number, has twelve divisors, namely 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, and 60 [...] "
            "With so many factors, many fractions involving sexagesimal numbers are simplified. "
            "For example, one hour can be divided evenly into sections of 30 minutes, 20 minutes, 15 minutes, 12 minutes, 10 minutes, 6 minutes, 5 minutes, 4 minutes, 3 minutes, 2 minutes, and 1 minute. "
            "60 is the smallest number that is divisible by every number from 1 to 6 [...] "
            "One hour of time is divided into 60 minutes, and one minute is divided into 60 seconds. "
            "Thus, a measurement of time such as 3:23:17 (3 hours, 23 minutes, and 17 seconds) can be interpreted as a whole sexagesimal number")],
    },
    # 11 Goldbach
    {
        "temas_secundarios": ["historia_matematica"],
        "tipos_espanto": ["misterio_aberto"],
        "gancho": "Todo número par maior que 2 parece ser a soma de dois primos: já se conferiu até 4 quintilhões. Mas ninguém prova isso desde uma carta de 1742.",
        "explicacao": (
            "A conjectura de Goldbach é um dos problemas sem solução mais antigos e conhecidos da matemática. Ela "
            "diz que todo número par maior que 2 é a soma de dois números primos: 4 = 2 + 2, 10 = 3 + 7, 100 = 47 "
            "+ 53, e assim por diante. Tudo começou em 7 de junho de 1742, quando o matemático prussiano Christian "
            "Goldbach escreveu uma carta a Leonhard Euler propondo uma versão da ideia. Desde então, a conjectura "
            "foi verificada para todos os números menores que 4 quintilhões (4 seguido de 18 zeros). Nenhuma "
            "exceção apareceu. Mesmo assim, ela continua sem prova, apesar de muito esforço, e verificar números, "
            "por mais que sejam, não basta para provar que vale para todos."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Goldbach's_conjecture",
            "Goldbach's conjecture is one of the oldest and best-known unsolved problems in number theory and all of mathematics. "
            "It states that every even natural number greater than 2 is the sum of two prime numbers. "
            "The conjecture has been shown to hold for all natural numbers less than 4×1018, but remains unproven despite considerable effort. [...] "
            "On 7 June 1742, the Prussian mathematician Christian Goldbach wrote a letter to Leonhard Euler (letter XLIII), in which he proposed the following conjecture",
            nome="Goldbach's conjecture")],
    },
]
