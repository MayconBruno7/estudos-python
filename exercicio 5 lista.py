"""
AUTOR.....: Maycon Bruno 
DATA/HORA.: 03/09/2022 as 11:39
FINALIDADE: 5) Ler duas listas A e B com 20 elementos. 
			Construir uma lista C, onde cada elemento 
			de C é a subtração do elemento correspondente
			de A com B. Apresentar as listas A, B e C.
"""

listaA = []
listaB = []
listaC = []

for x in range(6):

    listaA.append(int(input('Informe um valor para a lista A: ')))
    listaB.append(int(input('Informe um valor para a lista B: ')))

for x in range(len(listaA)):

    listaC.append(listaA[x] - listaB[x])

print ()
print('Exibindo as listas:')
print('Lista A  Lista B Lista C')

for x in range(len(listaA)):

    print(f'{listaA[x]:>6.0f}', end="   ")
    print(f'{listaB[x]:>6.0f}', end="   ")
    print(f'{listaC[x]:>6.0f}')