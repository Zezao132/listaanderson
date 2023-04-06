#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule e imprima a soma de todos os números ímpares na lista]

numeros = input("Digite uma lista de números separados por vírgula: ")

numeros = [int(x) for x in numeros.split(",")]

soma_impares = 0

for numero in numeros: 
    if numero % 2 == 1:
        soma_impares += numero
    
print("A soma dos números impares da lista são: ", soma_impares)

