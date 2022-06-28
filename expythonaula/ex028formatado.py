from random import randint
from time import sleep
computador = randint (0,5)
print('-=-'* 20)
print('Vou pensar em um número entre 0 e 5.Tente advinhar...')
print('-=-'*20)
jogador = int(input('Em que numero pensei ?'))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabens ganhou')
else:
    print('Errou')