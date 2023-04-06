#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista com os números duplicados removidos.

numeros =  input("Digite uma sequência de 5 números aleatórios sendo 1 deles duplicado: ")
numeros = numeros.split(',') 
numeros = [int(numero) for numero in numeros]

numeros_duplicados = list(set(numeros)) 

print("Lista sem duplicatas: ", numeros_duplicados)