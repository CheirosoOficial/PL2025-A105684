# Conversor de Markdown para HTML

## Introdução

Este TPC teve como objetivo desenvolver um programa em Python que converte textos formatados em Markdown para HTML. O programa processa um arquivo `.md`, identifica os diferentes elementos Markdown e os transforma em seus equivalentes HTML.

## Funcionamento

O programa percorre o texto em Markdown e aplica as seguintes transformações:

1. **Conversão de cabeçalhos:**
   - `# Título` → `<h1>Título</h1>`
   - `## Subtítulo` → `<h2>Subtítulo</h2>`

2. **Formatação de texto:**
   - `**negrito**` → `<b>negrito</b>`
   - `*itálico*` → `<i>itálico</i>`

3. **Conversão de listas numeradas:**
   - `1. Item` → `<ol><li>Item</li></ol>`

4. **Conversão de links e imagens:**
   - `[Texto](https://exemplo.com)` → `<a href="https://exemplo.com">Texto</a>`
   - `![Alt](imagem.jpg)` → `<img src="imagem.jpg" alt="Alt">`

## Testes

### Teste 1

**Entrada:**
```
# Texto Qualquer

Este é um **relatório simples** para teste de **conversor de .md para .html**

## Introdução
O objetivo deste relatório é apresentar a estrutura e os resultados obtidos com o processamento do dataset.

## Estrutura do Relatório
1. **Leitura e Normalização dos Dados**
2. *Conversão para um Dicionário*
3. **Geração de Estatísticas**
4. *Resultados e Conclusões*

Para mais informações, visite [este link](https://www.example.com).

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)
```

**Saída esperada:**
```html
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<body>
<h1>Texto Qualquer</h1>
<p>Este é um <b>relatório simples</b> para teste de <b>conversor de .md para .html</b></p>
<h2>Introdução</h2>
<p>O objetivo deste relatório é apresentar a estrutura e os resultados obtidos com o processamento do dataset.</p>
<h2>Estrutura do Relatório</h2>
<ol>
<li><b>Leitura e Normalização dos Dados</b></li>
<li><i>Conversão para um Dicionário</i></li>
<li><b>Geração de Estatísticas</b></li>
<li><i>Resultados e Conclusões</i></li>
</ol>
<p>Para mais informações, visite <a href="https://www.example.com">este link</a>.</p>
<p>Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"></p>
</body>
</html>
```

## Conclusão

O programa converte corretamente textos formatados em Markdown para HTML, preservando sua estrutura original e garantindo que os elementos principais (títulos, listas, links, imagens) sejam representados corretamente na página HTML gerada. O teste realizado confirma a precisão e a eficácia da implementação.