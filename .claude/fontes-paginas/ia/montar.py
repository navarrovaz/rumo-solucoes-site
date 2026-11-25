# Monta scratchpad/ia/modelo.html (v2): hero na linha do aigentx e blocagem na linha do taskxen,
# com os blocos comuns do modelo da Terceirização.   python montar.py
import io, os
aqui = os.path.dirname(os.path.abspath(__file__))
T = io.open(os.path.join(aqui, '..', 'terceirizacao', 'modelo.html'), encoding='utf-8').read()

def entre(a, b, s=T):
    i = s.index(a); j = s.index(b, i)
    return s[i:j]

def svg(d, cls='ico'):
    return '<svg class="%s" viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % (cls, d)

SETA = svg('<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>')
CHK = '<path d="M20 6 9 17l-5-5"/>'
I = {
 'bot': '<rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 8V4"/><path d="M9 14h.01"/><path d="M15 14h.01"/>',
 'code': '<path d="m16 18 6-6-6-6"/><path d="m8 6-6 6 6 6"/>',
 'sliders': '<path d="M4 21v-7"/><path d="M4 10V3"/><path d="M12 21v-9"/><path d="M12 8V3"/><path d="M20 21v-5"/><path d="M20 12V3"/><path d="M1 14h6"/><path d="M9 8h6"/><path d="M17 16h6"/>',
 'shield': '<path d="M12 3 4 6v6c0 4.5 3.4 8.3 8 9 4.6-.7 8-4.5 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'layers': '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
 'pulse': '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
 'mic': '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0"/><path d="M12 18v3"/>',
 'video': '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="m16 10 5-3v10l-5-3z"/>',
 'image': '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="m21 16-5-5-9 9"/>',
 'file': '<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4"/>',
 'chat': '<path d="M21 12a8 8 0 0 1-11.5 7.2L4 21l1.8-5.2A8 8 0 1 1 21 12z"/>',
 'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
 'refresh': '<path d="M21 12a9 9 0 0 1-15.5 6.2"/><path d="M3 12A9 9 0 0 1 18.5 5.8"/><path d="M18 2v4h-4"/><path d="M6 22v-4h4"/>',
 'chart': '<path d="M3 3v18h18"/><path d="M8 16v-5"/><path d="M13 16V8"/><path d="M18 16v-9"/>',
}

# ------------------------------------------------------------------ cabeça e CSS reaproveitado
head = r'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>Inteligência Artificial · Rumo Soluções</title>
<meta name="description" content="Agentes de IA construídos sob medida e integrados ao ERP, ao CRM e aos sistemas que a sua empresa já usa. Rumo AI, o braço de inteligência artificial da Rumo.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600&family=Geist+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="../../design-system/tokens.css">
<style>
/* Inteligência Artificial (Rumo AI): hero de referência aigentx e blocagem de referência taskxen, no escuro da Rumo, grid de 12 colunas do .wrap (1440px), acento ciano (2.5). Valores em design-system/tokens.css · design system v0.8.7 */
:root{color-scheme:dark}
/*CSS_BASE*/

'''
comum = entre('/* ---------- estrutura comum ---------- */', '/* hero: o mesmo contorno neon')
pill = entre('.pill{display:inline-flex', '.th h1 .ln')
marquee = entre('.marquee{position:relative', '/* modelos de contratação')
etapas_faq_form = entre('/* ---------- S05 · como funciona: quatro etapas', '/* ---------- responsivo ---------- */')

css = r'''/* contorno neon que segue o cursor (M20) */
.lum::before,.lum::after{content:"";position:absolute;inset:0;z-index:3;border-radius:inherit;padding:1px;pointer-events:none;-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude}
.lum::before{background:linear-gradient(180deg,rgba(255,255,255,.08),rgba(255,255,255,.03));transition:background-color var(--dur-base) var(--ease-out)}
.lum::after{background:radial-gradient(260px circle at var(--mx,50%) var(--my,0%),rgba(242,251,255,.95),rgba(0,172,229,.9) 24%,rgba(0,172,229,0) 70%);opacity:0;transition:opacity var(--dur-base) var(--ease-out)}
.lum.luz::after{opacity:1}
.lum.hov::before{background:rgba(0,172,229,.35)}
.lum.hov{box-shadow:0 0 44px -14px rgba(0,172,229,.5)}

/* ---------- S02 · hero (referência aigentx): luz de cima, grade fina, marcas nos cantos; título grande embaixo à esquerda, texto e CTA à direita ---------- */
.hx{position:relative;min-height:max(100svh,820px);display:flex;flex-direction:column;justify-content:flex-end;padding:120px 0 36px;background:var(--bg);overflow:hidden;isolation:isolate}
.hx-luz{position:absolute;inset:0;z-index:-3;pointer-events:none;background:radial-gradient(130% 100% at calc(50% + var(--x,0px)) -22%,rgba(0,172,229,.9) 0%,rgba(0,150,199,.58) 22%,rgba(0,117,156,.3) 40%,rgba(0,90,120,.1) 58%,rgba(5,5,5,0) 72%),radial-gradient(60% 34% at calc(50% + var(--x,0px)) -8%,rgba(191,239,255,.5) 0%,rgba(127,216,245,0) 70%)}
.hx-grade{position:absolute;inset:0;z-index:-2;pointer-events:none;background-image:linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px);background-size:72px 72px;background-position:center top;-webkit-mask-image:radial-gradient(80% 70% at 50% 20%,#000 0%,rgba(0,0,0,.5) 50%,transparent 85%);mask-image:radial-gradient(80% 70% at 50% 20%,#000 0%,rgba(0,0,0,.5) 50%,transparent 85%)}
.hx-esfera{position:absolute;inset:0;width:100%;height:100%;z-index:-1;pointer-events:none}
.hx-fundo{position:absolute;left:0;right:0;bottom:0;height:260px;z-index:-1;pointer-events:none;background:linear-gradient(180deg,rgba(5,5,5,0),var(--bg))}
.hx-cantos{position:absolute;inset:96px 0 24px;pointer-events:none}
.hx-cantos .wrap{position:relative;height:100%}
.hx-cantos i{position:absolute;width:13px;height:13px}
.hx-cantos i::before,.hx-cantos i::after{content:"";position:absolute;background:rgba(255,255,255,.4)}
.hx-cantos i::before{left:6px;top:0;width:1px;height:13px}
.hx-cantos i::after{top:6px;left:0;height:1px;width:13px}
.hx-cantos i:nth-child(1){left:max(clamp(16px,5.5vw,80px),env(safe-area-inset-left,0px));top:0;transform:translate(-6px,-6px)}
.hx-cantos i:nth-child(2){right:max(clamp(16px,5.5vw,80px),env(safe-area-inset-right,0px));top:0;transform:translate(6px,-6px)}
.hx-cantos i:nth-child(3){left:max(clamp(16px,5.5vw,80px),env(safe-area-inset-left,0px));bottom:0;transform:translate(-6px,6px)}
.hx-cantos i:nth-child(4){right:max(clamp(16px,5.5vw,80px),env(safe-area-inset-right,0px));bottom:0;transform:translate(6px,6px)}
.hx > .wrap{width:100%;min-width:0}
.hx-conf{min-width:0}
.hx-txt{align-items:start;row-gap:32px}
.hx-tit{grid-column:1/9;display:flex;flex-direction:column;align-items:flex-start;gap:22px}
.hx-tit .ln{display:block}
.hx-h1{letter-spacing:var(--text-display--letter-spacing);line-height:var(--text-h1--line-height)}
.olho{font-size:var(--text-small);font-weight:500;background:linear-gradient(92deg,var(--color-light-core) 0%,var(--color-light-near) 50%,var(--brand) 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.hx-dir{grid-column:9/13;display:flex;flex-direction:column;align-items:flex-start;gap:24px}
.hx-dir .lead{font-size:var(--text-body)}
.hx-dir small{font-size:var(--text-caption);color:var(--fg-subtle)}
.hx-conf{margin-top:40px;display:flex;flex-direction:column;align-items:center;gap:22px}
.hx-conf p{font-size:var(--text-small);color:var(--fg-muted)}
.hx-conf .marquee{width:100%}
/* faixa das ferramentas: bloco escuro de contraste e divisórias verticais entre os logos */
.hx-conf .marquee{border-radius:var(--radius-lg);background:var(--color-ink-950);box-shadow:inset 0 0 0 1px rgba(255,255,255,.08),0 24px 48px -24px rgba(5,5,5,.9);-webkit-mask-image:none;mask-image:none}
.hx-conf .marquee::before,.hx-conf .marquee::after{content:"";position:absolute;top:0;bottom:0;width:120px;z-index:1;pointer-events:none}
.hx-conf .marquee::before{left:0;background:linear-gradient(90deg,var(--color-ink-950),rgba(5,5,5,0));border-radius:var(--radius-lg) 0 0 var(--radius-lg)}
.hx-conf .marquee::after{right:0;background:linear-gradient(270deg,var(--color-ink-950),rgba(5,5,5,0));border-radius:0 var(--radius-lg) var(--radius-lg) 0}
.hx-conf .track .set{gap:0;padding-right:0}
.hx-conf .tech{height:88px;padding:0 44px;box-shadow:inset -1px 0 0 rgba(255,255,255,.1)}
.tech{display:inline-flex;align-items:center;gap:14px;color:var(--fg-subtle);font-size:var(--text-h4);font-weight:500;letter-spacing:-.015em;white-space:nowrap;transition:color var(--dur-fast) var(--ease-out)}
.tech:hover{color:var(--fg)}
.tech svg{width:32px;height:32px;fill:currentColor;flex:none}
.tech.t-n8n svg{color:var(--logo-n8n)}
.tech.t-gemini svg{color:var(--logo-gemini)}
.tech.t-aws svg{color:var(--logo-aws)}
.tech.t-claude svg{color:var(--logo-claude)}
.tech.t-googledrive svg{color:var(--logo-googledrive)}
.tech.t-outlook svg{color:var(--logo-outlook)}
.tech.t-deepseek svg{color:var(--logo-deepseek)}
.tech.t-json svg,.tech.t-chatgpt svg,.tech.t-github svg,.tech.t-copilot svg,.tech.t-cursor svg{color:var(--fg)}
/* CTA com a luz na borda: dá uma volta quando aparece e gira com o cursor sobre ele (9.5) */
.btn-luz{overflow:hidden;isolation:isolate;background:transparent}
.btn-luz::before{content:"";position:absolute;left:50%;top:50%;width:300%;aspect-ratio:1;z-index:-2;transform:translate(-50%,-50%) rotate(0deg);background:conic-gradient(from 0deg,rgba(0,172,229,0) 0deg,rgba(0,172,229,0) 250deg,var(--color-light-near) 310deg,var(--color-light-core) 340deg,rgba(0,172,229,0) 360deg);animation:volta var(--dur-cinematic) var(--ease-in-out) var(--dur-slow) 1 both}
.btn-luz::after{content:"";position:absolute;inset:2px;z-index:-1;border-radius:inherit;background:var(--brand)}
.btn-luz:hover::before{animation:volta var(--dur-cinematic) linear infinite}
@keyframes volta{to{transform:translate(-50%,-50%) rotate(360deg)}}

/* ---------- S04 · agentes (referência taskxen): três cards alternados, texto de um lado e o agente em ação do outro ---------- */
.cards-ag{display:flex;flex-direction:column;gap:24px}
.c-ag{padding:56px;align-items:center;row-gap:40px}
.c-ag .tx{grid-column:1/6;display:flex;flex-direction:column;align-items:flex-start;gap:18px}
.c-ag .vis{grid-column:7/13}
.c-ag.inv .tx{grid-column:8/13;grid-row:1}
.c-ag.inv .vis{grid-column:1/7;grid-row:1}
.c-ag .tx > p{color:var(--fg-muted)}
.ags{list-style:none;margin:6px 0 0;padding:0;width:100%;border-top:1px solid var(--border)}
.ags li{display:flex;justify-content:space-between;align-items:baseline;gap:16px;padding:13px 0;border-bottom:1px solid var(--border)}
.ags b{font-weight:500;font-size:var(--text-small);flex:none}
.ags span{font-size:var(--text-caption);color:var(--fg-subtle);text-align:right}
.palco{position:relative;border-radius:var(--radius-lg);background:radial-gradient(70% 60% at 50% 0%,rgba(0,172,229,.16),rgba(0,172,229,0) 70%),var(--color-ink-950);box-shadow:inset 0 0 0 1px rgba(255,255,255,.07);padding:28px;min-height:420px;display:flex;flex-direction:column;justify-content:center}
.palco .pts{display:flex;justify-content:center;gap:6px;margin-top:20px}
.palco .pts i{width:6px;height:6px;border-radius:50%;background:rgba(255,255,255,.2)}
.palco .pts i.on{background:var(--brand)}
.jan{border-radius:var(--radius-lg);background:rgba(11,11,11,.92);box-shadow:inset 0 0 0 1px rgba(255,255,255,.1),0 30px 60px -24px rgba(5,5,5,.9)}
.jan-h{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:14px 18px;border-bottom:1px solid var(--border)}
.jan-h .ag{display:flex;align-items:center;gap:12px}
.jan-h .ag b{font-weight:500;font-size:var(--text-small)}
.jan .cir{width:32px;height:32px;border-radius:50%;flex:none;display:grid;place-items:center;background:var(--brand);color:var(--on-brand)}
.jan .cir .ico{width:16px;height:16px}
/* vendas: conversa */
.msgs{padding:18px;display:flex;flex-direction:column;gap:10px;min-height:300px}
.msg{max-width:84%;padding:11px 15px;border-radius:var(--radius-lg);font-size:var(--text-small);line-height:1.5;opacity:0;transform:translateY(8px);transition:opacity var(--dur-base) var(--ease-out),transform var(--dur-base) var(--ease-out)}
.msg.on{opacity:1;transform:none}
.msg.cli{align-self:flex-end;background:var(--color-ink-800);color:var(--fg)}
.msg.age{align-self:flex-start;background:rgba(0,172,229,.12);box-shadow:inset 0 0 0 1px rgba(0,172,229,.3);color:var(--fg)}
.msg.sis{align-self:center;max-width:none;display:inline-flex;align-items:center;gap:8px;padding:8px 14px;border-radius:var(--radius-pill);background:none;box-shadow:inset 0 0 0 1px var(--border);font-family:var(--font-mono);font-size:var(--text-mono-micro);letter-spacing:var(--text-mono-micro--letter-spacing);text-transform:uppercase;color:var(--brand-text)}
.msg.sis .ico{width:13px;height:13px}
.msg .car{display:inline-block;width:2px;height:1em;margin-left:2px;vertical-align:-2px;background:var(--brand);animation:pisca var(--dur-cinematic) steps(1) infinite}
@keyframes pisca{50%{opacity:0}}
.jan-p{display:flex;align-items:center;gap:10px;padding:12px 18px;border-top:1px solid var(--border);color:var(--fg-subtle);font-size:var(--text-caption)}
.jan-p span{flex:1}
.rep{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 12px;border:0;border-radius:var(--radius-pill);background:none;box-shadow:inset 0 0 0 1px var(--border);color:var(--fg-muted);font-size:var(--text-caption);cursor:pointer;transition:color var(--dur-fast),box-shadow var(--dur-fast)}
.rep:hover{color:var(--fg);box-shadow:inset 0 0 0 1px var(--border-strong)}
.rep .ico{width:13px;height:13px}
/* operações: leitura de documento */
.doc{display:grid;grid-template-columns:150px 1fr;gap:18px;padding:18px}
.folha{border-radius:var(--radius-md);background:var(--color-ink-850);box-shadow:inset 0 0 0 1px rgba(255,255,255,.08);padding:16px 14px;display:flex;flex-direction:column;gap:7px;position:relative;overflow:hidden}
.folha i{height:5px;border-radius:var(--radius-xs);background:rgba(255,255,255,.12)}
.folha i.m{background:rgba(0,172,229,.55)}
.folha .scan{position:absolute;left:0;right:0;height:28px;top:-28px;background:linear-gradient(180deg,rgba(0,172,229,0),rgba(0,172,229,.22),rgba(0,172,229,0))}
.doc.on .folha .scan{animation:scan var(--dur-cinematic) var(--ease-in-out) 2 both}
@keyframes scan{to{top:100%}}
.campos{display:flex;flex-direction:column}
.campo{display:flex;justify-content:space-between;align-items:center;gap:12px;min-height:46px;border-bottom:1px solid var(--border);font-size:var(--text-small);color:var(--fg-muted);opacity:0;transform:translateX(8px);transition:opacity var(--dur-base) var(--ease-out),transform var(--dur-base) var(--ease-out)}
.campo:last-child{border-bottom:0}
.campo b{font-weight:500;color:var(--fg);text-align:right}
.doc.on .campo{opacity:1;transform:none}
/* decisão: BI conversacional */
.bi{padding:18px;display:flex;flex-direction:column;gap:16px}
.bi .msg{opacity:1;transform:none}
.barras{display:flex;flex-direction:column;gap:10px}
.barra{display:grid;grid-template-columns:96px 1fr 44px;align-items:center;gap:12px;font-size:var(--text-caption);color:var(--fg-muted)}
.barra .t{height:10px;border-radius:var(--radius-xs);background:rgba(255,255,255,.06);overflow:hidden}
.barra .t i{display:block;height:100%;width:0;border-radius:inherit;background:linear-gradient(90deg,var(--color-rumo-800),var(--brand));transition:width var(--dur-cinematic) var(--ease-out)}
.barra b{font-weight:500;color:var(--fg);text-align:right;font-family:var(--font-mono)}

/* ---------- S10 · integração (referência taskxen): título central, diagrama e CTA ---------- */
.diag{max-width:920px;margin:0 auto;padding:40px}
.diag svg{display:block;width:100%;height:auto}
.diag .ln{fill:none;stroke:rgba(127,216,245,.22);stroke-width:1.2;stroke-dasharray:1;stroke-dashoffset:1;transition:stroke-dashoffset var(--dur-cinematic) var(--ease-out),stroke var(--dur-fast) var(--ease-out)}
.diag.on .ln{stroke-dashoffset:0}
.diag .ln.acesa{stroke:var(--brand);stroke-width:1.6}
.diag .nd rect{fill:var(--color-ink-950);stroke:rgba(255,255,255,.12);transition:stroke var(--dur-fast) var(--ease-out)}
.diag .nd text{fill:var(--fg-muted);font-family:var(--font-mono);font-size:13px;letter-spacing:.04em;text-transform:uppercase}
.diag .nd:hover rect,.diag .nd.acesa rect{stroke:var(--brand)}
.diag .nd:hover text,.diag .nd.acesa text{fill:var(--fg)}
.diag .hub circle{fill:var(--brand)}
.diag .hub .anel{fill:none;stroke:rgba(0,172,229,.35);stroke-width:1}
.diag .hub text{fill:var(--on-brand);font-family:var(--font-sans);font-size:15px;font-weight:500}
.diag .tit{fill:var(--fg-subtle);font-family:var(--font-mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase}
.centro{display:flex;justify-content:center;margin-top:40px}

/* ---------- S10 · diferenciais (referência taskxen): grade 3 × 2 de ícone e texto ---------- */
.grade6{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));column-gap:72px;row-gap:56px}
.g6{display:flex;flex-direction:column;align-items:flex-start;gap:12px}
.g6 .cir{width:48px;height:48px;border-radius:50%;display:grid;place-items:center;margin-bottom:8px;background:radial-gradient(circle at 30% 25%,var(--color-ink-800),var(--color-ink-950) 70%);box-shadow:inset 0 0 0 1px rgba(255,255,255,.14);color:var(--brand);transition:background-color var(--dur-fast) var(--ease-out),color var(--dur-fast) var(--ease-out),box-shadow var(--dur-base) var(--ease-out)}
.g6 .cir .ico{width:20px;height:20px}
.g6:hover .cir{background:var(--brand);color:var(--on-brand);box-shadow:0 0 0 6px rgba(0,172,229,.12),0 0 28px -6px rgba(0,172,229,.7)}
.g6 b{font-weight:500;font-size:var(--text-h4);line-height:var(--text-h4--line-height)}
.g6 p{color:var(--fg-muted);font-size:var(--text-small)}

/* ---------- S07 · Sófi em operação (referência taskxen, depoimento fixo): o quadro fica parado e a rolagem troca as etapas ---------- */
.trilho{position:relative;height:300vh}
.pino{position:sticky;top:80px;height:calc(100vh - 80px);display:flex;align-items:center}
.pino .wrap{width:100%}
.sofi{align-items:center}
.sofi .l{grid-column:1/6;display:flex;flex-direction:column;align-items:flex-start;gap:20px}
.sofi .l > p{color:var(--fg-muted)}
.quem{display:flex;flex-wrap:wrap;gap:8px;margin-top:4px}
.quem span{height:32px;padding:0 14px;display:inline-flex;align-items:center;border-radius:var(--radius-pill);box-shadow:inset 0 0 0 1px var(--border);font-size:var(--text-caption);color:var(--fg-muted)}
.passos-s{display:flex;gap:8px;margin-top:8px}
.passos-s button{height:36px;padding:0 16px;border:0;border-radius:var(--radius-pill);background:none;box-shadow:inset 0 0 0 1px var(--border);font-size:var(--text-caption);color:var(--fg-muted);cursor:pointer;transition:background-color var(--dur-fast),color var(--dur-fast),box-shadow var(--dur-fast)}
.passos-s button[aria-current="true"]{background:var(--brand);color:var(--on-brand);box-shadow:none}
.fluxo-s{grid-column:7/13;padding:36px;display:grid;grid-template-columns:1fr auto 1fr auto 1fr;align-items:center;gap:16px;min-height:420px}
.fs-col{display:flex;flex-direction:column;gap:8px}
.fs-col .tag{margin-bottom:6px}
.fs-in{display:flex;align-items:center;gap:10px;height:40px;padding:0 14px;border-radius:var(--radius-pill);background:var(--color-ink-950);box-shadow:inset 0 0 0 1px rgba(255,255,255,.08);font-size:var(--text-small);color:var(--fg-subtle);transition:color var(--dur-base),box-shadow var(--dur-base)}
.fs-in .ico{width:14px;height:14px}
.fs-seta{color:var(--fg-subtle);transition:color var(--dur-base)}
.fs-seta .ico{width:18px;height:18px}
.fs-meio{display:grid;place-items:center;gap:10px;text-align:center;opacity:.35;transition:opacity var(--dur-base) var(--ease-out)}
.fs-meio .cir{width:72px;height:72px;border-radius:50%;display:grid;place-items:center;background:var(--color-ink-800);color:var(--fg-muted);box-shadow:inset 0 0 0 1px rgba(255,255,255,.14);transition:background-color var(--dur-base),color var(--dur-base),box-shadow var(--dur-base)}
.fs-meio .cir .ico{width:28px;height:28px}
.fs-meio b{font-weight:500}
.fluxo-s[data-p="0"] .fs-in,.fluxo-s[data-p="1"] .fs-in,.fluxo-s[data-p="2"] .fs-in{color:var(--fg);box-shadow:inset 0 0 0 1px rgba(0,172,229,.45)}
.fluxo-s[data-p="0"] .fs-in .ico{color:var(--brand)}
.fluxo-s[data-p="1"] .s1,.fluxo-s[data-p="2"] .s1,.fluxo-s[data-p="2"] .s2{opacity:1}
.fluxo-s[data-p="1"] .a1,.fluxo-s[data-p="2"] .a1,.fluxo-s[data-p="2"] .a2{color:var(--brand)}
.fluxo-s[data-p="1"] .s1 .cir,.fluxo-s[data-p="2"] .s2 .cir{background:var(--brand);color:var(--on-brand);box-shadow:0 0 0 8px rgba(0,172,229,.1),0 0 40px -6px rgba(0,172,229,.7)}
.fs-leg{grid-column:1/-1;text-align:center;color:var(--fg-muted);font-size:var(--text-small);min-height:1.5em}

/* ---------- S11 · CTA final (referência taskxen): selos, título e o formulário ---------- */
.selos{display:flex;justify-content:center;gap:10px;flex-wrap:wrap}
.selos span{display:inline-flex;align-items:center;gap:8px;height:32px;padding:0 14px;border-radius:var(--radius-pill);box-shadow:inset 0 0 0 1px var(--border);font-size:var(--text-caption);color:var(--fg-muted)}
.selos span .ico{width:13px;height:13px;color:var(--brand)}

'''

resp = r'''/* ---------- responsivo ---------- */
@media (max-width:1100px){
  .nav-links{display:none}
  .foot{grid-template-columns:1fr 1fr 1fr}
  .foot .brand{grid-column:1/-1}
  .hx-tit{grid-column:1/-1}
  .hx-dir{grid-column:1/8}
  .grade6{grid-template-columns:1fr 1fr;column-gap:48px}
  .fluxo-s{grid-template-columns:1fr;justify-items:stretch}
  .fs-seta{justify-self:center;transform:rotate(90deg)}
}
@media (max-width:960px){
  .c-ag .tx,.c-ag .vis,.c-ag.inv .tx,.c-ag.inv .vis,.sofi .l,.fluxo-s,.cf-t,.cf-v{grid-column:1/-1;grid-row:auto}
  .c-ag{padding:28px}
  .fluxo-s{margin-top:40px}
  .trilho{height:auto}
  .pino{position:relative;top:auto;height:auto;padding-block:var(--section-y)}
  .passos-s{display:none}
  .cf-v{margin-top:28px}
  .cf-p{padding:28px;min-height:0}
  .cf-nav{grid-template-columns:1fr 1fr;row-gap:28px}
  .cf-linha{display:none}
}
@media (max-width:640px){
  .nav-right .ai,.nav-right .btn{display:none}
  .menu-btn{display:inline-flex}
  .nav .wrap{gap:16px}
  .hx{min-height:0;padding-top:370px}
  .hx-dir{grid-column:1/-1}
  .hx-cantos{display:none}
  .grade6{grid-template-columns:1fr}
  .doc{grid-template-columns:1fr}
  .folha{display:none}
  .palco{padding:16px;min-height:0}
  .diag{padding:20px}
  .chips i{padding:0 10px}
  .form{padding:24px;grid-template-columns:1fr}
  .foot{grid-template-columns:1fr 1fr}
}
@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation:none!important;transition:none!important}
  .js .rv{opacity:1;transform:none}
  .msg,.campo{opacity:1;transform:none}
  .diag .ln{stroke-dashoffset:0}
}
</style></head><body>

<div class="texture" aria-hidden="true"><span class="lines"></span><span class="grain"></span></div>
<!--MENU-->

<main id="top">

