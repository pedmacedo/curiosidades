"""Rodada 2 de Personagens esquecidos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-personagens_esquecidos-01.py"))
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


# 0001 e 0004: só a nota (0012 e 0015 foram reprovados e ficam como estão)
trocar(1, nota_surpresa=5)
trocar(4, nota_surpresa=3)

# 0002: a contagem de 14 vacinas é de meados dos anos 2000
substituir(2, "gancho", "Das 14 vacinas de rotina do calendário dos EUA, oito saíram",
    "Das 14 vacinas de rotina do calendário americano dos anos 2000, oito saíram")
substituir(2, "explicacao", "Das 14 vacinas recomendadas de rotina no calendário americano, a equipe dele criou oito",
    "Das 14 vacinas recomendadas de rotina no calendário americano na época da morte dele, a equipe dele criou oito")
acrescentar_trecho(2, 0, "In 2007, Anthony S. Fauci wrote in a biographical memoir of Hilleman: [...] "
    "Of the fourteen vaccines currently recommended in the United States, Maurice developed eight.")

# 0006: as 2 mil receitas não saem das 640; cobaia antes dos pacientes, sem primazia exclusiva
substituir(6, "gancho", "e ela foi a primeira pessoa a testar o remédio em si mesma",
    "e ela se ofereceu como cobaia antes dos testes em pacientes")
substituir(6, "explicacao", "reuniu 640 receitas, e até 1971 a equipe tinha avaliado mais de 2 mil delas e preparado 380 extratos de ervas",
    "reuniu 640 receitas num caderno, e até 1971 a equipe tinha avaliado mais de 2 mil receitas tradicionais e preparado 380 extratos de ervas")
substituir(6, "explicacao", "Tu se ofereceu como primeira cobaia humana",
    "Tu se ofereceu como cobaia humana antes dos testes com pacientes")
acrescentar_trecho(6, 0, "She had no bad reactions, so she conducted successful clinical trials with human patients.")

# 0007: o cargo do governador e a descrição do IEEE
substituir(7, "gancho", "o corpo de um governador", "o corpo do governador de Bengala")
substituir(7, "explicacao", "passaram pelo corpo do vice-governador",
    "passaram pelo corpo do governador da província de Bengala")
substituir(7, "explicacao", "pelo IEEE, a maior associação de engenheiros eletricistas, o primeiro desses na Índia",
    "pelo IEEE, a associação internacional de engenheiros eletricistas e eletrônicos, o primeiro reconhecimento "
    "desse tipo a uma descoberta feita na Índia")

# 0008: descalço, não de pijama; com outros dois voluntários; a versão do Carnegie Hero Fund
trocar(8, confianca="consenso_parcial",
    gancho="Garrett Morgan, inventor negro, demonstrava seu capuz antifumaça disfarçado de \"Big Chief Mason\", um "
           "falso chefe indígena. Em 1916, usou o capuz para tirar homens de um túnel cheio de gás sob o lago Erie.")
substituir(8, "explicacao", "Morgan chegou com o irmão Frank, ainda de pijama, trazendo quatro capuzes",
    "Morgan chegou às pressas com o irmão Frank, trazendo quatro capuzes")
substituir(8, "explicacao", "os dois entraram e voltaram carregando homens nas costas; depois outros os seguiram",
    "os dois entraram com outros dois voluntários e ajudaram a tirar sobreviventes; depois outros os seguiram")
substituir(8, "explicacao", "A prefeitura pediu medalhas para outros participantes e o excluiu, o que ele atribuiu ao racismo.",
    "Morgan não recebeu a medalha de heroísmo do Carnegie Hero Fund e atribuiu isso ao racismo. Revendo seus "
    "arquivos, o fundo diz que ele foi indicado e recusado porque o capuz reduzia o risco que corria, e que não há "
    "prova de motivo racial.")
substituir_trecho(8, 0,
    "He and his brother Frank, arrived on the scene still wearing their pajamas and bringing four Smoke Hoods with them. ",
    "He and his brother Frank, arrived on the scene [...] bringing four Smoke Hoods with them. ")
substituir_trecho(8, 0,
    "The mayor, Harry L. Davis, failed to put Garrett Morgan's name on the list of recommended heroes. "
    "City officials requested that the Carnegie Hero Fund Commission issue medals to several of the men involved in the rescue, but excluded Morgan from their request. "
    "Morgan believed that the omission was racially motivated.",
    "Morgan believed that the omission was racially motivated.")
CANDIDATOS[7]["fontes"].append({
    "url": "https://www.carnegiehero.org/behind-the-scenes-shedding-light-on-the-complicated-case-of-black-inventor-garrett-morgan/",
    "titulo": "Behind the Scenes: Shedding Light on the complicated case of Black Inventor Garrett Morgan",
    "idioma": "en",
    "trecho": (
        "The safety of Morgan’s gas hood invention enabled him to go into the gas-filled tunnel multiple times to save men who had collapsed from lack of oxygen. [...] "
        "With several of his smoke hoods in tow, Morgan, who was barefoot, and his brother, Frank Morgan, arrived at the scene and called for volunteers. "
        "Only Frank, Clancy, and another man, Thomas Castleberry, volunteered. [...] "
        "Of the 22 people nominated for the award, in 1917 only four were awarded the Carnegie Medal [...] "
        "Garrett and Frank Morgan were the only two Black men of the 22 nominated, and many recent publications — large and small — have claimed that Garrett Morgan was denied the Carnegie Medal because of his race. "
        "However, there is simply no evidence to support the claim. [...] "
        "it’s likely that the Hero Fund Commission’s rejection of Morgan for the Carnegie Medal was because Morgan’s own invention lessened the risk for those in his party from the “extraordinary degree” that the previous rescuers encountered."
    ),
})

# 0009: a lei de 1932 mirava servidoras casadas
substituir(9, "explicacao",
    "Uma lei alemã de 1932 obrigava mulheres casadas a deixar o emprego; ela escapou por trabalhar como \"colaboradora não remunerada\".",
    "Uma lei alemã de 1932 pressionava mulheres casadas a deixar seus cargos; ela seguiu trabalhando graças ao status "
    "de \"colaboradora não remunerada\".")

# 0010: a data e o motivo da saída da Cruz Vermelha são disputados
substituir(10, "gancho", "e saiu da Cruz Vermelha por separarem o sangue de doadores negros",
    "e criticou a separação do sangue de doadores negros")
substituir(10, "explicacao", "Drew protestou contra a regra, que não tinha base científica, e pediu demissão em 1942.",
    "Drew criticou a regra, que não tinha base científica, e deixou o cargo, voltando para a Universidade Howard. "
    "A saída costuma ser contada como protesto, mas as fontes divergem sobre a data: há relatos que o põem de volta "
    "a Howard ainda em 1941, e outros que falam em 1942.")
CANDIDATOS[9]["fontes"].append({
    "url": "https://prologue.blogs.archives.gov/2023/02/08/dr-charles-drew-a-pioneer-in-blood-transfusions",
    "titulo": "Dr. Charles Drew: A Pioneer in Blood Transfusions (National Archives, Prologue)",
    "idioma": "en",
    "trecho": (
        "In January 1941, the U.S. federal government asked the National Research Council and the American Red Cross to establish a blood program, and Drew became the director of the new American Red Cross Blood Bank. [...] "
        "Drew’s stint with the Red Cross, however, was short-lived. "
        "At the time, the Red Cross segregated blood by race even though they acknowledged there was no scientific foundation for the practice. [...] "
        "Drew resigned and returned to Freedmen’s Hospital and Howard University."
    ),
})
CANDIDATOS[9]["fontes"].append({
    "url": "https://embryo.asu.edu/pages/charles-drew-1904-1950",
    "titulo": "Charles Drew (1904–1950) (The Embryo Project Encyclopedia, Arizona State University)",
    "idioma": "en",
    "trecho": "Drew passed his American Board of Surgery exams in 1941, and returned to Howard University Hospital, which was called Freedman's Hospital at that time, as Chief of Surgery.",
})

# 0013: a primazia é sobre o embrião de Louise Brown
trocar(13, gancho="A enfermeira Jean Purdy foi a primeira a ver se dividir o embrião que viraria Louise Brown, o primeiro bebê "
                  "de proveta. Em 1980, uma placa sobre a técnica omitiu o nome dela, apesar dos protestos de Robert Edwards.")
substituir(13, "explicacao", "Purdy foi a primeira a ver um óvulo fecundado se dividindo e,",
    "Purdy foi a primeira a ver se dividir o óvulo fecundado que daria origem a Louise Brown e,")

# 0014: sem "primeiro laboratório do país"; nota 3
trocar(14, nota_surpresa=3,
    gancho="Pagando a vidraria com um empréstimo pessoal, a médica Marthe Gautier montou um laboratório de cultura de "
           "células e viu, em 1958, o cromossomo a mais da síndrome de Down. A autoria ainda é disputada.")
substituir(14, "explicacao", "montou o primeiro laboratório de cultura de células in vitro do país",
    "montou do zero um laboratório de cultura de células in vitro")

# 0002: data da contagem sem número solto no gancho
substituir(2, "gancho", "Das 14 vacinas de rotina do calendário americano dos anos 2000, oito saíram",
    "Das 14 vacinas de rotina que os EUA recomendavam quando ele morreu, oito saíram")

# 0010: explicação dentro do limite de 250 palavras
substituir(10, "explicacao", "No fim de 1940, antes de os EUA entrarem na guerra, dirigiu", "No fim de 1940, dirigiu")
trocar(2, gancho="Das 14 vacinas de rotina recomendadas nos EUA quando Maurice Hilleman morreu, em 2005, oito saíram da equipe "
                 "dele, um nome que quase ninguém conhece. A da caxumba nasceu do vírus que ele colheu da filha doente, em 1963.")
