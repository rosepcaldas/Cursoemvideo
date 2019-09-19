'''

    EXERCÍCIO 86 - MATRIZ EM PYTHON

    Crie um programa que crie uma atriz de dimensão 3 x 3 e preencha
    com valores lidos pelo teclado.

    No final mostre a matriz com a formataçã correta
'''
matriz = [[0,0,0], [0,0,0], [0,0,0]]

for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para [{lin},{col}]:'))
print('-='*30)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[ {matriz[lin][col]:^5} ]', end='')
    print()
