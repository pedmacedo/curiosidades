"""Rodada 2 de Ásia antiga e medieval: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-asia_antiga-01.py"))
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


# 0001: o fósforo como explicação mais aceita, atribuída a Balasubramaniam (sem título brasileiro do livro: não há trecho)
substituir(1, "gancho", "há uns 1.600 anos. O segredo é o fósforo do ferro antigo, que forma uma película protetora.",
    "há uns 1.600 anos, graças, ao que tudo indica, ao fósforo do ferro antigo.")
substituir(1, "explicacao", "A diferença está na química.",
    "Segundo a explicação mais aceita, do metalurgista R. Balasubramaniam, a diferença está na química.")
trocar(1, confianca="consenso_parcial")
acrescentar_trecho(1, 0, "In a report published in the journal Current Science, R. Balasubramaniam of IIT Kanpur explains how the pillar's resistance to corrosion is due to a passive protective film at the iron-rust interface.")

# 0002: fim de Prinsep com trecho literal (sem idade calculada); tipos e nota
substituir(2, "explicacao", "Prinsep morreu em 1840, poucos anos depois; segundo sua biografia, literalmente se matou de trabalhar.",
    "Prinsep, nascido em 1799, começou a sofrer de dores de cabeça e mal-estar em 1838, voltou doente para a "
    "Inglaterra e morreu em 1840; diz-se que literalmente se matou de trabalhar.")
trocar(2, tipos_espanto=["historia_humana", "contraintuitivo"], nota_surpresa=3)
acrescentar_trecho(2, 1, "From 1838 he began to suffer from recurrent headaches and sickness. [...] "
    "He arrived in England in poor condition and did not recover.")

# 0003: "em parte"; consenso_parcial; ressalva do apadrinhamento
substituir(3, "gancho", "Os concursos do serviço público britânico se inspiraram nos exames da China imperial.",
    "Os concursos públicos britânicos se inspiraram em parte nos exames da China imperial.")
substituir(3, "explicacao", "ainda havia quem os atacasse como \"cultura chinesa adotada\".",
    "ainda havia quem os atacasse como \"cultura chinesa adotada\". Quanto a China de fato pesou na reforma "
    "ainda é discutido: ela também respondia à antiga distribuição de cargos por apadrinhamento.")
trocar(3, confianca="consenso_parcial")

# 0004: satélite e outras técnicas; irrigação provável e o debate sobre os reservatórios
substituir(4, "gancho", "e só imagens de satélite revelaram uma cidade de pelo menos 1.000 km².",
    "e foram precisas imagens de satélite para revelar uma cidade de pelo menos 1.000 km².")
substituir(4, "explicacao", "servia para irrigar os campos diante das monções imprevisíveis.",
    "provavelmente servia para irrigar os campos diante das monções imprevisíveis, embora alguns estudiosos "
    "vejam nos grandes reservatórios também um símbolo religioso.")
acrescentar_trecho(4, 0, "The significance of such reservoirs has been debated by modern scholars, some believing the use was the irrigation of rice fields,  "
    "others have regarded them as religiously charged symbols of the great mythological oceans surrounding Mount Meru, the abode of the gods.")

# 0006: restos de sangue; mais de 130 sementes; data aproximada
substituir(6, "gancho", "e sangue nas veias. Tinha 130 sementes de melão no estômago.",
    "e restos de sangue nas veias. Tinha mais de 130 sementes de melão no aparelho digestivo.")
substituir(6, "explicacao", "em 169 ou 168 a.C.", "por volta de 168 a.C.")
substituir(6, "explicacao", "As sementes de melão no estômago", "As mais de 130 sementes de melão no estômago")

# 0008: sem motivo atribuído; murais nas cavernas 1, 2, 16 e 17; nota 3
substituir(8, "gancho", "Para marcar o feito, riscou o nome sobre a figura de um bodisatva.",
    "Lá dentro, riscou de propósito o próprio nome sobre a figura de um bodisatva.")
substituir(8, "explicacao", "guardam o maior conjunto de pinturas murais da Índia antiga que chegou até nós.",
    "incluem, nas cavernas 1, 2, 16 e 17, o maior conjunto de pinturas murais da Índia antiga que chegou até nós.")
trocar(8, nota_surpresa=3)

# 0009: sem represar o rio; degradação no século XVII
substituir(9, "gancho", "controla as cheias do rio Min sem barragem:", "controla as cheias do rio Min sem represá-lo:")
substituir(9, "explicacao", "Danificado em guerras e destruído por um terremoto em 1933",
    "Degradado nas convulsões do século XVII e destruído por um terremoto em 1933")
acrescentar_trecho(9, 0, "Turmoil surrounding the conquering of Chengdu by peasant rebel leader Zhang Xianzhong in 1644, and the Ming-Qing transition more generally, "
    "led to depopulation and the deterioration of the Dujiangyan irrigation system to the point where rice cultivation was set back for decades.")

# 0010: cerca de 160 mil kofun; atribuições do século XIX em geral
substituir(10, "explicacao", "Entre o fim do século III e o século VI, o Japão ergueu mais de 20 mil kofun",
    "Entre meados do século III e o início do século VIII, o Japão ergueu cerca de 160 mil kofun")
substituir(10, "explicacao", "A ligação com Nintoku vem do século XIX.", "Boa parte dessas atribuições é do século XIX.")
acrescentar_trecho(10, 1, "It is estimated that some 160,000 burial mounds (kofun in Japanese, meaning ‘old mound’) were constructed between the middle of the 3rd century AD and the early 8th century.")

# 0013: gancho com "teriam"; descrição dos Niō com palavras próprias
trocar(13, gancho="Os guardiões musculosos e furiosos nos portões de templos budistas do Japão teriam um ancestral grego: "
    "Héracles. Na arte greco-budista, o herói virou o protetor do Buda, e essa imagem viajou pelo Leste Asiático.")
substituir(13, "explicacao", "guardiões irados e musculosos do Buda postos na entrada de muitos templos budistas",
    "a dupla de guardiões de expressão feroz e músculos saltados que flanqueia a entrada de muitos templos budistas")

# ganchos encurtados para caber em 220 caracteres
trocar(4, gancho="Em Angkor, capital khmer, só os deuses moravam em pedra: até a residência do rei era de madeira. Por isso "
    "sobraram os templos, e foram precisas imagens de satélite para revelar uma cidade de pelo menos 1.000 km².")
trocar(6, gancho="Uma nobre chinesa morta há mais de dois mil anos foi achada com pele macia, juntas que dobravam, restos "
    "de sangue nas veias e mais de 130 sementes de melão no aparelho digestivo. Não se sabe bem como se conservou.")
trocar(8, gancho="Em 1819, um oficial britânico que caçava tigres na Índia foi levado por um pastorzinho às cavernas budistas de "
    "Ajanta, cheias de pinturas antigas. Lá dentro, riscou de propósito o nome sobre a figura de um bodisatva.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(10, "explicacao", "Boa parte dessas atribuições é do século XIX.", "Boa parte das atribuições de túmulos a imperadores vem do século XIX.")
substituir(10, "explicacao", "Apesar de declarações oficiais recentes sugerindo mudança, o acesso continua em grande parte negado a quem está fora da agência.",
    "Mesmo com sinais oficiais recentes de abertura, quase ninguém de fora da agência consegue entrar.")
substituir(13, "explicacao", "a dupla de guardiões de expressão feroz e músculos saltados que flanqueia a entrada de muitos templos budistas",
    "os guardiões de expressão feroz e músculos saltados que ficam na entrada de muitos templos budistas")
substituir(1, "gancho", "Um pilar de ferro de mais de seis toneladas resiste à ferrugem em Délhi há uns 1.600 anos",
    "Um pilar de ferro de mais de seis toneladas, hoje em Délhi, resiste à ferrugem há uns 1.600 anos")
substituir(1, "explicacao", "No seu primeiro livro, de 1969, Erich von Däniken", "No seu primeiro livro, Erich von Däniken")
