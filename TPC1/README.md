# Analisador de Sequências Numéricas em Texto  

## Introdução  
Este TPC teve como objetivo desenvolver um programa em Python que
identifica e soma  todas as sequências numéricas presentes em um
texto. O programa permite  ativar ou desativar essa funcionalidade
com comandos específicos e  exibir o resultado acumulado quando
necessário.  

## Funcionamento  
O programa percorre a string fornecida e realiza as seguintes operações:  

- Soma todas as sequências de dígitos encontradas enquanto a funcionalidade estiver ativada.  
- Desativa a soma ao encontrar a palavra `"Off"` (independentemente da capitalização).  
- Reativa a soma ao encontrar a palavra `"On"`.  
- Sempre que encontra o caractere `"="`, exibe o total acumulado até aquele ponto.  

## Testes  

### Teste 1  
**Entrada:**  
```
"Maria 01 23 4 = off 567 8 on 9 ="
```
**Saída esperada:**  
```
28  
37  
```

---

### Teste 2  
**Entrada:**  
```
"on 10 20 off 30 = on 5 5 ="
```
**Saída esperada:**  
```
30  
40  
```

---

### Teste 3  
**Entrada:**  
```
"100 on 50 = off 200 300 on 50 ="
```
**Saída esperada:**  
```
150  
200  
```

## Conclusão  
O programa implementa com sucesso um mecanismo para a soma de números
em um texto, respeitando comandos de ativação e desativação. Os testes
demonstram sua funcionalidade correta em diferentes cenários.  
```  