// Recomendador (§6.2 do CLAUDE.md): Thompson sampling por tema, com exploração e diversidade.
// Módulo puro: não toca no DOM nem no armazenamento. Todo sorteio passa por um gerador
// com semente (criarRng), para que os testes sejam determinísticos.

// "Já sabia" saiu da tela em 2026-11-17 (decisão do Pedro: vale a reação ao conteúdo, mesmo
// que a pessoa já conhecesse o fato). O valor fica só para ler históricos antigos.
export const RECOMPENSA = { uau: 1.0, legal: 0.7, meh: 0.0, ja_sabia: 0.4 };
export const PRIORI = { adoro: [3, 1], tanto_faz: [1, 1], nao_curto: [1, 3] };
export const PESO = { tema: 1.0, secundario: 0.5, vizinho: 0.25, tipo: 1.0 };
export const PROB_EXPLORACAO = 0.15;
export const PESO_NOTA = 0.1;

// ---------- números aleatórios ----------

/** Gerador mulberry32. `rng.estado` pode ser guardado e usado como semente para continuar. */
export function criarRng(semente) {
  let s = (semente >>> 0) || 0x9e3779b9;
  const rng = {
    get estado() { return s; },
    proximo() {
      s = (s + 0x6d2b79f5) >>> 0;
      let t = s;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    },
  };
  return rng;
}

function normal(rng) {
  let u = 0;
  while (u === 0) u = rng.proximo();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * rng.proximo());
}

function gama(rng, a) {
  // Marsaglia e Tsang; para a < 1, usa o truque de elevar a u^(1/a).
  if (a < 1) {
    let u = 0;
    while (u === 0) u = rng.proximo();
    return gama(rng, a + 1) * Math.pow(u, 1 / a);
  }
  const d = a - 1 / 3;
  const c = 1 / Math.sqrt(9 * d);
  for (;;) {
    let x, v;
    do { x = normal(rng); v = 1 + c * x; } while (v <= 0);
    v = v * v * v;
    const u = rng.proximo();
    if (u < 1 - 0.0331 * x ** 4) return d * v;
    if (Math.log(u) < 0.5 * x * x + d * (1 - v + Math.log(v))) return d * v;
  }
}

export function amostrarBeta(rng, a, b) {
  const x = gama(rng, a);
  const y = gama(rng, b);
  return x / (x + y);
}

export const media = ([a, b]) => a / (a + b);

// ---------- índice do acervo ----------

/** Junta taxonomia e fatos em consultas rápidas. */
export function criarIndice(taxonomia, fatos, tiposEspanto = []) {
  const temas = new Map();   // id → {id, nome, area, vizinhos}
  const areas = new Map();   // id → {id, nome, temas: [ids]}
  for (const area of taxonomia.areas) {
    areas.set(area.id, { id: area.id, nome: area.nome, temas: area.temas.map((t) => t.id) });
    for (const t of area.temas) temas.set(t.id, { id: t.id, nome: t.nome, area: area.id, vizinhos: t.vizinhos || [] });
  }
  const fatoPorId = new Map();
  const fatosPorTema = new Map();
  for (const f of fatos) {
    if (!temas.has(f.tema)) continue;
    fatoPorId.set(f.id, f);
    if (!fatosPorTema.has(f.tema)) fatosPorTema.set(f.tema, []);
    fatosPorTema.get(f.tema).push(f);
  }
  const tipos = tiposEspanto.length ? tiposEspanto.map((t) => t.id) : [...new Set(fatos.flatMap((f) => f.tipos_espanto))];
  return { temas, areas, fatoPorId, fatosPorTema, tipos };
}

// ---------- estado ----------

/**
 * Estado inicial a partir da etapa 1 do questionário.
 * respostasAreas: {areaId: "adoro" | "tanto_faz" | "nao_curto"} (área sem resposta = tanto_faz).
 */
export function estadoInicial(indice, respostasAreas = {}) {
  const temas = {};
  for (const [id, t] of indice.temas) temas[id] = [...(PRIORI[respostasAreas[t.area]] || PRIORI.tanto_faz)];
  const tipos = {};
  for (const id of indice.tipos) tipos[id] = [1, 1];
  return { temas, tipos, vistos: [], exibicoesTema: {}, exibicoesArea: {}, ultimos: [] };
}

