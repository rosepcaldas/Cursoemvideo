# AZUL = \033[0;30;44m
# VERDE = \033[0;30;42m
# BRANCO = \033[40m
# LIMPA = '\033[m'
#print('\033[0;30;44mAZUL')
#print('\033[0;30;42mVERDE')
#print('\033[0;30;41mVERMELHO')
#print('\033[40mBRANCO')
#print('\033[mLIMPA')
def titulo(txt,cor):
    tam = len(txt)+4
    if cor == 'verde':
        ce = '\033[0;30;42m'
    if cor == 'azul':
        print('\033[0;30;44m~'*tam)
    print(f'{ce}~' * tam)
    print(' ',txt)
    print(f'{ce}~' * tam)

#while True:
titulo('SITEMA DE AJUDA PyHELP', 'verde')


