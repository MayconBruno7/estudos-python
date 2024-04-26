"""
AUTO......: Maycon Bruno
DATA/HORA.: 15/08/2022 as 14:06
FINALIDADE:
			38) Uma empresa concederá um aumento de salário aos seus
			funcionários, variável de acordo com o cargo, conforme a tabela
			abaixo. Faça um algoritmo que leia o salário e o cargo de 5 
			funcionário e calcule o novo salário. Se o cargo do funcionário 
			não estiver na tabela, ele deverá, então, receber 40% de aumento. 
			Mostre o salário antigo, o novo salário e a diferença para cada 
			funcionário. No final apresente o valor total da folha antes 
			do reajuste e depois do reajuste.

			COGIGO	DESCRIÇÃO				%
			101		Gerente					10
			102		Engenheiro				20
			103		Técnico					30
"""

antesReajuste = 0 
depoisReajuste = 0 

for x in range(5):

	salario = float(input("Favor informar o salário do funcionário:"))

	print("COGIGO		DESCRIÇÃO				 %")
	print("101			Gerente					10")		
	print("102			Engenheiro				20")	
	print("103			Técnico					30")

	cargo = int(input("Favor informar o cargo de acordo com o codigo descrito acima:"))

	if cargo == 101:
		reajuste = 10
	elif cargo == 102:
		reajuste = 20
	elif cargo == 103:
		reajuste = 30
	else:
		reajuste = 40

	novoSalario = salario + (salario * reajuste) / 100
	antesReajuste += salario 
	depoisReajuste += novoSalario

	print()
	print("=" * 50)
	print(f"Salário antes do reajuste {salario}")
	print(f"Total do reajuste {(novoSalario - salario)}")
	print(f"Salário do reajuste {novoSalario}")
	print()
	print("=" * 50)


print()
print("=" * 50)
print(f"Total da folha antes do reajuste {antesReajuste}.")
print(f"Total da folha após o reajuste {depoisReajuste}")
print()
print("=" * 50)