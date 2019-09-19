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

def leiaReal(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).replace(',','.').strip()
        try:
            valor = float(n)
            ok = True
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados')
        except:
            print('\033[0;31mERRO! Digite um número Real válido.\033[m')
        if ok:
            break
    return valor

i = leiaInt('Digite um número: ')
r = leiaReal('Digite um número real: ')
print(f'O número interio foi {i} e o real foi {r:.2f}')
