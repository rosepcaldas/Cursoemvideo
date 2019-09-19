# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos digitos separados.
# Ex: 1834
# unidade: 4
# dezena : 3
# centena: 8
# milhar : 1


n = input('Entre com um número de 0 a 9999: ')

print('-'*40)
print('Usando solução de fatiamento de string')
print('-'*40)

print('unidade :', n[3])
print('dezena  :', n[2])
print('centena :', n[1])
print('milhar  :', n[0])

print('-'*40)
print('Usando solução matemática')
print('-'*40)
nu = float(n)
nu1 = nu//1000
nu2 = (nu-(nu1*1000))//100
rnu = nu%1000
nu3 = (rnu-(nu2*100))//10
nu4 = rnu%10

print('unidade :{:.0f}'.format(nu4))
print('dezena  :{:.0f}'.format(nu3))
print('centena :{:.0f}'.format(nu2))
print('milhar  :{:.0f}'.format(nu1))

print('-'*40)