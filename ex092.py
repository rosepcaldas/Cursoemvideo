'''
EXERCÍCIO 92 - CADASTRO DE TRABALHADOR EM PYTHON

    Crie um programa que leia nome, ano de nascimento
    e carteira de trabalho e cadastre-os (com idade)
    em um dicionário se por acaso a CTPS for diferente
    de ZERO, o dicionário receberá também o ano de contratação
    e o salário. Calcule e acrecscente, além da idade, com
    quantos anos a pessoa vai se aposentar. aposenta com 35 anos)
'''
from _datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('Carteira ed trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contrato'] = int(input('ano de contraração: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = (dados['contrato'] + 35) - nasc
print('-='*30)
print(dados)
for i, v in dados.items():
    print(f'  - {i} tem o valor {v}')
