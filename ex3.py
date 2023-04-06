#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre o número máximo e o número mínimo da lista.

numeros =  input("Digite uma sequência de 5 números aleatórios, separados por virgula: ")
numeros = numeros.split(',') 
numeros = [int(numero) for numero in numeros]

valor_maximo = max(numeros)
valor_minimo = min(numeros)

print("O maior número da lista é: ", valor_maximo)
print("O menor número da lista é: ", valor_minimo) 