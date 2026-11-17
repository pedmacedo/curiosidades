// Interface do app: perfis, questionário, feed, favoritos e "Meu perfil" (§6.1).
// Toda a lógica de escolha fica em recomendador.js; aqui só há telas e eventos.

import * as R from "./recomendador.js";
import {
  criarArmazenamento, novoPerfil, exportarPerfil, lerPerfilImportado,
} from "./armazenamento.js";

const store = criarArmazenamento();
const tela = document.getElementById("tela");
const abas = document.getElementById("abas");
const chip = document.getElementById("chip-perfil");
const aviso = document.getElementById("aviso");

const REACOES = [
  { id: "uau", emoji: "🤯", nome: "Uau!" },
  { id: "legal", emoji: "🙂", nome: "Legal" },
  { id: "meh", emoji: "😐", nome: "Meh" },
];
const OPCOES_AREA = [
  { id: "adoro", nome: "Adoro" },
  { id: "tanto_faz", nome: "Tanto faz" },
  { id: "nao_curto", nome: "Não curto" },
];
const SELO = { consenso_parcial: "Consenso parcial", hipotese: "Hipótese" };
const N_QUESTIONARIO = 15;

let acervo = null; // {fatos, taxonomia, tipos, indice, nomeTipo, versao}
let passoQuestionario = 0; // posição na etapa 2 (só na memória)

// ---------- utilidades ----------

