# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO". 

my_str = str(input('Qual cidade você nasceu:'))

trimmed_my_str = my_str.strip().lower()
starts_with_santo = trimmed_my_str.startswith('santo')


print(starts_with_santo)  
