# Crie um programa que leia duas notas de um aluno e calcule sua média
# mostrando uma msg no final, de acordo com a média atingida.
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'verde':'\033[1;32m',
         'roxo':'\033[1;35m',
         'amarelo':'\033[1;33m'}
print('-'*80)
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
print('-'*80)
print('Sua média foi: {}{:.2f}{}'.format(cores['roxo'], media, cores['limpa']))
if media < 5:
    print('Média abaixo de {}5.0{}: {}REPROVADO{}'.format(cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa']))
elif 5 <= media < 7:
    print('Média entre {}5.0 e 6.9{}: {}RECUPERAÇÃO{}'.format(cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa']))
elif media >= 7:
    print('Média {}7.0{} ou superior: {}APROVADO{}'.format(cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa']))
