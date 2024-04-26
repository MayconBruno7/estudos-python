"""
AUTOR.....: Maycon Bruno
DATA/HORA.: 17/08/2022 as 13:55
FINALIDADE: Exemplo de busca de valores inteiros

"""

from random import randint

numeros = tuple(randint(0, 100) for x in range(20)) 

print("=" * 50)

for x in range(len(numeros)):
	print(f"{numeros[x]}", end=", ")

print('')
print("=" * 40)

while True:

	busca = int(input("Informe o numero que deseja buscar:"))

	if busca == 0:
		break

	achou = False 

	for n in range(len(numeros)):
		if numeros[n] == busca:
			print(f"O numero {busca} está localizado no indice {n}")
			achou = True

	if not achou:
		print("Número não localizado")

	print("=" * 50)

