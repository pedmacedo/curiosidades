"""Rodada 2 de Mundo islâmico medieval: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-mundo_islamico_medieval-01.py"))
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


# 0002: a frase da ponte é de al-Nahrawali
substituir(2, "explicacao", "Outra crônica do mesmo século fala em livros jogados no Eufrates",
    "Uma crônica do mesmo século, de Qutb al-Din al-Nahrawali, fala em livros jogados no Eufrates")
substituir_trecho(2, 1, "According to a 16th-century chronicle about the siege from Qu [...] ",
    "According to a 16th-century chronicle about the siege from Qu [...] al-Nahraw [...] ")

# 0003: Fatima é mencionada pela primeira vez séculos depois
substituir(3, "explicacao", "E a história de Fatima só aparece num cronista do século XIV, Ibn Abi Zar',",
    "E a história de Fatima aparece pela primeira vez séculos depois, num cronista do século XIV, Ibn Abi Zar',")

# 0006: ainda funcionava no século XV; a música foi introduzida pelo al-Mansuri
substituir(6, "explicacao", "O al-Mansuri funcionou até o século XV, e o prédio ainda existe no Cairo.",
    "O al-Mansuri ainda funcionava no século XV, e o prédio continua de pé no Cairo.")
substituir(6, "explicacao", "Como o hospital de Fustat antes dele, tratava doentes mentais e usava música como terapia.",
    "Assim como o hospital de Fustat antes dele, tratava doentes mentais, e introduziu a música como forma de terapia.")

# 0007: os 117 mil km incluem as viagens depois da volta, e vêm do próprio relato
substituir(7, "gancho", "Só voltou ao Marrocos 24 anos depois, após somar cerca de 117 mil km de viagens, bem mais que Marco Polo.",
    "Só voltou ao Marrocos 24 anos depois e, contando as viagens seguintes, teria somado uns 117 mil km, bem mais que Marco Polo.")
if len(CANDIDATOS[6]["gancho"]) > 220:
    substituir(7, "gancho", "para uma peregrinação a Meca", "rumo a Meca")

# 0009: sem as conversões erradas de Sparavigna; "sem medir distâncias entre cidades"
substituir(9, "explicacao",
    "Uma análise citada o converte em 3.928,77 milhas, 2% acima do raio médio real, mas tudo depende do tamanho do "
    "côvado, que não se sabe ao certo: com 18 polegadas seriam 3.600 milhas; com 22, 4.200.",
    "Quão perto ele chegou do valor moderno depende de quanto media o côvado que usou, e isso não se sabe ao certo: "
    "conforme a conversão escolhida, a estimativa fica mais ou menos próxima do raio real.")
substituir(9, "gancho", "calculou o raio da Terra sem viajar:", "calculou o raio da Terra sem medir distâncias entre cidades:")

# 0011: gancho centrado na circulação pulmonar e nos capilares
trocar(11,
    gancho="No século XIII, o médico Ibn al-Nafis descreveu o sangue indo do coração aos pulmões e de volta, e previu "
           "passagens minúsculas entre a artéria e a veia pulmonar, mais de 400 anos antes da descoberta dos capilares.",
    temas_secundarios=["historia_medicina", "anatomia", "revolucao_cientifica"])

# 0012: harmonizar a data de Hubble com galaxias-0001
substituir(12, "gancho", "mas só em 1925 Hubble mostrou que ela fica fora da Via Láctea",
    "mas só nos anos 1920 Hubble mostrou que ela fica fora da Via Láctea")
substituir(12, "explicacao", "A questão foi resolvida em 1925, quando Edwin Hubble encontrou",
    "A questão foi considerada resolvida em 1925, depois que Edwin Hubble encontrou")

# 0013: tipos de espanto e nota; gancho com "se diz"
trocar(13, tipos_espanto=["historia_humana", "contraintuitivo"], nota_surpresa=3)
substituir(13, "gancho", "que o metal teria se desvalorizado no Egito por anos",
    "que se diz ter desvalorizado o metal no Egito por anos")

# 0009: gancho cabendo em 220 caracteres
substituir(9, "gancho", "abaixo da linha horizontal.", "abaixo da horizontal.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(7, "gancho", "rumo a Meca que costumava levar dezesseis meses.", "rumo a Meca, viagem que costumava levar 16 meses.")
