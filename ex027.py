# Programa que leia o nome da pessoa e , mostrando em
# seguida o primeiro e o último nome separadamente.
# Ex. Ana Maria de Souza
# primeiro = Ana
# Último = Souza

nome = str(input('Nome completo: ')).strip()
nome1 = nome.split()
n = len(nome1)
#print(n)
print('Primeiro nome: {}'.format(nome1[0]))
print('Último nome  : {}'.format(nome1[n-1]))
