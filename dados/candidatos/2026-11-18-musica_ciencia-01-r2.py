"""Rodada 2 de Ciência da música: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-musica_ciencia-01.py"))
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


# 0001: concordância no gancho; nota reavaliada pelo verificador
trocar(1, nota_surpresa=3)
substituir(1, "gancho", "que foram melhor em tarefas espaciais", "que se saíram melhor em tarefas espaciais")

# 0005: "most common telephones" = telefones tradicionais; frequência fundamental
substituir(5, "gancho", "Telefones comuns não reproduzem", "Telefones tradicionais não reproduzem")
substituir(5, "gancho", "a nota fundamental perto de 150 Hz", "a frequência fundamental perto de 150 Hz")

# 0006: "usually" -> quase sempre
substituir(6, "gancho", "cada uma sempre do mesmo jeito.", "cada uma quase sempre do mesmo jeito.")

# 0007: nem toda frase funciona
substituir(7, "gancho", "Repita uma frase falada várias vezes, sem mudar nada no áudio, e ela passa a soar cantada.",
    "Repita certas frases faladas várias vezes, sem mudar nada no áudio, e elas passam a soar cantadas.")
substituir(7, "explicacao", "nada feito.",
    "nada feito. Nem toda frase funciona: as que têm sílabas de altura mais estável e um ritmo que lembra "
    "compasso favorecem a ilusão.")
acrescentar_trecho(7, 0, "Phrases that are marked by syllables with stable pitches and that favor a metrical interpretation tend to be conducive to the illusion.")

# 0008: a turnê era hipotética; tradução do timbre
substituir(8, "gancho", "para uma turnê.", "para uma turnê hipotética.")
substituir(8, "explicacao", "e empataram no mínimo em timbre.", "e ficaram pelo menos empatados em timbre.")

# 0009: a ressalva da aspereza acústica (o trecho sobre críticas ficou de fora: sem fonte baixada e conferida)
substituir(9, "explicacao",
    "Os Tsimane' distinguiam os dois tipos de som, e reagiram como os outros grupos a risadas e arfadas.",
    "Os Tsimane' distinguiam os dois tipos de som, reagiram como os outros grupos a risadas e arfadas e, como "
    "eles, não gostavam de sons acusticamente ásperos.")
acrescentar_trecho(9, 0, "They also showed the same dislike for a musical quality known as acoustic roughness.")

# 0010: as 2.000 sessões são o total de treino; a fonte fala em "ritmos" que ela não tinha ouvido
substituir(10, "explicacao",
    "que aprendeu a marcar o ritmo com a cabeça em mais de 2.000 sessões.",
    "que aprendeu a marcar o ritmo com a cabeça, inclusive em ritmos que nunca tinha ouvido, e já passou por "
    "mais de 2.000 sessões de treino.")
acrescentar_trecho(10, 1, "She later began to do so to music as well, including rhythms she has not heard before.")

# 0013: o argumento do primo veio antes; em 1939 os delegados concordaram com ele
trocar(13, gancho="Na reunião de 1939 que firmou o lá de 440 Hz como padrão, prevaleceu o argumento de um engenheiro "
    "britânico: 439, o padrão dos afinadores ingleses, é primo, e 440 é mais fácil de gerar eletronicamente.")

# 0014: os motivos da volta só eram obscuros na época
substituir(14, "explicacao",
    "Em 1938, ele voltou de repente à União Soviética, por motivos que não ficaram claros: houve quem dissesse "
    "que foi sequestrado.",
    "Em 1938, ele voltou de repente à União Soviética. Na época, houve quem dissesse que foi sequestrado; anos "
    "depois, veio à tona que ele enfrentava problemas financeiros e com impostos nos Estados Unidos, embora ele "
    "próprio tenha contado a Bulat Galeyev que saiu por medo da guerra que se aproximava.")
acrescentar_trecho(14, 0, "Many years later, it was revealed that Theremin had returned to his native land due to tax and financial difficulties in the United States. "
    "However, Theremin himself once told Bulat Galeyev that he decided to leave himself because he was anxious about the approaching war.")

# ganchos de 0006 e 0008 encurtados para caber em 220 caracteres
substituir(6, "gancho", "ideia que ainda divide estudos.", "ideia ainda debatida.")
substituir(8, "gancho", "E seis deles escolheram um violino novo para uma turnê hipotética.",
    "Seis deles escolheram um novo para uma turnê hipotética.")
