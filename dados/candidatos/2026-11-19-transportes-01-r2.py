"""Rodada 2 de Transportes: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-transportes-01.py"))
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


# 0001: a altitude dos 12.500 m é a do primeiro alarme; quem não sabia do autódromo
substituir(1, "gancho", "ficou sem combustível a 12.500 m", "ficou sem combustível em pleno voo, a mais de 10 mil metros de altitude")
substituir(1, "explicacao", "Nenhum dos dois sabia que parte dela tinha virado autódromo",
    "Nem Quintal nem o controle de tráfego aéreo sabiam que parte dela tinha virado autódromo")

# 0002: o efeito giroscópico também contribui; a faixa de velocidades
substituir(2, "gancho", "pode seguir de pé sozinha", "pode seguir de pé sozinha, na velocidade certa")
substituir(2, "explicacao",
    "Hoje se entende que geometria, distribuição de massa e velocidade se combinam, em graus variados, para produzir o equilíbrio.",
    "Hoje se entende que geometria, distribuição de massa e o próprio efeito giroscópico contribuem, em graus variados, "
    "sem que nenhum deles baste sozinho, e que a autoestabilidade só aparece dentro de uma faixa de velocidades.")

# 0004: o cone ajuda; os frisos ficam de reserva
substituir(4, "gancho", "O trem faz a curva porque as rodas são cones:", "O que ajuda o trem a fazer a curva é que as rodas são cones:")
substituir(4, "explicacao", "É esse formato que mantém o trem nos trilhos.",
    "É esse formato que mantém o trem centrado nos trilhos, deixando os frisos como reserva.")

# 0005: Muller venceu a aposta; Kusenko reconheceu por um detalhe técnico
substituir(5, "explicacao",
    "Kusenko pagou a aposta, mas disse que cedeu por um detalhe técnico e que não via prova de que o Blackbird tivesse superado o vento.",
    "Muller venceu com experimentos em modelo, os dados originais da corrida e as equações. Kusenko reconheceu a derrota, "
    "mas disse que cedeu por um detalhe técnico e que continuava sem ver prova de que o Blackbird tivesse superado o vento.")

# 0008: os recortes das antenas também eram quadrados; sem "pouco mais de um ano"
substituir(8, "gancho",
    "Mas a fadiga do metal partiu de recortes no teto feitos para antenas; o formato das janelas dos passageiros não foi apontado como causa.",
    "Mas a fadiga do metal partiu de recortes quadrados no teto, para antenas; as janelas dos passageiros não foram apontadas como causa.")
substituir(8, "explicacao", "Em pouco mais de um ano de serviço, três se perderam em pleno voo.", "Pouco depois da estreia, três se perderam em pleno voo.")

# 0010: o primeiro automóvel, não qualquer veículo
substituir(10, "gancho", "A barreira dos 100 km/h foi rompida por um carro elétrico, em 1899.",
    "O primeiro automóvel a passar dos 100 km/h foi um elétrico, em 1899.")

# 0011: a explicação por Newton é correta, mas incompleta
substituir(11, "explicacao", "Uma explicação simplificada melhor parte das leis de Newton:",
    "Outra explicação simplificada, correta mas incompleta, parte das leis de Newton:")
substituir(11, "explicacao", "o ar, em reação, empurra a asa para cima.",
    "o ar, em reação, empurra a asa para cima. A explicação completa junta as duas coisas: o desvio do ar para baixo e "
    "as diferenças de pressão e de velocidade em volta da asa.")

# 0013: Coester não partiu das ferrovias atmosféricas
substituir(13, "gancho", "Um brasileiro retomou a ideia:", "O mesmo princípio voltou pelas mãos de um brasileiro:")
substituir(13, "explicacao", "e retomou o princípio com materiais modernos.",
    "e criou um sistema que usa o mesmo princípio, agora viável graças a materiais modernos.")

# 0015: "geralmente"; o limite de 1896 podia ser reduzido
substituir(15, "explicacao", "na prática quase sempre um menino", "na prática geralmente um menino")
substituir(15, "explicacao", "livres dessas regras e com limite de 14 milhas por hora.",
    "livres dessas regras e com limite de até 14 milhas por hora, que as autoridades locais podiam reduzir.")

# ganchos encurtados para caber em 220 caracteres
trocar(1, gancho="Em 1983, um Boeing 767 ficou sem combustível a mais de 10 km de altitude porque a conta foi feita em libras, "
    "não em quilos. O comandante, piloto de planador, planou 17 minutos até uma ex-base aérea que virara autódromo.")
trocar(2, gancho="Empurrada sem ninguém em cima e na velocidade certa, uma bicicleta segue de pé sozinha. Muitos atribuem isso ao "
    "efeito giroscópico das rodas, mas em 2011 uma bicicleta feita para anular esse efeito também se equilibrou.")
substituir(4, "gancho", "O que ajuda o trem a fazer a curva é que", "O que ajuda o trem na curva é que")
trocar(13, gancho="Trens ingleses a pressão de ar, com um pistão num tubo vedado com couro e sebo, foram abandonados em 1847 e "
    "1848. O mesmo princípio voltou com um brasileiro: o Aeromóvel, que desde 2026 leva passageiros em Guarulhos.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(1, "explicacao", "Sobre Red Lake, em Ontário, os dois motores pararam, e parte das telas da cabine se apagou.",
    "Sobre Red Lake, em Ontário, soaram os alarmes de pressão de combustível; pouco depois, já desviando para Winnipeg, "
    "os dois motores pararam, e parte das telas da cabine se apagou.")
