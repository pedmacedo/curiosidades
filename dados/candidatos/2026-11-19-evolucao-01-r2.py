"""Rodada 2 de Evolução: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-evolucao-01.py"))
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


# 0003: a seca foi em 2003 e 2004; o gancho fala de uma espécie, não de todos os tentilhões
substituir(3, "gancho", "os tentilhões da ilha passaram a ter bicos maiores", "uma espécie de tentilhão passou a ter bicos maiores")
substituir(3, "explicacao", "Quando veio uma seca tão forte quanto a de 1977, em 2003,",
    "Quando veio uma seca tão forte quanto a de 1977, em 2003 e 2004,")
acrescentar_trecho(3, 1, "During a drought in 2004, overlap in the diets of the medium ground finch population and a recently settled population of large ground finches")

# 0004: parte das mudanças parece ser plasticidade (Sabolić et al., Molecular Ecology)
trocar(4, confianca="consenso_parcial", tipos_espanto=["contraintuitivo", "misterio_aberto"])
substituir(4, "explicacao",
    " A nova população cresceu por décadas sem interferência humana e chegou a superar outra espécie de lagartixa, hoje extinta no local.", "")
substituir(4, "explicacao",
    " O DNA mitocondrial confirmou que os animais de Pod Mrčaru continuam geneticamente muito parecidos com os da ilha de onde vieram.",
    " Ainda se discute quanto disso é mudança genética. Um estudo genômico mais recente achou sinais de adaptação "
    "no DNA, mas concluiu que, nesse estágio inicial, as principais causas das diferenças são a plasticidade, a "
    "resposta do corpo à dieta e ao ambiente, e a interação entre genes e ambiente: as diferenças de cabeça e "
    "mordida não se mantiveram quando os animais cresceram em condições iguais.")
CANDIDATOS[3]["fontes"].append({
    "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:38133599%20AND%20SRC:MED&resultType=core&format=json",
    "titulo": "Plastic and genomic change of a newly established lizard population following a founder event (Sabolić et al., Molecular Ecology, resumo via Europe PMC)",
    "idioma": "en",
    "trecho": (
        "Adaptive processes following the founder event are indicated by highly differentiated genomic loci associating with ecologically relevant phenotypic traits [...] "
        "Diverged traits related to head size and shape or bite force showed moderate heritability in a crossing experiment, but between-population differences in these traits did not persist in a common garden environment. "
        "Our results confirm the existence of sufficient additive genetic variance for traits to evolve under selection while also demonstrating that phenotypic plasticity and/or genotype by environment interactions are the main drivers of population differentiation at this early evolutionary stage."),
})

# 0006: reação "morna", não "ninguém notou"; a frase a Lyell (o "he" é Wallace)
trocar(6, gancho="Em 1858, Wallace enviou a Darwin um ensaio com a ideia que Darwin elaborava havia 20 anos sem publicar. "
    "Lidos juntos em Londres, os textos tiveram reação tão morna que o ano foi tido como sem grandes descobertas.")
substituir(6, "explicacao",
    "Darwin o recebeu em 18 de junho de 1858 e escreveu a Lyell que nem ele faria um resumo melhor.",
    "Darwin o recebeu em 18 de junho de 1858 e escreveu a Lyell que o texto parecia um resumo perfeito da sua "
    "própria teoria: até os termos de Wallace coincidiam com os títulos dos seus capítulos.")
substituir_trecho(6, 0, "he could not have made a better short abstract! [...] ",
    "he could not have made a better short abstract! Even his terms now stand as heads of my chapters [...] ")

# 0009: o que foi apoiado a partir de 1994 é a inversão do eixo dorso-ventral
substituir(9, "explicacao", "Georges Cuvier rejeitou a tese, mas em 1994 Geoffroy se mostrou correto.",
    "Georges Cuvier rejeitou a tese, mas, a partir de 1994, estudos de genes do desenvolvimento deram apoio à "
    "ideia de que o eixo barriga–costas está invertido entre artrópodes e vertebrados.")

# 0011: a Ormia é larvípara
substituir(11, "explicacao", "Achado o macho, ela põe ovos sobre ele e ao redor; as larvas entram no grilo",
    "Achado o macho, ela deposita larvas já eclodidas sobre ele e ao redor; as larvas entram no grilo")

# 0012: forma simples, sem o frameshift de Ohno; "inéditas" só na época
trocar(12, gancho="O náilon foi inventado em 1935. Em 1975, em lagoas com resíduos de uma fábrica de náilon, cientistas "
    "japoneses acharam uma bactéria que digere subprodutos dele, sem existência conhecida antes do material.")
substituir(12, "explicacao", "eram muito diferentes das de outras bactérias", "pareciam, na época, muito diferentes das de outras bactérias")
substituir(12, "explicacao", "a cópia antiga é cerca de cem vezes menos eficiente",
    "a outra cópia, chamada EII', é cerca de cem vezes menos eficiente")
substituir(12, "explicacao",
    "Para outra, o geneticista Susumu Ohno propôs que nasceu de uma mutação que desloca a leitura do gene, embaralhando "
    "a proteína, e mesmo assim deu origem a uma enzima com atividade fraca. A estrutura dessa enzima, resolvida em "
    "2018, indicou que ela não é tão inédita: pertence a uma família conhecida de enzimas.",
    "A terceira, EIII, chegou a ser tida como totalmente inédita, mas sua estrutura, resolvida em 2018, mostrou que "
    "ela pertence a uma família conhecida de enzimas.")
substituir_trecho(12, 0,
    "Susumu Ohno proposed that it had come about from the combination of a gene-duplication event with a frameshift mutation. [...] "
    "one of the enzymes involved was produced by a frame-shift mutation that completely scrambled transcribed amino acids. "
    "Despite this, the new gene still had a novel, albeit weak, catalytic capacity. "
    "This is seen as a good example of how mutations easily can provide the raw material for evolution by natural selection. ",
    "[...] ")

# 0014: Draper era da Universidade de Nova York; situar Huxley no gancho
trocar(14, gancho="No debate de 1860 sobre Darwin, em Oxford, o bispo Wilberforce teria perguntado ao darwinista Huxley se "
    "ele descendia de macaco pelo lado do avô ou da avó. Não há registro literal, e cada lado achou que venceu.")
substituir(14, "explicacao", "uma palestra do americano John William Draper,",
    "uma palestra de John William Draper, da Universidade de Nova York,")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(12, "gancho", "que digere subprodutos dele, sem existência conhecida antes do material.", "que digere subprodutos dele, substâncias sem existência conhecida antes de 1935.")
