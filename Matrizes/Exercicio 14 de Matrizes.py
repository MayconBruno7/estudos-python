"""
Autor: Maycon Bruno
Data: 03/10/ 2022 ás 21:14
   14)	Elabore um algoritmo que leia uma matriz de 5 linhas e 3 colunas. No final,
        imprima o maior e o menor valor, 
        e os dados informados na matriz.

"""

matrizValores = []
valores       = []

ilMaior = - 1 
icMaior = - 1

ilMenor = - 1
icMenor = - 1

for linhas in range(5):
    for colunas in range(3):
        valores.append(int(input('Informe o valor' + str(linhas + 1)+ ': ')))

    matrizValores.append(valores[:])
    valores.clear()

for linhas in range(len(matrizValores)):
    for colunas in range(len(matrizValores[linhas])):
        print(f'{matrizValores[linhas][colunas]:>5.0f}', end=' ')

        if linhas == 0 and colunas == 0:
            ilMaior = linhas
            icMaior = colunas

            ilMenor = linhas
            icMenor = colunas

        else:
            if matrizValores[linhas][colunas] < matrizValores[ilMenor][icMenor]:
                ilMenor = linhas
                icMenor = colunas

            if matrizValores[linhas][colunas] > matrizValores[ilMaior][icMaior]:
                ilMaior = linhas
                icMaior = colunas

    print()

print()
print('Exibindo o menor e o maior valor')
print()
print(f'O menor valor é {matrizValores[ilMenor][icMenor]} e está no indice: Linha {ilMenor} e coluna {icMenor}.')