"""
AUTOR.....: Maycon Bruno 
DATA/HORA.: 03/09/2022 as 15:32
FINALIDADE: 6) Ler duas listas A e B com 15 elementos cada. Construir uma
            lista C, sendo está a junção das duas outras listas. Desta
            forma, C deverá ter o dobro de elementos, ou seja, 30.
            Apresentar a lista C
"""

listaA = []
listaB = []
listaC = []

for x in range(15):
    
    print(f'Preencha os numeros para o indice {x}')
    listaA.append(int(input('Informe um valor para a lista A: ')))
    listaB.append(int(input('Informe um valor para a lista B: ')))

for x in range(len(listaA)):
    
    listaC.append(listaA[x])

for x in range(len(listaB)):

    listaC.append(listaB[x])

print()
print('ListaA  ListaB  ListaC')
print()

for x in range(len(listaC)):

    if x < len(listaA):

        print(f'{listaA[x]:>6.0f}', end="   ")
        print(f'{listaB[x]:>6.0f}', end="   ")

    else:
        print(' ' * 14, end="    ")

    print(listaC[x])