# Escreva um programa que leia um número n inteiro e mostre na tela
# os n primeiros elementos de uma sequencia de FIBONACCI
# Fn = Fn - 1 + Fn - 2
#
print('-'*60)
print('Sequência de Fibonacci')
print('-'*60)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*60)
print(t1, '→', t2, end='')
cont = 3
while n >= cont:
    t3 = t1 + t2
    print(' →', t3, end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
print('~'*60)
