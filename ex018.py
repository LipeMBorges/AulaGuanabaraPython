#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,cosseno e tangente desse ângulo.
import math
angulo=float(input('Digite um ângulo: '))
radianos=math.radians(angulo)
print(f'o seu seno é: {math.sin(radianos):.2f} ,seu cosseno é {math.cos(radianos):.2f}, e a sua tangente é: {math.tan(radianos):.2f}')

