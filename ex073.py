'''
    EXERCÍCIO 73

    Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato
    Brasileiro, na ordem de colocação. Depois mostre:
    A) Apenas os 5 primeiros colocados
    B) os ùltimos 4 colocados da tabela
    C) Uma lista com os times em ordem alafabética
    D) Em que posição na tabela está o time da Chapecoense
'''
print('-='*30)
times = ('Palmeiras', 'Atlético-MG', 'Santos', 'Flamengo',
         'Internacional', 'Bahia', 'Botafogo', 'São Paulo',
         'Corinthians', 'Athletico-PR', 'Ceará', 'Goiás',
         'Chapecoense', 'Fortaleza', 'Cruzeiro', 'Fluminense',
         'CSA', 'Grêmio', 'Avaí', 'Vasco')
print(f'Lista de times do Brasileirão: {times}')
print('-='*30)
print(f'Os 5 primeiros colocados: {times[0:5]}')
print('-='*30)
print(f' Os últimos 4 colocados são: {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}') # Exibe em ordem alfabetica, mas não muda a ordem da tupla
print('-='*30)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
