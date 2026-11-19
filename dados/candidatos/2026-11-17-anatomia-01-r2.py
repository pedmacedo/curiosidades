"""Rodada 2 de Anatomia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-17-anatomia-01.py"))
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


# 0002: só o nervo esquerdo contorna a aorta
substituir(2, "gancho", "O nervo que comanda a laringe desce", "O nervo esquerdo que comanda a laringe desce")

# 0003: estimativa de um modelo; nutrição é suspeita
trocar(3, confianca="consenso_parcial")
substituir(3, "explicacao", "aposta na nutrição:", "suspeita da nutrição:")

# 0005: a fronteira ar/lágrima (não a "lisura") é o principal componente da refração
substituir(5, "explicacao",
    "A lisura da superfície entre o ar e o filme de lágrima importa muito: é ela o componente mais importante "
    "do poder de refração do olho, e qualquer irregularidade ali piora a visão.",
    "A fronteira entre o ar e o filme de lágrima é o componente mais importante do poder de refração do olho, "
    "e qualquer irregularidade ou inchaço desse epitélio piora a visão.")

# 0007: revisão de 2017; não é mito desmentido, é hipótese
trocar(7, tipos_espanto=["contraintuitivo", "misterio_aberto"])
substituir(7, "explicacao", "e foi perdido no máximo seis vezes.",
    "e foi perdido no máximo seis vezes. Uma revisão de 2017, com dados atualizados, chegou a números parecidos: "
    "ao menos 29 surgimentos e no máximo 12 perdas.")
substituir(7, "explicacao", "A ideia é aceita como plausível, mas ainda é uma hipótese.",
    "A ideia ganhou apoio, mas ainda é uma hipótese.")
acrescentar_trecho(7, 0, "A 2017 study of an updated database yielded similar results, with estimates of at least 29 gains and at most 12 losses")

# 0009: ressalvas e a exceção da superalimentação
trocar(9, confianca="consenso_parcial")
substituir(9, "gancho", "ele se define na infância", "ele tende a se definir na infância")
substituir(9, "explicacao", "tem células maiores, não mais numerosas.", "em geral tem células maiores, não mais numerosas.")
substituir(9, "explicacao", "Reduzir esse número com dieta é difícil.",
    "Há exceções: num experimento de superalimentação com adultos, o número de células de gordura da parte "
    "inferior do corpo aumentou. Reduzir esse número com dieta é difícil.")
acrescentar_trecho(9, 0, "Body fat cells have regional responses to the overfeeding that was studied in adult subjects. [...] "
    "the number of lower-body adipocytes did significantly increase during the course of experiment.")

# 0010: 80% da população; desvio de septo como na fonte
trocar(10, gancho="Na maioria das pessoas, o ar passa mais por uma narina do que pela outra, e as duas se revezam sem que se perceba, num ciclo que dura em média duas horas e meia.")
substituir(10, "explicacao",
    "Quem tem desvio de septo costuma sentir o ciclo: a sensação de nariz entupido muitas vezes acompanha a fase "
    "de congestão do lado mais estreito.",
    "Em quem tem desvio de septo e obstrução nasal intermitente, o ciclo fica evidente: a sensação de nariz "
    "entupido muitas vezes acompanha a fase de congestão.")

# 0011: os mapas de Blaschko não cobriam cabeça, rosto e pescoço
substituir(11, "explicacao", "montou um esquema do corpo humano inteiro.",
    "montou um esquema do corpo humano. A cabeça, o rosto e o pescoço só foram mapeados décadas depois, por "
    "outros dermatologistas.")
acrescentar_trecho(11, 0, "expanded the map of the lines over the human body to include areas of the head, face, and neck, where Blaschko's original maps did not cover.")

# 0012: novidade contestada
trocar(12, gancho="Em 2020, médicos holandeses anunciaram ter achado, por acaso, um par de glândulas salivares no fundo do nariz. Alguns anatomistas contestam que seja algo novo.")
substituir(12, "explicacao", "efeitos colaterais do tratamento de câncer de cabeça e pescoço.",
    "efeitos colaterais do tratamento de câncer de cabeça e pescoço. A descoberta, porém, não é unânime: "
    "anatomistas contestam que essas glândulas tenham sido descobertas só agora.")
CANDIDATOS[11]["fontes"].append(wiki("Tubarial_salivary_gland",
    "The claim that this organ was only recently discovered has been disputed by anatomists.", nome="Tubarial salivary gland"))

# 0014: a hipótese foi questionada; confiança "hipotese"
trocar(14, confianca="hipotese")
substituir(14, "explicacao", "Uma não exclui a outra.",
    "Uma não exclui a outra. E a própria hipótese do olho cooperativo foi questionada por estudos que compararam "
    "o comportamento de seguir o olhar com os padrões de pigmentação dos olhos de humanos e grandes macacos.")
acrescentar_trecho(14, 0, "The cooperative eye hypothesis has been questioned based on examinations of the correspondence between known eye-gaze following behaviors and patterns of (de)pigmentation leading to conspicuous eye appearances in hominoids.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
# 0005: baixa rejeição em transplantes
substituir(5, "explicacao", "e qualquer irregularidade ou inchaço desse epitélio piora a visão.",
    "e qualquer irregularidade ou inchaço desse epitélio piora a visão. A falta de vasos traz outra vantagem: "
    "no transplante de córnea, feito com a córnea de um doador falecido, há poucos problemas de rejeição.")
acrescentar_trecho(5, 0, "If the corneal stroma develops visually significant opacity, irregularity, or edema, a cornea of a deceased donor can be transplanted. "
    "Because there are no blood vessels in the cornea, there are also few problems with rejection of the new cornea.")
# 0012: "segundo os pesquisadores"
substituir(12, "explicacao", "Até então se sabia que ali só havia glândulas microscópicas, até mil, espalhadas pela mucosa.",
    "Segundo os pesquisadores, até então só se conheciam ali glândulas microscópicas, até mil, espalhadas pela mucosa.")
