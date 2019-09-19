# A confederação nacional de natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 25 anos: Sênior
# - Acima master

from datetime import date

cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'verde':'\033[1;32m',
         'roxo':'\033[1;35m',
         'amarelo':'\033[1;33m'}

atual = date.today().year
anonasc = int(input('Ano de nascimento do atleta: '))
idade = atual - anonasc
print('Idade: {}'.format(idade))
if idade <= 9:
    print('Classificação: {}MIRIM{}'.format(cores['amarelo'], cores['limpa']))
elif 9 < idade <= 14:
    print('Classificação:: {}INFANTIL{}'.format(cores['amarelo'], cores['limpa']))
elif idade <= 19:
    print('Classificação:: {}JUNIOR{}'.format(cores['amarelo'], cores['limpa']))
elif idade <= 25:
    print('Classificação:: {}SENIOR{}'.format(cores['amarelo'], cores['limpa']))
else:
    print('Classificação:: {}MASTER{}'.format(cores['amarelo'], cores['limpa']))

