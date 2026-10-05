# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.

catetoOposto = float(input('Qual comprimento do cateto oposto: '))
catetoAdjacente = float(input('Qual ocmprimento do cateto adjacente: '))

hipotenusa = ((catetoOposto ** 2 + catetoAdjacente ** 2) ** 0.5)

print(f'A hipotenusa vai medir {hipotenusa}')
