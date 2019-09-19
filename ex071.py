# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado,
# (número inteiro) e o programa vai informar quantas cédulas de
# cada valor serão entregues.
# Obs.: Considere que o caixa tem cédulas de R$ 50, R$ 20, R$ 10 e R$ 1
print('='*40)
print('{:^40}'.format('BANCO CEV'))
print('='*40)
cont_50 = cont_20 = cont_10 = cont_1 = 0
valor = valor_r = int(input('Qual valor você quer sacar? R$ '))
while True:
    if valor_r >= 50:
        cont_50 += 1
        valor_r -= 50
        print(f'Total de {cont_50:>3} cédulas de R$50')
    if valor_r < 50:
         break
while True:
    if valor_r >= 20:
        cont_20 += 1
        valor_r -= 20
    if valor_r < 20:
        break
while True:
    if valor_r >= 10:
        cont_10 += 1
        valor_r -= 10
    if valor_r <10:
        break
while True:
    if valor_r >= 1:
        cont_1 += 1
        valor_r -= 1
    if valor_r < 1:
        break

print(f'Total de {cont_20:>3} cédulas de R$20')
print(f'Total de {cont_10:>3} cédulas de R$10')
print(f'Total de {cont_1:>3} cédulas de R$1')
print('='*40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')