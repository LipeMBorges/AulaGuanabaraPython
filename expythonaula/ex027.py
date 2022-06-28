#Faça um programa que leia o nome completo de uma pessoa,mostrandoo em seguida o primeiro e o último nome separadamente
#EX:Ana Maria de Souza
#primeiro=Ana
#último=Souza
nome = input('Digite uma nome:').split()
comprimento= len(nome)
ultimoC= nome[comprimento-1]
print(f'primeiro nome:{nome[0]}\nultimo nome: {ultimoC}')
#print("seu ultimo nome é:{}".format(nome[len(nome)-1]))
