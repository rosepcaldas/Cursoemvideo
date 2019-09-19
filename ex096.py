'''
    EXERCÍCIO 96 - FUNÇÃO QUE CALCULA ÁREA
    Faça um programa que tenha uma função área(), que receba as
    dimenções de um terreno (largura e comprimento) e mostre área
    do terreno.

'''


def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg}x{comp} é de {a}m².')

print('--------------------')
print('Controle de Terrenos')
print('--------------------')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
