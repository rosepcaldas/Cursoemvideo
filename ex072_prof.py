'''
    EXERCÍCIO 72

    Crie um programa que tenha uma tupla totalmente preenchida com uma
    contagem por extenso, de zero até vinte.
    Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.

'''
while True:
    extenso = ('zero', 'um', 'dois', 'três', 'quatro',
               'cinco', 'seis', 'sete', 'oito', 'nove',
               'dez', 'onze', 'doze', 'treze', 'quatorze',
               'quinze', 'dezesseis', 'dezessete', 'dezoito',
               'dezenove', 'vinte')
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {extenso[numero]}')
    continua = str(input('Quer continuar? [S,N]')).strip().upper()[0]
    if continua == 'N':
        break
