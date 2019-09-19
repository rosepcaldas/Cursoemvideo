# Escreva um programa que leia um número inteiro quelquer e peça para o
# usrário escolha a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTA
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} covertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} covertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} covertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVÁLIDA. Tente novamente!')
