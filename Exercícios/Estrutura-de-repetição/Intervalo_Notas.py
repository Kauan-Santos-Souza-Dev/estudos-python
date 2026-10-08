# FAÇA UM PROGRAMA QUE PEÇA UMA NOTA, ENTRE ZERO E DEZ. mOSTRE UMA MENSAGEM CASO O VALOR SEJA INVÁLIDO E CONTINUE PEDINDO ATÉ QUE O 
# USUÁRIO INFORME UM VALOR VÁLIDO.


# Preciso percorrer o input com um While para verificar se o input é um numero entre 0 e 10.

# Forma de resolver 1:

#while True:
#    try:
#        nota = int(input('Informe uma nota entre 0 e 10: '))
#       if nota >=0 and nota <= 10:  
#            break 
#        else:
#           print('A nota deve estar entre 0 e 10')
#   except ValueError:
#        print("Erro: Por favor, digite um número inteiro válido.")
#
#print(f'Você digitou a nota válida: {nota}')

            
while True:
    nota = int(input('Informe uma nota entre 0 e 10: '))
    if nota < 0 or nota > 10:
        print('Nota inválida, tente Novamente')
        continue
    else:
        print('Nota Valida') 
        break
