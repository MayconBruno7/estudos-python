"""
Autor: Maycon Bruno
Data: 03/10/ 2022 ás 21:14
   14)	Elabore um algoritmo que leia uma matriz de 5 linhas e 3 colunas. No final,
        imprima o maior e o menor valor, 
        e os dados informados na matriz.

"""

from argparse import _MutuallyExclusiveGroup


matrizValores = []
valores       = []

maior = - 1 
menor = - 1

for linhas in range(5):
    for colunas in range(3):
        valores.append(int(input('Informe o valor (linha) ' + str (linhas + 1) + ': ')))
    
    matrizValores.append(valores[:])
    valores.clear()

print()
for linhas in range(len(matrizValores)):
    for colunas in range(len(matrizValores[linhas])):
        print(f'{matrizValores[linhas][colunas]:>5.0f}', end="  ")

        if linhas == 0 and colunas == 0:
            maior = matrizValores[linhas][colunas]
            menor = matrizValores[linhas][colunas]

        else:    
            if matrizValores[linhas][colunas] < menor:
                menor = matrizValores[linhas][colunas]

            if matrizValores[linhas][colunas] > maior:
                maior = matrizValores[linhas][colunas]

        print()

print()
print('Exibindo o maior e o menor valor adicionado a matriz')
print()
print(f'O menor valor adicionado a matriz foi {menor}')
print(f'O maior valor adicionado a matriz foi {maior}')
print()