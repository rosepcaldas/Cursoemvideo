# desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0.50 por Km
# para cada viagem de até 200 Km e R$ 0.45 para viagens mais longas

d = int(input('Qual a distância da viagem? '))
if d <=200:
    passagem = d*0.5
else:
    passagem = d*0.45
print('O valor da passagem é R${:.2f}'.format(passagem))
