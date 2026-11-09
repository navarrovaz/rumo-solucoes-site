#!/usr/bin/env node
// Verificador do design system do site da Rumo Soluções.
//
//   node scripts/check-ds.mjs                compara o repositório com o último commit
//   node scripts/check-ds.mjs --base <ref>   compara com outro ponto do histórico (usado no GitHub)
//   node scripts/check-ds.mjs --hook         modo do hook do Claude Code (lê o JSON da ferramenta no stdin)
//
// Saída 0: site e design system concordam. Saída 1 (ou 2 no modo --hook): há divergência nova.

import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join, dirname, extname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

export const RAIZ = join(dirname(fileURLToPath(import.meta.url)), '..');
const TOKENS = 'design-system/tokens.css';
const GUIA = 'design-system/design-system-site.md';
export const PENDENCIAS = 'design-system/pendencias.json';

const FORA_DA_VARREDURA = new Set(['.git', '.claude', '.github', '.githooks', 'node_modules', '_fonte', 'design-system', 'scripts']);
// Variáveis definidas em tempo de execução pelo JavaScript dos efeitos (cursor).
const VARIAVEIS_DE_EXECUCAO = new Set(['x', 'mx', 'my']);
const PESOS_PERMITIDOS = new Set([400, 500, 600]);
const FONTES_PERMITIDAS = new Set(['Geist', 'Geist Mono']);
const SELETORES_DE_TIPO = {
  '.display': 'display', '.h1': 'h1', '.h2': 'h2', '.h3': 'h3', '.h4': 'h4',
  'h1,h2,h3,h4': 'h1', '.label': 'label', '.micro': 'mono-micro', '.lead': 'lead',
};
const PROPRIEDADES_DE_TIPO = { 'line-height': 'line-height', 'letter-spacing': 'letter-spacing', 'font-weight': 'font-weight' };

const ONDE_NO_GUIA = {
  'cor-fora-da-paleta': 'seção 2 (Cor)',
  'use-o-token': 'seção 2 (Cor) e checklist: só tokens semânticos',
  'token-inexistente': 'tokens.css',
  'token-local': 'tokens.css: valores não são definidos nas páginas',
  'tokens-nao-importados': 'tokens.css',
  'fonte-nao-permitida': 'seção 3.1',
  'tamanho-fora-da-escala': 'seção 3.3',
  'peso-nao-permitido': 'seção 3.2',
  'tipografia-fora-do-token': 'seção 3.3',
  'raio-fora-da-escala': 'seção 5',
  'duracao-fora-da-escala': 'seção 9',
  'secao-fora-da-biblioteca': 'seção 11',
  'secao-clara-proibida': 'evolução E19',
  'textura-ausente': 'seção 8.1 e evolução E20',
  'movimento-reduzido-ausente': 'seção 15',
  'travessao-longo': 'manual, seção 14',
  'versao-desatualizada': 'cabeçalho do guia',
  'token-sem-guia': 'seção 2',
  'tokens-sem-versao': 'seção 0 (Governança)',
  'tokens-sem-evolucao': 'seção 18',
  'pendencia-nova': 'seção 0 (Governança)',
};

