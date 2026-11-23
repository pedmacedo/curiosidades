"""Rodada 2 de História da matemática: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-historia_matematica-01.py"))
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


# 0001: sem "só no Brasil", sem a data de 1960; Bhaskara cita Sridhara
trocar(1, nota_surpresa=3,
    gancho="A \"fórmula de Bhaskara\" tem esse nome quase só no Brasil. Na maior parte do mundo ela é só a fórmula "
           "quadrática, e o indiano Bhaskara II não foi quem a descobriu: outros chegaram a métodos parecidos antes dele.")
substituir(1, "explicacao", "e o próprio Bhaskara reconhecia isso;", "e o próprio Bhaskara o cita;")
substituir(1, "explicacao",
    "No Brasil, a homenagem a Bhaskara teria se firmado por volta de 1960, e esse nome não se vê em outros países.",
    "O nome Bhaskara é típico do Brasil: na maioria dos países ela é só a fórmula quadrática.")
substituir_trecho(1, 0,
    "No Brasil, por volta de 1960, o nome de Bhaskara passou a designar a fórmula de resolução da equação do 2º grau. "
    "Não se vê essa nomeclatura em outros países, mesmo porque não foi ele quem a descobriu. ",
    "Não se vê essa nomeclatura em outros países, mesmo porque não foi ele quem a descobriu. ")

# 0002: é o cateto maior que não aparece na tabuinha
substituir(2, "explicacao",
    "o lado maior de cada triângulo, que não aparece na tabuinha, é sempre um número",
    "o cateto maior de cada triângulo (o maior dos dois lados que formam o ângulo reto), que não aparece na "
    "tabuinha, é sempre um número")

# 0003: "provavelmente" um estudante
substituir(3, "gancho", "um estudante anotou a raiz quadrada de 2", "provavelmente um estudante anotou a raiz quadrada de 2")

# 0004: "escadinha" em vez de "a mesma soma"; variantes de c. 1730; o erro do 2.301
trocar(4, nota_surpresa=3)
substituir(4, "gancho", "É a mesma soma de potências de 7 de uma charada infantil inglesa.",
    "A mesma escadinha de potências de 7 reaparece, milênios depois, numa charada infantil inglesa.")
substituir(4, "explicacao", "com resultado 19.607;",
    "com resultado 19.607 (o escriba errou uma das parcelas, escrevendo 2.301 em vez de 2.401, mas acertou o total);")
substituir(4, "explicacao",
    "E a cantiga inglesa \"As I was going to St Ives\", registrada num manuscrito de cerca de 1730, fala de um homem "
    "com sete esposas, 49 sacos, 343 gatos e 2.401 filhotes.",
    "E a cantiga inglesa \"As I was going to St Ives\", que já circulava em variantes num manuscrito de cerca de "
    "1730, fala, na versão mais conhecida, de um homem com sete esposas, 49 sacos, 343 gatos e 2.401 filhotes.")
acrescentar_trecho(4, 1,
    "Note that the author of the papyrus listed a wrong value for the fourth power of 7; it should be 2,401, not 2,301. "
    "However, the sum of the powers (19,607) is correct. [...] "
    "The most common modern version is")

# 0005: as condições do quadrado e do triângulo valem só para os touros
substituir(5, "explicacao",
    "brancos e pretos juntos formam um quadrado, e amarelos e malhados juntos formam um triângulo",
    "os touros brancos e pretos juntos formam um quadrado, e os touros amarelos e malhados juntos formam um triângulo")

# 0007: Valentinus Otho (1573) antes de Anthoniszoon (1585)
substituir(7, "gancho", "e a Europa só a achou em 1585.", "e a Europa só a reencontrou no fim do século XVI.")
substituir(7, "explicacao",
    "Na Europa, a mesma fração só foi obtida pelo holandês Adriaan Anthoniszoon, em 1585.",
    "Na Europa, a mesma fração só reapareceu no fim do século XVI, mais de mil anos depois: o alemão Valentinus "
    "Otho a propôs em 1573, e o holandês Adriaan Anthoniszoon chegou a ela em 1585.")
CANDIDATOS[6]["fontes"].append(wiki("Valentinus_Otho",
    "was a German mathematician and astronomer. [...] "
    "In 1573 he came to Wittenberg, proposing to Johannes Praetorius an approximation of pi as",
    nome="Valentinus Otho"))
acrescentar_trecho(7, 0, "the Chinese possessed this most extraordinary fraction over a whole millennium earlier than Europe")

# 0011: o galo é "conta-se"; Napier dizia não ser possível saber a data exata
substituir(11, "explicacao", "Um episódio reforçou os boatos: para achar um ladrão, mandou os criados",
    "Conta-se também que, para achar um ladrão, ele mandou os criados")
substituir(11, "explicacao", "concluía que o fim viria em 1688 ou 1700.",
    "concluía que o fim viria em 1688 ou 1700. Ele dizia que ninguém podia saber a data exata, mas achava que a "
    "Bíblia trazia pistas de sobra porque Deus queria que a Igreja soubesse quando o fim viria.")
substituir(11, "explicacao",
    "A leitura era fortemente antipapal, a ponto de chamar o papa de Anticristo em alguns escritos. ",
    "A leitura era fortemente antipapal. ")
acrescentar_trecho(11, 0,
    "Napier did not believe that people could know the true date of the Apocalypse, but claimed that since the Bible "
    "contained so many clues about the end, God wanted the Church to know when the end was coming.")

# 0012: uma ampliação de um cálculo de 1853, não "duas décadas de cálculos"
substituir(12, "gancho", "depois de duas décadas de cálculos.", "ampliando um cálculo seu de 1853.")

# 0014: a regra dos 50 anos é suposta
substituir(14, "explicacao", "espera-se que cada um se aposente por volta dos 50 anos",
    "diz-se que cada um deve se aposentar por volta dos 50 anos (regra que historiadores não acharam por escrito)")
acrescentar_trecho(14, 0,
    "However, historian Liliane Beaulieu has been critical of the claim. "
    "She reported never having found written affirmation of the rule, and has indicated that there have been exceptions.")

# 0015: simetria contínua; "muitas vezes" em nome de Hilbert; quem barrou e quando
trocar(15, gancho="Emmy Noether provou o teorema que liga cada simetria contínua das leis da física a uma grandeza que se "
    "conserva, como a energia. Na época, dava aulas sem salário nem cargo, muitas vezes em nome de outro professor.")
substituir(15, "explicacao", "A faculdade, porém, barrou a entrada dela como docente.",
    "Já em 1915, porém, filólogos e historiadores da faculdade tinham barrado a entrada dela como docente.")
substituir(15, "explicacao", "com cursos anunciados em nome de Hilbert", "com cursos muitas vezes anunciados em nome de Hilbert")

# 0016: a leitura dos primos não foi refutada
trocar(16, tipos_espanto=["misterio_aberto"])

# ganchos dentro do limite de 220 caracteres
substituir(4, "gancho", "reaparece, milênios depois, numa charada", "reaparece numa charada")
substituir(7, "gancho", "chega mais perto, e a Europa", "é melhor, e a Europa")
