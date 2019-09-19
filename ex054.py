# Programa que leia o ano de nascimento de 7 pessoas e
# No final diga quantas atingiram a maioridade
from datetime import date
atual = date.today().year
contador = 0
for c in range(0,7):
    nasc = int(input('Ano de nascimenro: '))
    idade = atual - nasc
    if idade >= 21:
        contador += 1
print('Entre as 7 pessoas {} atingiram a moioridade e {} ainda não atingiram.'.format(contador, 7-contador))
