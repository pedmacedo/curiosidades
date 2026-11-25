"""Rodada 2 de Fronteiras e países: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-fronteiras_paises-01.py"))
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


# notas revistas pelo verificador (fatos aprovados sem mudança de texto)
trocar(4, nota_surpresa=5)
trocar(6, nota_surpresa=3)
trocar(11, nota_surpresa=3)

# 0003: o que se alterna é a administração, não o país (a soberania é conjunta)
substituir(3, "gancho",
    "troca de país a cada seis meses: é espanhola de fevereiro a julho e francesa de agosto a janeiro.",
    "muda de mãos a cada seis meses: fica sob administração da Espanha de fevereiro a julho e da França de agosto a janeiro.")

# 0008: Nunavut não assinou; a divisão foi "quase" ao meio
substituir(8, "gancho",
    "Em 2022, dividiram a ilha ao meio, e os dois países ganharam uma fronteira terrestre.",
    "Em 2022, dividiram a ilha em duas, e os dois países ganharam uma fronteira terrestre.")
substituir(8, "explicacao",
    "Em junho de 2022, os dois governos e os da Groenlândia e de Nunavut assinaram a divisão da ilha quase ao meio,",
    "Em junho de 2022, Canadá, Dinamarca e Groenlândia assinaram a divisão da ilha quase ao meio,")

# 0010: a indefinição vale para a maior parte do lago (o Obersee); posição alemã descrita de formas diferentes
trocar(10, tipos_espanto=["contraintuitivo"],
    gancho="No lago de Constança, entre Alemanha, Suíça e Áustria, nunca se acertou onde passa a fronteira na maior "
           "parte do lago, longe das margens. A Suíça diz que é no meio; a Áustria, que a área é de todos.")
substituir(10, "explicacao", "Para o resto do lago, não existe nenhum acordo",
    "Para a maior parte do resto do lago, a porção principal chamada Obersee, não existe nenhum acordo")
substituir(10, "explicacao", "A Alemanha mantém uma posição ambígua.",
    "A posição da Alemanha é descrita de formas diferentes: ambígua, segundo algumas fontes, ou próxima da "
    "austríaca, segundo o órgão de cartografia da Suíça.")
CANDIDATOS[9]["fontes"].append({
    "url": "https://www.swisstopo.admin.ch/en/technical-boundary-in-lake-constance",
    "titulo": "Technical boundary in the Lake Constance",
    "idioma": "en",
    "trecho": "Did you know that there are no legally valid international boundaries for the largest part of Lake Constance - the so-called Obersee (Upper Lake)? "
              "Switzerland is assuming a real sharing in the middle of the lake. "
              "Germany and Austria regard the Obersee as a condominium in the joint control of the neighbouring countries.",
})

# 0014: a vila continua na área alfandegária alemã
substituir(14, "explicacao",
    "Até a Áustria entrar na União Europeia, em 1995, a vila fazia parte da área alfandegária alemã, e usou o "
    "marco alemão até a chegada do euro, em 2002.",
    "Antes mesmo de a Áustria entrar na União Europeia, em 1995, a vila já ficava na área alfandegária alemã, e "
    "ainda hoje aplica as alíquotas alemãs de imposto sobre consumo; até a chegada do euro, em 2002, usava o "
    "marco alemão.")

# 0016: sai a lenda do cavalo (e as fontes de Melgarejo); Gálvez sem o cargo de cônsul; rendição só com o mês
trocar(16, tipos_espanto=["historia_humana", "contraintuitivo"])
substituir(16, "explicacao",
    " Daí a fragilidade de uma história famosa: "
    "conta-se que o ditador boliviano Mariano Melgarejo deu ao Brasil uma enorme área em troca de um cavalo "
    "branco, marcando o mapa com o casco do animal. O tratado de limites assinado no governo dele, porém, "
    "foi justamente o de 1867, que deu terras ao Brasil, mas deixou o Acre com a Bolívia.",
    "")
substituir(16, "explicacao",
    "chefiada pelo espanhol Luis Gálvez, que tinha sido cônsul boliviano em Belém.",
    "chefiada pelo espanhol Luis Gálvez.")
substituir(16, "explicacao",
    "em 15 de março de 1900, uma flotilha de guerra brasileira chegou a Puerto Alonso",
    "em março de 1900, uma flotilha de guerra brasileira chegou a Puerto Alonso")
CANDIDATOS[15]["fontes"] = [f for f in CANDIDATOS[15]["fontes"] if "Melgarejo" not in f["url"]]
acrescentar_trecho(14, 0, "Even after the introduction of the euro as the EU's common currency, Jungholz, as a German customs-union area, continues to apply German VAT rates.")
