#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista ordenada em ordem crescente.

numeros = input('Digite uma lista de 5 números aleatórios, separados por vírgulas: ')
numeros = numeros.split(",")
numeros = [int(numero) for numero in numeros]

ordem_crescente = sorted(numeros)

print("Lista ordenada dos números em ordem crescente: ", ordem_crescente)
    