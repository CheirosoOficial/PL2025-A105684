# Máquina de Vendas

## Introdução
Este TPC tinha como objetivo implementar uma máquina de vendas automatizada
utilizando a biblioteca **PLY.LEX** para análise léxica e tomada de
decisões baseada em estados. O sistema simula uma máquina de venda com
funcionalidades como listagem de produtos, adição de moedas, seleção de produtos
e consulta ao saldo. O código é dividido em duas partes principais: um analisador
léxico e a lógica de controle da máquina.

## Funcionamento

#### Definição da Máquina de Vendas
A máquina de vendas é representada por um estado atual, um saldo de moedas (em centavos) e um estoque de produtos. As principais funções da máquina incluem:
- **Carregar e listar estoque**: O estoque é carregado de um arquivo JSON e pode ser listado.
- **Adicionar moedas**: O usuário pode inserir moedas em centavos ou euros (1 euro = 100 centavos).
- **Selecionar produtos**: O usuário pode escolher um produto baseado em um código, que será descontado do saldo.
- **Verificar saldo**: O saldo disponível é exibido após cada operação.

#### Tokens Definidos
- **COMMAND**: Comandos de operação como "LISTAR", "MOEDA", "SELECIONAR", "SAIR".
- **COINS**: Valores de moedas em euros (e) ou centavos (c).
- **CODES**: Códigos de produtos, que seguem o formato `A1`, `B2`, etc.


#### Fluxo de Execução (Main)
O fluxo de execução principal é responsável por:
1. Exibir uma mensagem de boas-vindas ao usuário.
2. Aguardar a entrada do usuário.
3. Processar a entrada e executar a ação correspondente, como listar produtos, adicionar moedas, ou selecionar produtos.
4. Manter o estado da máquina enquanto o usuário interage.

## Testes

### Teste 1  
**Entrada:**  
```
>> LISTAR
```
**Saída Esperada**:
```
maq: cod | nome | quantidade | preço
---------------------------------
 A1 | Produto A | 10 | 1.50 
 B2 | Produto B | 5 | 2.00
```

---

### Teste 2  
**Entrada:**  
```
>> MOEDA 1e
```
**Saída Esperada**:
```
maq: Saldo = 1e0c
```

---

### Teste 3  
**Entrada:**  
```
>> SELECIONAR A1
```
**Saída Esperada**:
```
maq: Pode retirar o produto dispensado "Produto A"
maq: Saldo = 0e50c
```

## **Conclusão**
Este sistema de máquina de vendas automatizada é uma 
implementação funcional que utiliza análise léxica para
interpretar as entradas do usuário. A máquina é capaz de
listar produtos, adicionar moedas e realizar a compra de
produtos com base no saldo disponível e na quantidade em
estoque. O código está estruturado de forma modular e pode
ser facilmente estendido ou modificado para adicionar
novas funcionalidades ou alterar a lógica de funcionamento.

