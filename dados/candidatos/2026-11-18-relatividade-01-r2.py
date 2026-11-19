"""Rodada 2 de Relatividade: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-18-relatividade-01.py"))
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


# 0001: o que conta é a distância do centro da Terra
trocar(1, nota_surpresa=3)
substituir(1, "explicacao",
    "Pela relatividade geral, quanto mais fraca a gravidade, mais rápido o tempo passa, e na altitude dos satélites isso adianta os relógios em cerca de 45,8 microssegundos por dia.",
    "Pela relatividade geral, o tempo passa mais devagar perto de um corpo de grande massa; como os satélites ficam "
    "bem mais longe do centro da Terra do que nós, isso adianta os relógios deles em cerca de 45,8 microssegundos por dia.")
acrescentar_trecho(1, 1, "the slowing down of time near gravitating bodies. "
    "In case of the GPS, the receivers are closer to the center of Earth than the satellites")

# 0003: o gancho no tom da fonte; sem "química clássica"
substituir(3, "gancho", "Sem eles, uma bateria de estanho, que é parecido com o chumbo, funcionaria igual. Não funciona.",
    "Sem eles, o chumbo agiria como o estanho, e baterias de estanho funcionariam. Não funcionam.")
substituir(3, "explicacao", "e pela química clássica os dois deveriam se comportar de modo muito parecido",
    "e, sem os efeitos relativísticos, os dois deveriam se comportar de modo muito parecido")

# 0004: Rossi-Hall entre os primeiros testes, não necessariamente o primeiro
substituir(4, "explicacao",
    "Foi com múons, no experimento de Rossi e Hall, em 1941, que a dilatação do tempo foi observada pela primeira vez.",
    "Em 1941, o experimento de Rossi e Hall usou múons justamente para observar essa dilatação do tempo, num dos "
    "primeiros testes diretos da relatividade especial.")

# 0005: repetições cada vez mais precisas
substituir(5, "explicacao", "O experimento foi repetido com mais precisão em 2010.",
    "Depois, o experimento foi repetido várias vezes, com métodos cada vez mais precisos.")
acrescentar_trecho(5, 0, "Because the Hafele–Keating experiment has been reproduced by increasingly accurate methods")

# 0006: "a célebre confirmação de 1919", não "a primeira"
substituir(6, "gancho", "A primeira confirmação da relatividade geral veio, em boa parte, de Sobral",
    "A célebre confirmação da relatividade geral em 1919 veio, em boa parte, de Sobral")
substituir(6, "gancho", "no eclipse de 1919, as melhores fotos", "no eclipse, as melhores fotos")

# 0007: não é mito desmentido
trocar(7, tipos_espanto=["historia_humana", "contraintuitivo"])

# 0008: 1960; 22,5 m entre fonte e absorvedor; a gravidade muda a luz
trocar(8, gancho="Em 1960, físicos de Harvard mediram como a gravidade muda a \"cor\" da luz em 22,5 metros, do telhado "
    "ao porão. Subindo, os raios gama perdiam um tiquinho de energia: 2,56 partes em mil trilhões, como previa Einstein.")
substituir(8, "explicacao", "Robert Pound e seu aluno de pós-graduação Glen Rebka o mediram numa torre",
    "Em 1960, Robert Pound e seu aluno de pós-graduação Glen Rebka o mediram numa torre")
substituir(8, "explicacao", "Uma fonte de raios gama ficava numa ponta e um absorvedor de ferro na outra, a 22,5 metros,",
    "Uma fonte de raios gama ficava perto do telhado e um absorvedor de ferro no porão, a 22,5 metros,")
acrescentar_trecho(8, 0, "It was to be Pound and Rebka's somewhat later contribution in April 1960 [...] "
    "was placed near the roof of the building. [...] was placed in the basement.")

# 0010: sem o número incoerente do próton; o anúncio depois da análise
trocar(10, gancho="A primeira onda gravitacional detectada, em 2015, deformou o espaço na proporção de mudar a distância "
    "até a estrela mais próxima na espessura de um fio de cabelo. Em som, o sinal parece o pio de um passarinho.")
substituir(10, "explicacao",
    "O sinal chegou em 14 de setembro de 2015 e só foi anunciado em 11 de fevereiro de 2016, depois de os cientistas se certificarem de que não era um teste simulado.",
    "O sinal chegou em 14 de setembro de 2015, quando os detectores ainda estavam em modo de testes, antes do início "
    "formal das observações. Foi preciso descartar que fosse um dos sinais falsos que a equipe inseria de propósito "
    "para se testar e analisar os dados a fundo, e a descoberta só foi anunciada em 11 de fevereiro de 2016.")
substituir(10, "explicacao",
    "A onda mudou o comprimento efetivo de 1.120 quilômetros do LIGO em um milésimo da largura de um próton, o que equivale a mudar a distância até a estrela mais próxima fora do Sistema Solar na espessura de um fio de cabelo.",
    "No LIGO, a mudança no comprimento dos braços foi uma fração minúscula da largura de um próton: em proporção, é "
    "como mudar a distância até a estrela mais próxima fora do Sistema Solar na espessura de um fio de cabelo.")
acrescentar_trecho(10, 0, "In February 2015, the two advanced detectors were brought into engineering mode [...] "
    "with formal science observations due to begin on 18 September 2015. "
    "Throughout the development and initial observations by LIGO, several \"blind injections\" of fake gravitational wave signals were introduced to test the ability of the researchers to identify such signals.")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(6, "gancho", "Einstein agradeceu ao \"céu do Brasil\".", "Einstein deu o crédito ao \"céu do Brasil\".")
substituir(8, "gancho", "em 22,5 metros, do telhado ao porão.", "em 22,5 metros, entre o telhado e o porão.")
substituir(8, "explicacao", "para não se espalharem.",
    "para não se espalharem. A cada poucos dias, fonte e absorvedor trocavam de lugar, para comparar os raios subindo e descendo.")
acrescentar_trecho(8, 0, "The source and absorber units were interchanged every several days to allow comparison between the results with the γ-rays rising versus the γ-rays falling")
substituir(10, "gancho", "até a estrela mais próxima na espessura", "até a estrela mais próxima além do Sol na espessura")
substituir(10, "gancho", "o pio de um passarinho", "o pio de um pássaro")
# encurta o gancho para caber nos 220 caracteres (sem mudar o sentido)
substituir(8, "gancho", "perdiam um tiquinho de energia", "perdiam um pouco de energia")
