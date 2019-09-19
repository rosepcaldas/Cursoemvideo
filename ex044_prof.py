# Elabore um programa que calcule o valor a ser pago por um produto
# considerando o se preço normal e condção de pagamento:
#
# - À vista dinheiro/ cheque: 10% de desconto
# - Á vista cartão: 5% de desconto
# - Em até 2 x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
#
cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m'}
print('{:=^80}'.format('LOJAS GUANABARA'))
pn = float(input('Preço normal: R$ '))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/ cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
cp = int(input('Qual é a opção?  '))
print('-' * 80)
if cp == 1:
    pf = pn - (pn * 0.10)
elif cp == 2:
    pf = pn - (pn * 0.05)
elif cp == 3:
    pf = pn
    parcela = pf / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif cp == 4:
    pf = pn + (pn * 0.20)
    totalparc = int(input('Quantas parcelas? '))
    parcela = pf / totalparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totalparc, parcela))
else:
    pf = pn
    print('{}OPÇÃO INVALIDA DE PAGAMENTO! TENTE NOVAMENTE!{}'.format(cores['vermelho'],cores['limpa']))
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(pn, pf))
