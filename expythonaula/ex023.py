#Faça um programa que leia um número ode 0 a 9999 e mostre na tela cada um dos dígitos separados.
#ex:Digite um número:1834
#unidade:4
#dezena:3
#centena:8
#milhar:1
#tentar fazer matematicamente e como string


numero = int(input('Digite um numero inteiro positivo: '))
unidade = numero // 1  % 10
dezena = numero//10 % 10
centena = numero // 100 % 10
milhar =  numero //1000 % 10

print(f'Analisando o {numero}, temos:\nunidade:{unidade}\ndezena {dezena}\ncentena:{centena}\nmilhar:{milhar}')