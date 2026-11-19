"""Rodada 2 de Animais extremos: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-animais_extremos-01.py"))
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


def acrescentar_trecho(n, i_fonte, extra):
    CANDIDATOS[n - 1]["fontes"][i_fonte]["trecho"] += " [...] " + extra


# 0001: o contraste vácuo x ultravioleta; o estado "tun" como a fonte descreve
trocar(1, gancho="Em 2007, tardígrados desidratados passaram 10 dias expostos ao espaço. O vácuo sozinho não lhes fez "
    "efeito significativo; o que matou muitos deles foi a luz ultravioleta do Sol.")
substituir(1, "explicacao",
    "eles perdem quase toda a água do corpo e entram num estado de vida suspensa em que podem passar anos.",
    "eles recolhem as patas e secam, formando um barrilzinho sem atividade metabólica (o estado \"tun\"), em "
    "que podem passar anos sem comida nem água.")
acrescentar_trecho(1, 0, "by drawing their legs in and forming a desiccated cyst, the cryptobiotic 'tun' state, where no "
    "metabolic activity takes place. In this state, they can go without food or water for several years.")

# 0002: a margem de erro da idade
trocar(2, gancho="O tubarão-da-groenlândia é o vertebrado mais longevo conhecido: datado pelo cristalino dos olhos, o "
    "mais velho teria 392 anos, com margem de 120 para mais ou para menos. Só se reproduz por volta dos 150.")

# 0003: o mecanismo e a ressalva de que nunca foi visto na natureza
substituir(3, "explicacao", "Na prática, na natureza",
    "Ela faz isso por transdiferenciação: células já especializadas mudam de identidade e viram outros tipos de "
    "célula. A reversão foi documentada em laboratório, mas nunca foi observada no ambiente natural, em parte "
    "porque acontece muito rápido. Na prática, na natureza")
acrescentar_trecho(3, 0, "It does this through the cell development process of transdifferentiation, which alters the "
    "differentiated state of the cells and transforms them into new types of cells.")
acrescentar_trecho(3, 0, "The process has not been observed in their natural habitat, in part because the process is "
    "quite rapid and because field observations at the right moment are unlikely.")

# 0004: a espécie certa; cavitação, não fervura
trocar(4, gancho="Um camarão-louva-a-deus, o Odontodactylus scyllarus, golpeia com aceleração de 10.400 g e chega a "
    "83 km/h. É tão rápido que a água vira bolhas de vapor que, ao estourar, atingem a presa uma segunda vez.")

# 0006: o recorde é de distância em voo migratório sem escalas
trocar(6, gancho="Em 2022, um jovem maçarico-de-bico-virado voou do Alasca à Tasmânia sem pousar nem comer: pelo "
    "menos 13.560 km em 11 dias, recorde de distância num voo migratório sem escalas.")
substituir(6, "explicacao",
    "é o voo sem escalas mais longo conhecido de qualquer ave, e a jornada mais longa de qualquer animal sem parar para comer",
    "é a jornada mais longa conhecida de qualquer animal sem parar para comer")

# 0007: sem a comparação com as plantas; "salvo tentativas esporádicas"
substituir(7, "gancho", "passa a queimar frutose, como fazem as plantas.", "passa a queimar frutose em vez de glicose.")
substituir(7, "explicacao", "e a respiração para.", "e a respiração para, salvo tentativas esporádicas.")

# 0009: a assexualidade é posta em dúvida; habitat e tamanho como a fonte diz
trocar(9, confianca="consenso_parcial")
substituir(9, "gancho", "E esse grupo vive há mais de 25 milhões de anos sem sexo.",
    "E esse grupo parece viver há mais de 25 milhões de anos sem sexo.")
substituir(9, "explicacao",
    "que vivem em água doce, musgos e solos úmidos. A olho nu, mal aparecem como pontinhos brancos.",
    "que vivem em ambientes de água doce do mundo todo. A maioria é pequena demais para o olho nu, mas aparece "
    "como pontinhos brancos sob uma lupa simples.")
substituir(9, "explicacao", "algo raríssimo entre os animais.",
    "algo raríssimo entre os animais. Mas um estudo encontrou sinais de troca genética entre indivíduos na "
    "espécie Adineta vaga, o que põe em dúvida essa assexualidade total.")
acrescentar_trecho(9, 0, "is a class of rotifers found in freshwater habitats all over the world.")
acrescentar_trecho(9, 0, "However, a new study provided evidence for interindividual genetic exchange and recombination "
    "in Adineta vaga, a species previously thought to be anciently asexual.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(9, "explicacao", "de 0,15 a 0,7 milímetro", "em geral de 0,15 a 0,7 milímetro")
substituir(2, "gancho", "Só se reproduz por volta dos 150.", "Só começa a se reproduzir por volta dos 150.")
