# Crie um programa que leia u, número inteiro e
# mostre na tela se ele é par ou impar

n = int(input('Informe o número: '))
na = len([n])
nu = n % 2 # pega o resto da divisão se for par a resposta é 0
if nu == 0:
    print('O número {:.0f} é par'.format(n))
else:
    print('O número {:.0f} é ímpar'.format(n))

