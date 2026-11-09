// Simulira "zaglavljenu" staru verziju: stari cache-first SW (sw.js ili service-worker.js), zatim deploy 1.3.0
const puppeteer = require('puppeteer-core');
const fs = require('fs'), path = require('path'), { execSync, spawn } = require('child_process');
const sleep = ms => new Promise(r => setTimeout(r, ms));
const PROD = '/workspace/servisni-intervali';
const OLD_INDEX = (swName) => `<!doctype html><html><head><meta charset="utf-8"><title>STARA</title></head><body><h1 id="v">STARA VERZIJA</h1>
<script>navigator.serviceWorker.register('./${swName}');</script></body></html>`;
const OLD_SW = `const C='old-cache-1';
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(['./','./index.html'])));self.skipWaiting();});
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('fetch',e=>{e.respondWith(caches.match(e.request,{ignoreSearch:true}).then(r=>r||fetch(e.request)));});`;
async function scenario(swName, port) {
  const dir = `/tmp/upd-${swName}`;
  execSync(`rm -rf ${dir} && mkdir -p ${dir}`);
  fs.writeFileSync(path.join(dir, 'index.html'), OLD_INDEX(swName));
  fs.writeFileSync(path.join(dir, swName), OLD_SW);
  const srv = spawn('python3', ['-m', 'http.server', String(port)], { cwd: dir, stdio: 'ignore' });
  await sleep(800);
  const browser = await puppeteer.launch({ executablePath: '/usr/bin/google-chrome', headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  const url = `http://localhost:${port}/`;
  await page.goto(url, { waitUntil: 'networkidle2' }); await sleep(1000);
  await page.reload({ waitUntil: 'networkidle2' });
  const before = await page.evaluate(() => document.title + ' | controlled=' + !!navigator.serviceWorker.controller);
  // "Deploy" nove verzije u istu mapu
  execSync(`cp -r ${PROD}/. ${dir}/ && rm -rf ${dir}/screens`);
  // 1. otvaranje nakon deploya (stari SW servira staru stranicu iz keša, ali preglednik provjeri SW)
  await page.goto(url, { waitUntil: 'networkidle2' }).catch(()=>{});
  await sleep(5000);
  const after1 = await page.evaluate(() => document.title + ' | APP_VERSION=' + (window.APP_VERSION || '-')).catch(e => 'err ' + e.message);
  // 2. sljedeće otvaranje
  await page.goto(url, { waitUntil: 'networkidle2' }).catch(()=>{});
  await sleep(2500);
  const after2 = await page.evaluate(async () => {
    const regs = await navigator.serviceWorker.getRegistrations();
    return document.title + ' | APP_VERSION=' + (window.APP_VERSION || '-') + ' | caches=' + JSON.stringify(await caches.keys()) + ' | regs=' + regs.map(r => (r.active && r.active.scriptURL.split('/').pop())).join(',');
  }).catch(e => 'err ' + e.message);
  console.log(`[${swName}] prije: ${before}\n   1. otvaranje nakon deploya: ${after1}\n   2. otvaranje: ${after2}`);
  await browser.close(); srv.kill();
}
(async () => { await scenario('sw.js', 8771); await scenario('service-worker.js', 8772); })();
