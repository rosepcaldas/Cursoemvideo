'''

    EXERCÍCIO 78 - MAIOR E MENOR VALORES NA LISTA

    Faça um programa que leia 5 valores e guarde-os em um alista.
    No final, mosrte qual fo o maior e o menor valor digitado e as
    suas respectivas posições na lista.

'''
valores = list()
for n in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {n}: ')))
print('-'*40)
print(f'Você digitou os valores {valores}')
máximo = max(valores)
print(f'O maior valor digitado foi {máximo} nas posições ', end=' ')
for p, v in enumerate(valores):
    if máximo == v:
        print(f'{p}...', end=' ')
mínimo = min(valores)
print(f'\nO menor valor digitado fois {mínimo} nas posições', end=' ')
for p, v in enumerate(valores):
    if mínimo == v:
        print(f'{p}...', end='')
