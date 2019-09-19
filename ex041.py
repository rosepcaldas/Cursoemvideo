# A confederação nacional de natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 20 anos: Sênior
# - Acima master

import datetime

cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'verde':'\033[1;32m',
         'roxo':'\033[1;35m',
         'amarelo':'\033[1;33m'}

now = datetime.datetime.now()

anonasc = int(input('Ano de nascimento do atleta: '))
idade = now.year - anonasc
print('Idade: {}'.format(idade))
if idade <= 9:
    print('- Até 9 anos: {}MIRIM{}'.format(cores['amarelo'], cores['limpa']))
elif 9 < idade <= 14:
    print('- Até 14 anos: {}INFANTIL{}'.format(cores['amarelo'], cores['limpa']))
elif 14 < idade <= 19:
    print('- Até 19 anos: {}JUNIOR{}'.format(cores['amarelo'], cores['limpa']))
elif 19196 < idade <= 25:
    print('- Até 25 anos: {}SENIOR{}'.format(cores['amarelo'], cores['limpa']))
else:
    print('Acima de 25 anos: {}MASTER{}'.format(cores['amarelo'], cores['limpa']))

