# Objava nove verzije Servisnih intervala

Repo: `Dadolinoo/servisni-intervali`  
Live: https://dadolinoo.github.io/servisni-intervali/  
GitHub Pages služi **korijen `main` grane** (ne diraj DH-Logix repoe).

## 1. Bump verzije (isti broj na 3 mjesta)

Primjer: `1.3.1` / `si-v4` → `1.3.2` / `si-v5`

1. `index.html` — `window.APP_VERSION = '…'`
2. `sw.js` — `VERSION` i `CACHE`
3. `version.json` — `{ "version": "…", "cache": "…" }`
4. Isto u `tools/template.html` (za iduće buildove iz predloška)
5. Ažuriraj broj u `IPHONE.md`

## 2. (Opcionalno) rebuild iz predloška

```bash
cd tools
python3 build.py <nav_variant> ../index.html
```

Većina izmjena radi se direktno u `index.html`.

## 3. Commit i push na `main`

```bash
git add -A
git commit -m "Servisni Intervali X.Y.Z"
git push origin main
```

Pages se sam rebuilda (obično 1–2 minute). Provjeri:

- https://dadolinoo.github.io/servisni-intervali/
- https://dadolinoo.github.io/servisni-intervali/version.json

## 4. Što ne dirati

- Nikad `Dadolinoo/autoservis-pro-releases` ni DH-Logix `status/*.yml`
- Ne commitaj `tools/node_modules`
- Ne mijenjaj `manifest` `start_url`/`scope` s `./` (radi pod `/servisni-intervali/`)

## 5. Premještanje podataka

localStorage je po domeni. Prije prelaska s druge adrese: Postavke → Preuzmi backup, pa na novoj → Vrati iz backupa.
