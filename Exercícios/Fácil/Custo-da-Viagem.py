# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = int(input('Digite a distância da viagem em KM: '))
# Primeira Forma de Fazer

'''if km <= 200:
    preço = km * 0.50
else: 
    preço = km * 0.45'''

# Segunda Forma de Fazer 

preço = km * 0.50 if km <= 200 else km * 0.45
print(f'Você vai pagar {preço}')