'''

# ------------------------------------------------------------------ hero
LOGOS = [('mercantil', 'Banco Mercantil', 155), ('santander', 'Santander', 155), ('bs2', 'Banco BS2', 155), ('ole-consignado', 'Olé Consignado', 155), ('mrv', 'MRV Engenharia', 155),
         ('grupo-barigui', 'Grupo Barigui', 155), ('hexagon', 'Hexagon', 155), ('carbel', 'Carbel', 154), ('augusto-cury', 'Augusto Cury', 155)]
def logos(alt=True):
    return ''.join('<img src="../../assets/clientes/%s.png" alt="%s" width="%d" height="36" loading="lazy">' % (f, a if alt else '', w) for f, a, w in LOGOS)

hero = r'''<!-- S02 · Hero de página interna (referência aigentx): luz de cima, grade, título embaixo à esquerda, CTA à direita e clientes -->
<section class="hx" id="hero" aria-labelledby="thT">
  <div class="hx-luz" id="hxLuz" aria-hidden="true"></div>
  <div class="hx-grade" aria-hidden="true"></div>
  <canvas class="hx-esfera" id="esfera" aria-hidden="true"></canvas>
  <div class="hx-fundo" aria-hidden="true"></div>
  <div class="hx-cantos" aria-hidden="true"><div class="wrap"><i></i><i></i><i></i><i></i></div></div>
  <div class="wrap">
    <div class="g12 hx-txt">
      <div class="hx-tit rv">
        <span class="olho">Inteligência artificial · Rumo AI</span>
        <h1 class="h1 hx-h1" id="thT"><span class="ln">Não usamos IA.</span><span class="ln tone">Nós construímos com ela.</span></h1>
      </div>
      <div class="hx-dir rv">
        <p class="lead">Ecossistemas de agentes inteligentes construídos sob medida, que aprendem com os seus dados e seguem o seu processo.</p>
        <a class="btn btn-primary btn-luz" href="#proposta">Quero meu diagnóstico ''' + SETA + r'''</a>
      </div>
    </div>
    <div class="hx-conf rv">
      <div class="marquee" aria-label="Tecnologias"><div class="track"><div class="set"><span class="tech t-n8n"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21.4737 5.6842c-1.1772 0-2.1663.8051-2.4468 1.8947h-2.8955c-1.235 0-2.289.893-2.492 2.111l-.1038.623a1.263 1.263 0 0 1-1.246 1.0555H11.289c-.2805-1.0896-1.2696-1.8947-2.4468-1.8947s-2.1663.8051-2.4467 1.8947H4.973c-.2805-1.0896-1.2696-1.8947-2.4468-1.8947C1.1311 9.4737 0 10.6047 0 12s1.131 2.5263 2.5263 2.5263c1.1772 0 2.1663-.8051 2.4468-1.8947h1.4223c.2804 1.0896 1.2696 1.8947 2.4467 1.8947 1.1772 0 2.1663-.8051 2.4468-1.8947h1.0008a1.263 1.263 0 0 1 1.2459 1.0555l.1038.623c.203 1.218 1.257 2.111 2.492 2.111h.3692c.2804 1.0895 1.2696 1.8947 2.4468 1.8947 1.3952 0 2.5263-1.131 2.5263-2.5263s-1.131-2.5263-2.5263-2.5263c-1.1772 0-2.1664.805-2.4468 1.8947h-.3692a1.263 1.263 0 0 1-1.246-1.0555l-.1037-.623A2.52 2.52 0 0 0 13.9607 12a2.52 2.52 0 0 0 .821-1.4794l.1038-.623a1.263 1.263 0 0 1 1.2459-1.0555h2.8955c.2805 1.0896 1.2696 1.8947 2.4468 1.8947 1.3952 0 2.5263-1.131 2.5263-2.5263s-1.131-2.5263-2.5263-2.5263m0 1.2632a1.263 1.263 0 0 1 1.2631 1.2631 1.263 1.263 0 0 1-1.2631 1.2632 1.263 1.263 0 0 1-1.2632-1.2632 1.263 1.263 0 0 1 1.2632-1.2631M2.5263 10.7368A1.263 1.263 0 0 1 3.7895 12a1.263 1.263 0 0 1-1.2632 1.2632A1.263 1.263 0 0 1 1.2632 12a1.263 1.263 0 0 1 1.2631-1.2632m6.3158 0A1.263 1.263 0 0 1 10.1053 12a1.263 1.263 0 0 1-1.2632 1.2632A1.263 1.263 0 0 1 7.579 12a1.263 1.263 0 0 1 1.2632-1.2632m10.1053 3.7895a1.263 1.263 0 0 1 1.2631 1.2632 1.263 1.263 0 0 1-1.2631 1.2631 1.263 1.263 0 0 1-1.2632-1.2631 1.263 1.263 0 0 1 1.2632-1.2632"/></svg>n8n</span><span class="tech t-googledrive"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.01 1.485c-2.082 0-3.754.02-3.743.047.01.02 1.708 3.001 3.774 6.62l3.76 6.574h3.76c2.081 0 3.753-.02 3.742-.047-.005-.02-1.708-3.001-3.775-6.62l-3.76-6.574zm-4.76 1.73a789.828 789.861 0 0 0-3.63 6.319L0 15.868l1.89 3.298 1.885 3.297 3.62-6.335 3.618-6.33-1.88-3.287C8.1 4.704 7.255 3.22 7.25 3.214zm2.259 12.653-.203.348c-.114.198-.96 1.672-1.88 3.287a423.93 423.948 0 0 1-1.698 2.97c-.01.026 3.24.042 7.222.042h7.244l1.796-3.157c.992-1.734 1.85-3.23 1.906-3.323l.104-.167h-7.249z"/></svg>Google Drive</span><span class="tech t-json"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.043 23.968c.479-.004.953-.029 1.426-.094a11.805 11.805 0 003.146-.863 12.404 12.404 0 003.793-2.542 11.977 11.977 0 002.44-3.427 11.794 11.794 0 001.02-3.476c.149-1.16.135-2.346-.045-3.499a11.96 11.96 0 00-.793-2.788 11.197 11.197 0 00-.854-1.617c-1.168-1.837-2.861-3.314-4.81-4.3a12.835 12.835 0 00-2.172-.87h-.005c.119.063.24.132.345.201.12.074.239.146.351.225a8.93 8.93 0 011.559 1.33c1.063 1.145 1.797 2.548 2.218 4.041.284.982.434 1.998.495 3.017.044.743.044 1.491-.047 2.229-.149 1.27-.554 2.51-1.228 3.596a7.475 7.475 0 01-1.903 2.084c-1.244.928-2.877 1.482-4.436 1.114a3.916 3.916 0 01-.748-.258 4.692 4.692 0 01-.779-.45 6.08 6.08 0 01-1.244-1.105 6.507 6.507 0 01-1.049-1.747 7.366 7.366 0 01-.494-2.54c-.03-1.273.225-2.553.854-3.67a6.43 6.43 0 011.663-1.918c.225-.178.464-.333.704-.479l.016-.007a5.121 5.121 0 00-1.441-.12 4.963 4.963 0 00-1.228.24c-.359.12-.704.27-1.019.45a6.146 6.146 0 00-.733.494c-.211.18-.42.36-.615.555-1.123 1.153-1.768 2.682-2.022 4.256-.15.973-.15 1.96-.091 2.95.105 1.395.391 2.787.945 4.062a8.518 8.518 0 001.348 2.173 8.14 8.14 0 003.132 2.23 7.934 7.934 0 002.113.54c.074.015.149.015.209.015zm-2.934-.398a4.102 4.102 0 01-.45-.228 8.5 8.5 0 01-2.038-1.534c-1.094-1.137-1.827-2.566-2.247-4.08a15.184 15.184 0 01-.495-3.172 12.14 12.14 0 01.046-2.082c.135-1.257.495-2.501 1.124-3.58a6.889 6.889 0 011.783-2.053 6.23 6.23 0 011.633-.9 5.363 5.363 0 013.522-.045c.029 0 .029 0 .045.03.015.015.045.015.06.03.045.016.104.045.165.074.239.12.479.271.704.42a6.294 6.294 0 012.097 2.502c.42.914.615 1.934.631 2.938.014 1.079-.18 2.157-.645 3.146a6.42 6.42 0 01-2.638 2.832c.09.03.18.045.271.075.225.044.449.074.688.074 1.468.045 2.892-.66 3.94-1.647.195-.18.375-.375.54-.585.225-.27.435-.54.614-.823.239-.375.435-.75.614-1.154a8.112 8.112 0 00.509-1.664c.196-1.004.211-2.022.149-3.026-.135-2.022-.673-4.045-1.842-5.724a9.054 9.054 0 00-.555-.719 9.868 9.868 0 00-1.063-1.034 8.477 8.477 0 00-1.363-.915 9.927 9.927 0 00-1.692-.598l-.3-.06c-.209-.03-.42-.044-.634-.06a8.453 8.453 0 00-1.015.016c-.704.045-1.412.16-2.112.337C5.799 1.227 2.863 3.566 1.3 6.67A11.834 11.834 0 00.238 9.801a11.81 11.81 0 00-.104 3.775c.12 1.02.374 2.023.778 2.977.227.57.511 1.124.825 1.648 1.094 1.783 2.683 3.236 4.51 4.24.688.39 1.408.69 2.157.944.226.074.45.15.689.21z"/></svg>JSON</span><span class="tech t-gemini"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11.04 19.32Q12 21.51 12 24q0-2.49.93-4.68.96-2.19 2.58-3.81t3.81-2.55Q21.51 12 24 12q-2.49 0-4.68-.93a12.3 12.3 0 0 1-3.81-2.58 12.3 12.3 0 0 1-2.58-3.81Q12 2.49 12 0q0 2.49-.96 4.68-.93 2.19-2.55 3.81a12.3 12.3 0 0 1-3.81 2.58Q2.49 12 0 12q2.49 0 4.68.96 2.19.93 3.81 2.55t2.55 3.81"/></svg>Gemini</span><span class="tech t-chatgpt"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z"/></svg>ChatGPT</span><span class="tech t-outlook"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7.88 12.04q0 .45-.11.87-.1.41-.33.74-.22.33-.58.52-.37.2-.87.2t-.85-.2q-.35-.21-.57-.55-.22-.33-.33-.75-.1-.42-.1-.86t.1-.87q.1-.43.34-.76.22-.34.59-.54.36-.2.87-.2t.86.2q.35.21.57.55.22.34.31.77.1.43.1.88zM24 12v9.38q0 .46-.33.8-.33.32-.8.32H7.13q-.46 0-.8-.33-.32-.33-.32-.8V18H1q-.41 0-.7-.3-.3-.29-.3-.7V7q0-.41.3-.7Q.58 6 1 6h6.5V2.55q0-.44.3-.75.3-.3.75-.3h12.9q.44 0 .75.3.3.3.3.75V10.85l1.24.72h.01q.1.07.18.18.07.12.07.25zm-6-8.25v3h3v-3zm0 4.5v3h3v-3zm0 4.5v1.83l3.05-1.83zm-5.25-9v3h3.75v-3zm0 4.5v3h3.75v-3zm0 4.5v2.03l2.41 1.5 1.34-.8v-2.73zM9 3.75V6h2l.13.01.12.04v-2.3zM5.98 15.98q.9 0 1.6-.3.7-.32 1.19-.86.48-.55.73-1.28.25-.74.25-1.61 0-.83-.25-1.55-.24-.71-.71-1.24t-1.15-.83q-.68-.3-1.55-.3-.92 0-1.64.3-.71.3-1.2.85-.5.54-.75 1.3-.25.74-.25 1.63 0 .85.26 1.56.26.72.74 1.23.48.52 1.17.81.69.3 1.56.3zM7.5 21h12.39L12 16.08V17q0 .41-.3.7-.29.3-.7.3H7.5zm15-.13v-7.24l-5.9 3.54Z"/></svg>Outlook</span><span class="tech t-deepseek"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M23.748 4.651c-.254-.124-.364.113-.512.233-.051.04-.094.09-.137.137-.372.397-.806.657-1.373.626-.829-.046-1.537.214-2.163.848-.133-.782-.575-1.248-1.247-1.548-.352-.155-.708-.311-.955-.65-.172-.24-.219-.509-.305-.774-.055-.16-.11-.323-.293-.35-.2-.031-.278.136-.356.276-.313.572-.434 1.202-.422 1.84.027 1.436.633 2.58 1.838 3.393.137.094.172.187.129.323-.082.28-.18.553-.266.833-.055.179-.137.218-.328.14a5.5 5.5 0 0 1-1.737-1.179c-.857-.828-1.631-1.743-2.597-2.46a12 12 0 0 0-.689-.47c-.985-.957.13-1.743.387-1.836.27-.098.094-.433-.778-.428-.872.003-1.67.295-2.687.685a3 3 0 0 1-.465.136 9.6 9.6 0 0 0-2.883-.101c-1.885.21-3.39 1.1-4.497 2.622C.082 8.776-.231 10.854.152 13.02c.403 2.284 1.568 4.175 3.36 5.653 1.857 1.533 3.997 2.284 6.438 2.14 1.482-.085 3.132-.284 4.994-1.86.47.234.962.328 1.78.398.629.058 1.235-.031 1.705-.129.735-.155.684-.836.418-.961-2.155-1.004-1.682-.595-2.112-.926 1.095-1.295 2.768-3.598 3.284-6.733.05-.346.115-.834.108-1.114-.004-.171.035-.238.23-.257a4.2 4.2 0 0 0 1.545-.475c1.397-.763 1.96-2.016 2.093-3.517.02-.23-.004-.467-.247-.588M11.58 18.168c-2.088-1.642-3.101-2.183-3.52-2.16-.39.024-.32.472-.234.763.09.288.207.487.371.74.114.167.192.416-.113.603-.673.416-1.842-.14-1.897-.168-1.361-.801-2.5-1.86-3.301-3.306-.775-1.393-1.225-2.888-1.299-4.482-.02-.385.094-.522.477-.592a4.7 4.7 0 0 1 1.53-.038c2.131.311 3.946 1.264 5.467 2.774.868.86 1.525 1.887 2.202 2.89.72 1.066 1.494 2.082 2.48 2.915.348.291.626.513.892.677-.802.09-2.14.109-3.055-.615zm1.001-6.44a.306.306 0 0 1 .415-.287.3.3 0 0 1 .113.074.3.3 0 0 1 .086.214c0 .17-.136.307-.308.307a.303.303 0 0 1-.306-.307m3.11 1.596c-.2.081-.4.151-.591.16a1.25 1.25 0 0 1-.798-.254c-.274-.23-.47-.358-.551-.758a1.7 1.7 0 0 1 .015-.588c.07-.327-.007-.537-.238-.727-.188-.156-.426-.199-.689-.199a.6.6 0 0 1-.254-.078.253.253 0 0 1-.114-.358 1 1 0 0 1 .192-.21c.356-.202.767-.136 1.146.016.352.144.618.408 1.001.782.392.451.462.576.685.915.176.264.336.536.446.848.066.194-.02.353-.25.45"/></svg>DeepSeek</span><span class="tech t-github"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>GitHub</span><span class="tech t-aws"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.763 10.036c0 .296.032.535.088.71.064.176.144.368.256.576.04.063.056.127.056.183 0 .08-.048.16-.152.24l-.503.335a.383.383 0 0 1-.208.072c-.08 0-.16-.04-.239-.112a2.47 2.47 0 0 1-.287-.375 6.18 6.18 0 0 1-.248-.471c-.622.734-1.405 1.101-2.347 1.101-.67 0-1.205-.191-1.596-.574-.391-.384-.59-.894-.59-1.533 0-.678.239-1.23.726-1.644.487-.415 1.133-.623 1.955-.623.272 0 .551.024.846.064.296.04.6.104.918.176v-.583c0-.607-.127-1.03-.375-1.277-.255-.248-.686-.367-1.3-.367-.28 0-.568.031-.863.103-.295.072-.583.16-.862.272a2.287 2.287 0 0 1-.28.104.488.488 0 0 1-.127.023c-.112 0-.168-.08-.168-.247v-.391c0-.128.016-.224.056-.28a.597.597 0 0 1 .224-.167c.279-.144.614-.264 1.005-.36a4.84 4.84 0 0 1 1.246-.151c.95 0 1.644.216 2.091.647.439.43.662 1.085.662 1.963v2.586zm-3.24 1.214c.263 0 .534-.048.822-.144.287-.096.543-.271.758-.51.128-.152.224-.32.272-.512.047-.191.08-.423.08-.694v-.335a6.66 6.66 0 0 0-.735-.136 6.02 6.02 0 0 0-.75-.048c-.535 0-.926.104-1.19.32-.263.215-.39.518-.39.917 0 .375.095.655.295.846.191.2.47.296.838.296zm6.41.862c-.144 0-.24-.024-.304-.08-.064-.048-.12-.16-.168-.311L7.586 5.55a1.398 1.398 0 0 1-.072-.32c0-.128.064-.2.191-.2h.783c.151 0 .255.025.31.08.065.048.113.16.16.312l1.342 5.284 1.245-5.284c.04-.16.088-.264.151-.312a.549.549 0 0 1 .32-.08h.638c.152 0 .256.025.32.08.063.048.12.16.151.312l1.261 5.348 1.381-5.348c.048-.16.104-.264.16-.312a.52.52 0 0 1 .311-.08h.743c.127 0 .2.065.2.2 0 .04-.009.08-.017.128a1.137 1.137 0 0 1-.056.2l-1.923 6.17c-.048.16-.104.263-.168.311a.51.51 0 0 1-.303.08h-.687c-.151 0-.255-.024-.32-.08-.063-.056-.119-.16-.15-.32l-1.238-5.148-1.23 5.14c-.04.16-.087.264-.15.32-.065.056-.177.08-.32.08zm10.256.215c-.415 0-.83-.048-1.229-.143-.399-.096-.71-.2-.918-.32-.128-.071-.215-.151-.247-.223a.563.563 0 0 1-.048-.224v-.407c0-.167.064-.247.183-.247.048 0 .096.008.144.024.048.016.12.048.2.08.271.12.566.215.878.279.319.064.63.096.95.096.502 0 .894-.088 1.165-.264a.86.86 0 0 0 .415-.758.777.777 0 0 0-.215-.559c-.144-.151-.416-.287-.807-.415l-1.157-.36c-.583-.183-1.014-.454-1.277-.813a1.902 1.902 0 0 1-.4-1.158c0-.335.073-.63.216-.886.144-.255.335-.479.575-.654.24-.184.51-.32.83-.415.32-.096.655-.136 1.006-.136.175 0 .359.008.535.032.183.024.35.056.518.088.16.04.312.08.455.127.144.048.256.096.336.144a.69.69 0 0 1 .24.2.43.43 0 0 1 .071.263v.375c0 .168-.064.256-.184.256a.83.83 0 0 1-.303-.096 3.652 3.652 0 0 0-1.532-.311c-.455 0-.815.071-1.062.223-.248.152-.375.383-.375.71 0 .224.08.416.24.567.159.152.454.304.877.44l1.134.358c.574.184.99.44 1.237.767.247.327.367.702.367 1.117 0 .343-.072.655-.207.926-.144.272-.336.511-.583.703-.248.2-.543.343-.886.447-.36.111-.734.167-1.142.167zM21.698 16.207c-2.626 1.94-6.442 2.969-9.722 2.969-4.598 0-8.74-1.7-11.87-4.526-.247-.223-.024-.527.272-.351 3.384 1.963 7.559 3.153 11.877 3.153 2.914 0 6.114-.607 9.06-1.852.439-.2.814.287.383.607zM22.792 14.961c-.336-.43-2.22-.207-3.074-.103-.255.032-.295-.192-.063-.36 1.5-1.053 3.967-.75 4.254-.399.287.36-.08 2.826-1.485 4.007-.215.184-.423.088-.327-.151.32-.79 1.03-2.57.695-2.994z"/></svg>AWS</span><span class="tech t-claude"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m4.7144 15.9555 4.7174-2.6471.079-.2307-.079-.1275h-.2307l-.7893-.0486-2.6956-.0729-2.3375-.0971-2.2646-.1214-.5707-.1215-.5343-.7042.0546-.3522.4797-.3218.686.0608 1.5179.1032 2.2767.1578 1.6514.0972 2.4468.255h.3886l.0546-.1579-.1336-.0971-.1032-.0972L6.973 9.8356l-2.55-1.6879-1.3356-.9714-.7225-.4918-.3643-.4614-.1578-1.0078.6557-.7225.8803.0607.2246.0607.8925.686 1.9064 1.4754 2.4893 1.8336.3643.3035.1457-.1032.0182-.0728-.164-.2733-1.3539-2.4467-1.445-2.4893-.6435-1.032-.17-.6194c-.0607-.255-.1032-.4674-.1032-.7285L6.287.1335 6.6997 0l.9957.1336.419.3642.6192 1.4147 1.0018 2.2282 1.5543 3.0296.4553.8985.2429.8318.091.255h.1579v-.1457l.1275-1.706.2368-2.0947.2307-2.6957.0789-.7589.3764-.9107.7468-.4918.5828.2793.4797.686-.0668.4433-.2853 1.8517-.5586 2.9021-.3643 1.9429h.2125l.2429-.2429.9835-1.3053 1.6514-2.0643.7286-.8196.85-.9046.5464-.4311h1.0321l.759 1.1293-.34 1.1657-1.0625 1.3478-.8804 1.1414-1.2628 1.7-.7893 1.36.0729.1093.1882-.0183 2.8535-.607 1.5421-.2794 1.8396-.3157.8318.3886.091.3946-.3278.8075-1.967.4857-2.3072.4614-3.4364.8136-.0425.0304.0486.0607 1.5482.1457.6618.0364h1.621l3.0175.2247.7892.522.4736.6376-.079.4857-1.2142.6193-1.6393-.3886-3.825-.9107-1.3113-.3279h-.1822v.1093l1.0929 1.0686 2.0035 1.8092 2.5075 2.3314.1275.5768-.3218.4554-.34-.0486-2.2039-1.6575-.85-.7468-1.9246-1.621h-.1275v.17l.4432.6496 2.3436 3.5214.1214 1.0807-.17.3521-.6071.2125-.6679-.1214-1.3721-1.9246L14.38 17.959l-1.1414-1.9428-.1397.079-.674 7.2552-.3156.3703-.7286.2793-.6071-.4614-.3218-.7468.3218-1.4753.3886-1.9246.3157-1.53.2853-1.9004.17-.6314-.0121-.0425-.1397.0182-1.4328 1.9672-2.1796 2.9446-1.7243 1.8456-.4128.164-.7164-.3704.0667-.6618.4008-.5889 2.386-3.0357 1.4389-1.882.929-1.0868-.0062-.1579h-.0546l-6.3385 4.1164-1.1293.1457-.4857-.4554.0608-.7467.2307-.2429 1.9064-1.3114Z"/></svg>Claude Code</span><span class="tech t-copilot"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M23.922 16.997C23.061 18.492 18.063 22.02 12 22.02 5.937 22.02.939 18.492.078 16.997A.641.641 0 0 1 0 16.741v-2.869a.883.883 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.098 10.098 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952C7.255 2.937 9.248 1.98 11.978 1.98c2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.841.841 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256Zm-11.75-5.992h-.344a4.359 4.359 0 0 1-.355.508c-.77.947-1.918 1.492-3.508 1.492-1.725 0-2.989-.359-3.782-1.259a2.137 2.137 0 0 1-.085-.104L4 11.746v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.359 4.359 0 0 1-.355-.508Zm2.328 3.25c.549 0 1 .451 1 1v2c0 .549-.451 1-1 1-.549 0-1-.451-1-1v-2c0-.549.451-1 1-1Zm-5 0c.549 0 1 .451 1 1v2c0 .549-.451 1-1 1-.549 0-1-.451-1-1v-2c0-.549.451-1 1-1Zm3.313-6.185c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"/></svg>GitHub Copilot</span><span class="tech t-cursor"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11.503.131 1.891 5.678a.84.84 0 0 0-.42.726v11.188c0 .3.162.575.42.724l9.609 5.55a1 1 0 0 0 .998 0l9.61-5.55a.84.84 0 0 0 .42-.724V6.404a.84.84 0 0 0-.42-.726L12.497.131a1.01 1.01 0 0 0-.996 0M2.657 6.338h18.55c.263 0 .43.287.297.515L12.23 22.918c-.062.107-.229.064-.229-.06V12.335a.59.59 0 0 0-.295-.51l-9.11-5.257c-.109-.063-.064-.23.061-.23"/></svg>Cursor</span></div><div class="set" aria-hidden="true"><span class="tech t-n8n"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21.4737 5.6842c-1.1772 0-2.1663.8051-2.4468 1.8947h-2.8955c-1.235 0-2.289.893-2.492 2.111l-.1038.623a1.263 1.263 0 0 1-1.246 1.0555H11.289c-.2805-1.0896-1.2696-1.8947-2.4468-1.8947s-2.1663.8051-2.4467 1.8947H4.973c-.2805-1.0896-1.2696-1.8947-2.4468-1.8947C1.1311 9.4737 0 10.6047 0 12s1.131 2.5263 2.5263 2.5263c1.1772 0 2.1663-.8051 2.4468-1.8947h1.4223c.2804 1.0896 1.2696 1.8947 2.4467 1.8947 1.1772 0 2.1663-.8051 2.4468-1.8947h1.0008a1.263 1.263 0 0 1 1.2459 1.0555l.1038.623c.203 1.218 1.257 2.111 2.492 2.111h.3692c.2804 1.0895 1.2696 1.8947 2.4468 1.8947 1.3952 0 2.5263-1.131 2.5263-2.5263s-1.131-2.5263-2.5263-2.5263c-1.1772 0-2.1664.805-2.4468 1.8947h-.3692a1.263 1.263 0 0 1-1.246-1.0555l-.1037-.623A2.52 2.52 0 0 0 13.9607 12a2.52 2.52 0 0 0 .821-1.4794l.1038-.623a1.263 1.263 0 0 1 1.2459-1.0555h2.8955c.2805 1.0896 1.2696 1.8947 2.4468 1.8947 1.3952 0 2.5263-1.131 2.5263-2.5263s-1.131-2.5263-2.5263-2.5263m0 1.2632a1.263 1.263 0 0 1 1.2631 1.2631 1.263 1.263 0 0 1-1.2631 1.2632 1.263 1.263 0 0 1-1.2632-1.2632 1.263 1.263 0 0 1 1.2632-1.2631M2.5263 10.7368A1.263 1.263 0 0 1 3.7895 12a1.263 1.263 0 0 1-1.2632 1.2632A1.263 1.263 0 0 1 1.2632 12a1.263 1.263 0 0 1 1.2631-1.2632m6.3158 0A1.263 1.263 0 0 1 10.1053 12a1.263 1.263 0 0 1-1.2632 1.2632A1.263 1.263 0 0 1 7.579 12a1.263 1.263 0 0 1 1.2632-1.2632m10.1053 3.7895a1.263 1.263 0 0 1 1.2631 1.2632 1.263 1.263 0 0 1-1.2631 1.2631 1.263 1.263 0 0 1-1.2632-1.2631 1.263 1.263 0 0 1 1.2632-1.2632"/></svg>n8n</span><span class="tech t-googledrive"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.01 1.485c-2.082 0-3.754.02-3.743.047.01.02 1.708 3.001 3.774 6.62l3.76 6.574h3.76c2.081 0 3.753-.02 3.742-.047-.005-.02-1.708-3.001-3.775-6.62l-3.76-6.574zm-4.76 1.73a789.828 789.861 0 0 0-3.63 6.319L0 15.868l1.89 3.298 1.885 3.297 3.62-6.335 3.618-6.33-1.88-3.287C8.1 4.704 7.255 3.22 7.25 3.214zm2.259 12.653-.203.348c-.114.198-.96 1.672-1.88 3.287a423.93 423.948 0 0 1-1.698 2.97c-.01.026 3.24.042 7.222.042h7.244l1.796-3.157c.992-1.734 1.85-3.23 1.906-3.323l.104-.167h-7.249z"/></svg>Google Drive</span><span class="tech t-json"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.043 23.968c.479-.004.953-.029 1.426-.094a11.805 11.805 0 003.146-.863 12.404 12.404 0 003.793-2.542 11.977 11.977 0 002.44-3.427 11.794 11.794 0 001.02-3.476c.149-1.16.135-2.346-.045-3.499a11.96 11.96 0 00-.793-2.788 11.197 11.197 0 00-.854-1.617c-1.168-1.837-2.861-3.314-4.81-4.3a12.835 12.835 0 00-2.172-.87h-.005c.119.063.24.132.345.201.12.074.239.146.351.225a8.93 8.93 0 011.559 1.33c1.063 1.145 1.797 2.548 2.218 4.041.284.982.434 1.998.495 3.017.044.743.044 1.491-.047 2.229-.149 1.27-.554 2.51-1.228 3.596a7.475 7.475 0 01-1.903 2.084c-1.244.928-2.877 1.482-4.436 1.114a3.916 3.916 0 01-.748-.258 4.692 4.692 0 01-.779-.45 6.08 6.08 0 01-1.244-1.105 6.507 6.507 0 01-1.049-1.747 7.366 7.366 0 01-.494-2.54c-.03-1.273.225-2.553.854-3.67a6.43 6.43 0 011.663-1.918c.225-.178.464-.333.704-.479l.016-.007a5.121 5.121 0 00-1.441-.12 4.963 4.963 0 00-1.228.24c-.359.12-.704.27-1.019.45a6.146 6.146 0 00-.733.494c-.211.18-.42.36-.615.555-1.123 1.153-1.768 2.682-2.022 4.256-.15.973-.15 1.96-.091 2.95.105 1.395.391 2.787.945 4.062a8.518 8.518 0 001.348 2.173 8.14 8.14 0 003.132 2.23 7.934 7.934 0 002.113.54c.074.015.149.015.209.015zm-2.934-.398a4.102 4.102 0 01-.45-.228 8.5 8.5 0 01-2.038-1.534c-1.094-1.137-1.827-2.566-2.247-4.08a15.184 15.184 0 01-.495-3.172 12.14 12.14 0 01.046-2.082c.135-1.257.495-2.501 1.124-3.58a6.889 6.889 0 011.783-2.053 6.23 6.23 0 011.633-.9 5.363 5.363 0 013.522-.045c.029 0 .029 0 .045.03.015.015.045.015.06.03.045.016.104.045.165.074.239.12.479.271.704.42a6.294 6.294 0 012.097 2.502c.42.914.615 1.934.631 2.938.014 1.079-.18 2.157-.645 3.146a6.42 6.42 0 01-2.638 2.832c.09.03.18.045.271.075.225.044.449.074.688.074 1.468.045 2.892-.66 3.94-1.647.195-.18.375-.375.54-.585.225-.27.435-.54.614-.823.239-.375.435-.75.614-1.154a8.112 8.112 0 00.509-1.664c.196-1.004.211-2.022.149-3.026-.135-2.022-.673-4.045-1.842-5.724a9.054 9.054 0 00-.555-.719 9.868 9.868 0 00-1.063-1.034 8.477 8.477 0 00-1.363-.915 9.927 9.927 0 00-1.692-.598l-.3-.06c-.209-.03-.42-.044-.634-.06a8.453 8.453 0 00-1.015.016c-.704.045-1.412.16-2.112.337C5.799 1.227 2.863 3.566 1.3 6.67A11.834 11.834 0 00.238 9.801a11.81 11.81 0 00-.104 3.775c.12 1.02.374 2.023.778 2.977.227.57.511 1.124.825 1.648 1.094 1.783 2.683 3.236 4.51 4.24.688.39 1.408.69 2.157.944.226.074.45.15.689.21z"/></svg>JSON</span><span class="tech t-gemini"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11.04 19.32Q12 21.51 12 24q0-2.49.93-4.68.96-2.19 2.58-3.81t3.81-2.55Q21.51 12 24 12q-2.49 0-4.68-.93a12.3 12.3 0 0 1-3.81-2.58 12.3 12.3 0 0 1-2.58-3.81Q12 2.49 12 0q0 2.49-.96 4.68-.93 2.19-2.55 3.81a12.3 12.3 0 0 1-3.81 2.58Q2.49 12 0 12q2.49 0 4.68.96 2.19.93 3.81 2.55t2.55 3.81"/></svg>Gemini</span><span class="tech t-chatgpt"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z"/></svg>ChatGPT</span><span class="tech t-outlook"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7.88 12.04q0 .45-.11.87-.1.41-.33.74-.22.33-.58.52-.37.2-.87.2t-.85-.2q-.35-.21-.57-.55-.22-.33-.33-.75-.1-.42-.1-.86t.1-.87q.1-.43.34-.76.22-.34.59-.54.36-.2.87-.2t.86.2q.35.21.57.55.22.34.31.77.1.43.1.88zM24 12v9.38q0 .46-.33.8-.33.32-.8.32H7.13q-.46 0-.8-.33-.32-.33-.32-.8V18H1q-.41 0-.7-.3-.3-.29-.3-.7V7q0-.41.3-.7Q.58 6 1 6h6.5V2.55q0-.44.3-.75.3-.3.75-.3h12.9q.44 0 .75.3.3.3.3.75V10.85l1.24.72h.01q.1.07.18.18.07.12.07.25zm-6-8.25v3h3v-3zm0 4.5v3h3v-3zm0 4.5v1.83l3.05-1.83zm-5.25-9v3h3.75v-3zm0 4.5v3h3.75v-3zm0 4.5v2.03l2.41 1.5 1.34-.8v-2.73zM9 3.75V6h2l.13.01.12.04v-2.3zM5.98 15.98q.9 0 1.6-.3.7-.32 1.19-.86.48-.55.73-1.28.25-.74.25-1.61 0-.83-.25-1.55-.24-.71-.71-1.24t-1.15-.83q-.68-.3-1.55-.3-.92 0-1.64.3-.71.3-1.2.85-.5.54-.75 1.3-.25.74-.25 1.63 0 .85.26 1.56.26.72.74 1.23.48.52 1.17.81.69.3 1.56.3zM7.5 21h12.39L12 16.08V17q0 .41-.3.7-.29.3-.7.3H7.5zm15-.13v-7.24l-5.9 3.54Z"/></svg>Outlook</span><span class="tech t-deepseek"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M23.748 4.651c-.254-.124-.364.113-.512.233-.051.04-.094.09-.137.137-.372.397-.806.657-1.373.626-.829-.046-1.537.214-2.163.848-.133-.782-.575-1.248-1.247-1.548-.352-.155-.708-.311-.955-.65-.172-.24-.219-.509-.305-.774-.055-.16-.11-.323-.293-.35-.2-.031-.278.136-.356.276-.313.572-.434 1.202-.422 1.84.027 1.436.633 2.58 1.838 3.393.137.094.172.187.129.323-.082.28-.18.553-.266.833-.055.179-.137.218-.328.14a5.5 5.5 0 0 1-1.737-1.179c-.857-.828-1.631-1.743-2.597-2.46a12 12 0 0 0-.689-.47c-.985-.957.13-1.743.387-1.836.27-.098.094-.433-.778-.428-.872.003-1.67.295-2.687.685a3 3 0 0 1-.465.136 9.6 9.6 0 0 0-2.883-.101c-1.885.21-3.39 1.1-4.497 2.622C.082 8.776-.231 10.854.152 13.02c.403 2.284 1.568 4.175 3.36 5.653 1.857 1.533 3.997 2.284 6.438 2.14 1.482-.085 3.132-.284 4.994-1.86.47.234.962.328 1.78.398.629.058 1.235-.031 1.705-.129.735-.155.684-.836.418-.961-2.155-1.004-1.682-.595-2.112-.926 1.095-1.295 2.768-3.598 3.284-6.733.05-.346.115-.834.108-1.114-.004-.171.035-.238.23-.257a4.2 4.2 0 0 0 1.545-.475c1.397-.763 1.96-2.016 2.093-3.517.02-.23-.004-.467-.247-.588M11.58 18.168c-2.088-1.642-3.101-2.183-3.52-2.16-.39.024-.32.472-.234.763.09.288.207.487.371.74.114.167.192.416-.113.603-.673.416-1.842-.14-1.897-.168-1.361-.801-2.5-1.86-3.301-3.306-.775-1.393-1.225-2.888-1.299-4.482-.02-.385.094-.522.477-.592a4.7 4.7 0 0 1 1.53-.038c2.131.311 3.946 1.264 5.467 2.774.868.86 1.525 1.887 2.202 2.89.72 1.066 1.494 2.082 2.48 2.915.348.291.626.513.892.677-.802.09-2.14.109-3.055-.615zm1.001-6.44a.306.306 0 0 1 .415-.287.3.3 0 0 1 .113.074.3.3 0 0 1 .086.214c0 .17-.136.307-.308.307a.303.303 0 0 1-.306-.307m3.11 1.596c-.2.081-.4.151-.591.16a1.25 1.25 0 0 1-.798-.254c-.274-.23-.47-.358-.551-.758a1.7 1.7 0 0 1 .015-.588c.07-.327-.007-.537-.238-.727-.188-.156-.426-.199-.689-.199a.6.6 0 0 1-.254-.078.253.253 0 0 1-.114-.358 1 1 0 0 1 .192-.21c.356-.202.767-.136 1.146.016.352.144.618.408 1.001.782.392.451.462.576.685.915.176.264.336.536.446.848.066.194-.02.353-.25.45"/></svg>DeepSeek</span><span class="tech t-github"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>GitHub</span><span class="tech t-aws"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.763 10.036c0 .296.032.535.088.71.064.176.144.368.256.576.04.063.056.127.056.183 0 .08-.048.16-.152.24l-.503.335a.383.383 0 0 1-.208.072c-.08 0-.16-.04-.239-.112a2.47 2.47 0 0 1-.287-.375 6.18 6.18 0 0 1-.248-.471c-.622.734-1.405 1.101-2.347 1.101-.67 0-1.205-.191-1.596-.574-.391-.384-.59-.894-.59-1.533 0-.678.239-1.23.726-1.644.487-.415 1.133-.623 1.955-.623.272 0 .551.024.846.064.296.04.6.104.918.176v-.583c0-.607-.127-1.03-.375-1.277-.255-.248-.686-.367-1.3-.367-.28 0-.568.031-.863.103-.295.072-.583.16-.862.272a2.287 2.287 0 0 1-.28.104.488.488 0 0 1-.127.023c-.112 0-.168-.08-.168-.247v-.391c0-.128.016-.224.056-.28a.597.597 0 0 1 .224-.167c.279-.144.614-.264 1.005-.36a4.84 4.84 0 0 1 1.246-.151c.95 0 1.644.216 2.091.647.439.43.662 1.085.662 1.963v2.586zm-3.24 1.214c.263 0 .534-.048.822-.144.287-.096.543-.271.758-.51.128-.152.224-.32.272-.512.047-.191.08-.423.08-.694v-.335a6.66 6.66 0 0 0-.735-.136 6.02 6.02 0 0 0-.75-.048c-.535 0-.926.104-1.19.32-.263.215-.39.518-.39.917 0 .375.095.655.295.846.191.2.47.296.838.296zm6.41.862c-.144 0-.24-.024-.304-.08-.064-.048-.12-.16-.168-.311L7.586 5.55a1.398 1.398 0 0 1-.072-.32c0-.128.064-.2.191-.2h.783c.151 0 .255.025.31.08.065.048.113.16.16.312l1.342 5.284 1.245-5.284c.04-.16.088-.264.151-.312a.549.549 0 0 1 .32-.08h.638c.152 0 .256.025.32.08.063.048.12.16.151.312l1.261 5.348 1.381-5.348c.048-.16.104-.264.16-.312a.52.52 0 0 1 .311-.08h.743c.127 0 .2.065.2.2 0 .04-.009.08-.017.128a1.137 1.137 0 0 1-.056.2l-1.923 6.17c-.048.16-.104.263-.168.311a.51.51 0 0 1-.303.08h-.687c-.151 0-.255-.024-.32-.08-.063-.056-.119-.16-.15-.32l-1.238-5.148-1.23 5.14c-.04.16-.087.264-.15.32-.065.056-.177.08-.32.08zm10.256.215c-.415 0-.83-.048-1.229-.143-.399-.096-.71-.2-.918-.32-.128-.071-.215-.151-.247-.223a.563.563 0 0 1-.048-.224v-.407c0-.167.064-.247.183-.247.048 0 .096.008.144.024.048.016.12.048.2.08.271.12.566.215.878.279.319.064.63.096.95.096.502 0 .894-.088 1.165-.264a.86.86 0 0 0 .415-.758.777.777 0 0 0-.215-.559c-.144-.151-.416-.287-.807-.415l-1.157-.36c-.583-.183-1.014-.454-1.277-.813a1.902 1.902 0 0 1-.4-1.158c0-.335.073-.63.216-.886.144-.255.335-.479.575-.654.24-.184.51-.32.83-.415.32-.096.655-.136 1.006-.136.175 0 .359.008.535.032.183.024.35.056.518.088.16.04.312.08.455.127.144.048.256.096.336.144a.69.69 0 0 1 .24.2.43.43 0 0 1 .071.263v.375c0 .168-.064.256-.184.256a.83.83 0 0 1-.303-.096 3.652 3.652 0 0 0-1.532-.311c-.455 0-.815.071-1.062.223-.248.152-.375.383-.375.71 0 .224.08.416.24.567.159.152.454.304.877.44l1.134.358c.574.184.99.44 1.237.767.247.327.367.702.367 1.117 0 .343-.072.655-.207.926-.144.272-.336.511-.583.703-.248.2-.543.343-.886.447-.36.111-.734.167-1.142.167zM21.698 16.207c-2.626 1.94-6.442 2.969-9.722 2.969-4.598 0-8.74-1.7-11.87-4.526-.247-.223-.024-.527.272-.351 3.384 1.963 7.559 3.153 11.877 3.153 2.914 0 6.114-.607 9.06-1.852.439-.2.814.287.383.607zM22.792 14.961c-.336-.43-2.22-.207-3.074-.103-.255.032-.295-.192-.063-.36 1.5-1.053 3.967-.75 4.254-.399.287.36-.08 2.826-1.485 4.007-.215.184-.423.088-.327-.151.32-.79 1.03-2.57.695-2.994z"/></svg>AWS</span><span class="tech t-claude"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m4.7144 15.9555 4.7174-2.6471.079-.2307-.079-.1275h-.2307l-.7893-.0486-2.6956-.0729-2.3375-.0971-2.2646-.1214-.5707-.1215-.5343-.7042.0546-.3522.4797-.3218.686.0608 1.5179.1032 2.2767.1578 1.6514.0972 2.4468.255h.3886l.0546-.1579-.1336-.0971-.1032-.0972L6.973 9.8356l-2.55-1.6879-1.3356-.9714-.7225-.4918-.3643-.4614-.1578-1.0078.6557-.7225.8803.0607.2246.0607.8925.686 1.9064 1.4754 2.4893 1.8336.3643.3035.1457-.1032.0182-.0728-.164-.2733-1.3539-2.4467-1.445-2.4893-.6435-1.032-.17-.6194c-.0607-.255-.1032-.4674-.1032-.7285L6.287.1335 6.6997 0l.9957.1336.419.3642.6192 1.4147 1.0018 2.2282 1.5543 3.0296.4553.8985.2429.8318.091.255h.1579v-.1457l.1275-1.706.2368-2.0947.2307-2.6957.0789-.7589.3764-.9107.7468-.4918.5828.2793.4797.686-.0668.4433-.2853 1.8517-.5586 2.9021-.3643 1.9429h.2125l.2429-.2429.9835-1.3053 1.6514-2.0643.7286-.8196.85-.9046.5464-.4311h1.0321l.759 1.1293-.34 1.1657-1.0625 1.3478-.8804 1.1414-1.2628 1.7-.7893 1.36.0729.1093.1882-.0183 2.8535-.607 1.5421-.2794 1.8396-.3157.8318.3886.091.3946-.3278.8075-1.967.4857-2.3072.4614-3.4364.8136-.0425.0304.0486.0607 1.5482.1457.6618.0364h1.621l3.0175.2247.7892.522.4736.6376-.079.4857-1.2142.6193-1.6393-.3886-3.825-.9107-1.3113-.3279h-.1822v.1093l1.0929 1.0686 2.0035 1.8092 2.5075 2.3314.1275.5768-.3218.4554-.34-.0486-2.2039-1.6575-.85-.7468-1.9246-1.621h-.1275v.17l.4432.6496 2.3436 3.5214.1214 1.0807-.17.3521-.6071.2125-.6679-.1214-1.3721-1.9246L14.38 17.959l-1.1414-1.9428-.1397.079-.674 7.2552-.3156.3703-.7286.2793-.6071-.4614-.3218-.7468.3218-1.4753.3886-1.9246.3157-1.53.2853-1.9004.17-.6314-.0121-.0425-.1397.0182-1.4328 1.9672-2.1796 2.9446-1.7243 1.8456-.4128.164-.7164-.3704.0667-.6618.4008-.5889 2.386-3.0357 1.4389-1.882.929-1.0868-.0062-.1579h-.0546l-6.3385 4.1164-1.1293.1457-.4857-.4554.0608-.7467.2307-.2429 1.9064-1.3114Z"/></svg>Claude Code</span><span class="tech t-copilot"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M23.922 16.997C23.061 18.492 18.063 22.02 12 22.02 5.937 22.02.939 18.492.078 16.997A.641.641 0 0 1 0 16.741v-2.869a.883.883 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.098 10.098 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952C7.255 2.937 9.248 1.98 11.978 1.98c2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.841.841 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256Zm-11.75-5.992h-.344a4.359 4.359 0 0 1-.355.508c-.77.947-1.918 1.492-3.508 1.492-1.725 0-2.989-.359-3.782-1.259a2.137 2.137 0 0 1-.085-.104L4 11.746v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.359 4.359 0 0 1-.355-.508Zm2.328 3.25c.549 0 1 .451 1 1v2c0 .549-.451 1-1 1-.549 0-1-.451-1-1v-2c0-.549.451-1 1-1Zm-5 0c.549 0 1 .451 1 1v2c0 .549-.451 1-1 1-.549 0-1-.451-1-1v-2c0-.549.451-1 1-1Zm3.313-6.185c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"/></svg>GitHub Copilot</span><span class="tech t-cursor"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11.503.131 1.891 5.678a.84.84 0 0 0-.42.726v11.188c0 .3.162.575.42.724l9.609 5.55a1 1 0 0 0 .998 0l9.61-5.55a.84.84 0 0 0 .42-.724V6.404a.84.84 0 0 0-.42-.726L12.497.131a1.01 1.01 0 0 0-.996 0M2.657 6.338h18.55c.263 0 .43.287.297.515L12.23 22.918c-.062.107-.229.064-.229-.06V12.335a.59.59 0 0 0-.295-.51l-9.11-5.257c-.109-.063-.064-.23.061-.23"/></svg>Cursor</span></div></div></div>
    </div>
  </div>