const ler = (rel) => readFileSync(join(RAIZ, rel), 'utf8').replace(/\r\n/g, '\n');
const semComentarios = (css) => css.replace(/\/\*[\s\S]*?\*\//g, (m) => m.replace(/[^\n]/g, ' '));
const linhaDe = (texto, pos) => texto.slice(0, pos).split('\n').length;
const hex2 = (n) => n.toString(16).padStart(2, '0').toUpperCase();

function normalizaHex(h) {
  let v = h.replace('#', '').toUpperCase();
  if (v.length === 3 || v.length === 4) v = [...v].map((c) => c + c).join('');
  return '#' + v.slice(0, 6);
}

function coresEm(valor) {
  const achadas = [];
  const limpo = valor.replace(/url\((?:"[^"]*"|'[^']*'|[^)]*)\)/g, '');
  for (const m of limpo.matchAll(/#[0-9a-fA-F]{3,8}\b/g)) {
    achadas.push({ bruto: m[0], rgb: normalizaHex(m[0]), comAlfa: m[0].length === 5 || m[0].length === 9 });
  }
  for (const m of limpo.matchAll(/rgba?\(\s*(\d+)[\s,]+(\d+)[\s,]+(\d+)[^)]*\)/g)) {
    achadas.push({ bruto: m[0].replace(/\s+/g, ''), rgb: '#' + hex2(+m[1]) + hex2(+m[2]) + hex2(+m[3]), comAlfa: /rgba|\//.test(m[0]) });
  }
  return achadas;
}

function declaracoes(corpo) {
  const saida = [];
  let inicio = 0, prof = 0, aspas = null;
  for (let i = 0; i <= corpo.length; i++) {
    const c = corpo[i];
    if (aspas) { if (c === aspas) aspas = null; continue; }
    if (c === '"' || c === "'") aspas = c;
    else if (c === '(') prof++;
    else if (c === ')') prof--;
    else if ((c === ';' && prof === 0) || i === corpo.length) {
      const txt = corpo.slice(inicio, i);
      const doisP = txt.indexOf(':');
      if (doisP > 0) {
        const antes = txt.slice(0, doisP);
        const offsetProp = inicio + (antes.length - antes.trimStart().length);
        saida.push({ prop: antes.trim().toLowerCase(), valor: txt.slice(doisP + 1).trim(), offset: offsetProp });
      }
      inicio = i + 1;
    }
  }
  return saida;
}

function regrasCss(css) {
  const limpo = semComentarios(css);
  const regras = [];
  for (const m of limpo.matchAll(/([^{}]+)\{([^{}]*)\}/g)) {
    const seletor = m[1].replace(/\s+/g, ' ').trim();
    const inicioCorpo = m.index + m[0].indexOf('{') + 1;
    regras.push({ seletor, corpo: m[2], inicioCorpo });
  }
  return regras;
}

function pxDe(texto) {
  const m = /^(-?\d*\.?\d+)(px|rem)$/.exec(texto.trim());
  return m ? (m[2] === 'rem' ? +m[1] * 16 : +m[1]) : null;
}

export function carregarTokens() {
  const css = ler(TOKENS);
  const nomes = new Set();
  const paleta = new Map();
  const brutos = new Map();
  const hexes = new Set();
  const tipo = {};
  const raios = new Set();
  const tamanhos = new Set();
  const duracoes = new Set();

  for (const r of regrasCss(css)) {
    const produto = r.seletor.includes('data-produto');
    const claro = r.seletor.includes('data-surface="light"') && !r.seletor.includes(':root');
    for (const d of declaracoes(r.corpo)) {
      if (!d.prop.startsWith('--')) continue;
      const nome = d.prop.slice(2);
      nomes.add(nome);
      if (!claro && !produto) brutos.set(nome, d.valor);
      if (produto || nome === 'grain-image') continue;
      for (const c of coresEm(d.valor)) {
        if (!paleta.has(c.rgb)) paleta.set(c.rgb, nome);
        if (!c.comAlfa) hexes.add(c.rgb);
      }
    }
  }

  const resolver = (nome, n = 0) => {
    const v = brutos.get(nome);
    const m = v && /^var\(--([\w-]+)\)$/.exec(v);
    return m && n < 6 ? resolver(m[1], n + 1) : v;
  };

  // Tokens exatos: o semântico tem preferência sobre o primitivo na sugestão.
  const exatos = new Map();
  for (const nome of brutos.keys()) {
    const v = resolver(nome);
    if (!v || !/^#[0-9a-f]{3,8}$/i.test(v)) continue;
    const rgb = normalizaHex(v);
    const atual = exatos.get(rgb);
    if (!atual || (atual.startsWith('color-') && !nome.startsWith('color-'))) exatos.set(rgb, nome);
  }

  for (const [nome, v] of brutos) {
    const raio = /^radius-/.test(nome) && pxDe(v);
    if (raio !== null && raio !== false) raios.add(raio);
    const dur = /^dur-/.test(nome) && /^(\d+)ms$/.exec(v);
    if (dur) duracoes.add(+dur[1]);
    const t = /^text-([\w-]+?)--(line-height|letter-spacing|font-weight)$/.exec(nome);
    if (t) (tipo[t[1]] ||= {})[t[2]] = parseFloat(v);
    else if (/^text-/.test(nome)) {
      const clamp = /^clamp\(([^,]+),.*,([^,)]+)\)$/.exec(v);
      for (const parte of clamp ? [clamp[1], clamp[2]] : [v]) {
        const px = pxDe(parte);
        if (px !== null) tamanhos.add(px);
      }
    }
  }
  return { css, nomes, paleta, hexes, exatos, tipo, raios, tamanhos, duracoes };
}

function maisProxima(rgb, tokens) {
  const canais = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16));
  const alvo = canais(rgb);
  let melhor = null, dist = Infinity;
  for (const [hexa, nome] of tokens.exatos) {
    const d = canais(hexa).reduce((s, v, i) => s + (v - alvo[i]) ** 2, 0);
    if (d < dist) { dist = d; melhor = `--${nome} (${hexa})`; }
  }
  return melhor;
}

function versaoDoGuia(guia) {
  const m = /\*\*Status:\*\*\s*v(\d+\.\d+)/.exec(guia);
  return m ? m[1] : null;
}
const totalDeEvolucoes = (guia) => (guia.match(/^\| E\d+ \|/gm) || []).length;

function paginas(dir = '') {
  const saida = [];
  for (const e of readdirSync(join(RAIZ, dir), { withFileTypes: true })) {
    if (e.isDirectory()) {
      if (!FORA_DA_VARREDURA.has(e.name)) saida.push(...paginas(join(dir, e.name)));
    } else if (['.html', '.css'].includes(extname(e.name))) {
      saida.push(join(dir, e.name).replace(/\\/g, '/'));
    }
  }
  return saida;
}

function verificarDeclaracao(d, seletor, linha, arquivo, tokens, add) {
  const reg = (regra, valor, msg, sugestao) => add({ arquivo, linha, regra, valor, contexto: seletor, msg, sugestao });
  const { prop, valor } = d;

  if (prop.startsWith('--')) {
    if (!VARIAVEIS_DE_EXECUCAO.has(prop.slice(2))) reg('token-local', prop, `${prop} é definido na página, não em tokens.css`);
    return;
  }
  for (const m of valor.matchAll(/var\(--([\w-]+)/g)) {
    if (!tokens.nomes.has(m[1]) && !VARIAVEIS_DE_EXECUCAO.has(m[1]) && m[1] !== 'gut') {
      reg('token-inexistente', `--${m[1]}`, `--${m[1]} não existe em tokens.css`);
    }
  }
  if (!/mask/.test(prop)) {
    for (const c of coresEm(valor)) {
      if (!tokens.paleta.has(c.rgb)) {
        reg('cor-fora-da-paleta', c.bruto, `${c.bruto} em ${prop} não pertence à paleta`, `mais próximo: ${maisProxima(c.rgb, tokens)}`);
      } else if (!c.comAlfa && tokens.exatos.has(c.rgb)) {
        reg('use-o-token', c.bruto, `${c.bruto} em ${prop} é um valor de token escrito à mão`, `use var(--${tokens.exatos.get(c.rgb)})`);
      }
    }
  }
  if (prop === 'font-family' && !/^(var\(--font-(sans|mono)\)|inherit)$/.test(valor)) {
    reg('fonte-nao-permitida', valor, `font-family ${valor}`, 'use var(--font-sans) ou var(--font-mono)');
  }
  if (prop === 'font-size') {
    const px = pxDe(valor);
    if (/^clamp\(/.test(valor) || (px !== null && !tokens.tamanhos.has(px))) {
      reg('tamanho-fora-da-escala', valor, `font-size ${valor} não está na escala tipográfica`, `escala: ${[...tokens.tamanhos].sort((a, b) => a - b).join(', ')} px`);
    }
  }
  if (prop === 'font-weight' && /^\d+$/.test(valor) && !PESOS_PERMITIDOS.has(+valor)) {
    reg('peso-nao-permitido', valor, `font-weight ${valor}`, 'pesos: 400, 500 e 600');
  }
  if (prop === 'border-radius') {
    for (const parte of valor.split(/\s+/)) {
      const px = pxDe(parte);
      if (px !== null && px !== 0 && !tokens.raios.has(px)) {
        reg('raio-fora-da-escala', parte, `border-radius ${parte} não está na escala`, `escala: ${[...tokens.raios].sort((a, b) => a - b).join(', ')} px`);
      }
    }
  }
  if (prop === 'transition' || prop === 'transition-duration') {
    const semCurvas = valor.replace(/cubic-bezier\([^)]*\)|var\([^)]*\)/g, '');
    for (const seg of semCurvas.split(',')) {
      const m = /(?:^|\s)(\d*\.?\d+)(ms|s)\b/.exec(seg);
      if (!m) continue;
      const ms = Math.round(+m[1] * (m[2] === 's' ? 1000 : 1));
      if (!tokens.duracoes.has(ms)) {
        reg('duracao-fora-da-escala', `${m[1]}${m[2]}`, `transição de ${ms}ms não é token de duração`, `escala: ${[...tokens.duracoes].sort((a, b) => a - b).join(', ')} ms`);
      }
    }
  }
  const tipoToken = SELETORES_DE_TIPO[seletor.replace(/\s*,\s*/g, ',')];
  if (tipoToken && PROPRIEDADES_DE_TIPO[prop] && !/^var\(/.test(valor)) {
    const esperado = tokens.tipo[tipoToken]?.[prop];
    if (esperado !== undefined && parseFloat(valor) !== esperado) {
      reg('tipografia-fora-do-token', valor, `${prop} ${valor} em ${seletor}; o token ${tipoToken} define ${esperado}`, `use var(--text-${tipoToken}--${prop})`);
    }
  }
}

function verificarCss(css, arquivo, base, posBase, tokens, add) {
  for (const r of regrasCss(css)) {
    if (r.seletor.startsWith('@font-face')) continue;
    for (const d of declaracoes(r.corpo)) {
      verificarDeclaracao(d, r.seletor, linhaDe(base, posBase + r.inicioCorpo + d.offset), arquivo, tokens, add);
    }
  }
}

function verificarHtml(html, arquivo, tokens, guia, add) {
  const versao = versaoDoGuia(guia);

  if (!/href="[^"]*design-system\/tokens\.css"/.test(html)) {
    add({ arquivo, linha: 1, regra: 'tokens-nao-importados', valor: 'tokens.css', contexto: 'head', msg: 'a página não importa design-system/tokens.css' });
  }

  for (const m of html.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/g)) {
    verificarCss(m[1], arquivo, html, m.index + m[0].indexOf('>') + 1, tokens, add);
  }

  // Marcação sem CSS e JS, preservando as posições para o número da linha.
  const branco = (t) => t.replace(/[^\n]/g, ' ');
  const marcacao = html
    .replace(/<style[^>]*>[\s\S]*?<\/style>/g, branco)
    .replace(/<script[^>]*>[\s\S]*?<\/script>/g, branco)
    .replace(/<!--[\s\S]*?-->/g, branco);

  for (const m of marcacao.matchAll(/\sstyle="([^"]*)"/g)) {
    for (const d of declaracoes(m[1])) {
      verificarDeclaracao(d, '[style]', linhaDe(html, m.index), arquivo, tokens, add);
    }
  }
  for (const m of marcacao.matchAll(/\s(fill|stroke|stop-color|color)="([^"]+)"/g)) {
    for (const c of coresEm(m[2])) {
      if (!tokens.paleta.has(c.rgb)) {
        add({ arquivo, linha: linhaDe(html, m.index), regra: 'cor-fora-da-paleta', valor: c.bruto, contexto: `[${m[1]}]`, msg: `${c.bruto} no atributo ${m[1]} não pertence à paleta`, sugestao: `mais próximo: ${maisProxima(c.rgb, tokens)}` });
      }
    }
  }
  for (const m of html.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/g)) {
    const inicio = m.index + m[0].indexOf('>') + 1;
    for (const s of m[1].matchAll(/['"`]\s*(#[0-9a-fA-F]{3,8})\s*['"`]|rgba?\(\s*\d+\s*,\s*\d+\s*,\s*\d+/g)) {
      const achadas = s[1] ? coresEm(s[1]) : coresEm(s[0] + ')');
      for (const c of achadas) {
        if (!tokens.paleta.has(c.rgb)) {
          add({ arquivo, linha: linhaDe(html, inicio + s.index), regra: 'cor-fora-da-paleta', valor: c.rgb, contexto: 'script', msg: `${c.rgb} no JavaScript não pertence à paleta`, sugestao: `mais próximo: ${maisProxima(c.rgb, tokens)}` });
        }
      }
    }
  }

  for (const m of html.matchAll(/fonts\.googleapis\.com\/css2\?([^"]+)"/g)) {
    for (const f of m[1].matchAll(/family=([^:&]+)/g)) {
      const nome = decodeURIComponent(f[1].replace(/\+/g, ' '));
      if (!FONTES_PERMITIDAS.has(nome)) {
        add({ arquivo, linha: linhaDe(html, m.index), regra: 'fonte-nao-permitida', valor: nome, contexto: 'head', msg: `a fonte ${nome} não pertence ao design system`, sugestao: 'use Geist e Geist Mono' });
      }
    }
  }

  const biblioteca = new Set([...guia.matchAll(/^\| \*\*(S\d+[a-z]?)\*\* \|/gm)].map((m) => m[1]));
  let cursor = 0;
  for (const m of html.matchAll(/<section\b/g)) {
    const trecho = html.slice(cursor, m.index);
    const marcadores = [...trecho.matchAll(/<!--\s*(S\d+[a-z]?)\b/g)];
    const id = marcadores.length ? marcadores[marcadores.length - 1][1] : null;
    if (!id || !biblioteca.has(id)) {
      add({ arquivo, linha: linhaDe(html, m.index), regra: 'secao-fora-da-biblioteca', valor: id || 'sem marcador', contexto: 'section', msg: id ? `a seção ${id} não existe na biblioteca do guia` : 'seção sem comentário <!-- Sxx · Nome --> da biblioteca do guia' });
    }
    cursor = m.index + 8;
  }

  for (const m of marcacao.matchAll(/data-surface="light"|class="[^"]*\blight\b[^"]*"/g)) {
    add({ arquivo, linha: linhaDe(html, m.index), regra: 'secao-clara-proibida', valor: m[0], contexto: 'marcação', msg: 'o site não usa superfícies claras desde a v0.5' });
  }
  if (!/class="[^"]*\bgrain\b/.test(marcacao) || !/class="[^"]*\blines\b/.test(marcacao)) {
    add({ arquivo, linha: 1, regra: 'textura-ausente', valor: 'grain/lines', contexto: 'body', msg: 'a página precisa da textura de grão e linhas' });
  }
  if (!/prefers-reduced-motion/.test(html)) {
    add({ arquivo, linha: 1, regra: 'movimento-reduzido-ausente', valor: 'prefers-reduced-motion', contexto: 'css', msg: 'a página não trata movimento reduzido' });
  }
  for (const m of html.matchAll(/—/g)) {
    add({ arquivo, linha: linhaDe(html, m.index), regra: 'travessao-longo', valor: '—', contexto: 'texto', msg: 'o site não usa travessão longo', sugestao: 'reescreva com vírgula, dois-pontos ou ponto' });
  }
  const marcador = /design system v(\d+\.\d+)/.exec(html);
  if (marcador && marcador[1] !== versao) {
    add({ arquivo, linha: linhaDe(html, marcador.index), regra: 'versao-desatualizada', valor: `v${marcador[1]}`, contexto: 'comentário', msg: `a página cita a v${marcador[1]}, o guia está na v${versao}` });
  }
}

function git(args) {
  try {
    return execFileSync('git', args, { cwd: RAIZ, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] });
  } catch {
    return null;
  }
}
const noHistorico = (ref, rel) => {
  const t = git(['show', `${ref}:${rel}`]);
  return t === null ? null : t.replace(/\r\n/g, '\n');
};

