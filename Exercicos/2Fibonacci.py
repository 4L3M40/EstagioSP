# Função que gera a sequência de Fibonacci até um número n
def fibonacci(n):
    # Inicializa a sequência com os dois primeiros números: 0 e 1
    fib_seq = [0, 1]
    # Enquanto o último número da sequência for menor que n
    while fib_seq[-1] < n:
        # Adiciona o próximo número que é a soma dos dois últimos
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq  # Retorna a sequência gerada

# Função que verifica se o número pertence à sequência de Fibonacci
def pertence_fibonacci(numero):
    fib_seq = fibonacci(numero)  # Gera a sequência até o número
    if numero in fib_seq:  # Verifica se o número está na sequência
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci."


numero = int(input("Informe um número: "))
print(pertence_fibonacci(numero))  # Verifica e imprime o resultado
