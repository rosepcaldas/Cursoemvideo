'''
    EXERCÍCIO 88 - PALPITES PARA MEGA SENA

    Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai
    perguntar quantos jogos serão gerados e vai sortear 6 númros entre a e 60 para cada jogo
    cadastrando tudo em uma lista omposta
'''
from random import randint
from time import sleep
jogo = []
listajogos = []
print('-'*40)
print(f'{"JOGO DA MEGASENA":^40}')
print('-'*40)
njogos = int(input('Quantos jogos você quer que sorteie? '))
print('-='*5, f'SORTEANDO {njogos}','-='*5)
for c in range(0, njogos):
    while len(jogo) <= 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogo.sort()
    listajogos.append(jogo[:])
    jogo.clear()
for i, l in enumerate(listajogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*3, '< BOA SORTE! >', '-='*3)
