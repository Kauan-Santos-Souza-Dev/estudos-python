# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Existem algumas formas de se resolver
# Forma 1: Pensada por mim:

# numero = float(input('Digite um numero: '))
# porcao = numero // 1

# print(f'{porcao}')

# Forma 2: 
'''
from math import trunc 

num = float(input('Digite um valor: '))
inteiro = trunc(num)

print(f'O valor digitado {num} sua porçao inteira é {inteiro}')
'''

# Forma 3: Função interna do Python

'''
num = float(input('Digite um valor: '))
valor = int(num)

print(f'O valor digitado {num} sua porçao inteira é {valor}')

'''



