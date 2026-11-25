"""Rodada 2 de Falhas de engenharia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-falhas_engenharia-01.py"))
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


# 0001: as réguas são explicação provável da assimetria; a causa principal foi o peso no alto
substituir(1, "explicacao", "depois de só três idas e vindas.", "depois de só três travessias.")
substituir(1, "explicacao",
    "As equipes mediram com unidades diferentes, e o navio ficou mais pesado a bombordo.",
    "O casco também é assimétrico, com mais peso a bombordo, e uma explicação provável é que equipes "
    "diferentes trabalharam com réguas diferentes. Mas o que derrubou o navio foi o excesso de peso no alto.")

# 0002: tom sóbrio no gancho
substituir(2, "gancho", "uma onda pegajosa matou 21 pessoas", "uma onda de melaço matou 21 pessoas")

# 0003: "quatro estados" só aparece no resumo da fonte
substituir(3, "explicacao", "A empresa de engenharia perdeu as licenças em quatro estados",
    "A empresa de engenharia perdeu as licenças em vários estados americanos")

# 0004: a explicação clássica da sincronia é contestada (Nature Communications, 2021)
trocar(4, confianca="consenso_parcial", tipos_espanto=["contraintuitivo", "mito_desmentido"],
    gancho="A ponte do Milênio, em Londres, fechou dois dias após abrir, em 2000, porque balançava de lado. "
           "A explicação clássica: os pedestres entravam no ritmo do balanço sem perceber e o reforçavam. "
           "Hoje isso é questionado.")
substituir(4, "explicacao", "Ela reabriu em fevereiro de 2002",
    "Um estudo publicado em 2021 na Nature Communications contestou essa versão: para os autores, os passos "
    "coordenados foram consequência do balanço, e não a causa, porque o jeito como cada pedestre se equilibra "
    "já bastaria para alimentar a oscilação, mesmo sem sincronia. A ponte reabriu em fevereiro de 2002")
CANDIDATOS[3]["fontes"].append({
    "url": "https://www.nature.com/articles/s41467-021-27568-y",
    "titulo": "Emergence of the London Millennium Bridge instability without synchronisation (Nature Communications, 2021)",
    "idioma": "en",
    "trecho": (
        "Published: 10 December 2021 [...] "
        "The pedestrian-induced instability of the London Millennium Bridge is a widely used example of Kuramoto synchronisation. "
        "Yet, reviewing observational, experimental, and modelling evidence, we argue that increased coherence of pedestrians’ foot placement is a consequence of, not a cause of the instability. "
        "Instead, uncorrelated pedestrians produce positive feedback, through negative damping on average, that can initiate significant lateral bridge vibration over a wide range of natural frequencies."
    )})

# 0005: saiu da rota aos 37 s e depois se destruiu; sem "engenhosidade"
substituir(5, "gancho", "se destruiu 37 segundos após decolar", "saiu da rota 37 segundos após decolar e se destruiu")
trocar(5, tipos_espanto=["contraintuitivo", "historia_humana"])

# 0006: "has become a case study", não "estudo obrigatório"
substituir(6, "explicacao",
    "O caso virou estudo obrigatório sobre o excesso de confiança de engenheiros que desprezam os relatos de quem usa a máquina.",
    "O caso virou estudo de caso em engenharia de software e ética na computação, como exemplo do excesso de "
    "confiança de engenheiros que desprezam os relatos de quem usa a máquina.")

# 0007: as colunas ajustáveis foram previstas no projeto, não motivadas pela medição de 1999
substituir(7, "explicacao",
    "Por isso, desde a construção do terminal, iniciada em 1991, o prédio se apoia em colunas ajustáveis",
    "Para compensar o afundamento, o terminal, cuja construção começou em 1991, foi projetado sobre colunas ajustáveis")

# 0008: o gancho atribui o argumento aos céticos; tipos ajustados
substituir(8, "gancho",
    "Coreia do Sul, Itália e Rússia gastaram pouco ou nada para se preparar e tiveram tão poucos problemas quanto quem gastou fortunas.",
    "Céticos citam Coreia do Sul, Itália e Rússia, que teriam gastado pouco e não tiveram mais problemas que quem gastou fortunas.")
trocar(8, nota_surpresa=3, tipos_espanto=["contraintuitivo", "historia_humana"])

# 0009: aprovado; nota 3
trocar(9, nota_surpresa=3)

# 0010: a fonte descarta a solda malfeita como origem das trincas
substituir(10, "gancho", "mostrou que o culpado não era a solda, e sim o aço",
    "mostrou que o culpado não era a solda malfeita, e sim o aço")

# 0011: "many", 33 (ou 35) e anéis de aço fora de Toronto
trocar(11, gancho="Muitos engenheiros canadenses usam no mindinho um anel de ferro que lembra suas obrigações. Diz o mito "
                  "que os primeiros saíram das vigas da ponte de Quebec, que desabou em 1907. Mas foram feitos por veteranos de guerra.")
substituir(11, "explicacao", "33 deles eram metalúrgicos mohawks de Kahnawake, segundo a contagem mais citada",
    "33 deles (algumas fontes dizem 35) eram metalúrgicos mohawks de Kahnawake")
substituir(11, "explicacao", "para raspar no papel e servir de lembrete.",
    "para raspar no papel e servir de lembrete. Hoje, fora de Toronto, os anéis são de aço inoxidável.")
acrescentar_trecho(11, 0, "All camps except Toronto have stopped conferring rings made of iron and have switched to stainless steel.")

# 0012: números do Apêndice F de Feynman, sem a pesquisa anônima
trocar(12,
    gancho="A gerência da NASA estimava em 1 em 100 mil o risco de perder um ônibus espacial; os engenheiros, em "
           "cerca de 1 em 100. No fim do programa, foram dois desastres em 135 voos.",
    explicacao=(
        "O físico Richard Feynman fez parte da comissão que investigou o acidente do Challenger, em 1986. Numa "
        "audiência televisionada, ele apertou um pedaço do material dos anéis de vedação dos foguetes laterais num "
        "grampo, mergulhou tudo num copo de água gelada e mostrou que, frio, o material perdia a elasticidade. Nas "
        "entrevistas, achou erros conceituais na gerência. Em testes antigos, alguns desses anéis tinham sido "
        "queimados até um terço da espessura, e os gerentes registraram isso como prova de um \"fator de "
        "segurança\" de 3. Para Feynman, era o contrário: uma peça que trinca, mesmo sem romper, tem fator de "
        "segurança zero, porque está com defeito. No apêndice que escreveu para o relatório, ele anotou a enorme "
        "divergência: as estimativas iam de cerca de 1 em 100, vindas dos engenheiros, a 1 em 100 mil, vindas da "
        "gerência. Este último número equivaleria a lançar uma nave por dia durante 300 anos e perder só uma. Ele "
        "descobriu que 1 em 100 mil era o índice que se queria ter num veículo tripulado, e que as chances das "
        "peças tinham sido deduzidas de trás para a frente. Ao fim do programa, foram dois desastres em 135 voos, "
        "cerca de 1 em 68. A socióloga Diane Vaughan descreveu depois a \"normalização do desvio\": uma prática "
        "insegura passa a parecer normal quando não provoca catástrofe na hora. Feynman resumiu: para uma "
        "tecnologia dar certo, a realidade precisa vir antes das relações públicas, porque a natureza não se deixa "
        "enganar."
    ))
substituir_trecho(12, 0,
    "He then decided to poll the engineers, asking them to write down an anonymous estimate of the odds of shuttle explosion. "
    "Feynman found most estimates fell between 1 in 50 and 1 in 200  (At the time of retirement",
    "The estimates range from roughly 1 in 100 to 1 in 100,000. The higher figures come from the working engineers, and the very low figures from management. [...] "
    "Since 1 part in 100,000 would imply that one could put a Shuttle up each day for 300 years expecting to lose only one [...] "
    "(At the time of retirement")

# 0013: sem causalidade inventada; "muito sobrecarregada"; fechamento definitivo em 1991
substituir(13, "gancho",
    "Só havia outras duas pontes do mesmo tipo, e uma é a Hercílio Luz, em Florianópolis, que escapou por ter mais barras.",
    "Só havia outras duas pontes de desenho parecido, e uma é a Hercílio Luz, em Florianópolis, que tinha o dobro de barras em cada elo.")
substituir(13, "explicacao", "se uma rompesse, a outra ficava com toda a carga",
    "se uma rompesse, a outra ficaria muito sobrecarregada")
substituir(13, "explicacao", "Ela foi fechada em 1991 por corrosão e reaberta em 2019.",
    "Mesmo assim, a corrosão a levou a ser fechada de vez em 1991, e ela só foi reaberta em 2019, depois de uma longa restauração.")

# 0015: sem a anedota do diretor; implosão durante a descida; fonte de Toronto sobre o cisalhamento
substituir(15, "gancho", "A causa foi uma simulação de computador mal feita.",
    "A causa principal foi um erro numa simulação de computador.")
trocar(15, explicacao=(
    "A Sleipner A era uma plataforma do tipo Condeep, com uma base de câmaras de concreto que serviam de lastro e "
    "flutuação. Para encaixar o convés, a base era rebaixada aos poucos no fiorde de Gands, num ritmo de um metro a "
    "cada 20 minutos. Ao chegar a 65 metros, ouviram-se estrondos e o barulho de água entrando: uma parede de uma "
    "das câmaras tinha cedido. A água entrou mais rápido do que as bombas davam conta, e em poucos minutos a "
    "estrutura afundava um metro por minuto. Enquanto ela descia no fiorde, de 210 metros, as câmaras de flutuação "
    "implodiram, e o choque dos destroços contra o fundo causou o tremor. Ninguém se feriu. A investigação do "
    "instituto norueguês SINTEF achou a causa num cálculo por elementos finitos: as tensões nas câmaras tinham sido "
    "subestimadas em 47%, e algumas paredes ficaram finas demais para a pressão da água. Pesquisadores da "
    "Universidade de Toronto, contratados pela firma projetista, concluíram que a parede que cedeu não tinha "
    "armadura transversal porque a análise global subestimou muito o cisalhamento nas pontas dela; o modelo deles "
    "previu a ruptura aos 62 metros. A base foi redesenhada, a plataforma ficou pronta em junho de 1993, e o caso "
    "virou lição para engenheiros que trabalham com simulações numéricas."
))
substituir_trecho(15, 0,
    "After the accident, the project leaders from Norwegian Contractors were brought before the Statoil board, and were expecting severe repercussions. "
    "But the director instead asked the famous question \"Can you make a new one before schedule?\" to which the contractors replied \"Yes we can\". "
    "The new hull was completed before schedule. [...] ",
    "")
acrescentar_trecho(15, 0, "The hull was redesigned after the accident and the Sleipner A Platform was successfully completed in June 1993.")
CANDIDATOS[14]["fontes"].append({
    "url": "https://canadianconsultingengineer.com/features/failure-of-an-offshore-platform",
    "titulo": "Failure of an offshore platform (Canadian Consulting Engineer)",
    "idioma": "en",
    "trecho": (
        "Professors Michael P. Collins and Frank J. Vecchio of the University of Toronto were retained by Dr. techn.Olav Olsen a.s., "
        "the Norwegian structural engineering firm responsible for the design, to develop a better understanding of the factors influencing the failure of the tricell wall. [...] "
        "The first computer run on the Sleipner analytical model predicted that the as-built structure would fail when the applied water pressure on the inner faces of the tricell reached a head of 62 metres [...] "
        "The tricell wall that failed did not contain stirrups because the global finite element analysis performed as part of the design seriously underestimated the magnitude of the shear at the ends of the wall"
    )})

# 0016: a função saiu de uso antes de 2005; o prejuízo veio ao desfazer as posições
trocar(16, gancho="Em 2012, uma corretora dos EUA perdeu mais de 460 milhões de dólares por 45 minutos de ordens "
                  "descontroladas: uma função antiga, fora de uso mas nunca apagada, voltou a funcionar. E-mails automáticos tinham avisado.")
substituir(16, "explicacao", "negociou mais de 397 milhões de ações.",
    "negociou mais de 397 milhões de ações, acumulando posições de bilhões de dólares que, ao serem desfeitas, "
    "deram o prejuízo de mais de 460 milhões.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(6, "explicacao",
    'Muitas mensagens de erro diziam só',
    'Várias mensagens de erro diziam só')
substituir(16, "explicacao",
    'Como ela não devia mais ser usada, ficou lá.',
    'Embora ela não devesse mais ser usada, a empresa a deixou lá.')
