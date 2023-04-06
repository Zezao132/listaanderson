#Escreva um programa que peça ao usuário para digitar uma lista de palavras e, em seguida, imprima apenas as palavras que começam com a letra "a".

palavras = input('Digite uma lista de palavras aleatórias, separadas por vírgulas: ')
palavras = palavras.split()
inicias_a = []

for palavra in palavras:
    if palavra.startswith("a") or palavra.startswith("A"):
        inicias_a.append(palavra)

print("Essas são as palavras que começam com a letra 'a': ", inicias_a)