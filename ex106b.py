from time import sleep

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{comando}\'', 'azul')
    titulo('', 'branco')
    help(com)


def titulo(txt, cor):
    tam = len(txt)+4
    codcor = {'limpa': '\n\033[m',
              'verde': '\033[0;30;42m',
              'vermelho': '\033[0;30;41m',
              'amarelo':'\033[0;30;43m',
              'azul':'\033[0;30;46m',
              'branco':'\033[7;30m'
              }
    if len(txt) == 0:
        print(codcor[cor], end='')
    else:
        print(codcor[cor], end='')
        print('~'*tam)
        print(' ',txt)
        print('~'*tam, codcor['limpa'], end='')

comando = ''
while comando != 'fim':
    sleep(0.5)
    titulo('SISTEMA DE AJUDA PyHELP', 'verde')
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() != 'FIM':
        sleep(0.5)
        ajuda(comando)

titulo('ATÉ LOGO !!!', 'vermelho')

