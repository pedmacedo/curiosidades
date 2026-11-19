LOTE = "2026-11-19-calendarios-01"
AREA = "sociedade"
TEMA = "calendarios"
W = "https://en.wikipedia.org/wiki/"


def wiki(titulo, trecho, nome=None, idioma="en"):
    base = {"en": W, "pt": "https://pt.wikipedia.org/wiki/"}[idioma]
    return {"url": base + titulo, "titulo": nome or titulo.replace("_", " "), "idioma": idioma, "trecho": trecho}


CANDIDATOS = [
    # 1 o calendário gregoriano nasceu da proposta de um médico
    {
        "temas_secundarios": ["historia_astronomia", "revolucao_cientifica"],
        "tipos_espanto": ["historia_humana", "engenhosidade"],
        "gancho": "O calendário que usamos saiu da proposta de um médico calabrês, Luigi Lilio. Ele queria tirar os 10 dias de atraso aos poucos, em quarenta anos, mas o papa preferiu o pulo: depois de 4 de outubro de 1582 veio o dia 15.",
        "explicacao": (
            "O calendário juliano supunha um ano de 365,25 dias, quase 11 minutos mais longo que o ano solar médio, "
            "e isso fazia as datas escorregarem cerca de três dias a cada 400 anos. Desde o Concílio de Niceia, em "
            "325, o equinócio de março tinha recuado 10 dias, para 10 ou 11 de março, o que bagunçava o cálculo da "
            "Páscoa. A reforma do papa Gregório XIII, oficializada por uma bula de fevereiro de 1582, partiu de uma "
            "proposta do médico calabrês Aloysius Lilius, ou Luigi Lilio. Ele sugeriu que, a cada quatro séculos, "
            "só 97 anos fossem bissextos, e não 100: os anos de virada de século só teriam 29 de fevereiro se "
            "fossem divisíveis por 400. Para recuperar os 10 dias perdidos, Lilio propôs suprimir o dia bissexto em "
            "dez ocasiões ao longo de quarenta anos. O matemático alemão Christopher Clavius, que ampliou o trabalho num "
            "volume de 800 páginas, achou melhor fazer a correção de uma vez, e foi esse o conselho que o papa "
            "seguiu. Nos domínios de Filipe II, que reinava sobre Espanha e Portugal, a quinta-feira 4 de outubro "
            "de 1582 foi seguida pela sexta-feira 15. As colônias espanholas e portuguesas só aderiram na prática um "
            "pouco depois, por causa da demora das comunicações. A França esperou alguns meses: lá, o 9 de dezembro "
            "foi seguido pelo dia 20."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Gregorian_calendar",
            "It was instituted by the papal bull Inter gravissimas dated 24 February 1582 by Pope Gregory XIII, after whom the calendar is named. [...] "
            "The reform adopted was a modification of a proposal made by the Calabrian doctor Aloysius Lilius (or Lilio). "
            "Lilius's proposal included reducing the number of leap years in four centuries from 100 to 97, by making three out of four centurial years common instead of leap years. [...] "
            "the Julian year is almost 11 minutes longer than the mean tropical year. The discrepancy results in a drift of about three days every 400 years. [...] "
            "At the time of Gregory's reform, there had already been a drift of 10 days since the Council of Nicaea, resulting in the vernal equinox falling on 10 or 11 March instead of the ecclesiastically fixed date of 21 March, and if unreformed it would have drifted further. "
            "Lilius proposed that the 10-day drift should be corrected by deleting the Julian leap day on each of its ten occurrences over a period of forty years, thereby providing for a gradual return of the equinox to 21 March. "
            "Lilius's work was expanded upon by Christopher Clavius in a closely argued, 800-page volume. He would later defend his and Lilius's work against detractors. "
            "Clavius's opinion was that the correction should take place in one move, and it was this advice that prevailed with Gregory. [...] "
            "The proposed rule was that \"years divisible by 100 would be leap years only if they were divisible by 400 as well\". [...] "
            "On 29 September 1582, Philip II of Spain decreed the change from the Julian to the Gregorian calendar. "
            "This affected much of Roman Catholic Europe, as Philip was at the time ruler over Spain and Portugal as well as much of Italy. "
            "In these territories, as well as in the Polish–Lithuanian Commonwealth and in the Papal States, the new calendar was implemented on the date specified by the bull, with Julian Thursday, 4 October 1582, being followed by Gregorian Friday, 15 October. "
            "The Spanish and Portuguese colonies followed somewhat later de facto because of delay in communication. "
            "The other major Catholic power of Western Europe, France, adopted the change a few months later: 9 December was followed by 20 December.",
            nome="Gregorian calendar"),
            wiki("Gregorian_calendar",
            "Ancient tables provided the Sun's mean longitude. The German mathematician Christopher Clavius, the architect of the Gregorian calendar, noted that the tables agreed neither on the time when the Sun passed through the vernal equinox nor on the length of the mean tropical year. [...] "
            "the Julian algorithm had caused the calendar to drift such that the March equinox was occurring well before its nominal 21 March date. This date was important to the Christian churches because it is fundamental to the calculation of the date of Easter. [...] "
            "The error in the Julian calendar (its assumption that there are exactly 365.25 days in a year) [...] "
            "Second, in the years since the First Council of Nicaea in AD 325, the excess leap days introduced by the Julian algorithm",
            nome="Gregorian calendar")],
    },
    # 2 o mito dos motins "devolvam nossos 11 dias"
    {
        "temas_secundarios": ["revolucao_industrial", "pintura"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "A história de que ingleses saíram às ruas gritando \"devolvam nossos 11 dias\" quando o calendário pulou de 2 para 14 de setembro de 1752 é, muito provavelmente, um mito. Ela nasceu de uma sátira e de um quadro.",
        "explicacao": (
            "Em 1752, a Grã-Bretanha e suas colônias adotaram, na prática, o calendário gregoriano, que boa parte da "
            "Europa já usava. Como o calendário juliano estava 11 dias atrasado, a lei mandou que a quarta-feira, 2 "
            "de setembro, fosse seguida pela quinta-feira, 14. Alguns livros de história contam que houve motins, "
            "com o povo exigindo de volta os dias \"roubados\". Só que não há registro desses tumultos nos "
            "depoimentos sobre motins guardados no arquivo público britânico. A lenda se apoia em apenas duas "
            "fontes: um periódico satírico de Lorde Chesterfield, justamente o político que apresentou o projeto na "
            "Câmara dos Lordes, e um quadro do satirista William Hogarth. A pintura, de 1755, inspirada numa eleição "
            "muito disputada em Oxfordshire, mostra no chão um cartaz com o slogan \"Give us our Eleven Days\". Na "
            "campanha, a oposição atacava os adversários por todo tipo de assunto, inclusive o calendário "
            "\"papista\". O cartaz de Hogarth fazia parte da sátira sobre o tom do debate, não era o retrato de uma "
            "multidão real. Preocupações práticas existiram, sim: para que ninguém pagasse antes da hora, a lei "
            "adiou em 11 dias o vencimento de aluguéis e outras dívidas."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Calendar_(New_Style)_Act_1750",
            "The Julian calendar was eleven days behind this 'New Style' calendar. With this Act, therefore, Britain implicitly adopted the Gregorian calendar. [...] "
            "Section I of the act corrects this divergence by providing that Wednesday, 2 September 1752 be followed by Thursday, 14 September 1752. [...] "
            "Some history books report rioting in reaction to the calendar change, with people demanding that their 'eleven days' be returned. "
            "However, this is very likely a myth, based on just two primary sources—The World, a satirical journal of Lord Chesterfield, and An Election Entertainment, a painting by the satirist William Hogarth. "
            "There are no contemporary records of any such events in the riot depositions at the Public Record Office. "
            "This is the same Lord Chesterfield who introduced the Bill to the House of Lords. [...] "
            "In 1755, Hogarth produced a painting (and an engraved print from the painting) loosely based on these elections, entitled An Election Entertainment, which shows a placard carrying the slogan \"Give us our Eleven Days\" (on the floor, lower right). [...] "
            "The election campaign depicted concluded in 1754, after a very lengthy contest between Court Whigs and Jacobite Tories. "
            "Every issue between the two factions was brought up, including the question of calendar reform. "
            "The Tories attacked the Whigs for every deviation, including their alleged favouritism towards foreign Jews and the 'Popish' calendar. "
            "Hogarth's placard, part of a satire on the character of the debate, was not an observation of actual crowd behaviour. [...] "
            "For example, Section VI, echoing a rule in Gregory's reform, provides that the date on which rents and other debts are due must be deferred by 11 days.",
            nome="Calendar (New Style) Act 1750"),
            wiki("Calendar_(New_Style)_Act_1750",
            "When the son of the Earl of Macclesfield (who had been influential in passing the act) stood for Parliament in Oxfordshire as a Whig in 1754, dissatisfaction with the calendar reform was one of a number of issues raised by his Tory opponents.",
            nome="Calendar (New Style) Act 1750")],
    },
    # 3 o ano fiscal britânico começa em 6 de abril
    {
        "temas_secundarios": ["economia_curiosa", "dinheiro"],
        "tipos_espanto": ["origem_inesperada", "conexao_inesperada"],
        "gancho": "O ano do imposto de renda britânico começa em 6 de abril por causa de uma troca de calendário de 1752, feita quando o ano inglês ainda virava em 25 de março, e não em 1º de janeiro.",
        "explicacao": (
            "Durante séculos, o ano legal inglês, usado em documentos, contratos e finanças, começou em 25 de março, "
            "o Lady Day. Assim, o dia seguinte a 24 de março de 1707 era 25 de março de 1708. A lei de 1750 que "
            "levou a Grã-Bretanha ao calendário gregoriano também mudou o início do ano para 1º de janeiro e "
            "suprimiu 11 dias de setembro de 1752. Para que ninguém ganhasse ou perdesse com o corte, as datas "
            "civis, como os dias de pagar aluguel, receber salário ou fechar contratos de trabalho, foram empurradas "
            "11 dias para a frente. O ano fiscal terminava em 25 de março, o dia tradicional de acertar as dívidas, "
            "e no novo calendário essa data equivalia a 5 de abril, enquanto o 26 de março virou 6 de abril. Daí "
            "vem o calendário fiscal das pessoas físicas no Reino Unido, que vai de 6 de abril a 5 de abril do ano "
            "seguinte. A mudança mexeu até com aniversários: George Washington nasceu em 11 de fevereiro de 1731 "
            "pelo calendário antigo, data hoje registrada oficialmente como 22 de fevereiro de 1732. Mudaram o dia e "
            "também o ano."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Calendar_(New_Style)_Act_1750",
                "The act also changed the start of the legal year from 25 March to 1 January. "
                "The act elided eleven days from September 1752. [...] "
                "It ordered that civil and market days  – for example the quarter days on which rent was due, salaries paid and new labour contracts agreed –  be moved forward in the calendar by eleven days so that no-one should gain or lose by the change [...] "
                "By the 18th century, the English legal year –  used for legal, financial and other civil purposes –  had for centuries begun on 25 March, or Lady Day. "
                "Thus, for example, 24 March 1707 was immediately followed by 25 March 1708",
                nome="Calendar (New Style) Act 1750"),
            wiki("Fiscal_year",
                "United Kingdom: the tax year for individuals begins on 6 April. "
                "This is due to Britain historically having a calendar year starting on Lady Day (25 March) in the Julian calendar but a fiscal year ending on that day. "
                "When the UK adopted the Gregorian calendar in 1752, 25 March translated to 5 April and 26 March to 6 April. [...] "
                "For personal tax purposes the fiscal year starts on 6 April and ends on 5 April of the next calendar year. [...] "
                "The difference between the two dates is accounted for by the eleven days omitted in September 1752 due to the Calendar (New Style) Act 1750 [...] "
                "However, although the calendar year finished on 24 March, the tax year finished a day later, on 25 March, the Quarter Day – the traditional day on which debts were settled.",
                nome="Fiscal year"),
            wiki("Old_Style_and_New_Style_dates",
                "George Washington is now officially reported as having been born on 22 February 1732, rather than on 11 February 1731/32 (Julian calendar).",
                nome="Old Style and New Style dates"),
        ],
    },
    # 4 o 30 de fevereiro sueco
    {
        "temas_secundarios": ["europa_medieval", "teoria_numeros"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1712, a Suécia teve um 30 de fevereiro. O país tentou chegar ao calendário gregoriano aos poucos, pulando dias bissextos, mas uma guerra travou o plano e o rei mandou desfazer tudo.",
        "explicacao": (
            "Em novembro de 1699, o governo sueco decidiu que não trocaria de calendário de uma vez, como outros "
            "países: a ideia era omitir os dias bissextos seguidos até alcançar o gregoriano. O dia bissexto de "
            "1700 foi suprimido, mas a Grande Guerra do Norte impediu os ajustes seguintes. Resultado: a Suécia, "
            "que então incluía a Finlândia, e seus domínios no Báltico passaram a usar um calendário só deles, um "
            "dia à frente do juliano e dez dias atrás do gregoriano. Em janeiro de 1711, escrevendo de seu "
            "acampamento em Bender, na atual Moldávia, o rei Carlos XII ordenou abandonar o experimento e voltar "
            "ao juliano. Para devolver o dia cortado em 1700, mandou acrescentar um dia extra no bissexto seguinte. "
            "Assim, fevereiro de 1712 teve 30 dias, e o ano, 367. A bagunça chegou à Páscoa: em 1709, os suecos a "
            "celebraram numa data que nenhum outro calendário usava, quatro semanas depois da Páscoa gregoriana e "
            "uma antes da juliana. A Suécia só adotou o calendário gregoriano em 1753, depois da Grã-Bretanha, e "
            "dessa vez de uma tacada: ao 17 de fevereiro seguiu-se o 1º de março."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Swedish_calendar",
            "The Swedish calendar (Swedish: svenska kalendern) or Swedish Style (svenska stilen) was a calendar in use in Sweden and its eastern Baltic dominions from 1 March 1700 until 30 February 1712. "
            "It was one day ahead of the Julian calendar and ten days behind the Gregorian calendar. [...] "
            "In November 1699, the Government of Sweden decided that, rather than adopt the Gregorian calendar outright, it would do so gradually. "
            "The leap day was omitted in 1700, but the Great Northern War stopped any further adjustments from being made in the following years. "
            "In January 1711, writing from his camp in Bender (in present-day Moldova), King Charles XII ordered the abandonment of the isolated Swedish calendar and return to the Julian calendar. "
            "The king's letter claims that the original intention had been to continually omit successive leap days until alignment with the New Style was reached. "
            "To reverse the 1700 omission and realign with the Old Style, the king ordered an extra day to be added to the next leap year. "
            "An extra day was added to February in the leap year of 1712, thus giving the month a unique 30-day (30 February) and the year a 367-day length. "
            "The Swedish calendar was used in Sweden, which then included Finland, as well as its dominions in the eastern Baltic [...] "
            "Great Britain, its colonies and Ireland introduced the Gregorian calendar in 1752, and Sweden followed suit in 1753. "
            "In Sweden, the leap of 11 days was accomplished in one step, with 17 February being followed by 1 March. [...] "
            "As a result, in 1709, Sweden celebrated Easter on a unique date: four weeks after the Gregorian Easter and one week before the Julian Easter.",
            nome="Swedish calendar")],
    },
    # 5 a semana soviética de cinco dias coloridos
    {
        "temas_secundarios": ["guerra_fria", "revolucao_industrial"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Em 1929, a URSS criou semanas de cinco dias, cada um com uma cor. Cada trabalhador folgava no dia da sua cor, para as fábricas nunca pararem. Casais com cores diferentes ficavam sem um dia livre em comum.",
        "explicacao": (
            "A ideia, chamada nepreryvka, ou semana contínua, foi apresentada por Yuri Larin em maio de 1929 e quase "
            "ninguém deu atenção, até ganhar o apoio de Stalin no mês seguinte. O raciocínio era simples: "
            "trabalhadores precisam de descanso, máquinas não. Com folgas escalonadas, as fábricas funcionariam todo "
            "dia e produziriam mais. De quebra, domingos e feriados religiosos viravam dias de trabalho, o que "
            "agradava à campanha antirreligiosa. Cada dia da semana de cinco dias levava uma de cinco cores ou um "
            "numeral romano de I a V, e cada trabalhador recebia a cor ou o número da sua folga. Assim, em cada "
            "fábrica, oito em cada dez pessoas trabalhavam todo dia e duas descansavam. Para todo o resto, valiam o calendário "
            "gregoriano e a semana de sete dias. Os problemas vieram logo. Maridos, esposas, parentes e amigos com "
            "cores diferentes não tinham um dia de descanso juntos. As máquinas quebravam mais, porque eram usadas "
            "por quem não as conhecia e nunca paravam para manutenção. Em 1931, Stalin condenou a semana contínua, e "
            "a maioria das fábricas passou a uma semana de seis dias com folga comum. A semana de sete dias, com "
            "descanso no domingo, só voltou em 27 de junho de 1940."
        ),
        "nivel": 1, "nota_surpresa": 5, "confianca": "alta",
        "fontes": [wiki("Soviet_calendar",
            "During the summer of 1929, five-day continuous work weeks were implemented in factories, government offices, and commercial enterprises, but not collective farms. [...] "
            "While the five-day week was used for scheduling work, the Gregorian calendar and its seven-day week were used for all other purposes. [...] "
            "During the second half of May 1929, Yuri Larin  proposed a continuous production week (nepreryvnaya rabochaya nedelya = nepreryvka) to the Fifth Congress of Soviets of the Union, but so little attention was paid to his suggestion that the president of the Congress did not even mention it in his final speech. "
            "By the beginning of June 1929, Larin had won the approval of Joseph Stalin, prompting all newspapers to praise the idea. "
            "The rationale was that while workers needed rest, machines did not; therefore, scheduling workers' days off in such a way as to maintain factories constantly in operation would make it possible to produce more for less time. "
            "In addition, the change was advantageous to the anti-religious movement, as Sundays and religious holidays became working days. [...] "
            "On 23 June 1931, Stalin condemned the continuous work week as then practiced, supporting the temporary use of the interrupted six-day week (one common rest day for all workers) until the problems with the continuous work week could be resolved. "
            "During August 1931, most factories were put on an interrupted six-day week [...] "
            "Due to a decree dated 26 June 1940, the traditional interrupted seven-day week with Sunday as the common day of rest was reintroduced on 27 June 1940. [...] "
            "Each day of the five-day week was labeled by either one of five colors or a Roman numeral from I to V. "
            "Each worker was assigned a color or number to identify his or her day of rest. "
            "Eighty percent of each factory's workforce was at work every day (except holidays) in an attempt to increase production while 20% were resting. "
            "But when spouses, and their relatives and friends, were assigned different colors or numbers, they did not have a common rest day for their family and social life. "
            "Furthermore, machines broke down more frequently both because they were used by workers not familiar with them, and because no maintenance could be performed on machines that were never idle",
            nome="Soviet calendar")],
    },
    # 6 Samoa: um dia repetido e um dia apagado
    {
        "temas_secundarios": ["fronteiras_paises", "comercio_rotas"],
        "tipos_espanto": ["historia_humana", "contraintuitivo"],
        "gancho": "Samoa já viveu o mesmo dia duas vezes e já pulou um dia inteiro. Em 1892, repetiu o 4 de julho para ficar com a data dos EUA. Em 2011, apagou o 30 de dezembro para ficar com a da Austrália.",
        "explicacao": (
            "A linha internacional de data não é fixada por nenhum tratado entre países, e cada um escolhe de que "
            "lado dela quer ficar. Até 1892, as ilhas Samoa usavam a data asiática, a oeste da linha. Naquele ano, "
            "comerciantes americanos convenceram o rei Malietoa Laupepa a adotar a data americana, e a troca foi "
            "feita repetindo a segunda-feira, 4 de julho de 1892, justamente o Dia da Independência dos EUA. Mais de "
            "um século depois, Austrália e Nova Zelândia tinham virado os maiores parceiros comerciais do país, além "
            "de abrigar grandes comunidades de expatriados. Estar 21 horas atrás deles atrapalhava os negócios: com "
            "os fins de semana desencontrados, só quatro dias úteis por semana eram comuns aos dois lados. Então, ao "
            "fim da quinta-feira, 29 de dezembro de 2011, Samoa passou direto para o sábado, 31, e trocou o fuso "
            "UTC−11 pelo UTC+13. A linha agora passa entre Samoa e a Samoa Americana, que continua do lado "
            "americano e um dia atrás. Por isso, os cristãos de Samoa celebram o Natal um dia antes dos vizinhos. "
            "Desde então, Samoa está entre os primeiros lugares do planeta a ver cada novo dia."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("International_Date_Line",
                "The Samoan Islands, now divided into Samoa and American Samoa, were on the west side of the IDL until 1892. "
                "In that year, King Mālietoa Laupepa was persuaded by American traders to adopt the American date (three hours behind California) to replace the former Asian date (four hours ahead of Japan). "
                "The change was made by repeating Monday, 4 July 1892, American Independence Day. "
                "In 2011, Samoa returned to the west side of the IDL by removing Friday, 30 December 2011 from its calendar. "
                "This changed the time zone from UTC−11:00 to UTC+13:00 (UTC−10 to UTC+14 DST). "
                "Samoa made the change because Australia and New Zealand have become its biggest trading partners, and also have large communities of expatriates. "
                "Being 21 hours behind made business difficult because having weekends on backward days meant only four days of the week were shared workdays. "
                "The IDL now passes between Samoa and American Samoa, which remains on the east (American) side of the line. [...] "
                "No international organization, nor any treaty between nations, has fixed the IDL drawn by cartographers [...] "
                "Thus, whether it is Western Christmas or Orthodox Christmas, Christians in Samoa, immediately west of the IDL, will celebrate the holiday a day before Christians in American Samoa, which is immediately east of the IDL. [...] "
                "American Samoa, the Cook Islands, Niue, and French Polynesia are east of the IDL and one day behind.",
                nome="International Date Line"),
            wiki("Time_in_Samoa",
                "As it is located just west of the International Date Line, Samoa is among the first places on Earth to see each new day [...] "
                "At the end of Thursday, 29 December 2011, Samoa continued directly to Saturday, 31 December 2011, skipping the entire calendar day of Friday, 30 December 2011 and effectively redrawing the International Date Line.",
                nome="Time in Samoa"),
        ],
    },
    # 7 a Páscoa segue uma lua de tabela e só se repete em 5,7 milhões de anos
    {
        "temas_secundarios": ["historia_astronomia", "teoria_numeros"],
        "tipos_espanto": ["escala_absurda", "engenhosidade"],
        "gancho": "A data da Páscoa não segue a Lua do céu, e sim uma lua cheia calculada em tabelas. A sequência de datas que essas regras produzem só se repete, na mesma ordem, depois de 5,7 milhões de anos.",
        "explicacao": (
            "Pela regra, a Páscoa é o domingo seguinte à lua cheia pascal, que é a lua cheia eclesiástica que cai "
            "em 21 de março ou depois. Nada disso é observado no céu. O décimo quarto dia do mês lunar é tratado, por "
            "convenção, como o dia da lua cheia, e o 21 de março faz o papel do equinócio, como uma aproximação. No "
            "sistema de Beda, do século VIII, a data saía de um ciclo de 19 anos, depois do qual as fases da Lua "
            "voltam às mesmas datas do calendário. Só que essas tabelas se descolam da realidade depois de uns dois "
            "séculos, e, na época da reforma de 1582, as luas novas de verdade já vinham quatro dias antes das "
            "calculadas. A reforma gregoriana passou a aplicar correções periódicas ligadas ao Sol e à Lua. É a "
            "combinação desses ajustes que estica o ciclo: a sequência de datas da Páscoa gregoriana só se repete "
            "exatamente na mesma ordem após 5.700.000 anos, ou 2.081.882.250 dias. Isso é teoria pura: muito antes, "
            "o calendário teria de ser ajustado, porque a duração do ano, do mês lunar e do próprio dia vai "
            "mudando aos poucos."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Date_of_Easter",
                "Easter is the Sunday following the Paschal full moon date. "
                "The paschal full moon date is the ecclesiastical full moon date on or after the ecclesiastical equinox on 21 March. "
                "The fourteenth day of the lunar month is ecclesiastically considered the day of the full moon. [...] "
                "Historically, in Beda Venerabilis' Easter cycle, the paschal full moon date for a year was found from its sequence number in the Metonic cycle, called the golden number, which cycle repeats the lunar phase on January 1 every 19 years. "
                "This method was modified in the Gregorian reform because the tabular dates go out of sync with reality after about two centuries. [...] "
                "So the Gregorian Easter dates repeat in exactly the same order only after 5,700,000 years, 70,499,183 lunations, or 2,081,882,250 days [...] "
                "Of course, the calendar would have to be adjusted after a few millennia because of changes in the length of the tropical year, the synodic month, and the day.",
                nome="Date of Easter"),
            wiki("Gregorian_calendar",
                "It was instituted by the papal bull Inter gravissimas dated 24 February 1582 [...] "
                "fter the ecclesiastical full moon on or after 21 March, which was adopted as an approximation to the March equinox. [...] "
                "The 19-year cycle used for the lunar calendar required revision because the astronomical new moon was, at the time of the reform, four days before the calculated new moon.",
                nome="Gregorian calendar"),
        ],
    },
    # 8 os segundos intercalares e a Terra que acelerou
    {
        "temas_secundarios": ["medidas_padroes", "historia_computacao"],
        "tipos_espanto": ["contraintuitivo", "engenhosidade"],
        "gancho": "Entre 1972 e 2016, os relógios oficiais do mundo ganharam 27 segundos extras para acompanhar a rotação da Terra. Em 2020, ela girou mais rápido, e engenheiros passaram a discutir tirar um segundo.",
        "explicacao": (
            "O horário de referência mundial, o UTC, é marcado por relógios atômicos, mas o dia solar depende da "
            "rotação da Terra, que é irregular. Para que os dois não se afastassem mais de 0,9 segundo, a partir de "
            "1972 passou-se a inserir, de tempos em tempos, um segundo extra: o relógio marcava 23:59:60 no fim de "
            "30 de junho ou de 31 de dezembro. Foram 27 ao todo, o último em 31 de dezembro de 2016. Esses saltos "
            "imprevisíveis podiam dar problema em programas de computador, e o Google passou a diluí-los, esticando "
            "levemente os segundos ao longo de 20 horas. Em 2020, a Terra girou mais depressa e teve os 28 dias mais "
            "curtos desde 1960. O mais curto já registrado foi 29 de junho de 2022, com 1,59 milissegundo a menos "
            "que 24 horas. Engenheiros começaram a discutir um segundo intercalar negativo, que nunca tinha sido "
            "usado, e a preocupação com o efeito disso nos computadores reforçou a ideia de acabar com os ajustes. "
            "Em 2022, a Conferência Geral de Pesos e Medidas decidiu ampliar, até 2035, a diferença tolerada entre "
            "o tempo atômico e o da rotação, de modo a garantir ao UTC pelo menos um século sem saltos."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Leap_second",
            "the standard set a maximum permitted variance of ±0.9 seconds. [...] "
            "The leap second was introduced in 1972. [...] "
            "In total, 27 leap seconds were added to UTC, with the final occurring on 31 December 2016 [...] "
            "All were positive leap seconds, adding a second to a UTC day; while a negative leap second was theoretically possible, none ever occurred. "
            "Because the Earth's rotational speed varies in response to climatic and geological events, UTC leap seconds were irregularly spaced and not precisely predictable. [...] "
            "In 2021, it was reported that Earth had been spinning faster in 2020 and experienced the 28 shortest days since 1960, each of which lasted less than 86399.999 seconds. "
            "This caused engineers worldwide to discuss a negative leap second and other possible timekeeping measures, such as eliminating the leap seconds. "
            "The shortest day ever recorded was 29 June 2022, at 1.59 milliseconds less than 24 hours. [...] "
            "Every leap second was scheduled for either 30 June or 31 December. The extra second was displayed on UTC clocks as 23:59:60. [...] "
            "Because adding an extra second directly could cause problem on various computer programs, data centers would spread out the addition of extra second throughout hours in a practice known as smearing. "
            "Instead of inserting a leap second at the end of the day, Google servers implemented a \"leap smear\", extending seconds slightly over a 20-hour period centered on the leap second [...] "
            "Worry over the impact of the possibility of negative leap seconds on computer timekeeping furthered discussion on elimination of the leap second. [...] "
            "On 18 November 2022, the General Conference on Weights and Measures (CGPM) passed Resolution 4, directing that the maximum permitted difference between UT1 and UTC be increased \"in, or before, 2035.\" [...] "
            "a plan to implement a new maximum (UT1−UTC) value by 2035 that would ensure UTC continuity for at least a century.",
            nome="Leap second"),
            wiki("Leap_second",
            "Leap seconds or intercalary seconds were one-second adjustments occasionally applied to Coordinated Universal Time (UTC) between 1972 and 2016, to accommodate the difference between International Atomic Time (TAI), as measured precisely by atomic clocks, and observed solar time (UT1), which varies due to irregularities and long-term slowdown in the Earth's rotation.",
            nome="Leap second")],
    },
    # 9 o tempo na Etiópia: 13 meses, outro ano e outro relógio
    {
        "temas_secundarios": ["africa_antiga", "religioes"],
        "tipos_espanto": ["contraintuitivo", "origem_inesperada"],
        "gancho": "Na Etiópia, o ano tem treze meses e está sete ou oito anos atrás do nosso, e o relógio começa a contar no amanhecer: 7 da manhã é 1 hora. O país festejou a chegada do terceiro milênio em setembro de 2007.",
        "explicacao": (
            "O calendário etíope, o oficial do país, é solar: tem doze meses de trinta dias e mais cinco ou seis dias "
            "extras, que formam um décimo terceiro mês. Como no calendário juliano, há um dia bissexto a cada quatro anos, sem "
            "exceção. O Ano-Novo, chamado Enkutatash em amárico, cai em 11 de setembro, ou em 12 de setembro no "
            "ano que antecede um bissexto gregoriano. A diferença na contagem dos anos vem de uma divergência antiga "
            "sobre a data da Anunciação. A Igreja etíope segue o cálculo de Aniano de Alexandria, feito por volta "
            "do ano 400, enquanto os europeus acabaram adotando o de Dionísio, o Exíguo, do ano 525, que punha a "
            "Anunciação nove anos antes. Por isso, de janeiro até setembro, o ano etíope tem oito anos a menos que "
            "o nosso e, depois, sete. O terceiro milênio etíope começou em 11 de setembro de 2007. As horas também "
            "são outras: quase todos os etíopes usam um relógio de 12 horas em que o ciclo do dia começa ao "
            "amanhecer, às 6h no horário internacional, e o da noite ao anoitecer, às seis da tarde. Na prática, basta "
            "subtrair seis horas do horário oficial."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("Ethiopian_calendar",
                "The Ethiopian calendar or Geʽez calendar is the official state civil calendar of Ethiopia [...] "
                "The Geʽez calendar is a solar calendar [...] "
                "but like the Julian calendar, it adds a leap day every four years without exception, and begins the year on 11 or 12 September in the Gregorian calendar (from 1900 to 2099). [...] "
                "The Ethiopian calendar has twelve months, all thirty days long, and five or six epagomenal days, which form a thirteenth month. [...] "
                "while in Amharic, the official language of Ethiopia, it is called Enkutatash meaning \"gift of jewels\". "
                "It occurs on 11 September in the Gregorian calendar; except for the year preceding a leap year, when it occurs on 12 September. [...] "
                "To indicate the year, followers of the Ethiopian and Eritrean churches today use the Incarnation Era, which dates from the Annunciation of the Incarnation of Jesus on 25 March AD 9 (Julian), as calculated by Annianus of Alexandria c. 400 [...] "
                "Meanwhile, Europeans eventually adopted the calculations made by Dionysius Exiguus in AD 525 instead, which placed the Annunciation nine years earlier (Anno Domini#New year) than had Annianus. "
                "This causes the Ethiopian year number to be eight years less than the Gregorian year number from January 1 until 10 or 11 September, then seven years less for the remainder of the Gregorian year.",
                nome="Ethiopian calendar"),
            wiki("Ethiopian_Millennium",
                "was a New Year event in Ethiopia celebrating the transition to third millennium in the Ethiopian calendar, on 11 September 2007.",
                nome="Ethiopian Millennium"),
            wiki("Time_in_Ethiopia",
                "Almost all Ethiopians use a modified 12-hour clock system. "
                "The daytime cycle begins at dawn 12:00 (6:00:00 AM EAT) and ends at dusk 11:59:59 (5:59:59 PM EAT). "
                "The nighttime cycle begins at dusk 12:00 (6:00:00 PM EAT) and ends at dawn at 11:59:59 (5:59:59 AM EAT). "
                "The convention is that the day begins at 1:00 o'clock in the morning according to the 12-hour cycle (7:00 AM EAT) rather than midnight (12:00 AM EAT). [...] "
                "In practice one can subtract 6 hours from EAT to get the Ethiopian one.",
                nome="Time in Ethiopia"),
        ],
    },
    # 10 o calendário maia não acabava em 2012
    {
        "temas_secundarios": ["americas_pre_colombianas", "cosmologia"],
        "tipos_espanto": ["mito_desmentido", "escala_absurda"],
        "gancho": "O calendário maia não terminava em 2012. Uma inscrição de Palenque projeta uma data no ano 4772, e uma estela de Cobá conta ciclos que, numa leitura, somam 2 quintilhões de vezes a idade do universo.",
        "explicacao": (
            "A febre do fim do mundo em 2012 nasceu de uma leitura da Contagem Longa, o calendário maia que conta os "
            "dias passados desde uma data mítica da criação, equivalente a 11 de agosto de 3114 a.C. Em 2012 se "
            "completava um dos grandes ciclos dessa contagem. Estudiosos dos maias rebateram que nenhum relato maia "
            "clássico previa uma catástrofe e que a ideia de que a Contagem Longa acabava em 2012 deturpava a "
            "história e a cultura maias. Para o especialista Mark Van Stone, a noção de um \"Grande Ciclo\" que se "
            "encerra é uma invenção moderna. A maioria das inscrições maias clássicas é histórica, sem profecias, e "
            "algumas citam datas muito além de 2012. No Templo das Inscrições, em Palenque, um texto parte do "
            "nascimento do governante Pakal, em 603, e soma a ele um intervalo que leva a 21 de outubro de 4772, "
            "mais de 4.000 anos depois de sua época. Em Cobá, a Estela 1 registra a data da criação com uma longa "
            "fileira de 13 acima do ciclo usado em 2012. Segundo a maianista Linda Schele, esses 13 seriam o ponto "
            "de partida de um enorme hodômetro do tempo, o que faria o universo atual durar pelo menos 2 "
            "quintilhões de vezes a idade calculada pelos cosmólogos."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            wiki("2012_phenomenon",
                "Mayan scholars stated that no classic Mayan accounts forecast impending doom, and the idea that the Long Count calendar ends in 2012 misrepresented Mayan history and culture. [...] "
                "\"The notion of a 'Great Cycle' coming to an end is completely a modern invention.\" [...] "
                "Most classic Maya inscriptions are strictly historical and do not make any prophetic declarations. [...] "
                "Maya inscriptions occasionally mention predicted future events or commemorations that would occur on dates far beyond the completion of the 13th [...] "
                "On the west panel at the Temple of Inscriptions in Palenque, a section of text projects forward to the 80th 52-year Calendar Round from the coronation of the ruler [...] "
                "The inscription begins with Pakal's birthdate of 9.8.9.13.0 (24 March, 603 AD Gregorian) and then adds the Distance Number 10.11.10.5.8 to it, arriving at a date of 21 October 4772 AD, more than 4,000 years after Pakal's time. "
                "Another example is Stela 1 at Coba which marks the date of creation as 13.13.13.13.13.13.13.13.13.13.13.13.13.13.13.13.13.13.13.13.0.0.0.0, or nineteen units above the [...] "
                "According to Linda Schele, these 13s represent \"the starting point of a huge odometer of time\", with each acting as a zero and resetting to 1 as the numbers increase. "
                "Thus this inscription anticipates the current universe lasting at least [...] "
                "a time span equal to 2 quintillion times the age of the universe as determined by cosmologists.",
                nome="2012 phenomenon"),
            wiki("Mesoamerican_Long_Count_calendar",
                "the Long Count calendar identifies a day by counting the number of days passed since a mythical creation date that corresponds to August 11, 3114 BCE in the proleptic Gregorian calendar.",
                nome="Mesoamerican Long Count calendar"),
        ],
    },
    # 11 o dia juliano dos astrônomos começa em 4713 a.C.
    {
        "temas_secundarios": ["historia_astronomia", "teoria_numeros"],
        "tipos_espanto": ["engenhosidade", "origem_inesperada"],
        "gancho": "Astrônomos contam os dias sem meses nem anos, a partir do meio-dia de 1º de janeiro de 4713 a.C. A data foi escolhida em 1583 por ser o último ano em que três ciclos do calendário começaram juntos.",
        "explicacao": (
            "É o dia juliano, uma contagem contínua de dias usada sobretudo na astronomia e também em programas que "
            "precisam calcular quanto tempo passou entre duas datas, como a fabricação e a validade de um alimento. "
            "A base é o período juliano, proposto em 1583, um ano depois da reforma gregoriana, pelo estudioso "
            "Joseph Scaliger. Ele é o produto de três ciclos usados junto com o calendário juliano: o solar, de 28 "
            "anos; o lunar, de 19; e o da indicção, de 15. Juntos, eles formam um período de 7.980 anos. O ano de "
            "4713 a.C. foi o último em que os três estavam no primeiro ano ao mesmo tempo, e ficava antes de "
            "qualquer registro histórico. Para os historiadores, isso era precioso: cada ano tinha uma combinação "
            "única de posições nos três ciclos, e esses números às vezes apareciam em documentos antigos sem o ano. "
            "Na contagem dos astrônomos, o dia 0 começa ao meio-dia de 1º de janeiro de 4713 a.C., e o meio-dia de "
            "1º de janeiro de 2000 abriu o dia 2.451.545. Muitas referências dizem que o nome homenageia o pai de "
            "Scaliger, Júlio, mas ele próprio escreveu que chamou o período de juliano porque se ajusta ao ano "
            "juliano. O próximo período juliano começa em 3268."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Julian_day",
            "The Julian day is a continuous count of days from the beginning of the Julian period; it is used primarily by astronomers, and in software for easily calculating elapsed days between two events (e.g., food production date and expiration date). "
            "The Julian period is a chronological interval of 7980 years, derived from three multi-year cycles: the indiction, solar, and lunar cycles. "
            "The last year that was simultaneously the beginning of all three cycles was 4713 BC (−4712) [...] "
            "The next Julian period begins in the year AD 3268. "
            "Historians used the period to identify Julian calendar years within which an event occurred when no such year was given in the historical record [...] "
            "Specifically, Julian day number 0 is assigned to the day starting at noon Universal Time on Monday, 1 January 4713 BC, proleptic Julian calendar [...] "
            "For example, the Julian day number for the day starting at 12:00 UT (noon) on 1 January 2000, was 2451545. [...] "
            "The Julian day number is based on the Julian period proposed by Joseph Scaliger, a classical scholar, in 1583 (one year after the Gregorian calendar reform) as it is the product of three calendar cycles used with the Julian calendar: [...] "
            "Years of the Julian period are counted from this year, 4713 BC, as year 1, which was chosen to be before any historical record. "
            "Scaliger corrected chronology by assigning each year a tricyclic \"character\", three numbers indicating that year's position in the 28-year solar cycle, the 19-year lunar cycle, and the 15-year indiction cycle. "
            "One or more of these numbers often appeared in the historical record alongside other pertinent facts without any mention of the Julian calendar year. "
            "The character of every year in the historical record was unique [...] "
            "Although many references say that the Julian in \"Julian period\" refers to Scaliger's father, Julius Scaliger, at the beginning of Book V of his Opus de Emendatione Temporum (\"Work on the Emendation of Time\") he states, \"Iulianam vocauimus: quia ad annum Iulianum accomodata\", which Reese, Everett and Craun translate as \"We have termed it Julian because it fits the Julian year\".",
            nome="Julian day")],
    },
    # 12 o "Franksgiving" de Roosevelt
    {
        "temas_secundarios": ["economia_curiosa", "costumes_rituais"],
        "tipos_espanto": ["historia_humana"],
        "gancho": "Em 1939, Roosevelt antecipou em uma semana o Dia de Ação de Graças para esticar as compras de Natal. Quase metade dos estados manteve a data antiga, e três deram folga nas duas.",
        "explicacao": (
            "Desde Lincoln, em 1863, o feriado caía na última quinta-feira de novembro. Em 1939, em plena Grande "
            "Depressão, novembro tinha cinco quintas, e a última era o dia 30. Na época, era malvisto o comércio "
            "fazer decorações e liquidações de Natal antes da Ação de Graças, e os empresários temiam perder vendas "
            "com tão poucos dias de compras até o Natal. A pedido de Fred Lazarus Jr., chefe de uma rede de lojas "
            "de departamento, Roosevelt mudou a data para 23 de novembro. A reação foi forte. O prefeito de Atlantic "
            "City apelidou a data de \"Franksgiving\", juntando Franklin e Thanksgiving, e uma pesquisa Gallup "
            "mostrou 62% dos americanos contra a mudança. Como cada estado decide as folgas do próprio "
            "funcionalismo, vinte e três estados e o Distrito de Columbia seguiram a nova data, vinte e dois ficaram com o dia 30, e "
            "Colorado, Mississippi e Texas deram feriado nas duas semanas. Times universitários de futebol americano "
            "que fechavam a temporada no feriado ficaram com jogos marcados na data errada. Uma pesquisa do "
            "Departamento de Comércio, em 1941, não achou aumento significativo nas vendas. No fim daquele ano, o "
            "Congresso aprovou e Roosevelt assinou a fixação do feriado na quarta quinta-feira de novembro, a "
            "partir de 1942."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Franksgiving",
            "In 1939, American President Franklin D. Roosevelt moved the Thanksgiving holiday earlier by one week, to the second-to-last Thursday in November. "
            "This change was intended to help boost the economy by providing an extra seven days for Christmas shopping. "
            "However, this decision led to significant public backlash, with many people deriding the holiday as Franksgiving. "
            "The term Franksgiving, a portmanteau of Franklin and Thanksgiving, was coined by Charles D. White, the mayor of Atlantic City, in the same year. [...] "
            "Then, in 1863, during the Civil War, Abraham Lincoln established the last Thursday of November as the official date for Thanksgiving to be celebrated each year. [...] "
            "However, in 1939, during the Great Depression, November had five Thursdays, and the last one fell on November 30, which left little time for the Christmas shopping season. "
            "To address this concern, in August 1939, President Franklin D. Roosevelt decided to break from tradition and issued an executive order declaring that Thanksgiving would be celebrated on November 23 instead of November 30. "
            "Fred Lazarus Jr., the head of Federated Department Stores (which would later become Macy's, Inc.), urged Roosevelt to move Thanksgiving to a week earlier [...] "
            "At that time, it was generally frowned upon for retailers to display Christmas decorations or hold Christmas sales prior to Thanksgiving [...] "
            "They feared that, particularly during the Depression, they would lose sales because there were only 24 shopping days between Thanksgiving and Christmas. [...] "
            "For example, many college football teams routinely ended their seasons with rivalry games on Thanksgiving, and had scheduled them that year for the last day in November [...] "
            "and that Americans overall opposed the change 62% to 38%. [...] "
            "and each state government can independently determine when to cancel work for state (and in some cases, municipal) employees. "
            "Twenty-three states' governments and the District of Columbia recognized the non-traditional date, twenty-two states preserved the traditional date on November 30, and the remaining three – Colorado, Mississippi, and Texas – gave holidays in both weeks. [...] "
            "A 1941 Commerce Department survey found no significant expansion of retail sales due to the change. [...] "
            "In December 1941, following the United States' entry into World War II, Congress approved a proclamation that President Roosevelt signed. "
            "This proclamation designated the federal Thanksgiving Day holiday as the fourth Thursday in November, starting in 1942.",
            nome="Franksgiving")],
    },
    # 13 o Excel acha que 1900 foi bissexto
    {
        "temas_secundarios": ["historia_computacao", "algoritmos"],
        "tipos_espanto": ["contraintuitivo", "conexao_inesperada"],
        "gancho": "Para o Excel, existiu o dia 29 de fevereiro de 1900, que nunca aconteceu. A Microsoft sabe e não corrige: o erro foi herdado de propósito do Lotus 1-2-3, e consertá-lo mudaria quase todas as datas das planilhas.",
        "explicacao": (
            "Pela regra do calendário gregoriano, um ano de virada de século só é bissexto se também for divisível "
            "por 400, e 1900 não é. O Lotus 1-2-3, porém, foi lançado tratando 1900 como bissexto. Segundo a "
            "Microsoft, isso simplificava o tratamento dos anos bissextos e não atrapalhava quase nenhum cálculo de "
            "datas. Quando o Multiplan e o Excel chegaram, a Microsoft adotou a mesma suposição de caso pensado: "
            "assim, os programas usavam o mesmo sistema de números de série para datas do Lotus, e as planilhas "
            "podiam passar de um programa para o outro. Hoje, a empresa diz que seria tecnicamente possível "
            "corrigir, mas que as desvantagens seriam maiores que as vantagens. Quase todas as datas das planilhas "
            "existentes recuariam um dia, o que daria muito trabalho para acertar, sobretudo em fórmulas. Funções "
            "como a WEEKDAY (DIA.DA.SEMANA, em português) passariam a devolver outros valores, e a compatibilidade "
            "de datas com outros programas se perderia. Mantido o erro, só sobra um problema: o dia da semana sai "
            "errado para datas anteriores a 1º de março de 1900, que quase ninguém usa. Todos os outros anos são "
            "tratados direito, inclusive os de século que não são bissextos, como 2100."
        ),
        "nivel": 1, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [
            {"url": "https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/excel/wrongly-assumes-1900-is-leap-year",
             "titulo": "Excel incorrectly assumes that the year 1900 is a leap year", "idioma": "en",
             "trecho": (
                "Microsoft Excel incorrectly assumes that the year 1900 is a leap year. [...] "
                "When Lotus 1-2-3 was first released, the program assumed that the year 1900 was a leap year, even though it actually was not a leap year. "
                "This made it easier for the program to handle leap years and caused no harm to almost all date calculations in Lotus 1-2-3. "
                "When Microsoft Multiplan and Microsoft Excel were released, they also assumed that 1900 was a leap year. "
                "This assumption allowed Microsoft Multiplan and Microsoft Excel to use the same serial date system used by Lotus 1-2-3 and provide greater compatibility with Lotus 1-2-3. "
                "Treating 1900 as a leap year also made it easier for users to move worksheets from one program to the other. "
                "Although it is technically possible to correct this behavior so that current versions of Microsoft Excel do not assume that 1900 is a leap year, the disadvantages of doing so outweigh the advantages. "
                "If this behavior were to be corrected, many problems would arise, including: "
                "Almost all dates in current Microsoft Excel worksheets and other documents would be decreased by one day. "
                "Correcting this shift would take considerable time and effort, especially in formulas that use dates. "
                "Some functions, such as the WEEKDAY function, would return different values; this might cause formulas in worksheets to work incorrectly. "
                "Correcting this behavior would break serial date compatibility between Microsoft Excel and other programs that use dates. "
                "If the behavior remains uncorrected, only one problem occurs: "
                "The WEEKDAY function returns incorrect values for dates before March 1, 1900. "
                "Because most users do not use dates before March 1, 1900, this problem is rare. "
                "NOTE: Microsoft Excel correctly handles all other leap years, including century years that are not leap years (for example, 2100).")},
            wiki("Gregorian_calendar",
                "The proposed rule was that \"years divisible by 100 would be leap years only if they were divisible by 400 as well\". [...] "
                "for many years it has been customary to put the extra day at the end of the month of February, adding a 29 February for the leap day.",
                nome="Gregorian calendar"),
        ],
    },
    # 14 o Ano-Novo judaico nunca cai em domingo, quarta ou sexta
    {
        "temas_secundarios": ["religioes", "teoria_numeros"],
        "tipos_espanto": ["engenhosidade", "contraintuitivo"],
        "gancho": "O calendário judaico tem regras para o Ano-Novo nunca cair num domingo, numa quarta ou numa sexta. Assim, o Yom Kippur, que segue restrições como as do sábado, nunca fica colado ao Shabat.",
        "explicacao": (
            "O ano comum do calendário hebraico tem 12 meses que, somados, dão 354 dias, e os anos bissextos ganham "
            "um mês a mais: o mês de Adar é desdobrado em Adar I e Adar II. As contas usam um mês lunar médio de 29 "
            "dias, 12 horas e 793 \"partes\", numa divisão em que cada hora tem 1.080 partes, e cada parte vale 3 "
            "segundos e um terço. Cada ano começa no Rosh Hashaná, o Ano-Novo, e quatro regras de adiamento, as "
            "dehiyyot, podem empurrar essa data. A mais usada no dia a dia: se a lua nova calculada cair num domingo, "
            "numa quarta ou numa sexta, o Ano-Novo passa para o dia seguinte. O motivo é religioso. Assim, o Yom "
            "Kippur nunca cai numa sexta nem num domingo, e o Hoshana Rabbah nunca cai num sábado. Como o Yom "
            "Kippur obedece às mesmas restrições do Shabat, se um viesse logo antes do outro não daria para "
            "preparar o segundo dia, por exemplo acendendo as velas. O Rosh Hashaná, portanto, só cai em segunda, "
            "terça, quinta ou sábado. Para encaixar tudo, o tamanho do ano varia: um ano comum pode ter 353, 354 ou "
            "355 dias, e um ano bissexto, 383, 384 ou 385."
        ),
        "nivel": 2, "nota_surpresa": 4, "confianca": "alta",
        "fontes": [wiki("Hebrew_calendar",
            "which is 29 days, 12 hours, and 793 parts (there are 1080 \"parts\" in an hour, so that one part is equal to 3+1⁄3 seconds). [...] "
            "Thus, the year normally contains twelve months with a total of 354 days. [...] "
            "During leap years, the 12th and 13th months are named Adar I and Adar II [...] "
            "Because each calendar year begins with Rosh Hashanah, adjusting the year length is equivalent to moving the day of the next Rosh Hashanah. [...] "
            "Four conditions are considered to determine whether the date of Rosh Hashanah must be postponed. These are called the Rosh Hashanah postponement rules, or deḥiyyot. [...] "
            "If the molad occurs on a Sunday, Wednesday, or Friday, Rosh Hashanah is postponed to the following day. [...] "
            "This rule is applied for religious reasons, so that Yom Kippur does not fall on a Friday or Sunday, and Hoshana Rabbah does not fall on Shabbat. "
            "Since Shabbat restrictions also apply to Yom Kippur, if either day falls immediately before the other, it would not be possible to make necessary preparations for the second day (such as candle lighting). [...] "
            "Thus, Rosh Hashanah can only fall on Monday, Tuesday, Thursday, and Saturday. [...] "
            "The rules of postponement of Rosh HaShanah make it that a Jewish common year will have 353, 354, or 355 days while a leap year (with the addition of Adar I which always has 30 days) has 383, 384, or 385 days.",
            nome="Hebrew calendar")],
    },
    # 15 Carnaval não é feriado nacional, e Tiradentes já perdeu o seu
    {
        "temas_secundarios": ["brasil_republica", "cultura_popular"],
        "tipos_espanto": ["mito_desmentido", "historia_humana"],
        "gancho": "O Carnaval não é feriado nacional no Brasil: para o governo federal, é ponto facultativo. E até Tiradentes já perdeu o seu: Getúlio Vargas cortou o feriado em 1930, junto com metade da lista, e o devolveu em 1933.",
        "explicacao": (
            "No Brasil, quem cria feriado é a lei, e ele pode ser civil ou religioso. Para a administração federal, "
            "a segunda e a terça de Carnaval, assim como a Quarta-feira de Cinzas e o Corpus Christi, são pontos "
            "facultativos, e não feriados nacionais. Essas datas móveis dependem da Páscoa, e a terça de Carnaval cai "
            "sempre quarenta e sete dias antes dela. Elas só viram feriado de fato quando um município as inclui entre os seus "
            "dias de guarda, que a lei limita a quatro, contando a Sexta-feira da Paixão. A lista nacional já mudou "
            "muito. Até 1930, o país tinha doze feriados nacionais, entre eles o 24 de fevereiro, da "
            "Constituição de 1891, o 3 de maio, então data do Descobrimento, o 13 de maio, da Abolição, e o 14 de "
            "julho, dedicado à liberdade e à independência dos povos americanos. Em 15 de dezembro de 1930, um "
            "decreto de Vargas reduziu a lista de doze para seis e eliminou até o 21 de abril, data da execução de "
            "Tiradentes. O feriado só foi restabelecido por outro decreto, em 17 de abril de 1933. O mais recente "
            "feriado nacional é o Dia da Consciência Negra, criado em 2024."
        ),
        "nivel": 1, "nota_surpresa": 3, "confianca": "alta",
        "fontes": [wiki("Feriados_no_Brasil",
            "No Brasil, os feriados nacionais, estaduais e municipais são estipulados por leis, e podem ter origem civil ou religiosa conforme estabelecida pela lei nº 9.093 de 1995 [...] "
            "O feriado mais recente criado foi o Dia da Consciência Negra em 2024 sancionado por Lula. "
            "São considerados pontos facultativos: a segunda e a terça-feira de Carnaval, a Quarta-feira de Cinzas, a quinta-feira de Corpus Christi [...] "
            "os dias de guarda, declarados em lei municipal, de acordo com a tradição local e em número não superior a quatro, neste incluída a Sexta-Feira da Paixão. [...] "
            "Em 15 de dezembro de 1930, pelo decreto nº 19.488, o presidente da república Getúlio Vargas reduziu o número de feriados nacionais de doze para seis. "
            "Até então eram feriados no Brasil, segundo o citado decreto nº 19.488: [...] "
            "24 de fevereiro (Constituição de 1891); "
            "21 de abril (Execução de Tiradentes); [...] "
            "3 de maio (Descobrimento do Brasil, antes era comemorado nesta data); "
            "13 de maio (Abolição da escravidão no Brasil); "
            "14 de julho (Liberdade e Independência dos Povos Americanos); [...] "
            "Este decreto nº 19.488 eliminara o feriado de Tiradentes, o qual foi restabelecido pelo decreto nº 22.647, de 17 de abril de 1933, assinado pelo presidente Getúlio Vargas. [...] "
            "As festas móveis são aquelas que dependem da Páscoa [...] "
            "Tais datas festivas ou de guarda não são feriados nacionais, mas podem ser alvo de feriados municipais, conforme prevê a lei nº 9.093/1995. São elas: "
            "Carnaval (terça-feira) - quarenta e sete dias antes da Páscoa;",
            nome="Feriados no Brasil", idioma="pt")],
    },
]
