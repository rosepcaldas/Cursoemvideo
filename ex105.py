'''
    EXERCÍCIO 105 - ANALISANDO E GERANDO DIICONÁRIOS

    Faça um programa que tenha uma função notas() que pode receber
    várias notas de alunose vai retornar um dicionário com as seguites
    informações.
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)
    Adicionar também as docstrings da função.
'''


def notas(* n, sit=0):
    """
    -> função para analisar notas e situações de vários alunos
    :param valores n: uma ou mais notas dos alunos (aceita várias)
    :param valores sit: valor opcinal, indicando se deve ou não adiconar situação
    :return: dicionário com várias informações sobre situação da turma
    """
    total = len(n)
    media = sum(n)/len(n)
    maior = max(n)
    menor = min(n)
    if sit:
        if media >=7:
            situacao = 'boa'
        elif 7 > media >= 5:
            situacao = 'razoável'
        else:
            situacao = 'ruim'
        return {'total': total, 'maior': maior, 'menor': menor, 'média:': media, 'situação: ': situacao}
    else:
        return {'total': total, 'maior': maior, 'menor': menor, 'média:': media}


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print('-'*80)
print(resp)
print('-'*80)
help(notas)
