"""
-------------------------------------------------
DATA/HORA..: 08/07/2022 às 18:10
ESCRITO POR: Maycon Bruno
FINALIDADE.: 34) Leia 10 valores inteiros e determine:  
                    - Qual é o menor valor informado;
                    - Qual é o maior valor informado;
                    - A soma dos valores informados;
                    - A média dos valores informados.
-------------------------------------------------
"""

maior = 0 
menor = 0
soma = 0
media = 0

for x in range(10):

    num = int(input("Informe um número inteiro:"))

    if x == 0:
        maior = num 
        menor = num
    elif num > maior:
        maior = num 
    elif num < menor:
        menor = num

    soma += num 


print("=" * 50)
print(f"O maior número informado é {maior}")
print(f"O menor número informado é {menor}")
print(f"A soma dos números informados é {soma}")
print(f"O média dos números informados é {(soma / 10):<12.2f}")
print("=" * 50)