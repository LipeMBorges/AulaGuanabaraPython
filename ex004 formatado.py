c1=input('digite algo:')
print(f' é um número?{c1.isnumeric()}\n',f'é alfanumérico?{c1.isalnum()}\n',
      f'é uma letra do alfabeto?{c1.isalpha()}\n',f'todos os caracteres são ASCII?{c1.isascii()}\n',
      f'é um número decimal?{c1.isdecimal()}\n',f'é um sequência de dígitos?{c1.isdigit()}\n',
      f'é um indicador python válido?{c1.isidentifier()}\n',f'so tem letras minúculas?{c1.islower()}\n',
      f'é imprimível?{c1.isprintable()}\n',f'so tem espaço?{c1.isspace()}\n',f'só tem letra maiúscula?{c1.isupper()}\n'
      f' esta capitalizada?{c1.istitle()}\n')



