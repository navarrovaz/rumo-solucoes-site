# Design System: Site Rumo Soluções

> **Papel:** guia de design vivo do site e dos produtos digitais da Rumo Soluções. Fonte de verdade para qualquer página, seção, componente, landing page ou peça web, consultado por designers, desenvolvedores e agentes do Rumo-cowork.
> **Status:** v0.8.4 aprovada em 2026-11-23 (página de Inteligência Artificial revisada pelo usuário, 12.3): logos de Google Drive, Outlook e DeepSeek na faixa de tecnologias e regra para marcas de cor escura (2.7), interface do WhatsApp nas ilustrações de conversa (2.10) e exceção de loop para o celular do card de destaque (9.5), tudo na evolução E39, usados na página de Inteligência Artificial; o menu passa a apontar para ela. v0.8.3 aprovada em 2026-11-19 (página de Terceirização revisada pelo usuário): primeira página de serviço publicada (12.3), neon verde e violeta nos cards de modelo de contratação (2.9), enxame de cursores que constrói a página e contorno neon que segue o cursor (M19, M20), itens do menu sem página apontando para a Home (evolução E38). v0.8.2 de 2026-11-16: listas de Serviços (Terceirização, Software, Aplicativos Mobile, Inteligência Artificial, Infraestrutura) e Produtos (PriceFleet, DataCar, SGAE, Genial) na navegação, com mapa do site atualizado (10.5, 12.1, evolução E37). v0.8.1 de 2026-11-16: guia alinhado à Home publicada, que é a versão oficial (navegação sem mega menu, rodapé, vidro, S12 Notícias, S17 e numeração da Home; S18 em revisão; evolução E36). v0.8 aprovada em 2026-11-13 (Home em código revisada pelo usuário): serviços na Home com o símbolo da Rumo em vidro 3D como fio condutor (S19, E31), wordmark do arquivo do usuário em Plus Jakarta Sans com degradê prateado (2.8). v0.7 de 2026-11-12: Home reorganizada pela estratégia de posicionamento (S18 Especialistas; S05 e S10 saem da Home; evolução E27), containers no preto com borda neon (E28), logos da stack nas cores originais (E29) e manifesto travado com fundo ciano (E30). v0.6 de 2026-11-09: governança do design system (tokens em `design-system/tokens.css`, verificador automático e registro de pendências, evolução E26). v0.5 aprovada em 2026-10-23 (Home em código revisada pelo usuário): site só no preto infinito, textura de linhas + grão em movimento, spotlight que acompanha o cursor, CTA em todo card de serviço, faixa de tecnologias, avaliações do Google e perguntas frequentes (evoluções E19 a E25). v0.4 aprovada em 2026-10-22. Promovido a guia de contexto em `style/` em 2026-10-23. Evoluções E01 a E25 aplicadas ao manual de design (seção 18 deste documento).
> **Referência em código:** Home · Desktop 1440 publicada em https://navarrovaz.github.io/rumo-solucoes-site/, com todos os efeitos deste guia funcionando.
> **Contexto visual:** este arquivo não tem imagens. Para ver cada padrão, consulte o PDF `Designer Gráfico/output/2026-10-22-design-system-site/Rumo-Solucoes-Design-System-Site-v0.4.pdf` (pasta Rumo-cowork do OneDrive; as saídas não estão no repositório) (42 páginas, sumário na página 2) e o Figma [Rumo · Site · Design System](https://www.figma.com/design/5t3Mwrd1SHHL1t9K7SGZKS) (time Marketing Rumo).
> **Escopo:** site institucional rumosolucoes.com (marca mãe Rumo Soluções, com páginas de produto) e produtos digitais.
> **Base:** `rumo-cowork/Designer Gráfico/style/manual-de-design.md` (identidade atual), evoluída para web. O resumo das regras do site está no manual, seção 18.
> **Plataforma alvo:** Next.js (App Router) + Tailwind CSS v4 · biblioteca espelhada no Figma
> **Contexto institucional:** `rumo-cowork/knowledge/rumo.md`

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
3. `rumo-cowork/Designer Gráfico/style/manual-de-design.md`, para tudo o que este documento não cobre;
4. `rumo-cowork/knowledge/rumo.md`, para fatos, números, serviços e produtos.

**Regras de leitura:**

- Valores de token (`design-system/tokens.css`, seção 16) são a fonte de verdade técnica. Tabelas ao longo do texto explicam o porquê.
- Itens **[EVOLUÇÃO]** marcam onde o site amplia o manual. Todos (E01 a E25) foram aprovados e aplicados ao manual em 2026-10-23.
- Itens **[v0.5]** substituem regras anteriores deste guia. Onde uma regra antiga cita seção clara, vale a versão v0.5: o site não usa seções claras.
- Para ver um padrão antes de aplicá-lo, abra a página correspondente do PDF (sumário na página 2) ou o Figma.
- Mudanças aprovadas no site atualizam este arquivo, o Figma e o PDF juntos. Uma mudança de identidade (cor, tipografia, logo) também sobe para o manual.
- Itens **[PENDENTE]** dependem de material ou decisão do usuário (seção 19).
- Nenhum texto produzido para o site usa o travessão longo (manual, seção 14).

**Governança [v0.6]:**

- O site importa `design-system/tokens.css`. Nenhuma página define ou copia valores de token.
- `node scripts/check-ds.mjs` compara o site com as regras. Ele roda a cada edição feita pelo Claude Code, a cada commit e a cada envio ao GitHub.
- Toda divergência nova tem duas saídas: **seguir o design system** (corrigir o site) ou **mudar a rota** (alterar o design system).
- Mudar a rota exige, na mesma entrega: alterar `tokens.css` ou este guia, subir a versão no campo Status, registrar uma evolução `E##` na seção 18 com o motivo e espelhar no Figma. Mudança de identidade (cor, tipografia, logo) também sobe para o manual.
- `design-system/pendencias.json` lista as divergências anteriores à v0.6 que ainda aguardam decisão. A lista só pode diminuir (seção 19, P11).
- O verificador cobre regras objetivas. Direção, composição e conteúdo continuam na revisão pelo checklist da seção 20.
- O PDF é um retrato da v0.4 e só é reexportado em versão fechada.
- A arquitetura de comunicação e marketing (base institucional, manuais, regras editoriais, skills) está no submódulo privado `rumo-cowork/`. Nada dele é copiado para fora do submódulo, porque este repositório é público (ver `CLAUDE.md`).

**Onde ver cada padrão no PDF** (`Designer Gráfico/output/2026-10-22-design-system-site/Rumo-Solucoes-Design-System-Site-v0.4.pdf` (pasta Rumo-cowork do OneDrive; as saídas não estão no repositório)):

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
3. **O ciano aponta.** Ele guia o olho para a ação, o ícone, a rota e a frase final do manifesto [v0.7]. Não preenche áreas e não entra no título (o título usa dois tons).
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

**Exceção [v0.7]:** o fundo da S03 passa a ciano enquanto a seção fica travada na tela, por decisão do usuário (E30). Fora desse efeito, o ciano continua proibido como fundo chapado.

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
| S03 travada [v0.7] | Exceção: durante o pin, o fundo vai do preto ao ciano e volta ao preto antes de soltar. Sobre o ciano, texto em `on-brand` (#050505), frase final em branco, provas pretas (E30) |

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
| PriceFleet | `#009844` | `#007A37` | `#050505` | Definido a partir da identidade do produto (`rumo-cowork/knowledge/rumo.md` 14.1). Apoio: `#2C3E4F` |
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


### 2.7 Cores originais das tecnologias [v0.7]

Os logos da faixa de tecnologias (S10b) aparecem na cor oficial de cada marca, por decisão do usuário (E29). As cores valem só para o logo da faixa (`.tech`); o nome da tecnologia segue em cinza e vai para branco no hover. O verificador recusa o uso em qualquer outro lugar. Tecnologias sem logo livre (COBOL, SQL Server, IBM DB2, Azure) mantêm o ícone genérico em cinza.

| Token | Cor | Tecnologia |
|---|---|---|
| `logo-java` | `#ED8B00` | Java |
| `logo-dotnet` | `#512BD4` | .NET |
| `logo-python` | `#3776AB` | Python |
| `logo-javascript` | `#F7DF1E` | JavaScript |
| `logo-php` | `#777BB4` | PHP |
| `logo-angular` | `#DD0031` | Angular |
| `logo-react` | `#61DAFB` | React |
| `logo-oracle` | `#F80000` | Oracle |
| `logo-mysql` | `#4479A1` | MySQL |
| `logo-mongodb` | `#47A248` | MongoDB |
| `logo-postgresql` | `#4169E1` | PostgreSQL |
| `logo-aws` | `#FF9900` | AWS |
| `logo-googlecloud` | `#4285F4` | Google Cloud |
| `logo-docker` | `#2496ED` | Docker |
| `logo-kubernetes` | `#326CE5` | Kubernetes |
| `logo-n8n` | `#EA4B71` | n8n |
| `logo-claude` | `#D97757` | Claude |
| `logo-gemini` | `#8E75B2` | Gemini |
| `logo-redis` | `#DC382D` | Redis |
| `logo-googledrive` | `#4285F4` | Google Drive [v0.8.4] |
| `logo-outlook` | `#0078D4` | Outlook [v0.8.4] |
| `logo-deepseek` | `#4D6BFE` | DeepSeek [v0.8.4] |

**Faixa de tecnologias da página de IA [v0.8.4]:** no hero da página de Inteligência Artificial, a mesma faixa `.tech` mostra as ferramentas dos agentes (n8n, Google Drive, JSON, Gemini, ChatGPT, Outlook, DeepSeek, GitHub, AWS, Claude Code, GitHub Copilot e Cursor), lista definida pelo usuário (E39). Marcas cuja cor oficial é preta ou escura demais para o fundo (JSON, OpenAI, GitHub, GitHub Copilot, Cursor) aparecem em branco (`fg`), como a própria marca orienta para fundos escuros.


### 2.8 Wordmark em vidro [v0.8]

Usado só na S19, por decisão do usuário (E31). Vem do arquivo `logo-3d-vidro/index.html` entregue por ele: letras RUMO em texto com degradê prateado e o símbolo em vidro 3D (WebGL). Os tokens ficam em `tokens.css` e o verificador recusa o uso fora de `.vb`.

| Token | Valor | Uso |
|---|---|---|
| `font-wordmark` | Plus Jakarta Sans 500 | Letras RUMO e "Soluções" do wordmark |
| `wordmark-from` | `#F2F2F4` | Topo do degradê das letras |
| `wordmark-to` | `#9A9CA3` | Base do degradê das letras |
| `wordmark-sub` | `#8D8F96` | "Soluções" |
| `wordmark-size` | `clamp(64px, 22vw, 330px)` | Lado do quadro do símbolo; as letras medem 0,78 desse valor |

### 2.9 Neon dos modelos de contratação [v0.8.3]

Usado só nos cards de modelo de contratação da página de Terceirização, por decisão do usuário (E38). Cada card é preto profundo e tem um neon próprio no lugar do ciano: eyebrow, ícone do cabeçalho, checks da lista, destaque do painel de exemplo, CTA primário e contorno.

| Token | Valor | Card |
|---|---|---|
| `brand` | `#00ACE5` | Alocação individual |
| `color-neon-green` | `#3DDC97` | Squad dedicada |
| `color-neon-violet` | `#9B8CFF` | Escopo fechado |

Regras:

- Texto sobre o neon: `#050505` (verde 11,5:1; violeta 7,4:1). Sobre o preto, os dois passam de 7:1.
- O verde não é status: não usar `success` nesses cards nem o neon verde para indicar estado.
- Fora desses três cards, o site segue só no ciano. **Exceção [v0.8.4]:** na página de Inteligência Artificial, as três áreas de agentes usam a mesma trinca (Vendas e marketing em ciano, Operações e processos em verde, Inteligência e decisão em violeta), na borda animada do card de área selecionado e do agente aberto e no ícone e na seta do card de área (E39).

---

### 2.10 Interface do WhatsApp nas ilustrações [v0.8.4]

Para ilustrar conversas de agentes de IA, a página de Inteligência Artificial usa o modelo real do WhatsApp (tema claro) dentro de um celular ilustrado, por decisão do usuário (E39): o preto sobre preto não dava impacto e confundia a conversa com o texto da página. As cores valem só dentro do celular (`.wa`); fora dele o site segue a paleta Rumo.

| Token | Valor | Uso |
|---|---|---|
| `wa-cabecalho` | `#008069` | Barra do contato e botão de enviar |
| `wa-fundo` | `#EFEAE2` | Fundo da conversa |
| `wa-saida` | `#D9FDD3` | Balão de quem envia (o cliente) |
| `wa-entrada` | `#FFFFFF` | Balão recebido (o agente), avatar e campo de mensagem |
| `wa-texto` | `#111B21` | Texto dos balões |
| `wa-meta` | `#667781` | Horário e aviso de data |
| `wa-check` | `#53BDEB` | Confirmação de leitura |

Regras:

- Nomes, pedidos e números das conversas são ilustrativos e o bloco leva a nota "Conversas ilustrativas".
- O logo do WhatsApp não aparece; a interface é reproduzida só para o visitante reconhecer o canal.
- O card de destaque que contém o celular usa o degradê ciano da marca (`rumo-400` → `brand` → `rumo-700`) com texto `on-brand`.

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
| `z-overlay` | 300 | Menu mobile, modal |
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
| `radius-lg` | 12px | Card, mídia, mockup |
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
| 3 · Flutuante | Nível 2 + `0 24px 48px -12px rgba(0,0,0,.6)` (modal, dropdown) |

### 5.4 Profundidade no claro

| Token | Valor |
|---|---|
| `shadow-sm` | `0 1px 2px rgba(10,20,25,.06)` |
| `shadow-md` | `0 8px 24px -8px rgba(10,20,25,.12)` |
| `shadow-lg` | `0 24px 48px -16px rgba(10,20,25,.18)` |

Sombras sempre frias (base `#0A1419`), nunca pretas puras. Nada de sombra pesada (manual 15.3).

### 5.5 Vidro (backdrop blur)

Uso **restrito** a dois casos funcionais:

1. navegação depois do scroll;
2. chips flutuando sobre foto ou vídeo.

Especificação escura [v0.8.1]: `background: rgba(5,5,5,.74)`, `backdrop-filter: blur(14px) saturate(140%)`, borda inferior `rgba(255,255,255,.06)`.

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
- texto sobre foto: overlay `#050505` de 40% a 70% (manual 10.2). **Exceção [v0.8]:** nas imagens dos cards de serviço da S19, o degradê vai de 0% no topo a 97% na base, por pedido do usuário (E35).

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
| Entrega | Tempo real (React Three Fiber) no hero; renders estáticos ou vídeo `webm` nas demais seções. **Exceção [v0.8]:** o símbolo em vidro da S19 roda em tempo real (Three.js), carregado só perto da seção, com resolução de no máximo 1.5x, pausado fora da tela e trocado pelo símbolo plano no celular (E31) |

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
| **M04** | Contador | Número sobe de 0 ao valor real em 1600ms, `ease-out`, números tabulares. Só números de `rumo-cowork/knowledge/rumo.md` |
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
| **M19** | Enxame de cursores [v0.8.3] | Só na página de Terceirização. Cursores com etiqueta de perfil constroem cada seção quando ela entra na tela: escrevem os títulos e pintam os blocos (molas criticamente amortecidas, sem overshoot). Cada seção revela sozinha em até 4,2 s; Esc pula a construção; com movimento reduzido, a página já aparece pronta. O cursor do visitante não muda |
| **M20** | Contorno neon que segue o cursor [v0.8.3] | Borda de 1px apagada; sob o cursor, o trecho mais próximo acende (radial de 260 a 280px) e, com o cursor sobre o card, o contorno inteiro acende com brilho, em `dur-base`. Nos modelos de contratação, a luz percorre a borda uma vez ao entrar na tela (`dur-cinematic`). Sem loop contínuo (9.5) |

### 9.5 Proibido

- bounce, elástico, shake, wobble;
- rotação de elementos de texto;
- loops chamativos perto de texto de leitura. **Exceção [v0.8.4]:** o celular com WhatsApp do card de destaque da página de IA percorre as conversas em loop, por pedido do usuário (E39); o loop pausa fora da tela e com o cursor sobre o card, e com movimento reduzido mostra uma conversa parada. Na mesma página, o card do agente aberto no acordeão tem uma luz neon girando pela borda, também por pedido do usuário (E39); com movimento reduzido a luz fica parada. Ainda na página de IA, os cards de área não selecionados dão micropulos contínuos (com leve quique) para indicar que são clicáveis, também por pedido do usuário (E39); param no hover, fora da tela e com movimento reduzido;
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
| Padrão [v0.8] | 52px | 26px | 15px / 500 (`button`) | 16px |
| `sm` [v0.8] | 40px | 18px | 14px / 500 | 16px |

Raio `radius-pill` em todos os botões [v0.8] (E34). Um tamanho só nas seções; o `sm` fica para o menu e o verso dos cards. Ícone à direita (seta), gap de 8px.

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
| Depois de 40px de scroll [v0.8.1] | Vidro escuro (seção 5.5) |
| Ao rolar | Fica sempre visível [v0.8.1] |
| Logo | Canto superior esquerdo (manual 11.5), altura de 28px (mínimo 24px) |
| Links [v0.8.1] | Serviços, Produtos, Cases, Sobre, Carreiras e Blog; 14px, branco a 78% → `fg` no hover; Serviços e Produtos com seta para baixo; sem indicador de página ativa |
| Direita | Link "Rumo AI ↗" + botão primário `sm` "Diagnóstico gratuito" |
| Lista de Serviços e Produtos [v0.8.2] | Lista simples, só com os nomes das subpáginas, nada de ícone, descrição ou card de destaque (o mega menu foi recusado, E36). Serviços: Terceirização, Software, Aplicativos Mobile, Inteligência Artificial, Infraestrutura. Produtos: PriceFleet, DataCar, SGAE, Genial. Painel `bg-sunken`, `radius-lg`, fio interno `border` e `shadow-float`, a 18px abaixo do link; itens de 14px em `fg-muted`, com fundo branco a 4% e `fg` no hover. Abre ao passar o cursor ou no clique, uma lista por vez; fecha ao sair, com Esc ou clicando fora. Entrada em `dur-fast` (E37) |
| Lista no celular [v0.8.2] | No overlay, os itens aparecem recuados 16px abaixo de Serviços e de Produtos, em `h4` / 500 `fg-muted`; o overlay rola se não couber e fecha ao tocar num link |
| Mobile [v0.8.1] | Botão de menu abre overlay em tela cheia quase preto (97%), links em 28px / 600 e botão primário "Diagnóstico gratuito" logo abaixo dos links |

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
| **Rodapé** [v0.8.1] | No fundo da página (preto infinito), com fio de 1px no topo. Cinco colunas: logo, frase "Desenvolvemos pessoas para transformar negócios." e selos ISO + GPTW (56px); Serviços; Produtos; Empresa; Contato com o endereço da sede. Títulos das colunas em mono maiúsculo `fg-subtle`, links em 14px. Barra final com fio de 1px, razão social, CNPJ, ano e "Desde 1997 · Lagoa Santa, MG". Sem redes sociais por enquanto |
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
- A cadeia só usa fatos de `rumo-cowork/knowledge/rumo.md`.
- A luz do card luminoso segue a anatomia da seção 8.8 (fonte, núcleo, corpo, queda). Continua proibido brilho em logo, símbolo, ícone ou texto.
- Ao trocar o ícone de um `Card/Tonal` no Figma, reaplique `brand` no traço (a troca volta o ícone para `fg-muted`).

---

## 11. Biblioteca de seções

Seções reutilizáveis para montar as páginas. Cada uma tem um protagonista.

| Código | Seção | Protagonista | Superfície | Efeitos permitidos |
|---|---|---|---|---|
| **S01** | Hero | Display centralizado + barra de pergunta | Escura | Mapa de rede vivo, véu central, HUD (relógio, metadados, contador) |
| **S02** | Hero de página interna | `h1` + visual | Escura | Dot grid ou foto com fade |
| **S03** | Manifesto e prova | Manifesto que acende + faixa de provas | Escura; ciano durante o pin [v0.7] | No desktop: seção travada (pin) por cerca de 2,4 telas de rolagem, fundo preto → ciano → preto, palavras acendem com a rolagem, provas com contador e luz. No celular: sem pin, fundo preto (E30) |
| **S03b** | Faixa de prova (alternativa) | Stats reais + selos | Escura | Contadores (M04) |
| **S04** | Serviços em bento | O grid | Escura | Spotlight |
| **S05** | Narrativa sticky | Etapas | Escura | Rota (M05), índice mono |
| **S06** | Destaque Rumo AI | Título + demonstração | Escura | Luz direcional, dot grid |
| **S07** | Produtos | Cards de produto | Escura | Acento por card |
| **S08** | Cases | Carrossel ou grid de cases | Escura ou clara | Hover de card |
| **S09** | Pessoas e cultura | Fotografia real | Escura | Fade radial |
| **S10** | Diferenciais | Quatro cards de diferencial | Escura [v0.5] | Spotlight nos cards |
| **S10b** | Faixa de tecnologias [v0.5] | Logos da stack (`rumo-cowork/knowledge/rumo.md`, seção 5.1) em marquee | Escura | M09. Na Home, logo abaixo do hero |
| **S11** | Diagnóstico gratuito | Oferta + CTA | Escura | Luz de topo no painel, HUD |
| **S12** | Conteúdo e notícias [v0.8.1] | Cards de artigo ou notícia. Na Home, "Notícias": três cards escuros (certificação, cultura, inovação) com imagem conceitual e link "Ver todas as notícias" | Escura [v0.5] | Hover de card |
| **S13** | Perguntas frequentes [v0.5] | Acordeão à direita; título, lead e link para especialista fixos à esquerda | Escura | Nenhum. Respostas só com fatos de `rumo-cowork/knowledge/rumo.md` |
| **S14** | CTA final | `h1` + um CTA | Escura | Dot grid com spotlight + luz de topo |
| **S15** | Linha do tempo | Rota 1997 → hoje | Escura | M05 |
| **S16** | Corpo de leitura | Texto 720px | Escura [v0.5] | Nenhum |
| **S17** | Avaliações do Google [v0.8] | Só as duas fileiras de cards em loop, em sentidos opostos, com as bordas sumindo (sem título visível) | Escura | M09, pausa sob o cursor. Card escuro; borda em degradê neon azul só com o cursor sobre ele; avatar ilustrado vetorial e colorido (E33), nome, cargo e depoimento. **[PENDENTE]** Os depoimentos atuais são ilustrativos (pessoas e textos fictícios, marcados "Ilustrativo" no card) e precisam ser trocados por depoimentos reais autorizados antes de publicar |
| **S19** | Marca em vidro, história e serviços [v0.8] | Wordmark em vidro (2.8) → linha do tempo → serviços em cards laterais → encerramento na ampulheta de pixels, com o símbolo em vidro como fio condutor | Escura | O símbolo sai do vão do wordmark passando por baixo das letras, fica no centro-direita enquanto os anos deslizam (linha com ponto e etiqueta do estágio: início, ascensão, expansão, premiados, reconhecimento), vai ao centro e desce em linha reta entre os cards dos serviços, e para no gargalo de uma ampulheta de pixels de uma tela (efeito do hero da Sluice), com o CTA do diagnóstico logo abaixo, subindo com a página; em seguida vem a S17 Avaliações. Giro contínuo no eixo Y, uma volta a cada 9 s; o canvas usa mescla `screen` para o preto do vidro não cobrir o conteúdo. Cards dos serviços com imagem conceitual gerada por IA (7.4), ícone, título `h3` e "Ver detalhes": o card gira no eixo Y (passar o cursor ou clicar) e o verso traz descrição, tópicos e CTA. No celular: símbolo plano no wordmark e conteúdo em lista (E31) |
| **S18** | Especialistas [em revisão, v0.8.1] | Quais tipos de profissionais a Rumo aloca e em quais níveis de senioridade, do estagiário ao sênior ou especialista. Nada além disso | Escura | Não está em nenhuma página publicada. O layout será definido a partir de uma referência do usuário, com esboço aprovado antes de construir (E36). Perfis só de `rumo-cowork/knowledge/rumo.md` 5.1 |

---

## 12. Arquitetura do site e templates de página

### 12.1 Mapa do site (proposta)

```
/                               Home
/servicos                       Hub de serviços (itens e ordem do menu, v0.8.2)
  /terceirizacao                Terceirização (Outsourcing de TI, carro-chefe)
  /software                     Software (desenvolvimento sob medida)
  /aplicativos-mobile           Aplicativos Mobile
  /inteligencia-artificial      Inteligência Artificial (Rumo AI) + link para rumoai.io
  /infraestrutura               Infraestrutura (e Cibersegurança)
/diagnostico-gratuito           Landing de conversão (CTA global)
/produtos                       Hub de produtos (itens e ordem do menu, v0.8.2)
  /pricefleet                   → página resumo + link pricefleet.com.br
  /datacar
  /sgae
  /genial
  /sofi, /startvet              Fora do menu por ora; seguem no rodapé
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
| 1 | S01 Hero | Display "Seu time de TI, sem complicações." + lead (profissionais certos, senioridade e fit cultural, custos e escala da equipe) + barra de pergunta + chips + "fale com um especialista" |
| 2 | S10b Faixa de tecnologias [v0.5] | Logos da stack em marquee, nas cores originais (2.7) |
| 3 | S03 Manifesto e prova | Argumento da estratégia (criar uma aplicação ficou fácil; fazê-la funcionar na empresa, não). No desktop a seção trava, o fundo vai do preto ao ciano e volta, a frase final "É nessa diferença que a Rumo trabalha desde 1997." fica em destaque e as cinco provas entram com contador |
| 4 | S19 Marca em vidro, história e serviços [v0.8] | Wordmark em vidro; linha do tempo (1997, 2004, 2009, 2011 e hoje, texto do usuário); os cinco serviços em cards que giram; encerramento na ampulheta de pixels com o símbolo. Substitui a S04 e a S18 na Home (E31) |
| 5 | S17 Avaliações do Google [v0.8] | Duas fileiras de cards em loop, sem título visível; depoimentos ilustrativos até haver avaliações reais do perfil (pendente, P9) |
| 6 | S12 Notícias [v0.8] | "Acontece na Rumo. Novidades e conquistas.", em cards escuros separados: novidades, eventos e conquistas (ISO 9001, GPTW, Rumo AI), com imagens conceituais geradas no Figma no padrão dos serviços |
| 7 | S13 Perguntas frequentes [v0.5] | Sete perguntas com respostas da base institucional |
| 8 | S14 CTA final | Assinatura da estratégia: "Não estamos presentes apenas na entrega. Estamos presentes na continuidade." |
| Fora da Home [v0.7] | S05 Narrativa sticky · S10 Diferenciais · S18 Especialistas [v0.8] | Na Home quebravam o fluxo de leitura (E27). Ficam para a página de Terceirização, publicada na v0.8.3 (12.3) |
| Fase 2 | S06 Rumo AI · S07 Produtos · S08 Cases · S09 Pessoas | Entram quando houver assets, cases autorizados e fotos reais |

### 12.3 Página de serviço

**Terceirização (`/servicos/terceirizacao/`), publicada na v0.8.3 (E38).** Ordem: S02 hero centralizado com bento de seis cards (foto de profissional real e autorizado, contorno neon da S17 no hover) → S10b clientes em marquee (M09, logos autorizados) → modelos de contratação em pilha fixa, cards pretos com um neon por card (2.9, M20) → S18 lista dos 16 perfis em quatro colunas, só texto → S10 seis diferenciais em 3 × 2 com contorno neon que segue o cursor (M20) → S05 como funciona em quatro etapas interativas (abas com setas do teclado) → S13 perguntas frequentes → S11 formulário de proposta (perfil, senioridade travada quando o perfil é "Ainda não sei", formato, contato e mensagem; o envio abre o e-mail do visitante com o pedido pronto até haver serviço de formulário, P12). A página inteira é construída pelo enxame de cursores (M19).

**Inteligência Artificial (`/servicos/inteligencia-artificial/`), aprovada na v0.8.4 (E39).** Ordem, na lógica de venda definida pelo usuário: S02 hero (luz de cima, grade, marcas nos cantos, esfera de partículas com "AI" que se forma ao carregar, título embaixo à esquerda alinhado pelo topo com o texto e o CTA, faixa `.tech` com as ferramentas num bloco escuro com divisórias) → S03 frase de efeito e três números de mercado com fonte → S04 três cards de área que funcionam como abas (o selecionado com borda animada na cor da área, ciano, verde ou violeta; os outros esmaecidos e com micropulos) → S04 os agentes da área escolhida em acordeão de cards, o aberto com borda animada na cor da área → S05 como trabalhamos em quatro cards de etapa com "o que você recebe" → S14 consultoria com a ampulheta de pixels da Home por trás do card no padrão do CTA final da Home → S13 perguntas frequentes. Ícones no padrão da Terceirização (disco escuro com aro e ícone na cor do contexto). Números de mercado só com fonte citada; nada de soluções próprias (Sófi, recrutador) nem de números institucionais repetidos.

Para as próximas páginas de serviço, o roteiro abaixo continua como ponto de partida. Antes de construir, o esboço da página inteira (ordem dos blocos e layout de cada um no grid de 12 colunas) precisa ser aprovado, com todo o conteúdo alinhado ao `.wrap` e pouca variação visual entre as seções (E36). O roteiro abaixo é ponto de partida, não template obrigatório.

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
| Proibido | Glow, contorno, sombra, gradiente, animação que deforme o logo, símbolo gigante solto como decoração. **Exceção [v0.8]:** na S19, o wordmark em vidro (2.8) tem letras com degradê prateado e o símbolo gira no eixo Y e se desloca como fio condutor dos serviços (E31) |
| Selos | ISO 9001 e GPTW pequenos, juntos, direto no fundo, sem caixa escura; preferencialmente no rodapé e na faixa de prova |

**[PENDENTE] Cor do logo:** os SVGs oficiais em `assets/logos/` usam `#05AAE2` (azul da identidade antiga), enquanto o manual define `#00ACE5`. A diferença é quase imperceptível, mas precisa de decisão: reexportar os arquivos oficiais com `#00ACE5` ou confirmar o `#05AAE2` como cor do logo. Até lá, o logo é usado exatamente como está no arquivo.

---

## 14. Conteúdo e microcopy

- **Tom:** consultivo, humano, sem "tecniquês" excessivo (`rumo-cowork/knowledge/rumo.md` 14.2). A copy do site é uma etapa à parte e segue a skill `copy-social-media` (`rumo-cowork/.claude/skills/copy-social-media/`) adaptada para web ou um briefing próprio.
- **CTA primário global:** "Agendar diagnóstico gratuito". Secundários: "Ver cases", "Conhecer serviços", "Falar com um especialista".
- **Evitar** "Saiba mais" e "Clique aqui". O rótulo diz o que acontece.
- **Números:** só os de `rumo-cowork/knowledge/rumo.md` seção 1.2, conferidos com a seção 16.3 antes de publicar. Para tempo de mercado, preferir **"desde 1997"**, que não vence (em 2026 já são 29 anos, e a base ainda diz "+28 anos").
- **Clientes e cases:** só com autorização para uso de nome e logo.
- **Travessão longo:** proibido em todo texto do site, inclusive `alt`, metadados e mensagens de erro.
- **Mensagens de sistema:** humanas e curtas ("Recebemos seu pedido. Um especialista responde em até 1 dia útil." somente se o prazo for real).

---

## 15. Acessibilidade e performance

### 15.1 Acessibilidade (WCAG 2.2 AA)

- Contraste AA em todo texto (tabela 2.4); 3:1 em bordas de componentes que precisam ser percebidas.
- Foco visível em todos os interativos; ordem de tabulação lógica; menus suspensos operáveis por teclado (Esc fecha).
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

Os valores ficam em [`tokens.css`](tokens.css), importado por todas as páginas. É a única cópia técnica: as tabelas deste guia explicam o porquê de cada valor, e o verificador acusa quando uma cor de `tokens.css` não está documentada aqui.

**Na migração para Next.js + Tailwind v4 (`app/globals.css`):** importe `tokens.css`, troque o primeiro bloco `:root` (primitivas) por `@theme` e acrescente o mapeamento semântico:

```css
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
```

**Base de toda página:**

```css
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

A biblioteca está no arquivo do Figma citado no cabeçalho e espelha `tokens.css`. Mudanças aprovadas são aplicadas nos dois lados na mesma entrega.

### 17.1 Arquivo

`Rumo · Site · Design System`

| Página | Conteúdo |
|---|---|
| Capa | Capa e sumário |
| Guia de uso | Como usar o arquivo |
| 01 · Cores | Primitivas e semânticas |
| 02 · Tipografia | Escala e estilos de texto |
| 03 · Grid, espaço e forma | Grid, espaçamento, raios, profundidade |
| 04 · Ícones | Lucide 1.5px nos quatro tamanhos + regras |
| 05 · Imagem e efeitos | Grão, dot grid com spotlight, mapa da operação, rotas, HUD, luz direcional, borda acesa · Efeitos interativos |
| 06 · Movimento | Durações, curvas e padrões |
| 07 · Componentes | Um frame por componente, com variantes e estados |
| 08 · Seções | Seções da biblioteca montadas com componentes |
| 09 · Templates | Home · Desktop 1440 · v0.7 e propostas A, B e C |
| ⚙ Biblioteca | Componentes mestre |

### 17.2 Coleções de variáveis

| Coleção | Modos | Conteúdo |
|---|---|---|
| **Primitivas** | (nenhum) | `ink/*`, `rumo/*`, `ice/*`, `success/*`, `error/*`, `logo/*` (cores originais das tecnologias, seção 2.7) |
| **Tema** | Dark · Light | Todas as semânticas da seção 2.2 (`bg`, `surface`, `fg`, `brand`...), apontando para Primitivas |
| **Produto** | Rumo · PriceFleet · Sófi · Genial · SGAE · Startvet | `accent`, `accent-text`, `on-accent` |
| **Dimensões** | (nenhum) | Espaçamento, raios, larguras de borda, tamanhos de ícone |
| **Tipografia** | Desktop · Mobile | Tamanhos dos níveis da escala (valores máximo e mínimo do `clamp`) |

### 17.3 Estilos

- **Texto:** um estilo por nível da escala (seção 3.3), em Geist, com `label` e `mono-micro` em Geist Mono.
- **Efeitos:** `elevation/2`, `elevation/3`, `shadow/sm`, `shadow/md`, `shadow/lg`, `focus-ring`, `glow/brand` (controle aceso), `Glow/Neon` e `Glow/Neon Strong` (containers neon, E28). Componentes de luz: `Light/Top Edge` e `Light/Rim`.
- **Componentes com variantes:** Botão (variante × tamanho × estado × tema), Input (estado × tema), Tag, Status, Cards (tipo × tema), Navegação (estado), Acordeão, Abas, Stat, Rodapé.

---

## 18. Evoluções propostas para o manual

Itens que mudam ou ampliam `rumo-cowork/Designer Gráfico/style/manual-de-design.md`. Todos foram aprovados e aplicados ao manual em 2026-10-23; a tabela fica como registro da origem de cada regra.

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
| E26 | Governança [v0.6] | Valores repetidos no guia, no Figma e nas páginas | `tokens.css` como única cópia técnica, verificador automático e duas saídas para toda divergência (seção 0). Inclui o token `--grain-image`. A seção 16 passou a seguir a tabela 3.3 e o Figma | Pedido do usuário: toda alteração atrelada ao design system, com alerta de divergência |
| E27 | Home pela estratégia de posicionamento [v0.7] | Home com a IA em destaque, narrativa sticky e diferenciais; ciano em uma palavra do manifesto | Home reordenada pela estratégia de 2026-11-12: S18 Especialistas entra, S05 e S10 saem da Home, a frase final do manifesto fica em ciano e as provas viram faixa de Stat | Estratégia de posicionamento e revisão do roteiro pelo usuário: fluxo de leitura e mensagem comercial |
| E28 | Containers no preto com borda neon [v0.7] | Cards em grafite (#131416 a #0D0E0F) com borda acesa discreta | Cards em `ink-925` → `ink-950`, borda acesa em ciano nas quatro laterais (mais forte no topo) e halo ciano suave; no hover, borda e halo se intensificam. Quadros internos no `bg` | Pedido do usuário: containers "bem mais dark, preto escuro, com efeitos neon" |
| E29 | Logos da stack nas cores originais [v0.7] | Logos em cinza (#6B6B6B), monocromáticos | Logos maiores (32px) na cor oficial de cada marca, só na faixa de tecnologias (2.7) | Pedido do usuário |
| E30 | Manifesto travado com fundo ciano [v0.7] | Site 100% no preto; ciano como fundo chapado reprovado (1.5) | Na S03, no desktop, a seção trava e o fundo vai do preto ao ciano e volta ao preto; texto preto sobre o ciano e frase final em branco. Atenção: branco sobre ciano tem contraste de 2,6:1, abaixo do AA (seção 2.4) | Pedido do usuário: destacar só o conteúdo da seção com transição de cor de fundo |
| E31 | Símbolo em vidro como fio condutor [v0.8] | Logo só como arquivo oficial, sem degradê nem animação; 3D em tempo real só no hero (13 e 7.3) | Na S19, wordmark do arquivo do usuário (Plus Jakarta Sans e degradê prateado) e símbolo em vidro 3D que sai do wordmark, passa pela linha do tempo, desce entre os cards dos cinco serviços e para numa ampulheta de pixels antes das Avaliações, girando no eixo Y. A S18 sai da Home. Mudança de identidade: o manual de design precisa registrar a exceção | Pedido do usuário, com a Volg (volg.framer.website) como referência de movimento |
| E33 | Avatares ilustrados nas avaliações [v0.8] | Pessoas geradas não representam depoimentos (7.4) | Na S17, cada avaliador ganha um avatar vetorial colorido feito no Figma, claramente ilustrado e sem pretender retratar a pessoa; cards com borda em degradê neon azul no hover | Pedido do usuário |
| E34 | Botões em pílula e padronização da página [v0.8] | Botões com `radius-md` em três tamanhos; logos da stack em 32px | Botões em pílula num tamanho só (52px; 40px no menu e no verso dos cards); títulos de seção em `h2`, subtítulos em `lead`, espaçamento `section-y` entre as seções. Sai o formulário do Diagnóstico da Home: os CTAs levam à futura página de contato | Pedido do usuário |
| E35 | Base das imagens de serviço quase preta [v0.8] | Overlay sobre foto entre 40% e 70% (7.2) | Nos cards de serviço da S19, degradê preto de 0% no topo a 55% na metade, 88% a dois terços e 97% na base, para o título e o botão ficarem legíveis | Pedido do usuário: escurecer mais a parte inferior |
| E36 | Guia alinhado ao site publicado [v0.8.1] | Mega menu com card de destaque (10.5); vidro em três casos (5.5); navegação que se esconde ao rolar; rodapé com redes sociais; S18 em abas na Home | A versão oficial é a publicada em https://navarrovaz.github.io/rumo-solucoes-site/. O guia passa a descrever a navegação, o rodapé e o vidro como estão no ar; o painel de Serviços e Produtos fica em aberto; a S18 fica em revisão (só tipos de profissionais e níveis de senioridade); páginas novas exigem esboço aprovado antes de construir. O rascunho v0.9 (página de Outsourcing recusada) não entra no guia | Decisão do usuário em 2026-11-16 |
| E37 | Listas de Serviços e Produtos na navegação [v0.8.2] | Painel de Serviços e Produtos em aberto (E36) | Lista simples só com os nomes, aprovada pelo usuário em 2026-11-13 e estendida a Produtos; itens e endereços definidos pelo usuário. As subpáginas ainda não existem: os links apontam para os endereços do mapa (12.1). Na v0.8.3, só a Terceirização tem página; os demais itens apontam para a Home (E38). Na v0.8.4, Inteligência Artificial também tem página (E39) | Pedido do usuário em 2026-11-16 |
| E38 | Página de Terceirização publicada [v0.8.3] | Site só no ciano (2.3); nenhuma página de serviço; menu apontando para subpáginas que não existem (E37) | Primeira página de serviço (12.3). Cards de modelo de contratação pretos, cada um com um neon no lugar do ciano: ciano, verde `#3DDC97` e violeta `#9B8CFF` (2.9). Enxame de cursores que constrói a página (M19) e contorno neon que segue o cursor, sem loop contínuo (M20). Itens do menu sem página apontam para o card do serviço na Home (Software, Inteligência Artificial, Infraestrutura, Aplicativos Mobile) ou para a seção de serviços (produtos) até a subpágina existir | Pedido e aprovação do usuário em 2026-11-19 |
| E39 | Ferramentas de IA na faixa de tecnologias [v0.8.4] | Faixa `.tech` só com a stack da Home (2.7) | Três cores oficiais novas (Google Drive, Outlook, DeepSeek) e marcas de cor escura em branco, para a faixa de ferramentas no hero da página de Inteligência Artificial. Na mesma versão, as cores reais do WhatsApp para ilustrar conversas (2.10) e o loop do celular no card de destaque e a luz neon girando no agente aberto e os micropulos dos cards de área não selecionados como exceções à 9.5. A borda animada do card de área selecionado e do agente aberto troca o brilho externo e usa uma cor por área, com a trinca da 2.9 | Pedido do usuário em 2026-11-23 |

---

## 19. Pendências

| # | Pendência | Bloqueia |
|---|---|---|
| P1 | Cor do logo: SVGs oficiais em `#05AAE2`, manual em `#00ACE5` (seção 13) | Exportação final do logo para o site |
| P2 | Paletas e logos de Rumo AI, Sófi, Genial, SGAE e Startvet | Acentos das páginas de produto |
| P3 | Sessão de fotos (lista na seção 7.2); `assets/fotos/` está vazia | Seções S09, Sobre, Carreiras |
| P4 | Lista de clientes autorizados para logo wall, cases e depoimentos | S08, S10, depoimentos |
| P5 | Referências de sites em Framer | Afinamento da direção (serão avaliadas contra este documento) |
| P6 | ~~Destino do arquivo no Figma~~ Resolvida: arquivo `Rumo · Site · Design System` no time Marketing Rumo | |
| P7 | Copy do site (manifesto, títulos, CTAs) | Templates com texto real |
| P8 | ~~Aprovação das evoluções E01 a E16~~ Resolvida: E01 a E25 aplicadas ao manual em 2026-10-23 | |
| P9 | Avaliações reais do Google: link do perfil ou prints, com nota média e total [v0.5] | Seção S17 |
| P10 | Lista final e logos oficiais da faixa de tecnologias (o usuário citou uma imagem que não chegou; a versão atual usa a stack da base institucional, com nome escrito onde não há logo livre: COBOL, SQL Server, IBM DB2, Azure) | Seção S10b |
| P11 | Divergências do site anteriores à v0.6, listadas em `design-system/pendencias.json`: decidir entre ajustar o site ou registrar a rota no design system | Conformidade total da Home |
| P12 | Envio do formulário de proposta da Terceirização: hoje abre o e-mail do visitante com o pedido pronto; ligar um serviço de formulários ou CRM [v0.8.3] | Medição de conversão da página |
| P13 | Espelhar a v0.8.3 no Figma (tokens neon, M19, M20 e a página de Terceirização): a conexão do Figma precisa ser autorizada | Paridade Figma e código |

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
- [ ] Ciano só aponta (CTA, ícones, rotas, brilho de card, a frase final do manifesto [v0.7])?
- [ ] Títulos em dois tons, sem ciano?
- [ ] Nenhum bloco de ciano chapado (exceto o fundo da S03 travada, E30), nenhum card branco sobre preto?
- [ ] Verde só em status real? Vermelho só em erro?
- [ ] Contrastes AA conferidos? Nenhuma seção clara no site [v0.5]?

**Tipografia**
- [ ] Só Geist (+ Geist Mono em labels e HUD)?
- [ ] Títulos em 600 (H4 em 500), tracking negativo, `text-wrap: balance`?
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
- [ ] Números e cases conferidos em `rumo-cowork/knowledge/rumo.md`?
- [ ] Nenhum travessão longo?

**Técnico**
- [ ] Foco visível e navegação por teclado?
- [ ] LCP < 2,5s, CLS < 0,1, 3D carregado depois do LCP?
- [ ] Logo oficial, com respiro, no canto superior esquerdo?
