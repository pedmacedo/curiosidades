"""Rodada 2 de Costumes e rituais: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-costumes_rituais-01.py"))
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

# 0004: o uso como incentivo é tradição
trocar(4, confianca="consenso_parcial")
substituir(4, "gancho", "A ameaça era usada nas fazendas", "Segundo a tradição, a ameaça era usada nas fazendas")

# 0005: "comeu", não "almoçou"; "muitos" modelos
substituir(5, "gancho", "e almoçou sopa, cerveja e salsichas lá embaixo", "e comeu sopa, cerveja e salsichas lá embaixo")
substituir(5, "explicacao", "dezenas de modelos de \"caixão de segurança\" foram patenteados", "muitos modelos de \"caixão de segurança\" foram patenteados")

# 0008: a ligação com a peste é suspeita e debatida
trocar(8, confianca="consenso_parcial")
substituir(8, "explicacao",
    "O contato direto com os corpos tem um lado perigoso: a prática é associada à transmissão da peste pneumônica no país, e o governo proibiu fazê-la com quem morreu da doença",
    "O contato direto com os corpos pode ter um lado perigoso: suspeita-se que a prática contribua para a transmissão da peste pneumônica no país, embora a força dessa ligação seja debatida, e o governo proibiu fazê-la com quem morreu da doença")

# 0009: texto próprio; "segundo os relatos"; sem historia_humana
trocar(9, tipos_espanto=["escala_absurda", "contraintuitivo"])
substituir(9, "explicacao",
    "Os Sateré-Mawé chamam o ritual de Wyamat e se referem a ele como \"meter a mão na luva\"; na região, é conhecido como Festa da Tocandira. "
    "É um rito de passagem em que os adolescentes se tornam homens, e tradicionalmente o evento que reúne os clãs desse povo. "
    "Os cantadores entoam, durante todo o ritual, cantos épicos que narram o mito de origem, o surgimento dos clãs e as guerras, inclusive a participação dos Sateré-Mawé na Cabanagem. "
    "As luvas são tecidas em palha, pintadas com jenipapo e enfeitadas com penas de arara e gavião.",
    "Os Sateré-Mawé, do Amazonas, chamam o ritual de Wyamat e o descrevem como \"meter a mão na luva\"; os vizinhos não indígenas o "
    "conhecem como Festa da Tocandira. É a cerimônia que marca a passagem dos meninos à vida adulta e, tradicionalmente, o momento em "
    "que os clãs se reúnem. Enquanto ela dura, cantadores entoam longos cantos que contam a origem do povo, o nascimento dos clãs e suas "
    "guerras, entre elas a Cabanagem. As luvas, trançadas em palha, recebem pintura de jenipapo e penas de arara e de gavião.")
substituir(9, "explicacao", "Para completar a iniciação, a prova é repetida 20 vezes, ao longo de meses ou anos.",
    "Segundo os relatos, a iniciação só se completa depois de umas 20 provas, espalhadas por meses ou anos.")

# 0010: "pelo menos seis"; cronologia
substituir(10, "gancho", "Nos EUA, seis estados já proibiram por lei dar gorjeta.", "Nos EUA, pelo menos seis estados já proibiram por lei dar gorjeta.")
substituir(10, "explicacao", "Seis estados aprovaram leis contra a gorjeta", "Pelo menos seis estados aprovaram leis contra a gorjeta")
substituir(10, "explicacao", "A gorjeta começou na Inglaterra dos Tudor. Na Idade Média, era um costume entre senhor e servo:",
    "A gorjeta tem raízes inglesas. Na origem, era um costume entre senhor e servo:")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(8, "explicacao", "e o governo proibiu fazê-la com quem morreu da doença, embora haja relatos de que a regra é desrespeitada.",
    "e o governo proibiu fazê-la com quem morreu da doença, mas há relatos de que a regra é desrespeitada.")
