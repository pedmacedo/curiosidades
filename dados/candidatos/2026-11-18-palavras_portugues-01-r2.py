"""Rodada 2 de Palavras do português: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-palavras_portugues-01.py"))
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


# 0002: a data é a época do livro de Esdras
substituir(2, "explicacao",
    "no livro bíblico de Esdras, escrito entre os séculos VI e V antes de Cristo, receber o sal",
    "na época do livro bíblico de Esdras, por volta de 550 a 450 antes de Cristo, receber o sal")

# 0005: "candidato mais forte", com a ressalva; a frase das atribuições é sobre o espanhol
substituir(5, "gancho", "É o empréstimo basco mais forte do português e do espanhol.",
    "Tirando termos culturais, é o candidato mais forte a empréstimo basco no espanhol e no português.")
substituir(5, "explicacao", "Já se atribuíram ao basco muitas palavras do espanhol e do português, mas a maioria",
    "Já se atribuíram ao basco muitas palavras do espanhol, mas a maioria")

# 0006: "provavelmente"; texto próprio; o parentesco com "soledad"
trocar(6, gancho="\"Saudade\" vem do latim \"solitatem\", solidão. Passou por \"soidade\" e \"soudade\" e provavelmente ganhou a forma atual por influência de \"saúde\" e \"saudar\". É prima do espanhol \"soledad\".")
substituir(6, "explicacao",
    "Saudade é uma das palavras mais presentes na poesia de amor em português e em galego e na música "
    "popular. Descreve uma mistura de perda, falta, distância e amor.",
    "Poucas palavras são tão associadas à poesia e à música em português e em galego, e ela nomeia um "
    "sentimento que junta falta, distância e afeto.")
substituir(6, "explicacao", "Foi a influência de duas palavras", "Acredita-se que foi a influência de duas palavras")
substituir(6, "explicacao",
    "Ou seja, a palavra que se costuma apresentar como intraduzível começou como um nome comum para estar "
    "sozinho.",
    "O mesmo étimo latino deu o espanhol \"soledad\", que lá continuou significando solidão. Em nenhuma "
    "outra língua românica a palavra ganhou o sentido que \"saudade\" tem em português.")
acrescentar_trecho(6, 0, "Pensa-se que por influência de \"saúde\" e \"saudar\", surgiu a variante \"saudade\" que atualmente predomina em português. "
    "O étimo latino foi produtivo em outras línguas românicas, por exemplo no castelhano \"soledad\", mas em nenhuma delas adquiriu o mesmo")

# 0007: sem o ano exato; a origem é disputada
substituir(7, "gancho", "O nome surgiu em 1823, num serviço de carruagens em Nantes, na França, e a origem exata ainda tem duas versões.",
    "O nome surgiu nos anos 1820, num serviço de carruagens em Nantes, na França, e a origem exata ainda é disputada.")
substituir(7, "explicacao", "Em 1823, Stanislas Baudry abriu em Nantes", "Na década de 1820, Stanislas Baudry abriu em Nantes")

# 0008: sem a anedota de Camilo, que não tem referência
trocar(8, gancho="\"Você\" começou como \"vossa mercê\", tratamento dado aos reis de Portugal. Quando os reis passaram a exigir \"alteza\" e depois \"majestade\", a \"mercê\" foi descendo a escala social até virar tratamento comum.")
substituir(8, "explicacao",
    "No século XIX, o \"vosmecê\" estava tão banalizado que o escritor Camilo Castelo Branco contou, rindo, que seu "
    "merceeiro tinha se ofendido por ser chamado de você: queria ser tratado por senhoria.",
    "No século XIX, o \"vosmecê\" já tinha se espalhado tanto que deixara de soar como deferência.")
