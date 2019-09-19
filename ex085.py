'''
    EXERCÍCIO 85 - LISTA DE PARES E ÍMPARES

    Crie um programa onde o usuário possa digitar 7 valores numéricos e
    cadastre-os em uma lista única que mantenha separado os valores pares
    e ímpares. No final mostre os valores pares e ímpares em ordem crescente.
'''
lista = [[], []]

for c in range(0,7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('-='*30)
print(f'Os valoes pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
