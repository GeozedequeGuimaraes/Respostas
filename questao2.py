def calcula_fibonacci(numero):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < numero:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

def verifica_fibonacci(numero):
    fibonacci_sequence = calcula_fibonacci(numero)
    return numero in fibonacci_sequence, fibonacci_sequence

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))


pertence, fibonacci_sequence = verifica_fibonacci(numero)
if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

print("Sequência de Fibonacci:")
print(fibonacci_sequence)

