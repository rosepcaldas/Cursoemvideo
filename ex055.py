# Programa que leia o peso de 5 pessoas e ao final
# diga qual foi o maior e o menor pesos lidos
MaiorPeso = 0
MenorPeso = 0
for p in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        MaiorPeso = peso
        MenorPeso = peso
    else:
        if peso > MaiorPeso:
            MaiorPeso = peso
        if peso < MenorPeso:
            MenorPeso = peso
print('O maior peso é: {}kg'.format(MaiorPeso))
print('O menor peso é: {}kg'.format(MenorPeso))