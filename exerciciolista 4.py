"""
AUTOR.....: Maycon Bruno 
DATA/HORA.: 03/09/2022 as 11:21
FINALIDADE: 4) Desenvolver um programa que efetue a 
			leitura de 5 elementos de uma matriz A do 
			tipo lista. No final, apresente o total 
			da soma de todos os elementos que sejam 
			impares.
"""

listaA = []
somaImpares = 0

for x in range(5):

    listaA.append(int(input('Informe os valores para a lista A: ')))

    if (listaA[x] % 2) != 0:
        somaImpares += listaA[x]

print()
print(f'Apresentando a soma dos numeros impares digitados')
print(f'Soma = {somaImpares}')
