# Desenvolva um programa que leia o comprimento de três
# retas e diga ao usuário se ela pode formar um triângulo
#
# Para que se possa construir um triângulo é necessário que a
# medida de qualquer um dos lados seja menor que a soma das medidas
# dos outros dois e maior que o valor absoluto da diferença entre essas medidas.
#
# {|b-c|<a<b+c}

print('-' * 80)
print('Entre com três valores de retas e direi se elas podem formar um triângulo')
print('-' * 80)
r1 = float(input('r1: '))
r2 = float(input('r2: '))
r3 = float(input('r3: '))
a = r1
b = r2
c = r3
if r2 > r1 and r2 > r3:
    a = r2
    b = r1
    c = r3
if r3 > r1 and r3 > r2:
    a = r3
    b = r1
    c = r2
bc = ((b-c)**2)**0.5
if bc < a < b+c:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')
