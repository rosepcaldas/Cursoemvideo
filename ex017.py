# Faça um programa que leia o comprimento do
# cateto oposto e do cateto adjacente de um
# triângulo retângulo, calcule e mostre o
# comprimento da hipotenusa.
import math
ca = float(input('Cateto adjacente: '))
co = float(input('Catetoa adjacente: '))
h = math.sqrt(math.pow(ca, 2) + math.pow(co, 2))
print('O comprimento da hipotenusa é: {}'.format(h))

