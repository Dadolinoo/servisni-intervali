from icons import *

# ---------- Filled ikone (za aktivni tab) – iste siluete kao outline ----------
CAR_BODY='M3 16V12.9a2 2 0 0 1 .59-1.41L5.4 9.7l1.7-3.7A2 2 0 0 1 8.9 4.8h6.2a2 2 0 0 1 1.8 1.2l1.7 3.7 1.81 1.79A2 2 0 0 1 21 12.9V16a1.2 1.2 0 0 1-1.2 1.2H4.2A1.2 1.2 0 0 1 3 16z'
CAR_O=f'<path d="{CAR_BODY}"/><path d="M5.4 9.7h13.2"/><circle cx="7.3" cy="13.3" r=".9"/><circle cx="16.7" cy="13.3" r=".9"/><path d="M6.3 17.3v2"/><path d="M17.7 17.3v2"/>'
def CAR_F(p): return (f'<defs><mask id="{p}car"><rect width="24" height="24" fill="#fff"/><path d="M8.35 6.3h7.3l1.3 2.9H7.05z" fill="#000"/>'
    f'<circle cx="7.3" cy="13.3" r="1.25" fill="#000"/><circle cx="16.7" cy="13.3" r="1.25" fill="#000"/></mask></defs>'
    f'<path d="{CAR_BODY}" fill="currentColor" stroke="none" mask="url(#{p}car)"/>'
    '<rect x="4.7" y="16" width="3.3" height="3.9" rx="1.2" fill="currentColor" stroke="none"/><rect x="16" y="16" width="3.3" height="3.9" rx="1.2" fill="currentColor" stroke="none"/>')
WRENCH_P='M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z'
WRENCH_O=f'<path d="{WRENCH_P}"/>'
def WRENCH_F(p): return f'<path d="{WRENCH_P}" fill="currentColor"/>'
DOC_P='M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5z'
DOC_O=f'<path d="{DOC_P}"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M8 13h8"/><path d="M8 17h5"/>'
def DOC_F(p): return (f'<defs><mask id="{p}doc"><rect width="24" height="24" fill="#fff"/><path d="M8 13h8M8 17h5" stroke="#000" stroke-width="1.9" stroke-linecap="round"/>'
    f'<path d="M14 1v5a2 2 0 0 0 2 2h5" stroke="#000" stroke-width="1.6" fill="none"/></mask></defs>'
    f'<path d="{DOC_P}" fill="currentColor" stroke="currentColor" mask="url(#{p}doc)"/>')
GEAR_P='M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z'
GEAR_O=f'<path d="{GEAR_P}"/><circle cx="12" cy="12" r="3"/>'
def GEAR_F(p): return (f'<defs><mask id="{p}gear"><rect width="24" height="24" fill="#fff"/><circle cx="12" cy="12" r="3.1" fill="#000"/></mask></defs>'
    f'<path d="{GEAR_P}" fill="currentColor" mask="url(#{p}gear)"/>')

TABS=[('vehicles','Vozila',CAR_O,CAR_F,"goTab('home')"),
      ('services','Servisi',WRENCH_O,WRENCH_F,"goTab('services')"),
      ('documents','Dokumenti',DOC_O,DOC_F,"goTab('documents')"),
      ('settings','Postavke',GEAR_O,GEAR_F,"showLang = true")]

def svg(inner, cls, sw):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" class="{cls}" aria-hidden="true">{inner}</svg>'

def dual(o, f, p, sw='1.8'):
    return svg(o, 'ic-o', sw) + svg(f(p), 'ic-f', sw)