</section>

'''

# ------------------------------------------------------------------ agentes em três cards alternados
AREAS = [
 ('Vendas e marketing', 'Leads atendidos', '24 horas por dia.', 'Agentes que qualificam, prospectam, precificam e testam anúncios, e entregam clientes prontos para o time comercial.', [
   ('Qualificador 24/7', 'WhatsApp e voz'), ('Social selling', 'Instagram'), ('Precificação dinâmica', 'Preço em tempo real'), ('Marketing preditivo', 'Anúncios testados')]),
 ('Operações e processos', 'Tarefas repetitivas', 'fora da fila da equipe.', 'Agentes que leem documentos e e-mails, atendem com contexto, fazem a triagem de currículos e analisam contratos.', [
   ('RPA cognitivo', 'Documentos e e-mails'), ('Suporte nível humano', 'Empatia e memória'), ('Recrutamento', 'Triagem e entrevistas'), ('Análise contratual', 'Cláusulas e termos')]),
 ('Inteligência e decisão', 'Decisões com os dados', 'que você já tem.', 'Agentes que antecipam churn e demanda, monitoram a marca, conversam com os seus dados e detectam fraudes.', [
   ('Análise preditiva', 'Churn, demanda e LTV'), ('Análise de sentimento', 'Reputação nas redes'), ('BI conversacional', 'Relatórios por texto'), ('Segurança e fraude', 'Comportamento suspeito')]),
]
vis_vendas = r'''<div class="jan" id="cons"><div class="jan-h"><div class="ag"><span class="cir">''' + svg(I['bot']) + r'''</span><div><b>Qualificador 24/7</b><br><span class="tag">WhatsApp</span></div></div><span class="tag">// exemplo</span></div>
            <div class="msgs" id="msgs">
              <div class="msg cli" data-t="Quero entender como funciona para a minha empresa."></div>
              <div class="msg age" data-t="Claro. Quantas pessoas atendem os seus clientes hoje?"></div>
              <div class="msg cli" data-t="Somos quatro, e o WhatsApp não para."></div>
              <div class="msg age" data-t="Entendi. Registrei o seu contato e agendei uma conversa com o time comercial."></div>
              <div class="msg sis">''' + svg(CHK) + r'''Lead qualificado · enviado ao CRM</div>
            </div>
            <div class="jan-p"><span>Conversa ilustrativa.</span><button class="rep" type="button" id="consRep" hidden>''' + svg(I['refresh']) + r'''Repetir</button></div></div>'''
folha = ''.join('<i%s style="width:%d%%"></i>' % (' class="m"' if k in (2, 6, 10) else '', w) for k, w in enumerate([92, 80, 88, 70, 95, 84, 76, 90, 64, 86, 72, 58]))
CAMPOS = [('Tipo', 'Contrato de serviço'), ('Vigência', '24 meses'), ('Reajuste', 'Anual'), ('Rescisão', 'Aviso de 30 dias'), ('Ponto de atenção', 'Multa na cláusula 9')]
vis_ops = (r'''<div class="jan"><div class="jan-h"><div class="ag"><span class="cir">''' + svg(I['file']) + r'''</span><div><b>Análise contratual</b><br><span class="tag">contrato.pdf</span></div></div><span class="tag">// exemplo</span></div>
            <div class="doc" id="doc"><div class="folha" aria-hidden="true">''' + folha + r'''<span class="scan"></span></div><div class="campos">'''
           + ''.join('<div class="campo"><span>%s</span><b>%s</b></div>' % c for c in CAMPOS) + r'''</div></div>
            <div class="jan-p"><span>Leitura ilustrativa de um contrato em PDF.</span></div></div>''')
BARRAS = [('Varejo', 72), ('Serviços', 54), ('Indústria', 38), ('Saúde', 26), ('Educação', 18)]
vis_dec = (r'''<div class="jan"><div class="jan-h"><div class="ag"><span class="cir">''' + svg(I['chart']) + r'''</span><div><b>BI conversacional</b><br><span class="tag">Seus dados</span></div></div><span class="tag">// exemplo</span></div>
            <div class="bi" id="bi"><div class="msg cli">Quais segmentos têm mais risco de cancelar este mês?</div><div class="msg age">Aqui está o risco de churn por segmento, com base nos últimos 90 dias:</div><div class="barras">'''
           + ''.join('<div class="barra"><span>%s</span><span class="t"><i data-w="%d"></i></span><b>%d%%</b></div>' % (n, v, v) for n, v in BARRAS) + r'''</div></div>
            <div class="jan-p"><span>Dados ilustrativos.</span></div></div>''')
VIS = [vis_vendas, vis_ops, vis_dec]
cards = ''
for k, (area, t1, t2, txt, ags) in enumerate(AREAS):
    pts = ''.join('<i%s></i>' % (' class="on"' if j == k else '') for j in range(3))
    cards += ('      <article class="c-ag cd lum g12%s rv" aria-labelledby="agA%d">\n' % (' inv' if k == 1 else '', k)
              + '        <div class="tx"><span class="micro-l">%02d · %s</span><h3 class="h2" id="agA%d">%s <span class="tone">%s</span></h3><p>%s</p>' % (k + 1, area, k, t1, t2, txt)
              + '<ul class="ags">' + ''.join('<li><b>%s</b><span>%s</span></li>' % a for a in ags) + '</ul>'
              + '<a class="link" href="#proposta" data-area="%s">Quero um agente de %s %s</a></div>\n' % (area, area.split(' ')[0].lower(), SETA)
              + '        <div class="vis"><div class="palco">' + VIS[k] + '<div class="pts" aria-hidden="true">' + pts + '</div></div></div>\n'
              + '      </article>\n')
agentes = r'''<!-- S04 · Serviços: os agentes, em três cards alternados por área -->
<section class="sec" id="agentes" aria-labelledby="agT">
  <div class="wrap">
    <div class="cab rv">
      <span class="micro-l">Agentes inteligentes</span>
      <h2 class="h2" id="agT">Da eficiência operacional <span class="tone">à disrupção de mercado.</span></h2>
      <p class="lead">Enquanto muitos só integram ferramentas prontas, a Rumo constrói agentes que operam de forma autônoma, aprendem com os dados e seguem o seu processo.</p>
    </div>
    <div class="cards-ag">
''' + cards + r'''    </div>
  </div>
</section>

'''

# ------------------------------------------------------------------ integração
CANAIS = ['WhatsApp', 'Voz', 'E-mail', 'Instagram']
SIST = ['ERP', 'CRM', 'Legado', 'Nuvem']
ys = [90, 170, 250, 330]
nodes = lines = ''
for i, (c, y) in enumerate(zip(CANAIS, ys)):
    nodes += '<g class="nd" data-n="c%d"><rect x="10" y="%d" width="140" height="40" rx="20"/><text x="80" y="%d" text-anchor="middle">%s</text></g>' % (i, y - 20, y + 5, c)
    lines += '<path class="ln" data-n="c%d" pathLength="1" d="M150 %d C 210 %d, 230 210, 262 210"/>' % (i, y, y)
for i, (c, y) in enumerate(zip(SIST, ys)):
    nodes += '<g class="nd" data-n="s%d"><rect x="450" y="%d" width="140" height="40" rx="20"/><text x="520" y="%d" text-anchor="middle">%s</text></g>' % (i, y - 20, y + 5, c)
    lines += '<path class="ln" data-n="s%d" pathLength="1" d="M338 210 C 370 210, 390 %d, 450 %d"/>' % (i, y, y)
diag = ('<svg viewBox="0 0 600 420" role="img" aria-label="Canais (WhatsApp, voz, e-mail e Instagram) ligados aos agentes da Rumo AI, que se conectam ao ERP, ao CRM, a sistemas legados e à nuvem">'
        '<text class="tit" x="80" y="40" text-anchor="middle">Canais</text><text class="tit" x="300" y="40" text-anchor="middle">Agentes</text><text class="tit" x="520" y="40" text-anchor="middle">Seus sistemas</text>'
        + lines + nodes + '<g class="hub"><circle class="anel" cx="300" cy="210" r="56"/><circle cx="300" cy="210" r="40"/><text x="300" y="215" text-anchor="middle">Rumo AI</text></g></svg>')
integ = r'''<!-- S10 · Diferenciais: integração aos sistemas que a empresa já usa -->
<section class="sec" id="integracao" aria-labelledby="inT">
  <div class="wrap">
    <div class="cab rv">
      <span class="micro-l">Integração</span>
      <h2 class="h2" id="inT">Conecta ao que a sua empresa <span class="tone">já usa.</span></h2>
      <p class="lead">ERP, CRM, sistema legado ou nuvem: os agentes entram no fluxo que já existe, pelos canais que os seus clientes já usam.</p>
    </div>
    <div class="diag cd lum rv" id="diag">''' + diag + r'''</div>
    <div class="centro rv"><a class="btn btn-secondary" href="#proposta">Conectar os meus sistemas ''' + SETA + r'''</a></div>
  </div>
</section>

'''

G6 = [
 ('code', 'Especialistas em software e dados', 'Soluções integradas de verdade aos seus sistemas.'),
 ('sliders', 'Modelos personalizáveis e treináveis', 'Agentes que se adaptam à sua realidade, e não o contrário.'),
 ('shield', 'Um ecossistema que é seu', 'O agente e os dados ficam com a sua empresa, sem depender de plataformas de terceiros.'),
 ('clock', 'Atendimento 24/7 multicanal', 'Agentes que atendem pelo WhatsApp, por voz e por outros canais, a qualquer hora.'),
 ('layers', 'Stack de IA atual', 'n8n, Python, GPT-4, Claude, Gemini, Evolution API, Redis e PostgreSQL.'),
 ('pulse', 'TI de missão crítica desde 1997', 'Quase três décadas desenvolvendo e sustentando sistemas para bancos, seguradoras, indústrias e saúde digital.'),
]
grade = r'''<!-- S10 · Diferenciais: IA com propósito, tecnologia e contexto -->
<section class="sec" id="diferenciais" aria-labelledby="dfT">
  <div class="wrap">
    <div class="cab rv">
      <span class="micro-l">Por que a Rumo AI</span>
      <h2 class="h2" id="dfT">IA com propósito, <span class="tone">tecnologia e contexto.</span></h2>
    </div>
    <div class="grade6">
''' + ''.join('      <div class="g6 rv"><span class="cir">%s</span><b>%s</b><p>%s</p></div>\n' % (svg(I[k]), t, d) for k, t, d in G6) + r'''    </div>
  </div>
</section>

'''

ENT = [('mic', 'Áudio'), ('video', 'Vídeo'), ('image', 'Print'), ('file', 'PDF'), ('chat', 'Texto')]
LEG = ['Chega um áudio, um vídeo, um print, um PDF ou uma mensagem.', 'A Sófi entende o pedido e faz a triagem.', 'Um especialista recebe a conversa já organizada.']
sofi = r'''<!-- S07 · Produtos: a Sófi em operação, num quadro fixo que a rolagem avança -->
<section class="sec" id="sofi" aria-labelledby="sfT" style="padding-block:0">
  <div class="trilho" id="trilho">
    <div class="pino">
      <div class="wrap">
        <div class="g12 sofi">
          <div class="l">
            <span class="micro-l">Em operação</span>
            <h2 class="h2" id="sfT">A Sófi já atende <span class="tone">clientes e o time da Rumo.</span></h2>
            <p>Assistente virtual humanizada e multicanal, com foco em WhatsApp. Interpreta áudios, vídeos, prints, PDFs e mensagens de texto e faz a triagem antes de passar a conversa para um especialista.</p>
            <div class="quem" aria-label="Quem a Sófi atende"><span>Startvet</span><span>SGAE</span><span>PriceFleet</span><span>Genial</span><span>Carbel</span><span>Barigui</span><span>RH e Infraestrutura da Rumo</span></div>
            <div class="passos-s" role="group" aria-label="Etapas da Sófi"><button type="button" data-p="0" aria-current="true">1 · Chega</button><button type="button" data-p="1">2 · Triagem</button><button type="button" data-p="2">3 · Especialista</button></div>
          </div>
          <div class="fluxo-s cd lum" id="fluxoS" data-p="0">
            <div class="fs-col"><span class="tag">Chega</span>''' + ''.join('<span class="fs-in">%s%s</span>' % (svg(I[k]), t) for k, t in ENT) + r'''</div>
            <span class="fs-seta a1" aria-hidden="true">''' + SETA + r'''</span>
            <div class="fs-meio s1"><span class="cir">''' + svg(I['bot']) + r'''</span><b>Sófi</b><span class="tag">Triagem</span></div>
            <span class="fs-seta a2" aria-hidden="true">''' + SETA + r'''</span>
            <div class="fs-meio s2"><span class="cir">''' + svg(I['user']) + r'''</span><b>Especialista</b><span class="tag">Atende</span></div>
            <p class="fs-leg" id="fsLeg" aria-live="polite">''' + LEG[0] + r'''</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

'''

ck = '<span class="ck">' + svg(CHK) + '</span>'
row = lambda t: '<div class="cf-r"><span class="l">' + ck + t + '</span></div>'
ETAPAS = [
 ('Diagnóstico gratuito', 'Você e Rumo', 'Um especialista entende o seu processo e aponta onde um agente gera mais resultado.',
  '<div class="cf-hd"><span class="tag">// diagnóstico · exemplo</span><span class="tag">Gratuito</span></div>' + row('Processo mapeado com a sua equipe') + row('Ponto de maior ganho identificado') + row('Agente recomendado para começar')),
 ('MVP do agente', 'Rumo', 'O primeiro agente roda em um recorte do processo, para validar com uso real antes de crescer.',
  '<div class="cf-hd"><span class="tag">// mvp · exemplo</span><span class="tag">Rumo</span></div>' + row('Recorte do processo definido') + row('Agente treinado com os seus dados') + row('Teste com uso real')),
 ('Entrada na operação', 'Rumo', 'O agente passa a trabalhar no fluxo da sua equipe, no dia a dia.',
  '<div class="cf-hd"><span class="tag">// operação · exemplo</span><span class="tag">Rumo</span></div>' + row('Canal de atendimento conectado') + row('Registros entrando no CRM') + row('Equipe usando no dia a dia')),
 ('Evolução contínua', 'Contínuo', 'O agente evolui junto com o uso, com acompanhamento contínuo da Rumo.',
  '<div class="cf-hd"><span class="tag">// acompanhamento · exemplo</span><span class="tag">Contínuo</span></div>' + row('Uso e resultados monitorados') + row('Ajustes no treinamento') + row('Novas tarefas para o agente')),
]
nav = ''.join('<button class="cf-s" type="button" role="tab" id="cfS%d" aria-controls="cfP%d" aria-selected="%s" tabindex="%s"><span class="n">%02d</span><span>%s</span><span class="tag">%s</span></button>'
              % (i + 1, i + 1, 'true' if i == 0 else 'false', '0' if i == 0 else '-1', i + 1, t, q) for i, (t, q, _, _) in enumerate(ETAPAS))
pans = ''.join('      <div class="cf-p" role="tabpanel" id="cfP%d" aria-labelledby="cfS%d"%s><div class="cf-t"><span class="num">%02d / 04</span><h3 class="h3">%s</h3><p>%s</p></div><div class="cf-v"><div class="cf-card">%s</div></div></div>\n'
               % (i + 1, i + 1, '' if i == 0 else ' hidden', i + 1, t, d, v) for i, (t, _, d, v) in enumerate(ETAPAS))
como = r'''<!-- S05 · Narrativa: como funciona, em quatro etapas interativas -->
<section class="sec" id="como-funciona" aria-labelledby="hwT">
  <div class="wrap">
    <div class="cab rv">
      <span class="micro-l">Como funciona</span>
      <h2 class="h2" id="hwT">Do diagnóstico ao agente <span class="tone">em operação.</span></h2>
      <p class="lead">Quatro etapas, do primeiro recorte ao agente rodando na sua operação. Clique para ver cada uma.</p>
    </div>
    <div class="cf-nav rv" role="tablist" aria-label="Etapas"><span class="cf-linha" aria-hidden="true"><i id="cfLinha"></i></span>''' + nav + r'''</div>
    <div class="cd">
''' + pans + r'''    </div>
  </div>
</section>

'''

FAQ = [
 ('Preciso trocar os meus sistemas?', 'Não. A Rumo conecta a IA a ERPs, CRMs e sistemas legados com uma integração não invasiva, sem reestruturar a infraestrutura e sem parar a operação.'),
 ('Os agentes desta página são prontos?', 'São pontos de partida. Cada agente é construído e treinado sob medida para o processo, os dados e os sistemas da sua empresa.'),
]
PM = '<span class="pm" aria-hidden="true"><svg class="ico" viewBox="0 0 24 24"><path d="M12 5v14"/><path d="M5 12h14"/></svg></span>'
faq = ('<!-- S13 · Perguntas frequentes -->\n<section class="sec" id="faq" aria-labelledby="fqT">\n  <div class="wrap">\n'
       '    <div class="cab rv"><span class="micro-l">Perguntas frequentes</span><h2 class="h2" id="fqT">Perguntas, <span class="tone">respondidas.</span></h2></div>\n    <div class="faq rv">\n'
       + ''.join('      <div class="qa%s"><h3><button class="qa-q" type="button" aria-expanded="%s" aria-controls="a%d">%s%s</button></h3><div class="qa-a" id="a%d" role="region"><div><p>%s</p></div></div></div>\n'
                 % (' open' if i == 0 else '', 'true' if i == 0 else 'false', i, q, PM, i, a) for i, (q, a) in enumerate(FAQ))
       + '    </div>\n  </div>\n</section>\n\n')

opts_area = ''.join('<option>%s</option>' % a[0] for a in AREAS) + '<option>Ainda não sei</option>'
opts_ag = ''.join('<optgroup label="%s">%s</optgroup>' % (a[0], ''.join('<option>%s</option>' % n for n, _ in a[4])) for a in AREAS)
LOCK = svg('<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>')
SELOS = [('sliders', 'Sob medida'), ('layers', 'Integrado aos seus sistemas'), ('shield', 'Ecossistema seu')]
form = r'''<!-- S11 · Diagnóstico gratuito (CTA final com selos e o formulário de proposta) -->
<section class="sec fim" id="proposta" aria-labelledby="pdT">
  <div class="wrap">
    <div class="cab rv"><div class="selos">''' + ''.join('<span>%s%s</span>' % (svg(I[k]), t) for k, t in SELOS) + r'''</div><h2 class="h1" id="pdT">Vamos construir um agente <span class="tone">para o seu negócio?</span></h2><p class="lead">Seja qual for o desafio, de operação, vendas, atendimento ou decisão, a Rumo desenvolve uma solução de IA sob medida.</p></div>
    <div class="panel cd lit" id="panel">
      <!-- ENVIO POR E-MAIL (P12 do guia): sem servidor no GitHub Pages; o envio abre o e-mail do visitante com o pedido pronto, endereçado a DESTINO (no script). -->
      <form class="form" id="form" novalidate>
        <div class="f"><label for="fArea">Área</label><select id="fArea" name="area"><option value="">Escolha uma área</option>''' + opts_area + r'''</select></div>
        <div class="f" id="fAgBox"><label for="fAg">Agente de interesse <span class="trava" aria-hidden="true">''' + LOCK + r'''</span></label><select id="fAg" name="agente" aria-describedby="hAg"><option value="">Escolha um agente</option>''' + opts_ag + r'''<option>Outro ou mais de um</option></select><span class="hint" id="hAg" hidden>O agente fica para a conversa com o especialista.</span></div>
        <div class="f"><label for="fNome">Nome</label><input id="fNome" name="nome" autocomplete="name" required aria-describedby="eNome"><span class="err" id="eNome" hidden></span></div>
        <div class="f"><label for="fEmp">Empresa</label><input id="fEmp" name="empresa" autocomplete="organization" required aria-describedby="eEmp"><span class="err" id="eEmp" hidden></span></div>
        <div class="f"><label for="fEmail">E-mail corporativo</label><input id="fEmail" name="email" type="email" autocomplete="email" required aria-describedby="eEmail"><span class="err" id="eEmail" hidden></span></div>
        <div class="f"><label for="fTel">Telefone</label><input id="fTel" name="telefone" type="tel" autocomplete="tel"></div>
        <div class="f full"><label for="fMsg">Desafio</label><textarea id="fMsg" name="mensagem" rows="5" placeholder="Conte qual processo você quer automatizar ou o que o seu time precisa"></textarea></div>
        <div class="send"><small>Seus dados servem só para responder a este pedido, conforme a LGPD.</small><button class="btn btn-primary" type="submit">Solicitar proposta ''' + SETA + r'''</button></div>
        <div class="ok" id="ok" hidden role="status"><p class="h4">Seu pedido está pronto no seu e-mail.</p><p>Abrimos o seu programa de e-mail com tudo preenchido. É só enviar, e um especialista da Rumo responde.</p></div>
      </form>
    </div>
    <p class="rv" style="text-align:center;margin-top:32px"><a class="link" href="https://rumoai.io" rel="noopener">Conheça a Rumo AI em rumoai.io ''' + SETA + r'''</a></p>
  </div>
</section>

</main>

<!--RODAPE-->

'''

# ------------------------------------------------------------------ JavaScript
js_base = entre('<script src="https://cdn.jsdelivr.net/npm/lenis', '/* ---------- modelos: o contorno neon')
js_etapas = entre('/* ---------- como funciona: etapas como abas', '/* ---------- perguntas frequentes')
js_faq = entre('/* ---------- perguntas frequentes', '/* ---------- formulário: "Ainda não sei"')
js_form_base = entre('/* ---------- formulário (envio desligado) ---------- */', "form.addEventListener('submit'")

js = r'''/* ---------- contorno neon que segue o cursor (M20) ---------- */
$$('.lum').forEach(el => {
  const pos = e => { const r = el.getBoundingClientRect(); el.style.setProperty('--mx', (e.clientX - r.left) + 'px'); el.style.setProperty('--my', (e.clientY - r.top) + 'px'); };
  el.addEventListener('pointerenter', () => el.classList.add('hov'));
  el.addEventListener('pointermove', e => { el.classList.add('luz'); pos(e); });
  el.addEventListener('pointerleave', () => el.classList.remove('luz', 'hov'));
});

/* ---------- hero: a luz de cima segue o cursor no eixo x, até 120px (spotlight, padrão 04) ---------- */
(function luz(){
  const el = $('#hxLuz'), hero = $('#hero'); if (!el || reduce || !fine) return;
  let alvo = 0, x = 0, ativo = false;
  hero.addEventListener('pointermove', e => { const r = hero.getBoundingClientRect(); alvo = Math.max(-1, Math.min(1, (e.clientX - r.left) / r.width * 2 - 1)) * 120; if (!ativo) { ativo = true; requestAnimationFrame(passo); } });
  hero.addEventListener('pointerleave', () => { alvo = 0; });
  function passo(){ x += (alvo - x) * .08; el.style.setProperty('--x', x.toFixed(1) + 'px'); if (Math.abs(alvo - x) > .3) requestAnimationFrame(passo); else ativo = false; }
})();

