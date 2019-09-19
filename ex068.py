# Faça um programa que joque par ou impar com o computador
# O jogo só interrompe quando o jogador PERDER, mostrando
# o total de vitórias consecutivas que le conquistou
# no final do jogo
from random import randint
nvitoria = 0
print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*40)
while True:
    jogador = int(input('Diga um valor: '))
    PI = str(input('Par ou impar? [P/I] ')).upper().strip()[0]
    print('-'*40)
    computador = randint(0, 10)
    soma = jogador + computador
    sobra = soma % 2
    if sobra == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    if (PI == 'P' and resultado == 'PAR') or (PI == 'I' and resultado == 'ÍMPAR'): # vendecor é quem escolheu PAR
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU {resultado}')
        print('-' * 40)
        print('Você VENCEU!')
        nvitoria +=1
        print('Vamos jogar novamente...')
        print('-=' * 20)
    elif (PI == 'P' and resultado != 'PAR') or (PI == 'I' and resultado != 'ÍMPAR'): # PERDEU
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU {resultado}')
        print('-' * 40)
        print('Você PERDEU!')
        print('-=' * 20)
        print(f'GAME OVER! Você venceu {nvitoria} vezes.')
        break
