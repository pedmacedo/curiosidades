"""Rodada 2 de Desenvolvimento humano: aplica as correções pedidas pelo verificador."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("base", Path(__file__).with_name("2026-11-24-desenvolvimento_humano-01.py"))
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


# 0001: atribuir ao estudo; consenso parcial; 31 bebês
trocar(1, confianca="consenso_parcial",
    gancho="Um estudo que mediu bebês até todos os dias concluiu que eles não crescem aos pouquinhos: passam de 2 a 63 "
           "dias sem crescimento mensurável e então dão um salto, às vezes de até um centímetro num dia.")
substituir(1, "explicacao", "e três deles todos os dias, durante os ",
    "e três deles todos os dias; eram 31 bebês, 19 meninas e 12 meninos, acompanhados durante os ")
substituir(1, "explicacao", "Pelas contas do estudo, de 90% a 95%", "Os autores estimaram que de 90% a 95%")
substituir(1, "explicacao", "Lampl chamou o modelo de saltação e estase:", "Lampl chamou a proposta de modelo de saltação e estase:")

# 0002: o mecanismo é debatido; carta de Skoyles e réplica dos autores
trocar(2, tipos_espanto=["escala_absurda", "conexao_inesperada", "misterio_aberto"],
    gancho="Aos 5 anos, o cérebro de uma criança usa o dobro da glicose do cérebro de um adulto. É também a fase em que "
           "o corpo cresce mais devagar, e cientistas ainda debatem por que as duas coisas coincidem.")
substituir(2, "explicacao",
    "A ligação entre as duas curvas é uma interpretação dos autores, não uma prova "
    "de causa.",
    "A ligação é uma interpretação. Numa carta, o pesquisador John Skoyles propôs outra explicação: o que "
    "ligaria o cérebro faminto ao corpo que cresce devagar seria o risco de hipoglicemia provocado pelos "
    "músculos, não uma troca de energia. Os autores responderam que quem acompanha o pico do cérebro é a "
    "queda no ritmo de crescimento, não a massa muscular.")
substituir(2, "explicacao", "Kuzawa nota um efeito que os pais "
    "conhecem: a partir de certa idade fica difícil adivinhar a idade de uma criança pelo tamanho, e é "
    "preciso ouvi-la falar. ", "")
CANDIDATOS[1]["fontes"] += [
    {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/25385652?resultType=core&format=json",
     "titulo": "Skeletal muscle-induced hypoglycemia risk, not life history energy trade-off, links high child brain glucose use to slow body growth (Skoyles, PNAS, 2014), registro na Europe PMC",
     "idioma": "en",
     "trecho": "Skeletal muscle-induced hypoglycemia risk, not life history energy trade-off, links high child brain glucose use to slow body growth. [...] Skoyles JR."},
    {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/article/MED/25385651?resultType=core&format=json",
     "titulo": "Reply to Skoyles: Decline in growth rate, not muscle mass, predicts the human childhood peak in brain metabolism (Kuzawa et al., PNAS, 2014), registro na Europe PMC",
     "idioma": "en",
     "trecho": "Reply to Skoyles: Decline in growth rate, not muscle mass, predicts the human childhood peak in brain metabolism. [...] Kuzawa CW"},
]

# 0003: a origem do 25 (palpite de Giedd à Time); Laurence Steinberg
trocar(3, gancho="A ideia de que o cérebro fica pronto aos 25 anos nasceu de um palpite, não de um resultado. Um estudo de "
                 "2025, com exames de 3.802 pessoas, viu a fiação cerebral seguir em fase adolescente até cerca de 32.")
substituir(3, "explicacao",
    "Mas, como lembra o Escritório de Ciência e "
    "Sociedade da Universidade McGill, o 25 resume tendências gerais, sem um estudo definitivo por trás, e "
    "até o psicólogo Larry Steinberg, muito citado no tema, o trata como uma estimativa, não um prazo.",
    "Mas o número vem de um palpite do psiquiatra Jay Giedd, do NIMH, ao comentar na revista Time um estudo "
    "que acompanhou jovens com ressonâncias repetidas: os exames iam até os 18 ou 20 anos, e ele disse que, "
    "se tivesse de escolher um número, provavelmente iria até os 25. Até o psicólogo Laurence Steinberg, "
    "muito citado no tema, disse não saber por que se escolheu o 25.")
CANDIDATOS[2]["fontes"].append(wiki("Brain_matures_at_25_myth",
    "It originated from the research of neuroscientist Jay Giedd, who, when speaking to Time magazine, speculatively expressed a desire to have continued his studies on brain development, which ended at age 18 to 20 and found the brain still developing at those points, all the way to age 25. [...] "
    "Jay N. Giedd, a child and adolescent psychiatrist and researcher at the National Institute of Mental Health (NIMH) [...] "
    "He is quoted as saying, \"When we started, we thought we'd follow kids until about 18 or 20. If we had to pick a number now, we'd probably go to age 25.\" [...] "
    "Laurence Steinberg is another influential figure in adolescent brain psychology. [...] "
    "He would later say in a 2022 article that he was not sure where the \"25\" number came from in regards to the age of brain maturity, stating, \"I honestly don't know why people picked 25.",
    nome="\"Brain matures at 25\" myth"))

# 0004: poda pelo complemento mostrada em camundongos; efeito modesto
trocar(4, gancho="Em camundongos, uma peça do sistema imune ajuda a podar conexões do cérebro jovem. Em humanos, variantes "
                 "do gene dela, o C4, que aumentam sua produção no cérebro elevam um pouco o risco de esquizofrenia.")
substituir(4, "explicacao", "maior o risco. ",
    "maior o risco. O efeito é modesto: entre as variantes comuns, o risco relativo vai de 1,00 a 1,27, ou "
    "seja, até cerca de 27% a mais. ")
substituir(4, "explicacao", "Quem ajuda a marcar sinapses para remoção é o sistema "
    "complemento,", "Em camundongos, quem ajuda a marcar sinapses para remoção é o sistema complemento,")
substituir(4, "explicacao", "de células. Em camundongos, a proteína C3 marca sinapses,", "de células: a proteína C3 marca sinapses,")
acrescentar_trecho(4, 0, "these alleles showed relative risks ranging from 1.00 to 1.27")

# 0005: a cultura, não necessariamente as mesmas células; "a maioria" das células de câncer
trocar(5, gancho="Um Nobel manteve viva por mais de 20 anos uma cultura de células de coração de embrião de galinha, e a "
                 "ciência passou a crer que células eram imortais. Em 1961, Hayflick mostrou que não: as normais param de se dividir.")
substituir(5, "explicacao", "As células de câncer escapam "
    "graças à enzima telomerase", "A maioria das células de câncer escapa graças à enzima telomerase")

# 0006: indícios em chimpanzés e gorilas, ainda discutidos
substituir(6, "explicacao", "e estudos recentes acharam menopausa "
    "também em chimpanzés e gorilas selvagens de Uganda.",
    "e estudos recentes acharam indícios de menopausa também em chimpanzés e gorilas selvagens de Uganda, "
    "embora isso ainda seja discutido.")

# 0007: mais de 60 bebês, dedo ou bastão fino, só duas exceções; fonte primária
trocar(7, gancho="Num artigo de 1891, um médico darwinista contou ter pendurado mais de 60 bebês com menos de um mês num "
                 "dedo ou num bastão fino: só dois não aguentaram o próprio peso por 10 segundos, e um ficou 2 min 35 s.")
substituir(7, "explicacao", "O que ele explorava",
    "Em pelo menos metade dos casos, o teste foi feito na primeira hora de vida. O que ele explorava")
substituir(7, "explicacao", "Um feto já o mostra por volta de 28 semanas de gestação,",
    "Um feto já o mostra até a 28ª semana de gestação (às vezes já na 16ª),")
substituir(7, "explicacao", "Ele é comandado pela medula "
    "espinhal e aparece até em bebês sem a maior parte do cérebro. ", "Ele depende da medula espinhal. ")
CANDIDATOS[6]["fontes"].insert(0, {
    "url": "https://en.wikisource.org/wiki/Popular_Science_Monthly/Volume_40/March_1892/Darwinism_in_the_Nursery",
    "titulo": "Darwinism in the Nursery (Louis Robinson; Popular Science Monthly, vol. 40, março de 1892), no Wikisource",
    "idioma": "en",
    "trecho": "I have now records of upward of sixty cases in which the children were under a month old, and in at least half of these the experiment was tried within an hour of birth. [...] "
              "In every instance, with only two exceptions, the child was able to hang on to the finger or a small stick three quarters of an inch in diameter by its hands, like an acrobat from a horizontal bar, and sustain the whole weight of its body for at least ten seconds. [...] "
              "and one infant of three weeks old for two minutes thirty-five seconds!"})

# 0009: o levantamento nacional, sem atribuir à polícia
substituir(9, "explicacao",
    "A busca que se seguiu mostrou que a polícia não sabia se 234.354 "
    "pessoas com mais de 100 anos estavam vivas.",
    "Um levantamento nacional que se seguiu mostrou que as autoridades não sabiam se 234.354 pessoas com "
    "mais de 100 anos ainda estavam vivas; mais de 77 mil delas teriam passado dos 120 anos.")
acrescentar_trecho(9, 0, "prompted a nationwide investigation, which concluded that police did not know if 234,354 people older than 100 were still alive. "
    "More than 77,000 of these people, officials said, would have been older than 120 years old if they were still alive.")

# 0010 (aprovado): troca opcional
substituir(10, "gancho", "Há pessoas com mais de 80 anos", "Há pessoas de 80 anos ou mais")

# 0012: só a National Autistic Society se manifestou
substituir(12, "explicacao", "e entidades ligadas ao autismo protestaram.",
    "e a National Autistic Society, entidade britânica ligada ao autismo, se disse extremamente preocupada "
    "com os efeitos sobre pessoas autistas.")

# 0015: limites do uso forense; segunda fonte
substituir(15, "gancho", "Peritos a usam para saber se um bebê nasceu vivo e quanto viveu.",
    "Peritos a usam para indicar se um bebê nasceu vivo e quanto viveu.")
substituir(15, "explicacao", "dá para estimar por quanto tempo o bebê sobreviveu.",
    "dá para estimar por quanto tempo o bebê sobreviveu. Há limites: o bebê precisa ter sobrevivido pelo "
    "menos alguns dias para a linha aparecer, e a ausência dela não prova que ele nasceu morto.")
CANDIDATOS[14]["fontes"].append({
    "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3190441/fullTextXML",
    "titulo": "Neonatal line as a linear evidence of live birth: estimation of postnatal survival of a new born from primary tooth germs (Janardhanan et al., J Forensic Dent Sci, 2011)",
    "idioma": "en",
    "trecho": "The presence of neonatal line indicates live birth and it is possible to estimate the exact period of survival of the infant in days by measuring the amount of postnatal hard tissue formation [...] "
              "The main limitation of using neonatal line for the assessment of postnatal survival of infants is that most of the infanticides occur immediately after birth, but a couple of days of survival are necessary before the neonatal lines could be detected. [...] "
              "the absence of this line is not an indication of still birth."})

# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---
substituir(7, "explicacao", "Ele depende da medula espinhal.", "Ele parece ser comandado pela medula espinhal, já que aparece até em bebês anencéfalos.")
substituir(12, "explicacao", "uma frequência de 8 kHz, que quase todos escutam", "uma frequência de 8 kHz, que a maioria das pessoas escuta")
substituir(12, "explicacao", "se disse extremamente preocupada com os efeitos sobre pessoas autistas", "se disse extremamente preocupada com possíveis efeitos nocivos sobre pessoas autistas")
