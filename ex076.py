'''
  EXERCÍCIO 76 - LISTA DE PREÇOS EM UMA TUPLA

  Crie um programa que tenha uma tupla única com nomes de produtos e seus preços, na sequência.
  o final, mostre uma listagem de preços, organizados de forma tabular.

'''
listagem = ('Lápis', 1.75,
            'Borracha',2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40} ')
print('-'*40)
for pos in range(0,len(listagem),2):
    print(f'{listagem[pos]:.<30} R$ {listagem[pos+1]:>6.2f}')
print('-'*40)
