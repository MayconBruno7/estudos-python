"""
AUTOR.....: Maycon Bruno 
DATA/HORA.: 03/09/2022 as 15:52
FINALIDADE: 8) Ler uma lista A com 15 elementos. Construir uma lista B de
            mesmo tipo, sendo que cada elemento da matriz B seja a
            fatorial do elemento correspondente a lista A. Apresentar a
            lista B.

"""

listaA = []
listaB = []

for x in range(15):

    print(f'Indice - {x}')
    listaA.append(int(input('Informe um valor para a lista A: ')))

    listaB.append(1)

    for y in range(1, listaA[x] + 1):

        listaB[x] = listaB[x] * y

print()
print('Apresentando a lista:')
print('Lista A  Lista B')

for x in range(len(listaA)):

    print(f'{listaA[x]:>6.0f}', end='   ')
    print(f'{listaB[x]:>6.0f}')
