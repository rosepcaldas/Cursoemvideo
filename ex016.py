# Crie um programa que leia um número Real qualquer pelo teclado
# e mostr na tela a sua porção inteira
import math
n = float(input('Digite um número: '))
ni = math.floor(n)
print('O número {} tem a parte inteira {}'.format(n, ni))