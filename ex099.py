'''
    EXERCÍCIO 99 - FUNÇÃO QUE DESCOBRE O MAIOR

    Faça um programa que tenha uma funçõ chamada maior(), que receba
    vários parâmetros com valores inteiros
    Seu programa tem que analisar e dizer qual deles é o maior
'''
from time import sleep


def maior(*numeros):
    print('-='*30)
    print('Analizsando os valores passados ...')
    maior = 0
    if len(numeros) == 0:
        print(f'Foram informados 0 valores ao todo')
        print(f'O maior valor informado foi 0')
    else:
        for valor in numeros:
            sleep(0.3)
            print(f'{valor} ', end='')
        print(f'Foram informados {len(numeros)} valores ao todo')
        print(f'O maior valor informado foi {max(numeros)}')



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

