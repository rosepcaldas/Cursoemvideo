# MELHORAR O DESAFIO 61 PERGUNTANDO AO USUÁRIO QUANTOS TERMOS
# A MAIS ELE QUER VER E ENCERRA SE ELE DISSER 0 TERMOS
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
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        cont += 1
        termo += razão
    print('PAUSA')
    mais = int(input('Quabtos termos você quer a mais? '))
print('Progresão finalizada com {} termos mostrados'.format(total))
