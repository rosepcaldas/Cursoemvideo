# Melhore o jogo do desafio 028 onde o computador vai
# 'pensar' em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários.
from random import randint
from time import sleep
n = 1
sorteio = 2
cont = 0
while n != sorteio:
    n = int(input('Adivinhe o número sorteado pelo pc: '))
    sorteio = randint(0,10)
    print('processando...')
    sleep(1)
    if n == sorteio:
        print('{} VOCÊ ACERTOU!!!'.format(sorteio))
    else:
        print('{} ERROU!!!'.format(sorteio))
        cont += 1
print('Você acertou depois de {} tentativas.'.format(cont))