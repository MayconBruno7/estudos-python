"""
AUTOR......: Maycon Bruno
DATA/HORA.: 05/06/2022 as 16:24
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

for repeat in range(5):

	print('===================================')
	print('COGIGO	DESCRIÇÃO				% ')
	print('-----------------------------------')
	print('101		Gerente					10')
	print('102		Engenheiro				20')
	print('103		Técnico					30')
	print('???		Outros                  40')
	print('-----------------------------------')

	cargo = int(input("Informe o seu cargo de acordo com  a tabela:"))
	salario = float(input("Informe o seu salário:"))


	if cargo == 101:
		percReajuste = 10
	elif cargo == 102:
		percReajuste = 20
	elif cargo == 103:
		percReajuste = 30
	else: 
		percReajuste = 40

	novoSalario =  salario + round((salario * percReajuste) / 100,2)
	antesReajuste += salario
	depoisReajuste += novoSalario

	print("=" * 50)
	print(f"O seu salário era R$ {salario:>12.2f}") 
	print(f"O seu salário agora é R$ {novoSalario:>12.2f}") 
	print(f"O seu salário teve um aumento de R$ {novoSalario - salario:>12.2f}") 

print("=" * 50)
print(f"TOTAL DA FOLHA ANTES DO REAJUSTE  R$ {antesReajuste:>12.2f}")
print(f"TOTAL DA FOLHA DEPOIS DO REAJUSTE R$ {depoisReajuste:>12.2f}")
print("=" * 50)













