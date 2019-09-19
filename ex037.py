# Escreva um programa que leia um número inteiro quelquer e peça para o
# usrário escolha a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('-'*80)
print('Programa de conversão de bases:')
print('-'*80)

Numero = int(input('Número: '))
print('{}1{} para {}binário{}    '.format(cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa']))
print('{}2{} para {}octal{}      '.format(cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa']))
print('{}3{} para {}hexadecimal{}'.format(cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa']))
Base = int(input('conversão para: '))
print('-'*80)
if Base == 1:
    # cálculo base binária
    Binaria = bin(Numero)
    print('A conversão de {:.0f} para base binária é: ( {} )'.format(Numero, Binaria))
elif Base == 2:
    # cálculo base octal
    Octal = oct(Numero)
    print('A conversão de {:.0f} para base octal é: {}'.format(Numero, Octal))
elif Base == 3:
    # cálculo base hexadeciamal
    Hexadecimal = hex(Numero)
    print('A conversão de {:.0f} para base hexadecimal é: {} '.format(Numero, Hexadecimal))
else
    print('OPÇÃO INVÁLIDA!')