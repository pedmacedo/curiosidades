# Progresso

> Estado atual do projeto. Atualize ao fim de cada sessão de trabalho. A referência permanente é o `CLAUDE.md`.

**Última atualização:** 2026-11-17
**Fase atual:** 3 (app MVP): app publicado em https://pedmacedo.github.io/curiosidades/; **falta o Pedro testar no celular**.

## Fases

| Fase | Situação |
|---|---|
| 0. Fundação | ✅ Concluída em 2026-11-17 |
| 1. Taxonomia | ✅ Aprovada pelo Pedro em 2026-11-17 (16 áreas, 161 temas; tipos de espanto da lista fixa) |
| 2. Piloto de conteúdo | ✅ Concluída em 2026-11-17 (Pedro revisou os 40: 39 ok, 1 chato; 39 fatos aprovados) |
| 3. App MVP | ⏳ App feito e testado no navegador (inclusive offline); falta publicar e abrir no celular |
| 4. Produção | — |
| 5. Polimento | — |

## Fase 2: piloto (2026-11-17)

Temas escolhidos, de áreas bem diferentes: **Microbiologia** (Biologia), **Amazônia** (Brasil) e **Palavras viajantes** (Línguas e palavras).

| Tema | Candidatos | 1ª rodada (aprovado / ajustar / reprovado) | Aprovados no fim | Descartados |
|---|---|---|---|---|
| Microbiologia | 16 | 8 / 8 / 0 | 16 | 0 |
| Amazônia | 14 | 4 / 7 / 3 | 11 | 3 (pororoca, ponte, Encontro das Águas) |
| Palavras viajantes | 15 | 6 / 7 / 2 | 13 | 2 (açúcar, jaguar) |
| **Total** | **45** | **18 / 22 / 5** | **40** | **5 (11%)** |
| Depois da revisão do Pedro | | | **39** | **6 (13%)** |

- Só 40% dos candidatos passaram de primeira. Quase metade precisou de correção, e todos os corrigidos foram aprovados na 2ª rodada (6 deles com ajuste pontual).
- O descarte final (11%) ficou abaixo dos 30–40% que o CLAUDE.md considera normal. Pode ser bom sinal (candidatos escolhidos com cuidado) ou sinal de que a correção está "salvando" fatos que deviam cair. **A revisão do Pedro decide.** Se ele marcar vários corrigidos como "errado" ou "chato", a regra passa a ser descartar mais e corrigir menos.
- Nota média dos aprovados: 4,1 (Microbiologia), 3,7 (Amazônia) e 3,5 (Palavras viajantes). A régua derrubou sobretudo fatos conhecidos demais para um brasileiro.

### O que o piloto ensinou (e o que mudou no processo)

1. **O maior risco não é o trecho, é a explicação.** Todos os trechos passaram no `checar_citacoes.py`, mas na 1ª rodada o verificador pediu ajuste em cerca de metade dos fatos, quase sempre por frases da explicação sem apoio na fonte (detalhes "de enfeite", causalidade inventada, generalização). **Regra nova:** toda frase da explicação precisa de um trecho que a sustente; se não houver, a frase sai. O lote da Amazônia foi reescrito com essa regra antes da verificação.
2. **A Wikipedia às vezes erra ou simplifica números.** Exemplos reais do piloto: "99,1% das amostras" (o artigo diz 39,6–99,1% da comunidade); "13–48% do oxigênio do mundo" (era só no Pacífico equatorial); poeira do Saara com "22 milhões de t de fósforo" (são 22 mil t); temperaturas do Encontro das Águas (número de turismo). **Regra nova:** para números de destaque, preferir a fonte primária (artigo, comunicado institucional) à Wikipedia.
3. **A Wikipedia se contradiz entre seções.** O artigo "Robot" diz no topo que Karel Čapek criou a palavra e, mais abaixo, que foi o irmão dele. O verificador lê o contexto todo e pegou isso.
4. **Fatos famosos no Brasil são reprovados pela régua.** Pororoca, Encontro das Águas e "não há ponte no Amazonas" caíram como `pouco_interessante`. Para temas brasileiros, o que um brasileiro curioso já sabe conta como trivia.
5. **2ª rodada com ajuste pontual.** Na rodada final, o verificador só pede `ajustar` para trocas pequenas e exatas (ex.: "rios" → "lagos"), que são aplicadas sem uma 3ª verificação e registradas com `"ajuste_pontual": true`. Problema maior → reprovado. (Instrução acrescentada em `.claude/agents/verificador.md`.)
6. **Ajustes no código:** `checar_citacoes.py` aceita pedaços exatos citados fora da ordem da página (antes caía em "aproximado"), tenta de novo quando recebe HTTP 429 e usa a página renderizada da Wikipedia se o extrato falhar. `validar.py` mede o limite de 400 caracteres por pedaço citado, não pelo trecho inteiro.
7. **Ferramentas novas no pipeline:** `montar_lote.py` (monta o lote a partir de `dados/candidatos/<lote>.py`, numera ids continuando os do tema e confere os trechos antes de gravar), `aplicar_vereditos.py` (passo 6: aprovados → `fatos/`, reprovados → `descartados/`, a partir de `<lote>.vereditos.json`) e `estatisticas.py`.
8. **Revisão do Pedro (39 ok, 0 errado, 1 chato).** O único "chato" foi a vitória-régia que inspirou o Palácio de Cristal: *"nunca ouvi falar do palácio"*. **Regra nova na régua do verificador:** uma conexão só espanta se as duas pontas forem conhecidas do leitor brasileiro (ou se o gancho explicar a ponta desconhecida). O fato foi para `descartados/` com `sortear_amostra.py --apurar ... --descartar`, opção nova que move os marcados como errado/chato e guarda o comentário em `revisao_humana`.

