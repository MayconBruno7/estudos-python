"""
AUTOR.....: Maycon Bruno
DATA/HORA.: 22/09/2022 as 23:04
FINALIDADE: (4,0 pontos). Solicite ao usuário que informe 10 
					números inteiros em uma tupla. Ao final 
					exiba os seguintes dados sobre os números informados: 
			•A soma dos números.
			•A média dos números.
			•O menor dos números e seu índice na tupla.
			•O índice na tupla para o menor dos números pares informado.
"""

numeros = tuple(int(input("Informe um número inteiro para índice " + str(x) + ": ")) for x in range(10))

soma = 0
indMenor = -1
indMenorPar = -1

for x in range(len(numeros)):

	soma += numeros[x]
	
	if x == 0:
		indMenor = x
	else:
		if numeros[x] < numeros[indMenor]:
			indMenor = x

	if (numeros[x] % 2) == 0:
		if indMenorPar == -1:
			indMenorPar = x
		else:
			if numeros[x] < numeros[indMenorPar]:
				indMenorPar = x

print()
print('=' * 50)
print(f'A soma dos numeros digitados é {soma}')
print(f'A media dos numeros digitados é {soma / len(numeros)}')
print(f'O menor dos numeros digitados foi {numeros[indMenor]} e esta localizado no indice {indMenor}')
print(f'O indice em que está localizado o menor número par digitado é {indMenorPar}')

