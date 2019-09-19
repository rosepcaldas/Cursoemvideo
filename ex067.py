# Faça um programa que mostra a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompidoquando o número for negativo

while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if tab < 0:
        break
    for n in range (1,11):
        print(f'{tab} x {n:2} = {tab*n}')
    print('-'*40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
