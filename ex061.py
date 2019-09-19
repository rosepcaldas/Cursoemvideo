# REFAÇA O DESAFIO 51, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA
# MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDI WHILE
# Programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa prograssão
#
primeiro = int(input('Primeiro termo:'))
razão = int(input('Rasão:'))
print('Os 10 primeiros termos de uma PA de razão {} iniciando com {}:'.format(razão, primeiro))
décimo = primeiro + (10 - 1) * razão
PA = primeiro
print(PA,end=' → ')
while PA <= (décimo-1):
    PA += razão
    print(PA,end=' → ')
print('ACABOU')