function verificarGovernanca(base, guia, tokens, add) {
  if (!base) return;
  const guiaAntes = noHistorico(base, GUIA);
  const tokensAntes = noHistorico(base, TOKENS);
  const compacto = (t) => t.replace(/\s+/g, '');

  if (tokensAntes !== null && guiaAntes !== null && compacto(tokensAntes) !== compacto(tokens.css)) {
    if (versaoDoGuia(guiaAntes) === versaoDoGuia(guia)) {
      add({ arquivo: GUIA, linha: 4, regra: 'tokens-sem-versao', valor: `v${versaoDoGuia(guia)}`, contexto: 'governança', msg: 'tokens.css mudou, mas a versão do guia não', sugestao: 'suba a versão no campo Status do guia' });
    }
    if (totalDeEvolucoes(guia) <= totalDeEvolucoes(guiaAntes)) {
      add({ arquivo: GUIA, linha: 1, regra: 'tokens-sem-evolucao', valor: 'seção 18', contexto: 'governança', msg: 'tokens.css mudou, mas não há evolução nova registrada', sugestao: 'adicione uma linha E## na seção 18 com o motivo' });
    }
  }

  const pendAntes = noHistorico(base, PENDENCIAS);
  if (pendAntes !== null && existsSync(join(RAIZ, PENDENCIAS))) {
    const antes = JSON.parse(pendAntes);
    const agora = JSON.parse(ler(PENDENCIAS));
    for (const [chave, qtd] of Object.entries(agora)) {
      if (qtd > (antes[chave] || 0)) {
        add({ arquivo: PENDENCIAS, linha: 1, regra: 'pendencia-nova', valor: chave, contexto: 'governança', msg: 'a lista de pendências cresceu', sugestao: 'novas divergências devem ser resolvidas, não registradas' });
      }
    }
  }
}

