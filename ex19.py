#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que são divisíveis por um número fornecido pelo usuário.


# solicita ao usuário uma lista de números
numeros = input("Digite uma lista de números separados por vírgulas: ").split(",")

# converte cada número da lista de entrada em um inteiro
numeros = [int(num) for num in numeros]

# solicita ao usuário o número divisor
divisor = int(input("Digite o número divisor: "))

# cria uma nova lista contendo apenas os números divisíveis pelo divisor
divisiveis = [num for num in numeros if num % divisor == 0]

# imprime a lista de números divisíveis
print("Os números divisíveis por", divisor, "são:", divisiveis)
