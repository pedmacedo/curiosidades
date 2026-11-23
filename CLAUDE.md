# Projeto: Curiosidades sob medida

App pessoal (uso do Pedro e da família) que descobre os gostos de cada pessoa por um questionário curto e, a partir daí, oferece curiosidades verificadas que combinam com ela. O app também abre espaço para descobertas fora da zona de conforto.

> Este arquivo é a referência permanente do projeto. O andamento fica em `PROGRESSO.md`, que deve ser atualizado ao fim de cada sessão de trabalho.

---

## 1. Decisões já tomadas

| Tema | Decisão |
|---|---|
| Plataforma | Web app / PWA, mobile-first, que funciona offline e pode ser "instalado" no celular |
| Público | Só o Pedro e a família. Sem login e sem servidor: o perfil fica no próprio aparelho |
| Hospedagem | Site estático (GitHub Pages ou similar). Sem backend |
| LLM depois de pronto | **Nenhum.** O app roda 100% sem LLM |
| Geração e verificação dos fatos | Feitas **pelo próprio Claude Code**, em lotes, usando busca e leitura na web. Sem chave de API |
| Escala da 1ª versão | **~1.500 fatos** cobrindo **todas as áreas** (~150 temas × ~10 fatos) |
| Idioma | Conteúdo em português do Brasil. As fontes podem estar em qualquer idioma |
| Stack | Pipeline em Python 3.11+ (stdlib + `requests` + `beautifulsoup4`). App em HTML/CSS/JS puro com ES modules, sem framework e sem build |

Se alguma decisão precisar mudar, pergunte ao Pedro antes.

---

## 2. Princípios

1. **O LLM fica na fábrica, não na loja.** A IA produz e verifica o acervo. O app só lê arquivos JSON.
2. **Na dúvida, descarte.** Há fatos de sobra no mundo, e descartar 30–40% dos candidatos é normal e saudável.
3. **Toda afirmação tem fonte e trecho literal**, conferido por código, não por "confiança" do modelo.
4. **Interessante de verdade.** O alvo é o espanto que leva a pessoa a pesquisar mais, não trivia de almanaque (ver §4).
5. **Serendipidade é recurso, não acidente.** O recomendador reserva espaço para temas vizinhos e distantes.
6. **Texto próprio.** Ganchos e explicações são escritos com palavras próprias. Só o campo `trecho` copia a fonte.

---

## 3. Estrutura de pastas

```
curiosidades/
  CLAUDE.md                  # este arquivo
  PROGRESSO.md               # estado atual, próximos lotes, estatísticas
  dados/
    taxonomia.json           # áreas → temas, com vizinhos
    tipos_espanto.json       # lista fixa de "tipos de curiosidade"
    fatos/<area>.jsonl       # fatos APROVADOS (um JSON por linha)
    descartados/<area>.jsonl # candidatos reprovados + motivo (para estatística)
    lotes/<lote>.jsonl       # candidatos em trabalho (área temporária)
    revisao/<lote>.md        # amostras sorteadas para revisão humana
    cache_fontes/            # texto baixado das fontes (gerado pelo script)
  pipeline/
    validar.py               # esquema, limites, ids únicos, duplicatas
    checar_citacoes.py       # baixa cada URL e confere o trecho literal
    sortear_amostra.py       # sorteia N fatos aprovados → revisao/<lote>.md
    estatisticas.py          # taxa de descarte, cobertura por tema etc.
    construir_dados_app.py   # gera app/data/*.json a partir de dados/
  .claude/agents/
    verificador.md           # subagente cético (ver §5.3)
  app/
    index.html  estilo.css  app.js  recomendador.js  armazenamento.js
    sw.js  manifest.json
    data/ (gerado)
  testes/
```

---

## 4. Conteúdo

### 4.1 Taxonomia (dois níveis + vizinhança)

- ~15 **áreas** → ~150 **temas** (cerca de 10 por área).
- Cada tema tem `vizinhos`: 2 a 5 temas de **outras** áreas com afinidade real (ex.: `microbiologia` ↔ `geologia` ↔ `astrobiologia`). É por essas pontes que o recomendador explora.
- Ponto de partida para as áreas (o Pedro aprova a versão final): Biologia · Corpo humano e medicina · Terra, clima e geologia · Espaço e astronomia · Física e química · Matemática e lógica · Tecnologia e engenharia · História antiga e medieval · História moderna e contemporânea · Brasil · Línguas e palavras · Artes, música e literatura · Sociedade, costumes e economia · Comida e bebida · Mente e comportamento · Esportes e jogos.

