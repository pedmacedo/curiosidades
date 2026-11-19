"""Rodada 2 de Infinito: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-infinito-01.py"))
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


def acrescentar_trecho(n, i_fonte, extra):
    CANDIDATOS[n - 1]["fontes"][i_fonte]["trecho"] += " [...] " + extra


# 0003: explicação com texto próprio
trocar(3, explicacao=(
    "O argumento aparece em Duas Novas Ciências, o último livro científico de Galileu, escrito como um diálogo "
    "entre personagens. De um lado, parece óbvio que os inteiros, que juntam quadrados e não quadrados, são mais "
    "numerosos que os quadrados sozinhos. De outro, dá para casar cada inteiro com o seu quadrado: o 1 com o 1, "
    "o 2 com o 4, o 3 com o 9, e assim por diante, sem que ninguém fique de fora em nenhuma das duas listas. Pelos "
    "pares, os dois conjuntos teriam o mesmo tamanho. Esse casamento termo a termo é o que hoje se chama "
    "correspondência um a um. Galileu não foi o primeiro a usá-lo, mas foi um dos pioneiros a aplicá-lo ao "
    "infinito. Diante do impasse, ele preferiu concluir que comparar tamanhos só faz sentido para quantidades "
    "finitas. No século XIX, Georg Cantor fez o caminho oposto: adotou os pares como a própria definição de "
    "\"mesmo tamanho\". Por esse critério, quadrados e inteiros empatam, e alguns conjuntos infinitos acabam "
    "sendo estritamente maiores que outros."))

# 0004: o paradoxo é só aparente já no gancho; frases próprias; tipos
trocar(4, tipos_espanto=["contraintuitivo", "escala_absurda"],
    gancho="A trombeta de Gabriel é uma forma com volume finito e superfície infinita: em tese caberia nela uma "
           "quantidade limitada de tinta, que no entanto não bastaria para pintar sua parede. O paradoxo é só aparente.")
substituir(4, "explicacao", "O nome remete à ideia cristã de que o arcanjo Gabriel tocará sua trombeta para anunciar o Juízo Final.",
    "O apelido vem do arcanjo Gabriel, que, segundo a tradição cristã, soprará uma trombeta no dia do Juízo Final.")
substituir(4, "explicacao", "O aparente paradoxo entrou numa disputa sobre a natureza do infinito que envolveu pensadores como Thomas Hobbes, John Wallis e Galileu.",
    "Na época, a figura virou argumento num debate acalorado sobre o que é o infinito, com Galileu, Thomas Hobbes e "
    "John Wallis entre os envolvidos.")

# 0007: a crítica da Smithsonian; Casimir simplificado; frase própria
substituir(7, "explicacao", "e espalhou a ideia sem a ressalva.", "e foi descrito pela revista Smithsonian como enganoso.")
substituir(7, "explicacao", "a regularização da série aparece no cálculo da força de Casimir, uma atração entre placas no vácuo,",
    "a regularização da série aparece num cálculo simplificado da força de Casimir, uma atração entre placas no vácuo,")
substituir(7, "explicacao",
    "A fórmula famosa só vale com essa ressalva: o lado esquerdo é o valor obtido por esses métodos, e não a soma de uma série infinita no sentido usual.",
    "Ou seja, o sinal de igual da fórmula famosa tem um sentido especial: indica o valor que esses métodos "
    "associam à série, e não o resultado de somar seus termos um a um.")
acrescentar_trecho(7, 0, "Coverage of this topic in Smithsonian magazine describes the Numberphile video as misleading [...] "
    "computing the Casimir force for a scalar field in one dimension.")

# 0008: sem a frase do ouro; "usa"; frase própria; gancho; tipo
trocar(8, tipos_espanto=["contraintuitivo"])
substituir(8, "gancho", "em um número finito de pedaços, só cinco no mínimo, e remontá-los", "em apenas cinco pedaços e remontá-los")
substituir(8, "explicacao", " E não permite duplicar ouro: nenhum objeto físico pode ser cortado em nuvens infinitas de pontos.", "")
substituir(8, "explicacao", "A prova depende de um axioma da teoria dos conjuntos, o axioma da escolha, que permite",
    "A prova usa um axioma da teoria dos conjuntos, o axioma da escolha, que permite")
substituir(8, "explicacao", "É um paradoxo verídico: contraria a intuição geométrica, mas não é falso nem contraditório.",
    "Os matemáticos o chamam de paradoxo \"verídico\": o resultado parece absurdo, mas está demonstrado e não gera contradição.")

# 0010: a normalidade bastaria, mas não é necessária; frase própria
substituir(10, "explicacao", "A afirmação depende de pi ser um número \"normal\": aquele em que",
    "A afirmação estaria garantida se pi fosse um número \"normal\": aquele em que")
substituir(10, "explicacao",
    "Já para os números que surgem naturalmente, como raiz de 2, pi, e ou o logaritmo de 2, a suspeita é forte, mas ainda não se sabe se são normais. Não foi provado nem que todos os algarismos aparecem infinitas vezes na expansão decimal deles.",
    "Com os números que não foram inventados para isso, como raiz de 2, pi, e ou o logaritmo de 2, quase todo "
    "matemático aposta que são normais, mas ninguém conseguiu demonstrar. Nem mesmo se garante que cada algarismo "
    "volte a aparecer para sempre em suas casas decimais.")
acrescentar_trecho(10, 0, "A normal sequence is disjunctive, but a disjunctive sequence need not be normal.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(4, "explicacao", "A versão do pintor é a mais popular:", "Daí vem o chamado paradoxo do pintor:")
substituir(4, "gancho", "não bastaria para pintar sua parede", "não bastaria para pintar sua superfície")
substituir(8, "gancho", "Um teorema de 1924 diz que dá para cortar", "Um teorema diz que dá para cortar")
substituir(8, "explicacao", "publicado por Stefan Banach e Alfred Tarski a partir de", "publicado por Stefan Banach e Alfred Tarski em 1924, a partir de")
substituir(10, "gancho", "Dizem que toda sequência de números, como sua data de nascimento, aparece em algum lugar de pi.",
    "Dizem que toda sequência de números, de qualquer tamanho, aparece em algum lugar de pi.")
