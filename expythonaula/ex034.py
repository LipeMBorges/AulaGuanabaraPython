"""
Escreva um programa que pergunte o salário de um funcionáro e calcule o valor do seu aumento.
Para salários superiores a R$1250,00,calcule um aumento de 10%
Para os inferiores ou iguais,o aumento é de 15%.
"""
salario =  float(input('Digite o salário: R$ '))
if salario>1250.00:
    salario = salario+(salario*0.10)
    print(f'Novo salário com aumento de 10% é:{salario}')
else:
    salario = salario+(salario * 0.15)
    print(f'Novo salário com aumento de 15% é:{salario}')

