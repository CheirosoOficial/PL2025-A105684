# Parser de Leituras em Ficheiros CSV

## Introdução

Este TPC teve como objetivo desenvolver um programa em Python que
processa um arquivo  CSV contendo informações sobre obras musicais.
O objetivo é extrair e  analisar dados relevantes, como compositores,
períodos das obras e  títulos, fornecendo insights organizados sobre
o conteúdo do arquivo.

## Funcionamento

O programa realiza as seguintes operações:

1. **Leitura do Arquivo CSV**: Abre e lê o conteúdo do arquivo especificado.
2. **Normalização dos Dados**: Remove espaços em brancos desnecessárias e organiza as linhas do arquivo.
3. **Conversão para Estrutura de Dados**: Transforma o conteúdo CSV em um dicionário estruturado para facilitar a manipulação dos dados.
4. **Queries Específicas**:
   - Gera uma lista ordenada alfabeticamente dos compositores musicais.
   - Calcula a distribuição das obras por período, indicando quantas obras pertencem a cada período.
   - Cria um dicionário associando cada período a uma lista alfabética dos títulos das obras correspondentes.

## Testes

### Teste 1

**Entrada:**

Um arquivo `obras.csv` com o seguinte conteúdo:

```
nome;compositor;periodo
"Sinfonia nº 5";"Beethoven";"Clássico"
"Concerto para Violino";"Bach";"Barroco"
"Bolero";"Ravel";"Moderno"
"Sinfonia nº 9";"Beethoven";"Clássico"
"Clair de Lune";"Debussy";"Moderno"
```

**Saída Esperada:**
```
Resultado da Leitura:
{
  "nome": [
    "\"Sinfonia nº 5\"",
    "\"Concerto para Violino\"",
    "\"Bolero\"",
    "\"Sinfonia nº 9\"",
    "\"Clair de Lune\""
  ],
  "compositor": [
    "\"Beethoven\"",
    "\"Bach\"",
    "\"Ravel\"",
    "\"Beethoven\"",
    "\"Debussy\""
  ],
  "periodo": [
    "\"Clássico\"",
    "\"Barroco\"",
    "\"Moderno\"",
    "\"Clássico\"",
    "\"Moderno\""
  ]
}


Resultado das Queries:
['"Bach"', '"Beethoven"', '"Debussy"', '"Ravel"']
{'"Clássico"': 2, '"Barroco"': 1, '"Moderno"': 2}
{
  "\"Clássico\"": [
    "\"Sinfonia nº 5\"",
    "\"Sinfonia nº 9\""
  ],
  "\"Barroco\"": [
    "\"Concerto para Violino\""
  ],
  "\"Moderno\"": [
    "\"Bolero\"",
    "\"Clair de Lune\""
  ]
}
```
- Lista de compositores ordenada: `["Bach", "Beethoven", "Debussy", "Ravel"]`
- Distribuição por período: `{"Clássico": 2, "Barroco": 1, "Moderno": 2}`
- Obras por período:
  - **Clássico**: `["Sinfonia nº 5", "Sinfonia nº 9"]`
  - **Barroco**: `["Concerto para Violino"]`
  - **Moderno**: `["Bolero", "Clair de Lune"]`

---

### Teste 2

**Entrada:**

Um arquivo `obras.csv` com o seguinte conteúdo:

```
nome;compositor;periodo
"Eine kleine Nachtmusik";"Mozart";"Clássico"
"Messias";"Händel";"Barroco"
"Tristão e Isolda";"Wagner";"Romântico"
"Rapsódia Húngara nº 2";"Liszt";"Romântico"
"Prelúdio Op. 28 nº 4";"Chopin";"Romântico"
```

