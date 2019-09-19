# Crie um programa que faça o computador jogar jokenpô com você.
# Pedra ganha de tesoura
# Tesoura ganha de papel
# Papel ganha de pedra

from random import randint

print('-'*80)
print('JOGO JOKENPÔ')
print('-'*80)
print('1 - PAPEL')
print('2 - TESOURA')
print('3 - PEDRA')
print('-'*80)
jogador = int(input('Faça sua escolha: '))
sorteio = randint(1,3)
print(sorteio)
if jogador == sorteio:
    print('EMPATE!!!!')
elif jogador == 1 and sorteio == 3:
    print('Jogador:  PAPEL')
    print('Oponente: PEDRA')
    print('VOCÊ GANHOU!!!')
elif jogador == 2 and sorteio == 1:
    print('Jogador:  TESOURA')
    print('Oponente: PAPEL')
    print('VOCÊ GANHOU!!!')
elif jogador == 3 and sorteio == 2:
    print('Jogador:  PEDRA')
    print('Oponente: TESOURA')
    print('VOCÊ GANHOU!!!')
else:
    print('PERDEU!!!')

