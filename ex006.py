# Exercício 6
# Crie um algorítimo que leia um número e mostre seu dobro, triplo e a raiz quadrada.
#
n = int(input('Entre com um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é {}.'.format(n, d))
print('O triplo de {} é {}. \nA raiz quadrada de {} é igual a {:.2f}'.format(n, t, n, r))
#
# Outra forma
#
print('\n\nO dobro de {} é {}.'.format(n, (n*2)))
print('O triplo de {} é {}. \nA raiz quadrada de {} é igua a {:.2f}.'.format(n,(n*3),n,pow(n,(1/2))))
