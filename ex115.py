'''
    Crie um pequeno sistema modularizado que permita cadastrar
    pessoas pelo seu nome e idade em um arquivo de texto simples.

    O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e
    listar todas as pessoas
'''
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

def cadastro(msg1, msg2):
    print('-' * 30)
    print(f'{"NOVO CADASTRO":^30}')
    print('-' * 30)
    nome = input(msg1)
    idade = leiaInt(msg2)
    idade = str(idade)
    # Criando e escrevendo em arquivos de texto (modo 'w').
    arquivo = open('cadastro.txt', 'a')
    arquivo.write(nome)
    arquivo.write(',')
    arquivo.write(idade)
    arquivo.write('\n')
    arquivo.close()
    print(f'Novo cadastro de {nome} adicionado')

def imprime():
    # Lendo o arquivo criado:
    print('-'*30)
    print(f'{"PESSOAS CADASTRADAS":^30}')
    print('-' * 30)

    arquivo = open('cadastro.txt', 'r')

    for linha in arquivo:
        linha = linha.rstrip()
        print(linha)
    arquivo.close()

while True:
    print('-'*30)
    print(f'{"MENU PRINCIPAL":^30}')
    print('-'*30)
    print('\033[0;32m1 - \033[mVer pessoas cadastradas')
    print('\033[0;32m2 - \033[mCadastrar novas pessoas')
    print('\033[0;32m3 - \033[mSair do sistema')
    print('-' * 30)
    op = input('\033[0;32mSua opção: \033[m').strip()
    if op == '3':
        break
    elif op == '2':
        cadastro('Nome: ', 'Idade: ')
    elif op == '1':
        imprime()
