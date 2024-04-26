"""
AUTOR......: Maycon Bruno
DATA/HORA.: 05/06/2022 as 17:11
FINALIDADE:
			39) Escrever um algoritmo que leia o nome e o sexo de 15
			pessoas, ao final determine:
				• Total de homens e de mulheres.
				• A mulher mais nova
				• O homem mais velho
				• A média de idade de todas as pessoas
"""
qtdHomens = 0
qtdMulheres = 0

mulherNova = 0
homemVelho = 0

homemVelhoNome = ''
mulherNovaNome = ''

somaIdade = 0 

for repeat in range(4):

	nome = input("Informe o seu nome:")
	
	while True:

		sexo = input("Informe o seu sexo:")

		if sexo.upper() == "M" or sexo.upper() == "F":
			break

		else:
			print("Por favor, informe um sexo válido!")

	idade = int(input("Informe a sua idade:"))

	if sexo.upper() == "M":
		qtdHomens += 1

		if idade > homemVelho or qtdHomens:
			homemVelho = idade
			homemVelhoNome = nome

	elif sexo.upper() == "F":
		qtdMulheres += 1

		if idade < mulherNova or qtdMulheres:
			mulherNova = idade
			mulherNovaNome = nome

	somaIdade += idade

print("=" * 50)
print(f"Total de homens informados é {qtdHomens}")
print(f"Total de mulheres informados é {qtdMulheres}")
print(f"A mulher mais nova é {mulherNovaNome}, e tem {mulherNova} anos(s)")
print(f"O homem mais velho é {homemVelhoNome}, e tem {homemVelho} anos(s)")
print(f"A média da idade das pessoas informadas é {round((somaIdade / (repeat + 1)), 1)}")
print("=" * 50)





		

		
