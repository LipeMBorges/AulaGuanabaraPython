#escreva um programa que leia um valor em metros e o exiba covertido em centimetros e milímetros.
#km->hm->dam->m->dm->cm->mm
valor=float(input('digite o valor em metros, para sua conversão: '))
print(f'O valor convertido em kilômetros:{valor*0.001:.2f}\nE em hectômetro: {valor*0.01:.2f}\nOvalor convertido em decâmetro:{valor*0.1:.2f}\nOvalor convertido em decímetro:{valor*10:.2f}\nO valor convertido em centímetros:{valor*100:.2f}\nE em milímetros: {valor*1000:.0f}\n')
