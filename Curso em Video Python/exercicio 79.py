"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre
-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos
 todos os valores únicos digitados, em ordem crescente. 

"""

valores = list()

while True:

	n = int(input('Digite um valor:'))

	if n not in valores:
		valores.append(n)
		print("Valor adicionado com sucesso!")
	else:
		print("Valor duplicado, não vou adicionar!")

	r = str(input('Quer continuar? [S/N]'))

	if r in 'Nn':
		break

print('=' * 50)
valores.sort()
print(f'Você digitou os valores {valores}')