export const chaveDe = (v) => `${v.arquivo} | ${v.regra} | ${v.valor} | ${v.contexto}`;

export function analisar({ base } = {}) {
  const guia = ler(GUIA);
  const tokens = carregarTokens();
  const achados = [];
  const add = (v) => achados.push(v);

  for (const hexa of tokens.hexes) {
    if (!guia.toUpperCase().includes(hexa)) {
      add({ arquivo: TOKENS, linha: 1, regra: 'token-sem-guia', valor: hexa, contexto: 'paleta', msg: `${hexa} está em tokens.css, mas não está documentado no guia` });
    }
  }
  for (const arq of paginas()) {
    const texto = ler(arq);
    if (extname(arq) === '.html') verificarHtml(texto, arq, tokens, guia, add);
    else verificarCss(texto, arq, texto, 0, tokens, add);
  }
  if (existsSync(join(RAIZ, 'README.md'))) {
    const m = /design system do site \(v(\d+\.\d+)\)/.exec(ler('README.md'));
    if (m && m[1] !== versaoDoGuia(guia)) {
      add({ arquivo: 'README.md', linha: 3, regra: 'versao-desatualizada', valor: `v${m[1]}`, contexto: 'README', msg: `o README cita a v${m[1]}, o guia está na v${versaoDoGuia(guia)}` });
    }
  }
  verificarGovernanca(base, guia, tokens, add);
  return achados;
}

