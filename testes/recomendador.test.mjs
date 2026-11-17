// Testes do recomendador e do armazenamento do app. Rodar com: node --test testes/
import { test } from "node:test";
import assert from "node:assert/strict";

import * as R from "../app/recomendador.js";
import * as A from "../app/armazenamento.js";

const TAXONOMIA = {
  areas: [
    { id: "biologia", nome: "Biologia", temas: [
      { id: "microbiologia", nome: "Microbiologia", vizinhos: ["geologia", "astro"] },
      { id: "botanica", nome: "Botânica", vizinhos: ["geologia"] },
    ] },
    { id: "terra", nome: "Terra", temas: [{ id: "geologia", nome: "Geologia", vizinhos: ["microbiologia"] }] },
    { id: "espaco", nome: "Espaço", temas: [{ id: "astro", nome: "Astrobiologia", vizinhos: ["microbiologia"] }] },
  ],
};
const TIPOS = ["contraintuitivo", "escala_absurda", "origem_inesperada"].map((id) => ({ id, nome: id }));

function f(id, tema, tipos = ["contraintuitivo"], nota = 3, secundarios = []) {
  return { id, tema, tipos_espanto: tipos, nota_surpresa: nota, temas_secundarios: secundarios, gancho: id };
}

const FATOS = [
  f("mic-1", "microbiologia", ["contraintuitivo"], 3, ["astro"]),
  f("mic-2", "microbiologia", ["escala_absurda"], 5),
  f("mic-3", "microbiologia"),
  f("bot-1", "botanica"),
  f("bot-2", "botanica"),
  f("geo-1", "geologia", ["origem_inesperada"]),
  f("geo-2", "geologia"),
  f("ast-1", "astro"),
];

const indice = () => R.criarIndice(TAXONOMIA, FATOS, TIPOS);

test("gerador com semente é determinístico e fica em [0,1)", () => {
  const a = R.criarRng(42), b = R.criarRng(42);
  for (let i = 0; i < 1000; i++) {
    const x = a.proximo();
    assert.equal(x, b.proximo());
    assert.ok(x >= 0 && x < 1);
  }
  const c = R.criarRng(a.estado), d = R.criarRng(a.estado);
  assert.equal(c.proximo(), d.proximo());
});

test("amostra de Beta tem a média esperada", () => {
  const rng = R.criarRng(7);
  for (const [a, b] of [[3, 1], [1, 3], [1, 1], [0.5, 2.25]]) {
    let soma = 0;
    const n = 20000;
    for (let i = 0; i < n; i++) soma += R.amostrarBeta(rng, a, b);
    assert.ok(Math.abs(soma / n - a / (a + b)) < 0.01, `Beta(${a},${b})`);
  }
});

test("prioris vêm da etapa 1 por área", () => {
  const e = R.estadoInicial(indice(), { biologia: "adoro", espaco: "nao_curto" });
  assert.deepEqual(e.temas.microbiologia, [3, 1]);
  assert.deepEqual(e.temas.botanica, [3, 1]);
  assert.deepEqual(e.temas.geologia, [1, 1]);
  assert.deepEqual(e.temas.astro, [1, 3]);
  assert.deepEqual(e.tipos.escala_absurda, [1, 1]);
});

test("reação atualiza tema, secundários, vizinhos e tipos com os pesos certos", () => {
  const ix = indice();
  const e = R.estadoInicial(ix, {});
  R.registrarReacao(e, ix, ix.fatoPorId.get("mic-1"), "legal"); // r = 0,7
  const perto = (x, y) => assert.ok(Math.abs(x - y) < 1e-9, `${x} ≠ ${y}`);
  perto(e.temas.microbiologia[0], 1.7); perto(e.temas.microbiologia[1], 1.3);
  // astro é secundário (0,5) e vizinho (0,25): vale o maior peso
  perto(e.temas.astro[0], 1.35); perto(e.temas.astro[1], 1.15);
  perto(e.temas.geologia[0], 1.175); perto(e.temas.geologia[1], 1.075);
  assert.deepEqual(e.temas.botanica, [1, 1]);
  perto(e.tipos.contraintuitivo[0], 1.7);
  R.registrarReacao(e, ix, ix.fatoPorId.get("mic-2"), "meh");
  perto(e.temas.microbiologia[1], 2.3);
  assert.throws(() => R.registrarReacao(e, ix, ix.fatoPorId.get("mic-2"), "outra"));
});