# ============ PROD (1.2.0) – postojeća navigacija, nepromijenjena ============
PROD_CSS='''    .safe-nav { bottom: calc(0.75rem + var(--sab)); left: calc(1rem + var(--sal)); right: calc(1rem + var(--sar)); }
    .tab-btn:active { animation: none; transform: scale(0.9); }
    /* iOS-style lebdeća tab traka */
    .tab-bar { display: flex; justify-content: space-around; align-items: stretch; padding: 6px;
      background: rgba(30,41,59,0.72); -webkit-backdrop-filter: blur(24px) saturate(180%); backdrop-filter: blur(24px) saturate(180%);
      border: 1px solid rgba(148,163,184,0.16); border-radius: 9999px; box-shadow: 0 10px 30px rgba(0,0,0,0.45), inset 0 1px 0 rgba(255,255,255,0.05); }
    .tab-btn { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 2px; padding: 6px 0 4px; color: #94a3b8;
      background: none; border: 0; transition: color .25s ease, transform .15s ease; }
    .tab-icon { position: relative; width: 52px; height: 30px; display: flex; align-items: center; justify-content: center; }
    .tab-icon svg { position: relative; z-index: 1; transition: transform .3s cubic-bezier(.34,1.56,.64,1); }
    .tab-pill { position: absolute; inset: 0; border-radius: 9999px; background: rgba(59,130,246,0.18);
      opacity: 0; transform: scale(.6); transition: opacity .3s ease, transform .35s cubic-bezier(.34,1.56,.64,1); }
    .tab-label { font-size: 11px !important; line-height: 14px; font-weight: 500; letter-spacing: .01em; animation: none !important; }
    .tab-bar span { animation: none !important; } /* globalni letterFade bi inače prepisao opacity pill indikatora */
    .tab-active { color: #3b82f6; }
    .tab-active .tab-pill { opacity: 1; transform: scale(1); }
    .tab-active .tab-icon svg { transform: translateY(-1px); }
'''
def PROD_HTML():
    ic={'vehicles':ICON_CAR,'services':ICON_WRENCH,'documents':ICON_DOC,'settings':ICON_GEAR}
    out=['  <!-- Bottom Nav (iOS-style glass tab bar) -->','  <nav class="tab-bar safe-nav fixed z-20" role="tablist">']
    for key,label,o,f,click in TABS:
        out.append(f'''    <button @click="{click}" class="tab-btn" :class="activeTab() === '{key}' ? 'tab-active' : ''" aria-label="{label}">
      <span class="tab-icon"><span class="tab-pill"></span>{SVG(ic[key])}</span>
      <span class="tab-label">{label}</span>
    </button>''')
    out.append('  </nav>')
    return '\n'.join(out)

# ============ A: iOS 26 Liquid Glass ============
A_CSS='''    /* Varijanta A – iOS 26 "Liquid Glass" */
    .nav-a { position: fixed; z-index: 20; left: calc(14px + var(--sal)); right: calc(14px + var(--sar)); bottom: calc(8px + var(--sab));
      height: 64px; padding: 5px; display: grid; grid-template-columns: repeat(4, 1fr); border-radius: 32px; isolation: isolate;
      background: linear-gradient(180deg, rgba(255,255,255,0.13) 0%, rgba(255,255,255,0.04) 55%, rgba(255,255,255,0.07) 100%), rgba(22,30,48,0.42);
      -webkit-backdrop-filter: blur(22px) saturate(200%) brightness(1.08); backdrop-filter: blur(22px) saturate(200%) brightness(1.08);
      box-shadow: 0 18px 40px -8px rgba(0,0,0,0.55), 0 2px 6px rgba(0,0,0,0.25), inset 0 0.5px 0 rgba(255,255,255,0.55), inset 0 -0.5px 0 rgba(255,255,255,0.12); }
    /* tanki svijetli rub (gradijentni "specular" obrub) */
    .nav-a::before { content: ''; position: absolute; inset: 0; border-radius: inherit; padding: 1px; pointer-events: none;
      background: linear-gradient(160deg, rgba(255,255,255,0.55), rgba(255,255,255,0.08) 35%, rgba(255,255,255,0.04) 65%, rgba(255,255,255,0.3));
      -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0); -webkit-mask-composite: xor; mask-composite: exclude; }
    .nav-a .ind { position: absolute; z-index: 0; top: 5px; bottom: 5px; left: 5px; width: calc((100% - 10px) / 4); border-radius: 27px;
      background: linear-gradient(180deg, rgba(255,255,255,0.2), rgba(255,255,255,0.07));
      box-shadow: inset 0 0.5px 0 rgba(255,255,255,0.6), inset 0 0 0 0.5px rgba(255,255,255,0.18), 0 6px 16px rgba(0,0,0,0.28);
      transform: translateX(calc(var(--i, 0) * 100%)); transition: transform .55s cubic-bezier(.28,1.4,.45,1); }
    .nav-a button { position: relative; z-index: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px;
      color: rgba(226,232,240,0.78); background: none; border: 0; transition: color .3s ease, transform .2s ease; }
    .nav-a button:active { animation: none; transform: scale(.88); }
    .nav-a .ic { position: relative; width: 24px; height: 24px; }
    .nav-a .ic svg { position: absolute; inset: 0; width: 24px; height: 24px; transition: opacity .25s ease, transform .4s cubic-bezier(.34,1.56,.64,1); }
    .nav-a .ic-f { opacity: 0; transform: scale(.7); }
    .nav-a .lbl { font-size: 10.5px; line-height: 12px; font-weight: 600; letter-spacing: .01em; }
    .nav-a .is-active { color: #4c8dff; }
    .nav-a .is-active .ic-o { opacity: 0; transform: scale(.7); }
    .nav-a .is-active .ic-f { opacity: 1; transform: scale(1); }
    .nav-a span { animation: none !important; }
'''
def A_HTML():
    out=['  <!-- Bottom Nav – varijanta A: Liquid Glass -->',
         '''  <nav class="nav-a" role="tablist" :style="'--i:' + tabIndex()">''','    <span class="ind" aria-hidden="true"></span>']
    for key,label,o,f,click in TABS:
        out.append(f'''    <button @click="{click}" :class="activeTab() === '{key}' && 'is-active'" aria-label="{label}"><span class="ic">{dual(o,f,'a')}</span><span class="lbl">{label}</span></button>''')
    out.append('  </nav>'); return '\n'.join(out)

