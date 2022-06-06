#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
#ex:digite um número:6127
#O número 6.127 tem a parte inteira 6.
#dica:olhar módulo math
import math
n1=float(input('digite um número real:'))
print(f'a parte inteira é:{math.trunc(n1)}')
#sem o import daria pra usar ...print(f"a parte inteira eh{int(n1)"}')