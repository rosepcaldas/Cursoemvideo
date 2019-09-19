# Desenvolva um programa que leia o comprimento de três
# retas e diga ao usuário se ela pode formar um triângulo
#
# Para que se possa construir um triângulo é necessário que a
# medida de qualquer um dos lados seja menor que a soma das medidas
# dos outros dois e maior que o valor absoluto da diferença entre essas medidas.
#
# {|b-c|<a<b+c}

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('r1: '))
r2 = float(input('r2: '))
r3 = float(input('r3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
