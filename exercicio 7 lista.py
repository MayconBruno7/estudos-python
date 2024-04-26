"""
AUTOR.....: Maycon Bruno 
DATA/HORA.: 03/09/2022 as 15:52
FINALIDADE: 7) Ler 20 elementos em uma lista A e construir uma lista B de
            mesma dimensão com os mesmos elementos de A, sendo
            que estes deverão estar invertidos, ou seja, o primeiro
            elemento de A passa a ser o último de B, o segundo
            elemento de A passa a ser o penúltimo de B e assim por
            diante. Apresentar as listas A e B
"""

listaA = []
listaB = []

for x in range(20):

    listaA.append(int(input('Informe os valores para a lista A:')))

for x in range(len(listaA) -1, -1, -1):

    listaB.append(listaA[x])

print()
print('ListaA   ListaB')
print()

for x in range(len(listaA)):

    print(f'{listaA[x]:>6.0f}', end="   ")
    print(f'{listaB[x]:>6.0f}')

print('=' * 50) 


