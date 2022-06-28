"""
Escreva uym programa que leia a velocidade de um carro,se ele ultrapassar 80km/h,
mostre uma mesagem dizendo que ele foi multado .
A multa vai custar R$7,00 por cada Km acima do limite.
"""

veloc =  float(input('Qual velocidade atual do carro?'))
if veloc<=80:
    print('Você está dentro do permitido')
else:
    ultrapassou = veloc - 80
    multa= ultrapassou * 7
    print(f'Você ultrapassou o máximo permitido e terá que pagar uma multa de {multa:.2f} reais.')
