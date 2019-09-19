# Escreva um programa que leia um número n inteiro e mostre na tela
# os n primeiros elementos de uma sequencia de FIBONACCI
# Fn = Fn - 1 + Fn - 2
#
n = int(input('Entre com número de elementos: '))
cont = Fn = f1 = 0
f2 = 1
print(f1, '→', f2, end='')
while (n-3) >= cont:
    Fn = f1 + f2
    print('→', Fn, end='')
    f1 = f2
    f2 = Fn
    cont += 1
