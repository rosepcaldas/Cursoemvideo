import random
from time import sleep
print('-='*50)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar....')
print('-='*50)
cont = 0
jogador = 1
computador = 2
while jogador != computador:
    computador = random.randint(0,5)
    jogador = int(input('Escolha um número entre 0 e 5: '))
    print('PROCESSANDO ...')
    sleep(1)
    if cont == 0 and jogador != computador:
        print('{:.0f} ERROU!!!'.format(computador))
    if cont >= 1 and jogador != computador:
        print('{:.0f} ERROU DE NOVO!!!'.format(computador))
    if cont > 5 and jogador != computador:
        print('CREDO, JÁ ERROU {} vezes!!!'.format(computador, cont))
    cont += 1
print('Você venceu depois de {} tentativas!'.format(cont))