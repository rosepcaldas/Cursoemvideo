# Escreva um programa que pergunte a quantidade de Km
# percorridos por uma carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagas
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
aluguel = dias*60+km*0.15
print('O total a pagar é de R$ {:.2f}'.format(aluguel))