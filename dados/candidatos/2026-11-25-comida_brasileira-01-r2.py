"""Rodada 2 de Comida brasileira: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-comida_brasileira-01.py"))
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


# 0001: mostrar também o outro lado do debate
substituir(1, "explicacao",
    "do que uma contribuição africana. ",
    "do que uma contribuição africana. A questão não está fechada: outros historiadores veem a feijoada "
    "brasileira como fruto da mistura de tradições portuguesas, africanas e indígenas no período colonial, e é "
    "certo que feijão e partes do porco alimentavam os escravizados. ")
substituir(1, "explicacao",
    "Ensopados de carne cozidos em panela de barro existem por toda a Europa, como o cozido português, e as feijoadas de Portugal já misturavam",
    "As feijoadas de Portugal já misturavam")
acrescentar_trecho(1, 0, "Pig parts and Brazilian beans undoubtedly provided sustenance for the enslaved.")
acrescentar_trecho(1, 1, "During slavery, it combined Portuguese, African, and indigenous culinary traditions, according to historical consensus from the University of Sao Paulo (2015).")

# 0004: um só estudo para os 42%; a lista de 2009 sai; a sentença de 2012 fica
trocar(4, nota_surpresa=3)
substituir(4, "explicacao",
    "e até hoje é a planta mais importante da dieta de populações tradicionais: num estudo com três comunidades caboclas, ele somava até 42% de tudo o que se comia, em peso.",
    "e num estudo com três comunidades caboclas foi descrito como a planta mais importante da dieta, somando até 42% de tudo o que se comia, em peso.")
substituir(4, "explicacao",
    "e as promessas exageradas atraíram golpistas: em 2009, os golpes com açaí lideraram a lista de fraudes da Comissão Federal de Comércio americana, que em 2012 impôs uma condenação de 80 milhões de dólares a cinco empresas que prometiam emagrecimento.",
    "e as promessas exageradas atraíram golpistas: em 2012, a Comissão Federal de Comércio americana obteve uma sentença de 80 milhões de dólares contra cinco empresas que vendiam cápsulas de açaí prometendo emagrecimento e prevenção de câncer de cólon.")
substituir_trecho(4, 0,
    "In 2009, açaí scams were ranked No. 1 on the U.S. Federal Trade Commission's \"scams and rip-offs\" list [...] ",
    "")

# 0005: mecanismo como suposição; limitações declaradas pelos autores
substituir(5, "gancho",
    "o suspeito era o açaí, contaminado por barbeiros na hora de fazer a polpa.",
    "o suspeito era o açaí, provavelmente contaminado por barbeiros.")
substituir(5, "explicacao", "Os investigadores compararam quem adoeceu com quem não adoeceu. ", "")
substituir(5, "explicacao",
    "Nenhum barbeiro foi achado nos locais vistoriados",
    "Os próprios autores apontam limites: pode ter havido viés de memória, pela demora entre a doença e a "
    "investigação, e nenhuma amostra do alimento foi coletada para teste. Nenhum barbeiro foi achado nos locais vistoriados")
substituir_trecho(5, 0,
    "[...] Studies are needed",
    "[...] Limitations of this study are possible recall bias caused by delay between illness and investigation and failure to collect food samples for testing. Studies are needed")

# 0007: dono de padaria; sem o número velho de lojas; a comida árabe em geral
trocar(7, nota_surpresa=3)
substituir(7, "gancho", "por um padeiro nascido em Portugal", "por um dono de padaria nascido em Portugal")
substituir(7, "explicacao", "pediu emprego na padaria de Alberto Saraiva, padeiro nascido em Portugal.",
    "pediu emprego a Alberto Saraiva, dono de padaria nascido em Portugal.")
substituir(7, "explicacao",
    "A rede cresceu, passou de 475 lojas e ficou conhecida pelos preços muito baixos.",
    "A rede cresceu depressa e ficou conhecida pelos preços muito baixos.")
substituir(7, "explicacao",
    "Era popular, mas pouco acessível e costumava ser cara.",
    "A comida árabe era popular, mas pouco acessível e costumava ser cara.")

# 0011: o ano de 1934 é contestado
trocar(11, nota_surpresa=3)
substituir(11, "gancho", "foi pedido em 1934, num restaurante de São Paulo,", "foi pedido num restaurante de São Paulo")
substituir(11, "explicacao", "Em 1934, Casemiro Pinto Neto estudava", "Casemiro Pinto Neto estudava")

# 0012: não contradizer o fato da domesticação da mandioca
trocar(12, nota_surpresa=3)
substituir(12, "explicacao",
    "planta nativa do Norte e do Nordeste do Brasil que hoje cresce também",
    "planta nativa do Brasil que hoje cresce também")

# 0013: a expulsão dos jesuítas foi em 1767
substituir(13, "gancho", "Com a expulsão deles, nos anos 1770,", "Com a expulsão deles, no século XVIII,")
substituir(13, "explicacao", "Com a expulsão da ordem, nos anos 1770,", "Com a expulsão da ordem, no século XVIII,")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(4, 'gancho',
    'Na foz do Amazonas, o açaí é comida básica há séculos: em três comunidades caboclas estudadas,',
    'Na foz do Amazonas, o açaí é comida básica há séculos; em três comunidades caboclas da Amazônia,')
substituir(12, 'explicacao',
    'Na produção tradicional dessas regiões brasileiras,',
    'Na produção tradicional do Norte e do Nordeste do Brasil,')
substituir(12, 'explicacao',
    'Na Ásia, elas se chamam boba',
    'No Leste Asiático, elas se chamam boba')
