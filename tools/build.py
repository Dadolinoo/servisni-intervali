import sys, re, os
sys.path.insert(0, os.path.dirname(__file__))
from icons import *
from nav_variants import VARIANTS
T=os.path.dirname(__file__)
def build(variant, sim=False):
    s=open(os.path.join(T,'template.html')).read()
    dp=open('/tmp/defaultphoto.js').read().rstrip('\n') if os.path.exists('/tmp/defaultphoto.js') else open(os.path.join(T,'defaultphoto.js')).read().rstrip('\n')
    s=s.replace('/*__DEFAULT_PHOTO__*/',dp)
    css,html=VARIANTS[variant]
    s=s.replace('/*__NAV_CSS__*/\n',css).replace('/*__NAV_HTML__*/',html())
    icons={'DL':ICON_DL,'GLOBE':ICON_GLOBE,'PLUS':ICON_PLUS,'WRENCH':ICON_WRENCH,'DOC':ICON_DOC,'CHEV':ICON_CHEV,'CLIP':ICON_CLIP,'REFRESH':ICON_REFRESH}
    s=re.sub(r'\{\{HSVG:(\w+)\}\}',lambda m:HSVG(icons[m.group(1)]),s)
    s=re.sub(r'\{\{SVG:(\w+)\}\}',lambda m:SVG(icons[m.group(1)]),s)
    assert '{{' not in s and '/*__' not in s
    if sim:  # simulacija iPhone safe-area + statusne trake za screenshotove
        s=s.replace('</style>','''    :root { --sat: 47px !important; --sab: 34px !important; }
    .sim-status { position: fixed; top: 0; left: 0; right: 0; height: 47px; z-index: 60; pointer-events: none; display: flex; align-items: flex-end; justify-content: space-between; padding: 0 30px 9px 44px; color: #fff; font: 600 16px/1 -apple-system, "SF Pro Text", "Inter", system-ui, sans-serif; }
    .sim-island { position: fixed; top: 11px; left: 50%; transform: translateX(-50%); width: 124px; height: 36px; border-radius: 20px; background: #000; z-index: 61; }
    .sim-home { position: fixed; bottom: 8px; left: 50%; transform: translateX(-50%); width: 134px; height: 5px; border-radius: 3px; background: rgba(255,255,255,0.85); z-index: 61; pointer-events: none; }
  </style>''',1)
        s=s.replace('<body class="font-sans">','''<body class="font-sans">
<div class="sim-status"><span>9:41</span><span style="display:flex;gap:6px;align-items:center"><svg width="18" height="12" viewBox="0 0 18 12" fill="#fff"><rect x="0" y="8" width="3" height="4" rx="1"/><rect x="5" y="5.5" width="3" height="6.5" rx="1"/><rect x="10" y="3" width="3" height="9" rx="1"/><rect x="15" y="0" width="3" height="12" rx="1"/></svg><svg width="16" height="12" viewBox="0 0 16 12" fill="#fff"><path d="M8 2.5c2.3 0 4.4.9 6 2.4l1.1-1.2A10.2 10.2 0 0 0 8 .8C5.3.8 2.8 1.8.9 3.7L2 4.9a8.5 8.5 0 0 1 6-2.4zm0 3.4c1.4 0 2.6.5 3.6 1.4l1.1-1.2A6.9 6.9 0 0 0 8 4.2c-1.8 0-3.5.7-4.7 1.9l1.1 1.2c1-.9 2.2-1.4 3.6-1.4zM8 9.2l2-2.1a3 3 0 0 0-4 0z"/></svg><svg width="27" height="13" viewBox="0 0 27 13"><rect x=".5" y=".5" width="23" height="12" rx="3.5" fill="none" stroke="rgba(255,255,255,.4)"/><rect x="2" y="2" width="20" height="9" rx="2" fill="#fff"/><path d="M25 4.5v4c.8-.3 1.3-1.1 1.3-2s-.5-1.7-1.3-2z" fill="rgba(255,255,255,.4)"/></svg></span></div>
<div class="sim-island"></div><div class="sim-home"></div>''',1)
    return s
if __name__=='__main__':
    v=sys.argv[1]; out=sys.argv[2]; sim=len(sys.argv)>3 and sys.argv[3]=='sim'
    open(out,'w').write(build(v,sim))
