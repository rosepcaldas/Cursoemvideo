# Escreva um programa que faça o computador 'pensar'
# em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador
#
# O programa deverá ecrever na tela se o usuário venceu ou perdeu

import random
from time import sleep
print('-='*50)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar....')
print('-='*50)
computador = random.randint(0,5)
jogador = int(input('Escolha um número entre 0 e 5: '))
print('PROCESSANDO ...')
sleep(1)
if computador == jogador:
    print('PARABÉNS! Você venceu!')
else:
    print('GANHEI! Eu pensei no número {:.0f}'.format(computador))