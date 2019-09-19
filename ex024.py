# Crie um programa que leia o nome
# de uma cidade e diga se ela começa com o
# nome "SANTO".

print('-'*40)
cidade = str(input('Entre com o nome da cidade: '))

cidade2 = cidade.upper().split()

print('sua cidade começa com SANTO:','SANTO' in cidade2[0])
print('-'*40)
print('Resolução do profesor')
print('-'*40)

cid = str(cidade).strip()
print(cid[:5].upper() == 'SANTO')
