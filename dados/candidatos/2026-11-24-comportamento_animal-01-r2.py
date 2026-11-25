"""Rodada 2 de Comportamento animal: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-comportamento_animal-01.py"))
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)

LOTE, AREA, TEMA = _base.LOTE, _base.AREA, _base.TEMA
wiki = _base.wiki
EPMC = _base.EPMC
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


def acrescentar_fonte(n, fonte):
    CANDIDATOS[n - 1]["fontes"].append(fonte)


# 0001: a reinterpretação de Rutz et al. (2016): dobrar ferramentas é natural da espécie, e Betty era selvagem
substituir(1, "explicacao",
    "E, num estudo da Sociedade Max Planck, corvos montaram ferramentas compostas encaixando de 2 a 4 galhinhos curtos.",
    "Em 2016, uma equipe liderada por Christian Rutz mostrou que dobrar ferramentas faz parte do comportamento "
    "natural da espécie na natureza, e Betty tinha sido capturada na natureza ainda jovem. Isso não apaga o feito, "
    "mas sugere que ela pode ter levado ao arame um movimento que a espécie já conhecia.")
acrescentar_fonte(1, {
    "url": EPMC + "PMC5108972/fullTextXML",
    "titulo": "Tool bending in New Caledonian crows (Royal Society Open Science, 2016, via Europe PMC)",
    "idioma": "en",
    "trecho": "Author for correspondence: Christian Rutz [...] 2016 [...] "
              "Recent field experiments have revealed that tool bending is part of the species' natural behavioural repertoire, providing important context for interpreting Betty's iconic wire-bending feat. [...] "
              "Our findings therefore suggest that Betty, who had been wild-caught as a young bird, may well have expressed behaviours during test trials that were an existing part of her natural repertoire, rather than innovative solutions to an unfamiliar problem."})

# 0002: o comportamento medido é repreender aos gritos (scolding), não atacar
substituir(2, "explicacao", "passaram a atacar a máscara com gritos assim que a viam",
    "passaram a repreender a máscara com gritos assim que a viam")
substituir(2, "explicacao", "também aprenderam a atacar a máscara",
    "também aprenderam a repreender a máscara aos gritos")
substituir(2, "explicacao", "a frequência dos ataques à máscara dobrou",
    "a frequência dos gritos contra a máscara dobrou")

# 0003: os 93% valem para campeiras experientes
substituir(3, "gancho", "93% das que seguiram a dança foram a lugares que já conheciam",
    "93% das veteranas que seguiram a dança foram a lugares já conhecidos")
substituir(3, "explicacao", "a maioria das que acompanharam a dança com atenção ignorou direção e distância",
    "a maioria das campeiras experientes, que já conheciam uma fonte de comida, ignorou direção e distância "
    "mesmo depois de acompanhar a dança com atenção")

# 0004: centenas de batedoras (Seeley e Visscher) e quórum de cerca de 15 a 30
substituir(4, "gancho", "de 20 a 50 batedoras visitam ocos", "centenas de batedoras visitam ocos")
substituir(4, "explicacao", "enquanto de 20 a 50 batedoras procuram ocos adequados",
    "enquanto algumas centenas de batedoras procuram ocos adequados")
substituir(4, "explicacao", "um quórum de 20 a 30 batedoras num mesmo local",
    "um quórum de cerca de 15 a 30 batedoras num mesmo local")
substituir_trecho(4, 0,
    "There they cluster about the queen and send 20 to 50 scout bees out to find suitable new nest locations.",
    "There they cluster about the queen")
acrescentar_fonte(4, {
    "url": "https://www.news.cornell.edu/stories/2006/04/honeybee-decision-making-ability-rivals-any-department-committee",
    "titulo": "How 10,000 bees decide where to go when they fly the coop (Cornell Chronicle, 2006)",
    "idioma": "en",
    "trecho": "Their technique, says Cornell University biologist Thomas Seeley, includes coalition building until a quorum develops. [...] "
              "As soon as 15 or more bees are at any one site, the researchers found, the scouts signal to the waiting bees in the swarm that it's time to warm up their flight muscles in preparation for takeoff. [...] "
              "When a hive gets too crowded, its queen and half the hive will swarm to a nearby tree and quietly wait while several hundred scouts go house hunting."})

# 0005: projéteis (muitos de concreto), e as críticas eram ao relato de 2009
substituir(5, "gancho", "Mais tarde, passou a escondê-las sob montes de feno.",
    "Mais tarde, passou a esconder seus projéteis sob montes de feno.")
substituir(5, "explicacao", "Das 46 pedras recolhidas no período, 35 estavam escondidas.",
    "Dos 46 projéteis recolhidos no período, em geral pedaços de concreto, 35 estavam escondidos.")
substituir(5, "explicacao", "Há quem questione como interpretar esses dados.",
    "Críticos do primeiro relato, de 2009, lembraram que ninguém registrou como surgiram os primeiros montes de "
    "pedras, o que deixa aberta a interpretação.")
substituir_trecho(5, 0, "concerns have been raised over how the findings should be interpreted",
    "concerns have been raised over how the findings should be interpreted – because no detailed data is available on the chimpanzee's behaviour and circumstances at the moment when the first caches were made")
acrescentar_trecho(5, 0, "In 2009 one of us (MO) reported on the projectile related behaviour of the male chimpanzee [...] "
    "The projectiles were chipped off the surface layer of the concrete in the outdoor compound island immediately before they were used. [...] "
    "with two concrete projectiles in his hand [...] "
    "recovered twelve remaining projectiles from the island, all from concrete")

# 0006: sem "primeiro caso em invertebrados"; a classificação como ferramenta é contestada
trocar(6, gancho="Um polvo da Indonésia recolhe metades de casca de coco jogadas fora por humanos, carrega-as por até "
                 "20 metros e depois as monta em volta do corpo como um abrigo portátil.")
substituir(6, "explicacao", "o que o museu chamou de \"uso verdadeiro de ferramenta\".",
    "o que o museu chamou de \"uso verdadeiro de ferramenta\". Nem todos concordam: para outros biólogos, a casca "
    "é só uma proteção contínua contra predadores, e não uma ferramenta.")
acrescentar_fonte(6, wiki("Tool_use_by_animals",
    "The authors of the research article claimed this behaviour falls under the definition of tool use because the shells are carried for later use. "
    "However, this argument remains contested by a number of other biologists who state that the shells actually provide continuous protection from abundant bottom-dwelling predators in their home range.",
    nome="Tool use by animals"))

# 0007: "possuns", começo reescrito com palavras próprias, indícios dos dois lados sobre a flauta
substituir(7, "explicacao",
    "Os pássaros-lira da Austrália são imitadores extraordinários. Reproduzem com fidelidade o canto de outras aves "
    "e o alarido de bandos, além de sons de gambás, coalas e dingos. Há registros deles imitando serrote, motosserra, "
    "motores e alarmes de carro, tiros, obturadores de câmera, cães latindo, bebês chorando, toques de celular e até "
    "a voz humana.",
    "Os pássaros-lira da Austrália são mestres da imitação: copiam com fidelidade o canto de outras aves, o "
    "burburinho de bandos inteiros e até sons de possuns (marsupiais australianos), coalas e dingos. Já foram "
    "gravados reproduzindo serrote, motosserra, motor e alarme de carro, tiro, obturador de câmera, latido, choro "
    "de bebê, toque de celular e voz humana.")
substituir(7, "explicacao",
    "nunca foi comprovada: um grupo de pesquisa não conseguiu provar que a ave tinha sido de estimação.",
    "nunca foi comprovada: um grupo de pesquisa não conseguiu provar que a ave tinha sido de estimação, embora "
    "tenha reconhecido indícios dos dois lados.")
acrescentar_trecho(7, 0, "although they acknowledged compelling evidence on both sides of the argument")

# 0009: 59 era o total da colônia, não os lavadores
substituir(9, "gancho", "Os macacos japoneses que lavavam batata aprenderam devagar, e eram só 59 em 1962.",
    "Os macacos japoneses que lavavam batata aprenderam devagar, e a colônia inteira tinha só 59 em 1962.")
substituir(9, "gancho", "em que um hábito saltaria sozinho para ilhas vizinhas", "em que um hábito saltaria por si só a ilhas vizinhas")

# 0011: "nem todos", "boa parte" do território, e a ressalva de Ferguson (fuga e leopardo)
substituir(11, "gancho", "Muitos cientistas não acreditaram nela.", "Nem todos os cientistas acreditaram nela.")
substituir(11, "explicacao", "mas logo o perderam para comunidades vizinhas mais numerosas",
    "mas logo perderam boa parte dele para comunidades vizinhas mais numerosas")
substituir(11, "explicacao", "em quatro anos todos os machos Kahama foram mortos ou desapareceram.",
    "em quatro anos todos os machos Kahama foram mortos ou desapareceram. O antropólogo Brian Ferguson pondera "
    "que alguns desaparecidos podem ter fugido para outra comunidade, e um leopardo que rondava Gombe na época pode "
    "ter levado parte deles.")
acrescentar_trecho(11, 0,
    "Ferguson argued that at least some of the missing Kahama may have survived the war by escaping the Gombe area, as the Kahama community had friendly contacts with an unstudied chimpanzee community [...] "
    "anthropologist R. Brian Ferguson [...] "
    "the Kasakela quickly gave up much of their new territory. [...] "
    "some research has suggested that the casualties of the war may have been smaller than initially reported, as a leopard had been active in Gombe at the time of the war and might have taken some of the missing chimpanzees.")

# 0012: explicação reescrita com palavras próprias; Van Gogh e Chagall
trocar(12, explicacao=(
    "Em 1995, Watanabe, Sakamoto e Wakita publicaram o experimento. O treino era simples: diante de um quadro de "
    "Picasso, o pombo que bicava ganhava comida; diante de um Monet, bicar era inútil. Depois de praticar com um "
    "punhado de telas, as aves passaram a bicar só os Picasso. O teste de verdade veio com quadros novos: os pombos "
    "continuaram acertando o autor e conseguiram até separar pinturas cubistas, a escola de Picasso, de "
    "impressionistas, a de Monet. Virar as telas de ponta-cabeça atrapalhou a classificação dos Monet, mas não a "
    "das obras cubistas. Num trabalho posterior, Watanabe deu o mesmo treino a pombos e a universitários para "
    "distinguir Van Gogh de Chagall, e o desempenho dos dois grupos foi parecido. O estudo rendeu aos autores o Ig "
    "Nobel de Psicologia de 1995, paródia do Nobel que premia pesquisas que \"primeiro fazem rir e depois fazem "
    "pensar\"."))
acrescentar_trecho(12, 0, "In a later paper, Watanabe showed that if pigeons and human college students undergo the same training, their performance in distinguishing between Van Gogh and Chagall paintings is comparable.")

# 0015: registrar a contestação de linguistas (Pullum, Language Log)
substituir(15, "explicacao", "Para cachorros domésticos, ficam parados onde estavam, observando.",
    "Para cachorros domésticos, ficam parados onde estavam, observando. Já a leitura de que isso seria uma "
    "linguagem é contestada: em 2017, no blog de linguística Language Log, Geoffrey Pullum respondeu com um "
    "\"não\" claro à pergunta \"cães-da-pradaria falam?\".")
acrescentar_fonte(15, {
    "url": "https://languagelog.ldc.upenn.edu/nll/?p=32716",
    "titulo": "On whether prairie dogs can talk (Language Log, 2017)",
    "idioma": "en",
    "trecho": "On whether prairie dogs can talk [...] May 16, 2017 [...] Filed by Geoffrey K. Pullum [...] "
              "Ferris Jabr recently published in the New York Times Magazine an interesting article about the field research of Con Slobodchikoff, professor emeritus of biology at Northern Arizona University, on prairie dog alarm calls. "
              "The article title is \"Can Prairie Dogs Talk?\" [...] "
              "I will provide a clear and explicit answer to Jabr's question. No."})

# 0016: probabilidade, não certeza; "significativamente"
trocar(16, gancho="Elefantes do Quênia distinguem vozes: ao ouvir homens masais, ficam mais propensos a se agrupar em "
                  "defesa e farejar o ar. Vozes de mulheres e meninos masais, pouco perigosos, provocam isso com menos frequência.")
substituir(16, "explicacao", "bem mais propensos", "significativamente mais propensos")
substituir(16, "explicacao", "com frequência bem menor", "com frequência significativamente menor")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(5, "explicacao", "em geral pedaços de concreto", "muitos deles pedaços de concreto")
substituir(11, "explicacao", "e um leopardo que rondava Gombe", "e outros estudos lembram que um leopardo que rondava Gombe")
