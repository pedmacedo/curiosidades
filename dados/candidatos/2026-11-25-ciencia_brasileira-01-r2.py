"""Rodada 2 de Ciência brasileira: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-ciencia_brasileira-01.py"))
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


# 0001: gancho pela Plataforma Lattes; sem apresentar "primeiro autor" como mérito
trocar(1, gancho="A Plataforma Lattes, o banco nacional de currículos de cientistas, homenageia o curitibano César Lattes, "
    "um dos descobridores do píon em 1947. O Nobel ligado à descoberta foi só para o chefe do grupo.")

# 0002: o sentido de "urka" não foi "notado" por Gamow
substituir(2, "explicacao", "Gamow ainda notou que, no dialeto russo dele, \"urka\" pode significar ladrão.",
    "Por coincidência, no dialeto do sul da Rússia falado por Gamow, \"urka\" também pode significar ladrão ou bandido.")

# 0003, 0004, 0006: aprovados; só a nota
trocar(3, nota_surpresa=3)
trocar(4, nota_surpresa=3)
trocar(6, nota_surpresa=3)

# 0005: sem ano de formatura; Hamburgo sem o "a partir de 1909"
substituir(5, "explicacao", "Rocha Lima, carioca formado em medicina em 1905, foi um dos fundadores",
    "Rocha Lima, médico carioca, foi um dos fundadores")
substituir(5, "explicacao", "e, a partir de 1909, dirigiu o departamento de patologia de um instituto de doenças tropicais em Hamburgo, na Alemanha",
    "e depois foi trabalhar num instituto de doenças tropicais em Hamburgo, na Alemanha, onde chefiou o departamento de patologia")

# 0008: datas das picadas, o grupo de controle de abril de 1903, sem "primeiro latino-americano"
trocar(8, nota_surpresa=3, tipos_espanto=["historia_humana", "contraintuitivo"])
substituir(8, "gancho", "Em 1903,", "Entre 1902 e 1903,")
substituir(8, "explicacao", "Em 1903, Ribas repetiu na capital paulista",
    "Entre dezembro de 1902 e janeiro de 1903, Ribas repetiu na capital paulista")
substituir(8, "explicacao", "Oscar Moreira e outros voluntários. ",
    "Oscar Moreira e outros voluntários. Ribas, Lutz e Moreira não tiveram sintomas, provavelmente por já estarem "
    "imunizados, mas os outros três voluntários adoeceram. ")
substituir(8, "explicacao",
    "No mesmo ano, no Hospital de Isolamento, que hoje leva o seu nome, tocou em dejetos de doentes e deitou-se ao lado deles para mostrar que a doença não pegava pelo contato.",
    "Em abril de 1903, no Hospital de Isolamento, que hoje leva o seu nome, três voluntários italianos passaram 20 dias "
    "em quartos protegidos de mosquitos, cheios de roupas e objetos sujos de doentes, e nenhum adoeceu.")
substituir(8, "explicacao",
    "Lutz, que dirigia o Instituto Bacteriológico de São Paulo, é apontado como o primeiro cientista latino-americano a estudar a fundo e confirmar como o Aedes aegypti transmite a febre amarela.",
    "Lutz dirigia então o Instituto Bacteriológico de São Paulo.")
substituir_trecho(8, 1, " [...] Lutz was the first Latin American scientist to study in depth and to confirm the mechanisms of transmission of yellow fever by the Aedes aegypti species of mosquitoes", "")
CANDIDATOS[7]["fontes"].append({
    "url": "https://revistapesquisa.fapesp.br/na-propria-pele/",
    "titulo": "Na própria pele (Revista Pesquisa FAPESP, mar. 2009)", "idioma": "pt",
    "trecho": "A voz corrente da medicina acreditava que a infecção era causada por microrganismos presentes em bolores e ares contaminados por outros doentes. [...] "
        "Autorizado pelo governo, realizou a primeira etapa das experiências entre 15 de dezembro de 1902 e 20 de janeiro de 1903. "
        "Ao lado de Lutz, diretor do Instituto Bacteriológico, se deixou picar durante cinco sessões por mosquitos infectados de um caso leve. "
        "Outros quatro voluntários fizeram o mesmo (Oscar Moreira, Domingos Pereira Vaz, André Ramos e Januário Fiori). "
        "Os três primeiros não apresentaram sintomas, provavelmente por já estarem imunizados – eles frequentavam regiões onde a doença era endêmica. "
        "Mas Vaz, Ramos e Fiori adoeceram. "
        "Em abril de 1903 ocorreu a segunda etapa das experiências. "
        "O grupo de controle, com três voluntários italianos, ficou fechado por 20 dias em quartos protegidos contra mosquitos, cheios de roupas e objetos sujos de urina, vômito e fezes de doentes da febre. "
        "Nenhum adoeceu. [...] "
        "As duas experiências ocorreram no Hospital de Isolamento de São Paulo [...] "
        "Posteriormente, o antigo hospital deu origem ao Instituto de Infectologia Emílio Ribas."})

# 0009: a colônia funcionou de 1924 a 2022; fontes acadêmicas
trocar(9, nota_surpresa=3)
substituir(9, "explicacao", "Uma colônia psiquiátrica no Rio leva o seu nome.",
    "Uma colônia psiquiátrica no Rio, que funcionou de 1924 a 2022, levou o seu nome.")
CANDIDATOS[8]["fontes"] += [
    wiki("Colônia_Juliano_Moreira",
        "Foi fundada em 1924 com o objetivo de abrigar os internos das colônias psiquiátricas da Ilha do Governador [...] "
        "A partir dos anos 80, reduziu o escopo de suas atividades até ser fechada completamente em 2022 em resposta ao progresso da luta antimanicomial.",
        nome="Colônia Juliano Moreira (pt)", idioma="pt"),
    {"url": "https://www.scielo.br/j/anp/a/M96PpVryDbWFgW5bnQWn7Wc/?lang=en",
     "titulo": "Juliano Moreira (Arquivos de Neuro-Psiquiatria, SciELO)", "idioma": "en",
     "trecho": "Moreira joined the Medical School of Bahia (FAMEB) in 1886 at the age of 14, two years prior to the abolition of slavery in Brazil."},
    {"url": "https://www.scielo.br/j/rbp/a/wzF5QyZ7pVvVVF5VqRHwSHf/",
     "titulo": "Juliano Moreira (Revista Brasileira de Psiquiatria, SciELO)", "idioma": "pt",
     "trecho": "a abolição do uso de coletes e camisas de força; a retirada de grades de ferro das janelas"},
]

# 0010: três frases reescritas com palavras próprias
trocar(10, nota_surpresa=3)
substituir(10, "explicacao",
    "Na construção da ferrovia que ligaria Bauru, em São Paulo, a Mato Grosso, eram comuns os casos da \"úlcera de Bauru\"",
    "Os operários que abriam a ferrovia de Bauru (SP) rumo a Mato Grosso sofriam muito com a chamada \"úlcera de Bauru\"")
substituir(10, "explicacao", "As feridas dos pacientes secaram, e ele apresentou",
    "Com o novo tratamento, as lesões cicatrizaram, e ele apresentou")
substituir(10, "explicacao",
    "levou no rosto um jato do líquido da cavidade torácica, que entrou pela boca e pelo nariz",
    "foi atingido no rosto por líquido contaminado que esguichou do tórax do cadáver e lhe chegou à boca e ao nariz")

# 0011: papel da Embrapa sem exclusividade; "em grande parte"
trocar(11, nota_surpresa=3)
substituir(11, "explicacao",
    "A virada veio com a pesquisa agropecuária. Pesquisadores da Embrapa, empresa pública criada em 1973, descobriram que o solo podia ser corrigido com fósforo e calcário",
    "A pesquisa agronômica, com papel central da Embrapa (empresa pública criada em 1973), mostrou que o solo podia ser corrigido com fósforo e calcário")
substituir(11, "explicacao", "e a expansão da soja é o principal motor da perda",
    "e a perda é puxada em grande parte pela expansão da soja")

# 0012: sem o "cerca de metade", número antigo
substituir(12, "explicacao",
    "Isso pesa no mundo: Brasil e EUA produzem cerca de metade da soja do planeta, uma das principais fontes de proteína, em geral via ração animal.",
    "Isso pesa no mundo: Brasil e EUA são os maiores produtores de soja, uma das principais fontes de proteína do planeta, consumida sobretudo como ração animal.")

# 0013: o que o software deduz, a sonda dos motores comuns e o papel da Magneti Marelli
trocar(13, nota_surpresa=3)
substituir(13, "gancho", "para saber quanto álcool há no tanque", "para saber quanto álcool está queimando")
substituir(13, "gancho", "com a sonda que já mede a queima em qualquer motor com injeção",
    "com a sonda que os motores comuns já usam para avaliar a queima")
substituir(13, "explicacao",
    "A tecnologia foi desenvolvida pela subsidiária brasileira da Bosch em 1994 e lançada comercialmente em 2003, no Gol Total Flex.",
    "A filial brasileira da Bosch desenvolveu a tecnologia em 1994; aprimorada pela Magneti Marelli, ela chegou ao mercado "
    "em 2003, quando o Gol Total Flex inaugurou os carros flex.")
substituir_trecho(13, 0, "The technology was developed by the Brazilian subsidiary of Bosch in 1994 [...] ",
    "The technology was developed by the Brazilian subsidiary of Bosch in 1994, but was further improved and commercially implemented in 2003 by the Italian subsidiary of Magneti Marelli. [...] ")

# 0008: gancho dentro do limite de 220 caracteres
substituir(8, "gancho", "por mosquitos que tinham sugado o sangue de um doente.", "por mosquitos que sugaram sangue de um doente.")
