'''
    EXERCÍCIO 95 - APRIMORANDO OS DICIONÁRIOS
    Aprimore o desafio 093 para que ele funcione com vários jogadores,
    incluindo um sistema de visualização de detalhes do aproveitamento
    de cada jogador.
'''
jogador = dict()
partidas = list()
time = list()
cont = 0
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).upper()
    tot = int(input(f'Quantidade de partidas{jogador["nome"]} jogou? '))
    for i in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {i+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continua = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continua in 'NS':
            break
        else:
            print('ERRO! Digite S ou N')
    if continua == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for j in time:
    print(f'{cont:<2} {j["nome"]:<10} {j["gols"]} {j["total"]}')
    cont +=1

while True:
    while True:
        print('-=' * 60)
        selec = int(input('mostrar dados de qual jogador? '))
        if selec < len(time) or selec == 999:
            break
        else:
            print(f'ERRO! Não existe jogador com cod {selec}! Tente novamente.')
    if selec == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADR {time[selec]["nome"]}:')
    for i, v in enumerate(time[selec]['gols']):
        print(f'   No jogo {i} fez {v} gols.')

#print(f'Foi um total de {jogador["total"]} gols')
