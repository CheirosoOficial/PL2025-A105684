# TP1: Função sum_reader

## Descrição
A função `sum_reader` percorre um texto, somando sequências de dígitos, respeitando comandos "On" e "Off" e exibindo o resultado ao encontrar "=".

## Testes

### Teste 1
**Entrada:** `"123"`  
**Saída esperada:** `123`

### Teste 2
**Entrada:** `"12 off = 34"`  
**Saída esperada:** `12 12`

### Teste 3
**Entrada:** `"= on 50 off 25"`  
**Saída esperada:** `0 50`

### Teste 4
**Entrada:** `"10 off = on 5"`  
**Saída esperada:** `10 15`

### Teste 5
**Entrada:** `"off 100 on 200"`  
**Saída esperada:** `200`