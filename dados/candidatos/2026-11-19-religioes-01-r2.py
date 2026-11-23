"""Rodada 2 de Religiões e crenças: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-religioes-01.py"))
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


# 0004: sem "fundir o misticismo europeu e o asiático"; o espiritismo de Hugo foi durante o exílio
substituir(4, "explicacao",
    "ele mesmo praticou o espiritismo na ilha de Jersey, de 1852 a 1855, e previu que seria o profeta de uma nova "
    "religião capaz de fundir o misticismo europeu e o asiático.",
    "durante o exílio na ilha de Jersey, de 1852 a 1855, ele mesmo frequentou sessões espíritas e chegou a prever "
    "que seria o profeta de uma nova religião.")
substituir_trecho(4, 0, "and predicted that he would become the prophet of a new religion to merge European and Asian mysticism.",
    "and predicted that he would become the prophet of a new religion")
CANDIDATOS[3]["fontes"].append(wiki("Victor_Hugo",
    "Hugo decided to live in exile after Napoleon III's coup d'état at the end of 1851. [...] "
    "then moved to the Channel Islands, first to Jersey (1852–1855) [...] "
    "He frequented spiritism during his exile (where he participated also in many séances conducted by Madame Delphine de Girardin)",
    nome="Victor Hugo"))

# 0006: "escolhida acima das mulheres dos mundos"; estudiosos modernos; Pseudo-Mateus no Egito; Gálatas "de mulher"
trocar(6, gancho="Maria, mãe de Jesus, é a única mulher chamada pelo nome no Alcorão, que lhe dedica uma surata inteira e "
    "narra um parto diferente do bíblico: sozinha, sob uma tamareira, com um bebê que fala em sua defesa.")
substituir(6, "explicacao", "o Alcorão a apresenta como a maior mulher que já existiu",
    "o Alcorão diz que Deus a escolheu acima das mulheres dos mundos, e muitos comentaristas a consideram a maior "
    "mulher de todos os tempos")
substituir(6, "explicacao", "Estudiosos ligam esses episódios", "Estudiosos modernos ligam esses episódios")
substituir(6, "explicacao", "um milagre da tamareira com Maria aparece no Evangelho do Pseudo-Mateus",
    "um milagre da tamareira com Maria, no Egito, aparece no Evangelho do Pseudo-Mateus")
substituir(6, "explicacao",
    "No Novo Testamento, as principais fontes sobre Maria são os Evangelhos e os Atos dos Apóstolos. O relato mais "
    "antigo, porém, está na carta aos Gálatas, escrita antes dos evangelhos, onde ela aparece apenas como \"uma "
    "mulher\", sem nome.",
    "O texto mais antigo do Novo Testamento a mencioná-la, a carta aos Gálatas, escrita antes dos evangelhos, diz "
    "apenas que Jesus nasceu \"de mulher\", sem dar nome; nos Evangelhos e nos Atos, ela já aparece pelo nome "
    "várias vezes.")
substituir_trecho(6, 0, "explicitly identifies her as the greatest woman to have ever lived. ", "")
acrescentar_trecho(6, 0, "Mary is believed to have been chosen by God, above all \"the women of the worlds\" in Islam [...] "
    "many commentators followed this verse in the absolute sense, and agreed that Mary was the greatest woman of all time. [...] "
    "The Qurʾanic birth narrative closely resembles ones found in Christian apocryphal texts, which modern scholars consider the Qurʾanic account to be dependent on.")
substituir_trecho(6, 1, "She is referred to as \"a woman\" and is not named",
    "She is referred to as \"a woman\" and is not named: \"But when the fullness of time had come, God sent his Son, born of a woman, born under the law\" (Galatians 4:4). "
    "Mary is mentioned several times in the canonical Gospels and the Acts of the Apostles")
acrescentar_trecho(6, 1, "Both Μαρία and Μαριάμ appear in the New Testament.")

# 0007: invenções sem patente, prioridade disputada
trocar(7, gancho="Os shakers, cristãos celibatários dos EUA, chegaram a 6 mil fiéis e ficaram famosos como inventores (a eles "
    "se atribuem, sem patente, a serra circular e o prendedor de roupa). Em 2026, restam só dois.")
substituir(7, "explicacao", "ainda uma máquina de lavar movida a roda e penas de metal.",
    "ainda uma máquina de lavar movida a roda e penas de metal. Como eles não patenteavam o que criavam, é difícil "
    "provar quem veio primeiro, e a autoria da serra circular, por exemplo, é disputada.")
substituir(7, "explicacao", "contrato ou conversão, e muitas vezes acolhiam órfãos.", "contrato ou conversão.")
acrescentar_trecho(7, 0, "Even prolific Shaker inventors like Tabitha Babbit did not patent their inventions before or after putting them into practice, "
    "which has complicated subsequent efforts by 20th-century historians to assign priority.")

# 0010: os 16 eram o acervo, não os expostos na abertura
trocar(10, gancho="O Museu da Bíblia, em Washington, abriu em 2017 exibindo fragmentos dos Manuscritos do Mar Morto. Em 2020, "
    "análises concluíram que os 16 fragmentos do acervo eram falsificações modernas.")
substituir(10, "explicacao", "Em março de 2020, todos os 16 estavam confirmados como falsificações modernas.",
    "Em 2020, o museu informou que todos os 16 fragmentos que havia comprado entre 2009 e 2014 eram falsificações "
    "modernas.")
acrescentar_trecho(10, 0, "The Museum of the Bible is a museum in Washington, D.C., United States [...] "
    "The museum, which opened on November 17, 2017")
acrescentar_trecho(10, 1, "the Museum of the Bible in the United States (also known as Green Collection) reported that all 16 purported "
    "\"Dead Sea Scroll fragments\" they had acquired between 2009 and 2014 were in fact modern forgeries.")

# 0011: de onde vem o sentido de "secreto"; nota 3
trocar(11, nota_surpresa=3)
substituir(11, "explicacao", "e não de algum departamento da Cúria Romana.",
    "e não de algum departamento da Cúria Romana. Em inglês, esse sentido antigo sobrevive em palavras como "
    "\"secretary\", secretário, que indicavam um posto de honra e de confiança.")
acrescentar_trecho(11, 0, "The word secret continues to be used in this older, original sense in the English language, in phrases such as "
    "secret servants, secret cupbearer, or secretary, much like an esteemed position of honour and regard comparable to a VIP.")

# 0012: "cerca de 36 anos"; as estimativas vão de 35 a 42
substituir(12, "gancho", "viveu 36 anos no alto de colunas", "viveu cerca de 36 anos no alto de colunas")
substituir(12, "explicacao", "e lhe sobrava pouco tempo para as devoções.",
    "e lhe sobrava pouco tempo para as devoções. Os relatos divergem sobre quanto tempo ele ficou lá em cima: as "
    "estimativas vão de 35 a 42 anos.")
acrescentar_trecho(12, 0, "Accounts differ with regard to how long Simeon lived upon the pillar, with estimates ranging from 35 to 42 years.")

# 0009: "cópias hebraicas então conhecidas"; as variantes, em geral pequenas
trocar(9, gancho="Um pastor que buscava um animal perdido perto do mar Morto atirou uma pedra e ouviu cerâmica quebrando. Ali "
    "surgiria um rolo de Isaías de cerca de 125 a.C., mil anos mais velho que as cópias hebraicas então conhecidas.")
substituir(9, "explicacao", "Mesmo assim, há mais de 2.600 variantes, entre erros de copista, correções e diferenças em versículos.",
    "Mesmo assim, além de erros de copista e correções, há mais de 2.600 variantes em relação ao texto massorético: "
    "a maioria é pequena, como grafias ou uma palavra trocada, mas algumas envolvem versículos inteiros.")
substituir_trecho(9, 0, "Some variants are significant and include differences in one or more verses",
    "Some variants are significant and include differences in one or more verses or in several words. "
    "Most variants are more minor and include differences of a single word, alternative spellings, plural versus single usage, and changes in the order of words.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(6, "gancho", "que lhe dedica uma surata inteira e narra", "que dá o nome dela a uma surata e narra")
substituir(7, "explicacao", "Como eles não patenteavam o que criavam", "Como muitos inventores shakers não patenteavam o que criavam")
_frase = " Os relatos divergem sobre quanto tempo ele ficou lá em cima: as estimativas vão de 35 a 42 anos."
substituir(12, "explicacao", _frase, "")
substituir(12, "explicacao", "e uma grade em volta.", "e uma grade em volta." + _frase)
