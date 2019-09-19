'''
    EXERCÍCIO 97 - UM PRINT ESPECIAL

    Faça um programa que tenha uma função chamada escreva() e mostre
    uma mensagem com tamanho adaptável.
    Ex. escreva('Olá, Mundo!')
    Saída:
    -----------
    Olá, Mundo!
    -----------
'''
def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'{(txt):^{tam}}')
    print('~' * tam)

escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('Cev')
escreva('olá, Mundo!')