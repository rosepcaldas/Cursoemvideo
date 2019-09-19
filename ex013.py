# Faça um algoritmo que lê o salário de um funcionário e mostre
# seu novo salário com 15% de aumento.
print('-'*40)
print('Cálculo de 15% de aumento em salário')
print('-'*40)
sal = float(input('Qual o salário do funcionário? R$ '))
nsal = sal+(sal*15/100)
print('O salário com 15% de acréscimo fica R$ {:.2f}'.format(nsal))
