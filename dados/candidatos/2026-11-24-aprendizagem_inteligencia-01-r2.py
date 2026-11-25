"""Rodada 2 de Aprendizagem e inteligência: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-aprendizagem_inteligencia-01.py"))
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


# 0005: o apelido "Termites" não está nas fontes citadas
substituir(5, "explicacao", "e o grupo chegou a 1.528 participantes, apelidados de \"Termites\".",
    "e o grupo chegou a 1.528 participantes.")

# 0008: cada voluntário passou pelas duas condições; os 80% do estudo original
substituir(8, "explicacao",
    "No teste, com quadros novos dos mesmos pintores, quem tinha visto tudo misturado reconheceu melhor os estilos.",
    "Cada voluntário passou pelas duas condições, com pintores diferentes em cada uma. No teste, com quadros "
    "novos, os pintores vistos de forma misturada foram reconhecidos com mais acerto.")
substituir(8, "explicacao",
    "e só 12% escolheram a misturada, o contrário do que o teste mostrava.",
    "e só 12% escolheram a misturada, o contrário do que o teste mostrava. No estudo original, 80% também "
    "tinham preferido o agrupado.")
acrescentar_trecho(8, 0, "experiment (i.e., 80%) reported that massing had led to better learning than spacing.")

# 0009: a meta-análise e o teste holandês tratam de meninas em provas de matemática
substituir(9, "explicacao", "Uma meta-análise de 2015 concluiu",
    "Uma meta-análise de 2015, com estudos sobre meninas em idade escolar, concluiu")
substituir(9, "explicacao",
    "O maior teste experimental, com 2.064 estudantes holandeses do ensino médio, não achou efeito",
    "O maior teste experimental, com 2.064 estudantes holandeses do ensino médio em provas de matemática, não "
    "achou efeito")
acrescentar_trecho(9, 0,
    "\"that the effects of stereotype threat on math test performance should not be overgeneralized.\" [...] "
    "Reviews have raised concerns that the effect might have been over-estimated in the performance of schoolgirls "
    "and argued that the field likely suffers from publication bias.")

# 0010: sem o número de shows em Hamburgo
substituir(10, "explicacao",
    "com exemplos como os Beatles, que tocaram ao vivo mais de 1.200 vezes em Hamburgo entre 1960 e 1964.",
    "com exemplos como os Beatles e suas longas temporadas de shows em Hamburgo.")
substituir_trecho(10, 2,
    "The Beatles performed live in Hamburg, Germany over 1,200 times from 1960 to 1964, amassing more than 10,000 hours of playing time, therefore meeting the 10,000-Hour Rule.",
    "A common theme that appears throughout Outliers is the \"10,000-Hour Rule\", based on a study by Anders Ericsson. "
    "Gladwell claims that greatness requires enormous time, using the source of the Beatles' musical talents and Gates' computer savvy as examples.")

# 0011: Sofia e os limites do "experimento"
substituir(11, "explicacao",
    "Em 1965, cortejou por cartas Klara, uma professora de línguas ucraniana, e nelas expôs o projeto pedagógico que tinha em mente. ",
    "")
substituir(11, "explicacao",
    "jornal americano notou que os detratores o pintavam como um Dr. Frankenstein.",
    "jornal americano notou que os detratores o pintavam como um Dr. Frankenstein. A filha do meio, Sofia, chegou "
    "a sexta melhor jogadora do mundo e depois largou o xadrez. E é o caso de uma única família, sem grupo de "
    "comparação: como as meninas herdaram os genes dos mesmos pais que as treinaram, não dá para separar talento "
    "de treino, e o experimento não prova que qualquer criança viraria gênio.")
acrescentar_trecho(11, 0,
    "Still, Sophia, the least successful of the three, who became the sixth-best female player in the world, quit playing, "
    "studied painting and interior design, and focused on being a housewife and mother.")

# 0012: primeira infância; "tenderia a 100%"
trocar(12, gancho="O peso dos genes nas diferenças de QI parece crescer com a idade: cerca de 20% em bebês e 60% em "
    "adultos, segundo uma revisão. E, se todos vivessem no mesmo ambiente, esse peso tenderia a 100%.")
substituir(12, "explicacao", "se todos tivessem o mesmo ambiente, ela seria de 100%",
    "se todos tivessem o mesmo ambiente, ela tenderia a 100%")
substituir(12, "explicacao", "de cerca de 20% na infância para 60% na vida adulta",
    "de cerca de 20% na primeira infância para 60% na vida adulta")

# 0013: equipe francesa, 20 voluntários; bloquear o aprendizado, não apagar memórias
substituir(13, "explicacao",
    "Em 2017, uma equipe de pesquisadores tocou amostras de ruído para pessoas adormecidas.",
    "Em 2017, uma equipe francesa tocou amostras de ruído para 20 voluntários adormecidos.")
substituir(13, "explicacao",
    "mas o estudo mostra que o cérebro adormecido pode tanto gravar quanto apagar.",
    "mas o estudo sugere que o cérebro adormecido pode tanto gravar algo novo quanto bloquear esse "
    "aprendizado, conforme a fase do sono.")
acrescentar_trecho(13, 1,
    "École Normale Supérieure-PSL Research University, Paris, 75005 France [...] "
    "Human listeners were tested in a whole-night sleep experiment [...] "
    "= 20) were instructed to discriminate Gaussian noise")

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(11, "explicacao", "E é o caso de uma única família, sem grupo de comparação: como as meninas herdaram os genes dos mesmos pais que as treinaram, não dá para separar talento de treino, e o experimento não prova que qualquer criança viraria gênio.", "Mas é o caso de uma única família, e a dúvida segue de pé: um livro sobre as irmãs se chama justamente \"Treino ou gênio?\".")
acrescentar_trecho(11, 0, "In 1992, Cathy Forbes published a book entitled The Polgár Sisters: Training or Genius?")
substituir(12, "explicacao", "E métodos genômicos recentes dão estimativas bem menores que os de gêmeos.", "E métodos genômicos recentes dão estimativas menores que os de gêmeos.")
