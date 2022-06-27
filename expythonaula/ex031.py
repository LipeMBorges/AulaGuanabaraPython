"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem,cobrando R$0.50 por Km para viagens de até 200Km
e R$0.45 para viagens mais longas
"""

distancia = float(input('Qual distância  da viagem em KM? '))
if distancia <= 200:
    valor = 0.50 * distancia
    print(f'Total a pagar é {valor}')
else:
    valor = 0.45 * distancia
    print(f'Total a pagar é {valor}')

