# Site Rumo Soluções

Toda alteração no site segue o design system em `design-system/`.

## Comunicação, marketing e base institucional

A arquitetura de comunicação da Rumo fica em `rumo-cowork/`, um submódulo do repositório privado `navarrovaz/rumo-cowork`. Comece por `rumo-cowork/CLAUDE.md`, que roteia artigos, posts e peças visuais.

- **Fatos:** números, serviços, produtos, história, missão, visão e valores vêm só de `rumo-cowork/knowledge/rumo.md`. Não invente e não crie cópias da base.
- **Texto do site:** tom da seção 14.2 da base, skill `rumo-cowork/.claude/skills/copy-social-media/` adaptada para web e regras de `rumo-cowork/Artigos Linkedin - BLOG/style/manual-de-redacao.md.txt`.
- **Identidade:** `rumo-cowork/Designer Gráfico/style/manual-de-design.md`. No que é específico do site, prevalece `design-system/design-system-site.md`.
- **Nunca publique no site** o que a base marca como [DIRECIONAMENTO ESTRATÉGICO] (SWOT, concorrentes, personas, lógica de preço), nem clientes e cases sem autorização confirmada (seção 16 da base).
- **Nunca copie arquivos de `rumo-cowork/` para fora do submódulo.** Este repositório é público e o GitHub Pages publica o que está nele.
- **Mudanças no Rumo-cowork** são commits dentro de `rumo-cowork/`, enviados ao repositório privado. Depois, atualize o ponteiro do submódulo neste repositório.

## Antes de alterar uma página

- Consulte a seção pertinente de `design-system/design-system-site.md` e os valores em `design-system/tokens.css`.
- Use os tokens. Não escreva cores, escalas ou durações fora deles e não defina tokens nas páginas.
- Se o pedido contrariar o design system, **pare antes de editar**. Mostre a regra afetada e peça uma escolha:
  - **A. Seguir o design system:** o pedido é adaptado à regra.
  - **B. Mudar a rota:** o design system muda junto com o site.

## Quando o verificador acusar divergência

O hook roda `node scripts/check-ds.mjs` após cada edição. Trate o alerta como bloqueio: apresente a divergência e as saídas A e B e aguarde a escolha, salvo se o pedido já tiver indicado qual seguir.

Nunca adicione entradas em `design-system/pendencias.json` para silenciar um alerta. Essa lista só pode diminuir.

## Mudança de rota (saída B)

Na mesma entrega:

1. Altere `design-system/tokens.css` ou a regra no guia.
2. Suba a versão no campo Status do guia e cite a nova versão no `index.html` e no `README.md`.
3. Adicione uma linha `E##` na seção 18 do guia com o motivo.
4. Espelhe a mudança no Figma (arquivo `5t3Mwrd1SHHL1t9K7SGZKS`).
5. Se mudar identidade (cor, tipografia, logo), avise que `style/manual-de-design.md` também precisa ser atualizado. Esse arquivo fica fora deste repositório.

## O que o script não verifica

Direção, composição, uso do ciano e conteúdo dependem de revisão. Aplique o checklist da seção 20 do guia ao concluir uma página ou seção.