test("nunca repete fato nem tema seguido, e não passa de duas vezes a mesma área", () => {
  const ix = indice();
  for (let semente = 1; semente <= 30; semente++) {
    const e = R.estadoInicial(ix, { biologia: "adoro" });
    const rng = R.criarRng(semente);
    const vistos = [];
    for (;;) {
      const p = R.proximoFato(e, ix, rng);
      if (!p) break;
      vistos.push(p.fato);
      R.marcarExibido(e, ix, p.fato);
      R.registrarReacao(e, ix, p.fato, "uau");
    }
    assert.equal(vistos.length, FATOS.length);
    assert.equal(new Set(vistos.map((x) => x.id)).size, FATOS.length);
    // As regras só podem ser quebradas quando não há alternativa: confira só o começo,
    // enquanto ainda há fatos em todas as áreas.
    for (let i = 1; i < 4; i++) assert.notEqual(vistos[i].tema, vistos[i - 1].tema, `semente ${semente}`);
  }
});

test("regra de área: depois de duas da mesma área, a terceira é de outra", () => {
  const ix = indice();
  const e = R.estadoInicial(ix, {});
  R.marcarExibido(e, ix, ix.fatoPorId.get("mic-1"));
  R.marcarExibido(e, ix, ix.fatoPorId.get("bot-1"));
  const el = R.temasElegiveis(e, ix);
  assert.deepEqual(el, ["astro", "geologia"]);
});

test("quando só sobra o mesmo tema, as regras relaxam", () => {
  const ix = indice();
  const e = R.estadoInicial(ix, {});
  for (const id of ["bot-1", "bot-2", "geo-1", "geo-2", "ast-1", "mic-1"]) R.marcarExibido(e, ix, ix.fatoPorId.get(id));
  assert.deepEqual(R.temasElegiveis(e, ix), ["microbiologia"]);
});

test("Thompson favorece temas com Uau; exploração aparece perto de 15%", () => {
  const ix = indice();
  let micro = 0, exploracao = 0;
  const n = 4000;
  const rng = R.criarRng(123);
  for (let i = 0; i < n; i++) {
    const e = R.estadoInicial(ix, { biologia: "adoro", terra: "nao_curto", espaco: "nao_curto" });
    e.temas.microbiologia = [20, 1];
    const p = R.proximoFato(e, ix, rng);
    if (p.fato.tema === "microbiologia") micro++;
    if (p.modo === "exploracao") exploracao++;
  }
  assert.ok(micro / n > 0.7, `micro ${micro / n}`);
  assert.ok(Math.abs(exploracao / n - 0.15) < 0.02, `exploração ${exploracao / n}`);
});

test("exploração prefere tema pouco exibido, vizinho de favorito", () => {
  const ix = indice();
  const e = R.estadoInicial(ix, {});
  e.temas.microbiologia = [10, 1];
  e.exibicoesTema = { microbiologia: 5, botanica: 3, geologia: 1 };
  e.exibicoesArea = { biologia: 8, terra: 1 };
  const p = R.proximoFato(e, ix, R.criarRng(1), { probExploracao: 1 });
  assert.equal(p.modo, "exploracao");
  assert.equal(p.fato.tema, "astro"); // vizinho de microbiologia e nunca exibido
});

