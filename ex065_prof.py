# Programa que leia n numeros inteiros e mostre:
# média, maior e menor valor
# pergunte ao usuário se ele quer ou não continuar
continuar = 'S'
cont = soma = maior = menor = 0
while continuar in 'Ss':
    n = int(input('Entre com o número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = (str(input('Quer continuar? [S/N] '))).upper().strip()[0]
media = soma / cont
print('-'*60)
print('Maior número: {}'.format(maior))
print('Menor número: {}'.format(menor))
print('Você entrou com {} números e a média é: {:.2f}'.format(cont,media))
print('-'*60)
