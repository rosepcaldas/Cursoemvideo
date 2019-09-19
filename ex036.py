# Escrevam um programa para aprovar um empréstimo bancário
# para compra de uma casa.
# O programa vai perguntar:
# VALOR DA CASA
# SALÁRIO
# QUANTOS ANOS ele vai pagar
#
# Calcule o valor da prestação mensal, sabendo que
# ela não pode exceder 30% do salário ou então o empréstimo
# será negado
#
print('-'*80)
ValorCasa = float(input('Qual o valor da casa? R$ '))
Salario = float(input('Qual o valor do salário? R$ '))
QuantosAnos = float(input('Em quantos anos pretende pagar: '))
PrestacaoMensal = (ValorCasa / QuantosAnos / 12)
PrestacaoLimite = Salario*0.3

print('-'*80)
print('O valor limite da mensalidade para aprovação é de (30% do salário): R$ {:.2f}'.format(PrestacaoLimite))
print('O valor da mensalidade é de: R$ {:.2f}'.format(PrestacaoMensal))
print('-'*80)
if PrestacaoMensal <= PrestacaoLimite:
    print('A prestação mensal será de R$ {:.2f} por {:.0f} anos.'.format(PrestacaoMensal, QuantosAnos))
else:
    print('O empréstimo NÃO foi aprovado pois o valor da mensalidade excede 30% do salário')

print('-'*80)







