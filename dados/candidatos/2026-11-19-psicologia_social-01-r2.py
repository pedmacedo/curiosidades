"""Rodada 2 de Psicologia social: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-19-psicologia_social-01.py"))
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


# 0001: os 5% com um parceiro eram de respostas, não de voluntários; sai o número
substituir(1, "explicacao",
    "Bastava um único ator dando a resposta certa para que só 5% continuassem seguindo a maioria.",
    "Bastava um único ator dando a resposta certa para que a adesão ao erro da maioria despencasse.")
substituir_trecho(1, 0,
    "In studies that had one actor give correct responses to the questions, only 5% of the participants continued to answer with the majority.",
    "The presence of a single dissenter dramatically reduced conformity")

# 0003: o gancho fala de um estudo; frase da explicação reescrita
trocar(3, gancho="A história das 38 testemunhas inertes no assassinato de Kitty Genovese, que inspirou o estudo do efeito "
    "espectador, era exagerada. E um estudo com câmeras de rua viu alguém ajudar em mais de 90% das brigas.")
substituir(3, "explicacao",
    "a presença de outras pessoas inibia a ajuda, muitas vezes por larga margem",
    "quem estava acompanhado tendia a ajudar bem menos do que quem estava sozinho")

# 0004: a barraca derrubada é lembrança de um membro da equipe; nota 3
trocar(4, nota_surpresa=3,
    gancho="Antes de Robbers Cave, o famoso acampamento em que meninos viraram inimigos, houve um ensaio em 1953 dado "
           "como fracasso. Segundo um membro da equipe, colegas derrubaram uma barraca para atiçar a rivalidade.")

# 0005: as gravações foram muito discutidas em 2017, não reveladas em 2017
substituir(5, "explicacao",
    "Em 2017, gravações do site oficial do estudo mostraram o assistente",
    "Gravações do site oficial do estudo, muito discutidas em 2017, mostram o assistente")

# 0007: Dunbar pediu dados de símios, não só de grandes símios
substituir(7, "explicacao",
    "Dunbar respondeu que a conta deveria usar só dados de grandes símios.",
    "Dunbar respondeu que a conta deveria usar só dados de símios (gibões, orangotangos, chimpanzés, bonobos e "
    "gorilas), poucos demais para uma análise estatística, segundo os críticos.")
acrescentar_trecho(7, 0,
    "This would mean that his cognitive limit would be based on 16 pair-living gibbon species, three solitary orangutans, "
    "and only four group living great apes (chimpanzees, bonobos and two gorilla species), which would not be sufficient for statistical analyses.")

# 0008: "sem parar" exagera; a rejeição do esporão é posição de Waller
substituir(8, "gancho", "dezenas de pessoas dançaram sem parar por semanas", "dezenas de pessoas passaram semanas dançando nas ruas")
substituir(8, "explicacao",
    "A hipótese do esporão-do-centeio perdeu força, porque o envenenamento",
    "Waller rejeita a hipótese do esporão-do-centeio, porque o envenenamento")
acrescentar_trecho(8, 1, "However, the historian John Waller has debunked the ergot hypothesis in his brilliant book on the dancing plague")

# 0009: tese de um único autor independente, sem confirmação
trocar(9, gancho="Um livro de 1956 virou caso clássico da dissonância cognitiva: quando o fim do mundo não veio, uma seita "
    "teria redobrado a fé. Em 2025, um estudo de arquivos recém-abertos afirmou o contrário.")
substituir(9, "explicacao", "o pesquisador Thomas Kelly", "o pesquisador independente Thomas Kelly")
acrescentar_trecho(9, 1, "Independent Scholar, Washington DC.")

# 0010: cerca de três quartos subestimavam, não todos
trocar(10, gancho="Em Riad, 87% dos jovens maridos de um estudo apoiavam, em sigilo, o trabalho feminino fora de casa, mas a "
    "maioria subestimava o apoio dos vizinhos. Informados, mais deles inscreveram a esposa num serviço de empregos.")

# 0011: sem "desconhecidos"; frase do ganho sem aparente contradição
trocar(11, gancho="Pessoas divididas em grupos só por preferirem quadros de Klee ou de Kandinsky passaram a favorecer o "
    "próprio grupo ao dividir dinheiro, chegando a abrir mão de ganho só para ficar à frente do outro grupo.")

# 0012: os dados reapareceram antes da publicação de 2011; sai o ano
trocar(12, gancho="Entre 1924 e 1927, uma fábrica aumentou a luz e a produção subiu; diminuiu a luz e ela subiu de novo, até "
    "na sala de controle. Daí veio o \"efeito Hawthorne\". Décadas depois, os dados originais mal o confirmaram.")
substituir(12, "explicacao",
    "até achá-los num microfilme da Universidade de Wisconsin em Milwaukee, em 2011.",
    "até achá-los num microfilme da Universidade de Wisconsin em Milwaukee.")
substituir_trecho(12, 0,
    "before finding it in a microfilm at the University of Wisconsin in Milwaukee in 2011.",
    "before finding it in a microfilm at the University of Wisconsin in Milwaukee [...]")

# 0013: sem "o mesmo da obediência"; "muitas" correntes; o viés no sentido contrário
substituir(13, "explicacao",
    "O experimento foi de Stanley Milgram, o mesmo dos estudos de obediência, e foi divulgado em 1967.",
    "O experimento foi do psicólogo Stanley Milgram e foi divulgado em 1967.")
substituir(13, "explicacao",
    "A maioria das correntes se perdeu porque alguém se recusava a continuar.",
    "Muitas correntes se perderam porque alguém se recusava a continuar.")
substituir(13, "explicacao",
    "gente que se considerava bem relacionada.",
    "gente que se considerava bem relacionada. Por outro lado, como ninguém enxerga a rede inteira, as cartas nem "
    "sempre seguiam o caminho mais curto, o que pode ter alongado as correntes.")
acrescentar_trecho(13, 0,
    "since the participants of the Milgram experiment do not have a topological map of the social network, they might actually be sending the package further away from the target rather than sending it along the shortest path. "
    "This is very likely to increase route length, overestimating the average number of ties needed to connect two random people.")

# 0014: hooliganismo com contexto; "pode não saber"
substituir(14, "explicacao",
    "Em Hillsborough, em 1989, parte dos policiais e fiscais estava tão preocupada com o que via como possível vandalismo de torcedores",
    "No desastre do estádio de Hillsborough, na Inglaterra, em 1989, parte dos policiais e fiscais estava tão "
    "preocupada com o que via como possível violência de torcedores (o hooliganismo)")
substituir(14, "explicacao",
    "Quem chega atrás muitas vezes não sabe o que acontece na frente e continua empurrando.",
    "Quem chega atrás pode não saber o que acontece na frente e continuar empurrando.")
acrescentar_trecho(14, 0, "Examples of crushes are the Hillsborough disaster in Sheffield, South Yorkshire, England, in 1989")
