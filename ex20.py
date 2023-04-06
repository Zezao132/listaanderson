#Escreva um programa que peça ao usuário para digitar uma lista de palavras e, em seguida, crie uma nova lista que contenha apenas as palavras que têm um número ímpar de letras.

palavras = str(input("Digite uma lista de palavras separadas por vírgula(com espaço após a virgula): "))
lista_palavras = palavras.split(", ") 


palavras_impares = []

for palavra in lista_palavras:
    if len(palavra) % 2 != 0:
        palavras_impares.append(palavra)

print("Palavras com número ímpar de letras: ", palavras_impares)