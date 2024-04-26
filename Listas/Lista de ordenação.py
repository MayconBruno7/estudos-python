"""
AUTOR.....: Maycon Bruno
DATA/HORA.: 24/09/2022 as 13:06
FINALIDADE: Criar uma lista de ordenação para 5 valores utilizando o metodo bolha.

"""

listaA = list()

print()
print('Ordenando os valores com o metodo bolha:')
print()

for x in range(5):

    listaA.append(int(input('Informe os valores desejados: ')))

for x in range(1, len(listaA)):
    for y in range(len(listaA) - 1, 0, -1):
        if listaA[y] < listaA[y - 1]:
            aux          = listaA[y]
            listaA[y]    = listaA[y-1]
            listaA[y- 1] = aux

print()
print('Exibindo os numeros já ordenados:')
print()

for x in range(len(listaA)):
    print(f"{listaA[x]}")
