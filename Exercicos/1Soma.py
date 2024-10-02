# Definindo as variáveis iniciais
INDICE = 13  # O índice limite
SOMA = 0  # Variável que acumula a soma
K = 0  # Contador

# Loop que vai rodar enquanto K for menor que INDICE
while K < INDICE:
    K += 1  # Incrementa o valor de K em 1
    SOMA += K  # Soma o valor de K na variável SOMA

# Exibe o valor final de SOMA
print(f"O valor final de SOMA é {SOMA}")
