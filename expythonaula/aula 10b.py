'''nome = str(input('Qual seu nome?'))
if nome == 'vegeta':
    print('o princípe dos sayajins')
else:
    print("Guerreiro fraco")
print(f'para a guerra! {nome}')'''
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('sua média foi boa!')
else:
    print('sua média foi ruim')