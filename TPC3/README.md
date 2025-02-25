# Conversor de Markdown para HTML

Este conversor transforma arquivos **Markdown** em **HTML** simples, convertendo elementos básicos.

## Funcionalidades
1. **Títulos**: Converte `# Título` em `<h1>Título</h1>`, `## Subtítulo` em `<h2>Subtítulo</h2>`, etc.
2. **Texto**: Transforma `**negrito**` em `<b>negrito</b>` e `*itálico*` em `<i>itálico</i>`.
3. **Listas**: Converte listas numeradas (`1. Item`) em `<ol><li>Item</li></ol>`.
4. **Links e Imagens**: `[Texto](url)` vira `<a href="url">Texto</a>`, `![Alt](img.jpg)` vira `<img src="img.jpg" alt="Alt">`.

## Uso
O script lê um arquivo `.md`, processa os elementos e gera um `.html` formatado.
