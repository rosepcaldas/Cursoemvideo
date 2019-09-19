'''
    EXERCÍCIO 93 - Cadastro de jogador de Futebol

    Crie um programa que gerencie o aproveitamento de um jogador de futebol.
    O programa vai ter o nome do jogador e quantas partidas ele jogou.
    Depois vai ler a quantidade de gol feitos em cada partida.
    No final, tudo isso será mostrado em um dicionário, incluindo o total
    de gols feitos durante o campeonato.
'''
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantidade de partidas{jogador["nome"]} jogou? '))
for i in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {i+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for i, v in jogador.items():
    print(f'O campo {i} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')
