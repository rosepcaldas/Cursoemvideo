# Refaça o desafio 00, mostrando a tabuada de im número
# que o usuário encolher, só que agora utilizando o laço for
tab = int(input('Tabuada de: '))
print('-'*14)
for n in range(1,11):
    print('{} x {:2} = {:2}'.format(tab, n, tab*n))
print('-'*14)