# ============ B: Material 3 Expressive – kompaktna kapsula ============
B_CSS='''    /* Varijanta B – kompaktna tamna kapsula, aktivni tab = proširena plava pilula */
    .nav-b { position: fixed; z-index: 20; left: 50%; transform: translateX(-50%); bottom: calc(14px + var(--sab));
      display: flex; align-items: center; gap: 4px; padding: 7px; border-radius: 9999px;
      background: rgba(13,19,33,0.86); -webkit-backdrop-filter: blur(20px) saturate(160%); backdrop-filter: blur(20px) saturate(160%);
      border: 1px solid rgba(255,255,255,0.07);
      box-shadow: 0 20px 44px -10px rgba(0,0,0,0.7), 0 0 0 0.5px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.06); }
    .nav-b button { height: 50px; min-width: 50px; padding: 0 13px; border-radius: 9999px; display: flex; align-items: center; justify-content: center; gap: 0;
      color: #8a97ab; background: transparent; border: 0;
      transition: background-color .35s ease, color .3s ease, padding .45s cubic-bezier(.2,.9,.25,1.15), gap .45s cubic-bezier(.2,.9,.25,1.15), transform .2s ease; }
    .nav-b button:active { animation: none; transform: scale(.9); }
    .nav-b .ic { position: relative; width: 24px; height: 24px; flex: none; }
    .nav-b .ic svg { position: absolute; inset: 0; width: 24px; height: 24px; transition: opacity .2s ease; }
    .nav-b .ic-f { opacity: 0; }
    .nav-b .lbl { max-width: 0; opacity: 0; overflow: hidden; white-space: nowrap; font-size: 14px; line-height: 18px; font-weight: 600; letter-spacing: .005em;
      transition: max-width .45s cubic-bezier(.2,.9,.25,1.15), opacity .25s ease .05s; }
    .nav-b .is-active { background: #3b82f6; color: #fff; padding: 0 18px 0 15px; gap: 8px;
      box-shadow: 0 6px 18px -4px rgba(59,130,246,0.65), inset 0 1px 0 rgba(255,255,255,0.22); }
    .nav-b .is-active .ic-o { opacity: 0; } .nav-b .is-active .ic-f { opacity: 1; }
    .nav-b .is-active .lbl { max-width: 110px; opacity: 1; }
    .nav-b span { animation: none !important; }
'''
def B_HTML():
    out=['  <!-- Bottom Nav – varijanta B: kompaktna kapsula (Material 3 Expressive) -->','  <nav class="nav-b" role="tablist">']
    for key,label,o,f,click in TABS:
        out.append(f'''    <button @click="{click}" :class="activeTab() === '{key}' && 'is-active'" aria-label="{label}"><span class="ic">{dual(o,f,'b','1.9')}</span><span class="lbl">{label}</span></button>''')
    out.append('  </nav>'); return '\n'.join(out)

