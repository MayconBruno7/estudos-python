"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final
, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

"""

listaNum = []

maior = 0 
menor = 0

for l in range(0, 5):

	listaNum.append(int(input(f"Informe um valor para a posiçâo {l}: ")))

	if l == 0:
		maior = listaNum[l]
		menor = listaNum[l]

	else:
		if listaNum[l] > maior:
			maior = listaNum[l]

		if listaNum[l] < menor:
			menor = listaNum[l]

print('=' * 50)
print(f'Você digitou os valores: {listaNum}')
print(f'O maior valor digitado foi {maior} e esta na posição', end=' ')

for i, v in enumerate(listaNum):

	if v == maior:
		print(f'{i}', end=' ')
print()

print(f'O menor valor digitado foi {menor} e está na posição', end=' ')

for i, v in enumerate(listaNum):

	if v == menor:
		print(f'{i}', end=' ')
print()

