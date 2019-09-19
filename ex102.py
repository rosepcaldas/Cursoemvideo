'''
    EXERCÍCIO 102 - FUNÇÃO FATORIAL

    Crie um programa que tenha uma função fatorial() que receba
    dois parâmetros: o primeiro que indique o número a calcular
    e o outro show, que será um valor lógico (opcional) indicando
    se será mostrado ou não na tela o processo de cáluculo do
    fatorial.
'''


def fatorial(numero, show=0):
    '''
    -> Calcula o fatorial de um número.
    :param numero: o número a ser calculado.
    :param show: (opcional) mostra ou nao a conta, True para mostrar.
    :return: retorna o valor do fatorial de um número.
    '''
    fat = 1
    print('-'*40)
    for i in range(numero, 0, -1):
        fat *= i
        if show:
            print(f'{i} ', end='')
            if i == 1:
                print('= ', end='')
            else:
                print('x ', end='')
    return fat


print(fatorial(5, True))
print('-'*40)
help(fatorial)
