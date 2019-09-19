'''
    EXERCÍCIO 90 - DICIONÁRIO EM PYTHON

    Faça um exercício que leia nome e média e um aluno, gurdando também
    a situação em um dicionário.
    No final, mostre o conteúdo da estrutura na tela
'''

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >=7.0:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7.0:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*40)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')


