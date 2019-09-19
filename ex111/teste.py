from ex111.utilidadesCev import moeda, dado


p = dado.leiaDinheiro('Digite o preço: R$ ')
print(f'Você acabou de digitar o número {p}')
moeda.resumo(p, 80, 35)