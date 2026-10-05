""" Faça um programa que faça cinco perguntas para uma pessoa sobre um crime.
    O programa deve no final emitir uma classificação sobre a participação da pessoa no crime:
    - Se a pessoa responder positivamente a 2 questões:
    classificada como "suspeita" - Entre 3 e 4 questões: classificada como "cúmplice" - 5 questões: 
    classificada como "assassino" - Caso contrário: classificada como "inocente" """


pergunta1 = str(input('Telefonou para a vítima?')).strip().lower()
pergunta2 = str(input('Esteve no locão da vítima?')).strip().lower()
pergunta3 = str(input('Mora perto da vítima?')).strip().lower()
pergunta4 = str(input('Devia para a vítima?')).strip().lower()
pergunta5 = str(input('Ja trabalhou para a vitima?')).strip().lower()

a = pergunta1 in ['sim', 's', 'true']
b = pergunta2 in ['sim', 's', 'true']
c = pergunta3 in ['sim', 's', 'true']
d = pergunta4 in ['sim', 's', 'true']
e = pergunta5 in ['sim', 's', 'true']



if a + b + c + d + e == 5:
    print('Assassino')
elif a + b + c + d + e >= 3:
    print('Cúmplice')
elif a + b + c +d + e == 2:
    print('Suspeito')
else:
    print('Inocente')

# Segunda forma de fazer: Forma do Vídeo
'''
analise = 0

lista = ['Telefonou para a vítima?',
'Esteve no locão da vítima?',
'Mora perto da vítima?',
'Devia para a vítima?',
'Ja trabalhou para a vitima?']

for pergunta in lista:
    resposta = input(pergunta)
    resposta = 1 if resposta == 's' else 0
    analise += resposta

if analise == 5:
    print('Assasino')
elif analise >= 3:
    print('Cumplice')
elif analise == 2:
    print('Ssupeito')
else:
    print('inocente')
'''
