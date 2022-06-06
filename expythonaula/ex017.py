#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,calcule e
# mostre o comprimento da hipontenusa.
import math
cat1=float(input('digite o valor do cateto oposto:'))
cat2=float(input('digite o valor do cateto adjacente'))
print(f'a hipotenusa é: {math.hypot(cat1,cat2):.2f}')
#print(f'a hipotenusa é: {math.sqrt(cat1*cat1 + cat2*cat2)}')
#hip=(co ** 2 + ca ** 2) ** (1/2)