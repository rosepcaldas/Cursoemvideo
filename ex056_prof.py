3# Programa que leia:
# nome, idade e sexo de 4 pessoas.
# No final mostre
# - Média de idade do grupo
# - Qual o nome do homem mais velho
# - Quantas mulheres tem menos de 20 anos
#
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('------ {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('Média de idade do grupo: {}'.format(mediaidade))
print('{} é o homem mais velho e sua idade é {}'.format(nomevelho, maioridadehomem))
print('Este grupo tem {} mulheres com menos de 20 anos'.format(totmulher20))
