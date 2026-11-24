"""Rodada 2 de Telecomunicações: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-23-telecomunicacoes-01.py"))
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


# 0001: mensagem da rainha com ~16 horas; "ajudou a arruinar"; "homens-chave"
substituir(1, "gancho", "forçou até 2.000 volts por ele e danificou a isolação",
    "forçou até 2.000 volts por ele e ajudou a arruinar a isolação")
substituir(1, "explicacao", "O projeto tinha dois técnicos que não se entendiam.",
    "Dois homens-chave do projeto não se entendiam.")
substituir(1, "explicacao",
    "a mensagem da rainha Vitória ao presidente Buchanan levou 67 minutos para chegar à Terra Nova, e a cópia de confirmação levou 16 horas para voltar à Irlanda",
    "a mensagem de 98 palavras da rainha Vitória ao presidente Buchanan levou cerca de 16 horas para ser transmitida")
substituir_trecho(1, 0,
    "The inaugural message from Queen Victoria took 67 minutes to transmit to Newfoundland, but it took 16 hours for the confirmation copy to be transmitted back to Whitehouse in Valentia.",
    "Queen Victoria's message of 98 words took 16 hours to send.")

# 0003: a escuta contínua veio da emenda de 1912 à lei de 1910, para navios de passageiros
substituir(3, "gancho", "a escuta de rádio 24 horas virou regra nos navios",
    "a escuta de rádio contínua virou exigência nos navios de passageiros")
substituir(3, "explicacao",
    "Depois do desastre, os EUA aprovaram a Lei do Rádio de 1912, que exigiu escuta de rádio 24 horas em todos os navios, e a "
    "primeira Convenção Internacional para a Salvaguarda da Vida Humana no Mar fez a mesma exigência.",
    "Depois do desastre, uma emenda de julho de 1912 a uma lei americana de 1910 passou a exigir dois ou mais operadores e "
    "escuta contínua nos navios de passageiros, e a primeira Convenção Internacional para a Salvaguarda da Vida Humana no "
    "Mar também previu escuta de rádio 24 horas.")
substituir_trecho(3, 0,
    "The United States passed the Radio Act of 1912, which required 24-hour radio watch on all ships in case of an emergency. ",
    "")
CANDIDATOS[2]["fontes"].append(wiki("Wireless_Ship_Act_of_1910",
    "The new law required that all passenger-carrying ocean vessels of any nationality leaving a U.S. port had to be fitted with efficient radio apparatus when carrying 50 or more passengers and crew. [...] "
    "It was approved on June 24, 1910 as Public Law No. 262 [...] "
    "In response to the sinking of the RMS Titanic in April 1912, some of the provisions of the original act were strengthened by an amendment passed on July 23, 1912. [...] "
    "and a requirement that ships carry two or more operators and maintain a continuous watch.",
    nome="Wireless Ship Act of 1910"))

# 0004: sem contradição sobre os 200 m; contatos de rotina; reservadas aos amadores
substituir(4, "explicacao",
    "Ir abaixo disso era tecnicamente "
    "ilegal, mas tolerado, justamente porque as autoridades achavam aquelas ondas inúteis. ", "")
substituir(4, "explicacao", "Em 1923, alguns, com licença especial, fizeram nos 100 metros",
    "Em 1923, alguns, com licença especial para ir abaixo dos 150 metros, fizeram nos 100 metros")
substituir(4, "explicacao",
    "em 1924 muitos já conversavam a 9.600 km ou mais; amadores da Califórnia chegaram a falar com um da Nova Zelândia",
    "em 1924 muitos já faziam contatos de rotina a 9.600 km ou mais; amadores da Califórnia chegaram a trocar mensagens com um da Nova Zelândia")
substituir(4, "explicacao",
    "eram vistas como imprestáveis para longa distância e por isso ficavam com os amadores",
    "eram vistas como imprestáveis para longa distância e, em muitos países, estavam reservadas aos amadores")

# 0005 (aprovado): duas frases reescritas com palavras próprias, sem mudar o sentido
substituir(5, "explicacao", "O anúncio foi saudado como um grande avanço, mas o ceticismo existe desde então.",
    "Muitos celebraram o feito como um marco da ciência, mas as dúvidas surgiram logo e nunca se dissiparam.")
substituir(5, "explicacao",
    "Hoje se sabe, embora Marconi não soubesse, que essa era a pior escolha: "
    "nessa faixa, de dia, a ionosfera absorve demais o sinal.",
    "Marconi ignorava, mas não havia momento pior: nesse comprimento de onda, a ionosfera diurna absorve "
    "o sinal com força e impede o alcance longo.")

# 0010: Antheil "tentou" sincronizar as pianolas
substituir(10, "explicacao", "a experiência de uma obra de vanguarda em que sincronizara várias pianolas com rolos iguais",
    "a experiência de uma obra de vanguarda em que tentara sincronizar várias pianolas com rolos iguais")

# 0012: local incerto; "ficou com pouco do valor"
substituir(12, "explicacao", "e depois virou agente funerário no Kansas.",
    "e depois virou agente funerário no meio-oeste americano (as fontes citam cidades do Kansas e Kansas City, no Missouri).")
substituir(12, "explicacao", "Strowger não enriqueceu com ela: vendeu",
    "Strowger ficou com pouco do valor que a invenção alcançaria: vendeu")

# 0013: sem a causalidade dos fusos horários; acrescenta o registro de 1826
substituir(13, "explicacao",
    "Antes do telefone, os cumprimentos costumavam mencionar a hora do dia, como \"bom dia\". Mas o "
    "aparelho passou a ligar pessoas em fusos horários diferentes, e saudações sem hora ganharam espaço. "
    "As palavras já existiam com outros usos:",
    "O \"hello\" já aparecia por escrito nos EUA desde 1826. As palavras da família tinham outros usos:")
substituir_trecho(13, 0,
    "Before the telephone, verbal greetings often involved a time of day, such as \"good morning\" or \"good afternoon\". "
    "When the telephone began connecting people in different time zones, greetings without time gained popularity. ",
    "")
acrescentar_trecho(13, 0,
    "Hello, with that spelling, was used in publications in the U.S. as early as the 18 January 1826 edition of the Norwich Courier")

# 0015: o PAMOR "buscava" espionar; gancho sem "satélites artificiais"
trocar(15, gancho="Antes dos satélites de comunicação, a Marinha dos EUA usou a Lua como satélite, refletindo nela sinais de "
    "rádio entre Washington e o Havaí. A ideia veio de uma tentativa de espionar radares soviéticos na Lua.")
substituir(15, "explicacao",
    "começou a captar sinais de radares soviéticos que batiam na Lua e voltavam, num programa que virou espionagem oficial.",
    "passou a observar a Lua para tentar interceptar sinais de radares soviéticos que batiam nela e voltavam, num programa "
    "que em menos de um ano virou espionagem oficial da Marinha.")

# 0003: gancho encurtado para caber em 220 caracteres (mesmo sentido da correção pedida)
trocar(3, gancho="Minutos antes de o Titanic bater no iceberg, o único operador de rádio do Californian, parado no gelo ali "
    "perto, desligou o aparelho e foi dormir. Após o naufrágio, a escuta contínua virou regra em navios de passageiros.")