function atualizar(par, r, w) {
  par[0] += r * w;
  par[1] += (1 - r) * w;
}

/** Aplica a reação a um fato. Altera e devolve `estado`. */
export function registrarReacao(estado, indice, fato, reacao) {
  const r = RECOMPENSA[reacao];
  if (r === undefined) throw new Error(`reação desconhecida: ${reacao}`);
  const pesos = new Map();
  const dar = (tema, w) => {
    if (tema === fato.tema || !(tema in estado.temas)) return;
    pesos.set(tema, Math.max(pesos.get(tema) || 0, w));
  };
  for (const t of fato.temas_secundarios || []) dar(t, PESO.secundario);
  for (const t of indice.temas.get(fato.tema)?.vizinhos || []) dar(t, PESO.vizinho);
  if (fato.tema in estado.temas) atualizar(estado.temas[fato.tema], r, PESO.tema);
  for (const [t, w] of pesos) atualizar(estado.temas[t], r, w);
  for (const tipo of fato.tipos_espanto || []) {
    if (!estado.tipos[tipo]) estado.tipos[tipo] = [1, 1];
    atualizar(estado.tipos[tipo], r, PESO.tipo);
  }
  return estado;
}

/** Marca o fato como exibido (não volta a aparecer) e atualiza as contagens de diversidade. */
export function marcarExibido(estado, indice, fato) {
  if (!estado.vistos.includes(fato.id)) estado.vistos.push(fato.id);
  const area = indice.temas.get(fato.tema)?.area;
  estado.exibicoesTema[fato.tema] = (estado.exibicoesTema[fato.tema] || 0) + 1;
  if (area) estado.exibicoesArea[area] = (estado.exibicoesArea[area] || 0) + 1;
  estado.ultimos = [...estado.ultimos, { tema: fato.tema, area }].slice(-2);
  return estado;
}

// ---------- escolha do próximo fato ----------

function naoVistos(estado, indice, tema) {
  const vistos = new Set(estado.vistos);
  return (indice.fatosPorTema.get(tema) || []).filter((f) => !vistos.has(f.id));
}

/** Temas com fatos ainda não vistos, respeitando as regras de diversidade (relaxadas se preciso). */
export function temasElegiveis(estado, indice) {
  const comFatos = [...indice.fatosPorTema.keys()].filter((t) => naoVistos(estado, indice, t).length > 0).sort();
  const [penultimo, ultimo] = estado.ultimos.length === 2 ? estado.ultimos : [null, estado.ultimos[0] || null];
  const areaBloqueada = penultimo && ultimo && penultimo.area === ultimo.area ? ultimo.area : null;
  const semTema = comFatos.filter((t) => !ultimo || t !== ultimo.tema);
  const semArea = semTema.filter((t) => indice.temas.get(t).area !== areaBloqueada);
  if (semArea.length) return semArea;
  if (semTema.length) return semTema;
  return comFatos;
}

/** Temas favoritos: até 3 com média acima de 0,5, do maior para o menor. */
export function temasFavoritos(estado, n = 3) {
  return Object.entries(estado.temas)
    .filter(([, p]) => media(p) > 0.5)
    .sort((x, y) => media(y[1]) - media(x[1]) || (x[0] < y[0] ? -1 : 1))
    .slice(0, n)
    .map(([id]) => id);
}

function escolherExploracao(estado, indice, elegiveis, rng) {
  const vizinhosFav = new Set(temasFavoritos(estado).flatMap((t) => indice.temas.get(t)?.vizinhos || []));
  const areasElegiveis = [...new Set(elegiveis.map((t) => indice.temas.get(t).area))];
  const exibArea = (a) => estado.exibicoesArea[a] || 0;
  const mediaArea = areasElegiveis.reduce((s, a) => s + exibArea(a), 0) / areasElegiveis.length;
  const preferidos = elegiveis.filter((t) => vizinhosFav.has(t) || exibArea(indice.temas.get(t).area) < mediaArea);
  const pool = preferidos.length ? preferidos : elegiveis;
  const menor = Math.min(...pool.map((t) => estado.exibicoesTema[t] || 0));
  const menos = pool.filter((t) => (estado.exibicoesTema[t] || 0) === menor);
  return menos[Math.floor(rng.proximo() * menos.length)];
}

