# crie um programa que leia dois valores e mostre
# um meno a tela
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair
cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m'}
opção = 0
while opção != 5:
    print('{}={}'.format(cores['amarelo'],cores['limpa'])*40)
    n1 = float(input('Número 1: '))
    n2 = float(input('Número 2: '))
    while opção != 5:
        print('{}={}'.format(cores['amarelo'],cores['limpa'])*40)
        print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair')
        print('{}={}'.format(cores['amarelo'],cores['limpa'])*40)
        opção = int(input('Digite sua opção: '))
        if opção != 4:
            if opção == 1:
                soma = n1 + n2
                print('{} + {} = {}'.format(n1, n2, soma))
            elif opção == 2:
                mult = n1 * n2
                print('{} x {} = {}'.format(n1, n2, mult))
            elif opção == 3:
                if n1 > n2:
                    print('O maior número é: {}'.format(n1))
                elif n2 > n1:
                    print('O maior número é: {}'.format(n2))
                else:
                    print('Os dois números são iguais')
