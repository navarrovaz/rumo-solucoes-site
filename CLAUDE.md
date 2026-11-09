# Site Rumo Soluções

Toda alteração no site segue o design system em `design-system/`.

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
