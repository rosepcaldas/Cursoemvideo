'''
    EXERCÍCIO 100 - FUNÇÕES PARA SORTEAR E SOMAR

    Faça um programa que tenha uma lista chamada números e
    duas funções chamadas sorteia() e somaPar(). A primeira
    função vai sortear 5 números e vai coocá-los dentro da lista
    e a segunda vai mostrar a soma entre todos os valores pares
    sorteados pela função anterior.
'''
from random import randint
from time import sleep


def sorteia():
    print(f'Srteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        sleep(0.4)
        numeros.append(randint(1, 10))
        print(numeros[i], end=' ')
    print('Pronto!')
def soma():
    s = 0
    for i in range(0, 5):
        if (numeros[i] % 2) == 0:
            s += numeros[i]
    print(f'Somando os valores pares de {numeros}, temos {s}')

numeros = list()
sorteia()
soma()