function separar(achados) {
  const registradas = existsSync(join(RAIZ, PENDENCIAS)) ? JSON.parse(ler(PENDENCIAS)) : {};
  const restante = { ...registradas };
  const novas = [];
  let conhecidas = 0;
  for (const v of achados) {
    const k = chaveDe(v);
    if (restante[k] > 0) { restante[k]--; conhecidas++; } else novas.push(v);
  }
  const resolvidas = Object.entries(restante).filter(([, q]) => q > 0).map(([k]) => k);
  return { novas, conhecidas, resolvidas };
}

function relatorio({ novas, conhecidas, resolvidas }) {
  const l = [];
  if (novas.length) {
    l.push('', `DESIGN SYSTEM: ${novas.length} divergência(s) nova(s)`, '');
    for (const v of novas) {
      l.push(`  ${v.arquivo}:${v.linha}  [${v.regra}]  ${v.contexto}`);
      l.push(`    ${v.msg}${v.sugestao ? `; ${v.sugestao}` : ''}`);
      if (ONDE_NO_GUIA[v.regra]) l.push(`    Regra: ${ONDE_NO_GUIA[v.regra]}`);
    }
    l.push('', 'Antes de continuar, escolha uma saída para cada divergência:');
    l.push('  A. Seguir o design system: corrija o site conforme a regra indicada.');
    l.push('  B. Mudar a rota: altere design-system/tokens.css e o guia na mesma entrega,');
    l.push('     suba a versão, registre uma evolução E## na seção 18 e espelhe no Figma.');
  } else {
    l.push('Design system: nenhuma divergência nova.');
  }
  if (conhecidas) l.push(`Pendências registradas e ainda abertas: ${conhecidas} (design-system/pendencias.json).`);
  if (resolvidas.length) {
    l.push(`Pendências já resolvidas, remova de pendencias.json (${resolvidas.length}):`);
    for (const k of resolvidas) l.push(`  ${k}`);
  }
  return l.join('\n');
}

function principal() {
  const args = process.argv.slice(2);
  const modoHook = args.includes('--hook');
  const iBase = args.indexOf('--base');

  if (modoHook) {
    let entrada = {};
    try { entrada = JSON.parse(readFileSync(0, 'utf8') || '{}'); } catch { /* sem entrada: verifica tudo */ }
    const alvo = String(entrada?.tool_input?.file_path || '').replace(/\\/g, '/');
    if (alvo && !/\.(html|css)$|design-system\//.test(alvo)) process.exit(0);
    if (/\/_fonte\//.test(alvo)) process.exit(0);
  }

  const temHead = git(['rev-parse', '--verify', 'HEAD']) !== null;
  const base = iBase >= 0 ? args[iBase + 1] : temHead ? 'HEAD' : null;
  const resultado = separar(analisar({ base }));
  const texto = relatorio(resultado);

  if (resultado.novas.length) {
    console.error(texto);
    process.exit(modoHook ? 2 : 1);
  }
  if (!modoHook) console.log(texto);
  process.exit(0);
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) principal();
