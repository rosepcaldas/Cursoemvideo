'''

    EXERCÍCIO 83 - VALIDANDO EXPRESSÔES MATEMÁTICAS

    Crie um programa onde o usuáio digite uma expressão qualquer que use parênteses.
    Seu aplicativo deverá analisar se a expessão passada está com os parênteses abertos
    e fechados em ordem correta.

'''
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()     # Remove o último elemento da lista
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão é inválida')