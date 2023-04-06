#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre e imprima o segundo número mais alto na lista.


numeros = input("Digite uma lista de números separados por vírgula: ")


numeros = [int(x) for x in numeros.split(",")]


maior = max(numeros)


numeros.remove(maior)


segundo_maior = max(numeros)


print("O segundo número mais alto na lista é:", segundo_maior)