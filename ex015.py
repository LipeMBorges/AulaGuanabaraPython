#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado.Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

distancia=float(input('Quantos Km o carro andou? '))
dias=float(input('Quantos dias usou? '))
print(f'preço a pagar {(60*dias)+(0.15*distancia):.2f}')
