# Faça um programa que leia um número qualquer e mostre
# o seu fatorial.
# Ex. 5! = 5x4x3x2x1 = 120
print('==== CÁLCULO FATORIAL =====')
n = int(input('Entre com o número: '))
fat = 1
c = n
print(n, '!=', end=' ')
while c > 0:
    if c != 1:
        print(c, 'x', end=' ')
    else:
        print(c, '=', end=' ')
    fat *= c
    c -= 1
print(fat)