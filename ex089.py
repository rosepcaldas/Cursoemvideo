'''
    EXERCÍCIO 89 - BOLETIM COM LISTAS COMPOSTAS

    Crie um programa que lei o nome e duas notas de vários alnos e guarde
    tudo em uma lista composta. No final, mostre um boletim contendo a
    média de cada um e permita que o usuário possa mostrar as notas de cada
    aluno individalmente.
'''
ficha = list()
continua = 'S'
while continua not in 'Nn':
    nome = str(input('Nome: ')).upper()
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    continua = str(input('Quer continuar? [S/N] ')).strip()
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('mostrar a nota de qual aluno? (999) interrompe'))
    if opc == 999:
        print('FINALIZANDO ...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]} ')
print('<<<<< VOLTE SEMPRE >>>>>')
