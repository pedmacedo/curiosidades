"""Rodada 2 de Contabilidade brasileira: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-contabilidade_brasileira-01.py"))
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


# 0001: "precedente", não descendência; "em parte"; "com frequência", parte ou todo o quinto
substituir(1, "gancho", "tem um antecedente islâmico: o khums", "teve um precedente islâmico: o khums")
substituir(1, "explicacao", "Do lado cristão, o imposto vinha também de outra ideia medieval:",
    "Nos reinos cristãos, a fonte aponta que o imposto vinha, ao menos em parte, de uma ideia medieval:")
substituir(1, "explicacao", "os reis às vezes abriam mão de parte do quinto",
    "os reis com frequência abriam mão de parte ou de todo o quinto")
acrescentar_trecho(1, 0, "Nonetheless, to encourage exploration and colonization, Iberian monarchs often allowed explorers and colonial developers to retain part or all of the royal fifth")

# 0002: o gancho não generaliza a proibição do ouro em pó
substituir(2, "gancho",
    "No Brasil colonial, o ouro só podia circular fundido em barras com a marca da Coroa, prova de que o quinto fora pago.",
    "Nas casas de fundição do Brasil colonial, o ouro virava barra com a marca da Coroa, prova de que o quinto fora pago.")

# 0007: origem da Casa dos Contos e o Ministério da Fazenda como descendente
substituir(7, "explicacao", "As contas do reino eram conferidas desde o fim do século XIII pela Casa dos Contos de Lisboa.",
    "As contas do reino eram conferidas pela Casa dos Contos, órgão com origens no fim do século XIII.")
substituir(7, "explicacao",
    "Com a Independência, a parte que ficou no Brasil virou o Tesouro Público e, em 1824, ganhou o nome de Ministério da Fazenda.",
    "Com a Independência, a parte que ficou no Brasil virou o Tesouro Público, antepassado direto do atual Ministério da Fazenda.")
acrescentar_trecho(7, 1, "O Real Erário, ressalvadas as diferenças institucionais, foi o antepassado direto do atuais Ministério das Finanças de Portugal, Tribunal de Contas de Portugal, Ministério da Fazenda do Brasil")

# 0008: causalidade mais branda; a proposta de 5% foi de uma comissão presidida pelo ministro
substituir(8, "gancho", "Na virada de 1880, um imposto", "Em 1880, um imposto")
substituir(8, "gancho", "e derrubou o gabinete.", "e ajudou a derrubar o gabinete.")
substituir(8, "explicacao", "Desgastado, o gabinete caiu", "Desgastado também pela revolta, o gabinete caiu meses depois")
substituir(8, "explicacao", "Afonso Celso consultou financistas e propôs à Câmara um imposto de 5% sobre a renda",
    "Afonso Celso consultou financistas e uma comissão presidida por ele propôs à Câmara um imposto de 5% sobre a renda")

# 0011: a imunidade não atravessou o Estado Novo; voltou na Constituição de 1946 (art. 203)
trocar(11, gancho="A Constituição de 1934 proibiu impostos sobre a profissão de escritor, jornalista ou professor. A regra sumiu "
                  "em 1937, voltou em 1946 e só em 1964 esses rendimentos passaram de vez a pagar imposto de renda.")
substituir(11, "explicacao",
    "A proteção atravessou o Estado Novo e o pós-guerra; em 1947, uma lei ainda retirou da tributação os rendimentos de "
    "professor, jornalista, escritor, pintor e escultor e os direitos autorais.",
    "A Carta do Estado Novo, de 1937, deixou a regra de fora, mas a Constituição de 1946 a retomou: nenhum imposto "
    "incidiria diretamente sobre direitos de autor nem sobre a remuneração de professores e jornalistas. Em 1947, uma "
    "lei retirou da tributação os rendimentos de professor, jornalista, escritor, pintor e escultor e os direitos "
    "autorais.")
CANDIDATOS[10]["fontes"].append({
    "url": "https://www2.camara.leg.br/legin/fed/consti/1940-1949/constituicao-1946-18-julho-1946-365199-publicacaooriginal-1-pl.html",
    "titulo": "Constituição dos Estados Unidos do Brasil, de 18 de setembro de 1946 — Câmara dos Deputados",
    "idioma": "pt",
    "trecho": "Art. 203. Nenhum impôsto gravará diretamente os direitos de autor, nem a remuneração de professôres e jornalistas. [...] "
              "Rio de Janeiro, 18 de setembro de 1946",
})
acrescentar_trecho(11, 0, "A Constituição de 1937, que substituiu a de 1934")

# 0015: 15% contra 16% dos portugueses e 24% dos demais; sem 25%; tabaco/açúcar e tráfico corrigidos
trocar(15,
    gancho="Em 1810, um tratado com a Inglaterra fez os produtos ingleses pagarem só 15% de imposto para entrar no Brasil, "
           "menos que os 16% cobrados dos produtos do próprio Portugal. Os de outros países pagavam 24%.",
    explicacao=(
        "O acordo, negociado pelo diplomata britânico Lorde Strangford, foi assinado no Rio de Janeiro em 19 de "
        "fevereiro de 1810, com o governo português instalado no Brasil. Era a contrapartida da ajuda inglesa: a "
        "Inglaterra tinha ajudado a Corte a escapar do exército francês. A tarifa de 15% sobre o valor das mercadorias "
        "inglesas ficou abaixo da cobrada sobre as portuguesas, e por isso o tratado foi criticado como favorável "
        "demais aos britânicos. O efeito foi grande. Até 1808, um decreto de 1785 só permitia às fábricas brasileiras "
        "produzir tecido para roupa de escravos ou sacos para mantimentos. A proibição caiu com a abertura dos portos, "
        "mas os produtos da nascente Revolução Industrial britânica, mais baratos, logo dominaram o mercado e "
        "prejudicaram as manufaturas locais. O texto foi traduzido tão às pressas que a palavra policy, política, "
        "virou \"polícia\" na versão portuguesa. Num dos tratados de 1810, Portugal também se comprometeu a limitar a "
        "importação de escravizados africanos. Mais tarde, a tarifa foi uniformizada em 15%, o que apertou as "
        "finanças do governo; numa fase de maiores dificuldades fiscais, criou-se um imposto de 8% sobre as "
        "exportações."
    ))
substituir_trecho(15, 0, "Imported British goods only received a 15% duty, compared to 25% for goods from other nations. ", "[...] ")
CANDIDATOS[14]["fontes"].append(wiki("Tratados_de_1810",
    "Em 1810, D.João VI assinou vários tratados com a Inglaterra, que ficaram conhecidos como Tratados de 1810 e incluem o de Aliança e Amizade e o de Comércio e Navegação. "
    "Este foi de maior interesse pois concedia essencialmente a permissão de entrada de mercadorias inglesas pagando apenas o direito de 15% ad valorem. "
    "As decisões dos decretos de 28 de janeiro e de 11 de junho de 1808 foram revogadas pelo Tratado de 1810, que estabelecia a taxa de 15% para os comerciantes lusos, sobre as mercadorias inglesas; mantinha os 16% sobre as mercadorias portuguesas; e 24% sobre as mercadorias de outras origens. "
    "Os ingleses dominaram o mercado brasileiro. [...] "
    "beneficiando produtos da nascente Revolução Industrial [...] "
    "O acordo foi criticado pelo favorecimento excessivo à Inglaterra, já que a tarifa cobrada dos ingleses era menor do que de Portugal. "
    "Aliás, \"seu texto fora tão atropoeladamente traduzido do idioma inglês que a palavra policy, por exemplo, passou a significar, em português, polícia em lugar de política. "
    "Além do problema desse grande favorecimento, a invasão de produtos ingleses que se seguiu serviu para prejudicar as incipientes indústrias e manufaturas locais [...] "
    "O privilégio aduaneiro concedido à Inglaterra e a uniformização posterior da tarifa ao nível de 15% ad valorem criaram sérias dificuldades financeiras ao governo brasileiro. [...] "
    "Desta forma, foi introduzido um imposto de 8% ad valorem às exportações, na etapa de maiores dificuldades fiscais.",
    nome="Tratados de 1810", idioma="pt"))

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(1, "explicacao", "Nos reinos cristãos, a fonte aponta que o imposto vinha,", "Nos reinos cristãos, o imposto vinha,")
substituir(15, "explicacao", ' O texto foi traduzido tão às pressas que a palavra policy, política, virou "polícia" na versão portuguesa.', "")
substituir(15, "explicacao", "o que apertou as finanças do governo; numa fase de maiores dificuldades fiscais, criou-se um imposto de 8% sobre as exportações.", "o que apertou as finanças do governo.")
