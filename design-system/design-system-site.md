# Design System: Site Rumo Soluções

> **Papel:** guia de design vivo do site e dos produtos digitais da Rumo Soluções. Fonte de verdade para qualquer página, seção, componente, landing page ou peça web, consultado por designers, desenvolvedores e agentes do Rumo-cowork.
> **Status:** v0.5 aprovada em 2026-10-23 (Home em código revisada pelo usuário): site só no preto infinito, textura de linhas + grão em movimento, spotlight que acompanha o cursor, CTA em todo card de serviço, faixa de tecnologias, avaliações do Google e perguntas frequentes (evoluções E19 a E25). v0.4 aprovada em 2026-10-22. Promovido a guia de contexto em `style/` em 2026-10-23. Evoluções E01 a E25 aplicadas ao manual de design (seção 18 deste documento).
> **Referência em código:** Home · Desktop 1440 publicada em https://navarrovaz.github.io/rumo-solucoes-site/, com todos os efeitos deste guia funcionando.
> **Contexto visual:** este arquivo não tem imagens. Para ver cada padrão, consulte o PDF `output/2026-10-22-design-system-site/Rumo-Solucoes-Design-System-Site-v0.4.pdf` (42 páginas, sumário na página 2) e o Figma [Rumo · Site · Design System](https://www.figma.com/design/5t3Mwrd1SHHL1t9K7SGZKS) (time Marketing Rumo).
> **Escopo:** site institucional rumosolucoes.com (marca mãe Rumo Soluções, com páginas de produto) e produtos digitais.
> **Base:** `style/manual-de-design.md` (identidade atual), evoluída para web. O resumo das regras do site está no manual, seção 18.
> **Plataforma alvo:** Next.js (App Router) + Tailwind CSS v4 · biblioteca espelhada no Figma
> **Contexto institucional:** `Rumo-cowork/knowledge/rumo.md`

---

## Índice

0. Como usar este documento
1. Direção criativa
2. Cor
3. Tipografia
4. Layout, grid e espaçamento
5. Forma: raios, bordas e profundidade
6. Iconografia
7. Imagem: fotografia, 3D, IA e mockups
8. Efeitos e texturas
9. Movimento
10. Componentes
11. Biblioteca de seções
12. Arquitetura do site e templates de página
13. Logotipo e selos no site
14. Conteúdo e microcopy
15. Acessibilidade e performance
16. Tokens (CSS + Tailwind v4)
17. Biblioteca no Figma
18. Evoluções propostas para o manual
19. Pendências
20. Checklist de página

---

## 0. Como usar este documento

Este é o documento de contexto para quem projeta ou desenvolve qualquer página, seção ou componente do novo site: designers, desenvolvedores e agentes de IA.

**Hierarquia:**

1. solicitação atual do usuário;
2. este documento, para tudo o que é específico do site;
3. `style/manual-de-design.md`, para tudo o que este documento não cobre;
4. `Rumo-cowork/knowledge/rumo.md`, para fatos, números, serviços e produtos.

**Regras de leitura:**

- Valores de token (seção 16) são a fonte de verdade técnica. Tabelas ao longo do texto explicam o porquê.
- Itens **[EVOLUÇÃO]** marcam onde o site amplia o manual. Todos (E01 a E25) foram aprovados e aplicados ao manual em 2026-10-23.
- Itens **[v0.5]** substituem regras anteriores deste guia. Onde uma regra antiga cita seção clara, vale a versão v0.5: o site não usa seções claras.
- Para ver um padrão antes de aplicá-lo, abra a página correspondente do PDF (sumário na página 2) ou o Figma.
- Mudanças aprovadas no site atualizam este arquivo, o Figma e o PDF juntos. Uma mudança de identidade (cor, tipografia, logo) também sobe para o manual.
- Itens **[PENDENTE]** dependem de material ou decisão do usuário (seção 19).
- Nenhum texto produzido para o site usa o travessão longo (manual, seção 14).

**Onde ver cada padrão no PDF** (`output/2026-10-22-design-system-site/Rumo-Solucoes-Design-System-Site-v0.4.pdf`):

| Seção deste documento | Páginas do PDF |
|---|---|
| 1. Direção criativa | 3 e 4 |
| 2. Cor | 5 a 8 |
| 3. Tipografia | 9 a 11 |
| 4 e 5. Grid, espaço e forma | 12 e 13 |
| 8.8 Luz direcional | 14 |
| 8. Efeitos e texturas | 15 e 16 |
| 7. Imagem | 17 |
| 6. Iconografia | 18 |
| 9. Movimento e catálogo | 19 e 20 |
| 8.11 Efeitos interativos | 21 a 23 |
| 10. Componentes (01 a 14) | 24 a 33 |
| 11. Biblioteca de seções | 34 a 38 |
| 12. Template Home | 39 |
| 16. Tokens | 40 |
| 20. Checklist de página | 41 |

---

## 1. Direção criativa

### 1.1 Conceito: "a rota"

**Rumo** significa direção, curso, orientação. O posicionamento da empresa é ser a **parceira de continuidade tecnológica**, com a síntese *"confiança de banco, velocidade de startup"*.

O site traduz isso em um conceito visual único:

> **O site é um instrumento de navegação.** Uma base escura, sóbria e precisa (a confiança de banco), atravessada por rotas que se desenham com movimento preciso (a velocidade de startup).

Esse conceito organiza todas as decisões:

| Ideia | Tradução visual |
|---|---|
| Direção / rumo | Linhas de rota com nós, que se desenham conforme o scroll |
| Alcance e continuidade | Mapa da operação: rede viva de squads, sistemas, nuvem e IA (substitui o globo na v0.4) |
| Precisão de missão crítica | Camada HUD: cantoneiras, réguas, cruzes de registro, rótulos técnicos (aprovada nas capas pessoais HUD) |
| Confiança | Dark profundo, tipografia contida, muito espaço negativo, números reais |
| Velocidade | Movimento rico, porém exato: revelações curtas, sem bounce, sem excesso |

### 1.2 Três níveis de leitura

Toda seção é montada em três níveis, sempre nesta ordem de força (aprendizado das peças HUD aprovadas):

| Nível | O que é | Peso visual |
|---|---|---|
| **1º · Mensagem** | Título, número protagonista ou imagem principal | Máximo. Um só por seção |
| **2º · Conteúdo e marca** | Texto de apoio, cards, CTA, logos, mockups | Médio |
| **3º · Camada técnica** | Grão, dot grid com spotlight, mapa de rede, rotas, HUD, rótulos mono | Mínimo. Percebida, não lida |

Se o 3º nível compete com o 1º, ele está forte demais.

### 1.3 Referência de linguagem: sites feitos em Framer

A direção pede um site no padrão dos melhores templates e sites feitos em Framer. Do repertório, **aproveitar**:

- tipografia display muito grande, com tracking negativo e peso médio;
- scroll suave e revelações de texto por linha;
- seções com scroll travado (sticky) contando uma história em etapas;
- grids "bento" assimétricos;
- bordas que acendem sob o cursor (spotlight);
- contadores, marquees e transições de página;
- spotlight que acompanha o cursor dentro dos cards [v0.5].

**Não aproveitar** (clichês do gênero que descaracterizam a Rumo):

- gradientes mesh em roxo, rosa ou laranja (roxo e laranja são proibidos pelo manual);
- glassmorphism por todo lado;
- 3D genérico de "blob" colorido ou esferas cromadas sem conceito;
- texto em contorno (outline);
- cursor customizado substituindo o cursor do sistema no site inteiro;
- excesso de efeitos simultâneos na mesma dobra.

### 1.4 Princípios

1. **Uma ideia por dobra.** Cada viewport tem um protagonista.
2. **Escuro com profundidade, nunca chapado.** Degradê radial curto + grão em todo fundo escuro.
3. **O ciano aponta.** Ele guia o olho para a ação, o ícone, a rota e uma palavra do manifesto. Não preenche áreas e não entra no título (o título usa dois tons).
4. **Movimento com função.** Toda animação revela hierarquia, mostra causa e efeito ou dá retorno a uma ação.
5. **Prova antes de promessa.** Números reais, cases reais, fotos reais, produtos reais.

### 1.5 O que já foi reprovado e não pode voltar

Registro das reprovações do usuário em peças anteriores que se aplicam ao site:

- ciano em blocos chapados (fundos, pills cheias, faixas largas);
- variações de azul em módulos sobre fundo preto;
- quadrados ou cards brancos chapados sobre fundo preto;
- branco puro encostado em preto puro sem cinza intermediário;
- ícones de biblioteca centralizados em células iguais (cara de "seletor de ícones" ou template);
- todos os elementos com o mesmo peso, sem ponto focal;
- glow aplicado sobre o logo ou o símbolo;
- luz feita com círculo ciano em desfoque gaussiano (parece mancha, não luz; use a anatomia da seção 8.8);
- logo ou símbolo em contorno no lugar do preenchimento;
- efeito de papel recortado e sombras falsas;
- mistura de várias famílias tipográficas na mesma tela (Satoshi + serifa itálica + mono, carrossel v2);
- diagramação diferente a cada tela de uma mesma série;
- cinza claro opaco brigando com o preto ("usar o preto direito");
- selo dentro de tarja ou caixa escura;
- clip-art (chips, robôs, cadeados genéricos).

---

## 2. Cor

### 2.1 Primitivas

As primitivas são a paleta bruta. Componentes **nunca** usam primitivas diretamente: usam as semânticas da seção 2.2.

#### Neutros escuros (`ink`) [EVOLUÇÃO]

O manual tem três tons escuros (#050505, #171717, #262626). Um site precisa de degraus para fundo, superfície, hover, borda e desabilitado. A escala abaixo mantém os três tons oficiais e acrescenta os intermediários já usados nas peças aprovadas (#121212 → #080808 da capa 01; #2E2E2E das linhas).

| Token | HEX | Papel |
|---|---|---|
| `ink-950` | `#050505` | Fundo base (oficial) |
| `ink-925` | `#0B0B0B` | Fundo afundado, rodapé, fim do degradê |
| `ink-900` | `#121212` | Início do degradê radial de fundo |
| `ink-850` | `#171717` | Superfície: cards, painéis, inputs (oficial) |
| `ink-800` | `#1E1E1E` | Superfície elevada, hover de card |
| `ink-750` | `#262626` | Borda e divisor (oficial) |
| `ink-700` | `#2E2E2E` | Borda forte, hover de borda |
| `ink-600` | `#3D3D3D` | Desabilitado, trilhas inativas |
| `ink-500` | `#858585` | Texto terciário: legendas, metadados |
| `ink-400` | `#A1A1A1` | Texto secundário: corpo (oficial) |
| `ink-0` | `#FFFFFF` | Texto principal (oficial) |

#### Ciano (`rumo`) [EVOLUÇÃO]

Uma única cor de marca, com degraus **apenas para estados de interação**. Os degraus não são cores decorativas e nunca aparecem lado a lado como paleta (reprovação: "variação de azul no fundo preto ficou horrível").

| Token | HEX | Papel |
|---|---|---|
| `rumo-400` | `#33BDEA` | Hover do botão primário |
| `rumo-500` | `#00ACE5` | **Cor oficial de marca** |
| `rumo-600` | `#0096C7` | Pressionado (active) |
| `rumo-700` | `#00759C` | Ciano para texto sobre fundo claro (oficial do Modo claro) |
| `rumo-800` | `#005A78` | Pressionado sobre fundo claro |
| `rumo-a08` | `rgba(0,172,229,.08)` | Fundo de tag ativa, hover sutil |
| `rumo-a16` | `rgba(0,172,229,.16)` | Anel de foco em input |
| `rumo-a28` | `rgba(0,172,229,.28)` | Borda de elemento ativo |

#### Neutros frios claros (`ice`)

Herdados do Modo claro do manual (seção 1.4), com um acréscimo para legenda.

| Token | HEX | Papel |
|---|---|---|
| `ice-0` | `#FFFFFF` | Fundo claro (início do degradê) |
| `ice-50` | `#F2F8FB` | Fim do degradê claro, superfície alternada |
| `ice-100` | `#EAF7FC` | Superfície azul-gelo: tags, faixas leves |
| `ice-150` | `#E4F4FA` | Superfície azul-gelo alternativa |
| `ice-200` | `#D8E5EB` | Linhas, divisores, contornos de card |
| `ice-300` | `#C6E8F4` | Borda azul-gelo |
| `ice-500` | `#5B6B73` | Texto terciário no claro [EVOLUÇÃO: substitui o #8C8C8C, que tem contraste 3,4:1 e falha no AA] |
| `ice-700` | `#24323A` | Texto de corpo no claro |
| `ice-900` | `#0A1419` | Texto principal no claro |

#### Funcionais

| Token | HEX | Uso |
|---|---|---|
| `success` | `#13C71A` | Status real (Ativo, Enviado, Online). Nunca decorativo (manual 2.3) |
| `success-on-light` | `#0B7A10` | Mesmo papel, sobre fundo claro [EVOLUÇÃO] |
| `error` | `#F2555A` | Erro de formulário e validação, sobre escuro [EVOLUÇÃO] |
| `error-on-light` | `#C4262E` | Erro sobre fundo claro [EVOLUÇÃO] |

Vermelho existe **somente** como feedback de erro em formulário. O manual proíbe vermelho decorativo, e isso continua valendo. Não há cor de "aviso" (amarelo ou laranja): avisos usam ciano + ícone.

### 2.2 Semânticas

São estes nomes que os componentes usam. Cada um muda de valor conforme a superfície da seção (`data-surface="dark"` ou `"light"`).

> **[v0.5]** O site usa só a coluna Dark. A coluna Light fica para interfaces de produto que já são claras (mockups fiéis) e para peças fora do site.

| Token semântico | Dark (padrão) | Light (fora do site) |
|---|---|---|
| `bg` | `ink-950` | `ice-0` |
| `bg-sunken` | `ink-925` | `ice-50` |
| `surface` | `ink-850` | `ice-0` + borda `ice-200` |
| `surface-raised` | `ink-800` | `ice-0` + sombra `md` |
| `surface-tint` | `rumo-a08` | `ice-100` |
| `border` | `ink-750` | `ice-200` |
| `border-strong` | `ink-700` | `ice-300` |
| `fg` | `ink-0` | `ice-900` |
| `fg-muted` | `ink-400` | `ice-700` |
| `fg-subtle` | `ink-500` | `ice-500` |
| `brand` | `rumo-500` | `rumo-500` |
| `brand-hover` | `rumo-400` | `rumo-400` |
| `brand-pressed` | `rumo-600` | `rumo-600` |
| `brand-text` | `rumo-500` | `rumo-700` |
| `heading-secondary` | `ink-500` | `ice-500` |
| `fg-unlit` | branco 22% | `ice-900` 22% |
| `surface-soft` | `ink-850` | `ice-100` |
| `surface-soft-alt` | `ink-800` | `ice-50` |
| `disc` | `ink-800` | `ice-900` |
| `on-brand` | `ink-950` | `ink-950` |
| `focus-ring` | `rumo-500` | `rumo-700` |
| `success` | `success` | `success-on-light` |
| `error` | `error` | `error-on-light` |

### 2.3 Proporção no site

| Superfície | Proporção aproximada |
|---|---|
| Seções escuras | 75% fundos `ink` · 18% textos (branco e cinzas) · 5% ciano · 2% funcionais |
| Página inteira [v0.5] | 100% no preto infinito. Nenhuma seção clara: o ritmo entre seções vem de espaço, fios de 1px que esmaecem nas pontas e mudanças de densidade dos efeitos |

### 2.4 Contrastes verificados (WCAG 2.2)

| Texto | Fundo | Contraste | Resultado |
|---|---|---|---|
| `#FFFFFF` | `#050505` | 19,8:1 | AAA |
| `#A1A1A1` | `#050505` | 7,9:1 | AAA |
| `#A1A1A1` | `#171717` | 6,9:1 | AA |
| `#858585` | `#050505` | 5,5:1 | AA |
| `#858585` | `#171717` | 4,9:1 | AA |
| `#00ACE5` | `#050505` | 7,8:1 | AAA |
| `#050505` | `#00ACE5` (botão) | 7,8:1 | AAA |
| `#FFFFFF` | `#00ACE5` (botão) | 2,6:1 | **Falha.** Texto de botão ciano é sempre `#050505` [EVOLUÇÃO: o manual 5 permitia branco 600+] |
| `#00759C` | `#FFFFFF` | 5,2:1 | AA |
| `#0A1419` | `#FFFFFF` | 18,6:1 | AAA |
| `#24323A` | `#FFFFFF` | 12,9:1 | AAA |
| `#5B6B73` | `#FFFFFF` | 5,5:1 | AA |
| `#F2555A` | `#050505` | 6,0:1 | AA |
| `#C4262E` | `#FFFFFF` | 5,7:1 | AA |
| `#0B7A10` | `#FFFFFF` | 5,5:1 | AA |

`#3D3D3D` e `#262626` nunca levam texto: são só estrutura.

### 2.5 Acentos de produto [EVOLUÇÃO]

Decisão: **base Rumo + acento do produto.** Nas páginas de produto, a estrutura (fundo, tipografia, navegação, rodapé, grid) continua Rumo. Só o token `accent` muda, dentro do escopo da página (`data-produto="..."`).

O acento substitui o ciano **somente** em: eyebrow e tags da página, ícones de destaque, palavras destacadas no título, indicador de abas, luz de topo dos cards e do hero da página e CTA primário da página. A navegação global e o rodapé continuam em ciano Rumo.

| Produto | `accent` (sobre escuro) | `accent-text` (sobre claro) | `on-accent` | Status |
|---|---|---|---|---|
| Rumo (padrão) | `#00ACE5` | `#00759C` | `#050505` | Definido |
| PriceFleet | `#009844` | `#007A37` | `#050505` | Definido a partir da identidade do produto (`knowledge/rumo.md` 14.1). Apoio: `#2C3E4F` |
| Rumo AI | `#00ACE5` | `#00759C` | `#050505` | Usa a identidade da marca mãe até haver assets próprios **[PENDENTE]** |
| Sófi | a definir | a definir | a definir | **[PENDENTE]** |
| Genial | a definir | a definir | a definir | **[PENDENTE]** |
| SGAE | a definir | a definir | a definir | **[PENDENTE]** |
| Startvet | a definir | a definir | a definir | **[PENDENTE]** |

Regras:

- O verde do PriceFleet é cor de marca do produto, não status. Na página do PriceFleet, não usar o verde de status `#13C71A` para evitar confusão.
- Texto sobre o verde PriceFleet: `#050505` (5,4:1). Branco falha (3,8:1).
- A tipografia do produto (Nunito Sans no PriceFleet) **não** entra no site Rumo. O logo do produto entra como arquivo oficial.
- Um acento novo só entra com contraste verificado nas duas superfícies.

### 2.6 Degradês permitidos

| Degradê | Especificação | Uso |
|---|---|---|
| Fundo escuro | radial a partir do topo central: `#121212` → `#0B0B0B` → `#050505` | Fundo de toda seção escura |
| Fundo claro | radial curto a partir do canto superior esquerdo: `#FFFFFF` → `#F2F8FB` | Fundo de toda seção clara |
| Fade de imagem | radial ou linear de transparente → `bg` da seção | Integrar foto, vídeo ou 3D ao fundo |
| Luz direcional | fonte #F2FBFF → núcleo #7FD8F5 → corpo #00ACE5 → queda #005A78 → transparente, em Screen | Borda de topo, controles acesos, nós acesos (seção 8.8). Nunca elipse desfocada |
| Fio que esmaece | linear `rumo-500` 100% → 0% em linha de 1px | Divisores de destaque, linhas de rota |

Proibidos: ciano → verde em área grande, azuis antigos, arco-íris, mesh colorido, qualquer degradê que use roxo ou laranja.

---

## 3. Tipografia

### 3.1 Família: Geist [EVOLUÇÃO v0.4]

**Decisão do usuário (v0.4):** o site usa **Geist**, a família da referência Lumora, em títulos, corpo e interface, com **Geist Mono** nos rótulos e na camada técnica. Substitui a Satoshi: a Geist é mais encorpada, tem mais leitura e combina com a mono da mesma família. Poppins e Satoshi ficam fora do site.

- Uma família (com sua mono) mantém consistência e carregamento leve.
- Contraste entre níveis vem de **tamanho e peso**, não de troca de família.
- **Geist Mono:** labels de seção, rótulos HUD, índices (`01 / 05`), metadados e números de painel. Caixa alta quando for rótulo, até 13px (exceto números de painel do HUD).
- **Fallback:** Inter, depois `system-ui`.

**Carregamento:** `next/font/google` (Geist e Geist Mono, licença SIL Open Font License), variável, `display: swap`, pré-carregar só Geist. Números tabulares (`tnum`) em contadores e tabelas.

### 3.2 Pesos [EVOLUÇÃO v0.4]

| Uso | Peso |
|---|---|
| Display, H1, H2, H3 | **600 (SemiBold)**, como na Lumora |
| H4, botões, números grandes | 500 (Medium) |
| Lead, corpo, interface, navegação | 400 (Regular) |
| Números do HUD | Geist Mono 400 |
| 700 ou mais | Não usar |

No máximo 3 pesos por tela.

### 3.3 Escala fluida [v0.4]

Escala harmônica: o display tem cerca de **4x o lead** (Lumora: 68px sobre 18px). Valores de 375px a 1440px.

| Token | Tamanho | Desktop / mobile | Entrelinha | Tracking | Peso | Uso |
|---|---|---|---|---|---|---|
| `display` | `clamp(2.75rem, 5.6vw, 5rem)` | 80 / 44 | 1.02 | -0.04em | 600 | Título do hero. Uma vez por página |
| `h1` | `clamp(2.5rem, 4.4vw, 4rem)` | 64 / 40 | 1.04 | -0.035em | 600 | Título de página interna, CTA final |
| `h2` | `clamp(2rem, 3.4vw, 3rem)` | 48 / 32 | 1.08 | -0.03em | 600 | Título de seção, manifesto |
| `h3` | `clamp(1.375rem, 2vw, 1.75rem)` | 28 / 22 | 1.2 | -0.02em | 600 | Título de bloco, card grande |
| `h4` | `clamp(1.125rem, 1.4vw, 1.25rem)` | 20 / 18 | 1.3 | -0.01em | 500 | Título de card |
| `stat` | `clamp(2.75rem, 5vw, 4.5rem)` | 72 / 44 | 1 | -0.03em | 500 | Números protagonistas |
| `lead` | `clamp(1.125rem, 1.4vw, 1.25rem)` | 20 / 18 | 1.55 | -0.005em | 400 | Parágrafo abaixo do título |
| `body` | `clamp(1rem, 0.95rem + 0.2vw, 1.0625rem)` | 17 / 16 | 1.6 | 0 | 400 | Texto corrido |
| `body-article` | `clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem)` | 19 / 17 | 1.7 | 0 | 400 | Corpo de artigo e case |
| `small` | `0.875rem` | 14 | 1.55 | 0 | 400 | Descrição de card, apoio |
| `caption` | `0.8125rem` | 13 | 1.5 | 0 | 400 | Legenda, data |
| `label` | `0.75rem` | 12 / 11 | 1 | 0.06em | Mono 500 | Eyebrow de seção (Geist Mono). CAIXA ALTA |
| `button` | `0.9375rem` | 15 | 1 | -0.005em | 500 | Texto de botão |
| `mono-micro` | `0.6875rem` | 11 | 1 | 0.06em | Mono 400 | Camada HUD. CAIXA ALTA |

[EVOLUÇÃO] Corpo mínimo de **16px** (o manual aceitava 0.9rem, cerca de 14px). 16px é o mínimo confortável em tela e evita zoom automático em campos no iOS.

### 3.4 Regras de composição tipográfica

- Contraste de tamanho agressivo: o título tem pelo menos 3x o tamanho do corpo (manual 4.3).
- **Título em dois tons** [EVOLUÇÃO E17]: a 1ª frase em `fg`, a 2ª em `heading-secondary` (cinza frio, 5,5:1). Vale para display, H1 e H2; H3 e H4 ficam em um tom. O título não leva ciano. Quebre a linha onde a frase muda de tom (ex.: "A TI que sustenta / quem não pode parar.").
- Títulos com `text-wrap: balance`. Parágrafos com `text-wrap: pretty`.
- Linha de texto corrido com no máximo **65 caracteres** (`max-width: 65ch`). Lead com no máximo 48ch.
- Alinhamento à esquerda por padrão. Centralizar só hero curto, CTA final e manifesto.
- Números com `font-variant-numeric: tabular-nums` em contadores, tabelas e métricas.
- Caixa alta só em `label` e `mono-micro`. Nunca em corpo nem em título.
- Sem texto em contorno, sem sombra em texto, sem degradê dentro de letras.

### 3.5 Hierarquia padrão de uma seção

```
[label]   SERVIÇOS                      → rumo-500, 12px, +0.12em
[h2]      Sua operação não pode parar.  → fg
          A nossa também não.           → heading-secondary (dois tons)
[lead]    Texto de apoio curto...       → ink-400, máx. 48ch
[ação]    Botão primário ou link        → no máximo um CTA primário
```

Espaços: label → título 24px · título → lead 24px a 32px · lead → ação 40px.

---

## 4. Layout, grid e espaçamento

### 4.1 Breakpoints

| Token | Largura mínima | Colunas | Uso típico |
|---|---|---|---|
| (base) | 0 | 4 | Celular |
| `sm` | 640px | 4 | Celular grande |
| `md` | 768px | 8 | Tablet |
| `lg` | 1024px | 12 | Notebook |
| `xl` | 1280px | 12 | Desktop |
| `2xl` | 1536px | 12 | Desktop grande |
| `3xl` | 1720px | 12 | Container máximo (manual 6.2) |

### 4.2 Grid

| Item | Valor |
|---|---|
| Container máximo | 1720px (manual) |
| Margem lateral | `clamp(1.5rem, 3.5vw, 4rem)` (manual) |
| Gutter | `clamp(1rem, 1.6vw, 1.5rem)` |
| Coluna de leitura (artigo, case) | 720px, centralizada ou deslocada para a esquerda com índice lateral |
| Coluna de texto em seção | 5 a 6 colunas de 12 |

Composições preferidas:

- **5 + 7:** texto à esquerda, visual à direita (padrão de seção);
- **4 + 8:** título curto, visual protagonista;
- **12:** manifesto, número protagonista, CTA final;
- **Bento:** grid de 12 colunas com células de tamanhos diferentes (6+6, 8+4, 4+4+4 em linhas alternadas). Nunca células todas iguais.

Todo canto da composição precisa ter função (reprovação: "espaço vazio no topo direito"). Espaço negativo é intencional; vazio por esquecimento não.

### 4.3 Escala de espaçamento

Base de 4px.

| Token | Valor | Uso típico |
|---|---|---|
| `1` | 4px | Ícone ↔ texto pequeno |
| `2` | 8px | Ícone ↔ texto, gaps de tag |
| `3` | 12px | Padding de tag |
| `4` | 16px | Gap entre elementos de um card |
| `6` | 24px | Label → título, título → lead |
| `8` | 32px | Padding de card |
| `10` | 40px | Lead → CTA |
| `12` | 48px | Padding de card grande |
| `16` | 64px | Cabeçalho de seção → conteúdo |
| `24` | 96px | Cabeçalho de seção → conteúdo (desktop) |
| `32` | 128px | Respiro entre blocos de uma seção longa |

### 4.4 Ritmo vertical das seções

| Token | Valor | Uso |
|---|---|---|
| `section-y` | `clamp(6rem, 11vw, 10rem)` | Padding vertical padrão de seção (96px a 160px) |
| `section-y-tight` | `clamp(4rem, 8vw, 8rem)` | Faixas de prova, logos, seções curtas |
| `section-y-hero` | altura mínima `100svh`, conteúdo ancorado no terço inferior | Hero |

"Na dúvida, dobre o espaçamento" (manual 6.1).

### 4.5 Camadas (z-index)

| Token | Valor | Uso |
|---|---|---|
| `z-base` | 0 | Conteúdo |
| `z-decor` | 1 | Dot grid, mapa de rede, HUD (sempre `pointer-events: none`) |
| `z-raised` | 10 | Cards em hover, mídia sobreposta |
| `z-sticky` | 100 | Elementos sticky de seção |
| `z-nav` | 200 | Navegação |
| `z-overlay` | 300 | Mega menu, menu mobile |
| `z-modal` | 400 | Modais |
| `z-toast` | 500 | Notificações |
| `z-grain` | 900 | Camada de grão (`pointer-events: none`) |

---

## 5. Forma: raios, bordas e profundidade

### 5.1 Raios [EVOLUÇÃO: escala explícita dentro da faixa 6px a 12px do manual]

| Token | Valor | Uso |
|---|---|---|
| `radius-xs` | 4px | Checkbox, código inline, marcadores |
| `radius-sm` | 6px | Botão pequeno, input pequeno, tooltip |
| `radius-md` | 8px | Botão, input, container de ícone |
| `radius-lg` | 12px | Card, mídia, mockup, mega menu |
| `radius-panel` | 24px | Somente cantos superiores do painel claro que sobe sobre a seção escura (seção 8.10) |
| `radius-pill` | 999px | Tag, filtro, status |

Nada de card com raio acima de 12px. Nada de canto totalmente reto em botão.

### 5.2 Bordas

- Sempre **1px**. Nunca bordas grossas (manual 15.3).
- Escuro: `border` (`#262626`) ou branco a 6% a 9%. Hover: `border-strong` (`#2E2E2E`) ou branco a 16%.
- Claro: `ice-200`; hover `ice-300`.
- Destaque: fio ciano que esmaece (degradê 100% → 0%), nunca borda ciano cheia em volta de card.

### 5.3 Profundidade no escuro

No dark, profundidade vem de **tom de superfície + borda + luz de topo**, não de sombra.

| Nível | Especificação |
|---|---|
| 0 · Fundo | `bg` com degradê radial e grão |
| 1 · Superfície | `surface` (`#171717`) + borda `#262626` |
| 2 · Elevada | `surface-raised` (`#1E1E1E`) + borda `#2E2E2E` + `inset 0 1px 0 rgba(255,255,255,.04)` (luz de topo) |
| 3 · Flutuante | Nível 2 + `0 24px 48px -12px rgba(0,0,0,.6)` (mega menu, modal, dropdown) |

### 5.4 Profundidade no claro

| Token | Valor |
|---|---|
| `shadow-sm` | `0 1px 2px rgba(10,20,25,.06)` |
| `shadow-md` | `0 8px 24px -8px rgba(10,20,25,.12)` |
| `shadow-lg` | `0 24px 48px -16px rgba(10,20,25,.18)` |

Sombras sempre frias (base `#0A1419`), nunca pretas puras. Nada de sombra pesada (manual 15.3).

### 5.5 Vidro (backdrop blur)

Uso **restrito** a três casos funcionais:

1. navegação depois do scroll;
2. mega menu;
3. chips flutuando sobre foto ou vídeo.

Especificação escura: `background: rgba(5,5,5,.72)`, `backdrop-filter: blur(16px) saturate(140%)`, borda inferior `rgba(255,255,255,.06)`.

Não usar vidro em cards de conteúdo nem em ícones 3D (reprovação: sinais de código em vidro 3D azul).

---

## 6. Iconografia

### 6.1 Biblioteca

**Lucide** (`lucide-react`), estilo outline, conforme manual 9.4.

| Item | Valor |
|---|---|
| Traço | 1.5px (`strokeWidth={1.5}`), sem escalonar o traço com o tamanho (`absoluteStrokeWidth`) |
| Tamanhos | 16px (inline, botões) · 20px (navegação, listas) · 24px (cards) · 32px (destaque de seção) |
| Cor padrão | `fg-muted` |
| Cor de destaque | `brand-text` ou `accent` |
| Cantos | Arredondados (padrão Lucide) |

### 6.2 Regras

- Um estilo só no site inteiro. Não misturar Lucide com Phosphor, Heroicons ou ícones filled.
- Ícone é **apoio**, nunca o protagonista de uma seção.
- **Proibido** o padrão "ícone centralizado em célula igual" repetido em grade (reprovação "desenho de criança"). Em grid de serviços, o ícone fica alinhado à esquerda, pequeno, acima do título, e pelo menos uma célula do grid tem visual próprio (mockup, foto, rota).
- Container de ícone, quando necessário: 40px × 40px, `radius-md`, borda `border`, fundo transparente ou `surface`. Nunca fundo ciano cheio.
- Ícones de tecnologia (stack, integrações): logos oficiais das tecnologias em monocromático `ink-500`, que vão para branco no hover. Nunca em cor original misturada.
- Seta de link: `ArrowRight` ou `ArrowUpRight` (link externo), 16px.

### 6.3 Ícones proprietários (opcional, fase 2)

Para os seis serviços, pode existir um conjunto próprio desenhado sobre o grid da Lucide (24px, traço 1.5px, cantos 2px), incorporando o motivo de rota (linha + nó). Só criar se o conjunto Lucide não diferenciar o site o suficiente.

---

## 7. Imagem: fotografia, 3D, IA e mockups

### 7.1 Hierarquia de imagens

1. **Fotografia real** da Rumo (equipe, sede, eventos, Rumo Academy, NOC);
2. **mockups reais** dos produtos e de entregas;
3. **composições gráficas** (tipografia + mapa de rede + HUD + 3D);
4. **imagens geradas por IA**, somente conceituais.

### 7.2 Fotografia

**Tratamento (dark):**

- baixa saturação (–20 a –35);
- contraste alto, pretos levemente levantados (curva com ponto preto em cerca de 8 a 12);
- temperatura neutra a fria; luz ciano só quando vier de fonte real (monitor, luminária);
- vinheta suave e grão por cima, alinhado ao grão do site;
- integração ao fundo com fade radial (nunca foto em caixa rígida sem motivo, manual 10.6);
- texto sobre foto: overlay `#050505` de 40% a 70% (manual 10.2).

**Tratamento (seções claras):** natural, levemente dessaturado, sem overlay escuro, cantos `radius-lg`.

**Lista de fotos para produzir [PENDENTE: `assets/fotos/` está vazia]:**

| Tema | Enquadramento |
|---|---|
| Desenvolvimento | Pessoas trabalhando com código em telas, luz do monitor no rosto, sem olhar para a câmera |
| Sustentação 24/7 | Telas de monitoramento e painéis reais, ambiente de baixa luz |
| Squads | Conversas reais em torno de tela ou quadro, plano médio, em ação |
| Rumo Academy | Treinamentos, mentoria, mãos em teclado |
| Sede | Fachada, arquitetura, detalhes de materiais (Lagoa Santa) |
| Liderança | Retratos ambientados, luz lateral, fundo escuro, sem pose de banco de imagem |
| Eventos | Minas Summit e eventos com presença real da Rumo |
| Detalhes | Hardware, cabos, teclados, close-ups técnicos para composições |

Evitar: aperto de mão, sorriso posado para a câmera, reunião encenada, foto clara e saturada sem tratamento (manual 10.5 e 15.4).

### 7.3 3D

| Regra | Especificação |
|---|---|
| Materiais | Monocromáticos: grafite, preto fosco, metal escovado escuro, vidro fumê escuro |
| Cor | O ciano entra como **luz** (emissivo pequeno, reflexo, linha de rota), nunca como material dominante |
| Iluminação | Low-key, luz de recorte lateral, sombra projetada de verdade |
| Objetos aprovados | Símbolo da Rumo extrudado monocromático (capa isométrica aprovada). O globo saiu na v0.4 |
| Proibido | Glow ou contorno no símbolo; blobs coloridos; robôs humanoides; esferas cromadas sem conceito; 3D "fofo" |
| Entrega | Tempo real (React Three Fiber) no hero; renders estáticos ou vídeo `webm` nas demais seções |

### 7.4 Imagens geradas por IA

- Somente conceituais: ambientes, texturas, materiais, abstrações de dados.
- Pessoas geradas por IA nunca representam colaboradores, clientes ou depoimentos da Rumo.
- Mesmo tratamento da fotografia real.
- Nunca simular evento, escritório ou entrega que não aconteceu.

### 7.5 Mockups

- Telas reais dos produtos e de projetos entregues (com autorização do cliente).
- Interface dark ou clara conforme o produto real. Não "escurecer" a interface de um produto que é claro.
- Moldura mínima: `radius-lg`, borda `border`, sombra nível 3. Sem moldura de notebook 3D genérica.
- Proibido inventar funcionalidade ou exibir dado fictício como real (manual 10.7).

### 7.6 Composições tipográficas

Seções sem foto se apoiam em tipografia + camada técnica:

- display gigante com revelação por linha e título em dois tons;
- número protagonista (`stat`) com rota desenhada até ele;
- manifesto em uma coluna, com HUD discreto nos cantos.

### 7.7 Proporções de mídia

| Uso | Proporção |
|---|---|
| Hero de página interna | 21:9 ou tela cheia com fade |
| Card de case | 16:10 |
| Card de artigo | 16:9 |
| Retrato de liderança | 4:5 |
| Mockup de produto | Proporção real da tela |
| Thumbnail de vídeo | 16:9 |

---

## 8. Efeitos e texturas

Cada efeito tem função. Nenhum entra só para "parecer tecnologia" (manual, `CLAUDE.md` seção 19). Máximo de **dois efeitos da camada técnica visíveis por viewport** (o grão não conta).

### 8.1 Grão (obrigatório)

Toda superfície do site tem grão, como em todas as peças aprovadas.

| Item | Valor |
|---|---|
| Implementação | Uma única camada fixa em tela cheia, com ruído SVG (`feTurbulence`, `baseFrequency` cerca de 0.8) ou PNG de ruído 256px repetido |
| Opacidade | Escuro: 3,5% a 5% · Claro: 2,5% |
| Mistura | `mix-blend-mode: overlay` (escuro) ou `soft-light` (claro) |
| Interação | `pointer-events: none`, `z-grain` |
| Movimento [v0.5] | Grão em movimento: a camada (80px maior que a tela) desloca até 24px em 7 passos a cada 1,4s (`steps(7)`), só com `transform`. Parado em movimento reduzido |

### 8.1b Linhas de varredura [v0.5]

Textura de linhas horizontais finas sobre toda a página, junto com o grão. Princípio aprendido no site de referência Signal (Framer), aplicado com valores próprios.

| Item | Valor |
|---|---|
| Desenho | Linha de 1px a cada 3px: `repeating-linear-gradient(180deg, rgb(231 233 234) 0 1px, transparent 1px 3px)` |
| Opacidade | 2,5% a 3% |
| Camada | Fixa, em tela cheia, acima do conteúdo e abaixo da navegação, `pointer-events: none` (mesma camada do grão) |
| No Figma | Componente `Texture/Lines` (preenchimento em mosaico) sobre cada seção e template |
| Limite | Nunca mais forte que 4%: a linha é percebida como acabamento, não como efeito |

```css
.texture { position: fixed; inset: 0; pointer-events: none; z-index: 200; overflow: hidden; }
.texture .lines { position: absolute; inset: 0; opacity: .028;
  background: repeating-linear-gradient(180deg, rgb(231 233 234) 0 1px, transparent 1px 3px); }
.texture .grain { position: absolute; inset: -80px; opacity: .06; mix-blend-mode: overlay;
  background-image: var(--grain); animation: grain 1.4s steps(7) infinite; }
```

### 8.2 Fundo escuro com profundidade

Degradê radial do topo central `#121212` → `#050505` (seção 2.6) + grão. Nenhuma seção escura tem fundo chapado.

### 8.3 Dot grid

| Item | Valor |
|---|---|
| Ponto | 1px |
| Espaçamento | 24px |
| Cor | Branco a 6% (escuro) · ciano a 10% (claro) |
| Máscara | Sempre com fade radial: aparece em uma área (atrás do título ou do visual), nunca uniforme na página toda |
| Conceito | Dados, redes, sistemas |

### 8.4 Mapa da operação (assinatura, substitui o globo) [v0.4]

O globo em wireframe saiu: ficava vazio, sem impacto e sem interatividade. No lugar, uma rede viva no estilo da referência Signal (componente `BG/Network Graph`).

| Item | Valor |
|---|---|
| Base | Pretos frios: radial `#11141A` → `#0A0C0F` → `#07080A` |
| Grade | Linhas de 1px a cada 60px, branco a 3% |
| Hubs | 12 hubs rotulados em Geist Mono 12px (squad-java, erp-core, noc-24/7, crm, ia-agent, cloud-aws, legado-cobol, api-gateway, db-oracle, devops-k8s, qa, squad-.net): quadrado 12px com miolo |
| Satélites | ~300 nós com glifos técnicos (quadrado, losango, anel, ponto), ligados ao hub por arestas de 1px a 4% a 13%; rótulos curtos a 20% |
| Poeira | ~340 micropontos de 1,2px a 5% a 19% |
| Rotas ativas | 6 arestas em degradê azul quase branco → ciano, com nós acesos (anatomia 8.8) |
| Zona calma | Elipse central onde a rede esmaece até 8%; o texto do hero fica ali |
| Legibilidade | Véu radial `#07080A` (94% → 0) atrás do conteúdo central e véus nos cantos atrás do HUD |
| No site | Canvas 2D: nós flutuam de 6 a 14px, rotas pulsam a cada 4s, raio de 140px atrai nós ao redor do mouse e acende arestas, hover no hub abre um cartão (efeito 05 da seção 8.11) |

Os rótulos são ilustrativos da operação de um cliente (sistemas e squads genéricos), sem números inventados.

### 8.4b Dot grid com spotlight [v0.4]

Componente `BG/Dot Grid Spotlight`: pontos de 1,5px a cada 28px (branco 10%). Num raio de 360px ao redor do cursor os pontos crescem até 3px e clareiam até azul quase branco, e uma luz direcional acompanha o cursor. Bordas esmaecem. Uso: CTA final, diagnóstico, Rumo AI.

### 8.5 Linhas de rota (assinatura)

O motivo visual próprio do site.

| Item | Valor |
|---|---|
| Linha | 1px, `ink-700` (rota inativa) ou fio ciano que esmaece (rota ativa) |
| Nó | 3px a 4px. Nó aceso: miolo quase branco + halo azul claro + halo ciano (seção 8.8), com anel fino a 35% no nó ativo. Nó apagado: `ink-600` |
| Comportamento | Desenha-se com o scroll (`stroke-dashoffset`), ligando etapas, números ou seções |
| Usos | Linha do tempo (1997 até hoje), "como trabalhamos", integração de sistemas, Non-Invasive Deployment, conexão entre serviços |
| Limite | Uma rota por seção |

### 8.6 Camada HUD

Aprovada nas capas pessoais HUD. Sempre 3º nível.

| Elemento | Especificação |
|---|---|
| Cantoneiras | 12px × 12px, traço 1px, branco a 20%, nos cantos do visual protagonista |
| Régua | Ticks de 1px a cada 8px, um maior a cada 64px, branco a 12% |
| Cruz de registro | 9px × 9px, traço 1px, branco a 20% |
| Rótulos técnicos | `mono-micro`, branco a 30% a 38% (ex.: `RUMO.SOLUÇÕES`, `// DESDE 1997`, `01 / 06`, coordenadas reais da sede) |
| Destaque | No máximo um rótulo em ciano por seção |

Rótulos HUD só trazem informação verdadeira. Nada de dados técnicos inventados como "decoração" (nada de `UPTIME 99.99%` se não for dado real).

### 8.7 Fade radial

Máscara radial que dissolve bordas de foto, vídeo, 3D ou mockup no fundo. Padrão para toda mídia em seção escura que não está dentro de um card.

### 8.8 Luz direcional (substitui o "glow ambiente") [v0.3]

Luz não é um círculo ciano com desfoque gaussiano: isso parece uma mancha, não luz (reprovado). Luz nasce de uma **fonte** e cai em gradiente de várias paradas, sempre na mesma direção.

**Anatomia (de cima para baixo):**

| Camada | Cor | Papel |
|---|---|---|
| 1 · Fonte | `light-core` #F2FBFF, 80% a 95% | Fio fino onde a luz bate: borda de topo, aresta, horizonte |
| 2 · Núcleo | `light-near` #7FD8F5 (e `light-ice` #BFEFFF junto à fonte) | Faixa curta e intensa logo abaixo da fonte |
| 3 · Corpo | `rumo-500` #00ACE5, 10% a 25% | A massa de luz que desce |
| 4 · Queda | `light-fall` #005A78 → transparente | Queda longa e não linear |

Regras:

- Camadas sobrepostas em `mix-blend-mode: screen` (ou `plus-lighter`), nunca uma mancha só.
- Direção única no site: do **topo** (cards, painéis, barra de pergunta, seções).
- Grão por cima, para o degradê não formar faixas.
- Proibido: elipse ciano desfocada como efeito principal, luz pulsando, luz sobre logo, símbolo, ícone ou texto.

**Três aplicações (componentes no Figma):**

| Aplicação | Componente | Onde |
|---|---|---|
| Borda de topo | `Light/Top Edge` (Default, Strong) | Card luminoso, card de produto (na cor accent), painel do diagnóstico, card da narrativa sticky, célula maior do bento. Strong = hover |
| Aro (sem uso desde v0.4) | `Light/Rim` | Mantido só como referência da anatomia em aro |
| Controle aceso | Efeitos em camadas | Barra de pergunta, chip ativo, botão primário em hover: borda clara no topo que vira ciano embaixo, realce branco interno de 1px, halo azul claro curto + halo ciano longo |

Nós de rota acesos: miolo quase branco + halo azul claro (5px) + halo ciano (16px), com um anel fino a 35% em vez do círculo ciano chapado.

**Receita CSS da borda de topo:**

```css
.light-top {
  position: absolute; inset: 0 0 auto 0; height: 260px;
  pointer-events: none; mix-blend-mode: screen;
  background:
    linear-gradient(90deg, transparent 4%, rgb(127 216 245 / .4) 25%,
      rgb(242 251 255 / .85) 50%, rgb(127 216 245 / .4) 75%, transparent 96%)
      top / 100% 1px no-repeat,                                  /* 1 · fonte */
    radial-gradient(55% 90% at 50% 0%,
      rgb(191 239 255 / .36) 0%, rgb(127 216 245 / .26) 15%,     /* 2 · núcleo */
      rgb(0 172 229 / .14) 40%,                                  /* 3 · corpo */
      rgb(0 90 120 / .05) 70%, transparent 100%);                /* 4 · queda */
}
```

No site, a borda de topo do card acompanha o cursor no eixo x.

**Spotlight do cursor [v0.5]:** além da luz de topo, todo container interativo (cards de serviço, diferenciais, avaliações, painel do diagnóstico) tem um spotlight que acompanha o cursor por onde ele for, em x e y. São duas camadas, as duas em Screen e com a mesma anatomia de luz:

| Camada | Especificação |
|---|---|
| Spotlight interno | Radial de 440px centrado no cursor: azul quase branco 16% → azul claro 10% (20%) → ciano 5% (42%) → `light-fall` 2% (58%) → transparente (70%) |
| Borda acesa no cursor | Radial de 280px no cursor aplicado só na borda de 1px (máscara): branco-azulado 80% → azul claro 38% → ciano 12% → transparente |
| Movimento | Posição com lerp 0,18 por quadro (segue sem atraso perceptível); aparece e some em `dur-base` |
| Limite | Só desktop (`hover: hover`); nunca em botões, inputs ou listas |

```css
.card .spot { position: absolute; inset: 0; pointer-events: none; mix-blend-mode: screen; opacity: 0;
  background: radial-gradient(440px circle at var(--mx) var(--my),
    rgb(191 239 255 / .16), rgb(127 216 245 / .10) 20%, rgb(0 172 229 / .05) 42%,
    rgb(0 90 120 / .02) 58%, transparent 70%); }
.card:hover .spot { opacity: 1; }
```

### 8.9 Borda acesa (cards)

| Item | Valor |
|---|---|
| Borda | Degradê vertical: azul quase branco no topo (22%; 55% no hover) → azul claro → branco a 7% → 5% embaixo |
| Hover | `Light/Top Edge` passa de Default para Strong, a borda clareia, elevação nível 3 |
| Cursor [v0.5] | Luz de topo segue o x; spotlight interno e borda acesa seguem x e y do cursor (seção 8.8). Só desktop (`@media (hover: hover)`) |
| Limite | Não usar em botões, inputs ou listas |

### 8.10 Ritmo entre seções [v0.5]

O site não troca de superfície: tudo acontece no preto infinito. O painel claro que subia sobre a seção escura foi retirado na v0.5 (decisão do usuário: "distorceu muito a identidade visual").

| Recurso | Especificação |
|---|---|
| Espaço | `section-y` (160px) entre seções |
| Fio | Linha de 1px, branco 8%, que esmaece nas pontas (`transparent → 8% → 8% → transparent`), na largura do conteúdo |
| Densidade | Alternar seções com efeito (mapa, dot grid, luz) e seções calmas (só textura) |

Não usar ondas, diagonais ou formas orgânicas entre seções.

### 8.11 Efeitos interativos padronizados [v0.4]

No Figma: página 05 · Imagem e efeitos, prancha "Efeitos interativos" (quadros de estado de cada efeito).

| # | Efeito | Quando | Parâmetros | Implementação | Movimento reduzido |
|---|---|---|---|---|---|
| 01 | Dot grid com spotlight | Fundos escuros (CTA final, diagnóstico, Rumo AI) | Raio 360px; pontos crescem e clareiam; luz segue o cursor | Canvas 2D ou CSS mask com `--x/--y` no `pointermove`, lerp 0,12 | Spotlight fixo no centro |
| 02 | Spotlight que segue o cursor [v0.5] | Todo container interativo, barra de pergunta | Luz de topo segue o x; spotlight de 440px e borda acesa seguem x e y (seção 8.8) | `pointermove` → CSS vars `--x`, `--mx`, `--my` com lerp (ou Motion `useSpring` 300/40) | Sem spotlight; hover troca a luz de topo para Strong |
| 03 | Borda luminosa que percorre | Um destaque por página | Segmento branco → azul claro → ciano percorre a borda em 6s | `conic-gradient` + `@property --angle` + mask | Borda acesa estática |
| 04 | Spotlight de seção | Heros internos, seções de destaque | Cone de luz do topo, desloca até 120px na direção do cursor | Radial elíptico + `useSpring` | Cone centralizado |
| 05 | Rede de partículas | Hero da Home, Rumo AI | Flutuação 6 a 14px, pulso das rotas a cada 4s, atração em 140px, cartão no hover | Canvas 2D próprio (DPR máx. 1,5, pausa fora da tela) | Quadro estático |
| 06 | Mockup de dashboard | Sustentação, IA, produtos | Dados ilustrativos sinalizados; linhas com stagger 60ms; gráfico desenha em 1,2s | React (Recharts/visx) ou SVG + Motion | Estático completo |
| 07 | Ícones animados (Lottie) | Confirmações, etapas, estados vazios | Traço 1,5px, até 1,2s, toca uma vez | `@lottiefiles/dotlottie-react` a partir dos ícones Lucide | Último quadro |
| 08 | Estados com Framer Motion | Botões, cards, menus, abas, modais | Hover 200ms; layout 400ms ease-out; presence com y 8px; spring sem overshoot | `motion/react`: `whileHover`, `layout`, `AnimatePresence` | Só cor e opacidade |
| 09 | Revelação ao rolar | Toda entrada de bloco | 15% visível, uma vez; y 24 → 0 em 750ms; stagger 60ms | `whileInView` + `viewport {once:true, amount:.15}` | Fade de 200ms |
| 10 | Texto letra por letra | Manifesto e números protagonistas | Opacidade + blur 6px + y 8px por letra, 28ms entre letras, máx. 1,2s | Split por caractere + `staggerChildren`; `aria-label` com o texto | Fade único |
| 11 | Digitação (typewriter) | Barra de pergunta, terminal, replay | 40ms/caractere, cursor 1,1s, pausa 1,8s, apaga a 20ms | Hook `useTypewriter` + `useReducedMotion` | Primeira sugestão fixa |
| 12 | Parallax de profundidade | Hero e seções em camadas | Grade 0,1 · mapa 0,25 · luz 0,4 · conteúdo 1,0; máx. 80px | `useScroll` + `useTransform`; Lenis (lerp 0,1) | Camadas fixas |

Regras de convivência: no máximo dois efeitos ambientes por viewport (o grão não conta); efeitos nunca atrás de texto sem véu de legibilidade; todo efeito pausa fora da tela.

### 8.12 Legibilidade sobre fundos [v0.4]

- Todo texto sobre fundo com efeito (mapa, dot grid, foto) fica sobre um **véu**: radial `#07080A` de 90% a 95% no centro, esmaecendo até 0.
- HUD nos cantos ganha véu próprio.
- Linhas, nós e rótulos do fundo nunca cruzam títulos ou parágrafos: a zona calma do mapa e o véu garantem isso.
- Contraste AA conferido com o fundo **mais claro** que pode passar atrás do texto.

---

## 9. Movimento

Nível escolhido: **rico e imersivo**, com a precisão do manual (sem bounce, sem frenesi). O movimento é o principal tradutor de "velocidade de startup".

### 9.1 Tokens de duração [EVOLUÇÃO: amplia a faixa 0.4s a 0.75s do manual]

| Token | Valor | Uso |
|---|---|---|
| `dur-instant` | 100ms | Pressionar botão |
| `dur-fast` | 200ms | Hover de cor, borda, ícone |
| `dur-base` | 400ms | Abrir acordeão, trocar aba, menus |
| `dur-slow` | 750ms | Revelações de conteúdo |
| `dur-cinematic` | 1200ms | Hero, transição de página, revelação de display |
| `dur-ambient` | 40s a 90s | Loops (flutuação do mapa de rede, marquee) |

### 9.2 Curvas

| Token | Valor | Uso |
|---|---|---|
| `ease-out` | `cubic-bezier(.16,1,.3,1)` | **Padrão** (manual 7). Entradas e revelações |
| `ease-in-out` | `cubic-bezier(.65,0,.35,1)` | Troca de estado, transição de página |
| `ease-in` | `cubic-bezier(.7,0,.84,0)` | Somente saídas |
| `linear` | `linear` | Loops ambientes |

Molas (spring) só sem overshoot (amortecimento crítico), por exemplo em elementos que seguem o mouse.

### 9.3 Coreografia

| Parâmetro | Valor |
|---|---|
| Deslocamento de entrada | 24px (elementos pequenos) · 48px (blocos). Nunca mais de 64px |
| Stagger entre itens | 60ms |
| Stagger entre linhas de título | 80ms |
| Tempo total máximo de uma sequência | 1200ms |
| Gatilho | Quando 15% do elemento entra na tela. Uma vez só (não reanimar ao voltar) |
| Ordem | Sempre a ordem de leitura: label → título → lead → ação → visual |

### 9.4 Catálogo de padrões

| Código | Padrão | Especificação |
|---|---|---|
| **M01** | Entrada de bloco | Opacidade 0 → 1 + `translateY(24px)` → 0, `dur-slow`, `ease-out` |
| **M02** | Título por linha | Cada linha em máscara (`overflow: hidden`), sobe de 100% → 0, 900ms, stagger 80ms (a sequência inteira cabe em 1200ms) |
| **M03** | Manifesto que acende | Parágrafo do manifesto começa em `fg-unlit` (22%) e cada palavra vai a `fg` ligada ao scroll (começa com a seção a 80% da tela, termina a 30%). Uma palavra-chave termina em `brand-text`. Movimento reduzido: texto já aceso |
| **M04** | Contador | Número sobe de 0 ao valor real em 1600ms, `ease-out`, números tabulares. Só números de `knowledge/rumo.md` |
| **M05** | Rota desenhada | Linha de rota ligada ao scroll (`stroke-dashoffset`); nós acendem quando a linha passa por eles |
| **M06** | Narrativa sticky | Seção travada; o texto da esquerda troca por etapa e o visual da direita se transforma. Índice `01 / 05` em `mono-micro` |
| **M07** | Parallax leve | Camadas de fundo (grade, mapa de rede, luz) a 0.1 a 0.4 da velocidade do scroll. Nunca em texto |
| **M08** | Hero vivo | Mapa de rede em canvas: nós flutuam, rotas pulsam, o mouse atrai nós num raio de 140px e o hover no hub abre um cartão (seção 8.11, efeito 05) |
| **M09** | Marquee | Logos (stack ou clientes autorizados) em loop de 40s a 60s, pausa no hover, logos em `ink-500` que vão para branco no hover, bordas esmaecidas por máscara |
| **M10** | Hover de card | Spotlight e borda acesa seguindo o cursor (seção 8.8) + `translateY(-2px)` + mídia com escala 1.03 em `dur-slow` |
| **M11** | Botão | Cor em `dur-fast`; seta desliza 4px; primário acende: realce branco interno de 1px no topo + halo azul claro curto + halo ciano longo (estilo Glow/Brand) |
| **M12** | Transição de página | Cortina `#050505` sobe em 600ms (`ease-in-out`) e o conteúdo novo entra com M01. Implementar com View Transitions API quando disponível |
| **M13** | Scroll suave | Lenis com `lerp: 0.1`; desligado em toque e em movimento reduzido |
| **M14** | Menu mobile | Overlay em tela cheia; links em `h3` entram com stagger de 60ms |
| **M15** | Abas e indicadores | Indicador de 2px desliza entre abas (layout animation), `dur-base` |
| **M16** | Digitação da barra de pergunta | Placeholder digita a 40ms por caractere, pausa 1,8s, apaga a 20ms por caractere e passa para a próxima sugestão. Para quando o campo recebe foco |
| **M17** | Luz do card luminoso | A luz de topo passa de Default a Strong, a borda clareia no topo e o card ganha elevação, em `dur-base`. O centro da luz segue o cursor no eixo x |
| **M18** | Cadeia de números | Pílulas entram com stagger de 60ms; as setas entre elas desenham da esquerda para a direita |

### 9.5 Proibido

- bounce, elástico, shake, wobble;
- rotação de elementos de texto;
- loops chamativos perto de texto de leitura;
- animar tudo ao mesmo tempo na mesma dobra;
- scroll sequestrado que impede o usuário de sair da seção (sticky sim, travamento não);
- cursor customizado no site inteiro (permitido só um rótulo contextual sobre mídias, como "Ver case", em desktop).

### 9.6 Movimento reduzido

Com `prefers-reduced-motion: reduce`:

- sem scroll suave, parallax, animação do mapa de rede ou marquee;
- revelações viram fade de opacidade em 200ms;
- contadores mostram direto o valor final;
- hero 3D mostra um quadro estático;
- narrativa sticky vira lista de etapas normal.

### 9.7 Stack de movimento

| Necessidade | Ferramenta |
|---|---|
| Animações de componente e layout | Motion (`motion/react`, antigo Framer Motion) |
| Scroll suave | Lenis |
| Narrativas ligadas ao scroll complexas | Motion `useScroll`; GSAP ScrollTrigger só se o caso exigir |
| 3D em tempo real | React Three Fiber + drei |
| Transições de página | View Transitions API (Next.js) com fallback em Motion |

---

## 10. Componentes

Todo componente tem os estados: padrão, hover, foco visível, pressionado e desabilitado (quando aplicável). Desde a v0.5 o site usa só a superfície escura; as versões claras ficam para interfaces de produto que já são claras.

**Foco visível (todos os interativos):** `outline: 2px solid var(--focus-ring)`, `outline-offset: 2px`. Nunca remover o foco.

### 10.1 Botão

| Tamanho | Altura | Padding horizontal | Texto | Ícone |
|---|---|---|---|---|
| `sm` | 36px | 14px | 14px / 500 | 16px |
| `md` | 44px | 20px | 15px / 500 | 16px |
| `lg` | 52px | 24px | 16px / 500 | 20px |

Raio `radius-md`. Ícone à direita (seta), gap de 8px.

| Variante | Padrão | Hover | Pressionado | Desabilitado |
|---|---|---|---|---|
| **Primário** | fundo `brand`, texto `on-brand` | fundo `brand-hover` + controle aceso (Glow/Brand, seção 8.8) | fundo `brand-pressed` | fundo `ink-750`, texto `ink-500` |
| **Secundário** | transparente, borda branco 16%, texto `fg` | borda branco 32%, fundo branco 4% | fundo branco 8% | borda `ink-750`, texto `ink-600` |
| **Link** | texto `brand-text` + seta | seta +4px | `brand-pressed` | `fg-subtle` |
| **Ícone** | 40px × 40px, borda `border` | borda `border-strong` | fundo `surface` | opacidade 40% |

No claro: primário igual; secundário com borda `ice-300` e texto `ice-900`.

Regras: um CTA primário por seção (manual 4.5); botão primário nunca ocupa largura total em desktop; rótulos de verbo + objeto ("Agendar diagnóstico").

### 10.2 Link em texto

- Em parágrafo: `fg` ou `brand-text`, **sublinhado** de 1px com `text-underline-offset: 3px` a 40% de opacidade, que vai a 100% no hover [EVOLUÇÃO: o manual pede links sem sublinhado; em texto corrido, a acessibilidade exige uma pista além da cor].
- Fora de parágrafo (navegação, cards, "ver todos"): sem sublinhado, com seta.

### 10.3 Label (eyebrow) e tags

| Componente | Especificação |
|---|---|
| **Label de seção** | `label`, `brand-text`, opcionalmente precedido de um nó de 4px ou de `//` em `mono-micro` |
| **Tag de categoria** | Pill de 28px de altura, padding 12px, `label` sem caixa alta e em 13px, borda `border`, texto `fg-muted` |
| **Tag ativa (filtro)** | Borda `rumo-a28`, fundo `rumo-a08`, texto `fg` |
| **Tag no claro** | Fundo `ice-100`, borda `ice-300`, texto `rumo-700` |
| **Status** | Ponto de 6px em `success` + texto `small`. Só para status real |

### 10.4 Campos de formulário

| Item | Escuro | Claro |
|---|---|---|
| Altura | 48px (textarea a partir de 120px) | 48px |
| Fundo | `ink-850` | `ice-0` |
| Borda | `ink-750` → hover `ink-700` | `ice-200` → hover `ice-300` |
| Foco | borda `rumo-500` + anel de 3px `rumo-a16` | borda `rumo-700` + anel `rumo-a16` |
| Texto | 16px, `fg` | 16px, `ice-900` |
| Placeholder | `ink-500` | `ice-500` |
| Label | Acima do campo, 14px / 500, `fg-muted` | `ice-700` |
| Erro | Borda `error` + mensagem 13px em `error` com ícone `AlertCircle` | idem com `error-on-light` |
| Raio | `radius-md` | `radius-md` |

Formulário principal: **Diagnóstico Técnico Gratuito** (nome, e-mail corporativo, empresa, cargo, desafio principal). Sucesso com status verde + mensagem humana.

### 10.5 Navegação

| Item | Especificação |
|---|---|
| Altura | 72px (desktop) · 64px (mobile) |
| Estado inicial | Transparente sobre o hero |
| Depois de 24px de scroll | Vidro escuro (seção 5.5) |
| Ao rolar para baixo | Esconde; reaparece ao rolar para cima |
| Logo | Canto superior esquerdo (manual 11.5), altura de 28px a 32px (mínimo 24px) |
| Links | 15px / 500, `fg-muted` → `fg` no hover; ativo com nó ciano de 4px abaixo |
| Direita | Link "Rumo AI ↗" (opcional) + botão primário `sm` "Diagnóstico gratuito" |
| Mega menu | Serviços e Produtos. Painel nível 3, colunas com ícone 20px + título + uma linha de descrição; à direita, um card de destaque (case ou produto) |
| Mobile | Overlay em tela cheia `ink-950`, links em `h3`, CTA fixo no rodapé do menu |

### 10.6 Cards

| Card | Anatomia | Notas |
|---|---|---|
| **Luminoso** (grades de serviço) | Mini-interface ilustrativa no topo (zona de altura fixa) → número mono `01` em ciano → título → descrição → CTA | Luz de borda de topo (`Light/Top Edge`, seção 8.8), Strong no hover, spotlight no cursor. Ver 10.8 |
| **Serviço** (listas simples) | Ícone 24px (esquerda) → `h4` → `small` em `fg-muted` → link com seta | `surface`, borda, `radius-lg`, padding 32px, spotlight |
| **Diferencial** [v0.5] | Disco 48px com aro ciano 32% e ícone em `light-near` → título `h4` → descrição | Card escuro com borda acesa, luz de topo e spotlight no cursor. Substitui o container tonal claro |
| **Bento (serviços na home)** | Células de tamanhos diferentes; a maior tem visual próprio (rota, mockup ou foto) | Nunca células iguais com ícone centralizado. [v0.5] Todo card tem CTA (verbo + objeto: "Conhecer a Sustentação 24/7"), sempre no pé do card; cards da mesma linha têm a zona de visual com a mesma altura (200px), para títulos, descrições e CTAs ficarem alinhados |
| **Case** | Mídia 16:10 com tratamento dark → logo do cliente (real, autorizado) → tag de setor → métrica em `h3` + rótulo → título | Hover: mídia 1.03, rótulo de cursor "Ver case" |
| **Produto** | Logo do produto → `h4` → descrição → mockup real → link "Conhecer ↗" | Luz de topo na cor `accent` (máscara alfa em Screen) + fio branco |
| **Artigo** | Imagem 16:9 → tag → `h4` → `caption` com data e tempo de leitura | Seção escura; título vai para `light-near` no hover |
| **Stat** | `stat` em `fg` + unidade em `fg-muted` → `small` com o rótulo | Separadores verticais de 1px entre stats |
| **Depoimento** | Citação em `lead` peso 300 → nome, cargo, empresa, logo | Somente depoimentos reais, com autorização |
| **Avaliação do Google** [v0.5] | Estrelas (nota real) → trecho da avaliação → avatar com iniciais, nome, cargo ou empresa e mês/ano | Card escuro com spotlight. Só avaliações reais do perfil da empresa, texto exato, com autorização. Enquanto não houver, o card mostra "Aguardando avaliação" |
| **Pergunta frequente** [v0.5] | Pergunta em 19px peso 500 → botão circular de 34px com "+" que gira 45° → resposta em `body` `fg-muted` | Acordeão com uma pergunta aberta por vez, fio de 1px entre itens, primeira aberta. Abre em `dur-base` |

### 10.7 Demais componentes

| Componente | Especificação |
|---|---|
| **Acordeão (FAQ)** | Linhas com borda inferior `border`; título 18px / 500; ícone `Plus` que gira 45°; conteúdo em `fg-muted`; altura anima em `dur-base` |
| **Abas** | Texto 15px / 500; indicador de 2px em `brand` deslizando (M15) |
| **Linha do tempo** | Rota horizontal (desktop) ou vertical (mobile) com nós; ano em `mono-micro` + título `h4` + texto curto. Começa em 1997 |
| **Logo wall** | Logos monocromáticos `ink-500`, altura óptica igual (24px a 32px), em grid ou marquee (M09) |
| **Faixa de selos** | ISO 9001 e GPTW (arquivos oficiais), pequenos, direto no fundo, sem caixa ou tarja |
| **Breadcrumb** | `caption`, separador `/` em `fg-subtle`, item atual em `fg` |
| **Paginação** | Botões ícone + números `small`; atual com borda `rumo-a28` |
| **Tooltip** | Fundo `ink-800`, borda `ink-700`, `caption`, `radius-sm` |
| **Toast** | Nível 3, ícone de status + mensagem; some em 5s |
| **Rodapé** | Fundo `ink-925`; logo; colunas de links (`small`); selos ISO + GPTW; endereço da sede; redes sociais (ícones 20px); barra final em `caption` com CNPJ e ano |
| **Link de pular** | "Pular para o conteúdo", visível no foco |

### 10.8 Padrões aprovados no benchmark (v0.2)

Seis propostas aprovadas em 2026-10-22 depois da análise de quatro referências (Lumora, Verity, Signal e Optivio). No Figma: página 07 · Componentes, prancha "Novos padrões".

| # | Padrão | Origem | Especificação na Rumo |
|---|---|---|---|
| 01 | **Título em dois tons** | Lumora, Signal | 1ª frase `fg`, 2ª `heading-secondary`. Sem ciano no título (seção 3.4) |
| 02 | **Manifesto que acende** | Signal, Lumora | H2 52px, até 45 palavras, de `fg-unlit` a `fg` com o scroll (M03), uma palavra-chave em `brand-text`. Um por página, logo depois do hero |
| 07 | **Container de diferencial** [v0.5] | Optivio | Antes tonal azul-gelo em seção clara; desde a v0.5 é card escuro com borda acesa, spotlight e ícone em disco com aro ciano |
| 13 | **Card luminoso** | Lumora, Verity | `Card/Luminous`: luz de borda de topo com fonte quase branca (seção 8.8), mini-interface ilustrativa (`MiniUI/Squad`, `Code`, `Tickets`, `Ask`, `Shield`), número mono + título + descrição. Hover M17 |
| 14 | **Barra de pergunta** | Lumora | `Ask Bar`, 640 × 64, vidro (blur 12) + controle aceso (seção 8.8): borda clara no topo que vira ciano embaixo, fio branco no centro do topo, realce interno e halos azul claro e ciano. Placeholder "Do que sua operação precisa?" digita sugestões (M16). Enviar leva a `/diagnostico-gratuito` com o desafio preenchido. É a ação principal do hero, com chips de sugestão e link para o diagnóstico abaixo |
| 21 | **Cadeia de números** | Signal | `Proof Chain`: 4 `Proof Pill` com setas entre elas, uma em destaque (ciano): +70.000 demandas entregues → < 2% de taxa de erro → 24/7 sustentação crítica → 1 parceiro de continuidade. Entrada M18 |

Regras comuns:

- Mini-interfaces e filas de chamados são **ilustrativas**: status genéricos, nenhum número inventado.
- A cadeia só usa fatos de `knowledge/rumo.md`.
- A luz do card luminoso segue a anatomia da seção 8.8 (fonte, núcleo, corpo, queda). Continua proibido brilho em logo, símbolo, ícone ou texto.
- Ao trocar o ícone de um `Card/Tonal` no Figma, reaplique `brand` no traço (a troca volta o ícone para `fg-muted`).

---

## 11. Biblioteca de seções

Seções reutilizáveis para montar as páginas. Cada uma tem um protagonista.

| Código | Seção | Protagonista | Superfície | Efeitos permitidos |
|---|---|---|---|---|
| **S01** | Hero | Display centralizado + barra de pergunta | Escura | Mapa de rede vivo, véu central, HUD (relógio, metadados, contador) |
| **S02** | Hero de página interna | `h1` + visual | Escura | Dot grid ou foto com fade |
| **S03** | Manifesto e prova | Manifesto que acende + cadeia de números | Escura | M03, M18 |
| **S03b** | Faixa de prova (alternativa) | Stats reais + selos | Escura | Contadores (M04) |
| **S04** | Serviços em bento | O grid | Escura | Spotlight |
| **S05** | Narrativa sticky | Etapas | Escura | Rota (M05), índice mono |
| **S06** | Destaque Rumo AI | Título + demonstração | Escura | Luz direcional, dot grid |
| **S07** | Produtos | Cards de produto | Escura | Acento por card |
| **S08** | Cases | Carrossel ou grid de cases | Escura ou clara | Hover de card |
| **S09** | Pessoas e cultura | Fotografia real | Escura | Fade radial |
| **S10** | Diferenciais | Quatro cards de diferencial | Escura [v0.5] | Spotlight nos cards |
| **S10b** | Faixa de tecnologias [v0.5] | Logos da stack (`knowledge/rumo.md`, seção 5.1) em marquee | Escura | M09. Na Home, logo abaixo do hero |
| **S11** | Diagnóstico gratuito | Oferta + CTA | Escura | Luz de topo no painel, HUD |
| **S12** | Conteúdo (blog) | Cards de artigo | Escura [v0.5] | Hover de card |
| **S13** | Perguntas frequentes [v0.5] | Acordeão à direita; título, lead e link para especialista fixos à esquerda | Escura | Nenhum. Respostas só com fatos de `knowledge/rumo.md` |
| **S14** | CTA final | `h1` + um CTA | Escura | Dot grid com spotlight + luz de topo |
| **S15** | Linha do tempo | Rota 1997 → hoje | Escura | M05 |
| **S16** | Corpo de leitura | Texto 720px | Escura [v0.5] | Nenhum |
| **S17** | Avaliações do Google [v0.5] | Resumo do perfil (nota e total reais) + três cards de avaliação | Escura | Spotlight nos cards |

---

## 12. Arquitetura do site e templates de página

### 12.1 Mapa do site (proposta)

```
/                               Home
/servicos                       Hub de serviços
  /outsourcing-de-ti            Outsourcing de TI (carro-chefe)
  /fabrica-de-software          Fábrica de Software e Desenvolvimento Sob Medida
  /sustentacao                  Sustentação de Sistemas e Infraestrutura Crítica
  /inteligencia-artificial      IA Enterprise (Rumo AI) + link para rumoai.io
  /ciberseguranca               Cibersegurança e Compliance
/diagnostico-gratuito           Landing de conversão (CTA global)
/produtos                       Hub de produtos
  /pricefleet                   → página resumo + link pricefleet.com.br
  /sofi
  /genial
  /sgae
  /startvet
/cases                          Hub de cases (filtro por setor)
  /[case]                       Case
/sobre                          História, missão, cultura, ISO, GPTW
/carreiras                      Rumo Academy, cultura, vagas
/blog                           Hub de artigos
  /[artigo]                     Artigo
/contato                        Contato
```

### 12.2 Home

| # | Seção | Conteúdo (a definir na etapa de copy) |
|---|---|---|
| 1 | S01 Hero manifesto | Título em dois tons + lead + barra de pergunta (ação principal) + chips de sugestão + link "agende um diagnóstico gratuito". Composição centralizada sobre o mapa de rede, com HUD nos cantos |
| 2 | S10b Faixa de tecnologias [v0.5] | Logos da stack em marquee |
| 3 | S03 Manifesto e prova | Manifesto que acende + cadeia de números |
| 4 | S04 Serviços em bento | Outsourcing na célula maior; demais serviços em cards luminosos; CTA em todos |
| 5 | S05 Narrativa sticky | Como a Rumo trabalha: diagnóstico → seleção técnica → operação → corresponsabilidade → evolução |
| 6 | S10 Diferenciais | Quatro cards de diferencial no escuro |
| 7 | S17 Avaliações do Google [v0.5] | Avaliações reais do perfil (pendente, P9) |
| 8 | S12 Conteúdo | Últimos artigos |
| 9 | S13 Perguntas frequentes [v0.5] | Sete perguntas com respostas da base institucional |
| 10 | S11 Diagnóstico gratuito | Formulário de conversão |
| 11 | S14 CTA final | Diagnóstico gratuito |
| Fase 2 | S06 Rumo AI · S07 Produtos · S08 Cases · S09 Pessoas | Entram quando houver assets, cases autorizados e fotos reais |

### 12.3 Página de serviço

S02 hero (label do serviço, `h1`, lead, CTA diagnóstico) → dor da persona → S05 como funciona → modelos de contratação (ex.: Time & Materials e Escopo Fechado no Outsourcing) → S10 stack → S08 case relacionado → S13 FAQ → S14 CTA final.

### 12.4 Página de produto

`data-produto` ativo. S02 hero com luz de topo no `accent` + mockup real → bento de recursos reais → integrações (ex.: FIPE, DataCar, Locavia, BlueFleet no PriceFleet) → case → CTA "Conhecer o [produto] ↗" para o site do produto, quando existir.

### 12.5 Case

Hero escuro (cliente, setor, até três métricas reais) → S16 corpo no escuro: contexto, desafio, solução, resultado → próximo case → S14.

### 12.6 Artigo do blog

Cabeçalho escuro curto (tag, `h1`, data, tempo de leitura) → corpo no escuro, coluna de 720px, `body-article`, índice lateral sticky em desktop → artigos relacionados → CTA. Os artigos vêm do projeto `Artigos Linkedin - BLOG/`.

### 12.7 Sobre

S02 → S15 linha do tempo desde 1997 → missão, visão e valores → S09 cultura → ISO 9001 e GPTW → liderança (somente fotos reais) → S14.

### 12.8 Carreiras

S02 com foto real → cultura, DNA remoto e híbrido → Rumo Academy → GPTW → lista de vagas (cards simples com tag de modelo de trabalho) → S14 "Ver vagas".

---

## 13. Logotipo e selos no site

| Item | Regra |
|---|---|
| Arquivo | Somente arquivos oficiais de `Designer Gráfico/assets/logos/`. Exportar para o site como SVG otimizado, sem redesenhar |
| Versão no header (escuro) | Horizontal completa, versão principal (ciano + branco) ou branca |
| Versão em seção clara | Horizontal colorida |
| Altura | 28px a 32px no header desktop, mínimo 24px (manual 11.4) |
| Respiro | Altura do "R" em todos os lados (manual 11.3) |
| Favicon | Símbolo oficial (`SIMBOLO DO LOGO rumo.svg`) em 32px, 180px (Apple) e SVG |
| Proibido | Glow, contorno, sombra, gradiente, animação que deforme o logo, símbolo gigante solto como decoração |
| Selos | ISO 9001 e GPTW pequenos, juntos, direto no fundo, sem caixa escura; preferencialmente no rodapé e na faixa de prova |

**[PENDENTE] Cor do logo:** os SVGs oficiais em `assets/logos/` usam `#05AAE2` (azul da identidade antiga), enquanto o manual define `#00ACE5`. A diferença é quase imperceptível, mas precisa de decisão: reexportar os arquivos oficiais com `#00ACE5` ou confirmar o `#05AAE2` como cor do logo. Até lá, o logo é usado exatamente como está no arquivo.

---

## 14. Conteúdo e microcopy

- **Tom:** consultivo, humano, sem "tecniquês" excessivo (`knowledge/rumo.md` 14.2). A copy do site é uma etapa à parte e segue a skill `copy-social-media` adaptada para web ou um briefing próprio.
- **CTA primário global:** "Agendar diagnóstico gratuito". Secundários: "Ver cases", "Conhecer serviços", "Falar com um especialista".
- **Evitar** "Saiba mais" e "Clique aqui". O rótulo diz o que acontece.
- **Números:** só os de `knowledge/rumo.md` seção 1.2, conferidos com a seção 16.3 antes de publicar. Para tempo de mercado, preferir **"desde 1997"**, que não vence (em 2026 já são 29 anos, e a base ainda diz "+28 anos").
- **Clientes e cases:** só com autorização para uso de nome e logo.
- **Travessão longo:** proibido em todo texto do site, inclusive `alt`, metadados e mensagens de erro.
- **Mensagens de sistema:** humanas e curtas ("Recebemos seu pedido. Um especialista responde em até 1 dia útil." somente se o prazo for real).

---

## 15. Acessibilidade e performance

### 15.1 Acessibilidade (WCAG 2.2 AA)

- Contraste AA em todo texto (tabela 2.4); 3:1 em bordas de componentes que precisam ser percebidas.
- Foco visível em todos os interativos; ordem de tabulação lógica; mega menu operável por teclado (Esc fecha).
- Áreas de toque de pelo menos 44px × 44px.
- `lang="pt-BR"`; um `h1` por página; títulos em ordem.
- Canvas 3D com `aria-hidden="true"` e o conteúdo equivalente em texto.
- Status e erro nunca só por cor (cor + ícone + texto, manual 5).
- Movimento reduzido respeitado (seção 9.6).
- `alt` descritivo em fotos reais; vazio em imagens decorativas.

### 15.2 Orçamento de performance

| Métrica | Meta |
|---|---|
| LCP | < 2,5s (4G) |
| CLS | < 0,1 |
| INP | < 200ms |
| Fontes pré-carregadas | 1 arquivo (Geist Variable) |
| Vídeo de fundo | ≤ 3MB, `webm`/`mp4`, mudo, com pôster |

Regras para o 3D:

- carregar o canvas **depois** do LCP (o título do hero é o LCP, nunca o canvas);
- `dpr` máximo de 1.5; pausar a renderização fora da tela;
- em mobile ou aparelho fraco, trocar o tempo real por vídeo ou imagem estática;
- imagens em AVIF ou WebP com `next/image`.

---

## 16. Tokens (CSS + Tailwind v4)

Arquivo sugerido: `app/globals.css`.

```css
@import "tailwindcss";

/* ============ 1. PRIMITIVAS ============ */
@theme {
  /* Neutros escuros */
  --color-ink-950: #050505;
  --color-ink-925: #0B0B0B;
  --color-ink-900: #121212;
  --color-ink-850: #171717;
  --color-ink-800: #1E1E1E;
  --color-ink-750: #262626;
  --color-ink-700: #2E2E2E;
  --color-ink-600: #3D3D3D;
  --color-ink-500: #858585;
  --color-ink-400: #A1A1A1;
  --color-ink-0:   #FFFFFF;

  /* Ciano Rumo */
  --color-rumo-400: #33BDEA;
  --color-rumo-500: #00ACE5;
  --color-rumo-600: #0096C7;
  --color-rumo-700: #00759C;
  --color-rumo-800: #005A78;

  /* Neutros frios claros */
  --color-ice-0:   #FFFFFF;
  --color-ice-50:  #F2F8FB;
  --color-ice-100: #EAF7FC;
  --color-ice-150: #E4F4FA;
  --color-ice-200: #D8E5EB;
  --color-ice-300: #C6E8F4;
  --color-ice-500: #5B6B73;
  --color-ice-700: #24323A;
  --color-ice-900: #0A1419;

  /* Funcionais */
  --color-success-500: #13C71A;
  --color-success-700: #0B7A10;
  --color-error-400:   #F2555A;
  --color-error-700:   #C4262E;

  /* Tipografia */
  --font-sans: "Geist", "Inter", ui-sans-serif, system-ui, sans-serif;
  --font-mono: "Geist Mono", ui-monospace, monospace;

  --text-display: clamp(2.75rem, 5.6vw, 5rem);
  --text-display--line-height: 0.92;
  --text-display--letter-spacing: -0.04em;
  --text-display--font-weight: 500;

  --text-h1: clamp(2.5rem, 4.4vw, 4rem);
  --text-h1--line-height: 0.98;
  --text-h1--letter-spacing: -0.03em;
  --text-h1--font-weight: 500;

  --text-h2: clamp(2rem, 3.4vw, 3rem);
  --text-h2--line-height: 1.04;
  --text-h2--letter-spacing: -0.025em;
  --text-h2--font-weight: 500;

  --text-h3: clamp(1.375rem, 2vw, 1.75rem);
  --text-h3--line-height: 1.15;
  --text-h3--letter-spacing: -0.015em;
  --text-h3--font-weight: 500;

  --text-h4: 1.25rem;
  --text-h4--line-height: 1.25;
  --text-h4--letter-spacing: -0.01em;
  --text-h4--font-weight: 500;

  --text-stat: clamp(2.75rem, 5vw, 4.5rem);
  --text-stat--line-height: 1;
  --text-stat--letter-spacing: -0.04em;
  --text-stat--font-weight: 400;

  --text-lead: clamp(1.125rem, 1.4vw, 1.25rem);
  --text-lead--line-height: 1.5;
  --text-lead--letter-spacing: -0.005em;

  --text-body: clamp(1rem, 0.95rem + 0.2vw, 1.0625rem);
  --text-body--line-height: 1.6;

  --text-body-article: clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem);
  --text-body-article--line-height: 1.7;

  --text-small: 0.875rem;
  --text-small--line-height: 1.55;

  --text-caption: 0.8125rem;
  --text-caption--line-height: 1.5;
  --text-caption--letter-spacing: 0.01em;

  --text-label: 0.75rem;
  --text-label--line-height: 1;
  --text-label--letter-spacing: 0.12em;
  --text-label--font-weight: 500;

  --text-button: 0.9375rem;
  --text-button--line-height: 1;
  --text-button--font-weight: 500;

  --text-mono-micro: 0.6875rem;
  --text-mono-micro--line-height: 1;
  --text-mono-micro--letter-spacing: 0.08em;

  /* Breakpoint extra (container máximo do manual) */
  --breakpoint-3xl: 107.5rem; /* 1720px */

  /* Raios */
  --radius-xs: 4px;
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-panel: 24px;
  --radius-pill: 999px;

  /* Sombras (superfície clara) */
  --shadow-sm: 0 1px 2px rgba(10, 20, 25, .06);
  --shadow-md: 0 8px 24px -8px rgba(10, 20, 25, .12);
  --shadow-lg: 0 24px 48px -16px rgba(10, 20, 25, .18);
  /* Sombra de flutuação (superfície escura) */
  --shadow-float: 0 24px 48px -12px rgba(0, 0, 0, .6);

  /* Luz direcional (seção 8.8) */
  --color-light-core: #F2FBFF;
  --color-light-ice:  #BFEFFF;
  --color-light-near: #7FD8F5;
  --color-light-fall: #005A78;
  --shadow-lit: inset 0 1px 0 rgba(255,255,255,.35), 0 2px 8px -2px rgba(127,216,245,.4), 0 10px 28px -8px rgba(0,172,229,.3);

  /* Movimento */
  --ease-out: cubic-bezier(.16, 1, .3, 1);
  --ease-in-out: cubic-bezier(.65, 0, .35, 1);
  --ease-in: cubic-bezier(.7, 0, .84, 0);
}

/* ============ 2. SEMÂNTICAS ============ */
:root,
[data-surface="dark"] {
  --bg:             var(--color-ink-950);
  --bg-sunken:      var(--color-ink-925);
  --bg-glow-from:   var(--color-ink-900);
  --surface:        var(--color-ink-850);
  --surface-raised: var(--color-ink-800);
  --surface-tint:   rgba(0, 172, 229, .08);
  --border:         var(--color-ink-750);
  --border-strong:  var(--color-ink-700);
  --fg:             var(--color-ink-0);
  --fg-muted:       var(--color-ink-400);
  --fg-subtle:      var(--color-ink-500);

  --brand:          var(--color-rumo-500);
  --brand-hover:    var(--color-rumo-400);
  --brand-pressed:  var(--color-rumo-600);
  --brand-text:     var(--color-rumo-500);
  --on-brand:       var(--color-ink-950);
  --focus-ring:     var(--color-rumo-500);

  --heading-secondary: var(--color-ink-500);
  --fg-unlit:       rgba(255, 255, 255, .22);
  --surface-soft:   var(--color-ink-850);
  --surface-soft-alt: var(--color-ink-800);
  --disc:           var(--color-ink-800);

  --accent:         var(--brand);
  --accent-text:    var(--brand-text);
  --on-accent:      var(--on-brand);

  --success:        var(--color-success-500);
  --error:          var(--color-error-400);

  --grain-opacity:  .04;
  --grain-blend:    overlay;
}

[data-surface="light"] {
  --bg:             var(--color-ice-0);
  --bg-sunken:      var(--color-ice-50);
  --bg-glow-from:   var(--color-ice-0);
  --surface:        var(--color-ice-0);
  --surface-raised: var(--color-ice-0);
  --surface-tint:   var(--color-ice-100);
  --border:         var(--color-ice-200);
  --border-strong:  var(--color-ice-300);
  --fg:             var(--color-ice-900);
  --fg-muted:       var(--color-ice-700);
  --fg-subtle:      var(--color-ice-500);

  --brand-text:     var(--color-rumo-700);
  --brand-pressed:  var(--color-rumo-800);
  --focus-ring:     var(--color-rumo-700);
  --accent-text:    var(--brand-text);

  --success:        var(--color-success-700);
  --error:          var(--color-error-700);

  --heading-secondary: var(--color-ice-500);
  --fg-unlit:       rgba(10, 20, 25, .22);
  --surface-soft:   var(--color-ice-100);
  --surface-soft-alt: var(--color-ice-50);
  --disc:           var(--color-ice-900);

  --grain-opacity:  .025;
  --grain-blend:    soft-light;
}

/* ============ 3. ACENTO DE PRODUTO ============ */
[data-produto="pricefleet"] {
  --accent:      #009844;
  --accent-text: #009844;
  --on-accent:   #050505;
}
[data-produto="pricefleet"] [data-surface="light"],
[data-produto="pricefleet"][data-surface="light"] {
  --accent-text: #007A37;
}

/* ============ 4. UTILITÁRIOS SEMÂNTICOS NO TAILWIND ============ */
@theme inline {
  --color-bg:             var(--bg);
  --color-bg-sunken:      var(--bg-sunken);
  --color-surface:        var(--surface);
  --color-surface-raised: var(--surface-raised);
  --color-surface-tint:   var(--surface-tint);
  --color-line:           var(--border);
  --color-line-strong:    var(--border-strong);
  --color-fg:             var(--fg);
  --color-fg-muted:       var(--fg-muted);
  --color-fg-subtle:      var(--fg-subtle);
  --color-brand:          var(--brand);
  --color-brand-hover:    var(--brand-hover);
  --color-brand-pressed:  var(--brand-pressed);
  --color-brand-text:     var(--brand-text);
  --color-on-brand:       var(--on-brand);
  --color-accent:         var(--accent);
  --color-accent-text:    var(--accent-text);
  --color-on-accent:      var(--on-accent);
  --color-success:        var(--success);
  --color-error:          var(--error);
}

/* ============ 5. LAYOUT E MOVIMENTO (variáveis CSS) ============ */
:root {
  --container-max: 1720px;
  --page-margin:   clamp(1.5rem, 5.5vw, 5rem);
  --gutter:        clamp(1rem, 1.6vw, 1.5rem);
  --section-y:       clamp(6rem, 11vw, 10rem);
  --section-y-tight: clamp(4rem, 8vw, 8rem);

  --dur-instant:   100ms;
  --dur-fast:      200ms;
  --dur-base:      400ms;
  --dur-slow:      750ms;
  --dur-cinematic: 1200ms;

  --z-decor: 1;  --z-raised: 10; --z-sticky: 100; --z-nav: 200;
  --z-overlay: 300; --z-modal: 400; --z-toast: 500; --z-grain: 900;
}

/* ============ 6. BASE ============ */
body {
  background: var(--bg);
  color: var(--fg-muted);
  font-family: var(--font-sans);
  font-size: var(--text-body);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

[data-surface] {
  background:
    radial-gradient(120% 80% at 50% 0%, var(--bg-glow-from) 0%, var(--bg) 70%);
  color: var(--fg-muted);
}

:focus-visible {
  outline: 2px solid var(--focus-ring);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 1ms !important;
    transition-duration: 200ms !important;
    scroll-behavior: auto !important;
  }
}
```

Uso no JSX: `bg-surface border border-line text-fg rounded-lg`, `text-h2 text-fg`, `text-label uppercase text-brand-text`, `bg-brand text-on-brand hover:bg-brand-hover`.

---

## 17. Biblioteca no Figma

A biblioteca será construída **depois da aprovação deste documento**, espelhando os tokens da seção 16 um para um.

### 17.1 Arquivo

`Rumo · Site · Design System`

| Página | Conteúdo |
|---|---|
| Capa | Nome, versão, status, link para este documento |
| Fundamentos | Cor, tipografia, grid, espaçamento, raios, profundidade |
| Efeitos | Grão, dot grid com spotlight, mapa da operação, rotas, HUD, luz direcional, borda acesa · Efeitos interativos (12 padrões) |
| Ícones | Lucide 1.5px nos quatro tamanhos + regras |
| Componentes | Um frame por componente, com todas as variantes e estados |
| Seções | S01 a S16 montadas com componentes |
| Templates | Home, serviço, produto, case, artigo, sobre, carreiras (desktop 1440 e mobile 375) |

### 17.2 Coleções de variáveis

| Coleção | Modos | Conteúdo |
|---|---|---|
| **Primitivas** | (nenhum) | `ink/*`, `rumo/*`, `ice/*`, `success/*`, `error/*` |
| **Tema** | Dark · Light | Todas as semânticas da seção 2.2 (`bg`, `surface`, `fg`, `brand`...), apontando para Primitivas |
| **Produto** | Rumo · PriceFleet · Sófi · Genial · SGAE · Startvet | `accent`, `accent-text`, `on-accent` |
| **Dimensões** | (nenhum) | Espaçamento, raios, larguras de borda, tamanhos de ícone |
| **Tipografia** | Desktop · Mobile | Tamanhos dos níveis da escala (valores máximo e mínimo do `clamp`) |

### 17.3 Estilos

- **Texto:** um estilo por nível da escala (seção 3.3), em Geist, com `label` e `mono-micro` em Geist Mono.
- **Efeitos:** `elevation/2`, `elevation/3`, `shadow/sm`, `shadow/md`, `shadow/lg`, `focus-ring`, `glow/brand` (controle aceso). Componentes de luz: `Light/Top Edge` e `Light/Rim`.
- **Componentes com variantes:** Botão (variante × tamanho × estado × tema), Input (estado × tema), Tag, Status, Cards (tipo × tema), Navegação (estado), Acordeão, Abas, Stat, Rodapé.

---

## 18. Evoluções propostas para o manual

Itens que mudam ou ampliam `style/manual-de-design.md`. Todos foram aprovados e aplicados ao manual em 2026-10-23; a tabela fica como registro da origem de cada regra.

| # | Tema | Manual hoje | Proposta | Motivo |
|---|---|---|---|---|
| E01 | Neutros | 3 tons escuros | Escala `ink` de 11 tons (2.1) | Estados e camadas de interface; tons já usados nas peças aprovadas |
| E02 | Ciano | Um valor | Degraus de estado `rumo-400` a `rumo-800` + alfas | Hover, pressionado e texto no claro, sem virar paleta decorativa |
| E03 | Pesos de título | 600 a 800 | 600 (SemiBold) nos títulos, nada acima | Referência Lumora aprovada (v0.4) |
| E04 | Corpo | Mínimo cerca de 14px | Mínimo 16px | Legibilidade em tela e campos no iOS |
| E05 | Família no site | Satoshi e Poppins | Geist + Geist Mono; Satoshi e Poppins fora do site | Pedido do usuário (v0.4): mais encorpada e legível, referência Lumora |
| E06 | Mono | Nenhuma obrigatória | Geist Mono só na camada HUD, até 12px | Camada técnica aprovada nas capas HUD |
| E07 | Modo claro | Comunicações leves e Endomarketing | Também em seções de leitura do site (blog, cases, artigo) | Decisão do usuário: "dark com seções claras" |
| E08 | Funcionais | Só verde | Vermelho funcional de erro + versões para fundo claro | Formulários precisam de erro acessível |
| E09 | Legenda no claro | `#8C8C8C` | `#5B6B73` | `#8C8C8C` tem 3,4:1 e falha no AA |
| E10 | Texto no botão ciano | Branco 600+ permitido | Sempre `#050505` | Branco sobre ciano dá 2,6:1 |
| E11 | Links | Sem sublinhado como padrão | Sublinhado em texto corrido; sem sublinhado fora dele | Acessibilidade (pista além da cor) |
| E12 | Produtos | Submarcas não herdam regras | Acento de produto em escopo de página | Decisão do usuário: "Rumo + acento do produto" |
| E13 | Textura | Não citada | Grão obrigatório em toda superfície | Checklist de acabamento do usuário |
| E14 | Glow | Permitido, sutil (luz ciano desfocada) | Luz direcional com anatomia fonte branca → azul claro → ciano → queda (8.8); nunca círculo desfocado; nunca em logo, símbolo, ícone ou texto | Reprovação do símbolo com brilho e do glow em blob (v0.3) |
| E15 | Movimento | 0.4s a 0.75s | Tokens de 100ms a 1200ms + loops | Interface pede respostas rápidas; hero pede tempo cinematográfico |
| E16 | Raios | 6px a 12px | Escala 4 / 6 / 8 / 12 + 24 só no painel de seção | Precisão de componente |
| E17 | Ciano no título | De 1 a 3 palavras em ciano | Título em dois tons (fg + cinza frio); ciano fora do título | Benchmark aprovado (proposta 01) |
| E18 | Containers no Modo claro | Cartões brancos com borda | Containers tonais azul-gelo sem borda, ícone ciano em disco #0A1419 | Benchmark aprovado (proposta 07). No site, substituído pela E19 |
| E19 | Superfície do site [v0.5] | Dark com seções claras (E07) | Só o preto infinito; nenhuma seção clara no site. Modo claro segue valendo para endomarketing e comunicações leves | Usuário: a seção branca "distorceu muito a identidade visual" |
| E20 | Textura [v0.5] | Grão estático | Grão em movimento + linhas de varredura de 1px a cada 3px (2,5% a 3%) em toda a página (8.1 e 8.1b) | Referência Signal aprovada pelo usuário |
| E21 | Luz no cursor [v0.5] | Luz só da borda de topo | Spotlight que acompanha o cursor em x e y dentro dos containers, com a mesma anatomia de luz (8.8) | Pedido do usuário |
| E22 | CTA nos cards de serviço [v0.5] | Só o card principal tinha link | Todo card de serviço tem CTA (verbo + objeto), alinhado no pé; títulos alinhados entre cards | Pedido do usuário |
| E23 | Faixa de tecnologias [v0.5] | Logo wall só para clientes | Marquee com a stack logo abaixo do hero | Pedido do usuário |
| E24 | Avaliações do Google [v0.5] | Não previsto | Seção S17 com avaliações reais do perfil | Pedido do usuário |
| E25 | Perguntas frequentes na Home [v0.5] | FAQ só em páginas de serviço | Seção S13 na Home | Pedido do usuário |

---

## 19. Pendências

| # | Pendência | Bloqueia |
|---|---|---|
| P1 | Cor do logo: SVGs oficiais em `#05AAE2`, manual em `#00ACE5` (seção 13) | Exportação final do logo para o site |
| P2 | Paletas e logos de Rumo AI, Sófi, Genial, SGAE e Startvet | Acentos das páginas de produto |
| P3 | Sessão de fotos (lista na seção 7.2); `assets/fotos/` está vazia | Seções S09, Sobre, Carreiras |
| P4 | Lista de clientes autorizados para logo wall, cases e depoimentos | S08, S10, depoimentos |
| P5 | Referências de sites em Framer | Afinamento da direção (serão avaliadas contra este documento) |
| P6 | Destino do arquivo no Figma (time ou projeto) | Construção da biblioteca |
| P7 | Copy do site (manifesto, títulos, CTAs) | Templates com texto real |
| P8 | ~~Aprovação das evoluções E01 a E16~~ Resolvida: E01 a E25 aplicadas ao manual em 2026-10-23 | |
| P9 | Avaliações reais do Google: link do perfil ou prints, com nota média e total [v0.5] | Seção S17 |
| P10 | Lista final e logos oficiais da faixa de tecnologias (o usuário citou uma imagem que não chegou; a versão atual usa a stack da base institucional, com nome escrito onde não há logo livre: COBOL, SQL Server, IBM DB2, Azure) | Seção S10b |

---

## 20. Checklist de página

Antes de considerar uma página pronta:

**Direção**
- [ ] Cada dobra tem um protagonista só?
- [ ] Os três níveis de leitura estão claros (mensagem > conteúdo > camada técnica)?
- [ ] No máximo dois efeitos da camada técnica por viewport?
- [ ] Nenhum item da lista de reprovações (1.5)?

**Cor**
- [ ] Componentes usam só tokens semânticos?
- [ ] Ciano só aponta (CTA, ícones, rotas, brilho de card, uma palavra do manifesto)?
- [ ] Títulos em dois tons, sem ciano?
- [ ] Nenhum bloco de ciano chapado, nenhum card branco sobre preto?
- [ ] Verde só em status real? Vermelho só em erro?
- [ ] Contrastes AA conferidos? Nenhuma seção clara no site [v0.5]?

**Tipografia**
- [ ] Só Geist (+ Geist Mono em labels e HUD)?
- [ ] Títulos em 500, tracking negativo, `text-wrap: balance`?
- [ ] Corpo de 16px ou mais, até 65 caracteres por linha?

**Layout**
- [ ] Alinhado ao grid de 12 colunas?
- [ ] `section-y` respeitado? Nenhum canto sem função?
- [ ] Funciona em 375px sem rolagem horizontal?

**Imagem e efeitos**
- [ ] Grão em movimento e linhas de varredura em toda a página [v0.5]?
- [ ] Spotlight do cursor nos containers interativos (só desktop) [v0.5]?
- [ ] Fotos reais tratadas e integradas com fade?
- [ ] Mockups fiéis ao produto real?
- [ ] Nenhum glow em logo, símbolo, ícone ou texto?
- [ ] Toda luz tem fonte quase branca e queda azul claro → ciano → transparente (nenhum círculo desfocado)?

**Movimento**
- [ ] Animações seguem a ordem de leitura e os tokens de duração e curva?
- [ ] Nada de bounce ou travamento de scroll?
- [ ] Movimento reduzido testado?

**Conteúdo**
- [ ] Um CTA primário por seção? Todo card de serviço com CTA alinhado no pé [v0.5]?
- [ ] Avaliações e depoimentos só reais, com autorização?
- [ ] Números e cases conferidos em `knowledge/rumo.md`?
- [ ] Nenhum travessão longo?

**Técnico**
- [ ] Foco visível e navegação por teclado?
- [ ] LCP < 2,5s, CLS < 0,1, 3D carregado depois do LCP?
- [ ] Logo oficial, com respiro, no canto superior esquerdo?
