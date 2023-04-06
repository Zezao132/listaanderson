#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que são divisíveis por 3.

numeros = input('Digite uma lista de 5 números aleatórios, separados por vírgulas: ')
numeros = numeros.split(",")
divisiveis_3 = []

for numero in numeros:
    numero = int(numero)
    if numero % 3 == 0:
        divisiveis_3.append(numero)
    
print("Esses são os números divisiveis por 3 na lista: ", divisiveis_3)