# Programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa prograssão
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
print('-'*80)
print('Os 10 primeiros termos da PA de razão {} iniciando com {}:'.format(razão, primeiro))
print('-'*80)
décimo = primeiro + (10 - 1) * razão
print(décimo)
for c in range(primeiro, décimo + 1, razão):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
print('-'*80)