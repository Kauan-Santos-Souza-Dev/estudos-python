# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
nome1 = str(input('Nome 1:'))
nome2 = str(input('Nome 2:'))
nome3 = str(input('Nome 3:'))
nome4 = str(input('Nome 4:'))

nomes = [nome1,nome2,nome3,nome4]
shuffle(nomes)
print(nomes)
