# Dados de faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Soma o faturamento total
total_faturamento = sum(faturamento_estados.values())

# Função para calcular o percentual de cada estado
def calcular_percentual(faturamento_estados, total):
    percentuais = {}
    # Para cada estado, calcula o percentual
    for estado, valor in faturamento_estados.items():
        percentuais[estado] = (valor / total) * 100
    return percentuais

# Calcula o percentual de cada estado
percentuais = calcular_percentual(faturamento_estados, total_faturamento)

# Exibe os percentuais
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
