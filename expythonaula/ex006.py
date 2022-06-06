#crie um algoritmo que leia um número e mostre o seu dobro,triplo e raiz quadrada.

budega=int(input('digite um número:'))
print(f'o dobro do número que digitou é: {budega*2}\no triplo é: {budega*3}\ne a raiz quadrada é: {budega**(1/2):.2f}',end=':D')
#:.0f para deixar 3 no resultado inves de 3.0
#raiz quadrada tb poderia ter sido feita assim... pow(budega,(1/2))


