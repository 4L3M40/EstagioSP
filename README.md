# Repositório de Exercícios

Este repositório contém a resolução de exercícios de lógica de programação em Python. Abaixo estão as descrições e detalhes de funcionamento de cada exercício.

---

## Exercício 1: Cálculo da Soma de Números em um Intervalo

### Descrição:
O objetivo deste exercício é calcular a soma de todos os números inteiros de 1 até um determinado índice (`INDICE`). O código utiliza um loop `while` para iterar sobre os números e acumular a soma na variável `SOMA`.

### Funcionamento:
1. **Variáveis Iniciais:**
   - `INDICE = 13`: Define o limite superior para o cálculo da soma.
   - `SOMA = 0`: Inicializa a variável que armazenará o resultado da soma.
   - `K = 0`: Inicializa o contador que será incrementado a cada iteração.

2. **Loop `while`:**
   - O loop continua enquanto `K` for menor que `INDICE`.
   - A cada iteração, `K` é incrementado em 1 (`K += 1`).
   - O valor de `K` é adicionado à variável `SOMA` (`SOMA += K`).

3. **Resultado Final:**
   - Após o loop, o valor final de `SOMA` é exibido. Neste caso, o valor será `91`, pois a soma dos números de 1 a 13 é 91.

---

## Exercício 2: Verificação de Número na Sequência de Fibonacci

### Descrição:
Este exercício verifica se um número informado pelo usuário pertence à sequência de Fibonacci. A sequência de Fibonacci é uma série de números onde cada número é a soma dos dois anteriores, começando com 0 e 1.

### Funcionamento:
1. **Função `fibonacci(n)`:**
   - Gera a sequência de Fibonacci até que o último número seja menor que `n`.
   - A sequência começa com `[0, 1]` e cada novo número é a soma dos dois últimos.

2. **Função `pertence_fibonacci(numero)`:**
   - Usa a função `fibonacci(n)` para gerar a sequência até o número informado.
   - Verifica se o número está na sequência e retorna uma mensagem correspondente.

3. **Entrada do Usuário:**
   - O usuário informa um número, e o programa verifica se ele pertence à sequência de Fibonacci.

---

## Exercício 3: Análise de Faturamento Mensal

### Descrição:
Este exercício lê os dados de faturamento diário de um arquivo JSON e calcula:
- O menor valor de faturamento.
- O maior valor de faturamento.
- O número de dias em que o faturamento foi superior à média mensal.

### Funcionamento:
1. **Leitura do Arquivo JSON:**
   - O código lê um arquivo JSON que contém uma lista de faturamento diário.
   - O arquivo deve ter a chave `"faturamento_mensal"` com os valores de faturamento.

2. **Cálculo das Métricas:**
   - Filtra os dias com faturamento válido (maior que 0).
   - Calcula o menor e o maior faturamento.
   - Calcula a média de faturamento e conta quantos dias tiveram faturamento acima da média.

3. **Exibição dos Resultados:**
   - O programa exibe o menor faturamento, o maior faturamento e o número de dias com faturamento acima da média.

---

## Exercício 4: Cálculo de Percentual de Representação por Estado

### Descrição:
Este exercício calcula o percentual de representação de cada estado em relação ao faturamento total. O faturamento de cada estado é fornecido em um dicionário.

### Funcionamento:
1. **Dicionário de Faturamento:**
   - Um dicionário contém o faturamento de cada estado, incluindo uma categoria "Outros".

2. **Cálculo do Percentual:**
   - O código calcula o faturamento total somando os valores do dicionário.
   - Para cada estado, calcula o percentual de representação em relação ao faturamento total.

3. **Exibição dos Resultados:**
   - O programa exibe o percentual de representação de cada estado.

---

## Exercício 5: Inversão de String

### Descrição:
Este exercício inverte uma string fornecida pelo usuário. O código percorre a string de trás para frente e constrói uma nova string com os caracteres invertidos.

### Funcionamento:
1. **Entrada do Usuário:**
   - O usuário informa uma string.

2. **Inversão da String:**
   - O código percorre a string de trás para frente, adicionando cada caractere a uma nova string.

3. **Exibição do Resultado:**
   - O programa exibe a string invertida.

---

## Como Executar os Exercícios

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório.
3. Navegue até a pasta do exercício desejado.
4. Execute o arquivo Python correspondente usando o comando:
   ```bash
   python nome_do_arquivo.py
   ```
 
