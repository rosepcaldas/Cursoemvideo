# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparede 'A'
# Em que posição ela aparece A primeira vez
# Em que posição ela aparece A última vez

frase = str(input('Entre com a frase: ')).strip()

print('Frase: {}'.format(frase))
print('A letra A aparece {} vezes'.format(frase.upper().count('A')))
print('A letra a aparece A primeira vez na posição: {}'.format((frase.upper().find('A')+1)))
print('A letra a aparece A última vez na posição: {}'.format((frase.upper().rfind('A'))+1))