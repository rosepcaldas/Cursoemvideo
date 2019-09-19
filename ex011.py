# Faça um programa que leia a largura e a altura de uma parede
# em metros e calcule sua área e a quantidade de tinta necessária
# para pintála, sabendo que cada litro de tinta pinta uma área de
# 2 m2.
print('-'*40)
print('Cálculo de área para pintura')
print('-'*40)
H = float(input('Qual a altura da parede em metros? '))
L = float(input('Qual a largura da parede em metros? '))
AREA = H * L
LITROS = AREA / 2
print('-'*40)
print('Altura {:.2f} m \nLargura {:.2f} m \nÁrea {:.2f} m2 \nLitros {:.2f}'.format(H, L, AREA, LITROS))
print('-'*40)
print('Serão necessários {:.2f} litros de tinta para pintar uma parede de {:.2f} x {:.2f}'.format(LITROS, H, L))