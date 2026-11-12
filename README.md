# Rumo Soluções · Novo site

Proposta da nova Home do site da Rumo Soluções, construída a partir do design system do site (v0.7).

**Ver online:** https://navarrovaz.github.io/rumo-solucoes-site/

## O que tem aqui

| Arquivo | Conteúdo |
|---|---|
| `index.html` | Home · Desktop 1440 em código, com todos os efeitos funcionando |
| `design-system/tokens.css` | Valores do design system, importados pelo site |
| `design-system/design-system-site.md` | Guia do design system do site: tipografia, luz, efeitos, componentes, seções, governança e checklist |
| `design-system/pendencias.json` | Divergências anteriores à v0.6 que aguardam decisão |
| `scripts/check-ds.mjs` | Verificador que compara o site com o design system |
| `rumo-cowork/` | Submódulo privado com a arquitetura de comunicação e marketing da Rumo (base institucional, manuais, regras editoriais, skills) |

## Design system

Toda divergência nova entre o site e o design system gera um alerta durante a edição, no commit e no GitHub. A saída é corrigir o site ou alterar o design system na mesma entrega (guia, seção 0).

Para verificar manualmente:

```bash
node scripts/check-ds.mjs
```

Para baixar também o submódulo privado `rumo-cowork/` (exige acesso a `navarrovaz/rumo-cowork`):

```bash
git submodule update --init
```

Para ativar o alerta de commit depois de clonar o repositório:

```bash
git config core.hooksPath .githooks
```

## Efeitos da página

- Mapa da operação em canvas no hero: nós que flutuam, rotas com pulsos de luz, atração pelo cursor e cartão ao passar sobre um hub.
- Título por linha, relógio BRT ao vivo, contador e barra de pergunta que digita sugestões.
- Faixa de tecnologias em loop.
- Manifesto que acende com a rolagem e cadeia de números com contadores.
- Cards de serviço com luz de topo e spotlight que acompanha o cursor.
- Narrativa travada na tela em "Como trabalhamos".
- Perguntas frequentes em acordeão e formulário de diagnóstico com validação.
- Dot grid com spotlight no CTA final, textura de linhas e grão em toda a página.

## Status

- Textos provisórios, com números e fatos conferidos na base institucional da Rumo.
- A seção de avaliações do Google aguarda as avaliações reais do perfil.
- O formulário é demonstrativo: nenhum dado é enviado.
- Layout pensado para desktop 1440px; a versão mobile está em desenho.

## Tecnologia

HTML, CSS e JavaScript em um único arquivo. Bibliotecas por CDN: GSAP 3.12.5 com ScrollTrigger e Lenis 1.1.13. Fontes Geist e Geist Mono pelo Google Fonts.

© 2026 Rumo Soluções · Rumo Informática Ltda.
