'''
    EXERCÍCIO 72

    Crie um programa que tenha uma tupla totalmente preenchida com uma
    contagem por extenso, de zero até vinte.
    Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.

'''
extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
numero = int(input('Entre com um número entre 0 e 20: '))
while numero < 0 or numero > 20:
    numero = int(input('Tente novamente. Entre com um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[numero]}')
