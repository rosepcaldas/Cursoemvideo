'''
    EXERCÍCIO 81 - EZTRAINDO DADOS DE UMA LISTA

    Crie um programa que vai ler vários números em uma lista.
    Depois disso mostre:
    A) Quantos números foram digitados
    B) A lista de valores ordenada de forma decrescente
    C) Se o valor 5 apareceu e etá ou não na lista
'''
lista = []
cont = 0
while True:
    n = int(input('Digite uma valor: '))
    lista.append(n)
    continua = str(input('Quer continuar? [S/N]')).strip().upper()
    if continua == 'N':
        break
lista.sort(reverse=True)
print('-='*30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado dentro da lista.')