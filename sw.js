// Servisni Intervali – service worker
// Za novu verziju: povećaj VERSION i CACHE (npr. '1.4.0' / 'si-v4') te isto u index.html (APP_VERSION) i version.json.
const VERSION = '1.4.1';
const CACHE = 'si-v6';
const RUNTIME = CACHE + '-runtime';

const PRECACHE = [
  './',
  './manifest.json',
  './icon-192.png',
  './icon-512.png',
  './icon-maskable-512.png',
  './apple-touch-icon.png',
  './favicon.png',
  './img/splash.jpg',
  './img/brand-renault.jpg',
  './img/brand-kia.jpg',
  './img/brand-dacia.jpg',
  './img/tire-winter.jpg',
  './img/tire-summer.jpg',
  './img/archivo-num.ttf',
  './img/summer-road.jpg',
  './img/winter-road.jpg',
  './img/tlak-tread.png',
  './img/top-suv.png',
  './img/top-limuzina.png',
  './img/top-hatchback.png',
  './img/top-karavan.png',
  './img/top-kupe.png',
  './img/top-kombi.png'
];

// Vanjski resursi koji se keširaju kad se uspješno dohvate
const RUNTIME_HOSTS = [
  'cdn.tailwindcss.com',
  'cdn.jsdelivr.net',
  'images.unsplash.com',
  'upload.wikimedia.org'
];

// Safari odbija odgovore s redirectom za navigaciju (npr. /index.html -> /), pa ih "očisti"
async function clean(res) {
  if (!res || !res.redirected) return res;
  const body = await res.blob();
  return new Response(body, { status: res.status, statusText: res.statusText, headers: res.headers });
}

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE)
      .then((cache) => Promise.all(PRECACHE.map(async (u) => {
        const res = await clean(await fetch(new Request(u, { cache: 'reload' })));
        if (!res.ok) throw new Error('Precache failed: ' + u);
        await cache.put(u, res);
      })))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    // Obriši SVE stare cacheove (i one od starih/tuđih verzija SW-a)
    const keys = await caches.keys();
    const old = keys.filter((k) => k !== CACHE && k !== RUNTIME);
    await Promise.all(old.map((k) => caches.delete(k)));
    await self.clients.claim();
    // Ako je postojala starija verzija, prisilno ponovno učitaj otvorene prozore –
    // i one sa starim index.html koji nema 'controllerchange' osvježavanje.
    if (old.length) {
      const wins = await self.clients.matchAll({ type: 'window', includeUncontrolled: true });
      await Promise.all(wins.map((c) => c.navigate(c.url).catch(() => {})));
    }
  })());
});

self.addEventListener('message', (event) => {
  const data = event.data || {};
  if (data === 'skipWaiting' || data.type === 'SKIP_WAITING') self.skipWaiting();
  if (data.type === 'GET_VERSION' && event.ports && event.ports[0]) {
    event.ports[0].postMessage({ version: VERSION, cache: CACHE });
  }
});

function isNavigation(req, url) {
  return req.mode === 'navigate' ||
    (url.origin === self.location.origin &&
      (url.pathname.endsWith('/') || url.pathname.endsWith('/index.html')));
}

// Network-first: uvijek pokušaj svježu verziju, keš samo kad nema mreže
async function networkFirst(req, key) {
  const cache = await caches.open(CACHE);
  try {
    const fresh = await clean(await fetch(req.url, { cache: 'no-cache', credentials: 'same-origin' }));
    if (fresh && fresh.ok) await cache.put(key || req, fresh.clone());
    return fresh;
  } catch (e) {
    return (await cache.match(key || req, { ignoreSearch: true })) ||
           (await cache.match('./')) ||
           Response.error();
  }
}

// Stale-while-revalidate za CDN/slike: odmah iz keša, u pozadini osvježi (sprema samo uspješne odgovore)
async function staleWhileRevalidate(event, req) {
  const cache = await caches.open(RUNTIME);
  const cached = await cache.match(req);
  const network = fetch(req).then((res) => {
    if (res && (res.ok || res.type === 'opaque')) cache.put(req, res.clone());
    return res;
  }).catch(() => cached);
  if (cached) {
    event.waitUntil(network.catch(() => {}));
    return cached;
  }
  return network;
}

// Lokalne statične datoteke: cache-first
async function cacheFirst(req) {
  const cache = await caches.open(CACHE);
  const cached = await cache.match(req, { ignoreSearch: true });
  if (cached) return cached;
  const res = await fetch(req);
  if (res && res.ok) cache.put(req, res.clone());
  return res;
}

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);

  if (url.origin === self.location.origin) {
    const p = url.pathname;
    // version.json i SW datoteke nikad iz keša
    if (p.endsWith('/version.json') || p.endsWith('.js') && /\/(sw|service-?worker)\.js$/.test(p)) return;
    if (isNavigation(req, url)) { event.respondWith(networkFirst(req, './')); return; }
    if (p.endsWith('/manifest.json')) { event.respondWith(networkFirst(req)); return; }
    event.respondWith(cacheFirst(req));
    return;
  }
  if (RUNTIME_HOSTS.some((h) => url.hostname === h || url.hostname.endsWith('.' + h))) {
    event.respondWith(staleWhileRevalidate(event, req));
  }
});
