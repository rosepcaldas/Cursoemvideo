from random import shuffle
n1 = input('Primeiro do aluno: ')
n2 = input('Segundo do aluno: ')
n3 = input('Terceiro do alino: ')
n4 = input('Quarto do aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('-'*40)
print('A ordem de apresentação será:')
print(lista)