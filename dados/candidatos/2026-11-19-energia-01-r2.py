"""Rodada 2 de Energia: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-energia-01.py"))
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


# 0002: "artificial" (houve reatores naturais)
trocar(2, gancho="O primeiro reator nuclear artificial foi montado em 1942 sob a arquibancada de um estádio de Chicago, "
    "numa quadra de squash. Sem blindagem, gerava meio watt, e um cientista vigiava com um balde de solução de cádmio.")

# 0003: os 14,8 m eram a cota do terreno, não a altura de um muro
substituir(3, "gancho", "Um engenheiro insistira numa barreira de 14,8 m contra tsunamis;",
    "Um engenheiro insistira em erguê-la 14,8 m acima do mar;")
substituir(3, "explicacao",
    "citado como a única pessoa do projeto a defender a barreira de 14,8 metros, quando muitos colegas achavam que 12 metros bastariam.",
    "citado como a única pessoa do projeto a defender que a usina fosse construída 14,8 metros acima do nível do mar, "
    "quando muitos colegas achavam que 12 metros bastariam.")
CANDIDATOS[2]["fontes"].append(wiki("Yanosuke_Hirai",
    "As a member of the committee, Hirai was the only one to insist, after examination of past tsunami records, that the plant be built 14.8 m above the sea level. [...] "
    "Although the height proposed by Hirai was five times as much as the then generally assumed expected height of a tsunami at Onagawa, the Tohoku Electric Power management consented to his proposal. [...] "
    "In contrast to the Fukushima Daiichi NPP, which experienced a meltdown of three of the plant’s six nuclear reactors, all three reactors of the Onagawa NPP which was closer to the epicenter of the earthquake and endured stronger quake and same tsunami level — survived virtually intact.",
    nome="Yanosuke Hirai"))

# 0005: rádios-relógio; a ordem causa/efeito dos 113 GWh
substituir(5, "gancho", "relógios de forno e de rádio", "relógios de forno e rádios-relógio")
substituir(5, "gancho", "deixou a rede elétrica do continente", "deixou a rede do continente")
substituir(5, "explicacao",
    "Parece nada, mas, acumulada por semanas, a diferença somou 113 GWh de energia faltante e deixou os relógios quase seis minutos atrasados.",
    "Parece nada, mas o déficit, que já somava 113 GWh de energia faltante, foi acumulando atraso por semanas e "
    "deixou os relógios quase seis minutos atrasados.")

# 0006: "muitas gravações"; "podem"
trocar(6, gancho="O zumbido da rede elétrica no fundo de muitas gravações funciona como marca-d'água: comparando suas "
    "variações com registros históricos, peritos podem datar um áudio e detectar cortes.")

# 0007: peculiaridade britânica; sem os MW de Dinorwig; recorde da TV
substituir(7, "gancho", "O recorde veio dos pênaltis", "O recorde da TV veio dos pênaltis")
substituir(7, "gancho", "centenas de megawatts extras", "centenas de MW extras")
substituir(7, "explicacao",
    "O fenômeno tem nome, TV pickup, e as próprias regras da rede o consideram exclusivo do Reino Unido.",
    "O fenômeno tem nome, TV pickup, e é tido como uma peculiaridade britânica.")
substituir(7, "explicacao", "ela vai de zero a 1.800 MW em cerca de 16 segundos", "ela vai de zero à potência total em cerca de 16 segundos")
substituir_trecho(7, 1, "zero to 1800 MW load can be achieved in approximately 16 seconds", "zero to [...] load can be achieved in approximately 16 seconds")

# 0008: a cadeia é um exemplo; o ar-condicionado é depois de apagão longo no verão; nota 3
trocar(8, nota_surpresa=3,
    gancho="Usinas precisam de eletricidade para funcionar. Após um apagão total, religar a rede pode exigir uma partida "
           "em cadeia: uma bateria liga um gerador a diesel, que liga uma hidrelétrica, que religa as usinas maiores.")
substituir(8, "explicacao",
    "porque religar tudo de uma vez, com os aparelhos de ar-condicionado ligados, exigiria mais do que a rede pode fornecer.",
    "porque, depois de um apagão longo no verão, religar tudo de uma vez, com os aparelhos de ar-condicionado "
    "ligados, exigiria mais do que a rede pode fornecer.")

# 0009: o número oficial alemão diverge (457 x 459)
substituir(9, "gancho", "Na Alemanha, isso aconteceu em 459 horas de 2024.", "Na Alemanha, isso aconteceu em mais de 450 horas de 2024.")

# 0010: "quase sempre"; canos de bambu na dinastia Han, sem a data solta; nota 3
trocar(10, nota_surpresa=3)
substituir(10, "gancho", "ele era um estorvo", "ele era quase sempre um estorvo")
substituir(10, "gancho", "Na China, por volta de 400 a.C., o gás desses poços já era levado por canos de bambu.",
    "Na China antiga, o gás desses poços já era levado por canos de bambu.")
substituir(10, "explicacao",
    "o gás que saía de perfurações em busca de salmoura começou a ser usado por volta de 400 a.C., levado por canos rústicos de bambu até onde servia para ferver a água salgada e extrair o sal, em Sichuan.",
    "relevos em tumbas da dinastia Han, em Sichuan, já mostram poços de salmoura e fornalhas aquecidas por gás "
    "natural levado por canos de bambu, que serviam para ferver a água salgada e extrair o sal.")
substituir_trecho(10, 2, "In ancient China, gas resulting from the drilling for brines was first used by about 400 BC. ", "")
CANDIDATOS[9]["fontes"].append(wiki("Science_and_technology_of_the_Han_dynasty",
    "On Han tomb brick reliefs of Sichuan province, scenes of borehole drilling for mining projects are shown. [...] "
    "They show towering derricks lifting liquid brine through bamboo pipes to the surface so that the brine could be distilled in evaporation pans over the heat of furnaces and produce salt. "
    "The furnaces were heated by natural gas brought by bamboo pipes, with gas brought up from 610 m (2,000 ft) below the surface.",
    nome="Science and technology of the Han dynasty"))

# 0011: Montrose sem os 30 anos; 1951 = primeira turbina de serviço público; relato da Strathclyde
substituir(11, "explicacao",
    "Uma versão melhorada serviu por 30 anos como fonte de emergência num hospital psiquiátrico de Montrose.",
    "Uma versão melhorada serviu por anos como fonte de emergência num hospital psiquiátrico de Montrose.")
substituir(11, "explicacao",
    "o Reino Unido só voltou a construir turbinas eólicas em 1951, 64 anos depois do primeiro protótipo de Blyth.",
    "a primeira turbina eólica de serviço público do Reino Unido só entrou em operação em 1951, nas Órcadas, 64 "
    "anos depois do primeiro protótipo de Blyth.")
substituir(11, "explicacao", "Segundo o relato registrado na biografia dele", "Segundo o relato preservado pela Universidade de Strathclyde")
substituir_trecho(11, 0, " for the next 30 years. ", " [...] ")
acrescentar_trecho(11, 0, "Britain's first public utility wind turbine did not come into operation until 1951, when a prototype turbine built by John Brown Engineering of Glasgow was installed at Costa Head, Orkney.")
CANDIDATOS[10]["fontes"].append({
    "url": "https://www.strath.ac.uk/professionalservices/library/researchrevise/collections/archivesspecialcollections/items/papersofjamesblyth/",
    "titulo": "Papers of James Blyth (University of Strathclyde Archives & Special Collections)",
    "idioma": "en",
    "trecho": (
        "his offer to use the surplus electricity to light the main street in Marykirk was rejected by locals, fearing it ‘the work of The Devil’! [...] "
        "64 years were to pass before the first public utility wind turbine was built at Costa Head, Orkney in 1951."),
})

# 0013: quem patenteou foi o AERE; "baterias de lítio" (sem anacronismo)
trocar(13, gancho="John Goodenough achou um material capaz de dobrar a capacidade das baterias de lítio, mas a "
    "Universidade de Oxford não quis patenteá-lo. Ele cedeu os direitos sem receber royalties e, aos 97 anos, ganhou o Nobel.")

# 0015: não eram lenhadores nem dormiram; a independência se aproximava; a morte em 2004
trocar(15, gancho="Em 2001, três homens que buscavam lenha na Geórgia acharam duas cápsulas quentes, com o chão fumegando "
    "ao redor, e passaram a noite encostados nelas. Eram núcleos radioativos de geradores soviéticos abandonados.")
substituir(15, "explicacao", "Com a independência da Geórgia, a obra parou", "Com a independência da Geórgia se aproximando, a obra parou")
substituir(15, "explicacao", "Os três se feriram e um deles morreu.", "Os três se feriram, e um deles morreu em 2004, mais de dois anos depois.")
acrescentar_trecho(15, 0, "He developed sepsis, and died of heart failure on May 13, 2004, 893 days after first exposure.")

# 0016: 3,15/300 ≈ 1%
substituir(16, "explicacao", "de modo que a fusão devolveu menos de 1% da energia gasta pela instalação",
    "de modo que a fusão devolveu só cerca de 1% da energia gasta pela instalação")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(13, "explicacao", "podia servir de cátodo e dobrar a capacidade das baterias de íon-lítio",
    "podia servir de cátodo e dobrar a capacidade das baterias de lítio recarregáveis")
