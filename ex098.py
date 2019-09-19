'''
    EXERCÍCIO 98 - FUNÇÃO CONTADOR

    aça um programa que tenha uma função chamada contador(),
    que receba tr~es parâmetros: inicio, fim, passo e realize a contagem
    Su programa tem que realizar três contagens através da função criada
    a) De 1 até 10, de 1 em 1
    b) de 10 até 0, de 2 em 2
    c) Um contagem personalizada
'''
from time import sleep

def contador(i, f, p):
    print('-='*20)
    p = abs(p)
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i > f:
        p = -p
        f = f-1
    else:
        f = f+1
    for k in range(i, f, p):
        print(k, end=' ')
        sleep(0.3)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
print('-='*20)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)