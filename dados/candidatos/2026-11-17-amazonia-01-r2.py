"""Rodada 2 da Amazônia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-17-amazonia-01.py"))
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)

LOTE, AREA, TEMA = _base.LOTE, _base.AREA, _base.TEMA
wiki, W, NASA = _base.wiki, _base.W, _base.NASA
CANDIDATOS = _base.CANDIDATOS


def trocar(n, **campos):
    CANDIDATOS[n - 1].update(campos)


# 0001: estimativa de 2015 + ressalva (outras fontes de fósforo); consenso_parcial
trocar(1,
    confianca="consenso_parcial",
    gancho="O Saara ajuda a adubar a Amazônia: segundo uma estimativa da NASA, milhões de toneladas de poeira africana com fósforo caem sobre a floresta todo ano.",
    explicacao=(
        "Os solos da Amazônia são pobres em nutrientes. Quase tudo o que a floresta precisa fica guardado nas "
        "próprias plantas, e folhas caídas se decompõem e são rapidamente reabsorvidas pelas raízes. Mas parte "
        "do fósforo é levada pela chuva para córregos e rios. Uma estimativa publicada em 2015, com dados de "
        "2007 a 2013 do satélite CALIPSO, da NASA, calculou que os ventos tiram do Saara, em média, 182 "
        "milhões de toneladas de poeira por ano, e que cerca de 27,7 milhões caem sobre a bacia amazônica. "
        "Uma fonte importante é a depressão de Bodélé, no Chade, um antigo leito de lago rico em fósforo. Pela "
        "estimativa, a poeira traria cerca de 22 mil toneladas de fósforo por ano, mais ou menos o que a "
        "floresta perde com a chuva e as enchentes. A poeira não é a única fonte: do fósforo que chega pelo ar, "
        "ela responderia por só cerca de 13%, e o resto viria de aerossóis biológicos e de fumaça, inclusive "
        "de queimadas na África."
    ),
    fontes=[
        {"url": NASA, "titulo": "NASA Satellite Reveals How Much Saharan Dust Feeds Amazon's Plants", "idioma": "en",
         "trecho": "Specifically the dust picked up from the Bodélé Depression in Chad, an ancient lake bed where rock minerals composed of dead microorganisms are loaded with phosphorus. [...] "
                   "Instead they are locked up in the plants themselves. [...] "
                   "But some nutrients, including phosphorus, are washed away by rainfall into streams and rivers [...] "
                   "The phosphorus that reaches Amazon soils from Saharan dust, an estimated 22,000 tons per year, is about the same amount as that lost from rain and flooding [...] "
                   "satellite from 2007 though 2013. [...] "
                   "The data show that wind and weather pick up on average 182 million tons of dust each year [...] "
                   "27.7 million tons – enough to fill 104,908 semi trucks – fall to the surface over the Amazon basin."},
        wiki("Saharan_dust",
             "While the relative amount of phosphorus deposition from the atmosphere into the Amazon Basin due to Saharan dust is relatively small (roughly 13%) "
             "compared to non-dust sources, such as biogenic aerosols and smoke particles, it is comparable to the hydrological loss of phosphorus.",
             "Saharan dust"),
        wiki("Amazon_rainforest", "Amazon phosphorus also comes as smoke due to biomass burning in Africa.", "Amazon rainforest"),
    ],
)
# a nota da NASA tem a data de publicação do estudo
CANDIDATOS[0]["fontes"][0]["trecho"] = "A new paper published Feb. 24 in Geophysical Research Letters [...] " + CANDIDATOS[0]["fontes"][0]["trecho"]
CANDIDATOS[0]["explicacao"] = CANDIDATOS[0]["explicacao"].replace(
    "Uma estimativa publicada em 2015,", "Uma estimativa publicada na revista Geophysical Research Letters,")

# 0007: só ~2.700 germinaram; licença sob falso pretexto; fonte nova
trocar(7,
    gancho="Das cerca de 70 mil sementes de seringueira que um inglês levou do Brasil em 1876, só 2.700 germinaram. Elas bastaram para acabar com o monopólio brasileiro da borracha.",
    explicacao=(
        "No século XIX, a Amazônia vivia o ciclo da borracha, com a extração do látex de seringueiras nativas. "
        "Em 1876, o inglês Henry Wickham juntou sementes de seringueira na região de Santarém. Não havia lei "
        "que proibisse exportar sementes, mas era preciso uma licença, e Wickham a conseguiu em Belém sob falso "
        "pretexto: declarou as sementes como 'espécimes acadêmicos', termo usado para material morto. Segundo "
        "o relato que ele próprio fez em 1908, eram cerca de 70 mil. Elas chegaram ao jardim botânico de Kew, em "
        "Londres, e em poucas semanas só 2.700 tinham germinado. Foi o suficiente. Das mudas saíram plantações no "
        "Ceilão, atual Sri Lanka, na Malásia britânica e em outras colônias, que produziam látex com mais "
        "eficiência que a coleta na floresta. A borracha asiática acabou com o monopólio brasileiro, e a "
        "ferrovia Madeira-Mamoré, terminada em 1912, chegou tarde demais."
    ),
    fontes=[
        wiki("Henry_Wickham_(explorer)",
             "He falsely declared 70,000 seeds as \"academic specimens\", a term the Brazilians frequently used to classify dead animals or plants, not viable seeds. "
             "They arrived in London's Kew Gardens on June 15, 1876. Within a few weeks, only 2,700 of the 70,000 smuggled seeds had successfully germinated. "
             "They were sufficient to jump-start widespread cultivation in Southeast Asia. "
             "Thirty years after the fact, Wickham claimed in 1908 that he was responsible for stealing about 70,000 seeds from the rubber-bearing tree, Hevea brasiliensis, in the Santarém area of Brazil in 1876. "
             "At the time, there was no law forbidding the export of seeds, although there was a requirement for an export licence, which Wickham obtained under false pretenses in Belém. [...] "
             "seedlings were dispatched to British Ceylon (now Sri Lanka), British Malaya (now Peninsular Malaysia)",
             "Henry Wickham (explorer)"),
        {"url": W + "Amazon_rubber_cycle", "titulo": "Amazon rubber cycle", "idioma": "en",
         "trecho": "Malaysia, which invested in the planting of rubber trees and in latex extraction technology, was the principal cause of the loss of the Brazilian monopoly [...] "
                   "The Madeira–Mamoré Railroad, finished in 1912, arrived too late. [...] "
                   "These plantations were able to produce latex with greater efficiency"},
    ],
)

# 0008: bioeletricidade
CANDIDATOS[7]["gancho"] = ("Um poraquê amazônico só reconhecido como espécie própria em 2019 dá descargas de até 860 volts: "
                           "é o mais forte gerador de bioeletricidade conhecido.")

# 0009: "pensava não haver", "cerca de mil km", debate; consenso_parcial
trocar(9,
    confianca="consenso_parcial",
    gancho="Na foz do Amazonas, sob a água barrenta onde se pensava não haver recifes, existe um sistema de recifes de cerca de mil quilômetros, que ganhou fama em 2016.",
    explicacao=(
        "Recifes costumam prosperar em águas limpas de plataformas tropicais. Por isso se acreditava que a foz "
        "do Amazonas, com sua pluma carregada de sedimentos, fosse uma lacuna na distribuição de recifes do "
        "Atlântico ocidental. Em abril de 2016, um estudo chamou a atenção do mundo ao descrever ali um sistema "
        "de recifes estimado em cerca de mil quilômetros de extensão e mais de 9.300 quilômetros quadrados. O "
        "segredo é a profundidade: o recife fica abaixo da camada de água doce que o rio despeja sobre o oceano. "
        "A maior parte dele é formada por rodolitos, algas vermelhas que lembram corais, e nas áreas do norte "
        "vivem sobretudo esponjas e animais carnívoros. O tamanho e a vitalidade do recife ainda são debatidos: "
        "um estudo de 2018 sugeriu que ele poderia se estender por até 56 mil quilômetros quadrados, enquanto "
        "outro, de 2022, questionou se ali há mesmo recifes vivos, e foi contestado por outros pesquisadores."
    ),
    fontes=[
        wiki("Amazon_Reef",
             "estimating its length at over 1,000 kilometres (600 miles), and its area as over 9,300 km2 (3,600 mi2). "
             "Publication of its discovery was released in April 2016 [...] "
             "Before the reef's discovery, it was originally believed that the Amazon, with its sediment-rich plume, represented a significant gap in reef distribution across the Western Atlantic, "
             "correlating with the accepted view that corals thrived in clear waters along tropical shelves. "
             "The reef primarily owes its existence to its depth, as it is below the freshwater layer of discharge from the Amazon into the Atlantic Ocean [...] "
             "The majority of the reef is made up of beds of rhodolith, various species of red algae, which superficially resemble coral. [...] "
             "northern areas are populated with sponges and carnivorous species such as hydroids.",
             "Amazon Reef"),
        {"url": "https://www.frontiersin.org/articles/10.3389/fmars.2022.1088956/full",
         "titulo": "The Great Amazon Reef System: A fact (Frontiers in Marine Science, 2022)", "idioma": "en",
         "trecho": "Francini-Filho et al. (2018) suggested that reef habitats could extend for up to 56,000 km2 of the Amazon shelf. [...] "
                   "The vitality of the GARS was also recently questioned by Vale et al. (2022)."},
    ],
)

# 0011: sem a frase global; texto próprio; mecanismo dos Andes
trocar(11,
    explicacao=(
        "Tudo começa no Atlântico, perto da linha do equador. Os ventos alísios empurram para o continente a "
        "umidade que evapora do oceano, e ela despenca como chuva sobre a floresta. As árvores, porém, não "
        "guardam toda essa água: puxam-na pelas raízes e a devolvem ao ar pelas folhas, e o vapor segue viagem "
        "para oeste, num ciclo que se repete pelo caminho. Esse fluxo invisível de umidade ganhou o apelido de "
        "rio voador. Ao chegar perto do Acre, ele esbarra na cordilheira dos Andes, que funciona como um muro, e "
        "faz uma curva para o sul. Passa pelo leste da Bolívia e pelo Paraguai e alcança estados como Mato "
        "Grosso, Mato Grosso do Sul, Minas Gerais, São Paulo e Paraná. É por isso que a floresta, tão longe, "
        "tem a ver com as chuvas fortes e prolongadas do Centro-Oeste, do Sudeste e do Sul do país."
    ),
    fontes=[wiki("Rios_voadores",
        "No Brasil, normalmente estão relacionados ao registro de chuvas intensas e duradouras nas regiões sudeste, sul e centro-oeste. "
        "A umidade evaporada a partir do Oceano Atlântico próximo à linha do equador é transportada pelos ventos alísios, formando nuvens capazes de causar muita precipitação. "
        "Quando chegam sobre a floresta amazônica, essas nuvens geram chuvas. "
        "Posteriormente, as árvores que absorveram essa água sofrem evapotranspiração, devolvendo para a atmosfera a umidade absorvida, na forma de vapor de água. "
        "Dessa forma, o mecanismo é retroalimentado e o ar continua sendo transportado até setores no entorno do estado brasileiro do Acre. "
        "Devido à presença da Cordilheira dos Andes, as massas de ar não conseguem continuar no rumo em que seguiam (oeste), sendo desviadas no sentido sul, "
        "avançando assim sobre o leste da Bolívia e Paraguai, chegando posteriormente aos estados brasileiros de MT, MS, MG, SP, PR, SC, RJ e RS.",
        "Rios voadores", idioma="pt")],
)

# 0013: atribuir a inspiração a Paxton; controvérsia; consenso_parcial
trocar(13,
    confianca="consenso_parcial",
    tipos_espanto=["conexao_inesperada", "mito_desmentido"],
    gancho="Joseph Paxton, que projetou o Palácio de Cristal de Londres, dizia ter se inspirado na folha da vitória-régia. Um especialista em biomimética diz que é lenda.",
    explicacao=(
        "Em 1849, o jardineiro Joseph Paxton conseguiu fazer florescer na Inglaterra a vitória-régia, trazida "
        "da Amazônia, e precisou construir uma estufa nova só para ela. A história famosa diz que a folha, "
        "descrita como 'um feito natural de engenharia', com nervuras que se irradiam do centro ligadas por "
        "nervuras transversais, inspirou a estrutura das estufas de Paxton e, depois, o Palácio de Cristal, "
        "erguido em Londres para a Grande Exposição de 1851. Para mostrar a resistência, ele teria posto a filha "
        "Annie sobre uma folha flutuando. O pesquisador de biomimética Julian Vincent chama isso de 'história "
        "da carochinha'. A folha é plana, flexível e flutua, enquanto o telhado é corrugado e rígido por si só. "
        "E o telhado em ziguezague já existia: foi inventado pelo horticultor John Claudius Loudon, que o "
        "mostrou a Paxton no fim dos anos 1820. Paxton o usou numa estufa bem antes de conhecer a planta."
    ),
    fontes=[
        wiki("Joseph_Paxton",
             "Crystal Palace, which was built in Hyde Park, London to house the Great Exhibition of 1851 [...] "
             "After experimentation, he designed a glass house with a ridge and furrow roof that would be at right angles to the morning and evening sun [...] "
             "The next great building at Chatsworth was built for the first seeds of the Victoria regia lily which had been sent to Kew from the Amazon in 1836. "
             "Although they had germinated and grown they had not flowered and in 1849 a seedling was given to Paxton to try out at Chatsworth. [...] "
             "It continued growing and it became necessary to build a much larger house, the Victoria Regia House. "
             "Inspired by the waterlily's huge leaves – 'a natural feat of engineering' – he found the structure for his conservatory which he tested by floating his daughter Annie on a leaf. "
             "The secret was in the rigidity provided by the radiating ribs connecting with flexible cross-ribs. "
             "Constant experimentation over a number of years led him to devise the glasshouse design that inspired the Crystal Palace.",
             "Joseph Paxton"),
        {"url": "https://www.imeche.org/news/news-article/fairy-stories-and-'magical-thinking'-obscure-origins-of-crystal-palace-and-eiffel-tower",
         "titulo": "Fairy stories and 'magical thinking' obscure origins of Crystal Palace and Eiffel Tower (IMechE, Julian Vincent)", "idioma": "en",
         "trecho": "One of the most robust fairy stories is that the ridge-and-valley roof of the Crystal Palace, designed by Joseph Paxton for the Great Exhibition of 1851, "
                   "took its inspiration from the leaves of a waterlily, Victoria regia. [...] "
                   "The lily leaf is flat, floppy and floats, while the roof is corrugated and independently stiff. "
                   "The ridge-and-valley structure was invented by the horticulturalist John Claudius Loudon [...] "
                   "Loudon showed this to Paxton in the late 1820s."},
    ],
)

# 0014: comparação correta (outros exemplos de cidades)
CANDIDATOS[13]["explicacao"] = CANDIDATOS[13]["explicacao"].replace(
    "mais de mil anos antes de qualquer outra sociedade complexa conhecida na Amazônia.",
    "cerca de mil anos antes de outros achados de cidades antigas na Amazônia, como os de Llanos de Mojos, na Bolívia.")
CANDIDATOS[13]["fontes"].append({
    "url": "https://www.nbcnews.com/science/science-news/lost-cities-oldest-ancient-complex-found-amazon-1000-years-rcna133608",
    "titulo": "Lost cities in the Amazon (NBC News, 2024)", "idioma": "en",
    "trecho": "The newly mapped cities in the Upano Valley are 1,000 years older than the previous findings, including Llanos de Mojos, an Amazonia society in Bolivia"})

# Reprovados na rodada 1 (0003, 0010, 0012) ficam como estão; não voltam ao verificador.

# Rodada 2: ajustes pontuais pedidos pelo verificador (aplicados sem nova verificação)
_antes = CANDIDATOS[0]["explicacao"]
CANDIDATOS[0]["explicacao"] = _antes.replace(
    "Uma estimativa publicada na revista Geophysical Research Letters, com dados de 2007 a 2013 do satélite CALIPSO, da NASA, calculou que",
    "Estudos com dados de 2007 a 2013 do satélite CALIPSO, da NASA, calcularam que")
assert CANDIDATOS[0]["explicacao"] != _antes
CANDIDATOS[12]["gancho"] = ("Conta-se que o Palácio de Cristal de Londres foi inspirado na folha da vitória-régia, cultivada por seu "
                            "projetista, Joseph Paxton. Um especialista em biomimética diz que é lenda.")
_antes = CANDIDATOS[12]["explicacao"]
CANDIDATOS[12]["explicacao"] = (_antes
    .replace("A folha é plana, flexível e flutua", "Segundo ele, a folha é plana, flexível e flutua")
    .replace("Paxton o usou numa estufa bem antes de conhecer a planta.", "Paxton o usou em estufas bem antes de cultivar a planta, em 1849."))
assert CANDIDATOS[12]["explicacao"].count("Segundo ele") == 1 and "em 1849." in CANDIDATOS[12]["explicacao"]
