# Melhore o jogo do desafio 028 onde o computador vai
# 'pensar' em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários.
from random import randint

computador = randint(0,10)
print('-'*80)
print('Sou seu computador ... Acabei de pensar em um número entre 0 e 10.'
      '\nSerá que você consegue adivinhar qual foi?')
print('-'*80)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Dê o seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ... Tente mais uma vez.')
        elif jogador> computador:
            print('Menos ... Tente mais uma vez.')
print('Acertou! com {} palpites. Parabéns!!!'.format(palpites))
