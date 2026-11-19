"""Rodada 2 de Expressões e ditados: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-expressoes-01.py"))
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)

LOTE, AREA, TEMA = _base.LOTE, _base.AREA, _base.TEMA
wiki = _base.wiki
CANDIDATOS = _base.CANDIDATOS

UF_CROCODILO = "https://archive.news.ufl.edu/articles/2007/10/researchers-no-faking-it-crocodile-tears-are-real.html"


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


# 0001: estudo pequeno, sem crocodilos; confiança rebaixada; comunicado da Universidade da Flórida como 2ª fonte
trocar(1, confianca="consenso_parcial")
substituir(1, "explicacao",
    "A dupla usou jacarés, parentes próximos dos crocodilos, porque ali eles se alimentavam em terra firme. "
    "Cinco dos sete animais \"lacrimejaram\" enquanto comiam.",
    "Foram filmados quatro jacarés sul-americanos, os caimãs, e três aligátores, todos parentes próximos dos "
    "crocodilos, escolhidos porque ali eram treinados para comer em terra firme. Dos sete animais filmados, cinco "
    "\"lacrimejaram\" enquanto comiam, numa amostra pequena e sem nenhum crocodilo de fato.")
CANDIDATOS[0]["fontes"].append({
    "url": UF_CROCODILO,
    "titulo": "Researchers: No faking it, crocodile tears are real - University of Florida",
    "idioma": "en",
    "trecho": (
        "UF observed and videotaped four captive caimans and three alligators, both close relatives of the crocodile, "
        "while eating on a spit of dry land at Florida’s St. Augustine Alligator Farm Zoological Park. "
        "He found that five of the seven animals teared up as they tore into their food [...] "
        "He decided to observe alligators and caimans, rather than crocodiles, because they are trained at the farm to feed on dry land."),
})

# 0002: quem levava o bode ao deserto não era o sumo sacerdote; nota 3
# (o opcional do penhasco ficou de fora: o trecho não está na versão do artigo no cache)
trocar(2, nota_surpresa=3,
    gancho="O \"bode expiatório\" era um bode de verdade: num ritual do Templo de Jerusalém, o sumo sacerdote passava "
           "para ele os pecados do povo, e o animal era levado para o deserto.")
substituir(2, "explicacao", "que o animal levaria simbolicamente para o deserto.",
    "que o animal levaria simbolicamente para o deserto, conduzido em geral por um sacerdote escolhido para a tarefa.")
acrescentar_trecho(2, 0, "a priest was generally picked for the task.")

# 0003: gancho menos taxativo
trocar(3, gancho="\"Lua de mel\" talvez tenha nascido com um toque irônico: o amor dos recém-casados seria como a lua "
                 "cheia, que mal se completa e já começa a minguar. Um texto inglês de 1552 já falava desse amor que logo se acalma.")

# 0004: frases reescritas com palavras próprias
substituir(4, "explicacao", "serviam de esconderijo para ouro e pó de diamante, longe dos olhos do fisco,",
    "guardariam ouro e pó de diamante escondidos do fisco,")
substituir(4, "explicacao",
    "Só que essa versão é considerada lenda, com pouca comprovação de que as imagens tenham sido usadas desse jeito, "
    "como acontece com muitas histórias mineiras ligadas a esse tipo de peça.",
    "O problema é que quase não há prova documental desse uso, e a história costuma ser posta entre as lendas que "
    "cercam as imagens sacras mineiras.")
substituir(4, "explicacao",
    "As imagens provavelmente eram ocas pelos mesmos motivos que na Europa, onde, desde a Idade Média, as esculturas "
    "de madeira eram escavadas para rachar menos e ficar mais leves.",
    "O oco devia ter uma razão técnica, herdada da Europa: desde a Idade Média, os escultores retiravam o miolo das "
    "peças de madeira, o que as deixava mais leves e menos sujeitas a rachar.")

# 0008: sem afirmar mais que a fonte
substituir(8, "gancho", "mas nunca na mesma frase.", "mas a frase famosa não aparece.")
substituir(8, "explicacao", "e foi por essas adaptações que a frase pegou.",
    "e as adaptações ajudaram a popularizar a frase.")

# 0010: primeiro registro não é origem; autoria discutida; Caruso "sugere"
trocar(10, gancho="O registro mais antigo de \"abracadabra\" é uma receita médica: um livro de medicina romano, atribuído "
                  "ao século 2, mandava quem tinha malária usar um amuleto com a palavra escrita em triângulo.")
substituir(10, "explicacao",
    "O primeiro registro conhecido está no \"Liber Medicinalis\", de Sereno Samônico, médico do imperador romano "
    "Caracala. No capítulo 52, ele recomenda",
    "O primeiro registro conhecido está no \"Liber Medicinalis\", tradicionalmente atribuído a Sereno Samônico, "
    "erudito da corte do imperador romano Caracala (a autoria é discutida). Ali, o autor recomenda")
substituir(10, "explicacao",
    "O linguista Steve Caruso afirma que a origem aramaica, muito repetida, é um engano que se popularizou",
    "O linguista Steve Caruso diz que a palavra não pode ser aramaica e sugere que esse engano, muito repetido, se popularizou")

# 0012: Brunelleschi não era "jovem" na disputa; gancho mais preciso
substituir(12, "explicacao", "O jovem arquiteto tinha projetado uma cúpula enorme e pesada",
    "O arquiteto tinha projetado uma cúpula enorme e pesada")
trocar(12, gancho="O \"ovo de Colombo\" talvez nem seja de Colombo: a história saiu num livro de 1565, mas 15 anos antes "
                  "Vasari já contava que Brunelleschi pusera um ovo em pé para ganhar a obra da cúpula de Florença.")

# 0014: gancho com a reviravolta; última frase reescrita; Luiz Gama e as ações de liberdade
trocar(14, gancho="A \"lei para inglês ver\" de 1831 não impediu que mais de 700 mil africanos fossem trazidos "
                  "ilegalmente ao Brasil, mas, como os declarava livres, virou arma de escravizados e abolicionistas nos tribunais.")
substituir(14, "explicacao",
    "Historiadores mais recentes acrescentam uma reviravolta: mesmo desrespeitada, a lei criou uma contradição no "
    "sistema escravista, e Sidney Chalhoub mostra como ela deu a abolicionistas e escravizados uma ferramenta para "
    "lutar pela liberdade nos tribunais.",
    "Historiadores mais recentes veem uma reviravolta: como todo africano desembarcado depois de 1831 era legalmente "
    "livre, a lei ignorada deixou uma bomba-relógio no sistema escravista, e Sidney Chalhoub mostra como escravizados "
    "e abolicionistas passaram a usá-la nos processos. A partir dos anos 1850, e com mais força depois de 1871, "
    "advogados como Luiz Gama fizeram dela o principal argumento das \"ações de liberdade\": cabia ao senhor provar "
    "que a pessoa escravizada tinha chegado antes da proibição.")
acrescentar_trecho(14, 0,
    "A partir da década de 1850, e com mais intensidade após 1871, advogados e rábulas abolicionistas, como o célebre Luiz Gama, "
    "começaram a usar a Lei de 1831 como principal argumento nas \"ações de liberdade\". "
    "A tese era simples: cabia ao senhor provar que seu escravizado havia entrado no Brasil antes da proibição.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(14, "explicacao",
    "A partir dos anos 1850, e com mais força depois de 1871, advogados como Luiz Gama fizeram dela o principal argumento das \"ações de liberdade\": cabia ao senhor provar que a pessoa escravizada tinha chegado antes da proibição.",
    "Advogados como Luiz Gama fizeram dela a base das \"ações de liberdade\", sobretudo após 1871, invertendo o ônus: o senhor é que precisava provar que o escravizado chegara antes da lei.")
