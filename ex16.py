#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que aparecem mais de uma vez na lista original.

numeros = input("Digite uma lista de números separados por vírgula: ")


numeros = [int(x) for x in numeros.split(",")]

repetidos = []
for num in set(numeros):
    if numeros.count(num) > 1:
        repetidos.append(num)


print("Os números repetido dessa lista são:", repetidos)