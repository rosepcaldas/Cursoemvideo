# MELHORAR O DESAFIO 61 PERGUNTANDO AO USUÁRIO QUANTOS TERMOS
# A MAIS ELE QUER VER E ENCERRA SE ELE DISSER 0 TERMOS
# Programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa prograssão
print('-'*40)
print('Gerador de PA')
print('-'*40)
primeiro = int(input('Primeiro termo:'))
razão = int(input('Rasão:'))
termo = primeiro
cont = 1
cont2 = 0
print('Os 10 primeiros termos de uma PA de razão {} iniciando com {}:'.format(razão, primeiro))
while cont <= 10:
    print('{} → '.format(termo), end='')
    cont += 1
    cont2 += 1
    termo += razão
print('PAUSA')
mais = 1
while mais != 0:
    mais = int(input('Quantos termos você quer a mais?'))
    cont = 1
    while cont <= mais:
        print('{} → '.format(termo), end='')
        cont += 1
        cont2 += 1
        termo += razão
    if mais > 0:
        print('PAUSA')
    else:
        print('A progressão foi finalizada com {} termos mostrados'.format(cont2))
