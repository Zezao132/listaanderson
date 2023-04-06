#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, verifique se um determinado nome está na lista. Se estiver, imprima "O nome está na lista"; caso contrário, imprima "O nome não está na lista".

    
nomes = ["Ana", "Bruno", "Carlos", "Débora", "Eduardo"]
search_name = input("Digite  nome para verificar se está na lista: ")

if search_name in nomes:
    print("O nome está na lista.")
else:
    print("O nome não está na lista.")