Formato de `taxonomia.json`:
```json
{
  "areas": [
    {"id": "biologia", "nome": "Biologia", "temas": [
      {"id": "microbiologia", "nome": "Microbiologia",
       "descricao": "Bactérias, arqueias, vírus e a vida microscópica",
       "vizinhos": ["geologia_profunda", "astrobiologia", "doencas_infecciosas"]}
    ]}
  ]
}
```
Os IDs de tema são únicos no projeto inteiro, em `snake_case` e sem acentos.

### 4.2 Tipos de espanto (lista fixa)

`escala_absurda` (tamanhos, tempos, números extremos) · `contraintuitivo` · `origem_inesperada` (de onde vem uma palavra, costume ou objeto) · `conexao_inesperada` (dois mundos que se ligam) · `mito_desmentido` · `misterio_aberto` (ainda sem resposta) · `engenhosidade` (soluções brilhantes da natureza ou de humanos) · `historia_humana` (episódio real com personagens).

Cada fato tem de 1 a 3 tipos.

### 4.3 Ficha do fato (`dados/fatos/<area>.jsonl`)

```json
{
  "id": "microbiologia-0007",
  "area": "biologia",
  "tema": "microbiologia",
  "temas_secundarios": ["geologia_profunda", "astrobiologia"],
  "tipos_espanto": ["escala_absurda", "contraintuitivo"],
  "gancho": "Há microrganismos vivendo em rochas a quilômetros de profundidade, com metabolismo tão lento que podem levar séculos para se dividir.",
  "explicacao": "Texto próprio, 80–250 palavras, explicando o porquê/como.",
  "nivel": 1,
  "nota_surpresa": 4,
  "confianca": "alta",
  "fontes": [
    {"url": "https://...", "titulo": "...", "idioma": "en",
     "trecho": "trecho LITERAL da fonte que sustenta o fato",
     "acessado_em": "2026-11-17"}
  ],
  "aprofundar": [
    {"tipo": "video|artigo|livro|podcast", "titulo": "...", "url": "https://..."}
  ],
  "lote": "2026-11-17-biologia-01",
  "verificado_em": "2026-11-17"
}
```

Regras:
- `gancho` ≤ 220 caracteres, autoexplicativo, sem clickbait vazio ("Você não vai acreditar…").
- `nivel`: 1 = qualquer adulto entende; 2 = exige atenção; 3 = exige alguma base.
- `nota_surpresa` vai de 1 a 5. Só entram fatos com nota ≥ 3 depois da verificação.
- `confianca`: `alta` (consenso bem estabelecido), `consenso_parcial` (aceito, mas com debate), `hipotese` (proposta séria ainda não confirmada; só com o tipo `misterio_aberto` e o gancho deixando isso claro).
- Pelo menos **uma** fonte precisa passar no `checar_citacoes.py`.
- Todo **número** do gancho e da explicação precisa estar sustentado pelo trecho de alguma fonte.
- `aprofundar` é opcional. Só entra URL que foi realmente aberta e cujo título confere. **Nunca invente link de vídeo.**

Os descartados usam a mesma ficha, mais `motivo_descarte` (por exemplo `citacao_nao_encontrada`, `mito`, `fonte_fraca`, `pouco_interessante`, `numero_divergente`, `duplicado`).

### 4.4 Régua de "interessante"

Rejeite um fato se ele:
- é trivia de almanaque que um adulto curioso provavelmente já ouviu (exemplo real que motivou esta régua: *"a caixa-preta dos aviões é laranja"*);
- é só um dado sem mecanismo ("X tem 3 metros");
- depende de uma definição forçada ou de pegadinha de palavras;
- é curiosidade "de lista da internet" que circula sem fonte boa.

Prefira fatos que:
- mudam como a pessoa enxerga algo (ex.: a **biosfera profunda**, vida microbiana abundante quilômetros abaixo da superfície);
- têm um "por quê" ou "como" que vale a explicação;
- puxam vontade de pesquisar mais;
- conectam áreas diferentes (esses são as melhores pontes).

---

## 5. Pipeline de produção (executado pelo Claude Code)

### 5.1 Um lote = um tema

1. Ler `taxonomia.json`, a régua (§4.4) e os fatos já aprovados do tema e dos vizinhos, para não repetir.
2. Gerar **~15 candidatos** para chegar a **~10 aprovados**, variando os tipos de espanto.
3. Para cada candidato, buscar na web uma fonte confiável e copiar o **trecho literal** que o sustenta.
   - Ordem de preferência: fonte primária ou institucional (universidade, agência científica, museu, artigo científico) → Wikipedia (en/pt) com referências → divulgação científica de boa reputação.
   - Não serve como fonte: sites de "curiosidades", agregadores, fóruns, conteúdo gerado por IA.
