'''
    EXERCÍCIO 103 - Ficha Jogador

    Faça um programa que tenha uma função chamada ficha(), que
    receba dois parâmetros opcionais: o nome de um jogador e
    quantos gols ele marcou.
    O programa deverá ser capaz de mostrar a ficha do jogador,
    mesmo que algum dado não tenha sido informado corretamente.
'''
def ficha(jogador=0, gols=0):
    if jogador == '':
        jogador = '<desconhecido>'
    if gols == '':
        gols = 0
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato.'



j = input('Nome do jogador: ')
g = input('Número de Gols: ')
print(ficha(j, g))
