# Função que inverte uma string
def inverter_string(s):
    string_invertida = ''
    # Percorre a string de trás para frente
    for i in range(len(s)-1, -1, -1):
        string_invertida += s[i]  # Adiciona os caracteres invertidos
    return string_invertida


texto = input("Digite uma string para inverter: ")
print(f"String invertida: {inverter_string(texto)}")
