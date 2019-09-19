# Crieum programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dolares ela pode comprar.
# Considere US$ 1.00 = R$ 3.27
reais = float(input('Quantos reais você tem na carteira? R$ '))
dolar = reais // 3.27
troco = reais % 3.27
print('Você pode comprar U$ {:.0f} e sobrará R$ {:.2f} na sua carteira'.format(dolar, troco))