4. Gravar os candidatos em `dados/lotes/<lote>.jsonl` e rodar:
   `python pipeline/checar_citacoes.py dados/lotes/<lote>.jsonl`
   Os candidatos sem nenhuma fonte confirmada são descartados (ou ganham outra fonte, numa única nova tentativa).
5. Mandar os sobreviventes ao subagente **verificador** (§5.3).
6. Aplicar os vereditos. Os aprovados vão para `dados/fatos/<area>.jsonl` e os reprovados para `dados/descartados/<area>.jsonl`.
7. Rodar `python pipeline/validar.py` (tem que passar sem erro).
8. Atualizar `PROGRESSO.md`: tema concluído, aprovados/descartados, observações.

### 5.2 `checar_citacoes.py` (verificação por código)

- Baixa cada URL com `requests` (timeout, user-agent identificável). Para Wikipedia, usa a API em texto puro (`action=query&prop=extracts&explaintext=1`). Guarda o texto em `cache_fontes/`.
- Normaliza (minúsculas, espaços, aspas tipográficas, hifenização) e confere se o `trecho` está contido no texto da fonte. Para trechos longos, aceita correspondência aproximada alta (≥ 0,9 via `difflib`) e registra que foi aproximada.
- Extrai os números do gancho e da explicação e avisa quando algum não aparece em nenhum trecho, porque números mudam de formato entre idiomas. O aviso não reprova sozinho: o verificador decide.
- Sai com um relatório por fato: `ok`, `aproximado`, `falhou (motivo)`, `aviso_numero`.
- Site bloqueado ou com paywall conta como falha daquela fonte. É preciso outra fonte.

### 5.3 Subagente `verificador` (cético e independente)

Crie `.claude/agents/verificador.md`. O subagente recebe **apenas** o fato, as fontes e os textos baixados, sem o raciocínio de quem gerou. Ele deve:
- confirmar que as fontes sustentam **exatamente** o que o gancho e a explicação dizem, sem exagero, generalização ou causalidade inventada;
- conferir cada número;
- checar se o fato é um **equívoco popular** conhecido (comparar com a "List of common misconceptions" da Wikipedia em inglês, baixada uma vez para o cache, e fazer busca própria quando houver suspeita);
- buscar ativamente uma contestação ("is it true that…", "myth…") quando o fato parecer bom demais;
- reavaliar `nota_surpresa` pela régua do §4.4;
- devolver JSON: `{"id":..., "veredito": "aprovado|reprovado|ajustar", "motivo": "...", "correcao": "...", "nota_surpresa": n}`.

Um fato com veredito `ajustar` é corrigido uma vez e volta ao verificador. Se não for aprovado na segunda rodada, é descartado.

### 5.4 Revisão humana por amostragem

> **Decisão do Pedro (2026-11-18):** a amostragem periódica foi **dispensada** a partir da Fase 4. O Pedro concordou com quase 100% do conteúdo e considera o pipeline (checagem por código + verificador em duas rodadas) suficiente. As regras abaixo ficam como referência, caso ele peça uma revisão. Os reportes "⚠ Parece errado" do app continuam sendo o canal de correção.

- A cada ~150 fatos aprovados, rodar `python pipeline/sortear_amostra.py --n 30` para gerar `dados/revisao/<lote>.md`, com gancho, explicação, fontes e caixas `[ ] ok [ ] errado [ ] chato`.
- O Pedro marca. Com **0–1** problema, o bloco segue. Com **2 ou mais**, pausar, diagnosticar qual etapa falhou e ajustar o processo antes de continuar.
- Depois de 3 amostras seguidas limpas, a amostra pode cair para 20.

### 5.5 Ritmo

Produzir ~1.500 fatos com verificação na web consome bastante uso da assinatura. Trabalhe em blocos de alguns temas por sessão e deixe sempre o `PROGRESSO.md` pronto para retomar.

---

## 6. O app

### 6.1 Telas

1. **Perfis**: escolher ou criar perfil local (vários membros da família podem usar o mesmo aparelho).
2. **Questionário** (cerca de 3 minutos):
   - Etapa 1: cada área com três opções: *Adoro / Tanto faz / Não curto*.
   - Etapa 2: **15 ganchos de amostra**, escolhidos para cobrir áreas e tipos de espanto variados, com as reações abaixo.
3. **Feed**: um fato por vez. Mostra o gancho, o botão "Ver explicação", as reações, ⭐ salvar, os links de "aprofundar", "⚠ Parece errado" e, discretamente, um selo quando `confianca` ≠ `alta`.
4. **Favoritos**.
   - **Temas** (aba própria, pedida pelo Pedro em 2026-11-23): lista dos temas por área, com busca; tocar num tema mostra todos os fatos dele. Ler por ali não altera o recomendador.
