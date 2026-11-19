"""Rodada 2 de Arquitetura: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-arquitetura-01.py"))
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


# 0002: a autocura é proposta do estudo, testada em réplicas
trocar(2, gancho="O concreto romano pode ter consertado as próprias rachaduras: pedrinhas brancas de cal, antes vistas como "
    "sinal de mistura malfeita, reagem com a água que entra nas fendas e as fecham com cristais novos.")

# 0004: o risco vinha dos cálculos; quem diz que o reforço talvez fosse desnecessário é a fonte, não o NIST
trocar(4, gancho="Em 1978, cálculos indicaram que um arranha-céu recém-inaugurado em Nova York podia cair com ventos na "
    "diagonal. O reforço foi feito às escondidas, à noite, com os escritórios abertos, e só veio a público em 1995.")
substituir(4, "explicacao", "a ameaça que se pensava, e que talvez o reforço nem fosse necessário.",
    "a ameaça que se pensava, e o reforço talvez nem fosse necessário.")

# 0006: mesmo desenho, não idêntico; adiamentos e ornamentos acrescentados; frase menos traduzida
substituir(6, "gancho", "é desmontado e refeito idêntico, no terreno ao lado, a cada 20 anos",
    "é desmontado e refeito com o mesmo desenho, no terreno ao lado, a cada 20 anos")
substituir(6, "explicacao",
    "A ideia é que os edifícios fiquem para sempre novos e, ao mesmo tempo, para sempre antigos e originais.",
    "O objetivo é que os prédios sejam sempre recém-construídos e, ainda assim, conservem a antiguidade do original.")
substituir(6, "explicacao", "a imperatriz Jitō, em 692.",
    "a imperatriz Jitō, em 692. Houve adiamentos ao longo dos séculos, sobretudo em tempos de guerra, e alguns "
    "detalhes, como ornamentos de cobre dourado, foram sendo incorporados.")
acrescentar_trecho(6, 0, "there have been some instances, especially because of war, where the shrine building process is postponed or delayed. [...] "
    "The shrine was not originally constructed with gold copper adornments; however, because of advancements in technology as well as Buddhist influence, it gained them over the years.")

# 0009: o recorde é entre estruturas comerciais; só o Wachusett tinha esqueleto todo de aço
trocar(9, gancho="O Monadnock, em Chicago, é o prédio comercial mais alto já feito com paredes de tijolo que sustentam o peso: "
    "16 andares e paredes de 1,8 m na base. A ampliação, que já usava aço, saiu 15% mais barata e 15% mais leve.")
substituir(9, "explicacao",
    "Projetada pela firma Holabird & Roche, ela usa estrutura de aço e só uma casca fina de tijolo e terracota",
    "Projetada pela firma Holabird & Roche, ela tem uma parte ainda em alvenaria com armação de ferro e outra, o "
    "Wachusett, com esqueleto todo de aço, e por fora usa só uma casca fina de tijolo e terracota")
acrescentar_trecho(9, 0, "its 215-foot-high (66 m) load-bearing walls were the tallest of any commercial structure in the world. [...] "
    "The Katahdin, built first, used the same iron framed masonry construction as the original. The Wachusett was entirely steel framed.")

# 0010: o anagrama é de 1675
substituir(10, "explicacao",
    "Em 1671, o inglês Robert Hooke anunciou ter achado a forma ideal de um arco e a escondeu num anagrama em latim, "
    "revelado só em 1705 pelo executor do seu testamento",
    "Em 1671, o inglês Robert Hooke anunciou ter achado a forma ideal de um arco; em 1675, publicou a solução "
    "cifrada num anagrama em latim, revelado só em 1705 pelo executor do seu testamento")

# 0011: sem exagero; 10,3 cm é a curvatura total
substituir(11, "gancho", "O Partenon quase não tem linhas retas:", "O Partenon foge sutilmente das linhas retas:")
substituir(11, "explicacao", "sobe no centro 10,3 centímetros a cada 70 metros.",
    "sobe no centro 10,3 centímetros ao longo de seus cerca de 70 metros (uma razão de 1 para 700).")
substituir(11, "explicacao", "as paredes internas", "as paredes da cela, a sala interna do templo,")

# 0013: cronologia; sem o número de anos
substituir(13, "gancho", "ficou 14 anos proibida ao culto", "passou mais de uma década proibida ao culto")
