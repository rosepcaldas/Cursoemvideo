# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento
# Para salários superiores a R$ 1.250,00 calcule um aumentode 10%
# Para salários inferiores ou iguais, o aumento será de 15%

s = int(input('Qual o salário do funcionário? R$ '))
if s > 1250:
    novo = (s*1.10)
    ajuste = '10%'
else:
    novo = (s*1.15)
    ajuste = '15%'
print('O salário com a juste de {} é R$ {:.2f}'.format(ajuste,novo))
