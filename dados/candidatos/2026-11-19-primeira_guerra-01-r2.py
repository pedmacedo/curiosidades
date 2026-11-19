"""Rodada 2 de Primeira Guerra Mundial: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-primeira_guerra-01.py"))
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


# 0001: foram vários canhões
substituir(1, "gancho", "Em 1918, um canhão alemão bombardeou Paris a 120 km de distância.", "Em 1918, canhões alemães bombardearam Paris a 120 km de distância.")
substituir(1, "explicacao", "Era o Canhão de Paris, usado de março a agosto de 1918.", "Eram os Canhões de Paris, usados de março a agosto de 1918.")

# 0002: desde janeiro de 1916; os 10 mil eram baixas lidas por engano
substituir(2, "explicacao", "Por quase dois anos, companhias de túneis", "A partir de janeiro de 1916, companhias de túneis")
substituir(2, "explicacao",
    "O número de mortos, divulgado muitas vezes como 10 mil, foi contestado pelo historiador Simon Jones, que estima no máximo 500 alemães mortos pelas minas e 7.344 feitos prisioneiros.",
    "As 10 mil baixas muitas vezes atribuídas às minas vêm, na verdade, da história oficial alemã, lida por engano por autores "
    "britânicos; o historiador Simon Jones estima que as minas mataram no máximo 500 alemães, e 7.344 foram feitos prisioneiros.")

# 0003: munições em geral, inclusive da Segunda Guerra; quem recolhe na França
substituir(3, "gancho", "Só o serviço francês recolhe cerca de 900 toneladas por ano", "Só o serviço francês recolhe cerca de 900 toneladas de munições por ano")
substituir(3, "explicacao", "Os agricultores deixam o material na beira dos campos, e o exército recolhe; na Bélgica, ele é destruído num centro em Poelkapelle.",
    "Os agricultores deixam o material na beira dos campos, e as autoridades recolhem; na Bélgica, o exército o destrói num centro em Poelkapelle.")
substituir(3, "explicacao", "O nome dado a isso é \"colheita de ferro\".", "O nome dado a isso é \"colheita de ferro\". Ela inclui também restos da Segunda Guerra.")

# 0004: sem o número incerto e sem citar a Wikipédia no texto
substituir(4, "explicacao", "Em Dacar, a gripe atingiu quase todos e paralisou a divisão: fontes falam em mais de cem mortos, e a Wikipédia em português registra 464.",
    "Em Dacar, a gripe atingiu quase todos e paralisou a divisão, matando mais de cem marinheiros.")

# 0008: o contrafactual é avaliação de muitos, não certeza
substituir(8, "gancho", "Sem ela, avalia-se, o país teria perdido em poucos meses.",
    "Sem ela, segundo muitos historiadores, o país teria ficado sem munição muito antes do fim da guerra.")
substituir(8, "explicacao", "e o processo foi considerado tão essencial que se tem como praticamente certo que, sem ele, a Alemanha teria sido derrotada em questão de meses",
    "e o processo foi tão essencial que muitos avaliam que, sem ele, a Alemanha teria sido derrotada em poucos meses")
substituir(8, "explicacao", "Mesmo que os alemães tivessem acesso legal a ele", "Mesmo que empresas alemãs tivessem controle legal sobre essas jazidas")

# 0011: "também foi chamada"
substituir(11, "explicacao", "Na Espanha, ela era a \"gripe francesa\".", "Na Espanha, também foi chamada de \"gripe francesa\".")

# 0014: o que passava por mãos britânicas; a história de fachada
substituir(14, "explicacao", "Tudo passava pela Sala 40, a central de decifração do Almirantado britânico.",
    "O que passava por mãos britânicas ia parar na Sala 40, a central de decifração do Almirantado britânico.")
substituir(14, "explicacao", "A versão pública foi a de que o texto tinha sido \"comprado no México\".",
    "A história de fachada foi a de que o texto tinha sido obtido por agentes no México.")

# 0015: papel decisivo, não "foi quem convenceu"
substituir(15, "explicacao",
    "Há um detalhe que confunde muita gente: outro Robertson, o canadense Lawrence Bruce, foi quem convenceu o corpo médico britânico a adotar transfusões",
    "Um detalhe curioso: outro Robertson, o canadense Lawrence Bruce, teve papel decisivo para convencer o corpo médico britânico a adotar transfusões")

# gancho do 0008 encurtado para caber em 220 caracteres
trocar(8, gancho="A reação química que hoje sustenta a comida de metade da humanidade deixou a Alemanha fazer explosivos sob "
    "bloqueio na Primeira Guerra. Sem ela, para muitos historiadores, a munição teria acabado bem antes.")
