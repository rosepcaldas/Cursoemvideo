'''

    EXERCÍCIO 79 - VALORES ÚNICOS EM UM ALISTA

    Crie um programa onde o usuário possa digitar vários valores e números e cadastre-os
    em uma lista.
    Caso o número já exista lá dentro, ele não será adicionado.
    No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
lista = list()
while True:
    valor = (int(input('Digite um valor: ')))
    tamanho = len(lista)
    if valor in lista:
        print(f'Valor duplicado! Não vou adicinar ...')
    else:
        lista.append(valor)
        print(f'Valor adicionado com sucesso ...')
    continua = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if continua == 'N':
        break
print('-='*30)
lista.sort()
print(f'Você digitou valores {lista}')
