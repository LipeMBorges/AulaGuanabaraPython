#comando import+nomedabiblioteca   ai vc consegue adiciona-las...importa todas funcionalidades do modulo
# se colocar from+nomedabiblioteca+import+(nome do objeto especifico dentro da biblioteca)...importa algo especifico do modulo
#exemplo: biblioteca"math":importa algumas funcionalidades matemáticas
#exeo de funcionalidades biblioteca math: ceil(arredonda pra cima), floor(arredonda pra baixo),trunc(elimina casas depois da vírgula),pow(potencia)
#...sqrt(raíz),factorial(fatorial)

#exemplo...quero importar biblioteca math inteira... import math
#quero importar uma coisa so... from math import sqrt
from math import sqrt,floor
num = int(input('Digite um número'))
raiz = sqrt(num)
print('raíz quadrada é:{:.2f}'.format(floor(raiz)))
#bibliotecas matematicas python no site https://docs.python.org/pt-br/3.8/library/numeric.html
import random
#módulo ramdom para número aleatorio
num=random.randint(1, 10)
print(num)
