"""Rodada 2 de Gramáticas surpreendentes: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-estruturas_linguisticas-01.py"))
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


# 0001: gancho menos absoluto (a "pureza" do sistema é discutida)
substituir(1, "gancho",
    "nada fica \"à esquerda\" ou \"na frente\" de nada: tudo é situado por norte, sul, leste e oeste.",
    "as posições são dadas por norte, sul, leste e oeste, e não por \"esquerda\" ou \"na frente\".")

# 0004: quíchua e aimará marcam a fonte, sem afirmar que "exigem"
substituir(4, "explicacao",
    "O quíchua e o aimará, nos Andes, também exigem a marca.",
    "O quíchua e o aimará, nos Andes, também marcam na gramática a fonte da informação.")

# 0007: autores de 2020 vêm de três instituições
substituir(7, "explicacao",
    "Em 2020, porém, pesquisadores da Universidade de Aberdeen refizeram as mesmas tarefas",
    "Em 2020, porém, pesquisadores de universidades do Reino Unido e da Rússia, liderados por uma equipe da "
    "Universidade de Aberdeen, refizeram as mesmas tarefas")
acrescentar_trecho(7, 1,
    "Department of Psychology, Liverpool Hope University [...] "
    "National Research University: Higher School of Economics [...] Moscow, Russia")

# 0008: o exemplo da ponte é o próprio estudo de Boroditsky e colegas (2003), que não se repetiu
trocar(8, tipos_espanto=["contraintuitivo", "mito_desmentido"],
    gancho="\"Ponte\" é feminino em alemão e masculino em espanhol. Um estudo famoso de 2003 relatou que alemães a "
           "descreviam como bela e elegante, e espanhóis, como forte e robusta. Testes independentes não repetiram o resultado.")
substituir(8, "explicacao", "Num estudo, falantes de alemão",
    "No estudo mais citado dessa linha, de Lera Boroditsky e colegas, em 2003, falantes de alemão")
substituir(8, "explicacao",
    " Em 2003, Boroditsky e colegas relataram um resultado parecido, com falantes de alemão e espanhol descrevendo "
    "objetos de acordo com o gênero da palavra na própria língua.", "")
substituir(8, "explicacao", "O trabalho foi citado inúmeras vezes",
    "O trabalho, nunca publicado na íntegra, foi citado inúmeras vezes")
CANDIDATOS[7]["fontes"].append({
    "url": "https://arxiv.org/pdf/2005.01204",
    "titulo": "On the Relationships Between the Grammatical Genders of Inanimate Nouns and Their Co-Occurring Adjectives and Verbs (Williams et al., 2020)",
    "idioma": "en",
    "trecho": (
        "Most famously, Boroditsky et al. (2003) claim to have conducted a laboratory experiment showing that speakers of "
        "German choose stereotypically feminine adjectives to describe, for example, bridges, while speakers of Spanish "
        "choose stereotypically masculine adjectives [...] "
        "while in Spanish, the word for a bridge, puente, is grammatically masculine. [...] "
        "That said, the experiment has not gone unchallenged. "
        "Indeed, Mickan et al. (2014) reported two unsuccessful replication attempts. [...] "
        "Lera Boroditsky, Lauren A. Schmidt, and Webb Phillips. 2003. Sex, Syntax, and Semantics."),
})

# 0009: as ideias ganharam mais alcance depois da morte; "insight" = discernimento
substituir(9, "explicacao",
    "e suas ideias só ganharam fama depois, quando colegas reuniram e divulgaram os seus manuscritos",
    "e suas ideias ganharam muito mais alcance depois, quando colegas reuniram e divulgaram os seus manuscritos")
substituir(9, "explicacao", "como uma falha de percepção humana, não de linguagem",
    "como uma falha de discernimento humano, não de linguagem")

# 0010: a frase de Whorf é de um texto de 1936, publicado postumamente; futuro/não futuro é discutível
substituir(10, "explicacao", "Nos anos 1940, Benjamin Whorf escreveu que",
    "Num texto de 1936, publicado só depois da sua morte, Benjamin Whorf escreveu que")
substituir(10, "explicacao", "Ele também mostrou que o verbo hopi distingue futuro de não futuro.",
    "Ele também defendeu que o verbo hopi distingue futuro de não futuro, ponto que outros linguistas, inclusive "
    "Comrie, acharam discutível.")
acrescentar_trecho(10, 0,
    "Whorf's most frequently cited statement regarding Hopi time is the strongly worded introduction of his 1936 paper "
    "\"An American Indian model of the Universe,\" which was first published posthumously in Carroll's edited volume. [...] "
    "But Comrie also notes that Malotki's \"claim that Hopi has a tense system based on the opposition of future and "
    "non-future ... strikes me as questionable")

# 0011: "ao" é palavra japonesa; só o caractere é o do chinês qīng
substituir(11, "explicacao",
    "É a mesma palavra, escrita com o mesmo caractere, que o chinês \"qīng\", capaz de designar tanto o azul quanto a "
    "maior parte dos verdes.",
    "Escreve-se com o mesmo caractere do chinês \"qīng\" e pode designar tanto o azul quanto a maior parte dos verdes.")

# 0012: gancho centrado em Geiger; sem moldura de mito desmentido
trocar(12, tipos_espanto=["conexao_inesperada", "historia_humana"],
    gancho="Homero chama o mar de \"cor de vinho\" e não tem palavra clara para azul. Nos anos 1860, um filólogo viu o "
           "mesmo na Bíblia, nos Vedas e no Alcorão e propôs que o azul é sempre a última cor a ganhar nome.")
substituir(12, "explicacao",
    "ideia que antecipou o famoso estudo de Berlin e Kay de 1969 sobre os termos básicos de cor.",
    "ideia que antecipou o famoso estudo de Berlin e Kay de 1969 sobre os termos básicos de cor, até hoje debatido.")
acrescentar_trecho(12, 0,
    "though even the basic framework is sometimes subject to significant controversy")

# 0013: em finlandês falado, "joo" é um pouco mais comum que a resposta-eco
substituir(13, "explicacao", "a resposta normal é \"Tulemme\", \"Estamos vindo\".",
    "a resposta pode ser simplesmente \"Tulemme\", \"Estamos vindo\", embora na fala um \"joo\" (sim) seja hoje um "
    "pouco mais comum.")
acrescentar_trecho(13, 0, "However, in spoken Finnish, a simple \"Yes\" answer is somewhat more common, Joo.")

# 0014: o hindi padrão não tem a distinção
substituir(14, "explicacao", "aparece em várias línguas da Índia, inclusive no hindi,",
    "aparece em várias línguas da Índia, como o marati e o guzerate,")
substituir_trecho(14, 1, "as well as in several Indo-European languages of India such as [...] Hindustani (Hindi-Urdu) [...] ",
    "as well as in several Indo-European languages of India such as Odia, Marathi, Rajasthani, Haryanvi, Punjabi, "
    "Saraiki, Hindustani (Hindi-Urdu), Sindhi and Gujarati [...] ")

# 0015: o gancho não esconde que, nos testes mais rigorosos, a correlação não foi significativa
substituir(15, "gancho", "a correlação enfraqueceu, mas não sumiu.",
    "a correlação enfraqueceu e, nos testes mais rigorosos, deixou de ser significativa.")
# o gancho com a troca pedida passou de 220 caracteres: mesma correção, frase mais curta
trocar(15, gancho="Um economista ligou línguas sem futuro obrigatório, como o finlandês e o mandarim, a poupar mais. "
                  "Testada depois por ele e dois céticos, a correlação enfraqueceu e, nos testes mais rigorosos, deixou "
                  "de ser significativa.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(10, "explicacao", "Ele também defendeu que o verbo hopi distingue futuro de não futuro, ponto que outros linguistas, inclusive Comrie, acharam discutível. Para o linguista Bernard Comrie, a argumentação de Malotki foi \"devastadora\".", "Ele também defendeu que o verbo hopi distingue futuro de não futuro. Para o linguista Bernard Comrie, a argumentação de Malotki foi \"devastadora\" para as teses fortes de Whorf, embora esse ponto do futuro lhe parecesse discutível.")
