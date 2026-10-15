
paisA = 80000
paisB = 200000  
anos = 0

while paisA < paisB:
    paisA += (paisA * 3) / 100
    paisB += (paisB * 1.5) / 100
    anos +=1
    if paisA > paisB:
        print(anos)
        print(paisA)
        print(paisB)
        break






# "Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de um país B seja de 200.000 habitantes com uma taxa de crescimento de 1,5%,
#  faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse 
# ou iguale a população do país B, mantidas as taxas de crescimento.




