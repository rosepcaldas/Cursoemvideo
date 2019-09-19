# Faça um programa que leia o ângulo e mostra na tela
# o valor do seno, cosseno e tangente desse ângulo
from math import radians, sin, cos, tan
ang_graus = float(input('Entre vom ângulo: '))
# math.sin( x )
# Devolve o seno de x radianos.
# precisamos converter
ang_rad = radians(ang_graus)
seno = sin(ang_rad)
# outra forma é aninhar a formula
coss = cos(radians(ang_graus))
tang = tan(ang_rad)
print('Para o ângulo {:.0f}º temos os seguintes valores: '
      '\n Seno = {:.2f}'
      '\n Cosseno = {:.2f}'
      '\n Tangente = {:.2f}'.format(ang_graus, seno, coss, tang))
