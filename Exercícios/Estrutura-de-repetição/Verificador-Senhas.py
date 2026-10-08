# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário
# Mostrando uma mensagem de erro e voltando a pedir as informações.


while True:
    nome = input('Digite seu nome: ').lower()
    senha = input('Digite sua senha: ').lower()

    if nome == senha:
        print('Dados não podem ser iguais, tente novamente.')
        continue
    else:
        print('Senha Cadastrada')
        break
