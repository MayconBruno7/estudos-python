"""
-------------------------------------------------
DATA/HORA..: 12/07/2022 às 14:59
ESCRITO POR: Maycon Bruno
FINALIDADE.: 36) Faça um algoritmo que receba a idade de 15 pessoas e mostre
            mensagem informando “maior de idade” e “menor de idade”
            para cada pessoa. Considere a idade a partir de 18 anos como
            maior de idade. Ao final apresente quantos % das pessoas
            informadas são “maior de idade” e “menor de idade”.e).
-------------------------------------------------
"""

maiorIdade = 0
menorIdade = 0

QtdMaiorIdade = 0
QtdMenorIdade = 0

for x in range(5):

    idade = int(input("Informe a idade: "))

    if idade >= 18:
        QtdMaiorIdade += 1
        if idade > maiorIdade:
            maiorIdade = idade 
           

    else:
        QtdMenorIdade += 1
        menorIdade = idade
        

print("=" * 50)
print(f'A maior idade digitada foi {maiorIdade}')
print(f'A menor idade digitada foi {menorIdade}')
print(f"A porcentagem de pessoas de maior idade é: {round((QtdMaiorIdade * 100) / 5)}")
print(f"A porcentagem de pessoas de menor idade é: {round((QtdMenorIdade * 100) / 5)}")
print("=" * 50)



