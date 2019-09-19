# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor
a = int(input('Numero 1: '))
b = int(input('Numero 2: '))
c = int(input('Numero 3: '))
###########################################
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
###########################################
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
###########################################
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))