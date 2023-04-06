#-Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números pares da lista.

numeros = input('Digite uma lista de 5 números aleatórios, separados por vírgulas: ')
numeros = numeros.split(",")
valores_pares = []

for numero in numeros:
    numero = int(numero)
    if numero % 2 == 0:
        valores_pares.append(numero)
    
print("Esses são os números pares na lista: ", valores_pares)
