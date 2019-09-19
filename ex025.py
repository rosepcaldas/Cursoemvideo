# Crie programa que leia o nome de uma pessoa e diga
# se ela tem 'SILVA" no nome


print('-'*40)
nome = str(input('Qual o seu nome completo? ')).strip()
print('O nome tem Silva? ','SILVA' in nome.upper())