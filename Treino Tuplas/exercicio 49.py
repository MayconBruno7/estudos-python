"""
AUTOR.....: Maycon Bruno
DATA/HORA.: 17/08/2022 as 09:57
FINALIDADE: 49) Crie um programa que vai gerar dez números 
				aleatórios e colocar em uma tupla. 
				Depois disso mostre a listagem de números 
				gerados e também indique o menor e o maior 
				valor que estão na tupla.
"""

from random import randint

numeros = ( randint(0, 100), 
			randint(0, 100),
			randint(0, 100), 
			randint(0, 100),
			randint(0, 100),
			randint(0, 100),
			randint(0, 100),
			randint(0, 100),
			randint(0, 100),
			randint(0, 100)
)

maior = 0
menor = 0

print("Os valores aleatórios foram:")

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

print("-" * 30)
print(f"O menor valor sorteado foi {menor}")
print(f"O maior valor sorteado foi {maior}")

