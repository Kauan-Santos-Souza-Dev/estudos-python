# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Quanto custa o produto? '))
desconto =  produto - (produto * 5 / 100)

print(f'O produto que custava R${produto}, com desconto de 5% vai custar {desconto}')