# ============ C: Tab bar s istaknutim + u sredini ============
C_CSS='''    /* Varijanta C – usidrena traka, središnji plavi "+" gumb, točka ispod aktivnog taba */
    .header-plus { display: none !important; }
    .nav-c { position: fixed; z-index: 20; left: 0; right: 0; bottom: 0; padding: 0 calc(8px + var(--sar)) var(--sab) calc(8px + var(--sal));
      display: grid; grid-template-columns: 1fr 1fr 84px 1fr 1fr; align-items: start; height: calc(62px + var(--sab));
      background: linear-gradient(180deg, rgba(17,24,39,0.82), rgba(11,17,30,0.94));
      -webkit-backdrop-filter: blur(24px) saturate(170%); backdrop-filter: blur(24px) saturate(170%);
      border-top: 0.5px solid rgba(148,163,184,0.22); box-shadow: 0 -10px 30px rgba(0,0,0,0.35); }
    .nav-c button.tab { position: relative; height: 58px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px;
      color: #7b879b; background: none; border: 0; transition: color .25s ease, transform .2s ease; }
    .nav-c button.tab:active { animation: none; transform: scale(.88); }
    .nav-c .ic { width: 24px; height: 24px; }
    .nav-c .ic svg { width: 24px; height: 24px; transition: transform .35s cubic-bezier(.34,1.56,.64,1); }
    .nav-c .lbl { font-size: 10.5px; line-height: 12px; font-weight: 500; letter-spacing: .01em; }
    .nav-c .dot { position: absolute; bottom: 3px; width: 4px; height: 4px; border-radius: 9999px; background: #3b82f6;
      box-shadow: 0 0 8px rgba(59,130,246,0.9); transform: scale(0); opacity: 0; transition: transform .4s cubic-bezier(.34,1.8,.5,1), opacity .2s ease; }
    .nav-c .is-active { color: #3b82f6; }
    .nav-c .is-active .ic svg { transform: translateY(-2px); }
    .nav-c .is-active .lbl { font-weight: 600; }
    .nav-c .is-active .dot { transform: scale(1); opacity: 1; }
    .nav-c .fab-wrap { display: flex; justify-content: center; }
    .nav-c .fab { width: 60px; height: 60px; margin-top: -24px; border-radius: 9999px; display: flex; align-items: center; justify-content: center; color: #fff;
      background: radial-gradient(120% 120% at 30% 20%, #6aa5ff 0%, #3b82f6 45%, #1d5fe0 100%);
      border: 5px solid #0f172a; box-shadow: 0 10px 24px -4px rgba(59,130,246,0.7), 0 0 0 1px rgba(148,163,184,0.18), inset 0 1px 0 rgba(255,255,255,0.35);
      transition: transform .3s cubic-bezier(.34,1.56,.64,1), box-shadow .3s ease; }
    .nav-c .fab svg { width: 28px; height: 28px; transition: transform .45s cubic-bezier(.34,1.56,.64,1); }
    .nav-c .fab:active { animation: none; transform: scale(.9); }
    .nav-c .fab:active svg { transform: rotate(90deg); }
    .nav-c span { animation: none !important; }
'''
def C_HTML():
    out=['  <!-- Bottom Nav – varijanta C: usidrena traka sa središnjim + -->','  <nav class="nav-c" role="tablist">']
    def t(key,label,o,f,click):
        return f'''    <button @click="{click}" class="tab" :class="activeTab() === '{key}' && 'is-active'" aria-label="{label}"><span class="ic">{svg(o,'ic-o','1.6')}</span><span class="lbl">{label}</span><span class="dot"></span></button>'''
    out += [t(*TABS[0]), t(*TABS[1])]
    out.append(f'''    <div class="fab-wrap"><button @click="quickAdd()" class="fab" aria-label="Dodaj">{svg(ICON_PLUS,'','2.4')}</button></div>''')
    out += [t(*TABS[2]), t(*TABS[3])]
    out.append('  </nav>'); return '\n'.join(out)

VARIANTS={'prod':(PROD_CSS,PROD_HTML),'A':(A_CSS,A_HTML),'B':(B_CSS,B_HTML),'C':(C_CSS,C_HTML)}
