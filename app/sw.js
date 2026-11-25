// Service worker: guarda o app e os dados para funcionar offline (§6.3).
// O nome do cache leva a versão do código do app e a versão dos dados, ambas geradas em
// data/versao.js pelo construir_dados_app.py. Quando qualquer uma muda, o navegador instala
// o SW novo, que baixa tudo e apaga o cache antigo.

importScripts("data/versao.js");

const CACHE = `curiosidades-app-${self.VERSAO_APP || "x"}-dados-${self.VERSAO_DADOS || "x"}`;
const ARQUIVOS = [
  "./",
  "index.html",
  "estilo.css",
  "app.js",
  "recomendador.js",
  "armazenamento.js",
  "fundos.js",
  "manifest.json",
  "icones/icone.svg",
  "icones/icone-180.png",
  "icones/icone-192.png",
  "icones/icone-512.png",
  "icones/icone-maskable-512.png",
  "data/fatos.json",
  "data/taxonomia.json",
  "data/tipos_espanto.json",
  "data/versao.js",
];

// Em desenvolvimento (localhost), sempre busca na rede primeiro para ver as mudanças na hora.
const DESENVOLVIMENTO = ["localhost", "127.0.0.1", "[::1]"].includes(self.location.hostname);

self.addEventListener("install", (ev) => {
  ev.waitUntil(
    caches.open(CACHE)
      .then((c) => c.addAll(ARQUIVOS.map((u) => new Request(u, { cache: "reload" }))))
      .then(() => self.skipWaiting()),
  );
});

self.addEventListener("activate", (ev) => {
  ev.waitUntil(
    caches.keys()
      .then((nomes) => Promise.all(nomes.filter((n) => n.startsWith("curiosidades-") && n !== CACHE).map((n) => caches.delete(n))))
      .then(() => self.clients.claim()),
  );
});

self.addEventListener("fetch", (ev) => {
  const req = ev.request;
  if (req.method !== "GET" || new URL(req.url).origin !== self.location.origin) return;
  ev.respondWith(DESENVOLVIMENTO ? redePrimeiro(req) : cachePrimeiro(req));
});

async function cachePrimeiro(req) {
  const cache = await caches.open(CACHE);
  const achado = await cache.match(req, { ignoreSearch: true });
  if (achado) return achado;
  try {
    return await fetch(req);
  } catch {
    // navegação offline para um endereço desconhecido: devolve o app
    if (req.mode === "navigate") return (await cache.match("index.html")) || Response.error();
    return Response.error();
  }
}

async function redePrimeiro(req) {
  const cache = await caches.open(CACHE);
  try {
    const resp = await fetch(req, { cache: "no-store" });
    if (resp.ok) cache.put(req, resp.clone());
    return resp;
  } catch {
    return (await cache.match(req, { ignoreSearch: true })) ||
      (req.mode === "navigate" ? await cache.match("index.html") : null) ||
      Response.error();
  }
}
