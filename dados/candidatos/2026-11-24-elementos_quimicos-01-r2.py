"""Rodada 2 de Elementos químicos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-elementos_quimicos-01.py"))
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


# 0002: os 5.700 litros são estimativa
substituir(2, "gancho", "Ele usou cerca de 5.700 litros para obter só 120 gramas, e jogou fora a parte mais rica.",
    "Usou, por estimativa, uns 5.700 litros para obter só 120 gramas, e jogou fora a parte mais rica.")

# 0004: Mendeleev adotou o grupo zero, não o criou
substituir(4, "explicacao", "Mendeleev criou em 1902 um \"grupo zero\" para esses gases que quase não reagem",
    "Mendeleev pôs esses gases que quase não reagem, em 1902, num \"grupo zero\" da sua tabela")

# 0006: sem a causalidade do diploma; eleição como membro correspondente
trocar(6, gancho="O frâncio, último elemento descoberto na natureza, foi achado em 1939 por Marguerite Perey, que entrou "
    "no laboratório de Marie Curie como técnica, sem diploma universitário.")
substituir(6, "explicacao",
    "A nota à Academia de Ciências foi apresentada pelo físico Jean Perrin, porque ela era só assistente de laboratório, sem diploma universitário.",
    "A nota à Academia de Ciências foi apresentada pelo físico Jean Perrin.")
substituir(6, "explicacao",
    "Em 1962, Perey se tornou a primeira mulher eleita para a Academia de Ciências da França, honra que fora negada a Marie Curie.",
    "Em 1962, Perey se tornou a primeira mulher eleita para a Academia de Ciências da França, como membro correspondente, honra que fora negada a Marie Curie.")
CANDIDATOS[5]["fontes"].append({
    "url": "https://fr.wikipedia.org/wiki/Marguerite_Perey", "titulo": "Marguerite Perey", "idioma": "fr",
    "trecho": "Le 12 mars 1962, Marguerite Perey est la première femme élue correspondant de l'Académie des sciences. "
              "C'est la première fois que la société savante, qui s'était refusée à accueillir Marie Curie, recevait une femme."})

# 0007: o endereço segue a ordem de um envelope
substituir(7, "explicacao",
    "O endereço de brincadeira, notado pela revista Discover, juntava o seabórgio ao laurêncio (do laboratório onde ele trabalhava), ao berquélio, ao califórnio e ao amerício.",
    "O endereço de brincadeira, notado pela revista Discover, segue a ordem de um envelope: o destinatário "
    "(seabórgio), o local de trabalho (laurêncio, que remete ao Laboratório Lawrence Berkeley), a cidade "
    "(berquélio, de Berkeley), o estado (califórnio) e, por fim, as Américas (amerício).")
CANDIDATOS[6]["fontes"].append(wiki("Berkelium",
    "It is named after the city of Berkeley, California, the location of the Lawrence Berkeley National Laboratory",
    nome="Berkelium"))
CANDIDATOS[6]["fontes"].append(wiki("Americium",
    "located under the lanthanide element europium and was thus named after the Americas by analogy.",
    nome="Americium"))

# 0009: o ponto sólido é o descobridor registrado
substituir(9, "explicacao",
    "Foi o primeiro metal descoberto desde a pré-história: ferro, cobre, ouro e os outros metais antigos não têm descobridor registrado.",
    "É apontado como o primeiro metal com descobridor conhecido: ferro, cobre, ouro e os demais metais conhecidos "
    "antes dele, inclusive zinco e bismuto, não têm descobridor registrado.")

# 0010 (opcional): associação arqueológica
substituir(10, "explicacao", "Esmeraldas, no Equador, ligados à cultura La Tolita, tinham",
    "Esmeraldas, no Equador, que os arqueólogos costumam associar à cultura La Tolita, tinham")

# 0011 (opcional): morreram antes do anúncio
substituir(11, "explicacao", "que morreram entre a proposta e o anúncio, em agosto de 1955.",
    "que morreram antes do anúncio, feito em agosto de 1955.")

# 0012: sem "único"; "na extração"
trocar(12, gancho="O símbolo do tungstênio é W por causa de \"espuma de lobo\": o minério parecia devorar o estanho na "
    "extração. Em 1928, a Justiça dos EUA anulou a patente com que a GE tentava se apropriar do elemento.")

# 0014 (opcional): tema secundário
trocar(14, temas_secundarios=["fisica_particulas"])

# 0016: as algas davam carbonato de sódio para o salitre; "até o fim da vida"
substituir(16, "gancho", "nas cinzas de algas usadas para fazer salitre", "nas cinzas de algas usadas na produção de salitre")
substituir(16, "gancho", "Investigando por que os tachos de cobre corroíam,", "Ao investigar a corrosão dos tachos de cobre,")
substituir(16, "explicacao", "lutou com dificuldades financeiras a vida toda e morreu em 1838",
    "enfrentou dificuldades financeiras até o fim da vida e morreu em 1838")
