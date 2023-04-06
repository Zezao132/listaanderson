#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule a média dos números na lista.

n1 = float(input('insira um número aleatorio: '))
n2 = float(input('insira um número aleatorio '))
n3 = float(input('insira um número aleatorio: '))
n4 = float(input('insira um número aleatorio: '))
n5 = float(input('insira um número aleatorio: '))

média = (n1 + n2 + n3 + n4 + n5)/ 5
print('A média entre {}, {}, {}, {} e {} é = a {}'.format(n1, n2, n3, n4, n5, média))