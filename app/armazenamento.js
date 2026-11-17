// Armazenamento local dos perfis (§6.3). Usa localStorage quando existe; se falhar
// (modo privado, cota cheia, bloqueio), continua funcionando só na memória e avisa.

const CHAVE = "curiosidades.v1";
export const VERSAO_FORMATO = 1;

function vazio() {
  return { versao: VERSAO_FORMATO, perfilAtual: null, perfis: [] };
}

/** Cria o armazenamento. `storage` é injetável para os testes (padrão: localStorage). */
export function criarArmazenamento(storage = globalThis.localStorage) {
  let persistente = true;
  let memoria = null;

  function ler() {
    if (memoria) return memoria;
    try {
      const bruto = storage?.getItem(CHAVE);
      memoria = bruto ? normalizar(JSON.parse(bruto)) : vazio();
      if (!storage) persistente = false;
    } catch {
      persistente = false;
      memoria = vazio();
    }
    return memoria;
  }

  function gravar() {
    try {
      if (!storage) throw new Error("sem localStorage");
      storage.setItem(CHAVE, JSON.stringify(memoria));
      persistente = true;
    } catch {
      persistente = false;
    }
  }

  return {
    get persistente() { ler(); return persistente; },
    dados: ler,
    /** Aplica `fn(dados)` e grava. */
    alterar(fn) {
      const d = ler();
      fn(d);
      gravar();
      return d;
    },
  };
}

function normalizar(d) {
  if (!d || typeof d !== "object" || !Array.isArray(d.perfis)) return vazio();
  d.perfis = d.perfis.filter(perfilValido).map(completarPerfil);
  if (!d.perfis.some((p) => p.id === d.perfilAtual)) d.perfilAtual = null;
  d.versao = VERSAO_FORMATO;
  return d;
}

export function novoId() {
  return "p" + Date.now().toString(36) + Math.floor(Math.random() * 1e6).toString(36);
}

export function novoPerfil(nome) {
  return completarPerfil({
    id: novoId(),
    nome: String(nome).trim().slice(0, 40) || "Sem nome",
    criadoEm: new Date().toISOString(),
  });
}

/** Preenche campos ausentes (perfis antigos ou importados). */
export function completarPerfil(p) {
  return {
    id: p.id,
    nome: p.nome,
    criadoEm: p.criadoEm || new Date().toISOString(),
    questionario: { areas: {}, etapa1: false, etapa2: false, ...(p.questionario || {}) },
    historico: Array.isArray(p.historico) ? p.historico : [],
    favoritos: Array.isArray(p.favoritos) ? p.favoritos : [],
    reportes: Array.isArray(p.reportes) ? p.reportes : [],
    atual: p.atual || null,
    rng: Number.isInteger(p.rng) ? p.rng : Math.floor(Math.random() * 2 ** 32),
  };
}

export function perfilValido(p) {
  return !!p && typeof p === "object" && typeof p.id === "string" && p.id.length > 0 && typeof p.nome === "string";
}

/** Texto JSON para exportar um perfil. */
export function exportarPerfil(p) {
  return JSON.stringify({ app: "curiosidades", formato: VERSAO_FORMATO, exportadoEm: new Date().toISOString(), perfil: p }, null, 2);
}

/** Lê o JSON exportado. Lança Error com mensagem em português se for inválido. */
export function lerPerfilImportado(texto) {
  let obj;
  try {
    obj = JSON.parse(texto);
  } catch {
    throw new Error("O arquivo não é um JSON válido.");
  }
  const p = obj && obj.app === "curiosidades" ? obj.perfil : obj;
  if (!perfilValido(p)) throw new Error("O arquivo não parece um perfil exportado deste app.");
  return completarPerfil(p);
}