test("dentro do tema, nota alta pesa", () => {
  const ix = indice();
  const e = R.estadoInicial(ix, {});
  let mic2 = 0;
  const rng = R.criarRng(5);
  for (let i = 0; i < 500; i++) if (R.escolherFatoDoTema(e, ix, "microbiologia", rng).id === "mic-2") mic2++;
  // nota 5 contra nota 3: +0,2 no score. Com tipos ainda sem histórico (Beta(1,1)),
  // P(U1 + 0,2 > U2) = 1 − 0,8²/2 = 0,68.
  assert.ok(Math.abs(mic2 / 500 - 0.68) < 0.06, `${mic2}`);
});

test("amostra do questionário cobre áreas antes de repetir e é determinística", () => {
  const ix = indice();
  const a = R.amostraQuestionario(ix, R.criarRng(9), 3);
  const b = R.amostraQuestionario(ix, R.criarRng(9), 3);
  assert.deepEqual(a.map((x) => x.id), b.map((x) => x.id));
  const areas = new Set(a.map((x) => ix.temas.get(x.tema).area));
  assert.equal(areas.size, 3);
  assert.equal(R.amostraQuestionario(ix, R.criarRng(9), 50).length, FATOS.length);
});

test("reconstruirEstado reproduz a sequência de reações", () => {
  const ix = indice();
  const e = R.estadoInicial(ix, { terra: "adoro" });
  const hist = [];
  for (const [id, reacao] of [["mic-1", "uau"], ["geo-1", "meh"], ["ast-1", null]]) {
    const fato = ix.fatoPorId.get(id);
    R.marcarExibido(e, ix, fato);
    if (reacao) R.registrarReacao(e, ix, fato, reacao);
    hist.push({ id, exibido: true, reacao });
  }
  hist.push({ id: "bot-1", exibido: false, reacao: "legal" });
  R.registrarReacao(e, ix, ix.fatoPorId.get("bot-1"), "legal");
  assert.deepEqual(R.reconstruirEstado(ix, { terra: "adoro" }, hist), e);
});

// ---------- armazenamento ----------

function storageFalso() {
  const m = new Map();
  return { getItem: (k) => (m.has(k) ? m.get(k) : null), setItem: (k, v) => m.set(k, String(v)), m };
}

test("armazenamento grava e relê perfis", () => {
  const s = storageFalso();
  const a = A.criarArmazenamento(s);
  a.alterar((d) => { const p = A.novoPerfil("  Pedro  "); d.perfis.push(p); d.perfilAtual = p.id; });
  const b = A.criarArmazenamento(s);
  assert.equal(b.dados().perfis[0].nome, "Pedro");
  assert.equal(b.dados().perfilAtual, b.dados().perfis[0].id);
  assert.ok(b.persistente);
});

test("armazenamento sem localStorage funciona na memória", () => {
  const quebrado = { getItem() { throw new Error("bloqueado"); }, setItem() { throw new Error("bloqueado"); } };
  const a = A.criarArmazenamento(quebrado);
  a.alterar((d) => d.perfis.push(A.novoPerfil("X")));
  assert.equal(a.dados().perfis.length, 1);
  assert.equal(a.persistente, false);
  const c = A.criarArmazenamento(undefined);
  c.alterar((d) => d.perfis.push(A.novoPerfil("Y")));
  assert.equal(c.persistente, false);
});

test("dados corrompidos viram armazenamento vazio", () => {
  const s = storageFalso();
  s.setItem("curiosidades.v1", "{quebrado");
  assert.deepEqual(A.criarArmazenamento(s).dados().perfis, []);
});

test("exportar e importar perfil", () => {
  const p = A.novoPerfil("Ana");
  p.favoritos.push("mic-1");
  const volta = A.lerPerfilImportado(A.exportarPerfil(p));
  assert.deepEqual(volta, p);
  assert.throws(() => A.lerPerfilImportado("não é json"), /JSON/);
  assert.throws(() => A.lerPerfilImportado('{"x":1}'), /perfil/);
});
