# Faça um programa que leia um número qualquer e mostre
# o seu fatorial.
# Ex. 5! = 5x4x3x2x1 = 120
print('==== CÁLCULO FATORIAL =====')
n = int(input('Entre com o número: '))
fat = n
print(n,'! =',end=' ')
for n in range(n,n-(n-1),-1):
    fat = fat * (n-1)
    n = n - 1
    print(n+1, 'x',end=' ')
print(n,'=',fat)