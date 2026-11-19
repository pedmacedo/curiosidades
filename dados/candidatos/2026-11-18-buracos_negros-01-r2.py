"""Rodada 2 de Buracos negros e objetos extremos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-buracos_negros-01.py"))
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

# 0002: o Buraco Negro de Calcutá como fama, não como fato
substituir(2, "gancho", "cela famosa de onde quem entrava não saía vivo.", "cela que ganhou fama de lugar de onde ninguém saía vivo.")
substituir(2, "explicacao", "uma prisão que ficou notória porque as pessoas entravam e nunca saíam com vida",
    "uma prisão que ganhou a fama de lugar onde se entrava para nunca mais sair com vida")

# 0007: o inverno no Polo Sul atrasou o processamento, não explica os anos até a imagem
substituir(7, "explicacao",
    "A do buraco negro da Via Láctea, Sagitário A*, exigiu mais paciência: os dados tinham sido colhidos em abril de 2017, mas não há voos de ida e volta ao Polo Sul durante o inverno austral, de abril a outubro. Os discos do telescópio de lá só chegaram em dezembro de 2017, e a imagem foi divulgada em 12 de maio de 2022.",
    "O transporte aéreo tem seus limites: os dados de Sagitário A*, o buraco negro da Via Láctea, foram colhidos em abril de 2017, mas não há voos de ida e volta ao Polo Sul durante o inverno austral, de abril a outubro, e por isso o conjunto completo só pôde ser processado depois que os discos do telescópio de lá chegaram, em dezembro de 2017. A imagem de Sagitário A* foi divulgada em 12 de maio de 2022.")

# 0009: abaixo de 10^-7 K; frase truncada
substituir(9, "explicacao", "ela ficaria em torno de 10⁻⁷ kelvin, um décimo de milionésimo de grau acima do zero absoluto",
    "ela ficaria abaixo de 10⁻⁷ kelvin, menos de um décimo de milionésimo de grau acima do zero absoluto")
substituir(9, "explicacao", "e nenhum buraco negro estelar consegue evaporar mais frio que o ambiente",
    "e, como são mais frios que o espaço em volta, nenhum buraco negro estelar consegue evaporar")
