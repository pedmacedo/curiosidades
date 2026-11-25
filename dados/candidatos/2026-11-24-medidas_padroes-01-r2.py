"""Rodada 2 de Medidas e padrões: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-medidas_padroes-01.py"))
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


# 0001: comparações a cada ~40 anos; suspeita do mercúrio; campanha de 2014 não confirmou o afastamento
substituir(1, "explicacao", "e as comparações com o original foram raras: só três, em 1889, 1948 e 1989.",
    "e as comparações com o original foram raras, feitas em grandes campanhas separadas por décadas.")
substituir_trecho(1, 0, "The only three verifications occurred in 1889, 1948, and 1989. [...] ", "")
acrescentar_trecho(1, 0, "These were compared to the IPK roughly every 40 years")
substituir(1, "explicacao", "Nenhum mecanismo plausível foi proposto para explicar a deriva.",
    "A causa da deriva nunca foi esclarecida; uma das suspeitas é a contaminação da superfície, inclusive por "
    "mercúrio de instrumentos guardados perto.")
acrescentar_trecho(1, 0, "suggested that one source of the divergence between the various prototypes could be traced to mercury")
substituir(1, "explicacao", "as primeiras cópias ganharam, em média, cerca de 25 microgramas.",
    "as primeiras cópias ganharam, em média, cerca de 25 microgramas. Uma campanha extra de calibração em 2014 "
    "não confirmou que esse afastamento tivesse continuado depois de 1992.")
CANDIDATOS[0]["fontes"].append({
    "url": "https://iopscience.iop.org/article/10.1088/0026-1394/52/2/310",
    "titulo": "Calibration campaign against the international prototype of the kilogram in anticipation of the redefinition "
              "of the kilogram part I: comparison of the international prototype with its official copies (Metrologia, 2015)",
    "idioma": "en",
    "trecho": "at the beginning of the campaign (December 2013), in July 2014, and at the end of the long-term recontamination study "
              "(November 2014). [...] since the 3rd Periodic Verification of National Prototypes of the Kilogram (1988–1992). "
              "These results do not confirm the trend for the masses of the six official copies to diverge from the mass of the IPK",
})

# 0002: "atual", e a consequência (segundos bissextos em 1972)
substituir(2, "explicacao",
    "o segundo do SI já nasceu um pouco mais curto que o segundo solar médio da época em que foi adotado.",
    "o segundo do SI já nasceu um pouco mais curto que o segundo solar médio atual, e esse descompasso levou à "
    "criação dos segundos bissextos, em 1972.")
acrescentar_trecho(2, 3, "This led to the introduction of the leap second in 1972 to compensate for differences in the bases for time standardization.")

# 0003: pagamentos parciais; projeto conferido e ajustado; sem a data final do teste
substituir(3, "explicacao",
    "e ele só recebeu 8.750 libras do Parlamento em 1773, aos 80 anos, depois que o rei Jorge III testou um dos seus relógios e tomou o seu partido.",
    "e só em 1773, aos 80 anos, depois que o rei Jorge III testou um dos seus relógios e tomou o seu partido, o "
    "Parlamento lhe pagou 8.750 libras, somadas a pagamentos parciais que ele já recebera.")
substituir(3, "explicacao",
    "De 6 de janeiro a 17 de abril de 2015, ela funcionou numa caixa transparente no Observatório Real, sem ser tocada além da corda, e perdeu só 5/8 de segundo.",
    "Lá, o projeto foi conferido e ajustado e, por 100 dias a partir de 6 de janeiro de 2015, o relógio funcionou "
    "numa caixa transparente no Observatório Real, sem ser tocado além da corda, e perdeu só 5/8 de segundo.")
acrescentar_trecho(3, 0, "so the clock's design was carefully checked and adjusted [...] "
    "He received £4,315 in increments from the Board of Longitude for his work, £10,000 as an interim payment for H4 in 1765 and £8,750 from Parliament in 1773.")

# 0005: padrões baseados nos ingleses; fim do pé de agrimensura "no fim de 2022"
substituir(5, "explicacao",
    "Os padrões de referência das unidades tradicionais eram uma jarda e uma libra vindas da Inglaterra, mas a jarda imperial de 1855 se mostrou instável",
    "Os padrões de referência das unidades tradicionais eram baseados nos ingleses, mas a jarda imperial de "
    "1855, que os EUA usavam como padrão, se mostrou instável")
substituir(5, "explicacao",
    "Só em 31 de dezembro de 2022 o NIST e outros órgãos federais declararam obsoleto o pé de agrimensura.",
    "Só no fim de 2022 o NIST e outros órgãos federais aposentaram de vez o pé de agrimensura.")
acrescentar_trecho(5, 0, "one of them was adopted as the United States national standard yard")

# 0008: "muitas vezes"; quem notou a falha da regra de Galileu foram Mersenne e outros
substituir(8, "gancho", "acabavam balançando em sincronia", "muitas vezes entravam em sincronia")
substituir(8, "explicacao",
    "Huygens também percebeu que a regra de Galileu não é perfeita: balanços largos demoram um pouco mais que os estreitos. Mostrou, com geometria,",
    "Mersenne e outros já tinham notado que a regra de Galileu não é perfeita: balanços largos demoram um pouco "
    "mais que os estreitos. Huygens mostrou, com geometria,")

# 0009: "vários países"; a "nova vela" de 1937/1948; sem a lâmpada de Hefner
substituir(9, "explicacao", "Antes de 1948, cada país tinha o seu padrão de intensidade luminosa",
    "Antes de 1948, vários países usavam padrões próprios de intensidade luminosa")
substituir(9, "explicacao", "mas impurezas tornaram a ideia difícil de pôr em prática.",
    "mas impurezas tornaram a ideia difícil de pôr em prática. A solução veio décadas depois, com a platina "
    "derretida servindo de radiador ideal, e em 1948 essa \"nova vela\", com valor escolhido para ficar próximo da "
    "antiga unidade de vela, foi oficializada com o nome de candela.")
substituir(9, "explicacao", "Alemanha, Áustria e países escandinavos preferiam a lâmpada de Hefner. ", "")
acrescentar_trecho(9, 0, "In 1937, the Commission Internationale de l'Éclairage (International Commission on Illumination) and the CIPM proposed "
    "a \"new candle\" based on this concept, with value chosen to make it similar to the earlier unit candlepower. [...] "
    "It was then ratified in 1948 by the 9th CGPM which adopted a new name for this unit, the candela.")

# 0010: 1,72 ms por século (a Lua sozinha daria 2,4; o soerguimento pós-glacial compensa)
substituir(10, "explicacao",
    "Esses registros indicam que o dia aumentou cerca de 2,3 milissegundos por século desde então.",
    "Esses registros indicam que, nos últimos 2.700 anos, o dia aumentou em média cerca de 1,72 milissegundo por "
    "século, um pouco menos do que a Lua sozinha faria (2,4), porque a crosta ainda se recupera do peso das "
    "geleiras da última era do gelo, o que acelera um pouco a rotação.")
acrescentar_trecho(10, 0, "From the observed change in the Moon's orbit, the corresponding change in the length of the day can be computed [...] "
    "+2.4 ms/d/century [...] However, from historical records over the past 2700 years the following average value is found: "
    "+1.72 ± 0.03 ms/d/century [...] "
    "The explanation is that during the ice age large masses of ice collected at the poles, and depressed the underlying rocks. "
    "The ice mass started disappearing over 10000 years ago, but Earth's crust is still not in hydrostatic equilibrium and is still rebounding [...] "
    "This process alone leads to an increase of the rotation rate")
substituir_trecho(10, 1, "Analysis of historical astronomical records shows a slowing trend; the length of a day has increased by about 2.3 milliseconds per century since the 8th century BCE. [...] ", "")
# 0010: para não passar de 250 palavras, sai a frase dos sedimentos de 620 milhões de anos
substituir(10, "explicacao", "Sedimentos de maré de 620 milhões de anos são compatíveis com um dia de 21,9 horas. ", "")

# 0011: foco nos padrões perdidos e no plano B que falhou
trocar(11,
    temas_secundarios=["falhas_engenharia"],
    gancho="Uma lei inglesa de 1824 tinha um plano B: se a jarda e a libra-padrão se perdessem, seriam refeitas com um "
           "pêndulo e a massa de água. Em 1834, um incêndio no Parlamento as destruiu, e o plano B não funcionou.",
    explicacao=(
        "Em 16 de outubro de 1834, a queima de velhas varetas de contabilidade do Tesouro numa fornalha sob a Câmara "
        "dos Lordes provocou o incêndio que destruiu a maior parte do Palácio de Westminster. Entre as perdas estavam "
        "os padrões britânicos da jarda e da libra. Uma lei de 1824 tinha previsto um acidente assim: além dos "
        "protótipos, definia constantes físicas para recriá-los. A jarda seria reconstituída a partir do comprimento "
        "de um pêndulo que bate segundos na latitude de Greenwich, ao nível do mar e no vácuo, fixado em 39,1393 "
        "polegadas. A libra viria da massa de uma polegada cúbica de água destilada, sob pressão de 30 polegadas de "
        "mercúrio e a 62 graus Fahrenheit, fixada em 252,458 grãos, sendo 7.000 grãos uma libra. Na prática, foi "
        "impossível refazer os padrões a partir dessas definições. Uma lei de 1855 autorizou recriar os protótipos a "
        "partir de cópias secundárias reconhecidas, e a perda levou a uma reforma do sistema britânico de pesos e "
        "medidas. Um inquérito, de 1838 a 1841, comparou os dois sistemas de peso em uso no país, o avoirdupois e o "
        "troy, e decidiu que o avoirdupois seria o adotado; o troy ficou restrito a ouro, prata e pedras preciosas."
    ),
)
substituir_trecho(11, 1,
    "For the pound, the mass of a cubic inch of distilled water [...] ",
    "For the pound, the mass of a cubic inch of distilled water at an atmospheric pressure of 30 inches of mercury and a temperature "
    "of 62° Fahrenheit was defined as 252.458 grains, with there being 7,000 grains per pound. ")
acrescentar_trecho(11, 0, "An inquiry that ran from 1838 to 1841 considered the two competing systems used in the country, the avoirdupois and troy "
    "measures, and decided that avoirdupois would be used forthwith; troy weights were retained solely for gold, silver and precious stones.")

# 0014: "para evitar que o governo impusesse um sistema"
substituir(14, "gancho", "justamente para evitar uma lei", "para evitar que o governo impusesse um sistema")
if len(CANDIDATOS[13]["gancho"]) > 220:
    substituir(14, "gancho", "Antes, uma só ferrovia tinha sete zonas de horário na linha.",
               "Antes, uma só ferrovia usava sete horários na linha.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(3, "explicacao", "O Guinness a declarou o relógio mecânico mais preciso", "O Guinness o declarou o relógio mecânico mais preciso")
substituir(5, "explicacao", "a jarda imperial de 1855, que os EUA usavam como padrão, se mostrou instável", "a jarda imperial de 1855, da qual os EUA usavam uma cópia como padrão, se mostrou instável")
substituir(9, "explicacao", "com a platina derretida servindo de radiador ideal", "com uma cavidade imersa em platina derretida servindo de corpo negro")
substituir(9, "explicacao", "em geral baseado na chama", "em geral baseados na chama")
substituir(9, "explicacao", "uma vela comum emite mais ou menos uma candela", "uma vela comum emite cerca de uma candela")
substituir(9, "explicacao", "usada justamente em velas", "usada em velas")
substituir(11, "explicacao", "fixada em 252,458 grãos, sendo 7.000 grãos uma libra.", "fixada em 252,458 grãos.")
