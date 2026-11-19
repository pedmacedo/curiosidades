"""Rodada 2 de Invenções: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-invencoes-01.py"))
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


# 0003: sem as "oito semanas"; o processo de 1855 foi de um concorrente
substituir(3, "gancho", "patenteou o processo oito semanas antes dele e ganhou na Justiça.", "patenteou o processo pouco antes dele e a manteve na Justiça.")
substituir(3, "explicacao", "registrou em novembro de 1843 uma patente para vulcanizar borracha com enxofre, oito semanas antes de Goodyear nos Estados Unidos",
    "registrou em 21 de novembro de 1843 uma patente para vulcanizar borracha com enxofre, antes de Goodyear nos Estados Unidos")
substituir(3, "explicacao", "Na disputa judicial, químicos testemunharam",
    "Num processo de 1855, movido por um concorrente britânico que acusava Hancock de ter copiado Goodyear, químicos testemunharam")
substituir(3, "explicacao", "dois filhos dele morreram ainda bebês", "dois filhos dele morreram ainda pequenos")

# 0004: o Bureau de Química; "o começo da queda"
substituir(4, "explicacao", "Harvey Wiley, chefe da divisão de química da FDA, a agência americana de alimentos,",
    "Harvey Wiley, chefe do Bureau de Química do governo americano, o órgão que daria origem à FDA,")
substituir(4, "explicacao", "O episódio acabou com a carreira de Wiley.", "O episódio é apontado como o começo da queda de Wiley.")

# 0007: a patente original é de 1947; sem "o primeiro"
substituir(7, "explicacao", "Os cianoacrilatos surgiram em 1942, numa busca por materiais para fins militares durante a guerra.",
    "Em 1942, numa busca por materiais para fins militares durante a guerra, a equipe de Coover topou com uma fórmula de cianoacrilato.")
substituir(7, "explicacao", "Coover também foi o primeiro a reconhecer e patentear o uso como adesivo de tecidos do corpo, depois que",
    "Coover também patenteou o uso como adesivo de tecidos do corpo, depois que")

# 0008: sem a W. R. Grace (anacronismo); motivos como relato
trocar(8, confianca="consenso_parcial")
substituir(8, "gancho", "Antes, tinha deixado de patentear sua máquina de costura por medo de tirar o emprego das costureiras.",
    "Antes, segundo se conta, deixou de patentear sua máquina de costura por medo de tirar o emprego das costureiras.")
substituir(8, "explicacao", "Vendeu a patente à W. R. Grace and Company por 400 dólares, pagou a dívida e ficou com 385. A empresa lucrou milhões com o produto.",
    "Vendeu a patente por 400 dólares, pagou a dívida e ficou com 385. Quem comprou lucrou milhões com o produto.")
substituir(8, "explicacao", "segundo sua biografia, o credor era", "segundo outra versão, o credor era")
substituir(8, "explicacao", "Não a patenteou porque temia desempregar", "Segundo os relatos, não a patenteou porque temia desempregar")

# 0012: Kearns não foi "o inventor" do limpador intermitente
trocar(12, gancho="O limpador de para-brisa intermitente que virou padrão nos carros foi modelado no piscar do olho. Seu criador, "
    "Robert Kearns, processou a Ford e a Chrysler, foi muitas vezes o próprio advogado e venceu as duas.")

# 0013: "um dos primeiros" corretivos
trocar(13, gancho="Um dos primeiros corretivos líquidos foi criado por uma secretária que pintava vitrines e cobriu erros de "
    "datilografia com tinta. Ela foi demitida depois de assinar uma carta com o nome da própria empresa de corretivo.")

# 0015: a primeira corrida do aço de Brearley
substituir(15, "explicacao", "Segundo relatos, o primeiro aço inox de verdade saiu de um forno elétrico em agosto de 1913.",
    "Segundo relatos, a primeira corrida do aço inox de Brearley saiu de um forno elétrico em agosto de 1913.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(8, "explicacao", "Ele o fez para quitar 15 dólares que devia;", "Ele o fez para quitar 15 dólares que devia a um amigo;")
trocar(7, nota_surpresa=3)
trocar(8, nota_surpresa=3)
