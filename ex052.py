# Entre com numero inteiro e veja se ele é um num primo
n = int(input('Numero inteiro: '))
soma = 0
resultado = 1
for c in range(2, n):
    rd = n % c
    soma = soma + rd
   # print('{} / {} resto = {}'.format(n, c, rd))
    if rd == 0:
        resultado = 0
if resultado == 0:
    print('não é um número primo')
else:
    print('É um número primo')
