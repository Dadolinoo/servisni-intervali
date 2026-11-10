# Servisni Intervali – upute za iPhone (PWA)

Verzija: **1.4.0** · cache: **si-v5**

Aplikacija se ne instalira iz App Storea. Na iPhoneu je otvaraš u Safariju i
dodaješ na početni zaslon („Dodaj na početni zaslon”). Radi offline, u
samostalnom (standalone) načinu, s tamnom temom.

**Adresa:** https://dadolinoo.github.io/servisni-intervali/

---

## Dodaj na početni zaslon (iPhone)

1. Otvori gornju adresu u **Safariju** (ne u Chromeu).
2. Dodirni **Podijeli** (kvadrat sa strelicom).
3. Odaberi **Dodaj na početni zaslon**.
4. Potvrdi. Ikona „Servisi” / „Servisni Intervali” pojavit će se na početnom
   zaslonu; otvara se bez Safari trake.

---

## Ažuriranje

Kad izađe nova verzija, u aplikaciji se pojavi traka
**„Dostupna je nova verzija X”** s gumbima **Ažuriraj** i **Kasnije**.
Ažuriraj učitava novu verziju; Kasnije sakrije traku do sljedećeg otvaranja.

U **Postavke** možeš i ručno stisnuti
**„Provjeri ažuriranje / Osvježi aplikaciju”**. Briše stari keš i service
worker, a tvoji podaci (vozila, servisi, dokumenti) ostaju.

Ako i dalje ostane stara verzija:

1. Potpuno zatvori aplikaciju (App Switcher → povuci gore) i otvori je ponovno.
2. Zadnja opcija – ukloni ikonu s početnog zaslona, u iPhone
   **Postavke → Safari → Napredno → Podaci web-stranica** obriši ovu domenu,
   pa u Safariju ponovno otvori adresu i **Dodaj na početni zaslon**.

---

## Premještanje podataka (npr. sa starog Netlify URL-a)

Podaci su u lokalnoj pohrani preglednika i **ne prenose se** automatski na
novu adresu. Prije prelaska:

1. Na staroj adresi: **Postavke → Preuzmi backup** (JSON datoteka).
2. Na novoj adresi: **Postavke → Vrati iz backupa** i odaberi tu datoteku.

---

## Cloud backup (od 1.4.0)

U aplikaciji se prijavi emailom i lozinkom (**Postavke → Cloud backup**).
Podaci se spremaju lokalno i automatski sinkroniziraju u oblak. Na novom
mobitelu samo se prijavi istim računom i podaci se vrate.

---

## Autorstvo fotografije

Fotografija zimske gume (`img/tire-winter.jpg`): **HopsonRoad**,
**CC BY-SA 4.0**, Wikimedia Commons. Kredit je i u Postavkama aplikacije.

---

## Za razvoj / iduću verziju

Povećaj **isti** broj na tri mjesta:

- `window.APP_VERSION` u `index.html` (i u `tools/template.html`)
- `VERSION` i `CACHE` u `sw.js` (npr. `'1.4.0'` / `'si-v5'`)
- `version.json` (`{ "version": "1.4.0", "cache": "si-v5" }`)

Zatim slijedi `tools/PUBLISH.md`.
