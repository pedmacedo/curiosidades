"""Rodada 2 de África antiga e medieval: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-africa_antiga-01.py"))
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


# notas confirmadas pelo verificador (aprovados sem mudança de texto)
trocar(2, nota_surpresa=5)
trocar(7, nota_surpresa=3)

# 0003: tirar a lista das "quatro Candaces" (Malegereabar não era mulher); explicar os "etíopes" = Cuxe
substituir(3, "explicacao",
    " Quatro rainhas ficaram conhecidas no mundo greco-romano como \"as Candaces\": Amanishakheto, "
    "Amanirenas, Nawidemak e Malegereabar.", "")
substituir(3, "explicacao", "cuidava de todo o tesouro dela, e o batiza.",
    "cuidava de todo o tesouro dela, e o batiza. E os \"etíopes\" do texto não são os da Etiópia atual: "
    "gregos e romanos usavam essa palavra para o reino de Cuxe e os povos da Núbia.")
acrescentar_trecho(3, 0,
    "the Greek term “Aithiops” (Αἰθίοψ), a classical translation of \"Cush\" (כּוּשׁ) from the Hebrew Bible, "
    "originally used by Greco-Roman writers to describe the Kingdom of Kush and people of Nubia")

# 0004: a primazia da cruz nas moedas é discutida
substituir(4, "explicacao",
    "trocaram o disco e o crescente pela cruz, apontada como a primeira cruz cristã a aparecer numa moeda.",
    "trocaram o disco e o crescente pela cruz, às vezes apontada como a primeira moeda a exibir a cruz "
    "como símbolo da fé cristã, primazia que é discutida.")

# 0005: a ocupação não terminou em 1937; acordo de 1947 não foi "da ONU"; sem "maior carga aérea"
substituir(5, "explicacao",
    "Quando a ocupação italiana da Etiópia terminou, em 1937, ela foi cortada em três partes",
    "Em 1937, durante a ocupação italiana da Etiópia, ela foi cortada em três partes")
substituir(5, "explicacao", "Num acordo da ONU de 1947", "Num acordo de 1947")
substituir(5, "explicacao",
    "e os três pedaços voaram num Antonov An-124 em abril de 2005, carga descrita como a maior e mais "
    "pesada já transportada por via aérea.",
    "e os três pedaços voaram num Antonov An-124, em três viagens, em abril de 2005.")

# 0006: o carbono-14 confirmou a data dos monges; quem errou foram os estudiosos de fora
trocar(6, gancho="Evangelhos de um mosteiro etíope teriam sido escritos num só dia, com Deus segurando o sol. "
    "O radiocarbono os pôs séculos antes do que criam os estudiosos: talvez o mais antigo livro cristão ilustrado completo.")
substituir(6, "explicacao", "e as do Garima 1, de 530 a 660.",
    "e as do Garima 1, de 530 a 660. Os monges, que sempre situaram os livros perto do ano 500, estavam mais "
    "perto da verdade que os especialistas de fora.")
acrescentar_trecho(6, 0,
    "Monastic tradition holds that the first two were composed close to the year 500, a date supported by recent radiocarbon analysis")

# 0009: o metal veio "sobretudo" da Alemanha
substituir(9, "gancho",
    "Os célebres bronzes do Benin, na Nigéria, são em sua maioria de latão, e o metal veio da Alemanha:",
    "Os bronzes do Benin, na Nigéria, são em sua maioria de latão, e o metal veio sobretudo da Alemanha:")

# 0010: Museu Britânico com ~900 objetos; o MOWAA não abriu (protestos em novembro de 2025)
substituir(10, "gancho", "e o museu feito para exibi-las abriu sem nenhuma.",
    "e o museu feito para exibi-las ficou sem nenhuma.")
substituir(10, "explicacao",
    "Duzentas peças foram para o Museu Britânico, e o resto se espalhou por museus europeus e americanos.",
    "O Museu Britânico ficou com o maior acervo, hoje cerca de 900 objetos, e o resto se espalhou por "
    "coleções particulares e museus da Europa e dos EUA.")
substituir(10, "explicacao", "abriu em 2024 sem nenhum bronze no acervo.",
    "ficou sem nenhum bronze no acervo e desistiu de exibi-los. Na inauguração, em novembro de 2025, "
    "manifestantes que apoiavam o oba interromperam a cerimônia de prévia, e o museu continuou fechado.")
acrescentar_trecho(10, 0,
    "The British Museum in London became home to the largest single holding approximately 900 objects")
CANDIDATOS[9]["fontes"] += [
    wiki("Museum_of_West_African_Art",
        "The Museum of West African Art (MOWAA) is a museum that has been built in Benin City, Nigeria and was planned to open on 11 November 2025. "
        "However, due to political protests during opening ceremony, the museum remains closed until further notice. [...] "
        "The Museum of West African Art was originally intended to display these Benin Bronzes, but none of them are shown and none of them are in the museums depot. "
        "The Bronzes were given to Oba Ewuare II by president Muhammadu Buhari in 2023 before the museum was built. [...] "
        "On 9 November 2025, protests were reported at the museum during preview events ahead of the formal opening. "
        "This led the previews to be curtailed",
        nome="Museum of West African Art"),
    {"url": "https://www.pbs.org/newshour/arts/protesters-disrupt-opening-of-major-west-african-art-museum-in-nigeria",
     "titulo": "Protesters disrupt opening of major West African art museum in Nigeria (PBS NewsHour / AP)",
     "idioma": "en",
     "trecho": "Protesters in Nigeria have disrupted this week's opening of a major museum of West African art, where local disputes over the world-renowned Benin Bronzes have already kept them from being put on display. [...] "
               "They chanted in support of that ruler, the Oba of Benin. [...] "
               "After disputes with the Oba of Benin, plans to display the returned bronzes at the museum were shelved."},
]

# 0011: Frobenius viu uma só cabeça; nota 3
trocar(11, nota_surpresa=3)
substituir(11, "gancho",
    "Diante das cabeças de metal realistas de Ife, na Nigéria, o etnólogo alemão Leo Frobenius disse que eram obra",
    "Diante de uma cabeça de metal realista achada em Ife, na Nigéria, o etnólogo alemão Leo Frobenius disse que era obra")

# 0016: os 350 mil vêm dos organizadores; Charlie English suspeitou de exagero
trocar(16, gancho="Em 2012 e 2013, com jihadistas ocupando Tombuctu, no Mali, moradores tiraram da cidade, segundo os "
    "organizadores, cerca de 350 mil manuscritos em baús, por terra e pelo Níger. Muitos mensageiros eram adolescentes.")
substituir(16, "explicacao", "Em Bamako, os textos salvos enfrentaram outro inimigo: o mofo e a umidade.",
    "Em Bamako, os textos salvos enfrentaram outro inimigo: o mofo e a umidade. O número vem dos próprios "
    "organizadores. Em 2017, o jornalista britânico Charlie English, no livro The Book Smugglers of Timbuktu, "
    "admitiu que o total resgatado pode ter sido menor e levantou a suspeita de que a escala da operação foi "
    "exagerada.")
acrescentar_trecho(16, 0,
    "In 2017, journalist Charlie English published The Book Smugglers of Timbuktu")
CANDIDATOS[15]["fontes"] += [
    {"url": "https://qantara.de/en/article/book-review-charlie-english%CA%B9s-book-smugglers-timbuktu-myths-and-heroes",
     "titulo": "Of myths and heroes: book review of Charlie English's The Book Smugglers of Timbuktu (Qantara.de)",
     "idioma": "en",
     "trecho": "At the very end of the book, English admits that the real number of rescued manuscripts may actually have been smaller than claimed."},
    {"url": "https://ilab.org/article/book-review-the-book-smugglers-of-timbuktu-by-charlie-english",
     "titulo": "Book Review - The Book Smugglers of Timbuktu by Charlie English (ILAB)",
     "idioma": "en",
     "trecho": "he became increasingly suspicious that the scale of the rescue operation had been exaggerated by the heroes of his tale"},
]
