"""
AUTOR.....: Maycon Bruno 
DATA/HORA.: 03/09/2022 as 11:21
FINALIDADE: 3) Desenvolva um programa que efetue a leitura de 10
				elementos de uma matriz A tipo lista. Construir uma lista B
				de mesmo tipo, observando a seguinte lei de transformação:
				Se o valor do índice for par, o valor deverá ser multiplicado
				por 5; sendo impar, deverá ser somado com 5. ao final,
				mostrar o conteúdo das duas listas
"""
listA = []
listB = []

for x in range(10):
	listA.append(int(input('Informe um valor para a lista A: ')))

	if listA[x] % 2 == 0:
		listB.append(listA[x] * 5) 

	else:
		listB.append(listA[x] + 5)
	
print()
print('Exibindo as lista A:')
print()

for x in range(len(listA)):
	print(f'Lista A - {listA[x]}')

print()
print('Exibindo as lista B:')
print()

for x in range(len(listB)):
	print(f'Lista B - {listB[x]}')
