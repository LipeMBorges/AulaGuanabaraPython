"""
Faça um proigrama que leia um ano qualquer e mostre se ele é bissexto
"""
from calendar import isleap
ano = int(input('Digite o ano'))
if isleap(ano):
    print('É bissexto')
else:
    print('Não é bissexto')