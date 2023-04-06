#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre e imprima o segundo número mais baixo na lista.

numeros = input("Digite uma lista de números separados por vírgula: ")


numeros = [int(x) for x in numeros.split(",")]

menor = min(numeros)


numeros.remove(menor)


segundo_menor = min(numeros)


print("O segundo menor número da lista é: ", segundo_menor)