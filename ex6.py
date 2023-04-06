#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista ordenada em ordem decrescente.

numeros = input('Digite uma lista de 5 números aleatórios, separados por vírgulas: ')
numeros = numeros.split(",")
numeros = [int(numero) for numero in numeros]

ordem_decrescente = sorted(numeros, reverse =True)

print("Lista ordenada dos números em ordem decrescente: ", ordem_decrescente)