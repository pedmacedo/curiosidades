"""Rodada 2 de Herança africana: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-heranca_africana-01.py"))
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


# 0002: texto próprio, sem frases quase copiadas da fonte
substituir(2, "explicacao", "\"Pretos novos\" era o nome dado aos africanos que acabavam de chegar ao Rio pelo Cais do Valongo e eram postos à venda no mercado de escravizados.",
    "Chamavam-se \"pretos novos\" os africanos recém-desembarcados no Cais do Valongo, levados em seguida ao mercado para serem vendidos.")
substituir(2, "explicacao", "Quase todos desembarcavam muito debilitados, e uma parte significativa não resistia às condições da travessia do Atlântico ou do próprio mercado.",
    "A travessia do Atlântico e o confinamento no mercado deixavam quase todos muito fracos, e muitos morriam ali mesmo.")
substituir(2, "explicacao", "Na prática, a atividade só mudou de endereço.", "O comércio, porém, apenas se mudou para outro lugar.")
substituir(2, "explicacao", "encontraram fragmentos de ossos humanos misturados a cerâmica, vidro e ferro",
    "deram com pedaços de ossos humanos em meio a cacos de cerâmica, vidro e objetos de ferro")

# 0003: decréscimo natural, não só mortalidade
substituir(3, "gancho", "A diferença estava em quanto se morria aqui.", "Aqui, morriam mais cativos do que nasciam.")

# 0004: os mais velhos; texto próprio; casa colonial, não sobrados
trocar(4, gancho="No Benim, descendentes de africanos libertos que voltaram do Brasil festejam o Senhor do Bonfim, e os mais velhos "
    "se cumprimentam com \"Bom dia, como passou?\". Em Gana, viraram os \"tabom\", de \"tá bom\".")
substituir(4, "explicacao", "Têm sobrenomes como Souza, Silva e Almeida, dançam a burrinha, uma forma arcaica do bumba-meu-boi, fazem desfiles de Carnaval e se reúnem em torno de uma feijoada.",
    "Carregam sobrenomes portugueses, como Souza, Silva e Almeida, saem em cortejos de Carnaval, comem feijoada quando se reúnem e mantêm viva a burrinha, uma versão antiga do bumba-meu-boi.")
substituir(4, "explicacao", "Na Ilha de Lagos, o estilo dos sobrados coloniais brasileiros trazido pelos retornados dominava a arquitetura no fim do século XIX.",
    "Na Ilha de Lagos, o estilo arquitetônico trazido pelos retornados, inspirado na casa colonial brasileira, tornou-se dominante no fim do século XIX.")

# 0007: a mais antiga petição conhecida de uma pessoa escravizada; "escravizada"
substituir(7, "explicacao", "A carta foi redescoberta em 1979 e é considerada a primeira petição escrita por uma mulher na história do Brasil, além de um marco das origens da literatura afro-brasileira.",
    "A carta foi redescoberta em 1979 e é tida como a mais antiga petição conhecida escrita por uma pessoa escravizada no Brasil, além de um marco das origens da literatura afro-brasileira.")
substituir(7, "explicacao", "foi levada como escrava para a casa do capitão", "foi levada, escravizada, para a casa do capitão")
CANDIDATOS[6]["fontes"][1]["trecho"] = "is considered to have written the first earliest known slave petition in Brazil [...] " + CANDIDATOS[6]["fontes"][1]["trecho"]

# 0008: "em parte como reação"; sem "esporte nacional oficial" em 1937
substituir(8, "explicacao", "Em reação, Mestre Bimba (1899-1974) criou", "Em parte como reação, Mestre Bimba (1899-1974) criou")
substituir(8, "explicacao", "a partir de 1937, a capoeira foi legalizada e promovida pelo Estado e virou esporte nacional oficial.",
    "a partir de 1937, a capoeira foi legalizada e passou a ser promovida pelo Estado como parte da cultura nacional.")

# 0010: o que diz o trecho da letra; tipo
substituir(10, "explicacao", "A letra também tem história: segundo Donga, o trecho sobre o chefe da polícia era uma paródia criada por jornalistas do jornal A Noite.",
    "A letra também tem história: segundo Donga, o trecho em que o chefe da polícia avisa, pelo telefone, que há uma roleta na Carioca era uma paródia criada por jornalistas do jornal A Noite.")

# 0011: divergência acadêmica, não mistério; dado de 1978 no passado
trocar(11, tipos_espanto=["conexao_inesperada", "contraintuitivo"])
substituir(11, "explicacao", "A comunidade de falantes é minúscula: em 1978, eram 40 pessoas, que vivem numa área rural a 150 km da cidade de São Paulo.",
    "A comunidade de falantes era minúscula: em 1978, eram 40 pessoas, numa área rural a 150 km da cidade de São Paulo.")

# 0012: sem o número desatualizado; o IPHAN registrou o ofício das baianas
substituir(12, "explicacao", "Hoje, Salvador tem mais de 500 vendedoras, e o IPHAN reconheceu o acarajé, junto com o papel das baianas no preparo e na venda, como patrimônio imaterial do Brasil.",
    "Hoje, o IPHAN reconhece o ofício das baianas de acarajé, ou seja, o preparo e a venda do bolinho, como patrimônio imaterial do Brasil.")

# 0013: o tombamento federal se concluiu em 1986
substituir(13, "gancho", "Em 1986, um terreiro de Salvador virou", "Nos anos 1980, um terreiro de Salvador virou")
substituir(13, "explicacao", "e em agosto de 1986 veio o tombamento federal de todo o terreno", "e em 1986 se concluiu o tombamento federal de todo o terreno")
substituir(13, "explicacao", "Foi a primeira vez que o governo brasileiro reconheceu", "Foi a primeira vez que o governo federal reconheceu")
trocar(10, tipos_espanto=["historia_humana", "origem_inesperada"])
