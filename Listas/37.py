"""
AUTOR......: Maycon Bruno
DATA/HORA..: 14/08/2022 as 10:56
FINALIDADE.:

			37) O cardápio de uma lancheira é o seguinte

				CODIGO	DESCRICAO						PREÇO
				100		Cachorro Quente					 5,00
				101		Hamburger						12,00
				102		xBurguer						14,50
				103		xEggBurguer						16,00
				104		Cachorrão de salsicha			11,50
				105		xTudo							18,00

			Escrever um algoritmo que leia o código do item pedido, a 
			quantidade e calcule o valor a ser pago por aquele lanche. 
			O usuário poderá pedir quantos lanches desejar. Se informado 
			quantidade zero interrompe a execução e exibe o total do pedido.
"""

while True:

	print("CODIGO		DESCRICAO					PREÇO")
	print("100			Cachorro Quente				 5,00")
	print("101			Hamburger					12,00")
	print("102			xBurguer					14,50")
	print("103			xEggBurguer					16,00")
	print("104			Cachorrão de salsicha		11,50")
	print("105			xTudo						18,00")
	print()

	codigo = int(input("Informe o codigo do produto:"))

	if codigo == 0:
		break

	elif codigo >= 100 and codigo <= 105:
		qtde = int(input("Informe a quantidade de produtos:"))

		valor = 0
		valorTotal = 0
		totalPedido = 0

		if codigo == 100:
			valor = 5
			valorTotal = (qtde * valor)

			print(f"O valor do produto é R$ {valor}, o valor total a ser pago pelos {qtde} lanches é R$ {valorTotal}")

		elif codigo == 101:
			valor = 12
			valorTotal = (qtde * valor)

			print(f"O valor do produto é R$ {valor}, o valor total a ser pago pelos {qtde} lanches é R$ {valorTotal}")

		elif codigo == 102:
			valor = 14.5
			valorTotal = (qtde * valor)

			print(f"O valor do produto é R$ {valor}, o valor total a ser pago pelos {qtde} lanches é R$ {valorTotal}")

		elif codigo == 103:
			valor = 16
			valorTotal = (qtde * valor)

			print(f"O valor do produto é R$ {valor}, o valor total a ser pago pelos {qtde} lanches é R$ {valorTotal}")

		elif codigo == 104:
			valor = 11.5
			valorTotal = (qtde * valor)

			print(f"O valor do produto é R$ {valor}, o valor total a ser pago pelos {qtde} lanches é R$ {valorTotal}")

		elif codigo == 105:
			valor = 18
			valorTotal = (qtde * valor)

			print(f"O valor do produto é R$ {valor}, o valor total a ser pago pelos {qtde} lanches é R$ {valorTotal}")

		totalPedido += valorTotal

	else:
		print("Favor inserir um código de produto válido.")

print("=" * 50)
print(f'O total a ser pago é R$ {totalPedido}')





