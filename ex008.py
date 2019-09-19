# Escreva um programa que leia um número em metros e o exiba convertido em centímetros e milimetros
print('===== DESAFIO 8 =====')
print('Conversão de unidades')
print('=====================')
n = float(input('Entre com o valor em metros: '))
km = (n / 1000)
hm = (n / 100)
dam = (n / 10)
dm = (n * 10)
cm = (n * 100)
mm = (n * 1000)
print('a medida de {} corresponde a'
      '\n{} km'
      '\n{} hm'
      '\n{} dam'
      '\n{:.0f} dm'
      '\n{:.0f} cm'
      '\n{:.0f} mm'.format(n, km, hm, dam, dm,cm, mm))
