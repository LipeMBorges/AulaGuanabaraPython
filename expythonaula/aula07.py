#operadores aritmeticos:  +,-,*,/,//(divisao inteira),**(potencia),%(resto da divisao)
#Ordem de resolução: ()-->**-->*,/,//,%-->+,-
#== significa igual...e = significa recebe
#pow(4,3) --> outra forma de fazer potencia
#raiz quaddrada de um numero...exemplo: 81**(1/2)
#raiz cubica == 81**(1/3)

nome=input('qual seu nome?')
print('prazer em te conehcer {:>20}!'.format(nome))
# o : coloca espaço e o <> colcoa antes ou depois de...X
#^é para centralizar

# se fizer expressao por exemplo ...print('='*3) ele da ===
print('='*7)
peso=int(input('seu peso'))
print('seu peso é:{:=^20}'.format(peso))

n1=int(input('um valor:'))
n2=int(input('outro valor:'))
print(f'a soma vale:{n1+n2}')
#caso não precise criar uma variavel para mostrar depois, apenas o calculos, ja pode pode fazer direto assim

n3=int(input('digite um número:'))
n4=int(input('digite outro número:'))
s = n3 + n4
m = n3 * n4
d = n3 / n4
di = n3 // n4
e = n3 ** n4
print(f'o resultado da soma é:{s},o resultado da multiplicação é:{m}, e o da divisão é:{d}',end='')
print(f'divisão inteira{di:.3f}, e potência{e}')
#o  :.3f significa que quer colocar apenas 3 pontos flutuantes...casas após a vírgula, oq tiver nas aspas vai mostrar ao final da linha também
#end='' significa que a linha continua ali inves de pular