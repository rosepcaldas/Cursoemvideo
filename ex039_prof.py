# Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sa idade:
#
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
#
# Se programa também deve mostrar o tempo que falta ou que passou do prazo
print('-'*80)
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('-'*80)
print('Quem nasceu em {:.0f} tem {:.0f} anos em {:.0f}'.format(nasc, idade, atual))
if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    tempo = 18 - idade
    ano = atual + tempo
    print('Ainda faltam {} anos para o alistamento.'.format(tempo))
    print('Seu alistamento será em {:.0f}.'.format(ano))
elif idade > 18:
    tempo = idade - 18
    ano = atual - tempo
    print('Você já deveria ter se alistado há {} anos'.format(tempo))
    print('Seu alistamento foi em {:.0f}.'.format(ano))
print('-'*80)
