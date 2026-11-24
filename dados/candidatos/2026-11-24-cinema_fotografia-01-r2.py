"""Rodada 2 de Cinema e fotografia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-cinema_fotografia-01.py"))
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


# 0001: "a mais antiga tirada com câmera"; as outras heliografias eram cópias por contato
substituir(1, "gancho", "A foto mais antiga que sobreviveu, feita por Niépce em 1827,",
    "A foto mais antiga tirada com câmera que sobreviveu, feita por Niépce em 1827,")
substituir(1, "explicacao", "são telhados e o campo vistos de uma janela alta.",
    "são telhados e o campo vistos de uma janela alta. Sobrevivem mais de vinte heliografias dele, feitas "
    "entre 1825 e 1829, mas esta é a única vista feita com câmera que se conhece; as demais que ele mostrou "
    "na Inglaterra eram cópias de obras de arte feitas por contato.")
acrescentar_trecho(1, 0, "View from the Window at Le Gras was the only example of a camera photograph; the rest were contact-exposed copies of artwork.")
acrescentar_trecho(1, 1, "More than twenty of Niépce's heliographic plates and prints made between 1825 and 1829 are held in public and private collections, yet the Niépce Heliograph is the only known surviving point de vue.")

# 0002: a cena certa (o freguês e o engraxate) e "tida como"; restauração piorou uma placa já deteriorada
trocar(2, gancho="A foto tida como a mais antiga com gente, de cerca de 1838, mostra uma avenida movimentada de Paris que "
    "parece vazia: só um homem que mandava engraxar as botas (e o engraxate) ficou parado o bastante para aparecer.")
substituir(2, "explicacao", "A placa original foi arruinada por uma restauração malsucedida depois de 1970",
    "A placa original, já deteriorada, foi ainda mais danificada por uma restauração malsucedida a partir de 1970")
acrescentar_trecho(2, 0, "The images were stored at the royal palace and later at the Bavarian National Museum archives, where they gradually deteriorated")

# 0004: o primeiro teste foi a trote, com fios acionados; depois, Sallie Gardner a galope
substituir(4, "explicacao",
    "Fios passavam sob a pista e, ao serem rompidos um a um pela roda da charrete puxada pelo cavalo, "
    "disparavam os obturadores em sequência, com exposições que, segundo se anunciou, duravam um milésimo "
    "de segundo.",
    "No primeiro teste, um cavalo a trote puxava uma charrete: fios sob a pista eram acionados um a um pela "
    "roda, interrompiam um circuito elétrico e disparavam os obturadores em sequência, com exposições que, "
    "segundo se anunciou, duravam um milésimo de segundo. Logo depois, a égua Sallie Gardner passou pela "
    "pista a galope.")
acrescentar_trecho(4, 0, "After the first successful experiment, running mare Sallie Gardner was sent across the track.")

# 0006: nenhuma prova contra Edison; o depoimento do filho sem sugerir ligação com a morte
substituir(6, "explicacao", "A viúva suspeitou de crime ligado à disputa de patentes com Edison.",
    "A viúva suspeitou de crime ligado à disputa de patentes com Edison, mas nunca surgiu prova concreta disso.")
substituir(6, "explicacao",
    "Em 1898, o filho Adolphe testemunhou num processo em que Edison dizia ser o único inventor do cinema; "
    "três anos depois, foi achado morto, tendo se matado com um tiro.",
    "Em 1898, o filho Adolphe depôs contra Edison num processo em que o americano se dizia o único inventor "
    "do cinema, na esperança de ver o pai reconhecido; o caso foi perdido. Três anos depois, Adolphe se matou "
    "com um tiro.")
acrescentar_trecho(6, 0, "Le Prince's widow Lizzie and Adolphe hoped that this would gain recognition for Le Prince's achievement, but when the case went against Mutoscope their hopes were dashed.")

# 0007: converter os pés
substituir(7, "explicacao", "empilhou na piscina 500 mil pés de filme",
    "empilhou na piscina 500 mil pés de filme (cerca de 150 km de película)")

# 0008: mergulhar, não jogar água
substituir(8, "explicacao", "e jogar água pode até aumentar a fumaça",
    "e mergulhar o filme em chamas na água pode não apagá-lo e ainda aumentar a fumaça")

# 0009: a Kodak vendia e revelava; Shirley era o nome da primeira modelo
substituir(9, "explicacao", "quebrar o monopólio da Kodak, que então revelava quase todo o filme colorido do país",
    "quebrar o monopólio da Kodak, que então vendia quase todo o filme colorido do país e também o revelava em suas lojas")
trocar(9, gancho="Por décadas, laboratórios calibraram as cores das fotos pelo retrato de uma mulher branca, a \"Shirley\", "
    "nome da primeira modelo, funcionária da Kodak. O filme favorecia a pele clara; Godard chegou a recusá-lo.")

# 0011: "segundo um relato"; a falência veio da dívida com a Pathé
substituir(11, "explicacao", "uma cópia vendida para exibição só na Argélia foi parar",
    "segundo um relato, uma cópia vendida para exibição só na Argélia foi parar")
substituir(11, "explicacao", "Endividado, ele faliu e não fez mais filmes depois de 1912.",
    "Anos depois, ao romper o contrato com a produtora Pathé, ficou sem como pagar o que devia a ela; "
    "faliu e não fez mais filmes depois de 1912.")
acrescentar_trecho(11, 0, "When Méliès broke his contract with Pathé in 1913, he had nothing with which to cover his indebtedness to that company.")
substituir_trecho(11, 1, "Méliès sold a print of the film", "reports that Méliès sold a print of the film")

# 0013: emulsão de preto e branco, não "sem corante"; "cerca de" nove meses
substituir(13, "gancho", "Em 1891, Gabriel Lippmann fez fotos coloridas sem corante algum:",
    "Em 1891, Gabriel Lippmann fez fotos coloridas com uma emulsão de preto e branco:")
substituir(13, "explicacao", "após nove meses de exposição", "após cerca de nove meses de exposição")

# 0014: a demora foi ligar o cilindro ao filme; a pergunta vem antes de a câmera rodar
trocar(14, gancho="O filme mais antigo que se conhece com som gravado ao vivo, de 1894 ou 1895, mostra dois homens dançando "
    "ao som de um violino. O som, num cilindro de cera quebrado, só foi ligado ao filme em 1998.")
substituir(14, "explicacao", "No cilindro, antes da música, um homem pergunta se já está funcionando.",
    "No cilindro, antes de a câmera começar a rodar, um homem pergunta se já está funcionando.")

# 0015: fadas de papelão copiadas; só Elsie falou da vergonha
trocar(15, gancho="Na Inglaterra, em 1917, duas primas de 16 e 9 anos fotografaram \"fadas\" de papelão copiadas de um "
    "livro infantil. Conan Doyle, criador de Sherlock Holmes, publicou as fotos como prova. Só em 1983 admitiram a farsa.")
substituir(15, "explicacao", "Disseram que ficaram envergonhadas de desmentir um homem tão brilhante.",
    "Elsie contou que as duas ficaram envergonhadas de desmentir um homem tão brilhante.")
substituir(13, "gancho", "A ideia lhe deu o Nobel de Física de 1908.", "Ganhou o Nobel de Física de 1908.")
