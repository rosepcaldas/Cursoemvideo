# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$ 7,00 por cada km acima do limite
print('-'*80)
v = int(input('Velocidade (km/h): '))
print('-'*80)
if v > 80:
    multa = (v-80) * 7
    print('MULTADO! Você excedeu o limite permitido de 80Km/h e pagará uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
print('-' * 80)