"""
Desenvolva um programa que leia o comprimeto de três retas
e diga ao usuário se elas podem ou ão formar um triângulo
"""
reta1 = int(input('Comprimento da primeira reta: '))
reta2 = int(input('Comprimento da segunda reta: '))
reta3 = int(input('Comprimento da terceira reta: '))

if (reta1 + reta2)>reta3 and (reta3+reta1)>reta2 and (reta2+reta3)>reta1:
    print('É triângulo')
else:
    print('Não e triangulo')
