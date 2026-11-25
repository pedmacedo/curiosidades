"""Rodada 2 de Cultura popular brasileira: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-cultura_popular-01.py"))
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


# 0001: fonte da CNN Brasil para a lata azul; Azul no lugar de Nestlé e Visa; nota 3
trocar(1, nota_surpresa=3)
substituir(1, "explicacao", "e marcas azuis, como Nestlé e Visa, adotam o vermelho do Garantido",
    "e marcas azuis, como a companhia aérea Azul, já pintaram o logo de vermelho para o Garantido")
CANDIDATOS[0]["fontes"].append({
    "url": "https://www.cnnbrasil.com.br/pop/caprichoso-e-garantido-veja-marcas-que-mudaram-de-cor-por-rivalidade-entre-os-bois/",
    "titulo": "Caprichoso e Garantido: veja marcas que mudaram de cor por rivalidade entre os bois (CNN Brasil)",
    "idioma": "pt",
    "trecho": "Padrão da Coca-Cola, a lata vermelha tinha resistência dos torcedores do Caprichoso — boi azul e branco — no período do festival. "
              "Como a empresa é parceira dos dois bois, lançou a lata azul como forma de ativação, atenção ao público e proximidade com o festival. [...] "
              "A surpresa se deu pelo lado do boi Garantido. Não só um grande adesivo, mas a logo da Azul também estava pintada em vermelho.",
})

# 0002: o segundo domingo de outubro só virou data fixa em 1901
substituir(2, "explicacao",
    "O Círio acontece em Belém desde 1793, no segundo domingo de outubro, e reúne hoje cerca de dois milhões de pessoas.",
    "O Círio acontece em Belém desde 1793 (no segundo domingo de outubro desde 1901) e reúne hoje cerca de dois milhões de pessoas.")
acrescentar_trecho(2, 0, "Initially held between September and November without a fixed date, the Círio was set for the second Sunday of October in 1901 by Bishop Dom Francisco de Rego Maia.")

# 0004: etimologia como uma das propostas
substituir(4, "explicacao",
    "O nome, segundo a etimologia mais citada, quer dizer algo como \"pele áspera\", ou \"coberto de feridas\".",
    "Uma das etimologias propostas para o nome é \"coberto de feridas\" ou \"pele áspera\".")

# 0005: fogo-fátuo como explicação proposta; influência de mboi; novo gancho
trocar(5, gancho="Boitatá vem do tupi \"coisa de fogo\", com influência de mboi, \"cobra\". Anchieta registrou em 1560 o "
    "baetatá, um facho brilhante que atacava indígenas; mais tarde ele virou a cobra de fogo do folclore.")
substituir(5, "explicacao",
    "A origem do mito é associada ao fogo-fátuo: a matéria orgânica em decomposição solta gases que se inflamam ao "
    "contato com o ar, e a corrente de ar de alguém passando pode mover as chamas, que parecem perseguir a pessoa.",
    "A origem do mito é associada ao fogo-fátuo. A explicação que costuma ser dada é que gases da matéria orgânica em "
    "decomposição se inflamariam ao contato com o ar e que a corrente de ar de alguém passando moveria as chamas, que "
    "pareceriam persegui-lo.")
substituir(5, "explicacao", "O nome junta as palavras tupis mba'e, \"coisa\", e tatá, \"fogo\".",
    "O nome junta as palavras tupis mba'e, \"coisa\", e tatá, \"fogo\". A forma boitatá sofreu influência de mboi, \"cobra\".")
acrescentar_trecho(5, 1, "Boitatá (var. baitatá, batatá) derives from Tupi-Guaraní: mba'e 'thing' or 'agent, cause' + taʼta/tatá 'fire', influenced by mbói 'snake, serpent'.")

# 0007: as cavalhadas fazem parte da festa; quem pode se inscrever; sem a frase dos jesuítas; fonte nova
substituir(7, "gancho", "Depois da festa, dois exércitos", "Na festa, dois exércitos")
substituir(7, "explicacao", "Qualquer morador pode se inscrever no sorteio",
    "Pode se inscrever no sorteio qualquer morador que se julgue em condições de bancar a festa")
substituir(7, "explicacao",
    " No Brasil, esse tipo de encenação foi trazido pelos jesuítas, com autorização da Coroa, para catequizar.", "")
substituir_trecho(7, 1, " [...] No Brasil esta representação dramática foi introduzida, sob autorização da Coroa, pelos jesuítas, com o objetivo de catequizar os gentios e escravos africanos", "")
CANDIDATOS[6]["fontes"].append({
    "url": "https://curtamais.com.br/pirenopolis/2026/04/17/pirenopolis-celebra-200/",
    "titulo": "Pirenópolis celebra 200 anos (Curta Mais, 2026)",
    "idioma": "pt",
    "trecho": "A escolha do Imperador é feita por sorteio. "
              "Todos os pirenopolinos que se julgam em condições de realizar a festa podem se inscrever. "
              "Não há distinção entre ricos e pobres. [...] "
              "Sorteio do novo Imperador e cortejo de retorno •14h – 1º Dia de Cavalhadas",
})

# 0008: "segundo a versão mais contada"; sem Espanha e 14º Regimento; etimologia no fim
trocar(8, gancho="Segundo a versão mais contada, a sombrinha do frevo nasceu como arma: capoeiristas que abriam os blocos "
    "do Recife usavam cabos de guarda-chuva contra rivais e disfarçavam golpes como passos de dança.")
substituir(8, "explicacao", "As mais famosas, a Espanha e a do 14º Regimento de Infantaria, passaram a competir",
    "As bandas rivais passaram a competir")
substituir(8, "explicacao", "Quando a polícia passou a persegui-los, os capoeiras",
    "Segundo a versão mais difundida, quando a polícia passou a persegui-los, os capoeiras")
substituir(8, "explicacao", "Patrimônio Imaterial da Humanidade.",
    "Patrimônio Imaterial da Humanidade. O nome frevo vem de \"frever\", corruptela popular de \"ferver\".")
substituir_trecho(8, 1, "The two most famous bands were the Espanha (meaning Spain), whose conductor was of Spanish origin, and the 14, from the 14th Infantry Regiment. ", "")

# 0010: novo gancho; o relator sem "a fundo"; data do nome discutida
trocar(10, gancho="Apesar do nome, o cordel nordestino não era, por regra, vendido pendurado em cordões, costume de "
    "Portugal. Aqui se falava em folheto; \"cordel\" virou o nome geral no século XX, por influência de estudiosos.")
substituir(10, "explicacao",
    "Quem examinou o caso a fundo foi o historiador Ulpiano Bezerra de Meneses, da USP, relator do pedido",
    "O historiador Ulpiano Bezerra de Meneses, da USP, foi o relator do pedido")
substituir(10, "explicacao",
    "No parecer, ele observa que a exposição em cordinhas não está atestada como norma, e que o nome só virou a "
    "denominação geral a partir dos anos 1950, por influência do pesquisador Raymond Cantel.",
    "No parecer, apoiado no dossiê de pesquisa, ele observa que a exposição em cordinhas não está atestada como norma "
    "e situa nos anos 1950, por influência do pesquisador Raymond Cantel, o momento em que o nome virou a denominação "
    "geral; outros estudiosos datam essa adoção um pouco mais tarde.")
acrescentar_trecho(10, 0, "O Dossiê de Registro é um indispensável e competente repositório de informação e pistas para conhecimento do cordel, repositório de que me vali permanentemente")
acrescentar_trecho(10, 1, "Literatura de cordel também conhecida no Brasil como folheto, literatura popular em verso, ou simplesmente cordel [...] "
    "Nas décadas de 1960 e 1970, a expressão portuguesa \"literatura de cordel\" passou a ser usada no Brasil.")

# 0011: a gorjeta era para quem levasse o menino à polícia
substituir(11, "explicacao",
    "Editais da polícia fixavam multas e até gorjetas para quem levasse à polícia, \"pelo cós das calças\", um "
    "menino negro vendedor de limões de cera.",
    "Editais da polícia fixavam multas e chegavam a prometer gorjeta a qualquer cidadão que levasse à polícia, "
    "\"pelo cós das calças\", um menino negro vendedor de limões de cera.")

# 0012: sem tomar partido sobre a origem do visual de jacaré
substituir(12, "explicacao",
    "No livro \"O Saci\", de 1921, Monteiro Lobato descreve a Cuca apenas com \"cara de jacaré\" e dedos em garra; "
    "foram as adaptações e os ilustradores que a transformaram num jacaré com forma humana.",
    "No livro \"O Saci\", de 1921, Monteiro Lobato lhe deu \"cara de jacaré\" e dedos em garra; os ilustradores e as "
    "adaptações para a TV completaram a imagem do jacaré humanoide que o Brasil conhece.")
acrescentar_trecho(12, 1, "the show runners of the 1952's show interpreted her as a full alligator.")

# 0013: a fogueira veio do solstício; "um dos registros mais antigos"
trocar(13, gancho="A festa junina herdou das festas europeias do solstício de verão a fogueira, mas no Brasil cai em pleno "
    "inverno. No século XVI, o jesuíta Fernão Cardim já via indígenas da Bahia pulando as fogueiras de São João.")
substituir(13, "explicacao", "A primeira menção à festa no Brasil é do jesuíta Fernão Cardim",
    "Um dos registros mais antigos da festa no Brasil é do jesuíta Fernão Cardim")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(7, "explicacao", "Em Pirenópolis, a festa dura doze dias e culmina no Domingo do Divino", "Em Pirenópolis, a festa culmina no Domingo do Divino")
substituir(10, "explicacao", "Antes, poetas e leitores usavam muitos nomes: folheto,", "Os nomes, aliás, variam muito: folheto,")
trocar(8, nota_surpresa=3)