const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const urlSegura = (u) => (/^https?:\/\//i.test(u) ? esc(u) : "#");
const agora = () => new Date().toISOString();

function hashTexto(s) {
  let h = 2166136261;
  for (const c of s) h = Math.imul(h ^ c.codePointAt(0), 16777619);
  return h >>> 0;
}

function perfil(d = store.dados()) {
  return d.perfis.find((p) => p.id === d.perfilAtual) || null;
}

/** Altera o perfil atual e grava. */
function mudarPerfil(fn) {
  store.alterar((d) => { const p = perfil(d); if (p) fn(p); });
  mostrarAvisoArmazenamento();
}

function irPara(rota) {
  if (location.hash === rota) render();
  else location.hash = rota;
}

function nomeTema(id) { return acervo.indice.temas.get(id)?.nome || id; }
function nomeArea(id) { return acervo.indice.areas.get(id)?.nome || id; }

function estadoDoPerfil(p) {
  return R.reconstruirEstado(acervo.indice, p.questionario.areas, p.historico);
}

function mostrarAvisoArmazenamento() {
  aviso.hidden = store.persistente;
  if (!store.persistente) {
    aviso.textContent = "Este navegador não está guardando os dados. O seu progresso se perde quando a página fechar.";
  }
}

function mensagemRapida(texto) {
  const el = document.createElement("div");
  el.className = "toast";
  el.setAttribute("role", "status");
  el.textContent = texto;
  document.body.append(el);
  setTimeout(() => el.remove(), 2600);
}

async function copiar(texto) {
  try {
    await navigator.clipboard.writeText(texto);
    mensagemRapida("Copiado.");
  } catch {
    // sem permissão de área de transferência: mostra o texto para copiar à mão
    const dlg = document.createElement("dialog");
    dlg.innerHTML = `<p>Copie o texto abaixo:</p><textarea rows="10" readonly>${esc(texto)}</textarea>
      <div class="linha-botoes"><button class="botao" value="ok">Fechar</button></div>`;
    document.body.append(dlg);
    dlg.querySelector("button").onclick = () => dlg.close();
    dlg.addEventListener("close", () => dlg.remove());
    dlg.showModal();
    dlg.querySelector("textarea").select();
  }
}

// ---------- carregamento ----------

async function carregarAcervo() {
  const pegar = async (nome) => {
    const r = await fetch(`data/${nome}`);
    if (!r.ok) throw new Error(`${nome}: HTTP ${r.status}`);
    return r.json();
  };
  const [fatos, taxonomia, tipos] = await Promise.all([pegar("fatos.json"), pegar("taxonomia.json"), pegar("tipos_espanto.json")]);
  const indice = R.criarIndice(taxonomia, fatos.fatos, tipos.tipos);
  const nomeTipo = Object.fromEntries(tipos.tipos.map((t) => [t.id, t.nome]));
  return { fatos: fatos.fatos, taxonomia, tipos: tipos.tipos, indice, nomeTipo };
}

// ---------- roteamento ----------

const TELAS = {
  "/perfis": telaPerfis,
  "/questionario": telaQuestionario,
  "/feed": telaFeed,
  "/favoritos": telaFavoritos,
  "/perfil": telaMeuPerfil,
};

function render() {
  const rota = location.hash.replace(/^#/, "") || "/feed";
  const p = perfil();
  let destino = TELAS[rota] ? rota : "/feed";
  if (!p) destino = "/perfis";
  else if (destino !== "/perfis" && !(p.questionario.etapa1 && p.questionario.etapa2)) destino = "/questionario";

  const comAbas = !!p && destino !== "/questionario" && destino !== "/perfis";
  abas.hidden = !comAbas;
  for (const a of abas.querySelectorAll("a")) a.toggleAttribute("aria-current", "/" + a.dataset.aba === destino);
  chip.hidden = !p;
  if (p) chip.textContent = p.nome;
  document.body.classList.toggle("com-abas", comAbas);

  TELAS[destino]();
  tela.focus({ preventScroll: true });
  window.scrollTo(0, 0);
}

// ---------- perfis ----------

function telaPerfis() {
  const d = store.dados();
  tela.innerHTML = `
    <section class="bloco">
      <h1>${d.perfis.length ? "Quem está usando?" : "Bem-vindo!"}</h1>
      ${d.perfis.length ? "" : `<p class="leve">Cada pessoa da família pode ter o seu perfil neste aparelho. Os dados ficam só aqui.</p>`}
      <ul class="lista-perfis">
        ${d.perfis.map((p) => `<li><button class="botao grande ${p.id === d.perfilAtual ? "ativo" : ""}" data-perfil="${esc(p.id)}">${esc(p.nome)}</button></li>`).join("")}
      </ul>
      <form id="form-perfil" class="form-linha">
        <label for="nome-perfil">${d.perfis.length ? "Novo perfil" : "Como você se chama?"}</label>
        <div class="linha-botoes">
          <input id="nome-perfil" name="nome" maxlength="40" autocomplete="off" required placeholder="Nome">
          <button class="botao primario" type="submit">Criar</button>
        </div>
      </form>
      <p class="leve pequeno"><a href="#" id="importar-link">Importar um perfil exportado</a></p>
      <input type="file" id="arquivo-importar" accept="application/json,.json" hidden>
    </section>`;

  tela.querySelectorAll("[data-perfil]").forEach((b) => b.addEventListener("click", () => {
    store.alterar((d2) => { d2.perfilAtual = b.dataset.perfil; });
    irPara("#/feed");
  }));
  tela.querySelector("#form-perfil").addEventListener("submit", (ev) => {
    ev.preventDefault();
    const nome = ev.target.nome.value.trim();
    if (!nome) return;
    const p = novoPerfil(nome);
    store.alterar((d2) => { d2.perfis.push(p); d2.perfilAtual = p.id; });
    passoQuestionario = 0;
    irPara("#/questionario");
  });
  ligarImportacao(tela.querySelector("#importar-link"), tela.querySelector("#arquivo-importar"));
}

function ligarImportacao(link, input) {
  link.addEventListener("click", (ev) => { ev.preventDefault(); input.click(); });
  input.addEventListener("change", async () => {
    const arq = input.files[0];
    if (!arq) return;
    try {
      const p = lerPerfilImportado(await arq.text());
      const existe = store.dados().perfis.some((x) => x.id === p.id);
      if (existe && !confirm(`Já existe um perfil igual a "${p.nome}" neste aparelho. Substituir pelos dados do arquivo?`)) return;
      store.alterar((d) => {
        d.perfis = d.perfis.filter((x) => x.id !== p.id);
        d.perfis.push(p);
        d.perfilAtual = p.id;
      });
      mensagemRapida(`Perfil "${p.nome}" importado.`);
      irPara("#/feed");
    } catch (e) {
      alert(e.message);
    } finally {
      input.value = "";
    }
  });
}

// ---------- questionário ----------

function telaQuestionario() {
  const p = perfil();
  if (!p.questionario.etapa1) return etapa1(p);
  return etapa2(p);
}

function etapa1(p) {
  const respostas = p.questionario.areas;
  tela.innerHTML = `
    <section class="bloco">
      <p class="passo">Etapa 1 de 2</p>
      <h1>Do que você gosta?</h1>
      <p class="leve">Marque como você se sente sobre cada área. Isso é só o ponto de partida: o app aprende com as suas reações.</p>
      <form id="form-areas">
        ${acervo.taxonomia.areas.map((a) => `
          <fieldset class="area-escolha">
            <legend>${esc(a.nome)}</legend>
            <div class="segmentado">
              ${OPCOES_AREA.map((o) => `
                <label><input type="radio" name="${esc(a.id)}" value="${o.id}" ${(respostas[a.id] || "tanto_faz") === o.id ? "checked" : ""}><span>${o.nome}</span></label>`).join("")}
            </div>
          </fieldset>`).join("")}
        <button class="botao primario grande largo" type="submit">Continuar</button>
      </form>
    </section>`;
  tela.querySelector("#form-areas").addEventListener("submit", (ev) => {
    ev.preventDefault();
    const fd = new FormData(ev.target);
    const areas = {};
    for (const a of acervo.taxonomia.areas) areas[a.id] = fd.get(a.id) || "tanto_faz";
    mudarPerfil((p2) => { p2.questionario.areas = areas; p2.questionario.etapa1 = true; });
    passoQuestionario = 0;
    render();
  });
}

function amostraDoPerfil(p) {
  return R.amostraQuestionario(acervo.indice, R.criarRng(hashTexto(p.id)), N_QUESTIONARIO);
}

function etapa2(p) {
  const amostra = amostraDoPerfil(p);
  const respondidos = new Set(p.historico.filter((h) => h.origem === "questionario").map((h) => h.id));
  while (passoQuestionario < amostra.length && respondidos.has(amostra[passoQuestionario].id)) passoQuestionario++;
  if (passoQuestionario >= amostra.length) {
    mudarPerfil((p2) => { p2.questionario.etapa2 = true; });
    passoQuestionario = 0;
    mensagemRapida("Pronto! Agora é com você.");
    return irPara("#/feed");
  }
  const f = amostra[passoQuestionario];
  tela.innerHTML = `
    <section class="bloco">
      <p class="passo">Etapa 2 de 2 · ${passoQuestionario + 1} de ${amostra.length}</p>
      <div class="progresso" aria-hidden="true"><span style="width:${(100 * passoQuestionario) / amostra.length}%"></span></div>
      <p class="leve">Qual a sua reação a esta curiosidade?</p>
      <article class="cartao">
        <p class="rotulo">${esc(nomeArea(acervo.indice.temas.get(f.tema).area))} · ${esc(nomeTema(f.tema))}</p>
        <h1 class="gancho">${esc(f.gancho)}</h1>
      </article>
      ${htmlReacoes()}
      <p class="centro"><button class="botao-texto" id="pular">Pular</button></p>
    </section>`;
  tela.querySelectorAll("[data-reacao]").forEach((b) => b.addEventListener("click", () => {
    mudarPerfil((p2) => p2.historico.push({ id: f.id, origem: "questionario", exibido: false, reacao: b.dataset.reacao, em: agora() }));
    passoQuestionario++;
    render();
  }));
  tela.querySelector("#pular").addEventListener("click", () => {
    mudarPerfil((p2) => p2.historico.push({ id: f.id, origem: "questionario", exibido: false, reacao: null, em: agora() }));
    passoQuestionario++;
    render();
  });
}

function htmlReacoes() {
  return `<div class="reacoes" role="group" aria-label="Reações">
    ${REACOES.map((r) => `<button class="reacao" data-reacao="${r.id}"><span class="emoji" aria-hidden="true">${r.emoji}</span>${r.nome}</button>`).join("")}
  </div>`;
}

// ---------- feed ----------

function telaFeed() {
  const p = perfil();
  let fato = p.atual ? acervo.indice.fatoPorId.get(p.atual) : null;
  if (!fato) {
    const estado = estadoDoPerfil(p);
    const rng = R.criarRng(p.rng);
    const escolha = R.proximoFato(estado, acervo.indice, rng);
    if (!escolha) return telaFim(p);
    fato = escolha.fato;
    mudarPerfil((p2) => {
      p2.rng = rng.estado;
      p2.atual = fato.id;
      p2.historico.push({ id: fato.id, origem: "feed", exibido: true, reacao: null, modo: escolha.modo, em: agora() });
    });
  }
  const favorito = p.favoritos.includes(fato.id);
  tela.innerHTML = `
    <section class="bloco">
      ${htmlCartao(fato, { favorito, aberto: false })}
      ${htmlReacoes()}
    </section>`;
  ligarCartao(fato);
  tela.querySelectorAll("[data-reacao]").forEach((b) => b.addEventListener("click", () => {
    mudarPerfil((p2) => {
      const h = [...p2.historico].reverse().find((x) => x.id === fato.id && x.origem === "feed");
      if (h) { h.reacao = b.dataset.reacao; h.reagidoEm = agora(); }
      p2.atual = null;
    });
    render();
  }));
}

function telaFim(p) {
  const total = acervo.fatos.length;
  tela.innerHTML = `
    <section class="bloco centro">
      <h1>Você viu tudo!</h1>
      <p class="leve">Já passaram por aqui as ${total} curiosidades do acervo atual. Novas chegam quando o acervo for atualizado.</p>
      <p><a class="botao" href="#/favoritos">Rever favoritos (${p.favoritos.length})</a></p>
    </section>`;
}

function htmlCartao(f, { favorito, aberto }) {
  const area = acervo.indice.temas.get(f.tema).area;
  const paragrafos = f.explicacao.split(/\n{2,}/).map((t) => `<p>${esc(t)}</p>`).join("");
  return `
    <article class="cartao" data-fato="${esc(f.id)}">
      <p class="rotulo">${esc(nomeArea(area))} · ${esc(nomeTema(f.tema))}</p>
      <h1 class="gancho">${esc(f.gancho)}</h1>
      <p class="etiquetas">
        ${f.tipos_espanto.map((t) => `<span class="etiqueta">${esc(acervo.nomeTipo[t] || t)}</span>`).join("")}
        ${SELO[f.confianca] ? `<span class="etiqueta selo" title="A ciência ainda debate este assunto">${SELO[f.confianca]}</span>` : ""}
      </p>
      <button class="botao largo ver-explicacao" aria-expanded="${aberto}">${aberto ? "Esconder explicação" : "Ver explicação"}</button>
      <div class="explicacao" ${aberto ? "" : "hidden"}>
        ${paragrafos}
        <h2>Fontes</h2>
        <ul class="fontes">${f.fontes.map((x) => `<li><a href="${urlSegura(x.url)}" target="_blank" rel="noopener">${esc(x.titulo)}</a></li>`).join("")}</ul>
        ${f.aprofundar?.length ? `<h2>Para aprofundar</h2>
          <ul class="fontes">${f.aprofundar.map((x) => `<li><a href="${urlSegura(x.url)}" target="_blank" rel="noopener">${esc(x.titulo)}</a> <span class="leve">(${esc(x.tipo)})</span></li>`).join("")}</ul>` : ""}
      </div>
      <div class="acoes-cartao">
        <button class="botao-texto salvar" aria-pressed="${favorito}">${favorito ? "★ Salvo" : "☆ Salvar"}</button>
        <button class="botao-texto reportar">⚠ Parece errado</button>
      </div>
    </article>`;
}

/** Liga os botões de um cartão (explicação, salvar, reportar). */
function ligarCartao(f, raiz = tela) {
  const cartao = raiz.querySelector(`.cartao[data-fato="${CSS.escape(f.id)}"]`);
  const botaoExp = cartao.querySelector(".ver-explicacao");
  const exp = cartao.querySelector(".explicacao");
  botaoExp.addEventListener("click", () => {
    exp.hidden = !exp.hidden;
    botaoExp.setAttribute("aria-expanded", String(!exp.hidden));
    botaoExp.textContent = exp.hidden ? "Ver explicação" : "Esconder explicação";
  });
  const salvar = cartao.querySelector(".salvar");
  salvar.addEventListener("click", () => {
    let agoraFav = false;
    mudarPerfil((p) => {
      const i = p.favoritos.indexOf(f.id);
      if (i >= 0) p.favoritos.splice(i, 1);
      else { p.favoritos.push(f.id); agoraFav = true; }
    });
    salvar.setAttribute("aria-pressed", String(agoraFav));
    salvar.textContent = agoraFav ? "★ Salvo" : "☆ Salvar";
  });
  cartao.querySelector(".reportar").addEventListener("click", () => abrirReporte(f));
}

function abrirReporte(f) {
  const ja = perfil().reportes.find((r) => r.id === f.id);
  const dlg = document.createElement("dialog");
  dlg.innerHTML = `
    <form method="dialog">
      <h2>Parece errado?</h2>
      <p class="leve">O fato fica numa lista em "Meu perfil", que você pode copiar e mandar para o Pedro.</p>
      <label for="nota-reporte">O que parece errado? (opcional)</label>
      <textarea id="nota-reporte" rows="4" maxlength="600">${esc(ja?.nota || "")}</textarea>
      <div class="linha-botoes">
        <button class="botao" value="cancelar">Cancelar</button>
        <button class="botao primario" value="ok">${ja ? "Atualizar" : "Marcar"}</button>
      </div>
    </form>`;
  document.body.append(dlg);
  dlg.addEventListener("close", () => {
    if (dlg.returnValue === "ok") {
      const nota = dlg.querySelector("textarea").value.trim();
      mudarPerfil((p) => {
        p.reportes = p.reportes.filter((r) => r.id !== f.id);
        p.reportes.push({ id: f.id, nota, em: agora() });
      });
      mensagemRapida("Anotado. Obrigado!");
    }
    dlg.remove();
  });
  dlg.showModal();
}

// ---------- favoritos ----------

function telaFavoritos() {
  const p = perfil();
  const fatos = [...p.favoritos].reverse().map((id) => acervo.indice.fatoPorId.get(id)).filter(Boolean);
  tela.innerHTML = `
    <section class="bloco">
      <h1>Favoritos</h1>
      ${fatos.length ? "" : `<p class="leve">Ainda nada por aqui. Toque em ☆ Salvar numa curiosidade para guardá-la.</p>`}
      <div class="lista-cartoes">${fatos.map((f) => htmlCartao(f, { favorito: true, aberto: false })).join("")}</div>
    </section>`;
  fatos.forEach((f) => ligarCartao(f));
}

// ---------- meu perfil ----------

function telaMeuPerfil() {
  const p = perfil();
  const estado = estadoDoPerfil(p);
  const reacoes = Object.fromEntries(REACOES.map((r) => [r.id, 0]));
  for (const h of p.historico) if (h.origem === "feed" && h.reacao in reacoes) reacoes[h.reacao]++;
  const vistos = p.historico.filter((h) => h.exibido).length;

  // temas com fatos no acervo, ordenados pela chance estimada de "Uau"
  const temas = [...acervo.indice.fatosPorTema.keys()]
    .map((t) => ({ t, m: R.media(estado.temas[t]), n: estado.exibicoesTema[t] || 0 }))
    .sort((a, b) => b.m - a.m)
    .slice(0, 8);
  const areas = acervo.taxonomia.areas.filter((a) => p.questionario.areas[a.id] === "adoro").map((a) => a.nome);
  const tipos = Object.entries(estado.tipos)
    .filter(([, par]) => par[0] + par[1] > 2)
    .sort((a, b) => R.media(b[1]) - R.media(a[1]))
    .slice(0, 3)
    .map(([t]) => acervo.nomeTipo[t] || t);
  const reportes = p.reportes.map((r) => ({ ...r, fato: acervo.indice.fatoPorId.get(r.id) }));

  tela.innerHTML = `
    <section class="bloco">
      <h1>${esc(p.nome)}</h1>
      <p class="leve">${vistos} curiosidade(s) vista(s) de ${acervo.fatos.length} · ${REACOES.map((r) => `${r.emoji} ${reacoes[r.id]}`).join(" · ")}</p>

      <h2>Temas que mais combinam com você</h2>
      <p class="leve pequeno">Estimativa do app para a chance de você achar um fato do tema incrível. Muda a cada reação.</p>
      <ul class="barras">
        ${temas.map(({ t, m, n }) => `<li><span class="barra-nome">${esc(nomeTema(t))} <span class="leve pequeno">· ${n} visto(s)</span></span>
          <span class="barra-valor">${Math.round(m * 100)}%</span>
          <span class="barra"><span style="width:${Math.round(m * 100)}%"></span></span></li>`).join("")}
      </ul>
      ${tipos.length ? `<p>Tipos de curiosidade preferidos: <strong>${tipos.map(esc).join(", ")}</strong>.</p>` : ""}
      <p class="leve pequeno">Áreas marcadas como "Adoro": ${areas.length ? areas.map(esc).join(", ") : "nenhuma"}.</p>

      <h2>Marcados como "parece errado"</h2>
      ${reportes.length ? `
        <ul class="reportes">${reportes.map((r) => `<li><strong>${esc(r.id)}</strong>: ${esc(r.fato?.gancho || "(fato fora do acervo atual)")}${r.nota ? `<br><span class="leve">Nota: ${esc(r.nota)}</span>` : ""}</li>`).join("")}</ul>
        <div class="linha-botoes"><button class="botao" id="copiar-reportes">Copiar a lista</button><button class="botao-texto" id="limpar-reportes">Limpar</button></div>`
        : `<p class="leve">Nenhum. Use "⚠ Parece errado" num fato se algo não bater.</p>`}

      <h2>Opções</h2>
      <div class="coluna-botoes">
        <button class="botao" id="refazer">Refazer o questionário</button>
        <button class="botao" id="exportar">Exportar perfil (arquivo)</button>
        <button class="botao" id="importar">Importar perfil</button>
        <a class="botao" href="#/perfis">Trocar de perfil</a>
        <button class="botao perigo" id="apagar">Apagar este perfil</button>
      </div>
      <input type="file" id="arquivo-importar" accept="application/json,.json" hidden>
      <p class="leve pequeno rodape">Acervo com ${acervo.fatos.length} curiosidades verificadas · dados ${esc(self.VERSAO_DADOS || "")}</p>
    </section>`;

  tela.querySelector("#copiar-reportes")?.addEventListener("click", () => {
    const linhas = reportes.map((r) => `- ${r.id}: ${r.fato?.gancho || ""}${r.nota ? `\n  Nota: ${r.nota}` : ""}`);
    copiar(`Curiosidades que parecem erradas (${p.nome}):\n${linhas.join("\n")}`);
  });
  tela.querySelector("#limpar-reportes")?.addEventListener("click", () => {
    if (!confirm("Limpar a lista de fatos marcados como errados?")) return;
    mudarPerfil((p2) => { p2.reportes = []; });
    render();
  });
  tela.querySelector("#refazer").addEventListener("click", () => {
    if (!confirm("Refazer o questionário? As suas reações no feed continuam valendo.")) return;
    mudarPerfil((p2) => {
      p2.questionario.etapa1 = false;
      p2.questionario.etapa2 = false;
      p2.historico = p2.historico.filter((h) => h.origem !== "questionario");
    });
    passoQuestionario = 0;
    irPara("#/questionario");
  });
  tela.querySelector("#exportar").addEventListener("click", () => {
    const texto = exportarPerfil(p);
    const blob = new Blob([texto], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `curiosidades-${p.nome.toLowerCase().replace(/[^a-z0-9]+/gi, "-")}-${agora().slice(0, 10)}.json`;
    document.body.append(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(a.href), 1000);
  });
  ligarImportacao(tela.querySelector("#importar"), tela.querySelector("#arquivo-importar"));
  tela.querySelector("#apagar").addEventListener("click", () => {
    if (!confirm(`Apagar o perfil "${p.nome}" deste aparelho? Isso não pode ser desfeito (a não ser que você tenha exportado).`)) return;
    store.alterar((d) => { d.perfis = d.perfis.filter((x) => x.id !== p.id); d.perfilAtual = null; });
    irPara("#/perfis");
  });
}

// ---------- início ----------

async function iniciar() {
  mostrarAvisoArmazenamento();
  chip.addEventListener("click", () => irPara("#/perfis"));
  try {
    acervo = await carregarAcervo();
  } catch (e) {
    tela.innerHTML = `<section class="bloco"><h1>Não deu para carregar as curiosidades</h1>
      <p class="leve">Verifique a conexão e tente de novo. (${esc(e.message)})</p>
      <button class="botao" onclick="location.reload()">Tentar de novo</button></section>`;
    return;
  }
  // descarta o fato "atual" se ele saiu do acervo
  store.alterar((d) => { for (const p of d.perfis) if (p.atual && !acervo.indice.fatoPorId.has(p.atual)) p.atual = null; });
  window.addEventListener("hashchange", render);
  render();
}

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("sw.js").catch(() => { /* sem offline, mas o app funciona */ });
  });
}

iniciar();
