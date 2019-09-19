# Programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa prograssão
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
PA = n
print('-'*80)
print('Os 10 primeiros termos da PA de razão {} iniciando com {}:'.format(r,n))
print('-'*80)
print(PA)
for c in range(0, 10):
    PA = PA + r
    print(PA, end=' - ')
print('ACABOU')
print('-'*80)