# Crie um programa que leia o nome completo de uma pessoa
# e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo sem considerar espaços
# Quantas letras tem o primeiro nome
print('-'*50)
nome = input('Qual o seu nome completo? ')
print('-'*50)
print('Nome            :', nome)
print('Todas maiúsculas:', nome.upper())
print('Todas minúsculas:', nome.lower())
TCE = len(nome)
TE = nome.count(' ')
TL = TCE - TE
print('Total de letras sem espaço:', TL)
dividido = nome.split()
print(dividido)
print('Numero de letras primeiro nome (',dividido[0],'):',len(dividido[0]))
# print('numero de caracteres', len(nome))
print('-'*50)