### Fluxo de um lote (como ficou)

1. Escrever `dados/candidatos/<lote>.py` (~15 candidatos), baixando fontes com `checar_citacoes.py --baixar URL` e copiando trechos literais do cache.
2. `python pipeline/montar_lote.py dados/candidatos/<lote>.py` → corrigir até não sobrar pendência.
3. `python pipeline/checar_citacoes.py dados/lotes/<lote>.jsonl` e `python pipeline/validar.py dados/lotes/<lote>.jsonl`.
4. Subagente `verificador` (em paralelo, ~7 fatos por chamada). Registrar a rodada em `dados/lotes/<lote>.vereditos.json`.
5. Ajustes em `dados/candidatos/<lote>-r2.py` (importa o da rodada 1 e troca só o necessário) → montar, checar e 2ª rodada.
6. `python pipeline/aplicar_vereditos.py dados/lotes/<lote>.jsonl` → `python pipeline/validar.py` → `python pipeline/estatisticas.py --markdown`.
7. `python pipeline/construir_dados_app.py` para levar os fatos novos ao app.
8. A cada ~150 aprovados: `sortear_amostra.py --n 30`; depois da marcação do Pedro, `sortear_amostra.py --apurar <arquivo> --descartar`.

## Fase 3: app MVP (2026-11-17)

Arquivos em `app/` (HTML/CSS/JS puro, ES modules, sem dependências):

- `index.html`, `estilo.css`: mobile-first, fonte grande, tema claro e escuro automático (segue o celular), reações grandes perto do polegar, abas embaixo.
- `app.js`: telas de perfis, questionário (etapa 1: as 16 áreas com Adoro/Tanto faz/Não curto; etapa 2: 15 ganchos com reações, com opção de pular), feed, favoritos e "Meu perfil" (temas preferidos com barras, tipos de curiosidade preferidos, lista de "parece errado" que pode ser copiada, refazer questionário, exportar/importar perfil, trocar e apagar perfil).
- `recomendador.js`: exatamente o §6.2 (Beta por tema e por tipo de espanto, prioris do questionário, pesos 1/0,5/0,25, 15% de exploração, Thompson sampling, diversidade, semente injetável).
- `armazenamento.js`: `localStorage` com `try/catch`; se o navegador não guardar, o app funciona só na memória e mostra um aviso.
- `sw.js` + `manifest.json` + `icones/`: instalável e offline. O nome do cache leva a versão dos dados e a versão do código do app, as duas geradas em `app/data/versao.js`.
- `pipeline/construir_dados_app.py`: roda o `validar.py` e gera `app/data/` (fatos só com os campos do app, sem os trechos das fontes; taxonomia sem descrições; tipos; versões).

Decisões tomadas na implementação (dá para mudar):
- O perfil guarda só o **histórico** (fato, reação, origem). O estado do recomendador é recalculado a partir dele a cada abertura. Assim "Refazer questionário" troca as prioris e mantém tudo o que foi aprendido com as reações.
- Os 15 ganchos do questionário **não** contam como vistos: com só 39 fatos, eles voltam no feed com a explicação. Quando o acervo for grande, vale rever.
- A amostra do questionário é escolhida para cobrir o máximo de áreas e tipos de espanto (hoje, 5 de cada tema do piloto).
- Em `localhost`, o service worker busca primeiro na rede (para ver mudanças na hora). Publicado, busca primeiro no cache.

Ajustes pedidos pelo Pedro depois do primeiro teste (2026-11-17):
- Explicação com texto **justificado** (com hifenização em português, que funciona no celular).
- Reação **"Já sabia" retirada**: o que importa é a reação ao conteúdo. O `CLAUDE.md` (§6.1 e §6.2) foi atualizado. Históricos antigos com "Já sabia" continuam sendo lidos.

**Publicação:** repositório https://github.com/pedmacedo/curiosidades (público), app em **https://pedmacedo.github.io/curiosidades/**. Primeiro envio em 2026-11-17. O remoto usa `https://pedmacedo@github.com/...` porque o Windows tem salvo o login de outra conta (macedoped). O `.github/workflows/publicar.yml` roda os testes, gera `app/data/` e publica a pasta `app/` no GitHub Pages a cada envio. O `.gitignore` deixa de fora `dados/cache_fontes/` (texto completo de páginas de terceiros, que não deve ser republicado e é refeito com `--baixar`) e os arquivos gerados em `app/data/`.

