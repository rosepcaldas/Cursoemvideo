# Faça um programa que leia o sexo de uma pessoa, mas só aceite
# os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até# ter um
# valor correto
#
#while sexo != 'M' and 'F' != sexo:
sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Informe seu sexo [M/F]: ')).strip().upper()[0]
    # este último comando [0] faz um fatiamento pegando só a primeira letra em maiúsculo
print('Sexo {} registrado com sucesso'.format(sexo))
