# Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números e também indique o menor
# e o maior valor que estão na tupla
from random import randint
tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(tupla)
maior = menor = tupla[0]
for c in tupla:
    if c > maior:
        maior = c
    elif c < menor:
        menor = c
print(f'O maior sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
