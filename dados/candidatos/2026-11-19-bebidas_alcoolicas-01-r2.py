"""Rodada 2 de Bebidas alcoólicas: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-bebidas_alcoolicas-01.py"))
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


# 0005: "quase todas"; o dano vem das deformações e de fungos, não de um veneno
trocar(5, gancho="Sem raízes americanas, a Europa não teria indústria de vinho. Quase todas as suas videiras são enxertadas "
    "em raízes norte-americanas, a saída contra um inseto que arrasou os vinhedos europeus no século XIX.")
substituir(5, "explicacao",
    "ele injeta um veneno que corrói a raiz e, quando a seiva perde pressão, vai embora, de modo que quem arrancava uma planta morrendo não o encontrava.",
    "suas picadas deformam as raízes e abrem caminho para fungos que as estrangulam; quando a planta definha e a "
    "seiva perde pressão, o inseto a abandona, de modo que quem arrancava uma planta morrendo não o encontrava.")
acrescentar_trecho(5, 0,
    "On Vitis vinifera, the resulting deformations on roots (\"nodosities\" and \"tuberosities\") and secondary fungal "
    "infections can girdle roots, gradually cutting off the flow of nutrients and water to the vine.")
substituir_trecho(5, 1,
    "The proboscis of the grape phylloxera has both a venom canal from which it injects its deadly venom and a feeding tube through which it takes in vine sap and nutrients. "
    "As the toxin from the venom corrodes the root structure of a vine, the sap pressure falls and, as a result,",
    "the sap pressure falls and, as a result,")

# 0007: sem o Brasil em 1906 e sem sugerir que os outros seguiram a Suíça
substituir(7, "explicacao",
    "Outros países fizeram o mesmo: o Brasil e a Bélgica proibiram a venda em 1906, e os Estados Unidos, em 1912.",
    "Outros países também baniram a bebida naquela época, como a Bélgica, em 1906, e os Estados Unidos, em 1912.")

# 0010: "sobretudo", não "só"
substituir(10, "gancho", "dependem só do teor de álcool", "dependem sobretudo do teor de álcool")

# 0011: células de anfíbio em laboratório (Salamandridae nos descritores MeSH); "calam", não "bloqueia"
trocar(11, gancho="O vinho com \"gosto de rolha\" cheira a mofo, mas o culpado, o TCA, faz algo mais estranho: em células "
    "olfativas de anfíbio, no laboratório, doses ínfimas dele calam os canais que transmitem o cheiro.")
substituir(11, "explicacao",
    "feito com células receptoras olfativas isoladas, mostrou",
    "feito em laboratório com células receptoras olfativas isoladas de um anfíbio da família das salamandras "
    "(Salamandridae), e não no nariz humano, mostrou")
acrescentar_trecho(11, 0, "\"descriptorName\":\"Salamandridae\"")

# 0012: o teste original era o de queimar ou não; a pólvora era outro método
trocar(12, nota_surpresa=3,
    gancho="O \"proof\" dos rótulos de uísque vem de testes de fogo para cobrar imposto. Num deles, molhava-se pólvora "
    "na bebida: se ainda queimasse, estava \"acima da prova\". O limite equivalia a uns 57% de álcool.")

# 0015: sem Lisboa; "produção liberada" em vez de "legalizada"
trocar(15, nota_surpresa=3,
    gancho="Portugal proibiu várias vezes a cachaça no Brasil colonial para proteger a bagaceira e o vinho do reino. "
    "Disso ficaram uma revolta no Rio e apelidos para enganar a fiscalização; hoje ela tem mais de 2 mil nomes.")
substituir(15, "explicacao",
    "Em 1756, a aguardente de cana esteve entre os produtos que mais renderam impostos para reconstruir Lisboa, "
    "destruída pelo terremoto do ano anterior. ", "")
substituir(15, "explicacao", "Em 13 de setembro de 1661 a bebida foi legalizada",
    "Em 13 de setembro de 1661 a produção foi liberada")
substituir_trecho(15, 1,
    "Em 1756, a aguardente de cana-de-açúcar foi um dos gêneros que mais contribuíram com impostos voltados para a reconstrução de Lisboa, destruída no grande sismo de 1755. ",
    "[...] ")
