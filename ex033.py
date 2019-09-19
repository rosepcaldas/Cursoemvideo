# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor
n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))
###########################################
if n1>n2:
    n=n1
else:
    if n2>n3:
        n=n2
    else:
        n=n3
##########################################
if n1<n2:
    m=n1
else:
    if n2<n3:
        m=n2
    else:
        m=n3
print('entre {}, {}, {}: o maior número é {} e o menor é {}'.format(n1, n2, n3, n, m))