#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são maiores do que 10.

numeros =  input("Digite uma sequência de 5 números aleatórios, separados por virgula: ")
numeros = numeros.split(',') 
numeros = [int(numero) for numero in numeros]


valor_10 = [numero for numero in numeros if numero > 10]


print("Os números maiores que 10 dessa lista são: ", valor_10)
