from time import sleep
cor = ('\033[m',        # 0 - sem cores
       '\033[0;30;41m',   # 1 - vermelho
       '\033[0;30;42m',   # 2 - verde
       '\033[0;30;43m',   # 3 - amarelo
       '\033[0;30;44m',   # 4 - azul
       '\033[0;30;45m',   # 5 - roxo
       '\033[7;30m'       # 6 - branco
      )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cor[6])
    help(com)
    sleep(0.5)


def titulo(txt, c):
    tam = len(txt) + 4
    print(cor[c], end='')
    print('~' * tam)
    print(' ', txt)
    print('~' * tam)
    print(cor[0], end='')
    sleep(0.5)

comando = ''
while comando.upper() != 'FIM':
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() != 'FIM':
        sleep(0.5)
        ajuda(comando)
    sleep(0.5)

titulo('ATÉ LOGO !!!', 1)

