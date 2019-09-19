'''
    EXERCÍCIO 75

    Desenvolva um programa que leia quatro valores pelo teclado e guarde-osem uma tupla. No final mostre:
    A) Quantas vezes apareceu o valor 9
    B)Em que posição foi digitado o primeiro valor 3
    Quais foram os números pares

'''
temnove = temtres = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mas um número: '))
n4 = int(input('Digite o último número: '))
tupla = (n1, n2, n3, n4)
print(f'Voce digitou os valores {tupla}')
for c in tupla:
    if c == 9:
        temnove +=1
    if c == 3:
        temtres += 1
print(f'O valor 9 apareceu {tupla.count(9)} vezes' if temnove > 0 else 'O valor 9 apareceu 0 vezes')
print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posção' if temtres > 0 else 'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram:', end=' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')