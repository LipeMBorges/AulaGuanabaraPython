#Faça um programa que leia um número ode 0 a 9999 e mostre na tela cada um dos dígitos separados.
#ex:Digite um número:1834
#unidade:4
#dezena:3
#centena:8
#milhar:1
#tentar fazer matematicamente e como string


numero = int(input('Digite um numero inteiro positivo: '))

    # Extraindo a unidade
    unidade = numero % 10

    # Eliminando a unidade de nosso número
    numero = (numero - unidade)/10

    # Extraindo a dezena
    dezena = numero % 10

    # Eliminando a dezena do número original, fica a centena
    numero = (numero - dezena)/10
    centena = numero

    # Fazendo ser inteiros
    dezena = int(dezena)
    centena = int(centena)
    print(centena,'centena(),',dezena,'dezena() e',unidade,'unidade()')