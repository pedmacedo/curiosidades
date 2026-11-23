"""Rodada 2 de Mitologia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-mitologia-01.py"))
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


# 0001: o relato de Empédocles não está em nenhum texto antigo (está em Abel)
substituir(1, "gancho", "que não aparece em nenhum registro.", "que não aparece em nenhum texto antigo.")

# 0002: "às vezes" entalhavam (a fonte diz "occasionally")
substituir(2, "gancho", "e comerciantes entalhavam neles cabeças de cobra para vender.",
    "e comerciantes às vezes entalhavam neles cabeças de cobra para vender.")

# 0004: a ligação com Lucy Westenra é especulação
substituir(4, "explicacao",
    "Estudiosos sugerem que Bram Stoker soube do caso pelos jornais e se baseou nele para criar a personagem Lucy Westenra, de \"Drácula\".",
    "Alguns estudiosos especulam, sem prova direta, que Bram Stoker soube do caso pelos jornais e se inspirou nele para criar a personagem Lucy Westenra, de \"Drácula\".")

# 0006: "tinha visto antes", não "tinha acabado de ver"
substituir(6, "gancho", "tinha acabado de ver o filme de terror \"Species\"", "tinha visto antes o filme de terror \"Species\"")

# 0008: houve quem notasse a semelhança antes de 1859
substituir(8, "gancho", "veneraram um santo que era, sem que soubessem, o Buda.", "veneraram um santo que era, na prática, o Buda.")
substituir(8, "explicacao", "Só em 1859-1860 pesquisadores europeus estabeleceram",
    "Houve quem notasse a semelhança antes, como um manuscrito de Marco Polo e o cronista português Diogo do Couto, "
    "mas só em 1859-1860 pesquisadores europeus estabeleceram")
acrescentar_trecho(8, 0,
    "One of the Marco Polo manuscripts notes the remarkable similarity between the tale of \"Sergamoni Borcan\" (i.e. Sakyamuni Burkhan; the name that Polo recorded the Mongols using for the Buddha) and St. Josaphat [...] "
    "e a identificação, por Diogo do Couto (1542–1616), de Josaphate com o Buda.")

# 0010: Donnelly não foi o primeiro a tomar a Atlântida por real; nota 3
trocar(10, nota_surpresa=3)
substituir(10, "gancho", "Quem a transformou em civilização real foi um autor amador americano, num livro de 1882.",
    "A ideia de uma supercivilização real perdida deve muito a um autor amador, num livro de 1882.")
substituir(10, "explicacao",
    "O mito moderno nasceu no século XIX, quando estudiosos amadores leram Platão como relato histórico.",
    "Já na Antiguidade houve quem a tomasse por real, como Estrabão e Posidônio, e a partir do século XVI muitos a "
    "ligaram à América. Mas a versão popular de hoje vem do século XIX, quando estudiosos amadores leram Platão como "
    "relato histórico.")
acrescentar_trecho(10, 0,
    "Other ancient historians and philosophers who believed in the existence of Atlantis were Strabo and Posidonius. [...] "
    "modern interpretations regarding Atlantis are an amalgamation of diverse, speculative movements that began in the sixteenth century, when scholars began to identify Atlantis with the New World.")

# 0014: o canto enganador é tradição; a perna única não é atribuída a Cascudo
substituir(14, "gancho", "Para Câmara Cascudo, a perna única do Saci pode vir das aves, que muitas vezes pousam num pé só.",
    "Câmara Cascudo via nele um antigo mito de ave, e a perna única pode vir daí: aves muitas vezes pousam num pé só.")
substituir(14, "explicacao",
    "Esse pássaro alterna notas agudas e graves para fingir que está mais perto ou mais longe do que de fato está, e assim seu canto melancólico parece não vir de lugar nenhum, confundindo viajantes.",
    "Segundo a tradição, esse pássaro alterna notas agudas e graves que enganam sobre a distância de onde está pousado, e seu canto melancólico parece não vir de lugar nenhum, fazendo viajantes se perderem.")
substituir(14, "explicacao",
    "O folclorista Luís da Câmara Cascudo defendeu que o Saci era provavelmente um mito de ave, e notou que um pássaro muitas vezes se apoia numa perna só, o que pode levar facilmente à imagem de um menino de uma perna.",
    "O folclorista Luís da Câmara Cascudo defendeu que o Saci era provavelmente um mito de ave. E um pássaro muitas vezes se apoia numa perna só, o que pode levar facilmente à imagem de um menino de uma perna.")

# 0015: só os tipos; nota 3 mantida
trocar(15, tipos_espanto=["conexao_inesperada", "origem_inesperada"])
