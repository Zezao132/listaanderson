#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, remova todos os números duplicados da lista e imprima a nova lista.

numeros = input("Digite uma lista de números separados por vírgula, com um número duplicado: ")


numeros = [int(x) for x in numeros.split(",")]


sem_duplicatas = list(set(numeros))


print("A nova lista sem duplicatas é:", sem_duplicatas)