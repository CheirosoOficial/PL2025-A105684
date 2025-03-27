# Analisador Léxico para Structured querie Language

## Introdução  
Este relatório apresenta um analisador léxico desenvolvido
em Python utilizando a biblioteca **PLY.LEX**. O objetivo
do programa é processar um arquivo de entrada contendo
código escrito em uma querie structured language e
classificar os tokens presentes no texto.  

## Funcionamento  
O analisador reconhece seis tipos de tokens:  
  - **KEYWORD**: Palavras-chave da linguagem (`select`, `where`, `limit`, `a`).  
  - **VARIABLE**: Variáveis iniciadas por `?`.  
  - **IDENTIFIER**: Identificadores no formato `prefixo:nome`.  
  - **STRING**: Sequências entre aspas opcionais com marcação de idioma.  
  - **NUMBER**: Sequências numéricas.  
  - **SYMBOL**: Caracteres especiais `{ } . @ :`.  

## Testes  

### Teste 1  
**Entrada:**  
```
select ?var where { ?var a "Texto"@en . }
```
**Saída Esperada:**  
```
{
  "KEYWORD": ["select", "where", "a"],
  "VARIABLE": ["?var"],
  "IDENTIFIER": [],
  "STRING": ["\"Texto\"@en"],
  "NUMBER": [],
  "SYMBOL": ["{", "}", "."]
}
```

---

### Teste 2  
**Entrada:**  
```
limit 10 ?x :value "Example" .
```

**Saída Esperada:**  
```
{
  "KEYWORD": ["limit"],
  "VARIABLE": ["?x"],
  "IDENTIFIER": [":value"],
  "STRING": ["\"Example\""],
  "NUMBER": [10],
  "SYMBOL": ["."]
}
```

## Conclusão  
O analisador léxico foi implementado com sucesso, identificando e classificando corretamente os tokens da linguagem definida. Os testes demonstram que o programa pode processar diferentes entradas e extrair informações úteis para futuras análises. A estrutura modular do código permite fácil adaptação para outras linguagens ou regras léxicas.  
```