"""Rodada 2 de Fungos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-fungos-01.py"))
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


# 0002: toneladas métricas, idade como estimativa, Posidonia com 200 km², Michigan é A. gallica
trocar(2, nota_surpresa=3)
substituir(2, "gancho", "pode pesar até 35 mil toneladas e teria uns 8 mil anos.",
    "pode pesar cerca de 31.500 toneladas e, segundo estimativas, ter até 8 mil anos.")
substituir(2, "explicacao", "Só no outono ele põe para fora os cogumelos.", "No outono, ele põe para fora os cogumelos.")
substituir(2, "explicacao",
    "Se for tratado como um só organismo, em área ele só tem um rival conhecido: uma colônia de capim "
    "marinho, a Posidonia australis, no fundo do mar da Austrália.",
    "Se for tratado como um só organismo, em área ele só fica atrás de uma colônia de capim marinho, a "
    "Posidonia australis, que cobre 200 km² do fundo do mar da Austrália.")
substituir(2, "explicacao",
    "Em Michigan, uma análise genética mostrou que outro indivíduo da espécie, com uns 2.500 anos, ocupa 37 "
    "hectares e pesa cerca de 440 toneladas, o equivalente a três baleias-azuis. Ele descende de esporos de um "
    "fungo do Ontário, no Canadá.",
    "Em Michigan, um indivíduo de outra espécie do mesmo gênero, a Armillaria gallica, tem cerca de 2.500 "
    "anos e 400 toneladas, segundo estudos recentes. Apelidado de \"fungo gigantesco\", virou atração "
    "turística e inspira um festival anual na cidade de Crystal Falls.")
substituir(2, "explicacao", "os pinheiros jovens, de até 10 anos,", "as coníferas jovens, de até 10 anos,")
substituir_trecho(2, 0, "weighs as much as 35,000 tons [...] ", "weighs as much as 35,000 tons (about 31,500 tonnes) [...] ")
substituir_trecho(2, 0, "only knowingly rivalled by a colony of Posidonia australis on the Australian seabed [...] ",
    "only knowingly rivalled by a colony of Posidonia australis on the Australian seabed that measures 200 square kilometres [...] ")
substituir_trecho(2, 0,
    "a 2,500-year old specimen of Armillaria ostoyae in northern Michigan, United States originated from spores of a parent fungus in Ontario, Canada, "
    "then grew over millennia into the 21st century to a mass of 440 tons (4 × 105 kg), making it the equivalent in weight of 3 blue whales. [...] ",
    "")
substituir_trecho(2, 0,
    "A spatial genetic analysis estimated that an individual specimen growing over 91 acres (37 ha) in northern Michigan weighs 440 tons [...] ",
    "")
CANDIDATOS[1]["fontes"].append(wiki("Armillaria_gallica",
    "This individual is popularly known as the \"humongous fungus\", and is a tourist attraction and inspiration for an annual mushroom-themed festival in Crystal Falls. "
    "Recent studies have revised the fungus's age to 2,500 years and its size to about 400 tonnes",
    nome="Armillaria gallica"))

# 0004: o estudo de 2012 data os genes no fim do Carbonífero (destaque do DOE)
substituir(4, "explicacao",
    "Um estudo de 2012 na revista Science, que reconstruiu a história das enzimas comparando 31 genomas de fungos, "
    "reforçou a ideia ao sugerir que os fungos basidiomicetos com essas enzimas surgiram no Permiano, o período seguinte.",
    "Um estudo de 2012 na revista Science, que comparou 31 genomas de fungos, reforçou a ideia ao datar o "
    "surgimento dos genes que quebram a lignina por volta do fim do Carbonífero.")
substituir_trecho(4, 0,
    "Genetic analysis of basidiomycete fungi, which have enzymes capable of breaking down lignin, supports this theory by suggesting this fungi evolved in the Permian. ",
    "[...] ")
CANDIDATOS[3]["fontes"].append({
    "url": "https://science.osti.gov/ber/Highlights/2012/BER-2012-06-a",
    "titulo": "A Fungal End to Coal in the Carboniferous Period? (DOE Office of Science, destaque de pesquisa, 2012)",
    "idioma": "en",
    "trecho": "has proposed that a species of fungus, first appearing at about the end of the Carboniferous, could more efficiently break down dead plant matter, "
              "possibly leading to the decline in coal formation. [...] "
              "By comparing the genomic sequences of 31 fungi, including 12 sequenced for this study, "
              "the researchers showed that genes able to degrade lignin first appeared at the end of this period. [...] "
              "D. Floudas, et.al. (2012) “The Paleozoic Origin of Enzymatic Lignin Decomposition Reconstructed from 31 Fungal Genomes”, Science"})

# 0007: "dadas como extintas"; falência do coração
substituir(7, "gancho", "90 delas extintas na natureza", "90 delas dadas como extintas na natureza")
substituir(7, "explicacao", "leva à parada do coração", "leva à falência do coração")

# 0008: "entre as maiores acelerações"; ciclo é do Pilobolus; pressão sem acúmulo fora do normal
substituir(8, "gancho", "em aceleração, os voos mais rápidos já medidos na natureza.",
    "entre as maiores acelerações já medidas em seres vivos.")
substituir(8, "explicacao", "O ciclo desses fungos passa pelo intestino de herbívoros.",
    "O ciclo do Pilobolus, um desses fungos, passa pelo intestino de herbívoros.")
substituir(8, "explicacao", "em níveis comuns nos fungos, sem nenhum mecanismo especial.",
    "em níveis comuns nas células dos fungos, sem precisar acumular sais ou açúcares em concentrações fora do normal.")

# 0010: o alcance do terceiro parceiro ainda é discutido; papel das leveduras com cautela
substituir(10, "gancho", "Desde 1867, o líquen é descrito como uma parceria", "Desde 1867, propõe-se que o líquen seja uma parceria")
substituir(10, "explicacao", "Parece que muitos liquens, provavelmente a maioria, abrigam esse terceiro parceiro.",
    "Depois, leveduras desse tipo foram achadas em liquens de outras partes do mundo, mas ainda se discute em "
    "quantas espécies elas aparecem.")
substituir(10, "explicacao", "As leveduras formam a camada externa do líquen e podem influir na sua forma,",
    "As leveduras estariam ligadas à formação da camada externa do líquen e talvez à sua forma,")
acrescentar_trecho(10, 1, "The additional fungal component has also been found in lichens around the world.")

# 0012: sem "fogo-fátuo"; Aristóteles no século 4 a.C.
substituir(12, "explicacao", "A luz é o \"fogo-fátuo\" das florestas, em inglês \"foxfire\": o brilho verde-azulado",
    "A luz é o que em inglês se chama \"foxfire\": o brilho verde-azulado")
substituir(12, "explicacao", "Aristóteles já falava, em 382 a.C., de uma luz que",
    "Aristóteles já falava, no século IV a.C., de uma luz que")

# 0013: só o poliporo-da-bétula ia em tiras de couro; "orelha-de-pau"; fonte do museu
substituir(13, "gancho", "levava dois fungos presos em tiras de couro: um para acender fogo e outro com uma substância tóxica",
    "levava dois fungos: um para acender fogo e outro, preso em tiras de couro, com uma substância tóxica")
substituir(13, "explicacao", "dois tipos de cogumelos-orelha, os poliporos, atravessados por tiras de couro.",
    "dois tipos de orelha-de-pau (fungos do grupo dos poliporos).")
substituir(13, "explicacao", "O outro era o poliporo-da-bétula, que cresce quase só nessa árvore.",
    "O outro, em pedaços atravessados por tiras de couro, era o poliporo-da-bétula, que cresce quase só nessa árvore.")
substituir_trecho(13, 0, "two species of polypore mushrooms with leather strings through them. ", "two species of polypore mushrooms [...] ")
CANDIDATOS[12]["fontes"].append({
    "url": "https://www.iceman.it/en/oetzi/equipment",
    "titulo": "Ötzi's equipment (Museu de Arqueologia do Tirol do Sul)",
    "idioma": "en",
    "trecho": "Also part of Ötzi’s equipment were two pieces of birch polypore (birch fungus), which were threaded onto hide strips. "
              "It is assumed that the fungus had therapeutic purposes, since it was used medicinally as recently as the 20th century."})

# 0015: sem "pediu desculpas"; leitura por terceiros era a regra; retirada pedia mais trabalho
trocar(15, nota_surpresa=3,
    gancho="A criadora de Pedro Coelho, Beatrix Potter, estudou a germinação de esporos de cogumelos. Em 1897, quando "
           "mulheres nem podiam ser membros da Sociedade Lineana, um botânico apresentou o trabalho dela lá.")
substituir(15, "explicacao", "Mas o diretor de Kew a rejeitou por ser mulher e amadora.",
    "Mas o diretor de Kew a desprezou, segundo biógrafos, por ser mulher e amadora.")
substituir(15, "explicacao", "porque mulheres não podiam assistir às sessões nem ler os próprios trabalhos.",
    "porque na época os trabalhos eram lidos por outra pessoa e mulheres só foram aceitas como membros da "
    "sociedade em 1905.")
substituir(15, "explicacao", "Depois, ela retirou o artigo, ao perceber que algumas amostras estavam contaminadas.",
    "Dias depois, ela retirou o artigo, que segundo os avaliadores precisava de mais trabalho antes de ser "
    "impresso, e nunca o reapresentou.")
substituir(15, "explicacao",
    "Em 1997, a Sociedade Lineana pediu desculpas póstumas pelo sexismo com que tratou a pesquisa dela.",
    "Em 1997, o secretário-executivo da sociedade admitiu a um jornal que ela tinha sido \"tratada com "
    "desdém\" pelos membros da época.")
substituir_trecho(15, 0,
    "It was introduced by Massee because, as a woman, Potter could neither attend proceedings nor read her paper. "
    "She subsequently withdrew it, realising that some of her samples were contaminated [...] ",
    "[...] ")
substituir_trecho(15, 0,
    " [...] In 1997, the Linnean Society issued a posthumous apology to Potter for the sexism displayed in its handling of her research.",
    "")
CANDIDATOS[14]["fontes"].insert(0, {
    "url": "https://www.linnean.org/the-society/history-of-science/beatrix-potter-the-tale-of-the-linnean-society",
    "titulo": "Beatrix Potter: the tale of the Linnean Society (Linnean Society of London)",
    "idioma": "en",
    "trecho": "Dr John Marsden, Executive Secretary of the Linnean Society, founded in 1788, acknowledged Potter had suffered an injustice "
              "at the hands of his early 20th century predecessors: \"She was treated scurvily by members of the society. [...] "
              "From the article 'Beatrix Potter Boils Squirrels', 16 February 1997, The Sunday Times [...] "
              "While it is frustratingly true that women were not admitted as Fellows (or members) of the Society until 1905 "
              "(which was unfortunately the case for many learned societies at the time), the accepted practice was that papers were always read by someone other than the author. [...] "
              "In fact, it was Massee who read her paper at the Linnean Society. [...] "
              "The Society’s hand-written records show that her paper (designated No. 2978) was “read and discussed” on 1 April 1897 "
              "but then withdrawn, by Potter, on 8 April, and never resubmitted. [...] "
              "My paper was read at the Linnean Society and ‘well received’ according to Mr. Massee, but they say it requires more work in it before it is printed."})

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(2, "explicacao", "as coníferas jovens, de até 10 anos, são os mais vulneráveis", "as coníferas jovens, de até 10 anos, são as mais vulneráveis")
substituir(2, "gancho", "pode pesar cerca de 31.500 toneladas", "pode pesar até cerca de 31.500 toneladas")
substituir(7, "explicacao", "e certas populações se adaptaram depois de uma mortandade inicial", "e algumas espécies se adaptaram depois de uma mortandade inicial")
substituir(8, "explicacao", "O cavalo come o capim com o esporo grudado, o esporo atravessa o tubo digestivo sem germinar",
    "O cavalo come o capim com o pacote de esporos grudado, e esse pacote atravessa o tubo digestivo sem germinar")
