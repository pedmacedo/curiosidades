"""Rodada 2 de Videogames: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-videogames-01.py"))
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


# 0001: Los Alamos (grupo de eletrônica da bomba), patente "na época", estado de Nova York
trocar(1, gancho="Em 1958, um físico que tinha chefiado a equipe de eletrônica da bomba atômica, em Los Alamos, criou um jogo "
                 "de tênis para animar a visita do público a um laboratório dos EUA. O jogo foi desmontado e caiu no esquecimento.")
substituir(1, "explicacao", "Antes, de 1943 a 1945, tinha chefiado a divisão de eletrônica do Projeto Manhattan.",
    "Na Segunda Guerra, trabalhou no Projeto Manhattan, em Los Alamos, onde chefiou o grupo de eletrônica; sua equipe "
    "criou o mecanismo de ignição e os instrumentos de medição da primeira bomba atômica.")
substituir(1, "explicacao", "Higinbotham não achava que ele merecesse patente:",
    "Na época, Higinbotham não achou que o jogo merecesse patente, por ser só uma extensão do programa da bola quicando;")
substituir(1, "explicacao", "em Nova York", "no estado de Nova York")
CANDIDATOS[0]["fontes"].append(wiki("William_Higinbotham",
    "During World War II, he was working at Los Alamos Laboratory and headed the lab's electronics group in the later years of the war, where his team developed electronics for the first atomic bomb. "
    "His team created the bomb's ignition mechanism as well as measuring instruments for the device.",
    nome="William Higinbotham"))

# 0002: nome do programa e ideia a três
substituir(2, "explicacao", "O apelido era \"Planetário Caro\", por causa do preço do computador.",
    "O programa se chamava \"Expensive Planetarium\" (planetário caro), por causa do preço do computador.")
substituir(2, "explicacao", "Steve Russell tinha a ideia, mas não pretendia programá-la, e os colegas o pressionavam.",
    "Steve Russell tinha concebido o jogo com dois amigos, mas não pretendia programá-lo, e os colegas o pressionavam.")
acrescentar_trecho(2, 0, "came up with the idea for Spacewar! [...] "
    "Russell, Graetz and Wiitanen developed the basic Spacewar! concept in the summer of 1961")

# 0004: um numismata só fez a comparação
trocar(4, nota_surpresa=3)
substituir(4, "gancho", "Numismatas compararam a produção da Casa da Moeda japonesa com a renda do jogo e não acharam sinal disso.",
    "Um numismata comparou a produção da Casa da Moeda japonesa com a renda do jogo e não achou sinal disso.")

# 0007: engenheiro sem experiência em videogames; primeiro jogo da empresa
trocar(7, gancho="O Pong nasceu como exercício de treino para um engenheiro que nunca tinha feito videogames, inspirado "
                 "num pingue-pongue de console doméstico. Testado num bar, o protótipo parou: a caixa de moedas transbordou.")
substituir(7, "explicacao", "virou o primeiro produto da empresa", "virou o primeiro jogo da empresa")
acrescentar_trecho(7, 0, "Soon after the founding, Bushnell hired Allan Alcorn because of his experience with electrical engineering and computer science")

# 0008: único controle extra, primeira pistola de luz
substituir(8, "explicacao", "O único acessório lançado foi um rifle de luz, a primeira pistola de videogame,",
    "O único controle extra lançado foi um rifle de luz, a primeira pistola de luz da história dos videogames,")

# 0010: o excesso do Pac-Man, sem juízo de qualidade; 728 mil exatos
substituir(10, "explicacao",
    "Com o Pac-Man para o Atari 2600 a empresa tinha feito pior ainda: fabricou 12 milhões de cartuchos quando só havia cerca de 10 milhões de consoles vendidos.",
    "Com o Pac-Man para o Atari 2600, o excesso tinha sido ainda maior: a empresa fabricou 12 milhões de cartuchos quando "
    "só havia cerca de 10 milhões de consoles vendidos e, mesmo depois de enviar 7 milhões às lojas, ficou com mais de 5 "
    "milhões encalhados.")
substituir(10, "explicacao", "disse que foram cerca de 728 mil cartuchos, não milhões", "disse que foram 728 mil cartuchos, não milhões")
acrescentar_trecho(10, 0, "although it became the console's best-selling game after shipping 7 million units, it left Atari with over 5 million unsold cartridges")

# 0011 (aprovado): troca opcional sugerida pelo verificador
substituir(11, "gancho", "Esses baralhos japoneses se chamam karuta", "Baralhos japoneses como esses se chamam karuta")

# 0012: a lei não lhe dava direito; briga entre empresas
substituir(12, "gancho",
    "e a lei da URSS não deixava ninguém lucrar com as próprias criações. O jogo se espalhou de graça, e os direitos viraram uma briga entre vários países.",
    "e a lei da URSS não lhe dava direito de lucrar com o jogo. Ele se espalhou de graça, e os direitos viraram uma briga entre empresas de vários países.")

# 0014: o reset que resolveu e a ressalva sobre o jogo como modelo
substituir(14, "explicacao",
    " Segundo um jogador da época, em alguns servidores os personagens fracos morriam quase na hora nas grandes cidades.", "")
substituir(14, "explicacao", "A Blizzard só acabou com a peste reiniciando os servidores.",
    "Reiniciar os servidores um a um não resolveu: a peste voltava. A Blizzard só acabou com ela fazendo os servidores "
    "voltarem ao estado de antes da epidemia, e alguns pesquisadores lembraram que, num jogo em que o personagem "
    "ressuscita, as pessoas não se comportam como no mundo real.")
acrescentar_trecho(14, 0, "Blizzard attempted to put a stop to the pandemic with hotfixes, including restarting each game server on a rolling basis, but Corrupted Blood outbreaks soon re-emerged in restarted areas. [...] "
    "Blizzard performed hard resets on the World of Warcraft servers, resetting Azeroth to its state from just before the introduction of Corrupted Blood. [...] "
    "Neil Ferguson, director of the MRC Centre for Global Infectious Disease Analysis, noted that because characters could regenerate, there was not as much risk in becoming infected with a virtual disease, limiting the applicability of player behavior to the real world. [...] "
    "While World of Warcraft player characters are resurrected after death")

# 0015: "mais de uma década" (fonte jornalística) e doença parecida com a aids
trocar(15, gancho="Em 2011, jogadores do Foldit, um game de dobrar proteínas, modelaram em dez dias uma enzima de vírus de macaco "
                  "que causa doença parecida com a aids, cuja estrutura desafiava cientistas havia mais de uma década.")
substituir(15, "explicacao", "Sua estrutura cristalina estava sem solução havia 15 anos.",
    "Sua estrutura cristalina estava sem solução havia mais de uma década.")
CANDIDATOS[14]["fontes"].append({
    "url": "https://www.nationalgeographic.com/science/article/computer-gamers-solve-problem-in-aids-research-that-puzzled-scientists-for-years",
    "titulo": "Computer gamers solve problem in AIDS research that puzzled scientists for years (National Geographic)",
    "idioma": "en",
    "trecho": "When scientists struggle with a problem for over a decade [...] "
              "They discovered the structure of a protein belonging to the Mason-Pfizer monkey virus (M-PMV), a close relative of HIV that causes AIDS in monkeys."})

# 0016: três de cinco amnésicos; amnésia anterógrada
trocar(16, gancho="Num estudo publicado em 2000, três de cinco pacientes com amnésia que jogaram Tetris viram peças caindo ao "
                  "pegar no sono, sem lembrar de ter jogado. Uma delas punha os dedos nas teclas certas sem saber por quê.")
substituir(16, "explicacao", "cinco pessoas com amnésia por lesões no hipocampo, sem memória de curto prazo",
    "cinco pessoas com amnésia por lesões no hipocampo, incapazes de formar novas memórias conscientes")

# notas reavaliadas pelo verificador
for _n in (14, 15, 16):
    trocar(_n, nota_surpresa=4)

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(7, "gancho", "o protótipo parou: a caixa de moedas transbordou.", "o protótipo deu defeito: a caixa de moedas transbordou.")
