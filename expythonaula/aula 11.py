"""
Ansi
escape sequence
/033[style;text;back m
#olhar print pasta
"""
print('\033[4;31;44mOla, Mundo!\033[m')
#o 7 no style inverte texto e fundo
a = 3
b = 5
print(f'Os valores sao \033[32m{a} e \033[31m{b}\033[m!!!')