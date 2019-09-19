def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',','.').strip())
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número Real válido.\033[m')
            return n
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados')
            return 0
        else:
            return n


i = leiaInt('Digite um número: ')
r = leiaFloat('Digite um número real: ')
print(f'O número interio foi {i} e o real foi {r:.2f}')