Testado no navegador (tela de celular 375×812, claro e escuro): criar perfil, as duas etapas do questionário, explicação, salvar, "parece errado", os 39 fatos do feed sem repetir e sem 3 da mesma área seguidos, tela de fim, perfil, favoritos, refazer questionário e **funcionamento com o servidor desligado**.

## Como rodar

```
pip install -r requirements.txt
python -m unittest discover -s testes
node --test testes/recomendador.test.mjs
python pipeline/validar.py
python pipeline/estatisticas.py
python pipeline/construir_dados_app.py      # gera app/data/ (rode depois de aprovar fatos ou mudar o app)
python pipeline/servir_app.py              # abre o app em http://localhost:8765 (ou dois cliques em abrir_app.bat)
```

O app não abre com dois cliques no `index.html`: o navegador bloqueia módulos JavaScript em `file://`, e a página mostra um aviso com o caminho certo. O `servir_app.py` funciona de qualquer pasta, força os tipos certos para `.js`/`.json` (o registro do Windows às vezes diz que `.js` é texto puro) e confere se a porta já tem outro programa atendendo, por IPv4 e por IPv6. Se tiver, usa a próxima livre; se for o próprio app, só abre o navegador. (Um `python -m http.server` antigo escutando no IPv6 da mesma porta fazia o navegador cair num 404.)

Opcional: a variável de ambiente `CURIOSIDADES_CONTATO` acrescenta um contato ao User-Agent dos downloads (a Wikipedia recomenda). Sem ela, vai só o nome do app.

## Fase 0: o que foi feito

- Estrutura de pastas do §3 (`dados/`, `pipeline/`, `app/`, `testes/`, `.claude/agents/`), mais `dados/candidatos/` (fonte dos lotes, criada na Fase 2).
- `dados/tipos_espanto.json` com a lista fixa do §4.2.
- `pipeline/comum.py`, `validar.py`, `checar_citacoes.py`, `sortear_amostra.py` e o subagente `verificador`.
- Listas de equívocos populares da Wikipedia em inglês no cache (a página virou um índice de três listas: artes e cultura; história; ciência, tecnologia e matemática).
- Testes em `testes/` (unittest, sem internet; o download é testado com um servidor HTTP local).

## Fase 1: taxonomia

- `dados/taxonomia.json`: 16 áreas e 161 temas (10 por área; História antiga e medieval tem 11), cada tema com 2 a 5 vizinhos de outras áreas, e todo tema alcançável por algum vizinho. Resumo em `dados/revisao/taxonomia-proposta.md`.
- Encaixes: Paleontologia em *Terra*; Neurociência em *Mente*; Comida brasileira em *Comida*; Mitologia em *Artes*; Teoria dos jogos e Algoritmos em *Matemática*.

## Decisões e observações

- Motivos de descarte padrão: os do §4.3 mais `exagero` e `reprovado_verificador`. Motivos fora da lista geram aviso.
- Em lotes (candidatos), explicação fora de 80–250 palavras e nota < 3 são só aviso; nos aprovados, são erro.
- `checar_citacoes.py` sai com código 1 quando algum fato fica sem fonte confirmada.
- Número escrito por extenso na fonte gera `aviso_numero`; o aviso não reprova, o verificador decide.
- Sites que bloquearam o download no piloto: phys.org e pnas.org (HTTP 403). Nature, NASA, PMC, Frontiers, NBC e IMechE funcionaram.

## Próximos passos

1. **Fase 3:** o Pedro instalar o app no celular a partir de https://pedmacedo.github.io/curiosidades/ e testar, inclusive em modo avião.
2. **Fase 4:** produção de lotes, seguindo o fluxo acima, com a régua nova (pontas conhecidas).

## Estatísticas de conteúdo

Gerado por `python pipeline/estatisticas.py --markdown`:

| Lote | Tema | Candidatos | Aprovados | Descartados | Descarte | Rodada 1 (apr/ajus/repr) | Motivos | Nota média |
|---|---|---|---|---|---|---|---|---|
| 2026-11-17-amazonia-01 | amazonia | 14 | 10 | 4 | 29% | 4/7/3 | pouco_interessante 3, numero_divergente 1 | 3.7 |
| 2026-11-17-microbiologia-01 | microbiologia | 16 | 16 | 0 | 0% | 8/8/0 | — | 4.1 |
| 2026-11-17-palavras_viajantes-01 | palavras_viajantes | 15 | 13 | 2 | 13% | 6/7/2 | pouco_interessante 1, exagero 1 | 3.5 |
| **Total** | | 45 | 39 | 6 | 13% | | | |

Cobertura: 3 de 161 temas com pelo menos um fato aprovado.

## Revisões humanas

| Arquivo | Fatos | ok | errado | chato | Veredito |
|---|---|---|---|---|---|
| piloto-2026-11-17.md | 40 | 39 | 0 | 1 (amazonia-0013, Palácio de Cristal) | 1 problema → segue; fato descartado |
