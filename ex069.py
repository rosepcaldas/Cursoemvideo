# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deveráperguntar se o usuário
# quer ou não continuar.
# No final, modetre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantas são Homens
# C) Quantas mulheres tem menos d 20anos
c_idade = c_homem = c_mulher_20 = 0
while True:
    print('-'*40)
    print('***** CADASTRE UMA PESSOA *****')
    print('-'*40)
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if sexo in 'FM':
            break
    if idade >= 18:
        c_idade += 1
    if sexo == 'M':
        c_homem += 1
    elif sexo == 'F' and idade < 20:
        c_mulher_20 += 1
    print('-'*40)
    while True:
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continua in 'NS':
            break
    if continua == 'N':
        break
print('========== FIM DO PROGRAMA ============')
print(f'Total de pessoas com mais de 18 anos: {c_idade}')
print(f'Ao todo temos {c_homem} homens cadastrados')
print(f'E temos {c_mulher_20} mulheres com menos de 20 anos')