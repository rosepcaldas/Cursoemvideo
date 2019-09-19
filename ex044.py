# Elabore um programa que calcule o valor a ser pago por um produto
# considerando o se preço normal e condção de pagamento:
#
# - À vista dinheiro/ cheque: 10% de desconto
# - Á vista cartão: 5% de desconto
# - Em até 2 x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m'}
print('-'*80)
print('TABELA DE CONDIÇÕES DE PAGAMENTOS')
print('-'*80)
print('1 - À vista dinheiro/ cheque: 10% de desconto')
print('2 - Á vista cartão: 5% de desconto')
print('3 - Em até 2 x no cartão: preço normal')
print('4 - 3x ou mais no cartão: 20% de juros')
print('-'*80)
pn = float(input('Preço normal: R$ '))
cp = int(input('CÓDIGO - Condição de pagamento: '))
print('-'*80)
if cp == 1:
    print('Condição de pagamento: 1 - À vista dinheiro/ cheque: 10% de desconto ')
    pf = pn - (pn * 0.10)
    print('R$ {:.2f}'.format(pf))
elif cp == 2:
    print('Condição de pagamento: 2 - Á vista cartão: 5% de desconto')
    pf = pn - (pn * 0.05)
    print('R$ {:.2f}'.format(pf))
elif cp == 3:
    print('Condição de pagamento: 3 - Em até 2 x no cartão: preço normal')
    pf = pn
    print('R$ {:.2f}'.format(pf))
elif cp == 4:
    print('Condição de pagamento: 4 - 3x ou mais no cartão: 20% de juros')
    pf = pn + (pn * 0.20)
    print('R$ {:.2f}'.format(pf))
