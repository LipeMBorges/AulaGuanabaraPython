'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
peça para o usuário tennntar descobrir qual foi o númeroescolhido pelo computador
o programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random

num= int(random.uniform(1,5))
#num=random.randrange(6)#0-5
num2 = int(input('Digite um número de 1 ate 5 e tente acertar a escolha da máquina!:'))
if num == num2:
    print('parabéns você acertou o número')
else:
    print(f'O número escolhido foi {num} , vc perdeu! ')

