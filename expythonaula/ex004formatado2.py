c1=input('digite algo:')
print('é um número?{}\né alfanumérico?{}\ntem letra do alfabeto?{}\ntodos os caracteres são ASCII?{}\né um número decimal?{}é um sequência de dígitos?{}\né um indicador python válido?{}\nso tem letras minúculas?{}\né imprimível?{}\nso tem espaço?{}\nsó tem letra maiúscula?{}\nesta capitalizada?{}'
      .format(c1.isnumeric(),c1.isalnum(),c1.isalpha(),c1.isascii(),c1.isdecimal(),c1.isdigit(),c1.isidentifier(),c1.islower(),c1.isprintable(),c1.isspace(),c1.isupper(),c1.istitle()))

