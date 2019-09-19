'''
EXERCÍCIO 74

Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números e também indique o menor
e o maior valor que estão na tupla

'''
from random import randint
num_aleatorios = (randint(0, 10), randint(0, 10), randint(0, 10),
                  randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram :{num_aleatorios}')
print(f'O maior sorteado foi {max(num_aleatorios)}')
print(f'O menor valor sorteado foi {min(num_aleatorios)}')
