"""Rodada 2 de Neurociência: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-25-neurociencia-01.py"))
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)

LOTE, AREA, TEMA = _base.LOTE, _base.AREA, _base.TEMA
wiki = _base.wiki
fonte = _base.fonte
CANDIDATOS = _base.CANDIDATOS


def trocar(n, **campos):
    CANDIDATOS[n - 1].update(campos)


def substituir(n, campo, velho, novo):
    texto = CANDIDATOS[n - 1][campo]
    assert velho in texto, (n, velho)
    CANDIDATOS[n - 1][campo] = texto.replace(velho, novo)


def substituir_trecho(n, i_fonte, velho, novo):
    f = CANDIDATOS[n - 1]["fontes"][i_fonte]
    assert velho in f["trecho"], (n, velho)
    f["trecho"] = f["trecho"].replace(velho, novo)


def acrescentar_trecho(n, i_fonte, extra):
    CANDIDATOS[n - 1]["fontes"][i_fonte]["trecho"] += " [...] " + extra


# notas conforme os vereditos
trocar(6, nota_surpresa=4)
trocar(7, nota_surpresa=3)

# 0002: Diamond "nos anos 1980"; limitação admitida por ela; "sugerem"; acervo de Harvey
substituir(2, "explicacao", "Em 1984, a equipe de Marian Diamond publicou", "Nos anos 1980, a equipe de Marian Diamond publicou")
substituir_trecho(2, 0,
    "In 1984, Marian Diamond and her associates were the first ever to publish research on the brain of Albert Einstein. ",
    "In the 1980s, University of California, Berkeley professor Marian Diamond received four sections of the cortical association regions [...] ")
substituir(2, "explicacao",
    "Os críticos apontaram problemas: um único Einstein, controles com idade média de 64 anos, contra 76 dele, e pesquisadores que sabiam qual cérebro era o famoso.",
    "A própria Diamond admitiu que tinha um só Einstein para comparar; críticos apontaram ainda controles com idade média de 64 anos, contra 76 dele, e pesquisadores que sabiam qual cérebro era o famoso.")
substituir(2, "explicacao", "pesquisas mais recentes indicam", "pesquisas mais recentes sugerem")
substituir(2, "explicacao", "entregaram o que restava a um museu", "entregaram o que restava em poder de Harvey a um museu")

# 0004: quem eram os pesquisadores
substituir(4, "explicacao",
    "Neurocirurgiões da Universidade da Califórnia em Los Angeles, entre eles Itzhak Fried e Rodrigo Quian Quiroga,",
    "Pesquisadores da Universidade da Califórnia em Los Angeles e do Caltech, entre eles o neurocirurgião Itzhak Fried e seu orientando Rodrigo Quian Quiroga,")

# 0005: sem a pegadinha da lula-gigante; alcance do modelo; Nobel com Eccles
trocar(5, gancho="O impulso nervoso foi decifrado num nervo de lula: sem a capa isolante dos nossos nervos, ela compensa com um axônio de até 1,5 mm, largo o bastante para receber eletrodos por dentro.")
substituir(5, "explicacao",
    " A espécie das experiências era a lula-de-nadadeira-longa do Atlântico, bem longe dos gigantes do fundo do mar.", "")
substituir(5, "explicacao",
    "O modelo virou base da neurociência e rendeu aos dois o Nobel de 1963.",
    "O modelo serviu de base à maioria dos modelos de neurônio nas quatro décadas seguintes e rendeu aos dois o Nobel de 1963, dividido com John Eccles.")
substituir_trecho(5, 0, ", using the longfin inshore squid as the model organism", "")
acrescentar_trecho(5, 1,
    "was an English physiologist and biophysicist who shared the 1963 Nobel Prize in Physiology or Medicine with Andrew Huxley and John Eccles.")

# 0009: James é uma das origens; palestras depois das experiências
substituir(9, "explicacao",
    "A origem provável está no psicólogo William James, de Harvard. A partir dos anos 1890, ele dizia em palestras que",
    "Uma das origens prováveis está no psicólogo William James, de Harvard. Depois de experiências feitas nos anos 1890, ele passou a dizer em palestras que")
substituir(9, "explicacao", "uma afirmação plausível.",
    "uma afirmação plausível. Há outras explicações, como leituras erradas de pesquisas neurológicas antigas.")
acrescentar_trecho(9, 0,
    "According to a related origin story, the ten-percent myth most likely arose from a misunderstanding (or misrepresentation) of neurological research in the late 19th century or early 20th century.")
trocar(9, nota_surpresa=3)

# 0010: a reorganização do mapa foi contestada em 2025
trocar(10,
    gancho="Muitos amputados sentem o membro perdido, e alguns sentem toques na mão fantasma quando alguém toca o rosto. Por décadas, isso foi explicado por um mapa cerebral que se reorganiza; em 2025, um estudo desafiou a ideia.",
    confianca="consenso_parcial",
    tipos_espanto=["contraintuitivo", "misterio_aberto", "engenhosidade"])
substituir(10, "explicacao", "exames do cérebro de amputados depois viram essa reorganização.",
    "exames do cérebro de amputados pareceram confirmar essa reorganização. Em 2025, porém, uma equipe liderada "
    "pela neurocientista Tamar Makin acompanhou com ressonância três pessoas antes e até cinco anos depois de "
    "amputarem uma das mãos e viu os mapas da mão e dos lábios praticamente inalterados; para os autores, a dor "
    "estaria mais ligada aos nervos cortados no coto, que mandam sinais \"ruidosos\" ao cérebro. A causa do "
    "fenômeno segue em debate.")
acrescentar_trecho(10, 0, "There is still no clear consensus as to its cause.")
CANDIDATOS[10 - 1]["fontes"].append(fonte(
    "https://www.cam.ac.uk/research/news/gone-but-not-forgotten-brains-map-of-the-body-remains-unchanged-after-amputation",
    "Gone but not forgotten: brain's map of the body remains unchanged after amputation (University of Cambridge)",
    "The brain holds a ‘map’ of the body that remains unchanged even after a limb has been amputated, contrary to the prevailing view that it rearranges itself to compensate for the loss [...] "
    "For decades now, the commonly-accepted view among neuroscientists has been that following amputation of a limb, neighbouring regions rearrange and essentially take over the area previously assigned to the now missing limb. [...] "
    "a team led by Professor Tamar Makin from the University of Cambridge and Dr Hunter Schone from the University of Pittsburgh followed three individuals due to undergo amputation of one of their hands. [...] "
    "The researchers used the brain scans to construct maps of the hand and lips for each individual. [...] "
    "One participant was scanned again 18 months after amputation and a second participant five years after amputation. [...] "
    "even with their hand now missing, the corresponding brain region activated in an almost identical manner. [...] "
    "They found that it remained unchanged and had not taken over the region representing the missing hand. [...] "
    "Without an end-target, the nerves can continue to grow to form a thickening of the nerve tissue and send noisy signals back to the brain. [...] "
    "Nature Neuroscience; 21 Aug 2025"))

# 0012: crianças; "a maioria"; casos de bom resultado
trocar(12, gancho="Em epilepsias graves que não cedem a remédios, cirurgiões chegam a remover ou desligar metade do cérebro. Muitos pacientes ficam livres das crises e, mesmo assim, falam, leem e andam.")
substituir(12, "explicacao", "quase todos perdem a metade do campo visual", "a maioria perde a metade do campo visual")
substituir(12, "explicacao", "todos com capacidade cognitiva relativamente normal",
    "todos com capacidade cognitiva relativamente normal, escolhidos entre os casos de bom resultado")
acrescentar_trecho(12, 1,
    "\"We hope that a better understanding of how the brain is compensating in people who have optimal outcomes will eventually inform targeted intervention strategies for future hemispherectomy patients,\" says Paul.")

# 0013: sem os 50 bilhões; a proporção como média entre mamíferos
substituir(13, "explicacao",
    "e são os mais numerosos: as estimativas giram em torno de 50 bilhões, cerca de três quartos de todos os neurônios do cérebro.",
    "e são os mais numerosos de todo o cérebro.")
substituir(13, "explicacao",
    "A proporção, de cerca de 3,6 neurônios no cerebelo para cada um no neocórtex, se repete em muitas espécies de mamíferos.",
    "Em muitas espécies de mamíferos, o cerebelo tem cerca de 3,6 neurônios para cada um do neocórtex, uma proporção que se mantém de espécie para espécie.")
substituir_trecho(13, 0,
    "They are also the most numerous neurons in the brain: In humans, estimates of their total number average around 50 billion, which means that about 3/4 of the brain's neurons are cerebellar granule cells.",
    "They are also the most numerous neurons in the brain")

# 0010: explicação reescrita para caber em 250 palavras, com as mesmas correções
trocar(10, explicacao=(
    "Entre 50% e 80% dos amputados sentem um membro fantasma: coceiras, gestos e até dor num braço ou numa perna "
    "que já não existe. O nome foi criado em 1872 pelo médico Silas Weir Mitchell, mas o cirurgião militar francês "
    "Ambroise Paré já descrevia o fenômeno no século XVI. No fim dos anos 1980, Ronald Melzack notou que a velha "
    "explicação, a irritação dos nervos no coto, não podia estar certa: muitas pessoas que nasceram sem um membro "
    "também sentem um fantasma. Em 1991, uma equipe dos Institutos Nacionais de Saúde dos EUA mostrou que o córtex "
    "somatossensorial de macacos se reorganiza depois de perder a entrada de sinais. V. S. Ramachandran propôs que "
    "o mesmo valia para humanos, mostrou que tocar partes do rosto fazia pacientes sentirem toques no membro "
    "ausente, e exames de amputados pareceram confirmar a reorganização. Dele veio também a caixa de espelhos: o "
    "paciente vê o reflexo do membro saudável no lugar do ausente e, com movimentos simétricos, tem a ilusão de "
    "mexer o fantasma, o que pode ajudar a soltá-lo de posições dolorosas; a eficácia ainda é debatida. Em 2025, "
    "porém, uma equipe liderada pela neurocientista Tamar Makin acompanhou com ressonância três pessoas antes e até "
    "cinco anos depois de amputarem uma das mãos e viu os mapas da mão e dos lábios praticamente inalterados. Para "
    "os autores, a dor estaria mais ligada aos nervos cortados no coto, que mandam sinais \"ruidosos\" ao cérebro. "
    "A causa do fenômeno segue em debate."
))

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
# 0010: a falta de consenso da fonte é sobre a dor fantasma
substituir(10, "explicacao",
    "A causa do fenômeno segue em debate.",
    "A causa da dor fantasma segue em debate.")