5. **Meu perfil**: visualização simples dos temas preferidos, botões para refazer o questionário e para exportar/importar o perfil (JSON), além da lista de fatos marcados como "parece errado", que pode ser copiada para enviar ao Pedro.

Reações: 🤯 **Uau!** · 🙂 **Legal** · 😐 **Meh**. (A reação "Já sabia" foi retirada em 2026-11-17, por decisão do Pedro: o que importa é a reação ao conteúdo, mesmo que a pessoa já conhecesse o fato.)

### 6.2 Recomendador (`recomendador.js`), ponto de partida a calibrar

- Cada **tema** tem uma distribuição Beta(α, β) com a "probabilidade de Uau".
  - Priori pela etapa 1 do questionário: Adoro → (3, 1); Tanto faz → (1, 1); Não curto → (1, 3).
- Recompensa por reação: Uau = 1,0 · Legal = 0,7 · Meh = 0,0.
- Atualização: `α += r·w`, `β += (1−r)·w`, com peso `w` = 1,0 para o tema do fato, 0,5 para os `temas_secundarios` e 0,25 para os `vizinhos` do tema.
- **Tipos de espanto** têm Beta próprias, atualizadas do mesmo jeito (w = 1,0).
- Escolha do próximo fato:
  - com probabilidade **0,15**, **exploração**: sorteia um tema pouco exibido, de preferência vizinho dos temas favoritos ou de área ainda pouco vista;
  - senão, **Thompson sampling**: amostra θ de cada tema que ainda tem fatos não vistos e escolhe o maior;
  - dentro do tema: `score = média(amostras dos tipos de espanto do fato) + 0,1 × nota_surpresa`, e escolhe o maior entre os não vistos.
- Regras de diversidade: nunca o mesmo tema duas vezes seguidas, nem a mesma área três vezes seguidas.
- Um fato exibido não volta a aparecer.
- Tudo determinístico com semente injetável, para os testes.

### 6.3 Armazenamento e offline

- Perfis, estado do recomendador, histórico, favoritos e reportes ficam em `localStorage` ou IndexedDB, sempre com `try/catch` e degradando com elegância.
- `sw.js` faz cache do app e de `app/data/*.json` para funcionar offline. A versão dos dados vai no nome do cache.
- `construir_dados_app.py` gera `app/data/fatos.json` (apenas campos usados pelo app), `taxonomia.json` e `tipos_espanto.json`.

### 6.4 Visual

Mobile-first, leitura confortável (fonte grande, bom contraste, tema claro e escuro), reações fáceis de tocar com o polegar e sem distrações.

---

## 7. Fases e critérios de pronto

| Fase | Entrega | Pronto quando |
|---|---|---|
| 0. Fundação | Estrutura de pastas, `PROGRESSO.md`, `validar.py`, `checar_citacoes.py`, `sortear_amostra.py`, subagente verificador, testes dos scripts | Scripts passam nos testes, com casos de trecho presente, ausente e aproximado |
| 1. Taxonomia | `taxonomia.json` (~15 áreas, ~150 temas, vizinhos) e `tipos_espanto.json` | **O Pedro aprovou** |
| 2. Piloto de conteúdo | 3 temas de áreas bem diferentes (~30 fatos) pelo pipeline completo | O Pedro revisou **todos** os ~30, as taxas de descarte estão registradas e o processo foi ajustado |
| 3. App MVP | Questionário, feed, reações e recomendador, com os fatos do piloto e fatos de amostra | O app funciona no celular do Pedro, inclusive offline |
| 4. Produção | Lotes até ~1.500 fatos, ~10 por tema | Todos os temas cobertos e `validar.py` limpo (amostragem dispensada pelo Pedro em 2026-11-18) |
| 5. Polimento | Perfis da família, favoritos, exportar/importar, calibragem do recomendador | O Pedro e a família usando no dia a dia |

**Mostre resultados cedo.** Ao fim de cada fase, apresente ao Pedro o que foi feito e o que mudou antes de seguir.

---

## 8. Convenções

- Comentários, mensagens e documentação em **português do Brasil**.
- Scripts com `argparse`, saída legível e código de saída diferente de zero em caso de erro.
- Nada de dependências pesadas. No app, zero dependências externas.
- Nunca editar à mão os arquivos gerados em `app/data/`: regenere pelo script.
- Antes de mudanças grandes de estrutura ou de critério, pergunte ao Pedro.
