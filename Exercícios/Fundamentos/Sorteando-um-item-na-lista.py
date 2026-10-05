# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

nome1 = str(input('Nome 1:'))
nome2 = str(input('Nome 4:'))
nome3 = str(input('Nome 3:'))
nome4 = str(input('Nome 2:'))

nomes = [nome1,nome2,nome3,nome4]

print(random.choice(nomes))
