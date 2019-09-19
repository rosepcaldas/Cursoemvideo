'''
    EXERCÍCIO 87 - MAIS SOBRE MATRIZ EM PYTHON

    Aprimore os desafio anterior, mostrando no final:

    A) A soma de todos os valores digitados
    B) A soma dos vlores da terceira coluna
    C) O maior valor da segunda coluna
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum = sumpar = maxl2 = 0
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para [{lin}, {col}] '))
        if col == 2:
            sum += matriz[lin][col]
        if matriz[lin][col] % 2 == 0:
            sumpar += matriz[lin][col]
        if lin == 1 and matriz[lin][col] > maxl2:
            maxl2 = matriz[lin][col]
print('-='*30)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[ {matriz[lin][col]:^5} ]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {sumpar}')
print(f'a soma da terceira coluna é {sum}')
print(f'O maoir valor da segunda coluna é {maxl2}')
