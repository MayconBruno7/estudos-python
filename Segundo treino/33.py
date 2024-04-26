"""
-------------------------------------------------
DATA/HORA..: 13/06/2022 às 11:06
ESCRITO POR: Aldecir Fonseca
FINALIDADE.: 33) Faça um algoritmo que determine o maior 
                entre N números lidos. 
                - A condição de parada é a entrada de um valor 0.
                - Ou seja, o algoritmo deve ficar calculando 
                    o maior até que a entrada seja igual a 0 (ZERO).
-------------------------------------------------
"""

maior = 0

while True:

    num = int(input("Informe um numero:"))

    if num == 0:
        break
    else:
        num > 0 
        maior = num


print(f"O maior numero digitado é {maior}")

