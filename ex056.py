# Programa que leia:
# nome, idade e sexo de 4 pessoas.
# No final mostre
# - Média de idade do grupo
# - Qual o nome do homem mais velho
# - Quantas mulheres tem menos de 20 anos
#
MaisVelho=0
contM = 0
soma = 0
for c in range(0,5):
    Nome = str(input('Nome: '))
    Sexo = int(input('Sexo (1-Masc e 2- Fem): '))
    Idade = int(input('Idade: '))
    soma = soma + Idade
    if Sexo == 1:
        if MaisVelho <= Idade:
            MaisVelho = Idade
            NomeMV = Nome
    if Sexo == 2:
        if Idade < 20:
            contM = contM + 1
    if Sexo != 1 and Sexo !=2:
            print('Valor inválido para sexo')
media = soma / 5
print('Média do grupo: {}'.format(media))
print('{} é o homem mais velho e sua idade é {}'.format(NomeMV, MaisVelho))
print('Este grupo tem {} mulheres com menos de 20 anos'.format(contM))
