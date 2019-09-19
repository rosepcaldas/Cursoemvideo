# MELHORAR O DESAFIO 61 PERGUNTANDO AO USUÁRIO QUANTOS TERMOS
# A MAIS ELE QUER VER E ENCERRA SE ELE DISSER 0 TERMOS
# Programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa prograssão
#
primeiro = int(input('Primeiro termo: '))
razão = int(input('Rasão:'))
print('Os 10 primeiros termos de uma PA de razão {} iniciando com {}:'.format(razão, primeiro))
décimo = primeiro + (10 - 1) * razão
PA = primeiro
print(PA,end=' → ')
while PA <= (décimo-1):
    PA += razão
    print(PA, end=' → ')
print('')
ntermos = 1
while ntermos >= 1:
    cont = 0
    ntermos = int(input('Quantos termos a mais você quer ver? '))
    if ntermos >= 1:
        while cont != ntermos:
            PA += razão
            print(PA, end=' → ')
            cont += 1
    print('')
print('ACABOU')