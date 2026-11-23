// Gera servicos/terceirizacao/index.html a partir do modelo, copiando da Home
// o CSS compartilhado, o menu e o rodapé (com os links ajustados para dois níveis abaixo).
//   node gerar.mjs <raiz do repositório>
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const raiz = process.argv[2];
const aqui = dirname(fileURLToPath(import.meta.url));
const home = readFileSync(join(raiz, 'index.html'), 'utf8').replace(/\r\n/g, '\n');
const modelo = readFileSync(join(aqui, 'modelo.html'), 'utf8').replace(/\r\n/g, '\n');

const entre = (ini, fim, incluirFim = false) => {
  const a = home.indexOf(ini);
  const b = home.indexOf(fim, a + ini.length);
  if (a < 0 || b < 0) throw new Error('trecho não encontrado: ' + ini);
  return home.slice(a, incluirFim ? b + fim.length : b);
};

// Correções do que a Home ainda tem registrado em pendencias.json (aqui seguimos o design system).
const cssBase = entre(':root{color-scheme', '/* ---------- hero ----------').replace(/^:root\{[^\n]*\n/, '')
  .replace('rgb(231 233 234)', 'var(--fg)')
  .replace('line-height:1.06;text-wrap:balance', 'line-height:var(--text-h1--line-height);text-wrap:balance')
  .replace('letter-spacing:var(--text-display--letter-spacing);line-height:1.04', 'letter-spacing:var(--text-display--letter-spacing);line-height:var(--text-display--line-height)')
  .replace('.h2{font-size:var(--text-h2);line-height:1.1}', '.h2{font-size:var(--text-h2);line-height:var(--text-h2--line-height)}');
const cssRodape = entre('/* ---------- rodapé', '/* ---------- revelação');
let menu = entre('<header class="nav"', '<main id="top">').trimEnd();
let rodape = entre('<footer>', '</footer>', true);

const ajustar = (html) => html.replace(/href="([^"]*)"/g, (m, h) => {
  if (/^(https?:|mailto:|tel:|data:)/.test(h)) return m;
  if (h === '#top') return 'href="../../"';
  if (h.startsWith('#')) return `href="../../${h}"`;
  if (h === 'servicos/terceirizacao/') return 'href="./" aria-current="page"';
  return `href="../../${h}"`;
});
menu = ajustar(menu);
rodape = ajustar(rodape).replace('href="../../#servicos">Outsourcing de TI', 'href="./">Outsourcing de TI');

const saida = modelo
  .replace('/*CSS_BASE*/', cssBase.trimEnd())
  .replace('/*CSS_RODAPE*/', cssRodape.trimEnd())
  .replace('<!--MENU-->', menu)
  .replace('<!--RODAPE-->', rodape);

const destino = join(raiz, 'servicos', 'terceirizacao', 'index.html');
mkdirSync(dirname(destino), { recursive: true });
writeFileSync(destino, saida);
console.log('ok', destino, saida.length, 'bytes');
