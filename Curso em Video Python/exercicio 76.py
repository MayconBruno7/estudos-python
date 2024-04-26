"""
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus 
respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados
 em forma tabular.
""" 

listagem = ('Lápis', 1.75,'Borracha', 2, 'Caderno', 30, 'Lapiseira', 3, 'Caneta', 1.5, 'Bolsinha', 6,
 'Mochila', 75)

print("=" * 50)
print(f'{"Listagem de preços":^40}')
print("=" * 50)

for pos in range(len(listagem)):
	if pos % 2 == 0: 
		print(f"{listagem[pos]:.<30}", end='')
	else:
		print(f"R$ {listagem[pos]:>7.2f}")

