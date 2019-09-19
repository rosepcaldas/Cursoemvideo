'''
 EXERCÍCIO 75 - ANÁLISE DE DADOS EM TUPLAS

 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
 A) Quantas vezes apareceu o valor 9
 B)Em que posição foi digitado o primeiro valor 3
 C) Quais foram os números pares

'''
tupla = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mas um número: ')),
        int(input('Digite o último número: ')))
print(f'Voce digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes' if tupla.count(9) > 0
      else 'O valor 9 apareceu 0 vezes')
print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posção' if tupla.count(3) > 0
      else 'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram:', end=' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')