"""Rodada 2 de Ciência da cozinha: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-ciencia_cozinha-01.py"))
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


# 0002: a cor dos corpos dos pântanos tem explicações concorrentes
trocar(2, confianca="consenso_parcial")
substituir(2, "gancho",
    "também escurece a pele de corpos da Idade do Ferro preservados em pântanos e pode deixar o cabelo deles ruivo. Só que bem devagar.",
    "é apontada como causa da pele escura e do cabelo ruivo de corpos da Idade do Ferro preservados em pântanos. Só que bem devagar.")
substituir(2, "explicacao",
    "Fora da cozinha, a arqueologia reconhece o mesmo processo nos corpos dos pântanos",
    "Fora da cozinha, o mesmo processo é apontado como explicação para o aspecto dos corpos dos pântanos")

# 0003: vale para o aquecimento comum; com aquecimento ultrarrápido não houve degradação (Magoń et al. 2014)
trocar(3, confianca="consenso_parcial",
    gancho="Aquecido do jeito comum, o açúcar não derrete de verdade: ele começa a se decompor justamente quando parece "
           "derreter. Por isso o \"ponto de fusão\" da sacarose muda conforme a rapidez do aquecimento.")
substituir(3, "explicacao", "já não era só sacarose:", "já não era só sacarose, ao menos nas velocidades de aquecimento usuais:")
substituir(3, "explicacao",
    "A pesquisa, anunciada em 2011, saiu em artigos do Journal of Agricultural and Food Chemistry.",
    "A pesquisa, anunciada em 2011, saiu em artigos do Journal of Agricultural and Food Chemistry. Um estudo de 2014, "
    "com outra técnica, confirmou a decomposição durante a fusão em aquecimentos abaixo de 30 kelvins por minuto, mas "
    "não detectou degradação num aquecimento extremo, de 1000 kelvins por segundo.")
CANDIDATOS[2]["fontes"].append({
    "url": "https://trc.nist.gov/ThermoML/10.1016/j.tca.2014.05.029.html",
    "titulo": "Magoń et al. (2014), Heat capacity and transition behavior of sucrose by standard, fast scanning and temperature-modulated calorimetry, Thermochimica Acta 589 (resumo no ThermoML/NIST)",
    "idioma": "en",
    "trecho": "Thermochim. Acta 2014, 589, 183-96 [...] "
        "At heating rates less than 30 K/min, thermal decomposition occurred during melting, while at extreme rate of 1000 K/s, degradation was not observed."})

# 0004: quem saudou a novidade foram as comunidades; 1935 é o lançamento da Automa
trocar(4, nota_surpresa=3)
substituir(4, "gancho",
    "Em 1910, um inventor de Denver vendia panelas de pressão como novidade para quem cozinhava nas montanhas do Colorado.",
    "Em 1910, a panela de pressão de um inventor de Denver foi saudada como invenção maravilhosa nas montanhas do Colorado.")
substituir(4, "explicacao",
    "Em 1935, montanhistas que tentavam escalar o Everest levaram uma panela de pressão para cozinhar lá no alto.",
    "Um modelo lançado em 1935, a Automa, chegou a ser levado por montanhistas que tentavam escalar o Everest, para "
    "cozinhar lá no alto.")

# 0006: o reaquecimento funciona porque os cristais derretem com calor, não por causa do frio
substituir(6, "gancho", "Por isso, aquecê-lo a 60 °C o deixa macio de novo, em parte.",
    "Como os cristais derretem com calor, aquecê-lo a 60 °C o amacia de novo, em parte.")

# 0007: a fonte se contradiz sobre a penetração; sem "só as camadas de fora" e sem o 1 cm
trocar(7, nota_surpresa=3)
substituir(7, "gancho",
    "As ondas aquecem só as camadas de fora, e o miolo de um pedaço grosso esquenta pelo calor que vem delas.",
    "As ondas só alcançam alguns centímetros; o miolo de um pedaço grosso esquenta pelo calor conduzido dessa camada.")
substituir(7, "explicacao",
    "Nessa frequência, as ondas penetram cerca de 1 cm na maioria dos alimentos, e mesmo num alimento homogêneo e úmido o aquecimento só é razoavelmente uniforme nos 25 a 38 mm de fora.",
    "Nessa frequência, mesmo num alimento homogêneo e úmido, o aquecimento só é razoavelmente uniforme nos 25 a 38 mm de fora.")
substituir(7, "explicacao", "aquecido sobretudo pelo calor conduzido dessa camada externa.",
    "aquecido sobretudo pelo calor conduzido da parte de fora.")
substituir_trecho(7, 0,
    "2.45 GHz microwaves can only penetrate approximately 1 cm (0.4 in) into most foods. "
    "The inside portions of thicker foods are mainly heated by heat conducted from the outer 1 cm. [...] ",
    "The inside portions of thicker foods are mainly heated by heat conducted from the outer [...] ")

# 0008: gancho com o feito neozelandês de 2008; Sunions descritas sem "LFS silenciada"
trocar(8, nota_surpresa=3,
    gancho="A cebola faz chorar graças a duas enzimas que agem em sequência quando ela é cortada. Em 2008, bloqueando a "
           "segunda por engenharia genética, cientistas da Nova Zelândia criaram cebolas que não ardem nos olhos.")
substituir(8, "explicacao",
    "Em 2008, um instituto de pesquisa agrícola da Nova Zelândia criou, por modificação genética, cebolas \"sem "
    "lágrimas\" que não produzem a LFS. No início de 2018, a Bayer lançou a primeira safra comercial de cebolas com a "
    "LFS silenciada, as Sunions, fruto de 30 anos de cruzamentos, sem modificação genética. O sabor divide opiniões: "
    "como o processo atrapalha o uso do enxofre pela planta, há quem ache essas cebolas menos saborosas, embora um "
    "estudo sugira que os consumidores preferem as que têm menos LFS.",
    "Em 2008, um instituto de pesquisa agrícola da Nova Zelândia criou, por modificação genética, cebolas \"sem "
    "lágrimas\" que não produzem a LFS. O sabor delas divide opiniões: como o processo atrapalha o uso do enxofre "
    "pela planta, há quem as ache menos saborosas, embora um estudo sugira que os consumidores preferem cebolas com "
    "menos LFS. No início de 2018, a Bayer lançou nos EUA as Sunions, fruto de 30 anos de cruzamentos, sem "
    "modificação genética: a empresa selecionou os bulbos menos pungentes, medindo os compostos voláteis de cada um, e "
    "a cebola fica mais suave e arde menos nos olhos depois de armazenada.")
substituir_trecho(8, 1,
    "In early 2018, Bayer released the first crop yield of commercially available LFS-silenced onions under the name \"Sunions\". "
    "They were the product of 30 years of cross-breeding; genetic modification was not employed.",
    "In early 2018, Bayer released the first crop yield")
CANDIDATOS[7]["fontes"].append({
    "url": "https://www.npr.org/sections/thesalt/2018/02/08/583703262/stop-crying-tear-free-onions-are-here",
    "titulo": "Stop Crying! Tear-Free Onions Are Here (NPR, The Salt)",
    "idioma": "en",
    "trecho": "The Sunion, as the new onion has been named, took 30 years to develop using old-fashioned cross-breeding. "
        "Bayer scientists harvested generations of bulbs and looked for the ones that were the least pungent. "
        "Thanks to the advent of gas chromatography, they could test for and see the exact composition of volatile compounds in each onion. [...] "
        "\"The transition happens in storage,\" says Bayer's senior crop sales manager Lyndon Johnson. [...] "
        "Most onions only get stronger the longer they're stored; Sunions get sweeter, milder, and easier on the eyes."})

# 0010: "may help explain"; sem a frase sem apoio
substituir(10, "gancho", "ajuda a explicar", "explicaria")
substituir(10, "explicacao", "A sinergia pode explicar combinações tradicionais",
    "A sinergia pode ajudar a explicar combinações tradicionais")
substituir(10, "explicacao", " Cozinheiros chegaram a essas duplas por tentativa, muito antes de alguém saber o porquê.", "")

# 0011: a técnica nasceu nos anos 1940 (Peschardt, cerejas artificiais)
trocar(11, nota_surpresa=3,
    gancho="As bolinhas de \"caviar\" de suco que o El Bulli, de Ferran Adrià, tornou famosas vêm de um truque industrial "
           "dos anos 1940, criado para fazer cerejas artificiais: alginato de algas que vira gel no cálcio.")
substituir(11, "explicacao",
    "A técnica foi documentada pela Unilever nos anos 1950 e levada à cozinha de vanguarda",
    "A técnica nasceu na indústria: nos anos 1940, o cientista de alimentos William Peschardt a desenvolveu tentando "
    "fazer cerejas artificiais comestíveis, e a Unilever a documentou nos anos 1950. Décadas depois, ela foi levada à "
    "cozinha de vanguarda")
CANDIDATOS[10]["fontes"].append({
    "url": "https://news.lafayette.edu/2019/07/25/a-food-burst-in-your-mouth",
    "titulo": "A food burst in your mouth (Lafayette College News)",
    "idioma": "en",
    "trecho": "a mixture of sodium alginate, derived from seaweed, and liquid food—tea, maple syrup, honey, hot sauce—is dripped into a bath of calcium chloride solution [...] "
        "The modernist cuisine technique was invented in the 1940s by food scientist William Peschardt, who sought to create edible artificial cherries."})

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(10, "gancho", "Essa sinergia, descoberta em 1957, explicaria", "Essa sinergia explicaria")
substituir(10, "explicacao", "Em 1957, Akira Kuninaka percebeu que o GMP do cogumelo shiitake também dava gosto umami e, mais importante, descobriu o efeito sinérgico:",
    "Em 1957, Akira Kuninaka percebeu que o GMP do cogumelo shiitake também dava gosto umami. Mais importante, ele descobriu o efeito sinérgico:")
