# Escreva um programa que leia dois numeros inteiros e compare-os,
# mostrando na tela uma mensagem:
# - O preimiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguas
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('-'*80)
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número : '))
print('-'*80)
if n1 > n2:
    print('O {}primeiro valor{} é o {}maior'.format(cores['amarelo'],cores['limpa'],cores['azul']))
elif n2 > n1:
    print('O {}segundo valor{} é o {}maior'.format(cores['amarelo'], cores['limpa'], cores['azul']))
else:
    print('{}Não existe{} valor maior, os dois são {}IGUAIS'.format(cores['amarelo'], cores['limpa'], cores['azul']))
