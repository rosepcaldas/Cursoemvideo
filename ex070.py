# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final mostre:
# A) Qual é o total gasto na compra
# B) Quantos produtos custam mais de R$ 1000
# C) Qual é o nome do produto mais barato
print('-'*40)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('-'*40)
soma = total = cont = cont_mil = 0
while True:
    nome_produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    soma += preço
    while True:
        continua = str(input('Quer continuar [S/N]')).upper().strip()[0]
        if continua in 'SN':
            break
    total += preço
    cont += 1
    if cont == 1 or barato > preço:
        barato = preço
        prod_barato = nome_produto
    if preço > 1000:
        cont_mil += 1
    if continua == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R$ {soma:.2f}')
print(f'Temos {cont_mil} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {prod_barato} que custa {barato:.2f}')
