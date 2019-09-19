# Programa que leia vários números inteiros pelo teclado
# O programa só vai parar quando o usuário digitar 999, que
# é a condição de parada.
# No final mostre qunatos números foram digitados e qual foi
# a soma entre eles. Desconsiderando o flag
n = cont = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
        cont += 1
        soma += n
        n = int(input('Digite um número [999 para parar]: '))
print('Você entrou com {} números e a soma é: {}'.format(cont, soma))