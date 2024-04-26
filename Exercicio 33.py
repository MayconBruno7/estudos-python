"""
-------------------------------------------------
DATA/HORA..: 08/07/2022 às 17:54
ESCRITO POR: Maycon Bruno
FINALIDADE.: 33) Faça um algoritmo que determine o maior 
                entre N números lidos. 
                - A condição de parada é a entrada de um valor 0.
                - Ou seja, o algoritmo deve ficar calculando 
                    o maior até que a entrada seja igual a 0 (ZERO).
-------------------------------------------------
"""
maior = 0

while True:

    print("=" * 50) 
    print("Para terminar o programa digite (0)")

    num = int(input("Informe um número:"))
        
    if num == 0:
        print("O programa foi encerrado!")
        break

    elif num == num:
        maior = num

    elif num > maior: 
        maior = num


print("=" * 50)
print(f"O maior numero digitado é {maior}")

