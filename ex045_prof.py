from random import randint
from time import sleep
cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m'}
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Sua opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada? '))
if jogador >= 3:
    print('{}JOGADA INVÁLIDA{}'.format(cores['vermelho'],cores['limpa']))
elif jogador < 3:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print('-=' * 12)
    print('Computador jogou {}'.format(itens[computador]))
    print('jogador jogou {} '.format(itens[jogador]))
    print('-=' * 12)
    if computador == 0:  # computador jogou PEDRA
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('{}JOGADOR VENCE!{}'.format(cores['azul'],cores['limpa']))
        elif jogador == 2:
            print('{}COMPUTADOR VENCE!{}'.format(cores['vermelho'],cores['limpa']))
    elif computador == 1:# computador jogou PAPEL
        if jogador == 0:
            print('{}COMPUTADOR VENCE!{}'.format(cores['vermelho'],cores['limpa']))
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('{}JOGADOR VENCE!{}'.format(cores['azul'],cores['limpa']))
    elif computador == 2:# computador jogou TESOURA
        if jogador == 0:
            print('{}JOGADOR VENCE!{}'.format(cores['azul'],cores['limpa']))
        elif jogador == 1:
            print('{}COMPUTADOR VENCE!{}'.format(cores['vermelho'],cores['limpa']))
        elif jogador == 2:
            print('EMPATE!')
