# Soma entre númers ímpares que são múltiplos de 3
# e que se encontram no intervalo entre 1 e 500
soma = 0
soma3 = 0
cont = 0
print('='*80)
for n in range(1,501,1):
#    print(n, end=' ')
    s2 = n % 2  # Se o número for multiplo de 2 sobra = zero
    s3 = n % 3  # Se o número for multiplo de 3 sobra = zero
    #print('sobras {} e {}'.format(s2,s3))
    if s3 == 0 and s2 != 0:
        soma = soma + n
print('Soma:{}'.format(soma))
#######################################################
# forma mais eficiente
#######################################################
print('='*80)
for c in range(1,501,2):
    if c % 3 == 0:
        soma3 += c # contador
        cont += 1    # acumulador
print('A SOMA DE TODOS OS {} VALORES SOLICITADOS É: {}'.format(cont,soma3))
print('='*80)
