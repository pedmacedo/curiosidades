"""Rodada 2 de Memória: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-memoria-01.py"))
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)

LOTE, AREA, TEMA = _base.LOTE, _base.AREA, _base.TEMA
wiki = _base.wiki
CANDIDATOS = _base.CANDIDATOS


def trocar(n, **campos):
    CANDIDATOS[n - 1].update(campos)


def substituir(n, campo, velho, novo):
    texto = CANDIDATOS[n - 1][campo]
    assert velho in texto, (n, velho)
    CANDIDATOS[n - 1][campo] = texto.replace(velho, novo)


def substituir_trecho(n, i_fonte, velho, novo):
    fonte = CANDIDATOS[n - 1]["fontes"][i_fonte]
    assert velho in fonte["trecho"], (n, velho)
    fonte["trecho"] = fonte["trecho"].replace(velho, novo)


def acrescentar_trecho(n, i_fonte, extra):
    CANDIDATOS[n - 1]["fontes"][i_fonte]["trecho"] += " [...] " + extra


# 0001: "quase não conseguia"; fragmentos guardados (a planta da casa); frase menos literal
substituir(1, "gancho", "Henry Molaison nunca mais formou lembranças novas.",
    "Henry Molaison quase não conseguia mais formar lembranças novas.")
substituir(1, "explicacao", "ele passou a esquecer o que vivia, as pessoas que via e o que fazia.",
    "ele passou a esquecer quase tudo o que acontecia: episódios recentes, gente que conhecia depois da "
    "operação, tarefas que tinha acabado de fazer.")
substituir(1, "explicacao", "A inteligência e a memória de curto prazo continuavam normais.",
    "A inteligência e a memória de curto prazo continuavam normais. Ainda assim, guardou fragmentos: conseguia "
    "desenhar com bastante detalhe a planta da casa para onde se mudou cinco anos depois da cirurgia.")
acrescentar_trecho(1, 0, "Despite his general inability to form new episodic or factual long-term memories, as well as his heavy impairment on certain spatial memory tests, "
    "Molaison was able to draw a quite detailed map of the topographical layout of his residence. "
    "This finding is remarkable since Molaison had moved to the house five years after his surgery")

# 0002: tempo verbal (diário registrado até 2007; capacidade, não atividade atual)
substituir(2, "gancho", "esquece tudo em segundos e enche páginas do diário", "esquece tudo em segundos e encheu páginas do diário")
substituir(2, "gancho", "Mesmo assim, ainda toca peças complexas ao piano e rege um coro.",
    "Mesmo assim, continuou capaz de tocar peças complexas ao piano e de reger um coro.")
substituir(2, "explicacao", "mas lê partituras à primeira vista, toca peças complexas ao piano e ao órgão e rege um coro.",
    "mas continuou capaz de ler partituras à primeira vista, tocar peças complexas ao piano e ao órgão e reger um coro.")
acrescentar_trecho(2, 0, "he still wrote diary entries in 2007, more than 20 years after he started them.")

# 0003: "com mais frequência"; replicações do efeito geral; confiança
trocar(3, confianca="consenso_parcial",
    gancho="Num experimento de 1974, quem foi perguntado a que velocidade os carros \"se esmagaram\" passou a \"lembrar\" "
           "com mais frequência de vidro quebrado no vídeo do acidente. Não havia vidro nenhum.")
substituir(3, "explicacao",
    "Uma parte estatisticamente significativa do grupo do \"esmagaram\" disse que sim, embora o vídeo não mostrasse vidro algum.",
    "O grupo do \"esmagaram\" disse que sim com frequência significativamente maior que os outros dois, embora o vídeo não mostrasse vidro algum.")
substituir(3, "explicacao", "Bastou trocar uma palavra para que um detalhe falso entrasse na lembrança.",
    "Trocar uma única palavra bastou para que mais gente incorporasse um detalhe falso à lembrança.")
substituir(3, "explicacao", "e o estudo original abriu caminho para muitas replicações.",
    "e o efeito foi reproduzido em muitos estudos posteriores.")
acrescentar_trecho(3, 0, "The difference between this group and the others was that they were primed with the word \"smashed\" in the questionnaire, one week before answering the question.")

# 0004: foto fora do gancho; cautela com a diferença da foto; o debate (replicação de 2023 e reanálise); confiança
trocar(4, confianca="consenso_parcial",
    gancho="Em estudos que contaram a adultos um episódio falso da infância deles, parte passou a \"lembrar\" do que "
           "nunca viveu. Uma análise de oito estudos chegou a quase um terço; críticos acham que bem menos.",
    explicacao=(
        "A técnica foi criada por Elizabeth Loftus e um aluno dela, Jim Coan, que a testou primeiro no próprio "
        "irmão, com a história falsa de que ele tinha se perdido num shopping por volta dos 5 anos. Num estudo "
        "formal com 24 pessoas, cerca de 25% relataram lembrar o episódio. Como cada pesquisa definia \"lembrança "
        "falsa\" de um jeito, um grupo de pesquisadores reuniu as transcrições de oito estudos publicados, com 423 "
        "participantes, e as reclassificou com os mesmos sete critérios: 30,4% dos casos contaram como memórias "
        "falsas, e outros 23% aceitaram o episódio em algum grau. A fotografia adulterada, ao contrário do que se "
        "esperaria, pareceu render menos memórias falsas (25,9%, contra 33,6% sem foto), mas a diferença é pequena, "
        "e todas as fotos mostravam o mesmo episódio, um passeio de balão. A taxa de cerca de um terço é "
        "contestada. Em 2023, a psicóloga irlandesa Gillian Murphy e colegas repetiram o estudo do shopping com "
        "123 pessoas e classificaram 35% como tendo memória falsa, mas, quando perguntados, só 14% disseram "
        "lembrar do episódio. Ao reanalisar esses dados, os psicólogos Bernice Andrews e Chris Brewin, que pedem "
        "cautela com essa linha de pesquisa, concluíram que só cinco participantes, e não 43, podiam ser "
        "considerados com uma memória falsa. Para eles, implantar a lembrança de um episódio inteiro é bem mais "
        "difícil do que os estudos anteriores sugeriam."
    ))
CANDIDATOS[4 - 1]["fontes"].append(
    {"url": "https://www.scientificamerican.com/article/people-likely-arent-as-susceptible-to-false-memories-as-researchers-thought/",
     "titulo": "People Likely Aren't as Susceptible to False Memories as Researchers Thought (Bernice Andrews e Chris R. Brewin, Scientific American)",
     "idioma": "en",
     "trecho": "By Bernice Andrews & Chris R. Brewin [...] "
        "Our analysis digs into these questions and suggests that the body of research on false-memory induction must be treated with caution; "
        "it is probably much more difficult to convince someone of a false memory than past work has suggested. "
        "In 2023 Irish psychologist Gillian Murphy and her colleagues closely repeated the “lost in the mall” study, following the original methods. "
        "They used a larger sample of 123 people and reported that 35 percent of participants had a false memory, 10 percent more than in the original study. "
        "When asked, however, less than half as many participants (14 percent) said they had a memory of the fake event. [...] "
        "Taking everything into account, we estimated that only five participants could reasonably be claimed to have a false memory, rather than the 43 that were originally claimed. [...] "
        "it is easy to implant entire false memories in others"})

# 0005: a hipótese do mecanismo especial foi debatida, não "derrubada"
substituir(5, "explicacao", "A ideia não resistiu bem aos testes.", "Essas propriedades vêm sendo debatidas desde então.")
acrescentar_trecho(5, 0, "Most of these initial properties of flashbulb memory have been debated since Brown and Kulik first coined the term.")

# 0007: "podem", não "costumam"
substituir(7, "gancho", "Mesmo assim, costumam ir mal em decorar informações e formam memórias falsas",
    "Mesmo assim, podem ir mal em decorar informações e formam memórias falsas")

# 0009: a conclusão sobre a memória imperfeita é de Reed Johnson
substituir(9, "gancho", "Mas o diário dele diz que não tinha memória perfeita, e um sobrinho conta que ele treinava horas por dia para os shows.",
    "Mas um sobrinho conta que ele podia ser esquecido e treinava horas por dia para os shows.")
substituir(9, "explicacao", "Segundo o diário autobiográfico dele, encontrado por Reed Johnson, ele não tinha recordação perfeita.",
    "Reed Johnson, que encontrou um diário autobiográfico de Shereshevsky e escreveu sobre ele na revista The New "
    "Yorker, concluiu que ele não tinha memória perfeita.")
acrescentar_trecho(9, 0, "Johnson, Reed (12 August 2017), \"The Mystery of S., the Man with an Impossible Memory\", The New Yorker.")

# 0010: 2021 é o ano da publicação
substituir(10, "gancho", "Quando alguém enfim refez o experimento, em 2021, o efeito não apareceu.",
    "Quando alguém enfim refez o experimento (estudo publicado em 2021), o efeito não apareceu.")

# 0011: experimento em 2011-2012; exceção dos 31 dias; salto "provavelmente"
trocar(11, nota_surpresa=3,
    gancho="Em 1880, Hermann Ebbinghaus decorou sílabas sem sentido, sendo a própria cobaia, e traçou a curva do "
           "esquecimento. Em 2011, um estudante holandês passou 70 horas refazendo o experimento e obteve uma curva "
           "muito parecida.")
substituir(11, "explicacao", ", como \"WID\" e \"ZOF\", mais uniformes.", ", mais uniformes.")
substituir(11, "explicacao", "muitas vezes com três sessões por dia", "muitas vezes com até três sessões por dia")
substituir(11, "explicacao", "Em 2015, dois pesquisadores da Universidade de Amsterdã refizeram o experimento.",
    "Num estudo publicado em 2015, dois pesquisadores da Universidade de Amsterdã relataram como refizeram o "
    "experimento entre 2011 e 2012.")
substituir(11, "explicacao", "Os resultados ficaram parecidos com os originais.",
    "Os resultados ficaram parecidos com os originais, exceto no intervalo de 31 dias, em que a economia dele foi "
    "bem menor que a de Ebbinghaus.")
substituir(11, "explicacao", "E a curva não é totalmente lisa: há um salto para cima a partir do ponto de 24 horas.",
    "E a curva provavelmente não é totalmente lisa: os autores viram indícios de um salto para cima a partir do "
    "ponto de 24 horas.")
acrescentar_trecho(11, 0, "In the experimental phase, which took place between 01-12-2011 and 13-02-2012, a total of 69 lists was learned and relearned [...] "
    "The total time spent on data collection in the experimental phase amounted to about 70 hours. [...] "
    "Learning schedule during 2011–2012 for all lists [...] "
    "our replication was carried out in a Dutch language context [...] "
    "The greatest deviation is by Dros at 31 days; his savings score is much lower that any of the other three.")

# 0012: "nesse experimento"; a ressalva da replicação da UCLA (espaçamento)
substituir(12, "explicacao", "Ou seja, depois do primeiro acerto, estudar de novo",
    "Ou seja, nesse experimento, depois do primeiro acerto, estudar de novo")
substituir(12, "explicacao", "Em 2016, uma equipe da Universidade da Califórnia em Los Angeles replicou o resultado.",
    "Em 2016, uma equipe da Universidade da Califórnia em Los Angeles replicou o resultado, mas fez uma "
    "ressalva: a aparente inutilidade da releitura podia vir das diferenças de espaçamento entre as repetições, "
    "criadas pelo jeito como os grupos foram montados. Quando cada participante passou por todas as condições, "
    "tanto testar quanto reestudar melhoraram o aprendizado.")
acrescentar_trecho(12, 1, "We then examined whether the apparent ineffectiveness of restudying might be attributable to the spacing differences between items that were inherent in the between-subjects design employed by Karpicke and Roediger. "
    "When we controlled for these spacing differences by manipulating the various learning conditions within subjects in Experiment 2, we found that both repeated testing and restudying improved learning")

# 0013: sem o 51%; crianças de dois ou três anos; "reativados com luz"
substituir(13, "gancho", "quando os neurônios certos foram religados.", "quando os neurônios certos foram reativados com luz.")
substituir(13, "explicacao", "Crianças acertam 51% dos eventos ocorridos antes dos dois anos, período do qual os adultos não lembram quase nada.",
    "Crianças de dois ou três anos conseguem lembrar coisas que aconteceram quando tinham um ou dois anos, período "
    "do qual os adultos não lembram quase nada.")
substituir_trecho(13, 0, "Children's recall is 51% accurate for events that happened before the age of two whereas adults remember nearly nothing before that age.",
    "whereas adults remember nearly nothing before that age. [...] "
    "Children around the age of two to three have been found to remember things that occurred when they were only one to two years old.")
