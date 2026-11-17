"""Rodada 2 de palavras viajantes: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-17-palavras_viajantes-01.py"))
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)

LOTE, AREA, TEMA = _base.LOTE, _base.AREA, _base.TEMA
wiki, W = _base.wiki, _base.W
CANDIDATOS = _base.CANDIDATOS


def trocar(n, **campos):
    CANDIDATOS[n - 1].update(campos)


# 0010 ketchup: sem "fermentado", sem "muito citada", grafias históricas
trocar(10,
    explicacao=(
        "Hoje ketchup é sinônimo de molho de tomate, mas a origem da palavra é incerta e tem várias teorias "
        "concorrentes. Uma delas diz que o nome vem do chinês da região de Amoy (Xiamen) e significaria 'molho "
        "de tomate', mas essa explicação é considerada uma etimologia popular. Outra teoria liga a palavra ao "
        "hokkien, falado na região de Fujian, no litoral sul da China. Ali, as formas 'kôe-chiap' e 'kê-chiap' "
        "designavam a salmoura de peixe ou de frutos do mar em conserva, combinando 'comida em conserva' e "
        "'suco'. Se essa teoria estiver certa, o ancestral do ketchup seria algo mais próximo de um caldo de "
        "peixe em conserva do que do molho vermelho das lanchonetes. O nome sobreviveu às trocas de "
        "ingrediente, embora tenha mudado de forma no caminho: em inglês aparece como ketchup (1682), catchup "
        "(1690) e catsup (1730)."
    ),
)
CANDIDATOS[9]["fontes"][0]["trecho"] += " [...] appearing in print as ketchup (1682), catchup (1690), and later as catsup (1730)."

# 0013 algoritmo: "vem do nome"; arithmós; algarismo
trocar(13,
    gancho="'Algoritmo' e 'algarismo' vêm do nome de uma pessoa: o sábio persa al-Khwarizmi, que escreveu sobre os algarismos indianos por volta do ano 825.",
    explicacao=(
        "Por volta do ano 825, o cientista persa al-Khwarizmi escreveu livros sobre o cálculo com os "
        "algarismos indianos, o sistema de numeração posicional que usamos até hoje. No começo do século XII, "
        "esses textos foram traduzidos para o latim. Nas traduções, o nome do autor virou 'Algoritmi' ou "
        "'Alghoarismi', e um dos textos começava com 'Dixit Algoritmi', ou seja, 'assim falou al-Khwarizmi'. "
        "Com o tempo, o nome do autor passou a designar o próprio método de calcular com esses algarismos: em "
        "inglês, 'algorism' já aparece por volta de 1225. No século XV, por influência da palavra grega "
        "arithmós, 'número', a forma latina mudou para 'algorithmus', e por isso dizemos algoritmo, e não "
        "algorismo. A palavra portuguesa 'algarismo' tem a mesma origem: o nome de al-Khwarizmi está nos "
        "dígitos que escrevemos todo dia."
    ),
    fontes=[
        wiki("Algorithm",
             "Around 825 AD, Persian scientist and polymath al-Khwarizmi wrote kitāb al-ḥisāb al-hindī (\"Book of Indian computation\") [...] "
             "In the early 12th century, Latin translations of these texts involving the Hindu–Arabic numeral system and arithmetic appeared [...] "
             "Here, alghoarismi or algoritmi is the Latinization of Al-Khwarizmi's name; the text starts with the phrase Dixit Algoritmi, or \"Thus spoke Al-Khwarizmi\". "
             "The word algorism in English came to mean the use of place-value notation in calculations; it occurs in the Ancrene Wisse from circa 1225. [...] "
             "In the 15th century, under the influence of the Greek word ἀριθμός (arithmos, 'number'; cf. \"arithmetic\"), the Latin word was altered to algorithmus."),
        {"url": "https://pt.wikipedia.org/wiki/Algarismo", "titulo": "Algarismo", "idioma": "pt",
         "trecho": "A palavra \"algarismo\" tem sua origem no nome do famoso matemático Al-Khwarizmi."},
    ],
)

# 0014 robô: ideia de Josef Čapek; robôs da peça eram seres vivos
trocar(14,
    gancho="A palavra 'robô' foi sugerida pelo irmão de Karel Čapek para uma peça de 1920 e vem de 'robota', trabalho forçado. E os robôs da peça nem eram máquinas.",
    explicacao=(
        "A palavra robô ficou conhecida pela peça R.U.R. (Robôs Universais de Rossum), do escritor tcheco Karel "
        "Čapek, publicada em 1920. Mas não foi ele quem a inventou. Čapek contou depois que queria chamar suas "
        "criaturas de 'laboři', de labor, trabalho, mas não gostou da palavra e pediu ajuda ao irmão, o pintor "
        "e escritor Josef Čapek, que sugeriu 'roboti'. A raiz é o tcheco 'robota', trabalho forçado ou serviço "
        "obrigatório, aparentado com o eslavo antigo 'rabota', servidão. E os robôs da peça não eram de metal: "
        "eram pessoas vivas simplificadas, fabricadas numa indústria a partir de um substituto químico do "
        "protoplasma. Eram trabalhadores produzidos em massa, eficientes e sem emoções, que acabam se "
        "revoltando contra os humanos. A ideia de robô como máquina veio depois, mas o nome já trazia a de "
        "trabalho servil."
    ),
    fontes=[wiki("Robot",
        "The term comes from the Czech word robotník ('forced worker'), from robota 'forced labor, compulsory service, drudgery,' [...] "
        "akin to Old Church Slavonic rabota (работа) 'servitude,' [...] "
        "Čapek in his play R.U.R. (Rossum's Universal Robots), published in 1920. "
        "The play begins in a factory that uses a chemical substitute for protoplasm to manufacture living, simplified people called robots. [...] "
        "These mass-produced workers are depicted as efficient but emotionless [...] "
        "incite robots all around the world to rise up against the humans). Karel Čapek himself did not coin the word. "
        "He wrote a short letter in reference to an etymology in the Oxford English Dictionary in which he named his brother, the painter and writer Josef Čapek, as its actual originator. [...] "
        "he had originally wanted to call the creatures laboři ('workers', from Latin labor). However, he did not like the word, and sought advice from his brother Josef, who suggested roboti.")],
)

# 0001 laranja: gancho sem sugerir que o português passou pelo italiano/francês; "provavelmente"
trocar(1,
    gancho="'Laranja' provavelmente nasceu numa língua do sul da Índia e passou pelo sânscrito, pelo persa e pelo árabe. Em italiano e francês o 'n' inicial se perdeu, e daí veio o inglês 'orange'.",
)
CANDIDATOS[0]["explicacao"] = (CANDIDATOS[0]["explicacao"]
    .replace("A origem mais distante da palavra está numa língua dravídica", "A origem mais distante da palavra provavelmente está numa língua dravídica")
    .replace("Foi pelo árabe que a palavra chegou às línguas da Europa, junto com a fruta.", "Foi pelo árabe que a palavra chegou às línguas da Europa."))

# 0003 abacaxi: gancho fiel à fonte; cronologia; Hoyriri
trocar(3,
    gancho="Em inglês, o abacaxi se chama 'pineapple', 'maçã de pinheiro': lembrava uma pinha, e na época 'apple' servia para quase qualquer fruta de árvore desconhecida, firme e redonda.",
    explicacao=(
        "O abacaxi é nativo da América do Sul, onde é cultivado há séculos. Os espanhóis o chamaram de piña, "
        "pela semelhança com a pinha do pinheiro, e Colombo o levou para a Espanha como piña de Indes. Em "
        "inglês, 'pine apple' já existia desde o século XIV, mas designava a própria pinha. Na época, 'apple' "
        "servia para quase qualquer fruta de árvore desconhecida que fosse firme e arredondada. Em 1624, o "
        "explorador John Smith usou 'pine apple' para a fruta tropical, e o nome pegou. Antes disso, em 1568, "
        "a tradução inglesa de um livro do francês André Thevet já mencionava uma fruta cultivada pelos "
        "tupinambás, perto do atual Rio de Janeiro, hoje identificada como o abacaxi. No mesmo livro, ele a "
        "descreve com outra palavra tupi, 'nanas', a mesma raiz de 'ananás'."
    ),
)

# 0004 caju: atenuar a glosa do tupi
CANDIDATOS[3]["explicacao"] = CANDIDATOS[3]["explicacao"].replace(
    "que por sua vez vem da palavra tupi 'acajú', traduzida como 'noz que se produz sozinha'.",
    "que por sua vez vem da palavra tupi 'acajú', de sentido literal incerto (algumas fontes o traduzem como 'noz que se produz sozinha').")

# 0007 azul: "vem do nome"; semipreciosa; árabe, Badakhshan, lazulum = céu
trocar(7,
    gancho="A palavra 'azul' vem do nome de uma pedra: o persa 'lāžward', o lápis-lazúli, que também deu o inglês 'azure'. E 'lápis-lazúli' quer dizer 'pedra do céu'.",
    explicacao=(
        "O lápis-lazúli é uma rocha de um azul intenso, valorizada como pedra semipreciosa desde a Antiguidade "
        "justamente pela cor. Já no 7º milênio a.C. era minerada na região de Badakhshan, no nordeste do atual "
        "Afeganistão. O nome persa da pedra, 'lāžward', costuma ser interpretado como vindo de um nome de lugar "
        "dessa região. Do persa ele passou ao árabe 'lāzaward', que deu origem ao inglês 'azure' e ao latim "
        "medieval 'lazulum', palavra que acabou significando 'céu'. Para não confundir a pedra com o céu, os "
        "europeus passaram a chamá-la de lapis lazuli, a 'pedra do lazulum', ou seja, pedra do céu. A mesma "
        "raiz virou a palavra para a cor em várias línguas, inclusive o português e o espanhol 'azul'. Quando "
        "dizemos que o céu é azul, estamos, pela origem, usando o nome de uma pedra da Ásia Central."
    ),
    fontes=[wiki("Lapis_lazuli",
        "Lapis lazuli (UK: ; US: ) is a deep-blue metamorphic rock used as a semi-precious stone that has been prized since antiquity for its intense color. "
        "Its name originates from the Persian word for the gem, lāžward, and serves as the root for the word for \"blue\" in several languages, including Spanish and Portuguese azul and English azure. [...] "
        "As early as the 7th millennium BC, lapis lazuli was mined in the Sar-i Sang mines, in Shortugai, and in other mines in Badakhshan province in modern northeast Afghanistan. [...] "
        "is commonly interpreted as having an origin in a local place name. "
        "From the Persian, the Arabic لازورد lāzaward is the etymological source of both the English word azure (via Old French azur) and Medieval Latin lazulum, which came to mean 'heaven' or 'sky'. "
        "To disambiguate, lapis lazulī (\"stone of lazulum\") was used to refer to the stone itself",
        "Lapis lazuli")],
)

# Rodada 2: ajuste pontual pedido pelo verificador (aplicado sem nova verificação)
_antes = CANDIDATOS[2]["explicacao"]
CANDIDATOS[2]["explicacao"] = _antes.replace("hoje identificada como o abacaxi", "que hoje se acredita ser o abacaxi")
assert CANDIDATOS[2]["explicacao"] != _antes
