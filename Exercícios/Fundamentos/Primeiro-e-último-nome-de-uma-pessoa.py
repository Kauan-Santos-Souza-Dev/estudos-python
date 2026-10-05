#  Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip().lower()

primeiro = nome.split()[0]
ultimo = nome.split()[-1]

print(f'O primeiro nome é {primeiro} e o ultimo nome é {ultimo}')
