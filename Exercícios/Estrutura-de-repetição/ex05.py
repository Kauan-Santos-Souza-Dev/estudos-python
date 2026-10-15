# "Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário."

numero = int(input("Digite um numero"))

somatorio = 1
for num in range(numero,0,-1):
    somatorio *= num
    print(somatorio)