function escolherThompson(estado, elegiveis, rng) {
  let melhor = null, melhorTheta = -1;
  for (const t of elegiveis) {
    const [a, b] = estado.temas[t] || PRIORI.tanto_faz;
    const theta = amostrarBeta(rng, a, b);
    if (theta > melhorTheta) { melhor = t; melhorTheta = theta; }
  }
  return melhor;
}

/** Dentro do tema: média das amostras dos tipos de espanto do fato + 0,1 × nota_surpresa. */
export function escolherFatoDoTema(estado, indice, tema, rng) {
  const candidatos = naoVistos(estado, indice, tema).sort((x, y) => (x.id < y.id ? -1 : 1));
  const amostra = {};
  for (const tipo of new Set(candidatos.flatMap((f) => f.tipos_espanto))) {
    const [a, b] = estado.tipos[tipo] || [1, 1];
    amostra[tipo] = amostrarBeta(rng, a, b);
  }
  let melhor = null, melhorScore = -Infinity;
  for (const f of candidatos) {
    const ts = f.tipos_espanto.length ? f.tipos_espanto : [];
    const m = ts.length ? ts.reduce((s, t) => s + amostra[t], 0) / ts.length : 0.5;
    const score = m + PESO_NOTA * (f.nota_surpresa || 0);
    if (score > melhorScore) { melhor = f; melhorScore = score; }
  }
  return melhor;
}

/**
 * Escolhe o próximo fato. Não marca como exibido (chame marcarExibido ao mostrar).
 * Devolve {fato, modo: "exploracao" | "thompson"} ou null quando não há mais fatos.
 */
export function proximoFato(estado, indice, rng, { probExploracao = PROB_EXPLORACAO } = {}) {
  const elegiveis = temasElegiveis(estado, indice);
  if (!elegiveis.length) return null;
  const explorar = rng.proximo() < probExploracao;
  const tema = explorar ? escolherExploracao(estado, indice, elegiveis, rng) : escolherThompson(estado, elegiveis, rng);
  return { fato: escolherFatoDoTema(estado, indice, tema, rng), modo: explorar ? "exploracao" : "thompson" };
}

// ---------- questionário ----------

/**
 * Até n fatos para a etapa 2 do questionário, cobrindo áreas e tipos de espanto variados:
 * a cada passo, o fato que traz mais áreas novas, depois mais tipos novos, depois maior nota.
 */
export function amostraQuestionario(indice, rng, n = 15) {
  const restantes = [...indice.fatoPorId.values()].sort((x, y) => (x.id < y.id ? -1 : 1));
  const escolhidos = [];
  const contaArea = {}, contaTema = {}, tiposVistos = new Set();
  while (escolhidos.length < n && restantes.length) {
    let melhor = [], melhorChave = null;
    for (const f of restantes) {
      const area = indice.temas.get(f.tema).area;
      const chave = [
        -(contaArea[area] || 0),
        -(contaTema[f.tema] || 0),
        f.tipos_espanto.filter((t) => !tiposVistos.has(t)).length,
        f.nota_surpresa || 0,
      ];
      const cmp = melhorChave ? compararChaves(chave, melhorChave) : 1;
      if (cmp > 0) { melhor = [f]; melhorChave = chave; } else if (cmp === 0) melhor.push(f);
    }
    const f = melhor[Math.floor(rng.proximo() * melhor.length)];
    escolhidos.push(f);
    restantes.splice(restantes.indexOf(f), 1);
    const area = indice.temas.get(f.tema).area;
    contaArea[area] = (contaArea[area] || 0) + 1;
    contaTema[f.tema] = (contaTema[f.tema] || 0) + 1;
    f.tipos_espanto.forEach((t) => tiposVistos.add(t));
  }
  return escolhidos;
}

function compararChaves(a, b) {
  for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return a[i] > b[i] ? 1 : -1;
  return 0;
}

/** Recalcula o estado do zero: prioris do questionário + todas as reações do histórico, em ordem. */
export function reconstruirEstado(indice, respostasAreas, historico) {
  const estado = estadoInicial(indice, respostasAreas);
  for (const h of historico) {
    const f = indice.fatoPorId.get(h.id);
    if (!f) continue;
    if (h.exibido) marcarExibido(estado, indice, f);
    if (h.reacao) registrarReacao(estado, indice, f, h.reacao);
  }
  return estado;
}
