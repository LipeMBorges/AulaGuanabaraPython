#Crie um programa que leia o nome completo de uma pessoa e mostre:
#-O nome com todas as letras maiúsculas;
#-O nome com todas minúsculas;
#-Quantas letras tem o nome inteiro sem espaços;
#-Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' ')) # subtrai os espaços procurados pelo .count da frase, e conta quantos tem no total c o len
dividido = nome.split()
print(f'O seu o primeiro nome nome eh {dividido[0]} , e possui  possui {len(dividido[0])} letras')
print(f'o seu primeiro nome tem {nome.find(" ")} letras')# se der espaço antes de digitar primeiro nome da erro











