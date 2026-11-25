"""Rodada 2 de Línguas inventadas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-linguas_construidas-01.py"))
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


# 0001: o estudo era com oito crianças; redução de vogais só às vezes; a ressalva de Lindstedt
substituir(1, "gancho", "E elas não falam como os pais: largam regras da gramática que eles seguem.",
    "Num estudo com oito delas, várias largavam regras de gramática que os próprios pais seguiam.")
substituir(1, "explicacao",
    "Criar filhos na língua começou cedo na história do esperanto. Entre os nativos lembrados estão Daniel Bovet, "
    "Nobel de Medicina de 1957, e Petr Ginz, menino morto no Holocausto, cujo desenho da Terra vista da Lua foi "
    "levado a bordo do ônibus espacial Columbia. ",
    "")
substituir(1, "explicacao", "As crianças também reduziam vogais", "Às vezes, as crianças também reduziam vogais")
substituir(1, "explicacao", "usavam os prefixos e sufixos de aspecto verbal que os pais empregavam.",
    "usavam os prefixos e sufixos de aspecto verbal que os pais empregavam. O linguista Jouko Lindstedt, revendo "
    "o mesmo estudo, pondera que essas diferenças parecem vir sobretudo da outra língua materna, das diferenças "
    "entre fala e escrita e da aquisição incompleta, e não de uma \"nativização\" do esperanto; algumas crianças "
    "nativas usam o acusativo normalmente.")
substituir_trecho(1, 0,
    "Raising children in Esperanto occurred early in the history of the language [...] "
    "Also notable are young Holocaust victim Petr Ginz, whose drawing of the planet Earth as viewed from the Moon was carried aboard the Space Shuttle Columbia, and Daniel Bovet, the recipient of the 1957 Nobel Prize in Physiology or Medicine. [...] ",
    "")
acrescentar_trecho(1, 0,
    "Lindstedt, on the other hand, referencing Bergen's study, contends that \"it is difficult to find convincing examples of changes introduced by the process of nativisation. "
    "All examples proposed seem rather to be due to (1) transfers from the children’s other native languages, (2) differences between the spoken and written register of Esperanto and, in some cases, (3) incomplete acquisition.\" [...] "
    "such as the attrition of the accusative, are completely absent from the speech of some native-speaking children.")

# 0002: a maioria das palavras monossílabas, não todas
substituir(2, "explicacao", "mas deformado para ficar com uma sílaba só",
    "mas deformado, porque Schleyer queria que a maioria das palavras tivesse uma sílaba só")

# 0003: a refutação de Sapir-Whorf forte e a opinião de Quijada
substituir(3, "explicacao", " Ao todo, já são quatro versões publicadas.", "")
substituir(3, "explicacao", "segundo a qual a língua influencia o pensamento.",
    "segundo a qual a língua influencia o pensamento. A linguística atual rejeita as versões fortes dessa "
    "hipótese, e o próprio Quijada diz não acreditar que um falante pensaria mais rápido: cada palavra do Ithkuil "
    "exige muito mais reflexão antes de ser dita.")
acrescentar_trecho(3, 0,
    "However, strong forms of the hypothesis, which postulate that language determines thought and not only influences it, have been rejected by mainstream linguistics. "
    "Moreover, in line with this, Quijada has stated he does not believe a speaker would think necessarily any faster because even though Ithkuil is terse, a single word requires a lot more thought before it can be spoken than it would in a natural language.")

# 0004: gancho com o mito alemão; sem cronologia inventada; quem encomendou a língua
trocar(4, gancho="Em Jornada nas Estrelas VI, um líder klingon diz que só se conhece Shakespeare \"no original klingon\", "
    "alusão ao mito alemão de que ele era alemão. Fãs levaram a sério e traduziram Hamlet.")
substituir(4, "explicacao", "Vieram depois Muito Barulho por Nada", "Há também traduções de Muito Barulho por Nada")
substituir(4, "explicacao", "Para o terceiro filme, os produtores quiseram",
    "Para o terceiro filme, o diretor Leonard Nimoy e o produtor Harve Bennett quiseram")

# 0005: "quase só" em klingon; sem a idade de cinco anos
substituir(5, "gancho", "Um pai falou só em klingon com o filho", "Um pai falou com o filho quase só em klingon")
substituir(5, "gancho", "Depois dos cinco anos, o menino parou de responder e o pai desistiu.",
    "Com o tempo, o menino parou de responder, e o pai desistiu.")
substituir(5, "explicacao", "Depois do quinto aniversário do menino, Speers contou que o filho passou a não responder",
    "Com o tempo, Speers contou que o filho passou a não responder")

# 0006: a versão de Tolkien contestada por Dimitra Fimi
trocar(6, gancho="Tolkien dizia que as histórias da Terra-média foram feitas para dar um mundo às línguas élficas. "
    "Os manuscritos contam outra história: a mitologia começou antes da primeira língua.",
    tipos_espanto=["origem_inesperada", "historia_humana", "contraintuitivo"])
substituir(6, "explicacao", "descobriu que muitos queriam mais.",
    "descobriu que muitos queriam mais. A estudiosa Dimitra Fimi contesta essa versão: o poema The Voyage of "
    "Earendel, de setembro de 1914, já esboçava a mitologia antes do primeiro rascunho do qenya, de março de 1915. "
    "Para ela, língua e mito passaram a andar juntos nos anos de faculdade de Tolkien.")
substituir(6, "explicacao",
    " O resultado é uma família inteira de línguas élficas. A mais conhecida, o quenya, tem pronúncia baseada mais "
    "no latim do que no finlandês, embora tenha elementos dos dois. O sindarin recebeu de propósito um caráter "
    "parecido com o do galês.",
    "")
substituir_trecho(6, 0,
    "(I now find that many would have liked more.) [...] "
    "Tolkien based Quenya pronunciation more on Latin than on Finnish, though it has elements derived from both languages. [...] "
    "Tolkien wrote that he gave Sindarin \"a linguistic character very like (though not identical with) British-Welsh",
    "(I now find that many would have liked more.) [...] "
    "The Tolkien scholar and folklorist Dimitra Fimi questions this claim. "
    "In particular, his September 1914 The Voyage of Earendel the Evening Star, based on the Old English poem Crist 1, shows that he was starting to think about a mythology before he started to sketch his first invented Middle-earth language, Qenya, in March 1915. [...] "
    "Tolkien was, rather, in Fimi's view, emphasizing that language and myth \"began to flow together when I was an undergraduate")

# 0014: origem incerta, com as três visões
substituir(14, "explicacao",
    "Hale e colegas acreditam que foi inventado por anciãos lardil e notam que ele tem recursos típicos de jogos de "
    "linguagem do mundo todo, como trocar m e n por cliques nasais.",
    "A origem real é incerta. Hale e colegas acreditam que foi inventado por anciãos lardil, porque ele tem recursos "
    "típicos de jogos de linguagem do mundo todo, como trocar m e n por cliques nasais. Evans e colegas sugerem que "
    "os inventores foram anciãos yangkaal, e Fleming (2017) defende que ele surgiu aos poucos, sem planejamento.")
substituir(14, "explicacao",
    "As palavras eram gritadas ao iniciado numa única sessão da cerimônia warama, enquanto outro falante dava o "
    "equivalente em lardil, mas o domínio costumava exigir várias sessões.",
    "Era ensinado na cerimônia warama, com as palavras gritadas ao iniciado.")
acrescentar_trecho(14, 0,
    "The origin of Damin is unclear. [...] "
    "Evans and colleagues, after studying the mythology of both tribes, speculate that it was the Yangkaal elders who invented Damin and passed it to the Lardil. "
    "According to Fleming (2017), \"the eccentric features of Damin developed in an emergent and unplanned manner [...] "
    "However it was taught during the warama ceremony")

# 0015: o ensaio de Borges é de 1942
substituir(15, "gancho", "Borges respondeu com uma enciclopédia chinesa inventada.",
    "Em 1942, Borges a comparou a uma enciclopédia chinesa inventada.")

# 0016: o casal conversava em esperanto; Orwell defendeu o Basic English antes de criticá-lo
substituir(16, "gancho", "e sofria nas visitas a uma tia em Paris, em cuja casa só se falava esperanto.",
    "e, nas visitas a uma tia em Paris, sofria porque ela e o marido conversavam em esperanto.")
substituir(16, "explicacao", "Orwell, que durante a guerra trabalhou como propagandista na BBC, passou a achar",
    "Orwell chegou a defendê-lo entre 1942 e 1944, mas, depois de trabalhar como propagandista na BBC durante a "
    "guerra, passou a achar")
acrescentar_trecho(16, 1,
    "From 1942 to 1944, George Orwell was a proponent of Basic English, but in 1945, he became critical of universal languages.")

# 0017: troca o enredo pela estreia com esperantistas rindo
substituir(17, "explicacao",
    "A história se passa num vilarejo chamado Nomen Tuum, \"teu nome\" em latim, onde um poço cura doentes e deixa "
    "as pessoas mais bonitas, o que atrai gente vaidosa e corrupta. Súcubos seduzem essas almas e as levam à morte.",
    "Os atores decoraram as falas foneticamente em 10 dias de ensaio, sem ninguém no set para corrigir a pronúncia. "
    "Na estreia, no Festival de São Francisco, em outubro de 1966, um grupo de 50 a 100 esperantistas gritou e riu "
    "da pronúncia do elenco. Em parte pelo diálogo em esperanto, o filme só conseguiu distribuição na França.")
substituir_trecho(17, 0,
    " [...] The film is set in the village of Nomen Tuum (Latin, \"your name\"), which has a well that can heal the sick and make a person more beautiful. "
    "Because of the latter, many conceited or corrupt individuals come to the village for this cosmetic effect. [...] "
    "Along the village, succubi entice the tainted souls who come to Nomen Tuum and lead them to their deaths",
    "")
acrescentar_trecho(17, 0,
    "the actors rehearsed for 10 days to learn their lines phonetically, but no one was present on the set to correct their pronunciation during shooting. [...] "
    "The premiere of Incubus took place at the San Francisco Film Festival on October 26, 1966, where, according to producer Taylor, a group of 50 to 100 Esperanto enthusiasts \"screamed and laughed\" at the actors' poor pronunciation of the language. "
    "Partly because of its Esperanto dialogue, and partly because of the scandal [...] "
    "Taylor and Stevens were unable to find any distribution for the film except in France")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(6, "gancho", "a mitologia começou antes da primeira língua.", "o esboço da mitologia veio antes da primeira língua élfica.")
substituir(14, "explicacao", "e Fleming (2017) defende que ele surgiu aos poucos, sem planejamento.", "e Fleming (2017) defende que seus traços mais estranhos surgiram aos poucos, sem planejamento.")
substituir(16, "explicacao", "mas, depois de trabalhar como propagandista na BBC durante a guerra, passou a achar", "mas, enquanto trabalhava como propagandista na BBC durante a guerra, passou a achar")
