# Analisador Sintático de Operações Matematicas

## Introdução
Este TPC tinha como objetivo implementar um analisador sintático para expressões aritméticas simples utilizando a biblioteca **PLY (Python Lex-Yacc)**. O analisador é capaz de processar expressões com operações de adição, subtração, multiplicação, divisão e parênteses. A análise sintática segue uma hierarquia de operações (precedência de operadores), e o código realiza o cálculo de expressões passadas como entrada.

## Funcionamento
As regras de produção estão estruturadas para refletir a precedência das operações. Aqui está um detalhamento de como as produções estão definidas:

#### Operações de Adição e Subtração

- **p_operacao_grau1_1**: Uma expressão de grau 1 pode ser uma expressão de grau 2, que é o caso básico.
- **p_operacao_grau1_2**: Uma expressão de grau 1 pode ser a soma de duas expressões de grau 2.
- **p_operacao_grau1_3**: Uma expressão de grau 1 pode ser a subtração de duas expressões de grau 2.

#### Operações de Multiplicação e Divisão

- **p_operacao_grau2_1**: Uma expressão de grau 2 pode ser uma expressão de grau 3, o que representa o caso mais simples.
- **p_operacao_grau2_2**: Uma expressão de grau 2 pode ser a multiplicação de duas expressões de grau 3.
- **p_operacao_grau2_3**: Uma expressão de grau 2 pode ser a divisão de duas expressões de grau 3.

#### Números e Parênteses

- **p_operacao_grau3_1**: Uma expressão de grau 3 pode ser um número.
- **p_operacao_grau3_2**: Uma expressão de grau 3 pode ser uma expressão de grau 1 envolvida por parênteses.

## Testes

### Teste 1
**Entrada:**  
```
"4+(1)"
```
**Saída esperada:**  
```
5
```

## **Conclusão**
O código implementa com sucesso um analisador sintático que respeita a precedência
das operações em expressões aritméticas simples. Utilizando o PLY (Python Lex-Yacc),
o código organiza a análise da expressão em níveis (graus) que correspondem à
hierarquia dos operadores. O funcionamento do código permite a avaliação correta de
expressões como adição, subtração, multiplicação, divisão e parênteses.
