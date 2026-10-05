# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Qual ano você quer analisar: '))

if ano % 400 == 0:
    print(f'{ano} é bissexto')
elif ano % 100 == 0:
    print(f'{ano} não é bissexto (divisível por 100, mas não por 400)')
elif ano % 4 == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')
