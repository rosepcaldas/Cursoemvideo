# Programa que leia uma frase e diga se é um palíndromo
# desconsiderando os espaços.
# pode ser lida de trás para frente.
# ex: apos a sopa
c = 0
cont = 0
f = str(input('Frase: '))
F = f.upper()
F = ''.join(F.split())
tamanhoF = len(F)
print('fraze: {}, {}: {}'.format(f, F, tamanhoF))
for c in range(0,tamanhoF):
    x = tamanhoF-c-1
    if F[x] == F[c]:
        cont = cont + 1
if cont == tamanhoF:
    print('A frase é um palídromo.')
else:
    print('A frase NÃO é um palídrmo')

#fi = [f::-1]
#print(fi)