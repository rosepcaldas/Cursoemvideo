# Programa que leia uma frase e diga se é um palíndromo
# desconsiderando os espaços.
# pode ser lida de trás para frente.
# ex: apos a sopa

frase = str(input('Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if junto == inverso:
    print('A frase é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')
print('-'*40)
print('Frase: {}'.format(frase))
print('Split: {}'.format(palavras))
print('Join: {}'.format(junto))
print('Inverso: {}'.format(inverso))

