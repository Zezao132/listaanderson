#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, crie uma nova lista que contenha apenas os nomes que contêm a letra "e".

nomes = input('Digite uma lista de palavras aleatórias, separadas por vírgulas: ')
nomes = nomes.split()
contem_e = []

contem_e = []
for nome in nomes:
    if "e" in nome:
        contem_e.append(nome)

print("Os nomes que contêm a letra 'e' são:", contem_e)