frase = '                Curso em Vídeo Python'
print(frase[1:15:2])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('C'))
#ultima linha esta mandando contar quantos tem da letra dentro de uma frase transformada em maiuscula
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python','Android'))
print(frase)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])