/* ---------- hero: esfera de partículas com "AI" no centro (padrão 05). Gira devagar, cintila e o cursor afasta as partículas, que voltam por mola ---------- */
(function esfera(){
  const cv = $('#esfera'), hero = $('#hero'); if (!cv) return;
  const ctx = cv.getContext('2d');
  const COR = ['0,172,229', '127,216,245', '191,239,255', '242,251,255'];
  let W = 0, H = 0, R = 0, cx = 0, cy = 0, pts = [], rodando = true, semente = 7, t0 = -1, formado = reduce;
  const mouse = { x: -1e4, y: -1e4 };
  const rnd = () => (semente = (semente * 16807) % 2147483647) / 2147483647;
  // cada partícula nasce espalhada em volta da esfera e chega em espiral; a esfera forma primeiro e o AI fecha por último
  const partida = tipo => { const ang = rnd() * 6.283, dist = 1.5 + rnd() * 2.6; return { fx: Math.cos(ang) * dist, fy: Math.sin(ang) * dist * .75, d: tipo ? 900 + rnd() * 700 : rnd() * 900, dur: 1300 + rnd() * 700 }; };
  const suave = k => k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2;
  function montar(){
    semente = 7;
    const r = cv.getBoundingClientRect(); W = r.width; H = r.height;
    const dpr = Math.min(1.5, devicePixelRatio || 1); cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const mob = W < 640;
    const tab = !mob && W < 1100;
    R = mob ? Math.min(W * .34, 128) : tab ? Math.min(W * .2, 190) : Math.min(W * .162, H * .255, 248);
    cx = W / 2; cy = (mob || tab) ? 100 + R : Math.max(R + 112, H * .35);
    pts = [];
    const N = mob ? 2000 : 4200;
    for (let i = 0; i < N; i++) {
      const y = 1 - 2 * (i + .5) / N, rr = Math.sqrt(1 - y * y), th = i * 2.399963, s = 1 + (rnd() - .5) * .1;
      pts.push(Object.assign({ t: 0, x: Math.cos(th) * rr * s, y: y * s, z: Math.sin(th) * rr * s, a: .45 + rnd() * .55, c: rnd() < .55 ? 1 : (rnd() < .5 ? 0 : 2), tw: rnd() * 6.28, ox: 0, oy: 0, vx: 0, vy: 0 }, partida(0)));
    }
    // letras: desenha "AI" num canvas fora da tela e amostra os pixels
    const fs = Math.round(R * .78), off = document.createElement('canvas'), ow = Math.round(R * 1.6), oh = Math.round(fs * 1.1);
    off.width = ow; off.height = oh;
    const o = off.getContext('2d'); o.fillStyle = '#fff'; o.textAlign = 'center'; o.textBaseline = 'middle';
    o.font = '600 ' + fs + 'px Geist, system-ui, sans-serif'; o.fillText('AI', ow / 2, oh / 2 + fs * .04);
    const dados = o.getImageData(0, 0, ow, oh).data, passo = 2;
    for (let py = 0; py < oh; py += passo) for (let px = 0; px < ow; px += passo) {
      if (dados[(py * ow + px) * 4 + 3] < 140 || rnd() < .35) continue;
      pts.push(Object.assign({ t: 1, x: (px - ow / 2 + (rnd() - .5) * passo * 1.5) / R, y: (py - oh / 2 + (rnd() - .5) * passo * 1.5) / R, z: 0, a: .7 + rnd() * .3, c: rnd() < .5 ? 3 : (rnd() < .6 ? 1 : 2), tw: rnd() * 6.28, ox: 0, oy: 0, vx: 0, vy: 0 }, partida(1)));
    }
  }
  function quadro(t){
    ctx.clearRect(0, 0, W, H);
    const rot = reduce ? .6 : t * .00011, cr = Math.cos(rot), sr = Math.sin(rot), ct = Math.cos(.32), st = Math.sin(.32);
    // brilho interno da esfera
    if (!formado && t0 < 0) t0 = t;
    if (!formado && t - t0 > 3400) formado = true;
    const forma = formado ? 1 : Math.max(0, Math.min(1, (t - t0 - 600) / 2000));
    ctx.globalAlpha = forma;
    const g = ctx.createRadialGradient(cx, cy, 0, cx, cy, R * 1.1);
    g.addColorStop(0, 'rgba(0,172,229,.32)'); g.addColorStop(.5, 'rgba(0,172,229,.12)'); g.addColorStop(1, 'rgba(0,172,229,0)');
    ctx.fillStyle = g; ctx.beginPath(); ctx.arc(cx, cy, R * 1.1, 0, 6.283); ctx.fill();
    ctx.globalAlpha = 1;
    ctx.globalCompositeOperation = 'lighter';
    for (const p of pts) {
      let sx, sy, prof = 1, tam;
      if (p.t === 0) {
        const x1 = p.x * cr - p.z * sr, z1 = p.x * sr + p.z * cr, y2 = p.y * ct - z1 * st, z2 = p.y * st + z1 * ct;
        prof = (z2 + 1.2) / 2.2; sx = cx + x1 * R; sy = cy + y2 * R; tam = 1 + prof * 1.6;
      } else { sx = cx + p.x * R; sy = cy + p.y * R; tam = 1.8; }
      let alfa = 1;
      if (!formado) {
        const k = Math.max(0, Math.min(1, (t - t0 - p.d) / p.dur)), e = suave(k), q = 1 - e, ang = q * 1.1, c = Math.cos(ang), s2 = Math.sin(ang);
        const ddx = (cx + p.fx * R - sx) * q, ddy = (cy + p.fy * R - sy) * q;
        sx += ddx * c - ddy * s2; sy += ddx * s2 + ddy * c; alfa = Math.min(1, k * 1.6);
      }
      if (!reduce) {
        const dx = sx + p.ox - mouse.x, dy = sy + p.oy - mouse.y, d = Math.hypot(dx, dy);
        if (d < 110 && d > .1) { const f = (1 - d / 110) * 2.2; p.vx += dx / d * f; p.vy += dy / d * f; }
        p.vx = (p.vx - p.ox * .05) * .86; p.vy = (p.vy - p.oy * .05) * .86; p.ox += p.vx; p.oy += p.vy;
      }
      const brilho = alfa * p.a * (.6 + .4 * Math.sin(t * .0022 + p.tw)) * (p.t ? 1 : (.25 + prof * .75));
      ctx.fillStyle = 'rgba(' + COR[p.c] + ',' + brilho.toFixed(3) + ')';
      ctx.fillRect(sx + p.ox - tam / 2, sy + p.oy - tam / 2, tam, tam);
      if (p.t || prof > .8) { ctx.fillStyle = 'rgba(' + COR[p.c] + ',' + (brilho * .14).toFixed(3) + ')'; ctx.fillRect(sx + p.ox - tam * 2, sy + p.oy - tam * 2, tam * 4, tam * 4); }
    }
    ctx.globalCompositeOperation = 'source-over';
  }
  const laco = t => { if (rodando) quadro(t); requestAnimationFrame(laco); };
  montar();
  addEventListener('resize', montar);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => { montar(); if (reduce) quadro(0); });
  if (reduce) { quadro(0); return; }
  hero.addEventListener('pointermove', e => { const r = cv.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; });
  hero.addEventListener('pointerleave', () => { mouse.x = mouse.y = -1e4; });
  if ('IntersectionObserver' in window) new IntersectionObserver(es => { rodando = es[0].isIntersecting; }).observe(hero);
  requestAnimationFrame(laco);
})();

/* ---------- vendas: a conversa digita uma vez (M11); "Repetir" reinicia ---------- */
(function conversa(){
  const ms = $$('#msgs .msg'), rep = $('#consRep'); if (!ms.length) return;
  let fila = [];
  const limpar = () => { fila.forEach(clearTimeout); fila = []; ms.forEach(m => { m.classList.remove('on'); if (m.dataset.t) m.textContent = ''; }); };
  const tudo = () => { ms.forEach(m => { if (m.dataset.t) m.textContent = m.dataset.t; m.classList.add('on'); }); };
  const tocar = () => {
    limpar(); rep.hidden = true; let t = 300;
    ms.forEach(m => {
      const txt = m.dataset.t, cli = m.classList.contains('cli');
      fila.push(setTimeout(() => m.classList.add('on'), t));
      if (txt && !cli) {
        const car = document.createElement('i'); car.className = 'car';
        for (let k = 1; k <= txt.length; k++) fila.push(setTimeout(() => { m.textContent = txt.slice(0, k); if (k < txt.length) m.appendChild(car); }, t + 200 + k * 28));
        t += 200 + txt.length * 28 + 600;
      } else { if (txt) m.textContent = txt; t += 800; }
    });
    fila.push(setTimeout(() => { rep.hidden = false; }, t));
  };
  rep.addEventListener('click', tocar);
  if (reduce || !('IntersectionObserver' in window)) { tudo(); return; }
  const io = new IntersectionObserver(es => { if (es[0].isIntersecting) { io.disconnect(); tocar(); } }, { threshold: .4 });
  io.observe($('#cons'));
})();

/* ---------- operações e decisão: o documento é lido e o gráfico desenha uma vez ao entrar na tela (padrão 06) ---------- */
(function exemplos(){
  const doc = $('#doc'), bi = $('#bi');
  $$('.campo', doc).forEach((c, i) => c.style.transitionDelay = (300 + i * 220) + 'ms');
  const barras = () => $$('.barra .t i', bi).forEach((b, i) => { b.style.transitionDelay = (i * 60) + 'ms'; b.style.width = b.dataset.w + '%'; });
  if (reduce || !('IntersectionObserver' in window)) { doc.classList.add('on'); barras(); return; }
  const io = new IntersectionObserver(es => es.forEach(e => { if (!e.isIntersecting) return; io.unobserve(e.target); if (e.target === doc) doc.classList.add('on'); else barras(); }), { threshold: .45 });
  io.observe(doc); io.observe(bi);
})();

/* ---------- integração: as linhas desenham ao entrar na tela; o cursor num nó acende o caminho ---------- */
(function diagrama(){
  const d = $('#diag'); if (!d) return;
  if (reduce || !('IntersectionObserver' in window)) d.classList.add('on');
  else { const io = new IntersectionObserver(es => { if (es[0].isIntersecting) { io.disconnect(); d.classList.add('on'); } }, { threshold: .4 }); io.observe(d); }
  $$('.nd', d).forEach(n => {
    const ln = $('.ln[data-n="' + n.dataset.n + '"]', d);
    n.addEventListener('pointerenter', () => { n.classList.add('acesa'); ln.classList.add('acesa'); });
    n.addEventListener('pointerleave', () => { n.classList.remove('acesa'); ln.classList.remove('acesa'); });
  });
})();

/* ---------- Sófi: o quadro fica fixo e a rolagem avança as três etapas; os botões levam a cada etapa ---------- */
(function sofi(){
  const tr = $('#trilho'), f = $('#fluxoS'), leg = $('#fsLeg'), bs = $$('.passos-s button'); if (!tr) return;
  const LEG = ''' + repr(LEG).replace("'", '"') + r''';
  const marcar = p => { if (f.dataset.p === String(p)) return; f.dataset.p = p; leg.textContent = LEG[p]; bs.forEach(b => b.setAttribute('aria-current', b.dataset.p === String(p) ? 'true' : 'false')); };
  const fixo = () => getComputedStyle($('.pino', tr)).position === 'sticky';
  const ler = () => { if (!fixo()) { marcar(2); return; } const r = tr.getBoundingClientRect(), total = r.height - innerHeight; const k = Math.max(0, Math.min(.999, -r.top / total)); marcar(Math.floor(k * 3)); };
  addEventListener('scroll', ler, { passive: true }); addEventListener('resize', ler); ler();
  bs.forEach(b => b.addEventListener('click', () => { const r = tr.getBoundingClientRect(), total = r.height - innerHeight; scrollTo({ top: scrollY + r.top + total * (+b.dataset.p + .5) / 3, behavior: reduce ? 'auto' : 'smooth' }); }));
})();

/* ---------- agentes: o link do card leva ao formulário com a área já marcada ---------- */
$$('.c-ag a[data-area]').forEach(a => a.addEventListener('click', () => { const ar = $('#fArea'); ar.value = a.dataset.area; ar.dispatchEvent(new Event('change')); }));

/* ---------- formulário: "Ainda não sei" na área trava o agente ---------- */
(function trava(){
  const area = $('#fArea'), ag = $('#fAg'), box = $('#fAgBox'), dica = $('#hAg');
  const aplicar = () => { const t = area.value === 'Ainda não sei'; ag.disabled = t; if (t) ag.value = ''; box.classList.toggle('travado', t); dica.hidden = !t; };
  area.addEventListener('change', aplicar); aplicar();
})();

