#Faça um programa que leia uma frase pelo teclado e mostre:
#.Quantas vezes aparece a letra "A"
#.Em que posição ela aparece a primeira vez.
#.Em que posição ela aparece a última vez.
frase =input('Digite uma frase').upper()
contador = 0
for letra in frase:
    if letra == 'A':
        contador = contador + 1
print(f'a letra A aparece {contador} vezes na frase')
print('A primeira posição que a letra A aparece é {}'.format(frase.find('A')+1))
print('A última posição que a letra A parece é {}'.format(frase.rfind('A')+1))

