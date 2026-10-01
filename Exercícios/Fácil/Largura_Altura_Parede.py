# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Largura da parede: '))
Altura = float(input('Altura da parede: '))
Area = largura * Altura
Litros = Area / 2 

print(f'Sua parede tem dimensão de {largura}x{Altura} e sua área é de {Area}m².')
print(f'Para pintar essa parede você precisará de {Litros}L de tinta.')
