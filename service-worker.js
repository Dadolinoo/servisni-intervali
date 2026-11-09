// KILL-SWITCH service worker
// Postavlja se na adresu STAROG service workera (npr. service-worker.js) – ili privremeno umjesto sw.js.
// Kad ga preglednik preuzme kao "ažuriranje", odmah: briše sve cacheove, odregistrira sebe
// i ponovno učita otvorene prozore, pa se aplikacija učita svježe s mreže.
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.map((k) => caches.delete(k)));
    await self.registration.unregister();
    const wins = await self.clients.matchAll({ type: 'window', includeUncontrolled: true });
    await Promise.all(wins.map((c) => c.navigate(c.url).catch(() => {})));
  })());
});
// Ne presreće ništa – sve ide ravno na mrežu