'''

js_submit = r'''form.addEventListener('submit', e => {
  e.preventDefault();
  const ok = regras.map(([id, eid, f, msg]) => checar(id, eid, f(), msg));
  const primeiro = regras.find((r, i) => !ok[i]);
  if (primeiro) { $(primeiro[0]).focus(); return; }
  // envio pelo e-mail do visitante: monta o pedido e abre o programa de e-mail
  const DESTINO = 'comercial@rumosolucoes.com';
  const NL = String.fromCharCode(10);
  const val = id => ($(id).value || '').trim();
  const linhas = [['Área', val('#fArea')], ['Agente', $('#fAg').disabled ? 'A definir na conversa' : val('#fAg')], ['Nome', val('#fNome')], ['Empresa', val('#fEmp')], ['E-mail', val('#fEmail')], ['Telefone', val('#fTel')]]
    .filter(([, v]) => v).map(([k, v]) => k + ': ' + v);
  const msg = val('#fMsg');
  const corpo = linhas.join(NL) + (msg ? NL + NL + 'Desafio:' + NL + msg : '');
  location.href = 'mailto:' + DESTINO + '?subject=' + encodeURIComponent('Proposta de IA · ' + val('#fEmp')) + '&body=' + encodeURIComponent(corpo);
  [...form.children].forEach(c => { if (c.id !== 'ok') c.hidden = true; });
  $('#ok').hidden = false;
});
})();
</script>
</body></html>
'''

# ================== v5: menos blocos, menos texto, mais hierarquia ==================
css += r"""
/* v5: hierarquia mais clara, menos texto por bloco */
.c-ag{padding:64px;min-height:560px}
.c-ag .tx{gap:24px}
.c-ag .tx .h2{max-width:460px}
.chips-ag{display:flex;flex-wrap:wrap;gap:8px;margin-top:4px}
.chips-ag span{height:36px;padding:0 16px;display:inline-flex;align-items:center;border-radius:var(--radius-pill);box-shadow:inset 0 0 0 1px var(--border);font-size:var(--text-small);color:var(--fg-muted)}
.palco{min-height:440px}
.difs3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;max-width:920px;margin:48px auto 0}
.difs3 div{display:flex;align-items:center;gap:14px;font-weight:500}
.difs3 .cir{width:44px;height:44px;border-radius:50%;flex:none;display:grid;place-items:center;background:radial-gradient(circle at 30% 25%,var(--color-ink-800),var(--color-ink-950) 70%);box-shadow:inset 0 0 0 1px rgba(255,255,255,.14);color:var(--brand)}
.difs3 .cir .ico{width:18px;height:18px}
.prova{align-items:center}
.prova .l{grid-column:1/6;display:flex;flex-direction:column;align-items:flex-start;gap:20px}
.prova .l p{color:var(--fg-muted)}
.prova .fluxo-s{grid-column:7/13}
.passos4{list-style:none;margin:0 auto 40px;padding:0;max-width:880px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.passos4 li{display:flex;flex-direction:column;gap:10px;padding-top:16px;border-top:1px solid var(--border);font-size:var(--text-small);font-weight:500}
.passos4 li:first-child{border-top-color:var(--brand)}
.passos4 .n{font-family:var(--font-mono);font-size:var(--text-label);font-weight:400;color:var(--brand-text)}
.diag{max-width:720px;padding:32px}
.prova .fs-meio{opacity:1}
.prova .fs-meio .cir{background:var(--brand);color:var(--on-brand);box-shadow:0 0 0 8px rgba(0,172,229,.1),0 0 40px -6px rgba(0,172,229,.7)}
.prova .fs-seta{color:var(--brand)}
@media (max-width:1100px) and (min-width:641px){.hx{min-height:0;padding-top:520px}}
@media (max-width:960px){.c-ag{padding:28px;min-height:0}.difs3{grid-template-columns:1fr;max-width:420px}.prova .l,.prova .fluxo-s{grid-column:1/-1}.prova .fluxo-s{margin-top:40px}.passos4{grid-template-columns:1fr 1fr}}
"""

cards = ''
for k, (area, t1, t2, txt, ags) in enumerate(AREAS):
    cards += ('      <article class="c-ag cd lum g12%s rv" aria-labelledby="agA%d">\n' % (' inv' if k == 1 else '', k)
              + '        <div class="tx"><span class="micro-l">%02d · %s</span><h3 class="h2" id="agA%d">%s <span class="tone">%s</span></h3>' % (k + 1, area, k, t1, t2)
              + '<div class="chips-ag">' + ''.join('<span>%s</span>' % n for n, _ in ags) + '</div>'
              + '<a class="link" href="#proposta" data-area="%s">Quero um agente de %s %s</a></div>\n' % (area, area.split(' ')[0].lower(), SETA)
              + '        <div class="vis"><div class="palco">' + VIS[k] + '</div></div>\n'
              + '      </article>\n')
agentes = r"""<!-- S04 · Serviços: os agentes, em três cards alternados por área -->
<section class="sec" id="agentes" aria-labelledby="agT">
  <div class="wrap">
    <div class="cab rv">
      <span class="micro-l">Agentes inteligentes</span>
      <h2 class="h2" id="agT">Um agente para cada área <span class="tone">da sua empresa.</span></h2>
    </div>
    <div class="cards-ag">
""" + cards + r"""    </div>
  </div>
</section>

"""

D3 = [('code', 'Especialistas em software e dados'), ('sliders', 'Treinados na sua realidade'), ('shield', 'Agente e dados ficam com você')]
integ = r"""<!-- S10 · Diferenciais: integração aos sistemas que a empresa já usa -->
<section class="sec" id="integracao" aria-labelledby="inT">
  <div class="wrap">
    <div class="cab rv">
      <span class="micro-l">Integração</span>
      <h2 class="h2" id="inT">Conecta ao que a sua empresa <span class="tone">já usa.</span></h2>
      <p class="lead">Sem trocar sistemas e sem parar a operação.</p>
    </div>
    <div class="diag cd lum rv" id="diag">""" + diag + r"""</div>
    <div class="difs3 rv">""" + ''.join('<div><span class="cir">%s</span>%s</div>' % (svg(I[k]), t) for k, t in D3) + r"""</div>
  </div>
</section>

"""

sofi = r"""<!-- S07 · Produtos: a Sófi, agente próprio em operação -->
<section class="sec" id="sofi" aria-labelledby="sfT">
  <div class="wrap">
    <div class="g12 prova">
      <div class="l rv">
        <span class="micro-l">Em operação</span>
        <h2 class="h2" id="sfT">A Sófi já atende <span class="tone">clientes e o time da Rumo.</span></h2>
        <p>Entende áudio, vídeo, print, PDF e texto e faz a triagem antes de passar a conversa para um especialista.</p>
      </div>
      <div class="fluxo-s cd lum rv" data-p="2">
        <div class="fs-col"><span class="tag">Chega</span>""" + ''.join('<span class="fs-in">%s%s</span>' % (svg(I[k]), t) for k, t in ENT) + r"""</div>
        <span class="fs-seta a1" aria-hidden="true">""" + SETA + r"""</span>
        <div class="fs-meio s1"><span class="cir">""" + svg(I['bot']) + r"""</span><b>Sófi</b><span class="tag">Triagem</span></div>
        <span class="fs-seta a2" aria-hidden="true">""" + SETA + r"""</span>
        <div class="fs-meio s2"><span class="cir">""" + svg(I['user']) + r"""</span><b>Especialista</b><span class="tag">Atende</span></div>
      </div>
    </div>
  </div>
</section>

"""

P4 = ['Diagnóstico gratuito', 'MVP do agente', 'Entrada na operação', 'Evolução contínua']
form = form.split('<div class="cab rv"><div class="selos">')[0] + (
    '<div class="cab rv"><span class="micro-l">Proposta de IA</span><h2 class="h1" id="pdT">Vamos construir um agente <span class="tone">para o seu negócio?</span></h2></div>\n'
    '    <ol class="passos4 rv" aria-label="Como funciona">' + ''.join('<li><span class="n">%02d</span>%s</li>' % (i + 1, t) for i, t in enumerate(P4)) + '</ol>\n'
    '    <div class="panel cd lit" id="panel">' + form.split('<div class="panel cd lit" id="panel">')[1])
form = form.replace('<!-- S11 · Diagnóstico gratuito (CTA final com selos e o formulário de proposta) -->', '<!-- S11 · Diagnóstico gratuito (CTA final com as etapas e o formulário de proposta) -->')
grade = como = faq = ''

# ================== v8: blocagem editorial (referência consultant-website): abertura com números, agentes em linhas, em operação, linha do tempo, perguntas e contato ==================
css += r"""
/* ---------- v8 · blocagem editorial ---------- */
.big{font-size:var(--text-stat);font-weight:var(--text-stat--font-weight);letter-spacing:var(--text-stat--letter-spacing);line-height:var(--text-stat--line-height)}
.cab-e{display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:end;column-gap:24px;row-gap:12px;margin-bottom:48px}
.cab-e .h2{grid-column:1;max-width:760px}
.cab-e p{grid-column:1;color:var(--fg-muted)}
.cab-e .link{grid-column:2;grid-row:1/3;align-self:end;white-space:nowrap}
.abre{padding-block:var(--section-y) 0}
.frase{max-width:1080px;font-size:var(--text-h2);font-weight:500;letter-spacing:var(--text-h2--letter-spacing);line-height:1.18}
.frase .tone{color:var(--fg-subtle)}
.nums3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;margin-top:72px}
.nums3 div{display:flex;flex-direction:column;gap:10px;padding-top:24px;border-top:1px solid var(--border)}
.nums3 .big{font-variant-numeric:tabular-nums}
.nums3 div > span:last-child{color:var(--fg-muted);font-size:var(--text-small)}
.linhas{list-style:none;margin:0;padding:0;border-bottom:1px solid var(--border)}
.linhas li a{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px;align-items:center;padding:30px 0;border-top:1px solid var(--border);transition:background-color var(--dur-fast) var(--ease-out)}
.linhas .t{grid-column:1/6;font-size:var(--text-h3);font-weight:500;letter-spacing:var(--text-h3--letter-spacing);line-height:var(--text-h3--line-height);transition:transform var(--dur-base) var(--ease-out),color var(--dur-fast)}
.linhas .d{grid-column:6/9;color:var(--fg-muted);font-size:var(--text-small)}
.linhas .m{grid-column:9/12;display:flex;flex-direction:column;gap:2px;font-size:var(--text-caption);color:var(--fg-subtle)}
.linhas .m b{font-weight:500;color:var(--fg)}
.linhas .seta{grid-column:12;justify-self:end;width:44px;height:44px;border-radius:50%;display:grid;place-items:center;box-shadow:inset 0 0 0 1px var(--border-strong);color:var(--fg);transition:background-color var(--dur-fast),color var(--dur-fast),box-shadow var(--dur-fast)}
.linhas .seta .ico{width:16px;height:16px}
.linhas li a:hover .t,.linhas li a:focus-visible .t{transform:translateX(8px);color:var(--brand-text)}
.linhas li a:hover .seta,.linhas li a:focus-visible .seta{background:var(--brand);color:var(--on-brand);box-shadow:none}
.linhas li a:focus-visible{outline:0}
.casos{display:flex;flex-direction:column;gap:16px}
.caso{padding:36px 40px;min-height:300px;display:flex;flex-direction:column;justify-content:space-between;gap:48px}
.caso .topo{display:flex;justify-content:space-between;align-items:center;gap:16px}
.caso .meta{display:flex;align-items:center;gap:12px;font-size:var(--text-small);color:var(--fg-muted)}
.caso .meta i{width:24px;height:24px;border-radius:50%;background:radial-gradient(circle at 30% 30%,var(--color-light-near),var(--brand) 60%,var(--color-rumo-800))}
.caso .base{display:flex;justify-content:space-between;align-items:flex-end;gap:32px}
.caso .base h3{font-size:var(--text-h3);font-weight:500;letter-spacing:var(--text-h3--letter-spacing);line-height:var(--text-h3--line-height)}
.caso .base p{color:var(--fg-muted);font-size:var(--text-small);margin-top:6px}
.caso .num{text-align:right;display:flex;flex-direction:column;align-items:flex-end;gap:6px}
.caso .num span:last-child{font-size:var(--text-caption);color:var(--fg-muted);max-width:260px}
.tempo{position:relative;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;padding-top:40px}
.tempo::before{content:"";position:absolute;left:5px;right:0;top:5px;height:1px;background:linear-gradient(90deg,var(--brand),var(--color-light-near) 50%,var(--color-rumo-800))}
.tempo li{position:relative;list-style:none;display:flex;flex-direction:column;gap:10px}
.tempo li::before{content:"";position:absolute;left:0;top:-40px;width:11px;height:11px;border-radius:50%;background:var(--brand);box-shadow:0 0 0 4px var(--bg),0 0 14px rgba(0,172,229,.8)}
.tempo li:nth-child(2)::before{background:var(--color-light-near)}
.tempo li:nth-child(3)::before{background:var(--color-light-core)}
.tempo li:nth-child(4)::before{background:var(--color-rumo-600)}
.tempo .tag{color:var(--fg-subtle)}
.tempo h3{font-size:var(--text-h4);font-weight:500;line-height:var(--text-h4--line-height)}
.tempo p{color:var(--fg-muted);font-size:var(--text-small)}
.tempo{margin:0;padding-left:0}
#faq .faq{max-width:none;gap:0;border-bottom:1px solid var(--border)}
#faq .qa,#faq .qa.open{border-radius:0;background:none;box-shadow:none;border-top:1px solid var(--border)}
#faq .qa-q{padding:24px 0}
#faq .qa-q .pm{box-shadow:inset 0 0 0 1px var(--border-strong)}
#faq .qa-a p{padding:0 0 24px;max-width:760px}
.contato{text-align:center;display:flex;flex-direction:column;align-items:center;gap:24px;max-width:820px;margin:0 auto}
.contato .lead{max-width:560px}
.contato .acts{display:flex;gap:16px;align-items:center;justify-content:center;flex-wrap:wrap;margin-top:8px}
@media (max-width:960px){
  .cab-e{grid-template-columns:1fr}.cab-e .link{grid-column:1;grid-row:auto}
  .nums3{grid-template-columns:1fr;margin-top:48px}
  .linhas .t{grid-column:1/12}.linhas .d,.linhas .m{grid-column:1/12;margin-top:10px}.linhas .seta{grid-column:12;grid-row:1}
  .caso{padding:28px;min-height:0}.caso .base{flex-direction:column;align-items:flex-start}.caso .num{text-align:left;align-items:flex-start}
  .tempo{grid-template-columns:1fr 1fr;row-gap:56px}
}
@media (max-width:640px){.tempo{grid-template-columns:1fr}.tempo::before{display:none}.tempo li::before{top:-24px}}
"""

ARROW = svg('<path d="M7 17 17 7"/><path d="M8 7h9v9"/>')

abre = r"""<!-- S03 · Manifesto e prova: a frase de abertura e três números -->
<section class="sec abre" id="sobre" aria-label="Sobre a Rumo AI">
  <div class="wrap">
    <p class="frase rv">Enquanto muitos só integram ferramentas prontas, a Rumo constrói. São quase três décadas desenvolvendo software e sustentando TI de missão crítica, <span class="tone">agora aplicadas a agentes que operam sozinhos e decidem em tempo real.</span></p>
    <div class="nums3 rv">
      <div><span class="big" data-conta="1997" data-de="1970">1997</span><span>Ano em que a Rumo começou a desenvolver software</span></div>
      <div><span class="big">+<span data-conta="70">70</span></span><span>Especialistas em atuação</span></div>
      <div><span class="big">24/7</span><span>Agentes atendendo pelo WhatsApp e por voz</span></div>
    </div>
  </div>
</section>

"""

DESC = {'Vendas e marketing': 'Qualificam leads, prospectam, ajustam preços e testam anúncios.',
        'Operações e processos': 'Leem documentos, atendem com contexto, fazem triagem e analisam contratos.',
        'Inteligência e decisão': 'Antecipam churn e demanda, monitoram a marca e detectam fraudes.'}
linhas = ''.join('      <li><a href="#contato" data-area="%s"><span class="t">%s</span><span class="d">%s</span><span class="m">%s</span><span class="seta">%s</span></a></li>\n'
                 % (area, area, DESC[area], ''.join('<b>%s</b>' % n for n, _ in ags), ARROW) for area, t1, t2, txt, ags in AREAS)
agentes = abre + r"""<!-- S04 · Serviços: os agentes, em linhas por área -->
<section class="sec" id="agentes" aria-labelledby="agT">
  <div class="wrap">
    <div class="cab-e rv">
      <h2 class="h2" id="agT">Um agente para cada área da sua empresa</h2>
      <p>Construídos sob medida, a partir de um diagnóstico gratuito.</p>
      <a class="link" href="#contato">Falar com um especialista """ + SETA + r"""</a>
    </div>
    <ul class="linhas rv">
""" + linhas + r"""    </ul>
  </div>
</section>

"""

CASOS = [
 ('Assistente virtual', 'Produto próprio · em operação', 'Sófi', 'Atende clientes e o time da Rumo pelo WhatsApp e faz a triagem antes de passar para um especialista.', '5', 'formatos que ela entende: áudio, vídeo, print, PDF e texto'),
 ('Recursos humanos', 'Agente de IA para RH', 'Recrutamento', 'Triagem de currículos, entrevista pelo WhatsApp e agendamento, num ecossistema que fica com o cliente.', 'Centenas', 'de currículos triados sem trabalho manual'),
]
casos = ''.join(
    '      <article class="caso cd lum rv"><div class="topo"><span class="meta"><i aria-hidden="true"></i>%s · %s</span></div>'
    '<div class="base"><div><h3>%s</h3><p>%s</p></div><div class="num"><span class="big">%s</span><span>%s</span></div></div></article>\n'
    % (a, b, t, d, n, l) for a, b, t, d, n, l in CASOS)
integ = grade = ''
sofi = r"""<!-- S07 · Produtos: agentes em operação -->
<section class="sec" id="operacao" aria-labelledby="opT">
  <div class="wrap">
    <div class="cab-e rv">
      <h2 class="h2" id="opT">Agentes que já estão trabalhando</h2>
      <p>O que eles fazem no dia a dia.</p>
    </div>
    <div class="casos">
""" + casos + r"""    </div>
  </div>
</section>

"""

TEMPO = [('Gratuito', 'Diagnóstico', 'Um especialista entende o seu processo e aponta onde um agente gera mais resultado.'),
         ('Primeiro recorte', 'MVP do agente', 'O agente roda numa parte do processo para validar com uso real.'),
         ('No seu fluxo', 'Entrada na operação', 'O agente passa a trabalhar com a sua equipe, nos canais que ela já usa.'),
         ('Contínuo', 'Evolução', 'Acompanhamos o uso e ensinamos novas tarefas ao agente.')]
como = r"""<!-- S05 · Narrativa: como um projeto acontece -->
<section class="sec" id="como-funciona" aria-labelledby="hwT">
  <div class="wrap">
    <div class="cab-e rv">
      <h2 class="h2" id="hwT">Como um projeto acontece</h2>
      <p>Do diagnóstico ao agente em operação, com a Rumo ao lado em cada etapa.</p>
    </div>
    <ol class="tempo rv">""" + ''.join('<li><span class="tag">%s</span><h3>%s</h3><p>%s</p></li>' % t for t in TEMPO) + r"""</ol>
  </div>
</section>

"""

FAQ2 = [
 ('Preciso trocar os meus sistemas?', 'Não. A Rumo conecta a IA a ERPs, CRMs e sistemas legados com uma integração não invasiva, sem reestruturar a infraestrutura e sem parar a operação.'),
 ('Os agentes são prontos?', 'São pontos de partida. Cada agente é construído e treinado sob medida para o processo, os dados e os sistemas da sua empresa.'),
 ('O agente e os dados ficam com quem?', 'Com a sua empresa. O ecossistema é seu, sem depender de plataformas de terceiros.'),
 ('Em quais canais os agentes atendem?', 'WhatsApp, voz, e-mail e redes sociais, conforme o processo. Um mesmo agente pode atender em mais de um canal.'),
]
faq = ('<!-- S13 · Perguntas frequentes -->\n<section class="sec" id="faq" aria-labelledby="fqT">\n  <div class="wrap">\n'
       '    <div class="cab-e rv"><h2 class="h2" id="fqT">Perguntas antes de começar</h2><p>Não achou a sua? Escreva para o time e um especialista responde.</p><a class="link" href="mailto:comercial@rumosolucoes.com">comercial@rumosolucoes.com ' + SETA + '</a></div>\n    <div class="faq rv">\n'
       + ''.join('      <div class="qa"><h3><button class="qa-q" type="button" aria-expanded="false" aria-controls="a%d">%s%s</button></h3><div class="qa-a" id="a%d" role="region"><div><p>%s</p></div></div></div>\n'
                 % (i, q, PM, i, a) for i, (q, a) in enumerate(FAQ2))
       + '    </div>\n  </div>\n</section>\n\n')

MAIL = 'mailto:comercial@rumosolucoes.com?subject=' + 'Diagn%C3%B3stico%20de%20IA'
form = r"""<!-- S14 · CTA final: contato com um especialista -->
<section class="sec" id="contato" aria-labelledby="ctT">
  <div class="wrap">
    <div class="contato rv">
      <span class="micro-l">Diagnóstico gratuito</span>
      <h2 class="h1" id="ctT">Conte o que você quer <span class="tone">automatizar.</span></h2>
      <p class="lead">Um especialista da Rumo responde e mapeia, sem custo, onde um agente gera mais resultado para a sua empresa.</p>
      <div class="acts">""" + '<a class="btn btn-primary" href="' + MAIL + '">Quero meu diagnóstico ' + SETA + r"""</a><a class="link" href="https://rumoai.io" rel="noopener">Conheça a Rumo AI """ + SETA + r"""</a></div>
    </div>
  </div>
</section>

</main>

<!--RODAPE-->

"""
hero = hero.replace('href="#proposta"', 'href="#contato"')

# JS: sem formulário e sem os exemplos antigos; números contam ao entrar na tela
js = js.replace("(function exemplos(){\n  const doc = $('#doc'), bi = $('#bi');", "(function exemplos(){\n  const doc = $('#doc'), bi = $('#bi'); if (!doc || !bi) return;")
i = js.index('/* ---------- agentes: o link do card leva ao formulário')
js = js[:i] + r"""/* ---------- abertura: os números contam ao entrar na tela ---------- */
(function contar(){
  const els = $$('[data-conta]'); if (!els.length) return;
  const rodar = el => { const fim = +el.dataset.conta, de = +(el.dataset.de || 0), t0 = performance.now(), dur = 1200; const f = t => { const k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3); el.textContent = Math.round(de + (fim - de) * e); if (k < 1) requestAnimationFrame(f); }; requestAnimationFrame(f); };
  if (reduce || !('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { io.unobserve(e.target); rodar(e.target); } }), { threshold: .6 });
  els.forEach(el => io.observe(el));
})();

"""
js_form_base = ''
js_submit = "})();\n</script>\n</body></html>\n"

# ================== v9: números de mercado com fonte, agentes separados com a característica de cada um, sem Sófi e Recrutamento ==================
css += r"""
/* ---------- v9 · números de mercado e agentes por área ---------- */
.nums3 .fonte{font-family:var(--font-mono);font-size:var(--text-mono-micro);letter-spacing:var(--text-mono-micro--letter-spacing);text-transform:uppercase;color:var(--fg-subtle)}
.nums3 .fonte a{color:inherit;text-decoration:underline;text-underline-offset:3px;text-decoration-color:var(--border-strong)}
.nums3 .fonte a:hover{color:var(--fg)}
.areas-ag{border-bottom:1px solid var(--border)}
.area-ag{padding:48px 0;border-top:1px solid var(--border);align-items:start}
.area-ag .cab-a{grid-column:1/5;display:flex;flex-direction:column;gap:14px;position:sticky;top:120px}
.area-ag .cab-a .n{font-family:var(--font-mono);font-size:var(--text-label);color:var(--brand-text)}
.area-ag .cab-a h3{font-size:var(--text-h3);font-weight:500;letter-spacing:var(--text-h3--letter-spacing);line-height:var(--text-h3--line-height)}
.area-ag .cab-a .tag{color:var(--fg-subtle)}
.ags4{grid-column:5/13;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));list-style:none;margin:0;padding:0;border-top:1px solid var(--border);border-left:1px solid var(--border)}
.ags4 li{border-right:1px solid var(--border);border-bottom:1px solid var(--border)}
.ags4 a{position:relative;display:flex;flex-direction:column;gap:10px;height:100%;padding:28px 56px 28px 28px;transition:background-color var(--dur-fast) var(--ease-out)}
.ags4 b{font-weight:500;font-size:var(--text-h4);line-height:var(--text-h4--line-height);transition:color var(--dur-fast) var(--ease-out)}
.ags4 span{color:var(--fg-muted);font-size:var(--text-small)}
.ags4 .ir{position:absolute;right:20px;top:26px;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;color:var(--fg-subtle);box-shadow:inset 0 0 0 1px var(--border);transition:background-color var(--dur-fast),color var(--dur-fast),box-shadow var(--dur-fast)}
.ags4 .ir .ico{width:13px;height:13px}
.ags4 a:hover,.ags4 a:focus-visible{background:rgba(0,172,229,.05);outline:0}
.ags4 a:hover b,.ags4 a:focus-visible b{color:var(--brand-text)}
.ags4 a:hover .ir,.ags4 a:focus-visible .ir{background:var(--brand);color:var(--on-brand);box-shadow:none}
@media (max-width:960px){.area-ag .cab-a{grid-column:1/-1;position:static;margin-bottom:24px}.ags4{grid-column:1/-1}}
@media (max-width:640px){.ags4{grid-template-columns:1fr}}
"""

NUMS = [
 ('88%', 'das empresas já usam IA em pelo menos uma área do negócio', 'McKinsey, The State of AI 2025', 'https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025'),
 ('17%', 'das empresas brasileiras usam aplicações de IA', 'Cetic.br, TIC Empresas 2025', 'https://cetic.br/media/docs/publicacoes/2/pt-br/20260831091252/TIC_EMPRESAS_2025_PT_RE.pdf'),
 ('80%', 'dos atendimentos de rotina devem ser resolvidos por agentes de IA até 2029', 'Gartner, 2025', 'https://www.gartner.com/en/newsroom/press-releases/2025-03-05-gartner-predicts-agentic-ai-will-autonomously-resolve-80-percent-of-common-customer-service-issues-without-human-intervention-by-20290'),
]
abre = r"""<!-- S03 · Manifesto e prova: a frase de abertura e três números do mercado, com fonte -->
<section class="sec abre" id="sobre" aria-label="Sobre a Rumo AI">
  <div class="wrap">
    <p class="frase rv">Enquanto muitos só integram ferramentas prontas, a Rumo constrói. São quase três décadas desenvolvendo software e sustentando TI de missão crítica, <span class="tone">agora aplicadas a agentes que operam sozinhos e decidem em tempo real.</span></p>
    <div class="nums3 rv">
""" + ''.join('      <div><span class="big"><span data-conta="%s">%s</span>%%</span><span class="leg">%s</span><span class="fonte">Fonte: <a href="%s" rel="noopener" target="_blank">%s</a></span></div>\n'
              % (v.rstrip('%'), v.rstrip('%'), l, u, f) for v, l, f, u in NUMS) + r"""    </div>
  </div>
</section>

"""
css += ".nums3 div > span.leg{color:var(--fg-muted);font-size:var(--text-small)}\n.nums3 div > span:last-child.fonte{font-size:var(--text-mono-micro);color:var(--fg-subtle)}\n"

AG = [
 ('Vendas e marketing', [
   ('Agente Qualificador 24/7', 'Converte leads via WhatsApp e Voz, entregando clientes prontos para o time comercial.'),
   ('Agente de Social Selling', 'Prospecção e engajamento automático no Instagram de forma humanizada e contínua.'),
   ('Agente de Precificação Dinâmica', 'Otimiza o valor de produtos e serviços em tempo real com base em dados e comportamento de mercado.'),
   ('Agente de Marketing Preditivo', 'Cria e testa centenas de anúncios com foco em máxima conversão.')]),
 ('Operações e processos', [
   ('Agente de RPA Cognitivo', 'Automatiza tarefas repetitivas lendo e interpretando documentos e e-mails complexos.'),
   ('Agente de Suporte “Nível Humano”', 'Atende com empatia, memória e contexto, reproduzindo a qualidade do seu melhor atendente.'),
   ('Agente de Recrutamento', 'Realiza triagem de currículos e conduz entrevistas iniciais automaticamente.'),
   ('Agente de Análise Contratual', 'Lê PDFs jurídicos e responde dúvidas sobre cláusulas e termos contratuais.')]),
 ('Inteligência e decisão', [
   ('Agente de Análise Preditiva', 'Antecipação de churn, demanda de mercado e comportamento do cliente (LTV).'),
   ('Agente de Análise de Sentimento', 'Monitora a reputação da marca nas redes e analisa emoções em tempo real.'),
   ('Agente “Jarvis” de BI', 'Permite conversar com os dados da sua empresa e gerar relatórios em linguagem natural.'),
   ('Agente de Segurança', 'Detecta fraudes e comportamentos suspeitos automaticamente.')]),
]
blocos = ''
for k, (area, ags) in enumerate(AG):
    blocos += ('      <div class="area-ag g12">\n        <div class="cab-a"><span class="n">%02d</span><h3>%s</h3><span class="tag">%d agentes</span></div>\n        <ul class="ags4">'
               % (k + 1, area, len(ags))
               + ''.join('<li><a href="#contato"><b>%s</b><span>%s</span><span class="ir">%s</span></a></li>' % (n, d, ARROW) for n, d in ags)
               + '</ul>\n      </div>\n')
agentes = abre + r"""<!-- S04 · Serviços: os agentes, separados por área, cada um com a sua característica -->
<section class="sec" id="agentes" aria-labelledby="agT">
  <div class="wrap">
    <div class="cab-e rv">
      <h2 class="h2" id="agT">Um agente para cada área da sua empresa</h2>
      <p>Construídos sob medida, a partir de um diagnóstico gratuito.</p>
      <a class="link" href="#contato">Falar com um especialista """ + SETA + r"""</a>
    </div>
    <div class="areas-ag rv">
""" + blocos + r"""    </div>
  </div>
</section>

"""
sofi = ''

# ================== v10: limpeza do código da Sófi, que saiu da página ==================
_i = css.index('/* ---------- S07 · Sófi em operação'); _j = css.index('/* ---------- S11 · CTA final', _i)
css = css[:_i] + css[_j:]
_i = js.index('/* ---------- Sófi: o quadro fica fixo'); _j = js.index('/* ----------', _i + 20)
js = js[:_i] + js[_j:]

# ================== v11: agentes em cards empilhados (padrão da Terceirização) com abas por agente e conversa ilustrativa (referência Octadesk) ==================
css += r"""
/* ---------- v11 · agentes: três cards empilhados, abas por agente e conversa ao lado ---------- */
.pilha-ag{position:relative}
.ag-c{position:sticky;display:block;margin-bottom:28px;min-height:620px}
.ag-c:nth-child(1){top:96px}.ag-c:nth-child(2){top:168px}.ag-c:nth-child(3){top:240px}
.ag-h{display:flex;align-items:center;gap:14px;height:72px;padding:0 24px;border-bottom:1px solid rgba(255,255,255,.08)}
.ag-h .q{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 30% 25%,var(--color-ink-800),var(--color-ink-950) 70%);box-shadow:inset 0 0 0 1px rgba(0,172,229,.45),0 0 18px -6px rgba(0,172,229,.6);color:var(--brand)}
.ag-h .q .ico{width:18px;height:18px}
.ag-h b{font-weight:500}
.ag-h .tag{margin-left:8px}
.ag-h .btn{margin-left:auto}
.ag-b{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px;padding:48px;align-items:start}
.ag-t{grid-column:1/7;display:flex;flex-direction:column;align-items:flex-start;gap:20px}
.ag-v{grid-column:7/13}
.abas-ag{list-style:none;margin:8px 0 0;padding:0;width:100%;border-top:1px solid var(--border)}
.abas-ag li{border-bottom:1px solid var(--border)}
.aba-ag{width:100%;display:flex;flex-direction:column;align-items:flex-start;gap:0;padding:16px 0;background:none;border:0;text-align:left;cursor:pointer;color:var(--fg-muted)}
.aba-ag .nm{display:flex;align-items:center;gap:12px;font-size:var(--text-body);font-weight:500;transition:color var(--dur-fast) var(--ease-out)}
.aba-ag .nm i{width:8px;height:8px;border-radius:50%;box-shadow:inset 0 0 0 1px var(--border-strong);transition:background-color var(--dur-fast),box-shadow var(--dur-fast)}
.aba-ag .ds{display:grid;grid-template-rows:0fr;transition:grid-template-rows var(--dur-base) var(--ease-out);font-size:var(--text-small);color:var(--fg-muted)}
.aba-ag .ds > span{overflow:hidden;padding-left:20px}
.aba-ag:hover .nm{color:var(--fg)}
.aba-ag[aria-selected="true"] .nm{color:var(--fg)}
.aba-ag[aria-selected="true"] .nm i{background:var(--brand);box-shadow:0 0 10px rgba(0,172,229,.8)}
.aba-ag[aria-selected="true"] .ds{grid-template-rows:1fr}
.aba-ag[aria-selected="true"] .ds > span{padding-top:8px}
.aba-ag:focus-visible{outline:0}
.aba-ag:focus-visible .nm{color:var(--brand-text)}
.ag-v .palco{min-height:470px}
.ag-v .msgs{min-height:320px}
.ag-v .msg.sis{margin-top:4px}
@media (max-width:960px){
  .ag-c{position:relative;top:auto!important;min-height:0}
  .ag-b{padding:28px}
  .ag-t,.ag-v{grid-column:1/-1}
  .ag-v{margin-top:28px}
  .ag-h .tag{display:none}
}
@media (max-width:640px){.ag-h .btn{display:none}}
"""

ICO_AREA = {'Vendas e marketing': I['chat'], 'Operações e processos': I['layers'], 'Inteligência e decisão': I['chart']}
TIT_AREA = {'Vendas e marketing': ('Leads atendidos', '24 horas por dia.'),
            'Operações e processos': ('Tarefas repetitivas', 'fora da fila da equipe.'),
            'Inteligência e decisão': ('Decisões com os dados', 'que você já tem.')}
# conversas ilustrativas: (canal, [(quem, texto)]); quem = c (cliente ou equipe), a (agente), s (sistema)
CONV = {
 'Agente Qualificador 24/7': ('WhatsApp', [('c', 'Oi, queria saber o valor para a minha empresa.'), ('a', 'Claro! Quantas pessoas vão usar no dia a dia?'), ('c', 'Umas 30.'), ('a', 'Perfeito. Passei o seu contato para um consultor, ele fala com você em instantes.'), ('s', 'Lead qualificado · enviado ao CRM')]),
 'Agente de Social Selling': ('Instagram', [('a', 'Vi que vocês abriram uma nova unidade, parabéns! Posso mostrar como outras lojas automatizam o atendimento?'), ('c', 'Pode sim, manda aí.'), ('a', 'Te enviei um resumo de 1 minuto. Quer marcar uma conversa?'), ('s', 'Conversa iniciada · Instagram')]),
 'Agente de Precificação Dinâmica': ('Equipe comercial', [('c', 'Qual o melhor preço para o produto X hoje?'), ('a', 'A demanda subiu e o estoque está baixo. Sugiro R$ 189, 6% acima do preço atual.'), ('c', 'Pode aplicar no site.'), ('s', 'Preço atualizado · e-commerce')]),
 'Agente de Marketing Preditivo': ('Equipe de marketing', [('c', 'Crie variações para a campanha de lançamento.'), ('a', 'Criei 24 variações e coloquei todas em teste. A versão 7 está convertendo o dobro.'), ('c', 'Concentra a verba nela.'), ('s', 'Campanha otimizada')]),
 'Agente de RPA Cognitivo': ('Financeiro', [('a', 'Li 42 e-mails de fornecedores hoje. Lancei 38 notas no ERP e separei 4 para revisão.'), ('c', 'Me mostra as 4.'), ('a', 'Enviei a lista com o motivo de cada uma.'), ('s', 'Notas lançadas · ERP')]),
 'Agente de Suporte “Nível Humano”': ('WhatsApp', [('c', 'Meu pedido ainda não chegou, e já é a segunda vez.'), ('a', 'Sinto muito, Ana. O pedido 4821 saiu ontem e chega amanhã até as 18h. Liberei frete grátis na sua próxima compra.'), ('c', 'Obrigada pela atenção!'), ('s', 'Atendimento resolvido')]),
 'Agente de Recrutamento': ('WhatsApp', [('a', 'Olá, Pedro! Seu currículo foi selecionado para a vaga de analista. Posso fazer três perguntas rápidas?'), ('c', 'Claro!'), ('a', 'Ótimo. Você tem disponibilidade para trabalho híbrido?'), ('s', 'Entrevista em andamento · RH')]),
 'Agente de Análise Contratual': ('Jurídico', [('c', 'Esse contrato tem multa por rescisão?'), ('a', 'Tem. A cláusula 9 prevê multa de 20% do valor restante, com aviso prévio de 30 dias.'), ('c', 'E o reajuste?'), ('a', 'Anual, pelo IPCA, na cláusula 5.')]),
 'Agente de Análise Preditiva': ('Equipe comercial', [('c', 'Quais clientes podem cancelar este mês?'), ('a', 'Encontrei 37 clientes com risco alto, a maioria sem uso há 15 dias. Quer uma campanha de retenção?'), ('c', 'Quero.'), ('s', 'Campanha criada · CRM')]),
 'Agente de Análise de Sentimento': ('Marketing', [('a', 'Alerta: as menções negativas à marca triplicaram nas últimas 2 horas, todas sobre atraso na entrega.'), ('c', 'De onde veio?'), ('a', 'De um post no Instagram com 12 mil visualizações. Já avisei o time de atendimento.'), ('s', 'Alerta enviado · atendimento')]),
 'Agente “Jarvis” de BI': ('Diretoria', [('c', 'Quanto vendemos em outubro por região?'), ('a', 'Sudeste R$ 1,2 mi, Sul R$ 640 mil e Nordeste R$ 410 mil. O Sul cresceu 18% sobre setembro.'), ('c', 'Gera o relatório.'), ('s', 'Relatório enviado · PDF')]),
 'Agente de Segurança': ('Segurança', [('a', 'Bloqueei uma compra de R$ 4.900 com o cartão de um cliente, 10 minutos depois de um login suspeito.'), ('c', 'Libera?'), ('a', 'Recomendo confirmar com o cliente. Enviei a verificação por SMS.'), ('s', 'Transação em análise')]),
}
import json as _json
cards_ag = ''
for k, (area, ags) in enumerate(AG):
    t1, t2 = TIT_AREA[area]
    abas = ''.join('<li><button class="aba-ag" type="button" role="tab" aria-selected="%s" tabindex="%s" data-ag="%s"><span class="nm"><i aria-hidden="true"></i>%s</span><span class="ds"><span>%s</span></span></button></li>'
                   % ('true' if j == 0 else 'false', '0' if j == 0 else '-1', n.replace('"', '&quot;'), n, d) for j, (n, d) in enumerate(ags))
    cards_ag += ('      <article class="ag-c cd lum" aria-labelledby="agC%d">\n' % k
                 + '        <div class="ag-h"><span class="q">%s</span><b id="agC%d">%s</b><span class="tag">%d agentes</span><a class="btn btn-secondary sm" href="#contato">Quero um agente</a></div>\n' % (svg(ICO_AREA[area]), k, area, len(ags))
                 + '        <div class="ag-b">\n'
                 + '          <div class="ag-t"><span class="micro-l">%02d · %s</span><h3 class="h2">%s <span class="tone">%s</span></h3><ul class="abas-ag" role="tablist" aria-label="Agentes de %s">%s</ul></div>\n' % (k + 1, area, t1, t2, area.lower(), abas)
                 + '          <div class="ag-v"><div class="palco"><div class="jan"><div class="jan-h"><div class="ag"><span class="cir">' + svg(I['bot']) + '</span><div><b class="jn"></b><br><span class="tag jc"></span></div></div><span class="tag">// exemplo</span></div>'
                 + '<div class="msgs" aria-live="off"></div><div class="jan-p"><span>Conversa ilustrativa.</span><button class="rep" type="button" hidden>' + svg(I['refresh']) + 'Repetir</button></div></div></div></div>\n'
                 + '        </div>\n      </article>\n')

agentes = abre + r"""<!-- S04 · Serviços: os agentes em cards empilhados por área, com abas e conversa ilustrativa -->
<section class="sec" id="agentes" aria-labelledby="agT">
  <div class="wrap">
    <div class="cab-e rv">
      <h2 class="h2" id="agT">Um agente para cada área da sua empresa</h2>
      <p>Escolha um agente e veja como ele trabalha.</p>
      <a class="link" href="#contato">Falar com um especialista """ + SETA + r"""</a>
    </div>
    <div class="pilha-ag">
""" + cards_ag + r"""    </div>
  </div>
</section>

"""

js = js.replace("/* ---------- abertura: os números contam ao entrar na tela ---------- */", r"""/* ---------- agentes: cada card tem abas; a aba escolhida mostra a descrição e digita a conversa ilustrativa ---------- */
(function cardsAgentes(){
  const CONV = """ + _json.dumps(CONV, ensure_ascii=False) + r""";
  $$('.ag-c').forEach(card => {
    const abas = $$('.aba-ag', card), box = $('.msgs', card), rep = $('.rep', card), nome = $('.jn', card), canal = $('.jc', card);
    let fila = [], atual = abas[0];
    const limpar = () => { fila.forEach(clearTimeout); fila = []; box.textContent = ''; rep.hidden = true; };
    const bolha = (quem, txt) => { const m = document.createElement('div'); m.className = 'msg ' + (quem === 'a' ? 'age' : quem === 's' ? 'sis' : 'cli'); m.textContent = quem === 'a' ? '' : txt; box.appendChild(m); return m; };
    const tocar = ab => {
      limpar(); const c = CONV[ab.dataset.ag]; if (!c) return;
      nome.textContent = ab.dataset.ag; canal.textContent = c[0];
      if (reduce) { c[1].forEach(([q, t]) => { const m = bolha(q, t); m.textContent = t; m.classList.add('on'); }); return; }
      let t = 250;
      c[1].forEach(([q, txt]) => {
        fila.push(setTimeout(() => {
          const m = bolha(q, txt); requestAnimationFrame(() => m.classList.add('on'));
          if (q === 'a') { const car = document.createElement('i'); car.className = 'car'; for (let k = 1; k <= txt.length; k++) fila.push(setTimeout(() => { m.textContent = txt.slice(0, k); if (k < txt.length) m.appendChild(car); }, 150 + k * 22)); }
        }, t));
        t += q === 'a' ? 150 + txt.length * 22 + 500 : 800;
      });
      fila.push(setTimeout(() => { rep.hidden = false; }, t));
    };
    const ativar = (ab, foco) => { abas.forEach(o => { const on = o === ab; o.setAttribute('aria-selected', on ? 'true' : 'false'); o.tabIndex = on ? 0 : -1; }); atual = ab; tocar(ab); if (foco) ab.focus(); };
    abas.forEach((ab, i) => {
      ab.addEventListener('click', () => ativar(ab));
      ab.addEventListener('keydown', e => { const d = (e.key === 'ArrowDown' || e.key === 'ArrowRight') ? 1 : (e.key === 'ArrowUp' || e.key === 'ArrowLeft') ? -1 : 0; if (d) { e.preventDefault(); ativar(abas[(i + d + abas.length) % abas.length], true); } });
    });
    rep.addEventListener('click', () => tocar(atual));
    nome.textContent = atual.dataset.ag; canal.textContent = (CONV[atual.dataset.ag] || [''])[0];
    if (!('IntersectionObserver' in window)) { tocar(atual); return; }
    const io = new IntersectionObserver(es => { if (es[0].isIntersecting) { io.disconnect(); tocar(atual); } }, { threshold: .35 });
    io.observe(card);
  });
})();

/* ---------- abertura: os números contam ao entrar na tela ---------- */""")

# ================== v12: cards dos agentes mais compactos ==================
css += r"""
.ag-c{min-height:0;margin-bottom:20px}
.ag-b{padding:36px 48px 40px}
.ag-v .palco{min-height:0;padding:20px}
.ag-v .msgs{min-height:268px;padding:16px}
.ag-t{gap:16px}
.aba-ag{padding:13px 0}
"""

# ================== v13: lógica de venda, menos texto, WhatsApp real em loop num card de destaque ==================
css += r"""
/* ---------- v13 · categorias como blocos clicáveis e agentes da categoria ---------- */
.cats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.cat{position:relative;display:flex;flex-direction:column;align-items:flex-start;gap:18px;padding:28px;border:0;border-radius:var(--radius-lg);background:none;box-shadow:inset 0 0 0 1px var(--border-strong);text-align:left;color:var(--fg);cursor:pointer;transition:background-color var(--dur-base) var(--ease-out),box-shadow var(--dur-base) var(--ease-out),color var(--dur-base) var(--ease-out)}
.cat .cir{width:48px;height:48px;border-radius:50%;display:grid;place-items:center;background:rgba(0,172,229,.12);color:var(--brand);transition:background-color var(--dur-base),color var(--dur-base)}
.cat .cir .ico{width:22px;height:22px}
.cat b{font-size:var(--text-h3);font-weight:500;letter-spacing:var(--text-h3--letter-spacing);line-height:var(--text-h3--line-height)}
.cat .tag{color:inherit;opacity:.7}
.cat:hover{box-shadow:inset 0 0 0 1px var(--brand)}
.cat[aria-selected="true"]{background:linear-gradient(150deg,var(--color-rumo-400),var(--brand) 45%,var(--color-rumo-600));color:var(--on-brand);box-shadow:0 24px 60px -28px rgba(0,172,229,.8)}
.cat[aria-selected="true"] .cir{background:var(--color-ink-950);color:var(--brand)}
.cat:focus-visible{outline:0;box-shadow:0 0 0 3px rgba(0,172,229,.45)}
.ags-cat{margin-top:16px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.ags-cat[hidden]{display:none}
.ags-cat.in{animation:cfEntra var(--dur-base) var(--ease-out)}
.ag1{display:flex;flex-direction:column;gap:10px;padding:24px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--border)}
.ag1 b{font-weight:500;font-size:var(--text-body)}
.ag1 span{color:var(--fg-muted);font-size:var(--text-small)}

/* ---------- v13 · destaque: card ciano com o celular e o WhatsApp real, em loop ---------- */
.destaque{position:relative;border-radius:var(--radius-lg);overflow:hidden;background:linear-gradient(150deg,var(--color-rumo-400) 0%,var(--brand) 42%,var(--color-rumo-700) 100%);color:var(--on-brand);display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px;align-items:center;padding:64px;min-height:680px}
.destaque .tx{grid-column:1/7;display:flex;flex-direction:column;align-items:flex-start;gap:24px}
.destaque .micro-l{color:var(--on-brand)}
.destaque .micro-l::before{background:var(--on-brand)}
.destaque .h2 .tone{color:rgba(5,5,5,.6)}
.fila-ag{list-style:none;margin:8px 0 0;padding:0;display:flex;flex-direction:column;gap:8px;width:100%;max-width:420px}
.fila-ag li{display:flex;align-items:center;gap:14px;height:56px;padding:0 18px;border-radius:var(--radius-pill);background:rgba(5,5,5,.08);font-weight:500;transition:background-color var(--dur-base) var(--ease-out),color var(--dur-base)}
.fila-ag li i{width:10px;height:10px;border-radius:50%;background:rgba(5,5,5,.3);transition:background-color var(--dur-base)}
.fila-ag li.on{background:var(--color-ink-950);color:var(--fg)}
.fila-ag li.on i{background:var(--brand)}
.destaque .vis{grid-column:8/13;display:flex;justify-content:center}
.fone{width:340px;border-radius:var(--radius-panel);padding:12px;background:var(--color-ink-950);box-shadow:0 40px 80px -30px rgba(5,5,5,.75),inset 0 0 0 1px rgba(255,255,255,.12)}
.wa{border-radius:var(--radius-lg);overflow:hidden;background:var(--wa-fundo);display:flex;flex-direction:column;height:560px}
.wa-h{display:flex;align-items:center;gap:12px;padding:44px 16px 12px;background:var(--wa-cabecalho);color:var(--wa-entrada)}
.wa-h .av{width:38px;height:38px;border-radius:50%;display:grid;place-items:center;background:var(--wa-entrada);color:var(--wa-cabecalho)}
.wa-h .av .ico{width:20px;height:20px}
.wa-h b{display:block;font-weight:500;font-size:var(--text-body)}
.wa-h small{font-size:var(--text-caption);opacity:.85}
.wa-c{flex:1;padding:16px 12px;display:flex;flex-direction:column;gap:8px;overflow:hidden;background-image:radial-gradient(rgba(17,27,33,.06) 1px,transparent 1.2px);background-size:18px 18px}
.wa-d{align-self:center;padding:5px 12px;border-radius:var(--radius-md);background:var(--wa-entrada);color:var(--wa-meta);font-size:var(--text-caption);box-shadow:0 1px 1px rgba(17,27,33,.12)}
.wb{position:relative;max-width:80%;padding:7px 10px 18px;border-radius:var(--radius-md);font-size:var(--text-small);line-height:1.4;color:var(--wa-texto);box-shadow:0 1px 1px rgba(17,27,33,.12);opacity:0;transform:translateY(6px);transition:opacity var(--dur-fast) var(--ease-out),transform var(--dur-fast) var(--ease-out)}
.wb.on{opacity:1;transform:none}
.wb.in{align-self:flex-start;background:var(--wa-entrada);border-top-left-radius:0}
.wb.out{align-self:flex-end;background:var(--wa-saida);border-top-right-radius:0}
.wb .hr{position:absolute;right:8px;bottom:4px;display:flex;align-items:center;gap:3px;font-size:var(--text-mono-micro);color:var(--wa-meta)}
.wb .hr svg{width:16px;height:11px;fill:none;stroke:var(--wa-check);stroke-width:1.6}
.wa-p{display:flex;align-items:center;gap:8px;padding:8px 10px 18px}
.wa-p span{flex:1;height:40px;border-radius:var(--radius-pill);background:var(--wa-entrada);display:flex;align-items:center;padding:0 16px;color:var(--wa-meta);font-size:var(--text-small)}
.wa-p i{width:40px;height:40px;border-radius:50%;background:var(--wa-cabecalho)}
.destaque small.nota{font-size:var(--text-caption);opacity:.7}

/* ---------- v13 · como trabalhamos: fluxo interativo, sem caixa preta ---------- */
#como-funciona .cf-wrap{border-top:1px solid var(--border)}
#como-funciona .cf-p{padding:40px 0 0;min-height:0}
#como-funciona .cf-card{background:none;box-shadow:inset 0 0 0 1px var(--border)}

/* ---------- v13 · consultoria ---------- */
.consult{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px;align-items:center;padding:56px 64px;border-radius:var(--radius-lg);background:radial-gradient(80% 140% at 100% 0%,rgba(0,172,229,.35),rgba(0,172,229,0) 60%),var(--color-ink-925);box-shadow:inset 0 0 0 1px rgba(0,172,229,.35)}
.consult .tx{grid-column:1/8;display:flex;flex-direction:column;align-items:flex-start;gap:16px}
.consult .tx p{color:var(--fg-muted);max-width:560px}
.consult .acao{grid-column:9/13;display:flex;flex-direction:column;align-items:flex-start;gap:12px}
.consult .acao small{font-size:var(--text-caption);color:var(--fg-subtle)}

@media (max-width:960px){
  .cats,.ags-cat{grid-template-columns:1fr 1fr}
  .destaque{padding:32px;min-height:0;row-gap:40px}.destaque .tx,.destaque .vis{grid-column:1/-1}
  .consult{padding:32px;row-gap:24px}.consult .tx,.consult .acao{grid-column:1/-1}
}
@media (max-width:640px){.cats,.ags-cat{grid-template-columns:1fr}.fone{width:100%;max-width:320px}}
"""

ICO_CAT = {'Vendas e marketing': I['chat'], 'Operações e processos': I['layers'], 'Inteligência e decisão': I['chart']}
abre = r"""<!-- S03 · Manifesto e prova: frase de efeito comprovada por números do mercado -->
<section class="sec abre" id="sobre" aria-label="Sobre a Rumo AI">
  <div class="wrap">
    <p class="frase rv">Enquanto muitos só usam ferramentas prontas, <span class="tone">a Rumo constrói agentes de IA sob medida para a sua operação.</span></p>
    <div class="nums3 rv">
""" + ''.join('      <div><span class="big"><span data-conta="%s">%s</span>%%</span><span class="leg">%s</span><span class="fonte">Fonte: <a href="%s" rel="noopener" target="_blank">%s</a></span></div>\n'
              % (v.rstrip('%'), v.rstrip('%'), l, u, f) for v, l, f, u in NUMS) + r"""    </div>
  </div>
</section>

"""
cats = ''.join('<button class="cat" type="button" role="tab" id="cat%d" aria-controls="agc%d" aria-selected="%s" tabindex="%s"><span class="cir">%s</span><b>%s</b><span class="tag">4 agentes</span></button>'
               % (k, k, 'true' if k == 0 else 'false', '0' if k == 0 else '-1', svg(ICO_CAT[a]), a) for k, (a, _) in enumerate(AG))
listas = ''.join('      <div class="ags-cat" role="tabpanel" id="agc%d" aria-labelledby="cat%d"%s>%s</div>\n'
                 % (k, k, '' if k == 0 else ' hidden', ''.join('<div class="ag1"><b>%s</b><span>%s</span></div>' % (n, d) for n, d in ags)) for k, (a, ags) in enumerate(AG))
agentes = abre + r"""<!-- S04 · Serviços: as três áreas e, ao escolher uma, os agentes dela -->
<section class="sec" id="agentes" aria-labelledby="agT">
  <div class="wrap">
    <div class="cab-e rv">
      <h2 class="h2" id="agT">Construímos agentes para cada área da operação</h2>
      <p>Escolha uma área e veja os agentes dela.</p>
    </div>
    <div class="cats rv" role="tablist" aria-label="Áreas">""" + cats + r"""</div>
""" + listas + r"""  </div>
</section>

"""

LOOP = [('Agente Qualificador 24/7', 'Vendas e marketing'), ('Agente de Suporte “Nível Humano”', 'Operações e processos'), ('Agente de Recrutamento', 'Operações e processos')]
CHAT = {
 'Agente Qualificador 24/7': ('Loja Exemplo', [('out', 'Oi, queria saber o valor para a minha empresa.'), ('in', 'Olá! Claro. Quantas pessoas vão usar no dia a dia?'), ('out', 'Umas 30.'), ('in', 'Perfeito! Já passei o seu contato para um consultor. Ele fala com você em instantes.')]),
 'Agente de Suporte “Nível Humano”': ('Loja Exemplo', [('out', 'Meu pedido ainda não chegou, e já é a segunda vez.'), ('in', 'Sinto muito, Ana. O pedido 4821 saiu ontem e chega amanhã até as 18h.'), ('in', 'Para compensar, liberei frete grátis na sua próxima compra.'), ('out', 'Obrigada pela atenção!')]),
 'Agente de Recrutamento': ('RH Exemplo', [('in', 'Olá, Pedro! Seu currículo foi selecionado para a vaga de analista. Posso fazer três perguntas rápidas?'), ('out', 'Claro!'), ('in', 'Ótimo. Você tem disponibilidade para trabalho híbrido?'), ('out', 'Tenho sim.')]),
}
fila = ''.join('<li%s><i aria-hidden="true"></i>%s</li>' % (' class="on"' if k == 0 else '', n) for k, (n, _) in enumerate(LOOP))
integ = r"""<!-- S06 · Destaque Rumo AI: um agente trabalhando no WhatsApp, em loop -->
<section class="sec" id="destaque" aria-labelledby="dsT">
  <div class="wrap">
    <div class="destaque rv" id="destaqueAg">
      <div class="tx">
        <span class="micro-l">Na prática</span>
        <h2 class="h2" id="dsT">Veja um agente <span class="tone">atendendo no WhatsApp.</span></h2>
        <ol class="fila-ag" id="filaAg">""" + fila + r"""</ol>
        <small class="nota">Conversas ilustrativas.</small>
      </div>
      <div class="vis" aria-hidden="true">
        <div class="fone"><div class="wa">
          <div class="wa-h"><span class="av">""" + svg(I['bot']) + r"""</span><div><b id="waNome">Loja Exemplo</b><small id="waStatus">online</small></div></div>
          <div class="wa-c" id="waConversa"><span class="wa-d">Hoje</span></div>
          <div class="wa-p"><span>Mensagem</span><i></i></div>
        </div></div>
      </div>
    </div>
  </div>
</section>

"""
grade = sofi = ''

ck = '<span class="ck">' + svg(CHK) + '</span>'
row = lambda t: '<div class="cf-r"><span class="l">' + ck + t + '</span></div>'
ETAPAS2 = [
 ('Diagnóstico', 'Gratuito', 'Entendemos o seu processo e apontamos onde um agente gera mais resultado.', [row('Processo mapeado'), row('Ganho identificado')]),
 ('MVP', 'Primeiro recorte', 'O agente roda numa parte do processo para validar com uso real.', [row('Agente treinado com os seus dados'), row('Teste com uso real')]),
 ('Operação', 'No seu fluxo', 'O agente entra no dia a dia da equipe, nos canais que ela já usa.', [row('Canal conectado'), row('Equipe usando')]),
 ('Evolução', 'Contínuo', 'Acompanhamos o uso e ensinamos novas tarefas ao agente.', [row('Uso monitorado'), row('Novas tarefas')]),
]
nav2 = ''.join('<button class="cf-s" type="button" role="tab" id="cfS%d" aria-controls="cfP%d" aria-selected="%s" tabindex="%s"><span class="n">%02d</span><span>%s</span><span class="tag">%s</span></button>'
               % (i + 1, i + 1, 'true' if i == 0 else 'false', '0' if i == 0 else '-1', i + 1, t, q) for i, (t, q, _, _) in enumerate(ETAPAS2))
pans2 = ''.join('      <div class="cf-p" role="tabpanel" id="cfP%d" aria-labelledby="cfS%d"%s><div class="cf-t"><h3 class="h3">%s</h3><p>%s</p></div><div class="cf-v"><div class="cf-card">%s</div></div></div>\n'
                % (i + 1, i + 1, '' if i == 0 else ' hidden', t, d, ''.join(v)) for i, (t, _, d, v) in enumerate(ETAPAS2))
MAILR = 'mailto:comercial@rumosolucoes.com?subject=' + 'Agendar%20reuni%C3%A3o%20sobre%20IA'
como = r"""<!-- S05 · Narrativa: como trabalhamos, em fluxo interativo -->
<section class="sec" id="como-funciona" aria-labelledby="hwT">
  <div class="wrap">
    <div class="cab-e rv">
      <h2 class="h2" id="hwT">Como trabalhamos</h2>
      <p>Um fluxo em quatro etapas. Clique para ver cada uma.</p>
    </div>
    <div class="cf-nav rv" role="tablist" aria-label="Etapas"><span class="cf-linha" aria-hidden="true"><i id="cfLinha"></i></span>""" + nav2 + r"""</div>
    <div class="cf-wrap">
""" + pans2 + r"""    </div>
  </div>
</section>

<!-- S14 · CTA final: consultoria para descobrir o que automatizar -->
<section class="sec" id="contato" aria-labelledby="ctT">
  <div class="wrap">
    <div class="consult rv">
      <div class="tx">
        <span class="micro-l">Consultoria</span>
        <h2 class="h2" id="ctT">Ainda não sabe o que automatizar?</h2>
        <p>Agende uma reunião. Um especialista da Rumo mapeia com você o que dá para automatizar na sua empresa.</p>
      </div>
      <div class="acao">""" + '<a class="btn btn-primary" href="' + MAILR + '">Agendar uma reunião ' + SETA + '</a>' + r"""<small>Sem custo e sem compromisso.</small></div>
    </div>
  </div>
</section>

"""
faq = faq.replace('Perguntas antes de começar', 'Perguntas frequentes')
form = "</main>\n\n<!--RODAPE-->\n\n"

js = js.replace("/* ---------- abertura: os números contam ao entrar na tela ---------- */", r"""/* ---------- agentes: as áreas funcionam como abas; a escolhida mostra os seus agentes ---------- */
(function categorias(){
  const bs = $$('.cat'); if (!bs.length) return;
  const ativar = (b, foco) => { bs.forEach(o => { const on = o === b; o.setAttribute('aria-selected', on ? 'true' : 'false'); o.tabIndex = on ? 0 : -1; const p = $('#' + o.getAttribute('aria-controls')); p.hidden = !on; if (on) { p.classList.remove('in'); void p.offsetWidth; p.classList.add('in'); } }); if (foco) b.focus(); };
  bs.forEach((b, i) => {
    b.addEventListener('click', () => ativar(b));
    b.addEventListener('keydown', e => { const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0; if (d) { e.preventDefault(); ativar(bs[(i + d + bs.length) % bs.length], true); } });
  });
})();

/* ---------- destaque: o WhatsApp mostra os agentes em loop; pausa fora da tela e com o cursor sobre o card ---------- */
(function whatsapp(){
  const box = $('#waConversa'), card = $('#destaqueAg'); if (!box) return;
  const LOOP = """ + _json.dumps([n for n, _ in LOOP], ensure_ascii=False) + r""", CHAT = """ + _json.dumps(CHAT, ensure_ascii=False) + r""";
  const itens = $$('#filaAg li'), nome = $('#waNome'), status = $('#waStatus');
  const TICK = '<svg viewBox="0 0 16 11" aria-hidden="true"><path d="M1 6l3 3 6-7"/><path d="M6 9l1 1 7-8"/></svg>';
  let i = 0, fila = [], visivel = false, pausado = false, tocando = false;
  const hora = n => '10:' + String(12 + n).padStart(2, '0');
  const limpar = () => { fila.forEach(clearTimeout); fila = []; box.innerHTML = '<span class="wa-d">Hoje</span>'; };
  const bolha = (lado, txt, n) => { const b = document.createElement('div'); b.className = 'wb ' + lado; b.textContent = txt; const h = document.createElement('span'); h.className = 'hr'; h.innerHTML = hora(n) + (lado === 'out' ? TICK : ''); b.appendChild(h); box.appendChild(b); requestAnimationFrame(() => b.classList.add('on')); };
  const tocar = () => {
    if (!visivel || pausado) { tocando = false; return; }
    tocando = true; limpar();
    const ag = LOOP[i], c = CHAT[ag]; nome.textContent = c[0]; status.textContent = 'online';
    itens.forEach((li, k) => li.classList.toggle('on', k === i));
    let t = 500;
    c[1].forEach(([lado, txt], n) => {
      if (lado === 'in') { fila.push(setTimeout(() => { status.textContent = 'digitando...'; }, t)); t += 900; }
      fila.push(setTimeout(() => { bolha(lado, txt, n); status.textContent = 'online'; }, t));
      t += lado === 'in' ? 1400 : 1100;
    });
    fila.push(setTimeout(() => { i = (i + 1) % LOOP.length; tocar(); }, t + 1800));
  };
  if (reduce) { visivel = true; const c = CHAT[LOOP[0]]; c[1].forEach(([l, x], n) => bolha(l, x, n)); $$('.wb', box).forEach(b => b.classList.add('on')); return; }
  card.addEventListener('pointerenter', () => { pausado = true; });
  card.addEventListener('pointerleave', () => { pausado = false; if (!tocando) tocar(); });
  if (!('IntersectionObserver' in window)) { visivel = true; tocar(); return; }
  new IntersectionObserver(es => { visivel = es[0].isIntersecting; if (visivel && !tocando) tocar(); }, { threshold: .3 }).observe(card);
})();

/* ---------- abertura: os números contam ao entrar na tela ---------- */""")

# ================== v14: uma seção por categoria (clean) com o celular do WhatsApp solto, e o Como trabalhamos refeito ==================
css += r"""
/* ---------- v14 · categorias: uma seção por área, lista clean e celular solto ---------- */
.intro-cat{padding-bottom:0}
.atalhos{display:flex;flex-wrap:wrap;gap:10px;margin-top:4px}
.atalhos a{display:inline-flex;align-items:center;gap:10px;height:44px;padding:0 18px;border-radius:var(--radius-pill);box-shadow:inset 0 0 0 1px var(--border-strong);font-size:var(--text-small);font-weight:500;color:var(--fg);transition:box-shadow var(--dur-fast),color var(--dur-fast)}
.atalhos a .n{font-family:var(--font-mono);font-size:var(--text-mono-micro);color:var(--brand-text)}
.atalhos a:hover{box-shadow:inset 0 0 0 1px var(--brand);color:var(--brand-text)}
.cat-g{align-items:center}
.cat-tx{grid-column:1/7;display:flex;flex-direction:column;align-items:flex-start;gap:20px}
.cat-tx .sub{color:var(--fg-muted);font-size:var(--text-lead);line-height:var(--text-lead--line-height);max-width:520px}
.cat-vis{grid-column:8/13;position:relative;display:flex;justify-content:center}
.cat-g.inv .cat-tx{grid-column:7/13;grid-row:1}
.cat-g.inv .cat-vis{grid-column:1/6;grid-row:1}
.cat-vis::before{content:"";position:absolute;left:50%;top:50%;width:520px;height:520px;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(closest-side,rgba(0,172,229,.32),rgba(0,172,229,.1) 55%,rgba(0,172,229,0));pointer-events:none}
.cat-vis .fone{position:relative}
.ag-l{list-style:none;margin:8px 0 0;padding:0;width:100%;border-top:1px solid var(--border)}
.ag-l li{display:grid;grid-template-columns:40px 1fr;gap:4px 16px;padding:20px 0;border-bottom:1px solid var(--border)}
.ag-l .cir{grid-row:1/3;width:40px;height:40px;border-radius:50%;display:grid;place-items:center;background:rgba(0,172,229,.12);color:var(--brand)}
.ag-l .cir .ico{width:18px;height:18px}
.ag-l b{font-weight:500}
.ag-l span.d{grid-column:2;color:var(--fg-muted);font-size:var(--text-small)}

/* ---------- v14 · como trabalhamos: quatro etapas em cards, com o que o cliente recebe em cada uma ---------- */
.fluxo4{position:relative;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;padding-top:28px}
.fluxo4 .barra{position:absolute;left:0;right:0;top:0;height:2px;border-radius:var(--radius-xs);background:var(--border)}
.fluxo4 .barra i{position:absolute;inset:0;transform-origin:left;transform:scaleX(.25);background:linear-gradient(90deg,var(--color-rumo-700),var(--brand),var(--color-light-near));transition:transform var(--dur-slow) var(--ease-out)}
.passo{position:relative;display:flex;flex-direction:column;align-items:flex-start;gap:16px;min-height:340px;padding:28px;border:0;border-radius:var(--radius-lg);background:none;box-shadow:inset 0 0 0 1px var(--border);text-align:left;color:var(--fg);cursor:pointer;transition:background-color var(--dur-base) var(--ease-out),box-shadow var(--dur-base) var(--ease-out)}
.passo .n{font-family:var(--font-mono);font-size:var(--text-label);color:var(--fg-subtle);transition:color var(--dur-base)}
.passo .cir{width:52px;height:52px;border-radius:50%;display:grid;place-items:center;background:rgba(255,255,255,.06);color:var(--fg-muted);transition:background-color var(--dur-base),color var(--dur-base),box-shadow var(--dur-base)}
.passo .cir .ico{width:22px;height:22px}
.passo .t{font-size:var(--text-h3);font-weight:500;letter-spacing:var(--text-h3--letter-spacing);line-height:var(--text-h3--line-height)}
.passo .pp{color:var(--fg-muted);font-size:var(--text-small)}
.passo .entrega{margin-top:auto;display:flex;flex-direction:column;gap:6px;width:100%;padding-top:16px;border-top:1px solid var(--border)}
.passo .entrega .tag{color:var(--fg-subtle)}
.passo .entrega b{font-weight:500;font-size:var(--text-small)}
.passo:hover{box-shadow:inset 0 0 0 1px var(--border-strong)}
.passo.on{background:radial-gradient(90% 70% at 50% 0%,rgba(0,172,229,.16),rgba(0,172,229,0) 70%),var(--color-ink-925);box-shadow:inset 0 0 0 1px rgba(0,172,229,.55),0 30px 60px -30px rgba(0,172,229,.55)}
.passo.on .n{color:var(--brand-text)}
.passo.on .cir{background:var(--brand);color:var(--on-brand);box-shadow:0 0 0 6px rgba(0,172,229,.14),0 0 28px -6px rgba(0,172,229,.8)}
.passo:focus-visible{outline:0;box-shadow:0 0 0 3px rgba(0,172,229,.45)}

@media (max-width:960px){
  .cat-tx,.cat-vis,.cat-g.inv .cat-tx,.cat-g.inv .cat-vis{grid-column:1/-1;grid-row:auto}
  .cat-vis{margin-top:48px}
  .fluxo4{grid-template-columns:1fr 1fr}
  .passo{min-height:0}
}
@media (max-width:640px){.fluxo4{grid-template-columns:1fr}.cat-vis::before{width:340px;height:340px}}
"""

I2 = {
 'Agente Qualificador 24/7': I['chat'], 'Agente de Social Selling': I['user'], 'Agente de Precificação Dinâmica': I['sliders'], 'Agente de Marketing Preditivo': I['chart'],
 'Agente de RPA Cognitivo': I['file'], 'Agente de Suporte “Nível Humano”': I['chat'], 'Agente de Recrutamento': I['user'], 'Agente de Análise Contratual': I['file'],
 'Agente de Análise Preditiva': I['chart'], 'Agente de Análise de Sentimento': I['pulse'], 'Agente “Jarvis” de BI': I['code'], 'Agente de Segurança': I['shield'],
}
SUB = {'Vendas e marketing': 'Para atrair, qualificar e converter clientes sem aumentar o time.',
       'Operações e processos': 'Para tirar da equipe o trabalho repetitivo e manual.',
       'Inteligência e decisão': 'Para decidir com base nos dados que a empresa já tem.'}
IDS = {'Vendas e marketing': 'vendas', 'Operações e processos': 'operacoes', 'Inteligência e decisão': 'decisao'}
TIT = {'Vendas e marketing': ('Agentes de', 'vendas e marketing.'), 'Operações e processos': ('Agentes de', 'operações e processos.'), 'Inteligência e decisão': ('Agentes de', 'inteligência e decisão.')}
CONVS = {'Vendas e marketing': ['Agente Qualificador 24/7'], 'Operações e processos': ['Agente de Suporte “Nível Humano”', 'Agente de Recrutamento'], 'Inteligência e decisão': ['Agente “Jarvis” de BI']}
CHAT['Agente “Jarvis” de BI'] = ('BI da Empresa', [('out', 'Quanto vendemos em outubro por região?'), ('in', 'Sudeste R$ 1,2 mi, Sul R$ 640 mil e Nordeste R$ 410 mil. O Sul cresceu 18% sobre setembro.'), ('out', 'Me manda o relatório?'), ('in', 'Pronto! Enviei o PDF no seu e-mail.')])

def fone(convs):
    return ('<div class="fone" data-convs="%s" aria-hidden="true"><div class="wa">'
            '<div class="wa-h"><span class="av">%s</span><div><b class="wa-nome">%s</b><small class="wa-st">online</small></div></div>'
            '<div class="wa-c"><span class="wa-d">Hoje</span></div><div class="wa-p"><span>Mensagem</span><i></i></div></div></div>'
            % (_json.dumps(convs, ensure_ascii=False).replace('"', '&quot;'), svg(I['bot']), CHAT[convs[0]][0]))

intro = abre + r"""<!-- S04 · Serviços: as três áreas em que construímos agentes -->
<section class="sec intro-cat" id="agentes" aria-labelledby="agT">
  <div class="wrap">
    <div class="cab-e rv">
      <h2 class="h2" id="agT">Construímos agentes para três áreas da operação</h2>
      <div class="atalhos">""" + ''.join('<a href="#%s"><span class="n">%02d</span>%s</a>' % (IDS[a], k + 1, a) for k, (a, _) in enumerate(AG)) + r"""</div>
    </div>
  </div>
</section>

"""
secs = ''
for k, (area, ags) in enumerate(AG):
    t1, t2 = TIT[area]
    secs += ('<!-- S04 · Serviços: agentes de %s -->\n<section class="sec" id="%s" aria-labelledby="ct%d">\n  <div class="wrap">\n    <div class="g12 cat-g%s">\n'
             % (area.lower(), IDS[area], k, ' inv' if k == 1 else '')
             + '      <div class="cat-tx rv"><span class="micro-l">%02d · %s</span><h2 class="h2" id="ct%d">%s <span class="tone">%s</span></h2><p class="sub">%s</p>' % (k + 1, area, k, t1, t2, SUB[area])
             + '<ul class="ag-l">' + ''.join('<li><span class="cir">%s</span><b>%s</b><span class="d">%s</span></li>' % (svg(I2[n]), n, d) for n, d in ags) + '</ul></div>\n'
             + '      <div class="cat-vis rv">' + fone(CONVS[area]) + '</div>\n'
             + '    </div>\n  </div>\n</section>\n\n')
agentes = intro + secs
integ = ''

FL = [
 ('search', 'Diagnóstico', 'Entendemos o seu processo e apontamos onde um agente gera mais resultado.', 'Mapa do que automatizar primeiro'),
 ('sliders', 'MVP', 'O primeiro agente roda numa parte do processo para validar com uso real.', 'Um agente funcionando com os seus dados'),
 ('layers', 'Operação', 'O agente entra no dia a dia da equipe, integrado aos sistemas e canais.', 'Agente integrado à sua rotina'),
 ('pulse', 'Evolução', 'Acompanhamos o uso, ajustamos o treinamento e ensinamos novas tarefas.', 'Acompanhamento contínuo'),
]
I['search'] = '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>'
passos = ''.join('<button class="passo%s" type="button" data-i="%d"><span class="n">%02d</span><span class="cir">%s</span><span class="t">%s</span><span class="pp">%s</span><span class="entrega"><span class="tag">O que você recebe</span><b>%s</b></span></button>'
                 % (' on' if i == 0 else '', i, i + 1, svg(I[ic]), t, d, e) for i, (ic, t, d, e) in enumerate(FL))
consult = como[como.index('<!-- S14 · CTA final'):]
como = r"""<!-- S05 · Narrativa: como trabalhamos, em quatro etapas -->
<section class="sec" id="como-funciona" aria-labelledby="hwT">
  <div class="wrap">
    <div class="cab-e rv">
      <h2 class="h2" id="hwT">Como trabalhamos</h2>
      <p>Do diagnóstico à evolução contínua, com a Rumo ao lado em cada etapa.</p>
    </div>
    <div class="fluxo4 rv" id="fluxo4"><span class="barra" aria-hidden="true"><i id="fluxoBarra"></i></span>""" + passos + r"""</div>
  </div>
</section>

""" + consult

js = js.replace("/* ---------- abertura: os números contam ao entrar na tela ---------- */", r"""/* ---------- categorias: cada celular mostra as conversas da sua área em loop; pausa fora da tela ---------- */
(function celulares(){
  const CHAT2 = """ + _json.dumps(CHAT, ensure_ascii=False) + r""";
  const TICK = '<svg viewBox="0 0 16 11" aria-hidden="true"><path d="M1 6l3 3 6-7"/><path d="M6 9l1 1 7-8"/></svg>';
  $$('.fone[data-convs]').forEach(f => {
    const lista = JSON.parse(f.dataset.convs), box = $('.wa-c', f), nome = $('.wa-nome', f), st = $('.wa-st', f);
    let i = 0, fila = [], visivel = false, tocando = false;
    const bolha = (lado, txt, n) => { const b = document.createElement('div'); b.className = 'wb ' + lado; b.textContent = txt; const h = document.createElement('span'); h.className = 'hr'; h.innerHTML = '10:' + String(12 + n).padStart(2, '0') + (lado === 'out' ? TICK : ''); b.appendChild(h); box.appendChild(b); requestAnimationFrame(() => b.classList.add('on')); };
    const tocar = () => {
      if (!visivel) { tocando = false; return; }
      tocando = true; fila.forEach(clearTimeout); fila = []; box.innerHTML = '<span class="wa-d">Hoje</span>';
      const c = CHAT2[lista[i]]; nome.textContent = c[0]; st.textContent = 'online';
      let t = 500;
      c[1].forEach(([lado, txt], n) => {
        if (lado === 'in') { fila.push(setTimeout(() => { st.textContent = 'digitando...'; }, t)); t += 900; }
        fila.push(setTimeout(() => { bolha(lado, txt, n); st.textContent = 'online'; }, t));
        t += lado === 'in' ? 1400 : 1100;
      });
      fila.push(setTimeout(() => { i = (i + 1) % lista.length; tocar(); }, t + 2200));
    };
    if (reduce) { CHAT2[lista[0]][1].forEach(([l, x], n) => bolha(l, x, n)); $$('.wb', box).forEach(b => b.classList.add('on')); return; }
    if (!('IntersectionObserver' in window)) { visivel = true; tocar(); return; }
    new IntersectionObserver(es => { visivel = es[0].isIntersecting; if (visivel && !tocando) tocar(); }, { threshold: .3 }).observe(f);
  });
})();

/* ---------- como trabalhamos: as etapas acendem em sequência uma vez ao entrar na tela; o clique escolhe a etapa ---------- */
(function fluxo(){
  const ps = $$('.passo'), barra = $('#fluxoBarra'); if (!ps.length) return;
  let mexeu = false, fila = [];
  const marcar = i => { ps.forEach((p, k) => p.classList.toggle('on', k === i)); barra.style.transform = 'scaleX(' + ((i + 1) / ps.length) + ')'; };
  ps.forEach((p, i) => p.addEventListener('click', () => { mexeu = true; fila.forEach(clearTimeout); marcar(i); }));
  if (reduce || !('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver(es => { if (!es[0].isIntersecting) return; io.disconnect(); [1, 2, 3].forEach((k, j) => fila.push(setTimeout(() => { if (!mexeu) marcar(k); }, 1400 * (j + 1)))); }, { threshold: .45 });
  io.observe($('#fluxo4'));
})();

/* ---------- abertura: os números contam ao entrar na tela ---------- */""")

# ================== v15: áreas em cards grandes, agentes em acordeão e ícones no padrão da Terceirização ==================
css += r"""
/* ---------- v15 · ícone no padrão da Terceirização: disco escuro com aro, ícone ciano; acende e redesenha o traço no hover ---------- */
.ict{width:56px;height:56px;border-radius:50%;flex:none;display:grid;place-items:center;background:radial-gradient(circle at 30% 25%,var(--color-ink-800),var(--color-ink-950) 70%);box-shadow:inset 0 0 0 1px rgba(255,255,255,.14);color:var(--brand);transition:background-color var(--dur-fast) var(--ease-out),color var(--dur-fast) var(--ease-out),box-shadow var(--dur-base) var(--ease-out)}
.ict .ico{width:22px;height:22px}
.ict .ico *{stroke-dasharray:1;stroke-dashoffset:0}
.ict.p{width:44px;height:44px}
.ict.p .ico{width:18px;height:18px}
.acende:hover .ict,.acende.on .ict,.acende[aria-expanded="true"] .ict,.acende:focus-visible .ict{background:var(--brand);color:var(--on-brand);box-shadow:0 0 0 6px rgba(0,172,229,.12),0 0 28px -6px rgba(0,172,229,.7)}
.acende:hover .ict .ico *{animation:traca var(--dur-slow) var(--ease-out)}
@keyframes traca{from{stroke-dashoffset:1}}

/* ---------- v15 · áreas: título pequeno de apoio e três cards grandes ---------- */
.areas-top{display:flex;flex-direction:column;gap:12px;margin-bottom:32px}
.areas-top p{color:var(--fg-muted);font-size:var(--text-lead);line-height:var(--text-lead--line-height)}
.areas3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.area3{display:flex;flex-direction:column;gap:28px;min-height:300px;padding:32px}
.area3 .topo{display:flex;justify-content:space-between;align-items:center}
.area3 .n{font-family:var(--font-mono);font-size:var(--text-label);color:var(--fg-subtle)}
.area3 .nome{font-size:var(--text-h2);font-weight:500;letter-spacing:var(--text-h2--letter-spacing);line-height:var(--text-h2--line-height);margin-top:auto}
.area3 .base{display:flex;justify-content:space-between;align-items:center;padding-top:20px;border-top:1px solid var(--border)}
.area3 .base .tag{color:var(--fg-muted)}
.area3 .ir{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;box-shadow:inset 0 0 0 1px var(--border-strong);color:var(--fg);transition:background-color var(--dur-fast),color var(--dur-fast),box-shadow var(--dur-fast)}
.area3 .ir .ico{width:16px;height:16px}
.area3:hover .ir{background:var(--brand);color:var(--on-brand);box-shadow:none}

/* ---------- v15 · agentes de cada área em acordeão ---------- */
.cat-tx .tagq{color:var(--fg-subtle)}
.acc{list-style:none;margin:12px 0 0;padding:0;width:100%;border-top:1px solid var(--border)}
.acc > li{border-bottom:1px solid var(--border)}
.acc-b{width:100%;display:flex;align-items:center;gap:16px;padding:18px 0;background:none;border:0;text-align:left;color:var(--fg);cursor:pointer}
.acc-b b{flex:1;font-size:var(--text-h4);font-weight:500;line-height:var(--text-h4--line-height);transition:color var(--dur-fast)}
.acc-b .mais{width:32px;height:32px;border-radius:50%;flex:none;display:grid;place-items:center;box-shadow:inset 0 0 0 1px var(--border-strong);color:var(--fg-muted);transition:transform var(--dur-base) var(--ease-out),color var(--dur-fast),box-shadow var(--dur-fast)}
.acc-b .mais .ico{width:14px;height:14px}
.acc-b:hover b,.acc-b[aria-expanded="true"] b{color:var(--brand-text)}
.acc-b[aria-expanded="true"] .mais{transform:rotate(45deg);color:var(--brand);box-shadow:inset 0 0 0 1px var(--brand)}
.acc-b:focus-visible{outline:0}
.acc-p{display:grid;grid-template-rows:0fr;transition:grid-template-rows var(--dur-base) var(--ease-out)}
.acc-p.on{grid-template-rows:1fr}
.acc-p > div{overflow:hidden}
.acc-p .in{padding:0 0 22px 60px;display:flex;flex-direction:column;align-items:flex-start;gap:14px}
.acc-p p{color:var(--fg-muted)}
@media (max-width:960px){.areas3{grid-template-columns:1fr}.area3{min-height:0}.acc-p .in{padding-left:0}}
"""

ICO_AREA2 = {'Vendas e marketing': I['chat'], 'Operações e processos': I['layers'], 'Inteligência e decisão': I['chart']}
PLUS = svg('<path d="M12 5v14"/><path d="M5 12h14"/>')

def icone(d, pequeno=False):
    return '<span class="ict%s">%s</span>' % (' p' if pequeno else '', svg(d))

intro = abre + r"""<!-- S04 · Serviços: as três áreas em que construímos agentes -->
<section class="sec intro-cat" id="agentes" aria-labelledby="agT">
  <div class="wrap">
    <div class="areas-top rv">
      <span class="micro-l" id="agT">Áreas de atuação</span>
      <p>Construímos agentes de IA para três áreas da operação.</p>
    </div>
    <div class="areas3">
""" + ''.join('      <a class="area3 cd lum acende rv" href="#%s"><span class="topo">%s<span class="n">%02d</span></span><span class="nome">%s</span><span class="base"><span class="tag">%d agentes</span><span class="ir">%s</span></span></a>\n'
              % (IDS[a], icone(ICO_AREA2[a]), k + 1, a, len(ags), SETA) for k, (a, ags) in enumerate(AG)) + r"""    </div>
  </div>
</section>

"""

secs = ''
for k, (area, ags) in enumerate(AG):
    itens = ''
    for j, (n, d) in enumerate(ags):
        pid = 'ac%d_%d' % (k, j)
        aberto = j == 0
        itens += ('<li><button class="acc-b acende" type="button" aria-expanded="%s" aria-controls="%s">%s<b>%s</b><span class="mais">%s</span></button>'
                  '<div class="acc-p%s" id="%s" role="region"><div><div class="in"><p>%s</p><a class="link" href="#contato">Quero este agente %s</a></div></div></div></li>'
                  % ('true' if aberto else 'false', pid, icone(I2[n], True), n, PLUS, ' on' if aberto else '', pid, d, SETA))
    secs += ('<!-- S04 · Serviços: agentes de %s -->\n<section class="sec" id="%s" aria-labelledby="ct%d">\n  <div class="wrap">\n    <div class="g12 cat-g%s">\n'
             % (area.lower(), IDS[area], k, ' inv' if k == 1 else '')
             + '      <div class="cat-tx rv"><span class="micro-l">%02d · Área</span><h2 class="h2" id="ct%d">%s</h2><p class="sub">%s</p><span class="tag tagq">%d agentes</span>' % (k + 1, k, area, SUB[area], len(ags))
             + '<ul class="acc">' + itens + '</ul></div>\n'
             + '      <div class="cat-vis rv">' + fone(CONVS[area]) + '</div>\n'
             + '    </div>\n  </div>\n</section>\n\n')
agentes = intro + secs

# Como trabalhamos: ícones no mesmo padrão
for ic, t, d, e in FL:
    pass
passos = ''.join('<button class="passo acende%s" type="button" data-i="%d"><span class="n">%02d</span>%s<span class="t">%s</span><span class="pp">%s</span><span class="entrega"><span class="tag">O que você recebe</span><b>%s</b></span></button>'
                 % (' on' if i == 0 else '', i, i + 1, icone(I[ic]), t, d, e) for i, (ic, t, d, e) in enumerate(FL))
como = como[:como.index('<div class="fluxo4 rv" id="fluxo4">')] + '<div class="fluxo4 rv" id="fluxo4"><span class="barra" aria-hidden="true"><i id="fluxoBarra"></i></span>' + passos + como[como.index('</div>\n  </div>\n</section>', como.index('<div class="fluxo4 rv" id="fluxo4">')):]
css += ".passo .ict{margin:4px 0}\n.passo.on .ict{background:var(--brand);color:var(--on-brand);box-shadow:0 0 0 6px rgba(0,172,229,.12),0 0 28px -6px rgba(0,172,229,.7)}\n"

js = js.replace("/* ---------- abertura: os números contam ao entrar na tela ---------- */", r"""/* ---------- agentes: acordeão por área, um aberto por vez; o traço dos ícones redesenha no hover ---------- */
$$('.ict .ico *').forEach(p => p.setAttribute('pathLength', '1'));
$$('.acc').forEach(acc => {
  const bs = $$('.acc-b', acc);
  bs.forEach(b => b.addEventListener('click', () => {
    const abrir = b.getAttribute('aria-expanded') !== 'true';
    bs.forEach(o => { const on = o === b && abrir; o.setAttribute('aria-expanded', on ? 'true' : 'false'); $('#' + o.getAttribute('aria-controls')).classList.toggle('on', on); });
  }));
});

/* ---------- abertura: os números contam ao entrar na tela ---------- */""")

# ================== v16: as áreas viram seletores e a seção seguinte mostra só o acordeão da área escolhida ==================
css += r"""
/* ---------- v16 · áreas como seletores: a escolhida fica grifada, as outras esmaecidas ---------- */
.area3{font:inherit;width:100%;border:0;text-align:left;color:var(--fg);cursor:pointer;opacity:.42;transition:opacity var(--dur-base) var(--ease-out),box-shadow var(--dur-base) var(--ease-out)}
.area3:hover{opacity:.75}
.area3[aria-selected="true"]{opacity:1;box-shadow:inset 0 0 0 1px rgba(0,172,229,.65),0 0 48px -16px rgba(0,172,229,.55)}
.area3[aria-selected="true"] .ict{background:var(--brand);color:var(--on-brand);box-shadow:0 0 0 6px rgba(0,172,229,.12),0 0 28px -6px rgba(0,172,229,.7)}
.area3[aria-selected="true"] .ir{background:var(--brand);color:var(--on-brand);box-shadow:none}
.area3:focus-visible{outline:0;opacity:1;box-shadow:0 0 0 3px rgba(0,172,229,.45)}

/* ---------- v16 · acordeão limpo, de ponta a ponta do grid ---------- */
.lista-ag{padding-top:48px}
.lista-ag .acc{margin:0}
.lista-ag .acc[hidden]{display:none}
.lista-ag .acc.in{animation:cfEntra var(--dur-base) var(--ease-out)}
.lista-ag::before{display:none}
.lista-ag .acc{border-top:0;display:flex;flex-direction:column;gap:10px}
.lista-ag .acc > li{position:relative;border-bottom:0;border-radius:var(--radius-lg);background:rgba(255,255,255,.045);box-shadow:inset 0 0 0 1px rgba(255,255,255,.06);transition:background-color var(--dur-fast) var(--ease-out),box-shadow var(--dur-base) var(--ease-out)}
.lista-ag .acc > li:hover{background:rgba(255,255,255,.075)}
.lista-ag .acc > li:has(.acc-b[aria-expanded="true"]){box-shadow:0 0 0 1px rgba(0,172,229,.08),0 0 36px -12px rgba(0,172,229,.55)}
.lista-ag .acc > li:has(.acc-b[aria-expanded="true"])::before{background:linear-gradient(135deg,rgba(191,239,255,.75),rgba(0,172,229,.55) 35%,rgba(0,90,120,.25) 65%,rgba(127,216,245,.6))}
.lista-ag .acc-b:hover b,.lista-ag .acc-b[aria-expanded="true"] b{color:var(--fg)}
.lista-ag .acc-b[aria-expanded="true"] .mais{color:var(--fg);box-shadow:inset 0 0 0 1px var(--border-strong)}
.lista-ag .acc-b{padding:22px 28px;gap:24px}
.lista-ag .acc-b b{font-size:var(--text-h4)}
.lista-ag .acc-p .in{padding:0 28px 24px;flex-direction:row;justify-content:space-between;align-items:flex-end;gap:48px}
.lista-ag .acc-p p{max-width:720px;font-size:var(--text-body)}
.lista-ag .acc-p .link{white-space:nowrap}
@media (max-width:960px){.lista-ag .acc-p .in{flex-direction:column;align-items:flex-start;gap:14px}}
"""

intro = abre + r"""<!-- S04 · Serviços: as três áreas; a escolhida define os agentes listados logo abaixo -->
<section class="sec intro-cat" id="agentes" aria-labelledby="agT">
  <div class="wrap">
    <div class="areas-top rv">
      <span class="micro-l" id="agT">Áreas de atuação</span>
      <p>Construímos agentes de IA para três áreas da operação. Escolha uma para ver os agentes.</p>
    </div>
    <div class="areas3 rv" role="tablist" aria-label="Áreas de atuação">
""" + ''.join('      <button class="area3 cd lum acende" type="button" role="tab" id="ar%d" aria-controls="ls%d" aria-selected="%s" tabindex="%s"><span class="topo">%s<span class="n">%02d</span></span><span class="nome">%s</span><span class="base"><span class="tag">%d agentes</span><span class="ir">%s</span></span></button>\n'
              % (k, k, 'true' if k == 0 else 'false', '0' if k == 0 else '-1', icone(ICO_AREA2[a]), k + 1, a, len(ags), svg('<path d="M12 5v14"/><path d="m19 12-7 7-7-7"/>')) for k, (a, ags) in enumerate(AG)) + r"""    </div>
  </div>
</section>

"""

listas = ''
for k, (area, ags) in enumerate(AG):
    itens = ''
    for j, (n, d) in enumerate(ags):
        pid = 'ac%d_%d' % (k, j)
        aberto = j == 0
        itens += ('<li class="lum"><button class="acc-b" type="button" aria-expanded="%s" aria-controls="%s"><b>%s</b><span class="mais">%s</span></button>'
                  '<div class="acc-p%s" id="%s" role="region"><div><div class="in"><p>%s</p><a class="link" href="#contato">Quero este agente %s</a></div></div></div></li>'
                  % ('true' if aberto else 'false', pid, n, PLUS, ' on' if aberto else '', pid, d, SETA))
    listas += '    <ul class="acc" role="tabpanel" id="ls%d" aria-labelledby="ar%d"%s>%s</ul>\n' % (k, k, '' if k == 0 else ' hidden', itens)
agentes = intro + r"""<!-- S04 · Serviços: os agentes da área escolhida, em acordeão -->
<section class="sec lista-ag" id="lista-agentes" aria-label="Agentes da área escolhida">
  <div class="wrap">
""" + listas + r"""  </div>
</section>

"""

js = js.replace("/* ---------- abertura: os números contam ao entrar na tela ---------- */", r"""/* ---------- áreas: o card escolhido define a lista de agentes da seção seguinte ---------- */
(function areas(){
  const bs = $$('.area3[role="tab"]'); if (!bs.length) return;
  const ativar = (b, foco) => {
    bs.forEach(o => { const on = o === b; o.setAttribute('aria-selected', on ? 'true' : 'false'); o.tabIndex = on ? 0 : -1; const p = $('#' + o.getAttribute('aria-controls')); p.hidden = !on; if (on) { p.classList.remove('in'); void p.offsetWidth; p.classList.add('in'); } });
    if (foco) b.focus();
  };
  bs.forEach((b, i) => {
    b.addEventListener('click', () => { ativar(b); if (innerWidth < 961) $('#lista-agentes').scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' }); });
    b.addEventListener('keydown', e => { const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0; if (d) { e.preventDefault(); ativar(bs[(i + d + bs.length) % bs.length], true); } });
  });
})();

/* ---------- abertura: os números contam ao entrar na tela ---------- */""")

# ================== v17: o agente aberto ganha a luz neon girando sozinha pela borda (exceção à 9.5, pedido do usuário) ==================
css += r"""
/* ---------- v17 · agente aberto: luz neon girando pela borda ---------- */
.lista-ag .acc > li{background:var(--color-ink-900);overflow:hidden;isolation:isolate}
.lista-ag .acc > li:hover{background:var(--color-ink-850)}
.lista-ag .acc-b,.lista-ag .acc-p{position:relative;z-index:1}
.giro{position:absolute;inset:0;border-radius:inherit;overflow:hidden;z-index:0;opacity:0;pointer-events:none;transition:opacity var(--dur-base) var(--ease-out)}
.giro::before{content:"";position:absolute;left:50%;top:50%;width:160%;aspect-ratio:1;transform:translate(-50%,-50%);background:conic-gradient(from 0deg,rgba(0,172,229,0) 0deg,rgba(0,172,229,0) 200deg,var(--color-rumo-600) 260deg,var(--color-light-near) 320deg,var(--color-light-core) 345deg,rgba(0,172,229,0) 360deg);animation:volta calc(var(--dur-cinematic) * 3) linear infinite}
.giro::after{content:"";position:absolute;inset:1px;border-radius:inherit;background:var(--color-ink-900)}
.lista-ag .acc > li:has(.acc-b[aria-expanded="true"]) .giro{opacity:1}
.lista-ag .acc > li:has(.acc-b[aria-expanded="true"])::before,.lista-ag .acc > li:has(.acc-b[aria-expanded="true"])::after{opacity:0}
.lista-ag .acc > li:has(.acc-b[aria-expanded="true"]){background:var(--color-ink-900);box-shadow:0 0 40px -14px rgba(0,172,229,.6)}
"""
agentes = agentes.replace('<li class="lum"><button class="acc-b"', '<li class="lum"><span class="giro" aria-hidden="true"></span><button class="acc-b"')

# ================== v18: sem brilho externo; borda animada no card de área selecionado e no agente aberto, uma cor por área ==================
css += r"""
/* ---------- v18 · borda animada por área (ciano, verde, violeta; tokens da 2.9) e sem brilho externo ---------- */
.area3{position:relative;overflow:hidden;isolation:isolate}
.area3 > .topo,.area3 > .nome,.area3 > .base{position:relative;z-index:1}
.area3 .giro::after{background:linear-gradient(180deg,var(--color-ink-925) 0%,var(--color-ink-950) 100%)}
.area3[aria-selected="true"]{box-shadow:none}
.area3[aria-selected="true"]::before,.area3[aria-selected="true"]::after{opacity:0}
.area3[aria-selected="true"] .giro{opacity:1}
.lista-ag .acc > li:has(.acc-b[aria-expanded="true"]){box-shadow:none}
.c-ciano .giro::before{background:conic-gradient(from 0deg,rgba(0,172,229,0) 0deg,rgba(0,172,229,0) 200deg,var(--color-rumo-600) 260deg,var(--color-light-near) 320deg,var(--color-light-core) 345deg,rgba(0,172,229,0) 360deg)}
.c-verde .giro::before{background:conic-gradient(from 0deg,rgba(61,220,151,0) 0deg,rgba(61,220,151,0) 200deg,rgba(61,220,151,.45) 260deg,var(--color-neon-green) 320deg,var(--color-light-core) 345deg,rgba(61,220,151,0) 360deg)}
.c-violeta .giro::before{background:conic-gradient(from 0deg,rgba(155,140,255,0) 0deg,rgba(155,140,255,0) 200deg,rgba(155,140,255,.45) 260deg,var(--color-neon-violet) 320deg,var(--color-light-core) 345deg,rgba(155,140,255,0) 360deg)}
"""
COR = ['c-ciano', 'c-verde', 'c-violeta']
GIRO = '<span class="giro" aria-hidden="true"></span>'
for k in range(3):
    a = 'role="tab" id="ar%d"' % k
    assert agentes.count(a) == 1
    agentes = agentes.replace('<button class="area3 cd lum acende" type="button" ' + a, '<button class="area3 cd lum acende %s" type="button" ' % COR[k] + a)
    b = '<ul class="acc" role="tabpanel" id="ls%d"' % k
    assert agentes.count(b) == 1
    agentes = agentes.replace(b, '<ul class="acc %s" role="tabpanel" id="ls%d"' % (COR[k], k))
agentes = agentes.replace('<span class="topo"><span class="ict">', GIRO + '<span class="topo"><span class="ict">')

# ================== v19: ícone e seta dos cards de área na cor da área ==================
css += r"""
/* ---------- v19 · ícone e seta na cor da área (trinca da 2.9) ---------- */
.area3.c-verde .ict{color:var(--color-neon-green)}
.area3.c-violeta .ict{color:var(--color-neon-violet)}
.area3.c-verde[aria-selected="true"] .ict,.area3.c-verde:hover .ict,.area3.c-verde:focus-visible .ict{background:var(--color-neon-green);color:var(--on-brand);box-shadow:0 0 0 6px rgba(61,220,151,.12),0 0 28px -6px rgba(61,220,151,.7)}
.area3.c-violeta[aria-selected="true"] .ict,.area3.c-violeta:hover .ict,.area3.c-violeta:focus-visible .ict{background:var(--color-neon-violet);color:var(--on-brand);box-shadow:0 0 0 6px rgba(155,140,255,.12),0 0 28px -6px rgba(155,140,255,.7)}
.area3.c-verde[aria-selected="true"] .ir,.area3.c-verde:hover .ir{background:var(--color-neon-green);color:var(--on-brand);box-shadow:none}
.area3.c-violeta[aria-selected="true"] .ir,.area3.c-violeta:hover .ir{background:var(--color-neon-violet);color:var(--on-brand);box-shadow:none}
"""

# ================== v20: agentes com o mesmo fundo dos cards de área; prévia da cor da área em sombra no hover ==================
css += r"""
/* ---------- v20 · fundo dos agentes igual ao das áreas ---------- */
.lista-ag .acc > li,.lista-ag .acc > li:hover,.lista-ag .acc > li:has(.acc-b[aria-expanded="true"]){background:linear-gradient(180deg,var(--color-ink-925) 0%,var(--color-ink-950) 100%)}
.lista-ag .giro::after{background:linear-gradient(180deg,var(--color-ink-925) 0%,var(--color-ink-950) 100%)}

/* ---------- v20 · hover nas áreas: sombra na cor da borda animada daquela área ---------- */
.area3.c-ciano:not([aria-selected="true"]):hover{box-shadow:0 0 0 1px rgba(0,172,229,.25),0 18px 56px -18px rgba(0,172,229,.7)}
.area3.c-verde:not([aria-selected="true"]):hover{box-shadow:0 0 0 1px rgba(61,220,151,.25),0 18px 56px -18px rgba(61,220,151,.7)}
.area3.c-violeta:not([aria-selected="true"]):hover{box-shadow:0 0 0 1px rgba(155,140,255,.25),0 18px 56px -18px rgba(155,140,255,.7)}
.area3.c-verde::after{background:radial-gradient(260px circle at var(--mx,50%) var(--my,0%),rgba(242,251,255,.95),rgba(61,220,151,.9) 24%,rgba(61,220,151,0) 70%)}
.area3.c-violeta::after{background:radial-gradient(260px circle at var(--mx,50%) var(--my,0%),rgba(242,251,255,.95),rgba(155,140,255,.9) 24%,rgba(155,140,255,0) 70%)}
.area3.c-verde.hov::before{background:rgba(61,220,151,.35)}
.area3.c-violeta.hov::before{background:rgba(155,140,255,.35)}
"""

# ================== v21: micropulos contínuos nos cards de área não selecionados (exceção à 9.5, pedido do usuário) ==================
css += r"""
/* ---------- v21 · micropulos nos cards não selecionados; param no hover, no selecionado e fora da tela ---------- */
@keyframes pulinho{0%,62%,100%{transform:translateY(0)}72%{transform:translateY(-7px)}82%{transform:translateY(0)}88%{transform:translateY(-2px)}94%{transform:translateY(0)}}
.areas3.pula .area3:not([aria-selected="true"]){animation:pulinho calc(var(--dur-cinematic) * 2) var(--ease-out) infinite}
.areas3.pula #ar1:not([aria-selected="true"]){animation-delay:var(--dur-base)}
.areas3.pula #ar2:not([aria-selected="true"]){animation-delay:var(--dur-slow)}
.areas3.pula .area3:not([aria-selected="true"]):hover,.areas3.pula .area3:not([aria-selected="true"]):focus-visible{animation:none}
"""
js = js.replace("/* ---------- abertura: os números contam ao entrar na tela ---------- */", r"""/* ---------- áreas: os micropulos só rodam com a seção na tela ---------- */
(function pulos(){
  const box = $('.areas3'); if (!box || reduce || !('IntersectionObserver' in window)) return;
  new IntersectionObserver(es => box.classList.toggle('pula', es[0].isIntersecting), { threshold: .3 }).observe(box);
})();

/* ---------- abertura: os números contam ao entrar na tela ---------- */""")

# ================== v22: consultoria com a ampulheta de pixels da Home por trás e o card no padrão do "Vamos conversar" ==================
css += r"""
/* ---------- v22 · consultoria: pixels da Home (ampulheta) atrás do card; card no padrão do CTA final da Home ---------- */
.cs{position:relative;overflow:hidden;isolation:isolate;padding-block:var(--section-y)}
.cs-areia{position:absolute;inset:0;width:100%;height:100%;display:block;z-index:-1;pointer-events:none}
.cs-card{position:relative;min-height:480px;border-radius:var(--radius-panel);overflow:hidden;isolation:isolate;background:var(--color-ink-950);box-shadow:inset 0 0 0 1px rgba(255,255,255,.08),0 40px 90px -40px rgba(5,5,5,.95);display:flex;align-items:center;justify-content:center;text-align:center;padding:72px 48px}
.cs-dots{position:absolute;inset:0;width:100%;height:100%;z-index:-2}
.cs-lt{position:absolute;inset:0 0 auto 0;height:360px;z-index:-1;pointer-events:none;mix-blend-mode:screen;background:linear-gradient(90deg,transparent 18%,rgba(127,216,245,.35) 35%,rgba(242,251,255,.8) 50%,rgba(127,216,245,.35) 65%,transparent 82%) top/100% 1px no-repeat,radial-gradient(38% 80% at 50% 0%,rgba(191,239,255,.22),rgba(127,216,245,.16) 14%,rgba(0,172,229,.1) 38%,rgba(0,90,120,.04) 68%,transparent 100%)}
.cs-veil{position:absolute;inset:0;z-index:-1;pointer-events:none;background:radial-gradient(46% 44% at 50% 52%,rgba(5,5,5,.92),rgba(5,5,5,.6) 55%,rgba(5,5,5,0) 100%)}
.cs-in{display:flex;flex-direction:column;align-items:center;gap:24px;max-width:720px}
.cs-in .lead{max-width:560px}
.cs-acts{display:flex;gap:24px;align-items:center;flex-wrap:wrap;justify-content:center;margin-top:8px}
@media (max-width:640px){.cs-card{padding:48px 24px;min-height:0}}
"""
MAILR2 = 'mailto:comercial@rumosolucoes.com?subject=' + 'Agendar%20reuni%C3%A3o%20sobre%20IA'
MAILE = 'mailto:comercial@rumosolucoes.com?subject=' + 'Falar%20com%20um%20especialista%20em%20IA'
novo_cs = (r"""<!-- S14 · CTA final: consultoria para descobrir o que automatizar, com os pixels da Home por trás -->
<section class="cs" id="contato" aria-labelledby="ctT">
  <canvas class="cs-areia" id="csAreia" aria-hidden="true"></canvas>
  <div class="wrap">
    <div class="cs-card rv" id="csCard">
      <canvas class="cs-dots" id="csDots" aria-hidden="true"></canvas>
      <span class="cs-lt" aria-hidden="true"></span><span class="cs-veil" aria-hidden="true"></span>
      <div class="cs-in">
        <span class="micro-l">Consultoria</span>
        <h2 class="h2" id="ctT">Ainda não sabe <span class="tone">o que automatizar?</span></h2>
        <p class="lead">Agende uma reunião. Um especialista da Rumo mapeia com você o que dá para automatizar na sua empresa, sem custo.</p>
        <div class="cs-acts">""" + '<a class="btn btn-primary lg" href="' + MAILR2 + '">Agendar uma reunião ' + SETA + '</a><a class="link" href="' + MAILE + '">Falar com um especialista ' + SETA + '</a>' + r"""</div>
      </div>
    </div>
  </div>
</section>

""")
_i = como.index('<!-- S14 · CTA final')
como = como[:_i] + novo_cs

js = js.replace("/* ---------- abertura: os números contam ao entrar na tela ---------- */", r"""/* ---------- consultoria: ampulheta de pixels da Home (S19) atrás do card ---------- */
(function areia(){
  const cv = $('#csAreia'); if (!cv) return;
  const box = cv.parentElement, ctx = cv.getContext('2d');
  const tok = getComputedStyle(document.documentElement);
  const rgb = n => { const h = tok.getPropertyValue(n).trim().replace('#', ''); return [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16)).join(','); };
  const CI = rgb('--color-rumo-500'), CL = rgb('--color-light-near'), CE = rgb('--color-rumo-800'), CW = rgb('--color-light-core');
  const G = 6;
  let W = 0, H = 0, cx = 0, cy = 0, meia = 0, cintura = 0, campo = null, parts = [], rodando = false, last = 0;
  const altura = x => cintura + (meia - cintura) * Math.pow(Math.min(1, Math.abs(x - cx) / cx), 1.35);
  const snap = v => Math.round(v / G) * G;
  function montar(){
    const r = box.getBoundingClientRect(); W = r.width; H = r.height;
    const dpr = Math.min(1.5, devicePixelRatio || 1); cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    cx = W / 2; cy = H / 2; meia = Math.min(H * .34, 300); cintura = 60;
    campo = document.createElement('canvas'); campo.width = cv.width; campo.height = cv.height;
    const c = campo.getContext('2d'); c.setTransform(dpr, 0, 0, dpr, 0, 0);
    for (let x = 0; x <= W; x += G) { const h = altura(x); for (let y = snap(cy - h); y <= cy + h; y += G) { const borda = Math.abs(y - cy) / h, perto = 1 - Math.min(1, Math.abs(x - cx) / cx), a = (.05 + .22 * perto) * (1 - borda * .6) * (.4 + Math.random() * .6); c.fillStyle = 'rgba(' + (Math.random() < .5 ? CE : CI) + ',' + a.toFixed(3) + ')'; c.fillRect(x - 1.5, y - 1.5, 3, 3); } }
    parts = Array.from({ length: Math.round(W / 4) }, () => nova(Math.random() * W));
  }
  const nova = x => ({ x, v: (Math.random() * 2 - 1), s: 50 + Math.random() * 110, b: Math.random() < .08 });
  function quadro(dt){
    ctx.clearRect(0, 0, W, H); ctx.drawImage(campo, 0, 0, W, H);
    for (const p of parts) {
      p.x += p.s * dt * (1 + 1.4 * (1 - Math.min(1, Math.abs(p.x - cx) / cx)));
      if (p.x > W + 12) Object.assign(p, nova(-12));
      for (let k = 3; k >= 0; k--) { const x = p.x - k * G, h = altura(x), y = snap(cy + p.v * h), perto = 1 - Math.min(1, Math.abs(x - cx) / cx); const a = (1 - k / 4) * (.35 + .65 * perto); ctx.fillStyle = 'rgba(' + (k === 0 ? (p.b ? CW : CL) : CI) + ',' + a.toFixed(3) + ')'; ctx.fillRect(snap(x) - 1.5, y - 1.5, 3, 3); }
    }
    for (let k = 0; k < 24; k++) { const x = snap(cx + (Math.random() * 2 - 1) * cx * .5), h = altura(x), y = snap(cy + (Math.random() * 2 - 1) * h); ctx.fillStyle = 'rgba(' + CL + ',' + (.3 + Math.random() * .5).toFixed(2) + ')'; ctx.fillRect(x - 1.5, y - 1.5, 3, 3); }
  }
  function laco(ts){ if (!rodando) return; const dt = Math.min(.05, (ts - (last || ts)) / 1000); last = ts; quadro(dt); requestAnimationFrame(laco); }
  montar(); quadro(0);
  addEventListener('resize', () => { montar(); quadro(0); });
  if (reduce || !('IntersectionObserver' in window)) return;
  new IntersectionObserver(es => { const v = es[0].isIntersecting; if (v && !rodando) { rodando = true; last = 0; requestAnimationFrame(laco); } rodando = v; }).observe(box);
})();

/* ---------- consultoria: grade de pontos com foco de luz que segue o cursor, como o CTA final da Home ---------- */
(function pontos(){
  const cv = $('#csDots'), card = $('#csCard'); if (!cv) return;
  const c = cv.getContext('2d');
  const tok = getComputedStyle(document.documentElement);
  const rgb = n => { const h = tok.getPropertyValue(n).trim().replace('#', ''); return [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16)).join(','); };
  const CW = rgb('--color-light-core'), CL = rgb('--color-light-near');
  let W, H, sx, sy, tx, ty, rodando = false;
  function medir(){ const r = cv.getBoundingClientRect(); W = r.width; H = r.height; const dpr = Math.min(1.5, devicePixelRatio || 1); cv.width = W * dpr; cv.height = H * dpr; c.setTransform(dpr, 0, 0, dpr, 0, 0); sx = tx = W / 2; sy = ty = H * .42; }
  function desenhar(t){
    c.clearRect(0, 0, W, H);
    if (!fine && !reduce) { tx = W / 2 + Math.sin(t * .0004) * W * .18; ty = H * .42 + Math.cos(t * .0003) * H * .12; }
    sx += (tx - sx) * .12; sy += (ty - sy) * .12;
    const R = 320;
    for (let x = 12; x < W; x += 24) for (let y = 12; y < H; y += 24) {
      const d = Math.hypot(x - sx, y - sy), k = Math.max(0, 1 - d / R), e = k * k * (3 - 2 * k);
      c.fillStyle = 'rgba(' + (e > .02 ? CL : CW) + ',' + (.1 + e * .55).toFixed(3) + ')';
      c.beginPath(); c.arc(x, y, .8 + e * 1.1, 0, 6.283); c.fill();
    }
  }
  function laco(t){ if (rodando) desenhar(t); requestAnimationFrame(laco); }
  medir(); addEventListener('resize', medir);
  card.addEventListener('pointermove', e => { const r = cv.getBoundingClientRect(); tx = e.clientX - r.left; ty = e.clientY - r.top; });
  card.addEventListener('pointerleave', () => { tx = W / 2; ty = H * .42; });
  if (reduce || !('IntersectionObserver' in window)) { desenhar(0); return; }
  new IntersectionObserver(es => { rodando = es[0].isIntersecting; }).observe(card);
  requestAnimationFrame(laco);
})();

/* ---------- abertura: os números contam ao entrar na tela ---------- */""")

# ================== v24: demonstração num card dark: WhatsApp Web e RD Station CRM em sequência, em tela cheia, entre os números e as áreas ==================
css += r"""
/* ---------- v24 · demonstração: card dark com as telas do WhatsApp Web e do CRM, uma por vez ---------- */
.demo-card{border-radius:var(--radius-panel);background:linear-gradient(180deg,var(--color-ink-925),var(--color-ink-950));padding:40px}
.demo-top{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;margin-bottom:28px}
.demo-top > div:first-child{display:flex;flex-direction:column;gap:12px}
.demo-top p{color:var(--fg-muted);font-size:var(--text-lead);line-height:var(--text-lead--line-height);max-width:640px}
.demo-tabs{display:flex;gap:4px;padding:4px;border-radius:var(--radius-pill);box-shadow:inset 0 0 0 1px var(--border-strong)}
.demo-tabs span{display:inline-flex;align-items:center;gap:8px;height:36px;padding:0 16px;border-radius:var(--radius-pill);font-size:var(--text-small);color:var(--fg-subtle);transition:background-color var(--dur-base) var(--ease-out),color var(--dur-base) var(--ease-out)}
.demo-tabs span::before{content:"";width:6px;height:6px;border-radius:50%;background:currentColor;opacity:.5;transition:background-color var(--dur-base),opacity var(--dur-base)}
.demo-tabs span.on{background:rgba(255,255,255,.08);color:var(--fg)}
.demo-tabs span.on::before{background:var(--brand);opacity:1}
.palco{position:relative;height:680px}
.tela{position:absolute;inset:0;opacity:0;transform:scale(.985);visibility:hidden;transition:opacity var(--dur-slow) var(--ease-out),transform var(--dur-slow) var(--ease-out),visibility var(--dur-instant) linear var(--dur-slow)}
.tela.on{opacity:1;transform:none;visibility:visible;transition:opacity var(--dur-slow) var(--ease-out),transform var(--dur-slow) var(--ease-out)}
.demo-card small.nota{display:block;margin-top:16px;font-size:var(--text-caption);color:var(--fg-subtle)}

/* WhatsApp Web (seção 2.10) */
.wweb{display:grid;grid-template-columns:minmax(300px,34%) minmax(0,1fr);border-radius:var(--radius-lg);overflow:hidden;background:var(--wa-entrada);color:var(--wa-texto);box-shadow:var(--shadow-float);font-size:var(--text-small);line-height:1.4}
.wweb .ico{width:20px;height:20px;color:var(--wa-meta)}
.ww-side{display:flex;flex-direction:column;min-height:0;box-shadow:inset -1px 0 0 rgba(17,27,33,.1)}
.ww-sh{display:flex;align-items:center;justify-content:space-between;height:60px;padding:0 16px}
.ww-sh b{font-size:var(--text-h4);font-weight:600;color:var(--wa-texto)}
.ww-sh .acoes{display:flex;gap:18px}
.ww-busca{margin:0 12px 8px;height:36px;border-radius:var(--radius-md);display:flex;align-items:center;gap:14px;padding:0 14px;background:linear-gradient(rgba(17,27,33,.05),rgba(17,27,33,.05)),var(--wa-entrada);color:var(--wa-meta)}
.ww-busca .ico{width:16px;height:16px}
.ww-chips{display:flex;gap:8px;padding:0 12px 10px}
.ww-chips span{padding:5px 12px;border-radius:var(--radius-pill);background:linear-gradient(rgba(17,27,33,.05),rgba(17,27,33,.05)),var(--wa-entrada);color:var(--wa-meta)}
.ww-chips span.on{background:rgba(0,128,105,.12);color:var(--wa-cabecalho)}
.ww-lista{list-style:none;margin:0;padding:0;overflow:hidden}
.ww-lista li{display:flex;align-items:center;gap:14px;padding:0 0 0 14px;height:72px;transition:background-color var(--dur-fast) var(--ease-out)}
.ww-lista li.on{background:rgba(17,27,33,.07)}
.ww-av{flex:none;width:48px;height:48px;border-radius:50%;display:grid;place-items:center;overflow:hidden;background:rgba(17,27,33,.12)}
.ww-av svg{width:40px;height:40px;margin-top:10px;fill:var(--wa-entrada);stroke:none}
.ww-li{flex:1;min-width:0;height:100%;display:flex;flex-direction:column;justify-content:center;gap:2px;padding-right:14px;box-shadow:inset 0 -1px 0 rgba(17,27,33,.08)}
.ww-li .l1,.ww-li .l2{display:flex;justify-content:space-between;align-items:center;gap:8px}
.ww-li .l1 b{font-weight:400;font-size:var(--text-body);color:var(--wa-texto);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ww-li .l1 time{font-size:var(--text-caption);color:var(--wa-meta);flex:none}
.ww-li .l2 span{color:var(--wa-meta);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ww-li .l2 i{flex:none;min-width:20px;height:20px;padding:0 6px;border-radius:var(--radius-pill);display:grid;place-items:center;font-style:normal;font-size:var(--text-mono-micro);font-weight:600;background:var(--wa-cabecalho);color:var(--wa-entrada);transform:scale(0);transition:transform var(--dur-fast) var(--ease-out)}
.ww-lista li.nova .l2 i{transform:scale(1)}
.ww-lista li.nova .l1 time{color:var(--wa-cabecalho)}
.ww-lista li.nova .l2 span{color:var(--wa-texto)}
.ww-main{display:flex;flex-direction:column;min-width:0;min-height:0}
.ww-ch{flex:none;display:flex;align-items:center;gap:14px;height:60px;padding:0 16px;background:linear-gradient(rgba(17,27,33,.04),rgba(17,27,33,.04)),var(--wa-entrada);box-shadow:inset 0 -1px 0 rgba(17,27,33,.08)}
.ww-ch .ww-av{width:40px;height:40px}
.ww-ch .ww-av svg{width:34px;height:34px;margin-top:8px}
.ww-ch .quem{flex:1;min-width:0;display:flex;flex-direction:column}
.ww-ch .quem b{font-weight:400;font-size:var(--text-body);color:var(--wa-texto)}
.ww-ch .quem small{font-size:var(--text-caption);color:var(--wa-meta);min-height:1.2em}
.ww-ch .quem small.dig{color:var(--wa-cabecalho)}
.ww-ch .acoes{display:flex;gap:22px}
.ww-conv{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:flex-end;gap:4px;padding:16px 8% 12px;overflow:hidden;background-color:var(--wa-fundo);background-image:radial-gradient(rgba(17,27,33,.07) 1px,transparent 1.4px);background-size:20px 20px}
.ww-dia{align-self:center;margin-bottom:8px;padding:5px 12px;border-radius:var(--radius-md);background:var(--wa-entrada);color:var(--wa-meta);font-size:var(--text-caption);box-shadow:0 1px 1px rgba(17,27,33,.12)}
.ww-b{position:relative;max-width:65%;padding:6px 9px 8px;border-radius:var(--radius-md);color:var(--wa-texto);box-shadow:0 1px 1px rgba(17,27,33,.12);animation:wwEntra var(--dur-fast) var(--ease-out)}
.ww-b.c{align-self:flex-start;background:var(--wa-entrada)}
.ww-b.a{align-self:flex-end;background:var(--wa-saida)}
.ww-b.c.pri{border-top-left-radius:0;margin-top:8px}
.ww-b.a.pri{border-top-right-radius:0;margin-top:8px}
.ww-b .hr{float:right;display:inline-flex;align-items:center;gap:3px;margin:6px 0 -4px 12px;font-size:var(--text-mono-micro);color:var(--wa-meta)}
.ww-b .hr svg{width:16px;height:11px;fill:none;stroke:var(--wa-meta);stroke-width:1.6;transition:stroke var(--dur-fast)}
.ww-b.lido .hr svg{stroke:var(--wa-check)}
.ww-doc{display:flex;align-items:center;gap:10px;min-width:240px;padding:10px;margin-bottom:2px;border-radius:var(--radius-sm);background:rgba(17,27,33,.05)}
.ww-doc em{flex:none;width:30px;height:36px;border-radius:var(--radius-xs);display:grid;place-items:center;font-style:normal;font-size:var(--text-mono-micro);font-weight:600;color:var(--wa-entrada);background:var(--color-error-700)}
.ww-doc b{display:block;font-weight:400}
.ww-doc small{color:var(--wa-meta);font-size:var(--text-caption)}
.ww-pe{flex:none;display:flex;align-items:center;gap:16px;min-height:62px;padding:10px 16px;background:linear-gradient(rgba(17,27,33,.04),rgba(17,27,33,.04)),var(--wa-entrada)}
.ww-pe .ico{width:24px;height:24px}
.ww-campo{flex:1;min-width:0;min-height:42px;max-height:66px;padding:10px 14px;border-radius:var(--radius-lg);background:var(--wa-entrada);color:var(--wa-meta);overflow:hidden;display:flex;flex-direction:column;justify-content:flex-end}
.ww-campo.esc{color:var(--wa-texto)}
.ww-campo.esc span::after,.rd-in.esc::after{content:"";display:inline-block;width:1px;height:1.1em;margin-left:1px;vertical-align:-2px;background:currentColor}
.ww-env{flex:none;width:42px;height:42px;border-radius:50%;display:grid;place-items:center;transition:background-color var(--dur-fast)}
.ww-env .mic{display:block}.ww-env .env{display:none}
.ww-env.on{background:var(--wa-cabecalho)}
.ww-env.on .mic{display:none}.ww-env.on .env{display:block;color:var(--wa-entrada)}
@keyframes wwEntra{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}

/* RD Station CRM (seção 2.11): funil de negociações */
.rdc{display:flex;flex-direction:column;border-radius:var(--radius-lg);overflow:hidden;background:var(--rd-fundo);color:var(--rd-texto);box-shadow:var(--shadow-float);font-size:var(--text-small);line-height:1.4}
.rdc .ico{width:18px;height:18px;color:var(--rd-meta)}
.rd-nav{flex:none;display:flex;align-items:center;gap:28px;height:56px;padding:0 20px;background:var(--rd-superficie);box-shadow:inset 0 -1px 0 var(--rd-controle)}
.rd-nav nav{display:flex;gap:24px;height:100%}
.rd-nav nav span{display:flex;align-items:center;height:100%;color:var(--rd-meta)}
.rd-nav nav span.on{color:var(--rd-texto);font-weight:600;box-shadow:inset 0 -2px 0 var(--rd-primaria)}
.rd-nav .dir{margin-left:auto;display:flex;align-items:center;gap:18px}
.rd-nav .eu{width:32px;height:32px;border-radius:50%;display:grid;place-items:center;background:var(--rd-nova);color:var(--rd-superficie);font-size:var(--text-mono-micro);font-weight:600}
.rd-bar{flex:none;display:flex;align-items:center;gap:10px;padding:16px 20px 8px}
.rd-vis{display:flex;border-radius:var(--radius-sm);box-shadow:inset 0 0 0 1px var(--rd-controle);overflow:hidden}
.rd-vis span{width:34px;height:32px;display:grid;place-items:center}
.rd-vis span.on{background:var(--rd-primaria)}
.rd-vis span.on .ico{color:var(--rd-superficie)}
.rd-sel{display:flex;align-items:center;gap:8px;height:32px;padding:0 12px;border-radius:var(--radius-sm);background:var(--rd-superficie);box-shadow:inset 0 0 0 1px var(--rd-controle);color:var(--rd-texto);white-space:nowrap}
.rd-sel .ico{width:14px;height:14px}
.rd-sel.flt{color:var(--rd-primaria);box-shadow:inset 0 0 0 1px var(--rd-primaria)}
.rd-sel.flt .ico{color:var(--rd-primaria)}
.rd-bar .dir{margin-left:auto;display:flex;align-items:center;gap:12px}
.rd-criar{display:flex;align-items:center;gap:6px;height:32px;padding:0 14px;border-radius:var(--radius-sm);background:var(--rd-primaria);color:var(--rd-superficie);font-weight:600;transition:transform var(--dur-instant) var(--ease-out)}
.rd-criar .ico{width:14px;height:14px;color:var(--rd-superficie)}
.rdc .pres{transform:scale(.94)}
.rd-qtd{flex:none;padding:4px 20px 12px;color:var(--rd-meta);font-size:var(--text-caption)}
.rd-cols{flex:1;min-height:0;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;padding:0 20px 20px}
.rd-col{display:flex;flex-direction:column;gap:8px;min-height:0;padding:10px;border-radius:var(--radius-md);background:var(--rd-coluna)}
.rd-ch{display:flex;justify-content:space-between;align-items:center;gap:6px;padding:2px 2px 4px}
.rd-ch b{font-size:var(--text-caption);font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rd-ch span{flex:none;padding:2px 6px;border-radius:var(--radius-xs);background:var(--rd-controle);font-size:var(--text-mono-micro);color:var(--rd-meta)}
.rd-cards{display:flex;flex-direction:column;gap:8px}
.rd-card{position:relative;display:flex;flex-direction:column;gap:6px;padding:10px;border-radius:var(--radius-sm);background:var(--rd-superficie);box-shadow:0 1px 2px rgba(33,36,41,.12);transition:transform var(--dur-base) var(--ease-out),box-shadow var(--dur-base) var(--ease-out)}
.rd-card .tg{display:flex;align-items:center;gap:6px;font-size:var(--text-mono-micro);color:var(--rd-meta)}
.rd-card .tg::before{content:"";width:8px;height:8px;border-radius:var(--radius-xs);background:var(--rd-nova)}
.rd-card .tg.and::before{background:var(--rd-primaria)}
.rd-card b{font-size:var(--text-caption);font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rd-card small{font-size:var(--text-mono-micro);color:var(--rd-meta);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rd-card .vl{display:flex;align-items:center;gap:6px;font-size:var(--text-mono-micro);color:var(--rd-meta)}
.rd-card .vl .ico{width:12px;height:12px}
.rd-card .tf{display:flex;align-items:center;justify-content:center;gap:4px;height:24px;border-radius:var(--radius-xs);background:var(--rd-controle);font-size:var(--text-mono-micro);font-weight:600;color:var(--rd-texto);transition:transform var(--dur-instant) var(--ease-out)}
.rd-card .tf .ico{width:12px;height:12px;color:var(--rd-texto)}
.rd-card.novo{animation:rdNovo var(--dur-slow) var(--ease-out)}
.rd-card.pega{box-shadow:0 18px 32px -10px rgba(33,36,41,.35),0 0 0 2px var(--rd-primaria);z-index:3}
.rd-card.solto{transition:none}
.rd-ph{border-radius:var(--radius-sm);box-shadow:inset 0 0 0 1px var(--rd-primaria);background:rgba(22,199,209,.08)}
.rd-gav{position:absolute;top:0;right:0;bottom:0;width:380px;display:flex;flex-direction:column;background:var(--rd-superficie);box-shadow:-24px 0 48px -24px rgba(33,36,41,.35);transform:translateX(104%);transition:transform var(--dur-base) var(--ease-out);z-index:4}
.rd-gav.on{transform:none}
.rd-gh{display:flex;justify-content:space-between;align-items:center;height:56px;padding:0 20px;box-shadow:inset 0 -1px 0 var(--rd-controle)}
.rd-gh b{font-size:var(--text-body);font-weight:600}
.rd-gc{flex:1;display:flex;flex-direction:column;gap:14px;padding:20px}
.rd-gc label{display:flex;flex-direction:column;gap:6px;font-size:var(--text-caption);color:var(--rd-meta)}
.rd-in{min-height:36px;display:flex;align-items:center;padding:0 12px;border-radius:var(--radius-sm);box-shadow:inset 0 0 0 1px var(--rd-controle);color:var(--rd-texto);font-size:var(--text-small);transition:box-shadow var(--dur-fast)}
.rd-in.esc{box-shadow:inset 0 0 0 1px var(--rd-primaria)}
.rd-gp{display:flex;justify-content:flex-end;gap:10px;padding:16px 20px;box-shadow:inset 0 1px 0 var(--rd-controle)}
.rd-gp span{height:36px;display:flex;align-items:center;padding:0 16px;border-radius:var(--radius-sm);font-weight:600}
.rd-gp .cnc{color:var(--rd-meta)}
.rd-gp .slv{background:var(--rd-primaria);color:var(--rd-superficie);transition:transform var(--dur-instant) var(--ease-out)}
.rd-toast{position:absolute;left:50%;bottom:24px;display:flex;align-items:center;gap:10px;padding:12px 18px;border-radius:var(--radius-md);background:var(--rd-texto);color:var(--rd-superficie);box-shadow:0 12px 32px -12px rgba(33,36,41,.6);transform:translate(-50%,16px);opacity:0;transition:opacity var(--dur-base) var(--ease-out),transform var(--dur-base) var(--ease-out);z-index:5}
.rd-toast.on{opacity:1;transform:translate(-50%,0)}
.rd-toast .ico{width:18px;height:18px;color:var(--rd-primaria)}
.ia-cur{position:absolute;left:0;top:0;display:flex;align-items:flex-start;gap:4px;pointer-events:none;opacity:0;z-index:6;transition:transform var(--dur-base) var(--ease-out),opacity var(--dur-base)}
.ia-cur.on{opacity:1}
.ia-cur svg{width:20px;height:20px;fill:var(--brand);stroke:var(--color-ink-950);stroke-width:1.2;stroke-linejoin:round}
.ia-cur span{margin-top:14px;padding:4px 10px;border-radius:var(--radius-pill);background:var(--color-ink-950);color:var(--fg);font-size:var(--text-mono-micro);font-weight:600;white-space:nowrap;display:flex;align-items:center;gap:6px}
.ia-cur span::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--brand)}
@keyframes rdNovo{from{opacity:0;transform:translateY(-8px)}to{opacity:1;transform:none}}

@media (max-width:960px){
  .demo-card{padding:24px}
  .demo-top{flex-direction:column;align-items:flex-start}
  .wweb{grid-template-columns:minmax(0,1fr)}.ww-side{display:none}.ww-conv{padding-inline:12px}.ww-b{max-width:82%}
  .rd-nav nav span:not(.on),.rd-sel:not(.flt){display:none}
  .rd-cols{grid-template-columns:repeat(2,minmax(0,1fr));padding-inline:12px}.rd-col.opc{display:none}.rd-bar{padding-inline:12px}.rd-qtd{padding-inline:12px}.rd-nav{gap:16px;padding:0 12px}
  .rd-gav{width:100%}
}
@media (max-width:640px){.rd-vis,.rd-bar .dir > .ico{display:none}.palco{height:600px}.ww-doc{min-width:0}.ww-ch .acoes{display:none}.demo-card{padding:16px}}
"""

AV = '<span class="ww-av" aria-hidden="true"><svg viewBox="0 0 40 40"><circle cx="20" cy="13" r="8"/><path d="M3 40c0-10 8-15 17-15s17 5 17 15z"/></svg></span>'
IC = lambda d: svg(d)
IC_NOVA = IC('<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>')
IC_MENU = IC('<circle cx="12" cy="5" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="12" cy="19" r="1"/>')
IC_STATUS = IC('<circle cx="12" cy="12" r="9" stroke-dasharray="4 3"/><circle cx="12" cy="12" r="4"/>')
IC_BUSCA = IC('<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>')
IC_MAIS = IC('<path d="M12 5v14"/><path d="M5 12h14"/>')
IC_EMOJI = IC('<circle cx="12" cy="12" r="9"/><path d="M8.5 14.5a4.5 4.5 0 0 0 7 0"/><path d="M9 9.5h.01"/><path d="M15 9.5h.01"/>')
IC_MIC = '<svg class="ico mic" viewBox="0 0 24 24"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0"/><path d="M12 18v3"/></svg>'
IC_ENV = '<svg class="ico env" viewBox="0 0 24 24"><path d="M4 12 20 4l-4 16-4-7z"/><path d="m12 13 8-9"/></svg>'
IC_GRADE = IC('<rect x="4" y="4" width="6" height="6" rx="1"/><rect x="14" y="4" width="6" height="6" rx="1"/><rect x="4" y="14" width="6" height="6" rx="1"/><rect x="14" y="14" width="6" height="6" rx="1"/>')
IC_SINO = IC('<path d="M6 8a6 6 0 0 1 12 0c0 7 3 8 3 8H3s3-1 3-8"/><path d="M10 20a2 2 0 0 0 4 0"/>')
IC_FUNIL = IC('<path d="M5 4h4v16H5z"/><path d="M15 4h4v10h-4z"/>')
IC_LISTA = IC('<path d="M8 6h12"/><path d="M8 12h12"/><path d="M8 18h12"/><path d="M4 6h.01"/><path d="M4 12h.01"/><path d="M4 18h.01"/>')
IC_BAIXO = IC('<path d="m6 9 6 6 6-6"/>')
IC_FILTRO = IC('<path d="M4 5h16l-6 7v6l-4 2v-8z"/>')
IC_ESTRELA = IC('<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>')
IC_PESSOA = IC('<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>')
IC_CAIXA = IC('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5h8v2"/>')
IC_X = IC('<path d="M6 6l12 12"/><path d="M18 6 6 18"/>')
IC_OK = IC('<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>')
SETA_CUR = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M2 1.5 17 9l-6.5 1.6L7.4 17z"/></svg>'

# conversas ilustrativas: c = cliente (balão branco), a = agente de IA (balão verde, a tela é da empresa); d = documento enviado pelo agente
WCHATS = [
 ('Carlos Mendes', '09:38', [
   ('c', 'Olá! Quanto custa o plano para empresas?'),
   ('a', 'Olá, Carlos! Depende do tamanho do time. Quantas pessoas vão usar?'),
   ('c', 'Umas 30, no comercial.'),
   ('a', 'Para 30 pessoas, o plano Equipe atende bem. Posso agendar uma conversa com um consultor amanhã às 10h?'),
   ('c', 'Pode sim.'),
   ('a', 'Agendado! Mandei o convite para o seu e-mail.')]),
 ('Ana Souza', '09:42', [
   ('c', 'Oi, meu pedido ainda não chegou e já é a segunda vez.'),
   ('a', 'Sinto muito, Ana. Localizei o pedido 4821: ele saiu ontem e chega amanhã até as 18h.'),
   ('a', 'Para compensar a espera, liberei frete grátis na sua próxima compra.'),
   ('c', 'Nossa, obrigada pela atenção!'),
   ('a', 'Eu que agradeço. Aviso você assim que ele sair para entrega.')]),
 ('Juliana Prado', '09:53', [
   ('c', 'Posso cancelar o contrato antes de completar um ano?'),
   ('a', 'Pode, Juliana. Pela cláusula 9, basta avisar com 30 dias de antecedência e não há multa.'),
   ('a', 'Quer que eu envie o contrato com a cláusula marcada?'),
   ('c', 'Quero, por favor.'),
   ('d', 'Contrato de serviço.pdf|4 páginas · PDF')]),
]
WFIXAS = [('Marcos Vieira', 'Ontem', 'Obrigado, recebi a nota fiscal.'), ('Fernanda Lima', 'Ontem', 'Perfeito, até amanhã!'), ('Roberto Alves', 'Segunda-feira', 'Pode confirmar o endereço?'), ('Patrícia Gomes', 'Domingo', 'Combinado.')]
_ult = lambda msgs: msgs[-1][1].split('|')[0]
_li = lambda k, n, t, p: ('<li data-k="%s"%s>' % (k, ' class="on"' if k == '0' else '') + AV + '<div class="ww-li"><div class="l1"><b>%s</b><time>%s</time></div><div class="l2"><span>%s</span><i>1</i></div></div></li>' % (n, t, p))
wlista = ''.join(_li(str(k), n, t, _ult(m)) for k, (n, t, m) in enumerate(WCHATS)) + ''.join(_li('f', n, t, p) for n, t, p in WFIXAS)

# funil do CRM: negociações ilustrativas em cada etapa (valor em reais)
ETAPAS_RD = ['Sem contato', 'Contato feito', 'Identificação do interesse', 'Apresentação', 'Proposta enviada']
NEG = [[('Henrique Monteiro', 'Monteiro Logística', 0, 'Nova')],
       [('Carla Siqueira', 'Siqueira Consultoria', 1200, 'Nova')],
       [('Nina Vasconcelos', 'Vasconcelos Móveis', 2800, 'Em andamento')],
       [('Marcos Reis', 'Reis Software', 6000, 'Em andamento')],
       [('Lúcia Ferraz', 'Ferraz Engenharia', 9400, 'Em andamento')]]
real = lambda v: 'R$ ' + ('{:,.2f}'.format(v)).replace(',', 'X').replace('.', ',').replace('X', '.')
def rd_card(n, e, v, t, extra=''):
    return ('<div class="rd-card%s" data-v="%d"><span class="tg%s">%s</span><b>%s</b><small>%s</small><span class="vl">%s1 %s%s</span><span class="tf">%sCriar tarefa</span></div>'
            % (extra, v, ' and' if t != 'Nova' else '', t, n, e, IC_ESTRELA, IC_PESSOA, IC_CAIXA + ' ' + real(v), IC_MAIS))
rd_cols = ''.join('<div class="rd-col%s" data-c="%d"><div class="rd-ch"><b>%s (<i>%d</i>)</b><span>%s</span></div><div class="rd-cards">%s</div></div>'
                  % ('' if c in (0, 3) else ' opc', c, ETAPAS_RD[c], len(NEG[c]), real(sum(x[2] for x in NEG[c])), ''.join(rd_card(*x) for x in NEG[c])) for c in range(5))
CAMPOS_RD = [('Nome da negociação', 'Carlos Mendes · Plano Equipe'), ('Contato', 'Carlos Mendes'), ('Origem', 'WhatsApp'), ('Qualificação', '30 usuários no time comercial'), ('Valor estimado', 'R$ 4.500,00')]
rd_campos = ''.join('<label>%s<span class="rd-in" data-txt="%s"></span></label>' % (r, t) for r, t in CAMPOS_RD)

import json as _json
WDADOS = _json.dumps([{'n': n, 't': t, 'm': [[q, x] for q, x in m]} for n, t, m in WCHATS], ensure_ascii=False)
NOVO_RD = _json.dumps(rd_card('Carlos Mendes', 'Plano Equipe · 30 usuários', 4500, 'Nova', ' novo'), ensure_ascii=False)

demo = r"""<!-- S06 · Destaque Rumo AI: um agente de IA atendendo no WhatsApp e registrando a venda no CRM, em loop -->
<section class="sec" id="demonstracao" aria-labelledby="dmT">
  <div class="wrap">
    <div class="demo-card rv">
      <div class="demo-top">
        <div><span class="micro-l" id="dmT">Na prática</span><p>Um agente de IA atende o cliente no WhatsApp e registra a venda no CRM, sem ninguém da equipe tocar no teclado.</p></div>
        <div class="demo-tabs" aria-hidden="true"><span class="on" data-t="wa">WhatsApp</span><span data-t="crm">CRM</span></div>
      </div>
      <div class="palco" id="palco" aria-hidden="true">
        <div class="wweb tela on" id="wweb">
          <aside class="ww-side">
            <div class="ww-sh"><b>Conversas</b><span class="acoes">""" + IC_STATUS + IC_NOVA + IC_MENU + r"""</span></div>
            <div class="ww-busca">""" + IC_BUSCA + r"""<span>Pesquisar ou começar uma nova conversa</span></div>
            <div class="ww-chips"><span class="on">Tudo</span><span>Não lidas</span><span>Favoritas</span><span>Grupos</span></div>
            <ul class="ww-lista" id="wwLista">""" + wlista + r"""</ul>
          </aside>
          <div class="ww-main">
            <div class="ww-ch">""" + AV + r"""<div class="quem"><b id="wwNome">Carlos Mendes</b><small id="wwStatus">online</small></div><span class="acoes">""" + IC_BUSCA + IC_MENU + r"""</span></div>
            <div class="ww-conv" id="wwConv"><span class="ww-dia">Hoje</span></div>
            <div class="ww-pe">""" + IC_MAIS + IC_EMOJI + r"""<div class="ww-campo" id="wwCampo"><span>Digite uma mensagem</span></div><span class="ww-env" id="wwEnv">""" + IC_MIC + IC_ENV + r"""</span></div>
          </div>
        </div>
        <div class="rdc tela" id="rdc">
          <div class="rd-nav">""" + IC_GRADE + r"""<nav><span class="on">Negociações</span><span>Empresas</span><span>Contatos</span><span>Tarefas</span><span>Análises</span></nav><span class="dir">""" + IC_BUSCA + IC_SINO + r"""<span class="eu">EC</span></span></div>
          <div class="rd-bar"><span class="rd-vis"><span class="on">""" + IC_FUNIL + r"""</span><span>""" + IC_LISTA + r"""</span></span><span class="rd-sel">Funil padrão """ + IC_BAIXO + r"""</span><span class="rd-sel">Todos os status """ + IC_BAIXO + r"""</span><span class="rd-sel">Mais recentes """ + IC_BAIXO + r"""</span><span class="rd-sel flt">""" + IC_FILTRO + r"""Filtros (0)</span><span class="dir">""" + IC_MENU + r"""<span class="rd-criar" id="rdCriar">""" + IC_MAIS + r"""Criar</span></span></div>
          <div class="rd-qtd"><span id="rdQtd">5</span> negociações</div>
          <div class="rd-cols" id="rdCols">""" + rd_cols + r"""</div>
          <aside class="rd-gav" id="rdGav"><div class="rd-gh"><b>Nova negociação</b>""" + IC_X + r"""</div><div class="rd-gc">""" + rd_campos + r"""</div><div class="rd-gp"><span class="cnc">Cancelar</span><span class="slv" id="rdSalvar">Salvar</span></div></aside>
          <div class="rd-toast" id="rdToast">""" + IC_OK + r"""<span>Tarefa criada: reunião com consultor amanhã, 10:00</span></div>
          <div class="ia-cur" id="iaCur">""" + SETA_CUR + r"""<span>Agente de IA</span></div>
        </div>
      </div>
      <small class="nota">Conversas e dados ilustrativos.</small>
    </div>
  </div>
</section>

"""
agentes = agentes.replace('<!-- S04 · Serviços: as três áreas;', demo + '<!-- S04 · Serviços: as três áreas;', 1)
assert 'id="demonstracao"' in agentes

js = js.replace("/* ---------- abertura: os números contam ao entrar na tela ---------- */", r"""/* ---------- demonstração: conversa no WhatsApp e registro no CRM, em sequência e em loop; pausa fora da tela ---------- */
(function demo(){
  const palco = $('#palco'); if (!palco) return;
  const D = """ + WDADOS + r""", NOVO = """ + NOVO_RD + r""";
  const wa = $('#wweb'), rdc = $('#rdc'), abas = $$('.demo-tabs span');
  const conv = $('#wwConv'), nome = $('#wwNome'), st = $('#wwStatus'), campo = $('#wwCampo'), env = $('#wwEnv');
  const lis = $$('#wwLista li[data-k]').filter(l => l.dataset.k !== 'f');
  const CHK = '<svg viewBox="0 0 16 11"><path d="m1 6 3 3 6-7"/><path d="m6 9 1 1 6-8"/></svg>';
  let visivel = false;
  const dorme = ms => new Promise(r => setTimeout(r, ms));
  const espera = async ms => { let t = 0; while (t < ms) { while (!visivel) await dorme(200); const d = Math.min(50, ms - t); await dorme(d); t += d; } };
  const mostrar = qual => { wa.classList.toggle('on', qual === 'wa'); rdc.classList.toggle('on', qual === 'crm'); abas.forEach(a => a.classList.toggle('on', a.dataset.t === qual)); };

  /* WhatsApp */
  const hora = (base, i) => { const [h, m] = base.split(':').map(Number), tot = h * 60 + m + Math.floor(i / 2); return String(Math.floor(tot / 60) % 24).padStart(2, '0') + ':' + String(tot % 60).padStart(2, '0'); };
  let ultimo = '';
  const balao = (q, x, h) => {
    const b = document.createElement('div'), lado = q === 'c' ? 'c' : 'a';
    b.className = 'ww-b ' + lado + (ultimo !== lado ? ' pri' : ''); ultimo = lado;
    const meta = '<span class="hr">' + h + (lado === 'a' ? CHK : '') + '</span>';
    if (q === 'd') { const [n, s] = x.split('|'); b.innerHTML = '<div class="ww-doc"><em>PDF</em><div><b>' + n + '</b><small>' + s + '</small></div></div>' + meta; }
    else b.innerHTML = x + meta;
    conv.appendChild(b);
    while (conv.scrollHeight > conv.clientHeight + 2 && conv.children.length > 2) conv.children[1].remove();
    return b;
  };
  const abrir = k => {
    lis.forEach((l, i) => l.classList.toggle('on', i === k)); lis[k].classList.remove('nova');
    nome.textContent = D[k].n; st.textContent = 'online'; st.classList.remove('dig');
    conv.innerHTML = '<span class="ww-dia">Hoje</span>'; ultimo = '';
  };
  const previa = (k, x) => { lis[k].querySelector('.l2 span').textContent = x.split('|')[0]; };
  async function conversa(k){
    abrir(k);
    const ms = D[k].m;
    for (let i = 0; i < ms.length; i++) {
      const [q, x] = ms[i], h = hora(D[k].t, i);
      if (q === 'c') {
        await espera(300); st.textContent = 'digitando…'; st.classList.add('dig');
        await espera(450 + x.length * 7); st.textContent = 'online'; st.classList.remove('dig');
        balao(q, x, h); previa(k, x); await espera(400);
      } else {
        if (q !== 'd') {
          campo.classList.add('esc'); env.classList.add('on');
          const sp = campo.firstElementChild;
          for (let j = 2; j <= x.length + 1; j += 2) { sp.textContent = x.slice(0, j); await espera(15); }
          await espera(150);
        } else await espera(500);
        campo.classList.remove('esc'); env.classList.remove('on'); campo.firstElementChild.textContent = 'Digite uma mensagem';
        const b = balao(q, x, h); previa(k, x);
        await espera(350); b.classList.add('lido'); await espera(250);
      }
    }
  }
  const avisar = async k => { previa(k, D[k].m[0][1]); lis[k].classList.add('nova'); await espera(600); };

  /* CRM: o cursor do agente cria a negociação, preenche os campos, move o card no funil e agenda a tarefa */
  const cur = $('#iaCur'), gav = $('#rdGav'), toast = $('#rdToast'), qtd = $('#rdQtd'), cols = $$('#rdCols .rd-col');
  const real = v => 'R$ ' + v.toLocaleString('pt-BR', { minimumFractionDigits: 2 });
  const somar = () => { let n = 0; cols.forEach(c => { const cs = $$('.rd-card', c); n += cs.length; c.querySelector('.rd-ch i').textContent = cs.length; c.querySelector('.rd-ch span').textContent = real(cs.reduce((s, x) => s + +x.dataset.v, 0)); }); qtd.textContent = n; };
  const centro = (el, fx = .5, fy = .5) => { const a = rdc.getBoundingClientRect(), b = el.getBoundingClientRect(); return [b.left - a.left + b.width * fx, b.top - a.top + b.height * fy]; };
  let cx = 0, cy = 0;
  const ir = async (x, y) => { cx = x; cy = y; cur.style.transform = 'translate(' + x + 'px,' + y + 'px)'; await espera(450); };
  const irEl = (el, fx, fy) => ir(...centro(el, fx, fy));
  const clicar = async el => { el.classList.add('pres'); await espera(150); el.classList.remove('pres'); await espera(200); };
  const limparCRM = () => {
    $$('#rdCols .rd-card.ia, #rdCols .rd-ph').forEach(e => e.remove());
    $$('.rd-in', gav).forEach(e => { e.textContent = ''; e.classList.remove('esc'); });
    gav.classList.remove('on'); toast.classList.remove('on'); cur.classList.remove('on'); somar();
    cur.style.transition = 'none'; const a = rdc.getBoundingClientRect(); cx = a.width * .55; cy = a.height * .6; cur.style.transform = 'translate(' + cx + 'px,' + cy + 'px)'; void cur.offsetWidth; cur.style.transition = '';
  };
  async function crm(){
    limparCRM();
    await espera(500); cur.classList.add('on'); await espera(200);
    const criar = $('#rdCriar'); await irEl(criar); await clicar(criar);
    gav.classList.add('on'); await espera(350);
    for (const f of $$('.rd-in', gav)) {
      await irEl(f, .15, .5);
      f.classList.add('esc'); const t = f.dataset.txt;
      for (let j = 2; j <= t.length + 1; j += 2) { f.textContent = t.slice(0, j); await espera(15); }
      await espera(100); f.classList.remove('esc');
    }
    const salvar = $('#rdSalvar'); await irEl(salvar); await clicar(salvar);
    gav.classList.remove('on');
    const tmp = document.createElement('div'); tmp.innerHTML = NOVO; const card = tmp.firstElementChild; card.classList.add('ia');
    const dest0 = cols[0].querySelector('.rd-cards'); dest0.prepend(card); somar(); await espera(600);
    await irEl(card, .5, .3); card.classList.add('pega'); await espera(150);
    const ph = document.createElement('div'); ph.className = 'rd-ph'; ph.style.height = card.offsetHeight + 'px';
    cols[3].querySelector('.rd-cards').prepend(ph);
    const a = card.getBoundingClientRect(), b = ph.getBoundingClientRect(), dx = b.left - a.left, dy = b.top - a.top;
    card.style.transform = 'translate(' + dx + 'px,' + dy + 'px) rotate(2deg)';
    await ir(cx + dx, cy + dy);
    card.classList.add('solto'); card.style.transform = ''; ph.replaceWith(card); card.classList.remove('pega');
    const tg = card.querySelector('.tg'); tg.textContent = 'Em andamento'; tg.classList.add('and');
    void card.offsetWidth; card.classList.remove('solto'); somar(); await espera(350);
    const tf = card.querySelector('.tf'); await irEl(tf); await clicar(tf);
    toast.classList.add('on'); await espera(1800); toast.classList.remove('on');
    cur.classList.remove('on'); await espera(500);
  }

  const parado = () => { abrir(0); D[0].m.forEach(([q, x], i) => { const b = balao(q, x, hora(D[0].t, i)); b.classList.add('lido'); b.style.animation = 'none'; }); };
  if (reduce || !('IntersectionObserver' in window)) { parado(); return; }
  new IntersectionObserver(es => { visivel = es[0].isIntersecting; }, { threshold: .25 }).observe(palco);
  (async function laco(){
    for (;;) {
      mostrar('wa'); await conversa(0); await espera(900);
      mostrar('crm'); await crm();
      mostrar('wa'); await espera(500);
      for (let k = 1; k < D.length; k++) { await avisar(k); await conversa(k); await espera(1400); }
      await avisar(0);
    }
  })();
})();

/* ---------- abertura: os números contam ao entrar na tela ---------- */""")

saida = (head + comum + pill + marquee + css + etapas_faq_form + resp + hero + agentes + integ + grade + sofi + como + faq + form
         + js_base + js + js_etapas + js_faq + js_form_base.replace('/* ---------- formulário (envio desligado) ---------- */', '/* ---------- formulário (envio pelo e-mail do visitante) ---------- */') + js_submit)
io.open(os.path.join(aqui, 'modelo.html'), 'w', encoding='utf-8').write(saida)
print('ok', len(saida))
