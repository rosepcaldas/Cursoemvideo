def mostraMenu():
    print('-' * 30)
    print(f'{"MENU PRINCIPAL":^30}')
    print('-' * 30)
    print('\033[0;32m1 - \033[mVer pessoas cadastradas')
    print('\033[0;32m2 - \033[mCadastrar novas pessoas')
    print('\033[0;32m3 - \033[mSair do sistema')
    print('-' * 30)

def selecionaMenu():
    while True:
        op = input('\033[0;32mSua opção: \033[m').strip()
        if op == '1' or op == '2' or op == '3':
            break
        else:
            print('\033[0;32mErro! Digite uma opção válida!\033[m')
    return op

def cadastro():
    #   verificar se arquivo txt já existe
    import os.path
    os.path.isfile('cadastro.txt')
    try:
        with open('cadastro.txt', 'r') as f:
            processar_arquivo(f)
    except IOError:
        print('Arquivo não encontrado!')

# Programa principal
while True:
    mostraMenu()
    op = selecionaMenu()
    if op == '3':
        break
    elif op == '2':
        cadastro('Nome: ', 'Idade: ')
    elif op == '1':
        imprime()