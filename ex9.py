#screva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são menores do que 5.

numeros =  input("Digite uma sequência de 5 números aleatórios, separados por virgula: ")
numeros = numeros.split(',') 
numeros = [int(numero) for numero in numeros]


valor_5 = [numero for numero in numeros if numero < 5]


print("Os números menores que 5 dessa lista são: ", valor_5)