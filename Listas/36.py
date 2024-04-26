"""
AUTO......: Maycon Bruno
DATA/HORA.: 14/08/2022 as 10:41
FINALIDADE:
			36) Faça um algoritmo que receba a idade de 15 pessoas e mostre
			mensagem informando “maior de idade” e “menor de idade”
			para cada pessoa. Considere a idade a partir de 18 anos como
			maior de idade. Ao final apresente quantos % das pessoas
			informadas são “maior de idade” e “menor de idade”.
"""

maiorIdade = 0 
menorIdade = 0 

qtdMenor = 0 
qtdMaior = 0

for x in range(15):

	idade = int(input("Informe a idade:"))

	if idade >= 18:
		maiorIdade = idade 
		qtdMaior += 1
	else:
		menorIdade = idade 
		qtdMenor += 1

print()
print("=" * 50)
print(f"A maior idade digitada foi de {maiorIdade} anos.")
print(f"A menor idade digitada foi de {menorIdade} anos.")
print(f"A porcentagem de de pessoas que atingiram a maior idade é de {(qtdMaior * 100) / 15:<1.2f} %.")
print()
print("=" * 50)
