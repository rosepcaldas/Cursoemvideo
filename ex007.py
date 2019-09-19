# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2)/2
print('A média entre {} e {} é {:.1f}.'.format(n1, n2, m))