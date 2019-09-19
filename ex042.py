# Refaça o desafio 035 dos triânulos
# acrescentando o ecurso de mostrar que tipo de triânguloserá formado
# - Equilatero: todos os lados iguais
# - Isóceles: dois lados iguis
# - Escaleno: todos os lados diferentes
#
cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m'}
print('-'*80)
print('TRIÂNGULOS')
print('-'*80)
print('Entre com os lados de um triângulo')
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
if a == b == c:
    print('- {}Equilátero{}: todos os lados iguais'.format(cores['amarelo'],cores['limpa']))
elif (a == b or a == c or c == b) and (a < b + c and b < a + c and c < a + b):
    print('{}Isóceles{}: dois lados iguas'.format(cores['amarelo'], cores['limpa']))
elif a < b + c and b < a + c and c < a + b:
    print('{}Escaleno{}: todos os lados diferentes'.format(cores['amarelo'], cores['limpa']))
else:
    print('{}Não é um trângulo!!!{}'.format(cores['amarelo'], cores['limpa']))
