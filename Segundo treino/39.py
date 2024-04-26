"""
AUTO......: Maycon Bruno
DATA/HORA.: 15/08/2022 as 15:38
FINALIDADE:
			39) Escrever um algoritmo que leia o nome e o sexo de 15
			pessoas, ao final determine:
				• Total de homens e de mulheres.
				• A mulher mais nova
				• O homem mais velho
				• A média de idade de todas as pessoas
"""

totHomens = 0 
totMulheres = 0 

mulherNovaIdade = 0
homemVelhoIdade = 0 

mulherNovaNome = ''
homemVelhoNome = ''

mediaIdade = 0 

for x in range (3):

	name = input("Informe um nome:")

	while True:

		print("Digite (M) para masculino e (F) para feminino.")

		sexo = input("Informe o sexo:")

		if sexo.upper() == "M" or sexo.upper() == "F":
			break
		else:
			print("Sexo inválido, favor inserir um sexo válido!")

	idade = int(input("Informe a idade:"))
		
	if sexo.upper() == "M":
		totHomens += 1

		if idade > homemVelhoIdade or totHomens == 1:
			homemVelhoIdade = idade
			homemVelhoNome = name 

	elif sexo.upper() == "F":
		totMulheres += 1

		if idade < mulherNovaIdade or totMulheres == 1:
			mulherNovaIdade = idade 
			mulherNovaNome = name

	mediaIdade += idade 


print()
print("=" * 50)
print(f"O total de mulheres é {totMulheres} e o total de homens é {totHomens}")
print(f"A mulher mais nova é {mulherNovaNome} tem {mulherNovaIdade} anos.")
print(f"A média de idade de todas as pessoas é de {(mediaIdade) / 3}")


