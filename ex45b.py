# Crie um programa que faça o computador jogar jokenpô com você.
# Pedra ganha de tesoura
# Tesoura ganha de papel
# Papel ganha de pedra

from random import choice

cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m'}

print('-'*80)
print('JOGO JOKENPÔ')
print('-'*80)
print('1 - PAPEL')
print('2 - TESOURA')
print('3 - PEDRA')
print('-'*80)
jogador = int(input('Faça sua escolha: '))
if jogador == 1:
    jogo = 'PAPEL'
elif jogador == 2:
    jogo = 'TESOURA'
elif jogador == 3:
    jogo ='PEDRA'

lista = ['PAPEL','TESOURA','PEDRA']
sorteio = choice(lista)

if jogo == sorteio:
    print('Jogador: ', jogo)
    print('computador: ', sorteio)
    print('-' * 80)
    print('{}EMPATE!!!!{}'.format(cores['amarelo'],cores['limpa']))
    print('-' * 80)
elif jogo == 'PAPEL' and sorteio == 'PEDRA':
    print('Jogador:  ', jogo)
    print('computador: ', sorteio)
    print('-' * 80)
    print('{}VOCÊ GANHOU!!!{}'.format(cores['amarelo'],cores['limpa']))
    print('-' * 80)
elif jogo == 'TESOURA' and sorteio == 'PAPEL':
    print('Jogador:  ', jogo)
    print('Computador: A', sorteio)
    print('-' * 80)
    print('{}VOCÊ GANHOU!!!{}'.format(cores['amarelo'],cores['limpa']))
    print('-' * 80)
elif jogo == 'PEDRA' and sorteio == 'TESOURA':
    print('Jogador:  ', jogo)
    print('Oponente: ', sorteio)
    print('-' * 80)
    print('{}VOCÊ GANHOU!!!{}'.format(cores['amarelo'],cores['limpa']))
    print('-' * 80)
else:
    print('Jogador:  ', jogo)
    print('Oponente: ', sorteio)
    print('-' * 80)
    print('{}PERDEU!!!{}'.format(cores['amarelo'],cores['limpa']))
    print('-' * 80)

