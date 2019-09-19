'''
    EXERCÍCIO 101 - FUNÇÕES PARA VOTAÇÃO

    Crie um programa que tenha uma função chamada voto() que vai receber
    como parâmetro o ano de nascimento de uma pessoa, retornando um
    valor literal indicando se a pessoa tem voto NEGADO, OPCIONAL ou
    OBRIGATÓRIOnas eleições
'''


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: OBRIGATÓRIO'


nsc = int(input('Em que ano você nasceu? '))
print('-'*30)
print(voto(nsc))
