"""Rodada 2 de Espionagem: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-espionagem-01.py"))
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


# 0003: a tinta invisível ia nas partituras, não na pele
substituir(3, "explicacao",
    "As informações iam escritas nas mãos e nos braços, em tinta invisível, ou em bilhetes presos por dentro da roupa, até na roupa de baixo.",
    "As informações iam anotadas nas mãos e nos braços, escritas em tinta invisível nas partituras que ela levava, "
    "ou em bilhetes presos por dentro da roupa, até na roupa de baixo.")
acrescentar_trecho(3, 0, "Notes were written in invisible ink on Baker's sheet music.")
trocar(3, nota_surpresa=3)

# 0004: uma produtora (escritório), não um estúdio; menção ao filme de 2012
substituir(4, "gancho", "a CIA abriu em Hollywood um estúdio de fachada", "a CIA abriu em Hollywood uma produtora de fachada")
substituir(4, "explicacao", "os dois governos esconderam o papel da CIA, revelado só em 1997.",
    "os dois governos esconderam o papel da CIA, revelado só em 1997. A operação inspirou, com muitas liberdades, "
    "o filme Argo, de 2012.")
acrescentar_trecho(4, 0, "The article was used loosely—alongside a memoir Mendez wrote—by Chris Terrio as the basis of the 2012 film Argo.")
trocar(4, nota_surpresa=3)

# 0005: separar os dois argumentos; quem armou a armadilha (Nicolai)
substituir(5, "gancho", "foi um bode expiatório: as mensagens que a denunciaram usavam",
    "foi um bode expiatório, e as mensagens que a denunciaram usavam")
substituir(5, "explicacao", "o que sugere uma armadilha para entregá-la.",
    "o que sugere uma armadilha para entregá-la, montada pelos próprios alemães, insatisfeitos com as fofocas que "
    "ela lhes vendia.")
acrescentar_trecho(5, 0, "General Walter Nicolai, the chief intelligence officer of the German Imperial Army, had grown annoyed that "
    "Mata Hari had provided no real intelligence, instead selling the Germans mere Paris gossip [...] "
    "and decided to terminate her employment by exposing her as a German spy to the French.")

# 0007: 1929 ou 1930; sem a frase de Benedict Arnold
substituir(7, "gancho", "só foi identificado em 1929, quando um historiador", "só foi identificado por volta de 1930, quando um historiador")
substituir(7, "gancho", "A rede de espiões de George Washington", "A rede de espiões de Washington")
acrescentar_trecho(7, 1, "The identity of Samuel Culper, Jr. was discovered only in 1930 by the New York historian Morton Pennypacker.")
substituir(7, "explicacao", "O historiador Morton Pennypacker notou",
    "Por volta de 1930 (as fontes variam entre 1929 e 1930), o historiador Morton Pennypacker notou")
substituir(7, "explicacao",
    "Em 1780, a rede descobriu que um oficial americano de alta patente, depois identificado como Benedict Arnold, "
    "tramava entregar aos britânicos o forte de West Point. ", "")
substituir_trecho(7, 0,
    "In 1780, the Culper Ring discovered that a high-ranking American officer, subsequently identified as Benedict Arnold, "
    "was plotting with British Major John André to turn over the vitally important American fort at West Point [...] ", "")

# 0008: sem a ruptura de Argentina, Bolívia e Chile com o Eixo
substituir(8, "explicacao", "Depois que a rede caiu, Argentina, Bolívia e Chile romperam com o Eixo. ", "")
substituir_trecho(8, 0, "After the spy ring was broken, Argentina, Bolivia and Chile broke with the Axis powers and supported the Allies. [...] ", "")

# 0009: "anteriores"; a estimativa de 10 a 25 é de setembro de 1961 (NIE 11-8/1-61)
substituir(9, "gancho", "mais imagens da URSS que todos os voos do avião espião U-2",
    "mais imagens da URSS que todos os voos anteriores do avião espião U-2")
substituir(9, "explicacao", "um mês depois do voo, a conta caiu para 10 a 25.",
    "em setembro de 1961, depois de mais um ano de fotos do Corona e de outras fontes, a estimativa oficial caiu "
    "para 10 a 25.")
substituir_trecho(9, 0, "A month after the flight of Discoverer 14, that estimate was refined to just 10–25. [...] ", "[...] ")
CANDIDATOS[8]["fontes"].append({
    "url": "https://history.state.gov/historicaldocuments/frus1961-63v08/d45",
    "titulo": "National Intelligence Estimate 11-8/1-61, 21 de setembro de 1961 (Foreign Relations of the United States, 1961–1963, vol. VIII)",
    "idioma": "en",
    "trecho": "Washington, September 21, 1961. [...] We now estimate that the present Soviet ICBM strength is in the range of 10-25 launchers",
})

# 0011: quem foi avisado logo depois da confissão
substituir(11, "explicacao", "A rainha só foi informada oficialmente em 1973.", "O secretário particular da rainha foi avisado logo depois.")

# 0014: o papel de Julia é incerto; sem mito_desmentido
trocar(14, tipos_espanto=["conexao_inesperada", "engenhosidade"], nota_surpresa=3)
substituir(14, "explicacao",
    "A versão popular de que Julia inventou o repelente cozinhando é exagero: segundo a CIA, ela trabalhava perto dos oficiais que desenvolveram a fórmula.",
    "O tamanho do papel dela é incerto: há relatos de que ela mesma cozinhava misturas de teste, mas a CIA diz apenas "
    "que ela trabalhava perto dos oficiais que criaram a fórmula, embora Julia falasse no repelente \"que desenvolvemos\".")
substituir(14, "explicacao",
    "Os pesquisadores testaram mais de 100 substâncias, de extratos de carne de tubarão podre a sais de cobre.",
    "Os pesquisadores testaram mais de 100 substâncias; entre as mais promissoras estavam extratos de carne de "
    "tubarão podre e sais de cobre.")
acrescentar_trecho(14, 0, "I understand the shark repellent we developed is being used today for downed space equipment")

# 0015: a data exata é questão de historiadores, não "mito" comprovado
substituir(15, "gancho", "Que ele deu a data exata é mito.", "Já a data exata, ele provavelmente nunca deu.")
substituir(15, "explicacao",
    "Mas, segundo o historiador Gordon Prange, Sorge nunca chegou a dar a data certa, 22 de junho: o mais perto foi 20 de junho.",
    "Diz a lenda que ele cravou o dia, 22 de junho. O historiador Gordon Prange não aceitou essa versão: concluiu, "
    "em 1984, que o mais perto que Sorge chegou foi 20 de junho, e que o próprio espião nunca disse ter sabido a "
    "data certa.")
trocar(15, confianca="consenso_parcial")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(7, "gancho", "A rede de espiões de Washington era", "A rede de espiões de George Washington era")
substituir(7, "gancho", "Um dos líderes só foi identificado", "Um líder só foi identificado")
