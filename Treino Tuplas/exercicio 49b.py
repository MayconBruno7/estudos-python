"""
AUTOR.....: Maycon Bruno
DATA/HORA.: 17/08/2022 as 10:11
FINALIDADE: 49) Crie um programa que vai gerar dez números 
				aleatórios e colocar em uma tupla. 
				Depois disso mostre a listagem de números 
				gerados e também indique o menor e o maior 
				valor que estão na tupla.
"""

from random import randint

numeros = tuple(randint(0,100) for x in range(10))

maior = 0 
menor = 0 

print("Os valores aleatórios digitados foram:")

for x in range(len(numeros)):
	print(f"{numeros[x]}")

	if x == 0:
		maior = numeros[x]
		menor = numeros[x]

	else:
		if numeros[x] > maior:
			maior = numeros[x]
		if numeros[x] < menor:
			menor = numeros[x]

print('=' * 50)
print(f"O menor valor digitado é {menor}")
print(f"O maior valor digitado é {maior}")
print("=" * 50)