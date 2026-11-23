# Instruções para o subagente produtor de um lote (Fase 4)

Projeto: D:\Usuarios\03172817121\Desktop\CLAUDE\curiosidades. Leia antes o CLAUDE.md inteiro (§2, §4 e §5 são essenciais).
Todo o texto dos fatos é em português do Brasil. Suas mensagens também.

## O seu papel
Você é o PRODUTOR de UM lote (um tema). Você escreve os candidatos, baixa as fontes, monta e checa o lote.
Você NÃO verifica (o verificador independente é chamado pelo orquestrador) e NÃO aplica vereditos.
NÃO edite dados/fatos, dados/descartados, PROGRESSO.md, CLAUDE.md, app/ nem arquivos de outros lotes.
Só crie/edite: dados/candidatos/<LOTE>.py e <LOTE>-r2.py (e o que montar_lote/checar gerarem para o SEU lote).
Não faça commit nem push.

## Passos da rodada 1
1. Leia dados/taxonomia.json (o tema, a descrição e os vizinhos) e os ganchos já aprovados de dados/fatos/*.jsonl
   (grep pelo assunto) para não repetir fatos.
2. Pesquise e escolha ~12 candidatos fortes (a régua do §4.4: espanto real, com mecanismo/história; nada de trivia de
   almanaque nem "lista da internet"). Varie os tipos de espanto. Prefira Wikipedia em inglês (API em texto puro, via
   o helper `wiki()`), fontes institucionais ou artigos (Europe PMC: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC<id>/fullTextXML;
   o NCBI PMC mostra captcha).
3. Baixe as fontes para o cache e leia o texto antes de escrever:
   - baixar: `python pipeline/baixar_fontes.py "<url1>" "<url2>"`
     (sempre com aspas; URLs com parênteses quebram o bash sem aspas)
   - ler: `python pipeline/ver_fonte.py <parte do nome do arquivo em cache> <palavra1> <palavra2> --largura 400 --max 6`
     (todas as palavras são posicionais; nenhuma pode começar com "-")
   - ou leia direto os arquivos dados/cache_fontes/*__extrato.txt
4. Escreva dados/candidatos/<LOTE>.py seguindo EXATAMENTE o formato de dados/candidatos/2026-11-18-infinito-01.py
   (LOTE, AREA, TEMA, W, wiki(), CANDIDATOS com temas_secundarios, tipos_espanto, gancho, explicacao, nivel,
   nota_surpresa, confianca, fontes, e um comentário "# N título curto" antes de cada um).
   O LOTE é "<data de hoje>-<tema>-01" (o orquestrador informa o nome exato).
5. Rode, nesta ordem (no diretório do projeto):
   - `python pipeline/montar_lote.py dados/candidatos/<LOTE>.py --online`
   - `python pipeline/checar_citacoes.py dados/lotes/<LOTE>.jsonl`
   - `python pipeline/validar.py dados/lotes/<LOTE>.jsonl`
   Corrija até todos os trechos darem "ok" (não "aproximado" nem "falhou") e o validar passar.
   Diagnóstico de trecho que falhou: `python pipeline/diagnosticar_trecho.py` (veja o --help) ou, em Python,
   `from checar_citacoes import normalizar, fragmentos` e teste cada fragmento contra o cache normalizado. Quase sempre é
   um pedaço que atravessa um título de seção: quebre com " [...] ".

## Regras de escrita (as que mais reprovam)
- gancho ≤ 220 caracteres, autoexplicativo; explicação de 80 a 250 palavras.
- TODA frase do gancho e da explicação precisa estar sustentada por algum trecho. Todo número também.
  Nada de "fato de memória" sem trecho: se não achou na fonte, corte a frase.
- Texto próprio: não traduza a fonte frase a frase; reescreva com outras palavras e outra ordem.
- Sem exagero nem generalização: "um dos primeiros" ≠ "o primeiro"; "segundo X" quando a fonte atribui.
- Cuidado com frases de dois sujeitos: de quem é a data/número?
- Wikipedia às vezes se contradiz entre seções (datas, números): se o artigo der dois valores, evite o número ou
  use o que tem referência e cite os dois.
- `misterio_aberto` só para o que ainda não tem resposta; `mito_desmentido` só quando o fato desmente uma crença
  popular de verdade (não para hipótese científica refutada).
- confianca "hipotese" só com misterio_aberto e o gancho deixando claro.
- Nunca use hacks como `if False:` nos arquivos.
- `aprofundar` é opcional; só com URL que você abriu de fato. Nunca invente link de vídeo.

## Ao terminar a rodada 1
Responda ao orquestrador, em português, com: o caminho do lote (dados/lotes/<LOTE>.jsonl), a lista de ids com um
título curto de cada um, e qualquer observação (fonte fraca, dúvida). Não chame o verificador.

## Rodada 2 (quando o orquestrador mandar os vereditos)
Escreva dados/candidatos/<LOTE>-r2.py no formato de dados/candidatos/2026-11-18-ia_robotica-01-r2.py (importa o r1 e
usa trocar/substituir/substituir_trecho/acrescentar_trecho). Aplique as correções pedidas (fatos "reprovado" ficam
como estão: o orquestrador descarta). Rode montar (com --online se houver fonte nova), checar e validar no lote até
ficar tudo ok, e responda com a lista de ids que mudaram e um resumo de cada correção.
Se depois o orquestrador pedir ajustes pontuais, acrescente-os no fim do r2 sob o comentário
"# --- ajustes pontuais da rodada 2 (aplicados sem 3ª verificação) ---", rode montar/checar/validar e confirme
que o validar do lote passou e que nenhum gancho passou de 220 caracteres.

## Lições das primeiras rodadas em paralelo (leia!)
- Outros produtores trabalham AO MESMO TEMPO em outros temas (o orquestrador diz quais). Evite assuntos que caibam
  melhor no tema de outro produtor: na 1ª leva, "lei para inglês ver" saiu duplicada em dois lotes e um foi descartado.
- O verificador derruba sobretudo: (1) frases da fonte com sentido absoluto onde ela diz "may", "probably", "estimated",
  "last known", "one version"; (2) "o primeiro" quando há precedente; (3) números da Wikipedia que a fonte primária não
  confirma (prefira a fonte primária quando o fato depende de uma conta ou citação); (4) frases quase copiadas da fonte;
  (5) quem fez o quê em frases com dois sujeitos; (6) desmentidos conhecidos demais (pirâmides sem escravos, olho-de-boi).
- Da 2ª leva: (7) ano de publicação ≠ ano do experimento (diga "estudo publicado em X" ou dê o ano do experimento);
  (8) contas que a própria Wikipedia faz a partir de um dado não são "do instituto X"; (9) em psicologia e saúde,
  procure replicações e críticas antes de escrever, e use consenso_parcial quando houver debate; (10) "relatos
  tradicionais" e anedotas que só circulam em divulgação ficam marcados como tal ("segundo relatos"); (11) tempo
  verbal: não descreva no presente o que a fonte só registra até uma data antiga.
- Arquivos temporários: use nomes com o seu tema (ex.: `tmp_<tema>_1.txt`) — outros produtores usam a mesma pasta.
- Assuntos já usados em outros temas (confira sempre com grep em dados/fatos/*.jsonl): o Gimli Glider e o Comet saíram
  em transportes; o calendário republicano francês, a hora decimal, o metro de Méchain e a origem do 8 de março saíram
  em revolucoes_politicas; "o chá preto não é fermentado" já saiu em fermentação. Tacoma Narrows e Vajont ficam para
  falhas_engenharia (o navio Vasa também).
- Já usados em psicologia_social (evite em experimentos_psicologia): Asch, Milgram, Robbers Cave, Prisão de Stanford,
  Hawthorne, as baratas de Zajonc, When Prophecy Fails, o mundo pequeno de Milgram, Kitty Genovese, Dunbar, grupos mínimos
  de Tajfel, a epidemia de dança de 1518 e o "pânico" nas multidões.
