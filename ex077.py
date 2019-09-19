'''

    EXERCÍCIO 77 - CONTANDO VOGAIS EM TUPLA

    Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
    Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.

'''
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'futuro')
for n in range(0, len(palavras)):
    print(f'Na palavra {palavras[n].upper()} temos', end=' ')
    palavra_a = (palavras[n]).strip().upper()         # variável recebe o valor da palavra que será analisada
    for c in range(0,len(palavra_a)):
        if 'A' in palavra_a[c] or 'E' in palavra_a[c] or 'I' in palavra_a[c] or 'O' in palavra_a[c] or 'U' in palavra_a[c]:
            print(f'{palavra_a[c].lower()}', end=' ')
        if c == len(palavra_a)-1:
            print('')

