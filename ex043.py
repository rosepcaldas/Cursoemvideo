# Desenvova uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC mostrando seu status de acordo coma tabela abaixo:
#
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - Entre 25 a 30: Sobrepeso
# - Entre 30 a 40: Obesidade
# - Acima de 40: Obesidade móbida
#
#   IMC = peso / altura**2
#

cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m'}

print('-'*80)
peso = float(input('Qual o peso?  (kg): '))
altura = float(input('Qual altura? (m):'))
IMC = peso/(altura**2)
print('-'*80)
print('TABELA DE IMC')
print(' - Abaixo de 18.5: Abaixo do peso')
print(' - Entre 18.5 e 25: Peso ideal')
print(' - Entre 25 a 30: Sobrepeso')
print(' - Entre 30 a 40: Obesidade')
print(' - Acima de 40: Obesidade móbida')
print('-'*80)
print('{}IMC: {:.1f}{} '.format(cores['azul'],IMC,cores['limpa']), end='')
if IMC < 18.5:
    print('{}Abaixo do peso normal{}'.format(cores['amarelo'], cores['limpa']))
elif 18.5 <= IMC < 25:
    print('{}Peso ideal{}'.format(cores['verde'], cores['limpa']))
elif 25 <= IMC < 30:
    print('{}Sobrepeso{}'.format(cores['amarelo'], cores['limpa']))
elif 30 <= IMC < 40:
    print('{}obesidade{}'.format(cores['vermelho'], cores['limpa']))
else:
    print('{}Obesidade mórbida{}'.format(cores['vermelho'], cores['limpa']))
print('-'*80)
