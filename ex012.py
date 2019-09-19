# Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço, com 5% de desconto
print('-'*60)
print('Cálculo de 5% de desconto no preço do produto')
print('-'*60)
p = float(input('Qual o preço do produto? R$ '))
np = p - (p * 5 /100)
print('O novo preço com 5% de descoto é: {:.2f}'.format(np))
print('-'*60)