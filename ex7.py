#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, imprima o nome mais longo e o nome mais curto da lista.

nomes = input("Digite uma lista de 5 nomes aleatórios, separados por vírgula: ")
nomes = nomes.split(",") 

maior_nome = max(nomes, key=len)
menor_nome = min(nomes, key=len)

print("O nome mais longo da lista é: ", maior_nome)
print("O nome mais curto da lista é: ", menor_nome)