'''

    94 - Unindo dicionários e listas

    Crie um programa que leia nome, sexo, idade de várias
    pessoas, quardando os dados de cada pessoa em um dicionário
    e todos os dicionários em uma lista.
    No fina, mostre:
    A) Quantas pessoas foram cadastradas
    B) A média de idade do grupo
    C) Uma lista com todas as mulheres
    D) Uma lista com todas as pessoas com idade acima da média.
'''

pessoas = {}
lista = []
idades = []
continua = 'S'
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).upper()
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    while True:
        continua = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continua in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if continua == 'N':
        break
print('-='*30)
print(f' A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f' B) A média de idade é de {media:5.2f} anos.')
print(f' C) As mulheres cadastradas foram', end=' ')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end =', ')
print()
print(f' D) Lista das pessoas cadastradas que estão acima da média:')
for p in lista:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'    {k} = {v}', end=' ')
        print()
print('-='*30)
print('ENCERRADO')
print('-='*30)
