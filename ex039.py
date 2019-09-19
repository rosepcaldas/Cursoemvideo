# Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sa idade:
#
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
#
# Se programa também deve mostrar o tempo que falta ou que passou do prazo
import datetime

print('-'*80)
ano = int(input('Ano de nascimento: '))
print('-'*80)
now = datetime.datetime.now()
idade = now.year - ano
print('Sua idade é: {:.0f} anos'.format(idade))
print('')
if idade > 18:
    tempo = idade - 18
    print('O tempo de alistamento já passou {} anos'.format(tempo))
elif idade < 18:
    tempo = 18 - idade
    print('Faltam {} anos para o alistamento.'.format(tempo))
elif idade == 18:
    print('já está na hora de se alistar')

