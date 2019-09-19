# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
# de artifício, início de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

import emoji

print('====== CONTAGEM FOGOS DE ARTIFÍCIO =====')
for c in range(10,-1, -1):
    print(c)
    sleep(0.75)
print(emoji.emojize(':fire:'*16))
print('BUM!!!   BUM!!!   POW!!!!')
print(emoji.emojize(':fire:'*16))
