#  Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

numero = randint(1, 5)

escolha = int(input('Escolha um numero aleatório: '))

if escolha == numero:
    print('Você acertou o número aleatório!')
else:
    print(f'Você errou, o número era: {numero}')
