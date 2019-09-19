# REFAÇA O DESAFIO 51, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA
# MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDI WHILE
# Programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa prograssão
#
print('-'*40)
print('Gerador de PA')
print('-'*40)
primeiro = int(input('Primeiro termo:'))
razão = int(input('Rasão:'))
termo = primeiro
cont = 1
print('Os 10 primeiros termos de uma PA de razão {} iniciando com {}:'.format(razão, primeiro))
while cont <= 10:
    print('{} → '.format(termo), end='')
    cont += 1
    termo += razão
print('FIM')
