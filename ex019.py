# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude ele, lendo
# o nome deles e encrevendo o nome do escolhido
import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
print('-'*40)
print('O aluno escolhido foi: {}'.format(random.choice([a1,a2,a3,a4])))

