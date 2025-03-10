# Analisador lexico

Programa python desenvolvido em contexto de Processamento de linguagens onde utilizamos de conhecimentos de **Expressões regulares** e **Tokens** para desenvolver um analisidor de **linguagem de query**, convertendo elementos básicos.

## Funcionalidades
1. **TOKENS**: Ultilizando o ply.lex e suas normas foram definidos os seguintes tokens para classificar a linguagem:
   1. 'KEYWORD': {'select', 'where', 'limit', 'a'}
   2. 'VARIABLE': *r'\?[a-zA-Z0-9_]+'*
   3. 'IDENTIFIER': *r'[a-zA-Z]+:[a-zA-Z0-9_]+'*
   4. 'STRING': *r'\"[^\"]*\"(@[a-zA-Z]+)?'*
   5. 'NUMBER': *r'\d+'*
   6. 'SYMBOL': *r'[{}.@:]'*
2. **Defaults**: Por defeito o ply.lex ultiliza alguns tokens para tratar outros tipos de caracteres que possam aparecer no nosso alfabeto:
   1. 'IGNORE': *' \t'*
   2. 'NEWLINE': *'\n'*


## Uso
O script lê um arquivo `.txt`, processa os elementos e imprimi na tela cada token com seus respectivos elementos encontrados
