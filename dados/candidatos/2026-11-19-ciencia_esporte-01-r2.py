"""Rodada 2 de Ciência do esporte: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-ciencia_esporte-01.py"))
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


# 0006: a proibição valeu em 2010 (votada em 2009); sem a muleta "segundo a fonte"
substituir(6, "gancho", "Dois anos depois, maiôs de corpo inteiro foram proibidos.",
    "Em 2010, maiôs de corpo inteiro foram proibidos.")
substituir(6, "explicacao", "Segundo a fonte, reduzia em 24%", "Ele reduzia em 24%")

# 0007: "is likely an artifact" -> "indicou"; sem o ano contraditório da regra de desclassificação
substituir(7, "gancho", "concluiu que o sensor", "indicou que o sensor")
substituir(7, "explicacao", "e desde 2009 o atleta pode ser desclassificado na hora.",
    "e hoje a primeira largada falsa já pode desclassificar o atleta.")

# 0008: a panturrilha continua sendo o motor; o que muda é o ponto de rotação (Houdijk et al. 2000)
trocar(8, tipos_espanto=["engenhosidade", "historia_humana"],
    gancho="O patim de lâmina articulada, patenteado já em 1894 e desprezado pelos melhores patinadores holandeses "
           "nos anos 1980, provocou uma enxurrada de recordes na patinação de velocidade a partir da temporada 1996–1997.")
substituir(8, "explicacao",
    "Em 2000, o cientista do esporte holandês Han Houdijk mostrou que o ganho não vinha da panturrilha esticando o "
    "tornozelo, e sim da mudança do ponto de rotação, da ponta do patim para a dobradiça, o que facilita transmitir "
    "força ao gelo.",
    "Em 2000, um estudo do cientista do esporte holandês Han Houdijk e colegas, com dez patinadores de elite, apontou "
    "que o segredo está no ponto de rotação. No patim comum, o pé gira em torno da longa ponta da lâmina, e o "
    "impulso final é gerado de forma ineficaz. Com a dobradiça sob a base dos dedos, a extensão do tornozelo nos "
    "últimos 50 milissegundos da passada fica mais eficaz, e a velocidade subiu 5%.")
substituir_trecho(8, 0,
    "showed that the speed gain from using the clap skate does not originate in using the calf muscle to stretch the "
    "ankle, as was assumed in the creation of the clap skate, but in the fact that the point of rotation",
    "showed that the speed gain from using the clap skate [...] the point of rotation")
acrescentar_trecho(8, 0, "The clap skate was used first in the 1984/1985 skating season.")
CANDIDATOS[7]["fontes"].append({
    "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:10731006%20AND%20SRC:MED&resultType=core&format=json",
    "titulo": "Houdijk et al. (2000). Push-off mechanics in speed skating with conventional skates and klapskates. Medicine & Science in Sports & Exercise (resumo, Europe PMC)",
    "idioma": "en",
    "trecho": (
        "Ten elite speed skaters skated four 400-m laps at maximal effort with both conventional and klapskates. [...] "
        "Skating velocity increased 5% as a result of an increase in mean power output of 25 W when klapskates were used instead of conventional skates. [...] "
        "The difference in work per stroke occurs during the final 50 ms of the push-off. "
        "This is the result of the ineffective way in which push-off forces are generated with conventional skates when the foot rotates about the long front end of the blade. [...] "
        "A hinge under the ball of the foot enhances the effectiveness of plantar flexion during the final 50 ms of the push off with klapskates and increases work per stroke and mean power output."
    ),
})

# 0009: o pouco conhecido (só as excêntricas causam a dor) vai para o gancho; ressalva da segunda sessão
trocar(9, gancho="A dor muscular do dia seguinte vem das contrações em que o músculo faz força enquanto se alonga; as de "
                 "encurtamento não a causam. E o ácido lático, o suspeito de sempre, volta ao normal em até uma hora.")
substituir(9, "explicacao",
    "exercícios durante esse período não pioraram a lesão nem atrasaram a recuperação nos estudos.",
    "exercícios durante esse período não pioraram a lesão nem atrasaram a recuperação nos estudos, embora uma "
    "segunda sessão excêntrica até uma semana depois tenha reduzido a força do músculo logo em seguida.")
acrescentar_trecho(9, 0,
    "However, it was also observed that a second bout of eccentric exercise within one week of the initial exercise "
    "did lead to decreased muscle function immediately afterward.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(8, "gancho", "e desprezado pelos melhores patinadores holandeses nos anos 1980,", "e desprezado de início pelos melhores patinadores holandeses,")