**Saída Esperada:**
```
{
  "nome": [
    "\"Eine kleine Nachtmusik\"",
    "\"Messias\"",
    "\"Tristão e Isolda\"",
    "\"Rapsódia Húngara nº 2\"",
    "\"Prelúdio Op. 28 nº 4\""
  ],
  "compositor": [
    "\"Mozart\"",
    "\"Händel\"",
    "\"Wagner\"",
    "\"Liszt\"",
    "\"Chopin\""
  ],
  "periodo": [
    "\"Clássico\"",
    "\"Barroco\"",
    "\"Romântico\"",
    "\"Romântico\"",
    "\"Romântico\""
  ]
}


Resultado das Queries:
['"Chopin"', '"Händel"', '"Liszt"', '"Mozart"', '"Wagner"']
{'"Clássico"': 1, '"Barroco"': 1, '"Romântico"': 3}
{
  "\"Clássico\"": [
    "\"Eine kleine Nachtmusik\""
  ],
  "\"Barroco\"": [
    "\"Messias\""
  ],
  "\"Romântico\"": [
    "\"Prelúdio Op. 28 nº 4\"",
    "\"Rapsódia Húngara nº 2\"",
    "\"Tristão e Isolda\""
  ]
}
```
- Lista de compositores ordenada: `["Chopin", "Händel", "Liszt", "Mozart", "Wagner"]`
- Distribuição por período: `{"Clássico": 1, "Barroco": 1, "Romântico": 3}`
- Obras por período:
  - **Clássico**: `["Eine kleine Nachtmusik"]`
  - **Barroco**: `["Messias"]`
  - **Romântico**: `["Prelúdio Op. 28 nº 4", "Rapsódia Húngara nº 2", "Tristão e Isolda"]`

---

### Teste 3

**Entrada:**

Um arquivo `obras.csv` com o seguinte conteúdo:

```
nome;compositor;periodo
"Quatro Estações";"Vivaldi";"Barroco"
"Sinfonia nº 40";"Mozart";"Clássico"
"Fantasia em Ré menor";"Mozart";"Clássico"
"Noturno Op. 9 nº 2";"Chopin";"Romântico"
"Danúbio Azul";"Strauss II";"Romântico"
```

**Saída Esperada:**

```
Resultado da Leitura:
{
  "nome": [
    "\"Quatro Estações\"",
    "\"Sinfonia nº 40\"",
    "\"Fantasia em Ré menor\"",
    "\"Noturno Op. 9 nº 2\"",
    "\"Danúbio Azul\""
  ],
  "compositor": [
    "\"Vivaldi\"",
    "\"Mozart\"",
    "\"Mozart\"",
    "\"Chopin\"",
    "\"Strauss II\""
  ],
  "periodo": [
    "\"Barroco\"",
    "\"Clássico\"",
    "\"Clássico\"",
    "\"Romântico\"",
    "\"Romântico\""
  ]
}


Resultado das Queries:
['"Chopin"', '"Mozart"', '"Strauss II"', '"Vivaldi"']
{'"Barroco"': 1, '"Clássico"': 2, '"Romântico"': 2}
{
  "\"Barroco\"": [
    "\"Quatro Estações\""
  ],
  "\"Clássico\"": [
    "\"Fantasia em Ré menor\"",
    "\"Sinfonia nº 40\""
  ],
  "\"Romântico\"": [
    "\"Danúbio Azul\"",
    "\"Noturno Op. 9 nº 2\""
  ]
}
```
- Lista de compositores ordenada: `["Chopin", "Mozart", "Strauss II", "Vivaldi"]`
- Distribuição por período: `{"Barroco": 1, "Clássico": 2, "Romântico": 2}`
- Obras por período:
  - **Barroco**: `["Quatro Estações"]`
  - **Clássico**: `["Fantasia em Ré menor", "Sinfonia nº 40"]`
  - **Romântico**: `["Danúbio Azul", "Noturno Op. 9 nº 2"]`

## Conclusão

O programa demonstra eficácia na leitura e análise de dados de
um arquivo CSV contendo informações sobre obras musicais. As
funções implementadas permitem extrair insights valiosos, como
a diversidade de compositores, a distribuição das obras ao longo
dos períodos musicais e a catalogação organizada dos títulos das
obras por período. Os testes realizados confirmam a precisão e a
utilidade das análises fornecidas pelo programa. 