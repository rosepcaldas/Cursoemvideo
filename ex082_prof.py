num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um númro: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-='*40)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
