# Escolher a ordem de apresetação de trabalho de 4 alunos
# Ler 4 nomes
# Mostrar ordem sorteada
import random

n1 = input('Primeiro do aluno: ')
n2 = input('Segundo do aluno: ')
n3 = input('Terceiro do alino: ')
n4 = input('Quarto do aluno: ')
lista = [n1, n2, n3, n4]
print('-'*40)
print('A ordem de apresentação será:')
print(random.sample(lista, k=len(lista)))
