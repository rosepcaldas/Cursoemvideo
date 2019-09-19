'''
    EXERCÍCIO 82 - DIVIDINDO VALORES EM VÁRIAS LISTAS

    Crie u programa que vai ler vários números e colocar em uma lista.
    Depois disso, crie duas listas externas que vão conter os valores
    pares e os ímpares digitados, respectivamente.
    Ao final mostre o conteúdo das três listas geradas.
'''
lista = []
listapar = []
listaimpar = []
cont = 0
while True:
    lista.append(int(input('Digite um númro: ')))
    resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if lista[cont]%2 == 0:
        listapar.append(lista[cont])
    else:
        listaimpar.append(lista[cont])
    cont += 1
    if resp in 'N':
        break

print('-='*40)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')