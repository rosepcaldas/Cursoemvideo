from time import sleep


def titulo(txt, cor):
    tam = len(txt)+4
    limpa = '\n\033[m'
    if cor == 'verde':
        codcor = '\033[1;30;42m'
    if cor == 'vermelho':
        codcor = '\033[1;30;41m'
    if cor == 'amarelo':
        codcor = '\033[1;30;43m'
    if cor == 'azul':
        codcor = '\033[1;30;46m'
    if cor == 'branco':
        codcor = '\033[1;40m'
        print(codcor, end='')
    else:
        print(codcor, end='')
        print('~'*tam)
        print(' ',txt)
        print('~'*tam, limpa, end='')

x=''
while x != 'fim':
    titulo('SISTEMA DE AJUDA PyHELP', 'verde')
    x = input('Função ou biblioteca > ').lower()
    if x != 'fim':
        titulo(f"Acessando manual do comando '{x}'", 'azul')
        sleep(0.5)
        titulo('', 'branco')
        help(x)

titulo('ATÉ LOGO !!!', 'vermelho')

