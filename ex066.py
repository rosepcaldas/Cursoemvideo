# Crie u programa que leia vários números inteiros pelo teclado.
# O programa só vai para quando o usuário digitar o valor 999,
# que é a condição de parada.
# no final mostre quantos números foram digitados e qual foi a soma
# entre eles (desconsiderando o flag
cont = soma = 0
while True:
    número = int(input('Digite um valor (999 para para): '))
    if número == 999:
        break
    cont += 1
    soma += número
print(f'A soma dos {cont} valores foi {soma}!')
