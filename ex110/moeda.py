def metade(preço=0, formato=False):
   res = preço / 2
   return res if formato == False else moeda(res)


def dobro(preço=0, formato=False):
   res = preço * 2
   return res if formato == False else moeda(res)


def aumentar(preço=0, taxa=0, formato=False):
   res =  preço * (1 + taxa/100)
   return res if formato == False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
   res = preço - (preço * taxa/100)
   return res if formato == False else moeda(res)

def moeda(preço=0, moeda='R$'):
   return f'{moeda}{preço:.2f}'.replace('.', ',')
   # replace substitui aqui ponto por vírgula

def resumo(preço=0, taxaa=0, taxad=0):
   print('-'*30)
   print('RESUMO DO VALOR'.center(30))
   print('-' * 30)
   print(f'{"Preço analizado:":<20} {moeda(preço):<25}')
   print('-' * 30)
   print(f'Dobro do preço: \t{dobro(preço, True)}')
   print(f'Metade do preço: \t{metade(preço, True)}')
   print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
   print(f'{taxad}% de redução: \t{diminuir(preço, taxad, True)}')
   print('-' * 30)


